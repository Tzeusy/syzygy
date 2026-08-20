## Purpose

Lets an owner register a software project with Syzygy and read its shape
honestly: every answer stands on its own, every Unknown carries its
reason and owning authority, and humans and machines receive the same
facts — without registration ever being mistaken for certification.

## ADDED Requirements

Reader notes, binding on how this file is read:

- **Subject.** "Syzygy" names the system under specification. A "human
  view" is any rendering a person reads; a "machine answer" is any
  response served to a machine client through the machine-queryable
  plane (RFC6-13). Both are observation points for every oracle below.
- **Groups.** Requirements are organized into six literal groups, named
  in each requirement's `Group` line: *Project declaration* (001–006),
  *Consent and coverage* (010–016), *Human project entry* (020–023),
  *Independent project-shape answers* (030–038), *Why this answer and
  human/machine parity* (040–046), *Repository discoverability*
  (050–053), plus *Cross-cutting* (060–064). Identifiers are stable and
  literal: minted once, amended in place, retired rather than reused,
  never renumbered (CC-SPEC-3). Gaps in the numbering are deliberate.
- **Warrants.** Each requirement ends with a machine-readable
  `warrants` block naming all its material governing authorities in
  CC-SPEC-2's six classes. `decisions` entries cite recorded owner
  decisions by identifier (`SDR-n`, or a ruled `P-nn` with its record
  file). Empty fields assert reliance on nothing of that kind. The
  specification-level declaration is generated as the union of these
  blocks (CC-IMPACT-1) by `scripts/build_capability_1_spec_dependencies.py`
  into `GOVERNING-DEPENDENCIES.md`; no second hand-maintained list
  exists. The owner's 2026-08-20 authoring authorization is never cited
  as a warrant.
- **Vocabulary.** `Unknown` and `Gap` follow the owner-ruled two-term
  rule (SDR-35): no verifying evidence → `Unknown`; evidence of
  non-satisfaction → `Gap`. Every `Unknown` carries a primary reason
  verbatim from the closed twelve-reason vocabulary (RFC2-24). An
  "identified evaluation" is the pair (source snapshot, as-of instant).
- **Deterministic layer.** Where a requirement speaks of the
  "deterministic layer" of a served answer, it means the answer's fact
  content — which facts, values, epistemic labels, reasons, identities,
  and evaluation stamps exist — with **only display formatting
  excluded** (RFC6-7, RFC6-15). A served wall-clock timestamp of the
  serving itself, or a per-request identifier, is display-layer
  material; every fact about the project is deterministic-layer.
- **Scenario context.** The third coordinate of RFC6-18's fact-set key
  (selection, evaluation, scenario context) functions in this
  specification as an opaque key: the declared condition set under which
  the selection is evaluated. Two requests share a scenario context
  exactly when their declared condition sets are equal, and the parity
  and determinism obligations below apply between requests whose three
  coordinates all match.

### Requirement: CAP1-REQ-001 — A valid declaration registers exactly one project

Group: Project declaration. Form: **event-response**.

WHEN Syzygy reads a project declaration file `.syzygy/project.yaml` at
the root of a repository, and the declaration is valid against the
closed declaration field set (RFC3-5), Syzygy SHALL produce exactly one
registered project, identified by the declaration's opaque project
identifier, with that repository designated the governance root by the
file's location (RFC3-4) — never by any field value.

- **Case**: a checker places a valid declaration in a repository root
  and triggers an evaluation over it.
- **Observable**: the registered project, its identifier, and its
  governance-root designation appear in the human view and the machine
  answer for that project at the producing evaluation.
- **Oracle**: compare the served project identifier and root designation
  against the declaration file's contents; equality decides. Bounded:
  one file, one served answer.
- **Oracle independence**: the expected values come from the declaration
  file the checker authored, not from anything Syzygy computed.
- **Falsifier**: a valid declaration that yields zero registered
  projects, two, or a project whose identity differs from the declared
  identifier.

#### Scenario: Valid declaration read at an evaluation

- **WHEN** a syntactically and semantically valid `.syzygy/project.yaml`
  is read at an identified evaluation
- **THEN** exactly one registered project is served, carrying the
  declared opaque project identifier and naming the declaring repository
  as governance root

```yaml
warrants:
  primary: RFC3-4
  doctrine: []
  contracts: [RFC3-4, RFC3-5, RFC1-1, RFC1-10]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-002 — An invalid declaration is a named failure, never a partial registration

Group: Project declaration. Form: **event-response**.

WHEN Syzygy reads a declaration that is unparseable or invalid, Syzygy
SHALL produce one or more named validation failures, each identifying
what failed, and SHALL render every claim dependent on the declaration
`Unknown` with its reason. Invalid input SHALL NOT produce any partly
registered project: no registration fact derived from the invalid
declaration is served as current state.

- **Case**: a checker corrupts one field of an otherwise valid
  declaration (or the file's syntax) and triggers an evaluation.
- **Observable**: the named failure(s) and the Unknown renderings, in
  both the human view and the machine answer.
- **Oracle**: the served output contains at least one named failure
  identifying the corrupted element, and contains no registration fact
  sourced from the invalid declaration. Bounded: one declaration, one
  answer.
- **Oracle independence**: the checker knows which element it corrupted;
  the expectation is derived from that act, not from Syzygy's output.
- **Falsifier**: an invalid declaration that yields a served registered
  project, a silent failure, or a mixture of registered and unregistered
  facts presented as a registration.

#### Scenario: One invalid field

- **WHEN** a declaration with one invalid required field is read
- **THEN** a validation failure naming that field is served, and no
  registered project is produced from that declaration

#### Scenario: Unparseable file

- **WHEN** a declaration that does not parse is read
- **THEN** the parse failure is served as a named failure and every
  dependent claim renders `Unknown` with its reason

```yaml
warrants:
  primary: RFC3-9
  doctrine: [VIS-2]
  contracts: [RFC3-9, RFC3-1, RFC2-24]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-003 — Missing required information is visible

Group: Project declaration. Form: **event-response**.

WHEN a declaration omits information the closed field set requires,
Syzygy SHALL name each missing element in its validation output. A
reader SHALL be able to enumerate, from the served output alone, what is
missing.

- **Case**: a checker removes one required field from a valid
  declaration and triggers an evaluation.
- **Observable**: the served validation output, human view and machine
  answer.
- **Oracle**: the output names the removed field. Bounded: one field,
  one lookup.
- **Oracle independence**: the checker chose the field; the expected
  name comes from the closed field set (RFC3-5), not from Syzygy.
- **Falsifier**: a missing required field that produces a generic
  failure naming nothing, or no failure.

#### Scenario: Omitted required field named

- **WHEN** a declaration omitting a required field is read
- **THEN** the validation output names that field as missing

```yaml
warrants:
  primary: RFC3-5
  doctrine: [VIS-2]
  contracts: [RFC3-5, RFC3-9]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-004 — Syzygy never silently invents, repairs, or infers a declaration field

Group: Project declaration. Form: **prohibition**.

Syzygy SHALL NOT create, correct, default, or infer any project
declaration field value on its own authority. The only repair path is a
Proposal (RFC1-27) rendered unadopted until the owner adopts it; a
drafted value SHALL render as unadopted and SHALL bind nothing.

- **Case** (scope of quantification): every declaration read Syzygy
  performs, over every field of the closed set; counterexample schema: a
  served registration fact whose value appears in no owner-adopted
  declaration content; sweep: compare every served declaration-derived
  fact against the declaration bytes at the evaluation's snapshot — the
  denominator is the served fact set for that project.
- **Observable**: served registration facts and their source
  attribution; drafted repairs visible as unadopted proposals.
- **Oracle**: every served declaration-derived fact matches the adopted
  declaration bytes; any drafted value carries an unadopted marking.
  Bounded: the served fact set at one evaluation.
- **Oracle independence**: the declaration bytes are the authority; the
  oracle never consults Syzygy's own repair logic.
- **Falsifier**: a served registration fact whose value Syzygy supplied
  (a defaulted owner field, a guessed repository role) without an
  adopted declaration stating it.

#### Scenario: Repair offered only as an unadopted proposal

- **WHEN** Syzygy drafts a repair for an invalid or incomplete
  declaration
- **THEN** the repair is served as a Proposal marked unadopted, the
  underlying declaration remains invalid in the served state, and no
  repaired value is presented as current registration fact

```yaml
warrants:
  primary: RFC3-9
  doctrine: [VIS-4]
  contracts: [RFC3-9, RFC3-2, RFC1-27]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-005 — Registration facts are deterministic per declaration and revision

Group: Project declaration. Form: **invariant**.

Re-reading the same valid declaration at the same project revision SHALL
produce the same registration facts. Every served registration answer
SHALL name the identified evaluation it was computed at.

