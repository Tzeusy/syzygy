# RFC 0008 — Trajectory (Work Surface)

**Status:** Proposed foundational contract. This line is a self-declaration at authoring time (RFC3-16): effective status is established solely by the owner-act record binding this file's exact content digest, and acceptance edits nothing here. Absent such a record, this contract binds nothing.
**Date:** 2026-07-30 (amended through 2026-08-02)
**Serves:** vision.md Thesis (three states; work is never proof), VIS-1, VIS-2, VIS-5, VIS-6, VIS-7; architecture.md (typed authority; `work/`); SEC-5. Implements owner rulings SDR-5, SDR-6, SDR-7, SDR-8, SDR-9, SDR-10, SDR-11, SDR-12, SDR-18, and the SDR §2 Trajectory charter. Resolves the work-ontology portion of SDR §5 question 10.

---

## 0. Reader's summary (non-normative)

*Plain-language orientation. If this section and a clause ever disagree, the
clause wins.*

- Trajectory is the **work surface**: the complete, evidence-linked account
  of what remains, what's approved, active, blocked, merged — and the
  distinction no tracker carries: **what merged without yet being checked
  against the intent that warranted it**.
- Its three forbidden shapes: the **mirror** (a second editable copy of
  scheduler state), the **closure fallacy** (rendering a closed ticket as
  "done"), and the **amnesiac board** (columns with no account of change,
  cost, or authority).
- Work renders through a **closed vocabulary of thirteen states** in three
  partitions: eight live (`future` → `reconciled`), one terminal
  (`closed-unmerged` — deliberately never named "done"), and four honest
  absence values (`state-undetermined`, `activity-undetermined`…). Every
  state has a declared derivation; nothing is guessed or force-fitted.
- Beside that state travels a **second orthogonal field**: the
  reconciliation chain state. "Reconciled at E with evidence", "merged —
  not yet evaluated", "evaluated and unsatisfied", and "evaluated,
  contradiction raised" are four different answers that
  must never share a rendering (RFC8-28). At V0 the honest answer for merged work is
  "reconciliation evidence absent" — a wall of those on a fleet-built
  project is correct output.
- A worker is `active` only on a real progress signal within a declared
  staleness bound; no bound declared means `active` is unrenderable.
- **Cost is independent measures, never a composite "effort" score**; absent
  values are Unknown, never zero; every aggregate discloses coverage.
- Every diff is accounted for: work with no traceable warrant renders
  **Unknown-provenance** (counted, never green); a scheduler work item with
  no materialization record is an **orphaned-work contradiction** routed to
  the owner — never absorbed, never filtered away.
- Small changes riding a parent work item inherit its warrant only within
  the warrant's declared scope and a declared per-project size threshold —
  undeclared threshold means nothing inherits.

Structure: §3 is the contract (RFC8-1 … RFC8-32); §4 violation cases; §8
owner questions, answered ones marked in place.

---

## 1. Summary

Trajectory (`work/`) is the owner's complete, evidence-linked account of the
project's work: what remains, what is approved but unmaterialized, planned,
ready, active, blocked, under review, merged, what it cost, why each piece of
work was authorized — and the distinction no tracker carries: **what merged
without yet being reconciled against the intent that warranted it** [Observed:
SDR §2 charter]. This RFC is the surface's **semantic contract, not its UI
design**: it projects RFC 0001's entities (it forks no catalog), and defines
the normalized work-state vocabulary above provider-specific status with each
state's honest derivation, the blocked-cause taxonomy, independent cost
measures with no composite effort score, the change-accounting chain's
rendering obligations including broken joins, compaction/retention rendering,
inherited-mutation accounting, and the post-merge reconciliation rendering V0
stages as honest absence (SDR-12). The anti-thesis is binding: a Kanban board,
a Beads mirror, or an issue list that renders `closed` as "done" does not
satisfy this contract [Observed: SDR §2; RFC2-20].

---

## 2. Motivation and doctrine grounding

Doctrine keeps desired, observed-implementation, and execution state
semantically distinct, and rules that scheduled or completed work is never
proof intent is satisfied [Observed: vision.md, Thesis]. The lived failure
this surface ends is the amnesiac orchestration day — "oversized diffs and
scattered completions with no coherent account" [Observed: vision.md]. The
substrate audit found the account's lower half largely non-existent today: no
run identity, no durable gate artifacts, no reconciliation object anywhere,
warrants as prose, a scheduler that forgets by default [Observed:
`06-TRAJECTORY-BRIEF` §§6–8 — non-authoritative audit, adopted where cited].
The owner staged the answers: post-hoc telemetry at V1 (SDR-5),
Unknown-never-zero (SDR-6), pre-materialization authority (SDR-7),
reconciliation absence rendered at V0, computed at V1 (SDR-12).

[Inferred] The failure modes this contract guards against are three, named in
the research corpus: the **mirror** (a second editable copy of scheduler
state), the **closure fallacy** (execution closure rendered as done), and the
**amnesiac board** (current columns, no account of change, cost, or
authority). Each is individually attractive to an implementer and each
manufactures exactly the comprehensible fiction VIS-1 forbids.

---

## 3. The contract

Clauses are numbered `RFC8-n` for stable citation. Amend in place; retire
rather than renumber. Parentheticals beginning
*History:* are amendment records — when and why text changed — and carry
no normative force; the clause text around them is the contract.

### 3.1 Identity and plane discipline

**RFC8-1.** Trajectory renders all three state planes relevant to work —
desired (approved intent), execution (proposals-in-flight, work items, runs),
and observed (merge facts, verification evidence, reconciliation verdicts) —
**in one surface without letting any plane impersonate another** (RFC1-22/23).
Every rendered item carries its plane; an item whose plane cannot be
determined is counted and rendered Unknown, never omitted or guessed.

**RFC8-2.** **The anti-thesis is binding.** Trajectory must not be: (a) a
second editable store of any scheduler-owned field (RFC4-5, inward limb);
(b) a view in which scheduler closure renders as done, green, or complete
(RFC2-20); (c) a board showing current state that cannot answer "what did
the fleet change, at what cost, under whose authority" for a past window at
the fidelity the preserved records support.

**RFC8-3.** Trajectory is a **rebuildable projection** (VIS-6) over the
kernel, the `.syzygy/work/**` plane (RFC3-19), and the typed adapters —
never independently authoritative. Every mutation it offers is a
synchronous, attributed adapter or governance-plane act followed by a
re-read (RFC4-5) — never write-locally-and-sync-later.

### 3.2 Ontology: a projection of RFC 0001, not a fork

**RFC8-4.** Trajectory introduces **no new kernel entity**. Its ontology is a
projection of RFC1-5, with these bindings:

| Surface concept | Kernel identity (RFC 0001) |
|---|---|
| Candidate work / drafted plan | Proposal, kind *execution intent*, state drafted/under review (RFC1-27/31) |
| Approved plan / plan item | Approved execution-intent Proposal; decomposition via child Proposals (RFC1-30) |
| Materialization record | Materialization record (RFC1-29) |
| Work item (substrate alias "bead"), incl. epics | Work item, scheduler-issued, mirrored never minted (RFC1-5; RFC4-15) |
| Execution run / attempt | Execution run + its Execution Record (Evidence artifact, SDR-8; RFC4-18/19) |
| Review | Work item (review lane) + hosting PR facts as Evidence (RFC4-11) |
| Verification | Verification run — observed plane, never execution (RFC1-23; RFC4-13) |
| Reconciliation | Reconciliation evaluation and its verdict claim (RFC2-18) |
| Warrant | The `motivates` edge / a Decision — deliberately not reified (RFC1-8) |

**RFC8-5.** **Deliberate non-reifications**, recorded: an **idea** is
personal presentation state (VIS-6, exception (a)) until promoted into a
Proposal — never truth-bearing, never enumerated as work. A **milestone** is
an annotation-profile entity (RFC1-7), a lens for aggregation and compaction
boundaries, never itself work or a warrant. There is **no Feature entity**
(RFC1-32): "feature request" is intake vocabulary that must resolve to a
Capability identity before any status attaches. A **contradiction** and a
**dismissal** render here (as a blocker on a conclusion; as *dismissed by
decision*) but are never work items, never auto-scheduled (RFC1-21/20).

