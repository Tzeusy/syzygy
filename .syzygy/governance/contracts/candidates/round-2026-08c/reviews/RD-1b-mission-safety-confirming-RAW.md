# RD-1b — Second confirming review of RFC-0010 Mission safety

**Commissioned:** 2026-08-06, over the exact bytes at commit 0623784, with no authoring rationale.
**Subject digest:** `7f823aa3773c7bf47fed2f7634aa696c454b3ca62dea691c656a3f58a191f825`

# VERDICT
VERDICT: REVISE

---

## 0. Conditions of this review

**[Observed]** Subject file:
`/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/rfcs/RFC-0010-mission-control-autonomy.md`,
781 lines, sha256 as above, computed by me with `sha256sum` at commit
`0623784ca18247437083658bef41cf5fa8db1e4e`.

**[Observed]** `RFC-0010:N` means line N of the subject file at this digest.
Everything else is quoted with its path relative to
`.syzygy/governance/contracts/candidates/`.

**[Observed]** I read, in full: the subject file; then, after forming my own
reading of the clause text, `round-2026-08c/reviews/RD-1-mission-safety-confirming-RAW.md`;
`history/RFC-0010-history.md`; and the cited regions of
`rfcs/RFC-0002/rendering-vocabularies.md` (RFC2-23, RFC2-25),
`rfcs/RFC-0002/reconciliation-chain.md` (RFC2-15, RFC2-19),
`rfcs/RFC-0003/governance-homes-and-owner-acts.md` (RFC3-15, RFC3-16, RFC3-16(c)),
`rfcs/RFC-0004/execution-record.md` (RFC4-18..RFC4-21),
`rfcs/RFC-0005/admission-and-boundary.md` (RFC5-3/5/6, RFC5-25),
`rfcs/RFC-0005/consent-egress-secrets.md` (RFC5-12, RFC5-14, RFC5-15),
`rfcs/RFC-0005/execution-profiles.md` (RFC5-18, RFC5-21, RFC5-22),
`rfcs/RFC-0008/state-vocabulary-and-cost.md` (RFC8-12, RFC8-19),
`rfcs/RFC-0008/accounting-reconciliation-and-release.md` (RFC8-28, RFC8-30),
`rfcs/RFC-0006-cross-surface-selection-query-drawer.md` (RFC6-13, RFC6-14).
I read **nothing** under `round-2026-08c/` other than RD-1 and this file. I did
not read `MISSION-CONTRACT-SEMANTIC-DELTA.md`, any closure report, any
acceptance record, or `PROJECT-STATUS.md`.

**[Observed]** I ran one `git diff aee13d5 0623784` restricted to the subject
file, reading only added/removed **file content**, to answer criterion 4's
"does the contract still state every obligation it did before". I read no commit
message. Everything else in this report is derived from the current bytes.

**[Observed]** All clause-location and term sweeps used Python `re`, never
`grep`, per the repository's ugrep hazard. Counts over the moved violation cases
were computed by script, not read off.

---

## Summary of dispositions

| RD-1 finding | Status at this digest |
|---|---|
| **RD1-A** (blocking) `paused` unbounded | **Closed for `paused`.** Re-instantiated one state earlier — **RD1b-A**, blocking |
| **RD1-B** (blocking) unfundable compensation | **Closed.** Both of RD-1's alternatives were implemented. Accounting residue — **RD1b-E** |
| **RD1-C** (blocking) effects-applied predicate has no establisher at RFC10-19/RFC10-20(c) | **Closed for those two sites.** Two further sites unnamed — **RD1b-G** |
| **RD1-D** unmediated-surface Unknown keys on declaration | **Stands, verbatim, and now bites harder** |
| **RD1-E** "all four of completion's requirements" drops approval-time naming | **Stands, verbatim** |
| **RD1-F** RFC10-19(a) default non-monotonic | **Stands, verbatim** |
| **RD1-G** stop reaches only Syzygy-launched runs | **Stands, verbatim** |
| **RD1-H** hung kill switch at the undeclared-latency default | **Stands, verbatim**, plus a false citation in the same limb — **RD1b-H** |
| **RD1-I** no row for `blocked` with applied effects | **Closed.** Reproduced in `paused` — **RD1b-F** |
| **RD1-J** RFC10-8 block self-clearing by silence | **Stands, and widened** to both park states |
| **RD1-K** RFC 0004 not in `depends_on` | **Stands.** RFC-0011 is also absent |
| **RD1-L** "full retention horizon" undefined | **Stands** (1 occurrence of `retention` in the file) |
| **RD1-M** RFC10-5 ↔ RFC10-12 expiry enumeration | **Stands, and the second half is stronger than RD-1 said** — **RD1b-J** |

New at this digest: **RD1b-A** and **RD1b-B** blocking; **RD1b-C** through
**RD1b-L** exception-grade; **RD1b-M**, **RD1b-N** recorded.

---

# Criterion 1 — Did the three blocking repairs close what they claim?

## 1.1 RD1-A — the park rule. **Closed for `paused`. Not closed for every route.**

### What the repair does, and it does it correctly

`RFC-0010:147-153`:

> **No park is indefinite — `blocked` or `paused`, whatever gave rise to it.**
> Every non-terminal park carries a **maximum park duration**, declared by the
> envelope; where none is declared the maximum is the expiry of the Attention
> Item that park minted (RFC10-12), and where the park minted none it is the
> envelope's shortest declared maximum. Silence buys no unbounded park in any
> direction. At the maximum the mission transitions to **`expired`**, a terminal
> state whose reason is recorded.

`RFC-0010:431` adds `paused` to the held row:

> \| `blocked` or `paused`, no applied effects \| **held**, for no longer than
> RFC10-5's maximum park duration; released at the resulting transition to
> `expired` \|

and `RFC-0010:437-438` narrows the general sentence honestly:

> **No non-terminal park holds a reservation indefinitely** — in either park
> state.

**[Observed]** The sentence RD-1 correctly called false —
"An indefinite park is reachable only as an explicit, owner-visible envelope
declaration with its own act — never by silence" — is **removed**, not
re-argued. I confirmed by diff that no equivalent survives. That is the right
way to answer a finding of that shape.

**[Observed]** I re-ran RD-1's executed attack against the current text. Mission
pauses under RFC10-22:665-667; `RFC-0010:147` now reaches `paused`;
`RFC-0010:431` now has a `paused` row; the park expires to `expired`;
`RFC-0010:430` (`expired` → "as `failed`") releases the reservation after
RFC10-19's actions. **The attack no longer runs.** RD1-A is closed for the state
it was written about.

### FINDING RD1b-A [Observed, blocking] — the escape moved one state earlier: a child mission's grant is debited at *grant* time and released only at *mission* states, so a child that never starts holds its parent's budget forever

The park rule is scoped, by its own words, to two states — `RFC-0010:147`,
"`blocked` or `paused`" — and RFC10-17(a)'s table is keyed on states a mission
*reaches*. Neither reaches the pre-running states. That would be harmless if
nothing were held there. Something is.

`RFC-0010:259-262` (RFC10-8):

> Every child grant is **debited from the parent's remaining envelope at grant
> time**: the parent's own spend plus the sum of outstanding child grants never
> exceeds any parent budget, so sibling children can never jointly exceed what
> the one owner act authorized.

`RFC-0010:419-423` (RFC10-17(a)) claims to cover exactly this:

> **RFC10-17(a). Every reservation has a stated release point.** Reserved budget
> is *released* — returned to the envelope's available headroom, **and for a
> child mission to the parent's remaining envelope (RFC10-8)** — at the points
> below

and the points below are `RFC-0010:427-434`, eight rows keyed on `completed`,
`failed`, `cancelled`, `expired`, `blocked`-or-`paused`, and an unrecoverable
stop. **No row is keyed on `draft`, `awaiting-approval` or `approved`** —
`RFC-0010:131`'s first three states.

**The executed attack.**

