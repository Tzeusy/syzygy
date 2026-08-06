# RD-1 — Confirming review of RFC-0010 rev11b Mission safety

**Commissioned:** 2026-08-06, over the exact bytes at commit aee13d5, with no authoring rationale.
**Subject digest:** `09a9b9e2866964d45befa9e71624989e762971e8ad461a6d8c824d1a3214b00c`

# VERDICT
VERDICT: REVISE

---

## 0. Conditions of this review

**[Observed]** Subject file:
`/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/rfcs/RFC-0010-mission-control-autonomy.md`,
806 lines, sha256 as above, computed by me with `sha256sum` at commit
`aee13d5`. `git status --porcelain` reports the subject file **unmodified** in
the working tree, so the bytes I read are the bytes at the commit.

**[Observed]** Throughout, `RFC-0010:N` means line N of the subject file.
Everything else is quoted with its full relative path under
`.syzygy/governance/contracts/candidates/`.

**[Observed]** I read, in full: the subject file; `rfcs/RFC-0002/rendering-vocabularies.md`
(RFC2-23, RFC2-24, RFC2-25 regions), `rfcs/RFC-0002/reconciliation-chain.md`
(RFC2-19..22), `rfcs/RFC-0003/governance-homes-and-owner-acts.md` (RFC3-15,
RFC3-16, RFC3-16(a)), `rfcs/RFC-0004/execution-record.md` (RFC4-18..21),
`rfcs/RFC-0005/consent-egress-secrets.md` (RFC5-14, RFC5-15),
`rfcs/RFC-0005/execution-profiles.md` (RFC5-21, RFC5-22, RFC5-23),
`rfcs/RFC-0008/state-vocabulary-and-cost.md` (RFC8-19), clause headers of
`rfcs/RFC-0008/accounting-reconciliation-and-release.md`, mission-touching
lines of `rfcs/RFC-0011-context-compiler.md`, `CONTRACT-DEPENDENCY-INDEX.md`,
and the three prior raw reviews I was pointed at. I read **nothing** under
`round-2026-08c/` other than writing this file, and no commit message beyond
the one-line subject of `aee13d5` that `git log --oneline -1` printed as part of
establishing which commit I was on.

**[Observed]** All clause-location sweeps used Python `re`, never `grep`, per
the repository's ugrep hazard.

---

# Criterion 1 — Citation truth

I checked every cross-clause citation in the ten named clauses against the
cited text. **Most resolve exactly.** Two do not, and one is a citation used
for a proposition its target's own enumeration does not contain.

## 1.1 Citations verified true

**[Observed]** These I read at the target and confirm say what the citing
clause claims:

| Citing | Citation | Cited text (verified) |
|---|---|---|
| RFC10-5:155 | "RFC10-17 releases a reservation only on completion or termination" | `RFC-0010:388` — "**released** (reserved-but-unspent, returned on completion or termination)" ✅ |
| RFC10-5:153 | blocks arise under RFC10-8, RFC10-11, RFC10-18 | `RFC-0010:259` "the mission transitions to `blocked`"; `:309` "transition to `paused` or `blocked`"; `:463` "it enters `blocked`" ✅ |
| RFC10-5:160 | "fires RFC10-19's duties" for `expired` | `RFC-0010:522-523` "Where a mission enters `failed`, `cancelled`, or `expired`…" ✅ |
| RFC10-17:395 | Unknown spend (RFC8-19, RFC2-23) | `RFC-0008/state-vocabulary-and-cost.md:245` "**Absent means Unknown, never zero** (SDR-6; RFC2-23)"; `RFC-0002/rendering-vocabularies.md:81` "Missing quantity \| Cost/tokens/measures absent \| **Unknown, never zero**" ✅ |
| RFC10-17:392 | "the sibling-sum invariant RFC10-8 states for child missions" | `RFC-0010:255-257` "the parent's own spend plus the sum of outstanding child grants never exceeds any parent budget" ✅ |
| RFC10-17:404 | cost lives on the execution record | `RFC-0004/execution-record.md:99` "tokens / cost \| EA \| Per RFC4-21; absent → Unknown, never zero" ✅ |
| RFC10-17(a):422 | recovery cost reserved before it runs | consistent with RFC10-19:522-526 ✅ (see RD1-B for the consequence) |
| RFC10-17(a):427 | RFC10-20 limb (b) not achieved | `RFC-0010:608` "each such run's reservation is retained and named under RFC10-17(a)" — the two clauses agree in both directions ✅ |
| RFC10-18:440 | `gate-backed` (RFC2-25) | `RFC-0002/rendering-vocabularies.md:155` — `gate-backed` is "The **only** tier that may support a positive status claim" ✅, so RFC10-18's default is genuinely the strongest tier and is consistent with RFC10-6:172's "strongest applicable tier" |
| RFC10-18:451 | "wherever RFC2-19 leaves reconciliation uncomputed" | `RFC-0002/reconciliation-chain.md:205-212` — "**V0 renders the absence honestly** … **V1 computes**… Nothing in V0 may simulate the verdict." ✅ Accurate, and materially so: at V0 the no-establisher branch is the *normal* case, not an edge case |
| RFC10-18:460-461 | "RFC10-19 states that `blocked` discharges none of them" | `RFC-0010:527-528` "**Pause is not rollback**: transitioning to `paused` or `blocked` discharges no obligation under this clause." ✅ |
| RFC10-18:465-466 | "RFC10-5's human-resolution rule is scoped to blocks arising under RFC10-8 or RFC10-11" | `RFC-0010:143-145` "exit from `blocked` where the block arose under RFC10-8 or RFC10-11 is a **human resolution act**" ✅ — **this is the RC11-A repair and it is correct.** The clause now states the scope truthfully and names its own prior error at `:466-467` |
| RFC10-19:522 | "never by inheritance from an execution profile's standing approval (RFC5-22)" | `RFC-0005/execution-profiles.md:166-171` "every enabled class is either **per-run human-gated** … or **standing-approved** by the profile's approval Decision" ✅ RFC10-19 narrows RFC5-22; narrowing, not contradiction |
| RFC10-19:530-532 | resumption re-verifies RFC10-4 / RFC10-17 / RFC10-9 | all three exist and say what is claimed ✅ |
| RFC10-20:583 | "the kill switch RFC5-21 requires of every isolation class" | `RFC-0005/execution-profiles.md:148-149` "a kill switch terminating the run **and its descendants**" ✅ — including the descendants limb RFC10-20 relies on |
| RFC10-21:628-629 | "exactly as an undeterminable content class does (RFC5-14)" | `RFC-0005/consent-egress-secrets.md:142-144` "A composite whose class **cannot be determined fails closed** — the egress is **refused and the refusal rendered**" ✅ |
| RFC10-21:614-615 | "at the RFC5-15 choke point" | `RFC-0005/consent-egress-secrets.md:153-155` "Egress enforcement sits at a **single choke point** … naming (provider, content classes, project)" ✅ |
| RFC10-22:643 | "the narrowest reading (RFC10-7)" | `RFC-0010:201-206` ✅ |

## 1.2 FINDING RD1-E [Observed] — RFC10-18(a) claims to carry "all four of completion's requirements" and drops the one that makes independence non-gameable

`RFC-0010:482-483`:

> A branch selector chosen by the party it routes is not a determination, so
> **this one carries all four of completion's requirements:**

RFC10-18's requirements on the establisher, at `RFC-0010:438-447`, are four:

> (b) a declared, owner-approved evaluation independent of the executing
> principal and whose supporting evidence is `gate-backed` (RFC2-25) …
> **Independence is transitive, and established rather than asserted:** a
> principal routed by the executing principal at *any* depth is not
> independent, **and the establisher is named in the envelope at approval time
> (RFC10-9), so independence is a property of the approved envelope rather than
> a runtime selection.** An establisher chosen after the fact by the party whose
> work it adjudicates is not independent, whatever relation it declares.

i.e. (1) declared/owner-approved evaluator class, (2) transitive independence,
(3) **named in the envelope at approval time**, (4) `gate-backed` tier.

RFC10-18(a)'s four bullets are `RFC-0010:484-502`: **Evaluator**, **Evidence**,
**Minimum evidence tier**, **Externally mediated and externally credentialed
effects**. Two of those (Evidence, Externally-mediated) are *new* obligations,
not completion's. The Evaluator bullet reads, `RFC-0010:484-488`:

> - **Evaluator.** The same class of party RFC10-18 requires for `running →
>   completed`: an owner act, or a declared, owner-approved evaluation
>   independent — transitively — of the executing principal and of every
>   principal it routed.

**Requirement (3) is absent from the restatement.** The count "four" matches by
coincidence; the *set* does not. And (3) is the one requirement that closes
selection-time gaming: RFC10-18 says in terms that without approval-time naming,
independence would be "a runtime selection".

