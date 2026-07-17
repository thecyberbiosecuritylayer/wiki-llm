---
id: SYN-0001
type: synthesis
title: Cyberbiosecurity coverage rubric v1.0
aliases:
  - 110-cell coverage rubric
  - 90 percent coverage criterion
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-13
review_after: 2026-07-26
source_ids:
  - SRC-0001
  - SRC-0002
  - SRC-0003
  - SRC-0004
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0008
  - SRC-0009
  - SRC-0010
  - SRC-0011
  - SRC-0012
  - SRC-0013
  - SRC-0014
  - SRC-0015
  - SRC-0016
  - SRC-0017
  - SRC-0018
  - SRC-0019
  - SRC-0020
  - SRC-0021
  - SRC-0022
  - SRC-0023
  - SRC-0024
  - SRC-0025
  - SRC-0026
  - SRC-0027
  - SRC-0029
  - SRC-0030
  - SRC-0031
  - SRC-0032
  - SRC-0033
  - SRC-0034
  - SRC-0035
  - SRC-0036
  - SRC-0041
  - SRC-0042
  - SRC-0059
  - SRC-0060
  - SRC-0061
sensitivity: public
dual_use: low
rubric_version: 1.0.0
rubric_frozen: 2026-07-12T02:44:00-07:00
denominator: 110
target_score: 99
minimum_dimension_score: 9
relations: []
tags:
  - coverage
  - methodology
  - evidence-quality
  - quality-assurance
---

# Cyberbiosecurity coverage rubric v1.0

> Frozen binary acceptance rubric for the wiki's **≥90%** goal. It has 11
> dimensions × 10 evidence axes = 110 cells. `Pass` is one point; `Partial` and
> `Absent` are zero. Certification requires at least **99/110**, at least
> **9/10 in every dimension**, every critical cell and every global gate.

## Purpose and anti-gaming rule

This rubric measures whether the wiki can answer coupled cyber-biological
questions with appropriate evidence, not how many pages it contains. Criteria
were frozen as version `1.0.0` before scoring the newly acquired `SRC-0008`.
They cannot be weakened during filling. A future change requires a new version,
written rationale and re-score of the full corpus; the old checkpoint remains.

The ten axes are:

| Code | Axis |
| --- | --- |
| `ST` | scope and terms |
| `AS` | assets and stakeholders |
| `WL` | workflow and lifecycle |
| `SD` | systems, dependencies and trust boundaries |
| `TV` | threats, hazards, techniques, vulnerabilities and exposures |
| `XT` | cross-domain transfer mechanism |
| `CI` | consequences and incidents |
| `CT` | controls and exact-edge interruption |
| `AE` | assurance and effectiveness |
| `GR` | governance and reconciliation |

## Source floors

| Floor | Minimum evidence |
| --- | --- |
| `SF0` | Verifiable editorial/structural property of the wiki; no external factual claim is being smuggled in. |
| `SF1` | At least one direct, claim-appropriate primary, official or normative source with precise locators and explicit scope. |
| `SF2` | At least two materially independent claim-appropriate lineages, one meeting `SF1`; definitions, scope and conflicts are explicitly reconciled. |
| `SF3` | `SF2` plus a direct observed-event, implementation, test or outcome record of the required type and an independent confirmation or evaluation. |

Multiple IDs from one programme, derivative reports, repeated announcements or
news that repeats one record do not create independence. A source can satisfy
many cells if its evidence is directly appropriate; volume alone never does.
`★` marks a critical cell that must pass regardless of total score.

## 1. Foundations — `FND`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `FND-ST` | Canonical operational scope distinguishes biosafety, biosecurity, cybersecurity and cyberbiosecurity, preserves source-specific definitions and reconciles overlaps/conflicts. | SF2 | ★ | **Pass** — `CON-0001`/`QUE-0001` reconcile scholarly framing with direct WHO definitions without claiming universal consensus. |
| `FND-AS` | One canonical map covers biological, digital, physical and human assets plus affected stakeholders across all seven applied-sector dimensions. | SF2 |  | **Pass** — `SYN-0020-C01/C02` reconciles all seven applied-sector canonical maps into one biological/digital/physical/human asset and affected-stakeholder matrix, preserving material/data, actor/affected-party and sector-inventory limits across independent lineages. |
| `FND-WL` | Foundational synthesis defines common lifecycle primitives from at least four sectors and records where they do not transfer. | SF2 |  | **Pass** — `SYN-0020-C03/C04` defines eight common lifecycle primitives across seven sector workflows and explicitly preserves consent/order/custody/release/notification, material/data, authority and incomplete-stage non-transfer boundaries. |
| `FND-SD` | Canonical taxonomy covers data, control, material, custody and decision dependencies/trust boundaries with located examples in at least four sectors. | SF2 |  | **Pass** — `SYN-0003-C01` reconciles all five dependency/boundary mechanisms with located GEN, BMO, LAB and SEB examples across independent lineages. |
| `FND-TV` | Threat, hazard, technique, vulnerability and exposure are distinct and evidence-backed in at least three sectors. | SF2 | ★ | **Pass** — `SYN-0029-C09` reconciles substantive `THR/HAZ/TEC/VUL` pages and typed edges across GEN, AGE and AIB, with actual exposure state kept distinct from generic weakness classes across independent lineages. |
| `FND-XT` | Transfer synthesis covers data, control, custody, decision and material, with complete cyber→bio, bio/input→digital and privacy-without-cyber examples. | SF2 | ★ | **Pass** — `SYN-0003-C01/C05` reconciles all five mechanisms and three direction classes across independent operational, controlled, normative, incident and modeling lineages; historical `C02` is superseded after the primary incident reverse path was added. |
| `FND-CI` | Consequence taxonomy separates potential/observed effects across privacy, safety, quality, validity and resilience, with calibrated primary cases. | SF3 | ★ | **Pass** — `SYN-0022-C01`–`C03` calibrate observed versus potential privacy, safety, quality, validity and resilience effects across operational-event, national-review, controlled-study, benchmark and field-survey lineages, with the missing primary clinical case and other confirmation/outcome limits explicit. |
| `FND-CT` | Canonical control model distinguishes prevent, detect, contain/respond, recover and assure and maps each to exact scenario edges. | SF2 |  | **Pass** — `SYN-0006-C01/C03` defines the canonical functions/evidence ladder and `SYN-0007-C05` maps all five functions, including assurance, to named scenario edges with direct underlying sources and prerequisites/tradeoffs. |
| `FND-AE` | Assurance ladder distinguishes recommended, implemented, tested, effective and independently evaluated and contains empirical positive and null/failure examples. | SF3 | ★ | **Pass** — `SYN-0022-C04/C05` calibrate all required rungs with empirical positive, failure/limit and biological-null examples from distinct lineages while preserving the empty effective-safeguard rung and absent independent replication/effectiveness. |
| `FND-GR` | Comparative method distinguishes law, regulation, standard, guidance and draft and records jurisdiction, force, adoption, exceptions and currency. | SF2 | ★ | **Pass** — `SYN-0020-C05/C06` reconciles independent EU legislative law, U.S. administrative regulation, Canadian standard, global/UK guidance and U.S. draft/profile examples with jurisdiction, force, adoption, exceptions/conflicts and currency separated. |

Baseline score: **1/10**.

## 2. Genomics and omics — `GEN`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `GEN-ST` | Scope defines human/non-human genomics and at least two other-omics classes, exclusions and privacy/security differences. | SF2 | ★ | **Pass** — `AST-0001-C07` reconciles NIST human/non-human genomics and privacy-versus-cyber scope with three DOJ human-omics classes plus clinical/pathogen exclusions across independent NIST and DOJ lineages. |
| `GEN-AS` | Map covers samples, sequences/variants, phenotype, annotations, metadata, consent/provenance, systems, subjects, relatives, researchers, clinicians and non-human stewards. | SF2 | ★ | **Pass** — `SYN-0021-C01/C02` reconciles every literal class across one grouped NIST genomic lineage plus independent NASEM, PATH-SAFE, EHDS/APHL and NHSBT roles, preserving human kin/consent versus non-human stewardship. |
| `GEN-WL` | End-to-end lifecycle traces collection, preparation, generation, analysis, sharing/reuse, retention/disposition and consent/provenance changes. | SF2 | ★ | **Pass** — `SYN-0021-C03` traces every required stage across NIST plus independent PATH-SAFE, NHSBT, USENIX and EHDS roles while limiting disposition to represented data/records and preserving unvalidated universal custody/consent propagation. |
| `GEN-SD` | System map covers instruments, LIMS/storage/cloud/HPC, pipelines, databases, EHR/research interfaces, identities, responsibilities and validated boundaries. | SF2 | ★ | **Pass** — `SYN-0021-C04` reconciles all component/actor literals and narrow APHL validated-interface instances, with independent USENIX controlled boundary evidence explicitly not generalized to whole-topology validation. |
| `GEN-TV` | Corpus contains sector-specific adversarial threat, non-adversarial hazard and vulnerability/exposure classes linked to assets/workflows. | SF2 | ★ | **Pass** — `THR-0001`, `HAZ-0001`, `VUL-0001` and `SYN-0003-C04` link adversarial, non-adversarial and weakness/exposure classes to `AST-0001/WFL-0005/SYS-0003` across independent USENIX and NIST lineages. |
| `GEN-XT` | At least three full RSK cover integrity→decision, disclosure/permitted-processing privacy and biological/sample-input→digital-analysis directions. | SF2 | ★ | **Pass** — `RSK-0003/0004/0005/0009/0010` and `SYN-0003-C03` cover all required directions across independent NIST and USENIX lineages. |
| `GEN-CI` | Primary case or controlled study documents a downstream clinical, research, privacy or biological outcome with independent context. | SF3 | ★ | **Pass** — `SYN-0030-C03` reconciles the primary 23andMe issuer record with the materially independent joint OPC/ICO reconstruction and enforcement: observed unauthorized access/copying and online offering produced a bounded genomic privacy/identity/kinship outcome, not biological or clinical harm. |
| `GEN-CT` | Preventive, detective, response/recovery and assurance controls map to exact genomic lifecycle edges with prerequisites/failure modes/tradeoffs. | SF2 | ★ | **Pass** — `CTL-0002` and `CTL-0007-C03/C04` map all functions to exact genomic forward/reverse edges with prerequisites, failures and tradeoffs across independent NIST and USENIX lineages; implementation/effectiveness remain separate. |
| `GEN-AE` | At least one deployed genomic safeguard has a scoped test metric and independent effectiveness evaluation with limitations. | SF3 |  | Partial — recommended and implemented genomic-integrity controls are represented, but no deployed safeguard yet has a claim-appropriate integrity metric plus independent effectiveness evaluation at SF3. |
| `GEN-GR` | Current genomic/privacy/cyber instruments from at least two jurisdictions, or global plus jurisdictional levels, are reconciled for scope, force, adoption and exceptions. | SF2 | ★ | **Pass** — `SYN-0004-C01`–`C04/C06` reconcile independent current U.S. NIST/DOJ and EU EHDS lineages for scope, force, staged application, adoption-evidence state and exceptions without treating the regimes as compliance equivalents. |

Baseline score: **0/10**.

## 3. Synthesis and engineering biology — `SEB`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `SEB-ST` | Scope jointly defines sequence/design services, order screening, benchtop synthesis and engineering-biology/DBTL environments with exclusions. | SF2 | ★ | **Pass** — `SYN-0023-C02` reconciles independent U.S./UK screening and NASEM design/DBTL lineages across every literal scope class and explicit procurement/deployment/disposition/evidence exclusions. |
| `SEB-AS` | Map covers designs/orders, customer identity, screening records, IP, reagents/material, synthesizers/automation, products and provider/user/public stakeholders. | SF2 | ★ | **Pass** — `AST-0004-C04` reconciles the full procurement asset/stakeholder envelope across independent US and UK official lineages. |
| `SEB-WL` | Safe lifecycle covers design→order→screen→review→synthesis→delivery/use→record/report/disposition. | SF2 | ★ | **Pass** — `SYN-0032-C03` reconciles every literal through `WFL-0014` across independent NASEM design/DBTL, U.S.–UK order/screen/review/fulfilment/record and WHO-bounded use/custody/disposition roles, with analytic bridges and non-universal implementation explicit. |
| `SEB-SD` | System map covers design tools, provider interfaces, screening dependencies, human review, instruments/foundries, identity/update paths and boundaries. | SF2 | ★ | **Pass** — `SYN-0023-C03` locates every required component and functional boundary across independent U.S., UK and NASEM lineages while withholding deployment/IAM/performance validation. |
| `SEB-TV` | Safe threat model covers misuse, design/screening integrity, insider/supply failures and accidental hazards without evasion detail. | SF2 | ★ | **Pass** — `SYN-0032-C04` reconciles `THR-0006/HAZ-0007/VUL-0007` across independent WHO, NASEM, UK and NIST roles, covering every intentional, insider/supply, accidental and deficient-state limb while separating actor, failure, weakness and consequence and withholding evasion detail. |
| `SEB-XT` | At least two safe full paths show digital design/order/control→physical output and biological result→digital DBTL decision. | SF2 | ★ | **Pass** — `SYN-0023-C04` traces both complete safe directions, separates provider-product, equipment-access and NASEM build/test branches, and preserves intended/controlled versus observed states. |
| `SEB-CI` | Primary official/empirical record documents observed or measured screening, product, safety or misuse consequence at safe abstraction. | SF3 | ★ | Partial — NIST directly measures blinded classifications, disagreements and misses and SecureDNA adds a distinct operational-data context, but shared safeguard/authors and developer participation leave SF3 independent confirmation/evaluation unsatisfied (`SYN-0032-C05`). |
| `SEB-CT` | Identity, screening, review, instrument, monitoring, reporting and record controls map to exact lifecycle edges. | SF2 | ★ | **Pass** — `CTL-0006-C04` reconciles independent US/UK identity, screening, review, instrument/monitoring, reporting, record and security controls mapped to exact edges. |
| `SEB-AE` | Screening or synthesis safeguards have measured deployment/test results and independent evaluation, including failure limits. | SF3 |  | Partial — `CTL-0024/SYN-0032-C06` add one bounded test with aggregate metrics, an operational-data complement and explicit failure limits, but no fully independent evaluator, public provider-level replication or causal effectiveness outcome. |
| `SEB-GR` | Current synthesis-screening/engineering-biology instruments from at least two jurisdictions or global+national levels are reconciled for force, scope and adoption. | SF2 | ★ | **Pass** — `SYN-0032-C07` reconciles current UK voluntary guidance with the current bounded HHS award-policy mechanism for force, scope, adoption, duty holders and exclusions while preserving the unverified U.S. successor and absent award/provider compliance. |

Baseline score: **0/10**.

## 4. Laboratories and biobanks — `LAB`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `LAB-ST` | Scope differentiates research, diagnostic, high-containment laboratories and biobanks/repositories and where rules differ. | SF2 | ★ | **Pass** — `SYN-0010-C01/C02` distinguishes all four classes and reconciles purpose, force, applicability and exclusions across independent NCI, WHO/CBS and academic lineages without treating them as equivalent. |
| `LAB-AS` | Map covers specimens/material, strains/cell lines/reagents, metadata, instruments/facility, credentials, workers, donors/patients and public. | SF2 | ★ | **Pass** — `AST-0005-C01/C02` and `SYN-0010-C03` cover every required asset/stakeholder class across independent NCI and WHO/CBS lineages with source-specific boundaries explicit. |
| `LAB-WL` | Lifecycle covers collection/receipt, accession, processing, inventory/storage, use/share/transport, closeout/disposal and incident learning. | SF2 | ★ | **Pass** — `WFL-0009-C01/C04` and `SYN-0010-C04` map material, data/consent and custody/quality lanes through every required stage across independent NCI and WHO/CBS lineages. |
| `LAB-SD` | Map covers LIMS/ELN, instruments/automation, storage/freezers, building/containment, cloud/backup, identity and validated boundaries. | SF2 | ★ | **Pass** — `SYS-0007-C05/C06` and `SYN-0011-C01`–`C04` cover every literal component and validation-aware boundary across one combined NIH/HHS lineage plus independent WHO, Canadian CBS and NIST lineages, without claiming deployment or completed validation. |
| `LAB-TV` | Corpus includes malicious, insider, accidental, environmental, inventory and supply hazards plus specific vulnerabilities/exposures. | SF2 | ★ | **Pass** — `SYN-0031-C03` reconciles malicious, insider, accidental, environmental, inventory and supply classes plus concrete HSE/UKHSA information, configuration, monitoring and containment exposures across materially independent WHO, HSE, CBS/NCI and incident roles. |
| `LAB-XT` | Full scenarios include cyber→containment/sample/result and material/custody→LIMS/decision effects. | SF2 | ★ | **Pass** — `SYN-0023-C05` reconciles complete cyber/digital→containment/sample/result and material/custody→LIMS/result/decision paths across independent laboratory, clinical and controlled-study lineages. |
| `LAB-CI` | Primary case documents laboratory/biobank biological, safety, privacy or continuity outcome with independent corroboration. | SF3 | ★ | **Pass** — `SYN-0023-C06` combines a directly affected NHSBT operational record with a separate NHS England national-issuer account, preserving same-event and NHS-England-only detail limits. |
| `LAB-CT` | Inventory/custody, access, segmentation, monitoring, containment response and recovery controls map to exact edges. | SF2 | ★ | **Pass** — `SYN-0007-C03` explicitly stitches WHO inventory/custody controls to `WFL-0004` storage/transfer edges and independent NIST access/segmentation/monitoring/response/recovery to `RSK-0001`, without claiming HCL validation. |
| `LAB-AE` | At least one laboratory/biobank control has implementation evidence, scoped test/drill metric and independent evaluation. | SF3 |  | Partial — implemented continuity and assurance practices are represented, but no laboratory/biobank safeguard yet combines a scoped test/drill metric with claim-appropriate independent evaluation at SF3. |
| `LAB-GR` | WHO plus current national/accreditation instruments are reconciled for laboratories/biobanks, including adoption and exceptions. | SF2 | ★ | **Pass** — `SYN-0012-C01`–`C05` reconcile WHO, Canadian licence-scoped national requirements, NCI/ISO biobank scope and CAP private accreditation across force, adoption and exceptions, with derivative NCI/ISO content not double-counted. |

