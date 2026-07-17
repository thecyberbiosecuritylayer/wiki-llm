---
id: INC-0001
type: incident
title: Synnovis cyberattack and transfusion-service disruption
aliases:
  - June 2024 Synnovis laboratory disruption
  - south London transfusion compatibility disruption
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
event_date: 2024-06-03
source_ids:
  - SRC-0008
  - SRC-0009
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: INC-0001-C01
    evidence:
      - source: SRC-0008
        locator: "pp. 21–22 and 97; contextual pp. 44 and 92"
  - predicate: evidenced-by
    target: SRC-0009
    claim_id: INC-0001-C04
    evidence:
      - source: SRC-0009
        locator: "article update paragraphs 2–4 and subsequent status sections; HTML lines 190–200"
  - predicate: affects
    target: AST-0002
    claim_id: INC-0001-C02
    evidence:
      - source: SRC-0008
        locator: "pp. 21–22 and 97"
  - predicate: depends-on
    target: WFL-0006
    claim_id: INC-0001-C02
    evidence:
      - source: SRC-0008
        locator: "pp. 10, 21–22, 92, 97 and 124"
  - predicate: depends-on
    target: SYS-0004
    claim_id: INC-0001-C02
    evidence:
      - source: SRC-0008
        locator: "pp. 21–24, 92 and 97"
tags:
  - documented-incident
  - transfusion
  - laboratory-systems
  - blood-supply
  - clinical-continuity
  - ransomware
  - data-breach
---

# Synnovis cyberattack and transfusion-service disruption

> [!WARNING]
> **Evidence classification**
> Documented real event supported by two official institutional disclosures.
> NHS England is primary for its public chronology, aggregate delays, recovery
> statement and data-response process; NHSBT is primary for its response and
> observed blood-supply effects. They are separate issuers in the same NHS
> response ecosystem, not independent forensic investigations.

## Event and timeline

| Date | Event state | Evidence boundary |
| --- | --- | --- |
| 2024-06-03 | NHS England reports a ransomware cyberattack that significantly reduced Synnovis test-processing capacity; NHSBT separately reports disrupted access to grouping, antibody-screening and crossmatch systems in June | Exact discovery time, initial-access vector and technical mechanism remain unknown |
| 2024-06 onward | NHSBT RCI scales operations, extends hours and prioritizes urgent cases; hospitals rely more heavily on O-negative units | Exact duration and case volumes not reported |
| 2024-06-20 | NHS England reports that stolen files were published | Specific data fields, record count and final affected-person scope are not reported |
| 2024-06-25 | Official NHS England API metadata dates publication of its page to this day | This is a page-publication date, not necessarily the first incident disclosure by any party |
| 2024 summer | Increased O-negative demand contributes to an amber stock alert | Report does not isolate all alert causes/costs to this incident |
| By 2024-12 | NHS England states that services were fully restored after specialist support and IT-infrastructure rebuilding | Exact completion day, restored-component inventory and independent acceptance criteria are absent |
| 2025-07-17 | NHSBT annual report is published on GOV.UK | Publication date is not event/discovery/disclosure date |
| 2025-11-10 | Displayed NHS England update says customer attribution of fragmented stolen material was complete and customer/individual review was continuing | It is not the first incident-disclosure date or a final notification count |

> **Claim record — INC-0001-C01 | source-report**
> **Claim:** NHSBT reports that a June 2024 cyberattack on Synnovis disrupted
> access to critical laboratory systems for blood grouping, antibody screening
> and crossmatching in affected London services.
> **Claim status:** active
> **Scope:** Existence and stated service impact of the event, not actor,
> technical cause, data breach or patient injury.
> **As of:** 2024-06.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–22 and 97.
> **Basis / limits:** NHSBT was operationally involved in the response and
> directly states the disruption. Pages 22 and 97 are near-verbatim duplicates,
> not two sources; no Synnovis forensic artifact is present.

## Discovery date

**Unknown.** Neither current source states when Synnovis or another party first
detected the compromise relative to the 2024-06-03 event date.

## Public-disclosure date

**Unknown.** Neither archived source establishes the first public notice. The
2024-06-20 publication of stolen files is recorded separately and must not be
substituted for an official disclosure date.

## Source publication dates

- `SRC-0008`: NHS Blood and Transplant Annual Report and Accounts 2024–25,
  published 2025-07-17, reporting period ending 2025-03-31.
- `SRC-0009`: NHS England page published 2024-06-25 and modified 2025-11-10
  according to its official API metadata; the archived HTML itself displays
  only the 2025-11-10 update date.

No claim is made that either source supplies the first public-disclosure date.
The date on which stolen files were published is a confidentiality-event date,
not the date on which the incident was first publicly disclosed.

## Affected assets and services

- access to laboratory functions for grouping, antibody screening and
  crossmatching;
