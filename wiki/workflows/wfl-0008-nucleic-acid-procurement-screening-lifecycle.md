---
id: WFL-0008
type: workflow
title: Synthetic nucleic-acid procurement and screening lifecycle
aliases:
  - nucleic-acid order screening workflow
  - synthesis procurement screening lifecycle
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
    claim_id: WFL-0008-C01
    evidence:
      - source: SRC-0011
        locator: "§§I–V, printed pp. 4–13"
  - predicate: depends-on
    target: AST-0004
    claim_id: WFL-0008-C02
    evidence:
      - source: SRC-0011
        locator: "§§III–V, printed pp. 5–13"
  - predicate: depends-on
    target: SYS-0006
    claim_id: WFL-0008-C02
    evidence:
      - source: SRC-0011
        locator: "§IV Tables 1–2, pp. 6–7; §V, pp. 8–13"
  - predicate: governed-by
    target: GOV-0002
    claim_id: WFL-0008-C01
    evidence:
      - source: SRC-0011
        locator: "§§I–III, printed pp. 4–6"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: WFL-0008-C03
    evidence:
      - source: SRC-0012
        locator: "Figure 1 and customer/sequence screening through follow-up, HTML lines 833–1070"
  - predicate: governed-by
    target: GOV-0003
    claim_id: WFL-0008-C03
    evidence:
      - source: SRC-0012
        locator: "Scope and responsible-practice guidance, HTML lines 708–839"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: WFL-0008-C05
    evidence:
      - source: SRC-0033
        locator: "Summary Figure S-1, printed p. 3 (physical p. 24); Chapter 4 §AI and Biodesign Security, printed pp. 50–53 (physical pp. 71–74)"
tags:
  - synthesis
  - procurement
  - screening
  - human-review
  - recordkeeping
  - equipment-lifecycle
  - ai-design-interface
---

# Synthetic nucleic-acid procurement and screening lifecycle

> Safe functional lifecycle from funding/procurement context through provider
> selection, order/customer screening, bounded human review, fulfillment or
> refusal/reporting, records and equipment lifecycle. It is not a screening
> implementation guide or a complete design-to-use DBTL lifecycle.

## Scope

> **Claim record — WFL-0008-C01 | source-report**
> **Claim:** The revised OSTP framework defines a procurement flow in which
> federally funded customers use adherent providers/manufacturers, relevant
> orders and customers are screened, concerns are reviewed, fulfillment or
> refusal/reporting decisions are made, records are retained and equipment use/
> transfer remains accountable.
> **Claim status:** active
> **Scope:** Source-stated US funding/procurement framework as of September
> 2024; not proof of later implementation or current universal duty.
> **As of:** 2024-09-30.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§I–III, pp. 4–6; §V, pp. 8–13.
> **Basis / limits:** Functions and decisions are direct. Exact technical
> screening logic, indicators, contacts and equipment controls are deliberately
> not reproduced; deployment and outcomes are absent.

## Functional lifecycle

1. establish the applicable funding/procurement context and accountable party;
2. select a provider, manufacturer or intermediary represented as adherent;
3. receive an order/request and preserve its customer and provenance context;
4. apply the appropriate order/sequence and customer/equipment checks;
5. conduct bounded legitimacy review when the defined condition requires it;
6. approve and fulfill, or decline/escalate/report according to policy;
7. retain decision, interaction and response records securely;
8. maintain legitimate-user and transfer accountability across equipment life;
9. review screening/security mechanisms as standards and policy change.

> **Claim record — WFL-0008-C02 | analytic-judgment**
> **Claim:** This lifecycle couples digital identity/order/decision states to
> physical fulfillment or equipment access through provider, human-review and
> manufacturer boundaries represented in `SYS-0006` and assets in `AST-0004`.
> **Claim status:** active
> **Scope:** Defensive workflow interpretation, not a claim that every order
> follows one linear implementation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §IV Tables 1–2, pp. 6–7; §V, pp. 8–13.
> **Basis / limits:** The source establishes the conditional functions; their
> lifecycle arrangement is wiki analysis. No interface validation, timing,
> error rate or complete material custody is provided.

