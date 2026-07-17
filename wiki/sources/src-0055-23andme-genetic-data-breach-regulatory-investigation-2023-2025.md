---
id: SRC-0055
type: source
title: 23andMe genetic-data breach, company disclosures and Canada–UK investigation, 2023–2025
aliases:
  - 23andMe OPC ICO breach evidence package
  - 23andMe credential-stuffing regulatory record
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-12
source_type: official-joint-regulatory-findings-penalty-and-company-sec-disclosure-package
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/23andme-opc-ico-joint-findings-2025.html
raw_bytes: 251792
sha256: faa15da8ed6b10c9798cf8af2a39a9afa19967371aaeaebeed0a8b0fb43898b1
raw_components:
  - path: ../../raw/23andme-ico-penalty-notice-2025.pdf
    role: uk-commissioner-penalty-notice-from-the-joint-investigation
    bytes: 2433151
    sha256: d8509fdf38ddd2c29587d7cb73fdd505e072fbee5d2bec184eaf97e789b6d593
  - path: ../../raw/23andme-ico-enforcement-record-current-2026-07-12.html
    role: current-ico-enforcement-record-and-publication-context
    bytes: 32824
    sha256: f453c4841ad9e7b236e41afd9d70b43c79a8f5eaf28c1f1e72d35379959a94d2
  - path: ../../raw/23andme-sec-8k-2023-10-10.html
    role: company-preliminary-form-8-k-disclosure-filed-2023-10-10
    bytes: 26463
    sha256: 3d1300bc2f79c27a89ac765af403917071ac539cc59846efebc7f893eba59b0d
  - path: ../../raw/23andme-sec-8ka-2023-12-05.html
    role: company-form-8-k-a-amendment-filed-2023-12-01-local-filename-date-is-not-filing-date
    bytes: 29389
    sha256: eb852984baebd35d1c61a2690e42e2e61e52b570ba0fa89dd15ab971e0e3a41e
  - path: ../../raw/23andme-sec-10k-2024.html
    role: company-form-10-k-filed-2024-05-30
    bytes: 2759836
    sha256: 1c8d971d53a5a3700f349e797bbfe11909475e87df702b579e97e6d2b5166827
canonical_url: https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2025/pipeda-2025-001/
ico_penalty_url: https://ico.org.uk/media2/kclbljpo/23andme-penalty-notice.pdf
ico_enforcement_url: https://ico.org.uk/action-weve-taken/enforcement/2025/06/23andme/
sec_original_8k_url: https://www.sec.gov/Archives/edgar/data/1804591/000119312523253488/d520529d8k.htm
sec_amended_8k_url: https://www.sec.gov/Archives/edgar/data/1804591/000119312523287449/d242666d8ka.htm
sec_2024_10k_url: https://www.sec.gov/Archives/edgar/data/1804591/000180459124000038/me-20240331.htm
accessed: 2026-07-12
publication_date: 2025-06-25
issuers:
  - Office of the Privacy Commissioner of Canada
  - UK Information Commissioner's Office
  - 23andMe Holding Co.
jurisdictions:
  - Canada
  - United Kingdom
  - United States
tags:
  - genomics
  - consumer-genetics
  - credential-stuffing
  - privacy-breach
  - incident
  - enforcement
  - canada
  - united-kingdom
---

# 23andMe genetic-data breach, company disclosures and Canada–UK investigation, 2023–2025

## Package identity and reproducibility

The package retains the complete OPC-hosted joint report, the 153-page ICO
penalty notice and its current enforcement record, plus the original 8-K, its
Amendment No. 1 and the 2024 10-K. The misleading date in the immutable local
filename `23andme-sec-8ka-2023-12-05.html` is not used as document metadata:
the SEC artifact is accession `0001193125-23-287449`, filed and accepted on
2023-12-01.

The two regulator artifacts arise from the same joint investigation. The
penalty notice expressly says its findings are those of the UK Commissioner;
it is not a second independent investigation. The three SEC filings are one
company-reporting lineage whose statements evolve as the inquiry matures.

