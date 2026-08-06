# RD-1b — Mission safety confirming review (rev11c)

**Subject sha256:** 7f823aa3773c7bf47fed2f7634aa696c454b3ca62dea691c656a3f58a191f825
**Commissioned:** 2026-08-06, independent, no authoring context.

# VERDICT
VERDICT: REVISE

Subject digest verified at review start by `sha256sum` — matches the commissioned
value. [Observed] 781 lines.

---

## Answer to the commissioned question

**Yes.** A bounded, autonomous Mission conforming to every clause in this file can
cause an unrecoverable or unauthorized outcome with no owner act, by at least
three independent routes. The strongest, stated as a sequence a conforming
implementer produces without any bad faith:

**The unbounded-spend route.** The owner approves a mission with a monetary budget
of $100 and the maximum autonomy this contract permits — `propose-only`
(RFC10-7, L214–216). The mission dispatches one agent run whose *declared maximum
cost* is $100, satisfying RFC10-17's reservation predicate exactly: "**No work is
dispatched without reserving its declared maximum cost against the envelope at
dispatch time**, and reserved + spent never exceeds authorized" (L396–398). The
run loops, and the model provider bills $5,000. The provider's figure is known
only after the fact (RFC4-21: values "come only from runtime-reported or
toolchain-recorded facts captured as evidence"), so no measurement exists during
the run that RFC10-11 could halt on.

Nothing in this contract prevents that. RFC10-17 does not require the reservation
to be *enforced* anywhere — it requires it to be *recorded*. The clause's own
terminal quantity is "**overrun** (spend exceeding authorized)" (L395–396), and
its remedy is bookkeeping: "Any overrun is recorded as attributable evidence
against the mission and mints its own Attention Item" (L403–406), and "chronic
under-declaration renders as a recorded pattern of overrun attributable to that
authority" (L416–417). $4,900 of the owner's money is spent, irrecoverably,
outside anything the owner authorized, and the contract's response is a ledger
entry and a notification. That is an unauthorized, unrecoverable outcome reached
without an owner act, at the *most conservative autonomy level the contract
allows*.

Two aggravations make this worse than a candid limitation:

1. RFC10-10 states the opposite as a MUST — "Mission Control MUST prevent every
   act it mediates from exceeding the approved authority and resource envelope"
   (L296–297) — and declares it "**preventive**, not merely observational: an
   out-of-envelope act is refused at the choke point … not performed-then-flagged"
   (L300–302). RFC10-10 and RFC10-17 cannot both be satisfied for resource
   bounds: if the MUST held, `overrun` would be an unreachable quantity and
   RFC10-17's entire overrun limb would be dead letter. A reasonable implementer
   resolves this the permissive way, because RFC10-17 is the specific clause and
   it explicitly contemplates the state RFC10-10 forbids. [Inferred]

2. The choke point that would carry the check exists and is named elsewhere in
   the corpus — RFC5-15's single egress choke point ("every network transmission
   of governed-project content passes one consent check") and RFC5-21's isolation
   floor, which requires "enforced resource limits" of every class. **No clause
   in RFC-0010 binds a reservation to either.** The reservation is an accounting
   entry that never becomes a limit. [Observed — searched the full file for any
   clause attaching the reserved figure to RFC5-15, RFC5-18 launch, or RFC5-21
   limits; none exists.]

The other two routes are B2 (the `reversible` effect class carries no obligation
at all and is nowhere defined) and B4 (RFC10-5's park cascade has a third limb
that resolves to nothing, and the park it fails to bound is the one holding
applied effects undispositioned). Both are below.

---

## Findings, ranked

### BLOCKING

---

**B1. RFC10-17's reservation is accounting, not enforcement, and RFC10-10 says
otherwise.**

*Attack class: budget escape.* Sequence and analysis as in the answer above.

Exact text in conflict:

- L296–297: "Mission Control MUST prevent every act it mediates from exceeding
  the approved authority and resource envelope"
- L394–398: "**released** (reserved-but-unspent, returned on completion or
  termination), and **overrun** (spend exceeding authorized). **No work is
  dispatched without reserving its declared maximum cost against the envelope at
  dispatch time**, and reserved + spent never exceeds authorized"
- L403–406: "Any overrun is recorded as attributable evidence against the mission
  and mints its own Attention Item; a mission record showing a respected bound
  with unrecorded overrun is a violation of this clause."

[Observed] The invariant "reserved + spent never exceeds authorized" is stated
over the *ledger*. Nothing states it over *consumption*. [Observed] The only
clause that could carry consumption-side enforcement, RFC10-11, fires on
"**Reaching** any envelope bound" (L312) — a measurement event, and no clause in
this file states when spend is measured (see N11).

