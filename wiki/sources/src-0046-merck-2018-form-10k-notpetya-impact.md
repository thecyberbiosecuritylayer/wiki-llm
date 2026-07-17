---
id: SRC-0046
type: source
title: Merck 2018 Form 10-K cyberattack manufacturing and order impact record
aliases:
  - Merck 2018 10-K cyberattack impact
  - Merck NotPetya first-party manufacturing record
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_type: official-sec-filed-company-primary-incident-record
ingest_status: complete
sensitivity: public
dual_use: low
raw_path: ../../raw/merck-2018-form-10-k-2019-02-27.html
raw_bytes: 4496118
sha256: 948b71784cc44d599d7af67f7a41da6628d42bfe01df5398eba09fc60545a17e
canonical_url: https://www.sec.gov/Archives/edgar/data/310158/000031015819000014/mrk1231201810k.htm
accessed: 2026-07-12
filing_date: 2019-02-27
report_period_end: 2018-12-31
issuer: Merck and Co. Inc.
jurisdictions:
  - United States
tags:
  - biomanufacturing
  - pharmaceuticals
  - cyberattack
  - manufacturing-disruption
  - order-backlog
  - sec-filing
  - incident
---

# Merck 2018 Form 10-K cyberattack manufacturing and order impact record

## Identity, acquisition and review

The retained artifact is Merck's complete 2018 Form 10-K HTML filing from the
official SEC EDGAR archive. The 4,496,118-byte static filing has no script,
form or iframe elements; a fresh retrieval was byte-identical. It was reviewed
as HTML and as a complete plain-text rendering. The issuer is the affected
company, so its operational and financial figures are primary first-party
reporting, not independent investigation.

> **Claim record — SRC-0046-C01 | artifact-observation**
> **Claim:** The retained 4,496,118-byte artifact is the complete official SEC
> HTML filing for Merck's 2018 Form 10-K, filed 2019-02-27, with an exact hash
> and byte-identical repeat retrieval.
> **Claim status:** active
> **Scope:** Artifact identity and completeness; not SEC verification of every
> company assertion or independent incident evaluation.
> **As of:** 2026-07-12 acquisition.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Retained HTML; EDGAR filing header and report-period fields;
> local size/hash/repeat checks.
> **Basis / limits:** EDGAR authenticates the filed record and filing context;
> substantive incident statements remain Merck's reporting.

## Direct incident and supply consequence

> **Claim record — SRC-0046-C02 | source-report**
> **Claim:** Merck reports that a 2017 network cyberattack disrupted worldwide
> manufacturing, research and sales operations.
> **Claim status:** active
> **Scope:** Merck worldwide operational classes; not every site, system,
> product or production step.
> **As of:** Event in 2017; filing through 2018-12-31.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Form 10-K HTML anchor `sC5918D6835605DFB9861637AED9AB7C7`,
> Item 1A risk-factor subsection, displayed printed p. 25; anchor
> `s02DF6574F3035C8485C795D393F48705`, MD&A `Cyber-attack`, displayed
> printed p. 38.
> **Basis / limits:** The statement is direct and repeated in the filing. It
> does not identify affected manufacturing systems or production stages.

> **Claim record — SRC-0046-C03 | source-report**
> **Claim:** Merck reports inability to fulfil orders for certain unnamed
> products in certain unnamed markets, approximately $260 million adverse 2017
> sales effect, approximately $150 million adverse 2018 sales effect from the
> residual order backlog, and approximately $285 million of 2017 manufacturing-
> related and remediation expenses net of approximately $45 million insurance
> recoveries.
> **Claim status:** active
> **Scope:** Company-reported sales/expense measures; not lost physical-product
> volume, shortage prevalence, patient access, batch quality or net total loss.
> **As of:** 2017–2018 effects reported 2019-02-27.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Item 1A anchor `sC5918D6835605DFB9861637AED9AB7C7`,
> displayed printed p. 25; MD&A `Cyber-attack` anchor
> `s02DF6574F3035C8485C795D393F48705`, displayed printed p. 38.
> **Basis / limits:** Values and scopes are literal. Manufacturing variances
> and remediation are aggregated, and product/market identities are absent.