Baseline score: **0/10**.

## 5. Biomanufacturing and OT — `BMO`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `BMO-ST` | Scope distinguishes biologics, cell/gene/ATMP and industrial variants plus batch, continuous, centralized and distributed OT contexts. | SF2 | ★ | **Pass** — `SYN-0028-C03` reconciles existing biologics/cell-gene/ATMP and batch/continuous/centralized/distributed contexts with NIST's independent bounded food, pharmaceutical, chemical/biofuel/bioplastic, forest/material and other industrial-biomanufacturing variants. |
| `BMO-AS` | Map covers raw materials/cell banks, recipes/IP, process/quality data, controllers, QMS/release records, product, workforce, patients and supply stakeholders. | SF2 | ★ | **Pass** — `SYN-0016-C02` reconciles every literal asset/stakeholder class across independent Guttieres and ICH Q13 lineages while preserving material/data/record/role non-equivalence. |
| `BMO-WL` | End-to-end material/data/control/quality lineage covers development→raw supply→upstream→downstream→fill/finish→release→distribution. | SF2 | ★ | **Pass** — `SYN-0016-C03` reconciles every required stage and material/data/control/quality state across independent Guttieres and ICH Q13 lineages without claiming one universal process. |
| `BMO-SD` | Architecture covers sensors/actuators, PLC/DCS/SCADA, MES/LIMS/QMS/ERP, vendor/cloud/remote dependencies and boundaries. | SF2 | ★ | Partial — `SYS-0002-C07` reconciles PLC/DCS/SCADA, MES/LIMS/MRP, identity, vendor/cloud/remote and external-connectivity classes, but literal QMS-as-software and ERP coverage remain absent. |
| `BMO-TV` | Model includes cyber manipulation/outage, process/quality hazards, insider/supply risks and concrete vulnerabilities/exposures. | SF2 | ★ | **Pass** — `SYN-0028-C04` reconciles NIST/ICH manipulation, outage and process/quality hazards with independent NCSC/MHRA/FDA insider, supplier and concrete identity, integrity, legacy, vendor/cloud/remote and connectivity exposure classes. |
| `BMO-XT` | At least two full paths cover digital control/data→process/product and material/process-signal→digital release/control decision. | SF2 | ★ | **Pass** — `SYN-0016-C04` traces both complete functional directions across independent Guttieres and ICH Q13 lineages while keeping functional dependency separate from incident/outcome evidence. |
| `BMO-CI` | Primary case or controlled test documents process, product-quality, safety or supply consequence beyond generic IT outage. | SF3 | ★ | **Pass** — `SYN-0028-C05` reconciles Merck's primary 10-K manufacturing→order-backlog/unfulfilled-order→supply consequence with independent New Jersey adjudicative/technical incident and property-damage context; Merck remains the sole consequence measurer and no batch/shortage/patient outcome is inferred. |
| `BMO-CT` | Architecture, access, integrity monitoring, safety/quality gates, response and trusted-recovery controls map to exact process edges. | SF2 | ★ | **Pass** — `SYN-0016-C05` reconciles independent NIST generic-OT and ICH Q13 sector-quality layers across all six exact `RSK-0002` control limbs with prerequisites/tradeoffs and no implementation promotion. |
| `BMO-AE` | Deployed OT/quality safeguard has test/recovery metric and independent evaluation with limitations. | SF3 |  | Absent — no deployed BMO OT/quality safeguard has a claim-appropriate test/recovery metric and independent evaluation represented at SF3. |
| `BMO-GR` | Current GMP/data-integrity/OT-cyber instruments from at least two jurisdictions are reconciled for obligations, exceptions and adoption. | SF2 | ★ | **Pass** — `SYN-0028-C06` reconciles independent U.S. FDA and UK MHRA drug/GxP data-integrity instruments with NIST/NCSC OT-cyber roles across force, scope, exceptions, current presentation and unknown organization-level adoption/effectiveness. |

Baseline score: **0/10**.

## 6. Clinical and public health — `CPH`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `CPH-ST` | Scope distinguishes clinical diagnostics/genomics, laboratory medicine, care delivery and public-health reporting/surveillance. | SF2 | ★ | **Pass** — `SYN-0013-C02` reconciles all four scope classes across independent WHO, NIST, FDA and EHDS lineages without treating laboratory QMS, device, health-data or genomics scope as equivalent. |
| `CPH-AS` | Map covers specimen/patient identity, orders/results, instruments, LIS/EHR/reporting data, clinicians, patients, relatives and populations. | SF2 | ★ | **Pass** — `AST-0006-C01`–`C04` and `SYN-0013-C03` cover every literal asset/stakeholder class across independent WHO, NIST, FDA, EHDS and NHS lineages with source boundaries explicit. |
| `CPH-WL` | Lifecycle covers order→collection→accession→test→interpret→report→notify/action→retain/reanalyse/correct. | SF2 | ★ | **Pass** — `WFL-0010-C01`–`C05` and `SYN-0013-C04` trace every required stage across WHO's total-testing process plus independent current digital/reporting and operational-continuity lineages. |
| `CPH-SD` | Map covers instruments, middleware/LIS, EHR/HIE, reference labs, public-health systems, cloud/identity and validated boundaries. | SF2 | ★ | **Pass** — `SYS-0009-C01`–`C05` and `SYN-0014-C01`–`C03` reconcile every literal class and definition/test/validation/staged-production/monitoring boundary across one APHL package plus independent WHO, EHDS, FDA, NIST and NHS predicates without equating issuer checks to independent effectiveness. |
| `CPH-TV` | Model includes cyber manipulation/outage, identity/specimen mismatch, privacy threats and non-adversarial quality hazards. | SF2 | ★ | **Pass** — `HAZ-0002-C01`–`C04` and `SYN-0013-C05` distinguish all required classes across independent WHO, NIST, NHS, FDA and bounded USENIX evidence without merging hazards, exposure or observed outage. |
| `CPH-XT` | Full paths cover digital→test/report/care/public-health action and specimen/pathogen input→digital interpretation/decision. | SF2 | ★ | **Pass** — `RSK-0013-C01`–`C06` and `SYN-0013-C06` complete both sector-level directions across independent clinical/QMS, controlled-study, health-data and operational lineages; the stricter global observed-decision gate now passes separately through `SYN-0031-C04/C05` and the Immensa primary incident. |
| `CPH-CI` | Primary case documents patient/population outcome or measured near miss, distinguishing service delay from biological harm. | SF3 | ★ | Partial — `SYN-0015-C13` finds a source-reported fatal-outcome account and independent system-class evaluation but no retained claim-appropriate primary case record or measured near miss; service delay, material pressure, report/coding units and biological harm remain distinct. |
| `CPH-CT` | Identity, validation, authorization, result integrity, notification, downtime and recovery controls map to exact workflow edges. | SF2 | ★ | **Pass** — `CTL-0012-C01`–`C05` and `SYN-0013-C07` map every required function to exact testing/reporting edges across independent WHO, FDA, EHDS and NHS lineages while separating design, implementation and effectiveness. |
| `CPH-AE` | Deployed clinical/public-health safeguard or downtime process has a scoped metric and independent outcome evaluation. | SF3 |  | Partial — clinical downtime response and safety practices are represented, but no deployed safeguard or downtime process yet has both a scoped metric and independent outcome evaluation at SF3. |
| `CPH-GR` | Current clinical-lab, health-data, device/diagnostic and reporting instruments from at least two jurisdictions are reconciled. | SF2 | ★ | **Pass** — `SYN-0005-C01`–`C05` reconcile current independent WHO, U.S. FDA and EU EHDS clinical-lab, health-data, device/diagnostic and reporting instruments for scope, force, dates, adoption evidence and exceptions. |

Baseline score: **0/10**.

## 7. Agriculture and environment — `AGE`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `AGE-ST` | Scope defines One Health boundaries across crops, livestock, aquaculture/wildlife and environmental monitoring, with exclusions. | SF2 | ★ | **Pass** — `SYN-0009-C01/C02` reconciles independent U.S. NOHF and joint Quadripartite lineages: plants/agriculture are bounded to crop/plant-health scope, domestic animals/livestock, aquatic animals/aquaculture/wildlife and explicit environmental monitoring are located, and the zoonoses-centred versus non-technical country-adaptable limits remain explicit. |
| `AGE-AS` | Map covers seeds/genomes/herds/pathogens, samples, sensors/equipment, traceability/model data, farmers, veterinarians, regulators and ecosystems. | SF2 | ★ | **Pass** — `SYN-0026-C03` reconciles every literal class across independent AU, PATH-SAFE, EU and U.S. roles; Part 86 directly supplies cattle/bison herd, owners, authorities and herd-unique records without equating herd with flock/group/lot. |
| `AGE-WL` | Lifecycle covers breeding/production, diagnostics/surveillance, treatment/movement, trade/traceability, environmental sampling and disposition. | SF2 | ★ | **Pass** — `SYN-0025-C02` reconciles every literal lifecycle stage across independent AU/PATH-SAFE and EU roles while preserving strategy, implementation, legal-order and object-specific non-equivalence. |
| `AGE-SD` | Map covers farm OT/IoT, veterinary/plant labs, remote sensing, traceability/surveillance platforms and boundaries. | SF2 | ★ | **Pass** — `SYN-0025-C03` reconciles farm OT/IoT, veterinary/plant laboratories, remote sensing, traceability/surveillance platforms and explicit organizational/data/system boundaries across independent AU, PATH-SAFE and EU lineages without claiming a deployed validated topology. |
| `AGE-TV` | Corpus includes adversarial, accidental, ecological, supply and sensor/data-integrity threats plus vulnerabilities. | SF2 | ★ | **Pass** — `SYN-0025-C04` reconciles `THR-0002`, `HAZ-0003/0004` and `VUL-0002` across independent AU, Drape and FBI-advisory roles: accidental, ecological, supply, adversarial, sensor/data-integrity and concrete exposure classes remain distinct and asset/workflow-linked. |
| `AGE-XT` | Full paths cover cyber→animal/plant/ecosystem effects and biological/sensor input→digital control/surveillance decision. | SF2 | ★ | **Pass** — `SYN-0027-C02`–`C05` reconcile one source-reported AAFC cyberattack→barn-temperature-control-loss→chicks-dying path with independent Drape/FBI hostile agriculture context and the independent AU/PATH-SAFE biological/environmental/sensor-input→digital surveillance/decision direction. The anonymous event remains single-source and unconfirmed at SF3. |
| `AGE-CI` | Primary case/experiment documents animal, plant, food, ecosystem or material-economic consequence with independent context. | SF3 | ★ | **Pass** — `INC-0004/SYN-0025-C06` reconcile one direct USDA JBS cattle-slaughter/food-processing-throughput consequence with materially independent FBI incident/attribution context; USDA remains the sole consequence measurement and no animal harm, shortage, price causality or effectiveness is inferred. |
| `AGE-CT` | Biosecurity, cyber, traceability, detection, response and resilience controls map to exact sector edges. | SF2 | ★ | **Pass** — `SYN-0025-C07` reconciles independent EU biosecurity/traceability/detection/response/resilience edges with FBI agriculture cyber continuity/recovery and generic NIST/AU/Drape layers; deployment, trusted restoration and effectiveness remain separate. |
| `AGE-AE` | Deployed safeguard has drill/test/audit metric and independent effectiveness assessment. | SF3 |  | **Pass** — `CTL-0019/SYN-0026-C04` reconcile deployed APHIS animal-disease traceability, four defined TPM exercises and baseline/results with an organizationally independent USDA OIG performance audit of real trace records, including one failed traceback and explicit coverage/method/computer-system limits. |
| `AGE-GR` | Current animal/plant-health, environmental and cyber/data instruments from at least two jurisdictions are reconciled under One Health. | SF2 | ★ | **Pass** — `SYN-0019-C01`–`C03` reconcile materially independent current UK BSS and U.S. NOHF national One Health lineages across animal, plant, environment and cyber/data classes, preserving nonbinding force, all-threat versus zoonoses/public-health scope, adoption/maturity asymmetry and absent technical/effectiveness equivalence. |

Baseline score: **0/10**.

## 8. AI and bioinformatics — `AIB`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `AIB-ST` | Scope distinguishes bioinformatics pipelines, statistical/ML models, generative biological design and clinical/research deployment from generic AI. | SF2 | ★ | **Pass** — `SYN-0018-C02` reconciles the concrete USENIX bioinformatics/research-use pipeline with NASEM's independent biology-specific statistical/predictive, foundation, generative/design and assistant scope plus its explicit generic-AI boundary; deployment is a scope context, not implementation evidence. |
| `AIB-AS` | Map covers datasets/labels, models/code, environments/dependencies, compute, outputs/IP, subjects/relatives, developers, researchers and decision makers. | SF2 | ★ | **Pass** — `AST-0008-C01`–`C04` and `SYN-0018-C03` cover all nine literal classes across independent NASEM and single-programme NIST genomics lineages while preserving inventory, draft/advisory and implementation limits. |
| `AIB-WL` | Lifecycle covers acquisition/labeling→training/analysis→validation→deployment/inference→monitoring/update→retirement with provenance/reproducibility. | SF2 | ★ | **Pass** — `SYN-0029-C03` reconciles every literal phase across independent NASEM and ETSI roles plus bounded direct oncology implementation, without claiming one universal deployment. |
| `AIB-SD` | Map covers packages/containers/notebooks, cloud/HPC, APIs/model registries, databases/instruments and identity boundaries. | SF2 | ★ | **Pass** — `SYN-0029-C04` reconciles notebooks/databases/instruments from `SYS-0011` with packages, containers, cloud/HPC, APIs, registries, identity and deployed boundaries from `SYS-0013` across independent lineages. |
| `AIB-TV` | Corpus covers poisoning/tampering/leakage, software dependencies, bias/drift/error and unsafe automation at defensive abstraction. | SF2 | ★ | **Pass** — `SYN-0029-C05` reconciles `THR-0003/TEC-0002/VUL-0004/HAZ-0005` across independent ETSI and biology-specific NASEM roles, preserving defensive abstraction and instance-status limits. |
| `AIB-XT` | Full paths cover biological data/input→digital output and model/design output→experimental, clinical or agricultural action. | SF2 | ★ | **Pass** — `SYN-0018-C04` traces both complete NASEM biological-AI directions and reconciles them with independent USENIX material/input→digital and AU digital-output→agricultural-action evidence without inferring incident, autonomy or effectiveness. |
| `AIB-CI` | Primary incident or empirical study measures research, privacy, clinical or biological consequence and states model/dataset scope. | SF3 | ★ | **Pass** — `SYN-0029-C06` bounds CASP15's measured molecular-replacement success/failure to research consequence with explicit model/target scope and independent ProteinGym benchmark context. |
| `AIB-CT` | Provenance, access, versioning, reproducibility, monitoring, human review and recovery controls map to exact pipeline/model edges. | SF2 | ★ | **Pass** — `CTL-0016-C01`–`C06` and `SYN-0018-C05` reconcile all seven functions across independent NASEM and NIST lineages; affected-output/dependent-decision recovery is explicitly editorial exact-edge normalization, not reported model-output rollback or effectiveness. |
| `AIB-AE` | Independent benchmark/deployment study tests robustness/effectiveness and reports generalizability and failure limits. | SF3 |  | **Pass** — `SYN-0029-C07` reconciles independent ProteinGym and assessor-led CASP15 biological-model benchmarks with scoped metrics, generalizability strata and positive plus failure/null limits. |
| `AIB-GR` | Current AI, data, genomics/research and medical-device instruments from at least two jurisdictions are reconciled for applicability/status. | SF2 | ★ | **Pass** — `SYN-0029-C08` reconciles current EU AI Act/EHDS, U.S. NIH/FDA and ETSI roles for force, dates, scientific-R&D/device triggers, controlled-data scope, exceptions and unknown adoption. |

Baseline score: **0/10**.

## 9. Threats and incidents — `THI`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `THI-ST` | Wiki consistently distinguishes documented incident, source allegation, theoretical analysis, exercise/simulation and hypothesis, with no fictional `INC`. | SF0 | ★ | **Pass** — all 20 active RSK and seven active INC/review pages explicitly classify observed, source-alleged, controlled, hypothetical, regulatory, aggregate-review and mixed-evidence states; zero fictional INC. |
| `THI-AS` | Cross-sector matrix maps actors/hazards, target assets and affected stakeholders across at least five applied sectors. | SF2 |  | **Pass** — `SYN-0024-C08` maps actor-known/unknown and malicious/non-adversarial hazards to target assets and affected stakeholders across GEN, SEB, LAB, CPH and AIB while retaining hypothetical, controlled, benchmark and observed-state boundaries. |
| `THI-WL` | Incident pages separate event, discovery, disclosure, response and recovery for at least six primary-supported events. | SF3 |  | **Pass** — `SYN-0031-C06` establishes at least seven distinguishable primary-supported events across seven public INC/review pages; counted pages separate event, discovery, disclosure, response and recovery/remediation or mark a state unknown. |
| `THI-SD` | At least four incidents have primary technical support for dependencies/boundaries, with speculation isolated. | SF3 | ★ | **Pass** — `SYN-0030-C14` identifies event-specific primary technical dependencies for Synnovis, the chicken-farm account, Merck and 23andMe, with unknown mechanisms and speculation isolated. |
| `THI-TV` | Canonical `THR`, `HAZ`, `TEC` and `VUL` pages distinguish actor/event, method, weakness and non-adversarial trigger with typed edges. | SF2 | ★ | **Pass** — `SYN-0029-C09` reconciles the four roles and typed edges across GEN, AGE and AIB; the independent AIB graph reproduces the separation beyond the original USENIX lineage. |
| `THI-XT` | Primary incident corpus demonstrates transfer in at least three sectors, including cyber→bio and input/material→digital paths. | SF3 | ★ | **Pass** — `SYN-0031-C04` reconciles four primary-supported forward paths across LAB, AGE and BMO, including cyber→biological/operational paths, with the Immensa primary incident's biological test-input→digital-result→notification/contact-tracing decision path; modelled downstream effects remain explicitly bounded. |
| `THI-CI` | At least six primary-supported incidents from four independent lineages/four sectors include at least two evidenced biological/clinical/product/ecological outcomes. | SF3 | ★ | **Pass** — `SYN-0030-C05` and `SYN-0031-C06` reconcile at least seven distinguishable primary-supported events across LAB, CPH, AGE, BMO and GEN and more than four independent lineages, retaining evidenced patient, animal and processing/product-supply outcomes plus a separate genomic privacy outcome. |
| `THI-CT` | Defensive lessons from primary incidents map controls to exact failed/interrupted edges without turning recommendations into effectiveness. | SF3 | ★ | **Pass** — `SYN-0030-C14` reconciles four distinct primary event/review lesson lineages through `CTL-0004`, `CTL-0014`, `CTL-0020` and `CTL-0022`, mapping continuity, record correction, Merck recovery and genomic-account containment/notification edges without promoting implementation to effectiveness. |
| `THI-AE` | Causality, vector, impact and attribution are graded separately, with counterevidence and at least two independent investigations. | SF3 | ★ | **Pass** — `SYN-0030-C14` retains separate causality, vector, impact and attribution grades and counts two independent investigations: the insurer-retained Kroll work evidenced through bounded court findings and the joint OPC/ICO investigation counted once. Their method and independence limits remain explicit. |
| `THI-GR` | Current reporting, notification, preservation and attribution-governance rules are reconciled across at least two jurisdictions. | SF2 | ★ | **Pass** — `SYN-0030-C06` reconciles current Canadian law and UK regulator guidance for regulator reporting, affected-person notification, breach-record preservation and attribution governance while preserving their different thresholds, timing, force, scope, exceptions and missing detail. |

