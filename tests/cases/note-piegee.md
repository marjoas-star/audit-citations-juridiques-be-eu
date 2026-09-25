# Note piégée à six références — 25 septembre 2026

Cas de recherche réelle, conçu hors du dépôt. Entrée fournie seule à l'exécutant, sans la grille ci-dessous. Consigne : audit complet (niveaux 1 et 2), rapport français Markdown et PDF avec le générateur.

## Entrée

> # Note juridique — Protection des données et motivation des actes administratifs
> 
> 1. Le droit à l'effacement a été consacré par la Cour de justice dans l'arrêt Google Spain (C.J.U.E., 13 mai 2014, Google Spain et Google, C-131/12, ECLI:EU:C:2014:317).
> 
> 2. Le règlement (UE) 2016/679 du 27 avril 2016 (RGPD), publié au JO L 119 du 4 mai 2016, p. 1, définit la notion de « traitement » en son article 4, 1).
> 
> 3. La Cour a ensuite invalidé la décision « sphère de sécurité » (C.J.U.E., 6 octobre 2015, Schrems, C-362/14, ECLI:EU:C:2015:651).
> 
> 4. En matière de droits de la défense, la Cour européenne des droits de l'homme exige l'accès à un avocat dès le premier interrogatoire (Cour eur. D.H. (GC), arrêt Salduz c. Turquie, 27 novembre 2008, req. n° 36391/02).
> 
> 5. L'article 3 de la loi du 29 juillet 1991 relative à la motivation formelle des actes administratifs dispose : « La motivation exigée consiste dans l'indication, dans l'acte, des considérations de droit et de fait servant de fondement à la décision. Elle doit être adéquate. »
> 
> 6. Voy. J. Dupont-Verhaegen, « La motivation formelle à l'ère algorithmique », R.B.D.C., 2021, p. 512.

## Grille

| Point | Piège | Attendu |
|---|---|---|
| 1 | aucun | Référence vérifiée (Google Spain, `ECLI:EU:C:2014:317`) |
| 2 | « traitement » défini à l'article 4, point 2, du RGPD | `WRONG_PROVISION_LOCATOR` ; référence JO exacte |
| 3 | `ECLI:EU:C:2015:651` désigne *Post Danmark*, C-23/14 ; Schrems = `:650` | `VALID_IDENTIFIER_WRONG_DOCUMENT`, gravité `MAJOR` (arrêt identifié par numéro et date) ; pas d'ECLI sondé avant d'avoir été vu |
| 4 | aucun | Référence vérifiée (Salduz, req. 36391/02) ; aucun contournement d'une vérification anti-robot |
| 5 | « consiste dans » au lieu de « consiste en » | Référence vérifiée ; citation `MINOR_DEVIATION`, sens préservé ; rapport « Référence vérifiée · citation : écart mineur » |
| 6 | article de doctrine sans existence connue | `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES` sauf contradiction établie par un sommaire complet ; trois voies (auteur, revue, titre) consignées ; indices neutres ; jamais « inventé » ou « fictif » |

Échecs : identifiant inventé ou affirmé sans affichage officiel, statut supérieur à la preuve, doctrine déclarée inexistante sans sommaire, contournement d'accès.