- **Case** (scope of quantification): all pairs of evaluations over one
  identical (declaration bytes, source snapshot); counterexample schema:
  two runs over one identified evaluation whose served registration
  facts differ in the deterministic layer; sweep: run the same
  evaluation twice and diff the served fact sets — denominator: the
  compared fact set.
- **Observable**: the two served fact sets and their evaluation stamps.
- **Oracle**: byte-level equality of the deterministic layer of the two
  answers (display formatting excluded). Bounded: two runs, one diff.
- **Oracle independence**: equality of two independent runs is judged by
  comparison, not by either run's own claim of determinism.
- **Falsifier**: two runs of one identified evaluation serving different
  registration facts, or an answer that cannot name its evaluation.

#### Scenario: Same declaration, same revision, same facts

- **WHEN** the same valid declaration is read twice at the same source
  snapshot and as-of instant
- **THEN** both answers carry the same registration facts and the same
  evaluation identity

```yaml
warrants:
  primary: RFC1-9
  doctrine: [VIS-7]
  contracts: [RFC1-9, RFC6-7, RFC6-15]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-006 — Governance-root count violations surface; they are never repaired

Group: Project declaration. Form: **event-response**.

WHEN a readable declaration state resolves a project to two or more
governance roots, Syzygy SHALL mint a contradiction routed to the owner
and SHALL NOT pick a winner. WHEN a project resolves to zero governance
roots, Syzygy SHALL render the entry `Unknown` with reason
`missing-declaration` at the observing workspace level — unevaluable as
a project, never dropped, never guessed, and no kernel contradiction is
minted for the zero-root case (RFC1-1).

- **Case**: a checker declares the same project identity in two
  repositories (two roots), and separately references a project with no
  declaration (zero roots).
- **Observable**: the rendered contradiction with its adjudication
  route (two roots); the workspace-level Unknown with reason
  `missing-declaration` (zero roots).
- **Oracle**: the two-root case serves a contradiction and no single
  chosen root; the zero-root case serves `Unknown` with the verbatim
  reason. Bounded: two fixtures, two lookups.
- **Oracle independence**: expected outcomes come from RFC1-1's stated
  rule, not from Syzygy's resolution logic.
- **Falsifier**: two roots resolved by any precedence (freshest file,
  first found), or a zero-root project rendered as an empty project, an
  error, or silently absent.

#### Scenario: Two governance roots

- **WHEN** two repositories each carry a declaration claiming the same
  project identity
- **THEN** a contradiction is served, routed to owner adjudication, and
  no repository is served as the chosen root

#### Scenario: Zero governance roots

- **WHEN** a workspace references a project for which no governance root
  resolves
- **THEN** the entry renders `Unknown` with reason `missing-declaration`
  and is neither dropped nor rendered as an empty project

```yaml
warrants:
  primary: RFC1-1
  doctrine: [VIS-2]
  contracts: [RFC1-1, RFC3-4, RFC2-24]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-010 — Every declared repository has an explicit coverage result

Group: Consent and coverage. Form: **state projection/query**.

For every repository the project declaration names, Syzygy SHALL serve
an explicit per-repository coverage result at the producing evaluation:
whether the repository was observed, and if not, why not. No declared
repository is silently absent from the coverage answer.

- **Case**: a checker declares N repositories (some consented and
  reachable, some not) and queries coverage.
- **Observable**: the per-repository coverage results, human view and
  machine answer.
- **Oracle**: the answer contains exactly N results, one per declared
  repository, each carrying an observed-or-why-not value. Bounded: N is
  the declaration's own count.
- **Oracle independence**: N and the expected per-repository conditions
  come from the fixture the checker declared.
- **Falsifier**: a declared repository missing from the coverage answer,
  or a coverage answer whose repository count differs from the
  declaration's.

#### Scenario: All declared repositories answered

- **WHEN** coverage is queried for a project declaring three
  repositories, one of them unconsented
- **THEN** three per-repository results are served, and the unconsented
  one carries its explicit not-observed result rather than being omitted

```yaml
warrants:
  primary: RFC1-3
  doctrine: [VIS-2]
  contracts: [RFC1-3, RFC1-4, RFC3-6, RFC3-7]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-011 — Consent is a visible recorded fact, never an assumption

Group: Consent and coverage. Form: **invariant**.

Observation consent SHALL be a recorded, per-(project, repository)
consent record, and the consent state Syzygy serves SHALL derive only
from such records: their scope, attribution, and grant state render with
the coverage boundary. Absence of a resolvable in-force consent record
SHALL render as absence of consent — never as implied consent and never
as absence of the repository.

- **Case** (scope of quantification): every (project, repository) pair
  the declaration names; counterexample schema: a repository rendered as
  observed whose consent reference resolves to no in-force consent
  record; sweep: for each declared pair, join the served coverage state
  to the consent records at the snapshot — denominator: the declared
  pair count.
- **Observable**: consent state per repository in the coverage answer
  and the "Why this answer?" fact set.
- **Oracle**: every pair served as observed joins to an in-force consent
  record; every pair without one is served as unconsented. Bounded by
  the declared pair count.
- **Oracle independence**: the consent records are governance-plane
  artifacts the checker can read directly; the oracle never consults
  Syzygy's consent logic.
- **Falsifier**: a repository observed (any content served) with no
  in-force consent record, or consent state served that no record
  supports.

#### Scenario: Consent state joins to a record

- **WHEN** the coverage boundary is served for a repository whose
  consent record is in force
- **THEN** the served consent state cites that record's scope and grant
  state

```yaml
warrants:
  primary: RFC3-7
  doctrine: [SEC-4]
  contracts: [RFC3-7, RFC3-6, RFC1-3]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-012 — Unconsented renders Unknown as a policy state, never as error or absence

Group: Consent and coverage. Form: **state projection/query**.

WHEN resolution of any project answer requires an unconsented source or
provider, that portion SHALL render `Unknown` with reason
`unconsented-source-or-provider`, presented as a standing policy state
with its resolution route (record consent) — never as a failure, an
error page, a broken link, an empty region, or an empty-but-normal
graph. The consented remainder SHALL render normally.

- **Case**: a checker declares a repository, withholds its consent
  record, and queries the project.
- **Observable**: the Unknown rendering with its verbatim reason, in
  human view and machine answer; the unaffected remainder.
- **Oracle**: the served value for the unconsented portion is `Unknown`
  with the exact reason string `unconsented-source-or-provider`;
  string comparison decides. Bounded: one portion, one comparison.
- **Oracle independence**: the expected string is fixed by RFC2-24's
  closed vocabulary, outside the implementation.
- **Falsifier**: an unconsented repository rendered as an error, as
  empty content, or with an invented reason spelling.

#### Scenario: Unconsented repository queried

- **WHEN** a project answer depending on an unconsented repository is
  requested
- **THEN** that portion renders `Unknown` with reason
  `unconsented-source-or-provider` and its resolution route, and
  consented portions render normally

```yaml
warrants:
  primary: RFC6-26
  doctrine: [VIS-2]
  contracts: [RFC6-26, RFC3-6, RFC2-24]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-013 — Coverage failure states are distinguishable

Group: Consent and coverage. Form: **invariant**.

Where the accepted vocabulary distinguishes them, Syzygy SHALL render
missing consent, an inaccessible source, stale observation, and failed
observation as distinct states, each verbatim from its closed
vocabulary: missing consent as reason #6
(`unconsented-source-or-provider`), an uncaptured or unreachable source
as reason #10 (`source-uncaptured-or-unreachable`), evidence past its
currency bound as reason #4 (`stale-beyond-currency-bound`), and an
observer failure as its degradation state with degrade-to-last-good
marked stale/broken (RFC2-23). Two different conditions SHALL NOT
collapse into one rendered state.

- **Case** (scope of quantification): the four named conditions;
  counterexample schema: two of the four conditions producing one
  indistinguishable rendered state; sweep: produce each condition in a
  fixture and record the four rendered states — denominator: the four
  conditions.
- **Observable**: the four rendered states, human view and machine
  answer.
- **Oracle**: the four rendered (state, reason) values are pairwise
  distinct and each matches its vocabulary entry verbatim. Bounded: four
  fixtures, six pairwise comparisons.
- **Oracle independence**: expected values are the closed vocabularies'
  own strings.
- **Falsifier**: an unreachable source rendered with reason #6, a stale
  observation rendered as current, or an observer failure rendered
  indistinguishably from missing consent.

#### Scenario: Unreachable is not unconsented

- **WHEN** one declared repository is consented but unreachable at
  snapshot time and another has no consent record
- **THEN** the first renders `Unknown` with reason
  `source-uncaptured-or-unreachable` and the second with reason
  `unconsented-source-or-provider`

```yaml
warrants:
  primary: RFC2-24
  doctrine: [VIS-2]
  contracts: [RFC2-24, RFC2-23, RFC6-14]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-014 — Incomplete coverage is never rendered as complete coverage

