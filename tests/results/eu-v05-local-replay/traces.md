# Traces de consultation — audit T54 à T60

Date : 25 septembre 2026, 13:56–14:05 (Europe/Brussels, UTC+02:00). Ordre chronologique.

| # | URL réellement observée | Outil | Résultat | Ce qui a été lu |
|---|---|---|---|---|
| 1 | https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32019L1024 (idem 32024R1689, 32023R2854, 32022R0868) | curl (Bash) | TECHNICAL_FAILURE | Réponses vides (4 requêtes) ; aucune conclusion tirée |
| 2 | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32019L1024 | Navigateur (navigate + javascript_tool) | OK | Notice : intitulé, « JO L 172 du 26.6.2019, p. 56-83 », ELI, « En vigueur » (T54-a) |
| 3 | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689 | Navigateur | OK | Notice : intitulé, date 13 juin 2024, « JO L, 2024/1689, 12.7.2024 », ELI, acte modifié, consolidation 27/07/2026 (T54-b) |
| 4 | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32023R2854 | Navigateur | OK | Notice : intitulé, date 13 décembre 2023, « JO L, 2023/2854, 22.12.2023 », ELI (T55) |
| 5 | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32022R0868 | Navigateur | OK | Notice : intitulé intégral, date 30 mai 2022, « JO L 152 du 3.6.2022, p. 1-44 », ELI (T58) |
| 6 | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32025R2050 | Navigateur | OK | Intitulé, C/2025/4340, « JO L, 2025/2050, 9.10.2025 », visa (« notamment son article 40, paragraphe 13 »), article premier (« conformément à l'article 40, paragraphe 4 ») ; 0 occurrence de « paragraphe 12 » (T57) |
| 7 | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32022R2065 | Navigateur | OK | DSA, article 40, §§ 4, 12 et 13 (texte affiché par défaut) (T57) |
| 8 | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62021CJ0252 | Navigateur | OK | Arrêt (grande chambre) du 4 juillet 2023, Meta Platforms Inc. e.a. c. Bundeskartellamt, C-252/21, « Identifiant ECLI: ECLI:EU:C:2023:537 » (T59) |
| 9 | https://eur-lex.europa.eu/legal-content/FR/CASE/?uri=CELEX:62021CJ0252 | Navigateur | OK (partiel) | Dossier : « Statut: En cours », Arrêt 04/07/2023 ; liste repliée, conclusions non listées à l'affichage |
| 10 | https://curia.europa.eu/juris/liste.jsf?num=C-252/21&language=fr | curl (Bash) | TECHNICAL_FAILURE | Aucune sortie exploitable |
| 11 | https://curia.europa.eu/juris/liste.jsf?num=C-252/21&language=fr → redirigé vers https://infocuria.curia.europa.eu/tabs/affair?lang=fr&sort=AFF_NUM-DESC&searchTerm=%2522C%252D252%252F21%2522&publishedId=C-252%2F21 | Navigateur | OK | Fiche : « Clôturée » ; Arrêt 04/07/2023 (ECLI:EU:C:2023:537) ; Conclusions 20/09/2022 ; AG Rantos ; grande chambre (T59). Bannière cookies non acceptée |
| 12 | https://eur-lex.europa.eu/search.html?scope=EURLEX&text=%22ECLI%3AEU%3AC%3A2022%3A704%22&lang=fr&type=quick&qid=1 | Navigateur (recherche rapide) | TECHNICAL_FAILURE | Délai dépassé (300 s) ; page « ERROR: The request could not be satisfied » |
| 13 | Requête « "ECLI:EU:C:2022:704" » | WebSearch | OK (découverte) | Résultats orientant vers conclusions AG Rantos du 20.9.2022 ; lien EUR-Lex par ECLI découvert (non utilisé comme preuve) |
| 14 | Requête « EDPB Guidelines 3/2025 interplay DSA GDPR adopted version 1.1 » | WebSearch | OK (découverte) | Liens vers pages EDPB (non utilisés comme preuve) |
| 15 | https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=ecli:ECLI:EU:C:2022:704 | Navigateur | OK | Document 62021CC0252 : « Conclusie van advocaat-generaal A. Rantos van 20 september 2022 », C-252/21, « Identifiant ECLI: ECLI:EU:C:2022:704 » (T59) |
| 16 | https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2025/guidelines-32025-interplay-between-dsa-and-gdpr_en → redirigé vers https://www.edpb.europa.eu/public-consultations/guidelines-32025-on-the-interplay-between-the-dsa-and-the-gdpr_en | Navigateur | OK | « Closed for feedback », « Obsolete version », « Feedback period 12 September - 31 October 2025 », lien vers version finale, PDF v1 (T60). Bannière cookies non acceptée |
| 17 | https://www.edpb.europa.eu/documents/guideline/guidelines-32025-on-the-interplay-between-the-dsa-and-the-gdpr_en | Navigateur | OK | « 17 September 2026 », « Final version », PDF v2, rapport de consultation (T60) |
| 18 | https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v1_en.pdf et …_v2_en.pdf | curl (Bash) | OK | PDF téléchargés dans le scratchpad (701 143 et 824 166 octets) |
| 19 | fichiers PDF locaux | Read (rendu PDF) | TECHNICAL_FAILURE | pdftoppm absent ; aucun rendu |
| 20 | https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v1_en.pdf | Navigateur | TECHNICAL_FAILURE | Le serveur a renvoyé un téléchargement ; une boîte d'enregistrement a été présentée à l'utilisateur ; la page n'a pas navigué. Non réessayé |
| 21 | fichiers PDF locaux (v1, v2) | python3 (décompression zlib des flux) | OK | v1 : « Version 1.1 », « Adopted on 11 September 2025 », « Adopted - version for public consultation », historique (1.1 = 12.9.2025, corrections mineures ; 1.0 = 11.9.2025, adoption pour consultation). v2 : « Version 2.0 », « Adopted on 17 September 2026 », « Adoption of the Guidelines after public consultation » (T60) |
| 22 | Requête « "C(2023) 6102" ByteDance DMA designation decision » | WebSearch | OK (découverte) | Lien ELI EUR-Lex C/2023/552 découvert |
| 23 | Requête « Commission designates six gatekeepers Digital Markets Act 6 September 2023 press release » | WebSearch | OK (découverte) | Lien vers annonce sur digital-markets-act.ec.europa.eu |
| 24 | https://eur-lex.europa.eu/eli/C/2023/552/oj | Navigateur | OK | Document 52023DMA100040 : « Résumé de la décision de la Commission du 5 septembre 2023 … (Affaire DMA.100040 – BYTEDANCE …) [notifiée sous le numéro C(2023) 6102 final] », « JO C, C/2023/552, 27.10.2023 » (T56-A) |
| 25 | https://digital-markets-act.ec.europa.eu/commission-designates-six-gatekeepers-under-digital-markets-act-2023-09-06_en | Navigateur | OK | Annonce « 6 September 2023 », « Today (6 September 2023) … has designated … six gatekeepers » (T56-B) |

Aucun cookie non essentiel accepté ; aucun formulaire rempli ; aucun CAPTCHA ni restriction contournés.
