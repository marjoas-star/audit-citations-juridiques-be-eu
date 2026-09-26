# Formulaire de retour d'expérience — textes à copier dans Google Forms

Quatre formulaires identiques (FR, NL, DE, EN), tous associés à **la même feuille Google Sheets** (un onglet par langue). Créés le 26 septembre 2026 par un script Google Apps Script dans le compte du mainteneur ; adresses publiques (reprises dans `scripts/render_report.py`, `FEEDBACK_FORMS`) :

- FR : https://docs.google.com/forms/d/e/1FAIpQLSfQPQXVYSUUx5HGUq20m-ukle7YhquYHlJlACBjdg8oP3EQ6w/viewform
- NL : https://docs.google.com/forms/d/e/1FAIpQLSdGEC1njpDohmjYCASNJkWZXOCVrlEYciUxdvNY9QvGGyvTEA/viewform
- DE : https://docs.google.com/forms/d/e/1FAIpQLScTwVeTDbksjMzbX2lJ-7Vnc7JcOJOzoC-_EjmsCMBzoLHrPQ/viewform
- EN : https://docs.google.com/forms/d/e/1FAIpQLSfjMg3pOWrlxo6dnVdRbHvz0nSqQSnizGY8b4lv_lHQ6HURFQ/viewform

Pour les recréer à l'identique, recopier les textes ci-dessous.

Réglages communs dans Google Forms :
- Paramètres › Réponses : **ne pas** collecter les adresses e-mail ; **ne pas** exiger de connexion ; ne pas limiter à une réponse.
- Réponses › « Associer à Sheets » : la première fois, créer la feuille « Retours audit-citations » ; pour les autres langues, choisir « Sélectionner une feuille de calcul existante ».
- Types de questions : Q1 « Choix multiples » (obligatoire) ; Q2 « Liste déroulante » (obligatoire) ; Q3 « Réponse courte » ; Q4, Q5, Q6 « Paragraphe » ; Q7 « Réponse courte » (facultative).

---

## Français

**Titre** : Audit des citations juridiques — votre retour

**Description** :
Merci de prendre deux minutes pour nous dire comment s'est passé l'audit. Chaque problème signalé est vérifié sur la source officielle puis ajouté aux tests du skill, pour qu'il ne se reproduise pas.
⚠️ Ne collez jamais de document confidentiel ni de donnée relative à un client : la référence en cause et la source officielle suffisent.
Ce formulaire est anonyme. Si vous indiquez une adresse e-mail (facultatif), elle sert uniquement à vous recontacter au sujet de ce signalement et elle est effacée une fois le signalement traité.

