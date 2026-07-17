---
id: CTL-0002
type: control
title: Genomic-data risk management and lifecycle assurance
aliases:
  - genomic data RMF tailoring
  - consent-aware genomic lifecycle assurance
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0006
sensitivity: public
dual_use: low
control_status: recommended
implementation_status: unknown
testing_status: unknown
effectiveness_status: unknown
independent_evaluation_status: unknown
relations:
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: CTL-0002-C01
    evidence:
      - source: SRC-0005
        locator: "§4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24); §4.4, printed pp. 20–22 (PDF pp. 29–31)"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: CTL-0002-C07
    evidence:
      - source: SRC-0006
        locator: "§§3–6, printed pp. 14–31 (PDF pp. 25–42); Tables 4–36, printed pp. 32–166 (PDF pp. 43–177)"
  - predicate: mitigates
    target: RSK-0003
    claim_id: CTL-0002-C02
    evidence:
      - source: SRC-0005
        locator: "§2.1, printed pp. 3–4 (PDF pp. 12–13); Table 1, printed pp. 14–15 (PDF pp. 23–24); §3.5, printed p. 11 (PDF p. 20)"
      - source: SRC-0006
        locator: "§5.1, printed pp. 22–23 (PDF pp. 33–34); Tables 10–12, 15–25 and 33, printed pp. 64–90, 103–140 and 155–158"
  - predicate: mitigates
    target: RSK-0004
    claim_id: CTL-0002-C06
    evidence:
      - source: SRC-0005
        locator: "§§1.1–2.1, printed pp. 1–4 (PDF pp. 10–13); §§3.2 and 3.7, printed pp. 9–12 (PDF pp. 18–21); Table 1, printed pp. 14–15 (PDF pp. 23–24); §5.2, printed pp. 24–25 (PDF pp. 33–34)"
      - source: SRC-0006
        locator: "§§5.2 and 5.4–5.6, printed pp. 23–25 (PDF pp. 34–36); Tables 10, 13, 15 and 26–36"
  - predicate: mitigates
    target: RSK-0005
    claim_id: CTL-0002-C10
    evidence:
      - source: SRC-0005
        locator: "§1.1, printed pp. 1–2 (PDF pp. 10–11); §4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24)"
      - source: SRC-0006
        locator: "§§2.2–2.2.1, printed pp. 9–11 (PDF pp. 20–22); Tables 26 and 32–36, printed pp. 141–166 (PDF pp. 152–177)"
tags:
  - genomic-data
  - risk-management
  - lifecycle-assurance
  - consent-management
  - provenance
  - recommended-control
---

# Genomic-data risk management and lifecycle assurance

> Recommended defensive control family derived from NIST IR 8432's RMF
> tailoring and the integrated CSF 2.0/PF 1.0 **Second Public Draft** in NIST
> IR 8467. Implementation, testing, effectiveness and independent evaluation
> are all **unknown**.

## Objective

Manage cybersecurity and privacy risk across genomic data generation, analysis,
storage, sharing, reinterpretation and decision use. Tailor categorization,
control selection, assurance, monitoring, response and recovery to genomic-data
confidentiality, integrity, availability, provenance, consent and allowed-use
dependencies rather than treating the data as an undifferentiated IT asset.

This page records control objectives, not universal legal duties or a complete
technical baseline.

## Evidence status

| Dimension | Current status | What would change it |
| --- | --- | --- |
| Recommended | Yes — IR 8432 describes RMF tailoring and IR 8467 2pd supplies a draft integrated Community Profile | Final/superseding guidance or stronger source reconciliation |
| Implemented | Unknown | Organization- and system-specific implementation evidence |
| Tested | Unknown | Defined assessment, exercise or validation results |
| Effective | Unknown | Outcome evidence tied to an exact scenario edge |
| Independently evaluated | Unknown | Independent method, scope, findings and limitations |

> **Claim record — CTL-0002-C01 | source-report**
> **Claim:** NIST IR 8432 applies the RMF cycle to genomic data and highlights
> preparation, consent-aware categorization, control selection,
> implementation/assessment/authorization, continuous monitoring, incident
> response and recovery as relevant risk-management activities.
> **Claim status:** active
> **Scope:** Risk-management structure for organizations processing genomic
> data; applicability of legal or programme requirements remains entity- and
> jurisdiction-specific.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24).
> **Basis / limits:** The RMF stages and genomic relevance are explicit.
> NIST IR 8432 does not select a universal control baseline, report a completed
> authorization or evaluate an organization's implementation outcomes.

