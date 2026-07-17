---
id: CTL-0001
type: control
title: Risk-based laboratory information and cybersecurity controls
aliases:
  - laboratory information-security controls
  - WHO laboratory cyber control set
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0002
  - SRC-0004
  - SRC-0018
sensitivity: public
dual_use: moderate
control_status: recommended
implementation_status: unknown
testing_status: unknown
effectiveness_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: CTL-0001-C01
    evidence:
      - source: SRC-0004
        locator: "§6.5, printed pp. 34–37 (PDF pp. 54–57); §6.6, printed pp. 37–39 (PDF pp. 57–59); Annex 1, printed pp. 71–77 (PDF pp. 91–97)"
  - predicate: governed-by
    target: GOV-0001
    claim_id: CTL-0001-C01
    evidence:
      - source: SRC-0004
        locator: "§§4–5, printed pp. 12–23 (PDF pp. 32–43); §8.1, printed pp. 45–51 (PDF pp. 65–71)"
  - predicate: mitigates
    target: RSK-0001
    claim_id: CTL-0001-C02
    evidence:
      - source: SRC-0002
        locator: "§§ Cyber elements of high-containment laboratories and Identified Areas of Impact; Figure 2; Table 1"
      - source: SRC-0004
        locator: "§5.3.4, printed pp. 21–22 (PDF pp. 41–42); §§6.5–6.6, printed pp. 34–39 (PDF pp. 54–59)"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: CTL-0001-C06
    evidence:
      - source: SRC-0004
        locator: "§§6.3–6.6, printed pp. 31–39 (PDF pp. 51–59); §7, printed pp. 40–44 (PDF pp. 60–64)"
      - source: SRC-0018
        locator: "§§5.2.3, 6.2.1 and 6.3–6.5, printed pp. 71–75, 97–108, 126–138 (PDF pp. 88–92, 114–125, 143–155)"
tags:
  - laboratories
  - information-security
  - cybersecurity
  - risk-assessment
  - incident-response
  - recommended-control
---

# Risk-based laboratory information and cybersecurity controls

> WHO-recommended defensive control set for biosecurity-relevant information,
> connected laboratory equipment and facility/security systems. It is recorded
> as **recommended**; implementation, testing and effectiveness are all
> **unknown**.

## Objective

Reduce confidentiality, integrity, authentication and availability risk where
digital information or connected systems can affect biological-material
accountability, laboratory work, containment/safety support, continuity or
biosecurity decisions. Control choice must follow local biological and cyber
risk assessment rather than a generic checklist.

## Evidence status

| Dimension | Current status | What would change it |
| --- | --- | --- |
| Recommended | Yes — WHO normative guidance | Superseding/revised issuer guidance |
| Implemented | Unknown | Facility/program implementation record |
| Tested | Unknown | Test, exercise, audit or validation record for a defined deployment |
| Effective | Unknown | Outcome evidence tied to a scenario edge and relevant conditions |
| Independently evaluated | Unknown | Independent assessment with method, scope and results |

> **Claim record — CTL-0001-C01 | source-report**
> **Claim:** WHO recommends layered physical, personnel, electronic and
> administrative protection for biosecurity-relevant information and connected
> laboratory/facility systems, combined with risk assessment, incident response,
> recovery preparation and periodic assurance.
> **Claim status:** active
> **Scope:** Control-family recommendation from global laboratory guidance;
> not a technical baseline for every architecture.
> **As of:** 2024-06-21.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §6.5, printed pp. 34–37 (PDF pp. 54–57); §6.6, printed
> pp. 37–39 (PDF pp. 57–59); Annex 1, printed pp. 71–77
> (PDF pp. 91–97).
> **Basis / limits:** Categories are direct. Exact methods, maturity,
> implementation and effectiveness are not reported; current technical
> standards must refine the recommendations.

## Control functions

The following mapping is a wiki functional organization, not a claim that WHO
uses NIST function labels:

| Function | Safe high-level objective | Evidence boundary |
| --- | --- | --- |
| Identify | Inventory biosecurity-relevant information, equipment, dependencies, roles and applicable requirements | Does not establish a complete asset inventory |
| Protect | Apply authorized access, appropriate authentication, data/device/network protection and controlled lifecycle handling | No product, protocol or configuration is prescribed here |
| Detect | Maintain monitoring, protected reporting, discrepancy review and mechanisms to recognize suspected incidents | No detection rate or coverage evidence |
| Contain/respond | Use a locally validated escalation and response plan coordinated with biological safety, facilities and leadership | Annex steps are not universal OT/safety instructions |
| Recover | Prepare protected backups, continuity and restoration while preserving trustworthy material/data status | Backup presence alone does not prove safe recovery |
| Assure/improve | Audit, test, exercise, validate, investigate, track corrective action and reassess after change | These are recommended activities, not completed assurance |

## Scenario edges addressed

For
[RSK-0001](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md), the set
can address:

- origin prevention/detection for unauthorized or unreliable digital access;
- containment of propagation from information/control systems to laboratory
  operations;
- incident escalation and coordination before a cyber issue becomes a physical
  or biological consequence;
- recovery of trustworthy digital state together with material/process
  disposition and safety review.

> **Claim record — CTL-0001-C02 | analytic-judgment**
> **Claim:** `CTL-0001` conditionally mitigates the origin and transfer edges of
> `RSK-0001` because WHO's control scope includes information, connected
> laboratory equipment and building/security systems; no exact-edge
> effectiveness is established.
> **Claim status:** active
> **Scope:** High-level mapping to a hypothetical HCL containment-support
> scenario, not a facility control assertion.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> §§ Cyber elements of high-containment laboratories and Identified Areas of
> Impact; Figure 2; Table 1;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §5.3.4, printed pp. 21–22; §§6.5–6.6, printed pp. 34–39.
> **Basis / limits:** `SRC-0002` supplies the scenario dependency classes and
> `SRC-0004` supplies recommended control scope. WHO cites Crawford for cyber
> context, so this is not independent scenario corroboration; no implementation
> or test closes the edge.

## Applicability and prerequisites

The set is applicable only after identifying which information and systems have
material biosecurity relevance. Prerequisites include:

- institutional policy, accountable ownership and decision authority;
- current inventory of relevant data, equipment and dependencies;
- combined biosafety/biosecurity/cyber assessment with explicit tradeoffs;
- lawful, proportionate access and personnel processes;
- local IT/OT, facilities, safety, quality and incident-response coordination;
- resources for maintenance, training, assurance and corrective action;
- current legal/regulatory requirements and technical standards.

## Dependencies

- [GOV-0001](../governance/gov-0001-who-laboratory-biosecurity-guidance-2024.md)
  provides programme and oversight context.
- [WFL-0004](../workflows/wfl-0004-high-consequence-material-lifecycle.md) defines
  where information/equipment protection intersects material accountability.
- [SYS-0001](../systems/sys-0001-hcl-containment-support-systems.md) identifies a
  possible safety/containment dependency class but not an architecture.

## Implementation considerations

Implementation should be proportionate to the local consequence and dependency,
assign accountable roles, protect relevant information/systems across their
lifecycle, coordinate IT, facilities and biological safety, and locally validate
incident/recovery decisions before adoption.

WHO's detailed personnel-screening table is not carried into this control.
Any personnel measure must be lawful, role-relevant, privacy-preserving,
non-discriminatory, reviewable and paired with support and due process.

## Failure modes and tradeoffs

- a security action can conflict with containment, safety, quality or continuity;
- generic response actions can conflict with containment, safety or continuity
  unless their local tradeoffs are assessed and validated;
- restrictive access can impede outbreak response, research collaboration or
  safety-critical information sharing;
- untested backup can restore untrusted state or leave material disposition
  ambiguous;
- monitoring can create privacy or insider-risk harms if governance is weak;
- checklist compliance can obscure missing asset/dependency knowledge;
- controls can degrade after personnel, software, equipment or workflow changes.

> **Claim record — CTL-0001-C03 | source-report**
> **Claim:** WHO explicitly says biosafety and biosecurity measures may overlap
> or interfere and recommends coordinated risk-based prioritization, alternatives
> and reassessment.
> **Claim status:** active
> **Scope:** General safety/security tradeoff principle.
> **As of:** 2024-06-21.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §5.1, printed pp. 19–20 (PDF pp. 39–40); Figure 1.1.
> **Basis / limits:** Source states the overlap and need for decisions but does
> not resolve a specific facility tradeoff. Local safety engineering remains
> required.

