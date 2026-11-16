# Moniteur belge et Justel

**Dernière révision des instructions : 16 novembre 2026**

Principe : RefLex cartographie, le Moniteur belge établit la publication, Justel documente le texte consolidé et son évolution.

Toujours distinguer date de l'acte, publication, entrée en vigueur et date/version pertinente. Une version consolidée actuelle ne doit pas être utilisée seule pour vérifier une citation historique.

La consolidation peut accuser un retard ; les tables de modification et le Moniteur peuvent être nécessaires. NUMAC doit être copié depuis une source suffisante, jamais reconstruit.

Avant de qualifier une citation d’inexacte, appliquer le contrôle de version de [datation-et-rapport.md](datation-et-rapport.md). La date de consolidation, la date d’effet et la date de consultation sont distinctes. Comparer les textes modificatifs si deux consolidations divergent.

## Accès au site ejustice (Justel et Moniteur)

Constat du 16 novembre 2026, depuis une session cloud : tout le domaine `ejustice.just.fgov.be` (Justel, page d'accueil, PDF du Moniteur) renvoie une **vérification anti-robot**. La réponse a un statut 200 et un type HTML, même pour une adresse de PDF ; le texte contient « This question is for testing whether you are a human visitor ». Ce n'est ni le document ni une absence de document.

- Reconnaître la page (signature PDF absente, texte ci-dessus) et consigner `TECHNICAL_FAILURE`.
- Ne pas la contourner (règle 8 de `SKILL.md`) : pas de navigateur automatisé pour la franchir, pas de tentatives répétées, pas d'intermédiaire.
- Voies normales, par ordre de préférence :
  1. le navigateur de l'application de bureau ou l'extension Claude in Chrome, qui consultent le site depuis la connexion du juriste ; le juriste valide lui-même la vérification si elle s'affiche ;
  2. une session Claude qui tourne sur l'ordinateur du juriste (application de bureau, ou Remote Control) ;
  3. à défaut, une autre source officielle du même texte (ci-dessous), en indiquant que Justel n'a pas pu être consulté.

## Autres sources officielles

- **Moniteur belge 1934-1997** : la bibliothèque de droit de la KU Leuven tient une page d'accès au Moniteur numérisé (voir [recueils-numerises-kul.md](recueils-numerises-kul.md)), joignable depuis une session cloud le 16 novembre 2026 (connexions parfois coupées : réessayer une ou deux fois). Pour 1946-1959, cette page renvoie, mois par mois, à des numérisations hébergées par Google Books, qui n'ont pas été testées. Une telle numérisation établit la publication et le texte publié, pas la consolidation ; lire le texte sur l'image.
- **Coordinations officieuses jointes aux documents parlementaires** : un projet de loi qui modifie une loi existante en joint souvent une coordination, avec la référence de chaque modification. Exemple : DOC 51 2479/002 (2006), pour les lois sur le Conseil d'État. Elle est datée de son dépôt ; ne pas l'utiliser pour une autre date sans contrôle.
- **Textes consolidés publiés par une institution pour ses propres lois** : par exemple, le site du Conseil d'État (rubrique « Réglementation ») publie le texte consolidé des lois coordonnées sur le Conseil d'État, établi par son bureau de coordination, avec la version précédente et des notes de modification. C'est une source institutionnelle, non la consolidation Justel : relever la version et sa date d'application.
- **RefLex** peut renvoyer à des PDF du Moniteur ; le 16 novembre 2026, le domaine ne répondait pas depuis une session cloud (`TECHNICAL_FAILURE`, voir [reflex.md](reflex.md)).
