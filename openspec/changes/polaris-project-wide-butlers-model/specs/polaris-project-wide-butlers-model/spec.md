# Specification — polaris-project-wide-butlers-model

## Purpose

Polaris explains the full declared shape of the configured Butlers project in
plain language, with complete coverage, exact sources and visible gaps.

## ADDED Requirements

### Requirement: PWB-REQ-001 — Project-shape observation is revision-bound and explicitly scoped

Group: Observation. Form: **state projection/query**.

WHEN the POC observes Butlers, it SHALL bind the project-shape source manifest
and every admitted source to the configured repository's exact Git revision,
and SHALL expose the complete admitted source-path population to both human and
machine readers.

- **Case**: observe a repository at a known revision whose five-pillar index
  and roster population are known independently.
- **Observable**: the machine answer and Polaris expose the revision, admitted
  source paths and source count.
- **Oracle**: compare the exposed paths and revision to an independent Git tree
  listing and the declared five-pillar/roster indexes; exact set equality
  decides.
- **Oracle independence**: the expected set comes from Git and the Butlers
  indexes, not from the POC model.
- **Falsifier**: one admitted source is absent, one undeclared arbitrary source
  is included, or two exposed sources use different revisions.

#### Scenario: Source population is complete at one revision

- **WHEN** Butlers is observed at revision R
- **THEN** every admitted project-shape source resolves at R
- **AND** the human and machine views expose the same complete source set

```yaml
warrants:
  primary: VIS-7
  doctrine: [VIS-1, VIS-7, SEC-3]
  contracts: [RFC2-1, RFC2-2, RFC2-3, RFC2-6, RFC2-7, RFC3-27, RFC4-1, RFC4-2, RFC4-3, RFC4-7, RFC4-8, RFC4-10, RFC4-11, RFC6-13, RFC6-15, RFC7-10]
  policies: [CC-SPEC-4, CC-TEST-3]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-020]
```

### Requirement: PWB-REQ-002 — Every declared project-shape item is accounted for

Group: Coverage. Form: **invariant**.

Polaris SHALL account for every item declared by the configured Butlers
project-shape population across Heart and Soul, Legends and Lore, Spec and
Spine, Lay and Land, Craft and Care and roster identity. Each item SHALL be in
exactly one coverage state: modeled, Unknown or contradicted.

- **Case (sweep)**: enumerate the source population and every declared item in
  each category at one revision, then compare it to the model.
- **Observable**: per-category identities and reconciling counts are visible in
  the machine answer and reachable from Polaris.
- **Oracle**: independent extraction from the revision-bound source population
  produces denominator D; modeled + Unknown + contradicted equals D, with each
  identity appearing once.
- **Oracle independence**: the expected denominator is extracted from the
  source files, not from the POC's coverage object.
- **Falsifier**: an item disappears, appears twice, lacks a coverage state, or
  the counts do not reconcile.

#### Scenario: Declared shape reconciles

- **WHEN** the configured Butlers revision declares D project-shape items
- **THEN** Polaris accounts for all D items exactly once
- **AND** every category reports modeled, Unknown and contradicted counts that
  sum to its denominator

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-1, VIS-2, VIS-7]
  contracts: [RFC1-5, RFC1-7, RFC1-14, RFC2-6, RFC2-23, RFC2-24, RFC4-27, RFC6-16, RFC6-17, RFC6-21, RFC7-5, RFC7-6, RFC7-9, RFC7-15, RFC7-16, RFC7-19]
  policies: [CC-SPEC-4, CC-SPEC-11, CC-TEST-5, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-030]
