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
  sections; `catalog-entry` uses each top-level named entry under the V1 Core
  Infrastructure, Staffers, Butlers, Modules, Connectors, Dashboard, Identity System,
  Situational Awareness and Observability headings; `design-contract` uses each
  RFC index-table identity; `baseline-spec` uses each baseline spec directory;
  `topology-component` uses each first-column identity in the component tables;
  `craft-policy` uses each policy-file identity in the craft index; and
  `roster-identity` uses each top-level roster directory containing
  butler.toml. No other prose, heading, link or file mints an item.
- Stable item identity is `(item class, declared key)`. Repository-relative path
  and content hash are source-anchor state, never identity. A duplicate key in
  one class is a contradiction rather than a path-based disambiguation.
- The extraction grammar is literal:
  - `project-account-section` mints exactly six aggregate keys: purpose from
    vision.md H2 “What Butlers Is”; promises from vision.md H2 “What Success
    Looks Like”; refusals from vision.md H2 “What Butlers Is Not”; architecture
    from every H2 in architecture.md; V1 scope from v1.md H2 “What v1 Ships”
    and “What v1 Defers”; V1 success from v1.md H2 “Success Criteria”.
  - `principle` is each top-level decimal-list item under vision.md H2
    “Non-Negotiable Rules”; its literal leading bold phrase is the key.
  - `success-criterion` is each top-level list item under vision.md H2 “What
    Success Looks Like” (`vision:<one-based ordinal>`) and v1.md H2 “Success
    Criteria” (`v1:<one-based ordinal>`).
  - `catalog-entry` is each top-level unordered-list item beneath the exact V1
    H3 headings Core Infrastructure, Staffers, Butlers, Modules, Connectors,
    Dashboard, Identity System, Situational Awareness and Observability; the
    leading bold or code span before the first dash is the literal key.
  - `design-contract` is each body row under the Index table in the Legends and
    Lore README; the first-column RFC link text is the key.
  - `baseline-spec` is each Git-tree path matching
    openspec/specs/<one-directory>/spec.md; the one directory is the key.
  - `topology-component` is each first-column bold label in tables under an H2
    in lay-and-land/components.md whose text begins with a decimal plus optional
    lowercase suffix. The H2 establishes the literal ordinal context but mints
    no item itself; key is `<H2 ordinal>:<literal first-column label>`.
  - `craft-policy` is each body row in the Craft and Care README “Reading
    Order” table; the File-column link target basename is the key.
  - `roster-identity` is each Git-tree path roster/<one-directory>/butler.toml;
    the directory is the key and the TOML `[butler].name` must be non-empty.
  Heading levels/text, top-level list depth, table column counts, one-based
  ordinals and literal keys are exact. Unicode is NFC-normalized; no case
  folding, stemming or punctuation rewriting occurs. A missing heading,
  malformed row/list/TOML, unexpected duplicate key or ambiguous leading label
  makes the enclosing source's item denominator Unknown; it never produces a
  partial item set.
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
  and roster population are known independently, including a source-claimed
  instant distinct from the capture instant.
- **Observable**: the machine answer and Polaris expose the revision, source
  paths, source count, capture instant and every deterministic input and
  per-emission identity.
- **Oracle**: compare the exposed paths and revision to an independent Git tree
  listing and the closed discovery rules; exhaust every emitted fact's source,
  scope, capture-instant and observer-version stamp; verify capture time remains
  distinct from source-claimed time. Exact set, stamp and input-identity
  equality decides.
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
- **Oracle**: two independent extractors apply the literal grammar to the
  revision-bound source population and must produce the same identities and D;
  modeled + Unknown + contradicted equals D, with each identity appearing once;
  malformed/unreadable sources carry an Unknown item denominator.
- **Oracle independence**: the expected denominator is extracted from the
  source files, not from the POC's coverage object.