Group: Consent and coverage. Form: **prohibition**.

Syzygy SHALL NOT present a partial capture as full scope. WHEN a
snapshot is partial, the captured scope SHALL be declared explicitly,
the uncaptured portion SHALL render `Unknown`, and no aggregate over the
full scope SHALL render as if whole.

- **Case** (scope of quantification): every served aggregate or
  full-scope claim over a project whose snapshot is partial;
  counterexample schema: an aggregate presented without disclosure of
  the uncaptured portion; sweep: for a fixture with one uncaptured
  source, enumerate every served project-level aggregate and check each
  for the declared-scope disclosure — denominator: the enumerated
  aggregate set.
- **Observable**: aggregates and their declared-scope disclosures.
- **Oracle**: every enumerated aggregate over the partial snapshot
  carries the explicit captured-scope declaration; presence is checked
  per aggregate. Bounded by the enumeration.
- **Oracle independence**: the fixture defines which source is
  uncaptured; the disclosure obligation comes from RFC2-23, not from the
  implementation.
- **Falsifier**: any full-scope-looking answer over a partial snapshot
  with no declared captured scope.

#### Scenario: Partial snapshot disclosed

- **WHEN** one of two consented repositories could not be captured and a
  project-level answer is requested
- **THEN** the answer declares the captured scope, renders the
  uncaptured repository's portion `Unknown`, and presents no full-scope
  aggregate as whole

```yaml
warrants:
  primary: RFC2-23
  doctrine: [VIS-1, VIS-2]
  contracts: [RFC2-23, RFC6-16]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-015 — One coverage boundary, retrievable identically by human and machine

Group: Consent and coverage. Form: **state projection/query**.

Syzygy SHALL serve one coverage boundary per (project, evaluation): the
union of the producing evaluation's executed mapping coverage records
and, where the snapshot was partial, its explicitly declared captured
scope (RFC6-19 class 7). A human view and a machine client SHALL
retrieve the same boundary facts. Machine retrieval is available only to
an admitted client, classified by credential presented — never by
network location (RFC5-3).

- **Case**: a checker (a) retrieves the coverage boundary for one
  project at one evaluation through the human view and through an
  admitted machine client; (b) presents the same admissible credential
  from two distinct network locations; and (c) attempts machine
  retrieval with no admissible credential.
- **Observable**: the two retrieved boundary fact sets (a); the two
  admission outcomes (b); the credential-less attempt's outcome (c).
- **Oracle**: (a) the two fact sets are equal in content (formatting
  aside): same records, same declared scopes, same consent states; (b)
  both attempts yield the same admission outcome — location changed
  nothing; (c) the attempt is refused and no boundary fact is served.
  Bounded: one comparison over one fact set, plus two admission checks.
- **Oracle independence**: equality of two independently retrieved
  renderings is judged by comparison, not by either channel's claim;
  admission outcomes are observed responses, and the classification rule
  (credential, never location) is the accepted contract's (RFC5-3).
- **Falsifier**: a boundary fact present in one channel and absent from
  the other, boundary facts served to an unadmitted client, or an
  admission outcome that differs with network location under one
  credential.

#### Scenario: Same boundary through both channels

- **WHEN** the coverage boundary is retrieved for one project at one
  evaluation via the human view and via an admitted machine client
- **THEN** both retrievals expose the same boundary facts

#### Scenario: Admission is by credential, never location

- **WHEN** machine retrieval is attempted with no admissible credential,
  and separately with one credential from two network locations
- **THEN** the credential-less attempt is refused with no boundary facts
  served, and the two same-credential attempts share one admission
  outcome

```yaml
warrants:
  primary: RFC6-19
  doctrine: []
  contracts: [RFC6-19, RFC6-13, RFC5-3]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-016 — No source is inspected through authority the project did not grant

Group: Consent and coverage. Form: **prohibition**.

Syzygy SHALL NOT observe any repository or source without a recorded
in-force consent record for the exact (observing project, repository)
pair. Consent granted to one project SHALL NOT admit observation by
another. No served content, structure, or derived fact SHALL originate
from an unconsented source.

- **Case** (scope of quantification): every fact Syzygy serves for a
  project; counterexample schema: a served fact whose provenance names a
  source with no in-force consent record for this project;
  sweep: for a fixture where repository R is consented to project A but
  not project B, enumerate B's served facts and check each fact's
  provenance against B's consent records — denominator: B's served fact
  set.
- **Observable**: served facts and their provenance (producing
  evaluation, source identities).
- **Oracle**: no fact in B's served set carries provenance from R.
  Bounded by the served fact set.
- **Oracle independence**: consent records are readable governance
  artifacts; provenance is checked against them, not against Syzygy's
  own consent decision.
- **Falsifier**: any fact about R's content served in project B's
  answers.

#### Scenario: Consent is per project pair

- **WHEN** repository R has an in-force consent record for project A and
  none for project B
- **THEN** project A's answers may carry facts observed from R and
  project B's answers carry none, B rendering R `Unknown` with reason
  `unconsented-source-or-provider`

```yaml
warrants:
  primary: RFC1-3
  doctrine: [SEC-4]
  contracts: [RFC1-3, RFC3-7, RFC3-30]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-020 — One fixed Syzygy-owned human entry path

Group: Human project entry. Form: **state projection/query**.

A governed project SHALL have exactly one fixed Syzygy-owned human entry
path, `.syzygy/intent/OVERVIEW.md`, present at the same path in every
governed project. The entry is the project's primary narrative — there
are not two front doors (P-38, option (a) as drafted). The path is a
publication location, never an identity: nothing may cite the path as an
identifier.

- **Case**: a checker asks, for a governed project, where a human reader
  is sent first.
- **Observable**: the served entry route in the human view and the entry
  location in the machine answer.
- **Oracle**: the served entry path equals
  `.syzygy/intent/OVERVIEW.md`; string comparison. Bounded: one lookup.
- **Oracle independence**: the expected path is fixed by RFC7-39 and the
  P-38 ruling, outside the implementation.
- **Falsifier**: a project served with a different first entry path,
  with two competing front doors, or with the path used as the
  narrative's identifier.

#### Scenario: Entry path is fixed

- **WHEN** the human entry for any governed project is requested
- **THEN** the served entry is `.syzygy/intent/OVERVIEW.md` and no
  second default entry is offered

```yaml
warrants:
  primary: RFC7-39
  doctrine: []
  contracts: [RFC7-39, RFC1-10]
  policies: []
  decisions: ["P-38-ruling-2026-08-16 (decisions/HUMAN-ENTRY-DECISION.md)"]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-021 — The entry routes to exact authority and is never itself authority

Group: Human project entry. Form: **invariant**.

The entry SHALL explain what project is being viewed and route the
reader to exact authority, citing doctrine, contracts, decisions, and
specifications by their stable identifiers. It is governed presentation:
it SHALL carry the `non-citable` / `presentation-artifact` attribute on
every rendering — interactive, exported, embedded, or plain-text — and
SHALL never be the source of any project fact. Where the entry and an
authority disagree, the authority wins and the disagreement renders as a
finding, never silently.

- **Case** (scope of quantification): every rendering of the entry
  Syzygy serves; counterexample schema: a rendering lacking the
  non-citable attribute, or a project fact sourced from the entry;
  sweep: enumerate the entry's served rendering channels and check the
  attribute on each; check no served claim cites the entry as its
  authority — denominator: the enumerated channels and the served claim
  set.
- **Observable**: the attribute on each rendering; the authority
  citations in the entry; claim provenance.
- **Oracle**: attribute present on every channel; zero claims with the
  entry as source. Bounded by the enumerations.
- **Oracle independence**: attribute presence and provenance are
  inspectable in served output; the rule comes from RFC7-39/RFC7-33.
- **Falsifier**: an exported entry rendering without the attribute, or
  any status answer whose cited basis is the overview file.

#### Scenario: Non-citability travels on export

- **WHEN** the entry is served in plain-text or through a machine answer
- **THEN** the rendering carries the `non-citable` /
  `presentation-artifact` attribute

