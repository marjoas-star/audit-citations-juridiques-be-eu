# T61–T70 — non-régression après les retours de bêta-test

Ces scénarios servent au développement. Leurs attendus sont publics : leur rejeu n’est pas une mesure indépendante de généralisation.

| Cas | Entrée / risque | Attendu |
|---|---|---|
| T61 | Archive normative antérieure à une modification pertinente | Contrôler version et entrée en vigueur avant alerte ; incertitude si applicabilité non établie. |
| T62 | Mots exacts, décision citée erronée | Fidélité littérale préservée ; attribution corrigée séparément. |
| T63 | Citation exacte d’une disposition abrogée | Distinguer version et fidélité ; examiner les faits et le droit transitoire. |
| T64 | Une erreur répétée et une précision facultative | Une erreur distincte ; suggestion séparée ; toutes les occurrences conservées. |
| T65 | Réexport et révision d’un ancien rapport sans heure | Date initiale préservée, heure non inventée ; révision horodatée et périmètre explicite. |
| T66 | Correction NL d’une traduction amputée | Court original probant, traduction signalée et correction NL prête à reprendre. |
| T67 | Rapport pour juriste avec codes, doublons et blancs | Prose sans codes, tableau, regroupement, couleurs avec libellés, contrôle visuel. |
| T68 | Notice accessible mais contenu payant | Métadonnées réellement lues, contenu laissé partiel ; voie de vérification humaine. |
| T69 | Travaux cités par deux décisions successives | Chaîne d’attribution complète ; source directement lue distinguée de la source initiale. |
| T70 | Retours avec profils fictifs et durées estimées | Résultats déclarés, sans présentation comme évaluations humaines indépendantes ou temps mesurés. |

Les tests automatisés associés portent sur les invariants de présentation et de datation, pas sur l’exactitude du droit ni la disponibilité des sites.
