# Mission safety — closure report, and it does not close

> **Historical record — superseded at round-2026-08d.** This report
> describes the pre-split RFC-0010 single file (digest `7f823aa3…`) and the
> deliberate freeze that kept its findings unrepaired beside the reviews
> bound to them. Round-2026-08d split the contract into a five-module
> package and repaired the findings; the digests quoted here are the values
> of their time and name no current artifact. The repairs await their own
> fresh review — see the acceptance record's wave-history note.

> **Non-authoritative round record.** The raw reviews are
> `reviews/RD-1-mission-safety-confirming-RAW.md`,
> `reviews/RD-1b-mission-safety-confirming-RAW.md` and
> `reviews/RD-1b-mission-safety-RAW.md`, and none of the three is ever edited.
> Where this file and a raw review disagree about what a reviewer found, **the
> raw review wins**. Verdict words are copied, not summarised.

## The answer, first

> **Can a bounded, autonomous Mission cause an unrecoverable or unauthorized
> outcome without an owner act?**

**Yes.**

That is the independent reviewer's word, not a paraphrase:

> **Yes.** A bounded, autonomous Mission conforming to every clause in this
> file can cause an unrecoverable or unauthorized outcome with no owner act, by
> at least three independent routes.

**RFC-0010 Mission safety is not closed, and this report does not call it
closed.** The charter's §6.7 governs: *"if the verdict is `REVISE`,
`EXCEPTIONS`, or `REJECT`, do not call the Mission contract closed."* All three
verdicts are `REVISE`.

## The three reviews, and why there are three

| Review | Subject | Lens | Verdict |
|---|---|---|---|
| **RD-1** | rev11b | Adversarial, independent | **`REVISE`** — three blocking (A, B, C), five exception, five recorded |
| **RD-1b** *(confirming)* | rev11c, sha `7f823aa3…` | Did the three blocking repairs close what they claim? | **`REVISE`** |
| **RD-1b** *(independent)* | rev11c, sha `7f823aa3…` | Fresh adversarial read, eight attack classes, no knowledge of RD-1 | **`REVISE`** |

**The two RD-1b reviews are independent of each other and read the same
bytes.** Both verified the digest before starting. Neither read the other. They
converged on the same structural defect — B1 below and RD1b-A — from opposite
directions, one by re-running a repaired attack one state earlier, the other by
attacking a clause it had never seen critiqued.

**Two independent reviewers reaching the same blocking finding over identical
bytes is the strongest evidence this round produced about anything.**

## What the repairs did close

Recorded first, because the repairs were real and a report that opens with
failures misrepresents the work.

| RD-1 finding | Status at `7f823aa3…` |
|---|---|
| **RD1-A** (blocking) — `paused` unbounded | **Closed for `paused`.** The false sentence — *"An indefinite park is reachable only as an explicit, owner-visible envelope declaration with its own act — never by silence"* — was **removed, not re-argued**. The confirming reviewer re-ran RD-1's executed attack and reports *"The attack no longer runs"* |
| **RD1-B** (blocking) — unfundable compensation | **Closed.** Both of RD-1's alternatives were implemented |
| **RD1-C** (blocking) — the effects-applied predicate had no establisher | **Closed for the two sites it names** |

**And the clean checks matter too.** The independent reviewer verified, by
Python `re` over the file bytes: the front-matter clause list matches the file
exactly — all 22 clauses and all three sub-clauses defined, none missing,
duplicated or extra — and **all 32 distinct foreign clause citations resolve**,
with the load-bearing ones checked for substance against the cited clause text.
For a contract that has been amended four times in two rounds, that is not
nothing.

## The blocking findings, and none is repaired here

### B1 · The reservation is accounting, not enforcement — **the largest**

RFC10-10: *"Mission Control MUST prevent every act it mediates from exceeding
the approved authority and resource envelope."*

RFC10-17: *"reserved + spent never exceeds authorized"*, and any *"**overrun**
(spend exceeding authorized)"* is *"recorded as attributable evidence against
the mission and mints its own Attention Item."*

**The invariant is stated over the ledger. Nothing states it over
consumption.** The reviewer's sequence, which a conforming implementer produces
without any bad faith:

> The owner approves a mission with a monetary budget of $100 and the maximum
> autonomy this contract permits — `propose-only`. The mission dispatches one
> agent run whose *declared maximum cost* is $100, satisfying RFC10-17's
> reservation predicate exactly. The run loops, and the model provider bills
> $5,000. … $4,900 of the owner's money is spent, irrecoverably, outside
> anything the owner authorized, and the contract's response is a ledger entry
> and a notification.

