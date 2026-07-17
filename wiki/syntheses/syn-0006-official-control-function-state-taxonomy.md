---
id: SYN-0006
type: synthesis
title: Official control-function and evidence-state taxonomy
aliases:
  - prevent detect respond recover assure control taxonomy
  - recommended implemented tested effective control ladder
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-10
source_ids:
  - SRC-0004
  - SRC-0006
  - SRC-0008
  - SRC-0016
  - SRC-0017
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: SYN-0006-C01
    evidence:
      - source: SRC-0004
        locator: "§5.1, printed pp. 19–20 (PDF pp. 39–40); §§6.5–6.6, printed pp. 34–39 (PDF pp. 54–59); Annexes 1–2"
  - predicate: evidenced-by
    target: SRC-0006
    claim_id: SYN-0006-C01
    evidence:
      - source: SRC-0006
        locator: "§§3.2–3.3, printed pp. 16–19 (PDF pp. 27–30); §6 and Figure 4, printed pp. 29–31 (PDF pp. 40–42); Tables 4–36"
  - predicate: evidenced-by
    target: SRC-0017
    claim_id: SYN-0006-C01
    evidence:
      - source: SRC-0017
        locator: "§§V–VI, printed pp. 9–30 (PDF pp. 13–34); Appendix 1, printed pp. 38–46 (PDF pp. 42–50)"
tags:
  - controls
  - canonical-taxonomy
  - evidence-maturity
  - assurance
  - framework-reconciliation
---

# Official control-function and evidence-state taxonomy

## Purpose

This synthesis reconciles three materially independent official control
lineages—WHO laboratory guidance, NIST's draft genomic CSF/PF profile and FDA
medical-device guidance—into the wiki's functional model. EHDS supplies a
separate binding-design comparator, and NHSBT supplies a bounded implementation
example. Neither is treated as implementation of the three frameworks.

## Canonical function mapping

| Canonical function | FDA medical devices | NIST genomic CSF/PF profile | WHO laboratory biosecurity | Normalization boundary |
| --- | --- | --- | --- | --- |
| Govern/inventory prerequisite | risk ownership, threat model, architecture, SBOM, lifecycle plans | Govern/Identify and Current/Target Profile tailoring | governance, risk assessment, inventories and responsibilities | Enables selection; is not itself incident prevention |
| Prevent | authentication, authorization, cryptography, confidentiality, integrity and trustworthy updates | Protect plus selected Govern/Identify outcomes | physical/personnel/access, inventory, information/cyber and transport safeguards | Scope and asset dependencies differ |
| Detect | event detection/logging, anomaly/vulnerability monitoring and verification | Detect and relevant privacy processing review | monitoring, reporting, audit/tests and near-miss recognition | Required capability or recommendation is not measured detection |
| Contain/respond | vulnerability handling, communication and product/field response | Respond | alert/escalation, containment, investigation and corrective action | Safe intervention remains context-specific |
| Recover | resiliency, trusted restore and update/patch lifecycle | Recover | recovery preparation, continuity, review and learning | Restore availability does not prove trustworthy clinical/biological state |
| Assure | traceability, architecture views, verification/validation, testing and labeling | Current/Target assessment and Govern/Identify evidence expectations | periodic risk/control review, audit, tests and exercises | Requested assessment is not a passed result |

> **Claim record — SYN-0006-C01 | analytic-judgment**
> **Claim:** Independent FDA, NIST and WHO lineages can be normalized to
> govern/inventory, prevent, detect, contain/respond, recover and assure while
> preserving their device, genomic-data and laboratory scopes.
> **Claim status:** active
> **Scope:** Canonical defensive function taxonomy for the current corpus; not
> framework equivalence, compliance mapping or universal control sufficiency.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§V–VI, printed pp. 9–30 (PDF pp. 13–34); Appendix 1, printed
> pp. 38–46 (PDF pp. 42–50);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§3.2–3.3, printed pp. 16–19 (PDF pp. 27–30); §6 and Figure 4,
> printed pp. 29–31 (PDF pp. 40–42); Tables 4–36;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §5.1, printed pp. 19–20 (PDF pp. 39–40); §§6.5–6.6,
> printed pp. 34–39 (PDF pp. 54–59); Annexes 1–2.
> **Basis / limits:** Source function families are direct; normalization is
> editorial. It does not import underlying standards that are merely cited.

## Exact FDA category reconciliation

FDA's eight Appendix 1 categories remain visible rather than being replaced by
the canonical functions:

| FDA category | Primary canonical role | Secondary role/qualification |
| --- | --- | --- |
| Authentication | Prevent | Supplies evidence/log context only if events are recorded |
| Authorization | Prevent | Least privilege and role boundaries require correct identity/state |
| Cryptography | Prevent | Can support integrity/confidentiality; implementation quality unknown |
| Code, data and execution integrity | Prevent | Integrity monitoring can also detect deviation |
| Confidentiality | Prevent | FDA notes general PHI confidentiality can be governed elsewhere |
| Event detection and logging | Detect | Enables response/forensics but does not ensure action |
| Resiliency and recovery | Contain/respond; recover | Safe degraded state and restore are device/use-specific |
| Firmware and software updates | Prevent; recover | Update can remediate or introduce availability/safety risk |