> **Claim record — SRC-0055-C01 | artifact-observation**
> **Claim:** Six official objects totaling 5,533,455 bytes are retained with
> exact hashes: a complete joint findings page, 153-page UK penalty notice,
> current enforcement record and three SEC filings; repeat retrieval preserved
> byte identity for the PDF/SEC artifacts and substantive identity for the two
> dynamic regulator pages.
> **Claim status:** active
> **Scope:** Local artifact identity and reproducibility; not cryptographic
> issuer authentication or proof the live HTML will never change.
> **As of:** Retrieved and repeated 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Frontmatter paths, byte counts and SHA-256 values; `pdfinfo`,
> complete text review and normalized repeat-HTML comparisons.
> **Basis / limits:** Dynamic differences were generated form/DOM tokens, not
> substantive findings. The local 8-K/A filename date is explicitly corrected.

## Evidence lineages and investigation limits

> **Claim record — SRC-0055-C02 | analytic-judgment**
> **Claim:** The package contains two material evidence lineages—23andMe's
> evolving first-party SEC disclosures and one joint OPC/ICO investigation
> applying two jurisdictions—while the penalty notice and enforcement page are
> derivative regulatory outputs rather than additional investigations.
> **Claim status:** active
> **Scope:** Claim-specific independence accounting; not equal evidentiary
> weight, two independently replicated events or two independent deployments.
> **As of:** Records through 2025-06-25; checked 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Joint report paragraphs 13–19; penalty notice paragraphs 3 and
> 11; SEC filing identities and dates.
> **Basis / limits:** Issuers and evidence-production roles differ. Regulators
> reviewed company submissions, interviews and open sources but lacked some
> requested internal logs and the privileged forensic report; updated raw-DNA
> figures in paragraph 196 were not independently verified.

## Event, access populations and data classes

> **Claim record — SRC-0055-C03 | source-report**
> **Claim:** The joint investigation found credential stuffing from
> 2023-04-29 through 2023-09-20 directly accessed 18,222 customer accounts
> worldwide—769 in Canada and 611 in the UK—and leveraged linked DNA Relatives
> profiles to expose information beyond those accounts; the overall reported
> affected-customer total was almost seven million.
> **Claim status:** active
> **Scope:** One incident with distinct directly accessed and linked-profile
> populations; not seven million credential-stuffed accounts, a prevalence
> estimate or an independently reconstructed full log census.
> **As of:** Event period 2023-04-29–2023-09-20; findings 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Joint report paragraphs 20–35, especially 20, 28–30 and the
> Canada/UK/worldwide tables; penalty notice paragraphs 95–105 for UK scope.
> **Basis / limits:** Direct-account counts and linked-profile scale are
> regulator findings. Population definitions remain separate; approximations
> and company-supplied values are not converted into exact totals.

> **Claim record — SRC-0055-C04 | source-report**
> **Claim:** Depending on account/profile state, exposed information included
> identity and contact attributes, ancestry/race or ethnicity, health-related
> information, raw genetic data and DNA-relative/family-tree relationship,
> shared-segment or shared-percentage information; the exact mix differed
> between directly accessed accounts and linked profiles.
> **Claim status:** active
> **Scope:** Regulator-described data classes; not a claim every affected person
> had every field exposed, a re-identification procedure or biological harm.
> **As of:** Event 2023; findings 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Joint report paragraphs 28–35 and tables; paragraphs 136–147
> for sensitivity and harm analysis; SEC 8-K/A Item 7.01 for the earlier
> company-reported ancestry/health boundary.
> **Basis / limits:** Data types are direct but heterogeneous. Raw-DNA download
> attribution remained methodologically uncertain under paragraphs 188–196.

## Timeline and evolving company disclosure