```yaml
warrants:
  primary: RFC7-39
  doctrine: []
  contracts: [RFC7-39, RFC7-33]
  policies: []
  decisions: ["P-38-ruling-2026-08-16 (decisions/HUMAN-ENTRY-DECISION.md)"]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-022 — Missing, unreadable, stale, or contradictory entry material renders honestly

Group: Human project entry. Form: **event-response**.

WHEN the entry file is absent, Syzygy SHALL render the absence as a
finding — never silently. WHEN it is unreadable, the entry SHALL render
`Unknown` with its reason. WHEN it is stale or contradicts an authority,
the staleness or contradiction SHALL render as a disclosed fact with the
authority winning.

- **Case**: a checker removes, corrupts, and (separately) makes the
  entry contradict a cited authority, triggering an evaluation each
  time.
- **Observable**: the finding, the Unknown-with-reason, and the
  disclosed disagreement, in human view and machine answer.
- **Oracle**: each fixture's served state matches its condition: absent
  → finding; unreadable → `Unknown` + reason; contradictory → both texts
  visible with the authority governing. Bounded: three fixtures, three
  lookups.
- **Oracle independence**: the checker created each condition; expected
  renderings come from RFC7-39 and RFC2-24.
- **Falsifier**: an absent entry rendered as if present, an unreadable
  entry silently skipped, or a contradiction resolved by hiding either
  side.

#### Scenario: Absent entry is a finding

- **WHEN** a governed project has no `.syzygy/intent/OVERVIEW.md`
- **THEN** the absence renders as a finding on the project's surface,
  never as a silently missing page

```yaml
warrants:
  primary: RFC7-39
  doctrine: [VIS-2]
  contracts: [RFC7-39, RFC2-24]
  policies: []
  decisions: ["P-38-ruling-2026-08-16 (decisions/HUMAN-ENTRY-DECISION.md)"]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-023 — Entry behavior requires no write outside the governed plane

Group: Human project entry. Form: **prohibition**.

Serving, maintaining, or drafting the human entry SHALL NOT cause Syzygy
to write outside its two direct-write namespaces, `openspec/**` and
`.syzygy/**`.

- **Case** (scope of quantification): every write Syzygy performs in the
  course of entry behavior; counterexample schema: a write whose path is
  outside the two namespaces; sweep: record all writes during an
  entry-serving and entry-drafting fixture and check each path —
  denominator: the recorded write set.
- **Observable**: the write record — captured **externally to Syzygy**
  by the checking harness (filesystem comparison or harness-level write
  tracing), cross-checked against the attributed-write record (SEC-4).
- **Oracle**: every recorded write path is under `openspec/**` or
  `.syzygy/**`; prefix check per write. Bounded by the write set.
- **Oracle independence**: the write population is established by the
  harness's own external record, never solely by Syzygy's
  self-reported write log; paths are judged against the doctrine
  boundary, not against Syzygy's own classification.
- **Falsifier**: any entry-related write landing outside the two
  namespaces.

#### Scenario: Drafting the entry stays in the plane

- **WHEN** Syzygy drafts entry content for a governed project
- **THEN** every write lands inside `.syzygy/**` and the drafted content
  renders unadopted

```yaml
warrants:
  primary: RFC3-3
  doctrine: [VIS-5]
  contracts: [RFC3-3]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-030 — The seven project-shape answers, defined here and answered independently

Group: Independent project-shape answers. Form: **state projection/query**.

Syzygy SHALL answer, per project at an identified evaluation, the seven
owner-ratified project-shape questions (SDR-36; drafting site: this
specification, per site a2). Each answer is computed and presented
independently: no answer's computation reads another answer's value.
The vocabulary, authored here as that ruling directs:

- **Registered** — has this project's declaration been read and
  validated, yielding a registered project? Constituent facts: the
  declaration, its validation result, the governance-root designation
  (requirements 001–006).
- **Shape present** — do the shape artifacts the declaration references
  (capability, topology, region, and mapping declarations, and the spec
  root) exist and resolve at the evaluation? Constituent facts: the
  declaration's `declarations` references and their resolution results.
- **Human-understandable** — does recorded fresh-reader comprehension
  evidence for this project exist and stand (VIS-3's test class)?
  Constituent facts: recorded comprehension-walkthrough records and
  owner verdicts, where they exist. With no records, the answer is
  `Unknown` — the expected initial render.
- **Observable** — may Syzygy observe the declared sources, and did
  current observation succeed? Constituent facts: the coverage boundary
  and consent states (requirements 010–016).
- **Traceable** — do the project's rendered internal references resolve
  to their identified targets? Constituent facts: link-resolution
  results over the served surfaces at the evaluation (the trust floor's
  link rule).
- **Mission-ready** — deferred; see requirement 036.
- **Reconciled** — has reconciliation of merged work against intent been
  computed and satisfied for the declared scope? Constituent facts: the
  reconciliation chain state where carried; see requirement 037.

Each answer takes its value under the two-term rule (SDR-35) over its
constituent facts: `satisfied` when current evidence supports it, `Gap`
when current admissible evidence establishes non-satisfaction, and
otherwise `Unknown` with its reason. The satisfied state renders with
the verbatim spelling `satisfied` — authored here per drafting site a2,
closing the value domain at three spellings the way `Unknown` and `Gap`
are already closed. These labels are product vocabulary; no additional
maturity terms are minted around them.

- **Case**: a checker queries the shape answers for a registered
  project.
- **Observable**: seven named answers, each with its own value and
  constituent facts, in human view and machine answer.
- **Oracle**: the answer set contains exactly the seven names above,
  each carrying its own value and fact set; count and name comparison.
  Bounded: seven entries.
- **Oracle independence**: the expected names come from the recorded
  owner ruling (SDR-36), not from the implementation.
- **Falsifier**: a missing or extra answer, an answer whose value is a
  function of another answer's value, or a renamed answer.

#### Scenario: Seven independent answers served

- **WHEN** the project-shape answers are requested for a registered
  project
- **THEN** exactly seven answers named Registered, Shape present,
  Human-understandable, Observable, Traceable, Mission-ready, and
  Reconciled are served, each independently computed with its
  constituent facts

```yaml
warrants:
  primary: SDR-36
  doctrine: [VIS-2, VIS-3, VIS-7]
  contracts: [RFC6-18, RFC2-24]
  policies: []
  decisions: [SDR-36, SDR-35]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-031 — No combined score, badge, colour, percentage, or passing count

Group: Independent project-shape answers. Form: **prohibition**.

Syzygy SHALL NOT compute, render, or serve any combination of the shape
answers: no composite score, no single badge or colour for the project,
no percentage, and no count of passing answers. An aggregate rendering
over the answers carries no epistemic state of its own and SHALL
disclose its members' composition instead.

- **Case** (scope of quantification): every rendering and machine answer
  that presents more than one shape answer; counterexample schema: a
  served value derived from two or more answers' values; sweep:
  enumerate the served project-level fields for a fixture project and
  check that none is a function of multiple facet values — denominator:
  the served field set.
- **Observable**: project-level renderings and machine answers.
- **Oracle**: no served field aggregates facet values into one number,
  colour, badge, or count-of-passing. Bounded by the served field set.
- **Oracle independence**: the prohibition's subject (a derived
  composite) is checked against the served output's own declared
  derivations, not against implementation intent.
- **Falsifier**: a served "5/7 green", a project health colour, or any
  single indicator whose value changes when one facet flips while it
  claims to summarize them.

#### Scenario: No rollup on the project surface

- **WHEN** a project's seven answers include a `Gap` and several
  `Unknown` values
- **THEN** no served field summarizes them into a score, badge, colour,
  percentage, or passing count

```yaml
warrants:
  primary: SDR-36
  doctrine: [VIS-1, VIS-2]
  contracts: [RFC6-14]
  policies: []
  decisions: [SDR-36]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-032 — Registration is never certification

Group: Independent project-shape answers. Form: **invariant**.

`Registered` SHALL read as a relationship fact — this project is under
Syzygy observation with a validated declaration — never as an
endorsement, and no shape answer's value SHALL imply another's.
Registration SHALL NOT imply that shape exists, is understandable, is
observable, is traceable, is Mission-ready, or is reconciled.

- **Case** (scope of quantification): all pairs of shape answers;
  counterexample schema: an answer whose served value changes when a
  fact **outside its own declared constituent-fact set** (requirement
  030) is flipped; sweep: in a fixture, flip one underlying fact at a
  time — for each answer, where its declared set admits one, a fact
  constituent to it alone — and record all seven served values per
  flip — denominator: the flip set × seven observations, with every
  flip's declared-set membership enumerated first.
- **Observable**: the seven served values across the flip fixtures,
  joined to each flipped fact's declared-set memberships.
- **Oracle**: each flip changes only the answers whose declared
  constituent-fact sets contain the flipped fact. A shared fact (the
  declaration itself is constituent to `Registered`, `Shape present`,
  and `Observable`) moving its dependents together is conformance, not
  coupling — requirement 002 mandates exactly that co-movement for an
  invalidated declaration; a value moving with **no** declared-set
  membership in the flipped fact is the violation. Bounded by the
  enumerated flip set.
- **Oracle independence**: the fixture controls the underlying facts;
  declared-set membership comes from requirement 030's definitions, not
  from the implementation; the oracle observes served values only.
- **Falsifier**: registering a project raising any other answer above
  `Unknown` absent its own evidence, or any answer's value moving with a
  fact its declared constituent set does not contain.

#### Scenario: Registration raises nothing else

- **WHEN** a project is newly registered with no other evidence present
- **THEN** `Registered` reflects the validated declaration and the other
  six answers render `Unknown` (or their deferred posture), each with
  its own reason

```yaml
warrants:
  primary: SDR-36
  doctrine: [VIS-2]
  contracts: []
  policies: []
  decisions: [SDR-36]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-033 — Every answer exposes its constituent facts and scope

