---
id: CTL-0007
type: control
title: Secure sequencing input, bioinformatics processing and sample separation
aliases:
  - defensive biological-input processing controls
  - sequencing cross-talk and parser safeguards
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0006
  - SRC-0014
sensitivity: public
dual_use: low
control_status: recommended
implementation_status: unknown
testing_status: unknown
effectiveness_status: unknown
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: CTL-0007-C01
    evidence:
      - source: SRC-0014
        locator: "§7.3, printed p. 777 (PDF p. 14)"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: CTL-0007-C02
    evidence:
      - source: SRC-0005
        locator: "§4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24); §4.4.2, printed pp. 20–22 (PDF pp. 29–31)"
      - source: SRC-0006
        locator: "§5.1, printed pp. 22–23 (PDF pp. 33–34); Tables 10–25 and 33, printed pp. 64–140 and 155–158"
  - predicate: mitigates
    target: RSK-0009
    claim_id: CTL-0007-C03
    evidence:
      - source: SRC-0014
        locator: "§§3, 6 and 7.3, printed pp. 768–777 (PDF pp. 5–14)"
      - source: SRC-0005
        locator: "§4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24); §4.4.2, printed pp. 20–22 (PDF pp. 29–31)"
      - source: SRC-0006
        locator: "§5.1, printed pp. 22–23 (PDF pp. 33–34); Tables 10–25 and 33"
  - predicate: detects
    target: HAZ-0001
    claim_id: CTL-0007-C04
    evidence:
      - source: SRC-0014
        locator: "§§5 and 7.3, printed pp. 772–773 and 777 (PDF pp. 9–10 and 14)"
  - predicate: mitigates
    target: RSK-0010
    claim_id: CTL-0007-C04
    evidence:
      - source: SRC-0014
        locator: "§§5 and 7.3, printed pp. 772–773 and 777 (PDF pp. 9–10 and 14)"
      - source: SRC-0006
        locator: "§5.1, printed pp. 22–23 (PDF pp. 33–34); Tables 10–25 and 33"
tags:
  - genomics
  - bioinformatics
  - secure-input
  - sample-provenance
  - cross-sample-detection
  - recommended-control
---

# Secure sequencing input, bioinformatics processing and sample separation

## Objective

Interrupt reverse material/input→digital risk at the intake, measurement,
derived-data, parser, monitoring and recovery edges. The family combines:

- accountable material/sample provenance and trust classification;
- secure software implementation, bounds/input validation and review;
- controlled package/update and data authenticity;
- least-privilege isolation and failure containment for downstream processing;
- risk-aware multiplex separation plus detection/reduction of cross-sample
  reads; and
- review/recovery of affected outputs and dependent decisions.

These are control objectives, not product configurations or operational SOPs.

## Evidence state

| Dimension | Status | Evidence boundary |
| --- | --- | --- |
| Recommended | **Yes** | USENIX recommendations plus NIST genomic risk-management outcomes |
| Implemented | **Unknown** | No defined operational deployment record |
| Tested | **Unknown** | Experiments measured risks, not deployed safeguards |
| Effective | **Unknown** | No prevented-event or outcome comparison |
| Independently evaluated | **Unknown** | No independent deployment/control evaluation |

> **Claim record — CTL-0007-C01 | source-report**
> **Claim:** Ney et al. recommend secure coding/input validation, memory-safe
> handling or bounds checks, security review, managed patch/authenticity,
> sample provenance, risk-aware sample separation and technical cross-sample
> detection/reduction.
> **Claim status:** active
> **Scope:** Author recommendations for sequencing and analysis pipelines; not
> implementation guidance, deployment evidence or effectiveness.
> **As of:** 2017-08.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §7.3, printed p. 777 (PDF p. 14).
> **Basis / limits:** Control families are direct. The source tests risk
> mechanisms, not the safeguards, and its operational offensive detail is not
> reproduced.

### Independent normative lineage

NIST IR 8432 and IR 8467 independently contribute lifecycle inventory,
provenance, software/data integrity, control assessment, monitoring, incident
response and trustworthy recovery objectives for genomic generation/analysis.
The two NIST IDs are one programme lineage; together they are independent of the
University of Washington study, not independent of each other.

> **Claim record — CTL-0007-C02 | source-report**
> **Claim:** The NIST genomic corpus recommends inventory/provenance,
> integrity-aware processing, assessment, monitoring, response and recovery
> outcomes across generation and analysis dependencies.
> **Claim status:** active
> **Scope:** General US NIST genomic risk-management outcomes; not a direct
> cross-talk benchmark or validated parser control.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24); §4.4.2,
> printed pp. 20–22 (PDF pp. 29–31);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §5.1, printed pp. 22–23 (PDF pp. 33–34); Tables 10–25 and 33.
> **Basis / limits:** Functions and target outcomes are direct. Both NIST
> sources share one programme lineage and contain no deployment or measured
> safeguard outcome.

## Scenario edges addressed

### RSK-0009 — material/input to software execution

