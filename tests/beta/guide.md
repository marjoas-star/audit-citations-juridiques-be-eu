# Guide des bêta-testeurs

Audit des citations juridiques — Belgique, Union européenne et CEDH  
Campagne exploratoire · Consignes du 24 septembre 2026 · Version de départ : 0.5.0-beta.2

## Votre mission

Vérifier si l’outil retrouve les bonnes sources, contrôle correctement les références et les citations, et produit un rapport utile à un juriste. Nous cherchons autant les conclusions justes que les erreurs, les oublis et les difficultés d’utilisation. Un avis favorable sans exemple est moins utile qu’un retour précis sur une seule référence.

Vous n’avez pas à programmer, à calculer des statistiques ou à certifier le skill. Pour un premier essai, choisissez un extrait de 2 à 5 pages contenant environ 5 à 10 références dans une matière et une langue que vous maîtrisez. Ce format est une suggestion pratique, pas une obligation.

## Deux façons de participer

**Parcours accompagné, conseillé pour commencer.** Vous transmettez l’extrait au coordinateur qui vous a invité. Il organise l’exécution et vous remet le rapport intact. Vous établissez votre propre contrôle avant de lire ce rapport. Aucune installation n’est nécessaire de votre côté.

**Parcours autonome.** Vous utilisez le skill dans un environnement compatible, avec les outils de recherche et de lecture nécessaires. Les instructions d’installation figurent dans le [dépôt](https://github.com/marjoas-star/audit-citations-juridiques-be-eu). Conservez la version utilisée et le nom du modèle. Signalez si vous n’avez pas pu charger le skill ou accéder au web : c’est un retour utile, pas un échec personnel. L’installation du connecteur GitHub ne signifie pas, à elle seule, que le skill est chargé.

## Avant l’essai : préparez votre propre contrôle

1. Choisissez un document public, fictif ou dont l’utilisation dans l’environnement de test est autorisée. Un extrait d’ouvrage peut rester privé ; ne le publiez pas dans une discussion GitHub. Pour un dossier professionnel, utilisez une version appropriée au partage et aux outils retenus.
2. Numérotez les références de l’extrait et notez leur page ou leur note de bas de page. Incluez celles qui vous semblent correctes, pas seulement celles que vous soupçonnez.
3. Vérifiez chaque référence dans la source pertinente, officielle lorsqu’elle est accessible. Consignez : identité, éventuelle correction, lien ou pièce consultée, page ou paragraphe et limites. Pour une citation, comparez les mots et le contexte dans la langue citée.
4. Conservez ces réponses dans un fichier séparé, que vous ne joignez pas à la conversation de test. Ne donnez pas d’indice à l’outil sur les erreurs attendues.

Si vous souhaitez introduire volontairement une erreur, travaillez sur une copie clairement identifiée et conservez l’original ainsi que la liste privée des modifications. Ces cas artificiels seront distingués des erreurs présentes dans un document réel. Ne modifiez jamais un dossier de travail utilisé professionnellement pour les besoins du test.

## Lancez une première passe sans l’aider

Dans une nouvelle conversation, joignez uniquement l’extrait à examiner et les éléments de contexte nécessaires. Utilisez cette consigne :

> Utilise le skill audit-citations-juridiques-be-eu pour auditer toutes les références et citations de cet extrait. Contrôle leur identité et la fidélité des citations, en privilégiant les sources officielles. Indique précisément les corrections établies, les preuves consultées et ce qui reste non vérifiable. Conserve les références originales. Produis un rapport lisible par un juriste. Le périmètre est l’extrait joint ; il ne s’agit pas d’un examen général de l’argumentation juridique.

Ajoutez, si elle est connue et pertinente, la date juridique à laquelle le document se place. Ne demandez pas une actualisation au droit présent si vous cherchez seulement à vérifier une citation ancienne.

Conservez la première réponse complète, le rapport, la consigne et la date avant toute correction ou relance. En cas d’erreur technique, gardez le message et décrivez ce qui n’a pas fonctionné. Vous pouvez ensuite demander des améliorations, mais conservez ces reprises à part : elles ne remplacent pas le premier résultat.

## Comparez le rapport à vos propres vérifications

Pour chaque référence, répondez aux questions applicables :

- **Repérage :** la référence ou la citation a-t-elle été oubliée ?
- **Identité :** s’agit-il du bon arrêt, texte ou ouvrage ? Numéro, date, parties, auteur, édition et langue concordent-ils ?
- **Preuve :** le lien mène-t-il au document annoncé ? Le passage consulté justifie-t-il réellement la conclusion ? Une notice ou un résumé a-t-il été présenté à tort comme le texte intégral ?
- **Citation :** les mots, le locuteur et le localisateur sont-ils exacts ? Une suppression, un ajout ou une traduction modifie-t-il le sens ?
- **Correction :** la proposition du rapport est-elle fondée et assez précise pour être utilisée ? Une référence correcte a-t-elle été signalée à tort ?
- **Incertitude :** le rapport distingue-t-il une erreur, une source inaccessible et un contrôle partiel ?

Une mention « non vérifiable » n’est pas une erreur en elle-même. Si vous retrouvez la source, indiquez par quelle voie et avec quel accès : un abonnement ou un document que vous possédez peut expliquer la différence. Une conclusion identique à la vôtre, mais appuyée sur une mauvaise preuve, reste un problème à signaler.

## Donnez aussi votre avis de lecteur

Le rapport permet-il de comprendre rapidement ce qu’il faut corriger, ce qui a été vérifié et ce qui reste incertain ? Les fiches et liens permettent-ils de revenir facilement aux sources ? Relevez un passage obscur, inutilement technique ou trop affirmatif. Signalez les problèmes de mise en page. Estimez le temps de contrôle humain nécessaire et dites si l’outil vous a fait gagner du temps, avec un exemple.

## Ce que vous renvoyez

Utilisez la [fiche de retour](fiche-retour.md). Le minimum utile est :

1. Le document ou une description permettant au coordinateur d’identifier le lot, avec son périmètre.
2. La consigne exacte, la version du skill, l’environnement utilisé et la première réponse intacte ; écrivez « inconnu » lorsqu’une information manque.
3. Une appréciation pour chaque référence de votre liste, y compris les références oubliées et celles pour lesquelles vous confirmez le résultat.
4. Pour chaque désaccord : localisation, conclusion contestée, votre analyse, preuve et conséquence pratique.
5. Un bref retour sur la clarté et l’utilité du rapport.

Adressez le retour au coordinateur qui vous a invité, par le canal convenu avec lui. Ne publiez pas les documents, corrections réservées, noms de clients ni conversations complètes dans une issue publique. Aucune adresse de collecte n’est imposée par ce guide.

## Essai d’usage ou validation indépendante ?

Ce premier essai sert à améliorer le produit. Pour une validation indépendante, les cas doivent être réservés à l’avance et deux juristes doivent établir leurs réponses séparément, avant de voir celles du skill. Le coordinateur organise le rapprochement de leurs appréciations et conserve leurs désaccords initiaux. Les cas déjà utilisés pour corriger le skill ne sont pas réemployés comme preuve finale indépendante.

Si vous avez déjà lu le rapport de l’outil avant votre contrôle, indiquez-le simplement : votre retour reste utile, mais il ne sera pas présenté comme une appréciation faite à l’aveugle. La campagne formelle suit un [protocole distinct](../validation-v1/protocole.md) ; elle n’est pas réputée accomplie par la collecte de quelques avis favorables.
