---
id: RSK-0003
type: risk-scenario
title: Compromised genomic-data integrity and provenance with downstream decision harm
aliases:
  - genomic data integrity decision harm
  - genomic provenance failure scenario
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0006
sensitivity: public
dual_use: moderate
origin_domain: digital
destination_domains:
  - digital
  - biological
  - clinical
  - physical
relations:
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: RSK-0003-C01
    evidence:
      - source: SRC-0005
        locator: "§§1.1–1.2, printed pp. 1–2 (PDF pp. 10–11); §2.1, printed pp. 3–4 (PDF pp. 12–13); §§3.1 and 3.3–3.5, printed pp. 9–11 (PDF pp. 18–20)"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: RSK-0003-C04
    evidence:
      - source: SRC-0006
        locator: "§5.1, printed pp. 22–23 (PDF pp. 33–34); Tables 10–12, 15–25 and 33, printed pp. 64–90, 103–140 and 155–158"
  - predicate: depends-on
    target: AST-0001
    claim_id: RSK-0003-C01
    evidence:
      - source: SRC-0005
        locator: "§2.1, printed pp. 3–4 (PDF pp. 12–13); §3.2, printed pp. 9–10 (PDF pp. 18–19)"
  - predicate: depends-on
    target: SYS-0003
    claim_id: RSK-0003-C01
    evidence:
      - source: SRC-0005
        locator: "§§2.1–2.3, printed pp. 3–5 (PDF pp. 12–14); §4.4.2, printed pp. 20–22 (PDF pp. 29–31)"
  - predicate: affects
    target: WFL-0005
    claim_id: RSK-0003-C03
    evidence:
      - source: SRC-0005
        locator: "§2.1, printed pp. 3–4 (PDF pp. 12–13); §§3.3–3.5, printed pp. 10–11 (PDF pp. 19–20)"
tags:
  - genomic-data
  - data-integrity
  - provenance
  - decision-integrity
  - hypothetical
---

# Compromised genomic-data integrity and provenance with downstream decision harm

> [!WARNING]
> **Evidence classification**
> This is a **hypothetical, single-programme-lineage scenario**. `SRC-0005`
> describes risk classes, while draft `SRC-0006` adds desired control outcomes;
> they do not provide an end-to-end incident, actor, access path, evaluated
> likelihood, or tested propagation.

## Scenario

Genomic data, provenance metadata or an analysis result loses integrity during
generation, analysis, storage, sharing or integration into a research or
clinical decision. If the affected state remains trusted and independent
validation does not stop propagation, a downstream decision may rely on invalid
or contextually misapplied evidence. Conditional consequences include invalid
research, inappropriate clinical interpretation and disruption or uncertainty
in biopharmaceutical, biomanufacturing or agricultural activity.

The scenario does not prescribe a technique and does not assert that every
genomic workflow has a direct cyber-to-biological dependency.

## Assets and workflow

- [AST-0001](../assets/ast-0001-genomic-data.md) — genomic data, analysis outputs,
  provenance, consent/allowed-use context and related records;
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) —
  sequencing, analysis, storage and exchange system classes;
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) — data generation,
  analysis, storage, sharing, reinterpretation and decision use;
- research findings, clinical interpretations, manufacturing decisions and
  agricultural outputs as conditional receiving states.

## Preconditions and trust boundaries

The path requires all of the following:

1. a material integrity or provenance dependency in the receiving analysis or
   decision;
2. an unreliable data, metadata or analysis state that passes a lifecycle or
   organizational trust boundary;
3. absent, ineffective or bypassed validation, comparison, review or decision
   hold before downstream use;
4. reliance on the affected output sufficient to alter research, clinical or
   production activity.

`SRC-0005` does not identify a required actor, access route, exploitable
component, named facility, prevalence or probability for this complete path.

## Origin-domain state

The origin state is digitally stored genomic information, provenance or an
analysis result that is unreliable, corrupted, overwritten or no longer
traceable to the expected source and processing context. Trigger and intent are
unknown. Accidental failure and malicious action are not distinguished without
additional evidence.

