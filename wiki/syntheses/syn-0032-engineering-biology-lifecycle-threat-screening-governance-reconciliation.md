---
id: SYN-0032
type: synthesis
title: Engineering-biology lifecycle, threat, screening and governance reconciliation
aliases:
  - SEB lifecycle threat consequence assurance governance audit
  - NIST HHS SecureDNA engineering-biology reconciliation
status: active
created: 2026-07-13
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-07-27
source_ids:
  - SRC-0004
  - SRC-0011
  - SRC-0012
  - SRC-0013
  - SRC-0033
  - SRC-0059
  - SRC-0060
  - SRC-0061
sensitivity: public
dual_use: moderate
relations:
  - predicate: depends-on
    target: WFL-0014
    claim_id: SYN-0032-C03
    evidence:
      - source: SRC-0033
        locator: "Summary and Chapters 2–5 for design/DBTL boundaries"
      - source: SRC-0011
        locator: "2024 OSTP Framework §§I–V, printed pp. 4–13"
      - source: SRC-0012
        locator: "UK guidance actor, order, screen, review, decision, record and transfer sections, HTML lines 708–1070"
      - source: SRC-0004
        locator: "WHO §§1.1–1.2 and 6.3–7.3.5, printed pp. 2–3 and 31–44"
  - predicate: depends-on
    target: THR-0006
    claim_id: SYN-0032-C04
    evidence:
      - source: SRC-0004
        locator: "WHO §§3.2, 5.1, 5.3 and 6.1"
      - source: SRC-0033
        locator: "NASEM Chapters 2–5"
      - source: SRC-0012
        locator: "UK screening/process-integrity and provider/vendor/equipment responsibilities"
  - predicate: depends-on
    target: HAZ-0007
    claim_id: SYN-0032-C04
    evidence:
      - source: SRC-0059
        locator: "Blinded benchmark Results and disagreement analysis, physical pp. 9–19"
      - source: SRC-0061
        locator: "Operational corpus and aggregate decision states, Figure 4"
  - predicate: depends-on
    target: VUL-0007
    claim_id: SYN-0032-C04
    evidence:
      - source: SRC-0059
        locator: "Definition, reference-data, method and provider-configuration limits"
      - source: SRC-0012
        locator: "Identity, record, process-integrity, provider and equipment boundaries"
  - predicate: evidenced-by
    target: SRC-0059
    claim_id: SYN-0032-C05
    evidence:
      - source: SRC-0059
        locator: "SRC-0059-C02–C07; blinded method, aggregate results, failures and independence limits"
  - predicate: evidenced-by
    target: SRC-0061
    claim_id: SYN-0032-C05
    evidence:
      - source: SRC-0061
        locator: "SRC-0061-C02–C06; operational corpus, aggregate outputs and developer/data limits"
  - predicate: depends-on
    target: CTL-0024
    claim_id: SYN-0032-C06
    evidence:
      - source: SRC-0059
        locator: "NIST blinded common-dataset test and failure limits"
      - source: SRC-0061
        locator: "SecureDNA operational-data application and evidence limits"
  - predicate: governed-by
    target: GOV-0028
    claim_id: SYN-0032-C07
    evidence:
      - source: SRC-0060
        locator: "HHS GPS §§1.2, 1.4, 2.6, 3.5–3.6 and Appendix D §D.5.2.3"
      - source: SRC-0013
        locator: "EO 14292 §4(b), 90 FR 19612"
      - source: SRC-0011
        locator: "2024 OSTP Framework §§I–II and V"
  - predicate: depends-on
    target: RSK-0008
    claim_id: SYN-0032-C08
    evidence:
      - source: SRC-0059
        locator: "Observed labelled screening misses/disagreements at the classification edge"
      - source: SRC-0061
        locator: "Aggregate operational screening decision outputs without downstream fulfilment or harm outcome"
tags:
  - engineering-biology
  - synthetic-biology
  - lifecycle
  - threat-model
  - sequence-screening
  - assurance
  - governance
  - evidence-reconciliation
---

