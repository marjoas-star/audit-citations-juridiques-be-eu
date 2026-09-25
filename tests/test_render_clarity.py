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


if __name__ == '__main__':
    unittest.main()
