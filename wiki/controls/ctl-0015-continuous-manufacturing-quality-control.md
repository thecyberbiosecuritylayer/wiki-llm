---
id: CTL-0015
type: control
title: Continuous-manufacturing state-of-control, quality gates and disposition
aliases:
  - ICH Q13 quality controls
  - continuous manufacturing diversion and release controls
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2027-01-08
source_ids:
  - SRC-0003
  - SRC-0018
  - SRC-0031
sensitivity: public
dual_use: low
implementation_status: recommended
testing_status: method-specified-no-transaction-result
effectiveness_status: unknown
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0031
    claim_id: CTL-0015-C01
    evidence:
      - source: SRC-0031
        locator: "Part I §§3.1–3.3 and 4.1–4.10, printed pp. 2–14 (physical pp. 7–19); Annex III §§2–3, printed pp. 28–30 (physical pp. 33–35); Annex V §§1–3.3, printed pp. 37–41 (physical pp. 42–46)"
  - predicate: governed-by
    target: GOV-0016
    claim_id: CTL-0015-C01
    evidence:
      - source: SRC-0031
        locator: "ICH Step 4 cover/history, physical pp. 1–2; Part I §§3–4, printed pp. 2–14 (physical pp. 7–19)"
  - predicate: depends-on
    target: SYS-0002
    claim_id: CTL-0015-C02
    evidence:
      - source: SRC-0003
        locator: "§ Digital Information Flow in Biomanufacturing; Figure 1"
      - source: SRC-0031
        locator: "Part I §§3.1.4–3.1.7 and 4.1–4.4, printed pp. 4–10 (physical pp. 9–15)"
  - predicate: mitigates
    target: RSK-0002
    claim_id: CTL-0015-C02
    evidence:
      - source: SRC-0018
        locator: "§§5.2.3, 5.4 and 6.1–6.2, printed pp. 71–75, 83–125 (PDF pp. 88–92, 100–142)"
      - source: SRC-0031
        locator: "Part I §§3.1.1–3.1.7 and 4.1–4.2, printed pp. 2–10 (physical pp. 7–15)"
  - predicate: detects
    target: RSK-0002
    claim_id: CTL-0015-C02
    evidence:
      - source: SRC-0018
        locator: "§§6.3.1–6.3.3, printed pp. 126–133 (PDF pp. 143–150)"
      - source: SRC-0031
        locator: "Part I §§3.1.1–3.1.7 and 4.2, printed pp. 2–10 (physical pp. 7–15); Annex III §2.3, printed p. 29 (physical p. 34)"
  - predicate: contains
    target: RSK-0002
    claim_id: CTL-0015-C03
    evidence:
      - source: SRC-0018
        locator: "§§4.2.2, 6.2.4.5 and 6.4, printed pp. 55, 114–117, 134–137 (PDF pp. 72, 131–134, 151–154)"
      - source: SRC-0031
        locator: "Part I §§3.1.6 and 4.1–4.2/4.8, printed pp. 5, 8–10, 12 (physical pp. 10, 13–15, 17); Annex V §§3.1–3.3, printed pp. 38–41 (physical pp. 43–46)"
  - predicate: recovers
    target: RSK-0002
    claim_id: CTL-0015-C04
    evidence:
      - source: SRC-0018
        locator: "§§5.3.2, 6.2.4.3–6.2.4.5 and 6.5, printed pp. 79–80, 112–117, 137–138 (PDF pp. 96–97, 129–134, 154–155)"
      - source: SRC-0031
        locator: "Part I §§3.1.6 and 4.2/4.8, printed pp. 5, 8–10, 12 (physical pp. 10, 13–15, 17); Annex V §§3.2–3.3, printed pp. 39–41 (physical pp. 44–46)"
tags:
  - biomanufacturing
  - continuous-manufacturing
  - process-quality
  - monitoring
  - diversion
  - disposition
  - validation
---

# Continuous-manufacturing state-of-control, quality gates and disposition

## Objective and evidence state

This control family joins two different but complementary layers:

- ICH Q13 supplies continuous-manufacturing material/process/quality gates;
- NIST SP 800-82r3 supplies generic OT access, integrity, monitoring, response
  and trusted-digital-restoration functions.

The stitch is conditional on the sector dependency in Guttieres et al. It is
not a claim that one facility implemented the combined portfolio. All controls
remain recommended/design-level; tests, effectiveness and independent
evaluation are unknown.