### Integrated draft Community Profile

IR 8467 2pd turns the earlier cybersecurity-profile work and planned privacy
profile into one CSF 2.0/PF 1.0 matrix organized by 12 Mission Objectives. It
is a tailoring start point: organizations select relevant objectives, develop
Current and Target Profiles and perform their own gap analysis.

> **Claim record — CTL-0002-C07 | source-report**
> **Claim:** NIST IR 8467 2pd provides an integrated CSF 2.0/PF 1.0 Community
> Profile with 12 genomic Mission Objectives and context-tailorable priorities
> for 106 CSF and 100 PF outcomes.
> **Claim status:** active
> **Scope:** Second Public Draft target-state guidance; not a universal
> baseline, compliance profile, implementation or effectiveness result.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§3–6, printed pp. 14–31 (PDF pp. 25–42); Tables 3–36,
> printed pp. 22–166 (PDF pp. 33–177); official spreadsheet.
> **Basis / limits:** Versions, objectives, counts and tailoring use are direct.
> Priorities `1/2/3` mean High/Moderate/Other, not risk or effectiveness;
> `Other` is not low. Implementation Tiers are excluded, the CSF↔PF alignment
> is draft, and no organization-specific results are reported.

## Control functions

| Function | Safe high-level objective | Evidence boundary |
| --- | --- | --- |
| Prepare and govern | Identify lifecycle scope, accountable roles, stakeholders, applicable requirements and risk tolerance | Does not establish that the inventory or authority model is complete |
| Categorize | Classify data/system impact and preserve consent, allowed-use and provenance context needed for decisions | Categorization does not prove that handling matches consent or law |
| Select and protect | Choose proportionate safeguards for generation, analysis, storage, sharing and decision dependencies | No product, protocol or configuration is prescribed |
| Implement, assess and authorize | Document implementation and verify that selected controls are present, operate as intended and support an explicit residual-risk decision | A framework mapping or self-attestation is not a test result |
| Monitor and detect | Reassess threats, vulnerabilities, lifecycle changes and integrity/provenance or consent discrepancies | No detection rate, coverage or monitoring deployment is established |
| Respond and recover | Contain suspect state, coordinate affected decisions, restore trustworthy data/system state and reassess dependent outputs | Backup or restoration alone does not prove decision-safe recovery |

## Scenario edges addressed

For
[RSK-0003](../risk-scenarios/rsk-0003-genomic-data-integrity-decision-harm.md), the
control family conditionally addresses four exact edges:

1. **origin:** identify and assess integrity/provenance risk in genomic data and
   analysis dependencies;
2. **lifecycle transfer:** maintain context and validate state as data move
   through generation, analysis, storage, sharing or reinterpretation;
3. **decision transfer:** require appropriate assessment and authorization
   before a consequential research, clinical or production decision relies on
   the output;
4. **downstream containment/recovery:** isolate suspect state, reassess affected
   outputs and restore a trustworthy basis for further decisions.

> **Claim record — CTL-0002-C02 | analytic-judgment**
> **Claim:** `CTL-0002` conditionally mitigates the origin, lifecycle-transfer,
> decision-transfer and recovery edges of `RSK-0003`; current evidence does not
> establish implementation, test coverage or effectiveness for any edge.
> **Claim status:** active
> **Scope:** Genomic-data workflows with a documented digital-to-decision
> dependency; no named deployment.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §2.1, printed pp. 3–4 (PDF pp. 12–13); Table 1, printed
> pp. 14–15 (PDF pp. 23–24); §3.5, printed p. 11
> (PDF p. 20);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §5.1, printed pp. 22–23 (PDF pp. 33–34); Tables 10–12,
> 15–25 and 33.
> **Basis / limits:** The source supplies lifecycle dependencies, RMF assurance
> functions and possible decision consequences; the later draft adds inventory,
> logging, assessment and recovery outcomes. The sources share programme
> lineage. The exact-edge mapping is a wiki inference; no organization-specific
> control evidence closes the path.

For
[RSK-0004](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md), the
same family conditionally addresses data/purpose inventory, consent-aware
categorization, authorized sharing, privacy-risk assessment, discrepancy
monitoring and response. Those objectives can reduce an exposure or
authorized-use failure, but they cannot make genomic data anonymous or reverse
information already learned by an unauthorized recipient.