- hospital compatibility-testing capacity;
- NHSBT RCI specialist service capacity;
- O-negative blood-component availability and wider stock resilience;
- emergency and surgical transfusion continuity.
- wider pathology test-processing capacity and delayed outpatient/elective
  appointments;
- stolen, published files and the later customer/possible-person
  identifiability review, with exact data classes still unknown.

Neither source says NHSBT HAEMATOS was attacked or identifies a compromised
product. `SRC-0009` does not establish that every stolen file was a patient
record, pathology result or genomic datum.

## Confirmed impact

Confirmed as **source-reported operational facts**:

- an NHS England-classified ransomware attack on 2024-06-03 and significant
  reduction of Synnovis test-processing capacity;
- delays to more than 11,000 outpatient/elective-procedure appointments;
- loss of access to the named laboratory-system functions;
- urgent NHSBT RCI surge activity and extended hours;
- greater hospital reliance on O-negative products;
- sustained demand/limited-stock pressure contributing to an amber alert;
- extra internal NHSBT activity;
- publication of stolen files on 2024-06-20 and a later customer/possible-
  individual impact-review process;
- source-reported full service restoration by December 2024.

> **Claim record — INC-0001-C02 | source-report**
> **Claim:** The incident crossed from digital service availability into
> specialist laboratory workload and biological-product demand, with increased
> O-negative reliance contributing to an amber stock alert.
> **Claim status:** active
> **Scope:** NHSBT-observed downstream states; not a claim that stock was
> exhausted or a patient was injured.
> **As of:** 2024-06.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–22 and 97; contextual business-continuity account p. 92.
> **Basis / limits:** The transitions are explicitly reported. Demand quantity,
> backlog, stock trajectory, case-level delay/injury and share of alert cost
> attributable to this event are not reported; p. 92 does not name Synnovis.

Not confirmed by the current source:

- death, injury or incompatible transfusion caused by the event;
- exhaustion of O-negative stock;
- compromise of NHSBT systems or data;
- specific stolen-data fields, final record/person count or completed
  notification outcome;
- exact technical recovery boundary or independently validated restoration.

