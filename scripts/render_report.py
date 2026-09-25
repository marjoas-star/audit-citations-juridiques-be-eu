#!/usr/bin/env python3
"""Render an already established audit; performs no legal research or scoring."""
import argparse
from collections import Counter
from datetime import datetime, date
from zoneinfo import ZoneInfo
import re
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
DISCLAIMER = ('Ce rapport a été établi avec l’assistance de systèmes d’IA et au moyen de recherches documentaires. '
              'Sa fiabilité dépend de la disponibilité, de l’accessibilité, de l’indexation et de la mise à jour des sources consultées, '
              'dont les interfaces peuvent évoluer. L’absence de vérification ne signifie pas qu’une référence est erronée. '
              'Les conclusions valent à la date des vérifications indiquée ci-dessus, sans actualisation automatique, '
              'et ne constituent pas une certification générale de fiabilité. Une vérification humaine demeure indispensable '
              'avant toute utilisation juridictionnelle, procédurale, consultative ou scientifique.')
SEVERITY = {'CRITICAL': 'Priorité critique', 'MAJOR': 'Correction importante', 'MINOR': 'Correction ponctuelle', 'INFORMATION': 'Information'}


FUTURE_TOLERANCE_SECONDS = 300


def not_future(value, precision, timezone):
    # Reads the clock only to refuse a date that has not happened yet; never fills or rewrites a date.
    now = datetime.now(ZoneInfo(timezone))
    if precision == 'day':
        late = date.fromisoformat(value) > now.date()
    else:
        late = (datetime.fromisoformat(value) - now).total_seconds() > FUTURE_TOLERANCE_SECONDS
    if late:
        raise ValueError('Date postérieure à l’heure réelle : ' + value)


def report_dates(data):
    m = data.get('report_metadata')
    if not isinstance(m, dict):
        raise ValueError('Métadonnées de datation requises ; ne pas inventer une heure ancienne')
    for k in ('established_at', 'timezone', 'precision', 'report_version', 'checks_started_on', 'checks_completed_on', 'legal_reference'):
        if not m.get(k):
            raise ValueError('Datation incomplète : ' + k)
    ZoneInfo(m['timezone'])
    def timestamp(v, precision):
        if precision == 'day':
            return date.fromisoformat(v)
        t = datetime.fromisoformat(v)
        if t.tzinfo is None:
            raise ValueError('Décalage UTC requis')
        if t.utcoffset() != t.astimezone(ZoneInfo(m['timezone'])).utcoffset():
            raise ValueError('Décalage incompatible avec le fuseau nommé')
        return t.astimezone(ZoneInfo(m['timezone'])).date()
    if m['precision'] not in ('day', 'second'):
        raise ValueError('Précision temporelle inconnue')
    established = timestamp(m['established_at'], m['precision'])
    not_future(m['established_at'], m['precision'], m['timezone'])
    issued = established
    rev = m.get('revision')
    if rev:
        if not all(rev.get(k) for k in ('issued_at', 'scope', 'previous_version')):
            raise ValueError('Révision incomplète')
        issued = timestamp(rev['issued_at'], 'second')
        not_future(rev['issued_at'], 'second', m['timezone'])
        if issued < established:
            raise ValueError('Révision antérieure au rapport initial')
        if m['precision'] == 'second' and datetime.fromisoformat(rev['issued_at']) < datetime.fromisoformat(m['established_at']):
            raise ValueError('Révision antérieure au rapport initial')
        if rev['previous_version'] == m['report_version']:
            raise ValueError('Une révision exige une nouvelle version')
    start = date.fromisoformat(m['checks_started_on'])
    end = date.fromisoformat(m['checks_completed_on'])
    if start > end or end > issued:
        raise ValueError('Période de consultation incohérente')
    return m


QUOTE_OK = ('EXACT', 'EXACT_WITH_SIGNALLED_ADAPTATIONS')


def reference_label(r, data):
    # A correct reference whose quotation deviates must not read as a clean result.
    label = STATUS[r['status']]
    quotes = [q for q in data['quotations'] if q['record_id'] == r['id'] and q['status'] not in QUOTE_OK]
    if quotes:
        label += ' · citation : ' + ' ; '.join(dict.fromkeys(TEXT[q['status']].lower() for q in quotes))
    elif r['status'] == 'VERIFIED' and any(f.get('kind') == 'error' for f in r.get('findings', [])):
        label += ' · correction ci-dessus'
    return label


def unique_findings(data, kind='error'):
    seen = {}
    for r in data['records']:
        for f in r.get('findings', []):
            if f.get('kind') != kind:
                continue
            if f['id'] in seen:
                if seen[f['id']][1] != f:
                    raise ValueError('Verdicts différents pour un même constat : ' + f['id'])
            else:
                seen[f['id']] = (r, f)
    order = {'CRITICAL': 0, 'MAJOR': 1, 'MINOR': 2, 'INFORMATION': 3}
    return sorted(seen.values(), key=lambda pair: order[pair[1]['severity']])


