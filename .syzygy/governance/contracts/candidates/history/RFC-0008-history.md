# RFC-0008 — rationale and amendment history (Tier 2, non-normative)

Extracted at the rev10 compaction. Nothing here binds; the active contract is
`../rfcs/RFC-0008-trajectory-work-surface.md`. Full review corpus:
`_bootstrap/rfc-phase/reviews/`. Frozen rev9 source:
`_bootstrap/rfc-phase/rfcs/RFC-0008-trajectory-work-surface.md`.

Entries are keyed by clause ID. Text marked *(History: …)* is copied verbatim
from the rev9 source. Moved narrative is labeled by what it was.

---

## Front matter — rev9 status line and date

*Rev9 status line, superseded by the two-state model (OD-R10-5):*

> **Status:** Proposed foundational contract. This line is a self-declaration
> at authoring time (RFC3-16): effective status is established solely by the
> owner-act record binding this file's exact content digest, and acceptance
> edits nothing here. Absent such a record, this contract binds nothing.

*Rev9 date line:* **Date:** 2026-07-30 (amended through 2026-08-02).

---

## §0 / §1 — reader's summary and summary (merged at compaction)

Rev9 carried both a §0 "Reader's summary (non-normative)" and a §1 "Summary".
The compaction merged them into one §1 "Scope and reader's map"; no obligation
lived in either. Bullets dropped from the rev9 §0 that are stated normatively
elsewhere, retained here for the trail:

- "Its three forbidden shapes: the **mirror** (a second editable copy of
  scheduler state), the **closure fallacy** (rendering a closed ticket as
  'done'), and the **amnesiac board** (columns with no account of change,
  cost, or authority)." — now §2 and RFC8-2.
- "Work renders through a **closed vocabulary of thirteen states** in three
  partitions: eight live (`future` → `reconciled`), one terminal
  (`closed-unmerged` — deliberately never named 'done'), and four honest
  absence values (`state-undetermined`, `activity-undetermined`…). Every state
  has a declared derivation; nothing is guessed or force-fitted." — RFC8-12/13.
- "Beside that state travels a **second orthogonal field**: the reconciliation
  chain state. 'Reconciled at E with evidence', 'merged — not yet evaluated',
  'evaluated and unsatisfied', and 'evaluated, contradiction raised' are four
  different answers that must never share a rendering (RFC8-28). At V0 the
  honest answer for merged work is 'reconciliation evidence absent' — a wall
  of those on a fleet-built project is correct output." — RFC8-28/29.
- "A worker is `active` only on a real progress signal within a declared
  staleness bound; no bound declared means `active` is unrenderable." —
  RFC8-16.
- "**Cost is independent measures, never a composite 'effort' score**; absent
  values are Unknown, never zero; every aggregate discloses coverage." —
  RFC8-18/19.
- "Every diff is accounted for: work with no traceable warrant renders
  **Unknown-provenance** (counted, never green); a scheduler work item with no
  materialization record is an **orphaned-work contradiction** routed to the
  owner — never absorbed, never filtered away." — RFC8-23, RFC8-8.
- "Small changes riding a parent work item inherit its warrant only within the
  warrant's declared scope and a declared per-project size threshold —
  undeclared threshold means nothing inherits." — RFC8-25.

---

## §2 — motivation

Source citation for the substrate audit, given as a `_bootstrap/` path in rev9
and reduced to "[Observed: substrate audit]" in the active file (active
normative text does not cite `_bootstrap/` paths):

> [Observed: `06-TRAJECTORY-BRIEF` §§6–8 — non-authoritative audit, adopted
> where cited]

