---
id: SYN-0021
type: synthesis
title: Genomic assets, lifecycle and system-boundary reconciliation
aliases:
  - GEN-AS WL SD reconciliation
  - Genomics map and lifecycle synthesis
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0008
  - SRC-0014
  - SRC-0016
  - SRC-0027
  - SRC-0033
  - SRC-0035
sensitivity: public
dual_use: low
jurisdictions:
  - United States
  - European Union
  - United Kingdom
relations:
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: SYN-0021-C01
    evidence:
      - source: SRC-0005
        locator: "NIST IR 8432 genomic properties, assets, lifecycle, stakeholder and ecosystem evidence, §§2-5 and Appendix A, printed pp. 3-33"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: SYN-0021-C01
    evidence:
      - source: SRC-0006
        locator: "NIST genomic mission/objective, system, lifecycle, identity and responsibility classes, §§1.2, 3.2-3.3 and 5.1-5.12, PDF pp. 15-18, 24-30 and 32-39"
  - predicate: evidenced-by
    target: SRC-0007
    claim_id: SYN-0021-C01
    evidence:
      - source: SRC-0007
        locator: "NIST genomic privacy data-flow and system/interface context, Volume C §§2-4 and supplement model; one NIST programme lineage with SRC-0005/0006"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: SYN-0021-C01
    evidence:
      - source: SRC-0008
        locator: "Operational NHSBT sample-to-DNA-genotype-to-transfusion-matching segment and programme boundary, SRC-0008-C06, annual report pp. 30-31"
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: SYN-0021-C01
    evidence:
      - source: SRC-0014
        locator: "Controlled sequencer-to-read/file-to-software boundary and measured processing outcomes, paper §§2.2-2.3, 3 and 5-6, printed pp. 767-776/PDF pp. 4-13"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: SYN-0021-C01
    evidence:
      - source: SRC-0016
        locator: "EHDS EHR/health-data identity, rights, access, permit, infrastructure, responsibility and staged-application predicates, Articles 1-105, PDF pp. 29-91"
  - predicate: evidenced-by
    target: SRC-0027
    claim_id: SYN-0021-C01
    evidence:
      - source: SRC-0027
        locator: "APHL laboratory/public-health exchange system, interface-test, staged production and monitoring evidence, SRC-0027-C03/C04/C08–C10 and manual Chapters 2–9"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: SYN-0021-C01
    evidence:
      - source: SRC-0033
        locator: "NASEM biological-AI data/model/compute/researcher/decision-maker and research-interface classes, Chapters 2, 4-5, physical pp. 40-46 and 67-102"
  - predicate: evidenced-by
    target: SRC-0035
    claim_id: SYN-0021-C01
    evidence:
      - source: SRC-0035
        locator: "PATH-SAFE non-human samples/pathogens/genomes/metadata/stewards, sample-to-result/report lanes and platform sharing boundaries, SRC-0035-C03–C06"
tags:
  - genomics
  - omics
  - assets
  - stakeholders
  - lifecycle
  - systems
  - trust-boundaries
  - evidence-reconciliation
---

# Genomic assets, lifecycle and system-boundary reconciliation

## Question and provenance

This synthesis tests only `GEN-AS`, `GEN-WL` and `GEN-SD` at SF2. It uses the
NIST genomic corpus as one combined programme lineage, not three independent
sources. Independence comes from NASEM, UK PATH-SAFE, EU EHDS, APHL and the
controlled USENIX study where their claims are appropriate. Canonical pages
normalize those sources but do not create additional lineages.

Human genomic consent/kinship and non-human pathogen/surveillance stewardship
remain distinct. APHL laboratory/public-health interface test evidence is used
only for validated boundary instances; it is not generalized to validation of
the complete genomic topology, every pipeline or every organization.

