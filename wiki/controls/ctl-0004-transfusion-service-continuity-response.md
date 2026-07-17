---
id: CTL-0004
type: control
title: Transfusion-service surge and continuity response
aliases:
  - RCI surge continuity response
  - transfusion compatibility downtime response
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0008
sensitivity: public
dual_use: low
control_status: operational-response
implementation_status: implemented-in-one-incident
testing_status: real-event-exercised-not-formally-tested
effectiveness_status: source-reported-bounded
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: CTL-0004-C01
    evidence:
      - source: SRC-0008
        locator: "pp. 22, 92 and 97"
  - predicate: mitigates
    target: RSK-0006
    claim_id: CTL-0004-C02
    evidence:
      - source: SRC-0008
        locator: "pp. 21–22, 92 and 97"
  - predicate: depends-on
    target: WFL-0006
    claim_id: CTL-0004-C03
    evidence:
      - source: SRC-0008
        locator: "pp. 10, 21–22, 92, 97 and 124"
  - predicate: depends-on
    target: AST-0002
    claim_id: CTL-0004-C03
    evidence:
      - source: SRC-0008
        locator: "pp. 21–22 and 97"
tags:
  - transfusion
  - continuity
  - surge-capacity
  - incident-response
  - implemented-control
---

# Transfusion-service surge and continuity response

> Operational continuity control used during a real external laboratory-system
> disruption: expand specialist compatibility-testing capacity, extend service
> hours, prioritize urgent cases and coordinate constrained blood-stock use.
> It is not a preventive cyber control and its effectiveness is reported by the
> implementing organization, not independently proven.

## Objective

Maintain safe access to compatibility testing/advice and blood components when
ordinary laboratory-system capacity is disrupted, while preventing the
fallback from exhausting specialist staff or constrained product inventory.

## Evidence status

| Dimension | Current status | Evidence boundary |
| --- | --- | --- |
| Recommended | Yes, implicitly through reported continuity practice and future planning | Not presented as a universal guideline |
| Implemented | **Yes — one documented incident** | NHSBT reports the actions it took |
| Exercised | **Yes — real disruption** | Operational use is not a predefined test |
| Formally tested | Unknown | No exercise plan, acceptance criterion or test report |
| Effective | **Source-reported, bounded** | NHSBT says continuity was maintained; no independent metric/counterfactual |
| Independently evaluated | Unknown | C&AG audit does not assure the incident/control narrative |

> **Claim record — CTL-0004-C01 | source-report**
> **Claim:** During the June 2024 disruption, NHSBT reports that RCI scaled
> operations, extended working hours and prioritized urgent cases to support
> affected hospitals and maintain transfusion continuity.
> **Claim status:** active
> **Scope:** NHSBT's response to one Synnovis-related service disruption; not a
> universal capability or guarantee.
> **As of:** 2024-06.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 22 and 97; contingency context p. 92.
> **Basis / limits:** Implementation and management-reported continuity are
> direct. Pages 22/97 duplicate one account; case volume, response time,
> service-level objective, adverse outcomes and independent evaluation are
> absent. Page 92 does not name Synnovis.

## Scenario edges addressed

For
[RSK-0006](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md),
the control conditionally interrupts:

1. **compatibility-service gap:** specialist RCI testing/advice absorbs urgent
   cases when ordinary access is disrupted;
2. **time-to-care edge:** extended hours and urgent prioritization preserve
   access for emergency/surgical needs;
3. **supply-pressure edge:** coordination with the NHS manages and optimizes
   use of limited O-negative stock;
4. **continuity governance edge:** critical-incident/business-continuity
   structures coordinate the wider response.

> **Claim record — CTL-0004-C02 | analytic-judgment**
> **Claim:** The implemented response mitigated the service-gap and downstream
> continuity edges of `RSK-0006`, while greater O-negative reliance transferred
> part of the burden into constrained biological inventory.
> **Claim status:** active
> **Scope:** Exact-edge interpretation of the one reported event; not a claim
> that the control prevented every consequence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–22, 92 and 97.
> **Basis / limits:** The source connects actions to continuity and fallback to
> stock pressure. “Mitigated” is bounded to the stated edges; there is no
> independent causal estimate, counterfactual or proof of zero patient harm.

## Applicability and prerequisites

