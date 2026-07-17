---
id: AST-0006
type: asset
title: Clinical and public-health laboratory assets and stakeholders
aliases:
  - clinical laboratory asset map
  - CPH patient specimen result stakeholder map
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0008
  - SRC-0016
  - SRC-0017
  - SRC-0026
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: AST-0006-C01
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 7–15, 36–48, 61–72, 152–160 and 182–207"
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: AST-0006-C02
    evidence:
      - source: SRC-0005
        locator: "§§2.1–2.6 and 3.2, printed pp. 3–10/PDF pp. 12–19"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: AST-0006-C02
    evidence:
      - source: SRC-0016
        locator: "Articles 3–30 and Annexes I–II, PDF pp. 34–46 and 92–94"
  - predicate: evidenced-by
    target: SRC-0017
    claim_id: AST-0006-C03
    evidence:
      - source: SRC-0017
        locator: "§§II–V, printed pp. 2–25/PDF pp. 6–29"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: AST-0006-C03
    evidence:
      - source: SRC-0008
        locator: "pp. 9–10, 20–24 and 122–125"
tags:
  - clinical-laboratory
  - public-health
  - specimen
  - patient-identity
  - results
  - lis
  - ehr
  - stakeholders
---

# Clinical and public-health laboratory assets and stakeholders

## Scope and reconciliation

This page reconciles the older but complete WHO laboratory-QMS envelope with
independent current NIST genomics, EU EHDS health-data/EHR, FDA device-system
and NHSBT operational lineages. It contains class-level assets only—no patient,
specimen, system, facility, credential or public-health case record.

## Canonical matrix

| Frozen class | Reconciled assets/stakeholders | Evidence boundary |
| --- | --- | --- |
| specimen/patient identity | patient/person identity, request identifier, primary specimen/sample, aliquot/referral identity, collection/receipt/report timestamps | WHO LQMS pp. 61–72, 193–200; no actual identifier retained |
| orders/results | test request/order, clinical/epidemiological context, observation/result, interpretation, original/corrected report, notification/communication record | WHO pp. 64–68, 193–201; EHDS priority clinical-data categories |
| instruments and test system | diagnostic/analytical instrument, reagent/control, software-bearing device, maintenance/QC/validation state | WHO pp. 36–48, 74–100; FDA device-system scope |
| LIS/EHR/reporting data | register/worklist, LIS/LIMS, EHR laboratory/diagnostic result, interface/transmission, archive/backup/audit record | WHO pp. 197–207; EHDS Articles 3–30; NHSBT analyser→HAEMATOS example |
| clinicians and laboratory workforce | requester, clinician/provider, collector, laboratorian, director/quality manager, device/service supplier, reference lab | WHO pp. 152–160, 210–222; FDA lifecycle actors |
| patients and relatives | patient/data subject and care recipient; family/kin affected by support, consent or genomic relational privacy | WHO pp. 154–156; NIST `SRC-0005-C06` |
| populations/public | public-health officials/agencies, surveillance users, communities, demographic/population groups and public trust | WHO pp. 7–8, 154–156; NIST group/class privacy; EHDS public-health purposes |

> **Claim record — AST-0006-C01 | analytic-judgment**
> **Claim:** The reconciled matrix directly covers every frozen `CPH-AS`
> class: specimen/patient identity, orders/results, instruments, LIS/EHR/
> reporting data, clinicians, patients, relatives and populations.
> **Claim status:** active
> **Scope:** Class-level clinical/public-health asset envelope; not a deployed
> architecture, processing inventory or claim that every class exists in every
> laboratory.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C02/C04`–`C07`; [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C02/C04`–`C06`; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C03/C05/C09`; [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C04`–`C06`; [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C02/C05`.
> **Basis / limits:** WHO supplies the total-testing core; independent sources
> add literal genomics/kin, EHR, device and deployed analyser/LIS contexts.
> Coverage is categorical, not implementation prevalence.

> **Claim record — AST-0006-C02 | analytic-judgment**
> **Claim:** Patient/specimen identity and result provenance are distinct from
> genomic kin/group privacy: a correct laboratory association can still create
> relational privacy implications, while a privacy-preserving dataset can still
> carry an incorrect specimen/result association.
> **Claim status:** active
> **Scope:** Asset-state distinction for clinical/genomic workflows; not a
> finding about one dataset or patient.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C05`–`C08`, pp. 64–68 and 193–201;
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C03/C06`; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C05`–`C08`.
> **Basis / limits:** Identity/provenance and relational privacy predicates are
> direct but arise from different lineages; neither substitutes for the other.

> **Claim record — AST-0006-C03 | analytic-judgment**
> **Claim:** Instrument, LIS/EHR and human decision assets form separate trust
> boundaries: connectivity or an authorized role does not prove specimen
> identity, analytical validity, report integrity or correct clinical/public-
> health interpretation.
> **Claim status:** active
> **Scope:** Defensive dependency model; no actual topology, access decision,
> interface validation or diagnostic result.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C04/C07/C09`; [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C04`–`C08`; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C05/C08`; [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C05`.
> **Basis / limits:** Each source separates functional/design evidence from
> implementation or outcome. Boundaries are analytic, not deployment claims.

> **Claim record — AST-0006-C04 | artifact-observation**
> **Claim:** Independent strict review accepts this complete SF2 class map for
> `CPH-AS`; it does not promote `CPH-SD`, incident or effectiveness cells.
> **Claim status:** active
> **Scope:** Accepted frozen-rubric cell boundary after independent review.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `AST-0006-C01`–`C03`; frozen CPH criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Literal asset/stakeholder classes are complete; modern
> architecture validation, primary outcomes and evaluated safeguards remain
> separate evidence questions.

## Related pages

- [WFL-0010 — testing/reporting lifecycle](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md)
- [SYS-0008 — information/reporting ecosystem](../systems/sys-0008-clinical-laboratory-information-reporting-ecosystem.md)
- [SYS-0009 — integrated data-exchange architecture](../systems/sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md)
- [SYS-0010 — electronic patient-record safety dependencies](../systems/sys-0010-electronic-patient-record-safety-dependencies.md)
- [HAZ-0002 — identity/specimen/result failure](../hazards/haz-0002-patient-specimen-result-identity-quality-failure.md)
- [RSK-0013 — laboratory result/decision paths](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md)
- [INC-0003 — aggregate wrong-record review/fatal outcome](../incidents/inc-0003-national-allergy-recording-fatality-review-2021-2023.md)
- [RSK-0015 — incorrect allergy-state decision path](../risk-scenarios/rsk-0015-allergy-record-entry-propagation-medication-harm.md)
- [SYN-0013 — CPH reconciliation](../syntheses/syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md)
- [INC-0008 — observed laboratory result incident](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md)
- [RSK-0021 — biological-input to digital-decision path](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)

## Sources

- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