# Engineering-biology lifecycle, threat, screening and governance reconciliation

## Decision scope and frozen pre-state

This synthesis adjudicates SEB-WL, SEB-TV, SEB-CI, SEB-AE and SEB-GR against
the unchanged v1.0 rubric. It does not turn page count into coverage, treat
policy as deployment, count six benchmark tools as six independent tests, or
equate aggregate screening decisions with prevented biological harm.

> **Claim record — SYN-0032-C01 | artifact-observation**
> **Claim:** Before this transaction the recalculated public wiki has 98 Pass,
> 9 Partial and 3 Absent cells = 98/110 (89.1%), dimension vector
> 10/9/5/9/8/8/10/10/10/9/10, critical cells 84/6/1, eight dimensions at
> least 9/10 and global gates at 9 Pass/3 Fail.
> **Claim status:** active
> **Scope:** Artifact state after SYN-0031 and before this transaction; not
> absolute domain completeness.
> **As of:** Fully linted checkpoint 2026-07-13 after SYN-0031.
> **Review after:** 2026-07-27.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SYN-0001](syn-0001-coverage-rubric.md), checkpoint
> SYN-0001-C47; [SYN-0031](syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md),
> SYN-0031-C08/C12/C13.
> **Basis / limits:** This is reproducible current-corpus arithmetic only.

## Evidence roles, independence and non-duplication

| Role | Lineage | Counting boundary |
| --- | --- | --- |
| design and DBTL | NASEM 2025 | advisory engineering-biology/design lineage; no order transaction |
| procurement screening | U.S. OSTP 2024 and UK 2024 | independent national policy lineages; not implementation evidence |
| use, custody and closeout | WHO 2024 | global laboratory-biosecurity branch; not universal product disposition |
| current U.S. adoption | HHS GPS v2 | bounded department award-policy mechanism excluding NIH |
| blinded screening test | NIST-led 999-item study | one test instance, six comparators, developer participation |
| operational screening | SecureDNA peer-reviewed study | one developer-led operational-data lineage with anonymous providers |

The NIST and SecureDNA records are materially distinct test and operational
contexts, but SecureDNA is the named overlapping safeguard and at least Jens
Berlips and Leonard Foner appear in both author lineages. That overlap and
developer participation prevent calling either paper an independent
confirmation or effectiveness evaluation of the other. HHS normalized text
remains reproducible content evidence, not an issuer-owned binary or
cryptographic provenance record.

> **Claim record — SYN-0032-C02 | analytic-judgment**
> **Claim:** Claim-specific evidence roles are counted without inflation:
> NASEM, WHO, U.S. and UK policy lineages support lifecycle/threat/governance
> reconciliation; NIST contributes one blinded test; SecureDNA contributes one
> developer-led operational lineage; and HHS contributes bounded agency-policy
> adoption rather than award-level compliance or effectiveness.
> **Claim status:** active
> **Scope:** Source-lineage accounting for the five candidate cells; not equal
> source weight or independent replication of every empirical result.
> **As of:** Full package review 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** SRC-0059-C02/C03/C07; SRC-0060-C01/C06/C07;
> SRC-0061-C02/C05/C06; WFL-0014-C01; GOV-0028-C04/C05.
> **Basis / limits:** Issuer, method, system overlap, study identity and
> adoption predicates remain separate. Multiple representations of one source
> or multiple tools inside one study do not create independent lineages.

## Complete safe lifecycle — SEB-WL

The accepted composition is:

design → order → screen → review → synthesis/build → delivery/use →
record/report → disposition.

Design/DBTL comes from NASEM; order, screening, review, fulfilment, reporting
and records come from independent U.S. and UK instruments; WHO supplies the
bounded use/custody/disposition branch. The order bridge is analytic, denial
can terminate the flow, and no source is said to implement one universal
end-to-end transaction.

