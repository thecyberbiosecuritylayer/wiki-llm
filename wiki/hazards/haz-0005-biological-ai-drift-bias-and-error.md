---
id: HAZ-0005
type: hazard
title: Biological-AI drift, bias, error and non-adoption hazard
aliases:
  - biological model performance drift
  - non-adversarial life-science AI failure
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0033
  - SRC-0049
  - SRC-0050
  - SRC-0052
sensitivity: public
dual_use: low
hazard_kind: non-adversarial-distribution-performance-use-and-decision-failure
relations:
  - predicate: evidenced-by
    target: SRC-0049
    claim_id: HAZ-0005-C01
    evidence:
      - source: SRC-0049
        locator: "ETSI EN clause 5.4.2, p. 15; ETSI TR §6.12, pp. 65–69"
  - predicate: evidenced-by
    target: SRC-0050
    claim_id: HAZ-0005-C02
    evidence:
      - source: SRC-0050
        locator: "Results/Figure 2, article pp. 2–4; Discussion p. 7; Methods pp. 8–9"
  - predicate: evidenced-by
    target: SRC-0052
    claim_id: HAZ-0005-C03
    evidence:
      - source: SRC-0052
        locator: "journal pp. 1621–1628 and 1630–1633, Figures 2–8 and 12"
  - predicate: affects
    target: RSK-0016
    claim_id: HAZ-0005-C04
    evidence:
      - source: SRC-0033
        locator: "Chapters 2–5, printed pp. 19–37 and 46–81 (physical pp. 40–58 and 67–102)"
tags:
  - artificial-intelligence
  - hazard
  - drift
  - bias
  - error
  - generalizability
  - monitoring
---

# Biological-AI drift, bias, error and non-adoption hazard

## Hazard class

This page covers non-adversarial mismatch between model/data state and the
current population, task, environment or decision context. It includes data,
model or concept drift, biased or erroneous outputs, performance degradation,
miscalibration and failure to fit actual work. It is not evidence of an actor
or malicious method.

> **Claim record — HAZ-0005-C01 | source-report**
> **Claim:** The EN requires production logging and recommends analysis of
> logs plus internal-state and performance monitoring; the informative TR adds
> data/model/concept drift, error-rate, accuracy and bias examples. Those
> observations can inform review or update, while retirement remains a
> separate decision and requirement family.
> **Claim status:** active
> **Scope:** Current deployable-AI standard and informative implementation
> examples; not biological incidence, a universal metric or effectiveness.
> **As of:** ETSI EN 304 223 V2.1.1 and TR 104 128 V1.1.1.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> ETSI EN clause 5.4.2, p. 15; ETSI TR §6.12, pp. 65–69.
> **Basis / limits:** EN `shall` and `should` force levels and TR examples are
> kept separate. Neither artifact shows that a hazard occurred, that monitoring
> detects every failure or that observation automatically requires withdrawal.

## Oncology implementation observation

> **Claim record — HAZ-0005-C02 | source-report**
> **Claim:** A named oncology governance programme reports formal post-launch
> review of 33 live nomograms, monitoring plans and reports, six-to-twelve-
> month review after launch or major revision, and two model sunsets when the
> evidence base had evolved.
> **Claim status:** active
> **Scope:** One institutional oncology programme and its reported governance
> actions; not proof of patient harm avoided, independent effectiveness,
> general deployment prevalence or cybersecurity performance.
> **As of:** 2025 publication.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md),
> Results/Figure 2, article pp. 2–4; Discussion p. 7; Methods pp. 8–9.
> **Basis / limits:** Counts and governance states are direct issuer/author
> observations. The paper does not provide an independent patient-outcome or
> counterfactual effectiveness evaluation.

## Benchmark failure and generalizability evidence

> **Claim record — HAZ-0005-C03 | source-report**
> **Claim:** CASP15 reports model-performance differences and failure limits
> across target difficulty and taxa, including shallow-alignment and viral-
> target challenges plus interface, conformation and side-chain limits; high
> global structural quality did not guarantee catalytic-site accuracy.
> **Claim status:** active
> **Scope:** Blind protein-structure benchmark; not deployment drift, clinical
> validation, adversarial robustness or biological harm.
> **As of:** CASP15 assessment published 2023.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0052](../sources/src-0052-casp15-tertiary-structure-assessment-2023.md),
> journal pp. 1621–1628 and 1630–1633, Figures 2–8 and 12.
> **Basis / limits:** The assessor-led results and limits are direct. They
> demonstrate task-specific failure/generalizability, not temporal drift.

## Consequence boundary

> **Claim record — HAZ-0005-C04 | analytic-judgment**
> **Claim:** `HAZ-0005` affects `RSK-0016` only when an erroneous or stale
> output passes applicable review/experimental gates and changes a downstream
> action; observed model retirement or benchmark failure is not itself an
> adverse biological or clinical outcome.
> **Claim status:** active
> **Scope:** Defensive hazard-to-risk mapping.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> DBTL and decision-boundary discussion, printed pp. 19–37 and 64–81;
> `HAZ-0005-C01`–`C03`; [RSK-0016](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md).
> **Basis / limits:** The action boundary is source-supported; the conditional
> exact-edge relation is analytic and does not assert a real incident.

## Related pages

- [THR-0003 — Intentional AI threat](../threats/thr-0003-adversarial-ai-data-model-and-interface-actions.md)
- [TEC-0002 — High-level transfer techniques](../techniques/tec-0002-ai-data-model-manipulation-and-extraction.md)
- [VUL-0004 — AI exposure classes](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md)
- [WFL-0013 — Secure model lifecycle](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md)
- [RSK-0016 — Biological-AI output risk](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [SRC-0049 — ETSI AI cybersecurity](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md)
- [SRC-0050 — Oncology governance](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md)
- [SRC-0052 — CASP15](../sources/src-0052-casp15-tertiary-structure-assessment-2023.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)

## Sources

- [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md).
- [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md).
- [SRC-0052](../sources/src-0052-casp15-tertiary-structure-assessment-2023.md).
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md).
