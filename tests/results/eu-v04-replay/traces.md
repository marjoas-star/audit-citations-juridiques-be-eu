# Journal des opérations — 25 septembre 2026

Skill lu : SKILL.md, routing.md, eur-lex-legislation.md, cjue.md, citation-record.md, report-template.md, language-policy.md. Aucun dossier de tests, corrigés, evaluation/received ou autres sorties consulté. Les seuls fichiers de sortie lus pour contrôle sont ceux du présent audit.

Les fichiers evidence/web-N.txt conservent la réponse effective complète des huit appels groupés au lecteur/moteur web, incluant requêtes, liens, échecs et localisateurs. Les identifiants de retour qu’ils contiennent sont des identifiants d’outil, pas des identifiants juridiques. Ils sont conservés comme traces et non présentés comme liens publics.

| Tentative | Opération / objet | Résultat réellement obtenu |
|---|---|---|
| SEA-01 | Recherches 2019/1024, 2024/1689 et 2023/2854 ; voir web-1 | SUCCESS / candidats officiels découverts. Extraits uniquement à ce stade |
| SEA-02 | Ouvertures de ces trois candidats ; recherches ByteDance, 2025/2050, CEPD ; web-2 | PDF JO L172 intégral exploitable ; notices EUR-Lex IA et Data Act limitées à 3 lignes, TECHNICAL_FAILURE |
| SEA-03 | Ouvertures Data Act ES, EASA, 2025/2050 PDF, CEPD PDF/page, résumé ByteDance ; recherches DGA, Meta, ECLI, annonce ; web-3 | EASA et 2025/2050 ouverts ; autres ouvertures limitées/internes. Aucun échec assimilé à NO_RESULT |
| SEA-04 | InfoCuria dossier, DGA, annonce, 2025/2050 début ; lien EASA vers acte ; recherches ECLI erroné, date CEPD ; web-4 | Annonce exploitable ; InfoCuria 0 ligne, DGA erreur interne, acte IA 3 lignes |
| SEA-05 | Lecture visa et art.1 du 2025/2050 ; ouverture autre résultat InfoCuria ; web-5 | Visa 40(13), art.1 40(4) vérifiés ; autre InfoCuria en erreur |
| SEA-06 | PDF arrêt et conclusions, liens observés dans le dossier navigateur ; résumé T1077 ; rapport annuel CEPD ; web-6 | Contrôle JavaScript pour les trois EUR-Lex ; 429 pour CEPD. Pas de texte de jurisprudence validé |
| SEA-07 | PDF CEPD depuis lien actuel de la page ouverte ; web-7 | SUCCESS : PDF 39 pages, couverture et historique établis |
| SEA-08 | DSA par ELI observé dans PDF 2025/2050 ; web-8 | Lecteur : contrôle JavaScript ; navigateur ensuite exploitable |
| SEA-09 | Navigateur Chrome pour EUR-Lex | TECHNICAL_FAILURE : Chrome indisponible ; aucun onglet créé |
| SEA-10 | Onglet dédié navigateur intégré ; Data Act HIS puis clic Informations sur le document | SUCCESS : procédure puis notice et texte français. Référence JO et dates lues |
| SEA-11 | Export du contenu d’onglet | TECHNICAL_FAILURE : fonction non prise en charge ; relevés DOM utilisés |
| SEA-12 | Navigateur InfoCuria depuis lien découvert ; liste puis Voir plus (3) | SUCCESS : dossier français et métadonnées des deux documents distincts |
| SEA-13 | Navigateur page CEPD de consultation | SUCCESS : statut, dates et lien PDF déplacé observés. Lien vers version finale aperçu, non suivi |
| SEA-14 | Navigateur IA, depuis lien découvert | SUCCESS : notice et corps HTML français ; la ligne JO de notice a une date vide, le tableau du texte indique 12.7.2024 |
| SEA-15 | Navigateur notice danoise ByteDance puis lien HTML Français fourni | SUCCESS : résumé officiel français, numéro et adoption 5.9.2023. Document distinct de la décision intégrale |
| SEA-16 | Navigateur DGA français, depuis lien découvert | SUCCESS : titre/date/numéro lus |
| SEA-17 | Navigateur DSA depuis ELI observé | SUCCESS : article 40 §§4,12,13 en français |
| SEA-18 | Téléchargement ancien PDF CEPD observé sous 2025-09 | DNS indisponible en bac à sable puis réponse 404 via accès réseau autorisé ; TECHNICAL_FAILURE / lien obsolète, aucun fichier probant |
| SEA-19 | Téléchargement PDF CEPD sous 2026-09 observé sur page | SUCCESS : 684 ko reçus ; extraction locale non effectuée car pdftotext absent. Lecture probante assurée séparément par SEA-07 |

