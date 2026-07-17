---
id: HAZ-0007
type: hazard
title: Engineering-biology screening, synthesis and lifecycle failures
aliases:
  - engineering-biology non-adversarial failure classes
  - synthesis-screening and DBTL lifecycle hazards
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
relations:
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: HAZ-0007-C01
    evidence:
      - source: SRC-0033
        locator: "SRC-0033-C04; DBTL and data-feedback lifecycle, Chapters 2–5"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: HAZ-0007-C01
    evidence:
      - source: SRC-0012
        locator: "SRC-0012-C04/C08; provider order decision, record and transfer lifecycle with no implementation evidence"
  - predicate: evidenced-by
    target: SRC-0059
    claim_id: HAZ-0007-C02
    evidence:
      - source: SRC-0059
        locator: "SRC-0059-C03–C05; one blinded common-test instance, aggregate result and disagreement limits"
  - predicate: evidenced-by
    target: SRC-0061
    claim_id: HAZ-0007-C03
    evidence:
      - source: SRC-0061
        locator: "SRC-0061-C03–C05; anonymized operational corpus, aggregate decisions and causal limits"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: HAZ-0007-C04
    evidence:
      - source: SRC-0004
        locator: "SRC-0004-C04/C09/C10; material, information, transfer, disposition and incident lifecycles"
  - predicate: affects
    target: AST-0004
    claim_id: HAZ-0007-C01
    evidence:
      - source: SRC-0012
        locator: "SRC-0012-C03/C04; orders, customer state, records, equipment and product-transfer classes"
      - source: SRC-0033
        locator: "SRC-0033-C04/C05; digital design, physical build/test, material and feedback classes"
  - predicate: enables
    target: RSK-0008
    claim_id: HAZ-0007-C05
    evidence:
      - source: SRC-0012
        locator: "SRC-0012-C04/C05; review-to-fulfillment decision boundary"
      - source: SRC-0059
        locator: "SRC-0059-C04/C05; benchmark-bounded classification result and failure limits"
tags:
  - engineering-biology
  - hazard
  - non-adversarial
  - screening-error
  - synthesis-quality
  - dbtl
  - lifecycle
  - supply-continuity
---

# Engineering-biology screening, synthesis and lifecycle failures

## Canonical non-adversarial taxonomy

This page owns accidental triggers and resulting state changes across the
engineering-biology design-to-disposition lifecycle. Persistent deficient
conditions belong to `VUL-0007`; intentional actions belong to `THR-0006`.

| Hazard family | Non-adversarial trigger or transition | First affected state |
| --- | --- | --- |
| screening decision | classification, update, review or service error | pass/flag/refuse decision and order continuity |
| synthesis/build quality | specification, build, handling or identity error | physical output identity, integrity or availability |
| test/learn feedback | measurement, interpretation, record or feedback error | validation evidence and later design/decision state |
| custody/disposition/supply | accidental loss, misattribution, interruption or incorrect disposition | material/information accountability and continuity |

