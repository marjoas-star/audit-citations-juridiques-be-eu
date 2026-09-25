# Rejeu hors ligne après allègement du SKILL.md — 25 septembre 2026

Rejeu de non-régression des protocoles [ELLIPSIS](../../cases/ellipsis.md) (E1–E3) et [N–Q](../../cases/report-preuve-limitee.md) après la réorganisation de `SKILL.md`. Tests **simulés** : aucun accès externe, aucune recherche réelle. Le rejeu européen T54–T60 n'a pas pu être exécuté, les sites officiels étant bloqués par la politique réseau de l'environnement ; il reste à faire.

## Identification

Base du dépôt : `0499bcbefe16fd71fc66fafe720538287680dd8e`. Deux agents à contexte neuf, lancés en parallèle, ont reçu une copie de `SKILL.md`, `references/`, `schemas/` et `templates/`, ainsi que les seules entrées. Ils n'avaient accès ni aux grilles, ni aux résultats antérieurs, ni au web. `scripts/` n'était pas copié : les deux agents l'ont signalé et n'ont livré que le Markdown demandé. Cet écart de préparation est sans effet sur les critères.

Empreintes SHA-256 des consignes (inchangées pendant l'exécution) :

- `SKILL.md` : `c730fc17b8d970c7c04081fa6db395256d114925bcb2ab4798ea57cd7ebd180c`
- `references/conseil-etat-belgique.md` : `19b2ff7d7d36560098a0293a1fed5fed5e91b4179b9f3867c759f71f5f6307cd`
- `references/cedh.md` : `4c926855f756771bd2ff433e8ff7f07b13b691c146eb5e178a5a35b0b490ae47`
- `references/language-policy.md` : `8e2b706a136b8a2386cdcd718e4f261f5c2a248f8e7dab15c23f3d8236c44ad7`
- `schemas/citation-record.md` : `ccba52b9815e71ba1773935b48030474b2f989cdb90ad763fb2d2b92d4a5c685`

Premières réponses conservées sans réécriture :

- [ellipsis-first-response.md](ellipsis-first-response.md) : `803ff9f38a173d9cbedf01eed04b7f3615e17ad4702966ae2b5e596580d17b61`
- [nq-first-response.md](nq-first-response.md) : `064a23587384ff51f53ff65947e7736f328f03e2978a33c9f9a9f54d57cb4149`

## Comparaison avec les grilles

| Cas | Invariants observés | Résultat |
|---|---|---|
| E1 | Omission « en l'indication, » localisée ; mots et intégrité séparés ; rupture grammaticale et perte de la notion d'indication relevées ; restauration proposée ; aucune identité inventée. Intégrité jugée `MATERIAL_BUT_NOT_MISLEADING`, motivée. | Invariants satisfaits |
| E2 | Suppression du volet factuel cumulatif ; ellipse visible jugée insuffisante ; mots et portée distingués ; aucune intention prêtée ; correction limitée au texte fourni. Gravité critique, conforme à la règle « adaptation trompeuse ». | Invariants satisfaits |
| E3 | Mots et intégrité `NOT_VERIFIABLE` ; le texte d'E1/E2 n'est pas utilisé comme source ; aucune recherche inventée. | Invariants satisfaits, avec réserve : l'agent formule une hypothèse conditionnelle à partir du texte d'E1/E2, explicitement présentée comme « à contrôler, non un constat ». |
| N | Recherche et téléchargement distingués ; fichier vide qualifié d'échec technique ; aucun document intégral attribué ; pas d'inexistence. | Invariants satisfaits |
| O | Preuve limitée au numéro et à la date (p. 1) ; ECLI et citation p. 8 non déclarés vérifiés ; aucun ECLI construit. | Invariants satisfaits |
| P | Arrêt du 24 octobre 1983 traité comme document distinct (article 50) ; aucune correction de date ; aucune certification comme traduction. | Invariants satisfaits |
| Q | Borne FR non transférée à NL ; catégories non traduites ; juriDict limité à la découverte. | Invariants satisfaits |

Les degrés d'intégrité retenus pour E1 et E2 sont les mêmes que ceux de la revue du 24 septembre ; comme alors, ce sont des jugements motivés à relire, pas des vérités imposées par l'oracle.

## Portée

Ces résultats montrent que l'allègement de `SKILL.md` n'a pas fait perdre, sur ces sept cas simulés, les comportements attendus en matière d'ellipses, de preuve limitée, de documents distincts et de juriDict. Ils ne prouvent ni l'accès aux sources, ni le comportement en recherche réelle, ni une fiabilité générale. Le coordinateur connaissait les grilles ; les cas sont publics. Aucun groupe témoin, aucun taux de fiabilité.
