# User guide for legal practitioners

[Français](MODE-EMPLOI.md) · [Nederlands](HANDLEIDING.md) · [Deutsch](ANLEITUNG.md) · [English](USER-GUIDE.md)

This guide is for lawyers and other legal practitioners who want Claude to check the references in a document. No technical knowledge is required. The menus of the Claude app change over time: if a label differs slightly, look for the closest term.

## 1. What this skill does

You give Claude a legal document (written submissions, memo, article, opinion, brief…). Claude:

- identifies every reference and quotation;
- checks each one against the official sources (EUR-Lex, CURIA, HUDOC, Belgian Official Gazette (Moniteur belge / Belgisch Staatsblad), Justel, Council of State, Constitutional Court, JUPORTAL, parliamentary preparatory works…) and, for legal scholarship, against university catalogues and repositories;
- checks that quotations in quotation marks reproduce the text faithfully, including where passages have been omitted;
- gives you a report: corrections to make, points to check yourself, confirmed references, with links to the sources consulted.

What it **does not do**: it does not assess the quality of your reasoning (unless you expressly ask it to), it does not get around any subscription or paywall, and it never invents a number or an ECLI. When it cannot verify something, it says so: **"not verifiable" does not mean "wrong".**

## 2. What you need

- **Claude Cowork**, available with paid plans (Pro, Max, Team, Enterprise), and preferably the **Claude desktop app** (Mac or Windows) installed on your computer: it provides the browser that the skill needs for several official websites (section 4).
- The skill file: the `.zip` archive of the latest version, to be downloaded from the [Releases page of the repository](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/releases) ("Assets" section, file `audit-citations-juridiques-be-eu-….zip`). **Do not unzip the archive.**
- Your document as a PDF, Word or text file. A scanned PDF (an image with no text) is harder to read: use the Word version or a "text" PDF if you can.

The skill also works in an ordinary Claude conversation and in Claude Code; the settings are similar (see the end of section 3).

## 3. Installing the skill (one time only)

1. In the Claude app, open **Settings › Capabilities** and turn on **Code execution and file creation**. Without this option, skills do not work.
2. Open **Customize** (in the left sidebar) › **Skills**.
3. Click **+**, then **Create skill**, then **Upload a skill**.
4. Select the `.zip` archive you downloaded.
5. Check that the skill **audit-citations-juridiques-be-eu** appears in the list and is turned on.

The skill is then available in Cowork as well as in ordinary conversations. Official help: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

**In Claude Code** (the "Code" tab of the desktop app), the simplest way is to ask Claude: "Install the skill from the GitHub repository marjoas-star/audit-citations-juridiques-be-eu (latest published version) for all my projects."

## 4. The access Claude needs

This is the most important point: **the skill is only as good as the sources it can open.**

