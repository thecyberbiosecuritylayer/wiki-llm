---
id: RSK-0019
type: risk-scenario
title: Merck cyber disruption propagating into manufacturing and product supply
aliases:
  - Merck cyber to pharmaceutical supply path
  - NotPetya manufacturing order disruption path
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-15
source_ids:
  - SRC-0046
  - SRC-0047
sensitivity: public
dual_use: low
origin_domain: cyber
destination_domains:
  - biomanufacturing
  - pharmaceutical-supply
relations:
  - predicate: evidenced-by
    target: SRC-0046
    claim_id: RSK-0019-C01
    evidence:
      - source: SRC-0046
        locator: "10-K anchors sC5918D6835605DFB9861637AED9AB7C7 (Item 1A, displayed printed p. 25), s02DF6574F3035C8485C795D393F48705 (MD&A, p. 38) and sBB3EEB5901095A398997106BC9F8CDA1 (Vaccines, p. 41)"
  - predicate: evidenced-by
    target: SRC-0047
    claim_id: RSK-0019-C02
    evidence:
      - source: SRC-0047
        locator: "Opinion pp. 7–10; event, dependency, property damage and modality boundaries"
  - predicate: depends-on
    target: INC-0006
    claim_id: RSK-0019-C01
    evidence:
      - source: SRC-0046
        locator: "INC-0006-C01–C08 canonical event and evidence-role separation"
  - predicate: affects
    target: WFL-0003
    claim_id: RSK-0019-C01
    evidence:
      - source: SRC-0046
        locator: "manufacturing disruption→order backlog→unfulfilled-order path"
  - predicate: affects
    target: AST-0007
    claim_id: RSK-0019-C03
    evidence:
      - source: SRC-0046
        locator: "manufacturing, products/orders, stockpile and supply-stakeholder effects"
tags:
  - biomanufacturing
  - pharmaceuticals
  - cyberattack
  - manufacturing-disruption
  - product-supply
  - observed
---

# Merck cyber disruption propagating into manufacturing and product supply

## Evidence classification

This is a **mixed observed/analytic path** based on one canonical incident. The
cyberattack, manufacturing disruption and certain-product order/backlog effect
are observed first-party reports with independent incident/property-damage
context. Any further product-quality, shortage, patient or population effect is
unobserved and excluded.

## Complete observed path

`network cyberattack → worldwide manufacturing/research/sales disruption →
residual order backlog and inability to fulfil certain-product orders in
certain markets → bounded pharmaceutical-supply/sales consequence`

> **Claim record — RSK-0019-C01 | analytic-judgment**
> **Claim:** `INC-0006` supplies a complete observed cyber→manufacturing→order-
> backlog/unfulfilled-order→supply consequence path beyond generic IT outage.
> **Claim status:** active
> **Scope:** Merck's unnamed certain products/markets in 2017–2018; not product
> quality, shortage prevalence, patient harm or a universal BMO cascade.
> **As of:** Event/effects 2017–2018.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [INC-0006](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md),
> `INC-0006-C01`–`C06`; [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md),
> `SRC-0046-C02`–`C05`.
> **Basis / limits:** Every accepted node is directly reported. Financial and
> supply measures remain first-party.

## Independent context

> **Claim record — RSK-0019-C02 | analytic-judgment**
> **Claim:** The New Jersey opinion independently anchors the NotPetya
> incident, vendor/update dependency, broad network infection and property-
> damage context while preserving the manufacturing-offline sentence as
> Merck's contention and not replicating order/backlog values.
> **Claim status:** active
> **Scope:** Claim-appropriate independent context, not a second event or
> consequence measurement.
> **As of:** Opinion 2023-05-01.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md),
> `SRC-0047-C02`–`C07`.
> **Basis / limits:** Issuer and evidence-production process are independent;
> party contentions remain attributed.

## Assets and stakeholders

