---
id: VUL-0007
type: vulnerability
title: Synthesis-screening definition, database, integration and supply exposure classes
aliases:
  - nucleic-acid screening and lifecycle weakness classes
  - engineering-biology screening dependency exposures
status: active
created: 2026-07-13
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-10-13
source_ids:
  - SRC-0004
  - SRC-0012
  - SRC-0033
  - SRC-0059
  - SRC-0061
sensitivity: public
dual_use: low
vulnerability_status: mixed-benchmark-observed-and-generic-source-supported-current-instance-status-unknown
relations:
  - predicate: evidenced-by
    target: SRC-0059
    claim_id: VUL-0007-C01
    evidence:
      - source: SRC-0059
        locator: "SRC-0059-C03–C05; blinded common test, aggregate results and definition/database/method disagreement limits"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: VUL-0007-C03
    evidence:
      - source: SRC-0012
        locator: "SRC-0012-C04–C06; customer/order review, records, equipment integration and transfer accountability"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: VUL-0007-C04
    evidence:
      - source: SRC-0004
        locator: "SRC-0004-C06/C07/C09; cyber/service assurance, inventory, transfer and disposition accountability"
  - predicate: evidenced-by
    target: SRC-0061
    claim_id: VUL-0007-C05
    evidence:
      - source: SRC-0061
        locator: "SRC-0061-C03–C06; operational deployment context and developer-led/raw-data/causal limits"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: VUL-0007-C02
    evidence:
      - source: SRC-0033
        locator: "SRC-0033-C04/C05/C07; DBTL dependencies, provenance, validation and assurance functions"
  - predicate: affects
    target: SYS-0006
    claim_id: VUL-0007-C03
    evidence:
      - source: SRC-0012
        locator: "SRC-0012-C03–C06; provider, vendor, equipment and information boundaries"
      - source: SRC-0059
        locator: "SRC-0059-C03–C05; evaluated screening-tool boundary"
  - predicate: enables
    target: RSK-0008
    claim_id: VUL-0007-C06
    evidence:
      - source: SRC-0012
        locator: "SRC-0012-C04/C05; screening/review-to-fulfillment lifecycle"
      - source: SRC-0059
        locator: "SRC-0059-C04/C05; bounded classification disagreements and failure limits"
tags:
  - engineering-biology
  - vulnerability
  - sequence-screening
  - definitions
  - reference-data
  - integration
  - provenance
  - supply-chain
  - continuity
---

# Synthesis-screening definition, database, integration and supply exposure classes

## Exposure envelope

This page owns deficient conditions that can permit a screening, synthesis or
later lifecycle error to persist or cross a boundary. It does not label a
screening tool, database, provider, equipment item or external service as a
vulnerability merely because it exists.

| Exposure family | Canonical deficient condition | Current-instance state |
| --- | --- | --- |
| definition/decision basis | ambiguous, inconsistent or insufficiently versioned interpretation | benchmark-specific variation observed; general status unknown |
| reference data/change | incomplete, stale, unattributed or inadequately validated reference/update state | generic; current provider state unknown |
| integration/provenance | weak binding among order, customer, decision/version, physical output, test and record | generic; current provider/equipment state unknown |
| supply/coverage/continuity | critical provider, tool, database, service or equipment dependency lacks assured coverage or continuity | generic; current deployment state unknown |

## Benchmark-observed definition and reference sensitivity

> **Claim record — VUL-0007-C01 | source-report**
> **Claim:** In one blinded NIST-led common-dataset study, evaluated tools
> generally agreed at high aggregate levels but retained tool-specific
> disagreements that the authors associated with differences in definitions,
> methods and reference-data choices.
> **Claim status:** active
> **Scope:** Benchmark-specific variation in evaluated tool versions; not a
> product vulnerability disclosure, current provider weakness, deployment
> census, exploitability result or six independent safeguard tests.
> **As of:** Study publication lineage 2025–2026.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
> `SRC-0059-C03`–`C05`; blinded method, aggregate results and disagreement
> analysis.
> **Basis / limits:** The observed disagreements and author-attributed classes
> are direct. The common corpus, developer-supplied outputs and bounded tool
> versions limit generalization.

## Canonical weakness conditions