def clean_prose(text):
    # Never apply to verbatim originals, source excerpts, or URLs.
    text = re.sub(r'(?<!\.)\.\.(?!\.)', '.', str(text))
    text = re.sub(r'\.\s*;', ';', text)
    text = re.sub(r'§(?=\d)', '§ ', text)
    text = re.sub(r'([IVX]+)ème', r'\1e', text)
    return text


def public_text(data):
    for key in ('summary', 'scope', 'limitations', 'method'):
        value = data[key]
        yield from value if isinstance(value, list) else [value]
    for r in data['records']:
        for key in ('title', 'checked', 'limits'):
            yield r[key]
        yield from r.get('checks', [])
        yield from r.get('notes', [])
        for f in r.get('findings', []):
            yield f['problem']; yield f['action']
    for q in data['quotations']:
        for key in ('comparison', 'context', 'translation_assessment', 'attribution', 'temporal_assessment'):
            if q.get(key): yield q[key]


def validate(data):
    if data.get('report_language', 'fr') != 'fr':
        raise ValueError('Ce générateur fournit actuellement la présentation française uniquement')
    if not data.get('skill_version') and not data.get('version'):
        raise ValueError('Champ manquant : skill_version (version du skill utilisée pour l’audit)')
    for key in ('title', 'document', 'scope', 'summary', 'limitations', 'method', 'records', 'quotations'):
        if key not in data:
            raise ValueError('Champ manquant : ' + key)
    report_dates(data)
    for text in public_text(data):
        if re.search(r'\b(?:[A-Z]{2,}(?:_[A-Z0-9]+)+|MISLEADING|source_id|SKILL\.md|pypdf)\b', text):
            raise ValueError('Code interne dans la prose destinée au lecteur')
    ids = set()
    finding_ids = {}
    for r in data['records']:
        for key in ('id', 'source_id', 'title', 'original', 'checked', 'location', 'status', 'checks', 'limits', 'sources'):
            if key not in r:
                raise ValueError(f'{r.get("id", "fiche")} : champ manquant {key}')
        if r['id'] in ids:
            raise ValueError('Identifiant de fiche répété : ' + r['id'])
        ids.add(r['id'])
        for extra in r.get('additional_occurrences', []):
            if not all(extra.get(k) for k in ('id', 'location', 'original')) or extra['id'] in ids:
                raise ValueError('Occurrence regroupée incomplète ou répétée')
            ids.add(extra['id'])
        if r['status'] not in STATUS:
            raise ValueError('Statut inconnu : ' + r['status'])
        if r['status'] in ('VERIFIED', 'VERIFIED_WITH_ANOMALY') and (not r['checks'] or not r['sources']):
            raise ValueError('Une fiche vérifiée exige des contrôles et des preuves')
        for s in r['sources']:
            if not all(s.get(k) for k in ('label', 'url', 'locator', 'language')):
                raise ValueError('Source incomplète : ' + r['id'])
            if s.get('consulted_on'):
                consulted = date.fromisoformat(s['consulted_on'])
                m = data['report_metadata']
                if not date.fromisoformat(m['checks_started_on']) <= consulted <= date.fromisoformat(m['checks_completed_on']):
                    raise ValueError('Consultation hors de la période déclarée')
            u = urlsplit(s['url'])
            if u.scheme not in ('https', 'http') or not u.netloc:
                raise ValueError('Lien de preuve HTTP(S) requis : ' + r['id'])
        if not isinstance(r.get('notes', []), list) or not isinstance(r['checks'], list):
            raise ValueError('Notes et contrôles doivent être des listes')
        for f in r.get('findings', []):
            if not f.get('id') or f.get('kind') not in ('error', 'suggestion'):
                raise ValueError('Constat sans identifiant ou sans catégorie')
            if f['id'] in finding_ids and finding_ids[f['id']] != f:
                raise ValueError('Constat contradictoire : ' + f['id'])
            finding_ids[f['id']] = f
            if f['kind'] == 'error' and not any(x.get('excerpt') for x in r['sources']):
                raise ValueError('Une correction établie exige un court passage probant')
            if f.get('severity') not in SEVERITY or not f.get('problem') or not f.get('action'):
                raise ValueError('Constat incomplet : ' + r['id'])
    qids = set()
    for q in data['quotations']:
        for key in ('id', 'record_id', 'title', 'location', 'status', 'integrity', 'comparison', 'context'):
            if not q.get(key):
                raise ValueError('Citation incomplète : ' + key)
        if q['id'] in qids or q['record_id'] not in {r['id'] for r in data['records']}:
            raise ValueError('Identifiant ou rattachement de citation invalide')
        qids.add(q['id'])
        if q['status'] not in TEXT or q['integrity'] not in INTEGRITY:
            raise ValueError('Statut de citation inconnu')
        if q['status'] == 'NOT_APPLICABLE_TRANSLATION' and not q.get('translation_assessment'):
            raise ValueError('La traduction exige une appréciation distincte')
    unique_findings(data)
    unique_findings(data, 'suggestion')
    return data


