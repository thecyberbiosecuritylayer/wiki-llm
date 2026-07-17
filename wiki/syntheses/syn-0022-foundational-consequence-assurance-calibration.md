---
id: SYN-0022
type: synthesis
title: Foundational consequence and assurance calibration
aliases:
  - FND-CI AE calibration
  - Cross-sector consequence and evidence ladder
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0004
  - SRC-0008
  - SRC-0009
  - SRC-0014
  - SRC-0017
  - SRC-0018
  - SRC-0029
  - SRC-0030
  - SRC-0034
  - SRC-0035
sensitivity: public
dual_use: low
jurisdictions:
  - Global
  - United Kingdom
  - United States
relations:
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: SYN-0022-C01
    evidence:
      - source: SRC-0008
        locator: "Primary NHSBT Synnovis-related disruption, pressure, response and assurance boundary, SRC-0008-C03/C04/C08; annual report pp. 21-22 and 97; financial context p. 44; continuity/assurance pp. 92 and 104-105"
  - predicate: evidenced-by
    target: SRC-0009
    claim_id: SYN-0022-C01
    evidence:
      - source: SRC-0009
        locator: "NHS England Synnovis attack, test-capacity/delay, stolen-file/publication-notification and restoration chronology, current page sections retained in SRC-0009-C02–C06"
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: SYN-0022-C01
    evidence:
      - source: SRC-0014
        locator: "Controlled cross-sample read-exposure/misassignment result and boundary, SRC-0014-C04/C08, paper §5, printed pp. 772-773/PDF pp. 9-10"
  - predicate: evidenced-by
    target: SRC-0029
    claim_id: SYN-0022-C01
    evidence:
      - source: SRC-0029
        locator: "National Patient Safety Alert error class, fatal-outcome review context and required-action design, SRC-0029-C04–C08, physical PDF pp. 1-2 and matching long-read HTML headings"
  - predicate: evidenced-by
    target: SRC-0030
    claim_id: SYN-0022-C01
    evidence:
      - source: SRC-0030
        locator: "HSSIB lineage independence, method, EPR findings/recommendations and evidence limits, SRC-0030-C04/C05/C08–C11, physical pp. 2-29 and 36-50"
  - predicate: evidenced-by
    target: SRC-0034
    claim_id: SYN-0022-C01
    evidence:
      - source: SRC-0034
        locator: "Primary ProteinGym benchmark task/split/metric results, positive comparisons, failure/generalizability limits and evaluator overlap, SRC-0034-C03–C09"
  - predicate: evidenced-by
    target: SRC-0035
    claim_id: SYN-0022-C01
    evidence:
      - source: SRC-0035
        locator: "Primary APHA all-negative H5N1 field survey plus RAND implementation/evaluation limits, SRC-0035-C02–C09"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: SYN-0022-C04
    evidence:
      - source: SRC-0004
        locator: "Recommended WHO laboratory-biosecurity governance/control functions and evidence-state limits, §§4-8, PDF pp. 32-71"
  - predicate: evidenced-by
    target: SRC-0017
    claim_id: SYN-0022-C04
    evidence:
      - source: SRC-0017
        locator: "FDA device-security lifecycle/control/test/recovery design and implementation/effectiveness boundary, SRC-0017-C05–C09, physical pp. 5-57"
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: SYN-0022-C04
    evidence:
      - source: SRC-0018
        locator: "NIST OT recommended architecture/control/testing/recovery functions and non-implementation boundary, SRC-0018-C05–C08, §§3-6 and appendices"
tags:
  - foundations
  - consequences
  - incidents
  - assurance
  - effectiveness
  - empirical-calibration
  - evidence-ladder
---

# Foundational consequence and assurance calibration

## Exact question and evidence counting

This synthesis tests `FND-CI` and `FND-AE` at SF3. It does not reclassify the
global incident/control gates or any sector `CI/AE` cell. The consequence
taxonomy is calibrated by primary operational-event and controlled-study
records plus claim-appropriate independent context. The assurance ladder is
calibrated by distinct recommended, implemented, tested and independently
evaluated states; it keeps the `effective` rung explicitly unestablished where
no qualifying causal result exists.

