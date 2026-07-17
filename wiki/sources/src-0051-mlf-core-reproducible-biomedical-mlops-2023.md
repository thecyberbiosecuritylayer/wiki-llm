---
id: SRC-0051
type: source
title: mlf-core reproducible biomedical MLOps and determinism study 2023
aliases:
  - mlf-core a framework for deterministic machine learning
  - Heumos et al. mlf-core
  - deterministic biomedical MLOps
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: peer-reviewed-primary-software-and-empirical-method-study
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/heumos-mlf-core-deterministic-machine-learning-2023.pdf
raw_bytes: 3241915
sha256: cf42dcf775d6fc4ee7a918ff2e2eb1c6b7ac1f427d7ca484453a1281fd7ffcb1
raw_components:
  - path: ../../raw/heumos-mlf-core-supplementary-data-2023.pdf
    role: complete-publisher-supplementary-methods-tables-and-figures
    bytes: 3434595
    sha256: 8d5950c19747b3feb79040e75537248686aad8e3e16952e17cb8e23fe7c28e24
  - path: ../../raw/heumos-mlf-core-pmc-v1.json
    role: official-pmc-open-data-version-and-bibliographic-record
    bytes: 1279
    sha256: 4ea44e9028b56f96767affb03f6ae4e7eaeadfec0dbfb3db6441798ab126fa5b
canonical_url: https://academic.oup.com/bioinformatics/article/39/4/btad164/7099608
direct_pdf_url: https://pmc-oa-opendata.s3.amazonaws.com/PMC10089676.1/PMC10089676.1.pdf
supplement_url: https://pmc-oa-opendata.s3.amazonaws.com/PMC10089676.1/btad164_supplementary_data.pdf
pmc_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10089676/
doi: 10.1093/bioinformatics/btad164
pmcid: PMC10089676
pmid: 37004171
accessed: 2026-07-12
publication_date: 2023-04-02
publisher: Oxford University Press, Bioinformatics
version: PMC Open Data article version 1; publisher version of record
license: CC-BY-4.0
authors:
  - Lukas Heumos
  - Philipp Ehmele
  - Luis Kuhn Cuellar
  - Kevin Menden
  - Edmund Miller
  - Steffen Lemke
  - Gisela Gabernet
  - Sven Nahnsen
tags:
  - artificial-intelligence
  - biomedical-machine-learning
  - reproducibility
  - determinism
  - mlops
  - docker
  - containers
  - model-registry
  - cloud
  - api
  - primary-empirical-study
---

# mlf-core reproducible biomedical MLOps and determinism study 2023

## Identity, acquisition and complete artifact review

Heumos et al., *mlf-core: a framework for deterministic machine learning*,
`Bioinformatics` 39(4), btad164 (2023), DOI
`10.1093/bioinformatics/btad164`, combines a software-framework description
with empirical determinism experiments and three biomedical use cases.

- The retained main publisher PDF is 3,241,915 bytes and eight physical/
  printed pages. The complete 25-page supplementary PDF is 3,434,595 bytes;
  the PMC version-1 JSON is 1,279 bytes. The package totals 6,677,789 bytes.
- All three objects were retrieved twice from the official NLM PMC Open Data
  versioned paths on 2026-07-12 and each pair was byte-identical.
- All 33 PDF pages were text-reviewed. Main-paper Figures 1–2 and their
  architecture captions on p. 3 were rendered and visually checked; the
  supplement's tables, figures and methods were included in locator review.
- The main PDF is unencrypted, untagged PDF 1.3; the supplement is
  unencrypted, untagged PDF 1.4. `pdfinfo` reports no form or JavaScript and
  `pdfdetach` reports no embedded files. `pdfsig` reported no signatures
  after an NSS initialization warning, so no cryptographic-authenticity claim
  is made.
- The PMC JSON identifies version 1, CC BY, the DOI/PMID and
  `is_retracted: false`. This is current repository metadata, not a review of
  the current state of linked code, containers, documentation or services.

> **Claim record — SRC-0051-C01 | artifact-observation**
> **Claim:** The retained 6,677,789-byte package contains the complete
> publisher paper, complete 25-page supplement and official PMC version
> record, with byte-identical repeat retrievals and complete page review.
> **Claim status:** active
> **Scope:** Artifact identity, completeness and static review; not execution
> of the framework, reproduction of experiments, current repository audit or
> digital-signature validation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Main PDF pp. 1–8; Supplement pp. 1–25; PMC version-1 JSON;
> frontmatter byte counts and SHA-256 values.
> **Basis / limits:** Artifact state is direct. Main paper, supplement and PMC
> metadata are one author/publication lineage.

