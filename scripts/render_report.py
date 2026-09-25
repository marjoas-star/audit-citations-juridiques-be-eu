#!/usr/bin/env python3
# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
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

def _fr_date(d): return f'{d.day}{"er" if d.day == 1 else ""} {LANG["fr"]["months"][d.month - 1]} {d.year}'
def _nl_date(d): return f'{d.day} {LANG["nl"]["months"][d.month - 1]} {d.year}'
def _de_date(d): return f'{d.day}. {LANG["de"]["months"][d.month - 1]} {d.year}'
def _en_date(d): return f'{d.day} {LANG["en"]["months"][d.month - 1]} {d.year}'


LANG = {
    'fr': {
        'status': {'VERIFIED': 'Référence vérifiée', 'VERIFIED_WITH_ANOMALY': 'Référence identifiée, correction nécessaire',
                   'PARTIALLY_VERIFIED': 'Vérification partielle',
                   'NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES': 'Vérification impossible avec les sources accessibles',
                   'NOT_FOUND_OR_CONTRADICTORY': 'Référence non retrouvée ou contradiction établie'},
        'text': {'EXACT': 'Texte conforme', 'EXACT_WITH_SIGNALLED_ADAPTATIONS': 'Texte conforme avec adaptations signalées',
                 'MINOR_DEVIATION': 'Écart mineur', 'INEXACT': 'Citation inexacte', 'NOT_VERIFIABLE': 'Citation non vérifiable',
                 'NOT_APPLICABLE_TRANSLATION': 'Traduction contrôlée séparément'},
        'quote_short': {'MINOR_DEVIATION': 'écart mineur', 'INEXACT': 'inexacte', 'NOT_VERIFIABLE': 'non vérifiable'},
        'integrity': {'FAITHFUL': 'Sens préservé', 'MATERIAL_BUT_NOT_MISLEADING': 'Modification notable, sans déformation du sens',
                      'MISLEADING': 'Sens déformé', 'NOT_VERIFIABLE': 'Effet sur le sens non vérifiable'},
        'severity': {'CRITICAL': 'Priorité critique', 'MAJOR': 'Correction importante', 'MINOR': 'Correction ponctuelle', 'INFORMATION': 'Information'},
        'months': ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'],
        'date': _fr_date, 'at': lambda t: f' à {t.hour} h {t.minute:02d}',
        'numbers': 'zéro un deux trois quatre cinq six sept huit neuf dix onze douze treize quatorze quinze seize dix-sept dix-huit dix-neuf vingt'.split() + ['une'],
        'counts': {'sources distinctes': 'sources', 'erreurs distinctes': 'errors', 'corrections établies': 'errors'},
        'disclaimer': ('Ce rapport a été établi avec l’assistance de systèmes d’IA et au moyen de recherches documentaires. '
                       'Sa fiabilité dépend de la disponibilité, de l’accessibilité, de l’indexation et de la mise à jour des sources consultées, '
                       'dont les interfaces peuvent évoluer. L’absence de vérification ne signifie pas qu’une référence est erronée. '
                       'Les conclusions valent à la date des vérifications indiquée ci-dessus, sans actualisation automatique, '
                       'et ne constituent pas une certification générale de fiabilité. Une vérification humaine demeure indispensable '
                       'avant toute utilisation juridictionnelle, procédurale, consultative ou scientifique.'),
        'ui': {'established': 'Rapport établi le ', 'hour_not_kept': ' (heure non conservée)', 'consulted_on': 'Sources consultées le ',
               'consulted_from': 'Sources consultées du ', 'to': ' au ', 'revision': 'Révision du ', 'replaces': ' (remplace la version ',
               'revision_scope': 'Étendue de la révision : ', 'legal_date': 'Date juridique retenue : ', 'keep': 'Ce qu’il faut retenir',
               'stats': ['occurrences inventoriées', 'sources distinctes', 'erreurs distinctes'], 'corrections': 'Corrections nécessaires',
               'correction': 'Correction : ', 'passage': 'Passage source : ', 'references': 'Références et contrôles',
               'heads': ['Source / référence', 'Emplacements', 'Résultat'], 'cited': 'Référence citée : ',
               'cited_short': 'Référence citée (abrégée) : ', 'exact': 'Référence exacte : ', 'limit': 'Limite : ',
               'attribution': 'Attribution', 'version': 'Version', 'translation': 'Traduction', 'quote': ' · citation : ',
               'fix_above': ' · correction nécessaire (voir ci-dessus)', 'confirmed': 'Références confirmées sans réserve',
               'one_quote': ' Citation conforme.', 'n_quotes': ' {} citations conformes.', 'suggestions': 'Suggestions facultatives',
               'limits': 'Limites et traçabilité', 'method': 'Méthode suivie', 'skill_version': 'Version du skill : ',
               'disclaimer': 'Avertissement', 'proof': 'Preuve', 'consulted': ' · consulté le ', 'q_open': '« ', 'q_close': ' »'},
    },
    'nl': {
        'status': {'VERIFIED': 'Verwijzing gecontroleerd', 'VERIFIED_WITH_ANOMALY': 'Verwijzing geïdentificeerd, correctie nodig',
                   'PARTIALLY_VERIFIED': 'Gedeeltelijk gecontroleerd',
                   'NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES': 'Niet controleerbaar met de toegankelijke bronnen',
                   'NOT_FOUND_OR_CONTRADICTORY': 'Verwijzing niet teruggevonden of tegenstrijdigheid vastgesteld'},
        'text': {'EXACT': 'Tekst conform', 'EXACT_WITH_SIGNALLED_ADAPTATIONS': 'Tekst conform met aangegeven aanpassingen',
                 'MINOR_DEVIATION': 'Kleine afwijking', 'INEXACT': 'Onjuist citaat', 'NOT_VERIFIABLE': 'Citaat niet controleerbaar',
                 'NOT_APPLICABLE_TRANSLATION': 'Vertaling afzonderlijk gecontroleerd'},
        'quote_short': {'MINOR_DEVIATION': 'kleine afwijking', 'INEXACT': 'onjuist', 'NOT_VERIFIABLE': 'niet controleerbaar'},
        'integrity': {'FAITHFUL': 'Betekenis behouden', 'MATERIAL_BUT_NOT_MISLEADING': 'Wezenlijke wijziging, zonder vertekening van de betekenis',
                      'MISLEADING': 'Betekenis vertekend', 'NOT_VERIFIABLE': 'Gevolg voor de betekenis niet controleerbaar'},
        'severity': {'CRITICAL': 'Kritieke prioriteit', 'MAJOR': 'Belangrijke correctie', 'MINOR': 'Kleine correctie', 'INFORMATION': 'Informatie'},
        'months': ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december'],
        'date': _nl_date, 'at': lambda t: f' om {t.hour}.{t.minute:02d} uur',
        'numbers': 'nul een twee drie vier vijf zes zeven acht negen tien elf twaalf dertien veertien vijftien zestien zeventien achttien negentien twintig'.split() + ['één'],
        'counts': {'afzonderlijke bronnen': 'sources', 'afzonderlijke fouten': 'errors', 'vastgestelde correcties': 'errors'},
        'disclaimer': ('Dit verslag werd opgesteld met behulp van AI-systemen en documentair opzoekingswerk. '
                       'De betrouwbaarheid ervan hangt af van de beschikbaarheid, de toegankelijkheid, de indexering en de bijwerking van de geraadpleegde bronnen, '
                       'waarvan de interfaces kunnen veranderen. Dat een verwijzing niet kon worden gecontroleerd, betekent niet dat ze onjuist is. '
                       'De conclusies gelden op de hierboven vermelde datum van de controles, zonder automatische bijwerking, '
                       'en vormen geen algemene certificering van betrouwbaarheid. Een menselijke controle blijft onontbeerlijk '
                       'vóór elk gebruik in een rechterlijke, procedurele, adviserende of wetenschappelijke context.'),
        'ui': {'established': 'Verslag opgesteld op ', 'hour_not_kept': ' (uur niet bewaard)', 'consulted_on': 'Bronnen geraadpleegd op ',
               'consulted_from': 'Bronnen geraadpleegd van ', 'to': ' tot ', 'revision': 'Herziening van ', 'replaces': ' (vervangt versie ',
               'revision_scope': 'Reikwijdte van de herziening: ', 'legal_date': 'Gehanteerde juridische peildatum: ', 'keep': 'Wat u moet onthouden',
               'stats': ['geïnventariseerde vermeldingen', 'afzonderlijke bronnen', 'afzonderlijke fouten'], 'corrections': 'Noodzakelijke correcties',
               'correction': 'Correctie: ', 'passage': 'Passage uit de bron: ', 'references': 'Verwijzingen en controles',
               'heads': ['Bron / verwijzing', 'Vindplaatsen', 'Resultaat'], 'cited': 'Geciteerde verwijzing: ',
               'cited_short': 'Geciteerde verwijzing (verkort): ', 'exact': 'Juiste verwijzing: ', 'limit': 'Beperking: ',
               'attribution': 'Toeschrijving', 'version': 'Versie', 'translation': 'Vertaling', 'quote': ' · citaat: ',
               'fix_above': ' · correctie nodig (zie hierboven)', 'confirmed': 'Zonder voorbehoud bevestigde verwijzingen',
               'one_quote': ' Citaat conform.', 'n_quotes': ' {} citaten conform.', 'suggestions': 'Facultatieve suggesties',
               'limits': 'Beperkingen en traceerbaarheid', 'method': 'Gevolgde methode', 'skill_version': 'Versie van de skill: ',
               'disclaimer': 'Waarschuwing', 'proof': 'Bewijs', 'consulted': ' · geraadpleegd op ', 'q_open': '“', 'q_close': '”'},
    },
    'de': {
        'status': {'VERIFIED': 'Fundstelle überprüft', 'VERIFIED_WITH_ANOMALY': 'Fundstelle identifiziert, Korrektur erforderlich',
                   'PARTIALLY_VERIFIED': 'Teilweise überprüft',
                   'NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES': 'Mit den zugänglichen Quellen nicht überprüfbar',
                   'NOT_FOUND_OR_CONTRADICTORY': 'Fundstelle nicht auffindbar oder Widerspruch festgestellt'},
        'text': {'EXACT': 'Text übereinstimmend', 'EXACT_WITH_SIGNALLED_ADAPTATIONS': 'Text übereinstimmend, mit kenntlich gemachten Anpassungen',
                 'MINOR_DEVIATION': 'Geringfügige Abweichung', 'INEXACT': 'Unzutreffendes Zitat', 'NOT_VERIFIABLE': 'Zitat nicht überprüfbar',
                 'NOT_APPLICABLE_TRANSLATION': 'Übersetzung gesondert geprüft'},
        'quote_short': {'MINOR_DEVIATION': 'geringfügige Abweichung', 'INEXACT': 'unzutreffend', 'NOT_VERIFIABLE': 'nicht überprüfbar'},
        'integrity': {'FAITHFUL': 'Sinn gewahrt', 'MATERIAL_BUT_NOT_MISLEADING': 'Wesentliche Änderung, ohne Sinnentstellung',
                      'MISLEADING': 'Sinn entstellt', 'NOT_VERIFIABLE': 'Auswirkung auf den Sinn nicht überprüfbar'},
        'severity': {'CRITICAL': 'Kritische Priorität', 'MAJOR': 'Wichtige Korrektur', 'MINOR': 'Punktuelle Korrektur', 'INFORMATION': 'Information'},
        'months': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
        'date': _de_date, 'at': lambda t: f' um {t.hour}:{t.minute:02d} Uhr',
        'numbers': 'null eins zwei drei vier fünf sechs sieben acht neun zehn elf zwölf dreizehn vierzehn fünfzehn sechzehn siebzehn achtzehn neunzehn zwanzig'.split() + ['ein', 'eine'],
        'counts': {'unterschiedliche quellen': 'sources', 'unterschiedliche fehler': 'errors', 'festgestellte korrekturen': 'errors'},
        'disclaimer': ('Dieser Bericht wurde mit Unterstützung von KI-Systemen und durch Dokumentenrecherche erstellt. '
                       'Seine Verlässlichkeit hängt von der Verfügbarkeit, Zugänglichkeit, Indexierung und Aktualisierung der herangezogenen Quellen ab, '
                       'deren Benutzeroberflächen sich ändern können. Dass eine Fundstelle nicht überprüft werden konnte, bedeutet nicht, dass sie falsch ist. '
                       'Die Ergebnisse gelten zum oben angegebenen Datum der Überprüfung, ohne automatische Aktualisierung, '
                       'und stellen keine allgemeine Zertifizierung der Verlässlichkeit dar. Eine menschliche Überprüfung bleibt unerlässlich, '
                       'bevor der Bericht gerichtlich, im Verfahren, in der Beratung oder wissenschaftlich verwendet wird.'),
        'ui': {'established': 'Bericht erstellt am ', 'hour_not_kept': ' (Uhrzeit nicht festgehalten)', 'consulted_on': 'Quellen herangezogen am ',
               'consulted_from': 'Quellen herangezogen vom ', 'to': ' bis ', 'revision': 'Überarbeitung vom ', 'replaces': ' (ersetzt Version ',
               'revision_scope': 'Umfang der Überarbeitung: ', 'legal_date': 'Zugrunde gelegter rechtlicher Stichtag: ', 'keep': 'Das Wichtigste',
               'stats': ['erfasste Nennungen', 'unterschiedliche Quellen', 'unterschiedliche Fehler'], 'corrections': 'Erforderliche Korrekturen',
               'correction': 'Korrektur: ', 'passage': 'Belegstelle: ', 'references': 'Fundstellen und Prüfungen',
               'heads': ['Quelle / Fundstelle', 'Stellen im Dokument', 'Ergebnis'], 'cited': 'Zitierte Fundstelle: ',
               'cited_short': 'Zitierte Fundstelle (verkürzt): ', 'exact': 'Zutreffende Fundstelle: ', 'limit': 'Einschränkung: ',
               'attribution': 'Zuordnung', 'version': 'Fassung', 'translation': 'Übersetzung', 'quote': ' · Zitat: ',
               'fix_above': ' · Korrektur erforderlich (siehe oben)', 'confirmed': 'Ohne Vorbehalt bestätigte Fundstellen',
               'one_quote': ' Zitat übereinstimmend.', 'n_quotes': ' {} Zitate übereinstimmend.', 'suggestions': 'Fakultative Vorschläge',
               'limits': 'Grenzen und Nachvollziehbarkeit', 'method': 'Vorgehen', 'skill_version': 'Version des Skills: ',
               'disclaimer': 'Hinweis', 'proof': 'Beleg', 'consulted': ' · herangezogen am ', 'q_open': '„', 'q_close': '“'},
    },
    'en': {
        'status': {'VERIFIED': 'Reference verified', 'VERIFIED_WITH_ANOMALY': 'Reference identified, correction needed',
                   'PARTIALLY_VERIFIED': 'Partially verified',
                   'NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES': 'Not verifiable with accessible sources',
                   'NOT_FOUND_OR_CONTRADICTORY': 'Reference not found or contradicted'},
        'text': {'EXACT': 'Text matches', 'EXACT_WITH_SIGNALLED_ADAPTATIONS': 'Text matches, with signalled adaptations',
                 'MINOR_DEVIATION': 'Minor deviation', 'INEXACT': 'Inaccurate quotation', 'NOT_VERIFIABLE': 'Quotation not verifiable',
                 'NOT_APPLICABLE_TRANSLATION': 'Translation checked separately'},
        'quote_short': {'MINOR_DEVIATION': 'minor deviation', 'INEXACT': 'inaccurate', 'NOT_VERIFIABLE': 'not verifiable'},
        'integrity': {'FAITHFUL': 'Meaning preserved', 'MATERIAL_BUT_NOT_MISLEADING': 'Material change, meaning not distorted',
                      'MISLEADING': 'Meaning distorted', 'NOT_VERIFIABLE': 'Effect on meaning not verifiable'},
        'severity': {'CRITICAL': 'Critical priority', 'MAJOR': 'Important correction', 'MINOR': 'Minor correction', 'INFORMATION': 'Information'},
        'months': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'date': _en_date, 'at': lambda t: f' at {t.hour}:{t.minute:02d}',
        'numbers': 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty'.split(),
        'counts': {'distinct sources': 'sources', 'distinct errors': 'errors', 'established corrections': 'errors'},
        'disclaimer': ('This report was prepared with the assistance of AI systems and documentary research. '
                       'Its reliability depends on the availability, accessibility, indexing and updating of the sources consulted, '
                       'whose interfaces may change. A reference that could not be verified is not thereby wrong. '
                       'The conclusions speak as of the verification dates stated above, with no automatic update, '
                       'and are not a general certification of reliability. Human review remains essential '
                       'before any use in court, in proceedings, in advice or in scholarship.'),
        'ui': {'established': 'Report prepared on ', 'hour_not_kept': ' (time not recorded)', 'consulted_on': 'Sources consulted on ',
               'consulted_from': 'Sources consulted from ', 'to': ' to ', 'revision': 'Revision of ', 'replaces': ' (replaces version ',
               'revision_scope': 'Scope of the revision: ', 'legal_date': 'Legal reference date: ', 'keep': 'Key points',
               'stats': ['occurrences listed', 'distinct sources', 'distinct errors'], 'corrections': 'Corrections needed',
               'correction': 'Correction: ', 'passage': 'Source passage: ', 'references': 'References and checks',
               'heads': ['Source / reference', 'Locations', 'Result'], 'cited': 'Reference as cited: ',
               'cited_short': 'Reference as cited (abridged): ', 'exact': 'Correct reference: ', 'limit': 'Limitation: ',
               'attribution': 'Attribution', 'version': 'Version', 'translation': 'Translation', 'quote': ' · quotation: ',
               'fix_above': ' · correction needed (see above)', 'confirmed': 'References confirmed without reservation',
               'one_quote': ' Quotation matches.', 'n_quotes': ' {} quotations match.', 'suggestions': 'Optional suggestions',
               'limits': 'Limitations and traceability', 'method': 'Method', 'skill_version': 'Skill version: ',
               'disclaimer': 'Disclaimer', 'proof': 'Evidence', 'consulted': ' · consulted on ', 'q_open': '“', 'q_close': '”'},
    },
}
L = LANG['fr']


