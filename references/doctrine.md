# Doctrine

**Dernière révision des instructions : 25 septembre 2026**

Trois niveaux : D1 identité bibliographique, D2 localisation, D3 citation textuelle.

Sources : dépôts institutionnels, éditeurs, Crossref, KBR, bases professionnelles, bibliothèques. Pour les universitaires belges, rechercher tôt DIAL.pr, DI-fusion, ORBi, PURE, etc.

Un AAM/postprint peut vérifier les mots de l'auteur mais pas nécessairement la pagination éditeur. Open Access ne signifie pas absence de droit d'auteur ou de restrictions TDM.

Résoudre `op. cit.` et `ibid.` dans le document avant d'utiliser le web. Une absence Crossref ne prouve pas l'inexistence. ISBN, édition et DOI doivent être vérifiés, jamais devinés.

## Quand arrêter la recherche

Avant de conclure qu'une référence doctrinale n'est pas vérifiable, tenter au minimum, en consignant chaque essai comme `SEARCH_ATTEMPT` :

1. l'auteur : dépôt institutionnel ou page de l'université, annuaire ou catalogue d'autorités (KBR, BnF, VIAF, ORCID) ;
2. la revue ou l'ouvrage : sommaire du volume ou de l'année cités, sur le site de l'éditeur, d'une base professionnelle ou d'un catalogue de bibliothèque ;
3. le titre : recherche de la formulation exacte dans Crossref, Google Scholar ou un moteur général, dans chaque langue plausible.

S'arrêter dès que la référence est établie, ou lorsque ces trois voies ont été tentées sans élément nouveau. Ne pas multiplier les requêtes voisines. Un accès payant non disponible est une limite, pas un résultat négatif.

## Exprimer un doute sérieux

- **Contradiction établie** : si le sommaire complet du volume cité est accessible et ne contient pas l'article à la page indiquée (ou si cette page n'existe pas dans le volume), le statut est `NOT_FOUND_OR_CONTRADICTORY`, avec le sommaire comme preuve.
- **Sans contradiction** : si le sommaire est inaccessible, le statut reste `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES`. Les indices objectifs peuvent être énumérés de façon neutre (auteur introuvable dans les dépôts et catalogues, titre sans aucune occurrence, pagination incompatible avec la taille habituelle du volume) et assortis d'une recommandation de contrôle humain prioritaire.
- Ne jamais qualifier une référence d'« inventée » ou de « fictive » sans contradiction établie, et ne jamais prêter une intention à l'auteur du document.
