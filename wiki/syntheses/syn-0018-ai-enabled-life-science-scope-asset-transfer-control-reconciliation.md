---
id: SYN-0018
type: synthesis
title: AI-enabled life-science scope, asset, transfer and control reconciliation
aliases:
  - AIB ST AS XT CT reconciliation
  - biological AI four-cell SF2 audit
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0005
  - SRC-0006
  - SRC-0014
  - SRC-0032
  - SRC-0033
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: SYN-0018-C01
    evidence:
      - source: SRC-0005
        locator: "§§2.1, 3.5 and 4.1, printed pp. 3–4, 11 and 13–15 (PDF pp. 12–13, 20 and 22–24)"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: SYN-0018-C01
    evidence:
      - source: SRC-0006
        locator: "§§1.2 and 5.1–5.12, printed pp. 4–7 and 21–28 (PDF pp. 15–18 and 32–39); Tables 10–36"
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: SYN-0018-C01
    evidence:
      - source: SRC-0014
        locator: "Abstract, Introduction, §§3, 5–7 and Figures 1–5, printed pp. 765–778 (PDF pp. 2–15)"
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: SYN-0018-C01
    evidence:
      - source: SRC-0032
        locator: "System and transfer paths, printed pp. 10, 14–15, 23–24, 48–57 and 90–99 (physical pp. 16, 20–21, 29–30, 54–63 and 96–105)"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: SYN-0018-C01
    evidence:
      - source: SRC-0033
        locator: "Summary, printed pp. 1–8 (physical pp. 22–29); Chapters 1–5, printed pp. 9–84 (physical pp. 30–105); attributed Appendix A, printed pp. 85–141 (physical pp. 106–162)"
tags:
  - artificial-intelligence
  - bioinformatics
  - biological-models
  - assets
  - cross-domain-transfer
  - controls
  - evidence-reconciliation
---

# AI-enabled life-science scope, asset, transfer and control reconciliation

## Question, cutoff and strict method

This synthesis tests exactly four frozen cells after `SRC-0033`: `AIB-ST`,
`AIB-AS`, `AIB-XT` and `AIB-CT`. The evidence cutoff is 2026-07-12. It applies
the literal criterion, SF2 independence floor and anti-proxy/anti-duplication
rules in
[SYN-0001](syn-0001-coverage-rubric.md).

The test is conjunctive at cell level: every literal must have direct located
support somewhere in the reconciled union, and at least two materially
independent direct source lineages must support the cell. It does not require
every source to repeat every literal. A conceptual/recommended function is not
implementation, an experiment is not an incident, a cited study is not an
ingested source, and report volume does not create independence.

No operational biological design, model prompt/weight, screening rule,
laboratory parameter, exploit sequence, target-specific weakness or facility
topology is required or reproduced.

## Evidence roles and lineage accounting

| Evidence line | Claim-appropriate role | Independence boundary |
| --- | --- | --- |
| NIST IR 8432/8467 (`SRC-0005/0006`) | genomics assets/stakeholders, provenance, data/software/configuration context, access, monitoring, response and recovery | one NIST/NCCoE programme lineage, not two independent lines |
| USENIX/Ney et al. (`SRC-0014`) | controlled material/input→sequencer→digital file/software pipeline, measured exposure and version-bounded software audit | one academic/experimental line; not an AI incident or current production deployment |
| AU DAS (`SRC-0032`) | agriculture observation/sensor→analytics/decision and digital advisory/control→farm/value-chain action | one AUC/PRIDA regional-strategy line; intended function, not incident/effectiveness |
| NASEM (`SRC-0033`) | biology-specific versus generic AI scope, biological model/data/software ecosystem, DBTL/model-output transfer, threat/control review and U.S. advice | one committee-report package; NCBI/NASEM mirrors, chapters, Appendix A and citations are not multiplied |

NASEM is institutionally and methodologically independent from the NIST,
USENIX and AU lines. NIST supplies the second direct line for assets and
controls; USENIX supplies the second direct pipeline line for scope; AU and
USENIX add independent transfer predicates. Lineage sufficiency is adjudicated
per cell rather than globally.

