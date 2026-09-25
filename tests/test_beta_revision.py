"""Synthetic invariants, not a legal benchmark."""
import copy
import tempfile
import unittest
from pathlib import Path
from test_render_report import renderer, sample

class RevisionTests(unittest.TestCase):
    def error(self):
        d=sample();r=d['records'][0];r['status']='VERIFIED_WITH_ANOMALY';r['checks']=['Comparaison effectuée.'];r['sources']=[dict(label='Document fictif',url='https://example.org/doc',locator='Article 1',language='FR',excerpt='Texte de preuve synthétique.')]
        r['findings']=[dict(id='E1',kind='error',severity='MINOR',problem='Numéro fautif.',action='Remplacer par 1.')]
        return d

    def test_missing_date_rejected(self):
        d=sample();del d['report_metadata']
        with self.assertRaises(ValueError):renderer.validate(d)

    def test_reexport_does_not_rewrite_dates(self):
        d=sample(); before=copy.deepcopy(d)
        a=list(renderer.sections(renderer.validate(d)));b=list(renderer.sections(renderer.validate(d)))
        self.assertEqual(a,b);self.assertEqual(d,before)

    def test_day_precision_preserves_unknown_hour(self):
        d=sample();d['report_metadata'].update(established_at='2026-09-24',precision='day')
        text=str(list(renderer.sections(renderer.validate(d))))
        self.assertIn('heure non conservée',text);self.assertNotIn('T00:00',text)

    def test_future_consultation_rejected(self):
        d=sample();d['report_metadata']['checks_completed_on']='2026-09-25'
        with self.assertRaises(ValueError):renderer.validate(d)

    def test_revision_requires_scope_and_preserves_initial_date(self):
        d=sample();m=d['report_metadata'];m['report_version']='v2';m['revision']=dict(issued_at='2026-09-25T12:00:00+02:00',scope='Présentation seulement',previous_version='v1')
        text=str(list(renderer.sections(renderer.validate(d))))
        self.assertIn('2026-09-24T14:00:00+02:00',text);self.assertIn('Présentation seulement',text)
        del m['revision']['scope']
        with self.assertRaises(ValueError):renderer.validate(d)

    def test_offset_and_reverse_time_rejected(self):
        for value in ('2026-09-24T14:00:00','2026-09-24T14:00:00+01:00'):
            d=sample();d['report_metadata']['established_at']=value
            with self.assertRaises(ValueError):renderer.validate(d)
        d=sample();d['report_metadata'].update(report_version='v2',revision=dict(issued_at='2026-09-24T13:00:00+02:00',scope='Test',previous_version='v1'))
        with self.assertRaises(ValueError):renderer.validate(d)

    def test_repeated_error_counted_once_suggestion_not_error(self):
        d=self.error();r=copy.deepcopy(d['records'][0]);r['id']='R2';r['location']='Page 2';d['records'].append(r)
        d['records'][0]['findings'].append(dict(id='S1',kind='suggestion',severity='INFORMATION',problem='Précision facultative.',action='Ajouter le point.'))
        self.assertEqual(len(renderer.unique_findings(renderer.validate(d))),1)
        self.assertEqual(len(renderer.unique_findings(d,'suggestion')),1)
        stats=next(v for k,v in renderer.sections(d) if k=='stats')
        self.assertEqual([x[0] for x in stats],['2','1','1'])

    def test_conflicting_repeated_verdict_rejected(self):
        d=self.error();r=copy.deepcopy(d['records'][0]);r['id']='R2';r['findings'][0]['action']='Autre correction';d['records'].append(r)
        with self.assertRaises(ValueError):renderer.validate(d)

    def test_error_without_excerpt_rejected(self):
        d=self.error();del d['records'][0]['sources'][0]['excerpt']
        with self.assertRaises(ValueError):renderer.validate(d)

    def test_prose_cleaned_original_and_evidence_unchanged(self):
        d=self.error();r=d['records'][0];r['original']='Original.. §3';r['checks']=['Lu..','Confirmé.; suite'];r['sources'][0]['excerpt']='Source.. §3'
        nodes=list(renderer.sections(renderer.validate(d)));text=str(nodes)
        self.assertIn('Original.. §3',text);self.assertIn('Source.. §3',text);self.assertNotIn('Lu..',text);self.assertNotIn('Confirmé.;',text)

    def test_internal_codes_and_string_notes_rejected(self):
        d=sample();d['summary']='SOURCE_ATTRIBUTION_UNCERTAIN'
        with self.assertRaises(ValueError):renderer.validate(d)
        d=sample();d['records'][0]['notes']='Phrase'
        with self.assertRaises(ValueError):renderer.validate(d)

    def test_attribution_and_version_do_not_rewrite_exactness(self):
        d=sample();d['quotations']=[dict(id='Q',record_id='R1',title='Citation',location='Page 1',status='EXACT',integrity='FAITHFUL',comparison='Mots identiques.',context='Contexte lu.',attribution='Source erronée',temporal_assessment='Version abrogée')]
        text=str(list(renderer.sections(renderer.validate(d))))
        self.assertIn('Texte conforme',text);self.assertIn('Source erronée',text);self.assertIn('Version abrogée',text)
        self.assertNotIn('Sens déformé',text)

    def test_pdf_includes_printable_evidence_and_dates(self):
        from pypdf import PdfReader
        d=self.error()
        with tempfile.TemporaryDirectory() as tmp:
            f=Path(tmp)/'a.pdf';renderer.write_pdf(list(renderer.sections(renderer.validate(d))),f,d)
            text='\n'.join(p.extract_text() for p in PdfReader(f).pages)
            self.assertIn('https://example.org/doc',text);self.assertIn('2026-09-24T14:00:00+02:00',text);self.assertIn('Texte de preuve synthétique',text)
            self.assertTrue(any(p.get('/Annots') for p in PdfReader(f).pages))

    def test_source_date_and_cross_category_conflict(self):
        d=self.error();d['records'][0]['sources'][0]['consulted_on']='2030-01-01'
        with self.assertRaises(ValueError):renderer.validate(d)
        d=self.error();f=copy.deepcopy(d['records'][0]['findings'][0]);f['kind']='suggestion';d['records'][0]['findings'].append(f)
        with self.assertRaises(ValueError):renderer.validate(d)

    def test_evidence_versions_and_quote_locations_survive(self):
        d=self.error();r=d['records'][0];r['findings'][0]['kind']='suggestion'
        r['sources'][0].update(version='Version 2018',basis='Texte intégral')
        second=copy.deepcopy(r['sources'][0]);second['version']='Version 2022';r['sources'].append(second)
        d['quotations']=[dict(id='Q',record_id='R1',title='Citation distincte',location='Note 17, page 8',status='EXACT',integrity='FAITHFUL',comparison='Mots identiques.',context='Contexte lu.')]
        text=str(list(renderer.sections(renderer.validate(d))))
        for token in ('Texte de preuve synthétique.', 'Version 2018', 'Version 2022', 'Texte intégral', 'Note 17, page 8'):self.assertIn(token,text)

    def test_many_occurrences_table_can_split(self):
        from pypdf import PdfReader
        d=sample();base=d['records'][0]
        d['records']=[dict(copy.deepcopy(base),id=f'R{i}',location=f'Page {i}, note {i}') for i in range(250)]
        with tempfile.TemporaryDirectory() as tmp:
            f=Path(tmp)/'long.pdf';renderer.write_pdf(list(renderer.sections(renderer.validate(d))),f,d)
            self.assertGreater(len(PdfReader(f).pages),1)

if __name__=='__main__':unittest.main()
