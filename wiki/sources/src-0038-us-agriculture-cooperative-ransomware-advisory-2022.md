---
id: SRC-0038
type: source
title: FBI ransomware attacks on agricultural cooperatives advisory, 2022
aliases:
  - Ransomware Attacks on Agricultural Cooperatives Potentially Timed to Critical Seasons
  - FBI PIN 20220420-001
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_type: official-us-federal-private-industry-notification
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/us-agriculture-ransomware-advisory-2022.pdf
sha256: 9f47d51da3e11db00225502560e59c10c406b52081130327cd6294be8de8fcdd
raw_components:
  - path: ../../raw/ic3-2022-industry-alerts-current-2026-07-12.html
    role: current-official-ic3-2022-advisory-index
    sha256: 2188eab96b6f1013fc88112635abe653dd44c4b145a3c9c89329ac32f59bfd6d
canonical_url: https://www.ic3.gov/CSA/2022/220420-2.pdf
index_url: https://www.ic3.gov/CSA/2022
accessed: 2026-07-12
issued: 2022-04-20
issuer: Federal Bureau of Investigation
coordinated_with:
  - Cybersecurity and Infrastructure Security Agency
  - United States Department of Agriculture
jurisdictions:
  - United States
tags:
  - agriculture
  - ransomware
  - agricultural-cooperatives
  - production-continuity
  - supply-chain
  - recovery
  - federal-advisory
---

# FBI ransomware attacks on agricultural cooperatives advisory, 2022

## Identity, acquisition and complete review

The retained primary artifact is the four-page FBI Private Industry
Notification `20220420-001`, issued 20 April 2022 and titled *Ransomware
Attacks on Agricultural Cooperatives Potentially Timed to Critical Seasons*.
The document says it was coordinated with DHS/CISA and USDA. Coordination does
not turn one publication lineage into three independent sources.

- The official IC3 PDF is 1,342,213 bytes and was completely reviewed.
- The official current IC3 2022 advisory index snapshot is 55,434 bytes and
  still lists the notification on 2026-07-12. It is retained as a current
  discovery/status companion, not as an independent substantive source.
- The PDF is unencrypted, untagged PDF 1.7 with four letter-size pages, no form
  and no JavaScript reported. `pdfsig` reported no signature and emitted an
  NSS-initialisation warning, so no cryptographic-authentication claim is made.
- Static inspection of the retained index found six script and one form
  elements and no iframe/object/embed. Nothing was executed or submitted; the
  count is not runtime assurance.
- The two retained objects total 1,397,647 bytes.

> **Claim record — SRC-0038-C01 | artifact-observation**
> **Claim:** The retained 1,397,647-byte package contains the complete official
> four-page FBI notification and a current official IC3 index snapshot, with
> identity, byte hashes, complete-review state and static format/safety limits
> recorded.
> **Claim status:** active
> **Scope:** Retained artifacts and review process; not cryptographic
> authentication, runtime assurance or confirmation of every underlying case.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Raw objects, hashes and format observations above; PDF pp. 1–4;
> retained IC3 index entry for 20 April 2022.
> **Basis / limits:** Artifact identity and complete review are reproducible.
> The index is a companion from the same IC3 publication ecosystem.

## Publication role and evidence lineage

The notification is an official U.S. federal defensive advisory for Food and
Agriculture partners. The FBI is the issuing and reporting authority; CISA and
USDA are named as coordination partners. It aggregates agency observations and
source-reported events but does not identify every affected entity, disclose a
case method or provide independent case records.

The historical `TLP:WHITE` marking states that the product could be shared
without restriction subject to ordinary copyright rules. The wiki nevertheless
keeps only high-level defensive findings and excludes variant lists, exploit
identifiers, indicators and procedural attack detail.

> **Claim record — SRC-0038-C02 | source-report**
> **Claim:** `SRC-0038` is one FBI-issued, CISA/USDA-coordinated federal
> advisory lineage that reports multiple agriculture-sector events and gives
> defensive recommendations; it is not multiple independent investigations or
> an effectiveness study.
> **Claim status:** active
> **Scope:** Issuer, coordination, audience, publication role and independence
> classification; not legal authority, case attribution or outcome validation.
> **As of:** 2022-04-20; index presence checked 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF p. 1, publication metadata/summary; p. 2, reported events;
> pp. 3–4, recommendations/resources; current IC3 2022 advisory index.
> **Basis / limits:** Publication metadata are direct. Anonymous cases share
> the advisory's evidence lineage and are not converted into incident pages.

