---
id: SRC-0040
type: source
title: FBI statement on JBS cyberattack, June 2021
aliases:
  - FBI Statement on JBS Cyberattack
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: official-us-federal-law-enforcement-statement
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/fbi-statement-jbs-cyberattack-current-2026-07-12.html
sha256: 9adc10bd602c34b8c48df324308e88bcc1985e84e72ab71cd70a7bbc66941ebb
canonical_url: https://www.fbi.gov/news/press-releases/fbi-statement-on-jbs-cyberattack
accessed: 2026-07-12
published: 2021-06-02
page_modified: 2022-07-21T15:50:01+00:00
issuer: Federal Bureau of Investigation
issuing_office: FBI National Press Office
jurisdictions:
  - United States
tags:
  - agriculture
  - food-processing
  - jbs
  - cyberattack
  - attribution
  - law-enforcement
  - incident-context
---

# FBI statement on JBS cyberattack, June 2021

## Identity, acquisition and complete review

The retained artifact is the complete current FBI HTML presentation of *FBI
Statement on JBS Cyberattack*, published 2 June 2021 by the FBI National Press
Office. Embedded metadata reports modification on 21 July 2022. The page's
title, date, issuing-office block and single substantive paragraph were
reviewed in full on 2026-07-12.

- The retained official HTML is 50,011 bytes.
- A repeat official retrieval had the same size and identical title, date,
  metadata description and substantive paragraph, but a different hash because
  dynamic metadata ordering, body configuration and Cloudflare tokens changed.
  The comparison copy remained temporary.
- Static inspection found ten script, three form and six image tags, with no
  literal iframe/object/embed tag. A Cloudflare inline script contains code
  that would create a hidden iframe if executed. Nothing was executed or
  submitted; the counts are artifact observations, not runtime assurance.
- Initial no-trailing-slash acquisitions were challenged with HTTP 403 and
  created no raw object. A browser-compatible request to the canonical content
  path returned the complete HTTP 200 official page. The retained page's own
  canonical tag points to the URL above.

> **Claim record — SRC-0040-C01 | artifact-observation**
> **Claim:** The retained 50,011-byte artifact is a complete current official
> FBI HTML presentation whose title, publication/modified dates, issuing office
> and substantive paragraph were fully reviewed, with dynamic-repeat and
> static-script/form/iframe limits recorded.
> **Claim status:** active
> **Scope:** Retained official page and acquisition process; not cryptographic
> authentication, runtime assurance or proof that content never changed.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Raw HTML, hash and canonical/metadata/title/date/body elements
> described above; repeat retrieval comparison.
> **Basis / limits:** Identity and content are directly reproducible. Dynamic
> bytes are not presented as stable; the official page has no signed artifact.

## Publication role and scope

This is a short law-enforcement statement, not an indictment, technical
advisory, victim disclosure or economic consequence report. It identifies the
FBI as the lead federal investigative agency for cyber threats, states an
attribution and describes law-enforcement/private-sector response posture.

> **Claim record — SRC-0040-C02 | source-report**
> **Claim:** `SRC-0040` is an official FBI National Press Office statement
> about the JBS cyberattack and the FBI's investigative/partnership posture,
> not a technical incident report or measured consequence study.
> **Claim status:** active
> **Scope:** Issuer, publication class and self-described role; not a legal
> finding, adjudicated attribution, prosecution result or independent audit.
> **As of:** Published 2021-06-02; page reviewed 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Page title, date, `Washington, D.C./FBI National Press Office`
> block and complete substantive paragraph.
> **Basis / limits:** Page identity and role are direct. Institutional
> self-description is not external validation of investigative quality.

## JBS attribution statement

The FBI states that it attributed the JBS attack to names `REvil` and
`Sodinokibi` and was working to bring the responsible threat actors to justice.
The page does not explain whether the two names are aliases, enumerate actors,
publish attribution methodology or provide corroborating technical material.

> **Claim record — SRC-0040-C03 | source-report**
> **Claim:** The FBI attributes the JBS attack using the names `REvil` and
> `Sodinokibi` and refers to responsible cyber actors.
> **Claim status:** active
> **Scope:** FBI attribution statement at safe abstraction; not actor identity/
> number, alias resolution, ransomware classification, technical proof,
> conviction or independently adjudicated fact.
> **As of:** 2021-06-02.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Complete substantive paragraph, sentence beginning `We have
> attributed the JBS attack...`.
> **Basis / limits:** Attribution and names are direct source reporting. The
> statement supplies no method, evidence, confidence scale or procedural detail.

## Response and reporting posture

The statement says the FBI was working to impose consequences and hold actors
accountable, treats private-sector partnerships as important to rapid response
and victim support, and encourages cyberattack victims to notify an FBI field
office. It does not report an arrest, seizure, decryption, restoration or
effectiveness result for JBS.

