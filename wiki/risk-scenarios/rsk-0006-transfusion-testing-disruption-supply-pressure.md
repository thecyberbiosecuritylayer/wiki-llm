---
id: RSK-0006
type: risk-scenario
title: Transfusion compatibility-system disruption and blood-supply pressure
aliases:
  - compatibility testing outage to O-negative stock pressure
  - laboratory availability to transfusion continuity risk
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0008
  - SRC-0009
sensitivity: public
dual_use: low
origin_domain: digital
destination_domains:
  - digital
  - physical
  - biological
relations:
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: RSK-0006-C01
    evidence:
      - source: SRC-0008
        locator: "pp. 21–22, 92 and 97"
  - predicate: evidenced-by
    target: SRC-0009
    claim_id: RSK-0006-C03
    evidence:
      - source: SRC-0009
        locator: "article update paragraphs 2–3; HTML lines 190–191"
  - predicate: affects
    target: AST-0002
    claim_id: RSK-0006-C01
    evidence:
      - source: SRC-0008
        locator: "pp. 21–22 and 97"
  - predicate: depends-on
    target: WFL-0006
    claim_id: RSK-0006-C02
    evidence:
      - source: SRC-0008
        locator: "pp. 10, 21–22, 92, 97 and 124"
  - predicate: depends-on
    target: SYS-0004
    claim_id: RSK-0006-C02
    evidence:
      - source: SRC-0008
        locator: "pp. 21–24, 92 and 97"
tags:
  - transfusion
  - laboratory-availability
  - blood-supply
  - clinical-continuity
  - observed-path
---

# Transfusion compatibility-system disruption and blood-supply pressure

> [!WARNING]
> **Evidence classification**
> This path was **observed and source-reported** by an operationally involved
> responder in one 2024 event. NHS England separately supports the ransomware
> event, broad test-capacity reduction and appointment delays, but not the
> compatibility→O-negative→amber-alert transitions. This is not a generic
> likelihood estimate, forensic reconstruction or proof of patient injury.

## Scenario

Loss of access to laboratory systems interrupts grouping, antibody-screening
and crossmatch capacity. Affected hospitals require alternative compatibility
support and rely more heavily on O-negative components. The digital service
gap therefore changes a physical/biological inventory demand state, increases
load on specialist responders and can create wider supply and continuity risk.

During the documented Synnovis event, NHSBT reports this chain through RCI
surge support, sustained O-negative demand and an amber stock alert. The page
does not reproduce attack mechanics, patient data, inventory locations or
clinical procedures.

## Assets and workflow

- [AST-0002](../assets/ast-0002-transfusion-compatibility-and-blood-products.md) —
  compatibility information and blood-component availability;
- [WFL-0006](../workflows/wfl-0006-transfusion-compatibility-and-blood-issue.md) —
  the compatibility-testing/product-use dependency;
- [SYS-0004](../systems/sys-0004-transfusion-laboratory-information-systems.md) —
  external laboratory systems and separate NHSBT support systems/services;
- patients, clinicians, hospital laboratories, NHSBT RCI/supply teams and
  donors — affected stakeholders.

## Preconditions and trust boundaries

For the generalized path to apply:

1. clinical use depends on timely grouping/screening/crossmatch information;
2. ordinary local capacity is inaccessible or insufficient;
3. an external/specialist service or product fallback absorbs demand;
4. the fallback draws on constrained staff, testing or blood-component
   capacity;
5. response and coordination do not fully prevent pressure from propagating.

Only the 2024 event is observed. These conditions are not claimed for every
hospital or jurisdiction.

## Origin-domain state

The observed origin state is **loss of access** to critical laboratory systems
at an external pathology provider. NHS England calls the 2024-06-03 event a
ransomware cyberattack and reports significantly reduced test-processing
capacity; NHSBT reports the compatibility-system access loss. Neither supplies
the actor identity, ransomware family, initial-access vector, vulnerability or
evidence that NHSBT itself was compromised.

> **Claim record — RSK-0006-C01 | source-report**
> **Claim:** NHSBT reports an observed chain from a cyber-caused loss of access
> to grouping/screening/crossmatch systems through greater reliance on
> O-negative products to stock pressure and an amber alert.
> **Claim status:** active
> **Scope:** NHSBT-observed consequences of the June 2024 Synnovis event; not a
> complete forensic or patient-outcome account.
> **As of:** 2024-06.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–22 and 97; contingency context p. 92.
> **Basis / limits:** Each stated transition is direct in NHSBT's account.
> Pages 22 and 97 duplicate one narrative and do not create corroboration;
> p. 92 does not name Synnovis. Exact demand, duration, capacity, root cause and
> patient outcomes are not reported.

