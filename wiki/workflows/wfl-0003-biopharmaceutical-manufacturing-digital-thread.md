---
id: WFL-0003
type: workflow
title: Biopharmaceutical manufacturing information and control flows
aliases:
  - biopharmaceutical manufacturing digital thread
  - advanced biomanufacturing information flow
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0001
  - SRC-0003
  - SRC-0031
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0003
    claim_id: WFL-0003-C01
    evidence:
      - source: SRC-0003
        locator: "§ Digital Information Flow in Biomanufacturing; Figure 1 and caption"
  - predicate: depends-on
    target: SYS-0002
    claim_id: WFL-0003-C01
    evidence:
      - source: SRC-0003
        locator: "§ Digital Information Flow in Biomanufacturing; Figure 1 and caption"
  - predicate: evidenced-by
    target: SRC-0031
    claim_id: WFL-0003-C05
    evidence:
      - source: SRC-0031
        locator: "Part I §§1–4, printed pp. 1–14 (physical pp. 6–19); Annex III §§1–3, printed pp. 27–30 (physical pp. 32–35); Annex V §§1–3.3, printed pp. 37–41 (physical pp. 42–46)"
tags:
  - biomanufacturing
  - digital-thread
  - advanced-manufacturing
  - cyber-physical
---

# Biopharmaceutical manufacturing information and control flows

> Reconciled material/data/control/quality lineage for biopharmaceutical
> manufacturing. Guttieres et al. supply traditional-biologics/ATMP and
> fill/finish/distribution envelopes; ICH Q13 adds a continuous-manufacturing
> branch for therapeutic proteins and validation-aware quality, release, and
> disposition gates.
> “Digital thread” remains a wiki normalization, not a source term, deployment,
> or validated enterprise architecture.

## Scope

The primary source is a 2019 Perspective on biopharmaceutical manufacturing. It
uses a typical monoclonal-antibody process as an illustration and compares
centralized traditional, centralized ATMP, and decentralized ATMP models. This
page does not generalize that model to all food, industrial, agricultural, or
laboratory production systems.

ICH Q13 adds a normative continuous-manufacturing branch for chemical entities
and therapeutic proteins. Its Annex III is limited to therapeutic-protein drug
substance; Annex IV is a small-molecule integrated drug-substance/product
example. These examples are illustrative and are not merged into one claimed
commercial protein-product architecture.

[WFL-0001](wfl-0001-biomanufacturing-system.md) describes the system
scope of a single facility based on Murch et al.; `WFL-0003` adds explicit flow
categories and cross-site variants. Both models remain conceptual and do not
constitute independent facility validation.

## Within-facility manufacturing flow

Figure 1 presents this material sequence:

`raw materials → upstream cell culture → downstream purification → fill & finish → finished product`.

