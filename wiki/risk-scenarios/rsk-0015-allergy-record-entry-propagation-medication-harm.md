---
id: RSK-0015
type: risk-scenario
title: Incorrect allergy-record entry and propagation affecting medication decisions
aliases:
  - look-alike allergy-state medication harm
  - incorrect allergy label propagation path
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0029
sensitivity: public
dual_use: low
origin_domain: mixed
destination_domains:
  - digital
  - clinical
  - biological
relations:
  - predicate: evidenced-by
    target: SRC-0029
    claim_id: RSK-0015-C01
    evidence:
      - source: SRC-0029
        locator: "PDF p. 1 Explanation and p. 2 fatal-incident paragraph"
  - predicate: affects
    target: AST-0006
    claim_id: RSK-0015-C01
    evidence:
      - source: SRC-0029
        locator: "PDF p. 1 fatal summary and p. 2 fatal-incident paragraph"
tags:
  - clinical-information
  - semantic-integrity
  - allergy-safety
  - record-sharing
  - medication-decision
  - observed-outcome
  - non-adversarial
---

# Incorrect allergy-record entry and propagation affecting medication decisions

> [!WARNING]
> **Evidence classification**
> The fatal branch is source-reported and observed. The candidate interface-
> entry mechanisms and record-sharing propagation are issue-class mechanisms;
> they are not proven root causes or measured propagation in that fatal event.

## Observed and conditional paths

Observed fatal branch:

`known allergy → inaccurate primary-care allergy state → incompatible
prescription → anaphylaxis → death`.

General issue-class branch:

`look-alike label/interface presentation → possible wrong allergy selection →
potential propagation through record sharing → downstream medication decision
uses incorrect state → conditional patient harm`.

> **Claim record — RSK-0015-C01 | analytic-judgment**
> **Claim:** NHS England's fatal incident summary supports the complete inaccurate-record
> →prescription→anaphylaxis→death branch affecting the record, decision and
> patient classes in
> [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md).
> **Claim status:** active
> **Scope:** One anonymized source-reported event; not a likelihood, case date,
> independent adjudication or universal outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md),
> `SRC-0029-C06`; PDF p. 1 fatal summary and p. 2 fatal-incident paragraph.
> **Basis / limits:** The four states are direct in NHS England's summary. The
> arrow notation is analytic and does not add a case mechanism.

> **Claim record — RSK-0015-C02 | source-report**
> **Claim:** Similar-label/interface presentations and differing local
> configurations are candidate wrong-entry mechanisms for the issue class, but
> the alert does not establish which interface or entry process produced the
> fatal record error.
> **Claim status:** active
> **Scope:** General mechanism class, not named-product defect or fatal-case
> root cause.
> **As of:** 2025-11-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C04/C06`; PDF p. 1 `Explanation`.
> **Basis / limits:** Candidate mechanisms and `not specific to one system` are
> direct. UI steps and configuration details are withheld.

> **Claim record — RSK-0015-C03 | source-report**
> **Claim:** Record sharing can potentially spread an incorrect allergy state
> across settings, but the alert gives no propagation count, rate, topology or
> evidence that sharing occurred in the fatal incident or every reviewed report.
> **Claim status:** active
> **Scope:** Conditional digital→digital transfer branch.
> **As of:** 2025-11-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C04`; PDF p. 1 record-sharing statement; p. 2 Note B.
> **Basis / limits:** Potential propagation is literal; occurrence and scale
> are unmeasured.

> **Claim record — RSK-0015-C04 | analytic-judgment**
> **Claim:** The scenario spans entry/interface, shared-record, clinical-
> verification/correction and prescribing/administration boundaries; no single
> edge or actor is sufficient for all branches, and laboratory-oriented pages
> are not substituted for a dedicated ePMA/EPR system/workflow model.
> **Claim status:** active
> **Scope:** Defensive dependency model, not a facility architecture or patient
> record.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C04/C06/C08`; PDF pp. 1–2.
> **Basis / limits:** Source mechanisms/actions locate each boundary; the
> normalized cross-edge model is analytic.

> **Claim record — RSK-0015-C05 | analytic-judgment**
> **Claim:** [CTL-0014](../controls/ctl-0014-allergy-record-identification-correction-safety-controls.md)
> maps identification, clinical verification, synchronized correction,
> training/input checks, interface mitigation and recurring review to the exact
> edges, while retaining every action as required/recommended rather than
> implemented or effective.
> **Claim status:** active
> **Scope:** Defensive control mapping, not a deployment result.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C08/C09`; PDF pp. 1–2 `Actions required` and Notes.
> **Basis / limits:** Functions and modalities are direct; no recipient result
> or outcome evaluation exists.

> **Claim record — RSK-0015-C06 | artifact-observation**
> **Claim:** This second allergy-information outcome mechanism strengthens the
> evidence portfolio but no cell passes before independent HSSIB evaluation
> and reconciliation; score and all global gates remain 37/110 and unchanged.
> **Claim status:** active
> **Scope:** Frozen-rubric boundary.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `RSK-0015-C01`–`C05`; `SRC-0029-C11`; frozen rubric in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Separate national context is present, but not independent
> systems evaluation or control effectiveness.

## Safety boundary

Only system roles, abstract states, transitions and defensive control classes
are retained. The page omits UI/search steps, query syntax, exact warning text,
patient/facility identity, treatment detail and provider configuration.

## Related pages

- [INC-0003 — aggregate review and fatal incident](../incidents/inc-0003-national-allergy-recording-fatality-review-2021-2023.md)
- [SRC-0029 — official review/alert](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md)
- [CTL-0014 — exact-edge required controls](../controls/ctl-0014-allergy-record-identification-correction-safety-controls.md)

## Source

- [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md)
