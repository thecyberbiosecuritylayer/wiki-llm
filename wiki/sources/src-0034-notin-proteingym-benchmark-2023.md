---
id: SRC-0034
type: source
title: ProteinGym large-scale protein fitness benchmark 2023
aliases:
  - Notin et al. ProteinGym 2023
  - ProteinGym v1.0 benchmark paper
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: peer-reviewed-empirical-benchmark
ingest_status: complete
sensitivity: public
dual_use: moderate
raw_path: ../../raw/proteingym-large-scale-benchmarks-2023.pdf
sha256: a3b08cc4a6befd64620cf0f287d78d55a36dc2639955f52c5655f83833c50104
raw_components:
  - path: ../../raw/proteingym-neurips-proceedings-record-current-2026-07-12.html
    role: official-neurips-proceedings-record
    sha256: 094371231090d98b83b318798d00a3cd7f5c61180f249aab0526844dd29c032f
canonical_url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/cac723e5ff29f65e3fcbb0739ae91bee-Abstract-Datasets_and_Benchmarks.html
direct_pdf_url: https://proceedings.neurips.cc/paper_files/paper/2023/file/cac723e5ff29f65e3fcbb0739ae91bee-Paper-Datasets_and_Benchmarks.pdf
accessed: 2026-07-12
publication_date: 2023-12-15
publisher: Neural Information Processing Systems Foundation
venue: Advances in Neural Information Processing Systems 36
track: Datasets and Benchmarks
version: ProteinGym v1.0 paper artifact
authors:
  - Pascal Notin
  - Aaron W. Kollasch
  - Daniel Ritter
  - Lood van Niekerk
  - Steffanie Paul
  - Han Spinner
  - Nathan Rollins
  - Ada Shaw
  - Rose Orenbuch
  - Ruben Weitzman
  - Jonathan Frazer
  - Mafalda Dias
  - Dinko Franceschi
  - Yarin Gal
  - Debora S. Marks
tags:
  - artificial-intelligence
  - bioinformatics
  - protein-fitness
  - empirical-benchmark
  - generalizability
  - data-leakage
  - assurance
---

# ProteinGym large-scale protein fitness benchmark 2023

## Identity and complete artifact review

Notin et al., *ProteinGym: Large-Scale Benchmarks for Protein Fitness
Prediction and Design*, 37th NeurIPS Conference, Datasets and Benchmarks
Track, 2023. The official proceedings metadata gives publication date
2023-12-15, volume 36 and pages 64331–64379.

- Main artifact: `../../raw/proteingym-large-scale-benchmarks-2023.pdf`,
  1,213,964 bytes, 49 physical/printed pages, SHA-256
  `a3b08cc4a6befd64620cf0f287d78d55a36dc2639955f52c5655f83833c50104`.
- Official proceedings record:
  `../../raw/proteingym-neurips-proceedings-record-current-2026-07-12.html`,
  10,552 bytes, SHA-256
  `094371231090d98b83b318798d00a3cd7f5c61180f249aab0526844dd29c032f`.
- Two independent retrievals of each retained object were byte-identical.
  Comparison files remained temporary and are not evidence artifacts.
- All 49 pages were text-reviewed. Figures 1–2 and A1–A3, Tables 1–4 and
  A1–A20, low-text pages 37/49 and the large clustering graphic on page 35
  were rendered or visually reviewed. Pages 12–27 are references; pages
  28–49 are the full appendix, limitations, methods and result tables.
- The PDF is version 1.5, optimized, unencrypted and untagged, with no form,
  JavaScript, embedded file or reported signature. Its catalogue contains an
  `OpenAction`; `pdfinfo` exposes a `Doc-Start` destination and extensive
  internal named destinations, but the action was not executed. This supports
  a likely navigation role, not a runtime-security conclusion. `pdfsig` also
  emitted an NSS initialization warning, so absence of a reported signature
  is not cryptographic validation.
- The official HTML contains six script elements and one search form, with no
  iframe, object or embed. It was inspected only as static text; no script or
  form was executed.

> **Claim record — SRC-0034-C01 | artifact-observation**
> **Claim:** The retained package contains the complete official 49-page
> ProteinGym paper and official NeurIPS record; repeated retrievals were
> byte-identical and all pages, figures, tables, references and appendices were
> reviewed.
> **Claim status:** active
> **Scope:** Artifact identity, completeness and static inspection; not
> independent reproduction of code, datasets, model runs or PDF runtime safety.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Local files and hashes above; PDF physical pp. 1–49; official
> proceedings HTML metadata and paper links, accessed 2026-07-12.
> **Basis / limits:** Bytes, pagination, structure and static properties are
> direct. Official hosting supports provenance but is not a digital signature.