## Relevés de navigateur

Ces relevés sont transcrits des sorties DOM/AX réellement retournées, et ne prétendent pas constituer une capture intégrale des pages. Langue française sauf CEPD anglais et notice initiale ByteDance danoise.

### Data Act — SEA-10

URL suivie et affichée : https://eur-lex.europa.eu/legal-content/FR/ALL/?uri=celex:32023R2854

- En-tête : règlement (UE) 2023/2854 du Parlement européen et du Conseil du 13 décembre 2023.
- Ligne JO : « JO L, 2023/2854, 22.12.2023, ELI: » puis lien http://data.europa.eu/eli/reg/2023/2854/oj.
- Rubrique Dates : 13/12/2023 ; date de signature.
- Tableau de tête du texte : série L ; 2023/2854 ; 22.12.2023.

### InfoCuria — SEA-12

URL de découverte ouverte : https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?jur=C&language=fr&lgrec=fr&num=C-252%2F21&td=%3BALL

- Nom : C-252/21 — Meta Platforms e.a. (Conditions générales d’utilisation d’un réseau social).
- Juridiction : Cour de justice.
- Entrée Arrêt : 04/07/2023 ; ECLI:EU:C:2023:537.
- Après Voir plus (3), entrée Conclusions : 20/09/2022 ; ECLI:EU:C:2022:704.
- Liens observés : https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=CELEX:62021CJ0252 et https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=CELEX:62021CC0252.
- Fiche : date du prononcé 04/07/2023 ; date des conclusions 20/09/2022 ; avocat général Rantos ; grande chambre.

### CEPD — SEA-13

URL : https://www.edpb.europa.eu/public-consultations/guidelines-32025-on-the-interplay-between-the-dsa-and-the-gdpr_en?page=2

- Heading : Guidelines 3/2025 on the interplay between the DSA and the GDPR.
- Statuts : Closed for feedback ; Obsolete version.
- Feedback period : 12 September — 31 October 2025 (23:59 CET).
- Lien fourni « Guidelines 3/2025 v1 » : /system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v1_en.pdf.
- Un lien final version est également présent : il n’a pas été suivi. Le nom v1 de la page ne suffit pas à fixer le numéro de version ; le PDF ouvert donne Version 1.1.

### IA — SEA-14

URL : https://eur-lex.europa.eu/legal-content/fr/ALL/?uri=CELEX%3A32024R1689

- En-tête : règlement (UE) 2024/1689 du Parlement européen et du Conseil du 13 juin 2024.
- Ligne notice : JO L, 2024/1689, , ELI ; date absente dans cette ligne.
- Corps du texte : tableau « 2024/1689 12.7.2024 ». Ce tableau est la preuve directe de la date.

### ByteDance — SEA-15

Notice découverte : https://eur-lex.europa.eu/legal-content/DA/ALL/?uri=CELEX%3A52023DMA100040

Lien HTML Français fourni et suivi : https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=OJ:C_202300552

