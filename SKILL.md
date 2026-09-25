---
name: audit-citations-juridiques-be-eu
description: >
  Audite les références, citations et sources contenues dans un document
  juridique, principalement en droit belge, droit de l'Union européenne et
  droit de la Convention européenne des droits de l'homme. Identifie les
  sources citées, vérifie leurs références au moyen de sources externes
  accessibles en privilégiant les sources officielles, contrôle les citations
  textuelles et l'intégrité de leurs adaptations, signale les anomalies et
  indique explicitement ce qui n'a pas pu être vérifié. Fonctionne nativement
  en français, néerlandais, allemand et anglais, communique l'avancement des
  audits longs et peut produire un rapport professionnel en PDF.
---

# Audit des citations juridiques — Belgique & Europe

## 1. Objet

Cette compétence audite les références juridiques d'un document complet.

Elle vise notamment : mémoires, conclusions, avis, notes juridiques, consultations, articles scientifiques, projets d'ouvrages, rapports, travaux universitaires et documents générés ou assistés par IA.

Elle recherche notamment :

- sources fictives ;
- références plausibles mais inexistantes ;
- identifiants appartenant à un autre document ;
- erreurs de numéro, date, rôle ou ECLI ;
- confusion entre documents d'une même affaire ;
- mauvaise version temporelle ;
- erreur de langue ;
- mauvaise édition ;
- citations inexactes ;
- citations tronquées de manière trompeuse ;
- références doctrinales inventées ou mal attribuées.

## 2. Principe directeur

> **Vérifier la source, jamais la vraisemblance de la référence.**

Ne jamais inventer, compléter ou reconstruire de mémoire : ECLI, CELEX, ELI, NUMAC, DOI, ISBN, numéro de rôle, numéro d'arrêt, numéro parlementaire ou URL profonde.

## 3. Ne jamais sur-vérifier

> **Le statut de vérification ne peut jamais être supérieur au niveau de preuve réellement obtenu.**

Une référence corroborée par une source secondaire fiable mais dont la fiche institutionnelle n'a pas pu être consultée n'est pas automatiquement `VERIFIED`.

Exemple :

```text
identité générale : fortement corroborée
ECLI : non vérifié
texte officiel : inaccessible
```

doit pouvoir produire `🟠 PARTIALLY_VERIFIED`.

## 4. Périmètre

### Belgique

- législation ;
- Cour constitutionnelle ;
- Conseil d'État ;
- Cour de cassation ;
- cours et tribunaux ;
- JUPORTAL ;
- Moniteur belge ;
- Justel ;
- RefLex ;
- travaux parlementaires fédéraux ;
- travaux des entités fédérées ;
- jurisprudence historique ;
- doctrine.

### Union européenne

- traités ;
- Charte ;
- règlements ;
- directives ;
- décisions ;
- actes délégués et d'exécution ;
- consolidations ;
- rectificatifs ;
- transposition ;
- travaux préparatoires ;
- procédures législatives ;
- CJUE ;
- Tribunal ;
- conclusions d'avocats généraux.

### CEDH

- arrêts ;
- décisions ;
- avis ;
- requêtes ;
- documents HUDOC ;
- versions linguistiques.

## 5. Types d'entrée

PDF, DOCX, Markdown, texte brut, HTML ou texte collé.

Préserver autant que possible : pagination, notes, paragraphes, tableaux, guillemets et langues.

Pour un renvoi interne, une cible absente du fichier principal peut se trouver dans un autre extrait déjà fourni. Vérifier les titres, pages et sections du corpus disponible avant de conclure que la cible est inaccessible ; ne pas présumer pour autant que ce corpus contient tout l’ouvrage.

## 6. Communication de progression

Pour tout audit suffisamment important pour nécessiter plusieurs recherches externes ou plusieurs phases de traitement, informer l'utilisateur dès le début que l'audit comporte plusieurs étapes.

Le message de départ doit expliquer brièvement que :

- les références sont d'abord inventoriées ;
- chaque source unique est ensuite vérifiée ;
- les citations textuelles font l'objet d'un contrôle séparé lorsqu'elles sont accessibles ;
- les recherches dans les bases officielles peuvent nécessiter plusieurs voies de vérification.

