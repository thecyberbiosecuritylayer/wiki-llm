---
id: INC-0005
type: incident
title: Anonymous chicken-farm cyberattack, temperature-control loss and reported chick deaths, 2023
aliases:
  - late December 2023 chicken farm cyberattack
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
event_window: late-2023-12
source_ids:
  - SRC-0042
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0042
    claim_id: INC-0005-C01
    evidence:
      - source: SRC-0042
        locator: "SRC-0042-C03–C06; official transcript, scariest-example question and Ali response"
  - predicate: affects
    target: AST-0003
    claim_id: INC-0005-C02
    evidence:
      - source: SRC-0042
        locator: "Reported chicken-farm barn-temperature control loss and chicks dying"
  - predicate: depends-on
    target: WFL-0007
    claim_id: INC-0005-C02
    evidence:
      - source: SRC-0042
        locator: "Reported automated/digital barn-environment function and livestock production effect"
tags:
  - documented-incident
  - agriculture
  - poultry
  - chicken-farm
  - cyberattack
  - temperature-control
  - animal-effect
  - anonymous
---

# Anonymous chicken-farm cyberattack, temperature-control loss and reported chick deaths, 2023

> [!WARNING]
> **Evidence classification**
> One anonymous event represented by a single official transcript containing a
> responder's direct account of the call and the farmer's relayed operational/
> animal state. It is not independently confirmed by the victim, veterinarian,
> technical investigator or event record.

## Event and publication timeline

| Time | Supported state | Unknown/not substituted |
| --- | --- | --- |
| Late December 2023 | Responder says the chicken-farm call arrived while he was on holiday | Exact date/time, attack onset and discovery time |
| During call | Farmer reportedly says barn temperature control is being lost and chicks are dying | Exact duration, control values, animal count and direct observation |
| 2025-10-15 | AAFC page issues/publishes the transcript | Not necessarily first disclosure of the event |
| After call | Unknown | Response actions, containment, restoration and investigation result |

> **Claim record — INC-0005-C01 | source-report**
> **Claim:** An interviewed incident responder reports receiving a late-
> December-2023 call during a chicken-farm cyberattack and relays the farmer's
> contemporaneous barn-control and animal-impact statement.
> **Claim status:** active
> **Scope:** Event identity/window and evidence route; not exact location/date,
> firsthand animal observation, actor/vector, forensic proof or response.
> **As of:** Late December 2023 account, published 2025-10-15.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** [SRC-0042](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md),
> `SRC-0042-C03`; transcript locator in frontmatter.
> **Basis / limits:** The responder's call receipt is direct testimony; the
> farm/animal state is relayed testimony without independent record.

## Affected assets and reported impact

Supported only at high-level functional abstraction:

- a chicken-farm barn and chicks;
- a temperature-control function described as being lost;
- chicks described as dying during the same reported state.

No device, vendor, farm topology, temperature, count or production metric is
represented.

> **Claim record — INC-0005-C02 | source-report**
> **Claim:** The farmer's relayed report joins cyberattack context, loss of
> barn-temperature control and chicks dying into one observed-event account.
> **Claim status:** active
> **Scope:** Reported animal effect and functional dependency; not exact
> technical causality, measured loss, threshold, welfare diagnosis or general
> poultry risk estimate.
> **As of:** Late December 2023.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** `SRC-0042-C03/C04`; official transcript same response.
> **Basis / limits:** The source explicitly frames the event as a farm
> cyberattack and contemporaneously reports control loss/deaths. No independent
> forensic or veterinary confirmation is available.

## Vector, cause and attribution

**Unknown.** The event passage names no ransomware, malware, initial-access
route, vulnerability, product, vendor, attacker or affected digital component.
Generic ransomware/access statements elsewhere in the episode are not attached
to this event.

> **Claim record — INC-0005-C03 | analytic-judgment**
> **Claim:** The incident is classified only as a source-reported cyberattack;
> mechanism, actor, vector, vulnerability, product and system boundary remain
> unknown.
> **Claim status:** active
> **Scope:** Technical/attribution evidence grade; not evidence those facts do
> not exist outside the retained source.
> **As of:** 2026-07-12 review.
> **Review after:** 2026-10-15.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Full event passage and `SRC-0042-C06`.
> **Basis / limits:** Adjacent generic interview content is not event evidence.

