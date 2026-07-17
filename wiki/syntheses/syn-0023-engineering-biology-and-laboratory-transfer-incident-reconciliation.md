---
id: SYN-0023
type: synthesis
title: Engineering-biology and laboratory transfer/incident reconciliation
aliases:
  - SEB ST SD XT and LAB XT CI reconciliation
  - Engineering-biology laboratory transfer synthesis
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0002
  - SRC-0004
  - SRC-0005
  - SRC-0008
  - SRC-0009
  - SRC-0011
  - SRC-0012
  - SRC-0014
  - SRC-0019
  - SRC-0022
  - SRC-0023
  - SRC-0026
  - SRC-0033
sensitivity: public
dual_use: moderate
jurisdictions:
  - Global
  - United States
  - United Kingdom
  - Canada
relations:
  - predicate: evidenced-by
    target: SRC-0011
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0011
        locator: "U.S. sequence-provider, order/customer screening, review, benchtop-equipment and record/report design, Framework pp. 1-14"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0012
        locator: "UK provider/user/equipment, screening/review/identity/update and fulfilment boundaries, current guidance HTML lines 708-1070"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0033
        locator: "Engineering-biology design tools, foundry/cloud-lab/automation and DBTL input-output-feedback path, SRC-0033-C03–C05/C08, Chapters 2, 4–5 and Appendix A"
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0014
        locator: "Controlled biological/input-to-sequencer/read/file/software boundary and measured result, SRC-0014-C02/C03/C08, §§2.2–2.3 and 3, PDF pp. 4–8"
  - predicate: evidenced-by
    target: SRC-0002
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0002
        locator: "High-containment laboratory digital/control dependency and bounded cyber-disruption consequence analysis, SRC-0002-C02–C04, Figure 2, Table 1 and the Pathogen research/impact sections"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0004
        locator: "WHO laboratory material/information/custody/biosecurity lifecycle and system/control context, §§4–8, PDF pp. 32–71"
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0005
        locator: "NIST genomic sample-instrument-pipeline-data-decision and laboratory/system boundary context, IR 8432 §§2–5 and Appendix A"
  - predicate: evidenced-by
    target: SRC-0019
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0019
        locator: "Canadian laboratory material/inventory/containment and information-system governance, CBS §§3–5 and 9–16"
  - predicate: evidenced-by
    target: SRC-0022
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0022
        locator: "NCI biospecimen material/data/custody lifecycle and biobank informatics/storage boundaries, Chapters A–C and J–L"
  - predicate: evidenced-by
    target: SRC-0023
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0023
        locator: "NIH ELN record/instrument/user/authorization/hosting/backup and lifecycle boundaries, SRC-0023-C02–C08"
  - predicate: evidenced-by
    target: SRC-0026
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0026
        locator: "WHO clinical-laboratory specimen identity/quality to result, interpretation, report and decision pathway, total-testing process Chapters 1–7"
  - predicate: evidenced-by
    target: SRC-0008
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0008
        locator: "Primary NHSBT Synnovis-related grouping/screening/crossmatch disruption, specialist response and blood-stock continuity effects, SRC-0008-C03/C04/C08, annual report pp. 21–22, 44, 92, 97 and 104–105"
  - predicate: evidenced-by
    target: SRC-0009
    claim_id: SYN-0023-C01
    evidence:
      - source: SRC-0009
        locator: "Separate NHS England national-issuer account: ransomware, reduced test capacity, >11,000 delays and issuer-reported restoration, SRC-0009-C03/C04"
tags:
  - engineering-biology
  - sequence-screening
  - design-build-test-learn
  - laboratories
  - biobanks
  - cross-domain-transfer
  - incident
  - continuity
---

# Engineering-biology and laboratory transfer/incident reconciliation

## Question, evidence grouping and exclusions

This synthesis tests exactly `SEB-ST`, `SEB-SD`, `SEB-XT`, `LAB-XT` and
`LAB-CI`. It does not fill the missing engineering-biology product/material
disposition or insider/supply-threat evidence, the laboratory insider/hazard
taxonomy, or any safeguard-effectiveness cell.

