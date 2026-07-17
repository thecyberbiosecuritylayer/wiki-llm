# Cyberbiosecurity Wiki

An evidence-based Markdown knowledge base about risks at the boundary between
digital and biological systems.

Start with [`wiki/index.md`](wiki/index.md). It provides the subject map,
knowledge cutoff, and entry points into concepts, systems, workflows, risk
scenarios, controls, incidents, governance, sources, and cross-source
syntheses.

## What this repository contains

- [`wiki/`](wiki/) — the canonical, human-readable knowledge base;
- [`raw/`](raw/) — the policy boundary for the local immutable source archive;
  binary source artifacts are not tracked in the public Git history;
- [`wiki/sources/`](wiki/sources/) — one provenance note for each intellectual
  source;
- [`wiki/index.md`](wiki/index.md) — navigation and the knowledge cutoff;
- [`wiki/id-registry.md`](wiki/id-registry.md) — stable page identities;
- [`wiki/glossary.md`](wiki/glossary.md) — definitions and disambiguation.

Every decision-relevant claim has a stable local ID and identifies its evidence,
scope, and limits. Topic pages point to the underlying `SRC` provenance notes;
they are not treated as independent evidence.

## How to read it

Use GitHub search or a local text-search tool to find a term, page ID, claim ID,
author, organization, DOI, or source ID. A typical evidence path is:

```text
topic, risk, control, or synthesis page
  -> decision-relevant claim
  -> SRC provenance note and precise locator
  -> canonical external source or approved release artifact
```

Current laws, standards, product capabilities, and institutional positions can
change. Check each claim's `As of`, `Review after`, jurisdiction, version, and
limits before relying on it as current.

## Scope and safety

The wiki focuses on operational dependencies between digital and biological
systems. It distinguishes cyberbiosecurity from general cybersecurity,
biosecurity, and biosafety, and keeps incident evidence separate from
hypothetical risk scenarios.

The public corpus is defensive and source-based. It does not include harmful
biological sequences, deployable exploit code, credentials, facility access
details, or operational bypass instructions.

## Source artifacts

The local `raw/` layer is retained as an immutable primary-source archive.
Retained artifacts are never normalized or rewritten. Binary artifacts are not
stored in the public Git history. Where publication and safety boundaries
permit, Markdown `SRC` notes record bibliographic identity, provenance, source
coverage, precise locators, limitations, hashes, and canonical URLs.

Nine artifact-specific redistribution reviews currently support a separate
[public raw-evidence release](https://github.com/thecyberbiosecuritylayer/wiki-llm/releases/tag/evidence-2026-07-16).
The bundle preserves the exact reviewed bytes, provenance bindings, notices, and a
checksum manifest without placing binaries in the repository history. Every
other retained file remains local and, where a provenance binding exists, is
represented publicly by its `SRC` note and canonical source link. See
[`raw/README.md`](raw/README.md) for the archive policy,
[`RAW_SOURCES.md`](RAW_SOURCES.md) for the rights review, and
[`RAW_ARTIFACTS.sha256`](RAW_ARTIFACTS.sha256) for the released-file manifest.

See [`RIGHTS.md`](RIGHTS.md) for the reuse status of this knowledge base and its
sources.

## Reuse and contributions

Original Markdown content under `wiki/` and original project documentation are
licensed under the [Creative Commons Attribution 4.0 International
License](LICENSE), subject to the exclusions in [`RIGHTS.md`](RIGHTS.md). The
license does not cover third-party source artifacts in the local `raw/` archive
or public evidence release, quotations, official titles, trademarks, or other
material that the project does not own.
Project-authored validation code under `tools/` and workflow code under
`.github/workflows/` are separately licensed under the
[MIT License](tools/LICENSE).

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before
opening an issue or pull request, and use [`SECURITY.md`](SECURITY.md) rather
than a public issue for privacy, re-identification, sensitive-capability, or
security reports. Citation metadata is available in
[`CITATION.cff`](CITATION.cff).

## Validation

Run the repository's reader-facing validation before submitting a change:

```sh
python3 tools/check.py
```

The checks and their scope are documented in
[`tools/README.md`](tools/README.md).
