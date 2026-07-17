---
id: INC-0007
type: incident
title: 23andMe credential-stuffing and linked genetic-profile breach, 2023
aliases:
  - 23andMe genetic-data breach 2023
  - 23andMe DNA Relatives privacy incident
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-12
event_date: 2023-04-29
event_end_date: 2023-09-20
discovery_date: 2023-10-01
verification_date: 2023-10-05
disclosure_date: 2023-10-06
recovery_date: unknown
source_ids:
  - SRC-0055
  - SRC-0056
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0055
    claim_id: INC-0007-C01
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 3–35 and 188–196; SEC 8-K/8-K-A Item 7.01 and 2024 10-K Item 1A, Item 1C, MD&A and Note 13"
  - predicate: affects
    target: AST-0001
    claim_id: INC-0007-C06
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 28–45 and affected-population/data-type tables"
  - predicate: depends-on
    target: WFL-0005
    claim_id: INC-0007-C05
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 20–33; account, DNA Relatives, ancestry-report, family-tree and raw-DNA access states"
  - predicate: depends-on
    target: VUL-0005
    claim_id: INC-0007-C05
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 47–117; credential reuse, authentication, sensitive-download and linked-profile exposure findings"
  - predicate: governed-by
    target: GOV-0027
    claim_id: INC-0007-C10
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 118–200 and conclusions; UK penalty notice paragraphs 1–18 and 400"
      - source: SRC-0056
        locator: "PIPEDA sections 10.1–10.3; Canadian Breach Regulations sections 2–6; current ICO breach guide"
tags:
  - documented-incident
  - consumer-genetics
  - genomics
  - credential-stuffing
  - genetic-data
  - privacy-breach
  - linked-profiles
  - canada
  - united-kingdom
---

# 23andMe credential-stuffing and linked genetic-profile breach, 2023

> [!WARNING]
> **Evidence classification**
> This is **one incident**, not separate events created from direct-account
> access, linked-profile exposure, three SEC filings, two Commissioners or a
> later UK penalty. The evidence package contains two material lineages:
> 23andMe's evolving first-party SEC disclosures and one joint OPC/ICO
> investigation applying Canadian and UK law. The UK penalty notice and
> enforcement page are outputs of that same joint investigation.

## Event identity and evidence roles

