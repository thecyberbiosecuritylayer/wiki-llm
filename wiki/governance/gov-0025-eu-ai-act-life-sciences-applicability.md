---
id: GOV-0025
type: governance
title: EU AI Act staged GPAI and medical-device governance with pending 2026 amendment
aliases:
  - EU AI Act current staged governance
  - EU GPAI and medical-device AI governance
  - Digital Omnibus on AI pending amendment status
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-19
source_ids:
  - SRC-0053
jurisdictions:
  - European Union
issuer: European Parliament and Council of the European Union, with Commission and AIB/MDCG implementation companions
document_type: binding-eu-regulation-with-staged-application-and-nonbinding-implementation-companions
version: Regulation EU 2024/1689 base text with 2026 Digital Omnibus adopted but awaiting Official Journal publication
publication_date: 2024-07-12
adoption_date: 2024-06-13
effective_date: 2024-08-01
instrument_status: base-in-force-and-partly-applicable-pending-amendment-awaiting-oj-checked-2026-07-12
binding_status: base-regulation-binding-guidelines-and-faq-nonbinding-code-voluntary-pending-amendment-not-operative
implementation_status: formal-issuance-and-staged-application-observed-operator-implementation-and-outcomes-unknown
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0053
    claim_id: GOV-0025-C01
    evidence:
      - source: SRC-0053
        locator: "AI Act Article 113, PDF physical p. 123; Parliament T10-0198/2026 amendment (40) and Article 4; OEIL 2025/0359(COD) status and key events checked 2026-07-12"
tags:
  - governance
  - european-union
  - ai-act
  - general-purpose-ai
  - medical-devices
  - in-vitro-diagnostics
  - scientific-research
  - staged-application
  - pending-amendment
---

# EU AI Act staged GPAI and medical-device governance with pending 2026 amendment

## Status, force and temporal boundary

Regulation (EU) 2024/1689 is in-force, binding EU law, but it does not apply as
one block. Under base Article 113, Chapters I-II have applied since 2 February
2025; the named governance, GPAI and penalty provisions have applied since
2 August 2025; general application begins 2 August 2026; and Article 6(1) plus
corresponding Annex I product-system obligations apply from 2 August 2027.

Parliament adopted an amending position on 16 June 2026 and the Council adopted
the act after Parliament's first reading on 29 June. The official procedure
record still said `awaiting publication in Official Journal` on 12 July. The
amendment's 2027/2028 dates therefore remain adopted-pending rather than
operative until OJ publication triggers its entry-into-force clause.

> **Claim record — GOV-0025-C01 | analytic-judgment**
> **Claim:** The governing state on 2026-07-12 is the in-force, partly
> applicable base AI Act plus an adopted but not-yet-operative amendment; base
> dates control until Official Journal publication and entry into force.
> **Claim status:** active
> **Scope:** EU-level instrument force and temporal status on the review date;
> not a post-review consolidated text, national-readiness finding or legal
> advice for an operator.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-19.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0053](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md),
> `SRC-0053-C02/C07`; AI Act Article 113; Parliament T10-0198/2026 amendment
> (40) and Article 4; OEIL 2025/0359(COD) status/key events.
> **Basis / limits:** Force, adoption and pending publication are directly
> distinguished. Publication timing is unknown and needs near-term review.

## Actors, research and retained-law scope

Article 2 reaches Union and specified third-country providers/deployers,
importers, distributors, product manufacturers, authorised representatives and
affected persons. Sole-purpose scientific R&D systems/models and pre-market
research/testing/development receive separate bounded exclusions. Real-world
testing is not within the pre-market exclusion, and data/privacy law and other
applicable Union law continue to govern. Free/open-source status is not a
blanket exception for high-risk, prohibited or Article 50 systems.

> **Claim record — GOV-0025-C02 | source-report**
> **Claim:** Research and open-source applicability must be resolved through
> the exact Article 2 conditions; neither label removes real-world-testing,
> product, high-risk, transparency or retained data-law obligations by itself.
> **Claim status:** active
> **Scope:** Regulation-level scope test; not classification of a named model,
> laboratory, dataset, clinical study or research collaboration.
> **As of:** Base Act reviewed 2026-07-12.
> **Review after:** 2026-07-19.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0053](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md),
> `SRC-0053-C03`; AI Act Article 2(1), (6)-(8) and (12), PDF physical
> pp. 45-46.
> **Basis / limits:** Boundaries are direct; intended purpose, market status
> and testing facts determine actual application.

## Medical-device and IVD applicability

For MDR/IVDR products, Article 6(1) requires both a safety-component/product
role and third-party conformity assessment. Article 43(3) then uses the
sectoral MDR/IVDR route while incorporating AI Act requirements. The joint
AIB/MDCG FAQ is useful interpretation but expressly nonbinding. Its examples
preserve device-class and in-house boundaries rather than treating every
medical AI system as high-risk.

