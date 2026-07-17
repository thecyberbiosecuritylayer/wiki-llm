---
id: GOV-0027
type: governance
title: Canada–UK 23andMe genetic-data breach investigation and enforcement
aliases:
  - 23andMe OPC ICO enforcement governance
  - Canada UK genetic-data breach findings
  - PIPEDA and UK GDPR 23andMe case application
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-12
source_ids:
  - SRC-0055
  - SRC-0056
jurisdictions:
  - Canada
  - United Kingdom
issuer: Office of the Privacy Commissioner of Canada and UK Information Commissioner's Office
document_type: joint-cross-border-regulatory-findings-with-uk-penalty-and-current-rule-reconciliation
version: PIPEDA Findings 2025-001 with UK Penalty Notice issued 2025-06-05
publication_date: 2025-06-25
adoption_date: not-applicable-case-specific-regulatory-findings
effective_date: uk-penalty-notice-issued-2025-06-05
instrument_status: published-joint-findings-and-current-uk-enforcement-record-checked-2026-07-12
binding_status: case-specific-canadian-findings-and-uk-monetary-enforcement-not-general-cross-border-law
implementation_status: pre-breach-deficiencies-and-company-reported-remediation-regulator-evaluated-independent-effectiveness-unknown
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0055
    claim_id: GOV-0027-C01
    evidence:
      - source: SRC-0055
        locator: "Joint report paragraphs 13–19; UK penalty notice physical pp. 4 and 7, paragraphs 3 and 11"
  - predicate: evidenced-by
    target: SRC-0056
    claim_id: GOV-0027-C02
    evidence:
      - source: SRC-0056
        locator: "PIPEDA sections 10.1–10.3; Breach of Security Safeguards Regulations sections 2–6; current ICO breach guide notification and record sections"
tags:
  - governance
  - genomics
  - consumer-genetics
  - privacy-breach
  - enforcement
  - implementation-evaluation
  - incident-notification
  - canada
  - united-kingdom
  - pipeda
  - uk-gdpr
---

# Canada–UK 23andMe genetic-data breach investigation and enforcement

## Status, force and evidence-lineage boundary

The Office of the Privacy Commissioner of Canada (`OPC`) and the UK
Information Commissioner's Office (`ICO`) jointly investigated the 2023
23andMe breach. They examined one controller, one globally shared customer
platform and one incident record while applying two different national legal
regimes. Their joint work therefore produces two jurisdiction-specific legal
evaluations, but not two independent investigations, deployments or events.

The OPC-hosted findings, UK penalty notice and current ICO enforcement page
are outputs of that one joint investigation. The penalty notice expressly
states that its findings are those of the UK Commissioner only. The company
SEC filings retained in `SRC-0055` are a separate first-party disclosure
lineage, not a second regulator evaluation. None of these case records creates
a generally applicable merged Canada–UK rule.

