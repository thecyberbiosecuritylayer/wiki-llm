---
id: CTL-0006
type: control
title: Nucleic-acid order, customer and equipment screening controls
aliases:
  - synthesis procurement screening controls
  - provider and benchtop screening assurance
status: active
created: 2026-07-12
updated: 2026-07-13
last_reviewed: 2026-07-13
review_after: 2026-10-10
source_ids:
  - SRC-0011
  - SRC-0012
  - SRC-0033
  - SRC-0059
  - SRC-0060
  - SRC-0061
sensitivity: public
dual_use: moderate
control_status: multi-jurisdiction-normative-criteria-with-bounded-assurance-layer
implementation_status: bounded-hhs-award-policy-branch-adopted-provider-and-award-compliance-unknown
testing_status: one-nist-led-benchmark-and-one-developer-led-operational-data-context
effectiveness_status: no-causal-or-prevented-harm-result
independent_evaluation_status: absent-for-the-tested-overlapping-safeguard
relations:
  - predicate: evidenced-by
    target: SRC-0011
    claim_id: CTL-0006-C01
    evidence:
      - source: SRC-0011
        locator: "§I, p. 4; §V, pp. 8–13; §VI, p. 14"
  - predicate: mitigates
    target: RSK-0008
    claim_id: CTL-0006-C02
    evidence:
      - source: SRC-0011
        locator: "§V, printed pp. 8–13"
  - predicate: depends-on
    target: WFL-0008
    claim_id: CTL-0006-C02
    evidence:
      - source: SRC-0011
        locator: "§§I–V, printed pp. 4–13"
  - predicate: governed-by
    target: GOV-0002
    claim_id: CTL-0006-C01
    evidence:
      - source: SRC-0011
        locator: "§§I–II, printed pp. 4–5"
  - predicate: evidenced-by
    target: SRC-0012
    claim_id: CTL-0006-C03
    evidence:
      - source: SRC-0012
        locator: "Customer/sequence screening through cybersecurity sections, HTML lines 841–1050"
  - predicate: governed-by
    target: GOV-0003
    claim_id: CTL-0006-C03
    evidence:
      - source: SRC-0012
        locator: "Introduction and scope, HTML lines 708–839"
  - predicate: evidenced-by
    target: SRC-0033
    claim_id: CTL-0006-C05
    evidence:
      - source: SRC-0033
        locator: "Chapter 4 §AI and Biodesign Security, printed pp. 50–53 (physical pp. 71–74)"
tags:
  - synthesis
  - procurement
  - screening
  - customer-review
  - equipment-lifecycle
  - information-security
  - ai-assisted-screening
---

# Nucleic-acid order, customer and equipment screening controls

> Cross-jurisdiction control family spanning accountable disclosure, order/sequence and
> customer/equipment screening, bounded review, refusal/reporting, records and
> information security. The family is primarily policy design; a bounded HHS
> award-policy branch and one assurance layer are now represented without being
> inflated into provider implementation or effectiveness.

## Objective and evidence status

Prevent or detect inappropriate order fulfillment/equipment access, preserve
accountable decisions and protect customer, screening and procurement
information while allowing legitimate research to proceed.

| Dimension | Status | Boundary |
| --- | --- | --- |
| Normatively specified | **Yes** | Revised September 2024 framework |
| Funding-conditioned | HHS GPS v2 adopts one bounded award-policy branch | Excludes NIH; award-level compliance and wider agency status remain unknown |
| UK guidance | Voluntary expected responsible practice | No adoption dataset or central conformity result |
| Implemented | Policy branch only | No provider/manufacturer deployment or award-level compliance dataset |
| Tested | One bounded NIST-led benchmark plus developer-led operational context | Shared safeguard/authors; historical orders are not confirmed prospective deployment |
| Effective | Unknown | No causal prevention, downstream fulfillment or harm counterfactual |
| Independently evaluated | No | Developer participation and lineage overlap remain; peer review is not independent system evaluation |

