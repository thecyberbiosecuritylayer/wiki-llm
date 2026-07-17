---
id: SYN-0003
type: synthesis
title: Cyber-biological transfer directions and mechanisms
aliases:
  - cross-domain transfer synthesis
  - cyber to bio and bio input to digital map
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0003
  - SRC-0004
  - SRC-0005
  - SRC-0006
  - SRC-0008
  - SRC-0009
  - SRC-0011
  - SRC-0012
  - SRC-0014
  - SRC-0057
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0003
    claim_id: SYN-0003-C01
    evidence:
      - source: SRC-0003
        locator: "§ Digital Information Flow in Biomanufacturing; Figure 1"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: SYN-0003-C01
    evidence:
      - source: SRC-0005
        locator: "§§2.1–2.5 and 3.1–3.5, printed pp. 3–11 (PDF pp. 12–20)"
      - source: SRC-0006
        locator: "§§1.2–2.2.1 and 5.1–5.6, printed pp. 4–11 and 22–25 (PDF pp. 15–22 and 33–36)"
  - predicate: evidenced-by
    target: SRC-0009
    claim_id: SYN-0003-C02
    evidence:
      - source: SRC-0008
        locator: "pp. 21–22 and 97"
      - source: SRC-0009
        locator: "article chronology/status sections; HTML lines 190–200"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: SYN-0003-C01
    evidence:
      - source: SRC-0011
        locator: "§§I–V, printed pp. 4–13 (PDF pp. 5–14)"
      - source: SRC-0012
        locator: "screening lifecycle sections, HTML lines 833–1070"
  - predicate: evidenced-by
    target: SRC-0014
    claim_id: SYN-0003-C02
    evidence:
      - source: SRC-0014
        locator: "Introduction and §§3, 5–6, printed pp. 765–776 (PDF pp. 2–13)"
  - predicate: evidenced-by
    target: SRC-0057
    claim_id: SYN-0003-C05
    evidence:
      - source: SRC-0057
        locator: "SUI Executive summary ¶¶3–5; §2.6.7 printed p. 45; §3.1.1 p. 51; UKHSA preprint Introduction/Methods p. 2"
tags:
  - foundations
  - cross-domain-transfer
  - cyber-to-biological
  - biological-to-digital
  - privacy-without-cyber
  - directionality
---

# Cyber-biological transfer directions and mechanisms

## Canonical boundary

A cross-domain path in this wiki is not merely the adjacency of biology and IT.
It requires a source-backed origin state, transfer mechanism, receiving state,
consequence, and evidence boundary. The direction may be
digital/cyber→biological, biological/material/input→digital, or digital
processing→human privacy without a cyber incident.

## Five transfer mechanisms

| Mechanism | What crosses the boundary | Located corpus example | Evidence state |
| --- | --- | --- | --- |
| Data | sequence, annotation, result or provenance state changes what downstream analysis/decision receives | `RSK-0003` genomic integrity→decision | hypothetical NIST path |
| Control | digital measurement/command state changes a physical process or product/supply state | `RSK-0002` biomanufacturing control→process/product | hypothetical scholarly model |
| Custody | accountable possession/association of material, sample or record changes across people/organizations/stages | `WFL-0004` high-consequence material lifecycle | normative WHO objective, not event |
| Decision | screened/reviewed digital state gates physical fulfillment, refusal, reporting or equipment access | `RSK-0008` synthesis order decision→physical fulfillment | hypothetical path from independent US/UK instruments |
| Material/input | physical material is measured and becomes digital data interpreted by software or a decision workflow | `RSK-0009/0010/0021` sequencing input→execution/file state and test input→digital result/decision | controlled/observed technical plus primary incident evidence |

