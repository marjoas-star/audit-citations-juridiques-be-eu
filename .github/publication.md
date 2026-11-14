**Version proposée par défaut — essai public avant la 1.0.**

**Installer :** téléchargez `audit-citations-juridiques-be-eu.zip` ci-dessous, sans le décompresser, et suivez la [page d'installation](https://marjoas-star.github.io/audit-citations-juridiques-be-eu/). Pour remplacer une version précédente : Paramètres › Compétences › fiche du skill › ⋮ › **Supprimer**, puis **+ Ajouter › Importer une compétence** (« Remplacer » garde l'ancien contenu). Vérifiez dans l'onglet **Contenu** › `SKILL.md` que la version est 0.9.5.

**Nouveau dans la 0.9.5** : le site du Conseil d'État a été refondu à l'automne 2026 et la « Recherche avancée » par numéro a disparu. Le skill est adapté à la nouvelle interface (constats du 14 novembre 2026) :
- **Recherche** : numéro seul dans le champ unique ; l'arrêt est identifié par le titre de la fiche, car un numéro saisi ramène aussi les arrêts qui le citent et ceux dont le numéro de rôle le contient.
- **Adresse officielle directe** : l'index de recherche est moins complet que la collection. Quand la fiche attendue n'apparaît pas, le skill peut essayer les adresses stables `/arrets/<numéro>` et `/arresten/<numéro>` ; la preuve reste l'en-tête du PDF ouvert, et une recherche sans résultat ou une réponse 404 ne prouve pas l'inexistence.
- **ECLI** relevé seulement lorsqu'il est imprimé dans le PDF (arrêts récents). **Pseudonymisation** générale depuis février 2024 : un nom de partie absent du PDF publié n'est pas signalé comme une anomalie.
- **juriDict**, ordonnances de cassation et avis : nouvelles adresses et nouvelles recherches décrites.

Les cas de test propres au nouveau site (T53-R9 à R16) restent à rejouer à l'aveugle ; voir [VALIDATION.md](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/blob/main/VALIDATION.md).

**Depuis la 0.9.4** : les sources anciennes (arrêts du Conseil d'État d'avant 1994, revues et ouvrages anciens, travaux parlementaires anciens) sont recherchées dans les numérisations publiques, notamment celles de la KU Leuven, et vérifiées sur l'image de la page.

Gratuit pour tous les juristes, y compris dans leur pratique professionnelle ; ni vente ni intégration dans un produit payant (section 3 de [LICENSE](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/blob/main/LICENSE)). Un formulaire de retour sans compte figure à la fin de chaque rapport. Aucune certification ni taux de fiabilité n'est revendiqué ; une vérification humaine reste nécessaire.

Archives : `audit-citations-juridiques-be-eu.zip` (nom permanent, 30 fichiers, à importer), la même sous `…-0.9.5.zip`, et `…-0.9.5-complet.zip` (dépôt entier). Empreintes SHA-256 jointes.
