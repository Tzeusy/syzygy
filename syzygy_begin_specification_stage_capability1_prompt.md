# Syzygy — Begin the Specification Stage with Capability 1

Run this prompt in a **fresh Claude Fable / Opus session** at the root of
`Tzeusy/syzygy`.

This prompt is the owner’s authorization to leave the product-vision and
project-shape stage and begin defining required observable behavior.

The first OpenSpec change is:

```text
Capability 1 — Project registration and honest shape visibility
```

This is one shared product capability. It is not a Polaris-only,
Trajectory-only, or Orrery-only feature. It establishes the truthful project
foundation all three views and all machine consumers will later use.

Do not author the later Polaris, Trajectory, Orrery, cross-view, Mission
Control, or deterministic-context capabilities in this pass.

---

# Owner decision carried by this prompt

Record the following as a made owner decision in the repository’s existing
decision system:

> **AUTHORIZE CAPABILITY 1 SPECIFICATION AUTHORING**
>
> The adopted doctrine, accepted Waves A and B, recorded owner decisions, and
> in-force specification-quality and shape-to-specification policies define a
> sufficiently clear and coherent project shape for Capability 1.
>
> Administration 1 is accepted as useful diagnostic evidence. Its remaining
> findings have either been repaired, explicitly deferred, placed outside
> Capability 1, or knowingly accepted as process risks. No further
> repository-wide pre-specification review or launch-gate administration is
> required before Capability 1 is defined.
>
> Project-shape questions may reopen only when specification authoring exposes
> a concrete contradiction, a missing lawful authority, or a requirement that
> cannot be made testable.
>
> This decision authorizes specification definition only. It does not
> authorize implementation, implementation planning, agent orchestration,
> deployment, or code changes.

This prompt is itself an explicit owner instruction. Record the decision as
such. Do not imply that an LLM made the decision and do not rewrite it into a
broader authorization.

Update only the current pointer documents needed to reflect the lifecycle
transition:

```text
final pre-specification
→ specification defining
```

Do not edit adopted doctrine or accepted contract bytes merely to update
current status.

Do not alter or reinterpret the historical launch-gate verdict. Record the
owner’s launch decision separately, as the launch-gate policy already
requires.

---

# Governing objective

Produce one concise, human-readable, falsifiable OpenSpec change defining the
observable behavior of Capability 1.

A technically capable engineer with no Syzygy authoring history should be able
to read the resulting change and answer:

```text
What user problem does this capability solve?
What does the system do?
What does it refuse to claim or do?
What would prove each requirement satisfied?
What observation would prove each requirement violated?
Which accepted rule or owner decision warrants each requirement?
What remains Unknown or deliberately deferred?
```

The specification must be usable by both:

```text
a human implementing or reviewing the product
an agent receiving the specification as governed task context
```

It must not require either reader to study the project’s review history.

---

# Verify the repository state before writing

Read current `main` and current `HEAD`. Do not trust this prompt’s snapshot
over newer committed authority.

At the time this prompt was prepared, the repository had:

```text
Wave A accepted
Wave B accepted
CC-SPEC in force
CC-IMPACT in force
OpenSpec 1.9.0 selected
Capability 1 planning metadata present
no behavioral specification content
no application implementation
```

Confirm the current state from the owning records.

Read:

```text
README.md
AGENTS.md
PROJECT-STATUS.md

.syzygy/governance/doctrine/README.md
.syzygy/governance/doctrine/vision.md
.syzygy/governance/doctrine/v1.md
.syzygy/governance/doctrine/architecture.md
.syzygy/governance/doctrine/trust-and-evidence.md

.syzygy/governance/decisions/README.md
.syzygy/governance/decisions/DECISION-HISTORY.md
.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md
.syzygy/governance/decisions/HUMAN-ENTRY-DECISION.md
.syzygy/governance/decisions/OPENSPEC-FORM-AND-VERSION-DECISION.md
.syzygy/governance/decisions/SPECIFICATION-GRANULARITY-DECISION.md
.syzygy/governance/decisions/PROJECT-OPERATING-CONSTRAINTS-DECISION.md
.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md

.syzygy/governance/contracts/rfcs/
.syzygy/governance/contracts/candidates/CAPABILITY-1-CHARTER.yaml
.syzygy/governance/contracts/candidates/CAPABILITY-1-GENERATED-VIEWS.md
.syzygy/governance/contracts/candidates/FIRST-OPENSPEC-SEQUENCE.md
.syzygy/governance/contracts/candidates/TASK-ROUTER.md
.syzygy/governance/contracts/candidates/SURFACE-CLAUSE-ROUTING-MATRIX.md

.syzygy/governance/contracts/candidates/policy-candidates/
  SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md
.syzygy/governance/contracts/candidates/policy-candidates/
  SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md

openspec/config.yaml
```

