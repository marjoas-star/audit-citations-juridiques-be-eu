# Dernier benchmark avant les bêta-tests humains

**24 septembre 2026 — version testée : 0.5.0-beta.2, dépôt au commit 5370a00.**

**Conclusion : le skill est prêt pour des bêta-tests accompagnés, sur le périmètre éprouvé. Ce benchmark ne démontre pas une fiabilité générale ni une aptitude à remplacer la vérification du juriste.**

Le test porte sur six références avec recherches réelles et huit situations simulées. Les trois anomalies introduites dans les références réelles ont été repérées. Aucun identifiant inventé, aucune confusion documentaire acceptée et aucune citation trompeuse validée n’ont été observés dans les réponses conservées.

## Ce qui a réellement fonctionné

| Contrôle | Résultat observé |
|---|---|
| Traitement des références réelles | 6 sur 6 traitées, avec conclusion et preuves ou limites |
| Accès direct à un document officiel | 5 références sur 6 : deux au Conseil d’État, trois à la CJUE |
| Référence restante | Copie intégrale secondaire obtenue ; vérification maintenue partielle |
| Anomalies préparées | 3 sur 3 détectées : année fausse, négation supprimée, date des conclusions attribuée à l’arrêt |
| Références laissées correctes | Aucune correction injustifiée sur les trois références témoins |
| Situations simulées | 8 sur 8 satisfont les comportements attendus |
| Génération du rapport | Les 5 tests existants passent ; validation de structure du skill réussie |

Ces dénominateurs mesurent des choses différentes. Ils ne sont pas additionnés en un pourcentage de fiabilité.

## Références vérifiées sur les sites

| Cas | Entrée et résultat |
|---|---|
| CE1 | **Goossens, 240.858, 1er mars 2018** : identité confirmée dans les PDF officiels FR et NL. Leur identité commune est contrôlée ; aucune équivalence complète des versions n’est affirmée. |
| CE2 | **Province de Hainaut, 245.702, cité au 9 octobre 2018** : le PDF officiel établit le **9 octobre 2019**. Année erronée détectée. |
| CE3 | **De Man, Ceder et Annemans, 198.769, 9 décembre 2009** : recherche officielle exacte sans résultat ; copie secondaire intégrale retrouvée, avec le motif 2.2.3.1 aux pages 8–9. Le rapport conserve la vérification partielle. |
| EU1 | **Österreichische Post, C-154/21, 12 janvier 2023** : référence conforme au texte officiel. |
| EU2 | **Österreichische Post, C-300/21, 4 mai 2023** : identité conforme, mais la citation du dispositif supprimait « ne » et « pas ». Inversion du sens détectée et correction établie. |
| EU3 | **Österreichische Datenschutzbehörde et CRIF, C-487/21, présenté comme arrêt du 15 décembre 2022** : distinction correctement faite entre les conclusions de cette date et l’arrêt du **4 mai 2023**. |

Sources déterminantes : [Goossens FR](https://www.raadvst-consetat.be/Arrets/240000/800/240858f.pdf), [Goossens NL](https://www.raadvst-consetat.be/Arresten/240000/800/240858n.pdf), [Province de Hainaut](https://www.raadvst-consetat.be/Arrets/245000/700/245702.pdf), [copie secondaire de De Man](https://www.vreemdelingenrecht.be/sites/default/files/migrated/dbrechtspraak/RvS%20198.769.pdf), [C-154/21](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=ecli:ECLI:EU:C:2023:3), [C-300/21](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62021CJ0300), [C-487/21](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62021CJ0487). Les liens ont été découverts avant leur utilisation ; aucun schéma d’URL n’a été fabriqué.

Le problème de récupération au Conseil d’État est donc mieux maîtrisé : le formulaire numérique a été utilisé en premier, puis les vrais liens ont été téléchargés lorsque le lecteur web échouait. Il subsiste une limite d’accès à un arrêt de l’échantillon. Le test n’établit pas la cause de son absence des résultats officiels, ni l’exhaustivité de la collection.

## Situations contrôlées

| Situation simulée | Décision obtenue |
|---|---|
| Formulaire officiel en panne, moteur externe sans résultat | Échec technique signalé ; aucune conclusion d’inexistence |
| Lien officiel livrant du HTML en HTTP 200 | Absence de PDF reconnue ; recherche réussie distinguée de la récupération échouée |
| Citation française traduite d’un texte NL | Fidélité de traduction évaluée séparément ; pas de conformité littérale française prétendue |
| Ellipse supprimant une condition essentielle | Mots conservés distingués du sens ; adaptation jugée trompeuse |
| Argument du défendeur présenté comme solution de la Cour | Mots exacts, attribution erronée signalée |
| Conclusions d’avocat général présentées comme arrêt | Deux documents distingués, arrêt cible non vérifié |
| Phrase trouvée dans un manuscrit, page éditeur inaccessible | Mots vérifiés pour le manuscrit seulement ; page éditeur non certifiée |
| « Précité » après deux arrêts possibles | Renvoi laissé incertain, sans choix arbitraire |

Ces huit essais utilisent des observations fournies. Ils ne prouvent pas huit parcours de recherche sur Internet.

## Méthode et portée

Le protocole et les attentes ont été fixés avant la lecture des réponses. Deux agents avec contexte neuf ont exécuté les lots réels sans accès au corrigé. Un troisième agent, réutilisé après une tâche documentaire antérieure, a traité les simulations sans recevoir le corrigé. Cette dernière isolation est moins forte qu’un contexte neuf. Les premières réponses, les entrées et les traces sont conservées séparément du corrigé.

Le coordinateur a comparé les réponses aux invariants préparés, relu les documents du Conseil d’État obtenus et ouvert séparément les textes européens nécessaires à la vérification des erreurs. Il s’agit d’un contrôle entre exécutions d’IA, pas de deux évaluateurs humains indépendants. Les contrôles n’ont pas conduit à modifier les consignes ni à réécrire les premières réponses pour améliorer le score.

L’échantillon est volontairement petit et orienté vers les difficultés rencontrées. Il ne mesure pas les performances sur la doctrine payante, les textes historiques, la Cour de cassation, la Cour constitutionnelle, HUDOC, un document long, ni toutes les langues annoncées. Il n’y a pas de groupe sans skill : le gain attribuable au skill seul n’est donc pas mesuré. Le Markdown était demandé pour les essais ; aucun nouveau contrôle visuel d’un rapport PDF complet n’est revendiqué.

**Décision proposée : lancer les bêta-tests accompagnés avec les consignes déjà préparées.** Conserver l’étiquette expérimentale et demander aux juristes de comparer chaque conclusion à leurs propres sources, notamment les références laissées partiellement vérifiées. La validation générale V1 reste à établir.