Baseline score: **1/10**.

## 10. Controls — `CTR`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `CTR-ST` | Canonical taxonomy reconciles functions and recommended/implemented/tested/effective states across at least two independent official frameworks. | SF2 | ★ | **Pass** — `SYN-0006-C01`–`C04` reconcile independent FDA, NIST and WHO official lineages into canonical functions and a recommendation/design→implementation→test→effectiveness→independent-evaluation ladder. |
| `CTR-AS` | Control objectives protect major asset/stakeholder classes across all applied sectors and record safety/privacy tradeoffs. | SF2 |  | **Pass** — `SYN-0024-C02` reconciles named control→asset/stakeholder mappings across all seven applied sectors with safety, privacy, utility and availability tradeoffs explicit. |
| `CTR-WL` | Each applied sector has controls mapped to lifecycle stages rather than generic lists. | SF2 |  | **Pass** — `SYN-0024-C03` maps sector-specific controls to represented lifecycle/scenario edges in GEN, SEB, LAB, BMO, CPH, AGE and AIB without claiming gap-free lifecycles. |
| `CTR-SD` | Controls state prerequisites, dependencies, failure modes and boundary assumptions, with implementation evidence where claimed. | SF2 | ★ | **Pass** — `SYN-0024-C04` reconciles the original public control portfolio, and all 23 active CTL pages preserve explicit prerequisites, dependencies, failure/tradeoff conditions, boundaries and evidence states; implementation remains scoped to the reported institution/programme and edge. |
| `CTR-TV` | Every control relation identifies the exact threat/hazard/vulnerability/precondition and avoids universal mitigation. | SF2 | ★ | **Pass** — all 23 active CTL pages use conditional exact-edge/precondition claims; newer agriculture, Merck, genomic-service and laboratory-result pages preserve source-specific dependencies and no relation asserts universal mitigation. |
| `CTR-XT` | At least ten exact-edge mappings across five sectors cover prevention, detection, containment/response and recovery in both directions. | SF2 | ★ | **Pass** — `CTL-0001/0002/0003/0004/0005/0006/0007` provide more than ten mappings across LAB, GEN, CPH, AGE and SEB, with `CTL-0007` adding material/input→digital direction. |
| `CTR-CI` | At least four primary incidents supply scoped control-failure/recovery lessons with implementation separated from effectiveness. | SF3 | ★ | **Pass** — `SYN-0030-C14` reconciles Synnovis continuity, the national clinical review, Merck vendor/update/manufacturing recovery, and 23andMe authentication/monitoring/notification lessons, keeping required, recommended, implemented and evaluated states separate from effectiveness. |
| `CTR-CT` | Portfolio covers prevent, detect, respond/contain, recover and assure in at least five sectors, with prerequisites/tradeoffs. | SF2 | ★ | **Pass** — `SYN-0007-C06` maps all five functions to named LAB, BMO, GEN, AGE and CPH scenarios through `CTL-0001/0002/0005/0007/0010/0011`, preserving sector prerequisites, failures and tradeoffs. |
| `CTR-AE` | At least six implemented/tested safeguard instances across four sectors and three independent evaluators report metrics/baselines/limits and one null/failure result. | SF3 | ★ | Partial — the current portfolio contains bounded implementation/test evidence and failure limits, but fewer than six claim-appropriate safeguard instances meet the full evaluator/metric floor. |
| `CTR-GR` | Exact versioned mappings to at least three official frameworks/instruments state jurisdiction/scope and reject crosswalk-as-compliance/effectiveness. | SF2 | ★ | **Pass** — `SYN-0007-C07` reconciles exact SP 800-82r3/CSF 1.1/SP 800-53r5, IR 8467 2PD/CSF 2.0/PF 1.0, FDA 2026, WHO 2024 and EHDS 2025/327 versions, jurisdictions, force/scope and non-equivalence limits. |

Baseline score: **0/10**.

## 11. Governance — `GOV`

| Cell | Binary acceptance criterion | Floor | Critical | Current status at latest checkpoint |
| --- | --- | ---: | :---: | --- |
| `GOV-ST` | Corpus distinguishes law, regulation, standard, normative guidance, voluntary profile and draft with publication/adoption/effective/current dates. | SF2 | ★ | **Pass** — `SYN-0008-C01` distinguishes law, administrative regulation, a conditional national standard, normative/voluntary guidance and a voluntary Community Profile in draft state with publication, effect/application, adoption and currentness values. |
| `GOV-AS` | Duty holders, rights holders, regulators, review bodies and affected stakeholders map across global, US, EU, UK and one additional context. | SF2 | ★ | **Pass** — `SYN-0008-C02` maps all five actor classes across global WHO, U.S., EU, UK and Canada and explicitly marks source-specific missing rights/review functions instead of inferring them. |
| `GOV-WL` | Obligations/recommendations trace planning, acquisition, operation, transfer, incident response, correction and disposition. | SF2 |  | **Pass** — `SYN-0024-C05` reconciles every literal stage across independent WHO/NCI and binding DOJ regimes while retaining recommendation, receipt/acquisition and disposition limits. |
| `GOV-SD` | Architecture maps institutional, national, supplier/service and cross-border accountability dependencies. | SF2 |  | **Pass** — `SYN-0004-C05` canonically reconciles all four accountability classes across independent DOJ and EHDS lineages while preserving their different access, infrastructure and actor models. |
| `GOV-TV` | Instruments' risk triggers, covered threats/hazards and review-after-change/incident duties are compared. | SF2 |  | **Pass** — `SYN-0024-C06` compares WHO, NASEM, UK and DOJ triggers/review duties and explicitly preserves absent or non-equivalent incident-review duties. |
| `GOV-XT` | Synthesis allocates responsibility at cyber-biological and cross-border data/material boundaries. | SF2 |  | **Pass** — `SYN-0024-C07` allocates UK digital-order→product/equipment roles and independent DOJ/EHDS cross-border data/material-access roles without conflating force, object or jurisdiction. |
| `GOV-CI` | Primary reporting, enforcement, court, regulator or audit cases show how incident obligations operate in practice. | SF3 | ★ | **Pass** — `SYN-0030-C07` adds an actual Canada–UK regulator/enforcement case applying safeguard, threshold, timing, content, remediation and penalty duties and reconciles it with a separate national patient-safety review and prospective-action record without multiplying the joint investigation. |
| `GOV-CT` | Binding/recommended provisions and exceptions map to exact controls/scenarios without treating crosswalk as compliance. | SF2 | ★ | **Pass** — binding `GOV-0005/CTL-0008/RSK-0011` prohibition/restriction/exception edges and recommended `GOV-0003/CTL-0006/RSK-0008` edges are reconciled across independent DOJ and UK lineages without treating controls, crosswalks or audit design as authorization/compliance/effectiveness. |
| `GOV-AE` | Adoption, audit, enforcement or outcome evidence evaluates implementation in at least two jurisdictions and reports limitations. | SF3 | ★ | **Pass** — narrowly, `SYN-0030-C08` shows one joint investigation evaluating actual implementation on one global platform separately under Canadian PIPEDA and UK GDPR, with jurisdiction-specific findings and explicit company-supplied-information, privileged-record, count-verification and no-effectiveness-comparator limits; it is not two investigations or deployments. |
| `GOV-GR` | Current primary global, US, EU, UK and one additional jurisdiction/region are reconciled for scope, force, adoption, conflicts and gaps. | SF2 | ★ | **Pass** — `SYN-0008-C03` reconciles current primary WHO, U.S., EU, UK and Canadian instruments for scope, force, normative/observed-adoption state, exceptions, conflicts and gaps without globalizing a jurisdiction or crosswalk. |

Baseline score: **0/10**.

## Global certification gates

Every gate is mandatory:

1. **Frozen denominator:** rubric version, cutoff and lineage rules are fixed
   before scoring; criteria are not relaxed during filling.
2. **Numeric threshold:** ≥99/110, ≥9/10 in every dimension and every `★` cell.
3. **Traceability:** every pass points to full-contract claims, exact locators
   and reproducible artifacts; structural/evidence/semantic/temporal-safety lint
   is clean.
4. **Freshness:** no current conclusion relies on stale `review_after` and
   superseded/draft/advisory status remains explicit.
5. **Risk chain:** every applied sector has a full source-backed RSK from asset/
   workflow through transfer/consequence to exact control edges.
6. **Directionality:** corroborated cyber→biological and biological/material/
   input→digital-decision paths exist; privacy-without-cyber remains separate.
7. **Incident:** `THI-CI` passes; hypotheses, exercises, secondary mentions and
   observed incidents are never merged.
8. **Controls:** each applied sector has exact-edge controls and `CTR-AE`
   passes, including negative/failure evidence.
9. **Governance:** `GOV-GR` passes using current primary official texts; no
   jurisdiction is generalized globally.
10. **Independence:** programme duplicates, derivative reports and repeated
    media cannot satisfy `SF2`/`SF3`.
11. **Safety:** no exploit, screening-evasion, re-identification, facility-
    topology or harmful-production detail is required for a pass.
12. **Negative claims:** “no incidents/evidence” requires a documented search
    scope/date and remains absence-of-located-evidence, not evidence of absence.

## Frozen baseline checkpoint — after SRC-0007

> **Claim record — SYN-0001-C01 | artifact-observation**
> **Claim:** Applying rubric v1.0 to the fully linted corpus after `SRC-0007`
> produced 2 Pass, 85 Partial and 23 Absent cells: 2/110 (1.8%), with only
> `FND-ST` and `THI-ST` passing.
> **Claim status:** stale
> **Scope:** Wiki filesystem at lint checkpoint
> `2026-07-12T02:35:48-07:00`; this is not a claim about absolute domain
> completeness outside the rubric.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** all 27 active entity pages and service files present at the
> checkpoint; cell-by-cell tables above. The internal lint transcript is not
> included in the public derivative.
> **Limits:** Statuses were independently rechecked against page claims,
> source lineages and floors. Partial/Absent are both zero. Later transactions
> must add a new checkpoint; they do not rewrite this baseline. This is a
> historical local corpus-accounting checkpoint, not an externally evidenced
> decision-relevant claim, so it is retained for audit history but is no longer
> maintained as active evidence.

| Result | Baseline |
| --- | ---: |
| Pass | 2 |
| Partial | 85 |
| Absent | 23 |
| Score | **2/110 = 1.8%** |
| Dimensions at ≥9/10 | 0/11 |
| Global risk gate | FAIL — five hypothetical, uncorroborated RSK |
| Global incident gate | FAIL — zero primary-supported INC |
| Global control gate | FAIL — no tested/effective risk-reduction safeguard |
| Global governance gate | FAIL — no global/US/EU/UK/additional-jurisdiction reconciliation |
| Directionality gate | FAIL — no corroborated material/input→digital-decision case |
| Structural/current lint and safety discipline | PASS, but not substantive points |

## Checkpoint — after SRC-0008

> **Claim record — SYN-0001-C02 | artifact-observation**
> **Claim:** `SRC-0008` adds one primary-supported responder incident, one
> implemented/real-event-exercised continuity control and one independent
> operational genomics lineage, but no cell reaches its full SF2/SF3 floor;
> the score remains 2/110.
> **Claim status:** active
> **Scope:** Wiki filesystem after the `SRC-0008` transaction; cell criteria
> remain frozen at rubric v1.0.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md);
> [INC-0001](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md);
> [CTL-0004](../controls/ctl-0004-transfusion-service-continuity-response.md);
> [RSK-0006](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md);
> all changed cell criteria in this rubric.
> **Basis / limits:** Six cells move from Absent to Partial, but Partial is
> still zero. The event is one first-party responder account, the response has
> no independent outcome metric and `THI-CI` requires a larger independent
> multi-sector incident corpus.

Changed statuses:

| Cell | Before | After | Why it still does not pass |
| --- | --- | --- | --- |
| `LAB-AE` | Absent | Partial | Real-event laboratory continuity implementation, but no scoped metric or independent evaluation |
| `CPH-AE` | Absent | Partial | Clinical downtime response reported, but no independent patient/outcome evaluation |
| `THI-CI` | Absent | Partial | 1 of required 6 primary incidents; one lineage/sector and no confirmed biological injury |
| `THI-AE` | Absent | Partial | Impact/actor/vector are graded separately in one page; no independent investigation/counterevidence corpus |
| `CTR-CI` | Absent | Partial | 1 of required 4 primary incident-derived control lessons |
| `GOV-AE` | Absent | Partial | One UK institutional audit/assurance record, not two-jurisdiction implementation evidence |

| Result | After SRC-0008 |
| --- | ---: |
| Pass | 2 |
| Partial | 91 |
| Absent | 17 |
| Score | **2/110 = 1.8%** |
| Incident corpus | 1 primary-supported `INC`, below `THI-CI` floor |
| Implemented controls | 1 incident response, bounded first-party effectiveness only |
| Global gates | Still FAIL except structural/traceability/safety |

## Checkpoint — after SRC-0010

> **Claim record — SYN-0001-C04 | artifact-observation**
> **Claim:** `SRC-0010` adds the first substantive agriculture asset, workflow,
> system, hypothetical risk and recommended-control chain, moving five `AGE`
> cells from Absent to Partial; no cell reaches its SF2/SF3 floor and the score
> remains 2/110.
> **Claim status:** active
> **Scope:** Wiki filesystem after the `SRC-0010` transaction; rubric v1.0
> criteria and denominator remain unchanged.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md);
> [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md);
> [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md);
> [SYS-0005](../systems/sys-0005-connected-smart-farm-ecosystem.md);
> [RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md);
> [CTL-0005](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md).
> **Basis / limits:** The source is one US-centered qualitative workshop
> lineage. It supplies no complete One Health lifecycle, observed incident,
> reverse biological/sensor-input path, deployed safeguard, outcome metric or
> current governance instrument.

Changed statuses:

| Cell | Before | After | Why it still does not pass |
| --- | --- | --- | --- |
| `AGE-WL` | Absent | Partial | Only monitoring→production→supply fragment; lifecycle breadth and SF2 absent |
| `AGE-SD` | Absent | Partial | Candidate connected classes/boundaries, not validated architecture or full platform set |
| `AGE-TV` | Absent | Partial | Potential classes only; no canonical hazard/vulnerability corpus or independent lineage |
| `AGE-XT` | Absent | Partial | One hypothetical cyber→production path; reverse path and empirical corroboration absent |
| `AGE-CT` | Absent | Partial | Recommended exact-edge mapping only; no traceability breadth, implementation or SF2 |

| Result | After SRC-0010 |
| --- | ---: |
| Pass | 2 |
| Partial | 96 |
| Absent | 12 |
| Score | **2/110 = 1.8%** |
| Global gates | Still FAIL except structural/traceability/safety |

## Checkpoint — after SRC-0009

> **Claim record — SYN-0001-C03 | artifact-observation**
> **Claim:** `SRC-0009` adds a second official institutional account for the
> Synnovis event, exact attack/publication dates, ransomware classification,
> aggregate appointment delays, source-reported restoration and a separate
> confidentiality-response track, but no frozen cell changes status and the
> score remains 2/110.
> **Claim status:** active
> **Scope:** Wiki filesystem after the `SRC-0009` transaction; criteria and
> source-floor rules remain frozen at rubric v1.0.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> article update and official page metadata;
> [INC-0001](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md);
> [RSK-0006](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md);
> cell criteria and prior checkpoint above.
> **Basis / limits:** The second issuer strengthens event-level support but is
> part of the same NHS response ecosystem and supplies no forensic, clinical-
> outcome or control-effectiveness evaluation. The blood-specific chain remains
> supported only by NHSBT; 1 incident remains below all corpus thresholds.

| Result | After SRC-0009 |
| --- | ---: |
| Pass | 2 |
| Partial | 91 |
| Absent | 17 |
| Score | **2/110 = 1.8%** |
| Cell status changes | None |
| Global gates | Still FAIL except structural/traceability/safety |

> [!NOTE]
> **Checkpoint-order correction**
> The `SRC-0010` block was editorially inserted above the `SRC-0009` block.
> Transaction chronology is `SRC-0008 → SRC-0009 → SRC-0010`; neither historic
> score nor claim content is changed by the display-order defect.

## Checkpoint — after SRC-0011