def set_language(code):
    global L
    if code not in LANG:
        raise ValueError('Langue de rapport non prise en charge : ' + str(code) + ' (fr, nl, de, en)')
    L = LANG[code]


# Characters absent from the bundled Vera fonts, replaced in the PDF only (the Markdown keeps the original text).
PDF_GLYPHS = {'\u2010': '-', '\u2011': '-', '\u2012': '-', '\u202f': '\u00a0', '\u2009': ' ', '\u2192': '->'}


def pdf_text(text):
    return str(text).translate(str.maketrans(PDF_GLYPHS))




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
    label = L['status'][r['status']]
    quotes = [q for q in data['quotations'] if q['record_id'] == r['id'] and q['status'] in L['quote_short']]
    if quotes:
        label += L['ui']['quote'] + ' ; '.join(dict.fromkeys(L['quote_short'][q['status']] for q in quotes))
    elif r['status'] == 'VERIFIED' and any(f.get('kind') == 'error' for f in r.get('findings', [])):
        label += L['ui']['fix_above']
    return label


def reference_tone(r, data):
    quotes = [q for q in data['quotations'] if q['record_id'] == r['id']]
    if r['status'] in ('VERIFIED_WITH_ANOMALY', 'NOT_FOUND_OR_CONTRADICTORY') or any(f.get('kind') == 'error' for f in r.get('findings', [])) \
            or any(q['status'] == 'INEXACT' or q['integrity'] == 'MISLEADING' for q in quotes):
        return 'bad'
    if r['status'] == 'PARTIALLY_VERIFIED' or any(q['status'] == 'MINOR_DEVIATION' for q in quotes):
        return 'warn'
    if r['status'] == 'NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES':
        return 'muted'
    return 'ok'


