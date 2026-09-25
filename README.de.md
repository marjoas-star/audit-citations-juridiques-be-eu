# Prüfung juristischer Fundstellen — Belgien & Europa

**0.5.0-beta.3, experimentelle öffentliche Version.** Dieser Skill unterstützt einen Agenten bei der Prüfung von Fundstellen, Zitaten und internen Verweisen in belgischen, EU- und EMRK-Dokumenten. Die Anweisungen sind französisch; Arbeitssprachen sind FR/NL/DE/EN.

Das Release-Archiv entpacken und den Ordner `audit-citations-juridiques-be-eu` über die Skill-Funktion der jeweiligen Anwendung installieren. Für Codex liegt er unter `~/.codex/skills/` oder im skills-Ordner des konfigurierten CODEX_HOME. Für Claude Code unter `~/.claude/skills/` (alle Projekte) oder im `.claude/skills/` eines Projekts; in der Claude-App ein Zip des Ordners über die Skills-Einstellungen hochladen. Unterordner beibehalten; Einstiegspunkt ist `SKILL.md`.

Beispiel: „Prüfe mit audit-citations-juridiques-be-eu die Fundstellen und Zitate dieses Dokuments. Bewahre die ursprünglichen Angaben und unterscheide nachgewiesene Fehler von Zugangsbeschränkungen.“

Der Agent benötigt Such- und Browserzugang sowie Werkzeuge zum Lesen der bereitgestellten Dokumente. Markdown ist das maßgebliche Berichtsformat; PDF erfordert Erzeugung und visuelle Kontrolle. Ein [französischer PDF/Markdown-Generator](templates/report-rendering.md) ist enthalten (Python und ReportLab für PDF); eine eigenständige Suchmaschine ist nicht enthalten. PyYAML ist für die Nutzung der Anweisungen nicht erforderlich.

Amtliche Quellen haben Vorrang; Kennungen werden nicht erraten. Ein technischer Fehler beweist nicht die Nichtexistenz einer Entscheidung. Bei bekannter Entscheidungsnummer des belgischen Staatsrates ist zuerst das amtliche erweiterte Suchformular zu verwenden.

[VALIDATION.md](VALIDATION.md) trennt reale Prüfungen, Simulationen und Grenzen. Die Beta ist keine allgemeine V1-Zertifizierung; eine allgemeine Genauigkeitsquote wird nicht behauptet. Für professionelle Verwendung bleibt menschliche Prüfung erforderlich. Ursprüngliche Dokumentation: [CC BY-NC-SA 4.0](LICENSE). Externe Quellen unterliegen weiterhin ihren eigenen Bedingungen und werden hier nicht weiterverbreitet.

Betatest: [Anleitung für Juristen (Französisch)](tests/beta/guide.md) und [Rückmeldeformular](tests/beta/fiche-retour.md).
