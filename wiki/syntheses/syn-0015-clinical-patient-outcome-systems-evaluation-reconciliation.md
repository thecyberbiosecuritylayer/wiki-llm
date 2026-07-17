---
id: SYN-0015
type: synthesis
title: Clinical patient-outcome and systems-evaluation reconciliation
aliases:
  - CPH-CI criterion reconciliation
  - clinical-record outcome and EPR systems evidence synthesis
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-16
review_after: 2026-10-10
source_ids:
  - SRC-0008
  - SRC-0009
  - SRC-0029
  - SRC-0030
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0029
    claim_id: SYN-0015-C03
    evidence:
      - source: SRC-0029
        locator: "NatPSA PDF p. 1 fatal summary and p. 2 Patient safety incident data; SRC-0029-C04–C07"
  - predicate: evidenced-by
    target: SRC-0030
    claim_id: SYN-0015-C04
    evidence:
      - source: SRC-0030
        locator: "HSSIB About/Executive Summary and §§2–3, physical pp. 2–23; Appendix A pp. 36–38; Appendix B p. 39"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: SYN-0015-C12
    evidence:
      - source: SRC-0008
        locator: "NHSBT annual report pp. 21–22 and 97; service/system consequence and absent patient-outcome boundary"
  - predicate: evidenced-by
    target: SRC-0009
    claim_id: SYN-0015-C12
    evidence:
      - source: SRC-0009
        locator: "NHS England Synnovis update paragraphs 2–3, preserved HTML lines 190–191"
tags:
  - clinical-public-health
  - patient-outcome
  - incident-evidence
  - electronic-patient-record
  - systems-evaluation
  - lineage-reconciliation
  - evidence-quality
  - coverage
---

# Clinical patient-outcome and systems-evaluation reconciliation

## Question and current finding

This synthesis tests one frozen cell:

> `CPH-CI`: a primary case documents a patient or population outcome or a
> measured near miss, service delay is distinguished from biological harm,
> and the SF3 floor supplies SF2 independence and reconciliation plus a direct
> observed outcome and an independent confirmation or evaluation.

The public corpus distinguishes reported biological harm from service delay
and contains an independent EPR system-class evaluation. It does **not** retain
a claim-appropriate primary case record for the outcome branch. `CPH-CI`
therefore remains **Partial**. Neither the national aggregate review nor the
thematic systems evaluation is promoted into the missing primary-case role.

## Evidence roles and counting boundaries

| Lineage | Direct role | Explicit non-contribution |
| --- | --- | --- |
| National alert and review (`SRC-0029`) | official aggregate-review lineage and one source-reported fatal-outcome account | primary case record, unique incident or patient count, event-specific interface cause, measured near-miss count, or control effectiveness |
| Independent thematic review (`SRC-0030`) | primary for its review method, coding, and broader EPR system-class findings; derivative for underlying cases | primary event record, confirmation of the national-review outcome account, prevalence, or safeguard effectiveness |
| Synnovis/NHS operational record (`SRC-0008/0009`) | service, capacity, material-pressure, response, and restoration comparator | patient injury, incompatible transfusion, or independently validated recovery |

> **Claim record — SYN-0015-C03 | analytic-judgment**
> **Claim:** A national authority supplies one aggregate-review lineage and a
> source-reported fatal medication-safety outcome account.
> **Evidence:** [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md),
> `SRC-0029-C02/C05`–`C07`; NatPSA PDF p. 1 fatal summary and p. 2
> `Patient safety incident data`; [INC-0003](../incidents/inc-0003-national-allergy-recording-fatality-review-2021-2023.md),
> `INC-0003-C01`–`C05`; [RSK-0015](../risk-scenarios/rsk-0015-allergy-record-entry-propagation-medication-harm.md),
> `RSK-0015-C01`–`C03`.
> **Limits:** The aggregate units do not map one-to-one to events or patients,
> the page is not a primary individual case record, and unquantified harm
> language supplies no measured near-miss numerator.

> **Claim record — SYN-0015-C04 | analytic-judgment**
> **Claim:** HSSIB independently evaluates the broader EPR system class across
> its investigation corpus and identifies recurring availability/findability,
> incorrect-state, design/function/interoperability, local-configuration,
> integration, infrastructure, human-workflow, and governance dependencies.
> **Evidence:** [SRC-0030](../sources/src-0030-hssib-electronic-patient-record-systems-thematic-review.md),
> `SRC-0030-C02`–`C10`, physical pp. 2–23 and Appendix A pp. 36–38;
> [SYS-0010](../systems/sys-0010-electronic-patient-record-safety-dependencies.md),
> `SYS-0010-C01`–`C06`.
> **Limits:** HSSIB is primary for its method and system-class findings but
> derivative for underlying cases. Its report and coding units are not
> incidents, patients, or evaluations of an implemented safeguard.