- **Falsifier**: the independent extractors disagree, a malformed source emits
  a partial population, a known source disappears, an admitted item appears twice or
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

The POC SHALL NOT read any Butlers project-shape body until each of the exact
per-repository observation-consent record, the observing Syzygy project's
concrete secret-detection/classification policy and the project-shape
observer's governance-plane adapter-registry entry carries an effective human
owner act under RFC3-16(a), bound under RFC3-16(b) to the artifact's exact
digest, identity, act type, project and scope. Each act SHALL be accepted in
state (1), `owner-adopted (bootstrap, uncorrelated)`, or state (2),
`Syzygy-verified`. The three states SHALL be evaluated independently, and an
all-valid triple SHALL admit reads whether its states are equal or mixed.
Specification sign-off, tree attribution, a Git commit or tag, a machine
submission or an agent assertion SHALL NOT substitute for any act.

Each authority artifact identity and digest, act-record identity, act type and
scope, provenance state, and A1 audit-record identity or explicit absence SHALL
be an evaluation input. Every human and machine rendering of the authorization
basis and every dependent body-derived result SHALL expose each authority's
exact state. Only state (2) MAY be called independently verified. State (1)
SHALL render exactly: `Owner-trusted only; same-tree forgeable from Syzygy's
perspective. Digest detects drift, not authorship or attendance.`

A state-(1) act SHALL be valid only when the human act explicitly selected
state (1) and records the A1 audit-record identity as absent. A record claiming
state (2) whose correlation is failed, unavailable or indeterminate SHALL be
invalid and SHALL NOT downgrade to state (1).

The closed invalid-case population SHALL contain exactly 195 independently
decided cases. “Malformed” below means type- or shape-invalid; “wrong but
present” means well-formed but semantically different from the controlled
evaluation input.

| Case group | Required independent cases | Count |
|---|---|---:|
| RFC3-16(b) binding fields, per consent/policy/registry act | For each of project identity, stable artifact identity, exact digest, act type, act instant, scope, supersession/revocation target and A1 identity-or-explicit-absence: missing, malformed and wrong but present. Owner attribution has four independent cases: missing, malformed, another human and a non-human principal. Wrong instant includes a future instant; wrong A1 includes a mismatched but present identity. | 28 × 3 acts = 84 |
| Evaluation association, per act | Act-record identity missing, malformed or wrong but present; act paired to a different authority artifact. | 4 × 3 acts = 12 |
| Provenance-state input, per act | Missing; malformed; well-formed but outside the two-state vocabulary. | 3 × 3 acts = 9 |
| False substitutes, per act | Tree attribution only; Git commit/tag only; specification sign-off only; machine submission; agent assertion. | 5 × 3 acts = 15 |
| Lifecycle, per act | Stale; expired; superseded; revoked. | 4 × 3 acts = 12 |
| Provenance-state mechanics, per act | State (1) not explicitly selected; state (1) with a non-absent A1 identity; claimed state (2) with failed, unavailable or indeterminate correlation. | 5 × 3 acts = 15 |
| State-(1) record semantics, per act | Exact owner phrase missing, malformed or mismatched; recording commit/tag missing, malformed or mismatched. These cases validate trusted record semantics and never claim to prove attendance. | 6 × 3 acts = 18 |
| Consent-specific fields | For observing project, configured repository and observation content class: missing, malformed and wrong but present. | 9 |
| Policy-specific fields | For policy-owning project and policy version: missing, malformed and wrong but present. | 6 |
| Registry-specific fields | For governance home, project, repository, read-only authority and empty write surface: missing, malformed and wrong but present. | 15 |
| **Total** | **Every case above, no “other invalid” bucket.** | **195** |

The first seven groups form the closed common owner-act population of 55 cases
per act. The last three groups add 30 authority-specific cases.

Any one of those 195 cases in any limb SHALL produce zero body reads, a
project-model Unknown and the RFC3-16(a) contradiction while retaining the
authority artifact and invalid act state visibly.

