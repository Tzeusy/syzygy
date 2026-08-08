---
id: RFC-0010
title: Mission Control and Autonomy Envelopes — completion adjudication, effects, recovery, and stop
status_source: owner-act-record
module: effects-recovery-and-stop
clauses: "RFC10-18..RFC10-20, RFC10-23, with sub-clauses RFC10-18(a), RFC10-19(a) (see the package clause map)"
governs: [completion-adjudication, effect-classification, effect-dimensions, recovery, stop-guarantees]
applies_to: [mission-control, workspace, machine-clients]
depends_on: [RFC-0002, RFC-0003, RFC-0004, RFC-0005]
tags: [correction-plane, adjudication, compensation, stop, partial-failure]
---

# RFC 0010 — Mission Control: completion adjudication, effects, recovery, and stop

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until
the independent A1 correlation mechanism exists, and as a Syzygy-verified
effective act only after correlation (RFC3-16). Absent such a record, this
contract binds nothing.

**Package:** module 4 of 5 of the RFC 0010 contract package. Index, clause
map, lookup rule, package-level integration and deferrals: `README.md`.
Rationale, amendment history, and violation cases:
`../../history/RFC-0010-history.md` (non-normative).

**Serves:** VIS-2, VIS-4; SEC-3, SEC-4.

## 1. Scope of this module — the correction plane

The prevention plane (modules 1–3, 5) makes out-of-envelope acts impossible
at Syzygy's choke points. Prevention is not enough, because prevention only
ever addresses the *future*. This module addresses the *past*: work already
dispatched, money already spent, effects already applied, and a human who
needs to be able to stop all of it. Pause is not rollback; refusing the next
act does not undo the last one. It fixes: independent completion
adjudication and the independently established effects-applied determination
(RFC10-18, RFC10-18(a)); effect classification, compensation, recovery and
sibling disposition (RFC10-19, RFC10-19(a)); what stop guarantees
(RFC10-20); and the separately recorded effect dimensions (RFC10-23).

## 2. The contract

**RFC10-18. Completion is reported by the executor and established by
another.** A mission's executing agents, fleets, and workers **may report**
that the completion predicate is satisfied and **may never establish it**.
The `running → completed` transition is taken only by (a) an owner act, or
(b) a declared, owner-approved evaluation independent of the executing
principal and whose supporting evidence is `gate-backed` (RFC2-25) — never by
the principal that performed the work, and never by a principal that
principal routed. **Independence is transitive, and established rather than
asserted:** a principal routed by the executing principal at *any* depth is
not independent, and the establisher is named in the envelope at approval
time — the **completion establisher is a required envelope field under
RFC10-7's minimum**, honored under RFC10-9's provenance rule, and a derived
child mission **inherits its parent's declared establisher** (RFC10-8) — so
independence is a property of the approved envelope rather than a runtime
selection. An establisher chosen after the fact by the party whose work it
adjudicates is not independent, whatever relation it declares.

A mission's terminal state is an **authorization-bearing
determination** under RFC3-16(a) where it discharges an owner act's objective.
Where no independent establisher exists for a mission's objective class —
including wherever RFC2-19 leaves reconciliation uncomputed — the mission
**never reaches `completed`**. Which state it does
reach depends on whether effects have been applied — **as established under
RFC10-18(a), never as asserted by the executing principal**:

- **With effects already applied it enters `failed`**, so that RFC10-19's
  compensation, enumeration and disposition duties fire. Those duties are
  keyed to `failed`, `cancelled` and `expired`, and RFC10-19 states that
  `blocked` discharges none of them — so routing an effect-bearing mission to
  `blocked` would place it outside the correction plane entirely.
- **With no applied effects it enters `blocked`** with an Attention Item.
  **No human resolution act is owed for this block, and this clause says so
  rather than implying one.** RFC10-5's human-resolution rule is scoped to
  blocks arising under RFC10-8 or RFC10-11; an RFC10-18-sourced block arises
  under neither, and an earlier revision cited RFC10-5 for an obligation
  RFC10-5's own scope excludes. What bounds this park is RFC10-5's **maximum
  park duration**, which holds for every block class: at the maximum the
  mission transitions to `expired`, RFC10-19's duties fire, and RFC10-17(a)
  releases the reservation. A human resolution act stays *available* and is
  the better exit; it is simply not owed.

