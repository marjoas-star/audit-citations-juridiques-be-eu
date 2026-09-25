# Mode d'emploi pour les juristes

Ce guide s'adresse aux juristes qui veulent faire vérifier les références d'un document par Claude. Aucune connaissance informatique n'est nécessaire. Les menus de l'application Claude évoluent : si un libellé diffère légèrement, cherchez le terme le plus proche.

## 1. À quoi sert ce skill

Vous confiez à Claude un document juridique (conclusions, note, article, avis, mémoire…). Il :

- relève toutes les références et citations ;
- va vérifier chacune dans les sources officielles (EUR-Lex, CURIA, HUDOC, Moniteur belge, Justel, Conseil d'État, Cour constitutionnelle, JUPORTAL, travaux parlementaires…) et, pour la doctrine, dans les catalogues et dépôts universitaires ;
- contrôle que les citations entre guillemets reproduisent fidèlement le texte, y compris lorsque des passages ont été coupés ;
- vous remet un rapport : corrections à faire, points à vérifier vous-même, références confirmées, avec les liens vers les sources consultées.

Ce qu'il **ne fait pas** : il ne juge pas la qualité de votre argumentation (sauf si vous le demandez expressément), il ne contourne ni abonnement ni accès payant, et il n'invente jamais un numéro ou un ECLI. Quand il ne peut pas vérifier, il le dit : **« non vérifiable » ne veut pas dire « erroné ».**

## 2. Ce qu'il vous faut

- Un compte Claude sur lequel les **compétences** (« Skills ») et la **recherche web** sont disponibles. Dans une organisation (offres Team ou Enterprise), c'est l'administrateur qui les active (voir la section 4).
- Le fichier du skill : l'archive `.zip` de la dernière version, à télécharger sur la page [Releases du dépôt](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/releases) (rubrique « Assets », fichier `audit-citations-juridiques-be-eu-….zip`). **Ne décompressez pas l'archive.**
- Votre document en PDF, Word ou texte. Un PDF scanné (image sans texte) est plus difficile à lire : préférez la version Word ou un PDF « texte ».

## 3. Installer le skill (une seule fois)

### Dans l'application Claude (site claude.ai ou application de bureau)

1. Ouvrez **Paramètres › Capacités** (« Settings › Capabilities ») et activez **Exécution de code et création de fichiers** (« Code execution and file creation »). Sans cette option, les skills ne fonctionnent pas.
2. Ouvrez **Personnaliser › Skills** (« Customize › Skills »).
3. Cliquez sur **+**, puis **Créer un skill** (« Create skill »), puis **Importer un skill** (« Upload a skill »).
4. Choisissez l'archive `.zip` téléchargée.
5. Vérifiez que le skill **audit-citations-juridiques-be-eu** apparaît dans la liste et qu'il est activé.

Aide officielle : [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Dans Claude Code (onglet « Code » de l'application de bureau)

C'est l'environnement dans lequel le skill a été testé le plus complètement, parce qu'il dispose d'un navigateur intégré. Le plus simple est de le demander à Claude lui-même :

> Installe pour tous mes projets le skill qui se trouve dans le dépôt GitHub marjoas-star/audit-citations-juridiques-be-eu (dernière version publiée).

Acceptez les demandes d'autorisation qui s'affichent : il s'agit de télécharger et de copier le dossier du skill.

## 4. Les accès à donner à Claude

C'est le point le plus important : **le skill ne vaut que par les sources qu'il peut ouvrir.** Sans accès au web, il ne peut rien vérifier.

| Accès | À quoi il sert | Où l'activer | S'il manque |
|---|---|---|---|
| **Exécution de code et création de fichiers** | faire fonctionner le skill, produire le rapport PDF, lire les PDF officiels | Paramètres › Capacités | le skill ne se charge pas |
| **Recherche web** (« Web search ») | trouver les arrêts, lois et articles, et ouvrir les pages officielles | dans chaque conversation : bouton **+** en bas à gauche du champ de saisie › **Recherche web** (une coche apparaît) | **audit impossible** |
| **Navigateur** | ouvrir les sites qui refusent les outils simples (EUR-Lex, CURIA, HUDOC) | disponible dans Claude Code (onglet « Code ») ; dans l'application Claude, selon les extensions installées | ces sources ne sont vérifiées que partiellement |

Avant de commencer, Claude vérifie lui-même ces accès. S'il en manque un, il vous le dit et vous explique quoi faire, avant de lancer les recherches.

### Pour l'administrateur d'une organisation (Team, Enterprise)

À transmettre à la personne qui gère votre compte Claude :

- dans **Paramètres de l'organisation**, activer les **Skills**, l'**exécution de code et la création de fichiers** et la **recherche web** ;
- si l'accès réseau de l'exécution de code est restreint, autoriser au minimum ces domaines, utilisés pour télécharger les textes officiels : `eur-lex.europa.eu`, `data.europa.eu`, `curia.europa.eu`, `infocuria.curia.europa.eu`, `hudoc.echr.coe.int`, `ks.echr.coe.int`, `www.ejustice.just.fgov.be`, `juportal.be`, `www.const-court.be`, `www.raadvst-consetat.be`, `www.lachambre.be`, `www.dekamer.be`, `www.senate.be`, `www.edpb.europa.eu`, `orbi.uliege.be`, `dial.uclouvain.be`, `api.crossref.org`.

Un réglage n'est pris en compte que dans une **nouvelle** conversation.

Remarque : certains sites officiels (EUR-Lex, CURIA, Conseil d'État) bloquent les connexions venant de serveurs informatiques. Depuis un ordinateur personnel ou de bureau (Claude Code), ils sont généralement accessibles ; depuis un environnement « dans le cloud », ils peuvent rester fermés même après autorisation. Claude le signale alors comme une difficulté d'accès, jamais comme une absence de la source.

## 5. Lancer un audit

1. Ouvrez une **nouvelle conversation**.
2. Vérifiez que la **recherche web** est activée (bouton **+**).
3. Joignez votre document (trombone ou glisser-déposer).
4. Copiez cette demande, en l'adaptant si besoin :

> Utilise le skill audit-citations-juridiques-be-eu pour vérifier toutes les références et citations du document joint. Produis un rapport en français, en PDF.

Précisions utiles, à ajouter si elles vous concernent :

- **le périmètre** : « seulement les notes du chapitre 2 », « seulement la jurisprudence » ;
- **la date juridique** : « le document se place au 1er janvier 2024 » (utile pour vérifier une loi dans sa version de l'époque) ;
- **la langue du rapport** : français, néerlandais, allemand ou anglais (le PDF mis en page n'existe actuellement qu'en français) ;
- **le fond** : si vous voulez aussi savoir si les sources soutiennent réellement vos affirmations, demandez-le expressément ; ce contrôle n'est pas fait par défaut.

## 6. Combien de temps cela prend

**Un audit sérieux prend du temps**, parce que chaque source est réellement ouverte et lue, parfois par plusieurs voies. C'est le prix d'une vérification qui ne se fie pas aux apparences.

- Comptez **environ 1 à 3 minutes par source distincte**, davantage pour la doctrine, les décisions anciennes ou les sites lents.
- À titre d'exemple, lors des essais : 6 références ont pris 7 à 10 minutes ; 7 cas de droit européen, environ 11 minutes.
- Une vingtaine de sources : entre 20 minutes et une heure. Au-delà d'une cinquantaine, il est plus confortable de procéder par chapitre.

Après avoir lu votre document, Claude vous annonce le nombre de sources et une fourchette de durée, puis donne des points d'étape (« 12 sources sur 25 vérifiées »). **Laissez la conversation ouverte** ; vous pouvez faire autre chose et revenir. Ne relancez pas la demande : cela recommencerait le travail.

## 7. Lire le rapport

Le rapport commence par **ce qu'il faut retenir** et les **corrections nécessaires**, puis détaille chaque référence avec les liens vers les sources consultées.

| Mention | Signification |
|---|---|
| **Référence vérifiée** | la source existe et correspond à ce que vous avez écrit |
| **Référence vérifiée · citation : écart mineur** (ou « citation inexacte ») | la source est la bonne, mais le texte entre guillemets ne correspond pas exactement |
| **Référence identifiée, correction nécessaire** | c'est bien la bonne source, mais un élément est faux (date, numéro, ECLI, article…) ; la correction est indiquée |
| **Vérification partielle** | certains éléments sont confirmés, d'autres n'ont pas pu l'être |
| **Vérification impossible avec les sources accessibles** | la source n'a pu être ni confirmée ni écartée (accès payant, site bloqué, ouvrage non numérisé) : **à vérifier vous-même, ce n'est pas une erreur établie** |
| **Référence non retrouvée ou contradiction établie** | une source officielle contredit la référence : à examiner en priorité |

L'importance de chaque correction est indiquée : **priorité critique**, **correction importante**, **correction ponctuelle** ou **information**. Chaque correction est accompagnée du passage de la source qui la justifie : vous pouvez la contrôler en un clic.

Le rapport est une aide : **relisez les corrections avant de les reporter**, en particulier dans un acte de procédure.

## 8. Confidentialité

- Votre document est traité par Claude selon les conditions de votre abonnement ou de votre organisation.
- Pour vérifier les références, Claude envoie des **références et des extraits courts** (numéro d'arrêt, titre d'un article, phrase citée) aux moteurs de recherche et aux sites officiels. Le skill ne prévoit pas d'y transmettre votre document lui-même.
- Pour un dossier couvert par le secret professionnel, vérifiez que l'outil est autorisé par votre organisation, ou retirez d'abord les noms des parties : l'audit porte sur les références, pas sur les faits du dossier.

## 9. Problèmes fréquents

- **Claude répond sans utiliser le skill.** Mentionnez son nom dans la demande (« utilise le skill audit-citations-juridiques-be-eu ») et vérifiez qu'il est activé (section 3).
- **Presque tout est « non vérifiable ».** La recherche web est probablement désactivée, ou un site essentiel est bloqué. Activez-la et relancez dans une nouvelle conversation.
- **Pas de PDF, seulement du texte.** L'exécution de code n'est pas activée, ou l'environnement ne permet pas de créer des fichiers. Le contenu du rapport reste le même.
- **Un site demande de prouver qu'on est humain (« CAPTCHA »).** Claude ne contourne jamais ces protections : il cherche une autre voie officielle ou signale la limite.
- **Le document est très long.** Demandez un audit par chapitre ; chaque rapport reste daté et autonome.

## 10. Donner votre avis

Vos retours de juriste sont précieux, surtout lorsqu'une conclusion vous paraît fausse ou peu claire : utilisez la [fiche de retour](tests/beta/fiche-retour.md) ou ouvrez un « issue » sur le [dépôt GitHub](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/issues). Ne joignez jamais un document confidentiel.