> **Claim record — SYN-0032-C03 | analytic-judgment**
> **Claim:** SEB-WL passes at SF2 because WFL-0014 directly locates every
> required lifecycle literal across materially independent NASEM, U.S., UK and
> WHO roles while preserving analytic bridges, branching, force, scope and
> implementation limits.
> **Claim status:** active
> **Scope:** Safe lifecycle-class completeness for represented engineering-
> biology and synthesis contexts; not a production protocol, universal linear
> workflow, completed transaction or biological outcome.
> **As of:** 2026-07-13 corpus.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [WFL-0014](../workflows/wfl-0014-engineering-biology-design-to-disposition-lifecycle.md),
> WFL-0014-C01–C05; SRC-0033-C04/C08; SRC-0011-C03–C05;
> SRC-0012-C02/C04–C06; SRC-0004-C04/C09.
> **Basis / limits:** Each literal and SF2 independence are represented. The
> cross-source sequence is analytic and does not imply universal execution.

## Safe threat, hazard and exposure model — SEB-TV

The canonical model distinguishes intentional misuse, design/screening
integrity action, insider and malicious supply action from accidental
screening/build/feedback/custody failures and from persistent definition,
reference-data, integration, identity, coverage and continuity weaknesses.
NIST's disagreements remain non-adversarial measured failures unless intent is
separately evidenced.

> **Claim record — SYN-0032-C04 | analytic-judgment**
> **Claim:** SEB-TV passes at SF2 because THR-0006, HAZ-0007 and VUL-0007 cover
> every misuse, design/screening-integrity, insider/supply and accidental-
> hazard limb, link them to relevant assets/workflows and keep actor, method,
> weakness, failure and consequence separate across independent WHO, NASEM,
> UK and NIST roles.
> **Claim status:** active
> **Scope:** Defensive threat-model breadth; not a named misuse incident,
> current-provider vulnerability finding, prevalence estimate or operational
> evasion path.
> **As of:** 2026-07-13 corpus.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [THR-0006](../threats/thr-0006-engineering-biology-misuse-insider-and-supply-actions.md),
> THR-0006-C01–C06; [HAZ-0007](../hazards/haz-0007-engineering-biology-screening-synthesis-and-lifecycle-failures.md),
> HAZ-0007-C01–C05; [VUL-0007](../vulnerabilities/vul-0007-synthesis-screening-definition-database-integration-and-supply-exposures.md),
> VUL-0007-C01–C06.
> **Basis / limits:** All literal classes and their ontology boundaries have
> direct support. Generic classes are not converted into current exposures or
> incidents.

## Measured screening consequence remains incomplete — SEB-CI

NIST directly reports a blinded classification outcome and measured failure
limits. SecureDNA separately reports aggregate operational decision outcomes
over a large anonymized provider-order corpus. These are screening
consequences at safe abstraction: they do not establish malicious orders,
unsafe fulfilment, product harm or biological effect.

> **Claim record — SYN-0032-C05 | analytic-judgment**
> **Claim:** SEB-CI changes Absent→Partial, not Pass: the NIST-led primary
> empirical benchmark directly measures screening classifications,
> disagreements and misses, and the SecureDNA paper supplies a materially
> different real-order-data context and aggregate decision outcomes, but
> shared safeguard/authors and developer participation leave the mandatory SF3
> independent confirmation or evaluation literal unsatisfied.
> **Claim status:** active
> **Scope:** Observed/measured screening consequence at aggregate safe
> abstraction; not an incident, harmful-order prevalence, prospective
> fulfilment result, product effect or prevented biological harm.
> **As of:** Study lineages 2025–2026; reconciled 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
> SRC-0059-C03–C07; [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md),
> SRC-0061-C03–C06.
> **Basis / limits:** NIST supplies a controlled primary measurement and
> SecureDNA a distinct operational-data study, so the cell is no longer
> Absent. Different datasets do not erase shared tool/author lineage or create
> an independent confirmation, so Partial earns no point.

## Assurance remains incomplete — SEB-AE

CTL-0024 maps the benchmark to the exact classification edge and preserves
positive metrics, 43 missed NIST-labelled concerning items, provider-
configuration dependence and operational-data limits. Only one named
safeguard overlaps the benchmark and operational-data study. Its developers
participated in both lineages, and the operational raw orders are unavailable.

