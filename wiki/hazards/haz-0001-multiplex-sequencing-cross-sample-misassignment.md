---
id: HAZ-0001
type: hazard
title: Cross-sample read misassignment in multiplex sequencing
aliases:
  - multiplex sequencing sample cross-talk
  - index cross-talk read misassignment
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0014
sensitivity: public
dual_use: low
hazard_kind: non-adversarial-measurement-and-demultiplexing-condition
relations:
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: HAZ-0001-C01
    evidence:
      - source: SRC-0014
        locator: "§5, printed pp. 772–773 (PDF pp. 9–10)"
  - predicate: affects
    target: AST-0001
    claim_id: HAZ-0001-C02
    evidence:
      - source: SRC-0014
        locator: "§5, printed pp. 772–773 (PDF pp. 9–10)"
  - predicate: enables
    target: RSK-0010
    claim_id: HAZ-0001-C02
    evidence:
      - source: SRC-0014
        locator: "§5, printed pp. 772–773 (PDF pp. 9–10)"
tags:
  - genomics
  - sequencing
  - multiplexing
  - non-adversarial-hazard
  - data-integrity
  - confidentiality
---

# Cross-sample read misassignment in multiplex sequencing

## Hazard

During multiplex sequencing and demultiplexing, some reads can be associated
with the wrong sample. The immediate state change is digital: one sample's
output contains reads originating from another sample. That can create both
confidentiality exposure and integrity contamination without any malicious
actor or software compromise.

> **Claim record — HAZ-0001-C01 | source-report**
> **Claim:** Ney et al. directly measured bidirectional cross-sample reads in
> one multiplex run, including 112 comparison-sample-aligned reads in one file
> and 37 experimental reads in the comparison file.
> **Claim status:** active
> **Scope:** One permitted comparison and one sequencing/index configuration;
> not a universal rate or an observed privacy/research harm.
> **As of:** 2017-08.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §5, printed pp. 772–773 (PDF pp. 9–10).
> **Basis / limits:** Direction and counts are measured. The source describes
> the estimate as rough and sensitive to configuration; it does not measure
> downstream harm or current platform behavior.

## Trigger, affected state and boundary

The non-adversarial trigger is imperfect separation/assignment of reads in a
shared run. It affects the provenance and sample association of genomic data
represented by [AST-0001](../assets/ast-0001-genomic-data.md) and can enable the
technical exposure path in
[RSK-0010](../risk-scenarios/rsk-0010-multiplex-cross-sample-digital-exposure.md).

> **Claim record — HAZ-0001-C02 | analytic-judgment**
> **Claim:** Observed cross-sample misassignment changes digital provenance and
> sample association, enabling confidentiality/integrity exposure even without
> an adversary; privacy, research or clinical consequences require additional
> downstream conditions not established here.
> **Claim status:** active
> **Scope:** Defensive hazard model for multiplex sequencing outputs.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §5, printed pp. 772–773 (PDF pp. 9–10).
> **Basis / limits:** Cross-file origin mismatch is measured. Any sensitive
> inference, malicious injection, changed scientific result or patient impact
> is source-discussed possibility rather than observed consequence.

## Distinctions and uncertainty

- This is a `HAZ`, not a `THR`: it can arise without intent.
- The measured condition is not itself a privacy breach or re-identification.
- Source-side malicious uses are hypotheses and remain separate from the
  observed counts.
- Platform, indexing, density, diversity and processing differences limit
  generalization; no current prevalence statement is made.

## Controls

[CTL-0007](../controls/ctl-0007-secure-sequencing-input-processing.md) maps sample
provenance, risk-aware separation and detection/reduction objectives to this
hazard. These are recommendations only; no safeguard test or effectiveness
result is available in `SRC-0014`.

## Related pages

- [SYN-0022 — Foundational consequence/assurance calibration](../syntheses/syn-0022-foundational-consequence-assurance-calibration.md)

- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [AST-0001](../assets/ast-0001-genomic-data.md)
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [RSK-0010](../risk-scenarios/rsk-0010-multiplex-cross-sample-digital-exposure.md)
- [CTL-0007](../controls/ctl-0007-secure-sequencing-input-processing.md)

## Sources

- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md), §5.