```

### Requirement: PWB-REQ-003 — Missing, unreadable and excluded sources remain visible

Group: Coverage. Form: **prohibition**.

The POC SHALL NOT shrink the declared denominator when a project-shape source
is missing, unreadable, unclassifiable or excluded by the secret policy. The
affected item SHALL render Unknown with a fixed reason and exclusion
provenance that contains no excluded body content.

- **Case (counterexample + sweep)**: remove one admitted source, deny one read,
  and supply one source that the content classifier excludes.
- **Observable**: each case remains in coverage as Unknown; the machine answer
  and Polaris expose the reason without sensitive content.
- **Oracle**: compare the pre-fault denominator to the post-fault denominator
  and scan response bytes for sentinels; equal denominators, expected reasons
  and zero sensitive sentinels decide.
- **Oracle independence**: injected filesystem faults and sentinel values are
  controlled outside the observer.
- **Falsifier**: a faulted item disappears, becomes modeled, loses its reason,
  or reproduces excluded content.

#### Scenario: Excluded source fails closed

- **WHEN** an admitted shape source cannot be classified as safe to index
- **THEN** its declared item remains counted as Unknown
- **AND** only hash-not-body exclusion provenance is exposed

```yaml
warrants:
  primary: SEC-5
  doctrine: [VIS-1, VIS-2, VIS-7, SEC-5]
  contracts: [RFC2-23, RFC2-24, RFC3-30, RFC4-4, RFC5-16, RFC5-17, RFC6-27, RFC7-11, RFC7-19]
  policies: [CC-BAR-5, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-032]
```

### Requirement: PWB-REQ-004 — Conflicting declarations are disclosed and precedence is explicit

Group: Coverage. Form: **invariant**.

WHEN two admitted Butlers artifacts disagree about one project fact, Polaris
SHALL expose both source anchors and the disagreement. It SHALL identify an
effective statement only when Butlers declares an applicable precedence rule;
otherwise the fact SHALL remain Unknown.

- **Case**: observe two controlled declarations with different values, once
  with an applicable precedence rule and once without one.
- **Observable**: Polaris and the machine answer show both values and sources;
  the first case names the precedence basis and the second renders Unknown.
- **Oracle**: compare the rendered values, source identities and result to the
  controlled declarations and precedence input.
- **Oracle independence**: the conflict and precedence rule are fixtures
  supplied independently of the model.
- **Falsifier**: one declaration is hidden, a winner is selected without a
  rule, or disagreement is rendered as agreement.

#### Scenario: Stale summary does not silently replace V1 scope

- **WHEN** a summary count disagrees with the authoritative V1 declaration
- **THEN** Polaris exposes the disagreement and both sources
- **AND** any effective count cites the documented precedence rule that chose it

```yaml
warrants:
  primary: VIS-1
  doctrine: [VIS-1, VIS-2, VIS-7]
  contracts: [RFC1-24, RFC2-7, RFC2-24, RFC7-2, RFC7-10, RFC7-11, RFC7-11(a)]
  policies: [CC-BAR-3, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-032]
```

### Requirement: PWB-REQ-010 — Polaris opens with the whole project

Group: Presentation. Form: **state projection/query**.

WHEN Polaris is opened, it SHALL first present Butlers' purpose, promises,
non-goals, architecture, V1 scope and success criteria before presenting any
single capability's detail.

- **Case**: load Polaris with a model containing project statements and one or
  more capability deep dives.
- **Observable**: the first reading level answers the project questions and
  routes to the catalogs; capability detail is subordinate.
- **Oracle**: inspect the heading order and entity references against an
  independently enumerated project-level fact set.
- **Oracle independence**: expected facts and order come from RFC7-13 and the
  machine model, not the rendered page.
- **Falsifier**: the entry opens on one capability, omits a project-level
  category, or requires reading a capability deep dive to learn what Butlers is.

#### Scenario: WhatsApp is a drill-down, not the project account

- **WHEN** the existing WhatsApp capability slice is present
- **THEN** the Polaris entry explains Butlers before linking to that slice
- **AND** the slice is labeled as one capability within the complete catalog

```yaml
warrants:
  primary: RFC7-1
  doctrine: [VIS-1, VIS-3]
  contracts: [RFC7-1, RFC7-6, RFC7-13, RFC7-15, RFC7-17, RFC7-29]
  policies: [CC-BAR-3]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-030]