> **Claim record — SYN-0032-C06 | analytic-judgment**
> **Claim:** SEB-AE changes Absent→Partial, not Pass: measured test and bounded
> operational-data evidence with explicit failure limits now exists, but
> the same overlapping safeguard lacks a fully independent evaluator, public
> provider-level replication and a prospective or causal effectiveness
> outcome.
> **Claim status:** active
> **Scope:** Frozen assurance/effectiveness criterion and evidence ladder; not
> a product ranking or assertion that screening is ineffective.
> **As of:** Full source-pair review 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [CTL-0024](../controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md),
> CTL-0024-C01–C07; SRC-0059-C03–C07; SRC-0061-C03–C06; exact frozen SEB-AE
> criterion in SYN-0001.
> **Basis / limits:** Test, operational-data context and failure limits are direct.
> Independent evaluation is a mandatory literal and cannot be inferred from
> peer review, publication multiplicity or a developer-participating test.

## Current governance and adoption — SEB-GR

The UK has a current voluntary national guidance lineage. The current HHS GPS
adds an implemented U.S. department award-policy mechanism for its stated
scope, excludes NIH and supplies no award/provider compliance census. It still
references the 2024 OSTP framework while EO 14292 directs revision or
replacement; the completed successor remains unverified.

> **Claim record — SYN-0032-C07 | analytic-judgment**
> **Claim:** SEB-GR passes at SF2 because current independent UK guidance and
> the current bounded HHS award-policy mechanism are reconciled for
> jurisdiction, force, scope, adoption, duty holders, exclusions and currency,
> while the unresolved U.S. successor and absent organization-level compliance
> remain explicit gaps.
> **Claim status:** active
> **Scope:** Current UK plus bounded U.S. HHS governance reconciliation; not
> universal U.S. implementation, NIH policy, provider certification,
> compliance or effectiveness.
> **As of:** Current pages checked 2026-07-13.
> **Review after:** 2026-08-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [GOV-0028](../governance/gov-0028-hhs-synthetic-nucleic-acid-procurement-award-condition.md),
> GOV-0028-C01–C05; [SRC-0060](../sources/src-0060-hhs-nucleic-acid-procurement-award-condition-2025-2026.md),
> SRC-0060-C02–C07; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> SRC-0012-C01–C08; [SRC-0013](../sources/src-0013-us-eo-14292-biological-research-2025.md),
> SRC-0013-C02/C06.
> **Basis / limits:** Two current national policy contexts and their different
> force/adoption predicates are direct. No completed successor is inferred or
> fabricated for this bounded pass; its absence from the represented corpus
> remains a named gap.

## Risk-chain and cross-sector control accounting

NIST strengthens the classification-failure edge of RSK-0008 and SecureDNA
adds aggregate real-order decision context. Neither observes a screened order
crossing fulfilment into a biological consequence, so this transaction does
not by itself certify the SEB chain or the global risk-chain gate.

CTL-0024 contributes one tested SEB safeguard instance with an operational-data
complement to CTR-AE, not six tools or seven publications. It supplies a
negative/failure result but not an independent evaluator for the overlapping
safeguard.

> **Claim record — SYN-0032-C08 | analytic-judgment**
> **Claim:** RSK-0008 and the cross-sector assurance portfolio gain one
> bounded empirical classification/test and operational instance, but the
> global risk-chain and controls gates remain Fail because downstream
> fulfilment/consequence evidence and the frozen six-instance/four-sector/
> three-evaluator CTR-AE portfolio are still incomplete.
> **Claim status:** active
> **Scope:** Adjacent gate accounting; not a claim that screening failure or
> harm occurred.
> **As of:** 2026-07-13 transaction.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** RSK-0008-C01/C02; CTL-0024-C03/C05–C07;
> SRC-0059-C04/C05/C07; SRC-0061-C03–C06; frozen gates 5 and 8 in SYN-0001.
> **Basis / limits:** The new measured states stop at screening decisions and
> do not satisfy the missing downstream or portfolio-wide predicates.

## Accepted transitions and resulting state

