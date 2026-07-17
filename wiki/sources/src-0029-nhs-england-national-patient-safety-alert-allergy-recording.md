---
id: SRC-0029
type: source
title: NHS England NatPSA on incorrect penicillin/penicillamine allergy recording
aliases:
  - NatPSA/2025/006/NHSPS
  - NHS England national allergy-record incident review 2025
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: official-national-patient-safety-alert-and-incident-review
ingest_status: complete-package
sensitivity: public
dual_use: low
raw_path: ../../raw/nhs-england-natpsa-allergy-recording-2025.pdf
sha256: 9a1d2dd06a301eab8c58e1e3e8ff65d4641912f17affa6496775ad4c00c0d109
raw_components:
  - path: ../../raw/nhs-england-natpsa-allergy-recording-current-2026-07-12.html
    role: complete-official-long-read-rendering
    sha256: 9645f36c83279e5ffe2bbbab50f9506120602c6064c22e693a92813294d304af
  - path: ../../raw/nhs-england-national-patient-safety-alerts-current-2026-07-12.html
    role: current-official-alert-list-snapshot
    sha256: 65af5ab8e7a6801e12b07bf0bf2c37ba66fbe5aa7d290ad178bf10c05af29868
canonical_url: https://www.england.nhs.uk/long-read/national-patient-safety-alert-harm-from-incorrect-recording-of-a-penicillin-allergy-as-a-penicillamine-allergy/
repository_url: https://www.england.nhs.uk/wp-content/uploads/2025/11/national-patient-safety-alert-penicillamine-allergy-recording.pdf
catalogue_url: https://www.england.nhs.uk/patient-safety/patient-safety-insight/patient-safety-alerts/
accessed: 2026-07-12
publication_date: 2025-11-20
completion_deadline: 2026-11-20
reference: NatPSA/2025/006/NHSPS
issuer: NHS England
jurisdictions:
  - England
  - United Kingdom
tags:
  - national-patient-safety-alert
  - clinical-record
  - allergy-safety
  - semantic-integrity
  - electronic-prescribing
  - incident-review
  - anaphylaxis
  - non-cyber
---

# NHS England NatPSA on incorrect penicillin/penicillamine allergy recording

## Artifact identity and complete-package review

The preserved package contains the official two-page alert, its complete NHS
England long-read rendering and a current snapshot of NHS England's alert list.

- Main PDF: 200,663 bytes, SHA-256
  `9a1d2dd06a301eab8c58e1e3e8ff65d4641912f17affa6496775ad4c00c0d109`;
  tagged, unencrypted PDF 1.7, two A4 pages.
- Long-read HTML: 47,538 bytes, SHA-256
  `9645f36c83279e5ffe2bbbab50f9506120602c6064c22e693a92813294d304af`.
- Current alert-list HTML: 59,277 bytes, SHA-256
  `65af5ab8e7a6801e12b07bf0bf2c37ba66fbe5aa7d290ad178bf10c05af29868`.

Two official retrievals of each artifact on 2026-07-12 were byte-identical.
Both PDF pages were text-read and visually rendered: both are text-bearing,
with zero blank or wholly image-only pages. The PDF has no form, XFA,
JavaScript, embedded file, encryption or cryptographic signature; its ten
ordinary URI annotations were inventoried but not executed. The complete
substantive sections of both HTML pages were reviewed statically. The long-read
has 21 scripts, one search form and no iframe; the current list has 20 scripts,
one search form and one video iframe. None was executed.

> **Claim record — SRC-0029-C01 | artifact-observation**
> **Claim:** The preserved 307,478-byte package is complete for the official
> two-page PDF, full long-read and current alert-list snapshot: every file
> matches two byte-identical retrievals and its recorded hash/size; both PDF
> pages are text-bearing and visually reviewed, and static inspection finds no
> form, XFA, JavaScript, attachment, encryption or digital signature.
> **Claim status:** active
> **Scope:** Artifact identity, completeness and static active-content review
> on 2026-07-12; not substantive validation of the alert's conclusions.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Full two-page PDF and both complete HTML snapshots; hashes,
> byte/page counts, `pdfinfo`, `pdfsig`, `pdfdetach`, text inventory, URI
> inventory, full-page renders and static HTML element counts.
> **Basis / limits:** File properties and completeness are locally observable.
> Linked pages, scripts, form and iframe content were not executed or treated
> as substantive evidence.

## Lineage and modality