> **Claim record — WFL-0008-C03 | source-report**
> **Claim:** UK guidance independently describes an order flow with customer
> and sequence checks, legitimacy follow-up when concerns arise, fulfillment or
> denial/reporting, recordkeeping and later equipment/use/transfer controls.
> **Claim status:** active
> **Scope:** Voluntary UK guidance published 2024-10-08, not observed operation
> or a statutory workflow.
> **As of:** 2024-10-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> Figure 1 and customer/sequence screening through follow-up sections, HTML
> lines 833–1070.
> **Basis / limits:** Functional steps are direct; exact criteria and indicators
> are withheld. The source reports no deployment, latency, error or outcome.

> **Claim record — WFL-0008-C04 | analytic-judgment**
> **Claim:** Independent US and UK instruments converge on the safe lifecycle
> `order/context → customer+sequence checks → bounded review → fulfill or
> deny/report → records/equipment accountability`, while differing in force,
> covered population and assurance mechanism.
> **Claim status:** active
> **Scope:** Cross-jurisdiction functional reconciliation, not equivalence or
> proof of adoption.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§I–V, pp. 4–13; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> HTML lines 708–1070.
> **Basis / limits:** Shared stages are independently specified. Neither source
> supplies full design creation, experimental use, disposition or a biological-
> result→digital DBTL feedback loop.

> **Claim record — WFL-0008-C05 | source-report**
> **Claim:** NASEM directly supplies the bounded interface `AI-enabled design
> output → candidate synthesis order → existing screening/review/fulfillment
> lifecycle` and discusses possible metadata, logging and design-tool guardrail
> functions around that interface.
> **Claim status:** active
> **Scope:** Upstream interface to this procurement segment; not a complete
> DBTL lifecycle, screening implementation, universal order type or proof that
> a safeguard works.
> **As of:** 2025-04-23.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Summary Figure S-1, printed p. 3 (physical p. 24); Chapter 4 §AI and
> Biodesign Security, printed pp. 50–53 (physical pp. 71–74).
> **Basis / limits:** The report connects design tools, synthesis screening and
> fulfillment at functional level. It provides no order, design, technical
> rule, system integration, performance result or biological outcome.

## Trust and responsibility boundaries

- funding agency/recipient ↔ provider or manufacturer attestation;
- customer/end user ↔ ordering and legitimacy-review function;
- ordering interface ↔ screening method/database;
- automated result ↔ accountable human decision;
- provider/manufacturer ↔ intermediary or downstream recipient;
- digital decision ↔ physical fulfillment/equipment access;
- equipment owner/user ↔ later transfer or access change;
- screening/decision records ↔ cybersecurity, privacy and oversight.

The source defines expected responsibilities but does not validate any
implementation boundary.

## Completeness limits

The U.S./UK screening instruments do not substantively model design creation,
experimental use, product disposition or a biological-result→digital DBTL
feedback loop. NASEM adds only the bounded upstream AI-design interface. This
page therefore contributes a procurement/screening lifecycle segment, not full
engineering-biology lifecycle coverage. WFL-0014 now supplies the separate
cross-source design-to-disposition composition; it does not retroactively turn
this procurement segment into one universal implemented workflow.

## Related pages

- [SYN-0023 — Engineering-biology reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [AST-0004](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md)
- [SYS-0006](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [RSK-0008](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [CTL-0006](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [GOV-0002](../governance/gov-0002-us-federally-funded-nucleic-acid-screening-2024.md)
- [GOV-0003](../governance/gov-0003-uk-synthetic-nucleic-acid-screening-2024.md)
- [SYN-0002](../syntheses/syn-0002-us-uk-nucleic-acid-screening-comparison.md)
- [WFL-0011 — Full biological AI/DBTL lifecycle](wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [AST-0008 — Biological AI assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md)
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [WFL-0014 — Full cross-source lifecycle composition](wfl-0014-engineering-biology-design-to-disposition-lifecycle.md)
- [SYN-0032 — Current engineering-biology reconciliation](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)

## Sources

- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md), §§I–V,
  printed pp. 4–13.
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
  HTML lines 708–1070.
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
  Summary Figure S-1, printed p. 3 (physical p. 24); Chapter 4, printed
  pp. 50–53 (physical pp. 71–74).
