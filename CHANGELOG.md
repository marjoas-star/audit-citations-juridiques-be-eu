# Notes de version

## 0.9.0-rc.1 — 26 septembre 2026

Version candidate pour les essais de stabilité qui conditionnent la 1.0 (voir `CONTRIBUTING.md`) : formulaire de retour sans compte, rapports plus courts sans perte d'information, mise à jour par « Remplacer », règle sur les traductions, possibilité d'utiliser ChatGPT (non testée). Pré-version : la 0.7.0-beta.1 reste la version proposée par défaut.

- Modes d'emploi et page d'installation : mise à jour par « Remplacer » (menu ⋮ de la fiche du skill) au lieu de supprimer puis réimporter.
- Rapports plus courts sans perte d'information : une référence qui appelle une correction n'est présentée qu'une fois, avec sa correction ; une même preuve n'est plus répétée ; tableau récapitulatif et listes plus compacts ; le générateur compte les pages et signale un dépassement de la cible ; budget de 120 mots pour la synthèse ; raccourcir et relancer une fois devient obligatoire. Sur les rapports du bêta-test : B 14 → 11 pages, D 11 → 9, E 7 → 6, sans réécriture du contenu.
- Retours des utilisateurs sans compte GitHub : formulaire de deux minutes en quatre langues (Google Forms, textes dans `retours/FORMULAIRE.md`), lien en fin de chaque rapport dans sa langue (« Votre avis »), dans le message de fin d'audit, les modes d'emploi et les README, avec invitation à mettre une étoile sur GitHub (test ajouté).
- Version 1.0 redéfinie comme « stable » et non « validée » : non-régression rejouée deux fois (dont une dans Cowork), épreuve sur documents réels, formats figés, essai public d'au moins quatre semaines d'une version 0.9.x, documentation complète (`CONTRIBUTING.md`). Procédure de traitement des retours. Le protocole de validation indépendante devient un objectif facultatif.
- Possibilité d'utiliser le skill avec ChatGPT (skills des offres Business, Enterprise, Healthcare et Edu ; ChatGPT Work dans l'application de bureau) : section dédiée dans les quatre modes d'emploi, mentions du navigateur rendues neutres dans `SKILL.md`. Non encore testé.
- Retour du rapport E en néerlandais (0.7.0-beta.1, Cowork) : rapport entièrement localisé, 7 pages au lieu de 9, 3 erreurs sur 3. Corrigé : une traduction fidèle non signalée est une suggestion, non une erreur ; l'édition du Moniteur (« deuxième édition ») est recherchée explicitement pour la correction.
- Deux archives par version : allégée (30 fichiers, à importer dans Claude) et complète (`-complet`). Liens vers `tests/` remplacés par des adresses GitHub, pour rester valables dans l'archive allégée.
- Modes d'emploi : parade à la décompression automatique des `.zip` par Safari.
- Lien de téléchargement direct et permanent (`…/releases/latest/download/audit-citations-juridiques-be-eu.zip`) dans les modes d'emploi ; la publication est marquée « Latest ».

## 0.7.0-beta.1 — 25 septembre 2026

Rapport en français, néerlandais, allemand ou anglais. Corrections issues du bêta-test v2 dans Claude Cowork (22 erreurs sur 22 détectées, aucune fausse alerte), régressions corrigées et vérifiées à l'aveugle sur deux extraits. Rapport plus court et plus lisible, durée et date juridique mieux annoncées, description adaptée à l'aperçu de l'application, interdiction renforcée des recherches fondées sur la mémoire. Aucune certification générale.

- Description du skill ramenée sous 500 caractères : l'aperçu de l'application Claude coupe au-delà (test ajouté). Mode d'emploi français aligné sur les libellés de l'interface française (Paramètres › Compétences).
- Retour du premier audit réel dans Claude Cowork (extrait A du bêta-test v2, 4 erreurs sur 4, 1 précision, 3 informations de vigueur, 0 faux positif ; navigateur intégré efficace pour le Conseil d'État, Justel, EUR-Lex et la Cour constitutionnelle) : règle cardinale « chercher à partir du document, jamais de sa mémoire » après la sonde d'un numéro d'arrêt non cité ; vouvoiement par défaut ; CELEX transcrit d'un numéro d'affaire admis sous contrôle du type de document ; réutilisation de l'adresse de résultat du formulaire du Conseil d'État avec un numéro cité.
- Durée annoncée revue à la baisse (environ une minute par source, souvent moins ; une douzaine de sources : 5 à 15 minutes), l'essai dans Cowork ayant pris quelques minutes pour 12 sources. Le message de départ annonce la date juridique retenue et invite le juriste à en indiquer une autre ; seuls les contrôles dépendant de la date sont alors refaits. Modes d'emploi mis à jour dans les quatre langues.
- Rapport dans la langue de l'utilisateur : le générateur produit désormais le rapport PDF et Markdown en français, néerlandais, allemand ou anglais (`report_language`), statuts, dates et avertissement compris. Couleurs des statuts calculées à partir des statuts, et non plus du texte français.
- Retours du bêta-test v2 dans Cowork (22 erreurs sur 22 détectées, aucune fausse alerte ; synthèse dans le coffre du coordinateur) : inventaire des références citées sans note et des décisions évoquées ; « référence probablement inexistante » lorsque tous les identifiants renvoient ailleurs et que la recherche par parties et date échoue ; citation fidèle d'une version non applicable distinguée d'une citation inexacte ; comparaison effective avec la version d'origine d'une citation traduite ; doctrine lue sur la seule notice : vérification partielle et proposition de fournir l'extrait.
- Rapport plus court et plus lisible : dates en toutes lettres, suppression des mentions techniques (« Rapport v1 », « Actualisation ultérieure : aucune », « Référence constatée : identique »), références confirmées sans réserve regroupées en fin de rapport, chiffres de la synthèse contrôlés par rapport aux compteurs.
- Demande-type des modes d'emploi complétée par la date juridique du document.
- Régressions du bêta-test v2 corrigées (correction complète, auteur réel d'un passage mal attribué, affirmations datées, borne de date, une source par article, renvois exacts) et vérifiées par un rejeu à l'aveugle des extraits B et D. Longueur : budget de mots par champ, signalé par le générateur sans rien couper ; suggestions facultatives n'empêchant plus le regroupement en fin de rapport.
- Interdiction de principe maintenue pour les recherches fondées sur la mémoire (décision de l'auteur du skill) ; réflexe de provenance avant chaque requête et conduite à tenir en cas d'écart.

## 0.6.0-beta.1 — 25 septembre 2026

Version tournée vers les juristes : mode d'emploi en quatre langues centré sur Claude Cowork, contrôle des accès avant l'audit, durée annoncée, messages en langage courant. Règles de sonde, de gravité et de doctrine précisées, générateur de rapport plus lisible, licence logicielle distincte pour le code. Rejeux réels et d'expérience utilisateur consignés ; aucune certification générale.

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
