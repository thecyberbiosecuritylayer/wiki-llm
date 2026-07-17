---
id: SYN-0034
type: synthesis
title: "What Is Cyberbiosecurity? An Explanation Through Dependencies and Consequences"
aliases:
  - What Is Cyberbiosecurity?
  - Cyberbiosecurity explained
status: active
created: 2026-07-14
updated: 2026-07-16
last_reviewed: 2026-07-16
review_after: 2026-10-16
source_ids:
  - SRC-0001
  - SRC-0002
  - SRC-0003
  - SRC-0004
  - SRC-0005
  - SRC-0006
  - SRC-0008
  - SRC-0009
  - SRC-0011
  - SRC-0012
  - SRC-0014
  - SRC-0017
  - SRC-0046
  - SRC-0047
  - SRC-0055
  - SRC-0057
sensitivity: public
dual_use: low
tags:
  - cyberbiosecurity
  - foundations
  - public-explainer
  - cross-domain-transfer
  - risk-model
---

# What Is Cyberbiosecurity?

> **In brief.** Cyberbiosecurity is the analysis and management of risks that
> arise from dependencies between digital and biological systems. It is
> concerned with causality: how an error or disruption in data, software, or
> digital control can affect a biological process, product, or decision—and
> how biological material or a laboratory measurement can change a digital
> result.

## A digital disruption changed a biological chain

In June 2024, a ransomware attack on the British laboratory-services provider
Synnovis significantly reduced its capacity to process tests. The consequences
were not confined to IT infrastructure. Affected London hospitals experienced
disrupted access to systems needed for blood grouping, antibody screening, and
crossmatching.

Hospitals relied more heavily on O-negative blood components. NHS Blood and
Transplant (NHSBT) reported that this increased pressure on a limited stock and
contributed to an Amber alert. NHS England also reported that more than 11,000
planned outpatient appointments and elective procedures were postponed. The
available sources do not, however, establish that the blood stock was exhausted
or that the attack caused a specific patient injury (NHSBT, *Annual Report and
Accounts 2024–25*, pp. 21–22, 97; NHS England, update of 10 November 2025,
paras. 2–3).

The documented consequence was not a change to the blood itself, but disruption
of the digital processes used to work with it. That disruption affected the
ability to verify compatibility, the choice of blood component, laboratory
workload, and demand for a physical stock. This kind of causal transition
between the digital and biological parts of a system is the subject of
cyberbiosecurity.

## A working definition and its boundaries

In this article, **cyberbiosecurity** means the practical field of analyzing
and managing risks that arise from dependencies between digital and biological
systems, where a state change in one can alter a process, decision, or
consequence in the other.

This definition is broader than “laboratory cybersecurity.” It encompasses not
only computers and networks, but also samples, data, instruments, manufacturing
processes, supply chains, people, and the environment that digital systems and
digitally supported decisions may affect.

In 2018, Murch and colleagues proposed formalizing cyberbiosecurity as a new
hybrid discipline. They described their definition as an initial one that
should evolve with the field. Crawford and colleagues later applied this
framework to high-containment laboratories through an analysis of assets and
potential consequences. That work continued the same intellectual line, but it
did not establish a global consensus around a single definition of the term.

> **Claim record — SYN-0034-C01 | analytic-judgment**
> **Claim:** A practically useful definition of cyberbiosecurity should identify
> the digital side, the biological side, and the dependency or transfer
> mechanism between them; the mere presence of IT in a biological organization
> is not sufficient.
> **Evidence:** SRC-0001, § Introduction, first paragraph; SRC-0002, Abstract,
> § Introduction, second paragraph, and § Methods — Asset-impact analysis;
> SRC-0004, Glossary, printed pp. xiii–xiv, and §1, printed pp. 1–3.
> **Limits:** This is a synthesis and an editorial boundary used by the wiki,
> not a universally approved international definition. The World Health
> Organization defines adjacent laboratory domains, but not the term
> *cyberbiosecurity* itself.

## Four related but distinct fields

