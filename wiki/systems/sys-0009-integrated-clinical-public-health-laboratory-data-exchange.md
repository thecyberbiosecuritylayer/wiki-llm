---
id: SYS-0009
type: system
title: Integrated clinical and public-health laboratory data-exchange architecture
aliases:
  - instrument-LIS-EHR-HIE-public-health system map
  - validated CPH laboratory data boundaries
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
    claim_id: SYS-0009-C01
    evidence:
      - source: SRC-0027
        locator: "LIS guide pp. 5–32 and 36–38; AIMS toolkit pp. 2–28 and 53; Uganda `From point A to point B`, `Data in near real time` and `Looking ahead` sections"
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: SYS-0009-C03
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 11–15, 36–48, 61–72 and 193–207"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: SYS-0009-C03
    evidence:
      - source: SRC-0016
        locator: "Articles 3–30 and Annexes I–III, PDF pp. 34–46 and 92–95"
  - predicate: evidenced-by
    target: SRC-0017
    claim_id: SYS-0009-C03
    evidence:
      - source: SRC-0017
        locator: "§§II–VI and VII.A–C, printed pp. 2–35/PDF pp. 6–39; Appendices 1 and 4, printed pp. 38–53/PDF pp. 42–57"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: SYS-0009-C04
    evidence:
      - source: SRC-0008
        locator: "NHSBT pp. 20–24, especially implemented ART and incident-continuity context"
  - predicate: depends-on
    target: AST-0006
    claim_id: SYS-0009-C02
    evidence:
      - source: SRC-0027
        locator: "LIS guide pp. 5–10, 17–23 and 28–32; AIMS toolkit pp. 2–3 and 7–28"
  - predicate: enables
    target: WFL-0010
    claim_id: SYS-0009-C02
    evidence:
      - source: SRC-0027
        locator: "LIS guide pp. 5–10, 20–32; AIMS toolkit pp. 15–18"
  - predicate: supersedes
    target: SYS-0008
    claim_id: SYS-0009-C05
    evidence:
      - source: SRC-0027
        locator: "SRC-0027-C03–C10; LIS guide pp. 5–32 and 36–38; AIMS toolkit pp. 2–28 and 44–53; Uganda named sections"
tags:
  - clinical-laboratory
  - public-health
  - instrument
  - middleware
  - LIS
  - EHR
  - HIE
  - reference-laboratory
  - cloud
  - identity
  - validation
  - trust-boundary
---

# Integrated clinical and public-health laboratory data-exchange architecture

## Canonical class map

| Required class | Defensive function | Validation-aware boundary |
| --- | --- | --- |
| instruments/analyzers/POCT | produce or receive test/worklist/result state | device↔interface direction, result/test mapping and transfer monitoring |
| middleware/integration engine | parse, transform, route and orchestrate messages | declared sender/receiver, format, expected response and monitored interface |
| LIS/LIMS | accession, worklist, identity, result, approval, archive and report | identity/provenance, role, interface and release state remain associated |
| EHR/HIS/HMIS | submit orders/context and receive approved results for care | system/user authorization, semantic/syntactic mapping and correction path |
| HIE/exchange | bridge otherwise distinct provider/health-system records | verified partner, permitted routing and audit/monitoring boundary |
| referral/reference laboratory | receive referred specimen/order context and return results | originating/testing LIS and status/result reconciliation |
| public-health platform | receive authorized ELR/eCR/ETOR/surveillance information for action | jurisdiction, recipient, message validation and reporting authority remain explicit |
| cloud/hybrid/on-prem infrastructure | host, transport, store, recover and scale services | data residency, gateway, identity, availability and recovery assumptions |
| IAM/audit/operations | bind user/partner role to allowed data/action and support continuity | IAM/RBAC/SSO/federation, logs, health checks and support states |

> **Claim record — SYS-0009-C01 | analytic-judgment**
> **Claim:** APHL's integrated package directly supplies every literal
> `CPH-SD` class—instruments, middleware/LIS, EHR/HIE, reference laboratories,
> public-health systems, cloud and identity—plus explicit interface/message
> definition, test, validation, monitoring and production-state boundaries.
> **Claim status:** active
> **Scope:** Criterion-level functional architecture across APHL guidance,
> operating-platform description and issuer-reported implementation; not a
> universal or facility-specific topology.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0027](../sources/src-0027-aphl-integrated-laboratory-information-public-health-exchange.md),
> `SRC-0027-C03`–`C10`; LIS guide pp. 5–32 and 36–38; AIMS toolkit
> pp. 2–28, 44–53; Uganda `From point A to point B`, `Data in near real
> time` and `Looking ahead` sections.
> **Basis / limits:** Every class and boundary state is direct, but all APHL
> artifacts remain one lineage and require independent reconciliation for SF2.

## Trust-boundary flows

