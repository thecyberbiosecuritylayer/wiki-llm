---
id: HAZ-0006
type: hazard
title: Laboratory input, configuration, environmental, inventory and supply failures
aliases:
  - laboratory non-adversarial hazard classes
  - laboratory context and continuity failures
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-12
source_ids:
  - SRC-0004
  - SRC-0018
  - SRC-0022
  - SRC-0026
  - SRC-0057
  - SRC-0058
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0057
    claim_id: HAZ-0006-C02
    evidence:
      - source: SRC-0057
        locator: "SUI Executive summary ¶4, p. 8; Appendix 2 §2(B)(vi), p. 71; official press summary"
  - predicate: evidenced-by
    target: SRC-0058
    claim_id: HAZ-0006-C03
    evidence:
      - source: SRC-0058
        locator: "ED03-2024 Issue, Outline, multiple-sample and record/IT sections; HID 5-2011 Key Issues and Background"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: HAZ-0006-C01
    evidence:
      - source: SRC-0004
        locator: "WHO §§5.1, 5.3.1–5.3.6 and 6.4–6.6, printed pp. 19–39/PDF pp. 39–59"
  - predicate: evidenced-by
    target: SRC-0022
    claim_id: HAZ-0006-C04
    evidence:
      - source: SRC-0022
        locator: "NCI §§B.5, C.2.6, C.3.2 and C.4.2–C.4.4, printed pp. 32–40, 56–65"
  - predicate: affects
    target: AST-0005
    claim_id: HAZ-0006-C01
    evidence:
      - source: SRC-0004
        locator: "WHO laboratory biological-material, information, technology and facility scope, §§1–2 and 5–7"
  - predicate: enables
    target: RSK-0021
    claim_id: HAZ-0006-C02
    evidence:
      - source: SRC-0057
        locator: "Observed configuration error→digital result→decision path, SUI Executive summary ¶¶3–5"
tags:
  - laboratory
  - accidental
  - configuration-error
  - missing-context
  - environmental
  - inventory
  - supply
  - non-adversarial
---

# Laboratory input, configuration, environmental, inventory and supply failures

## Canonical non-adversarial taxonomy

This page owns broad LAB/biobank configuration, containment-context,
environmental, inventory and supply hazards. The narrower patient/specimen/
result identity-quality lifecycle in clinical/public-health testing remains
canonical in [HAZ-0002](haz-0002-patient-specimen-result-identity-quality-failure.md).

| Hazard family | First affected state | Evidence role |
| --- | --- | --- |
| input/context | identity, provenance, risk context or requested action | HSE investigated exposures; WHO LQMS design |
| configuration/change | measurement classification, interface or reporting state | Immensa observed incident |
| accidental handling/quality | material, worker, result or custody state | WHO/HSE official |
| environmental/utility | facility/containment, storage, equipment or continuity | WHO/NIST normative |
| inventory/accountability | material/reagent availability, identity, location or discrepancy | WHO/CBS/NCI normative |
| supply/third-party | reagent/service/provider availability, integrity or continuity | WHO/NCI/NIST normative |

