---
id: RSK-0004
type: risk-scenario
title: Disclosure of human genomic data and kin privacy harm
aliases:
  - genomic-data disclosure and re-identification
  - kin privacy harm from genomic data
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0005
  - SRC-0006
  - SRC-0007
sensitivity: public
dual_use: moderate
origin_domain: digital
destination_domains:
  - digital
relations:
  - predicate: evidenced-by
    target: SRC-0005
    claim_id: RSK-0004-C01
    evidence:
      - source: SRC-0005
        locator: "§§1.1–2.1, printed pp. 1–4 (PDF pp. 10–13); §§2.6–3.4, printed pp. 6–11 (PDF pp. 15–20)"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: RSK-0004-C04
    evidence:
      - source: SRC-0006
        locator: "§§2.2–2.2.1, printed pp. 9–11 (PDF pp. 20–22); §§5.2 and 5.4–5.6, printed pp. 23–25 (PDF pp. 34–36)"
  - predicate: evidenced-by
    target: SRC-0007
    claim_id: RSK-0004-C05
    evidence:
      - source: SRC-0007
        locator: "Volume C §§2.2.1–2.2.3 and Tables 12–15, printed pp. 20–30 (PDF pp. 29–39); static Appendices F–G"
  - predicate: affects
    target: AST-0001
    claim_id: RSK-0004-C01
    evidence:
      - source: SRC-0005
        locator: "§§2.6–3.4, printed pp. 6–11 (PDF pp. 15–20)"
  - predicate: depends-on
    target: WFL-0005
    claim_id: RSK-0004-C01
    evidence:
      - source: SRC-0005
        locator: "§2.1, printed pp. 3–4 (PDF pp. 12–13); §3.2, printed pp. 9–10 (PDF pp. 18–19)"
  - predicate: depends-on
    target: SYS-0003
    claim_id: RSK-0004-C01
    evidence:
      - source: SRC-0005
        locator: "§§2.1–2.3, printed pp. 3–5 (PDF pp. 12–14); §3.2, printed pp. 9–10 (PDF pp. 18–19)"
tags:
  - genomics
  - privacy
  - re-identification
  - kinship
  - hypothetical
---

# Disclosure of human genomic data and kin privacy harm

> [!WARNING]
> **Evidence classification**
> Hypothetical, single-programme-lineage scenario: unauthorized disclosure of
> human genomic data may enable linkage, re-identification or inference
> concerning an individual and biological relatives. NIST IR 8432, draft
> IR 8467 and SP 1800-43 share NCCoE programme lineage; likelihood, actor and
> disclosure vector remain unknown.

## Scenario

Loss of confidentiality or access-boundary control discloses human genomic data
to an unauthorized or unintended recipient.
If the disclosed data can be linked with other information or used to infer
identity, health, phenotype or kinship, the receiving digital state may associate
sensitive attributes with a participant or relative. Potential consequences
include privacy and dignity loss, discrimination, reputational or psychological
harm and economic harm.

The scenario does not provide re-identification instructions, dataset examples,
individual records or operational attack steps.

## Assets and workflow

- [AST-0001](../assets/ast-0001-genomic-data.md) — the disclosed biologically derived
  digital asset;
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) — generation,
  storage, aggregation, sharing, analysis and downstream use;
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) — the
  functional processing/storage ecosystem, not a claimed attack surface;
- research participants, patients, consumers and biological relatives —
  affected stakeholders.

## Preconditions and trust boundaries

The path requires:

1. human genomic data or derived information crosses its authorized
   confidentiality/access boundary to an unauthorized or unintended recipient;
2. the data retain enough information for linkage or inference in the relevant
   context;
3. other data, knowledge or services make association with a person or kin
   possible;
4. access, consent, contractual, technical or governance safeguards do not
   prevent or contain the downstream use.

None of these preconditions is established for a named organization or dataset.

## Origin-domain state

The origin state is loss of confidentiality or access authorization over human
genomic data. The trigger could be malicious or accidental; current evidence
does not identify actor, technique, vector, system vulnerability or observed
event. A technically authorized processing action without disclosure is
modeled separately in `RSK-0005`.

## Cross-domain transfer

The transfer mechanism is **data linkage and inference**: biologically derived
digital information is associated with identity, phenotype, health or kinship
information. This is a digital-to-human privacy consequence path; no change to
a genome, biological sample or clinical outcome is claimed.

