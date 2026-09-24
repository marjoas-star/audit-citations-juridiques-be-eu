# Contrôle des trois citations simulées

Audit du 24 septembre 2026. Application de `SKILL.md` et `schemas/citation-record.md`. Comparaison limitée aux textes fournis ; aucune recherche externe ni consultation d’historique. L’identité, la version et le localisateur juridique ne sont établis pour aucune entrée. Aucun intitulé, auteur, institution, numéro ou identifiant juridique n’est déduit des mots.

## AUDIT_CONTEXT

- `id`: AUDCTX-ELLIPSES
- `input_documents`: message contenant les entrées E1, E2 et E3
- `scope`: niveau 2, contrôle textuel et intégrité des adaptations dans le corpus simulé ; niveau 1 non vérifiable ; aucun avis de niveau 3
- `document_language`, `report_language`: français
- `document_date`, `author_legal_cutoff_date`: inconnues
- `audit_date`: 2026-09-24
- `source_ids`: SRC-12, SRC-3
- `occurrence_ids`: OCC-E1, OCC-E2, OCC-E3
- `quotation_ids`: QUO-E1, QUO-E2, QUO-E3
- `internal_reference_count`: 0
- `counts`: 3 occurrences ; 2 groupes de source d’entrée (sans prétendre identifier deux documents juridiques distincts) ; 2 comparaisons textuelles réalisées ; 1 citation non vérifiable ; 0 identité documentaire vérifiée

## SOURCE_RECORD

**SRC-12** : source textuelle fournie commune à E1 et E2. `source_type: OTHER` ; `original_reference: non fournie` ; `verified_reference: null` ; `reference_status: NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES` ; `severity: INFORMATION`. Langue de l’extrait : français. Identifiants et champs documentaires : inconnus. `evidence.overall_level: UNVERIFIED` pour l’authenticité et l’identité documentaires ; `per_field: {}`. `discovery_source`: entrée simulée ; `verification_source`: extrait du message, uniquement comme comparateur local. Version et dates de la source inconnues.

**SRC-3** : source non fournie pour E3. Même statut de référence et même niveau de preuve. Langue de citation : français ; langue de source : inconnue. `verification_source: null`. Ne pas fusionner cette source avec SRC-12 sur la seule ressemblance des citations.

L’absence de vérification ne signifie pas que les références sont erronées. Le niveau `UNVERIFIED` ne nie pas la possibilité de comparer les chaînes expressément fournies ; il interdit d’en déduire une vérification officielle.

## OCCURRENCE_RECORD et QUOTATION_RECORD — E1

- `id`: OCC-E1 ; `source_id`: SRC-12 ; `reference_status`: NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES ; `audit_record_ids`: [AUD-E1]. Localisation : entrée E1 du message, sans page ni paragraphe juridique vérifié.
- `original_text` / `quoted_text` : « La motivation exigée consiste […] dans l’acte, des considérations de droit et de fait servant de fondement à la décision. Elle doit être adéquate. »
- `id` de citation : QUO-E1 ; `occurrence_id`: OCC-E1.
- `source_text` : « La motivation exigée consiste en l’indication, dans l’acte, des considérations de droit et de fait servant de fondement à la décision. Elle doit être adéquate. »
- `textual_status`: EXACT_WITH_SIGNALLED_ADAPTATIONS, **uniquement au regard de l’extrait fourni**. Les mots conservés sont reproduits sans substitution. Ce statut ne valide pas la citation adaptée.
- Adaptation : `OMISSION`, signalée par `[…]` ; suppression exacte : « en l’indication, ».
- `quotation_adaptation.overall_integrity`: MISLEADING.
- Motif : la suppression retire le complément de « consiste » et le nom « indication », dont dépend « des considérations ». La suite « consiste […] dans l’acte, des considérations » est grammaticalement défectueuse et efface l’exigence d’indiquer ces considérations. La présence du signe d’ellipse ne répare pas cette altération.
- `source_version`: inconnue ; `source_language` et `citation_language`: français ; traduction : sans objet.
- `locator_verified`: false ; `evidence_attempt_ids`: [SEA-E1] ; `compared_scope`: les deux phrases fournies ; `omitted_context_consulted`: oui, pour l’omission située dans cet extrait ; contexte au-delà de celui-ci inconnu.

**AUD-E1** — catégorie `ELLIPSIS_ALTERS_SYNTAX_AND_MEANING` (suppression qui altère grammaire et sens) ; `severity: CRITICAL` ; `status: constat établi dans l’extrait simulé`. Correction établie : rétablir « en l’indication, », donc reproduire le `source_text` ci-dessus. Aucune correction d’identité ou de référence n’est proposée.

## OCCURRENCE_RECORD et QUOTATION_RECORD — E2

