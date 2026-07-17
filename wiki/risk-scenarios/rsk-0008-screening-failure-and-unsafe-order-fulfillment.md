---
id: RSK-0008
type: risk-scenario
title: Screening or decision failure leading to unsafe order fulfillment
aliases:
  - nucleic-acid screening failure scenario
  - unsafe synthesis order fulfillment path
status: active
created: 2026-07-12
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-10-10
source_ids:
  - SRC-0011
  - SRC-0012
  - SRC-0033
  - SRC-0059
  - SRC-0061
sensitivity: public
dual_use: moderate
origin_domain: digital
destination_domains:
  - physical
  - biological
relations:
  - predicate: evidenced-by
    target: SRC-0011
    claim_id: RSK-0008-C01
    evidence:
      - source: SRC-0011
        locator: "§I, p. 4; §V, pp. 8–13"
  - predicate: depends-on
    target: WFL-0008
    claim_id: RSK-0008-C01
    evidence:
      - source: SRC-0011
        locator: "§§I–V, printed pp. 4–13"
  - predicate: depends-on
    target: SYS-0006
    claim_id: RSK-0008-C02
    evidence:
      - source: SRC-0011
        locator: "§III, pp. 5–6; §V, pp. 8–13"
  - predicate: affects
    target: AST-0004
    claim_id: RSK-0008-C02
    evidence:
      - source: SRC-0011
        locator: "§V, pp. 8–13"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: RSK-0008-C03
    evidence:
      - source: SRC-0012
        locator: "Customer/sequence screening, follow-up and equipment sections, HTML lines 841–1050"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: RSK-0008-C04
    evidence:
      - source: SRC-0033
        locator: "Chapter 4 §AI and Biodesign Security, printed pp. 50–53 (physical pp. 71–74)"
  - predicate: evidenced-by
    target: SRC-0059
    claim_id: RSK-0008-C05
    evidence:
      - source: SRC-0059
        locator: "Blinded benchmark Results and disagreement analysis, physical pp. 9–19; aggregate labelled classifications and misses"
  - predicate: evidenced-by
    target: SRC-0061
    claim_id: RSK-0008-C05
    evidence:
      - source: SRC-0061
        locator: "Operational corpus and aggregate pass/flag/denial outputs, Figure 4; no public ground truth or downstream outcome"
tags:
  - synthesis
  - screening
  - order-integrity
  - decision-integrity
  - fulfillment
  - hypothetical
  - ai-design-interface
---

# Screening or decision failure leading to unsafe order fulfillment

> The full decision-to-fulfilment path remains hypothetical and framework-
> derived; one classification edge now has bounded benchmark and operational-
> data evidence. The page exposes no screening threshold, evasion logic,
> sequence data or device-bypass mechanism.

## Scenario

If an applicable order/customer/equipment condition is not recognized, or if a
screening/review/decision record is unavailable or untrustworthy, an order that
should receive further review or refusal could be approved. The digital
decision could then cross into physical product fulfillment or equipment
access. Downstream misuse or biological harm is possible in the policy's risk
rationale but is not documented as an observed outcome by any represented
source.

> **Claim record — RSK-0008-C01 | hypothesis**
> **Claim:** A failure of screening, legitimacy review or decision integrity can
> conditionally propagate through `WFL-0008` from a digital order state to
> physical product fulfillment or synthesis-equipment access.
> **Claim status:** active
> **Scope:** High-level procurement context represented by the 2024 framework;
> not an observed event, likelihood estimate or implementation weakness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §I, p. 4; §V, pp. 8–13.
> **Basis / limits:** The framework directly makes screening/review a condition
> of fulfillment and equipment legitimacy. The failure chain is wiki analysis;
> no occurrence, actor, technique, vulnerability or downstream harm is shown.

## Preconditions and transfer

Required preconditions include material reliance on the screening/decision
state, absence or failure of independent review, and actual fulfillment/access
after the decision. The transfer mechanism is **decision-to-custody/access**:

`digital order/identity state → screening and accountable review → approval
state → physical fulfillment or equipment access`.

> **Claim record — RSK-0008-C02 | analytic-judgment**
> **Claim:** The path affects order, identity, screening-record, product and
> equipment assets in `AST-0004` and crosses provider/human-review/fulfillment
> boundaries in `SYS-0006`, but it does not establish a biological outcome.
> **Claim status:** active
> **Scope:** Defensive mapping of the source's normative control points.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§III–V, printed pp. 5–13.
> **Basis / limits:** Roles, assets and fulfillment decisions are source-
> supported; the end-to-end failure path is analytic. Product misuse, exposure,
> disease, injury and environmental effects remain unobserved and unspecified.

