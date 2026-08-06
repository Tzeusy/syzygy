# Semantic delta SD-10 — RFC-0010 rev11b, the correction plane's own escapes

> **A proposal, not an act.** This delta describes a change made to *candidate*
> contract text inside act 1's digest subject. It accepts nothing. The clause
> text is the authority for what the contract says; where this file and a
> clause disagree, the clause wins and this file is wrong.
>
> Form: `../policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`. Workflow:
> `../policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`.

**Artifact(s):** `../rfcs/RFC-0010-mission-control-autonomy.md`
**Stable IDs affected:** RFC10-5, RFC10-17, RFC10-18, RFC10-19, RFC10-20,
RFC10-21, RFC10-22 (amended in place); RFC10-17(a), RFC10-18(a), RFC10-19(a)
(new)
**Change class:** **Normative** — every item below changes what a conforming
runtime must do. Nothing here is offered as editorial.
**Author:** the 2026-08-06 final-closure session
**Date:** 2026-08-06

---

## Why there are ten changes and not two

Two of them — RFC10-18's false citation and the unassigned effects-applied
predicate — are the open findings of review **RC-11**, which returned
`VERDICT: REVISE` over the exact bytes act 1 binds. The other eight are
findings **RC-10** and **RC-7** raised and the prior pass carried into
**P-27** rather than repaired.

They are repaired together because they are one defect seen from eight angles:
**the correction plane was written to fire on conditions that the party it
corrects gets to declare.** Who says effects were applied. Who says spend
happened. Who says the stop completed. Whether the mission's own park ever
ends. Each one, alone, reads as a drafting omission. Together they are a
pattern, and the pattern is what a reviewer named twice.

---

## Change 1 — RFC10-5: no block is indefinite

### Current meaning

> exit from `blocked` where the block arose under RFC10-8 or RFC10-11 is a
> **human resolution act** — an agent's "condition cleared" assertion never
> takes that transition.

and the lifecycle diagram's `running → blocked (→ running on unblock)`.

A mission in `blocked` has exactly one exit — back to `running` — and for two
of the three block classes that exit requires a human act. Nothing obliges
anyone to perform it. Nothing bounds the wait.

### Proposed meaning

The diagram gains `→ expired on park expiry`, and the clause gains:

> **No block is indefinite, whatever gave rise to it.** Every `blocked` state
> carries a **maximum park duration**, declared by the envelope; where none is
> declared the maximum is the expiry of the Attention Item the block minted
> (RFC10-12), so silence cannot buy an unbounded park. At the maximum the
> mission transitions **`blocked` → `expired`**, a terminal state whose reason
> is recorded. […] Expiry from `blocked` is a **termination, never a
> resolution**: it widens nothing (RFC10-12), does not substitute for the
> human resolution act where the paragraph above owes one, and does not mark
> the condition cleared.

### Why here, and not in RFC10-18

The charter that commissioned this pass says explicitly: *"Do not broaden
RFC10-5 merely to make a citation true unless that broader lifecycle rule is
independently justified across every block class."*

It is. The defect is that **`blocked` is non-terminal and RFC10-17 releases a
reservation only "on completion or termination"** — so a mission parked in
`blocked` holds its budget forever, and under RFC10-8's sibling-sum invariant
the parent envelope's headroom is consumed permanently. That is true of an
RFC10-8 block (a recorded self-widening attempt nobody resolves), of an
RFC10-11 block (an exhausted bound nobody raises), and of an RFC10-18 block
alike. It is a property of the lifecycle, not of any source.

So the rule is stated at lifecycle level, where lifecycle lives — and
RFC10-18 can then cite RFC10-5 **truthfully**, which is the opposite of what
rev11a did.

### What explicitly does NOT change

- **The human-resolution rule keeps its scope.** RFC10-8 and RFC10-11 blocks
  still require a human act to return to `running`. Expiry is a different
  transition to a different state and does not satisfy that requirement.
- **Expiry still cannot widen anything.** RFC10-12's safe-default rule is
  unchanged and is cited rather than restated.
- **The lifecycle is still provisional** pending the RFC 0008 work-state
  review. This adds an edge to a candidate vocabulary; it does not freeze it.

---

## Change 2 — RFC10-18: the false citation, removed and replaced

### Current meaning

> with no applied effects it enters `blocked` with an Attention Item, awaiting
> the human resolution act RFC10-5 requires

**This is false, and RC-11 established it against the clause text.** RFC10-5
scopes the human resolution act to blocks arising under RFC10-8 or RFC10-11.
An RFC10-18-sourced block arises under neither. A reader of RFC10-18 alone
concludes an exit obligation exists. None does.

### Proposed meaning