Ne pas donner de durée prévisionnelle artificielle.

## 7. Jalons de progression

Phases recommandées :

1. Inventaire ;
2. Classification et dédoublonnage ;
3. Vérification des sources ;
4. Contrôle des citations textuelles ;
5. Contrôles transversaux ;
6. Consolidation du rapport.

## 8. Compteurs de progression

Préférer des compteurs réels (`31/57 sources traitées`, `14/22 citations contrôlées`) à un pourcentage artificiellement précis.

Afficher lorsque pertinent : occurrences détectées, sources uniques, sources traitées, citations textuelles contrôlées et anomalies détectées.

## 9. Fréquence des mises à jour

Les mises à jour doivent correspondre à un changement réel d'état : inventaire terminé, passage à une nouvelle famille de sources, lot significatif de sources vérifiées, difficulté technique importante, anomalie majeure confirmée, début du contrôle des citations ou consolidation finale.

Ne pas produire de messages de progression simplement pour meubler.

## 10. Difficultés pendant l'audit

Lorsqu'une source ralentit la vérification, signaler sobrement la difficulté et ne jamais transformer une difficulté technique en inexistence juridique.

## 11. Audits courts

Pour quelques références simples, ne pas multiplier les mises à jour.

## 12. Workflow

```text
DOCUMENT
   ↓
inventaire
   ↓
détection des sources
   ↓
détection des citations textuelles
   ↓
résolution des renvois internes
   ↓
dédoublonnage
   ↓
classification
   ↓
routage
   ↓
recherche externe
   ↓
évaluation du niveau de preuve
   ↓
vérification des métadonnées
   ↓
contrôle textuel
   ↓
contrôle d'intégrité des adaptations
   ↓
rapport
```

## 13. Trois niveaux d'audit

### Niveau 1 — identité documentaire

Automatique. La source existe-t-elle et la référence correspond-elle au bon document ?

### Niveau 2 — fidélité citationnelle

Automatique lorsque le texte est accessible : fidélité textuelle puis intégrité des adaptations.

### Niveau 3 — soutien substantif

Seulement sur demande : la source soutient-elle réellement la proposition juridique formulée ?

Ne jamais confondre les niveaux.

## 14. Niveau de preuve

Valeurs :

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

Pour chaque champ ou citation déclaré vérifié, conserver le lien effectivement observé, la date de consultation, le type de document réellement ouvert, sa langue et le passage/localisateur contrôlé. L'accès à un document intégral ne signifie pas que tous ses champs ou passages ont été vérifiés. Un communiqué officiel reste un communiqué : il ne prouve pas les mots de l'arrêt.

Dans un arrêt, identifier qui s’exprime dans le passage cité : juridiction, partie, juridiction de renvoi ou texte reproduit. Une plage de paragraphes peut changer de locuteur ; ne pas attribuer à la Cour un argument de partie simplement parce qu’il figure dans son arrêt.

## 15. Ce qu'un snippet peut faire

Un snippet peut découvrir, orienter ou suggérer un candidat. Il ne peut pas à lui seul vérifier une citation textuelle, une page, un ECLI litigieux ou transformer une référence en `VERIFIED`.

## 16. Échec technique

Toujours distinguer `TECHNICAL_FAILURE` de `NO_RESULT`. Une panne, un timeout ou une interface inaccessible ne prouve aucune inexistence documentaire.

## 17. Statuts des références

- 🟢 `VERIFIED`
- 🟡 `VERIFIED_WITH_ANOMALY`
- 🟠 `PARTIALLY_VERIFIED`
- ⚪ `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES`
- 🔴 `NOT_FOUND_OR_CONTRADICTORY`

Pour ⚪ : **L'absence de vérification ne signifie pas que la référence est erronée.**

## 18. Inventaire

Avant recherche : identifier toutes les références et citations, repérer les renvois abrégés, relever la bibliographie et dédupliquer les sources. Ne pas corriger pendant cette phase.

## 19. Renvois internes

