---
id: CTL-0019
type: control
title: Animal-disease traceability performance and assurance controls
aliases:
  - U.S. ADT trace exercises and audit
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0041
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0041
    claim_id: CTL-0019-C01
    evidence:
      - source: SRC-0041
        locator: "SRC-0041-C03–C09; 9 CFR Part 86; APHIS performance PDF pp. 1–4; OIG PDF pp. 1–7 and 20–22"
  - predicate: depends-on
    target: WFL-0012
    claim_id: CTL-0019-C01
    evidence:
      - source: SRC-0041
        locator: "9 CFR §§86.1–86.5 identification, records, movement and trace functions"
  - predicate: mitigates
    target: HAZ-0004
    claim_id: CTL-0019-C05
    evidence:
      - source: SRC-0041
        locator: "OIG PDF pp. 1–5; traceability supports disease-spread control, with conditional and failed-trace limits"
tags:
  - agriculture
  - animal-health
  - traceability
  - identification
  - exercise
  - assurance
  - independent-audit
---

# Animal-disease traceability performance and assurance controls

## Exact-edge control map

| Function/evidence state | Exact edge | Represented evidence | Boundary |
| --- | --- | --- | --- |
| Binding design | herd/animal/group/premises → identifier/document → movement record | 9 CFR Part 86 | Interstate covered-livestock scope and exceptions |
| Implemented | State/Tribal/Federal cooperator record retrieval and trace work | APHIS ADT since 2013 | Issuer-reported national programme, not every animal |
| Tested | four traceback/trace-forward TPM exercises with elapsed time | APHIS 2013–2022 series | Method and coverage changed in 2020 |
| Positive scoped result | 490-hour baseline to 11.5 hours in year six; later table values near/below one hour | APHIS metric | Association across programme years, not isolated causality |
| Independent evaluation | OIG review of 11 represented disease incidents and programme oversight | USDA OIG | Non-statistical three-State sample |
| Failure/limit | one unsuccessful traceback; four gap classes and incomplete risk analysis | USDA OIG | Not a national failure rate or null programme verdict |

> **Claim record — CTL-0019-C01 | analytic-judgment**
> **Claim:** Binding identification/record/movement requirements and the
> implemented ADT programme map animal/herd state through official records to
> traceback/trace-forward response edges in `WFL-0012`.
> **Claim status:** active
> **Scope:** Functional animal-disease traceability; not disease prevention,
> universal coverage, cyber defense, live implementation census or outcome.
> **As of:** eCFR snapshot 2026-07-09; programme evidence through 2022.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0041](../sources/src-0041-us-animal-disease-traceability-herd-performance-audit.md),
> `SRC-0041-C03`–`C05`; [WFL-0012](../workflows/wfl-0012-animal-plant-health-surveillance-movement-response-lifecycle.md).
> **Basis / limits:** Design and implementation are direct across regulation
> and issuer report; they are not effectiveness by themselves.

## Test metric and positive result

> **Claim record — CTL-0019-C02 | source-report**
> **Claim:** APHIS defines four trace exercises, a start/end elapsed-time
> measure and a national baseline/comparison series, with combined TPM 2–4
> average time falling from 490 to 11.5 hours by year six.
> **Claim status:** active
> **Scope:** APHIS-reported exercise performance for covered cattle/bison;
> not a clinical/animal outcome, independent reproduction or causal estimate.
> **As of:** Baseline through cooperative-agreement year 2019–2020.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0041-C05`; APHIS PDF pp. 1, 3–4, Figure 1.
> **Basis / limits:** Metric and values are direct issuer reporting.

> **Claim record — CTL-0019-C03 | source-report**
> **Claim:** In 2020–2022 all reported national TPM averages/medians were about
> one hour or less, but exercises were scheduled with advance notice, reduced
> to eight traces per cooperator and could be prioritized as real incidents.
> **Claim status:** active
> **Scope:** Years seven/eight values and method change; not directly
> comparable causal proof or an unscheduled real-event recovery time.
> **As of:** Cooperative-agreement years 2020–2022.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0041-C05/C06`; APHIS PDF pp. 2–4, Table 1.
> **Basis / limits:** Both values and qualification are direct.