- a known [compatibility workflow](../workflows/wfl-0006-transfusion-compatibility-and-blood-issue.md) and criteria for urgent escalation;
- alternate specialist testing/advice capacity with competent staff;
- communication and decision authority across affected hospitals, provider and
  blood service;
- visibility of constrained product stock and ability to coordinate use;
- safe identity, specimen, result and product traceability during contingency;
- criteria for returning to normal operation and validating restored results;
- protection of the responder's own national supply and routine services.

> **Claim record — CTL-0004-C03 | source-report**
> **Claim:** NHSBT's report shows that contingency support depends on specialist
> service capacity, urgent-case prioritization and blood-stock coordination and
> warns that supporting the wider NHS must be balanced against NHSBT's ability
> to maintain its own stock and key-product supply.
> **Claim status:** active
> **Scope:** Dependencies and tradeoff stated for the south-London event and
> future similar circumstances.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–22, 92 and 97.
> **Basis / limits:** Capacity/supply balance is explicit. The report does not
> publish trigger thresholds, staffing model, stock quantities or transfer
> procedure, and this wiki does not infer them.

## Dependencies

- [AST-0002](../assets/ast-0002-transfusion-compatibility-and-blood-products.md) —
  compatibility information and material availability;
- [WFL-0006](../workflows/wfl-0006-transfusion-compatibility-and-blood-issue.md) —
  the service path to preserve;
- [SYS-0004](../systems/sys-0004-transfusion-laboratory-information-systems.md) —
  affected external systems and separate NHSBT support systems/services;
- competent RCI, blood-supply, hospital and incident-management personnel;
- cross-organizational communications and authority.

## Implementation considerations

- Predefine when specialist support is activated and who can reprioritize work.
- Maintain identity, result and product traceability under contingency; speed
  must not erase clinical/quality controls.
- Treat O-negative use as a constrained fallback with downstream stock effects.
- Track both assistance delivered and impact on the responder's normal duties.
- Validate restored systems/results before ending contingency.
- Record unserved/delayed cases, near misses, supply state and staff burden,
  including null or adverse findings.

## Failure modes and tradeoffs

- specialist capacity may saturate or depend on the same upstream services;
- extended hours can increase fatigue, staffing and quality risk;
- urgent prioritization can delay other cases;
- fallback product use can move risk into limited inventory;
- maintaining immediate care can mask accumulating workload or supply debt;
- restoration without integrity/identity validation can reintroduce unsafe
  state;
- a first-party success narrative can conceal unmeasured adverse outcomes.

## Validation and evidence of effectiveness

The event is strong implementation evidence but incomplete effectiveness
evidence. A robust evaluation would report:

- activation time and time to first/each completed specialist case;
- demand, capacity, backlog and unserved/delayed case counts;
- identity/result/product errors and near misses during contingency;
- O-negative consumption, stock trajectory and displaced demand;
- impact on NHSBT's routine services and staff;
- clinical outcomes or explicitly bounded absence-of-harm review;
- restoration validation and after-action findings;
- an independent evaluator and counterfactual/baseline where feasible.

The report also discloses a `Limited` internal-audit finding for disaster-
recovery planning of an unnamed critical ICT system and open ISO 22301 minor
non-conformities. These are valuable negative assurance context, not evidence
that this exact RCI response failed.

## Framework mappings

No universal framework or legal mapping is inferred from this single
institutional response. Later governance sources may map continuity, clinical
safety, information security and blood-service duties, with exact versions and
jurisdiction recorded.

## Related pages

- [INC-0001 — Synnovis transfusion-service disruption](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md)
- [RSK-0006 — Compatibility-system disruption and supply pressure](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md)
- [AST-0002 — Transfusion compatibility information and blood-product availability](../assets/ast-0002-transfusion-compatibility-and-blood-products.md)
- [WFL-0006 — Transfusion compatibility testing and blood issue](../workflows/wfl-0006-transfusion-compatibility-and-blood-issue.md)
- [SYS-0004 — Transfusion laboratory information systems](../systems/sys-0004-transfusion-laboratory-information-systems.md)
- [SRC-0008 — NHSBT Annual Report 2024–25](../sources/src-0008-nhsbt-annual-report-2024-2025.md)

## Sources

- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 21–22,
  77, 91–98 and 104.
