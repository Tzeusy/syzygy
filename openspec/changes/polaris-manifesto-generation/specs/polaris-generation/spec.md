# Polaris generation

Candidate specification — binds nothing until the required owner adoption.

Generate project-specific manifesto assets through a reusable, bounded editorial
workflow that preserves truthful reading depths and human authorship control.

## ADDED Requirements

### Requirement: Admitted project input

The generator SHALL accept an identified project source snapshot only after the applicable read, classification and provider permissions have been evaluated. Caller-supplied approval flags SHALL NOT substitute for that evaluation. Bundle content and captured claims SHALL match their owning admitted records; retaining a legitimate source reference while altering the supplied claim SHALL not bypass integrity checks. Missing or invalid authority SHALL prevent the corresponding effect and leave the deterministic source-backed view available with the reason. For absent or withdrawn provider consent, the draft layer SHALL render Unknown (`unconsented-source-or-provider`) as a policy state in both channels, including when a prior draft remains retained.

ID: REQ-polaris-generation-001
Source: SEC-2; governing warrants below.
Scope: v1-mandatory


#### Scenario: Two project identities

- **WHEN** two independently admitted snapshots from distinct project domains are supplied through the supported input boundary
- **THEN** the unchanged generator accepts each with its own project identity, source references and states
- **AND** neither project name nor a compiled content hash requires an application-source edit

#### Scenario: Permission absent or withdrawn

- **WHEN** a required read or provider permission is absent, withdrawn, mismatched or no longer effective before dispatch
- **THEN** the disallowed effect is not performed and its reason is visible in human and machine run views
- **AND** the available deterministic presentation remains readable without generated prose

Form: event-response.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: SEC-2
  doctrine: [SEC-2, SEC-5, VIS-2]
  contracts: [RFC7-20, RFC3-16]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Project argument and voice

The generator SHALL construct an editorial draft that explains the supported purpose, thesis, motives, promises, boundaries, essential concepts and capability relationships in a coherent project-specific argument. Source-supported inference SHALL expose its admitted premises and inferred status. Motives, history, definitions and relationships without sufficient source premises SHALL remain absent or Unknown; an Inferred label alone SHALL NOT make speculation eligible. Generated prose SHALL NOT impersonate an author or present invented first-person statements as quotations.

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

### Requirement: Bounded anchored assets

Each generated narrative block and supporting asset SHALL have its declared presentation role and generation provenance. Requested model identity and provider-reported version SHALL be distinguished; unavailable version information SHALL be explicit, not guessed. The bundle SHALL declare its reproducibility standard without promising identical generated bytes unless supported. Anchored claims SHALL have sufficient, minimal source support; non-normative framing SHALL NOT carry unused anchors. The asset bundle SHALL distinguish source claims, supported inference and non-normative framing and preserve captured epistemic states. Source anchors SHALL use the closed classes and durable revision/evaluation-bound identities required by RFC7-10, not labels or paths as identity. Human HTML and machine presentation SHALL derive from that same bundle, without making it authoritative or an anchor target. The versioned bundle SHALL distinguish narrative sections, contents, glossary, comparison tables, curated relationship diagrams and computed visual references. Unknown variants and effect-bearing extensions SHALL be refused. Generated diagrams SHALL remain editorial-draft until their applicable authorship act; every named element SHALL carry an anchor or non-normative/proposed marking, factual relationships SHALL be supported, and faithful legends and human/machine curated/computed provenance SHALL prevent proposed or editorial structure from impersonating computed project-map truth. Curated diagrams SHALL NOT claim reproducibility from the project snapshot. Computed references SHALL resolve only through an existing supported and authorized governed renderer at an identified evaluation, selection, scenario and declared view scope, retaining its applicable RFC9, machine-parity and nonvisual obligations. Provider-supplied facts, geometry, scripts or arbitrary embed URLs SHALL NOT substitute. This capability SHALL NOT activate deferred live Orrery transclusion or acquire additional source content to resolve a reference. Declared generation limits SHALL bound asset count, nodes/edges, table cells, text and total output; exceeded bounds SHALL identify the affected incomplete asset rather than silently truncate it. Every narrative-model unit SHALL preserve its presentation-only and non-citable semantics across rendering and export. The narrative SHALL NOT supply evidence, snapshot inputs, implementation mappings or work warrants; its deletion SHALL leave those owning records and their answers unchanged. Attribution SHALL be recoverable at claim-block granularity, splitting ambiguous blocks rather than adding unused citations.

ID: REQ-polaris-generation-003
Source: RFC7-20; governing warrants below.
Scope: v1-mandatory


#### Scenario: Aligned human and machine views

- **WHEN** a bundle is rendered for a reader and queried by a machine
- **THEN** both views identify the same blocks, source anchors, captured states, reading structure and editorial-draft state
- **AND** generation provenance identifies the model, version, policy and input snapshot

#### Scenario: Unsupported or surplus anchor

- **WHEN** a claim lacks sufficient support or carries an unrelated supporting anchor
- **THEN** the bundle records a fidelity finding and cannot become ready for owner adoption
- **AND** qualifying a source claim as stronger than its captured state is also a finding

#### Scenario: Editorial relationship diagram

- **WHEN** admitted sources support a relationship explanation and the generator composes a diagram
- **THEN** the diagram and equivalent text carry the supported relationships, per-element anchors or non-normative/proposed markings, faithful legend and editorial-draft provenance
- **AND** unsupported or proposed structure cannot appear as existing computed-map structure

#### Scenario: Supported computed visual reference

- **WHEN** an authorized existing renderer supports a requested reference at its identified evaluation, selection, scenario and view scope
- **THEN** the rendered asset preserves that renderer's provenance and applicable map, machine and nonvisual obligations
- **AND** model-generated geometry, scripts, arbitrary URLs and live transclusion cannot substitute for that result

#### Scenario: Asset exceeds declared generation limits

- **WHEN** a generated diagram, table or bundle exceeds the declared structural or content bound
- **THEN** validation identifies the affected incomplete asset and refuses an apparently complete rendering
- **AND** silent truncation cannot make it reviewed or satisfy its reading obligation

#### Scenario: Every narrative unit stays presentation in every form

- **WHEN** a bundle containing sections, blocks, glossary, tables, diagrams, bands, review and drift states is rendered, embedded, exported and queried
- **THEN** each narrative-model unit retains presentation-artifact/non-citable metadata and every applicable role, band authority, curated/computed, editorial/adoption, proposal, review, target-change and epistemic distinction in each form
- **AND** machine narrative blocks have a distinguishing type from kernel Claim entities, and plain-text output retains the distinctions without relying on visual position

#### Scenario: Presentation cannot enter truth or warrant inputs

- **WHEN** a caller offers a generated or curated narrative unit as evidence, snapshot source input, implementation mapping or work warrant
- **THEN** the owning input boundary rejects that presentation unit for each offered authority role
- **AND** deleting the presentation and rebuilding its projection leaves underlying truth, status, work and consent records and answers unchanged

#### Scenario: Ambiguous support is split at the claim block

- **WHEN** a multi-sentence block has sufficient source material but a reader cannot recover which of its anchors supports each claim
- **THEN** fidelity validation identifies ambiguous attribution and requires a split or explicit recoverable claim-to-support mapping
- **AND** block-level citation is permitted without a citation after every sentence, but unrelated anchors and an unattributable many-anchor block cannot pass

#### Scenario: Typed source relations are not flattened for layout

- **WHEN** admitted source relations include declared dependency, operative depends_on, implementation mapping and multiple placed_in relationships
- **THEN** adaptation and presentation preserve each owning type, direction, evaluation and nonfunctional placement cardinality
- **AND** explanatory curated edges cannot mint kernel relations or replace unsupported conversion with a guessed unique placement

#### Scenario: Computed output has no enabled production renderer

- **WHEN** a first-version request asks for a computed visual reference
- **THEN** its disposition is unresolved with the unsupported renderer identified, and required computed output keeps readiness unmet
- **AND** curated diagrams or screenshots are not counted as the computed result, while supported independent assets retain their actual state

Form: invariant.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: RFC7-20
  doctrine: [VIS-1, VIS-2, VIS-6]
  contracts: [RFC7-2, RFC7-3, RFC7-9, RFC7-10, RFC7-20, RFC7-28, RFC7-33, RFC7-34, RFC1-25, RFC4-26]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Understandable reading depths

The presentation SHALL open with a clear core introduction and provide a coherent concise reading path through the project argument to deeper capability and exact-source material. It SHALL provide contents, terminology and relationship assets where supported and useful. Required stopping depths SHALL independently answer: opening—purpose and central thesis; concise account—motives, promises and boundaries; deeper account—capability relationships, material design choices and exact-source access. Each depth SHALL retain a true coarser account; content available only at a deeper level SHALL NOT discharge an earlier level's obligation. Supported gaps remain explicit at the depth they affect. Every requested asset SHALL have an explicit produced, reasoned-omission or unresolved disposition. An asset required by the request, reading obligation or frozen acceptance criteria SHALL remain unmet when support, permission or renderer capability is unavailable. Optional omission SHALL NOT excuse an unmet reading-depth obligation; silent omission, decorative approximation or an unapproved textual substitute SHALL NOT discharge a required asset. The primary narrative SHALL use RFC7-13's default altitude order unless the owner rules otherwise; alternative named narratives remain subject to the same per-altitude and exact-leaf obligations. Capability deep dives SHALL preserve RFC7-17's three authority classes and default argument/contract/reality ordering. The argument band SHALL include the motivating principle/decision and related capabilities with their support; the contract band SHALL include accepted contract and declared topology-placement references alongside operative requirements/scenarios; the reality band SHALL retain the four SDR-3 implementation-mapping classes queryably distinct and intent-adoption/amendment/dismissal history, not substitute a commit log. Catalog membership SHALL come from declared capabilities, with drafts unadopted and missing declarations explicit; empty bands SHALL retain an honest absence line.

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

### Requirement: Explicit bounded generation

A generation request SHALL identify positive finite limits for provider calls, input/output volume, charged usage and elapsed time, plus a finite nonnegative repair-cycle limit before dispatch. The run SHALL expose its current stage, completed artifacts, remaining limits and reasons for refusal/failure. A provider response alone SHALL NOT establish completion.

ID: REQ-polaris-generation-005
Source: RFC7-20; governing warrants below.
Scope: v1-mandatory


#### Scenario: Inspectable successful run

- **WHEN** a bounded run produces a candidate asset
- **THEN** its record identifies source understanding, narrative construction, fidelity review, rendered design review and any repairs with their actual inputs and outputs
- **AND** the owner can distinguish work completed from reviews still required

#### Scenario: Invalid output or exhausted budget

- **WHEN** a stage returns malformed output, fails, times out or reaches an admitted limit
- **THEN** the run stops further disallowed work, records actual usage and exposes the incomplete stage
- **AND** the candidate does not become ready or replace a valid presentation

Form: event-response.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: RFC7-20
  doctrine: [VIS-1, VIS-2, SEC-2]
  contracts: [RFC7-20, RFC7-22, RFC7-24]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Independent review and repair

A draft SHALL become ready for owner review only after independent fidelity and rendered-design reviews confirm the frozen bundle and all blocking findings have dispositions verified against that same bundle. Fidelity review SHALL use an independently prepared, frozen inventory of material source claims, qualifications, conflicts and trade-offs, covering the entire admitted source population. The fidelity reviewer SHALL verify inventory accuracy and completeness against the owning admitted sources rather than trusting preparation output. It SHALL record both inventory-to-draft coverage and draft-to-source support, including justified omissions; unresolved material omissions SHALL prevent readiness. The candidate-authoring stage SHALL NOT define or narrow its own review denominator. The bounded workflow SHALL prepare or validate the independent inventory and questions from admitted sources, accounting for those calls in its run budget; it SHALL NOT require the owner to hand-author project-specific editorial preparation before starting. Reviewers SHALL receive the artifact, governing references and acceptance criteria without the authoring conversation. A revision SHALL retire dependent review evidence. Every candidate that changes the reading order, section set, anchor targets or manifesto/thesis, and every target-changed block, SHALL receive the fresh-reader review required by RFC7-25 before becoming ready; failed review remains recorded and visible. The generator SHALL not classify its own wording change as immaterial.

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

