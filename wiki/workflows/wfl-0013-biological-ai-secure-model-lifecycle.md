---
id: WFL-0013
type: workflow
title: Secure biological-AI model lifecycle from intake to retirement
aliases:
  - deployed biological AI lifecycle
  - biological AI MLOps lifecycle
  - secure model deployment monitoring and retirement
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0049
  - SRC-0050
  - SRC-0051
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0049
    claim_id: WFL-0013-C01
    evidence:
      - source: SRC-0049
        locator: "EN Introduction, p. 5; clauses 5.1.2–5.5.1, pp. 10–15; TR clauses 6.11–6.13, pp. 63–70"
  - predicate: evidenced-by
    target: SRC-0050
    claim_id: WFL-0013-C02
    evidence:
      - source: SRC-0050
        locator: "Results and Figure 2, pp. 2–4; Discussion, p. 7; Methods, pp. 8–10"
  - predicate: evidenced-by
    target: SRC-0051
    claim_id: WFL-0013-C03
    evidence:
      - source: SRC-0051
        locator: "Methods/Results and Figures 1–2, pp. 2–4; Discussion, pp. 6–7; Supplementary Methods, pp. 17–23"
  - predicate: depends-on
    target: SYS-0013
    claim_id: WFL-0013-C04
    evidence:
      - source: SRC-0049
        locator: "EN clauses 5.2.1–5.2.3, pp. 12–13"
      - source: SRC-0050
        locator: "Methods and Figure 6, pp. 9–10"
      - source: SRC-0051
        locator: "Results and Figures 1–2, pp. 3–4"
tags:
  - artificial-intelligence
  - biological-models
  - model-lifecycle
  - deployment
  - monitoring
  - drift
  - reproducibility
  - retirement
---

# Secure biological-AI model lifecycle from intake to retirement

## Scope and reconciliation rule

This page joins three materially independent forms of evidence:

- a current cross-sector ETSI requirements lineage for deployed AI;
- a primary oncology governance implementation with real production,
  monitoring and model-sunset actions; and
- a primary biomedical MLOps/determinism study for reproducible development
  environments and model state.

No source is treated as if it demonstrates the complete lifecycle alone.
ETSI does not supply biological scope or implementation; the oncology study
does not document every acquisition/training/dependency state; and mlf-core
does not demonstrate live monitoring or retirement. The workflow below is a
defensive reconciliation, not one universal procedure or automation recipe.

## Generic deployed-AI lifecycle baseline

ETSI EN 304 223 separates design, development, deployment, maintenance and
end of life and maps them to deployment, operations/monitoring and retirement.
It requires or recommends lifecycle audit trails, pre-deployment testing,
post-deployment maintenance plans, updates/version evaluation, production
monitoring and secure decommission/disposal. Its scope excludes systems used
only for academic research and never intended for deployment.

> **Claim record — WFL-0013-C01 | source-report**
> **Claim:** ETSI supplies a current, explicit deployment-to-retirement
> security lifecycle with provenance, validation, update, monitoring and
> decommission functions for AI systems intended for deployment.
> **Claim status:** active
> **Scope:** Generic requirements and informative examples; not biological
> scope, implementation, conformance or successful lifecycle operation.
> **As of:** EN V2.1.1, 2025-12; package status reviewed 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> `SRC-0049-C02`–`C04`; EN Introduction, p. 5; Scope, p. 6;
> `5.1.2–5.5.1`, pp. 10–15; TR `6.11–6.13`, pp. 63–70.
> **Basis / limits:** EN phases/provisions are direct. TR details remain
> informative examples for the predecessor TS and are not implementation
> evidence or a second lineage.

## Direct oncology deployment and retirement segment

MSK's iLEAP implementation distinguishes research, internally developed and
acquired/co-developed model paths. Its gates connect proposal/intake,
registration, Model Information Sheet, validation/risk review, Monitoring
Plan, production release and Monitoring Report. The study reports production
monitoring, six-to-twelve-month or major-revision review, and two actual
nomogram sunsets after clinical evidence changed.

> **Claim record — WFL-0013-C02 | source-report**
> **Claim:** A primary oncology implementation directly instantiates
> validation→registry/gate→production→monitoring and evidence-driven model
> sunset, including drift/performance and safety/adoption monitoring state.
> **Claim status:** active
> **Scope:** One comprehensive cancer centre's governed clinical/operational
> models; not every research model, secure deletion, a complete training-data
> lineage or measured governance effectiveness.
> **As of:** Reported first programme year; published 2025-07-04.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md),
> `SRC-0050-C02`–`C04`; Results and Figure 2, pp. 2–4; Discussion, p. 7;
> Methods, pp. 8–10.
> **Basis / limits:** Gates, monitoring and two sunset actions are direct.
> Drift-based retirement authority is prospective and is not silently called
> the observed cause of those two sunsets.

## Reproducible development and model-state segment

mlf-core reports an explicit project path through templates, dependency-
managed Conda/Docker environments, CI, training, linting, hardware and
parameter logging, model Registry storage, evaluation and optional REST
serving. Its experiments support bit-exact repeatability only when relevant
software/hardware state is controlled; different hardware and some multi-GPU
settings break the result.

> **Claim record — WFL-0013-C03 | source-report**
> **Claim:** A primary biomedical MLOps study directly instantiates a bounded
> environment→train/analyse→record→evaluate→register/serve segment and tests
> reproducibility limits across software and compute state.
> **Claim status:** active
> **Scope:** Reported 2023 framework and three biomedical use cases; not a live
> production service, current code/container audit, clinical validation,
> ongoing drift monitor or retirement process.
> **As of:** Publication 2023-04-02.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md),
> `SRC-0051-C02`–`C06`; main pp. 2–7; Supplement pp. 2–23.
> **Basis / limits:** Workflow and same-infrastructure results are direct.
> Determinism does not establish accuracy, security, fairness or biological
> validity.