> **Claim record — GOV-0027-C01 | analytic-judgment**
> **Claim:** The retained governance record is one joint OPC/ICO investigation
> of one controller, shared platform and incident, with separate Canadian and
> UK legal conclusions; the UK penalty notice, enforcement page and related
> company filings must not be multiplied into additional investigations or
> deployments.
> **Claim status:** active
> **Scope:** Evidence-lineage, controller, platform and jurisdiction accounting
> for this case; not a claim that the regulators, statutes or legal conclusions
> are institutionally or legally identical.
> **As of:** Joint findings published 2025-06-25; corpus checked 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C01/C02`; joint report paragraphs 13–19; UK penalty notice
> physical p. 4, paragraph 3, and physical p. 7, paragraph 11.
> **Basis / limits:** The joint character, legal bases, evidence methods and
> UK-only character of the penalty findings are direct. Shared fact-finding
> does not erase the two national decisions, but it prevents independence
> inflation.

## Current national duties are not interchangeable

The current-rule package retains independent Canadian law and current UK
regulator guidance. It is used here to state the two governance frames, not to
retroactively replace the legal provisions applied by the Commissioners to
the 2023 facts.

| Function | Canada | United Kingdom | Reconciliation limit |
| --- | --- | --- | --- |
| Regulator threshold | real risk of significant harm under PIPEDA | likely risk to rights and freedoms under UK-GDPR guidance | thresholds are not declared equivalent |
| Regulator timing | as soon as feasible | without undue delay and, where feasible, within 72 hours | different timing formulas |
| Affected-person threshold | real risk of significant harm | likely high risk | national tests remain separate |
| Notice content | prescribed circumstances, period, data, mitigation and contact fields | breach nature, populations where possible, contact, consequences and measures | phased UK reporting does not excuse undue further delay |
| Records | every breach; prescribed 24-month Canadian period | every breach; no duration established by the retained guide | accountability records are not full forensic-log custody |

> **Claim record — GOV-0027-C02 | analytic-judgment**
> **Claim:** PIPEDA and its breach regulations, and the current UK regulator
> guidance, independently govern reporting, affected-person notification and
> breach records, but their thresholds, timing formulas, notice fields, force
> and exceptions cannot be substituted for one another.
> **Claim status:** active
> **Scope:** Current federal Canadian private-sector and UK-GDPR governance
> represented in `SRC-0056`; not provincial Canadian coverage, every UK
> sectoral regime, conflict-of-laws advice or retroactive adjudication.
> **As of:** Canadian consolidations current to 2026-05-26; UK guide checked
> 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0056](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md),
> `SRC-0056-C02`-`C06/C08`-`C10`; PIPEDA sections 4 and 10.1–10.3;
> *Breach of Security Safeguards Regulations* sections 2–6; current ICO guide
> sections on thresholds, timing, content and records.
> **Basis / limits:** The national duties and express Canadian qualifications
> are direct. The current guide supports present-day reconciliation, while the
> case report remains authoritative for what the ICO found on the historical
> facts.

## Two jurisdiction-specific applications of the shared facts

The joint report did not issue a single blended legal outcome. The OPC applied
PIPEDA to Canadian customers and the UK Commissioner applied the UK GDPR and
Data Protection Act framework to UK customers. Reported populations also have
different jurisdictional and category frames: 769 Canadian and 611 UK
accounts were directly credential stuffed, while broader affected/profile
populations were much larger and partly overlapping. They cannot be summed as
independent or mutually exclusive exposure groups.

| Decision branch | Safeguards | Notification | Resolution/enforcement |
| --- | --- | --- | --- |
| Canada | Principle 4.7 contravention | section 10.1 and Regulations content defects; stuffed-account notices not as soon as feasible | both issues found well-founded and resolved after represented measures; no Canadian monetary penalty is established by this package |
| United Kingdom | Articles 5(1)(f) and 32 infringement | Articles 33/34 content failures; explained initial regulator-report delay accepted in the circumstances | historical infringements remedied by 2024-12-31; UK Commissioner imposed £2.31 million for Articles 5(1)(f)/32 infringements |

> **Claim record — GOV-0027-C03 | source-report**
> **Claim:** The Canadian Commissioner found that 23andMe contravened PIPEDA
> Principle 4.7 and breach-report/notice provisions, including a Canadian
> timing defect for notices to directly accessed account holders, and later
> classified the safeguard and notification issues as well-founded and
> resolved after represented remediation.
> **Claim status:** active
> **Scope:** OPC findings for this private-sector cross-border case; not every
> Canadian affected person, provincial law, a Canadian fine or independent
> measurement of post-remediation performance.
> **As of:** Joint findings published 2025-06-25.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C07`-`C09`; joint report paragraphs 112, 117(a), 118(a),
> 163–164, 183–186, 197–201 and the Canadian conclusions under paragraph
> 201.
> **Basis / limits:** Contraventions, timing distinction and resolution label
> are direct OPC findings. Resolution is a regulatory conclusion, not proof
> that copied data were recovered or future harm was prevented.

