# Primary-source archive

This directory is the immutable evidence layer for the wiki. Each retained
artifact is linked from a corresponding `wiki/sources/SRC-*.md` provenance note,
which records its identity, version, access date, hash, reading coverage,
locators, and limitations.

## Immutability

Existing artifacts are not edited, renamed, reformatted, or replaced. A revised
edition or materially different version is retained as a separate artifact and
documented in the relevant source note.

## Public-repository boundary

Local retention and public redistribution are different decisions. Many files
in this archive are third-party works. Public availability at the original URL
does not by itself grant permission to upload a copy to another repository.

For that reason, the public Git configuration tracks this README but excludes
all binary raw artifacts. An exact copy may enter a separately versioned public
evidence release only after an artifact-specific review confirms all of the
following:

1. the exact retained version may be redistributed;
2. required attribution and licence notices are preserved;
3. third-party figures, photographs, datasets, or other exclusions are handled;
4. the file contains no personal, controlled, restricted, or unsafe operational
   material that should not be republished; and
5. the matching `SRC` note accurately records the artifact and its limitations.

An approved release bundle is a distribution convenience, not the canonical
archive and not a single relicensed collection. Each file retains its own
terms, required notice, provenance binding, and checksum. When a raw file
cannot be redistributed, its `SRC` note remains the public evidence route and
points readers to the rightsholder's canonical copy.

## Reader guidance

If a raw path referenced by an `SRC` page is absent from a public clone, use the
page's `canonical_url`, DOI, official publication identifier, and precise
locator. For files explicitly named in the root `RAW_SOURCES.md`, the versioned
public evidence release is an additional verified copy. The missing local file
does not change the claim's evidence identity; it only reflects the
redistribution boundary.