> **Claim record — SRC-0046-C04 | analytic-judgment**
> **Claim:** The unfulfilled-order/backlog branch is a direct primary supply
> consequence beyond generic IT outage and a candidate `BMO-CI` anchor, while
> Merck remains the sole source measuring that consequence.
> **Claim status:** superseded
> **Scope:** Frozen BMO consequence literal before independent-context
> reconciliation; not independent confirmation or automatic score promotion.
> **As of:** 2026-07-12 corpus state before `SYN-0028`.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0046-C02/C03`; `BMO-CI` criterion in
> [SYN-0001](../syntheses/syn-0001-coverage-rubric.md).
> **Basis / limits:** The filing directly crosses manufacturing disruption to
> order fulfilment; SF3 still requires a materially independent role.
> **Superseded by:** `SYN-0028-C05`, after canonical incident and independent-
> context reconciliation.

## Confounders and excluded outcomes

> **Claim record — SRC-0046-C05 | source-report**
> **Claim:** The filing reports that Merck's decision to borrow Gardasil 9
> doses from a CDC pediatric vaccine stockpile was driven partly by the
> temporary cyberattack-related shutdown and partly by higher-than-expected
> demand; partial 2017 and remaining 2018 replenishment and the separate
> $125 million accounting effects are not merged with the cyberattack's
> $260 million order/sales effect.
> **Claim status:** active
> **Scope:** Financial-report separation and causal boundary.
> **As of:** 2017 reporting in the 2018 Form 10-K.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** MD&A/Sales discussion at displayed printed pp. 38–39;
> Vaccines anchor `sBB3EEB5901095A398997106BC9F8CDA1`, displayed printed
> p. 41, paragraphs on the CDC Pediatric Vaccine Stockpile.
> **Basis / limits:** Cyber shutdown and demand are explicit co-drivers. The
> $125 million reversal/recognition is an accounting treatment, not a measured
> shortage, patient outcome or additive incident-loss estimate.

> **Claim record — SRC-0046-C06 | analytic-judgment**
> **Claim:** The filing supplies no product or market identity for the
> unfulfilled-order/backlog branch, batch-quality deviation, unsafe release,
> product destruction, patient injury, shortage count, exact outage duration,
> system topology, initial-access vector or actor attribution. Gardasil 9 is
> named only in the separate stockpile branch whose drivers are explicitly
> mixed between the temporary cyberattack shutdown and higher demand.
> **Claim status:** active
> **Scope:** Full-filing incident-gap audit; absence from this filing, not
> evidence that no such fact existed elsewhere.
> **As of:** 2026-07-12 review.
> **Review after:** 2026-10-15.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Full retained filing; `SRC-0046-C02`–`C05`.
> **Basis / limits:** Product identity is absent only for the backlog branch;
> the named mixed-cause Gardasil branch is preserved separately. The later
> court lineage has a different technical/adjudicative role.

## Response and assurance boundary

> **Claim record — SRC-0046-C07 | source-report**
> **Claim:** Merck reports implemented system-enhancement/modernisation and an
> enterprise resilience effort intended to prevent similar attacks, speed
> recovery and support continuity, but provides no safeguard-specific test,
> comparator, outcome metric or independent evaluation.
> **Claim status:** active
> **Scope:** Issuer-reported implementation objective, not tested/effective
> control state or trusted recovery of a named system.
> **As of:** Filing through 2018-12-31.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Item 1A anchor `sC5918D6835605DFB9861637AED9AB7C7`,
> displayed printed p. 25, paragraphs following insurance coverage; filing
> caveat that success cannot be assured.
> **Basis / limits:** Implementation and intended purpose are direct; test and
> effectiveness predicates are absent.

> **Claim record — SRC-0046-C08 | analytic-judgment**
> **Claim:** This filing can support incident chronology, consequence and
> issuer-response lessons, but cannot by itself satisfy independent SF3,
> `BMO-AE`, `CTR-AE` or any global control gate.
> **Claim status:** active
> **Scope:** Source-level rubric/evidence-state boundary; not the final
> cross-source synthesis decision.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SRC-0046-C01`–`C07`; frozen source floors and criteria.
> **Basis / limits:** One issuer filing is not independent confirmation or
> effectiveness evaluation.

## Safety boundary

> **Claim record — SRC-0046-C09 | analytic-judgment**
> **Claim:** The page retains only public high-level event, manufacturing,
> supply, financial and evidence-state information; it exposes no endpoint,
> credential, exploit, vulnerable product, network path, facility topology,
> process setting, recipe or operational response procedure.
> **Claim status:** active
> **Scope:** Local page content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local content and explicit exclusions.
> **Basis / limits:** Defensive consequence abstraction is sufficient for the
> rubric; technical reproduction is unnecessary.

## Integration map

- [INC-0006](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md)
- [RSK-0019](../risk-scenarios/rsk-0019-merck-cyber-manufacturing-supply-disruption.md)
- [CTL-0020](../controls/ctl-0020-merck-incident-vendor-update-continuity-recovery-lessons.md)
- [SYN-0028](../syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)
- [WFL-0003](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
- [AST-0007](../assets/ast-0007-biomanufacturing-assets-stakeholders.md)
