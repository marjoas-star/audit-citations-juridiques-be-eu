# Révision 0.5.0-beta.3 — 25 septembre 2026

## Ce qui a été vérifié

- 21 tests automatiques passent : datation initiale immuable, révision avec périmètre, décalage UTC, dates des sources, déduplication des erreurs, séparation des suggestions, conservation des versions et du type de preuve, localisateurs des citations, intégrité de la transcription et pagination de 250 occurrences.
- Le validateur structurel du skill réussit. Ce contrôle ne valide pas le droit.
- Quatre nouveaux scénarios fictifs ont été appliqués par un agent distinct, sans corrigé fourni : réexport ancien, archive normative à applicabilité incertaine, mots exacts mal attribués, erreur répétée et suggestion. Les quatre réponses respectent les invariants attendus ; la [première réponse](beta3-forward-first-response.md) est conservée. Ce sont des simulations, pas des recherches juridiques ni des évaluations humaines indépendantes.
- Une revue indépendante du générateur a révélé cinq défauts supplémentaires : tableau très long, date de preuve incohérente, informations probantes perdues, identifiant de constat partagé entre catégories, localisateur de citation non affiché. Ils ont été corrigés et couverts par les tests.

## Retours de bêta-test et portée

Cinq retours portant sur des extraits construits déclarent chacun quatre erreurs introduites détectées. Ce total déclaré ne mesure pas la précision générale : des faux positifs et qualifications excessives ont aussi été relevés. Les profils sont présentés comme fictifs et les durées comme estimées ; ne pas annoncer cinq évaluateurs humains indépendants ni un gain de temps mesuré.

Les règles ont été corrigées : version normative avant alerte, axes de citation distincts, preuves visibles, corrections dans la langue du document, dates persistantes, compteurs cohérents, présentation condensée. Les rapports initiaux et retours sont conservés dans le dossier privé ; leur révision ciblée n’est pas un nouveau benchmark indépendant.

[T61–T70](../cases/beta-revision.md) consignent les scénarios de développement. Pour mesurer la généralisation, il reste nécessaire de conduire le protocole prospectif sur un corpus réservé, avec relectures humaines documentées. Les documents privés, rapports et textes sous abonnement ne sont pas publiés dans ce dépôt.