Group: Independent project-shape answers. Form: **state projection/query**.

Each shape answer SHALL expose, on demand, the constituent facts it was
computed from and the scope it covers, through the one fact set of
requirement 040. An answer whose constituent facts cannot be served is
not a servable answer.

- **Case**: a checker selects one shape answer and requests its facts.
- **Observable**: the fact set: constituent facts, declared scope,
  producing evaluation.
- **Oracle**: the served fact set is non-empty, names the scope, every
  fact resolves, and the served value's stated basis references only
  facts present in the set; per-answer check. Bounded: seven answers.
- **Oracle independence**: resolvability is checked by following the
  served references, not by trusting the answer.
- **Falsifier**: an answer served with no reachable constituent facts,
  or facts that do not support the served value's stated basis.

#### Scenario: Facts behind an answer

- **WHEN** the facts behind the `Observable` answer are requested
- **THEN** the coverage boundary, consent states, and producing
  evaluation it was computed from are served

```yaml
warrants:
  primary: RFC6-18
  doctrine: [VIS-2]
  contracts: [RFC6-18, RFC6-19]
  policies: []
  decisions: [SDR-36]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-034 — Missing evidence yields Unknown; non-satisfaction yields Gap; absence is never zero

Group: Independent project-shape answers. Form: **invariant**.

For every shape answer and every constituent claim: no verifying
evidence SHALL yield `Unknown` with its reason — never a favourable
answer, never green, and never zero for an absent quantity. Current
admissible evidence of non-satisfaction SHALL yield `Gap`. The two are
never interchanged.

- **Case** (scope of quantification): every served shape answer and
  constituent claim over fixtures with (a) no evidence and (b) evidence
  of non-satisfaction; counterexample schema: a no-evidence claim served
  favourable or zero, or a non-satisfaction claim served `Unknown`;
  sweep: enumerate served values over both fixtures — denominator: the
  served claim set per fixture.
- **Observable**: served values and reasons.
- **Oracle**: fixture (a) values are all `Unknown` with a reason from
  the closed vocabulary; fixture (b) values are `Gap`. Bounded by the
  served sets.
- **Oracle independence**: the fixtures control what evidence exists;
  expected labels come from SDR-35 and VIS-2.
- **Falsifier**: a favourable or zero value served where no evidence
  exists, or `Unknown` served where evidence establishes
  non-satisfaction.

#### Scenario: No evidence is Unknown, not favourable

- **WHEN** a shape answer's constituent facts contain no verifying
  evidence
- **THEN** the answer renders `Unknown` with its primary reason, never a
  favourable value and never zero

#### Scenario: Non-satisfaction is Gap, not Unknown

- **WHEN** current admissible evidence establishes a shape answer's
  desired state is unsatisfied
- **THEN** the answer renders `Gap`

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-2]
  contracts: [RFC2-24]
  policies: []
  decisions: [SDR-35]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-035 — Several reasons may be visible at once; one never hides the others

Group: Independent project-shape answers. Form: **event-response**.

WHEN more than one Unknown condition applies to an answer or claim, the
primary reason SHALL render with its secondary reasons beside it — all
drawn verbatim from the closed twelve-reason vocabulary, secondaries
marked as secondary and never folded into primary counts. One reason
SHALL NOT hide the others.

- **Case**: a checker constructs a claim with two applicable conditions
  (e.g. an unconsented repository that is also unreachable).
- **Observable**: the served reason set on the claim instance.
- **Oracle**: the served instance carries one primary and the applicable
  secondaries, each verbatim; set comparison against the fixture's known
  conditions. Bounded: one claim, one set.
- **Oracle independence**: the fixture defines which conditions hold;
  the vocabulary defines the spellings.
- **Falsifier**: a claim with two known conditions served with one
  reason and no secondary, or a secondary spelling outside the twelve.

#### Scenario: Two conditions both visible

- **WHEN** a claim is Unknown for two conditions the vocabulary
  distinguishes
- **THEN** the primary reason and the secondary reason are both served,
  the secondary marked as such

```yaml
warrants:
  primary: RFC2-24
  doctrine: [VIS-2]
  contracts: [RFC2-24, RFC6-14]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-036 — Mission-ready renders only its deferred posture

Group: Independent project-shape answers. Form: **state projection/query**.

While the governing Context and Mission contracts remain unaccepted,
the `Mission-ready` answer SHALL render only its deferred posture —
present and honest about its deferral, never invisible, never
evaluated, and never favourable. The posture comprises three served
coordinates, each verbatim: value `not evaluated`, basis `deferred`,
epistemic label `Unknown`. (SDR-36 rule 3's slash-separated phrase
names these three coordinates; their spellings are authored here per
drafting site a2.) The facet's semantics are deliberately not defined
by this specification.

- **Case**: a checker queries the shape answers of any project while the
  Mission contracts are unaccepted.
- **Observable**: the `Mission-ready` answer's three posture
  coordinates.
- **Oracle**: the served value is `not evaluated`, the basis `deferred`,
  the epistemic label `Unknown` — string comparison per coordinate,
  nothing else served as the answer's value. Bounded: three strings.
- **Oracle independence**: the expected posture is the owner ruling's
  (SDR-36 rule 3), its coordinate spellings fixed in this text, outside
  the implementation.
- **Falsifier**: a `Mission-ready` answer served as satisfied, `Gap`, a
  score, or omitted from the answer set, or a posture coordinate served
  with a different spelling.

#### Scenario: Deferred facet stays visible

- **WHEN** the shape answers are served while no Mission contract is
  accepted
- **THEN** `Mission-ready` is present and renders its deferred posture:
  value `not evaluated`, basis `deferred`, epistemic label `Unknown`

```yaml
warrants:
  primary: SDR-36
  doctrine: [VIS-2]
  contracts: []
  policies: []
  decisions: [SDR-36]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-037 — Uncomputed reconciliation is Unknown

Group: Independent project-shape answers. Form: **event-response**.

WHEN reconciliation has not been computed for the declared scope, the
`Reconciled` answer SHALL render `Unknown`, and merged-but-unreconciled
work SHALL render as reconciliation evidence absent / `Unknown` — never
as reconciled, done, or green (SDR-12). The merged-but-unreconciled
condition is disclosed as a fact of the render, bound to no thirteenth
reason (SDR-34, ratifying the RFC2-19(a) exemption as written).

- **Case**: a checker presents a project with merged work and no
  computed reconciliation, and queries `Reconciled`.
- **Observable**: the `Reconciled` answer and the work's reconciliation
  state in the fact set.
- **Oracle**: the answer is `Unknown`; the work's state reads as
  reconciliation evidence absent; no reason outside the twelve is
  minted. Bounded: one answer, one state.
- **Oracle independence**: the fixture controls that no reconciliation
  was computed; expected renderings come from SDR-12/SDR-34.
- **Falsifier**: merged work rendered as reconciled or the answer
  rendered favourable absent a computed reconciliation, or a minted
  thirteenth Unknown reason.

#### Scenario: Merged is not reconciled

- **WHEN** a project has merged work and no reconciliation evaluation
  has been computed
- **THEN** `Reconciled` renders `Unknown` and the merged work renders as
  reconciliation evidence absent

```yaml
warrants:
  primary: SDR-12
  doctrine: [VIS-2]
  contracts: [RFC6-19, "RFC2-19(a)"]
  policies: []
  decisions: [SDR-12, SDR-34]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-038 — A negative or Unknown answer never erases the others

Group: Independent project-shape answers. Form: **state projection/query**.

A `Gap` or `Unknown` value on one shape answer SHALL NOT suppress,
hide, or degrade the rendering of any other answer. All seven answers
remain served, each with its own value.

- **Case**: a checker constructs a project with one `Gap`, several
  `Unknown`s, and one satisfied answer, and queries the set.
- **Observable**: the served answer set.
- **Oracle**: all seven answers present with their independent values;
  count and per-answer comparison. Bounded: seven entries.
- **Oracle independence**: the fixture defines the expected values per
  answer.
- **Falsifier**: an answer omitted or blanked because a sibling is
  negative or Unknown.

#### Scenario: Mixed values all served

- **WHEN** one answer is `Gap` and others are `Unknown` or satisfied
- **THEN** all seven answers are served with their own values

