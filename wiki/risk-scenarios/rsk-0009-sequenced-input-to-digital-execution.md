---
id: RSK-0009
type: risk-scenario
title: Sequenced biological input reaching vulnerable software execution
aliases:
  - controlled DNA input to digital execution path
  - biological material to parser compromise proof of concept
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0014
sensitivity: public
dual_use: moderate
origin_domain: biological
destination_domains:
  - digital
scenario_classification: controlled-proof-of-concept-not-incident
transfer_mechanism: material-to-measurement-to-digital-input
relations:
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: RSK-0009-C01
    evidence:
      - source: SRC-0014
        locator: "Introduction and §3, printed pp. 765–771 (PDF pp. 2–8)"
  - predicate: depends-on
    target: AST-0001
    claim_id: RSK-0009-C02
    evidence:
      - source: SRC-0014
        locator: "§§2.2–2.3 and 3, printed pp. 767–771 (PDF pp. 4–8)"
  - predicate: depends-on
    target: WFL-0005
    claim_id: RSK-0009-C02
    evidence:
      - source: SRC-0014
        locator: "§§2.2–2.3 and 3, printed pp. 767–771 (PDF pp. 4–8)"
  - predicate: depends-on
    target: SYS-0003
    claim_id: RSK-0009-C02
    evidence:
      - source: SRC-0014
        locator: "§§2.2–2.3 and 3, printed pp. 767–771 (PDF pp. 4–8)"
tags:
  - genomics
  - sequencing
  - biological-to-digital
  - controlled-proof-of-concept
  - not-incident
---

# Sequenced biological input reaching vulnerable software execution

> [!WARNING]
> **Evidence classification**
> This is a **controlled proof of concept**, not a documented incident. The
> authors intentionally modified the target utility, added a weakness, and
> weakened environmental protections. No unmodified production system or
> external victim was compromised.

## Scenario

A physical biological or synthetic input enters a sequencing workflow. The
instrument transforms it into digital reads, which reach downstream software.
If compatible unsafe input handling is reachable and isolation/validation does
not interrupt the chain, processing can change digital software state. In the
source's constructed environment, that terminal state was code execution.

No sequence, payload, encoding, target-specific weakness or procedure is
included here.

> **Claim record — RSK-0009-C01 | source-report**
> **Claim:** Ney et al. report a controlled path from synthetic physical DNA
> through sequencing and downstream processing to code execution in an
> intentionally modified, deliberately permissive target environment.
> **Claim status:** active
> **Scope:** One 2017 research setup; not an operational compromise, current
> exploit, representative pipeline or likelihood estimate.
> **As of:** 2017-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> Introduction and §3, printed pp. 765–771 (PDF pp. 2–8).
> **Basis / limits:** Cross-domain stages and observed endpoint are direct. The
> authors created the weakness, disabled common defenses and observed fragile
> run behavior, so external validity is sharply limited.

## Assets and workflow

- [AST-0001](../assets/ast-0001-genomic-data.md) — physical sample/material,
  sequence-derived reads, provenance and downstream output state;
- [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) — preparation,
  generation and downstream processing segment;
- [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) —
  sequencer, file transformation and analysis-software classes;
- research operators and downstream users — potentially affected stakeholders,
  though no external user was affected in the experiment.

## Preconditions and trust boundaries

1. biological/synthetic input is accepted into a sequencing process;
2. derived digital data remains causally linked to that input;
3. it reaches a downstream component with compatible unsafe handling;
4. validation, isolation, privilege boundaries and failure containment do not
   interrupt the path; and
5. the software-state change reaches an execution consequence.

The source establishes this alignment only in its purpose-built environment.

## Origin-domain state

The origin is a physical material/input state represented by
[THR-0001](../threats/thr-0001-adversarial-sequencing-input.md). The input becomes
security-relevant not because DNA is inherently executable, but because the
measurement pipeline converts material into digital data that downstream
software interprets.

## Cross-domain transfer

[TEC-0001](../techniques/tec-0001-biological-input-to-digital-parser-transfer.md)
captures the transfer, and
[VUL-0001](../vulnerabilities/vul-0001-unsafe-bioinformatics-input-handling.md)
captures the weakness class.

> **Claim record — RSK-0009-C02 | analytic-judgment**
> **Claim:** The complete safe path is `material/input → sequencing
> transformation → digital reads → downstream parser → software-state change`,
> conditional on the linked threat, transfer method, workflow/system and unsafe
> input-handling preconditions.
> **Claim status:** active
> **Scope:** Structural interpretation of the demonstrated experiment; not an
> operational recipe or universal sequencing-system property.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §§2.2–2.3 and 3, printed pp. 767–771 (PDF pp. 4–8); §6,
> printed pp. 773–776 (PDF pp. 10–13).
> **Basis / limits:** Each stage is source-supported and the experimental
> outcome closes the reverse-direction path. Only the authors' artificial
> environment joins all conditions; no field prevalence is inferred.

## Receiving-domain state and consequences

The immediate receiving state is changed digital program execution. The source
does not document altered genomic interpretation, corrupted research, clinical
decision, privacy harm, safety outcome or biological effect from the PoC.

> **Claim record — RSK-0009-C03 | analytic-judgment**
> **Claim:** The observed consequence is digital execution in a controlled
> target; downstream research, privacy, clinical, safety and biological harms
> remain unobserved and cannot be counted as incident consequences.
> **Claim status:** active
> **Scope:** Consequence classification for the 2017 proof of concept.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> Introduction, §§3, 7 and Conclusions, printed pp. 765–778
> (PDF pp. 2–15).
> **Basis / limits:** The experiment stops at digital execution; later impacts
> appear only in threat discussion. No `INC` or downstream outcome is created.

## Evidence

One peer-reviewed author-team lineage supplies the experiment and analysis.
There is no independent replication, production victim, forensic record or
current exposure assessment. Reliability measurements characterize the setup,
not sector likelihood.

## Controls by function

[CTL-0007](../controls/ctl-0007-secure-sequencing-input-processing.md) conditionally
maps provenance/intake, safe parsing, validation/isolation, update authenticity,
monitoring and containment/recovery to exact edges. All are recommended-only;
the experiment did not test them as safeguards.

## Assumptions and uncertainty

- input access and parser reach are not established for any real service;
- current software and platform defenses are unknown;
- the source's target weakness is not the same as its three crash-only audit
  findings;
- a physical-to-digital possibility is not a probability;
- no biological or human consequence followed from the experiment.

## Related scenarios

- [RSK-0010](rsk-0010-multiplex-cross-sample-digital-exposure.md)
- [RSK-0003](rsk-0003-genomic-data-integrity-decision-harm.md)

## Sources

- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
  Introduction, §§2–3, 6–8.