## Threat pattern and seasonal context

The FBI says ransomware actors may be more likely to target agricultural
cooperatives during time-critical planting and harvest periods because of the
cooperatives' production role and perceived pressure to pay. This is a federal
threat assessment, not proof of a deterministic seasonal strategy, actor
identity, event likelihood or future frequency.

> **Claim record — SRC-0038-C03 | source-report**
> **Claim:** The FBI assesses that ransomware actors may target
> agricultural cooperatives around planting or harvest, creating a potential
> availability, financial and food-supply risk at time-sensitive production
> stages.
> **Claim status:** active
> **Scope:** High-level ransomware threat and timing assessment for U.S. Food
> and Agriculture partners; not actor attribution, exploit detail, incidence
> rate, quantified likelihood or biological consequence.
> **As of:** 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF p. 1, Summary; p. 2, Threat.
> **Basis / limits:** The assessment is direct source reporting. `May` and
> `potentially` are preserved; event timing does not prove attacker intent.

## Exposure and dependency preconditions

At safe abstraction, the notification associates initial access or secondary
infection with known-but-unpatched common software weaknesses, shared network
resources and compromised managed services. These are exposure/dependency
classes, not a product advisory or a verified weakness inventory for every
affected cooperative.

> **Claim record — SRC-0038-C04 | source-report**
> **Claim:** The advisory reports three high-level exposure/dependency classes:
> unpatched known software weaknesses, shared-network-resource propagation and
> downstream exposure through compromised managed services.
> **Claim status:** active
> **Scope:** Source-reported classes across aggregated cases; no named product,
> identifier, configuration, exploitation sequence or current prevalence.
> **As of:** Cases since 2021, reported 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF p. 2, first paragraph under `Threat`.
> **Basis / limits:** The classes are direct but not case-by-case mappings.
> The wiki deliberately omits variant and exploit details.

## Observed operational outcomes

The source distinguishes outcomes. For some targeted entities, production was
slower because work shifted to manual operation or production halted. Other
entities lost only administrative functions such as websites and email, with
no production impact. Two reported February 2022 attempts were detected and
stopped before encryption. These differences prevent a claim that every
compromise produced a production or supply consequence.

> **Claim record — SRC-0038-C05 | source-report**
> **Claim:** Across the source-reported cases, some agricultural entities
> experienced slower manual processing or complete production halt, others
> lost administrative functions without production impact, and two attempts
> were stopped before encryption.
> **Claim status:** active
> **Scope:** Aggregated operational states reported by the FBI; not entity-
> specific loss magnitude, duration, independent verification, biological
> harm or sector-wide outcome.
> **As of:** Events in 2021–March 2022, reported 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF p. 2, `Threat` and event bullets.
> **Basis / limits:** Outcome distinctions are direct. Anonymous reporting and
> missing denominators preclude rate, causality-strength or prevalence claims.

## Event aggregation and supply dependencies

The source reports six cooperative attacks between 15 September and 6 October
2021, a July 2021 business-software compromise that led to secondary
infections among clients including cooperatives, two stopped attempts in
February 2022, and a March 2022 event affecting a multi-state grain company.
For the March company, the source identifies grain processing plus seed,
fertilizer and logistics services as important planting-season dependencies.

This chronology is retained only at aggregate level. Named malicious-software
families and ransom amounts add no defensive value to the wiki's current
criterion and are not reproduced.

> **Claim record — SRC-0038-C06 | source-report**
> **Claim:** The notification aggregates several 2021–2022 event clusters and
> directly places grain processing, seed, fertilizer and logistics services in
> a planting/harvest production-and-supply dependency context.
> **Claim status:** active
> **Scope:** Source chronology and sector dependencies; not distinct wiki
> incidents, complete case histories, attribution, affected-asset topology or
> independent consequence confirmation.
> **As of:** Events from July 2021 through March 2022.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF pp. 1–2, Summary and event bullets.
> **Basis / limits:** Dates and dependencies are direct. All cases remain one
> anonymous/source-reported advisory lineage for evidence-floor purposes.

## Conditional downstream cascades

The advisory separately describes possible broader cascades: severe grain
disruption could affect human food, animal feed and commodities; disruption at
protein or dairy processing could spoil product and pressure farms when
animals cannot be processed. It does not say those outcomes occurred in the
reported cooperative cases.

