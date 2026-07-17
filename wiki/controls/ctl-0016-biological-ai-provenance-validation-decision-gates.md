---
id: CTL-0016
type: control
title: Biological-AI provenance, validation and decision-gate controls
aliases:
  - biological model assurance controls
  - AI-enabled life-science decision gates
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0033
  - SRC-0006
  - SRC-0005
  - SRC-0034
sensitivity: public
dual_use: low
control_status: recommended
implementation_status: unknown
testing_status: one-output-evaluation-layer-tested-not-control-family
effectiveness_status: unknown
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: CTL-0016-C01
    evidence:
      - source: SRC-0033
        locator: "Chapter 4, printed pp. 50–59 (physical pp. 71–80); Chapter 5, printed pp. 65–81 (physical pp. 86–102), especially Boxes 5-1–5-3"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: CTL-0016-C05
    evidence:
      - source: SRC-0006
        locator: "§5.1, printed pp. 22–23 (PDF pp. 33–34); Tables 10–12, 15–25 and 33; recovery Table 24, printed pp. 135–138 (PDF pp. 146–149)"
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: CTL-0016-C05
    evidence:
      - source: SRC-0005
        locator: "§4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24)"
  - predicate: mitigates
    target: RSK-0016
    claim_id: CTL-0016-C02
    evidence:
      - source: SRC-0033
        locator: "Chapter 5, printed pp. 73–81 (physical pp. 94–102)"
      - source: SRC-0006
        locator: "§5.1 and Tables 10–12, 15–25 and 33"
      - source: SRC-0005
        locator: "§4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24)"
  - predicate: depends-on
    target: AST-0008
    claim_id: CTL-0016-C03
    evidence:
      - source: SRC-0033
        locator: "Chapter 5, printed pp. 64–80 (physical pp. 85–101)"
      - source: SRC-0006
        locator: "§§5.1–5.12, printed pp. 22–28 (PDF pp. 33–39)"
  - predicate: depends-on
    target: SYS-0011
    claim_id: CTL-0016-C03
    evidence:
      - source: SRC-0033
        locator: "Figures 2-1 and 5-2, printed pp. 20 and 73 (physical pp. 41 and 94)"
  - predicate: governed-by
    target: GOV-0018
    claim_id: CTL-0016-C04
    evidence:
      - source: SRC-0033
        locator: "Summary Recommendations 1–3, printed pp. 4–8 (physical pp. 25–29); Chapter 4, printed pp. 55–59 (physical pp. 76–80)"
  - predicate: evidenced-by
    target: SRC-0034
    claim_id: CTL-0016-C07
    evidence:
      - source: SRC-0034
        locator: "§§4–5, pp. 6–9; Appendix §§A.2–A.3.2, pp. 28–31; Tables A5–A18, pp. 38–45"
tags:
  - artificial-intelligence
  - biological-models
  - provenance
  - access-control
  - software-assurance
  - validation
  - human-review
  - recovery
---

# Biological-AI provenance, validation and decision-gate controls

## Objective

Maintain a trustworthy, authorized and reviewable basis from biological data
and model/software state through digital output, experimental validation and
consequential use. Prevent or contain erroneous, corrupted or deliberately
misused state before it crosses into physical biological action or a research,
clinical or public-health decision.

This is a recommended defensive control family. It contains no product
configuration, attack recipe, screening criterion, model prompt, biological
design or laboratory procedure.

## Evidence state

| Dimension | Status | Boundary |
| --- | --- | --- |
| Recommended | yes | NASEM recommendations/review plus NIST genomic RMF/profile guidance |
| Implemented | unknown | no named biological-AI deployment record |
| Tested | partial | ProteinGym directly tests one output-evaluation layer; the complete control family is not implemented or tested |
| Effective | unknown | no exact-edge outcome/comparator result |
| Independently evaluated | unknown | no independent deployment/control evaluation in the represented corpus |

> **Claim record — CTL-0016-C01 | source-report**
> **Claim:** NASEM recommends or discusses provenance/curation, controlled
> access and sandboxes, data/software assurance, screening, adversarial and
> anomaly assessment, continuous testing/audit, human review and experimental
> validation for AI-enabled biological work.
> **Claim status:** active
> **Scope:** Committee recommendations and reviewed control functions; not a
> universal baseline, implementation, successful test or effectiveness result.
> **As of:** 2025-04-23.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Summary, printed pp. 4–8 (physical pp. 25–29); Chapter 4, printed pp. 50–59
> (physical pp. 71–80); Chapter 5, printed pp. 65–81 (physical pp. 86–102),
> especially Boxes 5-1–5-3.
> **Basis / limits:** Functions and tradeoffs are direct. Candidate methods,
> Appendix background and cited literature are not independent evidence of
> implementation or control performance.

