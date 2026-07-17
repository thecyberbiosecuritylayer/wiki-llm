---
id: SYS-0006
type: system
title: Synthesis-provider and benchtop procurement-screening systems
aliases:
  - nucleic-acid provider screening system
  - benchtop synthesis screening ecosystem
status: active
created: 2026-07-12
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-10-10
source_ids:
  - SRC-0011
  - SRC-0012
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0011
    claim_id: SYS-0006-C01
    evidence:
      - source: SRC-0011
        locator: "§III, pp. 5–6; §IV Tables 1–2, pp. 6–7; §V, pp. 8–13"
  - predicate: depends-on
    target: AST-0004
    claim_id: SYS-0006-C02
    evidence:
      - source: SRC-0011
        locator: "§V, printed pp. 8–13"
  - predicate: governed-by
    target: GOV-0002
    claim_id: SYS-0006-C01
    evidence:
      - source: SRC-0011
        locator: "§§I–III, printed pp. 4–6"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: SYS-0006-C03
    evidence:
      - source: SRC-0012
        locator: "Definitions, provider/manufacturer and equipment sections, HTML lines 793–1050"
  - predicate: governed-by
    target: GOV-0003
    claim_id: SYS-0006-C03
    evidence:
      - source: SRC-0012
        locator: "Scope and responsible-practice guidance, HTML lines 708–839"
tags:
  - synthesis
  - provider
  - manufacturer
  - screening
  - human-review
  - benchtop-equipment
---

# Synthesis-provider and benchtop procurement-screening systems

> Functional system class for provider/manufacturer ordering, screening,
> review, decision, record and equipment-lifecycle responsibilities. It omits
> screening logic, sequence content, bypass mechanics and deployment topology.

## Scope and components

> **Claim record — SYS-0006-C01 | source-report**
> **Claim:** The OSTP framework covers traditional providers plus biofoundries,
> cloud labs, institutional core facilities and integrated research services,
> as well as manufacturers, intermediaries and benchtop equipment, and assigns
> them ordering, screening, review, record, security and lifecycle functions.
> **Claim status:** active
> **Scope:** Functional roles in the revised September 2024 framework; not
> deployed architecture or current adoption.
> **As of:** 2024-09-30.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §III, pp. 5–6; §IV Tables 1–2, pp. 6–7; §V, pp. 8–13.
> **Basis / limits:** Roles/functions are direct. The source supplies no product
> list, topology, interface protocol, configuration or system test.

| Function | System class | Boundary |
| --- | --- | --- |
| Intake | provider/manufacturer/intermediary order channel | identity, purpose and order provenance enter together |
| Screen | method/service and protected reference/database capability | exact contents and logic withheld |
| Review | accountable human legitimacy/decision function | decision authority and escalation must be explicit |
| Fulfill | provider product distribution or manufacturer equipment access | digital decision crosses into physical availability |
| Record/report | secure decision, interaction and incident records | privacy, IP, integrity and retention interests coexist |
| Lifecycle | legitimate user/access and later equipment transfer state | no anti-tamper or reagent-control mechanics consolidated |
| Govern/update | attestation, funding terms, standards and review process | attestation is not technical verification |

> **Claim record — SYS-0006-C02 | analytic-judgment**
> **Claim:** Candidate trust boundaries include customer↔ordering interface,
> order↔screening function, automated result↔human review, decision↔physical
> fulfillment and equipment owner↔later user/transfer, all dependent on the
> assets in `AST-0004`.
> **Claim status:** active
> **Scope:** Defensive functional mapping for `WFL-0008`; no boundary is
> claimed validated.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §V, printed pp. 8–13.
> **Basis / limits:** The source assigns the functions; the boundary map is wiki
> analysis. No implementation, failure rate, security assessment or independent
> validation is supplied.

> **Claim record — SYS-0006-C03 | source-report**
> **Claim:** UK guidance independently assigns provider, manufacturer,
> third-party vendor, principal-user and end-user roles to order intake,
> screening/update capability, human follow-up, decision/reporting, records,
> equipment authentication/logging and transfer accountability.
> **Claim status:** active
> **Scope:** Functional UK guidance model, not a deployed system or tested
> equipment architecture.
> **As of:** 2024-10-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> definitions and provider/manufacturer/equipment sections, HTML lines
> 793–1050.
> **Basis / limits:** Roles/functions are direct. The page reports no interface
> protocol, deployment topology, identity assurance test, screening benchmark
> or independent evaluation.

> **Claim record — SYS-0006-C04 | analytic-judgment**
> **Claim:** US and UK sources independently support provider-interface,
> screening-dependency, human-review, identity/update, instrument and record
> boundaries, but neither supplies design-tool integration or validated
> deployment architecture.
> **Claim status:** active
> **Scope:** Reconciled safe system map for procurement screening.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§III–V, pp. 5–13; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> HTML lines 793–1050.
> **Basis / limits:** Independent sources converge on the functional system
> classes. This page alone did not establish trust-boundary validation, design
> environments or implementation; SYN-0023 later supplied the wider
> reconciliation needed for the already-passed SEB-SD cell.

## Evidence and uncertainty

The original frameworks permit heterogeneous implementations and contain no
provider/manufacturer deployment, benchmark, independent audit or equipment
evaluation. SRC-0059 and CTL-0024 later add one bounded benchmark/configuration
dependency, while SRC-0061 adds a historical operational-data context; neither
validates a provider-wide architecture, current equipment deployment or
independent safeguard effectiveness.

## Related pages

- [SYN-0023 — Engineering-biology reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [AST-0004](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md)
- [WFL-0008](../workflows/wfl-0008-nucleic-acid-procurement-screening-lifecycle.md)
- [RSK-0008](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [CTL-0006](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [GOV-0002](../governance/gov-0002-us-federally-funded-nucleic-acid-screening-2024.md)
- [GOV-0003](../governance/gov-0003-uk-synthetic-nucleic-acid-screening-2024.md)
- [SYN-0002](../syntheses/syn-0002-us-uk-nucleic-acid-screening-comparison.md)
- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md)
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [WFL-0014 — Design-to-disposition lifecycle](../workflows/wfl-0014-engineering-biology-design-to-disposition-lifecycle.md)
- [VUL-0007 — Screening/integration exposure classes](../vulnerabilities/vul-0007-synthesis-screening-definition-database-integration-and-supply-exposures.md)
- [CTL-0024 — Benchmark assurance](../controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md)
- [SYN-0032 — Engineering-biology reconciliation](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)

## Sources

- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md), §§III–V,
  printed pp. 5–13.
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
  HTML lines 793–1050.