**RFC8-6.** A **compaction record** is a durable, identified record under
`.syzygy/work/**` (schema: RFC 0003) naming what it summarized, what it
discarded, and what remains externally queryable. It is a fact about
retention, never a status claim, and may never alter one (§3.13).

### 3.3 Pre-materialization authority and "What remains?"

**RFC8-7.** Trajectory renders the approved-Proposal lifecycle **drafted →
under review → approved → queued-for-materialization → materialized** over
the RFC1-28 entity, in RFC1-31's own state names.
`queued-for-materialization` is realized as a **recorded queue act in
`.syzygy/work/**` on an approved Proposal** — Syzygy's own ordered intent to
materialize — not a new kernel lifecycle state and **never named "scheduled"**:
the scheduling question is typed-authority-routed to the work scheduler
[Observed: architecture.md, typed authority]. The lifecycle terminates at
`materialized` (RFC1-29).

**Post-materialization withdrawal and supersession are scheduler lifecycle
state, and Syzygy never holds a mutable record of that state.** They are
**read from the scheduler at the answering evaluation** (RFC4-15) and
**rendered against the materialization record's join** (RFC8-10/8-11),
stamped with the evaluation that read them, discarded and re-derived at the
next evaluation — never merged (RFC4-5, inward limb). No annotation, field,
log, or appended entry recording post-materialization scheduler state may be
written onto the materialization record, and no `.syzygy/work/**` transition
may record it. Two clauses forbid the alternative and one makes it
unfixable: the record is
immutable and "divergence between record and later scheduler state is a fact
about the scheduler, never grounds to rewrite history" (RFC1-29); a durable
Syzygy copy of a scheduler-owned mutable field is the second editable store
RFC8-2(a) names as anti-thesis (RFC4-5, inward limb); and RFC8-11 forbids
correcting the record to match the scheduler, so a written annotation could
never be repaired once it diverged. Post-materialization regret is expressed
as a **new Proposal citing the old one** (RFC1-31), not as a mutation of
either store.

**Capturing that a withdrawal or supersession *occurred* is a different act,
and it is permitted — indeed required where a durable Syzygy record depends
on the fact (RFC4-16(2)).** An immutable, evaluation-stamped observation
record or Execution Record noting the transition as a historical fact about
the scheduler is captured evidence, not a mutable projection of a
scheduler-owned field (RFC4-5, inward limb, which draws exactly this line):
it is never rewritten, never presented as the item's current lifecycle
state, and never joined into or appended onto the materialization record.
Nor is it a `.syzygy/work/**` **transition**: RFC3-19 houses Execution
Records in that namespace, and the prohibition above is on Syzygy recording
a *lifecycle transition* of its own for a scheduler-owned state change, not
on the namespace. What the paragraph above forbids is the **second editable
store of *current* scheduler state** — not beating the substrate's retention
horizon. The two
duties are complementary: a transition lost to `bd gc` before capture
renders **Unknown citing the retention event** (RFC4-16(3)), and nothing
here licenses that loss. [Inferred — the scoping RFC4-5's inward limb
already implies, stated so the two clauses do not read as opposed.]

**RFC8-8.** **"What remains?" enumerates three planes, each labeled:**
(a) approved normative claims (requirements, governance clauses) covered by
no approved execution-intent Proposal — at V0 this is absence surfacing, not
gap computation [Observed: v1.md, V0/V1 gap boundary]; (b) approved execution
intent not yet materialized — from `.syzygy/work/**`, queue order visible;
(c) open materialized work items — from the scheduler read (RFC4-15) at the
answering evaluation, **each checked against the materialization record**
(RFC8-10). Drafted (unapproved) proposals render as *unadopted draft*
(RFC2-25 sibling state) — enumerable, never counted among approved intent,
never anchoring any remaining-work total.

**Orphaned work is a Contradiction, not a badge.** A scheduler work item
matching **no materialization record** is an **orphaned-work Contradiction**
(RFC1-29, final paragraph) — two stores answering one question, no pinned
intent revision for RFC2-18 to bind to, no warrant traceable through
`materializes`. Trajectory is the only surface that enumerates scheduler work
items, so the obligation lands here: the enumeration **must** perform the
check, mint the Contradiction per RFC1-5/RFC1-18(b), route it to **owner
adjudication as its only lawful exit** (RFC1-21; RFC2-15), render the
affected conclusion Unknown (reason #8 `contradicted-pending-adjudication`,
`suspended` tier, RFC2-15), and render the finding itself — **never silently
adopted into a record, never silently deleted, never read as evidence that
materialization happened** (RFC1-29). It is **exempt from filtering**
(§8 q4): unlike RFC8-23's Unknown-provenance it is not a visibility default
the owner may tune. Re-materialization after a partial failure must **cite
and supersede the orphan finding** in the new materialization record
(RFC1-29). An orphaned work item is **not** an Unknown-provenance item and
never renders as one: see RFC8-23 for the distinction.

**Exclusivity binds every enumeration and every total.** Every Proposal
declares an exclusivity group (RFC1-27). Trajectory's queue, its
"what remains" enumeration, and **every remaining-work total, count, or
aggregate** must never union — or sum across — two proposals in one
exclusivity group, or proposals whose compatibility is undeclared. The
honest render is ***N candidate futures*, selectable one at a time**
(RFC1-27; VIS-1), carrying the explicit scenario context RFC6-24 requires;
a context naming two members of one group resolves `incompatible-scenario`
(RFC6-5), never a merged scene and never a summed count. Two approved
exclusive proposals are **one** unit of remaining work with two candidate
shapes, never two. This is not discharged by the drafted-proposal rule above:
that rule excludes *drafts* from totals, says nothing about two **approved**
exclusive proposals, and does not stop a queue from listing exclusive
alternatives as parallel work.

**RFC8-9.** Per SDR-18, **Trajectory owns the drafting queue and the work
lifecycle** — **an ownership asserted against Polaris, not against the work
scheduler**. Queue state, assignment, and progress live in this surface and
**Polaris renders that state read-only** (RFC7-24); Polaris owns the
contextual intent-authoring and adoption experience. Nothing here qualifies
architecture.md's typed-authority row: after materialization the **scheduler**
is authoritative for work lifecycle state (RFC8-10; RFC1-29), Trajectory
renders it and never stores it (RFC8-2/8-3). An intent-shaped queue item (a
spec or governance delta) renders in Trajectory's queue and adopts through
Polaris; the underlying Proposal and its state are one and the same in both
surfaces (RFC6-3).

### 3.4 Materialization rendering

**RFC8-10.** Materialization renders as a **one-way door** (SDR-7; RFC1-29):
the immutable materialization record — **proposal identity, work-item
identity set, and the pinned warranted intent revision** (RFC1-29; RFC1-5),
all three **required**, none conditional — is the join Trajectory walks in
both directions. The pinned revision is load-bearing, not optional: RFC2-18's
verdict binds to it, RFC8-21's chain runs through it, and RFC8-28's four-way
distinction has nothing to evaluate `reconciled@E` *against* without it.
Trajectory additionally renders the **materializing evaluation** alongside
the record — a Trajectory-side extension, not a kernel record component
(§5, flagged extension). After materialization the scheduler is authoritative
for lifecycle state; `.syzygy/work/**` plan state is never rendered as
current for a materialized item.

**A missing record is a finding, not a silent skip.** Walking the join
inward, a scheduler work item that matches no materialization record is the
**orphaned-work Contradiction** of RFC1-29's final paragraph, handled per
RFC8-8 — rendered and routed to owner adjudication, never absorbed into the
account as ordinary work and never treated as evidence that materialization
occurred. Until the record exists, materialization has not occurred, whatever
the scheduler already holds (RFC1-29).

