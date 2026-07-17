---
id: INC-0006
type: incident
title: Merck NotPetya manufacturing and supply disruption, 2017
aliases:
  - Merck 2017 network cyberattack
  - Merck NotPetya manufacturing incident
status: active
created: 2026-07-12
updated: 2026-07-16
last_reviewed: 2026-07-12
review_after: 2026-10-15
event_date: 2017-06-27
discovery_date: unknown
disclosure_date: unknown-earliest-public-disclosure
source_ids:
  - SRC-0046
  - SRC-0047
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0046
    claim_id: INC-0006-C04
    evidence:
      - source: SRC-0046
        locator: "10-K HTML anchors sC5918D6835605DFB9861637AED9AB7C7 (Item 1A, displayed printed p. 25), s02DF6574F3035C8485C795D393F48705 (MD&A, p. 38) and sBB3EEB5901095A398997106BC9F8CDA1 (Vaccines, p. 41)"
  - predicate: evidenced-by
    target: SRC-0047
    claim_id: INC-0006-C01
    evidence:
      - source: SRC-0047
        locator: "NJ Appellate opinion pp. 4–12 and 34–35"
  - predicate: affects
    target: WFL-0003
    claim_id: INC-0006-C04
    evidence:
      - source: SRC-0046
        locator: "10-K Item 1A and MD&A Cyber-attack; manufacturing→order/backlog consequence"
  - predicate: affects
    target: AST-0007
    claim_id: INC-0006-C04
    evidence:
      - source: SRC-0046
        locator: "10-K manufacturing, certain-product order, sales and stockpile predicates"
  - predicate: depends-on
    target: VUL-0003
    claim_id: INC-0006-C03
    evidence:
      - source: SRC-0047
        locator: "Opinion pp. 7–10; trusted third-party software/update dependency in court record"
tags:
  - biomanufacturing
  - pharmaceuticals
  - notpetya
  - manufacturing-disruption
  - supply
  - order-backlog
  - incident
---

# Merck NotPetya manufacturing and supply disruption, 2017

> [!WARNING]
> **Evidence classification**
> This is one **documented incident**, not two events created from two sources.
> Merck's SEC filing is the sole direct measurer of manufacturing/order/sales
> consequences. The New Jersey opinion supplies materially independent
> adjudicative/technical incident and property-damage context; company
> contentions and disputed attribution remain labeled.

## Event and evidence roles

> **Claim record — INC-0006-C01 | analytic-judgment**
> **Claim:** `INC-0006` canonicalizes one 2017-06-27 Merck network cyberattack
> across a first-party SEC consequence record and an independent published
> appellate incident/property-damage record without multiplying sources into
> events or consequence measurements.
> **Claim status:** active
> **Scope:** One incident/evidence ecosystem; not an independently replicated
> order/sales measure or every worldwide NotPetya victim.
> **As of:** Event 2017-06-27; represented records through 2023-05-01.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md),
> `SRC-0046-C01`–`C08`; [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md),
> `SRC-0047-C01`–`C08`.
> **Basis / limits:** Issuer, genre and claim roles are independent. Merck
> remains the sole supply/financial consequence measurer.

## Timeline

| State | Represented evidence | Boundary |
| --- | --- | --- |
| Event | network cyberattack on 2017-06-27 | exact initial time/site unknown |
| Discovery | no separate discovery timestamp located | not equated with event start |
| Response | CDC stockpile borrowing partly due shutdown and partly demand; system modernisation/resilience effort reported | no exact action chronology or tested outcome |
| Recovery indicators | partial stockpile replenishment in 2017, remaining doses replenished in 2018; residual order backlog affected 2018 sales; 2018 incident costs called immaterial | no full trusted-restoration or production-output date |
| Represented disclosure | 2018 Form 10-K filed 2019-02-27; opinion decided 2023-05-01 | not claimed as earliest public disclosure |

> **Claim record — INC-0006-C02 | analytic-judgment**
> **Claim:** The page separates event, unknown discovery/earliest disclosure,
> represented publication, response and bounded recovery indicators; unknown
> dates are not filled from filing or judgment dates.
> **Claim status:** active
> **Scope:** Event-state chronology required by `THI-WL`, not a complete
> incident-response timeline.
> **As of:** 2026-07-12 review.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md),
> Form 10-K Item 1A, displayed p. 25; MD&A, displayed pp. 38–39; Vaccines,
> displayed p. 41; and filing metadata; [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md),
> opinion cover/publication mark and pp. 7–12.
> **Limits:** Every represented state is directly located; exact
> discovery and full restoration remain unknown.

