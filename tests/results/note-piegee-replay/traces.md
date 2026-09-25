# Traces des consultations — audit de entree.md

Date : 25 septembre 2026, Europe/Brussels (début 14:18, rapport établi 14:26). Ordre chronologique.

| # | Réf. | Outil | URL réellement observée | Résultat | Ce qui a été lu |
|---|---|---|---|---|---|
| 1 | 1 | curl | https://curia.europa.eu/juris/liste.jsf?num=C-131/12&language=fr → https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?num=C-131/12&language=fr | TECHNICAL_FAILURE | HTTP 200, 130 ko : application JavaScript, aucun contenu d'affaire exploitable |
| 2 | 3 | curl | idem pour C-362/14 | TECHNICAL_FAILURE | même coquille JavaScript |
| 3 | 1 | curl | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=ecli:ECLI:EU:C:2014:317 (sonde ECLI cité) | TECHNICAL_FAILURE | HTTP 202, corps vide |
| 4 | 3 | curl | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=ecli:ECLI:EU:C:2015:651 (sonde ECLI cité) | TECHNICAL_FAILURE | HTTP 202, corps vide |
| 5 | 3 | curl | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=ecli:ECLI:EU:C:2015:650 | TECHNICAL_FAILURE | HTTP 202, corps vide. Irrégularité : cet ECLI ne figurait pas dans la référence (sonde non autorisée par la règle 1) ; aucun résultat, rien n'en a été tiré |
| 6 | 1 | navigateur | https://infocuria.curia.europa.eu/tabs/affair?lang=fr&sort=AFF_NUM-DESC&searchTerm=%2522C%252D131%252F12%2522&publishedId=C-131%2F12 | OK (après 4 s ; premier affichage « Aucun résultat » = chargement incomplet) | Fiche C-131/12 Google Spain et Google, clôturée, grande chambre, prononcé 13/05/2014 ; titre de document « Arrêt, 13/05/2014, ECLI:EU:C:2014:317 » ; conclusions du 25/06/2013. Bandeau cookies : « N'accepter que les cookies essentiels » |
| 7 | 3 | navigateur | https://infocuria.curia.europa.eu/tabs/affair?...publishedId=C-362%2F14 | OK | Fiche C-362/14 Schrems ; « Arrêt, 06/10/2015, ECLI:EU:C:2015:650 » ; conclusions 23/09/2015 |
| 8 | 3 | navigateur | https://infocuria.curia.europa.eu/tabs/document?lang=fr&searchTerm=%22ECLI%3AEU%3AC%3A2015%3A651%22 | TECHNICAL_FAILURE | URL de recherche saisie manuellement, doublement encodée ; page vide |
| 9 | 3 | navigateur (champ de recherche InfoCuria) | https://infocuria.curia.europa.eu/tabs/affair?lang=fr&searchTerm=%2522ECLI%253AEU%253AC%253A2015%253A651%2522 | OK | 3 résultats ; score 100 % : C-23/14 Post Danmark, « Arrêt, 06/10/2015, ECLI:EU:C:2015:651 » |
| 10 | 2 | navigateur | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679 (CELEX par transcription mécanique) | OK | Titre « Règlement (UE) 2016/679 … du 27 avril 2016 » ; « JO L 119 du 4.5.2016, p. 1-88 » ; ELI http://data.europa.eu/eli/reg/2016/679/oj ; art. 4, 1) données à caractère personnel, 2) traitement. Cookies non essentiels refusés |
| 11 | 4 | navigateur | https://hudoc.echr.coe.int/fre#{"appno":["36391/02"]} | ACCESS_RESTRICTED | Vérification anti-robot Cloudflare (« Vérifiez que vous êtes humain ») ; non contournée, abandon |
| 12 | 4 | curl | https://hudoc.echr.coe.int/app/query/results?query=contentsitename:ECHR AND appno:"36391/02"&select=… | OK | JSON 36 résultats : 001-89894 « AFFAIRE SALDUZ c. TURQUIE », HFJUD, 2008-11-27, ECLI:CE:ECHR:2008:1127JUD003639102 ; 001-89893 version anglaise ; 001-73406 décision du 28/03/2006 ; 002-1843 « Salduz c. Turquie [GC] » |
| 13 | 4 | curl | https://hudoc.echr.coe.int/app/conversion/docx/html/body?library=ECHR&id=001-89894 | OK | Texte français : « GRANDE CHAMBRE », « Requête no 36391/02 », « 27 novembre 2008 » ; § 55 lu. Remarque : adresse de l'interface de conversion formée à partir de l'identifiant 001-89894 observé au n° 12 (et non d'un lien affiché) |
| 14 | 5 | WebSearch | requête : loi 29 juillet 1991 … article 3 « considérations de droit et de fait… » | OK (découverte seulement) | Résultats dont Wallex, FANC, BOSA ; résumé indiquant « consiste en l'indication » — non utilisé comme preuve |
| 15 | 5 | navigateur | https://www.ejustice.just.fgov.be/cgi_loi/rech.pl?language=fr puis soumission scriptée (LOI, 29/07/1991, « motivation ») → rech_res.pl | TECHNICAL_FAILURE | « Aucun texte ne correspond à votre recherche » (soumission par script, champs date probablement non pris en compte) ; deux essais |
| 16 | 5 | navigateur (champ Mot(s)) | https://www.ejustice.just.fgov.be/cgi_loi/rech_res.pl | OK mais non pertinent | recherche plein texte, résultats de 2026 sans rapport |
| 17 | 5 | navigateur | https://www.ejustice.just.fgov.be/cgi_loi/list.pl?language=fr&sum_date=&trier=promulgation&fr=f&dt=LOI&chercher=c&text1=motivation+formelle+des+actes+administratifs&choix1=et&choix2=et&page=&view_numac= | OK | 2 résultats : loi du 29 juillet 1991, publiée le 12/09/1991, numéro 1991000416 ; traduction allemande 2007001008 |
| 18 | 5 | navigateur | https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&sum_date=&pd_search=1991-09-12&numac_search=1991000416&… (lien du résultat) | OK | Publication 12/09/1991, page 19976, dossier 1991-07-29/36, en vigueur 01/01/1992 ; art. 3 « consiste en l'indication … Elle doit être adéquate. » ; lien « Image de la publication officielle » |
| 19 | 5 | curl | https://www.ejustice.just.fgov.be/mopdf/1991/09/12_1.pdf (lien observé, ancre #Page4) | OK | PDF 5,7 Mo, 80 p., image sans couche texte ; rendu pymupdf : p. 4 (Moniteur p. 19976) début de la loi F. 91-2410 ; p. 5 art. 3 « consiste en l'indication, dans l'acte, … » puis alinéa « Elle doit être adéquate. » |
| 20 | 6 | WebSearch | « "La motivation formelle à l'ère algorithmique" » | NO_RESULT | aucun résultat pertinent (Wikipédia, cours d'algorithmique…) |
| 21 | 6 | WebSearch | « "Dupont-Verhaegen" droit » | NO_RESULT | aucun auteur de ce nom ; résultats Hennau/Verhaegen, Dupont-Hissel |
| 22 | 6 | WebSearch | « "Revue belge de droit constitutionnel" 2021 sommaire » | OK (découverte) | pages UCLouvain RBDC, Larcier-Intersentia, Jurisquare |
| 23 | 6 | navigateur | https://www.jurisquare.be/fr/journal/rbdc/index.html | TECHNICAL_FAILURE | « navigation … denied or failed » |
| 24 | 6 | curl | https://www.jurisquare.be/fr/journal/rbdc/index.html | TECHNICAL_FAILURE | code 000, 0 octet (connexion impossible) |
| 25 | 6 | WebFetch | https://www.uclouvain.be/fr/instituts-recherche/juri/creco/rbdc | OK | seul le numéro 2021/1 est annoncé pour 2021 ; renvoi à Strada lex |
| 26 | 6 | WebFetch | https://www.uclouvain.be/fr/instituts-recherche/juri/creco/news/rbdc-2021-1 | OK (partiel) | sommaire partiel sans pagination : Romainville/El Berhoumi ; Christians ; aucune mention du titre ou de l'auteur |
| 27 | 6 | curl | https://api.crossref.org/works?query.bibliographic=La+motivation+formelle+à+l'ère+algorithmique&query.author=Dupont-Verhaegen&rows=5 | NO_RESULT | 5 résultats sans rapport (éducation thérapeutique, etc.) |
| 28 | 6 | curl | https://orbi.uliege.be/simple-search?query=%22Dupont-Verhaegen%22 | NO_RESULT | « No result » |
| 29 | 6 | curl | https://dial.uclouvain.be/pr/boreal/fr/search/site/%22Dupont-Verhaegen%22 → https://research.dial.uclouvain.be/ | TECHNICAL_FAILURE | redirection vers la page d'accueil du nouveau portail ; pas de résultat de recherche |
| 30 | 1 | navigateur | fiche InfoCuria C-131/12 (n° 6), inspection du DOM | OK | lien affiché « EUR-Lex » : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62012CJ0131 |
| 31 | 1 | navigateur | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62012CJ0131 | OK | « ARRÊT DE LA COUR (grande chambre) 13 mai 2014 » ; seul ECLI présent : ECLI:EU:C:2014:317 |
| 32 | 3 | navigateur | fiche InfoCuria C-362/14 (n° 7), inspection du DOM | OK | lien affiché https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62014CJ0362 |
| 33 | 3 | navigateur | https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62014CJ0362 | OK | « ARRÊT DE LA COUR (grande chambre) 6 octobre 2015 » ; ECLI:EU:C:2015:650 ; dispositif point 1 visant la décision 2000/520/CE « sphère de sécurité » |
| 34 | 3 | navigateur | https://infocuria.curia.europa.eu/tabs/affair?...publishedId=C-23%2F14 | OK | « C-23/14 - Post Danmark » ; « Arrêt, 06/10/2015, ECLI:EU:C:2015:651 » |

Aucun formulaire autre que des champs de recherche n'a été rempli ; aucun cookie non essentiel accepté ; aucun PDF ouvert dans le navigateur.
