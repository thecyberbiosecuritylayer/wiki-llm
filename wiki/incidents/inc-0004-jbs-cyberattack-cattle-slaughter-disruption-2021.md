---
id: INC-0004
type: incident
title: JBS cyberattack and temporary U.S. cattle-slaughter disruption, 2021
aliases:
  - May June 2021 JBS cyberattack
  - JBS cattle-slaughter disruption
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
event_date: 2021-05-30
source_ids:
  - SRC-0039
  - SRC-0040
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0039
    claim_id: INC-0004-C01
    evidence:
      - source: SRC-0039
        locator: "SRC-0039-C02–C06; PDF pp. 2–4, especially p. 3 JBS subsection and AMS table"
  - predicate: evidenced-by
    target: SRC-0040
    claim_id: INC-0004-C04
    evidence:
      - source: SRC-0040
        locator: "SRC-0040-C02–C05; title, date and complete substantive paragraph"
  - predicate: affects
    target: AST-0003
    claim_id: INC-0004-C02
    evidence:
      - source: SRC-0039
        locator: "SRC-0039-C03/C04; PDF pp. 2–3"
  - predicate: depends-on
    target: WFL-0007
    claim_id: INC-0004-C07
    evidence:
      - source: SRC-0039
        locator: "SRC-0039-C03–C05; PDF pp. 2–3"
tags:
  - documented-incident
  - agriculture
  - food-processing
  - cattle-slaughter
  - cyberattack
  - jbs
  - fbi-attribution
---

# JBS cyberattack and temporary U.S. cattle-slaughter disruption, 2021

> [!WARNING]
> **Evidence classification**
> One documented real event with two materially distinct official roles. USDA
> ERS reports the operational/throughput consequence and AMS comparator data;
> the FBI independently confirms JBS incident/attribution context. The sources
> do not independently measure the same consequence and do not create two
> incidents.

## Event and timeline

| Date | Event state | Evidence boundary |
| --- | --- | --- |
| 2021-05-30 | USDA ERS reports that JBS Foods was the victim of a cyberattack | Discovery time, initial access and affected digital system are unknown |
| 2021-06-01 | USDA ERS reports closure of nine JBS plants in the United States | The source does not call all nine beef plants or identify locations |
| 2021-06-01–02 | ERS summary characterizes cattle-slaughter disruption as two days; its AMS table reports 94.0 and 105.0 thousand head on Tuesday/Wednesday | National actual-and-estimated series, not JBS throughput or a causal loss estimate |
| By 2021-06-02 | FBI publishes its statement naming `REvil` and `Sodinokibi` in the attribution | The statement does not explain alias relation, actor number, method or evidence |
| By 2021-06-03 | USDA ERS reports facilities fully operational | Not an exact reopening time or independently tested clean/trusted recovery |
| 2021-06-16 | USDA ERS publishes `LDP-M-324` | Publication date is not event/discovery/recovery date |

> **Claim record — INC-0004-C01 | source-report**
> **Claim:** USDA ERS reports a 30-May JBS cyberattack, closure of nine U.S.
> plants on 1 June, a two-day cattle-slaughter disruption and facilities fully
> operational by 3 June.
> **Claim status:** active
> **Scope:** Source-reported event identity, operational states and dates; not
> ransomware classification, initial access, plant identity, system topology,
> exact outage duration or independently tested recovery.
> **As of:** Event 2021-05-30 through 2021-06-03.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0039](../sources/src-0039-usda-ers-jbs-cyberattack-cattle-slaughter-2021.md),
> `SRC-0039-C03`; PDF p. 2 summary and p. 3 JBS subsection.
> **Basis / limits:** The sequence and two-day wording are direct ERS
> reporting. The source does not provide underlying cyber-forensic evidence.

## Source publication dates

- `SRC-0039`: USDA ERS report published 2021-06-16; current landing verified
  2026-07-12.
- `SRC-0040`: FBI statement published 2021-06-02; page metadata modified
  2022-07-21; current presentation verified 2026-07-12.

The first detection time and first public disclosure before the FBI statement
remain unknown. No page date is substituted for discovery.

## Affected assets and services