**The escape this opens.** The dispatching authority (not the executing
principal — so the "routed by" test is passed) selects, after the mission has
already applied effects, an evaluator for the effects-applied predicate. Nothing
in RFC10-18(a) requires that evaluator to have been named at approval. RFC10-18's
after-the-fact bar is written narrowly — "chosen after the fact **by the party
whose work it adjudicates**" — so a third-party post-hoc selection passes both
of RFC10-18(a)'s stated independence tests.

**[Inferred]** A charitable reading says "the same class of party RFC10-18
requires" imports (3) wholesale and the bullet merely summarises. That reading
is available. But the bullet *restates* the other requirements rather than
incorporating them by reference, and the clause immediately claims to have
carried "all four" — which is the reading a self-interested party will hold you
to. This is structurally the same defect class RC11-A found (a citing clause
representing its source as saying something its source's own scope does not),
inverted: here the citing clause claims to have *imported* a requirement it
dropped.

## 1.3 FINDING RD1-M [Observed] — RFC10-5 cites RFC10-12 for a proposition RFC10-12's enumeration does not contain

`RFC-0010:147-151`:

> Every `blocked` state carries a **maximum park duration**, declared by the
> envelope; **where none is declared the maximum is the expiry of the Attention
> Item the block minted (RFC10-12)** … At the maximum the mission transitions
> **`blocked` → `expired`**, a terminal state whose reason is recorded.

and `RFC-0010:157-158`: "Expiry from `blocked` is a **termination, never a
resolution**: it widens nothing (RFC10-12)".

RFC10-12, at `RFC-0010:325-327`, enumerates what an expiry may do:

> the **default and expiry if ignored** — an expiry default must be safe:
> **expiry may narrow, pause, or block, and may never widen an envelope or
> approve anything**

**Terminating a mission is not in that list.** In the *undeclared* park-duration
case — which is the default, and therefore the case that governs unless an
envelope author thinks about it — the Attention Item's own expiry is what fires
the `blocked → expired` transition. So an Attention Item's expiry does something
RFC10-12's enumeration of expiry effects does not admit.

**[Inferred]** Whether this is a contradiction turns on whether "may narrow,
pause, or block" is closed. The framing sentence is "an expiry default **must be
safe**", which reads as a purpose clause with an illustrative list, and
terminating a mission is safe. So I do not rate this blocking. It is a
**citation that overstates its target** and it makes the two clauses read as
disagreeing at exactly the seam where the correction plane's timing lives.

It also makes `RFC-0010:426` misleading in the default case:

> \| `blocked` after its Attention Item expires \| the item's expiry releases
> nothing — an item's expiry resolves the item, not the mission's state. **The
> park duration is what ends the hold** \|

Where no park duration is declared, the park duration **is** the item's expiry
(`:148-150`). The row asserts a separation that, at the default, does not exist:
the same instant both resolves the item and ends the hold. The row is written as
though the two are independent quantities.

## 1.4 FINDING RD1-K [Observed] — RFC 0004 became a reliance at rev11 and `depends_on` was not updated

`RFC-0010:8`:

> depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0005, RFC-0006, RFC-0008]

RFC 0004 is not there. But the new clauses make it load-bearing, not merely
cited:

- `RFC-0010:403-405` — "`spent` is admitted from the execution record of a
  Syzygy-launched profiled run (RFC5-21, **RFC4-18..RFC4-21**) or from an
  **adapter-backed provider record (RFC 0004)**". This is the admissibility rule
  for the quantity the whole budget plane is accounted in.
- `RFC-0010:489-491` — the effects-applied determination's evidence basis is
  "the mission's guardrail decision record (RFC10-10), **each run's execution
  record (RFC4-18..RFC4-21)**, and the envelope's declared effect classification".
- `RFC-0010:501-502` — the Unknown escape hatch for unmediated surfaces is "an
  **independent adapter-backed observation (RFC 0004)**".

`CONTRACT-DEPENDENCY-INDEX.md:92` records RFC-0004 for RFC-0010 in the **cites**
column, and `:59-65` states the governing convention:

> Derived, never authored … **A citation is not a reliance.** Most of these are
> forward references from a lower layer to the surface that consumes it …
> Whether any one of them is a genuine missed dependency is owner item
> **P-21(b)**.

**[Observed]** RFC-0004 → RFC-0010 is not a forward reference from a lower layer
to a consuming surface; it is RFC-0010 reaching *down* for the evidence class
its determinations are defined over. `python3 scripts/build_dependency_index.py
--check` prints "dependency index matches regeneration — no drift", which is
true and irrelevant: the index is regenerated from the same front matter, so it
cannot detect the omission. **[Inferred]** The blanket P-21(b) disclosure covers
this row by accident, not by judgment, and the disclosure's own stated reason
("forward references from a lower layer") is false of this pair.

Consequence: a reader compiling RFC-0010's context per `06-CONTEXT-LOAD-MAP.md`
or `scripts/context_load.py` does not load the contract that defines what
`spent` and "each run's execution record" mean.

## 1.5 FINDING RD1-L [Observed] — "the mission's full retention horizon" binds to an undefined term

`RFC-0010:489-491`: the effects-applied evidence must be "retained for the
mission's **full retention horizon**."

**[Observed]** `retention` occurs exactly once in the subject file (Python `re`
sweep over all 806 lines, 1 hit, at `:491`). RFC10-7's enumeration of envelope
fields (`RFC-0010:188-201`) contains no retention field. No cited clause defines
a mission retention horizon.

This is RC-7's F1 shape ("a cap binding to an undefined term is not a cap")
applied to an obligation rather than a cap. **Severity is limited** because the
next sentence fails closed — `:492` "A determination whose evidence has aged out
is Unknown, not negative" — and Unknown routes to `failed` under `:504-507`. So
an envelope that sets a zero retention horizon buys itself a `failed` mission,
not an escape. I record it as a defect of definition, not an exploit.

## 1.6 Citations I checked and found sound but weak

**[Observed]** `RFC-0010:403-404` cites **RFC5-21** for "a Syzygy-launched
profiled run". RFC5-21 (`RFC-0005/execution-profiles.md:141-160`) is *isolation
mechanism classes*; the clause that establishes profiled execution is RFC5-18.
RFC5-21 is nonetheless on point for admissibility — `:151-153` "its outputs are
inadmissible as `gate-backed` evidence — at most `report-fact`" — so the citation
is not false, only imprecise. Not a finding.

**[Observed]** `RFC-0010:449-450` — "A mission's terminal state is an
**authorization-bearing determination** under RFC3-16(a)". RFC3-16(a)'s subject
is an *artifact*: `RFC-0003/governance-homes-and-owner-acts.md:158-162` "An
**authorization-bearing governance artifact** is any artifact whose presence
authorizes a dangerous act…". A determination is not an artifact until it is
recorded. The extension is reasonable and RFC3-16(a)'s fourth limb ("otherwise
binds project truth in a way no downstream status check can falsify") plainly
reaches it — but note that same clause's warning at `:164-170`: "Where the fourth
limb is the *only* one that catches an artifact, the honest reading is that the
artifact's class has not yet been thought about properly." Not a finding; a flag.

**Criterion 1 answer:** RFC10-17, RFC10-17(a), RFC10-18, RFC10-19, RFC10-19(a),
RFC10-20, RFC10-21, RFC10-22 cite truthfully throughout. RFC10-18(a) contains one
false characterisation of what it imported (**RD1-E**). RFC10-5 contains one
citation that overstates its target's enumeration (**RD1-M**). One undeclared
reliance (**RD1-K**) and one undefined term (**RD1-L**). The specific defect the
criterion was written to catch — RFC10-18 citing RFC10-5 for an obligation
RFC10-5's scope excluded — **is repaired, correctly and explicitly** at
`RFC-0010:463-471`.

---

# Criterion 2 — The effects-applied determination (RFC10-18(a))

I attacked each of the five limbs separately. **Three hold. Two break, and the
second break is the more serious because it puts the whole sub-clause outside
the place where the duties actually live.**

## 2.1 Limbs that hold

**Minimum evidence tier — holds.** `RFC-0010:493-495`: "`gate-backed` (RFC2-25).
A `report-fact` assertion by the executor is admissible as evidence and is never
the determination." I tried tier-shopping: report the absence of effects at
`report-fact` (RFC2-25's "'X reported Y' is Observed as a fact about the report;
Y itself is not thereby Observed") and argue the tier requirement is satisfied
because *something* Observed exists. The clause forecloses it by name. I tried
`reduced-fidelity` ("Full Observed authority *at its declared granularity*") —
the clause requires `gate-backed` specifically, and RFC2-25 makes `gate-backed`
the only tier with positive-claim authority. **Sound.**

**Unknown rule — holds, and it is the strongest sentence in the sub-clause.**
`RFC-0010:504-509`: "**Unknown fails closed: where whether effects were applied
is Unknown, effects are treated as applied** … The mission enters `failed`,
RFC10-19's duties fire, and the Attention Item states that the disposition rests
on an unresolved determination rather than on an observed effect." I could not
construct a route that turns an Unknown into a negative. The costs paragraph at
`:511-513` is honest about the trade. **Sound.**

**Transitive independence from routed principals — holds.** `RFC-0010:486-488`
plus RFC10-18's "at *any* depth". I tried a three-hop laundering chain (executor
→ sub-agent → evaluator); "at any depth" closes it. **Sound.**