The consent subject SHALL be exactly `(observing Syzygy project, configured
Butlers repository)` with the observation content class. The policy SHALL be
the observing project's own exact policy. The registry entry SHALL live in
Syzygy's governance plane, name that same pair and declare read-only authority
with an empty write surface. These acts warrant only use of their exact
consent, policy and registration. They are never evidence that a read occurred,
screening succeeded, admitted content is secret-free or a derived claim is
true. Later A1 correlation MAY change a later evaluation to state (2), but
SHALL NOT rewrite the state under which an earlier read occurred.

- **Case (state and invalid-arm sweep)**: exercise all eight valid
  state-(1)/state-(2) consent/policy/registry triples, all 195 invalid cases
  above and later correlation of a prior state-(1) act, using an injected read
  spy; report all three denominators separately.
- **Observable**: any invalid limb yields zero read calls, Unknown and the
  contradiction; state-(1), state-(2) and mixed all-valid triples permit reads;
  the per-authority states and state-(1) disclosure are identical in the human
  surface and machine answer; later correlation leaves the earlier evaluation
  recorded as state (1).
- **Oracle**: compare a hard-coded expected table, every RFC3-16(b) field,
  explicit A1 identity or absence, registry home/pair/scope/write-surface,
  evaluation inputs, disclosures and read-spy calls across all cases.
- **Oracle independence**: the expected table, authority fixtures and read spy
  live outside the observer and do not import its validator or state
  vocabulary; for state (1), the oracle verifies record semantics and
  disclosure without claiming to prove human attendance.
- **Mutation proof**: for each of the 195 invalid case instances, temporarily
  mutate the implementation to permit the read or suppress Unknown or the
  contradiction and confirm the independent test fails before restoration.
  Separately mutate exact state, exact disclosure, failed-state-(2)
  no-fallback and prior-evaluation history one predicate at a time and retain
  fail-then-restore evidence.
- **Falsifier**: any body is read or fact emitted before all three acts are
  effective; valid state (1) or a mixed triple is rejected; an invalid or
  failed-state-(2) act is accepted or downgraded; a state is hidden, collapsed
  or calls state (1) verified; a digest or tag is treated as attendance proof;
  an act is treated as read, screening or truth evidence; or the registry
  declares a non-empty write surface.

#### Scenario: Missing observation consent blocks content reads

- **WHEN** no effective Butlers observation-consent act exists
- **THEN** the project-shape observer performs zero body reads
- **AND** the project model reports Unknown with the consent reason

#### Scenario: State-(1) authorities permit reads with the trust gap visible

- **WHEN** all three exact authorities carry valid state-(1) human owner acts
- **THEN** the project-shape observer may perform the bounded body reads
- **AND** both surfaces expose every state as owner-adopted and the exact
  same-tree-forgeability disclosure

#### Scenario: Mixed valid authority states permit reads

- **WHEN** the exact consent, policy and registry acts are all valid but use a
  mixture of state (1) and state (2)
- **THEN** the project-shape observer may perform the bounded body reads
- **AND** both surfaces preserve each authority's distinct exact state

#### Scenario: Failed state-(2) correlation blocks without fallback

- **WHEN** any authority claims state (2) and its A1 correlation fails
- **THEN** the project-shape observer performs zero body reads
- **AND** the invalid act does not downgrade to state (1)

#### Scenario: Later correlation preserves prior authorization history

- **WHEN** a later evaluation correlates an authority previously used in
  state (1)
- **THEN** the later evaluation may render that authority in state (2)
- **AND** the earlier evaluation remains recorded as state (1)

