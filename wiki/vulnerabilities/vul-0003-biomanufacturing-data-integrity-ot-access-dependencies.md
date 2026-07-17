---
id: VUL-0003
type: vulnerability
title: Biomanufacturing data-integrity and OT access/dependency exposures
aliases:
  - BMO GxP OT exposure classes
  - manufacturing data integrity access supply dependencies
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-07-26
source_ids:
  - SRC-0018
  - SRC-0031
  - SRC-0044
  - SRC-0045
  - SRC-0048
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0044
    claim_id: VUL-0003-C01
    evidence:
      - source: SRC-0044
        locator: "MHRA PDF §§4.1–4.6, 6.15–6.20, printed pp. 5–6 and 15–19"
  - predicate: evidenced-by
    target: SRC-0045
    claim_id: VUL-0003-C01
    evidence:
      - source: SRC-0045
        locator: "NCSC definitive-architecture PDF pp. 3–7, 12–31; secure-connectivity PDF pp. 2–32"
  - predicate: evidenced-by
    target: SRC-0048
    claim_id: VUL-0003-C01
    evidence:
      - source: SRC-0048
        locator: "FDA PDF report pp. 4–13 (physical pp. 8–17), Q1–Q18"
  - predicate: affects
    target: SYS-0002
    claim_id: VUL-0003-C02
    evidence:
      - source: SRC-0044
        locator: "§§6.16 and 6.20, printed pp. 16 and 19"
      - source: SRC-0045
        locator: "Definitive-architecture PDF pp. 3–5, 16–31"
  - predicate: affects
    target: WFL-0003
    claim_id: VUL-0003-C02
    evidence:
      - source: SRC-0044
        locator: "§§4.1–4.6 and 6.15–6.20, printed pp. 5–6 and 15–19"
      - source: SRC-0048
        locator: "FDA Q1–Q18, report pp. 4–13"
  - predicate: enables
    target: RSK-0002
    claim_id: VUL-0003-C03
    evidence:
      - source: SRC-0045
        locator: "Secure-connectivity PDF pp. 5–9 and 20–23"
tags:
  - biomanufacturing
  - operational-technology
  - data-integrity
  - access-control
  - insider-risk
  - supply-chain
  - cloud
  - vulnerability
---

# Biomanufacturing data-integrity and OT access/dependency exposures

## Defensive scope

This page normalizes public regulator and government guidance into defensive
exposure classes. It does not assert that any named manufacturer has one of
these conditions, that a condition is exploitable, or that a recommended
control is implemented or effective.

> **Claim record — VUL-0003-C01 | analytic-judgment**
> **Claim:** Independent MHRA, NCSC and FDA sources directly support a bounded
> BMO-relevant exposure corpus covering non-attributable/shared access and
> administrator conflict, data/audit-trail gaps, transfer or result-
> invalidation risk, legacy/obsolete technology, third-party/supply/vendor,
> cloud/remote and undocumented-connectivity dependencies.
> **Claim status:** active
> **Scope:** Defensive condition classes at GxP-computerized-system and generic
> OT levels; not one facility, product, architecture or exploit chain.
> **As of:** Source states through 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0044](../sources/src-0044-uk-mhra-gxp-data-integrity-guidance-2018-current.md),
> MHRA §§4.1–4.6, 6.15–6.20, printed pp. 5–6 and 15–19;
> [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md),
> definitive-architecture pp. 3–7, 12–31 and secure-connectivity pp. 2–32;
> [SRC-0048](../sources/src-0048-us-fda-drug-cgmp-data-integrity-guidance-2018-current.md),
> FDA Q1–Q18, report pp. 4–13.
> **Basis / limits:** Each class is literal in at least one official source;
> source-specific force, sector scope and recommendation state remain separate.

## Asset and workflow mapping

| Exposure class | Affected class/edge | Consequence state if controls fail |
| --- | --- | --- |
| non-attributable/shared access or administrator conflict | user/admin→GxP record, configuration or audit trail | unauthorized or non-reconstructable change |
| incomplete metadata/audit trail or invalid result handling | raw/process/test data→review/release evidence | unreliable or incomplete quality decision premise |
| transfer/migration/interface weakness | source record/system→downstream application or report | altered, missing or context-stripped data |
| legacy/obsolete component | controller/computerized system→maintenance/connectivity | unpatched, weakly authenticated or fragile dependency |
| vendor, third-party or supply dependency | component/service/update/support→OT/GxP boundary | inherited weakness, unauthorized change or unavailable support |
| cloud/remote/external connectivity | external service/access→OT or regulated data | availability, integrity, ownership, retention or access dependency |
| undocumented assets/connectivity | architecture record→risk/control decision | hidden boundary, incomplete monitoring or unsafe isolation premise |

> **Claim record — VUL-0003-C02 | analytic-judgment**
> **Claim:** These classes map to exact `SYS-0002/WFL-0003` boundaries between
> identity/administration, process/control systems, GxP data and quality review,
> external providers and continuity/recovery decisions.
> **Claim status:** active
> **Scope:** Class-level mapping, not proof of a complete MES/LIMS/QMS/ERP
> topology or a validated deployed boundary.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `VUL-0003-C01`; [SYS-0002](../systems/sys-0002-biomanufacturing-process-control.md);
> [WFL-0003](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md);
> MHRA §§6.16/6.20; FDA Q1–Q18; NCSC architecture/connectivity principles.
> **Basis / limits:** The affected functions and trust relationships are
> direct; the normalized edge labels are editorial.