Résoudre d'abord `ibid.`, `idem`, `op. cit.`, `précité`, `supra`, `infra` dans le document. Si plusieurs sources restent possibles : `SOURCE_ATTRIBUTION_UNCERTAIN`. Ne pas utiliser le web pour deviner la source.

## 20. Typologie

Catégories principales : `BE_LEGISLATION`, `BE_CONSTITUTIONAL_COURT`, `BE_COUNCIL_OF_STATE`, `BE_CASSATION`, `BE_JUDICIARY`, `BE_PARLIAMENT_FEDERAL`, `BE_PARLIAMENT_FEDERATED`, `BE_HISTORICAL_CASELAW`, `EU_LEGISLATION`, `EU_CASELAW`, `EU_PREPARATORY_WORK`, `ECHR_CASELAW`, `DOCTRINE_BOOK`, `DOCTRINE_ARTICLE`, `DOCTRINE_CHAPTER`, `DOCTRINE_CASE_NOTE`, `DOCTRINE_ONLINE`, `DOCTRINE_THESIS`, `OTHER`.

## 21. Routage

Appliquer `references/routing.md`, puis le module spécialisé correspondant.

## 22. Source de découverte et source de preuve

Conserver séparément `discovery_source` et `verification_source`.

> **La base qui permet de trouver n'est pas nécessairement la source qui permet de vérifier.**

## 23. Modèle de données

Utiliser `schemas/citation-record.md` avec les objets `SOURCE_RECORD`, `OCCURRENCE_RECORD`, `QUOTATION_RECORD`, `SEARCH_ATTEMPT` et `AUDIT_RECORD`.

## 24. Original et corrigé

Toujours conserver `original` et `verified`. Une correction ne doit jamais effacer la référence originale.

## 25. Vérification par champ

Une source peut être identifiée tandis qu'un champ reste non vérifié : rôle vérifié, date corroborée, ECLI non vérifié, etc.

## 26. Identifiant valide mais mauvais document

Utiliser `VALID_IDENTIFIER_WRONG_DOCUMENT`. L'existence d'un identifiant ne suffit jamais ; vérifier qu'il désigne exactement le document cité.

## 27. Citation textuelle

Créer un `QUOTATION_RECORD` pour toute citation attribuée à une source. Contrôler source, version, langue, localisation, mots reproduits, suppressions, insertions et adaptations.

## 28. Statuts textuels

- ✅ `EXACT`
- 🟢 `EXACT_WITH_SIGNALLED_ADAPTATIONS`
- 🟡 `MINOR_DEVIATION`
- 🔴 `INEXACT`
- ⚪ `NOT_VERIFIABLE`
- `NOT_APPLICABLE_TRANSLATION` pour une traduction contrôlée séparément.

Une comparaison entre langues différentes ne produit pas `EXACT` : utiliser `NOT_APPLICABLE_TRANSLATION` et évaluer séparément la fidélité de traduction. Si la version citée est inconnue, ne pas supposer qu'il s'agit d'une traduction d'auteur. Toute ellipse exige un contrôle distinct de son intégrité ; si le contexte supprimé est inaccessible, cette intégrité reste `NOT_VERIFIABLE`.

## 29. Adaptations de citation

Types : `OMISSION`, `INSERTION`, `GRAMMATICAL_ADJUSTMENT`, `TYPOGRAPHICAL_ADJUSTMENT`, `EMPHASIS_ADDED`, `EMPHASIS_REMOVED`, `CORRECTION`, `TRANSLATION`, `OTHER`.

Une adaptation signalée n'est pas automatiquement acceptable.

## 30. Intégrité des adaptations

Valeurs : `FAITHFUL`, `MATERIAL_BUT_NOT_MISLEADING`, `MISLEADING`, `NOT_VERIFIABLE`.

Une citation peut être `EXACT_WITH_SIGNALLED_ADAPTATIONS` tout en étant `MISLEADING`.

## 31. Cas sensibles

Contrôle approfondi lorsqu'une adaptation touche : négation, condition, exception, délai, qualité d'une personne, compétence, modalité, causalité, obligation/faculté, réserve, articulation `et/ou` ou dispositif.

## 32. Ellipses

