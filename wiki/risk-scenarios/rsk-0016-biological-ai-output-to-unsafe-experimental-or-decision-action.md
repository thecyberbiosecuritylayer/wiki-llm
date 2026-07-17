---
id: RSK-0016
type: risk-scenario
title: Biological-AI output to unsafe experimental or decision action
aliases:
  - biological model output integrity and misuse risk
  - AI design output to unsafe action
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0033
  - SRC-0034
sensitivity: public
dual_use: moderate
origin_domain: mixed
origin_domain_components:
  - biological
  - digital
destination_domains:
  - digital
  - physical
  - biological
  - clinical
  - public-health
relations:
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: RSK-0016-C01
    evidence:
      - source: SRC-0033
        locator: "Chapters 3 and 5, printed pp. 28–40 and 73–80 (physical pp. 49–61 and 94–101); Figure 5-2"
  - predicate: depends-on
    target: AST-0008
    claim_id: RSK-0016-C02
    evidence:
      - source: SRC-0033
        locator: "Chapter 5, printed pp. 64–80 (physical pp. 85–101)"
  - predicate: depends-on
    target: SYS-0011
    claim_id: RSK-0016-C02
    evidence:
      - source: SRC-0033
        locator: "Figures 2-1 and 5-2, printed pp. 20 and 73 (physical pp. 41 and 94)"
  - predicate: affects
    target: WFL-0011
    claim_id: RSK-0016-C03
    evidence:
      - source: SRC-0033
        locator: "Chapter 2, printed pp. 19–25 (physical pp. 40–46); Chapter 5, printed pp. 73–80 (physical pp. 94–101)"
  - predicate: evidenced-by
    target: SRC-0034
    claim_id: RSK-0016-C05
    evidence:
      - source: SRC-0034
        locator: "§§4–5, pp. 6–9; Appendix §§A.2–A.3.2, pp. 28–31; detailed results, pp. 35–45"
tags:
  - artificial-intelligence
  - biological-models
  - data-integrity
  - model-security
  - experimental-safety
  - decision-safety
---

# Biological-AI output to unsafe experimental or decision action

## Scenario

An erroneous, corrupted, insufficiently validated or deliberately misused
biological-AI state produces a misleading prediction, classification, score or
candidate design. If provenance, evaluation and accountable decision gates do
not detect or contain the state, the output can influence an experiment,
material/order decision, countermeasure programme, surveillance response or
other consequential use. The downstream state may be wasted work, delayed
response, incorrect interpretation or unsafe biological/clinical action.

This is a defensive hypothesis family—not an incident and not a guide for
creating or evading safeguards. Model, sequence, target, prompt, experimental
and screening details are intentionally absent.

> **Claim record — RSK-0016-C01 | source-report**
> **Claim:** NASEM describes potential paths from noisy, biased, incomplete or
> manipulated data/model/software state to erroneous or unsafe biological-AI
> outputs and downstream research, experimental, countermeasure or decision
> consequences.
> **Claim status:** active
> **Scope:** High-level potential failure/misuse classes; not an observed
> incident, exploit mechanism, likelihood estimate or verified causal outcome.
> **As of:** 2025-04-23.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 2, printed pp. 21–25 (physical pp. 42–46); Chapter 3, printed pp.
> 28–40 (physical pp. 49–61); Chapter 5, printed pp. 73–80 (physical pp.
> 94–101), especially Figure 5-2.
> **Basis / limits:** Threat, hazard and consequence classes are direct.
> Examples are report synthesis/citations and cannot establish frequency,
> feasibility, attributable harm or an operational attack path.

## Assets and workflow

The scenario depends on:

- data, labels, provenance, model, code/dependency, compute, output and actor
  classes in [AST-0008](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md);
- repository, compute, model/API, application and laboratory boundaries in
  [SYS-0011](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md);
- the acquire/curate→train/analyze→evaluate→gate→build/test/use→feedback states
  in [WFL-0011](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md).

> **Claim record — RSK-0016-C02 | analytic-judgment**
> **Claim:** The scenario depends on susceptible data/model/software assets in
> `AST-0008`, transfer boundaries in `SYS-0011`, a consequential output, an
> insufficiently effective validation/decision gate and a receiving
> experimental or decision context.
> **Claim status:** active
> **Scope:** Necessary high-level conditions for this hypothesis; not a claim
> that they coexist in any named system.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Figures 2-1 and 5-2, printed pp. 20 and 73 (physical pp. 41 and 94); Chapter
> 5, printed pp. 73–80 (physical pp. 94–101).
> **Basis / limits:** Source layers, transfers and possible consequences are
> direct; the necessary-condition form is wiki analysis. No deployed topology,
> actor access, target state or control failure is established.

## Origin-domain state

Two branches are kept distinct.

### Non-adversarial or systemic error

- incomplete, noisy, poorly labeled, unrepresentative or changing biological
  evidence;
- model limitation, bias, generalization error or inappropriate task transfer;
- software/dependency defect or configuration/version mismatch;
- recursively generated data and feedback that amplify low-quality state;
- misuse of predicted or synthetic state as if experimentally established.

### Deliberate manipulation or misuse

- data poisoning or other integrity manipulation;
- hidden or altered model behavior;
- bypass or removal of intended safeguards;
- malicious adaptation/instruction of a model;
- deliberate use of a legitimate capability for a harmful purpose.

