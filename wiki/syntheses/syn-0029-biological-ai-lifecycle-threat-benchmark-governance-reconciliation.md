---
id: SYN-0029
type: synthesis
title: Biological-AI lifecycle, threat, benchmark and governance reconciliation
aliases:
  - AIB residual WL SD TV CI AE GR reconciliation
  - biological AI evidence completion audit
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0005
  - SRC-0006
  - SRC-0014
  - SRC-0016
  - SRC-0017
  - SRC-0033
  - SRC-0034
  - SRC-0038
  - SRC-0049
  - SRC-0050
  - SRC-0051
  - SRC-0052
  - SRC-0053
  - SRC-0054
sensitivity: public
dual_use: low
relations:
  - predicate: depends-on
    target: SYN-0018
    claim_id: SYN-0029-C01
    evidence:
      - source: SRC-0033
        locator: "SYN-0018-C01–C07 prior AIB reconciliation and explicit residuals"
  - predicate: evidenced-by
    target: SRC-0049
    claim_id: SYN-0029-C03
    evidence:
      - source: SRC-0049
        locator: "ETSI EN 304 223 clauses 5.1–5.5, pp. 10–15; ETSI TR §§6.1–6.13, pp. 19–70"
  - predicate: evidenced-by
    target: SRC-0050
    claim_id: SYN-0029-C03
    evidence:
      - source: SRC-0050
        locator: "Results/Figure 2, article pp. 2–4; Discussion p. 7; Methods pp. 8–9"
  - predicate: evidenced-by
    target: SRC-0051
    claim_id: SYN-0029-C04
    evidence:
      - source: SRC-0051
        locator: "§§2.1 and 3.1, Figures 1–2, article pp. 2–3"
  - predicate: evidenced-by
    target: SRC-0052
    claim_id: SYN-0029-C06
    evidence:
      - source: SRC-0052
        locator: "journal pp. 1616–1633, especially pp. 1617–1623 and 1627–1631, Tables/Figures 1–12"
  - predicate: evidenced-by
    target: SRC-0053
    claim_id: SYN-0029-C08
    evidence:
      - source: SRC-0053
        locator: "Regulation (EU) 2024/1689 Arts 2, 6, 8–15, 43, 51–56, 111 and 113; Annex I; current official companions"
  - predicate: evidenced-by
    target: SRC-0054
    claim_id: SYN-0029-C08
    evidence:
      - source: SRC-0054
        locator: "NOT-OD-14-124 §§II–V; NOT-OD-25-081; NOT-OD-26-023 proposal-only status"
  - predicate: depends-on
    target: WFL-0013
    claim_id: SYN-0029-C03
    evidence:
      - source: SRC-0049
        locator: "WFL-0013 complete lifecycle and provenance/reproducibility boundary"
  - predicate: depends-on
    target: SYS-0013
    claim_id: SYN-0029-C04
    evidence:
      - source: SRC-0049
        locator: "SYS-0013 closes package/container/cloud-HPC/API/model-registry/identity and deployed-boundary gaps"
  - predicate: depends-on
    target: SYS-0011
    claim_id: SYN-0029-C04
    evidence:
      - source: SRC-0033
        locator: "SYS-0011-C01–C05 supplies the prior notebook/workbench, database/repository and laboratory-instrument classes"
  - predicate: depends-on
    target: THR-0003
    claim_id: SYN-0029-C05
    evidence:
      - source: SRC-0049
        locator: "THR-0003-C01–C03 intentional actor/action classification"
  - predicate: depends-on
    target: HAZ-0005
    claim_id: SYN-0029-C05
    evidence:
      - source: SRC-0049
        locator: "HAZ-0005-C01–C04 non-adversarial drift/bias/error classification"
  - predicate: depends-on
    target: TEC-0002
    claim_id: SYN-0029-C09
    evidence:
      - source: SRC-0049
        locator: "TEC-0002-C01–C03 abstract method and transfer role"
  - predicate: depends-on
    target: TEC-0003
    claim_id: SYN-0029-C09
    evidence:
      - source: SRC-0038
        locator: "TEC-0003-C01–C03; FBI notification pp. 1–2"
  - predicate: depends-on
    target: VUL-0004
    claim_id: SYN-0029-C05
    evidence:
      - source: SRC-0049
        locator: "VUL-0004-C01–C05 dependency/identity/interface exposure and actual-weakness roles"
  - predicate: depends-on
    target: CTL-0021
    claim_id: SYN-0029-C03
    evidence:
      - source: SRC-0049
        locator: "CTL-0021-C01–C08 exact-edge lifecycle controls and evidence-state limits"
  - predicate: governed-by
    target: GOV-0024
    claim_id: SYN-0029-C08
    evidence:
      - source: SRC-0049
        locator: "ETSI EN/TR force, scope and lifecycle roles"
  - predicate: governed-by
    target: GOV-0025
    claim_id: SYN-0029-C08
    evidence:
      - source: SRC-0053
        locator: "EU AI Act applicability, application dates and exceptions"
  - predicate: governed-by
    target: GOV-0026
    claim_id: SYN-0029-C08
    evidence:
      - source: SRC-0054
        locator: "NIH genomic-data and AI-use policy scope and exceptions"
