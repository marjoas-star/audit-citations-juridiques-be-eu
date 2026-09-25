# Rejeu d'expérience utilisateur : contrôle des accès et messages au juriste — 25 septembre 2026

Deux exécutions de la note piégée ([note-piegee](../../cases/note-piegee.md)) sur la version `bc038f1bd5ea608a6a3bf7c90c8626a2957157d8`, pour tester la section 10 de `SKILL.md` (communication avec l'utilisateur). Chaque agent, à contexte neuf, jouait Claude face à un juriste et consignait mot pour mot chaque message qu'il lui adressait. Fichiers fournis : `SKILL.md`, `MODE-EMPLOI.md`, `references/`, `schemas/`, `templates/`, `scripts/render_report.py` et l'entrée ; contrôle de fuite effectué ; empreintes inchangées après exécution (`SKILL.md` : `cb4a9938f46674c36b99ec9388475274749524c12468a82bf8dd8cef8e8bd190`, `MODE-EMPLOI.md` : `340f8451a14648517481849f781ce461afed70d49fa962e256093f8916dd126f`).

Demande du juriste, identique dans les deux cas : « Utilise le skill audit-citations-juridiques-be-eu pour vérifier toutes les références et citations du document joint. Produis un rapport en français, en PDF. »

## A. Sans accès au web ([sans-web/](sans-web/messages-utilisateur.md))

Environnement simulé sans recherche, lecture de pages ni navigateur. Attendu : ne pas commencer, expliquer en clair, renvoyer au mode d'emploi.

Observé : un seul message de trois phrases, sans jargon ni code interne ; audit non commencé, aucun PDF ; explication de la conséquence (tout serait « non vérifiable ») ; renvoi à la section « Les accès à donner à Claude » et invitation à relancer dans une nouvelle conversation. **Conforme.**

Empreinte : `5373006acee5abbda85a10213edc826f4a848e08aebd4164d51b333dade6a6e1`.

## B. Avec accès ([avec-acces/](avec-acces/messages-utilisateur.md))

Recherche web, lecture de pages, curl et navigateur intégré, sur une connexion résidentielle. Durée réelle : 6 min 36 s pour six sources.

| Attendu | Observé |
|---|---|
| Contrôle des accès avant l'inventaire | Signalé dans le message de départ (« Les accès nécessaires fonctionnent ») |
| Message de départ : sources, étapes, fourchette, ce que doit faire le juriste | Six sources nommées en clair, étapes, « entre 10 et 25 minutes environ », « vous n'avez rien à faire » |
| Points d'étape à un changement réel, avec compteurs | Un point d'étape « 3 sources sur 6 », avec les deux corrections déjà établies |
| Fin : corrections, puis à vérifier, puis confirmé ; rappel « non vérifiable » ≠ erreur | Respecté ; emplacement des fichiers indiqué |
| Aucun code interne ni jargon dans les messages | Respecté |
| Résultats d'audit (grille de la note piégée) | Conformes ; gravité de l'article 4 du RGPD notée `MINOR` (voir ci-dessous) |

Empreintes : `messages-utilisateur.md` `530e3eba3276900eccc668902ccd6907339cbeeb2db2eb35412ee52ad3120567` ; `audit.json` `fb149c713f93a44bf2036846598979c6c2e07b770a1b3123ac4de2b965dc4ace` ; `rapport.md` `a175f94cadb3c0778ab79b0f88ccce4d592138fcc8fd2e99e688b83c322e2bd8` ; `traces.md` `c6e827696747fdc451e54ee3f20140d0ab0a0cc6cd0bd7a0ca2e6d2a582089b6`.

Écart de forme : l'heure du premier message n'a pas été relevée.

## Ambiguïtés révélées et corrigées ensuite

- Durée : la règle « pas de durée pour quelques références » contredisait le message de départ ; seuil fixé à trois sources.
- Gravité d'une mauvaise disposition : notée `MAJOR` dans le rejeu précédent et `MINOR` ici ; règle fixée (`MAJOR` sauf contenu identique).
- Statut d'une source confirmée par métadonnées officielles sans texte intégral : précisé (identité oui, passages non).
- Moteur de recherche public de HUDOC utilisé après un contrôle anti-robots du navigateur : voie publique alternative distinguée d'un contournement.
- Jurisquare tenté pour un sommaire de revue : plateforme fermée depuis 2024 ; les plateformes d'éditeurs sur abonnement ne sont plus tentées, seulement indiquées au juriste.
- Trait d'union insécable affiché comme un carré dans le PDF : caractères absents de la police remplacés dans le PDF.
- Cowork : le message de départ demande de laisser l'application de bureau ouverte.

## Portée

Un document, un passage par scénario, coordinateur auteur de la grille ; l'absence d'accès était simulée par consigne. Ces essais montrent le comportement attendu des messages ; ils ne mesurent ni la compréhension par des juristes réels ni une fiabilité générale.
