---
id: AST-0004
type: asset
title: Synthetic nucleic-acid orders, screening records and synthesis equipment
aliases:
  - nucleic-acid procurement and screening assets
  - synthesis order and benchtop equipment assets
status: active
created: 2026-07-12
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-10-10
source_ids:
  - SRC-0011
  - SRC-0012
  - SRC-0033
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0011
    claim_id: AST-0004-C01
    evidence:
      - source: SRC-0011
        locator: "§§III–V, printed pp. 5–13, especially Tables 1–2"
  - predicate: governed-by
    target: GOV-0002
    claim_id: AST-0004-C02
    evidence:
      - source: SRC-0011
        locator: "§§I–III, printed pp. 4–6"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: AST-0004-C03
    evidence:
      - source: SRC-0012
        locator: "Definitions and screening/equipment sections, HTML lines 793–1050"
  - predicate: governed-by
    target: GOV-0003
    claim_id: AST-0004-C03
    evidence:
      - source: SRC-0012
        locator: "Introduction and scope, HTML lines 708–839"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: AST-0004-C05
    evidence:
      - source: SRC-0033
        locator: "Summary Figure S-1, printed p. 3 (physical p. 24); Chapter 4 §AI and Biodesign Security, printed pp. 50–53 (physical pp. 71–74)"
tags:
  - synthesis
  - procurement
  - screening
  - customer-information
  - records
  - benchtop-equipment
  - ai-design-output
---

# Synthetic nucleic-acid orders, screening records and synthesis equipment

> Defensive asset map for US and UK procurement-screening contexts.
> It keeps order/design information, customer identity, screening records,
> physical products, equipment and institutional capability distinct and omits
> sequences, screening logic and operational bypass detail.

## Scope

`SRC-0011` and `SRC-0012` cover synthetic nucleic-acid procurement and benchtop
synthesis equipment through providers, manufacturers, users and intermediaries.
The page represents their shared asset/stakeholder classes and differences; it
is not a complete engineering-biology or DBTL asset model.

> **Claim record — AST-0004-C01 | source-report**
> **Claim:** The OSTP framework addresses synthetic nucleic-acid purchase
> orders, customer/institution information, screening decisions and records,
> provider/manufacturer attestations, screening databases, synthesized
> products, benchtop synthesis equipment and equipment lifecycle transfer.
> **Claim status:** active
> **Scope:** Roles and assets in the revised September 2024 US framework, not
> current adoption or every research collaboration.
> **As of:** 2024-09-30.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§III–V, printed pp. 5–13, especially Tables 1–2.
> **Basis / limits:** Asset/role classes are direct. The framework does not
> inventory deployments, quantify orders/products or publish a system topology.

## Asset and stakeholder classes

| Class | Protected interest | Boundary |
| --- | --- | --- |
| Order/design request | integrity, authorized purpose and controlled disclosure | No sequence or exact screening criterion is reproduced |
| Customer/end-user identity and affiliation | authenticity, proportional use and privacy | Identity attributes are represented only as a legitimacy class |
| Screening database/method | integrity, currency, confidentiality and availability | Contents and matching logic are withheld |
| Decision, rationale and record | provenance, accountability and retention | No suspicious-order indicators or reporting contacts are consolidated |
| Synthetic nucleic-acid product | authorized fulfillment and accountable custody | No sequence, construct or production parameter is included |
| Benchtop synthesis equipment and associated access channel | legitimate acquisition/use and lifecycle accountability | No device architecture, reagent constraint or anti-tamper mechanism is described |
| Provider/manufacturer capability | consistent screening, response and secure operation | Attestation is not effectiveness evidence |
| Research institution/funding agency/public | research continuity, oversight, biosecurity and trust | Framework scope is not generalized beyond its stated funding context |

> **Claim record — AST-0004-C02 | analytic-judgment**
> **Claim:** The framework creates a coupled asset boundary in which digital
> order, identity and decision records condition physical product fulfillment
> or equipment access, while the asset classes retain distinct privacy,
> integrity, biosecurity and continuity interests.
> **Claim status:** active
> **Scope:** Defensive asset interpretation of the 2024 framework.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§I–III, pp. 4–6; §V, pp. 8–13.
> **Basis / limits:** Conditional order-to-fulfillment and equipment-access
> decisions are direct; the asset taxonomy is wiki analysis. It does not prove
> a safeguard was implemented or that an accepted order is safe in all uses.