> **With no applied effects it enters `blocked`** with an Attention Item.
> **No human resolution act is owed for this block, and this clause says so
> rather than implying one.** RFC10-5's human-resolution rule is scoped to
> blocks arising under RFC10-8 or RFC10-11; an RFC10-18-sourced block arises
> under neither, and an earlier revision cited RFC10-5 for an obligation
> RFC10-5's own scope excludes. What bounds this park is RFC10-5's **maximum
> park duration** […] A human resolution act stays *available* and is the
> better exit; it is simply not owed.

### Warrant

Review **RC-11**, finding **RC11-A** `[Observed]`, verdict `REVISE`. The
finding is quoted in full in `../round-2026-08b/DISPOSITIONS-RC-11-RC-12.md`
and raw at `../round-2026-08b/reviews/RC-11-repair-confirming-RAW.md` §2.2.

### What explicitly does NOT change

- The `running → completed` rule. A mission still never reaches `completed`
  on its own authority.
- The routing of effect-bearing missions to `failed`. That limb is unchanged
  and is why RFC10-19's duties fire.
- **The clause still admits it was wrong**, in its own body, rather than
  silently correcting. A reader who saw the old text needs to know it was
  false, not merely that it is gone.

---

## Change 3 — RFC10-18(a): the branch selector gets an owner

### Current meaning

There is none. The predicate *"whether effects have been applied"* appears in
RFC10-18 and is defined, evidenced, tiered and Unknown-ruled **nowhere**.

RC-11 swept the file for every occurrence of `appl(y|ied|ies)` with Python
`re` — 14 hits, all read — and reported: never assigned to an independent
party, no evidence-tier requirement, no Unknown rule. Meanwhile the *other*
determination in the same paragraph is meticulous about all three.

### Proposed meaning

