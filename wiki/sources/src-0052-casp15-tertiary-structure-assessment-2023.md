---
id: SRC-0052
type: source
title: CASP15 tertiary-structure assessment 2023
aliases:
  - Simpkin et al. CASP15 tertiary assessment
  - CASP15 single-chain protein structure benchmark
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: peer-reviewed-empirical-benchmark-assessment
ingest_status: partial
sensitivity: public
dual_use: moderate
raw_path: ../../raw/casp15-tertiary-structure-assessment-2023.pdf
raw_bytes: 9588462
sha256: 0f681e4b4f6a2f3383ec2d5c359cb4a6e3648412b9f8918405aa305216b80a22
raw_components:
  - path: ../../raw/casp15-in-numbers-current-2026-07-12.html
    role: official-casp15-scope-counts
    bytes: 32132
    sha256: a66c6c3d3e55319b2220019c4e34d48d200913ec391f5fe4ff327c5d23f75ba0
  - path: ../../raw/casp-independent-assessors-current-2026-07-12.html
    role: official-independent-assessor-policy-and-casp15-role
    bytes: 40509
    sha256: dbc0b200704d52c450289145d8fd693d2c037b88ed72130f335a3afae939ea8a
  - path: ../../raw/casp15-regular-results-tables-2023.tar.gz
    role: official-regular-tertiary-result-tables
    bytes: 4280186
    sha256: a117e2c85f55683bca24184d70d76feedd66a314ba9d1f92f471acf61e1134e6
canonical_url: https://doi.org/10.1002/prot.26593
direct_pdf_url: https://rcastoragev2.blob.core.windows.net/30220f3ebc0b7774942bbacc030f2b72/PROT-91-1616.pdf
publisher_record_url: https://onlinelibrary.wiley.com/doi/10.1002/prot.26593
official_results_url: https://predictioncenter.org/download_area/CASP15/results/tables/regular.tar.gz
accessed: 2026-07-12
publication_date: 2023-09-25
issue_date: 2023-12
publisher: Wiley Periodicals LLC
venue: Proteins Structure Function and Bioinformatics
volume: 91
issue: 12
pages: 1616-1635
doi: 10.1002/prot.26593
version: final-version-of-record
authors:
  - Adam J. Simpkin
  - Shahram Mesdaghi
  - Filomeno Sánchez Rodríguez
  - Luc Elliott
  - David L. Murphy
  - Andriy Kryshtafovych
  - Ronan M. Keegan
  - Daniel J. Rigden
tags:
  - artificial-intelligence
  - bioinformatics
  - protein-structure-prediction
  - benchmark
  - casp15
  - generalizability
  - molecular-replacement
  - assurance
---

# CASP15 tertiary-structure assessment 2023

## Identity, acquisition and review boundary

Simpkin et al., *Tertiary structure assessment at CASP15*, *Proteins:
Structure, Function, and Bioinformatics* 91(12), 1616–1635. The final article
was first published on 2023-09-25 under DOI `10.1002/prot.26593`.

- Main artifact: `../../raw/casp15-tertiary-structure-assessment-2023.pdf`,
  9,588,462 bytes, 20 physical pages/journal pp. 1616–1635, SHA-256
  `0f681e4b4f6a2f3383ec2d5c359cb4a6e3648412b9f8918405aa305216b80a22`.
- Official CASP15 counts page:
  `../../raw/casp15-in-numbers-current-2026-07-12.html`, 32,132 bytes,
  SHA-256
  `a66c6c3d3e55319b2220019c4e34d48d200913ec391f5fe4ff327c5d23f75ba0`.
- Official assessor page:
  `../../raw/casp-independent-assessors-current-2026-07-12.html`, 40,509
  bytes, SHA-256
  `dbc0b200704d52c450289145d8fd693d2c037b88ed72130f335a3afae939ea8a`.
- Official regular tertiary-result tables:
  `../../raw/casp15-regular-results-tables-2023.tar.gz`, 4,280,186 bytes,
  SHA-256
  `a117e2c85f55683bca24184d70d76feedd66a314ba9d1f92f471acf61e1134e6`.
- The four retained objects total 13,941,289 bytes. A second retrieval of
  each object was byte-identical; comparison copies remained temporary.
