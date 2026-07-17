---
id: RSK-0021
type: risk-scenario
title: Biological test input to digital result and public-health action
aliases:
  - laboratory reverse-transfer incident path
  - biological input to digital decision risk
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-12
source_ids:
  - SRC-0026
  - SRC-0057
  - SRC-0058
sensitivity: public
dual_use: low
origin_domain: biological
destination_domains:
  - digital
  - public-health
  - biological
transfer_mechanism: material-to-measurement-to-digital-result-and-decision
risk_state: mixed-observed-incident-and-investigated-exposure-paths
relations:
  - predicate: evidenced-by
    target: SRC-0057
    claim_id: RSK-0021-C01
    evidence:
      - source: SRC-0057
        locator: "SUI Executive summary ¶¶3–5 and §3.1.1; UKHSA preprint Introduction/Methods/Results, pp. 1–5"
  - predicate: evidenced-by
    target: SRC-0058
    claim_id: RSK-0021-C03
    evidence:
      - source: SRC-0058
        locator: "ED03-2024 Issue, Outline, multiple-sample and record/IT sections; HID 5-2011 Background"
  - predicate: depends-on
    target: WFL-0010
    claim_id: RSK-0021-C01
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS total-testing workflow pp. 11–15 and result/report/decision controls pp. 162–168 and 193–207"
  - predicate: depends-on
    target: SYS-0008
    claim_id: RSK-0021-C04
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS information-system and reporting boundaries, pp. 193–207"
      - source: SRC-0058
        locator: "HSE record/IT context capture, visibility, linkage and update-alert conditions"
  - predicate: affects
    target: AST-0006
    claim_id: RSK-0021-C02
    evidence:
      - source: SRC-0057
        locator: "SUI §§1.2 and 3.1; UKHSA preprint population-level impact scope"
tags:
  - laboratory
  - public-health
  - biological-input
  - digital-result
  - decision
  - reverse-direction
  - observed-incident
  - modelled-consequence
---

# Biological test input to digital result and public-health action

> [!WARNING]
> **Evidence classification**
> Path A is an observed non-malicious incident through the digital-result node;
> its population consequences are modelled. Path B is an HSE regulator summary
> of investigated exposure occasions. Neither is a cyberattack, procedure or
> likelihood estimate.

## Path A — observed biological input to digital result and action state

`biological test input → laboratory measurement/configured interpretation →
digital result → person/public-health isolation and tracing decision state →
modelled population-level transmission consequence`

> **Claim record — RSK-0021-C01 | analytic-judgment**
> **Claim:** `INC-0008` supplies an observed complete material/input→digital-
> decision path: a staff classification-configuration error caused some test
> measurements to be digitally reported negative when otherwise positive,
> altering the digital notification state that ordinarily initiates positive-
> result isolation/contact-tracing action.
> **Claim status:** active
> **Scope:** Safe high-level path across
> [WFL-0010](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md);
> no assay setting, patient record, procedure or claim every estimated report
> produced the same downstream behavior.
> **As of:** Event September–October 2021; findings 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md),
> `SRC-0057-C03/C04/C10`; SUI Executive summary ¶¶3–5; SUI §2.6.7,
> printed p. 45 (data-upload KPI), and §3.1.1, p. 51 (barcode review and
> tailored text messages); UKHSA preprint Introduction, p. 2 (positive-result
> notification initiates contact tracing). [INC-0008](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md)
> `C03/C06/C09` supplies canonical event navigation, not independent evidence.
> **Basis / limits:** Input, interpretation, report and intended action nodes
> are direct. Person-level behavior and health outcomes are not reconstructed.

> **Claim record — RSK-0021-C02 | analytic-judgment**
> **Claim:** The affected state spans test integrity, public-health decision
> quality and represented population transmission: about 39,000 incorrect
> reports are estimated, and area-level models estimate additional cases and
> infections while hospitalisation/death intervals include zero.
> **Claim status:** active
> **Scope:** Consequence ladder affecting
> [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md);
> estimated/modelled nodes remain distinct from observed digital reports and
> are not individual attribution.
> **As of:** Event/model period 2021; publications 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** `INC-0008-C04/C05/C07`; `SRC-0057-C05`–`C07`; UKHSA
> preprint Methods/Results/Discussion and Tables 3, 5–6.
> **Basis / limits:** Revised result scale and ecological effects are estimates;
> the retained preprint's ambiguous multiplier is excluded.

## Path B — investigated context input to containment decision