## Scenario edges addressed

For
[RSK-0016](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md),
the family conditionally addresses:

1. **data origin/curation:** establish source, labels, consent/purpose where
   applicable, quality and custody context;
2. **software/model origin:** inventory code/dependencies, versions,
   configuration and training/validation basis;
3. **access/adaptation:** restrict and log authorized data/model/tool use;
4. **output evaluation:** test robustness, uncertainty, task fit, misuse and
   anomalous behavior without treating a grade as proof of safety;
5. **digital-to-physical transfer:** require accountable human review,
   applicable screening and experimental validation before action;
6. **monitoring:** reassess capability, data/model/software change and
   emergent vulnerability;
7. **containment/recovery:** isolate suspect state, trace affected outputs and
   dependent decisions, restore a documented trustworthy basis and revalidate
   before resumption.

> **Claim record — CTL-0016-C02 | analytic-judgment**
> **Claim:** `CTL-0016` conditionally mitigates the data/model origin,
> software/access, output-evaluation, digital-to-physical decision, monitoring
> and recovery edges of `RSK-0016`.
> **Claim status:** active
> **Scope:** Exact-edge defensive mapping; not evidence that any control is
> implemented, complete, tested or effective in a named system.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 5, printed pp. 73–81 (physical pp. 94–102);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md), §5.1
> and Tables 10–12, 15–25 and 33;
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24).
> **Basis / limits:** NASEM supplies AI/data/software/gate functions; the
> independent NIST line supplies genomic RMF monitoring, response and recovery.
> Exact scenario-edge normalization is wiki inference, and no outcome closes
> an edge empirically.

## Control matrix

| Frozen `AIB-CT` function | Safe objective | Direct support and limit |
| --- | --- | --- |
| Provenance | link data origin/creator, labels, model/tool/software dependency and training/derivation state | NASEM pp. 73–75; NIST §5.1. Completeness not measured |
| Access | apply fine-grained, purpose-aware access, sandbox and accountable user/institution boundaries | NASEM pp. 66–69, 75; applicable law/consent remains context-specific |
| Versioning | record data/software/model/configuration and update state needed to reproduce or assess an output | NASEM Figure 5-1, printed p. 70 (physical p. 91), plus layer/provenance/software context at printed pp. 73–76 (physical pp. 94–97); NIST §5.1. No complete model registry is present |
| Reproducibility | preserve experimental context, records, evaluation split and dependencies; distinguish prediction from measured result | NASEM Figure 5-1/Appendix A; cited benchmarks are not ingested tests |
| Monitoring | continuous capability/risk reassessment, anomaly detection, pen testing and update audits | NASEM pp. 58–59, 77–81. No cadence/threshold/result is demonstrated |
| Human review | accountable scientific/model review plus experimental and applicable screening gates | NASEM Chs. 2/4/5. Human presence is not a correctness guarantee |
| Recovery | contain suspect state, communicate affected data/results and verify restoration of a trustworthy data/system basis; editorially map those functions to affected AI outputs and dependent decisions | NIST IR 8432/8467 independent line; the exact AI-pipeline mapping is wiki normalization and NASEM does not give a complete recovery family |

> **Claim record — CTL-0016-C03 | analytic-judgment**
> **Claim:** Reliable operation of this control family depends on the asset
> inventory/stakeholders in `AST-0008` and the explicit data, model/API,
> application and laboratory boundaries in `SYS-0011`.
> **Claim status:** active
> **Scope:** Control prerequisites; not proof the dependencies are inventoried,
> assigned or trusted.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Figures 2-1 and 5-2, printed pp. 20 and 73 (physical pp. 41 and 94); Chapter
> 5, printed pp. 64–80 (physical pp. 85–101);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§5.1–5.12, printed pp. 22–28 (PDF pp. 33–39).
> **Basis / limits:** Required objects and boundaries are direct; dependency
> normalization is inferred. No source reports a complete biological-AI
> inventory, identity hierarchy or control owner map.

## Governance mapping

[GOV-0018](../governance/gov-0018-nasem-ai-life-sciences-advisory-recommendations-2025.md)
is the nonbinding advisory basis for the NASEM-derived functions. NIST
IR 8432/8467 are independent technical guidance/draft profile lines. None is a
universal legal mandate, and applicability still depends on jurisdiction,
organization, data, research and system context.

> **Claim record — CTL-0016-C04 | analytic-judgment**
> **Claim:** `CTL-0016` is governed-by `GOV-0018` only in the sense of an
> advisory NASEM recommendation basis; the relation does not establish binding
> force, adoption, compliance or authority over a deployment.
> **Claim status:** active
> **Scope:** Governance semantics of the typed relation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Summary Recommendations 1–3, printed pp. 4–8 (physical pp. 25–29); Chapter
> 4, printed pp. 55–59 (physical pp. 76–80).
> **Basis / limits:** Recommendation wording and actor allocation are direct.
> `governed-by` records the source of advisory design, not law or implementation.