### Requirement: Cancellation and interruption

The owner SHALL be able to request cancellation. Cancellation accepted before authored-write commitment SHALL prevent new dispatches and readiness/adoption, attempt supported in-flight cancellation, and report which operations actually stopped. A request after that commitment SHALL report too late and the actual finalization state; it SHALL NOT claim an already committed write was cancelled or reversed. Late provider results and charges SHALL be accounted without resuming the cancelled workflow. Dispatch admission SHALL mean the durable reserved-to-dispatching transition, serialized against accepted cancellation in execution control; reservation alone SHALL NOT admit an effect. An attempt admitted earlier SHALL be reported as potentially in flight, including uncertainty before physical transmission, never falsely acknowledged as stopped.

ID: REQ-polaris-generation-007
Source: VIS-2; governing warrants below.
Scope: v1-mandatory


#### Scenario: Cancel during a provider call

- **WHEN** the owner cancels while a provider request is in flight
- **THEN** no subsequent stage is dispatched and the run records the actual cancellation outcome
- **AND** a late response cannot advance the cancelled run to ready

#### Scenario: Process interrupted

- **WHEN** the runner disappears after a completed stage
- **THEN** the next inspection shows the last durably recorded progress and the incomplete execution state
- **AND** missing evidence is not interpreted as completion

#### Scenario: Cancellation wins before dispatch admission

- **WHEN** cancellation is accepted after budget reservation but before the reserved-to-dispatching transition
- **THEN** the transition is refused and the provider adapter receives no send request
- **AND** reservation alone cannot be presented as an already admitted operation

#### Scenario: Admission wins before cancellation

- **WHEN** an attempt acquires dispatch admission before cancellation is accepted and transmission has not been confirmed
- **THEN** the attempt is reported as potentially in flight, supported cancellation is attempted, and later admissions are refused
- **AND** no response or missing response is rewritten as proof that the admitted effect stopped

Form: lifecycle transition.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-2, SEC-2]
  contracts: [RFC7-22, RFC7-24]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Safe resume and duplicate requests

A resumed run SHALL reuse only verified checkpoints whose input identity, permissions, policy and artifact digests remain applicable. The authoritative lifecycle adapter SHALL durably and atomically reserve budget and grant exclusive dispatch ownership before each provider effect, checking current run disposition and deadline. Duplicate starts for the same request identity SHALL not duplicate provider effects or spend the same allowance. An uncertain attempt SHALL continue to reserve its maximum charge until trusted effect-and-usage resolution; missing receipts or expired leases SHALL not permit redispatch. When prior dispatch completion is uncertain, the run SHALL expose that uncertainty and require an explicit bounded retry decision rather than silently redispatching. Each dispatch admission SHALL obtain a new identified scheduler observation and validate the materialization join and execution warrant at that admission evaluation. Missing, withdrawn, superseded, ineligible, unavailable, future-dated or expired required state SHALL refuse admission; cached permissive state SHALL NOT substitute. The local transaction SHALL bind the observation within its declared freshness bound while atomically checking execution-control revision, disposition, budget and deadline. This SHALL establish eligibility at that evaluation, not unchanged scheduler state through physical transmission or provider completion. Transitions to ready and authored-write commitment SHALL also obtain a new scheduler observation under the same eligibility and freshness check. Subsequently observed withdrawal or supersession SHALL block further admissions, readiness and not-yet-committed finalization, attempt supported cancellation and preserve actual outcomes and usage; an existing authored-write commitment SHALL retain its separately defined ordering semantics. Provider/content consent SHALL remain a separate effect-boundary predicate.

ID: REQ-polaris-generation-008
Source: VIS-2; governing warrants below.
Scope: v1-mandatory


#### Scenario: Resume valid work

- **WHEN** a stopped run has valid completed checkpoints and effective permissions
- **THEN** resume reuses those stages and records which work was reused and newly dispatched
- **AND** the remaining original budget is respected

#### Scenario: Duplicate or ambiguous dispatch

- **WHEN** a duplicate start arrives or a crash leaves dispatch completion uncertain
- **THEN** the system reuses or rejects the request explicitly without an unrecorded duplicate effect
- **AND** different run identities cannot overwrite each other's artifacts

#### Scenario: Concurrent starts share one remaining allowance

- **WHEN** two workers attempt the same stage or compete for the run's last admissible provider allowance
- **THEN** only a successful atomic lifecycle reservation and exclusive dispatch claim can contact the provider
- **AND** the other worker receives the existing attempt or a conflict without spending that allowance

#### Scenario: Crash after dispatch claim but before receipt

- **WHEN** a process disappears after the durable dispatch claim and no trustworthy receipt establishes the effect
- **THEN** the attempt remains uncertain and its maximum charge remains reserved
- **AND** recovery neither redispatches it nor treats its missing response as zero usage

#### Scenario: Scheduler unavailable at admission

- **WHEN** a fresh scheduler read fails while an older observation shows the work eligible
- **THEN** dispatch is refused with the source failure visible and the provider receives no send request
- **AND** the old observation remains historical or visibly stale evidence, never current execution authority

#### Scenario: External withdrawal races with admitted transmission

- **WHEN** the scheduler withdraws work after the captured admission observation and the provider attempt has acquired dispatch admission
- **THEN** the run reports eligibility only at that observation and preserves any resulting effect and usage
- **AND** the next observation of withdrawal stops further admissions, readiness and not-yet-committed finalization without claiming the earlier effect was prevented

#### Scenario: Reservation outlives its scheduler observation

- **WHEN** a reserved attempt resumes or its admission observation exceeds the declared freshness bound
- **THEN** dispatch needs a new scheduler observation and current authority evaluation
- **AND** an old permissive capture or remaining budget cannot authorize the send

Form: lifecycle transition.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-2, SEC-2]
  contracts: [RFC4-5, RFC4-15, RFC7-20, RFC7-22, RFC7-24, RFC8-7, RFC8-9, RFC8-10]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Source drift and regeneration

A source or generation-policy change SHALL create a distinct generation context and invalidate affected readiness/adoption applicability. Regeneration SHALL produce a separately reviewable candidate through the same supported workflow without editing renderer code or compiled passage offsets. Previously curated prose SHALL remain attributable and recoverable, with drift visible. Broken anchors SHALL follow RFC7-11's claim reason and distinct navigation outcome; resolving target changes SHALL follow RFC7-11(a) without inventing an epistemic reason. A new evaluation identity alone SHALL NOT count as target drift. Captured authorship state SHALL remain immutable and only the applicable authoring act that rereads the target may clear the drift marker.

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

### Requirement: Human authorship provenance

A generated bundle SHALL remain editorial-draft until the existing effective-owner-act predicate under RFC3-16 and RFC7-21 admits an attributed per-block authorship act for its exact subject. A stored human label, review result, button press alone or whole-document signature without the required attestation SHALL NOT substitute. Curated presentation SHALL remain non-authoritative and non-citable.

ID: REQ-polaris-generation-010
Source: RFC7-21; governing warrants below.
Scope: v1-mandatory


#### Scenario: Valid act

- **WHEN** an effective owner act attests the exact eligible blocks
- **THEN** only those blocks gain curated status with the act's exact provenance state visible
- **AND** neither underlying intent adoption nor release authority is implied

#### Scenario: Invalid or partial act

- **WHEN** an act is missing, invalid, bound to other bytes or lacks required block attestation
- **THEN** unattested blocks remain editorial-draft and the invalidity is visible
- **AND** no automatic fallback manufactures human authorship

#### Scenario: Every authoring path has the same per-claim gate

- **WHEN** content is introduced by direct prose editing, structural editing, model generation, agent repair or import into an existing or additional narrative
- **THEN** each path applies the same claim-role/support validation and exact per-block effective authorship predicate before curated status
- **AND** a direct edit or repair cannot bypass the gate, change protected historical bytes or treat a successful editor save as an owner act

Form: lifecycle transition.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: RFC7-21
  doctrine: [VIS-4, VIS-6]
  contracts: [RFC3-16, RFC7-2, RFC7-4, RFC7-20, RFC7-21, RFC7-23]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Rejection and retention

A rejected draft SHALL leave the intent surface entirely in accordance with RFC7-22, with rejection recorded on its authoritative work item. Retention SHALL distinguish draft projections and expirable raw detail from RFC8-26's preservation set: structured run summaries, work warrants, decisions, materialization mappings, known cost/token totals, evidence identities and hashes, and reconciliation outcomes SHALL survive every compaction. Draft/raw-detail cleanup SHALL NOT delete that set or authored composition. Compaction SHALL produce an identified, durable record. A claim whose only substantiation expired SHALL render Unknown citing the compaction or retention event, never absence or a confident restatement from its summary. Preserved summaries SHALL retain their recorded tiers. Missing artifacts SHALL render broken references and affect tier through the next identified evaluation, without rewriting immutable historical conclusions or upgrading tiers. Provider expiry SHALL NOT erase retained confirmation captures; later authorized re-confirmation SHALL produce a new observation and evaluation. A preserved hash without a required capture or another satisfied RFC4-13 route SHALL be visibly capped at report-fact, never gate-backed. No records found SHALL remain visually and queryably distinguishable from nothing happened. Retention, deletion and export SHALL expose what is affected, preserve attribution and obey existing consent and artifact-retention boundaries. They SHALL NOT silently overwrite authored content, expose retained history as an adoptable rejected draft, or authorize additional source reads, provider calls or remote publication.

ID: REQ-polaris-generation-011
Source: RFC7-22; governing warrants below.
Scope: v1-mandatory


#### Scenario: Reject a draft

- **WHEN** the owner rejects a candidate
- **THEN** it is removed from Polaris reading, search and adoption surfaces and its lifecycle records the rejection
- **AND** retained execution evidence cannot present it as an adoptable draft

#### Scenario: Export or cleanup

- **WHEN** an operator requests export or retention cleanup
- **THEN** only the authorized destination/content and declared retention operation are affected
- **AND** the operation preserves attribution and does not silently replace an authored artifact

#### Scenario: Compact a rejected run

- **WHEN** declared policy expires a rejected draft and its raw transcript
- **THEN** the draft stays absent from reading, search and adoption surfaces while each applicable preservation-set record survives with an identified durable compaction record
- **AND** known usage totals survive and retained history neither reconstructs adoptable prose nor changes unknown usage into zero

#### Scenario: Only substantiation expires

- **WHEN** permitted retention removes a claim's only substantiating material
- **THEN** the claim renders Unknown citing that event and its missing reference renders broken under the evaluation rules
- **AND** a preserved summary neither substantiates the lost detail nor changes its recorded tier or an immutable historical evaluation
- **AND** human and machine views distinguish missing records from no activity

#### Scenario: Provider history expires after capture

- **WHEN** an external provider expires records whose confirmation capture remains in the identified snapshot
- **THEN** the historical evaluation retains its recorded tier and retention triggers no additional external read
- **AND** later authorized re-confirmation produces a new observation and evaluation rather than changing that stored conclusion

#### Scenario: Only an evidence hash survives

- **WHEN** an evaluation has a preserved hash but no required confirmation capture and no other satisfied RFC4-13 route
- **THEN** the artifact cannot establish gate-backed evidence and its report-fact cap is visible
- **AND** claims whose only substantiation is gone remain Unknown rather than gaining support from the hash

Form: lifecycle transition.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: RFC7-22
  doctrine: [VIS-6, SEC-2, SEC-4, SEC-5]
  contracts: [RFC4-13, RFC7-7, RFC7-20, RFC7-22, RFC7-24, RFC8-6, RFC8-26, RFC8-27]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Safe accessible presentation

Generated pages SHALL render untrusted source and provider content inertly, make distinctions recoverable by keyboard and assistive technology, maintain readable contrast and fit on desktop/mobile, and keep navigation and lengthy technical reference material from obstructing the default account. Exact normative leaves SHALL retain their owning identity and verbatim text; generated prose SHALL NOT substitute for the owning artifact's text. Diagram text equivalents SHALL preserve elements, relationships, anchors, legends and markings. Tables, contents, glossary routes and visual-reference controls SHALL retain their semantics and required paths in machine output and keyboard/nonvisual use. Contents SHALL derive destinations from actual reading structure; contextual definitions and glossary links SHALL refer to the same supported term entry.

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