> **Claim record — SYN-0018-C01 | analytic-judgment**
> **Claim:** NASEM, the single NIST genomics programme line, USENIX and AU DAS
> form materially distinct claim-appropriate evidence roles: NASEM+USENIX
> support `AIB-ST`, NASEM+NIST support `AIB-AS/CT`, and NASEM+AU/USENIX support
> `AIB-XT`, without multiplying mirrors, programme siblings, Appendix A or
> citations.
> **Claim status:** active
> **Scope:** Frozen SF2 lineage accounting for four AIB cells; not blanket
> source equivalence, implementation, incident or effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C02/C03/C05/C07/C08/C10`;
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> `SRC-0005-C03/C05/C12`;
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> `SRC-0006-C02/C05/C07/C08/C11`;
> [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> `SRC-0014-C02/C04/C08`;
> [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C05/C06/C09`; exact frontmatter locators above.
> **Basis / limits:** Issuers, genres, methods and derivation are explicit.
> NIST 8432/8467 share a programme; NASEM Appendix A is commissioned background
> in the report package; AU companion material is not a second AU line.

## `AIB-ST` — scope and terms

| Literal element | Direct reconciled support | Boundary |
| --- | --- | --- |
| Bioinformatics pipelines | USENIX directly exercises physical DNA→sequencer→derived reads/files→downstream analysis software; NASEM separately places bioinformatics tools and scientific AI assistants within biological AI | controlled research pipeline is not generic AI or production prevalence |
| Statistical/ML models | NASEM distinguishes supervised/predictive, unsupervised/foundation and other biological model functions | Appendix taxonomy is same-lineage background, not independent support |
| Generative biological design | NASEM main report directly treats AI-enabled biological design and its DBTL boundary | no harmful design or current capability inventory is reproduced |
| Clinical/research deployment | NASEM covers research, surveillance/countermeasure and bounded clinical/decision contexts; USENIX directly supplies a research bioinformatics environment | intended/research use is not validated deployment or clinical outcome |
| Distinction from generic AI | NASEM scopes biology-specific/scientific AI and excludes general chatbot risk work from its central biological-tool analysis | one direct distinction is sufficient as a literal; SF2 applies to the whole cell, not each phrase |

The second lineage is substantive rather than terminological: USENIX gives a
direct bioinformatics pipeline and research environment, while NASEM supplies
the remaining frozen biological-AI category distinctions. The union therefore does
more than label all computation as AI.

> **Claim record — SYN-0018-C02 | analytic-judgment**
> **Claim:** `AIB-ST` passes: NASEM directly distinguishes biology-specific
> foundation/predictive/generative/design/assistant functions from generic AI,
> while independent USENIX evidence supplies the concrete bioinformatics
> pipeline and research-use/deployment-context class required by the same scope
> contract; “deployment” here is a scope category, not implementation evidence.
> **Claim status:** active
> **Scope:** Cell-level scope/terms coverage at SF2; not a current model
> catalogue, production deployment, incident or performance evaluation.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Summary, printed pp. 1–2 (physical pp. 22–23); Chapter 1, printed pp. 16–17
> (physical pp. 37–38); Chapters 2–5, printed pp. 19–81 (physical pp. 40–102);
> [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md), Abstract,
> Introduction and §3, printed pp. 765–771 (PDF pp. 2–8); `SRC-0033-C03`,
> `SRC-0014-C02/C08` and `SYS-0003-C06`.
> **Basis / limits:** Every literal has direct located support in the union and
> the two source lineages are materially independent. USENIX does not
> corroborate every AI category; the floor is cell-level and NASEM's generic-
> versus-biological distinction is not projected backward onto USENIX.

## `AIB-AS` — assets and stakeholders

