---
id: AST-0001
type: asset
title: Genomic data
aliases:
  - genomic information
  - genome data
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0006
  - SRC-0008
  - SRC-0014
  - SRC-0015
  - SRC-0016
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: AST-0001-C01
    evidence:
      - source: SRC-0005
        locator: "§§1–2.1, printed pp. 1–4 (PDF pp. 10–13); Figure 1"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: AST-0001-C04
    evidence:
      - source: SRC-0006
        locator: "§1.2, printed pp. 4–7 (PDF pp. 15–18); Figure 1"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: AST-0001-C05
    evidence:
      - source: SRC-0008
        locator: "pp. 30–31"
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: AST-0001-C06
    evidence:
      - source: SRC-0014
        locator: "§§2.2–2.3, 3 and 5, printed pp. 767–773 (PDF pp. 4–10)"
  - predicate: evidenced-by
    target: SRC-0015
    claim_id: AST-0001-C07
    evidence:
      - source: SRC-0015
        locator: "28 CFR §§202.205–.206 and .222–.224, final-rule PDF pp. 73, 77 / 90 FR 1708, 1712; NIST scope reconciliation in existing SRC-0005/0006 claims"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: AST-0001-C08
    evidence:
      - source: SRC-0016
        locator: "Regulation (EU) 2025/327, Articles 2 and 51, PDF pp. 31–33, 57–58"
tags:
  - genomics
  - data
  - privacy
  - bioinformatics
---

# Genomic data

> In NIST IR 8432/8467, **genomic data** encompass information about DNA
> sequences, variants, modifications, gene activity, and annotations. This is a
> biologically derived digital asset; the page contains no individual-level
> genomic records.

## Scope