> **Claim record — RSK-0003-C01 | analytic-judgment**
> **Claim:** `SRC-0005` supports a structurally plausible integrity/provenance
> path across genomic data generation, analysis, storage and downstream use,
> but does not establish an observed end-to-end incident, actor, access method
> or likelihood.
> **Claim status:** active
> **Scope:** Genomic-data workflows with a material dependency between trusted
> digital state and a research, clinical, manufacturing or agricultural
> decision.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§1.1–1.2, printed pp. 1–2 (PDF pp. 10–11); §2.1, printed
> pp. 3–4 (PDF pp. 12–13); §§3.1 and 3.3–3.5, printed
> pp. 9–11 (PDF pp. 18–20).
> **Basis / limits:** The report links genomic-data integrity and lifecycle
> dependencies to possible decision and sector consequences. Its use cases are
> simulations and its concerns combine workshop input with literature; no
> complete path is observed or tested.

## Cross-domain transfer

The modeled transfer is defensive and high-level:

- **data/provenance transfer:** an unreliable genomic record or analysis output
  is stored, shared, aggregated or reinterpreted as if trustworthy;
- **decision transfer:** a research, clinical or production decision uses that
  output without sufficient independent validation;
- **conditional cyber-to-biological/physical transfer:** the decision changes,
  delays or invalidates work involving patients, biological production or
  agricultural activity.

No sequence content, manipulation method, access path or operational production
parameter is needed to describe these edges.

## Receiving-domain state

The immediate receiving state is an analysis, record or decision whose
integrity, provenance or fitness for use is uncertain. A downstream biological,
clinical or physical consequence exists only if the decision is acted upon and
independent safeguards fail to detect or contain the discrepancy.

- In a research setting, reliance may delay work or leave findings unreliable.
- In a clinical setting, an affected interpretation would have to reach and
  influence a care decision before a clinical state can change.
- In a manufacturing or agricultural setting, an affected genomic output would
  have to influence a production decision before a biological or physical state
  can change or operations become disrupted.

These destination states explain the conditional frontmatter domains; the
source does not show that any one path occurred or that all environments share
the same coupling.

## Immediate and downstream consequences

> **Claim record — RSK-0003-C02 | source-report**
> **Claim:** NIST IR 8432 identifies potential integrity-related consequences
> that include delay or disruption of research, harm to genomic or precision-
> medicine capability, and disruption of biopharmaceutical,
> biomanufacturing or agricultural activity.
> **Claim status:** active
> **Scope:** Potential consequence classes in a stakeholder-informed report,
> not one observed event or a quantified impact model.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §1.1, printed pp. 1–2 (PDF pp. 10–11); §§3.1 and 3.3,
> printed pp. 9–10 (PDF pp. 18–19); §§3.4–3.5, printed p. 11
> (PDF p. 20).
> **Basis / limits:** The consequence categories are explicit, but likelihood,
> frequency, causal sufficiency, magnitude and safeguard failure are not
> evaluated. Potential harmful production discussed elsewhere in §3.1 remains
> speculative and is not treated as an incident.

> **Claim record — RSK-0003-C03 | analytic-judgment**
> **Claim:** Integrity or provenance loss can conditionally affect `WFL-0005`
> when an unreliable output crosses from generation or analysis into storage,
> sharing, EHR/research use or another decision gate; propagation stops if the
> discrepancy is detected, rejected or safely recovered before reliance.
> **Claim status:** active
> **Scope:** High-level lifecycle and decision edge; no named pipeline or
> facility implementation.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §2.1, printed pp. 3–4 (PDF pp. 12–13); §§3.3–3.5,
> printed pp. 10–11 (PDF pp. 19–20); §4.4.2, printed
> pp. 20–22 (PDF pp. 29–31).
> **Basis / limits:** The report supports the lifecycle stages, integrity
> concern and possible decision harms. The exact transfer duration, validation
> coverage and downstream reliance are environment-specific and unverified.

## Evidence

The source states broadly that cyberattacks have occurred against genomic
databases, organizations, instruments and tools, while separately describing
other attack scenarios as proposed (printed pp. 7–8; PDF pp. 16–17). It does
not provide the primary records needed to connect any named event to the full
`RSK-0003` path. No `INC` inference is made.

IR 8467 2pd designates provenance and data quality as Mission Objective 1 and
adds defensive interruption points, but it is a draft outcome profile from the
same NIST/NCCoE lineage, not independent corroboration of the risk path.