## 2.2 FINDING RD1-D [Observed] — the unmediated-effect-surface Unknown is keyed to the envelope's own declaration, not to observed coverage

`RFC-0010:496-502`:

> - **Externally mediated and externally credentialed effects.** An effect
>   reachable outside Syzygy's mediation is **representable only as a declared,
>   named unmediated effect surface on the envelope** … Syzygy's records cannot
>   establish that an unmediated effect did *not* occur, so **where the envelope
>   names any such surface this predicate resolves Unknown** unless an independent
>   adapter-backed observation (RFC 0004) covers it.

The Unknown fires **on the declaration**, not on the existence of the surface.
Where the envelope names none, the predicate is decided on Syzygy's own records
alone — which, by RFC10-10's own admission at `RFC-0010:296-302`, do not see
externally-credentialed acts:

> The MUST is scoped honestly to **Syzygy's own choke points**: an actor holding
> externally-granted toolchain credentials can act outside Syzygy's mediation,
> and those effects are bounded by the adapter and credential authorization
> (VIS-5) — not by this runtime.

**The scenario.** An envelope grants an execution profile carrying an injected
credential for an external service (permitted: `RFC-0005/execution-profiles.md`
resource/credential machinery, and RFC5-21:157-158 contemplates "consuming a
credential beyond its stated purpose" as a *detectable violation*, i.e. the
capability exists). The envelope declares **no** unmediated effect surface — the
field is simply absent. The run mutates the external service. At determination
time: the guardrail decision record shows no refused or mediated external act
(there was none to mediate); the execution record's policy-violation flags are
class **EA**, so absent → Unknown-with-reason
(`RFC-0004/execution-record.md:101`), but the *determination* is about effects,
not about violations; the envelope's declared effect classification lists no
external class. An evaluator reading exactly the three evidence sources
`RFC-0010:489-491` names finds nothing, and `:496-502` gives it no instruction to
resolve Unknown because no surface was named. It resolves **negative**. Route to
`blocked`; correction plane never engages; the external mutation stands
unreported.

**Why RFC10-7's narrowest-reading rule does not save it.** `RFC-0010:212-221`
splits the rule into two limbs that give *opposite* answers here:

> an unstated *grant* is the narrowest grant; an unstated *obligation* is the
> strictest obligation.