```yaml
warrants:
  primary: SEC-5
  doctrine: [VIS-2, VIS-4, SEC-2, SEC-5]
  contracts: [RFC2-1, RFC3-7, RFC3-16, "RFC3-16(a)", "RFC3-16(b)", "RFC3-16(c)", RFC3-30, RFC4-3, RFC4-7, RFC5-12, RFC5-16]
  policies: [CC-BAR-5, CC-SEC-5, CC-SEC-6, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31, PWB-STATE1-AMENDMENT-DIR-2026-09-02]
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

Every project entity and project-fact claim SHALL have a stable semantic Claim
identity plus an evaluation instance, be challengeable with resolvable support, and carry the
closed label, tier, exactly one primary reason, zero or more closed secondary
reasons, freshness, challenge state and evaluation identity that govern it.
Unknown reasons SHALL use RFC2-24 values verbatim and expose their resolution
routes. Aggregates SHALL disclose label, tier, freshness and separate primary/
secondary reason counts without a headline status, composite maturity or
inferred success. Default Polaris status presentation SHALL not render trends,
metric walls or count walls; coverage counts remain available on demand.

- **Case (sweep)**: enumerate every project entity, claim and aggregate across
  two evaluations of the same semantic subjects, including fixtures for every
  admitted label, tier, reason, freshness, challenge and sibling state plus
  out-of-vocabulary and missing-currency cases.
- **Observable**: human and machine views expose identical complete tuples;
  invalid/missing currency stays Unknown and aggregates expand to members.
- **Oracle**: compare each tuple and tier meaning to independent literal
  vocabularies and provenance-verified currency inputs; verify stable semantic
  identity across the two evaluation instances; exhaust challenge/sibling
  separation, aggregate label/tier/freshness/reason counts and supports links;
  zero invalid, missing or folded values decides.
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
Anchor targets SHALL use the closed classes doctrine, contract, requirement,
decision, evidence and work with durable target identity; labels, file paths
and coordinates SHALL never serve as anchor identity.

- **Case (sweep)**: enumerate every narrative unit, claim and anchor, then
  enumerate every citation/reference emitted by the Syzygy and Butlers source
  populations at the evaluated revisions. Repeat after deleting Polaris
  presentation and after injecting personal view state and a later-read target
  mutation.
- **Observable**: claim roles and non-authority attributes are machine-readable;
  every claim has exact/minimal anchors and no downstream authority reference
  targets Polaris.
- **Oracle**: independent claim-to-source mapping establishes covering,
  minimality, closed target class, durable identity, exact narrative-vs-kernel
  machine type and captured target state; removing any used anchor fails one
  claim and adding an unused anchor fails surplus; a later-read mutation cannot
  rewrite the captured state; a complete downstream-reference scan has zero
  Polaris authority targets; deletion leaves truth unchanged and injected
  personal state never enters the truth model.
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
The default reading mode SHALL be `Base` and include observed reality. Every
block SHALL carry exactly one of the three band-class attributes. No
reorganized or stored normative copy of doctrine, non-goal, requirement or
scenario text SHALL exist outside its owning artifact.

- **Case (sweep)**: enumerate every capability deep dive at an evaluation that
  includes current intent, a draft capability and two incompatible proposals.
- **Observable**: Base mode, band class/order, verbatim current text, proposal lifecycle,
  non-anchorability and separate futures are recoverable in both channels.
- **Oracle**: compare current requirement/scenario, doctrine and non-goal bytes
  to their owning artifacts, compare
  proposal identities/exclusivity to captured changes, exhaust band and anchor
  populations and perform a static-source sweep for normative copies; exact
  bytes/order, exactly one class per block, zero stored copies and zero proposal
  authority decide.
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
denominator, contradiction, body-read authority state and walkthrough-judgment
state or disclosure Polaris presents SHALL be recoverable from the same
evaluation in the machine answer, preserving multiplicity and exact provenance
state.

- **Case (sweep)**: enumerate every project-shape parity marker on Polaris and
  every corresponding machine-answer fact at one evaluation, including every
  PWB-REQ-005 authority state and PWB-REQ-022 judgment state and disclosure.
- **Observable**: both populations contain equivalent multisets.
- **Oracle**: an independent order-insensitive, multiplicity-preserving
  comparator reports both denominators and zero differences.
- **Oracle independence**: the comparator extracts each channel separately and
  imports no production vocabulary or rendering code.
- **Mutation proof**: for each fact, authority-state, judgment-state and
  disclosure marker class, independently inject a missing, duplicated,
  changed, collapsed and wrong-evaluation marker and confirm the comparator
  fails before restoration; report both channel denominators for every run.
- **Falsifier**: one fact, authority state, judgment state or disclosure is
  missing, duplicated, changed, collapsed or associated with a different
  evaluation in either channel.

#### Scenario: Complete model has wire parity

- **WHEN** Polaris renders a project-wide evaluation
- **THEN** the complete human fact multiset equals the machine fact multiset
- **AND** the check reports both denominators, including the authorization and
  judgment provenance markers

```yaml
warrants:
  primary: RFC6-22
  doctrine: [VIS-1, VIS-7]
  contracts: ["RFC3-16(c)", RFC6-13, RFC6-14, RFC6-15, RFC6-22, RFC6-23, RFC7-1, RFC7-18, RFC7-33]
  policies: [CC-TEST-5]
  decisions: [POLARIS-DIR-2026-08-31, PWB-STATE1-AMENDMENT-DIR-2026-09-02]
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
separate owner judgment in `.syzygy/governance/decisions/` both bind the exact
walkthrough-record identity, surface version and evaluation identity. The run
record SHALL name the surface version, evaluation identity,
nonvisual/keyboard-only mode and traversed paths. The judgment SHALL name the
verdict, rationale, judging party and exact run record, and SHALL carry an
effective human owner act under RFC3-16(a) satisfying RFC3-16(b). The act SHALL
be accepted in state (1), `owner-adopted (bootstrap, uncorrelated)`, or state
(2), `Syzygy-verified`.