> **Claim record — RSK-0003-C04 | source-report**
> **Claim:** IR 8467 2pd recommends provenance/data-quality outcomes including
> data, metadata and dependency inventories, flow mapping,
> change/authenticity assessment, logging, exercises, backup integrity and
> restored-state verification.
> **Claim status:** active
> **Scope:** Defensive outcomes applicable to `RSK-0003`; not evidence that the
> scenario occurred or that any outcome is deployed or effective.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §5.1, printed pp. 22–23 (PDF pp. 33–34); Tables 10–12,
> 15–25 and 33, printed pp. 64–90, 103–140 and 155–158.
> **Basis / limits:** Outcomes and rationales are explicit recommendations;
> their placement as candidate interruption points on this page is a wiki
> mapping. Priority values do not measure scenario risk reduction, and the source
> supplies no implementation, test result, incident path or residual-risk
> measurement.

Evidence that would materially change confidence includes a primary incident or
technical record with traceable integrity failure, verified lifecycle transfer,
documented decision reliance and a measured consequence; or independent
validation showing that a relevant safeguard reliably interrupts an exact edge.

## Controls by function

[CTL-0002](../controls/ctl-0002-genomic-data-risk-management.md) conditionally maps
to the scenario as follows:

- **identify/categorize:** establish which data, provenance, consent and
  decision dependencies are material;
- **protect/assure:** preserve trustworthy lifecycle state and validate changes
  before consequential use;
- **detect:** compare, assess and monitor for integrity, provenance or
  authorization discrepancies;
- **contain/respond:** hold suspect data or decisions and coordinate review;
- **recover:** restore a trustworthy state and reassess dependent outputs or
  decisions before resumption.

IR 8467 refines these into candidate interruption points: lifecycle inventory
and flow mapping, software/data/configuration version context, change and
authenticity checks, audit records, tests/exercises with partners, protected
backups and verification of restored asset/pipeline integrity. These remain
recommended outcomes, not a tested chain.

This is a control-objective mapping, not evidence that any control is
implemented, tested or effective for this scenario.

## Assumptions and uncertainty

- Likelihood: unassessed by the source.
- Actor, intent, technique, access and attribution: unknown.
- Exact system architecture, data lineage and trust boundaries: not established.
- Downstream reliance and consequence severity: environment-specific.
- Counterevidence: reference comparisons, provenance checks, independent
  validation, decision holds and safe recovery may interrupt propagation; the
  report does not measure their coverage or effectiveness.
- The scenario must not be presented as an incident or a current vulnerability
  assertion.

## Related scenarios

`RSK-0003` differs from
[RSK-0002](rsk-0002-biomanufacturing-control-integrity-disruption.md):
this page begins with genomic data/provenance and transfers through analysis or
decision, while `RSK-0002` begins with manufacturing process-control or
process/quality-data dependency. They may converge on manufacturing consequence
without constituting the same evidence path.

It also differs from
[RSK-0009](rsk-0009-sequenced-input-to-digital-execution.md) and
[RSK-0010](rsk-0010-multiplex-cross-sample-digital-exposure.md):
those begin with biological/material input and terminate first in a digital
state, while this scenario begins with digital genomic integrity/provenance and
continues toward a consequential decision.

## Related pages

- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [SYS-0003 — Genomic sequencing and analysis ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [WFL-0005 — Genomic data lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [CTL-0002 — Genomic-data risk management and lifecycle assurance](../controls/ctl-0002-genomic-data-risk-management.md)
- [CTL-0009 — EHDS health-data and EHR safeguards](../controls/ctl-0009-ehds-health-data-and-ehr-safeguards.md)
- [SYN-0003 — Cross-domain transfer directions](../syntheses/syn-0003-cross-domain-transfer-directions.md)
- [SRC-0005 — NIST IR 8432 Cybersecurity of Genomic Data](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0006 — NIST IR 8467 2pd](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)

## Sources

- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
  §§1–3; §4.4.2; printed pp. 1–12, 20–22 (PDF pp. 10–21,
  29–31).
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
  §§5.1 and 6; Tables 10–12, 15–25 and 33.