tags:
  - artificial-intelligence
  - biological-models
  - lifecycle
  - mlops
  - threat-taxonomy
  - benchmark
  - governance
  - reconciliation
---

# Biological-AI lifecycle, threat, benchmark and governance reconciliation

## Decision scope and frozen method

This synthesis adjudicates the six residual AIB cells and the two exact
cross-cutting taxonomy cells directly affected by the new canonical graph:
`AIB-WL/SD/TV/CI/AE/GR`, `FND-TV` and `THI-TV`. The frozen wording, source
floors and anti-duplication rules in `SYN-0001` are unchanged.

> **Claim record — SYN-0029-C01 | artifact-observation**
> **Claim:** Before this transaction the recalculated public wiki has 78 Pass,
> 29 Partial and 3 Absent cells = 78/110 (70.9%), AIB is 4/10, FND 9/10 and
> THI 2/10, with 66/24/1 critical cells, 2/11 dimensions at least 9/10 and global
> gates at 7 Pass/5 Fail.
> **Claim status:** active
> **Scope:** Wiki after `SYN-0028` and before this transaction; not absolute
> domain completeness.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SYN-0001](syn-0001-coverage-rubric.md), checkpoint
> `SYN-0001-C50`; [SYN-0018](syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md).
> **Basis / limits:** This is reproducible artifact state only.

## Evidence roles and independence

| Lineage | Direct role | Independence/limit |
| --- | --- | --- |
| NASEM (`SRC-0033`) | biology-specific scope, assets, DBTL, threats and recommended controls | one U.S. consensus-report line; advisory and not a deployment |
| ETSI (`SRC-0049`) | current complete lifecycle, dependencies, threat/monitoring and retirement requirements/examples | EN+TR+work-item records are one standards lineage |
| Stetson oncology (`SRC-0050`) | named production governance, registry, monitoring, reviews and model sunset | one institution/author evaluation; no patient-outcome comparator |
| mlf-core (`SRC-0051`) | direct biomedical package/container/registry/environment implementation context | research framework, not a security/effectiveness audit |
| ProteinGym (`SRC-0034`) | primary protein-fitness benchmark with split/task/metric failure limits | developer/evaluator overlap and one benchmark line |
| CASP15 (`SRC-0052`) | independent blind structure assessment and measured molecular-replacement outcome | different task/corpus; not ProteinGym replication or deployment |
| EU/NIH/ETSI plus existing EHDS/FDA | current law/policy/standard applicability | force, actor, date and exception differences preserved |

