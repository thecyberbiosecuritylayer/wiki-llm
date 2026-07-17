---
id: WFL-0002
type: workflow
title: Cyberphysical workflow of a high-containment laboratory
aliases:
  - HCL cyber workflow
  - high-containment laboratory workflow
status: active
created: 2026-07-11
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0002
  - SRC-0003
  - SRC-0004
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0002
    claim_id: WFL-0002-C01
    evidence:
      - source: SRC-0002
        locator: "§ Cyber elements of high-containment laboratories; Figure 2 and caption; §§ Project planning–Data storage and communications"
  - predicate: depends-on
    target: SYS-0001
    claim_id: WFL-0002-C02
    evidence:
      - source: SRC-0002
        locator: "§§ Pathogen research, Sample storage, Data collection; Figure 2"
  - predicate: evidenced-by
    target: SRC-0003
    claim_id: WFL-0002-C05
    evidence:
      - source: SRC-0002
        locator: "§ Cyber elements of high-containment biomanufacturing facilities"
      - source: SRC-0003
        locator: "§§ Digital Information Flow in Biomanufacturing, Considerations for Emerging Biologic Products; Figures 1–2"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: WFL-0002-C06
    evidence:
      - source: SRC-0002
        locator: "Figure 2; §§ Cyber elements of high-containment laboratories, Sample storage"
      - source: SRC-0004
        locator: "§§1.1–1.2, printed pp. 2–3 (PDF pp. 22–23); §§6.3–7, printed pp. 31–44 (PDF pp. 51–64)"
tags:
  - laboratories
  - high-containment
  - workflow
  - cyber-physical
---

# Cyberphysical workflow of a high-containment laboratory

> Crawford et al. model HCLs through six process categories—planning, pathogen
> research, sample storage, data collection, data analysis, and data storage
> and communications—and connect them to digital and cyberphysical
> dependencies. This is a high-level exposure map, not a complete lifecycle or
> network architecture.

## Scope and unit of analysis

