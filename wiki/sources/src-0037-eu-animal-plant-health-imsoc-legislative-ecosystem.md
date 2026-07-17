---
id: SRC-0037
type: source
title: EU Animal Health, Plant Health and IMSOC legislative ecosystem, current consolidated texts
aliases:
  - EU Animal Health Law and Plant Health Regulation with IMSOC
  - Regulations EU 2016/429, 2016/2031 and 2019/1715
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_type: official-eu-legislative-ecosystem
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/eu-plant-health-regulation-consolidated-2026-07-06.html
sha256: 152ce650a9563b32aefe729ba111fda59fa20111e47c060e3dec10b4e76d2835
raw_components:
  - path: ../../raw/eu-animal-health-law-consolidated-2021-04-21.html
    role: current-official-consolidated-animal-health-html
    sha256: ad09aca8d1d3a2c3ab7c9ad029299d02b875ed3a9b30a62947d5a359faeaf173
  - path: ../../raw/eu-animal-health-law-consolidated-2021-04-21.pdf
    role: current-official-consolidated-animal-health-pdf
    sha256: b9599b9b3897f7f845d98ff8b4b14490e16af17f81843e76cc5514976d5f046b
  - path: ../../raw/eu-imsoc-regulation-consolidated-2021-12-01.html
    role: current-official-consolidated-imsoc-html
    sha256: f559cdae7c57d0599a7b8b193d995036a7c69fa30f74f93a0ec6f4c7a5a26738
  - path: ../../raw/eu-imsoc-regulation-consolidated-2021-12-01.pdf
    role: current-official-consolidated-imsoc-pdf
    sha256: 499a65a81e95c5c9541dc4f94e0b56a9c30d73b4d335afdd7747ce97fe8fd1e9
  - path: ../../raw/eu-animal-health-law-authentic-oj-2016.pdf
    role: authentic-official-journal-animal-health-base-act
    sha256: f310f231f24eb3b6ef8afaf3d0783b6a4157112862452c2d7bc9e25adf1efb93
  - path: ../../raw/eu-plant-health-regulation-authentic-oj-2016.pdf
    role: authentic-official-journal-plant-health-base-act
    sha256: 5afba03fed1fa80ea94ab7c4d6eef9a34d88be7aa7dd20ecdcec42415222578b
  - path: ../../raw/eu-plant-health-amendment-2024-3115-authentic-oj.pdf
    role: authentic-official-journal-current-plant-health-amendment
    sha256: 8904bdc5c60c4b24a799a0d32bf1a08b69fd94c52edba6ff1da0480e9ac635ae
  - path: ../../raw/eu-imsoc-regulation-authentic-oj-2019.pdf
    role: authentic-official-journal-imsoc-base-act
    sha256: 71024ced03e9caa011e0aea30626a76d6e1fcd29a76a391973b085502f85b6df
  - path: ../../raw/eu-imsoc-amendment-2021-547-authentic-oj.pdf
    role: authentic-official-journal-current-imsoc-amendment
    sha256: 978f375b0d0add51b6d2430a771a83d603d6f8eaa8c89a4f66f0e313f3e409f8
animal_health_url: https://eur-lex.europa.eu/eli/reg/2016/429/2021-04-21/eng
plant_health_url: https://eur-lex.europa.eu/eli/reg/2016/2031/2026-07-06/eng
imsoc_url: https://eur-lex.europa.eu/eli/reg_impl/2019/1715/2021-12-01/eng
animal_health_authentic_oj_url: https://eur-lex.europa.eu/eli/reg/2016/429/oj/eng/pdf
plant_health_authentic_oj_url: https://eur-lex.europa.eu/eli/reg/2016/2031/oj/eng/pdf
plant_health_current_amendment_oj_url: https://eur-lex.europa.eu/eli/reg/2024/3115/oj/eng/pdf
imsoc_authentic_oj_url: https://eur-lex.europa.eu/eli/reg_impl/2019/1715/oj/eng/pdf
imsoc_current_amendment_oj_url: https://eur-lex.europa.eu/eli/reg_impl/2021/547/oj/eng/pdf
accessed: 2026-07-12
animal_health_consolidation_date: 2021-04-21
plant_health_consolidation_date: 2026-07-06
imsoc_consolidation_date: 2021-12-01
issuers:
  - European Parliament
  - Council of the European Union
  - European Commission
jurisdictions:
  - European Union
tags:
  - animal-health
  - plant-health
  - agriculture
  - traceability
  - surveillance
  - movement
  - imsoc
  - traces
  - adis
  - europhyt
  - legislation
