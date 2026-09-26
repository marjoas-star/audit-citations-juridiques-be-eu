# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
"""Presentation tests: dates, combined labels, closing sections and the documented example."""
from datetime import datetime, timedelta
import json
from pathlib import Path
from zoneinfo import ZoneInfo
import tempfile
import unittest

from test_render_report import renderer, sample


class ClarityTests(unittest.TestCase):
    def test_future_establishment_rejected(self):
        future = (datetime.now(ZoneInfo('Europe/Brussels')) + timedelta(days=2)).replace(microsecond=0)
        d = sample(); m = d['report_metadata']
        m['established_at'] = future.isoformat(); m['checks_completed_on'] = future.date().isoformat()
        with self.assertRaises(ValueError): renderer.validate(d)
        d = sample(); m = d['report_metadata']
        m['precision'] = 'day'; m['established_at'] = future.date().isoformat(); m['checks_completed_on'] = future.date().isoformat()
        with self.assertRaises(ValueError): renderer.validate(d)

    def test_correct_reference_with_deviating_quotation_is_labelled(self):
        d = sample(); r = d['records'][0]
        r.update(status='VERIFIED', checks=['Intitulé'], sources=[dict(label='Source', url='https://example.org', locator='art. 1', language='FR')])
        d['quotations'] = [dict(id='Q1', record_id='R1', title='Citation', location='Page 1', status='MINOR_DEVIATION',
                                integrity='FAITHFUL', comparison='Un mot diffère.', context='Sans effet.')]
        text = str(list(renderer.sections(renderer.validate(d))))
        self.assertIn('Référence vérifiée · citation : écart mineur', text)

    def test_method_and_full_disclaimer_have_headings(self):
        nodes = list(renderer.sections(renderer.validate(sample())))
        headings = [v for k, v in nodes if k == 'h2']
        self.assertIn('Méthode suivie', headings); self.assertIn('Avertissement', headings)
        callout = next(v for k, v in nodes if k == 'callout')
        for words in ('interfaces', 'vérification humaine', 'erronée'):
            self.assertIn(words, callout)

    def test_skill_version_field(self):
        d = sample(); d['skill_version'] = d.pop('version')
        self.assertIn('Version du skill : test', str(list(renderer.sections(renderer.validate(d)))))
        del d['skill_version']
        with self.assertRaises(ValueError): renderer.validate(d)

    def test_documented_example_is_valid(self):
        path = Path(__file__).parents[1] / 'templates/example-audit.json'
        renderer.validate(json.loads(path.read_text(encoding='utf-8')))

    def test_supplied_guillemets_are_not_doubled(self):
        self.assertEqual(renderer.bare_excerpt('« Texte. »'), 'Texte.')
        self.assertEqual(renderer.bare_excerpt('Texte « cité » ici'), 'Texte « cité » ici')

    def test_closing_block_is_kept_together(self):
        kinds = [k for k, v in renderer.sections(renderer.validate(sample()))]
        start, end = kinds.index('keep_start'), kinds.index('keep_end')
        self.assertLess(start, kinds.index('callout')); self.assertGreater(end, kinds.index('callout'))

    def test_skill_md_states_current_version(self):
        root = Path(__file__).parents[1]
        version = (root / 'VERSION').read_text(encoding='utf-8').strip()
        self.assertIn('Version du skill : `' + version + '`', (root / 'SKILL.md').read_text(encoding='utf-8'))

    def test_example_is_fictitious(self):
        text = (Path(__file__).parents[1] / 'templates/example-audit.json').read_text(encoding='utf-8')
        for marker in ('Schrems', 'Post Danmark', 'Dupont-Verhaegen', 'Google Spain', 'Salduz', '29 juillet 1991', 'Rantos', 'ByteDance'):
            self.assertNotIn(marker, text)

    def test_pdf_replaces_glyphs_missing_from_font(self):
        self.assertEqual(renderer.pdf_text('C\u201123/14\u202f§'), 'C-23/14\u00a0§')

    def test_skill_description_fits_app_preview(self):
        # The Claude app preview shows the first 500 characters of the description.
        import re
        text = (Path(__file__).parents[1] / 'SKILL.md').read_text(encoding='utf-8')
        desc = ' '.join(re.search(r'description: >\n(.*?)\n---', text, re.S).group(1).split())
        self.assertLessEqual(len(desc), 500)

    def test_report_languages(self):
        french_only = ('Référence vérifiée', 'Ce qu’il faut retenir', 'Avertissement', 'Méthode suivie', 'Sources consultées')
        for code, marker in (('nl', 'Wat u moet onthouden'), ('de', 'Das Wichtigste'), ('en', 'Key points')):
            d = sample(); d['report_language'] = code
            text = str(list(renderer.sections(renderer.validate(d))))
            self.assertIn(marker, text)
            for word in french_only:
                self.assertNotIn(word, text)
            with tempfile.TemporaryDirectory() as tmp:
                renderer.write_pdf(list(renderer.sections(d)), Path(tmp) / 'r.pdf', d)
        d = sample(); d['report_language'] = 'es'
        with self.assertRaises(ValueError): renderer.validate(d)

    def test_report_ends_with_feedback_invitation_in_its_language(self):
        for code in ('fr', 'nl', 'de', 'en'):
            d = sample(); d['report_language'] = code
            nodes = list(renderer.sections(renderer.validate(d)))
            self.assertEqual(nodes[-2][0], 'feedback', code)
            urls = [url for _, url in nodes[-2][1] if url]
            self.assertEqual(urls, [renderer.FEEDBACK_FORMS[code], renderer.REPO_URL])
            self.assertEqual(len(set(renderer.FEEDBACK_FORMS.values())), 4)
            with tempfile.TemporaryDirectory() as tmp:
                renderer.write_markdown(nodes, Path(tmp) / 'r.md')
                self.assertIn('](' + renderer.FEEDBACK_FORMS[code] + ')', (Path(tmp) / 'r.md').read_text(encoding='utf-8'))

    def test_reference_with_error_shown_once_and_proofs_not_repeated(self):
        d = sample()
        nodes = list(renderer.sections(renderer.validate(d)))
        self.assertEqual(sum(1 for k, v in nodes if k == 'p' and v.startswith('Référence citée')), 1)
        links = [v for k, v in nodes if k == 'link']
        self.assertEqual(len(links), len(set(links)))
        self.assertEqual(renderer.page_target(d), 6)

    def test_long_summary_flagged(self):
        d = sample(); d['summary'] = 'mot ' * 130
        self.assertTrue(any('synthèse' in w for w in renderer.length_warnings(d)))

    def test_quotation_of_other_version_not_shown_as_preserved(self):
        d = sample(); r = d['records'][0]
        r.update(status='VERIFIED', checks=['Intitulé'], sources=[dict(label='Source', url='https://example.org', locator='art. 1', language='FR')])
        d['quotations'] = [dict(id='Q1', record_id='R1', title='Citation', location='Page 1', status='EXACT', integrity='FAITHFUL',
                                applicable_version=False, comparison='Mots de la version antérieure.', context='Portée changée.')]
        text = str(list(renderer.sections(renderer.validate(d))))
        self.assertIn('Texte d’une autre version que celle applicable', text)
        self.assertNotIn('Sens préservé', text)
        self.assertIn('citation : autre version', text)

    def test_confirmed_references_go_to_compact_annex(self):
        d = sample(); r = d['records'][0]
        r.update(status='VERIFIED', checks=['Intitulé'], limits='', sources=[dict(label='Source', url='https://example.org', locator='art. 1', language='FR')])
        nodes = list(renderer.sections(renderer.validate(d)))
        self.assertIn(('h1', 'Références confirmées sans réserve'), nodes)
        self.assertNotIn(('h2', 'Référence fictive'), nodes)

    def test_summary_counts_must_match(self):
        d = sample(); d['summary'] = 'Onze sources distinctes examinées.'
        with self.assertRaises(ValueError): renderer.validate(d)
        d['summary'] = 'Une seule source distincte : 1 sources distinctes.'
        renderer.validate(d)


if __name__ == '__main__':
    unittest.main()
