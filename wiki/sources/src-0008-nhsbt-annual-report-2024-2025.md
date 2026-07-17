---
id: SRC-0008
type: source
title: NHS Blood and Transplant Annual Report and Accounts 2024–25
aliases:
  - NHSBT Annual Report 2024–25
  - HC 1095
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: official-disclosure
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/nhsbt-annual-report-accounts-2024-2025.pdf
sha256: f39dd82b7a4e42cca3bf6451dc83aedb6b6f8adda403b6b7010e8e344c74e8e8
canonical_url: https://www.gov.uk/government/publications/nhs-blood-and-transplant-annual-report-and-accounts-2024-to-2025
download_url: https://assets.publishing.service.gov.uk/media/6878a0f80263c35f52e4dcd3/nhsbt-annual-report-and-accounts-2024-to-2025.pdf
accessed: 2026-07-12
transient: true
issuer: NHS Blood and Transplant
publication_date: 2025-07-17
reporting_period_start: 2024-04-01
reporting_period_end: 2025-03-31
isbn: 978-1-5286-5880-5
jurisdictions:
  - England
  - United Kingdom
tags:
  - transfusion
  - laboratory-systems
  - blood-supply
  - clinical-continuity
  - incident-disclosure
  - implemented-control
---

# NHS Blood and Transplant Annual Report and Accounts 2024–25

## Bibliographic identity

NHS Blood and Transplant. *Annual Report and Accounts 2024–25*. HC 1095;
SG/2025/107; ISBN `978-1-5286-5880-5`. Presented to Parliament and ordered to
be printed 17 July 2025.

This is an institutional annual report and official first-party disclosure.
NHSBT directly reports its operational response to the June 2024 Synnovis
cyberattack, its transfusion/pathology services, implemented digital changes,
business-continuity state and internal/external assurance. It is primary for
NHSBT's own response and observed service/stock effects, but secondary for the
mechanics inside Synnovis. It is not a forensic report and does not
independently establish the attack actor, entry vector, exploited vulnerability
or patient harm.

## Provenance

- Immutable artifact:
  `../../raw/nhsbt-annual-report-accounts-2024-2025.pdf`, 5,499,567 bytes,
  PDF 1.7, 144 physical pages, SHA-256
  `f39dd82b7a4e42cca3bf6451dc83aedb6b6f8adda403b6b7010e8e344c74e8e8`.
- Retrieved from the official GOV.UK asset URL on 2026-07-12. The GOV.UK record
  identifies NHS Blood and Transplant, publication date 2025-07-17, England
  applicability, 144 pages, ISBN, HC and document reference.
- The PDF is unencrypted and has no JavaScript, XFA, digital signature or
  embedded files. Its catalog has an empty AcroForm field array and an
  `OpenAction` that is an ordinary `GoTo` to the first page; neither was
  executed.
- Pagination: physical pp. 1–5 are cover/blank/title/copyright/contents.
  Numbered p. 6 is physical p. 6, and numbered pp. 6–140 therefore equal PDF
  physical pages. Physical pp. 141–144 are blank/end matter/back cover.
- Fully reviewed: cover and publication identity; performance report pp. 6–48;
  remuneration/staff report pp. 49–65; corporate-governance report pp. 66–80;
  governance statement pp. 81–98; parliamentary accountability pp. 99–101;
  C&AG certificate pp. 102–106; financial statements and notes pp. 107–140;
  all rendered tables/figures relevant to cyberbiosecurity and the final blank/
  cover pages.

## Executive summary

The report supplies a primary operationally involved account of a documented
cyber-to-clinical/material pathway. In June 2024, a cyberattack on external
pathology provider Synnovis disrupted access to systems supporting blood
grouping, antibody screening and crossmatching. NHSBT reports that its Red Cell
Immunohaematology service expanded operations, extended hours and prioritized
urgent cases; it says this maintained compatibility-testing support and
continuity of transfusion care. The same disruption increased reliance on
O-negative units, pressured a limited biological inventory and contributed to
an amber stock alert.

This evidence supports an `INC`, an observed `RSK` and an implemented
continuity `CTL`. The effectiveness statement remains first-party and bounded
to the reported response: the report does not quantify cases served, compare a
counterfactual, disclose independent operational evaluation or establish that
no patient was harmed across the wider Synnovis incident.

