---
id: CTL-0014
type: control
title: Allergy-record identification, clinical correction and safety controls
aliases:
  - wrong-allergy-state corrective controls
  - NatPSA allergy-record safeguards
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0029
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0029
    claim_id: CTL-0014-C01
    evidence:
      - source: SRC-0029
        locator: "PDF p. 1 Actions required 1–5 and p. 2 Notes A–E"
  - predicate: mitigates
    target: RSK-0015
    claim_id: CTL-0014-C01
    evidence:
      - source: SRC-0029
        locator: "PDF p. 1 Actions required 1–4 and p. 2 Notes A–E"
  - predicate: detects
    target: RSK-0015
    claim_id: CTL-0014-C02
    evidence:
      - source: SRC-0029
        locator: "PDF p. 1 Actions 1(a)–(c), 3 and 5; p. 2 Notes A–C"
  - predicate: recovers
    target: RSK-0015
    claim_id: CTL-0014-C02
    evidence:
      - source: SRC-0029
        locator: "PDF p. 1 Actions 1(b)–(c); p. 2 Notes A–C"
tags:
  - clinical-information
  - allergy-safety
  - record-identification
  - clinical-review
  - correction
  - training
  - interface-safety
  - assurance
  - required-not-verified
---

# Allergy-record identification, clinical correction and safety controls

## Exact-edge control and state map

| Risk edge | Defensive functions | Source modality/state | Evidence limit |
| --- | --- | --- | --- |
| candidate wrong state↔record set | authorized reporting to identify potentially affected records | required by future deadline | no query syntax, result count or completion |
| candidate record↔true clinical state | clinical review before amendment | required | no blind replacement; review outcome unknown |
| corrected source↔related systems | synchronized update across relevant records/settings | required | no propagation/completeness audit |
| user entry↔allergy label | guidance, training and additional input checks | required | no reach, competency or adherence result |
| interface presentation↔selection | supplier/user mitigations and safe upgrade deployment | required/prospective | no product, conformance or effectiveness result |
| admission/discharge↔record state | check and correct at care transitions | required | no sampled correctness outcome |
| intervention↔assurance | recurring allergy-status reports until assurance | strongly considered/recommended | no implemented programme, threshold or result |

> **Claim record — CTL-0014-C01 | analytic-judgment**
> **Claim:** The matrix maps identification, clinical verification,
> synchronized correction, transition checks, training/input checks, interface
> mitigation and recurring review to every edge in
> [RSK-0015](../risk-scenarios/rsk-0015-allergy-record-entry-propagation-medication-harm.md).
> **Claim status:** active
> **Scope:** Alert-derived defensive control map; not a universal baseline,
> recipient implementation or effectiveness claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md),
> `SRC-0029-C08`; PDF pp. 1–2 `Actions required` and Notes A–E.
> **Basis / limits:** Functions and modalities are direct; the exact-edge
> matrix is analytic and context-specific.

## Identification, verification and correction

> **Claim record — CTL-0014-C02 | source-report**
> **Claim:** The alert requires authorized identification of candidate records,
> clinical verification before correction and update of related digital
> records; this detects a suspect state while guarding against replacing a
> genuine allergy or intolerance with another inaccurate state.
> **Claim status:** active
> **Scope:** Control objective at safe abstraction; no query logic, patient
> record, automatic relabelling or completed review.
> **As of:** 2025-11-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C08`; PDF p. 1 Action 1(a)–(c) and p. 2 Notes A–C.
> **Basis / limits:** Identification, clinical review and correction sequence is
> direct. Clinical caveats make blind bulk substitution unsafe.

## Entry, transition and interface prevention

> **Claim record — CTL-0014-C03 | source-report**
> **Claim:** Guidance/training, admission/discharge correction and additional
> input checks aim to prevent or catch wrong allergy states at human entry and
> care-transition edges, but the alert provides no adoption, competency,
> adherence or correctness measure.
> **Claim status:** active
> **Scope:** Required process controls, not evaluated human-factor performance.
> **As of:** 2025-11-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C08`; PDF p. 1 Actions 2–3.
> **Basis / limits:** Required functions are direct. No recipient result is
> reported.

> **Claim record — CTL-0014-C04 | source-report**
> **Claim:** Supplier/user interface mitigations and safe deployment of
> upgrades address selection risk, but differing local configurations mean a
> data-source change would not eliminate the issue and no named control has a
> published effectiveness result in this package.
> **Claim status:** active
> **Scope:** Prospective system-control class and residual-risk boundary; no UI
> recipe, vendor defect or product recommendation.
> **As of:** 2025-11-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C04/C08`; PDF p. 1 Action 4 and p. 2 Notes D–E.
> **Basis / limits:** Mitigation/residual-risk language is direct. Supplier
> meetings and examples are not deployment, test or independent evaluation.

## Monitoring and evidence maturity

> **Claim record — CTL-0014-C05 | analytic-judgment**
> **Claim:** The 315-report search and clinical relevance review detect a
> pre-alert problem class, while recommended recurring reports could monitor
> response; neither measures whether post-alert controls reduce incorrect
> records, prescribing errors or patient harm.
> **Claim status:** active
> **Scope:** Detection versus effectiveness boundary.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C05/C07/C08/C09`; PDF p. 1 Action 5 and p. 2
> incident-data section.
> **Basis / limits:** Pre-alert signal detection and prospective monitoring are
> distinguishable; no post-alert baseline/comparator or outcome is present.

> **Claim record — CTL-0014-C06 | artifact-observation**
> **Claim:** Alert issuance and the national search/review are completed issuer
> actions, supplier discussions are ongoing, and recipient controls remain
> required/recommended through a future deadline; none is demonstrated
> implemented, tested, compliant, effective or independently evaluated.
> **Claim status:** active
> **Scope:** Evidence-state classification through 2026-07-12.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C08/C09`; PDF pp. 1–2; current alert-list snapshot.
> **Basis / limits:** Issuer versus recipient verbs and future deadline are
> direct. Listing is not compliance status; possible enforcement is not an
> enforcement event.

> **Claim record — CTL-0014-C07 | artifact-observation**
> **Claim:** This portfolio strengthens incident-derived control lessons but
> cannot pass `CPH-AE`, `CTR-AE` or a global control gate; no cell changes and
> the score remains 37/110 pending independent evaluation.
> **Claim status:** active
> **Scope:** Frozen-rubric control-evidence boundary.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `CTL-0014-C01`–`C06`; `SRC-0029-C11`; frozen criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Required design, pre-alert detection and a future deadline
> do not satisfy implementation/outcome/independence floors.

## Failure modes and safety boundary

Controls can fail through incomplete identification, incorrect clinical
reclassification, unsynchronized correction, weak training/adherence,
configuration variation, alert fatigue or misleading activity measures. The
page retains no record-query syntax, exact warning text, patient identity,
provider configuration or treatment procedure.

## Related pages

- [RSK-0015 — mitigated wrong-entry path](../risk-scenarios/rsk-0015-allergy-record-entry-propagation-medication-harm.md)
- [INC-0003 — national review](../incidents/inc-0003-national-allergy-recording-fatality-review-2021-2023.md)
- [SRC-0029 — alert/review evidence](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md)

## Source

- [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md)