> **Claim record — INC-0007-C01 | analytic-judgment**
> **Claim:** `INC-0007` canonicalizes one 2023 credential-stuffing incident
> across an evolving 23andMe SEC issuer lineage and one materially independent
> joint OPC/ICO investigation, without multiplying filings, jurisdictions,
> regulatory outputs, access populations or remedial stages into separate
> events or investigations.
> **Claim status:** active
> **Scope:** One event and two evidence-production lineages; not two
> independently reconstructed event logs or independent replication of every
> company-supplied population figure.
> **As of:** Event and response 2023–2024; findings through 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C01`–`C03`; joint report paragraphs 3–35; penalty notice
> paragraphs 3 and 11; SEC filing identities and amendment language.
> **Basis / limits:** Issuer and regulator roles are materially different.
> Regulators relied partly on company records and did not independently verify
> every count, so corroboration is claim-specific rather than universal.

## Event, discovery, disclosure, response and recovery timeline

| Date or period | State | Evidence boundary |
| --- | --- | --- |
| 2023-04-29–2023-09-20 | Credential stuffing directly accessed 18,222 customer accounts | Event period; not discovery or public disclosure |
| 2023-04-29–2023-05-16 | First intense period directly accessed 9,974 accounts | Subset of the 18,222 total, not additive to it |
| 2023-07 | Extreme login and attempted profile-transfer anomalies included a platform crash | Regulator-retrospective missed indicators; no procedure is reproduced |
| 2023-08-10 | A claim of a much larger theft was investigated and classified by 23andMe as a hoax | The classification was contemporaneous; later scope does not validate the claimed volume |
| 2023-09 | A second intense period compromised another 4,364 accounts; represented attack activity ended 2023-09-20 | Does not establish the actor's identity or every access time |
| 2023-10-01 | A 23andMe employee found an online post offering customer information; investigation began | Discovery/awareness, not event start |
| 2023-10-05 | 23andMe internally confirmed a successful credential-stuffing breach | Verification is distinct from discovery |
| 2023-10-06 | 23andMe published a website disclosure | Earliest represented company public disclosure; not the SEC filing date |
| 2023-10-09 | All active platform sessions were disabled | Containment action, not proof copied data were recovered |
| 2023-10-10 | Global password reset and all-customer email; original Form 8-K filed | Preliminary disclosure and response, not final scope |
| 2023-10-15 / 2023-10-18 | Initial reports submitted to ICO / OPC | Regulator-notice dates; content findings are separate |
| 2023-11-06 / 2023-11-09 | SEC 8-K/A says the requirement began 2023-11-06; the later joint findings give 2023-11-09 | Source-specific date difference is retained, not silently resolved |
| 2023-12-01 | Form 8-K/A Amendment No. 1 filed | The immutable local filename's `12-05` is not its filing date |
| 2023-12-04 | 23andMe reported updated total and raw-DNA involvement to OPC | A corresponding ICO update was not supplied until 2024-06-24 |
| 2024-01-03 onward | Directly accessed account holders began receiving specific notices | More than a month after stuffed accounts were determined in late November |
| through 2024-12-31 | Additional safeguard and notification-process changes represented to the Commissioners | Bounded regulatory remediation state, not a technical recovery date |
| 2025-06 | UK penalty and joint findings published | Enforcement/findings dates, not event, discovery or recovery dates |

> **Claim record — INC-0007-C02 | analytic-judgment**
> **Claim:** The official record separates attack activity, missed indicators,
> discovery, internal verification, website and SEC disclosure, containment,
> regulator reporting, affected-person notification, remediation and
> enforcement; no filing or findings date is substituted for event start,
> discovery or recovery.
> **Claim status:** active
> **Scope:** Canonical incident-state chronology; not a complete session-level
> forensic log or proof of the actor's activity outside the represented period.
> **As of:** Events 2023–2025 represented in findings dated 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C03/C05/C06`; joint report paragraphs 3–12,
> 20–27, 89–110, 153–187 and 198–200; original/amended 8-K Item 7.01;
> 2024 10-K Item 1C and Note 13.
> **Basis / limits:** Each represented state is directly located. Exact
> minute-level discovery, complete containment and trusted-restoration states
> are not present.

## Affected populations

The investigation separates **directly accessed accounts** from information
reachable through account-to-relative links. These are different units and
must not be added as if mutually exclusive people or accounts.

| Represented population or data view | Canada | United Kingdom | Worldwide | Counting boundary |
| --- | ---: | ---: | ---: | --- |
| Credential-stuffed accounts | 769 | 611 | 18,222 | Accounts directly accessed with valid reused credentials |
| DNA Relatives profiles | 244,583 | 120,031 | 5,497,376 | Linked profile views; not directly accessed accounts |
| Ancestry reports | 245,208 | 120,504 | 5,512,131 | Overlaps DNA Relatives profiles; not additive |
| Family Tree profiles | 74,282 | 35,561 | 1,468,791 | Separate table category; do not add to other rows without deduplication |

Separate official totals also changed over time. On 2023-12-04, 23andMe
reported `6,984,430` affected customers worldwide and `319,635` in Canada.
The UK penalty later covered `155,592` UK data subjects. These totals have
different reporting/legal contexts and are not reconstructed by summing the
table.

