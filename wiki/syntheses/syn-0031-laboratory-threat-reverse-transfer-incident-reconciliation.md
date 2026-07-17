---
id: SYN-0031
type: synthesis
title: Laboratory threat breadth and reverse-transfer incident reconciliation
aliases:
  - LAB-TV and THI-XT reconciliation
  - Immensa HSE laboratory threat directionality audit
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0004
  - SRC-0008
  - SRC-0009
  - SRC-0019
  - SRC-0022
  - SRC-0026
  - SRC-0039
  - SRC-0040
  - SRC-0042
  - SRC-0046
  - SRC-0047
  - SRC-0057
  - SRC-0058
sensitivity: public
dual_use: low
relations:
  - predicate: depends-on
    target: SYN-0001
    claim_id: SYN-0031-C12
    evidence:
      - source: SRC-0057
        locator: "Frozen rubric current LAB-TV/THI-XT rows and recalculated checkpoint SYN-0001-C51 before this transaction"
  - predicate: evidenced-by
    target: SRC-0057
    claim_id: SYN-0031-C04
    evidence:
      - source: SRC-0057
        locator: "SUI Executive summary, §§1.2, 3.1, 3.3 and 4; UKHSA and Warwick impact-analysis roles/limits"
  - predicate: evidenced-by
    target: SRC-0058
    claim_id: SYN-0031-C03
    evidence:
      - source: SRC-0058
        locator: "HSE ED03-2024 and HID 5-2011 issue, investigation, system-exposure and action sections"
  - predicate: depends-on
    target: THR-0005
    claim_id: SYN-0031-C03
    evidence:
      - source: SRC-0004
        locator: "WHO malicious/insider/supply threat and control classes, §§5–7"
      - source: SRC-0019
        locator: "CBS requirement 4.1.8 and adjacent programme/role requirements"
  - predicate: depends-on
    target: HAZ-0006
    claim_id: SYN-0031-C03
    evidence:
      - source: SRC-0057
        locator: "Observed accidental configuration error"
      - source: SRC-0058
        locator: "Investigated missing-context and containment-exposure hazards"
  - predicate: depends-on
    target: VUL-0006
    claim_id: SYN-0031-C03
    evidence:
      - source: SRC-0057
        locator: "Event-specific monitoring, assurance and incident-governance weaknesses"
      - source: SRC-0058
        locator: "Concrete context-capture, visibility, linkage and alert exposures"
  - predicate: depends-on
    target: INC-0008
    claim_id: SYN-0031-C04
    evidence:
      - source: SRC-0057
        locator: "INC-0008-C01–C09; one observed non-malicious event and evidence-state limits"
  - predicate: depends-on
    target: RSK-0021
    claim_id: SYN-0031-C04
    evidence:
      - source: SRC-0057
        locator: "RSK-0021-C01/C02/C05; observed input→digital-result→decision path"
  - predicate: depends-on
    target: CTL-0023
    claim_id: SYN-0031-C07
    evidence:
      - source: SRC-0057
        locator: "CTL-0023-C01–C07; incident exact-edge controls and effectiveness limits"
      - source: SRC-0058
        locator: "HSE context/linkage/alert/containment-decision controls"
tags:
  - laboratory
  - threat-model
  - incident
  - reverse-transfer
  - directionality
  - public-health
  - evidence-reconciliation
---

# Laboratory threat breadth and reverse-transfer incident reconciliation

## Decision scope and frozen pre-state

This synthesis adjudicates only `LAB-TV`, `THI-XT` and the global
directionality gate. It does not reopen already passed cells, lower source
floors or convert implementation into effectiveness.

`SYN-0031-C01` is superseded because its pre-state included a rubric unit
retired from the public corpus.

> **Claim record — SYN-0031-C12 | artifact-observation**
> **Claim:** Before this transaction the recalculated public wiki has 96 Pass,
> 11 Partial, and 3 Absent cells, or 96/110 (87.3%), with dimension vector
> `10/9/5/8/8/8/10/10/9/9/10`, critical cells 82/8/1, seven dimensions
> at least 9/10, and global gates at 8 Pass/4 Fail.
> **Evidence:** [SYN-0001](syn-0001-coverage-rubric.md), recalculated
> checkpoint `SYN-0001-C51`;
> [SYN-0030](syn-0030-23andme-genomic-incident-governance-reconciliation.md),
> `SYN-0030-C13`–`C15`.
> **Limits:** This is public-corpus checkpoint arithmetic, not absolute domain
> completeness.

## Evidence roles and non-duplication

