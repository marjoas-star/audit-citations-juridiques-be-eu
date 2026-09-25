# Audit de quatre situations de recherche (N, O, P, Q)

## Fichiers du skill lus

- `skill/SKILL.md`
- `skill/references/routing.md`
- `skill/references/conseil-etat-belgique.md`
- `skill/references/cedh.md`
- `skill/references/language-policy.md`
- `skill/references/datation-et-rapport.md`
- `skill/schemas/citation-record.md`
- `skill/templates/report-template.md`

Non lus (sans pertinence pour ces quatre situations) : les autres modules de `references/` et `templates/report-rendering.md`. Le script `scripts/render_report.py` cité par le skill ne figure pas dans le répertoire fourni ; seul le Markdown est livré, **aucun PDF n'a été produit**.

## Datation

- Rapport établi le : 2026-09-25T13:19:16+02:00 (Europe/Brussels)
- Version du rapport : 1 (première réponse, gelée pour l'évaluation)
- Version des instructions : révision du 24 septembre 2026
- Période des vérifications : aucune consultation effectuée par l'auditeur. Les seules prémisses sont les observations fournies dans la consigne ; leurs dates de consultation ne sont pas fournies et restent **inconnues**.
- Date juridique de référence : non fournie ; sans incidence sur les conclusions ci-dessous.

## 1. Synthèse

| Situation | Référence visée | Statut | Niveau de preuve le plus élevé atteint | Point clé |
|---|---|---|---|---|
| N | Arrêt n° 42 (juridiction non précisée dans les observations) | **Vérification partielle** | Résultat de recherche officiel | Le PDF téléchargé est vide (0 octet) : c'est un échec technique d'ouverture, pas un document consulté, et pas une preuve d'inexistence. |
| O | Arrêt dont le PDF officiel a été ouvert | **Vérification partielle** | Document officiel intégral (pour le numéro et la date seulement) | Numéro et date vérifiés en page 1 ; ECLI non vérifié ; la citation de la page 8 n'a pas été contrôlée. |
| P | Arrêt CEDH du 25 mars 1983 | **Vérification impossible avec les sources accessibles** | Aucun pour le document visé | Le candidat du 24 octobre 1983 (article 50) est un autre arrêt de la même affaire : il ne vérifie pas la référence et ne permet pas de la « corriger ». |
| Q | Recherche juriDict (aucune décision identifiée) | Pas de statut de référence ; couverture NL non vérifiée | Découverte uniquement | La divergence FR/NL des catégories est normale (arbres indépendants) ; la borne FR ne vaut pas pour la branche NL. |

Compteurs : 4 situations examinées ; 3 références visées (N, O, P) ; 0 vérifiée intégralement ; 2 partiellement vérifiées (N, O) ; 1 non vérifiable avec les sources accessibles (P) ; 0 non retrouvée ou contradictoire. Citations textuelles : 1 relevée (O, page 8), 0 contrôlée. Aucune anomalie d'erreur établie dans les références elles-mêmes. Aucun pourcentage de fiabilité n'est calculé.

## 2. Alertes et points d'attention

1. **N — ne pas conclure à l'inexistence ni à la vérification.** Un transfert HTTP 200 qui livre un fichier de zéro octet n'est pas un document obtenu. La tentative d'ouverture est un **échec technique** ; le résultat de recherche officiel reste valable, mais seulement au niveau des métadonnées affichées.
2. **O — ne pas étendre la preuve du PDF aux champs non contrôlés.** L'ouverture du document officiel ne valide ni l'ECLI (absent du document), ni la citation de la page 8 (non lue).
3. **P — ne pas substituer le candidat à la cible.** Même parties et mêmes requêtes ne signifient pas même document : la Cour peut rendre un arrêt au fond puis un arrêt distinct sur la satisfaction équitable (ancien article 50). Aucune correction de date n'est établie.
4. **Q — ne pas traduire une catégorie juriDict FR en catégorie NL**, ni transférer la borne de couverture FR à la branche NL.

## 3. Fiches détaillées

### Situation N — arrêt n° 42 : PDF vide

**Observations fournies.** Un résultat officiel annonce l'arrêt 42 ; le téléchargement répond HTTP 200 mais livre un fichier PDF de zéro octet ; seules les métadonnées affichées au résultat sont disponibles.

**Statut : vérification partielle** (code interne `PARTIALLY_VERIFIED`), à condition que les métadonnées affichées concordent avec la référence citée — les valeurs affichées (date, parties, etc.) ne figurent pas dans les observations fournies et ne peuvent donc pas être reprises ici.

**Champs réellement établis**

| Champ | Valeur | Statut du contrôle | Niveau de preuve |
|---|---|---|---|
| Existence d'un résultat officiel pour l'arrêt 42 | oui | établi | résultat de recherche officiel (`OFFICIAL_SEARCH_RESULT`) |
| Numéro | 42 | établi au niveau du résultat | résultat de recherche officiel |
| Autres métadonnées affichées | non transmises dans les observations | établies seulement au niveau du résultat, valeurs non reprises | résultat de recherche officiel |
| Juridiction | non précisée dans les observations | non établie par ce rapport | — |
| Nature du document, parties, langue, rôle | — | non vérifiés au niveau du document | aucun document ouvert |
| ECLI | — | non vérifié ; ne doit pas être construit à partir du numéro | — |
| Texte, passage cité, page | — | non vérifiables | — |

**Traces (tentatives distinctes)**

- Recherche : succès, résultat trouvé (`SUCCESS` / `RESULT_FOUND`), niveau résultat de recherche officiel.
- Ouverture/téléchargement : **échec technique** (`TECHNICAL_FAILURE`) — observation de contenu : fichier vide, 0 octet, malgré HTTP 200. Le statut HTTP et l'extension PDF ne prouvent pas que le contenu a été obtenu (pas de signature PDF, pas de page, pas d'identité vérifiable).

