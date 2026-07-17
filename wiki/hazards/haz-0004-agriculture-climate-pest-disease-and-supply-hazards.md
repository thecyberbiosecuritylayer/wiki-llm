---
id: HAZ-0004
type: hazard
title: Agriculture climate, pest, disease, environmental-resource and supply hazards
aliases:
  - agriculture ecological and supply hazards
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0032
sensitivity: public
dual_use: low
hazard_kind: ecological-biological-resource-and-supply
relations:
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: HAZ-0004-C01
    evidence:
      - source: SRC-0032
        locator: "SRC-0032-C03/C04/C07; printed pp. 4–15, 19–24, 80–99 and 123–129"
  - predicate: affects
    target: AST-0003
    claim_id: HAZ-0004-C02
    evidence:
      - source: SRC-0032
        locator: "SRC-0032-C03/C07; crop/livestock/environmental/input/output/value-chain assets and named risks"
  - predicate: affects
    target: WFL-0007
    claim_id: HAZ-0004-C02
    evidence:
      - source: SRC-0032
        locator: "SRC-0032-C04/C06/C07; production/value-chain, early-warning and supply-risk functions"
tags:
  - agriculture
  - hazard
  - climate
  - pest
  - disease
  - environment
  - supply-chain
---

# Agriculture climate, pest, disease, environmental-resource and supply hazards

## Hazard classes

The AU Digital Agriculture Strategy directly identifies climate/weather,
pest/disease, environmental-resource and supply/value-chain risks around crop,
livestock, fisheries and agricultural value chains. These are ecological,
biological, physical or organizational hazards; they are not relabeled as
cyberattacks.

> **Claim record — HAZ-0004-C01 | source-report**
> **Claim:** AU DAS identifies climate/weather, pest/disease,
> over-irrigation/environmental-resource and supply/value-chain risk classes
> across agriculture production and downstream value chains.
> **Claim status:** active
> **Scope:** Strategy-level risk classes; not a named disaster/disease event,
> quantified prevalence, causal study or observed cyber consequence.
> **As of:** 2023-10.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C03/C04/C07`; printed pp. 4–15, 19–24, 80–99 and 123–129.
> **Basis / limits:** Named risks, assets and lifecycle context are direct.
> The strategy is prospective and not an incident/outcome record.

## Asset, workflow and interaction boundary

Ecological or supply hazards can affect soil/water, crops, livestock,
production inputs, equipment availability, processing/storage/transport and
market access. Digital early-warning or advisory systems may observe or help
manage them; this functional dependency does not make the originating hazard
cyber.

> **Claim record — HAZ-0004-C02 | analytic-judgment**
> **Claim:** The source links these ecological/supply hazards to `AST-0003` and
> production/value-chain stages in `WFL-0007`, while `RSK-0007` must keep
> natural/organizational origin separate from digital transfer or control
> failure.
> **Claim status:** active
> **Scope:** Defensive classification and mapping; not a universal causal chain
> or evidence that a digital control failed during a natural hazard.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `HAZ-0004-C01`; `SRC-0032-C04/C06/C07`;
> [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md);
> [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md).
> **Basis / limits:** Source functions and risks are direct; canonical hazard-
> to-workflow normalization is wiki analysis.

## Distinctions

- `HAZ-0003`: accidental sensor/data-quality state.
- `THR-0002`: intentional criminal ransomware.
- `VUL-0002`: digital exposure/dependency preconditions.
- Disease/pest early warning is a control/functional system class, not proof
  that a hazard occurred or that the control is effective.

Safety boundary: the page preserves ecological, biological, physical, supply
and cyber-origin non-equivalence and contains no pathogen, facility, route,
threshold or response-procedure detail.

> **Claim record — HAZ-0004-C03 | analytic-judgment**
> **Claim:** The page preserves ecological, biological, physical, supply and
> cyber-origin non-equivalence and contains no pathogen, facility, route,
> threshold or response-procedure detail.
> **Claim status:** stale
> **Scope:** Local classification and safety boundary.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content; no external source is applicable to this
> editorial self-audit.
> **Limits:** Retained as a historical local-content audit, not as an
> externally evidenced decision claim. The current safety boundary is the
> prose above.

## Related pages

- [SYN-0025](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)
- [CTL-0019](../controls/ctl-0019-animal-disease-traceability-performance-assurance.md)
- [HAZ-0003](haz-0003-agriculture-sensor-and-data-quality-failure.md)
- [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md)
- [VUL-0002](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md)
- [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)

## Sources

- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