| Evidence role | Lineage | Counting boundary |
| --- | --- | --- |
| global laboratory threat/hazard taxonomy | WHO 2024 | one normative lineage; no event/adoption |
| Canadian national facility programme | CBS Third Edition | independent national requirement lineage |
| biobank inventory/supply/continuity context | NCI best practices | official voluntary U.S. lineage |
| concrete exposure investigation summary | HSE 2011/2024 | one evolving UK regulator lineage; unnamed occasions not INC count |
| primary reverse-transfer incident | UKHSA SUI | one event; operationally separate panel inside same agency |
| issuer impact analysis | UKHSA preprint | different method, same institution; modelled outcomes |
| external impact context | Warwick working paper | one independent institution; not another incident investigation |

> **Claim record — SYN-0031-C02 | analytic-judgment**
> **Claim:** The package meets claim-specific SF2/SF3 independence without
> inflating pages or teams: WHO, CBS/NCI and HSE are materially distinct
> taxonomy/regulatory lineages; the SUI is the primary incident record; UKHSA
> impact modelling remains same-institution; Warwick adds independent
> directional context but not a second event or forensic investigation.
> **Claim status:** active
> **Scope:** Evidence-role accounting for the two candidate cells; not equal
> source weight or independent replication of every incident estimate.
> **As of:** Full package review 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0057-C01/C02/C06/C07`; `SRC-0058-C01/C02/C07`;
> `SRC-0004-C01/C11`; `SRC-0019-C01/C08`; `SRC-0022-C01/C09`.
> **Basis / limits:** Issuer, genre, method and event identity remain separate
> predicates.

## Laboratory threat and vulnerability corpus — `LAB-TV`

| Literal criterion limb | Canonical evidence | State boundary |
| --- | --- | --- |
| malicious | `THR-0005`, WHO unauthorized/misuse/theft/diversion classes | normative, not current incident |
| insider | WHO personnel-risk + CBS personnel-security/accountability roles | position does not imply motive |
| accidental | `HAZ-0006`, Immensa configuration error, HSE context failures | observed/investigated, non-malicious |
| environmental | WHO facility/utility/natural-event + NCI storage/alternate-capability context | generic source-supported |
| inventory | WHO/CBS accountability + NCI inventory/check/recovery context | generic source-supported |
| supply | WHO provider/service + NCI reagent/service/continuity + NIST third-party context | generic source-supported |
| specific exposures | HSE context capture/visibility/linkage/alerts; UKHSA monitoring/assurance/configuration | concrete, event/investigation-bounded |

> **Claim record — SYN-0031-C03 | analytic-judgment**
> **Claim:** `LAB-TV` passes at SF2: `THR-0005/HAZ-0006/VUL-0006` cover every
> literal malicious, insider, accidental, environmental, inventory and supply
> limb plus concrete HSE/UKHSA information, configuration, monitoring and
> containment exposures across materially independent WHO, HSE, CBS/NCI and
> incident roles.
> **Claim status:** active
> **Scope:** Complete defensive threat-model breadth for represented laboratory/
> biobank contexts; not prevalence, a named malicious incident, implementation
> census or guarantee every context has every class.
> **As of:** 2026-07-12 corpus.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§5.1, 5.3.1–5.3.6 and 6.4–6.6, printed pp. 19–39/PDF pp. 39–59;
> [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> requirement 4.1.8 and adjacent programme/role requirements, pp. 84–91;
> [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§B.5, C.2.6, C.3.2 and C.4.2–C.4.4, printed pp. 32–40 and 56–65;
> [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> pp. 61–72, 89–100 and 193–207; [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md),
> SUI Executive summary ¶¶4, 8–16 and §§2.6, 3.4 and 4, pp. 8–11 and
> 45–63; [SRC-0058](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md),
> ED03-2024 `Issue`, `Outline`, multiple-sample and record/IT sections and HID
> 5-2011 `Key Issues`/`Background`. `THR-0005/HAZ-0006/VUL-0006` are the
> canonical graph pages; the exact frozen criterion is in `SYN-0001`.
> **Basis / limits:** All literal classes, specific exposures and SF2 are
> direct/reconciled. Generic classes are not silently promoted to events.

## Primary incident reverse direction — `THI-XT`

The accepted reverse path is:

`biological test input → laboratory measurement/configured classification →
digital result → person/public-health isolation and tracing decision state →
modelled population-level transmission consequence`

The already audited public corpus supplies four primary-supported forward paths
across three sectors. This transaction adds the missing primary incident direction
rather than re-counting those paths.

| Sector | Primary-supported forward path | Direction/evidence boundary |
| --- | --- | --- |
| LAB | Synnovis, `INC-0001-C01/C02/C04` | cyber→laboratory/transfusion continuity |
| AGE | JBS, `INC-0004-C01/C02/C07` | cyber→livestock-processing continuity |
| AGE | anonymous poultry account, `INC-0005-C01`–`C04` | source-reported cyber→animal effect; assurance limits retained |
| BMO | Merck, `INC-0006-C01/C03/C04` | cyber→manufacturing/product-supply state |

The 23andMe privacy impact is not treated as a biological direction.

> **Claim record — SYN-0031-C04 | analytic-judgment**
> **Claim:** `THI-XT` passes at SF3: the pre-existing primary incident corpus
> retains at least three-sector cyber→biological/operational forward transfer,
> and `INC-0008/RSK-0021` now supplies the missing primary material/input→
> digital-result→decision path with an official investigation, independent
> directional context and explicit ecological/outcome limits.
> **Claim status:** active
> **Scope:** Frozen cross-sector incident-direction criterion; not a malicious
> reverse path, person-level outcome, representative incidence or control
> effectiveness result.
> **As of:** Incident corpus 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Forward corpus: [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–22 and 97, and [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> update paragraphs 2–4;
> [SRC-0039](../sources/src-0039-usda-ers-jbs-cyberattack-cattle-slaughter-2021.md),
> pp. 2–3, and [SRC-0040](../sources/src-0040-fbi-statement-jbs-cyberattack-2021.md),
> complete substantive paragraph; [SRC-0042](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md),
> official transcript, `scariest example` question and response;
> [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md), Form 10-K
> displayed pp. 25, 38 and 41, and [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md),
> pp. 7–10. Reverse path: [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md),
> SUI Executive summary ¶¶3–5; §2.6.7, printed p. 45; §3.1.1, p. 51;
> UKHSA preprint Introduction/Methods, p. 2. The incident/RSK claim IDs in the
> table and `INC-0008-C01–C09`/`RSK-0021-C01/C02/C05/C06` are canonical
> navigation; the frozen current `THI-XT` row supplies the acceptance contract.
> **Basis / limits:** The new input→digital result/decision direction is
> observed through the result node; downstream population effects are modelled
> and never converted into individual observations.

## Global directionality gate

> **Claim record — SYN-0031-C05 | analytic-judgment**
> **Claim:** The global directionality gate changes Fail→Pass: previously
> accepted cyber→biological paths remain corroborated, and the Immensa primary
> incident now supplies the required biological/material/input→digital-
> decision direction while privacy-only and non-cyber states remain separate.
> **Claim status:** active
> **Scope:** Frozen global gate 6; not universal bidirectionality in every
> sector or a claim both directions share mechanism, intent or consequence.
> **As of:** 2026-07-12 corpus.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Cyber→biological/operational direction: [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–22 and 97; [SRC-0039](../sources/src-0039-usda-ers-jbs-cyberattack-cattle-slaughter-2021.md),
> pp. 2–3; [SRC-0042](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md),
> official transcript incident passage; [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md),
> displayed pp. 25, 38 and 41. Biological/material/input→digital-decision
> direction: [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md),
> SUI Executive summary ¶¶3–5, §2.6.7 printed p. 45 and §3.1.1 p. 51;
> UKHSA preprint Introduction/Methods, p. 2. `SYN-0031-C04` and the frozen
> global directionality gate in [SYN-0001](syn-0001-coverage-rubric.md)
> provide reconciliation and the acceptance contract.
> **Basis / limits:** Both required directions and evidence predicates now
> exist. Directional existence is not frequency or causal equivalence.

## Incident count and control-state nonpromotions

> **Claim record — SYN-0031-C06 | analytic-judgment**
> **Claim:** `INC-0008` is distinct in organization, date, cause and affected
> system from the prior six-event lower bound, so seven public INC/review pages
> now support at least seven distinguishable events; `THI-WL/CI` were already Pass
> and gain no additional point, while HSE's unnamed exposure occasions are not
> multiplied into incidents.
> **Claim status:** active
> **Scope:** Conservative event identity and adjacent-cell accounting; not
> eight distinct events or a prevalence census.
> **As of:** 2026-07-12 corpus.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0030-C04/C05`; `INC-0008-C01/C02`; `SRC-0058-C02/C06`.
> **Basis / limits:** Aggregate review units are not multiplied into events,
> and HSE gives no event identities or count.

