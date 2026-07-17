---
id: SRC-0050
type: source
title: Stetson et al. responsible AI governance in oncology 2025
aliases:
  - Responsible Artificial Intelligence governance in oncology
  - MSK iLEAP AI lifecycle
  - MSK oncology AI model registry
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: peer-reviewed-primary-single-centre-governance-implementation-study
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/stetson-responsible-ai-governance-oncology-2025.pdf
raw_bytes: 3084909
sha256: 44084643bbfaac66815c1903794c40fd22d64c959038a8807b23c178f4794c03
raw_components:
  - path: ../../raw/stetson-responsible-ai-governance-oncology-pmc-v1.json
    role: official-pmc-open-data-version-and-bibliographic-record
    bytes: 1349
    sha256: 321f1ed2274f11b50206b1d0609014d1624f8f7e717eb2efec8b414292c904c8
canonical_url: https://www.nature.com/articles/s41746-025-01794-w
direct_pdf_url: https://pmc-oa-opendata.s3.amazonaws.com/PMC12227680.1/PMC12227680.1.pdf
pmc_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12227680/
doi: 10.1038/s41746-025-01794-w
pmcid: PMC12227680
pmid: 40615544
accessed: 2026-07-12
publication_date: 2025-07-04
publisher: Springer Nature, npj Digital Medicine
version: PMC Open Data article version 1; publisher version of record
license: CC-BY-NC-ND-4.0
authors:
  - Peter D. Stetson
  - January Choy
  - Natalia Summerville
  - Abigail Baldwin-Medsker
  - Janet Mak
  - Avijit Chatterjee
  - Kristen Kim
  - Chhavi Kumar
  - Patrick Samedy
  - Joanna Halperin
  - Louis Voigt
  - Justin Jee
  - Jill Fraser
  - MaryAnn Connor
  - Richard Harper
  - Rémy Evard
  - Anaeze C. Offodile 2nd
tags:
  - artificial-intelligence
  - oncology
  - clinical-ai
  - model-lifecycle
  - model-registry
  - deployment
  - monitoring
  - drift
  - model-retirement
  - primary-implementation
---

# Stetson et al. responsible AI governance in oncology 2025

## Identity, acquisition and complete artifact review

Stetson et al., *Responsible Artificial Intelligence governance in oncology*,
`npj Digital Medicine` 8, article 407 (2025), DOI
`10.1038/s41746-025-01794-w`, reports Memorial Sloan Kettering Cancer Center's
design and first year of a responsible-AI governance programme.

- The retained publisher PDF from the official NLM PMC Open Data versioned
  object is 3,084,909 bytes and 12 physical/printed pages. Its companion PMC
  version-1 JSON is 1,349 bytes; the two-object package totals 3,086,258
  bytes.
- Both objects were retrieved twice on 2026-07-12 and each repeat pair was
  byte-identical. The PMC record identifies the publisher DOI, version 1,
  `CC BY-NC-ND`, `is_retracted: false` and the PDF object's MD5.
- All 12 PDF pages were text-reviewed. Figure 2's lifecycle/gates on p. 3 and
  Figure 6's architecture on p. 10 were rendered and visually checked.
- The PDF is unencrypted, untagged PDF 1.4. Its AcroForm has an empty
  `Fields[]` array, its EmbeddedFiles name object is empty and its OpenAction
  is an internal page-fit destination. `pdfinfo` reports no JavaScript and
  `pdfdetach` reports zero embedded files. `pdfsig` found no signature after
  an NSS initialization warning, so cryptographic authenticity was not
  validated.

> **Claim record — SRC-0050-C01 | artifact-observation**
> **Claim:** The retained 3,086,258-byte package contains the complete
> publisher article and official PMC version record, with byte-identical
> repeat retrievals and complete page review.
> **Claim status:** active
> **Scope:** Artifact identity, completeness, static structure and local
> review; not independent replication, runtime inspection, digital-signature
> authentication or validation of the institution's underlying records.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Local PDF pp. 1–12; PMC version-1 JSON; frontmatter hashes and
> byte counts.
> **Basis / limits:** Bibliographic identity and bytes are direct. Nature and
> PMC manifestations are publication/provenance routes for one author-team
> study, not independent lineages.

## Study design and implementation boundary

The authors used a consensus-based approach to design governance tools and
then describe one year of real-world implementation at a single comprehensive
cancer centre. The programme covered clinical, operational and selected
research contexts through a multidisciplinary AI Governance Committee (AIGC),
an intake process, risk assessment, Model Information Sheet (MIS), Model
Registry and the iLEAP lifecycle.

