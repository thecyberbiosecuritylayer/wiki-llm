---
id: SYN-0014
type: synthesis
title: Clinical and public-health system-boundary reconciliation
aliases:
  - CPH-SD criterion reconciliation
  - instrument LIS EHR HIE public-health architecture synthesis
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0008
  - SRC-0016
  - SRC-0017
  - SRC-0026
  - SRC-0027
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0027
    claim_id: SYN-0014-C01
    evidence:
      - source: SRC-0027
        locator: "SRC-0027-C02: LIS guide pp. 1 and 4; AIMS toolkit pp. 6 and 54; Uganda title/date/byline/opening; current APHL catalogue entries"
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: SYN-0014-C01
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 11–15, 36–48, 61–72 and 193–207"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: SYN-0014-C01
    evidence:
      - source: SRC-0016
        locator: "Articles 3–30 and Annexes I–III, PDF pp. 34–46 and 92–95"
  - predicate: evidenced-by
    target: SRC-0017
    claim_id: SYN-0014-C01
    evidence:
      - source: SRC-0017
        locator: "§§II–VI and VII.A–C, printed pp. 2–35/PDF pp. 6–39; Appendices 1 and 4, printed pp. 38–53/PDF pp. 42–57"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: SYN-0014-C03
    evidence:
      - source: SRC-0008
        locator: "NHSBT pp. 20–24, bounded implemented result-transfer and continuity context"
  - predicate: depends-on
    target: SYS-0009
    claim_id: SYN-0014-C02
    evidence:
      - source: SRC-0027
        locator: "class/flow/boundary evidence in LIS guide pp. 5–38 and AIMS toolkit pp. 2–53"
      - source: SRC-0026
        locator: "WHO laboratory workflow/referral/information functions pp. 11–15, 36–72 and 193–207"
  - predicate: supersedes
    target: SYS-0008
    claim_id: SYN-0014-C04
    evidence:
      - source: SRC-0027
        locator: "SRC-0027-C03–C10; LIS guide pp. 5–32 and 36–38; AIMS toolkit pp. 2–28 and 44–53; Uganda named sections"
tags:
  - clinical-public-health
  - system-architecture
  - interoperability
  - trust-boundary
  - validation
  - evidence-reconciliation
  - coverage
---

# Clinical and public-health system-boundary reconciliation

## Lineages and predicate allocation

| Lineage | Direct contribution | Explicit non-contribution |
| --- | --- | --- |
| APHL 2024–2026 | complete modern laboratory/exchange class map, AIMS operation, message/interface tests and one bounded rollout | regulator status, independent conformance or effectiveness |
| WHO LQMS | independent testing, instrument, referral, LIS/LIMS, reporting and QMS state | modern HIE/cloud/IAM architecture |
| EU EHDS | current EHR/interoperability/logging/identity and Union/national infrastructure responsibilities | completed laboratory deployment or APHL compliance |
| U.S. FDA | current connected device-system architecture, lifecycle validation/test evidence and boundary assumptions | LIS/HIE/public-health platform deployment |
| NIST genomics | independent sequencing/instrument→storage/pipeline→EHR ecosystem and dependency limits | clinical/public-health architecture validation |
| NHSBT | bounded implemented result-transfer and observed continuity context | complete architecture or independent effectiveness |

