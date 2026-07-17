---
id: SRC-0003
type: source
title: "Cyberbiosecurity in Advanced Manufacturing Models"
aliases:
  - Guttieres et al. 2019
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_type: expert-analysis
ingest_status: complete
sensitivity: public
dual_use: moderate
raw_path: ../../raw/mantle-advanced-biomanufacturing-2019.html
sha256: 77de4393d3d6f9747ae2a5167eb9addf3f7e25710ad77c9e42109f827b2fc054
raw_components:
  - path: ../../raw/guttieres-advanced-biomanufacturing-2019-figure-1.jpg
    role: figure-1
    sha256: 9e9986761419a9479fd7b52c36d6092138b3d5de8d95782825dbdba8a486b06a
  - path: ../../raw/guttieres-advanced-biomanufacturing-2019-figure-2.jpg
    role: figure-2
    sha256: bc4c32fa4ef04d8d0df4ff37d135d2deeca0586b297e5eed95081b63f63afc9d
canonical_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6737271/
publisher_url: https://www.frontiersin.org/articles/10.3389/fbioe.2019.00210
accessed: 2026-07-12
doi: 10.3389/fbioe.2019.00210
pmcid: PMC6737271
pmid: "31552236"
tags:
  - cyberbiosecurity
  - biomanufacturing
  - advanced-manufacturing
  - process-control
  - digital-thread
---

# Cyberbiosecurity in Advanced Manufacturing Models

## Bibliographic identity

Donovan Guttieres, Shannon Stewart, Jacqueline Wolfrum, and Stacy L. Springs.
*Frontiers in Bioengineering and Biotechnology*, 7:210, published 4 September
2019. DOI: `10.3389/fbioe.2019.00210`; PMCID: `PMC6737271`; PMID: `31552236`.

The publisher classifies the publication as a `Perspective article`; its
`source_type` in the wiki is `expert-analysis`. It proposes conceptual
information-flow models and defensive recommendations, but does not describe
an empirical facility study, systematic review, or control-effectiveness
evaluation.

> [!NOTE]
> **Filename mismatch**
> The immutable raw file is named `mantle-advanced-biomanufacturing-2019.html`,
> but its metadata, title, DOI, PMCID, and authors unambiguously identify it as
> **Guttieres et al. 2019**, not Mantle et al. The actual Mantle et al. article
> has a different DOI and remains a separate candidate source; the raw file was
> not renamed.

## Provenance

- Primary local HTML:
  `../../raw/mantle-advanced-biomanufacturing-2019.html`, 148 942 bytes,
  SHA-256
  `77de4393d3d6f9747ae2a5167eb9addf3f7e25710ad77c9e42109f827b2fc054`.
- Figure 1 is archived as
  `../../raw/guttieres-advanced-biomanufacturing-2019-figure-1.jpg`, 669×325,
  SHA-256
  `9e9986761419a9479fd7b52c36d6092138b3d5de8d95782825dbdba8a486b06a`.
- Figure 2 is archived as
  `../../raw/guttieres-advanced-biomanufacturing-2019-figure-2.jpg`, 669×533,
  SHA-256
  `bc4c32fa4ef04d8d0df4ff37d135d2deeca0586b297e5eed95081b63f63afc9d`.
- Canonical PMC page:
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC6737271/>.
- External publisher presentation for the article type and visible update
  status: <https://www.frontiersin.org/articles/10.3389/fbioe.2019.00210>;
  `transient`, reviewed 2026-07-12.
- The HTML contains the complete main text, captions, and 31 references. No
  supplementary materials are declared in the snapshot. Both external figure
  rasters were obtained from NCBI, checked at their original displayed
  resolution, and added as immutable raw components.

`ingest_status: complete` applies to the locally available article package. It
does not mean that all 31 cited sources were independently verified.

## Executive summary

The article presents two complementary models. Figure 1 shows the internal
information and control flow of typical monoclonal-antibody manufacturing, from
raw materials through upstream, downstream, and fill/finish operations to the
finished product, and connects process equipment to controller and control-
system layers. Figure 2 broadens the scope to a network of suppliers,
manufacturers, providers, patients, and control centers, comparing centralized
traditional, centralized ATMP, and decentralized ATMP manufacturing.

The article's main value for the wiki is its explicit separation of material,
information, and control flows and its explanation of why continuous,
distributed, and personalized models create more cross-site dependencies. The
diagrams are nevertheless conceptual and non-exhaustive; the article does not
establish current prevalence, validated trust boundaries, attack likelihood,
or the effectiveness of the proposed controls.