## Cross-lineage completeness

> **Claim record — CTL-0016-C05 | analytic-judgment**
> **Claim:** NASEM plus the materially independent NIST genomics line
> collectively cover provenance, access, versioning, reproducibility,
> monitoring, human review and recovery functions mapped to the biological-AI
> pipeline, without establishing implementation or effectiveness.
> **Claim status:** active
> **Scope:** Collective SF2 control-function coverage for later synthesis; not
> a universal baseline or a claim that every function appears in each source.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapters 4–5, printed pp. 50–81 (physical pp. 71–102);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §5.1, printed pp. 22–23 (PDF pp. 33–34); Tables 10–12, 15–25 and 33,
> especially recovery Table 24, printed pp. 135–138 (PDF pp. 146–149);
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24).
> **Basis / limits:** Institutions and evidence lineages are independent.
> NASEM supplies AI-specific provenance/evaluation/gates; NIST supplies
> genomic data/software version context and response/recovery. Affected-output
> and dependent-decision mapping is editorial exact-edge normalization rather
> than a literal NIST model-output rollback claim. Coverage is functional, not
> implementation/testing/effectiveness evidence.

## Failure modes and tradeoffs

- Provenance can be incomplete, wrong or too coarse to isolate affected output.
- Restrictive access or screening can delay beneficial work and generate false
  positives; permissive access can increase misuse or privacy risk.
- Version records without environment/dependency detail may not reproduce a
  result.
- Benchmarks may reward narrow task performance and miss new unsafe capability.
- Red teaming or anomaly detection has unknown coverage and can miss latent
  behavior.
- Human reviewers can be overconfident, lack context or inherit model bias.
- Experimental testing is resource-intensive and not a universal detector.
- Restoring a running system does not restore trustworthy data/model/output or
  reverse a downstream decision.

## Validation and evidence of effectiveness

> **Claim record — CTL-0016-C06 | analytic-judgment**
> **Claim:** The represented corpus contains recommended assessment and
> validation methods but no direct independent study showing that `CTL-0016`
> was implemented, tested successfully, effective or safely generalizable.
> **Claim status:** active
> **Scope:** Evidence-state classification for this control family.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 5, printed pp. 79–81 (physical pp. 100–102); Appendix A benchmark
> discussion, printed pp. 103–104 and 115–119 (physical pp. 124–125 and
> 136–140); NIST sources at the locators above.
> **Basis / limits:** Methods and limitations are direct. Reviewed/cited
> studies are not ingested primary tests, and NIST guidance/profile outcomes
> are target states rather than deployment results.

> **Claim record — CTL-0016-C07 | analytic-judgment**
> **Claim:** ProteinGym directly tests one output-evaluation layer—multiple
> splits, metrics and biological strata with explicit leakage/bias/failure
> limits—but does not implement or independently evaluate the complete
> provenance/access/versioning/monitoring/human-gate/recovery control family.
> **Claim status:** active
> **Scope:** Partial empirical evidence for model-output evaluation within
> `AIB-AE`; not deployment, downstream safety, control-family implementation or
> independent effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md),
> §§4–5, pp. 6–9; Appendix §§A.2–A.3.2, pp. 28–31; Tables A5–A18,
> pp. 38–45; `SRC-0034-C04`–`C08`.
> **Basis / limits:** Evaluation functions and measured variability are direct;
> mapping them to one `CTL-0016` layer is analysis. Author overlap with several
> evaluated methods and absence of an external replication prevent SF3.

## Related pages

- [RSK-0016 — AI output to unsafe action](../risk-scenarios/rsk-0016-biological-ai-output-to-unsafe-experimental-or-decision-action.md)
- [AST-0008 — Biological AI assets](../assets/ast-0008-ai-enabled-biological-data-model-stakeholder-assets.md)
- [WFL-0011 — Biological AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [SYS-0011 — Biological AI ecosystem](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md)
- [GOV-0018 — NASEM advisory governance](../governance/gov-0018-nasem-ai-life-sciences-advisory-recommendations-2025.md)
- [CTL-0002 — Genomic-data RMF controls](ctl-0002-genomic-data-risk-management.md)
- [CTL-0006 — Nucleic-acid screening controls](ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [SRC-0033 — NASEM AI/life-sciences report](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SYN-0018 — Biological-AI SF2 reconciliation](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)
- [SRC-0034 — ProteinGym benchmark](../sources/src-0034-notin-proteingym-benchmark-2023.md)

## Sources

- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md).
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md).
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md).
- [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md).
