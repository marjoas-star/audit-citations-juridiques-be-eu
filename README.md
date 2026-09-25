# Audit des citations juridiques — Belgique & Europe

**Version 0.7.0-beta.1 — publication expérimentale.** Méthode pour auditer les références et citations d’un document en droit belge, droit de l’Union européenne et CEDH. Ce skill accompagne un agent ; ce n’est pas un moteur de recherche autonome.

> **Vous êtes juriste ?** Lisez d'abord le **[mode d'emploi](MODE-EMPLOI.md)** : installation pas à pas, accès à donner à Claude, temps à prévoir et lecture du rapport. Aucune connaissance informatique n'est nécessaire. Aussi en [néerlandais](HANDLEIDING.md), [allemand](ANLEITUNG.md) et [anglais](USER-GUIDE.md).

[Français](README.fr.md) · [Nederlands](README.nl.md) · [Deutsch](README.de.md) · [English](README.en.md)

## Ce qu’il fait

- Inventorier sources, occurrences et renvois ; vérifier les champs réellement établis.
- Chercher dans les sources officielles, puis contrôler le texte obtenu.
- Comparer les citations dans leur langue et examiner séparément les ellipses/adaptations.
- Signaler les erreurs confirmées et les limites d’accès sans inventer d’identifiant.
- Produire un rapport Markdown ; PDF si les outils de génération et d’inspection sont disponibles.

Pour un arrêt du Conseil d’État belge dont le numéro est connu, la recherche avancée officielle par numéro est prioritaire. Une panne du formulaire est un échec technique, jamais une preuve d’inexistence. Couverture annoncée depuis septembre 1994, régime particulier étrangers et asymétrie juriDict FR/NL sont conservés dans le module.

## Installation et usage

La procédure détaillée pour les juristes figure dans le [mode d'emploi](MODE-EMPLOI.md) ; ce qui suit s'adresse aux utilisateurs techniques.


Télécharger l’archive de la version dans les publications GitHub et extraire le dossier `audit-citations-juridiques-be-eu`. Dans Codex, placer ce dossier dans `~/.codex/skills/` (ou dans le dossier `skills` du CODEX_HOME configuré). Le fichier d’entrée doit être `audit-citations-juridiques-be-eu/SKILL.md`. Dans Claude Code, placer ce dossier dans `~/.claude/skills/` (tous les projets) ou dans `.claude/skills/` d’un projet ; dans l’application Claude, importer l’archive zip du dossier depuis les réglages des compétences (Skills). Dans un autre hôte compatible, utiliser son mécanisme de chargement de skills en conservant les sous-dossiers.

Exemple de demande :

> Utilise audit-citations-juridiques-be-eu pour auditer les références et citations de ce document. Conserve les originaux, indique les sources réellement consultées et distingue les vérifications incomplètes des erreurs.

Préciser le périmètre, les documents de contexte et, lorsqu’elle compte, la date juridique pertinente. Les règles du skill sont rédigées en français ; les langues de travail sont FR/NL/DE/EN. L’accès aux sources dépend des outils de recherche et de navigation de l’agent. La lecture des PDF/DOCX et la production de fichiers nécessitent les outils correspondants. PyYAML n’est pas nécessaire pour utiliser la méthode documentaire.

## Rapport lisible

Un [générateur de rapport](templates/report-rendering.md) en français, néerlandais, allemand ou anglais fournit une présentation PDF et Markdown régulière, avec des libellés compréhensibles par un juriste. Le PDF requiert Python 3.10+ et ReportLab (`pip install -r requirements.txt`, qui installe aussi pypdf pour les tests) ; le générateur met en page des conclusions déjà établies. Il ne réalise pas les recherches.

## Validation et limites

Voir [VALIDATION.md](VALIDATION.md) pour les essais exécutés, les limites et les protocoles. Les recherches réelles et simulations sont séparées ; aucun taux global de fiabilité n’est revendiqué. La bêta ne constitue pas une certification générale V1. Les notices, extraits indexés et tables historiques ne valent pas texte intégral d’un arrêt. Un contrôle humain reste nécessaire avant usage professionnel.

## Contenu et licence

Instructions : [SKILL.md](SKILL.md). Modules : `references/`. Convention de données : [schemas/citation-record.md](schemas/citation-record.md). Modèle de rapport : `templates/`.

Documentation originale sous CC BY-NC-SA 4.0 ; code Python (`scripts/`, `tests/`) sous [PolyForm Noncommercial 1.0.0](LICENSE-CODE.md). Voir [LICENSE](LICENSE). Les sources externes citées conservent leur régime propre. Le dépôt ne redistribue ni les ouvrages de test, ni les PDF juridictionnels, ni les journaux privés de recherche. Maintenu sous le compte GitHub `marjoas-star` ; contributions décrites dans [CONTRIBUTING.md](CONTRIBUTING.md).

## Participer aux essais

Juristes volontaires : [guide des bêta-testeurs](tests/beta/guide.md) et [fiche de retour](tests/beta/fiche-retour.md). Un parcours accompagné permet de participer sans installation.
