---
id: WFL-0014
type: workflow
title: Engineering-biology design-to-disposition lifecycle
aliases:
  - engineering biology safe lifecycle
  - design order screening synthesis use disposition workflow
  - synthesis design-to-closeout lifecycle
status: active
created: 2026-07-13
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-08-12
source_ids:
  - SRC-0004
  - SRC-0011
  - SRC-0012
  - SRC-0033
  - SRC-0060
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: WFL-0014-C01
    evidence:
      - source: SRC-0033
        locator: "Summary, printed pp. 2–4; Chapters 2–3, printed pp. 19–37; Chapter 5, printed pp. 69–74; Appendix A Figure A-1 and printed pp. 106–109"
  - predicate: evidenced-by
    target: SRC-0011
    claim_id: WFL-0014-C02
    evidence:
      - source: SRC-0011
        locator: "2024 OSTP Framework §§I–V, printed pp. 4–13 (PDF pp. 5–14)"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: WFL-0014-C02
    evidence:
      - source: SRC-0012
        locator: "UK guidance Figure 1 and customer/sequence screening through record/transfer sections, HTML lines 833–1070"
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: WFL-0014-C03
    evidence:
      - source: SRC-0004
        locator: "WHO §§1.1–1.2, printed pp. 2–3; §§6.3–7.3.5, printed pp. 31–44 (PDF pp. 51–64)"
  - predicate: governed-by
    target: GOV-0028
    claim_id: WFL-0014-C04
    evidence:
      - source: SRC-0060
        locator: "HHS GPS §§1.2, 1.4 and Appendix D §D.5.2.3"
  - predicate: depends-on
    target: AST-0004
    claim_id: WFL-0014-C05
    evidence:
      - source: SRC-0011
        locator: "2024 OSTP Framework §§III–V, printed pp. 5–13"
      - source: SRC-0012
        locator: "UK guidance definitions and actor/asset/lifecycle sections, HTML lines 708–1070"
  - predicate: depends-on
    target: SYS-0006
    claim_id: WFL-0014-C05
    evidence:
      - source: SRC-0011
        locator: "2024 OSTP Framework §IV Tables 1–2 and §V, printed pp. 6–13"
      - source: SRC-0012
        locator: "UK provider/vendor/manufacturer screening and equipment sections, HTML lines 833–1039"
tags:
  - engineering-biology
  - synthetic-biology
  - design-build-test-learn
  - nucleic-acid-synthesis
  - procurement-screening
  - human-review
  - delivery
  - use
  - records
  - reporting
  - disposition
---

# Engineering-biology design-to-disposition lifecycle

> Safe, source-reconciled coverage of `design → order → screen → review →
> synthesis → delivery/use → record/report → disposition`. No source reports
> that one universal transaction follows this whole sequence, and the page
> contains no biological design, screening-evasion or laboratory procedure.

## Scope and reconciliation rule

This page joins four materially different evidence roles:

- NASEM supplies engineering-biology design and the digital-output→physical
  build/test→result-feedback DBTL boundary;
- the U.S. 2024 OSTP framework and independent UK guidance supply the
  order→screen→review→fulfil/decline/report→record segment;
- WHO supplies a broader laboratory-biosecurity use/custody/closeout branch for
  biosecurity-relevant material, equipment, information and records; and
- the current HHS GPS supplies a bounded funding/procurement overlay for its
  covered awards, excluding NIH.

No source is treated as a complete universal lifecycle. The U.S. policy
documents remain one national policy ecosystem for independence counting;
the UK, WHO and NASEM roles are materially separate. The joined lifecycle is a
canonical defensive map, not a claim that every engineered-biological product
is high consequence, every design becomes an order, or every order proceeds to
synthesis and use.

