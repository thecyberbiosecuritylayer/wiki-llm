---
id: WFL-0007
type: workflow
title: Smart-farm monitoring, production and supply segment
aliases:
  - smart-farm monitoring-to-supply workflow
  - connected agriculture production segment
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0010
  - SRC-0032
  - SRC-0035
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0010
    claim_id: WFL-0007-C01
    evidence:
      - source: SRC-0010
        locator: "HTML #s1, lines 1472–1473; #s1-1, line 1475; #s1-4, line 1478; #s3-1, lines 1547–1556"
  - predicate: depends-on
    target: AST-0003
    claim_id: WFL-0007-C02
    evidence:
      - source: SRC-0010
        locator: "HTML #s1, lines 1472–1473; #s1-1, line 1475; #s1-4, line 1478"
  - predicate: depends-on
    target: SYS-0005
    claim_id: WFL-0007-C02
    evidence:
      - source: SRC-0010
        locator: "HTML #s1, lines 1472–1473; #s1-1, line 1475"
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: WFL-0007-C04
    evidence:
      - source: SRC-0032
        locator: "Figure 2, printed pp. 9–10 (physical pp. 15–16); data readiness, printed pp. 19–20 (physical pp. 25–26); Annex A1.1–A1.2, printed pp. 43–57 (physical pp. 49–63); action packages, printed pp. 81–99 (physical pp. 87–105)"
  - predicate: evidenced-by
    target: SRC-0035
    claim_id: WFL-0007-C06
    evidence:
      - source: SRC-0035
        locator: "Main PDF pp. 7, 13–19, 22–35; Box 1 pp. 24–26; Annex A §§A.1–A.4.5; APHA PDF pp. 3–7"
tags:
  - agriculture
  - smart-farming
  - monitoring
  - production
  - food-supply-chain
  - conceptual-workflow
---

# Smart-farm monitoring, production and supply segment

> Conceptual agriculture lifecycle connecting environmental/crop/livestock
> observation, farm management and production, value-chain movement,
> traceability and downstream supply. It reconciles a workshop-derived segment
> with AU strategy use cases, not a universal operating procedure or validated
> end-to-end data/material flow.

## Scope

`SRC-0010` supplies the original remote-monitoring→production→supply risk
segment. `SRC-0032` adds distinct AU strategy evidence for input delivery,
farm/breeding-cycle planning, production, collection/aggregation, processing,
quality, storage/cooling, transport, traceability/certification, markets and
environmental/pest/disease observation-to-decision paths. `SRC-0035` adds
implemented animal, food and environmental surveillance lanes, including a
bounded bulk-milk sample→laboratory result→policy-report path.

The page still excludes a complete seed/genetic-resource workflow, treatment,
regulated animal movement, formal recall, disposition and end-of-life. Its
diagnostic/surveillance and environmental-sampling lanes remain a heterogeneous
programme set, not a universal sequence, custody audit, food-safety validation
or consumer-use stage.

> **Claim record — WFL-0007-C01 | source-report**
> **Claim:** Drape et al. associate connected crop/livestock monitoring and
> farm-management technology with production/harvest and describe supplier,
> vendor and downstream food-supply dependencies that could transmit a local
> disruption.
> **Claim status:** active
> **Scope:** High-level associations in one qualitative/literature-synthesis
> article, not a validated sequence followed by every agricultural operation.
> **As of:** 2021-08-19.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML Introduction `#s1`, lines 1472–1473; `#s1-1`, line 1475;
> `#s1-4`, line 1478; Theme 1 `#s3-1`, lines 1547–1556.
> **Basis / limits:** The component associations and potential ripple effect are
> direct source statements. Exact order, handoffs, decision rights, timing,
> traceability, buffers and technical interfaces are not reported.

## Functional segment

