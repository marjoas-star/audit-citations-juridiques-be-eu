# Notes de version

## Non publié

- `SKILL.md` allégé (environ 3 200 → 2 200 mots) et réorganisé en 12 sections : règles cardinales regroupées, table de routage par famille de sources, doublons avec le module Conseil d'État réduits. Aucune règle d'audit supprimée.
- Règles de maintenance, benchmarks, release blockers, versionnement et licence déplacés dans `CONTRIBUTING.md`.
- Description enrichie de formulations de déclenchement (FR/NL/EN).
- README : installation dans Claude Code et l'application Claude.
- Rejeu hors ligne ELLIPSIS E1–E3 et N–Q sur la version allégée : invariants satisfaits (simulations) ; rejeu européen T54–T60 en attente d'un accès réseau. Voir `tests/results/skill-allege-replay/`.
- Rejeu européen T54–T60 en recherche réelle sur la version allégée, exécuté en local : sept cas conformes à la grille, sans invention, sur-vérification ni fusion. Voir `tests/results/eu-v05-local-replay/`.
- Sonde par identifiant cité : ouvrir une base officielle avec un ECLI, CELEX, ELI ou numéro d'affaire tel qu'il est cité, ou mécaniquement transcrit, est une tentative de recherche et non une reconstruction ; règle précisée dans `SKILL.md`, `references/eur-lex-legislation.md` et `references/cjue.md`, avec la voie d'accès observée pour EUR-Lex.
- Isolation des rejeux : liste des fichiers fournis à l'exécutant et exclusion des fichiers de résultats (`CHANGELOG.md`, `VALIDATION.md`, `RELEASE.md`) dans `CONTRIBUTING.md`.
- Générateur de rapport : titres « Méthode suivie » et « Avertissement », avertissement complet (sources, interfaces, vérification humaine), refus d'une date d'établissement ou de révision postérieure à l'heure réelle, libellé combiné lorsqu'une référence exacte comporte une citation inexacte (« Référence vérifiée · citation : écart mineur »), champ `skill_version` (l'ancien `version` reste accepté).
- `requirements.txt` (ReportLab, pypdf) et exemple d'entrée complet `templates/example-audit.json`, validé par les tests.
- Gravité précisée pour un identifiant valide désignant un autre document ; module doctrine complété par un seuil d'arrêt des recherches et une manière d'exprimer un doute sérieux sans affirmer l'invention.
- Rejeu réel de la note piégée à six références : grille satisfaite, un écart de procédure déclaré (sonde d'un identifiant non encore affiché). Voir `tests/results/note-piegee-replay/`.
- Corrections issues de ce rejeu : exemple d'entrée entièrement fictif, version du skill indiquée dans `SKILL.md`, guillemets d'extrait non doublés, bloc final du PDF indivisible, renvoi à `VALIDATION.md` retiré de `cjue.md`, règle de sonde étendue aux identifiants affichés par une source officielle et interdisant la sonde d'un identifiant supposé.
- Licence du code : les fichiers Python de `scripts/` et `tests/` passent sous PolyForm Noncommercial 1.0.0 (`LICENSE-CODE.md`, en-têtes SPDX), licence conçue pour du logiciel et qui conserve la restriction non commerciale ; la documentation reste sous CC BY-NC-SA 4.0.
- Expérience des juristes : `MODE-EMPLOI.md` (installation pas à pas, accès à donner, domaines pour l'administrateur, durée à prévoir, lecture du rapport, confidentialité, problèmes fréquents), signalé en tête des README. `SKILL.md` : contrôle des accès avant l'inventaire, message de départ avec fourchette de durée indicative (1 à 3 minutes par source), points d'étape et messages en langage courant, sans codes internes. Mode d'emploi centré sur Claude Cowork (navigateur intégré indispensable pour EUR-Lex, CURIA, HUDOC et le Conseil d'État, réglages administrateur, quota d'utilisation). Traductions : `HANDLEIDING.md` (NL), `ANLEITUNG.md` (DE), `USER-GUIDE.md` (EN).
- Doctrine : plateformes d'éditeurs sur abonnement (par exemple Strada lex) non tentées et seulement indiquées au juriste ; Jurisquare, fermé depuis 2024, n'est plus ni consulté ni proposé.
- Précisions issues du rejeu d'expérience utilisateur : gravité `MAJOR` pour une mauvaise disposition (sauf contenu identique), métadonnées officielles suffisantes pour les champs d'identité mais pas pour les passages, voie publique alternative d'un même site officiel distinguée d'un contournement, pas de message de départ pour trois sources ou moins, application de bureau à laisser ouverte dans Cowork, trait d'union insécable normalisé dans le PDF.

## 0.5.0-beta.3 — 25 septembre 2026

Datation persistante des rapports et révisions, contrôle de version avant alerte, axes de citation séparés, erreurs et suggestions distinctes, preuves visibles, regroupement des occurrences et nettoyage de la restitution. Validation documentaire et tests de rendu ne constituent pas une certification générale.

## Après 0.5.0-beta.2 — sources de développement

- Dates d'adoption, d'annonce, de publication et versions institutionnelles distinguées ; consultation clôturée distincte de version finale.
- Références JO et titres abrégés évalués selon le contexte éditorial, sans faux défaut documentaire automatique.
- Habilitation et disposition mise en œuvre des actes délégués/d'exécution contrôlées séparément, avec champs de preuve correspondants.
- Rejeu européen T54–T60 révisé ; résultats et limites documentés séparément des anciens résultats déclarés.

Ces modifications concernent les sources de la branche principale. L'archive publiée sous le tag 0.5.0-beta.2 reste inchangée.

## 0.5.0-beta.2 — 24 septembre 2026

- Présentation juridique française réutilisable : synthèse, corrections, fiches, citations et limites ; générateur PDF/Markdown et cinq tests de conditionnement.
- Récupération des PDF du Conseil d’État depuis les liens observés, contrôle du contenu reçu et de la langue ; compléments T53-R et précisions FR/NL de juriDict.
- Protocole prospectif V1 et plan du corpus réservé, sans revendication de campagne indépendante exécutée.


## 0.5.0-beta.1 — première publication publique

- Recherche exacte prioritaire du Conseil d’État belge par formulaire officiel ; panne distincte d’absence de résultat.
- Preuves par champ, identité de source distincte des occurrences et des documents liés.
- Contrôle séparé des mots, adaptations, langues et intégrité des citations.
- Vérification des renvois dans tous les extraits effectivement fournis.
- Contexte d’audit et statuts d’occurrence explicités ; prérequis de lecture et de rapport documentés.
- Essais réels et simulations distingués ; protocole d’ellipse prospectif par invariants.

Les anciens numéros de travail et annonces de validation non traçables ne sont pas des publications validées. Cette première bêta conserve les limites exposées dans VALIDATION.md et ne revendique pas une certification générale V1.