**RFC8-11.** **Divergence renders; Trajectory never adjudicates it.**
Substrate-side edits of Syzygy-written pointers (the warrant reference,
RFC4-17) render as substrate annotations ("edited in substrate at T; not a
warrant claim"): the `.syzygy/work/**` record stays authoritative, the
pointer is re-asserted at the next evaluation, and no contradiction is
manufactured on the chain's load-bearing join (RFC4-5, outward limb).
Divergence between the record and later scheduler state is a fact about the
scheduler, never grounds to rewrite the record (RFC1-29).

### 3.5 The normalized state vocabulary

**RFC8-12.** Trajectory renders work through a **closed normalized state
vocabulary**, partitioned so the distinction between being in flight, being
finished with, and not being determinable stays legible:

- **eight live states** — `future`, `planned`, `ready`, `active`, `blocked`,
  `review`, `merged`, `reconciled`;
- **one terminal state** — `closed-unmerged`: the scheduler closed the item
  and no merge fact exists (RFC8-15). It is named here, in the contract,
  precisely so that no implementer has to name it: it is **never** `done`,
  `complete`, `finished`, or `resolved`, because "done" is exactly the word
  the closure fallacy needs (§6; RFC8-30);
- **four absence values** — `state-undetermined`,
  `eligibility-undetermined`, `activity-undetermined`, `stale-or-dead`.

**Thirteen values, closed**, each with its derivation and its honest-absence
behavior in RFC8-13. **The field renders no value outside this list**, and no
implementation may mint, spell, or force-fit one — the force-fit RFC8-14
forbids for raw substrate statuses is equally forbidden here. The closure has
to be genuine, not nominal: RFC6-14 requires every machine answer to carry
its state **verbatim**, and RFC6-22/23 make disagreement between two
renderings over one declared scope release-blocking under the trust floor, so
a value the contract never names can be neither carried verbatim nor checked
for parity. RFC 0009's work/construction overlay (RFC9-32) consumes this
vocabulary, so any ambiguity here propagates to the map. `unadopted
draft` and `dismissed by decision` are sibling *surface* states (RFC2-25's
deliberately-outside-the-registry note; RFC8-8), never members of this
vocabulary. Every value is a **per-evaluation derived projection**, never a
stored or editable field.

**The normalized state is one of two orthogonal fields, not the whole
answer.** "The field renders no value outside this list" closes *this*
field — the normalized work state — and closes nothing else. The **RFC2-18
chain state** (`merged`, `reconciliation-pending`, `reconciled@E`,
`unsatisfied`, `contradiction-raised`, `Unknown(reason)`) is a **separate
field with its own closed vocabulary** (RFC8-28), carried beside the
normalized state on every rendering, filter, count, and machine answer, and
never folded into it. The two vocabularies overlap in spelling and are not
the same field: normalized `merged` and `reconciled` say where execution
reached; the chain state says what the post-merge evaluation found. An item
whose normalized state is `merged` may carry chain state
`reconciliation-pending`, `unsatisfied`, or `contradiction-raised` — three
different answers, and rendering all three as normalized `merged` alone is
exactly the merge RFC2-17's word reservation forbids. Every consumer of this
vocabulary, RFC9-32's work/construction overlay included, consumes **both
fields** (§5). [Inferred — stated because the single-field reading let three
chain states share one rendering downstream.]

**The normalized state is not a Claim** (RFC1-24; RFC2-5). It is a derived
rendering of scheduler and repository facts — a projection of board state,
not a status claim about a capability — so it carries no RFC2-5 two-level
claim identity, no RFC2-25 tier, and no membership in the observation record
(RFC2-6). Its four absence values are therefore **state-local**: they are
never stamped with, never counted among, and never absorbed by an aggregate
of RFC2-24 Unknown reasons, exactly as RFC6-6 rules for navigation outcomes.
A board's "`state-undetermined` ×12" must never contaminate the project's
Unknown-reason counts. For RFC6-14's label parity, every machine answer
carries the normalized state value **verbatim**, the raw substrate status it
derives from (RFC8-14), and the evaluation identity (RFC6-15); the epistemic
label, rendering tier, and Unknown reason on any answer are those of the
*claims* rendered beside the state, never of the state itself. [The Claim
reading is defensible and drags RFC2-5 identity, RFC2-25 tiers and RFC2-6
record membership behind it; §8 q5 routes the choice to the owner.]

The substrate-to-normalized mapping is a **declared, versioned derivation
artifact** in the governance plane and a snapshot input (**RFC2-1 item 7** —
the observer/adapter/parser/policy version list; not item 8, which is
deterministic parsing configuration). It is an **authorization-bearing
governance artifact and is honored only under RFC3-16(a)** (RFC3-16(a),
policy-declaration class): `.syzygy/governance/**` is writable by untrusted
fleet workers (SEC-3's actor class, extended to committed artifacts by the
premise RFC3-16(a) states), and a mapping row projecting a custom substrate status
into `ready` or `active` would make the board and the endpoints report
dispatch-eligible and live work on the strength of a file no owner act
authorized. Substrate statuses are read from the tool, verbatim, per RFC4-15.

**RFC8-13.** The derivations. Every value RFC8-12 enumerates has a row here,
and every row states its honest-absence behavior. **Live states:**

| State | Meaning | Derivation | Honest absence |
|---|---|---|---|
| `future` | Approved execution intent, pre-materialization | `.syzygy/work/**`: Proposal approved or queued-for-materialization; no materialization record | Sub-state (approved vs queued, queue order) always visible; drafted proposals are *unadopted draft*, not `future`. **Exclusivity binds here:** two proposals in one exclusivity group never render as parallel `future` work and never sum into one remaining-work total — the honest render is *N candidate futures*, selectable one at a time (RFC1-27; RFC6-24), and a scenario context naming both resolves `incompatible-scenario` (RFC6-5) |
| `planned` | Materialized, open, not dispatch-eligible | Scheduler read: open with unmet dependency edges, or deliberately frozen (`deferred`/equivalent, with its reason) | Frozen-vs-dependency distinction rendered; an unreadable dependency set renders `eligibility-undetermined`, not `planned` |
| `ready` | Open, unblocked, dispatch-eligible | A derived query at the answering evaluation **over snapshot inputs only** — the work-state export captured in the snapshot (RFC2-1 item 3) plus RFC4-15's dependency feed — recomputed per evaluation, never cached as truth. **No implementation may invoke the substrate's live readiness computation at answer time**: a source not identified in the snapshot must not influence that evaluation's answers (RFC2-2), and calling a substrate whose state has moved defeats RFC2-3's identity test on re-run — the same rule RFC2-18 states for chain states | A ready-set without its evaluation identity is not a ready-set; where the work-state export or the dependency feed is uncaptured, the item renders `eligibility-undetermined`, never `ready` |
| `active` | Claimed, with current progress | Claimed (in-progress + assignee) **and** a progress signal — branch tip moved, new commit, PR state changed — within the declared staleness bound (RFC4-23) | See RFC8-16: no declared bound ⇒ `activity-undetermined`; signal older than the bound ⇒ `stale-or-dead`; never `active` in either case |
| `blocked` | Open, waiting on something nameable | Substrate blocked/waiting status, dependency edges, gates | Carries a blocked-cause class or cause-Unknown (RFC8-17) |
| `review` | An open review lane bound to an exact head SHA | Open PR facts (hosting sub-adapter) + review work item/labels + `external_ref` | Lane-open is derivable; **reviewer activity is never claimed** (a review lock label is a lock, not liveness); a merge-readiness verdict binds to its head SHA and expires when the head moves |
| `merged` | The change reached the integration branch | **A VCS merge fact only** (RFC4-11) — never inferred from scheduler closure | Execution state: never done, never green; enters the RFC2-18 chain as `reconciliation-pending` at the evaluation that first captures the merge fact |
| `reconciled` | `reconciled@E` per RFC2-18 | A reconciliation verdict claim, gate-backed Observed (RFC2-25), rendered with its evaluation identity | V0: never renders (§3.14); merged-but-unreconciled renders "reconciliation evidence absent / Unknown" |

**Terminal state:**

| State | Meaning | Derivation | Honest absence |
|---|---|---|---|
| `closed-unmerged` | The scheduler closed the item and no merge fact exists — abandoned, superseded, deduplicated, or unexplained | Scheduler read: item closed (RFC4-15) **and** no VCS merge fact joins to it (RFC4-11/RFC4-22). Closure alone never derives `merged`, and this state never derives `reconciled` | The substrate's closure reason renders **verbatim**; where the substrate recorded none, the reason renders Unknown citing the substrate's silence — never guessed. Never `done`, `complete`, or green (RFC8-15/8-30); the closure event stays queryable execution history, and a `closed-unmerged` item is never counted among satisfied, reconciled, or completed work |

**Absence values** (state-local per RFC8-12 — never RFC2-24 Unknown reasons):

| Value | Meaning | Derivation | Honest absence |
|---|---|---|---|
| `state-undetermined` | The declared mapping has no row for this item's raw substrate status | The verbatim substrate status (RFC4-15) falls outside the declared substrate-to-normalized mapping (RFC8-12/8-14) | Raw status always rendered and queryable beside it; the item is never dropped and never force-fitted into a neighbouring state. Resolution: amend the declared mapping, honored only under RFC3-16(a) |
| `eligibility-undetermined` | Materialized and open; dispatch-eligibility could not be computed | The dependency set or the work-state export needed to decide `planned` vs `ready` was not readable at the answering evaluation — adapter degraded (RFC4-15), uncaptured (RFC2-2), or lost past the retention horizon (RFC4-16) | The open fact is never suppressed and the item never renders `ready` or `planned` on a guess; the render cites *what* could not be read, and where the cause is a retention event it cites that event (RFC8-24) |
| `activity-undetermined` | Claimed, but no staleness bound is declared, so no signal can count as current | A claim fact exists and RFC4-23's staleness bound is undeclared — RFC2-9's mechanics applied to liveness | `active` is **unrenderable** until the bound is declared (RFC8-16). The claim fact and its instant still render; resolution is a governance act — declare the bound — not fresh evidence |
| `stale-or-dead` | Claimed; the last progress signal is older than the declared staleness bound | A claim fact plus a last-signal instant older than the declared bound (RFC4-23) | The last-signal instant is always shown; never `active`, never green. The coordinator heartbeat, lock labels, and worktree existence are never admissible as signal (RFC8-16) |

**RFC8-14.** **Raw provider status stays visible and queryable** behind
every normalized state, substrate-qualified (RFC4-6): the normalized state
is a lens, never a replacement. A substrate status the declared mapping does
not cover (`pinned`, `hooked`, a custom status) renders its raw status with
normalized state **`state-undetermined`** (RFC8-12/8-13; resolution: amend
the declared mapping, honored only under RFC3-16(a)) — never dropped, never
force-fitted. `state-undetermined` is a **state-local absence value**: it is
not the RFC2-24 Unknown reason `missing-declaration`, is never stamped with
one, and is never counted among a project's Unknown-reason totals (RFC8-12;
RFC6-6). [§8 q7 routes the alternative — an RFC2-24 reason for this case — to
the owner, per RFC 0002 §8 q1(a).]

