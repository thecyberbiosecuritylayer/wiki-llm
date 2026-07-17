---
id: SYN-0027
type: synthesis
title: AAFC-account agriculture cyber-to-animal-effect reconciliation
aliases:
  - AGE XT chicken farm reconciliation
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0010
  - SRC-0032
  - SRC-0035
  - SRC-0038
  - SRC-0042
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0042
    claim_id: SYN-0027-C03
    evidence:
      - source: SRC-0042
        locator: "SRC-0042-C03–C08; official AAFC transcript chicken-farm account"
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: SYN-0027-C04
    evidence:
      - source: SRC-0032
        locator: "SRC-0032-C06; observation/input→transmission/storage/analytics→decision/action functions"
  - predicate: evidenced-by
    target: SRC-0035
    claim_id: SYN-0027-C04
    evidence:
      - source: SRC-0035
        locator: "SRC-0035-C03/C05/C06; implemented sample→test/result→weekly surveillance-report lane"
  - predicate: depends-on
    target: INC-0005
    claim_id: SYN-0027-C03
    evidence:
      - source: SRC-0042
        locator: "INC-0005-C01–C07; canonical anonymous event and evidence boundaries"
  - predicate: depends-on
    target: RSK-0018
    claim_id: SYN-0027-C03
    evidence:
      - source: SRC-0042
        locator: "RSK-0018-C01–C04; complete safe forward path"
  - predicate: depends-on
    target: SYN-0025
    claim_id: SYN-0027-C01
    evidence:
      - source: SRC-0042
        locator: "SYN-0025-C05/C09 prior AGE-XT gap and score state"
tags:
  - agriculture
  - poultry
  - cross-domain-transfer
  - animal-effect
  - incident
  - reconciliation
---

# AAFC-account agriculture cyber-to-animal-effect reconciliation

## Decision scope

This synthesis audits only `AGE-XT` and the adjacent incident/global gates
that might be incorrectly promoted by one anonymous event. It does not claim
forensic causality, independent event confirmation or control effectiveness.

> **Claim record — SYN-0027-C01 | artifact-observation**
> **Claim:** Before this transaction the corpus is 74 Pass, 33 Partial and
> 3 Absent = 74/110, with AGE at 9/10 and only `AGE-XT` open.
> **Claim status:** active
> **Scope:** Wiki after `SYN-0026` and before `SRC-0042/SYN-0027` activation.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SYN-0001](syn-0001-coverage-rubric.md), checkpoint
> C42; [SYN-0026](syn-0026-us-animal-disease-traceability-herd-assurance-reconciliation.md),
> `SYN-0026-C06`.
> **Basis / limits:** Reproducible artifact state, not external completeness.

## Evidence roles and independence

| Required role | Lineage | Contribution | Boundary |
| --- | --- | --- | --- |
| Observed forward animal-effect anchor | AAFC official transcript / U. Guelph responder testimony | cyberattack→barn-control loss→chicks dying | Anonymous, relayed farmer state, no independent investigation |
| Independent hostile agriculture context | Virginia Tech Drape; U.S. FBI advisory | adversarial sensor/data and ransomware→production availability paths | Potential/aggregated, not confirmation of chicken event |
| Reverse functional direction | AU strategy | biological/environmental/sensor input→analytics→decision/action | Intended strategy functions |
| Reverse implemented lane | UK PATH-SAFE/APHA | sample→test/result→weekly surveillance report | Programme implementation, not universal control decision |

AAFC, Virginia Tech, U.S. FBI, AU and UK programme lineages are materially
independent. The AAFC transcript and infographic are one lineage; the
infographic is hypothetical and adds no confirmation.