> **Claim record — SYN-0014-C01 | analytic-judgment**
> **Claim:** The synthesis counts APHL/Ruvos/CDC-funded package components once
> and assigns independent WHO, EHDS, FDA, NIST and NHS evidence only to their
> direct predicates; no source is treated as reproducing another regime,
> deployment or technology stack.
> **Claim status:** active
> **Scope:** SF2 lineage/predicate reconciliation for `CPH-SD`, not a compliance
> crosswalk or generalization from one jurisdiction to another.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0027](../sources/src-0027-aphl-integrated-laboratory-information-public-health-exchange.md),
> `SRC-0027-C02`–`C11`; [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C04/C06/C07/C11`; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C05/C08/C09`; [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C04`–`C08`; [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C04/C05`; [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C05`.
> **Basis / limits:** Issuers, genres, dates and dependencies are materially
> distinct. Shared public-health subject matter does not create duplication,
> and APHL partner/funder names do not create extra lineages.

## Frozen-criterion matrix

| `CPH-SD` literal | Located direct evidence | Reconciled boundary |
| --- | --- | --- |
| instruments | APHL LIS pp. 14, 20, 22–26, 36–38; WHO equipment/QMS | instrument support is not analytical validity |
| middleware/LIS | APHL LIS pp. 5–21, 24–26, 36–38; AIMS pp. 21–23, 27, 43, 53 | engine/broker/gateway classes, no exposed configuration |
| EHR/HIE | APHL LIS pp. 6–10, 17–24; AIMS pp. 2–3, 7–18, 53; EHDS | care/HIE/public-health roles remain jurisdiction-specific |
| reference labs | APHL LIS pp. 19 and 22–23; Uganda `From point A to point B`; WHO referral | information flow, not specimen-routing detail |
| public-health systems | APHL LIS pp. 6–10, 19, 28–35; AIMS ELR/eCR/ETOR pp. 7–18; EHDS | platform and reporting authority are not universal |
| cloud/identity | APHL LIS pp. 12, 17–21 and 26; AIMS pp. 13–14, 19–23, 50–53; EHDS/FDA | cloud is optional; IAM classes do not expose credentials |
| validated boundaries | APHL LIS pp. 10, 17, 19–21, 32–38; AIMS pp. 9–10, 13, 20–25, 44–49; Uganda phased validation | definition/test/validation/production/monitoring states are separate from effectiveness |

> **Claim record — SYN-0014-C02 | analytic-judgment**
> **Claim:** `SYS-0009-C01`–`C03` and the matrix satisfy every literal system,
> dependency and trust-boundary limb of `CPH-SD` at SF2 with exact locators,
> including modern middleware/HIE/public-health/cloud/IAM and validation-aware
> boundaries that were missing after `SRC-0026`.
> **Claim status:** active
> **Scope:** Clinical/public-health architecture criterion, not every product,
> provider, country, facility or possible interface.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYS-0009](../systems/sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md),
> `SYS-0009-C01`–`C03`; `SRC-0027-C03`–`C10`; direct independent claims
> allocated in `SYN-0014-C01`; frozen `CPH-SD` criterion in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** All named classes and the test/validation boundary are
> literal. The cross-source canonical map is analytic and bounded to the
> criterion; APHL alone is not counted as SF2.

## Validation and assurance boundary

> **Claim record — SYN-0014-C03 | analytic-judgment**
> **Claim:** `validated boundaries` is satisfied by direct evidence of defined
> message/interface contracts, repeated integration testing, sender/inline
> validation, staged environments, production monitoring and phased validated
> rollout; it does not mean that a third party certified the entire end-to-end
> architecture or proved a safeguard effective.
> **Claim status:** active
> **Scope:** Interpretation of the frozen `CPH-SD` architecture predicate,
> preserving the stricter and still-unmet `CPH-AE`/global-control predicates.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0027-C04/C09/C10`; `SYS-0009-C04`;
> [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C06/C08`; [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C05`; frozen `CPH-SD/AE` and global-control criteria in `SYN-0001`.
> **Basis / limits:** Completed APHL issuer-reported boundary checks and
> operation are more than architecture recommendation. Missing independent
> results, denominators and patient/outcome evaluation prevent AE promotion.

> **Claim record — SYN-0014-C04 | artifact-observation**
> **Claim:** Independent strict review accepts exactly `CPH-SD` as
> Partial→Pass, raising CPH from 7/10 to 8/10 and the overall score from
> 36/110 to 37/110 (33.6%), with 37 Pass, 67 Partial and 6 Absent.
> **Claim status:** active
> **Scope:** Accepted checkpoint arithmetic under frozen rubric v1.0; narrow
> supersession of `SYS-0008-C04`, not absolute domain completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SYN-0014-C01`–`C03`; prior `SYN-0001-C20` at 36 Pass/
> 68 Partial/6 Absent; frozen score method in `SYN-0001`.
> **Basis / limits:** One literal transition produces the arithmetic;
> independent artifact, locator, lineage, graph and binary-cell review
> completed 2026-07-12.

> **Claim record — SYN-0014-C05 | artifact-observation**
> **Claim:** `CPH-CI/AE` remain Partial, the other seven CPH cells remain Pass
> and every adjacent cell/global gate remains unchanged: this architecture
> package is not a new incident/outcome or independent effectiveness study.
> **Claim status:** active
> **Scope:** Adjacent-cell and global-gate residual audit at the accepted
> SRC-0027 checkpoint.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0027-C02/C07`–`C12`; `SYS-0009-C04/C05`; frozen CPH and
> twelve global-gate criteria in `SYN-0001`.
> **Basis / limits:** Architecture completeness, implementation, patient
> consequence and independently evaluated effectiveness are separate evidence
> predicates; score proximity does not change a global gate.

## Safety boundary

The synthesis exposes only classes, flow roles, trust-boundary states and
evidence maturity. It contains no live topology, facility map, endpoint,
credential, message schema, routing logic, patient/specimen data or protocol
implementation recipe.

## Related pages

- [SRC-0027 — APHL package](../sources/src-0027-aphl-integrated-laboratory-information-public-health-exchange.md)
- [SYS-0009 — integrated system map](../systems/sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md)
- [SYS-0008 — earlier bounded map](../systems/sys-0008-clinical-laboratory-information-reporting-ecosystem.md)
- [SYN-0013 — CPH lifecycle reconciliation](syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md)
- [SYN-0001 — frozen rubric](syn-0001-coverage-rubric.md)

## Sources

- [SRC-0027](../sources/src-0027-aphl-integrated-laboratory-information-public-health-exchange.md)
- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