def quote_tone(q):
    if q['status'] == 'INEXACT' or q['integrity'] == 'MISLEADING':
        return 'bad'
    if q['status'] in ('MINOR_DEVIATION', 'NOT_APPLICABLE_TRANSLATION') or q['integrity'] == 'MATERIAL_BUT_NOT_MISLEADING':
        return 'warn'
    if q['status'] == 'NOT_VERIFIABLE':
        return 'muted'
    return 'ok'


def clean_record(r, data):
    # Confirmed without reservation: shown as a compact annex line instead of a full card.
    return (r['status'] == 'VERIFIED' and not r.get('findings') and not r['limits'] and not r.get('notes')
            and all(q['status'] in QUOTE_OK and q['integrity'] == 'FAITHFUL' for q in data['quotations'] if q['record_id'] == r['id']))


def human_date(value):
    return L['date'](date.fromisoformat(value[:10]))


def human_moment(value, precision='second'):
    if precision == 'day' or len(value) <= 10:
        return human_date(value)
    t = datetime.fromisoformat(value)
    return human_date(value) + L['at'](t)


def check_summary_counts(data, counts):
    # The summary is free prose: any figure it gives for these totals must match the computed tiles.
    words = {w: i for i, w in enumerate(L['numbers'][:21])}
    words.update({w: 1 for w in L['numbers'][21:]})
    pattern = r"(?<![\w-])(\d+|[^\W\d_][\w-]*)\s+(" + '|'.join(re.escape(k) for k in L['counts']) + ')'
    for m in re.finditer(pattern, data['summary'].lower()):
        word, what = m.group(1), m.group(2)
        n = int(word) if word.isdigit() else words.get(word)
        expected = counts[L['counts'][what]]
        if n is not None and n != expected:
            raise ValueError(f'Synthèse incohérente : « {m.group(0)} » alors que le rapport en compte {expected}')


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


