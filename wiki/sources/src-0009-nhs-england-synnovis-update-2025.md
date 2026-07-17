---
id: SRC-0009
type: source
title: NHS England Synnovis cyber incident update, 10 November 2025
aliases:
  - NHS England Synnovis cyber incident page
  - Synnovis cyber incident update 2025
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: official-disclosure
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/nhs-synnovis-cyber-incident-2025.html
sha256: d198ee3b0d1c42d240346ccf4cd124be8c807be75423e02c07e68710176ac0b7
canonical_url: https://www.england.nhs.uk/synnovis-cyber-incident/
accessed: 2026-07-12
transient: true
issuer: NHS England
publication_date: 2024-06-25
displayed_update_date: 2025-11-10
api_modified_at: 2025-11-10T08:14:57Z
jurisdictions:
  - England
  - United Kingdom
tags:
  - synnovis
  - ransomware
  - pathology
  - clinical-continuity
  - data-breach
  - incident-disclosure
---

# NHS England Synnovis cyber incident update, 10 November 2025

## Bibliographic identity

NHS England. *Synnovis cyber incident*. The archived page identifies its
substantive text as an “Update on the Synnovis cyber incident: 10 November
2025”. No separate original-publication timestamp or revision history is
exposed in the HTML. The official WordPress API record for page `248048`
reports publication at `2024-06-25T07:56:40Z` and modification at
`2025-11-10T08:14:57Z`; this metadata endpoint is transient and was checked on
2026-07-12.

This is an official health-system disclosure. It is primary for NHS England's
published incident chronology, aggregate service impact, recovery statement
and notification process. It is not a forensic report, clinical-outcomes study
or independent effectiveness evaluation. NHS England and NHSBT are distinct
issuers, but both participated in the same NHS response ecosystem; agreement
between `SRC-0008` and this page improves institutional corroboration without
creating independent technical attribution.

## Provenance

- Immutable local snapshot:
  `../../raw/nhs-synnovis-cyber-incident-2025.html`, 35,726 bytes, SHA-256
  `d198ee3b0d1c42d240346ccf4cd124be8c807be75423e02c07e68710176ac0b7`.
- Canonical official page:
  <https://www.england.nhs.uk/synnovis-cyber-incident/>; accessed and checked
  2026-07-12. The live response was byte-identical to the archived snapshot at
  that check, including the displayed 10 November 2025 update.
- Official transient metadata companion:
  `https://www.england.nhs.uk/wp-json/wp/v2/pages/248048`, page ID `248048`,
  `date_gmt` 2024-06-25T07:56:40 and `modified_gmt`
  2025-11-10T08:14:57; checked 2026-07-12. This API response was not archived
  and is used only for page publication/modification metadata.
- The UTF-8 HTML contains one substantive `<article>`, 20 script tags, one
  site-search form, no iframe and no object/embed element. Scripts, forms and
  linked content were not executed; the article was reviewed statically.
- Fully reviewed: document head/canonical identity, navigation, all article
  headings and paragraphs, outbound-link labels and footer. The linked public
  Q&A, NCSC guidance, NHS London news and Synnovis site are separate candidate
  sources and are not part of this ingest.
- `ingest_status: complete` applies to this single archived page. It does not
  imply that the linked investigations, customer records or notification
  materials were accessible.

## Executive summary

NHS England dates the ransomware attack to 3 June 2024 and reports a material
availability and confidentiality incident at pathology provider Synnovis. It
says service capacity was significantly reduced, more than 11,000 outpatient
and elective-procedure appointments were delayed, and services were fully
restored by December 2024. Separately, it reports that stolen files were
published on 20 June 2024 and describes a later customer/individual-impact
review and notification process.

The source strengthens `INC-0001` by supplying an exact event date, an official
ransomware classification, an aggregate care-delivery delay measure, a bounded
restoration month and an observed data-publication track. It does not establish
the initial-access vector, ransomware family, exploited vulnerability, specific
data fields or records, actor identity, patient injury, complete technical
recovery criteria, or causal attribution of the NHSBT O-negative stock path.

