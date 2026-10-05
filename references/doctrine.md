# Doctrine

**Dernière révision des instructions : 5 octobre 2026**

Trois niveaux : D1 identité bibliographique, D2 localisation, D3 citation textuelle.

Sources : dépôts institutionnels, éditeurs, Crossref, KBR, bases professionnelles, bibliothèques. Pour les universitaires belges, rechercher tôt DIAL.pr, DI-fusion, ORBi, PURE, etc.

Un AAM/postprint peut vérifier les mots de l'auteur mais pas nécessairement la pagination éditeur. Open Access ne signifie pas absence de droit d'auteur ou de restrictions TDM.

Résoudre `op. cit.` et `ibid.` dans le document avant d'utiliser le web. Une absence Crossref ne prouve pas l'inexistence. ISBN, édition et DOI doivent être vérifiés, jamais devinés.

## Quand arrêter la recherche

Avant de conclure qu'une référence doctrinale n'est pas vérifiable, tenter au minimum, en consignant chaque essai comme `SEARCH_ATTEMPT` :

1. l'auteur : dépôt institutionnel ou page de l'université, annuaire ou catalogue d'autorités (KBR, BnF, VIAF, ORCID) ;
2. la revue ou l'ouvrage : sommaire du volume ou de l'année cités, sur une page publique de l'éditeur ou de la revue, ou dans un catalogue de bibliothèque ;
3. le titre : recherche de la formulation exacte dans Crossref, Google Scholar ou un moteur général, dans chaque langue plausible.

S'arrêter dès que la référence est établie, ou lorsque ces trois voies ont été tentées sans élément nouveau. Ne pas multiplier les requêtes voisines. Un accès payant non disponible est une limite, pas un résultat négatif.

**Plateformes d'éditeurs sur abonnement** (par exemple Strada lex) : ne pas les tenter, même sur leurs pages publiques ; elles exigent un compte et refusent généralement les accès automatisés. Les indiquer seulement au juriste comme lieu où vérifier lui-même, s'il y a accès. Jurisquare n'existe plus depuis 2024 (voir l'annonce de la bibliothèque de droit de la KU Leuven : https://bib.kuleuven.be/rbib/collectie/stopzetting-jurisquare) : ne pas le consulter ni le proposer.

**Contenu non lu.** Une notice d'éditeur ou de bibliothèque établit l'identité (auteur, titre, revue, année, pages) mais pas le contenu : lorsque le document attribue à l'ouvrage une proposition, une page précise ou une citation, le statut est `PARTIALLY_VERIFIED` et la fiche dit « contenu non vérifié ». Proposer alors au juriste de fournir l'extrait concerné (copie des pages ou PDF qu'il possède) pour compléter le contrôle.

## Doctrine ancienne et ouvrages numérisés

Avant de déclarer non vérifiable un ouvrage ou un article ancien (auteur classique, revue antérieure aux bases en ligne), chercher une numérisation publique :

- ouvrages belges classiques et revues belges anciennes : bibliothèque de droit de la KU Leuven (voir [recueils-numerises-kul.md](recueils-numerises-kul.md)) ; dépôts numériques des universités pour leurs propres revues ;
- ouvrages et revues étrangers du domaine public : bibliothèque numérique nationale du pays (pour la France, Gallica) ; son catalogue signale aussi des **bibliothèques partenaires**, où se trouvent parfois les éditions qu'elle n'a pas elle-même (par exemple les éditions d'un même traité numérisées par une université) ;
- une reproduction en ligne dans une revue ou un site universitaire est une source secondaire : elle peut vérifier les mots, mais la fiche dit que le recueil d'origine n'a pas été consulté.

**Méthode dans une bibliothèque numérique.** Mode texte du volume pour repérer le passage ; recherche interne au document pour obtenir la vue ; table de pagination pour passer de la page imprimée à la vue ; **image de la page** pour vérifier. Relever la page imprimée et la vue. Si le site soumet l'accès à un contrôle anti-robot, appliquer la règle 8 : s'arrêter et proposer au juriste de le valider lui-même dans le navigateur.

**Édition exacte.** Vérifier l'édition que cite le document (numéro d'édition, année, éditeur lus sur la page de titre). Une autre édition peut confirmer que l'idée est bien de l'auteur ; elle ne vérifie ni la page ni les mots, car le texte a pu être réécrit d'une édition à l'autre. Dans ce cas : D1 vérifié pour l'ouvrage, D2 et D3 non vérifiés pour l'édition citée, et la fiche nomme l'édition lue. Une réédition moderne d'un texte ancien a sa propre pagination et son propre appareil (préface, notes) protégé par le droit d'auteur.

**Citation de seconde main.** Lorsqu'un passage est cité d'après un autre auteur (« cité par », ou reprise manifeste d'une formule), vérifier l'original s'il est accessible. Écarts fréquents : formule tronquée ou un mot changé ; résumé de l'auteur intermédiaire pris pour une citation de l'auteur d'origine ; date ou page reprises d'un recueil intermédiaire ; rubrique d'une chronique citée comme un article autonome. Si l'original reste inaccessible, la fiche dit « cité d'après … ; original non consulté » : statut `PARTIALLY_VERIFIED`, et jamais de correction fondée sur la seule source intermédiaire.

**Dépôts non officiels.** Un document déposé par un particulier sur une plateforme de partage peut orienter vers un passage ; il ne vérifie rien et ne se cite pas dans le rapport comme source de vérification.

## Exprimer un doute sérieux

- **Contradiction établie** : si le sommaire complet du volume cité est accessible et ne contient pas l'article à la page indiquée (ou si cette page n'existe pas dans le volume), le statut est `NOT_FOUND_OR_CONTRADICTORY`, avec le sommaire comme preuve.
- **Sans contradiction** : si le sommaire est inaccessible, le statut reste `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES`. Les indices objectifs peuvent être énumérés de façon neutre (auteur introuvable dans les dépôts et catalogues, titre sans aucune occurrence, pagination incompatible avec la taille habituelle du volume) et assortis d'une recommandation de contrôle humain prioritaire.
- Ne jamais qualifier une référence d'« inventée » ou de « fictive » sans contradiction établie, et ne jamais prêter une intention à l'auteur du document.