| Field | Central question | Simplified example |
| --- | --- | --- |
| **Cybersecurity** | Are digital systems and information protected? | Could someone steal an account or alter a database? |
| **Biosafety** | How can unintentional exposure or accidental release during biological work be prevented? | Could a procedural error accidentally cause an exposure? |
| **Biosecurity** | How can unauthorized access, loss, theft, misuse, diversion, or release of biological material, technology, or information be prevented? | Could an outsider gain control of a sample or access sensitive information or technology? |
| **Cyberbiosecurity** | How does a change in the digital or biological part of a system cross a dependency and create a consequence in another part? | Could an incorrect digital result alter treatment, manufacturing, or a public-health action? |

This table is a guide, not a rigid international dictionary. The World Health
Organization (WHO) shows that *biosafety* and *biosecurity* partly overlap.
Precise analysis should therefore retain the English terms rather than rely on
translation alone (WHO, *Laboratory Biosecurity Guidance*, 2024, Glossary,
pp. xiii–xiv; §1 and Figure 1.1, pp. 1–3).

## Cyberbiosecurity starts with a dependency

To describe a problem as cyberbiosecurity, the analysis must show a biological
side, a digital dependency, and a consequence of their connection. Consequences
may include loss of confidentiality, integrity, availability, authenticity, or
data provenance, as well as harm to privacy, human safety, product quality,
research validity, resilience, governance, or supply continuity.

For example, a phishing attack against a pharmaceutical company's accounting
department is not yet a complete cyberbiosecurity scenario unless a connection
to biological data, manufacturing, a product, or a decision is demonstrated.
An accidental manual spill with no digital dependency belongs primarily to
*biosafety*, while theft of a sample with no digital transition belongs to
*biosecurity*. An adjacent topic becomes cyberbiosecurity when a causal bridge
between the fields can be traced—not merely when the prefixes “cyber” and “bio”
are placed next to each other.

## How risk travels

It is simplest to think in terms of a causal chain rather than a list of
threats:

> **Malicious action or unintentional failure** → **interaction with a
> weakness or failed trust boundary** → **the first digital, biological, or
> physical state change** → **transfer of that change between domains** → **a
> new state in the receiving system** → **a consequence for people, a product,
> research, an organization, or the environment**.

Once this chain has been constructed, each edge can be mapped to a safeguard
that should prevent the unwanted change, detect it, contain its consequences,
or support recovery.

Five transfer mechanisms are useful for analysis:

- **Data:** a change to a sequence, annotation, result, or provenance
  information affects later analysis or a decision.
- **Control:** a digital reading or command changes a physical or biological
  process.
- **Custody:** risk arises as material or a record passes between people,
  organizations, or stages and its correct association or traceability is lost.
- **Decision:** a digital check permits, blocks, or alters physical execution,
  product release, notification, or access.
- **Material or input:** a physical or biological object becomes the source of
  data interpreted by software or a decision process.

This is a working analytic classification, not a universal standard. It does
not imply that all mechanisms are equally likely or present in every sector.

> **Claim record — SYN-0034-C04 | analytic-judgment**
> **Claim:** The five mechanisms—data, control, custody, decision, and
> material/input—form a practical editorial scheme for describing how a change
> transfers between the digital and biological parts of a system.
> **Evidence:** Data: SRC-0005, §§2.1–3.5, and SRC-0006, §§1.2–2.2.1 and
> 5.1–5.6. Control: SRC-0003, § Digital Information Flow in Biomanufacturing
> and Figure 1. Custody: SRC-0004, §§6.3–6.4.2, printed pp. 31–34, and §7,
> printed pp. 40–44. Decision: SRC-0011, §§I–V, and SRC-0012, HTML lines
> 841–1070. Material/input: SRC-0014, Introduction and §§3, 5–6, and SRC-0057,
> SUI Executive summary, paras. 3–5, §2.6.7, p. 45, and §3.1.1, p. 51.
> **Limits:** This is an editorial synthesis, not a universal standard or an
> exhaustive list. The sources have different scopes and levels of evidence and
> do not establish that the mechanisms are equally prevalent.

## Three kinds of consequence

### From digital disruption to clinical and material continuity

Synnovis shows how disruption of laboratory-system availability can alter
compatibility testing, the choice of blood component, and demand for a limited
physical stock. This is not evidence that a digital event always causes
biological harm. It is a documented example of a digital dependency affecting
clinical continuity and management of a biological resource.

### When biological material becomes a digital result

