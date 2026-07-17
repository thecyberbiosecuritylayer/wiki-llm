---
id: THR-0005
type: threat
title: Laboratory malicious, insider and supply-chain action classes
aliases:
  - laboratory intentional threat classes
  - laboratory insider and third-party threat actions
status: active
created: 2026-07-12
updated: 2026-07-12
last_reviewed: 2026-07-12
review_after: 2026-10-12
source_ids:
  - SRC-0004
  - SRC-0019
  - SRC-0022
  - SRC-0057
  - SRC-0058
sensitivity: public
dual_use: moderate
threat_kind: intentional-malicious-insider-and-third-party-actions
relations:
  - predicate: evidenced-by
    target: SRC-0004
    claim_id: THR-0005-C01
    evidence:
      - source: SRC-0004
        locator: "WHO glossary and §§5.1, 5.3, 6.4–6.6 and 7.3.1, printed pp. xiii–xiv and 19–41/PDF pp. 15–16 and 39–61"
  - predicate: evidenced-by
    target: SRC-0019
    claim_id: THR-0005-C02
    evidence:
      - source: SRC-0019
        locator: "CBS requirement 4.1.8 and adjacent programme/role requirements, pp. 84–91"
  - predicate: exploits
    target: VUL-0006
    claim_id: THR-0005-C04
    evidence:
      - source: SRC-0004
        locator: "WHO §§5.1, 5.3 and 6.4–6.6, exposure and protection classes"
      - source: SRC-0019
        locator: "CBS §4.1 physical/personnel security, accountability and information-management requirements"
  - predicate: affects
    target: AST-0005
    claim_id: THR-0005-C03
    evidence:
      - source: SRC-0004
        locator: "WHO biological material, information, technology and facility asset scope, §§1–2 and 5–7"
tags:
  - laboratory
  - malicious
  - insider
  - supply-chain
  - unauthorized-access
  - theft
  - diversion
  - defensive-taxonomy
---

# Laboratory malicious, insider and supply-chain action classes

## Threat definition

This page represents intentional actor/action classes only. Accidental,
environmental, inventory-control and ordinary supply-availability failures are
separate [HAZ-0006](../hazards/haz-0006-laboratory-input-configuration-environmental-and-inventory-failures.md)
states; enabling weaknesses are [VUL-0006](../vulnerabilities/vul-0006-laboratory-context-threshold-oversight-and-supply-exposures.md);
and neither `INC-0008` nor the HSE exposure notices report malicious causation.

> **Claim record — THR-0005-C01 | source-report**
> **Claim:** WHO's current laboratory-biosecurity guidance defines intentional
> unauthorized access, misuse, loss, theft, diversion, release and related
> malicious actions against biological material, information, technology and
> facilities and requires risk-based physical, personnel, inventory and
> information/cybersecurity treatment.
> **Claim status:** active
> **Scope:** High-level defensive threat classes; no target, access path,
> procedure, material inventory or attack method.
> **As of:** WHO guidance published 2024-06-21; reviewed 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> `SRC-0004-C02/C03/C05/C07/C09`; glossary and §§5.1, 5.3, 6.4–6.6 and
> 7.3.1, printed pp. xiii–xiv and 19–41/PDF pp. 15–16 and 39–61.
> **Basis / limits:** Threat and control categories are direct. WHO guidance
> does not establish an event, prevalence or facility exposure.