> **Claim record — SYN-0031-C07 | analytic-judgment**
> **Claim:** `CTL-0023` maps preventive, detective, containment/correction,
> recovery and assurance functions to the exact failed/interrupted edges, but
> issuer-reported implementation and regulator-directed actions lack an
> independent outcome test; `LAB-AE`, `CTR-AE` and the global control gate
> remain unchanged.
> **Claim status:** active
> **Scope:** Control-lesson contribution and evidence-state boundary.
> **As of:** Full transaction review 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [CTL-0023](../controls/ctl-0023-laboratory-result-validation-anomaly-detection-and-containment-controls.md),
> `CTL-0023-C01`–`C07`; `SRC-0057-C09/C10`; `SRC-0058-C05/C07`.
> **Basis / limits:** Exact edges and control states are direct; causal
> effectiveness predicates are absent.

## Accepted transitions and resulting state

> **Claim record — SYN-0031-C08 | analytic-judgment**
> **Claim:** Independent strict review supports exactly two cell transitions:
> `LAB-TV` and `THI-XT` change Partial→Pass; no other rubric cell changes.
> **Claim status:** active
> **Scope:** Frozen 110-cell rubric transaction; Partial/Absent still earn zero.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0031-C02`–`C07`; exact frozen criteria/source floors;
> independent LAB-source and Immensa-locator audits completed 2026-07-12.
> **Basis / limits:** Threat breadth and incident direction meet their full
> contracts. Implementation, modelling or page volume creates no other point.

`SYN-0031-C09` is superseded because its pre-state included a rubric unit
retired from the public corpus.

> **Claim record — SYN-0031-C13 | artifact-observation**
> **Claim:** The two accepted transitions produce 98 Pass, 9 Partial, and
> 3 Absent cells, or 98/110 (89.1%), with dimension vector
> `10/9/5/9/8/8/10/10/10/9/10`, critical cells 84/6/1, eight dimensions
> at least 9/10, and global gates at 9 Pass/3 Fail.
> **Evidence:** `SYN-0031-C08/C12`; frozen dimension membership, critical
> flags, and global gates in [SYN-0001](syn-0001-coverage-rubric.md).
> **Limits:** Two Partial→Pass transitions add two points. The numeric gate
> still fails because every dimension must be at least 9 and every critical
> cell must pass; SEB is 5/10, BMO and CPH are 8/10, and seven critical cells
> remain open.

## Nonpromotions and safety

> **Claim record — SYN-0031-C10 | analytic-judgment**
> **Claim:** This transaction creates no transition for `LAB-AE`, `CPH-AE`,
> `CTR-AE` or any governance cell: modelled consequences are not measured
> safeguard effects, issuer implementation is not independent evaluation and
> HSE-directed action is not adoption evidence.
> **Claim status:** active
> **Scope:** Adjacent-cell and evidence-ladder audit.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0057-C06/C09/C10`; `SRC-0058-C05/C07`;
> `CTL-0023-C07`; frozen assurance criteria.
> **Basis / limits:** Consequence and safeguard-effectiveness predicates are
> distinct even when they concern the same event.

