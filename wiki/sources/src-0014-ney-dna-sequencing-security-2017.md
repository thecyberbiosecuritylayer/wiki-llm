---
id: SRC-0014
type: source
title: "Computer Security, Privacy, and DNA Sequencing: Compromising Computers with Synthesized DNA, Privacy Leaks, and More"
aliases:
  - Ney et al. DNA sequencing security 2017
  - USENIX synthetic DNA to computer proof of concept
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_type: peer-reviewed-study
ingest_status: complete
sensitivity: public
dual_use: moderate
raw_path: ../../raw/usenix-dna-sequencing-security-2017.pdf
sha256: 4731fc39b3f89094447be655df236cb1927cd926697e9f28f77cf5388ea8762e
canonical_url: https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/ney
direct_pdf_url: https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-ney.pdf
accessed: 2026-07-12
authors:
  - Peter Ney
  - Karl Koscher
  - Lee Organick
  - Luis Ceze
  - Tadayoshi Kohno
publisher: USENIX Association
conference: 26th USENIX Security Symposium
publication_date: 2017-08
pages: 765–779
isbn: 978-1-931971-40-9
tags:
  - dna-sequencing
  - bioinformatics
  - controlled-proof-of-concept
  - sample-cross-talk
  - software-security
  - reverse-cross-domain-path
---

# Computer Security, Privacy, and DNA Sequencing

## Bibliographic identity

Peter Ney, Karl Koscher, Lee Organick, Luis Ceze and Tadayoshi Kohno,
University of Washington. *Computer Security, Privacy, and DNA Sequencing:
Compromising Computers with Synthesized DNA, Privacy Leaks, and More*.
Proceedings of the 26th USENIX Security Symposium, August 2017, printed
pp. 765–779.

The paper reports three related studies by one author team: a controlled
synthetic-DNA→sequencing→software proof of concept, a measurement of
cross-sample read misassignment in one multiplex run, and a version-bounded
software-security audit. They are three findings from one lineage, not three
independent replications.

## Provenance

- Immutable local artifact:
  `../../raw/usenix-dna-sequencing-security-2017.pdf`, 1,275,518 bytes,
  17 physical pages (USENIX cover plus 16 proceedings pages), SHA-256
  `4731fc39b3f89094447be655df236cb1927cd926697e9f28f77cf5388ea8762e`.
- PDF 1.6, unencrypted and untagged, with no JavaScript, form, embedded file or
  digital signature. All pages, figures, tables, footnotes, conclusions,
  acknowledgements and references were textually and visually reviewed.
- The official USENIX paper page supplies matching authors, title, venue,
  ISBN and printed pages. A streamed official PDF retrieval on 2026-07-12
  returned 1,275,518 bytes with the same SHA-256.
- No appendix, dataset or supplementary artifact is included or linked as a
  separate evidentiary component. The source's referenced tools, services,
  repositories and code were not executed or treated as current evidence.
- The source contains operational exploit material. It was reviewed as
  untrusted data, but derivative pages omit the sequence, payload, byte
  encoding, vulnerability construction, source code, procedural exploit steps,
  infrastructure identifiers and proposed robustness adaptations.

> **Claim record — SRC-0014-C01 | artifact-observation**
> **Claim:** The preserved 1,275,518-byte PDF is the complete 17-page USENIX
> artifact identified above, and the official USENIX download was
> byte-identical on 2026-07-12.
> **Claim status:** active
> **Scope:** Artifact identity, completeness and dated remote comparison; not
> current software-vulnerability or real-world threat status.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** local file/hash/PDF inspection; cover and printed pp. 765–779
> (PDF pp. 1–17); USENIX landing metadata and streamed official-PDF hash.
> **Basis / limits:** Bytes, page structure and bibliographic fields are direct.
> The paper does not provide an external replication package.

## Executive summary

The first experiment demonstrates a reverse cyber-biological direction at safe
abstraction: a deliberately constructed physical DNA input was sequenced;
resulting digital reads were processed by a downstream utility that the authors
had intentionally modified to add a memory-safety weakness; the research setup
then reached code execution. The target was not an unmodified field tool or a
production laboratory system, and common platform defenses were deliberately
weakened.

The second study measured bidirectional read misassignment between samples in
one multiplexed sequencing run. This is observed technical confidentiality and
integrity exposure. The authors' malicious-injection and sensitive-information
uses are threat hypotheses, not observed privacy harm, scientific error or
clinical consequence.

The third study compared proxy indicators in 13 selected C/C++ NGS programs and
10 Internet-facing controls, then produced controlled crashes in three NGS
programs. The audit is version- and 2017-sample-specific. It does not establish
the exploitability or current affected status of those packages.

## Claims and locators

