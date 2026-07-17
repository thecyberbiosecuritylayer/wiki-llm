---
id: SYN-0007
type: synthesis
title: Applicability limits of general OT security across cyberbiosecurity sectors
aliases:
  - NIST OT cyberbio sector applicability
  - cross-sector OT control edge matrix
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-08-11
source_ids:
  - SRC-0002
  - SRC-0003
  - SRC-0004
  - SRC-0005
  - SRC-0006
  - SRC-0010
  - SRC-0014
  - SRC-0016
  - SRC-0017
  - SRC-0018
  - SRC-0031
sensitivity: public
dual_use: low
relations:
  - predicate: evidenced-by
    target: SRC-0018
    claim_id: SYN-0007-C01
    evidence:
      - source: SRC-0002
        locator: "HCL dependency analysis and Table 1"
      - source: SRC-0003
        locator: "Digital Information Flow in Biomanufacturing and Figure 1"
      - source: SRC-0004
        locator: "§§6.3–6.6, printed pp. 31–39 (PDF pp. 51–59); §7, printed pp. 40–44 (PDF pp. 60–64)"
      - source: SRC-0010
        locator: "HTML #s1-1, #s1-4 and #s3-1–2; Tables 1–2"
      - source: SRC-0018
        locator: "§§1.1, 2.3, 4–6 and Appendix F"
  - predicate: evidenced-by
    target: SRC-0031
    claim_id: SYN-0007-C10
    evidence:
      - source: SRC-0018
        locator: "§§5.2.3, 5.4 and 6.1–6.5, printed pp. 71–75, 83–138 (PDF pp. 88–92, 100–155)"
      - source: SRC-0031
        locator: "Part I §§3.1–4.9, printed pp. 2–12 (physical pp. 7–17); Annex III §§2–3, printed pp. 28–30 (physical pp. 33–35); Annex V, printed pp. 37–41 (physical pp. 42–46)"
tags:
  - operational-technology
  - applicability
  - cross-sector-controls
  - laboratory
  - biomanufacturing
  - agriculture
---

# Applicability limits of general OT security across cyberbiosecurity sectors

## Applicability rule

A generic OT safeguard transfers to a cyberbiosecurity sector only when an
independent sector source establishes the relevant process, physical, custody
or decision dependency. A component name, critical-infrastructure label or
notional topology is not enough to establish a sector architecture,
vulnerability, consequence or control result.