## Threat, hazard and scenario boundary

> **Claim record — VUL-0003-C03 | analytic-judgment**
> **Claim:** The same exposure can enable deliberate manipulation/outage,
> insider misuse or supply compromise, or contribute to non-adversarial error,
> misconfiguration and recovery failure; trigger and intent must therefore be
> recorded separately in `RSK-0002` or an incident page.
> **Claim status:** active
> **Scope:** Vulnerability/precondition role, not actor attribution,
> vulnerability prevalence, exploitability or occurrence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0044](../sources/src-0044-uk-mhra-gxp-data-integrity-guidance-2018-current.md),
> MHRA §§4.1–4.6, printed pp. 5–6, and §6.16, printed pp. 16–17;
> [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md),
> definitive-architecture pp. 12–15 and 23–31, and secure-connectivity
> pp. 2–9 and 20–23;
> [SRC-0048](../sources/src-0048-us-fda-drug-cgmp-data-integrity-guidance-2018-current.md),
> Background, report pp. 2–3, Q2, report p. 6, Q4–Q5, report p. 7, and
> Q15–Q18, report p. 12.
> **Limits:** Sources distinguish intentional/unintentional changes,
> attacker/insider/supply roles and accidental system/process states.

## Criterion contribution

> **Claim record — VUL-0003-C04 | analytic-judgment**
> **Claim:** Combined with existing NIST OT cyber manipulation/outage and ICH
> Q13 process/quality hazards, this multi-lineage corpus supplies the missing
> insider/supply and concrete-exposure limbs for candidate `BMO-TV` SF2 review.
> **Claim status:** superseded
> **Scope:** Candidate source-floor contribution before `SYN-0028`; no score
> transition by page creation alone.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `VUL-0003-C01`–`C03`;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md);
> [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md); frozen
> `BMO-TV` criterion.
> **Basis / limits:** The independent union covers every literal class; a
> synthesis must still reconcile generic OT and sector-specific applicability.
> **Superseded by:** `SYN-0028-C04`, after strict SF2 threat/exposure
> reconciliation.

> **Claim record — VUL-0003-C05 | analytic-judgment**
> **Claim:** Existing `CTL-0011/CTL-0015` and the FDA/MHRA/NCSC sources map
> architecture, access, integrity review, quality gates, response and recovery
> functions to these exposures, but recommendations and requirements are not
> evidence of implementation or effectiveness.
> **Claim status:** active
> **Scope:** Control relevance and evidence state, not a new control score.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [CTL-0011](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md);
> [CTL-0015](../controls/ctl-0015-continuous-manufacturing-quality-control.md);
> source locators in `VUL-0003-C01`.
> **Basis / limits:** Exact defensive functions exist; no deployed test or
> independent outcome result is added.

## Nonpromotions

> **Claim record — VUL-0003-C06 | analytic-judgment**
> **Claim:** `BMO-SD` remains Partial because the source union still lacks
> literal QMS-as-software and ERP coverage; MHRA's MRP example and
> organizational quality-system language are not substitutes. `BMO-AE`
> remains Absent because no deployed safeguard metric or independent evaluator
> is present.
> **Claim status:** active
> **Scope:** Adjacent-cell audit, not evidence that such systems or evaluations
> do not exist outside the represented corpus.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `VUL-0003-C01`–`C05`; exact `BMO-SD/AE` criteria.
> **Basis / limits:** Literal class and SF3 predicates are conjunctive;
> near-equivalents and recommendations earn no point.

## Safety boundary

This page exposes no manufacturer/facility identity, endpoint, address,
credential, default, vulnerable product/version, exploit, protocol instruction,
attack sequence, process value, recipe or response procedure.

> **Claim record — VUL-0003-C07 | analytic-judgment**
> **Claim:** This page exposes no manufacturer/facility identity, endpoint,
> address, credential, default, vulnerable product/version, exploit, protocol
> instruction, attack sequence, process value, recipe or response procedure.
> **Claim status:** stale
> **Scope:** Local content.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local content and safety abstraction.
> **Limits:** Class-level defensive mapping was sufficient at the stated
> review date. Repository-content assertions can change; this one is retained
> only as a historical safety note, with the current boundary stated in prose
> above.

## Related pages

- [SYS-0002](../systems/sys-0002-biomanufacturing-process-control.md)
- [WFL-0003](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
- [RSK-0002](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [INC-0006](../incidents/inc-0006-merck-notpetya-manufacturing-supply-disruption-2017.md)
- [CTL-0020](../controls/ctl-0020-merck-incident-vendor-update-continuity-recovery-lessons.md)
- [SYN-0028](../syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)

## Sources

- [SRC-0044](../sources/src-0044-uk-mhra-gxp-data-integrity-guidance-2018-current.md)
- [SRC-0045](../sources/src-0045-uk-ncsc-operational-technology-guidance-2024-current.md)
- [SRC-0048](../sources/src-0048-us-fda-drug-cgmp-data-integrity-guidance-2018-current.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md)
