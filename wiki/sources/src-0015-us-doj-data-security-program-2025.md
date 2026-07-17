---
id: SRC-0015
type: source
title: US DOJ Data Security Program final rule and current correction chain
aliases:
  - DOJ Data Security Program 2025
  - 28 CFR Part 202 sensitive data rule
  - 90 FR 1636 data security final rule
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_type: official-legal-text
ingest_status: complete
sensitivity: public
dual_use: moderate
raw_path: ../../raw/us-doj-data-security-program-final-rule-2025.pdf
sha256: 39bffaa3d80af59cfb88beed74abe16e19b56b2c285a98707f7e081f816269cb
canonical_url: https://www.federalregister.gov/documents/2025/01/08/2024-31486/preventing-access-to-us-sensitive-personal-data-and-government-related-data-by-countries-of-concern
direct_pdf_url: https://www.govinfo.gov/content/pkg/FR-2025-01-08/pdf/2024-31486.pdf
accessed: 2026-07-12
issuer: US Department of Justice, National Security Division
publication_date: 2025-01-08
effective_date: 2025-04-08
correction_effective_date: 2025-04-18
affirmative_compliance_date: 2025-10-06
citation: 90 FR 1636–1752; 28 CFR Part 202; FR Doc. 2024-31486
jurisdictions:
  - United States
external_companions:
  - title: Correcting amendment, FR Doc. 2025-06477
    canonical_url: https://www.govinfo.gov/content/pkg/FR-2025-04-18/pdf/2025-06477.pdf
    accessed: 2026-07-12
    transient: true
    sha256_at_access: 6669c01d757314561cd0e174d3cff1fd460a7daf32b1dc226e7dfbce407a7875
  - title: Current eCFR 28 CFR Part 202
    canonical_url: https://www.ecfr.gov/current/title-28/chapter-I/part-202
    accessed: 2026-07-12
    transient: true
  - title: CISA Security Requirements for Restricted Transactions
    canonical_url: https://www.cisa.gov/sites/default/files/2025-01/Security_Requirements_for_Restricted_Transaction-EO_14117_Implementation508.pdf
    accessed: 2026-07-12
    transient: true
    sha256_at_access: f4d38bd0f2d461b2fc31c2b5019c0d138dda83ae171c1bf8951aa1d9185e75e8
tags:
  - united-states
  - regulation
  - covered-person-data-access
  - genomic-data
  - omics
  - biospecimens
  - restricted-transactions
---

# US DOJ Data Security Program final rule and current correction chain

## Bibliographic and legal identity

The local artifact is DOJ/NSD's final rule, Docket `NSD 104`, RIN
`1124-AA01`, published on 8 January 2025 as 90 FR 1636–1752 and codified at
28 CFR Part 202. It implements Executive Order 14117 through transaction-
specific prohibitions and restrictions concerning access to government-related
data and bulk U.S. sensitive personal data.

The preserved January PDF is not current standalone text: it contains an
incorrect cross-reference in §202.401(a). The official correcting amendment,
effective 18 April 2025, replaced `§202.408` with `§202.248`. Every current
claim below uses that correction and the current eCFR view, not the uncorrected
local sentence.

## Provenance and full-document review

- Immutable local artifact:
  `../../raw/us-doj-data-security-program-final-rule-2025.pdf`, 1,458,276
  bytes, 117 physical pages, SHA-256
  `39bffaa3d80af59cfb88beed74abe16e19b56b2c285a98707f7e081f816269cb`.
- The PDF is version 1.7 and unencrypted. `pdfinfo`, complete static text
  extraction, page rendering and official metadata all confirm 117 pages;
  the local `file` utility's 10-page report is erroneous. The AcroForm is the
  GPO signature widget. No JavaScript, XFA, launch action, rich media or
  embedded file was exposed or executed.
- The GPO whole-document SHA-256 signature covers the artifact and was made on
  7 January 2025 while its certificate was valid. Certificate expiry after
  signing is not treated as alteration evidence.