**RFC8-15.** **Closure is not a normalized "done."** Scheduler closure
without a merge fact (abandoned, superseded, deduplicated, unexplained)
renders as the terminal state **`closed-unmerged`** (RFC8-12/8-13) with the
substrate's reason verbatim — never `merged`, never `reconciled`, never
green (RFC2-20), and never under any label meaning done, complete, finished,
or resolved. Closure *with* a merge fact renders `merged` and enters the
reconciliation chain; the closure event stays queryable execution history.

### 3.6 Activity and liveness

**RFC8-16.** `active` requires a **progress signal within a declared
staleness bound** (bound value: quality-policy material; the obligation to
declare is binding — RFC4-23(2), including that clause's requirement that the
bound be honored only under RFC3-16(a) — a worker-minted bound is what turns
`active` from unrenderable into renderable, so an unverifiable one leaves
this clause's floor exactly where an undeclared one does). Until the bound is
declared, `active` is unrenderable: claimed items render
**`activity-undetermined`** on RFC2-9's
mechanics applied to liveness (the condition RFC2-24 reason
`no-currency-bound-declared` names for claims; the *state* value is
state-local per RFC8-12, never that reason, never counted among a project's
Unknown-reason totals — RFC6-6). Between signals, worker liveness renders
**Unknown**; past the bound, **`stale-or-dead` with the last-signal instant
shown** — never `active`, never green. Never admissible as liveness: the
coordinator heartbeat (coordinator-claim only), lock labels, worktree
existence (RFC4-23) [Observed: `06` §3.2a — workers never heartbeat in the
initial substrate].

### 3.7 Blocked causes

**RFC8-17.** `blocked` carries a cause from the **closed taxonomy**
{`dependency`, `pr-wait`, `external`, `decision`}, each a **declared
derivation**: `dependency` from unmet work-item dependency edges; `pr-wait`
from an open PR awaiting review or corrections (`external_ref` + PR/review
state); `external` from a declared external event (CI in flight, timer or
substrate gate); `decision` from a pending human gate, owner decision, or
adjudication (an unresolved contradiction renders here, the conclusion
Unknown per RFC2-15). Where the substrate conflates causes and no declared
derivation resolves one, the item renders **blocked with cause Unknown** —
the blocked fact is never suppressed and a cause is never guessed.

### 3.8 Cost without an effort score

**RFC8-18.** Cost renders as **independent measures, never a composite**.
The V1 measure set (each with declared source and evidence class; the list
is amendable here, the independence rule is not): estimated effort and
declared complexity tier (**`declared-only`**, RFC2-25 — the declaration is
Observed, its accuracy Unknown; **never `Inferred`**: doctrine reserves
Inferred for the output of a declared inference process carrying inference
provenance [Observed: trust-and-evidence.md], and RFC2-7 requires an overlay
recording model, version, parameters and exact inputs, none of which a human
judgment has. Filing owner estimates in the inference plane would make them
render Unknown on any project without model-provider consent — the common
proving-ground case, RFC2-7/SEC-2 — and would give them RFC2-8/RFC1-22
challenge authority only, in place of a governance-plane declaration's
standing); lead time; active compute
time; blocked time (split by RFC8-17 cause where history supports it); input
tokens; output tokens; billed or derived API cost (derived-from-rates is
Inferred, labeled — RFC4-21); attempts (countable only from Execution
Records, RFC4-20); review rounds; CI time; rework; touched
files/components/interfaces (from VCS; component granularity resolves
through the **declared implementation mapping** — a governance-plane
artifact, RFC1-16 class (i), whose primary declaration site is RFC4-26/SDR-4;
RFC 0009 consumes it for geography and does not own it). **No synthetic "effort"
number may be computed, rendered, or served** — collapsing independent
measures is the error doctrine rejects for maturity [Observed:
architecture.md, Genome-complete note].

**RFC8-19.** **Absent means Unknown, never zero** (SDR-6; RFC2-23). Every
aggregate over partially-known measures discloses coverage ("cost known for
n of m runs") and never renders as a complete total (RFC4-21). A
predominantly-Unknown cost pane on the initial substrate is the correct
output, not a defect (VIS-1, VIS-2) [Observed: `06` §6 — six of thirteen
measures are recorded nowhere today].

### 3.9 Telemetry staging (SDR-5)

**RFC8-20.** **V1** renders structured, **post-hoc** execution telemetry
exclusively from captured Execution Records (the RFC4-19 run envelope):
per-run model/runtime, timing, tokens/cost, attempts, gate outcomes at their
RFC2-25 tiers, parent/child run structure — absent fields Unknown.
**Deferred entirely**: terminal-grade streaming, live intervention, and
control [Observed: SDR-5; vision.md eventual mandate — live views never
contribute to status claims]. **V0** renders what the derivation-first
adapters provide (RFC4-28) and the rest Unknown; nothing at V0 may simulate
telemetry.

### 3.10 The change-accounting chain

**RFC8-21.** Trajectory must walk, in both directions, the chain: **warrant
(normative reference or Decision) → approved plan item (execution-intent
Proposal) → materialization record → work item → execution run(s) →
commits/PR → merge fact → reconciliation verdict** — joined on the RFC1-25
relations (`motivates`, `materializes`, `produced_by`, `supports`) and the
RFC4-22 adapter joins, each rendered with its declared basis
(`recorded-identity` vs `naming-convention`, the latter `reduced-fidelity`).
**Against today's actuator toolchain this chain is honest but thin**: several
of its links resolve only by naming convention, and the enrichments that
would carry them to event-time Observed — durable and parent run identity,
dispatch records, resolvable spec anchors on work items — are named on the
RFC4-29 roadmap and deliberately **not required**. Trajectory therefore ships
a chain that is mostly `reduced-fidelity` at first and gains fidelity as the
toolchain emits more; that thinness must render as thinness, and must never
be presented — in this RFC, in the surface, or in an acceptance test — as a
chain awaiting completion rather than one that is complete and weak.
[Inferred — composition of RFC4-22's join bases with RFC4-29's
never-required roadmap.]

**RFC8-22.** **A broken join renders; it is never silently skipped.** Where
a link cannot be established at the answering evaluation, the chain renders
the break at that link — Unknown with its RFC2-24 reason — and everything
downstream renders with provenance degraded accordingly. Reconstructing a
join by similarity, interpolation, or inference is forbidden (RFC4-22;
missing evidence never renders Inferred [Observed: trust-and-evidence.md]).

### 3.11 Unknown-provenance work and the reasons this surface renders

**RFC8-23.** A work item, run, or merged change with **no traceable warrant**
renders **Unknown-provenance**: a first-class, filterable, counted rendered
state — never green, never silently pooled into warranted work, and never an
ingest rejection (RFC4-10). A substrate-side warrant-field edit is an
annotation, not a competing warrant (RFC8-11); the human intent behind such
an edit surfaces as a Proposal against the plan item, where a warrant change
belongs.

**Unknown-provenance is not orphaned work, and this clause never absorbs
it.** They are different objects with different resolution owners. An
Unknown-provenance item may be perfectly legitimate untraceable work — a
pre-Syzygy backlog item, an import — and its route is *surface it*: counted,
never green, resolvable by supplying a warrant. An **orphaned work item** is
two stores answering one question (RFC8-8; RFC1-29), and its **only** lawful
exit is owner adjudication (RFC1-21; RFC2-15). Rendering an orphaned work
item as Unknown-provenance mis-routes it, skips minting the Contradiction,
and skips RFC2-15's Unknown rendering of the affected conclusion. Where an
item is both, the orphaned-work Contradiction governs and is never filtered
away behind the provenance badge.

**RFC8-24.** The RFC2-24 reasons Trajectory most renders **on its claims**,
each with its route visible: `missing-evidence` (no gate artifact behind a
claimed outcome — SDR-9); `source-uncaptured-or-unreachable` (adapter export
unavailable; facts lost past the retention horizon before capture, rendered
**citing the retention event**, never "no work existed" — RFC4-16);
`no-currency-bound-declared` (undeclared staleness bound, undeclared
retention bound, **or an undeclared maximum inter-pass interval** — RFC4-16(2):
the interval is the only thing that *bounds* pre-horizon history loss rather
than merely rendering it honestly, so until it is declared, every claim
depending on pre-horizon scheduler history renders Unknown on these
mechanics, and the fleet-day account renders that dependence visibly);
`stale-beyond-currency-bound`; `missing-declaration` (a governing
declaration — capability, topology, mapping, policy — absent behind a claim).
Unknown aggregation follows RFC2-24's rendering rule: aggregate, disclose
reason counts, expand.

**These are claim reasons only.** The normalized state's four absence values
(RFC8-12/8-13) are state-local, take no reason from this list, and are
counted separately — an aggregate of Unknowns never absorbs them (RFC6-6).

### 3.12 Inherited mutations (SDR-11)

**RFC8-25.** Small inherited mutations — warranted changes riding a parent
work item without one of their own — appear as **sub-entries of the parent
run's summary** (within the parent's Execution Record), each with rationale
and touched surfaces; never one work item each, never invisible. A
diff hunk resolving to no work item and no parent run summary renders
**Unknown-provenance** (RFC8-23) — the honest form of unexplained diff
coverage, never omitted from the account.

**"Small" is a declared per-project threshold, and its absence fails closed**
*(ruled at acceptance by owner decision B13, answering §8 q6).* The threshold
is **quality-policy material** (`governance/policies/`, RFC3-15): the
obligation to declare it binds now, the value is the owner's and may differ per
project, and the declared value is a snapshot input (RFC2-1 item 7) like every
other policy version. **Where no threshold is declared, no mutation inherits** —
every change requires its own warrant, and the account renders the absent
policy rather than assuming a permissive bound.

[Inferred] The fail-closed direction is the whole point of routing this to the
owner. Left undeclared and permissive, "small" is decided by **the worker
writing the summary** — the party with both the incentive and the sole
opportunity to call its own oversized change small, and the one whose prose
RFC4-19 already classes as worker-asserted. That is the same structure review 1
flagged wherever a policy's trigger is a classification: name the party who
makes it, and make a false one findable. Declaring the threshold moves the
classification from the worker's prose to a policy the owner set, and makes
exceeding it a mechanically checkable violation instead of a judgment call.
Absence renders as absence, never as a default — the rule this package applies
to every other undeclared policy value.

**Warrant coverage is a test, not a presumption.** The fleet-day account
attributes an inherited mutation's diff through the parent's warrant **only
where the mutation's touched surfaces fall within that warrant's declared
scope** — the requirement, scenario, governance clause, or Decision the
parent work item's `motivates` edge names (RFC1-25, whose warrant classes are
closed; trust-and-evidence.md: a work warrant requires *traceable
authority*). **Anything outside that scope does not inherit**: it renders
**Unknown-provenance per RFC8-23**, counted and never green, exactly as if no
parent summary existed. A warrant is never extended by execution-side prose;
a worker cannot widen the authority under which it acted by describing what
it also did. Without this test the charter's named lived failure — "oversized
diffs and scattered completions with no coherent account" (§2) — returns as
an *accounted* oversized diff attributed to a warrant that never covered it.