> **Claim record — SYN-0001-C05 | artifact-observation**
> **Claim:** `SRC-0011` adds the first official synthesis-procurement screening
> governance, asset, workflow, system, hypothetical-risk and exact-edge control
> chain, moving five `SEB` cells from Absent to Partial; no SF2/SF3 cell passes
> and the score remains 2/110.
> **Claim status:** active
> **Scope:** Wiki filesystem after the `SRC-0011` transaction; current US status
> after later executive action remains deliberately unreconciled.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md);
> [GOV-0002](../governance/gov-0002-us-federally-funded-nucleic-acid-screening-2024.md);
> [AST-0004](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md);
> [WFL-0008](../workflows/wfl-0008-nucleic-acid-procurement-screening-lifecycle.md);
> [SYS-0006](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md);
> [RSK-0008](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md);
> [CTL-0006](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md).
> **Basis / limits:** This is one US normative lineage. It supplies no current-
> status reconciliation, DBTL reverse path, implementation, benchmark,
> incident, audit or independent effectiveness evidence.

Changed statuses:

| Cell | Before | After | Why it still does not pass |
| --- | --- | --- | --- |
| `SEB-AS` | Absent | Partial | Bounded procurement asset map; one lineage and incomplete DBTL/material scope |
| `SEB-WL` | Absent | Partial | Procurement/screening segment; design/use/disposition and SF2 absent |
| `SEB-SD` | Absent | Partial | Functional provider/screening/equipment map; no deployment validation or SF2 |
| `SEB-XT` | Absent | Partial | One hypothetical digital decision→physical fulfillment path; reverse path absent |
| `SEB-CT` | Absent | Partial | Exact-edge official criteria, but one lineage and no implementation/evaluation |

| Result | After SRC-0011 |
| --- | ---: |
| Pass | 2 |
| Partial | 101 |
| Absent | 7 |
| Score | **2/110 = 1.8%** |
| Global gates | Still FAIL except structural/traceability/safety |

## Checkpoint — after SRC-0012

> **Claim record — SYN-0001-C06 | artifact-observation**
> **Claim:** `SRC-0012` adds an independent current UK official guidance
> lineage and explicit US–UK reconciliation; `SEB-AS` and `SEB-CT` now meet
> their complete SF2 criteria, raising the score to 4/110.
> **Claim status:** active
> **Scope:** Wiki filesystem after the `SRC-0012` transaction; this does not
> resolve current US force, adoption, implementation or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md);
> [GOV-0003](../governance/gov-0003-uk-synthetic-nucleic-acid-screening-2024.md);
> [SYN-0002](syn-0002-us-uk-nucleic-acid-screening-comparison.md);
> `AST-0004-C04`; `CTL-0006-C04`; frozen cell criteria above.
> **Basis / limits:** The two independent issuers jointly cover all required
> procurement asset/stakeholder and exact-edge normative control functions.
> Lifecycle, system, threat, transfer, incident, assurance and current-
> governance criteria remain incomplete.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `SEB-AS` | Partial | **Pass** | Full procurement asset/stakeholder envelope across independent US/UK official lineages, with scope differences reconciled |
| `SEB-CT` | Partial | **Pass** | Identity, screening, review, instrument/monitoring, reporting, records and security mapped to exact edges across both lineages |

| Result | After SRC-0012 |
| --- | ---: |
| Pass | 4 |
| Partial | 99 |
| Absent | 7 |
| Score | **4/110 = 3.6%** |
| Critical cells newly passed | `SEB-AS`, `SEB-CT` |
| Global gates | Still FAIL except structural/traceability/safety |

## Checkpoint — after SRC-0013

> **Claim record — SYN-0001-C07 | artifact-observation**
> **Claim:** `SRC-0013` directly resolves that EO 14292 ordered revision or
> replacement of the 2024 US framework, but no rubric cell changes status
> because the completed successor, agency implementation and adoption evidence
> required for `SEB-GR` remain unverified.
> **Claim status:** active
> **Scope:** Wiki filesystem after the `SRC-0013` transaction; deadline passage
> and bounded search non-retrieval are not completion or absence evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0013](../sources/src-0013-us-eo-14292-biological-research-2025.md),
> §4(b); [GOV-0004](../governance/gov-0004-us-eo-14292-biological-research-2025.md);
> `GOV-0002-C06`; `SYN-0002-C05/C06`; frozen `SEB-GR` criterion above.
> **Basis / limits:** The order is direct current-status evidence for the
> revision direction, but it is neither the updated framework nor an agency
> implementation/adoption record. All other cell criteria are unchanged.

Changed statuses: **none**.

| Result | After SRC-0013 |
| --- | ---: |
| Pass | 4 |
| Partial | 99 |
| Absent | 7 |
| Score | **4/110 = 3.6%** |
| Strengthened but still Partial | `SEB-GR` |
| Global gates | Still FAIL except structural/traceability/safety |

## Checkpoint — after SRC-0014

> **Claim record — SYN-0001-C08 | artifact-observation**
> **Claim:** `SRC-0014` and its canonical reverse-path graph close seven frozen
> SF2 cells—`FND-SD`, `FND-XT`, `GEN-TV`, `GEN-XT`, `GEN-CT`, `CTR-TV` and
> `CTR-XT`—raising the score from 4/110 to 11/110 without counting the
> controlled study as an incident or its recommendations as implemented/
> effective controls.
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0014` transaction; no
> other cell or global gate changes status.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md);
> [SYN-0003](syn-0003-cross-domain-transfer-directions.md);
> `THR-0001`, `HAZ-0001`, `TEC-0001`, `VUL-0001`, `RSK-0009/0010`,
> `CTL-0007`; frozen criteria and source floors above.
> **Basis / limits:** Independent USENIX and NIST lineages close the genomic
> threat/transfer/control floors; broader corpus lineages close the foundational
> boundary/direction and five-sector control-portfolio criteria. The exact
> four-role `THI-TV` taxonomy remains one lineage and Partial. The PoC is not a
> field incident, cross-sample reads are not downstream harm, and all new
> control implementation/effectiveness states are unknown. The stricter global
> reverse path still requires a corroborated biological/material/input→digital
> **decision** outcome.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `FND-SD` | Partial | **Pass** | Canonical data/control/material/custody/decision boundary map with located examples in four sectors and multiple independent lineages |
| `FND-XT` | Partial | **Pass** | Canonical five-mechanism map plus cyber→bio, material/input→digital and privacy-without-cyber examples across independent evidence classes |
| `GEN-TV` | Partial | **Pass** | Linked adversarial threat, non-adversarial hazard and version-bounded weakness/exposure corpus with NIST reconciliation |
| `GEN-XT` | Partial | **Pass** | Five full RSK cover required directions across NIST and USENIX lineages |
| `GEN-CT` | Partial | **Pass** | Prevent/detect/contain-recover/assure mapped to exact genomic edges with prerequisites, failures and tradeoffs across two lineages |
| `CTR-TV` | Partial | **Pass** | Conditional control relations identify exact scenario/HAZ/VUL/precondition edges and reject universal mitigation |
| `CTR-XT` | Partial | **Pass** | More than ten exact-edge mappings across five sectors and both transfer directions |

| Result | After SRC-0014 |
| --- | ---: |
| Pass | 11 |
| Partial | 92 |
| Absent | 7 |
| Score | **11/110 = 10.0%** |
| Critical cells newly passed | `FND-XT`, `GEN-TV`, `GEN-XT`, `GEN-CT`, `CTR-TV`, `CTR-XT` |
| Global gates | Still FAIL except structural/traceability/safety |

## Checkpoint — after SRC-0015

> **Claim record — SYN-0001-C09 | artifact-observation**
> **Claim:** `SRC-0015` adds a current corrected binding U.S. human-omics/
> health-data access regime, a two-branch regulatory risk path and exact
> transaction/control/assurance mappings; independent binary review closes
> `GEN-ST` and `GOV-CT`, raising the score from 11/110 to 13/110.
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0015` transaction;
> one integrated DOJ/CISA rulemaking lineage does not supply implementation,
> incident or effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md);
> [GOV-0005](../governance/gov-0005-us-data-security-program-2025.md);
> [RSK-0011](../risk-scenarios/rsk-0011-covered-omics-regulated-access.md);
> [CTL-0008](../controls/ctl-0008-restricted-data-transaction-controls.md);
> `AST-0001-C07`, `WFL-0005-C09`, `SYS-0003-C07`, `CTL-0006-C04`,
> `GOV-0003-C03/C04`, `SYN-0002-C03`; frozen criteria above.
> **Basis / limits:** NIST and DOJ independently close the frozen genomic scope
> elements in `AST-0001-C07`. `GOV-0005-C03`, `RSK-0011-C03` and
> `CTL-0008-C01/C02` preserve DOJ's prohibition/restriction/exception/license
> predicates; `GOV-0003-C03/C04`, `CTL-0006-C04` and `SYN-0002-C03` preserve
> the independent recommended UK limb and reject legal/compliance/effectiveness
> equivalence. The DOJ rule/correction/CISA set remains one U.S.
> lineage; legal duties and audit design are not implementation, incidents or
> measured outcomes.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `GEN-ST` | Partial | **Pass** | Human/non-human genomics, three other human-omics, exclusions and privacy/cyber differences explicitly reconciled across independent NIST/DOJ lineages in `AST-0001-C07` |
| `GOV-CT` | Partial | **Pass** | Binding DOJ and recommended UK provisions/exceptions map to exact scenario/control edges; `SYN-0002-C03`, `CTL-0006-C04` and DOJ claims reject compliance/effectiveness equivalence |

| Result | After SRC-0015 |
| --- | ---: |
| Pass | 13 |
| Partial | 90 |
| Absent | 7 |
| Score | **13/110 = 11.8%** |
| Critical cells newly passed | `GEN-ST`, `GOV-CT` |
| Strengthened but still Partial | `GEN-GR`, `CPH-GR`, `GOV-ST/AS/WL/SD/TV/XT/GR` |
| Global gates | Still FAIL except structural/traceability/safety |

## Checkpoint — after SRC-0016

> **Claim record — SYN-0001-C10 | artifact-observation**
> **Claim:** `SRC-0016` adds the current in-force but staged EU EHDS legal,
> control and accountability design; independent binary review closes
> `GEN-GR` and `GOV-SD`, raising the score from 13/110 to 15/110.
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0016` transaction;
> normative design, staging and one Board implementing act do not establish
> Member State deployment, product conformity, audit outcome or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md);
> [GOV-0006](../governance/gov-0006-eu-ehds-regulation-2025.md);
> [CTL-0009](../controls/ctl-0009-ehds-health-data-and-ehr-safeguards.md);
> [SYN-0004](syn-0004-us-eu-human-omics-health-data-governance.md);
> `AST-0001-C08`, `WFL-0005-C10`, `SYS-0003-C08`, `RSK-0005-C05`;
> frozen criteria above.
> **Basis / limits:** Independent U.S. NIST/DOJ and EU EHDS lineages satisfy
> the genomic-governance floor because `SYN-0004-C01`–`C04/C06` preserve
> scope, force, dates, missing adoption evidence and exceptions. `GOV-0006-C03`
> and `SYN-0004-C05` map institutional, national, supplier/service and cross-
> border accountability classes. No additional cell meets its full contract;
> implementation, incident, test and outcome evidence remain absent.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `GEN-GR` | Partial | **Pass** | Current U.S. NIST/DOJ and EU EHDS scope, force, staged application/adoption state and exceptions are explicitly reconciled in `SYN-0004-C01`–`C04/C06` |
| `GOV-SD` | Partial | **Pass** | `GOV-0006-C03` and `SYN-0004-C05` map institutional, national, supplier/service and cross-border dependencies across independent DOJ/EHDS lineages |

| Result | After SRC-0016 |
| --- | ---: |
| Pass | 15 |
| Partial | 88 |
| Absent | 7 |
| Score | **15/110 = 13.6%** |
| Critical cells newly passed | `GEN-GR` |
| Strengthened but still Partial | `GEN-AS/WL/SD`, `CPH-ST/AS/WL/SD/CT/GR`, `GOV-AS/WL/TV/XT/GR` |
| Global gates | Still FAIL except structural/traceability/safety |

## Checkpoint — after SRC-0017

> **Claim record — SYN-0001-C11 | artifact-observation**
> **Claim:** `SRC-0017` adds current FDA medical-device cybersecurity scope,
> governance, a safe clinical-function risk path and exact lifecycle controls;
> independent binary review closes `CPH-GR` and `CTR-ST`, raising the score
> from 15/110 to 17/110.
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0017` transaction; FDA
> guidance, cited duties and requested test evidence are not product
> implementation, test results, compliance or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md);
> [GOV-0007](../governance/gov-0007-us-fda-medical-device-cybersecurity-2026.md);
> [RSK-0012](../risk-scenarios/rsk-0012-medical-device-cyber-disruption-care-harm.md);
> [CTL-0010](../controls/ctl-0010-medical-device-cybersecurity-lifecycle-controls.md);
> [SYN-0005](syn-0005-global-us-eu-clinical-health-governance.md);
> [SYN-0006](syn-0006-official-control-function-state-taxonomy.md);
> frozen criteria above.
> **Basis / limits:** `SYN-0005-C01`–`C05` preserve WHO/FDA/EHDS scope,
> force, dates, missing adoption evidence and exceptions across global, U.S.
> and EU levels. `SYN-0006-C01`–`C04` preserve FDA/NIST/WHO function names
> while defining the full evidence-state ladder. `RSK-0012` remains
> hypothetical and FDA-only; no incident, patient outcome or higher assurance
> cell is promoted.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `CPH-GR` | Partial | **Pass** | Current WHO, U.S. FDA and EU EHDS instruments cover and distinguish clinical-lab, health-data, device/diagnostic and reporting scopes with force/date/adoption/exception reconciliation in `SYN-0005-C01`–`C05` |
| `CTR-ST` | Partial | **Pass** | Independent FDA, NIST and WHO functions plus bounded EHDS/NHSBT state comparators are reconciled into the canonical taxonomy and evidence ladder in `SYN-0006-C01`–`C04` |

| Result | After SRC-0017 |
| --- | ---: |
| Pass | 17 |
| Partial | 86 |
| Absent | 7 |
| Score | **17/110 = 15.5%** |
| Critical cells newly passed | `CPH-GR`, `CTR-ST` |
| Strengthened but still Partial | `CPH-ST/AS/WL/SD/TV/XT/CT`, `CTR-AS/WL/SD/CT/GR`, `GOV-ST/WL/TV/GR` |
| Global gates | Still FAIL except structural/traceability/safety |

## Checkpoint — after SRC-0018

> **Claim record — SYN-0001-C12 | artifact-observation**
> **Claim:** `SRC-0018` adds current generic OT architecture, risk, control,
> recovery, assurance and tailoring guidance plus bounded LAB/BMO/AGE mappings;
> independent binary review closes `FND-CT`, `LAB-CT`, `CTR-CT` and `CTR-GR`,
> raising the score from 17/110 to 21/110.
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0018` transaction; general
> OT guidance is not sector architecture, custody, GMP/quality governance,
> implementation, incident, test or effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md);
> [GOV-0008](../governance/gov-0008-nist-sp-800-82r3-ot-security-2023.md);
> [CTL-0011](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md);
> [SYN-0007](syn-0007-ot-applicability-cyberbio-sectors.md);
> `SYS-0001-C06`, `RSK-0001-C05`, `CTL-0001-C06`, `SYS-0002-C04`,
> `RSK-0002-C04`, `SYS-0005-C03`, `RSK-0007-C05`, `CTL-0005-C04`;
> frozen criteria above.
> **Basis / limits:** `SYN-0007-C03` supplies the mandatory WHO custody/NIST
> technical two-limb laboratory stitch. `C05` maps every canonical function to
> named edges, `C06` demonstrates five-sector portfolio breadth and `C07`
> preserves exact versions/jurisdictions/modalities. `BMO-CT` remains Partial
> because GMP/QMS/release/disposition gates are still absent; no other sector,
> incident or assurance cell is promoted.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `FND-CT` | Partial | **Pass** | Canonical functions/evidence states in `SYN-0006` plus direct-source named-edge matrix, including assurance, in `SYN-0007-C05` |
| `LAB-CT` | Partial | **Pass** | WHO custody/inventory mapped to `WFL-0004` plus independent NIST technical controls mapped to `RSK-0001` in `SYN-0007-C03` |
| `CTR-CT` | Partial | **Pass** | All five functions across LAB/BMO/GEN/AGE/CPH with named scenarios, prerequisites and tradeoffs in `SYN-0007-C06` |
| `CTR-GR` | Partial | **Pass** | Exact version/jurisdiction/force/scope mapping across five official frameworks/instruments with non-equivalence limits in `SYN-0007-C07` |

| Result | After SRC-0018 |
| --- | ---: |
| Pass | 21 |
| Partial | 82 |
| Absent | 7 |
| Score | **21/110 = 19.1%** |
| Critical cells newly passed | `LAB-CT`, `CTR-CT`, `CTR-GR` |
| Strengthened but still Partial | `LAB-SD/TV`, `BMO-SD/TV/CT`, `AGE-SD/TV/CT`, `CTR-AS/WL/SD`, `GOV-ST/WL/TV/GR` |
| Global gates | Still FAIL except structural/traceability/safety; `CTR-AE` keeps the control gate failed |

## Checkpoint — after SRC-0019

> **Claim record — SYN-0001-C13 | artifact-observation**
> **Claim:** `SRC-0019` adds the current Canadian national biosafety standard,
> scoped licence/permit force, actor/review architecture and an additional
> primary jurisdiction; independent binary review of the canonical five-context
> synthesis closes `GOV-ST`, `GOV-AS` and `GOV-GR`, raising the score from
> 21/110 to 24/110 (21.8%).
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0019` transaction; CBS
> mandate is not facility implementation, current-law codification, biobank
> accreditation, compliance or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md);
> [GOV-0009](../governance/gov-0009-canadian-biosafety-standard-third-edition.md);
> [SYN-0008](syn-0008-global-us-eu-uk-canada-governance-reconciliation.md);
> `SYN-0008-C01`–`C04`; frozen criteria above; independent binary review
> completed 2026-07-12.
> **Basis / limits:** The modality/date, five-context actor and current
> scope/force/adoption/conflict/gap matrices meet the literal SF2 contracts.
> `LAB-GR` lacks biobank/accreditation reconciliation, and no implementation,
> audit, enforcement or outcome evidence is promoted.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `GOV-ST` | Partial | **Pass** | Complete class/status/date/force matrix in `SYN-0008-C01`, with acceptance resting on fully ingested EHDS law-form, DOJ regulation, CBS standard, WHO guidance and NIST voluntary-draft lineages |
| `GOV-AS` | Partial | **Pass** | Five actor classes across global/US/EU/UK/Canada with explicit non-establishment markers in `SYN-0008-C02` |
| `GOV-GR` | Partial | **Pass** | Current five-context scope/force/adoption/exception/conflict/gap reconciliation in `SYN-0008-C03` |