> **Claim record — SYN-0021-C01 | analytic-judgment**
> **Claim:** The reconciliation combines one NIST genomic programme lineage
> with materially independent NASEM, PATH-SAFE, EHDS, APHL and USENIX roles and
> preserves their human/non-human, normative/operational and validation-scope
> differences.
> **Claim status:** active
> **Scope:** SF2 provenance/counting for `GEN-AS/WL/SD`; not independent
> confirmation of every class, boundary, implementation or effect.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Source IDs and exact locators in frontmatter; canonical
> [AST-0001](../assets/ast-0001-genomic-data.md),
> [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) and
> [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) source/
> relation boundaries; `SRC-0033-C02/C03`, `SRC-0035-C03/C04`,
> `SRC-0027-C03/C04/C08–C10` and `SRC-0016-C04–C07`.
> **Basis / limits:** Issuers, methods, sectors and evidence states are direct.
> Claim-appropriate independence is applied at criterion level, not manufactured
> per document or per literal class.

## Complete asset and stakeholder reconciliation

| Frozen literal | Direct canonical location | Independent extension or boundary | Accepted meaning |
| --- | --- | --- | --- |
| Samples | `AST-0001-C06` links specimen/material to derived genomic state | PATH-SAFE `SRC-0035-C03` adds implemented animal/food/environment samples | physical material is not equated with sequence data |
| Sequences/variants | `AST-0001-C01/C04` | PATH-SAFE adds pathogen sequence/genomic outputs without human kinship meaning | digital sequence/variant class, not a sample or person |
| Phenotype | `AST-0001-C02` | NASEM adds biological data/model use but is not used to invent clinical phenotype completeness | phenotype is distinct from genotype/annotation |
| Annotations and metadata | `AST-0001-C01/C02/C04`; `SRC-0006-C09` | PATH-SAFE supplies surveillance/project metadata and documents interoperability limits | metadata is not complete provenance or consent |
| Consent/provenance | `AST-0001-C03`; `WFL-0005-C05` | EHDS supplies independent rights/access/correction/permit/audit state; NASEM adds dataset/model provenance | human consent/right and technical lineage remain different |
| Systems | `SYS-0003-C01/C04–C06` | APHL/NASEM add laboratory exchange and research compute/interfaces | system class coverage is not full deployment inventory |
| Subjects and relatives | `AST-0001-C03` directly preserves subjects/relatives | NASEM independently adds subjects/participants but explicitly does not supply relatives or consent roles | kin impact is human-genomic, not projected onto non-human data |
| Researchers and clinicians | `WFL-0005-C07`; NIST stakeholder classes | NASEM adds researchers/developers/decision makers; APHL/EHDS add clinical/public-health roles | roles are classes, not one universal RACI |
| Non-human stewards | non-human genomic scope in `AST-0001-C01/C04` | PATH-SAFE directly adds veterinary, food/environment laboratory and public-authority stewardship | stewardship is not human consent or complete sector ownership |