> **Claim record — INC-0007-C03 | source-report**
> **Claim:** The joint investigation found 18,222 directly accessed accounts
> worldwide—769 in Canada and 611 in the UK—and a linked-profile fan-out
> involving approximately 5.5 million DNA Relatives profiles, 5.5 million
> ancestry reports and 1.47 million Family Tree profiles, with explicit
> overlap and population-unit limits.
> **Claim status:** active
> **Scope:** Regulator-reported direct-account and linked-view populations;
> not seven million credential-stuffed accounts, unique-person arithmetic,
> prevalence or an independently reconstructed complete census.
> **As of:** Event 2023; figures represented through joint findings 2025.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C03`; joint report paragraphs 20, 28–33 and both
> affected-population tables; penalty notice paragraphs 95–105.
> **Basis / limits:** Counts and table overlap notes are direct findings, but
> much of the underlying census was supplied by 23andMe and was not fully
> independently reconstructed by the Commissioners.

## Data-type boundaries

Linked DNA Relatives/family-tree access could expose names, self-reported year
of birth and location, profile image, race or ethnic origin, relationship
labels, percentage of DNA shared, matching or identical-by-descent segments
and family-tree information. This does **not** mean every linked person had raw
DNA or a health report accessed.

Directly accessed accounts could additionally contain some or all of full
name, date of birth, sex at birth, gender, email, residence, height/weight,
ancestry composition, raw genotype data, genetic-health-risk,
pharmacogenetic/carrier-status reports and self-reported health conditions.
The exact mix differed by account.

| Direct-account data state reported 2024 | Canada | United Kingdom | Worldwide | Boundary |
| --- | ---: | ---: | ---: | --- |
| Raw DNA downloaded, initial estimate | 1 | 0 | 18 | Later revised after further analysis |
| Raw DNA accessed/browsed | 2 | 2 | 49 | Access/browse is not the same as download |
| Health reports | 413 | 320 | 8,217 | Does not mean all report types or all fields per account |
| Self-reported health condition | 2 | 3 | 63 | Separate from genetic health reports |

After the Preliminary Report and further analysis, 23andMe revised the raw-DNA
download figure to four individuals worldwide and none in Canada or the UK.
Between those states, the Commissioners' deliberately broader screening rule
identified more than 270 accounts with downloads **potentially** initiated by
the actor, including 10 in Canada and eight in the UK; that was a conservative
candidate set, not a finding that all 270 downloads were actor-caused. The
Commissioners did not independently verify the final revised four-person
figure. The initial 18, the broader `>270` candidate set and the later four are
retained with their different methods and modalities; none is silently treated
as an immutable ground truth.

> **Claim record — INC-0007-C04 | source-report**
> **Claim:** The breach exposed heterogeneous identity, contact, ancestry,
> race/ethnicity, relationship, genetic and health-information classes, while
> raw-DNA access/browse, raw-DNA download, health reports, directly accessed
> accounts and linked profiles remain separate data and population states.
> **Claim status:** active
> **Scope:** Regulator-described data classes and bounded counts; not a claim
> that every field was present for every person, that all affected information
> was genomic sequence data or that the revised raw-DNA count was independently
> verified.
> **As of:** Event 2023; raw-DNA revision represented 2025-04-30.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C04`; joint report paragraphs 28–33, affected-data
> tables and paragraphs 188–196; penalty notice UK data-category findings.
> **Basis / limits:** Categories and distinctions are direct. Company-supplied
> raw-DNA figures changed after deficiencies in the earlier forensic method
> were identified; the Commissioners' `>270` result is a potential-download
> screening population rather than a confirmed-download count.

## High-level technical dependencies and vector

The safe defensive path is:

`credentials compromised elsewhere and reused → valid account login without
mandatory additional authentication → access to information in that account →
DNA Relatives/family-tree links expand reachable profile information → copying
or download creates persistent confidentiality loss`.

The record identifies actual event conditions rather than only hypothetical
weakness classes:

- credential stuffing had not been treated as a high platform risk;
- MFA was optional and fewer than 22% of customers used MFA or SSO;
- password length/complexity and compromised-password checks were inadequate;
- no additional identity check protected raw-DNA download;
- detection, logging, monitoring and anomaly investigation were inadequate;
- one linked account exposed many relative-profile views by feature design.

The credentials' external origin does not turn these platform conditions into
user-only causation or negate the controller's safeguard duties. Conversely,
the record does not show that the credentials were stolen from 23andMe, that a
software vulnerability was exploited or that core genomic-analysis systems
were penetrated.