NHSBT and NHS England are distinct organizations with different roles in the
same Synnovis event ecosystem, not two independent incidents. The national
alert and HSSIB thematic review have materially different national-review and
system-evaluation roles; neither is treated as a retained primary individual
case record. ProteinGym is one
author-team benchmark lineage;
NASEM citation is not counted as replication. PATH-SAFE's APHA null survey and
commissioned RAND evaluation have different roles but do not create independent
laboratory replication or a control-failure result.

> **Claim record — SYN-0022-C01 | analytic-judgment**
> **Claim:** The calibration groups same-event/programme records correctly and
> uses materially independent national-review, thematic-evaluation,
> controlled-study, benchmark and field-survey lineages only for their direct
> consequence/evidence-state roles.
> **Claim status:** active
> **Scope:** SF3 provenance/counting for foundational `CI/AE`; not forensic
> independence, unique-patient proof, benchmark replication or safeguard-
> effectiveness confirmation.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Frontmatter sources/locators; current
> [INC-0001](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md),
> [INC-0003](../incidents/inc-0003-national-allergy-recording-fatality-review-2021-2023.md),
> [SYN-0015](syn-0015-clinical-patient-outcome-systems-evaluation-reconciliation.md),
> `SYN-0015-C03/C04/C11/C12`; `SRC-0034-C08/C09`;
> `SRC-0035-C02/C05/C06/C08`.
> **Basis / limits:** Issuer/method/event relationships and independence limits
> are explicit. No record count is converted into an event/effect count.

## Potential-versus-observed consequence calibration

| Consequence class | Primary observed state | Potential/unestablished extension | Calibration boundary/context |
| --- | --- | --- | --- |
| Privacy | NHS England reports stolen Synnovis files were published and notification work; confidentiality loss is observed | identity theft, discrimination, individual clinical harm and exact affected data/person counts are not established in this package | separate NHSBT operational report supports event/service context but does not independently enumerate stolen files or person harm |
| Safety | a national alert reports a fatal medication-safety outcome within its aggregate review | a primary individual case record, exact digital root cause, unique-person count, single control failure and universal patient-risk rate remain unestablished | the thematic review supplies independent EPR system-class evaluation but does not confirm or reconstruct the reported outcome |
| Quality | controlled USENIX work observes/measures cross-sample read exposure/misassignment and provenance contamination under its tested setting | downstream clinical/research decision error or biological harm is not observed | the controlled study is primary; no independent replication or downstream outcome is ingested |
| Validity | ProteinGym directly measures task/split/metric-dependent model performance, comparative gains and failure/generalizability limits | deployment, clinical validity, universal model ranking and downstream biological benefit/harm are not established | evaluator/developer overlap and absent independent replication remain explicit |
| Resilience | NHSBT reports specialist workload/extended operations and blood-stock pressure; NHS England reports reduced test capacity, >11,000 delayed appointments and later restoration | patient injury, exact counterfactual delays, fully trusted recovery and independent restoration validation are unestablished | the two issuers corroborate one event ecosystem from different operational/national roles, not two incidents |

Potential consequences remain hypotheses or unmeasured extensions. Controlled
quality/validity effects are not relabelled as operational incidents; observed
service/privacy/safety states retain their different causal confidence and
units.