| Literal class | NASEM biological-AI line | Independent NIST genomics line | Boundary |
| --- | --- | --- | --- |
| Datasets/labels | biological sequence/structure/function/omics, surveillance and experimental data, annotations and metadata | human/non-human genomic and derived data, annotations/provenance | predicted data are not experimental truth |
| Models/code | foundation, predictive, generative/design and assistant models; code/libraries/packages | software versions/configuration/analysis parameters in provenance | no source code, weights or executable package is included |
| Environments/dependencies | open-source dependencies, API and sandbox/workbench contexts | organization-specific system/data/software inventories | containers are not inferred here; that gap belongs to `AIB-SD` |
| Compute | cloud/HPC, repositories, storage and training/inference resources | cloud/service/provider roles and inventory outcomes | no capacity, tenancy or resilience result |
| Outputs/IP | predictions, scores, candidate designs, analyses, records and Figure 5-1 IP | explicit intellectual-property mission objective | no design or IP content is reproduced |
| Subjects/relatives | consented human-data participant case and user/institution roles | direct donor and relative privacy/consent objectives | applies only where human genomic data are processed |
| Developers | model/software developers, data stewards, infrastructure providers and laboratory operators | technology developer/provider and accountable organization roles | role class is not assigned responsibility in one deployment |
| Researchers | scientists, model users, data-access bodies and funders | researchers/education and authorized-use roles | no identity or organization is exposed |
| Decision makers | experimental reviewers, clinical/public-health/research users and agencies | trustworthy research/product/decision and access/authorization objectives | human role does not guarantee safe judgment |

This is the exact class map in `AST-0008`. Each literal appears somewhere in
the union; the claim does not say both institutions repeat every class.

> **Claim record — SYN-0018-C03 | analytic-judgment**
> **Claim:** `AIB-AS` passes: NASEM and the independent NIST genomics programme
> collectively provide direct coverage for datasets/labels, models/code,
> environments/dependencies, compute, outputs/IP, subjects/relatives,
> developers, researchers and decision makers.
> **Claim status:** active
> **Scope:** Cell-level biological-AI asset/stakeholder class coverage at SF2;
> not one universal inventory, ownership model, deployment or protection result.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [AST-0008](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md),
> `AST-0008-C01`–`C04` and canonical matrix;
> [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md), Chapters
> 2, 4 and 5, printed pp. 19–25 and 46–81 (physical pp. 40–46 and 67–102);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md), §§1.2
> and 5.1–5.12, printed pp. 4–7 and 21–28 (PDF pp. 15–18 and 32–39).
> **Basis / limits:** All nine literal classes are direct in the two-lineage
> union. NIST remains a draft genomics profile and NASEM a report-era broad AI
> synthesis; neither supplies an organization-specific completeness result.

## `AIB-XT` — cross-domain transfer

| Required direction | Full direct path | Independent support and boundary |
| --- | --- | --- |
| Biological data/input→digital output | NASEM: genomic/biological/epidemiological data→biology-specific model/analysis→detection, prediction, classification or design/decision-support output | USENIX directly exercises physical DNA→sequencer→digital reads/file→software outcome; AU independently supplies biological/environmental/sensor observation→transmission/analytics/AI/ML→surveillance/advisory decision. Controlled/intended states are not incidents |
| Model/design output→experimental, clinical or agricultural action | NASEM: model/design output→candidate selection/human scientific gate→physical build/test/experimental validation→result feedback; it separately describes decision-support uses | AU independently supplies digital advisory/control/record state→irrigation/input/equipment/certification/market action. It is an agricultural intended-use path, not malicious causality or outcome effectiveness |

The criterion says experimental, clinical **or** agricultural action. NASEM
directly closes the experimental branch and AU directly supplies an independent
agricultural action branch. No universal clinical human gate is inferred.

