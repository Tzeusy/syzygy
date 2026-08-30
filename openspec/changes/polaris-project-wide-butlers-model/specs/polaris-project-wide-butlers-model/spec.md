# Specification — polaris-project-wide-butlers-model

## Purpose

Polaris explains the full declared shape of the configured Butlers project in
plain language, with complete coverage, exact sources and visible gaps.

Reader definitions:

- The **source-path population** is closed by four rules: the five pillar roots
  named in Butlers' root project-shape index; files named by each pillar's own
  index within that root; baseline `openspec/specs/*/spec.md` Git-tree entries;
  and top-level roster directories containing `butler.toml`, with their
  `MANIFESTO.md` when present. Narrative links do not recurse.
- A **declared item** has one class from this closed set and one extraction rule:
  `project-account-section` uses the six keys purpose, promises, refusals,
  architecture, V1 scope and V1 success; `principle` uses each numbered
  non-negotiable; `success-criterion` uses each list item in the two success
  sections; `catalog-entry` uses each top-level named entry under the V1
  Staffers, Butlers, Modules, Connectors, Dashboard, Identity System,
  Situational Awareness and Observability headings; `design-contract` uses each
  RFC index-table identity; `baseline-spec` uses each baseline spec directory;
  `topology-component` uses each first-column identity in the component tables;
  `craft-policy` uses each policy-file identity in the craft index; and
  `roster-identity` uses each top-level roster directory containing
  butler.toml. No other prose, heading, link or file mints an item.
- Stable item identity is `(item class, declared key)`. Repository-relative path
  and content hash are source-anchor state, never identity. A duplicate key in
  one class is a contradiction rather than a path-based disambiguation.
- The source-path denominator remains known through body-read failures. An
  unavailable body's within-source item denominator is Unknown, never copied
  from a fixture or prior ambient state.

## ADDED Requirements

### Requirement: PWB-REQ-001 — Project-shape observation is revision-bound and explicitly scoped

Group: Observation. Form: **state projection/query**.

WHEN the POC observes Butlers, it SHALL bind the complete source-path
population to the configured repository's exact Git revision and SHALL bind
the consent record, secret-policy version, source-discovery version and
observer/parser version as deterministic evaluation inputs. Human and machine
readers SHALL receive those identities, the capture instant and the same source
population. Every emitted project-shape fact SHALL carry its source identity,
scope, capture instant and observer identity/version.

- **Case**: observe a repository at a known revision whose five-pillar index
  and roster population are known independently.
- **Observable**: the machine answer and Polaris expose the revision, source
  paths, source count, capture instant and every deterministic input and
  per-emission identity.
- **Oracle**: compare the exposed paths and revision to an independent Git tree
  listing and the closed discovery rules; exact set and input-identity equality
  decides.
- **Oracle independence**: the expected set comes from Git and the Butlers
  indexes, not from the POC model.
- **Falsifier**: one source is absent, one arbitrary source is included, one
  deterministic input identity is missing, or exposed sources use different
  revisions.

#### Scenario: Source population is complete at one revision

- **WHEN** Butlers is observed at revision R
- **THEN** every admitted project-shape source resolves at R
- **AND** the human and machine views expose the same complete source set

```yaml
warrants:
  primary: VIS-7
  doctrine: [VIS-1, VIS-7, SEC-3]
  contracts: [RFC2-1, RFC4-1, RFC4-2, RFC4-3, RFC4-11, RFC6-15, RFC7-10]
  policies: [CC-SPEC-4, CC-TEST-3]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-020]
```

### Requirement: PWB-REQ-002 — Every declared project-shape item is accounted for

Group: Coverage. Form: **invariant**.

For every lawfully admitted source body, Polaris SHALL account for each
declared item discovered by the closed extraction rule across Heart and Soul,
Legends and Lore, Spec and Spine, Lay and Land, Craft and Care and roster
identity. Each admitted item SHALL be in exactly one coverage state: modeled,
Unknown or contradicted. A source whose item population cannot be read SHALL
retain its source identity while its item denominator renders Unknown.