> **Claim record — INC-0007-C05 | source-report**
> **Claim:** The event used externally compromised, reused credentials against
> insufficient account-authentication, sensitive-action, detection and linked-
> sharing boundaries, allowing direct-account access to fan out into relative-
> profile exposure; no software exploit, 23andMe credential-origin breach or
> genomic-analysis compromise is established.
> **Claim status:** active
> **Scope:** High-level defensive event dependency and actual exposure state;
> no credential material, endpoint, automation, evasion, request sequence,
> target-selection method or reproducible access procedure.
> **As of:** Event conditions in 2023; regulatory findings 2025.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C03/C04/C07`; joint report paragraphs 20–33,
> 47–117; [VUL-0005](../vulnerabilities/vul-0005-genetic-service-authentication-and-relative-graph-exposures.md);
> [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md).
> **Basis / limits:** Access class, actual weaknesses and feature-mediated
> expansion are direct. Low-level implementation and actor tooling are absent
> and unnecessary for defensive analysis.

## Consequences and explicit non-consequences

Confirmed outcome classes are unauthorized access/copying, loss of control
over sensitive personal information, exposure of genetic-relative
relationships, online sale/publication of some information, notification and
remediation obligations, litigation/inquiries, incident expense and Canadian/
UK legal findings. The UK Commissioner imposed a £2.31-million penalty for
Articles 5(1)(f) and 32(1) infringements affecting 155,592 UK data subjects.

The SEC issuer lineage reports approximately `$4.6 million` of FY2024 incident
expense offset by approximately `$2.8 million` of probable insurance
recoveries; its Adjusted-EBITDA reconciliation reports `$1.765 million` net.
These are company accounting measures, not victim-harm values or the UK fine.

> **Claim record — INC-0007-C06 | analytic-judgment**
> **Claim:** `INC-0007` produced a documented human-genomic privacy, identity,
> kinship, legal and financial consequence, but the retained record does not
> establish altered biological material, corrupted genetic results, clinical
> decision error, care disruption, disease, physical injury or another
> biological/clinical outcome.
> **Claim status:** active
> **Scope:** Confirmed incident outcomes and nonpromotion boundary; not denial
> of possible psychological, discrimination, fraud or future misuse risks.
> **As of:** Event consequences and findings through 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C04/C06/C08/C10/C11`; joint report paragraphs
> 28–45, 118–187 and conclusions; penalty notice; 10-K Item 1A, MD&A and
> Note 13; [AST-0001](../assets/ast-0001-genomic-data.md).
> **Basis / limits:** Confidentiality/legal/accounting consequences are direct.
> Regulators assessed serious risk and sensitivity, not a measured biological
> change or case-level clinical injury.

## Evolving company disclosure and regulatory reconstruction

| Record | Represented state | Boundary |
| --- | --- | --- |
| Original 8-K, 2023-10-10 | Preliminary reused-credential explanation; scope and costs unknown; no indication credentials came from 23andMe | One issuer's early assessment, furnished under Item 7.01 |
| 8-K/A, 2023-12-01 | `0.1%` direct-account estimate, unspecified significant linked-profile files, password reset, mandatory two-step verification, contained activity and investigation believed complete | No 6.9-million absolute total; local filename date is misleading |
| 2024 10-K, 2024-05-30 | Approximately 5.5 million DNA Relatives and 1.5 million Family Tree profiles; incident expense, litigation and current cyber programme | Filed issuer record; not independent incident validation |
| Joint OPC/ICO findings, 2025 | Exact attack period, direct-account count, linked-profile/data classes, missed indicators, safeguards, notification defects and bounded remediation | One joint investigation under two legal regimes |

The later regulatory record materially expands and qualifies the early issuer
account. It supports the external credential-stuffing cause but challenges the
breadth of phrases such as `immediate action` and the finality of
`investigation complete`: the Commissioners found response delays and later
forensic revisions. The issuer and regulators are not collapsed into one
voice.