---

# EU Animal Health, Plant Health and IMSOC legislative ecosystem

## Identity, acquisition and complete review

The package retains the official EUR-Lex current consolidated English texts
available on 2026-07-12 for Regulation (EU) 2016/429 (Animal Health Law),
Regulation (EU) 2016/2031 (protective measures against plant pests) and
Commission Implementing Regulation (EU) 2019/1715 (IMSOC Regulation).

- The current plant-health HTML is 5,978,413 bytes and identifies consolidation
  `02016R2031-20260706`. The corresponding current ELI PDF endpoint returned an
  HTML response at review time, so no file was mislabeled or used as a PDF.
- The animal-health HTML/PDF are 1,632,080 and 2,318,978 bytes; the 236-page
  PDF identifies consolidation `02016R0429-20210421`.
- The IMSOC HTML/PDF are 9,983,435 and 1,533,839 bytes; the 72-page PDF
  identifies consolidation `02019R1715-20211201`.
- Five additional authentic Official Journal PDFs retain the 208-page Animal
  Health base act, 101-page Plant Health base act, 13-page Regulation
  2024/3115 plant-health amendment, 60-page IMSOC base act and 11-page
  Implementing Regulation 2021/547 amendment.
- The ten retained objects total 33,192,799 bytes. Repeat animal/IMSOC PDF
  retrievals were byte-identical. Repeat HTML bytes differed in dynamic page
  material, but complete statically extracted visible text was byte-identical;
  the comparison copies remained temporary.
- Every current animal-health and IMSOC PDF page and the complete current
  plant-health HTML text were reviewed, including article structure, amendment
  markers, annexes, exceptions and final provisions. The five authentic OJ
  PDFs were text-extracted and their force/application and relevant base/
  amendment provisions were cross-checked against the consolidations. The
  animal and IMSOC consolidated PDFs are
  tagged, unencrypted PDF 1.7 without forms or reported JavaScript. Neither
  reported a signature; `pdfsig` emitted an NSS warning, so this is not
  cryptographic authentication.
- Each retained EUR-Lex HTML contains 60 script and five form elements and no
  iframe/object/embed found by static tag count. Nothing was executed or
  submitted; this is an artifact observation, not a runtime-security finding.

> **Claim record — SRC-0037-C01 | artifact-observation**
> **Claim:** The retained 33,192,799-byte package contains complete official
> current-consolidated EUR-Lex representations of all three instruments plus
> authentic Official Journal base/final-provision texts and selected date-
> driving plant/IMSOC amenders used for force/application checks, with format,
> repeat-retrieval and static-safety limits recorded.
> **Claim status:** active
> **Scope:** Retained artifacts and complete-review process; not legal advice,
> cryptographic authentication or runtime assurance of EUR-Lex.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Ten raw objects, byte counts and hashes above; PDF metadata,
> complete extracted text, static tag counts and repeat comparisons.
> **Basis / limits:** Object identity and review are directly reproducible.
> Dynamic HTML bytes are not represented as byte-stable. The package is not a
> complete authentic amendment/corrigendum lineage; current integrated wording
> is represented by the official but non-authentic consolidations.

## Legal force, currentness and lineage

The three instruments are one connected EU legislative ecosystem, not three
independent jurisdictions or empirical studies. The Animal Health and Plant
Health Regulations were adopted by the Parliament and Council; the IMSOC
implementing regulation was adopted by the Commission under the official-
controls framework. EUR-Lex marks each act in force and exposes the
consolidation dates above.

Consolidated texts are documentation tools and are not the authentic legal
versions; authentic acts and amendments are those published in the Official
Journal. Consolidation dates do not make every underlying provision newly
effective on that date, and delegated/implementing measures, national
penalties, derogations and staged application remain relevant.

> **Claim record — SRC-0037-C02 | source-report**
> **Claim:** EUR-Lex presents the three regulations as in-force EU instruments
> with current consolidations dated 2021-04-21, 2026-07-06 and 2021-12-01,
> while the consolidated representations themselves carry a non-authentic
> documentation-tool boundary.
> **Claim status:** active
> **Scope:** Instrument class, issuer, in-force/current-consolidation status and
> consolidation disclaimer on 2026-07-12; not interpretation of every
> amendment, national implementation or legal compliance.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** EUR-Lex document-information/current-version panels and
> consolidated-text headers for `02016R0429-20210421`,
> `02016R2031-20260706` and `02019R1715-20211201`; authentic Animal Article
> 283, Plant Article 113 and IMSOC Article 48 plus the retained 2024/3115 and
> 2021/547 amendment texts.
> **Basis / limits:** Status/date markers are direct. The three texts count as
> one EU legal ecosystem for independence floors.