1. `instrument/POCT ↔ middleware/engine ↔ LIS`
2. `LIS ↔ EHR/HIS/HMIS ↔ authorized care decision`
3. `originating LIS ↔ referral/reference-laboratory LIS`
4. `laboratory/EHR/HIE ↔ public-health exchange/platform ↔ authorized action`
5. `partner identity ↔ gateway ↔ cloud/hybrid/on-prem service`
6. `defined interface → test/validation → staged production → monitoring/change`

> **Claim record — SYS-0009-C02 | analytic-judgment**
> **Claim:** The six flows bind the assets in
> [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md)
> to the testing/reporting/correction stages in
> [WFL-0010](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md)
> without treating transfer, validation or availability as proof of result
> correctness or authorized downstream action.
> **Claim status:** active
> **Scope:** Defensive dependency/trust-boundary abstraction; no live endpoint,
> credential, patient/specimen record or deployable route.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYS-0009-C01`; [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C04`–`C09`; `AST-0006-C01`–`C03`; `WFL-0010-C01`–`C04`.
> **Basis / limits:** APHL supplies modern exchange classes; WHO independently
> supplies the testing/referral/reporting state that the architecture serves.

> **Claim record — SYS-0009-C03 | analytic-judgment**
> **Claim:** Independent WHO, EHDS and FDA lineages corroborate different
> boundary predicates: laboratory workflow/referral/information state, current
> EHR/interoperability/identity-log responsibilities and device-system lifecycle
> architecture/testing respectively; none is misrepresented as reproducing the
> full APHL stack.
> **Claim status:** active
> **Scope:** SF2 predicate reconciliation, not cross-jurisdiction compliance or
> an assertion that the independent instruments describe one deployment.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C04/C06/C07/C11`; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> `SRC-0016-C05/C08/C09`; [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C04`–`C08`; [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C04/C05`.
> **Basis / limits:** The sources are materially independent and current where
> claimed. They contribute only their direct functional/normative predicates.

## Evidence-state boundary

| State | Direct evidence | Not inferred |
| --- | --- | --- |
| architecture/guidance | 2024 LIS guide and reusable AIMS model | universal adoption or validated implementation |
| operating platform | APHL describes AIMS production use, partners and environments | independent traffic/compliance audit |
| boundary tests | message self-test/inline validation, staged environments, CI/CD and health checks | clinical correctness or conformance of every sender |
| bounded implementation | Uganda phased test/validation/rollout; NHSBT result-transfer implementation | common protocol, independent acceptance or patient outcome |
| assurance | audit/readiness/control documentation classes | published audit result or independent effectiveness |

> **Claim record — SYS-0009-C04 | analytic-judgment**
> **Claim:** The evidence portfolio distinguishes recommended architecture,
> issuer-described operation, boundary testing, bounded implementation and
> independently evaluated effectiveness; only the first four have evidence,
> and none is promoted to the fifth.
> **Claim status:** active
> **Scope:** Evidence maturity for the system map, not a judgement that an
> unobserved evaluation does not exist.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0027-C02/C04/C07`–`C10`; [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C05`; [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> `SRC-0017-C06/C08`.
> **Basis / limits:** Source modalities and state verbs are direct. No
> architecture diagram, `validation`, traffic count or audit-design reference
> is treated as an independent outcome by itself.

> **Claim record — SYS-0009-C05 | artifact-observation**
> **Claim:** Independent strict review accepts that this map resolves the exact
> missing predicates in `SYS-0008-C04` and supports `CPH-SD` Partial→Pass; it
> does not promote `CPH-CI`, `CPH-AE` or a global gate.
> **Claim status:** active
> **Scope:** Accepted frozen-rubric cell boundary and narrow supersession of an
> earlier corpus-gap claim, not supersession of `SYS-0008`'s valid classes.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYS-0009-C01`–`C04`; `SYS-0008-C01`–`C04`; frozen
> `CPH-SD/CI/AE` criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** The architecture criterion is complete at SF2; primary
> patient outcome and independently evaluated safeguard evidence are different
> predicates and remain absent.

## Safety boundary

Only component classes, state transitions, trust-boundary questions and
defensive validation functions are retained. The page omits APHL's geographic
exchange maps, vendor deployment layout, facility identifiers, endpoints,
credentials, routing logic, message fields, protocol recipes and operational
thresholds.

## Related pages

- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)

- [SRC-0027 — APHL package](../sources/src-0027-aphl-integrated-laboratory-information-public-health-exchange.md)
- [SYS-0008 — prior bounded system map](sys-0008-clinical-laboratory-information-reporting-ecosystem.md)
- [AST-0006 — assets/stakeholders](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md)
- [WFL-0010 — lifecycle](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md)
- [SYN-0014 — criterion reconciliation](../syntheses/syn-0014-clinical-public-health-system-boundary-reconciliation.md)

## Sources

- [SRC-0027](../sources/src-0027-aphl-integrated-laboratory-information-public-health-exchange.md)
- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