> A mission is approved with an explicit decomposition grant (`RFC-0010:253-256`
> permits children only with one). Its planner mints three child missions and
> grants each a share of the remaining envelope. Each child is debited at grant
> time (`:259-260`). The children stay in `draft`. Nothing dispatches, so
> RFC10-17's dispatch-time reservation rule (`:396-397`) never fires and no
> RFC10-11 bound is reached. The children are in no park, so `:147` does not
> reach them and `:431` has no row for them. RFC10-20's transitive stop
> (`:608-613`) fires only on "A human stop, cancellation, or expiry of a
> mission" — no act has occurred. **The parent's budget is consumed and no
> clause releases it.**

**[Observed]** This is RD-1's own finding text, one state earlier: "For a child
mission, the parent's headroom is consumed permanently … the parent can never
grant that budget again." RD-1 marked `draft` "no — reservation is made 'at
dispatch'" and `approved` **[Unknown]**. Both are wrong on the current text,
because RFC10-8 debits at **grant** time, not dispatch time, and RFC10-17(a)
names child-mission budget as within its own scope.

**[Observed]** The defect is in the repaired sub-clause's own claim. Its title
is "Every reservation has a stated release point"; for a reservation it names
by hand in its opening sentence, it states none.

**[Inferred]** Two adequate fixes exist and either would close it: bound the
pre-running states the way parks are bounded (a maximum time to first dispatch,
expiring to `expired`), or state that a child grant is released to the parent's
remaining envelope when the child reaches any terminal state **or when the
parent does**. Neither is present.

**[Observed]** Also unstated: what happens to an outstanding child grant when
the **parent** terminates. `RFC-0010:427` releases the parent's reservation "in
full at the terminal record", and `:421` says a child releases "to the parent's
remaining envelope" — an envelope that no longer has a running mission. The
contract does not say.

### FINDING RD1b-C [Observed, exception] — RFC10-5's own state vocabulary has no `paused → expired` edge, which the repaired paragraph in the same clause requires

`RFC-0010:130-135`:

```text
draft → awaiting-approval → approved → running
running ⇄ paused
running → blocked (→ running on unblock, or → expired on park expiry)
running → completed | failed | cancelled | expired
```

The block was amended for `blocked` — the parenthetical "or → expired on park
expiry" is on the `blocked` line — and **not** for `paused`. The only edge out
of `paused` in the vocabulary is back to `running`. Fifteen lines later,
`RFC-0010:147-153` transitions `paused` to `expired`, and `RFC-0010:431`
accounts for that transition.