## Animal-health assets, actors and responsibility envelope

The Animal Health Law directly represents terrestrial, aquatic/aquaculture,
wild and kept animals; germinal products, animal-origin and by-product classes;
establishments, epidemiological units, zones and compartments; movements and
means of transport; vaccines/diagnostic reagents; samples, laboratory results,
identification and movement records; computerised databases and TRACES. Roles
include operators, transporters, animal professionals, veterinarians, official
laboratories, competent authorities, Member States, Commission bodies and
affected animal/public-health interests.

> **Claim record — SRC-0037-C03 | source-report**
> **Claim:** The Animal Health Law supplies a direct asset/stakeholder map for
> animals, group identification, epidemiological-unit/establishment records
> and aquaculture/wildlife contexts, germinal/material/product
> classes, establishments/transport, identification/records/databases,
> laboratories and operator/veterinary/authority/public-health roles.
> **Claim status:** active
> **Scope:** Classes directly represented by Regulation 2016/429; not one farm
> inventory, genome map, sensor topology, consumer-outcome study or deployment
> validation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Animal Health Law Articles 2–4, 10–17, 43–52, 84–123 and the
> corresponding terrestrial/aquatic registration, identification, record and
> movement provisions in Parts IV–VI.
> **Basis / limits:** Named classes and roles are direct. `Herd` is not an
> operative term and is not silently equated with animal groups,
> establishments, epidemiological units or species-scoped databases.

## Animal-health lifecycle and control states

The functional lifecycle spans operator biosecurity/prevention; notification;
surveillance, sampling, laboratory examination and reporting; preparedness,
contingency and vaccination resources; suspicion/confirmation; epidemiological
enquiry; restriction, movement control, identification/traceability,
vaccination/treatment, slaughter where applicable, cleaning and disposal;
continued surveillance, repopulation/restoration and review. Registration,
approval, movement certification and records run through routine operation.

> **Claim record — SRC-0037-C04 | source-report**
> **Claim:** Regulation 2016/429 directly covers breeding/keeping and routine
> operation, diagnostics/surveillance, treatment/vaccination, regulated
> movement/trade/traceability, outbreak response, disposal and bounded
> restoration/repopulation stages.
> **Claim status:** active
> **Scope:** Legal functional stages and conditional measures; not one species-
> specific procedure, guaranteed action order, observed outbreak, ecological
> outcome or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Animal Health Law Articles 10–17, 18–30, 43–52, 53–83,
> 84–123 and relevant movement/certification Parts IV–VI; especially Articles
> 61–71 for sampling, movement, treatment/vaccination, traceability, cleaning,
> disposal, continued surveillance and restoration conditions.
> **Basis / limits:** Lifecycle predicates are direct but conditional and
> species/disease dependent; adoption and outcome evidence are absent.

## Plant-health assets and lifecycle

The current Plant Health Regulation defines plants to include seeds intended
for planting, tissue cultures and germplasm; plant products, wood/packaging,
lots/trade units, plants for planting, other objects, pests, professional/
registered/authorised operators, final users, quarantine/confinement facilities
and traceability codes. It covers production and breeding, notification,
official-laboratory confirmation, survey/sampling/testing, contingency and
simulation, eradication/containment, movement/trade, operator registers,
traceability, passports/certificates, treatment and destruction/disposition.

> **Claim record — SRC-0037-C05 | source-report**
> **Claim:** Regulation 2016/2031 supplies direct seed/planting-material,
> production-operator, lot/traceability, laboratory/authority and plant-
> environment asset classes plus breeding/production→surveillance/testing→
> movement/trade/traceability→response/treatment/destruction lifecycle stages.
> **Claim status:** active
> **Scope:** Plant-health legal objects/stages; not farm OT, a seed-genome
> database, observed pest event, environmental-monitoring implementation or
> measured effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Plant Health Regulation Articles 1–2, 8–27, 40–70, 78–104;
> especially Articles 2, 10, 17–27, 60–70, 78–95 and 100–104.
> **Basis / limits:** Classes/stages and exceptions are direct. Environmental
> consequence language is risk scope, not environmental-sampling evidence.

## IMSOC architecture, boundaries and responsibility