The report also documents a live analyser-to-HAEMATOS automatic result-transfer
programme, operational molecular-genotype testing and extensive governance/
assurance context. It simultaneously discloses weaknesses: a `Limited` internal
audit opinion for disaster-recovery planning of a critical ICT system and open
minor non-conformities against reported ISO 22301 certification.

## Claims and locators

> **Claim record — SRC-0008-C01 | artifact-observation**
> **Claim:** The archived artifact is the official 144-page NHSBT Annual Report
> and Accounts 2024–25 published on GOV.UK, with the recorded identity, size and
> SHA-256.
> **Claim status:** active
> **Scope:** Local artifact and official publication record checked 2026-07-12.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** artifact provenance above; title/publication pages physical
> pp. 1–4; GOV.UK publication record.
> **Basis / limits:** Hash, metadata, page count and official identity are
> direct observations. The web record is volatile; substantive historical
> content is reproducible from the immutable PDF.

> **Claim record — SRC-0008-C02 | source-report**
> **Claim:** NHSBT's operating model couples donor/material collection,
> manufacturing, testing and distribution with specialist pathology services,
> including Red Cell Immunohaematology, and digital/data support.
> **Claim status:** active
> **Scope:** NHSBT functions and reporting segments in 2024–25, not a universal
> transfusion architecture.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** pp. 9–10, 20–24 and 122–125.
> **Basis / limits:** Functions and service segments are directly reported.
> The report does not publish a complete patient/sample/product event model,
> deployed network topology or interface assurance.

> **Claim record — SRC-0008-C03 | source-report**
> **Claim:** NHSBT reports that a June 2024 cyberattack on Synnovis disrupted
> access to laboratory systems for blood grouping, antibody screening and
> crossmatching, increased reliance on O-negative blood and contributed to an
> amber stock alert.
> **Claim status:** active
> **Scope:** The external pathology disruption and NHSBT-observed transfusion/
> supply consequences; not a forensic attribution or confirmed patient injury.
> **As of:** 2024-06.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** pp. 21–22 and 97; financial-response context p. 44.
> **Basis / limits:** NHSBT directly describes the gap and its own stock/service
> consequences. The report names no actor, malware/ransomware class, entry
> vector, exploited weakness, affected-host count, patient-level record or
> confirmed injury. `Serious risk to patient safety` is a risk statement.

> **Claim record — SRC-0008-C04 | source-report**
> **Claim:** NHSBT reports that its Red Cell Immunohaematology team scaled
> operations, extended working hours and prioritized urgent cases to support
> affected hospitals, and states that clinicians could continue safe
> transfusion in emergency and surgical settings.
> **Claim status:** active
> **Scope:** Implemented response during the reported Synnovis disruption, not
> a general effectiveness guarantee.
> **As of:** 2024-06.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** pp. 22 and 97; business-continuity account p. 92.
> **Basis / limits:** Actions and source-reported continuity are direct.
> Case volume, time-to-service, control baseline, test design, adverse outcomes
> and counterfactual are absent. The statement is not independently evaluated.

> **Claim record — SRC-0008-C05 | source-report**
> **Claim:** NHSBT reports an implemented Automated Results Transfer capability
> that moves analyser results into its HAEMATOS laboratory information system,
> with an initial two-process rollout and work progressing on six more
> processes in 2024–25.
> **Claim status:** active
> **Scope:** NHSBT pathology result transfer; not a complete LIMS architecture
> or measured error-reduction study.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** pp. 20 and 23.
> **Basis / limits:** The live initial rollout and expansion status are direct.
> The report says automation reduces transcription risk, but supplies no error
> baseline, observed reduction, security assessment, interface validation or
> proof that all six additional processes were live.

> **Claim record — SRC-0008-C06 | source-report**
> **Claim:** NHSBT reports performing more than 5,300 extended blood-group
> genotype tests during 2024–25 to support transfusion matching for patients
> with sickle cell disorder, thalassaemia and other rare anaemias.
> **Claim status:** active
> **Scope:** One operational English clinical programme, not all genomics or a
> comparative effectiveness study.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** pp. 30–31.
> **Basis / limits:** Programme, population context and count are direct.
> The report's safer/more-effective language is not accompanied by validation
> accuracy, matching-outcome, adverse-event or independent evaluation data.