## Framework and empirical method

The authors define deterministic ML narrowly as reproducing bit-exact results
from complete documentation and model code on the **same computational
infrastructure**. They argue that fixed random seeds alone are insufficient
because libraries and parallel hardware can select nondeterministic
operations.

The core experiment compared three configurations—uncontrolled/random,
seeds-only and seeds plus enforced deterministic algorithms—across PyTorch,
TensorFlow and XGBoost, with CPU, single-GPU and multi-GPU settings. The
supplement records hardware, library versions, evaluation settings and model-
specific methods. This evaluates a narrow reproducibility property; it is not
a security, robustness, accuracy or clinical-outcome evaluation.

> **Claim record — SRC-0051-C02 | source-report**
> **Claim:** The study experimentally compares random, seeds-only and fully
> constrained deterministic configurations across three ML libraries and
> multiple compute settings, with a same-infrastructure definition of
> bit-exact determinism.
> **Claim status:** active
> **Scope:** Represented software versions, hardware and experimental models;
> not all ML libraries, cross-hardware reproducibility, semantic correctness,
> clinical validity, adversarial robustness or current mlf-core behavior.
> **As of:** Experiments reported in the 2023 publication.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Abstract/Introduction, pp. 1–2; Methods `2.1–2.2`, pp. 2–3;
> Results `3.2`, pp. 4–5; Supplementary Table S1 and Figures S1–S6,
> Supplement pp. 2 and 4–9; Supplementary Methods, pp. 17–19.
> **Basis / limits:** Configurations and evaluation design are direct. The
> authors developed and evaluated their own framework, so this is primary
> developer evidence rather than independent replication.

## Packages, containers, registry, cloud and API map

The paper makes several MLOps classes unusually explicit:

- the ecosystem contains the `mlf-core` and `system-intelligence` Python
  packages, community models and GPU-enabled Docker containers;
- project templates use Conda or Docker for isolated dependency-managed
  runtimes and GitHub Actions for continuous integration/container building;
- runs log hyperparameters, metrics, hardware and trained models through
  MLflow/TensorBoard and save models to a specified model registry;
- MLflow integration can serve a model through a REST API;
- training and inference are described for common cloud providers and Apache
  Spark; and
- template sync/versioning and static linting support ongoing maintenance.

These are reported framework capabilities and architecture, not a retained
container image, dependency lockfile, registry export, live API or verified
cloud deployment.

> **Claim record — SRC-0051-C03 | source-report**
> **Claim:** mlf-core directly instantiates a biomedical/research MLOps map
> containing Python packages, Conda/Docker containers, CI, experiment and
> hardware tracking, a model registry, REST serving and cloud/distributed
> compute.
> **Claim status:** active
> **Scope:** Reported 2023 framework and use-case workflow; not current
> package/container integrity, an SBOM, notebook environment, IAM boundary,
> production service, monitored deployment or model retirement.
> **As of:** Publication 2023-04-02.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Introduction and Table 1, pp. 1–2; Methods `2.1`, pp. 2–3;
> Results `3.1` and Figures 1–2, pp. 3–4; Supplementary Methods, pp. 17–19.
> **Basis / limits:** Classes and capabilities are direct in prose/captions
> and visually verified. Linked GitHub, container, documentation and service
> resources were not ingested or executed.

## Determinism results and failure limits

For the represented models, repeated runs under the complete deterministic
configuration produced exact results when infrastructure/hardware was held
constant. The paper also reports boundaries that prevent overclaiming:

- models run on different hardware still produced different results even
  with deterministic settings;
- represented multi-GPU XGBoost runs remained nondeterministic;
- deterministic settings sometimes increased runtime; and
- the software stack, compiled dependency versions and hardware architecture
  have to remain controlled.