Every human and machine rendering of the criterion SHALL expose the exact act
state. Only state (2) MAY be called independently verified. State (1) SHALL
render exactly: `Owner-trusted only; same-tree forgeable from Syzygy's
perspective. Digest detects drift, not authorship or attendance.` State (1)
SHALL require explicit human selection and explicit A1 audit-record absence.
Failed, unavailable or indeterminate state-(2) correlation SHALL be invalid
and SHALL NOT downgrade to state (1).

The execution-record identity, judgment artifact identity and digest,
act-record identity, act type and scope, provenance state, and A1 audit-record
identity or explicit absence SHALL be evaluation inputs.

The closed judgment-case population SHALL contain exactly 84 present-invalid
cases plus 2 absent cases. “Malformed” and “wrong but present” have the same
meanings as in PWB-REQ-005.

| Case group | Required independent cases | Count |
|---|---|---:|
| RFC3-16(b), association, provenance-state input, false-substitute, lifecycle, state-mechanics and state-(1)-record cases | Apply PWB-REQ-005's exact 55-case common population to the judgment act, including separate another-human/non-human owner cases, complete act-record identity and provenance-state cases, exact state-(1) owner phrase and recording context, stable artifact identity, instant, supersession target and A1 identity. | 55 |
| Run-record fields | For each of run-record identity, surface version, evaluation identity, nonvisual/keyboard-only mode and traversed paths: missing, malformed and wrong but present. | 15 |
| Judgment fields | For each of verdict, rationale, judging party and exact run-record reference: missing, malformed and wrong but present. | 12 |
| Governance homes | Run record outside `.syzygy/governance/records/`; judgment outside `.syzygy/governance/decisions/`. | 2 |
| **Present-invalid total** | **Every present invalid case above.** | **84** |
| Absent cases | No run record; no judgment. | 2 |