> **Claim record — CTL-0002-C06 | analytic-judgment**
> **Claim:** `CTL-0002` conditionally mitigates the access-authorization,
> disclosure and post-disclosure-use edges of `RSK-0004` through consent-aware
> categorization, proportionate access/sharing controls, assessment and
> monitoring; implementation and effectiveness remain unknown.
> **Claim status:** active
> **Scope:** Human genomic-data processing in a defined organizational and
> consent context, not a universal guarantee against re-identification.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§1.1–2.1, printed pp. 1–4 (PDF pp. 10–13); §§3.2 and 3.7,
> printed pp. 9–12 (PDF pp. 18–21); Table 1, printed pp. 14–15
> (PDF pp. 23–24); §5.2, printed pp. 24–25 (PDF pp. 33–34);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§5.2 and 5.4–5.6, printed pp. 23–25 (PDF pp. 34–36);
> Tables 10, 13, 15 and 26–36.
> **Basis / limits:** The source supplies privacy/consent dependencies and
> risk-management functions; the later draft adds purpose/data-action
> inventories, consent/permission, disclosure-record and communication
> outcomes. The exact-edge mapping is an inference. Neither reports deployment,
> disclosure outcome or measured residual risk.

For
[RSK-0005](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md),
the family addresses a different edge: technical authorization is not treated
as sufficient privacy assurance. Desired outcomes inventory processing
purposes/actions and affected people, align consent/preferences/minimization,
monitor problematic actions, communicate with individuals and test privacy
measures.

> **Claim record — CTL-0002-C10 | analytic-judgment**
> **Claim:** `CTL-0002` conditionally mitigates the processing-to-privacy-
> problem and privacy-problem-to-impact edges of `RSK-0005` through purpose and
> action inventories, consent/preference management, minimization, review,
> communication and assurance; implementation and effectiveness are unknown.
> **Claim status:** active
> **Scope:** Human genomic-data processing in a defined purpose, consent and
> organizational context; not a claim that technically permitted processing is
> always lawful, ethical or harmless.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §1.1, printed pp. 1–2 (PDF pp. 10–11); §4.1 and Table 1,
> printed pp. 13–15 (PDF pp. 22–24);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§2.2–2.2.1, printed pp. 9–11 (PDF pp. 20–22); Tables 26 and
> 32–36, printed pp. 141–166 (PDF pp. 152–177).
> **Basis / limits:** The sources distinguish cybersecurity and privacy and
> provide relevant management outcomes. They share NIST/NCCoE lineage; the
> exact-edge mapping is a wiki inference and no deployed safeguard or measured
> privacy outcome is reported.

## Applicability and prerequisites

The family applies where genomic data or associated context materially informs
research, clinical, manufacturing, agricultural or access decisions.
Prerequisites include:

- a bounded genomic-data lifecycle and accountable owners;
- inventory of relevant data, provenance, consent/allowed-use context, systems
  and decision dependencies;
- organization-specific risk tolerance and authorization authority;
- applicable legal, contractual, research and data-provider requirements;
- validation criteria for data, pipeline changes and consequential outputs;
- incident, continuity and recovery coordination across data, system and
  decision owners.

## Dependencies

- [AST-0001](../assets/ast-0001-genomic-data.md) defines the protected data and
  context classes.
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) defines
  the relevant generation, analysis, storage and exchange system classes.
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) identifies lifecycle
  stages and trust boundaries where assurance must be scoped.
- Applicable law, consent terms and programme rules must be verified from their
  own current primary sources; neither NIST report is a substitute.

## Implementation considerations

Tailoring should preserve both security and legitimate data use. Controls need
to follow the data and its decision context across organizational boundaries,
define who can accept residual risk, and distinguish restoration of bytes or
service from restoration of trustworthy provenance and decision fitness.

The report's federal, NIH and informed-consent examples are context-specific.
They must not be generalized into universal legal requirements.

## Candidate adjuncts, not control evidence

NIST IR 8432 records six stakeholder-informed solution opportunities with
different maturity labels:

- a June 2023 Initial Public Draft genomic Cybersecurity Framework Profile and
  a Privacy Framework Profile that the report describes as planned;
- notional MUD-based sequencer micro-segmentation;
- tailored pipeline/sequencer security guidelines and SBOM expectations;
- a genomic RMF demonstration using vendor-proposed solutions;
- privacy-enhancing and federated-analysis demonstrations.

These can inform later tailoring, but publication of an Initial Public Draft is
not implementation evidence, the privacy Profile was not yet published in the
report, and the remaining use cases simulate real-life challenges with ideas or
expected benefits. Generic-IoT MUD work is not a tested sequencer deployment;
vendor mappings are not compliance or effectiveness evidence; and
privacy-enhancing technologies are expressly not complete or general solutions.

