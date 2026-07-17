---
id: SRC-0059
type: source
title: NIST inter-tool baseline nucleic-acid screening benchmark, 2025–2026
aliases:
  - NIST inter-tool sequence-screening benchmark
  - Laird et al. baseline nucleic-acid screening study
status: active
created: 2026-07-13
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-10-13
source_type: peer-reviewed-empirical-benchmark-and-official-program-record-package
ingest_status: complete
sensitivity: public
dual_use: moderate
raw_path: ../../raw/nist-inter-tool-screening-preprint-2025.pdf
raw_bytes: 1267558
sha256: 9b210d16102ea8af76b1adb70f011bbfd9d534f0911b69a82dd8c184af3a1df3
raw_components:
  - path: ../../raw/nist-nucleic-acid-screening-program-current-2026-07-13.html
    role: official-current-nist-program-and-benchmark-status
    bytes: 95993
    sha256: 1d7c4836976ffd1ca41d450c5ef9b781bc1bb35ec66bcc2f21fdd8c20e945806
  - path: ../../raw/nist-inter-tool-screening-publication-current-2026-07-13.html
    role: official-nist-publication-record-and-abstract
    bytes: 82497
    sha256: 1c7fc0cf469e056518c22320c744a1bfbebadb7c5521f289cf5518e521b73bc1
  - path: ../../raw/nist-inter-tool-screening-peer-reviewed-current-2026-07-13.html
    role: publisher-owned-journal-doi-landing-response
    bytes: 217818
    sha256: 06524493b6ad4072607ce1688c2d1958cb9beaf3601a9ba3023766fbffd662a9
  - path: ../../raw/nist-inter-tool-screening-doi-current-2026-07-13.json
    role: crossref-journal-article-metadata
    bytes: 11052
    sha256: 50d17eb40ebe1a2f3310f1ced8b0b2d3fa24155dfb5d78b14d6df4587f98627a
canonical_url: https://doi.org/10.1177/15356760251401228
doi: 10.1177/15356760251401228
preprint_url: https://doi.org/10.1101/2025.05.30.655379
preprint_doi: 10.1101/2025.05.30.655379
nist_publication_url: https://www.nist.gov/publications/inter-tool-analysis-nist-dataset-assessing-baseline-nucleic-acid-sequence-screening
nist_program_url: https://www.nist.gov/programs-projects/biosecurity-synthetic-nucleic-acid-sequences
accessed: 2026-07-13
publication_date: 2025-12-26
preprint_date: 2025-06-01
nist_record_date: 2025-07-10
publisher: SAGE Publications
venue: Applied Biosafety
issuers:
  - National Institute of Standards and Technology
  - SAGE Publications
jurisdictions:
  - United States
authors:
  - Tyler S. Laird
  - Kevin Flyangolts
  - Craig Bartling
  - Bryan T. Gemler
  - Jacob Beal
  - Tom Mitchell
  - Steven T. Murphy
  - Jens Berlips
  - Leonard Foner
  - Ryan Doughty
  - Felix Quintana
  - Michael Nute
  - Todd J. Treangen
  - Gene Godbold
  - Krista Ternus
  - Tessa Alexanian
  - Nicole Wheeler
  - Samuel P. Forry
tags:
  - synthetic-biology
  - nucleic-acid-synthesis
  - sequence-screening
  - empirical-benchmark
  - assurance
  - tool-comparison
  - failure-limits
  - evidence-independence
---

# NIST inter-tool baseline nucleic-acid screening benchmark, 2025–2026

## Artifact identity and reproducibility

The retained package contains the complete 30-page preprint, two official NIST
HTML records, a publisher-owned journal-DOI landing response and the Crossref
metadata response for the later journal article. It deliberately retains no
sequence examples or operational screening parameters in this wiki page.

