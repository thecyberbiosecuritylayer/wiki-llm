---
id: INC-0003
type: incident
title: National allergy-recording incident review and reported fatality, 2021–2023
aliases:
  - NHS England 315-report allergy-record review
  - NatPSA allergy-record fatality signal
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-10-10
event_date: unknown
event_period_start: 2021-01-01
event_period_end: 2023-12-31
source_ids:
  - SRC-0029
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0029
    claim_id: INC-0003-C01
    evidence:
      - source: SRC-0029
        locator: "PDF pp. 1–2, Explanation, Actions required and Patient safety incident data; matching complete long-read sections"
  - predicate: affects
    target: AST-0006
    claim_id: INC-0003-C03
    evidence:
      - source: SRC-0029
        locator: "PDF p. 1 fatal summary and p. 2 fatal-incident paragraph; record/decision/patient classes"
tags:
  - aggregate-incident-review
  - clinical-information
  - allergy-safety
  - semantic-integrity
  - electronic-prescribing
  - biological-outcome
  - non-cyber
---

# National allergy-recording incident review and reported fatality, 2021–2023

> [!WARNING]
> **Evidence classification**
> This page represents one NHS England aggregate incident-review lineage and
> one anonymized fatal incident within it. It is not 315 independently supported
> incidents, patients or providers and is not an independently reconstructed
> case series.

## Review and publication timeline

| Date/period | Evidence state | Boundary |
| --- | --- | --- |
| 2021-01-01–2023-12-31 | occurrence window applied to searched reports | exact fatal-event date and report dates unknown |
| unknown | NHS England search and clinical relevance review | review date, deduplication and case-mapping method unreported |
| 2025-11-20 | alert issued/published/last updated | issue date is not an event date |
| 2026-07-12 | current NHS England list snapshot still includes the alert | listing is not implementation/compliance status |
| by 2026-11-20 | required-action completion deadline | future at snapshot; no completion inferred |

> **Claim record — INC-0003-C01 | analytic-judgment**
> **Claim:** The source supports a documented national non-adversarial,
> non-cyber allergy-record patient-safety signal and aggregate review, with one
> source-reported fatal biological outcome.
> **Claim status:** active
> **Scope:** Classification of one official review lineage and fatal incident;
> not 315 primary case files, cyber incidents or independently confirmed
> outcomes.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md),
> `SRC-0029-C02`–`C07`; PDF pp. 1–2.
> **Basis / limits:** The national review, error class and fatal incident are
> direct NHS England statements. No attacker, compromise, exploit, cyber outage
> or independent case investigation is supplied.

## Review units and outcome

> **Claim record — INC-0003-C02 | source-report**
> **Claim:** The review contains 315 clinically reviewed relevant reports—279
> from NRLS and 36 from LFPSE—covering incidents said to have occurred during
> 2021–2023.
> **Claim status:** active
> **Scope:** Report/repository units and occurrence-window filter; not unique
> incidents, patients, organizations or independent lineages.
> **As of:** 2023-12-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C05`; PDF p. 2, `Patient safety incident data`, first
> two paragraphs.
> **Basis / limits:** Count arithmetic is exact. Deduplication, denominator,
> completeness and report-to-case mapping are unavailable.

> **Claim record — INC-0003-C03 | source-report**
> **Claim:** NHS England reports one fatal event in which an inaccurate
> allergy state in a primary-care record was followed by incompatible
> prescribing, anaphylaxis and death, affecting the clinical-record, decision
> and patient classes in
> [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md).
> **Claim status:** active
> **Scope:** One anonymized issuer summary; not an exact event date, patient/
> facility identity, independently adjudicated cause or population rate.
> **As of:** 2023-12-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C06`; PDF p. 1 fatal summary and p. 2 fatal-incident
> paragraph.
> **Basis / limits:** Wrong record→prescription→anaphylaxis→death is direct.
> Software, entry route, exact chronology and root cause remain unknown.

> **Claim record — INC-0003-C04 | analytic-judgment**
> **Claim:** The reviewed issue spans entry/interface integrity, shared-record
> propagation, clinical review/correction and medication-decision boundaries,
> but the fatal incident directly establishes only the inaccurate-record and
> prescribing/outcome branch; laboratory-oriented maps are not substituted for
> a missing dedicated ePMA/EPR system model.
> **Claim status:** active
> **Scope:** Defensive boundary model, not a claim that record sharing or a
> particular interface caused the fatal incident.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C04/C06/C08`; PDF pp. 1–2.
> **Basis / limits:** General mechanisms/actions and the fatal branch are direct
> but are not case-level cross-tabulated; their reconciliation is analytic.

> **Claim record — INC-0003-C05 | source-report**
> **Claim:** After enumerating reports, NHS England describes all other
> relevant incidents with the combined `low or no harm` label; because no
> report-to-incident mapping is supplied, neither a remaining incident/report
> count nor a measured near-miss count can be derived.
> **Claim status:** active
> **Scope:** Aggregate severity boundary.
> **As of:** 2023-12-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C07`; PDF p. 1 final explanation sentence and p. 2
> fatal paragraph/issue bullets.
> **Basis / limits:** The source changes units and provides no low/no split or
> issue-category counts; low harm is not a near miss.

## Response state

> **Claim record — INC-0003-C06 | source-report**
> **Claim:** NHS England completed the national search/relevance review and
> alert issuance, while recipient working groups, record identification/
> clinical correction, training/checks, supplier mitigations and recurring
> assurance reporting were required, recommended, ongoing or prospective
> through the future deadline—not demonstrated complete or effective.
> **Claim status:** active
> **Scope:** Evidence state through 2026-07-12; not compliance, enforcement,
> resolved risk or post-alert outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C08/C09`; PDF pp. 1–2 `Actions required` and
> Notes; current alert-list snapshot.
> **Basis / limits:** Completed issuer actions and future recipient actions are
> grammatically distinct. The package contains no recipient result.

## Cross-event and rubric boundary

> **Claim record — INC-0003-C07 | artifact-observation**
> **Claim:** The national review strengthens but does not pass `CPH-CI`; the
> 315 reports are not multiplied into THI/CTR incident floors, actions do not
> pass `CPH-AE`, and all cells/gates remain unchanged at 37/110.
> **Claim status:** active
> **Scope:** Frozen-rubric boundary before separate HSSIB systems evaluation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `INC-0003-C01`–`C06`; `SRC-0029-C11`; frozen criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Independent national context is present, but the alert is
> not an independent systems evaluation or case-level confirmation; action
> design is not outcome effectiveness.

## Related pages

- [SYN-0022 — Foundational consequence/assurance calibration](../syntheses/syn-0022-foundational-consequence-assurance-calibration.md)

- [SRC-0029 — national alert/review](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md)
- [RSK-0015 — wrong-entry path](../risk-scenarios/rsk-0015-allergy-record-entry-propagation-medication-harm.md)
- [CTL-0014 — required controls](../controls/ctl-0014-allergy-record-identification-correction-safety-controls.md)

## Source

- [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md)
