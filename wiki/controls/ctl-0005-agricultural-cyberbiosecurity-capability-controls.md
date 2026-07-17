---
id: CTL-0005
type: control
title: Agricultural cyberbiosecurity capability and response controls
aliases:
  - smart-farm cyberbiosecurity capability controls
  - agriculture training monitoring and response controls
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0010
  - SRC-0018
  - SRC-0032
  - SRC-0035
sensitivity: public
dual_use: low
control_status: mixed-recommended-and-bounded-surveillance
implementation_status: bounded-biological-surveillance-elements
testing_status: bounded-method-and-survey-design
effectiveness_status: unknown
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0010
    claim_id: CTL-0005-C01
    evidence:
      - source: SRC-0010
        locator: "HTML #s3-2, lines 1556–1565; #s4, lines 1693–1698; #s6, lines 1702–1704"
  - predicate: mitigates
    target: RSK-0007
    claim_id: CTL-0005-C02
    evidence:
      - source: SRC-0010
        locator: "HTML #s3-2, lines 1556–1565; #s4, lines 1693–1698; #s6, lines 1702–1704"
  - predicate: depends-on
    target: WFL-0007
    claim_id: CTL-0005-C02
    evidence:
      - source: SRC-0010
        locator: "HTML #s1, lines 1472–1473; #s3-2, lines 1556–1565; #s4, lines 1693–1698"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: CTL-0005-C04
    evidence:
      - source: SRC-0010
        locator: "HTML #s1-1, #s1-4 and #s3-1–2; Tables 1–2"
      - source: SRC-0018
        locator: "§§2.3.8, 5.3.3, 5.3.6–5.3.7, 6.2.9–6.2.10 and 6.3–6.5, printed pp. 26–28, 81–82, 120–138"
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: CTL-0005-C05
    evidence:
      - source: SRC-0032
        locator: "Data/governance design, printed pp. 19–20, 24–39 and 60–68 (physical pp. 25–26, 30–45 and 66–74); data sharing, printed pp. 97–99 (physical pp. 103–105); Objectives B–F, printed pp. 121–129 (physical pp. 127–135)"
  - predicate: governed-by
    target: GOV-0017
    claim_id: CTL-0005-C05
    evidence:
      - source: SRC-0032
        locator: "Governance/implementation roles and Objectives B–F, printed pp. 35–39 and 121–129 (physical pp. 41–45 and 127–135)"
  - predicate: evidenced-by
    target: SRC-0035
    claim_id: CTL-0005-C07
    evidence:
      - source: SRC-0035
        locator: "Main PDF pp. 24–35 and 43–49; Annex A; APHA PDF pp. 3–7"
tags:
  - agriculture
  - training
  - monitoring
  - incident-response
  - collaboration
  - recommended-control
---

# Agricultural cyberbiosecurity capability and response controls

> Recommended capability family for role-appropriate training, dependency
> awareness, data validation/provenance, privacy/cyber standards, traceability,
> early warning, monitoring/reporting, locally validated response and cross-
> sector learning. Selected biological-surveillance elements are implemented/
> method-tested in a bounded UK case; no represented source shows complete
> cyberbiosecurity-family implementation, effectiveness or qualifying
> independent evaluation.

## Objective

Reduce the chance that unreliable digital state or unavailable access silently
propagates into agricultural production and downstream supply, and improve
recognition, escalation, safe continuity and learning when a disruption is
suspected.

## Evidence status

| Dimension | Status | Evidence boundary |
| --- | --- | --- |
| Recommended | **Yes** | Author/participant proposals plus AU strategy/action-plan recommendations |
| Implemented | **Partial, bounded** | PATH-SAFE/APHA used sampling logistics, DSA/anonymisation, RT-PCR and weekly reporting in one survey; no complete cyberbiosecurity deployment/adoption denominator |
| Tested | **Partial, method-level** | Assay pre-check and a 99%/1% sample-design target were applied; no cyber drill, control-family acceptance test or numeric assay-performance result |
| Effective | Unknown | No baseline, endpoint or outcome comparison |
| Independently evaluated | Unknown | RAND has a distinguishable commissioned evaluator role, but not qualifying independent safeguard-effectiveness evaluation/replication |