**Limites.** L'échec est technique ; il ne vaut ni « aucun résultat » ni inexistence. Le niveau de preuve ne dépasse pas celui du résultat de recherche. Aucun extrait probant n'existe.

**Suite possible (vérification humaine ou nouvelle tentative).** Relever le lien réellement affiché dans le résultat et retenter le téléchargement de ce même lien avec **un** autre client standard, sans reconstruire d'URL ni contourner de contrôle d'accès ; vérifier alors signature PDF, nombre de pages et identité du document. En cas d'échec persistant, consigner la limite. S'il s'agit du Conseil d'État et d'un arrêt postérieur à septembre 1994, l'impossibilité d'accès reste une limite technique de l'audit.

### Situation O — PDF officiel ouvert, citation non contrôlée

**Observations fournies.** PDF officiel ouvert ; numéro et date vérifiés en page 1 ; ECLI absent ; la citation attribuée à la page 8 n'a pas été consultée.

**Statut : vérification partielle** (`PARTIALLY_VERIFIED`). L'identité est solidement établie pour le numéro et la date, mais le statut ne peut dépasser la preuve obtenue : l'ECLI et la citation ne sont pas vérifiés.

**Champs réellement établis**

| Champ ou passage | Statut du contrôle | Niveau de preuve | Localisateur |
|---|---|---|---|
| Numéro | vérifié | document officiel intégral (`OFFICIAL_FULL_DOCUMENT`) | page 1 |
| Date | vérifiée | document officiel intégral | page 1 |
| ECLI | **non vérifié** — absent du document ouvert ; aucune source suffisamment forte ne le fournit | aucun | — |
| Nature, parties, langue, rectifications | non déclarés contrôlés dans les observations | non transférés depuis le PDF | — |
| Citation, page 8 | **non contrôlée** | aucun (page non lue) | page 8 non consultée |

**ECLI.** L'absence d'ECLI dans le PDF ne prouve pas qu'un ECLI cité serait faux : elle signifie seulement qu'il n'est pas vérifié. Aucun ECLI ne doit être construit à partir du numéro et de la date. Pas de constat de contradiction.

**Contrôle de la citation (page 8)**

| Élément | Résultat |
|---|---|
| Statut textuel | **Vérification impossible en l'état** (`NOT_VERIFIABLE`) — la page n'a pas été lue ; elle est toutefois accessible dans le document ouvert, le contrôle reste donc faisable |
| Adaptations (ellipses, crochets) | non évaluées |
| Intégrité du sens | non vérifiable (`NOT_VERIFIABLE`) |
| Localisateur « page 8 » | non vérifié |
| Locuteur (juridiction, partie, texte reproduit) | non identifié |

**Suite.** Lire la page 8 du même PDF officiel, comparer mot à mot, examiner toute ellipse ou insertion et identifier qui s'exprime dans le passage. Une vérification complète exigerait aussi le contrôle de la nature et des parties.

### Situation P — arrêt CEDH du 25 mars 1983 et candidat du 24 octobre 1983

**Observations fournies.** Arrêt recherché : 25 mars 1983. Candidat trouvé, en français : mêmes parties, mêmes requêtes, daté du 24 octobre 1983, relatif à l'article 50 (satisfaction équitable dans l'ancienne numérotation de la Convention).

**Statut : vérification impossible avec les sources accessibles** (`NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES`). L'absence de vérification ne signifie pas que la référence est erronée.

**Pourquoi ni « vérifiée », ni « partielle », ni « contradictoire »**

- Le candidat est un **document distinct** : date différente et objet propre (article 50). Les mêmes parties et requêtes peuvent désigner plusieurs arrêts, typiquement un arrêt au fond puis un arrêt sur la satisfaction équitable.
- La preuve relative à un candidat écarté ne justifie pas une vérification partielle de la cible ; seul un lien d'affaire (parties et requêtes communes) est corroboré, sans qu'aucun champ d'identité de l'arrêt du 25 mars 1983 soit établi.
- Aucune contradiction n'est établie : ne pas avoir retrouvé l'arrêt du 25 mars 1983 dans ces observations ne prouve pas son inexistence. Le statut « non retrouvée ou contradictoire » serait donc une sur-interprétation.

**Champs réellement établis**

