---
id: WFL-0004
type: workflow
title: Lifecycle of high-consequence and biosecurity-relevant laboratory material
aliases:
  - laboratory biosecurity material lifecycle
  - high-consequence material custody lifecycle
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0004
sensitivity: public
dual_use: moderate
relations:
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: WFL-0004-C01
    evidence:
      - source: SRC-0004
        locator: "§§1.1–1.2, printed pp. 2–3 (PDF pp. 22–23); §§6.3–7.3.5, printed pp. 31–44 (PDF pp. 51–64)"
  - predicate: governed-by
    target: GOV-0001
    claim_id: WFL-0004-C04
    evidence:
      - source: SRC-0004
        locator: "§1.1, printed p. 3 (PDF p. 23); §§4–4.2.2, printed pp. 12–16 (PDF pp. 32–36); §8.1, printed pp. 45–51 (PDF pp. 65–71)"
tags:
  - laboratories
  - biosecurity
  - lifecycle
  - inventory
  - custody
  - information
---

# Lifecycle of high-consequence and biosecurity-relevant laboratory material

> WHO 2024 defines a broad horizontal lifecycle for material, technology, and
> information: collection, transport, processing, storage, and, where needed,
> destruction. This page adds only source-supported governance and
> accountability gates; it is not a validated chain-of-custody implementation.

## Scope

`WFL-0004` covers high-consequence material and broader biosecurity-relevant
material in diagnostic, research, mobile, manufacturing/pharmaceutical, and
related laboratory settings. For WHO, a laboratory may include repositories,
waste-handling areas, and sample-collection locations (Glossary, printed
pp. xv–xvi; PDF pp. 17–18).

This is a general lifecycle. It does not replace an assay-specific workflow,
clinical chain of identity, biobank consent/governance, manufacturing QMS, or
jurisdiction-specific transport law.

## Lifecycle model

| Phase | Source-supported objective | Evidence not yet established |
| --- | --- | --- |
| Plan and authorize | Define scope, assess biosafety/biosecurity risks, identify accountable roles and approve work | Complete project portfolio, funder decision logic and jurisdictional authorization |
| Collect or receive | Bring material and associated information into controlled institutional handling | Universal identity, consent, provenance and acceptance schema |
| Process or use | Conduct diagnostics, research, storage-only activity or manufacturing under assessed controls | Procedure-level flows, parameters and technical architecture |
| Store and inventory | Maintain accountability, authorized access, records, reconciliation and review | Validated LIMS implementation, data model and measured discrepancy rate |
| Transfer or transport | Preserve authorization, responsibility, custody and receipt reconciliation across a boundary | Current legal requirements in each route/jurisdiction and implementation evidence |
| Retain, dispose or destroy | Resolve material, equipment, media, software and record obligations using validated local processes | Universal retention periods, disposal method or proof of effective execution |
| Detect, respond and learn | Report suspected events/near misses, investigate, correct and review controls | Observed incident corpus and measured recovery/corrective-action effectiveness |

> **Claim record — WFL-0004-C01 | source-report**
> **Claim:** WHO's horizontal laboratory-biosecurity scope explicitly spans
> collection, transport, processing, storage and, where necessary, destruction
> of high-consequence and other biosecurity-relevant material across several
> laboratory settings.
> **Claim status:** active
> **Scope:** General advisory lifecycle, not every laboratory's operating model.
> **As of:** 2024-06-21.
> **Review after:** 2027-01-08.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§1.1–1.2, printed pp. 2–3 (PDF pp. 22–23); §§6.3–7.3.5,
> printed pp. 31–44 (PDF pp. 51–64).
> **Basis / limits:** Stages are explicit; plan/authorize and incident learning
> are connected from programme/risk sections. Source does not present a single
> end-to-end implementation or empirical validation.

## Parallel asset flows

The lifecycle must track more than physical samples:

- **material:** biological agents, derivatives, reagents/intermediates and
  high-consequence or otherwise biosecurity-relevant material;
- **information:** identity/provenance, inventory, research/process records,
  sequence or other sensitive data, authorizations and transfer/disposal records;
- **equipment/software:** devices that handle material or retain/generate
  biosecurity-relevant data and software;
- **decision/accountability:** responsibility, approval, access, review,
  discrepancy disposition, incident escalation and final closeout.

> **Claim record — WFL-0004-C02 | source-report**
> **Claim:** WHO recommends updated inventory and accountability records,
> controlled access, discrepancy investigation, authorization and custody/receipt
> reconciliation across storage and transfer/transport.
> **Claim status:** active
> **Scope:** Control objectives for high-consequence and biosecurity-relevant
> material; operational detail withheld.
> **As of:** 2024-06-21.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§6.3–6.3.2, printed pp. 31–33 (PDF pp. 51–53); §7.3,
> printed pp. 41–44 (PDF pp. 61–64).
> **Basis / limits:** Objectives are direct recommendations. Source gives no
> implementation sample, error rate, digital-ledger design or effectiveness
> result.

