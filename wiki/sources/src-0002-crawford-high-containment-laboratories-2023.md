---
id: SRC-0002
type: source
title: "Cyberbiosecurity in high-containment laboratories"
aliases:
  - Crawford et al. 2023
  - Cyberbiosecurity in HCLs
status: active
created: 2026-07-11
updated: 2026-07-16
last_reviewed: 2026-07-11
review_after: 2027-01-07
source_type: peer-reviewed-study
ingest_status: complete
sensitivity: public
dual_use: moderate
raw_path: ../../raw/high-containment-cyberbiosecurity-2023.html
sha256: d990f84a4ee217f57676400dad9c0668347bab8df8adf48601cf188f23c9bc19
raw_components:
  - path: ../../raw/high-containment-cyberbiosecurity-2023-figure-1.jpg
    role: figure-1
    sha256: d28bed5ae2902de26189f9dcf9b8416fa1bcbc996b307f3bc67560907eaaf99a
  - path: ../../raw/high-containment-cyberbiosecurity-2023-figure-2.jpg
    role: figure-2
    sha256: ed069852a967f848604a12b17e2fe92a6a01c6bcf3d8cca88aceed2ea66ba7f8
  - path: ../../raw/high-containment-cyberbiosecurity-2023-figure-3.jpg
    role: figure-3
    sha256: 8a144d684d234ec66e3017347d9899266a7cc6846de27bb534388cada0638126
  - path: ../../raw/high-containment-cyberbiosecurity-2023-supplementary-table-s1-v2.docx
    role: supplementary-table-s1
    sha256: ef57ec958cb0e0d42d0c82a83426c42d60897554ed2d199c633c28bcf1123bcb
canonical_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10407794/
publisher_url: https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2023.1240281/full
accessed: 2026-07-11
doi: 10.3389/fbioe.2023.1240281
pmcid: PMC10407794
pmid: "37560539"
tags:
  - cyberbiosecurity
  - laboratories
  - high-containment
  - cyber-physical
  - risk-management
---

# Cyberbiosecurity in high-containment laboratories

## Bibliographic identity

Elizabeth Crawford, Adam Bobrow, Landy Sun, Sridevi Joshi, Viji Vijayan, Stuart
Blacksell, Gautham Venugopalan, and Nicole Tensmeyer. *Frontiers in
Bioengineering and Biotechnology*, 11:1240281, published July 25, 2023. DOI:
`10.3389/fbioe.2023.1240281`; PMCID: `PMC10407794`; PMID: `37560539`.

The publisher classifies the article as `Original Research`. In the wiki it is
a `peer-reviewed-study`: a qualitative asset-impact analysis built on
nonsystematic reviews and the authors' categorization of potential
consequences, not an empirical validation of architecture or controls in a
specific HCL.

## Provenance

- Primary immutable HTML snapshot:
  `../../raw/high-containment-cyberbiosecurity-2023.html`, 231,004 bytes,
  SHA-256
  `d990f84a4ee217f57676400dad9c0668347bab8df8adf48601cf188f23c9bc19`.
- Figures 1–3, which the original HTML loaded from the NCBI CDN, were archived
  separately under the paths and SHA-256 values in the frontmatter. Their
  dimensions match the HTML metadata, and all labels were verified visually.
- The genuine Supplementary Table S1 was archived as
  `../../raw/high-containment-cyberbiosecurity-2023-supplementary-table-s1-v2.docx`.
  The `v2` suffix denotes the second retrieval attempt, not a revision of the
  document.
- The first attempt to retrieve the supplement from PMC was retained as
  `../../raw/high-containment-cyberbiosecurity-2023-supplementary-table-s1.docx`.
  Despite its extension, it is a 1,817-byte HTML anti-bot/PoW shell with
  SHA-256
  `25fa012af11029d1dc5390cb52ed4afe6a9e9273d1453b70a0c157db698148c2`;
  it is not evidence and was not executed.
- Canonical PMC page:
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC10407794/>. Components were
  retrieved on 2026-07-11 from NCBI and the official Frontiers file host.
- External publisher page used to verify the article type and visible update
  status: <https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2023.1240281/full>;
  a `transient` presentation accessed on 2026-07-11. All substantive study
  claims rely on the local package, not this web presentation.
- The complete HTML was read through static conversion and direct inspection;
  Table 1 was checked as an HTML table; and the DOCX was inspected statically
  after its ZIP manifest was verified. No macros or executable content were
  run.

`ingest_status: complete` means that the main text, Table 1, all three figures,
and Supplementary Table S1 were read locally. It does not eliminate the
publication's own methodological gaps.

## Executive summary

The authors describe research, diagnostic, and high-containment
biomanufacturing laboratories through a shared cyber workflow and a set of
digital and cyber-physical dependencies. They apply qualitative asset-impact
analysis: identifying assets, considering losses of confidentiality, integrity,
or availability, and grouping potential consequences into five areas—worker
safety, public health, security, scientific advancement, and financial impact.