## Validation and evidence of effectiveness

WHO recommends evaluating availability, effectiveness and sustainability,
determining residual risk, auditing, testing, exercising, investigating and
tracking corrective actions. Those recommendations define an assurance plan;
they do not supply assurance evidence.

> **Claim record — CTL-0001-C04 | source-report**
> **Claim:** The WHO template requires users to assess whether selected measures
> are available, effective and sustainable and whether residual risk is
> acceptable, then review them after change or lessons learned.
> **Claim status:** active
> **Scope:** Recommended assurance questions, not measured answers.
> **As of:** 2024-06-21.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> Annex 1, printed pp. 71–77 (PDF pp. 91–97); §6.6.1, printed p. 38
> (PDF p. 58).
> **Basis / limits:** Template fields are explicit. No filled template, control
> test, incident outcome or independent evaluation is included.

> **Claim record — CTL-0001-C05 | analytic-judgment**
> **Claim:** Current corpus supports `recommended` status only; implementation,
> testing, effectiveness and independent evaluation of `CTL-0001` remain
> unknown.
> **Claim status:** active
> **Scope:** Evidence classification after `SRC-0004`.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§5–6 and Annexes 1–2; source methods/limitations.
> **Basis / limits:** Guidance provides recommendations/templates only. This
> claim must be updated if implementation or evaluation sources are ingested.

## Framework mappings

WHO custody/inventory and laboratory programme controls now combine with NIST
SP 800-82r3's generic identity/access, segmentation, monitoring, response and
recovery functions. NIST remains general OT guidance, not HCL custody guidance
or a substitute for local containment validation. Its Rev. 3 mapping is CSF
1.1/versioned SP 800-53 Rev. 5, not CSF 2.0. The WHO password box at printed
p. 37 remains excluded because its construction/periodic-change advice is not
accepted as current technical best practice without more specific
reconciliation.

> **Claim record — CTL-0001-C06 | analytic-judgment**
> **Claim:** Independent WHO and NIST lineages jointly support a two-limb
> laboratory control map: material inventory/custody/accountability plus
> generic OT access/segmentation/monitoring/response/recovery, with both limbs
> mapped conditionally rather than treated as implementation.
> **Claim status:** active
> **Scope:** Exact functional coverage for `WFL-0004` custody edges and the
> digital HCL edges of `RSK-0001`; no biobank, facility or tested-control claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§6.3–6.4.2, printed pp. 31–34 (PDF pp. 51–54); §7,
> printed pp. 40–44 (PDF pp. 60–64);
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §5.2.3, printed pp. 71–75; §6.2.1, printed pp. 97–108;
> §§6.3–6.5, printed pp. 126–138.
> **Basis / limits:** WHO custody and NIST technical functions are direct and
> independent; the stitch is editorial. NIST does not validate HCL containment
> or material custody, and no implementation/test/effectiveness follows.

## Related pages

- [SRC-0019 — Canadian Biosafety Standard](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [GOV-0009 — Canadian CBS governance](../governance/gov-0009-canadian-biosafety-standard-third-edition.md)

- [RSK-0001 — Disruption of digitally supported containment functions in an HCL](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md)
- [SYS-0001 — Containment-support cyberphysical systems in an HCL](../systems/sys-0001-hcl-containment-support-systems.md)
- [WFL-0004 — Lifecycle of high-consequence and biosecurity-relevant laboratory material](../workflows/wfl-0004-high-consequence-material-lifecycle.md)
- [GOV-0001 — WHO Laboratory Biosecurity Guidance 2024](../governance/gov-0001-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0004 — WHO Laboratory Biosecurity Guidance 2024](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SYN-0006 — Official control function/state taxonomy](../syntheses/syn-0006-official-control-function-state-taxonomy.md)
- [CTL-0011 — OT defense-in-depth and resilience](ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [SYN-0007 — OT applicability synthesis](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)
- [SRC-0018 — NIST SP 800-82r3](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)

## Sources

- [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
  HCL asset/dependency and potential-impact model.
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
  §§5–6; Annexes 1–2.
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
  §§5.2.3, 6.2.1 and 6.3–6.5.