- **Case (sweep)**: enumerate the source population and every declared item in
  each readable category at one revision, then compare it to the model; include
  an unreadable source case.
- **Observable**: per-category identities and reconciling counts are visible in
  the machine answer and reachable from Polaris.
- **Oracle**: independent extraction from the revision-bound source population
  produces denominator D; modeled + Unknown + contradicted equals D, with each
  identity appearing once; unreadable sources carry an Unknown item denominator.
- **Oracle independence**: the expected denominator is extracted from the
  source files, not from the POC's coverage object.
- **Falsifier**: a known source disappears, an admitted item appears twice or
  lacks a state, a known count does not reconcile, or an unavailable body's
  item denominator is presented as known.

#### Scenario: Declared shape reconciles

- **WHEN** the configured Butlers revision declares D project-shape items
- **THEN** Polaris accounts for all D items exactly once
- **AND** every category reports modeled, Unknown and contradicted counts that
  sum to its denominator

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-1, VIS-2, VIS-7]
  contracts: [RFC1-14, RFC2-23, RFC6-16, RFC6-17, RFC7-15]
  policies: [CC-SPEC-4, CC-SPEC-11, CC-TEST-5, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-030]
```

### Requirement: PWB-REQ-003 — Missing, unreadable and excluded sources remain visible

Group: Coverage. Form: **prohibition**.

The POC SHALL NOT shrink the source-path denominator when a project-shape
source is missing, unreadable, unclassifiable or excluded by the secret policy.
The affected source SHALL render Unknown with a fixed reason; its item
denominator SHALL render Unknown unless an identified, lawfully admitted
observation supplies that exact population. Exclusion provenance SHALL contain
no excluded body content.

- **Case (counterexample + sweep)**: remove one admitted source, deny one read,
  and supply one source that the content classifier excludes.
- **Observable**: each case remains in coverage as Unknown; the machine answer
  and Polaris expose the reason without sensitive content.
- **Oracle**: compare the Git source-path population to the post-fault source
  population and scan every model, cache, log, HTML, JSON and record sink for
  sentinels; equal source denominators, Unknown item denominator, expected
  reasons and zero sensitive sentinels decide.
- **Oracle independence**: injected filesystem faults and sentinel values are
  controlled outside the observer.
- **Falsifier**: a faulted source disappears, becomes modeled, loses its reason,
  or reproduces excluded content.

#### Scenario: Excluded source fails closed

- **WHEN** an admitted shape source cannot be classified as safe to index
- **THEN** its source identity remains counted as Unknown
- **AND** its within-source item denominator is Unknown
- **AND** only hash-not-body exclusion provenance is exposed

```yaml
warrants:
  primary: SEC-5
  doctrine: [VIS-1, VIS-2, VIS-7, SEC-5]
  contracts: [RFC2-2, RFC2-23, RFC4-4, RFC5-16, RFC5-17, RFC6-27]
  policies: [CC-BAR-5, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-032]