> **Claim record — WFL-0014-C01 | analytic-judgment**
> **Claim:** The workflow reconciles independent NASEM design/DBTL, U.S.–UK
> procurement-screening and WHO laboratory-biosecurity lifecycle roles without
> treating any source as a universal end-to-end engineering-biology procedure.
> **Claim status:** active
> **Scope:** Public, defensive lifecycle coverage across represented design,
> procurement, synthesis/build/test, use/accountability and closeout contexts;
> not a production protocol, a mandatory sequence or deployment evidence.
> **As of:** 2026-07-13.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C04/C08`; [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> `SRC-0011-C03`–`C05`; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> `SRC-0012-C02/C04`–`C06`; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> `SRC-0004-C04/C09`.
> **Basis / limits:** Each source role and its documentary boundary are direct.
> Their ordered composition is wiki analysis and creates no implementation or
> effectiveness claim.

## Reconciled lifecycle

| Stage | Required state or decision | Direct source role | Preserved boundary |
| --- | --- | --- | --- |
| 1. Design | define intended function/context; produce or select a candidate digital design under accountable review | NASEM biological-AI/design and DBTL frame | a design is not an authorization, order or validated biological result |
| 2. Order | translate an approved candidate or procurement need into an attributable customer/order request | U.S./UK customer/order models; the candidate/need→order connection is an explicit analytic bridge | not every design is ordered; identity and intended-use context remain source-specific |
| 3. Screen | apply the relevant high-level order and customer/equipment screening functions | independent U.S. and UK instruments | exact concern logic, thresholds, examples and bypass paths are withheld |
| 4. Review | route unresolved or policy-relevant screening state to accountable human legitimacy review and decision | U.S./UK follow-up and review functions | human review is neither universal nor proof of correctness |
| 5. Synthesis/build | approve physical fulfilment or authorized equipment access and carry a bounded design into physical build | U.S./UK provider/equipment fulfilment; NASEM physical DBTL build gate | fulfilment/equipment access does not prove product properties, experimental success or safety |
| 6. Delivery/use | transfer the resulting material or equipment state to an authorized recipient and conduct only the governed use/test represented by the applicable context | UK provision/use/transfer scope; NASEM build/test; WHO process/use and custody context | no universal custody schema, procedure or use authorization is inferred |
| 7. Record/report | preserve screening, review, decision, transfer and response context and report/escalate where the governing instrument requires | U.S./UK record/report functions; WHO accountability/incident loop | records do not prove accuracy; reporting design is not an event or enforcement result |
| 8. Disposition | resolve residual material, equipment, information, data and records through locally authorized retention, transfer, disposal or destruction | WHO laboratory-biosecurity closeout/accountability branch | applies only where the represented material/information is in WHO's biosecurity-relevant scope; no universal product-disposition method |
| 9. Learn/reassess | feed validated test/operational evidence and incidents or policy changes into later design, risk and control decisions | NASEM DBTL feedback; WHO review loop; U.S./UK update responsibilities | feedback can propagate error and does not make the workflow circular in every case |

The displayed arrow is a coverage shorthand. Record/report states exist across
several stages; denial can stop the flow before synthesis; disposal may occur
after storage or transfer; and DBTL learning can generate a later design rather
than a continuation of the same order.

> **Claim record — WFL-0014-C02 | analytic-judgment**
> **Claim:** At safe abstraction the reconciled corpus directly covers every
> literal in `design → order → screen → review → synthesis → delivery/use →
> record/report → disposition`, with independent source lineages and explicit
> branch, force, scope and evidence-state limits.
> **Claim status:** active
> **Scope:** Lifecycle coverage criterion for synthesis and engineering biology;
> not a universal linear procedure, implemented end-to-end transaction,
> biological outcome or safeguard-effectiveness result.
> **As of:** 2026-07-13.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `WFL-0014-C01`; [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Summary and Chapters 2–3/5, exact frontmatter locators; [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§I–V, printed pp. 4–13; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> HTML lines 708–1070; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§1.1–1.2 and 6.3–7.3.5, printed pp. 2–3 and 31–44.
> **Basis / limits:** Each named stage has direct located support and the
> cross-source composition preserves where stages do not transfer. Completeness
> means coverage of lifecycle classes, not proof of one completed lifecycle.

## Use, custody and disposition boundary

WHO's horizontal model expressly spans collection/receipt, processing or use,
storage/inventory, transfer/transport and disposal/destruction, with associated
records and responsibility. It applies across research, diagnostic,
manufacturing and pharmaceutical laboratory contexts for high-consequence or
other biosecurity-relevant material. This makes it appropriate for the missing
closeout class but not for all engineering-biology outputs by analogy.

> **Claim record — WFL-0014-C03 | analytic-judgment**
> **Claim:** WHO supplies a direct use/custody/disposition branch for
> biosecurity-relevant material, equipment and information, while the workflow
> limits that branch to the source's laboratory/material scope rather than
> universalizing it to every synthesized product.
> **Claim status:** active
> **Scope:** Closeout and accountability coverage; not a universal retention
> period, destruction method, product-stewardship regime or verified execution.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> `SRC-0004-C04/C09`; §§1.1–1.2, printed pp. 2–3; §§6.3–7.3.5,
> printed pp. 31–44 (PDF pp. 51–64); [WFL-0004](wfl-0004-high-consequence-material-lifecycle.md),
> `WFL-0004-C01`–`C03`, for canonical navigation only.
> **Basis / limits:** The lifecycle and closeout objectives are direct. The
> applicability bridge is bounded analysis and provides no procedure or result.

## Current HHS funding/procurement overlay

For the HHS branch only, GPS Version 2.0 is incorporated through covered award
terms, excludes NIH, provides general subrecipient flow-down, and states the
`D.5.2.3` adherence/procurement-source condition. It governs the funding and
provider-selection edge; it does not govern every upstream design or downstream
use/disposition decision represented in this composite workflow.

> **Claim record — WFL-0014-C04 | analytic-judgment**
> **Claim:** `GOV-0028` currently governs the HHS award/procurement slice of
> this workflow for its stated scope, but neither the HHS GPS nor the composite
> lifecycle proves that every represented stage is an HHS award duty.
> **Claim status:** active
> **Scope:** Covered HHS discretionary-award branch excluding NIH; not every
> U.S. agency, private procurement, downstream experiment or disposition rule.
> **As of:** 2026-07-13.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0060](../sources/src-0060-hhs-nucleic-acid-procurement-award-condition-2025-2026.md),
> `SRC-0060-C03`–`C07`; HHS GPS §§1.2, 1.4 and Appendix D §D.5.2.3;
> [GOV-0028](../governance/gov-0028-hhs-synthetic-nucleic-acid-procurement-award-condition.md),
> `GOV-0028-C01`–`C05`, as canonical interpretation.
> **Basis / limits:** The HHS funding/procurement predicate is direct. Other
> lifecycle stages arise from independent sources and are not imported into
> the award as unstated duties.

## Assets, systems and trust boundaries

> **Claim record — WFL-0014-C05 | analytic-judgment**
> **Claim:** The lifecycle depends on attributable design/order/material/
> record assets in `AST-0004` and provider, screening, review and equipment
> boundaries in `SYS-0006`; the new workflow adds lifecycle completeness but
> does not assert a deployed architecture or validated interface.
> **Claim status:** active
> **Scope:** Canonical dependency map; no provider topology, identity design,
> database content, configuration or implementation validation.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§III–V, printed pp. 5–13; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> definitions and lifecycle sections, HTML lines 708–1070;
> [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C04/C05`.
> **Basis / limits:** Asset and functional boundary classes are direct across
> independent lineages. Their joined graph is not deployment evidence.