- Résumé de la décision de la Commission ; du 5 septembre 2023 ; affaire DMA.100040 ; notifiée sous C(2023) 6102 final.
- Paragraphe avant section 1 : adoption de la décision expressément datée du 5 septembre 2023.
- Point 1 : désignation de ByteDance comme contrôleur d’accès.
- Tableau de publication : C/2023/552 ; 27.10.2023.

### DGA — SEA-16

URL : https://eur-lex.europa.eu/legal-content/fr/TXT/?uri=CELEX%3A32022R0868

En-tête : règlement (UE) 2022/868 du Parlement européen et du Conseil du 30 mai 2022 portant sur la gouvernance européenne des données et modifiant le règlement (UE) 2018/1724 (règlement sur la gouvernance des données).

### DSA — SEA-17

ELI observé dans le PDF 2025/2050 puis ouvert : http://data.europa.eu/eli/reg/2022/2065/oj ; URL finale affichée https://eur-lex.europa.eu/eli/reg/2022/2065/oj.

- Article 40 §4 : accès sur demande motivée du coordinateur aux chercheurs agréés satisfaisant au §8.
- Article 40 §12 : accès aux données publiquement accessibles sur les interfaces en ligne, chercheurs satisfaisant à certains points du §8.
- Article 40 §13 : actes délégués de la Commission sur les conditions techniques de partage en vertu des §§1 et 4.

## Registre des statuts

Les identités de source et occurrences sont séparées. T55-A et B renvoient au même SRC-55 ; T56-A et B sont des documents différents.

| Source | Occurrence | Statut occurrence | Niveau déterminant | Constat |
|---|---|---|---|---|
| SRC-54-DIR | OCC-54-DIR | VERIFIED | OFFICIAL_AUTHENTIC_PUBLICATION | Série/date/page contrôlées dans PDF JO |
| SRC-54-IA | OCC-54-IA | VERIFIED | OFFICIAL_FULL_DOCUMENT | En-tête du texte HTML |
| SRC-55 | OCC-55-A | VERIFIED | OFFICIAL_METADATA | Pas d’obligation éditoriale particulière |
| SRC-55 | OCC-55-B | VERIFIED_WITH_ANOMALY | OFFICIAL_METADATA | BIBLIOGRAPHIC_OMISSION ; MINOR ; identité VERIFIED |
| SRC-56-DEC | OCC-56-A | VERIFIED_WITH_ANOMALY | OFFICIAL_METADATA | WRONG_ADOPTION_DATE ; MAJOR ; résumé officiel ouvert |
| SRC-56-NEWS | OCC-56-B | VERIFIED | INSTITUTIONAL_FULL_DOCUMENT | Date d’annonce exacte |
| SRC-57 | OCC-57 | VERIFIED_WITH_ANOMALY | OFFICIAL_AUTHENTIC_PUBLICATION | WRONG_PROVISION_LOCATOR ; MAJOR |
| SRC-58 | OCC-58 | VERIFIED | OFFICIAL_FULL_DOCUMENT | Abréviation assumée |
| SRC-59-JUDGMENT | OCC-59 | VERIFIED_WITH_ANOMALY | OFFICIAL_METADATA | VALID_IDENTIFIER_WRONG_DOCUMENT ; MAJOR |
| SRC-60 | OCC-60 | VERIFIED_WITH_ANOMALY | INSTITUTIONAL_FULL_DOCUMENT | Date d’adoption et statut de version incorrects ; MAJOR |

Sources auxiliaires : SRC-57-DSA (OFFICIAL_FULL_DOCUMENT), SRC-59-OPINION (OFFICIAL_METADATA). Les sources principales sont identifiées, les anomalies appartiennent aux occurrences. Aucun contrôle intégral des textes non demandé ; aucun QUOTATION_RECORD de citation littérale d’ouvrage applicable à l’entrée.

Les références originales, les corrections et la preuve par champ sont conservées dans first-response.md. Les limites y sont également attachées à chaque cas. Le présent journal n’ajoute aucune correction postérieure à cette première réponse.
