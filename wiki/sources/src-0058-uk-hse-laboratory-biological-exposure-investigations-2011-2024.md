---
id: SRC-0058
type: source
title: UK HSE laboratory biological-exposure investigation notices, 2011 and 2024
aliases:
  - HSE missing clinical information laboratory notices
  - HSE specimen information containment exposure record
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-12
source_type: official-regulator-investigation-summary-and-safety-notice-lineage
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/hse-lab-biological-agent-exposure-safety-notice-current-2026-07-12.html
raw_bytes: 41443
sha256: 7a2b5f66e064748727011db66980ade664e2a907cd10640cf07b90c06fe69e66
raw_components:
  - path: ../../raw/hse-clinical-information-lab-safety-notice-current-2026-07-12.html
    role: predecessor-2011-investigation-summary-and-safety-alert
    bytes: 42886
    sha256: f3dead766059081eab0ac0f524072089bd6c7901e66508e6c43dc03fa8c41e2c
canonical_url: https://www.hse.gov.uk/safetybulletins/risk-exposure-lab-staff-biological-agents.htm
predecessor_url: https://www.hse.gov.uk/safetybulletins/clinicalinformation.htm
accessed: 2026-07-12
publication_date: 2024-11
issuer: UK Health and Safety Executive
jurisdictions:
  - United Kingdom
tags:
  - laboratory
  - veterinary-laboratory
  - exposure
  - specimen-information
  - containment-decision
  - record-system
  - safety-notice
---

# UK HSE laboratory biological-exposure investigation notices, 2011 and 2024

## Package identity and lineage

> **Claim record — SRC-0058-C01 | artifact-observation**
> **Claim:** Two complete HSE HTML notices totaling 84,329 bytes are retained
> with exact hashes; repeat retrieval preserved exact bytes for the 2024
> notice, while the 2011 page differed only in generated email-obfuscation
> tokens and retained substantively identical notice text.
> **Claim status:** active
> **Scope:** Local artifact identity and substantive repeatability; not proof
> that live pages will remain unchanged.
> **As of:** Retrieved and repeated 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Frontmatter paths/counts/hashes; repeat retrieval, `cmp`,
> one-line diff and full plain-text extraction/review.
> **Basis / limits:** The only repeat-page difference was Cloudflare-style
> protected-email encoding, not issue, action, legal or investigation content.

> **Claim record — SRC-0058-C02 | analytic-judgment**
> **Claim:** ED03-2024 and HID 5-2011 are one evolving HSE regulator lineage,
> not two independent investigations or a countable set of named incidents;
> the later notice expands the represented clinical/veterinary context and
> current IT/record-system actions.
> **Claim status:** active
> **Scope:** Evidence-lineage and event-count boundary; not a trend estimate or
> claim that the same cases recur.
> **As of:** Notices 2011-12-09 and 2024-11; checked 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Both notices' issuer, bulletin metadata, `Issue`/`Key Issues`,
> investigation and action sections.
> **Basis / limits:** HSE reports several/a number of investigated occasions
> without names, dates, case count, methods or independent confirmations.

## Investigated exposure pathway

> **Claim record — SRC-0058-C03 | source-report**
> **Claim:** HSE reports confirmed occasions in which missing, inaccurate or
> delayed specimen context prevented appropriate risk identification, led to
> laboratory handling under insufficient containment conditions and exposed
> workers to biological agents capable of severe disease.
> **Claim status:** active
> **Scope:** High-level investigated input/context→containment-decision→worker-
> exposure path; not an infection count, named laboratory, person-level
> outcome or operational containment procedure.
> **As of:** HSE investigations summarized in 2011 and 2024 notices.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** ED03-2024 `Issue`, `Outline of the problem` and `Clinical
> information on multiple samples`; HID 5-2011 `Key Issues`, `Introduction`
> and `Background`.
> **Basis / limits:** Exposure occasions and causal information gap are direct
> regulator statements. Illness, severity distribution and incidence are not
> reported.

> **Claim record — SRC-0058-C04 | source-report**
> **Claim:** HSE identifies absent cross-sample linkage, inadequate context
> capture/visibility and failure to alert staff when relevant information
> changes as concrete information-system exposure classes capable of affecting
> laboratory safety decisions.
> **Claim status:** active
> **Scope:** Conditional workflow/system weaknesses; not a vulnerability scan,
> product defect or claim every laboratory has these conditions.
> **As of:** ED03-2024 issue date 2024-11.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** ED03-2024 `Clinical information on multiple samples`, `Ensure
> that laboratory staff act` and `Ensure that record-keeping and IT systems
> are fit for purpose`.
> **Basis / limits:** The notice ties these states to investigated exposure
> contexts but does not publish a facility-level technical architecture.

## Required action and governance boundary

> **Claim record — SRC-0058-C05 | source-report**
> **Claim:** HSE directs duty holders to improve request guidance, staff
> training, relevant-context capture, cross-specimen linkage, information
> visibility, update alerts, monitoring/audit and response, while the 2024
> notice links relevant UK workplace-safety legislation.
> **Claim status:** active
> **Scope:** Regulator-directed defensive actions and linked legal context; not
> legal advice, confirmed implementation or measured effectiveness.
> **As of:** Current notice checked 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** ED03-2024 `Action required`, `Guidance` and `Relevant legal
> documents`; HID 5-2011 `Action required` and legal-documents list.
> **Basis / limits:** Recommended/required actions are direct. The notices do
> not evaluate adoption, test performance or outcome reduction.

> **Claim record — SRC-0058-C06 | analytic-judgment**
> **Claim:** The recurrence of the same information-to-safety theme across the
> two notices demonstrates a persistent regulator concern, but cannot establish
> prevalence, a worsening trend, a fixed event count or failure of every action
> issued in 2011.
> **Claim status:** active
> **Scope:** Temporal interpretation of one HSE lineage.
> **As of:** 2011–2024 notices; reviewed 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0058-C02`–`C05`; both notice texts.
> **Basis / limits:** Similar themes are direct; trend and causal persistence
> are not measured.

## Safety and contribution boundary

> **Claim record — SRC-0058-C07 | analytic-judgment**
> **Claim:** This package supplies concrete accidental, information, IT and
> containment-exposure evidence for laboratory threat modelling, but no
> malicious cause, exploit, facility topology, operational procedure,
> identifiable incident page or independent safeguard-effectiveness result.
> **Claim status:** active
> **Scope:** Downstream-use and safety classification.
> **As of:** Full package review 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0058-C02`–`C06`; both notices' stated scope and omissions.
> **Basis / limits:** High-level investigation findings and defensive controls
> are sufficient; operational biological detail is excluded.

## Related pages

- [HAZ-0006 — laboratory hazards](../hazards/haz-0006-laboratory-input-configuration-environmental-and-inventory-failures.md)
- [VUL-0006 — laboratory exposures](../vulnerabilities/vul-0006-laboratory-context-threshold-oversight-and-supply-exposures.md)
- [RSK-0021 — context/input decision path](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)
- [CTL-0023 — controls](../controls/ctl-0023-laboratory-result-validation-anomaly-detection-and-containment-controls.md)
- [SYN-0031 — rubric reconciliation](../syntheses/syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)

## Sources

- Retained current and predecessor HSE notices at frontmatter URLs.