### Requirement: Shared drafting lifecycle

Trajectory SHALL own drafting-queue presentation relative to Polaris, not relative to the work scheduler. Polaris SHALL expose contextual draft review and authorship and read queue state without maintaining a competing queue. After materialization, current work lifecycle SHALL be read from the scheduler at the answering evaluation; neither surface nor the generator SHALL maintain a second editable copy of scheduler-owned fields or append lifecycle changes to the immutable materialization record. Offered scheduler mutations SHALL use a synchronous attributed typed-adapter operation followed by a re-read, never local mutation with later synchronization. Generator stage progress, budget reservations, dispatch claims and finalization receipts SHALL be explicitly typed execution-control records, distinct from scheduler lifecycle, editorial state and the intent-reconciliation chain. These records SHALL NOT mint kernel states, stand in for scheduler completion or imply satisfied intent. These control records SHALL be subordinate metadata of the existing Execution run and Execution Record identities, not new kernel entities. The owning schemas, fields, adapters and retention rules SHALL be declared and reviewed before implementation. Human and machine views SHALL agree on record identity, governing source, evaluation and supported state; captured historical transitions SHALL remain immutable observations, never current scheduler state. Each enumerated scheduler work item SHALL be checked against its immutable materialization join: proposal identity, work-item identity set and pinned warranted intent revision, with materializing evaluation rendered alongside. A missing record SHALL produce the unfilterable orphaned-work Contradiction under RFC8-8, route only to owner adjudication, and render the affected conclusion Unknown with reason contradicted-pending-adjudication and suspended tier. It SHALL NOT be silently backfilled or treated as Unknown-provenance. Subsequent re-materialization SHALL cite and supersede the orphan finding in the new record. Reservation and dispatch SHALL independently require this valid join and warranted execution authority; skipping work enumeration SHALL NOT bypass that admission gate. Wherever normalized work state is rendered, queried or handed off, its separately identified intent-reconciliation chain state SHALL accompany it under RFC8-28; execution progress SHALL NOT supply that verdict.

ID: REQ-polaris-generation-013
Source: RFC7-24; governing warrants below.
Scope: v1-mandatory


#### Scenario: Observe the same run

- **WHEN** the owner inspects a run in Polaris and Trajectory and a machine queries it
- **THEN** all views identify the same lifecycle record and supported state
- **AND** a stale projection is visibly stale rather than a competing truth

#### Scenario: Transition race

- **WHEN** cancellation, rejection and a late completion race
- **THEN** the resolved authoritative lifecycle is reflected consistently and no draft with accepted rejection/cancellation becomes adoptable
- **AND** the event record explains the applied transition

#### Scenario: Scheduler changes after materialization

- **WHEN** the scheduler withdraws or supersedes materialized drafting work while a cached generator projection still shows it running
- **THEN** the next answering evaluation reads and renders the scheduler lifecycle and exposes stale projection evidence without rewriting the materialization record
- **AND** any captured prior transition is identified as historical evidence rather than a competing current lifecycle

#### Scenario: Work has no materialization join

- **WHEN** an enumerated scheduler work item has no materialization record
- **THEN** it produces an unfilterable orphaned-work Contradiction with owner adjudication as its only exit and suspends the affected conclusion as Unknown
- **AND** neither a generator request nor a scheduler success response is used to fabricate the missing record

#### Scenario: Direct dispatch bypasses surface enumeration

- **WHEN** a generation request attempts reservation without a valid materialization join or warranted execution authority
- **THEN** admission refuses reservation and provider dispatch even if no surface has enumerated the work item
- **AND** a missing materialization record follows the orphan-finding and owner-adjudication path rather than being synthesized from the request

#### Scenario: Generation succeeds while intent remains unevaluated

- **WHEN** a generation stage finishes or a delivery acknowledgment is recovered
- **THEN** its execution result is recorded in the matching control record without setting scheduler closure or an intent-reconciliation verdict
- **AND** human and machine views distinguish that result from editorial readiness and satisfied intent

Form: state projection/query.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: RFC7-24
  doctrine: [VIS-2, VIS-6]
  contracts: [RFC1-29, RFC4-5, RFC4-15, RFC7-22, RFC7-23, RFC7-24, RFC8-2, RFC8-3, RFC8-4, RFC8-7, RFC8-8, RFC8-9, RFC8-10, RFC8-28]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Reusable product validation

Generator completion SHALL require independent evidence from two substantively different, separately admitted real project domains using one unchanged supported generation path, including fresh generation and source-change regeneration. Independent cold readers SHALL record their understanding and navigation, and design reviewers SHALL assess the actual rendered argument and experience. Before candidate narrative drafting in the product evaluation, independent evaluators SHALL freeze project-specific comprehension questions, source-backed expected answers and blocking design/comprehension criteria directly from the admitted sources, outside the generator under test. The run's own inventory, questions or review verdict SHALL NOT serve as the sole completion oracle. Unresolved confident factual errors, inability to explain a supported central thesis or capability relationships, inaccessible required reading paths, and blocking visual findings SHALL prevent completion. Repairs SHALL require dispositions and a fresh passing evaluation of the changed output. At least one real evaluation SHALL require synthesis across verbose or scattered sources; replaying an already curated manifesto is insufficient. Synthetic tests and curated golden pages SHALL remain explicitly limited evidence.

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

### Requirement: Presentation profile admission

When a project lacks its required presentation profile, Polaris SHALL draft a default for owner sign-off and render the profile and dependent narrative unadopted-draft. It SHALL not presume profile adoption from source or provider admission. Permanent profile decline SHALL produce an explicitly reduced presentation. A project SHALL have at most one primary narrative, and a thin or undeclared project SHALL retain an honest front door rather than an absent one.

ID: REQ-polaris-generation-015
Source: RFC7-5; governing warrants below.
Scope: v1-mandatory

#### Scenario: Missing profile

- **WHEN** an admitted project has no adopted presentation profile
- **THEN** Polaris exposes the candidate profile and dependent presentation as unadopted-draft with the owner sign-off route
- **AND** source/provider permission does not change that state

#### Scenario: Declined or thin project

- **WHEN** the owner permanently declines the profile or the project has little declared intent
- **THEN** Polaris renders the explicitly reduced or thin primary presentation with its limitations
- **AND** it does not invent project facts or a second primary narrative

#### Scenario: Profile membership and human-readable authored representation

- **WHEN** a project has primary and additional narratives with sections, claim blocks and anchors
- **THEN** each entity has explicit presentation-profile membership and authored composition is retained in an attributed human-readable form governed by its owning write/version rules
- **AND** additional narratives obey the same claim, authorship, anchor and export rules and never become a competing primary

#### Scenario: Citation graph is rebuildable and personal state is local

- **WHEN** a narrative citation projection is deleted and rebuilt while bookmarks or reading position change
- **THEN** the rebuilt queryable citation graph has the same owning entity and anchor relationships, and personal state stays local outside authored narrative and governed truth
- **AND** labels, density or reading position do not mint entity identity, change source claims or require an authored-content write

