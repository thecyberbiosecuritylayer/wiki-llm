---
id: SYS-0008
type: system
title: Clinical laboratory information and reporting ecosystem
aliases:
  - clinical LIS reporting ecosystem
  - CPH laboratory information boundaries
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
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: SYS-0008-C01
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 36–48, 61–72, 193–207 and 214–219"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: SYS-0008-C02
    evidence:
      - source: SRC-0016
        locator: "Articles 3–30 and Annexes I–III, PDF pp. 34–46 and 92–95"
  - predicate: evidenced-by
    target: SRC-0017
    claim_id: SYS-0008-C02
    evidence:
      - source: SRC-0017
        locator: "§§II–V, printed pp. 2–27/PDF pp. 6–31"
  - predicate: depends-on
    target: AST-0006
    claim_id: SYS-0008-C03
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 61–72, 193–207"
      - source: SRC-0016
        locator: "Articles 3–16, PDF pp. 34–39"
  - predicate: enables
    target: WFL-0010
    claim_id: SYS-0008-C03
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 197–207"
      - source: SRC-0008
        locator: "NHSBT pp. 20 and 23"
tags:
  - clinical-laboratory
  - lis
  - lims
  - ehr
  - instruments
  - reporting
  - trust-boundary
---

# Clinical laboratory information and reporting ecosystem

## Functional system map

| System class | Function | Boundary/evidence limit |
| --- | --- | --- |
| collection/request endpoint | captures order, person/specimen identity and context | correct entry does not prove correct source or purpose |
| instrument/test system | transforms specimen/measurement into observation | connectivity does not prove calibration, QC or analytical validity |
| middleware/interface | moves instrument/worklist/result state | required class is inferred from current integrations; WHO does not model modern middleware |
| LIS/LIMS | accession, worklist, result, audit, report and archive functions | WHO supplies functions; no deployed configuration or current interface standard |
| EHR/HIE | care-facing clinical record/exchange | EHDS supplies staged current design, not completed EU deployment |
| reference laboratory | external sample/result service boundary | transport, identity, status and result reconciliation are required |
| public-health reporting/surveillance system | receives authorized laboratory information for public action | trigger, platform and authority vary by jurisdiction |
| backup/continuity service | protects/reconstructs data and service availability | prescribed backup/fallback is not a completed recovery test |
| identity/authorization/audit | binds user, role, action, release and communication | role/code is not proof of strong authentication or least privilege |

> **Claim record — SYS-0008-C01 | analytic-judgment**
> **Claim:** WHO directly supports instruments, paper/electronic registers,
> LIS/LIMS, referral laboratories, reporting users and backup/traceability
> functions in one testing ecosystem.
> **Claim status:** active
> **Scope:** Functional 2011 QMS classes, not current architecture or deployment.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C04`–`C07`, equipment pp. 36–48, sample/referral pp. 61–72,
> records/information pp. 193–207.
> **Basis / limits:** Classes and functions are direct. Paper and computer
> options are not evidence of one universal topology.

> **Claim record — SYS-0008-C02 | analytic-judgment**
> **Claim:** Independent EHDS and FDA lineages add current EHR exchange/logging,
> connected device-system, architecture and lifecycle-validation boundaries,
> but neither proves a laboratory-specific deployed end-to-end architecture.
> **Claim status:** active
> **Scope:** Current design overlays, not product/provider conformance.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C05/C08/C09`; [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C04`–`C08`; [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C05`.
> **Basis / limits:** Component/design requirements are direct; deployment and
> laboratory-specific boundary validation are absent.

> **Claim record — SYS-0008-C03 | analytic-judgment**
> **Claim:** Trustworthy operation requires identity and provenance to remain
> associated across instrument→interface→LIS→EHR/public-health/reporting and
> referral/continuity handoffs in [WFL-0010](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md).
> **Claim status:** active
> **Scope:** Required state relationship across [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md);
> no actual interface, credential or topology.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C06/C07/C09`; [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C03/C05`; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C05/C08`.
> **Basis / limits:** Identity, transmission, logging, availability and
> operational integration predicates are direct; the combined boundary is
> analytic and not validated.

> **Claim record — SYS-0008-C04 | artifact-observation**
> **Claim:** `CPH-SD` remains Partial because the corpus still lacks one
> criterion-level modern deployment/validation reconciliation for middleware,
> HIE, reference/public-health platforms, cloud and identity boundaries.
> **Claim status:** superseded
> **Scope:** Frozen-rubric corpus gap after SRC-0026; not evidence that real
> architectures or validations do not exist.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYS-0008-C01`–`C03`; frozen `CPH-SD` criterion in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Several classes are represented, but current class-level
> evidence and validated trust boundaries are incomplete; no proxy promotion is
> allowed.
> **Superseded by:** `SYS-0009-C05` after complete APHL integration and
> independent strict review on 2026-07-12.

## Safety boundary

No endpoint, interface, vendor, credential, network address, facility or patient
identifier is retained.

## Related pages

- [AST-0006 — assets/stakeholders](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md)
- [WFL-0010 — lifecycle](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md)
- [RSK-0013 — transfer paths](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md)
- [CTL-0012 — controls](../controls/ctl-0012-clinical-laboratory-quality-reporting-continuity-controls.md)
- [SYN-0013 — reconciliation](../syntheses/syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md)
- [SYS-0009 — complete modern successor map](sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md)
- [SYN-0014 — system-boundary reconciliation](../syntheses/syn-0014-clinical-public-health-system-boundary-reconciliation.md)
- [VUL-0006 — concrete context/configuration exposures](../vulnerabilities/vul-0006-laboratory-context-threshold-oversight-and-supply-exposures.md)
- [RSK-0021 — input-to-result decision path](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)

## Sources

- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
