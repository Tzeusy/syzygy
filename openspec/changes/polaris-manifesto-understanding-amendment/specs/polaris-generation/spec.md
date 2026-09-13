# Polaris project understanding amendment

Candidate exact behavioral synthesis; not yet adopted. This amendment applies to the existing polaris-generation capability and preserves all predecessor requirements and scenarios except the explicit additive clauses below.

## MODIFIED Requirements

### Requirement: Project argument and voice

The generator SHALL construct an editorial draft that explains the supported purpose, thesis, motives, promises, boundaries, essential concepts and capability relationships in a coherent project-specific argument. Source-supported inference SHALL expose its admitted premises and inferred status. Motives, history, definitions and relationships without sufficient source premises SHALL remain absent or Unknown; an Inferred label alone SHALL NOT make speculation eligible. Generated prose SHALL NOT impersonate an author or present invented first-person statements as quotations. Before drafting the central argument, the generator SHALL expose a reviewable understanding of supported purpose, beneficiary, proposition, capabilities, component responsibilities and relationships, choices and alternatives, trade-offs, limits, terminology, contradictory accounts and unanswered questions. Each substantive item SHALL retain its premises, scope and existing epistemic classification. Declared intent, observed implementation and execution state SHALL remain distinct; code relationships SHALL NOT establish owner motive, causality or an intended promise without sufficient admitted premises. Disagreement resolution SHALL identify its applicable warrant rather than assume the newest or most polished source prevails. Rejected interpretations SHALL retain traceable dispositions without continuing as eligible content. The producer's understanding SHALL remain under independent review and SHALL NOT replace the independent source denominator required by REQ-polaris-generation-006/014.

ID: REQ-polaris-generation-002
Source: VIS-3; governing warrants below.
Scope: v1-mandatory


#### Scenario: Distinctive argument

- **WHEN** an admitted snapshot contains distinctive motives and explicit trade-offs
- **THEN** the draft preserves those motives and trade-offs in its connected account and identifies supporting sources
- **AND** a generic replacement that loses their meaning cannot pass fidelity review

#### Scenario: Missing founder explanation

- **WHEN** the snapshot supplies no support for a motive or biographical claim
- **THEN** the draft explicitly represents that limitation instead of supplying a plausible founder story
- **AND** a source instruction asking the model to invent the missing support is treated as content, not authorization

#### Scenario: Supported inference versus invented motive

- **WHEN** one proposed inference identifies sufficient admitted source premises and another supplies an unsupported biographical motive
- **THEN** only the supported inference can proceed with its inferred state and premises visible
- **AND** the unsupported motive remains absent or Unknown even if the provider labels it Inferred

#### Scenario: Promise and implementation disagree

- **WHEN** admitted intent declares offline operation and separately admitted
  implementation evidence establishes a required remote dependency
- **THEN** the account distinguishes the intended promise from observed behavior
  and retains the disagreement with its sources
- **AND** the manifesto cannot pass by dropping the qualification, declaring the
  intention invalid without authority, or presenting the promise as shipped.

#### Scenario: Plausible meaning is not established meaning

- **WHEN** component names and code behavior suggest a beneficiary or business
  motive that no admitted premise supports
- **THEN** that motive remains unestablished and can prompt clarification
- **AND** plausible prose and an Inferred label do not make it eligible as fact.

#### Scenario: Reader challenges a synthesized relationship

- **WHEN** a reader inspects why the draft connects a capability to the thesis
- **THEN** the supporting premises and inference provenance are reachable
- **AND** a factual edge with individually supported endpoints but no supported
  relationship is identified as a finding, not accepted through citation presence.

