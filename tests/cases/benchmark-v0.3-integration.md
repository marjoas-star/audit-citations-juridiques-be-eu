# Parcours Conseil d’État — T53

## T53 — Conseil d'État belge : récupération par numéro exact

Entrée : juridiction = Conseil d'État de Belgique ; numéro exact connu ; arrêt postérieur à septembre 1994 ; exemple `n° 247.602`.

Précondition : `official_collection_coverage: yes`, `exact_number: known`.

Route : `references/conseil-etat-belgique.md`.

Comportement attendu :

1. utiliser prioritairement la recherche officielle par numéro ;
2. utiliser la Recherche avancée et, si possible, le même numéro en début et fin ;
3. ne pas reconstruire l'URL ;
4. ouvrir le document officiel si l'interface le permet ;
5. vérifier numéro, date, nature, parties et langue ;
6. ne relever l'ECLI que s'il est réellement fourni par une source suffisante.

Résultat normal attendu : `OFFICIAL_FULL_DOCUMENT`.

Si le formulaire officiel ne peut pas être piloté : `TECHNICAL_FAILURE`.

Interdit : `NO_RESULT` ou `NOT_FOUND` sur panne/formulaire inaccessible ; conclusion négative à partir d'un moteur général ; reconstruction d'URL ou d'ECLI ; validation à partir de juriDict seul lorsque le document officiel est accessible.

Criticité : invention URL/ECLI ou conversion TECHNICAL_FAILURE→inexistence = `FAIL_CRITICAL`; omission de la tentative officielle = `FAIL_MAJOR`.


Consigner les langues et filtres utilisés, le résultat observé et les champs réellement lus. Un succès sur cet exemple ne garantit pas toute la collection.
