# Legal citation audit — Belgium & Europe

**0.5.0-beta.2, experimental public release.** A skill for an agent auditing references, quotations and internal cross-references in Belgian, EU and ECHR legal documents. Instructions are written in French; working languages are French, Dutch, German and English.

Extract the release archive and install the `audit-citations-juridiques-be-eu` folder through your host’s skill mechanism. For Codex, put it under `~/.codex/skills/`, or the configured CODEX_HOME skills folder, preserving subfolders. Entry point: `SKILL.md`.

Example: “Use audit-citations-juridiques-be-eu to audit this document’s citations. Preserve the original references, report the evidence actually consulted and distinguish errors from access limitations.”

The agent needs search/browser access and tools for reading the supplied documents. Markdown is the canonical report; PDF requires generation and visual inspection tools. The package includes a [French PDF/Markdown renderer](templates/report-rendering.md) (Python and ReportLab for PDF), but no autonomous search engine; PyYAML is not required to use its instructions.

Official sources take priority. Never guess an identifier, equate a failed search interface with a nonexistent decision, or treat a snippet as a consulted judgment. Belgian Council of State decisions with a known number must be sought first through the official advanced search form.

See [validation](VALIDATION.md) for real trials, simulations and limits. This beta is not a general V1 certification; no overall accuracy percentage is claimed. Professional use requires human review. Original documentation: [CC BY-NC-SA 4.0](LICENSE). External sources retain their own terms and are not redistributed here.

Beta testing: [instructions for legal reviewers (French)](tests/beta/guide.md) and [feedback form](tests/beta/fiche-retour.md).