The reverse direction is easy to miss. In 2021, the contracted PCR laboratory
Immensa incorrectly reported some results. The UK Health Security Agency
(UKHSA) identified a staff configuration error as the immediate cause: some
measurements were classified as negative in the digital system when they
should have been positive. The investigation did not identify a cyberattack or
malicious intent (UKHSA, *Serious Untoward Incident Investigation*, Executive
summary, p. 8; Appendix 2, §2(B)(vi), p. 71).

The error occurred not in the sample itself, but at the boundary between a
laboratory measurement and its digital classification:

> **Biological sample** → **laboratory measurement** → **misconfigured digital
> classification** → **incorrect negative result** → **altered notification
> state and contact-tracing trigger**.

A positive result should have triggered notification and a subsequent contact-
tracing process, but the sources do not reconstruct the behavior of every
individual. UKHSA estimated that approximately 39,000 of the 417,000 tests
processed by the laboratory during the relevant period were likely incorrect
negative results. This is a statistical estimate, not 39,000 individually
confirmed results. Modeled population consequences likewise should not be
presented as observed outcomes for specific people (UKHSA SUI, §1.2.4, p. 13;
UKHSA preprint, Results and Table 3, pp. 3, 20).

This case does not mean that biological material “attacked” a digital system.
It demonstrates something different: a biological sample can be the input to a
chain that ends in a digital decision, and an error at the measurement-
interpretation boundary can change reporting and subsequent action.

### Genetic data: harm can occur without changing a biological process

Cyberbiosecurity is not limited to physical changes in biological material. In
genomics, the genetic data themselves, their context, and the relationships
between people are important assets.

During the 2023 23andMe incident, credential stuffing with reused credentials
provided direct access to 18,222 accounts worldwide. The DNA Relatives and
Family Tree features extended access to linked profiles. Separately, the
company reported that the total number of affected customers worldwide was
nearly seven million. This broader figure should not be added to 18,222 or
interpreted as the number of directly accessed accounts (joint report by the
Canadian and UK regulators, paras. 20–35 and affected-group tables).

The consequence was a loss of confidentiality and privacy that could extend
from one account to relatives through a network of family relationships. The
sources do not establish a change to laboratory analysis, treatment, or a
physical injury. Nor do they establish that the credentials were stolen from
23andMe, that a software exploit was used, or that raw genetic data or a genetic
health report was exposed for every affected person. This is a distinct class
of cyberbiosecurity consequence, not a weaker version of a clinical incident.

## A boundary example: manufacturing and supply

Following a 2017 network cyberattack, Merck reported disruption to
manufacturing, research, and sales operations, an inability to fulfill orders
for certain unnamed products in certain unnamed markets, and a residual order
backlog that also affected the following year. This is an example of a
transition from disruption of digital systems to manufacturing and supply. It
does not, however, establish compromise of a particular industrial controller,
a change in batch quality, or patient harm (Merck, 2018 Form 10-K, Item 1A,
p. 25; MD&A “Cyber-attack,” p. 38).

A New Jersey court opinion independently confirms the incident context and
property damage, but does not reproduce the order metrics or their effect on
sales (New Jersey Appellate Division opinion, 2023, pp. 7–10). Because the
products and manufacturing stages are unnamed, the available sources do not
close the full pathway to a biological or clinical consequence. That is why
mentioning a cyberattack should prompt the next question: which specific
process or product depended on the digital system, and what happened when that
dependency was disrupted?

> **Claim record — SYN-0034-C02 | analytic-judgment**
> **Claim:** Documented cases show different transfer roles: Synnovis—from
> disrupted digital availability to clinical and material continuity;
> Immensa—from material and measurement to a digital decision; 23andMe—genomic
> privacy consequences; and Merck—manufacturing and supply disruption.
> **Evidence:** SRC-0008, pp. 21–22, 97; SRC-0009, paras. 2–3; SRC-0057,
> SUI Executive summary, paras. 3–5, §2.6.7, p. 45, and §3.1.1, p. 51; UKHSA
> preprint, Introduction, p. 2; SRC-0055, joint report, paras. 20–35;
> SRC-0046, Form 10-K, Item 1A and MD&A “Cyber-attack.”
> **Limits:** Four cases do not establish the prevalence, likelihood, or
> typical scale of consequences across the domain. Merck does not close the
> full pathway to a biological or clinical consequence; source roles, causal
> strength, and measured outcomes differ across the cases.

