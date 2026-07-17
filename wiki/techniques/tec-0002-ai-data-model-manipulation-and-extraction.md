---
id: TEC-0002
type: technique
title: High-level AI data, model and information transfer techniques
aliases:
  - defensive AI manipulation and extraction taxonomy
  - AI state-transfer method classes
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
technique_kind: defensive-high-level-data-model-interface-transfer-taxonomy
relations:
  - predicate: evidenced-by
    target: SRC-0049
    claim_id: TEC-0002-C01
    evidence:
      - source: SRC-0049
        locator: "ETSI TR threat envelope and §§6.2.5–6.2.8/6.12, pp. 15–28 and 65–69; ETSI EN clauses 5.1.3/5.2.1–5.2.4, pp. 11–13"
  - predicate: exploits
    target: VUL-0004
    claim_id: TEC-0002-C02
    evidence:
      - source: SRC-0049
        locator: "ETSI EN clauses 5.2.1–5.2.4, pp. 12–13; ETSI TR §§6.2.5–6.2.8, pp. 25–28"
  - predicate: affects
    target: SYS-0013
    claim_id: TEC-0002-C02
    evidence:
      - source: SRC-0049
        locator: "ETSI lifecycle, asset/dependency, interface and monitoring requirements, EN pp. 10–15"
  - predicate: enables
    target: RSK-0016
    claim_id: TEC-0002-C03
    evidence:
      - source: SRC-0033
        locator: "Chapters 3–5, printed pp. 28–37 and 46–81 (physical pp. 49–58 and 67–102)"
tags:
  - artificial-intelligence
  - technique
  - defensive-taxonomy
  - data-state
  - model-state
  - confidentiality
---

# High-level AI data, model and information transfer techniques

## Method classes

This page records only the abstract transformation being attempted, not actor
identity, target details or instructions. The represented classes are:

- corrupt or bias training, evaluation or runtime data state;
- alter model, configuration or dependency state;
- misuse an interface so untrusted input changes model/tool behavior;
- infer or extract protected information from data/model behavior; and
- inherit compromised state through a software, container, model or dataset
  supply dependency.

> **Claim record — TEC-0002-C01 | analytic-judgment**
> **Claim:** ETSI names data poisoning, model tampering, interface-mediated
> action, information disclosure/extraction and supply-chain compromise as
> threat/control categories; this page defensively normalizes their abstract
> state transformations into high-level method classes.
> **Claim status:** active
> **Scope:** Defensive taxonomy only; not operational procedure, demonstrated
> success, biological targeting, frequency or severity.
> **As of:** ETSI EN 304 223 V2.1.1 and TR 104 128 V1.1.1.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> ETSI TR threat envelope and §§6.2.5–6.2.8/6.12, pp. 15–28 and 65–69;
> ETSI EN clauses 5.1.3 and 5.2.1–5.2.4, pp. 11–13.
> **Basis / limits:** The categories are direct; their organization as a
> separate canonical `TEC` role is wiki analysis. The informative TR and
> normative EN remain one ETSI lineage.

## Conditional path

> **Claim record — TEC-0002-C02 | analytic-judgment**
> **Claim:** A represented method can affect `SYS-0013` only by crossing an
> applicable data, identity, API, registry, runtime or dependency boundary and
> exploiting a weakness represented by `VUL-0004`; method classification does
> not establish that the boundary exists in a named deployment.
> **Claim status:** active
> **Scope:** Canonical defensive graph semantics, without topology or
> implementation detail.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `TEC-0002-C01`;
> [SYS-0013](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md);
> [VUL-0004](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md).
> **Basis / limits:** The boundaries and dependencies are source-supported;
> the exact-edge normalization is analysis and not a reconstructed system.

> **Claim record — TEC-0002-C03 | analytic-judgment**
> **Claim:** A changed data/model/output state can enable `RSK-0016` only if
> it survives validation and human/experimental gates and then influences a
> consequential research, clinical, public-health or physical action.
> **Claim status:** active
> **Scope:** High-level cyber/digital-to-decision transfer; no claim of a real
> incident, autonomous action or biological outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> DBTL and safeguard discussion, printed pp. 19–37 and 64–81 (physical pp.
> 40–58 and 85–102); [RSK-0016](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md).
> **Basis / limits:** NASEM supports the biological-AI action boundary. It
> does not show an adversarial method reaching that boundary in practice.

## Safety boundary

No prompt, query strategy, poisoning construction, extraction sequence,
payload, target identifier, model weight, biological design or experimental
parameter is retained.

## Related pages

- [THR-0003 — Adversarial AI threat](../threats/thr-0003-adversarial-ai-data-model-and-interface-actions.md)
- [HAZ-0005 — Non-adversarial AI hazard](../hazards/haz-0005-biological-ai-drift-bias-and-error.md)
- [VUL-0004 — AI exposure classes](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md)
- [SYS-0013 — Biological MLOps boundaries](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md)
- [RSK-0016 — Biological-AI output risk](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [SRC-0049 — ETSI AI cybersecurity](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)

## Sources

- [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md).
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md).
