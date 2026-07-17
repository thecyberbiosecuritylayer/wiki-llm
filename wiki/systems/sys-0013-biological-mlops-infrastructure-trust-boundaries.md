---
id: SYS-0013
type: system
title: Biological MLOps infrastructure and trust boundaries
aliases:
  - biological AI deployment infrastructure
  - biomedical MLOps system map
  - biological AI registry container and identity boundaries
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
    claim_id: SYS-0013-C01
    evidence:
      - source: SRC-0049
        locator: "EN clauses 5.1.2 and 5.2.1–5.2.3, pp. 10–13; TR clauses 6.2.5, 6.5.2 and 6.6.2–6.6.6, pp. 25, 38–39 and 42–46"
  - predicate: evidenced-by
    target: SRC-0051
    claim_id: SYS-0013-C02
    evidence:
      - source: SRC-0051
        locator: "Main paper pp. 2–4, especially Figures 1–2; Supplementary Methods pp. 17–19"
  - predicate: evidenced-by
    target: SRC-0050
    claim_id: SYS-0013-C03
    evidence:
      - source: SRC-0050
        locator: "Results pp. 2–4; Methods and Figure 6 pp. 9–10"
  - predicate: depends-on
    target: WFL-0013
    claim_id: SYS-0013-C04
    evidence:
      - source: SRC-0049
        locator: "EN lifecycle and infrastructure provisions, pp. 5 and 10–15"
      - source: SRC-0050
        locator: "Figure 2 p. 3 and Figure 6 p. 10"
      - source: SRC-0051
        locator: "Figures 1–2 p. 3 and serving/cloud text p. 4"
tags:
  - artificial-intelligence
  - biological-models
  - mlops
  - system-boundaries
  - containers
  - model-registry
  - cloud
  - hpc
  - api
  - identity
---

# Biological MLOps infrastructure and trust boundaries

## Scope and evidence rule

This system page reconciles a generic security baseline with two direct
biomedical/clinical system descriptions. It maps classes and trust crossings,
not a deployable reference architecture. No endpoint, credential, image tag,
package version, patient record, model weight or instrument-control command is
included.

The source roles remain distinct:

- ETSI EN provides current normative security functions; its TR adds
  informative examples and is not a second lineage.
- mlf-core reports a biomedical research MLOps implementation and developer-
  evaluated framework, not a current production audit.
- MSK reports a high-level real oncology platform and governance deployment,
  not a validated cybersecurity topology.

## Generic security and identity baseline

ETSI requires inventory of AI assets and interdependencies, authentication
and version control, protection of confidential data/weights, secure APIs,
dedicated development/tuning environments, least privilege, supply-chain
processes and cloud responsibility. Its informative TR explicitly names
libraries, programming packages, container images, model registries, package
repositories, RBAC/MFA, CI-mediated promotion and API gateways.

> **Claim record — SYS-0013-C01 | source-report**
> **Claim:** ETSI supplies a generic MLOps security boundary spanning external
> components, data/models, dedicated environments, APIs/cloud and identity/
> least privilege, with informative examples for packages, containers and
> model registries.
> **Claim status:** active
> **Scope:** Cross-sector requirements and examples; not a biological system,
> one topology, verified IAM, SBOM/ML-BOM, validated image or implemented
> control.
> **As of:** EN V2.1.1 and package status reviewed 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> `SRC-0049-C02/C05`; EN `5.1.2`, pp. 10–11 and `5.2.1–5.2.3`, pp. 12–13;
> TR `6.2.5`, p. 25, `6.5.2`, pp. 38–39 and `6.6.2–6.6.6`, pp. 42–46.
> **Basis / limits:** EN boundaries are normative. The literal container/model-
> registry implementations are TR examples tied to the predecessor TS and
> cannot be promoted to tested EN conformance.

## Biomedical research MLOps instance

mlf-core's figures and prose connect Python packages, templates, Conda/Docker
runtime isolation, GPU containers, CI, linting, parameter/metric/hardware
tracking, trained models in a Registry, visualization, REST serving and
cloud/Spark compute. The authors apply it to single-cell, gene-expression and
CT-segmentation models.