> **Claim record — CTL-0006-C01 | source-report**
> **Claim:** The OSTP framework groups adherence into accountable attestation;
> order/sequence screening; customer and equipment legitimacy review;
> refusal/reporting; record retention; and cybersecurity/information-security
> measures.
> **Claim status:** active
> **Scope:** Revised September 2024 US framework criteria; exact technical
> thresholds, indicators, contact details and bypass mechanics withheld.
> **As of:** 2024-09-30.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §I, p. 4; §V, pp. 8–13; §VI, p. 14.
> **Basis / limits:** Control families are direct. The source does not show
> adoption, test performance, prevented events or independent assurance.

## Exact scenario edges

For [RSK-0008](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md):

1. **accountability edge:** attestation and assigned authority establish who is
   responsible for the screening process;
2. **order-recognition edge:** screening identifies orders requiring the next
   decision step;
3. **identity/purpose edge:** customer/equipment legitimacy review informs an
   accountable human decision;
4. **decision-to-fulfillment edge:** refusal/escalation/reporting can stop or
   contain inappropriate fulfillment;
5. **history/cross-transaction edge:** protected records preserve rationale and
   support later review;
6. **system-integrity edge:** information security protects identities, IP,
   records and screening capability;
7. **equipment-lifecycle edge:** legitimate access/transfer accountability
   extends beyond initial purchase.

> **Claim record — CTL-0006-C02 | analytic-judgment**
> **Claim:** The seven functional mappings conditionally interrupt the
> recognition, review, decision, fulfillment and recovery/learning edges of
> `RSK-0008`, but `SRC-0011` does not demonstrate that any edge was interrupted
> in practice.
> **Claim status:** active
> **Scope:** Defensive mapping to `WFL-0008`, not compliance or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §V, printed pp. 8–13.
> **Basis / limits:** Each source criterion maps to a scenario edge; the
> interruption model is wiki analysis. Accuracy, latency, false decisions,
> implementation consistency and downstream outcomes are unknown.

> **Claim record — CTL-0006-C03 | source-report**
> **Claim:** UK guidance independently recommends customer and sequence checks,
> human follow-up, refusal/reporting, recordkeeping, equipment user/transfer
> controls, authentication/logging/process integrity, updated screening and
> cybersecurity/privacy safeguards.
> **Claim status:** active
> **Scope:** Voluntary UK responsible-practice guidance, not legal compliance,
> deployment or effectiveness.
> **As of:** 2024-10-08.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> customer/sequence screening through cybersecurity sections, HTML lines
> 841–1050.
> **Basis / limits:** Functions are direct. Exact technical rules, suspicious
> indicators, identity fields and device mechanics are withheld; implementation
> and outcomes are not reported.

> **Claim record — CTL-0006-C04 | analytic-judgment**
> **Claim:** Two independent official national lineages jointly cover identity,
> order/sequence screening, human review, instrument access/update/monitoring,
> refusal/reporting, records and cybersecurity, and each function is mapped to
> an exact `RSK-0008` lifecycle edge.
> **Claim status:** active
> **Scope:** Normative control coverage and mapping; not implementation,
> equivalence, compliance or effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md),
> §V, pp. 8–13; [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
> HTML lines 841–1050.
> **Basis / limits:** The two issuers independently specify the control
> functions. Their force and population differ, and neither supplies adoption,
> performance, failure corpus or independent evaluation.

> **Claim record — CTL-0006-C05 | source-report**
> **Claim:** NASEM reports that AI-enabled biological tools can both create new
> challenges for synthesis screening and potentially augment it, and discusses
> metadata/logging, layered screening and design-tool guardrails with explicit
> false-positive, feasibility and effectiveness limits.
> **Claim status:** active
> **Scope:** Emerging control research and tradeoffs; not a replacement
> screening standard, implementation, benchmark, adoption or effectiveness
> result.
> **As of:** 2025-04-23.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
> Chapter 4 §AI and Biodesign Security, printed pp. 50–53 (physical pp. 71–74).
> **Basis / limits:** The dual challenge/mitigation framing and tradeoffs are
> direct. No technical criterion, test set, performance value, deployed
> control, prevented event or independent evaluator is supplied.

> **Claim record — CTL-0006-C06 | analytic-judgment**
> **Claim:** Current evidence distinguishes three assurance states: HHS GPS v2
> adopts one bounded award-policy branch excluding NIH; `CTL-0024` adds one
> NIST-led benchmark and a developer-led operational-data complement; provider
> implementation, award-level compliance, independent system evaluation and
> causal effectiveness remain unestablished.
> **Claim status:** active
> **Scope:** Corpus-level status reconciliation for this control family; not a
> provider census, compliance finding, deployment claim or effectiveness result.
> **As of:** 2026-07-13.
> **Review after:** 2026-10-13.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md),
> `SRC-0059-C03`–`C07`; [SRC-0060](../sources/src-0060-hhs-nucleic-acid-procurement-award-condition-2025-2026.md),
> `SRC-0060-C03`–`C07`; [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md),
> `SRC-0061-C03`–`C06`; [SYN-0032](../syntheses/syn-0032-engineering-biology-lifecycle-threat-screening-governance-reconciliation.md),
> `SYN-0032-C02/C05`–`C07`.
> **Basis / limits:** Policy adoption, test context, operational-data context,
> evaluator overlap and absent outcomes are direct or explicitly bounded in the
> cited package; none is silently promoted to a stronger evidence predicate.