A related sub-escape rides the same gap: the "declared maximum cost" is a
declaration. RFC10-17 correctly forbids the dispatched worker from sizing its own
reservation ("declared by the envelope or by the dispatching authority, never by
the worker being dispatched", L414–416) — but the *dispatching authority* inside a
running mission is itself a mission-controlled component. A dispatching agent that
declares $1 per run and dispatches 100 runs that each cost $50 conforms to every
sentence of RFC10-17 up to the point where the pattern renders as recorded
overrun. Under-declaration is detected, never prevented.

**Repair.** Add to RFC10-17: a dispatch is admitted only where the reserved
maximum is bound to an enforced runtime limit at the launch gate — RFC5-21's
"enforced resource limits" for the run, and a remaining-headroom predicate
evaluated at the RFC5-15 choke point for every provider transmission — and where
no such enforceable limit exists for a cost kind, that cost kind is not
delegable under this contract. Then reconcile RFC10-10: either scope its MUST
away from resource bounds explicitly, or state that `overrun` is reachable only
through unmediated surfaces and is a bounded residual, not an expected accounting
state.

---

**B2. `reversible` is the effect class with no definition, no named action, no
funding requirement, and no duty — and it is the class an implementer will
choose.**

*Attack class: irreversibility escape.*

L529–533: "Every effect class an envelope permits is declared **reversible**,
**compensatable** (with the compensating action named), or **irreversible**. An
effect class not so classified is not authorized — RFC10-7's
unstated-is-narrowest rule applied to effects."

L536–541: "Where a mission enters `failed`, `cancelled`, or `expired` with
effects already applied: every compensatable effect's compensating action is
attempted and its outcome recorded as evidence; every irreversible effect is
enumerated in a single Attention Item naming what cannot be undone; and the
mission's terminal reason (RFC10-5) states the reversibility disposition of every
applied effect."

[Observed] Trace `reversible` through that sentence. It gets no attempted action —
that limb is scoped to `compensatable`. It gets no Attention Item — that limb is
scoped to `irreversible`. It gets one line in the terminal reason. **No effect
classified `reversible` is ever actually reversed by any clause in this
contract, and no clause says who would, with what budget, or what happens if the
reversal fails.**

[Observed] `reversible` is nowhere defined in the file. `compensatable` is defined
by its structural requirement (a named compensating action). `irreversible` is
defined by exclusion. `reversible` has no predicate, so the classification is
whatever the envelope author asserts.

Concrete attack: an envelope declares "database row writes" `reversible` ("we can
delete the row"). The mission applies 40,000 of them across a production store,
then fails. RFC10-19 fires: no compensating action is attempted, no Attention Item
is minted for them, the terminal reason states "reversible". The rows stand. The
owner approved a class the envelope told them could be undone, and nothing undoes
it, and nothing tells them it wasn't undone. This *also* defeats RFC10-19's
strongest sentence — "**A compensating action that fails is not discharged by
having been attempted**" (L559–560) — because no attempt is owed, so nothing can
fail, so nothing is reclassified.

It further hollows RFC10-19(a)'s default: `compensate-all` where "every applied
effect class is reversible or compensatable" (L588–589) is a no-op over the
reversible ones.

**Repair.** Either collapse `reversible` into `compensatable` (every non-
irreversible class names its reversing action, funded from recovery headroom, and
a failed reversal reclassifies as irreversible), or define `reversible` narrowly
enough that the absence of a duty is honest — e.g. "an effect whose reversal is
performed automatically and atomically by the mediating surface as part of the
same act, such that no post-hoc action exists to attempt" — and make anything else
`compensatable` by force.

---

**B3. Is egress an "effect"? The file forces the question and breaks whichever way
it is answered.**

*Attack classes: irreversibility escape, unknown-as-green.*

RFC10-18(a) fixes one predicate: "*have effects outside `.syzygy/**` and
`openspec/**` been applied under this mission?*" (L487–488), and says it "decides
whether the correction plane engages at all" (L488–489).

RFC10-7's `propose-only` says the mission "may **not** cause any effect outside
those two namespaces" and enumerates prohibitions, then carves out: "Egress to a
model provider remains permitted only under an RFC5-14 consent record naming the
provider and content classes" (L238–239).

[Observed] The carve-out's grammatical form — a prohibition on effects outside the
two namespaces, followed by "*remains permitted*" for egress — forces the reading
that **egress is an effect outside the two namespaces**. Otherwise the carve-out
is unnecessary. On that reading:

- Egress is irreversible in the only sense that matters: content transmitted to a
  provider cannot be recalled. Under RFC10-19 it is therefore an irreversible
  effect class, and "An envelope permitting any irreversible class states that
  class explicitly on its own face" (L533–534), and "An effect class not so
  classified is not authorized" (L531–532). **So no `propose-only` envelope may
  call a model provider unless it declares itself as permitting an irreversible
  class** — which contradicts `propose-only`'s own grant that a mission "may …
  run agents within its reserved budget (RFC10-17)" (L231–232), and destroys the
  premise on which the cap is said to make "several other deferrals safe"
  (L241–243).
- And every mission that ever called a provider has "applied effects", so
  RFC10-18's no-independent-establisher branch routes it to `failed` (L466–470),
  firing RFC10-19's duties and an irreversible-effects Attention Item, for every
  ordinary mission. The expected terminal state of a well-behaved mission becomes
  `failed`, and the attention queue floods — which RFC10-22 then answers by
  pausing missions.

On the other reading — egress is not an "applied effect" — a mission that
transmits an entire governed corpus to a provider registers as *no applied
effects*, enters `blocked` rather than `failed` (L471), and the correction plane
"engages at all" nowhere. The single largest irreversible act `propose-only`
permits sits outside the plane built to catch irreversible acts.

[Inferred] Neither reading is available without breaking a clause the contract
leans on. This is the seam where the contract's safety story is thinnest: the
autonomy cap that makes everything else safe permits, by name, an unrecallable
transmission whose classification the contract never settles.

**Repair.** State in RFC10-18(a) whether provider egress is inside the predicate.
If inside: give `propose-only` an explicit egress classification (irreversible,
bounded by the RFC5-14 consent's content classes) rather than requiring each
envelope to name it, and carve the resulting mission-terminal branch so an
egress-only mission does not route to `failed`. If outside: say so, and add a
separate disclosure duty for egress-only missions so the owner is told what left.

---

**B4. RFC10-5's park cascade has a third limb that resolves to nothing, and
RFC10-22 never defaults the maximum the second limb depends on. Indefinite park
is reachable.**

*Attack classes: time escape, irreversibility escape.*

L148–152: "Every non-terminal park carries a **maximum park duration**, declared
by the envelope; where none is declared the maximum is the expiry of the Attention
Item that park minted (RFC10-12), and where the park minted none it is the
envelope's shortest declared maximum. Silence buys no unbounded park in any
direction."

[Observed] Limb 3 — "the envelope's shortest declared maximum" — has no referent.
Its own premise is that the envelope declared no maximum park duration, so it
cannot mean that. The envelope's other declared maxima are a *maximum stop
latency* (RFC10-20(d), a latency for a different act), a *maximum outstanding
attention count* and a *maximum item rate* (RFC10-22 — a count and a rate, neither
a duration). "Shortest" over a set containing a count and a rate is undefined. If
the envelope declares no duration-shaped maximum at all, limb 3 yields nothing and
the park is unbounded.

[Observed] Limb 2 is defeated separately. RFC10-22 says "Every item's expiry falls
within a declared maximum beyond which its stated default is no longer presumed
safe; an item whose expiry exceeds that maximum is not well-formed" (L678–680) —
but RFC10-22 defaults only the *outstanding count*: "an undeclared maximum means
one outstanding item — the narrowest reading (RFC10-7)" (L665–666). **The maximum
item expiry is never defaulted.** An envelope that declares no maximum item expiry
makes an item with a ten-year expiry well-formed, because there is no declared
maximum for it to exceed, and limb 2 then hands the park a ten-year bound.

RFC10-7's obligation limb cannot rescue this. Its rule — "No field's absence ever
relaxes a duty" (L225) — cannot supply a *number*; the narrowest reading of an
undeclared duration is zero, which would expire every park instantly, a reading no
implementer takes. RFC10-5 supplies its own three-limb cascade precisely because
the general rule cannot decide it, which signals the cascade is meant to be
exhaustive.

Why this is blocking rather than cosmetic: RFC10-17(a) hangs the entire correction
plane off the park duration. Its table row reads "`blocked` **with** applied
effects | as above, and RFC10-19's duties fire **at the expiry, not at the park**"
(L433). An unbounded park is therefore an unbounded hold on reserved budget *and*
a mission with applied effects whose compensation, irreversible-effect enumeration
and terminal disposition never fire. The clause that exists to guarantee "No park
is indefinite" (L147) does not close its own last case.

**Repair.** Replace limb 3 with a stated absolute default park duration fixed by
this clause (a number or "the envelope's declared wall-clock budget remainder"),
and default RFC10-22's maximum item expiry the same way limb 3 of the count bound
is defaulted.

---

**B5. RFC10-20(d)'s undeclared stop latency is unbounded in exactly the case it
claims to bound.**

*Attack class: stop escape.*

L622–627: "The envelope declares a **maximum stop latency**; an undeclared latency
means the act is synchronous — it does not return until (a) and (b) hold.
Synchronous is not unbounded. Where the RFC5-21 kill switch reports failure for a
run, or a declared maximum elapses, **the act returns having failed to stop**".

[Observed] The clause offers exactly two exits from a stop that is not succeeding:
(i) the kill switch **reports failure**, or (ii) a **declared maximum elapses**. In
the undeclared-latency case there is no declared maximum, so exit (ii) is
unavailable by construction. If the kill switch neither succeeds nor reports
failure — it hangs, the container is wedged, the control connection is gone —
exit (i) never fires either. The synchronous act blocks forever. The assertion
"Synchronous is not unbounded" is stated but not implemented.

The clause's closing sentence does not cover this: "An isolation class whose kill
switch has no failure signal has not satisfied RFC5-21 and is not one a mission
may run under" (L631–633) addresses a switch that lacks a failure *channel by
design*, not one that has a channel and never uses it. A hang is not the absence
of a signal.

Nor does RFC10-5's park rule reach it: a mission with an unreturned stop act is
still `running`, not parked, so nothing bounds it. Meanwhile RFC10-20(a) has
already taken effect, so the mission dispatches nothing new — but its runs
continue executing, spending, and reaching effect surfaces, and the human who
pressed stop is holding an act that never returns.

Secondary defect in the same sentence: **the citation overreaches.** RFC5-21
(`rfcs/RFC-0005/execution-profiles.md:141`) requires of every isolation class "a
kill switch terminating the run and its descendants". It imposes **no**
failure-signal or observability requirement. RFC10-20(d)'s claim that a switch
without a failure signal "has not satisfied RFC5-21" is not a reading RFC5-21's
text supports. The rule RFC10-20 wants is fine; it must be stated as RFC10-20's
own requirement, not attributed to RFC5-21. See N6.

**Repair.** Make the undeclared default a stated finite maximum rather than
"synchronous", and add a third exit: elapse of that default with neither success
nor a failure report is itself a failed stop.

---

**B6. The D3 precondition is stated only in §2 prose. No numbered clause carries
it, and RFC10-16 gates on OpenSpec, not on doctrine.**

*Attack class: authorization laundering.*

L68–74: the D3 doctrine amendment "**is not applied by this RFC**; until the owner
rules on it, this contract's reading of human-triggered propagation stands only as
far as doctrine already permits — which means missions can be *specified* under
this contract but cannot lawfully *operate* under unamended doctrine's one-pass
trigger."

[Observed] That sentence lives in §2 "Motivation and doctrine grounding". It is
not RFC10-*n*. RFC10-16, the file's only phase rule, conditions implementation on
OpenSpec coverage — "every observable consequence either maps to an approved
OpenSpec requirement and scenario … or carries a reviewed N/A judgment" (L693–697)
— and says nothing about D3.

[Observed] Per `AGENTS.md`, act 5 (D3) is the one **optional** owner act; acts 1–4
can be performed without it. So the reachable state is: contract accepted at act
1, D3 never ruled on, OpenSpec written, RFC10-16 satisfied, missions operating.
The only thing standing between that state and a doctrine violation is a reader
who happens to read §2 and treats non-clause prose as binding. That is the
benevolent-implementer assumption this review was told not to grant.

The stake is the whole commissioned question: a mission operating without D3 is an
autonomous multi-pass propagation that unamended VIS-4/one-pass doctrine does not
authorize — an unauthorized outcome whose authorizing owner act does not exist.

**Repair.** Promote the condition into RFC10-16 (or a new numbered clause): no
mission leaves `awaiting-approval` until the doctrine amendment governing
multi-pass autonomous propagation is adopted by owner act, or the owner records a
ruling that unamended doctrine already permits it.

---

### NON-BLOCKING FINDINGS

**N1. A derived child mission's completion establisher is named by an agent, not
by an approval.** *(independence escape)*

RFC10-18 makes independence structural: "the establisher is named in the envelope
at approval time (RFC10-9), so independence is a property of the approved envelope
rather than a runtime selection" (L452–454). RFC10-8 lets an agent mint child
missions where the parent grants decomposition, with "the **parent's owner act
plus a recorded derivation**" as provenance (L256–259). [Observed] **A child
envelope never passes an approval.** So "named at approval time" has no analogue
for children: the agent authors the child envelope and thereby selects the child's
completion establisher and its RFC10-18(a) effects-determination evaluator. RFC10-8
forbids *widening a bound*; naming an establisher is filling a field, not widening
one, so the prohibition does not obviously reach it. An establisher the fleet
selected for its own child is exactly the "chosen after the fact by the party whose
work it adjudicates" case RFC10-18 refuses (L455–456), arriving by a door RFC10-18
did not think to close. **Repair:** state that a child mission inherits its
parent's declared establisher and evaluator, or that naming either in a child
envelope is a bound subject to RFC10-8.

**N2. RFC10-8's derived-child provenance is a form RFC3-16(b) item 3 does not
admit, and RFC10-9's "every amendment" rule is not reconciled with it.**
*(authorization laundering)*

RFC10-9: "The envelope (and every amendment to it) is an **authorization-bearing
governance artifact** under RFC3-16(a): it is honored only with **verifiable**
owner-act provenance" (L268–270). RFC3-16(b) item 3
(`rfcs/RFC-0003/governance-homes-and-owner-acts.md:249–252`): "the **exact content
or revision digest** of the artifact as acted on — **approving a path never
approves future content at that path**; an artifact edited after the act is, for
the predicate, an artifact with no act." [Observed] A child envelope's digest did
not exist at the parent act, and the "recorded derivation" is a tree-resident
record — precisely the class RFC3-16(a)/(c) declares non-self-authenticating.
Mitigating: the ⊆-parent debit is computed by the control-plane service, which
RFC10-2 makes the owner of runtime state, not by the tree. So the blast radius
stays inside the parent's owner-authorized bounds and this is not a widening.
It remains a stated exception to RFC3-16(b) item 3 that neither clause
acknowledges. **Repair:** state the derivation exception explicitly in RFC10-9 and
bound it (derived envelopes are honored on the parent act only for envelopes the
runtime computed as ⊆ parent; a derivation record read from the tree honors
nothing).

**N3. Attention allowance is not debited across the parent/child tree, so one
owner act can mint unbounded attention demand.** *(unknown-as-green / denial of
owner attention)*

RFC10-22 bounds attention **per envelope**: "Every envelope declares a **maximum
outstanding attention count** and a **maximum item rate** for the missions under
it" (L663–665). RFC10-8 debits **budget** across the child tree — "Every child
grant is **debited from the parent's remaining envelope at grant time**"
(L259–261) — and debits nothing else. [Observed] Attention is not a debited
resource. A parent with a decomposition grant and budget for N children mints N
attention allowances (each defaulting to one outstanding item) from one owner act.
RFC10-22's own closing sentence names the harm this permits: "without both,
denial of owner attention is reachable without widening anything" (L682–683) — and
the child tree is a route to it that does not widen anything. **Repair:** make the
attention allowance a debited quantity on the RFC10-8 sibling-sum invariant,
exactly as budget is.

**N4. Independence is required of the adjudicator and not of the evidence, so a
mission's own output can be the sole basis for its own completion.**
*(independence escape)*

RFC10-18 requires "a declared, owner-approved evaluation independent of the
executing principal and whose supporting evidence is `gate-backed` (RFC2-25)"
(L448–449). [Observed] The independence predicate attaches to the *establisher*;
the evidence requirement attaches only to a *tier*. A `gate-backed` artifact
produced by the executing principal's own Syzygy-launched profiled run qualifies —
RFC5-19 caps only artifacts "of unverifiable origin" at `report-fact`, and a
profiled run's origin is verifiable. So: executor runs the suite, retains the
report, owner-named establisher reads that report and takes `running → completed`.
The mission's own output satisfied its own gate, one indirection away. This may be
the intended and acceptable model (it is how CI works), but the clause's rhetoric —
"never by the principal that performed the work" (L449–450) — promises more than
the predicate delivers, and an implementer could reasonably read it as ruling this
out. **Repair:** say explicitly which of the two the clause requires.

**N5. RFC-0004 is a substantive reliance and is not in `depends_on`.**
*(citation / load-map defect)*

L8: `depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008]`.
[Observed] RFC-0010 relies on RFC-0004 for the evidence that makes two of its
load-bearing clauses operable: RFC10-17's `spent` is "admitted from the execution
record of a Syzygy-launched profiled run (RFC5-21, RFC4-18..RFC4-21) or from an
adapter-backed provider record (RFC 0004)" (L408–410), and RFC10-18(a)'s Evidence
limb requires "each run's execution record (RFC4-18..RFC4-21)" (L503–505) and an
"independent adapter-backed observation (RFC 0004)" (L516). Per
`CONTRACT-DEPENDENCY-INDEX.md` line 132, RFC-0004 is recorded for RFC-0010 as a
`cites` edge only. The index's own definition of `depends_on` is "A must be loaded
to interpret or modify B correctly" — which RFC-0004 plainly is here. Note this is
**not** caught by `build_dependency_index.py --check`: that script classifies any
citation absent from `depends_on` as a `cites` edge rather than flagging it, so
"no drift" is not evidence of correctness (verification rule 4 — the denominator).
Consequence: a reader who compiles context for RFC-0010 via the declared
dependency set never loads the contract defining the evidence RFC10-17 and
RFC10-18(a) rest on. [Observed] RFC-0011, which relies on RFC-0004 the same way,
does declare it. RFC-0007 and RFC-0009 are correctly cites-only — those references
are the RFC10-16 "shape-parallel" mentions, which verification rule 5 says are not
dependency edges.

**N6. RFC10-20(d) attributes a requirement to RFC5-21 that RFC5-21 does not
contain.** Detailed under B5. Standing alone this is a false citation of moderate
severity: the rule binds anyway through RFC10-20 itself, so nothing operational
turns on it, but a reader checking RFC5-21 for the failure-signal floor will not
find one, and an isolation class could be certified RFC5-21-conforming while
failing RFC10-20(d).

**N7. RFC10-5's state diagram lacks the terminal edges its own prose and RFC10-17(a)
and RFC10-20(d) require.** *(internal consistency / state machine)*

L131–135:
```
running ⇄ paused
running → blocked (→ running on unblock, or → expired on park expiry)
running → completed | failed | cancelled | expired
```
[Observed] Every terminal edge originates at `running`. But the same clause's park
paragraph applies to "**both** non-terminal states" (L155) and says "At the maximum
the mission transitions to **`expired`**" (L152–153) — requiring `paused → expired`,
which the diagram does not carry. RFC10-17(a)'s table requires the same:
"`blocked` or `paused`, no applied effects | **held** … released at the resulting
transition to `expired`" (L431). RFC10-20(d) requires `→ failed` from wherever the
stop was issued, including `paused`. The diagram is labelled "candidate" and
"provisional at this contract's acceptance" (L137–138), which covers *freezing*,
not *correctness* — a provisional vocabulary that contradicts three binding
clauses will be transcribed into the OpenSpec state machine as written.

**N8. Recovery headroom is required but never sized.** *(irreversibility escape)*

L439–442: "**Recovery headroom is carved out of `authorized` at approval time and
held undispatchable** … a budget with no declared recovery headroom authorizes no
effect class that requires compensation." [Observed] No clause requires the
headroom to be greater than or equal to the sum of the declared compensating
actions' costs — and RFC10-19 requires the compensating action to be **named**
(L530–531) but not **costed**. An envelope with $0.01 of headroom and five
compensatable classes conforms. The shortfall path is handled honestly (RFC10-19's
"A compensating action that cannot be funded is an escalation, not a silence",
L549–556), so the outcome is disclosed rather than silent — but it is
disclosed *after* the effect is applied and uncompensated, which is the wrong end.
**Repair:** require each compensating action to carry a declared maximum cost, and
require headroom ≥ their sum for the effect classes the envelope permits.

**N9. The write side of the cross-project path-grant seam is open; RFC10-21 closes
only the egress side.** *(scope escape)*

RFC10-21 is the file's strongest clause and it reasons correctly that the predicate
must be "a property of the *content*, not of the mission's scope declaration"
(L643–644), with the worked case "a mission declared against project A alone,
whose envelope grants a path containing project B's checkout" (L645–647). [Observed]
That reasoning is applied only to composites and egress. The same envelope, under
`propose-only`, may "author drafts, proposals, and submissions into `.syzygy/**`
and `openspec/**`" (L231–232) — with **no project qualifier on those namespaces**.
So it may write into project B's governance plane while declared against A.
Partially closed elsewhere: RFC5-12's write consent is per repository, so B must
have granted write consent — but that consent is a property of B, not of the
mission's target, so a B that consented for its own missions has consented for
A's. Damage is bounded: an unadopted draft authorizes nothing (RFC3-16(a)), and
RFC3-9 routes a governance artifact Syzygy did not author to a contradiction.
**Repair:** qualify `propose-only`'s two namespaces to the mission's declared
projects, on RFC10-21's own reasoning.

**N10. RFC10-8's load-bearing first sentence is scoped to the actor's own
envelope.** L245–247: "No agent, fleet, worker, or Mission Control component may
widen any bound of **the envelope it runs under**". [Observed] Widening a
*different* mission's envelope is outside that sentence. It is caught by the next
sentence ("Widening is exclusively a human act", L251–252) and by RFC10-9's
every-amendment rule, so nothing escapes — but the clause the contract calls "the
load-bearing rule" carries a scope its own backstops have to repair. Advisory.

**N11. No clause states the measurement instant for spend, or the clock for any
duration bound.** *(time escape / unknown-as-green)*

RFC10-17: "**Where measured spend against a bound is Unknown (RFC8-19, RFC2-23),
the bound is treated as reached**" (L400–402). [Observed] The file never says when
spend is measured. Read literally, provider spend is Unknown throughout every run
(RFC4-21 makes it post-hoc), so every mission halts on its first dispatch — an
unusable reading. Read as intended, there is an unstated measurement point and the
intra-run window is the B1 gap.

Separately, [Observed] no clause names the clock source for the maximum park
duration, the maximum stop latency, item expiry, or the wall-clock budget. The
corpus's own precedent cuts against a wall clock: RFC2-15 says a dismissal whose
expiry lapses "renders the gap again — **through a new evaluation, never a
wall-clock flip**", and RFC2-19 makes reconciliation evaluations human-triggered.
If park expiry is likewise computed only at an evaluation, then "At the maximum
the mission transitions to `expired`" has no actor and no trigger, and the park
bound is not self-executing — which would make B4 worse, not better. **Repair:**
name the actor and the clock for every duration bound, and state that these
transitions are runtime-service-driven rather than evaluation-driven.

**N12. "A named recovery owner" has no stated duties and no requirement of being
human.** L544–546: "A **named recovery owner** — the owner, or a principal the
envelope designates — is bound at approval time". [Observed] RFC 0005 principals
include machine clients, so the envelope may designate a fleet worker. No clause
says what the recovery owner does, what it may authorize, or that it must be
independent of the executing principal. Given RFC10-3's care that "a machine
credential can never itself produce the owner act" (L110–111), a designated
machine recovery owner is a hole shaped like the one RFC10-3 closed. **Repair:**
state the recovery owner's duties, and require it to be human or to be an owner-act
submission channel only.

**N13. RFC10-7's autonomy-level cap lifts on two conditions, only one of which
requires an owner act.** L239–241: "A level above `propose-only` is inoperative
until both the vocabulary is enumerated **and** each level's permitted effect set
is **stated**." [Observed] The first conjunct names an owner act ("Until the
autonomy-level vocabulary is enumerated by owner act", L229–230). The second names
no actor, and §7 defers the enumeration "to surface specification / OpenSpec
review" (L761–763). So the *content* of `merge` and `deploy` — the permitted effect
sets — can be fixed by an approved OpenSpec requirement, which this contract
nowhere makes an owner act. The owner enumerates the words; the spec decides what
they mean. **Repair:** require each level's permitted effect set to be fixed by the
same owner act that enumerates the vocabulary.

---

### CHECKS THAT CAME BACK CLEAN

- **Front-matter clause list matches the file.** L5 declares
  `RFC10-1..RFC10-22 (sub-clauses RFC10-17(a), RFC10-18(a), RFC10-19(a); no gaps,
  no retired numbers)`. [Observed] All 22 numbers and all three sub-clauses are
  defined; none missing, none duplicated, none extra. RFC10-16 is defined out of
  numeric order (§3.8, after RFC10-22) — deliberate and stated in §1.
- **Every `RFC\d+-\d+` citation resolves to an existing clause.** [Observed]
  Checked all 32 distinct foreign identifiers against their defining files. All
  resolve. Substance verified for the load-bearing ones: RFC2-15 (contradiction,
  owner adjudication only, never by precedence — matches RFC10-6's use), RFC2-19
  (V0 renders absence, V1 computes — matches RFC10-18's "leaves reconciliation
  uncomputed"), RFC2-25 (`gate-backed` and `report-fact` are real tiers with the
  authority RFC10-18/18(a) attribute to them), RFC3-16(b) item 3 (is the exact
  content digest, as RFC10-14 says), RFC3-16(c) (does split by role and does name
  RFC10-9 as its worked example — RFC10-9's use is exactly right), RFC5-3 (two
  exhaustive client classes, no third — RFC10-3 correct), RFC5-14/5-15 (consent
  names provider and content classes; undeterminable fails closed — RFC10-21
  correct), RFC5-22 (standing-approved-by-profile is real, so RFC10-19's
  no-inheritance rule bites on a real mechanism), RFC8-19 (absent means Unknown
  never zero), RFC8-12/8-28/8-30 (§5's two-field rule is accurate), RFC6-13/6-14,
  RFC4-21. The four RFC10-16 shape-parallel targets (RFC6-28, RFC7-38, RFC8-32,
  RFC9-52) all exist and are all "this contract schedules nothing" clauses.
  **One overreach only: N6.**
- **`verify_final_prespec.py`** — `PASS — all checks clean`. RFC-0010 is 6,749
  words, under the 7,000 ceiling; it is not among the flagged modules.
  `build_contract_index.py --check` and `build_dependency_index.py --check`
  both report no drift — but see N5 for why the dependency check cannot catch
  the defect there.
- **Attacks that the clauses genuinely stop.** Recording these, because a review
  that lists only holes misrepresents the artifact: sibling children jointly
  exceeding one owner act (RFC10-8's grant-time debit, L259–263); a child mission
  wider than its parent (same); a machine credential producing its own approval
  (RFC10-3, L108–111); an agent asserting "condition cleared" out of an RFC10-8 or
  RFC10-11 block (RFC10-5, L143–146); a bulk approval over unenumerated items
  (RFC10-12, L336–338); an expiry default that widens (RFC10-12, L332–334); an
  Attention Item silently disappearing (RFC10-13, L340–343); children outliving a
  parent stop (RFC10-20(b)'s transitive limb with its enumeration requirement,
  L607–615); a compensation that failed being recorded as merely attempted
  (RFC10-19, L559–567); partial compensation rendered as compensated (same);
  Unknown-effects read as no-effects (RFC10-18(a)'s fail-closed rule, L518–527);
  Unknown spend read as zero (RFC10-17, L400–403); a self-reported spend figure
  (RFC10-17's "never from a self-report by the principal whose spend it is",
  L410–411); a composite laundering project B's content through a mission declared
  against A (RFC10-21, L635–651 — the best clause in the file); an unstated
  obligation failing open (RFC10-7's obligation limb, L218–227); a
  destructive-operation class inherited from a profile's standing approval
  (RFC10-19, L535–536); a mission converting owner attention into throughput
  (RFC10-22's pause-on-bound, L666–667, subject to N3); a second exempt attention
  class (RFC10-22, L669–675); a re-spawned mission after a stop (RFC10-4 +
  RFC10-9 require a fresh owner act for a new top-level mission).

---

## Minimum to reach CONFIRM

1. **B1** — bind the reservation to an enforced limit at the launch gate (RFC5-21
   resource limits) and to a remaining-headroom predicate at the RFC5-15 choke
   point; make an un-enforceable cost kind non-delegable; reconcile RFC10-10's MUST
   with RFC10-17's `overrun` so both can be true at once.
2. **B2** — define `reversible`, or collapse it into `compensatable` so that every
   non-irreversible applied effect carries a named, funded action and a failed
   action reclassifies as irreversible.
3. **B3** — settle in RFC10-18(a) whether provider egress is inside the
   effects-applied predicate, and repair whichever of RFC10-7's `propose-only`
   grant or RFC10-18's `failed` branch that answer breaks.
4. **B4** — replace RFC10-5's third park limb with a stated absolute default, and
   default RFC10-22's maximum item expiry.
5. **B5** — give RFC10-20(d)'s undeclared-latency case a finite stated default and
   a third exit for a kill switch that neither succeeds nor reports failure;
   restate the failure-signal floor as RFC10-20's own requirement rather than as
   RFC5-21's (N6).
6. **B6** — carry the D3 precondition in clause text, not in §2 prose.

N1, N3, N5 and N7 are cheap and I would take them in the same pass: N1 and N3
close real escapes at the parent/child seam, N5 is a one-token front-matter fix
with a real context-load consequence, and N7 is a diagram that will be transcribed
into an OpenSpec state machine as written.

---

## Note on method and limits

[Observed] I read: the subject; `history/RFC-0010-history.md` was available and I
did not need it for any finding above (every finding rests on the subject's own
text or on a cited clause's text). I read the cited clause text in RFC-0002
(reconciliation-chain, rendering-vocabularies), RFC-0003
(governance-homes-and-owner-acts), RFC-0004 (execution-record), RFC-0005
(admission-and-boundary, consent-egress-secrets, execution-profiles), RFC-0006,
RFC-0008 (state-vocabulary-and-cost, accounting-reconciliation-and-release),
RFC-0011 front matter and RFC11-2, and `CONTRACT-DEPENDENCY-INDEX.md`. I did not
read any other file in this reviews directory, any commit message, or
`PROCESS-LESSONS.md`.

[Observed] Citation resolution and clause-definition enumeration were done with
Python `re` over the file bytes, not with shell `grep`, per verification rule 1.
[Unknown] Whether any of these escapes is *intended* and settled elsewhere in the
owner's direction record — I was given the contract as the subject and judged it
as a self-contained instrument, which is what a clause that "binds nothing today"
will become.

*End of RD-1b.*
