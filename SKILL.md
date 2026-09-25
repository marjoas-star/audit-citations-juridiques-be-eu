---
name: audit-citations-juridiques-be-eu
description: >
  Audite les références, citations et sources d'un document juridique en droit
  belge, droit de l'Union européenne et droit de la CEDH : vérifie dans les
  sources officielles que chaque arrêt, loi, acte, travail parlementaire ou
  ouvrage cité existe et correspond bien à la référence (numéro, date, rôle,
  ECLI, CELEX, NUMAC, page), contrôle les citations textuelles, ellipses et
  traductions, signale les anomalies et ce qui n'a pas pu être vérifié, et peut
  produire un rapport Markdown/PDF. À utiliser dès que l'utilisateur demande de
  vérifier, contrôler, relire ou auditer des références, notes de bas de page,
  citations, ECLI ou sources d'un mémoire, de conclusions, d'un avis, d'un
  article ou d'un texte généré par IA, ou demande si un arrêt ou une référence
  existe (« vérifie mes notes », « cet arrêt existe-t-il ? », « contrôle les
  ECLI », « controleer de voetnoten », « check these citations »). Fonctionne
  en français, néerlandais, allemand et anglais.
---

# Audit des citations juridiques — Belgique & Europe

## 1. Objet

Auditer les références juridiques d'un document complet : mémoires, conclusions, avis, notes, consultations, articles, projets d'ouvrages, rapports, travaux universitaires, documents générés ou assistés par IA.

Défauts recherchés : sources fictives ; références plausibles mais inexistantes ; identifiant appartenant à un autre document ; erreur de numéro, date, rôle ou ECLI ; confusion entre documents d'une même affaire ; mauvaise version temporelle, langue ou édition ; citations inexactes ou tronquées de manière trompeuse ; doctrine inventée ou mal attribuée.

