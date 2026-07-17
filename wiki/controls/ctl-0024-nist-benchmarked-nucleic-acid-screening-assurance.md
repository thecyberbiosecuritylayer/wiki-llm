---
id: CTL-0024
type: control
title: NIST-benchmarked nucleic-acid screening assurance
aliases:
  - baseline sequence-screening benchmark assurance
  - NIST screening test and operational-evidence control
status: active
created: 2026-07-13
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-10-13
source_ids:
  - SRC-0059
  - SRC-0061
sensitivity: public
dual_use: moderate
control_status: normative-screening-family-with-benchmark-and-bounded-operational-evidence
implementation_status: bounded-operational-data-application-not-prospective-provider-deployment-confirmed
testing_status: one-blinded-999-item-six-tool-benchmark
effectiveness_status: aggregate-classification-and-workflow-output-results-no-causal-harm-effect
independent_evaluation_status: absent-for-the-overlapping-safeguard-instance
relations:
  - predicate: evidenced-by
    target: SRC-0059
    claim_id: CTL-0024-C02
    evidence:
      - source: SRC-0059
        locator: "SRC-0059-C03/C04/C05; preprint Results pp. 9–18, Methods pp. 20–22, Table 2 p. 24 and Figure 1 p. 25"
  - predicate: evidenced-by
    target: SRC-0061
    claim_id: CTL-0024-C05
    evidence:
      - source: SRC-0061
        locator: "SRC-0061-C03/C04/C05; version-of-record Abstract, Quantifying specificity using real-world synthesis data, Figure 4, Author contributions and Data availability"
  - predicate: depends-on
    target: CTL-0006
    claim_id: CTL-0024-C01
    evidence:
      - source: SRC-0059
        locator: "SRC-0059-C06; NIST programme HTML lines 631–685"
  - predicate: detects
    target: RSK-0008
    claim_id: CTL-0024-C03
    evidence:
      - source: SRC-0059
        locator: "SRC-0059-C04/C05; preprint Results pp. 9–18, Table 2 p. 24 and Figure 1 p. 25"
  - predicate: depends-on
    target: SYS-0006
    claim_id: CTL-0024-C04
    evidence:
      - source: SRC-0059
        locator: "SRC-0059-C05; preprint Conclusion pp. 18–19 and Study Design pp. 20–22"
      - source: SRC-0061
        locator: "SRC-0061-C03/C05; operational dataset scope, Data availability and Author contributions"
tags:
  - synthetic-biology
  - nucleic-acid-synthesis
  - sequence-screening
  - benchmark
  - assurance
  - provider-configuration
  - operational-evidence
  - evidence-independence
---

# NIST-benchmarked nucleic-acid screening assurance

## Objective and evidence ladder

Use a versioned, blinded and reviewable baseline test to assess the screening
capability actually used in a provider context, record aggregate error and
disagreement limits, and route an unacceptable or stale result to accountable
review before relying on it for an order decision. This assurance layer does
not replace customer legitimacy review, refusal/reporting, records, security or
equipment-lifecycle functions in
[CTL-0006](ctl-0006-nucleic-acid-order-and-equipment-screening.md).

| Evidence rung | Current evidence | Boundary |
| --- | --- | --- |
| Recommended/normative | `CTL-0006` contains US/UK screening criteria; NIST describes a provider baseline-test programme | the represented package does not make this exact benchmark universally mandatory |
| Tested | one blinded 999-item, six-tool NIST study with aggregate sensitivity, accuracy and disagreement results | one study lineage; four developer-run and two NIST-run tools |
| Operational-data application | the overlapping SecureDNA system was applied to a large anonymized historical provider-order corpus | implementation is not confirmed; not proof that every order was prospectively screened before fulfilment |
| Effective | classification metrics and aggregate pass/flag/denial workflow outputs are measured | no causal unsafe-fulfilment, incident or harm-reduction outcome |
| Independently evaluated | no | developer/tool affiliations in both studies; provider identities/raw orders unavailable in the operational study |

