---
id: CTL-0021
type: control
title: Secure, monitored biological-AI lifecycle controls
aliases:
  - biological AI MLOps security controls
  - monitored model lifecycle control family
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-02
source_ids:
  - SRC-0033
  - SRC-0049
  - SRC-0050
  - SRC-0051
  - SRC-0052
  - SRC-0053
  - SRC-0054
sensitivity: public
dual_use: low
control_status: normative-and-recommended-family-with-bounded-implementation-examples
implementation_status: two-bounded-research-clinical-implementation-contexts
testing_status: process-and-model-evaluation-fragments-only
effectiveness_status: unknown
independent_evaluation_status: unknown-for-complete-control-family
relations:
  - predicate: evidenced-by
    target: SRC-0049
    claim_id: CTL-0021-C01
    evidence:
      - source: SRC-0049
        locator: "ETSI EN 304 223 clauses 5.1–5.5, pp. 10–15; ETSI TR §§6.1–6.13, pp. 19–70"
  - predicate: evidenced-by
    target: SRC-0050
    claim_id: CTL-0021-C02
    evidence:
      - source: SRC-0050
        locator: "Results/Figure 2, article pp. 2–4; Discussion p. 7; Methods pp. 8–9"
  - predicate: evidenced-by
    target: SRC-0051
    claim_id: CTL-0021-C03
    evidence:
      - source: SRC-0051
        locator: "§§2.1 and 3.1, Figures 1–2, article pp. 2–3"
  - predicate: evidenced-by
    target: SRC-0054
    claim_id: CTL-0021-C04
    evidence:
      - source: SRC-0054
        locator: "NOT-OD-14-124 §§II–V; NOT-OD-25-081 Purpose and requirements"
  - predicate: mitigates
    target: RSK-0016
    claim_id: CTL-0021-C05
    evidence:
      - source: SRC-0033
        locator: "Chapters 4–5, printed pp. 46–81 (physical pp. 67–102)"
      - source: SRC-0049
        locator: "ETSI EN clauses 5.1–5.5, pp. 10–15"
  - predicate: mitigates
    target: THR-0003
    claim_id: CTL-0021-C05
    evidence:
      - source: SRC-0049
        locator: "ETSI EN clauses 5.1.3, 5.2.1–5.2.5 and 5.4.2, pp. 11–15"
  - predicate: detects
    target: HAZ-0005
    claim_id: CTL-0021-C05
    evidence:
      - source: SRC-0049
        locator: "ETSI EN clause 5.4.2, p. 15; ETSI TR §6.12, pp. 65–69"
  - predicate: depends-on
    target: WFL-0013
    claim_id: CTL-0021-C06
    evidence:
      - source: SRC-0049
        locator: "ETSI lifecycle phases and clauses 5.1–5.5, pp. 5–15"
  - predicate: depends-on
    target: SYS-0013
    claim_id: CTL-0021-C06
    evidence:
      - source: SRC-0049
        locator: "ETSI EN clauses 5.1.2–5.2.4, pp. 10–13; ETSI TR §§6.2/6.5/6.6"
  - predicate: governed-by
    target: GOV-0024
    claim_id: CTL-0021-C07
    evidence:
      - source: SRC-0049
        locator: "ETSI EN 304 223 status/scope and clauses 5.1–5.5"
  - predicate: governed-by
    target: GOV-0025
    claim_id: CTL-0021-C07
    evidence:
      - source: SRC-0053
        locator: "Regulation (EU) 2024/1689 Arts 2, 6, 8–15, 43, 51–56 and 113"
  - predicate: governed-by
    target: GOV-0026
    claim_id: CTL-0021-C07
    evidence:
      - source: SRC-0054
        locator: "NOT-OD-14-124 and NOT-OD-25-081"
tags:
  - artificial-intelligence
  - biological-models
  - mlops
  - provenance
  - access-control
  - monitoring
  - drift
  - rollback
  - retirement
---

# Secure, monitored biological-AI lifecycle controls

## Objective and evidence states

Maintain traceable, authorized and reviewable data/model/software state from
design through deployment, operation, update and retirement. Interrupt
malicious or accidental state changes before they alter an experimental,
research, clinical or other consequential decision.