- nine source-reported JBS U.S. plants, without locations/types;
- cattle-slaughter/processing throughput;
- operational continuity of a large meatpacking organization;
- downstream food-processing availability as an affected interest.

No retained source identifies a particular IT/OT component, cattle inventory,
finished-meat quantity, customer order, food stock or market shortage.

## Confirmed impact

USDA ERS supplies the only direct consequence measurement. Its actual-and-
estimated AMS Memorial Day-week table reports 2021 slaughter values of 2.0,
94.0, 105.0, 120.0, 119.0 and 98.0 thousand head Monday–Saturday, total 538.0.
The week was above 2020's 527.1 but below 2018's 584.7 and 2019's 588.1.

> **Claim record — INC-0004-C02 | source-report**
> **Claim:** The event crossed from a cyberattack and plant availability loss
> into a temporary cattle-slaughter/food-processing-throughput consequence,
> with a national AMS holiday-week series providing bounded numeric context.
> **Claim status:** active
> **Scope:** Observed slaughter/processing throughput and source comparators;
> not JBS-specific headcount, finished-meat output, food shortage, animal harm,
> revenue/price loss or isolated causal effect.
> **As of:** Memorial Day week 2021.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0039-C02`–`C05`; PDF pp. 2–3, especially the AMS table.
> **Basis / limits:** Attack/closure/disruption and table are direct. National
> mixed actual/estimated values, holiday timing, compensating Saturday work and
> the abnormal 2020 comparator prevent a clean event-loss calculation.

Not confirmed:

- cattle injury, welfare outcome or biological/ecological harm;
- discarded/spoiled product, finished-meat loss or shortage;
- attack-caused price, revenue or annual production-forecast effect;
- plant-level throughput or a controlled counterfactual; or
- compromise of a named JBS system or control.

> **Claim record — INC-0004-C03 | source-report**
> **Claim:** USDA's adjacent production/price passages do not attribute their
> annual forecast or price changes to the JBS attack and cannot be counted as
> incident consequences.
> **Claim status:** active
> **Scope:** Causal non-attribution boundary for PDF pp. 3–4; not evidence that
> the attack had zero financial or market effect.
> **As of:** 2021-06-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0039-C06`; PDF p. 3 next subsection and p. 4 price section.
> **Basis / limits:** The report gives other stated rationales; absence of an
> attack attribution is not a null-effect study.

## Reported vector

**Unknown.** Neither source identifies an initial-access route, technique,
product, vulnerability or affected digital/OT system. The FBI attribution
names are not a vector.

## Suspected cause

No technical root cause is established. Both sources say attack/cyberattack;
neither explicitly classifies this event as ransomware in the retained page.

## Actor attribution

The FBI names `REvil` and `Sodinokibi` in its attribution statement. It does
not resolve whether the names are aliases, enumerate actors, disclose method/
evidence or report an adjudicated result.

> **Claim record — INC-0004-C04 | source-report**
> **Claim:** The FBI independently recognises the JBS attack and attributes it
> using the names `REvil` and `Sodinokibi`, without publishing attribution
> method or the incident's operational consequence.
> **Claim status:** active
> **Scope:** Law-enforcement incident/attribution context; not actor identity/
> count, explicit ransomware class, technical proof, conviction or independent
> throughput confirmation.
> **As of:** 2021-06-02.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0040](../sources/src-0040-fbi-statement-jbs-cyberattack-2021.md),
> `SRC-0040-C02`–`C05`; complete substantive paragraph.
> **Basis / limits:** Event name and attribution are direct FBI reporting. The
> one-paragraph statement provides no method or consequence data.

## Cross-domain consequences

The supported path is:

`cyberattack → source-reported closure of nine U.S. plants → two-day cattle-
slaughter/processing-throughput disruption → reported operational restoration`.

This is an observed cyber→cattle-processing-throughput effect at safe
abstraction. It is not an effect on animal health/welfare, plant state or an
ecosystem and is not a complete farm-to-consumer cascade.

