---
id: RSK-0005
type: risk-scenario
title: Privacy harm from technically authorized human-genomic-data processing
aliases:
  - genomic privacy harm without cyber incident
  - problematic permitted genomic-data processing
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0016
sensitivity: public
dual_use: low
origin_domain: digital
destination_domains:
  - digital
relations:
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: RSK-0005-C01
    evidence:
      - source: SRC-0006
        locator: "§§2.2–2.2.1 and Figures 2–3, printed pp. 9–11 (PDF pp. 20–22)"
  - predicate: evidenced-by
    target: SRC-0007
    claim_id: RSK-0005-C04
    evidence:
      - source: SRC-0007
        locator: "Volume C §§1.4–1.6, printed pp. 4–6 (PDF pp. 13–15); §3, printed p. 43 (PDF p. 52); static Appendix C"
  - predicate: depends-on
    target: AST-0001
    claim_id: RSK-0005-C02
    evidence:
      - source: SRC-0005
        locator: "§1.1, printed pp. 1–2 (PDF pp. 10–11); §§3.2 and 3.7, printed pp. 9–12 (PDF pp. 18–21)"
      - source: SRC-0006
        locator: "§§2.2–2.2.1, printed pp. 9–11 (PDF pp. 20–22); §§5.2 and 5.4–5.6, printed pp. 23–25 (PDF pp. 34–36)"
  - predicate: depends-on
    target: WFL-0005
    claim_id: RSK-0005-C02
    evidence:
      - source: SRC-0006
        locator: "§1.2 and Figure 1, printed pp. 4–5 (PDF pp. 15–16); Tables 26 and 32–36, printed pp. 141–166 (PDF pp. 152–177)"
  - predicate: depends-on
    target: SYS-0003
    claim_id: RSK-0005-C02
    evidence:
      - source: SRC-0006
        locator: "§1.3, printed p. 5 (PDF p. 16); Tables 26–36, printed pp. 141–166 (PDF pp. 152–177)"
  - predicate: evidenced-by
    target: SRC-0016
    claim_id: RSK-0005-C05
    evidence:
      - source: SRC-0016
        locator: "Articles 53–54 and 66–73, PDF pp. 59–60, 69–76; Article 105, PDF pp. 90–91"
  - predicate: governed-by
    target: GOV-0006
    claim_id: RSK-0005-C05
    evidence:
      - source: SRC-0016
        locator: "Articles 1–2, 50–54, 66–73 and 105, PDF pp. 29–33, 57–60, 69–76, 90–91"
tags:
  - genomic-data
  - privacy
  - problematic-data-action
  - consent
  - permitted-processing
  - hypothetical
---

# Privacy harm from technically authorized human-genomic-data processing

> [!WARNING]
> **Evidence classification**
> This is a **hypothetical, single-programme-lineage scenario**, not an incident
> or cyberattack. NIST explicitly recognizes that privacy harm may arise when
> technically authorized processing operates as intended but creates
> predictability, manageability, or disassociability problems for individuals.

## Scenario

An organization performs a technically permitted action on human genomic data,
but the processing purpose, combination, retention, inference, sharing or later
reuse is not sufficiently predictable, manageable or disassociated for the
affected person or biological relatives. A resulting problematic data action
may create unwanted identifiability, inference, loss of autonomy or inability
to exercise an applicable preference. Conditional consequences include dignity
or trust loss, discrimination, economic harm and organizational reputation or
participation impacts.

The path does not require loss of confidentiality, malicious access or system
compromise. It contains no individual records, linkage procedure, dataset
example or operational re-identification detail.

## Assets and workflow

- [AST-0001](../assets/ast-0001-genomic-data.md) — human genomic data, derived
  outputs, annotations and consent/purpose context;
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) — collection through
  disposition, including sharing, reuse and later analysis;
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) —
  processors, repositories, services and organizational roles;
- donors, patients, participants, consumers and biological relatives —
  potentially affected people, not data assets.

## Preconditions and trust boundaries

The conditional path requires:

1. processing of human genomic data or derived information is technically
   allowed in the system;
2. processing has inherent or contextual privacy effects that are not fully
   prevented or managed by applicable notice, consent, preferences,
   minimization or disassociation measures;
3. the action produces an association, inference, disclosure, retained state or
   loss of individual control capable of causing a privacy problem;
4. organizational review, communication, preference handling or another
   safeguard does not prevent or contain the consequence.

No precondition is established for a named organization, person or dataset.
Legal and ethical permissibility can differ from technical authorization and
must be assessed in the relevant jurisdiction and programme.

## Origin-domain state

The origin state is a technically authorized genomic-data processing action;
the scenario does not assume loss of confidentiality/access control and does
not require a defect in the stated purpose or consent state.
Examples at the safe abstraction level include using data for a changed
purpose, combining contexts, retaining or sharing a derived state, or producing
an inference. The wiki does not assume malicious intent or an exploited
vulnerability.