> **Claim record — SRC-0051-C04 | source-report**
> **Claim:** The empirical result supports bit-exact repeatability for tested
> configurations on held-constant infrastructure, while directly showing
> cross-hardware and some multi-GPU failure limits plus possible runtime cost.
> **Claim status:** active
> **Scope:** Evaluated models, libraries, versions and machines; not universal
> determinism, cross-platform reproducibility, model accuracy, biological
> validity, deployment reliability or independent reproduction.
> **As of:** Experiments reported in 2023.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Results `3.2`, pp. 4–5; Discussion, pp. 6–7; Supplementary
> Figures S3–S6, pp. 6–9; Supplementary Methods, pp. 17–19.
> **Basis / limits:** Within-study results and caveats are direct. The word
> `deterministic` is not normalized to secure, unbiased, correct or safe.

## Biomedical use cases

The authors apply the framework to three biomedical contexts: a TensorFlow
autoencoder for single-cell RNA sequencing, an XGBoost liver-cancer classifier
using gene-expression data, and a PyTorch U-Net for liver-tumour segmentation
of CT images. Nondeterministic runs changed cell clustering/visualization and
gene-feature importance; constrained runs held the represented outputs
constant. The segmentation case compares repeated prediction/metric state.

> **Claim record — SRC-0051-C05 | source-report**
> **Claim:** The study directly connects MLOps determinism to biomedical data
> and model outputs in single-cell analysis, liver-cancer gene-expression
> classification and liver-tumour CT segmentation.
> **Claim status:** active
> **Scope:** Three author-selected methodological use cases; not prospective
> diagnosis, downstream treatment, biological experiment outcome, population
> generalization or demonstrated patient benefit/harm.
> **As of:** Publication 2023-04-02.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Abstract/Introduction, pp. 1–2; Results `3.3.1–3.3.3`,
> pp. 4–6; Discussion, pp. 6–7; Supplementary Table S2 and Figures S7–S15,
> pp. 3 and 10–16; biomedical Supplementary Methods, pp. 19–23.
> **Basis / limits:** Inputs, models and within-study output differences are
> direct. Reproducible output does not establish biological truth or clinical
> utility.

## Reproducibility requirements and evidence boundary

The Discussion summarizes five requirements: set all relevant seeds; enforce
deterministic algorithms; containerize the runtime; log and hold hardware
constant; and document training, parameters, metrics and code. Those
requirements support provenance and repeatability but do not cover production
monitoring, drift, security response, model retirement or derivative-data
disposition.

> **Claim record — SRC-0051-C06 | source-report**
> **Claim:** The paper directly supports a joined provenance/reproducibility
> record across code, parameters, software/container environment, hardware,
> metrics and model state, with explicit same-infrastructure limits.
> **Claim status:** active
> **Scope:** Deterministic research workflow and reported resources; not an
> independently reproduced end-to-end run, complete data lineage, production
> audit trail or deployed lifecycle.
> **As of:** Publication 2023-04-02.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Results/Figures 1–2, pp. 3–4; Discussion requirements,
> pp. 6–7; Supplementary Methods, pp. 17–23.
> **Basis / limits:** Required state classes are direct. Current code/data
> availability, pinned dependencies and runtime reproduction were not tested
> in this transaction.

> **Claim record — SRC-0051-C07 | analytic-judgment**
> **Claim:** `SRC-0051` is an independent primary biomedical MLOps lineage for
> containers, model registry, cloud/API boundaries and empirical
> reproducibility limits, but not a live deployment, independent evaluator,
> security test, drift monitor, retirement process or effectiveness result.
> **Claim status:** active
> **Scope:** Evidence classification for lifecycle/system reconciliation; not
> a judgment that the software is ineffective or insecure.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0051-C02`–`C06`; author affiliations and framework
> development statements, pp. 1–3.
> **Basis / limits:** The architecture and experiments are direct primary
> evidence. Developer–evaluator overlap and uninspected current resources
> prevent independent or current-operational promotion.

## Safety abstraction

This page retains only defensive reproducibility and system classes. It omits
model weights, live endpoints, credentials, patient data and implementation-
ready biological or medical procedures.

## Related pages

- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [VUL-0004 — AI exposure classes](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SRC-0049 — ETSI AI cybersecurity package](src-0049-etsi-european-ai-cybersecurity-standard-implementation.md)
- [SRC-0050 — Oncology AI governance implementation](src-0050-stetson-responsible-ai-governance-oncology-2025.md)
- [WFL-0013 — Secure biological-AI model lifecycle](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md)
- [SYS-0013 — Biological MLOps infrastructure and trust boundaries](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md)

## Sources

- Heumos et al., main publisher PDF, complete supplement and official PMC
  Open Data version record, exact locators above.
