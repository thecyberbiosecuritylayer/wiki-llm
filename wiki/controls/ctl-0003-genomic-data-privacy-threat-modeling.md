---
id: CTL-0003
type: control
title: Genomic-data privacy threat modeling
aliases:
  - privacy threat modeling for genomic-data processing
  - Four Question genomic privacy assessment
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0007
sensitivity: public
dual_use: low
control_status: recommended
implementation_status: example-applied
testing_status: unknown
effectiveness_status: unknown
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0007
    claim_id: CTL-0003-C01
    evidence:
      - source: SRC-0007
        locator: "Volume C Summary and §§2.1–2.4, printed pp. 1 and 7–43 (PDF pp. 10 and 16–52); static Appendix D"
  - predicate: depends-on
    target: WFL-0005
    claim_id: CTL-0003-C02
    evidence:
      - source: SRC-0007
        locator: "Volume C §1.2 and Figure 1, printed pp. 2–3 (PDF pp. 11–12); §§2.1 and 2.1.4, printed pp. 7–19 (PDF pp. 16–28); static Appendix E"
  - predicate: depends-on
    target: SYS-0003
    claim_id: CTL-0003-C02
    evidence:
      - source: SRC-0007
        locator: "Volume C §§2.1.2–2.1.4, printed pp. 8–19 (PDF pp. 17–28); static Appendix E"
  - predicate: enables
    target: CTL-0002
    claim_id: CTL-0003-C04
    evidence:
      - source: SRC-0007
        locator: "Volume C §§2.3.2–2.4.4 and Table 21, printed pp. 35–43 (PDF pp. 44–52); static Appendices C–D"
tags:
  - genomic-data
  - privacy
  - threat-modeling
  - assessment
  - assurance
  - example-applied
---

# Genomic-data privacy threat modeling

> Reusable assessment control for bounding a genomic-data processing
> environment, mapping its physical and digital data actions, identifying
> possible privacy threats and selecting candidate responses. NIST applied the
> method in a bounded example, but did not test the method's accuracy or show
> that selected safeguards reduced privacy harm.

## Objective

Create a traceable, data-subject-centered privacy threat model before or during
system change and periodically revisit it as processing, stakeholders and
threat context change. The control should make assumptions, data actions,
responsibility boundaries, possible threats, response decisions and residual
uncertainty reviewable rather than treating technical authorization or a
generic control catalog as sufficient privacy assurance.

This is an **assessment and decision-support control**. It can enable selection
and assurance of safeguards, but its execution alone does not prevent,
detect, contain or recover from a privacy event.

## Evidence status

| Dimension | Current status | Meaning |
| --- | --- | --- |
| Recommended | Yes | SP 1800-43C presents the method for local adaptation |
| Implemented | **Example-applied** | The authors completed the method against bounded sample environments and report a reference-material workflow exercise |
| Tested | Unknown | No sensitivity, completeness, repeatability, inter-rater or outcome test is reported |
| Effective | Unknown | No comparison shows that using the method reduced incidents, missed threats or privacy harm |
| Independently evaluated | Unknown | Evidence is from the method's NIST/NCCoE authors and partners |

> **Claim record — CTL-0003-C01 | source-report**
> **Claim:** NIST SP 1800-43C demonstrates an iterative Four Question privacy
> threat-modeling method using adapted PRAM worksheets, contextual mappings,
> dataflow diagrams, LINDDUN, PANOPTIC, response selection and review.
> **Claim status:** active
> **Scope:** Example method for clinical/research genomic-data processing
> environments; not a universal baseline or mandatory practice.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> Volume C Summary, printed p. 1 (PDF p. 10); §§2.1–2.4, printed pp. 7–43
> (PDF pp. 16–52); static Appendix D.
> **Basis / limits:** The process and example outputs are direct. The draft
> reports no comparison group, accuracy measure, incident reduction or
> independent evaluation.

## Control workflow

1. **Bound the target.** Define organization-specific system and lifecycle
   boundaries, use cases, responsible entities, data subjects, mission/privacy
   objectives and assumptions.
2. **Document data actions.** Model components and material/digital flows at a
   defensible level, including collection, generation or transformation,
   retention/logging, disclosure/transfer and disposal.
3. **Identify possibilities.** Apply privacy threat categories per flow and
   build contextual attack-scenario groupings from the data subject's
   perspective.
4. **Screen and order.** Cross-check model entries against a second taxonomy
   and relevant privacy engineering objectives; document subjective
   feasibility/difficulty judgments rather than calling the result likelihood.
5. **Choose and trace responses.** Eliminate, disrupt, transfer or accept each
   prioritized threat under an accountable decision; trace candidate
   disruptions to relevant framework outcomes and controls.
6. **Review and iterate.** Revisit scope, assumptions, threats, responses and
   residual risk after system, purpose, stakeholder or threat changes and use
   defined testing where appropriate.

The wiki intentionally omits the source's detailed attack paths and operational
topology. Local teams need enough detail to evaluate their own system without
turning a public synthesis into an exploit guide.

## Applicability and prerequisites

The method is applicable where human genomic data or derived information moves
through multiple components, processors or organizations and ordinary system
operation can affect predictability, manageability or disassociability.
Prerequisites include:

- a bounded [lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md) and named
  processing purposes;
