---
id: WFL-0006
type: workflow
title: Transfusion compatibility testing and blood issue
aliases:
  - blood grouping and crossmatch workflow
  - transfusion compatibility-to-product workflow
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0008
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: WFL-0006-C01
    evidence:
      - source: SRC-0008
        locator: "pp. 10, 21–24, 97 and 124"
  - predicate: depends-on
    target: AST-0002
    claim_id: WFL-0006-C02
    evidence:
      - source: SRC-0008
        locator: "pp. 21–22 and 97"
  - predicate: depends-on
    target: SYS-0004
    claim_id: WFL-0006-C02
    evidence:
      - source: SRC-0008
        locator: "pp. 21–24, 92 and 97"
tags:
  - transfusion
  - laboratory-workflow
  - compatibility-testing
  - blood-issue
  - clinical-continuity
---

# Transfusion compatibility testing and blood issue

> Defensive functional workflow from specimen/test context through a
> compatibility decision to availability and clinical use of a blood product.
> It is a bounded synthesis of NHSBT's report, not a standard operating
> procedure, test method or complete hospital transfusion pathway.

## Scope

The source's organizational model separates donation, manufacturing, testing,
distribution/transport and clinical services. For the June 2024 disruption it
specifically identifies blood grouping, antibody screening and crossmatching as
the testing functions needed to support compatible product use, and Red Cell
Immunohaematology (RCI) as specialist capacity for complex cases.

> **Claim record — WFL-0006-C01 | source-report**
> **Claim:** NHSBT reports a coupled transfusion-service flow in which testing
> and specialist pathology support compatibility decisions between blood-
> component production/distribution and clinical use.
> **Claim status:** active
> **Scope:** NHSBT and affected London hospital services in 2024–25; not a
> complete or universal transfusion SOP.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 10, 21–24, 97 and 124.
> **Basis / limits:** Functional stages and service dependencies are direct.
> The report does not define a complete order/accession/identity event model,
> patient workflow, test procedure, issue authorization or product traceability
> schema.

## Functional lifecycle

| Stage | Defensive state needed | Current evidence boundary |
| --- | --- | --- |
| Request and specimen context | The required compatibility work is associated with the intended patient/case | Identity, collection and custody controls are not described |
| Grouping and antibody screening | Required information is available and suitable for the case | No method, result, accuracy or turnaround metric |
| Crossmatching/compatibility decision | Testing and interpretation support compatible product selection | No decision rule or procedure is reproduced |
| Specialist escalation | Complex cases can reach RCI testing/advice capacity | Capacity and escalation timing are not quantified |
| Product allocation and issue | A suitable component remains available for clinical use | Inventory and issue architecture are not described |
| Clinical use and continuity | Clinicians can use compatible products in emergency/surgical care | Source reports continuity, not patient-level outcomes |
| Supply feedback | Exceptional use can alter demand and stock alert state | The report links O-negative demand to an amber alert but gives no causal model for every alert |

The table is a safe wiki assembly of source-reported dependencies. It does not
claim that NHSBT publishes this exact sequence as a validated reference model.

## Systems and responsibility boundaries

[SYS-0004](../systems/sys-0004-transfusion-laboratory-information-systems.md) covers
the functional laboratory-system layer. Important boundaries are:

- external hospital/pathology laboratory service ↔ hospital clinicians;
- affected hospital testing capacity ↔ NHSBT specialist RCI support;
- compatibility decision ↔ available blood-component stock;
- NHSBT contingency support ↔ NHSBT's continuing national supply duties.

The report does not say NHSBT HAEMATOS was compromised. External hospital LIMS
and NHSBT's own laboratory information system remain separate system contexts.

> **Claim record — WFL-0006-C02 | analytic-judgment**
> **Claim:** The observed event supports a cross-organizational dependency from
> laboratory-system availability through compatibility testing and specialist
> escalation to blood-component demand and continuity of care.
> **Claim status:** active
> **Scope:** The June 2024 NHSBT-reported response, without a claim that every
> hospital uses the same architecture or fallback.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–22, 92 and 97.
> **Basis / limits:** Lost test-system access, RCI response, O-negative use and
> stock pressure are direct. The end-to-end boundary model is a bounded
> inference; provider topology, identity flow, exact capacity and patient
> outcomes are absent.

## Observed disruption and fallback

During the documented event, lost access to grouping/screening/crossmatch
systems created a compatibility-service gap. NHSBT reports RCI surge support
and greater use of O-negative products. The latter is a continuity option with
a material-supply tradeoff, not proof that testing or clinical judgement can be
discarded.

## Evidence and uncertainty

This is one first-party responder source. It supports the concrete handoffs and
an observed interruption but not a representative workflow, technical root
cause, full recovery timeline or absence of harm. An independent clinical/
provider source is needed before generalizing the workflow or effectiveness.

## Related pages

- [AST-0002 — Transfusion compatibility information and blood-product availability](../assets/ast-0002-transfusion-compatibility-and-blood-products.md)
- [SYS-0004 — Transfusion laboratory information systems](../systems/sys-0004-transfusion-laboratory-information-systems.md)
- [INC-0001 — Synnovis transfusion-service disruption](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md)
- [RSK-0006 — Compatibility-testing disruption and supply pressure](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md)
- [CTL-0004 — Transfusion-service continuity response](../controls/ctl-0004-transfusion-service-continuity-response.md)

## Sources

- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 10, 21–24,
  92, 97 and 124.