> **Claim record — INC-0007-C07 | analytic-judgment**
> **Claim:** The SEC lineage evolved from preliminary, percentage/vague-scope
> reporting to larger linked-profile and financial disclosure, while the joint
> investigation supplies the materially independent current event
> reconstruction and identifies response/forensic qualifications; the three
> filings remain one issuer lineage.
> **Claim status:** active
> **Scope:** Evidence-role and temporal reconciliation; not an allegation that
> every early statement was false or that a later regulator independently
> reproduced every company count.
> **As of:** SEC filings through 2024-05-30; findings 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C02/C05/C06`; original and amended 8-K Item 7.01;
> 10-K Item 1A, Item 1C, MD&A and Note 13; joint report paragraphs 3–35,
> 89–110 and 188–196.
> **Basis / limits:** Filing identities, dates and statements are direct.
> `0.1%` has no represented denominator and is not converted into an invented
> absolute count or labeled a mathematical contradiction.

## Response, containment, remediation and recovery

Represented response included investigation and external incident-response
support, disabling sessions, password reset, mandatory email-based two-step
verification, temporary restriction of raw-DNA downloads, affected-person and
regulator notification, removal efforts for posted information and later
changes to authentication, password screening, monitoring, customer event
history, sensitive downloads, exercises and incident procedures.

The Commissioners later accepted that represented measures through
2024-12-31 resolved their safeguard and notification concerns. This is a
bounded legal/remedial conclusion. It is not an independently measured
before/after cyber outcome, proof of permanent effectiveness, return or
deletion of copied information, or complete technical recovery. The joint
record says stolen data had not been recovered; a full recovery date remains
unknown.

> **Claim record — INC-0007-C08 | analytic-judgment**
> **Claim:** Sessions, credentials, authentication, monitoring and response
> processes were changed and the Commissioners accepted a bounded remediation
> state, but copied data were not shown recovered and no complete technical,
> privacy or harm-reversal endpoint or comparative control-effectiveness result
> is demonstrated.
> **Claim status:** active
> **Scope:** Response/remediation/recovery distinction for this incident; not a
> conclusion that later controls had no benefit.
> **As of:** Measures represented through 2024-12-31; findings 2025.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** medium
> **Evidence:** `SRC-0055-C05/C09`; joint report paragraphs 103–117,
> 188–200; 8-K/A Item 7.01; 10-K Item 1C.
> **Basis / limits:** Implementation and legal resolution are direct. Measures
> were principally company-reported, and no controlled comparator,
> independent penetration retest or measured victim-outcome reduction is
> retained.

## Safeguard findings

> **Claim record — INC-0007-C09 | source-report**
> **Claim:** OPC and ICO found pre/during-incident safeguards inappropriate
> for the sensitivity and scale of the information, including deficiencies in
> credential-stuffing risk treatment, authentication/password controls,
> sensitive-download protection, detection/logging, anomaly investigation and
> credential-stuffing response preparedness; they reached PIPEDA Principle
> 4.7 and UK-GDPR Articles 5(1)(f)/32 conclusions.
> **Claim status:** active
> **Scope:** One platform and incident assessed under two legal regimes; not a
> universal consumer-genetics baseline or proof each deficiency independently
> caused every exposed field.
> **As of:** Safeguards relevant to the 2023 breach; findings 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C07`; joint report paragraphs 37–117, especially
> 47–51, 61–88 and 103–113; penalty notice Sections VI.C(a)–(e).
> **Basis / limits:** Technical/organizational and legal findings are direct.
> Two legal conclusions from one joint fact-finding process are not counted as
> two independent technical tests.

## Notification and governance findings

The case-specific timing findings differ by jurisdiction:

- OPC accepted initial regulator reporting as soon as feasible, but found
  direct-account notices beginning in January 2024 were not as soon as
  feasible under PIPEDA;
- ICO accepted the explanation for initial regulator reporting outside 72
  hours, but found required regulator- and affected-person-notice content
  incomplete;
- both found notification-content problems, including incomplete description
  of possible raw-DNA involvement; affected-person communications also failed
  in relevant instances to state that some information had been offered for
  sale online.

These are not interchangeable findings that every notice in both countries
was late. Current Canadian and UK rules remain distinct from the historical
case application.

