---
id: SYS-0004
type: system
title: Transfusion laboratory information and result-transfer systems
aliases:
  - transfusion laboratory information systems
  - blood compatibility laboratory systems
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0008
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: SYS-0004-C01
    evidence:
      - source: SRC-0008
        locator: "pp. 21–24, 92, 97 and 124"
  - predicate: depends-on
    target: AST-0002
    claim_id: SYS-0004-C03
    evidence:
      - source: SRC-0008
        locator: "pp. 21–23 and 97"
tags:
  - transfusion
  - pathology
  - laboratory-information-system
  - result-transfer
  - clinical-systems
---

# Transfusion laboratory information and result-transfer systems

> Defensive functional system class for technology and service capacity that
> produces, transfers, stores or supports transfusion compatibility
> information. It is not a network diagram and does not imply that NHSBT's
> HAEMATOS system was affected by the Synnovis attack.

## Scope

The source contains three distinct contexts that must not be collapsed:

1. external Synnovis/hospital laboratory systems whose access was disrupted;
2. NHSBT's own HAEMATOS laboratory information system and analyser-result
   automation programme;
3. NHSBT RCI specialist testing/advice capacity used as a contingency.

> **Claim record — SYS-0004-C01 | source-report**
> **Claim:** NHSBT reports that external laboratory-system access supported
> grouping, antibody screening and crossmatching, while its own pathology
> environment separately includes HAEMATOS, analysers and RCI specialist
> services.
> **Claim status:** active
> **Scope:** Functional service/system classes in the NHSBT 2024–25 report, not
> a claim of shared topology or compromise.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–24, 92, 97 and 124.
> **Basis / limits:** Named functions and NHSBT systems/services are direct.
> The source does not identify the attacked LIMS product, protocol, hosts,
> provider architecture or a connection to HAEMATOS.

## Functional components and maturity

| Component/service class | Source-supported role | Status and boundary |
| --- | --- | --- |
| External pathology/laboratory systems | Support grouping, antibody screening and crossmatching for affected hospitals | Access disrupted; product, owner topology and root cause not disclosed |
| NHSBT HAEMATOS LIS | Receives pathology results in NHSBT's own environment | Named separately; not reported compromised |
| Analysers and Automated Results Transfer | Move selected analyser results into HAEMATOS without manual re-entry | Initial two-process rollout reported; six additional processes progressing, not all confirmed live |
| RCI laboratory/service | Provides specialist testing and advice for complex transfusion cases | Operational service; capacity/latency metrics absent |
| RCI Assist | Supports remote interpretation of results | Eight-hospital pilot called successful; full rollout planned for 2025–26, not yet live in the report |
| Fetal RhD electronic request/report | Supports digital ordering/reporting at participating hospitals | 36 hospitals reported live; not complete national coverage |

Planned systems such as OrganPath, a fully digitized apheresis pathway, bespoke
AI products and the new core blood-management system are not classified as
implemented here.

## Implemented result transfer

> **Claim record — SYS-0004-C02 | source-report**
> **Claim:** NHSBT reports partially deployed analyser-to-HAEMATOS automatic
> result transfer: an initial rollout covered two testing processes and work on
> automating six more progressed during 2024–25.
> **Claim status:** active
> **Scope:** NHSBT Automated Results Transfer programme, not all laboratory
> results or a security/effectiveness evaluation.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 20 and 23.
> **Basis / limits:** Deployment and expansion wording are direct. Claimed
> transcription-risk reduction has no before/after metric, interface test,
> validation coverage, security assessment or independent evaluation.

## Dependencies and trust boundaries

- analyser ↔ result-transfer capability ↔ NHSBT LIS;
- laboratory system ↔ grouping/screening/crossmatch workflow;
- hospital/provider ↔ NHSBT RCI contingency service;
- compatibility result/interpretation ↔ product-selection decision;
- digital-service continuity ↔ blood-component inventory pressure.

These are functional boundaries only. No address, protocol, privilege,
exposure, remote-access path or named weakness is asserted.

> **Claim record — SYS-0004-C03 | analytic-judgment**
> **Claim:** `SRC-0008` supports a reusable functional system map and one
> implemented result-transfer example, but not a representative architecture,
> compromise of NHSBT, validated boundary or product vulnerability.
> **Claim status:** active
> **Scope:** Evidence sufficiency after the NHSBT annual-report transaction.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–24, 47–48, 92, 95 and 97.
> **Basis / limits:** The source separates systems and reports an implemented
> integration. Critical-ICT risk and a limited disaster-recovery finding show
> why deployment is not assurance; the affected critical system is unnamed and
> its weakness is intentionally not inferred.

## Security, safety and recovery considerations

- availability of compatibility functions is time-sensitive, but an outage is
  not itself proof of patient harm;
- automated transfer can remove manual steps while adding interface,
  validation and recovery dependencies;
- continuity can shift burden to specialist laboratories and constrained blood
  stock;
- restoration of IT service is not enough unless result integrity, identity
  context and decision fitness are trustworthy;
- external-provider and NHSBT responsibilities must remain explicit.

## Evidence and uncertainty

Evidence is one organization report. It is primary for NHSBT systems and
response, secondary for the attacked provider, and does not contain technical
incident records or independent system evaluation. Current deployment and
remediation state must be rechecked after the reporting period.

## Related pages

- [AST-0002 — Transfusion compatibility information and blood-product availability](../assets/ast-0002-transfusion-compatibility-and-blood-products.md)
- [WFL-0006 — Transfusion compatibility testing and blood issue](../workflows/wfl-0006-transfusion-compatibility-and-blood-issue.md)
- [INC-0001 — Synnovis transfusion-service disruption](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md)
- [RSK-0006 — Compatibility-testing disruption and supply pressure](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md)
- [CTL-0004 — Transfusion-service continuity response](../controls/ctl-0004-transfusion-service-continuity-response.md)

## Sources

- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 20–24,
  47–48, 92, 95, 97 and 124.