- a current [system](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
  inventory and accountable owners;
- identified direct and indirect data subjects and applicable consent,
  programme, contractual and legal context;
- access to the people who understand actual data and material handoffs;
- an authority able to select, accept, fund and revisit responses;
- criteria for verifying whether selected safeguards were implemented and
  whether residual privacy objectives are met.

> **Claim record — CTL-0003-C02 | source-report**
> **Claim:** The method depends on locally documenting organizational context,
> system components, managing entities and physical/digital dataflows before
> generating or prioritizing privacy threats.
> **Claim status:** active
> **Scope:** Prerequisites demonstrated by the SP 1800-43C example, not proof
> that the source's architecture represents other organizations.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> Volume C §§2.1–2.1.4, printed pp. 7–19 (PDF pp. 16–28); static Appendix E.
> **Basis / limits:** The documented inputs and dependencies are direct. The
> diagrams cover a bounded example and do not validate identity, custody,
> consent propagation, network exposure or control state.

## Scenario edges addressed

The method can expose candidate edges in both
[RSK-0004](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md) and
[RSK-0005](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md):

- where physical or digital information crosses a responsibility boundary;
- where data are linked, identified, disclosed, retained or reused;
- where notice, consent, preference or individual intervention may be absent;
- where an ordinary data action can undermine a privacy engineering objective;
- where a response decision and later assurance activity need an owner.

It does **not** itself mitigate those edges. A direct `mitigates` relation would
overstate the evidence; only a selected, implemented and appropriately tested
safeguard can support such a claim.

> **Claim record — CTL-0003-C03 | analytic-judgment**
> **Claim:** The source's taxonomy cross-checking and numeric ordering improve
> traceability of the example but do not establish completeness, likelihood,
> severity, repeatability, implementation or effectiveness.
> **Claim status:** active
> **Scope:** Assurance interpretation of the method as demonstrated.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> Volume C §§2.2.3–2.4, printed pp. 28–43 (PDF pp. 37–52); Tables 15–21;
> static Appendices F–G.
> **Basis / limits:** The source explicitly uses analyst-set categorical and
> weighted values for ranking and reserves implementation/testing for later
> review. No empirical validation design or result is reported.

## Dependencies

- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) provides the lifecycle
  scope and candidate material/data handoffs.
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) provides
  the functional component and responsibility classes.
- [AST-0001](../assets/ast-0001-genomic-data.md) provides the protected data,
  derivation and kin/consent context.
- [CTL-0002](ctl-0002-genomic-data-risk-management.md) provides the
  broader control-selection, implementation, assessment, response and recovery
  cycle into which threat-model outputs can feed.

> **Claim record — CTL-0003-C04 | source-report**
> **Claim:** The demonstrated method can feed broader genomic-data risk
> management by tracing selected privacy threat actions through Privacy
> Framework outcomes and Genomic Data Profile priorities to candidate
> SP 800-53 controls.
> **Claim status:** active
> **Scope:** Control discovery and prioritization input, not proof that the
> candidate control is applicable, implemented or effective.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> Volume C §2.3.2 and Table 21, printed pp. 35–38 (PDF pp. 44–47); §2.4,
> printed pp. 38–43 (PDF pp. 47–52); static Appendices C–D.
> **Basis / limits:** The mapping path and illustrative selection are direct.
> Framework alignment is decision support; no safeguard implementation or
> outcome is reported.

## Implementation considerations

- Use the organization's actual purposes, people, data states and boundaries;
  copying the sample diagrams would create false assurance.
- Keep cybersecurity and privacy related but distinct. A system may be secure
  against unauthorized access and still create an unacceptable privacy action
  while operating as designed.
- Preserve links from each modeled threat to source/flow/destination,
  assumptions, affected people, objectives, decision owner and chosen response.
- Treat ranking values as explainable ordering aids, not calibrated risk or
  likelihood. Record disagreement and sensitivity to changed weights.
- Separate a response proposal from selection, implementation, testing and
  effectiveness; update those states only from corresponding evidence.
- Avoid collecting unnecessary personal or operational detail merely to
  populate a threat model; the assessment can itself create privacy or security
  risk.

## Failure modes and tradeoffs

- an incomplete boundary or stale diagram can systematically omit threats;
- taxonomy mappings can create a false sense of coverage;
- analyst-set rankings can conceal disagreement or unsupported assumptions;
- a component-focused model can miss downstream human, governance or decision
  consequences unless connected to risk analysis;
- selected catalog controls may not fit the actual threat action or local
  architecture;
- detailed models can become sensitive operational artifacts and need access,
  retention and sharing controls;
- repeated assessment without accountable implementation can produce
  documentation rather than risk reduction.

## Validation and evidence of effectiveness

The current evidence supports only **example application**. A stronger
evaluation would predefine and report:

- scope/diagram completeness checks against independent system records;
- analyst agreement and reproducibility across teams;
- seeded or independently derived threats and resulting miss/duplicate rates;
- traceability from selected response to deployed safeguard and exact scenario
  edge;
- verification that the safeguard operates as intended;
- privacy or operational outcome measures, side effects and residual risk;
- independent review with disclosed method, environment and limitations.

Exercises, red teaming and continuous review suggested in Question 4 are
future validation options, not results from `SRC-0007`.

## Framework mappings

`SRC-0007` connects threat actions to NIST Privacy Framework outcomes,
Mission Objective priorities from IR 8467 and candidate SP 800-53 Rev. 5
controls. This page deliberately does not reproduce the complete mapping as a
universal baseline: organizations must verify source versions, scope and local
applicability.

## Related pages

- [CTL-0002 — Genomic-data risk management and lifecycle assurance](ctl-0002-genomic-data-risk-management.md)
- [WFL-0005 — Genomic data lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003 — Genomic sequencing and analysis ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [RSK-0004 — Genomic-data disclosure and kin privacy harm](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md)
- [RSK-0005 — Technically authorized processing and genomic privacy harm](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md)
- [SRC-0007 — NIST SP 1800-43 A/C](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md)

## Sources

- [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
  Volume C Summary and §§1–3; Figures 1–4; Tables 1–21; static Appendices C–G.
