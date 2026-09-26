# Handleiding voor juristen

[Français](MODE-EMPLOI.md) · [Nederlands](HANDLEIDING.md) · [Deutsch](ANLEITUNG.md) · [English](USER-GUIDE.md)

Deze handleiding is bedoeld voor juristen die de verwijzingen in een document door Claude willen laten controleren. Informaticakennis is niet nodig. De menu's van de Claude-app veranderen geregeld: wijkt een benaming lichtjes af, zoek dan naar de term die er het dichtst bij ligt.

## 1. Waarvoor dient deze skill

U bezorgt Claude een juridisch document (conclusies, nota, artikel, advies, memorie…). Claude:

- spoort alle verwijzingen en citaten op;
- controleert elk ervan in de officiële bronnen (EUR-Lex, CURIA, HUDOC, Belgisch Staatsblad, Justel, Raad van State, Grondwettelijk Hof, JUPORTAL, parlementaire voorbereiding…) en, voor de rechtsleer, in universitaire catalogi en repositories;
- gaat na of de citaten tussen aanhalingstekens de tekst getrouw weergeven, ook wanneer er passages zijn weggelaten;
- bezorgt u een verslag: te maken correcties, punten die u zelf moet nagaan, bevestigde verwijzingen, met links naar de geraadpleegde bronnen.

Wat Claude **niet doet**: het beoordeelt de kwaliteit van uw argumentatie niet (tenzij u daar uitdrukkelijk om vraagt), het omzeilt geen abonnement of betaalde toegang, en het verzint nooit een nummer of een ECLI. Wanneer Claude iets niet kan controleren, zegt het dat: **"niet verifieerbaar" betekent niet "fout".**

## 2. Wat u nodig hebt

- **Claude Cowork**, beschikbaar met de betalende abonnementen (Pro, Max, Team, Enterprise), en bij voorkeur de **Claude-desktopapp** (Mac of Windows) op uw computer: die levert de browser die de skill nodig heeft voor verschillende officiële websites (punt 4).
- Het bestand van de skill, te downloaden met één klik: **[de laatste versie downloaden](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/releases/latest/download/audit-citations-juridiques-be-eu.zip)**. Deze link geeft altijd de meest recente versie. U kunt ook via de [Releases-pagina van de repository](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/releases) gaan, rubriek "Assets" (niet het bestand dat eindigt op `-complet`, dat voor het onderhoud bestemd is). **Pak het archief niet uit.**
  - **Op een Mac met Safari** wordt het bestand automatisch uitgepakt en krijgt u een map. Twee oplossingen: rechtsklik op de map › **Comprimeer "audit-citations-juridiques-be-eu"**, wat opnieuw een bruikbaar `.zip`-bestand oplevert; of, voorgoed, **Safari › Instellingen › Algemeen** en schakel **"Open 'veilige' bestanden na downloaden"** uit. Chrome en Firefox pakken niet uit.
- Uw document in pdf, Word of tekst. Een gescande pdf (een afbeelding zonder tekst) is moeilijker te lezen: gebruik bij voorkeur de Word-versie of een "tekst"-pdf.

De skill werkt ook in een gewoon Claude-gesprek en in Claude Code; de instellingen zijn vergelijkbaar (zie het einde van punt 3).

## 3. De skill installeren (eenmalig)

1. Open in de Claude-app **"Settings › Capabilities"** (Instellingen › Mogelijkheden) en schakel **"Code execution and file creation"** (Code uitvoeren en bestanden aanmaken) in. Zonder die optie werken skills niet.
2. Open **"Customize"** (Personaliseren, in de linkerzijbalk) › **"Skills"**.
3. Klik op **+**, vervolgens op **"Create skill"** (Skill aanmaken) en daarna op **"Upload a skill"** (Een skill uploaden).
4. Kies het gedownloade `.zip`-archief.
5. Controleer of de skill **audit-citations-juridiques-be-eu** in de lijst verschijnt en ingeschakeld is.

