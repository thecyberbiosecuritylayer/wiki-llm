---
id: RSK-0001
type: risk-scenario
title: Disruption of digitally supported containment functions in HCLs
aliases:
  - HCL containment-control disruption
  - cyber-to-safety path in high-containment laboratories
status: active
created: 2026-07-11
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0002
  - SRC-0004
  - SRC-0018
sensitivity: public
dual_use: moderate
origin_domain: cyber
destination_domains:
  - physical
  - biological
relations:
  - predicate: evidenced-by
    target: SRC-0002
    claim_id: RSK-0001-C01
    evidence:
      - source: SRC-0002
        locator: "Table 1, Worker Safety and Public Health rows; §§ Pathogen research, Worker safety, Public health"
  - predicate: depends-on
    target: SYS-0001
    claim_id: RSK-0001-C01
    evidence:
      - source: SRC-0002
        locator: "§ Pathogen research, first two paragraphs"
  - predicate: affects
    target: WFL-0002
    claim_id: RSK-0001-C03
    evidence:
      - source: SRC-0002
        locator: "Table 1, Worker Safety and Public Health rows; § Identified Areas of Impact"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: RSK-0001-C04
    evidence:
      - source: SRC-0002
        locator: "§ Pathogen research; Table 1, Worker Safety and Public Health rows"
      - source: SRC-0004
        locator: "§5.3.4, printed pp. 21–22 (PDF pp. 41–42); §§6.5–6.6, printed pp. 34–39 (PDF pp. 54–59)"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: RSK-0001-C05
    evidence:
      - source: SRC-0002
        locator: "§ Pathogen research; Table 1, Worker Safety and Public Health rows"
      - source: SRC-0018
        locator: "§§2.3.5–2.3.7, 4.2.2 and 5.3.1–5.3.2, printed pp. 22–26, 55, 79–80 (PDF pp. 39–43, 72, 96–97); §§6.3–6.5"
tags:
  - laboratories
  - high-containment
  - cyber-to-biological
  - safety
  - hypothetical
---

# Disruption of digitally supported containment functions in HCLs

> [!WARNING]
> **Evidence classification**
> This is a **hypothetical scenario with a single scenario-evidence lineage**,
> built from qualitative asset-impact analysis. Separate WHO control guidance
> does not corroborate the attack path. The scenario is not a documented HCL
> incident, contains no actor attribution, and does not establish likelihood.

## Scenario

A cyber event changes the integrity or availability of a digitally supported
containment or safety function. If that digital-to-physical dependency actually
exists and independent safeguards do not maintain a safe state, physical
protection may degrade. In the presence of hazardous biological material, this
could create conditions for worker exposure, contamination, or release;
downstream public-health consequences depend on the material, detection,
response, and actual containment.

The description intentionally omits operational settings, access routes,
exploit sequences, and facility-specific layouts.

## Assets and workflow

- [SYS-0001](../systems/sys-0001-hcl-containment-support-systems.md) — the origin
  asset class, in which a digital state can have a physical effect;
- biological materials and laboratory workers — receiving-domain assets and
  stakeholders;
- [WFL-0002](../workflows/wfl-0002-high-containment-laboratory.md) — pathogen
  research or other work that depends on containment-support functions; and
- operational continuity and public health — possible downstream interests.

## Preconditions and trust boundaries

The scenario requires several conditions to hold simultaneously:

1. the relevant safety or containment function actually has a digital control
   or monitoring dependency;
2. loss of integrity or availability in that dependency can change physical
   state, rather than visibility alone;
3. biological work or material is in a state where degradation has safety
   significance; and
4. independent engineered, procedural, or human safeguards do not prevent the
   change or contain it before it produces a consequence.

These conditions are an analytical decomposition. `SRC-0002` provides no
network architecture, privileges, access paths, fail-safe design, or evidence
that every condition occurs in a single HCL.

## Origin-domain state