> **Claim record — RSK-0004-C01 | analytic-judgment**
> **Claim:** Unauthorized disclosure of human genomic data can form a
> conditional path from loss of digital confidentiality/authorization through
> linkage or inference to privacy harms affecting both an individual and
> biological relatives.
> **Claim status:** active
> **Scope:** Human genomic data in research, clinical, consumer or aggregated
> data contexts; no named event.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** medium
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§1.1–2.1, printed pp. 1–4 (PDF pp. 10–13); §§2.6–3.4,
> printed pp. 6–11 (PDF pp. 15–20).
> **Basis / limits:** NIST directly connects confidentiality/privacy concerns,
> genomic persistence/kinship and potential harms, but it does not validate a
> full event path, likelihood or safeguards in a defined environment. Primary
> re-identification studies cited by NIST are not independently ingested.

## Receiving-domain state

The immediate receiving state is a digital association or inference that makes
previously unlinked identity, health, phenotype, relationship or consent context
available to an unauthorized or unintended party. The report does not establish
that every genomic fragment permits this outcome or that a uniform threshold
exists.

> **Claim record — RSK-0004-C02 | source-report**
> **Claim:** NIST IR 8432 reports that human genomic information may be
> persistent, identifying and correlated across relatives, and that even data
> stripped of conventional identifiers can retain re-identification concern.
> **Claim status:** active
> **Scope:** Source synthesis of human-genomic privacy characteristics.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** medium
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §2.1, printed pp. 3–4 (PDF pp. 12–13); §2.6, printed pp. 6–7
> (PDF pp. 15–16); §3.2, printed pp. 9–10 (PDF pp. 18–19).
> **Basis / limits:** This is NIST's report of workshop/literature findings.
> Underlying primary studies have not been ingested, one nearby citation number
> is internally inconsistent, and no universal re-identification success rate
> is established.

## Immediate and downstream consequences

Source-reported potential consequences include:

- exposure of sensitive health, phenotype or biological-relationship
  information;
- dignity, trust, psychological or reputational harm;
- discrimination or intimidation/extortion concerns;
- economic harm to an individual or organization;
- effects on relatives who did not provide or control the disclosed record.

> **Claim record — RSK-0004-C03 | source-report**
> **Claim:** NIST IR 8432 identifies privacy, dignity, discrimination,
> reputational, psychological and economic harms as potential consequences of
> loss or misuse of human genomic information, including effects on relatives.
> **Claim status:** active
> **Scope:** Potential consequence categories, not observed incidence,
> prevalence or severity.
> **As of:** 2023-12-20.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§3.2–3.4, printed pp. 9–11 (PDF pp. 18–20); §3.7, printed p. 12
> (PDF p. 21).
> **Basis / limits:** Confidence is high that the report lists these
> categories. It does not show that all harms follow every disclosure or
> provide a measured consequence distribution.

## Evidence

Evidence is one NIST/NCCoE programme lineage: a final stakeholder/expert
report supported by cited literature, a later draft profile and a bounded
privacy threat-modeling exercise. It is not an incident investigation, cohort
study or controlled evaluation. The cited primary re-identification studies
remain unreviewed in this wiki. No `INC`, `THR`, `TEC` or `VUL` page is
justified by these sources.

IR 8467 also makes an important boundary explicit: a privacy event can arise
from permitted processing without a cybersecurity incident. That sibling path
is modeled separately in
[RSK-0005](rsk-0005-permitted-genomic-processing-privacy-harm.md);
it must not be mislabeled as disclosure or used to imply unauthorized access.

> **Claim record — RSK-0004-C04 | source-report**
> **Claim:** IR 8467 2pd distinguishes cyber-related disclosure/privacy events
> from privacy problems caused by permitted processing and recommends separate
> donor, relative, consent and authorized-access objectives.
> **Claim status:** active
> **Scope:** Boundary around `RSK-0004`; permitted-processing harms are related
> but are not evidence that this disclosure path occurred.
> **As of:** 2024-12-16.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§2.2–2.2.1 and Figures 2–3, printed pp. 9–11 (PDF pp. 20–22);
> §§5.2 and 5.4–5.6, printed pp. 23–25 (PDF pp. 34–36).
> **Basis / limits:** The conceptual distinction and objectives are direct.
> The profile supplies no disclosure incident, likelihood, consent-system
> implementation or measured privacy outcome.

SP 1800-43C makes the modeling evidence more concrete by tracing possible
linking, identifying and disclosure conditions across bounded example
dataflows, then checking them against privacy objectives. Those entries remain
hypothetical outputs of the method. The source does not show that a modeled
attack occurred, that the example covers all relevant threats or that a
candidate intervention interrupted the path.