The publication is useful as the wiki's first structured model of HCLs, but it
does not establish scenario frequency, likelihood, or the effectiveness of
proposed controls. Historical examples are restated from news, vendor, and
other secondary sources; they are discovery leads, not independent grounds for
`INC` pages.

## Claims and locators

> **Claim record — SRC-0002-C01 | source-report**
> **Claim:** The authors applied qualitative asset-impact analysis to research,
> diagnostic, and high-containment biomanufacturing laboratories: they
> identified typical cyber and cyberphysical assets, considered possible losses
> of confidentiality, integrity, and availability, and assessed potential
> downstream consequences.
> **Claim status:** active
> **Scope:** A generalized model of HCLs that work with human pathogens without
> live-animal work.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, § Methods — Asset-impact analysis; Figure 1.
> **Basis / limits:** The high confidence applies to the stated method. The
> workflow review was nonsystematic and the consequence assessment qualitative;
> no independent facility validation is provided.

> **Claim record — SRC-0002-C02 | source-report**
> **Claim:** The article's general HCL cyber workflow comprises six process
> categories: project planning, pathogen research, sample storage, data
> collection, data analysis, and data storage and communications.
> **Claim status:** active
> **Scope:** The authors' generalization across three types of HCL, not the
> complete lifecycle of every laboratory.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, Figure 2 and its caption; § Cyber elements of
> high-containment laboratories.
> **Basis / limits:** The figure and text directly name the categories but do
> not establish detailed data or material flows, custody, retention or
> destruction, or formal trust boundaries. The opening prose of this section
> omits `sample storage`, but Figure 2, its caption, and a dedicated subsection
> include it.

> **Claim record — SRC-0002-C03 | source-report**
> **Claim:** The article connects the HCL workflow with planning and ordering
> software, building automation, inventory systems and LIMS, storage equipment,
> connected instruments and automation, analysis software, data platforms,
> communications, and quality-management systems; composition and connectivity
> vary with laboratory type and capability.
> **Claim status:** active
> **Scope:** Possible or typical asset classes in a qualitative literature
> synthesis, not a confirmed architecture for every HCL.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, §§ Cyber elements of high-containment
> laboratories, research laboratories, diagnostic laboratories, and
> high-containment biomanufacturing facilities; Figure 2.
> **Basis / limits:** The high confidence applies to the source's list. Much of
> the underlying evidence is vendor documentation or secondary literature;
> the presence and network exposure of particular systems were not verified.

> **Claim record — SRC-0002-C04 | source-report**
> **Claim:** The authors' asset-impact categorization identifies five areas of
> potential impact from a cyber incident in an HCL: worker safety, public health,
> security, scientific advancement, and financial impact.
> **Claim status:** active
> **Scope:** Potential consequences, not observed frequency or measured
> severity.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, § Identified Areas of Impact; Figure 3;
> Table 1.
> **Basis / limits:** The categories are directly presented by the authors. They
> should not be converted into a universal taxonomy or risk score without
> independent comparison.

> **Claim record — SRC-0002-C05 | source-report**
> **Claim:** The authors argue that cyber risk management should be integrated
> into biorisk management, controls should be linked to specific risk pathways
> and outcomes, and measures that reduce likelihood should be distinguished
> from measures that reduce impact.
> **Claim status:** active
> **Scope:** A source recommendation for HCLs; not evidence of implementation or
> effectiveness.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, § Cyber risk management in HCLs, paragraphs on
> the risk-based approach, layered controls, and risk register.
> **Basis / limits:** The article presents MFA, backup and recovery, CIS
> Controls, and cyber hygiene as illustrations. It does not report testing them
> in HCLs or establish effectiveness for specific containment edges.

> **Claim record — SRC-0002-C06 | source-report**
> **Claim:** The article distinguishes biosecurity as preventing unauthorized
> access to, loss, theft, misuse, diversion, or release of biological materials,
> and biosafety as preventing unintentional exposure or inadvertent release.
> **Claim status:** active
> **Scope:** A source-specific restatement of WHO 2020, not the authors'
> independent normative definition.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, § Introduction, second paragraph.
> **Basis / limits:** The formulation is clear but its evidence lineage derives
> from WHO. Until the relevant WHO document is ingested directly, it does not
> close the normative question in
> [QUE-0001](../questions/que-0001-domain-boundaries.md).

> **Claim record — SRC-0002-C07 | source-report**
> **Claim:** The article's search for historical incidents was a literature
> review using general keywords across news, government reports, grey
> literature, and peer-reviewed literature; the authors caution that the
> examples do not constitute a comprehensive history.
> **Claim status:** active
> **Scope:** The method used in this publication's historical-events section.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, § Methods — Identifying historical events;
> Supplementary Table S1, category `Historical Incidents`.
> **Basis / limits:** Search strings, databases, date ranges, screening process,
> and incident-level extraction are not provided. The Merck, EMA, Turla, and
> Oxford cases rely primarily on secondary reports here; the Oxford example is
> explicitly not an HCL.

