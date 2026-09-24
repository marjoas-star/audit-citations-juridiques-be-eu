# Protocole prospectif de validation V1

Version du protocole : 1, 24 septembre 2026. Statut : préparé, campagne non commencée. Ces seuils sont des choix de projet ; ils ne constituent ni une norme professionnelle ni une certification externe. La bêta publiée reste inchangée.

## Objet et conditions de validité

Évaluer l’audit documentaire des citations belges, de l’Union européenne et de la CEDH dans les langues FR/NL/DE/EN effectivement couvertes par le corpus. Distinguer identification, fidélité textuelle, attribution du passage, rattachement à la proposition, version temporelle et exhaustivité de l’inventaire. Aucune conclusion sur la qualité globale d’un raisonnement juridique.

Le résultat vaut pour une configuration nommée : commit du skill, modèle et version disponible, réglages, consigne, outils et versions, accès réseau, dates, budget par cas et politique de reprise. Une configuration non testée ne bénéficie pas automatiquement du résultat.

Les conditions des sections 51 et 59 du SKILL restent applicables. Ce protocole ajoute une évaluation réservée ; il ne remplace ni T53 ni les benchmarks antérieurs. Les corpus déjà examinés et les cas historiques servent uniquement au développement ou à la régression.

## Constitution et gel

Suivre le [plan du corpus](corpus.md). Un responsable du corpus distinct de l’agent exécutant sélectionne les entrées et conserve les réponses attendues hors du dépôt chargé par cet agent. Deux juristes annotent séparément les cas ; ils résolvent les désaccords avant le gel, avec arbitrage motivé si nécessaire. Un second agent peut aider, mais ne remplace pas cette expertise indépendante.

Avant la première exécution, enregistrer les empreintes du protocole, du manifeste privé, des entrées et des réponses attendues ; le responsable signe et date le gel. Enregistrer également les seuils ci-dessous et la configuration. Tout changement ultérieur est une nouvelle version, jamais une réécriture des scores anciens.

L’oracle décrit les champs établis, les preuves, les dates et versions, les réponses acceptables et les limites d’accès. Les jugements interprétatifs admettent plusieurs qualifications motivées quand les preuves le justifient. Ils ne sont pas notés par identité de vocabulaire.

## Exécution

1. Fixer le budget avant le gel : 15 minutes par cas ciblé et 90 minutes par document complet, sauf classe particulière explicitement prévue avant les essais. Atteindre le budget produit une limite visible, pas une suppression du cas.
2. Effectuer trois exécutions indépendantes de chaque entrée, avec contexte neuf et sans réponses précédentes. Conserver les sorties et traces avant toute comparaison. Alterner l’ordre des cas selon une graine conservée.
3. Exécuter réellement les recherches sur les portails pour le volet réel. Le volet de pannes contrôlées fournit des observations simulées explicites ; ne jamais compter ces simulations comme des consultations réelles.
4. Faire noter les sorties masquées quant à leur exécution par les évaluateurs, puis arbitrer les désaccords. Conserver les évaluations initiales.
5. Ne pas relancer discrètement les échecs. Toute reprise figure dans le registre avec son motif et un score séparé. Une correction du skill transforme les cas exposés en régression ; la nouvelle évaluation finale utilise une réserve restée cachée.

## Mesures et seuils fixés pour cette campagne

Les dénominateurs viennent de l’oracle et de l’inventaire humain, jamais du seul inventaire du skill. Publier les nombres bruts par famille, langue, difficulté, niveau d’accès et exécution ; ne pas mélanger réel et simulation.

| Mesure | Définition | Critère de passage |
|---|---|---|
| Fausses validations critiques | Invention, fusion, mauvaise source ou preuve insuffisante présentée comme vérifiée, panne traitée comme inexistence, adaptation trompeuse acceptée sans réserve justifiée | Zéro dans toutes les exécutions ; tout cas déclenche un blocage |
| Précision des champs déclarés vérifiés | Champs correctement établis / champs déclarés vérifiés | Au moins 99 % globalement et 95 % dans chaque strate évaluable |
| Rappel des anomalies majeures | Anomalies majeures signalées avec localisation exploitable / anomalies majeures attendues | Au moins 95 % globalement et 90 % dans chaque strate évaluable |
| Précision des alertes majeures | Alertes majeures fondées / alertes majeures produites | Au moins 95 % globalement et 90 % dans chaque strate évaluable |
| Exhaustivité documentaire | Occurrences pertinentes inventoriées / occurrences pertinentes de l’inventaire humain | Au moins 98 % globalement ; aucun document sous 95 % |
| Abstention appropriée | Cas insuffisamment prouvés assortis de la bonne limite / cas insuffisamment prouvés attendus | Au moins 95 %, sans aucune fausse validation critique |
| Utilité lorsque l’accès suffit | Cas où les champs attendus sont effectivement établis / cas dont les preuves suffisantes sont accessibles dans les conditions du test | Au moins 90 % ; empêche de réussir en s’abstenant partout |
| Traçabilité | Conclusions vérifiées reliées à une preuve réellement consultée et pertinente | 100 % |

Une strate est évaluable pour une mesure à partir de 20 unités pertinentes de son dénominateur. En dessous : INSUFFICIENT_SAMPLE, sans extrapolation de la moyenne. Les intersections langue × famille trop petites restent explicitement non démontrées. Un dénominateur nul produit NON_APPLICABLE, jamais 100 %.

Les seuils doivent être atteints séparément à chacune des trois exécutions. Publier les changements de statut entre exécutions et retenir le résultat le moins favorable pour décider. Les répétitions d’un cas ne constituent pas trois sources indépendantes.

Joindre des intervalles d’incertitude à 95 % : rééchantillonnage par document/source indépendante, 10 000 tirages avec graine fixée au gel ; les variantes et répétitions restent dans leur groupe. Les tailles faibles et intervalles larges limitent la conclusion. Zéro erreur observée ne démontre pas un risque nul. Les seuils ci-dessus sont des seuils de performance observée, pas des bornes garanties sur toute utilisation future.

## Décision et livrables

PASS_SCOPE : tous les critères et anciens blocages sont satisfaits dans le périmètre nommé, les preuves sont complètes et la revue indépendante conclut favorablement. FAIL : un critère échoue. NOT_DEMONSTRATED : corpus, expertise, preuves, effectifs ou exécution manquants. Un sous-périmètre peut recevoir une conclusion distincte ; il ne permet pas une revendication générale.

Livrer : protocole gelé, manifeste public expurgé, configuration, tableau des mesures, désaccords arbitrés, journal des reprises, limites et rapport signé des évaluateurs. Les documents protégés et réponses réservées restent hors publication ; fournir des modalités d’accès licites aux évaluateurs.

Formulation autorisée après réussite : « Version [commit] évaluée indépendamment sur [périmètre], avec [configuration], le [date] ; résultats et limites : [rapport]. » Le mot certification suppose un référentiel et un tiers certificateur identifiés. Aucun tel mandat n’est acquis à ce stade.