## Prerequisites, failure modes and tradeoffs

- accountable scope and current policy/technical specifications;
- protected and sufficiently current screening capability;
- proportionate identity/purpose review and trained decision-makers;
- secure records with usable provenance and privacy/IP safeguards;
- provider/manufacturer/intermediary and equipment-transfer responsibility;
- safe escalation and recovery that do not expose restricted screening detail.

Failure modes include stale or unavailable screening capability, false
acceptance/refusal, identity/provenance error, inconsistent intermediary
handling, insecure records, unclear human authority and unvalidated equipment
lifecycle controls. False refusal and delay can burden legitimate research;
collection/retention can create privacy and IP risk.

## Validation and framework mappings

Validation requires versioned test sets, error/latency measures, safety and
privacy limits, representative operational context, null/failure results and
an independent evaluator. The original sources identify future NIST
specifications, conformity work, effectiveness measurement and possible
audits. CTL-0024 now adds one bounded test plus operational-data complement,
but still lacks independent evaluation and causal effectiveness. References to
NIST/CISA/ISO/ISA/FDA practices remain neither compliance nor effectiveness
proof.

## Related pages

- [RSK-0008](../risk-scenarios/rsk-0008-screening-failure-and-unsafe-order-fulfillment.md)
- [WFL-0008](../workflows/wfl-0008-nucleic-acid-procurement-screening-lifecycle.md)
- [SYS-0006](../systems/sys-0006-synthesis-provider-and-benchtop-screening-systems.md)
- [AST-0004](../assets/ast-0004-synthetic-nucleic-acid-orders-and-equipment.md)
- [GOV-0002](../governance/gov-0002-us-federally-funded-nucleic-acid-screening-2024.md)
- [GOV-0003](../governance/gov-0003-uk-synthetic-nucleic-acid-screening-2024.md)
- [SYN-0002](../syntheses/syn-0002-us-uk-nucleic-acid-screening-comparison.md)
- [CTL-0016 — Broader biological-AI controls](ctl-0016-biological-ai-provenance-validation-decision-gates.md)
- [WFL-0011 — Biological AI/DBTL lifecycle](../workflows/wfl-0011-ai-enabled-biological-model-dbtl-lifecycle.md)
- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md)
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md)
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md)
- [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md)
- [SRC-0060](../sources/src-0060-hhs-nucleic-acid-procurement-award-condition-2025-2026.md)
- [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md)
- [CTL-0024 — NIST-benchmarked assurance layer](ctl-0024-nist-benchmarked-nucleic-acid-screening-assurance.md)

## Sources

- [SRC-0011](../sources/src-0011-ostp-nucleic-acid-screening-2024.md), §§I–VI,
  printed pp. 4–14.
- [SRC-0012](../sources/src-0012-uk-synthetic-nucleic-acid-screening-2024.md),
  HTML lines 841–1050.
- [SRC-0033](../sources/src-0033-nasem-age-of-ai-in-life-sciences-2025.md),
  Chapter 4, printed pp. 50–53 (physical pp. 71–74).
- [SRC-0059](../sources/src-0059-nist-nucleic-acid-screening-benchmark-2025-2026.md)
- [SRC-0060](../sources/src-0060-hhs-nucleic-acid-procurement-award-condition-2025-2026.md)
- [SRC-0061](../sources/src-0061-securedna-operational-synthesis-screening-study-2026.md)