An unstated minimum evidence tier means `gate-backed`;
"the strongest applicable tier" (RFC10-6) is never a judgment the executing
principal makes for itself.

**RFC10-18(a). Whether effects were applied is established, not asserted.**
One predicate — *have external-mutation effects (RFC10-23 dimension (ii))
been applied under this mission?* — decides whether the correction plane
engages at all. **This sub-clause governs that predicate wherever it
appears**, not only in the branch above: RFC10-19's `with effects already
applied` trigger, RFC10-19(a)'s `after applying effects` gate, RFC10-20(c)'s
`any effect already applied`, and RFC10-17(a)'s applied-effects row selection
are the same determination and are subject to every rule below, including
the fail-closed Unknown rule. That enumeration covers every site in the
current package, and **any future clause keying on this predicate is
governed by this sub-clause by that fact alone, named here or not** — a
predicate that has an establisher in one clause and none in a clause that
carries its duties is not established. The executing principal **may
report** on it and **may never establish** it, on the terms RFC10-18 sets
for completion. A branch selector chosen by the party it routes is not a
determination, so this one carries all four of completion's requirements:

- **Evaluator.** The same class of party RFC10-18 requires for `running →
  completed`: an owner act, or a declared, owner-approved evaluation
  independent — transitively — of the executing principal and of every
  principal it routed, **named in the envelope at approval time on the same
  terms as the completion establisher, and inherited by derived children
  (RFC10-8)**.
- **Evidence.** The mission's guardrail decision record (RFC10-10), each run's
  execution record (RFC4-18..RFC4-21), and the envelope's declared effect
  classification (RFC10-19), retained for the mission's full retention horizon.
  A determination whose evidence has aged out is Unknown, not negative.
- **Minimum evidence tier.** `gate-backed` (RFC2-25). A `report-fact`
  assertion by the executor is admissible as evidence and is never the
  determination.
- **Externally mediated and externally credentialed effects.** An effect
  reachable outside Syzygy's mediation is representable only as a declared,
  named **unmediated effect surface** on the envelope — the boundary RFC10-10
  draws for enforcement and RFC10-20 for stop. Syzygy's records cannot
  establish that an unmediated effect did *not* occur, so this predicate
  resolves **Unknown** where the envelope names any such surface — **and
  equally where the granted credentials, tools, and execution profiles
  reach beyond what declared adapter coverage observes: the Unknown keys on
  established coverage, never on the envelope's own declaration alone** —
  unless an independent adapter-backed observation (RFC 0004) covers the
  surface in question.

**The predicate is scoped to the external-mutation dimension, and the other
dimensions are recorded, not erased.** Consented provider disclosure and
metered resource consumption are effect dimensions of their own (RFC10-23,
dimensions (iii) and (iv)), pre-authorized by the RFC5-14 consent record and
the RFC10-17 reservation respectively; they are **outside this predicate** —
a mission whose only extramural effects are consented disclosure and
reserved spend has, for this predicate, applied no effects, and its record
still states both dimensions and is **never rendered as "no effects"**
(RFC10-23). Disclosure without a covering consent, or outside the consent's
named content classes, is an external mutation for this predicate.

**Unknown fails closed: where whether effects were applied is Unknown, effects
are treated as applied** — for recovery, for reservation, and for
human-attention purposes — until evidence establishes otherwise. The mission
enters `failed`, RFC10-19's duties fire, and the Attention Item states that the
disposition rests on an unresolved determination rather than on an observed
effect, so a compensation record never implies an effect was seen. This is
RFC10-17's Unknown-spend rule applied to the predicate that routes the whole
correction plane: **Unknown effects are never read as no effects.** The cost of
that reading is a compensation attempted needlessly; the cost of the other is
an applied effect nobody is told about.

**RFC10-19. Effects are classified before they are authorized.** Every effect
class an envelope permits is declared **atomically-reversible**,
**compensatable** (with the compensating action named and its **maximum cost
declared**), or **irreversible**. An effect class not so classified is not
authorized — RFC10-7's unstated-is-narrowest rule applied to effects.
**`atomically-reversible` means exactly this and nothing wider: reversal is
performed automatically and atomically by the mediating transaction as part
of the same act, such that no post-hoc action exists to attempt.** It is a
guarantee of the mediating surface, evidenced at classification time — never
an assertion of the envelope author — and **any effect class that does not
meet that definition and is not declared irreversible is compensatable by
force. There is no generic `reversible` class.** An envelope permitting any
irreversible class states that class explicitly on its own face; **a
destructive-operation class reaches a mission only where the envelope names
it, never by inheritance from an execution profile's standing approval
(RFC5-22)**. Where a mission enters `failed`, `cancelled`, or `expired` with
effects already applied: every compensatable effect's compensating action is
attempted and its outcome recorded as evidence; every atomically-reversible
effect's reversal is **verified from the mediating surface's transaction
record** — a reversal that cannot be verified reclassifies the effect as
irreversible for this mission, under the reclassification rule below; every
irreversible effect is enumerated in a single Attention Item naming what
cannot be undone; and the mission's terminal reason (RFC10-5) states the
disposition of every applied effect **in every recorded dimension
(RFC10-23)**. **Every effect instance records: its effect class and
dimension, the surface it touched, the acting principal, the establishing
evidence, its reversal or compensation action and that action's funding, and
the outcome.** **Pause is not rollback**: transitioning to `paused` or
`blocked` discharges no obligation under this clause. A **named recovery
owner** — the owner, or a principal the envelope designates — is bound at
approval time; the recovery owner's duties are to route and attend the
recovery, and **a machine principal so designated is an owner-act submission
channel only (RFC10-3): it may execute declared compensating actions within
`recovery_reserve` and may authorize nothing beyond them**. Resumption from
`paused` re-verifies the pinned inputs (RFC10-4), the remaining reserved
budget (RFC10-17), and the envelope's continued act provenance (RFC10-9)
before any dispatch.

**A compensating action that cannot be funded is an escalation, not a
silence.** Where the `recovery_reserve` (RFC10-17) is insufficient
to run a compensating action, the mission does not simply omit it: the
shortfall is an escalation trigger under RFC10-13, every uncompensated effect
joins the single Attention Item naming what cannot be undone, and the terminal
reason states it as uncompensated-for-want-of-budget. **This clause imposes no
duty RFC10-11 can quietly make impossible** — an exhausted bound bounds
further *work*, never the accounting of what that work already did.

**A compensating action that fails is not discharged by having been
attempted.** The effect is **reclassified as irreversible for this mission**,
joins the single Attention Item naming what cannot be undone, and is stated as
*uncompensated* in the terminal reason. An effect declared `compensatable`
whose compensation failed, and which the record shows only as an attempted
action, violates this clause: the declaration said it could be undone, the
attempt established it could not, and the record must carry the second fact
too. Where compensation succeeds for some effects and fails for others, the
outcome is recorded **per effect**; a partially compensated mission is never
rendered as compensated.

**RFC10-19(a). Sibling disposition after a partial failure is a declared
policy input, never an inference.** Where one run or child mission fails after
applying effects while its siblings completed or remain active, nothing in
this contract decides for the siblings, and nothing should: whether one
sibling's failure invalidates another is a property of the work, not of the
mission machinery. The envelope declares a **sibling disposition on partial
failure** from a closed set fixed at surface specification, minimum members:

```text
independent     a sibling's outcome is unaffected — completed siblings'
                effects stand, active siblings continue
