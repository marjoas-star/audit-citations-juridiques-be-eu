"""Packaging tests: no legal validity or source availability is inferred."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('renderer', Path(__file__).parents[1] / 'scripts/render_report.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


def sample():
    return dict(title='Rapport de test fictif', document='Document synthétique', date='24 septembre 2026',
                report_metadata=dict(established_at='2026-09-24T14:00:00+02:00', timezone='Europe/Brussels', precision='second', report_version='v1', checks_started_on='2026-09-23', checks_completed_on='2026-09-24', legal_reference='Non précisée'), version='test', scope='Cas synthétique sans recherche juridique.', summary='Contrôle de présentation uniquement.',
                limitations=['Aucune preuve juridique.'], method=['Données entièrement fictives.'], quotations=[],
                records=[dict(id='R1', source_id='S1', title='Référence fictive', original='Référence fictive',
                              checked='Non établie', location='Page 1', status='NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES',
                              checks=[], limits='Source inaccessible.', sources=[])])


class ReportTests(unittest.TestCase):
    def test_verified_without_evidence_is_rejected(self):
        d=sample();d['records'][0]['status']='VERIFIED'
        with self.assertRaises(ValueError): renderer.validate(d)

    def test_duplicate_occurrence_is_rejected(self):
        d=sample();d['records'].append(copy.deepcopy(d['records'][0]))
        with self.assertRaises(ValueError): renderer.validate(d)

    def test_counts_distinguish_occurrences_and_sources(self):
        d=sample();r=copy.deepcopy(d['records'][0]);r['id']='R2';d['records'].append(r)
        nodes=list(renderer.sections(renderer.validate(d)))
        stats=next(value for kind,value in nodes if kind=='stats')
        self.assertEqual([x[0] for x in stats], ['2','1','0'])

    def test_translation_is_not_exact_by_default(self):
        d=sample();d['quotations']=[dict(id='Q1',record_id='R1',title='Traduction',location='Page 1',
            status='NOT_APPLICABLE_TRANSLATION',integrity='NOT_VERIFIABLE',comparison='Test',context='Test')]
        with self.assertRaises(ValueError): renderer.validate(d)

    def test_long_card_survives_pdf_pagination_and_has_no_internal_status(self):
        from pypdf import PdfReader
        d=sample();d['records'][0]['notes']=['Texte synthétique de vérification de la pagination. ' * 180 + 'FIN DU CONTROLE LONG.']
        nodes=list(renderer.sections(renderer.validate(d)))
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/'report.pdf';renderer.write_pdf(nodes,p,d)
            text='\n'.join(page.extract_text() for page in PdfReader(p).pages)
            self.assertIn('FIN DU CONTROLE LONG.', ' '.join(text.split()))
            self.assertIn('Source inaccessible.', text)
            self.assertNotIn('NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES', text)
            renderer.write_markdown(nodes,p.with_suffix('.md'))
            self.assertIn('FIN DU CONTROLE LONG.',p.with_suffix('.md').read_text())


if __name__=='__main__': unittest.main()