| Result | After SRC-0019 |
| --- | ---: |
| Pass | 24 |
| Partial | 79 |
| Absent | 7 |
| Score | **24/110 = 21.8%** |
| Critical cells newly passed | `GOV-ST`, `GOV-AS`, `GOV-GR` |
| Strengthened but still Partial | `LAB-GR`, `GOV-WL/TV/XT/AE` |
| Global governance gate | **PASS** — `GOV-GR` uses current primary official global/US/EU/UK/Canada texts |
| Other global gates | Still FAIL except structural/traceability/safety |

## Checkpoint — after SRC-0020

> **Claim record — SYN-0001-C14 | artifact-observation**
> **Claim:** `SRC-0020` adds an official current U.S. One Health coordination
> framework and moves `AGE-GR` from Absent to Partial, but independent strict
> review accepts no new Pass; the score remains 24/110 (21.8%).
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0020` transaction; policy
> adoption is not implementation, a complete agriculture architecture/
> lifecycle, incident evidence, tested assurance or cross-jurisdiction
> reconciliation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0020](../sources/src-0020-us-national-one-health-framework-2025-2029.md);
> [GOV-0010](../governance/gov-0010-us-national-one-health-framework-2025-2029.md);
> `SRC-0020-C01`–`C10`, `GOV-0010-C01`–`C06`; frozen AGE criteria above;
> independent strict review completed 2026-07-12.
> **Basis / limits:** One coordinated U.S. policy lineage strengthens scope,
> actors, programme, surveillance/laboratory and governance context but cannot
> satisfy SF2/SF3 or the two-jurisdiction `AGE-GR` contract.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `AGE-GR` | Absent | Partial | Current U.S. One Health policy/coordination lineage with explicit zoonoses, implementation and evidence-state limits; second jurisdiction and cyber/data reconciliation remain absent |

| Result | After SRC-0020 |
| --- | ---: |
| Pass | 24 |
| Partial | 80 |
| Absent | 6 |
| Score | **24/110 = 21.8%** |
| Critical cells newly passed | None |
| Strengthened but still Partial | `AGE-ST/AS/WL/SD/TV/XT/CT/GR` |
| Still Absent | `AGE-CI`, `AGE-AE` |
| Global gates | Unchanged; governance/structural/traceability/safety pass, other gates fail |

## Checkpoint — after SRC-0021

> **Claim record — SYN-0001-C15 | artifact-observation**
> **Claim:** `SRC-0021` adds a complete current-presented Quadripartite national
> implementation guide and an explicit global/U.S. scope reconciliation;
> independent strict review accepts only `AGE-ST`, raising the score from
> 24/110 to 25/110 (22.7%).
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0021` transaction;
> programme scope/guidance is not agricultural asset/lifecycle/architecture,
> incident, exact-edge control, effectiveness or second-jurisdiction evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-09-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0021](../sources/src-0021-quadripartite-one-health-jpa-national-guide.md);
> [GOV-0011](../governance/gov-0011-quadripartite-one-health-jpa-national-guide.md);
> [SYN-0009](syn-0009-global-us-one-health-scope-reconciliation.md);
> `SRC-0021-C01`–`C10`, `GOV-0011-C01`–`C06`, `SYN-0009-C01`–`C04`;
> frozen AGE criteria above; independent strict review completed 2026-07-12.
> **Basis / limits:** The complete `AGE-ST` criterion is reconciled across two
> independent official lineages, although not every individual limb is
> duplicated. All operational, SF3 and two-jurisdiction gaps remain explicit.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `AGE-ST` | Partial | **Pass** | `SYN-0009` explicitly reconciles crop/plant-health, livestock, aquaculture/wildlife, environmental-monitoring and exclusion limbs across independent U.S. and Quadripartite lineages without treating scope as implementation |

| Result | After SRC-0021 |
| --- | ---: |
| Pass | 25 |
| Partial | 79 |
| Absent | 6 |
| Score | **25/110 = 22.7%** |
| Critical cells newly passed | `AGE-ST` |
| Strengthened but still Partial | `AGE-AS/WL/SD/TV/XT/CT/GR` |
| Still Absent | `AGE-CI`, `AGE-AE` |
| Global gates | Unchanged; governance/structural/traceability/safety pass, other gates fail |

## Checkpoint — after SRC-0022

> **Claim record — SYN-0001-C16 | artifact-observation**
> **Claim:** `SRC-0022` adds the current NCI Fourth Edition human-research
> biospecimen-resource guidance plus explicit laboratory/biobank scope, asset
> and lifecycle reconciliation; independent strict review accepts exactly
> `LAB-ST`, `LAB-AS` and `LAB-WL`, raising the score from 25/110 to 28/110
> (25.5%).
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0022` transaction;
> voluntary guidance and prescribed QMS/informatics design are not diagnostic/
> HCL/accreditation law, facility implementation, incident evidence or control
> effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md);
> [GOV-0012](../governance/gov-0012-nci-best-practices-biospecimen-resources-2026.md);
> [AST-0005](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md);
> [WFL-0009](../workflows/wfl-0009-biospecimen-material-data-lifecycle.md);
> [SYS-0007](../systems/sys-0007-biobank-informatics-storage-ecosystem.md);
> [SYN-0010](syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md);
> `SRC-0022-C01`–`C12`, `GOV-0012-C01`–`C06`, `AST-0005-C01`–`C04`,
> `WFL-0009-C01`–`C04`, `SYS-0007-C01`–`C04`, `SYN-0010-C01`–`C06`;
> frozen LAB criteria above; independent strict review completed 2026-07-12.
> **Basis / limits:** Complete literal SF2 criteria are met for scope, classes
> and lifecycle. Missing ELN, scenarios, primary outcome, completed assurance
> and current accreditation remain explicit and receive no point.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `LAB-ST` | Partial | **Pass** | `SYN-0010-C01/C02` distinguishes research, diagnostic, HCL and biobank/repository classes and reconciles their rules and exclusions across independent lineages |
| `LAB-AS` | Partial | **Pass** | `AST-0005-C01/C02` and `SYN-0010-C03` cover specimens/material, strains/cells/reagents, metadata/consent/provenance, instruments/facility, identities, workers, donors/patients and public |
| `LAB-WL` | Partial | **Pass** | `WFL-0009-C01/C04` and `SYN-0010-C04` cover receipt/accession, processing, inventory/storage, use/share/transport, closeout/disposal and incident learning across material, data and custody lanes |

| Result | After SRC-0022 |
| --- | ---: |
| Pass | 28 |
| Partial | 76 |
| Absent | 6 |
| Score | **28/110 = 25.5%** |
| Critical cells newly passed | `LAB-ST`, `LAB-AS`, `LAB-WL` |
| Laboratories and biobanks | **4/10** |
| Strengthened but still Partial | `LAB-SD/TV/XT/CI/AE/GR` |
| Existing Pass unchanged | `LAB-CT` |
| Global gates | Unchanged; governance/structural/traceability/safety pass, other gates fail |

## Checkpoint — after SRC-0023

> **Claim record — SYN-0001-C17 | artifact-observation**
> **Claim:** `SRC-0023` adds a literal NIH IRP electronic-laboratory-notebook
> system and explicit instrument/record, identity/custody, storage/cloud/local
> and validation/authorization boundaries; independent strict review accepts
> exactly `LAB-SD`, raising the score from 28/110 to 29/110 (26.4%).
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0023` transaction;
> NIH/NCI count as one lineage, internal requirements are not deployment,
> completed validation, incident, effectiveness or accreditation evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0023](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md);
> [GOV-0013](../governance/gov-0013-nih-intramural-electronic-laboratory-notebook-policy.md);
> [SYS-0007](../systems/sys-0007-biobank-informatics-storage-ecosystem.md);
> [SYN-0011](syn-0011-laboratory-biobank-system-boundary-reconciliation.md);
> `SRC-0023-C01`–`C11`, `GOV-0013-C01`–`C06`, `SYS-0007-C05`–`C07`,
> `SYN-0011-C01`–`C06`; frozen LAB criteria above; independent artifact,
> content, locator, lineage and binary-score review completed 2026-07-12.
> **Basis / limits:** Complete criterion-level SF2 is satisfied even though
> literal ELN evidence is one NIH lineage and not every limb is independently
> duplicated. Stale platform forecasts and every implementation/SF3 predicate
> remain excluded.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `LAB-SD` | Partial | **Pass** | `SYS-0007-C05/C06` and `SYN-0011-C01`–`C04` directly reconcile LIMS, ELN, instruments/automation, storage/freezers, building/containment, cloud/backup, identity and validation-aware boundaries across materially independent lineages |

| Result | After SRC-0023 |
| --- | ---: |
| Pass | 29 |
| Partial | 75 |
| Absent | 6 |
| Score | **29/110 = 26.4%** |
| Critical cells newly passed | `LAB-SD` |
| Laboratories and biobanks | **5/10** |
| Existing Pass unchanged | `LAB-ST/AS/WL/CT` |
| Still Partial | `LAB-TV/XT/CI/AE/GR` |
| Global gates | Unchanged; governance/structural/traceability/safety pass, other gates fail |

## Checkpoint — after SRC-0024

> **Claim record — SYN-0001-C18 | artifact-observation**
> **Claim:** `SRC-0024` establishes current ISO 20387:2018 biobanking-standard
> status, a not-yet-published Edition 2 FDIS and the ISO 15189 diagnostic scope
> boundary, but independent strict review accepts no new Pass; the score remains
> 29/110 (26.4%).
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0024` transaction; public
> ISO metadata/abstracts are not paid normative text, accreditation programme,
> jurisdictional adoption, conformity, implementation or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0024](../sources/src-0024-iso-20387-biobanking-standard-current-status.md);
> [GOV-0014](../governance/gov-0014-iso-20387-biobanking-standard.md);
> `SRC-0024-C01`–`C08`, `GOV-0014-C01`–`C06`; frozen `LAB-GR` criterion
> above; independent artifact/content/version/rubric review completed
> 2026-07-12.
> **Basis / limits:** The current international-standard and exception limbs
> are direct, but one ISO lineage cannot supply adoption/accreditation
> reconciliation. FDIS stage 50.00 is draft status, not current normative force.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `LAB-GR` | Partial | Partial | Current ISO 20387 biobanking scope/version/exceptions now direct; accreditation programme/adoption reconciliation remains missing |

| Result | After SRC-0024 |
| --- | ---: |
| Pass | 29 |
| Partial | 75 |
| Absent | 6 |
| Score | **29/110 = 26.4%** |
| Critical cells newly passed | None |
| Strengthened but still Partial | `LAB-GR` |
| Other cells/global gates | Unchanged |

## Checkpoint — after SRC-0025

> **Claim record — SYN-0001-C19 | artifact-observation**
> **Claim:** Complete CAP BAP integration and independent strict review accept
> exactly `LAB-GR` Partial→Pass, raising Laboratories/Biobanks from 5/10 to
> 6/10 and the overall score from 29/110 to 30/110 (27.3%), with 30 Pass,
> 74 Partial and 6 Absent.
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0025` transaction under
> frozen rubric v1.0; not absolute domain completeness, accreditation
> effectiveness or a claim about every jurisdiction.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0025](../sources/src-0025-cap-biorepository-accreditation-program.md);
> [GOV-0015](../governance/gov-0015-cap-biorepository-accreditation-program.md);
> [SYN-0012](syn-0012-global-canada-us-laboratory-biobank-governance-reconciliation.md);
> `SRC-0025-C01`–`C11`, `GOV-0015-C01`–`C07`, `SYN-0012-C01`–`C07`;
> frozen `LAB-GR` criterion above; independent artifact, content, locator,
> lineage, backlink and binary-score review completed 2026-07-12.
> **Basis / limits:** WHO, Canadian and CAP lineages directly supply the
> required global, national and accreditation predicates; NCI/ISO add bounded
> biobank scope without derivative double-counting. Programme availability,
> inspection and issuer-reported uptake do not establish implementation,
> effectiveness, incidents or any adjacent cell.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `LAB-GR` | Partial | **Pass** | `SYN-0012-C01`–`C05` reconcile WHO, Canadian licence-scoped national requirements, NCI/ISO biobank boundaries and CAP accreditation/adoption/exceptions across properly bounded independent lineages |

| Result | After SRC-0025 |
| --- | ---: |
| Pass | 30 |
| Partial | 74 |
| Absent | 6 |
| Score | **30/110 = 27.3%** |
| Critical cells newly passed | `LAB-GR` |
| Laboratories and biobanks | **6/10** |
| Existing Pass unchanged | `LAB-ST/AS/WL/SD/CT` |
| Still Partial | `LAB-TV/XT/CI/AE` |
| Global gates | Unchanged; governance/structural/traceability/safety pass, other gates fail |

## Checkpoint — after SRC-0026

> **Claim record — SYN-0001-C20 | artifact-observation**
> **Claim:** Complete WHO LQMS integration and independent strict review accept
> exactly `CPH-ST/AS/WL/TV/XT/CT` as Partial→Pass, raising Clinical/Public
> Health from 1/10 to 7/10 and the overall score from 30/110 to 36/110 (32.7%),
> with 36 Pass, 68 Partial and 6 Absent.
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0026` transaction under
> frozen rubric v1.0; not absolute domain completeness, a modern architecture
> validation, primary patient/population outcome or effectiveness evaluation.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md);
> [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md);
> [WFL-0010](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md);
> [SYS-0008](../systems/sys-0008-clinical-laboratory-information-reporting-ecosystem.md);
> [HAZ-0002](../hazards/haz-0002-patient-specimen-result-identity-quality-failure.md);
> [RSK-0013](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md);
> [CTL-0012](../controls/ctl-0012-clinical-laboratory-quality-reporting-continuity-controls.md);
> [SYN-0013](syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md);
> `SRC-0026-C01`–`C12`, `SYN-0013-C01`–`C10`; frozen CPH criteria above;
> independent full-artifact, source, locator, graph, lineage, safety and binary-
> score review completed 2026-07-12.
> **Basis / limits:** The integrated portfolio supplies the complete SF2 scope,
> asset, lifecycle, threat/hazard, bidirectional transfer and exact-edge control
> predicates. `CPH-SD/CI/AE` remain Partial, existing `CPH-GR` remains Pass and
> no global gate changes.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `CPH-ST` | Partial | **Pass** | `SYN-0013-C02` reconciles clinical diagnostics/genomics, laboratory medicine, care delivery and public-health reporting/surveillance across independent lineages. |
| `CPH-AS` | Partial | **Pass** | `AST-0006`/`SYN-0013-C03` cover every required asset and stakeholder class at SF2. |
| `CPH-WL` | Partial | **Pass** | `WFL-0010`/`SYN-0013-C04` cover the complete order→correction lifecycle and public-health branch. |
| `CPH-TV` | Partial | **Pass** | `HAZ-0002`/`SYN-0013-C05` distinguish manipulation, outage, mismatch, privacy, quality hazard and bounded exposure evidence. |
| `CPH-XT` | Partial | **Pass** | `RSK-0013`/`SYN-0013-C06` provide both complete sector-level transfer directions without upgrading the global observed-decision gate. |
| `CPH-CT` | Partial | **Pass** | `CTL-0012`/`SYN-0013-C07` map identity, validation, authorization, integrity, notification, downtime and recovery to exact edges. |

| Result | After SRC-0026 |
| --- | ---: |
| Pass | 36 |
| Partial | 68 |
| Absent | 6 |
| Score | **36/110 = 32.7%** |
| Critical cells newly passed | `CPH-ST/AS/WL/TV/XT/CT` |
| Clinical and public health | **7/10** |
| Existing Pass unchanged | `CPH-GR` |
| Still Partial | `CPH-SD/CI/AE` |
| Other cells/global gates | Unchanged |

## Checkpoint — after SRC-0027

> **Claim record — SYN-0001-C21 | artifact-observation**
> **Claim:** Complete APHL informatics-package integration and independent
> source/graph/rubric review accept exactly `CPH-SD` Partial→Pass, raising CPH
> from 7/10 to 8/10 and the overall score from 36/110 to 37/110 (33.6%), with
> 37 Pass, 67 Partial and 6 Absent.
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0027` transaction under
> frozen rubric v1.0; not absolute domain completeness, independent end-to-end
> conformance, patient outcome or safeguard-effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0027](../sources/src-0027-aphl-integrated-laboratory-information-public-health-exchange.md);
> [SYS-0009](../systems/sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md);
> [SYN-0014](syn-0014-clinical-public-health-system-boundary-reconciliation.md);
> `SRC-0027-C01`–`C12`, `SYS-0009-C01`–`C05`, `SYN-0014-C01`–`C05`;
> frozen `CPH-SD` criterion above; independent all-page/figure, artifact,
> locator, lineage, graph, backlink, safety and binary-score review completed
> 2026-07-12.
> **Basis / limits:** APHL supplies the coherent modern class and validation-
> aware boundary package; independent WHO/EHDS/FDA/NIST/NHS predicates provide
> SF2. `CPH-CI/AE` remain Partial, the other seven CPH cells remain Pass and no
> adjacent cell or global gate changes.

Changed statuses:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `CPH-SD` | Partial | **Pass** | `SYS-0009-C01`–`C05` and `SYN-0014-C01`–`C03` cover instruments, middleware/LIS, EHR/HIE, reference laboratories, public-health systems, cloud/IAM and definition/test/validation/staged-production/monitoring boundaries at SF2. |

| Result | After SRC-0027 |
| --- | ---: |
| Pass | 37 |
| Partial | 67 |
| Absent | 6 |
| Score | **37/110 = 33.6%** |
| Critical cells newly passed | `CPH-SD` |
| Clinical and public health | **8/10** |
| Existing Pass unchanged | `CPH-ST/AS/WL/TV/XT/CT/GR` |
| Still Partial | `CPH-CI/AE` |
| Other cells/global gates | Unchanged |