def bare_excerpt(text):
    # The renderer adds its own guillemets; drop one enclosing pair supplied with the excerpt.
    text = str(text).strip()
    for left, right in (('«', '»'), ('“', '”'), ('"', '"')):
        if text.startswith(left) and text.endswith(right) and len(text) > 1:
            return text[len(left):-len(right)].strip()
    return text


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
    set_language(data.get('report_language', 'fr'))
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
        if r['status'] not in L['status']:
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
            if f.get('severity') not in L['severity'] or not f.get('problem') or not f.get('action'):
                raise ValueError('Constat incomplet : ' + r['id'])
    qids = set()
    for q in data['quotations']:
        for key in ('id', 'record_id', 'title', 'location', 'status', 'integrity', 'comparison', 'context'):
            if not q.get(key):
                raise ValueError('Citation incomplète : ' + key)
        if q['id'] in qids or q['record_id'] not in {r['id'] for r in data['records']}:
            raise ValueError('Identifiant ou rattachement de citation invalide')
        qids.add(q['id'])
        if q['status'] not in L['text'] or q['integrity'] not in L['integrity']:
            raise ValueError('Statut de citation inconnu')
        if q['status'] == 'NOT_APPLICABLE_TRANSLATION' and not q.get('translation_assessment'):
            raise ValueError('La traduction exige une appréciation distincte')
    unique_findings(data)
    unique_findings(data, 'suggestion')
    check_summary_counts(data, {'sources': len({r['source_id'] for r in data['records']}), 'errors': len(unique_findings(data))})
    return data