- `id`: OCC-E2 ; `source_id`: SRC-12 ; `reference_status`: NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES ; `audit_record_ids`: [AUD-E2]. Localisation : entrée E2 du message.
- `original_text` / `quoted_text` : « La motivation exigée consiste en l’indication, dans l’acte, des considérations de droit […] servant de fondement à la décision. »
- `id` de citation : QUO-E2 ; `occurrence_id`: OCC-E2 ; `source_text`: même extrait intégral que pour E1.
- `textual_status`: EXACT_WITH_SIGNALLED_ADAPTATIONS, **uniquement au regard de l’extrait fourni**. Les mots reproduits concordent ; l’exactitude matérielle des fragments ne garantit pas leur fidélité d’ensemble.
- Adaptation interne : `OMISSION`, signalée ; mots supprimés : « et de fait ».
- `quotation_adaptation.overall_integrity`: MISLEADING.
- Motif : la grammaire reste correcte, mais l’ellipse efface le second terme de l’exigence cumulative « de droit et de fait ». La citation donne ainsi une portée réduite à l’exigence exprimée par la source. C’est une altération matérielle, non une simple abréviation fidèle.
- Limite finale également observée : la citation s’arrête après la première phrase ; « Elle doit être adéquate. » n’est pas reproduit et aucune ellipse finale n’est affichée. Citer une seule phrase n’impose pas, en soi, de signaler toutes les phrases suivantes. Néanmoins, cette seconde phrase ajoute une exigence ; le contexte d’utilisation manque pour déterminer si cette limitation finale induit, elle aussi, le lecteur en erreur. Elle ne neutralise pas l’altération interne déjà établie.
- `source_version`: inconnue ; `source_language` et `citation_language`: français ; traduction : sans objet.
- `locator_verified`: false ; `evidence_attempt_ids`: [SEA-E2] ; `compared_scope`: citation et deux phrases sources fournies ; `omitted_context_consulted`: oui dans l’extrait fourni, sans accès au document complet.

**AUD-E2** — catégorie `ELLIPSIS_REMOVES_CUMULATIVE_REQUIREMENT` (suppression d’une composante cumulative) ; `severity: CRITICAL` ; `status: constat établi dans l’extrait simulé`. Correction minimale établie : « La motivation exigée consiste en l’indication, dans l’acte, des considérations de droit et de fait servant de fondement à la décision. » Si l’on entend restituer l’ensemble des exigences figurant dans l’extrait fourni, conserver aussi « Elle doit être adéquate. » Aucun contexte juridique supplémentaire n’est présumé.

## OCCURRENCE_RECORD et QUOTATION_RECORD — E3

- `id`: OCC-E3 ; `source_id`: SRC-3 ; `reference_status`: NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES ; `audit_record_ids`: [AUD-E3]. Localisation : entrée E3 du message.
- `original_text` / `quoted_text` : « La motivation exigée consiste […] dans l’acte. »
- `id` de citation : QUO-E3 ; `occurrence_id`: OCC-E3 ; `source_text`: null.
- `textual_status`: NOT_VERIFIABLE.
- Adaptation : `OMISSION`, signalée par `[…]` ; contenu supprimé inconnu.
- `quotation_adaptation.overall_integrity`: NOT_VERIFIABLE.
- Motif : ni les mots conservés ni le contexte supprimé ne peuvent être comparés à une source. La formulation apparente peut appeler une vérification, mais elle ne permet pas de reconstruire l’omission ni d’affirmer que celle-ci est fidèle ou trompeuse. Le comparateur d’E1/E2 ne peut pas être attribué à E3 sans preuve.
- `source_version` et `source_language`: inconnues ; `citation_language`: français ; traduction : non déterminée.
- `locator_verified`: false ; `evidence_attempt_ids`: [] ; `compared_scope`: aucun texte source disponible ; `omitted_context_consulted`: non.

**AUD-E3** — catégorie `SOURCE_TEXT_UNAVAILABLE` ; `severity: INFORMATION` ; `status: non vérifiable`. Correction : aucune correction textuelle établie. Obtenir la source et le passage environnant avant toute validation ; ne pas compléter la citation par analogie.

## SEARCH_ATTEMPT — opérations effectivement réalisées

**SEA-E1** : `source_id: SRC-12` ; `source_or_database: message d’entrée` ; `operation: compare` ; `status: SUCCESS` ; résultat : mots conservés concordants et suppression « en l’indication, » localisée ; `evidence_level: UNVERIFIED` pour la preuve documentaire ; `document_type: extrait textuel simulé` ; `source_language: français` ; `consulted_locator: extrait fourni pour E1/E2` ; `observed_url: null` ; `url_origin: null` ; `technical_error: null` ; `timestamp: 2026-09-24, heure non enregistrée` ; `trace_path: présent rapport, textes reproduits sous E1`.

**SEA-E2** : mêmes paramètres de provenance ; `operation: compare` ; `status: SUCCESS` ; résultat : mots conservés concordants, suppression « et de fait » localisée, seconde phrase hors citation ; `trace_path: présent rapport, textes reproduits sous E1 et E2`.

Aucune tentative externe n’a été exécutée. L’indisponibilité de la source E3 n’est qualifiée ni de panne technique ni d’absence de résultat de recherche.

## Limites

Les deux statuts textuels positifs ne portent que sur les mots des extraits simulés. Ils coexistent avec une intégrité `MISLEADING` et avec des identités documentaires non vérifiées. E3 reste non vérifiable sur les deux axes. Rapport assisté par IA, dépendant des éléments accessibles et à soumettre à une vérification humaine avant réutilisation juridique ; il ne constitue pas une authentification de source ni un avis juridique. Les interfaces externes et leur évolution n’ont pas été contrôlées. Aucune garantie au-delà des comparaisons décrites n’est formulée, dans les limites permises par le droit applicable.
