---
id: WFL-0010
type: workflow
title: Clinical laboratory testing, reporting and correction lifecycle
aliases:
  - total testing process and reporting loop
  - CPH order to correction lifecycle
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0008
  - SRC-0009
  - SRC-0016
  - SRC-0026
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: WFL-0010-C01
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 11–15, 61–72, 89–124, 162–168 and 193–207"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: WFL-0010-C03
    evidence:
      - source: SRC-0016
        locator: "Articles 3–46, including Article 23 at PDF pp. 42–43; Annexes I–III, pp. 92–95"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: WFL-0010-C04
    evidence:
      - source: SRC-0008
        locator: "pp. 20–24, 92 and 97"
  - predicate: depends-on
    target: AST-0006
    claim_id: WFL-0010-C02
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 61–72, 152–160 and 193–207"
      - source: SRC-0016
        locator: "Articles 3–16 and Annex I, PDF pp. 34–39 and 92–93"
tags:
  - clinical-laboratory
  - public-health
  - total-testing-process
  - reporting
  - correction
  - retention
  - notification
---

# Clinical laboratory testing, reporting and correction lifecycle

## Scope

The workflow combines WHO's total testing process with independent current
health-data/EHR design and observed NHS laboratory-continuity context. It is a
functional lifecycle, not a diagnostic procedure or deployed dataflow.

## Canonical lifecycle

| Stage | Material/clinical state | Information/decision state | Control/exception boundary |
| --- | --- | --- | --- |
| order/request | requested examination and relevant patient/public-health need | requester, purpose, priority and clinical/epidemiological context | incomplete/nonurgent request may require clarification |
| collection | intended patient/source and suitable specimen | identity, time, collector and request association | mismatch/quality checks; no collection procedure retained |
| receipt/accession | received specimen/aliquots | register/LIS identifier and custody state | accept, conditionally process, reject/recollect or refer |
| examination/test | instrument/method/reagent/QC state produces observation | worklist, result and provenance record | failed QC prevents release; deviations recorded |
| interpret/authorize | result assessed against method/context | interpretation, authorizer, original/corrected status | human/authorized release remains distinct from automation |
| report/transmit | verified report leaves laboratory | destination, time, channel and receipt/notification record | right result→right recipient; urgent communication tracked |
| notify/action | clinician/public-health user receives information | care, surveillance, investigation or resource decision | report availability does not guarantee correct action |
| retain/reanalyse/correct | specimen/record retained or lawfully disposed | archive, comparison/retest, amended/corrected result and occurrence record | old result preserved; affected users informed; recurrence monitored |

> **Claim record — WFL-0010-C01 | analytic-judgment**
> **Claim:** The canonical lifecycle covers every frozen `CPH-WL` stage from
> order through collection, accession, test, interpretation, report,
> notification/action and retention/reanalysis/correction.
> **Claim status:** active
> **Scope:** Normalized clinical/public-health laboratory lifecycle; not a
> claim that WHO 2011 contains one literal modern digital diagram for all rows.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C04/C06/C09`, pp. 11–15, 61–72, 89–124, 162–168 and
> 193–207; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C05/C08`; [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C04/C05`.
> **Basis / limits:** WHO supplies the phase and sample/report/correction
> sequence; EHDS/NIST independently add current digital-data/lifecycle context.
> Reanalysis is a controlled recheck/retest/comparison state, not permission to
> reinterpret every result indefinitely.

> **Claim record — WFL-0010-C02 | analytic-judgment**
> **Claim:** Material, identity/permission, result and decision lanes must remain
> synchronized, because a valid analytical value can still be linked to the
> wrong person/specimen/purpose or delivered to the wrong user.
> **Claim status:** active
> **Scope:** Trust-boundary model across [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md);
> no actual mismatch, unauthorized use or patient record.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C05`–`C09`, especially pp. 64–68, 163–166 and 193–201;
> [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md), `SRC-0016-C05`–`C08`.
> **Basis / limits:** Separate identity, quality, authorization and reporting
> predicates are direct. Synchronization is an analytic control objective.

> **Claim record — WFL-0010-C03 | analytic-judgment**
> **Claim:** The public-health branch uses laboratory information for
> surveillance, disease detection/prevention and outbreak response, but the
> reporting platform, jurisdictional trigger and action authority are context-
> specific rather than universal steps.
> **Claim status:** active
> **Scope:** Functional reporting/action branch; not current mandatory disease-
> reporting law or evidence that a report reached a named authority.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C02/C04/C05`, pp. 7–8 and 152–156;
> [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md), `SRC-0016-C03/C05/C09`.
> **Basis / limits:** Public-health purposes/users and current EU infrastructure
> design are direct but not equivalent or globally generalized.

> **Claim record — WFL-0010-C04 | analytic-judgment**
> **Claim:** An availability failure can interrupt the lifecycle before report/
> action, as observed in the Synnovis service disruption, while restoration or
> fallback does not by itself prove every result, appointment or patient outcome
> was recovered.
> **Claim status:** active
> **Scope:** Availability/continuity overlay; not a general causal estimate.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C03/C04`; [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> `SRC-0009-C03/C04`; WHO reporting/backup dependencies in `SRC-0026-C07/C09`.
> **Basis / limits:** The incident establishes service interruption and bounded
> response; it supplies no patient injury or independently validated recovery.

> **Claim record — WFL-0010-C05 | artifact-observation**
> **Claim:** Independent strict review accepts the complete SF2 lifecycle for
> `CPH-WL` without promoting `CPH-SD`, `CPH-CI` or `CPH-AE`.
> **Claim status:** active
> **Scope:** Accepted frozen-rubric cell boundary after independent review.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `WFL-0010-C01`–`C04`; frozen CPH criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Lifecycle stages are complete; architecture validation,
> primary biological outcome and independent effectiveness remain absent.

## Related pages

- [AST-0006 — assets/stakeholders](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md)
- [SYS-0008 — information ecosystem](../systems/sys-0008-clinical-laboratory-information-reporting-ecosystem.md)
- [SYS-0009 — integrated data-exchange architecture](../systems/sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md)
- [HAZ-0002 — laboratory quality hazard](../hazards/haz-0002-patient-specimen-result-identity-quality-failure.md)
- [RSK-0013 — transfer paths](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md)
- [CTL-0012 — exact-edge controls](../controls/ctl-0012-clinical-laboratory-quality-reporting-continuity-controls.md)
- [SYN-0013 — CPH reconciliation](../syntheses/syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md)
- [INC-0008 — observed result-misreporting incident](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md)
- [RSK-0021 — observed reverse-transfer path](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)

## Sources

- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