The sub-escape rides the same gap: RFC10-17 correctly forbids the *worker* from
sizing its own reservation, but the **dispatching authority inside a running
mission is itself a mission-controlled component**. Declare $1 per run,
dispatch 100 runs that cost $50 each — every sentence satisfied.
**Under-declaration is detected, never prevented.**

**And RFC10-10 and RFC10-17 cannot both be true as written**: one says MUST
prevent, the other treats overrun as a reachable accounting state with a
bookkeeping remedy.

**Prescribed repair (RD-1b's, recorded verbatim in effect):** admit a dispatch
only where the reserved maximum is bound to an enforced runtime limit at the
launch gate — RFC5-21's enforced resource limits — and to a remaining-headroom
predicate at the RFC5-15 choke point for every provider transmission; make a
cost kind with no enforceable limit **non-delegable**; then reconcile RFC10-10.

### B2 · `reversible` is the effect class with no definition and no duty

RFC10-19 classifies every permitted effect class `reversible`, `compensatable`
or `irreversible`. Trace `reversible` through the terminal-disposition
sentence: the attempted-action limb is scoped to `compensatable`; the
Attention-Item limb is scoped to `irreversible`.

> **No effect classified `reversible` is ever actually reversed by any clause in
> this contract**, and no clause says who would, with what budget, or what
> happens if the reversal fails.

`compensatable` is defined by its structural requirement. `irreversible` is
defined by exclusion. **`reversible` has no predicate at all** — it is whatever
the envelope author asserts, and it is the class an implementer will choose.

The reviewer's attack: an envelope declares database row writes `reversible`
(*"we can delete the row"*); the mission applies 40,000 across a production
store and fails; nothing is attempted, nothing is minted, the rows stand. It
also **defeats RFC10-19's strongest sentence** — *"A compensating action that
fails is not discharged by having been attempted"* — because no attempt is
owed, so nothing can fail, so nothing is reclassified. And it hollows
RFC10-19(a)'s `compensate-all` default into a no-op.

**Prescribed repair:** collapse `reversible` into `compensatable`, or define it
narrowly enough that the absence of a duty is honest — *"reversal performed
automatically and atomically by the mediating surface as part of the same act,
such that no post-hoc action exists to attempt"* — and force everything else to
`compensatable`.

### B3 · Is provider egress an effect? The contract breaks either way

RFC10-18(a) fixes the predicate *"have effects outside `.syzygy/**` and
`openspec/**` been applied under this mission?"* and says it *"decides whether
the correction plane engages at all."* RFC10-7's `propose-only` forbids effects
outside those namespaces, then carves out: *"Egress to a model provider remains
permitted only under an RFC5-14 consent record."*

**The carve-out's grammar forces the reading that egress is such an effect** —
otherwise it would be unnecessary. On that reading egress is irreversible in
the only sense that matters, so an envelope permitting it must declare an
irreversible class on its face — which contradicts `propose-only`'s own grant
that a mission may run agents within its reserved budget. On the other reading,
a `propose-only` mission that has transmitted content to a provider counts as
having applied no effects, and the correction plane never engages.

### B4 · RFC10-5's third park limb, and RFC10-22's undefaulted expiry

The park rule's third fallback — *"where the park minted none it is the
envelope's shortest declared maximum"* — is **ill-typed and may have no
referent**, and the confirming reviewer shows it is reached in exactly the case
the rule exists for. RFC10-22's maximum item expiry has no default.

### B5 · A kill switch that neither succeeds nor reports failure

RFC10-20(d)'s undeclared-latency case has no finite default and no third exit.
Compounding it, **RFC10-20(d) attributes to RFC5-21 a requirement RFC5-21 does
not contain** — found independently by both RD-1b reviews (RD1b-H, N6). The
failure-signal floor needs restating as RFC10-20's own requirement.

### B6 · The D3 precondition lives in §2 prose, not in clause text

A precondition that binds must be a clause. Prose in an introductory section is
not one.

### RD1b-A · The escape moved one state earlier — **and this is why the round stops here**

The confirming reviewer's finding on the RD1-A repair: **a child mission's
grant is debited at *grant* time and released on the child's transition**, so
the bound the repair installed is re-instantiated one state earlier in the
parent/child seam.

**That is the shape of the problem, and it is why no further repair is made in
this pass.** Each repair closes the attack it was written against and the next
reviewer finds the same class one step away. A fourth repair-and-review cycle
inside one round would be the recursive churn the charter explicitly says to
stop, and the ceiling makes it worse: the contract sits at **6,749 of 7,000
words**, with its amendment log and 21 violation cases already moved to Tier 2
to make room. **There is no room left to repair in.** That is a structural
signal, not a formatting inconvenience: the package needs splitting before it
can absorb another correction plane.

### RD1b-B · RFC10-22's queue bound forbids Attention Items that five other clauses mandate

A bound that makes five mandated mints unlawful, with a prescribed remedy that
does not resolve the conflict.

## The findings that stand from RD-1, verbatim

The confirming reviewer re-tested each and reports them **unchanged at this
digest**: RD1-D (the unmediated-surface Unknown keys on the envelope's own
declaration rather than on observed coverage — *"now bites harder"*), RD1-E,
RD1-F (the sibling-disposition default is non-monotonic: **the more dangerous
the effect mix, the weaker the containment**), RD1-G, RD1-H, RD1-J (widened to
both park states), RD1-K, RD1-L, RD1-M.

**RD1-K deserves a sentence of its own** because it is the cheapest item on
this whole page and it is still open: **RFC-0004 is a substantive reliance and
is not in `depends_on`** — a one-token front-matter fix with a real
context-load consequence, found independently by both reviewers. **RFC-0011 is
also absent.** It is not applied here for one reason: **the bytes are frozen at
`7f823aa3…` and two reviews are bound to that digest.** Changing one token
would invalidate both, and a review bound to a digest that no longer exists is
worth nothing. The token costs less than the evidence it would destroy.

Plus RD1b-C through RD1b-N: the missing `paused → expired` edge in RFC10-5's
own state vocabulary; recovery headroom named two ways and representable in
none of RFC10-17's five quantities; a scoping sentence that asserts its
enumeration complete at two sites when there are at least four; RD1-I closed
for `blocked` and reproduced in `paused`; RFC10-19 imposing no duty on
`reversible` (the confirming reviewer's independent arrival at B2); RFC10-17(a)
row 6 contradicting RFC10-12 flatly; two false citations; and a `failed` branch
asserting a duty set that is by construction empty.

## What this round changed, honestly

**Three blocking findings were closed and two were created by the closing.**
The park rule now binds `paused`, and the same escape reappeared at the
parent/child grant seam. The effects-applied predicate now has an establisher
at the two sites RD-1 named, and there are at least four sites.

That is not a failed round. It is what an adversarial review loop looks like
when the underlying contract is genuinely hard, and the alternative — declaring
closure after the repairs and before the confirming review — is the exact move
the charter forbids and this repository has already paid for twice.

**Nothing here is softened.** No verdict is restated as "pass with findings",
no blocking finding is reclassified, and no acceptance waiver is offered over
any of it.

## Disposition, and what the next pass must do

**Mission safety is `[Observed]` open.** It is one of the two unmet
pre-specification criteria, and the readiness report says so.

**Frozen:** RFC-0010 stays at sha256
`7f823aa3773c7bf47fed2f7634aa696c454b3ca62dea691c656a3f58a191f825`. No
further edit in this pass, including the one-token RD1-K fix.

**The next pass, in order:**

1. **Split the RFC-0010 package.** Nothing else on this list fits under the
   ceiling. The word pressure is the symptom; a package holding a prevention
   plane, a correction plane, an attention system and a cross-project consent
   seam in one file is the cause.
2. **B1** — bind reservation to enforced limits at the RFC5-21 launch gate and
   the RFC5-15 egress choke point; make un-enforceable cost kinds
   non-delegable; reconcile RFC10-10.
3. **B2** — collapse or define `reversible`.
4. **B3** — settle whether egress is inside the effects-applied predicate, and
   repair whichever clause the answer breaks.
5. **B4, B5, B6**, then RD1b-A and RD1b-B.
6. **The cheap ones the independent reviewer would take in the same pass:** N1,
   N3, N5 (the `depends_on` fix), N7 (a state diagram that *"will be
   transcribed into an OpenSpec state machine as written"*).
7. **Then a fresh review over the new exact bytes**, by a reviewer who wrote
   none of it. **The repair pass may not be its own confirming reviewer** — the
   rule that produced every finding on this page.

**Owner items unchanged by this report:** P-19 (envelope residuals), P-23
(stage placement — RC-7's `propose-only` V0 recommendation is *strengthened* by
B1 and B2, since a V0 that cannot apply effects is not exposed to either),
P-24/D4, and P-28 (Mission is not an entity RFC-0001 admits).

**One reading of B1 and B2 that the owner should have.** Both are arguments for
capping V0 at `propose-only` and holding the correction plane for V1 — which is
packet 3's option (a). A V0 that can only propose is not exposed to B2 at all,
and is exposed to B1 only through provider spend, which is B3's question and a
narrower one. **The reviews did not set out to argue for a staging decision and
they argue for it anyway**, which is the most useful thing they produced.
