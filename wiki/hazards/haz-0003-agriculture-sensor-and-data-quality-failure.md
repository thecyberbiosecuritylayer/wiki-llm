---
id: HAZ-0003
type: hazard
title: Non-adversarial agriculture sensor and data-quality failure
aliases:
  - accidental smart-farm data failure
  - erroneous agriculture sensor data hazard
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0010
  - SRC-0032
sensitivity: public
dual_use: low
hazard_kind: accidental-sensor-data-quality-and-decision-failure
relations:
  - predicate: evidenced-by
    target: SRC-0010
    claim_id: HAZ-0003-C01
    evidence:
      - source: SRC-0010
        locator: "SRC-0010-C05; HTML #s1-1 and #s1-4, lines 1475 and 1478"
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: HAZ-0003-C02
    evidence:
      - source: SRC-0032
        locator: "SRC-0032-C06/C07; printed pp. 19–20, 23–24 and 82–99"
  - predicate: affects
    target: AST-0003
    claim_id: HAZ-0003-C03
    evidence:
      - source: SRC-0010
        locator: "SRC-0010-C04/C05; connected monitoring, equipment, production and supply classes"
      - source: SRC-0032
        locator: "SRC-0032-C03/C06/C07; sensor/model/production assets and poor-decision risks"
  - predicate: enables
    target: RSK-0007
    claim_id: HAZ-0003-C03
    evidence:
      - source: SRC-0010
        locator: "SRC-0010-C05; false sensor/data state to production/supply potential"
      - source: SRC-0032
        locator: "SRC-0032-C06/C07; input→analytics→decision/action and erroneous-data risk"
tags:
  - agriculture
  - hazard
  - non-adversarial
  - sensors
  - data-quality
  - decision-integrity
---

# Non-adversarial agriculture sensor and data-quality failure

## Hazard class

This class covers accidental or non-adversarial sensor, human-entry, metadata,
storage, transformation or update failures that make agriculture data
incomplete, outdated, erroneous or unfit for a decision. It is distinct from
criminal ransomware, intentional manipulation and a verified product defect.

> **Claim record — HAZ-0003-C01 | source-report**
> **Claim:** Drape et al. identify false sensor data and loss/misuse of data or
> machinery access as potential precision-agriculture risks that may disrupt
> production/harvest and downstream supply.
> **Claim status:** active
> **Scope:** Literature-derived potential classes in one article; not an
> observed accidental event, malicious act, validated vulnerability or
> quantified likelihood.
> **As of:** 2021-08-19.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> `SRC-0010-C05`; HTML `#s1-1` and `#s1-4`, lines 1475 and 1478.
> **Basis / limits:** False sensor/data state and potential path are direct
> author framing; intent and cause are not established.

> **Claim record — HAZ-0003-C02 | source-report**
> **Claim:** AU DAS identifies missing metadata, outdated or erroneous data,
> quality/interoperability problems and resulting poor decisions across sensor/
> human input, transmission, storage, analytics and action functions.
> **Claim status:** active
> **Scope:** Strategy-level data-quality hazards and functional path; not one
> incident, sensor model, error rate, validated control or outcome.
> **As of:** 2023-10.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C06/C07`; printed pp. 19–20, 23–24 and action-package risk panels
> pp. 82–99.
> **Basis / limits:** Named data states and decision risks are direct. The
> source does not assign malicious intent or publish empirical failure rates.

## Transfer and consequence boundary

The defensive path is:

`sensor/human observation → incomplete/outdated/erroneous digital state →
analytics/advisory/control decision → conditional production/resource/supply
effect`.

> **Claim record — HAZ-0003-C03 | analytic-judgment**
> **Claim:** AU directly supports a non-adversarial sensor/data-quality hazard
> linked to `AST-0003/WFL-0007`; Drape independently supports the sensor/data→
> production/supply transfer path in an adversarial hacker-exploitation context
> and does not corroborate the accidental label. Neither proves occurrence or
> biological harm.
> **Claim status:** active
> **Scope:** Canonical accidental AGE hazard class and asset/workflow mapping;
> not hostile manipulation, field prevalence or a complete consequence path.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `HAZ-0003-C01/C02`;
> [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md);
> [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md);
> [RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md).
> **Basis / limits:** AU supplies the accidental/error-state classification;
> Drape corroborates sector relevance and the transfer path only in an
> adversarial context. Neither reports an empirical accident.

## Distinctions and controls

- `THR-0002` is intentional criminal ransomware; this page is non-adversarial.
- `VUL-0002` is an exposure/dependency class; it is not a bad-data outcome.
- `HAZ-0004` covers ecological/climate/pest/disease and supply hazards.
- Validation, metadata/provenance, calibration/quality checks, human review and
  safe fallback can address edges, but represented deployment/effectiveness is
  not inferred.

Safety boundary: the page contains no device configuration, threshold,
operating parameter, exploit or target-specific weakness.

> **Claim record — HAZ-0003-C04 | analytic-judgment**
> **Claim:** The page contains no device configuration, threshold, operating
> parameter, exploit or target-specific weakness.
> **Claim status:** stale
> **Scope:** Local safety boundary.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content; no external source is applicable to this
> editorial self-audit.
> **Limits:** Retained as a historical local-content audit, not as an
> externally evidenced decision claim. The current safety boundary is the
> prose above.

## Related pages

- [SYN-0025](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)
- [HAZ-0004](haz-0004-agriculture-climate-pest-disease-and-supply-hazards.md)
- [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md)
- [VUL-0002](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md)
- [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)

## Sources

- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
