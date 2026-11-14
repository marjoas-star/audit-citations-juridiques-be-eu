# Conseil d'État de Belgique — jurisprudence

**Dernière révision des instructions : 14 novembre 2026** (refonte du site officiel constatée à cette date)

## 1. Objet

Ce module décrit la vérification des arrêts et ordonnances de non-admission de la section du contentieux administratif du Conseil d'État de Belgique, ainsi que l'usage de juriDict et des recueils historiques.

## 2. Sources officielles

Source primaire moderne : site officiel du Conseil d'État de Belgique, rubrique **Arrêts > Recherche dans les arrêts**. Le site a été refondu à l'automne 2026 ; ce module décrit l'interface observée le 14 novembre 2026. Les ordonnances de cassation et les avis de la section de législation ont chacun leur propre recherche (section 9.1).

Le site annonce :

- tous les arrêts depuis septembre 1994 et toutes les ordonnances de non-admission ;
- pour le contentieux des étrangers, une publication systématique depuis juin 2018 seulement ; auparavant, seules les décisions présentant un intérêt pour la jurisprudence ou la recherche juridique étaient publiées ;
- la publication dans la langue du prononcé ;
- la pseudonymisation de tous les arrêts et ordonnances depuis février 2024 (section 6.1).

### 2.1. La recherche dans les arrêts

L'ancienne « Recherche avancée » n'existe plus : il n'y a plus de champs `Numéro début`, `Numéro fin`, `Numéro de rôle`, `Parties`, `Décision` ni de date exacte. L'interface comprend :

- un champ unique de recherche **dans le texte** (« Chercher un arrêt ») ;
- quatre filtres : **Année**, **Langue**, **Chambre**, **Matière** ;
- un tri par pertinence ou par date ;
- dix résultats par page, sous forme de fiches intitulées « Arrêt 247.602 », avec la date, la chambre, le numéro de rôle, le début des parties ou la matière, et un lien vers le PDF.

Syntaxe indiquée par l'aide du site : plusieurs mots = tous requis ; expression exacte entre guillemets ; `|` = l'un ou l'autre ; `-mot` = exclusion ; `perm*` = début de mot.

### 2.2. L'index de recherche est moins complet que la collection

Constats du 14 novembre 2026 :

- le filtre Année compte 30 documents pour 1994, 472 pour 1995 et 1.932 pour 1996, bien moins que les arrêts prononcés ;
- l'arrêt n° 50.000 du 28 octobre 1994 n'est trouvé ni par son numéro ni par le nom d'une partie, alors que son PDF est servi par le site à son adresse directe (section 4.1).

Conséquence : **« 0 résultat » ou l'absence de la fiche attendue ne prouve pas que l'arrêt est absent de la collection**, surtout pour les années 1994 à 1996.
## 3. Règle fondamentale

> **Le numéro permet de chercher ; le document officiel permet de vérifier ; juriDict permet de découvrir.**

Une occurrence dans un moteur de recherche, un snippet, une référence doctrinale ou un point de droit juriDict ne remplace pas le document officiel intégral lorsqu'il est accessible.

## 4. Récupération par numéro exact — EXACT_DECISION_NUMBER_LOOKUP

Lorsqu'un numéro exact d'arrêt est connu :

1. saisir le numéro seul dans le champ de la recherche officielle dans les arrêts, sans filtre ; l'écriture avec ou sans point (`247602`, `247.602`) a donné les mêmes résultats ;
2. repérer la fiche dont **le titre** porte ce numéro (« Arrêt 247.602 ») ; ne jamais retenir le premier résultat sans lire son titre (section 4.0) ;
3. si aucune fiche ne porte ce numéro, essayer l'adresse officielle directe (section 4.1) avant de conclure ;
4. ne jamais construire un ECLI à partir de la date, du numéro ou d'un modèle supposé ;
5. ouvrir le document officiel ;
6. vérifier séparément, **dans le document** :
   - nature du document ;
   - numéro ;
   - date ;
   - parties (section 6.1) ;
   - langue ;
   - numéro de rôle si pertinent ;
   - passage cité ;
