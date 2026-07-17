---
id: RSK-0018
type: risk-scenario
title: Poultry-barn cyber disruption of environmental control to animal harm
aliases:
  - chicken barn cyber temperature-control animal-effect path
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-15
source_ids:
  - SRC-0042
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0042
    claim_id: RSK-0018-C01
    evidence:
      - source: SRC-0042
        locator: "SRC-0042-C03–C06; official transcript chicken-farm response"
  - predicate: evidenced-by
    target: INC-0005
    claim_id: RSK-0018-C03
    evidence:
      - source: SRC-0042
        locator: "INC-0005-C01–C07; same single event/source evidence route"
  - predicate: affects
    target: AST-0003
    claim_id: RSK-0018-C02
    evidence:
      - source: SRC-0042
        locator: "Reported barn temperature-control function and chicks dying"
  - predicate: depends-on
    target: WFL-0007
    claim_id: RSK-0018-C01
    evidence:
      - source: SRC-0042
        locator: "Farm environmental monitoring/control to livestock-production state"
tags:
  - agriculture
  - poultry
  - cyber-physical
  - environmental-control
  - animal-harm
  - observed-path
---

# Poultry-barn cyber disruption of environmental control to animal harm

## Safe canonical path

`source-reported cyberattack → reported loss of barn-temperature control →
reported chicks dying`

Every modifier matters: the path is complete at functional level but rests on
one official interview transcript containing responder testimony and a relayed
farmer statement. It contains no actionable detail.

> **Claim record — RSK-0018-C01 | analytic-judgment**
> **Claim:** `RSK-0018` maps a cyberattack context through loss of a digitally/
> automatically supported barn-environment function to a downstream animal-
> effect state.
> **Claim status:** active
> **Scope:** Functional transfer mechanism; not a specific architecture,
> malware action, operating threshold, likelihood or universal farm model.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** [SRC-0042](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md),
> `SRC-0042-C03/C04`; [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md).
> **Basis / limits:** The full nodes are in one source-reported event; exact
> technical causality and independent confirmation are absent.

## Receiving assets and consequence

The receiving biological state is chicks dying, not merely delayed processing,
lost production or hypothetical welfare pressure. The source supplies no count,
diagnosis, duration, economic metric or counterfactual.

> **Claim record — RSK-0018-C02 | analytic-judgment**
> **Claim:** The receiving state is a reported animal effect linked to
> `AST-0003`, while magnitude, veterinary cause, welfare scope and economic/
> production extensions remain unsupported.
> **Claim status:** active
> **Scope:** Consequence classification, not quantified harm or causal estimate.
> **As of:** Event account late December 2023.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** `SRC-0042-C03`–`C06`;
> [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md).
> **Basis / limits:** Animal-effect words are direct relayed testimony; all
> quantitative/clinical predicates are absent.

## Evidence-state reconciliation

| Layer | State |
| --- | --- |
| Event | One anonymous source-reported incident (`INC-0005`) |
| Cyber classification | Transcript question/answer context |
| Control loss | Farmer statement relayed by responder |
| Animal effect | Farmer statement relayed by responder |
| Mechanism infographic | Hypothetical same-lineage illustration, not event proof |
| Independent forensic/veterinary confirmation | Absent |

> **Claim record — RSK-0018-C03 | analytic-judgment**
> **Claim:** `INC-0005` provides observed-event instantiation at safe
> abstraction; the AAFC dairy infographic supplies only a separate hypothetical
> mechanism and cannot corroborate or multiply the chicken-farm event.
> **Claim status:** active
> **Scope:** Observed/hypothetical and same-lineage distinction.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [INC-0005](../incidents/inc-0005-anonymous-chicken-farm-temperature-control-animal-deaths-2023.md),
> `INC-0005-C01`–`C07`; `SRC-0042-C07/C08`.
> **Basis / limits:** Evidence roles are distinct even within one source package.

## Criterion contribution and controls

Generic agriculture cyber continuity/recovery controls in `CTL-0018` are
relevant to availability, but no represented source evaluates their use in
this incident. No control relation is promoted to effective interruption.

> **Claim record — RSK-0018-C04 | analytic-judgment**
> **Claim:** The page supplies the previously missing direct cyber→animal-
> effect literal for `AGE-XT`; pass still requires SF2 reconciliation with the
> independent reverse path and other forward-context lineages in `SYN-0027`.
> **Claim status:** superseded
> **Scope:** Candidate frozen-cell contribution; no source-accumulation score.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `RSK-0018-C01`–`C03`; `AGE-XT` criterion in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Literal forward path is present; source-floor audit is
> separate.
> **Superseded by:** `SYN-0027-C05` after independent SF2 reconciliation.

## Safety boundary

No farm/location, product, topology, endpoint, credential, operating value,
access route, exploit or operational response instruction is exposed.

> **Claim record — RSK-0018-C05 | analytic-judgment**
> **Claim:** No farm/location, product, topology, endpoint, credential,
> operating value, access route, exploit or operational response instruction is
> exposed.
> **Claim status:** stale
> **Scope:** Local page.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local content.
> **Limits:** Only safe functional nodes and evidence grades were retained at
> the stated review date. Repository-content assertions can change; this one is
> retained only as a historical safety note, with the current boundary stated
> in prose above.

## Related pages

- [INC-0005](../incidents/inc-0005-anonymous-chicken-farm-temperature-control-animal-deaths-2023.md)
- [SRC-0042](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md)
- [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [CTL-0018](../controls/ctl-0018-agriculture-cyber-resilience-and-recovery-controls.md)
- [SYN-0027](../syntheses/syn-0027-canada-agriculture-cyber-animal-effect-reconciliation.md)

## Sources

- [SRC-0042](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md)