A new sub-clause **RFC10-18(a)** giving the predicate the same four things
completion has: an **evaluator** (owner act, or a declared owner-approved
evaluation transitively independent of the executor), an **evidence basis**
(guardrail decision record, execution records, declared effect classification,
retained for the mission's retention horizon), a **minimum tier**
(`gate-backed`), and a rule for **externally mediated effects** (representable
only as a declared unmediated effect surface; the predicate resolves Unknown
where one is named and no adapter-backed observation covers it).

And the fail-closed rule the charter required verbatim:

> **Unknown fails closed: where whether effects were applied is Unknown,
> effects are treated as applied** — for recovery, for reservation, and for
> human-attention purposes — until evidence establishes otherwise.

### Warrant

Review **RC-11**, finding **RC11-B** `[Inferred]`, which the reviewer rated
*the more serious of the two*. Its scenario:

> A mission with applied effects reaches its completion predicate. No
> independent establisher exists for its objective class. The executing
> principal […] asserts that no effects were applied. RFC10-18 routes it to
> `blocked`. RFC10-19's duties […] never fire […] The mission parks, and the
> applied effects stand, unreported.

The corpus-wide answer was already available and unused: RFC10-17, written in
the same pass, states the fail-closed Unknown rule for exactly this shape
("Unknown spend is never read as zero spend"), and VIS-2 and RFC2-23 say an
Unknown is not a zero. RFC10-18(a) applies the rule the corpus already holds.

### What explicitly does NOT change

- **The executor may still report.** Reporting is admissible evidence and
  always was. What it may not do is *establish*.
- RFC10-19's duty keys. They remain `failed` / `cancelled` / `expired`.
- The cost asymmetry is stated in the clause rather than hidden: fail-closed
  costs a compensation attempted needlessly; fail-open costs an applied effect
  nobody is told about.

---

## Change 4 — RFC10-17: who measures `spent`, and who sizes a reservation

**Current:** `spent` is "measured consumption" — by nobody named, under no
independence requirement.

**Proposed:** admitted from a Syzygy-launched profiled run's execution record
(RFC5-21, RFC4-18..RFC4-21) or an adapter-backed provider record (RFC 0004),
never from a self-report by the principal whose spend it is; the **declared
maximum cost** sizing a reservation is declared by the envelope or the
dispatching authority, never by the worker being dispatched.

**Warrant:** RC-10 finding **RC10-C** `[Inferred]`, which rated RFC10-17 *the
weakest of the six* correction-plane clauses. Its distinction is preserved in
the clause: the existing Unknown rule closes **absent** telemetry; this limb
closes **false** telemetry.

**Not changed:** chronic under-declaration is still not *prevented*, and the
clause says so — it renders as a recorded pattern of overrun attributable to
the declaring authority. RC10-C named that residual and it survives.

---

## Change 5 — RFC10-17(a): every reservation has a release point

**Current:** `released` is "reserved-but-unspent, returned on completion or
termination". Seven reachable states are not covered by that phrase.

**Proposed:** a table giving the disposition for `completed`, `failed`,
`cancelled`, `expired`, `blocked` with no applied effects, `blocked` after its
Attention Item expires, and an unrecoverable stop — plus:

> **No non-terminal park holds a reservation indefinitely.** […] An indefinite
> park is reachable only as an explicit, owner-visible envelope declaration
> with its own act — never by silence.

Two rows carry the load. **Compensation cost is reserved before it runs**, so
recovery is never funded past an exhausted bound. And on an unrecoverable
stop, the reservations of runs that did *not* terminate are **retained and
named individually** — a reservation cannot be returned while the work it
funds may still spend.

**Warrant:** RC11-A's consequence limb ("Parking is now a way to hold
budget"), and RC10-E/RC10-F's stop findings, which left an unterminated run's
budget undefined.

---

## Change 6 — RFC10-19: a failed compensation is not discharged

**Current:** "every compensatable effect's compensating action is attempted
and its outcome recorded as evidence." A *failed* compensation is therefore
recorded and nothing more; the irreversible-effects Attention Item is scoped
only to effects *declared* irreversible up front.

**Proposed:** a failed compensation **reclassifies the effect as irreversible
for this mission**, joins that Attention Item, and is stated as
*uncompensated* in the terminal reason. Partial success is recorded per
effect, and a partially compensated mission is never rendered as compensated.

**Warrant:** RC-10 finding **RC10-D** `[Observed]`. Its scenario: an effect
declared `compensatable`; the compensating action fails; the mission
terminates; **the owner is never told that a supposedly-undoable effect
stands.**

---

## Change 7 — RFC10-19(a): sibling disposition is declared, not inferred

**Current:** nothing. RC-7's F4 was recorded as closed for four of five parts,
with this the unclosed fifth: RFC-0019 "does not state the relationship
between a failed run's output and its completed siblings' output".

**Proposed:** the envelope declares a **sibling disposition on partial
failure** from a closed set whose minimum members are `independent`,
`halt-siblings`, `compensate-all`. **Unstated is not `independent`**: under
RFC10-7's obligation limb it takes the strictest reading — `compensate-all`
where every applied class is reversible or compensatable, otherwise an
escalation before further dispatch.

The clause names the two assumptions it refuses, because the charter asked for
exactly that: one failure does not automatically invalidate a sibling, **and**
a completed sibling is not automatically still valid.

**Warrant:** RC-7 F4's open part, restated in
`../round-2026-08b/MISSION-SAFETY-CLOSURE-REPORT.md` F4, and the charter §6.5.

---

## Change 8 — RFC10-20(b) and (d): stop reaches children, and can fail

**(b) Current:** "every run Syzygy launched **under the mission**" — which
excludes runs launched under a *child* mission. RFC10-8 makes child missions
first-class reservations against the parent, and no clause propagated a parent
stop to them.

**(b) Proposed:** the stop propagates **transitively to every child mission
and their descendants**; each is stopped as if the act had named it, its runs
terminated under the same limb, its reservation dispositioned under
RFC10-17(a); and **the enumeration of descendant missions reached is part of
the record**.

**(d) Current:** "an undeclared latency means stop is synchronous — the act
does not return until (a) and (b) hold." If (b) cannot be achieved, there is
no timeout, no failure disposition, and no Attention Item. **The default is
the deadlocking one.**

**(d) Proposed:** synchronous is not unbounded. Where the RFC5-21 kill switch
reports failure, or a declared maximum elapses, the act **returns having
failed to stop**: the mission enters `failed` (never `paused` or `blocked`,
which discharge none of RFC10-19's duties), an Attention Item enumerates each
run not terminated and each effect surface it may still reach, and each such
run's reservation is retained and named. An isolation class whose kill switch
has no failure signal has not satisfied RFC5-21.

**Warrant:** RC-10 findings **RC10-E** and **RC10-F**, both `[Observed]`; and
RC-11's **RC11-E**, which found RC10-F had been *reframed into a closure* by
the prior pass and reinstated it as open. The reviewer's own sentence is
carried into the clause: a synchronous act with no failure path is an
unbounded latency with a different name.

---

## Change 9 — RFC10-21: the predicate keys on content, not on scope

**Current:** applies to a composite "assembled under a mission **spanning more
than one project**".

**Proposed:** applies to a composite "assembled **under any mission**", subject
to the consent of every project whose content it embeds "**regardless of how
many projects the mission's declared target names**" — with the reason stated:
keying on declared scope lets the composing party decide whether the rule
applies, by deciding how to declare its own target. A composite whose embedded
content cannot be attributed to a project of origin also fails closed.

**Warrant:** RC-10 finding **RC10-G** `[Inferred]`: *"the rule keys on mission
scope, the harm keys on content provenance."* Its scenario — declare the
mission targeting A only; the envelope grants paths including a checkout of B;
the composite embeds B's content — is now inside the clause and is violation
case 20.

---

## Change 10 — RFC10-22: the bound cannot suppress notice of itself

**Current:** "an undeclared maximum means one outstanding item"; "on reaching
either bound the mission pauses rather than enqueueing further items."

**Proposed:** exactly one exempt class — **the item reporting that a bound was
reached, or the resulting state change** — minted and delivered at the
maximum. Deduplicated like any other, and the only exemption, because a second
returns the queue to unbounded.

**Warrant:** RC-10 finding **RC10-H** `[Observed]`. *"The safe behaviour
(pause) is correct; the notification of that behaviour is blocked by the same
sentence."*

---

## Terms introduced / retired

**Introduced, and each is a candidate term requiring registry admission
(CC-KNOW-5/6) before it appears on any public path:**

| Term | Where defined | Public? |
|---|---|---|
| *maximum park duration* | RFC10-5 | No — internal envelope field |
| *unmediated effect surface* | RFC10-18(a) | No — internal envelope field |
| *sibling disposition on partial failure* | RFC10-19(a) | No — internal envelope field |

All three are **envelope field names**, not vocabulary a reader of the public
narrative meets. They are recorded here so that the term registry's admission
rule is applied to them deliberately rather than by omission, and they are
routed to `TERM-REGISTRY-SEMANTIC-DELTA.md` as advanced-tier candidates.

**Retired:** none. No clause was renumbered; no identifier was reused.

---

## Downstream impact

Method: `build_dependency_index.py` for the edge set, `check_governance.py`
for every mechanical dependent, and a `grep -F` sweep for `RFC10-` across all
tracked files. Not "reading" — the reading is what missed nine values last
round.

| Artifact | Impact | Status |
|---|---|---|
| `ACTIVE-CONTRACT-MANIFEST.txt` | RFC-0010's per-module sha256 moves | Regenerated by script |
| **Act 1's argument** | the manifest's own sha256 moves | **Re-quoted, fourth time.** CG-7a…d green |
| `05-CONTRACT-INDEX.yaml` | clause list gains three lettered limbs | Regenerated |
| `CONTRACT-DEPENDENCY-INDEX.md` | RFC-0010 gains derived `cites` edges to RFC-0004 and RFC-0009 (the new text cites RFC4-18..21 and RFC2-25) | Regenerated; the edges appeared automatically, which is the point of deriving `cites` |
| `SURFACE-CLAUSE-ROUTING-MATRIX.md` | three new clause identities need a route | All three routed `OS`; CG-17 examines 202 clauses, 0 findings |
| `history/RFC-0010-history.md` | **created** — the amendment log moved out | Written |
| Context fixture 5 (cross-project mission) | its mandatory set includes RFC-0010; digest and word count move | Regenerated by `build_budget_report.py`, verified independently by CG-18 |
| `MISSION-SAFETY-CLOSURE-REPORT.md` | F4 and F6 rows describe seams this delta closes | Superseded by `MISSION-SAFETY-CLOSURE-REPORT-vNEXT.md` |
| `PENDING-OWNER-DECISIONS.md` **P-27** | five of its carried items are closed by text | Updated, with the remainder named |
| RFC-0010's word ceiling | the additions took the file past 7,000 words | The amendment log was moved to Tier 2; the file now measures under the ceiling. Current figure: the generated `../CONTEXT-BUDGET-REPORT.md` |

---

## Migration / supersession plan

All of the above lands in **one logical change** (CC-REV-2). The manifest,
both indexes, the budget report and the routing matrix are regenerated in the
same commit as the clause edits; act 1's argument is re-quoted in the same
commit; and `check_governance.py` is run before and after.

**What this delta does not do, and must not be read as doing:**

1. It performs **no owner act**. Act 1 remains unperformed; every clause here
   is candidate text inside its digest subject.
2. It does not place any clause at a lifecycle stage. **P-23** is open.
3. It does not settle whether bounded missions are lawful under unamended
   doctrine. **D4 / P-24** is open.
4. It does not claim the seams are closed. That claim requires a review this
   session may not perform on itself.

---

## Review

**Required class:** confirming review over the exact repaired bytes, by a
reviewer that did not author them and receives no authoring rationale
(CC-REV-1; charter §6.7).

**Reviewer:** commissioned as **RD-1** after these bytes were frozen, over
the frozen bytes only, with no authoring rationale. Its raw output is stored
unedited in this round's reviews directory once it returns; until then there
is no review file, and its absence is the correct state rather than an
oversight.

**Verdict:** recorded verbatim in `MISSION-SAFETY-CLOSURE-REPORT-vNEXT.md` and
in `reviews/`. **A repair pass and the review of that pass cannot be the same
pass** — this file is the repair, and it does not get to grade itself.