> **Claim record — SRC-0029-C02 | artifact-observation**
> **Claim:** The PDF, long-read and current list are one NHS England alert and
> national incident-review lineage; two reporting repositories, partner logos,
> consulted stakeholders and duplicate renderings do not create independent
> sources or evaluations.
> **Claim status:** active
> **Scope:** Evidence-lineage classification, not a claim that contributors
> lacked relevant expertise.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF title/header, incident-data and stakeholder sections;
> long-read title/date/reference and identical substantive sections; current
> list item under 2025.
> **Basis / limits:** NHS England is the issuer and analyst throughout.
> Repository counts are inputs to one review, not independent corroboration.

## Alert identity and scope

> **Claim record — SRC-0029-C03 | source-report**
> **Claim:** NHS England issued `NatPSA/2025/006/NHSPS` on 20 November 2025 as
> a safety-critical and complex national patient-safety alert for specified
> English care-provider classes, with executive and relevant clinical-
> informatics coordination expected.
> **Claim status:** active
> **Scope:** Issuer, reference, date, recipient classes and coordination
> modality; not UK-wide legal force, adoption, compliance or effectiveness.
> **As of:** 2025-11-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF physical p. 1 header/preamble; long-read title, date,
> reference and introductory paragraphs.
> **Basis / limits:** Identity and recipient language are direct. Scotland
> appears as stakeholder engagement, not as proof that the English alert's
> obligations apply there.

## Error and propagation class

> **Claim record — SRC-0029-C04 | source-report**
> **Claim:** The alert describes a non-adversarial look-alike allergy-record
> integrity error in electronic prescribing: local interface/configuration
> presentations differ, the risk is not specific to one system, and record
> sharing can potentially propagate an incorrect state across care settings.
> **Claim status:** active
> **Scope:** General issue class and potential propagation, not the proven root
> cause or measured propagation path of the fatal incident.
> **As of:** 2025-11-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF physical p. 1, `Explanation of identified safety issue`;
> long-read `Explanation of identified safety issue` paragraphs 1–6.
> **Basis / limits:** Similar-label, variable-configuration and potential
> sharing predicates are direct. Step-by-step search/dropdown behavior and
> named vendor detail are intentionally omitted.

## National incident-data review

> **Claim record — SRC-0029-C05 | source-report**
> **Claim:** NHS England searched NRLS and LFPSE for reports of incidents said
> to have occurred from 1 January 2021 through 31 December 2023 and reports
> that clinical review deemed 315 relevant: 279 NRLS reports and 36 LFPSE
> reports.
> **Claim status:** active
> **Scope:** Report-search window, repository components and relevance count;
> not 315 unique incidents, patients, providers or independent samples.
> **As of:** 2023-12-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF physical p. 2, `Patient safety incident data`, first two
> paragraphs; long-read same heading and paragraphs.
> **Basis / limits:** `279 + 36 = 315` reconciles exactly. The source gives no
> deduplication method, report-to-patient mapping, denominator, reporting-
> completeness measure or raw dataset.

> **Claim record — SRC-0029-C06 | source-report**
> **Claim:** Within that review NHS England reports one fatal incident: a known
> allergy was inaccurately represented in a primary-care record, an
> incompatible medicine was prescribed, an anaphylactic reaction occurred and
> the patient died.
> **Claim status:** active
> **Scope:** One anonymized issuer-summarized fatal event; not an independently
> reviewable case file, exact event date or proof of the general interface/
> record-sharing mechanism in that case.
> **As of:** 2023-12-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF physical p. 1, final `Explanation` paragraphs, and p. 2,
> `Patient safety incident data`, fatal-incident paragraph; long-read matching
> paragraphs.
> **Basis / limits:** Incorrect record→prescription→anaphylaxis→death is direct
> in NHS England's summary. Date, identity, software, entry workflow, discovery
> and root cause are not reported.

> **Claim record — SRC-0029-C07 | source-report**
> **Claim:** After enumerating reports, NHS England switches unit and describes
> all other relevant incidents collectively as `low or no harm`, then lists
> uncounted symptom, inpatient prescribing/administration and discharge-
> information issue classes without a low-versus-no-harm split or
> cross-tabulation.
> **Claim status:** active
> **Scope:** Aggregate source severity wording, explicit unit change and issue
> categories; not a derived remaining incident/report/near-miss count, severity
> distribution or unique-case count.
> **As of:** 2023-12-31.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF physical p. 1, final explanation sentence, and p. 2,
> incident-data fatal paragraph/bullets; long-read matching sections.
> **Basis / limits:** The source gives no report-to-incident mapping. No count
> of remaining incidents or reports can therefore be derived; arithmetic must
> not turn low-harm events into near misses or resolve the missing allocation.