> **Claim record — RSK-0006-C03 | source-report**
> **Claim:** NHS England separately reports that the 3 June 2024 ransomware
> attack significantly reduced Synnovis test-processing capacity, delayed more
> than 11,000 outpatient/elective appointments and was followed by source-
> reported full service restoration by December 2024.
> **Claim status:** active
> **Scope:** Broader provider availability and care-delay context; not direct
> evidence for the compatibility-to-O-negative-to-amber-alert transitions.
> **As of:** 2024-12-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> article update paragraphs 2–3, HTML lines 190–191.
> **Basis / limits:** Event class, capacity reduction, aggregate delay and
> restoration month are explicit. The source does not identify the blood-
> compatibility systems or report O-negative demand, stock state, patient
> injury, technical acceptance criteria or independent recovery validation.

## Cross-domain transfer

The transfer mechanism is an **availability-dependent decision and material-
demand shift**:

`digital laboratory access loss → compatibility-service gap → alternative
testing/product decision → increased use of constrained biological inventory →
supply/continuity pressure`.

> **Claim record — RSK-0006-C02 | analytic-judgment**
> **Claim:** The event is a complete cyber-to-material/clinical consequence path
> because digital availability changed compatibility-service capacity and the
> pattern of blood-product demand, even though no blood component was digitally
> altered.
> **Claim status:** active
> **Scope:** Bounded cross-domain interpretation of the NHSBT-reported event.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 10, 21–22, 92, 97 and 124.
> **Basis / limits:** Source evidence establishes the system, workflow, demand
> and stock transitions. The cross-domain label is a wiki inference; it does
> not establish general likelihood, a biological change to blood or a
> deterministic safety outcome.

## Receiving-domain state

The immediate receiving state is reduced compatibility-testing capacity and a
shift toward O-negative use. The next state is pressure on limited blood stock
and responder capacity. An amber alert is an operational supply state, not
itself a patient injury.

## Immediate and downstream consequences

Confirmed/source-reported for the event:

- disruption of compatibility-system access;
- RCI surge activity and extended hours;
- greater O-negative reliance and sustained demand;
- contribution to an amber stock alert;
- source-reported continuity support for emergency/surgical transfusion.

Potential but **not confirmed by this source**:

- delayed or unavailable transfusion for a specific patient;
- incompatible product use or clinical injury;
- exhaustion of O-negative stock;
- compromise or corruption of NHSBT systems/results.

## Evidence

Evidence consists of two official institutional disclosures. The NHSBT annual
report is primary for its response and stock/service observations and secondary
for the affected Synnovis environment. NHS England is primary for its public
chronology, broad capacity/delay and recovery statement, but does not document
the blood-specific chain. The two issuers improve event-level corroboration;
they do not independently corroborate every scenario edge or provide technical/
clinical outcome evaluation.

## Controls by function

[CTL-0004](../controls/ctl-0004-transfusion-service-continuity-response.md) maps to
the service-gap and downstream supply-pressure edges through RCI surge,
extended hours, urgent-case prioritization and coordinated stock management.
It was implemented in the event and NHSBT reports continuity, but independent
effectiveness remains absent.

## Assumptions and uncertainty

- Event occurrence: supported by two official institutional accounts, high
  confidence; not independent forensic corroboration.
- General recurrence likelihood: not evaluated.
- Ransomware classification: source-reported by NHS England; family, actor,
  vector, exploited weakness and affected system product unknown.
- NHSBT compromise: not reported.
- Patient harm: not established; only serious risk is reported.
- Control capacity, response latency and counterfactual: not reported.
- Pages 22/97 are an internal duplicate, not independent evidence.

## Related scenarios

- [RSK-0001 — HCL containment-control disruption](rsk-0001-hcl-containment-control-disruption.md) is hypothetical and concerns containment/safety functions; this scenario is observed and concerns clinical compatibility/supply continuity.
- [RSK-0003 — Genomic-data integrity and decision harm](rsk-0003-genomic-data-integrity-decision-harm.md) concerns integrity; this scenario originates in availability loss.

## Related pages

- [INC-0001 — Synnovis transfusion-service disruption](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md)
- [AST-0002 — Transfusion compatibility information and blood-product availability](../assets/ast-0002-transfusion-compatibility-and-blood-products.md)
- [WFL-0006 — Transfusion compatibility testing and blood issue](../workflows/wfl-0006-transfusion-compatibility-and-blood-issue.md)
- [SYS-0004 — Transfusion laboratory information systems](../systems/sys-0004-transfusion-laboratory-information-systems.md)
- [CTL-0004 — Transfusion-service continuity response](../controls/ctl-0004-transfusion-service-continuity-response.md)
- [SRC-0008 — NHSBT Annual Report 2024–25](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0009 — NHS England Synnovis update](../sources/src-0009-nhs-england-synnovis-update-2025.md)

## Sources

- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 10,
  21–24, 92, 97 and 124.
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md), article
  update paragraphs 2–3, HTML lines 190–191.
