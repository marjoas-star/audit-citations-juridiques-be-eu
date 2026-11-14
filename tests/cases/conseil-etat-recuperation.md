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
| T53-R9 | Recherche du numéro : plusieurs fiches, dont un arrêt qui cite ce numéro et un arrêt dont le rôle le contient | Fiche retenue sur son titre ; en-tête du PDF contrôlé ; les autres fiches écartées sans alerte |
| T53-R10 | Recherche du numéro : 0 résultat ou fiche absente ; l’adresse officielle directe livre un PDF | Numéro et date lus dans l’en-tête ; obtention par adresse directe consignée ; aucun `NOT_FOUND` tiré de la recherche |
| T53-R11 | Recherche sans résultat et adresse directe en 404 | Aucune inexistence déduite ; juriDict ou corroboration ; `NOT_VERIFIABLE_WITH_ACCESSIBLE_SOURCES` à défaut |
| T53-R12 | Filtre Langue « Français » actif, arrêt néerlandais | Filtre retiré avant toute conclusion ; filtre consigné |
| T53-R13 | Ancienne adresse `?page=caselaw_page4` : page d’accueil en HTTP 200 | Pas un résultat ; reprise par le menu Arrêts ; aucune conclusion sur l’arrêt |
| T53-R14 | Ancien lien `arr.php` d’un arrêt bilingue : texte néerlandais reçu | Langue constatée ; adresse française de la fiche reprise pour une citation française |
| T53-R15 | Arrêt de 2025 : nom du requérant cité, PDF pseudonymisé | Champ parties non vérifiable sur la version publiée ; aucune correction proposée ; aucune recherche du nom ailleurs |
| T53-R16 | Arrêt récent : ECLI imprimé en pied de page ; arrêt de 2020 sans ECLI | ECLI relevé tel qu’imprimé pour le premier ; aucun ECLI composé pour le second |

Les cas R9 à R16 tiennent à la refonte du site constatée le 14 novembre 2026 (champ unique de recherche, adresses `/arrets/` et `/arresten/`). Ces cas complètent les règles antérieures : septembre 1994, exception étrangers, juriDict non exhaustif et asymétrique, aucun identifiant reconstruit, aucune adresse construite hors du schéma officiel admis. Ils ne les remplacent pas.