> **Claim record — RSK-0019-C03 | analytic-judgment**
> **Claim:** The observed path affects enterprise/network and manufacturing
> availability, unnamed products/orders, market/supply functions and company/
> customer/public-stockpile stakeholders without establishing a compromised
> controller, batch, release decision or patient effect.
> **Claim status:** active
> **Scope:** Public class-level assets/stakeholders for one incident.
> **As of:** 2017–2018.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md),
> `SRC-0046-C02/C03/C05/C06`, Item 1A, displayed p. 25; MD&A, displayed
> pp. 38–39; Vaccines, displayed p. 41;
> [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md),
> `SRC-0047-C02/C04`, opinion pp. 7–9.
> **Limits:** The 10-K supports manufacturing/orders/stockpile classes;
> no OT-controller or quality-state detail is supplied.

## Mixed-cause continuity branch

> **Claim record — RSK-0019-C04 | analytic-judgment**
> **Claim:** The Gardasil 9 stockpile branch is a bounded continuity response
> with two explicit drivers—temporary cyber-related shutdown and higher demand—
> plus replenishment; it is not an attack-only shortage, patient consequence or
> additive cyber-loss value.
> **Claim status:** active
> **Scope:** One product-specific response branch; not the identity of the
> unnamed unfulfilled orders.
> **As of:** 2017–2018.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** `SRC-0046-C05`; `INC-0006-C05`; 10-K Vaccines anchor
> `sBB3EEB5901095A398997106BC9F8CDA1`, displayed printed p. 41.
> **Basis / limits:** Co-causation and accounting/replenishment states remain
> explicit.

## Control edges and uncertainty

> **Claim record — RSK-0019-C05 | analytic-judgment**
> **Claim:** Defensive lessons map to vendor/update trust, detection/
> containment, critical-application/manufacturing availability, stockpile/order
> continuity and recovery-resilience edges, but no represented control has a
> tested or independently evaluated incident outcome.
> **Claim status:** active
> **Scope:** Exact public control-edge mapping, not operational configuration or
> effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [CTL-0020](../controls/ctl-0020-merck-incident-vendor-update-continuity-recovery-lessons.md);
> `INC-0006-C08`; `SRC-0046-C07`; `SRC-0047-C03/C08`.
> **Basis / limits:** Failure/interruption and response nodes are direct;
> proposed controls and issuer implementation objectives are unevaluated.

> **Claim record — RSK-0019-C06 | analytic-judgment**
> **Claim:** The path is candidate SF3 support for `BMO-CI` and technical,
> control-lesson and investigation thresholds, but it does not support
> `BMO-AE`, `THI-WL/TV/XT/CI/GR`, `CTR-AE` or any global incident/control/
> directionality/risk-chain transition.
> **Claim status:** superseded
> **Scope:** Pre-synthesis rubric boundary.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `RSK-0019-C01`–`C05`; frozen criteria/source floors.
> **Basis / limits:** Candidate relevance is not arithmetic promotion.
> **Superseded by:** `SYN-0028-C05/C08`–`C12`, after strict SF3 and
> nonpromotion reconciliation.

## Safety boundary

No indicator, code, credential, endpoint, vulnerable version, exploit
sequence, network/facility topology, process value, recipe or operational
response procedure is exposed.

> **Claim record — RSK-0019-C07 | analytic-judgment**
> **Claim:** No indicator, code, credential, endpoint, vulnerable version,
> exploit sequence, network/facility topology, process value, recipe or
> operational response procedure is exposed.
> **Claim status:** stale
> **Scope:** Local content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local content and safety abstraction.
> **Limits:** Public high-level evidence nodes sufficed at the stated review
> date. Repository-content assertions can change; this one is retained only as
> a historical safety note, with the current boundary stated in prose above.

## Related pages

- [INC-0006](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md)
- [CTL-0020](../controls/ctl-0020-merck-incident-vendor-update-continuity-recovery-lessons.md)
- [VUL-0003](../vulnerabilities/vul-0003-biomanufacturing-data-integrity-ot-access-dependencies.md)
- [RSK-0002](rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [SYN-0028](../syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)

## Sources

- [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md)
- [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md)