## Claims and locators

> **Claim record — SRC-0003-C01 | source-report**
> **Claim:** The authors set three objectives: model digital information flow
> in the biopharmaceutical value chain, consider potential cyberbiosecurity
> risks in continuous and distributed manufacturing, and propose risk-
> mitigation recommendations.
> **Claim status:** active
> **Scope:** Perspective analysis, not an empirical industry survey.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, Abstract; § Digital Information Flow in
> Biomanufacturing, first paragraph.
> **Basis / limits:** High confidence applies to the stated objectives. No
> formal methods, facility sample, validation criteria, or systematic search
> are provided.

> **Claim record — SRC-0003-C02 | source-report**
> **Claim:** Figure 1 models typical monoclonal-antibody manufacturing as the
> material sequence `raw materials → upstream cell culture → downstream
> purification → fill & finish → finished product`, connected to PLC/DCS/SCADA
> information and control layers.
> **Claim status:** active
> **Scope:** Conceptual within-facility model, not a reference architecture for
> every biologic process.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, § Digital Information Flow in
> Biomanufacturing; Figure 1 and caption.
> **Basis / limits:** Labels and directions were checked in the archived
> raster. The diagram does not show identities, protocols, network zones,
> validation gates, or a complete quality-data lineage.

> **Claim record — SRC-0003-C03 | source-report**
> **Claim:** Figure 2 compares centralized traditional biologics, centralized
> ATMP, and decentralized ATMP production and separately depicts material and
> product flows, information exchange, and control-center relationships among
> manufacturing sites, providers, and patients.
> **Claim status:** active
> **Scope:** High-level comparison of manufacturing models.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, § Considerations for Emerging Biologic
> Products, second paragraph; Figure 2 and caption.
> **Basis / limits:** The diagram explicitly distinguishes flow types. It is
> not a formal chain-of-custody, patient-identity, authorization, or cross-
> border data model.

> **Claim record — SRC-0003-C04 | source-report**
> **Claim:** The authors consider that advanced and personalized manufacturing
> increases cross-site exchange of data and materials, the coordination
> burden, and dependence on automated control, which may increase
> susceptibility to interruption or cyberattack.
> **Claim status:** active
> **Scope:** Potential risk in a 2019 Perspective, not a measured trend or
> current capability claim.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, §§ Distributed Manufacturing, Considerations
> for Emerging Biologic Products; Figure 2.
> **Basis / limits:** High confidence applies to the authors' position;
> prevalence, comparative incident rate, and the causal effect of distribution
> were not assessed.

> **Claim record — SRC-0003-C05 | source-report**
> **Claim:** The article identifies potential manufacturing consequences of a
> cyber breach: loss of process availability, equipment or product loss,
> quality deviation, requalification or revalidation burden, supply
> interruption, and possible patient harm.
> **Claim status:** active
> **Scope:** Consequence classes, not observed end-to-end scenarios or
> quantified severity.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, § Known Cybersecurity Risks Point to
> Vulnerabilities in Biomanufacturing, two paragraphs after the Merck case
> example.
> **Basis / limits:** The article combines reported incident context with
> forward-looking possibilities. Each consequence path requires separate
> validation.

> **Claim record — SRC-0003-C06 | source-report**
> **Claim:** The authors use Merck/NotPetya as a reported case of manufacturing
> and supply disruption and as motivation for biomanufacturing resilience
> analysis.
> **Claim status:** active
> **Scope:** How the Perspective presents the case, not independent incident
> verification or attribution.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** local artifact, § Known Cybersecurity Risks Point to
> Vulnerabilities in Biomanufacturing, boxed `Case Example — Merck & Co.`.
> **Basis / limits:** The case paragraph combines an SEC filing, media reports,
> and author inference, including on shortages and attribution. Before the
> primary SEC record was ingested, it was a discovery lead; no `INC` page was
> created from `SRC-0003`.

> **Claim record — SRC-0003-C07 | source-report**
> **Claim:** The authors recommend an identify/protect/detect/respond/recover
> program, mapping attack surfaces, protecting control and data interfaces,
> monitoring, response planning, and recovery preparation.
> **Claim status:** active
> **Scope:** Source recommendations based on NIST CSF 2014, not a current
> framework mapping or effectiveness evidence.
> **As of:** 2019-09-04.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, § Ensuring a Resilient Biomanufacturing
> Industry, paragraph beginning “What are some steps…”.
> **Basis / limits:** The recommendation status is explicit. The article does
> not report implementation, testing, independent evaluation, or safety
> tradeoffs; the current CSF must be ingested separately.