The two policy files above are stored under a historical `policy-candidates`
path but bind through their performed owner acts. The act record and craft
installation record own their effective status. Do not treat their old banner
wording as their current lifecycle.

Use the accepted copies of RFC 0001–0009 under
`.syzygy/governance/contracts/rfcs/` as authority. Candidate copies, generated
indexes, charters, routes, and sequence documents are navigation or planning
material only.

Do not read prior review rounds by default. Open a historical review only when
a current authoritative clause or decision explicitly requires its exact
record.

---

# Keep the stage transition small

Do not run another repository-wide review.

Do not administer the launch gate again.

Do not revisit the complete project shape.

Do not review deferred Waves C1, C2, D1, or D2.

Do not reopen an owner decision merely because another option can be imagined.

A project-shape issue blocks this specification only when all of the following
are true:

1. It lies directly on Capability 1’s path.
2. It creates a real contradiction with adopted doctrine, an accepted
   contract, an in-force policy, or a recorded owner decision.
3. A concrete requirement cannot be written truthfully without settling it.
4. It cannot be represented as an explicit Unknown, non-goal, or deferred
   behavior.
5. It would materially mislead a human or machine consumer.

If all five are not true, record it as a later concern and continue.

Do not create another active report for such concerns. Use the existing
decision queue or a single post-specification backlog record.

---

# Use the installed OpenSpec workflow

The selected medium is OpenSpec 1.9.0 with the `spec-driven` schema.

Before creating artifacts:

1. Run the installed OpenSpec CLI help and instruction commands.
2. Read the installed `/th-projects project-feature-request` workflow.
3. Follow the actual installed artifact schema and dependency order.
4. Do not invent an obsolete OpenSpec directory shape from memory.
5. Do not change the selected OpenSpec version or schema in this pass.

Create exactly one OpenSpec change with the literal identifier:

```text
project-registration-and-honest-shape-visibility
```

One change means:

```text
one coherent capability
one owner-readable product argument
one future acceptance decision
```

The change may contain several requirement sections or files when the
installed schema calls for them. It must not become several independently
adoptable capabilities disguised as one change.

Do not create implementation tasks. If the installed schema requires a tasks
artifact, state plainly that implementation planning is deferred until the
specification is adopted and include no technical backlog.

Do not invoke `/beads-orchestration`.

Do not create implementation Beads.

---

# The one-sentence product argument

Use this as the starting argument, refining only for clarity without expanding
scope:

> A project can be registered and its shape read honestly: every project
> answer stands on its own, every Unknown carries its reason and owning
> authority, and humans and machines receive the same facts without
> registration being mistaken for certification.

A fresh reader must be able to restate this without learning Syzygy’s internal
history or process vocabulary.

---

# Required behavior

Start from the six existing Capability 1 behavior rows. They are planning
inputs, not authority; resolve every cited identifier against its accepted
home.

## 1. Project declaration

Define observable behavior for reading and validating the project declaration.

At minimum:

- A valid declaration produces one identified registered project.
- An invalid declaration produces one or more named validation failures.
- Invalid input never produces a partly registered project.
- Missing required information is visible.
- Syzygy does not silently invent, repair, or infer a declaration field.
- Re-reading the same valid declaration at the same project revision produces
  the same registration facts.

Do not choose implementation schema libraries, parser technology, storage, or
transport.

## 2. Consent and repository coverage

Define observable behavior for showing what Syzygy may and may not inspect.

At minimum:

- Each declared repository or source has an explicit coverage result.
- Consent is a visible fact, not an assumption.
- Missing consent, inaccessible sources, stale observation, and failed
  observation are distinguishable where the accepted vocabulary requires it.
- Incomplete coverage is never rendered as complete coverage.
- A human and a machine can retrieve the same coverage boundary.
- No source is inspected through authority the project did not grant.

Do not define the later execution-profile mechanics beyond behavior already
required by accepted contracts.

## 3. Human project entry

Define the fixed Syzygy-owned human entry:

```text
.syzygy/intent/OVERVIEW.md
```

At minimum:

- A governed project has one fixed Syzygy-owned entry path.
- The entry explains what project is being viewed and routes to exact
  authority.
- The entry is governed presentation and cannot become the source of project
  truth.
- Missing, unreadable, stale, or contradictory entry material is represented
  honestly.
- The behavior does not require Syzygy to write outside its governed plane.

Use the recorded P-38 decision exactly. Do not create a second default entry
file.

## 4. Independent project-shape answers

Define the seven owner-ratified project-shape answers in the Capability 1
specification, because the owner selected this specification as their
authority site:

```text
Registered
Shape present
Human-understandable
Observable
Traceable
Mission-ready
Reconciled
```

Read the exact P-37 decision and preserve its accepted meanings.

Requirements:

- Each answer is computed and presented independently.
- There is no combined score, badge, colour, percentage, or count of passing
  answers.
- Registration is never certification.
- Each answer exposes its constituent facts and scope.
- Missing evidence yields Unknown rather than a favourable answer.
- Several reasons may be visible at once; one reason must not hide the others.
- Mission-ready is present only in the owner-ratified deferred posture:
  `not evaluated / deferred / Unknown` while its governing Context and Mission
  contracts remain unaccepted.
- Uncomputed reconciliation is Unknown.
- A negative or Unknown answer does not erase the other answers.

Use ordinary language first. The seven labels are product vocabulary; do not
invent additional maturity terms around them.

## 5. Explanation and human/machine parity

Every answer produced by Capability 1 must be explainable.

Where applicable, the human and machine representations expose the same
underlying facts:

```text
owning authority
governing revision
source or evidence revision
state category
evidence classification
evaluation identity
freshness
Unknown reason or reasons
coverage and consent boundary
active challenge
active contradiction
related work state
reconciliation state
```

Use only fields warranted by accepted clauses.

Requirements:

- The human view and machine interface may format information differently but
  may not disagree on meaning.
- Equivalent queries over the same project revision expose equivalent facts.
- A disagreement is visible and fails the applicable requirement; it is not
  resolved by presentation precedence.
- A missing explanation cannot be replaced with an optimistic summary.
- Generated presentation is never the source of the answer.
- Inferred information is distinguishable from observed information.

Call the human interaction something literal such as:

```text
Why this answer?
```

unless accepted product wording already governs it.

Do not define the future transport, endpoint protocol, framework, or data
store.

## 6. Repository discoverability

Define how Syzygy reports whether a repository’s ordinary entry helps a
newcomer find the Syzygy project entry.

Use the owner-ratified closed result vocabulary:

```text
yes
no
not applicable
Unknown
```

At minimum:

- The result is computed per repository.
- `yes` requires current evidence that the configured repository entry links
  to the fixed Syzygy entry.
- `no` requires current evidence that the relevant entry exists and does not
  provide the link.
- `not applicable` is used only under its accepted condition.
- Missing or unreadable evidence yields Unknown.
- Syzygy may propose a repository-entry link.
- Syzygy must not directly write the root README or another location outside
  its allowed project plane.
- A proposal is not rendered as an applied change.

Do not broaden this into repository editing, onboarding automation, or
cross-repository content management.

---

# Cross-cutting requirements

The specification must explicitly include these cross-cutting behaviors where
they are not already fully represented above.

## No false success

- No evidence yields Unknown.
- Stale evidence cannot silently remain current or favourable.
- Registration does not imply that project shape exists, is understandable,
  is observable, is traceable, is Mission-ready, or is reconciled.
- Absence is not zero.
- A proposal is not current state.

## Same facts for humans and machines

- Human-readable and machine-queryable outputs use the same project identity,
  project revision, observation identity, and underlying facts.
- Presentation-specific metadata does not become project truth.
- A machine consumer can retrieve every substantive fact needed to explain
  the corresponding human answer.
- Accessibility and non-visual use are considered in the behavior, without
  specifying a UI framework.

## Stable and literal identity

- Use accepted project and repository identities.
- Do not introduce display names as identity.
- Do not invent implementation-specific IDs.
- Requirement IDs are stable, never renumbered, reused, or silently deleted.

## Write boundary

- Capability 1 observes and presents.
- The only permitted mutation in this scope is a governed proposal or
  Syzygy-owned presentation/specification artifact where accepted authority
  permits it.
- No source-code edit, root-README edit, deployment, scheduler mutation, or
  external effect is part of this capability.

---

# Explicit non-goals

The resulting change must state that Capability 1 does not:

- certify a project;
- produce one overall health or maturity score;
- implement Polaris’s full project white paper;
- implement Trajectory work ingestion or execution accounting;
- implement Orrery’s 3D project map;
- execute or monitor Missions;
- generate task-specific context packets;
- calculate complete intent-to-code convergence;
- modify source code;
- edit a repository root README;
- create Beads work;
- select an implementation language, framework, database, renderer, graph
  store, or deployment model;
- register or onboard a real external project during specification authoring;
- implement anything.

These are true scope boundaries, not promises that every item is next.

---

# Requirement quality rules

Follow the in-force `CC-SPEC-1…11` rules exactly.

## Stable requirement identity

Use stable, literal identifiers such as:

```text
CAP1-REQ-001
CAP1-REQ-002
...
```

Use the installed OpenSpec identifier convention when it is stricter.

Never renumber an identifier after review. Retire rather than reuse.

## Governing warrants

For every requirement, provide the machine-readable governing identities
required by `CC-SPEC-2`:

```text
doctrine[]
contracts[]
policies[]
decisions[]
topology[]
parent_requirements[]
```

Name all material warrants, not merely one convenient source.

Only cite adopted, accepted, approved, or recorded authority.

Do not cite:

```text
the Capability 1 charter
a generated route
a candidate review
a pending decision
a summary
this prompt
```

as a governing warrant.

The owner launch decision recorded from this prompt may be cited only as
authorization to author the change, not as product-behavior authority.

## Requirement forms

Every requirement names one accepted form:

```text
event-response
state projection/query
invariant
prohibition
lifecycle transition
```

Every requirement states:

```text
reachable or bounded case
observable consequence or violation
effective success/failure oracle
why the oracle is independent of the implementation under test
concrete falsifying evidence
```

Reject tautological oracles, implementation-as-oracle, unreachable cases, and
unbounded “semantic equivalence” claims.

## Unknowns and non-goals

Every material Unknown states:

```text
what is unknown
why it is unknown
what evidence or owner decision would settle it
whether it blocks this capability
```

Do not use an Unknown to hide a decision that the accepted shape already made.

## No silent shape changes

Before freezing the specification, compare every requirement against the open
owner-decision queue.

If a requirement would settle a genuinely open shape question, mark it as a
blocker and present the exact issue to the owner.

Do not reopen deferred Mission or Context-selection questions merely because
their words appear in the project vocabulary.

## Implementation independence

Do not mention implementation details unless the observable behavior itself
requires them.

Do not choose:

```text
language
framework
database
graph technology
file-watcher
API transport
browser library
3D engine
authentication mechanism
deployment topology
```

The accepted local-first and human/machine commitments may appear as required
behavior only where they actually govern Capability 1.

---

# Coverage artifacts

The OpenSpec change must ship with two concise coverage views.

## Capability coverage

List every declared Capability 1 obligation and place it in exactly one set:

```text
covered by requirement IDs
lawfully out of scope, naming the non-goal
Unknown/unresolved, naming what settles it
```

The population is the obligations declared in the proposal and scope.

All six behavior groups must be represented.

## Contract-to-requirement coverage

Use the accepted phase-rule and specification policy.

For every applicable observable consequence of the accepted Wave A/B clauses:

```text
map it to one or more requirement IDs
or
identify a lawful owner-reviewed N/A judgment
```

Do not create N/A judgments on the author’s authority.

If no owner-reviewed N/A record exists, keep the consequence uncovered and
render the result Unknown; do not pretend review itself grants the judgment.

The coverage unit is an observable consequence, not merely a clause number.

Generate specification-level governing dependencies as the union of the
requirements’ governing declarations, as required by `CC-IMPACT-1`.

No second hand-maintained dependency list.

---

# Initial specification decomposition

Keep one OpenSpec change and one owner-readable argument.

Within that change, organize the requirements into a small number of literal
groups:

```text
Project declaration
Consent and coverage
Human project entry
Independent project-shape answers
Why this answer and human/machine parity
Repository discoverability
```

Do not mint new product names for these groups.

Do not split them into independently adoptable changes during this pass.

If the installed OpenSpec schema uses one specification document per
capability, keep them as sections in the one Capability 1 specification.

---

# Authoring workflow

Use this bounded process.

## Pass 1 — Draft

Create the OpenSpec change and all artifacts required by the installed schema.

Keep the main proposal concise:

```text
problem
one-sentence capability
why this capability is first
scope
non-goals
user-visible outcomes
machine-consumer outcomes
Unknowns
acceptance approach
```