> **Claim record — GOV-0025-C03 | analytic-judgment**
> **Claim:** EU medical-device AI governance is cumulative but conditional:
> MDR/IVDR classification and third-party-assessment status determine the
> Article 6(1) trigger, after which AI requirements join the sectoral conformity
> route without reclassifying the device merely because the AI is high-risk.
> **Claim status:** active
> **Scope:** Legal architecture and nonbinding FAQ interpretation; not a
> device-specific classification, approval, conformity or clinical finding.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-19.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0053](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md),
> `SRC-0053-C04`; AI Act Articles 6(1), 43(3), Annex I Section A(11)-(12);
> AIB 2025-1/MDCG 2025-6 disclaimer and Q2, Q4, Q25, Q27-Q28, Q35.
> **Basis / limits:** Primary trigger and route control. FAQ class/in-house
> examples cannot amend the law or substitute for notified-body analysis.

## Requirements and control mappings

Applicable high-risk duties cover risk management, data/data-governance,
technical documentation, logging, transparency, human oversight, accuracy,
robustness and cybersecurity. Applicable GPAI duties cover model/downstream
documentation, copyright policy and training-content summary; systemic-risk
models also receive evaluation, adversarial testing, systemic-risk mitigation,
incident reporting and cybersecurity duties. These functions map at a high
level to provenance, validation, decision-gate, monitoring and assurance
controls, not to proof that a control has been deployed or works.

> **Claim record — GOV-0025-C04 | source-report**
> **Claim:** The Act supplies lifecycle governance for applicable high-risk and
> GPAI systems across data, documentation, validation, oversight, incident and
> cyber-risk functions while preserving distinct system/model duty sets.
> **Claim status:** active
> **Scope:** Legal requirement classes subject to application dates and scope;
> not a control implementation, conformity certificate, benchmark or outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-19.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0053](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md),
> `SRC-0053-C05/C06`; AI Act Articles 8-15, 51, 53 and 55.
> **Basis / limits:** Duties are direct. Exact operator role and current date
> must be resolved before mapping them to a particular workflow.

## Guidance, code and exception force

The Commission GPAI guidelines are nonbinding interpretation that will guide
enforcement. The GPAI Code is a voluntary compliance route assessed as
adequate by the Commission and AI Board. Providers may instead demonstrate
alternative adequate means where the Act permits. Article 53's GPAI
open-source exception removes only specified documentation duties and does not
apply to systemic-risk models. The AIB/MDCG FAQ is also nonbinding. Imperative
language in these companions is not converted into an independent legislative
duty.

> **Claim record — GOV-0025-C05 | analytic-judgment**
> **Claim:** Binding Act duties, nonbinding Commission/AIB/MDCG interpretation
> and the voluntary Code are three different force classes and must remain
> separate in any compliance or cross-jurisdiction comparison.
> **Claim status:** active
> **Scope:** Instrument-force classification; not legal advice, a finding that
> an alternative means is adequate or provider compliance.
> **As of:** Commission pages checked 2026-07-12.
> **Review after:** 2026-07-19.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0053](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md),
> `SRC-0053-C04/C06`; AI Act Article 53(2), (4), Article 55(2); Commission
> GPAI pages; AIB/MDCG disclaimer p. 1.
> **Basis / limits:** Each source states its force or compliance role. Adequacy
> of a code is not evidence of its implementation or effectiveness.

## Adoption and evidence boundary

Formal adoption and application are observable. Code participation, provider
implementation, medical-device conformity, competent-authority enforcement,
incident handling and control effectiveness require different records. The six
source artifacts share one EU law/implementation family and do not themselves
constitute two materially independent jurisdictional lineages.

> **Claim record — GOV-0025-C06 | analytic-judgment**
> **Claim:** `GOV-0025` supplies one current EU governance lineage with force,
> scope, exceptions and temporal conflicts resolved, but no operator-level
> implementation or effectiveness evidence and no second jurisdiction.
> **Claim status:** active
> **Scope:** Evidence maturity and lineage counting; not a claim that no EU
> operator has implemented controls.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-19.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0053](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md),
> `SRC-0053-C01/C08`; full package provenance and institutional relationships.
> **Basis / limits:** Formal states are direct; uptake and outcomes require
> separate primary implementation/test/evaluation evidence.

## Cyberbiosecurity relevance and safety boundary

The regime directly reaches AI/data/model governance and conditionally reaches
MDR/IVDR systems used in biological, diagnostic and healthcare workflows. This
page preserves only public legal roles and defensive control functions. It
contains no patient data, device endpoint, credential, private model, exploit
or laboratory protocol.

> **Claim record — GOV-0025-C07 | analytic-judgment**
> **Claim:** The governance page supports defensive cyberbiosecurity comparison
> without exposing operational targets or converting legal design into
> implementation, safety or effectiveness claims.
> **Claim status:** active
> **Scope:** Local page and its high-level mappings; not legal advice or a
> security assessment of EU systems, models or devices.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `GOV-0025-C01`-`C06`; local representation.
> **Basis / limits:** Only governance-level content is retained.

## Related pages

- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)
- [SRC-0053 — EU source package](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md)
- [GOV-0006 — staged EU health-data governance](gov-0006-eu-ehds-regulation-2025.md)
- [AST-0008 — AI biological assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [WFL-0011 — AI biological lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [CTL-0016 — provenance and validation controls](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
- [SYN-0018 — existing AI/life-science reconciliation](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)

## Sources

- [SRC-0053](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md), at the exact legal, PDF and HTML locators above.