De skill is dan beschikbaar in Cowork en in gewone gesprekken. Officiële hulp (in het Engels): [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

**In Claude Code** (tabblad "Code" van de desktopapp) is de eenvoudigste manier het aan Claude te vragen: "Installeer voor al mijn projecten de skill uit de GitHub-repository marjoas-star/audit-citations-juridiques-be-eu (laatst gepubliceerde versie)."

### Gebruikt u ChatGPT in plaats van Claude?

De skill volgt een open formaat dat ook ChatGPT aanvaardt. **Hij werd nog niet met ChatGPT getest**: uw feedback is bijzonder welkom.

- **Beschikbaarheid**: volgens OpenAI zijn skills beschikbaar in ChatGPT **Business, Enterprise, Healthcare en Edu**. De beheerder van de werkruimte moet skills en het uploaden ervan toestaan ("Enable skills", "Enable skill uploading").
- **Importeren**: zijbalk › **Plugins** › tabblad **Skills** › **Create** › **Upload from your computer**, en kies hetzelfde `.zip`-bestand. ChatGPT scant de skill voordat hij beschikbaar wordt; hij kan als "Needs Review" worden gemarkeerd.
- **Gebruik**: voer de audit uit in **ChatGPT Work**, bij voorkeur in de **desktopapp** (lokaal werk, met de browser van uw computer). Op het web draait Work op de servers van OpenAI: EUR-Lex, CURIA en de Raad van State kunnen dan verbindingen weigeren, zoals bij Claude in de cloud.
- De voorbeeldvraag van punt 5 kan ongewijzigd worden gebruikt.

Officiële hulp: [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), [ChatGPT Work](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

## 4. De toegang die Claude nodig heeft

Dit is het belangrijkste punt: **de skill is maar zo goed als de bronnen die hij kan openen.**

| Toegang | Waarvoor dient ze | Waar inschakelen | Als ze ontbreekt |
|---|---|---|---|
| **"Code execution and file creation"** (Code uitvoeren en bestanden aanmaken) | de skill laten werken, het pdf-verslag aanmaken | "Settings › Capabilities" (Instellingen › Mogelijkheden) | de skill wordt niet geladen |
| **"Web search"** (Zoeken op het web) | arresten, wetten en artikelen vinden | inbegrepen in Cowork (de beheerder van een organisatie kan ze hebben uitgeschakeld); in een gewoon gesprek: knop **+** van het invoerveld › **"Web search"** (Zoeken op het web) | **audit onmogelijk** |
| **"Built-in browser"** (Ingebouwde browser) | websites openen die verbindingen vanaf servers weigeren: EUR-Lex, CURIA, HUDOC, Raad van State | "Settings › **Cowork** › **Preferred browser**" (Instellingen › Cowork › Voorkeursbrowser) › **"Built-in browser"** (Ingebouwde browser); de desktopapp **open en verbonden** laten tijdens de audit | deze bronnen worden slechts gedeeltelijk of helemaal niet gecontroleerd |
| **Gekoppelde map** (facultatief) | het document lezen en het verslag rechtstreeks op uw computer opslaan | wanneer Cowork er de eerste keer om vraagt, de betrokken map toestaan | het document bij het gesprek voegen en het verslag downloaden |

**Waarom de browser zo belangrijk is.** Cowork werkt standaard op servers van Anthropic. Verschillende officiële websites (EUR-Lex, CURIA, Raad van State) blokkeren echter verbindingen die van computerservers komen, en eenvoudige leestools krijgen van die websites een lege pagina. De ingebouwde browser werkt daarentegen in de desktopapp, op uw computer: die websites aanvaarden hem normaal wel. Claude meldt een geblokkeerde website altijd als een toegangsprobleem, nooit als het ontbreken van de bron.

Vóór de start controleert Claude zelf zijn toegang. Ontbreekt er iets, dan zegt Claude het u en legt het uit wat u moet doen, nog vóór de opzoekingen beginnen.

### Voor de beheerder van een organisatie (Team, Enterprise)

Te bezorgen aan de persoon die uw Claude-account beheert:

- **"Organization settings › Cowork"** (Organisatie-instellingen › Cowork): Cowork en de **ingebouwde browser** inschakelen (standaard uitgeschakeld bij Enterprise);
- **"Organization settings › Capabilities"** (Organisatie-instellingen › Mogelijkheden): **"Skills"**, **"Code execution and file creation"** (Code uitvoeren en bestanden aanmaken) en **"Web search"** (Zoeken op het web) inschakelen;
- in **"Capabilities › Code execution"** (Mogelijkheden › Code uitvoeren): als de netwerktoegang beperkt is (standaard het geval bij Enterprise), minstens de volgende domeinen toestaan, die gebruikt worden om officiële teksten te downloaden: `eur-lex.europa.eu`, `data.europa.eu`, `curia.europa.eu`, `infocuria.curia.europa.eu`, `hudoc.echr.coe.int`, `ks.echr.coe.int`, `www.ejustice.just.fgov.be`, `juportal.be`, `www.const-court.be`, `www.raadvst-consetat.be`, `www.lachambre.be`, `www.dekamer.be`, `www.senate.be`, `www.edpb.europa.eu`, `orbi.uliege.be`, `dial.uclouvain.be`, `api.crossref.org`.

Een instelling geldt pas in een **nieuwe** taak of een nieuw gesprek. Referenties (in het Engels): [Cowork voor Team en Enterprise](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans), [ingebouwde browser](https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork).

## 5. Een audit starten

1. Open de Claude-desktopapp en start een **nieuwe Cowork-taak** (kies "Cowork" in het invoerveld).
2. Voeg uw document toe (paperclip of slepen en neerzetten), of geef de locatie ervan in een gekoppelde map aan.
3. Kopieer deze vraag en pas ze zo nodig aan:

> Gebruik de skill audit-citations-juridiques-be-eu om alle verwijzingen en citaten in het bijgevoegde document te controleren. Stel een verslag op in het Nederlands, als pdf. Het document situeert zich op 1 maart 2024.

Vervang de datum door die van uw document (datum van opstelling, of de datum waarop het recht moet worden beoordeeld). Laat u ze weg, dan leidt Claude ze af uit het document of controleert het, bij gebrek daaraan, het vandaag geldende recht, en zegt het u dat.

Nuttige preciseringen, toe te voegen als ze op u van toepassing zijn:

- **de reikwijdte**: "alleen de voetnoten van hoofdstuk 2", "alleen de rechtspraak";
- **de juridische peildatum**: "het document plaatst zich op 1 januari 2024" (nuttig om een wet te controleren in haar toenmalige versie);
- **de taal van het verslag**: Frans, Nederlands, Duits of Engels (de pdf wordt opgemaakt in de taal die u kiest);
- **de grond van de zaak**: wilt u ook weten of de bronnen uw beweringen werkelijk ondersteunen, vraag het dan uitdrukkelijk; die controle gebeurt niet standaard.

## 6. Hoe lang het duurt

Elke bron wordt werkelijk geopend en gelezen, soms langs verschillende wegen: de audit gebeurt dus niet ogenblikkelijk, maar blijft snel.

- Reken op **ongeveer een minuut per afzonderlijke bron, vaak minder**, meer voor rechtsleer, oudere beslissingen of trage websites.
- Ter illustratie, tijdens de tests in Cowork: een uittreksel met 16 voetnoten die naar 12 bronnen verwijzen, werd in enkele minuten gecontroleerd.
- Een twaalftal bronnen: ongeveer 5 à 15 minuten. Vanaf een vijftigtal is het comfortabeler hoofdstuk per hoofdstuk te werken.

Nadat Claude uw document heeft gelezen, meldt het het aantal bronnen, de **juridische peildatum** waarop het de teksten controleert (de datum die u opgaf, of een datum die het uit het document afleidt) en een geschatte duur. **Past die datum niet, antwoord dan gewoon**, bijvoorbeeld "controleer op 1 januari 2016": Claude houdt er rekening mee zonder alles opnieuw te doen. Daarna geeft het tussentijds de stand van zaken ("12 van de 25 bronnen gecontroleerd"). **Laat de desktopapp open en verbonden**: de Cowork-taak loopt verder op de servers, maar de ingebouwde browser heeft de app nodig. U kunt intussen iets anders doen en later terugkomen. Stuur de vraag niet opnieuw: dan begint het werk van voren af aan.

Een lange audit verbruikt een aanzienlijk deel van uw gebruiksquotum (**"Settings › Usage"** (Instellingen › Gebruik)). Voor een omvangrijk document kunt u het verbruik beter spreiden door hoofdstuk per hoofdstuk te werken.

## 7. Het verslag lezen

Het verslag begint met **wat u moet onthouden** en de **noodzakelijke correcties**, en behandelt daarna elke verwijzing in detail, met links naar de geraadpleegde bronnen.

| Vermelding | Betekenis |
|---|---|
| **Verwijzing gecontroleerd** | de bron bestaat en stemt overeen met wat u schreef |
| **Verwijzing gecontroleerd · citaat: kleine afwijking** (of "onjuist") | de bron klopt, maar de tekst tussen aanhalingstekens stemt niet precies overeen |
| **Verwijzing geïdentificeerd, correctie nodig** | het is wel degelijk de juiste bron, maar een element is fout (datum, nummer, ECLI, artikel…); de correctie wordt vermeld |
| **Gedeeltelijk gecontroleerd** | sommige elementen zijn bevestigd, andere konden niet worden bevestigd |
| **Niet controleerbaar met de toegankelijke bronnen** | de bron kon noch bevestigd noch uitgesloten worden (betaalde toegang, geblokkeerde website, niet-gedigitaliseerd werk): **zelf na te gaan, dit is geen vastgestelde fout** |
| **Verwijzing niet teruggevonden of tegenstrijdigheid vastgesteld** | een officiële bron spreekt de verwijzing tegen: met voorrang te onderzoeken |

Het belang van elke correctie wordt aangegeven: **kritieke prioriteit**, **belangrijke correctie**, **kleine correctie** of **informatie**. Bij elke correctie staat de passage uit de bron die ze staaft: u kunt ze met één klik controleren.

Het verslag is een hulpmiddel: **lees de correcties na voordat u ze overneemt**, zeker in een procedurestuk.

## 8. Vertrouwelijkheid

- Uw document wordt door Claude verwerkt volgens de voorwaarden van uw abonnement of van uw organisatie.
- Om de verwijzingen te controleren stuurt Claude **verwijzingen en korte fragmenten** (rolnummer of nummer van een arrest, titel van een artikel, geciteerde zin) naar zoekmachines en officiële websites. De skill is er niet op gericht uw document zelf door te sturen.
- Voor een dossier dat onder het beroepsgeheim valt: ga na of het gebruik van de tool door uw organisatie is toegestaan, of verwijder eerst de namen van de partijen. De audit heeft betrekking op de verwijzingen, niet op de feiten van het dossier.

## 9. Vaak voorkomende problemen

- **Claude antwoordt zonder de skill te gebruiken.** Vermeld de naam ervan in de vraag ("gebruik de skill audit-citations-juridiques-be-eu") en controleer of hij ingeschakeld is (punt 3).
- **Bijna alles is "niet verifieerbaar".** Het zoeken op het web is waarschijnlijk uitgeschakeld, of een essentiële website is geblokkeerd. Schakel het in en probeer opnieuw in een nieuwe taak.
- **De Europese bronnen of die van de Raad van State blijven "gedeeltelijk".** De ingebouwde browser is niet ingeschakeld, of de desktopapp werd tijdens de audit gesloten (punt 4).
- **Geen pdf, alleen tekst.** Het uitvoeren van code is niet ingeschakeld, of de omgeving laat niet toe bestanden aan te maken. De inhoud van het verslag blijft dezelfde.
- **Een website vraagt te bewijzen dat u een mens bent ("CAPTCHA").** Claude omzeilt die beveiligingen nooit: het zoekt een andere officiële weg of meldt de beperking.
- **Het document is zeer lang.** Vraag een audit per hoofdstuk; elk verslag blijft gedateerd en op zichzelf staand.

## 10. Uw mening geven

De skill wordt beter dankzij de feedback van de juristen die hem gebruiken. Met een formulier van twee minuten, **zonder account**, kunt u melden:

- een fout die het verslag niet heeft opgemerkt;
- een vals alarm of een onduidelijke conclusie;
- een verwijzing die volgens u verzonnen is;
- een probleem bij de installatie of het gebruik;
- of gewoon dat alles goed werkte.

👉 **[Feedbackformulier](https://docs.google.com/forms/d/e/1FAIpQLSdGEC1njpDohmjYCASNJkWZXOCVrlEYciUxdvNY9QvGGyvTEA/viewform)** — de link staat ook aan het einde van elk verslag, in de taal van het verslag.

Vermeld de betrokken verwijzing en, indien mogelijk, de link naar de officiële bron die het juiste antwoord toont. **Plak nooit een vertrouwelijk document of gegevens over een cliënt.** Elk bevestigd probleem wordt verbeterd en aan de tests van de skill toegevoegd, zodat het zich niet herhaalt.

Hebt u een GitHub-account en bewijst de skill u diensten? Een ster ⭐ op de [projectpagina](https://github.com/marjoas-star/audit-citations-juridiques-be-eu) helpt andere juristen hem te ontdekken.