> **Claim record — SYN-0029-C02 | analytic-judgment**
> **Claim:** The listed lineages are materially independent only for their
> assigned claims: ETSI companions, Commission companions, NIH notices and
> CASP administrative artifacts are each kept within their parent lineage,
> while CASP15 and ProteinGym are independent benchmark lines with different
> authors, tasks, corpora, metrics and experimental truth.
> **Claim status:** active
> **Scope:** Claim-specific SF2/SF3 accounting; not equal evidentiary weight or
> universal institutional independence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0049-C01`; `SRC-0050-C01`; `SRC-0051-C01`;
> `SRC-0052-C01/C02`; `SRC-0053-C01`; `SRC-0054-C01`; existing
> `SRC-0033-C01/C02` and `SRC-0034-C01/C02`.
> **Basis / limits:** Source identities, authorship, genres, methods and
> programme boundaries are direct. A wrapper or guidance companion is not
> multiplied into corroboration.

## AIB decisions

### Complete lifecycle — `AIB-WL`

> **Claim record — SYN-0029-C03 | analytic-judgment**
> **Claim:** `AIB-WL` passes at SF2: NASEM supplies biology-specific
> acquisition/curation, analysis/training, validation, provenance,
> reproducibility and DBTL/action boundaries; independent ETSI plus direct
> oncology evidence complete deployment/inference, monitoring/update and
> retirement without treating the union as one universal deployment.
> **Claim status:** active
> **Scope:** Complete criterion-level lifecycle coverage; not proof of one
> end-to-end implementation, safe outcome or universal phase order.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [WFL-0013](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md);
> `SRC-0033-C04/C07`; `SRC-0049` lifecycle claims; `SRC-0050` production,
> monitoring and sunset claims; [CTL-0021](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md).
> **Basis / limits:** Every literal stage has direct located support and the
> two core lineages are independent. Stetson strengthens implementation reality
> but remains one programme.

### Systems and trust boundaries — `AIB-SD`

> **Claim record — SYN-0029-C04 | analytic-judgment**
> **Claim:** `AIB-SD` passes at SF2: `SYS-0011` supplies notebooks/
> workbenches, databases/repositories and instruments; `SYS-0013` adds
> packages, containers, cloud/HPC, APIs, model registries, identity and
> deployed boundaries. Together they reconcile the frozen map across NASEM,
> ETSI and direct biomedical-MLOps evidence.
> **Claim status:** active
> **Scope:** Component/boundary taxonomy; not a named validated topology,
> complete inventory, secure configuration or adoption census.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SYS-0013](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md);
> [SYS-0011](../systems/sys-0011-biological-ai-data-compute-model-laboratory-ecosystem.md);
> `SRC-0033-C05`; ETSI EN clauses 5.1.2–5.2.4 and TR §§6.2/6.5/6.6;
> [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md),
> §§2.1/3.1 and Figures 1–2.
> **Basis / limits:** All literals are direct in the independent union. The
> TR's literal container/registry examples are informative; mlf-core provides
> an independent direct biomedical implementation context.

### Threat/hazard/technique/vulnerability corpus — `AIB-TV`

> **Claim record — SYN-0029-C05 | analytic-judgment**
> **Claim:** `AIB-TV` passes at SF2: `THR-0003`, `TEC-0002`, `VUL-0004` and
> `HAZ-0005` distinguish poisoning/tampering/confidentiality leakage,
> software/model dependencies, bias/drift/error and unsafe automation across
> independent ETSI and biology-specific NASEM roles, with Stetson/CASP bounded
> implementation and failure observations.
> **Claim status:** active
> **Scope:** Safe defensive taxonomy; not exploitability, incidence,
> prevalence, biological targeting or control effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [THR-0003](../threats/thr-0003-adversarial-ai-data-model-and-interface-actions.md);
> [TEC-0002](../techniques/tec-0002-ai-data-model-manipulation-and-extraction.md);
> [VUL-0004](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md);
> [HAZ-0005](../hazards/haz-0005-biological-ai-drift-bias-and-error.md); direct
> underlying routes: [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> EN Introduction p. 5, clauses 5.1.2–5.1.4, pp. 10–11, 5.2.1–5.2.5,
> pp. 12–14, and 5.4.2, p. 15, plus TR threat overview pp. 15–16,
> clauses 6.2.5–6.2.8, pp. 25–28, 6.4.1–6.4.3, pp. 33–35, and
> 6.12.2–6.12.4, pp. 67–69; [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapters 2–3, printed pp. 21–37 (physical pp. 42–58), Chapter 5,
> printed pp. 64–81 (physical pp. 85–102), and Appendix A, printed
> pp. 115–124 (physical pp. 136–145); [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md),
> Results and Figure 2, pp. 2–4, Discussion p. 7 and Methods pp. 8–10; and
> [SRC-0052](../sources/src-0052-casp15-tertiary-structure-assessment-2023.md),
> Results and Figures 2–5, journal pp. 1621–1624, and Figures 6–8,
> pp. 1624–1628.
> **Limits:** Every literal and ontology role has direct evidence. The
> graph keeps actor, method, weakness and non-adversarial trigger separate.

### Measured research consequence — `AIB-CI`

> **Claim record — SYN-0029-C06 | analytic-judgment**
> **Claim:** `AIB-CI` passes at SF3, bounded to research consequence: CASP15
> states model/target scope and directly measures success/failure in using
> submitted structure predictions for experimental molecular replacement,
> including the T1145 outcome, while independent ProteinGym supplies a
> different scoped empirical biological-model benchmark context.
> **Claim status:** active
> **Scope:** Protein-model research workflow; not an incident, privacy loss,
> patient outcome, organism harm/benefit, deployment or cyber robustness.
> **As of:** CASP15/ProteinGym publications through 2023.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0052](../sources/src-0052-casp15-tertiary-structure-assessment-2023.md),
> journal pp. 1617–1619 and 1627–1631, Figures 9–11; especially T1145 on
> p. 1630; [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md),
> `SRC-0034-C03`–`C08`.
> **Basis / limits:** CASP provides a direct observed downstream research
> result and the two primary lineages are materially independent. This does
> not broaden “research consequence” into clinical or biological harm.

### Independent benchmark assurance — `AIB-AE`

> **Claim record — SYN-0029-C07 | analytic-judgment**
> **Claim:** `AIB-AE` passes at SF3: ProteinGym and independent assessor-led
> CASP15 test different biological-model tasks with explicit data/model scope,
> metrics, stratified generalizability and positive plus failure/null limits;
> CASP's withheld experimental structures and molecular-replacement tests add
> independent effectiveness evidence for the bounded research task.
> **Claim status:** active
> **Scope:** Protein fitness and tertiary-structure benchmark assurance; not
> control-family effectiveness, production monitoring, clinical validation or
> independent reproduction of either benchmark's exact scores.
> **As of:** 2023 benchmark publications.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0034-C03`–`C08`; `SRC-0052-C02`–`C08`; CASP15 journal
> pp. 1616–1633, Figures 1–12 and Table 1.
> **Basis / limits:** No author overlap, different governance/tasks/corpora and
> blind experimental targets establish material independence. CASP is not
> organizationally independent of its own assessor process and is not a
> ProteinGym replication.