The report does not establish that any branch occurred in a named biological-
AI deployment.

## Cross-domain transfer

The defensive path is:

`biological data/context → digital model/software state → prediction/design/
decision output → human or automated gate → experiment/material/order/clinical
or public-health action → biological or programme state`.

Feedback can return experimental/result state to the data/model layer. This
can improve later work when evidence is valid and governed, or amplify error
when provenance and reconciliation fail.

> **Claim record — RSK-0016-C03 | analytic-judgment**
> **Claim:** `RSK-0016` affects the output-selection, experimental/decision
> gate, physical build/test/use and result-feedback edges of `WFL-0011`.
> **Claim status:** active
> **Scope:** Exact lifecycle-edge mapping for defensive analysis; not an
> observed compromise or assertion that every model output crosses all edges.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 2, printed pp. 19–25 (physical pp. 40–46); Chapter 5 and Figure 5-2,
> printed pp. 73–80 (physical pp. 94–101); Appendix A Figure A-1, printed p.
> 89 (physical p. 110).
> **Basis / limits:** DBTL/layer paths and potential failure effects are
> direct; exact-edge normalization is inferred. Appendix A is attributed
> background in the same lineage, not corroboration.

## Receiving-domain state and consequences

Potential receiving states are kept at class level:

- an experiment or material/order action based on a weakly justified output;
- an ineffective or misdirected research/countermeasure candidate;
- erroneous surveillance, classification, prioritization or response advice;
- clinical/public-health interpretation that exceeds validated scope;
- delayed work, lost resources, inappropriate confidence or public-trust harm;
- in a deliberate-misuse branch, an unsafe biological action despite remaining
  physical, expertise, validation and mitigation barriers.

The report also emphasizes limits on current high-consequence biological
design and the continuing physical build/test bottleneck. A potential
consequence is not a demonstrated capability or outcome.

> **Claim record — RSK-0016-C04 | analytic-judgment**
> **Claim:** The package establishes a plausible scenario taxonomy and transfer
> path but provides no primary incident, case count, attributable model/dataset
> scope, likelihood, measured consequence or independent confirmation.
> **Claim status:** active
> **Scope:** Evidence-state classification for this scenario; not a statement
> that no external event exists.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 3 opening, printed p. 28 (physical p. 49); conclusion, printed p. 37
> (physical p. 58); Chapter 5, printed pp. 80–81 (physical pp. 101–102).
> **Basis / limits:** NASEM explicitly describes the empirical gap and report
> limits. Cited external studies and one committee-presentation anecdote are
> not independently ingested event evidence.

> **Claim record — RSK-0016-C05 | source-report**
> **Claim:** ProteinGym directly measures the origin/output portion of this
> risk family: split design, label leakage/circularity, assay/annotation bias
> and aggregation choice can change or overstate model-performance outputs
> across biological tasks and strata.
> **Claim status:** active
> **Scope:** Primary benchmark performance consequence for ProteinGym's stated
> model/dataset scope; not poisoning, confidentiality leakage, temporal drift,
> an incident or a downstream unsafe experiment/clinical action.
> **As of:** 2023-12-15.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md),
> §§4–5, pp. 6–9; Appendix §§A.2–A.3.2, pp. 28–31; detailed results,
> pp. 35–45; `SRC-0034-C04`–`C06/C08`.
> **Basis / limits:** The benchmark observations and limitations are direct.
> Input DMS measurements are biological ground truth for comparison, not a new
> downstream outcome caused by model use; the later action branch remains
> hypothetical.

## Controls by function

[CTL-0016](../controls/ctl-0016-biological-ai-provenance-validation-decision-gates.md)
conditionally addresses:

- origin: data quality, provenance, version/dependency and access controls;
- model/output: robust evaluation, audit, uncertainty and misuse assessment;
- transfer: accountable human review, screening and experimental validation;
- application: anomaly monitoring and bounded authority;
- response/recovery: isolate suspect state, trace affected outputs, restore a
  trustworthy basis and reassess dependent decisions.

Implementation, test coverage and effectiveness remain unknown.

## Related scenarios

- [CTL-0021 — Secure monitored AI controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [HAZ-0005 — Drift/bias/error hazard](../hazards/haz-0005-biological-ai-drift-bias-and-error.md)
- [TEC-0002 — AI transfer techniques](../techniques/tec-0002-ai-data-model-manipulation-and-extraction.md)
- [VUL-0004 — AI exposure classes](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md)
- [RSK-0003 — Genomic-data integrity to decision harm](rsk-0003-genomic-data-integrity-decision-harm.md)
- [RSK-0008 — Screening/fulfillment risk](rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [RSK-0009 — Biological input to digital execution](rsk-0009-sequenced-input-to-digital-execution.md)
- [AST-0008 — Biological AI assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [WFL-0011 — Biological AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [SYS-0011 — Biological AI ecosystem](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md)
- [SRC-0033 — NASEM AI/life-sciences report](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SYN-0018 — Biological-AI SF2 reconciliation](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)
- [SRC-0034 — ProteinGym benchmark](../sources/src-0034-notin-proteingym-benchmark-2023.md)

## Sources

- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md), exact
  locators above.
- [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md), exact
  locators above.