IR 8467 2pd is the documented follow-on for the first two profile items: the
cybersecurity and privacy outcomes now appear in one integrated draft using
CSF 2.0 and PF 1.0. This is material progress in specificity, but a draft
profile remains guidance rather than deployment or assurance evidence.

> **Claim record — CTL-0002-C03 | source-report**
> **Claim:** Chapter 5 records an Initial Public Draft cybersecurity Profile,
> a planned privacy Profile, and sequencer MUD, security-guideline, RMF and
> privacy-enhancing-technology solution or demonstration ideas; none is shown
> by this report to be implemented, tested or effective in a genomic deployment.
> **Claim status:** active
> **Scope:** Evidence classification of the six IR 8432 solution opportunities.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> Abstract, printed p. i (PDF p. 4); §1.2, printed p. 2
> (PDF p. 11); §§5.1–5.6, printed pp. 23–31
> (PDF pp. 32–40); §6, printed p. 32 (PDF p. 41).
> **Basis / limits:** The source distinguishes an existing Initial Public Draft
> from a planned profile and proposed/candidate demonstrations. Existence of a
> draft, framework, product or prior generic model does not demonstrate this
> genomic control family.

## Failure modes and tradeoffs

- incomplete lifecycle inventory can leave decision dependencies outside scope;
- consent or provenance context can be lost when data are aggregated or moved;
- a framework profile or control mapping can become checklist evidence without
  verification of operation or outcomes;
- restrictive controls can impede legitimate research, care or data sharing;
- monitoring can create additional privacy and governance risk;
- unvalidated changes or recovery can preserve or restore an unreliable state;
- privacy-enhancing methods may have analysis, accuracy, performance or scope
  limits and require complementary controls.

These are conditions to assess locally, not findings about a named deployment.

## Validation and evidence of effectiveness

Validation should be defined against the exact lifecycle and scenario edge. At
a high level, useful evidence would include:

- traceable control implementation records and accountable authorization;
- validation of data/provenance and pipeline changes before consequential use;
- assessment results showing controls operate as intended;
- monitoring and discrepancy-response coverage for defined dependencies;
- exercises demonstrating trustworthy recovery and reassessment of dependent
  outputs or decisions;
- independent evaluation with stated scope, method and limitations.

NIST IR 8432 describes the need for implementation, assessment, authorization,
monitoring, response and recovery. IR 8467 adds desired assessments, exercises,
supplier evidence, backup integrity and restored-state verification. Neither
supplies those results for `CTL-0002`.

> **Claim record — CTL-0002-C04 | artifact-observation**
> **Claim:** Chapter 5 contains internally inconsistent reference numbers,
> including citations for SP 1800-15, CIS Benchmarks, NISTIR 8259, SBOM and
> federated homomorphic encryption that do not match the corresponding
> bibliography entries.
> **Claim status:** active
> **Scope:** Internal citation integrity of the preserved NIST IR 8432 PDF;
> underlying external sources were not revalidated for this claim.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§5.3–5.4, printed pp. 25–27 (PDF pp. 34–36), compared
> with References [61]–[62] and [72]–[78], printed pp. 39–40
> (PDF pp. 48–49); §5.6, printed p. 30 (PDF p. 39), compared
> with References [87]–[88], printed p. 41 (PDF p. 50).
> **Basis / limits:** Direct body-to-bibliography comparison shows the mismatch;
> for example, body citation [87] accompanies federated homomorphic encryption,
> while bibliography [87] is an unrelated blockchain report and the matching
> paper is [88]. Intended references must be inspected before treating
> “demonstrated” or “proven” language as independent corroboration.

> **Claim record — CTL-0002-C05 | analytic-judgment**
> **Claim:** The current corpus supports `recommended` status for `CTL-0002`,
> while implementation, testing, effectiveness and independent evaluation all
> remain unknown.
> **Claim status:** active
> **Scope:** Wiki evidence classification after ingest of `SRC-0005` and
> `SRC-0006`.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §4.1 and Table 1, printed pp. 13–15 (PDF pp. 22–24);
> §§5.1–5.6, printed pp. 23–31 (PDF pp. 32–40); source
> methods and limitations;
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§3–6 and Tables 3–36, printed pp. 14–166 (PDF pp. 25–177).
> **Basis / limits:** The report provides a risk-management structure and
> the later draft provides a detailed target profile, but the sources share
> programme lineage and provide no deployment sample, completed control
> assessment, measured outcome or independent evaluation for this page's
> control family.

## Framework mappings

The versioned draft crosswalk can be used at this safe functional level:

| CTL function | IR 8467 outcome groups | PDF locator |
| --- | --- | --- |
| Scope, dependencies and requirements | `GV.OC`, `GV.RM`, `GV.RR`, `GV.PO`, `GV.OV` | Tables 4–8, printed pp. 32–56 |
| Third parties and supply chain | `GV.SC` | Table 9, printed pp. 57–63 |
| Inventory, flows and lifecycle | `ID.AM` plus PF inventory/mapping | Tables 10 and 26, printed pp. 64–77, 141–142 |
| Risk, change and improvement | `ID.RA`, `ID.IM` plus PF risk/ecosystem outcomes | Tables 11–12 and 28–31, printed pp. 78–90, 144–151 |
| Access, awareness and data protection | `PR.AA`, `PR.AT`, `PR.DS` plus aligned PF outcomes | Tables 13–15, printed pp. 91–108 |
| Platform and infrastructure resilience | `PR.PS`, `PR.IR` | Tables 16–17, printed pp. 109–120 |
| Detection and analysis | `DE.CM`, `DE.AE` | Tables 18–19, printed pp. 121–126 |
| Response and recovery | `RS.MA`, `RS.AN`, `RS.CO`, `RS.MI`, `RC.RP`, `RC.CO` | Tables 20–25, printed pp. 127–140 |
| Privacy processing and communication | PF `CT.PO`, `CT.DM`, `CT.DP`, `CM.PO`, `CM.AW` | Tables 32–36, printed pp. 152–166 |

> **Claim record — CTL-0002-C08 | source-report**
> **Claim:** IR 8467 maps governance through recovery and privacy-processing
> outcomes to each Mission Objective, but those mappings express recommended
> priority and rationale rather than implementation or assurance status.
> **Claim status:** active
> **Scope:** Versioned CSF 2.0/PF 1.0 functional map in the Second Public Draft.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §6 and Tables 4–36, printed pp. 29–166 (PDF pp. 40–177);
> official tailoring spreadsheet.
> **Basis / limits:** All 206 unique outcomes and priority cells were checked.
> The crosswalk is draft and one spreadsheet summary row mislabels
> `GV.OC-03` as `GV.OV-03`; canonical integrated rows and PDF tables take
> precedence. Primary framework publications must be separately ingested before
> claiming current compliance, exact legal applicability or framework
> equivalence.

## Related pages

- [CTL-0003 — Genomic-data privacy threat modeling](ctl-0003-genomic-data-privacy-threat-modeling.md) — example-applied assessment process that can feed candidate control selection; it does not establish this family's implementation or effectiveness.
- [CTL-0007 — Secure sequencing input processing](ctl-0007-secure-sequencing-input-processing.md) — independent USENIX-derived reverse-path and cross-sample control family; recommended only.
- [CTL-0008 — Part 202 transaction controls](ctl-0008-restricted-data-transaction-controls.md) — binding only for applicable Part 202 transaction branches; the NIST profile is not a compliance substitute or an implementation result.
- [CTL-0009 — EHDS health-data and EHR safeguards](ctl-0009-ehds-health-data-and-ehr-safeguards.md) — staged EU legal-design layer for covered health-data/EHR branches; no deployment or effectiveness inference.
- [SYN-0003 — Cross-domain transfer directions](../syntheses/syn-0003-cross-domain-transfer-directions.md) — reconciles exact direction/mechanism and evidence maturity.
- [SYN-0006 — Official control function/state taxonomy](../syntheses/syn-0006-official-control-function-state-taxonomy.md) — preserves NIST draft outcomes as recommended/design evidence and separates higher assurance states.
- [SYN-0007 — Cross-sector exact control-edge portfolio](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)
- [RSK-0003 — Compromised genomic-data integrity and provenance with downstream decision harm](../risk-scenarios/rsk-0003-genomic-data-integrity-decision-harm.md)
- [RSK-0004 — Disclosure of human genomic data and kin privacy harm](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md)
- [RSK-0005 — Privacy harm from technically authorized genomic-data processing](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md)
- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [SYS-0003 — Genomic sequencing and analysis ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [WFL-0005 — Genomic data lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SRC-0005 — NIST IR 8432 Cybersecurity of Genomic Data](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0006 — NIST IR 8467 2pd](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)

## Sources

- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
  §§2.1, 4.1, 4.4 and 5–6; Table 1; printed pp. 3–4, 13–15,
  20–32 (PDF pp. 12–13, 22–24, 29–41).
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
  §§1–6; Tables 3–36; official tailoring spreadsheet.
