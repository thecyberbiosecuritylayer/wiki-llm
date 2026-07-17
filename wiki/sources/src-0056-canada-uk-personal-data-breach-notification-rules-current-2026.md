---
id: SRC-0056
type: source
title: Current Canada–UK personal-data breach notification and record rules, 2026
aliases:
  - PIPEDA and UK GDPR breach notification rules
  - Canada UK breach reporting package
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-12
source_type: official-canadian-law-and-current-uk-regulator-guidance-package
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/canada-pipeda-current-2026-05-26.pdf
raw_bytes: 556391
sha256: 7f1b8bfe35eb7f58c3bbeb7c3e10672d34b7ae7951c7aaa1e09bac88be25a3ac
raw_components:
  - path: ../../raw/canada-breach-safeguards-regulations-current-2026-05-26.pdf
    role: current-canadian-prescribed-report-notification-and-record-content
    bytes: 117268
    sha256: 4635a7e70a2590a3c50040ea3bf86828b09e00029f9cbccadfcb356d52e032c5
  - path: ../../raw/uk-ico-personal-data-breaches-guide-current-2026-07-12.html
    role: current-uk-regulator-breach-notification-and-record-guidance
    bytes: 61390
    sha256: 0a733e4f3591069e37f3dd1b2978ddb7ed7d1192acc257890df7e01a7a169473
canonical_url: https://laws-lois.justice.gc.ca/eng/acts/P-8.6/
canada_regulation_url: https://laws-lois.justice.gc.ca/eng/regulations/SOR-2018-64/
uk_guidance_url: https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/
accessed: 2026-07-12
canada_current_to: 2026-05-26
uk_guidance_latest_update: 2025-08-20
issuers:
  - Minister of Justice Canada
  - UK Information Commissioner's Office
jurisdictions:
  - Canada
  - United Kingdom
tags:
  - governance
  - incident-reporting
  - breach-notification
  - record-preservation
  - canada
  - united-kingdom
  - privacy
---

# Current Canada–UK personal-data breach notification and record rules, 2026

## Package identity and reproducibility

The package contains the official Canadian consolidation of the *Personal
Information Protection and Electronic Documents Act* (`PIPEDA`), the official
consolidation of the *Breach of Security Safeguards Regulations*, and the
current ICO guide for UK-GDPR personal-data breaches. The two national regimes
remain separate; this package is a comparison, not a merged legal baseline.

The Canadian PDFs were retrieved twice byte-identically. The ICO HTML was the
same length on repeat retrieval and normalized to identical substantive
content; only a generated disclosure-toggle GUID changed. No form was
submitted and no script was executed.

> **Claim record — SRC-0056-C01 | artifact-observation**
> **Claim:** Three official objects totaling 735,049 bytes are retained with
> exact hashes: the 70-page PIPEDA consolidation, seven-page breach-regulation
> consolidation and complete current ICO breach guide; repeat retrievals
> preserved byte identity for both PDFs and substantive identity for the
> dynamic HTML.
> **Claim status:** active
> **Scope:** Local artifact identity and reproducibility; not legal advice,
> cryptographic authentication of the issuers or proof the live pages cannot
> change.
> **As of:** Retrieved and repeated 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Frontmatter paths, bytes and SHA-256 values; `pdfinfo`, complete
> extracted-text review and normalized repeat-HTML comparison.
> **Basis / limits:** Files and substantive content are reproducible. The ICO
> page is live guidance and contains one generated DOM identifier.

## Canada: threshold, timing and affected-person duties

PIPEDA section 10.1 uses a real-risk-of-significant-harm threshold. When that
threshold is met, an organization reports to the Commissioner and notifies the
affected individual. The Act uses “as soon as feasible,” not the UK 72-hour
formula. Sensitivity and probability of misuse are express risk factors.

> **Claim record — SRC-0056-C02 | source-report**
> **Claim:** PIPEDA section 10.1 requires a Commissioner report and affected-
> individual notification where a breach of safeguards creates a real risk of
> significant harm; reports and notifications are due as soon as feasible,
> and sensitivity plus probability of misuse are express assessment factors.
> **Claim status:** active
> **Scope:** Organizations and personal information within PIPEDA's statutory
> application; not every Canadian public-sector body, provincial regime,
> cross-border fact pattern or legal conclusion.
> **As of:** Consolidation current to 2026-05-26; last amended 2025-03-04.
> **Review after:** 2026-08-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PIPEDA sections 4, 10.1(1)–(8) and 10.2; retained PDF official-
> status/currentness pages and statutory text.
> **Basis / limits:** Threshold, actors, timing and factors are direct law.
> Applicability and risk remain fact-specific.

