# Produire un rapport régulier (FR, NL, DE, EN)

Le générateur transforme des conclusions établies en PDF et Markdown. Il ne recherche aucune source, n’évalue pas le droit et ne transforme pas une preuve faible en vérification. Les couleurs, polices, marges, titres, compteurs et règles de pagination sont centralisés dans un seul fichier.

## Utilisation

Python 3.10 ou ultérieur. Installer les dépendances avec `pip install -r requirements.txt`. Le PDF nécessite ReportLab ; ses polices Vera sont utilisées depuis l’installation, sans copie dans le dépôt. Le Markdown seul ne requiert aucune dépendance tierce. Les tests du PDF nécessitent aussi pypdf. PyYAML n’intervient pas.

```sh
python3 scripts/render_report.py audit.json --output rapport
python3 scripts/render_report.py audit.json --output rapport --markdown-only
python3 -m unittest discover -s tests -p 'test_*.py'
```

Le premier appel produit rapport.md et rapport.pdf ; le second uniquement rapport.md. Le chemin de sortie est choisi par l’utilisateur ou l’agent. Garder les données personnelles, documents sources et rapports de clients hors du dépôt public. Une sortie existante est remplacée : utiliser un nouveau nom pour une révision et préserver les réponses gelées d’une évaluation.

## Données d’entrée

Objet JSON UTF-8. `report_language` vaut `fr`, `nl`, `de` ou `en` (par défaut `fr`) : les titres, statuts, dates, avertissement et libellés sont alors produits dans cette langue. Rédiger dans la même langue la synthèse, le périmètre, les limites, la méthode, les contrôles et les constats ; les passages probants restent dans la langue de la source. Toute autre langue est refusée. Si la synthèse chiffre les sources distinctes ou les erreurs (« onze sources distinctes », « 4 corrections établies »…), ces chiffres doivent correspondre aux compteurs calculés, faute de quoi le rapport est refusé. Les références confirmées sans aucune réserve sont regroupées en fin de rapport, sous forme de liste compacte avec leurs preuves ; les autres gardent une fiche complète.

Un exemple complet, valide et entièrement fictif se trouve dans [example-audit.json](example-audit.json) : le copier et le remplacer champ par champ. Il ne reproduit aucun cas de test. Dans `excerpt`, donner le passage sans guillemets : le générateur les ajoute (une paire englobante fournie par erreur est retirée).