- All 117 pages, including preamble, codified text and appendices, were
  textually reviewed; rendered-page inspection covered the codified sections
  used here and the correction-sensitive page. Exact government-location
  polygons in §202.1401 and operational anti-evasion examples are intentionally
  not reproduced.
- On 12 July 2026, the official two-page correction streamed with SHA-256
  `6669c01d757314561cd0e174d3cff1fd460a7daf32b1dc226e7dfbce407a7875`;
  the official six-page CISA requirements streamed with SHA-256
  `f4d38bd0f2d461b2fc31c2b5019c0d138dda83ae171c1bf8951aa1d9185e75e8`.
  Both were fully read but not added to immutable raw storage.
- The eCFR version API and current text, displayed through 9 July 2026 and
  checked on 12 July, show the initial 8 April 2025 Part 202 text and the
  18 April correction for §202.401, with no later Part 202 amendment listed.
  This is a dated currency check, not a guarantee against later change.

> **Claim record — SRC-0015-C01 | artifact-observation**
> **Claim:** The preserved 1,458,276-byte artifact is the complete 117-page
> GPO final-rule PDF published as 90 FR 1636–1752, and its SHA-256 and signed
> document boundary match the identity recorded above.
> **Claim status:** active
> **Scope:** Local artifact identity and completeness; not current codified
> wording, compliance advice or proof of implementation.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local file/hash/PDF/signature inspection; Federal Register
> headers, PDF pp. 1–117; codified text, PDF pp. 72–117 / 90 FR 1707–1752.
> **Basis / limits:** File bytes, page count, metadata and signature coverage
> are directly reproducible. The January artifact retains a later-corrected
> cross-reference and therefore cannot alone establish current text.

## Effective and corrected status

The main rule became effective at 12:01 a.m. Eastern Time on 8 April 2025.
The affirmative due-diligence and audit duties in Subpart J, and the reporting
duties in §§202.1103–.1104, had a 6 October 2025 compliance date. A temporary
enforcement-discretion period did not postpone the legal effective date.

> **Claim record — SRC-0015-C02 | source-report**
> **Claim:** The final rule is effective from 8 April 2025; its specified
> affirmative compliance duties applied from 6 October 2025; and the 18 April
> 2025 correcting amendment makes §202.248—not nonexistent §202.408—the
> security-requirements cross-reference in current §202.401(a).
> **Claim status:** active
> **Scope:** Dated federal instrument status checked through 2026-07-12; not
> legal advice for a particular transaction.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** final rule `DATES` and §§202.216, 202.1001–.1002,
> 202.1103–.1104, PDF pp. 1, 76, 93–95 / 90 FR 1636, 1711, 1728–1730;
> correcting amendment, 90 FR 16466–16467; current eCFR §§202.248, .401 and
> version history checked 2026-07-12.
> **Basis / limits:** Dates and corrected phrase are explicit across multiple
> official publication surfaces within one integrated DOJ rulemaking lineage.
> Currency must be rechecked after the review date.

## Covered access and data classes

Part 202 is transactional and directional. A covered data transaction requires
a defined form of access to government-related data or bulk U.S. sensitive
personal data and one of the listed transaction classes. Applying security
requirements does not erase `access` or covered-transaction status.

> **Claim record — SRC-0015-C03 | source-report**
> **Claim:** Part 202 defines access broadly across logical or physical ability
> to obtain, view, receive or affect covered data, and defines a covered data
> transaction through data brokerage or a vendor, employment or investment
> agreement that involves such access.
> **Claim status:** active
> **Scope:** Regulatory classification; not a finding that a named system,
> person or agreement is covered.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§202.201 and 202.210, PDF pp. 72–74 / 90 FR 1707–1709.
> **Basis / limits:** Access and transaction classes are direct. Application
> also depends on actor, data, volume, exception and knowledge conditions.

The rule distinguishes human genomic data from systems-level epigenomic,
proteomic and transcriptomic data. It excludes specified routine individualized
clinical measurements from the latter three categories and pathogen-specific
data embedded in human-omic datasets. Biospecimens are separately defined,
including a treatment/diagnosis-purpose exclusion. Human genomic data has a
lower bulk threshold than the other human-omic classes; government-related data
does not depend on a bulk threshold. Pseudonymization, de-identification or
encryption does not automatically prevent a dataset from meeting `bulk`.