## Cross-domain path

`cyberattack context → reported barn-temperature-control loss → reported
chicks dying`

> **Claim record — INC-0005-C04 | analytic-judgment**
> **Claim:** `INC-0005` is a complete source-reported cyber→animal-effect path
> at safe abstraction, with every technical, quantitative and independent-
> confirmation gap explicit.
> **Claim status:** active
> **Scope:** Canonical transfer instance; not a forensic causality finding,
> likelihood model, threshold validation or population outcome.
> **As of:** 2026-07-12 reconciliation.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** `INC-0005-C01`–`C03`; `SRC-0042-C03`–`C06`;
> [RSK-0018](../risk-scenarios/rsk-0018-poultry-barn-cyber-temperature-control-animal-harm.md).
> **Basis / limits:** Source-reported nodes are complete; evidentiary assurance
> remains one official transcript with relayed farmer testimony.

## Response-time statement

The responder says the farmer told him that a temperature change lasting more
than 15 minutes causes chicks to start dying. The transcript does not say this
event lasted that long or provide a measured/control threshold. The number is
therefore retained only as attributed urgency context, not operational data.

> **Claim record — INC-0005-C05 | source-report**
> **Claim:** The 15-minute statement is nested farmer testimony about urgency,
> not a documented event duration, validated biological threshold or operating
> instruction.
> **Claim status:** active
> **Scope:** Evidence qualification for the transcript statement.
> **As of:** 2025-10-15 transcript.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0042-C05`.
> **Basis / limits:** The wiki does not operationalize the statement.

## Location, response, recovery and defensive lesson

The event location is unknown. Southern Ontario refers to the laboratory's
2024 incident-response count and is not assigned to this 2023 farm. No event-
specific response, recovery or control outcome is described.

The bounded defensive lesson is architectural: life-supporting environmental
functions require explicit cyber-dependency recognition, detection/escalation,
safe continuity and tested recovery. Recommendations in the transcript/
infographic remain generic; they are not credited with changing this event.

> **Claim record — INC-0005-C06 | analytic-judgment**
> **Claim:** The page contributes one anonymous primary-supported agriculture
> event and biological animal-effect instance, but no event-specific control,
> recovery, investigation, location or effectiveness evidence.
> **Claim status:** active
> **Scope:** Incident-corpus counting and assurance boundary.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `INC-0005-C01`–`C05`; `SRC-0042-C08`–`C10`.
> **Basis / limits:** One event is counted once; adjacent source examples and
> 46 calls are not multiplied.

## Evidence matrix

| Predicate | State |
| --- | --- |
| Chicken-farm cyberattack context | Responder source-report |
| Late December 2023 call | Responder source-report |
| Barn-temperature control loss | Farmer statement relayed by responder |
| Chicks dying | Farmer statement relayed by responder |
| Exact location/date/system/vector/actor | Unknown |
| Duration/count/forensic/veterinary confirmation | Unknown |
| Response/recovery/control effectiveness | Unknown |

> **Claim record — INC-0005-C07 | analytic-judgment**
> **Claim:** The evidence route and all known/unknown predicates remain
> explicit and are not upgraded from relayed testimony to independent finding.
> **Claim status:** active
> **Scope:** Local evidence model.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page and `INC-0005-C01`–`C06`.
> **Basis / limits:** Claim modality matches source role.

## Safety boundary

The page exposes no farm/location, live animal record, device, vendor,
endpoint, identifier, temperature/setpoint, validated operating threshold,
access route, exploit or response procedure; the 15-minute testimony remains
explicitly unvalidated urgency context.

> **Claim record — INC-0005-C08 | analytic-judgment**
> **Claim:** The page exposes no farm/location, live animal record, device,
> vendor, endpoint, identifier, temperature/setpoint, validated operating
> threshold, access route, exploit or response procedure; the 15-minute
> testimony remains explicitly unvalidated urgency context.
> **Claim status:** stale
> **Scope:** Local content.
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

- [SRC-0042](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md)
- [RSK-0018](../risk-scenarios/rsk-0018-poultry-barn-cyber-temperature-control-animal-harm.md)
- [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [SYN-0027](../syntheses/syn-0027-canada-agriculture-cyber-animal-effect-reconciliation.md)

## Sources

- [SRC-0042](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md)
