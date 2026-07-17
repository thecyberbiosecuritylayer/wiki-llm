---
id: RSK-0017
type: risk-scenario
title: Agriculture cyber disruption propagating into production and supply
aliases:
  - agricultural cooperative ransomware production cascade
  - cyber to agriculture production and supply path
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0038
sensitivity: public
dual_use: low
origin_domain: cyber
destination_domains:
  - agriculture-production
  - food-and-feed-supply
relations:
  - predicate: evidenced-by
    target: SRC-0038
    claim_id: RSK-0017-C01
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C03–C07; PDF pp. 1–2"
  - predicate: depends-on
    target: WFL-0007
    claim_id: RSK-0017-C01
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C05–C07; PDF pp. 1–2, production, seed, fertilizer, logistics and supply dependencies"
  - predicate: affects
    target: AST-0003
    claim_id: RSK-0017-C02
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C05/C06; PDF pp. 1–2"
tags:
  - agriculture
  - ransomware
  - cross-domain
  - production-continuity
  - manual-operations
  - supply-chain
---

# Agriculture cyber disruption propagating into production and supply

## Scenario

A criminal ransomware action reaches an exposed agriculture-sector digital or
shared-service dependency. Loss of system or information availability then
affects administrative work, processing, production support or logistics. If
the affected dependency is production-critical and continuity is insufficient,
work becomes slower/manual or stops. During planting or harvest, disruption
can pressure seed, fertilizer, grain/feed, processing and logistics functions;
broader food/feed, spoilage or farm consequences require additional conditions.

The scenario deliberately separates **observed operational limbs** from
**prospective downstream cascades**.

> **Claim record — RSK-0017-C01 | analytic-judgment**
> **Claim:** `SRC-0038` supports a bounded ransomware→digital unavailability→
> administrative loss or slower/manual production or halt→agriculture supply-
> dependency path, with planting/harvest timing as context rather than proof of
> intent or inevitability.
> **Claim status:** active
> **Scope:** High-level cyber→agriculture production/supply scenario; no
> intrusion procedure, entity reconstruction, likelihood or biological harm.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md),
> `SRC-0038-C03`–`C07`; PDF pp. 1–2;
> [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md).
> **Basis / limits:** Threat, availability outcomes and dependencies are direct;
> the canonical joined path is wiki synthesis. One advisory lineage does not
> satisfy the independent SF2 floor.

## Assets and workflow

The represented assets are deliberately broader than farm sensors: cooperative
administrative systems, processing functions, grain/feed operations, seed and
fertilizer services, logistics and the information/services needed to
coordinate them. These are a bounded extension of `AST-0003/WFL-0007`; the
source does not provide a plant-floor or network topology.

## Preconditions and trust boundaries

The path requires:

- an applicable exposed digital, shared-network or managed-service dependency;
- malicious reach into a service needed by an agricultural entity;
- insufficient prevention, segmentation, detection or containment;
- a dependency whose unavailability affects production or supply rather than
  administration only; and
- insufficient safe manual continuity or timely trusted recovery.

Managed-service and shared-resource reliance create organization-to-provider
or common-service trust boundaries. Exact architecture remains unknown.

## Origin-domain state

The source-reported origin state is criminal ransomware activity or attempted
activity against digital systems. Two attempts were detected and stopped
before encryption, demonstrating that malicious access does not automatically
produce the downstream state.

## Cross-domain transfer

The transfer variable is **availability of a digital function that production
or supply activity depends on**. Loss of administrative email or a website can
remain inside the cyber/business domain. Loss of a production-relevant service
can force manual work, slow processing or halt production.

