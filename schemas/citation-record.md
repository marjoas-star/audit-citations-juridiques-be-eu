# Schéma des données d'audit

## Identifiants

- `SRC-...` : source
- `OCC-...` : occurrence
- `QUO-...` : citation textuelle
- `SEA-...` : tentative de recherche
- `AUD-...` : constat d'audit

## AUDIT_CONTEXT

Convention documentaire, pas un schéma exécutable : les objets peuvent être conservés en Markdown ou en données structurées sans inventer une validation informatique.

```yaml
id:
input_documents: []
scope:
document_language:
report_language:
author_legal_cutoff_date:
document_date:
audit_date:
source_ids: []
occurrence_ids: []
quotation_ids: []
internal_reference_count:
counts: {}  # calculés depuis les registres finaux, pas depuis une estimation
limitations: []
```

`AUDIT_RECORD` ci-dessous désigne un constat individuel. `AUDIT_CONTEXT` décrit l'audit entier. Les différentes dates peuvent être inconnues ; une date d'export n'est pas une date de rédaction.

## SOURCE_RECORD

```yaml
id:
source_type:
original_reference:
verified_reference:
reference_status:
severity:
languages:
  citation_language:
  source_language:
identifiers:
  ecli:
  celex:
  eli:
  numac:
  docket:
  decision_number:
  doi:
  isbn:
fields:
  title:
  court_or_institution:
  date:
  parties:
  document_type:
  document_version:
  document_status:  # consultation / final / revised, si établi
  adoption_date:
  announcement_date:
  oj_publication_date:
  notification_date:
  entry_into_force_date:
  base_act:
  enabling_provision:
  operative_provision_implemented:
evidence:
  overall_level:
  per_field: {}
discovery_source:
verification_source:
relations: []
temporal_context:
  relevant_version_date:
  author_legal_cutoff_date:
  document_date:
  audit_date:
notes:
```

Dans `per_field`, chaque champ contrôlé contient `value`, `verification_status`, `evidence_level`, `attempt_id`, `document_type`, `source_language` et `locator`. Ne pas propager `overall_level` aux champs absents. Les données d'entrée restent distinctes des valeurs observées.

La preuve d'un candidat écarté ne justifie pas `PARTIALLY_VERIFIED` pour le document recherché. Lorsque seuls des liens d'affaire sont corroborés, conserver cette relation séparément : sans champ d'identité du document cible suffisamment établi, son statut reste `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES`. Réserver `NOT_FOUND_OR_CONTRADICTORY` à la contradiction effectivement établie, sans en déduire l'inexistence de la cible.

## OCCURRENCE_RECORD

```yaml
id:
source_id:
reference_status:  # statut de cette occurrence, distinct de celui de la source
audit_record_ids: []
location:
  page:
  paragraph:
  footnote:
original_text:
internal_reference_type:
internal_resolution:
```

## QUOTATION_RECORD

```yaml
id:
source_id:
occurrence_id:
quoted_text:
source_text:
textual_status:
source_version:
source_language:
citation_language:
quotation_adaptation:
  present:
  adaptations: []
  overall_integrity:
translation_status:
translation_fidelity:
locator_verified:
evidence_attempt_ids: []
compared_scope:
omitted_context_consulted:
```

Adaptations : `OMISSION`, `INSERTION`, `GRAMMATICAL_ADJUSTMENT`, `TYPOGRAPHICAL_ADJUSTMENT`, `EMPHASIS_ADDED`, `EMPHASIS_REMOVED`, `CORRECTION`, `TRANSLATION`, `OTHER`.

Intégrité : `FAITHFUL`, `MATERIAL_BUT_NOT_MISLEADING`, `MISLEADING`, `NOT_VERIFIABLE`.

## SEARCH_ATTEMPT

```yaml
id:
source_id:
source_or_database:
query:
status:
result:
evidence_level:
technical_error:
timestamp:
operation:  # search / open / compare
observed_url:
url_origin:  # lien affiché, résultat de recherche ou URL fournie ; jamais déduite
document_type:
source_language:
consulted_locator:
content_observation:  # contenu exploitable, page vide, erreur, contrôle d'accès...
trace_path:
```

`status` distingue notamment `SUCCESS`, `NO_RESULT`, `TECHNICAL_FAILURE`, `ACCESS_RESTRICTED`.

`result` peut préciser `RESULT_FOUND` pour une recherche réussie. Le succès de la recherche et celui de l'ouverture sont deux tentatives distinctes. Une opération non exécutée ne reçoit aucun résultat fictif. Un statut HTTP favorable ou un nom de fichier PDF ne prouve pas que le contenu a été obtenu : vérifier qu'il est non vide, exploitable et correspond au document demandé.

## AUDIT_RECORD

```yaml
id:
source_id:
occurrence_id:
category:
finding:
correction:
severity:
status:
evidence:
```

## Statuts de référence

- `VERIFIED`
- `VERIFIED_WITH_ANOMALY`
- `PARTIALLY_VERIFIED`
- `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES`
- `NOT_FOUND_OR_CONTRADICTORY`

## Niveaux de preuve

- `OFFICIAL_AUTHENTIC_PUBLICATION`
- `OFFICIAL_FULL_DOCUMENT`
- `OFFICIAL_METADATA`
- `OFFICIAL_SEARCH_RESULT`
- `INSTITUTIONAL_FULL_DOCUMENT`
- `PUBLISHER_FULL_DOCUMENT`
- `INSTITUTIONAL_METADATA`
- `RELIABLE_SECONDARY_CORROBORATION`
- `SEARCH_SNIPPET_ONLY`
- `UNVERIFIED`

## Cas particuliers

- `VALID_IDENTIFIER_WRONG_DOCUMENT`
- `SOURCE_ATTRIBUTION_UNCERTAIN`
- `MULTI_PROVISION_SEMANTIC_MISMATCH`
- `BIBLIOGRAPHIC_OMISSION`
- `TEMPORAL_UPDATE_REQUIRED`
- `POST_CUTOFF_LEGISLATIVE_CHANGE`
- `OUTDATED_LEGAL_POSITION`
- `INCOMPLETE_INSTITUTIONAL_REFERENCE`
- `IMPRECISE_BUT_IDENTIFIABLE_REFERENCE`
- `CORRECT_BUT_IMPRECISE_PROVISION`
- `CORRECT_AT_DOCUMENT_DATE_BUT_NOW_OUTDATED`
- `COLLECTIVE_HISTORICAL_SUPPORT`

Autres catégories explicites : `WRONG_PROVISION_LOCATOR`, `TRUNCATED_CASE_NUMBER`, `PROCEDURAL_STATUS_MISMATCH`. La liste de catégories est ouverte ; une nouvelle catégorie doit être expliquée par un constat traçable. Une source correctement identifiée peut avoir une occurrence fautive : conserver les deux statuts sans compter cette occurrence comme une nouvelle source.