## Where these dependencies arise

The same logic appears in many settings:

- **Genomics, other omics fields, and bioinformatics:** sequence-data
  processing, databases, identity management, cloud services, and high-
  performance computing affect privacy, analytic integrity, and later research
  or clinical decisions.
- **Laboratories and biobanks:** connected instruments, laboratory information
  systems, electronic notebooks, material records, result transmission, and
  storage monitoring are tied to sample identity, traceability, result
  correctness, and operational continuity.
- **Engineering biology and nucleic-acid synthesis:** design files, order
  screening, reference databases, and equipment access affect decisions to
  fulfill or reject an order.
- **Biomanufacturing and operational technology:** sensors, controllers,
  manufacturing and quality systems, recipes, and remote access are tied to
  process state, quality, product release, and supply.
- **Clinical systems and public health:** laboratory reporting, electronic
  health records, medical devices, and surveillance-data exchange can affect
  treatment, notification, delays, and human safety.
- **Agriculture and the environment:** sensors, automation, traceability, and
  animal- and plant-health systems are connected to production, food supply,
  and environmental decisions.
- **AI in biological research:** training data, models, application programming
  interfaces, computing infrastructure, and decision gates can affect research
  validity and the choice of a subsequent experimental or practical action.

This is an illustrative map of possible dependencies, not a claim that each is
compromised, prevalent, or equally risky. What matters in a particular
organization is its actual process, architecture, data flows, trust boundaries,
and decision-makers. The map draws on scholarship about the boundaries of
cyberbiosecurity and the digital flow of biomanufacturing, WHO laboratory-
biosecurity guidance, NIST models for genomic data, and US and UK nucleic-acid
synthesis screening frameworks.

## How to analyze a cyberbiosecurity scenario

Six questions are enough for a first pass:

1. **What or who on the biological side has value or could be harmed?** A
   sample, product, patient, process, population, study, or the environment?
2. **What digital component does it depend on?** Data, an identity system,
   software, a model, an instrument, a controller, a cloud service, or a
   supplier?
3. **What changes first?** Availability, integrity, confidentiality,
   configuration, chain of custody, or provenance?
4. **How does the change cross the boundary?** Through data, control, custody,
   a decision, or material input?
5. **Who or what experiences the consequence?** A person, relative, worker,
   organization, product, supply chain, population, or the environment?
6. **At which exact edge should a safeguard interrupt the pathway?** Before
   transfer, during it, after detection, or during recovery?

If the answers stop at “we have computers” or “we have biology,” the scenario
has not yet been constructed.

## A safeguard should interrupt a specific edge

“We need stronger cybersecurity” is too general. Different edges in the chain
require different functions. The following categories are a working editorial
scheme, not a universal model:

- **Govern and inventory:** identify assets, accountability, dependencies, and
  acceptable risk before selecting specific measures.
- **Prevent:** stop an unwanted change or unauthorized access from occurring.
- **Detect:** identify an anomaly, incorrect result, loss of traceability, or
  deviation in process state.
- **Contain and respond:** limit propagation and move the system into a safe or
  controlled state.
- **Recover:** restore not just availability, but a verified digital and
  biological system state.
- **Assure:** determine whether a measure is correctly configured, tested, and
  suitable for the specific process.

For example, result validation is needed at the transition from measurement to
classification. Anomaly monitoring is appropriate where results can be
compared with an expected pattern. A decision gate should operate before a
digital result triggers a physical or clinical action. A separate continuity
procedure is needed during an outage, and the restored state must be verified
before routine operations resume.

Merely naming a safeguard is insufficient. A recommended measure is not
necessarily implemented; an implemented measure is not necessarily tested; and
a successfully tested measure is not necessarily effective in a real event. A
legal or standards requirement does not prove compliance, while independent
evaluation is a separate evidentiary attribute and may identify an ineffective
measure.

