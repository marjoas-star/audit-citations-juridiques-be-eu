# Anleitung für Juristinnen und Juristen

[Français](MODE-EMPLOI.md) · [Nederlands](HANDLEIDING.md) · [Deutsch](ANLEITUNG.md) · [English](USER-GUIDE.md)

Diese Anleitung richtet sich an Juristinnen und Juristen, die die Fundstellen eines Dokuments von Claude überprüfen lassen möchten. Informatikkenntnisse sind nicht erforderlich. Die Menüs der Claude-App ändern sich: Weicht eine Bezeichnung leicht ab, suchen Sie nach dem ähnlichsten Begriff.

## 1. Wozu dieser Skill dient

Sie übergeben Claude ein juristisches Dokument (Schriftsatz, Vermerk, Aufsatz, Gutachten, Denkschrift…). Claude:

- erfasst sämtliche Fundstellen und Zitate;
- überprüft jede einzelne in den amtlichen Quellen (EUR-Lex, CURIA, HUDOC, Belgisches Staatsblatt, Justel, Staatsrat, Verfassungsgerichtshof, JUPORTAL, parlamentarische Vorarbeiten…) und, für die Rechtslehre, in Bibliothekskatalogen und Repositorien der Universitäten;
- prüft, ob die Zitate in Anführungszeichen den Wortlaut getreu wiedergeben, auch wenn Passagen ausgelassen wurden;
- übergibt Ihnen einen Bericht: vorzunehmende Korrekturen, selbst zu prüfende Punkte, bestätigte Fundstellen, mit Links zu den eingesehenen Quellen.

Was Claude **nicht tut**: Es beurteilt nicht die Qualität Ihrer Argumentation (es sei denn, Sie verlangen dies ausdrücklich), es umgeht weder Abonnements noch kostenpflichtige Zugänge, und es erfindet niemals eine Nummer oder einen ECLI. Kann Claude etwas nicht überprüfen, sagt es dies: **„nicht überprüfbar“ bedeutet nicht „falsch“.**

## 2. Was Sie benötigen

- **Claude Cowork**, verfügbar mit den kostenpflichtigen Abonnements (Pro, Max, Team, Enterprise), und vorzugsweise die auf Ihrem Computer installierte **Claude-Desktop-App** (Mac oder Windows): Sie stellt den Browser bereit, den der Skill für mehrere amtliche Websites benötigt (Abschnitt 4).
- Die Datei des Skills, mit einem Klick herunterzuladen: **[neueste Version herunterladen](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/releases/latest/download/audit-citations-juridiques-be-eu.zip)**. Dieser Link liefert immer die aktuellste Version. Sie können auch die [Releases-Seite des Repositorys](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/releases) nutzen, Rubrik „Assets“ (nicht die Datei mit der Endung `-complet`, die für die Wartung bestimmt ist). **Entpacken Sie das Archiv nicht.**
  - **Auf einem Mac mit Safari** wird die Datei automatisch entpackt und Sie erhalten einen Ordner. Zwei Lösungen: Rechtsklick auf den Ordner › **„audit-citations-juridiques-be-eu“ komprimieren**, wodurch wieder eine verwendbare `.zip`-Datei entsteht; oder dauerhaft **Safari › Einstellungen › Allgemein** und **„Sichere“ Dateien nach dem Laden öffnen** deaktivieren. Chrome und Firefox entpacken nicht.
- Ihr Dokument als PDF-, Word- oder Textdatei. Ein eingescanntes PDF (Bild ohne Text) ist schwerer zu lesen: Verwenden Sie nach Möglichkeit die Word-Fassung oder ein „Text“-PDF.

Der Skill funktioniert auch in einer gewöhnlichen Claude-Unterhaltung und in Claude Code; die Einstellungen sind ähnlich (siehe Ende von Abschnitt 3).

## 3. Den Skill installieren (nur einmal)