- All 20 article pages were text-reviewed. Figures 1–12 and Table 1 were
  rendered or visually checked, including the molecular-replacement examples
  on physical pp. 15–17/journal pp. 1630–1632.
- The PDF is version 1.7, optimized, unencrypted and untagged. No form,
  JavaScript or embedded file was detected. The signature tool reported no
  signature but also failed to initialize its NSS trust database, so this is
  not cryptographic authentication.
- The two HTML wrappers were inspected only as static text. Each contains ten
  script elements; no form, iframe, object or embed was detected, and no
  script was executed.
- The results archive passed gzip and tar integrity checks. It contains 132
  non-empty regular ASCII `.txt` tables, no links or traversal paths, 25,574,143
  uncompressed file bytes and 60,549 lines. The files include whole-target and
  domain variants, so 132 files must not be read as 132 independent targets or
  evaluation units.
- The article declares a 2.8 MB supporting-information DOCX (`DATA S1`) with
  Table S1 and Figures S1–S5. It was not retained or read, and no claim below
  depends on it. `ingest_status` is therefore `partial`, although the main
  20-page version of record and all four declared local artifacts are complete.

> **Claim record — SRC-0052-C01 | artifact-observation**
> **Claim:** The retained 13,941,289-byte package contains the complete
> 20-page version-of-record article and three minimal official CASP companion
> artifacts; repeat retrievals were byte-identical, all article pages and
> displayed results were reviewed, and the article-declared but locally
> unretained supporting DOCX is explicitly excluded.
> **Claim status:** active
> **Scope:** Artifact identity, integrity, review coverage and local package
> boundary; not cryptographic authentication, dynamic-page safety, independent
> scientific reproduction or review of `DATA S1`.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Frontmatter paths, byte counts and SHA-256 values; complete
> PDF review; static HTML review; archive inventory and repeat-retrieval hashes.
> **Basis / limits:** Byte identity and artifact structure are direct. All
> companions are from the same CASP publication programme and do not create
> independent scientific lineages.

## Benchmark design and represented scope

CASP15 participants predicted single-chain structures before corresponding
experimental X-ray, cryo-EM or NMR structures became public. The assessment
then compared submitted models with those targets under standardized metrics.
The article analyzes 132 submitting groups and 112 evaluation units from 77
targets; 118 groups with submissions for at least ten evaluation units enter
the broad comparison. Three low-resolution cryo-EM evaluation units were
excluded, leaving 109 in the main ranking: 47 TBM-easy, 15 TBM-hard, 8 TBM/FM
and 39 FM.

The official live counts page uses a different administrative denominator:
135 groups and 47 servers contributed tertiary predictions, with 9,143
model-1 and 42,737 total tertiary models. Across all CASP15 categories it
lists 165 registered groups, 81 tertiary targets and 53,764 total models.
These numbers describe registration/submission administration, whereas the
paper applies assessment-specific inclusion, target and evaluation-unit rules;
they are preserved rather than silently forced into one count.

> **Claim record — SRC-0052-C02 | source-report**
> **Claim:** CASP15 is a prospective, withheld-target protein-structure
> prediction benchmark in which participating groups submitted models before
> experimental structures became public and assessors compared them using a
> declared 109-evaluation-unit main-analysis set spanning four difficulty
> classes.
> **Claim status:** active
> **Scope:** Single-chain tertiary-structure prediction and the article's
> included CASP15 evaluation units; not complexes, RNA, ligands, future CASP
> rounds, production deployment or all possible proteins.
> **As of:** CASP15 assessment reported 2023-09-25.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Article Introduction and Methods, journal pp. 1616–1619;
> Figure 1, p. 1620; Figure 2, p. 1621.
> **Basis / limits:** Timing, inclusion rules and strata are direct source
> statements. A challenge benchmark tests represented targets, not universal
> biological or operational performance.

> **Claim record — SRC-0052-C03 | artifact-observation**
> **Claim:** The paper's 132-group/112-evaluation-unit analysis counts and the
> official page's 135-tertiary-contributor/81-tertiary-target administrative
> counts use different declared scopes and must not be treated as a defect or
> merged denominator without the underlying CASP inclusion rules.
> **Claim status:** active
> **Scope:** Count reconciliation between the retained paper and official
> CASP15 counts page; not reconstruction of every registration, withdrawal,
> target split or assessment decision.
> **As of:** Paper published 2023-09-25; official page retained 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Article Methods, journal pp. 1617–1618; official CASP15 counts
> HTML, tertiary-structure and all-category rows.
> **Basis / limits:** Both values are directly visible inside one CASP
> programme. The reason for nonidentity is supported by their different labels
> and article inclusion rules, not a row-level administrative reconstruction.

