# Prüfung juristischer Fundstellen — Belgien & Europa

**0.5.0-beta.1, experimentelle öffentliche Version.** Dieser Skill unterstützt einen Agenten bei der Prüfung von Fundstellen, Zitaten und internen Verweisen in belgischen, EU- und EMRK-Dokumenten. Die Anweisungen sind französisch; Arbeitssprachen sind FR/NL/DE/EN.

Das Release-Archiv entpacken und den Ordner `audit-citations-juridiques-be-eu` über die Skill-Funktion der jeweiligen Anwendung installieren. Für Codex liegt er unter `~/.codex/skills/` oder im skills-Ordner des konfigurierten CODEX_HOME. Unterordner beibehalten; Einstiegspunkt ist `SKILL.md`.

Beispiel: „Prüfe mit audit-citations-juridiques-be-eu die Fundstellen und Zitate dieses Dokuments. Bewahre die ursprünglichen Angaben und unterscheide nachgewiesene Fehler von Zugangsbeschränkungen.“

Der Agent benötigt Such- und Browserzugang sowie Werkzeuge zum Lesen der bereitgestellten Dokumente. Markdown ist das maßgebliche Berichtsformat; PDF erfordert Erzeugung und visuelle Kontrolle. Das Paket enthält keine eigenständige Suchmaschine und keinen PDF-Generator. PyYAML ist für die Nutzung der Anweisungen nicht erforderlich.

Amtliche Quellen haben Vorrang; Kennungen werden nicht erraten. Ein technischer Fehler beweist nicht die Nichtexistenz einer Entscheidung. Bei bekannter Entscheidungsnummer des belgischen Staatsrates ist zuerst das amtliche erweiterte Suchformular zu verwenden.

[VALIDATION.md](VALIDATION.md) trennt reale Prüfungen, Simulationen und Grenzen. Die Beta ist keine allgemeine V1-Zertifizierung; eine allgemeine Genauigkeitsquote wird nicht behauptet. Für professionelle Verwendung bleibt menschliche Prüfung erforderlich. Ursprüngliche Dokumentation: [CC BY-NC-SA 4.0](LICENSE). Externe Quellen unterliegen weiterhin ihren eigenen Bedingungen und werden hier nicht weiterverbreitet.
