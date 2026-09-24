# Entrées et protocole du benchmark final bêta 2

# Protocole gelé avant sorties

Version testée : main 5370a00, skill beta.2. Date : 24 septembre 2026.
Deux agents à contexte neuf pour les cas réels ; un agent réutilisé pour les simulations, avec un historique limité à un précédent contrôle documentaire sans ces entrées ni oracle. La création d’un troisième agent neuf a été refusée par la limite de tâches. Chaque demande fournit seulement le skill et son entrée. Première réponse conservée, sans correction silencieuse. Pas de comparaison sans skill : mesure d'efficacité observée, pas du gain causal dû au skill.

6 références avec recherches réelles et 8 observations simulées. CE1/CE3 proviennent de références de CONTADMI p.341-342 ; CE2 dérive de la référence du livre avec année volontairement changée de 2019 en 2018. Aucun de ces numéros ni les trois affaires UE trouvés dans tests/publication antérieurs lors de la recherche exacte. Cela ne garantit pas l'absence dans les connaissances du modèle.

Attendus à corroborer indépendamment par documents officiels pour le lot réel : CE1 identité correcte ; CE2 date 9 octobre 2019 ; CE3 identité et localisation à contrôler (ne pas valider le contenu faute de citation fournie). EU1 12 janvier 2023 arrêt ; EU2 4 mai 2023 arrêt et négation omise du dispositif ; EU3 15 décembre 2022 conclusions AG, arrêt 4 mai 2023. Ces attendus sont des hypothèses tant que les pièces officielles ne les établissent pas.

Simulations : S1 TECHNICAL_FAILURE sans inexistence ; S2 recherche réussie/transfert lecture échoué, HTML non PDF, corroboration seulement, aucun ECLI inventé ; S3 comparaison interlangue NOT_APPLICABLE_TRANSLATION et fidélité séparée ; S4 exactitude adaptée distincte d'intégrité MISLEADING ; S5 mots exacts mais mauvaise attribution de locuteur ; S6 pas de fusion arrêt/conclusions ; S7 mots vérifiables au manuscrit, page éditeur non vérifiée ; S8 attribution incertaine sans deviner.

Mesures séparées : couverture 6 références/1 citation réelle + 8 scénarios ; récupération documentaire officielle réelle /6 ; anomalies réelles attendues détectées et faux signalements ; huit décisions de prudence ; traçabilité liens observés/localisateurs ; nombre de cas limités et temps mural. Ne pas additionner ces dénominateurs en taux général de fiabilité. Succès partiel ou traces insuffisantes distingués des échecs.

Seuil avant bêta humaine accompagnée : aucun défaut critique observé (invention, sur-vérification, fusion, adaptation trompeuse acceptée), anomalies établies toutes signalées, limites explicitement conservées. V1/certification générale exclue de cette conclusion.



---

# Références à auditer

Vérifiez ces trois références. Rapport en français, Markdown uniquement pour cet essai. Conservez les références originales, les preuves, les champs contrôlés et les limites. Pas de contrôle substantif demandé.

- CE1 — C.E., 1er mars 2018, GOOSSENS, n° 240.858.
- CE2 — C.E., 9 octobre 2018, PROVINCE DE HAINAUT, n° 245.702.
- CE3 — C.E., 9 décembre 2009, DE MAN, CEDER et ANNEMANS, n° 198.769, motif 2.2.3.1.


---

# Références à auditer

Vérifiez toutes les références et citations suivantes. Rapport en français, Markdown uniquement pour cet essai, avec preuves, champs contrôlés et limites. Ne réalisez pas un avis sur le fond de l'argumentation.

- EU1 — CJUE, arrêt du 12 janvier 2023, Österreichische Post, C-154/21.
- EU2 — CJUE, arrêt du 4 mai 2023, Österreichische Post, C-300/21. Citation du dispositif : « la simple violation des dispositions de ce règlement suffit pour conférer un droit à réparation ».
- EU3 — CJUE, arrêt du 15 décembre 2022, Österreichische Datenschutzbehörde et CRIF, C-487/21.


---

# Dossier contrôlé — observations simulées

Appliquez le skill à chaque cas ci-dessous à partir de ces seules observations. Ne faites pas de recherches externes : il s'agit d'une simulation explicitement bornée. Produisez un rapport Markdown en français et conservez les statuts techniques dans une annexe. Les documents et noms X/Y sont fictifs ; on teste les décisions face aux preuves fournies.

S1. Citation « C.E., X, n° 250.123, 5 mai 2021 ». Le formulaire officiel de recherche avancée, numéro début=fin=250123, FR et NL, type arrêts, renvoie un timeout. Un moteur externe n'affiche aucun résultat. Aucun autre document obtenu.

S2. Même citation dans un dossier indépendant. Recherche officielle réussie avec un lien observé. Téléchargement HTTP 200, corps HTML : « document indisponible ». Aucun PDF reçu. Une notice universitaire confirme le numéro, le nom et la date ; aucun ECLI n'y figure.

S3. Citation française « La demande doit être rejetée », attribuée à l'arrêt Y, point 12. Le document officiel ouvert identifie exactement Y, mais son seul texte disponible est néerlandais : « Het verzoek moet worden afgewezen. » L'auteur précise « notre traduction ». Aucune version française officielle obtenue.

S4. Citation attribuée à la juridiction : « Le recours est recevable [...] ». Le texte officiel intégral au point indiqué dit : « Le recours est recevable uniquement si le requérant justifie d'un intérêt personnel et actuel. » Identité et langue françaises confirmées.

S5. Citation : « Le défendeur soutient que le recours est irrecevable. » Le texte officiel reproduit exactement ces mots dans la section « Arguments des parties ». Le document étudié présente cette phrase comme la solution retenue par la Cour. L'identité et le point sont confirmés.

S6. Une note renvoie à « CJUE, affaire C-X/24, arrêt du 10 février 2025 ». Le seul document officiel ouvert porte cet exact numéro et cette date, mais son en-tête est « CONCLUSIONS DE L'AVOCAT GÉNÉRAL ». Aucun arrêt obtenu.

S7. Une note doctrinale cite la page 214 de la version éditeur et contient la citation « La compétence ne se présume pas ». Un manuscrit accepté de l'auteur, identifié dans son dépôt universitaire, contient exactement cette phrase à sa page 8. La pagination de la version éditeur n'est pas accessible.

S8. Dans un même extrait, note 1 : « Arrêt Alpha, puis arrêt Bêta ». Note 2 : « Précité, point 7 ». Aucune autre indication ne permet de choisir entre Alpha et Bêta. Aucun texte externe fourni.


## Conservation des premières réponses

Les réponses intégrales et traces sont conservées dans le dossier de travail privé. Les PDF ne sont pas redistribués. Empreintes SHA-256 des réponses gelées :

- `outputs/ce/first-response.md` : `9dc0ad91053798517c258102350121252a43bd6fc458832ec2f91f7d8df52e03`
- `outputs/eu/premiere-reponse.md` : `8d59a5cba42a83a1f5e229d75b70376ca7d76d8388a94129ab23e6002b45367e`
- `outputs/controlled/first-response.md` : `35729f927352e87799f5604fcfaac98b472c340ce02a2bd3280aa046e7c5ecca`

[Résultats et limites](../results/benchmark-final-beta2.md). Les résultats ne mesurent ni un gain par rapport à une exécution sans skill, ni une fiabilité générale. Les sources officielles et les copies secondaires restent distinguées.
