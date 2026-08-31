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
population to one opaque repository identity, approved locator mapping,
resolved Git object database and exact Git revision. It SHALL bind the signed
PWB source-grammar digest and superseding sign-off act; accepted RFC3/RFC4/
RFC5 trust-rule module digests and superseding owner-act identities;
authorization mode; consent, policy and registry artifact/act identities,
versions, digests and provenance states; source-discovery algorithm/version;
resource limits; observer/parser version; and the Phase-A-derived manifest
digest as deterministic evaluation inputs.

Human and machine readers SHALL receive those identities, the capture instant
and the same source population. Every emitted project-shape fact SHALL carry
its source identity, scope, capture instant, observer identity/version,
authorization mode and act basis. The manifest digest becomes an evaluation
input only after Phase A derives and independently validates it; no ambient or
prior manifest may substitute.

- **Case**: observe a controlled repository at one known revision through both
  authorization modes, including an alternate locator/object database, a
  source-claimed instant distinct from capture, and a mutated Phase-A manifest.
- **Observable**: Polaris and `/api/poc` expose identical repository, revision,
  source paths/count, capture instant, authorization inputs, discovery identity
  and validated manifest digest; substitutions and invalid manifests never
  enter Phase B.
- **Oracle**: compare repository identity, approved locator, object database,
  revision and Phase-A/Phase-B paths to an independent controlled Git tree;
  independently derive and digest the manifest from the literal signed grammar;
  exhaust every emitted fact's source, scope, capture, observer and
  authorization stamps. Exact set, digest, stamp and input equality decides.
- **Oracle independence**: the Git tree, source population, manifest extractor,
  digester and expected input tuple live outside the POC model, observer, parser
  and renderers.
- **Falsifier**: one source is absent or arbitrary, one deterministic input is
  missing, the two channels differ, Phase B uses an unvalidated manifest, or
  any source crosses locator, object-database or revision boundaries.

#### Scenario: Source population is complete at one revision

- **WHEN** Butlers is observed at revision R through a valid authorization mode
  and validated Phase-A manifest
- **THEN** every admitted project-shape source resolves from the approved object
  database at R
- **AND** human and machine views expose the same complete source set, manifest
  digest and authorization basis