Pour `[...]`, vérifier ce qui a été supprimé, la grammaire résultante, la portée résultante et l'existence éventuelle d'une réserve supprimée.

## 33. Crochets

Vérifier l'antécédent, l'identité et l'absence d'élargissement/réduction de la règle.

## 34. Traductions

Appliquer `references/language-policy.md`. Valeurs de fidélité : `FAITHFUL`, `FAITHFUL_WITH_MINOR_VARIATION`, `PARTIALLY_FAITHFUL`, `MISLEADING`, `NOT_VERIFIABLE`.

## 35. Multilinguisme

Le skill travaille en français, néerlandais, allemand et anglais. Distinguer `document_language`, `citation_language`, `source_language`, `report_language`. Identifier avant de traduire.

## 36. Taxonomies

Ne jamais supposer qu'une taxonomie linguistique est la traduction exacte d'une autre. Règle critique : `juriDict FR ≠ traduction de juriDict NL`.

## 37. Législation belge

Router vers `references/moniteur-belge-justel.md`; RefLex peut aider pour les relations. Vérifier acte, publication, version temporelle, entrée en vigueur, modifications et rectificatifs.

## 38. Droit de l'Union

Router vers `references/eur-lex-legislation.md`. Distinguer acte publié, version consolidée, document préparatoire et procédure.

Ce module précise aussi les références au JO depuis octobre 2023, les titres abrégés, les dates institutionnelles et les versions de lignes directrices. Distinguer une erreur documentaire d'une harmonisation éditoriale ; pour un acte délégué ou d'exécution, contrôler séparément l'habilitation et la disposition mise en œuvre.

### 38.1. Disposition et objet normatif

Lorsqu'une note renvoie à une disposition pour une définition ou une règle déterminée, vérifier à la fois le localisateur et le contenu. Ce contrôle ciblé du localisateur ne constitue pas un avis sur le bien-fondé de l’argumentation, qui relève du niveau 3 sur demande. L'existence de l'article cité ne suffit pas. Si la définition se trouve dans une autre disposition, conserver la citation originale et signaler `WRONG_PROVISION_LOCATOR` avec la disposition officiellement vérifiée.

## 39. CJUE

Router vers `references/cjue.md`. Règle : `numéro d'affaire ≠ document`. Ne jamais fusionner arrêt, ordonnance, conclusions ou avis.

### 39.1. Intitulé, numéro et affaires jointes

Vérifier séparément l'intitulé usuel, chaque numéro d'affaire, la date et le type de document. Une graphie fautive du nom d'une partie n'annule pas une identification certaine par le numéro et la date : conserver la source comme identifiée et produire `VERIFIED_WITH_ANOMALY` pour l'occurrence.

Pour des affaires jointes, contrôler chaque numéro dans son intégralité. Un segment tronqué, par exemple `C-469/1` à la place de `C-469/10`, est une anomalie d'identifiant même si la première affaire et l'intitulé permettent de retrouver l'arrêt.

### 39.2. Statut procédural

Le statut `pending` ou `closed` se rapporte à une procédure et à une instance précises. Vérifier séparément l'affaire initiale et tout pourvoi : une affaire du Tribunal clôturée ne doit pas être dite pendante au seul motif que son pourvoi l'est. Conserver les deux numéros et signaler `PROCEDURAL_STATUS_MISMATCH` lorsque la référence attribue au dossier initial le statut de l'instance de recours.

## 40. CEDH

Router vers `references/cedh.md`. Distinguer requête, décision, arrêt, version linguistique et traduction.

## 41. Conseil d'État de Belgique

Router vers `references/conseil-etat-belgique.md`.

### 41.1. Numéro exact d'arrêt connu

Lorsqu'un numéro exact d'arrêt est connu, la voie primaire doit être la recherche officielle du Conseil d'État, de préférence via la **Recherche avancée** et les champs `Numéro début` / `fin`.

Procédure :