## Independent audit and failure limit

> **Claim record — CTL-0019-C04 | source-report**
> **Claim:** USDA OIG independently reviewed trace-investigation documentation
> for 11 sampled cattle-disease incidents and found one unsuccessful traceback
> associated with a known traceability risk.
> **Claim status:** active
> **Scope:** Three non-statistically selected States and represented diseases
> in FY2017–2020; not an event inventory or national failure rate.
> **As of:** OIG report 2022-11-28.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0041-C07`; OIG PDF pp. 3, 20–22.
> **Basis / limits:** The independent sample and negative result are direct.

> **Claim record — CTL-0019-C05 | analytic-judgment**
> **Claim:** `CTL-0019` conditionally mitigates the disease-spread response edge
> in `HAZ-0004` by supporting faster traceback/trace-forward work, and the
> portfolio supports a scoped implemented→tested→independently-evaluated
> assurance chain with positive exercise metrics and a real failure/gap result.
> **Claim status:** active
> **Scope:** Evidence-state classification for animal-disease traceability;
> not a cybersecurity safeguard, population effect size or null/causal trial.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `CTL-0019-C01`–`C04`; `SRC-0041-C05`–`C09`;
> [HAZ-0004](../hazards/haz-0004-agriculture-climate-pest-disease-and-supply-hazards.md).
> **Basis / limits:** APHIS supplies design/deployment/test; OIG supplies
> claim-appropriate independent assessment and limitations.

## Assurance interpretation

- Administrative closure of OIG recommendations is not a new performance test.
- Disease tracing can support containment; traceability does not prevent disease.
- Faster exercise completion is not automatically fewer infections or losses.
- OIG did not independently assess agency computer systems.
- Eleven sampled disease incidents are not eleven new `INC` pages.

> **Claim record — CTL-0019-C06 | analytic-judgment**
> **Claim:** `CTL-0019` supplies candidate evidence for `AGE-AE`, while
> `CTR-AE`, `THI-CI`, cyber-control effectiveness and global control gates
> remain below their separate multi-sector/count/evaluator floors.
> **Claim status:** superseded
> **Scope:** Frozen-rubric boundary before `SYN-0026`; no score transition.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `CTL-0019-C01`–`C05`; frozen criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** One AGE assurance instance cannot satisfy cross-sector
> effectiveness or incident-count contracts.
> **Superseded by:** `SYN-0026-C04/C05`, which accepts `AGE-AE` while retaining
> every cross-sector and incident non-promotion.

## Safety boundary

No live animal identifier, farm, disease case, record-query procedure, system
endpoint, credential, exploit or response procedure is exposed.

> **Claim record — CTL-0019-C07 | analytic-judgment**
> **Claim:** No live animal identifier, farm, disease case, record-query
> procedure, system endpoint, credential, exploit or response procedure is
> exposed.
> **Claim status:** stale
> **Scope:** Local page content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content; no external source is applicable to this
> editorial self-audit.
> **Limits:** Retained as a historical local-content audit, not as an
> externally evidenced decision claim. The current safety boundary is the
> prose above.

## Related pages

- [AST-0009](../assets/ast-0009-animal-plant-health-assets-stakeholders.md)
- [WFL-0012](../workflows/wfl-0012-animal-plant-health-surveillance-movement-response-lifecycle.md)
- [HAZ-0004](../hazards/haz-0004-agriculture-climate-pest-disease-and-supply-hazards.md)
- [SYN-0026](../syntheses/syn-0026-us-animal-disease-traceability-herd-assurance-reconciliation.md)
- [SYN-0001](../syntheses/syn-0001-coverage-rubric.md)

## Sources

- [SRC-0041](../sources/src-0041-us-animal-disease-traceability-herd-performance-audit.md)
