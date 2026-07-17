---
id: SYN-0020
type: synthesis
title: Foundational cross-sector asset, lifecycle and governance reconciliation
aliases:
  - FND-AS WL GR reconciliation
  - Cross-sector cyberbiosecurity foundation map
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0004
  - SRC-0006
  - SRC-0011
  - SRC-0012
  - SRC-0015
  - SRC-0016
  - SRC-0019
  - SRC-0022
  - SRC-0026
  - SRC-0031
  - SRC-0032
  - SRC-0033
sensitivity: public
dual_use: low
jurisdictions:
  - Global
  - United States
  - European Union
  - United Kingdom
  - Canada
  - African Union regional context
relations:
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: SYN-0020-C01
    evidence:
      - source: SRC-0006
        locator: "NIST genomic asset/lifecycle/control profile, §§1.2, 3.2-3.3 and 5.1-5.12, PDF pp. 15-18, 24-30 and 32-39"
  - predicate: evidenced-by
    target: SRC-0011
    claim_id: SYN-0020-C01
    evidence:
      - source: SRC-0011
        locator: "Synthetic-nucleic-acid order, identity, provider, equipment and screening lifecycle, Framework pp. 1-14"
  - predicate: evidenced-by
    target: SRC-0022
    claim_id: SYN-0020-C01
    evidence:
      - source: SRC-0022
        locator: "Biospecimen/material/data/stakeholder and lifecycle evidence, NCI Best Practices Chapters A-C and J-L, physical pp. 29-108 and 275-322"
  - predicate: evidenced-by
    target: SRC-0031
    claim_id: SYN-0020-C01
    evidence:
      - source: SRC-0031
        locator: "Biomanufacturing material/data/control/quality lifecycle, ICH Q13 §§2-4 and Annexes I-III"
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: SYN-0020-C01
    evidence:
      - source: SRC-0026
        locator: "Clinical laboratory total-testing process and asset/actor context, WHO LQMS Chapters 1-7 and process-pathway figures"
  - predicate: evidenced-by
    target: SRC-0032
    claim_id: SYN-0020-C01
    evidence:
      - source: SRC-0032
        locator: "Agriculture production/value-chain/data lifecycle and stakeholder/system classes, Parts II-IV and implementation matrices, physical pp. 32-134"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: SYN-0020-C01
    evidence:
      - source: SRC-0033
        locator: "Biological-AI data/model/compute/output/stakeholder and DBTL lifecycle, Chapters 2, 4-5 and Appendix A, physical pp. 40-46, 67-102 and 106-145"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: SYN-0020-C05
    evidence:
      - source: SRC-0004
        locator: "WHO final normative guidance identity, scope, current official status and adoption/force limits, copyright and §1, PDF pp. 4 and 21-23"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: SYN-0020-C05
    evidence:
      - source: SRC-0012
        locator: "UK voluntary screening guidance identity, scope, roles, force/adoption limits and current substantive page, HTML lines 609-623 and 708-1070"
  - predicate: evidenced-by
    target: SRC-0015
    claim_id: SYN-0020-C05
    evidence:
      - source: SRC-0015
        locator: "Current corrected U.S. administrative regulation, dates, scope, exceptions and compliance design, SRC-0015-C03/C05/C08 and 28 CFR Part 202 PDF pp. 1 and 72-95"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: SYN-0020-C05
    evidence:
      - source: SRC-0016
        locator: "EU binding legislative Regulation, in-force/staged dates, scope and exceptions, Articles 1-105, PDF pp. 29-91"
  - predicate: evidenced-by
    target: SRC-0019
    claim_id: SYN-0020-C05
    evidence:
      - source: SRC-0019
        locator: "Canadian standard and licence/permit adoption mechanism, Preface/Figure 1 and §§1.1-1.2.4, PDF pp. 6-7 and 34-37"
tags:
  - foundations
  - cross-sector
  - assets
  - stakeholders
  - lifecycle
  - governance
  - evidence-reconciliation
---

# Foundational cross-sector asset, lifecycle and governance reconciliation