> **Claim record — SRC-0040-C04 | source-report**
> **Claim:** The FBI describes an investigative/accountability objective,
> private-sector response partnership and victim-reporting channel, without
> reporting a completed JBS enforcement or recovery outcome.
> **Claim status:** active
> **Scope:** High-level response posture in the statement; not a deployed JBS
> safeguard, response timeline, technical procedure or measured effectiveness.
> **As of:** 2021-06-02.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Complete substantive paragraph after the attribution sentence.
> **Basis / limits:** Objectives, partnership and reporting language are direct.
> No case outcome or performance metric appears.

## Technical and consequence absences

The page does not state when the JBS event began, which countries or facilities
were disrupted, whether production/slaughter changed, when operations resumed,
or whether food, animal, financial or market consequences occurred. It also
does not explicitly call the attack ransomware or identify a vector,
vulnerability, affected IT/OT system, payment or control failure.

> **Claim record — SRC-0040-C05 | artifact-observation**
> **Claim:** Complete review finds no source support for event timing, facility/
> throughput/recovery consequence, explicit ransomware classification, vector,
> vulnerability, affected digital/OT-system type or topology, payment or
> safeguard-effectiveness claims.
> **Claim status:** active
> **Scope:** Retained FBI page; not a claim that those facts were unknown or
> unsupported in other independent/first-party records.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Complete title/date/office/body/metadata review.
> **Basis / limits:** The substantive page is one paragraph and the absences
> are directly checkable. No fact is imported from adjacent FBI publications.

## Independence and event-identity boundary

The FBI statement and USDA ERS `SRC-0039` have materially distinct roles:
law-enforcement incident attribution versus agricultural economic/throughput
analysis. They concern the same JBS event. The FBI statement independently
confirms an FBI-recognised JBS cyberattack and attribution context; it does not
independently confirm USDA's plant, date, slaughter or recovery measurements.

> **Claim record — SRC-0040-C06 | analytic-judgment**
> **Claim:** `SRC-0040` can provide materially independent incident/
> attribution context for the USDA consequence record, but it is neither a
> second incident nor an independent measurement of the cattle-slaughter
> consequence.
> **Claim status:** active
> **Scope:** Evidence-lineage role for the JBS event; not blanket independence
> of every claim or a final SF3 criterion decision.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0040-C02`–`C05`;
> [SRC-0039](src-0039-usda-ers-jbs-cyberattack-cattle-slaughter-2021.md),
> `SRC-0039-C02`–`C07`.
> **Basis / limits:** Issuers, functions and evidence objects differ, while
> event identity is shared. Consequence figures remain USDA-only.

## Rubric contribution and score boundary

Together with `SRC-0039`, the statement created a candidate SF3 structure at
the source-transaction checkpoint: direct official observed processing-
throughput consequence plus materially independent incident/attribution
context. `INC-0004/SYN-0025` later supplied the required bounded event and
criterion-level reconciliation.

> **Claim record — SRC-0040-C07 | analytic-judgment**
> **Claim:** `SRC-0040` strengthens candidate evidence for `AGE-CI` and one
> agriculture incident-context role, but this source transaction alone changes
> no frozen cell or global gate.
> **Claim status:** superseded
> **Scope:** Wiki after one FBI source transaction; no incident page, score
> transition, independent consequence replication or control-effectiveness
> conclusion.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0040-C02`–`C06`; `SRC-0039-C02`–`C08`; `AGE-CI`/SF3 in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** Independent context is now present, but score changes
> require a bounded canonical event and audited reconciliation rather than
> arithmetic source accumulation.
> **Superseded by:** `SYN-0025-C06`, after canonical same-event reconciliation
> with USDA as the sole consequence-measurement role.

> **Claim record — SRC-0040-C08 | analytic-judgment**
> **Claim:** The page is defensive and reproduces no indicators, malicious-
> software behavior, access vector, vulnerability, affected-system topology,
> payment detail or operational response procedure.
> **Claim status:** active
> **Scope:** Local page content, not the complete public raw HTML.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content compared with complete HTML review.
> **Basis / limits:** Attribution names are retained because they are the
> direct evidentiary contribution; no actionable operational detail is added.

## Limitations and conflicts

- One-paragraph FBI statement provides no attribution method or technical
  evidence and is not an adjudicated case result.
- It does not explicitly classify the event as ransomware.
- It supplies no closure, throughput, food/animal/market consequence or
  restoration measurement.
- Partnership and reporting language are not implementation or effectiveness.
- FBI and USDA roles are independent for relevant claims but describe one
  event; their evidence cannot be counted as two incidents or two consequence
  measurements.

## Integration map

- [SRC-0039](src-0039-usda-ers-jbs-cyberattack-cattle-slaughter-2021.md)
- [RSK-0017](../risk-scenarios/rsk-0017-agriculture-cyber-disruption-production-supply-cascade.md)
- [THR-0002](../threats/thr-0002-ransomware-against-agriculture-production-and-supply.md)
- [SYN-0001](../syntheses/syn-0001-coverage-rubric.md)
- [INC-0004](../incidents/inc-0004-jbs-cyberattack-cattle-slaughter-disruption-2021.md)
- [SYN-0025](../syntheses/syn-0025-agriculture-system-threat-transfer-consequence-control-reconciliation.md)