> **Claim record — SRC-0008-C07 | source-report**
> **Claim:** NHSBT reports standing up its critical-incident process 21 times
> while maintaining key products/services, acting as a LIMS contingency during
> the south-London event, carrying open minor ISO 22301 non-conformities and
> receiving a `Limited` internal-audit opinion for disaster-recovery planning of
> a critical ICT system.
> **Claim status:** active
> **Scope:** NHSBT's 2024–25 continuity and assurance disclosures; the ISO
> certificate and underlying audit reports were not independently ingested.
> **As of:** 2025-03-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** pp. 77, 91–92 and 95–96.
> **Basis / limits:** Counts, reported state and audit rating are direct from
> the annual report. They do not show which critical system had the weakness,
> whether every activation met objectives or whether ISO non-conformities were
> later closed. System-specific weakness is not exposed here.

> **Claim record — SRC-0008-C08 | analytic-judgment**
> **Claim:** The C&AG certificate supports financial-statement and regularity
> conclusions plus limited consistency/material-misstatement checks on other
> information; it does not independently assure the Synnovis narrative or the
> effectiveness of NHSBT's continuity response.
> **Claim status:** active
> **Scope:** Assurance boundary of this compound annual-report artifact.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** C&AG certificate pp. 103–106, especially `Other Information`
> and `Opinion on other matters`, p. 104; incident accounts pp. 22 and 97.
> **Basis / limits:** The certificate explicitly says the financial opinion
> does not cover other information and no assurance conclusion is expressed
> except as stated. Reading/consistency work is useful but is not operational
> control testing or forensic corroboration.

## Scope and methods

### Operational and clinical reporting

The performance report describes NHSBT's blood, plasma, pathology, cellular/
gene therapy, organ/tissue and digital programmes against 2024–25 objectives.
The governance statement adds principal risks, committees, clinical audit,
quality management, business continuity, data/cyber reporting, internal audit
opinions and the accounting officer's review of control effectiveness.

This makes the source unusually valuable across asset, workflow, system,
incident, response and assurance layers. All performance and incident findings
remain statements of NHSBT management unless the page explicitly attributes an
internal/external auditor or regulator.

### Audit layers

- The report attributes a `Moderate` overall governance/risk/control opinion
  and individual engagement ratings to the Government Internal Audit Agency.
- It reports external regulatory/accreditation inspections and ISO/DCB status,
  but underlying certificates and inspection reports are not part of this
  artifact.
- The statutory C&AG audit directly covers the financial statements,
  regularity and specifically audited report sections. The operational
  narrative is read for consistency/material misstatement; no general assurance
  conclusion is provided over it.

## Limitations and conflicts

- NHSBT is an operational participant/respondent but not Synnovis. Its report
  is primary for NHSBT actions and observed demand/stock effects, not for
  initial compromise, root cause or full affected-provider recovery.
- The report does not identify ransomware, an actor, an exploited
  vulnerability or exact event date. Those details require separate official
  sources and must not be imported from memory.
- Page 92 refers generically to an attack on hospital LIMS in south London,
  while p. 23 separately identifies HAEMATOS as NHSBT's own laboratory
  information system. The report does **not** say that HAEMATOS or NHSBT was
  compromised; these system contexts must remain separate.
- `Serious risk to patient safety` does not mean confirmed patient injury.
  The continuity statement does not establish that no patient was harmed in the
  wider incident.
- The RCI response was implemented and exercised during a real disruption. Its
  effectiveness is **source-reported for one event**, not causally or
  independently evaluated.
- ISO 22301, DCB1596 and regulatory/accreditation status are organization-
  reported until their direct records are ingested. Open non-conformities and
  a `Limited` disaster-recovery opinion prevent treating certification as
  complete control effectiveness.
- Page 92 visibly reports an impossible `889 per cent` FOI response rate. The
  wiki records this as a production defect and does not silently correct or use
  the metric. The same page says `94 per cent` of six high-severity alerts were
  responded to compliantly/timely; without a disclosed denominator method that
  percentage cannot be reconstructed from six alerts and is not used.
