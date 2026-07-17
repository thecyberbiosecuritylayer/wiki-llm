---
id: CTL-0018
type: control
title: Agriculture ransomware resilience, continuity and recovery controls
aliases:
  - agricultural cooperative ransomware controls
  - agriculture production continuity and recovery safeguards
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0038
sensitivity: public
dual_use: low
control_status: recommended
implementation_status: unknown
testing_status: unknown
effectiveness_status: unknown
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0038
    claim_id: CTL-0018-C01
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C08; PDF pp. 3–4"
  - predicate: mitigates
    target: RSK-0017
    claim_id: CTL-0018-C02
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C04/C05/C08; PDF pp. 2–4"
  - predicate: detects
    target: THR-0002
    claim_id: CTL-0018-C02
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C05/C08; PDF pp. 2–4, stopped-attempt boundary and monitoring/reporting recommendations"
  - predicate: recovers
    target: RSK-0017
    claim_id: CTL-0018-C03
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C08; PDF p. 3, protected backups, recovery planning and manual-continuity recommendations"
  - predicate: depends-on
    target: WFL-0007
    claim_id: CTL-0018-C02
    evidence:
      - source: SRC-0038
        locator: "SRC-0038-C06/C08; PDF pp. 1–3, production/supply dependencies and critical-function continuity"
tags:
  - agriculture
  - ransomware
  - resilience
  - continuity
  - backup
  - recovery
  - recommended-control
---

# Agriculture ransomware resilience, continuity and recovery controls

## Objective

Reduce the chance that ransomware reaches a production-critical agriculture
dependency, detect and contain malicious activity, preserve safe minimum
operations during digital unavailability, and restore trustworthy service
without silently carrying compromised state forward.

The FBI source supplies recommendations, not proof that any control is
implemented, tested or effective.

## Control-state table

| Dimension | State | Evidence boundary |
| --- | --- | --- |
| Recommended | **Yes** | Direct FBI recommendation set |
| Implemented | Unknown | No affected-entity deployment record |
| Tested | Unknown | No exercise, restoration test or acceptance result |
| Effective | Unknown | Stopped attempts are not linked to named controls |
| Independently evaluated | Unknown | One coordinated federal advisory lineage |

> **Claim record — CTL-0018-C01 | source-report**
> **Claim:** The FBI recommends a layered agriculture ransomware control set
> covering maintenance and access, segmentation and monitoring, protected
> backups, critical-function/manual continuity, recovery planning and training,
> plus assessment resources and reporting.
> **Claim status:** active
> **Scope:** High-level recommended functions; not configuration instructions,
> deployment, testing, interrupted-event evidence or effectiveness.
> **As of:** 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md),
> `SRC-0038-C08`; PDF pp. 3–4.
> **Basis / limits:** Recommendation status and functions are direct. The wiki
> aggregates them defensively and omits environment-specific procedure.

## Scenario edges addressed

For `RSK-0017`, the recommendations map to five bounded edges:

1. **Exposure edge:** maintenance, authentication, least privilege and
   segmentation reduce reachable or propagating exposure.
2. **Detection/containment edge:** monitoring, endpoint safeguards, awareness
   and reporting support recognition and escalation.
3. **Dependency edge:** critical-function identification distinguishes
   administration-only loss from production-critical unavailability.
4. **Continuity edge:** a preplanned safe manual mode can reduce production
   interruption where the physical process allows it.
5. **Recovery edge:** protected separated backups and recovery planning support
   restoration after containment.

> **Claim record — CTL-0018-C02 | analytic-judgment**
> **Claim:** The recommendation set maps directly to exposure, detection,
> containment, production-dependency and manual-continuity edges of
> `RSK-0017`, but the advisory does not demonstrate that any mapped control
> interrupted a represented case.
> **Claim status:** active
> **Scope:** Exact-edge defensive mapping; not deployment, causal effect or a
> complete agriculture cybersecurity baseline.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0038-C04/C05/C08`; PDF pp. 2–4;
> [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md).
> **Basis / limits:** The recommendation-to-edge alignment is explicit enough
> for defensive mapping. No case links its stopped attempts to these controls.

## Recovery and trusted-state boundary

The source directly recommends protected backups, physically separate or
segmented copies, a recovery plan and a plan for critical functions when
systems are offline. It does not specify agriculture safety acceptance
criteria, biological/quality/traceability reconciliation, recovery-point or
recovery-time targets, restoration testing, or evidence that the restored
state is trustworthy.

> **Claim record — CTL-0018-C03 | source-report**
> **Claim:** `SRC-0038` supplies an explicit agriculture-relevant recovery and
> manual-continuity design, while trusted restoration, local safety validation,
> testing and recovery performance remain unknown.
> **Claim status:** active
> **Scope:** Recovery-design evidence and its omissions; not an implemented or
> validated recovery procedure.
> **As of:** 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0038-C08`; PDF p. 3.
> **Basis / limits:** Recovery and manual-operation recommendations are direct.
> Trusted-state assurance and agriculture-specific acceptance predicates are
> not supplied.