## Reconciled lifecycle

| Phase | Required state or decision | Direct evidence contribution | Preserved boundary |
| --- | --- | --- | --- |
| 1. Intake and intended use | biological/clinical purpose, affected users, owner and deploy-or-research decision | MSK intake/G1; ETSI `5.1.2` | stated purpose is not authorization or feasibility |
| 2. Acquire, curate and label | source, sensitivity, provenance, quality and intended-use fit of biological/clinical data | MSK MIS/risk factors; mlf-core use-case datasets; ETSI `5.1.2-3`, `5.2.4` | package does not demonstrate one complete acquisition/label history |
| 3. Fix environment and dependencies | code, package/container, hardware, configuration and access state | mlf-core templates/containers/logging; ETSI asset/version controls | deterministic environment is not secure or correct by itself |
| 4. Train, adapt or analyse | model training/inference or bounded analysis with recorded parameters | mlf-core biomedical workflows; MSK model build path | no universal algorithm or biological task is implied |
| 5. Validate and risk-assess | held-out/task-fit evaluation, failure limits, security testing and responsible-use assessment | mlf-core experiments; MSK G3; ETSI `5.2.5` | internal validation is not prospective outcome evidence |
| 6. Register and authorize | model/MIS identity, version, owner, risk and approval decision | MSK Registry/G3–G4; mlf-core model Registry | governance-metadata and binary registries are distinct concepts |
| 7. Deploy and infer | controlled promotion/integration and communicated limitations | MSK production gate; ETSI `5.3`; mlf-core REST capability | capability to serve is not evidence of a live safe service |
| 8. Monitor production | logs, performance/error, drift, adoption, safety events and review date | MSK G4–G5; ETSI `5.4.2` | monitoring design does not prove detection or harm reduction |
| 9. Update, retrain or roll back | versioned change, retest, preview/staging, release and recovery decision | ETSI `5.4.1`; TR `6.11`; MSK major-revision review | TR examples are informative; no update result is measured |
| 10. Pause, retire and dispose | sunset/decommission decision, ownership transfer and secure data/configuration disposition | two MSK sunsets; ETSI `5.5.1`; TR `6.13` | model sunset and verified secure deletion are not the same event |

> **Claim record — WFL-0013-C04 | analytic-judgment**
> **Claim:** Reconciled across the independent ETSI, MSK oncology and mlf-core
> lineages, the workflow covers acquisition/curation through training,
> validation, deployment/inference, monitoring/update and retirement with
> explicit provenance/reproducibility state.
> **Claim status:** active
> **Scope:** Source-supported canonical lifecycle coverage; not one end-to-end
> deployed system, universal biological procedure, complete label lineage,
> verified deletion or causal effectiveness result.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `WFL-0013-C01`–`C03`; [SYS-0013](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md),
> `SYS-0013-C01`–`C04`.
> **Basis / limits:** Every named lifecycle class has direct support, and the
> generic post-deployment baseline is stitched to direct biomedical research
> and oncology implementation. The joined sequence is wiki analysis rather
> than a source-reported single workflow.

## Provenance and reproducibility record

A defensible lifecycle record keeps distinct but joinable identities for:

- source data, labels/annotations, sensitivity and intended use;
- code, packages, container/runtime and hardware;
- training configuration, parameters, metrics and model version;
- validation/risk decision and Registry/MIS entry;
- deployment/interface/version state;
- monitoring, drift/error/safety evidence and major revisions; and
- pause, sunset, transfer, decommission and disposition decisions.

ETSI requires many of these states, mlf-core implements and tests a bounded
development subset, and MSK reports operational governance/monitoring state.
No retained source provides one export joining every field or independently
reproduces a complete production model.

## Evidence-state audit

| Evidence question | State |
| --- | --- |
| Complete lifecycle classes | direct across three independent lineages |
| Direct biological/clinical deployment | yes, one-centre governance implementation |
| Direct production monitoring | yes, programme process and reported model reviews; no evaluated cyber outcome |
| Direct retirement | two evidence-driven model sunsets; secure-disposal verification absent |
| Provenance/reproducibility method | direct and empirically bounded in mlf-core; current runtime reproduction not performed |
| One complete acquisition-to-disposition record | not demonstrated |
| Independent effectiveness evaluation | absent |

> **Claim record — WFL-0013-C05 | analytic-judgment**
> **Claim:** `WFL-0013` is a complete **coverage map** and includes direct
> biomedical implementation segments, but it is not evidence that one model
> traversed every stage reproducibly, securely or effectively.
> **Claim status:** active
> **Scope:** Workflow evidence-state classification; not a claim of missing
> practice at any represented organization.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> EN Introduction, p. 5, and `5.1.2–5.5.1`, pp. 10–15;
> [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md),
> Results and Figure 2, pp. 2–4, Discussion, p. 7, and Methods, pp. 8–10;
> [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md),
> Methods/Results and Figures 1–2, pp. 2–4, Discussion, pp. 6–7, and
> Supplementary Methods, pp. 17–23.
> **Limits:** Cross-source coverage and source independence are direct
> enough for lifecycle mapping. Missing joined records, independent evaluator
> and outcomes prevent implementation/effectiveness overclaiming.

## Related pages

- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SRC-0049 — ETSI AI cybersecurity package](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md)
- [SRC-0050 — Oncology AI governance implementation](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md)
- [SRC-0051 — Reproducible biomedical MLOps](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md)
- [SYS-0013 — Biological MLOps infrastructure and trust boundaries](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md)

## Sources

- [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md), exact EN/TR locators above.
- [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md), exact article locators above.
- [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md), exact main/supplement locators above.