- Page 31's `17 per cent` statement about transfusion side effects from
  incomplete matching has no citation or disclosed method and is not used as
  prevalence evidence. Other production defects include duplicated
  `directions directions` on p. 105 and malformed text on p. 133.
- The p. 98 accounting-officer statement that effective control was maintained
  is read with, not above, the p. 47–48 critical-ICT risk at `Risk Limit`, the
  p. 91 overall `Moderate` assurance, partially met functional standards and
  p. 95 `Limited` disaster-recovery finding. These can coexist at different
  scopes, but they do not support “independently proven effective controls.”
- The page-92 serious data-security incident is unnamed and must not be merged
  with Synnovis. Aggregated counts of 17 cyber and 276 data-security incidents
  do not justify separate incident entities.
- The report describes AI products as integrated platform capabilities,
  exploration, development or governance formation; it does not establish a
  validated AI-security lifecycle or effectiveness.
- Operational system detail is retained only at functional level. No access
  path, network topology or critical-ICT system weakness is published in the
  wiki.

## Version status

The official GOV.UK record, accessed 2026-07-12, lists this as the final annual
report published 2025-07-17 and shows no update after publication. The report
is historical for the year ending 2025-03-31. Any present-tense certification,
programme, governance or remediation state must be rechecked by the review
date; event-history claims remain tied to their stated period.

## Integration map

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [AST-0002](../assets/ast-0002-transfusion-compatibility-and-blood-products.md) —
  compatibility information and blood-component availability as coupled
  digital/biological assets.
- [WFL-0006](../workflows/wfl-0006-transfusion-compatibility-and-blood-issue.md) —
  bounded compatibility-testing and product-issue workflow.
- [SYS-0004](../systems/sys-0004-transfusion-laboratory-information-systems.md) —
  functional laboratory/result-transfer systems and service dependencies.
- [INC-0001](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md) —
  documented event with primary NHSBT response evidence.
- [RSK-0006](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md)
  — observed cyber→laboratory→inventory/clinical consequence path.
- [CTL-0004](../controls/ctl-0004-transfusion-service-continuity-response.md) —
  implemented and real-event-exercised continuity response, with bounded
  first-party effectiveness evidence.
- [AST-0001](../assets/ast-0001-genomic-data.md) and
  [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) — operational clinical
  genotyping context from an independent institutional lineage.
- [SYN-0006](../syntheses/syn-0006-official-control-function-state-taxonomy.md) —
  uses the bounded continuity response only as an implemented-state example,
  not as framework adoption or independent effectiveness evidence.
- [AST-0006](../assets/ast-0006-clinical-public-health-laboratory-assets-stakeholders.md) —
  operational analyser/LIS and clinical-service asset context.
- [WFL-0010](../workflows/wfl-0010-clinical-laboratory-testing-reporting-correction-lifecycle.md) —
  observed availability interruption/continuity overlay.
- [RSK-0013](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md) —
  observed availability branch, not result corruption or patient injury.
- [CTL-0012](../controls/ctl-0012-clinical-laboratory-quality-reporting-continuity-controls.md) —
  implemented downtime response with effectiveness limits.
- [SYN-0013](../syntheses/syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md) —
  bounded operational lineage in the CPH criterion reconciliation.
- [SYS-0009](../systems/sys-0009-integrated-clinical-public-health-laboratory-data-exchange.md)
  and [SYN-0014](../syntheses/syn-0014-clinical-public-health-system-boundary-reconciliation.md) —
  bounded implemented result-transfer evidence in the CPH architecture/state
  reconciliation, not complete architecture or effectiveness.
- [SYN-0015](../syntheses/syn-0015-clinical-patient-outcome-systems-evaluation-reconciliation.md) —
  service/material consequence comparator that remains distinct from evidenced
  biological patient harm.
- No `THR`, `TEC` or `VUL` is created; actor, vector and weakness are unknown.
- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)
- [SYN-0022 — Foundational consequence/assurance calibration](../syntheses/syn-0022-foundational-consequence-assurance-calibration.md)
- [SYN-0023 — Laboratory continuity reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