Key trust boundaries are:

- designer/model user ↔ accountable design-selection gate;
- customer/recipient ↔ ordering/provider interface;
- customer/order state ↔ screening tool, reference data and policy definition;
- automated screen ↔ accountable reviewer;
- reviewer/provider decision ↔ physical fulfilment or equipment access;
- provider/carrier/recipient ↔ delivery and custody acceptance;
- physical build/test/use ↔ measured result and later digital learning;
- active material/data/equipment ↔ retention, transfer or disposition; and
- recipient ↔ subrecipient/provider under the applicable award condition.

These are handoffs requiring local validation, not confirmed vulnerabilities.

## Completeness and evidence-state audit

| Question | State |
| --- | --- |
| All required lifecycle classes | direct across independent lineages |
| One universal source workflow | explicitly absent |
| One observed end-to-end transaction | not demonstrated |
| Current HHS procurement policy | direct for bounded award scope |
| Current completed OSTP successor | unverified |
| Screening performance | separate NIST evidence; not established by this workflow page |
| Product/material disposition | direct only for WHO-bounded biosecurity-relevant contexts |
| Implementation/effectiveness | not inferred from lifecycle coverage |

## Safety boundary

The page omits biological designs, sequences, laboratory parameters, exact
screening logic, thresholds, concern examples, customer indicators, reporting
contacts, equipment tamper/bypass mechanics and disposition procedures. It
retains only the functional states, responsibilities and evidence boundaries
needed for defensive lifecycle analysis.

## Related pages

- [WFL-0008 — procurement/screening segment](wfl-0008-nucleic-acid-procurement-screening-lifecycle.md)
- [WFL-0011 — biological-AI DBTL lifecycle](wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [WFL-0004 — laboratory material lifecycle](wfl-0004-high-consequence-material-lifecycle.md)
- [AST-0004 — order/equipment assets](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md)
- [SYS-0006 — synthesis/screening systems](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [GOV-0028 — HHS award condition](../governance/gov-0028-hhs-synthetic-nucleic-acid-procurement-award-condition.md)
- [RSK-0008 — screening-failure risk](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [CTL-0006 — screening controls](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [SYN-0023 — prior engineering-biology reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [SYN-0032 — Lifecycle/threat/screening/governance reconciliation](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)

## Sources

- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md), exact DBTL/design locators above.
- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md), §§I–V, printed pp. 4–13.
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md), HTML lines 708–1070.
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md), §§1.1–1.2 and 6.3–7.3.5.
- [SRC-0060](../sources/src-0060-hhs-nucleic-acid-procurement-award-condition-2025-2026.md), HHS GPS exact sections above.