| Segment | Relevant digital/physical/biological state | Evidence boundary |
| --- | --- | --- |
| Observe | Connected technology produces or presents information about crops/livestock | No instrument, measurement, calibration or coverage is validated |
| Exchange context | Information may move within a farm/facility or across supplier/vendor relationships | Direction, schema, authorization and contractual responsibility are unknown |
| Interpret/manage | A producer or worker may use information to monitor or manage operations | No decision rule or automation authority is specified |
| Produce/harvest | Physical and biological activity yields or preserves agricultural output | No crop/livestock process, quality or safety endpoint is measured |
| Move downstream | Product/output and associated business information support downstream users in a supply chain | No traceability, logistics topology, inventory or service level is supplied |
| Learn/respond | Organizations may recognize an issue, invoke a protocol and feed lessons into training | These are recommendations, not observed workflow performance |

The first five rows preserve the original Drape-derived ordering. The sixth is
a recommended improvement loop, not evidence that it currently exists.

> **Claim record — WFL-0007-C02 | analytic-judgment**
> **Claim:** A minimal source-derived workflow can be represented as
> `observe/exchange → interpret/manage → produce/harvest → move downstream`,
> depending on the distinct assets in `AST-0003` and candidate system
> dependencies in `SYS-0005`.
> **Claim status:** active
> **Scope:** Conceptual smart-farm segment for defensive risk mapping; not a
> claim of universal order, automation or end-to-end lineage.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1`, lines 1472–1473; `#s1-1`, line 1475; `#s1-4`, line 1478;
> `#s3-1`, lines 1547–1556.
> **Basis / limits:** Source names all included elements and links a stopped
> point to ripple effects. Ordering and dependency edges are wiki analysis;
> the source provides no process observation, trace, identity/custody record or
> system validation.

## Data, decision, material and responsibility boundaries

- **monitoring input ↔ management decision:** relevance and decision authority
  are unknown; false data need not affect production if independently checked;
- **digital access ↔ equipment/operation:** the source identifies the risk
  class but not whether a system can command, merely observe or only record;
- **farm/facility ↔ supplier/vendor:** exchange is named without direction,
  authentication, provenance or responsibility allocation;
- **production output ↔ downstream supply:** the source describes ripple
  concerns but not logistics, inventory buffers or traceability;
- **operator ↔ organization/authority:** roles and escalation ownership were
  workshop concerns, not an established responsibility model.

No boundary is labeled trusted, validated or deployed by this page.

> **Claim record — WFL-0007-C03 | analytic-judgment**
> **Claim:** `WFL-0007` is only a production/supply segment and cannot satisfy a
> complete agriculture/One Health lifecycle because diagnostics/surveillance,
> treatment/movement, trade/traceability, environmental sampling and
> disposition are absent from the source model.
> **Claim status:** superseded
> **Scope:** Evidence-sufficiency assessment of this page and `SRC-0010`.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML Abstract `#abstract1`, line 1470; Introduction `#s1`, lines 1472–1478;
> Methodology `#s2`, lines 1485–1545; Results/Discussion `#s3`–`#s4`, lines
> 1546–1698.
> **Basis / limits:** This was the correct pre-`SRC-0032` page-state judgment.
> The AU strategy later added environmental observation, traceability and
> broader value-chain stages; current limits are stated in `WFL-0007-C05`.
> **Superseded by:** `WFL-0007-C05`.

## AU production, data and value-chain extension

| Lifecycle segment | Direct AU state transition | Remaining boundary |
| --- | --- | --- |
| Plan and obtain inputs | farm/crop/breeding-cycle plan; input delivery, finance or insurance context | not a complete genetics/seed provenance lifecycle |
| Observe and validate | satellite/drone/ground sensor or human entry; validation, metadata and standards | not laboratory diagnostics or validated sampling |
| Produce and manage | crop/livestock/fisheries production; advisory or equipment/irrigation/fertilization action | no universal automation authority or operating procedure |
| Collect and transform | aggregation/collection, quality control and processing/transformation | food-safety test and release gates are incomplete |
| Store, cool and transport | physical product and associated records move through storage/cooling/logistics | custody, buffer and service levels are not supplied |
| Trace and certify | farmer/animal identity, barcode/RFID/QR/GPS and certification/traceability records support provenance | proposed/use-case design, not a completed audit |
| Market and learn | marketing/market access/payment plus planned monitoring/evaluation and lessons | recall, disposition and end-of-life remain absent |