> **Claim record — SRC-0014-C02 | source-report**
> **Claim:** The authors report a controlled end-to-end experiment in which a
> synthetic physical DNA input was sequenced and its resulting reads caused
> code execution when processed by a deliberately modified downstream utility
> in a deliberately permissive research environment.
> **Claim status:** active
> **Scope:** One proof-of-concept setup; not an incident, production compromise,
> exploit of an unmodified field tool, prevalence estimate or likelihood.
> **As of:** 2017-08.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** Abstract and Introduction, printed pp. 765–766 (PDF pp. 2–3);
> §3 and Figures 1–3, printed pp. 768–771 (PDF pp. 5–8).
> **Basis / limits:** Physical input, sequencing, digital processing and observed
> execution are direct author-reported results. The authors introduced the
> target weakness and disabled common defenses, so field generalization is
> intentionally rejected.

> **Claim record — SRC-0014-C03 | source-report**
> **Claim:** In the proof-of-concept run, the authors report 811,118 reads;
> 76.2% had no sequencing error, 49.1% of error-free reads had the needed
> orientation, 37.4% of all reads met both conditions, and only one of four
> lane files produced the demonstrated execution outcome.
> **Claim status:** active
> **Scope:** Reliability measurements for the authors' single artificial setup;
> not attack probability for real sequencing services or current platforms.
> **As of:** 2017-08.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §3.2–3.3, printed pp. 770–771 (PDF pp. 7–8).
> **Basis / limits:** Counts and proportions are directly reported. The source's
> modeled multi-file probability is setup-specific and is not generalized here;
> the single-run outcome also shows material fragility.

> **Claim record — SRC-0014-C04 | source-report**
> **Claim:** In one eight-sample multiplex run, the authors measured
> bidirectional cross-sample read assignment: 112 reads in the experimental
> file aligned to the comparison sample (111 unique; 68 exact), representing
> 16,521 of about 235 million comparison-sample bases, while 37 experimental
> reads appeared in the comparison file (30 without error).
> **Claim status:** active
> **Scope:** One permitted comparison using one sequencing/index configuration;
> not a general platform rate, privacy breach, malicious injection or changed
> downstream decision.
> **As of:** 2017-08.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §5, printed pp. 772–773 (PDF pp. 9–10).
> **Basis / limits:** Direction and counts are measured. The paper calls the
> estimate rough, notes configuration sensitivity and reports no identified
> person, sensitive inference, corrupted research result or clinical harm.

> **Claim record — SRC-0014-C05 | source-report**
> **Claim:** The software audit found a higher mean frequency of selected
> insecure library calls in 13 versioned C/C++ NGS programs than in 10 selected
> Internet-facing control programs (2.005 versus 0.185 per 1,000 lines;
> two-tailed p=0.027), while static-buffer declarations did not differ
> significantly (6.729 versus 7.312; p=0.809).
> **Claim status:** active
> **Scope:** Non-random 2017 program/version sample and proxy measures; not a
> current vulnerability rate, exhaustive audit or causal comparison.
> **As of:** 2017-08.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §6, Table 1 and Figure 4, printed pp. 773–775
> (PDF pp. 10–12).
> **Basis / limits:** Sample, method, means and tests are direct. Insecure-call
> counts are heuristics; the selected groups differ by purpose, size and
> development context, and the null buffer-declaration result is retained.

> **Claim record — SRC-0014-C06 | source-report**
> **Claim:** Static analysis and manual review identified buffer-overflow
> conditions in three of the 13 audited NGS programs, and constructed inputs
> produced controlled crashes; the authors did not turn those three findings
> into working exploits.
> **Claim status:** active
> **Scope:** Named versions examined in 2017; not proof of code execution,
> current affected status, remediation failure or prevalence outside the sample.
> **As of:** 2017-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §6 `A Deeper Dive` and Figure 5, printed pp. 775–776
> (PDF pp. 12–13).
> **Basis / limits:** Findings and crash outcomes are direct. This synthesis
> intentionally omits tool-specific vulnerable code and input construction.
> Maintainer notification is reported, but patch, CVE and remediation testing
> are not documented.

> **Claim record — SRC-0014-C07 | source-report**
> **Claim:** The authors recommend secure coding/input validation, memory-safe
> implementation or bounds checks, security review, managed patch/authenticity
> practices, sample provenance/custody, risk-aware multiplex separation and
> technical reduction/detection of cross-sample reads.
> **Claim status:** active
> **Scope:** Defensive recommendations derived by the author team; not an
> implementation, safeguard test or effectiveness result.
> **As of:** 2017-08.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** §7.3, printed p. 777 (PDF p. 14).
> **Basis / limits:** Control families are directly recommended. Operational
> configurations and offensive detection-evasion detail are omitted; the paper
> reports no deployed-control population, acceptance metric or independent
> evaluation.

> **Claim record — SRC-0014-C08 | analytic-judgment**
> **Claim:** The artifact supports a controlled biological/input→digital proof
> of concept, an observed cross-sample technical exposure and a version-bounded
> software audit, but not a real-world incident, field exploit, downstream
> privacy/clinical/biological harm, current vulnerability status or control
> effectiveness.
> **Claim status:** active
> **Scope:** Evidence classification after full artifact review; not a claim
> that real incidents, current weaknesses or later replications do not exist.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** full artifact; especially Introduction, §§3, 5–7 and
> Conclusions, printed pp. 765–778 (PDF pp. 2–15).
> **Basis / limits:** The authors explicitly distinguish the modified PoC,
> measured leakage, heuristic audit, controlled crashes, hypothetical threat
> extensions and recommendations. No independent replication or operational
> victim record is part of the source.