The initial state is loss of integrity or availability in a digitally supported
facility or containment function. Trigger and intent are not established; the
source primarily models a generic cyber incident or attack and does not support
a separate non-adversarial hazard or an actor-, technique-, or
vulnerability-specific claim.

## Cross-domain transfer

The transfer mechanism is **control/state**: a digital command, configuration,
or service state affects a physical safety-support function. This structurally
distinguishes the scenario from a generic IT outage. Mere connectivity without
a physical effect does not satisfy the inclusion rule.

> **Claim record — RSK-0001-C01 | analytic-judgment**
> **Claim:** `SRC-0002` supports a structurally plausible
> cyber→physical→biological/safety path through the integrity or availability
> of a digitally supported containment function, but does not confirm an
> observed HCL incident or a specific exploit path.
> **Claim status:** active
> **Scope:** An HCL with an actual digital-to-physical containment dependency.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Pathogen research, first two paragraphs; Table 1, Worker Safety and Public
> Health rows; §§ Worker safety, Public health.
> **Basis / limits:** The source's asset-impact analysis directly links the
> system class to potential safety outcomes. Confidence is limited by the
> qualitative design, absence of primary incident or engineering validation,
> and unknown independent safeguards.

## Receiving-domain state

The receiving state is a degraded physical containment or safety-support
condition. A biological consequence is not automatic: it requires further
interaction with the material and workflow, together with inadequate
safeguards. The wiki does not equate system compromise with exposure or release
without this intermediate state.

## Immediate and downstream consequences

Potential immediate consequences include degradation of a safety-support
function, laboratory downtime, or interruption of relevant work. Potential
biological and public-health consequences—exposure, contamination, or
release—remain conditional rather than observed. Their scale and reversibility
depend on the specific facility and response.

> **Claim record — RSK-0001-C02 | source-report**
> **Claim:** Table 1 and the impact sections of Crawford et al. associate
> compromise of containment-support building automation with potential worker
> exposure and community or public-health consequences.
> **Claim status:** active
> **Scope:** A modeled potential loss in a qualitative HCL analysis.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> Table 1, Worker Safety row `Exposure of laboratory personnel…` and Public
> Health row `Community spread…`; §§ Worker safety, Public health.
> **Basis / limits:** The high confidence applies to the authors' mapping. The
> rows are potential forms of loss, not incident observations, quantified
> likelihood, or evidence of a complete attack chain.

> **Claim record — RSK-0001-C03 | analytic-judgment**
> **Claim:** If an HCL workflow actually depends on a digitally supported
> containment function, loss of that function's integrity or availability may
> interrupt pathogen-research operations or cause laboratory downtime; the
> extent and recovery path remain facility-specific.
> **Claim status:** active
> **Scope:** A conditional effect on
> [WFL-0002](../workflows/wfl-0002-high-containment-laboratory.md) in a configuration
> with a confirmed dependency.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Pathogen research; § Public health, paragraph on disruption of the
> diagnostic workflow; Table 1, Worker Safety and Public Health rows.
> **Basis / limits:** The source supports the possibility of downtime and
> containment-related impact, but does not measure the dependency, downtime
> duration, or recovery for a specific HCL. The typed `affects` edge is a
> conditional inference.

## Evidence

The evidence base is a single peer-reviewed qualitative analysis. The article's
Oxford example shows compromise of a cyber-physical system in an adjacent
laboratory based on secondary reporting, but the authors explicitly state that
it was not an HCL; it is therefore not used as incident corroboration. The other
historical examples likewise do not establish this containment path.

No `INC`, `THR`, `TEC`, or `VUL` page has been created from this scenario.
Direct WHO guidance now supports the recommended control scope but not the path
itself. Raising the scenario's evidence status would require independent
engineering records or primary incident or near-miss evidence.

## Controls by function

[CTL-0001](../controls/ctl-0001-risk-based-laboratory-information-cybersecurity.md)
maps WHO-recommended information and cyber functions to this scenario at a high
level:

- **prevent/detect:** inventory relevant dependencies, govern authorized access,
  protect information and systems, and monitor and report suspected events;