```

### Requirement: PWB-REQ-011 — Project summary, catalogs and exact sources are progressively reachable

Group: Presentation. Form: **invariant**.

Polaris SHALL provide a project summary, complete project catalogs, capability
deep dives and exact authoritative artifacts as progressively deeper reading
levels. A reader who stops at any level SHALL retain a true, coarser account.

- **Case (sweep)**: start from every project-level catalog category and follow
  one declared item through each available depth.
- **Observable**: each path resolves from summary to catalog to detail to exact
  source without changing the fact's identity or epistemic state.
- **Oracle**: enumerate every category and compare path targets to the machine
  answer and source anchors; the complete path population decides.
- **Oracle independence**: categories and anchors come from the source model,
  while expected depth semantics come from RFC7-13/14/17.
- **Falsifier**: a category is unreachable, a link resolves to a different
  identity, or a coarser level overstates the deeper source.

#### Scenario: Capability reaches exact requirements

- **WHEN** a reader opens a declared capability from the catalog
- **THEN** its detail links to the governing requirement identities
- **AND** exact requirement text remains reachable without treating Polaris as authority

```yaml
warrants:
  primary: RFC7-13
  doctrine: [VIS-1, VIS-3, VIS-7]
  contracts: [RFC1-26, RFC3-27, RFC3-28, RFC6-20, RFC6-21, RFC7-3, RFC7-9, RFC7-10, RFC7-13, RFC7-14, RFC7-17, RFC7-34]
  policies: [CC-BAR-3]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-031]
```

### Requirement: PWB-REQ-012 — Owner-facing copy is direct and concise

Group: Presentation. Form: **prohibition**.

Polaris SHALL use short headings that name Butlers concepts and direct
sentences that state project facts, gaps or actions. It SHALL NOT use
owner-facing meta-narration whose subject is the page, document, reading,
section, movement or presentation mechanism, except a necessary scope or
interaction instruction.

- **Case (counterexample + sweep)**: enumerate every owner-facing heading,
  lede, notice and explanatory sentence on Polaris, including a fixture with
  meta-narration.
- **Observable**: project copy names Butlers concepts directly; the injected
  meta-copy is rejected by the review oracle.
- **Oracle**: a fresh reader classifies each string by its subject and purpose,
  then performs the cold-open reading; zero unnecessary meta-narration and no
  required rereading decide.
- **Oracle independence**: the reviewer receives only rendered copy, the
  direct-copy criteria and the project facts, not implementation labels or the
  author's rationale.
- **Falsifier**: unnecessary copy explains how to read the page instead of
  explaining Butlers, or the owner must reread it to identify the project fact.

#### Scenario: Section headings name project concepts

- **WHEN** Polaris renders the project-level entry
- **THEN** its headings name concepts such as purpose, boundaries,
  architecture, V1 scope, capabilities, evidence or gaps
- **AND** no heading describes a document movement or reading stage

```yaml
warrants:
  primary: VIS-3
  doctrine: [VIS-1, VIS-3]
  contracts: [RFC7-1, RFC7-13, RFC7-30]
  policies: [CC-BAR-3, CC-REV-4]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```

### Requirement: PWB-REQ-013 — Proposed work stays subordinate to current project truth

Group: Presentation. Form: **prohibition**.

Polaris SHALL NOT present active or proposed OpenSpec changes as the current
project account. Proposed work SHALL appear only in the affected capability's
detail, with its lifecycle state and current authoritative requirement adjacent.

- **Case (counterexample + sweep)**: load current and proposed requirements for
  one capability and enumerate every project-level and capability-level claim.
- **Observable**: the project account uses current authority; proposal content
  appears only in capability detail and is visibly distinct.
- **Oracle**: compare all claims to the current/proposed source identities and
  lifecycle states in the machine answer.
- **Oracle independence**: expected current and proposed sets come from the
  OpenSpec artifacts, not Polaris.
- **Falsifier**: proposed content appears as current, replaces current text, or
  dominates the project-level account.

#### Scenario: Proposal is shown only in affected capability detail

- **WHEN** a capability has an active OpenSpec change
- **THEN** the project summary remains based on current authority
- **AND** the capability detail labels and presents the proposal beside current intent

```yaml
warrants:
  primary: VIS-4
  doctrine: [VIS-1, VIS-2, VIS-4]
  contracts: [RFC1-31, RFC6-24, RFC7-14, RFC7-26, RFC7-27]
  policies: [CC-BAR-5]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```

### Requirement: PWB-REQ-020 — Project-wide facts remain identical across human and machine views

Group: Parity. Form: **invariant**.

Every project-shape identity, statement, source anchor, coverage state,
denominator and contradiction Polaris presents SHALL be recoverable from the
same evaluation in the machine answer, preserving multiplicity.

- **Case (sweep)**: enumerate every project-shape parity marker on Polaris and
  every corresponding machine-answer fact at one evaluation.
- **Observable**: both populations contain equivalent multisets.
- **Oracle**: an independent order-insensitive, multiplicity-preserving
  comparator reports both denominators and zero differences.
- **Oracle independence**: the comparator extracts each channel separately and
  imports no production vocabulary or rendering code.
- **Falsifier**: one fact is missing, duplicated, changed or associated with a
  different evaluation in either channel.

#### Scenario: Complete model has wire parity

- **WHEN** Polaris renders a project-wide evaluation
- **THEN** the complete human fact multiset equals the machine fact multiset
- **AND** the check reports both denominators

```yaml
warrants:
  primary: RFC6-22
  doctrine: [VIS-1, VIS-7]
  contracts: [RFC6-13, RFC6-14, RFC6-15, RFC6-17, RFC6-21, RFC6-22, RFC6-23, RFC7-18, RFC7-33, RFC7-34]
  policies: [CC-TEST-5]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-020]