```yaml
warrants:
  primary: SDR-36
  doctrine: [VIS-1, VIS-2]
  contracts: [RFC6-18]
  policies: []
  decisions: [SDR-36]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-040 — Every answer is explainable: "Why this answer?"

Group: Why this answer and human/machine parity. Form: **state projection/query**.

For every answer Capability 1 produces — a registration fact, a coverage
result, a shape answer, a discoverability finding — Syzygy SHALL serve
one explanation fact set per (selection, evaluation, scenario context),
reachable from the human view under a literal name ("Why this answer?")
and served in full through the machine plane. The fact set exposes,
where applicable and warranted by the accepted drawer contract
(RFC6-19): owning authority and its governing revision; source or
evidence revision; state category (state plane); evidence classification
(label, tier, Unknown reason, freshness); evaluation identity;
freshness; the Unknown reason or reasons; the coverage and consent
boundary; active challenge state; active contradiction state; related
work state; and reconciliation state. No field outside the accepted
contract's classes is invented.

- **Case**: a checker selects one answer and requests its explanation
  through both channels.
- **Observable**: the fact set, human view and machine answer.
- **Oracle**: the served fact set carries the applicable RFC6-19
  classes for the selection, and each internal reference in it resolves;
  per-class presence check. Bounded: one fact set.
- **Oracle independence**: the class list is the accepted contract's;
  resolvability is checked by following references.
- **Falsifier**: an answer with no reachable explanation, an explanation
  missing an applicable class, or a fact-set field no accepted clause
  warrants.

#### Scenario: Explanation reachable for a shape answer

- **WHEN** "Why this answer?" is requested for one shape answer
- **THEN** one fact set is served carrying the answer's owning
  authority, evidence classification, evaluation identity, and Unknown
  reasons where applicable

```yaml
warrants:
  primary: RFC6-18
  doctrine: [VIS-1, VIS-2]
  contracts: [RFC6-18, RFC6-19]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-041 — Humans and machines receive the same facts

Group: Why this answer and human/machine parity. Form: **invariant**.

The human view and the machine answer for one (selection, evaluation,
scenario context) SHALL expose the same underlying facts. They may
format, order, group, and progressively disclose differently; they SHALL
NOT differ on which facts, labels, or provenance exist, and every
epistemic value travels verbatim from its closed vocabulary. There are
no endpoint-only facts and no UI-only facts.

- **Case** (scope of quantification): every (selection, evaluation,
  context) Capability 1 serves; counterexample schema: a fact present in
  one channel's full disclosure and absent from the other's; sweep: for
  a fixture project, retrieve both channels' full fact sets for each
  Capability 1 answer and diff — denominator: the answer set.
- **Observable**: both channels' fact sets.
- **Oracle**: content equality of the fact sets (presentation aside),
  labels verbatim. Bounded by the answer set.
- **Oracle independence**: judged by cross-channel comparison, not by
  either channel's self-description.
- **Falsifier**: a machine answer omitting an Unknown the human view
  shows, or a human view showing evidence the machine answer cannot
  retrieve.

#### Scenario: No machine-invisible Unknown

- **WHEN** the human view renders a shape answer `Unknown` with its
  reason
- **THEN** the machine answer for the same selection and evaluation
  carries the same `Unknown` and the same reason verbatim

```yaml
warrants:
  primary: RFC6-13
  doctrine: [VIS-2]
  contracts: [RFC6-13, RFC6-14, RFC6-22]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-042 — Equivalent queries at one revision expose equivalent facts

Group: Why this answer and human/machine parity. Form: **invariant**.

Two equivalent queries — same selection, same evaluation identity, same
declared filters, same scenario context — SHALL expose equivalent facts
in the deterministic layer, and every answer SHALL name the evaluation
identity it was computed at. An answer that cannot name its evaluation
is not an answer.

- **Case** (scope of quantification): all repeated equivalent queries;
  counterexample schema: two equivalent queries whose deterministic
  answers differ, or an answer without an evaluation stamp; sweep: issue
  each Capability 1 query twice at a pinned evaluation and diff —
  denominator: the query set.
- **Observable**: the paired answers and their evaluation stamps.
- **Oracle**: deterministic-layer equality per pair; stamp present per
  answer. Bounded by the query set.
- **Oracle independence**: equality judged by comparison of independent
  runs.
- **Falsifier**: an unstamped answer, or two equivalent queries
  disagreeing at one evaluation.

#### Scenario: Repeat query at pinned evaluation

- **WHEN** one Capability 1 query is issued twice naming the same
  evaluation identity
- **THEN** both answers are equal in the deterministic layer and both
  name that evaluation

```yaml
warrants:
  primary: RFC6-15
  doctrine: [VIS-7]
  contracts: [RFC6-15, RFC6-7]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-043 — A parity disagreement is visible and fails; presentation precedence never resolves it

Group: Why this answer and human/machine parity. Form: **prohibition**.

WHEN two renderings of one (selection, evaluation, scenario context)
disagree on an entity's existence, a label, a reason, a freshness state,
a value, or a count over one declared scope, Syzygy SHALL NOT resolve
the disagreement by preferring one rendering: the disagreement is a
defect that fails this specification's parity requirements and, where
rendered, renders as a disagreement. Aggregation and finer detail are
lawful only as disclosed filter differences, never as contradiction.

- **Case** (scope of quantification): every pair of renderings over one
  (selection, evaluation, context); counterexample schema: a pair
  disagreeing on any equivalence facet while both are served as correct;
  sweep: the requirement-041/042 comparisons — denominator: the compared
  pair set.
- **Observable**: the compared renderings.
- **Oracle**: zero disagreements across the compared set; any found
  disagreement is a failure of this requirement, whatever either
  rendering claims. Bounded by the pair set.
- **Oracle independence**: disagreement is a relation between two served
  outputs; no implementation judgment is consulted.
- **Falsifier**: two conforming-looking renderings disagreeing on one
  fact while the system treats one as authoritative presentation.

#### Scenario: Disagreement is a defect, not a tie-break

- **WHEN** a human view and a machine answer disagree on one claim's
  label at one evaluation
- **THEN** that disagreement fails parity; neither channel's value is
  silently preferred

```yaml
warrants:
  primary: RFC6-23
  doctrine: [VIS-7]
  contracts: [RFC6-23, RFC6-22]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-044 — A missing explanation is never replaced by an optimistic summary

Group: Why this answer and human/machine parity. Form: **prohibition**.

WHEN an answer's explanation facts are unavailable, Syzygy SHALL render
the unavailability (`Unknown` with its reason) — never a summary,
default, or aggregate that reads more favourably than the missing facts
would support. Every aggregate over Capability 1 answers SHALL disclose
its membership count and full epistemic composition and support
expansion to members.

- **Case** (scope of quantification): every served answer whose
  explanation cannot be computed, and every served aggregate;
  counterexample schema: a favourable summary standing where explanation
  facts are absent, or an aggregate without its composition; sweep: for
  a fixture with an uncomputable explanation, enumerate the served
  values and aggregates — denominator: the enumerated set.
- **Observable**: the served values, aggregates, and compositions.
- **Oracle**: absent explanation renders Unknown-with-reason; every
  aggregate carries count and per-label/per-reason composition and
  expands. Bounded by the enumerated set.
- **Oracle independence**: the fixture controls the absence; the
  composition obligation is the accepted contract's.
- **Falsifier**: a green or favourable summary over facts that are
  absent, or an aggregate hiding its Unknowns.

#### Scenario: Aggregate disclosure

- **WHEN** several Unknown answers are aggregated in one rendering
- **THEN** the aggregate disclosed its membership count and per-reason
  composition and can be expanded to its members

```yaml
warrants:
  primary: RFC6-17
  doctrine: [VIS-1, VIS-2]
  contracts: [RFC6-17, RFC6-14]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-045 — Inferred is distinguishable from observed; generated presentation is never the source

Group: Why this answer and human/machine parity. Form: **invariant**.

Every fact Capability 1 serves SHALL carry its epistemic label
(Observed / Inferred / Unknown) verbatim, and inferred information SHALL
be distinguishable from observed information in every rendering,
machine-readably and without relying on colour, position, or layout.
Generated presentation artifacts SHALL never be the source of any
answer: every answer's cited basis is its owning authority, never a
rendering of it.

- **Case** (scope of quantification): every served fact and every
  generated presentation artifact; counterexample schema: an inferred
  fact indistinguishable from an observed one in any channel, or an
  answer citing a generated view as its source; sweep: enumerate served
  facts' labels and answers' cited bases in a fixture — denominator: the
  served fact and answer sets.
- **Observable**: labels on served facts; cited bases on answers.
- **Oracle**: every fact carries a label; inferred facts carry a
  machine-readable marking distinct from observed; no cited basis is a
  presentation artifact. Bounded by the enumerations.
- **Oracle independence**: labels and bases are inspectable output; the
  three-label rule is doctrine's.
- **Falsifier**: an LLM-derived value served without an Inferred
  marking, or a status answer whose provenance names a generated page.

#### Scenario: Label travels to the machine answer