> **Claim record — RSK-0005-C01 | source-report**
> **Claim:** NIST IR 8467 2pd states that permitted data processing can create
> privacy problems independently of cybersecurity incidents, even when
> cybersecurity risk management controls access as intended.
> **Claim status:** active
> **Scope:** Human genomic-data privacy-risk framing, not an observed event or
> finding that all permitted processing is harmful.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§2.2–2.2.1 and Figures 2–3, printed pp. 9–11 (PDF pp. 20–22).
> **Basis / limits:** The distinct privacy-event pathway is explicit and the
> figures were visually checked. The source provides conceptual examples, not
> frequency, likelihood, a participant cohort or validated causal sequence.

## Cross-domain transfer

The transfer remains digital-to-human-privacy rather than cyber-to-biological:

- **processing transition:** technically permitted action changes what is
  knowable, linked, retained, inferred or manageable about a person or kin;
- **privacy transition:** the state becomes a privacy problem through lost
  predictability, manageability or disassociability;
- **consequence transition:** an individual experiences dignity, autonomy,
  discrimination, trust or economic harm; the organization may experience
  participation, reputation, financial or governance impact.

> **Claim record — RSK-0005-C02 | analytic-judgment**
> **Claim:** `SRC-0005` and `SRC-0006` support a conditional permitted-
> processing path across `AST-0001`, `WFL-0005` and `SYS-0003`, distinct from
> the unauthorized disclosure path in `RSK-0004`; no complete event, likelihood
> or safeguard failure is established.
> **Claim status:** active
> **Scope:** Human genomic-data processing where technical authorization and
> privacy acceptability are not equivalent; no named deployment.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §1.1, printed pp. 1–2 (PDF pp. 10–11); §§3.2 and 3.7,
> printed pp. 9–12 (PDF pp. 18–21);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§1.2–2.2, printed pp. 4–11 (PDF pp. 15–22); Tables 26 and
> 32–36, printed pp. 141–166 (PDF pp. 152–177).
> **Basis / limits:** Both sources distinguish privacy from confidentiality and
> describe lifecycle/data-processing dependencies. They share NIST/NCCoE
> programme lineage and provide no incident, prevalence, implementation or
> measured outcome; the exact scenario assembly is a bounded wiki inference.

## Receiving-domain state

The immediate receiving state is a privacy problem: unexpected association or
inference, lost practical control over processing preference, or inability to
keep a person or relative suitably disassociated. It can arise even when a
stated business purpose or consent state remains valid; it need not include
public disclosure, and the source establishes no universal harm threshold.

## Immediate and downstream consequences

Figure 3 connects problematic data actions to possible dignity effects,
discrimination and economic loss for individuals, then to organizational
impacts such as customer/participant abandonment, reputation, financial cost or
internal-culture effects.

> **Claim record — RSK-0005-C03 | source-report**
> **Claim:** IR 8467 presents dignity/stigma, discrimination and economic loss
> as possible individual outcomes of problematic data actions, with potential
> downstream organizational trust, participation, reputation, financial and
> internal-culture impacts.
> **Claim status:** active
> **Scope:** Potential consequence categories illustrated by the profile, not
> incidence, severity or a deterministic chain.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §2.2 and Figure 3, printed pp. 10–11 (PDF pp. 21–22).
> **Basis / limits:** Categories and diagrammed direction are direct. They do
> not show that every problematic action reaches an individual, that every
> individual impact reaches an organization or that the impacts were measured.

## Evidence

Evidence consists of three same-programme NIST source packages, with IR 8467
providing the clearest profile-level pathway and SP 1800-43C applying privacy
threat modeling to bounded example environments. None is an incident
investigation, representative study or effectiveness evaluation. No `INC`,
`THR`, `TEC` or `VUL` entity follows from this scenario.

Counterevidence or additional context could show that processing is expected,
purpose-compatible, consent-consistent, sufficiently disassociated, reversible
through preference handling, or otherwise prevented from causing a material
privacy problem. Those conditions require deployment-specific evidence.

> **Claim record — RSK-0005-C04 | source-report**
> **Claim:** NIST SP 1800-43C explicitly includes privacy threats caused by
> inaction, processing side effects or a system operating as designed and
> reports limited individual informed-consent/control as a notable concern in
> its examined use cases.
> **Claim status:** active
> **Scope:** Findings and modeled possibilities in the draft's generalized
> clinical/research environments; not prevalence, a legal determination or an
> observed harm event.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> Volume C §§1.4–1.6, printed pp. 4–6 (PDF pp. 13–15); §3, printed p. 43
> (PDF p. 52); static Appendix C, `Privacy Threat Modeling`.
> **Basis / limits:** The broader privacy-threat frame and source conclusion
> are direct. The exercise covers a small set of use cases and organizations;
> it reports no affected-person cohort, occurrence rate, causal validation,
> deployed consent control or measured outcome.

### EU EHDS-governed secondary-use branch

EHDS adds a binding but staged EU branch to this scenario. It distinguishes
permitted secondary-use purposes from prohibited uses and then conditions
access on an application/permit path, data minimisation, opt-out and exception
rules, secure processing and result-disclosure controls. These legal
interruption points neither establish that a particular processing action is
privacy-acceptable nor show that privacy harm occurred.

