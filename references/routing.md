# Routage des références

**Dernière révision des instructions : 24 septembre 2026**

## Principe

Router selon la nature réelle de la source, pas selon son apparence typographique.

Ordre recommandé : langue → identifiants → type → institution → module → fallback → vérification.

Priorité des identifiants lorsque présents : ECLI, CELEX, ELI, NUMAC, numéro d'arrêt/rôle/affaire/document parlementaire, DOI, ISBN.

> **La base qui permet de trouver n'est pas nécessairement la source qui permet de vérifier.**

## Routes principales

- législation belge → `moniteur-belge-justel.md`
- relations entre normes → `reflex.md`
- Conseil d'État belge → `conseil-etat-belgique.md`
- anciennes décisions CE → `recueils-numerises-kul.md`
- Cour constitutionnelle → `cour-constitutionnelle.md`
- Cassation / juridictions judiciaires → `juportal.md`
- travaux parlementaires fédéraux → `travaux-parlementaires-federal.md`
- travaux des entités fédérées → `travaux-parlementaires-entites-federees.md`
- droit UE → `eur-lex-legislation.md`
- CJUE / Tribunal → `cjue.md`
- CEDH → `cedh.md`
- doctrine → `doctrine.md`
- langue / traduction → toujours appliquer `language-policy.md`

## Conseil d'État belge — numéro exact

Si un numéro exact est connu, tenter en priorité la Recherche avancée officielle par numéro. Ne pas substituer juriDict ou un moteur général à cette route. Un formulaire officiel inaccessible donne `TECHNICAL_FAILURE`, pas `NOT_FOUND`.

## Législation belge

Moniteur belge pour la publication authentique ; Justel pour consolidation et historique ; RefLex pour relations et découverte.

## UE

Distinguer proposition, procédure, acte final, consolidation et rectificatif. Une proposition n'est jamais l'acte final.

## CJUE

Distinguer jugement, ordonnance, conclusions AG et autres documents. Le numéro d'affaire identifie un dossier, pas nécessairement un document unique.

## Parlement

Toujours distinguer dossier, document, rapport, amendement, texte adopté, débat et norme publiée.

## Doctrine

Résoudre d'abord les renvois internes (`op. cit.`, `ibid.`). Puis vérifier identité, localisation et citation.

## Référence composite

Scinder en plusieurs `SOURCE_RECORD` lorsque plusieurs documents distincts sont contenus dans une seule occurrence.

## Source fournie par l'utilisateur

Le fichier fourni peut vérifier texte, page et version. Le web peut compléter les métadonnées. Ne jamais confondre source fournie et source officielle sans base.
