# Semantic delta — PWB derived read-only machine views (PWB-REQ-020)

> **Candidate — binds nothing.** Agents drafted these bytes under the owner's
> 2026-09-21 P-68…P-83 pursuit ruling, which authorizes drafting and nothing
> else. Only the human owner may amend the signed PWB behavior, by an act
> over the digest of `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` recorded in
> `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`. Silence, a commit,
> a review, a merged pull request or a manifest performs no act. Nothing here
> authorizes an implementation.

**Artifact(s):**

- `openspec/changes/polaris-project-wide-butlers-model/` (the
  eleven-artifact signed PWB behavioral package, one indivisible subject).
  Two of the eleven change:
  `specs/polaris-project-wide-butlers-model/spec.md` (one block of prose
  inserted inside PWB-REQ-020; nothing removed, nothing reworded) and
  `GOVERNING-DEPENDENCIES.md`, whose single `Source:` line carries the
  specification's sha256 and therefore moves whenever the specification
  does. The other nine rows of `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` equal
  current bytes.
- No contract module, policy, doctrine file or registry declaration is
  amended by this package. In particular the adapter-registry entry
  `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
  is **not** a subject here; its `resourceLimits` envelope is the subject of
  the sibling candidate `pwb-registry-currency-briefing-amendment`, which
  mints the briefing ceiling (P-72 Q2, gate bead `syzygy-dov.18`).

**Stable IDs affected:** `PWB-REQ-020`. No requirement is minted, retired or
renumbered. No `warrants:` block changes, so every identifier table in the
generated `GOVERNING-DEPENDENCIES.md` is byte-identical and only its
generated `Source:` digest line moves — 17 requirements and 96 distinct
authorities before and after [Observed; the builder re-derives the proposed
declaration from the proposed specification with the generator CI runs].
`PWB-REQ-004`, `PWB-REQ-011`, `PWB-REQ-014` and `PWB-REQ-016` are **not**
amended; the section "What explicitly does NOT change" says why each is a
reader's reasonable guess and what happens to it instead.

**Change class:** **Normative.** Argued below under "The change class, and
where this delta contradicts its own source"; the analysis this delta comes
from recommends *Clarifying*, and that recommendation does not survive the
template's own test.

**Author:** the pursuit session for bead `syzygy-dov.22` (agents), drafting
only. No reviewer has seen these bytes.

**Date:** 2026-09-21 (first draft).

**Baseline:** commit `a4a34510a5582edbd38c1df57a064ba3ac0a33f2`, the branch
point for this draft. None of the eleven behavior subjects changes between
that commit and the commit carrying this draft; the builder's `--check`
recomputes every row from the tree it runs in, so a later baseline is caught
rather than assumed.

## Why this delta exists

Four independent pursuit analyses each stop at the same missing sentence: the
specification says what the machine answer must contain, and says nothing at
all about a *second* machine response derived from it. Today that gap is
filled by a code comment.

| Question | What is true today, 2026-09-21 | Source |
|---|---|---|
| Is `/api/poc/polaris` in the specification? | No. The specification names no route literal anywhere. | [Observed] sweep for `/api/poc` over the specification returns 0 |
| Is it served? | Yes — registered `machine-credentialed`, in the direct and tailnet-mount forms, under `maxMachineResponseBytes`. | [Observed] `apps/three-surface-poc/src/routes.ts` |
| Is its derivability from `/api/poc` verified? | No. Its route test has two cases: credential refusal with page-anchor citation, and typed failure under the machine ceiling. Neither compares the envelope's values against the machine answer's bytes. | [Observed] `apps/three-surface-poc/src/polaris-presentation-route.test.ts` |
| Does `/api/poc/briefing` exist? | No. It occurs in 12 tracked files, every one of them under `docs/design/`, `docs/evidence/`, `docs/pursuits/` or `docs/reviews/`. | [Observed] literal sweep, this session |
| Does `/polaris/draft/<runId>` exist? | No. 4 tracked files, all in the same four directories. | [Observed] literal sweep, this session |
| Is `maxBriefingResponseBytes` declared? | No. 7 tracked files name it: the ruling record, the decision history, one funnel and four retained raw reviews. No registry file. | [Observed] literal sweep, this session |

So one member is served without a stated rule, two members are unbuilt, and
the ceiling one of them needs is unminted. The delta states the rule once,
closes the membership, and makes the unminted ceiling a precondition of
service rather than an oversight discovered later.

## Current meaning

`PWB-REQ-020` today, quoted in full and unaltered
(`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
lines 902–944 at the baseline):