> **Claim record — GOV-0027-C04 | source-report**
> **Claim:** The UK Commissioner separately found Articles 5(1)(f) and 32
> safeguard infringements and Articles 33/34 notification-content failures,
> accepted the explanation for the initial regulator report outside 72 hours,
> and imposed a £2.31-million penalty for the Articles 5(1)(f)/32
> infringements affecting 155,592 UK data subjects.
> **Claim status:** active
> **Scope:** UK findings, timing treatment, legal basis, affected population
> and penalty; not a Canadian sanction, a separate investigation, proof of
> payment or final appellate disposition.
> **As of:** Penalty issued 2025-06-05; current enforcement page checked
> 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C07/C08/C10`; joint report paragraphs 113, 117(b), 118(b),
> 161–164, 181–182, 187 and 201; penalty notice physical pp. 4 and 7–9,
> paragraphs 1–3 and 11–18, and physical pp. 134–136, paragraphs 391–400;
> current ICO enforcement record, visible date/type and summary.
> **Basis / limits:** Amount, articles, UK population and timing analysis are
> direct. Notification defects contributed to the case analysis, but the
> retained enforcement record does not support describing the £2.31 million
> as a separate Article 33/34 penalty.

## What implementation the regulators evaluated

The investigation evaluated controls that existed and operated around a real
event rather than only reading a policy design. The shared pre-breach platform
made customer MFA optional; most customers did not use MFA or SSO; password
screening and password-policy controls were inadequate; there was no
additional verification before raw-genetic-data access/download; front-end
testing did not simulate credential stuffing; and no incident-specific
credential-stuffing playbook existed. Monitoring tools were capable of
detection but were not configured to identify the observed login pattern, and
the company did not adequately connect July and August anomalies to the wider
attack.

After verification of the breach, four days elapsed before all active sessions
were disabled and a global password reset was implemented. Self-service raw
DNA download remained available for almost one month, and mandatory email-
based two-step verification took more than a month. These are observed
implementation and response-timing findings, not merely recommendations.

> **Claim record — GOV-0027-C05 | source-report**
> **Claim:** OPC and ICO evaluated actual authentication, password, sensitive-
> download, testing, monitoring, anomaly-investigation and incident-response
> implementation on the shared platform and found material preventive,
> detective and response deficiencies under their respective legal regimes.
> **Claim status:** active
> **Scope:** Controls and response states examined in this incident; not proof
> each deficiency independently caused every access, a universal genetic-
> service control baseline or a reproducible offensive method.
> **As of:** Pre-breach and response implementation in 2023; findings 2025.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C05/C07`; joint report paragraphs 47–51, 57–74, 76–98 and
> 99–113; penalty notice physical pp. 7–9, paragraph 12 and paragraphs
> 16–17, plus Sections VI.C(a)–(d).
> **Basis / limits:** Implemented and missing measures, missed signals and
> response delays are regulator findings. Exact causal contribution and
> counterfactual loss reduction were not experimentally measured.

## Remediation and assurance maturity

The preliminary report called for stronger password screening and policy,
enhanced raw-DNA protection, improved logging and monitoring, regular attack
simulation, governance review and continuing reassessment. By 31 December
2024, 23andMe represented that it had implemented measures including a
12-character minimum password, comparison against the broader compromised-
credential corpus, mandatory email-based two-factor authentication, an
additional raw-DNA-download check and delay, credential-stuffing simulations,
security exercises, new alerts and risk monitoring, customer event history,
reconfigured logs and revised incident processes.

The Commissioners accepted these measures on balance and treated the
safeguard and notification concerns as resolved. The date-of-birth step was
not accepted as a strong standalone authenticator: the report records concerns
that birth dates may be discoverable. More importantly, the record does not
contain independent penetration-test replication, a comparative before/after
incident rate, measured harm reduction, independent outcome validation or
proof that copied information was recovered.

> **Claim record — GOV-0027-C06 | analytic-judgment**
> **Claim:** The joint investigation provides regulator evaluation of
> company-reported remediation in Canada and the UK and a bounded legal
> resolution as of 2024-12-31, but it does not provide independent evidence
> that the controls were effective, caused lower incident or harm rates, or
> recovered previously copied information.
> **Claim status:** active
> **Scope:** Remediation implementation and assurance maturity for this case;
> not a finding that measures were absent, ineffective, permanently adequate
> or independently tested outside the investigation.
> **As of:** Represented remediation through 2024-12-31; evaluated in 2025.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** medium
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C09/C11`; joint report paragraphs 106, 114–117 and 198–200;
> penalty notice physical pp. 86–87, paragraphs 247–250.
> **Basis / limits:** Measures and bounded regulatory acceptance are direct.
> They were principally represented by the company, and the retained record
> supplies no independent effectiveness or outcome test.

## Notification duties as implemented in the case

The initial regulator reports omitted that raw DNA and other sensitive data in
stuffed accounts were accessible, even though 23andMe knew that credential
stuffing exposed all account contents. The OPC received a December 2023
supplementary report, while the ICO did not receive formal raw-DNA notice until
24 June 2024; the UK Commissioner found no evidence that this omission was
intentional.

Timing and content must remain separate. The ICO accepted the explanation for
the first regulator report being outside the 72-hour period, and the OPC
accepted its first report as soon as feasible in the circumstances. Both found
content defects. Notices to DNAR-profile users omitted that data had been
posted for sale, and notices to stuffed-account users omitted or delayed
material facts. The OPC additionally found that directly accessed Canadian
account holders were not notified as soon as feasible. Revised logging and
incident-notification processes were later accepted as resolving the
notification issues, without an independent notification-quality outcome
study.

> **Claim record — GOV-0027-C07 | analytic-judgment**
> **Claim:** The case demonstrates how two non-equivalent national reporting
> regimes were applied to regulator and affected-person notice content and
> timing: initial regulator timing was accepted in context, both regimes
> produced content findings, and Canada separately produced a stuffed-account
> affected-person timing finding.
> **Claim status:** active
> **Scope:** Case application of PIPEDA and UK-GDPR notification duties; not a
> merged deadline, a conclusion that every notice was late or incomplete, or
> use of the current 2026 package as the historical decision itself.
> **As of:** Notifications 2023–2024; findings 2025; current rules checked
> 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C08/C09`; joint report paragraphs 155–187 and 197–200;
> [SRC-0056](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md),
> `SRC-0056-C02`-`C06/C08/C09`.
> **Basis / limits:** Each jurisdiction's timing and content result is direct,
> and current duties are independently located. The comparison does not turn
> contextual acceptance into a general extension or safe harbor.

