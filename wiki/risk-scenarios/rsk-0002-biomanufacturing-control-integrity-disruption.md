---
id: RSK-0002
type: risk-scenario
title: Disruption of integrity or availability in biomanufacturing process control
aliases:
  - biomanufacturing control-integrity disruption
  - digital-control to product-quality disruption
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0003
  - SRC-0018
  - SRC-0031
sensitivity: public
dual_use: moderate
origin_domain: cyber
destination_domains:
  - physical
  - biological
  - clinical
relations:
  - predicate: evidenced-by
    target: SRC-0003
    claim_id: RSK-0002-C01
    evidence:
      - source: SRC-0003
        locator: "§ Digital Information Flow in Biomanufacturing; Figure 1; § Known Cybersecurity Risks Point to Vulnerabilities in Biomanufacturing, paragraphs after the Merck case"
  - predicate: depends-on
    target: SYS-0002
    claim_id: RSK-0002-C01
    evidence:
      - source: SRC-0003
        locator: "§ Digital Information Flow in Biomanufacturing; Figure 1"
  - predicate: affects
    target: WFL-0003
    claim_id: RSK-0002-C03
    evidence:
      - source: SRC-0003
        locator: "§§ Known Cybersecurity Risks Point to Vulnerabilities in Biomanufacturing, Digital Information Flow in Biomanufacturing; Figure 1"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: RSK-0002-C05
    evidence:
      - source: SRC-0003
        locator: "Digital Information Flow in Biomanufacturing and Figure 1"
      - source: SRC-0018
        locator: "§2.3.3, printed pp. 19–21 (PDF pp. 36–38); §§3.2–3.2.1 and 4.1.1–4.1.2, printed pp. 34–35, 46–52 (PDF pp. 51–52, 63–69)"
  - predicate: evidenced-by
    target: SRC-0031
    claim_id: RSK-0002-C05
    evidence:
      - source: SRC-0031
        locator: "Part I §§3.1.1–3.1.7 and 4.1–4.9, printed pp. 2–12 (physical pp. 7–17); Annex III §§2–3, printed pp. 28–30 (physical pp. 33–35); Annex V §§1–3.3, printed pp. 37–41 (physical pp. 42–46)"
  - predicate: affects
    target: AST-0007
    claim_id: RSK-0002-C05
    evidence:
      - source: SRC-0031
        locator: "Part I §§3.1.3–3.1.7 and 4.1–4.8, printed pp. 3–12 (physical pp. 8–17); Annex III §§1–3, printed pp. 27–30 (physical pp. 32–35)"
tags:
  - biomanufacturing
  - process-control
  - product-quality
  - supply-continuity
  - hypothetical
---

# Disruption of integrity or availability in biomanufacturing process control

> [!WARNING]
> **Evidence classification**
> This is a **hypothetical, multi-lineage conceptual/normative scenario**.
> Guttieres, NIST, and Q13 establish dependencies, possible cyber/OT states,
> and quality gates, but no source documents an observed end-to-end attack,
> current exploitability, or safeguard failure. Operational attack detail is
> excluded.

## Scenario

Cyber event causes loss of integrity or availability in a digital
process-control or process/quality-data dependency. If the affected dependency
can change physical process execution or obscure reliable assessment, the
receiving manufacturing state may deviate or become unverifiable. If validation
and containment controls do not detect/stop the issue, possible consequences
include equipment/product loss, batch failure, quality uncertainty, production
interruption or downstream supply/patient impact.

## Assets and workflow

- [SYS-0002](../systems/sys-0002-biomanufacturing-process-control.md) — origin
  system class;