## Applicability and prerequisites

- identify critical production, processing and supply dependencies before an
  incident;
- assign system, operations, safety/quality and external-service owners;
- define when manual operation is safe, authorized and traceable;
- protect recovery material from the same failure domain;
- validate restored information and process state before reconnecting it to
  production; and
- preserve reporting and learning responsibilities.

Critical-function identification (item 1), the manual-operation concept in
item 3 and separated recovery material (item 4) are supported at high level by
the advisory. Owner assignment, safe/authorized/traceable manual-operation
predicates, restored-state validation and learning responsibilities are
conservative wiki requirements and must be supplied locally or by other
sources.

## Dependencies

The controls depend on a correct `AST-0003/WFL-0007` asset-and-workflow map and
on knowing external/shared-service trust boundaries. A backup cannot preserve
continuity if a critical external provider remains unavailable; a manual mode
can create quality or traceability problems if it is not locally validated.

## Failure modes and tradeoffs

- untested backups may be unavailable, incomplete or carry untrusted state;
- segmentation can impair safe operations if production dependencies are
  misunderstood;
- manual work can reduce throughput and introduce record, quality or safety
  errors;
- monitoring without an owner or response threshold may not contain harm;
- small or time-sensitive operators may lack alternate capacity; and
- generic recommendations can miss sector-specific biological, physical and
  traceability constraints.

## Validation and evidence of effectiveness

A complete test should state the environment, control version, scenario edge,
baseline, safe-state and traceability requirements, recovery criteria, timing,
adverse/null results and evaluator independence. `SRC-0038` supplies none of
those results. Two stopped attempts cannot be attributed to a named control.

> **Claim record — CTL-0018-C04 | analytic-judgment**
> **Claim:** The advisory provides no control implementation, test,
> effectiveness or independent-evaluation result, and its stopped-attempt
> reports cannot be used as causal safeguard evidence.
> **Claim status:** active
> **Scope:** Assurance status of the represented control family.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0038-C01/C05/C08`; complete PDF pp. 1–4.
> **Basis / limits:** No control-to-outcome linkage or test method appears in
> the source; absence is based on complete review of all four pages.

## Portfolio mapping

`CTL-0005` supplies broader agriculture capability, data/traceability and
bounded biological-surveillance controls. `CTL-0017` supplies binding EU
animal/plant biosecurity, traceability, detection/response and IMSOC
continuity-reconciliation edges. `CTL-0018` adds a concrete agriculture-
specific ransomware response, manual-continuity and recovery design. Their
combination was candidate evidence for `AGE-CT`; `SYN-0025` later completed
the independent criterion synthesis without adding effectiveness evidence.

> **Claim record — CTL-0018-C05 | analytic-judgment**
> **Claim:** `CTL-0018` fills the previously missing agriculture-specific
> cyber-response/recovery design contribution, but one FBI lineage and absent
> trusted-recovery testing mean this transaction alone does not pass `AGE-CT`.
> **Claim status:** superseded
> **Scope:** Candidate contribution to frozen `AGE-CT`; no score transition.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `CTL-0018-C01`–`C04`;
> [CTL-0005](ctl-0005-agricultural-cyberbiosecurity-capability-controls.md);
> [CTL-0017](ctl-0017-animal-plant-health-traceability-notification-response-controls.md);
> frozen rubric in [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** The cyber recovery edge is now direct, while criterion-
> level independence/reconciliation and effectiveness remain separate.
> **Superseded by:** `SYN-0025-C07`, which completes the independent exact-edge
> design reconciliation without promoting trusted recovery or effectiveness.

## Safety boundary

Only high-level defensive control functions are retained. No indicators,
exploit identifiers, access procedure, product-specific weakness or production
configuration is reproduced.

## Related pages

- [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md)
- [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md)
- [VUL-0002](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md)
- [CTL-0005](ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [CTL-0017](ctl-0017-animal-plant-health-traceability-notification-response-controls.md)
- [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [SYN-0025](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)

## Sources

- [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md),
  PDF pp. 3–4.