> **Claim record — SYN-0018-C04 | analytic-judgment**
> **Claim:** `AIB-XT` passes: NASEM supplies complete biological-data→digital-
> output and model/design-output→experimental-action paths; independent USENIX
> and AU evidence corroborate material/input→digital processing/decision and
> digital-output→agricultural-action directions without merging intended,
> controlled and adversarial states.
> **Claim status:** active
> **Scope:** Functional directionality at SF2; not a cyberattack, autonomous
> authority, clinical outcome, likelihood, deployment or effectiveness result.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 2 and Figure 2-1, printed pp. 19–20 (physical pp. 40–41); Chapter 4,
> printed pp. 46–50 (physical pp. 67–71); Figure 5-2, printed pp. 73–74
> (physical pp. 94–95); `SRC-0033-C04/C08`;
> [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md), Abstract and
> §3, printed pp. 765–771 (PDF pp. 2–8), `SRC-0014-C02/C08`;
> [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> printed pp. 10, 14–15, 23–24, 48–57 and 90–99, especially pp. 95–96
> (physical pp. 16, 20–21, 29–30, 54–63, 96–105 and especially 101–102),
> `SRC-0032-C05/C06`.
> **Basis / limits:** Both full NASEM directions and the independent
> controlled/intended comparators are direct. The reconciliation does not turn
> USENIX into AI, AU analytics into a hostile path or a functional output into
> a proven benefit/harm.

## `AIB-CT` — exact-edge control functions

The exact pipeline is:

`data/label origin → model/software/training-data lineage → analysis/design
output → validation and accountable gate → experiment/decision action →
feedback/monitoring → containment and trustworthy recovery`.

| Required function | Exact edge(s) addressed | Direct independent support | Boundary |
| --- | --- | --- | --- |
| Provenance | data/label/model/tool/dependency origin→training/analysis basis; output→affected downstream lineage | NASEM Chapter 5 plus NIST MO1 provenance | record existence is not completeness or truth |
| Access | contributor/repository→environment and user/API→model/tool use | NASEM fine-grained/sandbox cases plus NIST authorization/privacy outcomes | no universal IAM architecture or permitted-use conclusion |
| Versioning | data/software/configuration/parameter state→reproducible output and update review | NIST directly names versions/configuration/parameters; NASEM Figure 5-1 and software-dependency review | no complete model registry/checkpoint history |
| Reproducibility | data/context/dependency/evaluation state→repeatable analysis; prediction→experimental result distinction | NASEM data lifecycle/Appendix evaluation limits plus NIST provenance/assessment | cited benchmark is not an ingested successful replication |
| Monitoring | model/capability/data/software change→audit/anomaly/risk reassessment | NASEM continual assessment/pen test/audit plus NIST continuous monitoring | cadence, threshold and coverage unknown |
| Human review | model/design output→accountable scientific/screening/experimental decision gate | NASEM DBTL, screening and expert-review functions | human presence does not guarantee correctness |
| Recovery | suspect genomic data/system state→containment, affected data/results communication and verified restoration of a trustworthy basis; editorial mapping extends these functions to affected AI outputs and dependent decisions | NIST RMF/profile response/recovery line; NASEM supplies the AI-specific affected pipeline | output tracing and decision reassessment are exact-edge wiki normalization, not a literal NIST model-output rollback claim; NASEM alone lacks full recovery |

NASEM and NIST are the two independent control lineages. IR 8432/8467 are one
NIST programme, so their complementary functions count once. Control design is
not implementation, testing or effectiveness.

> **Claim record — SYN-0018-C05 | analytic-judgment**
> **Claim:** `AIB-CT` passes: independent NASEM and NIST lineages collectively
> cover provenance, access, versioning, reproducibility, monitoring, human
> review and recovery, with every function mapped to a named biological-AI
> pipeline/model edge and all implementation/effectiveness states left unknown.
> **Claim status:** active
> **Scope:** Cell-level exact-edge control-function coverage at SF2; not a
> universal baseline, implementation, successful test or independent
> effectiveness evaluation.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [CTL-0016](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md),
> `CTL-0016-C01`–`C06` and control matrix;
> [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md), Chapters
> 4–5, printed pp. 50–81 (physical pp. 71–102);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md), §5.1
> and Tables 10–12, 15–25 and 33, especially recovery Table 24, printed
> pp. 135–138 (PDF pp. 146–149);
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24).
> **Basis / limits:** NASEM supplies the AI-specific pipeline, provenance,
> access/evaluation/monitoring/human gates; NIST independently supplies genomic
> provenance/version/access/monitor/response/recovery. Mapping affected data/
> results and restored state onto AI outputs/dependent decisions is explicit
> editorial normalization; no source reports model-output rollback and no
> control outcome is observed.

## Cells deliberately not promoted

| Cell | State after this synthesis | Decisive missing predicate |
| --- | --- | --- |
| `AIB-WL` | Partial | no full acquisition/labeling→training→validation→deployment/inference→monitor/update→model-retirement lifecycle; data destruction is not model retirement |
| `AIB-SD` | Partial | no literal container map or model registry; a workbench/notebook and data repository do not substitute |
| `AIB-TV` | Partial | poisoning/tampering, software dependencies, bias/error and unsafe automation are strong, but literal model/data drift and confidentiality leakage remain unreconciled; train/test leakage is evaluation contamination |
| `AIB-CI` | Partial | no primary AI-biology incident/empirical study with measured consequence, model/dataset scope and SF3 evidence |
| `AIB-AE` | Absent | no ingested direct independent benchmark/deployment study with robustness/effectiveness, generalizability and failure limits |
| `AIB-GR` | Partial | NASEM is one nonbinding U.S. advisory line; no current AI/data/genomics/research/device reconciliation across at least two jurisdictions |

