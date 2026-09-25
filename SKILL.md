---
name: audit-citations-juridiques-be-eu
description: >
  Vérifie dans les sources officielles les références et citations d'un document
  juridique (droit belge, UE, CEDH) : existence et exactitude des arrêts, lois,
  actes et ouvrages cités (numéro, date, ECLI, CELEX, NUMAC, page), fidélité des
  citations, rapport des erreurs et des points non vérifiables. À utiliser pour
  vérifier ou auditer des notes, références, citations ou ECLI (« vérifie mes
  notes », « cet arrêt existe-t-il ? », « controleer de voetnoten », « check
  these citations »).
---

# Audit des citations juridiques — Belgique & Europe

Version du skill : `0.6.0-beta.1` (à reporter dans le champ `skill_version` du rapport).

## 1. Objet

Auditer les références juridiques d'un document complet : mémoires, conclusions, avis, notes, consultations, articles, projets d'ouvrages, rapports, travaux universitaires, documents générés ou assistés par IA.

Défauts recherchés : sources fictives ; références plausibles mais inexistantes ; identifiant appartenant à un autre document ; erreur de numéro, date, rôle ou ECLI ; confusion entre documents d'une même affaire ; mauvaise version temporelle, langue ou édition ; citations inexactes ou tronquées de manière trompeuse ; doctrine inventée ou mal attribuée.

Périmètre : législation belge (Moniteur, Justel, RefLex), Cour constitutionnelle, Conseil d'État, Cassation et juridictions judiciaires (JUPORTAL), travaux parlementaires fédéraux et fédérés, jurisprudence historique, doctrine ; droit de l'Union (traités, Charte, actes, consolidations, rectificatifs, travaux préparatoires, CJUE, Tribunal, conclusions d'avocats généraux) ; CEDH (arrêts, décisions, avis, requêtes, HUDOC).

## 2. Règles cardinales

> **Vérifier la source, jamais la vraisemblance de la référence.**

1. **Ne jamais inventer**, compléter ou reconstruire de mémoire un ECLI, CELEX, ELI, NUMAC, DOI, ISBN, numéro de rôle, d'arrêt ou parlementaire, ni une URL profonde.
   *Sonde autorisée* : ouvrir l'adresse de consultation d'une base officielle à partir d'un identifiant **tel qu'il figure dans la référence auditée ou tel qu'une source officielle consultée l'a affiché** (ECLI, CELEX, ELI, numéro d'affaire, identifiant de document d'un résultat de recherche) ou de sa transcription mécanique et documentée (par ex. « directive 2019/1024 » → CELEX `32019L1024`) est une tentative de recherche, pas une reconstruction. La consigner comme telle ; ne rien en conclure avant d'avoir contrôlé que le document reçu correspond à tous les champs cités ; un échec ou une page vide reste `TECHNICAL_FAILURE` ou `NO_RESULT`, jamais une inexistence. Un identifiant absent de la référence et non dérivable mécaniquement (NUMAC, ECLI d'un arrêt, numéro de document) se trouve par une recherche, jamais de mémoire. Ne jamais sonder un identifiant supposé (ECLI voisin, numéro deviné) avant de l'avoir vu affiché, même sans intention d'en tirer une conclusion. Un identifiant sondé n'apparaît dans le rapport que s'il est affiché par la source officielle.
