# Rejeu européen T54–T60 en recherche réelle après allègement du SKILL.md — 25 septembre 2026

Rejeu de la consigne [benchmark-v0.4-eu-revised](../../cases/benchmark-v0.4-eu-revised.md) sur la version allégée de `SKILL.md`, avec **recherches réelles** sur les sites officiels. Il complète le rejeu hors ligne [skill-allege-replay](../skill-allege-replay/README.md), où T54–T60 était resté en attente : depuis le conteneur cloud, EUR-Lex, Curia, le CEPD et le Conseil d'État refusaient les connexions (adresses de centres de données). Cette exécution a été faite en local, depuis une connexion résidentielle.

## Identification

Base du dépôt : `48218d54cb9b29aece8e07c72ed263af8c68c306` (branche `claude/skill-project-review-n8gu34`). Environnement : Claude Code (application de bureau, macOS), agent à contexte neuf ; outils : lecteur web, recherche web, curl et navigateur intégré. Modèle hérité de la session, sans identifiant exact enregistré par les outils de l'exécution.

L'exécutant a reçu une copie du dépôt **sans** `tests/`, `CHANGELOG.md`, `VALIDATION.md` ni `RELEASE.md` (les deux premiers mentionnent des éléments du corrigé), ainsi que la consigne seule. Il n'avait ni ce protocole, ni la grille, ni les résultats antérieurs.

Empreintes SHA-256 des consignes avant exécution (inchangées après) :

- `SKILL.md` : `c730fc17b8d970c7c04081fa6db395256d114925bcb2ab4798ea57cd7ebd180c`
- `references/eur-lex-legislation.md` : `62f4d977e08d8b6e0900d5aa7a7e4850ccc9cd5d0a650ee0c8f41ef968306b3c`
- `references/cjue.md` : `7ab06e0f352222bea33564d93d430c1baadcb72c3f6b5c71c49397268a5e9466`
- `schemas/citation-record.md` : `ccba52b9815e71ba1773935b48030474b2f989cdb90ad763fb2d2b92d4a5c685`
- consigne (lignes 3 et suivantes de `benchmark-v0.4-eu-revised.md`) : `c4e30fb68bf6b59808967636f3d0aa6db487413640dff06a47e43800698c0428`

Sorties originales, conservées sans réécriture :

- [first-response.md](first-response.md) : `a77c52e549006ee98c8cfe29378a112a8c61a1903413f48e5b6c45b1470cb25b`
- [traces.md](traces.md) : `764154f7f326b5902daced4c414b5c75d90da60a3d85fdf18329c7704181afe6`

## Comparaison avec la grille

Grille : [eu-v04-replay/protocol.md](../eu-v04-replay/protocol.md).

| Cas | Attendu | Observé | Résultat |
|---|---|---|---|
| T54 | Deux publications correctes ; pas de page exigée après 2023 | Deux notices EUR-Lex ouvertes ; aucun élément essentiel manquant ; aucune page exigée pour 2024/1689 | PASS |
| T55 | A : pas d'anomalie documentaire automatique ; B : omission éditoriale sans confusion sur l'acte | A vérifié, harmonisation seulement suggérée ; B : numéro manquant après « JO L » signalé, identité intacte | PASS |
| T56 | Décision ByteDance du 5 septembre 2023 ; annonce du 6 septembre correcte | A corrigée au 5 septembre ; B vérifiée | PASS — date établie par l'intitulé officiel du résumé au JO C, texte intégral non ouvert (limite déclarée) |
| T57 | Habilitation 40(13), accès 40(4), conditions 40(8), § 12 incorrect | Visa (§ 13) et article premier (§ 4) lus ; § 12 écarté et motivé | PASS — le § 8 n'est mentionné qu'incidemment, pas identifié comme siège des conditions |
| T58 | Référence correcte avec titre abrégé | Vérifiée ; titre abrégé non traité comme erreur | PASS |
| T59 | ECLI fourni = conclusions Rantos (20 septembre 2022) ; arrêt `ECLI:EU:C:2023:537` ; pas de fusion | Exactement ; documents distingués | PASS |
| T60 | Adoption 11 septembre 2025, v1.1 de consultation, clôture ≠ finalisation, preuve directe | Page de titre et historique du PDF officiel lus ; v2.0 mentionnée sans substitution | PASS |

Aucune invention d'identifiant, aucune sur-vérification, aucune fusion documentaire. Les échecs de curl vers EUR-Lex et InfoCuria et un délai dépassé sur EUR-Lex sont qualifiés d'échecs techniques.

## Observations

- Les URL EUR-Lex ont été formées à partir des numéros CELEX déduits des références citées, sans passer par une recherche. Aucune n'a conduit à une conclusion erronée, mais `SKILL.md` ne dit pas si cette pratique relève de la « reconstruction d'URL » interdite. À clarifier.
- EUR-Lex et InfoCuria renvoient des pages vides à curl et au lecteur web ; ils n'ont été lisibles qu'avec un navigateur réel. Une indication de repli dans `references/eur-lex-legislation.md` et `references/cjue.md` éviterait des essais inutiles.
- Le PDF du CEPD a été lu par une extraction rudimentaire ; l'ouverture dans le navigateur a déclenché un téléchargement.
- Préparation : `CHANGELOG.md` et `VALIDATION.md`, à la racine du skill, contiennent des éléments du corrigé. Un exécutant qui reçoit le dépôt entier sans `tests/` y aurait accès.

## Portée

Sept cas publics, un seul passage, coordinateur connaissant le corrigé. Ce rejeu montre que la version allégée conserve, en recherche réelle, les comportements attendus sur ces cas. Il ne constitue ni une certification, ni un taux de fiabilité, ni une comparaison avec une exécution sans skill.