> **Claim record — SRC-0038-C07 | source-report**
> **Claim:** The FBI identifies conditional cyber→agricultural production→
> food/feed/trading or processor→spoilage/farm-pressure cascades, but the
> notification does not report those downstream biological, animal, plant or
> ecological outcomes as observed in its cases.
> **Claim status:** active
> **Scope:** Prospective consequence model in the advisory; not a realized
> event path, causal estimate, loss amount or evidence of animal/plant harm.
> **As of:** 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF p. 2, second paragraph under `Threat`.
> **Basis / limits:** Modal language is preserved. Observed operational
> disruption and prospective downstream cascade are not merged.

## Recommended resilience and recovery controls

The notification recommends layered ransomware safeguards. At high level they
cover protected/offline backups; a separated recovery plan; critical-function
identification and manual continuity; segmentation; patch/update management;
multi-factor authentication and least privilege; remote-access monitoring;
endpoint safeguards; awareness/training; assessment and reporting resources.

> **Claim record — SRC-0038-C08 | source-report**
> **Claim:** The advisory supplies agriculture-relevant prevention, access,
> segmentation, monitoring, protected-backup, manual-continuity, reporting and
> recovery recommendations.
> **Claim status:** active
> **Scope:** High-level recommended control functions; no configuration,
> deployment, test, adoption denominator, interrupted event or effectiveness.
> **As of:** 2022-04-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF pp. 3–4, `Recommendations`, `Additional Resources` and
> `Reporting Notice`.
> **Basis / limits:** Recommendation status is direct. The advisory does not
> show that any named safeguard produced the stopped-attempt outcomes.

## Integration and score boundary

The source supports a generic ransomware threat, high-level agriculture IT
exposures, an observed cyber→availability→manual-operation/production-halt
limb, conditional supply cascades and explicit defensive/recovery controls. It
does not independently close an SF2 criterion because it is one lineage, and
it does not provide a primary independently contextualised material-economic
consequence study or observed animal/plant/ecosystem outcome.

> **Claim record — SRC-0038-C09 | analytic-judgment**
> **Claim:** `SRC-0038` strengthens candidate evidence for `AGE-TV`, `AGE-XT`
> and `AGE-CT` but alone changes no frozen cell: independent synthesis and
> additional lineages remain required, while `AGE-CI` receives no qualifying
> observed consequence from this package.
> **Claim status:** active
> **Scope:** Wiki after draft integration of one source transaction; no score
> transition and no conclusion about adjacent AGE cells.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0038-C02`–`C08`; frozen AGE criteria/source floors in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** This package contributes direct pieces but not source-
> floor independence, observed biological consequence or effectiveness.

> **Claim record — SRC-0038-C10 | analytic-judgment**
> **Claim:** The integrated source page remains defensive: it omits variants,
> product/exploit identifiers, indicators, operational intrusion procedure and
> affected-entity identities while preserving evidence needed for threat,
> consequence and control reasoning.
> **Claim status:** active
> **Scope:** Local page content, not a redaction certification of the raw
> public artifact.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content compared with complete PDF review.
> **Basis / limits:** The immutable raw source remains public and more detailed;
> the wiki does not reproduce its operationally unnecessary detail.

## Limitations and conflicts

- The notification is an agency advisory, not a peer-reviewed or independent
  empirical investigation.
- Most entities are anonymous; event and outcome detail is incomplete.
- It gives no denominator, duration, loss estimate or measured food-supply
  effect and does not independently validate the underlying reports.
- Reported stopped attempts are not attributed to a particular recommended
  control and therefore are not control-effectiveness evidence.
- Potential animal-feed, spoilage and farm cascades are prospective.
- Current actor prevalence, affected software and control adoption are unknown.

## Integration map

- [TEC-0003](../techniques/tec-0003-ransomware-availability-and-extortion-agriculture.md)
- [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md)
- [VUL-0002](../vulnerabilities/vul-0002-agriculture-it-access-and-dependency-exposures.md)
- [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [CTL-0018](../controls/ctl-0018-agriculture-cyber-resilience-and-recovery-controls.md)
- [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [CTL-0005](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [SYN-0001](../syntheses/syn-0001-coverage-rubric.md)
- [SYN-0025](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)
- [SYN-0027](../syntheses/syn-0027-canada-agriculture-cyber-animal-effect-reconciliation.md)