**The sub-entry's tier is fixed.** The rationale and touched-surface list
live in a worker-authored Execution Record whose prose fields RFC4-19 classes
as optional enrichment, so the sub-entry renders **`asserted-by-worker`**
(parent label Inferred, RFC2-25) — visible, challengeable, and **never a
status input** — unless the touched surfaces are independently evidenced from
VCS or gate artifacts, which render at their own tiers. RFC8-27's rule that a
summarized worker assertion stays `asserted-by-worker` applies after
compaction; this fixes the tier before it.

**The "small" threshold is not defined here.** Size, count, and scope bounds
on what may ride a parent warrant are an owner call routed to §8 q6, not a
choice for the implementation or for the worker writing the summary. Until
the bound is declared, the coverage test above is the operative limit.

### 3.13 Compaction and retention rendering (SDR-10)

**RFC8-26.** **The preservation set is binding**: structured run summaries,
work warrants, decisions, materialization mappings, known cost/token totals,
evidence identities and hashes, and reconciliation outcomes survive every
compaction. Raw transcripts and verbose logs may expire under declared
policy. A compaction is itself an identified, durable record (RFC8-6).

**RFC8-27.** **Expired-detail rendering.** *(History: amended at the rev7 rework,
blocker A3: the original read RFC4-13 route 2 as a confirmation performed
"at read time by an external system", which made a stored evaluation's tier
depend on a mutable external provider — RFC4-13(a) now fixes confirmation at
capture time.)* A claim whose only substantiation lived in expired material
renders Unknown **citing the compaction or retention event** — never absent,
never confidently restated from the summary. Preserved summaries render at
their recorded tier: a summarized worker assertion stays `asserted-by-worker`;
a preserved gate outcome **renders at the tier its evaluation recorded** —
an observation record is immutable (RFC2-6), and no later event at the
provider changes what an existing evaluation concluded. For route 2, what
the snapshot holds is the **external-confirmation capture artifact**
(RFC4-13(a)); the tier stands on that captured confirmation, so a CI
provider that expires its check records after ninety days expires nothing in
Syzygy — the historical evaluation and its `gate-backed` tier are untouched.
What provider expiry *does* mean: a **later re-confirmation is a new
observation** in a new snapshot, whose new evaluation may honestly find the
provider no longer confirms and record a degraded tier **there** (RFC2-4's
new-snapshot path) — degradation happens only through a new identified
evaluation, never by a stored record's meaning shifting under a display
query. Artifact resolvability alone is still not the test: RFC4-13 was
amended under AS-R3 to reject exactly that, and RFC 0004 §6 records
"`gate-backed` on retention and format alone" as Rejected — a preserved hash
with no capture artifact and no other satisfied route caps at `report-fact`,
with the cap visible. An artifact that is simply **gone** drops tier in the
next evaluation with the dangling reference rendered broken (RFC4-13). No
observer or surface ever *upgrades* a tier (RFC4-13); only new evidence in a
new snapshot can. "No records found" must be visually and queryably
distinguishable from "nothing happened" [Observed: `06` §9, adopted as
binding].