### Current multi-jurisdiction governance — `AIB-GR`

| Category | Jurisdiction/instrument | Force | Application/adoption state | Main boundary or exception |
| --- | --- | --- | --- | --- |
| AI systems and GPAI | EU AI Act, Regulation (EU) 2024/1689 | binding EU law | in force; provision-specific staged application; pending Omnibus dates not operative at cutoff | sole-purpose scientific R&D and pre-market activity exclusions are bounded; real-world testing and retained data law remain |
| Health/omics data and AI training | EU EHDS, Regulation (EU) 2025/327 | binding EU law | in force with 2027/2029/2031/2035 staged application | purpose/role/stage-specific opt-out, public-interest and national-safeguard conditions; secure-environment and prohibited-use boundaries |
| Genomic research and controlled-data generative AI | U.S. NIH GDS/DUC notices | conditional award/contract/intramural and data-use policy | base policy effective since 2015; generative-AI clarification current; later RFI is proposal only | NIH-supported/controlled-access scope, consent/scale exceptions, approved use/collaborators and closeout limits |
| AI/medical-device and IVD | EU AI Act plus MDR/IVDR trigger; U.S. FDA device cybersecurity guidance | EU law plus U.S. nonbinding guidance/cited statutory duties | EU product high-risk date remains base 2027-08-02 at cutoff; FDA 2026 guidance current | EU requires product/safety-component plus third-party assessment; in-house and research contexts are conditional; guidance is not approval |
| Cross-sector AI cybersecurity | ETSI EN 304 223 | normative voluntary European standard | current published EN; organization/national adoption and conformance unknown | research-only systems not intended for deployment excluded; TR is informative and predecessor-TS-bound |

