# Rejeu européen T54–T60 — 25 septembre 2026

**Résultat : sept cas satisfaisants dans le périmètre demandé, sur recherches réelles. Aucun défaut critique observé dans cette passe. La validation générale V1 reste non démontrée.**

Ce rejeu porte sur des entrées précisées après revue des trois fichiers transmis. Il ne certifie pas rétroactivement les anciens « 7/7 PASS », dont les réponses et traces n'étaient pas fournies, ni l'audit des 17 références/familles de l'ouvrage.

## Résultats comparés au corrigé

| Cas | Attendu | Réponse et preuves obtenues | Évaluation |
|---|---|---|---|
| T54 | Publications 2019 et 2024 conformes ; pas de page de fascicule exigée après le changement du JO | JO PDF pour 2019/1024, en-tête HTML officiel pour 2024/1689 ; aucun ajout de page fictive | PASS |
| T55 | A : note libre identifiable ; B : présentation JO complète exigée | Identité préservée dans les deux cas ; omission bibliographique signalée seulement en B, avec ELI observé | PASS |
| T56 | Adoption ByteDance le 5 septembre 2023 ; annonce du 6 correcte | Résumé officiel de décision ouvert et annonce de la Commission distingués ; date de notification non inventée | PASS |
| T57 | Distinguer disposition d'accès et habilitation | PDF officiel, visa 40(13) et article 1 renvoyant à 40(4) ; mauvais §12 signalé et DSA consulté | PASS |
| T58 | Titre abrégé assumé, numéro et date corrects | Texte officiel DGA ouvert ; aucune anomalie de titre artificielle | PASS |
| T59 | ECLI des conclusions associé à tort à l'arrêt | Métadonnées InfoCuria ouvertes : arrêt 4 juillet 2023 / 2023:537 ; conclusions 20 septembre 2022 / 2022:704 ; documents non fusionnés | PASS |
| T60 | Adoption, révision et statut de consultation distincts | PDF historique version 1.1 ouvert : adoption le 11 septembre 2025, corrections le 12 septembre ; version de consultation, malgré clôture | PASS |

Le PASS concerne les champs demandés et les invariants, pas une lecture intégrale de chaque source. Pour T56, le résumé officiel suffit à la date et à l'identité contrôlées ; il n'est pas présenté comme la décision intégrale. Pour T59, les métadonnées officielles suffisent à distinguer les documents ; leurs textes n'ont pas été obtenus. Le contrôle des conditions détaillées de l'article 40(8) n'était pas demandé dans T57 et ne reçoit pas de validation distincte.

Sept cas représentent dix occurrences : deux références en T54, deux contextes en T55, deux phrases en T56 et quatre autres occurrences. Neuf sources principales sont identifiées, avec deux sources connexes de contrôle. Cinq occurrences appellent une correction, dont une éditoriale uniquement. Ces compteurs ne sont pas un taux de fiabilité.

## Pièces permettant la revue

- [Entrées effectivement données à l'exécutant](../cases/benchmark-v0.4-eu-revised.md).
- [Première réponse conservée](eu-v04-replay/first-response.md), publiée sans réécriture après comparaison.
- [Journal et preuves par champ](eu-v04-replay/traces.md).
- [Protocole et empreintes](eu-v04-replay/protocol.md).

Les huit réponses brutes du lecteur web, PDF et fichiers reçus sont conservés dans le dossier de travail privé. Leurs mentions relatives dans le rapport et le journal désignent ce dossier, pas des téléchargements publics. Les ouvrages et documents sources intégraux ne sont pas redistribués.

## Apport particulier : lignes directrices du CEPD

Le lien ancien indexé était défaillant. L'exécutant a suivi le lien actuellement affiché par la page officielle, sans déduire une URL. Le [PDF historique](https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v1_en.pdf), couverture et historique p. 1–2, distingue adoption du 11 septembre 2025 et corrections de la version 1.1 du 12 septembre 2025. L'ancien rapport validait trop globalement la date du12 sans distinguer ces événements.

Le coordinateur a obtenu séparément les mêmes éléments et suivi le lien vers le [PDF version 2.0](https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v2_en.pdf), adopté le 17 septembre 2026 après consultation (p. 1–2). Ce complément ne remplace pas la version 1.1 dans l'audit et n'est pas attribué à l'exécutant, qui a seulement relevé l'existence du lien final.

## Méthode et limites

Les consignes du skill ont été révisées avant le test, puis gelées par empreintes. Un agent à contexte neuf a reçu uniquement le skill et les entrées, sans corrigé ni fichiers du benchmark antérieur. Les critères ont été écrits avant lecture de sa réponse. Les preuves directes complémentaires du coordinateur ont été conservées séparément. Aucun résultat n'a été obtenu par injection d'observations simulées.

Le coordinateur a lu la première réponse et les traces, contrôlé les extraits bruts des publications et du PDF CEPD, et recoupé séparément les métadonnées Meta et les versions CEPD. Aucun changement de consignes ni correction de la réponse n'a eu lieu pendant ou après l'exécution pour obtenir les sept succès. Le contrôle oppose deux exécutions d'IA ; il ne remplace pas une évaluation indépendante par des juristes.

Les cas sont construits et connus du coordinateur ; ils ne constituent pas un corpus représentatif tenu secret. Aucun groupe sans skill, aucune mesure du gain causal, de coût ou de vitesse. Aucun contrôle de citation textuelle longue, de soutien juridique général ni de PDF de rapport complet dans ce rejeu. Le contrôle de structure du skill et les cinq tests existants du générateur passent séparément ; ce sont des contrôles techniques.

**Décision : intégrer les améliorations aux sources de développement et poursuivre les bêta-tests accompagnés.** L'archive beta.2 et son tag restent inchangés ; ces résultats ne constituent ni une nouvelle certification ni une publication V1.