## Metrics and comparative findings

The assessment combines global fold, main-chain, side-chain and confidence
measures through declared z-score procedures and retains metric-specific
views. The official result archive exposes per-target/domain tables with fields
including `GDT_TS`, `GDT_HA`, `LDDT`, `CAD_AA`, `TMscore` and `reLLG`; it was
inventoried but not used for a row-by-row independent recomputation.

Table 1 reports, among the leading or reference methods:

| Group/method | Models with GDT_TS >= 45 | Models with GDT_TS >= 90 | Median GDT_TS |
| --- | ---: | ---: | ---: |
| PEZYFoldings | 101/107 (94.4%) | 53/107 (49.5%) | 89.65 |
| UM-TBM | 105/109 (96.3%) | 46/109 (42.2%) | 87.36 |
| Yang | 105/108 (97.2%) | 51/108 (47.2%) | 89.26 |
| ColabFold | 93/109 (85.3%) | 42/109 (38.5%) | 86.67 |
| NBIS-AF2-standard | 93/109 (85.3%) | 38/109 (34.9%) | 85.88 |
| ESM-single-sequence | 72/93 (77.4%) | 19/93 (20.4%) | 77.71 |

The authors use GDT_TS 45 as a correct-topology threshold and 90 as an
approximate crystal-form/expected-accuracy ceiling. These thresholds do not
turn a structure score into proof of biological function, clinical validity
or deployment safety.

> **Claim record — SRC-0052-C04 | source-report**
> **Claim:** CASP15 reports high but nonuniform tertiary-structure accuracy:
> multiple AF2-related leading groups produced correct-topology models for
> most represented units, while the fraction reaching the stricter GDT_TS 90
> threshold and the ordering varied by group and metric.
> **Claim status:** active
> **Scope:** Table 1 groups, submitted model-1 predictions and represented
> CASP15 targets; not all model variants, later systems, biological function,
> clinical performance or a universal best method.
> **As of:** CASP15 assessment reported 2023-09-25.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Article Table 1 and surrounding interpretation, journal
> pp. 1621–1623; Figures 1–3, pp. 1620–1623.
> **Basis / limits:** Values and threshold meanings are direct. Aggregate
> challenge scores remain sample-, metric- and submission-dependent.

## Generalizability and failure limits

The article isolates a hard 18-unit cluster, 17 of them FM. Seven of those 18
were viral, versus six of the other 91 units; the reported Fisher test is
`p = .001`. The hardest cases generally had shallow multiple-sequence
alignments or few detectable homologues, and the performance deficit of the
single-sequence protein-language-model entry increased as alignments became
shallower. The proposed small-size/alpha-helical association is described as
tentative, not a settled causal mechanism.

Local disagreement can also reflect conformational flexibility, crystal
contacts or chain interfaces rather than simple prediction error. Conversely,
good global backbone agreement was not sufficient for accurate side-chain or
functional-site geometry. For T1146, for example, the paper contrasts a QUIC
model with GDT_HA 79.4 but 2.36 Å catalytic-residue RMSD against an Agemo model
with global GDT_HA 51.3 but 0.34 Å catalytic-residue RMSD.

> **Claim record — SRC-0052-C05 | source-report**
> **Claim:** CASP15 directly measures failure concentration by target
> difficulty and biological/data strata: hard targets were associated with
> shallow alignments or few homologues and were disproportionately viral in
> this sample, while the article treats the size/secondary-structure pattern
> as tentative.
> **Claim status:** active
> **Scope:** Observed CASP15 associations for the 109-unit main analysis; not
> causal attribution, viral prevalence, adversarial robustness or performance
> for every sequence/taxon.
> **As of:** CASP15 assessment reported 2023-09-25.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Article Results and Figures 2–5, journal pp. 1621–1624.
> **Basis / limits:** Difficulty, alignment and taxon strata are direct; the
> sample is small and selected, and association does not establish cause.