> **Claim record — SYN-0027-C02 | analytic-judgment**
> **Claim:** `AGE-XT` has a claim-appropriate SF2 portfolio: one direct SF1
> AAFC forward-effect account, independent Drape/FBI hostile-context roles and
> independent AU/PATH-SAFE reverse-direction roles, with observed, potential,
> intended and implemented states kept distinct.
> **Claim status:** active
> **Scope:** Source-floor/role reconciliation; not SF3 event confirmation,
> source-count multiplication or universal agriculture behavior.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0010-C05`, `SRC-0032-C06`, `SRC-0035-C03/C05/C06`,
> `SRC-0038-C03`–`C05`, `SRC-0042-C03`–`C08`.
> **Basis / limits:** Institutional, jurisdictional and evidence-type roles are
> independent and non-equivalent.

## Forward direction — cyber to animal effect

The accepted functional path is:

`source-reported cyberattack → reported loss of barn-temperature control →
reported chicks dying`

It is stronger than the JBS processing-throughput path for the frozen literal
because the receiving state is animals. It is weaker in assurance: one
responder transcript relays the farmer's state and supplies no forensic/
veterinary confirmation, magnitude, exact date or location.

> **Claim record — SYN-0027-C03 | analytic-judgment**
> **Claim:** `INC-0005/RSK-0018` supply the missing complete cyber→animal-
> effect literal at safe abstraction, while every mechanism, magnitude,
> attribution, location and independent-confirmation gap remains explicit.
> **Claim status:** active
> **Scope:** One anonymous reported poultry event; not exact causal mechanism,
> likelihood, generality, threshold validation or SF3 consequence proof.
> **As of:** Event account late December 2023.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** [INC-0005](../incidents/inc-0005-anonymous-chicken-farm-temperature-control-animal-deaths-2023.md),
> `INC-0005-C01`–`C07`; [RSK-0018](../risk-scenarios/rsk-0018-poultry-barn-cyber-temperature-control-animal-harm.md),
> `RSK-0018-C01`–`C04`; `SRC-0042-C03`–`C06`.
> **Basis / limits:** The animal-effect nodes are source-reported; audit grade
> is medium because victim/veterinary/forensic confirmation is absent.

## Reverse direction — biological/environmental/sensor input to digital output

AU directly maps biological/environmental and sensor/human observations through
transmission, storage and analytics into surveillance/advisory/decision/action
functions. PATH-SAFE/APHA independently supplies an implemented environmental/
food sample→laboratory result→weekly surveillance-report lane. This was already
accepted as complete in `SYN-0025-C05` and is not reclassified as an incident.

> **Claim record — SYN-0027-C04 | analytic-judgment**
> **Claim:** Independent AU and PATH-SAFE/APHA roles retain the complete
> biological/environmental/sensor-input→digital surveillance/decision direction
> with intended-function and bounded-implementation states separated.
> **Claim status:** active
> **Scope:** Reverse AGE-XT functional path; not autonomous authority,
> universally observed decision outcomes or safeguard effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C06`; [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C03/C05/C06`; `SYN-0025-C05`.
> **Basis / limits:** Both directions' state and source roles remain explicit.

## `AGE-XT` decision

> **Claim record — SYN-0027-C05 | analytic-judgment**
> **Claim:** The independent portfolio now satisfies `AGE-XT` at SF2: one full
> cyber→animal-effect path and one full biological/environmental/sensor-input→
> digital surveillance/decision path are explicitly reconciled.
> **Claim status:** active
> **Scope:** Frozen bidirectional functional criterion; not an independently
> confirmed poultry case, population risk, universal automation or global
> directionality-gate decision.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0027-C02`–`C04`; exact `AGE-XT` criterion/source floor in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** Full literal directions and SF2 are met. SF3 is not the
> cell floor and is not implied.

## Incident and global-gate non-promotions

- `THI-WL`: at most five primary-supported events, below six.
- `THI-SD`: the barn-control dependency adds bounded detail, but fewer than
  four incidents have primary technical dependency support.
- `THI-XT`: forward cases span three sectors, but no primary incident supplies
  the required material/input→digital direction.
- `THI-CI`: at most five events across three sectors, below six/four even
  though an animal-effect example is added.
- `THI-CT/AE`: no event-specific control outcome or independent investigation.
- `CTR-CI/AE` and global control/incident gates remain below their floors.
- Global directionality remains Fail because AU supplies intended functions and
  PATH-SAFE reaches an implemented surveillance report, not a corroborated
  observed downstream decision outcome; this forward event adds no reverse
  outcome.

> **Claim record — SYN-0027-C06 | analytic-judgment**
> **Claim:** `THI-WL/SD/XT/CI/CT/AE`, `CTR-CI/AE` and all global gates remain
> unchanged; one anonymous event and one hypothetical infographic are not
> multiplied into missing events, directions, investigations or effectiveness.
> **Claim status:** active
> **Scope:** Adjacent-cell and gate audit after `INC-0005`.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYN-0027-C01`–`C05`; frozen criteria/gates.
> **Basis / limits:** Exact numeric, sector, direction and evaluator blockers
> remain explicit.

## Score decision

> **Claim record — SYN-0027-C07 | artifact-observation**
> **Claim:** Strict review accepts exactly `AGE-XT` Partial→Pass. Totals become
> 75 Pass, 32 Partial and 3 Absent = 75/110 (68.2%); AGE becomes 10/10,
> critical cells become 63/27/1, dimensions at least 9/10 remain 3/11 and
> global gates remain 7 Pass/5 Fail.
> **Claim status:** active
> **Scope:** Wiki after active `SRC-0042`, `INC-0005`, `RSK-0018` and
> `SYN-0027`; not absolute domain completeness or any adjacent transition.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0027-C01`–`C06`; exact frozen criterion/source floor;
> independent audits required before activation.
> **Basis / limits:** One critical cell moves; all count/effectiveness/global
> gates remain unchanged.

## Safety boundary

> **Claim record — SYN-0027-C08 | analytic-judgment**
> **Claim:** The synthesis exposes no farm/location, product, endpoint,
> identifier, credential, operating value, access route, exploit, biological
> procedure or operational response instruction.
> **Claim status:** stale
> **Scope:** Local content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local content and source safety boundaries.
> **Limits:** Only safe public functional/evidence-state reasoning is retained.
> This is a local page-content assertion, not an externally evidenced decision
> claim, so it is retained as a safety note but is no longer maintained as
> active evidence.

## Related pages

- [SYN-0001](syn-0001-coverage-rubric.md)
- [SYN-0025](syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)
- [INC-0005](../incidents/inc-0005-anonymous-chicken-farm-temperature-control-animal-deaths-2023.md)
- [RSK-0018](../risk-scenarios/rsk-0018-poultry-barn-cyber-temperature-control-animal-harm.md)

## Sources

- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [SRC-0038](../sources/src-0038-us-agriculture-cooperative-ransomware-advisory-2022.md)
- [SRC-0042](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md)