> **Claim record — SRC-0015-C04 | source-report**
> **Claim:** Part 202 supplies a bounded human-omics taxonomy—genomic,
> systems-level epigenomic, proteomic and transcriptomic data—with stated
> clinical/pathogen exclusions, separately treats derivable human
> biospecimens, and applies differentiated volume rules rather than one
> universal genomic-data threshold.
> **Claim status:** active
> **Scope:** Definitions used by this U.S. transaction rule; not a universal
> scientific ontology, non-human-omics scope or statement that de-identified
> data are always identifiable.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§202.205–.206, .222–.224 and .241, PDF pp. 73, 77–80 /
> 90 FR 1708, 1712–1715.
> **Basis / limits:** Categories, exclusions and threshold structure are
> explicit. This page omits individual-level data and re-identification
> mechanics; scientific or clinical classifications outside Part 202 differ.

## Prohibited and restricted transaction paths

Data brokerage involving a country of concern or covered person is prohibited.
Covered access to bulk human-omic data, or to biospecimens from which bulk
human-omic data could be derived, is also prohibited. Other vendor, employment
and investment transactions can be restricted rather than prohibited and are
authorized only when the CISA security requirements and all other applicable
Part 202 duties are satisfied. Security controls do not convert the prohibited
omics/biospecimen class into a restricted transaction.

> **Claim record — SRC-0015-C05 | source-report**
> **Claim:** Part 202 prohibits specified data-brokerage and bulk human-omic/
> derivable-biospecimen access transactions, while conditionally authorizing
> other restricted vendor, employment and investment transactions through
> corrected §202.401(a), incorporated CISA requirements and the remaining
> applicable duties.
> **Claim status:** active
> **Scope:** High-level transaction modalities; not a coverage decision for a
> named party, dataset, research project or clinical activity.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§202.301–.303 and corrected §202.401, PDF pp. 82–85 /
> 90 FR 1717–1720; correcting amendment, 90 FR 16466–16467; current eCFR
> §202.401 checked 2026-07-12.
> **Basis / limits:** Prohibited/restricted modalities are explicit. The
> regulation's detailed illustrative evasion scenarios are not reproduced.

## Controls, assurance duties and evidence boundary

At safe architectural level, CISA's incorporated requirements cover asset and
governance practices, vulnerability/supplier management, incident-response
planning, logical and physical access, identity, logging, data-risk assessment,
data minimization/masking, encryption/key management, privacy-enhancing
processing and denial of covered-person access. CISA expressly says this is not
a comprehensive cybersecurity programme.

> **Claim record — SRC-0015-C06 | source-report**
> **Claim:** The incorporated CISA requirements combine organizational,
> covered-system and data-level safeguards intended to prevent covered-person
> access in restricted transactions, while expressly disclaiming completeness
> as an organization-wide cybersecurity programme.
> **Claim status:** active
> **Scope:** Binding restricted-transaction control design; not proof of
> deployment, control operation or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** 28 CFR §§202.248 and .401, PDF pp. 80, 84–85 / 90 FR 1715,
> 1719–1720; CISA *Security Requirements for Restricted Transactions*,
> Background and §§I–II, pp. 1–6, streamed and fully read 2026-07-12.
> **Basis / limits:** Required functions and the completeness disclaimer are
> direct within the integrated federal lineage. Configuration, network
> topology and implementation detail are intentionally omitted.

Restricted-transaction U.S. persons also have defined due-diligence, policy,
annual independent-audit and records duties. The audit must assess
implementation/effectiveness and deficiencies, but a mandate to evaluate is not
itself an audit result or an effective-control finding.