Champs racine : `title`, `document`, `date` (date du document audité, libre), `skill_version` (version du skill utilisée, par ex. `0.5.0-beta.3` ; l'ancien nom `version` reste accepté, à ne pas confondre avec `report_version`), `scope`, `summary` (textes) ; `limitations` et `method` (listes de textes) ; `records` et `quotations` (listes). Décrire le périmètre réellement audité et les dates inconnues ; ne pas assimiler date d’export et date de rédaction.

`report_metadata` est obligatoire : `established_at` (ISO 8601 avec décalage UTC), `timezone`, `precision` (`second` ou `day` si l’heure ancienne n’est pas conservée), `report_version`, `checks_started_on`, `checks_completed_on` (dates ISO) et `legal_reference` (date juridique et provenance, ou incertitude explicite). Une révision ajoute `revision` : `issued_at`, `scope`, `previous_version`. Le générateur ne modifie jamais ces dates ; il ne lit l’horloge que pour refuser une date d’établissement ou de révision postérieure à l’heure réelle (tolérance de cinq minutes). Relever l’heure sur l’horloge du système au moment d’établir le rapport, jamais l’estimer. Exemple fictif :

```json
{"established_at":"2026-09-24","timezone":"Europe/Brussels","precision":"day","report_version":"v2","checks_started_on":"2026-09-24","checks_completed_on":"2026-09-25","legal_reference":"Non précisée dans la consigne","revision":{"issued_at":"2026-09-25T10:00:00+02:00","scope":"Corrections ciblées de deux références ; autres contrôles conservés","previous_version":"v1"}}
```

Chaque fiche `records` comporte :

- `id` unique pour l’occurrence ; `additional_occurrences` peut conserver des renvois regroupés (objets `id`, `location`, `original`), inclus dans le compteur ; leurs emplacements doivent rester visibles dans `location` ; `source_id` commun aux occurrences du même document ;
- `title`, `original`, `checked`, `location` ;
- `status` : un des cinq statuts internes de référence ;
- `checks` : liste explicite des champs/passages contrôlés, en précisant les différences de preuve si nécessaire ; `limits` : texte, éventuellement vide lorsque la limite commune figure déjà dans la synthèse ;
- `sources` : liste d’objets `label`, `url`, `locator`, `language`. Ne transmettre que des liens observés et des preuves réellement consultées. Pour des preuves locales, décrire les pièces dans la fiche et la méthode ; ne pas inventer une URL publique pour satisfaire le générateur ; utiliser le modèle manuel si aucune URL pertinente n’est disponible ;
- facultativement `notes` et `findings`. Chaque constat contient `id` (stable pour une même erreur répétée), `kind` (`error` ou `suggestion`), `severity`, `problem`, `action`. Toute erreur exige un court `excerpt` probant dans ses sources. `consulted_on` précise la date de consultation d’une source. `notes` est une liste de textes. `original_kind: summary` signale honnêtement une référence abrégée, si sa transcription intégrale n’a pas été conservée. Ne pas proposer une correction certaine lorsque la preuve ne le permet pas.

Lorsqu'une référence est exacte mais que sa citation s'écarte du texte, garder le statut de la référence (par ex. `VERIFIED`) et porter l'écart dans `quotations` : le tableau et la fiche afficheront alors « Référence vérifiée · citation : écart mineur », sans laisser croire à un résultat sans réserve.

Chaque citation `quotations` comporte `id`, `record_id`, `title`, `location`, `status`, `integrity`, `comparison`, `context`. Le dernier champ précise notamment le locuteur et l’effet des retraits. `attribution` et `temporal_assessment` permettent de séparer source attribuée et version temporelle de la fidélité des mots. `translation_assessment` est obligatoire pour une traduction ; la conformité littérale et la fidélité de traduction ne se confondent pas. Décrire les mots qui diffèrent, les adaptations signalées et leurs conséquences dans `comparison` et `context`, sans longues reproductions inutiles.

La convention d’audit complète reste dans [citation-record.md](../schemas/citation-record.md). L’entrée de présentation est une projection de ces données, pas leur remplacement. Les traces techniques détaillées restent séparées du rapport lisible.

## Longueur

Viser 5 à 6 pages pour une douzaine de sources ; le générateur compte les pages du PDF et signale un dépassement (cible : 6 pages jusqu'à 12 sources distinctes, une page de plus par tranche de 4 sources supplémentaires). La longueur vient surtout des textes libres : une synthèse de quelques phrases (120 mots au plus) ; un contrôle tient en une ligne (25 mots au plus, 4 contrôles au plus par fiche) ; un constat en deux phrases (60 mots au plus pour le problème comme pour la correction) ; un passage probant se limite aux mots qui prouvent (60 mots au plus) ; une limite en une phrase. Une référence qui appelle une correction n'est présentée qu'une fois, avec sa correction ; une même preuve n'est pas répétée. Le générateur signale les champs trop longs sans rien couper : les raccourcir puis relancer une fois, sans supprimer de correction, de preuve ni de limite.

## Vérifications de livraison

Le générateur refuse notamment les identifiants dupliqués, les statuts inconnus, les citations sans fiche et les références déclarées vérifiées sans contrôles ni sources. Cela vérifie la cohérence du fichier, pas l’authenticité des preuves. Les compteurs proviennent des fiches : occurrences et sources distinctes restent séparées.

Après génération : ouvrir le PDF, rendre toutes ses pages, contrôler lisibilité, retours à la ligne, tableaux, absence de pages quasi vides, liens de preuve et conservation des conclusions. Corriger la mise en page sans modifier les résultats de l’audit. En cas de dépendance indisponible, livrer le Markdown et préciser que le PDF n’a pas été produit.