> **Claim record — THR-0005-C02 | source-report**
> **Claim:** The Canadian Biosafety Standard independently requires a scoped
> biosecurity plan addressing dual-use risk, physical/personnel security,
> material accountability, inventory control, incident response and
> information management, thereby supporting insider and third-party/supply
> actor boundaries without asserting an incident.
> **Claim status:** active
> **Scope:** Licence/facility-scoped Canadian requirements and actor/control
> boundary; not global law, malicious-event evidence or implementation audit.
> **As of:** CBS Third Edition 2022; reviewed 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** single-source
> **Confidence:** high
> **Evidence:** [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> `SRC-0019-C05/C06`; requirement 4.1.8 and adjacent programme/role
> requirements, pp. 84–91.
> **Basis / limits:** The requirements and role classes are direct. A required
> plan does not prove adoption, threat presence or safeguard effectiveness.

## Actor, supply and asset boundaries

> **Claim record — THR-0005-C03 | analytic-judgment**
> **Claim:** An insider is defined here by authorized or trusted position, not
> presumed malicious motive; a supplier/service actor becomes an intentional
> threat only when adverse intent/action is evidenced, while ordinary defect,
> outage, shortage or environmental interruption remains a hazard.
> **Claim status:** active
> **Scope:** Canonical actor/hazard separation affecting
> [AST-0005](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md);
> not attribution of any current source event.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** `THR-0005-C01/C02`;
> [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md),
> `SRC-0022-C03/C05/C06` for non-adversarial supplier/inventory/continuity
> context.
> **Basis / limits:** Intent, role and failure state are distinct predicates.
> No actor is inferred from an asset dependency alone.

> **Claim record — THR-0005-C04 | analytic-judgment**
> **Claim:** These intentional classes can exploit `VUL-0006` only if a
> compatible access, trust, custody, information or supplier weakness exists
> and preventive/detective controls fail; category presence does not imply
> reach, success or consequence.
> **Claim status:** active
> **Scope:** Conditional defensive graph semantics; no exploitability score,
> topology, credential, payload or operational path.
> **As of:** 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** inferred
> **Confidence:** high
> **Evidence:** [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md),
> §§5.1, 5.3 and 6.4–6.6, printed pp. 19–39/PDF pp. 39–59 (threat,
> access, accountability and supplier/service protection conditions);
> [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md),
> §4.1, especially requirement 4.1.8 and adjacent physical/personnel-
> security, accountability and information-management requirements,
> pp. 84–91. `THR-0005-C01`–`C03` and [VUL-0006](../vulnerabilities/vul-0006-laboratory-context-threshold-oversight-and-supply-exposures.md)
> are canonical navigation, not independent evidence.
> **Basis / limits:** Conditional edges preserve actor, weakness, event and
> consequence separation.

> **Claim record — THR-0005-C05 | artifact-observation**
> **Claim:** The current incident additions remain non-adversarial: UKHSA
> attributes `INC-0008` to staff configuration error and HSE attributes its
> exposure pattern to missing/inaccurate/delayed context, so neither source is
> used to manufacture malicious or insider-event evidence.
> **Claim status:** active
> **Scope:** Attribution/nonpromotion check for the new corpus.
> **As of:** Full source review 2026-07-12.
> **Review after:** 2026-10-12.
> **Evidence status:** corroborated
> **Confidence:** high
> **Evidence:** [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md),
> `SRC-0057-C04/C08/C10`; [SRC-0058](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md),
> `SRC-0058-C03/C07`.
> **Basis / limits:** Absence of malicious attribution in these records is not
> evidence that malicious laboratory incidents never occur.

## Safety boundary

No target selection, access route, evasion, material detail, laboratory
procedure or facility topology is represented. The page is limited to threat
classification and defensive preconditions.

## Related pages

- [AST-0005 — affected assets/stakeholders](../assets/ast-0005-laboratory-biobank-material-data-stakeholders.md)
- [HAZ-0006 — non-adversarial hazards](../hazards/haz-0006-laboratory-input-configuration-environmental-and-inventory-failures.md)
- [VUL-0006 — enabling exposures](../vulnerabilities/vul-0006-laboratory-context-threshold-oversight-and-supply-exposures.md)
- [SYN-0031 — threat-corpus reconciliation](../syntheses/syn-0031-laboratory-threat-reverse-transfer-incident-reconciliation.md)

## Sources

- [SRC-0004](../sources/src-0004-who-laboratory-biosecurity-guidance-2024.md)
- [SRC-0019](../sources/src-0019-canadian-biosafety-standard-third-edition.md)
- [SRC-0022](../sources/src-0022-nci-best-practices-biospecimen-resources-fourth-edition.md)
- [SRC-0057](../sources/src-0057-ukhsa-immensa-pcr-misreporting-investigation-2021-2022.md)
- [SRC-0058](../sources/src-0058-uk-hse-laboratory-biological-exposure-investigations-2011-2024.md)
