---
id: THR-0001
type: threat
title: Adversarial biological or synthetic input entering sequencing analysis
aliases:
  - malicious sequencing input threat
  - adversarial physical DNA input
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0014
sensitivity: public
dual_use: moderate
threat_kind: hypothetical-intentional-input-with-controlled-capability-demonstration
relations:
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: THR-0001-C01
    evidence:
      - source: SRC-0014
        locator: "Introduction and §3, printed pp. 765–771 (PDF pp. 2–8)"
  - predicate: enables
    target: TEC-0001
    claim_id: THR-0001-C02
    evidence:
      - source: SRC-0014
        locator: "Introduction; §§3 and 7.2, printed pp. 765–771 and 776–777 (PDF pp. 2–8 and 13–14)"
tags:
  - genomics
  - sequencing
  - adversarial-input
  - hypothetical-threat
  - controlled-proof-of-concept
---

# Adversarial biological or synthetic input entering sequencing analysis

## Threat class

An intentional actor could seek to introduce a biological, synthetic or
sequence-derived input whose digital representation reaches downstream
analysis software. The threat matters only where intake, sequencing, transfer
and processing expose an applicable trust-boundary or software weakness.

This is a **generic threat class**, not an attributed actor, campaign or
incident. `SRC-0014` demonstrates a constrained technical possibility using a
researcher-built setup; its broader actor and attack-surface discussion is
hypothetical.

> **Claim record — THR-0001-C01 | source-report**
> **Claim:** Ney et al. treat adversarial biological/synthetic input as a threat
> to the sequencing-to-analysis pipeline and demonstrate one controlled
> physical-input→digital-execution possibility against an intentionally
> weakened target.
> **Claim status:** active
> **Scope:** Source threat model and controlled proof of concept; not evidence
> of a real attacker, field event, current prevalence or sector likelihood.
> **As of:** 2017-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> Introduction and §3, printed pp. 765–771 (PDF pp. 2–8).
> **Basis / limits:** The source's research objective, controlled outcome and
> artificial target conditions are explicit. Threat extrapolation beyond that
> environment remains hypothetical.

## Target assets and prerequisites

Potential targets are sequencing/analysis availability and integrity,
bioinformatics software/process state, derived research data and downstream
decisions. The class requires all of the following at high level:

- an input of untrusted or insufficiently bounded provenance enters the
  sequencing/analysis lifecycle;
- its derived digital representation reaches downstream processing;
- an applicable input-handling weakness or unsafe assumption exists; and
- process isolation, validation, detection or containment does not interrupt
  the path.

> **Claim record — THR-0001-C02 | analytic-judgment**
> **Claim:** This threat class can enable `TEC-0001` only when an untrusted
> material/input state is transformed into processable digital data and reaches
> a compatible weakness; the source does not establish those preconditions in
> production environments.
> **Claim status:** active
> **Scope:** Defensive precondition model for sequencing and downstream
> analysis, without operational construction detail.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> Introduction; §§3 and 7.2, printed pp. 765–771 and 776–777
> (PDF pp. 2–8 and 13–14).
> **Basis / limits:** The transfer stages and required target weakness are
> supported by the PoC; production exposure, actor access and reliability are
> not. No sequence, payload, encoding or exploit procedure is retained.

## Distinctions

- The actor/event category here is intentional; the transfer method is modeled
  separately in [TEC-0001](../techniques/tec-0001-biological-input-to-digital-parser-transfer.md).
- The software weakness is
  [VUL-0001](../vulnerabilities/vul-0001-unsafe-bioinformatics-input-handling.md).
- Non-adversarial cross-sample misassignment is
  [HAZ-0001](../hazards/haz-0001-multiplex-sequencing-cross-sample-misassignment.md),
  not evidence of this threat occurring.
- The controlled path is
  [RSK-0009](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md),
  not an incident page.

## Safety boundary

No input construction, sequence, code, payload, target configuration,
adaptation or delivery route is reproduced. The defensive value lies in
treating biological input as untrusted data at a cross-domain boundary.

## Related pages

- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [AST-0001](../assets/ast-0001-genomic-data.md)
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [TEC-0001](../techniques/tec-0001-biological-input-to-digital-parser-transfer.md)
- [VUL-0001](../vulnerabilities/vul-0001-unsafe-bioinformatics-input-handling.md)
- [RSK-0009](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md)

## Sources

- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
  Introduction, §§3 and 7.2.