> **Claim record — SRC-0059-C01 | artifact-observation**
> **Claim:** Five public objects totaling 1,674,918 bytes are retained with
> exact SHA-256 values, including a complete 30-page study artifact; repeat
> acquisition checks preserved identical extracted PDF text and substantive
> rendered HTML text even where build or dynamic-response bytes differed, and
> the repeated Crossref JSON was byte-identical.
> **Claim status:** active
> **Scope:** Local package identity, completeness and repeat-content
> comparison; not cryptographic issuer authentication, executable-page safety
> or scientific reproduction.
> **As of:** Retrieved and repeated 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Frontmatter paths, byte counts and SHA-256 values; PDF physical
> pp. 1–30; repeat `file`, `pdfinfo`, text/rendered-body comparison and DOI-JSON
> byte comparison.
> **Basis / limits:** Exact hashes identify the canonical retained objects.
> Temporary comparison copies are not evidence artifacts, and substantive-text
> identity does not imply byte identity or validate study conclusions.

## Publication and provenance state

The study first appeared as a bioRxiv preprint posted 2025-06-01. NIST's
publication record is dated 2025-07-10. Crossref now registers the same title
and 18-author lineage as a SAGE journal article in *Applied Biosafety*, first
published online 2025-12-26 under DOI `10.1177/15356760251401228`.

> **Claim record — SRC-0059-C02 | artifact-observation**
> **Claim:** The preprint, NIST publication/program records and registered
> journal article are publication states of one study lineage, not independent
> replications: the NIST record still carries a provisional journal citation,
> while Crossref supplies the later journal DOI and publication date and the
> retained SAGE route returned a generic publication-not-found page rather than
> a complete journal full text.
> **Claim status:** active
> **Scope:** Bibliographic identity, provenance and current retrieval state; not
> an editorial-process audit or a claim that every version is byte-identical.
> **As of:** Preprint/journal publication 2025; checked 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Preprint title page and header, physical pp. 1–4; NIST
> publication HTML lines 1–80 and 602–760; retained SAGE response; Crossref
> JSON `message.title`, `author`, `publisher`, `container-title`, `DOI`,
> `published-online` and `URL` fields.
> **Basis / limits:** Title, author lineage and dates are directly
> cross-checkable. Crossref confirms a registered journal article, but the
> publisher response retained here does not independently supply its article
> body; the complete reviewed methods/results text is the preprint artifact.

## Blinded method, operator roles and independence

> **Claim record — SRC-0059-C03 | source-report**
> **Claim:** NIST constructed and labelled a blinded 999-item test set and
> compared six screening tools: four tool developers ran the blinded set and
> returned results, while NIST ran two additional tools and then unblinded,
> analysed and discussed the results with developers.
> **Claim status:** active
> **Scope:** One inter-tool baseline-classification study; not six independent
> evaluations, provider acceptance tests or production-order deployments.
> **As of:** Study reported 2025.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Preprint Introduction/Results, physical pp. 7–10; Methods
> `Study Design`, physical pp. 20–22; title-page affiliations and `Competing
> Interests`, physical pp. 1–3.
> **Basis / limits:** Blinding, sample count and execution roles are direct.
> The authorship includes NIST and people affiliated with institutions that
> build or deploy screening software, and NIST supplied labels, analysis and
> two runs; this is developer-participating evaluation, not fully external
> independent assurance.

## Aggregate benchmark results

> **Claim record — SRC-0059-C04 | source-report**
> **Claim:** On this blinded NIST test set, every represented tool achieved at
> least 95% sensitivity and at least 97% accuracy against NIST labels;
> 923 of 999 items were unanimously classified in agreement with NIST, and a
> six-tool majority vote matched the NIST label for all 999 items.
> **Claim status:** active
> **Scope:** Aggregate test-set classification performance only; not a claim
> about live provider orders, all configurations, all sequence classes, harm
> prevention or an operational ensemble.
> **As of:** Study reported 2025.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Preprint Abstract, physical p. 4; Results `Test Dataset
> Validation`, physical pp. 9–10; Table 2, physical p. 24; Figure 1 caption,
> physical p. 25; NIST publication HTML lines 643–656.
> **Basis / limits:** The values are directly reported and Table 2 preserves
> anonymised tool-level results. Majority voting is a retrospective aggregate
> observation, not a tested deployment architecture or availability result.