def sections(data):
    """Compact canonical tree; no research, status inference, or automatic dating."""
    m = report_dates(data)
    errors = unique_findings(data)
    suggestions = unique_findings(data, 'suggestion')
    yield ('title', data['title'])
    yield ('subtitle', data['document'])
    precision = ' (heure non conservée)' if m['precision'] == 'day' else ''
    yield ('meta', 'Rapport établi le : ' + m['established_at'] + precision + ' · ' + m['timezone'])
    yield ('meta', 'Vérifications : ' + m['checks_started_on'] + ' au ' + m['checks_completed_on'] + ' · Rapport ' + m['report_version'])
    if m.get('revision'):
        rev = m['revision']
        yield ('meta', 'Révision : ' + rev['issued_at'] + ' · remplace ' + rev['previous_version'])
        yield ('p', 'Étendue de la révision : ' + rev['scope'])
    else:
        yield ('meta', 'Actualisation ultérieure : aucune')
    yield ('meta', 'Date juridique : ' + m['legal_reference'])
    yield ('h1', 'Ce qu’il faut retenir')
    yield ('p', clean_prose(data['summary']))
    yield ('stats', [(str(sum(1 + len(r.get('additional_occurrences', [])) for r in data['records'])), 'occurrences inventoriées'),
                     (str(len({r['source_id'] for r in data['records']})), 'sources distinctes'),
                     (str(len(errors)), 'erreurs distinctes')])
    yield ('p', clean_prose(data['scope']))
    if errors:
        yield ('h1', 'Corrections nécessaires')
        for r, f in errors:
            yield ('card_start', None)
            yield ('h2', r['title'] + ' · ' + SEVERITY[f['severity']])
            locations = list(dict.fromkeys(x['location'] for x in data['records'] if any(y['id'] == f['id'] for y in x.get('findings', []))))
            yield ('meta', ' ; '.join(locations))
            yield ('p', clean_prose(f['problem']))
            yield ('p', 'Correction : ' + clean_prose(f['action']))
            for proof in r['sources']:
                if proof.get('excerpt'):
                    yield ('p', 'Passage source : « ' + proof['excerpt'] + ' »')
                    yield ('link', (proof['label'], proof['url'], proof['locator'] + ' · ' + proof['language']))
            yield ('card_end', None)
    groups = {}
    for r in data['records']:
        groups.setdefault(r['source_id'], []).append(r)
    yield ('h1', 'Références et contrôles')
    rows = []
    for group in groups.values():
        labels = list(dict.fromkeys(reference_label(r, data) for r in group))
        rows.append((group[0]['title'], ' ; '.join(dict.fromkeys(r['location'] for r in group)), ' ; '.join(labels)))
    yield ('table', (['Source / référence', 'Emplacements', 'Résultat'], rows))
    for group in groups.values():
        yield ('card_start', None)
        yield ('h2', group[0]['title'])
        for r in group:
            yield ('badge', reference_label(r, data))
            yield ('meta', r['location'])
            prefix = 'Référence relevée (abrégée) : ' if r.get('original_kind') == 'summary' else 'Référence originale : '
            yield ('p', prefix + r['original'])
            yield ('p', 'Référence constatée : ' + ('identique' if r['checked'] == r['original'] else clean_prose(r['checked'])))
            for check in r['checks']:
                yield ('bullet', clean_prose(check))
            if r['limits']: yield ('p', 'Limite : ' + clean_prose(r['limits']))
            for note in r.get('notes', []): yield ('p', clean_prose(note))
            for q in (q for q in data['quotations'] if q['record_id'] == r['id']):
                yield ('meta', q['title'] + ' · ' + q['location'])
                yield ('badge', TEXT[q['status']] + ' · ' + INTEGRITY[q['integrity']])
                yield ('p', clean_prose(q['comparison']))
                yield ('p', clean_prose(q['context']))
                for key, label in [('attribution','Attribution'), ('temporal_assessment','Version'), ('translation_assessment','Traduction')]:
                    if q.get(key): yield ('p', label + ' : ' + clean_prose(q[key]))
        proof_groups = {}
        for r in group:
            for proof in r['sources']:
                key = tuple(proof.get(k, '') for k in ('url', 'language', 'version', 'basis', 'consulted_on'))
                entry = proof_groups.setdefault(key, {'proof': proof, 'locators': [], 'excerpts': []})
                if proof['locator'] not in entry['locators']: entry['locators'].append(proof['locator'])
                if proof.get('excerpt') and not any(f['kind'] == 'error' for f in r.get('findings', [])):
                    if proof['excerpt'] not in entry['excerpts']: entry['excerpts'].append(proof['excerpt'])
        for entry in proof_groups.values():
            proof = entry['proof']
            for excerpt in entry['excerpts']: yield ('p', 'Passage source : « ' + excerpt + ' »')
            loc = ' ; '.join(entry['locators']) + ' · ' + proof['language']
            for field, label in [('version', 'version'), ('basis', 'preuve')]:
                if proof.get(field): loc += ' · ' + label + ' : ' + proof[field]
            if proof.get('consulted_on'): loc += ' · consulté le ' + proof['consulted_on']
            yield ('link', (proof['label'], proof['url'], loc))
        yield ('card_end', None)
        yield ('space', None)
    if suggestions:
        yield ('h1', 'Suggestions facultatives')
        for r, f in suggestions:
            yield ('p', r['location'] + ' : ' + clean_prose(f['problem']) + ' ' + clean_prose(f['action']))
    yield ('h1', 'Limites et traçabilité')
    for item in data['limitations']: yield ('bullet', clean_prose(item))
    yield ('h2', 'Méthode suivie')
    for item in data['method']: yield ('bullet', clean_prose(item))
    yield ('meta', 'Version du skill : ' + (data.get('skill_version') or data['version']))
    yield ('h2', 'Avertissement')
    yield ('callout', DISCLAIMER)


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
    def style(name, size=9, lead=12.5, color=navy, bold=False, **kw):
        return ParagraphStyle(name, fontName='AuditBold' if bold else 'AuditRegular', fontSize=size, leading=lead,
                              textColor=colors.HexColor(color), spaceAfter=5, alignment=TA_LEFT, **kw)
    styles = {'title': style('title', 25, 31, bold=True, spaceBefore=22),
              'subtitle': style('subtitle', 12, 18), 'meta': style('meta', 8.5, 12, muted),
              'h1': style('h1', 17, 23, bold=True, spaceBefore=16),
              'h2': style('h2', 11.5, 17, bold=True, spaceBefore=12, keepWithNext=True),
              'p': style('p'), 'badge': style('badge', 9, 14, teal, True, keepWithNext=True),
              'cell': style('cell', 9, 13), 'stat': style('stat', 23, 29, teal, True),
              'link': style('link', 8.5, 13, teal, keepWithNext=True), 'url': style('url', 8.5, 13, teal), 'callout': style('callout', 9, 14, muted, backColor=colors.HexColor('#EFF4F5'), borderPadding=10, spaceBefore=8)}
    paragraph = lambda text, name='p': Paragraph(escape(str(text)), styles[name])
    story = []
    card_index = None
    for kind, value in nodes:
        if kind == 'card_start':
            card_index = len(story)
        elif kind == 'card_end':
            content = story[card_index:]
            del story[card_index:]
            story.extend(content)
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
            table = Table([[paragraph(c,'cell') for c in row] for row in [heads] + rows], colWidths=([155,150,190] if len(heads)==3 else [420,75]), repeatRows=1, splitInRow=1, hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#E4ECEF')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),0.3,colors.HexColor('#D9E1E4')),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
            story.append(table)
        elif kind == 'link':
            label,url,loc=value
            story.append(Paragraph(f'Preuve : <link href="{escape(url,quote=True)}" color="{teal}">{escape(label)}</link> — {escape(loc)}.', styles['link']))
            story.append(paragraph(url, 'url'))
        elif kind == 'bullet':
            story.append(paragraph('• ' + value))
        elif kind == 'badge':
            tone = '#17685F'
            if any(x in value for x in ('correction', 'inexacte', 'déformé', 'contradiction')): tone = '#A32722'
            elif any(x in value for x in ('partielle', 'Écart', 'écart', 'Traduction', 'traduction')): tone = '#805500'
            elif any(x in value for x in ('impossible', 'non vérifiable')): tone = '#52616B'
            story.append(Paragraph(escape(value), style('status', 9, 13, tone, True, keepWithNext=True)))
        else:
            if kind == 'h1':
                story.append(CondPageBreak(100))
            if kind == 'h2':
                story.append(CondPageBreak(115))
            story.append(paragraph(value, kind))
    def furniture(canvas, doc):
        canvas.setStrokeColor(colors.HexColor('#D9E1E4'));canvas.line(50,39,545,39)
        canvas.setFont('AuditRegular',8);canvas.setFillColor(colors.HexColor(muted))
        canvas.drawString(50,25,'Rapport ' + data['report_metadata']['report_version'] + ' · établi le ' + data['report_metadata']['established_at'][:10])
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