> **Claim record — SRC-0056-C03 | source-report**
> **Claim:** The Canadian regulations require regulator reports to describe
> circumstances/cause if known, period, data, affected count, mitigation and
> notification steps; individual notices require circumstances, period, data,
> mitigation/advice and contact information, while every breach record is kept
> for 24 months after determination.
> **Claim status:** active
> **Scope:** Prescribed Canadian report, notice and record fields; not proof
> that a particular organization supplied complete or accurate content.
> **As of:** Regulations current to 2026-05-26; last amended 2018-11-01.
> **Review after:** 2026-08-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** *Breach of Security Safeguards Regulations* sections 2, 3 and
> 6; PIPEDA sections 10.1–10.3.
> **Basis / limits:** Required fields and 24-month period are direct. Sector-
> specific or provincial duties are outside this package.

## United Kingdom: risk, 72 hours, individuals and records

The current ICO guide says a controller should establish whether a personal-
data breach occurred, contain and assess it, notify the ICO where risk to
rights and freedoms is likely, and notify individuals without undue delay
where high risk is likely. A feasible 72-hour deadline applies to the ICO
notification, and the controller records all breaches, including those not
reported.

> **Claim record — SRC-0056-C04 | source-report**
> **Claim:** Current ICO guidance states that a likely risk to rights and
> freedoms triggers regulator notification without undue delay and, where
> feasible, within 72 hours; likely high risk triggers direct notice to affected
> people without undue delay, and all personal-data breaches must be recorded.
> **Claim status:** active
> **Scope:** ICO's current UK-GDPR controller guidance; not PECR/eIDAS/NIS
> substitution rules, a legal opinion or proof of compliance.
> **As of:** Guide last updated 2025-08-20; accessed 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** ICO guide headings “At a glance,” “Risk-assessing data
> breaches,” “When do we need to tell individuals,” “What breaches do we need
> to notify the ICO,” “How much time” and record checklist.
> **Basis / limits:** The regulator states the operative guidance directly.
> The page notes related regimes and remains updateable guidance.

> **Claim record — SRC-0056-C05 | source-report**
> **Claim:** The ICO guide requires the notification to describe the breach,
> affected categories/counts where possible, contact point, likely
> consequences and measures taken or proposed; incomplete facts can be supplied
> in phases without undue further delay, and delayed initial reports require
> reasons.
> **Claim status:** active
> **Scope:** UK-GDPR notification content and phased-reporting guidance; not a
> finding about the completeness or timing of a named incident report.
> **As of:** Guide current on 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** ICO guide sections “What information must a breach notification
> to the ICO contain,” “What if we do not have all the required information”
> and “How much time do we have to report.”
> **Basis / limits:** Content and sequencing are directly stated; case-specific
> reasonableness remains for the regulator.

## Reconciliation and evidence role

| Element | Canada | United Kingdom |
| --- | --- | --- |
| Regulator threshold | real risk of significant harm | risk to rights/freedoms likely |
| Regulator timing | as soon as feasible | without undue delay, feasible 72 hours |
| Individual threshold | real risk of significant harm | likely high risk |
| Individual timing | as soon as feasible | without undue delay |
| Records | every breach, prescribed 24 months | every breach; duration not established here |