## Methodology, implementation-evaluation and effectiveness limits

The Offices reviewed company submissions, interviewed key staff and examined
open-source information. They did not obtain every requested record,
including parts of the internal incident logs and the privileged forensic
report; some responses were delayed, incomplete or inconsistent. Original
third-party raw-DNA-download logs were not retained, and the custom log stored
an invalid IP address. The company first identified 18 raw-DNA downloads; a
broader regulator method identified more than 270 potentially attributable
accounts; a later company reanalysis reported four worldwide and none in
Canada or the UK. The Commissioners did not independently verify the revised
four-person figure. The penalty notice also records that attribution to one
actor or group was not conclusive.

These limitations do not erase the directly observed enforcement and
implementation evaluation. They do bound it: this is one real cross-border
case, evaluated under two jurisdictions, for one shared platform. It is not
two independent technical evaluations, two deployments, a representative
consumer-genetics sample or evidence of causal safeguard effectiveness.

> **Claim record — GOV-0027-C08 | analytic-judgment**
> **Claim:** `GOV-0027` supplies direct cross-jurisdiction implementation and
> regulator evaluation for Canada and the UK, with UK monetary enforcement
> and explicit methodological limitations, while preserving one joint
> investigation, one controller and one platform and rejecting any inference
> of independently demonstrated control effectiveness.
> **Claim status:** active
> **Scope:** Evidence role for governance assurance and downstream
> reconciliation; not automatic rubric scoring, two independent deployments,
> sector-wide effectiveness or causal outcome evidence.
> **As of:** Full retained record reviewed 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** medium
> **Evidence:** `GOV-0027-C01`-`C07`;
> [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md),
> `SRC-0055-C02/C07`-`C11`; joint report paragraphs 15–19, 33,
> 188–196 and 201; penalty notice physical p. 8 footnote 9, physical p. 24
> paragraph 56 and physical pp. 62–65, paragraphs 182–192;
> [SRC-0056](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md),
> `SRC-0056-C06/C07/C10`.
> **Basis / limits:** Jurisdiction, actual implementation review, enforcement
> and disclosed evidence gaps are direct. Current independent national rules
> establish two legal frames, but shared case production and absent outcome
> testing prevent claims of replication or effectiveness.

## Cyberbiosecurity and safety boundary

The case connects consumer genetic information, relative graphs, account
security, monitoring, incident response and cross-border privacy governance.
This page retains only defensive governance and assurance abstractions. It
contains no credentials, personal records, raw genetic data, executable
automation, targetable endpoints or instructions for account access.

> **Claim record — GOV-0027-C09 | analytic-judgment**
> **Claim:** The page supports defensive genetic-data incident governance and
> cross-jurisdiction assurance comparison without exposing affected-person
> data or converting public regulator findings into operational attack
> guidance, legal advice or an effectiveness guarantee.
> **Claim status:** active
> **Scope:** Local content and safety classification; not a security assessment
> of the current 23andMe platform or advice for a live breach.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `GOV-0027-C01`-`C08`; local content.
> **Basis / limits:** Only public, defensive governance facts and bounded
> implementation findings are represented.

## Related pages

- [SRC-0055 — 23andMe investigation package](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md)
- [SRC-0056 — Current Canada–UK breach rules](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md)
- [INC-0007 — 23andMe incident](../incidents/inc-0007-23andme-genetic-data-breach-2023.md)
- [CTL-0022 — Genetic-service controls](../controls/ctl-0022-genetic-service-authentication-detection-notification-controls.md)
- [RSK-0020 — Genetic-account privacy-harm path](../risk-scenarios/rsk-0020-genetic-account-access-relative-graph-privacy-harm.md)
- [SYN-0030 — Incident/governance reconciliation](../syntheses/syn-0030-23andme-genomic-incident-governance-reconciliation.md)
- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)

## Sources

- [SRC-0055](../sources/src-0055-23andme-genetic-data-breach-regulatory-investigation-2023-2025.md), at the joint-report, penalty-notice and enforcement locators above.
- [SRC-0056](../sources/src-0056-canada-uk-personal-data-breach-notification-rules-current-2026.md), at the Canadian statutory/regulatory and current UK-guidance locators above.
