# Release policy

This file defines publication semantics. Release metadata and changelog entries
are project records, not factual evidence for the wiki.

## Two release tracks

| Track | Tag pattern | Contents | Project `Latest` |
| --- | --- | --- | --- |
| Knowledge base | `vMAJOR.MINOR.PATCH` | A complete Git snapshot of the Markdown corpus and its maintenance contract | Yes |
| Evidence bundle | `evidence-YYYY-MM-DD` | Separately reviewed raw bytes, rights metadata, and checksum manifests | No |

An evidence bundle is an optional reproducibility annex. It does not become the
canonical local `raw/` archive, grant redistribution rights to third-party
content, advance the wiki's knowledge cutoff, or turn an artifact into evidence
without its `SRC` provenance route. Evidence bundles are immutable after
publication.

## Knowledge-base versions

- **Major**: an incompatible change to the stable-ID, page, evidence, machine-
  maintenance, or public-safety contract.
- **Minor**: material new evidence integration, domain coverage, or revised
  synthesis conclusions.
- **Patch**: corrections to prose, links, metadata, and source locators that do
  not materially change a conclusion.

A release freezes the current repository state; it does not certify that the
corpus is complete, current, or universally applicable. The knowledge cutoff
is advanced only after the relevant evidence has been reviewed, never merely
because a release is created.

## Knowledge-release checklist

Only the maintainer of record may authorize a release. For each release:

1. prepare a release pull request that moves the applicable `Unreleased`
   entries into a dated version heading, sets matching `version` and
   `date-released` fields in `CITATION.cff`, and updates the current-publication-
   state section below plus any volatile release or citation wording in
   `README.md`;
2. confirm that the knowledge cutoff still describes the reviewed evidence,
   run `python3 tools/check.py` and `git diff --check`, review the complete diff,
   and merge the release pull request through branch protection;
3. fast-forward a clean local `main` to `origin/main`, rerun both checks, and
   verify that `HEAD` is the intended release commit;
4. create the matching `vMAJOR.MINOR.PATCH` tag and GitHub release from that
   exact `HEAD`, with the knowledge release marked as `Latest`; and
5. verify the tag, release notes, branch protections, and published citation
   metadata after publication.

For every new public knowledge release, the changelog version, citation
version, citation date, tag, and release commit form one publication
transaction. Do not claim a version in only some of those surfaces. The
documented pre-public `0.1.0` checkpoint below is the sole historical exception
and must not be reconstructed from a later commit.

## Evidence-bundle checklist

Before publishing an evidence bundle, verify explicit redistribution rights,
the allowlist in `RAW_SOURCES.md`, sorted SHA-256 entries in
`RAW_ARTIFACTS.sha256`, and each artifact's binding to exactly one `SRC` page.
Publish it as an immutable, non-`Latest` release. Never add raw binaries to Git
history.

## Current publication state

`0.1.0` in [`CHANGELOG.md`](CHANGELOG.md) records the initial corpus checkpoint
of 2026-07-13. The current public Git history has no corresponding `v0.1.0` tag,
so a historical tag must not be reconstructed from a later commit.

The immutable `evidence-2026-07-16` release is an evidence bundle, not a
versioned release of the knowledge base. Until the first knowledge release is
published, GitHub may display that bundle as `Latest`; it must not be cited as
the version of the wiki.

There is currently no versioned GitHub knowledge release. `CITATION.cff`
therefore omits `version` and `date-released`; cite the exact Git commit and
access date when a fixed snapshot is required. The next knowledge release
should be `v0.2.0`, because the current `Unreleased` work materially extends the
`0.1.0` checkpoint.

## Corrections and removal

Corrections are applied to the current default branch and recorded in the next
knowledge release. Published snapshots are not silently rewritten. If a
release itself creates a privacy or safety exposure, maintainers may seek
GitHub-assisted containment or removal and publish a documented superseding
record. Privacy and safety take precedence over historical availability.