> **Claim record — RSK-0008-C03 | analytic-judgment**
> **Claim:** Independent US and UK guidance lineages both condition physical
> fulfillment/equipment access on digital order, identity, screening and human-
> review states, corroborating the relevance of the high-level transfer path but
> not its occurrence or downstream harm.
> **Claim status:** active
> **Scope:** Normative rationale across two jurisdictions; not incident or
> effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §§I–V, pp. 4–13; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> HTML lines 841–1050.
> **Basis / limits:** Both instruments independently establish the decision-to-
> fulfillment control point. Neither provides a failed order, observed misuse,
> measured probability, biological endpoint or independent investigation.

## Consequences and uncertainty

Immediate potential consequences include inappropriate fulfillment, privacy/IP
exposure, false refusal and legitimate-research delay. Any downstream
biosecurity or biological consequence additionally depends on recipient intent,
capability, custody, use and other safeguards not evaluated here.

Canonical THR-0006, HAZ-0007 and VUL-0007 branches now represent intentional,
accidental and deficient-state classes, and NIST measures bounded test-edge
variation. No incident, technique, order occurrence, likelihood, unsafe
fulfilment or downstream biological harm is represented.

> **Claim record — RSK-0008-C04 | analytic-judgment**
> **Claim:** NASEM supports an additional abstract upstream branch in which an
> AI-enabled biological-design output becomes an order input and then crosses
> the existing screening-decision→fulfillment boundary; it does not establish
> evasion, occurrence or biological harm.
> **Claim status:** active
> **Scope:** Defensive design-output→screening→possible-fulfillment path with
> all operational design and screening detail withheld.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 4 §AI and Biodesign Security, printed pp. 50–53 (physical pp. 71–74).
> **Basis / limits:** The report directly links AI design, screening challenge
> and synthesis chokepoint; the conditional failure path is wiki analysis. No
> exact design, sequence, screening weakness, order, actor, event or outcome is
> represented.

## Empirical classification-edge update

> **Claim record — RSK-0008-C05 | analytic-judgment**
> **Claim:** NIST's blinded benchmark directly observes labelled
> classification misses and disagreements at the screening edge, while the
> SecureDNA paper adds aggregate historical-order decision outputs; together
> they strengthen only the classification/decision branch and do not observe
> approval-to-fulfilment transfer, unsafe use or biological harm.
> **Claim status:** active
> **Scope:** Bounded empirical support for one scenario edge; not a ground-
> truth evaluation of the operational corpus, provider-wide deployment,
> incident, probability or complete risk-chain confirmation.
> **As of:** Evidence package reviewed 2026-07-13.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
> SRC-0059-C03–C07; [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md),
> SRC-0061-C03–C06; [CTL-0024](../controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md),
> CTL-0024-C02–C07.
> **Basis / limits:** Benchmark labels support the detection claim; operational
> pass/flag/denial outputs provide context but no ground truth. Both stop
> before the downstream scenario edges.

## Controls by function

[CTL-0006](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md) maps
attestation, screening, bounded human review, refusal/reporting, records,
security and lifecycle accountability to exact edges. They are framework
criteria, not demonstrated safeguards.

## Related pages

- [SYN-0023 — Engineering-biology transfer reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
- [AST-0004](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md)
- [WFL-0008](../workflows/wfl-0008-nucleic-acid-procurement-screening-lifecycle.md)
- [SYS-0006](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [CTL-0006](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [GOV-0002](../governance/gov-0002-us-federally-funded-nucleic-acid-screening-2024.md)
- [GOV-0003](../governance/gov-0003-uk-synthetic-nucleic-acid-screening-2024.md)
- [SYN-0002](../syntheses/syn-0002-us-uk-nucleic-acid-screening-comparison.md)
- [RSK-0016 — Broader biological-AI output risk](rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [WFL-0011 — Biological AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md)
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [HAZ-0007 — Accidental screening/lifecycle failures](../hazards/haz-0007-engineering-biology-screening-synthesis-and-lifecycle-failures.md)
- [VUL-0007 — Screening and integration exposure classes](../vulnerabilities/vul-0007-synthesis-screening-definition-database-integration-and-supply-exposures.md)
- [CTL-0024 — Benchmark-bounded assurance](../controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md)
- [SYN-0032 — Engineering-biology reconciliation](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)

## Sources

- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md), §§I–V,
  printed pp. 4–13.
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
  HTML lines 841–1050.
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
  Chapter 4, printed pp. 50–53 (physical pp. 71–74).
- [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
  aggregate benchmark and failure limits.
- [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md),
  aggregate operational-data context and independence limits.