## Scope and methods

This is a peer-reviewed `Perspective`, not a research protocol. The authors
synthesize industrial and security literature, reported incidents, and
forward-looking manufacturing models. Figure 1 is described as `typical` and
Figure 2 as high-level; the first paragraph of the flow section explicitly
calls the scheme general and non-exhaustive.

The scope is primarily biopharmaceutical manufacturing, traditional biologics,
and ATMPs, with a strong US policy and industry context. The article is not a
general model of food production, industrial fermentation, agricultural
processing, or all healthcare delivery.

## Limitations and conflicts

- There are no formal methods, facility sample, empirical measurements,
  systematic incident search, or model validation.
- The figures are conceptual. They support flow categories and candidate
  interfaces, but not network topology, authorization, exact custody, or
  regulatory compliance.
- Forecasts concerning continuous, distributed, automated, and near-real-time
  release systems date from 2019. The wiki retains them as author projections,
  not as the current state of industry.
- Some controller-exposure statements rely on materials from 2011–2015,
  include overbroad language and reconnaissance-relevant detail, and were not
  integrated as current vulnerability claims.
- The Merck, Roche/Bayer, and healthcare examples are secondary reporting.
  `SRC-0003` does not support an independent `INC`, vector, or actor-attribution
  page.
- The control section relies on NIST CSF 2014 and general recommendations, not
  the current CSF 2.0 or measured effectiveness.
- The authors declared no commercial or financial conflicts. Reviewer KL
  reported past co-authorship with SLS (§ Conflict of Interest Statement). No
  separate funding statement appears in the snapshot.
- The definition of cyberbiosecurity expressly cites Murch et al.; it is not
  an independent definitional lineage.

## Version status

The article was received on 31 January, accepted on 19 August, and published on
4 September 2019 under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
The official article's license link and the unchanged status of the separately
retained NCBI-hosted figure JPEGs were reverified on 2026-07-16. This targeted
rights check did not advance the page-wide review date.

> **Claim record — SRC-0003-C08 | artifact-observation**
> **Claim:** No visible correction, retraction, or erratum notice was found in
> the local PMC snapshot or on the reviewed publisher page.
> **Claim status:** active
> **Scope:** Visible notices in two presentations, not an audit of all
> registries.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** local artifact, article header and notices; Frontiers article
> page, reviewed 2026-07-12.
> **Basis / limits:** The absence of a visible notice does not guarantee future
> status; the claim must be rechecked by its `review_after` date.

## Safety handling

The wiki does not reproduce product-specific operating parameters, controller-
discovery instructions, default-credential reconnaissance, internet-search
techniques, or detailed attack steps. Defensive derivatives retain system
layers, security properties, transfer mechanisms, consequences, and evidence
gaps.

## Integration map

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [WFL-0003](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
  — within-facility and cross-site material, data, and control flows.
- [SYS-0002](../systems/sys-0002-biomanufacturing-process-control.md) — defensive
  process-control stack without operational reconnaissance detail.
- [RSK-0002](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md)
  — hypothetical control/data-integrity-to-quality/supply path.
- [WFL-0001](../workflows/wfl-0001-biomanufacturing-system.md) — normal backlink and
  comparison of single-facility systems scope with the general digital thread.
- [WFL-0002](../workflows/wfl-0002-high-containment-laboratory.md) — normal backlink
  between general biomanufacturing and the high-containment subset.
- [SYN-0003](../syntheses/syn-0003-cross-domain-transfer-directions.md) — the
  paper's data/control-flow model supplies a bounded control-transfer example
  in the cross-domain taxonomy.
- [CTL-0011](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md) and
  [SYN-0007](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md) — generic
  OT mapping; [CTL-0015](../controls/ctl-0015-continuous-manufacturing-quality-control.md)
  now supplies the separate Q13 quality/release complement without claiming
  implementation.
- [AST-0007](../assets/ast-0007-biomanufacturing-assets-stakeholders.md) — a
  reconciled asset and stakeholder map using this source's IP, workforce,
  patient, and supply classes with independent Q13 quality and material
  classes.
- [SYN-0016](../syntheses/syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)
  — criterion-level asset, lifecycle, transfer, and control reconciliation.