`specimen + missing/inaccurate/delayed risk context → incomplete information
state → unsuitable containment decision → inappropriate handling → worker
exposure risk/event`

> **Claim record — RSK-0021-C03 | source-report**
> **Claim:** HSE independently anchors a related input/context→decision path:
> missing or delayed specimen information and absent cross-sample linkage led
> to insufficient containment decisions and confirmed worker-exposure
> occasions in clinical/veterinary laboratories.
> **Claim status:** active
> **Scope:** Investigated safety-decision path; not a digital-result incident,
> infection count, named facility or operational containment instruction.
> **As of:** HSE notices 2011 and 2024.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0058](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md),
> `SRC-0058-C02`–`C05`; ED03-2024 Issue/Outline/multiple-sample sections.
> **Basis / limits:** HSE reports the causal information gap and exposure
> occasions but no count, method or independent case confirmation.

## Boundaries and exact control points

| Path edge | Primary failure state | Defensive control point |
| --- | --- | --- |
| input/context→accession | missing identity/risk/provenance context | structured capture, validation, linkage, clarification |
| measurement→classification | incorrect or unverified configuration/change | change authorization, verification, QC and result hold |
| classification→report | anomalous pattern not detected/escalated | contextual performance monitoring and trigger investigation |
| report→decision | untrusted/incorrect result reaches user | authorization, notification, correction and affected-recipient action |
| concern→response | fragmented logging, ownership or analysis | single incident governance, risk assessment, evidence review, external challenge |
| containment→recovery/learning | suspension without trusted restoration proof | verified correction, traceable remediation, review and effectiveness evaluation |

> **Claim record — RSK-0021-C04 | analytic-judgment**
> **Claim:** The six control points map the observed/investigated paths to
> exact [SYS-0008](../systems/sys-0008-clinical-laboratory-information-reporting-ecosystem.md)
> boundaries and `CTL-0023` prevention, detection, response/correction,
> recovery and assurance functions without claiming universal mitigation.
> **Claim status:** active
> **Scope:** Defensive exact-edge map; not a deployment topology, operational
> procedure or safeguard-effectiveness result.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `RSK-0021-C01`–`C03`; `SRC-0057-C08/C09`;
> `SRC-0058-C04/C05`; [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C06/C07/C09/C10`.
> **Basis / limits:** Every function is source-supported; exact edge
> normalization is analytic and prerequisites remain context-specific.

## Directionality and nonpromotion

> **Claim record — RSK-0021-C05 | analytic-judgment**
> **Claim:** Unlike prior functional or controlled reverse paths, Path A is a
> primary official incident in which a biological input reached an erroneous
> digital result and downstream decision state; this strengthens global
> directionality but does not turn accidental error into cyber or malicious
> evidence.
> **Claim status:** active
> **Scope:** Evidence-state comparison for the reverse-direction corpus; gate
> adjudication remains in `SYN-0031`.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `RSK-0021-C01/C02`; [RSK-0013](rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md),
> `RSK-0013-C03/C06`; `SRC-0057-C10`.
> **Basis / limits:** Incident state and direction are direct. The consequence
> endpoint retains modelled uncertainty.

> **Claim record — RSK-0021-C06 | analytic-judgment**
> **Claim:** No source in this path establishes exploitability, recurrence
> likelihood, a person-level clinical outcome, full recovery or independently
> measured control effectiveness.
> **Claim status:** active
> **Scope:** Negative evidence boundary after full package review.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0057-C06/C09/C10`; `SRC-0058-C02/C05/C07`.
> **Basis / limits:** Missing predicates are explicit; absence of represented
> evidence is not evidence these outcomes or capabilities are impossible.

## Safety boundary

The page omits assay values, procedures, personal records, facility topology,
pathogen detail and any method for causing or evading the represented failures.

## Related pages

- [INC-0008 — observed incident](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md)
- [HAZ-0006 — triggers](../hazards/haz-0006-laboratory-input-configuration-environmental-and-inventory-failures.md)
- [VUL-0006 — enabling conditions](../vulnerabilities/vul-0006-laboratory-context-threshold-oversight-and-supply-exposures.md)
- [CTL-0023 — exact-edge controls](../controls/ctl-0023-laboratory-result-validation-anomaly-detection-and-containment-controls.md)
- [SYN-0003 — canonical transfer directions](../syntheses/syn-0003-cross-domain-transfer-directions.md)
- [SYN-0031 — directionality adjudication](../syntheses/syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)

## Sources

- [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md)
- [SRC-0058](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md)
- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
