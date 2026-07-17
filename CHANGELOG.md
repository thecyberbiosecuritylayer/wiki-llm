# Changelog

The format follows Keep a Changelog and the publication semantics in
[`RELEASES.md`](RELEASES.md). Versions describe knowledge-base snapshots; they
do not certify that every source or conclusion is complete, current, or
universally applicable.

## [Unreleased]

### Added

- A structured thematic guide in `wiki/index.md` connects domain-level
  syntheses to narrower workflows, risks, controls, incidents, and search
  vocabulary without duplicating a complete catalog.
- Maintainer authority and the two distinct release tracks are documented in
  `MAINTAINERS.md` and `RELEASES.md`.
- A structure-proposal issue form provides a public route for reusable-page,
  navigation, schema, and maintenance-contract changes.
- Dedicated synthesis and open-question templates cover the two page types
  previously missing from the public authoring surface.

### Changed

- The repository landing page, contribution route, and human quickstart now
  provide shorter public entry paths while preserving `AGENTS.md` as the full
  normative contract for LLM-assisted and automated maintenance.
- Security guidance now points directly to the enabled private vulnerability-
  reporting route.
- Citation metadata no longer presents an evidence-bundle date as a versioned
  release of the knowledge base.
- English is now the canonical language of the repository.
- Reader-facing content was standardized as ordinary GitHub-compatible
  Markdown that requires neither a custom renderer nor maintenance scripts to
  read.
- The local `raw/` directory remains the immutable primary-source layer; public
  Git history contains no binary raw artifacts.
- The public explainer [`SYN-0034`](wiki/syntheses/syn-0034-what-is-cyberbiosecurity-public-explainer.md)
  was added and fully edited for publication.
- The original Markdown knowledge layer is prepared for release under CC BY
  4.0, with third-party raw artifacts and other external rights explicitly
  excluded from the project licence.
- The public raw allowlist was narrowed to nine individually reviewed
  artifacts and moved into a separately versioned release bundle with checksum
  and rights metadata. Two non-commercially licensed files remain unchanged in
  the local evidence archive and are represented publicly through their `SRC`
  pages.
- A reconstructable clinical-record case branch was removed from the public
  knowledge layer, its stable IDs were retired, and dependent corpus findings
  were recalibrated. The underlying local raw evidence remains unchanged.
- Contributor, conduct, security, citation, pull-request, issue-reporting, and
  automated validation surfaces were added for an open knowledge workflow.

## [0.1.0] - 2026-07-13

This initial corpus checkpoint predates the current public Git history and has
no corresponding public tag. A later commit must not be tagged retroactively as
this historical state.

### Added

- Stable page and claim identifiers.
- Source provenance notes and an immutable local raw evidence archive.
- An initial evidence-based cross-domain cyberbiosecurity knowledge corpus.

### Fixed

- Restored a consistent `SYN-0032` checkpoint with 236 active pages and no
  active dependencies on 11 reserved IDs.
- Moved an unactivated multi-source transaction out of the canonical wiki
  without changing or deleting its immutable raw artifacts.