```

### Requirement: PWB-REQ-021 — POC success includes whole-project cold-open comprehension

Group: Evaluation. Form: **event-response**.

WHEN the owner performs a cold-open Polaris walkthrough with no repository or
authoring context, POC success SHALL require the reader to explain why Butlers
exists, what it promises and refuses, its major architecture and capability
groups, its V1 success criteria, where exact requirements live, and one current
Unknown or contradiction with its source.

- **Case**: an owner reads only Polaris at a named evaluation and answers the
  RFC7-30 prompts in their own words.
- **Observable**: a retained walkthrough record contains the answers, paths,
  evaluation identity and owner judgment.
- **Oracle**: compare each answer to its authoritative Butlers artifact and
  require every named prompt to be answered without a confident error caused by
  the surface.
- **Oracle independence**: answer checking uses Butlers artifacts; the owner,
  not the implementation, supplies the judgment.
- **Falsifier**: the reader cannot explain Butlers as a whole, confidently
  answers incorrectly because of Polaris, cannot reach exact intent, or cannot
  identify a visible Unknown or contradiction.

#### Scenario: Whole-project walkthrough passes

- **WHEN** the owner completes a cold-open walkthrough at evaluation E
- **THEN** every project-comprehension prompt is answered from Polaris alone
- **AND** the retained record resolves each answer to current Butlers authority

```yaml
warrants:
  primary: RFC7-30
  doctrine: [VIS-1, VIS-2, VIS-3]
  contracts: [RFC3-15, RFC3-16, RFC7-30, RFC7-31, RFC7-32]
  policies: [CC-REV-4]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```

### Requirement: PWB-REQ-022 — Absent or unlawful owner judgment never becomes success

Group: Evaluation. Form: **prohibition**.

The POC SHALL NOT render the project-wide Polaris evaluation successful unless
a retained walkthrough execution record and a lawful owner judgment both bind
the exact surface version and evaluation identity. Absent, stale or unverifiable
judgment SHALL render the criterion Unknown, never met.

- **Case (counterexample + sweep)**: evaluate absent, mismatched, stale and
  unverifiable judgment records plus one valid pair.
- **Observable**: only the valid pair may carry the owner's verdict; every
  invalid case renders Unknown with its reason.
- **Oracle**: compare record identities and owner-act provenance to the
  controlled inputs for all cases.
- **Oracle independence**: record validity is checked outside the surface
  using RFC3-16 owner-act provenance.
- **Falsifier**: any invalid case renders successful or a judgment is inferred
  from tests, code, an agent report or page availability.

#### Scenario: Missing judgment remains Unknown

- **WHEN** no lawful owner judgment exists for the exact walkthrough record
- **THEN** the POC reports the Polaris evaluation criterion as Unknown
- **AND** it does not substitute implementation or test evidence for judgment

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-2, VIS-4]
  contracts: [RFC3-15, RFC3-16, RFC7-31]
  policies: [CC-BAR-4, CC-TEST-2]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```