````markdown
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
````

Read as it stands, the requirement is a parity invariant over two
populations: what Polaris *presents* and what the machine answer *contains*
at one evaluation. It does not say what the machine answer is called, which
route serves it, or whether anything else may be served from it. A second
machine response composed out of the machine answer is neither admitted nor
excluded — and because the Observable is an equal-multiset test, a reader can
reasonably fear that a *task-scoped* second response breaks parity by serving
fewer facts. Nothing in the text answers that fear.

## Proposed meaning

The same requirement with one block inserted between the `Group:` line and
the SHALL sentence. The insertion is the whole change; the patch
`proposed/spec.md.patch` contains no removed line. Quoted in full:

````markdown
### Requirement: PWB-REQ-020 — Project-wide facts remain identical across human and machine views

Group: Parity. Form: **invariant**.

This requirement compares the human surface against the *machine answer*: the
authenticated project-wide machine response at one evaluation. Two closed
categories of derived, read-only machine view are served beside that answer.
Neither category is the machine answer, the recoverability comparison below
ranges over neither, and a route this specification does not name is a member
of neither.

A **derived read-only machine view** composes only values already reachable
from the machine answer at the same evaluation, mints no project fact, writes
nothing, is served only to machine-credentialed clients in every mount form,
and subtracts nothing: the complete fact set stays served by the machine
answer at that same evaluation. Every value such a view serves SHALL be
independently verified as derivable from the machine answer's own bytes at
that evaluation, by a checker that imports no rendering code. The members of
this category are the Polaris presentation view, `GET /api/poc/polaris`,
served under the machine-JSON ceiling the adapter-registry entry already
declares, and the agent briefing view, `GET /api/poc/briefing`, served under a
byte ceiling of its own.

A **generated editorial draft view** composes only the recorded bytes of one
identified generation run over sources that run was already admitted to read,
mints no project fact, writes nothing, sends no source or draft byte outside
the observing project, and is served only to machine-credentialed clients in
every mount form. It carries no project-shape identity, statement, source
anchor, coverage state, denominator or contradiction, and so contributes to
neither multiset compared below. The member of this category is the
generation draft view, `GET /polaris/draft/<runId>`.

A member served under a byte ceiling of its own SHALL NOT be served before the
adapter-registry entry's resource envelope declares that ceiling. A route
enters either category only by a later amendment to this specification naming
it as a member. A route in neither category is neither admitted nor forbidden
by this requirement.

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
````

## The two categories, and why two

**Category 1, derived read-only machine view.** Its membership test is
composition: every value is already reachable from the machine answer at the
same evaluation. Its two members are the Polaris presentation view, named
retroactively, and the agent briefing view, named prospectively.

**Category 2, generated editorial draft view.** Its member fails category 1's
test by construction, which is why a second category exists rather than a
widened first one: a generation draft is composed from a recorded generation
run, not from the machine answer. The disjointness is measured, not assumed —
the pursuit analysis records zero references to the POC core model across the
generation package and the app's generation directory [Observed, recorded in
`docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md`; that file is a candidate
analysis and never authority]. Because a draft carries no project-shape item,
statement, anchor, coverage state, denominator or contradiction, it
contributes to neither multiset the requirement compares, and saying so is
what keeps the parity oracle's denominators honest when the route ships.

Both categories are **closed by enumeration**: a reader does not infer
membership, and a route nobody named is a member of neither. How a later
instance enters is stated in the text itself — an amendment to this
specification naming it as a member — so the closure does not have to be
re-argued each time the project wants a third view.

## The change class, and where this delta contradicts its own source

The analysis that recommends this delta's shape
(`docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md`, Gate 5) records the class
as *clarifying*. Under the template's own test — "someone who complied before
may not comply now" — that does not hold:

1. **A verification obligation is added.** The text says every value a
   category-1 member serves SHALL be independently verified as derivable from
   the machine answer's own bytes at that evaluation, by a checker that
   imports no rendering code. No such checker exists today for the one member
   already served [Observed, route test enumerated above]. A route that
   complied before does not comply on the day the amendment takes effect.
2. **A precondition on service is added.** A member served under a byte
   ceiling of its own may not be served before the registry declares that
   ceiling. That is an obligation on a future route, and it is the
   specification's first sentence making service conditional on a registry
   field.
3. **A scope limit is added.** The requirement's comparison is stated not to
   range over either category. That is a narrowing of the parity oracle's
   population — a reader could previously have argued the presentation view's
   fields belonged in the compared multiset.

What *does* survive from the source's claim, and is stated here rather than
dropped: no Case, Observable, Oracle, Oracle-independence, Mutation-proof,
Falsifier or Scenario limb of PWB-REQ-020 changes; no existing falsifier is
weakened; nothing previously required becomes optional. The class is
Normative because obligations are *added*, not because anything is removed.

Procedurally the classification costs nothing and buys honesty: the
specification is digest-bound, so an owner act is required at either class,
and CC-REV-1's full-review floor already applies to a signed specification.
Recording *Clarifying* would have bought a reviewer's attention at the price
of a false statement of what the edit does.

## What explicitly does NOT change

Enumerated, because "I only touched PWB-REQ-020" is exactly the claim this
field exists to make contradictable.

1. **PWB-REQ-004's closed project-fact population.** Its sentence "The POC
   SHALL admit project facts only from this closed population: …" is
   untouched, and the inserted text says twice that a view "mints no project
   fact". No class, key, catalog or account key is added.
2. **Every existing sentence of PWB-REQ-020.** The SHALL sentence, all six
   bullets, the Scenario and the `warrants:` block are byte-identical. The
   patch is a pure insertion with no removed line; the builder's selftest
   mutates a context line and confirms the patch then refuses to apply.
3. **Every existing route's credential class and its ceiling.**
   `/api/poc/polaris` remains `machine-credentialed` under
   `maxMachineResponseBytes`; the human Polaris page remains `human-open`
   under `maxHumanResponseBytes`. This delta changes no registration, mints
   no `ResponseLimitIdentity` and renames nothing.
4. **The adapter-registry entry.** Not a manifest row here, not patched, and
   its field names are not written into the specification. The specification
   says "the adapter-registry entry's resource envelope declares that
   ceiling" and leaves the field's *identity* to the registry act, so
   adopting this delta before that act creates no dangling literal.
5. **PWB-REQ-011.** Progressive reachability and the exact-requirement route
   are untouched; a derived view is not a reading level.
6. **PWB-REQ-014.** The `presentation-artifact` and `non-citable` attributes,
   the anchor-set obligations and the prohibition on citing Polaris as an
   authority all stand unchanged. A category member is a machine response and
   is not an owner-visible narrative unit; nothing here licenses a view to be
   cited as authority.
7. **PWB-REQ-016 and non-visual recoverability.** Untouched. A derived view
   subtracts nothing, and the inserted text says so in terms.
8. **`design.md`.** Not patched. Its decision that human HTML and machine
   JSON have separate final encoded-byte ceilings stays true, because this
   delta mints no ceiling and names no numeric value. [Inferred] A reader may
   expect a design decision to be added; the honest position is that the
   design record describes ceilings that exist, and the one new ceiling this
   delta anticipates belongs to the sibling registry package.
9. **The contract-coverage matrix and `CONTRACT-COVERAGE.md`.** Not patched.
   The `RFC6-21.c2` row's `unknown-uncovered` disposition and its note remain
   accurate, and the matrix is generator-verified: the coverage builder
   reports the matrix matches regeneration at 324 clauses represented
   [Observed, run this session]. This is a reviewable claim, not a
   convenience — see the tension recorded next.
10. **No RFC clause is amended.** Unlike the sibling scoped-attributes
    candidate, this package carries no contract patch and needs no contract
    successor ceremony.
11. **No consent, retention or egress posture moves.** The draft view's
    "sends no source or draft byte outside the observing project" restates a
    bound the generation authorization already carries; it grants no read, no
    destination and no provider call.

## The RFC6-21 tension, disclosed rather than reconciled