> **Claim record — HAZ-0006-C01 | analytic-judgment**
> **Claim:** The six-row taxonomy reconciles accidental, environmental,
> inventory and supply failure classes across independent WHO, NIST, NCI and
> WHO-LQMS lineages while keeping them distinct from intentional `THR-0005`
> actions and named-event claims.
> **Claim status:** active
> **Scope:** Laboratory/biobank hazard breadth affecting
> [AST-0005](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md);
> not prevalence, a universal facility model or evidence every class occurred.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§5.1, 5.3.1–5.3.6 and 6.4–6.6, printed pp. 19–39/PDF pp. 39–59;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> `SRC-0018-C02/C04/C05`; [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> `SRC-0022-C03/C05/C06`; [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C03/C06/C08`.
> **Basis / limits:** Categories and dependencies are direct; the compact
> normalization and cross-source boundary are analytic.

## Observed configuration hazard

> **Claim record — HAZ-0006-C02 | source-report**
> **Claim:** `INC-0008` provides a concrete accidental configuration hazard:
> staff error in result classification caused some biological test
> measurements to be digitally reported negative when they otherwise would
> have been classified positive, enabling the observed `RSK-0021` path.
> **Claim status:** active
> **Scope:** One safe high-level event mechanism; no operational setting,
> procedure, malicious intent or claim all laboratories share the condition.
> **As of:** Event September–October 2021; findings 2022.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md),
> `SRC-0057-C03/C04`; [INC-0008](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md),
> `INC-0008-C03/C06`.
> **Basis / limits:** Cause is direct and non-malicious. Exact first error and
> person-level result states are unknown. `HAZ-0006` owns the accidental staff
> action/trigger and erroneous state transition; `VUL-0006-C02` owns the unsafe
> configuration state and validation/monitoring/oversight weaknesses that let
> the error persist or delayed its detection. `INC-0008` owns the event.

## Investigated context/containment hazard

> **Claim record — HAZ-0006-C03 | source-report**
> **Claim:** HSE reports investigated occasions where missing, inaccurate or
> delayed specimen context and failed cross-sample communication led to
> handling under insufficient containment and worker exposure risk/events.
> **Claim status:** active
> **Scope:** Clinical/veterinary laboratory context and safety-decision hazard;
> not an infection count, named event or operational containment procedure.
> **As of:** HSE notices 2011 and 2024.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0058](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md),
> `SRC-0058-C02`–`C04`; both notices' issue/background sections.
> **Basis / limits:** HSE directly reports exposures and the information gap;
> exact case count, methods and outcomes are absent.

## Environmental, inventory and supply limbs

> **Claim record — HAZ-0006-C04 | analytic-judgment**
> **Claim:** WHO and NCI independently support environmental/utility,
> inventory/accountability and reagent/service/supplier failure limbs through
> protected inventory, monitoring/alarms, alternate capability, physical
> checks, provider dependencies and continuity planning, without proving a
> named failure or universal implementation.
> **Claim status:** active
> **Scope:** SF2 hazard/exposure coverage for research, diagnostic, containment
> and biobank contexts; not an incident or effectiveness claim.
> **As of:** Source editions through 2024; reviewed 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§5.3.2, 5.3.6, 6.4–6.6 and 7.3.1; [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> `SRC-0022-C03/C05/C06`, §§B.5, C.2.6, C.3.2 and C.4.2–C.4.4.
> **Basis / limits:** Dependencies/control responses reveal the hazard limbs.
> Recommended resilience is not evidence a hazard occurred or was prevented.

> **Claim record — HAZ-0006-C05 | analytic-judgment**
> **Claim:** One hazard can cross material, information and physical-safety
> states, but input error, configuration error, environmental interruption,
> inventory discrepancy and supplier failure remain distinct triggers and are
> not multiplied into incidents or assigned common likelihood.
> **Claim status:** active
> **Scope:** Cross-state semantics and event-count discipline.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `HAZ-0006-C01`–`C04`; `SRC-0057-C05/C06` and
> `SRC-0058-C02/C06` for count/estimate limits.
> **Basis / limits:** State transitions are supported; frequency and common
> causation are not.

## Safety boundary

No assay threshold, pathogen procedure, inventory, facility topology or
operational response sequence is retained. Hazard description stays at the
level required for defensive control and evidence-state mapping.

## Related pages

- [HAZ-0002 — clinical specimen/result identity-quality boundary](haz-0002-patient-specimen-result-identity-quality-failure.md)
- [THR-0005 — intentional actions](../threats/thr-0005-laboratory-malicious-insider-and-supply-actions.md)
- [VUL-0006 — specific exposures](../vulnerabilities/vul-0006-laboratory-context-threshold-oversight-and-supply-exposures.md)
- [INC-0008 — observed configuration event](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md)
- [RSK-0021 — observed reverse path](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)
- [CTL-0023 — controls](../controls/ctl-0023-laboratory-result-validation-anomaly-detection-and-containment-controls.md)
- [SYN-0031 — reconciliation](../syntheses/syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md)
- [SRC-0058](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md)