> **Claim record — CTL-0005-C01 | source-report**
> **Claim:** Drape et al. recommend or report proposals for tailored training,
> train-the-trainer material, shared vocabulary, cross-sector collaboration,
> response protocols, better threat/breach tracking, proportionate authorized
> assessment and possible smart-equipment standards or assistance.
> **Claim status:** active
> **Scope:** High-level agricultural capability recommendations; not a binding
> standard, detailed assessment procedure or deployed safeguard.
> **As of:** 2021-08-19.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML Theme 2 `#s3-2`, lines 1556–1565; Discussion `#s4`, lines 1693–1698;
> Recommendations `#s6`, lines 1702–1704.
> **Basis / limits:** Recommendation status is explicit. The study supplies no
> implementation record, technical procedure, test, metric, causal outcome or
> independent evaluation.

## Scenario edges addressed

For [RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md),
the family can be mapped conditionally to:

1. **dependency/precondition edge:** identify which data/access genuinely
   matters to `WFL-0007` and assign responsibility;
2. **human-recognition edge:** role-appropriate training and a common language
   support recognition and escalation;
3. **detection/reporting edge:** proportionate monitoring and documented
   reporting identify loss of trustworthy state;
4. **transfer/response edge:** locally validated protocols, human review and
   safe continuity choices can contain a digital issue before production;
5. **recovery/learning edge:** verified restoration, incident learning and
   cross-sector coordination update controls.

> **Claim record — CTL-0005-C02 | analytic-judgment**
> **Claim:** These recommended families map to the precondition, detection,
> transfer, response and learning edges of `RSK-0007`, but the source does not
> show that any mapped control interrupted an event or reduced risk.
> **Claim status:** active
> **Scope:** Exact-edge defensive interpretation for the bounded
> `WFL-0007` segment.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s3-2`, lines 1556–1565; Discussion `#s4`, lines 1693–1698;
> Recommendations `#s6`, lines 1702–1704.
> **Basis / limits:** The mapping is wiki analysis. No event, deployed
> architecture, test result, counterfactual or independent outcome supports an
> effectiveness conclusion.

## AU data, traceability and resilience extension

AU DAS adds the following prospective control functions:

- validate data and retain comprehensive collection/processing/date/owner
  metadata before decision use;
- improve interoperability, quality and controlled sharing through national/
  regional data platforms;
- develop minimum privacy and cybersecurity standards and national policy/
  regulatory capacity;
- use farmer/animal identity, registries, traceability and certification to
  preserve provenance and support value-chain decisions;
- build agricultural climate and pest/disease early-warning and data platforms;
- assign AU/REC/Member-State and agriculture/ICT coordination roles;
- plan monitoring/evaluation through intended outcomes/KPIs and improve
  resilience, infrastructure, skills and financing.

> **Claim record — CTL-0005-C05 | source-report**
> **Claim:** AU DAS recommends validation/metadata/interoperability,
> privacy/cybersecurity standards, identity/traceability, early warning,
> cross-sector coordination, planned monitoring/evaluation and resilience
> functions for digital agriculture.
> **Claim status:** active
> **Scope:** Continental/regional/national strategy and action-plan functions;
> not a completed technical standard, implemented safeguard, tested response/
> recovery procedure or effectiveness result.
> **As of:** 2023-10.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> data/governance design, printed pp. 19–20, 24–39 and 60–68 (physical pp.
> 25–26, 30–45 and 66–74); data-sharing risks/controls, printed pp. 97–99
> (physical pp. 103–105); Objectives B–F, printed pp. 121–129 (physical pp.
> 127–135).
> **Basis / limits:** Named functions and action levels are direct. Targets,
> standards-to-be-developed and platform outcomes remain prospective; no
> incident-response/recovery metric or independent assurance is supplied.
> Early warning concerns agricultural climate/pest/disease signals and is not
> cyber-detection evidence.