> **Claim record — INC-0001-C04 | source-report**
> **Claim:** NHS England reports that a ransomware cyberattack on 3 June 2024
> significantly reduced Synnovis test-processing capacity, while NHSBT
> separately reports the June cyberattack and its compatibility-system
> effects.
> **Claim status:** active
> **Scope:** Event existence, exact date and source classification; not the
> initial-access mechanism, ransomware family, root cause or actor identity.
> **As of:** 2024-06-03.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> article update paragraph 2, HTML line 190;
> [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 21–22 and
> 97.
> **Basis / limits:** Two distinct official issuers support the event and
> disruption. Only NHS England supplies the exact day and ransomware label;
> both are participants in the same NHS response ecosystem and neither source
> is a technical forensic investigation.

> **Claim record — INC-0001-C05 | source-report**
> **Claim:** NHS England reports delays to more than 11,000 outpatient and
> elective-procedure appointments and states that Synnovis services were fully
> restored by December 2024.
> **Claim status:** active
> **Scope:** Aggregate care-delivery delay and institution-reported restoration,
> not clinical injury or independently tested technical recovery.
> **As of:** 2024-12-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> article update paragraphs 2–3, HTML lines 190–191.
> **Basis / limits:** Threshold count and restoration month are explicit. No
> denominator, delay-duration distribution, clinical-outcome review, exact
> restoration day, component inventory or independent acceptance test is given.

> **Claim record — INC-0001-C06 | source-report**
> **Claim:** NHS England reports publication of stolen files on 20 June 2024 and
> a later process to associate fragmented material with customers and determine
> possible individual identifiability and notification needs.
> **Claim status:** active
> **Scope:** Observed confidentiality-response track through the 10 November
> 2025 update; not a final person/record count or specification of data types.
> **As of:** 2025-11-10.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> update paragraph 4 and the sections “What has happened since then?” and
> “What will happen next?”, HTML lines 192–200.
> **Basis / limits:** Publication and process states are direct. The page says
> the material was unstructured, incomplete and fragmented; it does not list
> fields, confirm that every record identifies a person or report a final
> notification outcome.

## Reported vector

**Initial-access vector: unknown.** `SRC-0009` classifies the event as a
ransomware cyberattack; `SRC-0008` says cyberattack. Neither identifies the
delivery method, ransomware family, exploited weakness, affected product,
host count or technical entry sequence. Attack class is not an access vector.

## Suspected cause

No root cause beyond the source-reported ransomware/cyberattack classification
is established. This page does not infer a product defect, configuration
weakness, insider action or supply-chain route.

## Actor attribution

**Unknown.** `SRC-0009` generically refers to criminals responsible for the
attack but names no person, group, sponsor or attribution confidence; `SRC-0008`
names no actor. No `THR` page is created from these sources.

## Cross-domain consequences

The documented transfer is:

`digital laboratory-system access loss → compatibility-testing capacity gap →
specialist contingency/product fallback → O-negative inventory pressure →
supply alert and potential patient-safety exposure`.

The patient-safety state is described as a **serious risk**. It is not a
confirmed injury and not a prevalence statement.

A separate confidentiality track is also observed:

`ransomware incident → file theft/publication → fragmented customer-scope
reconstruction → organization review for possible identifiability and
notification`.

That track is relevant to a pathology provider but does not establish a
biological change, patient injury, genomic-data exposure or the content of any
particular record. It is not merged into the O-negative supply path.

## Response and recovery

NHSBT reports that RCI:

- scaled operations;
- extended working hours;
- prioritized urgent cases;
- supported affected hospitals while NHSBT/NHS coordinated limited stock use.

The report states that clinicians could continue safe transfusion in emergency
and surgical settings and calls NHSBT a contingency during the south-London
LIMS event. This is bounded first-party evidence of implemented response and
source-reported continuity, not an independently measured recovery result.

> **Claim record — INC-0001-C03 | source-report**
> **Claim:** NHSBT implemented specialist surge/triage and stock-coordination
> measures and reports maintained continuity of transfusion care during the
> disruption.
> **Claim status:** active
> **Scope:** NHSBT response and management conclusion for this event; no claim
> about complete Synnovis recovery or every affected patient.
> **As of:** 2024-06.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 22 and 97; p. 92.
> **Basis / limits:** Actions are direct and high-confidence; effectiveness
> confidence is medium because there are no outcome metrics, counterfactual,
> independent evaluation or bounded harm review. Pages 22/97 are duplicates.

NHS England separately reports that Synnovis engaged specialist support,
dedicated resources to service restoration and IT-infrastructure rebuilding,
and had fully restored services by December 2024
([SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md), article update
paragraphs 3–4). This is a provider-level management statement; the exact day,
technical recovery sequence, acceptance criteria and independent validation
remain absent. NHSBT continuity during the disruption and later Synnovis
restoration are distinct states.

## Defensive lessons

- Clinical laboratory cyber availability can propagate into biological
  inventory, not only appointment delay.
- Alternate specialist capacity needs explicit activation, prioritization and
  responsibility boundaries.
- Fallback product use must be evaluated as a constrained material resource.
- A responder can preserve care while accumulating staff/supply burden; both
  need measurement.
- Recovery assurance must validate identity, result integrity and decision
  fitness, not only service availability.
- First-party success statements need independent outcome evidence.

## Evidence and uncertainty

| Element | Current confidence | Reason |
| --- | --- | --- |
| Event existence and broad disruption | High | Two distinct official institutional accounts; shared response ecosystem |
| Exact date and ransomware classification | High as source report | Direct NHS England statement; no forensic artifact |
| NHSBT actions | High | First-party implementation account |
| O-negative/amber-alert path | High as source report | Direct NHSBT account; repeated pages are an internal duplicate |
| More than 11,000 delayed appointments | High as source report | Direct NHS England aggregate; no denominator or clinical follow-up |
| Stolen-file publication and review process | High as source report | Direct NHS England chronology; exact data/person scope absent |
| Continuity effectiveness | Medium | Management conclusion without metrics/independent evaluation |
| Patient injury | Unknown/not established | Source reports risk, not injury |
| Actor/initial-access vector/vulnerability | Unknown | Not disclosed |
| Service restoration by December 2024 | High as source report; independent assurance unknown | Provider-level statement via NHS England, without acceptance criteria |

The next needed evidence is a victim technical record, ICO/regulator outcome,
independent recovery validation and bounded clinical-outcome review. Repeated
institutional updates cannot substitute for those evidence classes.

## Related pages

- [SYN-0023 — Laboratory continuity reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [SYN-0022 — Foundational consequence/assurance calibration](../syntheses/syn-0022-foundational-consequence-assurance-calibration.md)

- [RSK-0006 — Compatibility-system disruption and blood-supply pressure](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md)
- [CTL-0004 — Transfusion-service continuity response](../controls/ctl-0004-transfusion-service-continuity-response.md)
- [AST-0002 — Transfusion compatibility information and blood-product availability](../assets/ast-0002-transfusion-compatibility-and-blood-products.md)
- [WFL-0006 — Transfusion compatibility testing and blood issue](../workflows/wfl-0006-transfusion-compatibility-and-blood-issue.md)
- [SYS-0004 — Transfusion laboratory information systems](../systems/sys-0004-transfusion-laboratory-information-systems.md)
- [SRC-0008 — NHSBT Annual Report 2024–25](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0009 — NHS England Synnovis update](../sources/src-0009-nhs-england-synnovis-update-2025.md)

## Sources

- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 21–22,
  44, 92 and 97.
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md), article
  update paragraphs 1–4 and subsequent status sections, HTML lines 188–200.