> **Claim record — SRC-0052-C06 | source-report**
> **Claim:** Global fold accuracy is not sufficient evidence of local
> side-chain, active-site or functional accuracy, and some model–target local
> differences may instead reflect flexibility or experimental packing and
> interface context.
> **Claim status:** active
> **Scope:** Structural interpretation in the represented CASP15 targets;
> not wet-lab validation of biological function, proof that deviations are
> harmless, or a rule that global metrics are uninformative.
> **As of:** CASP15 assessment reported 2023-09-25.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Article Results and Figures 6–8, journal pp. 1624–1628;
> functional-site analysis and Figure 12, pp. 1630–1632.
> **Basis / limits:** Metric discordance and structural contexts are directly
> reported. Functional consequences were inferred structurally, not measured
> as organism, patient or experimental biological outcomes.

## Bounded downstream research consequence

For 17 targets with diffraction data, the assessors directly tested submitted
model-1 predictions in molecular replacement. The workflow trimmed models by
reported confidence, used Phaser and treated `LLG >= 60` as a success
indicator. No group solved T1122 or T1125 using an unsplit model, whereas many
groups produced usable models for other targets. For T1145, splitting a model
into four domains allowed Phaser to position seven of eight domain copies;
Modelcraft built most of two copies and Refmac5 reached R/Rfree 0.26/0.30,
though the paper states that manual completion would usually still be needed.

> **Claim record — SRC-0052-C07 | source-report**
> **Claim:** CASP15 includes a direct downstream research-workflow test: some
> submitted predictions enabled experimental crystallographic molecular
> replacement under the declared 17-target protocol, while other targets
> failed and the T1145 example required domain splitting and still normally
> required manual completion.
> **Claim status:** active
> **Scope:** Research use in the paper's diffraction/molecular-replacement
> workflow; not autonomous structure determination, prospective deployment,
> clinical benefit, patient/organism outcome or validation of biological
> function.
> **As of:** CASP15 assessment reported 2023-09-25.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Article Methods, journal pp. 1618–1619; molecular-replacement
> Results and Figures 9–11, pp. 1627–1631.
> **Basis / limits:** The authors executed an experimental-structure-solving
> computational workflow against available diffraction data. It is a bounded
> research consequence, not an incident, deployment or biological outcome.

## Independence and evidence classification

The official assessor policy says independent assessors may not participate as
predictors or be directly involved in CASP organization, and its CASP15 row
names Daniel J. Rigden for the single-protein/domain category. The article is
therefore an assessor-led external evaluation of participant submissions.
However, coauthor Andriy Kryshtafovych is affiliated with the CASP Center, the
authors built parts of the analysis/molecular-replacement workflow, and the
paper includes assessor-run reference baselines. It is independent of the
participant teams in the policy's bounded sense, not institutionally
independent of the CASP programme.

The CASP15 author list has no overlap with the ProteinGym author list in
[SRC-0034](src-0034-notin-proteingym-benchmark-2023.md). The studies use
different institutions, governance, model tasks, target corpora and metrics.
CASP15 is therefore a materially independent benchmark lineage for a distinct
protein-AI task; it is not a replication of ProteinGym's fitness-prediction
scores or labels.

> **Claim record — SRC-0052-C08 | analytic-judgment**
> **Claim:** CASP15 supplies a materially independent protein-AI benchmark
> lineage relative to `SRC-0034`, with assessor separation from participant
> predictor teams, but it is neither a replication of ProteinGym nor evidence
> institutionally independent of the CASP programme itself.
> **Claim status:** active
> **Scope:** Claim-specific lineage independence for combining CASP15 and
> ProteinGym evidence; not universal assessor neutrality or independence from
> every method, institution or CASP administrative role.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** CASP15 paper author/affiliation and method statements, journal
> pp. 1616–1619; official independent-assessor policy and CASP15 role listing;
> `SRC-0052-C02`–`C07`; `SRC-0034-C03`–`C08` and its author list.
> **Basis / limits:** Author, institution, task, data and metric separation are
> directly comparable. Organizational participation is preserved, and
> different tasks prevent a replication claim.