> **Claim record — CTL-0024-C01 | analytic-judgment**
> **Claim:** `CTL-0024` is a benchmark-assurance layer within `CTL-0006`: it
> tests the order-recognition function and preserves a reviewable result, but
> depends on the broader identity, human-decision, fulfilment, record, security
> and lifecycle controls rather than replacing them.
> **Claim status:** active
> **Scope:** Defensive control-family placement; not a new screening standard,
> provider mandate, compliance conclusion or effectiveness result.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [CTL-0006](ctl-0006-nucleic-acid-order-and-equipment-screening.md),
> `CTL-0006-C01`–`C04`;
> [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
> `SRC-0059-C06`.
> **Basis / limits:** The normative family and NIST baseline-test role are
> direct. Their placement as one assurance layer is wiki normalization.

## Tested baseline performance

> **Claim record — CTL-0024-C02 | source-report**
> **Claim:** One blinded NIST benchmark compared six tools on 999 labelled
> items; all reached at least 95% sensitivity and at least 97% accuracy,
> 923 items had unanimous agreement with NIST, and a retrospective six-tool
> majority matched all NIST labels.
> **Claim status:** active
> **Scope:** Aggregate baseline-classification test evidence; not six
> independent safeguard instances, production performance or an operational
> ensemble control.
> **As of:** Study reported 2025; publication state reviewed 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
> `SRC-0059-C03/C04`; preprint Results, physical pp. 9–10; Table 2,
> physical p. 24; Figure 1, physical p. 25.
> **Basis / limits:** Design and values are direct. The four developer-run/two
> NIST-run roles and common study team preclude six-way independence.

## Exact scenario edge detected

> **Claim record — CTL-0024-C03 | analytic-judgment**
> **Claim:** The benchmark can detect a bounded `RSK-0008` failure at the
> screening-capability/configuration→classification edge by exposing labelled
> misses, false decisions and inter-tool disagreement before that
> classification is relied on; it does not test the later customer-review,
> approval→fulfilment, equipment-access or downstream biological edges.
> **Claim status:** active
> **Scope:** Conditional exact-edge mapping; no screening rule, sequence,
> threshold implementation, bypass method or universal mitigation assertion.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [RSK-0008](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md),
> `RSK-0008-C01/C02`; `SRC-0059-C04/C05`.
> **Basis / limits:** NIST-labelled items and measured classifications support
> the bounded detection claim. `SRC-0061` supplies operational context only:
> its aggregate decisions have no public ground truth and are not detection
> evidence. Exact edge placement is defensive analysis, and neither study
> observes unsafe fulfilment or biological harm.

## Provider-system and configuration dependency

> **Claim record — CTL-0024-C04 | analytic-judgment**
> **Claim:** Assurance must attach to the actual screening dependency and
> provider context in `SYS-0006`, because the NIST study states that provider
> configurations can change outputs and that tool-developer testing does not
> substitute for provider assessment.
> **Claim status:** active
> **Scope:** Version/configuration and deployment prerequisite at safe
> abstraction; not a configuration recipe, provider architecture or claim that
> every update requires the same test design.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SYS-0006](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md),
> `SYS-0006-C01/C02`; `SRC-0059-C05`, preprint Conclusion, physical
> pp. 18–19; `SRC-0061-C03/C05`.
> **Basis / limits:** Provider/configuration dependence is direct in the NIST
> paper. Attaching evidence to the represented system boundary is analytic;
> neither source supplies a provider-wide configuration inventory.

## One bounded operational complement