Either absent case SHALL render Unknown, never met, without inventing a
verdict. Any of the 84 present-invalid cases SHALL record
`verdict-unlawful`, render Unknown-never-met and mint or retain the
RFC3-16(a) contradiction. The owner act warrants honoring the judgment;
neither the act, its digest, its correlation nor the run record is evidence
that comprehension succeeded. The verdict remains recorded human judgment,
never Observed and never a score. Tests, code, an agent report or page
availability SHALL NOT substitute. Later correlation SHALL NOT rewrite the
provenance under which an earlier judgment took effect.

- **Case (state and invalid-arm sweep)**: exercise valid state (1), valid state
  (2), all 84 present-invalid cases, both absent cases and later correlation of
  a prior state-(1) judgment; report the valid, present-invalid and absent
  denominators separately.
- **Observable**: absence yields Unknown-never-met without a fabricated
  verdict; a present invalid judgment records exact `verdict-unlawful`; valid
  state-(1) and state-(2) judgments may carry the owner's verdict with exact
  state; the state-(1) disclosure is identical in the human surface, machine
  answer; later correlation preserves the earlier state history.
- **Oracle**: compare controlled run, judgment and act fixtures to a hard-coded
  expected table outside the surface and provenance validator, including every
  field, record identity, state, disclosure and `verdict-unlawful` value.
- **Oracle independence**: the expected table and fixtures do not import the
  production validator or state vocabulary; for state (1), the oracle checks
  record semantics and disclosure without claiming to prove human attendance.
- **Mutation proof**: for each of the 84 present-invalid cases, temporarily
  mutate the implementation to carry the owner verdict or render success and
  confirm the independent test fails before restoration. Mutate each absent
  case to fabricate a verdict, then mutate exact state, disclosure,
  failed-state-(2) no-fallback and prior-evaluation history one predicate at a
  time; every mutation SHALL fail before restoration and retain evidence.
- **Falsifier**: an absent or invalid pair renders successful; valid state (1)
  is rejected; a state is hidden or state (1) called verified; absence
  fabricates a verdict; failed state (2) downgrades; implementation, tests,
  reports or availability substitute for judgment; an act or run record is
  presented as success evidence; or historical provenance is rewritten.

#### Scenario: Missing judgment remains Unknown

- **WHEN** no lawful owner judgment exists for the exact walkthrough record
- **THEN** the POC reports the Polaris evaluation criterion as Unknown
- **AND** it does not substitute implementation or test evidence for judgment

#### Scenario: Lawful state-(1) judgment is honored with the trust gap visible

- **WHEN** the exact walkthrough pair carries a valid state-(1) owner judgment
- **THEN** the POC may carry the owner's recorded verdict
- **AND** both surfaces expose the state as owner-adopted with the exact
  same-tree-forgeability disclosure

#### Scenario: Lawful state-(2) judgment is independently verified

- **WHEN** the exact walkthrough pair carries a valid state-(2) owner judgment
- **THEN** the POC may carry the owner's recorded verdict
- **AND** both surfaces expose the state as Syzygy-verified

#### Scenario: Invalid claimed state-(2) judgment stays unlawful

- **WHEN** the judgment claims state (2) and its A1 correlation fails
- **THEN** the POC records `verdict-unlawful` and Unknown-never-met
- **AND** the judgment does not downgrade to state (1)

#### Scenario: Later correlation preserves prior judgment history

- **WHEN** a later evaluation correlates a judgment previously honored in
  state (1)
- **THEN** the later evaluation may render that judgment in state (2)
- **AND** the earlier evaluation remains recorded as state (1)

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-2, VIS-4]
  contracts: [RFC2-1, RFC3-15, RFC3-16, "RFC3-16(a)", "RFC3-16(b)", "RFC3-16(c)", RFC7-31]
  policies: [CC-BAR-4, CC-TEST-2]
  decisions: [POLARIS-DIR-2026-08-31, PWB-STATE1-AMENDMENT-DIR-2026-09-02]
  topology: []
  parent_requirements: []
```