> **Claim record — HAZ-0007-C01 | analytic-judgment**
> **Claim:** The four-row taxonomy reconciles NASEM's digital-design→physical-
> build/test→feedback boundary with the UK's order→screening→review→decision→
> record/transfer segment, without treating an accidental failure as an
> intentional threat, persistent vulnerability or observed incident.
> **Claim status:** active
> **Scope:** Broad non-adversarial hazard classes affecting
> [AST-0004](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md) and
> the wider `WFL-0014`; not likelihood, prevalence or a universal laboratory
> process.
> **As of:** Source editions through 2026; reviewed 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C04/C05`; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> `SRC-0012-C03/C04/C08`.
> **Basis / limits:** Lifecycle functions and boundaries are direct. The
> normalized hazard families and ontology separation are analytic.

## Observed screening-decision variation in one benchmark

> **Claim record — HAZ-0007-C02 | analytic-judgment**
> **Claim:** One NIST-led blinded common-dataset study found generally high
> aggregate agreement while retaining tool-specific disagreements associated
> with definition, method and reference-data differences, establishing that
> non-adversarial screening-classification variation can occur in a bounded
> test.
> **Claim status:** active
> **Scope:** One safeguard-test instance across six evaluated tools; not six
> independent evaluations, a deployed-provider failure rate, a named current
> vulnerability, an incident or causal harm.
> **As of:** Study publication lineage 2025–2026.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
> `SRC-0059-C03`–`C05`; blinded method, aggregate benchmark result and
> disagreement/failure limits.
> **Basis / limits:** The common test and disagreements are direct. Tool
> developers supplied outputs, the corpus is bounded and results are not a
> provider-deployment census.

## Operational decision-state boundary

> **Claim record — HAZ-0007-C03 | analytic-judgment**
> **Claim:** The SecureDNA operational study reports more than 99% pass,
> 0.57% flagged and 0.27% denied/recommended-denial outcomes across its
> anonymized corpus, but these are decision states rather than hazards; a
> screening hazard exists only when an order is unintentionally misclassified,
> delayed, refused or passed contrary to the intended decision basis.
> **Claim status:** active
> **Scope:** Aggregate operational context and hazard semantics; not a claim
> that flagged/denied orders were malicious, erroneous, fulfilled or harmful.
> **As of:** Peer-reviewed article 2026; reviewed 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md),
> `SRC-0061-C03`–`C05`; version-of-record Figure 4 and operational-results
> section.
> **Basis / limits:** Outputs and corpus are direct author reports. Provider
> identities/raw orders and causal prevented-harm evidence are unavailable.

## Physical, feedback, custody and continuity hazards

> **Claim record — HAZ-0007-C04 | analytic-judgment**
> **Claim:** Accidental specification/build deviation, material or result
> misidentification, failed experimental feedback, lost provenance/custody,
> incorrect disposition and supplier/service interruption can move an approved
> digital state into an unintended physical, evidence or continuity state.
> **Claim status:** active
> **Scope:** Defensive lifecycle hazard classes; not a biological procedure,
> named incident, current-facility finding or assertion that every transition
> produces harm.
> **As of:** Source editions through 2026; reviewed 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C04/C07`; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> `SRC-0004-C04/C09/C10`; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> `SRC-0012-C04/C06`.
> **Basis / limits:** Lifecycle stages, validation, records, transfers and
> accountability objectives are direct. Their deficient transitions are an
> analytic hazard model, not observed-event evidence.

## Conditional consequence and ontology boundary

> **Claim record — HAZ-0007-C05 | analytic-judgment**
> **Claim:** `HAZ-0007` enables `RSK-0008` only when an accidental error reaches
> review, fulfillment, build, test, use or disposition before validation,
> anomaly detection, containment or correction; a hazard state alone is not a
> consequence or incident.
> **Claim status:** active
> **Scope:** Defensive causal conjunction without probability, operational
> screening logic, biological content or event attribution.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `HAZ-0007-C01`–`C04`; `SRC-0012-C04/C05`;
> `SRC-0033-C04/C07`; `SRC-0059-C04/C05`.
> **Basis / limits:** Sources establish decision and physical lifecycle gates.
> The exact-edge conjunction and ontology boundary are analytic.

## Safety boundary

No biological sequence, screening threshold/window, decision-rule detail,
evasion path, synthesis procedure, provider configuration or facility topology
is represented. Hazard descriptions remain at the level needed for defensive
control and state-transition mapping.

## Related pages

- [WFL-0014 — Design-to-disposition lifecycle](../workflows/wfl-0014-engineering-biology-design-to-disposition-lifecycle.md)
- [THR-0006 — Intentional actions](../threats/thr-0006-engineering-biology-misuse-insider-and-supply-actions.md)
- [VUL-0007 — Deficient conditions and exposures](../vulnerabilities/vul-0007-synthesis-screening-definition-database-integration-and-supply-exposures.md)
- [RSK-0008 — Conditional screening-to-fulfillment path](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [CTL-0024 — Benchmark-bounded assurance](../controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md)
- [CTL-0006 — Existing screening controls](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [SYN-0032 — Engineering-biology reconciliation](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md)
- [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md)