> **Claim record — SYN-0015-C11 | analytic-judgment**
> **Claim:** The national-review, thematic-evaluation, and Synnovis lineages
> are materially distinct for their allocated predicates by issuer, corpus,
> method, and claim object.
> **Evidence:** `SYN-0015-C03/C04`;
> [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C03/C04`, pp. 21–22 and 97; and
> [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> `SRC-0009-C03/C04`, update paragraphs 2–3.
> **Limits:** Independent roles in a synthesis do not make the thematic review
> a confirmation of an event account or the two Synnovis issuers separate
> incidents.

## Outcome-state reconciliation

| Outcome state | Supported finding | Boundary |
| --- | --- | --- |
| biological harm | the national review contains one source-reported fatal-outcome account | not a retained primary case record, unique-person count, incidence estimate, or independently re-adjudicated outcome |
| service/capacity delay | Synnovis reduced test processing and reported more than 11,000 delayed appointments | observed service delay, not automatically biological injury |
| material/continuity pressure | compatibility-testing disruption, specialist workload, and blood-stock pressure | operational and material effect, with no confirmed patient injury in the retained package |
| HSSIB codes and vignettes | report-level thematic evidence about system classes | not added patient or event counts |
| low/no-harm and near-miss language | aggregate or derivative qualitative reporting | no qualifying measured near-miss numerator or denominator |

> **Claim record — SYN-0015-C12 | analytic-judgment**
> **Claim:** The retained corpus distinguishes a source-reported fatal clinical
> outcome from service delay and material pressure; the Synnovis lineage
> establishes operational consequences without confirming patient injury.
> **Evidence:** `SRC-0029-C06/C07`;
> [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> `SRC-0008-C03/C04`, pp. 21–22 and 97;
> [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> `SRC-0009-C03/C04`, update paragraphs 2–3; `INC-0001-C02/C04/C05`;
> `RSK-0006-C01/C03`.
> **Limits:** The national-review report units do not establish a patient or
> incident count, and delay, stock pressure, and restoration do not establish
> patient injury or control effectiveness.

## Rubric decision

| Required limb | Retained basis | Finding |
| --- | --- | --- |
| claim-appropriate primary case/outcome | no retained public primary case record | not satisfied |
| materially independent context | national aggregate review plus independent thematic EPR evaluation | satisfied for their bounded predicates |
| independent confirmation or evaluation | HSSIB evaluates the broader system class | evaluation available, but it cannot replace the missing primary case |
| service delay distinct from biological harm | national-review outcome account and Synnovis comparator | satisfied |
| measured near-miss alternative | no qualifying numerator and denominator | not satisfied |

> **Claim record — SYN-0015-C13 | analytic-judgment**
> **Claim:** `CPH-CI` remains Partial under the frozen SF3 criterion because
> the retained public corpus has a source-reported fatal-outcome account and an
> independent system-class evaluation but no claim-appropriate primary case
> record or measured near miss.
> **Evidence:** `SYN-0015-C03/C04/C11/C12`; the frozen `CPH-CI` criterion and
> SF3 source floor in [SYN-0001](syn-0001-coverage-rubric.md).
> **Limits:** This is a corpus-sufficiency finding, not evidence that no
> qualifying primary case or measured near miss exists externally.

> **Claim record — SYN-0015-C14 | analytic-judgment**
> **Claim:** `CPH-AE` remains Partial because recommendations, required
> actions, implementation statements, service metrics, and system-risk
> evaluation do not provide a scoped safeguard metric with independent
> patient-outcome evaluation.
> **Evidence:** `SRC-0029-C08/C09`; `INC-0003-C06`; `SRC-0030-C11/C13`;
> `SYS-0010-C07`; the frozen `CPH-AE` criterion in `SYN-0001`.
> **Limits:** The retained sources do not establish that no local improvement
> or unlocated evaluation exists.

> **Claim record — SYN-0015-C15 | artifact-observation**
> **Claim:** At the frozen checkpoint represented by this synthesis, no cell
> changes status: the score remains 37 Pass, 67 Partial, and 6 Absent, or
> 37/110 (33.6%), and CPH remains 8/10.
> **Evidence:** `SYN-0015-C11`–`C14`; the preceding 37/110 checkpoint and
> binary scoring method in [SYN-0001](syn-0001-coverage-rubric.md).
> **Limits:** This is historical checkpoint arithmetic, not the score after
> later source transactions or a measure of absolute domain completeness.

> **Claim record — SYN-0015-C16 | artifact-observation**
> **Claim:** The privacy-retired lineage contributes no public incident,
> outcome, control-lesson, evaluator, or independence unit to any rubric or
> global-gate numerator.
> **Evidence:** The public wiki graph and retired entries in
> [the ID registry](../id-registry.md), inspected 2026-07-16.
> **Limits:** The registry records identity history, not factual evidence about
> the underlying external event.

## Superseded public-corpus claims

Claims `SYN-0015-C01`, `C02`, and `C05`–`C10` are withdrawn from the public
corpus as of 2026-07-16 because their conclusions depended wholly or partly on
a lineage retired for privacy. They must not be used to support an outcome,
incident count, control lesson, rubric transition, or global gate. Current
findings are `SYN-0015-C11`–`C16`; `C03` and `C04` retain their narrower,
source-supported meanings.

## Safety boundary

This synthesis retains only issuer, evidence modality, aggregate outcome
class, service/material consequence, and system-level dependency distinctions.
It contains no patient identity, individual clinical particulars, facility or
provider identity, product configuration, user-interface procedure, endpoint,
credential, or system topology.

## Related pages

- [INC-0003 — national review and fatal-outcome account](../incidents/inc-0003-national-allergy-recording-fatality-review-2021-2023.md)
- [RSK-0015 — inaccurate-state branch](../risk-scenarios/rsk-0015-allergy-record-entry-propagation-medication-harm.md)
- [SYS-0010 — independent EPR systems evaluation map](../systems/sys-0010-electronic-patient-record-safety-dependencies.md)
- [INC-0001 — service/material consequence comparator](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md)
- [SYN-0001 — frozen rubric](syn-0001-coverage-rubric.md)

## Sources

- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md)
- [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md)
- [SRC-0030](../sources/src-0030-hssib-electronic-patient-record-systems-thematic-review.md)