Périmètre : législation belge (Moniteur, Justel, RefLex), Cour constitutionnelle, Conseil d'État, Cassation et juridictions judiciaires (JUPORTAL), travaux parlementaires fédéraux et fédérés, jurisprudence historique, doctrine ; droit de l'Union (traités, Charte, actes, consolidations, rectificatifs, travaux préparatoires, CJUE, Tribunal, conclusions d'avocats généraux) ; CEDH (arrêts, décisions, avis, requêtes, HUDOC).

## 2. Règles cardinales

> **Vérifier la source, jamais la vraisemblance de la référence.**

1. **Ne jamais inventer**, compléter ou reconstruire de mémoire un ECLI, CELEX, ELI, NUMAC, DOI, ISBN, numéro de rôle, d'arrêt ou parlementaire, ni une URL profonde.
2. **Ne jamais sur-vérifier** : le statut ne peut jamais dépasser le niveau de preuve réellement obtenu. Identité fortement corroborée + ECLI non vérifié + texte officiel inaccessible → `🟠 PARTIALLY_VERIFIED`, pas `VERIFIED`.
3. **Panne ≠ inexistence** : toujours distinguer `TECHNICAL_FAILURE` de `NO_RESULT`. Un timeout, une erreur ou une interface inaccessible ne prouve rien.
4. **Un snippet oriente, il ne vérifie pas** : il ne suffit jamais pour une citation textuelle, une page, un ECLI litigieux ou un statut `VERIFIED`.
5. **Découvrir ≠ prouver** : conserver séparément `discovery_source` et `verification_source`. La base qui permet de trouver n'est pas nécessairement celle qui permet de vérifier.
6. **Ne jamais fusionner** des documents distincts : arrêt et conclusions, proposition et acte adopté, rapport et projet, texte adopté et loi publiée.
7. **Ne jamais contourner** paywall, authentification, DRM, CAPTCHA ou restriction technique.

## 3. Entrées

PDF, DOCX, Markdown, texte brut, HTML ou texte collé. Préserver pagination, notes, paragraphes, tableaux, guillemets et langues.

Pour un renvoi interne, la cible peut se trouver dans un autre extrait déjà fourni : vérifier titres, pages et sections du corpus disponible avant de conclure qu'elle est inaccessible, sans présumer que ce corpus contient tout l'ouvrage.

Une source fournie par l'utilisateur peut vérifier texte, page et version ; ne pas la confondre avec une source officielle sans base.

## 4. Déroulement

```text
inventaire → renvois internes → dédoublonnage → classification → routage
→ recherche externe → niveau de preuve → métadonnées → contrôle textuel
→ intégrité des adaptations → rapport
```

**Inventaire.** Avant toute recherche : relever toutes les références, citations, renvois abrégés et la bibliographie ; dédupliquer les sources. Ne rien corriger à ce stade.

**Renvois internes.** Résoudre `ibid.`, `idem`, `op. cit.`, `précité`, `supra`, `infra` dans le document. Si plusieurs sources restent possibles : `SOURCE_ATTRIBUTION_UNCERTAIN`. Ne pas utiliser le web pour deviner la source.

**Classification.** `BE_LEGISLATION`, `BE_CONSTITUTIONAL_COURT`, `BE_COUNCIL_OF_STATE`, `BE_CASSATION`, `BE_JUDICIARY`, `BE_PARLIAMENT_FEDERAL`, `BE_PARLIAMENT_FEDERATED`, `BE_HISTORICAL_CASELAW`, `EU_LEGISLATION`, `EU_CASELAW`, `EU_PREPARATORY_WORK`, `ECHR_CASELAW`, `DOCTRINE_BOOK`, `DOCTRINE_ARTICLE`, `DOCTRINE_CHAPTER`, `DOCTRINE_CASE_NOTE`, `DOCTRINE_ONLINE`, `DOCTRINE_THESIS`, `OTHER`. Scinder une référence composite en plusieurs sources.

**Routage.** Appliquer [routing.md](references/routing.md), puis le module spécialisé (§8).

**Données.** Utiliser [citation-record.md](schemas/citation-record.md) : `SOURCE_RECORD`, `OCCURRENCE_RECORD`, `QUOTATION_RECORD`, `SEARCH_ATTEMPT`, `AUDIT_RECORD`.

**Datation.** Appliquer [datation-et-rapport.md](references/datation-et-rapport.md) à tout audit et toute révision : date réelle d'établissement, consultations, révision et son étendue enregistrées séparément. Réexporter ne réactualise pas le contrôle. Ne jamais inventer une heure ancienne ni imposer une date juridique fixe. Avant une correction normative, établir la version pertinente.

### Trois niveaux d'audit — ne jamais les confondre

1. **Identité documentaire** (automatique) : la source existe-t-elle et la référence désigne-t-elle le bon document ?
2. **Fidélité citationnelle** (automatique si le texte est accessible) : fidélité textuelle puis intégrité des adaptations.
3. **Soutien substantif** (seulement sur demande) : la source soutient-elle la proposition juridique formulée ?

## 5. Preuve et statuts

### Niveau de preuve

`OFFICIAL_AUTHENTIC_PUBLICATION`, `OFFICIAL_FULL_DOCUMENT`, `OFFICIAL_METADATA`, `OFFICIAL_SEARCH_RESULT`, `INSTITUTIONAL_FULL_DOCUMENT`, `PUBLISHER_FULL_DOCUMENT`, `INSTITUTIONAL_METADATA`, `RELIABLE_SECONDARY_CORROBORATION`, `SEARCH_SNIPPET_ONLY`, `UNVERIFIED`.

Pour chaque champ ou citation déclaré vérifié, conserver : lien effectivement observé, date de consultation, type de document réellement ouvert, langue, passage ou localisateur contrôlé. Accéder à un document intégral ne vérifie pas automatiquement tous ses champs. Un communiqué reste un communiqué : il ne prouve pas les mots de l'arrêt.

Dans un arrêt, identifier qui s'exprime : juridiction, partie, juridiction de renvoi ou texte reproduit. Une plage de paragraphes peut changer de locuteur.

### Vérification par champ

Une source peut être identifiée alors qu'un champ reste non vérifié (rôle vérifié, date corroborée, ECLI non vérifié…). L'existence d'un identifiant ne suffit jamais : s'il désigne un autre document, `VALID_IDENTIFIER_WRONG_DOCUMENT`.

### Statuts des références

- 🟢 `VERIFIED`
- 🟡 `VERIFIED_WITH_ANOMALY`
- 🟠 `PARTIALLY_VERIFIED`
- ⚪ `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES` — **l'absence de vérification ne signifie pas que la référence est erronée.**
- 🔴 `NOT_FOUND_OR_CONTRADICTORY`

### Gravité

`CRITICAL`, `MAJOR`, `MINOR`, `INFORMATION`. Critiques notamment : identifiant inventé, source fictive, mauvais document présenté comme vérifié, documents distincts fusionnés, citation substantiellement inexacte, adaptation trompeuse.

## 6. Citations textuelles

Créer un `QUOTATION_RECORD` pour toute citation attribuée à une source. Contrôler source, version, langue, localisation, mots reproduits, suppressions, insertions et adaptations.

**Statut textuel** : ✅ `EXACT`, 🟢 `EXACT_WITH_SIGNALLED_ADAPTATIONS`, 🟡 `MINOR_DEVIATION`, 🔴 `INEXACT`, ⚪ `NOT_VERIFIABLE`, `NOT_APPLICABLE_TRANSLATION`.

**Adaptations** : `OMISSION`, `INSERTION`, `GRAMMATICAL_ADJUSTMENT`, `TYPOGRAPHICAL_ADJUSTMENT`, `EMPHASIS_ADDED`, `EMPHASIS_REMOVED`, `CORRECTION`, `TRANSLATION`, `OTHER`. Une adaptation signalée n'est pas automatiquement acceptable.

**Intégrité** : `FAITHFUL`, `MATERIAL_BUT_NOT_MISLEADING`, `MISLEADING`, `NOT_VERIFIABLE`. Une citation peut être `EXACT_WITH_SIGNALLED_ADAPTATIONS` tout en étant `MISLEADING`.

**Contrôle approfondi** lorsqu'une adaptation touche : négation, condition, exception, délai, qualité d'une personne, compétence, modalité, causalité, obligation/faculté, réserve, articulation `et/ou` ou dispositif.

- **Ellipses `[...]`** : vérifier ce qui a été supprimé, la grammaire et la portée résultantes, et la suppression éventuelle d'une réserve. Si le contexte supprimé est inaccessible, l'intégrité reste `NOT_VERIFIABLE`.
- **Crochets** : vérifier l'antécédent, l'identité et l'absence d'élargissement ou de réduction de la règle.
- **Traductions** : appliquer [language-policy.md](references/language-policy.md). Une comparaison entre langues différentes ne produit jamais `EXACT` : utiliser `NOT_APPLICABLE_TRANSLATION` et évaluer séparément la fidélité (`FAITHFUL`, `FAITHFUL_WITH_MINOR_VARIATION`, `PARTIALLY_FAITHFUL`, `MISLEADING`, `NOT_VERIFIABLE`). Si la version citée est inconnue, ne pas supposer une traduction d'auteur.

## 7. Langues

Travail natif en FR, NL, DE, EN. Distinguer `document_language`, `citation_language`, `source_language`, `report_language`. Identifier avant de traduire. Ne jamais supposer qu'une taxonomie linguistique traduit exactement une autre : `juriDict FR ≠ traduction de juriDict NL`.

## 8. Règles par famille de sources

| Famille | Module | Points critiques |
|---|---|---|
| Législation belge | [moniteur-belge-justel.md](references/moniteur-belge-justel.md), [reflex.md](references/reflex.md) | acte, publication, version temporelle, entrée en vigueur, modifications, rectificatifs |
| Conseil d'État | [conseil-etat-belgique.md](references/conseil-etat-belgique.md) | voir ci-dessous |
| Jurisprudence CE ancienne | [recueils-numerises-kul.md](references/recueils-numerises-kul.md) | une table ne vaut pas texte intégral |
| Cour constitutionnelle | [cour-constitutionnelle.md](references/cour-constitutionnelle.md) | rôle ≠ numéro d'arrêt ≠ ECLI |
| Cassation, juridictions | [juportal.md](references/juportal.md) | document officiel > métadonnées > résultat > secondaire > snippet ; absence ≠ inexistence |
| Parlement fédéral | [travaux-parlementaires-federal.md](references/travaux-parlementaires-federal.md) | dossier ≠ pièce ≠ rapport ≠ texte adopté ≠ débat ≠ norme publiée |
| Entités fédérées | [travaux-parlementaires-entites-federees.md](references/travaux-parlementaires-entites-federees.md) | Bruxelles : identifier l'institution (PRBC, COCOM, COCOF, VGC) avant le numéro |
| Droit de l'Union | [eur-lex-legislation.md](references/eur-lex-legislation.md) | acte publié ≠ consolidation ≠ préparatoire ≠ procédure |
| CJUE / Tribunal | [cjue.md](references/cjue.md) | numéro d'affaire ≠ document |
| CEDH | [cedh.md](references/cedh.md) | requête, décision, arrêt, version linguistique, traduction |
| Doctrine | [doctrine.md](references/doctrine.md) | D1 identité, D2 localisation, D3 citation |

**Conseil d'État — numéro exact connu.** Voie primaire : la **Recherche avancée** officielle, champs `Numéro début` = `Numéro fin`. Ne jamais transformer le numéro en URL ou en ECLI supposés. Ouvrir le document officiel ; si le lecteur échoue, télécharger le lien effectivement observé avec un client standard et lire le PDF localement. Vérifier numéro, date, nature, parties, langue, rectifications, puis le passage cité. Ne relever un ECLI que s'il est fourni par une source suffisamment forte. Un formulaire inutilisable donne `TECHNICAL_FAILURE`, jamais `NO_RESULT`. La collection annonce tous les arrêts depuis septembre 1994 (régime particulier pour les étrangers) : une impossibilité récurrente d'y accéder est une limite technique, pas une preuve d'absence. juriDict découvre, il ne remplace pas le document intégral ; ses arbres FR et NL sont indépendants.

> **Le numéro permet de chercher ; le document officiel permet de vérifier ; juriDict permet de découvrir.**

**Droit de l'Union.** Le module précise les références au JO depuis octobre 2023, les titres abrégés, les dates institutionnelles et les versions de lignes directrices. Distinguer une erreur documentaire d'une harmonisation éditoriale. Pour un acte délégué ou d'exécution, contrôler séparément l'habilitation et la disposition mise en œuvre. Lorsqu'une note renvoie à une disposition pour une définition ou une règle, vérifier le localisateur **et** le contenu ; si la règle se trouve ailleurs, conserver l'original et signaler `WRONG_PROVISION_LOCATOR` avec la disposition vérifiée. Ce contrôle n'est pas un avis sur le bien-fondé de l'argumentation.

**CJUE.** Ne jamais fusionner arrêt, ordonnance, conclusions ou avis. Vérifier séparément intitulé, chaque numéro d'affaire, date et type de document. Une graphie fautive d'une partie avec numéro et date certains → source identifiée, `VERIFIED_WITH_ANOMALY`. Pour des affaires jointes, contrôler chaque numéro en entier (`C-469/1` au lieu de `C-469/10` est une anomalie). Le statut `pending`/`closed` vaut pour une instance précise : une affaire du Tribunal clôturée n'est pas pendante parce que son pourvoi l'est → `PROCEDURAL_STATUS_MISMATCH`.

**Doctrine.** Pour les universitaires belges, consulter tôt les dépôts institutionnels. Un AAM/postprint vérifie les mots de l'auteur, pas automatiquement la pagination de la version éditeur.

## 9. Corrections

- Toujours conserver `original` (copié littéralement) et `verified` ; la normalisation va dans le corrigé. Respecter la convention et la langue du document dans la formulation prête à reprendre.
- Ne proposer une correction que lorsqu'elle est établie ; ne jamais transformer « non vérifié » en « corrigé » par approximation.
- Séparer erreurs établies et suggestions : une paraphrase susceptible d'être complétée n'est pas, à elle seule, une citation fautive.
- Après correction, vérifier les marqueurs chronologiques (« déjà », « récemment », « depuis ») affectés par la nouvelle source.
- Une erreur répétée garde un identifiant de constat unique ; ses occurrences restent localisées.

## 10. Communication pendant l'audit

Pour un audit nécessitant plusieurs recherches, annoncer dès le début les étapes : inventaire, vérification de chaque source unique, contrôle séparé des citations accessibles, recherches pouvant exiger plusieurs voies. Pas de durée prévisionnelle.

Donner des compteurs réels (`31/57 sources traitées`, `14/22 citations contrôlées`) plutôt qu'un pourcentage. Ne publier une mise à jour qu'à un changement d'état réel : inventaire terminé, nouvelle famille de sources, lot significatif vérifié, difficulté technique importante, anomalie majeure confirmée, début du contrôle des citations, consolidation finale. Signaler sobrement une difficulté, sans la transformer en inexistence juridique. Pour quelques références simples, ne pas multiplier les messages.

## 11. Rapport

Par défaut : résumé conversationnel, Markdown canonique et PDF lorsque les outils de génération et de contrôle visuel sont disponibles ; DOCX si demandé. Si un format ne peut être produit, livrer ce qui est disponible et le dire, sans annoncer un fichier inexistant.

- **Français** : utiliser `scripts/render_report.py` selon [report-rendering.md](templates/report-rendering.md). Il met en page Markdown et PDF à partir de fiches déjà vérifiées ; il ne fait aucune recherche.
- **Autres langues** : appliquer le modèle éditorial dans la langue du rapport avec les outils disponibles.

Présentation selon [report-template.md](templates/report-template.md) :

- commencer par les conclusions utiles et les corrections, puis les preuves et les limites ;
- statuts en langage courant dans la langue du rapport, codes techniques réservés aux données et traces ;
- expliquer ce qui a été contrôlé sans supposer que le lecteur connaît le schéma ;
- conserver datation, synthèse, périmètre, corrections, preuves, limites et contrôle des citations ; diagnostic, extrait probant et correction restent réunis ;
- adapter la longueur (tableau des références, fiches par source ou problème, occurrences en annexe) ; aucune page distincte imposée par rubrique ;
- pour un audit significatif, montrer le travail accompli : occurrences, sources uniques, vérifiées/partielles/non vérifiables, citations contrôlées, anomalies ;
- pour une citation adaptée, présenter séparément fidélité textuelle, adaptations détectées, adaptations signalées ou non, intégrité et effet sur le sens ;
- aucun pourcentage de fiabilité déduit du nombre de références retrouvées ;
- conserver une première réponse gelée lorsque le rapport sert à une évaluation indépendante.

**Avertissement** à inclure : génération assistée par IA ; dépendance aux sources accessibles ; évolution possible des interfaces ; absence de vérification ≠ erreur ; vérification humaine nécessaire. Ne pas ajouter de clause générale de limitation de responsabilité.

## 12. Principe final

Dire avec précision ce qui est certain, corroboré, seulement probable, non vérifié, déjà traité et encore à vérifier. Préférer

> **« je ne peux pas vérifier davantage avec les sources accessibles »**

à une certitude non démontrée.