- process measurements, control logic, supervisory data and quality evidence;
- biological intermediates/product and manufacturing equipment;
- [WFL-0003](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
  — affected material/data/control/decision flow;
- operators, quality personnel, providers and patients as conditional
  stakeholders.

## Preconditions and trust boundaries

The path requires:

1. a material dependency between digital state/data and physical process or
   quality decision;
2. loss of integrity/availability that is not safely isolated at its origin;
3. insufficient independent verification, process validation, release or
   recovery controls to prevent downstream propagation;
4. continued use, release or prolonged outage sufficient to create product or
   supply consequence.

`SRC-0003` does not establish access route, exploitable vulnerability, actor,
specific facility configuration or prevalence of these preconditions.

## Origin-domain state

Origin state is unavailable, unreliable or unauthorized digital control/data.
Trigger and intent are unknown; the source discusses cyberattack risk generally
but does not validate a technique-specific path.

## Cross-domain transfer

Two transfer mechanisms are modeled at defensive level:

- **control:** digital logic/command changes or interrupts physical process;
- **data/decision:** unreliable process or quality data affects monitoring,
  investigation, release or recovery decisions.

Q13 makes the quality-gate chain explicit without asserting cyber origin:

`untrusted/unavailable control, model or data state → incorrect/missing
adjustment or detection → changed/non-conforming/unverifiable material →
failure or delay of pause/diversion/hold/test/disposition gate → conditional
product-quality or supply consequence`.

The counter-flow dependency is equally material:

`input/material/process/equipment condition → sensor/PAT/test/model data →
digital control or quality decision → adjust, continue, pause, divert,
investigate or release`.

This counter-flow is a dependency within the scenario, not a separate observed
biological-input cyber incident.

> **Claim record — RSK-0002-C01 | analytic-judgment**
> **Claim:** Figure 1 and consequence discussion in `SRC-0003` support a
> structurally plausible cyber→physical/biological path through process-control
> integrity/availability, but not observed exploitation, likelihood or a named
> facility case.
> **Claim status:** active
> **Scope:** Biopharmaceutical process with a material digital-control or
> process-data dependency.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Figure 1; § Digital Information Flow in Biomanufacturing; § Known
> Cybersecurity Risks Point to Vulnerabilities in Biomanufacturing, paragraphs
> after the Merck case.
> **Basis / limits:** Source explicitly links control/data compromise to possible
> process, equipment, product-quality and supply outcomes. It is a Perspective,
> and no end-to-end test, incident evidence or control-failure validation is
> supplied.

## Receiving-domain state

Receiving state may be a changed, interrupted or uncertain physical process; a
biological intermediate/product whose quality status is uncertain; or a
production state that cannot continue until trustworthy data/control is
restored. A cyber event alone is insufficient: cross-domain consequence depends
on the physical/decision coupling and independent safeguards.

## Immediate and downstream consequences

> **Claim record — RSK-0002-C02 | source-report**
> **Claim:** Guttieres et al. identify potential consequences including
> occupational hazard, equipment damage, batch/product loss,
> requalification/revalidation burden, supply interruption and possible patient
> harm. The source also identifies IP theft separately, but that confidentiality
> consequence is outside the modeled integrity/availability path.
> **Claim status:** active
> **Scope:** Author-listed consequence classes, not one observed complete chain.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> § Known Cybersecurity Risks Point to Vulnerabilities in Biomanufacturing, two
> paragraphs after boxed Merck case.
> **Basis / limits:** The list is explicit, but likelihood, magnitude,
> reversibility and dependence on product/process context are not evaluated.

> **Claim record — RSK-0002-C03 | analytic-judgment**
> **Claim:** Loss of trusted control or process/quality data can interrupt or
> invalidate a segment of `WFL-0003`; propagation beyond that segment is
> conditional on detection, validation, disposition and recovery decisions.
> **Claim status:** active
> **Scope:** Conditional effect on the conceptual digital thread.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Figure 1; §§ Digital Information Flow in Biomanufacturing, Known Cybersecurity
> Risks Point to Vulnerabilities in Biomanufacturing.
> **Basis / limits:** Source supports process/control coupling and potential
> interruption/quality effects, but not a specific propagation duration or
> release failure. Typed `affects` edge is therefore conditional.

## Evidence

The Merck/NotPetya mention in `SRC-0003` is secondary and does not show that a
process-control integrity path caused the reported effects. The subsequently
ingested primary/adjudicative package in [INC-0006](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md)
and [RSK-0019](rsk-0019-merck-cyber-manufacturing-supply-disruption.md)
supports a separate observed network-attack→manufacturing/order/supply path;
it still does not corroborate this page's hypothetical integrity/quality path.

## Controls by function

Two complementary control pages now map the exact edges:

- [CTL-0011](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
  supplies generic OT asset/access/integrity monitoring, response and trusted
  digital restoration;
- [CTL-0015](../controls/ctl-0015-continuous-manufacturing-quality-control.md)
  supplies Q13 material/process monitoring, quality gates, diversion,
  disposition, release and validation.

Prevent/detect must preserve the material↔signal/model association;
contain/respond must synchronize digital isolation with physical hold/diversion;
recover must validate both digital state and product/process disposition;
assurance requires scoped test results rather than guidance or crosswalks.
Neither family reports implementation/testing/effectiveness here.

> **Claim record — RSK-0002-C04 | analytic-judgment**
> **Claim:** NIST independently strengthens the plausibility of generic OT
> control/process dependencies and potential product/continuity consequences
> and supplies mapped controls, but does not corroborate an observed
> biomanufacturing path or the missing GMP/quality-release gates.
> **Claim status:** superseded
> **Scope:** Generic pharmaceutical/biomanufacturing OT branch of this
> hypothetical scenario.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Digital Information Flow and Figure 1;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §2.3.3, printed pp. 19–21 (PDF pp. 36–38); §§3.2–3.2.1 and
> 4.1.1–4.1.2, printed pp. 34–35, 46–52 (PDF pp. 51–52, 63–69).
> **Basis / limits:** NIST's generic dependencies/consequences are direct and
> independent; applying them to this sector path is editorial. No primary
> event, release decision or affected product is established. Historical
> after-`SRC-0018` assessment; Q13 now supplies normative quality/release gates,
> and `RSK-0002-C05/C06` state the current boundary.
> **Superseded by:** `RSK-0002-C05/C06`.

> **Claim record — RSK-0002-C05 | analytic-judgment**
> **Claim:** Q13 independently establishes that control/model/data gaps and
> process disturbances can affect adjustment, diversion, investigation and
> release decisions, completing both functional directions of the hypothetical
> path without establishing cyberattack or observed consequence.
> **Claim status:** active
> **Scope:** Q13 continuous-manufacturing quality dependency joined to the
> existing generic cyber/OT scenario; not a named event, product or facility.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Figure 1 and §§Digital Information Flow in Biomanufacturing/Known
> Cybersecurity Risks; [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.3, 3.2 and 4.1; [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1.1–3.1.7 and 4.1–4.9, printed pp. 2–12
> (physical pp. 7–17); Annex III §§2–3, printed pp. 28–30
> (physical pp. 33–35); Annex V §§1–3.3, printed pp. 37–41
> (physical pp. 42–46).
> **Basis / limits:** Cyber/OT dependency, quality decision edges and transfer
> directions are direct across independent lineages. The attack-origin stitch
> remains hypothetical and no outcome is observed.

> **Claim record — RSK-0002-C06 | analytic-judgment**
> **Claim:** The current control interruption model requires both generic OT
> access/integrity/monitoring/trusted restoration and Q13-specific
> monitoring/diversion/disposition/release gates; either layer alone leaves a
> material residual path.
> **Claim status:** active
> **Scope:** Exact-edge control architecture for this hypothetical scenario;
> not implementation, compliance or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§5.2.3, 5.4 and 6.1–6.5, printed pp. 71–75, 83–138;
> [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
> §§3.1.1–3.1.7 and 4.1–4.9, printed pp. 2–12
> (physical pp. 7–17); [CTL-0011-C02](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
> and [CTL-0015-C02](../controls/ctl-0015-continuous-manufacturing-quality-control.md)–`C04`.
> **Basis / limits:** Each source supplies a different direct layer; the
> conjunction is editorial. Wiki claim links are navigation only, and the
> underlying source locators remain the evidence.

## Assumptions and uncertainty

- Likelihood: not assessed.
- Consequence: conditional and product/process-specific.
- Actor, technique, access, vulnerability and attribution: unknown.
- Existing independent safety/quality systems: not inventoried.
- Current technology/adoption status: not established by a 2019 Perspective.
- Counterevidence: validation, segregation, manual/independent safeguards or
  timely detection may stop propagation; source does not evaluate them.

## Related scenarios

`RSK-0002` differs from
[RSK-0001](rsk-0001-hcl-containment-control-disruption.md):
the former concerns product/process quality and supply in biomanufacturing;
the latter concerns containment-support safety in HCL. They can share OT
control principles without being treated as the same scenario.

## Related pages

- [SYS-0002 — Biomanufacturing process-control stack](../systems/sys-0002-biomanufacturing-process-control.md)
- [WFL-0003 — Biopharmaceutical manufacturing information and control flows](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
- [SRC-0003 — Guttieres et al. 2019](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [SRC-0018 — NIST SP 800-82r3](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0031 — ICH Q13](../sources/src-0031-ich-q13-continuous-manufacturing.md)
- [AST-0007 — biomanufacturing assets/stakeholders](../assets/ast-0007-biomanufacturing-assets-stakeholders.md)
- [GOV-0016 — Q13 governance/adoption](../governance/gov-0016-ich-q13-continuous-manufacturing.md)
- [CTL-0011 — OT defense-in-depth and resilience](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [CTL-0015 — continuous-manufacturing quality controls](../controls/ctl-0015-continuous-manufacturing-quality-control.md)
- [SYN-0007 — OT applicability synthesis](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)
- [SYN-0016 — BMO four-cell reconciliation](../syntheses/syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)
- [VUL-0003 — BMO exposure classes](../vulnerabilities/vul-0003-biomanufacturing-data-integrity-ot-access-dependencies.md)
- [INC-0006 — observed Merck event](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md)
- [RSK-0019 — observed supply path, distinct from this hypothetical quality path](rsk-0019-merck-cyber-manufacturing-supply-disruption.md)
- [CTL-0020 — incident control lessons](../controls/ctl-0020-merck-incident-vendor-update-continuity-recovery-lessons.md)
- [SYN-0028 — BMO residual reconciliation](../syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)

## Sources

- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md), Figure 1;
  §§ Digital Information Flow in Biomanufacturing, Known Cybersecurity Risks
  Point to Vulnerabilities in Biomanufacturing.
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
  §§2.3.3, 3.2 and 4.1.
- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
  §§3.1–4.9; Annex III §§2–3; Annex V.
