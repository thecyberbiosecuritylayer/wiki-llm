# Contributing to the Cyberbiosecurity Wiki

Thank you for helping improve this evidence-based knowledge project. Useful
contributions make claims easier to verify, preserve uncertainty, and reduce
privacy and safety risk.

## Before contributing

1. Read [`AGENTS.md`](AGENTS.md) for the repository's evidence, page, safety,
   and maintenance rules.
2. Search `wiki/` and [`wiki/id-registry.md`](wiki/id-registry.md) for relevant
   titles, aliases, IDs, URLs, DOIs, and key terms.
3. Use an issue form for an evidence correction or a new-source proposal before
   starting a broad or structurally significant change.
4. Report privacy, re-identification, sensitive biological capability,
   credentials, or repository-security concerns privately as described in
   [`SECURITY.md`](SECURITY.md). Do not put sensitive details in an issue or
   pull request.

Keep pull requests small enough to review as a coherent evidence transaction.
Separate unrelated corrections.

## Evidence and page requirements

- Write reader-facing prose in English while preserving official titles and
  established technical terms where precision requires it.
- Reuse an existing page when it already represents the subject. Never reuse,
  silently renumber, or delete an issued page or claim ID.
- Create one `SRC` page for one intellectual source. Check for duplicates by
  title, DOI, canonical URL, version, and retained-artifact hash.
- Cite every material externally verifiable claim through the underlying `SRC`
  page and the most precise available source locator. Topic pages are not
  evidence for other topic pages.
- Distinguish artifact observations, source reports, analytic judgments, and
  hypotheses. Preserve study scope, jurisdiction, version, dates, conflicts,
  and limitations that affect interpretation.
- Use standard relative Markdown links that work on GitHub and in an ordinary
  Markdown reader.
- Do not alter content between `human-note` markers.

## Raw artifacts

Existing files under `raw/` are immutable: never edit, normalize, rename, move,
or delete them. Do not attach or commit a new raw artifact merely because it is
publicly accessible. Propose the source using its canonical URL first. A new
artifact requires explicit maintainer approval plus review of provenance,
redistribution rights, privacy, and dual-use risk.

[`RAW_SOURCES.md`](RAW_SOURCES.md) is the public-release allowlist and rights
map. Public raw binaries belong in a separately reviewed release artifact, not
in Git history. The allowlist does not grant permission to add another file.

## Privacy, safety, and dual use

Do not submit personal genomic, clinical, participant, or employee data;
re-identifiable case detail; credentials; harmful biological sequences;
deployable exploits; facility access details; screening-evasion instructions;
or operational bypass procedures. A pseudonym is not adequate when combined
facts can reconstruct an identity.

Keep threat and control discussion defensive and proportionate. If a proposed
change may expose an undisclosed vulnerability, sensitive biological
capability, or novel harmful attack chain, stop and use the private reporting
route in [`SECURITY.md`](SECURITY.md).

## Pull-request checklist

Before opening a pull request:

```sh
python3 tools/check.py
git diff --check
rg -n '\[\[' wiki
rg -n '\p{Cyrillic}' --glob '*.md' .
```

The two searches should produce no Obsidian-only links and no untranslated
Cyrillic prose. Also read the rendered diff, open every affected page and its
linked `SRC` notes, and verify changed relative links and source locators.
Explain any check you could not run.

## Contribution license

By submitting original content to the Markdown knowledge layer or project
documentation, you represent that you have the right to provide it and agree
that it is licensed under the same
[Creative Commons Attribution 4.0 International Public License](LICENSE) used
for that layer. This is an inbound-equals-outbound policy; no separate
contributor license agreement is required.

Original contributions to validation code under `tools/` or workflow code
under `.github/workflows/` are submitted under the same
[MIT License](tools/LICENSE) that applies to those paths.

Do not submit third-party material unless its terms permit the proposed use and
you clearly identify its source, license, required attribution, and any
exclusions. Contributions to a file that expressly carries a different license
remain subject to that file's license.