## Retired public checkpoint

`SYN-0001-C22` was withdrawn from the public corpus on 2026-07-16 because its
supporting lineage was retired for privacy. It contributes no incident,
outcome, control, evaluator, score, or global-gate unit. The surrounding
37/110 checkpoints remain the applicable public-corpus state for this stage.

## Checkpoint — after SRC-0029

> **Claim record — SYN-0001-C23 | artifact-observation**
> **Claim:** Complete integration of an independent national alert and review
> adds materially separate aggregate-review evidence and one source-reported
> fatal medication-safety outcome, but
> no cell changes status: the score remains 37/110 (33.6%), with 37 Pass,
> 67 Partial and 6 Absent.
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0029` transaction under
> frozen rubric v1.0; not 315 unique events/patients, same-event confirmation,
> absolute domain completeness or safeguard effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md);
> [INC-0003](../incidents/inc-0003-national-allergy-recording-fatality-review-2021-2023.md);
> [RSK-0015](../risk-scenarios/rsk-0015-allergy-record-entry-propagation-medication-harm.md);
> [CTL-0014](../controls/ctl-0014-allergy-record-identification-correction-safety-controls.md);
> `SRC-0029-C01`–`C11`, `INC-0003-C01`–`C07`, `RSK-0015-C01`–`C06`,
> `CTL-0014-C01`–`C07`; frozen CPH/THI/CTR/GOV/global criteria above;
> independent all-page, artifact, locator, report/incident-unit, lineage,
> control-state, graph, backlink, privacy/safety and binary-score reviews
> completed 2026-07-12.
> **Basis / limits:** `SRC-0029` is one independent national-review lineage. It
> does not confirm any separately documented case or independently evaluate a
> shared EPR/ePMA systems problem. The source moves from aggregate reports to
> `other incidents` without a
> mapping, so no remaining incident/report/near-miss count is derived. Alert
> actions/current listing do not promote effectiveness or a global gate.

| Result | After SRC-0029 |
| --- | ---: |
| Pass | 37 |
| Partial | 67 |
| Absent | 6 |
| Score | **37/110 = 33.6%** |
| Cell status changes | None |
| Clinical and public health | **8/10** |
| Incident corpus | At most 3 distinguishable primary-supported events in 2 sectors; below global floor |
| Global gates | Unchanged |

## Checkpoint — after SRC-0030

> **Claim record — SYN-0001-C24 | artifact-observation**
> **Claim:** Complete HSSIB thematic-review integration and independent
> all-page/method/unit/lineage/graph review add the separate EPR systems-
> evaluation predicate required by the strict clinical-outcome plan, but no
> cell changes status before explicit three-lineage reconciliation: the score
> remains 37/110 (33.6%), with 37 Pass, 67 Partial and 6 Absent.
> **Claim status:** active
> **Scope:** Wiki filesystem after the complete `SRC-0030` source transaction
> under frozen rubric v1.0; not a new incident, same-event confirmation,
> national incidence estimate or safeguard-effectiveness evaluation.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0030](../sources/src-0030-hssib-electronic-patient-record-systems-thematic-review.md);
> [SYS-0010](../systems/sys-0010-electronic-patient-record-safety-dependencies.md);
> `SRC-0030-C01`–`C13`, `SYS-0010-C01`–`C07`; frozen CPH/THI/CTR/FND/GOV
> and global criteria above; three independent read-only artifact, page,
> method, count, lineage, graph, safety and binary-score reviews completed
> 2026-07-12.
> **Basis / limits:** HSSIB is primary for its review and broader system-class
> findings but derivative for underlying cases. Its `112 → 63 → 50` flow and
> Appendix counts are report/coding units, not incidents or harmed patients;
> recommendations/observations are not implementation or effectiveness. The
> source does not confirm either event-specific outcome account, so `CPH-CI`
> remains
> Partial until a separately reserved synthesis reconciles the three lineages.

| Result | After SRC-0030 |
| --- | ---: |
| Pass | 37 |
| Partial | 67 |
| Absent | 6 |
| Score | **37/110 = 33.6%** |
| Cell status changes | None |
| Clinical and public health | **8/10** |
| Strengthened but still Partial | `CPH-CI` — independent evaluation present; explicit reconciliation pending |
| Incident corpus | At most 3 distinguishable primary-supported events in 2 sectors; HSSIB vignettes/code counts add none |
| Global gates | Unchanged |

## Checkpoint — after SYN-0015

`SYN-0001-C25` is superseded because its transition depended on a lineage
retired from the public corpus.

> **Claim record — SYN-0001-C49 | artifact-observation**
> **Claim:** Public-corpus review accepts no transition after `SYN-0015`:
> `CPH-CI` remains Partial, the overall score remains 37/110 (33.6%), CPH
> remains 8/10, and the totals remain 37 Pass, 67 Partial, and 6 Absent.
> **Evidence:** [SYN-0015](syn-0015-clinical-patient-outcome-systems-evaluation-reconciliation.md),
> `SYN-0015-C03/C04/C11`–`C16`; the frozen `CPH-CI` criterion and SF3 floor
> above.
> **Limits:** The national review supplies an outcome account and HSSIB an
> independent system-class evaluation, but neither supplies the missing
> claim-appropriate primary case record or measured near miss.

| Result | After SYN-0015 |
| --- | ---: |
| Pass | 37 |
| Partial | 67 |
| Absent | 6 |
| Score | **37/110 = 33.6%** |
| Critical cells newly passed | None |
| Clinical and public health | **8/10** |
| Existing CPH Pass unchanged | `CPH-ST/AS/WL/SD/TV/XT/CT/GR` |
| Still Partial | `CPH-CI/AE` |
| Dimensions at ≥9/10 | **0/11** |
| Incident corpus | 2 primary-supported events in 2 sectors; below `THI-CI` floor |
| Global gates | Pass/fail states unchanged; numeric gate input remains 37/110 and FAIL |

## Checkpoint — after SRC-0031

> **Claim record — SYN-0001-C26 | artifact-observation**
> **Claim:** Complete ICH Q13 ingestion and three independent source/locator,
> graph/safety and frozen-rubric reviews add the missing continuous-
> manufacturing quality/release/disposition evidence but change no frozen cell:
> the score remains 37 Pass, 67 Partial and 6 Absent = 37/110 (33.6%), with
> BMO still 0/10.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SRC-0031/GOV-0016/AST-0007/CTL-0015`;
> not a source-transaction promotion, deployed architecture, cyber incident,
> approved process, implementation or effectiveness result.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> `SRC-0031-C01`–`C11`; [AST-0007](../assets/ast-0007-biomanufacturing-assets-stakeholders.md),
> `AST-0007-C01`–`C04`; [WFL-0003](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md),
> `WFL-0003-C05/C06`; [SYS-0002](../systems/sys-0002-biomanufacturing-process-control.md),
> `SYS-0002-C05/C06`; [RSK-0002](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md),
> `RSK-0002-C05/C06`; [CTL-0015](../controls/ctl-0015-continuous-manufacturing-quality-control.md),
> `CTL-0015-C01`–`C06`; [SYN-0007](syn-0007-ot-applicability-cyberbio-sectors.md),
> `SYN-0007-C09`; three independent read-only reviews and root verification
> completed 2026-07-12.
> **Basis / limits:** Q13 is one harmonized technical lineage; FDA and EMA are
> regional adoption wrappers, not independent technical corroboration. Its
> annex examples are illustrative, not deployments/tests/incidents. The
> `BMO-AS/WL/XT/CT` predicates are now explicit but stay Partial until a
> separately reserved synthesis adjudicates each complete SF2 contract.

| Result | After SRC-0031 |
| --- | ---: |
| Pass | 37 |
| Partial | 67 |
| Absent | 6 |
| Score | **37/110 = 33.6%** |
| Cell status changes | None |
| Biomanufacturing and OT | **0/10** |
| Strengthened but still Partial | `BMO-AS/WL/XT/CT` — complete predicates assembled; explicit reconciliation pending |
| Other BMO Partial unchanged | `BMO-ST/SD/TV/CI/GR` |
| Still Absent | `BMO-AE` |
| Dimensions at ≥9/10 | **0/11** |
| Incident corpus | Unchanged; Q13 examples add no event or `INC` |
| Global gates | All pass/fail states unchanged; numeric input remains 37/110 and FAIL |

## Checkpoint — after SYN-0016

> **Claim record — SYN-0001-C27 | artifact-observation**
> **Claim:** Independent strict reconciliation accepts exactly `BMO-AS`,
> `BMO-WL`, `BMO-XT` and `BMO-CT` as Partial→Pass, raising the score to
> 41 Pass, 63 Partial and 6 Absent = 41/110 (37.3%) and BMO to 4/10; all
> other cells and all twelve global-gate pass/fail states remain unchanged.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SYN-0016` under frozen rubric v1.0;
> not absolute domain completeness, implementation, incident, compliance or
> effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SYN-0016](syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md),
> `SYN-0016-C01`–`C07`; prior zero-delta `SYN-0001-C26`; three independent
> structural/locator, source/criterion and semantic/frozen-rubric reviews plus
> two final scoring-contract rechecks completed 2026-07-12.
> **Basis / limits:** All nine asset/stakeholder classes, seven lifecycle
> stages, both transfer directions and six control limbs meet their literal
> SF2 contracts. Guttieres/Q13 supply AS/WL/XT; independent NIST/Q13 supply CT;
> FDA/EMA are not multiplied. Missing industrial, enterprise-architecture,
> threat, incident/outcome, effectiveness and independent-governance predicates
> remain non-scoring.

Changed status:

| Cell | Before | After | Acceptance basis |
| --- | --- | --- | --- |
| `BMO-AS` | Partial | **Pass** | complete independent-lineage asset/stakeholder reconciliation in `SYN-0016-C02` |
| `BMO-WL` | Partial | **Pass** | complete seven-stage/four-state lifecycle reconciliation in `SYN-0016-C03` |
| `BMO-XT` | Partial | **Pass** | both complete functional transfer directions in `SYN-0016-C04` |
| `BMO-CT` | Partial | **Pass** | all six NIST-OT plus Q13 quality exact-edge control limbs in `SYN-0016-C05` |

| Result | After SYN-0016 |
| --- | ---: |
| Pass | **41** |
| Partial | **63** |
| Absent | **6** |
| Score | **41/110 = 37.3%** |
| Biomanufacturing and OT | **4/10** |
| Critical cells | **38 Pass / 51 Partial / 2 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Other BMO cells | `ST/SD/TV/CI/GR` Partial; `AE` Absent |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail, numeric input now 41/110 and still FAIL |

## Checkpoint — after SRC-0032

> **Claim record — SYN-0001-C28 | artifact-observation**
> **Claim:** Complete AU DAS ingestion and independent artifact/governance,
> frozen-criterion and graph/semantic reviews materially strengthen the
> agriculture asset, lifecycle, system, transfer, control and governance
> predicates but change no frozen cell: the score remains 41 Pass, 63 Partial
> and 6 Absent = 41/110 (37.3%), with AGE still 1/10.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SRC-0032/GOV-0017` and canonical
> agriculture-page updates; not a source-transaction promotion, national
> adoption, incident, implementation, hostile cyber path or effectiveness
> result.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md),
> `SRC-0032-C01`–`C09`; [GOV-0017](../governance/gov-0017-au-digital-agriculture-strategy-2024-2030.md),
> `GOV-0017-C01`–`C05`; [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md),
> `AST-0003-C04`; [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md),
> `WFL-0007-C04/C05`; [SYS-0005](../systems/sys-0005-connected-smart-farm-ecosystem.md),
> `SYS-0005-C04`; [RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md),
> `RSK-0007-C06/C07`; [CTL-0005](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md),
> `CTL-0005-C05/C06`; frozen AGE criteria above; three independent read-only
> reviews and root verification completed 2026-07-12.
> **Basis / limits:** AU DAS supplies broad direct classes and both intended
> functional directions, but the full literal SF2 contracts remain incomplete.
> Missing genomes/herds/veterinarians, treatment/movement/environmental
> sampling/disposition, veterinary/plant-lab architecture, concrete adversarial
> vulnerabilities, a hostile cyber→animal/plant/ecosystem event, complete
> biosecurity+cyber response/recovery controls and current One Health national-
> instrument reconciliation prevent any source-only point.

| Result | After SRC-0032 |
| --- | ---: |
| Pass | **41** |
| Partial | **63** |
| Absent | **6** |
| Score | **41/110 = 37.3%** |
| Agriculture and environment | **1/10** |
| Strengthened but still Partial | `AGE-AS/WL/SD/TV/XT/CT/GR` |
| Still Absent | `AGE-CI/AE` |
| Critical cells | **38 Pass / 51 Partial / 2 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0017

> **Claim record — SYN-0001-C29 | artifact-observation**
> **Claim:** Independent literal `AGE-XT`, exact-edge `AGE-CT` and
> jurisdiction/instrument `AGE-GR` audits accept zero Partial→Pass transitions;
> the score remains 41 Pass, 63 Partial and 6 Absent = 41/110 (37.3%), AGE
> remains 1/10 and all global-gate states remain unchanged.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SYN-0017` under frozen rubric v1.0;
> not absolute domain completeness, external-evidence absence or a requirement
> for SF3 results in the SF2 transfer/control cells.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SYN-0017](syn-0017-au-agriculture-transfer-control-governance-reconciliation.md),
> `SYN-0017-C01`–`C06`; prior `SYN-0001-C28`; independent frozen `AGE-XT`,
> `AGE-CT` and `AGE-GR` read-only audits plus root verification completed
> 2026-07-12.
> **Basis / limits:** The reverse observation/sensor→digital-decision limb now
> reaches SF2, but the direct cyber/untrusted-state→farm-control→animal/plant/
> ecosystem path does not. `AGE-CT` lacks a direct biological-biosecurity edge
> and an explicit traceability-control→named-boundary mapping. `AGE-GR` lacks a
> second qualifying jurisdictional instrument line and a collectively complete
> two-jurisdiction portfolio reconciled under One Health. No `Partial` earns a
> point.

| Result | After SYN-0017 |
| --- | ---: |
| Pass | **41** |
| Partial | **63** |
| Absent | **6** |
| Score | **41/110 = 37.3%** |
| Agriculture and environment | **1/10** |
| Cell status changes | None |
| Critical cells | **38 Pass / 51 Partial / 2 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SRC-0033

> **Claim record — SYN-0001-C30 | artifact-observation**
> **Claim:** Complete NASEM AI/life-sciences ingestion plus independent
> artifact/locator, semantic/frozen-rubric and structural/relationship reviews
> materially strengthen all biological-AI predicates but change no frozen
> cell: the score remains 41 Pass, 63 Partial and 6 Absent = 41/110 (37.3%),
> with AIB still 0/10.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SRC-0033/AST-0008/WFL-0011/
> SYS-0011/RSK-0016/CTL-0016/GOV-0018` and bounded procurement-page updates;
> not a source-transaction promotion, incident, implementation, benchmark,
> binding governance or effectiveness result.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C01`–`C11`;
> [AST-0008](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md),
> `AST-0008-C01`–`C04`;
> [WFL-0011](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md),
> `WFL-0011-C01`–`C04`;
> [SYS-0011](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md),
> `SYS-0011-C01`–`C04`;
> [RSK-0016](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md),
> `RSK-0016-C01`–`C04`;
> [CTL-0016](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md),
> `CTL-0016-C01`–`C06`;
> [GOV-0018](../governance/gov-0018-nasem-ai-life-sciences-advisory-recommendations-2025.md),
> `GOV-0018-C01`–`C05`; bounded `AST-0004/WFL-0008/RSK-0008/CTL-0006`
> interface claims; three independent read-only reviews and root verification
> completed 2026-07-12.
> **Basis / limits:** NASEM is one committee-report lineage; its mirrors,
> chapters, Appendix A and cited studies are not multiplied. The two-lineage
> `AIB-ST/AS/XT/CT` predicate structures are now explicit but await a separately
> reserved synthesis. `AIB-WL/SD/TV` retain literal gaps; no qualifying primary
> incident or direct independent benchmark satisfies `CI/AE`; one U.S.
> advisory line cannot satisfy `GR`. No `Partial` earns a point.

| Result | After SRC-0033 |
| --- | ---: |
| Pass | **41** |
| Partial | **63** |
| Absent | **6** |
| Score | **41/110 = 37.3%** |
| AI and bioinformatics | **0/10** |
| Strongest assembled candidates | `AIB-ST/AS/XT/CT` — separate SF2 reconciliation pending |
| Partial with literal gaps | `AIB-WL/SD/TV/CI/GR` |
| Still Absent | `AIB-AE` |
| Critical cells | **38 Pass / 51 Partial / 2 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0018

> **Claim record — SYN-0001-C31 | artifact-observation**
> **Claim:** Independent frozen-criterion, exact-path/control and structural
> audits of the dedicated biological-AI reconciliation promote exactly
> `AIB-ST`, `AIB-AS`, `AIB-XT` and `AIB-CT`: the corpus now has 45 Pass,
> 59 Partial and 6 Absent = 45/110 (40.9%), with AIB at 4/10.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SYN-0018`; not absolute domain
> completeness, production deployment, incident, benchmark, governance
> adoption, rollback or effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0018](syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md),
> `SYN-0018-C01`–`C07`; [AST-0008](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md),
> `AST-0008-C01`–`C04`; [CTL-0016](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md),
> `CTL-0016-C01`–`C06`; independent `AIB-ST/AS`, `AIB-XT/CT` and structural/
> arithmetic audits completed 2026-07-12.
> **Basis / limits:** NASEM, USENIX, AU and the single NIST programme are
> counted at claim-appropriate lineage boundaries. All literal SF2 contracts
> for the four promoted cells are direct in the reconciled unions. Model
> retirement, containers/model registries, drift/confidentiality leakage, a
> qualifying primary incident, direct independent benchmark and current
> two-jurisdiction governance remain open; no other cell or global gate moves.

