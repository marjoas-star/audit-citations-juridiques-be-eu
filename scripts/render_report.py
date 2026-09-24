#!/usr/bin/env python3
"""Render an already established audit; performs no legal research or scoring."""
import argparse
from collections import Counter
from html import escape
import json
from pathlib import Path
from urllib.parse import urlsplit

STATUS = {
    'VERIFIED': 'Référence vérifiée',
    'VERIFIED_WITH_ANOMALY': 'Référence identifiée, correction nécessaire',
    'PARTIALLY_VERIFIED': 'Vérification partielle',
    'NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES': 'Vérification impossible avec les sources accessibles',
    'NOT_FOUND_OR_CONTRADICTORY': 'Référence non retrouvée ou contradiction établie',
}
TEXT = {'EXACT': 'Texte conforme', 'EXACT_WITH_SIGNALLED_ADAPTATIONS': 'Texte conforme avec adaptations signalées',
        'MINOR_DEVIATION': 'Écart mineur', 'INEXACT': 'Citation inexacte',
        'NOT_VERIFIABLE': 'Citation non vérifiable', 'NOT_APPLICABLE_TRANSLATION': 'Traduction : contrôle distinct'}
INTEGRITY = {'FAITHFUL': 'Sens préservé', 'MATERIAL_BUT_NOT_MISLEADING': 'Modification notable, sans déformation du sens',
             'MISLEADING': 'Sens déformé', 'NOT_VERIFIABLE': 'Effet sur le sens non vérifiable'}
SEVERITY = {'CRITICAL': 'Priorité critique', 'MAJOR': 'Correction importante', 'MINOR': 'Correction ponctuelle', 'INFORMATION': 'Information'}


def validate(data):
    if data.get('report_language', 'fr') != 'fr':
        raise ValueError('Ce générateur fournit actuellement la présentation française uniquement')
    for key in ('title', 'document', 'date', 'version', 'scope', 'summary', 'limitations', 'method', 'records', 'quotations'):
        if key not in data:
            raise ValueError('Champ manquant : ' + key)
    ids = set()
    for r in data['records']:
        for key in ('id', 'source_id', 'title', 'original', 'checked', 'location', 'status', 'checks', 'limits', 'sources'):
            if key not in r:
                raise ValueError(f'{r.get("id", "fiche")} : champ manquant {key}')
        if r['id'] in ids:
            raise ValueError('Identifiant de fiche répété : ' + r['id'])
        ids.add(r['id'])
        if r['status'] not in STATUS:
            raise ValueError('Statut inconnu : ' + r['status'])
        if r['status'] in ('VERIFIED', 'VERIFIED_WITH_ANOMALY') and (not r['checks'] or not r['sources']):
            raise ValueError('Une fiche vérifiée exige des contrôles et des preuves')
        for s in r['sources']:
            if not all(s.get(k) for k in ('label', 'url', 'locator', 'language')):
                raise ValueError('Source incomplète : ' + r['id'])
            u = urlsplit(s['url'])
            if u.scheme not in ('https', 'http') or not u.netloc:
                raise ValueError('Lien de preuve HTTP(S) requis : ' + r['id'])
        for f in r.get('findings', []):
            if f.get('severity') not in SEVERITY or not f.get('problem') or not f.get('action'):
                raise ValueError('Constat incomplet : ' + r['id'])
    qids = set()
    for q in data['quotations']:
        for key in ('id', 'record_id', 'title', 'location', 'status', 'integrity', 'comparison', 'context'):
            if not q.get(key):
                raise ValueError('Citation incomplète : ' + key)
        if q['id'] in qids or q['record_id'] not in ids:
            raise ValueError('Identifiant ou rattachement de citation invalide')
        qids.add(q['id'])
        if q['status'] not in TEXT or q['integrity'] not in INTEGRITY:
            raise ValueError('Statut de citation inconnu')
        if q['status'] == 'NOT_APPLICABLE_TRANSLATION' and not q.get('translation_assessment'):
            raise ValueError('La traduction exige une appréciation distincte')
    return data