> **Claim record — SRC-0056-C06 | analytic-judgment**
> **Claim:** Canada and the UK independently supply current reporting,
> affected-person notification and preservation/record rules, but their risk
> thresholds, timing formulas, statutory/guidance forms and exceptions are not
> interchangeable.
> **Claim status:** active
> **Scope:** `THI-GR` evidence role for two jurisdictions; not mutual adequacy,
> extraterritorial applicability, conflict-of-laws resolution or compliance.
> **As of:** 2026-07-12 comparison.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0056-C02`–`C05`; direct independent Canadian law and UK
> regulator guidance.
> **Basis / limits:** Every mapped function is explicit. The package does not
> replace case-specific jurisdiction analysis.

## Scope, notice route and attribution/preservation boundaries

> **Claim record — SRC-0056-C08 | source-report**
> **Claim:** PIPEDA excludes specified federal-government, exclusively
> personal/domestic and exclusively journalistic/artistic/literary processing,
> plus specified business-contact information used solely to communicate in
> an employment/business/professional context, and permits exemption of
> intra-provincial organizations/activities governed by substantially similar
> provincial law; where its breach duty applies, affected-person notice is
> required unless prohibited by law, is normally direct, and becomes indirect
> only for prescribed further-harm, undue-hardship or missing-contact-
> information circumstances.
> **Claim status:** active
> **Scope:** Express federal private-sector application limits and Canadian
> notice route; not a complete provincial, employment or constitutional scope
> opinion.
> **As of:** PIPEDA current to 2026-05-26; regulations current to the same date.
> **Review after:** 2026-08-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** PIPEDA sections 4(2), 4.01, 10.1(3)–(6) and 26(2)(b); *Breach
> of Security Safeguards Regulations* sections 4–5.
> **Basis / limits:** Exclusions, prohibition qualifier and direct/indirect
> route conditions are direct. Other statutes and provincial regimes remain
> outside this package.

> **Claim record — SRC-0056-C09 | source-report**
> **Claim:** Current ICO guidance requires clear affected-person communication
> of the breach nature, a contact point, likely consequences and measures taken
> or proposed, with practical protective advice where possible; its retained
> page does not enumerate the UK-GDPR Article 34(3) exception list or set a
> breach-record retention period.
> **Claim status:** active
> **Scope:** Content directly present or absent in the retained current ICO
> guide; not a claim that the underlying statute contains no exceptions.
> **As of:** Guide checked 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** ICO guide anchors `#whendowe`, `#whatinformationmust`,
> `#authority` and “Does the UK GDPR require us to take any other steps”.
> **Basis / limits:** The content checklist and all-breach record duty are
> direct. Unrepresented statutory detail cannot be inferred from guidance
> silence.

> **Claim record — SRC-0056-C10 | analytic-judgment**
> **Claim:** Neither regime makes known actor attribution a prerequisite for
> reporting: Canada's prescribed report asks for circumstances and cause only
> if known, while the UK minimum-content checklist requires breach nature,
> populations, contact, consequences and measures without an actor field; the
> preservation represented here is a breach-record/accountability duty, not
> forensic-log custody or evidentiary chain of custody.
> **Claim status:** active
> **Scope:** `THI-GR` attribution-governance and preservation semantics; not a
> bar on law-enforcement attribution or a complete evidence-preservation rule.
> **As of:** 2026-07-12 comparison.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Canadian Regulations sections 2(1)(a) and 6; ICO guide anchors
> `#authority` and the Article 33(5) record paragraph; `SRC-0056-C03/C05/C09`.
> **Basis / limits:** Required fields and record purposes are direct; the
> cross-jurisdiction attribution conclusion is conservative comparison.

> **Claim record — SRC-0056-C07 | analytic-judgment**
> **Claim:** This package supplies the current-rule limb consumed by
> `SYN-0030` for `THI-GR`; enforcement/application evidence must come from the
> separate 23andMe investigation package and existing independent case corpus.
> **Claim status:** active
> **Scope:** Evidence-role separation; this source page does not itself decide
> a rubric score or turn guidance into enforcement.
> **As of:** 2026-07-12 corpus state.
> **Review after:** 2026-08-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Frozen `THI-GR/GOV-CI/GOV-AE` criteria in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md); `SRC-0056-C02`–`C06`.
> **Basis / limits:** Rules and case application are distinct evidence roles;
> final reconciliation remains in `SYN-0030`.

## Limitations and safety

The package does not retain personal data, complaint submissions or breach-
report forms. It contains no exploit, credential, evasion or targeting detail.
It does not cover all provincial Canadian privacy regimes, UK PECR/eIDAS/NIS
branches, criminal procedure, litigation preservation or every 2025 Data (Use
and Access) Act consequence.

## Integration map

- [GOV-0027 — Canada–UK 23andMe enforcement](../governance/gov-0027-canada-uk-genetic-data-breach-enforcement.md)
- [INC-0007 — 23andMe incident](../incidents/inc-0007-23andme-genetic-data-breach-2023.md)
- [CTL-0022 — Genetic-service controls](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md)
- [SYN-0030 — Incident/governance reconciliation](../syntheses/syn-0030-23andme-genomic-incident-governance-reconciliation.md)
- [SYN-0001 — Frozen rubric](../syntheses/syn-0001-coverage-rubric.md)

## Official links

- <https://laws-lois.justice.gc.ca/eng/acts/P-8.6/>
- <https://laws-lois.justice.gc.ca/eng/regulations/SOR-2018-64/>
- <https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/>