| State | Represented evidence | Boundary |
| --- | --- | --- |
| attack | credential stuffing, 2023-04-29–2023-09-20 | start is not discovery |
| missed indicators | July platform/login and profile-transfer anomalies; August claim | regulator retrospective finding, not contemporaneous confirmation |
| discovery/verification | online post found 2023-10-01; legitimacy confirmed 2023-10-05 | confirmation distinct from first activity |
| public disclosure | company blog 2023-10-06; original 8-K filed 2023-10-10 | preliminary scope |
| containment actions | sessions disabled 2023-10-09; global password reset 2023-10-10; mandatory email-based 2SV in November | implementation is not causal effectiveness proof |
| direct-account notice | January 2024 after forensic analysis | regulator found content defects and Canadian timing defect |
| regulatory resolution | additional measures represented through 2024-12-31; joint findings 2025-06-25 | bounded legal resolution, not harm reversal |

> **Claim record — SRC-0055-C05 | analytic-judgment**
> **Claim:** The official record separates attack, missed-warning, discovery,
> verification, disclosure, containment, affected-person notification and
> bounded regulatory-resolution states rather than substituting a filing or
> publication date for event discovery or recovery.
> **Claim status:** active
> **Scope:** Defensible incident-state chronology; not a complete minute-level
> response log, full trusted-restoration date or proof stolen data were recovered.
> **As of:** Events 2023–2024; findings 2025.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Joint report paragraphs 20–27, 89–110, 153–187 and 198–200;
> original/amended 8-K Item 7.01; 2024 10-K Item 1C and Note 13.
> **Basis / limits:** Every represented state is located. The joint report says
> stolen data had not been recovered; a complete recovery endpoint is unknown.

> **Claim record — SRC-0055-C06 | source-report**
> **Claim:** 23andMe's SEC record evolved from a preliminary reused-credential
> explanation with unknown scope, through the 2023-12-01 8-K/A's 0.1% direct-
> account estimate, linked-profile access, password reset and two-step
> verification, to the 2024 10-K's approximately 5.5 million DNA Relatives and
> 1.5 million Family Tree profiles, $4.6 million of fiscal-year incident expense
> and $2.8 million of probable insurance recoveries.
> **Claim status:** active
> **Scope:** Attributed company disclosures and temporal evolution; not
> independent verification, additive population totals or regulator-approved
> final counts.
> **As of:** SEC filings 2023-10-10, 2023-12-01 and 2024-05-30.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Original 8-K and Amendment No. 1, Item 7.01; 2024 10-K Item 1A,
> printed pp. 46–47, HTML anchor
> `#i60a9d910bf16484f9c21b3c78f2f15ad_22`; Item 1C, pp. 69–70, anchor
> `#i60a9d910bf16484f9c21b3c78f2f15ad_721`; Note 13, pp. 128–129, XBRL block
> `#f-1138`.
> **Basis / limits:** The filings are one issuer lineage. The 8-K/A contains no
> 6.9-million absolute total, and its local filename does not set filing date.

## Safeguards, notification and enforcement

> **Claim record — SRC-0055-C07 | source-report**
> **Claim:** OPC and ICO found safeguards inadequate for the sensitivity and
> scale of the information, citing deficient credential-stuffing risk
> treatment, authentication, password screening, monitoring/detection,
> investigation of anomalies and incident-response preparedness; they reached
> separate PIPEDA Principle 4.7 and UK-GDPR Articles 5(1)(f)/32 conclusions.
> **Claim status:** active
> **Scope:** One shared platform assessed under two legal regimes; not a
> universal consumer-genetics baseline or proof each deficiency caused every
> affected record.
> **As of:** Relevant pre/during-breach safeguards; findings 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Joint report paragraphs 37–117, especially 89–113; penalty
> notice Sections VI.C(a)–(e).
> **Basis / limits:** Findings are direct and jurisdiction-specific. A single
> joint fact-finding process is not multiplied into independent technical tests.