**Q1. Votre retour concerne…**
- Tout a bien fonctionné
- Une erreur que le rapport n'a pas détectée
- Une fausse alerte (le rapport signale une erreur qui n'en est pas une)
- Une référence ou un contenu inventé par le rapport
- L'installation ou l'utilisation du skill
- Une suggestion

**Q2. Où avez-vous utilisé le skill ?**
- Claude Cowork (application de bureau)
- Claude (autre : navigateur web, application mobile…)
- ChatGPT
- Autre

**Q3. Version du skill** (elle figure à la fin du rapport, sous « Version du skill »)

**Q4. Référence en cause**, telle qu'elle figure dans votre document (par ex. « C. const., [date], n° [numéro], B.[point] » ou « note 12 »)

**Q5. Ce que dit le rapport, et ce qui est correct selon vous** — si possible avec le lien vers la source officielle (Justel, EUR-Lex, Conseil d'État, Cour constitutionnelle, HUDOC…)

**Q6. Commentaire libre**

**Q7. Adresse e-mail (facultatif)**, si vous acceptez d'être recontacté(e)

**Message de confirmation** : Merci ! Votre retour sera examiné. Si le skill vous a été utile et que vous avez un compte GitHub, une étoile sur la page du projet aide à le faire connaître.

---

## Nederlands

**Titel**: Controle van juridische verwijzingen — uw feedback

**Beschrijving**:
Bedankt om twee minuten te nemen om ons te laten weten hoe de controle verliep. Elk gemeld probleem wordt nagekeken in de officiële bron en daarna toegevoegd aan de tests van de skill, zodat het zich niet herhaalt.
⚠️ Plak nooit een vertrouwelijk document of gegevens over een cliënt: de betrokken verwijzing en de officiële bron volstaan.
Dit formulier is anoniem. Als u een e-mailadres opgeeft (facultatief), wordt het uitsluitend gebruikt om u over deze melding te contacteren en gewist zodra de melding is afgehandeld.

**V1. Uw feedback gaat over…**
- Alles werkte goed
- Een fout die het rapport niet heeft opgemerkt
- Een vals alarm (het rapport meldt een fout die er geen is)
- Een verwijzing of inhoud die het rapport heeft verzonnen
- De installatie of het gebruik van de skill
- Een suggestie

**V2. Waar hebt u de skill gebruikt?**
- Claude Cowork (desktopapp)
- Claude (andere: webbrowser, mobiele app…)
- ChatGPT
- Andere

**V3. Versie van de skill** (vermeld aan het einde van het rapport, onder „Versie van de skill“)

**V4. Betrokken verwijzing**, zoals ze in uw document staat (bv. „GwH [datum], nr. [nummer], B.[punt]“ of „voetnoot 12“)

**V5. Wat het rapport zegt, en wat volgens u juist is** — indien mogelijk met de link naar de officiële bron (Justel, EUR-Lex, Raad van State, Grondwettelijk Hof, HUDOC…)

**V6. Vrije opmerking**

**V7. E-mailadres (facultatief)**, als u gecontacteerd mag worden

**Bevestigingsbericht**: Bedankt! Uw feedback wordt bekeken. Was de skill nuttig en hebt u een GitHub-account? Een ster op de projectpagina helpt om hem bekend te maken.

---

## Deutsch

**Titel**: Prüfung juristischer Zitate — Ihre Rückmeldung

**Beschreibung**:
Vielen Dank, dass Sie sich zwei Minuten Zeit nehmen, um uns mitzuteilen, wie die Prüfung verlaufen ist. Jedes gemeldete Problem wird anhand der amtlichen Quelle überprüft und anschließend in die Tests des Skills aufgenommen, damit es sich nicht wiederholt.
⚠️ Fügen Sie niemals ein vertrauliches Dokument oder Mandantendaten ein: Die betroffene Fundstelle und die amtliche Quelle genügen.
Dieses Formular ist anonym. Wenn Sie eine E-Mail-Adresse angeben (freiwillig), wird sie ausschließlich verwendet, um Sie zu dieser Meldung zu kontaktieren, und nach Bearbeitung der Meldung gelöscht.

**F1. Ihre Rückmeldung betrifft…**
- Alles hat gut funktioniert
- Einen Fehler, den der Bericht nicht erkannt hat
- Einen Fehlalarm (der Bericht meldet einen Fehler, der keiner ist)
- Eine vom Bericht erfundene Fundstelle oder einen erfundenen Inhalt
- Die Installation oder Nutzung des Skills
- Einen Vorschlag

**F2. Wo haben Sie den Skill verwendet?**
- Claude Cowork (Desktop-App)
- Claude (andere: Webbrowser, mobile App…)
- ChatGPT
- Andere

**F3. Version des Skills** (steht am Ende des Berichts unter „Version des Skills“)

**F4. Betroffene Fundstelle**, wie sie in Ihrem Dokument steht (z. B. „VerfGH, [Datum], Nr. [Nummer], B.[Punkt]“ oder „Fußnote 12“)

**F5. Was der Bericht sagt und was Ihrer Ansicht nach richtig ist** — wenn möglich mit dem Link zur amtlichen Quelle (Justel, EUR-Lex, Staatsrat, Verfassungsgerichtshof, HUDOC…)

**F6. Freier Kommentar**

**F7. E-Mail-Adresse (freiwillig)**, falls Sie mit einer Kontaktaufnahme einverstanden sind

**Bestätigungsnachricht**: Vielen Dank! Ihre Rückmeldung wird geprüft. War der Skill nützlich und haben Sie ein GitHub-Konto? Ein Stern auf der Projektseite hilft, ihn bekannt zu machen.

---

## English

**Title**: Legal citation audit — your feedback

**Description**:
Thank you for taking two minutes to tell us how the audit went. Every reported problem is checked against the official source and then added to the skill's tests, so that it does not happen again.
⚠️ Never paste a confidential document or client data: the reference concerned and the official source are enough.
This form is anonymous. If you give an email address (optional), it is used only to contact you about this report and is deleted once the report has been handled.

**Q1. Your feedback is about…**
- Everything worked well
- An error the report did not detect
- A false alert (the report flags an error that is not one)
- A reference or content invented by the report
- Installing or using the skill
- A suggestion

**Q2. Where did you use the skill?**
- Claude Cowork (desktop app)
- Claude (other: web browser, mobile app…)
- ChatGPT
- Other

**Q3. Skill version** (shown at the end of the report, under "Skill version")

**Q4. Reference concerned**, as it appears in your document (e.g. "Const. Court, [date], No. [number], B.[point]" or "footnote 12")

**Q5. What the report says, and what you believe is correct** — if possible with the link to the official source (Justel, EUR-Lex, Council of State, Constitutional Court, HUDOC…)

**Q6. Any other comment**

**Q7. Email address (optional)**, if you agree to be contacted

**Confirmation message**: Thank you! Your feedback will be reviewed. If the skill was useful and you have a GitHub account, a star on the project page helps others discover it.