## Dependency and vector evidence

> **Claim record — INC-0006-C03 | analytic-judgment**
> **Claim:** Event-specific primary/adjudicative support identifies a trusted
> third-party accounting-software/update dependency leading into Merck's
> network and rapid broad propagation; the page retains source roles and omits
> operational exploit detail.
> **Claim status:** active
> **Scope:** High-level vendor/update/network trust boundary, not PLC/DCS/SCADA
> compromise, vulnerable-version guidance or a reproducible attack sequence.
> **As of:** Court record through 2023-05-01.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md),
> opinion pp. 7–10, including the Merck investigation, party-expert and Kroll
> passages.
> **Limits:** The dependency and propagation are direct in the court
> record; exact exploit/vulnerability predicates are unnecessary and excluded.

## Confirmed and reported consequences

The accepted safe path is:

`network cyberattack → manufacturing/research/sales disruption → order backlog
and inability to fulfil certain-product orders → bounded supply/sales effect`

> **Claim record — INC-0006-C04 | analytic-judgment**
> **Claim:** Merck's primary filing directly documents a manufacturing-to-
> supply consequence beyond generic IT outage: certain-product orders in
> certain markets could not be fulfilled, with bounded 2017 and residual-2018
> sales effects and manufacturing/remediation expense.
> **Claim status:** active
> **Scope:** Company-reported operational/supply consequence; not batch
> failure, product-quality change, shortage count, patient harm or independent
> replication of the figures.
> **As of:** 2017–2018 effects filed 2019-02-27.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `SRC-0046-C02`–`C04`; 10-K Item 1A anchor
> `sC5918D6835605DFB9861637AED9AB7C7`, displayed printed p. 25, and MD&A
> anchor `s02DF6574F3035C8485C795D393F48705`, displayed printed p. 38;
> `SRC-0047-C02/C04/C06` independent
> incident/property-damage context.
> **Basis / limits:** Consequence measurement is first-party. The court
> independently confirms context, not the order/backlog values.

> **Claim record — INC-0006-C05 | source-report**
> **Claim:** Merck reports that Gardasil 9 stockpile borrowing was driven by
> both the temporary cyberattack-related shutdown and higher-than-expected
> demand, followed by partial 2017 and remaining 2018 replenishment; the
> $125 million reversal/recognition is not a shortage, patient effect or
> additive cyber-loss measurement.
> **Claim status:** active
> **Scope:** Mixed-cause continuity response and accounting boundary.
> **As of:** 2017–2018.
> **Review after:** 2026-10-15.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** 10-K Vaccines anchor `sBB3EEB5901095A398997106BC9F8CDA1`,
> displayed printed p. 41; `SRC-0046-C05`.
> **Basis / limits:** Both causes and replenishment states are literal; neither
> product shortage nor patient outcome is reported.

> **Claim record — INC-0006-C06 | source-report**
> **Claim:** The court record states that the attack caused property damage and
> that there was no evidence of bodily injury or death; it labels production-
> facility/critical-application outage as Merck's contention.
> **Claim status:** active
> **Scope:** Court-record modalities; not product contamination, clinical
> outcome, manufacturing-output measurement or judicial replication of Merck's
> order figures.
> **As of:** Opinion 2023-05-01.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Opinion p. 9; `SRC-0047-C04`.
> **Basis / limits:** Separate modalities prevent company contention from
> becoming independent judicial measurement.

## Attribution

> **Claim record — INC-0006-C07 | analytic-judgment**
> **Claim:** Kroll, retained by the insurers and organizationally independent
> from Merck, is counted once as an investigative role; its high-confidence
> Russian-linked assessment is preserved as its conclusion, while attribution
> remained disputed and was not adjudicated by the trial or appellate court.
> **Claim status:** active
> **Scope:** Graded attribution/investigation state, not wiki attribution or a
> second investigation created from the court's recitation.
> **As of:** Opinion record through 2023-05-01.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** Opinion p. 10 and attribution-dispute footnote;
> `SRC-0047-C03/C05/C06`.
> **Basis / limits:** Kroll is insurer-retained rather than neutral and its full
> report is not retained. Court and Kroll are not multiplied.