**[Observed]** The clause anticipates the objection at `:137-139` ("This list is
**provisional** … not frozen until its interaction with Trajectory's normalized
work states (RFC 0008) is reviewed"), and `:140-141` enumerates "What *is* fixed
now". So the prose governs. But the vocabulary block is the **only** enumeration
of the state set, and RFC10-17(a)'s table is keyed on it. A repair that amended
the prose and left the diagram stating a narrower transition set is the same
defect class as RD1-I — a repaired rule whose companion enumeration was not
brought along.

**[Observed]** The block also lacks `paused → failed` and `paused → cancelled`,
both of which RFC10-20(d) (`:626-627`, "the mission enters `failed`") and
RFC10-5's own `:140-141` ("`expired` and `cancelled` are always reachable by human
act") require.

### FINDING RD1b-D [Observed, exception] — the park rule's third fallback limb is ill-typed and may have no referent, and it is reached in exactly the case RD1b-B constructs

`RFC-0010:148-151`:

> declared by the envelope; where none is declared the maximum is the expiry of
> the Attention Item that park minted (RFC10-12), **and where the park minted
> none it is the envelope's shortest declared maximum.**

Three problems, in order of severity.

1. **"Maximum" of what?** The envelope's declared maxima are not a homogeneous
   set. `RFC-0010:622-623` declares a "**maximum stop latency**" (a duration);
   `RFC-0010:663-664` declares a "**maximum outstanding attention count**" (a
   count) and a "**maximum item rate**" (a rate); `RFC-0010:680-681` declares a
   maximum item expiry (a duration). "The envelope's shortest declared maximum"
   ranges over durations, counts and rates alike. A count has no ordering
   against a duration.
2. **The set may be empty.** RFC10-7's envelope enumeration (`:194-216`) makes
   none of these mandatory. Where the envelope declares no maximum of any kind
   and the park minted no item, the limb has no referent and the park is
   unbounded — the exact condition `:151` asserts is impossible ("Silence buys
   no unbounded park in any direction").
3. **It is not a rare limb.** Every ordinary park mints an item — RFC10-8
   (`:264-265`), RFC10-11 (`:315-316`), RFC10-18 (`:471`), RFC10-22's exempt
   class (`:669-671`). So limb 3 is reached **precisely when a mandated item
   could not be minted**, which is RD1b-B's scenario below. The two defects
   interlock: the queue bound suppresses the item, and the missing item drops
   the park onto the limb that does not type-check.

**[Inferred]** RFC10-7's ambiguity rule (`:210-213`, "genuine ambiguity in a
load-bearing bound is an escalation trigger (RFC10-13), never a call the running
agent adjudicates for itself") arguably saves case 2 — the escalation mints an
item, which supplies limb 2. That is a circular-but-terminating rescue that the
text does not state, and it depends on an item being mintable, which is what
RD1b-B puts in doubt.

## 1.2 RD1-B — the recovery-headroom rule. **Closed. The rule itself is under-specified.**

RD-1 offered two alternatives ("Either require recovery headroom to be carved
out … **or** state expressly that an unfundable compensating action is an
escalation"). **Both were implemented.**

`RFC-0010:439-442`:

> **Recovery headroom is carved out of `authorized` at approval time and held
> undispatchable**, so that RFC10-19's compensating actions are fundable after
> an RFC10-11 exhaustion; a budget with no declared recovery headroom authorizes
> no effect class that requires compensation.

`RFC-0010:549-556`:

> **A compensating action that cannot be funded is an escalation, not a
> silence.** Where the reserved recovery headroom (RFC10-17(a)) is insufficient
> to run a compensating action, the mission does not simply omit it: the
> shortfall is an escalation trigger under RFC10-13, every uncompensated effect
> joins the single Attention Item naming what cannot be undone, and the terminal
> reason states it as uncompensated-for-want-of-budget. **This clause imposes no
> duty RFC10-11 can quietly make impossible** — an exhausted bound bounds
> further *work*, never the accounting of what that work already did.

**[Observed] Is the rule well-formed?** For the question RD-1 asked — a
mandatory duty with no stated outcome when it cannot be discharged — yes. The
second paragraph converts an unfundable compensation from an unstated outcome
into a recorded, escalated, per-effect one, and its last sentence draws the
right line between bounding work and bounding accounting. **RD1-B is closed.**

**[Observed] The commissioned sub-question: a mission whose envelope declares no
recovery headroom and permits a compensatable effect class.** `:441-442` answers
it: that budget "authorizes no effect class that requires compensation". The
class is therefore unauthorized, and an attempt to produce such an effect is
out-of-envelope and refused at RFC10-10's choke point (`:300-302`). The answer
is stated and it fails closed. Two residues, both in RD1b-E.

### FINDING RD1b-E [Observed, exception] — recovery headroom has no representation among RFC10-17's five quantities, the two clauses call it two incompatible things, and "at approval time" has no referent for a derived child mission

`RFC-0010:391-398` (RFC10-17):

> Every budget in an envelope is accounted in five distinct quantities:
> **authorized** (the owner act's figure), **reserved** (committed at dispatch to
> work not yet complete), **spent** (measured consumption), **released**
> (reserved-but-unspent, returned on completion or termination), and **overrun**
> (spend exceeding authorized). … reserved + spent never exceeds authorized

Three specific breaks against `:439-442` and `:550`.

**(a) The invariant does not protect the carve-out.** Recovery headroom is
"carved out of `authorized`", but `authorized` is defined as a single figure —
"the owner act's figure" — and the only stated invariant is `reserved + spent ≤
authorized`. Nothing states `reserved + spent + recovery-headroom ≤ authorized`,
and there is no sixth quantity naming the carve-out. A runtime conforming to
RFC10-17's invariant alone dispatches into the headroom.

**(b) RFC10-11's "any envelope bound" is undefined against the carve-out.**
`RFC-0010:313-314`: "Reaching any envelope bound (budget, time, retries, risk
floor) halts further materialization". Is the budget bound `authorized`, or
`authorized` minus headroom? On the first reading, work spends the headroom and
the carve-out is defeated. On the second, the carve-out holds. The contract does
not say. RFC10-7's obligation limb (`:218-221`) gets a reader to the second
reading by inference; the text states neither.

**(c) The two clauses name it incompatibly.** `:550` calls it "the **reserved**
recovery headroom". `:439-440` says it is "**held undispatchable**". `:393`
defines `reserved` as "committed **at dispatch** to work not yet complete" —
which headroom, by construction, is not. So RFC10-19 cites a quantity under a
name RFC10-17's own definition excludes.

**(d) "At approval time" has no referent for a derived child.** `RFC-0010:256-258`:
"A derived child's authorizing provenance is the **parent's owner act plus a
recorded derivation** — never a new self-minted act". A child mission has no
approval act of its own, so the moment `:439` names does not occur for it.
**[Inferred]** The consequence fails safe rather than open — a child with no
declared headroom authorizes no compensatable effect class under `:441-442` —
but the rule that makes RD1-B's repair work has no defined application to the
mission class RFC10-8 exists to govern.

**(e) Overrun still reaches the headroom.** `:393-394` makes `overrun` a
first-class quantity ("spend exceeding authorized"), so measured spend can
exceed `authorized` and *a fortiori* consume the carve-out. When it does, the
mission lands in `:549-556`'s escalation — recorded, not silent, which is why
this is exception-grade and not blocking. But the carve-out is protected against
*dispatch* only, never against *spend*, and the clause does not say so.

## 1.3 RD1-C — the effects-applied scoping sentence. **Closed for the two sites it names. It names two and there are at least four.**

`RFC-0010:486-494`:

> **RFC10-18(a). Whether effects were applied is established, not asserted.**
> One predicate — *have effects outside `.syzygy/**` and `openspec/**` been
> applied under this mission?* — decides whether the correction plane engages at
> all. **This sub-clause governs that predicate wherever it appears**, not only
> in the branch above: RFC10-19's `with effects already applied` trigger and
> RFC10-20(c)'s `any effect already applied` are the same determination and are
> subject to every rule below, including the fail-closed Unknown rule. A
> predicate that has an establisher in one clause and none in **the two clauses**
> that carry its duties is not established.

**[Observed] Does it reach both?** Yes, and the two trigger phrases it quotes
are verbatim accurate:

- RFC10-19's trigger, `RFC-0010:536`: "Where a mission enters `failed`,
  `cancelled`, or `expired` **with effects already applied**". ✅
- RFC10-20(c), `RFC-0010:617-618`: "**any effect already applied** is classified
  and dispositioned under RFC10-19". ✅

RD-1's executed scenario — a mission with a valid establisher that never enters
RFC10-18's no-establisher branch, self-asserts "no effects", and exits the
correction plane at RFC10-19 — **no longer runs**, because RFC10-19's trigger is
now governed. RD1-C is closed for the sites named.

### FINDING RD1b-G [Observed, exception] — the scoping sentence enumerates its own scope, asserts the enumeration is complete ("the two clauses"), and misses at least two further sites

The sentence opens general ("wherever it appears") and then enumerates, and then
counts. "**The two clauses** that carry its duties" is a claim, and it is false
of the current text. The predicate appears in at least two further places, both
carrying duties, neither named:

1. **RFC10-19(a)'s trigger**, `RFC-0010:570-571`: "Where one run or child
   mission fails **after applying effects** while its siblings completed or
   remain active". This is the gate on the entire sibling-disposition clause.
   Assert "no effects applied" and RFC10-19(a) never engages: active siblings
   continue, completed siblings stand, and the strict `compensate-all` default
   at `:587-592` is never reached. The party that benefits from that answer is
   the mission machinery whose siblings they are.
2. **RFC10-17(a)'s table rows**, `RFC-0010:431` ("`blocked` or `paused`, **no
   applied effects**") and `:433` ("`blocked` **with** applied effects"). The row
   selection is a reservation-disposition decision keyed on the same predicate.

**[Observed]** RD-1 applied exactly this reading discipline to the previous
revision — "the authors *did* write the incorporating phrase where they meant
it … the omission is meaningful" — and rated it blocking. The same discipline
applied here says the enumeration is what binds and the enumeration is short by
two. I rate it exception rather than blocking because the two largest sites are
now covered and because site 2's two rows converge on the same park bound, so
misselecting between them changes little. Site 1 is a real residue of RD1-C.

### The rest of RFC10-18(a) — what I could and could not break

**[Observed] Tier limb — holds.** `:507-509`: "`gate-backed` (RFC2-25). A
`report-fact` assertion by the executor is admissible as evidence and is never
the determination." I confirmed against
`rfcs/RFC-0002/rendering-vocabularies.md:155` that `gate-backed` is "The
**only** tier that may support a positive status claim". Tier-shopping is closed
by name.

**[Observed] Unknown limb — holds, and it is the best sentence in the file.**
`:518-521`: "**Unknown fails closed: where whether effects were applied is
Unknown, effects are treated as applied**". I tried four routes to a negative
and found none.

**[Observed] Transitive independence — holds.** `:453` ("at *any* depth") plus
`:500-502` ("of the executing principal and of every principal it routed").

**[Observed] RD1-D stands verbatim.** `:512-516` is unchanged: the Unknown fires
"where the envelope names any such surface", i.e. on the escaping party's own
declaration, not on evidence coverage. `unmediated` occurs exactly twice in the
file (Python `re`, lines 512 and 514), both inside RFC10-18(a); the field is
still absent from RFC10-7's enumeration at `:194-216`. **And it now bites
harder than when RD-1 wrote it:** because `:488-491` makes RFC10-18(a) the
governing rule for RFC10-19 and RFC10-20(c), the declaration-keyed Unknown is
now the *single* gate on the whole correction plane rather than one of two
routes in. Closing RD1-C raised RD1-D's severity.

**[Observed] RD1-E stands verbatim.** `:496-497` still claims "this one carries
all four of completion's requirements", and the Evaluator bullet at `:499-502`
still omits RFC10-18's third requirement — approval-time naming (`:453-455`).
See also RD1b-I, which is the same seam from the other side.

---

# Criterion 2 — Did the repairs introduce new defects?

They did. Three of the four I was asked to check specifically came back
positive, plus two I found elsewhere.

## 2.1 RFC10-5's park rule × RFC10-8 self-widening blocks

### RD1-J stands, and the repair widened it

`RFC-0010:163-166`:

> Expiry from a park is a **termination, never a resolution**: it widens nothing
> (RFC10-12), does not substitute for the human resolution act where the
> paragraph above owes one, and does not mark the condition cleared. It ends the
> mission and fires RFC10-19's duties.

against `RFC-0010:143-145`:

> exit from `blocked` where the block arose under RFC10-8 or RFC10-11 is a
> **human resolution act** — an agent's "condition cleared" assertion never takes
> that transition.

**[Observed]** RD-1's objection is unanswered and the answer offered does not
reach it: a mission that ends has no owed act left to owe. The sequence with
zero human involvement is unchanged — agent attempts to widen → `blocked` +
item → item expires to a safe default (RFC10-12, `:331-333`) → park maximum
(defaulted to that same expiry, `:149-150`) elapses → `expired`, reason recorded
as park expiry → `RFC-0010:430` releases the reservation in full to the parent.
The enforcement response to what `:245` calls "the load-bearing rule" remains
clearable by waiting.

**[Observed]** The repair **widened** this: `:147` now covers `paused` too, so
the same self-clearing route is available from either park state.

### FINDING RD1b-B [Observed, blocking] — RFC10-22's queue bound forbids Attention Items that five other clauses mandate, and its prescribed remedy is unavailable at a terminal transition

`RFC-0010:663-667` (RFC10-22):

> Every envelope declares a **maximum outstanding attention count** and a
> **maximum item rate** for the missions under it; an undeclared maximum means
> one outstanding item — the narrowest reading (RFC10-7). **On reaching either
> bound the mission pauses rather than enqueueing further items**

`RFC-0010:669-675`:

> **Exactly one class of item is exempt from both bounds: the item reporting
> that a bound was reached, or the resulting state change.** … it is
> deduplicated like any other, and it is the **only** exempt class; **a second
> one returns the queue to unbounded.**

The last clause forecloses the charitable reading. Now list the items other
clauses **mandate**, none of which is "the item reporting that a bound was
reached":

| Clause | Mandated item | Line |
|---|---|---|
| RFC10-8 | self-widening attempt → `blocked`, "an Attention Item is minted" | `:264-265` |
| RFC10-18 | no-effects branch → "`blocked` **with an Attention Item**" | `:471` |
| RFC10-18(a) | Unknown fail-closed → "the Attention Item states that the disposition rests on an unresolved determination" | `:521-523` |
| RFC10-19 | "every irreversible effect is enumerated in **a single Attention Item** naming what cannot be undone" | `:538-540` |
| RFC10-20(d) | "**an Attention Item enumerates each run that did not terminate** and each effect surface it may still reach" | `:628-630` |

**Two independent breaks.**

**(a) The remedy is unavailable.** RFC10-19's item is minted at `failed`,
`cancelled` or `expired`; RFC10-20(d)'s at `failed`. RFC10-22's stated response
to reaching the bound is that "the mission pauses". **A mission entering a
terminal state cannot pause.** The contract states no outcome for the collision
— which is precisely the defect shape RD-1 rated blocking as RD1-B ("mandatory
and impossible; what happens is **not stated anywhere in the contract**"),
relocated from the budget plane to the attention plane.

**(b) The suppression is agent-triggerable against the load-bearing rule.** The
default outstanding maximum is **one** (`:665`). Items are minted by the
mission. So:

> An agent mints one ordinary Attention Item, filling the queue. It then
> attempts to widen its envelope. RFC10-8 (`:263-265`) requires the mission to
> block **and an Attention Item to be minted**. RFC10-22 (`:665-667`) forbids
> enqueueing it and prescribes `paused` instead — a different state from the one
> RFC10-8 prescribes. The exempt class does not cover it: a self-widening
> attempt is not "a bound was reached", and `:673-675` forbids reading a second
> exemption into the clause.

Two clauses prescribe incompatible responses to the same event, and the event is
the enforcement of the rule the contract calls load-bearing.

**[Observed] Mitigations, stated so the owner can weigh them.** The widening
itself still fails — RFC10-8's prevention limb is untouched, and "the attempt is
recorded as evidence" (`:264`) independently of the item, so the fact remains
queryable. Items carry bounded expiry (`:679-681`), so a slot eventually frees
and the duty is deferred rather than destroyed. RFC10-13 (`:342-345`) requires
that items "never silently disappear". **[Inferred]** A conforming
implementation would probably hold and mint later — but no clause states a
deferral rule, and `:666` says "pauses rather than enqueueing", not "holds and
mints when a slot frees".

**[Observed] It interlocks with RD1b-D.** Suppressing the mandated item is
exactly the condition under which "the park minted none" (`:150`) is true, which
drops the park bound onto the fallback limb that does not type-check. The two
findings compose into an unbounded park reached without any envelope declaration
— the condition `:151` asserts is unreachable.

**[Observed]** RFC10-22's own closing sentence names this class:
`:681-683` — "without both, denial of owner attention is reachable without
widening anything."

## 2.2 Does the recovery-headroom rule create an accounting inconsistency with RFC10-17's five quantities?

**Yes — RD1b-E above, five distinct breaks.** The answer to the commissioned
question is that the carve-out is stated in prose and has no representation in
the accounting the clause it amends defines.

## 2.3 Does RFC10-18(a)'s widened scope contradict RFC10-19 or RFC10-20?

**[Observed] Not a contradiction — a silent narrowing, in a direction that
matters under the operative cap.** RFC10-18(a)'s predicate is namespace-scoped
(`:487-488`: "*have effects **outside** `.syzygy/**` and `openspec/**` been
applied*"). RFC10-19 and RFC10-20(c) previously spoke of effects unqualified.
Now that `:488-491` makes RFC10-18(a) govern them, both clauses' triggers are
narrowed to out-of-namespace effects. Consequences:

- RFC10-19's duty that "the mission's terminal reason (RFC10-5) states the
  reversibility disposition of **every applied effect**" (`:540-541`) no longer
  reaches in-namespace effects.
- RFC10-20(c)'s "any effect already applied is classified and dispositioned"
  (`:617-618`) likewise.

**[Inferred]** That is probably the intent — drafts in the two governed
namespaces render unadopted (`:232-233`) and are not the effects a correction
plane exists for. But the narrowing was effected by a sentence whose stated
purpose was to *widen* 18(a)'s reach, and neither RFC10-19 nor RFC10-20 says its
trigger has been narrowed. See criterion 6 for why this matters more than it
looks.

**[Observed] One timing tension.** `RFC-0010:601-602`: "A human stop,
cancellation, or expiry of a mission (RFC10-5) has three effects, **all
immediate at the act**". Limb (c) now requires an RFC10-18(a) determination —
independent evaluator, `gate-backed` evidence including "each run's execution
record (RFC4-18..RFC4-21)" (`:504`). For the runs limb (b) failed to terminate,
those execution records do not yet exist, so (c) cannot be established at the
act. RFC10-20(d) routes that case to `failed`, so it does not go unhandled, but
"all immediate at the act" now over-claims for (c). Recorded.

## 2.4 FINDING RD1b-F [Observed, exception] — RD1-I was closed for `blocked` and reproduced in `paused`

The new row, `RFC-0010:433`:

> \| `blocked` **with** applied effects \| as above, and RFC10-19's duties fire
> at the expiry, not at the park \|

closes RD1-I. But `paused` **with** applied effects now matches no row: `:431`
is qualified "no applied effects", `:433` is `blocked`-only, and `:432` addresses
only the non-event of item expiry. A Python `re` sweep confirms `paused` occurs
at `:431` and `:432` and **not** at `:433`.

The combination is trivially reachable and is the one RFC10-22 **mandates**:
RFC10-11 (`:315`, "transition to `paused` or `blocked`") and RFC10-22 (`:666`,
"the mission pauses") both put an effect-bearing mission into `paused`.

**[Observed]** The disposition is recoverable by inference — `:437-438` covers
"either park state", the park expires to `expired`, and `:430` disposes of that
— so this is a completeness gap in a table presented as the authority on "Every
reservation has a stated release point", not an indefinite hold. **[Inferred]**
Its significance is the pattern: this is the second consecutive round in which a
repair fixed the `blocked` case and left the `paused` sibling. RD1-A was the
first.

## 2.5 FINDING RD1b-K [Observed, exception] — RFC10-19 imposes no duty at all on `reversible` effects, and the recovery-headroom precondition does not reach them

`RFC-0010:529-532`:

> Every effect class an envelope permits is declared **reversible**,
> **compensatable** (with the compensating action named), or **irreversible**.

`RFC-0010:536-541` — the duties on termination:

> every **compensatable** effect's compensating action is attempted and its
> outcome recorded as evidence; every **irreversible** effect is enumerated in a
> single Attention Item naming what cannot be undone; and the mission's terminal
> reason (RFC10-5) states the reversibility disposition of every applied effect.

**`reversible` gets neither limb.** No reversal is required; no Attention Item is
minted. Only the terminal reason mentions it. And the new precondition at
`:441-442` binds only "effect class that **requires compensation**" — a
`reversible` class does not, so an envelope declaring every class `reversible`
needs no recovery headroom, incurs no undo duty, and mints no item.

**Nothing tests the declaration.** The reclassification mechanism at `:558-560`
("A compensating action that fails … The effect is **reclassified as
irreversible for this mission**") fires only on a failed *compensating action*,
which only `compensatable` classes have. A `reversible` declaration that turns
out to be false has no path to correction, and no run-time check ever asks
whether the reversal happened.

**[Inferred]** The natural fix is one clause: a `reversible` effect's reversal is
attempted on termination on the same terms as a compensating action, and a
reversal that fails reclassifies to irreversible. That would make the three-way
partition carry three duties instead of two.

---

# Criterion 3 — Citation truth

I enumerated every clause-identifier occurrence in the ten amended clauses by
Python `re` (`RFC ?\d{4}|RFC\d+-\d+(\(\w\))?|VIS-\d|SEC-\d|SDR-\d+`) and checked
each against its target's text.

## 3.1 Verified true

| Citing | Claim | Target text |
|---|---|---|
| RFC10-5 `:150` | item expiry (RFC10-12) | `:331-333` "the **default and expiry if ignored**" ✅ |
| RFC10-5 `:156` | "RFC10-11's `paused`-or-`blocked` disjunction" | `:315-316` "transition to `paused` or `blocked`" ✅ |
| RFC10-5 `:156` | "RFC10-22's pause-on-attention-bound" | `:666` "the mission pauses" ✅ |
| RFC10-5 `:158` | "RFC10-17 releases a reservation only on completion or termination" | `:393-394` "**released** … returned on completion or termination" ✅ |
| RFC10-5 `:166` | expiry "fires RFC10-19's duties" | `:536` "Where a mission enters `failed`, `cancelled`, or `expired`" ✅ |
| RFC10-17 `:398` | "the sibling-sum invariant RFC10-8 states" | `:259-262` ✅ |
| RFC10-17 `:401` | Unknown spend (RFC8-19, RFC2-23) | `RFC-0008/state-vocabulary-and-cost.md:245` "**Absent means Unknown, never zero**"; `RFC-0002/rendering-vocabularies.md:70-78` ✅ |
| RFC10-17 `:409-410` | execution / adapter records | `RFC-0004/execution-record.md:65,128` ✅; narrowing of RFC4-21's "runtime-reported", not contradiction |
| RFC10-17(a) `:434` | "RFC10-20 limb (b) not achieved" | `:630` "each such run's reservation is retained and named under RFC10-17(a)" ✅ bidirectional |
| RFC10-18 `:449` | `gate-backed` (RFC2-25) | `RFC-0002/rendering-vocabularies.md:155` — the only positive-claim tier ✅, so `:482-484`'s default is genuinely RFC10-6's "strongest applicable tier"; **no contradiction between RFC10-6 and RFC10-18** |
| RFC10-18 `:461` | "wherever RFC2-19 leaves reconciliation uncomputed" | `RFC-0002/reconciliation-chain.md:205-212` "**V0 renders the absence honestly** … **V1 computes**" ✅ |
| RFC10-18 `:466-468` | "RFC10-19 states that `blocked` discharges none of them" | `:541-543` "transitioning to `paused` or `blocked` discharges no obligation" ✅ |
| RFC10-18 `:474-476` | "RFC10-5's human-resolution rule is scoped to blocks arising under RFC10-8 or RFC10-11" | `:143-145` ✅ — **the RC11-A repair, correct, and it names its own prior error** |
| RFC10-18(a) `:490` | RFC10-19's "with effects already applied" trigger | `:536` verbatim ✅ |
| RFC10-18(a) `:491` | RFC10-20(c)'s "any effect already applied" | `:617-618` verbatim ✅ |
| RFC10-18(a) `:513` | "the boundary RFC10-10 draws for enforcement and RFC10-20 for stop" | `:302-306`, `:618-620` ✅ |
| RFC10-19 `:536` | destructive class not inherited (RFC5-22) | `RFC-0005/execution-profiles.md:162-171` ✅ narrowing |
| RFC10-19 `:545-546` | resumption re-verifies RFC10-4 / RFC10-17 / RFC10-9 | all three exist and say it ✅ |
| RFC10-19(a) `:587` | "RFC10-7's obligation limb" | `:218-227` ✅ |
| RFC10-20 `:605` | "the kill switch RFC5-21 requires of every isolation class" | `RFC-0005/execution-profiles.md:148-149` "a kill switch terminating the run **and its descendants**" ✅ exact |
| RFC10-21 `:638` | "at the RFC5-15 choke point" | `RFC-0005/consent-egress-secrets.md:153-155` ✅ |
| RFC10-21 `:650` | "exactly as an undeterminable content class does (RFC5-14)" | `RFC-0005/consent-egress-secrets.md:157-159` "undeterminable fails closed" ✅ |
| RFC10-21 `:655` | per-project budgets in the store's writ (RFC10-15) | `:366-368` ✅ |
| RFC10-22 `:665`, `:681` | RFC10-7 narrowest reading; RFC10-13 anti-streaming | `:207-209`; `:340-342` ✅ |

## 3.2 FINDING RD1b-H [Observed, exception] — RFC10-20(d) attributes to RFC5-21 a requirement RFC5-21 does not contain

`RFC-0010:631-633`:

> An isolation class whose kill switch **has no failure signal has not satisfied
> RFC5-21** and is not one a mission may run under: a stop with no failure path
> is an unbounded latency under a different name.

RFC5-21's floor, `rfcs/RFC-0005/execution-profiles.md:144-149`, in full:

> Every class must certify the same floor: no ambient credential access, **no
> channel to Syzygy's own control plane** (RFC5-20's network-policy exclusion,
> enforced by the isolation mechanism and not merely declared), filesystem
> confinement to the declared scope, enforced network policy, enforced resource
> limits, and **a kill switch terminating the run and its descendants**.

**There is no failure-signal requirement, and no reporting requirement of any
kind, in RFC5-21.** I read the clause in full (`execution-profiles.md:141-160`); the only reporting
it imposes is that a *policy violation* is recorded on the Execution record
(`execution-profiles.md:151-152`). RFC10-20(d) states a satisfaction condition for another contract's
clause that the clause does not carry.

**[Observed]** This is the same defect class RC-11 found (RC11-A: a citing
clause representing its source as saying something its source's scope does not
contain) and which `RFC-0010:475-476` names in terms as a prior error. It is
back, in a clause amended in the same pass.

**[Inferred]** The substance is defensible — a kill switch that cannot report
failure arguably cannot "certify" termination — but that is an argument RFC10-20
must make in its own voice, or a semantic delta against RFC5-21, not an
attribution. RD-1 observed that RFC5-21 "imposes no timeout on the kill switch
itself" (its RD1-H) without naming the attribution as false; it is.

## 3.3 FINDING RD1b-I [Observed, exception] — RFC10-18 cites RFC10-9 for approval-time naming of the establisher; RFC10-9 says nothing about what an envelope contains

`RFC-0010:453-456`:

> a principal routed by the executing principal at *any* depth is not
> independent, and **the establisher is named in the envelope at approval time
> (RFC10-9)**, so independence is a property of the approved envelope rather than
> a runtime selection.

RFC10-9 (`:268-283`) is entirely about act provenance: "The envelope (and every
amendment to it) is an **authorization-bearing governance artifact** under
RFC3-16(a): it is honored only with **verifiable** owner-act provenance." It says
nothing about envelope *contents*.

The clause that enumerates envelope contents is RFC10-7 (`:194-216`), and its
minimum list does not include a completion establisher. The nearest field is
"**required gates and independent reviews**" (`:204`), which is a plausible
home but is not named by RFC10-18 and does not obviously denote an adjudicator
of the completion predicate.

**[Observed]** The consequence fails closed, not open: absent a named
establisher, RFC10-18's own rule at `:460-462` applies — "Where no independent
establisher exists for a mission's objective class … the mission **never reaches
`completed`**." So this is a citation defect and a missing envelope field, not
an escape. It is nonetheless the pair to RD1-E: RFC10-18 asserts an
approval-time-naming requirement resting on a clause that does not carry it,
and RFC10-18(a) then drops that requirement while claiming to have imported it.
Neither clause has it on solid ground.

## 3.4 FINDING RD1b-J [Observed, exception] — RFC10-17(a)'s row 6 contradicts RFC10-12 flatly, not only at the default

`RFC-0010:432`:

> \| `blocked` or `paused` after its Attention Item expires \| the item's expiry
> releases nothing — **an item's expiry resolves the item, not the mission's
> state.** The park duration is what ends the hold \|

`RFC-0010:331-333` (RFC10-12):

> the **default and expiry if ignored** — an expiry default must be safe:
> **expiry may narrow, pause, or block**, and may never widen an envelope or
> approve anything

`pause` and `block` **are** mission states (`:131-133`). RFC10-12 expressly
permits an item's expiry to change the mission's state; RFC10-17(a) asserts, as
a general proposition and without qualification, that it does not. This is
sharper than RD-1's RD1-M, which framed the row as asserting "a separation that,
**at the default**, does not exist". The contradiction does not depend on the
default: it holds for any envelope whose item expiry default is `pause` or
`block`, which RFC10-12 encourages.

**[Observed] RD1-M's first half also stands.** `:150` makes an Attention Item's
expiry the trigger for `→ expired`, a mission termination, which is not in
RFC10-12's enumeration of what an expiry may do. RD-1 rated the enumeration
arguably illustrative and did not block on it; I agree with that grading and
disagree with its framing of the second half.

## 3.5 FINDING RD1b-N [Observed, recorded] — RFC10-5 overstates what RFC10-11 does

`RFC-0010:160-162`:

> **A rule that bounded `blocked` alone would leave `paused` as the park a
> mission is told to enter**, which is what RFC10-11 and RFC10-22 both do.

RFC10-22 **mandates** `paused` (`:666`). RFC10-11 does not: `:315-316` offers an
undecided disjunction, "transition to `paused` or `blocked`". "Both do" is
false of RFC10-11. Trivial in itself, but it papers over a live gap RD-1 named
and the repair did not take: **the RFC10-11 disjunction still has no decider.**
Now that both disjuncts are bounded the choice is no longer an escape, which is
why I record rather than except it.

## 3.6 Citations sound but imprecise, and one carried forward

**[Observed]** `RFC-0010:409` cites RFC5-21 for "a Syzygy-launched profiled
run"; the clause establishing profiled execution is RFC5-18. RFC5-21 is on point
for admissibility (`:151-153`). Imprecise, not false. RD-1 reached the same
conclusion.

**[Observed] RD1-K stands.** `RFC-0010:8` still reads
`depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008]`.
RFC-0004 is a reliance of RFC10-17 (`:409-410`) and RFC10-18(a) (`:504`,
`:516`) and is absent. **RFC-0011 is also absent**, while `:741-743` binds every
mission-spawned agent run to a governed context packet — RD-1 recorded this as
RC-7's F15.

**[Observed] RD1-L stands.** `retention` occurs exactly once in the file
(Python `re` over all 781 lines, 1 hit, `:505`), and no clause defines a mission
retention horizon. It fails closed via `:506` ("A determination whose evidence
has aged out is Unknown, not negative").

**[Observed] One recorded observation RD-1 did not make.** RFC10-17 sets no
evidence tier for `spent`, while `RFC-0004/execution-record.md:129-131` labels a
cost "computed from token counts and a rate table" **Inferred**. So a monetary
bound may be enforced on Inferred figures while RFC10-18(a) demands
`gate-backed` for the effects predicate. The two planes apply different evidence
bars to the two quantities they turn on, and the contract does not say so.

**[Observed] RFC10-17's `overrun` versus its own invariant.** `:397-398`
"reserved + spent never exceeds authorized" against `:393-394` "**overrun**
(spend exceeding authorized)". RD-1 rated this reconcilable (the invariant binds
dispatch, overrun arises from mis-declared maxima) and I agree — but the
invariant is written as a universal and is false as written, and RD1b-E(e)
depends on which reading holds.

---

# Criterion 4 — The moved material

## 4.1 Did anything normative move?

**[Observed] No.** I diffed the subject file between `aee13d5` and `0623784`
and read every removed line. The removals are: §0's reader summary (rewritten,
same content, compacted); RFC10-5's old park paragraph (replaced by a wider
one); two RFC10-17(a) table rows (replaced by four); the false sentence at old
`:431-433` (deleted, correctly); RFC10-18(a)'s and RFC10-19(a)'s opening
sentences (recompacted); and the twenty-one violation cases. **No obligation was
removed.** Every duty I could locate in the old text has a current home, and the
current text states several the old did not (`:439-442`, `:488-494`, `:549-556`,
plus RFC10-17(a) rows 5 and 7).

**[Observed]** The moved cases carry a non-normative label in both places —
`RFC-0010:708` ("They are non-normative teaching examples") and
`history/RFC-0010-history.md:87-89` ("Non-normative: … none of them binds
anything. Where a case and a clause disagree, the clause wins"). The history
file's own header, `:4-5`, states "**Nothing here binds.**" Correct.

**[Observed]** §5a's pointer (`:744-748`) and §6's ("full rationale in the
history file", `:750`) were already pointers before this revision; the amendment
log did not move in this pass.

## 4.2 FINDING RD1b-L [Observed, exception] — §4's pointer misdescribes the moved material, and the history file's own log describes the pre-repair text

**(a) "one per clause" is false.** `RFC-0010:705-707`:

> **Moved to `../../history/RFC-0010-history.md` §"Violation cases"** —
> **twenty-one worked scenarios, one per clause**, each naming the escape it
> closes.

Computed by script over `history/RFC-0010-history.md` §"Violation cases":

- 21 cases ✅ (the count is right)
- 17 distinct clause identifiers named
- **8 clauses have no case at all:** RFC10-3, RFC10-4, RFC10-7, RFC10-9,
  RFC10-10, RFC10-12, RFC10-14, RFC10-16
- **4 clauses have more than one:** RFC10-19 ×2, RFC10-20 ×3, RFC10-21 ×2,
  RFC10-22 ×2

The contract carries 25 clause identifiers (`:5`, RFC10-1..22 plus three
sub-clauses). "One per clause" is false in both directions. It is a small claim,
but it is the kind of derived total the repository's own verification rule 3
exists for ("a derived value quoted outside its owning artifact goes stale
silently"), and it is quoted in the contract about an artifact outside it.

**(b) The history file's rev11b entry describes the text RD-1 reviewed, not the
text that is there now.** `history/RFC-0010-history.md:57-59`:

> Amended in place: **RFC10-5** (**no block is indefinite** — `blocked →
> expired` at a declared maximum park duration, stated at lifecycle level because
> it holds for **every block class** and an indefinite park held budget under any
> source)

The current clause reads "**No park is indefinite — `blocked` or `paused`**"
(`RFC-0010:147`). The log's description is the pre-repair wording. Likewise
`history/RFC-0010-history.md:69-71` describes RFC10-17(a) as "a stated release point per terminal and park
state" with no mention of the recovery-headroom carve-out, and RFC10-18(a) with
no mention of its "governs that predicate wherever it appears" scope; and there
is no entry for the RD-1 repairs at all.

**[Observed]** So a reader following `RFC-0010:744-748` ("Moved to … which holds
the rev11, rev11a and rev11b entries in full") to learn how the contract got
here is told that RFC10-5 bounds `blocked`, which the clause it is the log of
contradicts. Non-normative, and the history file's own precedence rule (`history/RFC-0010-history.md:4-5`)
resolves it correctly — but the log is now wrong about its subject.

**(c) §4's other claims check out.** "twenty-two clauses and three sub-clauses in
one file" (`:711-712`) ✅ matches `:5`. "the convention seven of eleven contracts
already follow" (`:715-716`) ✅ — `rfcs/` holds seven package directories
(RFC-0002/3/4/5/7/8/9) and four single files (RFC-0001/6/10/11). The claim that
the cases "were the largest block of non-normative text in a contract that had
reached its per-module word ceiling" is **[Unknown]** to me: the ceiling lives
in an artifact I was not commissioned to read.

## 4.3 Does the contract still state every obligation it did before?

**[Observed] Yes**, per §4.1. And `:5`'s self-description
(`RFC10-1..RFC10-22 (sub-clauses RFC10-17(a), RFC10-18(a), RFC10-19(a); no gaps,
no retired numbers)`) matches the clause set present in the body — I checked each
of the 25 identifiers occurs as a bolded clause heading.

---

# Criterion 5 — RD-1's ten non-blocking findings

## 5.1 Exception-grade (RD1-D … RD1-H)

| ID | Status | Evidence |
|---|---|---|
| **RD1-D** | **Stands, verbatim, and its severity rose** | `:512-516` unchanged; the Unknown still fires "where the envelope names any such surface". Because `:488-491` made RFC10-18(a) the governing rule for RFC10-19 and RFC10-20(c), the declaration-keyed Unknown is now the sole gate on the correction plane rather than one of two. RD-1's proposed coverage-keyed alternative is not adopted; `unmediated` remains 2 occurrences, both inside 18(a), and the field is still not in RFC10-7's enumeration (`:194-216`) |
| **RD1-E** | **Stands, verbatim** | `:496-497` "carries all four of completion's requirements"; the Evaluator bullet `:499-502` still omits approval-time naming. See RD1b-I: the requirement it drops is itself resting on a false citation |
| **RD1-F** | **Stands, verbatim** | `:587-592` unchanged. The irreversible branch still escalates "before any further dispatch" without halting active siblings, while the safer all-compensatable branch takes `compensate-all` and does halt them (`:582-585`). The default remains weaker exactly where the effect mix is more dangerous |
| **RD1-G** | **Stands, verbatim** | `:603-620` unchanged; limb (b) still scoped to "every run Syzygy launched" and the boundary sentence `:618-620` still names only externally-credentialed effects. "work item" occurs zero times in RFC10-20 |
| **RD1-H** | **Stands, verbatim, and the same limb carries a false citation** | `:625` still enumerates only "reports failure … or a declared maximum elapses". The hung-kill-switch × undeclared-latency cell is untouched. Plus **RD1b-H** |

## 5.2 Recorded (RD1-I … RD1-M)

| ID | Status |
|---|---|
| **RD1-I** | **Closed** by the new `:433` row — and **reproduced in `paused`** (RD1b-F) |
| **RD1-J** | **Stands, and the repair widened it** to both park states (§2.1) |
| **RD1-K** | **Stands.** `:8` unchanged; RFC-0011 is also absent |
| **RD1-L** | **Stands.** 1 occurrence of `retention`, `:505` |
| **RD1-M** | **First half stands** (RFC10-12's enumeration); **second half changed shape and is stronger than RD-1 said** — RD1b-J: the row contradicts RFC10-12 generally, not only at the default |

---

# Criterion 6 — Calibration: which standing findings bite today?

**RD-1's reasoning, quoted:**

> Under the propose-only cap, `RFC10-18(a)`'s predicate — "have effects
> **outside** `.syzygy/**` and `openspec/**` been applied" — is always false,
> because `:228-233` forbids exactly those effects. So RD1-C, RD1-D, RD1-F and
> much of RD1-G are **inert until the cap lifts**.

**[Observed] That reasoning does not hold, and it is inconsistent with the
clause RD-1 rated its strongest.** It infers "the predicate is always false"
from "the cap forbids those effects" — which conflates *forbidden* with *did not
happen*. RFC10-18(a) itself refuses that inference, at `:514-516`:

> Syzygy's records cannot establish that an unmediated effect did *not* occur

and RFC10-10 concedes the capability, at `:302-306`:

> an actor holding externally-granted toolchain credentials can act outside
> Syzygy's mediation, and those effects are bounded by the adapter and credential
> authorization (VIS-5) — not by this runtime.

A propose-only envelope may still grant an execution profile carrying an
injected credential (RFC10-7 `:201-202` grants "tools, model/provider classes,
and execution profiles"). The cap forbids the *effect*; it does not remove the
*capability*, and the correction plane exists for the case where the prevention
plane was escaped. **The effects-applied predicate is therefore not inert under
the cap — under the cap it is the cap's only detector.** RD-1's own RD1-D makes
exactly this argument one section earlier ("the plane exists for the case where
the prevention plane was escaped") and then does not carry it into the
calibration note.

**Re-tested calibration:**

| Finding | Bites today under `propose-only`? | Why |
|---|---|---|
| **RD1b-A** child grants unreleased | **Yes** | `:231-232` permits "run agents within its reserved budget"; child grants are debited at grant time regardless of what is dispatched |
| **RD1b-B** queue bound vs mandated items | **Yes** | Items are minted under the cap; RFC10-8 blocks, RFC10-18 blocks and RFC10-20(d) failures are all reachable with no external effect |
| **RD1b-D** ill-typed fallback limb | **Yes** | Reached whenever a mandated item cannot be minted |
| **RD1b-E** headroom accounting | **Yes** | Budget is authorized, reserved, spent and can overrun under the cap |
| **RD1b-H** false RFC5-21 attribution | **Yes** | Stop is exercised over Syzygy-launched runs under the cap |
| **RD1b-I** RFC10-9 citation | **Yes** | Completion adjudication runs under the cap |
| **RD1b-J** RFC10-17(a) vs RFC10-12 | **Yes** | Items expire under the cap |
| **RD1b-L** §4 / history-log misdescription | **Yes** | Independent of the cap |
| **RD1-D** declaration-keyed Unknown | **Yes** — contra RD-1 | It is the detector for a cap breach; keying it on the breaching party's declaration is live today |
| **RD1-E** dropped approval-time naming | **Yes** — contra RD-1 (RD-1 did not class it inert, correctly) | Completion establishment runs under the cap |
| **RD1-G** stop coverage | **Yes**, in part | Syzygy-dispatched non-Syzygy-launched work exists under the cap; RD-1's "much of" is right |
| **RD1-H** hung kill switch | **Yes** | RD-1 agrees |
| **RD1b-C** missing `paused → expired` edge | **Yes** | RFC10-22 mandates `paused` under the cap |
| **RD1b-F** `paused`-with-effects row | **Waits** | Requires out-of-namespace effects |
| **RD1b-G** RFC10-19(a) unnamed site | **Waits, mostly** | Sibling disposition turns on external effects; live only on a cap breach |
| **RD1b-K** no duty on `reversible` | **Waits** | Requires a permitted external effect class |
| **RD1-F** non-monotonic sibling default | **Waits** | Same |
| **RD1-J** self-clearing RFC10-8 block | **Yes** | Widening attempts are reachable under the cap |
| **RD1-K / RD1-L** | **Yes** | Document-level |

**[Observed]** RD-1's core calibration claim — that RD1-A and RD1-B were *not*
inert because budget is spent under the cap — is correct and I confirm it. Its
extension of inertness to RD1-C/D/F/G is what does not survive.

---

# Criterion 7 — Attacks I constructed that the prior review did not

New at this digest: **RD1b-A** (child grants in pre-running states),
**RD1b-B** (queue bound vs mandated items), **RD1b-C** (missing vocabulary
edge), **RD1b-D** (ill-typed fallback limb), **RD1b-E** (headroom accounting),
**RD1b-G** (unnamed predicate sites), **RD1b-H** (false RFC5-21 attribution),
**RD1b-I** (RFC10-9 citation), **RD1b-K** (`reversible` has no duty),
**RD1b-L** (§4 and history-log misdescription), **RD1b-N** (RFC10-11
overstatement). All are set out above.

## 7.1 FINDING RD1b-M [Observed, recorded] — RFC10-18's no-effects branch asserts a duty set that is by construction empty

`RFC-0010:471-479`:

> - **With no applied effects it enters `blocked`** … at the maximum the mission
>   transitions to `expired`, **RFC10-19's duties fire**, and RFC10-17(a)
>   releases the reservation.

RFC10-19's duties are conditioned on "with effects already applied" (`:536`).
This is the **no** applied effects branch. So "RFC10-19's duties fire" describes
a trigger the branch's own predicate excludes. Harmless — the assertion is
vacuously satisfiable — but it reads as an assurance the branch cannot deliver,
and a reader checking the correction plane's coverage will count it as one.

## 7.2 Attacks that failed

Stated plainly, because most of this contract held and because a second
confirming review that reports only breakage is not calibrated.

- **The park rule against `paused`.** RD-1's executed attack no longer runs
  (§1.1). The repair is correct and the false sentence was deleted rather than
  defended.
- **The unfundable compensation.** I tried to reconstruct RD1-B through the
  `expired` row, through an overrun that eats the headroom, and through a child
  mission with no approval act. All three land in `:549-556`'s escalation:
  recorded, per-effect, named in the terminal reason. The duty is never silently
  omitted.
- **Tier shopping**, both at completion (`:482-484`) and at the effects
  predicate (`:507-509`). `report-fact` is excluded by name and RFC2-25 backs it.
- **The Unknown fail-closed rule** (`:518-527`). Four routes, none worked. It is
  correctly derived from RFC10-17's Unknown-spend rule and honest about its cost.
- **Delegation laundering** (`:451-456`, `:499-502`). "At any depth" closes it.
- **Cross-project egress** (RFC10-21). Content-keying plus the unattributable
  limb (`:650-651`) closed every composite I built, including one assembled by a
  child mission whose declared target names only the consented project.
- **The propose-only cap** (`:229-243`). I looked for an effect it permits
  outside the two namespaces and found none; the RFC5-22 override ("whether or
  not the granted execution profile standing-approved it", `:236-238`) closes
  the inheritance route, and `:242-243` forecloses reading the cap as
  provisional.
- **Stop propagation to descendant missions** (`:608-613`). Complete over
  RFC10-8's derivation relation, with an enumeration requirement that makes the
  record checkable.
- **Budget measurement independence** (`:408-417`). Self-reported `spent` and
  worker-declared maxima are both named and excluded.
- **An attention flood through the exempt class** (`:669-675`). Dedup plus
  single-exemption closes it. The clause is sound; RD1b-B is about what it
  collides with, not about the bound itself.

---

# Severity summary

**Blocking (REVISE) — 2**

| ID | Finding |
|---|---|
| **RD1b-A** | A child mission's grant is debited from the parent at *grant* time (`:259-260`) and released only at mission states the child may never reach (`:427-434`); a child left in `draft`/`approved` holds the parent's budget with no release point, falsifying RFC10-17(a)'s own title. RD1-A's escape, one state earlier |
| **RD1b-B** | RFC10-22's queue bound (`:665-667`, default one item) forbids Attention Items that RFC10-8, RFC10-18, RFC10-18(a), RFC10-19 and RFC10-20(d) mandate; its prescribed remedy — "the mission pauses" — is unavailable at a terminal transition, and the suppression is agent-triggerable against RFC10-8's self-widening notice. Outcome unstated |

**Exception-grade — 10 new, 5 carried**

| ID | Finding |
|---|---|
| **RD1b-C** | RFC10-5's state vocabulary (`:130-135`) has no `paused → expired` edge that the same clause's repaired prose (`:147-153`) and RFC10-17(a):431 both require |
| **RD1b-D** | The park rule's third fallback limb, "the envelope's shortest declared maximum" (`:150-151`), ranges over durations, counts and rates alike and may have no referent; it is reached exactly when RD1b-B suppresses the item |
| **RD1b-E** | Recovery headroom has no representation among RFC10-17's five quantities; the invariant does not protect it; RFC10-11's bound is undefined against it; RFC10-19 calls it "reserved" where RFC10-17 defines `reserved` to exclude it; "at approval time" has no referent for a derived child |
| **RD1b-F** | RFC10-17(a) has no row for `paused` **with** applied effects — the state RFC10-22 mandates. RD1-I closed for `blocked`, reproduced in the sibling |
| **RD1b-G** | RFC10-18(a) enumerates two governed sites and asserts "the two clauses"; RFC10-19(a)'s trigger (`:570-571`) and RFC10-17(a)'s row conditions are further sites it does not name |
| **RD1b-H** | RFC10-20(d):631-633 asserts that a kill switch without a failure signal "has not satisfied RFC5-21". RFC5-21 contains no failure-signal requirement |
| **RD1b-I** | RFC10-18:453-456 cites RFC10-9 for approval-time naming of the establisher; RFC10-9 says nothing about envelope contents, and RFC10-7's enumeration has no such field |
| **RD1b-J** | RFC10-17(a):432's "an item's expiry resolves the item, not the mission's state" contradicts RFC10-12:331-333's "expiry may narrow, pause, or block" generally, not only at the default |
| **RD1b-K** | RFC10-19 imposes no duty on `reversible` effects and has no reclassification path for a false `reversible` declaration; the recovery-headroom precondition does not reach them |
| **RD1b-L** | §4:705-707's "one per clause" is false (8 clauses have no case, 4 have several); the history file's rev11b entry describes the pre-repair RFC10-5, RFC10-17(a) and RFC10-18(a) |
| *(carried)* | **RD1-D**, **RD1-E**, **RD1-F**, **RD1-G**, **RD1-H** — all stand verbatim; RD1-D's severity rose |

**Recorded, non-blocking — 3 new, 4 carried**

| ID | Finding |
|---|---|
| **RD1b-M** | RFC10-18:477-479 asserts "RFC10-19's duties fire" in the branch whose own predicate excludes them |
| **RD1b-N** | RFC10-5:160-162 says RFC10-11 tells a mission to enter `paused`; RFC10-11:319-320 offers an unassigned disjunction, which remains unassigned |
| *(new)* | RFC10-17 sets no evidence tier for `spent` while RFC4-21:129-131 labels rate-table-derived cost Inferred; the correction plane's two turning quantities carry different evidence bars, unstated |
| *(carried)* | **RD1-I** closed; **RD1-J**, **RD1-K**, **RD1-L**, **RD1-M**(first half) stand |

---

# Minimum to reach CONFIRM

Exactly these two. Nothing else I found would block.

1. **Give a child mission's grant a release point outside the park states
   (RD1b-A).** Either add a bound on the pre-running states — a maximum time to
   first dispatch, expiring to `expired` and releasing under RFC10-17(a) — or
   add one row to RFC10-17(a)'s table stating that an outstanding child grant is
   released to the parent's remaining envelope when the child reaches any
   terminal state **or when the parent does**. The second is one row and closes
   both the never-started child and the orphaned-grant-on-parent-termination
   case RFC10-17(a) currently leaves unstated.

2. **State what happens when a mandated Attention Item meets the queue bound
   (RD1b-B).** Either (i) say that an item a clause of this contract *requires*
   is minted at the bound and counted, deduplicated like the existing exempt
   class — which means amending `:673-675`'s "only exempt class" sentence rather
   than leaving it to be read around — or (ii) state a hold-and-mint rule: the
   mandated item is retained and enqueued at the next free slot, and a mission
   entering a terminal state mints it regardless of the bound. Option (ii) also
   removes RD1b-D's trigger, since a park would then always have an item to
   inherit its maximum from.

The ten exception-grade findings I would accept as **named standing exceptions**
if the owner chooses to proceed, with two disclosures the acceptance record
should carry:

- **RD1b-H, RD1b-I and RD1b-L are citation and description defects, not
  escapes**, and each fails closed. They are cheap to fix and they are the third
  consecutive round in which a false or unsupported cross-reference appeared in
  a clause amended in that same round.
- **RD-1's inertness calibration should not be carried forward.** RD1-D and
  RD1-E are live today, not on cap-lift, for the reason set out in criterion 6:
  the effects-applied predicate is the propose-only cap's only detector, so
  keying it on the potentially-breaching party's own declaration is a live
  exposure under the cap rather than a deferred one. Only RD1b-F, RD1b-G,
  RD1b-K and RD1-F genuinely wait.

---

# Scope statement

**[Observed]** Everything in this report is a claim about the subject file's
bytes at sha256
`7f823aa3773c7bf47fed2f7634aa696c454b3ca62dea691c656a3f58a191f825`, commit
`0623784`, about `history/RFC-0010-history.md` at that commit, and about the
cited passages of the dependency contracts at that same commit. I make **no**
claim about the semantic delta, the offering documents, the acceptance record,
the manifest, any check script, `PROJECT-STATUS.md`, or any figure quoted
outside the two files I was permitted to read.

**[Unknown]** Whether RD1b-G's two unnamed predicate sites and RD1b-K's silence
on `reversible` effects are oversights or deliberate. I have no authoring
context and sought none. My findings are that the text does not require what I
say it does not require; intent is the owner's question.

**[Unknown]** Whether the per-module word ceiling §4:708-710 invokes is real or
what it permits. I was not commissioned to read the artifact that owns it, and
I make no claim about whether the package split §4 names for "the next pass" is
now required.

**[Observed] One note on my own grading.** I rated RD1b-B blocking on the same
standard RD-1 applied to RD1-B — a duty that is mandatory with no stated outcome
when it cannot be discharged. Its harm is more bounded than RD1-B's was: the
attempt remains recorded as evidence, and items expire, so the notification is
deferred rather than destroyed. I have set out those mitigations in §2.1 so the
owner can downgrade it to an exception on the record if they judge the deferral
adequate. I would not downgrade it myself, because the contract states no
deferral rule and `:666` prescribes a transition the mission cannot take.