The same audit is cited at RFC8-16 (`06` §3.2a — workers never heartbeat in
the initial substrate), RFC8-19 (`06` §6 — six of thirteen measures are
recorded nowhere today), RFC8-27 (`06` §9, adopted as binding), and §6's
alternatives (`06` §3.2 — the substrate's own `blocked` conflation).

Rev9 §2 closing sentence, preserved: "Each is individually attractive to an
implementer and each manufactures exactly the comprehensible fiction VIS-1
forbids."

---

## §3 preamble

*Rev9 wording, dropped as self-describing after every `*(History: …)*`
parenthetical moved to this file:*

> Parentheticals beginning *History:* are amendment records — when and why
> text changed — and carry no normative force; the clause text around them is
> the contract.

---

## RFC8-7

**Moved argument (the three-reason justification for the annotation ban).**
The active clause keeps the ban and a compressed form of the reasoning; the
rev9 wording of the argument was:

> Two clauses forbid the alternative and one makes it unfixable: the record is
> immutable and "divergence between record and later scheduler state is a fact
> about the scheduler, never grounds to rewrite history" (RFC1-29); a durable
> Syzygy copy of a scheduler-owned mutable field is the second editable store
> RFC8-2(a) names as anti-thesis (RFC4-5, inward limb); and RFC8-11 forbids
> correcting the record to match the scheduler, so a written annotation could
> never be repaired once it diverged.

**Moved scoping note.** The rev9 `[Inferred]` tag on the capture-permitted
paragraph carried its own rationale, compressed to a bare `[Inferred]` in the
active file:

> [Inferred — the scoping RFC4-5's inward limb already implies, stated so the
> two clauses do not read as opposed.]

Also moved: "Nor is it a `.syzygy/work/**` **transition**: RFC3-19 houses
Execution Records in that namespace, and the prohibition above is on Syzygy
recording a *lifecycle transition* of its own for a scheduler-owned state
change, not on the namespace." and "The two duties are complementary: a
transition lost to `bd gc` before capture renders **Unknown citing the
retention event** (RFC4-16(3)), and nothing here licenses that loss." Both
rules survive in the active clause; only the substrate-specific `bd gc` naming
and the "two duties are complementary" framing were dropped.

---

## RFC8-8

**Moved explanatory sentences** (rules survive in the active clause):

> It is **exempt from filtering** (§8 q4): unlike RFC8-23's Unknown-provenance
> it is not a visibility default the owner may tune.

> This is not discharged by the drafted-proposal rule above: that rule
> excludes *drafts* from totals, says nothing about two **approved** exclusive
> proposals, and does not stop a queue from listing exclusive alternatives as
> parallel work.

---

## RFC8-10

**Moved sentence** (the rule survives): "Walking the join inward, a scheduler
work item that matches no materialization record is the **orphaned-work
Contradiction** of RFC1-29's final paragraph, handled per RFC8-8 — rendered
and routed to owner adjudication, never absorbed into the account as ordinary
work and never treated as evidence that materialization occurred."

---

## RFC8-12

**Moved explanatory passages** (every rule survives in the active clause):

> The closure has to be genuine, not nominal: RFC6-14 requires every machine
> answer to carry its state **verbatim**, and RFC6-22/23 make disagreement
> between two renderings over one declared scope release-blocking under the
> trust floor, so a value the contract never names can be neither carried
> verbatim nor checked for parity. RFC 0009's work/construction overlay
> (RFC9-32) consumes this vocabulary, so any ambiguity here propagates to the
> map.

> The two vocabularies overlap in spelling and are not the same field:
> normalized `merged` and `reconciled` say where execution reached; the chain
> state says what the post-merge evaluation found. An item whose normalized
> state is `merged` may carry chain state `reconciliation-pending`,
> `unsatisfied`, or `contradiction-raised` — three different answers, and
> rendering all three as normalized `merged` alone is exactly the merge
> RFC2-17's word reservation forbids.

> [Inferred — stated because the single-field reading let three chain states
> share one rendering downstream.]

> Its four absence values are therefore **state-local**: they are never
> stamped with, never counted among, and never absorbed by an aggregate of
> RFC2-24 Unknown reasons, exactly as RFC6-6 rules for navigation outcomes.

**Moved routing note**, superseded by the owner's answer to §8 q5 (decision
B14) and replaced in the active clause by an inline `(ruled … B14)` cite:

> [The Claim reading is defensible and drags RFC2-5 identity, RFC2-25 tiers
> and RFC2-6 record membership behind it; §8 q5 routes the choice to the
> owner.]

**Note on the widening argument.** The rev9 paragraph making the
substrate-to-normalized mapping an authorization-bearing artifact honored only
under RFC3-16(a) — including the SEC-3 untrusted-fleet-worker premise and the
"a mapping row projecting a custom substrate status into `ready` or `active`"
consequence — is **retained verbatim in the active clause**, not moved here.
RFC3-16(a)'s own example list cites RFC8-12 as authorization-bearing.

---

## RFC8-14

**Moved routing note**, superseded by owner decisions A5 / B15 answering §8 q7:

> [§8 q7 routes the alternative — an RFC2-24 reason for this case — to the
> owner, per RFC 0002 §8 q1(a).]

---