> **Claim record — CTL-0005-C06 | analytic-judgment**
> **Claim:** The combined Drape, NIST, AU and PATH-SAFE portfolio can map
> prevention,
> generic cyber detection/response planning, agricultural early-warning,
> traceability, bounded biological-surveillance detection/reporting and
> resilience functions to `RSK-0007`, but it still lacks a complete
> agriculture-specific cyber response/trusted-recovery and explicit
> traceability-boundary stitch or demonstrated cyber-control interruption/
> effectiveness result.
> **Claim status:** active
> **Scope:** Current exact-edge evidence boundary for the canonical agriculture
> control page; not a frozen-cell decision, implementation claim or compliance
> assessment.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> `SRC-0010-C06/C07`; [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§5–6; [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C07/C08`; [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C05`–`C08`.
> **Basis / limits:** Distinct sources cover complementary functions;
> independence is claim-specific because AU cites/derives some FAO/ITU/Figure 2
> and use-case background, while PATH-SAFE delivery/evaluation roles share one
> programme ecosystem. Bounded biological-surveillance deployment does not
> establish complete cyber incident recovery, explicit traceability control,
> cyber-control testing or independent outcome effectiveness.

## PATH-SAFE bounded surveillance-control evidence

The 2024 APHA survey directly applied several biological-surveillance control
elements: pre-use assay assessment on milk matrices; a sample-size/PPS design;
processor consent and a Defra–National Milk Records data-sharing agreement;
ITL1 anonymisation; same-day laboratory testing; and weekly reporting to chief
veterinary officers and policy makers. The evaluation also records selected
method/process adoption plus limited programme-wide business-as-usual and
scale-up certainty.

> **Claim record — CTL-0005-C07 | source-report**
> **Claim:** PATH-SAFE/APHA supplies bounded implementation and method-level
> testing evidence for biological-surveillance detection, data-sharing/
> anonymisation and reporting controls, together with explicit maturity and
> evaluation limitations.
> **Claim status:** active
> **Scope:** Represented PATH-SAFE projects and 2024 Great Britain bulk-milk
> survey; not implementation or testing of the Drape/NIST cyber controls,
> complete traceability/recovery, causal effectiveness or independent
> safeguard evaluation.
> **As of:** 2025-06-18.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C05`–`C08`; main PDF pp. 24–35 and 43–49; Annex A;
> APHA PDF pp. 3–7.
> **Basis / limits:** Implementation, survey design and reporting are direct.
> The all-negative biological result is not a control-failure or effectiveness
> result; the 99% survey-design probability is not assay sensitivity; RAND's
> commissioned evaluation does not independently replicate the safeguard.

## Applicability, prerequisites and dependencies

- identify the farm/production context, safety constraints and material digital
  dependencies before selecting controls;
- assign accountable producer, technology-provider, supplier/vendor and
  escalation roles;
- tailor training and response to workforce, scale, connectivity and available
  resources;
- validate any continuity or recovery procedure locally so security action does
  not create a production, animal/plant-health or worker-safety problem;
- preserve trustworthy observations and provenance for decisions and recovery.

The source does not establish these prerequisites as implemented.

## Failure modes and tradeoffs

- generic training may not match local work or decision authority;
- monitoring can create noise, cost and additional sensitive data without a
  response owner;
- a protocol can fail if dependencies, safe states or supplier roles are wrong;
- resource-heavy assurance may be inaccessible to smaller producers;
- a single standardized control can conflict with heterogeneous equipment,
  safety, connectivity and production constraints.

> **Claim record — CTL-0005-C03 | source-report**
> **Claim:** The source says agricultural cyberbiosecurity is not one-size-fits-
> all and records concern that smaller producers may lack infrastructure,
> expertise or resources to adopt proposed measures.
> **Claim status:** active
> **Scope:** Workshop finding and implementation constraint, not proof that a
> particular control is infeasible or ineffective.
> **As of:** 2020-10-07.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML Theme 1 `#s3-1`, lines 1547–1556; Theme 2 `#s3-2`, lines 1556–1565;
> Discussion `#s4`, lines 1693–1698.
> **Basis / limits:** The constraint is directly reported as participant/
> author synthesis. Missing denominators prevent prevalence or cost inference.

## Validation method and evidence of effectiveness

A future complete validation should state environment, control version,
baseline, scenario edge, safety constraints, acceptance metric, adverse/null
results and independent evaluator. PATH-SAFE supplies a bounded biological-
surveillance implementation and evaluation, but no complete cyberbiosecurity
control-family test or causal effect; assurance beyond the stated partial
method/deployment evidence remains unknown.

## External framework mappings

NIST SP 800-82r3 supplies a current generic OT mapping for inventory, remote
access, monitoring, response and recovery. AU DAS adds a distinct agriculture-
specific regional strategy layer for data quality, traceability,
privacy/cyber standards and early warning. Neither is an implemented
agricultural cyberbiosecurity standard, One Health control baseline or
compliance/effectiveness result. Agency standards discussed by workshop
participants and AU minimum standards-to-be-developed remain proposals.

> **Claim record — CTL-0005-C04 | analytic-judgment**
> **Claim:** Independent agriculture and NIST sources support a conditional
> generic-OT overlay for the connected-equipment edges of `RSK-0007`, while
> the pre-`SRC-0032` pair did not supply traceability, biological-biosecurity,
> One Health or effectiveness limbs.
> **Claim status:** active
> **Scope:** Bounded `SYS-0005/RSK-0007` technical branch, not an agriculture
> compliance standard or full sector control model.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1-1`, `#s1-4`, `#s3-1–2` and Tables 1–2;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.8, 5.3.3, 5.3.6–5.3.7, 6.2.9–6.2.10 and 6.3–6.5,
> printed pp. 26–28, 81–82, 120–138.
> **Basis / limits:** Component/control overlap is independent/direct; exact
> edge mapping is inferred. `SRC-0032` later adds recommended conceptual
> traceability but not deployment, tested response/recovery or effectiveness;
> current combined limits are in `CTL-0005-C06`.

## Related pages

- [SRC-0020 — U.S. National One Health Framework](../sources/src-0020-us-national-one-health-framework-2025-2029.md)
- [GOV-0010 — U.S. One Health governance](../governance/gov-0010-us-national-one-health-framework-2025-2029.md)

- [RSK-0007 — Farm data/access production and supply disruption](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)
- [WFL-0007 — Smart-farm monitoring, production and supply segment](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [SYS-0005 — Connected smart-farm ecosystem](../systems/sys-0005-connected-smart-farm-ecosystem.md)
- [AST-0003 — Smart-farm production and supply assets](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [SRC-0010 — Drape et al. 2021](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0018 — NIST SP 800-82r3](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0032 — AU Digital Agriculture Strategy](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0035 — UK PATH-SAFE evaluation and implementation package](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [GOV-0017 — AU digital-agriculture governance](../governance/gov-0017-au-digital-agriculture-strategy-2024-2030.md)
- [CTL-0011 — OT defense-in-depth and resilience](ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [SYN-0007 — OT applicability synthesis](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)
- [SYN-0017 — Agriculture transfer/control/governance reconciliation](../syntheses/syn-0017-au-agriculture-transfer-control-governance-reconciliation.md)

## Sources

- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md), HTML
  `#s1`, `#s3-1`, `#s3-2`, `#s4`, `#s5` and `#s6`.
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
  §§2.3.8, 5.3, 6.2.9–6.2.10 and 6.3–6.5.
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
  printed pp. 19–20, 24–39, 60–68, 97–99 and 121–129.
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md), main PDF
  pp. 24–35 and 43–49; Annex A; APHA PDF pp. 3–7.
