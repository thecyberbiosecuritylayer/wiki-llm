---
id: VUL-0002
type: vulnerability
title: Agriculture IT access and shared-service dependency exposures
aliases:
  - agricultural cooperative digital exposure classes
  - agriculture shared-resource and managed-service exposure
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0038
sensitivity: public
dual_use: low
vulnerability_status: source-reported-aggregate-current-instance-status-unknown
relations:
  - predicate: evidenced-by
    target: SRC-0038
    claim_id: VUL-0002-C01
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C04; PDF p. 2, first paragraph under Threat"
  - predicate: enables
    target: RSK-0017
    claim_id: VUL-0002-C02
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C04–C06; PDF p. 2"
tags:
  - agriculture
  - vulnerability
  - patching
  - shared-resources
  - managed-services
  - dependency-risk
---

# Agriculture IT access and shared-service dependency exposures

## Exposure class

The class represents high-level digital preconditions reported in agriculture
ransomware cases: known software weaknesses left unpatched, shared network
resources that permit secondary spread, and compromise inherited through a
managed-service dependency. It covers exposure and dependency state, not the
criminal actor or downstream consequence.

> **Claim record — VUL-0002-C01 | source-report**
> **Claim:** The FBI advisory reports unpatched known software weaknesses,
> shared network resources and compromised managed services as aggregate
> initial-access or secondary-infection classes in agriculture ransomware
> cases.
> **Claim status:** active
> **Scope:** High-level source categories; no affected product, identifier,
> configuration, exploitation sequence, entity mapping or current prevalence.
> **As of:** Cases since 2021, reported 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md),
> `SRC-0038-C04`; PDF p. 2, first paragraph under `Threat`.
> **Basis / limits:** Categories are directly reported but not tied case-by-
> case to every outcome. They are not a verified inventory or prevalence study.

## Preconditions and trust boundaries

An exposure becomes consequential only if a malicious action reaches an
applicable service or shared dependency, the affected digital function matters
to production/supply, and controls fail to contain or restore it. Managed-
service and shared-resource dependencies also create organizational trust
boundaries: local continuity can depend on an external or common service whose
state the producer does not fully control.

> **Claim record — VUL-0002-C02 | analytic-judgment**
> **Claim:** These exposure classes can enable `RSK-0017` only where reach,
> dependency criticality and failed containment coincide; their presence alone
> does not establish compromise, production impact or downstream consequence.
> **Claim status:** active
> **Scope:** Defensive dependency model for the source-reported agriculture
> context; not a vulnerability rating or implementation assessment.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0038-C04`–`C06`; PDF p. 2;
> [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md).
> **Basis / limits:** The source directly reports exposure classes and mixed
> operational outcomes. The trust-boundary interpretation is defensive wiki
> synthesis and not a reconstructed network topology.

## Defensive implications

The associated source recommends timely updates, segmentation, access controls,
monitoring, protected backups and recovery/continuity planning. Those are
recommended control families only; the source supplies no adoption or
effectiveness result and does not link a specific control to stopped attempts.

> **Claim record — VUL-0002-C03 | source-report**
> **Claim:** `SRC-0038` recommends controls that address software-maintenance,
> access, shared-resource containment and recovery edges, without showing
> implementation or effectiveness for the represented cases.
> **Claim status:** active
> **Scope:** High-level defensive implications, not configuration instructions
> or causal control evaluation.
> **As of:** 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0038-C08`; PDF pp. 3–4.
> **Basis / limits:** Recommendations are direct. Control-to-event causality is
> absent.

## Safety boundary

No product, weakness identifier, exploit, access procedure or environment-
specific configuration is retained. The page remains at the exposure and
dependency level needed for defensive modeling.

## Related pages

- [TEC-0003 — Agriculture ransomware method](../techniques/tec-0003-ransomware-availability-and-extortion-agriculture.md)
- [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md)
- [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md)
- [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [CTL-0018](../controls/ctl-0018-agriculture-cyber-resilience-and-recovery-controls.md)
- [SYS-0005](../systems/sys-0005-connected-smart-farm-ecosystem.md)

## Sources

- [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md),
  PDF pp. 2–4.