> **Claim record — SYN-0022-C02 | analytic-judgment**
> **Claim:** The taxonomy separates potential from observed privacy, safety,
> quality, validity and resilience effects and calibrates each with a primary
> event, adjudicated record or controlled empirical result plus explicit
> independence or missing-confirmation context and missing-outcome limits.
> **Claim status:** active
> **Scope:** Foundational consequence classes; not one shared causal scale,
> unique-event count, population rate, patient-injury claim for Synnovis,
> benchmark deployment or control effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0022-C01` and matrix above; `INC-0001-C01–C06`;
> `INC-0003-C01–C07`; `SYN-0015-C03/C04/C11/C12`;
> [HAZ-0001](../hazards/haz-0001-multiplex-sequencing-cross-sample-misassignment.md),
> `HAZ-0001-C01/C02`; `SRC-0034-C03–C08`.
> **Basis / limits:** Each required class has a direct primary/controlled state
> and its potential/unobserved boundary. Independent roles support the combined
> taxonomy at SF3 and are not treated as replication of every row.

> **Claim record — SYN-0022-C03 | analytic-judgment**
> **Claim:** `FND-CI` passes at SF3: a calibrated cross-sector primary-case
> corpus now distinguishes potential/observed effects across all five required
> consequence classes without merging service delay, technical quality,
> benchmark validity, privacy exposure or biological harm.
> **Claim status:** active
> **Scope:** Frozen foundational consequence criterion; not `THI-CI`, a global
> event-count gate, sector incident sufficiency or universal causality.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0022-C01/C02`; exact `FND-CI` criterion/source floor in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** All literal classes and SF3 primary-plus-independent-
> context requirements are satisfied at taxonomy level across the combined
> portfolio, not per example. This does not create missing cases for another
> cell.

## Assurance/effectiveness ladder calibration

| Evidence rung | Direct example | What can be concluded | What cannot be concluded |
| --- | --- | --- | --- |
| Recommended/design | WHO, FDA and NIST prescribe/recommend risk, lifecycle, architecture, testing, response/recovery and assurance functions | a control/evaluation design exists in a defined instrument scope | deployment, test result, benefit or compliance |
| Implemented | NHSBT reported operational continuity response and result-transfer changes after a real event | a named response or change was reported put into operation | successful test, causal prevention, or durable effectiveness; national-alert actions required of recipients remain design or required state, not implementation |
| Tested/empirical positive | ProteinGym reports measured comparative performance in specified task/split/metric conditions | a bounded empirical result exists under stated benchmark conditions | universal superiority, deployment or biological/clinical benefit |
| Tested failure/limit | ProteinGym documents split/task/generalization and method failure limits; controlled sequencing documents quality/exposure limits | bounded failure or non-generalization is observed in a test context | universal failure rate or downstream incident effect |
| Empirical null | APHA detected no H5N1 in the bounded survey and reports its sampling/design assumptions | a population/time/design-bounded biological null result exists | zero national risk, control success/failure or independent replication |
| Independently evaluated | HSSIB evaluates EPR system-class safety problems independently of individual implementations; RAND evaluates PATH-SAFE contribution/maturity but is commissioned | an independent or distinguishable evaluator role and scoped findings/limits exist | same-case safeguard effectiveness unless outcome, comparator and causal support are actually present |
| Effective | no retained example meets the full causal/comparative independently evaluated safeguard-effectiveness predicate | the absence of a qualifying example is visible and not silently filled | no control is labelled effective by recommendation, implementation, test, null or issuer restoration alone |

> **Claim record — SYN-0022-C04 | analytic-judgment**
> **Claim:** The calibrated ladder distinguishes recommended, implemented,
> tested, effective and independently evaluated states and contains bounded
> empirical positive, failure/limit and null examples without promoting any
> non-equivalent state to effectiveness.
> **Claim status:** active
> **Scope:** Foundational evidence-state vocabulary and examples; not sector
> safeguard effectiveness, compliance, benchmark deployment or a claim that a
> biological null is a control result.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0006](syn-0006-official-control-function-state-taxonomy.md),
> `SYN-0006-C01–C05`; `INC-0001-C03–C05`;
> `SRC-0034-C03–C08`; `SRC-0035-C05/C06/C08`; `SYN-0015-C04/C14`;
> source relations above.
> **Basis / limits:** The ladder and empirical states are direct across
> independent lineages. The empty effective rung is an explicit calibration
> boundary, not evidence that no effective safeguard exists externally.