## Question, sectors and counting rules

This synthesis tests only `FND-AS`, `FND-WL` and `FND-GR` at SF2. The seven
applied-sector dimensions are Genomics/omics (`GEN`), Synthesis/engineering
biology (`SEB`), Laboratories/biobanks (`LAB`), Biomanufacturing/OT (`BMO`),
Clinical/public health (`CPH`), Agriculture/environment (`AGE`) and biological
AI/bioinformatics (`AIB`). Foundations, threats/incidents, controls and
governance are cross-cutting dimensions, not additional applied sectors.

Canonical sector pages normalize classes and stages; they do not create new
external lineages. SF2 rests on materially independent underlying NIST, U.S./
UK screening, WHO/NCI, ICH, AU, NASEM and multi-jurisdiction governance
sources. Joint, derivative or same-programme records remain grouped as in
their source/synthesis pages. A class can be direct at criterion level without
every sector repeating it in two sources; the complete cross-sector claim must
be supported by at least two independent claim-appropriate lineages.

> **Claim record — SYN-0020-C01 | analytic-judgment**
> **Claim:** The seven applied-sector canonical pages form one bounded
> cross-sector normalization layer over multiple materially independent
> lineages, without multiplying canonical pages, derivatives or same-programme
> records as additional evidence.
> **Claim status:** active
> **Scope:** SF2 provenance/counting for `FND-AS/WL`; not independence for
> every asset, lifecycle stage, implementation result or effect.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Canonical pages and their typed evidence:
> [AST-0001](../assets/ast-0001-genomic-data.md),
> [AST-0004](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md),
> [AST-0005](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md),
> [AST-0007](../assets/ast-0007-biomanufacturing-assets-stakeholders.md),
> [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md),
> [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md) and
> [AST-0008](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md);
> direct underlying routes: [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§1.2–1.3 and Figure 1, printed pp. 4–5 (PDF pp. 15–16), and Tables 4,
> 9–11 and 26–29, printed pp. 32–38, 57–85 and 141–146 (PDF pp. 43–49,
> 68–96 and 152–157); [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§III–V, printed pp. 5–13 (PDF pp. 6–14); [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§B.1–B.4, C.1.2, C.2.6, C.3.2 and C.5–C.6, printed pp. 4–8, 35–37,
> 50 and 57–70 (physical pp. 7–11, 38–40, 53 and 60–73);
> [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
> §§3.1.3–3.1.7, 4.1–4.4 and 4.7–4.10, printed pp. 3–6 and 8–14
> (physical pp. 8–11 and 13–19); [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> §§1-2–1-3, pp. 11–15, and the asset/stakeholder chapters at pp. 36–72,
> 152–160 and 182–207; [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> Executive Summary and ecosystem/role material, printed pp. 4–15 and 35–38
> (physical pp. 10–21 and 41–44); and
> [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapters 4–5, printed pp. 50–77 (physical pp. 71–98), and Appendix A,
> printed pp. 85–124 (physical pp. 106–145).
> **Limits:** Sector labels, canonical claims and underlying issuers are
> explicit. Normalization is editorial; it is not an inventory census,
> ownership allocation, deployment or cross-sector technical architecture.

## Canonical asset and affected-stakeholder map

| Applied sector | Biological assets | Digital/information assets | Physical/system assets | Human assets/actors | Affected stakeholders | Non-equivalence boundary |
| --- | --- | --- | --- | --- | --- | --- |
| GEN | specimens, DNA/RNA material and non-human genomic material | sequences/variants, phenotype, annotations, metadata, consent/provenance and analytical outputs | sequencers, storage/compute and laboratory interfaces | subjects/relatives, researchers, clinicians and data stewards | subjects/kin, patients, research communities and populations | a sequence is information derived from material, not the specimen or person |
| SEB | synthesized material and resulting products | sequence/design/order, customer identity, screening record and IP | provider systems, synthesis equipment/automation and delivery interfaces | customer/user, provider/manufacturer staff, reviewers and intermediaries | providers/users, research/public-health and public/biosecurity interests | an order/design is not a physical product; screening identity is not universal identity proof |
| LAB | specimens, strains/cell lines, reagents and stored collections | metadata, consent, inventory/custody, ELN/LIMS and result records | instruments/automation, storage/freezers and facility/containment | donors/patients, workers, researchers, custodians and oversight roles | donors/patients, staff, receiving researchers and public/community | biobank stewardship/consent differs from diagnostic custody and HCL containment |
| BMO | raw materials, cell banks, intermediates and product | recipe/IP, process/quality data, batch/release and QMS records | sensors/actuators, control/PAT, unit operations and facility/supply interfaces | development, operations, quality/release, vendor and regulator roles | workforce, patients/users, manufacturer and supply/public interests | material state, control signal and authorized release record are distinct |
| CPH | patient specimen and biological analyte/pathogen state | identity/order/result, LIS/EHR/reporting and correction state | instruments, middleware, clinical/reference/public-health systems | patient, clinician, laboratory/public-health staff and data/system roles | patients/relatives and represented populations plus care/public-health actors | analytical result, clinical interpretation and public-health notification are different decision states |
| AGE | crop/livestock/aquatic/wildlife/pathogen/sample and ecosystem state | sensor/remote/traceability/model, genomic/surveillance and business data | farm equipment/OT/IoT, sensors, laboratory/platform and supply interfaces | farmers, veterinarians, laboratory/regulator and value-chain roles | producers/workers, consumers, animal/plant health and ecosystems/public | represented breadth is not a complete seed/herd inventory or common custody architecture |
| AIB | biological/genomic/experimental input and physical validation material | datasets/labels, models/code, dependencies, outputs/designs, provenance and IP | compute/cloud/HPC, software environment and laboratory interface | subjects/relatives, developers, researchers and decision makers | subjects/kin, scientific/clinical/agricultural users and affected public | model, training data, output and experimentally validated biological state are not interchangeable |

Every row contains all four top-level asset classes and at least one affected-
stakeholder class. The map does not require identical granularity or ownership
semantics across sectors; it requires explicit class coverage and preserves
where data/material, operator/subject and decision/affected-party differ.

> **Claim record — SYN-0020-C02 | analytic-judgment**
> **Claim:** `FND-AS` passes: one canonical matrix covers biological, digital,
> physical and human assets plus affected stakeholders in all seven applied-
> sector dimensions, with material/data/actor/affected-party non-equivalences
> explicit at SF2.
> **Claim status:** active
> **Scope:** Foundational class map; not complete sector inventories, asset
> ownership, sensitivity classification, system topology, adoption or outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0020-C01` and matrix above; `AST-0001-C01`–`C08`;
> `AST-0004-C01`–`C05`; `AST-0005-C01`–`C04`; `AST-0007-C01`–`C04`;
> `AST-0006-C01`–`C04`; `AST-0003-C01`–`C05`; `AST-0008-C01`–`C05`.
> GEN physical/system and actor extensions are additionally located in
> [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md),
> `SYS-0003-C01/C04`, and
> [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md), `WFL-0005-C07`.
> **Basis / limits:** Each required sector×class intersection is direct in a
> canonical page backed by multiple independent source programmes. Granularity
> varies and no cross-sector technical or legal equivalence is inferred.

## Common lifecycle primitives and transfer limits

| Foundational primitive | Located sector realizations | Where it does not transfer unchanged |
| --- | --- | --- |
| Plan/authorize/initiate | research/consent and genomic purpose; synthesis procurement; biobank protocol; manufacturing development/control strategy; clinical order; farm planning; AI task/model purpose | patient consent, purchase authorization, manufacturing change control and model-use authorization are not one legal gate |
| Acquire/collect/receive | specimen/sample/material collection or receipt; raw supply; biological/observational data acquisition; order receipt | digital dataset acquisition has no physical custody unless linked to material; an order is not sample receipt |
| Identify/accession/classify | subject/specimen/order identity, accession/inventory, material lot/state, dataset/label/provenance | patient identity, customer legitimacy, lot identity and model version need different evidence and rights |
| Transform/process/analyse | sequencing/analysis; physical build/synthesis; specimen processing/testing; manufacturing unit operations; agricultural production/analytics; AI training/inference/DBTL | analysis does not always change biological material; synthesis/manufacture does; AI inference is not wet-lab validation |
| Validate/review/decide/release | genomic interpretation, screening review, laboratory validation/report authorization, quality/release, surveillance/advisory decision, model/human/experimental validation | product release, clinical interpretation, screening disposition and model validation have different authorities and acceptance evidence |
| Transfer/share/notify/act | genomic reuse, custody/transport, product distribution, report/notification, value-chain/traceability action, model/design-to-experiment handoff | data sharing is not material custody; clinical notification is not trade movement; intended action is not observed outcome |
| Retain/monitor/update/correct | data/material retention, inventory monitoring, batch/quality history, result correction, surveillance/model update | physical retention/disposal, legal record retention, corrected clinical result and model update are different state transitions |
| Close/return/dispose/retire/recover | specimen/material closeout/disposal, manufacturing diversion/disposition, clinical correction/continuity and agriculture fallback; model retirement is an open gap | model retirement remains incomplete in AIB; farm/product disposition and some sector recovery stages are incomplete and are not filled editorially |

The common model is a vocabulary for locating state transitions, not a single
universal process. Four independently evidenced sectors would meet the literal
minimum; the matrix uses all seven and marks missing stages instead of
projecting a complete lifecycle into every sector.

> **Claim record — SYN-0020-C03 | analytic-judgment**
> **Claim:** Eight common primitives normalize initiation through closeout
> across seven sector workflows while explicitly preserving legal, custody,
> material/data, decision/authority and incomplete-stage non-transfer limits.
> **Claim status:** active
> **Scope:** Foundational lifecycle vocabulary; not a universal procedure,
> complete lifecycle in every sector, process equivalence or implementation.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md),
> `WFL-0005-C01`–`C10`;
> [WFL-0008](../workflows/wfl-0008-nucleic-acid-procurement-screening-lifecycle.md),
> `WFL-0008-C01`–`C05`;
> [WFL-0009](../workflows/wfl-0009-biospecimen-material-data-lifecycle.md),
> `WFL-0009-C01`–`C04`;
> [WFL-0003](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md),
> current `WFL-0003-C01/C02/C05/C06`;
> [WFL-0010](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md),
> `WFL-0010-C01`–`C05`;
> [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md),
> `WFL-0007-C01`–`C06`; and
> [WFL-0011](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md),
> `WFL-0011-C01`–`C05`.
> **Basis / limits:** Stages and missing-stage statements are direct in
> canonical workflows across more than four independent sector lineages. The
> eight labels are editorial normalization and do not repair sector gaps.

> **Claim record — SYN-0020-C04 | analytic-judgment**
> **Claim:** `FND-WL` passes at SF2: the foundational synthesis defines common
> lifecycle primitives from at least four sectors and records where they do not
> transfer; using seven sectors does not imply each has a complete lifecycle.
> **Claim status:** active
> **Scope:** Frozen `FND-WL` only; not a sector-specific `WL` promotion,
> universal custody chain, common legal gate or observed operation.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0020-C01/C03`; workflow claims and matrices cited above;
> exact frozen criterion in [SYN-0001](syn-0001-coverage-rubric.md);
> direct lifecycle routes: [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§1.2–1.3 and Figure 1, printed pp. 4–5 (PDF pp. 15–16);
> [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md), §§I–V,
> printed pp. 4–13 (PDF pp. 5–14); [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> §§B.11–B.12.3 and C.2–C.2.10.4, printed pp. 29–34 and 41–57
> (physical pp. 32–37 and 44–60); [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1.4–3.1.7 and 4.1–4.4, printed pp. 4–6 and 8–11
> (physical pp. 9–11 and 13–16); [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> §§1-2–1-3 and the rendered workflow, pp. 11–15, and Chapter 5,
> pp. 61–72; [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> Figure 2 and related text, printed pp. 9–10 (physical pp. 15–16), and
> action packages, printed pp. 81–99 (physical pp. 87–105); and
> [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapters 2–3, printed pp. 19–37 (physical pp. 40–58), and Chapter 5,
> printed pp. 69–74 (physical pp. 90–95).
> **Limits:** The literal sector count, shared primitives and explicit
> non-transfer predicates are all present. Sector completeness is assessed by
> separate cells and remains unchanged.

## Comparative governance method

The method separates six fields that are often collapsed: instrument class;
issuer/jurisdiction; publication/effect/application/current dates; binding
force and duty population; normative/observed adoption state; and exceptions,
conflicts and evidence gaps. The following rows are class exemplars, not
claims that one instrument exhausts its jurisdiction.

| Required class | Exact exemplar | Jurisdiction/force | Adoption/currentness | Exceptions/conflicts boundary |
| --- | --- | --- | --- | --- |
| Law / binding legislative act | EU Regulation 2025/327 EHDS | EU legislative regulation, in force and directly applicable at EU level | signed/published/in-force dates are separate from staged 2027–2035 application; national/product rollout unknown | permits, prohibited uses, opt-out and national safeguards; other EU law preserved |
| Administrative regulation | U.S. DOJ 28 CFR Part 202 | binding final administrative regulation for scoped persons/transactions | effective/correction/compliance dates and corrected current eCFR state distinguished | prohibited/restricted/exempt transaction classes; not a general data-rights law |
| Standard | Canadian Biosafety Standard Third Edition | national standard applied through relevant HPTA licence/HAR permit conditions | publication, 2023 effective date, 2024 minor update and 2026 alignment notice separated; facility compliance unknown | specimen/activity exclusions, alternatives and Act-over-standard conflict rule |
| Normative guidance | WHO Laboratory Biosecurity Guidance 2024 and UK DSIT screening guidance | global final recommendations versus UK voluntary expected practice; neither is universal domestic law | publication/current presentation established; national/institutional adoption or provider uptake not inferred | risk/local-law tailoring and instrument-specific scope; cited laws are not imported |
| Draft / voluntary profile | NIST IR 8467 Second Public Draft | U.S. voluntary Community Profile in public-draft state | publication/comment-close/current 2PD status separated; no adoption/effective date or implementation census | draft priorities/tailoring are not final standard, compliance or effectiveness |

> **Claim record — SYN-0020-C05 | analytic-judgment**
> **Claim:** The comparative method distinguishes law, administrative
> regulation, standard, guidance and draft/profile and records jurisdiction,
> force, adoption, exceptions/conflicts and currency as separate fields.
> **Claim status:** active
> **Scope:** Instrument classification/comparison method; not legal advice,
> complete law for any jurisdiction, cross-compliance or implementation result.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0008](syn-0008-global-us-eu-uk-canada-governance-reconciliation.md),
> instrument/date matrix and `SYN-0008-C01/C03`; underlying `SRC-0004`,
> `SRC-0006`, `SRC-0012`, `SRC-0015`, `SRC-0016` and `SRC-0019` current
> claims/locators; matrix above.
> **Basis / limits:** Every literal method field is explicit across materially
> independent global/U.S./EU/UK/Canadian lineages. Exemplars are not generalized
> to unreviewed laws or jurisdictions.

> **Claim record — SYN-0020-C06 | analytic-judgment**
> **Claim:** `FND-GR` passes at SF2: a multi-jurisdiction comparative method
> now distinguishes all five required instrument classes and all six required
> method fields—including instrument class plus jurisdiction, force, adoption,
> exceptions and currency—without treating crosswalk as compliance.
> **Claim status:** active
> **Scope:** Frozen `FND-GR` method criterion; not a claim that every topic has
> complete global governance or that regimes are legally equivalent.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0020-C05`; [SYN-0008](syn-0008-global-us-eu-uk-canada-governance-reconciliation.md),
> `SYN-0008-C01`–`C04`; exact frozen criterion in `SYN-0001`.
> **Basis / limits:** The classification and comparison fields are direct at
> SF2. Topic-specific currentness/adoption still requires its own reconciliation.

## Non-promotions and strict score decision

This synthesis does not classify threat/hazard/technique/vulnerability
evidence, calibrate consequences, or assemble empirical positive and null/
failure assurance examples. `FND-TV/CI/AE` therefore remain Partial. Existing
`FND-ST/SD/XT/CT` remain Pass and are not counted again.

> **Claim record — SYN-0020-C07 | analytic-judgment**
> **Claim:** Only `FND-AS/WL/GR` change; `FND-TV/CI/AE` remain Partial because
> cross-sector assets, lifecycle vocabulary and governance method do not
> satisfy their distinct taxonomy, primary-case and SF3 assurance contracts.
> **Claim status:** stale
> **Scope:** Current frozen FND sufficiency after `SYN-0019`; not a claim that
> the represented corpus has no relevant threat/case/test evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0020-C01`–`C06`; current `FND-*` rows and source floors in
> [SYN-0001](syn-0001-coverage-rubric.md).
> **Limits:** Each non-promotion has a different literal/evidence-floor
> requirement. Similar vocabulary is not substituted for that evidence. This
> is a dated local rubric-accounting decision rather than an externally
> evidenced substantive claim; it is retained as historical context but is no
> longer maintained as active evidence.

> **Claim record — SYN-0020-C08 | artifact-observation**
> **Claim:** Independent strict review accepts exactly `FND-AS`, `FND-WL` and
> `FND-GR` Partial→Pass. Totals become 50 Pass, 57 Partial and 3 Absent =
> 50/110 (45.5%); Foundations becomes 7/10 and critical cells become 45 Pass,
> 45 Partial and 1 Absent. Dimensions at least 9/10 and all global gates remain
> unchanged.
> **Claim status:** active
> **Scope:** Filesystem after activation of `SYN-0020` and matching rubric
> checkpoint; not 45.5% absolute domain completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0020-C01`–`C07`; frozen criteria/source floors; prior
> `SYN-0001-C35` totals; independent literal/semantic/structural reviews
> completed 2026-07-12.
> **Basis / limits:** Three Partial→Pass changes produce the arithmetic; only
> `FND-GR` is critical. Partial remains zero points and no global gate moves.

## Safety boundary

The matrices contain only class-level public evidence. They omit identity,
sample/sequence content, farm/facility topology, credentials, operating/
screening/assay parameters, exploit mechanics and target-specific weaknesses.

> **Claim record — SYN-0020-C09 | analytic-judgment**
> **Claim:** The reconciliation is defensive and class-level and does not add
> operational biological/cyber detail or convert common vocabulary into a
> universal procedure.
> **Claim status:** stale
> **Scope:** Local synthesis content; not a downstream-use guarantee for every
> linked external resource.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYN-0020-C01`–`C08`; local page content.
> **Limits:** The page was checked for actionable operational detail;
> high-level public class/stage/governance comparison remains useful. This is
> a local page-content assertion, not an externally evidenced decision claim,
> so it is retained as a safety note but is no longer maintained as active
> evidence.

## Related pages

- [SYN-0024 — Cross-sector portfolio reconciliation](syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [AST-0001 — genomic assets](../assets/ast-0001-genomic-data.md)
- [AST-0004 — synthesis assets](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md)
- [AST-0005 — laboratory/biobank assets](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md)
- [AST-0007 — biomanufacturing assets](../assets/ast-0007-biomanufacturing-assets-stakeholders.md)
- [AST-0006 — clinical/public-health assets](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md)
- [AST-0003 — agriculture assets](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [AST-0008 — biological-AI assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [SYN-0008 — multi-context governance reconciliation](syn-0008-global-us-eu-uk-canada-governance-reconciliation.md)
- [SYN-0001 — frozen coverage rubric](syn-0001-coverage-rubric.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md)
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md)
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
