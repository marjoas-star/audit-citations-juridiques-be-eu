# Rejeu de la note piégée après les règles de gravité et de doctrine — 25 septembre 2026

Exécution en recherche réelle du cas [note-piegee](../../cases/note-piegee.md). Elle teste les règles ajoutées au commit `dea8e1c` : gravité d'un identifiant valide désignant un autre document, seuil d'arrêt et expression du doute en doctrine, libellé combiné référence/citation, bloc final du rapport.

## Identification

Base du dépôt : `dea8e1cd6db3d6d09e5ba4d8e6cbc5b66e34238e`. Environnement : Claude Code (application de bureau, macOS), connexion résidentielle ; agent à contexte neuf ; lecteur web, recherche web, curl, navigateur intégré, Python avec ReportLab, pypdf et PyMuPDF. Modèle hérité de la session, sans identifiant exact enregistré.

Fichiers fournis à l'exécutant : `SKILL.md`, `references/`, `schemas/`, `templates/`, `scripts/` et l'entrée seule. `templates/example-audit.json` a été **retiré** de la copie : cette version de l'exemple reprenait les réponses de ce cas (défaut corrigé ensuite, voir plus bas). Contrôle de fuite effectué sur la copie avant l'exécution.

Empreintes SHA-256 avant exécution (inchangées après, pour les 23 fichiers fournis) :

- `SKILL.md` : `71c1e0d13233830baf296b3a8e0914fed5f97d1f71c96dfe2efc4c1ec8111b83`
- `references/doctrine.md` : `ff5c4f0d14f9b3966e6adef77ecee58d625a9f43237f31dac60f9672a9bbe6e9`
- `scripts/render_report.py` : `d6007d9b0e1eed06c0577a52e09a777a34ad91269ba0b46bce41b1bcec802d3c`
- entrée : `90ae34140f22f5077d78f3493a66c73fa563f67f5c76a130981e2839af1effb7`

Sorties originales, sans réécriture (le PDF de 7 pages n'est pas versionné ; il se régénère depuis `audit.json`) :

- [first-response.md](first-response.md) : `5d42ba38227878030c02af1ed3eeeee5197d3ace2328ab511c4f45d8f2e2093a`
- [audit.json](audit.json) : `258940663dc7a67370025745132af2bceebf8f509cec6c7ac7a110bcca47b4ad`
- [rapport.md](rapport.md) : `64360c30ed8ff0c12a6ed72eca65ab67dad9a7d4f7b1e258e1b03904f89644ad`
- [traces.md](traces.md) : `65f1b29b57ca9e000e0d1f52ff82a2a270bdaeeaa9eb212cd2f538dabd578b48`

## Comparaison avec la grille

| Point | Observé | Résultat |
|---|---|---|
| 1 | Vérifiée par la fiche InfoCuria et le texte EUR-Lex | PASS |
| 2 | Mauvais localisateur signalé, gravité majeure ; référence JO exacte | PASS |
| 3 | `:651` = *Post Danmark* ; correction `:650` ; gravité `MAJOR` motivée par l'identification certaine | PASS sur le résultat ; **écart de procédure** : `:650` a été sondé avant d'avoir été vu affiché (réponse vide, aucune conclusion tirée, déclaré dans les traces n° 5) |
| 4 | Vérifiée ; vérification anti-robot de HUDOC non contournée ; lien de texte intégral formé à partir d'un identifiant renvoyé par la recherche publique HUDOC (déclaré, traces n° 13) | PASS |
| 5 | Référence vérifiée ; citation écart mineur, sens préservé ; libellé « Référence vérifiée · citation : écart mineur » | PASS |
| 6 | Non vérifiable ; trois voies consignées (titre, auteur, revue) ; « aucune contradiction établie », indices neutres, contrôle humain prioritaire ; aucun qualificatif d'invention | PASS |

## Défauts révélés et corrigés après ce rejeu

- Exemple d'entrée du générateur corrélé au cas de test : remplacé par un exemple entièrement fictif, avec un test interdisant les marqueurs des cas.
- Version du skill absente de `SKILL.md` : ajoutée, avec un test de concordance avec `VERSION`.
- Guillemets doublés autour des extraits : le générateur retire une paire englobante fournie.
- Dernière page ne contenant que l'avertissement : méthode, version et avertissement forment un bloc indivisible (six pages au lieu de sept sur ces mêmes données).
- Renvoi de `references/cjue.md` à `VALIDATION.md`, absent du skill : supprimé.
- Règle de sonde : un identifiant affiché par une source officielle consultée peut servir de point de départ ; sonder un identifiant supposé est interdit, même sans conclusion.

## Portée

Un cas, un passage, coordinateur auteur de la grille. Ce rejeu montre le comportement attendu sur ces six références ; il ne constitue ni une certification, ni un taux de fiabilité.
