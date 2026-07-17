---
id: AST-0002
type: asset
title: Transfusion compatibility information and blood-product availability
aliases:
  - transfusion compatibility assets
  - compatibility testing information and blood stock
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
    claim_id: AST-0002-C01
    evidence:
      - source: SRC-0008
        locator: "pp. 21–23, 31, 97 and 124"
tags:
  - transfusion
  - compatibility-testing
  - blood-products
  - clinical-assets
  - supply-resilience
---

# Transfusion compatibility information and blood-product availability

> Coupled asset envelope for the information needed to select compatible blood
> and the constrained biological product inventory needed to fulfil that
> decision. Loss of either state can affect the same clinical workflow, but
> information and blood components remain distinct assets.

## Scope

The information side includes the bounded outputs and decision context of blood
grouping, antibody screening, crossmatching and specialist Red Cell
Immunohaematology assessment. The material side includes available blood
components and stock state, with O-negative units especially relevant to the
reported contingency. Patient records, detailed test methods and inventory
locations are outside this page.

> **Claim record — AST-0002-C01 | source-report**
> **Claim:** NHSBT's report links blood-grouping, antibody-screening and
> crossmatch information to selection of compatible blood products and reports
> that loss of access to those testing systems increased reliance on limited
> O-negative stock.
> **Claim status:** active
> **Scope:** NHSBT/Synnovis transfusion-service context in 2024–25; not a
> universal blood-service architecture or a patient-level finding.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–23, 97 and 124.
> **Basis / limits:** The information/product dependency and stock pressure are
> directly reported. Exact records, stock quantities, patient identities,
> local allocation rules and test-system architecture are not disclosed.

## Asset classes and states

| Asset class | Relevant trustworthy/available state | Evidence boundary |
| --- | --- | --- |
| Specimen and identity context | Correct specimen/person association sufficient for the ordered compatibility work | This source does not validate identity or custody controls |
| Grouping/screening/crossmatch information | Available, attributable and suitable for the compatibility decision | No test method, result or patient record is reproduced |
| Specialist interpretation/advice | Timely expert support for complex transfusion cases | Capacity and response-time metrics are absent |
| Blood component | Correct product selected and available for issue | No location, quantity or allocation procedure is published |
| O-negative stock state | Sufficient constrained inventory for cases relying on the reported fallback | “Universal” does not remove clinical judgement or supply tradeoffs |

The source also reports operational blood-group genotyping. That is related
clinical information but does not mean all compatibility decisions are genomic
or that [AST-0001](ast-0001-genomic-data.md) and this asset are
interchangeable.

> **Claim record — AST-0002-C02 | analytic-judgment**
> **Claim:** Compatibility information and available blood components form a
> coupled digital/material decision asset because information-system
> unavailability can change which constrained product class is consumed even
> without changing the product itself.
> **Claim status:** active
> **Scope:** Observed NHSBT-reported dependency during the June 2024 disruption;
> not a general rule that every laboratory outage changes stock use.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–22 and 97.
> **Basis / limits:** The report explicitly connects lost crossmatch access to
> greater O-negative use and stock pressure. The combined asset envelope is a
> wiki abstraction; it does not imply a network connection to inventory or a
> deterministic consequence in every setting.

## Stakeholders

- patients requiring compatible blood products;
- clinicians ordering or using blood components;
- hospital transfusion laboratories and pathology providers;
- NHSBT RCI, blood-supply and continuity teams;
- donors and the wider NHS supply network.

The current source does not enumerate affected patients or establish harm to a
specific person.

## Security, safety and quality properties

- **availability:** compatibility information and specialist testing capacity
  must be available in time for care;
- **integrity/authenticity:** results and their identity context must be suitable
  for the intended compatibility decision;
- **provenance:** the source, test/interpretation state and responsible service
  need traceable context;
- **material availability:** sufficient appropriate components must remain for
  current and downstream demand;
- **privacy:** information may be patient-linked, but this source does not
  describe a confidentiality event.

## Evidence and uncertainty

`SRC-0008` is primary for NHSBT's response and observed demand/stock effects,
but does not validate the attacked provider's systems or the full workflow.
Actor, vector, vulnerability, individual records, product-level outcome and
patient injury are unknown. A second independent lineage is still required for
generalization.

## Related pages

- [WFL-0006 — Transfusion compatibility testing and blood issue](../workflows/wfl-0006-transfusion-compatibility-and-blood-issue.md)
- [SYS-0004 — Transfusion laboratory information systems](../systems/sys-0004-transfusion-laboratory-information-systems.md)
- [INC-0001 — Synnovis transfusion-service disruption](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md)
- [RSK-0006 — Compatibility-testing disruption and supply pressure](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md)
- [CTL-0004 — Transfusion-service continuity response](../controls/ctl-0004-transfusion-service-continuity-response.md)
- [AST-0001 — Genomic data](ast-0001-genomic-data.md)

## Sources

- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 21–23,
  31, 97 and 124.