> **Claim record — SRC-0052-C09 | analytic-judgment**
> **Claim:** This source provides an independent empirical-benchmark limb
> consumed by [SYN-0029](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
> for frozen `AIB-AE` because it measures effectiveness and failure limits
> across withheld targets, difficulty classes, taxa and model families. Its
> molecular-replacement test provides a narrowly bounded direct
> research-consequence limb consumed by `SYN-0029` for `AIB-CI`; neither
> contribution establishes
> adversarial/cyber robustness, deployment effectiveness, an incident,
> privacy consequence, clinical outcome or patient/organism impact.
> **Claim status:** active
> **Scope:** Evidence contribution to frozen `AIB-AE` and `AIB-CI`; this
> source page does not itself decide a score or evaluate the complete control
> family, while canonical reconciliation lives in `SYN-0029` and `SYN-0001`.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** `SRC-0052-C02`–`C08`; independent ProteinGym lineage and
> boundary in `SRC-0034-C08`; frozen criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Withheld-target comparison, strata, failures and the
> executed molecular-replacement workflow are direct. Mapping them to the
> rubric is analytic and deliberately restricted to research consequences;
> the source page supplies evidence while the synthesis and rubric own the
> verdict.

## Resources, reproducibility and completeness limits

The paper points to `https://github.com/hlasimpk/CASP15_high_accuracy` for
analysis code and says supporting data are available from the corresponding
author on reasonable request. That repository, its dependencies and external
tools were not retained or executed. The official result-table archive is
retained and structurally inventoried, but no assessor credentials, submitted
models, target structures, full author analysis environment or supplement are
pinned locally. The package supports audit of the publication and official
tables, not end-to-end reproduction.

No conflict-of-interest declaration was located in the retained PDF. The
article does identify funding and author contributions. Absence of a located
declaration is not evidence that no conflict existed.

> **Claim record — SRC-0052-C10 | source-report**
> **Claim:** The article reports analysis code and request-based supporting
> data, while the official companion supplies result tables; the retained
> package does not close the dependencies, credentials, submitted models,
> target structures, supplement or runtime environment needed for end-to-end
> reproduction.
> **Claim status:** active
> **Scope:** Reported resource availability and the local reproducibility
> boundary; not a claim that unretained resources are unavailable or invalid.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Article Data Availability Statement, journal p. 1633; article
> code-reference text; retained official results archive and local package
> inventory.
> **Basis / limits:** The source reports resources and the local exclusions are
> direct. Availability was not converted into a successful reproduction claim.

## Dual-use and safety boundary

This page retains aggregate benchmark design, metrics, limitations and a
high-level crystallographic workflow result. It does not reproduce sequences,
atomic coordinates, participant models, target-specific score-table rows,
model weights, executable code, assay recipes or procedures for changing
biological function.

> **Claim record — SRC-0052-C11 | analytic-judgment**
> **Claim:** The local representation stays at defensive evaluation and
> evidence-assurance abstraction and does not provide sequences, structures,
> model artifacts, executable workflows or operational instructions for
> altering biological function.
> **Claim status:** active
> **Scope:** This wiki page and its summarized content; not a safety assessment
> of all public CASP materials or protein-structure-prediction technology.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local content and explicit limits in `SRC-0052-C02`–`C10`.
> **Basis / limits:** Only aggregate research-evaluation findings are exposed
> here. The raw archive is preserved for evidence integrity, not operationally
> unpacked into the wiki.

## Integration map

This source is integrated through
[SYN-0029](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md),
where its benchmark role is reconciled with the other lineages. The canonical
rubric verdict remains in `SYN-0029` and
[SYN-0001](../syntheses/syn-0001-coverage-rubric.md). Reciprocal context includes:

- [HAZ-0005](../hazards/haz-0005-biological-ai-drift-bias-and-error.md)
- [SYN-0029](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SRC-0034](src-0034-notin-proteingym-benchmark-2023.md)
- [SYN-0018](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)
- [SYN-0001](../syntheses/syn-0001-coverage-rubric.md)

## Official links

- <https://doi.org/10.1002/prot.26593>
- <https://onlinelibrary.wiley.com/doi/10.1002/prot.26593>
- <https://predictioncenter.org/casp15/numbers.cgi>
- <https://predictioncenter.org/index.cgi?page=assessors_list>
- <https://predictioncenter.org/download_area/CASP15/results/tables/regular.tar.gz>