> **Claim record — SYS-0013-C02 | source-report**
> **Claim:** mlf-core directly instantiates a biomedical MLOps dependency graph
> from package/template and containerized compute through training/tracking to
> a model Registry and optional REST/cloud interface.
> **Claim status:** active
> **Scope:** Reported 2023 framework and use cases; not current package or
> container integrity, live API, production identity boundary, monitoring,
> retirement or independent framework evaluation.
> **As of:** Publication 2023-04-02.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md),
> `SRC-0051-C03/C05/C06`; main pp. 2–4, especially Figures 1–2;
> Supplementary Methods, pp. 17–23.
> **Basis / limits:** Components and connections are direct. Linked code,
> registries, images and services were neither retained nor executed.

## Oncology deployment instance

MSK's architecture connects multimodal, clinical, research, enterprise and
departmental data to access/virtualization, production support, experiment
tracking, high-performance compute, clinical/EHR/radiology/pathology contexts,
authentication/administration/monitoring/logging, containers/orchestration
and multi-cloud/on-premises infrastructure. Separate prose describes secure
PHI/de-identified sandboxes, an MIS Registry/dashboard and governance gates.

> **Claim record — SYS-0013-C03 | source-report**
> **Claim:** A primary oncology implementation directly supplies containers/
> orchestration, on-prem/cloud and HPC, diverse clinical data/application
> classes, authentication/logging and a governance Model Registry in one
> high-level institutional platform map.
> **Claim status:** active
> **Scope:** Reported MSK architecture/governance classes; not validated
> network or data-flow topology, complete database/instrument inventory, IAM
> test, model-binary registry, package inventory or transferable reference
> implementation.
> **As of:** Reported programme year; published 2025-07-04.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md),
> `SRC-0050-C03/C05`; Results pp. 2–4; Methods pp. 9–10, especially Figure 6
> and Registry/sandbox descriptions.
> **Basis / limits:** Classes are direct in text or visually verified. The
> source explicitly labels Figure 6 a high-level description and supplies no
> cyber-assurance result.

## Reconciled system and dependency map

| Layer | Direct classes | Key dependency/trust crossing | Boundary retained |
| --- | --- | --- | --- |
| Biological/clinical data | single-cell, gene-expression, CT/multimodal, clinical, research and departmental data | source/custodian → controlled analysis or training environment | digital records do not establish specimen/instrument provenance |
| Package and environment | Python packages, libraries, templates, Conda, external components | supplier/repository → developer/runtime | cited package is not a verified current artifact |
| Container and orchestration | Docker/GPU containers; institutional container/orchestration layer | build/CI → isolated runtime → production platform | containerization does not itself prove isolation or integrity |
| Compute and storage | CPU/GPU, HPC, on-premise, multi-cloud and distributed compute | institution/operator ↔ cloud/compute provider | capacity, tenancy and resilience are not tested |
| Model and registry | weights/checkpoints, run artifacts, binary Registry; MIS/governance Registry | training/evaluation → versioned model or metadata record → release gate | registry meanings differ and are not interchangeable |
| Interface/application | REST/API, model service, EHR/radiology/pathology/ambient and enterprise applications | model service → integrating application → user/workflow | serving capability is not authorization or clinical validity |
| Identity and governance | developers, system operators, data custodians, AIGC, RBAC/MFA examples, authentication/admin | human/service identity → data, model, pipeline and approval privilege | no complete identity hierarchy or access test is represented |
| Monitoring and change | logs, experiment/metric tracking, performance/drift, release/update state | production telemetry → operator/governance decision → update/pause | logging does not prove detection, response or recovery |
| End of life | sunset/decommission, model/data/configuration disposition | active service/registry → retired and retained/deleted state | observed sunset is not verified secure deletion |

