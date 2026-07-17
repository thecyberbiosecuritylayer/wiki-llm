---
id: THR-0006
type: threat
title: Engineering-biology misuse, insider and supply-chain action classes
aliases:
  - synthesis and screening intentional threat model
  - engineering biology misuse and integrity threats
  - synthesis insider and supplier threats
status: active
created: 2026-07-13
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-10-10
source_ids:
  - SRC-0004
  - SRC-0012
  - SRC-0033
  - SRC-0059
sensitivity: public
dual_use: moderate
threat_kind: intentional-misuse-design-screening-insider-and-supply-chain-actions
relations:
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: THR-0006-C02
    evidence:
      - source: SRC-0004
        locator: "WHO §3.2, printed p. 8; §§5.1 and 5.3.1–5.3.4, printed pp. 19–22; §6.1, printed pp. 25–28"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: THR-0006-C02
    evidence:
      - source: SRC-0033
        locator: "NASEM Chapters 2–3, printed pp. 21–37; Chapters 4–5, printed pp. 46–81; Appendix A, printed pp. 115–124"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: THR-0006-C03
    evidence:
      - source: SRC-0012
        locator: "UK screening, information/process-integrity and provider/vendor/equipment responsibilities, HTML lines 833–1039"
  - predicate: evidenced-by
    target: SRC-0059
    claim_id: THR-0006-C03
    evidence:
      - source: SRC-0059
        locator: "Blinded benchmark Abstract; Results, physical pp. 9–17; Table 2, physical p. 24; Figure 1, physical p. 25; Conclusion, physical pp. 18–19"
  - predicate: exploits
    target: VUL-0007
    claim_id: THR-0006-C06
    evidence:
      - source: SRC-0033
        locator: "NASEM data/model/software dependency and supply-chain exposure classes, Chapters 3–5"
      - source: SRC-0059
        locator: "NIST benchmark definition, reference-data and algorithm disagreement classes, Results and Conclusion"
  - predicate: affects
    target: AST-0004
    claim_id: THR-0006-C06
    evidence:
      - source: SRC-0012
        locator: "UK actor, order, record, equipment, product and transfer scope, HTML lines 708–1070"
      - source: SRC-0033
        locator: "NASEM biological design/data/model/software/material/automation asset scope, Chapters 2–5"
tags:
  - engineering-biology
  - synthetic-biology
  - nucleic-acid-synthesis
  - misuse
  - design-integrity
  - screening-integrity
  - insider
  - supply-chain
  - defensive-taxonomy
---

# Engineering-biology misuse, insider and supply-chain action classes

## Threat definition and separation rule

This page represents intentional actor/action classes that can affect
engineering-biology design, procurement, screening, physical synthesis and
associated digital/supply dependencies. It preserves five distinct classes:

1. misuse of biological design, synthesis or resulting capability;
2. intentional corruption of design/data/model state;
3. intentional interference with screening or review integrity;
4. malicious or policy-violating insider action; and
5. malicious supplier, service-provider or software-supply-chain action.

An actor class is not an event, access path, technique, vulnerability or
consequence. Ordinary error, outage, defective input, incomplete reference
data, unreliable automation and accidental release/loss are non-adversarial
hazards. The corresponding hazard and vulnerability pages remain distinct:
[HAZ-0007](../hazards/haz-0007-engineering-biology-screening-synthesis-and-lifecycle-failures.md)
and
[VUL-0007](../vulnerabilities/vul-0007-synthesis-screening-definition-database-integration-and-supply-exposures.md).