> **Claim record — SRC-0055-C08 | source-report**
> **Claim:** Both Commissioners found material notification-content defects;
> Canada also found direct-account notices were not sent as soon as feasible,
> while the UK accepted the explained regulator-report delay but found Article
> 33/34 content failures, including omission of possible raw-DNA access from
> affected-person communications.
> **Claim status:** active
> **Scope:** Case-specific reporting and notice findings; not a claim that all
> Canadian or UK notifications were late or that both timing laws are identical.
> **As of:** Notifications 2023–2024; findings 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Joint report paragraphs 118–187, especially 149–169 and
> 173–187; current rule package [SRC-0056](src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md).
> **Basis / limits:** Timing, content and jurisdiction are kept separate. The
> company completed parts of forensic analysis only later in November 2023.

> **Claim record — SRC-0055-C09 | analytic-judgment**
> **Claim:** The Commissioners accepted, on balance, that measures represented
> as implemented by 2024-12-31 resolved their safeguard and notification
> concerns, including stronger password screening/policy, mandatory MFA,
> sensitive-download checks/delay, attack exercises, monitoring alerts,
> customer event history and revised incident processes.
> **Claim status:** active
> **Scope:** Legal/remedial resolution of this investigation; not independent
> penetration-test replication, comparative harm reduction, permanent
> effectiveness or recovery of copied data.
> **As of:** Represented implementation through 2024-12-31; findings 2025.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** medium
> **Evidence:** Joint report paragraphs 114–117 and 198–200; penalty notice
> Section VI.C(e); 2024 10-K Item 1C for earlier issuer-reported changes.
> **Basis / limits:** Measures were principally company-reported and accepted
> under a bounded regulatory standard. Full internal logs/forensic report and
> independent outcome testing are absent from the retained record.

> **Claim record — SRC-0055-C10 | source-report**
> **Claim:** The UK Commissioner's 2025-06-05 penalty notice imposed a
> £2.31-million penalty for UK-GDPR Articles 5(1)(f) and 32(1) infringements
> affecting 155,592 UK data subjects; this UK enforcement output follows the
> same joint investigation and does not create a second event or investigator.
> **Claim status:** active
> **Scope:** UK penalty, legal basis and represented population; not Canadian
> monetary enforcement, final appellate disposition or a universal fine scale.
> **As of:** Penalty notice 2025-06-05; enforcement record checked 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Penalty notice cover and paragraphs 1–3, 8, 11–18 and 400;
> current ICO enforcement record.
> **Basis / limits:** Amount, articles and UK population are direct. The
> penalty notice says its findings are those of the UK Commissioner.

## Safety and contribution boundary

> **Claim record — SRC-0055-C11 | analytic-judgment**
> **Claim:** This package supports a documented genomic privacy incident,
> credential-based threat/control lessons and cross-border investigation, but
> supplies no clinical outcome, physical biological effect, exploit recipe,
> credential corpus or proof that post-event measures reduced harm.
> **Claim status:** active
> **Scope:** Evidence and safety classification for downstream pages; not a
> rubric score decision.
> **As of:** Full-package review 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C02`–`C10`; full retained artifacts.
> **Basis / limits:** Event, governance and privacy effects are direct. No
> operational access details or biological/clinical consequence are needed.

## Integration map

- [INC-0007 — 23andMe incident](../incidents/inc-0007-23andme-genetic-data-breach-2023.md)
- [THR-0004 — Credential-based genetic-data threat](../threats/thr-0004-credential-based-genetic-data-access.md)
- [TEC-0004 — Credential stuffing and linked-profile access](../techniques/tec-0004-credential-stuffing-and-linked-profile-scraping.md)
- [VUL-0005 — Authentication and relative-graph exposures](../vulnerabilities/vul-0005-genetic-service-authentication-and-relative-graph-exposures.md)
- [RSK-0020 — Genomic privacy harm path](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md)
- [CTL-0022 — Genetic-service controls](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md)
- [GOV-0027 — Canada–UK enforcement](../governance/gov-0027-canada-uk-genetic-data-breach-enforcement.md)
- [SYN-0030 — Reconciliation](../syntheses/syn-0030-23andme-genomic-incident-governance-reconciliation.md)
