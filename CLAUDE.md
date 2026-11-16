# Consignes pour Claude

## Vérification systématique de la jurisprudence du Conseil d'État

Toute réponse qui cite un arrêt ou une ordonnance du Conseil d'État de Belgique doit être vérifiée **par défaut**, sans attendre qu'on le demande, sur le site officiel du Conseil d'État, selon la procédure de `references/conseil-etat-belgique.md` :

1. rechercher le numéro seul dans la recherche officielle des arrêts (`https://www.raadvst-consetat.be/fr/recherche/arrets`) et repérer la fiche dont le titre porte ce numéro ;
2. ouvrir le PDF officiel (`/arrets/<numéro>` pour le français, `/arresten/<numéro>` pour le néerlandais) et contrôler la signature PDF ;
3. vérifier dans l'en-tête le numéro, la date et la formation (chambre, président seul, référé) ;
4. retrouver chaque passage cité dans le texte et contrôler qu'il figure dans les **motifs** de l'arrêt, et non dans le rapport de l'auditeur ou dans la thèse d'une partie reproduits dans l'arrêt ;
5. ne citer entre guillemets que du texte effectivement lu dans le document officiel, et donner l'adresse officielle `/arrets/` ou `/arresten/` (et non `arr.php?nr=`).

Les bases tierces (Legal Data Hunter, moteurs de recherche, doctrine) servent à **découvrir** des arrêts, jamais à les **vérifier**. Leurs métadonnées, en particulier les dates, peuvent être fausses.

Si le site officiel est inaccessible, le signaler comme limite technique (`TECHNICAL_FAILURE`) et ne présenter les citations que comme non vérifiées.