> **Claim record — SRC-0015-C07 | source-report**
> **Claim:** Subparts J and K require scoped due diligence, annually certified
> policies, an annual independent audit and at least ten years of relevant
> records for restricted transactions; the rule supplies no completed audit,
> adoption rate, deficiency distribution or measured risk-reduction outcome.
> **Claim status:** active
> **Scope:** Regulatory assurance design and evidence boundary, not a finding
> about any regulated person's compliance.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§202.1001–.1002 and .1101, PDF pp. 93–94 / 90 FR
> 1728–1729; audit discussion, PDF pp. 62–63 / 90 FR 1697–1698.
> **Basis / limits:** Duties and audit scope are direct. Required independent
> audit does not mean an audit occurred, passed, was external or demonstrated
> causal effectiveness.

## Research, clinical and institutional boundaries

Part 202 has no blanket exemption for all non-federally funded research.
Federal official-business/grant, international-health, regulatory-approval,
clinical-investigation and post-marketing provisions are bounded to their
stated conditions. Other federal authorities remain unaffected; a Part 202
license does not substitute for another agency's authorization.

> **Claim record — SRC-0015-C08 | source-report**
> **Claim:** Part 202 uses activity- and data-specific exceptions for defined
> federal, international-health, regulatory and clinical contexts rather than
> a universal research or healthcare exemption, and preserves other federal
> authorities.
> **Claim status:** active
> **Scope:** Exception architecture at safe abstraction; not legal advice or a
> determination that a particular study, grant or submission qualifies.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §§202.103, .504, .507–.511 and .803, PDF pp. 72, 85–92 /
> 90 FR 1707, 1720–1727.
> **Basis / limits:** Exceptions and non-displacement are explicit. Their
> application depends on facts and other authorities outside this source.

> **Claim record — SRC-0015-C09 | analytic-judgment**
> **Claim:** This legal lineage establishes binding control, audit, reporting
> and enforcement design, but it documents neither a completed regulated
> implementation nor an enforcement event, tested safeguard or independently
> evaluated effectiveness outcome.
> **Claim status:** active
> **Scope:** Evidence classification for the reviewed rule, correction, current
> codification and incorporated requirements.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** full final rule, especially Subparts D and J–M, PDF pp. 84–96 /
> 90 FR 1719–1731; correction and CISA requirements noted above.
> **Basis / limits:** Normative duties and enforcement powers do not prove
> adoption, inspection, violation, audit finding or outcome. Separate primary
> implementation/enforcement records are required for SF3 evidence.

## Safety and legal-use boundary

This page is a defensive governance abstraction, not legal advice. It omits
government-location coordinates, operational anti-evasion examples, personal
records, system topology, credential/configuration detail and any method for
bypassing access restrictions. Exact coverage must be assessed against current
codified text and facts by an authorized professional.

## Related pages

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [GOV-0005 — US Data Security Program](../governance/gov-0005-us-data-security-program-2025.md)
- [RSK-0011 — Part 202 regulated access branches](../risk-scenarios/rsk-0011-covered-omics-regulated-access.md)
- [CTL-0008 — Part 202 transaction controls](../controls/ctl-0008-restricted-data-transaction-controls.md)
- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [WFL-0005 — Genomic lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003 — Genomic ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [RSK-0004 — Genomic disclosure privacy path](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md)
- [CTL-0002 — Genomic risk management](../controls/ctl-0002-genomic-data-risk-management.md)
- [SYN-0004 — US–EU human-omics and health-data governance](../syntheses/syn-0004-us-eu-human-omics-health-data-governance.md)
- [SYN-0008 — Five-context governance reconciliation](../syntheses/syn-0008-global-us-eu-uk-canada-governance-reconciliation.md)

- [SYN-0020 — Foundational cross-sector reconciliation](../syntheses/syn-0020-foundational-cross-sector-assets-lifecycle-governance-reconciliation.md)

## Official links

- Final rule HTML: <https://www.federalregister.gov/documents/2025/01/08/2024-31486/preventing-access-to-us-sensitive-personal-data-and-government-related-data-by-countries-of-concern>
- Correction: <https://www.govinfo.gov/content/pkg/FR-2025-04-18/pdf/2025-06477.pdf>
- Current eCFR: <https://www.ecfr.gov/current/title-28/chapter-I/part-202>
- CISA requirements: <https://www.cisa.gov/sites/default/files/2025-01/Security_Requirements_for_Restricted_Transaction-EO_14117_Implementation508.pdf>
