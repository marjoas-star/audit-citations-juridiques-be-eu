# Complément T53 — récupération et lecture

Protocole descriptif, sans assertion de tests déjà exécutés. Conserver les sorties et comparer aux invariants ci-dessous.

| Cas | Observation fournie | Comportement attendu |
|---|---|---|
| T53-R1 | Numéro connu, date citée erronée | Recherche numérique seule, sans filtre de date masquant le résultat ; contrôle de la date dans le document |
| T53-R2 | Résultat officiel valide, lecteur web en erreur | Recherche marquée réussie ; erreur de lecture séparée ; téléchargement standard du href observé si disponible |
| T53-R3 | Téléchargement HTTP 200, contenu HTML d’erreur | Aucun VERIFIED sur la base du statut HTTP ; échec de récupération documenté |
| T53-R4 | Fiche juriDict FR, PDF reçu NL | Langue du PDF constatée ; aucune citation française déclarée EXACT à partir du NL |
| T53-R5 | Résultats PDF original et traduction | Documents distingués ; titre, en-tête et langue examinés |
| T53-R6 | Mention de rectification au début du PDF | Mention et portée pertinente contrôlées, sans fusion ni recherche supplémentaire automatique si le rectificatif est déjà joint |
| T53-R7 | Formulaire inaccessible, moteur général sans résultat | TECHNICAL_FAILURE, jamais inexistence déduite |
| T53-R8 | Plusieurs points de droit d’un seul arrêt | Une source judiciaire ; notices et citations distinctes |

Ces cas complètent les règles antérieures : septembre 1994, exception étrangers, juriDict non exhaustif et asymétrique, aucun identifiant ni URL reconstruits. Ils ne les remplacent pas.