## Claims and locators

> **Claim record — SRC-0009-C01 | artifact-observation**
> **Claim:** The archived 35,726-byte UTF-8 HTML is an NHS England page whose
> canonical URL, displayed update heading and SHA-256 are recorded above; the
> live official response was byte-identical when checked on 2026-07-12, and the
> official page API reported its publication/modification timestamps.
> **Claim status:** active
> **Scope:** Local artifact identity and one dated live-byte comparison.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local artifact, HTML `<head>` and lines 7–62; article heading
> lines 184–188; live HTTPS byte comparison and official WordPress API page
> `248048` metadata checked on 2026-07-12.
> **Basis / limits:** Identity, bytes and equality are direct observations.
> Future edits at the mutable canonical URL would require a new comparison and,
> if materially revised, a new preserved snapshot/source transaction.

> **Claim record — SRC-0009-C02 | source-report**
> **Claim:** NHS England describes Synnovis as a South-East London pathology
> provider for blood, urine and specimen testing, co-owned by two named NHS
> foundation trusts and SYNLAB.
> **Claim status:** active
> **Scope:** Provider identity and service scope stated in the 2025 update, not
> a complete corporate or technical architecture.
> **As of:** 2025-11-10.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** article, “Update on the Synnovis cyber incident”, paragraph 1;
> HTML line 189.
> **Basis / limits:** The statement is direct. No deployed topology, product
> inventory, interface map or responsibility matrix is supplied.

> **Claim record — SRC-0009-C03 | source-report**
> **Claim:** NHS England reports that Synnovis was the victim of a ransomware
> cyberattack on 3 June 2024 that disrupted services across the UK and
> significantly reduced test-processing capacity, with the greatest impact in
> South-East London.
> **Claim status:** active
> **Scope:** Official attack classification, event date and provider-level
> availability effect; not a forensic mechanism or root-cause conclusion.
> **As of:** 2024-06-03.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** article, “Update on the Synnovis cyber incident”, paragraph 2;
> HTML line 190.
> **Basis / limits:** Date, ransomware label and capacity impact are direct
> reports. The page names no ransomware family, initial-access vector,
> vulnerability, compromised product, host count or actor.

> **Claim record — SRC-0009-C04 | source-report**
> **Claim:** NHS England reports delays to more than 11,000 outpatient and
> elective-procedure appointments and states that Synnovis services were fully
> restored by December 2024 after specialist incident support and rebuilding
> of IT infrastructure.
> **Claim status:** active
> **Scope:** Aggregate service-delay and management-reported restoration state;
> not patient injury or independently validated technical recovery.
> **As of:** 2024-12-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** article, “Update on the Synnovis cyber incident”, paragraphs
> 2–3; HTML lines 190–191.
> **Basis / limits:** The threshold count and restoration month are explicit.
> The source gives no denominator, appointment-type breakdown, delay duration,
> adverse clinical outcome, acceptance test, restored-component inventory or
> independent recovery assessment.

> **Claim record — SRC-0009-C05 | source-report**
> **Claim:** NHS England reports that stolen data files were published on 20
> June 2024 and that a more-than-one-year investigation later completed the
> task of associating fragmented material with affected customers; customer
> and possible individual-impact review/notification was then continuing.
> **Claim status:** active
> **Scope:** Publication and 2025 investigation/notification status; not a
> claim about specific data fields, every affected person or final breach size.
> **As of:** 2025-11-10.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** article, update paragraph 4; “What has happened since then?”
> paragraphs 1–3; “What will happen next?” paragraphs 1–3; HTML lines 192–200.
> **Basis / limits:** Publication and process state are direct. The page calls
> the material unstructured, incomplete and fragmented and says organizations
> still had to determine content and identifiability; it supplies no data-field
> list, record count, validated identity set or final notification outcome.