## RFC8-21

**Moved explanatory clause** (the obligation survives): "…and the enrichments
that would carry them to event-time Observed — durable and parent run
identity, dispatch records, resolvable spec anchors on work items — are named
on the RFC4-29 roadmap and deliberately **not required**. Trajectory therefore
ships a chain that is mostly `reduced-fidelity` at first and gains fidelity as
the toolchain emits more."

Rev9 `[Inferred]` rationale, compressed to a bare `[Inferred]` in the active
file: "[Inferred — composition of RFC4-22's join bases with RFC4-29's
never-required roadmap.]"

---

## RFC8-25

**Moved `[Inferred]` rationale for the fail-closed direction** (verbatim; the
fail-closed rule itself survives in the active clause):

> [Inferred] The fail-closed direction is the whole point of routing this to
> the owner. Left undeclared and permissive, "small" is decided by **the
> worker writing the summary** — the party with both the incentive and the
> sole opportunity to call its own oversized change small, and the one whose
> prose RFC4-19 already classes as worker-asserted. That is the same structure
> review 1 flagged wherever a policy's trigger is a classification: name the
> party who makes it, and make a false one findable. Declaring the threshold
> moves the classification from the worker's prose to a policy the owner set,
> and makes exceeding it a mechanically checkable violation instead of a
> judgment call. Absence renders as absence, never as a default — the rule
> this package applies to every other undeclared policy value.

**Moved consequence sentence** (violation case 14 carries the same case):

> Without this test the charter's named lived failure — "oversized diffs and
> scattered completions with no coherent account" (§2) — returns as an
> *accounted* oversized diff attributed to a warrant that never covered it.

**Retired paragraph — superseded by owner decision B13.** Rev9's RFC8-25
closed with a paragraph written before the acceptance ruling, which the
compaction dropped as superseded:

> **The "small" threshold is not defined here.** Size, count, and scope bounds
> on what may ride a parent warrant are an owner call routed to §8 q6, not a
> choice for the implementation or for the worker writing the summary. Until
> the bound is declared, the coverage test above is the operative limit.