> **Claim record — SRC-0002-C08 | artifact-observation**
> **Claim:** Supplementary Table S1 contains 63 bibliography rows, grouped as
> 41 `Cyber Workflow`, 12 `Historical Incidents`, and 10 `Risk Management`
> entries, but contains no separate incident findings or reproducible search
> protocol.
> **Claim status:** active
> **Scope:** The locally archived DOCX supplement.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Supplementary Table S1, complete table and caption; static DOCX
> conversion and row count on 2026-07-11.
> **Basis / limits:** This is an observation about the artifact's content, not
> an assessment of the quality of each of the 63 cited sources.

## Scope and methods

The authors combined three components: a literature review of historical
incidents, a nonsystematic review of typical HCL workflows and assets, and
qualitative asset-impact analysis. For assets, they considered possible
connectivity, organizational, scientific, or public value, and downstream
consequences of compromise. They then grouped consequences into higher-order
impact areas.

The primary scope is HCLs that work with human pathogens: research laboratories,
diagnostic laboratories, and a small subset of high-containment
biomanufacturing. Animal facilities, agricultural HCLs, and live-animal
workflows were explicitly excluded; the authors only suggest possible partial
generalizability.

## Limitations and conflicts

- This is a qualitative analysis. It has no facility sample, empirical
  measurements, validation study, quantitative likelihood, or effectiveness
  evaluation.
- The workflow review is described as nonsystematic. Search strings, databases,
  date ranges, inclusion and exclusion counts, and quality appraisal are absent
  even from Supplementary Table S1.
- Figure 2 is a high-level process map, not a network, data-lineage, custody, or
  trust-boundary architecture.
- Table 1 contains potential forms of loss. It does not establish that complete
  scenarios have occurred in HCLs or are equally plausible across all
  laboratory types.
- Historical incidents are used as analogies and discovery leads. The
  publication is not a primary victim, regulator, court, or forensic record; no
  `INC` pages were created from it, and actor or vector attribution was not
  transferred.
- The control discussion relies primarily on CIS and NIST frameworks and
  general examples. Recommendations do not mean controls were implemented,
  tested, or independently evaluated.
- The article was funded by the US Department of State and the Wellcome Trust.
  Some authors were employed by Gryphon Scientific, Veribo Analytics, and
  Praxis Biorisk Systems; the authors declared no other commercial or financial
  conflicts (§ Funding Statement; § Conflict of interest).
- Source-specific WHO-derived definitions are useful for terminology
  comparison but are not an independent normative lineage.

## Version status

The article was received on June 14, accepted on July 13, and published on
July 25, 2023 under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
The official article's license link and the unchanged status of the separately
retained NCBI-hosted figure JPEGs were reverified on 2026-07-16. This targeted
rights check did not advance the page-wide review date.

> **Claim record — SRC-0002-C09 | artifact-observation**
> **Claim:** No visible correction, retraction, or erratum notice was found in
> the local PMC snapshot or on the inspected official Frontiers page.
> **Claim status:** active
> **Scope:** Visible notices in two representations of the article; not an
> exhaustive audit of every correction and retraction registry.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-07.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** local artifact, article header and notices; official Frontiers
> article page, `Updates`, accessed 2026-07-11.
> **Basis / limits:** The absence of a visible notice does not establish that
> the status will remain unchanged; it must be rechecked by `review_after`.

## Safety handling

Operational containment parameters, specific access paths, product-specific
attack descriptions, and material relevant to proliferation have not been
consolidated. The wiki retains only defensive system classes, security
properties, consequence categories, and high-level cross-domain transfer. The
source and derived pages are labeled `dual_use: moderate` because of their HCL
context.

## Integration map

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [SRC-0022](src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md) and
  [SYN-0010](../syntheses/syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md)
  — independent human-research biobank scope plus explicit reconciliation of
  research, diagnostic, HCL, and repository environments.
- [WFL-0002](../workflows/wfl-0002-high-containment-laboratory.md) — general HCL
  workflow, laboratory variants, and candidate dependencies.
- [SYS-0001](../systems/sys-0001-hcl-containment-support-systems.md) —
  containment-support cyberphysical systems at a safe level of abstraction.
- [RSK-0001](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md) — a
  hypothetical cyber-to-biological or safety path, not an observed incident.
- [CON-0001](../concepts/con-0001-cyberbiosecurity.md) — the derived source definition
  and its operationalization through asset-impact analysis.
- [QUE-0001](../questions/que-0001-domain-boundaries.md) — the WHO-derived
  distinction, reconciled with direct WHO 2024 evidence in `SRC-0004`.
- [CTL-0001](../controls/ctl-0001-risk-based-laboratory-information-cybersecurity.md)
  — a separate lineage of WHO-recommended controls mapped to the HCL scenario
  without treating it as evidence of implementation or effectiveness, or as
  independent threat evidence.
- [CTL-0011](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md) and
  [SYN-0007](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md) — a generic
  OT technical overlay, explicitly not an HCL architecture validation.
- [WFL-0001](../workflows/wfl-0001-biomanufacturing-system.md) — a navigational
  comparison between the general biomanufacturing test bed and the
  high-containment subset.
- [SYN-0023 — Laboratory transfer/incident reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