### 3.14 Post-merge reconciliation rendering

**RFC8-28.** The RFC2-18 chain states — `merged`, `reconciliation-pending`,
`reconciled@E`, `unsatisfied`, `contradiction-raised`, `Unknown(reason)` —
are **first-class Trajectory states**, queryable and filterable on the durable
identity: *reconciled at E with evidence* vs *merged, not yet evaluated* vs
*evaluated and unsatisfied* vs *evaluated, contradiction raised* are four
different answers and must never share a rendering. Unqualified
"reconciliation" means only the doctrinal sense; scheduler-state repair never
shares a field, count, or UI string with it — and the same reservation binds
`unsatisfied` (a gap) against `contradiction-raised` (a Contradiction, owner
adjudication only), which Trajectory must never merge into one count or one
badge (RFC2-17; RFC4-6).

**The chain state is a field of its own, orthogonal to RFC8-12's normalized
work state**, and the two travel together — never one in place of the other.
RFC8-12's closure binds the normalized field only; a rendering that shows
normalized `merged` without the item's chain state has answered the
execution question and silently dropped the reconciliation one, which
collapses *merged, not yet evaluated*, *evaluated and unsatisfied*, and
*evaluated, contradiction raised* into a single mark — the shared rendering
this clause forbids. Every rendering, filter, count, endpoint answer, and
cross-surface handoff that carries the normalized state carries the chain
state beside it, including RFC 0009's work/construction overlay (RFC9-32;
§5).

**RFC8-29.** **V0 renders the absence honestly** (SDR-12; RFC2-19): every
merged-but-unreconciled item renders "reconciliation evidence absent /
Unknown," and a wall of such Unknowns on a fleet-built project is correct
output, not a defect. Nothing in V0 simulates a verdict. **V1 computes** the
reconciliation evaluation and renders its gap as a navigable object.

**RFC8-30.** **The closure fallacy is forbidden.** No Trajectory aggregate,
badge, progress bar, or prose sentence renders a `closed` work item as done,
complete, or satisfied absent a `reconciled@E` verdict with gate-backed
evidence — a narrative sentence doing a badge's work is judged as a badge
[Observed: trust-and-evidence.md]. Progress aggregates over merged work
disclose their reconciliation composition (n reconciled, m pending, k
unsatisfied, c contradiction-raised, j Unknown).

### 3.15 Selection, drawer, endpoints