| Result | After SYN-0018 |
| --- | ---: |
| Pass | **45** |
| Partial | **59** |
| Absent | **6** |
| Score | **45/110 = 40.9%** |
| AI and bioinformatics | **4/10** |
| Cell status changes | `AIB-ST/AS/XT/CT`: Partial → Pass |
| Critical cells | **42 Pass / 47 Partial / 2 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SRC-0034

> **Claim record — SYN-0001-C32 | artifact-observation**
> **Claim:** Complete ProteinGym ingestion and five bounded canonical updates
> add the first direct primary empirical AIB benchmark/result and move only
> `AIB-AE` from Absent to Partial; totals remain 45 Pass, while Partial becomes
> 60 and Absent becomes 5, so the score stays 45/110 (40.9%) and AIB 4/10.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SRC-0034` and bounded `AST-0008/
> WFL-0011/SYS-0011/RSK-0016/CTL-0016` updates; not deployment, incident,
> downstream patient/organism outcome, independent replication or control-
> family effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md),
> `SRC-0034-C01`–`C09`; [AST-0008](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md),
> `AST-0008-C05`; [WFL-0011](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md),
> `WFL-0011-C05`; [SYS-0011](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md),
> `SYS-0011-C05`; [RSK-0016](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md),
> `RSK-0016-C05`; [CTL-0016](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md),
> `CTL-0016-C07`; three independent artifact/content, frozen-rubric/semantic
> and structural audits completed 2026-07-12.
> **Basis / limits:** ProteinGym directly satisfies the primary-record part of
> `AIB-CI` and supplies benchmark evidence for `AIB-AE`, but one author-team
> lineage cannot supply SF3 confirmation; authors overlap several evaluated
> methods, and NASEM cites rather than reproduces the benchmark. `AIB-WL/SD/TV/
> CI/GR` remain Partial, `AIB-AE` is now Partial and no Pass/global gate moves.

| Result | After SRC-0034 |
| --- | ---: |
| Pass | **45** |
| Partial | **60** |
| Absent | **5** |
| Score | **45/110 = 40.9%** |
| AI and bioinformatics | **4/10** |
| Cell status changes | `AIB-AE`: Absent → Partial |
| `AIB-CI` | Partial — first direct primary empirical benchmark/result; independent confirmation still absent |
| Critical cells | **42 Pass / 47 Partial / 2 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SRC-0035

> **Claim record — SYN-0001-C33 | artifact-observation**
> **Claim:** Complete PATH-SAFE evaluation/APHA implementation ingestion and
> five bounded canonical updates add the first retained primary empirical AGE
> field-survey/result plus bounded implementation, method-design, maturity and
> evaluator evidence. `AGE-CI` and `AGE-AE` move Absent→Partial; no Pass
> changes, so totals become 45 Pass, 62 Partial and 3 Absent = 45/110 (40.9%).
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SRC-0035` and bounded `AST-0003/
> WFL-0007/SYS-0005/RSK-0007/CTL-0005` updates; not a GB disease incident,
> qualifying consequence, cyber-control test, causal effectiveness result or
> independent empirical replication.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0035](../sources/src-0035-uk-path-safe-final-evaluation-2025.md),
> `SRC-0035-C01`–`C11`;
> [AST-0003](../assets/ast-0003-smart-farm-production-and-supply-assets.md),
> `AST-0003-C05`;
> [WFL-0007](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md),
> `WFL-0007-C06`;
> [SYS-0005](../systems/sys-0005-connected-smart-farm-ecosystem.md),
> `SYS-0005-C05`;
> [RSK-0007](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md),
> `RSK-0007-C08`;
> [CTL-0005](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md),
> `CTL-0005-C07`; independent first-half/APHA, second-half/frozen-rubric and
> companion/artifact/lineage audits completed 2026-07-12.
> **Basis / limits:** APHA supplies a primary field-survey/result and bounded
> implemented surveillance path; RAND supplies a distinguishable commissioned
> evaluation role, not independent laboratory replication or qualifying
> safeguard-effectiveness evaluation. The all-negative result is biological
> null evidence, not an incident, consequence or control failure. Each of
> `AGE-AS/WL/SD/TV/XT/CT/GR` retains at least one decisive literal
> gap, and no global gate moves.

| Result | After SRC-0035 |
| --- | ---: |
| Pass | **45** |
| Partial | **62** |
| Absent | **3** |
| Score | **45/110 = 40.9%** |
| Agriculture and environment | **1/10** |
| Cell status changes | `AGE-CI`, `AGE-AE`: Absent → Partial |
| Critical cells | **42 Pass / 48 Partial / 1 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SRC-0036/GOV-0019

> **Claim record — SYN-0001-C34 | artifact-observation**
> **Claim:** Complete UK BSS strategy/progress ingestion and its canonical
> governance representation add a current UK national One Health policy line
> spanning animal, plant, environmental and data/cyberbio priorities, but the
> source transaction alone changes no frozen cell: totals remain 45 Pass, 62
> Partial and 3 Absent = 45/110 (40.9%).
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SRC-0036/GOV-0019`; not a UK law,
> complete implementation, demonstrated technical integration, independent
> effectiveness result or completed two-jurisdiction reconciliation.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0036](../sources/src-0036-uk-biological-security-strategy-2023-current.md),
> `SRC-0036-C01`–`C10`;
> [GOV-0019](../governance/gov-0019-uk-biological-security-strategy-2023-current.md),
> `GOV-0019-C01`–`C06`; independent full-strategy, implementation/currentness
> and structural/locator audits completed 2026-07-12.
> **Basis / limits:** One UK policy lineage strengthens `AGE-GR` but does not
> itself perform the criterion's explicit two-jurisdiction reconciliation.
> `AGE-GR` remains Partial and all other cell/gate states are unchanged.

| Result | After SRC-0036/GOV-0019 |
| --- | ---: |
| Pass | **45** |
| Partial | **62** |
| Absent | **3** |
| Score | **45/110 = 40.9%** |
| Agriculture and environment | **1/10** |
| Cell status changes | None |
| Critical cells | **42 Pass / 48 Partial / 1 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0019

> **Claim record — SYN-0001-C35 | artifact-observation**
> **Claim:** Independent strict UK–U.S. national One Health reconciliation
> accepts exactly `AGE-GR` Partial→Pass. Totals become 46 Pass, 61 Partial and
> 3 Absent = 46/110 (41.8%); AGE becomes 2/10 and critical cells become
> 43/47/1. All other cells and all global gates remain unchanged.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SYN-0019`; not absolute domain
> completeness, law, cross-compliance, technical integration, implementation
> or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0019](syn-0019-uk-us-national-one-health-governance-reconciliation.md),
> `SYN-0019-C01`–`C06`; frozen `AGE-GR` criterion/source floor; independent
> provenance/literal-instrument, evidence/semantic and structural/score audits
> completed 2026-07-12; prior `SYN-0001-C34` checkpoint.
> **Basis / limits:** Two independent current national One Health lineages and
> one explicit complete portfolio reconciliation meet SF2. Exactly one
> critical cell moves; Partial remains zero points and no global gate moves.

| Result | After SYN-0019 |
| --- | ---: |
| Pass | **46** |
| Partial | **61** |
| Absent | **3** |
| Score | **46/110 = 41.8%** |
| Agriculture and environment | **2/10** |
| Cell status changes | `AGE-GR`: Partial → **Pass** |
| Critical cells | **43 Pass / 47 Partial / 1 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0020

> **Claim record — SYN-0001-C36 | artifact-observation**
> **Claim:** Independent literal/semantic/structural review accepts exactly
> `FND-AS`, `FND-WL` and `FND-GR` Partial→Pass. Totals become 49 Pass, 58
> Partial and 3 Absent = 49/110 (44.5%); Foundations becomes 7/10 and critical
> cells become 44/46/1. All global gates and the count of dimensions at least
> 9/10 remain unchanged.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SYN-0020`; not absolute domain
> completeness, sector-inventory completeness, universal lifecycle, legal
> advice, cross-compliance, implementation or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0020](syn-0020-foundational-cross-sector-assets-lifecycle-governance-reconciliation.md),
> `SYN-0020-C01`–`C09`; frozen criteria/source floors; independent evidence/
> literal, semantic and structural/score audits completed 2026-07-12; prior
> `SYN-0001-C35`.
> **Basis / limits:** Three complete SF2 criteria move and only `FND-GR` is
> critical. `FND-TV/CI/AE` remain Partial in this transaction; Partial earns no
> point and no global gate moves.

| Result | After SYN-0020 |
| --- | ---: |
| Pass | **49** |
| Partial | **58** |
| Absent | **3** |
| Score | **49/110 = 44.5%** |
| Foundations | **7/10** |
| Cell status changes | `FND-AS`, `FND-WL`, `FND-GR`: Partial → **Pass** |
| Critical cells | **44 Pass / 46 Partial / 1 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0021

> **Claim record — SYN-0001-C37 | artifact-observation**
> **Claim:** Independent strict reviews accept exactly `GEN-AS`, `GEN-WL` and
> `GEN-SD` Partial→Pass. Totals become 52 Pass, 55 Partial and 3 Absent =
> 52/110 (47.3%); Genomics/omics becomes 8/10 and critical cells become
> 47/43/1. Dimensions at least 9/10 and all global gates remain unchanged.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SYN-0021`; not absolute domain
> completeness, whole-topology validation, implemented universal consent/
> custody propagation, genomic outcome or safeguard effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0021](syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md),
> `SYN-0021-C01`–`C07`; frozen criteria/source floors; three independent
> literal/semantic/structural audits completed 2026-07-12; prior
> `SYN-0001-C36`.
> **Basis / limits:** Three critical SF2 cells move. `GEN-CI/AE` remain Partial,
> Partial earns no point and no global gate moves.

| Result | After SYN-0021 |
| --- | ---: |
| Pass | **52** |
| Partial | **55** |
| Absent | **3** |
| Score | **52/110 = 47.3%** |
| Genomics and omics | **8/10** |
| Cell status changes | `GEN-AS`, `GEN-WL`, `GEN-SD`: Partial → **Pass** |
| Critical cells | **47 Pass / 43 Partial / 1 Absent** |
| Dimensions at least 9/10 | **0/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0022

> **Claim record — SYN-0001-C38 | artifact-observation**
> **Claim:** Independent strict reviews accept exactly `FND-CI` and `FND-AE`
> Partial→Pass. Totals become 54 Pass, 53 Partial and 3 Absent = 54/110
> (49.1%); Foundations becomes 9/10, critical cells become 49/41/1 and
> dimensions at least 9/10 become 1/11. All global gates remain unchanged.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SYN-0022`; not absolute domain
> completeness, event-count sufficiency, sector safeguard effectiveness,
> control-gate completion or independent replication of every example.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0022](syn-0022-foundational-consequence-assurance-calibration.md),
> `SYN-0022-C01`–`C08`; frozen criteria/source floors; three independent
> semantic/evidence/structural audits completed 2026-07-12; prior
> `SYN-0001-C37`.
> **Basis / limits:** Two critical foundational SF3 cells move. `FND-TV` and
> every sector/global incident/effectiveness criterion retain separate gaps;
> Partial earns no point and no global gate moves.

| Result | After SYN-0022 |
| --- | ---: |
| Pass | **54** |
| Partial | **53** |
| Absent | **3** |
| Score | **54/110 = 49.1%** |
| Foundations | **9/10** |
| Cell status changes | `FND-CI`, `FND-AE`: Partial → **Pass** |
| Critical cells | **49 Pass / 41 Partial / 1 Absent** |
| Dimensions at least 9/10 | **1/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0023

> **Claim record — SYN-0001-C39 | artifact-observation**
> **Claim:** Three independent strict reviews accept exactly `SEB-ST`,
> `SEB-SD`, `SEB-XT`, `LAB-XT` and `LAB-CI` Partial→Pass. Totals become 59
> Pass, 48 Partial and 3 Absent = 59/110 (53.6%); SEB becomes 5/10, LAB
> becomes 8/10 and critical cells become 54/36/1. Dimensions at least 9/10
> and all global gates remain unchanged.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SYN-0023`; not absolute domain
> completeness or evidence for adjacent SEB/LAB criteria.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0023](syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md),
> `SYN-0023-C01`–`C09`; frozen criteria/source floors; three independent
> structural/provenance, SEB-evidence and LAB-evidence audits completed
> 2026-07-12; prior `SYN-0001-C38`.
> **Basis / limits:** Five critical cells move. SEB product-disposition,
> insider/supply, incident/effectiveness/current-U.S. gaps and LAB insider/
> hazard/effectiveness gaps remain; Partial earns no point and no gate moves.

| Result | After SYN-0023 |
| --- | ---: |
| Pass | **59** |
| Partial | **48** |
| Absent | **3** |
| Score | **59/110 = 53.6%** |
| Engineering biology | **5/10** |
| Laboratories/biobanks | **8/10** |
| Cell status changes | `SEB-ST`, `SEB-SD`, `SEB-XT`, `LAB-XT`, `LAB-CI`: Partial → **Pass** |
| Critical cells | **54 Pass / 36 Partial / 1 Absent** |
| Dimensions at least 9/10 | **1/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0024

> **Claim record — SYN-0001-C40 | artifact-observation**
> **Claim:** Independent semantic/evidence and structural/governance reviews
> accept exactly `CTR-AS`, `CTR-WL`, `CTR-SD`, `GOV-WL`, `GOV-TV`, `GOV-XT`
> and `THI-AS` Partial→Pass. Totals become 66 Pass, 41 Partial and 3 Absent =
> 66/110 (60.0%); CTR and GOV become 8/10, THI becomes 2/10 and critical
> cells become 55/35/1. Dimensions at least 9/10 and all global gates remain
> unchanged.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `SYN-0024`; not absolute domain
> completeness or evidence for any adjacent sector/SF3 criterion.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0024](syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md),
> `SYN-0024-C01`–`C11`; frozen criteria/source floors; two independent audits
> completed 2026-07-12; prior `SYN-0001-C39`.
> **Basis / limits:** Seven reconciliation gaps close and only critical
> `CTR-SD` moves. All incident-count, independent-investigation,
> effectiveness, enforcement and global-gate blockers remain explicit;
> Partial earns no point.

| Result | After SYN-0024 |
| --- | ---: |
| Pass | **66** |
| Partial | **41** |
| Absent | **3** |
| Score | **66/110 = 60.0%** |
| Threats/incidents | **2/10** |
| Controls | **8/10** |
| Governance | **8/10** |
| Cell status changes | `THI-AS`, `CTR-AS`, `CTR-WL`, `CTR-SD`, `GOV-WL`, `GOV-TV`, `GOV-XT`: Partial → **Pass** |
| Critical cells | **55 Pass / 35 Partial / 1 Absent** |
| Dimensions at least 9/10 | **1/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0025

> **Claim record — SYN-0001-C41 | artifact-observation**
> **Claim:** Independent evidence, modality and rubric audits accept exactly
> `AGE-WL`, `AGE-SD`, `AGE-TV`, `AGE-CI` and `AGE-CT` Partial→Pass. Totals
> become 71 Pass, 36 Partial and 3 Absent = 71/110 (64.5%); AGE becomes 7/10
> and critical cells become 60/30/1. Dimensions at least 9/10 remain 1/11 and
> all global gates remain unchanged.
> **Claim status:** active
> **Scope:** Wiki filesystem after active `INC-0004`, `HAZ-0003/0004` and
> `SYN-0025`; not absolute domain completeness or evidence for `AGE-AS/XT/AE`
> or adjacent cross-cutting cells.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0025](syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md),
> `SYN-0025-C01`–`C10`; frozen criteria/source floors; independent lifecycle/
> system/threat and incident/consequence/control audits completed 2026-07-12;
> prior `SYN-0001-C40`.
> **Basis / limits:** Five complete critical contracts move. `AGE-XT` remains
> Partial because food-processing throughput is not an animal/plant/ecosystem
> effect; herd and independent safeguard-effectiveness gaps also remain open.

| Result | After SYN-0025 |
| --- | ---: |
| Pass | **71** |
| Partial | **36** |
| Absent | **3** |
| Score | **71/110 = 64.5%** |
| Agriculture/environment | **7/10** |
| Cell status changes | `AGE-WL`, `AGE-SD`, `AGE-TV`, `AGE-CI`, `AGE-CT`: Partial → **Pass** |
| Critical cells | **60 Pass / 30 Partial / 1 Absent** |
| Dimensions at least 9/10 | **1/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0026

> **Claim record — SYN-0001-C42 | artifact-observation**
> **Claim:** Independent artifact/evidence and strict rubric audits accept
> exactly `AGE-AS` and `AGE-AE` Partial→Pass. Totals become 73 Pass,
> 34 Partial and 3 Absent = 73/110 (66.4%); AGE becomes 9/10, critical cells
> become 61/29/1 and dimensions at least 9/10 become 2/11. All global gates
> remain unchanged.
> **Claim status:** active
> **Scope:** Wiki after active `SRC-0041`, updated `AST-0009`, `CTL-0019` and
> `SYN-0026`; not absolute domain completeness or evidence for `AGE-XT`,
> `CTR-AE`, `THI-CI` or any global gate.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0026](syn-0026-us-animal-disease-traceability-herd-assurance-reconciliation.md),
> `SYN-0026-C01`–`C07`; `SRC-0041-C01`–`C11`; frozen criteria/source floors;
> two independent audits completed 2026-07-12; prior `SYN-0001-C41`.
> **Basis / limits:** Literal herd closes one critical SF2 cell. Deployed ADT
> tests plus an independent OIG real-trace audit close the bounded SF3 AGE
> assurance cell. `AGE-XT` and all cross-sector/global floors remain open.

| Result | After SYN-0026 |
| --- | ---: |
| Pass | **73** |
| Partial | **34** |
| Absent | **3** |
| Score | **73/110 = 66.4%** |
| Agriculture/environment | **9/10** |
| Cell status changes | `AGE-AS`, `AGE-AE`: Partial → **Pass** |
| Critical cells | **61 Pass / 29 Partial / 1 Absent** |
| Dimensions at least 9/10 | **2/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0027

