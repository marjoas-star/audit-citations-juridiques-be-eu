# Validation publique — 0.9.0-rc.1

26 septembre 2026. Version candidate : les essais de stabilité qui conditionnent la 1.0 (non-régression rejouée deux fois, documents réels, formats figés, essai public) sont à exécuter sur cette version ; leurs résultats seront consignés ici. Générateur : 38 tests automatisés, dont la présentation unique d'une référence corrigée, l'absence de preuve répétée et le lien de retour dans la langue du rapport. Rapports du bêta-test régénérés avec la nouvelle mise en page : B 14 → 11 pages, D 11 → 9, E 7 → 6, contenu inchangé.

## Historique — 0.7.0-beta.1

25 septembre 2026. Aucune certification générale ni taux de fiabilité global n'est revendiqué.

- **Bêta-test v2 dans Claude Cowork** (application de bureau, navigateur intégré), sur la version 0.6.0-beta.1 : cinq extraits réels préparés avec corrigé, dont quatre passés à l'aveugle dans des tâches neuves. 22 erreurs introduites sur 22 détectées, aucune fausse alerte de fond ; les sources bloquées depuis le cloud (Conseil d'État, Justel, EUR-Lex, Cour constitutionnelle) ont toutes été consultées. Les évaluations détaillées sont conservées dans le dossier de travail du coordinateur.
- **Régressions relevées** (référence fantôme trop prudente, version non applicable qualifiée d'altération, date juridique, inventaire incomplet, cohérence des compteurs, longueur) : règles corrigées, puis **rejeu à l'aveugle des extraits B et D** en local : 6/6 erreurs dans chacun, régressions levées ; longueur encore à réduire (budget de mots ajouté).
- **Générateur** : 35 tests automatisés, dont le rendu en quatre langues et le contrôle des chiffres de la synthèse.

Limites : un passage par extrait, coordinateur auteur des corrigés, deux écarts de procédure déclarés par les agents (recherche fondée sur la mémoire, requête déguisée en navigateur) sans effet sur les conclusions.

## Historique — 0.6.0-beta.1

25 septembre 2026. Aucune certification générale ni taux de fiabilité global n'est revendiqué. Essais de cette version, avec premières réponses, empreintes et comparaisons conservées :

- **Rejeu européen T54–T60 en recherche réelle**, exécuté depuis une connexion résidentielle : sept cas conformes à la grille ([résultats](tests/results/eu-v05-local-replay/README.md)). Depuis un environnement cloud, les sites officiels refusaient les connexions : échec technique documenté, non compté comme résultat.
- **Note piégée à six références** (bon article, mauvais ECLI, mauvaise disposition, citation altérée, doctrine introuvable) : grille satisfaite, un écart de procédure déclaré ([résultats](tests/results/note-piegee-replay/README.md)).
- **Expérience utilisateur** : sans accès au web, refus clair de commencer ; avec accès, message de départ, point d'étape et restitution en langage courant ([résultats](tests/results/ux-acces-replay/README.md)).
- **Rejeux simulés** ELLIPSIS E1–E3 et N–Q après allègement de `SKILL.md` : invariants satisfaits, sans recherche réelle ([résultats](tests/results/skill-allege-replay/README.md)).
- **31 tests automatisés** du générateur de rapport (présentation et cohérence, pas validité juridique).

Limites : un passage par cas, coordinateur auteur des grilles, cas publics. Chaque rejeu a révélé des ambiguïtés, corrigées ensuite dans cette version sans être toutes rejouées. La compréhension par des juristes réels reste à évaluer en bêta-test.

## Historique — 0.5.0-beta.3

25 septembre 2026. Révision après retours de bêta-test : voir [les résultats et leurs limites](tests/results/beta3-revision.md). Les résultats historiques ci-dessous restent conservés. Aucune certification générale ni taux de fiabilité global n’est revendiqué.

## Historique — 0.5.0-beta.2

24 septembre 2026. **Bêta expérimentale ; validation générale V1 non démontrée.** Cette note est une synthèse des essais réalisés, pas une certification ni une reproduction des documents de travail.

## Ce qui a été exécuté

- 57 cas principaux ont reçu une application : 16 avec recherches réelles et 41 sur observations simulées. Les entrées simulées étaient parfois abrégées ; elles ne prouvent pas les recherches correspondantes. Dans cette campagne : 10 cas réels satisfaisants dans le périmètre contrôlé, 6 limités, 40 simulations satisfaisantes et 1 désaccord d’oracle. Aucun taux global de fiabilité n’en est tiré.
- Deux recherches exactes officielles du Conseil d’État, arrêts 247602 (20 mai 2020) et 230687 (27 mars 2015), ont abouti à leurs PDF : identité et passages pertinents lus, aucune URL/ECLI reconstruite. Point d’entrée : [recherche avancée officielle](https://www.raadvst-consetat.be/?lang=fr&page=caselaw_page4). Le [protocole T53](tests/cases/benchmark-v0.3-integration.md) décrit la répétition.
- Neuf variantes de panne, résultat nul, mauvais document, langues et couverture ont été appliquées en simulation ; elles ne constituent pas des requêtes réellement exécutées sur le service.
- Un fichier complet de deux pages a été audité : 15 expressions externes, 4 sources uniques, 5 renvois internes, 1 titre normatif cité. Les 4 sources et 5 renvois ont été contrôlés dans les champs visés. La première passe avait omis de chercher quatre cibles dans les autres extraits disponibles ; après correction du skill, ces quatre cibles ont été trouvées. La première réponse est conservée dans le dossier de travail.
- Deux fixtures de l’article 4(13) du RGPD ont été comparées aux textes HTML officiels NL/DE : mots concordants, guillemets internes absents des fixtures ; différence mineure signalée, sans comparaison française de remplacement.
- Le scan d’une table historique KU Leuven corrobore Agimont 3957 du 7 janvier 1955. Le texte intégral de cet arrêt n’a pas été obtenu : la table ne vérifie ni ses mots ni son dispositif.

## Compléments avant publication

La fiche officielle de la directive 2011/92/UE a été ouverte puis son lien de consolidation suivi : document 02011L0092-20140515, version 15 mai 2014. L’avertissement documentaire sans effet juridique a été lu. [Consolidation effectivement consultée](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02011L0092-20140515). Cette opération complète le contrôle de version absent du premier parcours.

Le texte néerlandais de Kraaijeveld a été ouvert depuis la liste des langues officielle : affaire C-72/95, arrêt du 24 octobre 1996, ECLI:EU:C:1996:404, CELEX61995CJ0072. [Document consulté](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:61995CJ0072). Aucune citation littérale n’avait été fournie dans ce cas : aucun EXACT n’est revendiqué.

Le désaccord sur l’ellipse « en l’indication, » a conduit à un [nouveau protocole prospectif](tests/cases/ellipsis.md), avec trois entrées et une [revue par invariants](tests/results/ellipsis-review.md). Il n’annule pas le résultat historique contesté. La grammaire défectueuse et la suppression sont vérifiables ; le degré de déformation doit être motivé.

## Audit complémentaire d’un extrait long

Un fichier complet de 16 pages, comprenant 42 notes, a fait l’objet d’une lecture intégrale de son extraction textuelle : 101 occurrences groupées par localisateur, 30 sources ou ensembles de sources et 2 renvois internes résolus. Chaque source a reçu un résultat ou une limite : 5 VERIFIED, 3 VERIFIED_WITH_ANOMALY, 17 PARTIALLY_VERIFIED et 5 NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES. Ces nombres ne signifient donc pas que les 30 sources sont intégralement vérifiées.

Dix segments ont un registre de citation : un contrôle terminologique et neuf comparaisons, dont cinq EXACT, trois MINOR_DEVIATION et une INEXACT. Une comparaison repose sur une reproduction secondaire ; une autre ne vérifie que la version actuelle d’un texte, sans établir son état historique. Le rapport distingue 10 anomalies ou réserves établies au niveau de preuve déclaré et 3 points corroborés restant à confirmer. Cet essai a notamment éprouvé les erreurs de renvoi, de titre et les omissions dans les citations. Il ne couvre pas l’ouvrage entier et ne démontre aucun taux général de fiabilité. Les pièces et journaux détaillés restent dans le dossier de travail privé.

## Limites et reproductibilité

Les références doctrinales peuvent être identifiées dans une notice ou un manuscrit sans que la pagination éditeur soit vérifiée. Un texte ancien inaccessible n’est pas réputé inexistant. Une réussite du formulaire dans cet environnement ne garantit ni toute la collection ni toutes les langues. Les interprétations d’ellipses ne sont pas des verdicts sur l’intention d’un auteur.

Les protocoles sont descriptifs. Le paquet ne fournit pas de moteur d’audit automatique ni de suite attestant mécaniquement la justesse juridique. Les vérifications de frontmatter, liens et archive sont des contrôles de conditionnement. Rejouer les cas affectés en conservant entrées, réponses, observations et comparaison séparées.

Les livres, PDF officiels, captures et journaux bruts ne sont pas redistribués. Le dépôt publie les règles, les protocoles synthétiques et cette synthèse de résultats. La disponibilité des sources peut changer ; conserver la date et les limites de chaque nouvel audit.

## Compléments de la bêta 2

Dix recherches numériques officielles supplémentaires ont abouti à des PDF FR/NL, téléchargés et ouverts localement après l’échec d’autres clients. Les essais distinguent recherche, transfert et lecture ; aucun schéma d’URL n’a été reconstruit. Un lien de juriDict FR a livré un texte NL, et un lien récent une page HTML en HTTP 200 : la langue et le contenu reçu sont désormais contrôlés explicitement. Les scénarios T53-R décrivent les comportements à rejouer ; ils ne sont pas présentés comme huit exécutions indépendantes.

Le générateur français a passé cinq tests : rejet des preuves manquantes pour une référence vérifiée, identifiants dupliqués, comptage distinct des sources et occurrences, contrôle distinct des traductions, conservation d’une fiche longue à travers la pagination. Un rapport pilote de six pages a été inspecté visuellement. Ces contrôles portent sur la présentation et la cohérence, pas sur la validité juridique. Le [protocole V1](tests/validation-v1/protocole.md) reste prospectif ; la validation humaine indépendante n’est pas acquise.

## Dernier benchmark avant bêta-tests humains

Un [benchmark complémentaire](tests/results/benchmark-final-beta2.md), avec [entrées et protocole](tests/cases/benchmark-final-beta2.md), a porté sur six références réelles et huit simulations. Les trois anomalies introduites ont été détectées. Cinq références ont été vérifiées directement dans des documents officiels ; une reste partielle sur copie secondaire après résultat officiel nul. Les huit invariants simulés sont satisfaits. Aucun défaut critique observé dans cette passe ; aucun taux général de fiabilité déduit. Bêta-tests accompagnés recommandés, validation V1 toujours non démontrée.

## Rejeu européen après revue — 25 septembre 2026

Sept cas T54–T60 précisés et rejoués sur les sources accessibles donnent sept résultats satisfaisants dans leur périmètre, avec premières réponses et traces conservées. Résumés officiels et métadonnées restent distingués des textes intégraux. Ces nouveaux résultats ne certifient pas rétroactivement les scores déclarés dans le dossier reçu. Voir le [rapport du rejeu](tests/results/benchmark-v0.4-replay.md). Les instructions évoluent dans la branche principale ; l’archive beta.2 reste inchangée et la validation générale V1 non démontrée.