1. rechercher le numéro exact dans la collection officielle ;
2. ne jamais transformer le numéro en URL supposée ;
3. ouvrir le document officiel lorsqu'il est accessible ;
4. si le lecteur échoue, télécharger le lien effectivement observé avec un client standard puis lire le PDF localement ; distinguer cet échec de lecture d’un échec du formulaire ;
5. vérifier le contenu réellement reçu, numéro, date, nature du document, parties, langue et éventuelles rectifications ;
6. vérifier le passage cité lorsque le texte est accessible ;
7. ne relever un ECLI que s'il est effectivement fourni par une source suffisamment forte ;
8. si le formulaire officiel ne peut pas être piloté ou échoue techniquement, enregistrer `TECHNICAL_FAILURE`, jamais `NO_RESULT` ;
9. poursuivre ensuite par les voies de corroboration prévues sans sur-vérifier.

La collection officielle annonce tous les arrêts depuis septembre 1994, sous réserve du régime de publication particulier du contentieux des étrangers. Une impossibilité récurrente d'interroger cette collection pour un arrêt postérieur à septembre 1994 constitue une limitation technique du skill, pas une preuve d'absence documentaire.

### 41.2. juriDict

juriDict est un outil de découverte et d'accès au contenu juridique, pas un substitut automatique au document intégral. Son absence de résultat ne prouve pas l'absence de la décision. Les arbres FR et NL sont indépendants.

### 41.3. Jurisprudence historique

Pour les décisions anciennes hors collection moderne, router vers `references/recueils-numerises-kul.md`.

> **Le numéro permet de chercher ; le document officiel permet de vérifier ; juriDict permet de découvrir.**

## 42. Cour constitutionnelle

Router vers `references/cour-constitutionnelle.md`. Distinguer rôle, numéro d'arrêt et ECLI.

## 43. JUPORTAL

Router vers `references/juportal.md`. Hiérarchie : document officiel > métadonnées officielles > résultat officiel > source secondaire fiable > snippet. L'absence dans JUPORTAL ne prouve pas nécessairement l'inexistence.

## 44. Travaux parlementaires

Toujours distinguer dossier, pièce, rapport, texte adopté, débat et norme publiée.

## 45. Bruxelles

Identifier l'institution avant le numéro : PRBC, COCOM, COCOF, VGC.

## 46. Doctrine

Router vers `references/doctrine.md`. Trois niveaux : D1 identité, D2 localisation, D3 citation. Pour les universitaires belges, rechercher rapidement les dépôts institutionnels.

## 47. AAM / postprint

Un AAM peut vérifier les mots de l'auteur. Il ne vérifie pas automatiquement la pagination de la version éditeur.

## 48. Accès

Ne jamais contourner paywall, authentification, DRM ou restrictions techniques.

## 49. Corrections

Proposer une correction uniquement lorsqu'elle est établie. Ne jamais transformer `non vérifié` en `corrigé` par approximation.

## 50. Gravité

`CRITICAL`, `MAJOR`, `MINOR`, `INFORMATION`.

Critiques notamment : identifiant inventé, source fictive, mauvais document présenté comme vérifié, arrêt et conclusions fusionnés, proposition et acte adopté fusionnés, citation substantiellement inexacte, adaptation trompeuse.

## 51. Release blockers

Une V1 publique est interdite tant qu'un benchmark révèle :

### A — invention

Identifiant fabriqué ou référence complétée sans preuve.

### B — sur-vérification

Snippet → `VERIFIED`, source secondaire → ECLI vérifié, panne → inexistence.

### C — fusion

Arrêt + conclusions, proposition + directive, rapport + projet, texte adopté + loi.

### D — intégrité citationnelle

Ellipse trompeuse validée comme simple adaptation.

### E — récupération Conseil d'État par numéro exact

Avant passage du `PUBLIC_RELEASE_GATE` au vert :

```text
COUNCIL_OF_STATE_EXACT_NUMBER_RETRIEVAL = GREEN
```

Le test T53 doit confirmer que la recherche officielle par numéro exact est tentée prioritairement, sans reconstruction d'URL/ECLI, et qu'un échec du formulaire produit `TECHNICAL_FAILURE` plutôt qu'une fausse inexistence.

## 52. Rapport