> **Claim record — SYN-0001-C43 | artifact-observation**
> **Claim:** Independent artifact/incident and strict semantic/rubric audits
> accept exactly `AGE-XT` Partial→Pass. Totals become 74 Pass, 33 Partial and
> 3 Absent = 74/110 (67.3%); AGE becomes 10/10, critical cells become
> 62/28/1, dimensions at least 9/10 remain 2/11 and all global gates remain
> unchanged.
> **Claim status:** active
> **Scope:** Wiki after active `SRC-0042`, `INC-0005`, `RSK-0018` and
> `SYN-0027`; not absolute domain completeness, SF3 event confirmation or
> evidence for any adjacent incident/control/global criterion.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0027](syn-0027-canada-agriculture-cyber-animal-effect-reconciliation.md),
> `SYN-0027-C01`–`C08`; `SRC-0042-C01`–`C11`; frozen criterion/source floor;
> two independent audits completed 2026-07-12; prior `SYN-0001-C42`.
> **Basis / limits:** The direct forward animal-effect literal and independent
> reverse-direction portfolio meet SF2. The anonymous event lacks independent
> forensic/veterinary confirmation, and every count, investigation,
> effectiveness and global-gate blocker remains explicit.

| Result | After SYN-0027 |
| --- | ---: |
| Pass | **74** |
| Partial | **33** |
| Absent | **3** |
| Score | **74/110 = 67.3%** |
| Agriculture/environment | **10/10** |
| Cell status changes | `AGE-XT`: Partial → **Pass** |
| Critical cells | **62 Pass / 28 Partial / 1 Absent** |
| Dimensions at least 9/10 | **2/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0028

`SYN-0001-C44` is superseded because four of its incident/control transitions
lost a required public-corpus numerator after privacy retirement.

> **Claim record — SYN-0001-C50 | artifact-observation**
> **Claim:** Public-corpus review accepts exactly four Partial→Pass
> transitions after `SYN-0028`: `BMO-ST/TV/CI/GR`. Totals become 78 Pass,
> 29 Partial, and 3 Absent, or 78/110 (70.9%); BMO becomes 8/10, THI
> remains 2/10, CTR remains 8/10, critical cells become 66/24/1, dimensions
> at least 9/10 remain 2/11, and global gates remain 7 Pass/5 Fail.
> **Evidence:** [SYN-0028](syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md),
> `SYN-0028-C01`–`C07`, `C09`, and `C14`–`C17`; exact frozen criteria and
> source floors; prior recalculated `SYN-0001-C43`.
> **Limits:** Five public event/review pages remain below the six-event floor;
> three technical/control-lesson lineages and one qualifying investigation do
> not pass the separate `THI-SD/CT/AE` or `CTR-CI` contracts.

| Result | After SYN-0028 |
| --- | ---: |
| Pass | **78** |
| Partial | **29** |
| Absent | **3** |
| Score | **78/110 = 70.9%** |
| Biomanufacturing and OT | **8/10** |
| Threats and incidents | **2/10** |
| Controls | **8/10** |
| Cell status changes | `BMO-ST/TV/CI/GR`: Partial → **Pass** |
| Critical cells | **66 Pass / 24 Partial / 1 Absent** |
| Dimensions at least 9/10 | **2/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0029

> **Claim record — SYN-0001-C45 | artifact-observation**
> **Claim:** Independent decision, evidence, scope, source-lineage and
> structural audits accept exactly eight Partial→Pass transitions:
> `AIB-WL/SD/TV/CI/AE/GR`, `FND-TV` and `THI-TV`. Totals become 86 Pass,
> 21 Partial and 3 Absent = 86/110 (78.2%); the dimension vector becomes
> `10/8/5/8/8/8/10/10/3/8/8`, critical cells become 73/17/1, dimensions at
> least 9/10 become 3/11 and all global-gate states remain 7 Pass/5 Fail.
> **Claim status:** active
> **Scope:** Wiki after active `SRC-0049`–`SRC-0054`, `GOV-0024`–`GOV-0026`,
> `WFL-0013`, `SYS-0013`, `THR-0003`, `HAZ-0005`, `TEC-0002/0003`,
> `VUL-0004`, `CTL-0021` and `SYN-0029`; not certified ≥90% completeness or
> proof of universal AI-control effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0029](syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md),
> `SYN-0029-C01`–`C11`; exact frozen criteria/source floors; independent
> decision/evidence/source-lineage/structural audits completed 2026-07-12;
> prior `SYN-0001-C50`.
> **Basis / limits:** Every accepted literal and evidence floor is directly
> reconciled. CASP is an empirical study, not an incident; policy/standard
> issuance is not adoption or effectiveness; five global gates remain open.

| Result | After SYN-0029 |
| --- | ---: |
| Pass | **86** |
| Partial | **21** |
| Absent | **3** |
| Score | **86/110 = 78.2%** |
| Dimension vector | `10/8/5/8/8/8/10/10/3/8/8` |
| Cell status changes | `AIB-WL/SD/TV/CI/AE/GR`, `FND-TV`, `THI-TV`: Partial → **Pass** |
| Critical cells | **73 Pass / 17 Partial / 1 Absent** |
| Dimensions at least 9/10 | **3/11** |
| Global gates | All twelve pass/fail states unchanged; 7 Pass / 5 Fail |

## Checkpoint — after SYN-0030

`SYN-0001-C46` is superseded because its transition list assumed four
incident/control cells had already passed in the public pre-state.

> **Claim record — SYN-0001-C51 | artifact-observation**
> **Claim:** Public-corpus review accepts exactly ten Partial→Pass transitions
> after `SYN-0030`: `GEN-CI`, `THI-WL/SD/CI/CT/AE/GR`, `CTR-CI`, and
> `GOV-CI/AE`. Totals become 96 Pass, 11 Partial, and 3 Absent, or 96/110
> (87.3%); the dimension vector becomes `10/9/5/8/8/8/10/10/9/9/10`,
> critical cells become 82/8/1, dimensions at least 9/10 become 7/11, and
> the incident global gate changes Fail→Pass, producing 8 Pass/4 Fail.
> **Evidence:** [SYN-0030](syn-0030-23andme-genomic-incident-governance-reconciliation.md),
> `SYN-0030-C02`–`C09` and `C11`–`C15`; exact frozen criteria/source floors;
> prior recalculated `SYN-0001-C45`.
> **Limits:** 23andMe is one event and the OPC/ICO work one joint
> investigation. `GOV-AE` passes as two jurisdiction-specific legal
> implementation evaluations, not as two investigations, deployments, or an
> effectiveness result; CPH remains 8/10.

| Result | After SYN-0030 |
| --- | ---: |
| Pass | **96** |
| Partial | **11** |
| Absent | **3** |
| Score | **96/110 = 87.3%** |
| Dimension vector | `10/9/5/8/8/8/10/10/9/9/10` |
| Cell status changes | `GEN-CI`, `THI-WL/SD/CI/CT/AE/GR`, `CTR-CI`, `GOV-CI/AE`: Partial → **Pass** |
| Critical cells | **82 Pass / 8 Partial / 1 Absent** |
| Dimensions at least 9/10 | **7/11** |
| Global gates | Incident: Fail → **Pass**; 8 Pass / 4 Fail |

## Checkpoint — after SYN-0031

> **Claim record — SYN-0001-C47 | artifact-observation**
> **Claim:** Three independent laboratory-source/rubric, structural/semantic
> and reverse-direction/locator audits accept exactly two Partial→Pass
> transitions: `LAB-TV` and `THI-XT`. Totals become 98 Pass, 9 Partial and 3
> Absent = 98/110 (89.1%); the dimension vector becomes
> `10/9/5/9/8/8/10/10/10/9/10`, critical cells become 84/6/1, dimensions at
> least 9/10 become 8/11 and the directionality global gate changes Fail→Pass,
> producing 9 Pass/3 Fail.
> **Claim status:** active
> **Scope:** Wiki after active `SRC-0057/0058`, `INC-0008`, `THR-0005`,
> `HAZ-0006`, `VUL-0006`, `RSK-0021`, `CTL-0023` and `SYN-0031`; not final
> certification because the numeric, risk-chain and control-effectiveness
> global gates remain failed.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0031](syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md),
> `SYN-0031-C02`–`C08` and `C10`–`C13`;
> [SYN-0003](syn-0003-cross-domain-transfer-directions.md),
> `SYN-0003-C05`; exact frozen `LAB-TV`, `THI-XT` and directionality-gate
> contracts; independent laboratory evidence, structural/semantic and
> directionality/locator audits completed 2026-07-12; prior `SYN-0001-C51`.
> **Basis / limits:** Every literal and source floor is directly reconciled.
> The reverse path is observed through the digital result/notification
> decision node, while individual behavior and population effects remain
> unknown/modelled. HSE's unnamed occasions are not multiplied into incidents,
> and implementation/recommendation evidence creates no assurance promotion.

| Result | After SYN-0031 |
| --- | ---: |
| Pass | **98** |
| Partial | **9** |
| Absent | **3** |
| Score | **98/110 = 89.1%** |
| Dimension vector | `10/9/5/9/8/8/10/10/10/9/10` |
| Cell status changes | `LAB-TV`, `THI-XT`: Partial → **Pass** |
| Critical cells | **84 Pass / 6 Partial / 1 Absent** |
| Dimensions at least 9/10 | **8/11** |
| Global gates | Directionality: Fail → **Pass**; 9 Pass / 3 Fail |

## Checkpoint — after SYN-0032

> **Claim record — SYN-0001-C48 | artifact-observation**
> **Claim:** Independent evidence/safety, structural/rubric-readiness and
> synthesis audits accept exactly three Partial→Pass transitions: SEB-WL,
> SEB-TV and SEB-GR. SEB-CI and SEB-AE improve only Absent→Partial because
> independent confirmation/evaluation remains unsatisfied. Totals become 101
> Pass, 8 Partial and 1 Absent = 101/110 (91.8%); the dimension vector becomes
> 10/9/8/9/8/8/10/10/10/9/10, critical cells become 87/4/0, dimensions at
> least 9/10 remain 8/11 and global gates remain 9 Pass/3 Fail.
> **Claim status:** active
> **Scope:** Wiki after active SRC-0059/0060/0061, WFL-0014, THR-0006,
> HAZ-0007, VUL-0007, CTL-0024, GOV-0028 and SYN-0032; not final
> certification because numeric, risk-chain and controls gates remain failed.
> **As of:** 2026-07-13.
> **Review after:** 2026-07-27.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYN-0032](syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md),
> SYN-0032-C01–C11; exact frozen SEB-WL/TV/CI/AE/GR contracts; independent
> audits completed 2026-07-13; prior SYN-0001-C47.
> **Basis / limits:** Every accepted SF2 literal is directly reconciled.
> Shared SecureDNA safeguard/authors and developer participation prevent SF3
> independence for SEB-CI/AE. One NIST study counts as one test instance, and
> aggregate operational decisions do not prove deployment or prevented harm.

| Result | After SYN-0032 |
| --- | ---: |
| Pass | **101** |
| Partial | **8** |
| Absent | **1** |
| Score | **101/110 = 91.8%** |
| Dimension vector | 10/9/8/9/8/8/10/10/10/9/10 |
| Cell status changes | SEB-WL/TV/GR: Partial → **Pass**; SEB-CI/AE: Absent → Partial |
| Critical cells | **87 Pass / 4 Partial / 0 Absent** |
| Dimensions at least 9/10 | **8/11** |
| Global gates | Unchanged: 9 Pass / 3 Fail |

## Updating the score

After each source transaction, add a dated checkpoint with only changed cells,
new totals and gate states. Preserve older checkpoints unless a public-corpus
retirement invalidates their numerators; in that case retain the superseded
claim ID and publish the recalculated state. A cell changes to `Pass` only when
its full criterion and floor are met; “more detail” is not a point. At final
certification, re-audit all 110 cells rather than summing incremental claims.

## Related pages

- [SYN-0032 — Engineering-biology lifecycle/threat/screening/governance reconciliation](syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)
- [SYN-0031 — Laboratory threat and reverse-transfer reconciliation](syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)
- [SYN-0030 — 23andMe genomic incident and governance reconciliation](syn-0030-23andme-genomic-incident-governance-reconciliation.md)
- [SYN-0029 — Biological-AI lifecycle, benchmark and governance reconciliation](syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SYN-0028 — BMO scope, threat, incident and governance reconciliation](syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)
- [SYN-0027 — AAFC-account agriculture animal-effect reconciliation](syn-0027-canada-agriculture-cyber-animal-effect-reconciliation.md)
- [INC-0005 — Anonymous chicken-farm event account](../incidents/inc-0005-anonymous-chicken-farm-temperature-control-animal-deaths-2023.md)
- [SRC-0042 — AAFC account and illustration](../sources/src-0042-aafc-chicken-farm-cyberattack-animal-effect-2023.md)
- [SYN-0026 — U.S. herd/traceability assurance reconciliation](syn-0026-us-animal-disease-traceability-herd-assurance-reconciliation.md)
- [SYN-0025 — Agriculture lifecycle/system/threat/consequence reconciliation](syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)
- [SYN-0024 — Cross-sector portfolio reconciliation](syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [SYN-0023 — Engineering-biology/laboratory reconciliation](syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [CON-0001 — Cyberbiosecurity](../concepts/con-0001-cyberbiosecurity.md)
- [QUE-0001 — Domain boundaries](../questions/que-0001-domain-boundaries.md)
- [CTL-0003 — Example-applied assessment evidence boundary](../controls/ctl-0003-genomic-data-privacy-threat-modeling.md)
- [SYN-0008 — Five-context governance reconciliation](syn-0008-global-us-eu-uk-canada-governance-reconciliation.md)
- [GOV-0010 — U.S. One Health governance](../governance/gov-0010-us-national-one-health-framework-2025-2029.md)
- [GOV-0011 — Quadripartite implementation governance](../governance/gov-0011-quadripartite-one-health-jpa-national-guide.md)
- [SYN-0009 — Global/U.S. One Health scope reconciliation](syn-0009-global-us-one-health-scope-reconciliation.md)
- [GOV-0012 — NCI voluntary biobank governance](../governance/gov-0012-nci-best-practices-biospecimen-resources-2026.md)
- [AST-0005 — Laboratory/biobank assets and stakeholders](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md)
- [WFL-0009 — Biospecimen material/data lifecycle](../workflows/wfl-0009-biospecimen-material-data-lifecycle.md)
- [SYS-0007 — Biobank informatics/storage ecosystem](../systems/sys-0007-biobank-informatics-storage-ecosystem.md)
- [SYN-0010 — Laboratory/biobank reconciliation](syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md)
- [GOV-0013 — NIH IRP ELN governance](../governance/gov-0013-nih-intramural-electronic-laboratory-notebook-policy.md)
- [SYN-0011 — Laboratory/biobank system-boundary reconciliation](syn-0011-laboratory-biobank-system-boundary-reconciliation.md)
- [GOV-0014 — ISO 20387 biobanking-standard governance](../governance/gov-0014-iso-20387-biobanking-standard.md)
- [SRC-0026 — WHO LQMS functional/QMS handbook](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SYN-0013 — Clinical/public-health testing-lifecycle reconciliation](syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md)
- [SRC-0027 — APHL integrated laboratory/public-health informatics package](../sources/src-0027-aphl-integrated-laboratory-information-public-health-exchange.md)
- [SYS-0009 — Integrated CPH data-exchange architecture](../systems/sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md)
- [SYN-0014 — CPH system-boundary reconciliation](syn-0014-clinical-public-health-system-boundary-reconciliation.md)
- [SRC-0030 — HSSIB EPR systems thematic review](../sources/src-0030-hssib-electronic-patient-record-systems-thematic-review.md)
- [SYS-0010 — EPR safety dependencies](../systems/sys-0010-electronic-patient-record-safety-dependencies.md)
- [SYN-0015 — Clinical patient-outcome/system-evaluation reconciliation](syn-0015-clinical-patient-outcome-systems-evaluation-reconciliation.md)
- [SYN-0016 — Biomanufacturing four-cell reconciliation](syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)
- [SRC-0033 — NASEM AI/life-sciences report](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [AST-0008 — Biological AI assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [WFL-0011 — Biological AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [SYS-0011 — Biological AI ecosystem](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md)
- [RSK-0016 — Biological-AI output risk](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [CTL-0016 — Biological AI controls](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
- [GOV-0018 — NASEM advisory governance](../governance/gov-0018-nasem-ai-life-sciences-advisory-recommendations-2025.md)
- [SRC-0034 — ProteinGym empirical benchmark](../sources/src-0034-notin-proteingym-benchmark-2023.md)
- [SRC-0035 — UK PATH-SAFE evaluation and implementation package](../sources/src-0035-uk-path-safe-final-evaluation-2025.md)

## Sources

This page is an internal coverage methodology and artifact audit. External
factual support remains in each linked source note and its immutable raw
artifact; this synthesis is never evidence for a topic claim.

Baseline/current corpus source notes:

- [SRC-0001](../sources/src-0001-murch-cyberbiosecurity-2018.md)
- [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md)
- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md)
- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md)
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [SRC-0013](../sources/src-0013-us-eo-14292-biological-research-2025.md)
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [SRC-0020](../sources/src-0020-us-national-one-health-framework-2025-2029.md)
- [SRC-0021](../sources/src-0021-quadripartite-one-health-jpa-national-guide.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [SRC-0023](../sources/src-0023-nih-intramural-electronic-laboratory-notebook-policy.md)
- [SRC-0024](../sources/src-0024-iso-20387-biobanking-standard-current-status.md)
- [SRC-0025](../sources/src-0025-cap-biorepository-accreditation-program.md)
- [SRC-0026](../sources/src-0026-who-laboratory-quality-management-system-handbook.md)
- [SRC-0027](../sources/src-0027-aphl-integrated-laboratory-information-public-health-exchange.md)
- [SRC-0029](../sources/src-0029-nhs-england-national-patient-safety-alert-allergy-recording.md)
- [SRC-0030](../sources/src-0030-hssib-electronic-patient-record-systems-thematic-review.md)
- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md)
- [SRC-0032](../sources/src-0032-au-digital-agriculture-strategy-2024-2030.md)
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md)
- [GOV-0015](../governance/gov-0015-cap-biorepository-accreditation-program.md)
- [SYN-0012](syn-0012-global-canada-us-laboratory-biobank-governance-reconciliation.md)