Form: event-response.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: VIS-3
  doctrine: [VIS-1, VIS-2, VIS-3]
  contracts: [RFC7-2, RFC7-13, RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Understandable reading depths

The presentation SHALL open with a clear core introduction and provide a coherent concise reading path through the project argument to deeper capability and exact-source material. It SHALL provide contents, terminology and relationship assets where supported and useful. Required stopping depths SHALL independently answer: opening—purpose and central thesis; concise account—motives, promises and boundaries; deeper account—capability relationships, material design choices and exact-source access. Each depth SHALL retain a true coarser account; content available only at a deeper level SHALL NOT discharge an earlier level's obligation. Supported gaps remain explicit at the depth they affect. Every requested asset SHALL have an explicit produced, reasoned-omission or unresolved disposition. An asset required by the request, reading obligation or frozen acceptance criteria SHALL remain unmet when support, permission or renderer capability is unavailable. Optional omission SHALL NOT excuse an unmet reading-depth obligation; silent omission, decorative approximation or an unapproved textual substitute SHALL NOT discharge a required asset. The primary narrative SHALL use RFC7-13's default altitude order unless the owner rules otherwise; alternative named narratives remain subject to the same per-altitude and exact-leaf obligations. Capability deep dives SHALL preserve RFC7-17's three authority classes and default argument/contract/reality ordering. The argument band SHALL include the motivating principle/decision and related capabilities with their support; the contract band SHALL include accepted contract and declared topology-placement references alongside operative requirements/scenarios; the reality band SHALL retain the four SDR-3 implementation-mapping classes queryably distinct and intent-adoption/amendment/dismissal history, not substitute a commit log. Catalog membership SHALL come from declared capabilities, with drafts unadopted and missing declarations explicit; empty bands SHALL retain an honest absence line. The editorial plan SHALL identify the central reader question, supported thesis, progression of explanations, material tensions, stopping-depth obligations and reasons for diagram, glossary and deep-dive selection for the chosen audience. Material editorial omissions SHALL have reasons, and a qualification reversing a promise SHALL remain at the affected depth. A diagram SHALL identify the relationship it clarifies, with support for factual edges as well as nodes; a figure quota SHALL NOT establish explanatory value. Optional depth SHALL answer a distinct useful question; a component deep dive SHALL explain supported purpose, responsibility, neighboring interactions and limits rather than repeat its parent or dump source text. Glossaries SHALL explain concepts where needed for comprehension. Project-specific headings and composition SHALL preserve the existing primary altitude order, authority bands and required populations; missing content SHALL remain honestly absent or Unknown, not invented to fill a template.

ID: REQ-polaris-generation-004
Source: RFC7-13; governing warrants below.
Scope: v1-mandatory


#### Scenario: Qualified claim shortened

- **WHEN** a declaration contains a material exception or condition
- **THEN** every shortened claim retains the qualification needed for its meaning or is withheld from that reading depth
- **AND** the complete relevant source remains reachable

#### Scenario: No supported optional asset

- **WHEN** the sources do not establish a glossary definition or a proposed map relationship
- **THEN** the presentation omits unsupported decoration and discloses any resulting knowledge gap
- **AND** it does not fabricate content merely to fill a template

#### Scenario: Deeper content cannot rescue a failed introduction

- **WHEN** the complete declaration explains the thesis but the opening omits it or misstates it
- **THEN** the opening-depth review fails and the candidate cannot become ready
- **AND** a reviewer evaluates each required depth against its own frozen questions before using deeper content

#### Scenario: Required visual unavailable

- **WHEN** a requested or acceptance-required visual lacks source support, authorization or a supported renderer capability
- **THEN** its disposition names the unresolved condition and the corresponding readiness criterion remains unmet
- **AND** extra reads, live transclusion, a doorway or a decorative/textual substitute cannot silently clear that obligation

#### Scenario: Primary altitudes and one-step source access

- **WHEN** a primary narrative has no owner ruling changing its default altitude order
- **THEN** it offers thesis/manifesto, architecture story, capability catalog, capability deep dive and verbatim specification leaf in that order, with each stopping depth independently honest
- **AND** each anchored block reaches the owning artifact in one step regardless of browsing depth; a differently ordered additional narrative still meets each altitude obligation

#### Scenario: Capability detail keeps three authority classes

- **WHEN** a generated deep dive combines an explanation, requirements and current reality
- **THEN** its default argument, contract and reality bands appear in that order with exactly one of the three authority classes declared per band in human and machine forms
- **AND** reality facts come from the shared drawer, the contract band links exact owning text, and an empty band collapses to an honest absence line with the relevant Unknown reason instead of disappearing or leaving scaffold headings

#### Scenario: Catalog membership comes from declarations

- **WHEN** code names and a draft capability suggest functionality absent from adopted capability declarations
- **THEN** the catalog preserves declared identities, visibly marks the draft unadopted and renders undeclared or unmapped coverage Unknown with its reason and route
- **AND** the model cannot invent a declared capability from code, and a predominantly Unknown catalog remains a normal honest presentation

#### Scenario: Capability bands preserve their actual content populations

- **WHEN** a capability has motivating intent, related capabilities, accepted contract/topology references, implementation mappings and intent history
- **THEN** argument exposes its motivating principle/decision and related capabilities; contract exposes its accepted contracts, declared topology placement and operative requirements/scenarios; reality exposes the four distinct SDR-3 mapping classes and adoption/amendment/dismissal history
- **AND** missing contents retain their explicit absence/Unknown rather than disappearing, and a commit log cannot substitute for intent history

#### Scenario: Accurate catalog, unsuccessful explanation

- **WHEN** a draft lists correct features but independent readers cannot explain
  why the project exists or how those features support its purpose
- **THEN** argument/comprehension remains failed despite accurate individual facts
- **AND** repair revisits the argument and necessary understanding, not merely
  headings or additional citations.

#### Scenario: Meaningful visual instead of decorative quota

- **WHEN** a long architecture explanation obscures a material relationship that
  a supported diagram can clarify
- **THEN** the author/design review identifies the question, requires a useful
  relationship treatment and checks the rendered result
- **AND** inserting boxes with supported nouns but unsupported or meaningless
  arrows cannot close the finding; a figure count is not the acceptance oracle.

#### Scenario: Concision and optional depth preserve meaning

- **WHEN** a shorter introduction would omit a qualification that reverses its
  apparent promise, or a deep dive only repeats its parent
- **THEN** the qualification remains at the affected stopping depth and the
  redundant depth is repaired or explicitly omitted where optional
- **AND** source/catalog navigation cannot become the only way to understand the
  thesis, while required exact-source access remains available.

Form: state projection/query.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: RFC7-13
  doctrine: [VIS-1, VIS-3, VIS-7]
  contracts: [RFC7-13, RFC7-14, RFC7-19, RFC7-15, RFC7-16, RFC7-17, RFC7-18]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [SDR-3]
  topology: []
  parent_requirements: []
```

### Requirement: Independent review and repair

A draft SHALL become ready for owner review only after independent fidelity and rendered-design reviews confirm the frozen bundle and all blocking findings have dispositions verified against that same bundle. Fidelity review SHALL use an independently prepared, frozen inventory of material source claims, qualifications, conflicts and trade-offs, covering the entire admitted source population. The fidelity reviewer SHALL verify inventory accuracy and completeness against the owning admitted sources rather than trusting preparation output. It SHALL record both inventory-to-draft coverage and draft-to-source support, including justified omissions; unresolved material omissions SHALL prevent readiness. The candidate-authoring stage SHALL NOT define or narrow its own review denominator. The bounded workflow SHALL prepare or validate the independent inventory and questions from admitted sources, accounting for those calls in its run budget; it SHALL NOT require the owner to hand-author project-specific editorial preparation before starting. Reviewers SHALL receive the artifact, governing references and acceptance criteria without the authoring conversation. A revision SHALL retire dependent review evidence. Every candidate that changes the reading order, section set, anchor targets or manifesto/thesis, and every target-changed block, SHALL receive the fresh-reader review required by RFC7-25 before becoming ready; failed review remains recorded and visible. The generator SHALL not classify its own wording change as immaterial. Findings SHALL identify the deficient subject as discovery, understanding, clarification, argument, prose, asset or rendering. Research or inventory findings SHALL reopen the deficient artifact for repair and independent source review, invalidating dependent plans, drafts, assets and reviews. Editing prose against an unchanged defective inventory SHALL NOT close an inventory finding. The original finding, repair, dispositions and input/output identities SHALL remain traceable. Further acquisition SHALL use its required new admitted input identity and consume remaining original bounds or a separately authorized new run; repair SHALL NOT broaden permission, erase spent usage or replay an uncertain effect.

ID: REQ-polaris-generation-006
Source: VIS-3; governing warrants below.
Scope: v1-mandatory


#### Scenario: Meaningful rendered review

- **WHEN** the draft is reviewed after rendering
- **THEN** the retained review assesses its argument, capability explanation, visual hierarchy, navigation and source fidelity using actual artifacts
- **AND** heading presence, anchor counts or accessibility results alone do not establish confirmation

#### Scenario: Revision after confirmation

- **WHEN** any reviewed block, anchor set, reading order or asset is changed
- **THEN** the affected confirmation is retired and readiness identifies the remaining review
- **AND** the old raw review remains preserved against its original subject

#### Scenario: Source trade-off omitted entirely

- **WHEN** all generated claims have anchors but an independently inventoried material trade-off is absent from the account
- **THEN** source-to-draft coverage records the omission as a blocking finding
- **AND** an author-generated outline or claim list cannot replace the independent source inventory

#### Scenario: Omitted material qualification

- **WHEN** independent source review finds a material admitted qualification that
  both inventory and draft omitted
- **THEN** the inventory is repaired and re-reviewed against the source population;
  dependent argument, draft and asset reviews become stale
- **AND** the finding remains open if only its wording is inserted into a paragraph
  while the source-understanding defect and affected artifacts remain unchanged.

#### Scenario: New evidence outside the current budget or authority

- **WHEN** a finding requires acquisition the existing permission or remaining
  budget cannot support
- **THEN** the run records the unresolved dependency and affected readiness
- **AND** no repair loop expands access, erases spent usage or disguises a new run
  as a resumed old one.

Form: lifecycle transition.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: VIS-3
  doctrine: [VIS-1, VIS-3]
  contracts: [RFC7-9, RFC7-13, RFC7-25]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Source drift and regeneration

A source or generation-policy change SHALL create a distinct generation context and invalidate affected readiness/adoption applicability. Regeneration SHALL produce a separately reviewable candidate through the same supported workflow without editing renderer code or compiled passage offsets. Previously curated prose SHALL remain attributable and recoverable, with drift visible. Broken anchors SHALL follow RFC7-11's claim reason and distinct navigation outcome; resolving target changes SHALL follow RFC7-11(a) without inventing an epistemic reason. A new evaluation identity alone SHALL NOT count as target drift. Captured authorship state SHALL remain immutable and only the applicable authoring act that rereads the target may clear the drift marker. A changed, corrected or withdrawn attributed owner answer SHALL produce a distinct generation context and identify affected thesis, explanations, diagrams, terms, deep dives and review applicability through recorded dependencies. All artifact kinds SHALL be reevaluated against the same changed supported understanding. An unchanged URL, label or question identifier SHALL NOT restore an obsolete answer or review's eligibility. A narrower owner-selected project scope after discovery failure SHALL be a separately identified request and SHALL NOT turn the original broader request into a successful one.

ID: REQ-polaris-generation-009
Source: VIS-6; governing warrants below.
Scope: v1-mandatory


#### Scenario: Changed source

- **WHEN** a previously rendered project changes a source declaration
- **THEN** Polaris identifies the affected stale presentation and offers a newly bound generation run
- **AND** the old review and authorship act are not transferred to the new candidate

#### Scenario: Preserve human curation

- **WHEN** regeneration completes for a human-curated presentation
- **THEN** the new editorial draft is separate and the authored predecessor remains identifiable and recoverable
- **AND** replacement requires its own applicable per-block human authorship act

#### Scenario: Broken and retired anchor targets degrade explicitly

- **WHEN** an existing anchor fails to resolve, separately because its target is missing and because it is retired
- **THEN** the primary block and same-evaluation machine answer show the named break, claim Unknown with reference-unresolvable and repair-reference route, separately from navigation unresolvable or retired
- **AND** the renderer neither drops the anchor, guesses a replacement nor silently follows a successor; keyboard expansion reaches the same break explanation

#### Scenario: Resolving target drift differs from an evaluation tick

- **WHEN** an anchor still resolves after a rule revision or kernel label/tier/reason change, while a control case changes only kernel evaluation identity
- **THEN** the changed case shows anchored — target changed since authorship with recorded versus current state and review required on the primary surface and machine answer; the evaluation-only case has no drift marker
- **AND** captured author-time state remains immutable, drift creates no new Unknown reason, and rereading or regenerating alone cannot clear it without the applicable fresh authoring act that rereads its target

#### Scenario: Overview disagrees with current authority

- **WHEN** the fixed primary account retains an older promise while its still-resolving owning authority now qualifies that promise
- **THEN** the affected account is visibly stale or target-changed and is offered for review/regeneration
- **AND** historical prose and authorship remain recoverable and are not presented as current merely because their source link resolves

#### Scenario: Clarification changes meaning

- **WHEN** an attributed answer changes or is withdrawn
- **THEN** the affected thesis, explanations, diagrams, terminology, deep dives
  and reviews are identified through their dependencies and reevaluated
- **AND** prior generated content cannot silently regain eligibility by retaining
  the same question identifier or an obsolete owner answer.

Form: event-response.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: VIS-6
  doctrine: [VIS-1, VIS-2, VIS-6]
  contracts: [RFC7-11, RFC7-20, RFC7-21, RFC7-25]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Safe accessible presentation

Generated pages SHALL render untrusted source and provider content inertly, make distinctions recoverable by keyboard and assistive technology, maintain readable contrast and fit on desktop/mobile, and keep navigation and lengthy technical reference material from obstructing the default account. Exact normative leaves SHALL retain their owning identity and verbatim text; generated prose SHALL NOT substitute for the owning artifact's text. Diagram text equivalents SHALL preserve elements, relationships, anchors, legends and markings. Tables, contents, glossary routes and visual-reference controls SHALL retain their semantics and required paths in machine output and keyboard/nonvisual use. Contents SHALL derive destinations from actual reading structure; contextual definitions and glossary links SHALL refer to the same supported term entry. The desktop reading SHALL provide a navigable left section drawer and use available horizontal space meaningfully for orientation and informative figures while keeping prose comfortably readable. Mobile navigation SHALL start compactly and expose the same required destinations. Sources SHALL support the default argument rather than dominate it. Actual design review SHALL assess deliberate composition across the opening, representative middle, diagrams and optional depth; an attractive opening SHALL NOT compensate for inaccessible or incomprehensible later reading. These choices SHALL preserve existing visual meanings, source routes, required disclosures and nonvisual equivalents.

ID: REQ-polaris-generation-012
Source: VIS-7; governing warrants below.
Scope: v1-mandatory


#### Scenario: Malicious source or output

- **WHEN** an input contains executable markup, unsafe links or instructions to broaden tool access
- **THEN** rendering executes none of that content and the workflow obtains no new authority from it
- **AND** excluded or unclassifiable content is not revealed in assets or diagnostics

#### Scenario: Actual reader navigation

- **WHEN** a reader uses narrow and wide viewports and keyboard-only navigation
- **THEN** the opening, contents, terminology and exact-source path remain usable without overlays, clipped targets or horizontal page overflow
- **AND** source lists and detailed remediation remain reachable without dominating the first reading

#### Scenario: Exact adopted leaves remain operative in proposed context

- **WHEN** a reader reaches a requirement and its scenarios or doctrine rule from a generated account in Proposed context
- **THEN** the owning text remains verbatim and operative with any proposal delta adjacent, distinctly marked and non-anchorable
- **AND** presentation ordering and annotations create no stored reorganized normative copy, and export/query preserves which text is operative

#### Scenario: Minimal status retains its epistemic strength at rest

- **WHEN** a major claim or capability has a kernel label, tier, freshness and evaluation
- **THEN** the default narrative exposes those values with a drawer/handoff and visible staleness, without a composite maturity score or metric wall
- **AND** generated prose cannot strengthen the status or hide its tier in deeper disclosure

#### Scenario: Full reading and responsive navigation

- **WHEN** the same generated account is read at desktop and mobile widths and through keyboard/nonvisual paths
- **THEN** desktop section navigation uses the left drawer, mobile navigation starts compactly, and each required destination remains reachable
- **AND** review includes the middle, diagrams and optional depth; an attractive opening cannot discharge a blocking composition or navigation finding elsewhere.

Form: invariant.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: VIS-7
  doctrine: [VIS-1, VIS-3, VIS-7, SEC-1, SEC-5]
  contracts: [RFC7-13, RFC7-14, RFC7-33, RFC7-34]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Reusable product validation

Generator completion SHALL require independent evidence from two substantively different, separately admitted real project domains using one unchanged supported generation path, including fresh generation and source-change regeneration. Independent cold readers SHALL record their understanding and navigation, and design reviewers SHALL assess the actual rendered argument and experience. Before candidate narrative drafting in the product evaluation, independent evaluators SHALL freeze project-specific comprehension questions, source-backed expected answers and blocking design/comprehension criteria directly from the admitted sources, outside the generator under test. The run's own inventory, questions or review verdict SHALL NOT serve as the sole completion oracle. Unresolved confident factual errors, inability to explain a supported central thesis or capability relationships, inaccessible required reading paths, and blocking visual findings SHALL prevent completion. Repairs SHALL require dispositions and a fresh passing evaluation of the changed output. At least one real evaluation SHALL require synthesis across verbose or scattered sources; replaying an already curated manifesto is insufficient. Synthetic tests and curated golden pages SHALL remain explicitly limited evidence. Evaluation SHALL disclose supported profiles and freeze case repository/snapshot, admitted classes, project boundary, audience, interpretation and scale bounds, permitted owner participation, and engine/prompt/schema/renderer versions before generation. Independent evaluators SHALL freeze material facts, qualifications, conflicts, unknowns, reader questions and acceptable answers, relationships and counterexamples, required reading routes, and blocking design criteria directly from admitted sources, outside producer context. Expected case outcomes SHALL distinguish a supported whole account, a correct bounded partial account, required clarification and unsupported/refused scope. Evaluation SHALL include a project configuration held out from project-specific recipe tuning and challenge conditions for sparse intent, unconventional or multi-package structure, source disagreement, verbose populations, generated or misleading bulk, unsupported relationships, unavailable sources or interpretation support, and changed meaning. Characteristics MAY coexist in one case; synthetic challenges SHALL NOT replace the existing two-real-project obligation. Every attempt, repair, failure and abandoned run SHALL remain represented under applicable retention rules. Separate judgments SHALL cover scope, understanding, argument, asset fidelity, reader experience, owner effort, regeneration and operational behavior, with unmet/unproven distinctions and reasons for any evaluation-local non-applicability rather than a universal quality score. Actual owner interventions SHALL distinguish consequential clarification from manual inventory, outline or prose rescue without an invented universal time threshold. Reader evidence SHALL cover successive stopping depths and actual narrow/wide, keyboard and nonvisual paths across the full reading. Comparison with the repository entry point and a simple source-summary baseline SHALL use equivalent questions and permissions; winning a comparison SHALL NOT waive any blocking finding. Evaluator corrections SHALL retain reasons and prior oracle versions. New owner premises SHALL receive an independently frozen oracle extension from admitted attributed input before revised-output evaluation; generated prose or internal verdicts SHALL NOT supply that extension. Affected earlier judgments SHALL become inapplicable but remain traceable. Correct partial/refusal behavior and successful narrowed requests SHALL NOT count as completed original whole-project manifestos or universal codebase support.

ID: REQ-polaris-generation-014
Source: VIS-3; governing warrants below.
Scope: v1-mandatory


#### Scenario: Generality and comprehension

- **WHEN** the same generator is evaluated on two admitted projects
- **THEN** retained runs and reader records demonstrate each project's distinct purpose, thesis, motives, boundaries and capability relationships without project-specific source edits
- **AND** the reviewers identify source-backed answers, confident errors, navigation failures and visual/comprehension findings

#### Scenario: Narrow evidence offered as completion

- **WHEN** only synthetic provider runs, a Butlers-specific page or unchanged golden artifacts are available
- **THEN** the completion report marks real generation, regeneration and reader-quality requirements unproven
- **AND** no test score or successful provider response is substituted for that missing evidence

#### Scenario: Reader records show unresolved failure

- **WHEN** retained reader answers contain a confident source-induced factual error or cannot explain the supported central thesis
- **THEN** product completion remains unmet despite passing mechanical checks and the existence of reader records
- **AND** a repaired asset needs a fresh passing reader/design evaluation rather than a rewritten verdict over the failed output

#### Scenario: Unfamiliarity without project-specific patching

- **WHEN** the frozen engine, supported adapters, prompts and renderer are used on
  an admitted project held out from recipe tuning
- **THEN** the evaluation records input/profile differences and actual reader
  outcomes without manually fixing generated content or adding project branches
- **AND** failure remains a failure even if a bespoke page for that project can be
  produced outside the unchanged process.

#### Scenario: Correct partial account and false universal claim

- **WHEN** a case lacks purpose evidence or exceeds declared interpretation support
- **THEN** the evaluator checks the correct uncertainty, question or scope refusal
  and reports the incomplete manifesto separately
- **AND** neither success on two selected projects nor correctness on that partial
  case establishes support for every codebase.

#### Scenario: Shared model blind spot

- **WHEN** authoring and internal review agree on an account that omits an
  independently identified material source fact
- **THEN** the external evaluation fails it using the frozen source-derived oracle
- **AND** additional agreeing model verdicts do not override the missing support.

#### Scenario: Clarification changes the evaluation premises

- **WHEN** an owner answer establishes a purpose absent from the initial frozen
  evaluation sources
- **THEN** independent evaluators record its admitted attribution and freeze a
  source-derived oracle extension before judging the revised draft
- **AND** affected prior judgments become inapplicable, while the original
  insufficient-intent result remains recorded; neither producer prose nor an
  internal model verdict supplies the new expected answer.

#### Scenario: Complete case reporting and owner effort

- **WHEN** evaluation includes an abandoned attempt, manual prose rescue and a correct partial account alongside a successful generated account
- **THEN** the report retains each outcome and classifies the owner interventions, with separate scope, understanding, argument, fidelity, experience, effort, regeneration and operations judgments
- **AND** baseline comparisons and universal scores cannot hide a blocking finding or relabel the partial/rescued case as an independently generated whole manifesto.

Form: invariant.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: VIS-3
  doctrine: [VIS-1, VIS-2, VIS-3]
  contracts: [RFC7-13, RFC7-25, RFC7-30, RFC7-34]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Versioned interchange and reference integrity

Generator records SHALL use explicit class/version and typed variants with separate ownership for requests, inventories, controls, generated assets, Execution Records and authored content. Each requested asset SHALL have its own identity, kind, requiredness and purpose, resolving to one produced, omitted or unresolved disposition; produced SHALL reference actual matching assets while unresolved SHALL NOT fabricate output identities or digests. Provider-local handles SHALL NOT mint presentation or kernel identities: a trusted recorded authoring operation SHALL issue opaque presentation identities with retained provenance, without claiming human adoption. Serialized editorial/profile flags SHALL NOT replace effective owner-act evaluation. Canonical anchors SHALL use RFC7-10's target-specific identity, fragment and state representation, distinguishing artifact revision from kernel evaluation and verbatim label/tier/reason. PWB wire conventions SHALL be preserved through explicit compatibility adaptation, never silently promoted into a generic schema or used to widen source admission. Unsupported adaptation SHALL remain explicit without invented identity/state. Required internal references SHALL resolve; definitions SHALL be unique, support references SHALL belong to their claim block, and ownership/containment and stage-input graphs SHALL be acyclic. Supported factual relationship cycles and glossary cross-reference cycles SHALL remain representable. Validation SHALL reject duplicate object keys, unknown interchange versions/kinds, undeclared effect-bearing fields and exceeded structural/content bounds without silent truncation. Shape validity SHALL NOT establish authority, fidelity, readiness or authorship. Newer unsupported plane versions SHALL forbid writes/downgrade and render uninterpretable content Unknown; older content SHALL use declared compatibility paths without mutation on read. Persistent migration SHALL require its own reviewed, attributed, atomic and reversible act, preserving the identities, meanings and citation resolution protected by RFC3-23; OpenSpec content SHALL remain outside that migration authority. Versioned discovery-scope, project-understanding, clarification and argument records SHALL retain their owning inputs, dependencies, coverage and omission dispositions, questions and attributed answer revisions, contradiction or interpretation dispositions, and links to generated artifacts and affected reviews. They SHALL be reviewable projections, not new authority stores or automatically adopted ontologies. Existing owning identities SHALL be referenced through their contracts; temporary research handles SHALL NOT mint kernel facts. Prose, diagrams, glossary and deep dives SHALL share the same supported understanding and dependency identities. Producer understanding and internal review records SHALL NOT replace independent source/evaluation oracles. Clarification persistence and draft use SHALL require applicable input classification, content consent and retention; an answer SHALL NOT become evidence of implementation or an intent-adoption/write act by being serialized.

ID: REQ-polaris-generation-019
Source: RFC7-10; governing warrants below.
Scope: v1-mandatory

#### Scenario: Provider claims an existing identity or curated state

- **WHEN** model output uses an existing identifier as a local handle or asserts curated/profile-adopted state
- **THEN** trusted validation resolves local handles without minting or replacing kernel identities and derives effective state from owning records
- **AND** draft production cannot become human adoption or override an unsigned presentation profile

#### Scenario: Two requested diagrams have different obligations

- **WHEN** one required computed diagram and one optional editorial diagram are requested and only the editorial diagram is produced
- **THEN** separate request identities retain their own dispositions and the required computed request stays unresolved without a fabricated output digest
- **AND** duplicate kind labels or produced optional content cannot discharge that required request

#### Scenario: PWB revision cannot establish a kernel evaluation

- **WHEN** a compatibility input contains a revision but lacks the canonical evaluation identity or captured tuple needed for a kernel reference
- **THEN** adaptation reports the typed inability without coercing the revision into an evaluation or inventing label/tier/reason values
- **AND** the adopted PWB form retains its own meaning and source-admission limits

#### Scenario: Structural and semantic cycles differ

- **WHEN** input contains a section-containment or stage-input cycle, a dangling internal reference or an out-of-block support reference
- **THEN** validation refuses the malformed composition without silently deleting a reference
- **AND** a supported relationship cycle or glossary cross-reference cycle alone remains valid

#### Scenario: Unsupported version is read

- **WHEN** a consumer encounters an unknown interchange version or a newer unsupported plane schema
- **THEN** unknown interchange is refused without interpreting unknown fields, and the newer plane is neither written nor downgraded
- **AND** uninterpretable plane content is Unknown rather than a partially parsed whole, with no lazy migration

#### Scenario: Duplicate keys or silently truncated content

- **WHEN** a provider response repeats an object key or exceeds declared structural/content limits
- **THEN** validation rejects the ambiguous or incomplete record with permitted bounded diagnostics
- **AND** accepting one duplicate value or dropping an array tail cannot make the original output complete

#### Scenario: Canonical anchors reject presentation and unstable targets

- **WHEN** a provider supplies a narrative/draft/rendering target, an unknown anchor class or a label/path in place of a durable target and fragment
- **THEN** validation refuses each invalid anchor instead of coercing it into evidence
- **AND** valid target-specific variants retain their owning identity and captured revision/state, and opaque presentation IDs are issued with recorded provenance independently of labels

#### Scenario: Research projection cannot mint authority

- **WHEN** a supported research interpretation or owner answer enters an understanding record and feeds several artifact kinds
- **THEN** its input identity, epistemic class, attribution and dependencies remain inspectable across prose, diagrams, glossary and depth
- **AND** serialization neither creates kernel facts or adopted intent nor lets the producer's record become the independent evaluation oracle.

Form: invariant.

- **Case:** Exercise each record variant and independently mutate identity references, state assertions, versions, keys, graph edges and bounds.
- **Observable:** Parse result, trusted identity issuance, typed resolution, requested-asset dispositions, effective states and attempted writes.
- **Oracle:** Governing identity/state contracts and independently defined valid/invalid records; provider assertions never supply expected authority.
- **Falsifier:** A provider mints authority, unsupported content is silently coerced, required output is invented, meaningful graph cycles are banned, or reading mutates/downgrades the plane.

```yaml
warrants:
  primary: RFC7-10
  doctrine: [VIS-1, VIS-2, VIS-4, VIS-6, VIS-7, SEC-3, SEC-4, SEC-5]
  contracts: [RFC3-22, RFC3-23, RFC3-24, RFC3-25, RFC3-26, RFC7-5, RFC7-9, RFC7-10, RFC7-11, RFC7-20, RFC7-21]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

## ADDED Requirements

### Requirement: Accounted unfamiliar-project discovery

The generator SHALL perform question-directed, bounded discovery for a selected project only after the applicable metadata-only start preparation, work/admission gates and effect permissions; investigation SHALL NOT read sources to authorize itself. Before claiming source coverage it SHALL expose the selected project boundary and audience, admitted source classes, supported languages/source forms/repository shapes and scale bounds, inspected and selected material, and reasons relevant material is excluded, unavailable, unresolved or deferred by budget. It SHALL NOT assume a prescribed layout, equate one repository with one thesis, or treat a README or retrieved subset as the complete project. A frozen supported profile SHALL NOT be retrospectively narrowed to relabel an in-profile failure as unsupported success. The stopping reason SHALL identify supported sufficiency within scope, unavailable source, unsupported interpretation, budget exhaustion or an unresolved boundary requiring owner selection. Body, code, history and other content reads SHALL remain individually covered by applicable consent and classification; no shell or observed-project execution is implied. Source-scope changes SHALL create identified inputs and invalidate dependent coverage. Supported partial findings SHALL remain inspectable, while a narrower requested scope SHALL be separately identified and SHALL NOT pass the original broader request.

ID: REQ-polaris-generation-030
Source: SEC-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Purpose outside the obvious entry point

- **WHEN** an independently prepared case places material purpose and architecture
  information in permitted sources outside its README and conventional directories
- **THEN** the discovery account identifies the relevant material and its role in
  the understanding, or explicitly reports the unsupported discovery boundary
- **AND** an apparently complete account based only on the entry point fails the
  evaluation when that omitted material changes its meaning.

#### Scenario: Partial access and finite research

- **WHEN** a material question needs a denied source, unsupported interpreter or
  more research than the remaining budget permits
- **THEN** the run records that question, the applicable reason and affected scope
- **AND** it neither reads the denied content nor substitutes lack of retrieval for
  absence of a capability, source or qualification
- **AND** the owner may inspect the supported partial account without it claiming
  whole-project coverage
- **AND** a later accepted narrower scope is a separately identified request; it
  does not convert failure to satisfy the original requested scope into success.

#### Scenario: Multiple applications in one repository

- **WHEN** discovery identifies several potential project boundaries and the
  selected profile does not determine which is the requested subject
- **THEN** the owner sees the candidate boundaries and why selection matters
- **AND** no single-project thesis or relationship claim is silently constructed
  by merging unrelated packages; declared child relationships retain existing rules.

Form: event-response.

- **Case:** Exercise the named cases using independently prepared source populations, permission outcomes, supported profiles and attributed owner responses.
- **Observable:** Inspect the discovery/question account, source reads, scope disposition, answer revisions, dependencies and resulting human/machine presentation.
- **Oracle:** Frozen source-derived expectations and governing authority evaluations prepared outside the generator; producer coverage flags and prose are not expected truth.
- **Oracle independence:** Evaluate omissions and necessary questions against owning sources before seeing generated arguments; preserve explicit unknown answers.
- **Falsifier:** A denied source is read, an unsupported purpose becomes fact, partial scope becomes whole-project success, an answer self-adopts or repair evades original bounds.

```yaml
warrants:
  primary: SEC-2
  doctrine: [VIS-1, VIS-2, VIS-3, SEC-2, SEC-3, SEC-5]
  contracts: [RFC7-20, RFC7-40, RFC4-5]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: [REQ-polaris-generation-001, REQ-polaris-generation-005, REQ-polaris-generation-017, REQ-polaris-generation-020, REQ-polaris-generation-025]
```

### Requirement: Consequential owner clarification

After investigation within admitted bounds, the generator SHALL present the smallest useful prioritized group of unresolved questions material to the requested account, identifying evidence considered and the draft consequence of each answer. It SHALL offer supported interpretations where available, free-text correction and an explicit leave-unknown or defer path. An unsupported central thesis SHALL require clarification or remain explicitly unestablished; supported partial architecture/account exploration MAY remain available without claiming a complete manifesto. Attributed answers, presentation preferences and adopted intent SHALL remain distinct existing classes, with permitted use and revision/withdrawal dispositions recorded. An answer SHALL NOT prove implementation or adopt intent without its applicable act and write checks. Unchanged questions SHALL reuse prior answers or dispositions rather than be repeatedly asked. Question groups, research and clarification/repair loops SHALL have finite declared limits and consume original remaining bounds or a visibly new authorized run; owners SHALL NOT have to prewrite an inventory or outline. Answer changes and withdrawals SHALL invalidate dependent content and review applicability under REQ-polaris-generation-009. Missing input/persistence consent SHALL preserve the limitation without silently retaining or using the answer.

ID: REQ-polaris-generation-031
Source: VIS-4; governing warrants below.
Scope: v1-mandatory

#### Scenario: Mechanics without purpose

- **WHEN** the admitted repository supports an architectural explanation but
  supplies no sufficient purpose or beneficiary premises
- **THEN** Polaris asks the consequential purpose question with its scope and
  reason, while preserving useful supported findings
- **AND** it offers no fabricated mission or founder story as a default fact.

#### Scenario: Owner declines to establish purpose

- **WHEN** the owner leaves the purpose unknown
- **THEN** the resulting account retains that limitation and no confidence badge
  or completion claim covers it

#### Scenario: Owner supplies new purpose input

- **WHEN** the owner supplies a purpose statement
- **THEN** its attribution, revision and permitted draft use are recorded
- **AND** the statement neither proves implementation behavior nor adopts itself
  into project intent without the existing applicable act and write checks.

#### Scenario: Questions cannot become an endless interview

- **WHEN** optional uncertainties remain after the declared question or research
  budget is exhausted, or an unchanged question was already deferred
- **THEN** the owner sees the remaining scope and can continue with a limited
  account or stop; the process does not repeat questions or extend spending
- **AND** consequential unresolved facts remain explicit in the affected reading.

Form: event-response.

- **Case:** Exercise the named cases using independently prepared source populations, permission outcomes, supported profiles and attributed owner responses.
- **Observable:** Inspect the discovery/question account, source reads, scope disposition, answer revisions, dependencies and resulting human/machine presentation.
- **Oracle:** Frozen source-derived expectations and governing authority evaluations prepared outside the generator; producer coverage flags and prose are not expected truth.
- **Oracle independence:** Evaluate omissions and necessary questions against owning sources before seeing generated arguments; preserve explicit unknown answers.
- **Falsifier:** A denied source is read, an unsupported purpose becomes fact, partial scope becomes whole-project success, an answer self-adopts or repair evades original bounds.

```yaml
warrants:
  primary: VIS-4
  doctrine: [VIS-1, VIS-2, VIS-3, VIS-4, SEC-2, SEC-4]
  contracts: [RFC7-20, RFC7-21, RFC3-16]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: [REQ-polaris-generation-002, REQ-polaris-generation-005, REQ-polaris-generation-009, REQ-polaris-generation-010, REQ-polaris-generation-016, REQ-polaris-generation-019, REQ-polaris-generation-020, REQ-polaris-generation-025]
```