> **Claim record — SYN-0022-C05 | analytic-judgment**
> **Claim:** `FND-AE` passes at SF3: the complete assurance ladder is calibrated
> with empirical positive, null and failure/limit examples drawn from materially
> independent lineages, while preserving the absence of a qualifying effective
> safeguard; no example is claimed independently replicated unless directly
> stated.
> **Claim status:** active
> **Scope:** Frozen foundational assurance/effectiveness criterion; not
> `CTR-AE`, any sector `AE`, a control-gate pass or external absence claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0022-C01/C04`; exact `FND-AE` criterion/source floor in
> `SYN-0001`; independent evaluation and empirical source roles above.
> **Basis / limits:** The literal ladder and example classes meet SF3 at the
> foundational calibration level. Effectiveness remains a distinguished rung,
> not a required positive example under the frozen wording.

## Non-promotions and strict score decision

`FND-TV` remains Partial because a complete evidence-backed threat/hazard/
technique/vulnerability/exposure distinction is not present in at least three
sectors. `THI-CI`, `CTR-AE`, `GEN-CI/AE`, `CPH-AE`, `AGE-CI/AE`, `AIB-CI/AE`
and every other sector/global gate retain their own exact gaps.

> **Claim record — SYN-0022-C06 | analytic-judgment**
> **Claim:** Only `FND-CI/AE` change; calibrated primary cases and the evidence
> ladder do not satisfy the different event-count, sector-outcome, deployed-
> safeguard-effectiveness or global-gate contracts.
> **Claim status:** active
> **Scope:** Current frozen sufficiency after planned active `SYN-0021`; not an
> external absence claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0022-C01–C05`; current frozen rows/source floors and prior
> `SYN-0001-C37` in `SYN-0001`.
> **Basis / limits:** Each non-promotion has a literal predicate not supplied
> by a foundational taxonomy or ladder.

> **Claim record — SYN-0022-C07 | artifact-observation**
> **Claim:** Independent strict review accepts exactly `FND-CI` and `FND-AE`
> Partial→Pass. After active `SYN-0021`, totals become 54 Pass, 53 Partial and
> 3 Absent = 54/110 (49.1%); Foundations becomes 9/10, critical cells become
> 49 Pass, 41 Partial and 1 Absent, and dimensions at least 9/10 remain 1/11.
> All global gates remain unchanged.
> **Claim status:** active
> **Scope:** Filesystem after activation of `SYN-0022` following `SYN-0021`;
> not 50% absolute domain completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0022-C01–C06`; frozen criteria/source floors; prior planned
> `SYN-0001-C37`; independent audits completed 2026-07-12.
> **Basis / limits:** Two critical Partial→Pass changes produce the arithmetic;
> Partial remains zero points and no sector/global gate moves.

## Safety boundary

The calibration retains public class-level outcomes and evidence states only.
It omits personal identifiers, patient records, stolen-file contents, biological
sequence/sample content, facility/system topology, credentials, operational
parameters and exploit mechanics.

> **Claim record — SYN-0022-C08 | analytic-judgment**
> **Claim:** The calibration is defensive and outcome/evidence-state level and
> does not expose sensitive event, biological or cyber operational detail.
> **Claim status:** active
> **Scope:** Local page content; not a downstream-use guarantee for every
> linked external resource.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYN-0022-C01–C07`; local page content.
> **Basis / limits:** The page was reviewed for identity/actionable details;
> high-level public consequence/assurance calibration remains useful.

## Related pages

- [SYN-0006 — evidence ladder](syn-0006-official-control-function-state-taxonomy.md)
- [INC-0001 — Synnovis/NHSBT disruption](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md)
- [INC-0003 — national-review outcome context](../incidents/inc-0003-national-allergy-recording-fatality-review-2021-2023.md)
- [HAZ-0001 — controlled quality effect](../hazards/haz-0001-multiplex-sequencing-cross-sample-misassignment.md)
- [SRC-0034 — validity benchmark](../sources/src-0034-notin-proteingym-benchmark-2023.md)
- [SRC-0035 — field null/evaluation](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [SYN-0015 — clinical/system evaluation reconciliation](syn-0015-clinical-patient-outcome-systems-evaluation-reconciliation.md)
- [SYN-0001 — frozen coverage rubric](syn-0001-coverage-rubric.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md)
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md)
- [SRC-0030](../sources/src-0030-hssib-electronic-patient-record-systems-thematic-review.md)
- [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md)
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