The U.S. and UK screening instruments are independent official jurisdictional
lineages. NASEM is an independent U.S. expert-consensus lineage and supplies
engineering-biology/DBTL scope, not provider compliance. WHO/NCI/CBS/NIH are
grouped according to their existing derivative/programme relationships. NHSBT
and NHS England are different operational/national issuer roles in one
Synnovis event ecosystem, not two incidents or forensic investigations.

All engineering-biology transfers are presented at safe functional level. The
page contains no sequence/design, concern-category logic, screening threshold,
laboratory parameter, facility topology or actionable bypass/exploit detail.

> **Claim record — SYN-0023-C01 | analytic-judgment**
> **Claim:** The synthesis preserves claim-appropriate independence across
> U.S./UK screening, NASEM, laboratory guidance/research and Synnovis issuer
> roles while grouping derivatives and same-event records without multiplying
> jurisdictions, paths, incidents or effects.
> **Claim status:** active
> **Scope:** SF2/SF3 provenance for the five tested cells; not compliance,
> forensic independence, experimental replication or control effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Direct U.S./UK screening routes:
> [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md), §§III–V,
> printed pp. 5–13 (PDF pp. 6–14), and
> [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> HTML lines 790–1070; biological-AI/DBTL route:
> [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Summary, printed pp. 1–8 (physical pp. 22–29), Chapters 2 and 4–5,
> printed pp. 19–25 and 46–81 (physical pp. 40–46 and 67–102), and
> Appendix A, printed pp. 85–124 (physical pp. 106–145); laboratory
> guidance/research routes: [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§1.1–1.2 and 5–8, printed pp. 2–3 and 19–51 (PDF pp. 22–23 and 39–71),
> [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md), §§3 and
> 5–7, printed pp. 768–777 (PDF pp. 5–14),
> [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> Introduction and §§B.1–B.12.3/C.1–C.6, printed pp. 1–70
> (physical pp. 4–73), [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> §§1.1–1.2.4 and 4.1, printed pp. 2–5 and 52–57 (PDF pp. 34–37 and
> 84–89), [SRC-0023](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md),
> HTML §§II–VI and companion printed pp. 5–13 (physical pp. 8–16), and
> [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md),
> workflow/QMS pp. 11–17, sample management pp. 61–72 and information
> management pp. 182–207; same-event issuer-role routes:
> [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 21–22,
> 44, 92 and 97, and [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> update paragraphs 2–4 and recovery/notification paragraphs (HTML lines
> 190–200). Canonical grouping is retained in `SYN-0002`, `SYN-0010`–
> `SYN-0015`, `SYN-0018` and `INC-0001`.
> **Limits:** Issuers, jurisdictions, methods and event roles are
> direct. Independence is criterion-level, not created by file or agency count.

## `SEB-ST` — joint scope and exclusions

| Required scope | Direct evidence | Reconciled boundary |
| --- | --- | --- |
| Sequence/design services | U.S./UK frameworks define providers, customers/users, orders and synthesis services; NASEM supplies biological design/model tools | a digital design/order is not a physical product or proof of safe use |
| Order screening | both national frameworks define customer/order screening and follow-up/review functions | guidance/framework design is not adoption, test or effectiveness; screening logic is omitted |
| Benchtop synthesis | U.S./UK frameworks directly cover benchtop nucleic-acid synthesis equipment/manufacturers/users | equipment scope is not an inventory, deployment or security validation |
| Engineering-biology/DBTL | NASEM directly describes design→build→test→learn, automation, foundry/cloud-lab and experimental-validation contexts | consensus-report scope is not one deployed foundry or provider rule |
| Exclusions | `WFL-0008` bounds procurement/screening and lacks complete design/use/disposition; `WFL-0011` bounds model/DBTL and lacks complete deployment/retirement | the two models complement but do not merge into one universal safe lifecycle |

> **Claim record — SYN-0023-C02 | analytic-judgment**
> **Claim:** `SEB-ST` passes at SF2: the reconciled corpus jointly defines
> sequence/design services, order screening, benchtop synthesis and
> engineering-biology/DBTL environments and explicitly records procurement,
> deployment, disposition and evidence-state exclusions.
> **Claim status:** active
> **Scope:** Frozen `SEB-ST`; not a complete engineering-biology taxonomy,
> implemented provider/foundry environment, legal equivalence or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYS-0006](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md),
> `SYS-0006-C01/C03`; [WFL-0008](../workflows/wfl-0008-nucleic-acid-procurement-screening-lifecycle.md),
> `WFL-0008-C01/C04/C05`; [WFL-0011](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md),
> `WFL-0011-C01/C04`; [SYS-0011](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md),
> `SYS-0011-C01/C02`; source relations above.
> **Basis / limits:** Every scope literal and exclusion is direct across three
> materially independent issuer roles. Scope does not imply implementation.

## `SEB-SD` — system/dependency map

| Required component/boundary | Located system function | Limit |
| --- | --- | --- |
| Design tools | NASEM biological model/design data/tool environment | no current tool inventory, deployment or validated output |
| Provider interfaces | customer/intermediary/provider order and delivery interfaces in U.S./UK models | no endpoint, protocol, topology or live transaction |
| Screening dependencies | customer/order/equipment screening, reference/update and escalation/review functions | no concern logic, threshold, bypass route or measured performance |
| Human review | follow-up/escalation and reviewer decision state | role/function, not workload, competence or result |
| Instruments/foundries | benchtop equipment plus NASEM automation, physical build/test and foundry/cloud-lab contexts | no organization-specific foundry architecture or validation |
| Identity/update paths | customer/principal-user identity, record/report and equipment/reference-update responsibilities | no universal identity assurance, update deployment or compliance |
| Boundaries | design/order→provider/reviewer/equipment→physical fulfilment plus experimental result→data/model/next-design handoffs | functional map, not deployed trust-boundary validation |

> **Claim record — SYN-0023-C03 | analytic-judgment**
> **Claim:** `SEB-SD` passes at SF2: design tools, provider interfaces,
> screening dependencies, human review, instruments/foundries, identity/update
> paths and their exact functional boundaries are all directly represented
> across independent U.S., UK and NASEM lineages.
> **Claim status:** active
> **Scope:** Frozen `SEB-SD`; not live architecture, operational interface,
> screening performance, IAM validation, compliance or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYS-0006-C01`–`C04`; `SYS-0011-C01`–`C04`;
> `WFL-0008-C02`–`C05`; [AST-0004](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md),
> `AST-0004-C01`–`C05`; `SRC-0011-C02/C04/C05/C07`,
> `SRC-0012-C03`–`C06` and `SRC-0033-C03`–`C05`.
> **Basis / limits:** Every literal class and boundary is located at SF2.
> Missing deployment validation belongs to implementation/assurance, not the
> frozen structural criterion.

## `SEB-XT` — two safe complete directions

| Direction | Complete path | Independent support and boundary |
| --- | --- | --- |
| Digital design/order/control→physical output | design/model output → bounded human/order gate → customer/order screening → follow-up/review/decision → provider product fulfilment → physical synthesis output; authorized benchtop-equipment access remains an intermediate branch, while NASEM separately supplies physical build/test output | NASEM supplies design/build/test context; U.S. and UK independently supply provider procurement/screening/product fulfilment and the separate equipment-access branch. Equipment access alone is not treated as proof of synthesis output. This is an intended/hypothetical safe function, not an observed unsafe event |
| Biological result→digital DBTL decision | physical build/test/experimental result → measurement/data and curation → analysis/model evaluation/learning → human scientific review/refinement → next design/experimental decision | NASEM directly supplies the literal DBTL loop; independent USENIX exercises biological material→digital read/file/software processing but is not a DBTL replication or decision outcome |

No physical product properties, laboratory recipe or screening rule are
retained. The human gate is bounded to represented review/decision functions;
it is not claimed universal or sufficient.

> **Claim record — SYN-0023-C04 | analytic-judgment**
> **Claim:** `SEB-XT` passes at SF2: two safe full paths cover digital
> design/order/control→physical output and biological experimental result→
> digital DBTL decision, with intended, hypothetical, controlled and observed
> states kept distinct.
> **Claim status:** active
> **Scope:** Frozen `SEB-XT`; not autonomous authority, unsafe product,
> incident, reliable screening, experimental success or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `WFL-0008-C02`–`C05`; `RSK-0008-C01`–`C04`;
> `WFL-0011-C01`–`C03`; `SYS-0011-C01/C02`;
> [SYN-0018](syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md),
> `SYN-0018-C04`; `SRC-0014-C02/C08`.
> **Basis / limits:** Both literal directions are complete in the combined
> portfolio and the complete cell has multiple independent lineages. The
> reverse literal rests on NASEM; USENIX independently supports only its
> material/input→digital processing limb, not the DBTL decision.

## `LAB-XT` — cyber/digital and material/custody paths

| Required direction | Full scenario/path | Evidence and limit |
| --- | --- | --- |
| Cyber→containment/sample/result effect | compromised/unavailable digital/control state → monitoring/control or laboratory-system loss → degraded containment/sample handling or test/result availability → laboratory/operational/care response state | `RSK-0001` supplies a bounded HCL containment branch from Crawford with WHO/NIST context; `INC-0001`/`RSK-0013` supply an observed ransomware→laboratory-test availability→service/supply branch. No HCL incident or containment release is inferred |
| Material/custody→LIMS/decision effect | specimen/material identity + custody/quality state → receipt/accession/inventory or LIMS/ELN record → processing/test/result → review/interpretation/report → research, clinical or public-health decision/action | `WFL-0009`/`SYS-0007` reconcile NCI/WHO/CBS/NIH custody/informatics; WHO LQMS and independent NIST/USENIX support specimen/input→digital result/decision boundaries. No universal procedure or validated topology is inferred |

> **Claim record — SYN-0023-C05 | analytic-judgment**
> **Claim:** `LAB-XT` passes at SF2: the reconciled corpus contains complete
> cyber/digital→containment/sample/result and material/custody→LIMS/result/
> decision paths across independent laboratory, clinical and controlled-study
> lineages.
> **Claim status:** active
> **Scope:** Frozen `LAB-XT`; not an observed HCL release, one universal lab
> architecture, patient harm, validated topology or causal effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [RSK-0001](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md),
> `RSK-0001-C01`–`C05`; [RSK-0013](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md),
> `RSK-0013-C01`–`C06`; [WFL-0009](../workflows/wfl-0009-biospecimen-material-data-lifecycle.md),
> `WFL-0009-C01`–`C03`; [SYS-0007](../systems/sys-0007-biobank-informatics-storage-ecosystem.md),
> `SYS-0007-C02/C03/C05`–`C07`; `SRC-0002-C02`–`C04`,
> `SRC-0026-C03`–`C08` and
> `SRC-0014-C02/C08`.
> **Basis / limits:** Both directions and receiving states are explicit at
> SF2. Hypothetical, intended, controlled and observed evidence types remain
> separated.

## `LAB-CI` — primary continuity outcome and corroboration

NHSBT is a directly affected operational participant. It reports disruption
of blood grouping, antibody screening and crossmatching access, increased
O-negative reliance/amber stock pressure and implemented specialist surge/
triage/coordination. NHS England separately reports the 3 June 2024 ransomware
attack, reduced laboratory test capacity, more than 11,000 delayed outpatient/
elective appointments and issuer-reported restoration by December 2024.

These are laboratory continuity, service and material-pressure outcomes. They
do not establish patient injury, exact delay duration, initial access,
vulnerability, actor, complete stolen-data scope or independently accepted
recovery. Different issuer roles corroborate one event, not two incidents.

> **Claim record — SYN-0023-C06 | analytic-judgment**
> **Claim:** `LAB-CI` passes at SF3: a primary operational participant documents
> observed laboratory testing/continuity and blood-supply pressure effects, and
> a materially separate national health issuer corroborates the event and
> general laboratory disruption and separately supplies the ransomware label,
> reduced test capacity, large service-delay count and restoration chronology.
> **Claim status:** active
> **Scope:** Frozen laboratory/biobank `CI` through bounded continuity outcome;
> not a biobank event, confirmed patient injury, forensic attribution, root
> cause, independent recovery acceptance or safeguard effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [INC-0001](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md),
> `INC-0001-C01`–`C05`; `SRC-0008-C03/C04/C08`; `SRC-0009-C03/C04`.
> **Basis / limits:** NHSBT supplies direct participant evidence and NHS England
> separate national issuer context. It corroborates the event and general
> laboratory disruption; the delay count and reported restoration state are
> NHS England-only details, not independently corroborated facts. This is not
> forensic independence or proof of biological injury/effective recovery.

## Non-promotions and strict score decision

`SEB-AS/CT` remain Pass. `SEB-WL` remains Partial because product/material
disposition is absent; `SEB-TV` lacks explicit insider and complete supply-
failure coverage; `SEB-CI/AE` remain Absent; `SEB-GR` still lacks a completed
current U.S. successor/adoption reconciliation. `LAB-ST/AS/WL/SD/CT/GR` remain
Pass. `LAB-TV` lacks explicit laboratory insider and clean SF2 hazard/
vulnerability coverage, and `LAB-AE` lacks a deployed safeguard with scoped
test/drill metric and independent evaluation.

> **Claim record — SYN-0023-C07 | analytic-judgment**
> **Claim:** Only `SEB-ST/SD/XT` and `LAB-XT/CI` change; every other SEB/LAB
> cell and every global gate retains its current exact blocker.
> **Claim status:** active
> **Scope:** Current frozen sufficiency after active `SYN-0022`; not an
> external absence claim or promotion by related vocabulary.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0023-C01`–`C06`; current frozen SEB/LAB rows/source floors
> and `SYN-0001-C38` in [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** Each non-promotion has a missing direct literal or SF3
> effectiveness/current-governance predicate. LAB-CI does not add a new event
> to the already represented global incident corpus.

> **Claim record — SYN-0023-C08 | artifact-observation**
> **Claim:** Independent strict review accepts exactly `SEB-ST`, `SEB-SD`,
> `SEB-XT`, `LAB-XT` and `LAB-CI` Partial→Pass. Totals become 60 Pass, 47
> Partial and 3 Absent = 60/110 (54.5%); SEB becomes 5/10, LAB becomes 8/10
> and critical cells become 55 Pass, 35 Partial and 1 Absent. Dimensions at
> least 9/10 and all global gates remain unchanged.
> **Claim status:** active
> **Scope:** Filesystem after activation of `SYN-0023` and matching checkpoint;
> not 54.5% absolute domain completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0023-C01`–`C07`; frozen criteria/source floors; prior
> `SYN-0001-C38`; independent audits completed 2026-07-12.
> **Basis / limits:** Five critical Partial→Pass changes produce the arithmetic;
> Partial remains zero points and no global gate moves.

## Safety boundary

This page uses only public functional classes and safe causal abstractions. It
omits sequences/designs, screening logic/thresholds, sample/person data,
facility/system topology, endpoints, credentials, assay/lab parameters and
actionable exploit or bypass mechanics.

> **Claim record — SYN-0023-C09 | analytic-judgment**
> **Claim:** The reconciliation is defensive and does not expose operational
> engineering-biology, laboratory or cyber detail or merge intended paths with
> observed incidents.
> **Claim status:** stale
> **Scope:** Local page content; not a downstream-use guarantee for every
> linked external resource.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYN-0023-C01`–`C08`; local page content.
> **Limits:** The page was checked for identity/actionable details;
> class-level public evidence remains useful. This is a local page-content
> assertion, not an externally evidenced decision claim, so it is retained as
> a safety note but is no longer maintained as active evidence.

## Related pages

- [SYS-0006 — synthesis screening systems](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [WFL-0008 — procurement/screening lifecycle](../workflows/wfl-0008-nucleic-acid-procurement-screening-lifecycle.md)
- [WFL-0011 — biological-AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [RSK-0008 — screening/fulfilment risk](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [RSK-0001 — HCL containment disruption](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md)
- [WFL-0009 — biospecimen lifecycle](../workflows/wfl-0009-biospecimen-material-data-lifecycle.md)
- [SYS-0007 — biobank/lab ecosystem](../systems/sys-0007-biobank-informatics-storage-ecosystem.md)
- [RSK-0013 — laboratory result/decision paths](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md)
- [INC-0001 — Synnovis laboratory disruption](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md)
- [SYN-0001 — frozen coverage rubric](syn-0001-coverage-rubric.md)

## Sources

- [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md)
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md)
- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md)
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [SRC-0023](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md)
- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