IMSOC comprises iRASFF, ADIS, EUROPHYT and TRACES. It defines networks,
contact points, national systems, governance, member ownership/responsibility,
links between components, standards-based exchange with national/external
systems, Commission maintenance, access restrictions, controllers/security,
notification workflows, certificate/signature/seal predicates, retention and
contingency arrangements. ADIS links animal notifications; EUROPHYT links
plant outbreaks; TRACES exchanges certificates, consignment decisions and
follow-up states.

> **Claim record — SRC-0037-C06 | source-report**
> **Claim:** The IMSOC Regulation directly maps animal/plant surveillance and
> traceability architecture across iRASFF, ADIS, EUROPHYT, TRACES, Member-
> State/national systems, networks/contact points, authority/operator access,
> cross-component interfaces, certificates, responsibility, retention and
> outage/reconciliation boundaries.
> **Claim status:** active
> **Scope:** Legal system/component and trust-boundary model; not deployed
> network topology, live IAM configuration, protocol implementation, service-
> level performance, validation or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** IMSOC Regulation Articles 1–11, 12–46; especially Articles
> 2–11, 29–37 and 39–46.
> **Basis / limits:** Named components, roles and exchanges are direct.
> `EUROPHYT outbreak` is a notification class, not a cyber incident.

## Safe functional directions

The ecosystem directly supports intended bidirectional functions. Biological/
material observations or samples can become laboratory results, surveillance/
notification records and authority decisions in ADIS/EUROPHYT/TRACES. In the
other direction, an authorized digital certificate, notification or control
decision can condition physical movement, inspection, restriction, treatment,
response or disposition. Neither direction is a hostile cyber event.

> **Claim record — SRC-0037-C07 | source-report**
> **Claim:** The package contains complete intended animal/plant observation-
> or sample→laboratory/digital notification→authority-decision and authorized
> digital decision/certificate→physical movement/control-action directions.
> **Claim status:** active
> **Scope:** Intended legal/operational functions at safe abstraction; not a
> hostile path, autonomous authority, observed incident, outcome or reliable
> implementation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Animal Articles 17–30, 53–71 and movement/certification Parts;
> Plant Articles 9–27, 69–104; IMSOC Articles 3–11, 29–46.
> **Basis / limits:** Both functional directions are explicit inside one EU
> legal ecosystem; independent SF2 transfer corroboration remains separate.

## Exact-edge controls and evidence maturity

Animal controls include operator biosecurity, notification, surveillance,
laboratory confirmation, contingency, movement restriction, identification/
traceability, vaccination/treatment, disposal, cleaning and restoration
conditions. Plant controls include operator/authority notification,
confirmation, survey/testing, eradication/containment, registers, traceability,
passports, critical-point plans, inspection, invalidation and destruction.
IMSOC adds named responsibility, standards-based exchange, scoped access,
security/controller duties, signatures/seals, retention and contingency data
reconciliation.

> **Claim record — SRC-0037-C08 | source-report**
> **Claim:** The three regulations map biosecurity, traceability,
> detection/notification, response and resilience/continuity controls to exact
> animal, plant, record, movement, certificate and system-outage edges.
> **Claim status:** active
> **Scope:** Binding legal/control design within stated scope and exceptions;
> not organization-specific implementation, test, audit result, compliance or
> independent effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Animal Articles 10, 16–30, 43–71, 84–123; Plant Articles
> 9–27, 60–70, 78–95, 103–104; IMSOC Articles 4–11, 29b, 32, 36–46.
> **Basis / limits:** Edge/control predicates are direct. Effectiveness and
> actual compliance are not inferred from law or system design.

## Privacy, continuity, exceptions and adoption boundary

IMSOC assigns data ownership, joint controllership, security and access roles;
uses signatures/seals and retention limits; and defines contingency capture and
later reconciliation when ADIS/TRACES or national functions are unavailable.
Animal and plant regimes contain numerous risk-, species-, movement-, final-
user-, low-risk-operator- and scientific-use derogations. Member States retain
roles in authorities, penalties and implementation.

> **Claim record — SRC-0037-C09 | source-report**
> **Claim:** The ecosystem explicitly records data/access/security,
> integrity/signature, retention, contingency/reconciliation and scoped
> derogation predicates, but provides no corpus-wide implementation or outcome
> evaluation.
> **Claim status:** active
> **Scope:** Direct legal design and exception/evidence boundary; not GDPR
> compliance analysis, live security assessment, adoption metric or proof of
> resilience.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** IMSOC Articles 5–11, 28, 29b, 34, 36–46; Animal and Plant
> scope/derogation/record provisions cited in `C03`–`C08`.
> **Basis / limits:** The law states duties/design. No audit, exercise or
> independently evaluated outcome is contained in this package.