> **Claim record — SYN-0034-C03 | analytic-judgment**
> **Claim:** Cyberbiosecurity analysis should separately identify whether a
> measure is recommended, implemented, tested, effective, or independently
> evaluated; each state or attribute requires separate evidence and does not
> follow automatically from another.
> **Evidence:** SRC-0004, §6 introduction and §6.6, printed pp. 24, 37–39;
> SRC-0006, §§3.2–3.3 and 6, printed pp. 16–19, 29–31; SRC-0017, §§V.C and
> VII.E, printed pp. 25–27, 36–37.
> **Limits:** These states and attributes are an editorial synthesis used by
> the wiki, not a universal maturity scale. Guidance and testing requirements
> establish expectations, but do not by themselves prove implementation,
> effectiveness, or the result of an independent evaluation.

## How to avoid overstating risk

Cyberbiosecurity is easy to sensationalize because it joins two complex
fields. Useful analysis instead separates concepts that are often conflated:

- **A possible scenario** is not a documented incident.
- **A demonstration in a controlled environment** does not establish real-
  world exploitation or prevalence.
- **A source reporting an incident** does not automatically establish the
  actor, entry method, root cause, or every downstream consequence.
- **A law, standard, or regulatory guidance** does not prove that a measure was
  implemented or effective.
- **One case, sector, or country** does not represent the entire world.

Even the boundaries of the term remain partly open. Murch and colleagues
proposed an initial definition; Crawford and colleagues applied it to high-
containment laboratories; and WHO defines adjacent laboratory domains but does
not establish a universal definition of *cyberbiosecurity*. Precision matters
more here than an appearance of certainty.

This article reflects the wiki's evidence corpus with a knowledge cutoff of
**13 July 2026**. It does not claim complete coverage of the global domain and
is not a substitute for checking primary sources when making a specific
decision.

## The central idea

Cyberbiosecurity is not merely cybersecurity in a laboratory, nor is it a
vague story about “hacked biology.” It is a way to see the complete system: a
biological asset or process, a digital dependency, a causal transition, a
consequence, and the point where protection can break the chain.

Return to Synnovis. The available sources do not establish a change to the
blood itself, but they document disruption of digital processes needed for
compatibility testing, a change in laboratory workload, greater reliance on
O-negative components, and pressure on a limited physical stock. This is the
central test of the concept:

> If a scenario cannot clearly identify the biological side, the digital
> dependency, and the causal connection between them, it is not yet a complete
> cyberbiosecurity scenario.

## Evidence base

- **SRC-0001** — Murch et al. *Cyberbiosecurity: An Emerging New Discipline to
  Help Safeguard the Bioeconomy* (2018).
- **SRC-0002** — Crawford et al. *Cyberbiosecurity in High-Containment
  Laboratories* (2023).
- **SRC-0003** — Guttieres et al. *Cyberbiosecurity in Advanced Manufacturing
  Models* (2019).
- **SRC-0004** — WHO. *Laboratory Biosecurity Guidance* (2024).
- **SRC-0005** — NIST IR 8432. *Cybersecurity of Genomic Data* (2023).
- **SRC-0006** — NIST IR 8467. *Genomic Data Cybersecurity and Privacy
  Frameworks Community Profile* (Second Public Draft, 2024).
- **SRC-0008** — NHS Blood and Transplant. *Annual Report and Accounts
  2024–25*.
- **SRC-0009** — NHS England. *Synnovis Cyber Incident Update*
  (10 November 2025).
- **SRC-0011** — U.S. OSTP. *Framework for Nucleic Acid Synthesis Screening*
  (revised September 2024).
- **SRC-0012** — UK Government. *Screening Guidance on Synthetic Nucleic Acids
  for Users and Providers* (2024).
- **SRC-0014** — Ney et al. *Computer Security, Privacy, and DNA Sequencing*
  (2017).
- **SRC-0017** — U.S. FDA. *Cybersecurity in Medical Devices: Quality
  Management System Considerations and Content of Premarket Submissions*
  (2026).
- **SRC-0046** — Merck & Co. Inc. *2018 Form 10-K*, filed 27 February 2019.
- **SRC-0047** — Superior Court of New Jersey, Appellate Division. *Merck v.
  ACE*, A-1879-21/A-1882-21 (2023).
- **SRC-0055** — joint OPC and ICO investigation materials concerning the
  23andMe genetic-data breach (2023–2025).
- **SRC-0057** — UKHSA investigation materials and analyses of the consequences
  of Immensa PCR-result misreporting (2021–2022).
