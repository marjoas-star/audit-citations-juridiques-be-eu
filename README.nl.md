# Audit van juridische verwijzingen — België & Europa

**0.5.0-beta.3, experimentele publieke versie.** Deze skill begeleidt een agent bij de controle van verwijzingen, citaten en interne verwijzingen in Belgische, EU- en EVRM-documenten. De instructies zijn in het Frans; werktalen zijn FR/NL/DE/EN.

Pak het release-archief uit en installeer de map `audit-citations-juridiques-be-eu` via het skillmechanisme van de gebruikte toepassing. Voor Codex: onder `~/.codex/skills/`, of de skills-map van het ingestelde CODEX_HOME. Voor Claude Code: onder `~/.claude/skills/` (alle projecten) of `.claude/skills/` van een project; in de Claude-app een zip van de map uploaden via de Skills-instellingen. Behoud de submappen. Startbestand: `SKILL.md`.

Voorbeeld: “Gebruik audit-citations-juridiques-be-eu om de verwijzingen en citaten in dit document te controleren. Bewaar de oorspronkelijke verwijzingen en onderscheid vastgestelde fouten van beperkingen van de toegang.”

De agent heeft zoek- en browsertoegang en hulpmiddelen voor de aangeleverde documenten nodig. Markdown is het basisrapport; PDF vereist hulpmiddelen voor generatie en visuele controle. Een [Franse PDF/Markdown-generator](templates/report-rendering.md) is inbegrepen (Python en ReportLab voor PDF: `pip install -r requirements.txt`); er is geen zelfstandige zoekmachine. PyYAML is niet nodig om de instructies te gebruiken.

Officiële bronnen krijgen voorrang. Identificatoren worden niet geraden. Een technische storing bewijst niet dat een arrest niet bestaat. Bij een bekend arrestnummer van de Belgische Raad van State wordt eerst het officiële geavanceerde zoekformulier gebruikt. De FR- en NL-trefwoordenstructuren van juriDict zijn niet automatisch elkaars vertaling.

Zie [VALIDATION.md](VALIDATION.md) voor echte proeven, simulaties en beperkingen. Deze bèta is geen algemene V1-certificering; er wordt geen algemeen betrouwbaarheidspercentage gegeven. Menselijke controle blijft nodig voor professioneel gebruik. Oorspronkelijke documentatie: CC BY-NC-SA 4.0; Python-code (`scripts/`, `tests/`): [PolyForm Noncommercial 1.0.0](LICENSE-CODE.md). Zie [LICENSE](LICENSE). Externe bronnen behouden hun eigen voorwaarden en worden hier niet verspreid.

Bètatest: [instructies voor juristen (Frans)](tests/beta/guide.md) en [feedbackformulier](tests/beta/fiche-retour.md).