> **Claim record — SYS-0013-C04 | analytic-judgment**
> **Claim:** Reconciled across ETSI, mlf-core and MSK, the system map directly
> covers packages, containers, cloud/HPC, APIs, two forms of model registry and
> identity boundaries for biomedical/clinical MLOps, including deployment,
> monitoring and end-of-life dependencies.
> **Claim status:** active
> **Scope:** Canonical class/dependency coverage; not one deployed topology,
> complete database/notebook/instrument inventory, verified interface,
> authorization map or secure configuration.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYS-0013-C01`–`C03`;
> [WFL-0013](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md),
> `WFL-0013-C01`–`C04`.
> **Basis / limits:** Each named class has direct support, including direct
> biological/clinical instances. The normalized layer graph is wiki analysis,
> and no source claims all components coexist in one system.

## Registry semantics

`Model Registry` is not one stable asset class across the sources:

- mlf-core's Figure 2 says training runs save models in a specified Registry,
  indicating model/run artifact storage;
- MSK describes its Registry as a repository/dashboard of Model Information
  Sheets and operational status; and
- ETSI TR uses a Registry as an asset/version-control and promotion example.

The wiki therefore preserves at least `model-artifact registry` and
`governance-metadata registry` as separate logical stores even if one product
can implement both.

> **Claim record — SYS-0013-C05 | analytic-judgment**
> **Claim:** The reconciled architecture distinguishes binary/run-artifact
> Registry state from governance/MIS Registry state and requires identity,
> version and promotion links rather than treating the word `registry` as one
> self-proving control.
> **Claim status:** active
> **Scope:** Semantic reconciliation of direct source uses; not a prescribed
> product design, claim of physical separation or implemented linkage.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md),
> Figure 2, p. 3;
> [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md),
> Registry description, p. 10;
> [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> TR `6.5.2`, pp. 38–39 and `6.6.3`, p. 44.
> **Limits:** Different source meanings are explicit. The logical
> distinction prevents an unsupported inference that metadata registration
> proves model-binary provenance or vice versa.

## Literal coverage and unresolved boundaries

| Frozen system literal | This package |
| --- | --- |
| Packages | direct in mlf-core and ETSI TR |
| Containers | direct in mlf-core, MSK Figure 6 and ETSI TR |
| Notebooks/workbenches | **not directly established by these three sources** |
| Cloud/HPC | direct in MSK; cloud/distributed compute also in mlf-core and EN |
| APIs | direct in mlf-core and EN/TR |
| Model registries | direct in all three, with reconciled meanings |
| Databases/instruments | clinical/research data and EHR/imaging applications are direct; a laboratory database/instrument topology is not |
| Identity boundaries | direct in EN, TR examples and MSK Figure 6/governance roles |

This package directly closes container and model-registry gaps and adds a
second biological/clinical architecture lineage. It does not silently turn a
sandbox into a notebook, an imaging application into an instrument inventory,
or a data source into a database topology.

> **Claim record — SYS-0013-C06 | analytic-judgment**
> **Claim:** `SYS-0013` is strong direct evidence for the previously missing
> container and model-registry classes and for independent deployed biological
> MLOps boundaries, but it is not a standalone complete notebook/database/
> laboratory-instrument map or architecture-assurance result.
> **Claim status:** active
> **Scope:** Literal-coverage and evidence-state audit of this source package;
> not a claim that represented organizations lack omitted components.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYS-0013-C01`–`C05`; full source reviews and exact table
> locators above.
> **Basis / limits:** Present/absent literals were checked directly. Full
> domain coverage requires reconciliation with a separate biological data,
> repository, notebook and laboratory-system lineage.

## Safety abstraction

Only high-level defensive component and trust-boundary classes are retained.
No live target, network address, credential, package exploit, container tag,
patient-level value, model parameter or instrument-control path is exposed.

## Related pages

- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [TEC-0002 — AI transfer techniques](../techniques/tec-0002-ai-data-model-manipulation-and-extraction.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SRC-0049 — ETSI AI cybersecurity package](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md)
- [SRC-0050 — Oncology AI governance implementation](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md)
- [SRC-0051 — Reproducible biomedical MLOps](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md)
- [WFL-0013 — Secure biological-AI model lifecycle](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md)

## Sources

- [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md), exact EN/TR locators above.
- [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md), exact article locators above.
- [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md), exact paper/supplement locators above.