## Required actions and evidence state

> **Claim record — SRC-0029-C08 | source-report**
> **Claim:** The alert calls for cross-setting coordination, authorized record
> identification, clinical accuracy review and synchronized correction,
> guidance/training, entry checks, supplier/user interface mitigations and
> periodic reporting for assurance, as soon as possible but no later than
> 20 November 2026.
> **Claim status:** active
> **Scope:** Required or recommended action design and deadline; not blind bulk
> relabelling, query instructions, deployment, compliance or effectiveness.
> **As of:** 2025-11-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF physical p. 1, `Actions required` 1–5, and p. 2 Notes A–E;
> long-read `Actions required` and `Additional information`.
> **Basis / limits:** Clinical review before correction and source-specific
> `should`/`strongly consider` modalities are retained. No record-query syntax,
> exact alert copy or de-labelling procedure is reproduced.

> **Claim record — SRC-0029-C09 | artifact-observation**
> **Claim:** On 2026-07-12 NHS England's current list still presented this
> 20 November 2025 alert and its deadline was future, while the package
> supplies no recipient implementation, declared compliance, enforcement,
> corrected-record denominator, post-alert trend, risk resolution or
> independent outcome evaluation.
> **Claim status:** active
> **Scope:** Dated current-list presence and absent evidence predicates; not a
> claim that the alert was the latest, active/unresolved in a legal sense, or
> that no implementation occurred elsewhere.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Current alert-list snapshot, 2025 list item and generic
> provider/alert-governance sections; PDF/long-read action deadline.
> **Basis / limits:** Continued official listing and a future deadline are
> direct. The list contains a later December 2025 alert and no compliance
> status for this item; possible CQC action is not actual enforcement.

## Limitations and criterion boundary

> **Claim record — SRC-0029-C10 | artifact-observation**
> **Claim:** The cited approximate allergy-label prevalence/inaccuracy figures
> derive from external literature rather than the 315-report review, the
> supplier example is not independent effectiveness evidence and the phrase
> `significant numbers` has no count, denominator or method; none is used as a
> NatPSA outcome metric.
> **Claim status:** active
> **Scope:** Citation and metric-provenance boundary.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PDF physical p. 2 Notes A, D–E, incident-data final paragraph
> and References 3–4; long-read corresponding notes/references.
> **Basis / limits:** Citation attribution is direct. The referenced research,
> supplier blog and underlying enquiry data were not independently ingested.

> **Claim record — SRC-0029-C11 | artifact-observation**
> **Claim:** This materially separate national review strengthens the
> `CPH-CI`, THI, CTR and governance-case evidence portfolios but changes no
> frozen cell: `CPH-CI` remains Partial pending an independent systems-
> evaluation lineage and reconciliation; actions/current listing do not pass
> `CPH-AE`, and the score remains 37/110.
> **Claim status:** active
> **Scope:** Frozen-rubric boundary after this single NHS England review
> lineage; not a claim that 315 reports have no substantive value.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0029-C02`–`C10`; frozen `CPH-CI/AE`, THI/CTR/GOV and
> global criteria in [SYN-0001](../syntheses/syn-0001-coverage-rubric.md); prior
> `SYN-0001-C22` checkpoint at 37/110.
> **Basis / limits:** This is one independent national-review lineage. It does
> not confirm any separately documented case or evaluate a shared systems
> problem, and its report count is not multiplied into the incident-corpus
> gates.

## Safety handling

The wiki retains only official alert identity, aggregate report units,
minimum anonymized fatal-outcome chain, system-role boundaries, action classes
and evidence state. It omits UI/search instructions, query syntax, exact alert
copy, patient/facility identity, treatment detail, provider configuration and
record-level data.

## Integration map

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [INC-0003 — national aggregate review and reported fatality](../incidents/inc-0003-national-allergy-recording-fatality-review-2021-2023.md)
- [RSK-0015 — wrong-entry and potential-propagation path](../risk-scenarios/rsk-0015-allergy-record-entry-propagation-medication-harm.md)
- [CTL-0014 — required corrective-control map](../controls/ctl-0014-allergy-record-identification-correction-safety-controls.md)
- [SYN-0015 — accepted clinical-outcome/system-evaluation reconciliation](../syntheses/syn-0015-clinical-patient-outcome-systems-evaluation-reconciliation.md)
- [SYN-0022 — Foundational consequence/assurance calibration](../syntheses/syn-0022-foundational-consequence-assurance-calibration.md)