halt-siblings   active siblings stop under RFC10-20; completed siblings'
                effects stand
compensate-all  active siblings stop, and every completed sibling's effects
                are dispositioned under this clause as if that sibling had
                failed
```

**Unstated is not `independent`.** Under RFC10-7's obligation limb an
undeclared disposition takes its strictest reading: `compensate-all` where
every applied effect class is atomically-reversible or compensatable, and
otherwise **`halt-siblings` plus an escalation (RFC10-13) before any further
dispatch, with every compensatable effect still dispositioned** — the
presence of an irreversible class in the mix never yields a weaker default
than its absence: siblings stop, what can be undone is undone, and what
cannot is enumerated.

Two assumptions this clause refuses, because making either is the common
error: **one failure does not automatically invalidate a sibling** — outputs
may be genuinely independent, and forcing compensation destroys correct work;
and **a completed sibling is not automatically still valid** — it may have
consumed the failed sibling's partial output. The declared policy is what
decides between them.

**RFC10-20. What stop guarantees.** A human stop, cancellation, or expiry of
a mission (RFC10-5) has three effects, all immediate at the act: **(a)** no
further work is dispatched and no further Syzygy-mediated act is admitted
under that mission; **(b)** every run Syzygy launched under the mission is
terminated together with its descendants, through the kill switch RFC5-21
requires of every isolation class — a stop that leaves Syzygy-launched runs
executing does not conform — **and the stop propagates transitively to every
child mission derived from it (RFC10-8) and to their descendants**: a
descendant mission is stopped as if the act had named it, its own runs
terminated under this same limb, and its reservation dispositioned under
RFC10-17(a). A stop record reporting (a) and (b) complete while any descendant
mission may still dispatch does not conform, and the **enumeration of the
descendant missions reached** is part of the record. RFC10-8 makes child missions
reservations against the parent; without this limb a parent stop left the
children it authorized dispatching; **(c)** each terminated run's partial state is
checkpointed and recorded as evidence, and any effect already applied is
classified and dispositioned under RFC10-19 — for a run limb (b) failed to
terminate, (c)'s determination completes when that run's records exist or
resolves Unknown, and limb (d) routes that case rather than leaving it
waiting. Effects produced outside
Syzygy's mediation by externally-granted credentials are **not** covered by
(b); the mission's stop record states that boundary explicitly rather than
implying a completeness the runtime cannot deliver (RFC10-10).

**(d) A stop that cannot complete is an outcome, not a wait.** The envelope
declares a **maximum stop latency**; **an undeclared maximum means a stated
finite default: the isolation class's declared kill-report interval, and
where the class declares none, the envelope's shortest declared
duration-typed bound — at minimum the wall-clock budget every runnable
mission has (RFC10-5)**. The act does not return until (a) and (b) hold or
that bound elapses: synchronous, and bounded. Where the kill mechanism
reports failure for a run, **or the bound elapses with neither success nor a
failure report — a hang is a failed stop, and this third exit is stated so
that no reading leaves the act blocking forever** — the act returns having
failed to stop and says so: the mission enters `failed` — never `paused` or
`blocked`, which discharge none of RFC10-19's duties — an Attention Item
enumerates each run that did not terminate and each effect surface it may
still reach, each such run's reservation is retained and named under
RFC10-17(a), and the stop record states the boundary. **An isolation class
admits mission runs only where its kill mechanism reports success or failure
within a declared finite interval — this is this clause's own admission
requirement on the isolation class, stated here and not attributed to
RFC5-21** (RFC5-21 requires the kill switch; the failure-signal floor and
its interval are this clause's): a class without that property is not one a
mission may run under, because a stop with no failure path is an unbounded
latency under a different name.

**RFC10-23. Effect dimensions are recorded separately, and no single
predicate collapses them.** Every mission records, each in its own
dimension:

1. **project mutation** — drafts, proposals, and submissions inside the
   `.syzygy/**` and `openspec/**` namespaces of the mission's declared
   target projects, rendered unadopted (RFC3-16);
2. **external-system mutation** — any state change outside those namespaces
   other than dimensions (iii) and (iv);
3. **external disclosure** — content crossing an egress boundary, lawful
   only under the RFC5-14/RFC5-15 consent gates, recorded with the
   provider, the covering consent record, and the content classes
   disclosed;
4. **resource consumption** — metered spend accounted under RFC10-17.

The correction plane's effects-applied predicate (RFC10-18(a)) engages on
dimension (ii) alone. A mission's terminal record states all four
dimensions. `propose-only` (RFC10-7) bounds dimension (ii) to nothing and
is **never rendered as "no effects"** where dimension (i), (iii), or (iv)
is non-empty: a mission that disclosed content and spent budget had
effects, and the record says which kind, under which authorization.

---

*End of RFC 0010 module 4. Clauses RFC10-18 … RFC10-20 and RFC10-23, with
sub-clauses RFC10-18(a) and RFC10-19(a) living with their parents — the
package README's clause map is the lookup authority. Nothing merged,
nothing retired.*