Do not include the history of how Syzygy reached this stage.

## Pass 2 — Three bounded reviews

Run three independent fresh-context reviewers over the exact draft.

### Human comprehension reviewer

Given only:

```text
the specification
the directly cited doctrine/contract/decision clauses
the acceptance criteria
```

Ask whether an unfamiliar technical reader can correctly explain the
capability, its boundaries, and its success conditions.

### Behavior and testability reviewer

Check:

- every requirement has a valid form;
- every case is reachable or bounded;
- every oracle terminates and is implementation-independent;
- every falsifier is concrete;
- no requirement is an implementation plan.

### Authority and coverage reviewer

Check:

- every material warrant is named;
- every warrant is accepted or recorded;
- no generated or candidate artifact is treated as authority;
- the capability and contract coverage tables are complete;
- no unresolved shape decision was silently selected.

Each reviewer may return at most:

```text
5 blockers
5 non-blocking findings
```

A blocker must show a concrete failure in this specification.

Do not ask reviewers to audit the whole repository.

## Pass 3 — One repair

Repair the consolidated blockers once.

Do not churn the specification for non-blocking stylistic preferences.

## Pass 4 — Confirmation

Run one fresh confirming review over the changed bytes.

If a real blocker remains, stop and present the owner with:

```text
the blocker
the exact affected requirement
repair
reduce scope
defer the behavior
accept the disclosed risk
```

Do not automatically start another open-ended cycle.

---

# Validation

Run:

- the OpenSpec validator required by the installed version;
- the repository’s current canonical governance battery;
- the generated Capability 1 view/router drift checks;
- coverage completeness checks;
- a clean-clone validation over the exact review commit.

Read denominators and output, not exit codes alone.

Do not claim hosted CI is green unless a run is visible for the exact commit.

---

# Current-state updates

After the specification draft exists:

- Update `PROJECT-STATUS.md` to say specification defining is in progress.
- Update `AGENTS.md` so Capability 1 specification authoring is permitted but
  implementation remains prohibited.
- Update the one current first-specification sequence.
- Do not copy requirement totals, review totals, digests, or current status
  into several files.
- Do not update accepted doctrine or accepted contract bytes merely because a
  specification now exists.
- Do not mark the specification accepted.
- Do not create implementation work.

If the owner later adopts the specification, that is a separate exact-digest
act under `VIS-4` and `CC-SPEC-10`.

---

# Outputs

Produce only the artifacts necessary for the specification stage:

```text
a recorded Capability 1 specification-authoring launch decision
one OpenSpec change:
    project-registration-and-honest-shape-visibility
the artifacts required by the installed OpenSpec schema
stable requirements and scenarios
requirement-level governing-warrant declarations
generated specification-level dependency declaration
capability coverage
contract-to-requirement coverage
explicit non-goals and Unknowns
three raw bounded reviews
one consolidated repair record
one confirming review
updated current status and agent routing
```

Do not create:

```text
application code
implementation tasks
implementation Beads
architecture selection
database or framework proposals
a new project-shape review
another launch-gate administration
a specification for later capabilities
```

At the end, provide a concise owner-facing summary:

```text
What Capability 1 now requires
What it deliberately does not require
Any remaining blocker
The exact OpenSpec artifacts created
The exact validation commands and results
Whether the change is ready for owner adoption
```

Do not perform the owner’s specification-adoption act.

---

# What comes after this pass

Do not author these now, but update the non-authoritative sequence so the next
specification families are clear:

```text
Shared foundation
    Project registration and honest shape visibility
    Deterministic context packet generation, later

Polaris
    Minimum project comprehension

Trajectory
    Minimum work truth and reconciliation visibility

Orrery
    Minimum structural project map

Cross-view
    Shared selection, deep links, revision consistency, evidence consistency,
    and Unknown propagation

Integrated proof
    One real capability exercised across all three views
```

Mission Control remains a separate later family.

Do not turn this roadmap into requirements inside Capability 1.

---

# Stop condition

Stop when one reviewed Capability 1 OpenSpec change exists and is ready for the
owner’s adoption decision.

Do not continue into implementation.

Do not perform another repository-wide review.

Do not expand the capability because later product areas are interesting.

The success condition is:

> A fresh engineer can read one concise OpenSpec change and understand exactly
> how Syzygy registers a project, shows the limits of what it can know,
> provides a human entry, reports project shape without a false score, explains
> every answer, and gives humans and machines the same truth.