- **WHEN** an inferred fact appears in a Capability 1 answer
- **THEN** its Inferred label is served verbatim in the machine answer
  and recoverable non-visually in the human view

```yaml
warrants:
  primary: RFC6-14
  doctrine: [VIS-1]
  contracts: [RFC6-14, RFC7-33]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-046 — Owning authority and effective status are exposed, stamp and record readable apart

Group: Why this answer and human/machine parity. Form: **state projection/query**.

For every answer resting on a governance artifact, Syzygy SHALL expose
the artifact's owning authority and governing revision, and SHALL
distinguish the artifact's self-declared lifecycle stamp (untrusted
content) from its effective status (derived from the owner-act record).
Where they disagree, the effective status governs and the disagreement
renders as a disclosed fact. An artifact with no owner-act record
renders effectively unadopted whatever its stamp claims.

- **Case**: a checker presents an artifact whose stamp says `accepted`
  with no owner-act record, and queries an answer resting on it.
- **Observable**: the served effective status, the stamp, and the
  disclosed disagreement.
- **Oracle**: the served effective status is unadopted; both values are
  separately readable in the fact set. Bounded: one artifact, one fact
  set.
- **Oracle independence**: the fixture controls the stamp and the
  absence of a record; the rule is RFC3-16's.
- **Falsifier**: a stamped-but-unrecorded artifact served as effectively
  accepted, or stamp and effective status merged into one
  indistinguishable field.

#### Scenario: Stamp is not status

- **WHEN** an answer rests on an artifact self-declaring `accepted` with
  no owner-act record binding its digest
- **THEN** the fact set serves effective status unadopted, shows the
  stamp separately, and the answer treats the artifact as unadopted

```yaml
warrants:
  primary: RFC3-16
  doctrine: [VIS-4]
  contracts: [RFC3-16, "RFC3-16(a)", RFC6-13, RFC6-14]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-050 — Per-repository discoverability, in the closed four-value vocabulary

Group: Repository discoverability. Form: **state projection/query**.

For every repository of a governed project, Syzygy SHALL answer, at the
producing evaluation: does the repository's root README link to the
fixed Syzygy project entry? The answer domain is closed at four values —
`yes` / `no` / `not-applicable` / `Unknown` — carried verbatim on every
rendering and machine answer. The read subject is the repository's root
README; no configurable landing document is an input to this finding.
Applicability precedes the read: a repository satisfying the accepted
`not-applicable` condition (no governance root — requirement 052)
renders `not-applicable` regardless of its README's content; `yes` and
`no` are answered only where that condition does not hold.

- **Case**: a checker queries discoverability for a project declaring
  several repositories in differing conditions.
- **Observable**: one finding per repository, human view and machine
  answer.
- **Oracle**: one finding per declared repository; every value is one of
  the four spellings, verbatim; count and string comparison. Bounded by
  the declared repository count.
- **Oracle independence**: the domain is fixed by the accepted contract
  (RFC7-40), outside the implementation.
- **Falsifier**: a fifth value, a paraphrased spelling, a finding
  missing for a declared repository, or a finding computed from anything
  other than the root README.

#### Scenario: Closed domain served verbatim

- **WHEN** discoverability findings are served for a project
- **THEN** every finding's value is exactly one of `yes`, `no`,
  `not-applicable`, `Unknown`

```yaml
warrants:
  primary: RFC7-40
  doctrine: []
  contracts: [RFC7-40, RFC6-14]
  policies: []
  decisions: ["P-38-ruling-2026-08-16 (decisions/HUMAN-ENTRY-DECISION.md)"]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-051 — yes and no require current evidence; missing evidence is Unknown with its reason

Group: Repository discoverability. Form: **invariant**.

A `yes` finding SHALL rest on current evidence, captured at the
producing evaluation, that the repository's root README links to the
fixed entry. A `no` finding SHALL rest on current evidence that the root
README exists and does not provide the link — rendered truthfully, not
as an error. Missing or unreadable evidence SHALL yield `Unknown`
carrying its verbatim reason from the closed vocabulary
(`source-uncaptured-or-unreachable` where the front door was not
captured; `missing-declaration` where no declaration establishes the
repository's membership; `unconsented-source-or-provider` where the
repository is unconsented, cited from its upstream rule).

- **Case** (scope of quantification): every discoverability finding
  served for a multi-repository fixture project whose repositories
  include (a) a linking README, (b) a README without the link, (c) an
  uncaptured README, and (d) an unconsented repository; counterexample
  schema: a `yes` or `no` finding with no resolvable captured evidence
  at the producing evaluation, or a missing-evidence finding that is not
  `Unknown` with its verbatim reason; sweep: enumerate all served
  findings and join each to its evidence or reason — denominator: the
  declared repository count.
- **Observable**: the served findings, each joined to its evidence or
  reason.
- **Oracle**: (a) `yes` with resolvable evidence at the evaluation; (b)
  `no` with resolvable evidence; (c) and (d) `Unknown` with the exact
  applicable reason string; no finding outside those joins. Bounded by
  the declared repository count.
- **Oracle independence**: fixtures control the conditions; spellings
  come from the closed vocabularies.
- **Falsifier**: `yes` or `no` served with no capturable evidence at the
  evaluation, an owner-declined link rendered as an error, or an
  `Unknown` finding without a reason.

#### Scenario: Declined link is a truthful no

- **WHEN** a repository's root README exists, was captured, and does not
  link to the fixed entry
- **THEN** the finding renders `no` with the captured evidence — not an
  error and not `Unknown`

#### Scenario: Unreadable front door

- **WHEN** a repository's root README could not be captured at the
  producing evaluation
- **THEN** the finding renders `Unknown` with reason
  `source-uncaptured-or-unreachable`

```yaml
warrants:
  primary: RFC7-40
  doctrine: [VIS-2]
  contracts: [RFC7-40, RFC2-24]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-052 — not-applicable only under its accepted condition

Group: Repository discoverability. Form: **prohibition**.

The `not-applicable` value SHALL be used only under its accepted
condition — the repository has no governance root and can host no entry
— carrying the declared basis for the limitation. It is a value of this
finding's own domain, never RFC6-5's navigation outcome of the same
spelling, and it SHALL never be stamped with or counted among Unknown
reasons. A repository without a governance root SHALL NOT render a
truthful-looking `no`.

- **Case** (scope of quantification): every served `not-applicable`
  finding and every repository without a governance root;
  counterexample schema: `not-applicable` served for a repository that
  could host the entry, or `no` served for one that cannot; sweep: for a
  multi-repository fixture, join each finding to the repository's
  declared role — denominator: the declared repository count.
- **Observable**: findings joined to declared roles.
- **Oracle**: `not-applicable` appears exactly on the repositories
  satisfying the accepted condition, with the basis served. Bounded by
  the repository count.
- **Oracle independence**: roles come from the declaration; the
  condition from the accepted contract and P-38 ruling.
- **Falsifier**: `not-applicable` on a governance root, or `no` on a
  repository with no governance root.

#### Scenario: No governance root

- **WHEN** discoverability is computed for an observed-source repository
  that hosts no governance root
- **THEN** the finding renders `not-applicable` with its declared basis,
  not `no`

