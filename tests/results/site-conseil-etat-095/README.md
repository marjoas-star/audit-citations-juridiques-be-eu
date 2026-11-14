# Constats — site du Conseil d'État refondu (0.9.5)

Date : 14 novembre 2026. Client : `curl`, depuis un serveur, sans navigateur. Il s'agit de constats sur le site, relevés pour réécrire `references/conseil-etat-belgique.md` ; ce n'est pas un passage à l'aveugle du skill. Les pages et PDF téléchargés ne sont pas redistribués ici.

## Anciennes adresses

| Adresse demandée | Réponse |
|---|---|
| `/?lang=fr&page=caselaw`, `caselaw_page4`, `juridict`, `search_help_adv` | redirection vers `/fr/?lang=fr&page=…`, HTTP 200, page d'accueil (62 255 octets, identique pour les quatre) |
| `/arr.php?nr=247602` | redirection vers `/arresten/247602`, PDF de 6 pages, texte français |
| `www.conseildetat.be`, `www.raadvanstate.be` | redirection vers `/nl/`, même page d'accueil |

## Recherche dans les arrêts (`/fr/recherche/arrets`)

Formulaire en GET, champ `query` ; filtres `year`, `language`, `chambre`, `category` ; tri `sort` (pertinence, `date_desc`, `date_asc`) ; pagination `page`, dix fiches par page. Total sans critère : 120.093 documents (néerlandais 60.798, français 58.798, allemand 497). Par année : 1994 : 30 ; 1995 : 472 ; 1996 : 1.932 ; 1997 : 3.474.

| Requête | Total | Fiches |
|---|---|---|
| `247602`, `247.602`, `"247.602"` | 2 | Arrêt 247.602 (20-05-2020, XI, A. 229.684/XI-22.803) ; Arrêt 258.417 (12-01-2024, même rôle) |
| `230687` | 3 | Arrêt 230.687 (27-03-2015, XV) ; Arrêts 249.691 et 247.647 (rôle A. 230.687/XI-22.963) |
| `247602` + année 2020 + langue français | 1 | Arrêt 247.602 |
| `247.602` + langue néerlandais | 0 | — |
| `268329` | 1 | Arrêt 268.329 (12-11-2026, X), néerlandais |
| `268329` + langue français | 0 | — |
| `A. 242.444/X-18.746` | 1 | Arrêt 268.329 |
| `50000` | 608 | l'arrêt n° 50.000 n'est pas dans les premières pages |
| `50000` ou `"50.000"` + année 1994 | 2 | deux fiches de l'arrêt 49.889 (FR et NL) |
| `AUTO-MARKET` + année 1994 | 0 | — |
| `61000` | 20 | aucune fiche « Arrêt 61.000 » |
| `61000` + année 1996 | 0 | — |
| `999999999` | 0 | « Aucun document trouvé. » |

## Adresses directes

| Adresse | Réponse |
|---|---|
| `/arrets/247602`, `/arresten/247602` | même PDF (24 769 octets), français, « no 247.602 du 20 mai 2020 », sans ECLI |
| `/arrets/50000` | PDF de 11 pages, « no 50.000 du 28 octobre 1994 », A.48.856/VI-11.039, sans ECLI |
| `/arrets/268329` | PDF de 25 pages, néerlandais, « nr. 268.329 van 12 november 2026 », `ECLI:BE:RVSCE:2026:ARR.268.329` en pied de chaque page |
| `/arrets/92340` / `/arresten/92340` | arrêt français / « Nederlandse tekst (titel VI, hoofdstuk II, …) » |
| `/arrets/70412` / `/arresten/70412` | « Texte français (Titre VI, chapitre II, …) » / arrêt néerlandais |
| `/arrets/61000`, `/arrets/999999999` | 404, corps vide |
| `/fr/arrets/247602` | 404, page HTML |

## Autres collections

- Ordonnances (`/fr/recherche/ordonnances`) : 6.252 documents ; filtres Année, Langue ; fiches « Ordonnance de cassation 16.903 », lien `/cassations/16903` ; requérants « XXXXX ».
- Avis (`/fr/recherche/avis`) : 79.830 documents ; filtres Année, Chambre, Matière, Type de norme, Demandeur d'avis, Délai ; liens `/avis/80136` et `/avis/80136/projet`.
- juriDict (`/fr/banques-de-donnees/juridict`) : sans préférence de langue, redirection vers `/nl/databanken/juridict/` ; avec la langue française choisie, recherche `q=247.602` : 1 point de droit, dont la fiche renvoie à `/arrets/247602` ; aucun ECLI affiché. Champs de la recherche avancée : `applicant`, `decision`, `procedure` (chambre), `number`, `from`, `before`, `domain`, `kind`.

## Limites

Un seul client, un seul jour, une douzaine de numéros. L'incomplétude de l'index n'est établie que pour l'arrêt n° 50.000 et par les totaux annuels ; elle peut être provisoire (migration en cours). Le n° 61.000 n'a été obtenu par aucune voie : son existence en ligne n'est ni établie ni exclue.
