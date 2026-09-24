# Plan du corpus réservé V1

Statut : plan de collecte, aucun cas réservé ni oracle indépendant constitué à ce stade. Ce document ne prétend pas que les évaluateurs ont été recrutés ou que le corpus est gelé.

## Taille et couverture

Prévoir 240 cas ciblés : 180 pour l’évaluation et 60 en réserve de remplacement après exposition. Ajouter 12 documents complets pour l’évaluation et 4 documents de réserve, de 5 à 20 pages chacun. Un document complet désigne le fichier entier retenu, pas nécessairement un ouvrage entier. Les occurrences de ces documents ont un inventaire humain exhaustif ; elles ne sont pas ajoutées artificiellement au nombre des cas ciblés.

Répartition initiale des 180 cas : 30 Conseil d’État belge, 30 autres juridictions belges, 30 jurisprudence UE, 30 textes normatifs UE, 30 CEDH, 30 doctrine et autres sources belges. Réserver 45 cas par langue de citation FR/NL/DE/EN dans des combinaisons juridiquement pertinentes, sans imposer des traductions inexistantes. La sélection doit préserver la diversité des documents, auteurs, périodes et types de sources.

Composition transversale : 60 cas corrects, 60 avec anomalies documentées, 30 ambigus ou réellement inaccessibles, 30 scénarios adversariaux contrôlés. Parmi les anomalies : identifiants, dates, localisateurs, version historique, attribution, citation et adaptation. Croiser les catégories avec les familles sans sélectionner uniquement des cas faciles. Les pannes simulées restent un volet séparé du réel dans les scores.

Inclure dans le Conseil d’État : numéro exact avec date/nom discordant, panne du formulaire, résultat nul, lien observé vers un mauvais document, FR/NL, antériorité à septembre 1994, exception étrangers, limites de juriDict. Préserver la distinction recherche officielle/juriDict/moteurs externes et l’interdiction de fabriquer URL ou ECLI. Ces caractéristiques reprennent les risques connus ; les entrées concrètes doivent être nouvelles.

Le responsable ajuste avant gel les effectifs transversaux pour fournir au moins 20 unités pertinentes par strate revendiquée et mesure. Si le budget ne le permet pas, réduire explicitement le périmètre revendiqué. Les quotas globaux ne garantissent pas à eux seuls ce minimum.

## Séparation et protection

Exclure de l’évaluation réservée les ouvrages déjà utilisés, les cas T01–T57, leurs variantes, les ellipses déjà analysées et tout cas dont l’agent exécutant a vu la correction. Garder chaque document, affaire et variante dans une seule partition. L’inédit concerne l’élaboration et l’exécution du test ; il n’est pas possible de garantir l’absence des décisions publiques dans les données d’entraînement du modèle.

Conserver les entrées, sources et oracles dans un espace séparé accessible au seul responsable du corpus et aux annotateurs. Livrer à l’exécutant uniquement l’entrée nécessaire, le skill et les outils autorisés. Ne pas placer un oracle caché dans un simple sous-dossier du même espace accessible.

## Champs du manifeste privé

Pour chaque cas : case_id, partition, source_group_id, document_id, famille, langue de citation, langue de source, réel/simulé, catégorie, date juridique de référence, entrée et empreinte, source des droits d’accès, difficulté prévue, annotateurs, version de l’oracle et empreinte, date de gel. Les identités réelles et chemins privés ne figurent pas dans la version publique.

L’oracle privé contient : inventaire et localisateurs, identité attendue par champ, texte de comparaison dans la bonne langue/version, liens observés et preuves conservées, anomalies et gravité motivées, limites acceptables, qualifications alternatives recevables et arbitrage. Une absence de preuve n’est jamais complétée par une invention.

## Ordre de mise en œuvre

1. Désigner un responsable du corpus et deux juristes évaluateurs, puis convenir de leurs accès aux sources.
2. Collecter et annoter les candidats dans l’espace séparé, sans exposer la réserve à l’agent chargé du développement.
3. Dédupliquer par affaire/document, vérifier droits et quotas, puis geler le manifeste et les oracles.
4. Fixer la configuration et exécuter le [protocole](protocole.md).

La préparation autonome des documents méthodologiques est achevable maintenant. La constitution d’un oracle juridiquement indépendant exige la participation effective des évaluateurs ; une auto-évaluation du même agent ne peut en tenir lieu.