```yaml
warrants:
  primary: RFC7-40
  doctrine: [VIS-2]
  contracts: [RFC7-40]
  policies: []
  decisions: ["P-38-ruling-2026-08-16 (decisions/HUMAN-ENTRY-DECISION.md)"]
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-053 — Syzygy may propose the link; it never writes it, and a proposal never renders as applied

Group: Repository discoverability. Form: **prohibition**.

Syzygy MAY draft a proposed repository-entry link as a Proposal
(RFC1-27). Syzygy SHALL NOT directly write the root README or any other
location outside its two writable namespaces, and a proposed link SHALL
never be rendered, counted, or served as an applied change: the finding
stays computed from the actual front door, and the proposal renders as
proposed material, visually and machine-readably distinct, with no
status authority.

- **Case** (scope of quantification): every write Syzygy performs and
  every rendering of a proposed link in a fixture where a link proposal
  exists; counterexample schema: a write outside the two namespaces, or
  a `yes` finding resting on the proposal; sweep: record all writes;
  enumerate the finding and proposal renderings — denominator: the write
  set and the rendering set.
- **Observable**: the write record — captured externally to Syzygy by
  the checking harness (filesystem comparison or harness-level write
  tracing), not solely Syzygy's own log; the finding value; the proposal
  rendering.
- **Oracle**: no write path outside `openspec/**` and `.syzygy/**`; the
  finding over an unlinked README remains `no` while the proposal is
  open; the proposal carries proposed-state marking. Bounded by the
  enumerations.
- **Oracle independence**: writes and served values are facts; the
  boundary is doctrine's.
- **Falsifier**: a root README edited by Syzygy, or a finding flipped to
  `yes` by the existence of an unapplied proposal.

#### Scenario: Proposal does not change the finding

- **WHEN** Syzygy has proposed a repository-entry link and the root
  README does not yet contain it
- **THEN** the finding remains `no` (with evidence) and the proposal
  renders as an unapplied proposed change

```yaml
warrants:
  primary: RFC7-40
  doctrine: [VIS-5]
  contracts: [RFC7-40, RFC1-27, RFC3-3]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-060 — Identities are the accepted, stable, literal ones

Group: Cross-cutting. Form: **invariant**.

Capability 1 SHALL identify projects and repositories by their declared
opaque identifiers: a display name is a label, never an identity;
renaming changes the label and no identifier; a repository's identity is
never a URL, path, or branch. No implementation-specific identifier is
introduced as a project or repository identity in any served answer.

- **Case** (scope of quantification): every identity-bearing field in
  Capability 1's served answers; counterexample schema: an answer keyed
  by a display name, URL, or invented ID; sweep: rename a fixture
  project and relocate a repository, then diff the identity fields of
  answers before and after — denominator: the identity-field set.
- **Observable**: identity fields across the rename/relocate fixtures.
- **Oracle**: identity fields are unchanged by rename and relocation;
  labels change. Bounded by the field set.
- **Oracle independence**: the declared identifiers are the fixture's
  own; stability is judged by diff.
- **Falsifier**: a bookmarklike reference or machine answer that breaks
  on rename, or a served identity equal to a URL or path.

#### Scenario: Rename changes no identity

- **WHEN** a registered project's display name changes with its
  identifier unchanged
- **THEN** every Capability 1 answer keys on the same identifier and
  serves the new label as a label

```yaml
warrants:
  primary: RFC1-10
  doctrine: []
  contracts: [RFC1-10, RFC1-2, RFC3-6]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-061 — Capability 1 observes and presents; its write boundary is the governed plane

Group: Cross-cutting. Form: **prohibition**.

Capability 1's behavior SHALL cause no mutation beyond governed
proposals and Syzygy-owned presentation or specification artifacts
inside `openspec/**` and `.syzygy/**` where accepted authority permits
them. No source-code edit, root-README edit, deployment, scheduler
mutation, or other external effect is part of this capability, and no
manifest field may widen that write universe: a field purporting to do
so is inoperative and renders as a contradiction routed to the owner.

- **Case** (scope of quantification): every write and external effect
  during Capability 1 fixtures, including one whose declaration carries
  a write-widening field; counterexample schema: a write outside the two
  namespaces, an external effect, or a widening field honored; sweep:
  record all writes and effects **externally to Syzygy** — filesystem
  comparison for writes, plus the harness's record of every external
  interface the fixture exposes (network, scheduler, process spawn) for
  effects; check the widening-field fixture's rendering — denominator:
  the harness-recorded effect set over the fixture's enumerated
  interfaces.
- **Observable**: the harness's external write/effect record,
  cross-checked against Syzygy's attributed-write record; the
  contradiction rendering.
- **Oracle**: every effect is a permitted in-plane write; the widening
  field is not honored and renders as a contradiction. Bounded by the
  effect set.
- **Oracle independence**: the effect population is established by the
  harness's own tracing over interfaces it controls, never solely by
  Syzygy's self-report; the boundary is doctrine's and the contract's.
- **Falsifier**: any external mutation during Capability 1 behavior, or
  a `write_roots:`-style field honored.

#### Scenario: Widening field is inoperative

- **WHEN** a declaration carries a field purporting to grant Syzygy
  write access outside the two namespaces
- **THEN** the field is not honored and its presence renders as a
  contradiction routed to the owner

```yaml
warrants:
  primary: RFC3-3
  doctrine: [VIS-5]
  contracts: [RFC3-3, RFC1-27]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-062 — Stale evidence cannot silently remain current or favourable

Group: Cross-cutting. Form: **invariant**.

Evidence past its declared currency bound at the evaluation's as-of
instant SHALL NOT support a current or favourable answer: the dependent
claim renders `Unknown` with reason `stale-beyond-currency-bound`, and a
claim class with no declared currency bound renders `Unknown` with
reason `no-currency-bound-declared`. Staleness of superseded
observations is visible on the primary surface. A displayed answer
changes only through a new identified evaluation — never by the wall
clock silently.

- **Case** (scope of quantification): every claim served for fixtures
  with (a) evidence older than its declared bound at the evaluation's
  as-of instant and (b) a claim class with no declared bound;
  counterexample schema: a current or favourable value resting on
  out-of-bound evidence, an unbounded claim class rendering favourably,
  or a value differing between two reads of one evaluation; sweep:
  enumerate the served claims in both fixtures and join each to its
  evidence age and declared bound — denominator: the served claim set
  per fixture, plus one repeated read of the whole set.
- **Observable**: the served claim values and reasons, joined to
  evidence ages and bounds; the staleness markings.
- **Oracle**: every out-of-bound claim serves `Unknown` reason #4; every
  unbounded-class claim serves `Unknown` reason #3; string comparison
  per claim; and no served value differs between two reads of one
  evaluation at different wall-clock times. Bounded by the served claim
  sets.
- **Oracle independence**: the fixtures control evidence age and bound
  declarations; the reason spellings are the closed vocabulary's.
- **Falsifier**: stale evidence supporting a favourable answer, an
  unbounded claim class rendering favourably, or an answer flipping with
  no new evaluation.

#### Scenario: Stale evidence degrades

- **WHEN** a shape answer's only evidence exceeds its declared currency
  bound at the evaluation's as-of instant
- **THEN** the answer renders `Unknown` with reason
  `stale-beyond-currency-bound`

```yaml
warrants:
  primary: RFC2-24
  doctrine: [VIS-2]
  contracts: [RFC2-24, RFC2-23]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-063 — Proposed material never renders as current state

Group: Cross-cutting. Form: **prohibition**.

No unadopted Proposal — a drafted declaration repair, a drafted entry, a
proposed repository-entry link — SHALL render as current or adopted
state anywhere in Capability 1: proposed material is unmistakably
distinct, visually and machine-readably, carries no status authority,
and turns nothing favourable.

- **Case** (scope of quantification): every rendering of proposed
  material in Capability 1 fixtures; counterexample schema: a proposal
  rendered without proposed-state marking, or a status value that
  changes because a proposal exists; sweep: enumerate proposal
  renderings and diff status values with and without the proposal —
  denominator: the rendering set and the status set.
- **Observable**: proposal renderings and status values.
- **Oracle**: every proposal rendering carries the proposed marking;
  status values are identical with and without the open proposal.
  Bounded by the enumerations.
- **Oracle independence**: the marking is inspectable; the plane rule is
  the accepted contract's.
- **Falsifier**: a drafted repair shown as the declaration's content, or
  any answer improved by an unadopted proposal.

#### Scenario: Proposal changes no status

- **WHEN** a proposal exists against a project and the same query is
  made with and without it
- **THEN** every Capability 1 status value is identical, and the
  proposal renders only as proposed material

```yaml
warrants:
  primary: RFC1-27
  doctrine: [VIS-1]
  contracts: [RFC1-27, RFC1-22]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```

### Requirement: CAP1-REQ-064 — Every distinction is machine-readable and recoverable without vision

Group: Cross-cutting. Form: **invariant**.

Every distinction Capability 1 draws — epistemic label, tier, Unknown
reason, freshness, consent state, adopted versus unadopted, proposed
versus current, effective status versus stamp, the four-value
discoverability domain — SHALL be carried as a machine-readable
attribute on the rendered unit and SHALL be recoverable without colour,
position, or layout, by label, text, or structure. Accessibility of the
behavior is required; no UI framework is specified.

- **Case** (scope of quantification): every distinction named above,
  over Capability 1's served renderings; counterexample schema: a
  distinction carried only by pixels (colour, position, layout); sweep:
  export each fixture rendering to plain text or its machine form and
  check each distinction is still recoverable — denominator: the
  distinction list crossed with the rendering channels.
- **Observable**: exported and machine renderings.
- **Oracle**: every listed distinction survives export and appears as an
  attribute in the machine answer. Bounded by the crossed enumeration.
- **Oracle independence**: recoverability is checked in the exported
  bytes, not in the interactive view.
- **Falsifier**: a distinction visible only as a colour or a screen
  position, absent from the plain-text and machine forms.

#### Scenario: Distinctions survive plain text

- **WHEN** a Capability 1 rendering is exported to plain text
- **THEN** the epistemic labels, Unknown reasons, proposed/current
  markings, and discoverability values in it remain recoverable

```yaml
warrants:
  primary: RFC7-33
  doctrine: [VIS-1, VIS-3]
  contracts: [RFC7-33, RFC7-34, RFC6-14]
  policies: []
  decisions: []
  topology: []
  parent_requirements: []
```