> **Claim record — INC-0004-C07 | analytic-judgment**
> **Claim:** `INC-0004` instantiates the operational limb of `RSK-0017` and a
> complete cyber→cattle-processing-throughput path, while animal welfare,
> finished-food, consumer, ecological and market-effect extensions remain
> unsupported.
> **Claim status:** active
> **Scope:** Canonical cross-domain event path, not a likelihood model,
> ransomware technique, isolated causal loss or biological-injury claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `INC-0004-C01`–`C04`;
> [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md);
> `SRC-0039-C02`–`C07`; `SRC-0040-C02`–`C06`.
> **Basis / limits:** USDA directly supplies the event path and metric; FBI is
> materially independent for the incident/attribution context only. The
> outcome itself is not independently measured.

## Response and recovery

USDA reports full operation by 3 June. FBI describes general investigative,
private-sector partnership and victim-reporting posture. Neither source states
the JBS recovery mechanism, restoration test, backup use, safety/quality
reconciliation or independent acceptance criteria.

> **Claim record — INC-0004-C05 | source-report**
> **Claim:** Operational restoration is source-reported by USDA, while the FBI
> gives only general response posture; no represented source demonstrates a
> specific recovery control or its effectiveness.
> **Claim status:** active
> **Scope:** Event response/recovery evidence state; not a conclusion about
> unrepresented JBS actions.
> **As of:** 2021-06-03.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0039-C03/C05`; `SRC-0040-C04/C05`.
> **Basis / limits:** Distinct sources support operational status and general
> posture; neither identifies a control-to-outcome mechanism or test.

## Defensive lessons

- Distinguish national throughput context from organization-specific loss.
- Preserve holiday/catch-up and actual-versus-estimated qualifiers.
- Do not infer ransomware mechanics from actor/family names.
- Treat `fully operational` as reported status, not trusted recovery.
- Count two source roles as one incident and one consequence measurement.

> **Claim record — INC-0004-C06 | analytic-judgment**
> **Claim:** `INC-0004` is one documented agriculture cyber incident supported
> by two materially distinct official roles; it counts once in incident
> chronology and supplies no effectiveness example.
> **Claim status:** active
> **Scope:** Wiki event identity/count and assurance classification.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `INC-0004-C01`–`C05`; `SRC-0040-C06`; `SRC-0039-C08`.
> **Basis / limits:** Event identity is shared; source roles differ. No control
> is linked causally to restoration.

## Evidence and uncertainty

| Predicate | State |
| --- | --- |
| Real JBS cyber event | Corroborated official context |
| Attack date/closure/restoration | USDA source-reported |
| Two-day cattle-slaughter disruption | USDA source-reported |
| National slaughter table | USDA AMS actual-and-estimated context |
| FBI attribution names | FBI source-reported |
| Explicit ransomware class | Unknown in retained sources |
| Vector/vulnerability/system | Unknown |
| Finished-meat/shortage/price/biological harm | Not demonstrated |
| Recovery control/effectiveness | Unknown |

> **Claim record — INC-0004-C08 | analytic-judgment**
> **Claim:** The page preserves source-specific roles and uncertainty without
> merging attribution, throughput measurement, consequence replication or
> recovery-effectiveness predicates.
> **Claim status:** active
> **Scope:** Local evidence model.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page, `INC-0004-C01`–`C07`.
> **Basis / limits:** Every supported and unsupported predicate is listed.

## Safety boundary

No indicators, malicious-software behavior, access procedure, vulnerability,
affected-system topology, payment detail, facility location or operational
recovery procedure is exposed.

> **Claim record — INC-0004-C09 | analytic-judgment**
> **Claim:** No indicators, malicious-software behavior, access procedure,
> vulnerability, affected-system topology, payment detail, facility location
> or operational recovery procedure is exposed.
> **Claim status:** stale
> **Scope:** Local page content.
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

- [SRC-0039](../sources/src-0039-usda-ers-jbs-cyberattack-cattle-slaughter-2021.md)
- [SRC-0040](../sources/src-0040-fbi-statement-jbs-cyberattack-2021.md)
- [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md)
- [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [SYN-0025](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)

## Sources

- [SRC-0039](../sources/src-0039-usda-ers-jbs-cyberattack-cattle-slaughter-2021.md),
  PDF pp. 2–4.
- [SRC-0040](../sources/src-0040-fbi-statement-jbs-cyberattack-2021.md), complete
  substantive paragraph.
