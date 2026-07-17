---
id: THR-0002
type: threat
title: Criminal ransomware against agriculture production and supply dependencies
aliases:
  - agriculture ransomware threat
  - cooperative production ransomware
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0038
sensitivity: public
dual_use: low
threat_kind: criminal-ransomware-availability-and-extortion
relations:
  - predicate: evidenced-by
    target: SRC-0038
    claim_id: THR-0002-C01
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C03/C05/C06; PDF pp. 1–2"
  - predicate: exploits
    target: VUL-0002
    claim_id: THR-0002-C02
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C04; PDF p. 2, first paragraph under Threat"
  - predicate: enables
    target: RSK-0017
    claim_id: THR-0002-C02
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C03–C07; PDF pp. 1–2"
  - predicate: enables
    target: TEC-0003
    claim_id: THR-0002-C02
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C03–C07; PDF pp. 1–2"
tags:
  - agriculture
  - ransomware
  - criminal-threat
  - availability
  - production-continuity
  - supply-chain
---

# Criminal ransomware against agriculture production and supply dependencies

## Threat class

The class covers criminal ransomware that makes agriculture-sector digital
services or information unavailable and may combine disruption with
extortion. The FBI advisory gives direct agriculture context: cooperatives can
be attractive during time-sensitive planting or harvest periods because
production and supply dependencies increase urgency.

This is a **generic threat class**, not an attribution to one actor, family,
campaign or event. Seasonal coincidence does not establish attacker intent.

> **Claim record — THR-0002-C01 | source-report**
> **Claim:** The FBI reports ransomware affecting U.S. agricultural
> cooperatives and assesses that planting/harvest timing may increase targeting
> pressure because of their time-sensitive production-and-supply role.
> **Claim status:** active
> **Scope:** Generic ransomware threat and source-reported agriculture
> context; not actor identity, exploit procedure, event likelihood or future
> frequency.
> **As of:** Events since 2021, advisory issued 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md),
> `SRC-0038-C03/C05/C06`; PDF pp. 1–2.
> **Basis / limits:** Threat and timing assessment are direct source reporting.
> The cases are one FBI advisory lineage and are not independent incident
> confirmations.

## Target assets and dependency context

Potentially affected functions include administrative services, grain/feed
processing, seed and fertilizer services, logistics and other digital
dependencies represented by `AST-0003` and `WFL-0007`.
Disruption can remain administrative, move production to slower manual work or
halt production; the source reports all three states across different cases.

> **Claim record — THR-0002-C02 | analytic-judgment**
> **Claim:** `THR-0002` can enable the high-level ransomware method in
> `TEC-0003`, and that method can enable `RSK-0017` when it reaches an exposed
> digital dependency and availability loss propagates into a critical
> production or supply function; the path is not inevitable and may be
> interrupted or remain limited to administration.
> **Claim status:** active
> **Scope:** Defensive precondition model for agriculture production and supply;
> no intrusion steps, product identifiers, likelihood or biological outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0038-C03`–`C07`; PDF pp. 1–2;
> [TEC-0003](../techniques/tec-0003-ransomware-availability-and-extortion-agriculture.md);
> [VUL-0002](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md).
> **Basis / limits:** The source directly distinguishes interrupted attempts,
> administrative-only loss and production impacts. The canonical path is a
> bounded synthesis, not a universal case reconstruction.

## Consequence boundary

Observed source outcomes stop at digital/administrative loss, slower manual
processing or production halt. Food/feed, spoilage and farm-pressure cascades
are prospective. No animal, plant, human-health or ecological injury is
reported.

> **Claim record — THR-0002-C03 | source-report**
> **Claim:** The represented threat has an observed cyber→operational-
> availability limb, while biological and broader food/feed consequences
> remain conditional rather than observed.
> **Claim status:** active
> **Scope:** Evidence-maturity boundary for `SRC-0038`; not a conclusion that
> such consequences cannot occur.
> **As of:** 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0038-C05/C07`; PDF p. 2.
> **Basis / limits:** The source grammatically separates reported operational
> outcomes from potential downstream cascades.

## Safety boundary

No malicious-software family, indicator, product weakness, exploitation
sequence, credential route or operational intrusion detail is reproduced. The
page supports recognition, dependency analysis and resilience planning.

## Related pages

- [TEC-0003 — Agriculture ransomware method](../techniques/tec-0003-ransomware-availability-and-extortion-agriculture.md)
- [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md)
- [VUL-0002](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md)
- [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [CTL-0018](../controls/ctl-0018-agriculture-cyber-resilience-and-recovery-controls.md)
- [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)

## Sources

- [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md),
  PDF pp. 1–2.