## Version and bibliographic boundaries

The paper calls the represented suite ProteinGym v1.0 and distinguishes it
from an earlier v0.1 prototype. The PDF metadata creation/modification time is
2024-01-16, later than the proceedings publication date; it is a file-build
timestamp, not the publication date. The HTML abstract says “over 40” models,
whereas the PDF abstract and Figure 1 say “over 70” baselines. The paper's
disaggregated tables and setting-specific counts are used instead of silently
normalizing those headline phrasings. The official HTML names `Han Spinner`
where the PDF title page prints `Hansen Spinner`; it omits the PDF middle
initials in `Aaron W. Kollasch` and `Debora S. Marks` and places Rose Orenbuch
earlier in the author order than the PDF. The frontmatter author list follows
the official proceedings HTML metadata and does not overwrite the PDF form.
The main text sets the
gnomAD pseudocontrol frequency threshold above 5%, whereas Appendix A.3.2 says
above 0.5%. Table A14 ranks ProGen2 M first but its copied standard-error
caption calls TranceptEVE the best overall model. These are preserved as
identity/method/caption defects rather than silently repaired.

> **Claim record — SRC-0034-C02 | artifact-observation**
> **Claim:** The official record identifies a NeurIPS 2023 v1.0 benchmark
> paper published 2023-12-15, while the later PDF build timestamp and differing
> author spelling, `over 40` versus `over 70` headline counts, pseudocontrol
> threshold and Table A14 caption are artifact/version or internal-production
> distinctions rather than evidence of a later scientific study.
> **Claim status:** active
> **Scope:** Bibliographic and version normalization for this package.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Official HTML citation metadata/abstract; PDF title/footer and
> Abstract, p. 1; Figure 1, p. 3; clinical-data description, p. 5; Table A1,
> p. 29; Appendix §A.3.2, p. 31; Table A14, p. 43; PDF metadata.
> **Basis / limits:** The mismatch is directly observable. It does not change
> the setting-specific result tables or create a second evidence lineage.

## Dataset, model and result scope

ProteinGym combines experimental DMS and clinical-annotation benchmarks. Its
summary reports:

| Ground-truth set | Mutation class | Scope reported | Boundary |
| --- | --- | ---: | --- |
| DMS | substitutions | Table 1: 217 proteins; Table A1: 217 assays; about 2.4 million mutants | experimental readouts vary in noise, range and relationship to organismal fitness |
| DMS | indels | Table 1: 66 proteins; Table A1: 66 assays; about 0.3 million mutants | fewer model families can score variable-length inputs |
| clinical | substitutions | 2,525 proteins; about 63,000 variants | community annotations are sparse, biased and potentially circular |
| clinical | short indels | 1,555 proteins; about 3,000 variants | class imbalance required stated pseudocontrol choices |
| deduplicated total | all represented classes | 3,422 proteins; about 2.7 million mutants/variants | rows and assays are not independent incidents or deployments |

The DMS corpus spans activity, binding, expression, organismal-fitness and
stability functions and human, other-eukaryote, prokaryote and viral taxa.
Underlying studies, ClinVar/gnomAD records and model papers are cited inputs,
not separately ingested or multiplied lineages in this transaction.

> **Claim record — SRC-0034-C03 | source-report**
> **Claim:** ProteinGym directly states the dataset/model scope for a broad
> protein-fitness benchmark: experimental and clinical labels, substitution
> and indel classes, 3,422 deduplicated proteins and about 2.7 million
> observations, evaluated across multiple model families and biological
> strata.
> **Claim status:** active
> **Scope:** Benchmark sample and task scope; not a population prevalence
> estimate, independent replication of each input assay or complete biology.
> **As of:** 2023-12-15.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Abstract and Introduction, pp. 1–2; Figure 1, p. 3; §§3.1–3.3,
> pp. 4–6; Table 1, p. 6; Tables A1–A4, pp. 29–31; Tables A19–A20, pp. 46–49.
> **Basis / limits:** Counts and category definitions are direct. Several
> assays share biological/model context, and one compilation is one evaluation
> lineage.

## Evaluation workflow and controls against misleading performance

