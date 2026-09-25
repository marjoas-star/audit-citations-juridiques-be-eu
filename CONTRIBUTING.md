# Contribuer

Décrire un défaut par une entrée reproductible, le résultat observé et les preuves réellement accessibles. Ne pas publier de document confidentiel, de journal de session ou de données de compte dans une issue.

Préserver les originaux, les règles de non-invention et les limitations de couverture. Un résultat négatif et une panne sont deux observations différentes. Toute modification d’un oracle doit être motivée et versionnée, sans changer rétroactivement les anciens résultats.

Pour tester un comportement, donner à un évaluateur indépendant le skill et l’entrée sans l’oracle. Conserver sa réponse avant la comparaison. Séparer recherche réelle, simulation et contrôle de structure. Les protocoles de `tests/cases/` sont des tests descriptifs, pas une suite automatiquement exécutée.

L'exécutant d'un rejeu reçoit uniquement `SKILL.md`, `references/`, `schemas/`, `templates/`, `scripts/` et l'entrée du cas. Exclure `tests/` et tout fichier qui rapporte des résultats ou des corrigés, notamment `CHANGELOG.md`, `VALIDATION.md` et `RELEASE.md`. Avant l'exécution, rechercher dans la copie fournie les éléments caractéristiques du corrigé (noms, identifiants, dates attendues) ; toute occurrence rend le rejeu non indépendant tant que le fichier n'est pas retiré. Consigner la liste des fichiers fournis avec les empreintes. L'exemple `templates/example-audit.json` est fictif et ne doit reprendre aucun cas de test.

La version indiquée en tête de `SKILL.md` doit rester identique au fichier `VERSION` ; un test le vérifie.

Avant une publication : contrôler les liens relatifs et le frontmatter, relire les différences, rejouer les cas affectés, documenter la version et les limites. Ne pas convertir un contrôle de format en validation juridique. Les rapports publics doivent être des synthèses minimales ; conserver les pièces complètes dans le dossier de travail approprié.

La prochaine campagne suit le [protocole prospectif V1](tests/validation-v1/protocole.md) et son [plan de corpus réservé](tests/validation-v1/corpus.md). Ils décrivent des travaux à exécuter, pas des résultats acquis.

Pour un essai exploratoire par un juriste : [guide des bêta-testeurs](tests/beta/guide.md) et [fiche de retour](tests/beta/fiche-retour.md). Les retours d’usage ne remplacent pas la validation indépendante.

## Règles de maintenance et de publication

Ces règles concernent les mainteneurs ; elles ne font pas partie des instructions exécutées pendant un audit (`SKILL.md`).

### Datation des modules

Chaque module de `references/` indique sa date de révision des instructions. Les vérifications fonctionnelles sont datées séparément et rattachées aux parcours réellement exécutés : une révision documentaire ne prouve pas le fonctionnement d’une interface. Tester URLs, recherche, interfaces, replis et exemples selon les changements observés.

### Versionnement

Semantic Versioning `MAJOR.MINOR.PATCH`. Avant V1 : `0.x`.

### Benchmarks exigés avant V1

Benchmark v0.1, benchmark v0.2 adversarial, benchmark v0.3 intégration, test UX de progression, test T53 et audits d’intégration complets.

Un résultat de test renvoie à ses entrées, à la sortie effectivement produite, aux observations/outils et à la comparaison avec l’oracle. Distinguer revue de spécification, scénario simulé et parcours réel. Un oracle seul n’est pas une exécution ; une validation de structure ou de mise en page n’est pas une validation comportementale ou documentaire. Sans trace suffisante, noter `NOT_DEMONSTRATED`, jamais `PASS`. Les résultats historiques non traçables ne permettent pas le passage au vert.

Conditions minimales : 0 invention, 0 sur-vérification, 0 fusion documentaire, 0 adaptation trompeuse acceptée et progression adaptée à la taille de l’audit.

### Release blockers

Une V1 publique est interdite tant qu’un benchmark révèle :

- **A — invention** : identifiant fabriqué ou référence complétée sans preuve ;
- **B — sur-vérification** : snippet → `VERIFIED`, source secondaire → ECLI vérifié, panne → inexistence ;
- **C — fusion** : arrêt + conclusions, proposition + directive, rapport + projet, texte adopté + loi ;
- **D — intégrité citationnelle** : ellipse trompeuse validée comme simple adaptation ;
- **E — récupération Conseil d’État par numéro exact** : avant passage du `PUBLIC_RELEASE_GATE` au vert, `COUNCIL_OF_STATE_EXACT_NUMBER_RETRIEVAL = GREEN`. Le test T53 doit confirmer que la recherche officielle par numéro exact est tentée prioritairement, sans reconstruction d’URL/ECLI, et qu’un échec du formulaire produit `TECHNICAL_FAILURE` plutôt qu’une fausse inexistence.

### Documentation et licence

README en FR/NL/DE/EN : `README.md`, `README.fr.md`, `README.nl.md`, `README.de.md`, `README.en.md`. Documentation sous `CC BY-NC-SA 4.0` ; code Python (`scripts/`, `tests/`) sous `PolyForm Noncommercial 1.0.0` (voir `LICENSE-CODE.md`). Tout nouveau fichier Python porte l'en-tête `# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0`. Ne pas qualifier le projet d’« open source » au sens OSI compte tenu de la restriction NC.