This page covers the authors' generalized model of research, diagnostic, and
high-containment biomanufacturing laboratories that work with human pathogens
without live-animal work. It does not extend the findings to ABSL, BSL-Ag,
agricultural pathogens, or animal workflows without additional evidence
([SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
§ Cyber considerations in HCLs, first two paragraphs).

`High-containment laboratory` is the source scope here, not a claim that all
BSL-3, BSL-4, or other institutional classes share the same architecture or
level of cyber exposure.

## Workflow map

Figure 2 and its caption identify six categories:

1. **Project planning** — experimental design, budgeting, ordering, and
   acquisition planning.
2. **Pathogen research** — handling and research work and dependent
   containment-support functions.
3. **Sample storage** — inventory, identification, environmental monitoring,
   and controlled access to stored material.
4. **Data collection** — connected instruments and partly or fully automated
   laboratory operations.
5. **Data analysis** — instrument-linked, local, or third-party analysis
   software.
6. **Data storage and communications** — local or cloud storage, sharing,
   collaboration, and reporting.

The opening prose in § Cyber elements of high-containment laboratories lists
only five categories and omits `sample storage`, while Figure 2, its caption,
and the separate `Sample storage` subsection give six. The wiki retains the
visible six-component model while recording this editorial inconsistency
([SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
Figure 2; §§ Cyber elements of high-containment laboratories, Sample storage).

> **Claim record — WFL-0002-C01 | source-report**
> **Claim:** Figure 2, its caption, and the article's subsections support a six-
> component HCL cyber workflow: project planning, pathogen research, sample
> storage, data collection, data analysis, and data storage and communications.
> **Claim status:** active
> **Scope:** High-level author model for HCLs conducting human-pathogen work.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> Figure 2 and caption; §§ Project planning–Data storage and communications.
> **Basis / limits:** The opening sentence of the section omits sample storage,
> but the visible figure, its caption, and a separate subsection include it.
> The model does not contain a complete accession-to-destruction lifecycle.

## Laboratory variants

### Research HCL

The source analysis emphasizes unique datasets, research findings, protocols,
legacy samples, and biorepositories; such laboratories may depend on
institution-wide cyber infrastructure. This is a possible or typical profile,
not a facility census or evidence of prevalence
([SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
§ Cyber elements of research laboratories).

### Diagnostic HCL

The diagnostic variant is described as receipt of samples and accompanying
data → storage and handling → data collection and analysis → reporting. It
depends on coordination with hospitals, clinics, other laboratories, and
public-health entities. The source does not formalize chain of custody,
identity resolution, interoperability, or reporting trust boundaries
([SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
§ Cyber elements of diagnostic laboratories, first two paragraphs).

### High-containment biomanufacturing

This variant adds production and quality-management functions to the shared
inventory, storage, facility, instrument, and data dependencies. Direct ingest
of Guttieres et al. supports the general biomanufacturing process-control and
cross-site flow model, but not its HCL-specific applicability; Crawford et al.
explicitly cite Guttieres, so these statements form a single evidence lineage
([SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
§ Cyber elements of high-containment biomanufacturing facilities;
[SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md), Figures 1–2;
§§ Digital Information Flow in Biomanufacturing, Considerations for Emerging
Biologic Products).

> **Claim record — WFL-0002-C05 | analytic-judgment**
> **Claim:** `SRC-0003` directly supports the general process-control and
> material/information-flow model cited by Crawford et al., but does not
> independently validate that model in high-containment manufacturing.
> **Claim status:** active
> **Scope:** Reconciliation of general biopharmaceutical and HCL-specific
> conceptual models.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> § Cyber elements of high-containment biomanufacturing facilities;
> [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md), Figures 1–2;
> §§ Digital Information Flow in Biomanufacturing, Considerations for Emerging
> Biologic Products.
> **Basis / limits:** Crawford explicitly cites Guttieres for general
> biomanufacturing. Direct ingest improves provenance but not evidence
> independence or HCL-specific validation.

> **Claim record — WFL-0002-C02 | source-report**
> **Claim:** In the source model, the HCL workflow depends on a combination of
> information systems, inventory and storage systems, connected laboratory
> instruments, and containment-support cyberphysical systems; the particular
> set and its connectivity depend on laboratory type and capability.
> **Claim status:** active
> **Scope:** General asset classes, not the architecture of a specific facility.
> **As of:** 2023-07-25.
> **Review after:** 2027-01-11.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> Figure 2; §§ Pathogen research, Sample storage, Data collection, Data analysis,
> Data storage and communications.
> **Basis / limits:** The source synthesizes literature and vendor examples; it
> does not measure prevalence, external exposure, segmentation, or implemented
> controls.

## Data, material, and control dependencies

At a defensive level, the source model supports only the following **candidate
dependencies**:

- **material/custody:** ordering or receipt → storage and inventory → laboratory
  handling; formal custody states are not defined;
- **data:** planning and metadata → collection → analysis → storage, sharing,
  and reporting; provenance and identity controls are not described;
- **control:** digital state or commands may affect connected instruments and
  facility-support functions; precise protocols and control paths are not
  published;
- **decision:** diagnostic or QMS outputs may affect reporting or product
  decisions, but decision authority and validation gates are not modeled.

[WFL-0004](wfl-0004-high-consequence-material-lifecycle.md) adds direct
WHO normative objectives for collection and receipt, inventory, transfer,
storage, disposal, and incident review. This broadens lifecycle coverage but
does not validate Crawford's HCL architecture, a LIMS schema, or facility
custody practice.

> **Claim record — WFL-0002-C03 | analytic-judgment**
> **Claim:** Figure 2 and the accompanying prose are sufficient for a candidate
> data, material, and control dependency map, but not for confirmed trust
> boundaries, data lineage, chain of custody, or a complete laboratory
> lifecycle.
> **Claim status:** active
> **Scope:** Editorial assessment of the source model's suitability for the
> defensive wiki.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> Figure 2; §§ Cyber elements of high-containment laboratories, Methods —
> Asset-impact analysis.
> **Basis / limits:** The source explicitly names process and asset classes,
> but does not show identities, privileges, protocols, network zones, custody
> states, retention, or destruction. Further detail requires independent
> workflow and normative evidence.

## Candidate trust boundaries

The publication mentions external vendors, third-party platforms,
collaborators, institution-wide infrastructure, and diagnostic networks. These
references indicate where boundaries of responsibility or trust may exist, but
do not establish their configuration. They therefore remain candidate
boundaries and are not converted into facility-level network claims.

## Consequence classes

The source's asset-impact analysis connects compromise with potential worker-
safety, public-health, security, scientific-advancement, and financial
consequences. Table 1 contains 13 potential-loss rows, not 13 incidents. One
complete cyber-to-safety path is developed in
[RSK-0001](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md); the
other rows remain source-level candidates until sufficient evidence becomes
available.

## Evidence and uncertainty

> **Claim record — WFL-0002-C04 | analytic-judgment**
> **Claim:** WFL-0002 is a useful initial exposure model for HCLs, but does not
> satisfy the criterion for a complete laboratory or biobank lifecycle because
> accession, consent and authorization, formal custody, retention and
> destruction, validated trust boundaries, and a recovery workflow are absent.
> **Claim status:** superseded
> **Scope:** Coverage assessment as of 2026-07-11.
> **As of:** 2026-07-11.
> **Review after:** 2027-01-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> Figure 2; §§ Methods, Cyber considerations in HCLs, Conclusion.
> **Basis / limits:** The absent elements are not presumed absent from real
> HCLs; they are simply not modeled by this source. The gap must be addressed
> with WHO or LIMS, biobank, and primary workflow evidence.
> **Superseded by:** `WFL-0002-C06` after direct WHO lifecycle ingest.

> **Claim record — WFL-0002-C06 | analytic-judgment**
> **Claim:** WHO 2024 adds normative lifecycle, accountability, and review
> objectives around `WFL-0002`, but the HCL page still lacks validated
> accession and identity, LIMS lineage, formal custody, implementation
> architecture, and measured recovery or assurance.
> **Claim status:** active
> **Scope:** Reconciliation of the Crawford HCL exposure model with general WHO
> laboratory guidance.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> Figure 2; §§ Cyber elements of high-containment laboratories, Sample storage;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§1.1–1.2, printed pp. 2–3; §§6.3–7, printed pp. 31–44.
> **Basis / limits:** WHO supplies broad normative stages and control
> objectives, not HCL-specific architecture or implementation evidence.
> Missing evidence is a corpus gap, not proof that real HCLs lack lifecycle
> controls.

Historical-event examples in `SRC-0002` do not raise the workflow's evidence
status: they are mostly secondary, and the Oxford example is explicitly not an
HCL. No incident or specific attack vector is used to confirm the architecture.

## Related pages

- [SRC-0019 — Canadian Biosafety Standard](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [GOV-0009 — Canadian CBS governance](../governance/gov-0009-canadian-biosafety-standard-third-edition.md)

- [SYS-0001 — Containment-support cyberphysical systems](../systems/sys-0001-hcl-containment-support-systems.md)
- [RSK-0001 — Disruption of digitally supported containment functions](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md)
- [WFL-0001 — Systems model of a single biomanufacturing facility](wfl-0001-biomanufacturing-system.md)
- [WFL-0003 — Information and control flows in biopharmaceutical manufacturing](wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
- [WFL-0004 — Lifecycle of high-consequence and biosecurity-relevant laboratory material](wfl-0004-high-consequence-material-lifecycle.md)
- [GOV-0001 — WHO Laboratory Biosecurity Guidance 2024](../governance/gov-0001-who-laboratory-biosecurity-guidance-2024.md)
- [CON-0001 — Cyberbiosecurity](../concepts/con-0001-cyberbiosecurity.md)
- [SRC-0002 — Crawford et al. 2023](../sources/src-0002-crawford-high-containment-laboratories-2023.md)
- [SRC-0003 — Guttieres et al. 2019](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [SRC-0004 — WHO Laboratory Biosecurity Guidance 2024](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)

## Sources

- [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
  Figure 2; §§ Methods, Cyber considerations in HCLs, Identified Areas of Impact.
- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md), Figures 1–2;
  §§ Digital Information Flow in Biomanufacturing, Considerations for Emerging
  Biologic Products.
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
  §§1.1–1.2, 6.3–7; Annexes 1–2.