The authors distinguish zero-shot from supervised evaluation. They use
task-appropriate rank, classification, error and top-ranked-design metrics,
group results before aggregation, and stratify results by function, taxon,
alignment depth and mutation depth. For supervised DMS evaluation, Random,
Contiguous and Modulo cross-validation splits test different levels of
position generalization within the benchmark. The paper warns that a random
mutation split can put substitutions from the same residue position in train
and test; substitutions with similar biochemical properties at that position
often have similar effects, so performance at unseen positions can be
overstated.

For clinical evaluation, the authors explicitly warn that test labels can
overlap supervised training sources and that population-frequency information
can create leakage/circularity. The full-label clinical comparison is therefore
not an unbiased prospective clinical validation.

> **Claim record — SRC-0034-C04 | source-report**
> **Claim:** The study implements an explicit data→preprocessing/split→model
> scoring→metric/stratification workflow and directly tests within-benchmark
> split/stratum generalization sensitivity while documenting overfitting,
> label-leakage and aggregation risks.
> **Claim status:** active
> **Scope:** Research benchmark design and observed evaluation behavior; not a
> deployed MLOps lifecycle, production monitor, model registry or clinical
> validation.
> **As of:** 2023-12-15.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§3.3 and 4.1–4.2, pp. 5–8; Results, pp. 8–10; Appendix
> §§A.3.1–A.4.3, pp. 29–34; Tables A5–A18, pp. 38–45.
> **Basis / limits:** Methods and warnings are direct. The paper does not
> evaluate a live workflow or independently reproduce every baseline.

## Empirical findings and failure limits

The benchmark reports measured differences rather than a universal winner:

- zero-shot substitution performance varies substantially across models,
  assay functions, taxa, alignment depths and mutation depths;
- supervised random-fold scores are markedly higher than the harder
  position-separated splits for several baselines, demonstrating that split
  choice changes the apparent result;
- aggregate mean, median and design-oriented metrics can rank models
  differently, so one score does not determine task fitness;
- indel leaders/orderings differ between library-derived and model-designed or
  natural-sequence sets;
- clinical-label performance can look strong while remaining vulnerable to
  training overlap, population-frequency leakage, label imbalance and weak
  cross-gene calibration.

> **Claim record — SRC-0034-C05 | source-report**
> **Claim:** ProteinGym measures model- and setting-dependent research
> performance, including split-sensitive within-benchmark generalization and
> different leaders/orderings across task and metric strata; it does not
> support a single universally robust protein model.
> **Claim status:** active
> **Scope:** Observed benchmark consequence for the represented datasets and
> baselines; not clinical benefit/harm, biological validity outside the assays
> or prospective performance.
> **As of:** 2023-12-15.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Results §§5.1–5.2, pp. 8–9; Tables 2–4, pp. 9–10; Appendix
> §A.5, pp. 35–45, especially Tables A5–A18 and Figures A1–A3.
> **Basis / limits:** Comparative results and strata are directly reported.
> Benchmark association is not an experimental downstream outcome or proof of
> safety/effectiveness in a deployment.

The limitations appendix is unusually explicit: DMS has measurement noise,
dynamic-range ceilings/floors, replicate variability, protein-selection bias,
imperfect organismal representativeness and heterogeneous upstream processing.
ClinVar has annotation noise, studied-gene/ancestry bias and multiple
circularity routes. The benchmark covers coding-region protein changes, not
mutations or labels in regulatory regions. The authors performance-filtered a
large stability collection from 331 natural domains to 65 assays by excluding
datasets where no tested evolutionary model exceeded Spearman 0.2, which they
interpret as inadequate evolutionary-fitness signal; this selection also
limits representativeness of the retained sample.

> **Claim record — SRC-0034-C06 | source-report**
> **Claim:** The authors state material generalizability and failure limits for
> labels, assays, splits, aggregation and clinical interpretation, including
> noise, selection bias, representativeness, inconsistent processing and
> circularity.
> **Claim status:** active
> **Scope:** Limitations of ProteinGym v1.0 and its inputs; not evidence that
> every result is invalid or that later versions share the same state.
> **As of:** 2023-12-15.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §2 clinical-benchmark boundary, p. 4; §§4.1–4.2, pp. 6–8;
> Appendix §§A.1–A.3.2, pp. 28–31.
> **Basis / limits:** Limitations are direct author statements and observed
> design properties. Later website/repository changes were not imported.

## Resources, reproducibility and evidence state