**RFC8-31.** Every Trajectory rendering obeys RFC 0006: selection by kernel
identity only (no work-item row handles across boundaries, RFC6-1), the
single drawer fact set (RFC6-18/19), label parity on every machine answer
(RFC6-14), evaluation stamping (RFC6-15), aggregation disclosure (RFC6-17),
the **closed navigation-outcome set including `incompatible-scenario`**
(RFC6-5), and **explicit, singular scenario context on every selection**
(RFC6-24) that **travels with every URL, cross-surface synchronization, and
query answer** (RFC6-25) — a queue row, a remaining-work count, and an
endpoint answer each carry the context they were computed under, and a
surface may never silently swap it. Trajectory adds **no surface-only facts**: anything it renders — normalized
states, blocked causes, chain joins, cost measures — is queryable with
identical labels, and its answers ("what remains," "what changed," "what
still lacks reconciliation") are endpoint-answerable at a named evaluation.

### 3.16 Authority boundary at the OpenSpec seam (binding phase rule)

**RFC8-32 — This contract schedules nothing.** *(History: added at the rev8 rework,
directive item 7.)* This RFC fixes the semantics of the work surface; it is
**not a specification of record from which implementation work may be
scheduled**. No implementation work for **user-observable Trajectory
behavior** may be scheduled solely from this RFC: before implementation,
every observable consequence of RFC8-1…RFC8-31 must either **map to an
approved OpenSpec requirement or scenario** in the governance root's
`openspec/**` plane, or carry an **explicit, reviewed N/A judgment**
recording why that consequence needs no requirement. The surface-
specification phase must produce, as a deliverable, a **clause-to-
requirement coverage matrix** for this RFC — every clause mapped to
requirement identities or to its reviewed N/A — and that matrix is review
material, never authority. This clause creates no OpenSpec content now
(none may exist during bootstrap); it binds the phase boundary so RFC prose
is never quietly treated as an implementable behavioral spec.

---

## 4. Violation cases

Each recognizable, not rhetorical:

1. *(RFC8-2/3)* A planning board stores an editable copy of scheduler status
   and syncs nightly; drag-to-column writes locally and reconciles later.
2. *(RFC8-7)* A `.syzygy/work/**` state named `scheduled`; a plan item edited
   after its materialization record exists; post-materialization supersession
   recorded as a `.syzygy/work/**` transition — **or appended to the
   materialization record as a `superseded_at` / `withdrawn_by` annotation**,
   which within months is a durable Syzygy-owned log of scheduler lifecycle
   transitions that RFC8-11 then forbids correcting.
3. *(RFC8-8)* "What remains" counts drafted proposals among approved intent,
   or omits items whose plane could not be determined.
4. *(RFC8-11/23)* A substrate `spec_id` edit adjudicated as a warrant
   contradiction — or, worse, adopted as the new warrant.
5. *(RFC8-13/16)* A dead worker renders `active` because the coordinator
   heartbeat is fresh and the worktree exists; `active` with no declared
   staleness bound.
6. *(RFC8-13/15)* `merged` derived from scheduler closure; a `pinned` item
   dropped because the mapping had no row for it.
7. *(RFC8-17/18/19)* A blocked cause guessed from a title; a single
   "effort: 7.2" score; a cost total silently treating Unknown runs as zero.
8. *(RFC8-21/22)* A chain rendered complete by fuzzy-matching a deleted
   branch name; a broken warrant join skipped so the chain "reads clean."
9. *(RFC8-25/27)* Cleanup hunks invisible in the fleet-day account; a gate
   rendered `gate-backed` after its artifact expired; "no work existed"
   where the honest output is Unknown citing the retention event.
10. *(RFC8-28/30)* "Reconciled: 12" counted from scheduler-repair events; a
    100% progress bar over merged-but-unreconciled work.
11. *(RFC8-8/10)* A work item with no materialization record rendered as
    ordinary open work, or as a filterable Unknown-provenance badge filtered
    off the board with only a count disclosed — no Contradiction minted, no
    adjudication route, the affected conclusion never rendered Unknown.
12. *(RFC8-8/9/13)* Two approved proposals in one exclusivity group listed as
    two queue rows and counted "what remains: 2" — the fictitious-consensus
    render arriving through a count; a queue row or endpoint answer served
    without its scenario context.
13. *(RFC8-12/13/15)* A closure-without-merge rendered as `done`, `complete`,
    or a value the contract never names; a stale-or-dead item force-fitted
    into `blocked` because the board had no column for it.
14. *(RFC8-25)* A one-line parent work item carrying forty sub-entries across
    three capabilities, attributed through a warrant that never covered them
    — an *accounted* oversized diff.

---

## 5. Integration

**Relies on RFC 0001:** the closed entity/relation vocabulary this surface
projects (RFC1-5/25); the plan-item resolution and one-way materialization,
including the orphaned-work Contradiction (RFC1-28/29/30); exclusivity groups
and *N candidate futures* (RFC1-27); the declared implementation mapping as a
governance artifact, class (i) (RFC1-16); plane assignment (RFC1-22/23);
no-Feature (RFC1-32); gap exits and adjudication-only Contradiction exits
(RFC1-20/21). **RFC 0002:** the label+tier+reason vocabulary rendered
verbatim (RFC2-24/25, including `declared-only`); the reconciliation chain
and reserved word (RFC2-17…20); the snapshot closure and identity test
(RFC2-1/2/3); lawful tier degradation (RFC2-4); degradation states (RFC2-23).
**RFC 0003:** `.syzygy/work/**` schemas for plan items, materialization
records, Execution Records, compaction records (RFC3-19); **the owner-act
provenance predicate governing the substrate-to-normalized derivation mapping
(RFC3-16(a))**. **RFC 0004:** the faithful scheduler feed whose normalized
mapping this RFC owns (RFC4-15); liveness honesty (RFC4-23); join bases
(RFC4-22); capture-before-horizon **and its declared maximum inter-pass
interval** (RFC4-16, incl. RFC4-16(2)); the `gate-backed` provenance
predicate (RFC4-13); the declaration sites for the capability mapping
(RFC4-26); the run envelope and its class-O prose fields (RFC4-19); the
two-limb anti-duplication invariant (RFC4-5).
**RFC 0005:** machine-client admission for RFC8-31's endpoint answers.
**RFC 0006:** selection, drawer, label parity, equivalence; the closed
navigation-outcome set incl. `incompatible-scenario` (RFC6-5); outcomes are
not Unknown reasons (RFC6-6); scenario context and its travel
(RFC6-24/25).

**Defects found in the foundations (reported, not silently diverged from):**

1. **RFC1-28/31 omit the queued-for-materialization stage** of the
   owner-ratified pre-materialization lifecycle (surface-shaping corpus,
   T-F8 disposition; SDR-7 context): proposed → approved →
   queued-for-materialization → materialized. This RFC realizes the queue
   stage as a recorded work-plane fact on the approved Proposal (RFC8-7),
   minting no kernel state; RFC 0001 should confirm that reading or add the
   state.
2. **RFC1-31 lists `superseded` as a Proposal terminal state without
   restricting it to pre-materialization** — *resolved in the drafts under
   review; retained for the trail.* RFC1-31 now states that "rejection,
   abandonment, and supersession are reachable **only before
   materialization** — `materialized` is terminal (RFC1-29), and superseding
   a materialized proposal would recreate the second editable store", with
   post-materialization regret expressed as a new proposal citing the old
   one. RFC8-7 adopts that reading verbatim. **No RFC 0001 change is
   outstanding on this item.**
3. **RFC1-29's materialization record lacks the pinned intent revision** —
   *resolved; retained for the trail.* Satisfied by the **RFC1-29 amendment
   of 2026-07-30**, which now pins "the exact intent revision — requirement,
   scenario, or governance clause version — cited by the proposal's warrant",
   and by RFC1-5's materialization-record row, which lists the pinned
   warranted intent revision as a component. RFC 0003 (RFC3-19 note) and
   RFC 0004 (§5 defect 1) record the identical closure. RFC8-10 accordingly
   states all three components as required, with **no conditional hedge**:
   the earlier "(pending the RFC 0001 amendment)" parenthetical was removed
   because, in normative text, it invited an implementer to omit the field
   the whole change-accounting chain joins through. **No RFC 0001 or RFC 0002
   change is outstanding on this item, and it is not a blocker on
   `ACCEPT FOUNDATIONAL RFCS`.**
4. **RFC2-18 wording vs RFC2-19** — *resolved; retained for the trail.*
   RFC2-18's bullet now reads that `reconciliation-pending` "attaches
   automatically and deterministically **at the first evaluation that
   captures the merge fact** (inside RFC2-19's deliberately triggered passes
   — never on a live merge event)", which is exactly the reading RFC8-13's
   `merged` row adopts. **No RFC 0002 change is outstanding on this item.**
5. **RFC2-24 has no exact reason for a substrate value outside a declared
   derivation mapping** — *the cross-reference is closed; the choice is now
   an open question of this RFC.* RFC 0006 §8 q3 has been answered by
   RFC2-24's added reason #11 (`reference-unresolvable`), so the paired
   cross-reference no longer stands. RFC 0002's own §8 q1(a) names this case
   as a vocabulary strain "deliberately left unamended" and routes it back to
   the owner as a live call. This RFC therefore no longer decides it in
   normative prose alone: RFC8-12/8-14 render the unmapped-status case as the
   **state-local absence value `state-undetermined`** (not an RFC2-24
   reason), and the alternative is posed to the owner at **§8 q7**.

**Extension flagged (not a defect).** RFC8-10 renders the **materializing
evaluation** alongside the materialization record. RFC1-29 and RFC1-5 name
three components (proposal identity, work-item identity set, pinned warranted
intent revision) and do not include it. It is a reasonable and useful field,
but it is a **Trajectory-side rendering extension, not a kernel record
component**, and this RFC does not add it to a kernel-owned immutable record
by assertion. RFC 0001 may adopt it as a fourth component if the owner wishes;
until then RFC8-10 renders it as an extension and nothing binds on it.

**Provides to:** **RFC 0007** — the SDR-18 boundary (RFC8-9): drafting queue
and work lifecycle here, intent authoring and adoption there. **RFC 0009** —
the work/construction overlay's declared work state, which is **two
orthogonal fields, not one** (RFC8-12; RFC8-28), both of which RFC9-32
consumes:

1. the **normalized work state** — RFC8-12/13's closed vocabulary, at
   present **thirteen values in three partitions**, not eight: eight live
   states, the terminal `closed-unmerged`, and four state-local absence
   values. Each partition renders as itself; the absence values are never
   folded into an Unknown-reason aggregate (RFC8-12).
2. the **RFC2-18 chain state** — `merged`, `reconciliation-pending`,
   `reconciled@E`, `unsatisfied`, `contradiction-raised`,
   `Unknown(reason)` — carried beside the normalized state on every element
   and every aggregate (RFC8-28), with **RFC2-17's word reservation binding
   the overlay**: `unsatisfied` and `contradiction-raised` never merge into
   one count, badge, or mark, and neither collapses into `merged`.

This handoff is stated as **two fields** rather than as a value count on
purpose. It has now been widened three times — first for the state-local
absence values, then for the thirteen-value count, now for the chain state —
and a count-shaped handoff fails silently whenever either vocabulary grows.
**A consumer conforms by consuming both fields and rendering every value
each field currently carries**, so an addition to either vocabulary crosses
the seam without amending this paragraph; a value the consumer cannot render
is a defect in the consumer, never a licence to fold it into a neighbouring
value.

Also to **RFC 0009**: the touched-components measure's dependence on the
declared implementation mapping (RFC8-18).
**Not this RFC's:** staleness/retention bound *values* (quality policy);
board/queue layout and interaction (craft); the V1 reconciliation-gap
computation (V1 RFC); streaming and control (deferred, SDR-5).

---

## 6. Alternatives considered

- **A Trajectory-local work-state field** (normalized state stored on a
  mirrored record). Rejected: the mirror anti-thesis — a second editable
  store that drifts (RFC4-5); per-evaluation derivation is the only form
  that cannot lie about its source.
- **Fewer normalized states** (collapse `future`/`planned`, or `review` into
  `blocked`). Rejected: each collapse erases a distinction the owner's
  questions need — approved-but-unmaterialized is the charter distinction
  (SDR-7), and review-wait vs dependency-wait have different resolution
  owners; the substrate's own `blocked` conflation is the defect, not the
  model [Observed: `06` §3.2].
- **More normalized states** (`claimed`, `changes-requested`,
  `verification-failed`). Rejected for the closed eight *live* states: they
  are renderable sub-facts (claim facts, review-cycle facts, gate outcomes),
  drawer-visible and queryable, without inflating the vocabulary every
  consumer must handle.
- **Leaving the closure-without-merge state unnamed** ("a terminal execution
  state"), on the reasoning that naming is presentation. Rejected: a value
  the contract never names cannot be carried verbatim on a machine answer
  (RFC6-14) and cannot be checked for parity, so two conforming
  implementations would spell it `closed`, `abandoned`, `terminal` — or
  `done` — and a third would force-fit it into `blocked` or drop it, with the
  disagreement release-blocking under RFC6-22/23. `closed-unmerged` is named
  in RFC8-12 for exactly that reason; the word "done" is the one outcome the
  closure fallacy needs, and leaving the naming to an implementer is how it
  gets chosen.
- **A composite effort/health score with disclosed weights.** Rejected even
  disclosed: weights are an opinion rendered as a measurement (RFC8-18).
- **Rendering `closed` as "done, pending reconciliation."** Rejected: "done"
  is exactly the word the closure fallacy needs (RFC8-28/30).
- **Auto-creating reconciliation work items for merged-but-unreconciled
  work.** Rejected: a derived absence is not a work warrant (RFC1-21); the
  loop is human-triggered (RFC2-19).

---

## 7. Deliberately deferred

Physical schemas for plan items, queue records, materialization records, and
compaction records → RFC 0003. Staleness/retention bound, **the maximum
inter-pass interval RFC4-16(2) requires the quality policy to declare**, and
measure *values* → quality/evidence policy (the *values* are deferred; the
obligation to declare each of them is binding here, and Trajectory is where
an undeclared interval renders — RFC8-24). The V1 reconciliation-gap
computation → V1 RFC
(SDR-12 staging). Streaming, intervention, control → deferred with telemetry
as entry criterion (SDR-5). Queue/board presentation, filters, saved views →
craft and personal presentation state (VIS-6, exception (a)) — **with one
obligation that does not defer**: a board or queue laid out as an ordered
sequence of columns *teaches* the reader that the states form a monotone
progress ladder, which RFC8-12's partition denies (the terminal state is not
the last rung, and the four absence values are not rungs at all), so any such
layout must place the terminal and absence values off the ladder rather than
at the end of it. The
confirmation-path enumeration behind RFC1-21 → shared with RFC 0002; this RFC
renders the outcome, not the mechanism. Cross-project work views → portfolio
profile (SDR-29/30).

---

## 8. Open questions for acceptance

1. **Vocabulary closure (RFC8-12/13).** *(Re-posed. The earlier form asked
   the owner to ratify "eight states" while **four clauses already rendered
   five values outside it** — RFC8-13's own `planned` and `ready` rows,
   RFC8-14, RFC8-15, and RFC8-16 (twice). An `ACCEPT` would have ratified a
   vocabulary the text contradicted in its own derivation table.)* The proposed closure is **thirteen values in three
   partitions**: eight live states (`future`, `planned`, `ready`, `active`,
   `blocked`, `review`, `merged`, `reconciled`), one terminal state
   (`closed-unmerged`), and four state-local absence values
   (`state-undetermined`, `eligibility-undetermined`, `activity-undetermined`,
   `stale-or-dead`), every one with a derivation row in RFC8-13. Two calls:
   (a) accept the partitioned closure, or collapse it (e.g. fold
   `activity-undetermined` into `stale-or-dead`, accepting that "no bound was
   ever declared" and "the bound was exceeded" then share a rendering and a
   resolution route)? (b) `closed-unmerged` is the drafted name for the
   terminal state, chosen so that no implementer has to name it and so that
   it can never be read as done; confirm the name, or choose another — **any name
   meaning done, complete, finished, or resolved is out of scope of this
   question** (RFC8-15; §6). Note `claimed`-without-signal remains a
   sub-fact, not a state.

   > **ANSWERED at acceptance — A8.** The **partitioned closure is accepted**: thirteen values in three partitions (eight live, one terminal `closed-unmerged`, four state-local absence values), each with a derivation row.
2. **Queue realization (RFC8-7; Integration defect 1).** Confirm
   queued-for-materialization as a work-plane fact on the approved Proposal,
   or direct RFC 0001 to add it as a kernel lifecycle state.
3. **Blocked-time cause split (RFC8-18).** The split needs transition
   history the substrate GC's away (RFC4-16); until capture cadence is
   settled it renders Unknown for most items. Worth its capture obligation
   at V1, or an enrichment-roadmap item (RFC4-29)?
4. **Unknown-provenance visibility default.** RFC8-23 makes it filterable
   but always counted. Should the fleet-day account view pin it (always
   visible, never filtered out), as the surface's main honesty signal about
   untraceable work? Proposed: yes for the account view; ordinary boards may
   filter with the count disclosed. **Scope limit:** this question governs
   Unknown-provenance only. The **orphaned-work Contradiction** (RFC8-8/8-10)
   is *not* filterable under any answer — it is a Contradiction whose only
   lawful exit is adjudication (RFC1-21; RFC2-15), and filtering it would
   mis-route it and skip the Unknown rendering of the affected conclusion.
5. **Epistemic class of the normalized state (RFC8-12).** *(Drafted position
   taken; routed for ratification.)* The RFC rules the normalized state a
   **derived rendering, not a Claim** — no RFC2-5 claim identity, no RFC2-25
   tier, no RFC2-6 record membership — and therefore gives it its own,
   separately-counted absence values rather than RFC2-24 Unknown reasons,
   following RFC6-6's rule for navigation outcomes. The alternative (a
   derived Claim) is defensible but drags RFC2-5 two-level identity, tier
   assignment, and observation-record membership behind it, and lets a
   board's state counts contaminate the project's Unknown-reason counts.
   Confirm the drafted position, or direct the Claim reading?

   > **ANSWERED at acceptance — B14.** **A derived rendering, not a Claim.** It carries its own separately-counted absence values (per A8's partition) rather than RFC2-24 Unknown reasons, which keeps board-state absences out of the project's Unknown-reason counts. The Claim reading is defensible but would drag two-level identity, rendering tiers and observation-record membership behind every board cell.
6. **The "small" threshold on inherited mutations (RFC8-25; SDR-11).**
   Currently undefined and unbounded; RFC8-25 now bounds the case by a
   *warrant-coverage test* (touched surfaces must fall inside the parent
   warrant's declared scope, else Unknown-provenance), but states no size,
   count, or scope-breadth limit — so "small" is otherwise decided by the
   worker writing the summary. Should the owner declare a bound (e.g. a
   maximum count of sub-entries, or a same-capability restriction), leave it
   to the coverage test alone, or route the value to quality policy?

   > **ANSWERED at acceptance — B13.** The threshold is **declared per project** as quality-policy material and **fails closed**: where none is declared, no mutation inherits. See RFC8-25.
7. **The unmapped-substrate-value rendering (RFC8-14; §5 item 5).** RFC 0002
   §8 q1(a) routes this back to the owner as a live call. RFC 0008 renders it
   as the state-local absence value **`state-undetermined`** (consistent with
   q5's non-Claim reading). The alternative is the RFC2-24 Unknown reason
   **`missing-declaration`**, which would make the normalized state a
   claim-bearing field and let board-state counts enter the project's
   Unknown-reason totals. Confirm `state-undetermined`, or direct the reason?

   > **ANSWERED at acceptance — A5 / B15, read with A8 / B14.** **No new RFC2-24 reason is minted for this case.** The board field itself renders the state-local absence value `state-undetermined` (accepted in A8's partition and reaffirmed by B14's non-Claim ruling); where a *claim* depends on the missing mapping, its RFC2-24 reason stays **#1 `missing-declaration`**, whose route already reads "declare the mapping". RFC8-12/8-13/8-14 stand as written.

---

*End of RFC 0008. Clauses RFC8-1 … RFC8-32. Lettered limbs cited inside
their parent clauses (e.g. RFC8-2(a)–(c)) are parts of those clauses —
list items within one clause body — not separate sub-clauses with their own
headings. The clause range is closed: amend in place, never renumber.*
