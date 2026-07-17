---
id: TEC-0003
type: technique
title: Ransomware availability denial and extortion in agriculture contexts
aliases:
  - agriculture ransomware method class
  - production dependency availability-denial technique
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0038
sensitivity: public
dual_use: low
technique_kind: defensive-high-level-ransomware-availability-and-extortion-class
relations:
  - predicate: evidenced-by
    target: SRC-0038
    claim_id: TEC-0003-C01
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C03–C07; FBI notification pp. 1–2"
  - predicate: exploits
    target: VUL-0002
    claim_id: TEC-0003-C02
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C04; FBI notification p. 2, first paragraph under Threat"
  - predicate: enables
    target: RSK-0017
    claim_id: TEC-0003-C02
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C03–C07; FBI notification pp. 1–2"
tags:
  - agriculture
  - technique
  - ransomware
  - availability
  - extortion
  - production-continuity
  - defensive-taxonomy
---

# Ransomware availability denial and extortion in agriculture contexts

## Method class

This page isolates the high-level method from the actor and event. The method
uses malicious software to deny access to digital systems or information and
create extortion pressure. In agriculture, consequence depends on whether the
affected digital function is coupled to time-sensitive production, processing
or supply work.

> **Claim record — TEC-0003-C01 | source-report**
> **Claim:** The FBI agriculture advisory reports ransomware as a method that
> can make cooperative administrative or production functions unavailable and
> create extortion pressure during time-sensitive planting or harvest periods.
> **Claim status:** active
> **Scope:** High-level method and agriculture dependency context; not actor
> identity, intrusion route, encryption procedure, payment guidance,
> likelihood or a biological outcome.
> **As of:** Cases since 2021, advisory issued 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md),
> `SRC-0038-C03`–`C07`; FBI notification pp. 1–2.
> **Basis / limits:** Method, timing context and mixed administrative/
> production effects are direct aggregate reporting. Anonymous cases are one
> FBI lineage and not multiplied into independently confirmed incidents.

## Preconditions and consequence boundary

> **Claim record — TEC-0003-C02 | analytic-judgment**
> **Claim:** `TEC-0003` can exploit the high-level access/shared-service
> exposures in `VUL-0002` and enable `RSK-0017` only when reach, dependency
> criticality and failed containment or recovery coincide; ransomware presence
> does not guarantee production, supply or biological consequence.
> **Claim status:** active
> **Scope:** Defensive exact-edge model without access, execution, lateral-
> movement, encryption, evasion or payment instructions.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `TEC-0003-C01`;
> [VUL-0002](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md);
> [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md).
> **Basis / limits:** The source supplies exposure and mixed-outcome classes;
> the conditional graph keeps method, weakness and consequence separate.

## Ontology distinction

> **Claim record — TEC-0003-C03 | analytic-judgment**
> **Claim:** `THR-0002` records the intentional criminal actor/threat class,
> `TEC-0003` the availability/extortion method, `VUL-0002` the enabling
> weakness/dependency state and `HAZ-0003/0004` independent non-adversarial
> triggers; none of these labels creates a documented incident.
> **Claim status:** active
> **Scope:** Canonical AGE taxonomy and typed-graph semantics.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md);
> [VUL-0002](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md);
> [HAZ-0003](../hazards/haz-0003-agriculture-sensor-and-data-quality-failure.md);
> [HAZ-0004](../hazards/haz-0004-agriculture-climate-pest-disease-and-supply-hazards.md);
> `SRC-0038-C03/C04` and independent AU/Drape hazard roles.
> **Basis / limits:** Source roles and canonical distinctions are explicit.
> Threat/hazard pages are not event records and generic technique evidence is
> not prevalence.

## Safety boundary

No access method, executable behavior, encryption procedure, persistence,
evasion, target selection, payment route or operational configuration is
included.

## Related pages

- [THR-0002 — Agriculture ransomware threat](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md)
- [VUL-0002 — Agriculture exposures](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md)
- [HAZ-0003 — Sensor/data-quality hazard](../hazards/haz-0003-agriculture-sensor-and-data-quality-failure.md)
- [HAZ-0004 — Ecological/supply hazards](../hazards/haz-0004-agriculture-climate-pest-disease-and-supply-hazards.md)
- [RSK-0017 — Agriculture disruption path](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [CTL-0018 — Agriculture resilience controls](../controls/ctl-0018-agriculture-cyber-resilience-and-recovery-controls.md)
- [SRC-0038 — FBI agriculture advisory](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md)
- [SYN-0029 — Cross-sector taxonomy audit](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)

## Sources

- [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md), exact locators above.