The paper reports an open-source repository, common model interface,
preprocessing code, processed/raw datasets, alignments, predicted structures,
all benchmark model scores, some checkpoints/service files on ProteinGym
servers and a comparison website; most checkpoints remain in upstream model
repositories. Those resources were not
retained or executed in this transaction: no commit is pinned, dependency or
container environment is preserved, and end-to-end reproduction was not run.
The paper plans continuing benchmark updates but provides no model-retirement
process or production monitoring evidence.

> **Claim record — SRC-0034-C07 | source-report**
> **Claim:** ProteinGym reports reproducibility resources and a consistent
> research interface, but this retained package validates only the paper and
> proceedings record—not current code/data availability, dependency closure,
> runtime reproduction, registry state or maintenance/retirement practice.
> **Claim status:** active
> **Scope:** Reported resource availability and local evidence boundary.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Introduction, p. 2; Resources/Conclusion, pp. 9–10; Appendix
> §§A.3.3–A.3.4, p. 32; local raw package above.
> **Basis / limits:** Paper statements and retained-object scope are direct.
> Links/citations are acquisition leads, not silently imported artifacts.

> **Claim record — SRC-0034-C08 | analytic-judgment**
> **Claim:** This is one primary empirical benchmark lineage with direct
> model/dataset scope, comparative metrics, generalizability analyses and
> failure limits. Its author team also developed or evaluated several included
> methods, so it is not an independent evaluator of every baseline and cannot
> confirm itself. DMS inputs include biological assay outcomes, but the paper
> is not a deployment, incident, new downstream patient/organism outcome
> caused by model use, benchmark-team wet-lab validation or evaluation of the
> complete `CTL-0016` control family. It satisfies the direct-primary-record
> limb of `AIB-CI` and supplies Partial evidence for `AIB-AE`, but not SF3.
> **Claim status:** active
> **Scope:** Evidence classification for frozen `AIB-CI/AE` and adjacent
> lifecycle/system/threat cells.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** PDF title-page author list, p. 1; baseline descriptions and
> author-linked citations in §§4.1–4.2, pp. 6–8, Appendix §§A.4.1–A.4.3,
> pp. 32–34, and References, pp. 12–27; `SRC-0034-C01`–`C07`;
> [SRC-0033](src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C10`; frozen criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** A benchmark result is empirical research evidence but not
> a real-world incident or independent replication. The authors overlap with
> Tranception, TranceptEVE, ProteinNPT and the broader EVE/Marks line, so those
> comparisons cannot be treated as uniformly external evaluation. Multiple
> datasets, models, tables and cited studies do not multiply the lineage.

## Dual-use and safety boundary

The paper notes that protein-fitness/design tools can have beneficial and
harmful uses and that wet-laboratory experimentation remains necessary. This
wiki retains only aggregate benchmark structure, metrics and limitations. It
does not reproduce biological sequences, model inputs/weights, generation
methods, target-specific results or procedures for altering biological
function.

> **Claim record — SRC-0034-C09 | analytic-judgment**
> **Claim:** ProteinGym's social-impact appendix explicitly flags dual-use risk
> and the continuing wet-laboratory boundary; the benchmark does not establish
> that a digital score is a safe, effective or authorized biological action.
> **Claim status:** active
> **Scope:** High-level safety/evidence boundary only.
> **As of:** 2023-12-15.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Appendix §A.1, p. 28; relationship between fitness prediction
> and design, p. 4.
> **Basis / limits:** The warning and laboratory boundary are direct. No
> operational design or misuse detail is needed or retained.

## Related pages

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [AST-0008 — Biological AI assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [WFL-0011 — Biological AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [SYS-0011 — Biological AI ecosystem](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md)
- [RSK-0016 — Biological-AI output risk](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [CTL-0016 — Biological AI controls](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
- [SYN-0018 — Biological-AI SF2 reconciliation](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)
- [SYN-0001 — Coverage rubric](../syntheses/syn-0001-coverage-rubric.md)

## Official links

- [NeurIPS proceedings record](https://proceedings.neurips.cc/paper_files/paper/2023/hash/cac723e5ff29f65e3fcbb0739ae91bee-Abstract-Datasets_and_Benchmarks.html)
- [Official paper PDF](https://proceedings.neurips.cc/paper_files/paper/2023/file/cac723e5ff29f65e3fcbb0739ae91bee-Paper-Datasets_and_Benchmarks.pdf)
- [SYN-0022 — Foundational consequence/assurance calibration](../syntheses/syn-0022-foundational-consequence-assurance-calibration.md)