Produire par défaut : résumé conversationnel, Markdown canonique et PDF professionnel lorsque les outils de génération et de contrôle visuel sont disponibles ; DOCX si demandé. Si un format ne peut pas être produit, livrer les résultats disponibles et indiquer cette limite, sans annoncer un fichier inexistant. Pour un rapport en français, utiliser le générateur de mise en page `scripts/render_report.py` selon `templates/report-rendering.md`. Il produit Markdown et PDF à partir des mêmes fiches déjà vérifiées ; il ne réalise pas les recherches. Pour les autres langues, appliquer le modèle éditorial dans la langue du rapport avec les outils disponibles.

### Présentation destinée au juriste

Suivre `templates/report-template.md`. Commencer par les conclusions utiles et les corrections, puis donner les preuves et les limites. Afficher les statuts en langage courant dans la langue du rapport ; conserver les codes techniques dans les données et traces. Expliquer ce qui a été contrôlé sans supposer que le lecteur connaît un schéma de données. Aucun pourcentage de fiabilité déduit du seul nombre de références retrouvées. Conserver une première réponse gelée quand le rapport sert à une évaluation indépendante ; une nouvelle présentation ne remplace pas cette réponse.

## 53. Rapport PDF

Doit contenir : couverture, résumé exécutif, déroulement de l'audit, statistiques, anomalies prioritaires, fiches détaillées, contrôle des citations, intégrité des adaptations, niveau de preuve, sources consultées, limitations et avertissement.

## 54. Déroulement de l'audit dans le rapport

Pour les audits significatifs, inclure une section montrant le travail réellement accompli : occurrences, sources uniques, sources vérifiées/partiellement vérifiées, citations textuelles, anomalies et références non vérifiables.

## 55. Rapport d'une citation adaptée

Présenter séparément : fidélité textuelle, adaptations détectées, adaptations signalées ou non, intégrité de l'adaptation et conséquence éventuelle sur le sens.

## 56. Avertissement

Inclure notamment : génération assistée par IA ; dépendance aux sources accessibles ; évolution possible des interfaces ; absence de vérification ≠ erreur ; nécessité d'une vérification humaine ; limitation de responsabilité dans les limites permises par le droit applicable.

## 57. Maintenance

Chaque module indique sa date de révision des instructions. Les vérifications fonctionnelles sont datées séparément et rattachées aux parcours réellement exécutés : une révision documentaire ne prouve pas le fonctionnement d’une interface. Tester URLs, recherche, interfaces, replis et exemples selon les changements observés.

## 58. Versionnement

Semantic Versioning `MAJOR.MINOR.PATCH`. Avant V1 : `0.x`.

## 59. Benchmarks

Avant V1 : benchmark v0.1, benchmark v0.2 adversarial, benchmark v0.3 intégration, test UX de progression, test T53 et audits d'intégration complets.

Un résultat de test doit renvoyer à ses entrées, à la sortie effectivement produite, aux observations/outils et à la comparaison avec l'oracle. Distinguer revue de spécification, scénario simulé et parcours réel. Un oracle seul n'est pas une exécution ; une validation de structure ou de mise en page n'est pas une validation comportementale ou documentaire. Sans trace suffisante, noter `NOT_DEMONSTRATED`, jamais `PASS`. Les résultats historiques non traçables ne permettent pas le passage au vert.

Conditions minimales : 0 invention, 0 sur-vérification, 0 fusion documentaire, 0 adaptation trompeuse acceptée et progression adaptée à la taille de l'audit.

## 60. README

Documentation en FR/NL/DE/EN : `README.md`, `README.fr.md`, `README.nl.md`, `README.de.md`, `README.en.md`.

## 61. Licence

Documentation : `CC BY-NC-SA 4.0`. Ne pas qualifier abusivement le projet d'« open source » au sens OSI compte tenu de la restriction NC.

## 62. Principe final

Le skill doit pouvoir dire avec précision : ce qui est certain, corroboré, seulement probable, non vérifié, déjà traité et encore à vérifier.

Il doit préférer :

> **« je ne peux pas vérifier davantage avec les sources accessibles »**

à une certitude non démontrée.

Et toujours :

> **Vérifier la source, jamais la vraisemblance de la référence.**