```yaml
warrants:
  primary: VIS-7
  doctrine: [VIS-1, VIS-7, SEC-3]
  contracts: [RFC2-1, RFC4-1, RFC4-2, RFC4-3, RFC4-11, RFC6-15, RFC7-10]
  policies: [CC-SPEC-4, CC-TEST-3]
  decisions: [POLARIS-DIR-2026-08-31, TRUSTED-BOOTSTRAP-OBSERVATION-DIR-2026-08-31]
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

The POC SHALL perform zero Butlers project-shape body reads until it resolves
an exact observation-consent record, secret-classification policy and
registered project-shape adapter entry for the same
`(project:syzygy, repository:butlers-configured-poc)` subject.

Each artifact SHALL have a current, attributable owner act bound to its exact
digest. The authorization mode SHALL be `independently-verified` when all three
acts correlate through A1. Otherwise it SHALL be `owner-trusted-bootstrap` only
when every artifact has an exact digest-bound owner act, at least one act
remains uncorrelated, and the amended PWB behavior signed under
`TRUSTED-BOOTSTRAP-OBSERVATION-DIR-2026-08-31` permits that mode. No other
combination authorizes a read. Lack of independent correlation alone SHALL NOT
block the trusted mode and SHALL NOT be represented as independent
verification.

The consent record SHALL live in Syzygy's decisions plane and name the
observation class, exact subject, declared-project-shape content scope,
principal, grant instant and revocation state. The governing policy SHALL be
the observing Syzygy project's exact policy and SHALL apply before every ingest,
parse, store, log, surface, endpoint and record boundary. The registry entry
SHALL live in Syzygy's governance plane, name the same subject and declare
read-only Git authority with empty write, database, network, credential,
process-environment and observed-code-execution surfaces. The observer SHALL
NOT write, migrate or repair the observed repository or its governance plane.

Every artifact identity, version and digest; owner-act identity and provenance
state; A1 correlation identity or its explicit absence; authorization mode;
accepted RFC3/RFC4/RFC5 trust-rule module digests and their superseding owner
act identities; signed PWB source-grammar digest and superseding sign-off act;
source-discovery algorithm and version; opaque repository identity; approved
locator mapping; exact Git revision; and permitted Git object database SHALL be
deterministic evaluation inputs. Missing, mismatched, stale, revoked,
unattributed, wrong-subject, wrong-scope or effect-widening authority SHALL
produce zero body reads and a project-model Unknown.

When `owner-trusted-bootstrap` is active, Polaris SHALL show the persistent
project-account notice “Observation uses owner-trusted records; independent
audit is not configured.” Each affected claim SHALL expose the same basis on
demand, and `/api/poc` SHALL carry the authorization mode, act identities,
artifact digests and uncorrelated provenance state on every admitted
project-shape fact. Neither channel may label that basis verified or infer a
positive security, conformance, release or certification claim from it.

After authority admission, discovery SHALL run within one identified
evaluation at one exact Git revision in two phases. Phase A SHALL read only the
exact Git object for the Butlers path “about/README.md”, then only the README
index under each of the five normalized pillar roots that index declares, plus
Git-tree metadata needed to enumerate baseline `openspec/specs/*/spec.md` paths
and top-level `roster/*/butler.toml` and corresponding `MANIFESTO.md`
candidates. Narrative links SHALL NOT recurse. The secret policy SHALL screen
each transient body before parsing; raw bodies SHALL never be stored, logged,
rendered or returned.

Phase A SHALL emit a revision-bound manifest containing normalized
repository-relative paths, Git object identities, extraction classes, the
source-discovery version and a manifest digest. The manifest is derived
evaluation data, not a separate authorization artifact: the owner acts bind the
signed grammar and discovery algorithm, while the manifest digest becomes an
evaluation input after derivation. Phase B SHALL begin only after an independent
validator confirms that the manifest exactly satisfies the signed PWB grammar
at the same repository identity, revision and object database. Phase B SHALL
read only exact Git objects named by that manifest. A Phase-A parse,
containment, limit or manifest-validation failure SHALL produce zero Phase-B
body reads and a project-model Unknown; it does not erase already admitted
Phase-A read calls. PWB-REQ-006 applies to both phases.

Revocation or supersession SHALL stop new reads at the next evaluation. Prior
observation records remain immutable and visibly withdrawn or stale. No later
act retroactively authorizes an earlier read.

- **Case (counterexample sweep)**: for each artifact and act, exercise absent,
  mismatched, stale, revoked, unattributed, wrong-subject, wrong-scope and
  digest-mismatch cases; exercise valid all-A1, all-uncorrelated and mixed
  A1/uncorrelated tuples; exercise every non-empty authority surface; then, for
  each valid mode, exercise Phase-A seed widening, recursive-link widening,
  malformed discovery output, manifest/revision/object-database mismatch and
  Phase-B path widening with separate injected phase read spies.
- **Observable**: every invalid authority tuple yields zero Phase-A and Phase-B
  body calls and a fixed Unknown reason; both valid modes permit only the exact
  Phase-A seed set and validated Phase-B manifest; a Phase-A or manifest failure
  yields zero Phase-B calls; trusted mode is identical across human and machine
  views and is never rendered as verified.
- **Oracle**: independently compare artifact bytes and digests, act fields,
  subjects, scopes, lifecycle states, A1 correlations, adapter authority and
  mode derivation. Derive the expected Phase-A set from the literal signed
  grammar and controlled Git tree, derive the expected manifest with an
  independent extractor, and compare both phase spies, evaluation inputs and
  every human/machine provenance marker. Exact equality, zero out-of-set reads
  and the phase-specific zero-read rules decide.
- **Oracle independence**: authority fixtures, literal authorization-mode
  vocabulary, expected discovery algorithm, independent manifest extractor,
  controlled Git tree and both read spies live outside the observer, production
  parser and renderers.
- **Falsifier**: any body read under invalid authority; incorrect mode
  selection; a missing deterministic input; a trusted basis hidden or called
  verified; a Phase-A read outside the closed seed algorithm; a Phase-B read
  before manifest validation or outside the manifest; cross-revision,
  alternate-locator or alternate-object-database substitution; raw-body
  persistence; or admission of any non-read authority.

#### Scenario: Owner-trusted bootstrap acts permit read-only observation

- **WHEN** every matching consent, policy and empty-authority registry artifact
  has a current exact digest-bound owner act and at least one act remains
  uncorrelated
- **THEN** the two-phase observation may run in `owner-trusted-bootstrap` mode
  at one exact Git revision
- **AND** Polaris and `/api/poc` disclose the owner-trusted, uncorrelated basis
  without calling it verified

#### Scenario: A1-correlated acts render independently verified

- **WHEN** all three matching owner acts correlate through A1
- **THEN** the same bounded observation may run in independently-verified mode
- **AND** the trusted-bootstrap notice is absent

#### Scenario: Invalid authority blocks before discovery

- **WHEN** any required artifact or act is absent, mismatched, stale, revoked,
  unattributed, wrong-subject, wrong-scope or effect-widening
- **THEN** both discovery phases perform zero body reads
- **AND** the project model reports Unknown with the exact failed gate and
  resolution route

#### Scenario: Discovery failure blocks manifest reads

- **WHEN** valid authority admits Phase A but its seed parsing or derived
  manifest fails the signed grammar, containment, revision or limit checks
- **THEN** Phase B performs zero body reads
- **AND** the project model reports Unknown without claiming a complete source
  population

```yaml
warrants:
  primary: SEC-5
  doctrine: [VIS-1, VIS-2, VIS-4, VIS-7, SEC-2, SEC-3, SEC-5]
  contracts: [RFC1-3, RFC2-1, RFC2-23, RFC3-7, RFC3-8, RFC3-16, "RFC3-16(a)", "RFC3-16(c)", RFC3-30, RFC4-3, RFC4-7, RFC4-11, RFC5-12, RFC5-13, RFC5-16, RFC5-17, RFC5-19, RFC6-13, RFC6-22, RFC7-33]
  policies: [CC-BAR-5, CC-SEC-5, CC-SEC-6, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31, TRUSTED-BOOTSTRAP-OBSERVATION-DIR-2026-08-31]
  topology: []
  parent_requirements: []