> **Claim record — RSK-0017-C02 | source-report**
> **Claim:** The advisory directly reports mixed transfer outcomes: stopped
> attempts, administrative-only loss without production impact, slower manual
> processing and complete production halt.
> **Claim status:** active
> **Scope:** Aggregated source-reported states, not outcome frequency, duration,
> entity-level mapping or independent case confirmation.
> **As of:** Events in 2021–March 2022.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0038-C05/C06`; PDF p. 2.
> **Basis / limits:** The distinct outcome states are direct. Anonymous cases
> and absent denominators prohibit prevalence or probability inference.

## Receiving-domain state

The demonstrated receiving state is agriculture operational disruption:
manual/slower processing or production halt. The source also identifies seed,
fertilizer, grain/feed and logistics as time-sensitive dependencies, but does
not show which specific physical processes or inventories were affected in
each case.

## Immediate and downstream consequences

Immediate observed represented consequences are service unavailability,
administrative loss, slower manual work and production halt. The advisory
presents financial loss, food/feed/trading pressure and processor-spoilage/farm
effects as potential or possible consequences, not observed case outcomes.

> **Claim record — RSK-0017-C03 | source-report**
> **Claim:** `RSK-0017` has an observed cyber→operational-disruption limb, but
> its food/feed, spoilage, farm, animal, plant and ecosystem consequence limbs
> remain prospective or unsupported in this source.
> **Claim status:** active
> **Scope:** Consequence maturity for the represented advisory cases; not a
> statement that broader consequences are impossible.
> **As of:** 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0038-C05/C07`; PDF p. 2.
> **Basis / limits:** Source modal language and observed-outcome language are
> kept separate. No biological injury or ecological outcome is reported.

## Evidence maturity

| Path limb | State | Boundary |
| --- | --- | --- |
| Ransomware attempt/activity | Source-reported | One FBI advisory lineage; no entity-level primary record |
| Administrative unavailability | Source-reported observed | No duration or independent validation |
| Manual/slower production | Source-reported observed | Aggregated, no quantified output loss |
| Production halt | Source-reported observed | Aggregated, no duration or causal case record |
| Seed/fertilizer/logistics dependency | Direct context | Not proof each service was disrupted |
| Food/feed/trading cascade | Prospective | No observed outcome in cases |
| Spoilage/farm pressure | Prospective | No observed outcome in cases |
| Animal/plant/ecosystem harm | Unsupported | Not reported |

> **Claim record — RSK-0017-C04 | analytic-judgment**
> **Claim:** The source supplies the first retained concrete agriculture-
> specific hostile cyber→production-availability path, but independent
> corroboration and a complete observed biological/ecosystem limb remain
> absent; `AGE-XT` therefore stays Partial after this transaction.
> **Claim status:** superseded
> **Scope:** Candidate contribution to frozen `AGE-XT`; no score transition.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `RSK-0017-C01`–`C03`; frozen rubric in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Hostile direction and operational consequence are direct
> enough for candidate evidence, but one lineage cannot meet SF2 and no
> animal/plant/ecosystem effect is observed.
> **Superseded by:** `SYN-0025-C05`, which adds independent operational context
> but keeps `AGE-XT` Partial because animal/plant/ecosystem effect is absent.

## Controls by function

- **Reduce exposure:** maintenance, access and segmentation safeguards.
- **Detect/contain:** monitoring, awareness, escalation and containment.
- **Continue safely:** critical-function analysis and locally validated manual
  operation where safe.
- **Recover:** protected separated backups and a recovery plan with verified
  restoration criteria supplied locally.
- **Report:** external reporting through the source-described channel.

Only recommendation status is evidenced here. See `CTL-0018`.

## Assumptions and uncertainty

- A targeted or compromised entity need not suffer production impact.
- Manual operation may preserve continuity but can be slower and may introduce
  safety, quality or traceability risks not evaluated by this source.
- Seasonal timing may reflect opportunity or reporting selection; intent is
  not established.
- Anonymous case aggregation prevents incident-count independence.
- No claim is made about current ransomware prevalence or current exposure.

## Safety boundary

The page excludes malicious-software names, indicators, exploit identifiers,
affected-entity identity and operational intrusion detail.

## Related scenarios

- [TEC-0003 — Agriculture ransomware method](../techniques/tec-0003-ransomware-availability-and-extortion-agriculture.md)
- [RSK-0007](rsk-0007-farm-data-access-production-supply-disruption.md)
- [RSK-0002](rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md)
- [VUL-0002](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md)
- [CTL-0018](../controls/ctl-0018-agriculture-cyber-resilience-and-recovery-controls.md)

## Sources

- [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md),
  PDF pp. 1–4.