> **Claim record — SYN-0003-C01 | analytic-judgment**
> **Claim:** Independent corpus lineages support five distinct transfer
> mechanisms—data, control, custody, decision and material/input—with located
> examples whose observed, controlled, normative and hypothetical states remain
> explicit.
> **Claim status:** active
> **Scope:** Canonical defensive taxonomy for the current wiki corpus; not a
> claim that every mechanism occurs in every sector or has equal likelihood.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> § Digital Information Flow and Figure 1;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> Chapters 2–4, pp. 10–57;
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§2.1–2.5 and 3.1–3.5;
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§1.2–2.2.1 and 5.1–5.6;
> [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md), §§I–V;
> [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> HTML lines 833–1070;
> [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md), §§2–6.
> **Basis / limits:** Each source directly supports its bounded transition.
> The taxonomy is wiki synthesis; it does not turn normative or hypothetical
> paths into observed events, and source IDs from one programme are not counted
> as independent lineages.

## Three direction classes

### Cyber/digital → biological, clinical or supply state

The Synnovis event is the corpus's primary observed example: an official NHS
incident update classifies ransomware and service disruption, while NHSBT
records downstream transfusion compatibility-testing disruption, constrained
blood-product availability and continuity response. The two organizational
records describe roles in one event and are not counted as two independent
incidents. Actor, initial access, vulnerability and patient injury remain
unknown.

### Biological/material/input → digital state

`SRC-0014` provides two direct technical paths: a deliberately constructed
input reached code execution in an artificial target, and cross-sample reads
changed file provenance in one multiplex run. The former is a controlled PoC;
the latter is observed technical exposure. Neither is a field incident or
downstream clinical/biological harm. `SRC-0057/INC-0008/RSK-0021` now add a
primary non-malicious incident path from biological test input through
configured classification to a digital result and the positive-result
notification/contact-tracing decision boundary; individual behavior and
population outcomes remain unobserved/modelled as stated on those pages.

### Privacy impact without cyber compromise

NIST's genomic privacy model explicitly permits privacy problems from
technically authorized processing. `RSK-0005` therefore stays separate from
unauthorized disclosure and from cross-domain material/input paths.

> **Claim record — SYN-0003-C02 | analytic-judgment**
> **Claim:** The corpus now contains complete, separately classified examples
> of cyber/digital→biological/clinical continuity, biological/material/input→
> digital state, and privacy harm without a cyber compromise.
> **Claim status:** superseded
> **Scope:** Directional completeness at safe abstraction; not equal evidence
> maturity, causal generalization or satisfaction of the global incident gate.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md),
> pp. 21–22 and 97; [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> article chronology/status sections, HTML lines 190–200;
> [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> Introduction and §§3, 5–6;
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§2.2–2.2.1 and Figures 2–3, printed pp. 9–11 (PDF pp. 20–22).
> **Basis / limits:** Each direction has an end-to-end state transition, but
> evidence classes differ: one operational event lineage, one controlled/
> technical study lineage and one normative privacy model. This does not make
> the USENIX PoC an incident or provide a biological→digital *decision* outcome
> required by the stricter global directionality gate.
> **Superseded by:** `SYN-0003-C05`, after `SRC-0057/INC-0008/RSK-0021`
> supplied the missing primary incident input→digital-decision outcome.

## Genomic scenario set

The genomic/omics direction set now includes:

- [RSK-0003](../risk-scenarios/rsk-0003-genomic-data-integrity-decision-harm.md) —
  altered genomic/analysis state→downstream decision and possible harm;
- [RSK-0004](../risk-scenarios/rsk-0004-genomic-data-disclosure-kin-privacy.md) —
  unauthorized disclosure/linkage→individual/kin privacy consequences;
- [RSK-0005](../risk-scenarios/rsk-0005-permitted-genomic-processing-privacy-harm.md)
  — technically authorized processing→privacy problem without cyber incident;
- [RSK-0009](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md) —
  controlled biological input→digital execution; and
- [RSK-0010](../risk-scenarios/rsk-0010-multiplex-cross-sample-digital-exposure.md)
  — observed technical material/run→digital provenance exposure.

> **Claim record — SYN-0003-C03 | analytic-judgment**
> **Claim:** Across independent NIST/NCCoE and University of Washington
> lineages, at least three full genomic risk scenarios cover integrity→decision,
> disclosure/permitted-processing privacy and biological/sample-input→digital
> analysis directions with conflicts and evidence maturity explicitly bounded.
> **Claim status:** active
> **Scope:** Corpus acceptance basis for `GEN-XT`; not incident or likelihood
> evidence and not a claim that all omics classes are covered.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§1.1–4.4.2; [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§1.2–2.2.1 and 5.1–5.6;
> [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> Introduction and §§3, 5–6; linked full RSK claims.
> **Basis / limits:** NIST supports the first two direction classes; USENIX
> independently supplies reverse material/input paths. NIST IDs share one
> programme lineage, USENIX experiments share one author lineage, and none of
> the hypothetical downstream harms becomes observed.

## Threat–hazard–technique–vulnerability distinction

For the reverse sequencing path, the graph keeps four roles separate:

| Type | Page | Role |
| --- | --- | --- |
| Threat | `THR-0001` | intentional actor/event class, currently hypothetical outside the PoC |
| Hazard | `HAZ-0001` | non-adversarial cross-sample condition, technically observed |
| Technique | `TEC-0001` | material→measurement→digital-parser transfer method |
| Vulnerability | `VUL-0001` | unsafe input/memory handling weakness, historical/version-bounded |

Typed relations connect the threat to the method, the method to the weakness
and controlled scenario, and the hazard to the separate exposure scenario.
They are not interchangeable labels.

> **Claim record — SYN-0003-C04 | analytic-judgment**
> **Claim:** The canonical reverse-path graph distinguishes intentional threat,
> non-adversarial hazard, transfer technique and software weakness with typed
> edges, while independent NIST genomic threat/integrity modeling supplies a
> second claim-appropriate lineage for the wider genomic threat corpus.
> **Claim status:** active
> **Scope:** Ontology and evidence-lineage reconciliation supporting `GEN-TV`;
> not independent SF2 support for the exact four-role `THI-TV` taxonomy.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** medium
> **Evidence:** [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> Introduction and §§3, 5–7;
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§1.1, 3.1–3.5 and 4.4.2;
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§2.1–2.2.1 and 5.1.
> **Basis / limits:** USENIX supports the concrete reverse-path roles and NIST
> independently supports genomic threat/integrity/privacy distinctions. The
> NIST lineage does not independently reproduce the four-role graph. The source
> sets do not establish actor prevalence, current vulnerable versions or an SF2
> cross-sector `THR/HAZ/TEC/VUL` taxonomy by themselves; `THI-TV` later passes
> independently through `SYN-0029-C09`, not through this GEN-scoped claim.

## Control interruption

[CTL-0007](../controls/ctl-0007-secure-sequencing-input-processing.md) maps
prevention, detection, containment and recovery to `RSK-0009/0010` using
independent USENIX and NIST lineages. It remains recommended-only. Existing
sector controls map other directions; this page never treats a mapped control
as implemented or effective.

## Evidence ladder and remaining gates

- observed operational: Synnovis disruption/continuity lineage;
- controlled empirical: USENIX reverse execution and read-misassignment study;
- observed technical, no downstream harm: cross-sample reads;
- normative: WHO custody and US/UK screening decisions;
- hypothetical/analytical: genomic integrity/privacy and manufacturing paths;
- implemented/tested/effective/independently evaluated: unresolved except
  separately scoped incident-response implementation already recorded.

The global directionality gate now passes because the prior corroborated
cyber→biological corpus is joined by the primary Immensa biological/material/
input→digital-result→decision path. This does not make the reverse incident
malicious, establish individual behavior or turn modelled population effects
into observations. The numeric, risk-chain and control-effectiveness gates
remain failed for their own independent criteria.

> **Claim record — SYN-0003-C05 | analytic-judgment**
> **Claim:** The corpus now satisfies the global directionality contract: its
> independent primary cyber→biological/operational paths remain intact, and
> the Immensa incident adds the previously missing primary biological test-
> input→configured classification→digital-result→positive-result notification/
> contact-tracing decision path, while privacy-without-cyber remains separate.
> **Claim status:** active
> **Scope:** Global directional existence at safe abstraction; not universal
> bidirectionality, malicious reverse transfer, person-level behavior,
> incidence, causally observed population harm or control effectiveness.
> **As of:** Corpus reconciled 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Cyber→biological/operational direction:
> [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 21–22 and
> 97, and [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md),
> update paragraphs 2–4. Primary reverse direction:
> [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md),
> SUI Executive summary ¶¶3–5, §2.6.7 printed p. 45 and §3.1.1 p. 51;
> UKHSA preprint Introduction/Methods, p. 2. Privacy boundary:
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§2.2–2.2.1 and Figures 2–3. [INC-0008](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md),
> [RSK-0021](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)
> and [SYN-0031](syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)
> are canonical navigation/reconciliation, not independent evidence.
> **Basis / limits:** Each required direction has direct located evidence and
> remains independently classified. The reverse path is observed through the
> digital result/notification decision node; individual actions and downstream
> population effects retain their unknown/modelled states.

## Safety boundary

The synthesis contains only direction, mechanism, evidence class and defensive
control edges. It omits exploit construction, sequence/payload/code,
screening-evasion, re-identification methods, target-specific weaknesses,
facility topology and harmful production detail.

## Related pages

- [CON-0001](../concepts/con-0001-cyberbiosecurity.md)
- [SYN-0001](syn-0001-coverage-rubric.md)
- [RSK-0006](../risk-scenarios/rsk-0006-transfusion-testing-disruption-supply-pressure.md)
- [RSK-0009](../risk-scenarios/rsk-0009-sequenced-input-to-digital-execution.md)
- [RSK-0010](../risk-scenarios/rsk-0010-multiplex-cross-sample-digital-exposure.md)
- [INC-0008](../incidents/inc-0008-immensa-pcr-false-negative-reporting-2021.md)
- [RSK-0021](../risk-scenarios/rsk-0021-biological-test-input-to-digital-result-public-health-action.md)
- [CTL-0007](../controls/ctl-0007-secure-sequencing-input-processing.md)
- [SYN-0031](syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)

## Sources

- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md).
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md).
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md).
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md).
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md).
- [SRC-0009](../sources/src-0009-nhs-england-synnovis-update-2025.md).
- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md).
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md).
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md).
- [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md).