> **Claim record — SYN-0018-C06 | analytic-judgment**
> **Claim:** `AIB-WL/SD/TV/CI/GR` remain Partial and `AIB-AE` remains Absent;
> NASEM's review, recommendations, Appendix and citations do not supply model
> retirement, containers/registry, literal drift/confidentiality-leakage
> reconciliation, a primary incident, direct independent benchmark or current
> two-jurisdiction governance.
> **Claim status:** active
> **Scope:** Frozen-cell non-promotion audit; not a claim that the missing
> evidence does not exist outside the represented corpus.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C03`–`C11`; [WFL-0011](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md),
> `WFL-0011-C03/C04`; [SYS-0011](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md),
> `SYS-0011-C03/C04`; [RSK-0016](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md),
> `RSK-0016-C04`; [CTL-0016](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md),
> `CTL-0016-C06`; [GOV-0018](../governance/gov-0018-nasem-ai-life-sciences-advisory-recommendations-2025.md),
> `GOV-0018-C04/C05`.
> **Basis / limits:** Each blocker follows the literal frozen contract and
> evidence floor. Related citations are acquisition leads rather than silently
> imported primary evidence.

## Scoring decision

Exactly four cells change from Partial to Pass:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `AIB-ST` | Partial | **Pass** | complete cell-level scope/category map across independent NASEM and USENIX roles |
| `AIB-AS` | Partial | **Pass** | all nine asset/stakeholder classes across independent NASEM and NIST roles |
| `AIB-XT` | Partial | **Pass** | both complete NASEM directions plus independent USENIX/AU transfer support |
| `AIB-CT` | Partial | **Pass** | seven exact-edge control functions across independent NASEM and NIST roles |

The total moves from 42 to 46 Pass; Partial moves from 62 to 58; Absent remains
6. The score is **46/110 = 41.8%** and AIB becomes **4/10**. Critical cells
move from 39/50/2 to **43 Pass / 46 Partial / 2 Absent**. Dimensions at least
9/10 remain 1/11 and all 12 global-gate states remain 7 Pass / 5 Fail.

> **Claim record — SYN-0018-C07 | analytic-judgment**
> **Claim:** Strict SF2 reconciliation promotes exactly `AIB-ST`, `AIB-AS`,
> `AIB-XT` and `AIB-CT`, producing 46 Pass, 58 Partial and 6 Absent = 46/110
> (41.8%) and AIB 4/10; no other cell or global gate changes.
> **Claim status:** active
> **Scope:** Frozen rubric v1.0 after activation of this synthesis; not
> absolute domain completeness, implementation, incident, benchmark,
> governance adoption or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0018-C01`–`C06`; frozen criteria and prior zero-delta
> checkpoint `SYN-0001-C30`; source/canonical claims at exact locators above.
> **Basis / limits:** Only full literal SF2 contracts are promoted. The six
> non-promoted AIB cells retain explicit blockers; Partial/Absent both score
> zero and source volume does not alter the denominator.

## Related pages

- [SYN-0029 — AIB residual reconciliation](syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SYN-0001 — Coverage rubric](syn-0001-coverage-rubric.md)
- [SRC-0033 — NASEM AI/life-sciences report](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [AST-0008 — Biological AI assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [WFL-0011 — Biological AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [SYS-0011 — Biological AI ecosystem](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md)
- [RSK-0016 — Biological-AI output risk](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [CTL-0016 — Biological AI controls](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
- [GOV-0018 — NASEM advisory governance](../governance/gov-0018-nasem-ai-life-sciences-advisory-recommendations-2025.md)
- [SYS-0003 — Genomic sequencing/bioinformatics ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [SRC-0014 — Controlled bioinformatics pipeline evidence](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [SRC-0032 — Agriculture transfer evidence](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0034 — Later ProteinGym empirical benchmark](../sources/src-0034-notin-proteingym-benchmark-2023.md)
  — post-synthesis evidence for `AIB-CI/AE`; it does not alter this four-cell
  SF2 decision.

## Sources

- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md).
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md).
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md).
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md).
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md).