Below the production stages, the diagram shows process-control layers:
field-level measurement/action, equipment controllers, distributed
coordination, and supervisory data collection/monitoring/control. The wiki
retains only the functional layers; product-specific parameters, protocols, and
exposure details are excluded
([SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
§ Digital Information Flow in Biomanufacturing; Figure 1).

> **Claim record — WFL-0003-C01 | source-report**
> **Claim:** Figure 1 of Guttieres et al. links the material flow of traditional
> biopharmaceutical manufacturing to hierarchical information/control flow
> through measurement/action, equipment-control, distributed-control, and
> supervisory layers.
> **Claim status:** active
> **Scope:** Conceptual typical monoclonal-antibody manufacturing model.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> § Digital Information Flow in Biomanufacturing; Figure 1 and caption.
> **Basis / limits:** Labels and arrows were verified in the local raster. The
> diagram does not establish network zones, identity, authorization, exact
> protocols, or complete quality-system integration.

## Cross-site manufacturing network

Figure 2 distinguishes three models:

1. **Centralized traditional biologics:** raw materials enter one manufacturer;
   products move through a supply/provider network while product information is
   tracked; the control center remains within the facility.
2. **Centralized ATMP:** providers/hospitals and the manufacturer exchange
   patient-specific material and information; production is centralized.
3. **Decentralized ATMP:** multiple manufacturing sites interact with a control
   center that may be co-located or standalone.

> **Claim record — WFL-0003-C02 | source-report**
> **Claim:** Figure 2 distinguishes material/product flow, information exchange,
> and control-center relationships for centralized traditional, centralized
> ATMP, and decentralized ATMP manufacturing.
> **Claim status:** active
> **Scope:** High-level source comparison, not a production-network
> architecture.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> § Considerations for Emerging Biologic Products, second and third paragraphs;
> Figure 2 and caption.
> **Basis / limits:** The flow types and three models are shown directly. Patient
> identity, consent, chain of identity/custody, cross-border status, and release
> authority are not modeled.

## Flow classes and decision dependencies

| Flow | Source-supported content | Not established |
| --- | --- | --- |
| Material | Raw/cell-bank inputs, intermediates/patient-specific inputs, finished/diverted material and criteria-based disposition | Complete identity/custody, storage and logistics execution |
| Data | Collection, PAT/testing, model/quality/release records, monitoring and process/product/patient exchange | Enterprise provenance, identity resolution, retention and access policy |
| Control | Feedback and commands between process equipment and control layers; cross-site supervision in distributed model | Protocols, privileges, segmentation, fail-safe design |
| Decision | Criteria support adjust/pause/divert/collect/investigate/test/release and lifecycle-change decisions | Named authority, deployed exception workflow and measured decision correctness |

> **Claim record — WFL-0003-C03 | analytic-judgment**
> **Claim:** `SRC-0001` and `SRC-0003` together support a biomanufacturing
> system scope that extends beyond IT and includes candidate material, data, and
> control flows, but not a validated digital-thread reference architecture.
> **Claim status:** active
> **Scope:** Cross-source reconciliation of one test-bed systems view and one
> general Perspective model.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> § Adding another dimension; Figure 1;
> [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md), Figures 1–2;
> §§ Digital Information Flow in Biomanufacturing, Considerations for Emerging
> Biologic Products.
> **Basis / limits:** The sources converge on coupled process, information, and
> facility scope, but they use different conceptual units, and neither validates
> a complete architecture. Guttieres cites Murch for the field framing, so the
> corroboration is not fully independent.

## Reconciled development-to-distribution lineage

| Required stage | Direct source support | Preserved boundary |
| --- | --- | --- |
| Development | cell-line/process development and process-design/IP context; Q13 control-strategy, model and process development | no named programme, technology-transfer dossier or product |
| Raw supply | raw/input materials, supplier/batch variability, cell-bank vials and traceability | no supplier-qualification outcome or complete custody chain |
| Upstream | cell culture generally and Annex III perfusion culture/harvest branch | Q13 branch is therapeutic-protein drug substance, not all biologics/ATMP |
| Downstream | purification plus capture chromatography, virus inactivation, polishing, virus filtration and concentration classes | functional sequence only; no operating recipe or deployment |
| Fill/finish | Guttieres Figure 1 links downstream to fill/finish and finished product | Q13 Annex III does not independently supply sterile protein fill/finish |
| Quality/release | monitoring/PAT, reference/offline tests, specifications, validation/continuous verification, PQS diversion/disposition/CAPA and release evidence | design/evidence expectations, not a released batch or approval result |
| Distribution | Guttieres Figure 2 links finished product/information to provider/warehouse/supply network | high-level network, not storage conditions, logistics controls or actual delivery |

The continuous quality-decision loop is:

`material/process/equipment state → sensor/PAT/test/model data → compare with
criteria → adjust, continue, pause or divert → investigate/test/disposition →
release or reject → lifecycle learning/change`.

> **Claim record — WFL-0003-C05 | analytic-judgment**
> **Claim:** Guttieres and Q13 jointly cover the literal biomanufacturing
> lineage from development and raw supply through upstream, downstream,
> fill/finish, quality/release and distribution, with source-specific gaps
> visible at every stage.
> **Claim status:** active
> **Scope:** Represented traditional-biologics/ATMP and Q13 continuous-
> therapeutic-protein contexts; not an industrial variant, universal SOP,
> named implementation or complete storage/recall/retirement architecture.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> §§New Risks Within the Growing Bioeconomy, Digital Information Flow in
> Biomanufacturing and Considerations for Emerging Biologic Products;
> Figures 1–2; [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§1–4, printed pp. 1–14 (physical pp. 6–19); Annex III §§1–3,
> printed pp. 27–30 (physical pp. 32–35).
> **Basis / limits:** Every frozen stage is direct in the union of two
> independent lineages. The normalized row-to-row stitch is editorial and does
> not claim all stages occur in one process or jurisdiction.

> **Claim record — WFL-0003-C06 | analytic-judgment**
> **Claim:** The lineage contains both digital-control/data→process/product and
> material/process-signal→digital control/quality-decision dependencies, while
> cyber origin, exploitation and safeguard failure remain separate predicates.
> **Claim status:** active
> **Scope:** Functional directionality in represented biomanufacturing
> processes; not an observed reverse-direction incident or outcome.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Figure 1 and §Digital Information Flow in Biomanufacturing;
> [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
> §§3.1.4–3.1.7 and 4.1–4.2, printed pp. 4–10
> (physical pp. 9–15); Annex III §2.3, printed p. 29
> (physical p. 34).
> **Basis / limits:** Both directions are explicit as intended operation. No
> source reports malicious manipulation of either direction.

## Candidate trust boundaries

At a high level, the diagrams support candidate boundaries between:

- the supplier/raw-material network and the manufacturer;
- process equipment/controllers and the supervisory layer;
- the manufacturing facility and an external or standalone control center;
- multiple manufacturing sites;
- provider- and patient-facing workflows and manufacturing operations;
- manufacturer, warehouse, and downstream providers.

These boundaries have no source-defined trust levels, identities, privileges,
protocols, or responsibility allocations. They are research targets, not
confirmed vulnerabilities.

## Continuous and distributed variants

The authors describe continuous manufacturing as a more automated end-to-end
process with stronger dependence on sensors and quality data, and distributed
manufacturing as a multiple-site model with greater dependence on coordination
and networks. These are 2019 projections and risk considerations, not current
adoption measurements
([SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
§§ Continuous Manufacturing, Distributed Manufacturing).

## Coverage limits

> **Claim record — WFL-0003-C04 | analytic-judgment**
> **Claim:** The current page is not yet a complete BMO digital thread because
> the sources do not provide sufficient detail or evidence for development and
> technology transfer, supplier qualification, complete QC/release authority,
> deviation/CAPA, storage, distribution, recall, retirement, or validated
> recovery flows.
> **Claim status:** superseded
> **Scope:** Coverage assessment after `SRC-0003`.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md),
> § Adding another dimension; [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Abstract; Figures 1–2; §§ Digital Information Flow in Biomanufacturing,
> Considerations for Emerging Biologic Products.
> **Basis / limits:** The sources name some broader functions but do not model
> them as a complete, verified lifecycle. Missing documentation here is not
> evidence that real manufacturers lack these processes. This historical gap
> assessment, made after ingesting `SRC-0003`, is superseded for current corpus
> coverage by `WFL-0003-C05`; its implementation and architecture gaps remain
> valid limitations.
> **Superseded by:** `WFL-0003-C05`.

Current residual gaps are detailed supplier qualification/technology transfer,
complete storage and recall execution, retirement and validated recovery. They
do not erase the now explicit frozen stage sequence, but they prevent this page
from being treated as a complete implementation or enterprise digital thread.

## Evidence and uncertainty

`SRC-0003` is `expert-analysis`, not empirical architecture validation. Merck
case context supports the importance of availability and continuity but is
secondary and does not validate Figure 1/2 or a control-integrity attack path.
Q13 supplies newer normative quality/release structure but no adoption,
deployment or effectiveness result. Merck context remains secondary and does
not validate a process-control integrity path.

## Related pages

- [SYS-0002 — Biomanufacturing process-control stack](../systems/sys-0002-biomanufacturing-process-control.md)
- [RSK-0002 — Process-control integrity or availability disruption](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [WFL-0001 — Single-site biomanufacturing system model](wfl-0001-biomanufacturing-system.md)
- [WFL-0002 — HCL cyberphysical workflow](wfl-0002-high-containment-laboratory.md)
- [SRC-0003 — Guttieres et al. 2019](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [SRC-0031 — ICH Q13](../sources/src-0031-ich-q13-continuous-manufacturing.md)
- [AST-0007 — biomanufacturing assets/stakeholders](../assets/ast-0007-biomanufacturing-assets-stakeholders.md)
- [GOV-0016 — Q13 governance/adoption](../governance/gov-0016-ich-q13-continuous-manufacturing.md)
- [CTL-0015 — continuous-manufacturing quality controls](../controls/ctl-0015-continuous-manufacturing-quality-control.md)
- [SYN-0016 — BMO four-cell reconciliation](../syntheses/syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)
- [VUL-0003 — BMO exposure classes](../vulnerabilities/vul-0003-biomanufacturing-data-integrity-ot-access-dependencies.md)
- [INC-0006 — observed manufacturing/order disruption](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md)
- [RSK-0019 — observed supply path](../risk-scenarios/rsk-0019-merck-cyber-manufacturing-supply-disruption.md)
- [CTL-0020 — incident control lessons](../controls/ctl-0020-merck-incident-vendor-update-continuity-recovery-lessons.md)
- [SYN-0028 — BMO residual reconciliation](../syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)

## Sources

- [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md), § Adding another
  dimension; Figure 1.
- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md), Figures 1–2;
  §§ Digital Information Flow in Biomanufacturing, Considerations for Emerging
  Biologic Products.
- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
  §§1–4; Annex III; Annex V.