Form: lifecycle transition.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: RFC7-5
  doctrine: [VIS-2, VIS-3, VIS-4]
  contracts: [RFC1-7, RFC7-5, RFC7-6, RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Authored artifact ownership and writes

Authored narrative-model changes SHALL be versioned, attributed to Syzygy, atomic and individually revertible under the applicable per-repository write consent. Authored narrative SHALL reside in the intent home and remain with the repository at offboarding, never in a cache. Queue state SHALL remain in its governing work home, with each act recorded once. A conflicting existing artifact SHALL be surfaced without silent overwrite. Authored-write commitment SHALL be serialized against cancellation/rejection, and each finalization identity SHALL apply at most once. Atomic application SHALL include a durable receipt; loss of the work acknowledgment SHALL be recovered from that receipt without repeating the act/write or overwriting subsequent human edits. Commitment alone SHALL not be rendered as successful application.

ID: REQ-polaris-generation-016
Source: RFC7-7; governing warrants below.
Scope: v1-mandatory

#### Scenario: Conflict or interrupted write

- **WHEN** a proposed authored change encounters changed destination bytes or interruption before atomic completion
- **THEN** the previous artifact remains valid and the conflict or incomplete effect is exposed
- **AND** retry cannot silently overwrite the intervening author work

#### Scenario: Reversal and offboarding

- **WHEN** an owner reverses one authored change or offboards the project
- **THEN** the individual change can be reversed with attribution and authored narrative remains repository-owned after offboarding
- **AND** discarding generated caches cannot delete authored composition

#### Scenario: Cancellation races with authored-write commitment

- **WHEN** cancellation/rejection and finalization compete for the same eligible draft
- **THEN** the authoritative conditional commitment determines the winner: accepted cancellation prevents the write, while an earlier commitment makes the cancellation request too late
- **AND** the visible state distinguishes commitment, actual application and any refused or uncertain effect

#### Scenario: Authored write succeeds before acknowledgment is lost

- **WHEN** an atomic authored write succeeds but its work acknowledgment crashes, including a subsequent human edit before recovery
- **THEN** recovery uses the durable application receipt to confirm the existing act and written version without another write
- **AND** later human edits are preserved; absence of a receipt leaves uncertainty rather than permission for blind replay

Form: lifecycle transition.

- **Case:** Run the named scenarios using controlled input snapshots, provider outcomes and lifecycle events.
- **Observable:** Inspect human/machine state, recorded artifacts and independently captured dispatch/write effects.
- **Oracle:** Compare each scenario's observations with its explicit required outcomes; missing evidence is unproven. Where a requirement calls for human review, verify the bound review record and verdict, not an automated claim of understanding.
- **Oracle independence:** Expected outcomes, source facts and injected events are defined outside the generator under test.
- **Falsifier:** A prohibited effect occurs, a required disclosure is absent, or a state advances without its required evidence.

```yaml
warrants:
  primary: RFC7-7
  doctrine: [VIS-5, VIS-6, SEC-4]
  contracts: [RFC3-18, RFC3-20, RFC7-5, RFC7-7, RFC7-8, RFC7-24]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Registered adapter boundaries

Every generator observer or adapter SHALL resolve a per-project registry entry with RFC4-2's declared role/implementation identities, versions, inputs and snapshot mapping, output classes and identity schemes, per-output determinism class, failure mapping and exact authority/write boundary before its output is admitted. External authorities SHALL be accessed through their single registered adapter per project, never a competing direct route. New effects SHALL require the corresponding effective registration and effect authority; internal services SHALL NOT acquire external authority merely by being named interfaces. Registry adoption SHALL be evaluated under RFC3-16, never trusted from an entry's own label. Every resulting fact SHALL carry the effective registry-act reference and exact state-(1) or state-(2) provenance; state-(1) SHALL remain visibly uncorrelated and successful admission SHALL NOT upgrade it. Emissions SHALL carry source identity, capture instant, capturing observer identity/version, scope and relocation provenance, with source-reported time distinct. Registry, policy and implementation versions SHALL be snapshot inputs. Missing or ineffective registration SHALL leave affected deterministic claims Unknown with source-uncaptured-or-unreachable. Adapter and registry changes SHALL create new snapshots without rewriting historical meanings; unsupported older-version fields SHALL remain Unknown, undefined claimed contract versions SHALL be inadmissible, and cross-version joins SHALL use only identically declared identity schemes. Substitution SHALL preserve role identity and resolving historical implementation identities/aliases. Internal failures SHALL map to RFC2-23's applicable degradation and rendering obligations, with affected claim reasons and resolution routes; unrelated execution/editorial failures SHALL NOT be forced into a fabricated degradation state.

ID: REQ-polaris-generation-017
Source: RFC4-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Self-declared adapter approval

- **WHEN** a route supplies a registry entry with an adopted label but no effective owner act
- **THEN** its output cannot establish a deterministic fact and new effects using that unregistered authority are refused
- **AND** affected claims carry the prescribed Unknown reason rather than trusting the route's label

#### Scenario: Adapter substitution and version skew

- **WHEN** an implementation is replaced or a declared contract version differs from the consumer's version
- **THEN** new snapshot inputs identify the change while historical records keep their original identities, versions and aliases
- **AND** missing older-version fields remain Unknown, undefined versions are inadmissible and incompatible identity schemes do not join

#### Scenario: Capture fails after a successful observation

- **WHEN** the registered observer fails to capture required current input
- **THEN** last-good evidence is visibly stale or broken and affected new claims are Unknown with source-uncaptured-or-unreachable and its repair route
- **AND** neither a full-scope aggregate nor a provider dispatch treats the old permissive capture as current authority

#### Scenario: Interface tries to bypass its adapter

- **WHEN** a generation stage requests a direct source, scheduler or provider operation outside its registered route and effective write surface
- **THEN** the operation is refused without performing the external effect
- **AND** naming an internal service as an adapter does not confer that authority

#### Scenario: Effective registry act admits a fact

- **WHEN** an otherwise admissible adapter entry is supported by an effective state-(1) or state-(2) owner act
- **THEN** each resulting fact carries that act reference and exact provenance state in human and machine output
- **AND** state-(1) stays visibly uncorrelated rather than becoming verified merely because admission succeeded

Form: invariant.

- **Case:** Vary each declaration field, effective registry act, claimed version and external route independently; capture emitted identities and attempted effects.
- **Observable:** Registry evaluation, snapshot closure, emitted provenance/degradation and external-adapter calls.
- **Oracle:** The frozen registry declarations, governing field obligations and controlled source/act inputs, independent of the generator's approval assertions.
- **Falsifier:** An unregistered effect occurs, a missing declaration is silently defaulted, historical meaning changes, or a failed capture yields current positive authority.

```yaml
warrants:
  primary: RFC4-2
  doctrine: [VIS-2, VIS-5, VIS-6, VIS-7, SEC-2, SEC-4, SEC-5]
  contracts: [RFC2-1, RFC2-23, RFC2-24, RFC3-16, RFC4-1, RFC4-2, RFC4-3, RFC4-4, RFC4-5, RFC4-7, RFC4-8, RFC4-9]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Complete execution history

Each execution run SHALL retain one immutable, identified, integrity-verifiable Execution Record in its governing work home as execution-plane Evidence, never proof of desired-state satisfaction. It SHALL carry every RFC4-19 required field group and every expected-where-available group with an explicit Unknown reason when unavailable, preserving each group's semantics. A stage artifact or provider success response SHALL NOT substitute for that envelope. Run identity origins SHALL be queryably distinct; derived identity collisions SHALL render reduced-fidelity with indistinguishable-runs and Unknown run count rather than silently collapse dispatches. Missing terminal reports SHALL use unknown-terminal with reason; unattributable runs SHALL remain visible as execution noise rather than being dropped. Missing warrant/profile evidence SHALL NOT erase observed history or authorize a new dispatch. Optional worktree/prose and fine-grained heartbeat, phase, span or streaming enrichment SHALL NOT be required for envelope admissibility or substituted for required fields. Prompt/transcript bodies SHALL NOT enter the envelope; optional prose SHALL pass the observing project's screening policy. Reported profile violations SHALL terminate the run and cap outputs at report-fact; missing violation evidence SHALL remain Unknown. Captured usage/timing SHALL remain distinguishable from rate-table-derived Inferred cost, with derivation and rate version retained. Partial totals SHALL disclose known and total populations, absent quantities SHALL NOT count as zero, and independent measures SHALL NOT be merged into an effort score. Execution instants SHALL remain distinct from evaluation time.

ID: REQ-polaris-generation-018
Source: RFC4-19; governing warrants below.
Scope: v1-mandatory

#### Scenario: Interrupted run lacks optional evidence

- **WHEN** a run has no terminal report, final usage receipt, branch, PR or fine-grained telemetry
- **THEN** its envelope preserves the required representations including unknown-terminal and explicit reasons for unavailable expected fields
- **AND** optional telemetry absence does not reject or degrade that envelope, and missing usage is not zero

#### Scenario: Historical run lacks dispatch authority

- **WHEN** captured execution has an absent warrant or unrecoverable profile identity
- **THEN** history remains visible with its Unknown qualifications and applicable evidence-tier restrictions
- **AND** historical admissibility cannot authorize a new generator dispatch

#### Scenario: Derived run identities collide

- **WHEN** two actual dispatches cannot be distinguished by the adapter's durable identity inputs
- **THEN** the affected records disclose reduced-fidelity with indistinguishable-runs and Unknown run count
- **AND** a scheduler mutation trail cannot silently supply the missing distinction

#### Scenario: Usage is only partly known

- **WHEN** captured run records contain known and unknown usage and cost is derived from a rate table
- **THEN** aggregates disclose their known and total populations and derived cost is Inferred with the rate version and derivation
- **AND** missing quantities remain Unknown and separate measures do not become an effort score

#### Scenario: Profile violation or unscreened prose

- **WHEN** a run reports a profile violation or an envelope includes prompt/transcript bodies or unscreened prose
- **THEN** the violating run is terminated with outputs capped at report-fact, and prohibited prose is excluded under the applicable screening policy
- **AND** an absent violation report is never presented as evidence of a clean run

Form: invariant.

- **Case:** Supply complete, partially known, unattributable, interrupted and identity-colliding source records; omit each optional field independently.
- **Observable:** Persisted envelope, source provenance, identity origin, qualified outcomes, evidence tiers and aggregate coverage.
- **Oracle:** RFC4-19's field classification and controlled source receipts; expected values never come from the generated summary or scheduler closure.
- **Falsifier:** A required field is absent, an unavailable expected value is invented, an optional field blocks admissibility, runs silently collapse, or uncertain usage becomes zero.

```yaml
warrants:
  primary: RFC4-19
  doctrine: [VIS-1, VIS-2, VIS-6, SEC-5]
  contracts: [RFC3-19, RFC4-3, RFC4-13, RFC4-18, RFC4-19, RFC4-20, RFC4-21, RFC4-24, RFC8-26, RFC8-27]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Versioned interchange and reference integrity

Generator records SHALL use explicit class/version and typed variants with separate ownership for requests, inventories, controls, generated assets, Execution Records and authored content. Each requested asset SHALL have its own identity, kind, requiredness and purpose, resolving to one produced, omitted or unresolved disposition; produced SHALL reference actual matching assets while unresolved SHALL NOT fabricate output identities or digests. Provider-local handles SHALL NOT mint presentation or kernel identities: a trusted recorded authoring operation SHALL issue opaque presentation identities with retained provenance, without claiming human adoption. Serialized editorial/profile flags SHALL NOT replace effective owner-act evaluation. Canonical anchors SHALL use RFC7-10's target-specific identity, fragment and state representation, distinguishing artifact revision from kernel evaluation and verbatim label/tier/reason. PWB wire conventions SHALL be preserved through explicit compatibility adaptation, never silently promoted into a generic schema or used to widen source admission. Unsupported adaptation SHALL remain explicit without invented identity/state. Required internal references SHALL resolve; definitions SHALL be unique, support references SHALL belong to their claim block, and ownership/containment and stage-input graphs SHALL be acyclic. Supported factual relationship cycles and glossary cross-reference cycles SHALL remain representable. Validation SHALL reject duplicate object keys, unknown interchange versions/kinds, undeclared effect-bearing fields and exceeded structural/content bounds without silent truncation. Shape validity SHALL NOT establish authority, fidelity, readiness or authorship. Newer unsupported plane versions SHALL forbid writes/downgrade and render uninterpretable content Unknown; older content SHALL use declared compatibility paths without mutation on read. Persistent migration SHALL require its own reviewed, attributed, atomic and reversible act, preserving the identities, meanings and citation resolution protected by RFC3-23; OpenSpec content SHALL remain outside that migration authority.

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

### Requirement: Guided start and materialization

The owner SHALL be able to request generation or regeneration from project context without manually assembling governance or scheduler records. The application SHALL resolve the project's declared governance root and authorized work/artifact homes rather than infer write locations from an observed source path, showing missing/conflicting prerequisites explicitly. It SHALL prepare a bounded effect plan from admitted metadata, owner selections and effective presets without provider calls or additional body reads to authorize its own start; persistence SHALL require effective write authority. Existing work SHALL be reused only when its actual warrant, immutable join, current scheduler eligibility, pinned intent and remaining authorized allowance cover the request. Ambiguous, exclusive or undeclared-compatible candidates SHALL NOT be silently selected or merged. Otherwise the application SHALL prepare the execution-intent Proposal and concrete missing-approval context; preparation or a generic Start action SHALL NOT confer approval, and children SHALL inherit approval only when the approving Decision explicitly permits it. Approval SHALL preserve Proposal identity. The application SHALL continue the same identified request once missing authority is effective without re-requesting unchanged approvals. Authorized scheduler creation SHALL use a stable operation identity and exclusive durable creation claim before the effect; duplicates SHALL return the same outcome or a conflict, and uncertain creation SHALL NOT be retried blindly. Only the written immutable materialization record binding Proposal, complete scheduler work-item identity set and pinned warranted intent revision SHALL transition authority to the scheduler. Before that record, the Proposal SHALL remain authoritative and provider dispatch SHALL be refused. An observed scheduler item without its record SHALL produce the unfilterable orphan Contradiction and Unknown/suspended conclusion even during attempted materialization; it SHALL NOT be silently filled in or deleted. Recovery SHALL follow owner adjudication and authorized re-materialization SHALL cite and supersede the finding. Ordinary editorial stages SHALL remain subordinate run metadata rather than requiring a new Proposal/work item for each model call. Existing dispatch, cancellation, retention, review and per-block authorship gates SHALL remain distinct from start-flow success.

ID: REQ-polaris-generation-020
Source: RFC1-29; governing warrants below.
Scope: v1-mandatory

#### Scenario: First request needs approval

- **WHEN** no eligible warranted work covers the owner's requested manifesto
- **THEN** the application prepares the Proposal and bounded effect plan from admitted metadata, names missing approvals and lets the owner complete the existing gates without assembling records manually
- **AND** neither a provider call nor an unconsented persistent write is used to bootstrap that approval

#### Scenario: Exact reusable work remains eligible

- **WHEN** existing work and effective permissions cover the request, its pinned warrant and remaining allowance
- **THEN** the application reuses that validated binding and continues without asking for the same approvals again
- **AND** a matching title, earlier successful run or exhausted/narrower authorization is insufficient

#### Scenario: Concurrent preparation reaches scheduler creation

- **WHEN** two callers continue the same approved request toward materialization
- **THEN** only the holder of the durable creation claim can issue the scheduler operation and the other caller gets the existing outcome or a conflict
- **AND** an uncertain result cannot be replayed merely because a local materialization file is missing

#### Scenario: Scheduler creation succeeds but recording fails

- **WHEN** the scheduler has issued a work item and the immutable materialization record cannot be written
- **THEN** the Proposal remains authoritative, provider dispatch stays refused and observed orphan work is visible as a Contradiction with its Unknown/suspended conclusion
- **AND** recovery neither silently backfills nor deletes the item; authorized re-materialization cites and supersedes the owner-adjudicated finding

#### Scenario: Approval and stage identity remain distinct

- **WHEN** a prepared Proposal is approved and the subsequent run performs several editorial stages
- **THEN** approval preserves Proposal identity, materialization alone transfers lifecycle authority, and stages remain subordinate execution metadata
- **AND** a child Proposal receives no inherited approval unless the approving Decision expressly grants it

Form: lifecycle transition.

- **Case:** Walk first-time, reusable, ambiguous, concurrent and partially failed requests using controlled approval/scheduler outcomes.
- **Observable:** Prepared effects, owner-facing next step, Proposal identity, creation claims, scheduler calls, immutable joins, orphan findings and provider calls.
- **Oracle:** Independently supplied scope/act records and scheduler receipts, never a title match or the preparation stage's approval assertion.
- **Falsifier:** Manual record assembly is required, a missing gate is inferred from Start, duplicate creation occurs, or a provider call precedes valid materialization.

```yaml
warrants:
  primary: RFC1-29
  doctrine: [VIS-2, VIS-3, VIS-4, VIS-5, VIS-6, SEC-2, SEC-4]
  contracts: [RFC1-1, RFC1-27, RFC1-28, RFC1-29, RFC1-30, RFC1-31, RFC3-16, RFC3-19, RFC4-5, RFC4-15, RFC8-7, RFC8-8, RFC8-9, RFC8-10]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Scoped caller admission for generator operations

Every authenticated generator act SHALL bind exactly one explicit principal and authorize its operation/project against that principal's scopes, separately from authentication. The route inventory SHALL include preparation, start/resume/retry, progress/artifact retrieval, cancellation/rejection, ceremonies, authorship/reversal, export and recovery, with data/state-change classification and required gates. Requests SHALL use only the existing browser/machine client classes, classified by valid presented credential, never location, first-party status or header absence. Data-bearing and state-changing browser routes SHALL require an owner-attended session, including on loopback; state-changing requests SHALL additionally require per-session anti-forgery proof, validate present Origin/Sec-Fetch-Site values and reject undeclared Host before application logic. Missing origin headers SHALL neither admit nor condemn and SHALL NOT remove the proof requirement. Sessions SHALL have declared maximum lifetime and next-request owner revocation, without device/IP identity binding; undeclared lifetime SHALL forbid persistence beyond process lifetime. Machine clients SHALL use their own explicitly scoped credentials issued only through an owner-attended trusted ceremony, never an owner's session, another machine credential's issuance or observed content. Unscoped credentials SHALL be invalid; rotation SHALL preserve client identity with only declared overlap, and revocation SHALL support identity or instance at the next request. Server storage SHALL retain only credential verifiers and secret-free governance metadata. Unauthenticated access SHALL be restricted to the existing interface-qualified health/bootstrap set without project data or unattended credential issuance. Fresh installation SHALL remain loopback-only; non-loopback service SHALL require effective exposure authority, declared hosts, TLS and owner-device restriction plus full application authentication. Invalid exposure SHALL refuse serving. A session's expiry SHALL block its subsequent requests without retroactively revoking an independently valid background execution warrant; each subsequent adapter effect SHALL still require current authority.

ID: REQ-polaris-generation-021
Source: RFC5-1; governing warrants below.
Scope: v1-mandatory

#### Scenario: Browser attempts a mutation

- **WHEN** a browser submits start, cancellation, authorship or export on loopback or an enabled non-loopback mode
- **THEN** session, project/operation scope, anti-forgery proof, declared Host and applicable present origin headers are checked before the action
- **AND** host/origin matching alone cannot admit the mutation, while missing Origin alone neither admits nor condemns it

#### Scenario: Machine credential crosses scope or client identity

- **WHEN** a CLI or protocol client requests another project or an operation outside its credential scope
- **THEN** permission is refused without serving protected data or performing the effect
- **AND** co-location, packaging, an owner session or an unscoped credential supplies no bypass

#### Scenario: Credential lifecycle and secret storage

- **WHEN** a machine credential is issued, rotated or revoked
- **THEN** issuance requires the owner-attended ceremony, rotation preserves identity with declared overlap, and revocation applies by identity or instance at the next request
- **AND** the server stores its verifier and secret-free metadata rather than the presentable secret

#### Scenario: Session expires during generation

- **WHEN** the initiating browser session expires or is revoked while an independently authorized run is active
- **THEN** later browser requests require valid admission and the worker cannot reuse that session as a machine credential
- **AND** ongoing effects still evaluate their own current warrant/consent/profile authority rather than inheriting browser admission

#### Scenario: Invalid exposure or anonymous data request

- **WHEN** serving would expose project data without the required exposure act, TLS/device restriction or application authentication
- **THEN** the invalid serving configuration or unauthorized data request is refused
- **AND** health/bootstrap exemptions cannot expose project content or issue unattended credentials

#### Scenario: Machine authentication cannot mint an attended browser session

- **WHEN** an authenticated machine client prepares a pairing request but no fresh owner-attended confirmation exists for its exact origin, scope, nonce and expiry
- **THEN** no browser grant or session is issued, even if the caller supplies an attendance flag or points to a mutable approval file
- **AND** only the trusted supervisor interface may record the attended confirmation; valid one-use redemption still creates a credential-only session with its declared lifetime and revocation behavior

Form: invariant.

- **Case:** Enumerate every generator route and vary client class, principal scope, session/proof, headers, credential lifecycle and exposure independently.
- **Observable:** Admission/permission results, returned data, external effects, credential persistence and next-request behavior.
- **Oracle:** Effective principal/credential/exposure records and route declarations, not network location or the caller's claimed identity.
- **Falsifier:** A protected route bypasses its class discipline, a scope change exposes another project, or a presentable secret is retained by the verifier store.

```yaml
warrants:
  primary: RFC5-1
  doctrine: [VIS-2, SEC-1, SEC-2, SEC-4, SEC-5]
  contracts: [RFC5-1, RFC5-2, RFC5-3, RFC5-4, RFC5-5, RFC5-6, RFC5-7, RFC5-8, RFC5-9, RFC5-10, RFC5-11]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Protected audit and prospective revocation

Every admission, denial, egress, run launch, adapter effect, consent grant/revocation and credential issuance/rotation/revocation SHALL emit durable, identified, integrity-verifiable audit Evidence with principal, credential/session identity, act, subject, exposure mode, actual act instant and outcome, plus source, capture time, scope and provenance. Unknown identity on refusal SHALL be explicit rather than fabricated. The trail SHALL reside outside the governed plane and untrusted actor write reach; work records or a same-user writable directory SHALL NOT substitute. Audit SHALL exclude secrets, credential values and excluded bodies, using permitted digest provenance for offending payloads. Adapter credentials SHALL remain a distinct scoped population, inaccessible to observed code and indexed surfaces; adapter effects SHALL be attributed to Syzygy with initiating-request provenance separately linked. Credentials authenticating to Syzygy SHALL NOT be injectable into observed-project execution. New spending, content-release, generation/adoption and artifact-write effects SHALL require durable audit admission/attempt recording; unavailable recording SHALL refuse those effects without claiming the failed audit write succeeded. Audit outage SHALL NOT delay currently authenticated and authorized local run stops, permitted cancellation of an existing attempt, or denial of further use specified by a valid revocation request. Those stop controls SHALL NOT authorize new generation, export, content release, artifact reversal/deletion or permission grants. Protective enforcement SHALL apply immediately; if required audit durability or owner-act correlation is unavailable, formal revocation/audit SHALL remain explicitly pending rather than falsely verified or assigned a fallback authority state. Pending-event recovery SHALL use trustworthy records, never mutable work files as invented ceremony evidence; missing durability SHALL remain Unknown. A protective hold SHALL NOT silently clear on audit recovery. Existing cancellation/write-commitment ordering and current effect permission SHALL remain controlling, and remote termination SHALL NOT be presumed. Pending audit attempts SHALL NOT prove an external effect occurred. Actual outcomes SHALL be appended under stable identities; lost outcome acknowledgment SHALL require authoritative receipt recovery under current permission without effect replay or fabricated completion. Required missing audit evidence SHALL leave audit-dependent confirmation unmet. Current credentials, consent and applicable profile state SHALL be checked at each attempted act, regardless of earlier scheduler observation or local commitment. Recording revocation SHALL immediately label subsequent dependent renders with withdrawal and trigger a new identified evaluation, without directly rewriting immutable claim values. Before evaluation finishes the prior value SHALL retain the withdrawal label. Revocation identity, instant, principal and dependent consequences SHALL remain visible; restoration SHALL require a fresh grant/record. Already transmitted effects and charges SHALL retain their actual or uncertain outcomes rather than being falsely reversed by revocation.

ID: REQ-polaris-generation-022
Source: RFC5-25; governing warrants below.
Scope: v1-mandatory

#### Scenario: Audit records an adapter effect

- **WHEN** Syzygy performs an authorized provider or artifact-adapter effect initiated by an owner request
- **THEN** protected audit records carry Syzygy's acting identity, linked initiating provenance, actual act/capture instants, subject, mode and outcome
- **AND** neither credential values nor excluded payload bodies enter the trail, and a repository-local work receipt cannot substitute for it

#### Scenario: Audit unavailable before effect

- **WHEN** the protected recorder cannot durably accept the identified admission/attempt record for new spending, content release, generation/adoption or an artifact write
- **THEN** that new effect is refused with audit availability unresolved
- **AND** no pending or failed record is presented as proof that the effect occurred or auditing succeeded

#### Scenario: Outcome acknowledgment is lost after effect

- **WHEN** an external effect may have completed but its audit outcome acknowledgment is missing
- **THEN** recovery uses permitted authoritative receipts to append the outcome idempotently or preserves uncertainty
- **AND** it neither replays the effect nor assumes the absence of an audit outcome means nothing happened

#### Scenario: Revocation arrives after commitment

- **WHEN** applicable consent or credentials are revoked after a local dispatch/write commitment but before the next attempted effect
- **THEN** current boundary checks refuse the effect despite that commitment
- **AND** already transmitted work retains its real outcome and late usage rather than being declared remotely stopped or reversed

#### Scenario: Revocation precedes claim recomputation

- **WHEN** revocation is recorded while a dependent claim still has its prior evaluated value
- **THEN** every later served dependent render carries withdrawal immediately and a new identified evaluation is triggered
- **AND** immutable prior values are not rewritten by the security act, and restoration needs a fresh grant record

#### Scenario: Authorized stop during audit outage

- **WHEN** a currently authenticated and authorized owner requests a local stop, permitted existing-attempt cancellation or revocation while the recorder is unavailable
- **THEN** protective enforcement prevents further admissions/use immediately and attempts only the permitted stop operation without claiming remote termination
- **AND** missing audit durability or owner-act correlation remains pending/Unknown rather than verified, and recovery cannot silently clear the hold or invent trusted ceremony evidence from a work record
- **AND** the stop path confers no new spending, content release, grant or artifact reversal/deletion authority

#### Scenario: Untrusted actor forges or replaces audit evidence

- **WHEN** an excluded actor attempts to append as another principal, forge a receipt, or replace the protected journal, integrity key or recorder executable
- **THEN** the real protected boundary denies the write/operation or detects the invalid receipt before an audit-dependent effect proceeds
- **AND** the verified prior history remains intact; a same-user mock or mutable work record cannot satisfy the protection evidence

#### Scenario: Trusted recovery remains unavailable after restart

- **WHEN** the generator restarts with pending controls and cannot obtain a verified receipt/control position from the protected recorder
- **THEN** new generation, spending, adoption and export remain stopped without effect replay or invented completion
- **AND** the authorized local protective-stop path remains usable while its pending audit/correlation and in-flight outcome uncertainty remain explicit

Form: invariant.

- **Case:** Exercise each audit event class, recorder failure before/after effect, prospective revocation and interim render before evaluation completes.
- **Observable:** Protected audit records/access boundaries, actual effects and receipts, permission results, withdrawal labels and evaluation identities.
- **Oracle:** Controlled principal/act/receipt records and independently observed audit/write/egress effects; missing evidence never supplies a success verdict.
- **Falsifier:** A new spending/content/write effect proceeds after recording refusal, untrusted writers can forge the trail, revocation waits for evaluation, or an uncertain effect is blindly replayed.

```yaml
warrants:
  primary: RFC5-25
  doctrine: [VIS-2, VIS-6, SEC-1, SEC-2, SEC-3, SEC-4, SEC-5]
  contracts: [RFC3-16, RFC5-11, RFC5-24, RFC5-25, RFC5-26]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Fixed manifesto entry and repository discoverability

The governed project's primary narrative SHALL be published at .syzygy/intent/OVERVIEW.md, with the application and formal walkthrough entering that same account. The path SHALL remain a publication location rather than narrative identity or authority; additional named narratives SHALL NOT become a competing default. The entry SHALL retain the applicable claim-support, profile, authorship/version, broken/target-changed anchor, nonvisual and machine-parity obligations, including presentation-artifact/non-citable metadata on every exported, embedded and plain-text rendering. Known absence SHALL surface as a finding and unobservability as Unknown with its owning reason, never a fabricated complete narrative. Publication SHALL still require effective write/authorship authority, predecessor checks and the target artifact's own gates; a fixed path SHALL NOT permit overwriting protected bytes. At each producing evaluation, repository discoverability SHALL assess each declared repository's root README link to the project entry using only admitted reads, never a configurable substitute. Its human/machine domain SHALL be exactly yes, no, not-applicable or Unknown. Declined links SHALL render no without becoming errors; a repository without a governance root SHALL carry not-applicable and its declared basis. Unknown SHALL carry its actual RFC2-24 reason/route, including the unconsented-source-or-provider upstream branch. Missing membership/input or incomplete repository scope SHALL remain explicit. The finding's not-applicable SHALL NOT be used as a navigation outcome or Unknown reason. Syzygy MAY propose the link through the existing Proposal mechanism and SHALL NOT write the root README link.

ID: REQ-polaris-generation-023
Source: RFC7-39; governing warrants below.
Scope: v1-mandatory

#### Scenario: Primary publication and exported reading

- **WHEN** an authorized primary narrative is published and read through the application, export or walkthrough
- **THEN** those forms identify the same primary account at its fixed publication location with its opaque identity and presentation-artifact/non-citable metadata
- **AND** another named narrative cannot silently replace the default or become authority

#### Scenario: Entry absent, unreadable or protected

- **WHEN** the entry is known absent, cannot be observed or cannot lawfully be replaced
- **THEN** the corresponding absence, Unknown or publication conflict is visible without fabricating a complete primary or overwriting protected bytes
- **AND** separate candidate preparation does not imply publication permission

#### Scenario: Repository discoverability has different outcomes

- **WHEN** declared repositories have an existing link, an owner-declined link, no governance root or unavailable/unconsented README input
- **THEN** their findings respectively retain the applicable yes, no, not-applicable or Unknown value with its reason/basis and producing evaluation in both channels
- **AND** no extra read, configurable landing file or automatic README write is used to turn the finding positive

Form: state projection/query.

- **Case:** Exercise the fixed entry and every declared repository's discoverability outcome with controlled observation and write gates.
- **Observable:** Primary identity/location, exported metadata, findings and any attempted README/entry writes.
- **Oracle:** Declared repository membership, admitted root README input, owning narrative identity and effective target gates, independent of the generated prose.
- **Falsifier:** A second default appears, a path becomes authority, a missing entry is hidden, or a finding grants an unconsented read/write.

```yaml
warrants:
  primary: RFC7-39
  doctrine: [VIS-1, VIS-2, VIS-3, VIS-5, VIS-6, VIS-7, SEC-2, SEC-4]
  contracts: [RFC3-5, RFC3-6, RFC7-2, RFC7-3, RFC7-5, RFC7-6, RFC7-7, RFC7-11, RFC7-33, RFC7-34, RFC7-39, RFC7-40]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Owner walkthrough and review-freeze discipline

Internal editorial/design confirmation SHALL remain distinct from owner judgment and SHALL NOT clear an effective review freeze. Reading-order, section-set, anchor-target and manifesto/thesis changes SHALL be material, and target-changed blocks SHALL trigger review without requiring a prose change. An author MAY escalate wording-only changes to material but SHALL NOT declare them immaterial; undeclared wording changes SHALL remain open/contestable until owner classification or contest resolution. Review-failure judgments SHALL live in the governing decisions home and remain visible in human/machine narrative views until lawfully cleared. A clearing/holding verdict SHALL require the effective owner-act predicate with exact state-(1)/(2) provenance, retaining uncorrelated state-(1); an ineffective purported pass SHALL leave the failure visible, preserve the freeze and produce the prescribed Contradiction. Repair drafting SHALL remain permitted under its existing per-claim/write gates. Formal walkthroughs SHALL enter the primary narrative, use a fresh reader without authoring context and keep traversal within Polaris, recording the reader's own account of purpose, promises, a non-goal with its rule text, major capability relationships, verbatim requirement access, an honest Unknown and its presentation, and a chosen fact's epistemic strength and what would strengthen it. Answers SHALL then be checked against owning admitted sources and divergences recorded. A dangling internal link on the path or surface-induced confident falsehood SHALL fail; honest thinness/Unknowns or a reader's own misreading of an honest page SHALL remain owner-judgment territory. Material changes and release milestones SHALL trigger the walkthrough, with at least one nonvisual/keyboard-only path run per release milestone. Each run SHALL have a kernel-recorded execution record in the governing records home naming surface version, evaluation context and traversal mode; its separate owner judgment with verdict, rationale and judging party SHALL reside in decisions, never narrative or a substitute generator Execution Record. Missing execution evidence SHALL leave the test Unknown-never-met; an unattributed, unreasoned or ineffectively authorized judgment SHALL record verdict-unlawful and also leave it Unknown-never-met. A valid judgment SHALL remain a human warrant, never Observed or a numerical score. Preview/internal review SHALL NOT prove a formal walkthrough of different published bytes. Existing PWB walkthrough act-validity behavior and its closed case population SHALL remain unchanged; generator quality/readiness SHALL NOT become extra predicate fields, replace the evaluator or automatically invalidate a lawful PWB judgment.

ID: REQ-polaris-generation-024
Source: RFC7-31; governing warrants below.
Scope: v1-mandatory

#### Scenario: Internal pass awaits an owner verdict

- **WHEN** a repaired candidate passes internal editorial checks and no clearing owner verdict has been submitted
- **THEN** the failure and freeze remain visible with owner review pending, while the candidate may be ready to present for that review
- **AND** the internal pass does not itself mint a Contradiction or clear the freeze

#### Scenario: Purported clearing verdict lacks effective authority

- **WHEN** a clearing pass is submitted as an owner verdict but fails the effective owner-act predicate
- **THEN** the failure and freeze remain visible and the ineffective purported clearing pass produces the prescribed Contradiction
- **AND** repair drafting may continue without claiming the freeze cleared

#### Scenario: Walkthrough tests comprehension and paths

- **WHEN** a fresh reader walks the primary narrative at a material change or release milestone
- **THEN** the record captures the required answers and actual paths, including rule text, exact requirement, Unknown and epistemic-strength explanation, followed by owning-source comparison
- **AND** at least one release-milestone run exercises nonvisual/keyboard traversal rather than only isolated controls

#### Scenario: Honest thinness and misleading output differ

- **WHEN** a page is predominantly Unknown because its project is undeclared, or separately causes a confident false answer or dangling walked link
- **THEN** honest thinness remains judgment territory while the surface-induced falsehood or dangling link fails
- **AND** the generator does not invent facts to satisfy the walkthrough questions

#### Scenario: Judgment or execution record is invalid

- **WHEN** a walkthrough lacks its execution record or its judgment lacks attribution, rationale or an effective owner act
- **THEN** the test remains Unknown-never-met and a defective judgment records verdict-unlawful
- **AND** record location, a numeric score or an internal model verdict cannot manufacture an owner judgment

#### Scenario: Existing PWB judgment remains independently evaluated

- **WHEN** generator quality or readiness changes while an existing PWB judgment is evaluated
- **THEN** the unchanged PWB act-validity predicate uses its own recorded bindings and closed population
- **AND** new quality checks neither supply a missing act nor invalidate a lawful judgment through added predicate fields

#### Scenario: Wording classification and target-only review stay open

- **WHEN** a direct author or agent calls a wording-only edit immaterial, leaves it undeclared, or retains prose while an anchor target changes
- **THEN** self-declared immateriality does not de-escalate review, undeclared wording remains open and contestable, and target-only change triggers fresh review
- **AND** only the applicable owner classification or contest resolution de-escalates; failures remain recorded in the decisions home

#### Scenario: Lawful owner verdict and execution record are distinct

- **WHEN** a complete walkthrough execution and separate lawful owner judgment are recorded, separately under state-(1) and state-(2) provenance
- **THEN** the execution record in its governing records home identifies surface version, evaluation and traversal mode, while the decisions-home judgment identifies verdict, rationale and judging party
- **AND** the effective judgment and any clearing outcome retain their exact provenance, state-(1) stays visibly uncorrelated, and neither judgment is rendered Observed, as a score or as a generator review

#### Scenario: Canonical diagram-set edits are presumptively material

- **WHEN** the canonical diagram set changes without a prose change
- **THEN** the deterministic materiality floor triggers the required review/walkthrough path
- **AND** neither an author's cosmetic label nor unchanged prose clears that obligation or an existing review freeze

Form: invariant.

- **Case:** Exercise materiality triggers, effective/ineffective freeze verdicts, complete/missing walkthrough records and honest/misleading reader outcomes.
- **Observable:** Review records/homes, exact subject bindings, owner-act provenance, visible freeze/test states and actual traversed paths.
- **Oracle:** Independent source-backed questions, controlled act records and the governing walkthrough floors; the generator's own verdict is not the oracle.
- **Falsifier:** An internal pass clears a freeze, a defective judgment passes, honest Unknowns force invented content, or a new quality check rewrites PWB act validity.

```yaml
warrants:
  primary: RFC7-31
  doctrine: [VIS-1, VIS-2, VIS-3, VIS-4, VIS-6, VIS-7]
  contracts: [RFC3-15, RFC3-16, RFC7-2, RFC7-6, RFC7-11, RFC7-25, RFC7-30, RFC7-31, RFC7-32, RFC7-33, RFC7-34, RFC7-23]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Provenance-bound source policy

The generator SHALL resolve the observing project and governance root from owning declarations, never the page label or observed directory. Each consent record SHALL grant exactly one class with subject, scope, granting principal, grant instant and revocation state: observation/write consent per repository, egress consent per project/provider pair with permitted content classes, and execution consent per project for an exact profile version. These permissions SHALL remain separately revocable/renderable and SHALL NOT imply one another. Content classification SHALL use RFC5-14's closed vocabulary and the effective declared policy to derive a composite's inherited highest embedded class from actual content provenance; composition SHALL preserve embedded classifications and origins rather than trust its own output label. The generator SHALL NOT invent a class ordering or a stricter all-embedded-classes consent rule. Indeterminate classification SHALL refuse egress visibly, and derived-composites consent alone SHALL NOT launder unconsented content. Every governed-content network transmission, including side effects and remote backing dependencies, SHALL traverse the single egress check for in-force consent, determinable permitted classification and the separate effective classification-policy and consent acts with exact provenance disclosed. An invalid purported consent act SHALL block transmission and produce the prescribed Contradiction, without treating mere absence as a forged act. Before every ingest into any store/surface/endpoint, content SHALL be screened under the observing project's secret policy with effective exact-digest act and snapshot-bound version, never under an observed source's self-supplied policy. Missing/invalid policy authority SHALL block ingestion; unclassifiable content SHALL be excluded, not indexed. Exclusion provenance SHALL contain only permitted digest/location/policy/redaction metadata, never excluded bytes. Whole-artifact exclusion and unclassifiable-excluded SHALL make every dependent claim Unknown with excluded-content and count; redacted-span SHALL retain permitted surviving evidence at its otherwise-earned tier with disclosed count, making only claims dependent on removed spans Unknown. Redaction branches SHALL remain limited to those the adopted policy permits. Revoked-provider overlays SHALL not be recomputed or admit new kernel challenges; existing admitted challenges SHALL retain their lifecycle until a governing resolution act, without silent resolution or unsuspension. Existing project-specific admission, grammar and policy gates SHALL NOT be widened by generic schema support or fallback.

ID: REQ-polaris-generation-025
Source: RFC5-14; governing warrants below.
Scope: v1-mandatory

#### Scenario: Composite classification cannot be derived

- **WHEN** a prompt includes content whose inherited class cannot be determined under the effective policy and available origin records
- **THEN** egress is refused with the uncertainty visible
- **AND** the composer's derived-composites label, vocabulary order or an invented permission union cannot supply the missing policy decision

#### Scenario: Consent is valid but policy act is not

- **WHEN** consent is in force but the classification or ingest policy lacks its required effective owner act
- **THEN** the corresponding egress or ingestion is blocked rather than using that policy
- **AND** adapter registration or the consent's valid act does not authenticate the separate policy

#### Scenario: Observed source supplies a permissive policy

- **WHEN** an observed repository or provider response includes policy text proposing weaker screening
- **THEN** that text remains input data screened under the observing project's effective policy
- **AND** source labels or directory proximity cannot select a different governing policy

#### Scenario: Partial redaction retains usable support

- **WHEN** an authorized redacted-span result removes one claim's supporting span while another claim is supported by surviving content
- **THEN** only the removed-support claim becomes Unknown with excluded-content, while surviving support retains its otherwise-earned tier and disclosed redaction count
- **AND** a policy permitting only whole-artifact exclusion is not silently changed to partial redaction

#### Scenario: Excluded content reaches a diagnostic boundary

- **WHEN** excluded or unclassifiable material would enter a store, surface, endpoint, provider-result capture or audit diagnostic
- **THEN** the ingest boundary withholds it and retains only permitted digest/location/policy/redaction metadata and counts
- **AND** neither excluded bytes nor a sensitive location string bypasses screening as metadata

#### Scenario: Provider revoked with an existing challenge

- **WHEN** a provider is revoked while one kernel challenge is admitted and another challenge is requested against its overlay
- **THEN** the overlay is not recomputed, the new challenge is not admitted and the existing challenge stays in its governing lifecycle
- **AND** immediate withdrawal/evaluation behavior remains in force without silently resolving or unsuspending that existing challenge

Form: invariant.

- **Case:** Vary consent class/scope, policy and act identity, composition origins, ingest routes, redaction branches and challenge timing independently.
- **Observable:** Resolved policy/consent provenance, actual transmissions, ingest/exclusion records, affected claim tiers/counts and challenge lifecycle.
- **Oracle:** Effective declarations, actual embedded content provenance and independently marked surviving/removed support, never a composer's asserted class.
- **Falsifier:** A source selects its own weaker policy, a composite launders content, excluded bytes persist, surviving evidence is blanket-degraded or revocation rewrites challenge history.

```yaml
warrants:
  primary: RFC5-14
  doctrine: [VIS-1, VIS-2, VIS-6, SEC-2, SEC-3, SEC-4, SEC-5]
  contracts: [RFC2-13, RFC3-7, RFC3-30, RFC5-11, RFC5-12, RFC5-13, RFC5-14, RFC5-15, RFC5-16, RFC5-17]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Stable selection and explicit context

Generator reading assets and controls SHALL resolve cross-surface selections through owning entity kind and durable identity, project identity, optional evaluation and exactly one scenario context. Private paths, labels, row/scene indices and coordinates SHALL NOT cross the boundary as identity. Loaded project-profile and core selections SHALL retain their existing identity rules without activating deferred profiles or making presentation entities valid source anchors. Unqualified selections SHALL resolve at the latest identified evaluation available at resolution and name it; pinned selections SHALL retain their immutable answer with supersession/staleness visible. Renames, layout changes and presentation hints SHALL NOT change resolution. Every URL-pinned selection SHALL be openable across surfaces with the same semantics; skew SHALL name both evaluations rather than mix them. The kernel SHALL use RFC6-5's fixed first-applicable order: excluded, unconsented, incompatible-scenario, unresolvable, retired, resolved-absent, unknown, resolved. Each outcome SHALL carry its prescribed counts, policy/reason routes, conflict or failed-reference detail, retirement/successors, presence evaluations or complete facts. Not-applicable SHALL be surface-only, preserve the underlying kernel outcome and drawer, and name applicable surfaces; it SHALL NOT be a kernel/URL/endpoint outcome or claim Unknown reason. Kernel-emitted dangling links SHALL be trust-floor incidents, not silent 404s or guessed redirects. Context SHALL be Base by default, Proposed with an explicitly compatible proposal set, or Historical at its immutable superseded evaluation. Non-default-revision Base SHALL name that revision; incompatible/undeclared-compatible proposal combinations SHALL remain separate futures without status authority. Context SHALL travel unchanged through selection, URL, query and handoff. Principal/project/operation admission SHALL precede this resolution; denied callers SHALL receive no project facts or counts disguised as an unconsented selection result.

ID: REQ-polaris-generation-026
Source: RFC6-1; governing warrants below.
Scope: v1-mandatory

#### Scenario: Follow and return to a fact

- **WHEN** an admitted reader follows a manifesto fact into its details or another surface and returns
- **THEN** the selection retains project, durable identity, evaluation and scenario while personal reading hints may be restored
- **AND** renaming, layout movement or stripping surface hints does not change the resolved answer

#### Scenario: Pinned, unpinned and skewed answers

- **WHEN** a pinned selection is reopened after newer evidence exists, an unpinned selection is resolved, or a consumer can answer only at another evaluation
- **THEN** the pinned answer stays historical with staleness, the unpinned answer names its latest identified evaluation, and skew names both identities
- **AND** no consumer silently substitutes current bytes or mixes evaluations

#### Scenario: Policy precedence and absent surface projection

- **WHEN** a reference satisfies multiple resolution conditions or has no projection on the chosen surface
- **THEN** the fixed kernel precedence determines the outcome and a surface-only not-applicable presentation still provides the drawer and applicable-surface choices
- **AND** navigation outcomes neither replace governing claim reasons nor enter their counts

#### Scenario: Proposed context or non-default Base

- **WHEN** a selection names incompatible proposals or a Base evaluation from a non-default revision
- **THEN** incompatible-scenario exposes separate candidate futures, while Base remains Base with the revision explicitly marked
- **AND** handoff and query preserve that context without giving proposed structure status authority

#### Scenario: Unauthorized selection request

- **WHEN** a caller lacks the required principal/project/operation permission
- **THEN** admission refuses before project selection facts or counts are served
- **AND** filters or a normal-looking unconsented navigation response cannot bypass that boundary

#### Scenario: Draft badge cannot adopt a proposed promise

- **WHEN** Base and Proposed accounts describe the same capability and proposed behavior is placed in draft-badged prose as though already adopted
- **THEN** Base retains adopted intent together with observed reality, and fidelity rejects the claim that the proposal is current despite its surrounding draft badge
- **AND** Proposed keeps its explicit proposal membership and adjacent delta without replacing the adopted operative leaf

Form: state projection/query.

- **Case:** Resolve the same references across surfaces with controlled identities, evaluations, policy states, contexts and credentials; vary presentation hints independently.
- **Observable:** Typed outcome, selected identity/evaluation/context, disclosure paths, received facts and authentication refusal.
- **Oracle:** Existing kernel identity/context/outcome rules and independently supplied snapshots; rendered labels and coordinates never define identity.
- **Falsifier:** A handoff changes its question, policy precedence differs, a surface dead-ends a valid reference or a denied caller receives project data.

```yaml
warrants:
  primary: RFC6-1
  doctrine: [VIS-1, VIS-2, VIS-3, VIS-7, SEC-1, SEC-2, SEC-5]
  contracts: [RFC6-1, RFC6-2, RFC6-3, RFC6-4, RFC6-5, RFC6-6, RFC6-7, RFC6-8, RFC6-9, RFC6-10, RFC6-11, RFC6-12, RFC6-24, RFC6-25, RFC6-26, RFC6-27]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Shared facts and honest aggregate composition

For one selection, evaluation and scenario, all generator-facing surfaces and endpoints SHALL consume the same kernel-computed Why this answer? fact set, with no endpoint-only or UI-only facts. It SHALL retain all applicable RFC6-19 groups: identity/lifecycle/plane, complete epistemic state, every supporting evidence reference with capture/scope/integrity/revision binding, producing evaluation and typed authority with governing normative revision and observer versions, governing warrants/dismissals, every open challenge with lifecycle/provenance and contradictions, policy/consent/exclusion/coverage, and separate work/chain states. Coverage SHALL be the executed mapping records plus explicitly captured scope of a partial snapshot, not an invented could-observe judgment. Label, tier, primary Unknown reason and freshness SHALL travel verbatim, with secondary reasons separately marked, sibling states retained and challenge-pending beside the tuple rather than suspending it. Minimal presentation SHALL preserve reachable full facts, and machine queries SHALL serve the complete authorized set without implicitly fetching source bodies. Every answer SHALL declare evaluation and filters/scope; partial/filtered results SHALL NOT claim whole scope. Aggregates SHALL have no epistemic label, tier, reason or freshness of their own. They SHALL expose membership and expandable composition by label, all six tiers, primary Unknown reason, freshness, sibling states, pending challenges and applicable chain/normalized-work values. Secondary reasons, navigation outcomes and work-state absence values SHALL NOT inflate primary Unknown-reason totals. Equivalent renderings SHALL preserve evaluation, declared filters, graph, full epistemic/sibling/challenge/work/chain state and scenario, with matching counts over the same scope. Finer detail SHALL be disclosed as a filter/aggregation difference; disagreement over equivalent scope SHALL be a release-blocking projection/kernel defect. All required selections, disclosures and handoffs SHALL remain keyboard/nonvisual operable, including the path back to the reading. Evidence metadata and resolvable links SHALL NOT be treated as authority for extra body reads or as substitutes for the owning verbatim route. Any related-project navigation or child-fact composition used by a generated account SHALL follow declared asymmetric relationships: one-sided declarations remain unconfirmed and confirmation requires compatible counterpart declarations. Child labels SHALL remain unchanged and any offered rollup SHALL retain the shared aggregate composition contract. This does not introduce a workspace or portfolio presentation.

ID: REQ-polaris-generation-027
Source: RFC6-18; governing warrants below.
Scope: v1-mandatory

#### Scenario: Same fact set at different reading densities

- **WHEN** the same authorized selection is inspected in a concise narrative, expanded details and machine output at one evaluation/context
- **THEN** all required fact groups, labels and provenance remain reachable and semantically identical
- **AND** hiding detail at rest neither removes facts nor causes an implicit unconsented body fetch

#### Scenario: Aggregate mixes confidence and work outcomes

- **WHEN** an aggregate contains members with different labels, tiers, freshness, sibling/challenge states and work/chain values
- **THEN** it exposes membership and complete expandable composition without a headline aggregate epistemic state
- **AND** matching-scope renderings agree on counts and cannot turn mixed membership into a positive summary label

#### Scenario: Secondary reasons and pending challenges

- **WHEN** a member has primary and secondary Unknown reasons or a submitted but not admitted challenge
- **THEN** primary counts include the claim once, secondary annotations stay separate and challenge-pending leaves its existing tuple unsuspended
- **AND** navigation and work-state absence values are not counted as claim Unknown reasons

#### Scenario: Filters or detail level differ

- **WHEN** two views use different filters or one exposes finer detail than a visual aggregate
- **THEN** the difference and resulting scope are declared rather than labelled equivalent whole-project answers
- **AND** over an equivalent scope any fact, tuple, context or count disagreement fails the parity check

#### Scenario: Keyboard and nonvisual deep reading

- **WHEN** a reader opens Why this answer?, follows supporting records and returns without a pointing device or visual layout cues
- **THEN** the required facts, policy distinctions and navigation paths remain usable with the same selection context
- **AND** accessible individual controls alone cannot establish this path-level result

#### Scenario: Declared project relation may be one-sided

- **WHEN** an admitted project declares a parent/child or related-project edge with absent, incompatible or compatible counterpart declarations
- **THEN** only compatible counterpart declarations establish confirmation; one-sided declarations remain explicitly unconfirmed and unavailable counterpart evidence remains Unknown
- **AND** neither diagram geometry nor narrative prose invents confirmation, and any displayed child facts retain their original epistemic labels

#### Scenario: Related-child rollup retains composition

- **WHEN** a related-child fact rollup is offered from admitted existing relations
- **THEN** the rollup exposes the same member composition and equivalence context required for other shared aggregates, with expandable members
- **AND** a child Unknown is never folded into a positive parent summary, and the relationship grants no additional child-source access

#### Scenario: A work item has an indeterminate state plane

- **WHEN** a scoped work observation cannot determine the item's state plane
- **THEN** the item remains present and counted with its plane explicitly Unknown and its actual missing-input cause
- **AND** no consumer drops it or guesses a plane to make the aggregate look complete

Form: invariant.

- **Case:** Compare independent renderings and machine responses over controlled mixed memberships, filters, challenge states and identical/different evaluations.
- **Observable:** Full fact groups, member composition, scope/context envelope and actual keyboard/nonvisual traversal.
- **Oracle:** Independent member tuples, executed coverage records and kernel fact sets, not the aggregate's label or one renderer's equality claim.
- **Falsifier:** A fact disappears by channel/density, an aggregate acquires its own epistemic state, reason counts inflate or a required path is inaccessible.

```yaml
warrants:
  primary: RFC6-18
  doctrine: [VIS-1, VIS-2, VIS-3, VIS-7, SEC-2, SEC-5]
  contracts: [RFC6-13, RFC6-14, RFC6-15, RFC6-16, RFC6-17, RFC6-18, RFC6-19, RFC6-20, RFC6-21, RFC6-22, RFC6-23, RFC6-24, RFC6-25, RFC8-1]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Evidence-derived work state and liveness

Recorded generator stages and provider/artifact receipts SHALL remain distinct from normalized work state and worker liveness. Normalization SHALL be a per-evaluation projection under an effective, versioned mapping captured as RFC2-1 item 7, never an editable scheduler mirror or a new Claim/observation-record member. It SHALL use the exact RFC8-12 thirteen-value vocabulary and RFC8-13 predicates, carrying qualified raw substrate values read from the tool's declared vocabulary. Unknown raw mappings SHALL remain state-undetermined with their mapping route, never dropped or force-fitted. Every rendering, filter, count, export and machine answer of drafting work SHALL carry separately qualified normalized and chain fields, including normalized reconciled; that value SHALL additionally retain the underlying verdict's tier/evaluation and SHALL NOT appear without its required support. State-local absence values SHALL NOT enter claim Unknown-reason counts. Ready SHALL derive only from the answering snapshot's captured work/dependency inputs, never a live scheduler readiness call. New dispatch SHALL use its separately fresh admission evaluation without rewriting historical readiness. Worker activity SHALL use only RFC4-23's qualifying branch-tip/commit/PR signal, actual instant and effectively declared bound; provider receipts, draft saves, coordinator heartbeats, locks and worktree presence SHALL NOT substitute. Missing/ineffective bounds and expired signals SHALL retain their specified absence behavior, while between-signal liveness SHALL remain Unknown. Blocked SHALL carry every derived dependency/pr-wait/external/decision cause in all views/filters/counts/answers, with cause-Unknown only for the empty set. Future/planned/review/merged/terminal states SHALL preserve their approval, exclusivity, dependency, exact-head and VCS predicates; closure alone SHALL NOT imply completion or satisfied intent. Where no current predicate defines a normalized value, the system SHALL expose the unsupported derivation with valid raw/progress facts and liveness Unknown, without inventing a value or claiming complete normalized-state conformance. Another state SHALL apply only through its own independently satisfied predicate. Phase applicability SHALL follow EXECUTION-PHASES.md: Phase A introduces no live work-state consumer or effect, while Phase B's drafting-work drawer, Trajectory work rows, work filters/counts, work exports and machine work answers SHALL implement these projections. Stage receipts and narrative assets SHALL NOT become work items or substitute for the owning drafting lifecycle. The generator SHALL NOT infer a worker bound from provider timeout, run deadline or receipt cadence, and SHALL NOT discard an effective bound to select an absence case. A selected live profile requiring an unsupported normalized derivation SHALL fail admission before materialization or provider dispatch until its mapping/required act is effective; a different profile SHALL require explicit selection. Pure mechanics, honest refusal or a successful supported-profile run SHALL NOT establish support for an unimplemented predicate or completion of the full generator objective.

ID: REQ-polaris-generation-028
Source: RFC8-12; governing warrants below.
Scope: v1-mandatory

#### Scenario: Displayed ready and later admission differ

- **WHEN** readiness is queried at evaluation E and a later dispatch captures changed scheduler data
- **THEN** E replays from its captured work/dependency inputs while dispatch uses the new identified admission evaluation
- **AND** neither a live ready command nor the later result overwrites E's answer

#### Scenario: Generation activity lacks a qualifying worker signal

- **WHEN** provider responses or saved drafts exist without a captured qualifying branch-tip, commit or PR signal
- **THEN** those generation facts remain visible without asserting worker liveness or normalized active
- **AND** if the next requested live run selects a profile requiring a bound-but-no-signal case with no accepted predicate, admission refuses before materialization or provider dispatch, preserves the unsupported-case finding and names its mapping/act route
- **AND** neither silent profile substitution nor completing pure fixture mechanics satisfies that required support

#### Scenario: Mechanics do not introduce a live work projection

- **WHEN** the authorized mechanics phase validates, generates fixture assets or renders a synthetic preview
- **THEN** it produces no live scheduler mutation, provider call or owner effect control and identifies its evidence as mechanics-only
- **AND** integration requirements remain unmet until their actual consumers/effects and final owner experience are implemented and verified

#### Scenario: Missing bound or expired real signal

- **WHEN** the liveness bound is absent/ineffective or a real qualifying signal is older than the effective bound
- **THEN** the corresponding activity-undetermined or stale-or-dead behavior is preserved with available claim/signal instants and the governing resolution route
- **AND** a heartbeat, lock or worktree cannot make active renderable

#### Scenario: Several blocked causes resolve

- **WHEN** declared derivations establish dependency and review-wait causes for the same item
- **THEN** every consumer carries the full dependency/pr-wait set rather than choosing one cause
- **AND** cause-Unknown is reserved for no resolving cause and never mixed into that nonempty set

#### Scenario: Closure or reconciled projection is inspected

- **WHEN** closure lacks merge evidence, or normalized reconciled is requested without the verdict's tier/evaluation
- **THEN** closure remains closed-unmerged with its actual/absent reason and unsupported reconciled is not emitted
- **AND** separate chain/raw/evaluation fields remain available and no normalized value becomes independent satisfaction evidence

Form: state projection/query.

- **Case:** Vary raw vocabulary, effective mapping/bounds, snapshot inputs, progress signals, blocked sets and merge/verdict evidence independently.
- **Observable:** Qualified normalized/raw/chain values, liveness, provenance, counts/filters and unsupported-case findings.
- **Oracle:** Accepted state predicates and captured source facts, never generation-stage labels or a current scheduler command outside the snapshot.
- **Falsifier:** A stage becomes worker liveness, absent evidence produces a fabricated state/time, or a state/count consumer drops its paired chain field.

```yaml
warrants:
  primary: RFC8-12
  doctrine: [VIS-1, VIS-2, VIS-6, VIS-7]
  contracts: [RFC4-15, RFC4-23, RFC8-7, RFC8-8, RFC8-12, RFC8-13, RFC8-14, RFC8-15, RFC8-16, RFC8-17, RFC8-28, RFC8-29, RFC8-30, RFC8-31]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: Captured work history and traceable accounting

Every scheduler-resident fact on which a durable generator record depends SHALL be captured into owned Execution/observation evidence before the declared retention horizon. Effective policy SHALL declare that horizon and a maximum inter-pass interval tied to it; missing/ineffective declarations SHALL leave dependent history claims Unknown under no-currency-bound-declared mechanics. Capture SHALL remain within ordinary human-triggered observation, without inventing autonomous polling authority. Missed capture and lost history SHALL remain visible with the retention event, never interpreted as no work existing. Substrate pins SHALL be supplementary rather than the primary durability guarantee. Compaction records SHALL identify summarized, discarded and externally queryable populations without changing claim meaning. Historical telemetry SHALL derive exclusively from captured Execution Records with unavailable fields Unknown; V0 SHALL not simulate it, and optional enrichment SHALL remain optional. Consumed warrant-to-Proposal-to-materialization-to-work-to-run-to-change-to-merge-to-reconciliation joins SHALL be traversable both ways with their recorded-identity/naming-convention basis and fidelity. Missing joins SHALL show the break, actual reason and downstream degradation without similarity-based invention. Reduced-fidelity facts SHALL carry structured declared granularity, unavailable granularity, an RFC4-24 cause and upgrade path. The cause vocabulary SHALL remain post-merge-history-unreachable, replace-in-place-source, retention-horizon-passed, derived-from-convention, approximated-boundary, terminal-report-only or indistinguishable-runs. Finer-granularity questions SHALL render Unknown with their governing reason instead of interpolation, without erasing the coarser fact's otherwise-earned authority at its declared granularity; fidelity causes SHALL NOT become new claim Unknown reasons. A complete weak chain SHALL remain complete and weak, not incomplete solely for absent optional instrumentation. Unknown-provenance work/run/change SHALL remain visible, counted, filterable and separate from warranted work without ingress rejection; an orphan Contradiction SHALL retain its stronger unfilterable owner-adjudication route. Native edits to derived warrant pointers SHALL render as annotations and the authoritative pointer SHALL be reasserted at the next evaluation without rewriting the materialization record. Measures SHALL remain independent: estimates/complexity declared-only with accuracy Unknown, derived cost Inferred, attempt counts from records, overlapping blocked-cause intervals disclosed and touched components resolved through declared mapping. Missing measures and partial totals SHALL retain Unknown and coverage rather than a synthetic effort score. No observed-fleet live streaming/control, unsupported reconciliation computation or inherited mutation beyond its own warrant SHALL be introduced by this accounting.

ID: REQ-polaris-generation-029
Source: RFC4-16; governing warrants below.
Scope: v1-mandatory

#### Scenario: Retention declaration or timely capture is missing

- **WHEN** the effective retention/interval declaration is absent or a required scheduler fact is lost before capture
- **THEN** the dependent history claim is Unknown with its actual declaration or retention-event explanation
- **AND** a substrate pin or empty current export cannot prove no work existed

#### Scenario: Compaction retains its account

- **WHEN** permitted raw history is compacted
- **THEN** the compaction identifies what was summarized, discarded and remains queryable while protected structured history survives
- **AND** historical telemetry and claim meanings are not reconstructed or upgraded from summaries

#### Scenario: A chain is weak or broken

- **WHEN** one join has a declared naming-convention basis and another cannot be established
- **THEN** the first retains its reduced-fidelity basis while the second exposes the break and downstream degradation
- **AND** optional instrumentation absence does not make a complete weak chain incomplete, and similarity cannot fabricate a missing join

#### Scenario: Unwarranted history or edited pointer appears

- **WHEN** observed work lacks a traceable warrant or a substrate-side warrant pointer is edited
- **THEN** untraceable history remains separately visible and the pointer edit is an annotation with authoritative reassertion at the next evaluation
- **AND** an orphan remains its unfilterable Contradiction rather than disappearing behind the provenance label or a rewritten join

#### Scenario: Independent measures and captured telemetry

- **WHEN** usage, estimates, blocked intervals and touched-component measures are rendered
- **THEN** each retains its source/class, overlapping causes and declared mapping, with partial coverage and no composite effort score
- **AND** recorded generation stages or simulated values cannot fill missing historical telemetry

#### Scenario: Requested detail exceeds preserved granularity

- **WHEN** a captured fact supports PR-level history but a query asks for unavailable per-commit detail
- **THEN** its structured fidelity label names supported/unavailable granularity, the governing cause and an upgrade path, while the finer answer is Unknown with its own governing reason
- **AND** the coarser fact is neither discarded nor interpolated into stronger detail, and the fidelity cause does not enter claim-reason counts

Form: invariant.

- **Case:** Vary capture history, effective interval policies, compaction records, join evidence and measure coverage over an identified window.
- **Observable:** Durable source captures, history/chain traversal, provenance/fidelity, pointer effects and measure composition.
- **Oracle:** Captured records, governing bounds and declared joins/mappings, never current substrate emptiness or inferred reconstruction.
- **Falsifier:** A lost event becomes absence, a pointer edit changes authority, weak evidence is strengthened, or independent measures become synthetic certainty.

```yaml
warrants:
  primary: RFC4-16
  doctrine: [VIS-1, VIS-2, VIS-6, VIS-7]
  contracts: [RFC4-16, RFC4-20, RFC4-21, RFC4-22, RFC4-24, RFC8-6, RFC8-7, RFC8-11, RFC8-18, RFC8-19, RFC8-20, RFC8-21, RFC8-22, RFC8-23, RFC8-24, RFC8-26, RFC8-27, RFC8-31]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: []
```