- **contain/respond:** use locally validated escalation coordinated with
  biological safety, facilities, and leadership;
- **recover:** restore trustworthy digital service together with verification
  of physical state and disposition of materials and workflows; and
- **assure:** audit, test, exercise, investigate, track corrective actions, and
  reassess after change.

`CTL-0001` is **recommended only**. Implementation, testing, effectiveness, and
independent evaluation are unknown; generic response or backup actions are not
treated as universally applicable to a containment-support edge without local
engineering validation and a safety and security tradeoff assessment.

> **Claim record — RSK-0001-C04 | analytic-judgment**
> **Claim:** WHO 2024 provides recommended controls relevant to the origin and
> transfer conditions of `RSK-0001`, but does not validate this HCL scenario or
> demonstrate exact-edge implementation, testing, or effectiveness.
> **Claim status:** active
> **Scope:** Control mapping to a hypothetical HCL containment-support scenario.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Pathogen research; Table 1, Worker Safety and Public Health rows;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §5.3.4, printed pp. 21–22; §§6.5–6.6, printed pp. 34–39;
> Annex 1, printed pp. 71–77.
> **Basis / limits:** `SRC-0002` defines the potential dependency and
> consequence; `SRC-0004` defines broad recommended control and assurance
> functions. WHO cites Crawford for cyberattack context and reports no facility
> evaluation, so scenario confidence and likelihood do not increase.

> **Claim record — RSK-0001-C05 | analytic-judgment**
> **Claim:** Generic NIST guidance for BAS, PACS, safety, monitoring, incident
> response, and recovery conditionally maps to the digitally supported edges of
> `RSK-0001` but does not validate the HCL scenario, the biological safe state,
> or facility implementation.
> **Claim status:** active
> **Scope:** Generic OT control applicability to an independently supported HCL
> dependency; no incident, topology, or control result.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Pathogen research and Table 1;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.5–2.3.7, 4.2.2, 5.3.1–5.3.2 and 6.3–6.5,
> printed pp. 22–26, 55, 79–80, 126–138.
> **Basis / limits:** The dependency and generic control functions are direct;
> exact-edge mapping is editorial. Implementation, testing, and effectiveness
> are unknown.

## Assumptions and uncertainty

- Likelihood: **not assessed**.
- Consequence: conditional and facility-specific; no numerical rating.
- Exposure and connectivity: unknown for any named facility.
- Actor, technique, vulnerability, and attribution: unknown or not modeled.
- Counterevidence: independent safeguards could break the path; the source does
  not inventory them.
- External validity: human-pathogen HCLs without live-animal work; not
  automatically generalizable to animal or agricultural containment.

## Related scenarios

Diagnostic integrity and availability and sample-inventory scenarios remain
candidates in `SRC-0002`; they require separate primary workflow or incident
evidence before a priority `RSK` page is created.

## Related pages

- [SYN-0023 — Laboratory transfer reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [SYS-0001 — Containment-support cyberphysical systems](../systems/sys-0001-hcl-containment-support-systems.md)
- [WFL-0002 — HCL cyber-physical workflow](../workflows/wfl-0002-high-containment-laboratory.md)
- [CTL-0001 — Risk-based laboratory information and cybersecurity controls](../controls/ctl-0001-risk-based-laboratory-information-cybersecurity.md)
- [GOV-0001 — WHO Laboratory Biosecurity Guidance 2024](../governance/gov-0001-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0002 — Crawford et al. 2023](../sources/src-0002-crawford-high-containment-laboratories-2023.md)
- [SRC-0004 — WHO Laboratory Biosecurity Guidance 2024](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0018 — NIST SP 800-82r3](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [CTL-0011 — OT defense-in-depth and resilience](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [SYN-0007 — OT applicability synthesis](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)

## Sources

- [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
  Table 1; §§ Pathogen research, Worker safety, Public health.
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
  §§5.3.4, 6.5–6.6; Annex 1.
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
  §§2.3.5–2.3.7, 4.2.2, 5.3, and 6.3–6.5.