> **Claim record — VUL-0007-C02 | analytic-judgment**
> **Claim:** Definition and reference-data differences become canonical
> vulnerabilities only when ambiguity, incompleteness, stale state, weak
> version/provenance control or inadequately validated change can produce a
> wrong decision that is not detected and corrected at the intended review
> gate.
> **Claim status:** active
> **Scope:** Defensive deficient-state semantics; no screening rule, database
> content, current named instance, exploit route, severity score or frequency.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `VUL-0007-C01`;
> [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C04/C05/C07`; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> `SRC-0012-C04/C05/C08`.
> **Basis / limits:** NIST supplies one concrete comparison; NASEM and UK
> sources establish lifecycle, provenance, review and validation functions.
> Expressing their deficient state as a vulnerability is analytic.

## Integration, identity and lifecycle-record exposures

> **Claim record — VUL-0007-C03 | analytic-judgment**
> **Claim:** A provider or equipment workflow is exposed when customer/order
> identity, screening result and version, authorization/review, synthesized
> output, test evidence, transfer and disposition records are not reliably
> bound, attributable and carried across the relevant lifecycle handoffs.
> **Claim status:** active
> **Scope:** Generic integration/provenance conditions affecting
> [SYS-0006](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
> and the broader `WFL-0014`; not a finding that any named organization has
> these weaknesses.
> **As of:** Source editions through 2026; reviewed 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> `SRC-0012-C03`–`C06`; [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C04/C05/C07`; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> `SRC-0004-C04/C09`.
> **Basis / limits:** Identity, records, transfer, validation and provenance
> functions are direct. Their inadequate implementation is a generic exposure
> class with unknown current-instance status.

## Supply, service, coverage and continuity exposures

> **Claim record — VUL-0007-C04 | analytic-judgment**
> **Claim:** Screening-provider, reference-data, external-service, equipment
> and material dependencies form vulnerability classes only when a critical
> dependency lacks adequate integrity/availability assurance, monitoring,
> controlled fallback, continuity or lifecycle coverage.
> **Claim status:** active
> **Scope:** Generic dependency and incomplete-coverage conditions; not a
> provider list, architecture, outage, adoption estimate or claim that
> centralization/decentralization is inherently vulnerable.
> **As of:** Source editions through 2026; reviewed 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> `SRC-0004-C06/C07/C09`; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> `SRC-0012-C03/C04/C06`; [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C05/C07`.
> **Basis / limits:** Dependency, lifecycle and assurance functions are direct.
> The deficient-state conjunction and its grouping are analytic.

## Current-instance and evidence boundary

> **Claim record — VUL-0007-C05 | analytic-judgment**
> **Claim:** Only benchmark-specific disagreement among evaluated tool versions
> is represented as concrete; the SecureDNA paper demonstrates one anonymized,
> developer-led operational integration lineage but cannot establish a
> provider vulnerability census because provider identities and raw orders are
> unavailable and no independent causal effectiveness evaluation is supplied.
> **Claim status:** active
> **Scope:** Vulnerability-state and evidence calibration; not a claim that an
> anonymous provider is vulnerable or that operational screening failed.
> **As of:** Evidence package reviewed 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `VUL-0007-C01`–`C04`;
> [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md),
> `SRC-0061-C03`–`C06`.
> **Basis / limits:** Operational corpus and evidence limits are direct or
> explicitly bounded. All named-provider/equipment current-instance states
> remain unknown.

## Conditional consequence

> **Claim record — VUL-0007-C06 | analytic-judgment**
> **Claim:** These exposure classes enable `RSK-0008` only when the deficient
> state affects a relevant order or design and passes review, validation and
> containment gates into fulfillment, build, use or disposition; inventory,
> integration or an aggregate flag alone is not a compromise or consequence.
> **Claim status:** active
> **Scope:** Defensive exact-edge model without provider topology, screening
> logic, biological content, exploit path, probability or incident attribution.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `VUL-0007-C01`–`C05`; `SRC-0012-C04/C05`;
> `SRC-0033-C04/C07`; `SRC-0059-C04/C05`.
> **Basis / limits:** Sources establish the relevant decision and physical
> gates; the causal conjunction is analytic and context-specific.

## Safety boundary

No biological sequence or example, exact matching threshold/window, database
content, screening implementation, evasion mechanic, provider configuration,
credential, endpoint, cost or infrastructure detail is represented.

## Related pages

- [WFL-0014 — Design-to-disposition lifecycle](../workflows/wfl-0014-engineering-biology-design-to-disposition-lifecycle.md)
- [THR-0006 — Intentional actions](../threats/thr-0006-engineering-biology-misuse-insider-and-supply-actions.md)
- [HAZ-0007 — Non-adversarial failure transitions](../hazards/haz-0007-engineering-biology-screening-synthesis-and-lifecycle-failures.md)
- [SYS-0006 — Screening system boundary](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [RSK-0008 — Conditional consequence path](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [CTL-0024 — Benchmark-bounded assurance](../controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md)
- [CTL-0006 — Existing screening controls](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [SYN-0032 — Engineering-biology reconciliation](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md)
- [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md)