The associated data path is `entry/observation → validation + metadata →
storage/update → sharing/interoperability → analysis → advisory, alert,
decision or machine feedback`.

> **Claim record — WFL-0007-C04 | source-report**
> **Claim:** AU DAS directly adds input/planning, observation/validation,
> production, collection/processing, storage/transport, traceability/
> certification and market stages plus a metadata/interoperability/analysis
> data lifecycle to the canonical agriculture workflow.
> **Claim status:** active
> **Scope:** Strategy-level lifecycle classes across multiple use cases; not a
> universal order, validated custody trace, deployed workflow or achieved
> outcome.
> **As of:** 2023-10.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> Figure 2, printed pp. 9–10 (physical pp. 15–16); data readiness, printed
> pp. 19–20 (physical pp. 25–26); strategy/use cases, printed pp. 23–24 and 37
> (physical pp. 29–30 and 43); Annex A1.1–A1.2, printed pp. 43–57 (physical
> pp. 49–63); action packages, printed pp. 81–99 (physical pp. 87–105).
> **Basis / limits:** Named stages and data states are direct. Their normalized
> ordering is editorial, and laboratory diagnostics, treatment/movement,
> recall/disposition and end-of-life remain missing.

> **Claim record — WFL-0007-C05 | analytic-judgment**
> **Claim:** The combined Drape/AU/PATH-SAFE page is broader than the original
> monitoring→production→supply fragment and now includes implemented
> diagnostic/surveillance and environmental-sampling lanes, but still cannot
> satisfy a complete agriculture/One Health lifecycle because treatment,
> regulated movement, formal recall/disposition/end-of-life and one joined
> custody lifecycle remain incomplete.
> **Claim status:** active
> **Scope:** Current evidence-sufficiency boundary for `WFL-0007`, not a claim
> that those stages do not exist in the wider sector.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> complete accessible article; [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> complete 145-page review and `SRC-0032-C04`;
> [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C03/C05` and `WFL-0007-C06`.
> **Basis / limits:** Current included/missing classes were checked across all
> three packages. PATH-SAFE's heterogeneous surveillance lanes do not create a
> universal custody lifecycle or supply the remaining treatment/movement/
> disposition predicates.

## PATH-SAFE surveillance lanes

PATH-SAFE supplies direct operational lanes across agriculture, food and the
environment. The best-located case separates the decision chronology from the
subsequent result flow:

1. prior pilot feasibility evidence, partner relationships, sampling logistics
   and workflow experience → Defra discussion/proposal → Animal Disease Policy
   Group selection of the bulk-milk approach;
2. processor consent and a Defra–NMR data-sharing agreement → raw bulk-milk
   collection representing 455 farms → processors submit to NMR → NMR delivers
   to APHA → APHA same-day RT-PCR → weekly reporting to chief veterinary
   officers/policy makers → bounded all-negative surveillance conclusion.

Other workstreams add wastewater, river/coastal/shellfish, abattoir, animal-
feed, raw-pet-food, hospital/care-home and genomic-source-attribution lanes.
They do not collapse into one custody trace or establish treatment, regulated
movement, recall or disposition.

> **Claim record — WFL-0007-C06 | source-report**
> **Claim:** PATH-SAFE directly adds implemented biological/environmental
> sample→processing/test/sequencing→metadata/analysis→report or surveillance-
> decision lanes, while the primary bulk-milk record separates the prior
> method-selection decision from later weekly null-result reporting.
> **Claim status:** active
> **Scope:** Represented PATH-SAFE projects and the 23 May–27 June 2024 APHA
> survey; not a universal One Health workflow, treatment/movement/disposition
> lifecycle or proof that weekly reports caused a later policy decision.
> **As of:** 2025-03-11.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C03/C05/C06`; main PDF pp. 7, 13–19, 22–35; Box 1,
> pp. 24–26; Annex A §§A.1–A.4.5; APHA PDF pp. 3–7.
> **Basis / limits:** Stages and the two bulk-milk paths are direct across the
> commissioned evaluation and distinct primary APHA implementation record.
> Their programme relationship prevents blanket SF3 independence; normalized
> cross-project ordering remains editorial.

## Disruption and fallback boundary

[RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)
uses the segment only conditionally: a digital change crosses into production
only where data/access materially informs or enables the physical/biological
stage and safeguards do not stop it. Supply consequence additionally requires
duration/severity sufficient to exceed local and downstream buffers.

[CTL-0005](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
records recommended planning, monitoring/reporting, response and learning
objectives. The source does not demonstrate a deployed fallback, tested response
or safe-recovery path.

## Evidence and uncertainty

The evidence base now includes a U.S.-centered workshop and a distinct AU
regional strategy whose claim-specific independence requires later synthesis.
The map still does not show universal
adoption, actual custody/data lineage, device authority, food-safety release,
recall/disposition or biological outcomes. The FAO/AUC companion documents an
implementation-support session and uneven continental digital-agriculture
progress, not measured DAS implementation, adoption or KPI attainment.
PATH-SAFE now supplies bounded operational and laboratory/animal-health
evidence. Complete treatment/movement/disposition, custody and independent
effectiveness evidence remain required.

## Related pages

- [SRC-0021 — programme lifecycle and sector-scope boundary](../sources/src-0021-quadripartite-one-health-jpa-national-guide.md)
- [SYN-0009 — reconciled One Health scope and explicit lifecycle gap](../syntheses/syn-0009-global-us-one-health-scope-reconciliation.md)
- [SRC-0020 — U.S. National One Health Framework](../sources/src-0020-us-national-one-health-framework-2025-2029.md)
- [GOV-0010 — U.S. One Health governance](../governance/gov-0010-us-national-one-health-framework-2025-2029.md)

- [AST-0003 — Smart-farm production and supply assets](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [SYS-0005 — Connected smart-farm ecosystem](../systems/sys-0005-connected-smart-farm-ecosystem.md)
- [RSK-0007 — Farm data/access production and supply disruption](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)
- [RSK-0017 — Agriculture cyber disruption to production/supply](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [CTL-0005 — Agricultural cyberbiosecurity capability controls](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [CTL-0018 — Agriculture ransomware continuity/recovery controls](../controls/ctl-0018-agriculture-cyber-resilience-and-recovery-controls.md)
- [SRC-0010 — Drape et al. 2021](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0032 — AU Digital Agriculture Strategy](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0035 — UK PATH-SAFE evaluation and implementation package](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [GOV-0017 — AU digital-agriculture governance](../governance/gov-0017-au-digital-agriculture-strategy-2024-2030.md)
- [HAZ-0004 — Ecological and supply hazards](../hazards/haz-0004-agriculture-climate-pest-disease-and-supply-hazards.md)
- [INC-0004 — JBS cattle-processing disruption](../incidents/inc-0004-jbs-cyberattack-cattle-slaughter-disruption-2021.md)
- [INC-0005 — Anonymous chicken-farm animal-effect incident](../incidents/inc-0005-anonymous-chicken-farm-temperature-control-animal-deaths-2023.md)
- [RSK-0018 — Poultry-barn cyber-to-animal path](../risk-scenarios/rsk-0018-poultry-barn-cyber-temperature-control-animal-harm.md)

## Sources

- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md), HTML
  `#s1`, `#s1-1`, `#s1-4`, `#s3-1`, `#s4` and `#s6`.
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
  printed pp. 9–10, 19–24, 37, 43–57 and 81–99.
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md), main PDF
  pp. 7, 13–19, 22–35; Annex A; APHA PDF pp. 3–7.