> **Claim record — SYN-0006-C02 | analytic-judgment**
> **Claim:** FDA's eight categories map many-to-many to the canonical
> functions; a category label alone does not establish an exact control,
> implementation state or clinical outcome.
> **Claim status:** active
> **Scope:** FDA category normalization, not product architecture or control
> selection advice.
> **As of:** 2026-07-12.
> **Review after:** 2027-01-08.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §V.B.1, printed pp. 21–22 (PDF pp. 25–26); Appendix 1, printed
> pp. 38–46 (PDF pp. 42–50); `CTL-0010-C01`–`C06`.
> **Basis / limits:** Category functions and cautions are direct; the compact
> crosswalk is editorial and no crosswalk is compliance/effectiveness evidence.

## Evidence-state ladder

| State | Acceptance meaning | Current example/boundary |
| --- | --- | --- |
| Recommended | An official source proposes an outcome, control or process for its scope | FDA, NIST draft profile and WHO guidance; no deployment follows |
| Binding design | An in-scope legal instrument requires a capability/process | Staged EHDS and separately scoped FDA-cited duties; no compliance follows |
| Implemented | Direct evidence shows a bounded organization used or deployed the safeguard/action | NHSBT used one continuity response; not implementation of FDA/NIST/WHO profiles |
| Tested | A scoped method, comparator/baseline where appropriate and result exercise the safeguard | Unknown for the represented framework controls; a testing requirement is not a result |
| Effective | Outcome evidence supports benefit within stated causal and measurement limits | Unknown here; first-party continuity language is not an independent causal evaluation |
| Independently evaluated | A materially independent evaluator assesses implementation/outcome with limits | Unknown for these controls |

> **Claim record — SYN-0006-C03 | analytic-judgment**
> **Claim:** The corpus separates recommended, binding-design, implemented,
> tested, effective and independently evaluated states; evidence moves upward
> only when the next state's own contract is met.
> **Claim status:** active
> **Scope:** Canonical evidence maturity, not a maturity score or assertion that
> every control should reach every state.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§V.C and VII.E, printed pp. 25–27, 36–37 (PDF pp. 29–31, 40–41);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§3.2–3.3 and 6, printed pp. 16–19, 29–31;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§6 introduction and 6.6, printed pp. 24, 37–39;
> [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md), Articles 36–46,
> 59, 73 and 99–105, PDF pp. 50–55, 63–64, 75–76, 88–91;
> [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md), pp. 22, 92, 97.
> **Basis / limits:** Modalities and the bounded NHSBT action are direct; the
> ladder is editorial. NHSBT supplies neither a framework adoption claim nor
> independent effectiveness evidence.

## CTR-ST acceptance finding

> **Claim record — SYN-0006-C04 | analytic-judgment**
> **Claim:** The current corpus satisfies `CTR-ST`: independent FDA, NIST and
> WHO official lineages are reconciled into a canonical functional taxonomy,
> and their recommended/design states are explicitly separated from
> implemented, tested and effective evidence.
> **Claim status:** active
> **Scope:** Frozen `CTR-ST` criterion in `SYN-0001`; not control completeness,
> framework equivalence or evidence that any represented control is effective.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md);
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md);
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md);
> `SYN-0006-C01`–`C03`; frozen `CTR-ST` row.
> **Basis / limits:** Three independent official lineages satisfy SF2. The
> ladder records missing higher states instead of inferring them from framework
> language; `CTR-AE` remains separate and unpassed.

## Crosswalk limits

- Function similarity does not transfer legal obligations or compliance.
- A framework reference does not ingest the referenced standard.
- Draft priorities are not risk or maturity scores.
- Binding design is not adoption; implementation is not a test.
- Test completion does not by itself establish effectiveness.
- Source-reported continuity is not independent causal evaluation.
- Product/laboratory/genomic controls must still map to exact scenario edges.

> **Claim record — SYN-0006-C05 | analytic-judgment**
> **Claim:** This taxonomy supports comparison and exact-edge mapping only;
> crosswalk membership cannot establish applicability, compliance, testing or
> effectiveness.
> **Claim status:** active
> **Scope:** Use limitation for this synthesis.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYN-0006-C01`–`C04`; source modality/evidence limits in
> `SRC-0004-C07`, `SRC-0006-C06/C11`, `SRC-0017-C03/C08/C10` and
> `SRC-0016-C10`.
> **Basis / limits:** The prohibition follows from preserved source modalities
> and evidence contracts. It is not a claim that mappings are useless.

## Related pages

- [SYN-0024 — Cross-sector portfolio reconciliation](syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [SYN-0022 — Foundational consequence/assurance calibration](syn-0022-foundational-consequence-assurance-calibration.md)

- [SRC-0004 — WHO laboratory guidance](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0006 — NIST IR 8467 draft profile](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0017 — FDA device guidance](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
- [SRC-0016 — EHDS Regulation](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0008 — NHSBT implementation example](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [CTL-0001 — Laboratory controls](../controls/ctl-0001-risk-based-laboratory-information-cybersecurity.md)
- [CTL-0002 — Genomic controls](../controls/ctl-0002-genomic-data-risk-management.md)
- [CTL-0009 — EHDS safeguards](../controls/ctl-0009-ehds-health-data-and-ehr-safeguards.md)
- [CTL-0010 — FDA medical-device controls](../controls/ctl-0010-medical-device-cybersecurity-lifecycle-controls.md)
- [SYN-0005 — Clinical-health governance reconciliation](syn-0005-global-us-eu-clinical-health-governance.md)
- [SYN-0007 — Exact cross-sector OT control-edge matrix](syn-0007-ot-applicability-cyberbio-sectors.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0008](../sources/src-0008-nhsbt-annual-report-2024-2025.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