The source scope includes human, microbial, plant, and animal genomic data, but
claims concerning privacy, informed consent, re-identification, and kinship
primarily concern **human genomic data**. Human privacy properties should not be
transferred automatically to non-human datasets; conversely, the risks of
non-human genomic information should not be reduced to personal privacy alone
([SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
§§1–2, printed pp. 1–8).

> **Claim record — AST-0001-C01 | source-report**
> **Claim:** NIST IR 8432 describes genomic data as information generated
> through the study of genome structure and function that may include DNA
> sequences, variants, and gene activity.
> **Claim status:** active
> **Scope:** Source definition for human and non-human genomic information.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §1, printed p. 1 (PDF p. 10); §2 and Figure 1, printed p. 3
> (PDF p. 12).
> **Basis / limits:** The definition and examples are direct. The report does
> not establish a single universal file format, sensitivity level, or legal
> classification for all genomic datasets.

> **Claim record — AST-0001-C04 | source-report**
> **Claim:** NIST IR 8467 2pd expands examples of genomic data to include
> sequences, variants, modifications, gene activity, and annotations, and its
> scope covers human, microbiome, microbial, model-organism, and plant data.
> **Claim status:** active
> **Scope:** Source examples and profile scope; human privacy outcomes apply
> when human genomic data are processed.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §1.2, printed pp. 4–7 (PDF pp. 15–18); Figure 1.
> **Basis / limits:** Data examples and scope are direct. The draft does not
> assign one sensitivity, legal classification or privacy rule to every data
> type, and it does not make non-human data a personal-privacy asset by default.

## Source-reported combined properties

Figure 2 and §2.6 identify seven characteristics whose **combination**, the
source argues, increases value and sensitivity:

- **phenotype** — possible observable traits;
- **health** — information about the presence of disease or disease risk;
- **immutable** — the practical persistence of information about the genome;
- **unique** — the potential to distinguish an individual;
- **mystique** — the source's label for public perception and uncertainty about
  future uses, not a technical property;
- **value** — scientific, clinical, commercial, or institutional value; and
- **kinship** — information about common ancestors, descendants, and relatives.

> **Claim record — AST-0001-C02 | source-report**
> **Claim:** NIST IR 8432 presents phenotype, health, immutability, uniqueness,
> mystique, value, and kinship as seven combined properties of genomic
> information.
> **Claim status:** active
> **Scope:** Source-reported stakeholder/research framing, not a universal
> scientific taxonomy.
> **As of:** 2023-12-20.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §2.6, printed pp. 6–7 (PDF pp. 15–16); Figure 2.
> **Basis / limits:** The high confidence applies to the list in the report.
> The figure caption mistakenly cites `[6]`, although the List of Figures
> correctly identifies Naveed et al. as `[7]`; §2.6 also mistakenly calls the
> May sessions the `first workshop` and cites the unrelated `[2]`. The
> underlying paper has not been ingested separately into the wiki.

## Human-genomic privacy and persistence

For human data, practical immutability extends the consequences of losing
control, while kinship means that processing or disclosure may affect relatives
who did not participate in consent. Consent and authorized-use conditions
should accompany data through aggregation, sharing, and analysis, but the
report provides no validated consent-propagation implementation
([SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
§§2.1, 2.6, 3.2, 3.7, printed pp. 3–10, 12).

> **Claim record — AST-0001-C03 | source-report**
> **Claim:** The report associates human genomic data with long-lived
> re-identification, kinship, and informed-consent concerns that may affect both
> an individual and biological relatives.
> **Claim status:** active
> **Scope:** Human genomic data in research, clinical and consumer contexts.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §2.1, printed pp. 3–4 (PDF pp. 12–13); §2.6, printed pp. 6–7
> (PDF pp. 15–16); §§3.2 and 3.7, printed pp. 9–12 (PDF pp. 18–21).
> **Basis / limits:** The report synthesizes workshop input and secondary
> literature. The cited primary re-identification studies have not been
> ingested into the wiki, and the artifact has a citation-number inconsistency
> near one claim; this page therefore does not establish a universal
> re-identification rate.

## Evidence and uncertainty

### Independent operational clinical use

NHSBT adds an independent institutional lineage for one bounded human-genomic
use: extended blood-group genotyping used to support future transfusion
matching. This is implementation evidence for generation/use of genotype
information, not for the NIST control profile or for genomic-data security.

> **Claim record — AST-0001-C05 | source-report**
> **Claim:** NHSBT reports more than 5,300 DNA-based extended blood-group
> genotype tests in 2024–25 for patients with sickle cell disorder,
> thalassaemia and other rare anaemias to support transfusion matching.
> **Claim status:** active
> **Scope:** One operational English clinical programme; not all genomics,
> data formats or a comparative outcome study.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 30–31.
> **Basis / limits:** Programme context and test count are direct. No genomic
> records, accuracy/validation results, matching outcome, cyber control or
> independent effectiveness evaluation is provided. The uncited nearby
> `17 per cent` prevalence statement is not used.

### Physical-input and sample-association states

USENIX adds an independent experimental lineage connecting physical sample/
material, derived reads, sample association and downstream software input. It
does not change the human-privacy definition of genomic data, but makes material
origin and read provenance explicit asset states.

> **Claim record — AST-0001-C06 | source-report**
> **Claim:** Ney et al. directly connect physical sequencing input to derived
> digital reads and downstream processing, and measure cross-sample reads that
> change the provenance/sample-association state of those outputs.
> **Claim status:** active
> **Scope:** One controlled proof of concept and one multiplex run; not a
> universal asset model or current error rate.
> **As of:** 2017-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §§2.2–2.3, 3 and 5, printed pp. 767–773 (PDF pp. 4–10).
> **Basis / limits:** Material, reads, processing and association errors are
> direct. No personal record, re-identification, downstream decision harm or
> current platform prevalence is established.

### Human-omics regulatory scope reconciliation

Part 202 adds a U.S. legal taxonomy for human genomic, systems-level
epigenomic, proteomic and transcriptomic data, together with bounded clinical
and pathogen exclusions. That taxonomy applies only within the regulation.
The NIST genomic profile separately includes human, microbial, plant and animal
genomic data and distinguishes privacy risk from cybersecurity risk. Together
they provide a reconciled scope: `genomic` is not synonymous with `human`,
`human omic` is not a universal scientific category, and privacy properties do
not transfer automatically to non-human data.

> **Claim record — AST-0001-C07 | analytic-judgment**
> **Claim:** Independent NIST and DOJ lineages jointly support a bounded scope
> that distinguishes human and non-human genomics, at least three other human-
> omic classes, regulation-specific exclusions, and privacy versus
> cybersecurity properties without universalizing either taxonomy.
> **Claim status:** active
> **Scope:** Canonical wiki scope reconciliation; not a scientific ontology or
> a legal coverage decision for a dataset.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§1.1–1.2 and 2.1, printed pp. 1–4 (PDF pp. 10–13);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§1.1–1.3 and 2.2, printed pp. 3–5, 9–11 (PDF pp. 14–16, 20–22);
> [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.205–.206 and .222–.224, PDF pp. 73, 77 / 90 FR 1708, 1712.
> **Basis / limits:** NIST supplies human/non-human and cyber/privacy scope;
> DOJ supplies independent other-omics definitions and exclusions. The
> reconciliation is editorial and preserves each instrument's purpose.

### EU electronic-health and secondary-use asset envelope

EHDS places genetic/genomic and multiple other human-omics beside EHR,
pathogen, clinical-study, cohort and biobank data in a minimum secondary-use
envelope. These are related legal asset classes, not all synonyms for genomic
data. Primary/secondary use, personal/non-personal status, permit purpose,
provenance and national safeguards remain material context.

> **Claim record — AST-0001-C08 | source-report**
> **Claim:** EHDS places human genetic/genomic data within a broader electronic-
> health-data asset envelope that includes multiple other omics, pathogen,
> clinical-study, cohort and biobank categories and permits additional national
> safeguards for specified sensitive classes.
> **Claim status:** active
> **Scope:** EU secondary-use legal categories, not a universal genomic asset
> ontology, dataset availability or access authorization.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> Articles 2 and 51, PDF pp. 31–33, 57–58.
> **Basis / limits:** Categories and safeguard option are direct. `AST-0001`
> remains the genomic-data page; other EHDS classes are adjacent assets and
> their 2031 application is separately recorded.

NIST IR 8432 and IR 8467 2pd belong to the same NIST/NCCoE program lineage;
the latter publication adds later stakeholder sessions and draft framework
mapping but is not an independent population study or systematic review. The
seven properties and privacy concerns are useful as an asset model but do not
establish uniform sensitivity, harm, or regulatory classification for every
dataset. Classification should account for species, identifiability, data
granularity, linkage context, consent, use, and applicable law; the current
corpus does not yet validate a complete classification scheme.

## Related pages

- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)

- [WFL-0005 — Genomic data lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003 — Genomic sequencing and analysis ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [RSK-0003 — Genomic-data integrity and decision harm](../risk-scenarios/rsk-0003-genomic-data-integrity-decision-harm.md)
- [RSK-0004 — Genomic-data disclosure and kin privacy harm](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md)
- [RSK-0020 — Observed genetic-account and kin privacy harm](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md)
- [INC-0007 — 23andMe genetic-data breach](../incidents/inc-0007-23andme-genetic-data-breach-2023.md)
- [RSK-0005 — Technically authorized processing and genomic privacy harm](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md)
- [HAZ-0001 — Cross-sample read misassignment](../hazards/haz-0001-multiplex-sequencing-cross-sample-misassignment.md)
- [RSK-0009 — Sequenced input to digital execution](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md)
- [RSK-0010 — Cross-sample digital exposure](../risk-scenarios/rsk-0010-multiplex-cross-sample-digital-exposure.md)
- [RSK-0011 — Part 202 regulated access branches](../risk-scenarios/rsk-0011-covered-omics-regulated-access.md)
- [CTL-0002 — Genomic-data risk management](../controls/ctl-0002-genomic-data-risk-management.md)
- [SRC-0005 — NIST IR 8432](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0006 — NIST IR 8467 2pd](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0008 — NHSBT Annual Report 2024–25](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0014 — Ney et al. 2017](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [GOV-0005 — US Data Security Program](../governance/gov-0005-us-data-security-program-2025.md)
- [CTL-0008 — Part 202 transaction controls](../controls/ctl-0008-restricted-data-transaction-controls.md)
- [CTL-0009 — EHDS safeguards](../controls/ctl-0009-ehds-health-data-and-ehr-safeguards.md)
- [GOV-0006 — EU EHDS governance](../governance/gov-0006-eu-ehds-regulation-2025.md)
- [SYN-0004 — US–EU governance reconciliation](../syntheses/syn-0004-us-eu-human-omics-health-data-governance.md)
- [SRC-0015 — DOJ final rule and correction chain](../sources/src-0015-us-doj-data-security-program-2025.md)
- [SRC-0016 — EU EHDS Regulation](../sources/src-0016-eu-ehds-regulation-2025.md)

## Sources

- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
  §§1–3.7, printed pp. 1–12; Figures 1–2.
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
  §1.2, printed pp. 4–7; Figure 1.
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 30–31.
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md), §§2–3 and 5.
- [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
  §§202.205–.206 and .222–.224.
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md), Articles 2 and 51.