`RFC6-21` (`.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`)
holds that minimal display never subtracts facts and that endpoints always
serve the full set. A task-scoped briefing view can be read as a second
endpoint that does not serve the full set.

**The reading this delta takes:** RFC6-21's subject is display depth — what a
surface shows by default — and its endpoint sentence guarantees that the full
set stays retrievable. Under this delta it does: the machine answer keeps
serving the complete fact set at the same evaluation, and the inserted text
says a derived view "subtracts nothing" for exactly this reason. A derived
view hides nothing at rest.

**The reading this delta does not take, stated so a reviewer can take it:**
if `RFC6-21` is read as a property of *every* endpoint rather than of the
fact set's availability, then a task-scoped briefing needs an `RFC-0006`
contract amendment and a second owner act, in the shape the sibling
scoped-attributes candidate took for `RFC7-33`. That would make this package
two acts rather than one. This delta does not decide it; a reviewer who
reaches the second reading should record it as a finding rather than a
question, because it changes the act count. [Inferred]

## Warrant

The owner's dated ruling record
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
2026-09-21:

- **P-72, arm A, question 1** — one PWB semantic delta naming a closed
  "derived read-only machine view" category covering the machine Polaris
  route and the briefing; and the cross-cutting sentence that no route is
  served before its ceiling is declared.
- **P-76, arm A, question 3** — folded into P-72's delta as a second declared
  category.
- The record's cross-cutting reading names this delta's gate bead
  (`syzygy-dov.22`) the widest gate, with M5 slice 3, M7 slice 4, M10's
  schema document and M11's machine status route all waiting on it.

Cited by path and identifier; no digest of any performed act is reproduced
here.

## Evidence or decision basis

Every source below is reachable by anyone who can reach the specification.

- The ruling record above — the only authority in this list.
- `docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md` (Gate 5) for the
  recommended delta shape and the retroactive/prospective membership order;
  `docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md` (Q3) for the second
  category, its name and its disjointness measurement;
  `docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md` (slice 3) and
  `docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md` (slice 2) for the two
  consumers this wording must not foreclose. All four are candidate
  analyses; none is authority, and where this delta departs from one — the
  change class — it says so.
- Implementation observations, all re-run this session and named in the table
  above: `apps/three-surface-poc/src/routes.ts`,
  `apps/three-surface-poc/src/polaris-presentation-route.test.ts`,
  `packages/three-surface-poc-core/src/project-shape-observation.ts`.
- `IMPACT-LEDGER.md` beside this file carries the sweep, its two methods and
  its denominator.

## Terms introduced / retired

**Introduced: two**, both defined at their only point of use, inside
PWB-REQ-020, and both closed by enumeration.

- **derived read-only machine view** — the owner's words, from P-72's ruled
  arm. Admission test: a reader given the definition can decide membership
  without inference, because the members are listed.
- **generated editorial draft view** — proposed. These are the words the M7
  analysis recommends; the ruling folds the category in without naming it, so
  the *name* is an owner value this draft proposes rather than carries. The
  alternative considered and rejected was widening category 1, which fails on
  the disjointness measurement above.

**Retired: none.** Nothing is renamed, and no existing term changes meaning.
"Machine answer" is used in the inserted text in the sense the requirement
already uses it and is not newly defined.

## Downstream impact

**Method, stated so the figure can be re-derived rather than re-read** (rules
2 and 9). Two sweeps over every tracked file at the baseline commit
`a4a34510a5582edbd38c1df57a064ba3ac0a33f2`, run 2026-09-21; nothing sampled.

1. Python `re` over the UTF-8 text of every path in the tracked-file listing:
   `PWB-REQ-020\b` per file, plus a second pattern for continuation forms
   (`PWB-REQ-014/020`, `PWB-REQ-007, 014, 020`, and the `..` range form).
2. `grep -l -F` for the literal identifier over the same tracked listing.

Method 1's full-form pattern and method 2 both return **112 files**. The
continuation pattern adds **9 more** that the full form misses, each verified
by printing its matched text, so the citer population is **121 files** over a
denominator of **1,334** tracked files. The nine are:

