# Produire un rapport régulier en français

Le générateur transforme des conclusions établies en PDF et Markdown. Il ne recherche aucune source, n’évalue pas le droit et ne transforme pas une preuve faible en vérification. Les couleurs, polices, marges, titres, compteurs et règles de pagination sont centralisés dans un seul fichier.

## Utilisation

Python 3.10 ou ultérieur. Le PDF nécessite ReportLab ; ses polices Vera sont utilisées depuis l’installation, sans copie dans le dépôt. Le Markdown seul ne requiert aucune dépendance tierce. Les tests du PDF nécessitent aussi pypdf. PyYAML n’intervient pas.

```sh
python3 scripts/render_report.py audit.json --output rapport
python3 scripts/render_report.py audit.json --output rapport --markdown-only
python3 tests/test_render_report.py
```

Le premier appel produit rapport.md et rapport.pdf ; le second uniquement rapport.md. Le chemin de sortie est choisi par l’utilisateur ou l’agent. Garder les données personnelles, documents sources et rapports de clients hors du dépôt public. Une sortie existante est remplacée : utiliser un nouveau nom pour une révision et préserver les réponses gelées d’une évaluation.

## Données d’entrée

Objet JSON UTF-8. Les données doivent être rédigées en français courant ; `report_language` vaut `fr`. Le générateur refuse une autre langue pour éviter de produire silencieusement un rapport bilingue. Le skill conserve ses quatre langues de travail ; les rapports NL/DE/EN utilisent le modèle éditorial avec un autre outil de mise en page jusqu’à localisation du générateur.

Champs racine : `title`, `document`, `date`, `version`, `scope`, `summary` (textes) ; `limitations` et `method` (listes de textes) ; `records` et `quotations` (listes). Décrire le périmètre réellement audité et les dates inconnues ; ne pas assimiler date d’export et date de rédaction.

Chaque fiche `records` comporte :

- `id` unique pour l’occurrence ; `source_id` commun aux occurrences du même document ;
- `title`, `original`, `checked`, `location` ;
- `status` : un des cinq statuts internes de référence ;
- `checks` : liste explicite des champs/passages contrôlés, en précisant les différences de preuve si nécessaire ; `limits` : texte, éventuellement vide lorsque la limite commune figure déjà dans la synthèse ;
- `sources` : liste d’objets `label`, `url`, `locator`, `language`. Ne transmettre que des liens observés et des preuves réellement consultées. Pour des preuves locales, décrire les pièces dans la fiche et la méthode ; ne pas inventer une URL publique pour satisfaire le générateur ; utiliser le modèle manuel si aucune URL pertinente n’est disponible ;
- facultativement `notes` et `findings`. Chaque constat contient `severity`, `problem`, `action`. Ne pas proposer une correction certaine lorsque la preuve ne le permet pas.

Chaque citation `quotations` comporte `id`, `record_id`, `title`, `location`, `status`, `integrity`, `comparison`, `context`. Le dernier champ précise notamment le locuteur et l’effet des retraits. `translation_assessment` est obligatoire pour une traduction ; la conformité littérale et la fidélité de traduction ne se confondent pas. Décrire les mots qui diffèrent, les adaptations signalées et leurs conséquences dans `comparison` et `context`, sans longues reproductions inutiles.

La convention d’audit complète reste dans [citation-record.md](../schemas/citation-record.md). L’entrée de présentation est une projection de ces données, pas leur remplacement. Les traces techniques détaillées restent séparées du rapport lisible.

## Vérifications de livraison

Le générateur refuse notamment les identifiants dupliqués, les statuts inconnus, les citations sans fiche et les références déclarées vérifiées sans contrôles ni sources. Cela vérifie la cohérence du fichier, pas l’authenticité des preuves. Les compteurs proviennent des fiches : occurrences et sources distinctes restent séparées.

Après génération : ouvrir le PDF, rendre toutes ses pages, contrôler lisibilité, retours à la ligne, tableaux, absence de pages quasi vides, liens de preuve et conservation des conclusions. Corriger la mise en page sans modifier les résultats de l’audit. En cas de dépendance indisponible, livrer le Markdown et préciser que le PDF n’a pas été produit.