Is an absent unmediated-effect-surface declaration a grant or an obligation?
Read as a grant → "no unmediated surfaces are granted" → the predicate may
resolve negative (the attacker's reading). Read as an obligation → "assume every
surface may be unmediated" → the predicate is always Unknown → every mission
ends `failed`, which is absurd and which no author intended. **The contract does
not say which limb applies, and the field is not in RFC10-7's enumerated envelope
fields at all** (`RFC-0010:188-201` — I checked each; "unmediated" appears
nowhere outside RFC10-18(a), 2 hits total by Python `re`).

**[Observed]** RFC10-19:517-519 does say "An effect class not so classified is
**not authorized**". That makes the undeclared external effect *unlawful*. It
does not make it *unrepresentable in the determination*, which is the whole
point of a correction plane: the plane exists for the case where the prevention
plane was escaped. Keying the Unknown on the escaping party's own declaration
reproduces, one level down, exactly the defect RC11-B named at the level above.

**[Inferred]** The correct key is coverage, not declaration: the determination is
Unknown unless the evidence basis demonstrably *covers* every effect surface the
envelope's granted tools and credentials can reach. That is the empty-plot
discipline the corpus already has —
`RFC-0002/rendering-vocabularies.md:116`, reason #5 `mapping-coverage-absent`,
"empty-plot rule: **absence claims need a coverage record**". RFC10-18(a) is
making an absence claim and does not require one.

## 2.3 FINDING RD1-C [Observed] — RFC10-18(a) is scoped to RFC10-18's branch; the predicate that actually triggers the correction plane is in RFC10-19 and has no establisher

This is the escape I rate most serious under this criterion.

RFC10-18(a) opens, `RFC-0010:477-481`:

> **RFC10-18(a). Whether effects were applied is established, not asserted.**
> **The branch above** turns on one predicate — *have effects outside `.syzygy/**`
> and `openspec/**` been applied under this mission?* — and it decides whether
> the correction plane engages at all.

and the bullets are introduced, `:482-483`, as attaching to "**this one**" — this
branch selector. "The branch above" is RFC10-18's, and RFC10-18's branch fires
**only** in the narrow case at `RFC-0010:450-453`:

> **Where no independent establisher exists for a mission's objective class** —
> including wherever RFC2-19 leaves reconciliation uncomputed — the mission
> **never reaches `completed`**.

Now read where the correction plane's duties actually attach, `RFC-0010:522-527`:

> Where a mission enters `failed`, `cancelled`, or `expired` **with effects
> already applied**: every compensatable effect's compensating action is
> attempted and its outcome recorded as evidence; every irreversible effect is
> enumerated in a single Attention Item naming what cannot be undone; and the
> mission's terminal reason (RFC10-5) states the reversibility disposition of
> every applied effect.

**RFC10-19 does not cite RFC10-18(a).** I swept the clause: the string
`RFC10-18` does not occur anywhere in RFC10-19 or RFC10-19(a). Nor in RFC10-20(c),
`RFC-0010:593-595`:

> **(c)** each terminated run's partial state is checkpointed and recorded as
> evidence, and **any effect already applied** is classified and dispositioned
> under RFC10-19.

The contrast is decisive because the authors *did* write the incorporating
phrase where they meant it, at `RFC-0010:453-455`:

> Which state it does reach depends on whether effects have been applied — **as
> established under RFC10-18(a), never as asserted by the executing principal**:

That phrase appears once. It does not appear on RFC10-19's trigger or on
RFC10-20(c). Under ordinary reading — and certainly under the reading a party
escaping obligation will advance — the omission is meaningful.

**The scenario I could not find a clause to stop.**

> A mission runs with an independent establisher validly named in its envelope,
> so RFC10-18's no-establisher branch never fires and RFC10-18(a) never engages
> by its own terms. The mission applies effects outside `.syzygy/**`, then fails
> on its own — or the owner cancels it, or it park-expires under RFC10-5. It
> enters `failed` / `cancelled` / `expired`. RFC10-19's duties are conditioned on
> "with effects already applied". **Nothing names who determines that.** The
> executing principal reports no effects. No compensation is attempted, no
> irreversible effect is enumerated, and the terminal reason states the
> reversibility disposition of an empty set. The applied effects stand,
> unreported. The mission's own record shows a clean terminal state.

**[Observed]** The `cancelled` limb is the sharpest form: an owner hitting stop
is the moment the owner most needs the enumeration, and it is a moment
RFC10-18(a) provably does not reach — RFC10-20(c) routes to RFC10-19 with the
bare phrase "any effect already applied".

**[Inferred]** A charitable reading takes RFC10-18(a)'s *title* ("Whether effects
were applied is established, not asserted") and its concluding sentence at
`:509-511` ("the predicate that routes the whole correction plane") as general.
That reading is available and is probably what was intended. But intent is not
what a contract binds with, and RC-11's finding on the previous revision was
precisely that a determination the clause "assigns to nobody" is a determination
the interested party makes. The generalisation must be in the operative text, in
RFC10-19 and RFC10-20(c), not inferable from a heading.

**Criterion 2 answer:** Yes — an executing principal can still route itself
outside the correction plane, by two routes. (i) **RD1-C:** stay out of
RFC10-18's no-establisher branch entirely and self-assert the RFC10-19 trigger,
which no clause assigns. (ii) **RD1-D:** stay inside RFC10-18(a) but exploit that
its Unknown fires on a declaration the escaping party controls. Each of the five
limbs I was asked to break independently: evaluator — cracked (RD1-E, the
approval-time-naming requirement is dropped); evidence basis — cracked (RD1-D,
no coverage requirement; RD1-L, undefined retention horizon); minimum tier —
holds; unmediated-effect-surface rule — cracked (RD1-D); Unknown rule — holds
and is excellent.

---

# Criterion 3 — Termination and reservation

**Answer: yes. `paused` is a reachable, non-terminal, unbounded state that holds
a reservation indefinitely, discharges none of RFC10-19's duties, and appears in
no row of RFC10-17(a).** This is the single most serious finding in this review.

## 3.1 The full trace

RFC10-5's state vocabulary, `RFC-0010:130-135`:

```text
draft → awaiting-approval → approved → running
running ⇄ paused
running → blocked (→ running on unblock, or → expired on park expiry)
running → completed | failed | cancelled | expired
```

Ten states: `draft`, `awaiting-approval`, `approved`, `running`, `paused`,
`blocked`, `completed`, `failed`, `cancelled`, `expired`.

RFC10-17(a)'s table, `RFC-0010:419-427`, has seven rows keyed on: `completed`,
`failed`, `cancelled`, `expired`, `blocked` (no applied effects), `blocked`
after item expiry, and one row keyed not on a state at all ("unrecoverable stop
— RFC10-20 limb (b) not achieved").

| State | Covered? | Can hold a reservation? |
|---|---|---|
| `draft` | no | no — reservation is made "at dispatch" (`:390-392`) |
| `awaiting-approval` | no | no; and RFC10-9:276-277 parks it here forever without an act, which is correct |
| `approved` | no | **[Unknown]** — the contract does not say whether dispatch requires `running`; low risk |
| `running` | no | yes, correctly and by design |
| **`paused`** | **no** | **yes — and nothing bounds it. See RD1-A** |
| `blocked`, no applied effects | yes | bounded by RFC10-5's park duration ✅ |
| **`blocked`, with applied effects** | **no** | **yes — see RD1-I** |
| `completed` / `failed` / `cancelled` / `expired` | yes | released ✅ |

## 3.2 FINDING RD1-A [Observed, blocking] — the RFC10-5 repair closed `blocked` and left `paused` open, and `paused` is the state two clauses route to

RFC10-5's new paragraph is scoped, by its own words, to exactly one state
(`RFC-0010:147-157`):

> **No block is indefinite, whatever gave rise to it.** **Every `blocked` state**
> carries a **maximum park duration** … so silence cannot buy an unbounded park.
> At the maximum the mission transitions **`blocked` → `expired`** … because the
> defect is **a lifecycle defect and not a property of any one source**:
> `blocked` is non-terminal, and RFC10-17 releases a reservation only on
> completion or termination, **so an indefinite park is a way to hold budget that
> no clause elsewhere reaches**.

Every word of that reasoning is true of `paused`, and the clause reaches only
`blocked`. `paused` is not mentioned once in RFC10-5. (Python `re` sweep for
`paused` over the whole file: **5 hits**, at `:132`, `:309`, `:528`, `:530`,
`:605`. None is in RFC10-5's park rule; none is in RFC10-17(a).)

**Two clauses route missions into `paused`, and neither assigns the choice.**

`RFC-0010:307-310`, RFC10-11:

> Reaching any envelope bound (budget, time, retries, risk floor) halts further
> materialization and execution under that mission — **transition to `paused` or
> `blocked`** with an Attention Item

The disjunction has **no decider**. RFC10-5's park rule attaches to one of the
two disjuncts. A runtime — or a fleet that can influence which bound it reaches
first — picks the unbounded one.

`RFC-0010:643-645`, RFC10-22:

> **On reaching either bound the mission pauses rather than enqueueing further
> items**: a mission may not convert the owner's finite attention into
> throughput.

This one is not even a choice: RFC10-22 **mandates** `paused`. At the stated
default of one outstanding item (`:640-643`), reaching the second item is
trivial and deterministic.

**`paused` discharges no correction duty.** `RFC-0010:527-528`: "**Pause is not
rollback**: transitioning to `paused` or `blocked` discharges no obligation under
this clause." RFC10-19's trigger set (`:522-523`) is `failed`/`cancelled`/`expired`.
`paused` is outside it, exactly as `blocked` is — but unlike `blocked`, `paused`
has no expiry into a state that *is* inside it.

**Nothing exits `paused` except a human.** RFC10-5:141-142 says "`expired` and
`cancelled` are always reachable by human act". *By human act.* The clause's own
standard, three lines later, is that "silence cannot buy an unbounded park" —
and for `paused`, silence buys precisely that.

**The clause that claims to close this is falsified by its own text.**
`RFC-0010:429-433`:

> **No non-terminal park holds a reservation indefinitely.** A runtime holding
> reservation **past RFC10-5's maximum** violates this clause, and so does a
> mission record showing headroom that reserved work still holds. **An indefinite
> park is reachable only as an explicit, owner-visible envelope declaration with
> its own act — never by silence.**

Sentence one states a general rule over "non-terminal park". Sentence two gives
it a mechanism — "RFC10-5's maximum" — that exists for `blocked` only. For
`paused` there is no maximum, so there is nothing to be "past", and the general
rule has no operative content. Sentence three is a **false claim about the
current text**: an indefinite park *is* reachable by silence, via `paused`, and
RFC10-22 will put a mission there without anyone declaring anything.

**The executed attack.**

> A mission is approved with a decomposition grant and a substantial budget.
> It dispatches work, reserving the declared maximum against the envelope
> (`:390-392`). It applies effects outside `.syzygy/**`. It then mints Attention
> Item #1 for any ordinary reason. The envelope declares no maximum outstanding
> attention count, so the maximum is one (`:640-643`). The mission mints a
> second item. RFC10-22 fires: **the mission pauses.** The exempt bound-reached
> item is minted (`:647-653`) — the owner *is* told, which is RC10-H correctly
> closed — and its expiry default, per RFC10-12:325-327, may be "pause". It
> expires to that default. The item is resolved. The mission is `paused`.
>
> From here: no park duration applies (RFC10-5 reaches `blocked` only). No
> release row applies (RFC10-17(a) has no `paused` row). No RFC10-19 duty
> applies (`:527-528` says so expressly). No terminal state is ever reached, so
> no terminal reason is ever recorded and no applied effect is ever
> dispositioned. **For a child mission, the parent's headroom is consumed
> permanently** under `:415-416` ("for a child mission to the parent's remaining
> envelope") and RFC10-8's sibling-sum invariant (`:255-257`) — the parent can
> never grant that budget again.

This is RC11-A's consequence paragraph ("Parking is now a way to hold budget"),
reproduced verbatim in the sibling state, after a repair whose stated rationale
was that "the defect is a lifecycle defect and not a property of any one source."

**Violation case 15 in the contract's own §4 (`RFC-0010:720-722`) describes this
exact failure and names only `blocked`:**

> 15. *(RFC10-5, RFC10-17(a))* A mission sits in `blocked` for four months. Its
>     reservation is never released, because `blocked` is neither completion nor
>     termination. Parking became a way to hold budget.

Substitute `paused` and the case is live against the current text.

## 3.3 FINDING RD1-I [Observed] — `blocked` **with** applied effects has no row

`RFC-0010:425` reads: "\| `blocked`, **no applied effects** \| **held**, for no
longer than RFC10-5's maximum park duration…"

An effect-bearing mission can reach `blocked` without going through RFC10-18:
RFC10-8 (`:258-260`) — "An *attempted* self-widening is a violation: the mission
transitions to `blocked`" — and RFC10-11 (`:309`). Neither is conditioned on the
mission having applied no effects. So `blocked` + applied effects is reachable,
and **no row of the table states its disposition**. The reservation is eventually
released when the park expires into `expired` (row `:424`), so this is a gap in
the stated table rather than an indefinite hold — but the table is presented as
the authority on "Every reservation has a stated release point" (`:413`), and for
this reachable combination it states none.

**[Observed]** Note also that the `blocked` rows are the only ones qualified by
an effects predicate — the very predicate RD1-C shows has no establisher for
non-RFC10-18 blocks. The row's condition is therefore evaluated by the party
that benefits from the answer.

## 3.4 FINDING RD1-J [Observed] — RFC10-5's park expiry makes an RFC10-8 self-widening violation self-clearing by silence

`RFC-0010:258-260`, RFC10-8:

> An *attempted* self-widening is a violation: the mission transitions to
> `blocked`, the attempt is recorded as evidence, and an Attention Item is minted.

`RFC-0010:143-145`, RFC10-5:

> exit from `blocked` where the block arose under RFC10-8 or RFC10-11 is a
> **human resolution act** — an agent's "condition cleared" assertion never takes
> that transition.

`RFC-0010:147-160` now adds a second exit that is not a human act: at the maximum
park duration the mission transitions to `expired`. The clause anticipates the
objection at `:157-160` — expiry "does not substitute for the human resolution
act where the paragraph above owes one, and does not mark the condition cleared."
But it also says "**It ends the mission**". Once the mission is terminal, the
owed act is owed on nothing.

Where no park duration is declared, the maximum is the Attention Item's expiry
(`:148-150`), and RFC10-12 permits an item to expire to a safe default without
any human act (`:325-327`). So the complete sequence with **zero human
involvement** is: agent attempts to widen its envelope → `blocked` + item → item
expires to safe default → park maximum (= item expiry) reached → mission
`expired`, terminal, reason recorded as expiry → RFC10-17(a) `expired` row
releases the reservation in full back to the parent envelope.

**[Inferred]** The enforcement response to the contract's own "load-bearing rule"
(RFC10-8's heading, `:239`) is now a state a violating agent can clear by
waiting, recovering its parent's budget for a fresh child. RFC10-22 bounds the
item flood, so this is not a throughput attack; it is a **consequence-erasure**
attack, and the terminal reason recorded is "park expiry", not "self-widening
violation".

**Criterion 3 answer:** Yes, indefinitely, via `paused` (**RD1-A**, blocking).
The table does not cover `draft`, `awaiting-approval`, `approved`, `running`,
`paused`, or `blocked`-with-applied-effects; of these, `paused` and
`blocked`-with-effects are reachable while holding a reservation (**RD1-A**,
**RD1-I**). The `blocked` closure is otherwise complete and correct.

---

# Criterion 4 — Stop completeness (RFC10-20)

I took the five categories separately.

## 4.1 What holds

**Direct runs — holds.** `RFC-0010:582-583`: "every run Syzygy launched under the
mission is terminated". ✅

**Descendant runs — holds.** Same sentence, "together with its descendants,
through the kill switch RFC5-21 requires of every isolation class", and RFC5-21
does require exactly that: `RFC-0005/execution-profiles.md:148-149` "a kill switch
terminating the run **and its descendants**". ✅ The citation is exact.

**Child missions and descendant missions — holds, and this is a clean closure of
RC10-E.** `RFC-0010:584-591`:

> **and the stop propagates transitively to every child mission derived from it
> (RFC10-8) and to their descendants**: a descendant mission is stopped as if the
> act had named it, its own runs terminated under this same limb, and its
> reservation dispositioned under RFC10-17(a). A stop record reporting (a) and (b)
> complete while any descendant mission may still dispatch does not conform, and
> the **enumeration of the descendant missions reached** is part of the record.

I tried to find a mission that is authorized by the stopped mission but is not
"derived from" it. RFC10-8 (`:248-254`) permits child missions **only** under an
explicit decomposition grant with "a recorded derivation", so the derivation
relation is total over children. The transitive closure plus the enumeration
requirement closes the category. ✅

**Externally mediated effects — honestly excluded.** `RFC-0010:595-598`:

> Effects produced outside Syzygy's mediation by externally-granted credentials
> are **not** covered by (b); the mission's stop record states that boundary
> explicitly rather than implying a completeness the runtime cannot deliver
> (RFC10-10).

This is the right posture and matches doctrine's not-an-enforcement-engine-outward
position as RFC10-10 states it (`:299-302`). ✅

## 4.2 FINDING RD1-G [Observed] — a third category exists between "Syzygy launched it" and "externally credentialed", and stop reaches neither it nor its boundary statement

Limb (b) is scoped to "**every run Syzygy launched**". The boundary sentence
excludes only effects "**by externally-granted credentials**". Between those two
sits: **work the mission materialized and Syzygy dispatched, running as a run
Syzygy did not itself launch.**

That category is not hypothetical; the corpus and this contract both name it:

- `RFC-0010:404-405` — `spent` may be admitted "from an **adapter-backed provider
  record (RFC 0004)**", an alternative that exists precisely because some spend
  is not on a Syzygy-launched profiled run.
- `RFC-0004/execution-record.md:100` — "profile identity + version … **absent for
  runs Syzygy did not launch**, rendered Unknown-with-reason, never blank."
- `RFC-0010:163-166`, RFC10-6 — "Missions authorize the *materialization* of work
  items; the work items themselves, their states, **dispatch**, execution records,
  and evidence remain entirely RFC 0008/0002 semantics."

**The scenario.** A mission materializes work items into the RFC 0008 work
substrate. The substrate's own scheduler (an external CI, a worker pool) picks
them up. The owner stops the mission. Limb (a) — "no further work is dispatched
and no further Syzygy-mediated act is admitted **under that mission**" — binds
Syzygy, not the substrate's scheduler, which reads work items and knows nothing
of missions. Limb (b) terminates only Syzygy-launched runs. **The already-picked-up
work continues, and the work items not yet picked up remain dispatchable.** The
stop record can truthfully report (a) and (b) complete.

**[Observed]** RFC10-20 says nothing about the work items the mission
materialized — the string "work item" occurs in RFC10-20 zero times. I checked
RFC 0008 for a routing target: its clause set
(`RFC-0008/state-vocabulary-and-cost.md`, `accounting-reconciliation-and-release.md`)
is a rendering-and-semantics contract with no cancellation act. **[Inferred]**
There is therefore no existing obligation for RFC10-20 to route to, which makes
this a genuine open seam rather than a missing citation.

The narrower harm is that the boundary sentence at `:595-598` names *one*
exclusion and thereby represents the coverage as complete but for
externally-credentialed acts. It is not.

## 4.3 FINDING RD1-H [Observed] — (d)'s failure path triggers on a kill switch that *reports failure*; a kill switch that hangs is still an unbounded wait

`RFC-0010:600-611`:

> The envelope declares a **maximum stop latency**; **an undeclared latency means
> the act is synchronous** — it does not return until (a) and (b) hold.
> Synchronous is not unbounded. **Where the RFC5-21 kill switch reports failure
> for a run, or a declared maximum elapses**, the act returns having failed to
> stop … An isolation class whose kill switch **has no failure signal** has not
> satisfied RFC5-21 and is not one a mission may run under: a stop with no
> failure path is an unbounded latency under a different name.

Two escape conditions are enumerated: *reports failure*, or *a declared maximum
elapses*. At the default — **latency undeclared** — the second is unavailable.
So the entire termination guarantee rests on the kill switch producing a failure
report.

The last sentence disqualifies an isolation class whose kill switch **has no
failure signal**. That is a *design-time* property. It does not reach the
*runtime* case: a kill switch that possesses a failure signal and, on this
invocation, neither succeeds nor signals — it hangs. RFC5-21
(`RFC-0005/execution-profiles.md:141-160`) requires "a kill switch terminating
the run and its descendants" and imposes **no timeout on the kill switch
itself**; I read the clause in full and there is none.

**The scenario.** Envelope declares no maximum stop latency (the default, and
RFC10-7's narrowest-reading rule does not supply one — a latency is neither a
grant nor an obligation-shaped envelope field in `:188-201`'s enumeration). Owner
stops. One run's sandbox is wedged; the kill switch call blocks. No failure is
reported. No declared maximum exists to elapse. **The act is synchronous and
never returns.** The owner holds a stop that has neither succeeded nor failed —
which is, word for word, violation case 17 in the contract's own §4
(`RFC-0010:726-729`):

> 17. *(RFC10-20(d))* A stop is issued against a run that will not die. Latency
>     is undeclared, so the act is synchronous — and waits. Nothing times out, no
>     item is minted, and the owner holds a stop that has neither succeeded nor
>     failed.

The clause closes the case where the kill switch *says* it failed. Its own
violation case is written against the case where nothing says anything.
**[Inferred]** RC10-F is substantially but not fully closed; the residue is the
undeclared-latency × silent-failure cell, which is the default × the realistic
failure mode.

**Criterion 4 answer:** Direct runs ✅, descendant runs ✅, child missions ✅,
descendant missions ✅ — all four are genuinely closed and the enumeration
requirement is a real improvement. Externally mediated effects are honestly
excluded ✅. Two categories are not reached: **Syzygy-dispatched work running
outside a Syzygy-launched run, and undispatched materialized work items**
(RD1-G); and **a hung kill switch under the default undeclared latency** (RD1-H).
Yes, work can continue after a stop act reports success.

---

# Criterion 5 — Sibling disposition (RFC10-19(a))

## 5.1 Is `compensate-all where every applied effect class is reversible or compensatable, otherwise escalate` well-defined?

**[Observed] For the effect *classification* — yes, and cleanly.** RFC10-19
(`:515-519`) makes the classification a closed three-way partition —
`reversible` / `compensatable` / `irreversible` — and "An effect class not so
classified is **not authorized**". So the domain of "every applied effect class"
is a subset of a three-member set with no fourth value and no undefined value.
The predicate "every member is reversible or compensatable" is total over that
domain. ✅

**[Observed] Two under-specifications, both minor.**

(i) **Whose effects?** `:566-567` says "every applied effect class" without
saying whose. `compensate-all` disposes "every completed sibling's effects
… as if that sibling had failed" (`:561-563`), so the natural scope is all
siblings' effects; but read narrowly (the failed sibling's only), a completed
sibling holding an irreversible effect would take the `compensate-all` branch.
Both readings terminate safely — the narrow one lands in RFC10-19, which
enumerates irreversible effects in an Attention Item — so this is an ambiguity,
not an escape.

(ii) **"Applied" is again unestablished** — the same predicate RD1-C shows has no
named establisher outside RFC10-18's branch. Here the party choosing the branch
is the mission machinery reading a predicate about its own siblings' effects.

## 5.2 FINDING RD1-F [Observed] — the "strictest" default is non-monotonic: the more dangerous the effect mix, the weaker the sibling containment

`RFC-0010:555-563` — the three closed-set members and what each does to *active*
siblings:

```text
independent     a sibling's outcome is unaffected — completed siblings'
                effects stand, active siblings continue
halt-siblings   active siblings stop under RFC10-20; completed siblings'
                effects stand
compensate-all  active siblings stop, and every completed sibling's effects
                are dispositioned under this clause as if that sibling had
                failed
```

`RFC-0010:565-570` — the default:

> **Unstated is not `independent`.** Under RFC10-7's obligation limb an
> undeclared disposition takes its strictest reading: **`compensate-all` where
> every applied effect class is reversible or compensatable, and otherwise an
> escalation (RFC10-13) before any further dispatch**

Read the two branches against the table:

- **All effects reversible/compensatable** (the *safer* mix) → `compensate-all`
  → **"active siblings stop"**.
- **Any effect irreversible** (the *more dangerous* mix) → escalation "**before
  any further dispatch**" → active siblings are **not** stopped. Escalation
  under RFC10-13 mints an Attention Item; nothing in RFC10-13 (`:334-343`) stops
  a running sibling, and the qualifier is expressly about *dispatch*, not about
  work already dispatched.

**The scenario.** Five siblings run under one mission with no declared sibling
disposition. Sibling 3 fails having applied an irreversible effect. The default's
second branch fires: escalate, block further dispatch. Siblings 1, 2, 4 and 5
**keep running**, and — per the clause's own stated hazard at `:574-576` — two of
them "may have consumed the failed sibling's partial output". The item's expiry
default may safely be "pause" (RFC10-12:325-327), at which point RD1-A's
`paused` hole applies to the whole mission.

Had the same mission's effects all been compensatable, the default would have
stopped every active sibling.

**[Inferred]** The intended strict reading is almost certainly "halt the active
siblings **and** escalate". The text supplies only the escalation. Under
RFC10-7's own obligation limb — "an unstated *obligation* is the strictest
obligation. … **No field's absence ever relaxes a duty**" (`:214-221`) — a default
that contains active siblings *less* than a declared `halt-siblings` would have
is not the strictest reading of the undeclared field.

## 5.3 Is the default reading actually the strict one it claims to be?

**Partly.** Against `independent` — yes, decisively, and closing "unstated is not
`independent`" was the right call. Against `halt-siblings` — **no**, in the
irreversible branch, per RD1-F. **[Observed]** The clause's justification at
`:568-570` is "the narrow reading of an undeclared *obligation* is the one that
does not silently let partial output stand" — which is an argument about
*completed* siblings' output. It does not argue anything about *active* siblings,
and that is the limb where the default is weak.

**[Observed] One structural note, not a finding.** `:552-554` fixes the closed
set "at surface specification, whose **minimum** members are" the three. A
surface specification may add a fourth, weaker member; the default's strictness
is stated relative to a set that is not yet closed. That is a deliberate,
disclosed deferral consistent with §7.

**Criterion 5 answer:** The predicate is well-defined for every effect mix over
the classification RFC10-19 fixes. The default is strict against `independent`
and **not** strict against `halt-siblings` in the irreversible branch (RD1-F).
Two minor scope ambiguities, neither an escape.

---

# Criterion 6 — Internal consistency

I checked each new clause against RFC10-1..RFC10-16 and against RFC-0001, 0002,
0003, 0005, 0006, 0008 and 0011.

## 6.1 Contradictions and near-contradictions found

**(a) RFC10-19 vs RFC10-17(a) vs RFC10-11 — the unfundable compensation.
See RD1-B below. This is the one I rate as a true contradiction.**

**(b) RFC10-5 vs RFC10-12 — expiry effects.** Named as RD1-M above. Quoting both:

- `RFC-0010:325-327` (RFC10-12): "an expiry default must be safe: **expiry may
  narrow, pause, or block**, and may never widen an envelope or approve anything"
- `RFC-0010:148-151` (RFC10-5): "where none is declared the maximum is **the
  expiry of the Attention Item** the block minted (RFC10-12) … At the maximum the
  mission transitions **`blocked` → `expired`**"

An item expiry that terminates a mission is outside RFC10-12's enumeration.
Non-blocking if the enumeration is illustrative; the clause does not say.

**(c) RFC10-17's invariant vs RFC10-17's own `overrun` quantity.** `:391-393`
"reserved + spent never exceeds authorized"; `:389-390` "**overrun** (spend
exceeding authorized)". A quantity whose existence the same paragraph's invariant
forbids. **[Inferred] Not a defect**: the invariant binds dispatch decisions and
overrun arises from mis-declared maxima, which `:409-411` names explicitly
("chronic under-declaration renders as a recorded pattern of overrun attributable
to that authority"). Reconcilable, and I record it only because it reads as a
contradiction on first pass.

**(d) RFC10-17(a):429-433 vs the current text.** Recorded under RD1-A: "An
indefinite park is reachable only as an explicit, owner-visible envelope
declaration with its own act — never by silence" is falsified by RFC10-22:643-645
plus RFC10-11:309. A clause contradicting the reachability its sibling clauses
create.

## 6.2 FINDING RD1-B [Observed, blocking] — after an RFC10-11 bound exhaustion, RFC10-19's mandatory compensation is unfundable, and the contract states no resolution

Three clauses, each sound alone:

- `RFC-0010:522-526` (RFC10-19): "Where a mission enters `failed`, `cancelled`, or
  `expired` with effects already applied: **every compensatable effect's
  compensating action is attempted** and its outcome recorded as evidence"
- `RFC-0010:422` (RFC10-17(a)): "`failed` \| released in full **after** RFC10-19's
  compensating actions are attempted — **their own cost is reserved *before* they
  run**, so recovery is never funded past an exhausted bound"
- `RFC-0010:313-316` (RFC10-11): "**strictly within the budget reserved for it at
  dispatch (RFC10-17): completion headroom is reserved in advance or the work is
  checkpointed and halted, never funded by spending past the exhausted bound.**"

and the accounting invariant, `RFC-0010:391-393`: "**reserved + spent never
exceeds authorized**".

**The scenario.** A mission with an effect-applying dispatch exhausts its
authorized budget: `spent` = `authorized`, `released` = 0. RFC10-11 fires;
the mission goes to `blocked`; RFC10-5's park duration elapses; the mission
enters `expired`. RFC10-17(a)'s `expired` row is "as `failed`", so RFC10-19's
compensating actions must be attempted, **and their cost must be reserved before
they run**. There is no headroom to reserve against — reserving anything would
violate `reserved + spent ≤ authorized`, and spending without reserving violates
`:390-392` ("**No work is dispatched without reserving its declared maximum
cost**") and RFC10-11's "never funded by spending past the exhausted bound".

**The compensation is therefore mandatory and impossible.** What happens is
**not stated anywhere in the contract**:

- It is not the failed-compensation case. `RFC-0010:535-544` covers "A
  compensating action **that fails** is not discharged by having been attempted"
  — reclassify as irreversible, join the Attention Item, state as *uncompensated*.
  An action never attempted has not failed; the record would show neither an
  attempt nor a failure, and `:540-544` conditions on "an attempted action".
- It is not an escalation. RFC10-13's minimum trigger set (`:340-343`) includes
  "unsafe recovery", which arguably fires — but "arguably" is the problem, and
  nothing routes an *unfundable* recovery there.
- It is not a widening. RFC10-8 (`:245-247`) makes widening "exclusively a human
  act", correctly. So the only lawful cure is an owner act that no clause
  requires anyone to request.

**[Observed]** This is a consequence created by the rev11b repair set:
RFC10-5's new `blocked → expired` transition is what forces an RFC10-11-exhausted
mission into RFC10-19's trigger set *without* human involvement, at exactly the
moment its budget is by definition gone. Before the lifecycle rule, an exhausted
mission parked in `blocked` and RFC10-19 never fired. The repair closed the park
and opened the funding contradiction.

**[Inferred]** The right shape is almost certainly that recovery headroom is
reserved out of `authorized` **at approval time** — carved out and never
dispatchable — so that exhaustion of the working budget cannot exhaust the
recovery budget. The contract has no such carve-out; `:386-390`'s five quantities
do not include one.

## 6.3 Consistency checks that passed

**[Observed]** I checked and found consistent:

| RFC-0010 claim | Target | Result |
|---|---|---|
| RFC10-18/18(a) require `gate-backed` | `RFC-0002/rendering-vocabularies.md:155` | consistent and strictly narrower ✅ |
| RFC10-17 Unknown ≠ zero | RFC2-23 `:81`, RFC8-19 `:245` | applies the corpus rule; does not restate a new one ✅ |
| RFC10-19 destructive class not inherited | RFC5-22 `:162-171` | narrows RFC5-22 for missions ✅ |
| RFC10-20(b) kill switch | RFC5-21 `:148-149` | exact, including descendants ✅ |
| RFC10-21 at the choke point | RFC5-15 `:153-168` | adds a conjunctive per-project condition at the same point ✅ |
| RFC10-9 A1-mechanism approval | RFC3-16(c) two-state model | consistent; RFC10-9 correctly refuses the bootstrap state for a runtime act ✅ |
| RFC10-14 act-record home | RFC3-15 `decisions/` row `:88`, RFC3-16(b) item 3 | consistent ✅ |
| RFC10-3 submission-only machine scopes | RFC5-3/5/6, RFC3-16(a) | consistent; a machine credential cannot produce the act ✅ |
| §5 RFC 0008 bullet: two fields, never folded | RFC8-12 `:76`, RFC8-28 `:216`, RFC8-30 `:242` | all three exist and say what is claimed ✅ |
| RFC-0011 packet is never an authorization source | `RFC-0011-context-compiler.md:84-85` "it is never itself an authorization source — enforcement re-derives every permission from the envelope" | consistent with RFC10-8 ✅ |

**[Observed] No contradiction found with RFC-0001, RFC-0006 or RFC-0011.**

**Criterion 6 answer:** One true contradiction (**RD1-B**, RFC10-19 vs
RFC10-17(a)/RFC10-11), one clause falsified by its siblings (**RD1-A**,
RFC10-17(a):431-433 vs RFC10-22:643 and RFC10-11:309), one enumeration mismatch
(**RD1-M**, RFC10-5 vs RFC10-12). No contradiction with RFC-0001/0002/0003/0005/
0006/0008/0011.

---

# Criterion 7 — New defects the repair introduced

I was asked to assume this round introduced one and to check RFC10-5's new
lifecycle rule against RFC10-8 and RFC10-11 blocks specifically. **It introduced
at least two, and both are on exactly that seam.**

## 7.1 Consequence for RFC10-11 blocks that the contract does not state

**RD1-B**, §6.2 above. RFC10-5's `blocked → expired` transition drags every
bound-exhausted mission into RFC10-19's trigger set at the moment it has, by
construction, no budget left to fund RFC10-19's mandatory compensating actions —
which RFC10-17(a):422 requires be reserved before they run and RFC10-11:315-316
forbids funding past the exhausted bound. Unstated outcome. **Blocking.**

## 7.2 Consequence for RFC10-8 blocks that the contract does not state

**RD1-J**, §3.4 above. The RFC10-8 self-widening block — the enforcement response
to what the contract calls its load-bearing rule — is now clearable by silence:
item expires to a safe default, park maximum (defaulted to that same expiry)
elapses, mission terminates `expired` with reason "expiry", reservation returned
in full to the parent envelope. The clause anticipates half the objection
("does not substitute for the human resolution act") and does not notice that
terminating the mission moots the act. **Exception-grade.**

## 7.3 The third one, which is on a different seam

**RD1-A**, §3.2. The lifecycle rule's own stated rationale — "the defect is a
lifecycle defect and not a property of any one source" (`:152-154`) — is not
carried out: it reaches `blocked` only, while RFC10-22:643-645 *mandates*
`paused` and RFC10-11:309 permits it. The repair simultaneously introduced the
claim at `:431-433` that "An indefinite park is reachable only as an explicit,
owner-visible envelope declaration with its own act — never by silence", which
the same revision's own RFC10-22 falsifies. **Blocking.**

## 7.4 Repairs that introduced nothing I could find

**[Observed]** RFC10-21's rev11b broadening ("under **any** mission",
"**regardless of how many projects the mission's declared target names**",
`:614-620`) introduces no new hole I could construct. I tried: a composite whose
embedded content is unattributable — closed by `:628-629` ("so does a composite
whose embedded content cannot be attributed to a project of origin at all"); a
mission declaring itself against a project whose consent it holds — closed by
`:620-626` (the predicate is "a property of the *content*"). Clean repair.

**[Observed]** RFC10-22's exempt class (`:647-653`) introduces no flood: it is
deduplicated "like any other" (`:651-652`) and is declared "the **only** exempt
class; a second one returns the queue to unbounded". I tried to flood through the
exemption by minting distinct bound-reached items for distinct bounds; dedup is
keyed on "presenting the same decision" (`:655-657`), which is arguably not the
same for two different bounds — **[Unknown]**, since the mission pauses on the
first bound anyway and cannot then reach a second. Not a finding.

**[Observed]** RFC10-19's failed-compensation paragraph (`:535-544`) is a clean
closure of RC10-D and introduces nothing; the "recorded **per effect**" and
"a partially compensated mission is never rendered as compensated" sentences
close the aggregation escape I tried next.

---

# Criterion 8 — What is still open

Judged against the clause text at this digest, not against any report.

## 8.1 RC-7 F1–F11

| Finding | Status on the current text | Evidence |
|---|---|---|
| **F1** propose-only undefined | **Closed** | `RFC-0010:223-237` carries RC-7's proposed text essentially verbatim, plus "Because this cap is what makes several other deferrals safe, it may not be read as provisional: **a cap binding to an undefined term is not a cap**" |
| **F2** no reservation / unbounded overrun / no cost-uncertainty rule | **Closed** | RFC10-17 `:385-411` and the consequential RFC10-11 amendment `:311-316`, both present |
| **F3** completion self-adjudicable | **Partly open** | RFC10-18 `:435-447` closes it for `running → completed`. **Open:** RFC10-19's and RFC10-20(c)'s "with effects already applied" predicate has no establisher — **RD1-C** — and the evaluator requirement is weakened — **RD1-E** |
| **F4** no reversibility / compensation / recovery owner / resumption | **Closed with one new gap** | RFC10-19 `:515-544` closes all five limbs. **New:** the compensation can be unfundable — **RD1-B** |
| **F5** narrowest rule covers grants not obligations | **Closed** | `RFC-0010:212-221`, including the parenthetical naming the prior error. Note it is *silent* on which limb governs an unstated field that is neither — see RD1-D |
| **F6** stop | **Partly open** | RFC10-20 (a)–(d) close in-flight runs, descendants, child and descendant missions, and the declared-latency failure path. **Open:** RD1-G (Syzygy-dispatched, non-Syzygy-launched work; undispatched materialized work items) and RD1-H (hung kill switch at the undeclared-latency default) |
| **F7** cross-project composite consent | **Closed** | `RFC-0010:613-629`, keyed on content provenance, with the unattributable case closed |
| **F8** attention queue unbounded | **Closed** | RFC10-22 `:637-661`: urgency class, max outstanding, max rate, one-item default, pause-not-enqueue, dedup with multiplicity, bounded expiry |
| **F9** disagreeing evidence | **Closed** | `RFC-0010:176-184`, including the RFC2-15 routing for co-unsatisfiable claims |
| **F10** D3 pre-answers D4; doctrine floor omits an autonomy ceiling | **Open, and untouched by this file** | `RFC-0010:66-74` — D3 "**is not applied by this RFC**". Nothing in the subject file closes or could close F10; it is an owner item on the doctrine amendment |
| **F11** the §14 coverage review's stated digest | **[Unknown]** | Concerns a different artifact I was not commissioned to read. I make no claim |

## 8.2 RC-10 findings RC10-C through RC10-H

| Finding | Status on the current text | Evidence |
|---|---|---|
| **RC10-C** `spent` has no independent measurer; nobody sizes the declared maximum | **Closed** | `RFC-0010:402-411`: "`spent` is admitted from the execution record of a Syzygy-launched profiled run … **never from a self-report by the principal whose spend it is**… The **declared maximum cost** sizing a reservation is declared by the envelope or by the dispatching authority, **never by the worker being dispatched**; chronic under-declaration renders as a recorded pattern of overrun attributable to that authority." Both limbs of RC10-C answered exactly |
| **RC10-D** failed compensation recorded and nothing more | **Closed** | `RFC-0010:535-544`: reclassified irreversible, joins the single Attention Item, stated *uncompensated* in the terminal reason, per-effect recording, "a partially compensated mission is never rendered as compensated" |
| **RC10-E** stop does not reach child missions | **Closed** | `RFC-0010:584-591`, transitive to descendants, with the enumeration in the record |
| **RC10-F** synchronous stop has no failure path | **Partly closed** | `RFC-0010:600-611` supplies a failure path for *reported* kill-switch failure and for a *declared* elapsed maximum. The default × silent-hang cell remains — **RD1-H** — and it is the cell the contract's own violation case 17 describes |
| **RC10-G** RFC10-21 keys on mission scope | **Closed** | `RFC-0010:614-626` keys on content, "regardless of how many projects the mission's declared target names", with the rationale that scope-keying lets "the composing party choose whether the rule applies" |
| **RC10-H** the bound suppresses notice of itself | **Closed** | `RFC-0010:647-653`, the single exempt class, minted and delivered at the maximum, deduplicated, declared the only one |
| *(RC10-A/B, for completeness)* | **Closed as stated, recurring in a sibling state** | RC10-A: `blocked` is no longer called a termination. RC10-B: effect-bearing missions enter `failed`. But the identical structure — a non-terminal state outside RFC10-19's trigger set holding a reservation — is now live in `paused`: **RD1-A** |

## 8.3 RC-11's findings on this file

**[Observed] RC11-A (RFC10-18 cited RFC10-5 for an obligation RFC10-5's scope
excluded) is closed, and closed well** — `RFC-0010:463-471` states the scope
correctly, names the prior error in terms ("an earlier revision cited RFC10-5 for
an obligation RFC10-5's own scope excludes"), and supplies the replacement bound.

**[Observed] RC11-B (the branch selector is self-adjudicable) is closed for the
branch RFC10-18(a) covers and reopened one level out** — RD1-C. RFC10-18(a) is
a strong sub-clause; its scoping sentence puts it in the wrong place.

**[Unknown]** RC11-C through RC11-H concern manifest and offering artifacts, not
this file. Outside my commission; no claim.

## 8.4 Non-blocking RC-7 residues I re-checked

**[Observed] F13** ("Escalation-sourced `blocked` states have no human-exit rule")
is **closed** by RFC10-5's park duration for `blocked` — and reappears as RD1-A
for `paused`, which has no exit rule of any kind.

**[Observed] F15** (context-packet identity reaches missions only through
unnumbered §5 prose) is **still open**: `RFC-0010:766-767` is the only place
RFC-0011 is bound, it is a §5 Integration bullet, and RFC-0011 is not in
`depends_on` (`:8`).

**[Observed] F16** (portfolio × per-mission concurrency composition) is **partly
closed**: `RFC-0010:632-635` gives the lesser-binds rule for *budgets*.
Concurrency and fleet capacity are listed in RFC10-15's writ (`:360-362`) with
no composition rule. Non-blocking.

---

# Severity summary

**Blocking (REVISE) — 3**

| ID | Finding |
|---|---|
| **RD1-A** | `paused` is an unbounded, un-releasing, duty-free park; RFC10-22 mandates it and RFC10-11 permits it; RFC10-17(a):431-433's claim that indefinite parks are unreachable by silence is false |
| **RD1-B** | RFC10-19's mandatory compensation is unfundable after an RFC10-11 bound exhaustion, and the contract states no outcome for that case |
| **RD1-C** | RFC10-18(a) is scoped to RFC10-18's branch; RFC10-19's and RFC10-20(c)'s "with effects already applied" predicate has no named establisher |

**Exception-grade — 5**

| ID | Finding |
|---|---|
| **RD1-D** | RFC10-18(a)'s unmediated-effect Unknown keys on the envelope's own declaration, not on evidence coverage; RFC10-7's two limbs give opposite answers for the missing field |
| **RD1-E** | RFC10-18(a) claims to carry "all four of completion's requirements" and drops approval-time naming of the evaluator |
| **RD1-F** | RFC10-19(a)'s strict default is non-monotonic: the irreversible branch escalates but does not halt active siblings |
| **RD1-G** | RFC10-20 stop reaches only Syzygy-launched runs; Syzygy-dispatched non-Syzygy-launched work and undispatched materialized work items are neither stopped nor named in the boundary statement |
| **RD1-H** | RFC10-20(d)'s failure path requires a *reported* kill-switch failure; a hung kill switch under the default undeclared latency is still an unbounded wait |

**Recorded, non-blocking — 5**

| ID | Finding |
|---|---|
| **RD1-I** | RFC10-17(a) has no row for `blocked` with applied effects |
| **RD1-J** | RFC10-5's park expiry makes an RFC10-8 self-widening violation self-clearing by silence |
| **RD1-K** | RFC 0004 is a reliance of RFC10-17 and RFC10-18(a) and is not in `depends_on`; the index's "a citation is not a reliance" rationale is false of this pair |
| **RD1-L** | "the mission's full retention horizon" is an undefined term with no envelope field |
| **RD1-M** | RFC10-5 cites RFC10-12 for a termination effect RFC10-12's expiry enumeration does not contain, and RFC10-17(a):426 asserts a separation that does not exist at the default |

---

# What I tried and could not break

Stated plainly, because the commission asks for it and because most of this
contract held.

- **The Unknown-fails-closed rule** (`:504-513`). I tried four routes to turn an
  Unknown effects-applied predicate into a negative and found none. The rule is
  correctly generalised from RFC10-17's Unknown-spend rule and correctly names
  its own cost.
- **Transitive independence** (`:441-447`). Delegation laundering at any depth is
  closed by name. My attempt to make a routed establisher *count* as independent
  instead fails closed into "no independent establisher exists", which is a
  liveness cost, not a safety one.
- **Tier shopping** (`:493-495`, `:473-475`). Both the completion tier and the
  effects-applied tier default to `gate-backed`, and `report-fact` is named and
  excluded. RFC2-25 backs this exactly.
- **Cross-project egress** (RFC10-21). The content-provenance keying plus the
  unattributable-content limb closed every composite I could construct.
- **Attention flooding** (RFC10-22). Bounds on count, rate, dedup and expiry, with
  a single deduplicated exemption. I could not construct a flood. The flood is
  now converted into a *pause*, which is where RD1-A begins — the queue clause is
  sound; the state it lands in is not.
- **Stop propagation to child and descendant missions** (`:584-591`). Complete
  over the derivation relation RFC10-8 makes total, with an enumeration
  requirement that makes the record checkable.
- **Budget measurement independence** (`:402-411`). RC10-C is fully answered on
  both limbs. I tried self-reported `spent` and worker-declared maxima; both are
  named and excluded.
- **The propose-only cap** (`:223-237`). I tried to find an effect it permits
  outside the two namespaces and could not; the RFC5-22 override ("whether or not
  the granted execution profile standing-approved it") closes the inheritance
  route.

**[Observed] A calibration note the owner should have.** Under the propose-only
cap, `RFC10-18(a)`'s predicate — "have effects **outside** `.syzygy/**` and
`openspec/**` been applied" — is always false, because `:228-233` forbids exactly
those effects. So RD1-C, RD1-D, RD1-F and much of RD1-G are **inert until the cap
lifts**, in the same sense RC-7 said of F3/F4. RD1-A and RD1-B are **not inert**:
budget is spent and reserved under propose-only (`:227-228` permits "run agents
within its reserved budget"), so a `paused` park holds real budget today, and an
exhausted-budget mission with `.syzygy/**`-internal effects still traverses
RFC10-19's trigger set via RFC10-5's new expiry.

---

# Minimum to reach CONFIRM

Exactly these, and nothing else I found would block.

1. **Bound `paused` the way `blocked` is bound (RD1-A).** Extend RFC10-5's
   maximum-park-duration rule to `paused`, or state a separate maximum for it,
   with a transition to a terminal state at the maximum; add a `paused` row to
   RFC10-17(a)'s table; and either assign the RFC10-11 `paused`-or-`blocked`
   choice to a named party or collapse the disjunction. Correct or delete
   `RFC-0010:431-433` ("An indefinite park is reachable only as an explicit,
   owner-visible envelope declaration with its own act — never by silence"),
   which is false while RFC10-22:643-645 stands.

2. **State the outcome when compensation cannot be funded (RD1-B).** Either
   require recovery headroom to be carved out of `authorized` at approval time
   and held undispatchable, or state expressly that an unfundable compensating
   action is an escalation under RFC10-13 and that every uncompensated effect
   joins the irreversible Attention Item and the terminal reason. As written,
   RFC10-19 imposes a duty RFC10-17(a) and RFC10-11 can make impossible.

3. **Generalise the effects-applied establisher to where the duties are
   (RD1-C).** Put "as established under RFC10-18(a), never as asserted by the
   executing principal" on RFC10-19's trigger sentence (`:522-523`) and on
   RFC10-20(c) (`:593-595`), or restate RFC10-18(a)'s opening so that its scope is
   the predicate wherever it appears rather than "the branch above".

The five exception-grade findings (RD1-D through RD1-H) I would accept as named
standing exceptions if the owner chooses to proceed — RD1-D, RD1-F and most of
RD1-G are inert under the propose-only cap and become live the moment it lifts,
which is the disclosure the acceptance record should carry. RD1-H is live today.

---

# Scope statement

**[Observed]** Everything in this report is a claim about the subject file's
bytes at sha256
`09a9b9e2866964d45befa9e71624989e762971e8ad461a6d8c824d1a3214b00c`, commit
`aee13d5`, and about the cited passages of the dependency contracts at that same
commit. I make **no** claim about the offering documents, the acceptance record,
the manifest, any check script's correctness, or any figure quoted outside this
file — I did not read them, by commission.

**[Unknown]** Whether RD1-C's narrow scoping of RFC10-18(a) and RD1-D's
declaration-keyed Unknown are oversights or deliberate deferrals. I have no
authoring context and sought none. My findings are that the text does not
require what I say it does not require; the question of intent is the owner's.

**[Unknown]** Whether `approved` can hold a reservation. The contract does not
say whether dispatch requires `running`; I could not establish it either way and
have not counted it as a finding.