- `.syzygy/governance/decisions/DECISION-HISTORY.md`
- `.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`
- `apps/three-surface-poc/src/polaris.ts`
- `apps/three-surface-poc/src/pwb-mutation-sweep-main.ts`
- `apps/three-surface-poc/src/routes.ts`
- `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-09-named-absent-file-dropped.json`
- `docs/reviews/2026-09-05-pwb-live-exact-head-packet.md`
- `docs/reviews/R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-READING-ASSETS-REPAIR-2026-09-10-RAW.md`

**What the 121 need.** Because the edit removes and rewords nothing, no
citing sentence becomes false: every existing statement about PWB-REQ-020's
parity invariant stays exactly as true as it was. [Observed — the patch has
no removed line; the builder verifies the population of changed subjects
against the declared one.] What the citers gain is a sentence they did not
have, so the impact is *work to be done*, not *text to be repaired*. The
implementation sites for the bead that follows adoption are enumerated in
`IMPACT-LEDGER.md`.

**Derived artifacts.** One: `GOVERNING-DEPENDENCIES.md`, regenerated from the
proposed specification bytes inside the package rather than hand-edited. The
contract-coverage matrix and `CONTRACT-COVERAGE.md` are also generated and
are byte-stable under this delta [Observed, coverage builder run this
session]. No index, register or status page is updated in anticipation of
adoption (template rule 5).

**Digests.** `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` hashes the *proposed*
bytes of all eleven subjects. Any repair to any of them retires the manifest
digest and every copy of it, including the one `OWNER-DECISION-PACKET.md`
quotes.

## Migration / supersession plan

In order. Steps 1–3 are drafting and review; only step 5 is an owner act.

1. **Review**, CC-REV-1 full class in CC-REV-4 fresh context, against a frozen
   commit; raw output retained verbatim under `docs/reviews/` with a
   `-RAW.md` filename. Findings dispositioned here, finding by finding.
2. **Repairs**, then a manifest regeneration with the builder's `--write`
   mode, then every quoted copy of the digest updated in the same commit.
   A regeneration retires any review bound to the old bytes (rule 10).
3. **Registration** of the act phrase and its packet digest copies in
   `scripts/check_governance.py` before the act exists, so CG-7d can see a
   stale copy. The three edits are listed in `OWNER-DECISION-PACKET.md`.
4. **The registry act** (P-72 question 2, gate bead `syzygy-dov.18`), which
   mints the briefing ceiling in the adapter-registry entry. It is a separate
   owner act over a separate subject and may be performed before or after
   this one. Until it is performed the briefing view may not be served — that
   is the point of the precondition sentence, not a defect in the ordering.
5. **The owner's PWB behavior amendment act** over the manifest digest,
   recorded in `ACCEPTANCE-ACT-RECORD.md` with its own dedicated record.
6. **At adoption, in the same logical change (CC-REV-2):** the builder's
   adoption mode writes the two patched subjects into the tree; the act
   record lands; the generated dependency declaration is already correct
   because it is part of the applied bytes; `check_governance.py` and the
   CI workflow gain this package's `--check` and `--selftest`.
7. **Implementation** is a separate bead under a separate authorization.
   Adoption of this delta authorizes no route, no test and no registry edit.

**Ordering against the sibling candidate.** The scoped-attributes candidate
(`.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/`)
is pending against the same eleven subjects. The two specification patches
compose in either order, and the builder's `--check` verifies both
compositions on every run and confirms the composed specification's warrants
still validate. The generated dependency declaration does not compose: both
packages rewrite its one `Source:` digest line, so **whichever package the
owner signs second must be regenerated with `--write` against the tree after
the first lands**, and its packet digest updated before the second act. This
is mechanical, not a conflict of meaning: neither package's prose touches the
other's sentences.

## Review

**Required class:** CC-REV-1 full review, run per CC-REV-4 in fresh context
with only the artifact, its governing references and the acceptance criteria
in `REVIEW-BRIEF.md`. CC-TEST-6's mutation bar applies to the builder, whose
`--selftest` holds the fixtures.

**Reviewer:** not yet assigned. The reviewer must not have authored this
change or shared its session; this draft's author has run no review of it and
has written none.

**Verdict:** none. No review has been run against these bytes, and no verdict
word may be written here by anyone who did not produce it.