1. Öffnen Sie in der Claude-App **„Settings › Capabilities“** (Einstellungen › Funktionen) und aktivieren Sie **„Code execution and file creation“** (Codeausführung und Dateierstellung). Ohne diese Option funktionieren Skills nicht.
2. Öffnen Sie **„Customize“** (Anpassen, in der linken Seitenleiste) › **„Skills“**.
3. Klicken Sie auf **+**, dann auf **„Create skill“** (Skill erstellen) und anschließend auf **„Upload a skill“** (Skill hochladen).
4. Wählen Sie das heruntergeladene `.zip`-Archiv aus.
5. Prüfen Sie, dass der Skill **audit-citations-juridiques-be-eu** in der Liste erscheint und aktiviert ist.

Der Skill steht dann sowohl in Cowork als auch in gewöhnlichen Unterhaltungen zur Verfügung. Offizielle Hilfe (auf Englisch): [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

**Eine neue Version installieren.** Laden Sie das neue Archiv herunter (gleiche Schaltfläche), öffnen Sie dann in den Einstellungen unter **Skills** die Seite des Skills, Menü **⋮** › **Ersetzen** (Option mit dem Pfeil nach oben, „Replace“ in der englischen Oberfläche) und wählen Sie die `.zip`-Datei. Die alte Version müssen Sie nicht löschen. Die installierte Version steht am Ende jedes Berichts („Version des Skills“); die Angabe „v1“ auf der Seite ist ein Zähler der App.

**In Claude Code** (Registerkarte „Code“ der Desktop-App) ist es am einfachsten, Claude darum zu bitten: „Installiere für alle meine Projekte den Skill aus dem GitHub-Repository marjoas-star/audit-citations-juridiques-be-eu (neueste veröffentlichte Version).“

### Sie verwenden ChatGPT statt Claude?

Der Skill folgt einem offenen Format, das auch ChatGPT akzeptiert. **Er wurde mit ChatGPT noch nicht getestet**: Ihre Rückmeldungen sind besonders willkommen.

- **Verfügbarkeit**: Laut OpenAI stehen Skills in ChatGPT **Business, Enterprise, Healthcare und Edu** zur Verfügung. Die Administration des Arbeitsbereichs muss Skills und deren Upload erlauben („Enable skills“, „Enable skill uploading“).
- **Import**: Seitenleiste › **Plugins** › Registerkarte **Skills** › **Create** › **Upload from your computer**, dann dieselbe `.zip`-Datei wählen. ChatGPT prüft den Skill, bevor er verfügbar wird; er kann als „Needs Review“ markiert werden.
- **Nutzung**: Führen Sie die Prüfung in **ChatGPT Work** aus, vorzugsweise in der **Desktop-App** (lokale Arbeit mit dem Browser Ihres Computers). Im Web läuft Work auf den Servern von OpenAI: EUR-Lex, CURIA und der Staatsrat können Verbindungen dann ablehnen, wie bei Claude in der Cloud.
- Die Musteranfrage aus Abschnitt 5 kann unverändert verwendet werden.

Offizielle Hilfe: [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt), [ChatGPT Work](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

## 4. Die Zugänge, die Claude benötigt

Dies ist der wichtigste Punkt: **Der Skill ist nur so gut wie die Quellen, die er öffnen kann.**

| Zugang | Wozu er dient | Wo er aktiviert wird | Wenn er fehlt |
|---|---|---|---|
| **„Code execution and file creation“** (Codeausführung und Dateierstellung) | den Skill ausführen, den PDF-Bericht erstellen | „Settings › Capabilities“ (Einstellungen › Funktionen) | der Skill wird nicht geladen |
| **„Web search“** (Websuche) | Urteile, Gesetze und Aufsätze finden | in Cowork enthalten (der Administrator einer Organisation kann sie deaktiviert haben); in einer gewöhnlichen Unterhaltung: Schaltfläche **+** im Eingabefeld › **„Web search“** (Websuche) | **Prüfung unmöglich** |
| **„Built-in browser“** (Integrierter Browser) | Websites öffnen, die Verbindungen von Servern ablehnen: EUR-Lex, CURIA, HUDOC, Staatsrat | „Settings › **Cowork** › **Preferred browser**“ (Einstellungen › Cowork › Bevorzugter Browser) › **„Built-in browser“** (Integrierter Browser); die Desktop-App während der Prüfung **geöffnet und verbunden** lassen | diese Quellen werden nur teilweise oder gar nicht überprüft |
| **Verbundener Ordner** (optional) | das Dokument lesen und den Bericht direkt auf Ihrem Computer speichern | bei der ersten Anfrage von Cowork den betreffenden Ordner freigeben | das Dokument der Unterhaltung beifügen und den Bericht herunterladen |

**Warum der Browser so wichtig ist.** Cowork arbeitet standardmäßig auf Servern von Anthropic. Mehrere amtliche Websites (EUR-Lex, CURIA, Staatsrat) sperren jedoch Verbindungen, die von Rechenservern kommen, und einfache Lesewerkzeuge erhalten von ihnen nur eine leere Seite. Der integrierte Browser läuft dagegen in der Desktop-App, auf Ihrem Computer: Diese Websites akzeptieren ihn normalerweise. Claude meldet eine gesperrte Website stets als Zugangsproblem, niemals als Fehlen der Quelle.

Vor Beginn überprüft Claude selbst seine Zugänge. Fehlt einer, teilt Claude Ihnen dies mit und erklärt, was zu tun ist, bevor die Recherchen beginnen.

### Für den Administrator einer Organisation (Team, Enterprise)

An die Person weiterzuleiten, die Ihr Claude-Konto verwaltet:

- **„Organization settings › Cowork“** (Organisationseinstellungen › Cowork): Cowork und den **integrierten Browser** aktivieren (bei Enterprise standardmäßig deaktiviert);
- **„Organization settings › Capabilities“** (Organisationseinstellungen › Funktionen): **„Skills“**, **„Code execution and file creation“** (Codeausführung und Dateierstellung) und **„Web search“** (Websuche) aktivieren;
- unter **„Capabilities › Code execution“** (Funktionen › Codeausführung): Ist der Netzwerkzugang eingeschränkt (bei Enterprise standardmäßig der Fall), mindestens folgende Domains zulassen, die zum Herunterladen der amtlichen Texte verwendet werden: `eur-lex.europa.eu`, `data.europa.eu`, `curia.europa.eu`, `infocuria.curia.europa.eu`, `hudoc.echr.coe.int`, `ks.echr.coe.int`, `www.ejustice.just.fgov.be`, `juportal.be`, `www.const-court.be`, `www.raadvst-consetat.be`, `www.lachambre.be`, `www.dekamer.be`, `www.senate.be`, `www.edpb.europa.eu`, `orbi.uliege.be`, `dial.uclouvain.be`, `api.crossref.org`.

Eine Einstellung wird erst in einer **neuen** Aufgabe oder Unterhaltung wirksam. Referenzen (auf Englisch): [Cowork für Team und Enterprise](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans), [integrierter Browser](https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork).

## 5. Eine Prüfung starten

1. Öffnen Sie die Claude-Desktop-App und starten Sie eine **neue Cowork-Aufgabe** (wählen Sie „Cowork“ im Eingabebereich).
2. Fügen Sie Ihr Dokument bei (Büroklammer oder Ziehen und Ablegen) oder geben Sie seinen Speicherort in einem verbundenen Ordner an.
3. Kopieren Sie diese Anfrage und passen Sie sie bei Bedarf an:

> Verwende den Skill audit-citations-juridiques-be-eu, um alle Fundstellen und Zitate im beigefügten Dokument zu überprüfen. Erstelle einen Bericht auf Deutsch, als PDF. Das Dokument bezieht sich auf den Stand vom 1. März 2024.

Ersetzen Sie das Datum durch das Ihres Dokuments (Datum der Abfassung oder Zeitpunkt, zu dem die Rechtslage zu beurteilen ist). Lassen Sie es weg, leitet Claude es aus dem Dokument ab oder prüft ersatzweise das heute geltende Recht und teilt Ihnen dies mit.

Nützliche Präzisierungen, die Sie hinzufügen können, wenn sie Sie betreffen:

- **der Umfang**: „nur die Fußnoten von Kapitel 2“, „nur die Rechtsprechung“;
- **der rechtliche Stichtag**: „das Dokument bezieht sich auf den Stand vom 1. Januar 2024“ (nützlich, um ein Gesetz in seiner damaligen Fassung zu überprüfen);
- **die Sprache des Berichts**: Französisch, Niederländisch, Deutsch oder Englisch (das PDF wird in der gewählten Sprache gestaltet);
- **die inhaltliche Prüfung**: Möchten Sie auch wissen, ob die Quellen Ihre Aussagen tatsächlich stützen, verlangen Sie dies ausdrücklich; diese Kontrolle erfolgt nicht standardmäßig.

## 6. Wie lange es dauert

Jede Quelle wird tatsächlich geöffnet und gelesen, mitunter auf mehreren Wegen: Die Prüfung erfolgt also nicht sofort, bleibt aber zügig.

- Rechnen Sie mit **etwa einer Minute pro einzelner Quelle, oft weniger**, mehr bei Rechtslehre, älteren Entscheidungen oder langsamen Websites.
- Zur Veranschaulichung aus den Tests in Cowork: Ein Auszug mit 16 Fußnoten und 12 Quellen wurde in wenigen Minuten geprüft.
- Etwa ein Dutzend Quellen: rund 5 bis 15 Minuten. Ab etwa fünfzig Quellen ist es angenehmer, kapitelweise vorzugehen.

Nachdem Claude Ihr Dokument gelesen hat, nennt es die Anzahl der Quellen, den **rechtlichen Stichtag**, zu dem es die Texte prüft (den von Ihnen angegebenen oder einen aus dem Dokument abgeleiteten), und eine voraussichtliche Dauer. **Passt dieser Stichtag nicht, antworten Sie einfach**, etwa „prüfe zum 1. Januar 2016“: Claude berücksichtigt ihn, ohne von vorn zu beginnen. Danach meldet es Zwischenstände („12 von 25 Quellen überprüft“). **Lassen Sie die Desktop-App geöffnet und verbunden**: Die Cowork-Aufgabe läuft auf den Servern weiter, aber der integrierte Browser benötigt die App. Sie können sich anderen Dingen widmen und später zurückkehren. Senden Sie die Anfrage nicht erneut: Die Arbeit würde sonst von vorn beginnen.

Eine lange Prüfung verbraucht einen erheblichen Teil Ihres Nutzungskontingents (**„Settings › Usage“** (Einstellungen › Nutzung)). Bei einem umfangreichen Dokument lässt sich der Verbrauch durch kapitelweises Vorgehen besser verteilen.

## 7. Den Bericht lesen

Der Bericht beginnt mit dem **Wesentlichen** und den **notwendigen Korrekturen** und behandelt dann jede Fundstelle im Einzelnen, mit Links zu den eingesehenen Quellen.

| Vermerk | Bedeutung |
|---|---|
| **Fundstelle überprüft** | die Quelle existiert und entspricht dem, was Sie geschrieben haben |
| **Fundstelle überprüft · Zitat: geringfügige Abweichung** (oder „unzutreffend“) | die Quelle ist richtig, aber der Text in Anführungszeichen stimmt nicht genau überein |
| **Fundstelle identifiziert, Korrektur erforderlich** | es handelt sich um die richtige Quelle, aber ein Element ist falsch (Datum, Nummer, ECLI, Artikel…); die Korrektur wird angegeben |
| **Teilweise überprüft** | einige Elemente sind bestätigt, andere konnten nicht bestätigt werden |
| **Mit den zugänglichen Quellen nicht überprüfbar** | die Quelle konnte weder bestätigt noch ausgeschlossen werden (kostenpflichtiger Zugang, gesperrte Website, nicht digitalisiertes Werk): **selbst zu überprüfen; dies ist kein festgestellter Fehler** |
| **Fundstelle nicht auffindbar oder Widerspruch festgestellt** | eine amtliche Quelle widerspricht der Fundstelle: vorrangig zu prüfen |

Die Bedeutung jeder Korrektur wird angegeben: **kritische Priorität**, **wichtige Korrektur**, **punktuelle Korrektur** oder **Information**. Jeder Korrektur ist die Passage aus der Quelle beigefügt, die sie belegt: Sie können sie mit einem Klick nachprüfen.

Der Bericht ist ein Hilfsmittel: **Lesen Sie die Korrekturen durch, bevor Sie sie übernehmen**, insbesondere in einem Verfahrensschriftstück.

## 8. Vertraulichkeit

- Ihr Dokument wird von Claude nach den Bedingungen Ihres Abonnements oder Ihrer Organisation verarbeitet.
- Um die Fundstellen zu überprüfen, sendet Claude **Fundstellen und kurze Auszüge** (Nummer eines Urteils, Titel eines Aufsatzes, zitierter Satz) an Suchmaschinen und amtliche Websites. Der Skill sieht nicht vor, ihnen Ihr Dokument selbst zu übermitteln.
- Bei einer Akte, die dem Berufsgeheimnis unterliegt, vergewissern Sie sich, dass das Werkzeug von Ihrer Organisation zugelassen ist, oder entfernen Sie zuerst die Namen der Parteien: Die Prüfung betrifft die Fundstellen, nicht den Sachverhalt der Akte.

## 9. Häufige Probleme

- **Claude antwortet, ohne den Skill zu verwenden.** Nennen Sie seinen Namen in der Anfrage („verwende den Skill audit-citations-juridiques-be-eu“) und prüfen Sie, ob er aktiviert ist (Abschnitt 3).
- **Fast alles ist „nicht überprüfbar“.** Die Websuche ist wahrscheinlich deaktiviert oder eine wesentliche Website ist gesperrt. Aktivieren Sie die Websuche und starten Sie die Prüfung in einer neuen Aufgabe erneut.
- **Die europäischen Quellen oder die des Staatsrats bleiben „teilweise“ überprüft.** Der integrierte Browser ist nicht aktiviert, oder die Desktop-App wurde während der Prüfung geschlossen (Abschnitt 4).
- **Kein PDF, nur Text.** Die Codeausführung ist nicht aktiviert, oder die Umgebung erlaubt keine Dateierstellung. Der Inhalt des Berichts bleibt derselbe.
- **Eine Website verlangt einen Nachweis, dass man ein Mensch ist („CAPTCHA“).** Claude umgeht diese Schutzmechanismen niemals: Es sucht einen anderen amtlichen Weg oder weist auf die Einschränkung hin.
- **Das Dokument ist sehr lang.** Verlangen Sie eine Prüfung Kapitel für Kapitel; jeder Bericht bleibt datiert und in sich abgeschlossen.

## 10. Ihre Meinung

Der Skill wird dank der Rückmeldungen der Juristinnen und Juristen besser, die ihn nutzen. Mit einem Formular von zwei Minuten, **ohne Konto**, können Sie melden:

- einen Fehler, den der Bericht nicht erkannt hat;
- einen Fehlalarm oder eine unklare Schlussfolgerung;
- eine Fundstelle, die Ihnen erfunden erscheint;
- ein Problem bei Installation oder Nutzung;
- oder einfach, dass alles gut funktioniert hat.

👉 **[Rückmeldeformular](https://docs.google.com/forms/d/e/1FAIpQLScTwVeTDbksjMzbX2lJ-7Vnc7JcOJOzoC-_EjmsCMBzoLHrPQ/viewform)** — der Link steht auch am Ende jedes Berichts, in der Sprache des Berichts.

Geben Sie die betroffene Fundstelle an und, wenn möglich, den Link zur amtlichen Quelle, die die richtige Antwort zeigt. **Fügen Sie niemals ein vertrauliches Dokument oder Mandantendaten ein.** Jedes bestätigte Problem wird behoben und in die Tests des Skills aufgenommen, damit es sich nicht wiederholt.

Sie haben ein GitHub-Konto und der Skill ist Ihnen nützlich? Ein Stern ⭐ auf der [Projektseite](https://github.com/marjoas-star/audit-citations-juridiques-be-eu) hilft anderen, ihn zu entdecken.
