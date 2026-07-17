---
id: RSK-0010
type: risk-scenario
title: Multiplex sequencing cross-sample digital exposure
aliases:
  - sample cross-talk confidentiality and integrity path
  - cross-sample read misassignment scenario
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0014
sensitivity: public
dual_use: low
origin_domain: biological
destination_domains:
  - digital
scenario_classification: observed-technical-exposure-not-incident
transfer_mechanism: shared-measurement-and-sample-association
relations:
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: RSK-0010-C01
    evidence:
      - source: SRC-0014
        locator: "§5, printed pp. 772–773 (PDF pp. 9–10)"
  - predicate: depends-on
    target: AST-0001
    claim_id: RSK-0010-C02
    evidence:
      - source: SRC-0014
        locator: "§5, printed pp. 772–773 (PDF pp. 9–10)"
  - predicate: depends-on
    target: WFL-0005
    claim_id: RSK-0010-C02
    evidence:
      - source: SRC-0014
        locator: "§§2.2–2.3 and 5, printed pp. 767 and 772–773 (PDF pp. 4 and 9–10)"
  - predicate: depends-on
    target: SYS-0003
    claim_id: RSK-0010-C02
    evidence:
      - source: SRC-0014
        locator: "§§2.2–2.3 and 5, printed pp. 767 and 772–773 (PDF pp. 4 and 9–10)"
tags:
  - genomics
  - sequencing
  - multiplexing
  - biological-to-digital
  - confidentiality
  - integrity
  - not-incident
---

# Multiplex sequencing cross-sample digital exposure

> [!WARNING]
> **Evidence classification**
> Cross-sample reads are **observed technical exposure** in one controlled
> research run. The page is not a privacy incident, re-identification event,
> malicious injection, clinical error or observed research harm.

## Scenario

Multiple physical samples share a sequencing run. A non-adversarial assignment
condition causes some derived reads to be associated with another sample's
digital output. The immediate receiving state is a provenance/sample-association
error with confidentiality and integrity implications.

> **Claim record — RSK-0010-C01 | source-report**
> **Claim:** Ney et al. measured bidirectional cross-sample assignment in one
> multiplex run: 112 comparison-sample-aligned reads in the experimental file
> and 37 experimental reads in the comparison file.
> **Claim status:** active
> **Scope:** One permitted run/configuration; not a general rate or downstream
> consequence measurement.
> **As of:** 2017-08.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §5, printed pp. 772–773 (PDF pp. 9–10).
> **Basis / limits:** Cross-file counts are direct and bidirectional. The study
> labels its estimate rough and does not establish a sensitive identity,
> corrupted conclusion or current platform behavior.

## Assets and workflow

- physical samples and their source/provenance context;
- [AST-0001](../assets/ast-0001-genomic-data.md) raw reads and sample association;
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) preparation,
  generation and analysis handoff;
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) shared
  sequencer, demultiplexing/output and downstream analysis classes;
- sample contributors and research/clinical users as possible downstream
  stakeholders, none shown harmed by this study.

## Preconditions and trust boundaries

The source-specific path requires multiplexing, imperfect read assignment,
shared measurement context and downstream reliance on sample association.
Actual consequence depends on what the misassigned reads reveal or change and
whether validation detects them.

## Origin-domain and cross-domain transfer

The origin state is multiple physical samples sharing measurement. The transfer
through sequencing and sample assignment converts the physical mixture/run
condition into a digital provenance error. The immediate condition is captured
by [HAZ-0001](../hazards/haz-0001-multiplex-sequencing-cross-sample-misassignment.md).

> **Claim record — RSK-0010-C02 | analytic-judgment**
> **Claim:** The complete observed technical path is `shared physical samples
> → sequencing/demultiplexing → cross-sample reads → incorrect digital sample
> association`, creating confidentiality/integrity exposure without requiring
> an adversary or cyber compromise.
> **Claim status:** active
> **Scope:** One controlled multiplex run mapped to the genomic workflow and
> system classes; not a universal architecture or consequence claim.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §§2.2–2.3 and 5, printed pp. 767 and 772–773
> (PDF pp. 4 and 9–10).
> **Basis / limits:** The material-to-read-to-file transition and bidirectional
> mismatches are observed. The wiki labels the resulting security properties;
> no person, diagnosis or scientific conclusion was evaluated.

## Immediate and downstream consequences

Immediate: reads in a file have the wrong sample provenance. Possible later
effects include information exposure or distorted analysis, but the source's
adversarial and harm scenarios are hypothetical.

> **Claim record — RSK-0010-C03 | analytic-judgment**
> **Claim:** `SRC-0014` supports observed technical confidentiality/integrity
> exposure only; malicious injection, sensitive inference, privacy harm,
> research invalidity and clinical/biological consequence remain hypothetical
> or unmeasured.
> **Claim status:** active
> **Scope:** Consequence boundary for the measured cross-sample result.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §5, printed pp. 772–773 (PDF pp. 9–10); Conclusions,
> printed p. 778 (PDF p. 15).
> **Basis / limits:** Counts are measured; later harms are discussed as
> possibilities. This prevents a technical exposure from becoming a fictional
> `INC` or re-identification claim.

## Controls by function

[CTL-0007](../controls/ctl-0007-secure-sequencing-input-processing.md) maps sample
provenance, risk-aware run separation, cross-sample detection/reduction,
result validation and affected-analysis review to exact edges. The source
recommends these functions but does not test their effectiveness.

## Assumptions and uncertainty

- configuration substantially affects transfer rate;
- the measured corpus is one run and not representative;
- downstream sensitivity and reliance determine consequence;
- current platform behavior and operational safeguards are unknown;
- adversarial use must not be inferred from a non-adversarial observation.

## Related scenarios

- [RSK-0009](rsk-0009-sequenced-input-to-digital-execution.md)
- [RSK-0004](rsk-0004-genomic-data-disclosure-kin-privacy.md)
- [RSK-0005](rsk-0005-permitted-genomic-processing-privacy-harm.md)

## Sources

- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md), §5.