> **Claim record — SYN-0032-C09 | analytic-judgment**
> **Claim:** Independent strict review accepts exactly three Pass transitions:
> SEB-WL, SEB-TV and SEB-GR change Partial→Pass, while SEB-CI and SEB-AE
> change only Absent→Partial; no other cell or global gate changes.
> **Claim status:** active
> **Scope:** Frozen 110-cell rubric transaction; Partial and Absent both earn
> zero points.
> **As of:** 2026-07-13.
> **Review after:** 2026-07-27.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** SYN-0032-C02–C08; exact frozen criteria/source floors; two
> independent evidence/safety and structural/rubric-readiness audits completed
> 2026-07-13.
> **Basis / limits:** Three full contracts pass. Mandatory independent-
> confirmation/evaluation literals prevent SEB-CI and SEB-AE promotion to
> Pass.

> **Claim record — SYN-0032-C10 | artifact-observation**
> **Claim:** The three accepted Pass transitions produce 101 Pass, 8 Partial
> and 1 Absent cells = 101/110 (91.8%), dimension vector
> 10/9/8/9/8/8/10/10/10/9/10, critical cells 87/4/0, eight dimensions at least
> 9/10 and global gates at 9 Pass/3 Fail.
> **Claim status:** active
> **Scope:** Arithmetic state after activation and clean lint; not final
> certification because the numeric, risk-chain and controls gates remain
> failed.
> **As of:** 2026-07-13 transaction.
> **Review after:** 2026-07-27.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** SYN-0032-C01/C09; frozen dimension membership, critical flags
> and global gates in [SYN-0001](syn-0001-coverage-rubric.md).
> **Basis / limits:** Three new Pass states add three points. The remaining
> open cells are GEN-AE, SEB-CI, SEB-AE, LAB-AE, BMO-SD, BMO-AE, CPH-AE and
> CTR-AE; SEB and BMO remain below 9/10.

## Safety and nonpromotion boundary

> **Claim record — SYN-0032-C11 | analytic-judgment**
> **Claim:** The transaction remains defensive and evidence-calibrated: it
> exposes no biological design or sequence, screening parameter, concern
> example, provider weakness, configuration, evasion path, customer record,
> synthesis procedure or harmful-production detail, and it preserves policy,
> test, deployment, decision-output, effectiveness and independent-evaluation
> states.
> **Claim status:** active
> **Scope:** Transaction content and safety boundary.
> **As of:** 2026-07-13.
> **Review after:** 2027-01-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Safety sections in SRC-0059/0060/0061, WFL-0014, THR-0006,
> HAZ-0007, VUL-0007, CTL-0024 and GOV-0028.
> **Basis / limits:** High-level defensive abstractions are sufficient for all
> accepted decisions; missing operational detail cannot be used as a reason
> to weaken the rubric.

## Related pages

- [SYN-0001 — frozen coverage rubric](syn-0001-coverage-rubric.md)
- [SYN-0031 — prior checkpoint](syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)
- [WFL-0014 — complete safe lifecycle](../workflows/wfl-0014-engineering-biology-design-to-disposition-lifecycle.md)
- [THR-0006 — intentional threat classes](../threats/thr-0006-engineering-biology-misuse-insider-and-supply-actions.md)
- [HAZ-0007 — accidental hazard classes](../hazards/haz-0007-engineering-biology-screening-synthesis-and-lifecycle-failures.md)
- [VUL-0007 — exposure classes](../vulnerabilities/vul-0007-synthesis-screening-definition-database-integration-and-supply-exposures.md)
- [CTL-0024 — benchmark assurance](../controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md)
- [GOV-0028 — HHS award condition](../governance/gov-0028-hhs-synthetic-nucleic-acid-procurement-award-condition.md)
- [RSK-0008 — screening-failure path](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md)
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [SRC-0013](../sources/src-0013-us-eo-14292-biological-research-2025.md)
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md)
- [SRC-0060](../sources/src-0060-hhs-nucleic-acid-procurement-award-condition-2025-2026.md)
- [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md)