> **Claim record — SYN-0021-C02 | analytic-judgment**
> **Claim:** `GEN-AS` passes: samples, sequences/variants, phenotype,
> annotations, metadata, consent/provenance, systems, subjects, relatives,
> researchers, clinicians and non-human stewards are all directly represented
> and explicitly reconciled across independent human and non-human lineages.
> **Claim status:** active
> **Scope:** Frozen class-level `GEN-AS`; not a complete inventory, ownership/
> rights allocation, sensitivity scheme, adoption or outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0021-C01` and matrix above; `AST-0001-C01`–`C08`;
> [AST-0008](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md),
> `AST-0008-C01–C04`; [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md),
> `AST-0003-C05`; `SRC-0035-C03/C04`; `WFL-0005-C05/C07`.
> **Basis / limits:** Every literal class is located and the complete map meets
> SF2. No one source or organization is claimed to hold the complete inventory.

## End-to-end genomic lifecycle

| Stage | Direct path | Independent support and unresolved implementation boundary |
| --- | --- | --- |
| Collection | specimen/subject/non-human source → collected material + identity/context | PATH-SAFE directly implements non-human/environment sampling; no universal custody/consent system |
| Preparation | received material → accession/preparation/library or assay-ready state | NIST model plus PATH-SAFE laboratory processing; protocols differ by context |
| Generation | prepared biological input → instrument output/read/sequence/measurement | USENIX directly exercises sequencer→read/file and PATH-SAFE reports assay/sequencing lanes; not one clinical validation result |
| Analysis | generated data → pipeline/algorithm/database → variant/feature/model/result | NIST functional map, USENIX controlled processing and NASEM research compute/model context; accuracy is not generalized |
| Sharing/reuse | data/result + metadata/conditions → repository, partner, research or public-health use | PATH-SAFE documents real deposits/exchanges and unresolved legal/metadata/ownership boundaries; EHDS supplies staged permitted-use governance |
| Retention/disposition | data/record → retain/archive/delete/dispose according to purpose/rule | NIST canonical lifecycle represents data/record retention/disposition; complete physical-sample disposition, universal organization schedule and deletion proof remain unestablished |
| Consent/provenance change | purpose/permission/lineage state → reviewed authorization, correction, withdrawal/restriction or updated provenance | NIST human-genomic and EHDS rights/permit/accountability states are independent; they do not apply identically to non-human surveillance |

> **Claim record — SYN-0021-C03 | analytic-judgment**
> **Claim:** `GEN-WL` passes: one reconciled path traces collection,
> preparation, generation, analysis, sharing/reuse, retention/disposition and
> consent/provenance changes at SF2 while preserving human/non-human custody,
> rights and implementation differences.
> **Claim status:** active
> **Scope:** Frozen `GEN-WL`; not one deployed end-to-end system, validated
> consent propagation, common retention schedule or lifecycle effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md),
> `WFL-0005-C01/C02/C04/C05/C07/C08/C10`;
> [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md),
> `WFL-0007-C06`; `SRC-0035-C03/C04`; `SRC-0014-C02/C03/C04`; EHDS lifecycle
> overlay in current `WFL-0005-C10`.
> **Basis / limits:** All literal stages and at least two independent roles are
> direct. Missing one implemented universal chain is an implementation/
> assurance limit, not a missing stage in this criterion.

## Systems, responsibilities and validated boundaries

| Frozen system/dependency literal | Located components and boundaries | Validation/evidence limit |
| --- | --- | --- |
| Instruments | sequencer/laboratory instrument acquisition and output boundaries in `SYS-0003-C01/C04`; USENIX controlled sequencer→file path | one controlled path does not validate all instruments |
| LIMS and storage | laboratory/inventory/result functions, databases, repositories and storage in `SYS-0003-C01/C04–C06`; APHL exchange nodes | class/function map, not an organization inventory |
| Cloud/HPC | NIST cloud/storage/compute plus NASEM research cloud/HPC/compute in `SYS-0011-C01–C03` | no universal tenancy/configuration or performance claim |
| Pipelines and databases | sequence-processing/bioinformatics pipeline, tools/dependencies and genomic/reference/research databases in `SYS-0003`/`SYS-0011` | component presence does not establish trustworthy output |
| EHR and research interfaces | NIST clinical/research use boundaries plus EHDS EHR/data-infrastructure and NASEM research interfaces | regulatory/design state and deployment state remain separate |
| Identities and responsibilities | subject/specimen/user/organization/partner roles, authorization, stewardship and accountable exchange/processing actors | no common IAM or complete operational RACI is inferred |
| Validated boundaries | APHL distinguishes interface specification/conformance testing, staged production and post-production monitoring; USENIX directly tests one input→file→software boundary | these are validated boundary instances, not validation of the entire genomic topology or every pipeline/interface |

> **Claim record — SYN-0021-C04 | analytic-judgment**
> **Claim:** `GEN-SD` passes narrowly: the reconciled map contains instruments,
> LIMS, storage, cloud/HPC, pipelines, databases, EHR/research interfaces,
> identities, responsibilities and validated boundary instances at SF2 without
> claiming whole-topology validation.
> **Claim status:** active
> **Scope:** Frozen `GEN-SD` component/boundary map; not one deployed genomic
> architecture, universal IAM/RACI, conformance result or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md),
> `SYS-0003-C01/C04–C06/C08`;
> [SYS-0011](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md),
> `SYS-0011-C01–C03`;
> [SYS-0009](../systems/sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md),
> `SYS-0009-C01–C04`; `SRC-0027-C03/C04/C08–C10` and
> `SRC-0014-C02/C06/C08`.
> **Basis / limits:** Every literal component and identity/responsibility class
> is located. APHL supplies direct validated-interface instances; independently,
> USENIX supplies a controlled exercised boundary rather than interface/
> conformance validation. Neither is generalized to system-wide validation.

## Non-promotions and score decision

`GEN-ST/TV/XT/CT/GR` remain Pass. `GEN-CI` remains Partial because no genomic
primary case/controlled study yet has the required downstream clinical,
research, privacy or biological outcome plus independent context. `GEN-AE`
remains Partial because no deployed genomic safeguard has both a scoped test
metric and independent effectiveness evaluation.

> **Claim record — SYN-0021-C05 | analytic-judgment**
> **Claim:** Only `GEN-AS/WL/SD` change; `GEN-CI/AE` remain Partial because
> structural class/lifecycle/boundary completion cannot substitute for their
> SF3 downstream-outcome and safeguard-effectiveness predicates.
> **Claim status:** active
> **Scope:** Current frozen GEN sufficiency after active `SYN-0020`; not a
> claim that no external genomic case or evaluation exists.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0021-C01–C04`; current `GEN-*` rows/source floors and
> `SYN-0001-C36` in [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** Each unchanged cell has a distinct result/effectiveness
> requirement. No structural evidence is promoted across that boundary.

> **Claim record — SYN-0021-C06 | artifact-observation**
> **Claim:** Independent strict review accepts exactly `GEN-AS`, `GEN-WL` and
> `GEN-SD` Partial→Pass. Totals become 53 Pass, 54 Partial and 3 Absent =
> 53/110 (48.2%); Genomics/omics becomes 8/10 and critical cells become 48
> Pass, 42 Partial and 1 Absent. Dimensions at least 9/10 and all global gates
> remain unchanged.
> **Claim status:** active
> **Scope:** Filesystem after activation of `SYN-0021` and matching rubric
> checkpoint; not 48.2% absolute domain completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0021-C01–C05`; frozen criteria/source floors; prior
> `SYN-0001-C36`; independent audits completed 2026-07-12.
> **Basis / limits:** Three critical Partial→Pass transitions change the totals;
> Partial remains zero points and no global gate moves.

## Safety boundary

The synthesis retains class/stage/interface evidence only. It omits any sample
or sequence content, identity, credential, endpoint, configuration, assay/
pipeline parameter, exploit detail and target-specific weakness.

> **Claim record — SYN-0021-C07 | analytic-judgment**
> **Claim:** The genomic reconciliation is defensive and class-level and adds
> no operational biological/cyber detail or whole-system validation claim.
> **Claim status:** active
> **Scope:** Local page content; not a runtime/downstream-use guarantee for
> every linked external resource.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYN-0021-C01–C06`; local page content.
> **Basis / limits:** Content was checked for actionable details; high-level
> public class/lifecycle/boundary comparison remains useful.

## Related pages

- [AST-0001 — genomic assets](../assets/ast-0001-genomic-data.md)
- [WFL-0005 — genomic lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003 — genomic ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [SYS-0009 — integrated laboratory exchange](../systems/sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md)
- [SYS-0011 — biological-AI ecosystem](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md)
- [SRC-0035 — PATH-SAFE](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
- [SYN-0001 — frozen coverage rubric](syn-0001-coverage-rubric.md)

## Sources

- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0027](../sources/src-0027-aphl-integrated-laboratory-information-public-health-exchange.md)
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)