| Evidence rung | Current evidence |
| --- | --- |
| Recommended/normative | ETSI EN requirements, ETSI TR implementation examples, NASEM recommendations and NIH policy boundaries |
| Implemented | one reported oncology governance programme and one reproducible biomedical-ML framework context |
| Tested | bounded model/process evaluations; not the complete control family |
| Effective | unknown |
| Independently evaluated | CASP independently evaluates models, not this end-to-end control family |

> **Claim record — CTL-0021-C01 | source-report**
> **Claim:** The ETSI package covers risk ownership, asset/dependency
> inventory, provenance/audit, access and environment separation,
> pre-deployment testing, secure deployment, update/versioning/rollback,
> production monitoring and secure retirement across the complete AI
> lifecycle.
> **Claim status:** active
> **Scope:** EN normative requirements plus TR implementation examples for
> deployable AI; not certification, adoption or effectiveness evidence.
> **As of:** ETSI EN 304 223 V2.1.1 and TR 104 128 V1.1.1.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> ETSI EN clauses 5.1–5.5, pp. 10–15; ETSI TR §§6.1–6.13, pp. 19–70.
> **Basis / limits:** Functions are direct. The TR is informative and the two
> artifacts remain one ETSI lineage.

## Implemented fragments

> **Claim record — CTL-0021-C02 | source-report**
> **Claim:** The oncology programme reports governance intake, validation-to-
> production gates, a model registry, monitoring plans/reports, periodic
> review and two model sunsets across 33 live nomograms.
> **Claim status:** active
> **Scope:** One institutional clinical-research model-governance programme;
> not proof of patient benefit, harm prevention, cyber resilience or external
> generalizability.
> **As of:** 2025 publication.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md),
> Results/Figure 2, article pp. 2–4; Discussion p. 7; Methods pp. 8–9.
> **Basis / limits:** Implemented process states and counts are direct. The
> authors/programme do not supply an independent outcome comparator.

> **Claim record — CTL-0021-C03 | source-report**
> **Claim:** `mlf-core` reports reproducibility-oriented packaged code,
> isolated Conda/container environments, model registry/MLflow and service
> interfaces applied to several biomedical-model examples.
> **Claim status:** active
> **Scope:** Research framework and examples; not a security audit, production
> prevalence or effectiveness evaluation.
> **As of:** 2023 publication.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md),
> §§2.1 and 3.1, Figures 1–2, article pp. 2–3.
> **Basis / limits:** Components and uses are direct. Reproducibility design is
> not proof that every run, dependency or security control was validated.

> **Claim record — CTL-0021-C04 | source-report**
> **Claim:** NIH policy adds an enforceable award/contract/intramural boundary
> for covered genomic research and restricts development, sharing and closeout
> handling of generative-AI models, including parameters, derived from NIH controlled-access human
> genomic data to the NIH-approved use and approved-user collaborators, with
> the stated closeout-retention restriction.
> **Claim status:** active
> **Scope:** NIH-funded/controlled-access policy population; not all U.S.
> biology, an AI safety standard or evidence of organizational compliance.
> **As of:** Base policy effective 2015-01-25; clarification issued 2025-03-28.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md),
> NOT-OD-14-124 §§II–V; NOT-OD-25-081 Purpose and requirements.
> **Basis / limits:** Policy scope and duties are direct. Enforcement authority
> is not a compliance finding or an effectiveness result.

## Exact-edge control map

| Pipeline/model edge | Prevent | Detect/assure | Respond/recover |
| --- | --- | --- | --- |
| acquire/label → train/analyse | authorized data use, provenance, inventory | quality/bias checks and audit trail | quarantine or correct suspect data and re-evaluate descendants |
| code/dependency → build/runtime | versioned packages, containers and registries; separated environments | dependency and change review | rollback to a trusted version and rebuild affected state |
| model → deployment/inference | pre-deployment validation, intended-use boundary and accountable approval | acceptance tests and traceable release | contain or withdraw a release |
| inference → consequential use | least privilege, bounded authority and human/experimental gate | output, error and anomaly review | stop action, notify owners and reassess dependent decisions |
| operation → update | controlled change, staged rollout and versioning | drift, performance, bias and security monitoring | rollback/retrain/revalidate where justified |
| end of life | documented retirement and access revocation | verify decommission/disposition state | preserve required records while removing unneeded model/data access |