```

### Requirement: PWB-REQ-005 — Consent and policy authority precede every body read

Group: Admission. Form: **prohibition**.

The POC SHALL NOT read any Butlers project-shape body until an exact
per-repository observation-consent record, a concrete secret-classification
policy and the project-shape observer's registered adapter entry all have
verifiable owner-act provenance. Their identities and versions SHALL be
evaluation inputs. Absence, mismatch, staleness or unverifiable provenance
SHALL produce zero body reads and a project-model Unknown.
The consent subject SHALL be the exact `(observing Syzygy project, configured
Butlers repository)` pair; a consent for another project, repository or content
class SHALL not match.

- **Case (counterexample sweep)**: provide absent, mismatched, stale,
  unverifiable and valid consent/policy/registry triples to an observer with an
  injected read spy.
- **Observable**: invalid triples yield zero read calls and fixed Unknown reasons;
  only the all-valid triple permits reads.
- **Oracle**: independently verify all three owner-act provenances, compare read
  calls and evaluation inputs across all cases.
- **Oracle independence**: authority fixtures and the read spy live outside
  the observer.
- **Falsifier**: any body is read before all three authorities verify, any
  identity is absent from the evaluation, or invalid authority yields a fact.

#### Scenario: Missing observation consent blocks content reads

- **WHEN** no lawful Butlers observation-consent record exists
- **THEN** the project-shape observer performs zero body reads
- **AND** the project model reports Unknown with the consent reason

```yaml
warrants:
  primary: SEC-5
  doctrine: [VIS-2, VIS-4, SEC-2, SEC-5]
  contracts: [RFC2-1, RFC3-7, RFC3-16, RFC3-30, RFC4-3, RFC4-7, RFC5-12, RFC5-16]
  policies: [CC-BAR-5, CC-SEC-5, CC-SEC-6, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```

### Requirement: PWB-REQ-006 — Project-shape content stays contained, inert and bounded

Group: Admission. Form: **prohibition**.

The POC SHALL read only exact Git objects addressed by normalized
repository-relative paths inside the consented repository. It SHALL NOT follow
absolute paths, traversal, NUL-bearing paths, working-tree symlinks or
submodules; execute observed content; or emit active Markdown, HTML, SVG,
scripts, event handlers or unsafe URL schemes. Declared source-count, byte,
depth, parse-time and rendered-output limits SHALL be evaluation inputs;
breaches SHALL leave the source counted and Unknown.

- **Case (counterexample sweep)**: exercise every prohibited path/content form
  and each declared limit with controlled sentinels.
- **Observable**: no request escapes the Git object reader, no active sentinel
  reaches a sink, and every rejected/limited source stays visible as Unknown.
- **Oracle**: injected Git/read/render spies plus complete sink-byte scans and
  limit-boundary cases decide.
- **Oracle independence**: malicious paths, content, limits and spies are
  supplied outside production parsing/rendering code.
- **Falsifier**: host filesystem access, submodule/symlink traversal, executed
  active content, unsafe URL output, an unbounded operation, or a vanished
  rejected source.

#### Scenario: Active repository content remains inert

- **WHEN** an admitted Markdown source contains raw active HTML or an unsafe URL
- **THEN** no active content reaches Polaris, JSON, logs, caches or records
- **AND** the affected source remains counted with an exclusion or Unknown reason

```yaml
warrants:
  primary: SEC-3
  doctrine: [VIS-1, VIS-2, VIS-7, SEC-3, SEC-5]
  contracts: [RFC2-1, RFC2-23, RFC4-4, RFC5-16, RFC5-17, RFC5-19]
  policies: [CC-BAR-5, CC-SEC-5, CC-SEC-6, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```

### Requirement: PWB-REQ-007 — Every project claim carries its complete epistemic state

Group: Truth. Form: **invariant**.

Every project-fact claim SHALL have a stable semantic Claim identity plus an
evaluation instance, be challengeable with resolvable support, and carry the
closed label, tier, exactly one primary reason, zero or more closed secondary
reasons, freshness, challenge state and evaluation identity that govern it.
Unknown reasons SHALL use RFC2-24 values verbatim and expose their resolution
routes. Aggregates SHALL disclose label, tier, freshness and separate primary/
secondary reason counts without a headline status, composite maturity or
inferred success. Default Polaris status presentation SHALL not render trends,
metric walls or count walls; coverage counts remain available on demand.

- **Case (sweep)**: enumerate every project-fact claim and aggregate at one
  evaluation, including fixtures for every admitted label, tier, reason and
  freshness value plus out-of-vocabulary and missing-currency cases.
- **Observable**: human and machine views expose identical complete tuples;
  invalid/missing currency stays Unknown and aggregates expand to members.
- **Oracle**: compare each tuple to independent literal vocabularies and
  provenance-verified currency inputs; exhaust identity stability, aggregate
  label/tier/freshness/reason counts and supports
  links; zero invalid, missing or folded values decides.
- **Oracle independence**: the checker hard-codes the accepted vocabularies and
  reads captured authority/evidence, importing no production vocabulary.
- **Falsifier**: a positive claim lacks current support, a tuple field is
  absent/out of vocabulary, a reason has no route, Unknown is folded into a
  total, or an aggregate claims its own headline status.

#### Scenario: Missing current evidence remains explicit Unknown

- **WHEN** a declared project fact lacks evidence under its current currency bound
- **THEN** its claim renders Unknown with the exact primary reason and route
- **AND** its tier, freshness and evaluation identity remain visible

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-1, VIS-2, VIS-7]
  contracts: [RFC1-18, RFC1-19, RFC1-24, RFC2-9, RFC2-10, RFC2-23, RFC2-24, RFC2-25, RFC6-14, RFC6-17, RFC7-16, RFC7-33]
  policies: [CC-BAR-3, CC-BAR-4, CC-TEST-5, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
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
  contracts: []
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
  contracts: [RFC7-1, RFC7-6, RFC7-13, RFC7-15]
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
  contracts: [RFC1-26, RFC3-27, RFC3-28, RFC6-20, RFC6-21, RFC7-13]
  policies: [CC-BAR-3]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-031]
```

### Requirement: PWB-REQ-012 — Owner-facing copy is direct and concise

Group: Presentation. Form: **prohibition**.

Every owner-visible Polaris string SHALL carry exactly one role from the closed
set `project-fact`, `epistemic-disclosure`, `action-label`,
`scope-instruction`. Headings SHALL contain at most six words and entry ledes
at most twenty. Heading, lede and notice strings SHALL NOT contain the
case-insensitive words `page`, `document`, `reading`, `section`, `movement` or
`presentation`. At most one entry `scope-instruction` may state the POC bound;
each interactive control may carry one `action-label`.

- **Case (counterexample + sweep)**: enumerate every owner-facing heading,
  lede, notice and explanatory sentence on Polaris, including a fixture with
  meta-narration.
- **Observable**: every string exposes one role; word limits, prohibited terms
  and cardinalities are recoverable in the machine and human outputs.
- **Oracle**: exhaust the owner-visible string population and apply the closed
  role, word, term and cardinality rules; zero violations decides the
  mechanical copy criterion. Cold-open comprehension is judged separately by
  PWB-REQ-021.
- **Oracle independence**: a plain DOM/text extractor with an independent word
  counter and prohibited-term set performs the sweep.
- **Falsifier**: an unclassified/multiply classified string, a limit breach, a
  prohibited term or an extra scope/action instruction.

#### Scenario: Section headings name project concepts

- **WHEN** Polaris renders the project-level entry
- **THEN** its headings name concepts such as purpose, boundaries,
  architecture, V1 scope, capabilities, evidence or gaps
- **AND** no heading describes a document movement or reading stage

```yaml
warrants:
  primary: VIS-3
  doctrine: [VIS-1, VIS-3]
  contracts: []
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
  contracts: [RFC1-14, RFC1-22, RFC1-25, RFC1-31, RFC7-14, RFC7-26]
  policies: [CC-BAR-5]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```

### Requirement: PWB-REQ-014 — Every narrative claim is bounded, anchored and non-authoritative

Group: Presentation. Form: **invariant**.

Every owner-visible narrative unit SHALL carry `presentation-artifact` and
`non-citable` attributes and exactly one claim role: anchored project fact,
explicitly non-normative framing, or epistemically labeled claim. Every
anchored claim block SHALL have a typed, revision-bound anchor set that covers
all its claims, contains no unused anchors and is small enough for a reader to
identify which anchor supports which claim. No project artifact, evidence,
snapshot input, work warrant or internal relation SHALL cite Polaris as its
authority. Each anchor SHALL retain the target's captured label, tier and
reason and SHALL not rewrite that target state on later reads. Narrative claim
blocks SHALL use a machine type distinct from kernel Claim. Personal view state
SHALL remain outside the truth model.

- **Case (sweep)**: enumerate every narrative unit, claim and anchor, then
  enumerate every citation/reference emitted by the Syzygy and Butlers source
  populations at the evaluated revisions.
- **Observable**: claim roles and non-authority attributes are machine-readable;
  every claim has exact/minimal anchors and no downstream authority reference
  targets Polaris.
- **Oracle**: independent claim-to-source mapping establishes covering and
  minimality and captured target state; removing any used anchor fails one
  claim and adding an unused anchor fails surplus; a later-read mutation cannot
  rewrite the captured state; a complete downstream-reference scan has zero
  Polaris authority targets.
- **Oracle independence**: expected source spans and reference targets come
  from captured artifacts, not the rendered claim blocks.
- **Falsifier**: an unclassified narrative unit, uncovered claim, surplus or
  ambiguous anchor, missing non-citable attribute, or downstream citation to
  Polaris.

#### Scenario: A project claim is supported without making Polaris authority

- **WHEN** Polaris states one project fact
- **THEN** the fact's bounded claim block identifies its exact source anchor
- **AND** both human and machine forms mark the block non-citable presentation

```yaml
warrants:
  primary: RFC7-2
  doctrine: [VIS-1, VIS-2, VIS-7]
  contracts: [RFC7-1, RFC7-2, RFC7-3, RFC7-5, RFC7-9, RFC7-10, RFC7-12, RFC7-29, RFC7-33]
  policies: [CC-BAR-3, CC-REV-3, CC-TEST-5]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-031]
```

### Requirement: PWB-REQ-015 — Capability detail preserves authority bands and exact intent

Group: Presentation. Form: **invariant**.

Every capability deep dive SHALL contain, in order, an `argument` band marked
non-normative, a `contract` band with verbatim current requirement/scenario,
governing doctrine and non-goal text, and a `reality` band sourced only from
the shared model. Draft capabilities SHALL remain unadopted. Proposed deltas SHALL be adjacent to current text,
visibly distinct, non-anchorable and unable to grant status; competing
proposals SHALL remain separate candidate futures.

- **Case (sweep)**: enumerate every capability deep dive at an evaluation that
  includes current intent, a draft capability and two incompatible proposals.
- **Observable**: band class/order, verbatim current text, proposal lifecycle,
  non-anchorability and separate futures are recoverable in both channels.
- **Oracle**: compare current requirement/scenario, doctrine and non-goal bytes
  to their owning artifacts, compare
  proposal identities/exclusivity to captured changes, and exhaust band and
  anchor populations; exact bytes/order and zero proposal authority decide.
- **Oracle independence**: current/proposed artifacts and exclusivity inputs
  come from captured OpenSpec state, not Polaris.
- **Falsifier**: a missing/misordered band, summarized normative text, draft
  rendered adopted, proposal substituted/interleaved/anchored/green, or
  competing proposals collapsed.

#### Scenario: Proposed work stays beside exact current intent

- **WHEN** a declared capability has an active proposal
- **THEN** the contract band renders current requirement text verbatim
- **AND** the proposal remains adjacent, distinct, non-anchorable and non-status-bearing

```yaml
warrants:
  primary: RFC7-17
  doctrine: [VIS-1, VIS-2, VIS-4]
  contracts: [RFC1-14, RFC1-27, RFC7-12, RFC7-13, RFC7-14, RFC7-15, RFC7-17, RFC7-18, RFC7-26, RFC7-27, RFC7-29, RFC7-33]
  policies: [CC-BAR-3, CC-BAR-5, CC-TEST-5]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```

### Requirement: PWB-REQ-016 — Project comprehension works without vision or a pointing device

Group: Evaluation. Form: **invariant**.

Every project distinction and summary-to-source path SHALL be recoverable by
text and operable by keyboard without relying on color, position or layout. A
nonvisual or keyboard-only cold-open walkthrough SHALL run for this material
narrative change, and its record SHALL identify that mode.

- **Case (sweep)**: traverse every disclosure, catalog, capability, anchor and
  exact-source path by keyboard and through the nonvisual representation, then
  perform the complete cold-open prompt set.
- **Observable**: every distinction has text, focus order reaches every target,
  no pointer-only action exists, and the walkthrough record names its mode.
- **Oracle**: compare the complete interactive/path population to keyboard and
  accessibility-tree traces, then apply PWB-REQ-021's prompt oracle.
- **Oracle independence**: DOM/accessibility-tree enumeration and input events
  come from a browser driver outside the renderer.
- **Falsifier**: a color/layout-only distinction, unreachable target, pointer-
  only action, keyboard trap, missing mode flag or failed cold-open path.

#### Scenario: Keyboard-only owner reaches exact intent

- **WHEN** the owner performs the material-change walkthrough without a pointing device
- **THEN** every prompt and exact-source path remains operable and understandable
- **AND** the retained run record identifies keyboard-only mode

```yaml
warrants:
  primary: RFC7-34
  doctrine: [VIS-1, VIS-3, VIS-7]
  contracts: [RFC7-30, RFC7-31, RFC7-32, RFC7-34]
  policies: [CC-BAR-3, CC-REV-4, CC-TEST-5]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-061]
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
  contracts: [RFC6-13, RFC6-14, RFC6-15, RFC6-22, RFC6-23, RFC7-1, RFC7-18, RFC7-33]
  policies: [CC-TEST-5]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-020]
```

### Requirement: PWB-REQ-021 — POC success includes whole-project cold-open comprehension

Group: Evaluation. Form: **event-response**.

WHEN the owner performs a cold-open Polaris walkthrough with no repository or
authoring context, the complete RFC7-30 prompt set SHALL remain mandatory. In
addition, POC success SHALL require the reader to explain Butlers' major
architecture and capability groups and its V1 success criteria. The retained
answer SHALL include why Butlers exists, what it promises and refuses, where
exact requirements live, one current Unknown or contradiction with its source,
and for one chosen fact how strongly Polaris claims to know it and what would
make that claim stronger.

- **Case**: an owner reads only Polaris at a named evaluation and answers the
  RFC7-30 prompts in their own words.
- **Observable**: a retained walkthrough execution record contains only the
  answers, paths, surface/evaluation identity and nonvisual/keyboard flag. A
  separate owner-judgment decision records verdict, rationale and judging party
  and references that execution record.
- **Oracle**: compare each answer to its authoritative Butlers artifact and
  exhaust the complete RFC7-30 prompt list plus the two project-wide additions;
  every prompt answered without a confident surface-caused error decides.
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
  contracts: [RFC7-25, RFC7-30, RFC7-31]
  policies: [CC-REV-4]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```

### Requirement: PWB-REQ-022 — Absent or unlawful owner judgment never becomes success

Group: Evaluation. Form: **prohibition**.

The POC SHALL NOT render the project-wide Polaris evaluation successful unless
a retained walkthrough execution record in `.syzygy/governance/records/` and a
lawful owner judgment in `.syzygy/governance/decisions/` both bind the exact
surface version and evaluation identity. Absent, stale or unverifiable judgment
SHALL render the criterion Unknown, never met.

- **Case (counterexample + sweep)**: evaluate absent, mismatched, stale and
  unverifiable judgment records plus one valid pair.
- **Observable**: the run record names surface version, evaluation identity,
  nonvisual/keyboard mode and paths; the judgment names verdict, rationale,
  judging party and run record. Only the valid pair may carry the owner's
  verdict; every invalid case records `verdict-unlawful` and renders Unknown.
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
