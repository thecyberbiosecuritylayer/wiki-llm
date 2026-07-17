# Raw-source redistribution review

The local immutable archive contains 192 non-Markdown files as of 2026-07-16.
The public Git tree contains no non-Markdown raw artifacts. The nine artifacts
allowlisted below are distributed separately in the
[public raw-evidence release](https://github.com/thecyberbiosecuritylayer/wiki-llm/releases/tag/evidence-2026-07-16).
The review uses notices in the retained artifacts and the matching
`wiki/sources/` provenance pages. Public availability, government authorship,
or a canonical download URL was not treated as redistribution permission.

The allowlist below is limited to the exact bytes identified by the SHA-256 in
the cited `SRC` page and [`RAW_ARTIFACTS.sha256`](RAW_ARTIFACTS.sha256). It does
not relicense any artifact, permit edits to the local `raw/` archive, or
authorize Git tracking. Required notices must accompany every released copy,
and each artifact remains subject to its own terms.

## Confirmed public-release allowlist

The table identifies exactly nine internal bundle paths. They are not files in
the Git tree. Every non-Markdown artifact not named in the table remains **not
allowlisted** for public redistribution.

| Exact artifact | Provenance | Local permission basis | Notice and restrictions required for a public copy |
| --- | --- | --- | --- |
| `raw/casp15-tertiary-structure-assessment-2023.pdf` | [SRC-0052](wiki/sources/src-0052-casp15-tertiary-structure-assessment-2023.md) | Article notice and embedded link identify CC BY 4.0. | Credit Simpkin et al. and the original *Proteins* publication, include DOI `10.1002/prot.26593` and the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) link, and state that the archived file is unmodified. Preserve `© 2023 The Authors`. |
| `raw/ema-ich-q13-step5-2023.pdf` | [SRC-0031](wiki/sources/src-0031-ich-q13-continuous-manufacturing.md) | The retained PDF states that reproduction is authorized when the source is acknowledged. | Preserve `© European Medicines Agency, 2023` and identify the source as *ICH guideline Q13 on continuous manufacturing of drug substances and drug products, Step 5*, EMA, 2023. |
| `raw/guttieres-advanced-biomanufacturing-2019-figure-1.jpg`<br>`raw/guttieres-advanced-biomanufacturing-2019-figure-2.jpg` | [SRC-0003](wiki/sources/src-0003-guttieres-advanced-manufacturing-2019.md) | The official article's license link resolves to [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and applies to the authors' article figures; no separate third-party credit is stated for either figure. | Credit `© 2019 Guttieres, Stewart, Wolfrum, and Springs` and cite *Cyberbiosecurity in Advanced Manufacturing Models*, DOI `10.3389/fbioe.2019.00210`. These are the unchanged NCBI-hosted JPEG response bytes saved separately from the article HTML; they were not cropped, resized, or re-encoded. Distribute only the exact hashed images. |
| `raw/heumos-mlf-core-deterministic-machine-learning-2023.pdf` | [SRC-0051](wiki/sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md) | The PDF and `SRC` record identify CC BY 4.0. | Credit Heumos et al., cite *mlf-core: a framework for deterministic machine learning*, DOI `10.1093/bioinformatics/btad164`, include the [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) link, preserve `© The Author(s) 2023`, and state that the file is unmodified. |
| `raw/high-containment-cyberbiosecurity-2023-figure-1.jpg`<br>`raw/high-containment-cyberbiosecurity-2023-figure-2.jpg`<br>`raw/high-containment-cyberbiosecurity-2023-figure-3.jpg` | [SRC-0002](wiki/sources/src-0002-crawford-high-containment-laboratories-2023.md) | The official article's license link resolves to [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and applies to the authors' article figures; no separate third-party credit is stated for these figures. | Credit `© 2023 Crawford, Bobrow, Sun, Joshi, Vijayan, Blacksell, Venugopalan, and Tensmeyer` and cite *Cyberbiosecurity in high-containment laboratories*, DOI `10.3389/fbioe.2023.1240281`. These are the unchanged NCBI-hosted JPEG response bytes saved separately from the article HTML; they were not cropped, resized, or re-encoded. Distribute only the exact hashed images. |
| `raw/ukhsa-immensa-epidemiological-analysis-preprint-2022.pdf` | [SRC-0057](wiki/sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md) | Every page identifies the retained preprint as CC BY-ND 4.0. | Distribute only the exact, unmodified preprint. Credit Hounsome et al., cite *Epidemiological impact of a large number of incorrect negative SARS-CoV-2 test results in South West England during September and October 2021*, DOI `10.1101/2022.11.30.22282922`, include the [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/) link, and retain its preprint warning. |

## Not allowlisted

The remaining 183 artifacts are not approved for public release: 24 have no
matching active `SRC` provenance binding, and 159 have a binding but lack a
clear artifact-wide redistribution grant or retain unresolved restrictions.
Common blockers include all-rights-reserved notices, personal/internal-use-only
terms, third-party images or logos, licenses that apply only to article content
rather than the complete saved webpage or supplement, and privacy or dual-use
detail deliberately withheld from the public Markdown layer.

Two reviewed artifacts are deliberately excluded because their licences limit
reuse to non-commercial purposes: the Quadripartite national One Health guide
(`CC BY-NC-SA 3.0 IGO`) and the Stetson oncology-AI article
(`CC BY-NC-ND 4.0`). Their local files remain unchanged, and their `SRC` pages
continue to provide canonical source links and evidence locators.

This is a conservative publication boundary, not a conclusion that every
excluded artifact is legally non-redistributable. A file may move onto the
allowlist only after a new artifact-specific review resolves its exact license
terms, attribution requirements, third-party exclusions, privacy concerns, and
safety conditions.