| Access | What it is for | Where to turn it on | If it is missing |
|---|---|---|---|
| **Code execution and file creation** | running the skill, producing the PDF report | Settings › Capabilities | the skill does not load |
| **Web search** | finding judgments, statutes and articles | included in Cowork (an organization's administrator may have turned it off); in an ordinary conversation, **+** button in the input field › **Web search** | **audit impossible** |
| **Built-in browser** | opening websites that refuse connections coming from servers: EUR-Lex, CURIA, HUDOC, Council of State | Settings › **Cowork** › **Preferred browser** › **Built-in browser**; keep the desktop app **open and connected** during the audit | these sources are only partly verified, or not at all |
| **Connected folder** (optional) | reading the document and saving the report directly on your computer | when Cowork first asks, allow access to the relevant folder | attach the document to the conversation and download the report |

**Why the browser matters so much.** By default, Cowork works on Anthropic's servers. However, several official websites (EUR-Lex, CURIA, Council of State) block connections coming from computer servers, and simple reading tools receive a blank page from them. The built-in browser, on the other hand, runs in the desktop app, on your computer: these websites normally accept it. Claude always reports a blocked website as an access problem, never as the source not existing.

Before starting, Claude checks its own access. If something is missing, it tells you and explains what to do, before starting the searches.

### For an organization's administrator (Team, Enterprise)

To pass on to the person who manages your Claude account:

- **Organization settings › Cowork**: turn on Cowork and the **built-in browser** (off by default on Enterprise);
- **Organization settings › Capabilities**: turn on **Skills**, **code execution and file creation** and **web search**;
- in **Capabilities › Code execution**, if network access is restricted (the default on Enterprise), allow at least these domains, used to download official texts: `eur-lex.europa.eu`, `data.europa.eu`, `curia.europa.eu`, `infocuria.curia.europa.eu`, `hudoc.echr.coe.int`, `ks.echr.coe.int`, `www.ejustice.just.fgov.be`, `juportal.be`, `www.const-court.be`, `www.raadvst-consetat.be`, `www.lachambre.be`, `www.dekamer.be`, `www.senate.be`, `www.edpb.europa.eu`, `orbi.uliege.be`, `dial.uclouvain.be`, `api.crossref.org`.

A setting only takes effect in a **new** task or conversation. References: [Cowork for Team and Enterprise](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans), [built-in browser](https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork).

## 5. Running an audit

1. Open the Claude desktop app and start a **new Cowork task** (choose "Cowork" in the input area).
2. Attach your document (paperclip or drag and drop), or give its location in a connected folder.
3. Copy this request, adapting it if needed:

> Use the audit-citations-juridiques-be-eu skill to check all references and quotations in the attached document. Produce a report in English.

Useful details to add if they apply to you:

- **the scope**: "only the footnotes in chapter 2", "only the case law";
- **the legal reference date**: "the document speaks as of 1 January 2024" (useful for checking a statute as it stood at the time);
- **the language of the report**: French, Dutch, German or English (the formatted PDF currently exists only in French; in the other languages, Claude prepares a Markdown report);
- **the substance**: if you also want to know whether the sources actually support your statements, ask for it expressly; this check is not done by default.

## 6. How long it takes

Each source is actually opened and read, sometimes by several routes: the audit is not instant, but it remains quick.

- Allow **about one minute per distinct source, often less**, more for legal scholarship, older decisions or slow websites.
- For example, in Cowork testing: an extract with 16 footnotes citing 12 sources was audited in a few minutes.
- About a dozen sources: roughly 5 to 15 minutes. Beyond about fifty, it is more comfortable to proceed chapter by chapter.

After reading your document, Claude tells you the number of sources, the **legal reference date** at which it will check the texts (the one you gave, or one it infers from the document) and an estimated time range. **If that date does not suit you, just reply**, for example "check as at 1 January 2016": it will take it into account without starting over. It then gives progress updates ("12 of 25 sources checked"). **Keep the desktop app open and connected**: the Cowork task continues on the servers, but the built-in browser needs the app. You can do something else and come back. Do not resend the request: that would restart the work.

A long audit uses a significant share of your usage allowance (**Settings › Usage**). For a large document, proceeding chapter by chapter spreads it out better.

## 7. Reading the report

The report starts with the **key points** and the **corrections needed**, then goes through each reference in detail, with links to the sources consulted.

| Status | Meaning |
|---|---|
| **Reference verified** (PDF: « Référence vérifiée ») | the source exists and matches what you wrote |
| **Reference verified · quotation: minor discrepancy** (or "inaccurate quotation") (PDF: « Référence vérifiée · citation : écart mineur » / « citation inexacte ») | the source is correct, but the text in quotation marks does not match exactly |
| **Reference identified, correction needed** (PDF: « Référence identifiée, correction nécessaire ») | it is indeed the right source, but one element is wrong (date, number, ECLI, article…); the correction is indicated |
| **Partial verification** (PDF: « Vérification partielle ») | some elements are confirmed, others could not be |
| **Verification impossible with the accessible sources** (PDF: « Vérification impossible avec les sources accessibles ») | the source could be neither confirmed nor ruled out (paywall, blocked website, work not digitized): **check it yourself; this is not an established error** |
| **Reference not found or contradiction established** (PDF: « Référence non retrouvée ou contradiction établie ») | an official source contradicts the reference: to be examined first |

The importance of each correction is indicated: **critical priority** (PDF: « priorité critique »), **important correction** (PDF: « correction importante »), **minor correction** (PDF: « correction ponctuelle ») or **information** (PDF: « information »). Each correction comes with the passage from the source that supports it: you can check it in one click.

The report is an aid: **review the corrections before carrying them over**, especially in a court filing.

## 8. Confidentiality

- Your document is processed by Claude under the terms of your plan or your organization.
- To check the references, Claude sends **references and short extracts** (case number, title of an article, quoted sentence) to search engines and official websites. The skill is not designed to send them your document itself.
- For a matter covered by professional secrecy, check that the tool is authorized by your organization, or first remove the names of the parties: the audit concerns the references, not the facts of the case.

## 9. Common problems

- **Claude answers without using the skill.** Mention its name in the request ("use the audit-citations-juridiques-be-eu skill") and check that it is turned on (section 3).
- **Almost everything is "not verifiable".** Web search is probably turned off, or an essential website is blocked. Turn it on and try again in a new task.
- **EU or Council of State sources remain "partial".** The built-in browser is not turned on, or the desktop app was closed during the audit (section 4).
- **No PDF, only text.** Code execution is not turned on, or the environment does not allow files to be created. The content of the report remains the same.
- **A website asks you to prove you are human ("CAPTCHA").** Claude never gets around these protections: it looks for another official route or reports the limitation.
- **The document is very long.** Ask for an audit chapter by chapter; each report remains dated and self-contained.

## 10. Giving feedback

Your feedback as a legal practitioner is valuable, especially when a conclusion seems wrong or unclear to you: use the [feedback form](tests/beta/fiche-retour.md) (in French) or open an "issue" on the [GitHub repository](https://github.com/marjoas-star/audit-citations-juridiques-be-eu/issues). Never attach a confidential document.