```

### Requirement: PWB-REQ-006 — Project-shape content stays contained, inert and bounded

Group: Admission. Form: **prohibition**.

Both discovery phases SHALL read only exact Git objects addressed by normalized
repository-relative paths within the consented opaque repository, approved
locator, resolved object database and one exact revision. Phase A SHALL stay
inside PWB-REQ-005's closed seed algorithm; Phase B SHALL start only after
independent manifest validation and stay inside that manifest.

Neither phase SHALL follow absolute paths, traversal, NUL-bearing paths,
working-tree files, symlinks, submodules, filters, credential helpers,
environment-selected locators, alternate object databases or remote fetches;
execute observed content; or emit active Markdown, HTML, SVG, scripts, event
handlers or unsafe URL schemes. The secret policy SHALL screen transient bytes
before parsing in both phases. Declared source-count, byte, depth, parse-time
and rendered-output limits SHALL be evaluation inputs; breaches SHALL keep the
affected source visible and Unknown.

- **Case (counterexample sweep)**: exercise every prohibited path, object
  database, revision, Git helper/filter/fetch and active-content form plus each
  limit; include valid authority followed by malformed Phase-A output and
  manifest validation failure.
- **Observable**: no request escapes the phase-specific Git object reader; no
  prohibited helper, fetch, execution or active sentinel runs or reaches a
  sink; rejected/limited sources remain visible; invalid authority yields zero
  Phase-A/Phase-B calls, while Phase-A/manifest failure yields zero Phase-B
  calls.
- **Oracle**: separate injected Phase-A and Phase-B read spies, Git helper/
  fetch/execute spies, independent manifest validator, complete sink-byte scans
  and every limit boundary decide.
- **Oracle independence**: malicious paths, repositories, object databases,
  manifests, content, limits and spies are supplied outside production
  discovery, parsing and rendering code.
- **Falsifier**: host working-tree access, alternate locator/object database,
  cross-revision read, submodule/symlink/traversal, Git helper/filter/fetch,
  observed execution, unsafe output, an unbounded operation, a vanished rejected
  source or any Phase-B call after failed manifest validation.

#### Scenario: Active repository content remains inert

- **WHEN** either phase encounters raw active HTML, an unsafe URL or secret
  sentinel in an otherwise admitted Markdown source
- **THEN** no active or secret content reaches Polaris, JSON, logs, caches or
  records
- **AND** the affected source remains counted with its exclusion or Unknown
  reason

#### Scenario: Invalid manifest blocks Phase B

- **WHEN** valid authority admits Phase A but the derived manifest changes
  locator, object database, revision, path scope or signed grammar
- **THEN** Phase B performs zero body reads
- **AND** the project model remains Unknown with the failed validation route

```yaml
warrants:
  primary: SEC-3
  doctrine: [VIS-1, VIS-2, VIS-7, SEC-3, SEC-5]
  contracts: [RFC2-1, RFC2-23, RFC4-4, RFC5-16, RFC5-17, RFC5-19]
  policies: [CC-BAR-5, CC-SEC-5, CC-SEC-6, CC-TEST-6]
  decisions: [POLARIS-DIR-2026-08-31, TRUSTED-BOOTSTRAP-OBSERVATION-DIR-2026-08-31]
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
- **Oracle**: compare every run-record field, every judgment field, exact
  `verdict-unlawful` state, record identities and owner-act provenance to the
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