> **Claim record — WFL-0004-C03 | source-report**
> **Claim:** WHO extends closeout accountability to equipment, storage media,
> software and information, requiring locally validated decontamination,
> disposal or data-removal processes and records appropriate to assessed risk.
> **Claim status:** active
> **Scope:** Defensive lifecycle objective, not a universal disposal technique.
> **As of:** 2024-06-21.
> **Review after:** 2026-10-10.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§6.4–6.4.2, printed pp. 33–34 (PDF pp. 53–54).
> **Basis / limits:** Source recognizes residual material/data and recordkeeping.
> Specific biological destruction and media-sanitization procedures require
> local validation and are intentionally not reproduced.

## Decision and governance gates

At high level the source supports these gates:

1. institutional policy assigns responsibility and communication;
2. risk assessment informs whether work proceeds and what controls apply;
3. IBC/authorized leadership reviews relevant work and residual risk;
4. inventory/transfer/disposal decisions remain attributable and reviewable;
5. national oversight supplies applicable requirements and receives defined
   feedback for high-consequence work;
6. incidents and near misses feed corrective action and reassessment.

> **Claim record — WFL-0004-C04 | analytic-judgment**
> **Claim:** `WFL-0004` is governed at two connected levels in the WHO model:
> institutional review/accountability handles local lifecycle decisions, while
> national oversight sets risk-informed requirements and receives feedback;
> actual authority depends on local law and adoption.
> **Claim status:** active
> **Scope:** Reconciliation of WHO programme, lifecycle and two-tier governance
> sections.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §1.1, printed p. 3 (PDF p. 23); §§4–4.2.2, printed pp. 12–16
> (PDF pp. 32–36); §8.1, printed pp. 45–51 (PDF pp. 65–71);
> Figure 8.1.
> **Basis / limits:** WHO explicitly links the levels. `GOV-0001` is advisory;
> no universal legal authority or adoption is inferred.

## Trust boundaries and transfer points

Candidate boundaries requiring local validation include:

- collection site or provider ↔ receiving laboratory;
- laboratory ↔ repository or off-site storage;
- material custody ↔ inventory/information system;
- laboratory ↔ internal/external transport function;
- sender ↔ carrier ↔ recipient;
- active work/storage ↔ waste, disposal or destruction process;
- institution ↔ regulator or external emergency/assurance function.

These are lifecycle handoffs, not confirmed vulnerabilities. Wiki omits routes,
timing, quantities, storage locations, access configurations and response contact
chains.

## Incident and review loop

WHO templates share a defensive lifecycle: detect or receive a report, escalate,
secure the situation, investigate, report/review and improve. It also recommends
near-miss reporting and reassessment after material, personnel, equipment,
facility or knowledge changes.

> **Claim record — WFL-0004-C05 | analytic-judgment**
> **Claim:** Current evidence supports a reusable material/information lifecycle
> and review loop, but not a complete digital lineage, biobank governance model,
> clinical chain of identity, manufacturing release workflow or quantified
> assurance level.
> **Claim status:** active
> **Scope:** Wiki coverage assessment after `SRC-0004`.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§1.1–1.2, printed pp. 2–3; §§6.3–7, printed pp. 31–44; Annexes 1–2,
> printed pp. 59–82.
> **Basis / limits:** Guidance supplies categories, objectives and templates but
> no implementation architecture. Absence here is a corpus gap, not evidence
> that real institutions lack these processes.

## Related pages

- [WFL-0009 — human-biobank material/data/consent lifecycle](wfl-0009-biospecimen-material-data-lifecycle.md)
- [AST-0005 — laboratory/biobank asset and stakeholder classes](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md)
- [SYN-0010 — laboratory/biobank reconciliation](../syntheses/syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md)
- [SRC-0019 — Canadian Biosafety Standard](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [GOV-0009 — Canadian CBS governance](../governance/gov-0009-canadian-biosafety-standard-third-edition.md)

- [GOV-0001 — WHO Laboratory Biosecurity Guidance 2024](../governance/gov-0001-who-laboratory-biosecurity-guidance-2024.md)
- [CTL-0001 — Risk-based laboratory information and cybersecurity controls](../controls/ctl-0001-risk-based-laboratory-information-cybersecurity.md)
- [WFL-0002 — HCL cyberphysical workflow](wfl-0002-high-containment-laboratory.md)
- [SRC-0004 — WHO Laboratory Biosecurity Guidance 2024](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SYN-0007 — WHO custody/NIST technical laboratory-control stitch](../syntheses/syn-0007-ot-applicability-cyberbio-sectors.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
  §§1, 4–8; Annexes 1–2.