> **Claim record — SRC-0009-C06 | source-report**
> **Claim:** NHS England reports that Synnovis worked with NCSC, law enforcement
> and the NHS, obtained an injunction against use/further publication, reported
> the incident to the ICO and used an organization-led notification process.
> **Claim status:** active
> **Scope:** Reported incident-response and notification actions, not a legal
> determination that all duties were satisfied or that the actions were
> effective.
> **As of:** 2025-11-10.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** article, update paragraph 4 and “What will happen next?”
> paragraphs 1–3; HTML lines 192 and 198–200.
> **Basis / limits:** Actions are directly stated. The injunction, ICO record,
> notification letters and legal basis were not independently ingested; the
> page does not report enforcement findings or measured risk reduction.

## Scope and methods

This is a short public update, not a study. It presents an institutional
timeline and aggregate service/data-response facts for public communication.
No sampling method, causal model, case definition, clinical endpoint, technical
forensic method, audit criterion or quantitative uncertainty is supplied.

The availability and confidentiality tracks must remain separate:

1. ransomware → reduced pathology capacity → appointment delay → reported
   restoration; and
2. theft/publication of files → customer-scope reconstruction → organization-
   led review and possible individual notification.

Neither track establishes patient injury. The page does not tie every stolen
record to a pathology result, genomic datum or identified individual.

## Limitations and conflicts

- NHS England is an official participant in the affected health system and a
  relevant primary disclosure authority, not an external forensic evaluator.
- “Fully restored” is an unqualified institutional statement without technical
  acceptance criteria or independent validation.
- “Over 11,000” is an aggregate threshold without denominator, distribution or
  clinical-outcome follow-up.
- Ransomware class is reported; delivery mechanism, family, vulnerability,
  actor identity and attribution confidence remain unknown.
- The investigation/process status was current on 10 November 2025 and is
  time-sensitive. The same text remained live on 2026-07-12, but that does not
  prove that notification work had not progressed elsewhere.
- The page provides no correction history. Linked Q&A and third-party pages are
  outside this source transaction.

## Version status

The archived and live page display `10 November 2025`; no superseding date is
visible. The canonical page was byte-identical to the snapshot on 2026-07-12.
The official API reports publication of this page on 2024-06-25 and last
modification on 2025-11-10; it does not establish that 25 June was the first
public disclosure of the incident by any party.
Because incident attribution and notification status are volatile, current use
must be reviewed by 2026-10-10 or sooner if NHS England publishes a revision.

## Integration map

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [INC-0001](../incidents/inc-0001-synnovis-transfusion-disruption-2024.md) — exact
  event date, ransomware classification, aggregate delays, restoration month,
  data-publication and notification tracks.
- [RSK-0006](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md)
  — corroborating provider-level availability context only; NHSBT remains the
  source for the compatibility/O-negative/amber-alert chain.
- [SYN-0001](../syntheses/syn-0001-coverage-rubric.md) — checkpoint evidence; no new
  cell passes the frozen `SF2`/`SF3` threshold.
- [SYN-0003](../syntheses/syn-0003-cross-domain-transfer-directions.md) — bounded
  observed cyber/digital→clinical-continuity direction; NHS England and NHSBT
  remain two roles in one event lineage, not two independent incidents.
- [RSK-0013](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md) —
  provider-level availability/care-delay branch only.
- [SYN-0013](../syntheses/syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md) —
  preserves service delay versus biological-harm and effectiveness boundaries.
- [SYN-0015](../syntheses/syn-0015-clinical-patient-outcome-systems-evaluation-reconciliation.md) —
  aggregate service-delay comparator; no patient injury is inferred.
- [SYN-0022 — Foundational consequence/assurance calibration](../syntheses/syn-0022-foundational-consequence-assurance-calibration.md)
- [SYN-0023 — Laboratory continuity reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