> **Claim record — THR-0006-C01 | analytic-judgment**
> **Claim:** The canonical model separates intentional misuse, design/screening
> integrity action, insider action and malicious supply action from accidental
> hazards and enabling vulnerabilities; category presence alone does not prove
> actor access, intent, success or downstream harm.
> **Claim status:** active
> **Scope:** Defensive engineering-biology/synthesis threat taxonomy; no target,
> design, sequence, access route, screening rule, exploit or laboratory method.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> `SRC-0004-C01/C11`, WHO §§3.2, 5.1 and 5.3; [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C06`, Chapters 2–5; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> `SRC-0012-C05/C06`; [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
> `SRC-0059-C03`–`C05`.
> **Basis / limits:** The sources distinguish misuse, intentional manipulation,
> integrity controls and observed non-adversarial screening disagreements. The
> clean actor/hazard/vulnerability separation is wiki analysis.

## Misuse and design-integrity actions

WHO places synthetic biology and artificial DNA synthesis within a
proportionate biosecurity assessment because beneficial products/capabilities
can also be misused. NASEM independently describes malicious use of biological
AI/design capability and intentional manipulation of data/model/software state
that can corrupt design or experimental decisions. Neither source documents a
named synthesis-misuse incident or supplies prevalence.

> **Claim record — THR-0006-C02 | analytic-judgment**
> **Claim:** Independent WHO and NASEM lineages support high-level intentional
> misuse and design-integrity threat classes across synthetic-biology and
> biological-AI/DBTL contexts, without establishing a specific actor, event,
> exposed design or successful harmful output.
> **Claim status:** active
> **Scope:** Potential intentional action at defensive abstraction; not
> likelihood, attribution, capability assessment or operational method.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> `SRC-0004-C01/C11`, §3.2, printed p. 8 (PDF p. 28), and §§5.1/5.3,
> printed pp. 19–22; [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C06`, Chapters 2–3, printed pp. 21–37, and Chapters 4–5,
> printed pp. 46–81.
> **Basis / limits:** Misuse and integrity categories are direct and the
> institutional lineages are materially independent. Source examples are not
> consolidated into operational detail or incident claims.

## Screening-integrity actions and measured failure boundary

UK guidance independently requires protected customer/order/screening
information, process integrity, logging and accountable review for provider,
vendor and equipment settings. Those are control requirements that identify an
integrity boundary; they are not proof of attack or implementation.

The NIST inter-tool study supplies a separate empirical boundary. In one
blinded baseline benchmark, six tools achieved the reported aggregate
performance floors but still produced false-negative and false-positive calls
and tool disagreements. The paper attributes disagreements broadly to
definition, reference-data and algorithm differences and warns that provider
configuration can change results. Those findings demonstrate fallible
screening integrity and dependency state—not malicious interference, evasion or
provider-wide effectiveness.

> **Claim record — THR-0006-C03 | analytic-judgment**
> **Claim:** UK guidance supplies the intentional screening/process-integrity
> threat boundary, while the NIST benchmark separately measures positive
> performance and non-adversarial disagreement/failure limits; together they
> preserve both classes without turning benchmark errors into evidence of a
> malicious actor or exploitable bypass.
> **Claim status:** active
> **Scope:** High-level screening integrity and evidence limits; no exact
> sequence, tool-specific result, threshold, configuration, provider weakness
> or evasion procedure.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> `SRC-0012-C05/C06`, HTML lines 833–1039;
> [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
> `SRC-0059-C03`–`C06`; Abstract, Results physical pp. 9–17, Table 2
> physical p. 24, Figure 1 physical p. 25 and Conclusion physical pp. 18–19.
> **Basis / limits:** Policy integrity functions and measured benchmark limits
> are direct and materially different evidence roles. The study is one
> developer-participating evaluation, not a provider deployment or attack.

## Insider actions

WHO explicitly treats insider threats and insider-caused biosecurity incidents
as risk-assessment and personnel-reliability concerns. It also distinguishes
deliberate from accidental loss/release. For this page, `insider` means a person
with an authorized, trusted or institutionally proximate role; it does not
presume malicious motive. A policy violation, negligence or mistake remains a
hazard or compliance state unless adverse intent/action is evidenced.

> **Claim record — THR-0006-C04 | source-report**
> **Claim:** WHO explicitly identifies insider threats, deliberate misuse,
> theft/diversion and insider-caused biosecurity incidents and recommends
> proportionate personnel, accountability and reporting controls, while also
> preserving accidental loss/release as a different state.
> **Claim status:** active
> **Scope:** WHO laboratory-biosecurity actor/action taxonomy applied only at
> high level to relevant engineering-biology environments; not a synthesis
> incident, employee suspicion rule or personnel-screening procedure.
> **As of:** WHO guidance published 2024-06-21; reviewed 2026-07-13.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§5.1 and 5.3.1–5.3.4, printed pp. 19–22 (PDF pp. 39–42), especially
> insider-threat and insider-incident text; §6.1, printed pp. 25–28.
> **Basis / limits:** The actor/action classes are direct WHO text. This is
> normative taxonomy, not an observed event, prevalence estimate or evidence
> about any named person or organization.

## Supplier and service-provider actions

WHO names service providers and suppliers among potential external threat
actors and treats outsourced information/service and transfer relationships as
biosecurity-relevant boundaries. NASEM independently identifies open-source
software and dependency supply-chain exposure in biological-AI/design
environments. UK guidance adds third-party vendor, provider, manufacturer and
equipment-update responsibility. These sources support actor and trust-boundary
classes, not a documented malicious supplier case.

> **Claim record — THR-0006-C05 | analytic-judgment**
> **Claim:** WHO, NASEM and UK guidance jointly support malicious supplier,
> service-provider, software/dependency and intermediary action classes, while
> ordinary outage, defect, shortage, stale reference data or maintenance error
> remains a non-adversarial hazard unless intent is evidenced.
> **Claim status:** active
> **Scope:** Supply actor/trust categories across represented engineering-
> biology and screening systems; not an incident, attribution, topology,
> dependency inventory or access method.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §3.5 and §§5.1/6.4–7.3, especially external service-provider/supplier and
> transfer/accountability roles; [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C05/C06`, Chapters 3–5; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> `SRC-0012-C03/C06`, HTML lines 708–885 and 933–1039.
> **Basis / limits:** Actor, dependency and responsibility classes are direct
> across independent lineages. Intent/state separation prevents ordinary
> supply failure from being mislabeled as an attack.

## Accidental hazard and vulnerability boundary

The safe threat model is complete only when intentional action is not allowed
to absorb accidental states. WHO explicitly includes accidental loss/release;
NASEM separately includes noisy/incomplete data, generalization failure and
unreliable automation; NIST measures screening misses/false alarms without
attributing intent. Those states belong to `HAZ-0007`. Definition, database,
algorithm, integration, identity and supplier dependencies belong to
`VUL-0007` until an actual exposed state is evidenced.

> **Claim record — THR-0006-C06 | analytic-judgment**
> **Claim:** `THR-0006`, paired with the distinct `HAZ-0007` and `VUL-0007`
> nodes, covers misuse, design/screening integrity, insider/supply action and
> accidental-failure boundaries without merging actor, failure, weakness or
> consequence and without operational evasion detail.
> **Claim status:** active
> **Scope:** Canonical safe threat-model structure and conditional graph edges;
> not an exposure finding, likelihood score, complete attack path or rubric
> decision by itself.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `THR-0006-C01`–`C05`; [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§5.1/5.3; [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> `SRC-0033-C06`; [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
> `SRC-0059-C04/C05`.
> **Basis / limits:** All literal classes have direct source support and their
> separation is explicit. Conditional `exploits`/`affects` edges require a
> compatible weakness, access and failed safeguards; no such state is presumed.

## Safety boundary

No target selection, biological design, sequence example, screening parameter,
reference-data content, customer indicator, access route, payload, instrument
configuration, provider weakness, facility topology or laboratory procedure is
represented. NIST results remain aggregate/anonymized and no disagreement is
translated into an evasion technique.

## Related pages

- [HAZ-0007 — non-adversarial failures](../hazards/haz-0007-engineering-biology-screening-synthesis-and-lifecycle-failures.md)
- [VUL-0007 — enabling exposures](../vulnerabilities/vul-0007-synthesis-screening-definition-database-integration-and-supply-exposures.md)
- [AST-0004 — synthesis order/equipment assets](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md)
- [SYS-0006 — provider/screening systems](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [WFL-0014 — complete lifecycle](../workflows/wfl-0014-engineering-biology-design-to-disposition-lifecycle.md)
- [RSK-0008 — screening-failure path](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [CTL-0006 — normative screening controls](../controls/ctl-0006-nucleic-acid-order-and-equipment-screening.md)
- [CTL-0024 — benchmarked assurance](../controls/ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md)
- [SYN-0032 — Engineering-biology reconciliation](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md), exact WHO locators above.
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md), exact NASEM locators above.
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md), HTML lines 708–1039.
- [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md), exact benchmark locators above.
