# Politique linguistique

**Dernière révision des instructions : 24 septembre 2026**

## Langues natives

FR, NL, DE, EN.

Conserver séparément :

```yaml
document_language:
citation_language:
source_language:
report_language:
translation_status:
```

Ne jamais traduire ou « franciser » une référence avant de l'identifier.

## Statuts de traduction

- `ORIGINAL_OR_AUTHENTIC`
- `OFFICIAL_PARALLEL_VERSION`
- `OFFICIAL_TRANSLATION`
- `INSTITUTIONAL_TRANSLATION`
- `AUTHOR_TRANSLATION`
- `EDITORIAL_TRANSLATION`
- `MODEL_TRANSLATION`
- `MACHINE_TRANSLATION`
- `UNKNOWN`

Le mot « officiel » signifie fourni par l'institution ; il ne signifie pas nécessairement juridiquement authentique.

## Traductions d'auteur

Contrôle sémantique :

- `FAITHFUL`
- `FAITHFUL_WITH_MINOR_VARIATION`
- `PARTIALLY_FAITHFUL`
- `MISLEADING`
- `NOT_VERIFIABLE`

## juriDict

Les taxonomies FR et NL sont indépendantes. Ne jamais traduire les catégories comme des équivalents. Chercher dans chaque arbre séparément puis comparer les décisions.

Consigner aussi la couverture documentaire observée pour chaque langue. Si une borne n'a pas été consultée, la laisser non vérifiée ; ne pas transférer la borne FR à la branche NL ou inversement.