def proof_link(proof, locators):
    loc = ' ; '.join(locators) + ' · ' + proof['language']
    details = [proof[k] for k in ('version', 'basis') if proof.get(k)]
    if details: loc += ' (' + ', '.join(details) + ')'
    if proof.get('consulted_on'): loc += L['ui']['consulted'] + human_date(proof['consulted_on'])
    return (proof['label'], proof['url'], loc)


def sections(data):
    """Compact canonical tree; no research, status inference, or automatic dating."""
    set_language(data.get('report_language', 'fr'))
    u = L['ui']
    m = report_dates(data)
    errors = unique_findings(data)
    suggestions = unique_findings(data, 'suggestion')
    quoted = lambda text: u['q_open'] + text + u['q_close']
    yield ('title', data['title'])
    yield ('subtitle', data['document'])
    yield ('meta', u['established'] + human_moment(m['established_at'], m['precision']) + (u['hour_not_kept'] if m['precision'] == 'day' else ''))
    start, end = m['checks_started_on'], m['checks_completed_on']
    yield ('meta', u['consulted_on'] + human_date(end) if start == end else u['consulted_from'] + human_date(start) + u['to'] + human_date(end))
    if m.get('revision'):
        rev = m['revision']
        yield ('meta', u['revision'] + human_moment(rev['issued_at']) + u['replaces'] + rev['previous_version'] + ')')
        yield ('p', u['revision_scope'] + rev['scope'])
    yield ('meta', u['legal_date'] + m['legal_reference'])
    yield ('h1', u['keep'])
    yield ('p', clean_prose(data['summary']))
    yield ('stats', list(zip([str(sum(1 + len(r.get('additional_occurrences', [])) for r in data['records'])),
                              str(len({r['source_id'] for r in data['records']})), str(len(errors))], u['stats'])))
    yield ('p', clean_prose(data['scope']))
    if errors:
        yield ('h1', u['corrections'])
        for r, f in errors:
            yield ('card_start', None)
            yield ('h2', r['title'] + ' · ' + L['severity'][f['severity']])
            locations = list(dict.fromkeys(x['location'] for x in data['records'] if any(y['id'] == f['id'] for y in x.get('findings', []))))
            yield ('meta', ' ; '.join(locations))
            yield ('p', clean_prose(f['problem']))
            yield ('p', u['correction'] + clean_prose(f['action']))
            for proof in r['sources']:
                if proof.get('excerpt'):
                    yield ('p', u['passage'] + quoted(bare_excerpt(proof['excerpt'])))
                    yield ('link', proof_link(proof, [proof['locator']]))
            yield ('card_end', None)
    groups = {}
    for r in data['records']:
        groups.setdefault(r['source_id'], []).append(r)
    yield ('h1', u['references'])
    rows = []
    for group in groups.values():
        labels = list(dict.fromkeys(reference_label(r, data) for r in group))
        rows.append((group[0]['title'], ' ; '.join(dict.fromkeys(r['location'] for r in group)), ' ; '.join(labels)))
    yield ('table', (u['heads'], rows))
    annex = [g for g in groups.values() if all(clean_record(r, data) for r in g)]
    for group in (g for g in groups.values() if g not in annex):
        yield ('card_start', None)
        yield ('h2', group[0]['title'])
        for r in group:
            yield ('badge', (reference_label(r, data), reference_tone(r, data)))
            yield ('meta', r['location'])
            yield ('p', (u['cited_short'] if r.get('original_kind') == 'summary' else u['cited']) + r['original'])
            if r['checked'] != r['original']:
                yield ('p', u['exact'] + clean_prose(r['checked']))
            for check in r['checks']:
                yield ('bullet', clean_prose(check))
            if r['limits']: yield ('p', u['limit'] + clean_prose(r['limits']))
            for note in r.get('notes', []): yield ('p', clean_prose(note))
            for q in (q for q in data['quotations'] if q['record_id'] == r['id']):
                yield ('meta', q['title'] + ' · ' + q['location'])
                yield ('badge', (L['text'][q['status']] + ' · ' + L['integrity'][q['integrity']], quote_tone(q)))
                yield ('p', clean_prose(q['comparison']))
                yield ('p', clean_prose(q['context']))
                for key in ('attribution', 'temporal_assessment', 'translation_assessment'):
                    label = {'attribution': u['attribution'], 'temporal_assessment': u['version'], 'translation_assessment': u['translation']}[key]
                    if q.get(key): yield ('p', label + ' : ' + clean_prose(q[key]) if L is LANG['fr'] else label + ': ' + clean_prose(q[key]))
        proof_groups = {}
        for r in group:
            for proof in r['sources']:
                key = tuple(proof.get(k, '') for k in ('url', 'language', 'version', 'basis', 'consulted_on'))
                entry = proof_groups.setdefault(key, {'proof': proof, 'locators': [], 'excerpts': []})
                if proof['locator'] not in entry['locators']: entry['locators'].append(proof['locator'])
                if proof.get('excerpt') and not any(f['kind'] == 'error' for f in r.get('findings', [])):
                    if proof['excerpt'] not in entry['excerpts']: entry['excerpts'].append(proof['excerpt'])
        for entry in proof_groups.values():
            for excerpt in entry['excerpts']: yield ('p', u['passage'] + quoted(bare_excerpt(excerpt)))
            yield ('link', proof_link(entry['proof'], entry['locators']))
        yield ('card_end', None)
        yield ('space', None)
    if annex:
        yield ('h1', u['confirmed'])
        for group in annex:
            locations = ' ; '.join(dict.fromkeys(r['location'] for r in group))
            quotes = [q for q in data['quotations'] if q['record_id'] in {r['id'] for r in group}]
            extra = u['one_quote'] if len(quotes) == 1 else (u['n_quotes'].format(len(quotes)) if quotes else '')
            yield ('bullet', group[0]['title'] + ' (' + locations + ').' + extra)
            seen = set()
            for r in group:
                for proof in r['sources']:
                    if proof['url'] not in seen:
                        seen.add(proof['url'])
                        yield ('link', proof_link(proof, [proof['locator']]))
    if suggestions:
        yield ('h1', u['suggestions'])
        for r, f in suggestions:
            yield ('p', r['location'] + ' : ' + clean_prose(f['problem']) + ' ' + clean_prose(f['action']))
    yield ('h1', u['limits'])
    for item in data['limitations']: yield ('bullet', clean_prose(item))
    yield ('keep_start', None)
    yield ('h2', u['method'])
    for item in data['method']: yield ('bullet', clean_prose(item))
    yield ('meta', u['skill_version'] + (data.get('skill_version') or data['version']))
    yield ('h2', u['disclaimer'])
    yield ('callout', L['disclaimer'])
    yield ('keep_end', None)


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
            result.append(f"{L['ui']['proof']}{' :' if L is LANG['fr'] else ':'} [{label}]({url}) — {loc}.")
        elif kind == 'callout':
            result.append('> ' + value)
        elif kind == 'bullet':
            result.append('- ' + value)
        elif kind == 'badge':
            result.append(value[0])
        elif kind not in ('space', 'page', 'card_start', 'card_end', 'keep_start', 'keep_end'):
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
    paragraph = lambda text, name='p': Paragraph(escape(pdf_text(text)), styles[name])
    story = []
    card_index = None
    keep_index = None
    for kind, value in nodes:
        if kind == 'keep_start':
            # Closing block (method, skill version, disclaimer) moves as one unit: no page holding only the disclaimer.
            keep_index = len(story)
        elif kind == 'keep_end':
            block = story[keep_index:]
            del story[keep_index:]
            story.append(KeepTogether(block))
            keep_index = None
        elif kind == 'card_start':
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
            story.append(Paragraph(f"{L['ui']['proof']}{' :' if L is LANG['fr'] else ':'} " + f'<link href="{escape(url,quote=True)}" color="{teal}">{escape(pdf_text(label))}</link> — {escape(pdf_text(loc))}.', styles['link']))
            story.append(paragraph(url, 'url'))
        elif kind == 'bullet':
            story.append(paragraph('• ' + value))
        elif kind == 'badge':
            text, tone = value
            color = {'ok': '#17685F', 'bad': '#A32722', 'warn': '#805500', 'muted': '#52616B'}[tone]
            story.append(Paragraph(escape(pdf_text(text)), style('status', 9, 13, color, True, keepWithNext=True)))
        else:
            if kind == 'h1':
                story.append(CondPageBreak(100))
            if kind == 'h2' and keep_index is None:
                story.append(CondPageBreak(115))
            story.append(paragraph(value, kind))
    def furniture(canvas, doc):
        canvas.setStrokeColor(colors.HexColor('#D9E1E4'));canvas.line(50,39,545,39)
        canvas.setFont('AuditRegular',8);canvas.setFillColor(colors.HexColor(muted))
        canvas.drawString(50,25,pdf_text(L['ui']['established'] + human_date(data['report_metadata']['established_at'])))
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
