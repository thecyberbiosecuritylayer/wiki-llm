---
id: VUL-0004
type: vulnerability
title: Biological-AI dependency, identity, interface and data exposure classes
aliases:
  - biological MLOps exposure classes
  - AI model and data dependency weaknesses
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0033
  - SRC-0049
  - SRC-0051
  - SRC-0054
sensitivity: public
dual_use: low
vulnerability_status: generic-source-supported-current-instance-status-unknown
relations:
  - predicate: evidenced-by
    target: SRC-0049
    claim_id: VUL-0004-C01
    evidence:
      - source: SRC-0049
        locator: "ETSI EN clauses 5.1.2–5.2.4, pp. 10–13; ETSI TR §§6.2.5–6.2.8 and 6.5–6.6, pp. 25–28 and 38–44"
  - predicate: evidenced-by
    target: SRC-0051
    claim_id: VUL-0004-C02
    evidence:
      - source: SRC-0051
        locator: "§§2.1 and 3.1 with Figures 1–2, article pp. 2–3"
  - predicate: evidenced-by
    target: SRC-0054
    claim_id: VUL-0004-C03
    evidence:
      - source: SRC-0054
        locator: "NIH NOT-OD-25-081 Purpose and controlled-access-data requirements"
  - predicate: enables
    target: RSK-0016
    claim_id: VUL-0004-C04
    evidence:
      - source: SRC-0033
        locator: "Chapters 4–5, printed pp. 46–81 (physical pp. 67–102)"
      - source: SRC-0049
        locator: "ETSI EN clauses 5.1–5.5, pp. 10–15"
tags:
  - artificial-intelligence
  - vulnerability
  - dependencies
  - identity
  - api
  - model-registry
  - containers
  - controlled-data
---

# Biological-AI dependency, identity, interface and data exposure classes

## Exposure envelope

The class covers generic weaknesses or trust assumptions around packages,
container images, models, datasets, registries, APIs, runtime environments,
cloud services, identities and controlled data. It is not a finding that a
named model, laboratory, institution or repository is vulnerable.

> **Claim record — VUL-0004-C01 | source-report**
> **Claim:** ETSI requires AI-system inventories and risk treatment to include
> software, model, dataset, hardware and service dependencies, their versions
> and interfaces, separated environments and least-privilege access; its
> companion TR explicitly includes packages, container images and model
> registries among the dependency and boundary classes.
> **Claim status:** active
> **Scope:** Generic deployable-AI exposure and control classes; not a
> deployment inventory, vulnerability scan, conformity result or prevalence.
> **As of:** ETSI EN 304 223 V2.1.1 and TR 104 128 V1.1.1.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> ETSI EN clauses 5.1.2–5.2.4, pp. 10–13; ETSI TR §§6.2.5–6.2.8 and 6.5–6.6,
> pp. 25–28 and 38–44.
> **Basis / limits:** EN requirements and TR examples are direct but form one
> lineage. The literal container/model-registry examples are informative, not
> separate normative `shall` requirements.

## Biomedical implementation context

> **Claim record — VUL-0004-C02 | source-report**
> **Claim:** `mlf-core` supplies a direct biomedical-research implementation
> context for packaged code, GPU containers, isolated environments, model
> registry/MLflow and service interfaces across single-cell, gene-expression
> and liver-tumour examples.
> **Claim status:** active
> **Scope:** Reported framework components and research examples; not a
> security assessment, named weakness, current deployment census or control
> effectiveness result.
> **As of:** 2023 publication record.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md),
> §§2.1 and 3.1 with Figures 1–2, article pp. 2–3.
> **Basis / limits:** Components and biomedical examples are direct. Their
> existence does not prove secure configuration, adoption or vulnerability.

## Controlled genomic-data boundary

> **Claim record — VUL-0004-C03 | source-report**
> **Claim:** NIH's current clarification treats public generative-AI upload of
> NIH controlled-access human genomic data as inconsistent with the applicable
> data-use commitment and treats resulting models/parameters as controlled
> derivatives, limiting use to the NIH-approved purpose and sharing to
> approved-user collaborators.
> **Claim status:** active
> **Scope:** NIH controlled-access human genomic data under approved use; not
> all genomic data, all U.S. research, a technical exploit or proof of leakage.
> **As of:** NOT-OD-25-081, 2025-03-28.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md),
> NOT-OD-25-081, Purpose and stated controlled-access-data requirements.
> **Basis / limits:** The policy classification and boundary are direct. A
> prohibited transfer condition is not evidence that a breach occurred.

## Canonical weakness and exposure conditions

The inventory items above become vulnerability/exposure classes only under a
deficient or uncontrolled state. The canonical conditions are:

- an external package, container, model or dataset reaches build/runtime
  without adequate identity, version, integrity or provenance assurance;
- API, registry, service or human privileges exceed the intended role, or
  changes cannot be attributed to an authenticated identity;
- development, test and production state is insufficiently separated, so an
  unapproved or unvalidated state can cross a promotion boundary; or
- protected data or a governed derivative can cross its authorized use,
  collaborator, transfer or closeout boundary.

> **Claim record — VUL-0004-C05 | analytic-judgment**
> **Claim:** `VUL-0004` denotes untrusted/unverified dependency state,
> overbroad or unattributable identity/API/registry access, inadequate
> environment separation and uncontrolled protected-data/derivative transfer;
> it does not label packages, containers, registries, APIs or open research as
> vulnerabilities merely because they exist.
> **Claim status:** active
> **Scope:** Non-actionable canonical weakness/exposure semantics; not a named
> instance, exploitability finding, severity score or compliance conclusion.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `VUL-0004-C01`–`C03`; ETSI EN clauses 5.1.2–5.2.4 and TR
> §§6.2.5–6.6.6; NIH NOT-OD-25-081 transfer, approved-use, collaborator and
> closeout boundaries.
> **Basis / limits:** Expected-control and data-use boundaries are direct;
> expressing their deficient state as an exposure is defensive analysis. No
> current organization or artifact is asserted to meet a deficient condition.

## Conditional consequence

> **Claim record — VUL-0004-C04 | analytic-judgment**
> **Claim:** These exposure classes enable `RSK-0016` only when relevant reach,
> dependency criticality, altered or disclosed state and failed validation or
> containment coincide; an inventory item or open interface alone is not a
> compromise or downstream consequence.
> **Claim status:** active
> **Scope:** Defensive exact-edge model, without facility topology,
> configuration, exploitability score or event attribution.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `VUL-0004-C01`–`C03`;
> [RSK-0016](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md);
> [CTL-0021](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md).
> **Basis / limits:** Sources provide the dependency and policy boundaries;
> the canonical causal conjunction is analytic and intentionally conditional.

## Related pages

- [THR-0003 — Adversarial AI threat](../threats/thr-0003-adversarial-ai-data-model-and-interface-actions.md)
- [TEC-0002 — High-level transfer techniques](../techniques/tec-0002-ai-data-model-manipulation-and-extraction.md)
- [HAZ-0005 — Drift, bias and error hazard](../hazards/haz-0005-biological-ai-drift-bias-and-error.md)
- [SYS-0013 — Biological MLOps boundaries](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md)
- [RSK-0016 — Biological-AI output risk](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [SRC-0049 — ETSI AI cybersecurity](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md)
- [SRC-0051 — mlf-core](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md)
- [SRC-0054 — NIH genomic AI policy](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md)
- [SYN-0029 — AIB reconciliation](../syntheses/syn-0029-biological-ai-lifecycle-threat-benchmark-governance-reconciliation.md)

## Sources

- [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md).
- [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md).
- [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md).
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md).