> **Claim record — RSK-0005-C05 | source-report**
> **Claim:** EHDS demonstrates that permitted electronic-health and human-
> omics secondary use remains purpose-, permit-, prohibition-, minimisation-,
> opt-out- and safeguard-bounded; legal permission therefore is not evidence
> that a particular action is privacy-acceptable or that harm occurred.
> **Claim status:** active
> **Scope:** EHDS-governed EU secondary use under the applicable staged dates;
> no actual permit, dataset, person, national exception or outcome.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> Articles 53–54 and 66–73, PDF pp. 59–60, 69–76; Article 105,
> PDF pp. 90–91.
> **Basis / limits:** Purposes, prohibitions, permit conditions, minimisation,
> opt-out and secure-processing requirements are direct. Their application is
> staged, national exceptions and other law remain relevant, and the source
> provides no processing event, affected person, implementation or outcome.

## Controls by function

[CTL-0002](../controls/ctl-0002-genomic-data-risk-management.md) conditionally maps
to the path through:

- **govern/inventory:** record purposes, data actions, affected groups, roles,
  requirements and processing locations;
- **prevent/manage:** align access, minimization, consent and preferences with
  each processing action rather than relying on technical authorization alone;
- **detect/review:** monitor processing, disclosures, provenance and
  problematic-action reports; reassess when technology, purpose or partners
  change;
- **respond/communicate:** handle complaints, corrections, deletion or consent
  changes where applicable and notify affected parties when required;
- **assure:** test the defined privacy outcomes and document residual risk.

These are draft recommended outcomes. Implementation, testing, effectiveness
and independent evaluation remain unknown.

[CTL-0003](../controls/ctl-0003-genomic-data-privacy-threat-modeling.md) can expose
ordinary data actions that may undermine privacy objectives and make response
decisions traceable. Its example application is not direct mitigation and does
not establish that `CTL-0002` safeguards were implemented or effective.

## Assumptions and uncertainty

- Likelihood and prevalence: not reported.
- Processing purpose, data granularity, inference context and affected people:
  unspecified.
- Technical authorization does not establish legal, ethical or consent
  permissibility; no universal rule is inferred.
- Individual and organizational consequences are conditional.
- No operational re-identification, evasion or attack assumptions are used.
- Same NIST/NCCoE lineage does not satisfy independent corroboration.

## Related scenarios

- [RSK-0004 — Disclosure and kin privacy harm](rsk-0004-genomic-data-disclosure-kin-privacy.md) requires loss of confidentiality, authorization or purpose control and allows linkage/inference after exposure; `RSK-0005` does not require a cyber or access-control failure.
- [RSK-0003 — Genomic-data integrity and decision harm](rsk-0003-genomic-data-integrity-decision-harm.md) concerns data/decision integrity rather than privacy acceptability of permitted processing.
- [RSK-0010 — Multiplex cross-sample technical exposure](rsk-0010-multiplex-cross-sample-digital-exposure.md) begins with a measurement/association condition and does not require technically authorized purposeful processing.
- [RSK-0011 — Part 202 regulated access branches](rsk-0011-covered-omics-regulated-access.md) classifies a U.S. regulatory access/transaction boundary; authorization under that regime neither proves privacy acceptability nor establishes privacy harm.

## Related pages

- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [WFL-0005 — Genomic data lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003 — Genomic sequencing and analysis ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [CTL-0002 — Genomic-data risk management](../controls/ctl-0002-genomic-data-risk-management.md)
- [CTL-0003 — Genomic-data privacy threat modeling](../controls/ctl-0003-genomic-data-privacy-threat-modeling.md)
- [CTL-0008 — Part 202 transaction controls](../controls/ctl-0008-restricted-data-transaction-controls.md)
- [CTL-0009 — EHDS health-data and EHR safeguards](../controls/ctl-0009-ehds-health-data-and-ehr-safeguards.md)
- [GOV-0005 — US Data Security Program](../governance/gov-0005-us-data-security-program-2025.md)
- [GOV-0006 — EU EHDS governance](../governance/gov-0006-eu-ehds-regulation-2025.md)
- [SYN-0003 — Cross-domain transfer directions](../syntheses/syn-0003-cross-domain-transfer-directions.md)
- [SYN-0004 — US–EU human-omics and health-data governance](../syntheses/syn-0004-us-eu-human-omics-health-data-governance.md)
- [SRC-0005 — NIST IR 8432](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0006 — NIST IR 8467 2pd](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0007 — NIST SP 1800-43 A/C](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md)
- [SRC-0016 — EU EHDS Regulation](../sources/src-0016-eu-ehds-regulation-2025.md)

## Sources

- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
  §§1.1, 3.2 and 3.7.
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
  §§1.2–2.2, 5.2, 5.4–5.6 and 6; Figures 1–3; Tables 26 and 32–36.
- [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
  Volume C §§1.4–1.6 and §3; static Appendix C.