| Élément | Statut |
|---|---|
| Arrêt du 25 mars 1983 — date, nature, formation, identifiant, texte | non établis |
| Relation : même affaire (parties et requêtes communes) avec l'arrêt du 24 octobre 1983 | observée, conservée comme relation distincte ; niveau de preuve non précisé par les observations (base consultée non indiquée) |
| Arrêt du 24 octobre 1983 | document distinct, français, article 50 ; ne doit pas être fusionné avec la cible |

**Correction.** **Aucune correction n'est proposée** : remplacer « 25 mars 1983 » par « 24 octobre 1983 » transformerait un « non vérifié » en « corrigé » par approximation et substituerait un autre arrêt. Aucun identifiant HUDOC ni URL ne doit être déduit de ceux du candidat ou d'une autre version linguistique.

**Suite (vérification humaine).** Dans HUDOC, rechercher par numéros de requête, en contrôlant la date (25 mars 1983), la nature (arrêt, pas décision ni rapport de la Commission) et l'objet (fond), puis accéder à la version linguistique par un lien observé. Si le passage cité provient d'une autre langue, séparer comparaison sémantique et vérification des mots.

### Situation Q — juriDict : catégories FR/NL différentes, borne FR seule consultée

**Observations fournies.** Les catégories juriDict FR et NL diffèrent ; seule la borne de couverture FR a été consultée.

**Statut.** Aucune référence n'est identifiée par cette situation : il n'y a pas de statut de référence à attribuer. juriDict est une voie de **découverte** ; toute décision qu'il ferait apparaître resterait à vérifier sur le document officiel intégral.

**Analyse**

- **Catégories différentes : pas une anomalie.** Les arbres FR et NL sont indépendants ; une catégorie FR n'est pas la traduction d'une catégorie NL. Chaque arbre doit être parcouru dans sa langue, puis les décisions retrouvées sont comparées (et non les intitulés).
- **Borne FR : établie seulement pour la branche FR**, selon l'observation fournie (sa valeur n'étant pas reprise dans l'observation, elle n'est pas reproduite ici comme constat de l'audit).
- **Borne NL : non vérifiée.** Elle ne doit pas être déduite de la borne FR. Le skill signale d'ailleurs que les documentations FR et NL peuvent annoncer des couvertures différentes ; cette connaissance d'instruction ne remplace pas une consultation et n'est donc pas présentée comme vérifiée ici.
- **Portée d'un résultat nul.** Une absence dans une branche, ou dans juriDict en général, ne prouve pas l'inexistence d'une décision ; la couverture juriDict est distincte de la collection générale des arrêts.

**Champs réellement établis.** Divergence des catégories FR/NL (observée) ; borne de couverture FR (observée, pour FR seulement). Rien d'autre.

**Suite.** Consulter la présentation de la couverture NL et la consigner séparément ; mener la recherche dans chaque arbre ; ouvrir le document officiel de toute décision retenue.

## 4. Niveau de preuve par champ (récapitulatif)

| Situation | Champ ou passage | Statut du contrôle | Preuve |
|---|---|---|---|
| N | Numéro 42 (et métadonnées affichées) | établi au niveau du résultat | résultat de recherche officiel |
| N | Contenu du document | échec technique (fichier vide) | aucune |
| O | Numéro, date | vérifiés | document officiel intégral, page 1 |
| O | ECLI | non vérifié (absent) | aucune |
| O | Citation p. 8 | non contrôlée | aucune |
| P | Arrêt du 25 mars 1983 | non établi | aucune |
| P | Lien d'affaire avec l'arrêt du 24 octobre 1983 | relation observée | non précisée |
| Q | Catégories FR/NL | divergence observée | découverte (juriDict) |
| Q | Borne de couverture NL | non vérifiée | aucune |

## 5. Sources consultées

Aucune consultation n'a été effectuée par l'auditeur : aucun accès externe, conformément à la consigne. Toutes les conclusions reposent exclusivement sur les observations fournies ; aucun lien, identifiant ou date de consultation n'est inventé. Recherches infructueuses significatives : N (téléchargement vide, échec technique), P (arrêt du 25 mars 1983 non retrouvé dans les observations — sans conclusion d'inexistence).

## 6. Conclusion et corrections

- **Corrections certaines : aucune.** Aucune erreur de référence n'est établie dans les quatre situations.
- **Pistes de vérification humaine :** N — nouveau téléchargement du lien observé avec un autre client standard ; O — lecture de la page 8 et contrôle de l'ECLI dans une source suffisamment forte ; P — recherche HUDOC de l'arrêt au fond du 25 mars 1983 par numéros de requête ; Q — consultation de la couverture NL et recherche dans chaque arbre.

Je ne peux pas vérifier davantage avec les sources accessibles.

## 7. Avertissement

Ce rapport est généré à l'aide de systèmes d'IA à partir des seules observations fournies. Sa fiabilité dépend de la disponibilité, de l'accessibilité, de l'indexation et de la mise à jour des sources, ainsi que de l'évolution possible de leurs interfaces. L'absence de vérification ne signifie pas qu'une référence est erronée. Une vérification humaine demeure indispensable avant toute utilisation juridictionnelle, procédurale, consultative ou scientifique.