def sections(data):
    """One human-readable document tree feeds both output formats."""
    count = Counter(r['status'] for r in data['records'])
    findings = [(r, f) for r in data['records'] for f in r.get('findings', [])]
    yield ('title', data['title'])
    yield ('subtitle', data['document'])
    yield ('meta', f"{data['date']}  |  Version du skill : {data['version']}")
    yield ('h1', 'Ce qu’il faut retenir')
    yield ('p', data['summary'])
    yield ('stats', [(str(len(data['records'])), 'références examinées'),
                     (str(len({r['source_id'] for r in data['records']})), 'sources principales'),
                     (str(len(data['quotations'])), 'citations examinées')])
    yield ('h2', 'Étendue du contrôle')
    yield ('p', data['scope'])
    yield ('table', (['Résultat des références', 'Nombre'], [(STATUS[s], str(count[s])) for s in STATUS if count[s]]))
    yield ('callout', 'Une référence vérifiée l’est seulement pour les éléments explicitement contrôlés. Une impossibilité de vérifier n’établit pas une erreur.')
    yield ('page', None)
    yield ('h1', 'Corrections et vérifications à prévoir')
    if findings:
        for r, f in findings:
            yield ('h2', r['title'] + ' — ' + SEVERITY[f['severity']])
            yield ('meta', r['location'])
            yield ('p', f['problem'])
            yield ('p', 'Suite proposée : ' + f['action'])
    else:
        yield ('p', 'Aucune correction établie dans les fiches de cet audit. Les limites ci-dessous restent applicables.')
    yield ('h2', 'Ce qui reste hors du contrôle')
    for item in data['limitations']:
        yield ('bullet', item)
    yield ('h2', 'Comment lire les fiches')
    yield ('p', 'Chaque fiche conserve la référence du document, précise ce qui a été constaté et donne accès à la preuve. Les citations sont examinées séparément : l’identité d’un arrêt ne suffit pas à garantir les mots qui lui sont attribués.')
    yield ('page', None)
    yield ('h1', 'Examen des références')
    for index, r in enumerate(data['records'], 1):
        yield ('card_start', None)
        yield ('h2', f"{index:02d}. {r['title']}")
        yield ('badge', STATUS[r['status']])
        yield ('meta', r['location'])
        yield ('p', 'Référence citée : ' + r['original'])
        if r['checked'] != r['original']:
            yield ('p', 'Référence constatée : ' + r['checked'])
        yield ('p', 'Éléments contrôlés : ' + '; '.join(r['checks']) + '.')
        for note in r.get('notes', []):
            yield ('p', note)
        if r['limits']:
            yield ('p', 'Limites : ' + r['limits'])
        for s in r['sources']:
            yield ('link', (s['label'], s['url'], s['locator'] + ' · ' + s['language']))
        yield ('card_end', None)
        yield ('space', None)
    if data['quotations']:
        yield ('page', None)
        yield ('h1', 'Fidélité des citations')
        for q in data['quotations']:
            yield ('h2', q['title'])
            yield ('meta', q['location'])
            yield ('badge', TEXT[q['status']] + ' · ' + INTEGRITY[q['integrity']])
            yield ('p', q['comparison'])
            yield ('p', q['context'])
            if q.get('translation_assessment'):
                yield ('p', q['translation_assessment'])
    yield ('h1', 'Méthode et portée du rapport')
    for item in data['method']:
        yield ('p', item)
    yield ('callout', 'Rapport préparé avec une assistance d’intelligence artificielle. Les conclusions dépendent des sources effectivement consultées. Une relecture juridique reste nécessaire avant utilisation ; ce rapport ne constitue pas une certification générale de fiabilité.')


def write_markdown(nodes, path):
    result = []
    for kind, value in nodes:
        if kind in ('title', 'h1', 'h2'):
            result.append({'title': '# ', 'h1': '## ', 'h2': '### '}[kind] + value)
        elif kind == 'table':
            heads, rows = value
            clean = lambda x: str(x).replace('|', '\\|').replace('\n', ' ')
            result.append('\n'.join(['| ' + ' | '.join(map(clean, heads)) + ' |', '| ' + ' | '.join(['---'] * len(heads)) + ' |'] + ['| ' + ' | '.join(map(clean, row)) + ' |' for row in rows]))
        elif kind == 'stats':
            result.append(' · '.join(a + ' ' + b for a, b in value))
        elif kind == 'link':
            label, url, loc = value
            result.append(f'Preuve : [{label}]({url}) — {loc}.')
        elif kind == 'callout':
            result.append('> ' + value)
        elif kind == 'bullet':
            result.append('- ' + value)
        elif kind not in ('space', 'page', 'card_start', 'card_end'):
            result.append(value)
    path.write_text('\n\n'.join(result) + '\n', encoding='utf-8')