> **Claim record — AST-0004-C03 | source-report**
> **Claim:** UK guidance independently addresses orders/design information,
> customer/principal/end-user identity and affiliation, screening and follow-up
> records, customer IP/confidential information, synthesized material,
> benchtop equipment and transfer/use accountability across providers,
> manufacturers, vendors and users.
> **Claim status:** active
> **Scope:** UK guidance published 2024-10-08; role and asset classes, not
> adoption or implementation evidence.
> **As of:** 2024-10-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> definitions and screening/equipment sections, HTML lines 793–1050.
> **Basis / limits:** Classes are direct. Exact screening criteria, sequence
> content, suspicious indicators, identity checklist and device mechanics are
> not reproduced.

> **Claim record — AST-0004-C04 | analytic-judgment**
> **Claim:** Two independent national guidance lineages support a reconciled
> procurement asset map spanning designs/orders, identities, screening records,
> IP, synthesized material, equipment/automation and provider/user/public
> stakeholders, with jurisdiction-specific force kept separate.
> **Claim status:** active
> **Scope:** Shared US–UK screening asset envelope; not a full DBTL asset map or
> claim of adoption.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§III–V, pp. 5–13; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> HTML lines 708–1050.
> **Basis / limits:** The sources independently cover materially similar asset
> classes, while their scope/force differ. Experimental designs after order,
> biological-result data and DBTL retirement/disposition remain incomplete.

## AI-design interface

> **Claim record — AST-0004-C05 | source-report**
> **Claim:** NASEM adds AI-generated biological-design output as one possible
> upstream input to an order/screening decision and identifies design metadata,
> tool-use records and provider context as potentially relevant assets.
> **Claim status:** active
> **Scope:** Bounded biological-design-to-procurement interface; not a claim
> that all orders are AI-generated, that metadata standards exist or that a
> complete DBTL asset map is present.
> **As of:** 2025-04-23.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Summary Figure S-1, printed p. 3 (physical p. 24); Chapter 4 §AI and
> Biodesign Security, printed pp. 50–53 (physical pp. 71–74).
> **Basis / limits:** Design-tool output, screening context and suggested
> metadata/logging functions are direct. No order, sequence, standard,
> deployment, screening result or downstream biological outcome is supplied.

## Evidence and uncertainty

The original asset sources do not provide adoption counts, inventories,
screening accuracy, incident records, end-use outcomes or independent
evaluation. SRC-0059/0061 later add bounded screening evidence without changing
this asset map. Beyond the upstream interface in AST-0004-C05, experimental
plans, products after use and DBTL feedback remain bounded by WFL-0014 rather
than inferred here.

## Related pages

- [WFL-0008 — Nucleic-acid procurement and screening lifecycle](../workflows/wfl-0008-nucleic-acid-procurement-screening-lifecycle.md)
- [SYS-0006 — Synthesis-provider and benchtop screening systems](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [RSK-0008 — Screening failure and unsafe order fulfillment](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [CTL-0006 — Nucleic-acid order and equipment screening](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [GOV-0002 — US federally funded screening framework](../governance/gov-0002-us-federally-funded-nucleic-acid-screening-2024.md)
- [GOV-0003 — UK voluntary screening guidance](../governance/gov-0003-uk-synthetic-nucleic-acid-screening-2024.md)
- [SYN-0002 — US–UK screening comparison](../syntheses/syn-0002-us-uk-nucleic-acid-screening-comparison.md)
- [AST-0008 — Biological AI assets](ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [WFL-0011 — Biological AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [SRC-0011 — OSTP framework 2024](../sources/src-0011-ostp-nucleic-acid-screening-2024.md)
- [SRC-0012 — UK guidance 2024](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [SRC-0033 — NASEM AI/life-sciences report](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [WFL-0014 — Design-to-disposition lifecycle](../workflows/wfl-0014-engineering-biology-design-to-disposition-lifecycle.md)
- [THR-0006 — Intentional engineering-biology actions](../threats/thr-0006-engineering-biology-misuse-insider-and-supply-actions.md)
- [HAZ-0007 — Accidental engineering-biology failures](../hazards/haz-0007-engineering-biology-screening-synthesis-and-lifecycle-failures.md)

## Sources

- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md), §§I–V,
  printed pp. 4–13.
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
  HTML lines 708–1050.
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
  Summary Figure S-1, printed p. 3 (physical p. 24); Chapter 4, printed
  pp. 50–53 (physical pp. 71–74).