## Scope and methods

The proof of concept used one constructed sample, one sequencing run and a
purpose-modified target in a weakened environment. The cross-sample analysis
used demultiplexed results from that run and a second team's sample with
permission. The software study selected 13 open-source C/C++ NGS programs from
six pipeline categories, largely using ecosystem-use criteria, and compared
them with 10 selected Internet-facing C/C++ programs. It counted proxy code
patterns, then applied static analysis/manual review to the NGS group.

The unit of evidence differs across findings: one controlled execution result;
read-level misassignment counts; program-version proxy counts and three crash
demonstrations. None is an observed external incident or a representative
sector survey.

## Limitations and conflicts

- The code-execution target was intentionally modified and common protections
  were disabled. No unmodified production bioinformatics tool was compromised.
- One short construct, one sequencing platform/configuration and one main run
  do not establish external reliability or real-world likelihood.
- Cross-sample measurement is technically observed, but malicious use and
  downstream privacy/integrity consequences are hypotheses.
- The software sample is small, non-random, C/C++-only and frozen to 2017
  versions. A proxy call count is not a vulnerability or exploitability rate.
- Three controlled crashes do not establish arbitrary code execution. The
  source contains no current patch/remediation verification.
- The same team conducted all studies and authored the recommendations; there
  is no independent replication or control-effectiveness evaluation.
- References to biological regulation and external mitigations are background,
  not independently ingested current legal or effectiveness evidence.

## Safety abstraction

The derivative corpus retains system boundaries, experimental classification,
counts, uncertainty and defensive control objectives. It excludes exact DNA,
payload/code, byte representation, construction recipe, target-specific flaw,
crash inputs, adaptation proposals, infrastructure identifiers and operational
attack routes. This omission does not reduce the evidence needed for a safe
reverse-direction cyberbiosecurity model.

## Version status

The artifact is the stable 2017 proceedings version. Current status of the
audited software packages, sequencing configurations and proposed defenses is
not inferred. Later version, replication, patch and deployment evidence must be
ingested independently.

## Integration map

- [SYN-0024 — Cross-sector portfolio reconciliation](../syntheses/syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [AST-0001](../assets/ast-0001-genomic-data.md),
  [WFL-0005](../workflows/wfl-0005-genomic-data-lifecycle.md) and
  [SYS-0003](../systems/sys-0003-genomic-sequencing-analysis-ecosystem.md) — add
  physical-input/read-provenance states and a controlled sequencer→file→
  downstream-processing segment without claiming a production architecture.
- [THR-0001](../threats/thr-0001-adversarial-sequencing-input.md) — generic
  intentional-input threat class without a claimed real actor.
- [HAZ-0001](../hazards/haz-0001-multiplex-sequencing-cross-sample-misassignment.md)
  — measured non-adversarial cross-sample condition.
- [TEC-0001](../techniques/tec-0001-biological-input-to-digital-parser-transfer.md)
  — safe material→measurement→digital-parser transfer abstraction.
- [VUL-0001](../vulnerabilities/vul-0001-unsafe-bioinformatics-input-handling.md)
  — version-bounded unsafe input-handling weakness class.
- [RSK-0009](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md)
  and [RSK-0010](../risk-scenarios/rsk-0010-multiplex-cross-sample-digital-exposure.md)
  — controlled execution and cross-sample exposure paths, neither an `INC`.
- [CTL-0007](../controls/ctl-0007-secure-sequencing-input-processing.md) —
  recommended-only defensive controls and exact edges.
- [SYN-0003](../syntheses/syn-0003-cross-domain-transfer-directions.md) —
  cross-corpus direction and transfer-mechanism reconciliation.
- [RSK-0013](../risk-scenarios/rsk-0013-laboratory-result-disruption-clinical-public-health-decision.md) —
  controlled material/input→digital evidence used only at safe abstraction.
- [SYN-0013](../syntheses/syn-0013-clinical-public-health-testing-lifecycle-reconciliation.md) —
  bounded exposure/reverse-direction evidence, not a clinical incident.
- [SYN-0018](../syntheses/syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md) —
  independent controlled bioinformatics-pipeline and material/input→digital
  evidence; the study is not relabeled as AI or production deployment.
- [SYN-0021 — Genomic asset/lifecycle/system reconciliation](../syntheses/syn-0021-genomic-assets-lifecycle-system-boundary-reconciliation.md)
- [SYN-0022 — Foundational consequence/assurance calibration](../syntheses/syn-0022-foundational-consequence-assurance-calibration.md)
- [SYN-0023 — Transfer-path reconciliation](../syntheses/syn-0023-engineering-biology-and-laboratory-transfer-incident-reconciliation.md)