> **Claim record — RSK-0004-C05 | source-report**
> **Claim:** NIST SP 1800-43C models possible linking, identification and data-
> disclosure threats across example genomic-processing flows and internally
> cross-checks retained entries against LINDDUN, PANOPTIC and privacy
> engineering objectives.
> **Claim status:** active
> **Scope:** Hypothetical threats in generalized clinical/research sample
> environments; not an observed disclosure or re-identification event.
> **As of:** 2025-08-05.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
> Volume C §§2.2.1–2.2.3 and Tables 12–15, printed pp. 20–30
> (PDF pp. 29–39); static Appendices F–G.
> **Basis / limits:** The modeled categories, scenarios and internal validation
> are direct. They provide no actor attribution, exploited weakness,
> occurrence, prevalence, likelihood, empirical completeness or safeguard
> outcome. Detailed paths are not reproduced.

## Controls by function

[CTL-0002](../controls/ctl-0002-genomic-data-risk-management.md) records the
source's proposed risk-management, access/consent, sharing, monitoring and
privacy-enhancing directions. Relevant functions include:

- identify data, purposes, subjects/kin implications, consent and recipients;
- prevent unauthorized disclosure or use with proportionate access and
  data-sharing controls;
- detect/report access, transfer or consent deviations;
- contain disclosure and support affected persons when an event occurs;
- reassess aggregation, linkage and residual privacy risk;
- validate protections for the defined analysis and environment.

The source supplies proposals and expected benefits, not implementation,
testing or effectiveness evidence. `CTL-0002` cannot close this path without
deployment-specific assurance.

[CTL-0003](../controls/ctl-0003-genomic-data-privacy-threat-modeling.md) can help a
local team identify and trace candidate disclosure/linkage edges and response
decisions. It is an assessment control, not a direct mitigation, and its
example application does not change the implementation or effectiveness state
of `CTL-0002`.

## Assumptions and uncertainty

- Likelihood: **not evaluated**.
- Actor, intent, vector and vulnerability: **unknown**.
- Data granularity, linkage environment and inference capability: unspecified.
- Legal and consent context: organization- and jurisdiction-specific.
- Consequence: conditional; no numerical severity or frequency.
- Counterevidence: access limits, purpose controls, privacy-enhancing methods
  and lack of linkable auxiliary data may interrupt the path; their actual
  implementation is unknown.

## Related scenarios

- [RSK-0003 — Genomic-data integrity and decision harm](rsk-0003-genomic-data-integrity-decision-harm.md) addresses integrity and downstream decisions; `RSK-0004` addresses confidentiality/authorized use and privacy.
- [RSK-0005 — Technically authorized processing and genomic privacy harm](rsk-0005-permitted-genomic-processing-privacy-harm.md) addresses a distinct no-cyber-incident processing pathway.
- [RSK-0010 — Multiplex cross-sample technical exposure](rsk-0010-multiplex-cross-sample-digital-exposure.md) measures a provenance/confidentiality exposure but does not establish disclosure harm or re-identification.
- [RSK-0011 — Part 202 regulated access branches](rsk-0011-covered-omics-regulated-access.md) models legal transaction/access classification; regulated access is not by itself evidence of unauthorized disclosure, linkage or kin harm.

## Related pages

- [RSK-0020 — Observed consumer-genetics disclosure and kin-privacy path](rsk-0020-genetic-account-access-relative-graph-privacy-harm.md)

- [AST-0001 — Genomic data](../assets/ast-0001-genomic-data.md)
- [WFL-0005 — Genomic data lifecycle](../workflows/wfl-0005-genomic-data-lifecycle.md)
- [SYS-0003 — Genomic sequencing and analysis ecosystem](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md)
- [CTL-0002 — Genomic-data risk management](../controls/ctl-0002-genomic-data-risk-management.md)
- [CTL-0003 — Genomic-data privacy threat modeling](../controls/ctl-0003-genomic-data-privacy-threat-modeling.md)
- [CTL-0008 — Part 202 transaction controls](../controls/ctl-0008-restricted-data-transaction-controls.md)
- [CTL-0009 — EHDS health-data and EHR safeguards](../controls/ctl-0009-ehds-health-data-and-ehr-safeguards.md)
- [GOV-0005 — US Data Security Program](../governance/gov-0005-us-data-security-program-2025.md)
- [SYN-0003 — Cross-domain transfer directions](../syntheses/syn-0003-cross-domain-transfer-directions.md)
- [SRC-0005 — NIST IR 8432](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0006 — NIST IR 8467 2pd](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0007 — NIST SP 1800-43 A/C](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md)

## Sources

- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
  §§1–3.7, printed pp. 1–12.
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
  §§2.2–2.2.1, 5.2 and 5.4–5.6; Figures 2–3.
- [SRC-0007](../sources/src-0007-nist-sp-1800-43-genomic-privacy-threat-modeling-2025.md),
  Volume C §§2.2.1–2.2.3; Tables 12–15; static Appendices F–G.