> **Claim record — SYN-0007-C01 | analytic-judgment**
> **Claim:** General OT guidance can support exact cyberbio control mappings
> only after an independent sector lineage establishes the corresponding
> dependency/path and the mapping preserves sector-specific missing limbs.
> **Claim status:** active
> **Scope:** Applicability method for LAB, BMO and AGE in this transaction; not
> a universal cross-sector control transfer rule.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> HCL dependency analysis/Table 1;
> [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Digital Information Flow/Figure 1;
> [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1-1`, `#s1-4`, `#s3-1–2` and Tables 1–2;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§1.1, 2.3, 4–6 and Appendix F.
> **Basis / limits:** Sector dependencies and NIST's generic scope/tailoring
> boundary are direct; the transfer rule is editorial. It never creates
> deployment or effectiveness evidence.

## Historical pre-Q13 biomanufacturing quality-gate state

Guttieres establishes measurement/action, PLC/DCS/SCADA and process/quality
data dependencies; NIST independently names pharmaceutical DCS and supplies
architecture, access, integrity, monitoring, safety-aware response and recovery
functions. The combination maps `CTL-0011` to `RSK-0002`, but does not supply
GMP/QMS, batch-release authority, deviation/CAPA, validated quality decisions
or product-disposition gates.

| BMO edge | NIST/sector function | Evidence boundary |
| --- | --- | --- |
| Unknown asset/flow/boundary → unmanaged control dependency | inventory, ownership and boundary mapping | Generic architecture only |
| Unauthorized/incorrect digital state → changed process state | access, configuration, segmentation and integrity controls | No validated recipe/QMS/release path |
| Hidden anomaly → unrecognized process/quality state | passive monitoring, logs and process/network baselines | No bioprocess detection metric |
| Detected condition → unsafe/quality consequence | independent safety, response authority and safe/manual operation | No GMP quality-hold/disposition evidence |
| Loss/corruption → untrusted recovery | verified backup/restore, graceful degradation and testing | No validated process/product disposition after restore |

> **Claim record — SYN-0007-C02 | analytic-judgment**
> **Claim:** NIST closes the generic BMO OT architecture/control portion but
> `BMO-CT` remains Partial because complete safety/quality, GMP release and
> trustworthy product-disposition gates are absent.
> **Claim status:** superseded
> **Scope:** `SYS-0002/RSK-0002/CTL-0011`; no facility, product or compliance
> conclusion.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Digital Information Flow/Figure 1 and source limitations;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.3, 5.2.3, 5.4, 6.1–6.5 and Appendix F;
> `SYS-0002-C04`, `RSK-0002-C04`, `CTL-0011-C02`, `WFL-0003-C04`.
> **Basis / limits:** Generic control coverage and missing sector gates are
> explicit. Component similarity cannot manufacture the missing quality limb.
> Historical after-`SRC-0018` assessment; superseded by `SYN-0007-C09` after
> Q13.
> **Superseded by:** `SYN-0007-C09`.

## Q13 quality-gate update

Q13 and [CTL-0015](../controls/ctl-0015-continuous-manufacturing-quality-control.md)
now supply the previously absent process monitoring, material trace/diversion,
quality hold/disposition, release/reference-test, validation and PQS/CAPA limb.
They do not retroactively turn NIST into GMP guidance or establish one deployed
combined control stack.

| BMO edge | Generic OT layer | Q13 quality layer | Remaining state |
| --- | --- | --- | --- |
| unauthorized/incorrect digital state → process action | access/configuration/segmentation/integrity | validated process/model premise and acceptance criteria | design-level stitch only |
| hidden condition → unrecognized quality state | passive monitoring/logs/baselines | PAT/sampling/trend/data-gap/reference-test gates | no deployment metric |
| detected condition → continued affected material | safe response/isolation | pause, traceable diversion, quarantine, investigation/CAPA | no observed containment result |
| restoration → resumed process/product use | trusted restore and configuration validation | collection-restart criteria plus material disposition/release | no tested combined recovery |

> **Claim record — SYN-0007-C09 | analytic-judgment**
> **Claim:** Independent NIST and ICH Q13 lineages now provide the complete
> generic-OT plus continuous-manufacturing quality/release/disposition control
> limbs, but `BMO-CT` remains Partial in this source transaction pending a
> separately reserved frozen-cell reconciliation.
> **Claim status:** superseded
> **Scope:** Historical `RSK-0002` control-design corpus at the `SRC-0031`
> source checkpoint; not implementation, compliance, effectiveness or a
> source-transaction score change.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-10.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§5.2.3, 5.4 and 6.1–6.5, printed pp. 71–75, 83–138;
> [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md), Part I
> §§3.1–4.9, printed pp. 2–12 (physical pp. 7–17); Annex III §§2–3,
> printed pp. 28–30 (physical pp. 33–35); Annex V, printed pp. 37–41
> (physical pp. 42–46); `CTL-0011-C02`, `CTL-0015-C01`–`C06`.
> **Basis / limits:** The two direct layers and their exact edges are explicit;
> the normalized conjunction is editorial. Binary promotion requires the
> dedicated synthesis and independent rubric audit. Historical `SRC-0031`
> source-transaction conclusion; superseded by `SYN-0007-C10` after the
> independently audited `SYN-0016` decision.
> **Superseded by:** `SYN-0007-C10`.

> **Claim record — SYN-0007-C10 | analytic-judgment**
> **Claim:** Independent NIST and ICH Q13 lineages supply the complete generic-
> OT plus continuous-manufacturing quality/release/disposition control limbs,
> and `SYN-0016-C05` subsequently adjudicates their exact-edge reconciliation
> as sufficient for `BMO-CT` while implementation and effectiveness remain
> unknown.
> **Claim status:** active
> **Scope:** Current frozen `BMO-CT` evidence sufficiency for `RSK-0002`; not a
> deployed combined stack, regional compliance, completed test or safeguard
> result.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.3, 2.4, 4.2.2, 5.2.3, 5.4 and 6.1–6.5, printed pp. 19–21,
> 28–32, 55, 71–75, 83–138; [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1–4.9, printed pp. 2–12/physical pp. 7–17; Annex III
> §§2–3, printed pp. 28–30/physical pp. 33–35; Annex V §§3.1–3.3,
> printed pp. 38–41/physical pp. 43–46;
> [SYN-0016](syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md),
> `SYN-0016-C01/C05/C07`.
> **Basis / limits:** NIST and Q13 contribute complementary independent direct
> layers; the conjunction and frozen-cell decision are editorial. Acceptance
> establishes design-level evidence sufficiency only.

## Laboratory two-limb control stitch

`LAB-CT` requires both material custody/accountability and technical controls.
WHO supplies the first; NIST supplies the second. They remain distinct:

| Required limb | Exact lifecycle/scenario edge | Control basis | Limitation |
| --- | --- | --- | --- |
| Inventory/custody | `WFL-0004` store/inventory → transfer/custody/receipt → disposition | WHO responsibility, records, reconciliation, controlled transfer/receipt/disposal | NIST is not HCL custody guidance |
| Access | `RSK-0001` digital-origin precondition | NIST identity/access enforcement (§6.2.1) plus WHO local responsibility | No facility identity implementation |
| Segmentation/independence | origin → containment-support transfer | NIST DMZ/zoning (§5.2.3), access boundaries and independent safety (§4.2.2) | No validated containment architecture |
| Monitoring | altered/unavailable state → unrecognized transfer | NIST passive monitoring/logging (§6.3) plus WHO reporting | No detection metric |
| Containment/response | recognized condition → potential physical/biological consequence | NIST OT-aware response (§6.4) plus WHO escalation/investigation/corrective action | Safe intervention is facility-specific |
| Recovery | contained state → trustworthy digital/physical/material service | NIST recovery (§6.5) plus WHO continuity/disposition/review | No recovery-time or biological safe-state test |

> **Claim record — SYN-0007-C03 | analytic-judgment**
> **Claim:** The current corpus satisfies `LAB-CT`: independent WHO and NIST
> lineages jointly map inventory/custody, access, segmentation, monitoring,
> containment/response and recovery to exact `WFL-0004` and `RSK-0001` edges,
> with implementation/effectiveness kept separate.
> **Claim status:** active
> **Scope:** Frozen `LAB-CT` criterion; not biobank control completeness,
> facility validation or `LAB-AE` evidence.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§6.3–6.4.2, printed pp. 31–34 (PDF pp. 51–54); §7,
> printed pp. 40–44 (PDF pp. 60–64); `SRC-0004-C09`;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §5.2.3, printed pp. 71–75; §6.2.1, printed pp. 97–108;
> §§6.3–6.5, printed pp. 126–138;
> `WFL-0004-C02`, `RSK-0001-C05`, `CTL-0001-C06`, `CTL-0011-C03`.
> **Basis / limits:** The two required limbs and exact edges are explicit and
> independently sourced. NIST does not establish custody/containment and WHO
> does not validate the technical deployment.

## Agriculture applicability and unresolved sector limbs

Drape supports a bounded monitoring/equipment/production path; NIST supports
generic IIoT, remote access, monitoring, response and recovery. The combination
still lacks One Health breadth, veterinary/plant labs, traceability/surveillance
architecture, ecological/biological hazard controls and a reverse input→decision
path. No AGE cell passes in this transaction.

> **Claim record — SYN-0007-C04 | analytic-judgment**
> **Claim:** NIST strengthens the generic technical branch of `RSK-0007` but
> cannot close `AGE-CT` or another AGE cell without the missing traceability,
> biological-biosecurity, One Health and outcome evidence.
> **Claim status:** active
> **Scope:** `SYS-0005/RSK-0007/CTL-0005/CTL-0011`; no farm deployment or
> sector-wide conclusion.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1-1`, `#s1-4`, `#s3-1–2` and Tables 1–2;
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§2.3.8, 5.3, 6.2.9–6.2.10 and 6.3–6.5;
> `SYS-0005-C03`, `RSK-0007-C05`, `CTL-0005-C04`, `CTL-0011-C04`.
> **Basis / limits:** Technical overlap and missing sector categories are
> direct. The applicability inference does not establish control use.

## Canonical function-to-edge matrix

`SYN-0006` defines the function and evidence-state taxonomy; this transaction
adds named scenario-edge mappings:

| Function | Named exact-edge examples | Control claims | Prerequisite/tradeoff |
| --- | --- | --- | --- |
| Prevent | `RSK-0001` digital origin→containment support; `RSK-0002` control/data→process; `RSK-0012` security state→device function | `CTL-0001-C06`, `CTL-0011-C02/C03`, `CTL-0010-C02` | Correct scope, identity, architecture and safe operating constraints |
| Detect | `RSK-0009/0010` input/parser and cross-sample edges; `RSK-0002/0007` hidden OT state | `CTL-0007-C03`, `CTL-0011-C02/C04` | Passive/validated monitoring; blind spots and false signals remain |
| Contain/respond | `RSK-0001` recognized condition before physical/biological transfer; `RSK-0012` device condition before clinical action | `CTL-0011-C03`, `CTL-0010-C04` | Disconnect/shutdown can worsen safety or care |
| Recover | `RSK-0002/0007` disrupted process/equipment state; `RSK-0012` untrusted device state | `CTL-0011-C02/C04`, `CTL-0010-C04` | Restore must re-establish trustworthy digital and physical/decision state |
| Assure | test the claimed interruption at `RSK-0009` input→parser/execution, `RSK-0001` digital state→containment-support transfer and `RSK-0012` device function→clinical action | `CTL-0007-C04`, `CTL-0001-C06`, `CTL-0010-C05/C07`, `CTL-0011-C06/C07` | Recommended assessment is not a result; each edge needs scoped safety/acceptance criteria |

> **Claim record — SYN-0007-C05 | analytic-judgment**
> **Claim:** The current corpus satisfies `FND-CT`: a canonical prevent,
> detect, contain/respond, recover and assure model is mapped to named scenario
> edges with prerequisites and evidence-state limits across independent
> lineages.
> **Claim status:** active
> **Scope:** Frozen `FND-CT` criterion; not universal sector control coverage or
> effectiveness.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SYN-0006](syn-0006-official-control-function-state-taxonomy.md),
> `SYN-0006-C01/C03`; matrix and exact control/scenario claims above;
> [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> HCL dependency analysis/Table 1;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§6.3–6.6 and §7, printed pp. 31–44;
> [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Digital Information Flow/Figure 1;
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§2.1, 4.1, 4.4 and 5–6;
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§3.2–3.3, 5–6 and Tables 4–36;
> [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §§3, 5–6, printed pp. 769–776 (PDF pp. 6–13);
> [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1-1`, `#s1-4`, `#s3-1–2` and Tables 1–2;
> [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§V–VII, printed pp. 9–37 (PDF pp. 13–41);
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§3.3.8–3.3.9, 4.3.4–4.3.7, 5–6 and Appendix F.
> **Basis / limits:** Functions, named edges and qualifications are explicit.
> Higher assurance remains unknown and is evaluated separately.

## Five-sector portfolio

| Sector | Scenario(s) and controls | All five functions | Material prerequisites/tradeoffs |
| --- | --- | --- | --- |
| LAB | `RSK-0001`; `CTL-0001/0011` | prevent, detect, contain/respond, recover, assure | WHO custody + generic NIST technical stitch; facility safe state unknown |
| BMO | `RSK-0002`; `CTL-0011/0015` | prevent, detect, contain/respond, recover, assure | generic OT + Q13 quality/release stitch; design only, no deployment/test metric |
| GEN | `RSK-0003/0004/0005/0009/0010`; `CTL-0002/0007` | prevent, detect, contain/respond, recover, assure | data/sample provenance and privacy scope; higher assurance unknown |
| AGE | `RSK-0007`; `CTL-0005/0011` | prevent, detect, contain/respond, recover, assure | bounded farm branch; One Health/traceability absent |
| CPH | `RSK-0012`; `CTL-0010` | prevent, detect, contain/respond, recover, assure | FDA device scope; intervention can disrupt care |

> **Claim record — SYN-0007-C06 | analytic-judgment**
> **Claim:** The current portfolio satisfies `CTR-CT`: all five control
> functions are mapped to exact scenarios in LAB, BMO, GEN, AGE and CPH with
> sector prerequisites, failure modes and tradeoffs.
> **Claim status:** active
> **Scope:** Frozen cross-sector portfolio criterion; a sector's portfolio
> inclusion does not mean every sector-specific CT or AE cell passes.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md),
> HCL dependency analysis/Table 1;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§6.3–6.6 and §7, printed pp. 31–44;
> [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md),
> Digital Information Flow/Figure 1;
> [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md),
> §§2.1, 4.1, 4.4 and 5–6;
> [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§3.2–3.3, 5–6 and Tables 4–36;
> [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md),
> §§3, 5–6, printed pp. 769–776 (PDF pp. 6–13);
> [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md),
> HTML `#s1-1`, `#s1-4`, `#s3-1–2` and Tables 1–2;
> [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§V–VII, printed pp. 9–37 (PDF pp. 13–41);
> [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §§4–6 and Appendix F; [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md),
> Part I §§3.1–4.9; `CTL-0001/0002/0005/0007/0010/0011/0015` and their
> named RSK relations; `SYN-0007-C01`–`C05`.
> **Basis / limits:** Portfolio breadth and qualifications are explicit. No
> implementation/test/effectiveness is inferred, and BMO/AGE CT remain Partial.

## Versioned framework/instrument mappings

| Framework/instrument | Jurisdiction/force | Exact represented version/mapping | Non-equivalence boundary |
| --- | --- | --- | --- |
| NIST SP 800-82 Rev. 3 | U.S. federal technical guideline; contextual/voluntary outside specific mandates | CSF 1.1 in §6; SP 800-53 Rev. 5/800-53B OT overlay in Appendix F | Rev. 3 is not native CSF 2.0 and mapping is not compliance |
| NIST IR 8467 Second Public Draft | U.S. voluntary draft genomic profile | CSF 2.0 and PF 1.0 priorities; Implementation Tiers excluded | Priority is not risk, adoption or effectiveness |
| FDA February 2026 Level 2 final guidance | U.S. nonbinding guidance with separately scoped cited duties | eight FDA device-control categories and lifecycle assurance | Guidance/category mapping is not product compliance or test result |
| WHO Laboratory Biosecurity Guidance 2024 | global normative guidance | risk/custody/information/incident/assurance families | Recommendation is not national adoption |
| Regulation (EU) 2025/327 EHDS | binding EU regulation with staged application | primary-use/EHR and secondary-use legal safeguard design | Binding design is not Member State/product implementation |

Only locally ingested instruments count. IEC/ISA/ISO publications merely cited
inside FDA or NIST are not treated as ingested frameworks.

> **Claim record — SYN-0007-C07 | analytic-judgment**
> **Claim:** The current corpus satisfies `CTR-GR`: at least three official
> versioned frameworks/instruments are mapped with jurisdiction, force and
> scope, and every mapping rejects applicability, compliance, implementation
> and effectiveness equivalence.
> **Claim status:** active
> **Scope:** Frozen `CTR-GR` criterion; not a complete standards catalogue or
> legal crosswalk.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md),
> §6 and Appendix F; [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md),
> §§3.2–3.3, 6 and Tables 4–36;
> [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md),
> §§V–VII and Appendix 1;
> [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§5–8; [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md),
> Articles 1–105; `GOV-0001/0006/0007/0008`, `SYN-0006`.
> **Basis / limits:** Versions, modalities and scope are direct; the
> reconciliation is editorial. Referenced-but-not-ingested standards do not
> count.

## Conservative limits

> **Claim record — SYN-0007-C08 | analytic-judgment**
> **Claim:** This transaction closes `FND-CT`, `LAB-CT`, `CTR-CT` and
> `CTR-GR` only; all BMO/AGE sector cells, other LAB cells and every incident/
> effectiveness question remain unpassed.
> **Claim status:** active
> **Scope:** Frozen rubric rescore after `SRC-0018`.
> **As of:** 2026-07-12.
> **Review after:** 2026-08-11.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** `SYN-0007-C01`–`C07`; frozen rubric criteria and independent
> binary review.
> **Basis / limits:** Four full contracts are met; missing quality, One Health,
> incident and assurance evidence is explicit and receives no score.

## Related pages

- [SYN-0024 — Cross-sector portfolio reconciliation](syn-0024-cross-sector-control-threat-asset-governance-reconciliation.md)
- [SYN-0010 — LAB scope/assets/lifecycle; existing LAB-CT retained](syn-0010-laboratory-biobank-scope-asset-lifecycle-reconciliation.md)
- [SYN-0011 — LAB system-boundary reconciliation](syn-0011-laboratory-biobank-system-boundary-reconciliation.md)
- [SYS-0007 — biobank/ELN system-boundary map](../systems/sys-0007-biobank-informatics-storage-ecosystem.md)
- [SRC-0018 — NIST SP 800-82r3](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [GOV-0008 — NIST OT governance](../governance/gov-0008-nist-sp-800-82r3-ot-security-2023.md)
- [CTL-0011 — OT defense-in-depth and resilience](../controls/ctl-0011-ot-defense-in-depth-resilience-assurance.md)
- [CTL-0015 — continuous-manufacturing quality controls](../controls/ctl-0015-continuous-manufacturing-quality-control.md)
- [SRC-0031 — ICH Q13](../sources/src-0031-ich-q13-continuous-manufacturing.md)
- [SYN-0006 — Control function/state taxonomy](syn-0006-official-control-function-state-taxonomy.md)
- [WFL-0004 — High-consequence material lifecycle](../workflows/wfl-0004-high-consequence-material-lifecycle.md)
- [RSK-0001 — HCL containment disruption](../risk-scenarios/rsk-0001-hcl-containment-control-disruption.md)
- [RSK-0002 — BMO control disruption](../risk-scenarios/rsk-0002-biomanufacturing-control-integrity-disruption.md)
- [RSK-0007 — Farm production/supply disruption](../risk-scenarios/rsk-0007-farm-data-access-production-supply-disruption.md)
- [SYN-0016 — BMO four-cell reconciliation](syn-0016-biomanufacturing-assets-lifecycle-transfer-control-reconciliation.md)

## Sources

- [SRC-0002](../sources/src-0002-crawford-high-containment-laboratories-2023.md)
- [SRC-0003](../sources/src-0003-guttieres-advanced-manufacturing-2019.md)
- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0005](../sources/src-0005-nist-ir-8432-cybersecurity-genomic-data-2023.md)
- [SRC-0006](../sources/src-0006-nist-ir-8467-genomic-data-profile-2024.md)
- [SRC-0010](../sources/src-0010-drape-agriculture-cyberbiosecurity-2021.md)
- [SRC-0014](../sources/src-0014-ney-dna-sequencing-security-2017.md)
- [SRC-0016](../sources/src-0016-eu-ehds-regulation-2025.md)
- [SRC-0017](../sources/src-0017-fda-medical-device-cybersecurity-2026.md)
- [SRC-0018](../sources/src-0018-nist-sp-800-82r3-ot-security-2023.md)
- [SRC-0031](../sources/src-0031-ich-q13-continuous-manufacturing.md)