7. ne relever un ECLI que s'il est effectivement imprimé dans le document ou affiché par une source suffisamment forte (section 4.2) ;
8. conserver le niveau de preuve par champ.

### 4.0. Lire la liste de résultats

La recherche porte sur le texte des arrêts : un numéro saisi ramène aussi les arrêts qui **citent** ce numéro et ceux dont le **numéro de rôle** le contient. Exemples du 14 novembre 2026 : `247602` donne l'arrêt n° 247.602 et l'arrêt n° 258.417, rendu dans la même affaire ; `230687` donne l'arrêt n° 230.687 et deux arrêts du rôle A. 230.687. Un numéro rond ou court donne des centaines de résultats (`50000` : 608).

- Identifier l'arrêt par le titre de la fiche, puis par l'en-tête du PDF ; la date et le numéro de rôle de la fiche servent de premier contrôle.
- Chercher d'abord le numéro seul. Les mots ajoutés et les filtres se combinent par ET : une erreur dans la citation masquerait le bon résultat.
- Si les résultats sont trop nombreux, restreindre par le filtre Année tiré de la citation. Si la fiche n'apparaît toujours pas, retirer ce filtre et essayer les années voisines avant de passer à l'adresse directe : la date citée peut être fausse.
- Le filtre Langue porte sur la langue du document : `Français` masque un arrêt néerlandais (l'arrêt n° 268.329, néerlandais, donne 0 résultat avec ce filtre). Ne pas l'utiliser pour identifier un arrêt ; s'il est utilisé, le consigner.
- Un arrêt ancien publié avec sa traduction apparaît sur deux fiches (« En cause » et « In zake ») ; les deux fiches peuvent renvoyer à la même adresse. Contrôler la langue du PDF reçu (section 7).
- L'adresse de la page de résultats (`/fr/recherche/arrets?query=…`, avec `year`, `language`, `chambre`, `category`, `sort`, `page`) reflète la recherche effectuée : elle peut être conservée dans les traces et réutilisée avec un autre numéro **cité dans le document**.

### 4.1. Adresse officielle directe d'un arrêt

Sur le nouveau site, chaque arrêt a une adresse stable, celle que portent les fiches de résultats et les fiches juriDict :

```text
https://www.raadvst-consetat.be/arrets/<numéro sans point>     texte français
https://www.raadvst-consetat.be/arresten/<numéro sans point>   texte néerlandais
```

Pour un arrêt rendu dans une seule langue, les deux adresses livrent le même PDF. Pour un arrêt publié avec sa traduction (constaté sur les n° 70.412 et 92.340), chacune livre un texte différent, dont l'un porte en tête « Texte français » ou « Nederlandse tekst » avec la mention du titre VI, chapitre II, des lois coordonnées : c'est la traduction.

Règle :

- la recherche reste la voie primaire ; l'adresse directe n'est essayée qu'après une recherche par numéro qui n'a pas montré la fiche attendue, ou lorsque la recherche est en panne ;
- **l'adresse n'est jamais une preuve** : seul le PDF ouvert, dont l'en-tête porte le numéro et la date, établit l'existence et l'identité de l'arrêt ;
- une réponse 404 à cette adresse ne prouve pas l'inexistence (constatée pour le n° 61.000, cité par l'ancienne documentation de juriDict) : consigner l'échec et poursuivre par juriDict ou une corroboration ;
- consigner dans les traces que le document a été obtenu par l'adresse directe, après quelle recherche ;
- cette tolérance ne vaut que pour ces deux schémas, observés sur le site officiel. Aucune autre adresse n'est construite, et jamais un ECLI.

### 4.2. ECLI