## Disagreements, failure and generalisability limits

> **Claim record — SRC-0059-C05 | source-report**
> **Claim:** Forty-three items that NIST labelled concerning were missed by
> one or two tools; the paper attributes disagreements broadly to definition,
> reference-data and algorithm differences and states that actual provider
> assessment remains necessary because provider configurations can change
> outputs.
> **Claim status:** active
> **Scope:** Aggregate disagreement and deployment-generalisation boundary;
> no sequence example, tool-specific failure, screening parameter or evasion
> inference is reproduced.
> **As of:** Study reported 2025.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Preprint Results, physical pp. 10–17; Conclusion, physical
> pp. 18–19; Figure 1, physical p. 25.
> **Basis / limits:** The observed misses and stated explanation classes are
> direct. The curated test is not a production-prevalence sample; no external
> replication, provider-wide configuration study, prospective incident rate,
> prevented fulfilment or biological outcome is represented.

## Current NIST programme status

> **Claim record — SRC-0059-C06 | source-report**
> **Claim:** NIST's current programme page describes a benchmark dataset with
> known performance metrics for testing providers' baseline screening
> capabilities and calls the six-tool study fit for purpose, but the retained
> programme package supplies no provider-adoption census, conformity decision,
> live-order outcome or independent effectiveness evaluation.
> **Claim status:** active
> **Scope:** NIST programme and benchmark status visible 2026-07-13; not a
> certification, universal standard or provider deployment result.
> **As of:** Current page accessed 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** NIST programme HTML lines 631–685, especially `Selected
> Programs and Accomplishments` / `Improving Current Screening Practices`;
> NIST publication HTML lines 602–760.
> **Basis / limits:** Programme language and the benchmark role are direct.
> Its shorthand description of testing by six developers is not promoted over
> the paper's more precise four developer-run/two NIST-run method.

## Safety and assurance boundary

> **Claim record — SRC-0059-C07 | analytic-judgment**
> **Claim:** This package supplies one empirical test instance for the
> sequence-screening safeguard class: the six tools are comparators inside one
> study, not six independent safeguard instances. It distinguishes tested
> baseline classification from provider deployment, real-world effectiveness
> and independent evaluation and therefore cannot satisfy `SEB-AE` or
> `CTR-AE` by itself.
> **Claim status:** active
> **Scope:** Safe evidence accounting for screening assurance; no sequence,
> operational screening parameter, provider weakness or bypass instruction.
> **As of:** Full package review 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0059-C02`–`C06`; frozen `SEB-AE` and `CTR-AE` criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Study-lineage, operator and deployment boundaries are
> explicit. A separate operational source can complement this test evidence,
> but shared tools/authors or a common programme do not automatically create
> independent outcome evaluation.

## Related pages

- [CTL-0024 — benchmarked screening assurance](../controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md)
- [CTL-0006 — normative screening control family](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [RSK-0008 — screening-failure path](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [SYS-0006 — provider/equipment system boundary](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [SYN-0001 — frozen coverage rubric](../syntheses/syn-0001-coverage-rubric.md)
- [THR-0006 — Engineering-biology intentional threat boundary](../threats/thr-0006-engineering-biology-misuse-insider-and-supply-actions.md)
- [HAZ-0007 — Benchmark-bounded accidental failures](../hazards/haz-0007-engineering-biology-screening-synthesis-and-lifecycle-failures.md)
- [VUL-0007 — Definition/reference exposure classes](../vulnerabilities/vul-0007-synthesis-screening-definition-database-integration-and-supply-exposures.md)
- [SYN-0032 — Engineering-biology reconciliation](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)

## Sources

- Retained objects, exact canonical URLs and hashes in frontmatter.