> **Claim record — INC-0007-C10 | source-report**
> **Claim:** The joint investigation found Canada/UK notification-content
> deficiencies and jurisdiction-specific timing outcomes: Canada additionally
> found delayed direct-account notices, while the UK accepted the explained
> regulator-report timing but found Articles 33/34 content failures; the UK
> penalty arose from the same joint investigation.
> **Claim status:** active
> **Scope:** Case-specific PIPEDA/UK-GDPR application and UK enforcement; not a
> merged cross-border deadline, a claim all notices were late or independent
> duplication of the joint investigation.
> **As of:** Notifications 2023–2024; findings/penalty 2025; current rules
> checked 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C08/C10`; joint report paragraphs 118–187 and
> conclusions; penalty notice paragraphs 1–18 and 400;
> [SRC-0056](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md),
> `SRC-0056-C02`–`C10`; [GOV-0027](../governance/gov-0027-canada-uk-genetic-data-breach-enforcement.md).
> **Basis / limits:** Timing, content, jurisdiction and lineage are explicit.
> Current-rule sources contextualize rather than retroactively replace the
> Commissioners' case findings.

## Investigation, attribution and uncertainty

The Commissioners reviewed company submissions, interviews and open-source
material. They did not receive every requested underlying log or the
privileged independent forensic report, and they did not independently verify
the final revised raw-DNA-download figure. Some account/profile counts derive
from 23andMe's analysis. The source does not identify or adjudicate a named
actor, sponsor or motive.

> **Claim record — INC-0007-C11 | analytic-judgment**
> **Claim:** The joint investigation is materially independent from the SEC
> issuer lineage but is not a de novo complete forensic reconstruction:
> underlying evidence access was incomplete, several counts were company-
> supplied, raw-DNA analysis moved from 18 attributed downloads through a
> broader `>270` potential-account screen to a revised company estimate of
> four, and the actor remains unattributed.
> **Claim status:** active
> **Scope:** Investigation and attribution confidence; not a rejection of the
> Commissioners' legal findings or established direct-account/event period.
> **As of:** Joint record through 2025-06-25.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0055-C02/C03/C04`; joint report methodology and
> paragraphs 188–196; penalty notice evidence/representation limits.
> **Basis / limits:** Source access and verification limits are direct. The
> page therefore grades individual predicates instead of assigning one
> confidence label to the whole incident.

## Safety boundary

This page retains only public high-level event, exposure, consequence, response
and governance evidence; it contains no credential, account identifier,
endpoint, request pattern, automation/evasion guidance, target-selection
method, downloadable record, personal data, exploitation sequence or
operational recovery instruction.

> **Claim record — INC-0007-C12 | analytic-judgment**
> **Claim:** This page retains only public high-level event, exposure,
> consequence, response and governance evidence; it contains no credential,
> account identifier, endpoint, request pattern, automation/evasion guidance,
> target-selection method, downloadable record, personal data, exploitation
> sequence or operational recovery instruction.
> **Claim status:** stale
> **Scope:** Local page content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content; no external source is applicable to this
> editorial self-audit.
> **Limits:** Retained as a historical local-content audit, not as an
> externally evidenced decision claim. The current safety boundary is the
> prose above.

## Related pages

- [SRC-0055 — Incident evidence package](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md)
- [SRC-0056 — Current Canada–UK notification rules](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md)
- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [WFL-0005 — Genomic-data lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [THR-0004 — Credential-based genetic-data threat](../threats/thr-0004-credential-based-genetic-data-access.md)
- [TEC-0004 — Credential stuffing and linked-profile access](../techniques/tec-0004-credential-stuffing-and-linked-profile-scraping.md)
- [VUL-0005 — Authentication and relative-graph exposures](../vulnerabilities/vul-0005-genetic-service-authentication-and-relative-graph-exposures.md)
- [RSK-0020 — Genomic privacy-harm path](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md)
- [CTL-0022 — Genetic-service controls](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md)
- [GOV-0027 — Canada–UK enforcement](../governance/gov-0027-canada-uk-genetic-data-breach-enforcement.md)
- [SYN-0030 — Incident/governance reconciliation](../syntheses/syn-0030-23andme-genomic-incident-governance-reconciliation.md)