## Frozen-rubric contribution

This transaction fills direct EU seed and species-scoped animal-group/
epidemiological-unit/establishment-record, treatment/movement/
disposition, official-laboratory/traceability-platform and exact-control
evidence gaps. It remains one legal ecosystem. Existing independent AU,
PATH-SAFE, Drape, U.S. and One Health lineages require explicit reconciliation
before any AGE cell changes.

> **Claim record — SRC-0037-C10 | artifact-observation**
> **Claim:** `SRC-0037` alone changes no frozen cell: `AGE-AS/WL/SD/CT` gain
> strong direct candidate evidence but remain Partial pending criterion-level
> independent synthesis; `AGE-TV/XT/CI/AE` and all global gates are unchanged.
> **Claim status:** active
> **Scope:** Wiki after this source transaction; not an external domain-
> completeness or legal-evidence claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0037-C01`–`C09`; frozen AGE criteria/source floors in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md); existing AGE pages.
> **Basis / limits:** One EU ecosystem cannot create independent SF2 by page or
> regulation count; no cell receives a point from vocabulary alone.

## Safety boundary

The page retains only public legal object, actor, lifecycle, architecture and
defensive-control classes. It omits farm/facility locations, animal/plant/
sample records, operational identifiers, credentials, live endpoints,
laboratory parameters and misuse-enabling procedural detail.

> **Claim record — SRC-0037-C11 | analytic-judgment**
> **Claim:** The retained abstraction is defensive and does not expose
> personal, facility, biological-content or actionable operational detail.
> **Claim status:** active
> **Scope:** Local source note; not a downstream-use guarantee for every
> external legal annex or linked resource.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0037-C01`–`C10`; local page content.
> **Basis / limits:** Article-level public legal functions remain useful.

## Integration map

- [AST-0009 — animal/plant-health assets and stakeholders](../assets/ast-0009-animal-plant-health-assets-stakeholders.md)
- [WFL-0012 — surveillance/movement/response lifecycle](../workflows/wfl-0012-animal-plant-health-surveillance-movement-response-lifecycle.md)
- [SYS-0012 — EU IMSOC architecture](../systems/sys-0012-eu-animal-plant-health-imsoc-architecture.md)
- [CTL-0017 — traceability/notification/response controls](../controls/ctl-0017-animal-plant-health-traceability-notification-response-controls.md)
- [GOV-0020 — EU animal/plant/IMSOC governance](../governance/gov-0020-eu-animal-plant-health-imsoc-legislation.md)
- [AST-0003 — existing smart-farm assets](../assets/ast-0003-smart-farm-production-and-supply-assets.md)
- [WFL-0007 — existing smart-farm lifecycle](../workflows/wfl-0007-smart-farm-monitoring-production-supply.md)
- [SYS-0005 — existing connected-farm system](../systems/sys-0005-connected-smart-farm-ecosystem.md)
- [CTL-0005 — existing agriculture controls](../controls/ctl-0005-agricultural-cyberbiosecurity-capability-controls.md)
- [SYN-0025 — agriculture lifecycle/system/control reconciliation](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)
- [SYN-0026 — herd and traceability-assurance reconciliation](../syntheses/syn-0026-us-animal-disease-traceability-herd-assurance-reconciliation.md)

## Official links

- Animal Health Law current consolidated text: <https://eur-lex.europa.eu/eli/reg/2016/429/2021-04-21/eng>
- Animal Health Law authentic OJ base PDF: <https://eur-lex.europa.eu/eli/reg/2016/429/oj/eng/pdf>
- Plant Health Regulation current consolidated text: <https://eur-lex.europa.eu/eli/reg/2016/2031/2026-07-06/eng>
- Plant Health Regulation authentic OJ base PDF: <https://eur-lex.europa.eu/eli/reg/2016/2031/oj/eng/pdf>
- Plant Health current amendment 2024/3115 authentic OJ PDF: <https://eur-lex.europa.eu/eli/reg/2024/3115/oj/eng/pdf>
- IMSOC Regulation current consolidated text: <https://eur-lex.europa.eu/eli/reg_impl/2019/1715/2021-12-01/eng>
- IMSOC authentic OJ base PDF: <https://eur-lex.europa.eu/eli/reg_impl/2019/1715/oj/eng/pdf>
- IMSOC amendment 2021/547 authentic OJ PDF: <https://eur-lex.europa.eu/eli/reg_impl/2021/547/oj/eng/pdf>