> **Claim record — CTL-0015-C01 | source-report**
> **Claim:** Q13's quality-control family spans input/material characterization,
> equipment/system integration, state-of-control monitoring, PAT/sampling,
> models, traceability/diversion, release/reference testing, process/model
> validation, PQS investigation/CAPA and lifecycle change.
> **Claim status:** active
> **Scope:** Q13 continuous-manufacturing control design; not a complete cyber
> control baseline, implementation result or universal process prescription.
> **As of:** 2022-11-16.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1–3.3 and 4.1–4.10, printed pp. 2–14
> (physical pp. 7–19); Annex III §§2–3, printed pp. 28–30
> (physical pp. 33–35); Annex V §§1–3.3, printed pp. 37–41
> (physical pp. 42–46).
> **Basis / limits:** Functions and exact quality edges are direct. Annex
> examples are illustrative, and Q13 does not supply cyber access or recovery.

## Scenario edges addressed

| Function | Exact `RSK-0002` edge | Q13 quality-side action | Required cyber-side complement |
| --- | --- | --- | --- |
| Prevent | variable input/equipment/model state → unreliable process/control premise | input/material characterization, equipment integrity/integration, validated model assumptions and acceptance criteria | asset/boundary inventory, authorized change, segmentation and configuration integrity |
| Detect | process/material/equipment state → missing or misleading digital assessment | PAT/sampling, trend/drift/data-gap review, model monitoring, reference/offline testing | cyber integrity/availability monitoring, attributable event logging and independent signal paths |
| Contain/respond | detected deviation → continued processing or collection | pause/stop, traceable diversion, quarantine/offline test, investigation, root cause and CAPA | safe isolation, incident command and preservation of trustworthy evidence |
| Re-enter/recover | diverted/paused state → resumed collection and final disposition | predefined restart/collection criteria, complete affected-material diversion, disposition and PQS decision | trusted digital restoration, configuration/data validation and reconciliation before process use |
| Assure | control design → confidence in intended use | model/process validation, continuous process verification, acceptance metrics and lifecycle monitoring | independent cyber assessment, restoration exercise and measured outcome evidence |

