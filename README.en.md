# Legal citation audit — Belgium & Europe

> **Legal practitioners:** a step-by-step [user guide](USER-GUIDE.md) explains installation, the access Claude needs, how long an audit takes and how to read the report.

**0.9.0-rc.2, release candidate (stability trial before 1.0).** A skill for an agent auditing references, quotations and internal cross-references in Belgian, EU and ECHR legal documents. Instructions are written in French; working languages are French, Dutch, German and English.

Extract the release archive and install the `audit-citations-juridiques-be-eu` folder through your host’s skill mechanism. For Codex, put it under `~/.codex/skills/`, or the configured CODEX_HOME skills folder, preserving subfolders. For Claude Code, put it under `~/.claude/skills/` (all projects) or a project’s `.claude/skills/`; in the Claude app, upload a zip of the folder from the Skills settings. Entry point: `SKILL.md`.

Example: “Use audit-citations-juridiques-be-eu to audit this document’s citations. Preserve the original references, report the evidence actually consulted and distinguish errors from access limitations.”

The agent needs search/browser access and tools for reading the supplied documents. Markdown is the canonical report; PDF requires generation and visual inspection tools. The package includes a [PDF/Markdown renderer in French, Dutch, German or English](templates/report-rendering.md) (Python and ReportLab for PDF: `pip install -r requirements.txt`), but no autonomous search engine; PyYAML is not required to use its instructions.

Official sources take priority. Never guess an identifier, equate a failed search interface with a nonexistent decision, or treat a snippet as a consulted judgment. Belgian Council of State decisions with a known number must be sought first through the official advanced search form.

See [validation](VALIDATION.md) for real trials, simulations and limits. This beta is not a general V1 certification; no overall accuracy percentage is claimed. Professional use requires human review. Original documentation: CC BY-NC-SA 4.0; Python code (`scripts/`, `tests/`): [PolyForm Noncommercial 1.0.0](LICENSE-CODE.md). See [LICENSE](LICENSE). External sources retain their own terms and are not redistributed here.

Feedback: [two-minute form, no GitHub account needed](https://docs.google.com/forms/d/e/1FAIpQLSfjMg3pOWrlxo6dnVdRbHvz0nSqQSnizGY8b4lv_lHQ6HURFQ/viewform). If the skill is useful to you, a star ⭐ on this repository helps others find it.

Beta testing: [instructions for legal reviewers (French)](tests/beta/guide.md) and [feedback form](tests/beta/fiche-retour.md).
