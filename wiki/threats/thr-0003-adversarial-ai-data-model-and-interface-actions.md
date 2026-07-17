---
id: THR-0003
type: threat
title: Adversarial actions against biological-AI data, models and interfaces
aliases:
  - biological AI adversarial threat class
  - AI data and model integrity threat
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0033
  - SRC-0049
sensitivity: public
dual_use: moderate
threat_kind: intentional-data-model-interface-and-supply-chain-action
relations:
  - predicate: evidenced-by
    target: SRC-0049
    claim_id: THR-0003-C01
    evidence:
      - source: SRC-0049
        locator: "ETSI EN 304 223 clauses 5.1.3, 5.2.1–5.2.4 and 5.4.2, pp. 11–15; ETSI TR 104 128 §§5, 6.2 and 6.12, pp. 15–28 and 65–69"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: THR-0003-C02
    evidence:
      - source: SRC-0033
        locator: "Chapters 3–5, printed pp. 28–37 and 46–81 (physical pp. 49–58 and 67–102)"
  - predicate: exploits
    target: VUL-0004
    claim_id: THR-0003-C03
    evidence:
      - source: SRC-0049
        locator: "ETSI EN clauses 5.2.1–5.2.4, pp. 12–13; ETSI TR §§6.2.5–6.2.8, pp. 25–28"
  - predicate: enables
    target: TEC-0002
    claim_id: THR-0003-C03
    evidence:
      - source: SRC-0049
        locator: "ETSI TR threat envelope and §§6.2/6.12, pp. 15–28 and 65–69"
tags:
  - artificial-intelligence
  - biological-models
  - adversarial-threat
  - data-integrity
  - model-integrity
  - confidentiality
  - supply-chain
---

# Adversarial actions against biological-AI data, models and interfaces

## Threat class

An intentional actor may try to alter data or model state, misuse an exposed
interface, obtain protected information or compromise a software/model supply
dependency. This is an actor-and-intent class. It is not the method
(`TEC-0002`), the enabling weakness (`VUL-0004`), a non-adversarial model
failure (`HAZ-0005`) or an observed incident.

> **Claim record — THR-0003-C01 | source-report**
> **Claim:** The current ETSI AI-cybersecurity package treats poisoning,
> model tampering, privacy or information-disclosure attacks, interface abuse
> and software/model supply-chain compromise as intentional threat classes;
> the package places such security analysis within a lifecycle that spans AI
> design, development, deployment, operation and retirement.
> **Claim status:** active
> **Scope:** Defensive high-level taxonomy for deployable AI systems; not an
> attack recipe, sector prevalence, successful event or biological target.
> **As of:** ETSI EN 304 223 V2.1.1, 2025-12; companion TR V1.1.1, 2025-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> ETSI EN clauses 5.1.3, 5.2.1–5.2.4 and 5.4.2, pp. 11–15; ETSI TR threat
> envelope and §§6.2/6.12, pp. 15–28 and 65–69.
> **Basis / limits:** The threat categories and lifecycle applicability are
> direct. The TR supplies examples but is informative and part of the same
> ETSI lineage as the controlling EN.

## Biological-AI applicability

NASEM independently places related data/model manipulation, software-supply,
privacy and unsafe-automation concerns in life-science data, model, DBTL and
experimental-decision contexts. It does not report a named attack or validate
the ETSI taxonomy clause by clause.

> **Claim record — THR-0003-C02 | analytic-judgment**
> **Claim:** NASEM provides the biology-specific asset and consequence bridge
> for this threat class, while ETSI supplies an independent deployed-AI threat
> taxonomy; their union does not establish that a particular biological model
> or laboratory is exposed or compromised.
> **Claim status:** active
> **Scope:** Claim-specific SF2 applicability stitch, not deployment,
> incidence, likelihood or effectiveness evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapters 3–5, printed pp. 28–37 and 46–81 (physical pp. 49–58 and 67–102);
> [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> exact locators above.
> **Basis / limits:** The institutions, genres and scopes are independent.
> Generic ETSI categories are not silently presented as observed biological
> events, and NASEM citations are not multiplied into primary sources.

## Preconditions and graph semantics

> **Claim record — THR-0003-C03 | analytic-judgment**
> **Claim:** `THR-0003` can exploit `VUL-0004` and enable the high-level
> transfer classes in `TEC-0002` only when actor access, a compatible
> dependency/interface weakness and failed prevention or containment coincide.
> **Claim status:** active
> **Scope:** Defensive precondition model; no access path, payload, prompt,
> extraction procedure, biological design or exploitability rating.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `THR-0003-C01/C02`;
> [VUL-0004](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md);
> [TEC-0002](../techniques/tec-0002-ai-data-model-manipulation-and-extraction.md).
> **Basis / limits:** The conditional relation preserves actor, method,
> weakness and consequence as separate nodes. Category presence alone is not
> proof of reach, success or downstream harm.

## Safety boundary

The page deliberately omits operational prompts, extraction procedures,
poisoning strategies, target selection, model weights, biological designs and
laboratory parameters. Defensive value is limited to classification, boundary
mapping and control selection.

## Related pages

- [AST-0008 — Biological-AI assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [WFL-0013 — Secure model lifecycle](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md)
- [SYS-0013 — Biological MLOps boundaries](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md)
- [HAZ-0005 — Drift, bias and error hazard](../hazards/haz-0005-biological-ai-drift-bias-and-error.md)
- [TEC-0002 — High-level AI transfer techniques](../techniques/tec-0002-ai-data-model-manipulation-and-extraction.md)
- [VUL-0004 — AI exposure classes](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md)
- [RSK-0016 — Biological-AI output risk](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [SRC-0033 — NASEM biological AI](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SRC-0049 — ETSI AI cybersecurity](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)

## Sources

- [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md), exact EN/TR locators above.
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md), exact report locators above.
