# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
"""Presentation tests: dates, combined labels, closing sections and the documented example."""
from datetime import datetime, timedelta
import json
from pathlib import Path
from zoneinfo import ZoneInfo
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


if __name__ == '__main__':
    unittest.main()
