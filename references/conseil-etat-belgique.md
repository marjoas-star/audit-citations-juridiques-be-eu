# Conseil d'État de Belgique — jurisprudence

**Dernière révision des instructions : 24 septembre 2026**

## 1. Objet

Ce module décrit la vérification des arrêts et ordonnances de non-admission de la section du contentieux administratif du Conseil d'État de Belgique, ainsi que l'usage de juriDict et des recueils historiques.

## 2. Sources officielles

Source primaire moderne : site officiel du Conseil d'État de Belgique, rubrique **Chercher > Arrêts**.

Le site annonce que la collection numérisée comprend :

- tous les arrêts à partir de septembre 1994 ;
- toutes les ordonnances de non-admission ;
- avec un régime particulier pour le contentieux des étrangers, où seules les décisions présentant un intérêt pour la jurisprudence ou la recherche juridique sont publiées ;
- publication dans la langue du prononcé.

La page officielle **Recherche avancée** offre notamment les champs :

- Date ;
- Numéro début ;
- Numéro fin ;
- Numéro de rôle ;
- Parties ;
- Décision ;
- type de document ;
- langue.

## 3. Règle fondamentale

> **Le numéro permet de chercher ; le document officiel permet de vérifier ; juriDict permet de découvrir.**

Une occurrence dans un moteur de recherche, un snippet, une référence doctrinale ou un point de droit juriDict ne remplace pas le document officiel intégral lorsqu'il est accessible.

## 4. Récupération par numéro exact — EXACT_DECISION_NUMBER_LOOKUP

Lorsqu'un numéro exact d'arrêt est connu :

1. utiliser en priorité la recherche officielle du Conseil d'État ;
2. utiliser `Numéro début` et `Numéro fin` avec le même numéro lorsque l'interface le permet ; consigner les langues et les autres filtres effectivement sélectionnés (un filtre linguistique restreint la portée d’un résultat nul) ;
3. ne jamais construire une URL profonde à partir du numéro ;
4. ne jamais construire un ECLI à partir de la date, du numéro ou d'un modèle supposé ;
5. ouvrir le document officiel lorsque le résultat le permet ;
6. vérifier séparément :
   - nature du document ;
   - numéro ;
   - date ;
   - parties ;
   - langue ;
   - numéro de rôle si pertinent ;
   - passage cité si le texte intégral est accessible ;
7. ne relever un ECLI que s'il est effectivement présent dans une source suffisamment forte ;
8. conserver le niveau de preuve par champ.

### 4.1. Échec du formulaire

Si le formulaire officiel ne peut pas être piloté, renvoie une erreur, un timeout ou une réponse techniquement inexploitable :

```text
TECHNICAL_FAILURE
```

Ne jamais convertir cet échec en :

```text
NO_RESULT
NOT_FOUND
```

L'absence d'un résultat dans Google/Bing ou un autre moteur général ne peut pas davantage établir l'inexistence de l'arrêt.

### 4.2. Arrêt postérieur à septembre 1994

Si l'arrêt est postérieur à septembre 1994 et ne relève pas d'une exception de publication connue, une impossibilité persistante d'accéder au document doit être décrite comme une limitation technique de l'audit.

Le statut peut rester `PARTIALLY_VERIFIED` ou `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES` selon les autres preuves obtenues.

## 5. juriDict

juriDict donne accès au contenu juridique de la jurisprudence et renvoie à des arrêts et ordonnances de non-admission.

La structure est divisée en branches francophone et néerlandophone.

### 5.1. Couverture

La documentation officielle francophone indique un accès systématique à partir du n° 61.000 du 17 juillet 1996 ; avant cette date, la reprise est sporadique. Les décisions ne tranchant pas de nouvelles questions juridiques peuvent ne pas y figurer.

Les informations de couverture doivent être vérifiées dans chaque langue lorsque l'asymétrie entre les interfaces ou taxonomies est pertinente.

### 5.2. Taxonomies FR/NL

Règle impérative :