> **Claim record — SYN-0031-C11 | analytic-judgment**
> **Claim:** The transaction remains defensive: it exposes no pathogen
> sequence, assay setting, laboratory procedure, facility topology, personal
> record, exploit or evasion method and preserves observed, estimated,
> modelled, recommended and implemented evidence states.
> **Claim status:** active
> **Scope:** Transaction content and safety boundary.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Safety sections in `SRC-0057/0058`, `INC-0008`, `THR-0005`,
> `HAZ-0006`, `VUL-0006`, `RSK-0021` and `CTL-0023`.
> **Basis / limits:** High-level causal and defensive abstractions suffice for
> both rubric decisions.

## Related pages

- [SYN-0001 — Frozen rubric](syn-0001-coverage-rubric.md)
- [SYN-0003 — canonical transfer directions](syn-0003-cross-domain-transfer-directions.md)
- [SYN-0030 — prior checkpoint](syn-0030-23andme-genomic-incident-governance-reconciliation.md)
- [SRC-0057 — Immensa package](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md)
- [SRC-0058 — HSE exposure package](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md)
- [INC-0008 — incident](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md)
- [RSK-0021 — reverse path](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)
- [CTL-0023 — controls](../controls/ctl-0023-laboratory-result-validation-anomaly-detection-and-containment-controls.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md)
- [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0039](../sources/src-0039-usda-ers-jbs-cyberattack-cattle-slaughter-2021.md)
- [SRC-0040](../sources/src-0040-fbi-statement-jbs-cyberattack-2021.md)
- [SRC-0042](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md)
- [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md)
- [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md)
- [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md)
- [SRC-0058](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md)
