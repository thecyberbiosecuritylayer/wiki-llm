---
id: HAZ-0002
type: hazard
title: Patient, specimen and result identity or quality failure
aliases:
  - clinical laboratory identity mismatch hazard
  - specimen-to-result quality failure
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0007
  - SRC-0026
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: HAZ-0002-C01
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 10–15, 61–72, 89–100, 123, 147–148, 162–168 and 201"
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: HAZ-0002-C03
    evidence:
      - source: SRC-0005
        locator: "§§1.1 and 3.1–3.5, printed pp. 1–2 and 9–11/PDF pp. 10–11 and 18–20"
  - predicate: evidenced-by
    target: SRC-0007
    claim_id: HAZ-0002-C03
    evidence:
      - source: SRC-0007
        locator: "Volume C §§1.4–1.6, printed pp. 4–6/PDF pp. 13–15"
  - predicate: affects
    target: AST-0006
    claim_id: HAZ-0002-C02
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS pp. 64–68 and 162–166"
  - predicate: enables
    target: RSK-0013
    claim_id: HAZ-0002-C02
    evidence:
      - source: SRC-0026
        locator: "WHO LQMS workflow pp. 11–15 and error/consequence pp. 162–166"
tags:
  - clinical-laboratory
  - specimen-identity
  - patient-identity
  - quality-error
  - non-adversarial
  - near-miss
---

# Patient, specimen and result identity or quality failure

## Hazard definition

This hazard covers unintended loss of the trustworthy association among the
intended person/source, request, specimen, examination, result, report and
recipient. It also covers non-adversarial quality states capable of producing
an invalid/unavailable result across the clinical/public-health total-testing
lifecycle. It is not an attacker technique or incident. Broader laboratory/
biobank configuration, containment-context, environmental, inventory and
supply hazards belong to [HAZ-0006](haz-0006-laboratory-input-configuration-environmental-and-inventory-failures.md).

## Phase taxonomy

| Phase | Hazard classes | First affected state |
| --- | --- | --- |
| pre-examination | wrong/missing identity, unsuitable/degraded sample, request mismatch, transport/referral delay | specimen/request provenance or availability |
| examination | instrument/reagent/method/operator/environment failure, failed QC, stale procedure | analytical validity or result availability |
| post-examination | transcription, wrong destination, lost/delayed/non-reported result, interpretation/context gap | report integrity/availability or recipient trust |
| cross-phase | workload, training, role ambiguity, record loss, interface incompatibility | detection, traceability or recovery capability |

> **Claim record — HAZ-0002-C01 | analytic-judgment**
> **Claim:** The phase taxonomy reconciles WHO's non-adversarial identity,
> specimen, analytical, information and reporting hazard classes without
> relabeling them as cyberattacks.
> **Claim status:** active
> **Scope:** Clinical/public-health laboratory quality hazards; not frequency,
> severity, attribution or a named event.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C04/C06`–`C10`, especially pp. 64–68, 89–100, 123,
> 147–148, 162–168 and 201.
> **Basis / limits:** Hazard classes are direct; the four-row normalization is
> analytic. Old secondary error percentages are excluded.

> **Claim record — HAZ-0002-C02 | analytic-judgment**
> **Claim:** If undetected before release/action, a specimen/result association
> or quality failure can propagate through [WFL-0010](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md)
> into inappropriate care or public-health action, but that consequence is
> conditional rather than observed in this source.
> **Claim status:** active
> **Scope:** Potential hazard transfer affecting [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md);
> not a patient-outcome case or deterministic medical conclusion.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C04/C08`, pp. 10–12, 62–72 and 162–166.
> **Basis / limits:** Workflow and possible consequences are direct; the compact
> propagation statement is analytic. The p. 165 diagram is illustrative only.

> **Claim record — HAZ-0002-C03 | analytic-judgment**
> **Claim:** Ordinary processing, inaction or association error can also create
> privacy or decision risk without malicious cyber activity; conversely,
> genomic integrity manipulation is a separate adversarial possibility and must
> not be merged into this non-adversarial hazard.
> **Claim status:** active
> **Scope:** Boundary between quality hazard, privacy side effect and cyber
> integrity threat; no observed privacy harm or manipulation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> `SRC-0007-C04`; [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C03/C07`; [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> `SRC-0026-C08/C11`.
> **Basis / limits:** Each source distinguishes relevant states. This page does
> not infer one cause from another.

> **Claim record — HAZ-0002-C04 | artifact-observation**
> **Claim:** `HAZ-0002` can supply the missing non-adversarial/identity limbs of
> `CPH-TV` only within an SF2 synthesis that separately includes malicious,
> outage, privacy and specific exposure evidence; it cannot satisfy `CPH-CI`.
> **Claim status:** active
> **Scope:** Accepted criterion boundary after independent review.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `HAZ-0002-C01`–`C03`; frozen `CPH-TV/CI` criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** One hazard lineage is not the complete threat corpus and
> supplies no qualifying primary case/outcome.

## Controls and safety boundary

Identity checks, QC/result withholding, verification, authorized release,
notification and correction are mapped in
[CTL-0012](../controls/ctl-0012-clinical-laboratory-quality-reporting-continuity-controls.md).
No patient/specimen data, thresholds, procedures or pathogen settings are
retained.

## Related pages

- [AST-0006 — affected assets](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md)
- [WFL-0010 — lifecycle](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md)
- [HAZ-0006 — broader laboratory/biobank hazards](haz-0006-laboratory-input-configuration-environmental-and-inventory-failures.md)
- [RSK-0013 — transfer paths](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md)
- [SYN-0013 — CPH reconciliation](../syntheses/syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md)

## Sources

- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md)
