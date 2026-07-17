---
id: RSK-0011
type: risk-scenario
title: Part 202 regulated covered-data access with a human-omics/biospecimen branch
aliases:
  - Part 202 covered omics access path
  - regulated country-of-concern or covered-person access to U.S. omics data
  - restricted covered-data access path
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0015
sensitivity: public
dual_use: low
origin_domain: mixed
origin_domain_components:
  - digital
  - biological
destination_domains:
  - digital
  - biological
scenario_classification: regulatory-risk-path-not-incident
transfer_mechanism: regulated-logical-or-physical-access-transaction
relations:
  - predicate: evidenced-by
    target: SRC-0015
    claim_id: RSK-0011-C01
    evidence:
      - source: SRC-0015
        locator: "28 CFR §§202.201, .205–.206, .210–.211, .222–.224 and .301–.401, final-rule PDF pp. 72–85 / 90 FR 1707–1720; correction, 90 FR 16466–16467"
  - predicate: affects
    target: AST-0001
    claim_id: RSK-0011-C02
    evidence:
      - source: SRC-0015
        locator: "§§202.205–.206, .222–.224 and .241, PDF pp. 73, 77–80 / 90 FR 1708, 1712–1715"
  - predicate: depends-on
    target: WFL-0005
    claim_id: RSK-0011-C02
    evidence:
      - source: SRC-0015
        locator: "§§202.201, .210 and Subparts C–E and J–K, PDF pp. 72–95 / 90 FR 1707–1730"
  - predicate: governed-by
    target: GOV-0005
    claim_id: RSK-0011-C03
    evidence:
      - source: SRC-0015
        locator: "Corrected 28 CFR Part 202, especially Subparts B–E"
tags:
  - genomics
  - omics
  - biospecimens
  - covered-person-access
  - regulatory-scenario
  - not-incident
---

# Part 202 regulated covered-data access with a human-omics/biospecimen branch

> [!WARNING]
> **Evidence classification**
> This is a **regulatory risk path**, not a documented data transfer, breach,
> victim, attribution or demonstrated privacy/biological outcome. Part 202
> defines when a class of transactions is prohibited or restricted; it does
> not prove that the path occurred.

## Scenario and two regulatory branches

A defined U.S. person enters or participates in a transaction that gives a
country of concern or covered person regulated access to government-related
data or bulk U.S. sensitive personal data. One cyberbiosecurity-relevant branch
is bulk human-omic data or biospecimens from which bulk human-omic data could
be derived; specified access transactions in that branch are prohibited. A
separate branch covers other data in eligible vendor, employment or investment
transactions and is restricted subject to controls and other duties. The
branches are kept distinct.

> **Claim record — RSK-0011-C01 | source-report**
> **Claim:** Part 202 defines a conditional access path in which actor, data,
> volume, knowledge and transaction conditions determine whether covered
> human-omic or derivable-biospecimen access is prohibited or whether another
> covered-data access transaction is restricted.
> **Claim status:** active
> **Scope:** Regulatory scenario architecture, not an actual transaction or
> conclusion about a named organization.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.201, .205–.206, .210–.211, .222–.224 and .301–.401, PDF pp. 72–85 /
> 90 FR 1707–1720; correcting amendment, 90 FR 16466–16467.
> **Basis / limits:** Conditions and modalities are direct. This page does not
> apply them to a person, reveal protected data or reproduce evasion examples.

## Assets, workflow and system boundary

- [AST-0001](../assets/ast-0001-genomic-data.md) supplies human genomic data and
  derived-data states; Part 202 adds other human-omic and derivable-biospecimen
  regulatory classes without redefining all genomic science.
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) provides the broader
  collection-to-disposition lifecycle; the regulated transition is the access/
  transaction edge, not a new sequencing phase.
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) provides
  storage, cloud, analysis, repository and interface classes; the rule and CISA
  requirements define covered-system responsibility without a deployment
  topology.
- individuals, patients and research participants may be affected
  stakeholders; U.S. persons and counterparties are governance actors.

> **Claim record — RSK-0011-C02 | analytic-judgment**
> **Claim:** The safe end-to-end path is `covered omic data or derivable
> biospecimen → transaction/access boundary → country-of-concern or
> covered-person access → potential privacy/national-security consequence`;
> `AST-0001` and the sharing/reuse/access portion of `WFL-0005` supply the
> represented asset and lifecycle context.
> **Claim status:** active
> **Scope:** Conditional analytic path; no access, recipient use, inference or
> downstream consequence is observed.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.101, .201, .205–.206, .210, .222–.224, .248 and .301–.401,
> PDF pp. 72–85 / 90 FR 1707–1720; CISA requirements, pp. 1–6.
> **Basis / limits:** The regulation supplies digital human-omic and physical
> biospecimen origin states, the access boundary and covered receiving state;
> privacy/national-security effects are consequence categories, not domains or
> empirical events. The `WFL-0005` dependency is limited to its access/sharing
> branch. No linkage, re-identification or misuse method is included.

## Preconditions and governance classification

The path requires all applicable legal predicates, including a covered data
class, relevant quantitative or government-related-data condition, defined
access, a listed transaction form, covered actor relationship and applicable
knowledge state, with no controlling exception or license. Each predicate can
fail independently.

> **Claim record — RSK-0011-C03 | analytic-judgment**
> **Claim:** `RSK-0011` is governed by `GOV-0005` only when the complete Part
> 202 predicates apply; data sensitivity or foreign involvement alone is
> insufficient to classify a transaction as prohibited or restricted.
> **Claim status:** active
> **Scope:** Evidence-calibrated governance boundary, not legal advice.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md),
> §§202.101–.103, Subparts B–E and H, PDF pp. 72–92 / 90 FR 1707–1727.
> **Basis / limits:** Definitions, modalities, exceptions and licenses are
> explicit. Applying them requires current text and facts outside this wiki.

## Consequence and incident boundary

The rule is motivated by national-security and privacy risks, but this source
transaction contains no completed prohibited/restricted transaction,
individual harm, altered clinical/research decision, biological consequence,
enforcement finding or incident attribution. `RSK-0004` remains the separate
conditional genomic disclosure/kin-privacy model; neither scenario is an INC.

## Controls by exact edge

[CTL-0008](../controls/ctl-0008-restricted-data-transaction-controls.md) maps
classification/prohibition to the transaction-decision edge. Organization and
system safeguards apply only to the restricted-data limb's access edge;
logging applies to detection, incident planning to response/recovery and
diligence/audit/records to assurance. Prohibition—not the CISA safeguard
set—is the preventive rule for the human-omic/derivable-biospecimen limb.

## Related pages

- [SRC-0015 — DOJ final rule and correction chain](../sources/src-0015-us-doj-data-security-program-2025.md)
- [GOV-0005 — US Data Security Program](../governance/gov-0005-us-data-security-program-2025.md)
- [CTL-0008 — Part 202 transaction controls](../controls/ctl-0008-restricted-data-transaction-controls.md)
- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [WFL-0005 — Genomic lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003 — Genomic ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [RSK-0004 — Genomic disclosure privacy path](rsk-0004-genomic-data-disclosure-kin-privacy.md)

## Sources

- [SRC-0015](../sources/src-0015-us-doj-data-security-program-2025.md), corrected
  Part 202 and incorporated requirements at the claim locators above.