Its first sentence survives in the active clause ("Size, count, and
scope-breadth bounds are the owner's call, never the implementation's and
never the worker's"). Its last sentence — "Until the bound is declared, the
coverage test above is the operative limit" — is **superseded**: B13 rules
that where no threshold is declared, **no mutation inherits at all**, which is
strictly stricter than falling back to the coverage test. The "routed to §8
q6" routing is also spent, q6 having been answered. See the compaction report
for this judgment call.

---

## RFC8-27

**Amendment record, verbatim:**

*(History: amended at the rev7 rework, blocker A3: the original read RFC4-13
route 2 as a confirmation performed "at read time by an external system",
which made a stored evaluation's tier depend on a mutable external provider —
RFC4-13(a) now fixes confirmation at capture time.)*

**Moved explanatory phrasing** (rules survive): "…so a CI provider that
expires its check records after ninety days expires nothing in Syzygy — the
historical evaluation and its `gate-backed` tier are untouched. What provider
expiry *does* mean: a **later re-confirmation is a new observation**…" and
"Artifact resolvability alone is still not the test: RFC4-13 was amended under
AS-R3 to reject exactly that, and RFC 0004 §6 records "`gate-backed` on
retention and format alone" as Rejected."

---

## RFC8-28

**Moved explanatory sentence** (the rule survives): "RFC8-12's closure binds
the normalized field only; a rendering that shows normalized `merged` without
the item's chain state has answered the execution question and silently
dropped the reconciliation one, which collapses *merged, not yet evaluated*,
*evaluated and unsatisfied*, and *evaluated, contradiction raised* into a
single mark — the shared rendering this clause forbids."

---

## RFC8-32

**Amendment record, verbatim:**

*(History: added at the rev8 rework, directive item 7.)*

The clause text itself is retained at full strength in the active file; only
this parenthetical moved. It is shape-parallel with RFC6-28, RFC7-38, and
RFC9-52.

---

## §5 — foundation defects closed before rev10

Rev9 §5 carried five reported defects. One (item 1, the missing
queued-for-materialization stage) is still outstanding and stays in the active
file. The four closed ones are recorded here in full; the active file names
them in one sentence each with the note that no RFC 0001 or RFC 0002 change is
outstanding on any of them.

**Item 2 — RFC1-31 lists `superseded` as a Proposal terminal state without
restricting it to pre-materialization** — *resolved in the drafts under
review; retained for the trail.* RFC1-31 now states that "rejection,
abandonment, and supersession are reachable **only before materialization** —
`materialized` is terminal (RFC1-29), and superseding a materialized proposal
would recreate the second editable store", with post-materialization regret
expressed as a new proposal citing the old one. RFC8-7 adopts that reading
verbatim. **No RFC 0001 change is outstanding on this item.**

**Item 3 — RFC1-29's materialization record lacks the pinned intent
revision** — *resolved; retained for the trail.* Satisfied by the **RFC1-29
amendment of 2026-07-30**, which now pins "the exact intent revision —
requirement, scenario, or governance clause version — cited by the proposal's
warrant", and by RFC1-5's materialization-record row, which lists the pinned
warranted intent revision as a component. RFC 0003 (RFC3-19 note) and RFC 0004
(§5 defect 1) record the identical closure. RFC8-10 accordingly states all
three components as required, with **no conditional hedge**: the earlier
"(pending the RFC 0001 amendment)" parenthetical was removed because, in
normative text, it invited an implementer to omit the field the whole
change-accounting chain joins through. **No RFC 0001 or RFC 0002 change is
outstanding on this item, and it is not a blocker on `ACCEPT FOUNDATIONAL
RFCS`.**

**Item 4 — RFC2-18 wording vs RFC2-19** — *resolved; retained for the trail.*
RFC2-18's bullet now reads that `reconciliation-pending` "attaches
automatically and deterministically **at the first evaluation that captures
the merge fact** (inside RFC2-19's deliberately triggered passes — never on a
live merge event)", which is exactly the reading RFC8-13's `merged` row
adopts. **No RFC 0002 change is outstanding on this item.**

**Item 5 — RFC2-24 has no exact reason for a substrate value outside a
declared derivation mapping** — *the cross-reference is closed; the choice is
now an open question of this RFC.* RFC 0006 §8 q3 has been answered by
RFC2-24's added reason #11 (`reference-unresolvable`), so the paired
cross-reference no longer stands. RFC 0002's own §8 q1(a) names this case as a
vocabulary strain "deliberately left unamended" and routes it back to the
owner as a live call. This RFC therefore no longer decides it in normative
prose alone: RFC8-12/8-14 render the unmapped-status case as the
**state-local absence value `state-undetermined`** (not an RFC2-24 reason),
and the alternative is posed to the owner at **§8 q7**. *(Since answered —
owner decisions A5 / B15, below.)*

**Provides-to narrative, moved.** The rev9 handoff paragraph explained its own
history:

> This handoff is stated as **two fields** rather than as a value count on
> purpose. It has now been widened three times — first for the state-local
> absence values, then for the thirteen-value count, now for the chain state —
> and a count-shaped handoff fails silently whenever either vocabulary grows.

The conformance rule it introduces is retained in the active file.

---

## §6 — alternatives considered (moved wholesale)

Two of these are load-bearing for reading live clauses and keep a
one-sentence pointer in the active §6: the closure-without-merge naming, and
the composite score. All seven are recorded verbatim.

- **A Trajectory-local work-state field** (normalized state stored on a
  mirrored record). Rejected: the mirror anti-thesis — a second editable store
  that drifts (RFC4-5); per-evaluation derivation is the only form that cannot
  lie about its source.
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
  state"), on the reasoning that naming is presentation. Rejected: a value the
  contract never names cannot be carried verbatim on a machine answer
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

## §8 — answered owner questions (moved with their answers)

Questions 2, 3, and 4 remain open and stay in the active file. The four
answered questions are recorded here with their rev9 text and the owner's
answer verbatim; each ruling is carried inline in the clause named.

### q1 — Vocabulary closure (RFC8-12/13) → **A8**

*(Re-posed. The earlier form asked the owner to ratify "eight states" while
**four clauses already rendered five values outside it** — RFC8-13's own
`planned` and `ready` rows, RFC8-14, RFC8-15, and RFC8-16 (twice). An `ACCEPT`
would have ratified a vocabulary the text contradicted in its own derivation
table.)* The proposed closure is **thirteen values in three partitions**:
eight live states (`future`, `planned`, `ready`, `active`, `blocked`,
`review`, `merged`, `reconciled`), one terminal state (`closed-unmerged`), and
four state-local absence values (`state-undetermined`,
`eligibility-undetermined`, `activity-undetermined`, `stale-or-dead`), every
one with a derivation row in RFC8-13. Two calls: (a) accept the partitioned
closure, or collapse it (e.g. fold `activity-undetermined` into
`stale-or-dead`, accepting that "no bound was ever declared" and "the bound
was exceeded" then share a rendering and a resolution route)? (b)
`closed-unmerged` is the drafted name for the terminal state, chosen so that
no implementer has to name it and so that it can never be read as done;
confirm the name, or choose another — **any name meaning done, complete,
finished, or resolved is out of scope of this question** (RFC8-15; §6). Note
`claimed`-without-signal remains a sub-fact, not a state.

> **ANSWERED at acceptance — A8.** The **partitioned closure is accepted**:
> thirteen values in three partitions (eight live, one terminal
> `closed-unmerged`, four state-local absence values), each with a derivation
> row.

*Carried in:* RFC8-12 (inline cite), RFC8-13 (the derivation rows).

### q5 — Epistemic class of the normalized state (RFC8-12) → **B14**

*(Drafted position taken; routed for ratification.)* The RFC rules the
normalized state a **derived rendering, not a Claim** — no RFC2-5 claim
identity, no RFC2-25 tier, no RFC2-6 record membership — and therefore gives
it its own, separately-counted absence values rather than RFC2-24 Unknown
reasons, following RFC6-6's rule for navigation outcomes. The alternative (a
derived Claim) is defensible but drags RFC2-5 two-level identity, tier
assignment, and observation-record membership behind it, and lets a board's
state counts contaminate the project's Unknown-reason counts. Confirm the
drafted position, or direct the Claim reading?

> **ANSWERED at acceptance — B14.** **A derived rendering, not a Claim.** It
> carries its own separately-counted absence values (per A8's partition)
> rather than RFC2-24 Unknown reasons, which keeps board-state absences out of
> the project's Unknown-reason counts. The Claim reading is defensible but
> would drag two-level identity, rendering tiers and observation-record
> membership behind every board cell.

*Carried in:* RFC8-12 (inline cite).

### q6 — The "small" threshold on inherited mutations (RFC8-25; SDR-11) → **B13**

Currently undefined and unbounded; RFC8-25 now bounds the case by a
*warrant-coverage test* (touched surfaces must fall inside the parent
warrant's declared scope, else Unknown-provenance), but states no size, count,
or scope-breadth limit — so "small" is otherwise decided by the worker writing
the summary. Should the owner declare a bound (e.g. a maximum count of
sub-entries, or a same-capability restriction), leave it to the coverage test
alone, or route the value to quality policy?

> **ANSWERED at acceptance — B13.** The threshold is **declared per project**
> as quality-policy material and **fails closed**: where none is declared, no
> mutation inherits. See RFC8-25.

*Carried in:* RFC8-25 (inline cite). See the RFC8-25 entry above for the rev9
paragraph this answer superseded.

### q7 — The unmapped-substrate-value rendering (RFC8-14; §5 item 5) → **A5 / B15**

RFC 0002 §8 q1(a) routes this back to the owner as a live call. RFC 0008
renders it as the state-local absence value **`state-undetermined`**
(consistent with q5's non-Claim reading). The alternative is the RFC2-24
Unknown reason **`missing-declaration`**, which would make the normalized
state a claim-bearing field and let board-state counts enter the project's
Unknown-reason totals. Confirm `state-undetermined`, or direct the reason?

> **ANSWERED at acceptance — A5 / B15, read with A8 / B14.** **No new RFC2-24
> reason is minted for this case.** The board field itself renders the
> state-local absence value `state-undetermined` (accepted in A8's partition
> and reaffirmed by B14's non-Claim ruling); where a *claim* depends on the
> missing mapping, its RFC2-24 reason stays **#1 `missing-declaration`**,
> whose route already reads "declare the mapping". RFC8-12/8-13/8-14 stand as
> written.

*Carried in:* RFC8-14 (inline cite), RFC8-12.

---

## Rev9 end-of-contract marker

> *End of RFC 0008. Clauses RFC8-1 … RFC8-32. Lettered limbs cited inside
> their parent clauses (e.g. RFC8-2(a)–(c)) are parts of those clauses — list
> items within one clause body — not separate sub-clauses with their own
> headings. The clause range is closed: amend in place, never renumber.*

The rev10 marker adds only the explicit "contiguous — no gaps, nothing merged,
nothing retired" statement the compaction charter requires.