1 bis. **Chercher à partir du document, jamais de sa mémoire** : toute recherche part d'un élément écrit dans le document ou affiché par une source officielle consultée. Ne jamais interroger une base avec un numéro d'arrêt, un ECLI ou une référence connus par ailleurs (connaissance générale, affaire voisine, souvenir du dossier), même « pour vérifier une intuition » et même sans en tirer de conclusion. Si une source non citée paraît utile, la chercher par les mots du document (parties, date, objet), ou le signaler au juriste.
2. **Ne jamais sur-vérifier** : le statut ne peut jamais dépasser le niveau de preuve réellement obtenu. Identité fortement corroborée + ECLI non vérifié + texte officiel inaccessible → `🟠 PARTIALLY_VERIFIED`, pas `VERIFIED`.
3. **Panne ≠ inexistence** : toujours distinguer `TECHNICAL_FAILURE` de `NO_RESULT`. Un timeout, une erreur ou une interface inaccessible ne prouve rien.
4. **Un snippet oriente, il ne vérifie pas** : il ne suffit jamais pour une citation textuelle, une page, un ECLI litigieux ou un statut `VERIFIED`.
5. **Découvrir ≠ prouver** : conserver séparément `discovery_source` et `verification_source`. La base qui permet de trouver n'est pas nécessairement celle qui permet de vérifier.
6. **Ne jamais fusionner** des documents distincts : arrêt et conclusions, proposition et acte adopté, rapport et projet, texte adopté et loi publiée.
7. **Ne jamais contourner** paywall, authentification, DRM, CAPTCHA ou restriction technique. Utiliser une autre voie publique que le même site officiel offre sans contrôle (par exemple son moteur de recherche public ou sa fonction d'export) n'est pas un contournement ; imiter un navigateur, répéter les tentatives ou modifier l'origine de la connexion pour franchir un contrôle en est un.

## 3. Entrées

PDF, DOCX, Markdown, texte brut, HTML ou texte collé. Préserver pagination, notes, paragraphes, tableaux, guillemets et langues.

Pour un renvoi interne, la cible peut se trouver dans un autre extrait déjà fourni : vérifier titres, pages et sections du corpus disponible avant de conclure qu'elle est inaccessible, sans présumer que ce corpus contient tout l'ouvrage.

Une source fournie par l'utilisateur peut vérifier texte, page et version ; ne pas la confondre avec une source officielle sans base.

## 4. Déroulement

```text
contrôle des accès (§10) → inventaire → renvois internes → dédoublonnage → classification → routage
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

Des métadonnées officielles (fiche ou notice de la juridiction ou de l'éditeur officiel) suffisent pour déclarer `VERIFIED` les champs d'identité qu'elles affichent (juridiction, date, numéro, parties). Elles ne suffisent pas pour un localisateur de passage ni pour une citation : ces éléments restent non vérifiés tant que le texte n'a pas été lu, et la fiche le dit.

### Statuts des références

- 🟢 `VERIFIED`
- 🟡 `VERIFIED_WITH_ANOMALY`
- 🟠 `PARTIALLY_VERIFIED`
- ⚪ `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES` — **l'absence de vérification ne signifie pas que la référence est erronée.**
- 🔴 `NOT_FOUND_OR_CONTRADICTORY`

### Gravité

`CRITICAL`, `MAJOR`, `MINOR`, `INFORMATION`. Critiques notamment : identifiant inventé, source fictive, mauvais document présenté comme vérifié, documents distincts fusionnés, citation substantiellement inexacte, adaptation trompeuse.

Identifiant valide mais désignant un autre document (`VALID_IDENTIFIER_WRONG_DOCUMENT`) : `MAJOR` lorsque la source visée reste identifiée avec certitude par les autres champs cités (numéro d'affaire, date, parties, intitulé) ; `CRITICAL` lorsque l'identifiant fautif est le seul moyen d'identification, lorsque le texte s'appuie sur le contenu de l'autre document (par exemple des conclusions présentées comme la position de la Cour), ou lorsque l'identifiant n'existe pas. Un segment tronqué ou une coquille qui ne mène à aucun autre document reste `MINOR`.

Mauvaise disposition (`WRONG_PROVISION_LOCATOR`, par exemple une définition attribuée au mauvais point d'un article) : `MAJOR`, car le lecteur est renvoyé à une règle au contenu différent ; `MINOR` seulement si la disposition citée et la bonne ont le même contenu utile (renumérotation, simple faute de frappe sans autre disposition désignée).

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

**Conseil d'État — numéro exact connu.** Voie primaire : la **Recherche avancée** officielle (ou l'adresse de résultat que ce formulaire a produite, réutilisée avec un autre numéro **cité dans le document**), champs `Numéro début` = `Numéro fin`. Ne jamais transformer le numéro en URL ou en ECLI supposés. Ouvrir le document officiel ; si le lecteur échoue, télécharger le lien effectivement observé avec un client standard et lire le PDF localement. Vérifier numéro, date, nature, parties, langue, rectifications, puis le passage cité. Ne relever un ECLI que s'il est fourni par une source suffisamment forte. Un formulaire inutilisable donne `TECHNICAL_FAILURE`, jamais `NO_RESULT`. La collection annonce tous les arrêts depuis septembre 1994 (régime particulier pour les étrangers) : une impossibilité récurrente d'y accéder est une limite technique, pas une preuve d'absence. juriDict découvre, il ne remplace pas le document intégral ; ses arbres FR et NL sont indépendants.

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

## 10. Communication avec l'utilisateur

L'utilisateur est un juriste, pas un informaticien. Dans tous les messages qui lui sont destinés : langage courant, dans sa langue ; vouvoiement (« vous », « u », « Sie ») sauf si l'utilisateur tutoie lui-même ; aucun code interne (`VERIFIED`, `TECHNICAL_FAILURE`, noms de champs) ; aucun jargon technique (proxy, HTTP, curl, JSON) sans explication en une phrase ; les codes restent dans les données et les traces. Guide de l'utilisateur : [MODE-EMPLOI.md](MODE-EMPLOI.md).

### Avant de commencer : contrôle des accès

Avant l'inventaire, vérifier quels outils sont réellement disponibles et, si possible, les essayer une fois (une recherche simple, l'ouverture d'une page officielle, par exemple la page d'accueil d'EUR-Lex) :

| Accès | Rôle | Sans lui |
|---|---|---|
| Recherche web | trouver les sources | audit impossible : le dire et s'arrêter |
| Lecture de pages web | ouvrir notices et textes officiels | vérifications limitées aux extraits de recherche, donc presque rien de vérifié |
| Navigateur réel (dans Cowork : navigateur intégré de l'application de bureau) | sites qui renvoient une page vide aux outils simples ou refusent les connexions venant de serveurs (EUR-Lex, CURIA, HUDOC, Conseil d'État) | vérifications partielles pour ces sources ; indiquer à l'utilisateur de choisir le navigateur intégré dans les réglages de Cowork et de laisser l'application de bureau ouverte |
| Lecture du document joint | lire PDF ou DOCX | demander un autre format ou un copier-coller |
| Exécution de code | générer le PDF, lire un PDF officiel téléchargé | rapport en Markdown seulement ; certains textes non lus |

Si un accès indispensable manque, ne pas commencer l'audit : expliquer en deux ou trois phrases ce qui manque, ce que cela change pour le résultat et où l'activer (renvoyer à la section « Les accès à donner » du mode d'emploi). Si seul un accès utile manque, le dire et demander si l'utilisateur veut poursuivre avec des vérifications plus limitées. Ne jamais demander de mot de passe, ni de désactiver une protection de sécurité en général.

### Message de départ

Après l'inventaire, un seul message court, avant les recherches :

- ce qui a été trouvé : nombre de références et de sources distinctes, citations textuelles à contrôler ;
- les étapes : vérification de chaque source dans les bases officielles, puis contrôle des citations, puis rapport ;
- **une fourchette de durée**, présentée comme indicative : compter environ 1 à 3 minutes par source distincte, davantage pour la doctrine, les décisions anciennes ou les sites lents (par exemple : « une vingtaine de sources : entre 20 minutes et une heure ») ; ne jamais donner une durée précise ;
- ce que l'utilisateur doit faire : rien, sauf laisser la conversation ouverte (dans Cowork, laisser aussi l'application de bureau ouverte et connectée, car le navigateur intégré en dépend) ; il peut faire autre chose et revenir ; des points d'étape suivront.

Pour un document très long (plus d'une cinquantaine de sources), proposer de commencer par une partie (un chapitre, les notes d'une section) ou de traiter le document par lots, chaque lot faisant l'objet d'un rapport daté.

### Pendant l'audit

Donner des compteurs réels (« 31 sources sur 57 vérifiées », « 14 citations sur 22 contrôlées ») plutôt qu'un pourcentage. Ne publier un point d'étape qu'à un changement d'état réel : inventaire terminé, nouvelle famille de sources, lot significatif vérifié, difficulté d'accès importante, erreur importante confirmée, début du contrôle des citations, rédaction du rapport. Signaler sobrement une difficulté d'accès (« le site de la Cour européenne des droits de l'homme bloque les consultations automatisées ; je passe par une autre voie »), sans la transformer en inexistence juridique. Pour un audit de trois sources ou moins, se passer du message de départ et des points d'étape : répondre directement. Au-delà, le message de départ (avec sa fourchette de durée) est donné une seule fois ; ne pas la répéter ensuite.

### Fin de l'audit

Commencer par ce que le juriste doit faire : corrections établies, puis points à vérifier lui-même, puis ce qui est confirmé. Rappeler en une phrase qu'une référence « non vérifiable » n'est pas pour autant erronée. Indiquer où se trouvent le rapport et ses fichiers.

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