def write_pdf(nodes, path, data):
    import reportlab
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, CondPageBreak, KeepTogether
    fonts = Path(reportlab.__file__).parent / 'fonts'
    pdfmetrics.registerFont(TTFont('AuditRegular', str(fonts / 'Vera.ttf')))
    pdfmetrics.registerFont(TTFont('AuditBold', str(fonts / 'VeraBd.ttf')))
    navy, teal, muted = '#173449', '#17685F', '#52616B'
    def style(name, size=10, lead=15, color=navy, bold=False, **kw):
        return ParagraphStyle(name, fontName='AuditBold' if bold else 'AuditRegular', fontSize=size, leading=lead,
                              textColor=colors.HexColor(color), spaceAfter=8, alignment=TA_LEFT, **kw)
    styles = {'title': style('title', 25, 31, bold=True, spaceBefore=22),
              'subtitle': style('subtitle', 12, 18), 'meta': style('meta', 8.5, 12, muted),
              'h1': style('h1', 17, 23, bold=True, spaceBefore=16, keepWithNext=True),
              'h2': style('h2', 11.5, 17, bold=True, spaceBefore=12, keepWithNext=True),
              'p': style('p'), 'badge': style('badge', 9, 14, teal, True, keepWithNext=True),
              'cell': style('cell', 9, 13), 'stat': style('stat', 23, 29, teal, True),
              'link': style('link', 8.5, 13, teal), 'callout': style('callout', 9, 14, muted, backColor=colors.HexColor('#EFF4F5'), borderPadding=10, spaceBefore=8)}
    paragraph = lambda text, name='p': Paragraph(escape(str(text)), styles[name])
    story = []
    card_index = None
    for kind, value in nodes:
        if kind == 'card_start':
            card_index = len(story)
        elif kind == 'card_end':
            content = story[card_index:]
            del story[card_index:]
            story.append(KeepTogether(content))
            card_index = None
        elif kind == 'page':
            story.append(PageBreak())
        elif kind == 'space':
            story.append(Spacer(1, 8))
        elif kind == 'stats':
            table = Table([[paragraph(a, 'stat') for a, b in value], [paragraph(b, 'meta') for a, b in value]], colWidths=[165] * 3)
            table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0F6F5')), ('VALIGN',(0,0),(-1,-1),'TOP'), ('LEFTPADDING',(0,0),(-1,-1),12), ('TOPPADDING',(0,0),(-1,0),12), ('BOTTOMPADDING',(0,1),(-1,-1),10)]))
            story.extend([Spacer(1,10), table, Spacer(1,10)])
        elif kind == 'table':
            heads, rows = value
            table = Table([[paragraph(c,'cell') for c in row] for row in [heads] + rows], colWidths=[420,75], repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E4ECEF')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),0.3,colors.HexColor('#D9E1E4')),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
            story.append(table)
        elif kind == 'link':
            label,url,loc=value
            story.append(Paragraph(f'Preuve : <link href="{escape(url,quote=True)}" color="{teal}">{escape(label)}</link> — {escape(loc)}.', styles['link']))
        elif kind == 'bullet':
            story.append(paragraph('• ' + value))
        else:
            if kind == 'h2':
                story.append(CondPageBreak(115))
            story.append(paragraph(value, kind))
    def furniture(canvas, doc):
        canvas.setStrokeColor(colors.HexColor('#D9E1E4'));canvas.line(50,39,545,39)
        canvas.setFont('AuditRegular',8);canvas.setFillColor(colors.HexColor(muted))
        canvas.drawString(50,25,'Audit des citations juridiques · ' + data['date'])
        canvas.drawRightString(545,25,str(doc.page))
    SimpleDocTemplate(str(path), pagesize=(595.28,841.89), leftMargin=50,rightMargin=50,topMargin=35,bottomMargin=55,
                      title=data['title'],author='Audit des citations juridiques').build(story,onFirstPage=furniture,onLaterPages=furniture)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('--output',required=True,type=Path,help='Output stem, without extension')
    parser.add_argument('--markdown-only',action='store_true')
    args=parser.parse_args()
    data=validate(json.loads(args.input.read_text(encoding='utf-8')))
    nodes=list(sections(data));args.output.parent.mkdir(parents=True,exist_ok=True)
    write_markdown(nodes,args.output.with_suffix('.md'))
    if not args.markdown_only:
        write_pdf(nodes,args.output.with_suffix('.pdf'),data)


if __name__=='__main__':
    main()