> **Claim record — CTL-0024-C05 | analytic-judgment**
> **Claim:** SecureDNA is the one named safeguard that overlaps the NIST
> comparison and the operational study: the latter applies it to anonymized
> historical orders covering more than 150,000 genes/oligonucleotides and more
> than 67 million nucleotides across participating providers in three regions
> and reports aggregate pass/flag/denial outputs.
> **Claim status:** active
> **Scope:** One benchmark-plus-operational-data safeguard instance; not a
> provider census, six deployed tools, prospective screening of every order,
> adoption prevalence or observed prevention of harm.
> **As of:** Operational study version of record 2026-02-16.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0059-C03/C07`;
> [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md),
> `SRC-0061-C03/C04`.
> **Basis / limits:** Tool overlap, corpus and aggregate outputs are direct.
> The two studies provide complementary test and operational-data roles, but
> shared tool/developer participation prevents treating them as independent
> effectiveness confirmation.

## Failure, tradeoff and independence limits

> **Claim record — CTL-0024-C06 | analytic-judgment**
> **Claim:** The evidence retains positive and failure results—high aggregate
> benchmark scores alongside 43 NIST-labelled concerning items missed by one
> or two tools—but lacks a fully independent evaluator for the overlapping
> safeguard, public raw operational orders, provider-level replication,
> prospective unsafe-fulfilment outcomes or a causal comparator.
> **Claim status:** active
> **Scope:** Evidence limits and null/failure accounting; not disclosure of
> item examples, tool-specific weaknesses or operational screening parameters.
> **As of:** Full source-pair review 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0059-C03/C05`; `SRC-0061-C05/C06`.
> **Basis / limits:** Miss counts, contributor roles and data-availability
> limits are direct. Absence of represented causal evidence is not evidence
> that screening had no benefit.

## Rubric contribution and non-multiplication rule

> **Claim record — CTL-0024-C07 | analytic-judgment**
> **Claim:** For `SEB-AE` and `CTR-AE`, this page contributes exactly one
> tested safeguard instance with a bounded operational-data complement,
> metrics and a failure result: the SecureDNA overlap. The other five
> benchmark comparators are not counted as deployed instances, and neither
> study supplies the independent evaluation
> or causal effectiveness needed for an `SEB-AE` pass or to complete the
> cross-sector `CTR-AE` portfolio.
> **Claim status:** active
> **Scope:** Frozen-rubric evidence accounting; not a change to the rubric
> score, certification or comparative product ranking.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `CTL-0024-C02`–`C06`; frozen `SEB-AE` and `CTR-AE` criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Instance counting follows safeguard/tool overlap and
> claim-appropriate lineage roles. Publication multiplicity, six tool rows and
> one operational corpus are not seven independent safeguards or evaluators.

## Applicability and prerequisites

- bind the result to the actual provider tool, version, configuration and
  relevant decision context rather than a generic product label;
- use a representative, versioned and labelled test with an explicit reference
  basis, scope and known blind spots;
- define accountable review, acceptance, escalation and retest decisions
  before relying on a score;
- retain the identity, authorization, record, fulfilment and equipment
  controls in CTL-0006 around the tested classification edge; and
- trigger reassessment after material tool, reference-data, configuration,
  workflow or policy change.

These prerequisites are necessary for applicability. Their presence does not
prove implementation, conformity or effectiveness.

## Failure modes and tradeoffs

- stale or non-representative tests can miss configuration-specific failures;
- benchmark optimization can improve the score without proving production
  generalisability;
- false decisions can either burden legitimate work or miss items requiring
  review;
- unavailable raw operational orders limit independent reproduction;
- screening accuracy cannot compensate for missing identity, authority,
  fulfilment, record, security or equipment-lifecycle controls.

## Safety boundary

This page contains no biological sequence or example, screening parameter,
tool-specific weakness, decision rule, provider architecture, credential,
evasion path or bypass instruction. Only aggregate defensive metrics, exact
evidence states and high-level control edges are retained.

## Related pages

- [CTL-0006 — broader screening control family](ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [RSK-0008 — exact bounded failure edge](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [SYS-0006 — provider-system dependency](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [SRC-0059 — blinded benchmark](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md)
- [SRC-0061 — operational complement](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md)
- [SYN-0001 — frozen evidence criteria](../syntheses/syn-0001-coverage-rubric.md)
- [SYN-0032 — Engineering-biology reconciliation](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)

## Sources

- [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
  `SRC-0059-C01`–`C07`.
- [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md),
  `SRC-0061-C01`–`C06`.