The Abstract and Results report registration, evaluation and monitoring of 26
AI models including LLMs, two ambient-AI pilots and retrospective review of 33
live nomograms. Other counts have narrower denominators: the Registry then
contained 21 MIS records, the engineering team had supported 19 models and
performed 17 acquired-model risk assessments, and two of 19 live models had
qualified for the Express Path. These are retained as distinct programme
counts rather than normalized into one inventory total.

The Methods describe programme design, descriptive outputs and two
illustrative case studies. Authors were programme designers and implementers;
the paper is not an external audit or controlled comparison. Its data-
availability statement supplies no registry-level dataset for reanalysis.

> **Claim record — SRC-0050-C02 | source-report**
> **Claim:** The paper is a primary descriptive implementation study of one
> cancer centre's first-year AI governance programme, reporting 26 governed
> models, two ambient-AI pilots, 33 retrospectively reviewed live nomograms
> and multiple lifecycle/governance tools.
> **Claim status:** active
> **Scope:** MSK clinical, operational and research-adjacent programme
> activity over the reported year; not a randomized study, independent audit,
> complete underlying dataset, multi-centre result or clinical-effectiveness
> evaluation.
> **As of:** Study period ending in 2024/early 2025 as reported; publication
> 2025-07-04.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Abstract/Introduction, p. 1; Results, pp. 2–5; Discussion,
> p. 7; Methods and Table 4, pp. 8–10.
> **Basis / limits:** Programme counts, tools and method are direct. The
> authors' institutional implementation role prevents treating the report as
> independent evaluation of its own programme.

## Oncology AI lifecycle and decision gates

Figure 2 defines three paths—research, internally developed and acquired/co-
developed—and decision gates from idea/model proposal through registration,
MIS, monitoring plan and monitoring report. Research-only projects generally
remain under scientific/IRB review; when a research model moves toward
clinical or operational translation, AIGC review begins no later than the MIS
gate.

The transition from G3 MIS to G4 Monitoring Plan occurs after validation in a
testing environment and before production. Reported exit conditions include
registry entry, MIS completion, risk assessment and an AIGC review letter.
G5 is post-launch monitoring. The Registry tracks models by gate, while the
paper later clarifies that this Registry is a repository/dashboard of MIS
information and operational status—not necessarily a binary model-artifact
store.

> **Claim record — SRC-0050-C03 | source-report**
> **Claim:** MSK implemented an oncology-specific lifecycle that joins intake,
> model registration, risk/MIS review, validation, production authorization,
> monitoring planning and post-launch monitoring through explicit decision
> gates and a Model Registry.
> **Claim status:** active
> **Scope:** Reported governance lifecycle for in-scope MSK models; not every
> research model, source-data/label lineage, one mandatory development method,
> technical enforcement of every gate or proof that approval ensured safety.
> **As of:** Reported first programme year.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Results and Figure 2, pp. 2–3; monitoring discussion, p. 4;
> Methods, pp. 8–10, especially Table 4 and the Registry description on p. 10.
> **Basis / limits:** Gates, stated exit conditions and Registry purpose are
> direct. The lifecycle figure is an operating model, not evidence that all 26
> models traversed every gate.

## Monitoring, change and retirement evidence

The G5 monitoring model compares production and laboratory performance,
including precision, recall and F-measure for drift; it also considers
adoption, prespecified success metrics and AI-induced adverse-event rates.
Formal AIGC review is usually scheduled six to twelve months after go-live or
a major revision and tailored to model risk/workflow.

The study reports two different retirement predicates:

- **Observed:** retrospective G5 review of 33 live clinical nomograms resulted
  in two being sunset because clinical evidence had evolved (p. 3).
- **Prospective authority:** the Discussion anticipates acceleration,
  deceleration, sunsetting for drift/worsening/non-adoption, or rejection
  decisions (p. 7); p. 4 also says charter language on authority to pause or
  terminate degraded/unsafe models was being finalized.

These forms are not conflated. Two observed sunsets do not prove that the
prospective drift rule has been exercised or that the governance programme
caused improved clinical outcomes.

> **Claim record — SRC-0050-C04 | source-report**
> **Claim:** The programme directly implemented post-launch monitoring with
> drift/performance, adoption, success and safety measures, reported six-to-
> twelve-month or major-revision reviews, and actually sunset two live
> nomograms after evidence changed.
> **Claim status:** active
> **Scope:** Reported MSK governance actions and monitoring design; not a
> measured drift event for the two sunset models, secure data deletion,
> comparative control effectiveness or demonstrated patient benefit.
> **As of:** Reported programme year.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Results and Figure 2, pp. 3–4; Discussion/limitations, p. 7;
> technical-support methods, pp. 9–10.
> **Basis / limits:** Monitoring dimensions, cadence and the two evidence-
> driven sunsets are direct. Drift-based sunsetting is proposed authority, not
> the stated cause of those two observed actions.