> **Claim record — CTL-0021-C05 | analytic-judgment**
> **Claim:** The reconciled family maps provenance, access, versioning,
> reproducibility, monitoring, human/experimental review, update/rollback and
> retirement to exact `RSK-0016`, `THR-0003` and `HAZ-0005` edges without
> treating a recommendation or implementation fragment as effectiveness.
> **Claim status:** active
> **Scope:** Defensive cross-lineage control mapping; not a universal baseline
> or claim that every function is required in every jurisdiction.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `CTL-0021-C01`–`C04`;
> [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapters 4–5; [RSK-0016](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md).
> **Basis / limits:** Functions have direct independent support; affected-
> output rollback and decision reassessment are conservative exact-edge
> normalization, not a reported universal mechanism.

> **Claim record — CTL-0021-C06 | analytic-judgment**
> **Claim:** Control applicability depends on the lifecycle in `WFL-0013` and
> the component/identity boundaries in `SYS-0013`; missing inventory,
> authority, observability or a trusted rollback basis can make a named
> control ineffective or inapplicable.
> **Claim status:** active
> **Scope:** Preconditions and failure modes, not a named deployment finding.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `CTL-0021-C01`–`C05`;
> [WFL-0013](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md);
> [SYS-0013](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md).
> **Basis / limits:** Preconditions follow the represented lifecycle and
> boundaries; no topology or implementation score is inferred.

## Governance and effectiveness boundaries

> **Claim record — CTL-0021-C07 | analytic-judgment**
> **Claim:** The ETSI European standard, EU AI Act and NIH governance layers
> differ in force,
> actors, exclusions and applicability; `governed-by` edges record those
> bounded roles and do not establish compliance or legal equivalence.
> **Claim status:** active
> **Scope:** Governance semantics for this control family.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-02.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> EN Foreword p. 4, Scope p. 6, stakeholder definitions pp. 9–10 and clauses
> 5.1–5.5, pp. 10–15; [SRC-0053](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md),
> Regulation (EU) 2024/1689 Articles 2, 6, 8–15, 43, 51–56 and 113;
> [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md),
> `NOT-OD-14-124` Sections II–III, IV.C.4–6 and V.A–B, and
> `NOT-OD-25-081` `Purpose`, both reminder bullets and the paragraphs beginning
> `Additionally` and `Until that guidance is issued`.
> **Limits:** The source instruments are direct and independently
> scoped. Crosswalk is analysis, not legal advice.

> **Claim record — CTL-0021-C08 | analytic-judgment**
> **Claim:** The corpus does not independently evaluate the complete control
> family's reduction of cyber, biological or clinical harm; oncology process
> adoption, mlf-core reproducibility and CASP model assessment remain bounded
> implementation/evaluation fragments.
> **Claim status:** active
> **Scope:** Evidence-ladder classification.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `CTL-0021-C02/C03`; [SRC-0052](../sources/src-0052-casp15-tertiary-structure-assessment-2023.md),
> assessment scope and limits.
> **Basis / limits:** Separating implementation, test and effectiveness avoids
> promoting component evidence into end-to-end safety assurance.

## Related pages

- [WFL-0013 — Secure model lifecycle](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md)
- [SYS-0013 — Biological MLOps boundaries](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md)
- [THR-0003 — Adversarial AI threat](../threats/thr-0003-adversarial-ai-data-model-and-interface-actions.md)
- [HAZ-0005 — Drift, bias and error hazard](../hazards/haz-0005-biological-ai-drift-bias-and-error.md)
- [VUL-0004 — AI exposure classes](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md)
- [RSK-0016 — Biological-AI output risk](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [GOV-0024 — ETSI European AI standard](../governance/gov-0024-etsi-european-ai-cybersecurity-standard.md)
- [GOV-0025 — EU AI Act](../governance/gov-0025-eu-ai-act-life-sciences-applicability.md)
- [GOV-0026 — NIH genomic AI policy](../governance/gov-0026-nih-genomic-data-ai-use-policy.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)

## Sources

- [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md).
- [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md).
- [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md).
- [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md).
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md).