> **Claim record — SYN-0029-C08 | analytic-judgment**
> **Claim:** `AIB-GR` passes at SF2: current EU AI Act/EHDS, U.S. NIH genomic-
> data policy and FDA medical-device roles, plus the ETSI European standard, are
> reconciled across AI, data, genomic/research and medical-device categories
> for jurisdiction, force, application dates, scientific-R&D/device triggers,
> controlled-data scope, exceptions and unknown organization-level adoption.
> **Claim status:** active
> **Scope:** Applicability/status map through 2026-07-12; not legal advice,
> global equivalence, compliance or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-02.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [GOV-0024](../governance/gov-0024-etsi-european-ai-cybersecurity-standard.md);
> [GOV-0025](../governance/gov-0025-eu-ai-act-life-sciences-applicability.md);
> [GOV-0026](../governance/gov-0026-nih-genomic-data-ai-use-policy.md);
> [GOV-0006](../governance/gov-0006-eu-ehds-regulation-2025.md);
> [GOV-0007](../governance/gov-0007-us-fda-medical-device-cybersecurity-2026.md);
> direct underlying routes: [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md),
> EN Foreword p. 4, Scope p. 6 and clauses 5.1–5.5, pp. 10–15;
> [SRC-0053](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md),
> AI Act Articles 2(1), 2(6)–(8) and 2(12), Official Journal PDF
> pp. 45–46, Article 6(1), p. 53, Articles 8–15, pp. 55–61, Article
> 43(3), p. 78, Articles 51, 53, 55–56 and 111(3), pp. 83–87 and 121,
> Annex I, p. 124, and Article 113, p. 123; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> Articles 1–2, PDF pp. 29–33, Article 51, pp. 57–58, Articles 53–54
> and 67–71, pp. 59–60 and 69–74, and Article 105, pp. 90–91;
> [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md),
> `NOT-OD-14-124` §§II–V, `NOT-OD-25-081` Purpose and interim-condition
> paragraphs, and `NOT-OD-26-023` title, Purpose, Draft Policy, Proposed
> Revisions and Request for Input; and [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§I–III, printed pp. 1–3 (PDF pp. 5–7), and §VII.A–C, printed
> pp. 31–34 (PDF pp. 35–38).
> **Limits:** Binding law, funding/data-use policy, medical-device
> statute/guidance and voluntary standard are distinct. The adopted EU
> Omnibus amendment remains non-operative until OJ publication/entry into
> force and therefore does not replace base AI Act dates at this cutoff.

## Cross-cutting canonical taxonomy

| Sector | Intentional threat/actor | Non-adversarial hazard | Method/technique | Weakness versus exposure state |
| --- | --- | --- | --- | --- |
| GEN | `THR-0001` | `HAZ-0001` | `TEC-0001` | `VUL-0001`; version-bounded controlled evidence, not a current field exposure census |
| AGE | `THR-0002` | `HAZ-0003/0004` | `TEC-0003` | `VUL-0002`; source-reported aggregate exposure classes, named/current-instance state unknown |
| AIB | `THR-0003` | `HAZ-0005` | `TEC-0002` | `VUL-0004-C05`; generic deficient dependency/identity/separation/transfer states, named-instance exposure unknown |

`VUL` records a weakness or dependency condition. “Exposure” is a state in
which that condition is actually reachable/applicable; it remains unknown
unless a source locates it in a bounded instance. The table therefore does not
turn a generic weakness class into a finding about a current system.

> **Claim record — SYN-0029-C09 | analytic-judgment**
> **Claim:** `FND-TV` and `THI-TV` pass at SF2: substantive canonical
> `THR/HAZ/TEC/VUL` pages now distinguish actor/event, non-adversarial trigger,
> method and weakness with typed edges across GEN, AGE and AIB sectors, and the
> AIB graph independently reproduces the exact four-role separation beyond
> the original USENIX lineage.
> **Claim status:** active
> **Scope:** Corpus ontology and evidence backing; not threat completeness,
> incidence, likelihood or a universal taxonomy mandate.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `THR-0001`–`THR-0003`; `HAZ-0001`–`HAZ-0005`;
> `TEC-0001`–`TEC-0003`; `VUL-0001`–`VUL-0004`, including
> `VUL-0004-C05` and page-level instance-status boundaries; independent `SRC-0014`,
> `SRC-0033`, `SRC-0038` and `SRC-0049` roles; exact typed relations.
> **Basis / limits:** Three sectors and materially independent lineages are
> represented. Canonical labels do not turn hypotheses or hazards into
> incidents.

## Nonpromotions and scoring

> **Claim record — SYN-0029-C10 | analytic-judgment**
> **Claim:** No incident count, global directionality, cross-sector safeguard-
> effectiveness or governance-enforcement gate changes: CASP is an empirical
> study rather than an incident; Stetson is not an independent patient-outcome
> evaluation; standards and policy issuance are not adoption/effectiveness.
> **Claim status:** stale
> **Scope:** Adjacent-cell and global-gate boundaries.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Exact frozen `THI-WL/XT/CI`, `CTR-AE`, `GOV-CI/AE` and global
> gate criteria; source limitations above.
> **Limits:** Related evidence is not promoted across a different required
> evidence type. This is a dated local rubric/non-promotion decision rather
> than an externally evidenced substantive claim; it is retained as historical
> context but is no longer maintained as active evidence.

> **Claim record — SYN-0029-C11 | artifact-observation**
> **Claim:** Exactly eight Partial→Pass transitions are accepted:
> `AIB-WL/SD/TV/CI/AE/GR`, `FND-TV` and `THI-TV`. Totals become 86 Pass, 21
> Partial and 3 Absent = 86/110 (78.2%); the dimension vector becomes
> `10/8/5/8/8/8/10/10/3/8/8`, critical cells 73/17/1, dimensions at least
> 9/10 become 3/11 and global gates remain 7 Pass/5 Fail.
> **Claim status:** active
> **Scope:** Frozen rubric v1.0 after activation and full clean lint of this
> transaction; not ≥90% certification because numeric, per-dimension and
> global gates remain unmet.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SYN-0029-C01`–`C10`; exact frozen cells and their cited local
> pages. The internal lint transcript is not included in the public derivative.
> **Basis / limits:** Partial/Absent both remain zero points. This claim becomes
> valid only with zero-error lint and independent decision review.

## Related pages

- [SYN-0001 — Coverage rubric](syn-0001-coverage-rubric.md)
- [SYN-0018 — Prior AIB reconciliation](syn-0018-ai-enabled-life-science-scope-asset-transfer-control-reconciliation.md)
- [WFL-0013 — Secure model lifecycle](../workflows/wfl-0013-biological-ai-secure-model-lifecycle.md)
- [SYS-0013 — Biological MLOps boundaries](../systems/sys-0013-biological-mlops-infrastructure-trust-boundaries.md)
- [THR-0003 — Adversarial AI threat](../threats/thr-0003-adversarial-ai-data-model-and-interface-actions.md)
- [HAZ-0005 — Drift/bias/error hazard](../hazards/haz-0005-biological-ai-drift-bias-and-error.md)
- [TEC-0002 — High-level transfer techniques](../techniques/tec-0002-ai-data-model-manipulation-and-extraction.md)
- [TEC-0003 — Agriculture ransomware method](../techniques/tec-0003-ransomware-availability-and-extortion-agriculture.md)
- [VUL-0004 — AI exposure classes](../vulnerabilities/vul-0004-biological-ai-dependency-identity-and-data-exposures.md)
- [CTL-0021 — Secure monitored controls](../controls/ctl-0021-secure-monitored-biological-ai-lifecycle-controls.md)
- [GOV-0024 — ETSI European standard](../governance/gov-0024-etsi-european-ai-cybersecurity-standard.md)
- [GOV-0025 — EU AI Act](../governance/gov-0025-eu-ai-act-life-sciences-applicability.md)
- [GOV-0026 — NIH genomic AI policy](../governance/gov-0026-nih-genomic-data-ai-use-policy.md)
- [SRC-0034 — ProteinGym](../sources/src-0034-notin-proteingym-benchmark-2023.md)
- [SRC-0052 — CASP15](../sources/src-0052-casp15-tertiary-structure-assessment-2023.md)

## Sources

- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md).
- [SRC-0034](../sources/src-0034-notin-proteingym-benchmark-2023.md).
- [SRC-0049](../sources/src-0049-etsi-european-ai-cybersecurity-standard-implementation.md).
- [SRC-0050](../sources/src-0050-stetson-responsible-ai-governance-oncology-2025.md).
- [SRC-0051](../sources/src-0051-mlf-core-reproducible-biomedical-mlops-2023.md).
- [SRC-0052](../sources/src-0052-casp15-tertiary-structure-assessment-2023.md).
- [SRC-0053](../sources/src-0053-eu-ai-act-life-sciences-current-2026.md).
- [SRC-0054](../sources/src-0054-nih-genomic-data-ai-policy-current-2025.md).