## Infrastructure and trust-boundary evidence

The Methods describe centralized AI/ML engineering support from initial
design through post-launch monitoring, approved information-secure sandboxes,
on-premise and public-cloud operation, and research/platform groups that
validate models and move selected work into production.

Figure 6 visually represents multimodal, clinical, research, enterprise and
departmental data sources; data access and virtualized datasets; production
support; experiment tracking; high-performance computing; clinical/EHR,
radiology, pathology and ambient-model contexts; authentication,
administration, monitoring and logging; **containers and orchestration**; and
multi-cloud/on-premises infrastructure. The prose adds a prospective MIS
Registry/dashboard and PHI/de-identified generative-AI sandboxes.

> **Claim record — SRC-0050-C05 | source-report**
> **Claim:** The study provides a direct high-level oncology deployment map
> with diverse data sources, secure sandboxes, on-prem/public-cloud and HPC,
> containers/orchestration, production integration, authentication/logging,
> clinical systems and a governance Model Registry.
> **Claim status:** active
> **Scope:** Reported architecture classes and institutional boundaries; not a
> validated network diagram, container/package inventory, IAM configuration,
> interface test, model-binary registry or universal hospital architecture.
> **As of:** Reported programme year.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Results and Registry, pp. 2–4; Methods, pp. 9–10, especially
> Figure 6 and the sandbox/MLOps/Registry paragraphs.
> **Basis / limits:** Classes are direct in text or visually verified. Figure
> 6 explicitly calls itself a high-level description; security testing and
> current configuration were not reported.

## Generalizability and outcome limits

The authors state that clinical and operational impact of individual models
is outside the study's scope and identify the single-centre setting as a
generalizability limitation. They also describe open questions about adverse-
event handling, vendor data, effectiveness, value and which models require
governance. Oncology models are not assumed transportable from general
populations without local tuning/validation.

> **Claim record — SRC-0050-C06 | source-report**
> **Claim:** The paper directly limits its result to one centre's descriptive
> governance implementation and does not measure the clinical/operational
> effectiveness, financial value or patient outcome of the governed models or
> of the governance programme itself.
> **Claim status:** active
> **Scope:** Stated study limitations and missing outcomes; not a claim that
> the programme had no benefit or that the described tools cannot transfer.
> **As of:** Publication 2025-07-04.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Introduction, p. 1; Discussion and limitations, p. 7; Methods,
> p. 8; Data availability, p. 10.
> **Basis / limits:** Limits are direct author statements. Absence of an
> evaluated outcome cannot be converted into evidence of failure.

> **Claim record — SRC-0050-C07 | analytic-judgment**
> **Claim:** `SRC-0050` is a direct primary biological/clinical implementation
> lineage for deployment, monitoring, Model Registry, architecture and model
> sunset, but it is neither independent evaluation nor end-to-end provenance,
> cybersecurity-conformance or safeguard-effectiveness evidence.
> **Claim status:** active
> **Scope:** Evidence classification for lifecycle/system reconciliation; not
> a score change or a judgment on the institution's quality.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0050-C02`–`C06`; author affiliations and Methods,
> pp. 8–10.
> **Basis / limits:** Direct implementation is strong for represented classes.
> Author–implementer overlap, one-centre scope and missing outcome comparison
> prevent independent-effectiveness promotion.

## Safety abstraction

This page retains governance, lifecycle and high-level architecture only. It
does not expose patient data, credentials, endpoints, model parameters,
medical decision instructions or biological intervention details.

## Related pages

- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [HAZ-0005 — Drift/bias/error hazard](../hazards/haz-0005-biological-ai-drift-bias-and-error.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SRC-0049 — ETSI AI cybersecurity package](src-0049-etsi-european-ai-cybersecurity-standard-implementation.md)
- [SRC-0051 — Reproducible biomedical MLOps](src-0051-mlf-core-reproducible-biomedical-mlops-2023.md)
- [WFL-0013 — Secure biological-AI model lifecycle](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md)
- [SYS-0013 — Biological MLOps infrastructure and trust boundaries](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md)

## Sources

- Stetson et al., publisher PDF and official PMC Open Data version record,
  exact locators above.