Les arrêts récents portent leur ECLI en pied de chaque page du PDF (constaté sur l'arrêt n° 268.329 du 12 novembre 2026 : `ECLI:BE:RVSCE:2026:ARR.268.329`). Les arrêts n° 247.602 (2020) et n° 50.000 (1994) n'en portent pas ; ni les fiches de résultats ni les fiches juriDict n'en affichent. Relever l'ECLI tel qu'il est imprimé dans le PDF ; ne pas en composer un pour un arrêt qui n'en porte pas.

### 4.3. Récupérer et lire le document

Le lien d'une fiche ouvre directement le PDF. Si le lecteur intégré échoue ou empêche l'extraction, télécharger le lien observé avec un client standard et lire le PDF localement ; `curl --fail --location` a fonctionné le 14 novembre 2026 pour la recherche comme pour les PDF, ce qui ne garantit pas tous les environnements. Ne pas contourner un contrôle d'accès ni un CAPTCHA. Conserver l'échec du premier client et le résultat du repli.

Un statut HTTP 200 ne suffit pas : vérifier la signature PDF, l'ouverture par un lecteur, le nombre de pages et l'identité du document. Une page HTML servie en 200 reste un échec de récupération ; c'est le cas des anciennes adresses `?page=…`, qui renvoient désormais la page d'accueil (section 9). Lire l'en-tête, la langue, les mentions de traduction et de rectification avant le passage cité. Chercher ensuite le passage dans le texte extrait et rendre visuellement les pages pertinentes si l'extraction est douteuse. Ne pas transformer des espaces parasites d'extraction en fautes de l'auteur.

Pour un lot, conserver les liens observés dans un manifeste, limiter les téléchargements simultanés et réutiliser les fichiers déjà obtenus. Un seul changement de client standard suffit pour tester un repli ; en cas d'échec persistant, consigner la limite et passer à une voie de corroboration. Séparer recherche, téléchargement et lecture dans les traces.

### 4.4. Échec de la recherche

Si la recherche officielle ne peut pas être pilotée, renvoie une erreur, un timeout ou une réponse techniquement inexploitable :

```text
TECHNICAL_FAILURE
```

Ne jamais convertir cet échec en :

```text
NO_RESULT
NOT_FOUND
```

L'absence d'un résultat dans Google/Bing ou un autre moteur général ne peut pas davantage établir l'inexistence de l'arrêt. Il en va de même d'un « 0 résultat » de la recherche officielle elle-même (section 2.2) : essayer l'adresse directe, puis juriDict, avant toute conclusion ; à défaut de document, le statut est `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES`, pas une inexistence.

### 4.5. Arrêt postérieur à septembre 1994

Si l'arrêt est postérieur à septembre 1994 et ne relève pas d'une exception de publication connue, une impossibilité persistante d'accéder au document doit être décrite comme une limitation technique de l'audit.

Le statut peut rester `PARTIALLY_VERIFIED` ou `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES` selon les autres preuves obtenues.

## 5. juriDict

juriDict donne accès au contenu juridique de la jurisprudence et renvoie à des arrêts et ordonnances de non-admission.

La structure est divisée en branches francophone et néerlandophone.

### 5.1. Accès et couverture

Adresse : `/fr/banques-de-donnees/juridict` (néerlandais : `/nl/databanken/juridict`). Sans préférence de langue enregistrée, l'adresse française a renvoyé l'interface néerlandaise : contrôler la langue de l'interface reçue avant de lire les rubriques.

Le champ simple accepte des mots, un numéro d'arrêt ou une date. La recherche avancée offre : Requérant, Décision, Chambre, N° d'arrêt, dates Du/Au, Domaine, Type (arrêt, ordonnance, question préjudicielle, assemblée générale). Le site précise que les arrêts dépersonnalisés et les ordonnances ne sont pas cherchés par nom. Les résultats sont des **points de droit** ; chacun renvoie au PDF de l'arrêt par son adresse directe (section 4.1). juriDict peut ainsi retrouver par numéro un arrêt que la recherche plein texte ne montre pas, dans les limites de sa couverture.

Les présentations française et néerlandaise, relues le 14 novembre 2026, annoncent chacune pour sa structure un accès systématique aux arrêts depuis le 1er janvier 2000, et depuis juin 2018 pour le contentieux des étrangers ; la jurisprudence plus ancienne est reprise de manière sélective ; les arrêts de procédure sont exclus ; les ordonnances de non-admission ne figurent que si elles présentent un intérêt. (L'ancienne documentation française annonçait le n° 61.000 du 17 juillet 1996 comme point de départ : cette indication n'est plus affichée.)

Ces indications concernent juriDict, pas la collection générale des PDF depuis septembre 1994.

### 5.2. Taxonomies FR/NL

Règle impérative :

```text
juriDict FR ≠ traduction de juriDict NL
```

Ne jamais traduire un mot-clé ou une branche française en néerlandais, ou inversement, comme s'il s'agissait d'une équivalence taxonomique.

Rechercher chaque arborescence dans sa langue et comparer ensuite les décisions retrouvées.

### 5.3. Valeur probatoire

juriDict peut :

- découvrir une décision ;
- fournir un point de droit ;
- orienter la recherche ;
- corroborer certaines métadonnées.

juriDict ne doit pas être utilisé seul pour prétendre avoir contrôlé :

- le dispositif complet ;
- une citation textuelle étendue ;
- une page précise ;
- un passage omis ;
- un ECLI non affiché.

## 6. Types documentaires

Distinguer strictement :

- arrêt ;
- ordonnance de non-admission en cassation administrative ;
- avis de la section de législation ;
- document de l'auditorat ;
- point de droit / notice juriDict.

Un document de l'auditorat n'est pas une « conclusion d'avocat général ».

## 6.1. Parties et pseudonymisation

Depuis février 2024, tous les arrêts et ordonnances publiés sont pseudonymisés ; dans le contentieux des étrangers, l'identité des requérants est toujours omise (« XXXXX »), et une partie peut obtenir l'omission de son identité. Des arrêts plus anciens affichent encore les noms.

Un nom de partie cité dans le document audité mais absent du PDF publié n'est donc pas une anomalie de la citation : marquer le champ « parties » comme non vérifiable sur la version publiée, sans proposer de correction.

## 7. Langue

Conserver séparément :

```yaml
source_language:
decision_language:
translation_status:
```

Le site officiel publie les arrêts et ordonnances dans la langue où ils ont été prononcés.

Le chemin de l'adresse indique la langue demandée, pas la langue du prononcé : `/arrets/` pour le français, `/arresten/` pour le néerlandais (section 4.1). Constater la langue sur le PDF reçu. Ne jamais déclarer `EXACT` une citation française à partir d'un texte néerlandais, ni l'inverse.

Si une traduction institutionnelle existe, ne pas la présenter comme texte authentique sans base juridique spécifique.

## 8. Décisions anciennes

Pour les décisions antérieures à la collection moderne, utiliser `references/recueils-numerises-kul.md`.

Principe :

> **L'OCR sert à trouver ; le scan sert à vérifier.**

Les quelques documents antérieurs à 1994 que montre le filtre Année du site ne font pas de celui-ci une source pour cette période. Chercher l'arrêt dans le fascicule du mois de son prononcé, par son numéro. Contrôler la citation dans les **motifs** et non dans le sommaire qui précède l'arrêt : le sommaire peut en généraliser la portée. Donner la page imprimée du recueil.

Ne jamais inventer un ECLI pour une ancienne décision qui n'en possède pas ou dont l'identifiant n'a pas été vérifié.

## 9. Anciens liens et URL

Depuis la refonte (constat du 14 novembre 2026) :

- les anciennes pages `?lang=fr&page=…` (`caselaw`, `caselaw_page4`, `juridict`, aides) renvoient la **page d'accueil** avec un statut 200 : ce n'est ni la page demandée ni une preuve de quoi que ce soit ;
- un ancien lien `arr.php?nr=<numéro>` est redirigé vers `/arresten/<numéro>`, c'est-à-dire l'adresse **néerlandaise** : un arrêt francophone unilingue arrive en français, mais un arrêt publié dans les deux langues arrive en néerlandais. Contrôler la langue reçue et, au besoin, reprendre l'adresse française de la fiche de résultats ;
- les domaines `conseildetat.be` et `raadvanstate.be` affichent la même page d'accueil.

Un lien `arr.php` trouvé dans une source peut être suivi tel quel. Hors des deux schémas de la section 4.1, ne fabriquer aucune adresse à partir d'un numéro.

Une adresse, même officielle, n'est jamais une preuve d'existence documentaire : seul le document ouvert l'est.

## 9.1. Autres voies de consultation

- **Ordonnances de cassation** : recherche distincte (`/fr/recherche/ordonnances`), filtres Année et Langue, fiches « Ordonnance de cassation 16.903 », adresse `/cassations/<numéro>`. La numérotation est propre aux ordonnances : chercher un numéro dans la collection qui correspond à la nature du document cité.
- **Avis de la section de législation** : recherche distincte (`/fr/recherche/avis`), filtres Année, Chambre, Matière, Type de norme, Demandeur d'avis, Délai ; une fiche donne l'avis (`/avis/<numéro>`) et, séparément, le projet soumis (`/avis/<numéro>/projet`). Ne pas confondre les deux documents.
- **juriDict** : une recherche peut produire plusieurs points de droit pour un seul arrêt. Ne pas compter ces lignes comme autant de sources.
- **Décisions récentes** : l'ancienne liste par mois a disparu ; le tri « Les plus récents en premier » la remplace.

Pages consultées le 14 novembre 2026 : [recherche dans les arrêts](https://www.raadvst-consetat.be/fr/recherche/arrets/), [Qu'est-ce qu'un arrêt ?](https://www.raadvst-consetat.be/fr/arrets/qu-est-ce-qu-un-arret/), [Qu'est-ce que juriDict ?](https://www.raadvst-consetat.be/fr/banques-de-donnees/qu-est-ce-que-juridict/), [Wat is juriDict?](https://www.raadvst-consetat.be/nl/databanken/wat-is-juridict/), [manuel juriDict](https://www.raadvst-consetat.be/fr/publications/brochures/manuel-juridict/).

## 10. Procédure recommandée

### Cas A — numéro exact connu

```text
numéro exact
→ recherche officielle dans les arrêts (numéro seul)
→ fiche dont le titre porte le numéro
   (à défaut : adresse officielle directe, puis juriDict)
→ document officiel
→ métadonnées
→ texte
→ citation éventuelle
```

### Cas B — nom/date mais numéro inconnu

```text
nom/date
→ collection officielle et/ou juriDict
→ candidat
→ document officiel
→ vérification
```

### Cas C — décision ancienne

```text
référence historique
→ KU Leuven / recueil numérisé
→ OCR pour localisation
→ scan pour vérification
```

## 11. Statuts

- document officiel ouvert et champs correspondants : `VERIFIED` ;
- identité corroborée mais document officiel non ouvert : `PARTIALLY_VERIFIED` ;
- aucune preuve suffisante malgré les voies accessibles : `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES` ;
- erreur technique : `TECHNICAL_FAILURE` dans `SEARCH_ATTEMPT`, sans conclusion d'inexistence ;
- contradiction établie avec le document officiel : `NOT_FOUND_OR_CONTRADICTORY` ou `VERIFIED_WITH_ANOMALY` selon le cas.

## 12. Test de non-régression

Voir T53 dans `tests/cases/benchmark-v0.3-integration.md`.

Le module n'est considéré prêt pour V1 que si :

```text
COUNCIL_OF_STATE_EXACT_NUMBER_RETRIEVAL = GREEN
```

## 13. Points d'entrée officiels vérifiés (14 novembre 2026)

- Arrêts, présentation et couverture : https://www.raadvst-consetat.be/fr/arrets/
- Recherche dans les arrêts : https://www.raadvst-consetat.be/fr/recherche/arrets/ (néerlandais : https://www.raadvst-consetat.be/nl/zoeken/arresten)
- Recherche dans les ordonnances de cassation : https://www.raadvst-consetat.be/fr/recherche/ordonnances
- Recherche dans les avis : https://www.raadvst-consetat.be/fr/recherche/avis
- juriDict : https://www.raadvst-consetat.be/fr/banques-de-donnees/juridict

Si ces adresses ne répondent plus ou renvoient la page d'accueil, repartir du menu **Arrêts** de la page d'accueil et signaler au juriste que le module est à réviser.

## Traçabilité de T53

Conserver les observations brutes et la sortie réelle séparément de l'oracle. Les variantes simulées testent les décisions face aux observations fournies, pas le pilotage du site. Un succès sur un arrêt ne prouve pas la récupération générale. Un test sans sortie conservée reste `NOT_DEMONSTRATED`.

Complément de protocole : [récupération et lecture](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/blob/main/tests/cases/conseil-etat-recuperation.md).