## Response, recovery and defensive lessons

> **Claim record — INC-0006-C08 | analytic-judgment**
> **Claim:** Primary records support bounded lessons at vendor-update trust,
> detection/containment, critical-application/manufacturing availability,
> stockpile/order continuity and recovery-resilience edges, but Merck's generic
> modernization language supplies no safeguard test or effectiveness result.
> **Claim status:** active
> **Scope:** Event-specific control lessons for `THI-CT/CTR-CI`; not an exact
> product configuration, trusted-restoration proof or `BMO/CTR-AE` evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-15.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md),
> opinion pp. 7–10 for the trusted dependency and broad propagation;
> [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md), Item 1A,
> displayed p. 25, for disruption and the issuer-reported modernization and
> resilience effort, MD&A displayed pp. 38–39 for the order/backlog effects,
> and Vaccines displayed p. 41 for the mixed-cause stockpile and replenishment
> indicators.
> **Limits:** Failed/interrupted edges and bounded recovery indicators
> are direct; control design is defensive synthesis and remains unevaluated.

## Criterion contribution and nonpromotions

> **Claim record — INC-0006-C09 | analytic-judgment**
> **Claim:** `INC-0006` is candidate SF3 evidence for `BMO-CI`, the fourth
> technically supported event, fourth control-lesson lineage and one bounded
> Kroll investigation. It creates the fourth sector and sixth INC/review page,
> but not a proven sixth distinguishable event because public evidence does not
> establish that every clinical outcome account represents a distinct event;
> exact transitions require `SYN-0028`.
> **Claim status:** superseded
> **Scope:** Candidate contribution before strict synthesis, not source-count
> promotion or a claim for `THI-WL/TV/XT/CI/GR`, `BMO-AE`, `CTR-AE` or the
> global incident gate.
> **As of:** 2026-07-12.
> **Review after:** 2026-07-26.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `INC-0006-C01`–`C08`; frozen BMO/THI/CTR criteria and source
> floors.
> **Basis / limits:** Counts, roles and missing predicates are explicit; court,
> Kroll and filing remain one incident ecosystem.
> **Superseded by:** `SYN-0028-C05/C08`–`C12`, after conservative event-
> identity, incident and control-threshold reconciliation.

## Safety boundary

This page contains no indicator, malware code or actionable/low-level malware
behavior, endpoint, credential, vulnerable version, exploit sequence,
network/facility topology, manufacturing setting, recipe or operational
response instruction. Only high-level broad propagation is retained.

> **Claim record — INC-0006-C10 | analytic-judgment**
> **Claim:** This page contains no indicator, malware code or actionable/
> low-level malware behavior, endpoint, credential, vulnerable version,
> exploit sequence, network/facility topology, manufacturing setting, recipe
> or operational response instruction. Only high-level broad propagation is
> retained.
> **Claim status:** stale
> **Scope:** Local page.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** Local page content; no external source is applicable to this
> editorial self-audit.
> **Limits:** Retained as a historical local-content audit, not as an
> externally evidenced decision claim. The current safety boundary is the
> prose above.

## Related pages

- [RSK-0019](../risk-scenarios/rsk-0019-merck-cyber-manufacturing-supply-disruption.md)
- [CTL-0020](../controls/ctl-0020-merck-incident-vendor-update-continuity-recovery-lessons.md)
- [VUL-0003](../vulnerabilities/vul-0003-biomanufacturing-data-integrity-ot-access-dependencies.md)
- [WFL-0003](../workflows/wfl-0003-biopharmaceutical-manufacturing-digital-thread.md)
- [AST-0007](../assets/ast-0007-biomanufacturing-assets-stakeholders.md)
- [SYN-0028](../syntheses/syn-0028-biomanufacturing-scope-threat-incident-governance-reconciliation.md)

## Sources

- [SRC-0046](../sources/src-0046-merck-2018-form-10k-notpetya-impact.md)
- [SRC-0047](../sources/src-0047-new-jersey-merck-notpetya-insurance-opinion-2023.md)