```text
juriDict FR ≠ traduction de juriDict NL
```

Ne jamais traduire un mot-clé ou une branche française en néerlandais, ou inversement, comme s'il s'agissait d'une équivalence taxonomique.

Rechercher chaque arborescence dans sa langue et comparer ensuite les décisions retrouvées.

### 5.3. Valeur probatoire

juriDict peut :

- découvrir une décision ;
- fournir un point de droit ;
- orienter la recherche ;
- corroborer certaines métadonnées.

juriDict ne doit pas être utilisé seul pour prétendre avoir contrôlé :

- le dispositif complet ;
- une citation textuelle étendue ;
- une page précise ;
- un passage omis ;
- un ECLI non affiché.

## 6. Types documentaires

Distinguer strictement :

- arrêt ;
- ordonnance de non-admission en cassation administrative ;
- avis de la section de législation ;
- document de l'auditorat ;
- point de droit / notice juriDict.

Un document de l'auditorat n'est pas une « conclusion d'avocat général ».

## 7. Langue

Conserver séparément :

```yaml
source_language:
decision_language:
translation_status:
```

Le site officiel publie les arrêts et ordonnances dans la langue où ils ont été prononcés.

Si une traduction institutionnelle existe, ne pas la présenter comme texte authentique sans base juridique spécifique.

## 8. Décisions anciennes

Pour les décisions antérieures à la collection moderne, utiliser `references/recueils-numerises-kul.md`.

Principe :

> **L'OCR sert à trouver ; le scan sert à vérifier.**

Ne jamais inventer un ECLI pour une ancienne décision qui n'en possède pas ou dont l'identifiant n'a pas été vérifié.

## 9. Anciens liens et URL

Ne pas fabriquer ou réutiliser aveuglément d'anciens schémas d'URL, notamment les anciens liens `arr.php`.

Une URL reconstruite à partir d'un numéro n'est jamais une preuve d'existence documentaire.

## 10. Procédure recommandée

### Cas A — numéro exact connu

```text
numéro exact
→ Recherche avancée officielle
→ document officiel
→ métadonnées
→ texte
→ citation éventuelle
```

### Cas B — nom/date mais numéro inconnu

```text
nom/date
→ collection officielle et/ou juriDict
→ candidat
→ document officiel
→ vérification
```

### Cas C — décision ancienne

```text
référence historique
→ KU Leuven / recueil numérisé
→ OCR pour localisation
→ scan pour vérification
```

## 11. Statuts

- document officiel ouvert et champs correspondants : `VERIFIED` ;
- identité corroborée mais document officiel non ouvert : `PARTIALLY_VERIFIED` ;
- aucune preuve suffisante malgré les voies accessibles : `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES` ;
- erreur technique : `TECHNICAL_FAILURE` dans `SEARCH_ATTEMPT`, sans conclusion d'inexistence ;
- contradiction établie avec le document officiel : `NOT_FOUND_OR_CONTRADICTORY` ou `VERIFIED_WITH_ANOMALY` selon le cas.

## 12. Test de non-régression

Voir T53 dans `tests/cases/benchmark-v0.3-integration.md`.

Le module n'est considéré prêt pour V1 que si :

```text
COUNCIL_OF_STATE_EXACT_NUMBER_RETRIEVAL = GREEN
```

## 13. Points d'entrée officiels vérifiés

- Jurisprudence / collection numérisée : https://www.raadvst-consetat.be/?lang=fr&page=caselaw
- Recherche avancée : https://www.raadvst-consetat.be/?lang=fr&page=caselaw_page4
- juriDict : https://www.raadvst-consetat.be/?lang=fr&page=juridict

## Traçabilité de T53

Conserver les observations brutes et la sortie réelle séparément de l'oracle. Les variantes simulées testent les décisions face aux observations fournies, pas le pilotage du site. Un succès sur un arrêt ne prouve pas la récupération générale. Un test sans sortie conservée reste `NOT_DEMONSTRATED`.