> **Claim record — CTL-0015-C02 | analytic-judgment**
> **Claim:** Q13 prevention/detection gates and NIST OT access/integrity/
> monitoring controls conditionally interrupt the premise→measurement→control
> portion of `RSK-0002`, provided the mapped sensor/model/control boundary
> actually governs the affected process.
> **Claim status:** active
> **Scope:** Generic biopharmaceutical/continuous-manufacturing dependency;
> not a named architecture, guaranteed detection or observed attack.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> §Digital Information Flow in Biomanufacturing and Figure 1;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§5.2.3, 5.4 and 6.1–6.3, printed pp. 71–75, 83–133;
> [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
> §§3.1.1–3.1.7 and 4.1–4.2, printed pp. 2–10
> (physical pp. 7–15); Annex III §2.3, printed p. 29
> (physical p. 34).
> **Basis / limits:** Sector coupling, quality gates and generic cyber controls
> are direct across independent lineages; their exact conjunction is editorial
> and deployment-specific.

> **Claim record — CTL-0015-C03 | analytic-judgment**
> **Claim:** Traceability, pause/diversion, quarantine/testing, investigation
> and CAPA map to containment/response after a process or quality anomaly, but
> only if detection and material-time boundaries remain trustworthy.
> **Claim status:** active
> **Scope:** Quality-stream containment for `RSK-0002`; not proof that cyber
> compromise was contained or that all affected material was found.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1.6 and 4.1–4.2/4.8, printed pp. 5, 8–10, 12
> (physical pp. 10, 13–15, 17); Annex V §§3.1–3.3, printed pp. 38–41
> (physical pp. 43–46); [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§4.2.2, 6.2.4.5 and 6.4, printed pp. 55, 114–117, 134–137.
> **Basis / limits:** Quality and cyber containment functions are direct;
> applicability and the integrity of the trigger/trace are untested.

> **Claim record — CTL-0015-C04 | analytic-judgment**
> **Claim:** Q13 criteria support quality-stream resumption and disposition
> after diversion, while trusted cyber recovery additionally requires NIST-
> derived restoration and validation of digital state; neither source proves
> the combined recovery succeeded in deployment.
> **Claim status:** active
> **Scope:** Conditional re-entry/recovery edge of `RSK-0002`; `recovers` does
> not mean generic backup or process restart alone is sufficient.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1.6 and 4.2/4.8, printed pp. 5, 8–10, 12
> (physical pp. 10, 13–15, 17); Annex V §§3.2–3.3, printed pp. 39–41
> (physical pp. 44–46); [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§5.3.2, 6.2.4.3–6.2.4.5 and 6.5, printed pp. 79–80, 112–117,
> 137–138.
> **Basis / limits:** Resumption/disposition and trusted-restoration functions
> are separate direct predicates. The combined evidence state remains design.

## Applicability and prerequisites

- A process-specific material/time boundary and justified state-of-control
  model must exist; generic controls cannot invent it.
- Monitoring frequency, latency, sampling and model performance must be fit for
  the process dynamics and intended decision.
- A digital signal must remain associated with the correct material segment,
  equipment state and batch/release record.
- Offline/reference testing and independent quality authority remain necessary
  where PAT/RTRT cannot support an attribute or data are unavailable.
- Response must preserve safe biological/physical state; a cyber-optimal
  disconnect, shutdown or rollback can be unsafe or invalidate product state.
- Recovery must reconcile digital configuration/data and physical material/
  disposition. Backup existence alone proves neither.

## Therapeutic-protein branch

Q13 Annex III adds cell-bank-to-batch traceability, adventitious-agent testing,
single-use/filter integrity, sampling/PAT, online/in-line and conventional
offline release testing, extended-run considerations and viral-clearance
validation. This is a therapeutic-protein drug-substance example, not a full
sterile fill/finish or distribution system.

> **Claim record — CTL-0015-C05 | source-report**
> **Claim:** For therapeutic-protein continuous manufacture, Q13 retains
> biological contamination/integrity and offline-release gates alongside
> automation/PAT rather than treating digital monitoring as sufficient.
> **Claim status:** active
> **Scope:** Annex III normative/illustrative branch; not a named deployment,
> contamination event or measured safeguard performance.
> **As of:** 2022-11-16.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Annex III §§1–3.3, printed pp. 27–30 (physical pp. 32–35).
> **Basis / limits:** Cell-bank, biological-control, PAT/offline-test and
> validation predicates are explicit. The example is not outcome evidence.

## Validation and evidence of effectiveness

Q13 calls for model validation, process validation or justified continuous
verification, monitoring and quantitative acceptance criteria. NIST calls for
assessment, monitoring, response and restoration testing. The source package
contains no named facility, control implementation, baseline/comparator,
metric value, null/failure result or independent evaluator.

> **Claim record — CTL-0015-C06 | analytic-judgment**
> **Claim:** Validation and verification are assurance methods in this family,
> not evidence that `CTL-0015` was implemented, tested successfully, effective
> or independently evaluated.
> **Claim status:** active
> **Scope:** Evidence-state classification for this page; not a finding that no
> external Q13 validation or OT assessment exists.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1.7, 3.3 and 4.3–4.9, printed pp. 5–12
> (physical pp. 10–17); [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§4.3.5–4.3.7 and 6.3.2–6.5, printed pp. 63–65, 128–138.
> **Basis / limits:** Requested methods are direct; transaction-level result
> evidence is absent from both sources.

## Failure modes and tradeoffs

- PAT/data gaps or model drift can hide or distort the quality state.
- Sampling may disturb the process; averaging may mask a short disturbance.
- Incorrect trace/diversion boundaries can leave affected material in stream
  or discard conforming material.
- Frequent individually acceptable disturbances can exceed process capability.
- Automated pause/diversion may fail or create availability and waste costs.
- Offline testing adds delay; RTRT cannot replace unsupported attributes.
- Restoration to a technically running state can leave product quality or
  disposition unresolved.

## Framework mappings

- ICH Q13 Step 4, 2022: continuous-manufacturing quality/control architecture.
- FDA Q13 final Level 1, 2023: nonbinding U.S. regional presentation.
- EMA Q13 Step 5, effective 2023-07-10: adopted EU scientific-guideline
  presentation.
- NIST SP 800-82r3, 2023: generic OT cyber controls and assurance.

The mapping does not establish regional compliance, implementation,
equivalence or effectiveness.

## Related pages

- [SRC-0031 — ICH Q13](../sources/src-0031-ich-q13-continuous-manufacturing.md)
- [GOV-0016 — Q13 governance/adoption](../governance/gov-0016-ich-q13-continuous-manufacturing.md)
- [CTL-0011 — generic OT controls](ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [RSK-0002 — control/data integrity disruption](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [SYS-0002 — process-control stack](../systems/sys-0002-biomanufacturing-process-control.md)
- [WFL-0003 — manufacturing lineage](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
- [AST-0007 — assets/stakeholders](../assets/ast-0007-biomanufacturing-assets-stakeholders.md)
- [SYN-0016 — BMO four-cell reconciliation](../syntheses/syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)

## Sources

- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