| Edge | Control objective | Failure boundary |
| --- | --- | --- |
| input acceptance | establish provenance, trust and allowed processing context | provenance does not make an input intrinsically safe |
| measurement→file | preserve source association and validate derived state | validation coverage and error tolerance need defined tests |
| file→parser | safe memory/input handling, review and authenticated dependencies | compatible unknown weakness or stale dependency may remain |
| parser→execution | isolation, least privilege and behavior/failure monitoring | sandbox escape/coverage are not assumed |
| execution/failure→containment and recovery | contain the affected process, identify affected digital state and restore trusted software/data versions | restoration does not prove that every effect was contained or that separate downstream dependencies are fit for use |

> **Claim record — CTL-0007-C03 | analytic-judgment**
> **Claim:** Across independent USENIX and NIST lineages, `CTL-0007`
> conditionally maps prevention, detection, containment and recovery to the
> input→measurement→file→parser→execution→containment/recovery edges of
> `RSK-0009`, but no edge has implementation or effectiveness evidence.
> **Claim status:** active
> **Scope:** Genomic sequencing/analysis environments with the documented
> reverse-direction dependency; no named deployment.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** medium
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §§3, 6 and 7.3, printed pp. 768–777 (PDF pp. 5–14);
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §4.1 and Table 1, printed pp. 13–15; §4.4.2, printed pp. 20–22;
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §5.1 and Tables 10–25 and 33.
> **Basis / limits:** The study supplies exact risk edges/recommendations and
> NIST supplies independent lifecycle/assurance functions. Convergence supports
> relevance, not implementation or risk reduction.

### RSK-0010 — cross-sample exposure

| Edge | Control objective | Failure boundary |
| --- | --- | --- |
| sample→shared run | classify source trust and separate combinations when risk requires | separation affects capacity/cost and is not always necessary |
| run→sample association | detect/reduce cross-sample assignment and preserve provenance | method performance is platform/configuration-specific |
| suspect reads→analysis | validate outputs, quarantine/review suspect state | false positives/negatives and residual contamination remain |
| affected result→later use | trace dependent analyses/decisions and correct or rerun where justified | no universal materiality threshold is established |

> **Claim record — CTL-0007-C04 | analytic-judgment**
> **Claim:** Sample trust/separation, cross-sample detection/reduction, output
> validation and affected-analysis review conditionally detect `HAZ-0001` and
> mitigate `RSK-0010`; no source reports a deployed detection rate, acceptance
> criterion or downstream outcome benefit.
> **Claim status:** active
> **Scope:** Multiplex sequencing confidentiality/integrity exposure at safe
> functional abstraction.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §§5 and 7.3, printed pp. 772–773 and 777 (PDF pp. 9–10 and 14);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §5.1 and Tables 10–25 and 33.
> **Basis / limits:** Source recommendations map directly to measured
> association errors; NIST provides broader provenance/monitoring/recovery
> objectives. Neither source tests these safeguards in the measured run.

## Applicability and prerequisites

- a bounded sample→generation→analysis workflow and responsible owners;
- explicit sample/data provenance and trust assumptions;
- software/dependency inventory and supported update paths;
- defined input and result validation with failure handling;
- isolation and recovery boundaries appropriate to downstream consequence;
- traceability from a suspect run/file to affected analyses and decisions; and
- validation criteria that measure both detection and operational side effects.

## Dependencies

- [AST-0001](../assets/ast-0001-genomic-data.md) for material, read, association and
  provenance states;
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) for intake,
  generation, analysis, sharing and disposition edges;
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) for
  instrument, software, repository and responsibility boundaries;
- maintained software/build provenance and accountable sample/run governance.

## Failure modes and tradeoffs

- provenance checks can be complete yet parser behavior unsafe;
- validation can miss unknown malformed states or reject legitimate variation;
- isolation can limit performance and still fail if privileges/boundaries are
  mis-scoped;
- patch centralization can create availability and supply-chain dependencies;
- strict sample separation can reduce throughput and increase cost;
- cross-sample filtering can remove valid signal or leave residual reads;
- rerun/recovery can restore service without repairing downstream decisions;
- a control catalog or recommendation can create false assurance without test
  evidence.

## Validation and evidence of effectiveness

Required evidence would define target workflow/software versions, seeded and
natural test conditions, positive and null cases, detection/miss rates,
containment behavior, affected-output traceability, recovery acceptance,
performance/cost impact and independent evaluator limitations. None is present
in the current corpus.

## Safety boundary

The page contains control functions and test requirements only. It omits
sequence/payload/code, target configuration, exact crash inputs, offensive
adaptations and screening-evasion detail.

## Related pages

- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [RSK-0009](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md)
- [RSK-0010](../risk-scenarios/rsk-0010-multiplex-cross-sample-digital-exposure.md)
- [HAZ-0001](../hazards/haz-0001-multiplex-sequencing-cross-sample-misassignment.md)
- [VUL-0001](../vulnerabilities/vul-0001-unsafe-bioinformatics-input-handling.md)
- [CTL-0002](ctl-0002-genomic-data-risk-management.md)
- [SYN-0007 — Cross-sector exact control-edge portfolio](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)

## Sources

- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md).
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md).
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md).
