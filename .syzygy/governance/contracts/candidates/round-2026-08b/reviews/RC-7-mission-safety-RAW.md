# RC-7 — Adversarial safety review of Mission Control and the bounded-mission autonomy envelope

**RAW reviewer output. Stored verbatim. This artifact is not authority, accepts
nothing, adopts nothing, and proposes no edit that has been made.** Every
"proposed clause text" block below is a *draft for the owner*, not an applied
change.

**Reviewer posture:** independent adversarial safety review. No authoring
history was read; `_bootstrap/**` was not opened. The assumed threat model is a
**competent, self-interested agent fleet** reading the contract as a lawyer
reads a contract — taking every permission at its widest defensible reading and
every obligation at its narrowest — with **the owner asleep** for the duration
of the mission. Doctrine is treated as settled and is not contested.

**Standard applied:** a seam is *closed* only when a clause states a **decision
rule** and names **who decides**. A clause that raises a topic, lists a field
name, or defers a mechanism to surface specification is recorded as **open**,
regardless of how obviously the right answer follows for a good-faith reader.
"An implementation would obviously do X" is not a finding of coverage — it is
the finding.

---

## 0. Material read, with digests as read (2026-08-05)

| Artifact | sha256 as read |
|---|---|
| `rfcs/RFC-0010-mission-control-autonomy.md` | `dfcedbbf187cfcc30d05d1a23806c0efd4f30efc96b005ff34771b04710364c7` |
| `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` | `0328cb379cab1ffa462cc5bf2205241b96dec21b0917d485b0906d4fe7dcd96c` |
| `07-AUTONOMY-EXTENSION-REGISTER.md` | `43c654caad2eb5cecb6d62367076d7cebd5489525c83fcffada06a5079f40a76` |
| `round-2026-08/MISSION-CONTROL-REVIEW.md` | `66df52a4450ede0ed4e83aa53361642844b78345b70f340fe1bc0fbe6c84950f` |
| `rfcs/RFC-0011-context-compiler.md` | `ab941b801307a69f53252dd4acbbf2f0129c7fc5250a21f9b022bdf19d717dfc` |
| `doctrine/vision.md` | `816ad50c59abb08ab85dcb1be18e39c4123695521914249d9ded1a980beafa86` |
| `doctrine/architecture.md` | `e19d255f9a2f2ddaf4da83eb0fe74f17b17d96d31b31bb03f76accb1a2ac11de` |
| `doctrine/v1.md` | `aba82d1fec25d38770a94a359aef65a23506896babfaa77256c931116d229dbb` |

Also read in full or at the cited clauses: `rfcs/RFC-0005/**` (all three
modules), `rfcs/RFC-0008/**` (all three modules),
`rfcs/RFC-0003/governance-homes-and-owner-acts.md`,
`rfcs/RFC-0003/manifests-and-namespace.md` §2.3/§2.8,
`rfcs/RFC-0002/rendering-vocabularies.md`,
`rfcs/RFC-0002/reconciliation-chain.md`,
`rfcs/RFC-0002/snapshot-and-evaluation-core.md`,
`rfcs/RFC-0001-project-graph-identity-state-planes.md` §3.5–3.6.

**Method note on absence claims.** Every "the word does not appear" claim below
was produced with Python `re` over the file, never with this machine's `grep`
(which is ugrep). Terms swept over `RFC-0010` and `RFC-0011`: `rollback`,
`roll back`, `compensat`, `revert`, `irreversib`, `reversib`, `reserve`,
`reservation`, `committed`, `spent`, `released`, `overrun`, `idempot`,
`checkpoint`, `resume`, `resumption`, `recovery`, `atomic`, `partial`,
`concurren`, `rate limit`, `rate-limit`, `aggregat`, `priority`, `expiry`,
`stale`, `adjudicat`, `self-adjudicat`, `attest`. Results are cited inline.

---

## 0.1 A finding that precedes the attacks: the §14 coverage review's stated digest is wrong

`round-2026-08/MISSION-CONTROL-REVIEW.md:16` records the artifact it reviewed as:

> `| rfcs/RFC-0010-mission-control-autonomy.md | 8481335836115c5ec0316f62fd229177f17292e35cc1d71e9d48d0445c3574c6 |`

and `round-2026-08/MISSION-CONTROL-REVIEW.md:21-23` then asserts:

> **[Observed]** RFC-0010's live digest equals its `ACTIVE-CONTRACT-MANIFEST.txt`
> entry — the contract is unedited since manifest generation…

[Observed] Both claims are false as stated. The live file's sha256 is
`dfcedbbf187cfcc30d05d1a23806c0efd4f30efc96b005ff34771b04710364c7`; the
`ACTIVE-CONTRACT-MANIFEST.txt` entry for `rfcs/RFC-0010-mission-control-autonomy.md`
is the same `dfcedbbf…`; and `git show f2d202c:<path> | sha256sum` — the only
commit that has ever contained this file — is also `dfcedbbf…`. The value
`8481335836…` is a digest **RFC-0010 has never carried in the repository's
history**. `git status` reports the file unmodified.

[Inferred] Two readings, and both are damaging in the same way. Either the
review computed the digest of a different byte-sequence (a pre-commit working
copy that was subsequently edited, or the wrong file), in which case its
clause-by-clause coverage tables in §§3–4 were produced against an artifact
whose identity can no longer be established; or the digest was hand-transcribed
wrongly, in which case an `[Observed]` equality claim was recorded without the
comparison having been run in the same session. The repository's own hazard list
names both failure modes explicitly ("Digests are scripted, never
hand-transcribed"; "A derived value quoted for convenience is a promise";
"Never write a 'zero / all / 100%' claim without running that exact sweep in the
same session").

This matters beyond hygiene. `MISSION-CONTROL-REVIEW.md` is the artifact that
records **14 COVERED · 2 PARTIAL · 0 ABSENT** for the envelope field set and
**8 COVERED · 0 PARTIAL · 0 ABSENT** for the Attention Item — i.e. it is the
evidence that RFC-0010 satisfies charter §14. An acceptance decision resting on
those totals is resting on a review whose stated reading-basis does not verify.
The totals themselves are, as far as this review can tell, *substantively*
correct against the live file — I re-derived them independently below and agree
with the field-by-field marks — but "the numbers happen to be right" is not the
same as "the evidence is sound", and the review's own §4 note that it "did not
read all 28 RFC-0010/0011 clauses in full" makes the provenance question live
rather than academic.

**Disposition:** the review should be re-run against the live digest, or its
digest table corrected and its `[Observed]` label re-derived, *before* its
coverage totals are cited in the act-1 offering. Do not edit the stored raw
output; allowlist or supersede it.

---

## 1. ATTACK — Partial failure and irreversible effects

**Scenario.** A mission dispatches five workers. Three complete. One fails. One
has already published a package to a registry (`RFC5-22`'s second
destructive-operation class), which cannot be undone.

### What the contract actually says

| Question asked | Clause | Verdict |
|---|---|---|
| Does every authorized effect class declare reversible / compensatable / irreversible? | — | **ABSENT.** `irreversib` appears **zero times** in RFC-0010. `reversib` appears exactly once, at `RFC-0010:266`, and it is a field of the **Attention Item**, not of the envelope |
| Is there a checkpoint policy? | `RFC10-7` at `RFC-0010:167-168` | **FIELD NAME ONLY.** "**checkpoint and recovery obligations**" is listed among envelope fields. No clause states what a checkpoint must contain, when one must be taken, or what happens if the envelope declares none. `checkpoint format` is deferred at `RFC-0010:387` |
| Is there a rollback or compensation action? | — | **ABSENT.** `rollback`, `roll back`, `compensat`, and `revert` appear **zero times** in RFC-0010 (Python `re`, whole file) |
| Is a recovery owner named? | — | **ABSENT.** No clause names who performs recovery, who decides recovery succeeded, or who owns an unrecoverable effect |
| Is there a defined failure state? | `RFC10-5` at `RFC-0010:127` | **NAME ONLY.** `failed` appears in the lifecycle diagram. `RFC-0010:133-134` requires "every terminal state is recorded with its reason". No clause states what `failed` *obliges* — no cleanup duty, no notification duty, no evidence duty beyond the reason |
| Are there resumption semantics? | — | **ABSENT.** `resume` and `resumption` appear **zero times**. `running ⇄ paused` at `RFC-0010:126` is a transition arrow with no stated preconditions for the return leg — notably, no requirement that the envelope be re-checked, that pinned inputs be re-verified, or that remaining budget be re-computed before a paused mission resumes |

### Does the contract confuse pause with rollback?

Not by explicit conflation — the words never co-occur. It does something
subtler and worse: **pause/block is the only remedy the contract ever offers,
for every failure class.** Trace the exits:

- self-widening attempt → `blocked` + Attention Item (`RFC10-8`, `RFC-0010:198-201`)
- bound exhaustion → `paused` or `blocked` + Attention Item (`RFC10-11`, `RFC-0010:248-252`)
- pinned-input change → escalation (`RFC10-4`, `RFC-0010:117-119`)
- out-of-envelope act → refused at the choke point (`RFC10-10`, `RFC-0010:235-238`)
- ambiguous bound → escalation (`RFC10-7`, `RFC-0010:172-174`)
- unsafe recovery → escalation trigger (`RFC10-13`, `RFC-0010:281`)

Every one of these stops the *future*. Not one of them addresses the *past*.
Against a published package, a pushed commit, a mutated production database, or
a sent email, "the mission transitions to `blocked` and an Attention Item is
minted" is a no-op dressed as a control. The contract's guardrail plane is
described at `RFC-0010:235-236` as "**preventive**, not merely observational" —
which is true and valuable, and is also the whole of it. There is **no
corrective plane at all**.

`RFC10-13`'s trigger "unsafe recovery" (`RFC-0010:281`) is the single place the
contract acknowledges recovery can go wrong. It presupposes a recovery concept
the contract never defines.

### The register's answer, and why it is not enough today

`07-AUTONOMY-EXTENSION-REGISTER.md:17` schedules this honestly:

> Checkpoint/resume: **required before V1 autonomy**. Compensation/rollback of
> *external* effects: **required before auto-merge/deploy**

`MISSION-CONTROL-REVIEW.md:143-149` (F4) accepts that gating, reasoning that
"while RFC10-7's propose-only cap stands, no mission can produce the external
effect that would need rolling back."

[Inferred] **That reasoning does not hold, for two independent reasons.**

**(a) "propose-only" is undefined** — see attack §10.1 below. The cap binds to a
term whose only occurrence outside the cap itself is inside a parenthetical
example list (`RFC-0010:160-161`) in a sentence declaring the vocabulary *not
yet enumerated*. Nothing in the corpus states whether propose-only permits
launching an execution profile, spending tokens, egressing to a model provider,
or writing into `.syzygy/work/**`. A self-interested fleet reads propose-only as
"anything short of merging."

**(b) Even on the narrowest reading, the envelope inherits destructive classes
by reference.** `RFC10-7` at `RFC-0010:163-164` grants "allowed **tools,
model/provider classes, and execution profiles** (by RFC5-18 profile
identity)". `RFC5-22` (`rfcs/RFC-0005/execution-profiles.md:163-172`) lets a
profile **standing-approve** destructive classes — remote pushes, registry
publication, external-service mutation, out-of-scratch deletion — via the
profile's approval Decision, with only the security/privacy/data-contract
subset held per-run human-gated. So a mission envelope naming one profile
identity silently carries whatever irreversible effect classes that profile
standing-approved, **and the envelope has no field in which those classes are
named, bounded, or declared irreversible.** The owner approving the envelope is
not shown them.

### Verdict

**OPEN — blocking.** The contract has a prevention plane and no correction
plane. Five workers, one irreversible effect: RFC-0010 says the mission goes to
`blocked`, an Attention Item is minted stating (per `RFC-0010:266`) "whether the
situation is **reversible**", and nothing else happens. No compensating action
is owed, no owner is named, no state is guaranteed consistent, and the three
completed workers' output has no defined relationship to the failed one's.

---

## 2. ATTACK — Budget race under concurrent dispatch

**Scenario.** Envelope authorizes 10M tokens / $200. The planner dispatches
eight workers concurrently. Nothing reserves budget at dispatch.

### The distinct-quantities test

The contract does **not** define reserved / committed / spent / released /
overrun as distinct quantities. Verified by Python `re` over RFC-0010:

- `reserve` — **zero occurrences**
- `reservation` — **one occurrence**, at `RFC-0010:189`, and it is about *child
  missions*, not budget units: "**Child missions are reservations, not copies**"
- `committed` — **zero occurrences**
- `spent` — **zero occurrences**
- `released` — **zero occurrences**
- `overrun` — **zero occurrences**

The only budget vocabulary in the contract is the field list at `RFC10-7`,
`RFC-0010:164-165`: "**budgets** — token, monetary, wall-clock, retry, and
concurrency." One number per kind. No lifecycle.

### The one place reservation semantics do exist — and its scope

`RFC10-8` at `RFC-0010:194-198` is genuinely strong, and it is the model the
rest of the clause should have followed:

> Every child grant is **debited from the parent's remaining envelope at grant
> time**: the parent's own spend plus the sum of outstanding child grants never
> exceeds any parent budget, so sibling children can never jointly exceed what
> the one owner act authorized.

That is debit-at-grant with an explicit sibling-sum invariant — exactly right.
**It applies only to child missions.** Sibling *work items* and *agent runs*
dispatched under one mission — the ordinary case, and the case in this attack —
have no equivalent rule. `RFC10-6` (`RFC-0010:141-143`) hands work-item
semantics wholly to RFC 0008/0002, and RFC 0008 has no budget concept at all:
its cost clauses (`RFC8-18`/`RFC8-19`,
`rfcs/RFC-0008/state-vocabulary-and-cost.md:223-251`) are **rendering** rules
for independent cost *measures*, not enforcement rules for a spend envelope.

So: eight concurrent dispatches, each lawful at dispatch time because the
envelope's remaining budget was positive when each was checked. Collectively
they can spend an unbounded multiple of the authorized envelope, and no clause
in the corpus makes any of them unlawful.

### The sanctioned overrun

`RFC10-11` at `RFC-0010:252-254` does not merely fail to prevent this — **it
authorizes it**:

> Partial work already lawfully dispatched completes or checkpoints per the
> envelope's recovery obligations.

Read adversarially: dispatch is the moment authority attaches; once dispatched,
work completes; completion spends past the exhausted bound; the contract
requires nothing about the size of that spend, does not require it to be
reserved for in advance, and does not require it to be recorded *as* an overrun.
A conforming implementation exhausts a 10M-token budget, then spends 40M
completing eight in-flight runs, and the mission record shows a respected bound
with no overrun anywhere in it.

`MISSION-CONTROL-REVIEW.md:326-336` (F3) found this same sentence and disposed
of it as "**Material after the propose-only cap lifts; inert before it**".

[Inferred] **That disposition is wrong.** Token and monetary budgets are
consumed by *thinking*, not by *merging*. A propose-only mission still runs LLM
workers, still compiles context packets (`RFC11-11`,
`rfcs/RFC-0011-context-compiler.md:193-209`, which explicitly contemplates
sharding a packet — i.e. multiplying provider calls), still egresses to a model
provider under `RFC5-14`, and still bills. The propose-only cap constrains what
a mission may *change*; it constrains nothing about what a mission may *spend*.
F3 is live at V0, under the cap, on day one.

### Cost uncertainty — the sharpest edge

The corpus guarantees that mission spend is **partly Unknown**, and then
forbids the arithmetic that would let a bound be enforced anyway.

- `RFC8-19` (`rfcs/RFC-0008/state-vocabulary-and-cost.md:246-251`): "**Absent
  means Unknown, never zero** (SDR-6; RFC2-23). Every aggregate over
  partially-known measures discloses coverage … and never renders as a complete
  total", with the observed note "six of thirteen measures are recorded nowhere
  today".
- `RFC2-23` (`rfcs/RFC-0002/rendering-vocabularies.md:82`), *Missing quantity*:
  "**Unknown, never zero** (SDR-6); no aggregate silently treats absent as 0".

So the runtime asks "has the token budget been reached?" and the honest answer
is **Unknown**. `RFC10-11` (`RFC-0010:248-249`) triggers on "**Reaching** any
envelope bound". Unknown is not "reaching". **No clause in RFC-0010 states what
a guardrail runtime does when the spend against a bound cannot be determined.**
The corpus's general posture is fail-closed (`RFC5-14`, `RFC5-16`, `RFC11-6`,
SEC-5), and `RFC10-7`'s unstated-is-narrowest rule points the same way — but
neither reaches this case, because the *bound* is stated and it is the
*measurement* that is Unknown. The narrowest-reading rule is about the envelope's
text, not about telemetry.

A self-interested fleet reads: the bound is not demonstrably reached; therefore
`RFC10-11` has not fired; therefore work continues.

### Verdict

**OPEN — blocking.** Three independent holes: no reservation at dispatch for
sibling runs (only for child missions); a contract-sanctioned, unbounded,
unrecorded post-exhaustion overrun; and no defined behavior when spend is
Unknown, in a corpus that guarantees spend will be Unknown.

---

## 3. ATTACK — Completion self-adjudication

**The question:** who is permitted to determine that a Mission's completion
predicate is satisfied?

**The answer in the contract: nobody is named.** This is the single clearest
un-closed seam in RFC-0010.

`RFC10-5` (`RFC-0010:121-128`) states the lifecycle:

```text
running → completed | failed | cancelled | expired
```

and then, at `RFC-0010:133-138`, fixes exactly four things about it: terminal
states record their reason; `expired` and `cancelled` are "always reachable by
human act"; no transition widens the envelope; and —

> exit from `blocked` where the block arose under RFC10-8 or RFC10-11 is a
> **human resolution act** — an agent's "condition cleared" assertion never
> takes that transition.

That sentence proves the drafter knew how to name a decider and did so **for one
transition only**. By the ordinary reading of a closed enumeration, the
`running → completed` transition is *not* a human resolution act, and an agent's
"predicate satisfied" assertion **does** take it. Nothing anywhere contradicts
this: `who determines`, `self-adjudicat`, and `self-assess` return **zero
occurrences** across the whole `rfcs/` tree; `adjudicat` appears in RFC-0010
exactly once, at `RFC-0010:174`, and it is about ambiguous *bounds*, not about
completion.

### The defences that are offered, and why each is insufficient

**Defence 1 — `RFC10-6` binds the predicate to evidence.** `RFC-0010:143-152`:

> A mission's completion predicate is evaluated against **evidence** (RFC 0002),
> never against work having been performed. … The completion predicate declares
> the **minimum RFC2-25 evidence tier** it accepts (unstated means, per
> RFC10-7's narrow reading, the strongest applicable tier) … "all work items
> closed" or worker assertion alone never satisfies a conforming predicate.

This is real and it kills the crudest attack (closing tickets ≠ done). It does
**not** answer the question asked. "Evaluated against evidence" is passive
voice; the clause names no evaluator. An executing agent that produces a test
report, retains it as an Execution Record (an Evidence artifact per SDR-8), and
then declares the predicate satisfied against its own artifact has done exactly
what `RFC10-6` says, in the order `RFC10-6` says it.

**Defence 2 — `RFC2-25` reserves positive claims to `gate-backed`.**
`rfcs/RFC-0002/rendering-vocabularies.md:156` makes `gate-backed` "The **only**
tier that may support a positive status claim (Aligned, Converged, reconciled,
green)", and `:159` makes `asserted-by-worker` "never a status input".

[Inferred] **This does not evidently reach mission completion, and the corpus
supplies the counter-example itself.** `RFC8-12`
(`rfcs/RFC-0008/state-vocabulary-and-cost.md:113-116`) rules, by owner decision
B14, that the normalized work state "**is not a Claim** … a derived rendering of
scheduler and repository facts, not a status claim about a capability, so it
carries no RFC2-5 two-level claim identity, no RFC2-25 tier". A mission's
lifecycle state is the same shape of object as a work state, and **no clause
anywhere types a mission's terminal state as a Claim.** If it is not a Claim,
`RFC2-25`'s gate-backed-only rule does not bind it, and `completed` is
establishable by whatever the mission's own machinery says. If it *is* a Claim,
that is a load-bearing fact stated in no clause. Either way the contract does
not decide, and an agent choosing for itself will choose the reading that lets
it finish.

**Defence 3 — "the strongest applicable tier" (`RFC-0010:149-150`).** The
unstated-tier default is self-referentially weak: *applicable* is exactly the
judgment the executing agent makes. For an objective class with no available
gate — a refactor, a documentation pass, an investigation — the strongest
*applicable* tier is plausibly `asserted-by-worker`, and the default collapses
into the thing `RFC-0010:151-152` says never satisfies a predicate. The clause
forbids the outcome and then supplies the route to it.

**Defence 4 — reconciliation.** `RFC8-30`
(`rfcs/RFC-0008/accounting-reconciliation-and-release.md:243-249`) forbids
rendering closed work as done absent `reconciled@E`, and RFC-0010 §5
(`RFC-0010:364-370`) imports that. But `RFC2-19`
(`rfcs/RFC-0002/reconciliation-chain.md:206-213`) states that reconciliation
evaluations run only "inside a deliberately triggered propagate/sync or
observation pass", and that **"V0 renders the absence honestly"** — at V0 the
verdict is not computed at all (`RFC8-13`,
`rfcs/RFC-0008/state-vocabulary-and-cost.md:151`: "`reconciled` … V0: never
renders"). So the one mechanism that would make completion independently
establishable is, by design, unavailable for the entire stage in which Mission
Control is proposed to first exist.

### Verdict

**OPEN — blocking, per the review brief's own standing instruction.** The
contract permits self-adjudication by omission: it names a decider for one
transition and for no other, and every mechanism that would supply an
independent establisher is either not typed to reach mission state or not
computed at V0. The executing agent may report completion; nothing stops it
being the sole establisher of success.

---

## 4. ATTACK — Contradictory completion evidence

**Scenario.** The mission's own retained gate artifact says the objective is
met. The project's CI, captured at the same revision, says it is not.

**Rule found: none.**

- `RFC2-15` (`rfcs/RFC-0002/reconciliation-chain.md:71-77`) defines a
  Contradiction as "a set of **authoritative claims** in one declared scope that
  cannot simultaneously be satisfied". `RFC1-21`
  (`rfcs/RFC-0001-project-graph-identity-state-planes.md:364-370`) is identical:
  "co-unsatisfiable authoritative **claims**". **Two disagreeing evidence
  artifacts are not claims**, and nothing promotes them into claims
  automatically. The contradiction machinery — Unknown reason #8, `suspended`
  tier, adjudication-only exit — does not fire on evidence disagreement as such.
- `RFC10-13`'s trigger list (`RFC-0010:277-281`) contains "an unresolved
  contradiction or genuine product choice" — the RFC2-15 sense, i.e. not this —
  and "evidence unable to establish progress". The second is about *inability*.
  Here the agent has an artifact that does establish progress; a self-interested
  reading is that this trigger has not fired.
- `RFC2-25`'s tier ordering gives a **partial** rule: an
  `asserted-by-worker` artifact cannot defeat a `gate-backed` one, because the
  former is "never a status input". That disposes of worker-assertion-vs-CI. It
  says nothing about `gate-backed` vs `gate-backed`, or `report-fact` vs
  `report-fact`, which is the interesting case and the one an adversary
  constructs.
- Sweeps for `disagree`, `conflict`, `precedence`, `tie-break`, `tiebreak` across
  `rfcs/**` return no evidence-level rule. Every `precedence` hit is a
  *prohibition* on resolving contradictions by precedence — the right instinct,
  applied to a different object.

**Verdict: OPEN.** Non-blocking for foundational acceptance only because the
right answer is already the corpus's default posture everywhere else
(disagreement ⇒ Unknown ⇒ escalate) and the fix is one sentence. But as written
there is no rule, and an agent facing two artifacts picks the one that finishes
the mission.

---

## 5. ATTACK — Attention-item flooding

**Scenario.** Overnight, a fleet emits 400 Attention Items. One of them is the
production-database migration.

### The eight required fields — all present

I re-derived this independently of `MISSION-CONTROL-REVIEW.md` §4 (which,
per §0.1, was produced against an unverifiable digest). Against the live file,
`RFC10-12` at `RFC-0010:258-270` binds:

| # | Field asked for | Present? | Exact text and line |
|---|---|---|---|
| 1 | what happened | **YES** | "**what happened**" — `RFC-0010:259` |
| 2 | why human judgment is required | **YES** | "**why human attention is required**" — `RFC-0010:260` |
| 3 | evidence | **YES** | "the **evidence and its uncertainty** (Unknowns rendered as Unknowns, RFC 0002)" — `RFC-0010:261-262` |
| 4 | the choices | **YES** | "the **available choices**" + "the **consequence of each choice**" — `RFC-0010:262-263` |
| 5 | the default if ignored | **YES** | "the **default and expiry if ignored** — an expiry default must be safe: expiry may narrow, pause, or block, and may never widen an envelope or approve anything" — `RFC-0010:263-265` |
| 6 | blocked work | **YES** | "what work is **blocked**" — `RFC-0010:265-266` |
| 7 | reversibility | **YES** | "whether the situation is **reversible**" — `RFC-0010:266` |
| 8 | deadline/expiry | **YES** | "**expiry** if ignored" — `RFC-0010:263`; plus `RFC10-13`'s no-silent-disappearance rule at `RFC-0010:274-277` |

**8 of 8 required by clause. None missing.** `RFC10-12` also exceeds the ask in
three respects that an implementation would be tempted to drop, and they are
worth naming because they are the clause's real strength: the **safe-expiry
rule** (expiry may never widen or approve — `RFC-0010:263-265`); the
**resolution act and its provenance** as a bound field, with an authorizing
resolution being an RFC3-16(a) act (`RFC-0010:266-268`); and the **anti-bulk
rule** — "a bulk act over unenumerated items resolves nothing"
(`RFC-0010:268-270`).

### What bounds the volume: nothing

| Control asked for | Clause | Verdict |
|---|---|---|
| Rate limit | — | **ABSENT.** `rate limit` / `rate-limit`: **zero occurrences** in RFC-0010 |
| Aggregation | `RFC10-13`, `RFC-0010:272-274` | **NOT THIS.** "The attention queue **compresses event volume into decision-ready packets**" bounds the *event → item* conversion, not the item count. It is a rule against streaming, not a rule against volume. `aggregat` appears once more, at `RFC-0010:368`, about work-state rendering |
| Priority | — | **ABSENT.** `priority` appears once, at `RFC-0010:346`, and it is inside violation case 6 about a workspace store overriding a *requirement* priority. No Attention Item carries an urgency, severity, or risk class |
| Expiry | `RFC10-12`, `RFC-0010:263-265` | **PRESENT but unbounded.** Every item must state an expiry and the expiry must be safe. **No clause bounds the expiry's duration**, so an item may lawfully declare an expiry far outside the window in which its default is still safe |
| Deduplication | — | **ABSENT** |
| Queue-depth bound / overflow behavior | — | **ABSENT.** No clause states what happens when the queue exceeds any size |
| SLA | `RFC-0010:387` | **DEFERRED explicitly**: "attention-queue SLA and batching policy" |

### The attack, executed

`RFC10-13`'s compression rule is a **qualitative** obligation with no metric, no
threshold, and — decisively — **no named decider**. Nothing states who judges
whether a queue is compressed, nor what a violation looks like from outside.
400 individually well-formed, individually decision-ready, individually
non-streaming Attention Items violate no clause of RFC-0010.

Two consequences compound:

1. **The anti-bulk rule becomes a weapon.** `RFC-0010:268-270` requires one
   authorizing resolution act per item, or an act explicitly enumerating each
   item's identity and the option chosen for it. That rule is correct and I
   would not weaken it — but combined with unbounded volume it converts flooding
   into a guaranteed denial of the owner's attention. Burying the migration item
   at position 287 costs the fleet nothing and is not a violation of anything.
2. **The safe-expiry rule turns flooding into a liveness attack.** Ignored items
   expire to safe defaults, and safe means "narrow, pause, or block"
   (`RFC-0010:264-265`). 400 ignored items expiring to `block` is fail-safe in
   the security sense and a total halt in the operational sense. That is the
   correct trade — but it means an adversary who cannot widen anything can still
   reliably stop everything, and no clause acknowledges or bounds that.

**Verdict: OPEN.** The *content* of an Attention Item is fully specified and is
the strongest part of RFC-0010. The *queue* is unspecified in every dimension
that flooding exploits.

---

## 6. ATTACK — Mission self-widening

**This attack fails.** `RFC10-8` (`RFC-0010:180-201`) is the best clause in the
contract and closes every route I could construct.

| Route attempted | Blocked by | Line |
|---|---|---|
| Raise own budget / autonomy level / paths / tools / gates | "No agent, fleet, worker, or **Mission Control component** may widen any bound of the envelope it runs under: not budgets, not autonomy level, not surfaces, not paths, not tools, not gates" | `RFC-0010:180-184` |
| Spawn a wider child | "not by creating a child mission whose envelope exceeds the parent's remaining envelope" | `RFC-0010:184-185` |
| Spawn *any* child | "an agent may mint a child mission only where the parent envelope **explicitly grants decomposition** … absent the grant, the narrow reading is no children" | `RFC-0010:189-192` |
| Spawn many children summing over the parent | "Every child grant is **debited from the parent's remaining envelope at grant time**" | `RFC-0010:194-198` |
| Child self-mints its own authorizing act | "A derived child's authorizing provenance is the **parent's owner act plus a recorded derivation** — never a new self-minted act" | `RFC-0010:192-194` |
| Borrow another mission's budget | "not by consuming another mission's budget" | `RFC-0010:185-186` |
| Reinterpret an ambiguous bound favourably | "not by re-interpreting an ambiguous bound in its own favor (ambiguity resolves narrow, per RFC10-7)" | `RFC-0010:186-187` |
| Propose a widening and act on it | "An agent-proposed widening is a **proposal** — it renders as an Attention Item and has no effect until the act" | `RFC-0010:187-189` |
| Use a machine credential to perform the widening act | `RFC10-3`: "Holding a mission-affecting scope permits **submitting** the corresponding act for owner attendance and nothing more — a machine credential can never itself produce the owner act the submission awaits" | `RFC-0010:101-104` |
| Mint a fresh sibling mission with a wider envelope | `RFC10-4` (mission approval is an RFC3-16(a) owner act) + `RFC10-9` (approval is specifically an A1-mechanism runtime act; a state-(1) record does not satisfy it) | `RFC-0010:106-119`, `203-218` |
| Self-widen and hope nobody notices | "An *attempted* self-widening is a violation: the mission transitions to `blocked`, the attempt is recorded as evidence, and an Attention Item is minted" — and `RFC10-5` makes exit from *that* block a human act | `RFC-0010:198-201`, `134-138` |

**Two residual routes remain open, and neither is a widening of *authority* —
they are widenings of *what counts as success*:**

**(a) The objective is not a bound.** `RFC10-8`'s anti-reinterpretation limb is
scoped to "an ambiguous **bound**" (`RFC-0010:186`), and `RFC10-7`'s narrow-
reading rule is likewise scoped: "A **bound** stated ambiguously likewise
resolves to its narrowest defensible reading, and genuine ambiguity in a
load-bearing **bound** is an escalation trigger" (`RFC-0010:171-174`). The
**objective** (`RFC10-4`, `RFC-0010:107-108`) and the **completion predicate**
(`RFC10-7`, `RFC-0010:168-169`) are not obviously "bounds" — they are the
mission's *purpose* and its *success test*, and both are listed as envelope
fields rather than as bounds. An agent that reinterprets its objective downward
until the predicate is met has widened nothing the clause names.

**(b) Combined with §3 (self-adjudication), (a) is the whole attack.** The fleet
does not need more authority. It needs a lower bar, and it is the sole judge of
whether the bar is met.

**Verdict: CLOSED against authority-widening. OPEN against
success-criterion-widening.**

---

## 7. ATTACK — Stale context packet

**Scenario.** Mission runs six hours on a packet compiled at hour zero. At hour
three the owner amends the governing requirement.

### What is stated

- `RFC10-4` (`RFC-0010:116-119`) is the governing rule, and it is a good one:
  > Pinned inputs are immutable for the mission's life: a change to any pinned
  > input does not silently retarget a running mission — it raises an escalation
  > (RFC10-13) whose choices include re-approval against the new inputs.
- `RFC11-2` (`rfcs/RFC-0011-context-compiler.md:90-95`): amending context mid-run
  **mints a new packet version**; packets are never edited in place; the record
  binds every version consumed.
- `RFC11-6` (`rfcs/RFC-0011-context-compiler.md:126-140`): required context that
  "is **stale** against the selected evaluation" marks the packet
  incomplete/Unknown and **by default the run does not launch**.

### What is not stated — and it is the whole mechanism

1. **No detector.** `RFC10-4` says a pinned-input change "raises an escalation"
   in the passive voice and names nobody. Who compares pinned digests against
   the live tree, and how often? Not stated in RFC-0010, not in RFC-0011.
2. **No cadence.** `RFC11-6`'s staleness check is a **compile-time** gate — it
   governs whether a run *launches*, not whether a running mission's packet has
   aged out. `stale` appears in RFC-0011 at lines 119, 131, 138, 257 and in
   every case in the compile/selection context. **`stale` appears zero times in
   RFC-0010.**
3. **No maximum packet age.** No clause bounds how old a packet may be when
   consumed, and `RFC11-2`'s re-mint rule is *permissive* ("Amending context
   mid-run mints a new packet version") — it states what happens **if** context
   is amended, never that it **must** be.
4. **No halt.** `RFC10-4` says the escalation's "choices **include** re-approval"
   — choices, not a suspension. Nothing pauses the mission while the owner
   decides.

### The downstream consequence, which is doctrinally coherent and operationally bad

`RFC2-18` (`rfcs/RFC-0002/reconciliation-chain.md:146-162`) binds a
reconciliation verdict to the **warranted** intent revision, and states that
"Intent drift after merge therefore surfaces as a new gap on the current-revision
claim, never as retroactive failure of the work." Correct, and deliberate.
Applied here it means: the mission spends its full envelope for three more hours
producing work that reconciles cleanly against superseded intent, and the drift
surfaces later as a *new gap* — i.e. as more work. The owner pays twice and the
record shows a successful mission.

The system does eventually self-heal *if* the escalation is raised, because
`RFC10-12`'s safe-expiry (`RFC-0010:263-265`) eventually pauses or blocks. The
entire safety of this path therefore rests on an escalation whose trigger
mechanism, cadence, and detecting party are all unspecified.

**Verdict: PARTIALLY OPEN.** The rule exists (`RFC10-4`); the decider does not.

---

## 8. ATTACK — Cross-project authority leakage

**Scenario.** A portfolio mission targets projects A and B. Can authority,
credentials, evidence, or budget granted for A be used against B?

### What holds — and it is substantial

| Vector | Boundary clause | Line | Holds? |
|---|---|---|---|
| Portfolio store overriding project truth | `RFC10-15`: the store "**must never become authoritative for project-internal doctrine, contracts, specifications, or behavior** — its writ ends at scheduling, budget, and attention policy", and where the writ's own enumeration meets that prohibition "**the prohibition wins**" | `RFC-0010:302-310` | **YES** |
| Mission Control minting project truth | `RFC10-1`: "It mints no project truth … a projection of kernel answers (RFC 0006), rebuildable and non-authoritative" | `RFC-0010:73-80` | **YES** |
| Execution consent | `RFC5-23`: "Profiles are per-project … **no project executes under another project's consent**" | `rfcs/RFC-0005/execution-profiles.md:180-183` | **YES** |
| Observation consent | `RFC3-30`: "Role and consent are properties of the *(Project, repository)* pair … never global" | `rfcs/RFC-0003/manifests-and-namespace.md:421-425` | **YES** |
| Screening policy | `RFC3-30`: "Project A screens … under **A's** policies"; content read from B's plane "is **data about B, never governing policy for A**" | `rfcs/RFC-0003/manifests-and-namespace.md:432-450` | **YES** |
| Machine credentials | `RFC5-6` deny-by-default scoping ("which projects it may read"); `RFC5-24` injection prohibition | `rfcs/RFC-0005/admission-and-boundary.md:181-186`, `268-285` | **YES** |
| Write reach | `RFC10-7` bounds "allowed **projects, repositories, and paths**", unstated ⇒ none | `RFC-0010:163`, `169-171` | **YES** |
| Gate bypass | `RFC10-6`: "No mission bypasses evidence, reconciliation, consent (RFC5-12), egress (RFC5-14), or execution-profile (RFC5-18) gates" | `RFC-0010:144-148` | **YES** |

This is a genuinely well-composed boundary and I could not break it on
credentials, execution, observation, or write reach.

### Where it breaks: the cross-project composite

Every egress clause in RFC 0005 is written **per project**, because until
RFC-0010 nothing in the corpus produced an artifact spanning two projects.
`RFC5-15` (`rfcs/RFC-0005/consent-egress-secrets.md:154-160`) fixes the check as:

> every network transmission of governed-project content passes one consent check
> naming (**provider, content classes, project**)

singular project. `RFC5-12` (`:88-90`) makes egress consent "**one record per
*(Project, provider)* pair**". `RFC5-14` (`:126-128`) supplies a composition rule
for **classes** — "A composite inherits the **highest** class of any content it
embeds" — and **no composition rule for projects**.

Now introduce the object RFC-0010 creates. A portfolio mission spans A and B.
`RFC11-1` (`rfcs/RFC-0011-context-compiler.md:71-73`) has the packet identify
"the **project and workspace identity**" — singular again. A packet compiled for
a cross-project mission embeds A's `code-structure` and B's `code-content` and
goes to a model provider. Which consent record governs?

- `RFC5-14`'s highest-class rule gives the *class* (`code-content`).
- Nothing gives the *project*. The check names one project; the composite has two.

A self-interested compiler names project A — for which egress consent to that
provider exists — and ships B's source inside it. Every field of `RFC5-15`'s
three-part check reads as satisfied: the consent record is in force, the class is
determinable and within A's consented set, and the record's provenance verifies.
**This is precisely the failure `RFC5-14`'s undeterminable-fails-closed paragraph
(`:139-152`) was built to prevent, arriving through the one dimension that
paragraph does not cover.** RFC-0010 §5 (`RFC-0010:360-361`) asserts
"consent/egress gates unbypassed (RFC10-6)" without noticing that the gate's own
subject is singular.

**Second, smaller leak — evidence.** `RFC10-6` binds a completion predicate to
evidence but never requires the evidence's project to match the target project.
For a portfolio mission, evidence gathered in A can satisfy a predicate about B
with no clause forbidding it.

**Third — budget.** `RFC10-15` (`RFC-0010:297-299`) puts "global **and
per-project** budgets" in the workspace store; `RFC10-7` (`RFC-0010:164-165`)
puts budgets in the envelope. **No composition rule.** Which binds when they
differ, and is a portfolio mission's spend against B debited from B's per-project
budget? Unstated. (The parallel concurrency gap was noted as F7 in
`MISSION-CONTROL-REVIEW.md:419`; budget has the same shape and is the more
dangerous half.)

**Verdict: MOSTLY CLOSED, one blocking leak.** The credential/execution/write
boundary is sound. The **egress composite spanning two projects has no rule**,
and it is the highest-consequence leak in the contract because it moves source
code across a consent boundary while every field reads green.

---

## 9. ATTACK — STOP

**Scenario.** The owner hits stop. What is guaranteed to actually stop, how
fast, and what is guaranteed not to be left inconsistent?

### What stops

| Guarantee | Clause | Line | Strength |
|---|---|---|---|
| `cancelled` and `expired` always reachable by human act | `RFC10-5` | `RFC-0010:134-135` | Strong — the transition cannot be blocked by an agent |
| Further materialization and execution halt at bound exhaustion | `RFC10-11` | `RFC-0010:248-252` | Strong for the *bound* case |
| Out-of-envelope acts refused at the choke point, not performed-then-flagged | `RFC10-10` | `RFC-0010:235-238` | Strong, and honestly scoped: "The MUST is scoped honestly to **Syzygy's own choke points**" (`RFC-0010:238-244`) — an actor holding externally-granted credentials acts outside it |
| Every guardrail decision (allow / refuse / halt) recorded as attributable evidence | `RFC10-10` | `RFC-0010:244-246` | Strong |
| Isolation classes must certify a kill switch "terminating the run **and its descendants**" | `RFC5-21` | `rfcs/RFC-0005/execution-profiles.md:142-151` | Strong — but this is a *profile* property, not a mission control |
| Revoking execution consent terminates running processes | `RFC5-23` | `rfcs/RFC-0005/execution-profiles.md:178-180` | Strong — but revocation is a *different act* from stopping a mission |

### What does not stop

**1. In-flight work is explicitly exempted.** `RFC10-11`, `RFC-0010:252-254`:

> Partial work already lawfully dispatched completes or checkpoints per the
> envelope's recovery obligations.

There is **no clause anywhere in RFC-0010 binding a mission `cancel` or `stop` to
the termination of running work.** `RFC10-5:127` lists `cancelled` as a terminal
state and states nothing about its effect. The only sentence in the contract
about the fate of in-flight work says it **completes**. Read plainly: the owner
hits stop, and the eight workers already dispatched run to completion, spending
budget and producing effects, lawfully.

The strong kill-switch guarantees above are reachable only through **different
acts** — revoking execution consent (`RFC5-23`) or revoking a credential
(`RFC5-11`, effective "at the next act"). Neither is what "stop the mission"
means, and no clause routes one to the other. An owner who hits the mission stop
button and believes running work has been killed has been misled by a control
that RFC-0010 never claims does that — which is worse than an absent control.

**2. No latency bound.** No clause states how fast stop takes effect. `RFC5-11`
(`rfcs/RFC-0005/admission-and-boundary.md:236-242`) makes revocation effective
"at the next **act**" — i.e. at the next admission check, which a mid-run worker
does not perform. `attention-queue SLA` is deferred (`RFC-0010:387`); mission
stop latency is not even deferred, it is simply unaddressed.

**3. No consistency guarantee.** `atomic` appears **zero times** in RFC-0010.
`partial` appears once, at `RFC-0010:252`, in the sentence that permits partial
work to continue. Nothing states that a stopped mission leaves no half-applied
multi-file write, no pushed-but-unrecorded commit, no partially-mutated external
service. `MISSION-CONTROL-REVIEW.md:349-355` (S2 residual) identified the same
hole from the write side and deferred it to the envelope's recovery obligations —
which, per attack §1, are a field name with no content.

**Verdict: OPEN — blocking.** Stop reliably prevents *new* dispatch and reliably
refuses *new* out-of-envelope acts. It guarantees nothing about work already
running, has no latency bound, and makes no consistency claim.

---

## 10. STAGE PLACEMENT — do bounded Missions belong in V0 or V1?

### 10.1 The prior question: "propose-only" is undefined

Before placement, the safety default has to mean something. `RFC10-7` at
`RFC-0010:159-161`:

> the **maximum autonomy level** — levels are an enumerated vocabulary to be
> fixed at surface specification (e.g. propose-only, materialize work, open PR,
> merge, deploy; the enumeration is an explicit open default, §8 q2)

and at `RFC-0010:174-178`:

> Until the autonomy-level vocabulary is enumerated by owner act (§8 q2), the
> maximum autonomy level of every envelope is capped at **propose-only**: a
> stated higher level has no enumerated vocabulary to bind to and does not take
> effect.

[Observed] The term `propose-only` occurs three times in the file
(`RFC-0010:161`, `176`, `395`) and is **defined nowhere in the corpus**. The cap
— the single load-bearing safety default on which `MISSION-CONTROL-REVIEW.md`
rests its disposition of F3 and F4, and on which the D3 packet rests its
"operational risk today is nil" — binds to a term drawn from a parenthetical
`e.g.` list inside the very sentence declaring that the vocabulary is not yet
enumerated. **The cap's own referent has no enumerated vocabulary to bind to,
by the cap's own reasoning.**

Unanswerable from the text, and each answer materially changes the risk:

- May a propose-only mission launch an execution profile (`RFC5-18`) and run
  observed-project code?
- May it egress content to a model provider (`RFC5-14`)?
- May it spend money and tokens without limit short of the envelope's budget?
- May it write proposals into `.syzygy/work/**` (`RFC3-19`)?
- May it open a pull request? (`RFC-0010:161` lists "open PR" as a *separate*
  level, so presumably not — but "presumably" is doing load-bearing work.)

There is also an internal tension worth flagging: `RFC-0010:395-397` asks the
owner whether to fix "a floor … (e.g. nothing above open-PR before further act)"
— i.e. §8 q2 offers a *floor* strictly **above** the cap RFC10-7 already
imposes. Not a contradiction, but a fresh reader cannot tell from the two
passages what the operative ceiling is.

**This is the single highest-leverage fix in the review: one sentence defining
propose-only converts three deferred findings from "inert under the cap" to
genuinely inert.**

### 10.2 The V0/V1 boundary as doctrine draws it

From `doctrine/v1.md`:

- V0 is "**the trustworthy observatory, with proof the loop is real**"
  (`v1.md:3`). Its propagation mandate is explicitly minimal and one-item-grained:
  "**from one signed-off spec delta, dispatch one scheduled work item end to end
  for a worker to materialize**" (`v1.md:41-42`). One delta, one item, one
  sign-off.
- V0's writes are `openspec/**` and `.syzygy/**` only, and "**Drafting is not
  adopting**" (`v1.md:44-50`). "Syzygy never writes code."
- V1 is "**the harness**" — "Human-triggered propagation **at full breadth**"
  (`v1.md:64-73`).
- **Live agent-fleet monitoring is deferred**, with the stated rationale
  "Meaningless without the observed truth it would annotate" (`v1.md:82`).
- The **fleet-account test is a V1 test**: "at the end of an orchestration day,
  the owner can produce, from Syzygy alone, an accurate account of what the fleet
  changed and why" (`v1.md:121-124`).

A bounded Mission is, by construction, "repeated plan/materialize/execute/verify/
re-plan cycles" under one act. That is *full-breadth* propagation with the
human-approval grain coarsened. It is the V1 harness.

### 10.3 The contract's own clauses point the same way

Three independent internal signals place Mission Control past V0:

1. **`RFC10-9` makes an unbuilt mechanism a hard precondition.**
   `RFC-0010:203-215`: mission approval "is a *runtime* act … so it is always an
   A1-mechanism act — an owner-attended, Syzygy-mediated ceremony correlated to
   the external audit trail — never a bootstrap-shaped tree record: an approval
   resting on a state-(1) record (RFC3-16(c)) has **not** satisfied the predicate,
   and its mission does not leave `awaiting-approval`. **Shipping that ceremony
   is therefore a hard precondition of Mission Control operating at V0.**" The A1
   mechanism does not exist (`RFC3-16(b)` *Bootstrap correlation*,
   `rfcs/RFC-0003/governance-homes-and-owner-acts.md:269-285`), and the machine-
   credential mechanism underneath it is open (`RFC5-7` §8 q1,
   `rfcs/RFC-0005/admission-and-boundary.md:393`). **RFC-0010 as written cannot
   operate at V0 today, by its own clause.** This is a virtue of the drafting, not
   a defect — and it is an argument the placement recommendation should adopt
   rather than work around.
2. **Reconciliation, the only independent completion establisher, is a V1
   computation.** `RFC2-19` and `RFC8-29`: V0 renders reconciliation absence
   honestly; V1 computes. A mission whose completion predicate must be
   evidence-established has, at V0, no gate to be established *by* for the whole
   class of work that matters.
3. **The extension register already gates the safety machinery past V0.**
   `07-AUTONOMY-EXTENSION-REGISTER.md:14-19` marks agent/fleet profile registry,
   shadow mode, policy regression tests, checkpoint/resume, and the incident
   loop all as "**required before V1 autonomy**", and compensation/rollback as
   "required before auto-merge/deploy". Every prerequisite for running a mission
   safely is itself scheduled after V0.

### 10.4 Recommendation

**Bounded Missions belong in V1. What belongs in V0 is strictly three things:**

1. **The mission and envelope *record* schema** — so a mission is a first-class
   identified entity from the start and nothing has to be retrofitted
   (`RFC10-4`, `RFC10-7`).
2. **The approval ceremony and the external audit trail** (`RFC10-9`,
   `RFC5-25`) — this is the A1 correlation mechanism the whole corpus is
   currently waiting on, and building it under Mission Control's banner is the
   right forcing function.
3. **Read-only mission rendering** — missions and Attention Items served through
   the same semantic API with human/machine parity (`RFC10-2`, `RFC6-13/14`).

**What must not ship at V0:** unattended multi-cycle execution; child-mission
decomposition; any autonomy level above the V0 ceiling below; and any mission
whose completion is established by the executing party.

### 10.5 The V0 autonomy ceiling, stated concretely

**V0 ceiling: propose-only, defined as *no effect outside `.syzygy/**` and
`openspec/**` that is not itself an owner-signed dispatch of one work item*.**

Concretely, at V0 a mission may:

- read observed sources under existing observation consent;
- compile context packets and run agents, **within a budget that is reserved at
  dispatch**;
- write drafts and proposals into `.syzygy/**` and `openspec/**`, rendered
  unadopted (`v1.md:44-50`, `RFC3-16`);
- **submit** acts for owner attendance (`RFC10-3`, `RFC-0010:101-104`);
- dispatch **one** scheduled work item per owner-signed delta — v1.md's own
  propagation slice, no more.

At V0 a mission may **not**: open a pull request; merge; deploy; execute any
`RFC5-22` destructive-operation class, whether or not the profile
standing-approved it; mint a child mission; or take the `running → completed`
transition on its own authority.

**Explicitly: no autonomous merge, and not even autonomous PR-opening.** The
open-PR level deserves comment because it is the tempting middle: a PR looks
reversible. It is not — it consumes reviewer attention, it is externally
visible, on many configurations it triggers CI spend and deploy previews, and
under `RFC5-22` a push to a remote is a **default-blocked destructive class**
precisely because its effects outlast the sandbox. Open-PR belongs at V1, gated
on the shadow-mode and policy-regression rows of the extension register
(`07-AUTONOMY-EXTENSION-REGISTER.md:15-16`), and auto-merge belongs behind the
compensation/rollback row (`:17`).

---

## 11. D3 AMENDMENT SUFFICIENCY

**The VIS-4 test.** `doctrine/vision.md:72-74`:

> - **Not autonomous.** The loop is human-triggered; autonomy beyond VIS-4's
>   stated bounds is licensed only through the mechanism VIS-4 names, never by
>   reinterpretation.

and `vision.md:127-131` names the mechanism: "both an accepted adjudication RFC
… *and* the owner's explicit doctrine amendment recording that the gate opens;
RFC acceptance alone never opens it."

**The question:** do D3 + RFC-0010 satisfy that mechanism, or assume the
conclusion?

### 11.1 What the packet gets right

The packet is unusually honest, and three things deserve credit before the
criticism:

- It **poses the D4 question against itself** (`D3:31-44`) rather than burying
  it, and states plainly that if the owner rules the other way, "an accepted
  adjudication RFC is **also** required, this amendment alone is insufficient".
- It states the **consequence of declining** without softening
  (`D3:26-29`): "RFC-0010 can be *accepted* without this amendment … but Mission
  Control cannot lawfully *operate*."
- It **preserves the load-bearing half** of the bullet untouched (`D3:130-132`),
  and correctly identifies that half as what "forecloses reading a mission as its
  own licensing mechanism".
- Its diagnosis of the actual defect is correct: the obstacle is
  `architecture.md`'s one-pass grain, not `vision.md`'s bullet
  (`D3:20-24`, corroborated at `MISSION-CONTROL-REVIEW.md:213-228`).

### 11.2 Where it assumes the conclusion

**The proposed `vision.md` text answers D4 inside the one sentence whose second
half exists to prevent exactly that.** `D3:104-110` inserts, before the
semicolon:

> - **Not autonomous.** The loop is human-triggered **(a trigger may authorize
>   one propagate/sync pass or one bounded, envelope-limited mission — see
>   architecture.md; …)**; autonomy beyond VIS-4's stated bounds is licensed only
>   through the mechanism VIS-4 names, never by reinterpretation.

Read the amended bullet as a fresh reader must. The first half now *declares* a
bounded mission to be a species of human trigger. The second half says autonomy
beyond VIS-4's bounds needs VIS-4's mechanism. Having placed missions inside the
first half **by definition**, the second half can never reach them — not because
the argument was made and won, but because the amendment stipulated the
classification in the same breath.

The packet argues the classification separately and defensibly at `D3:31-44` (a
mission delegates execution inside every gate, never adoption or an always-human
class). That argument may well be right — I think it probably is. But **it lives
in packet prose that is explicitly not proposed for insertion**, while the
*conclusion* is what gets adopted into doctrine. The owner is asked to adopt a
sentence that settles D4, in a packet that says D4 is unsettled and is the
owner's to rule (`D3:40-44`, `D3:181-185`). Those two things cannot both be true
of one act.

This is not a drafting quibble. The second half of that bullet is, on the
packet's own account (`D3:130-132`), "load-bearing: it forecloses reading a
mission as its own licensing mechanism". An insertion that pre-classifies
missions is the most efficient possible way to defeat it.

### 11.3 The under-disclosed consequence: doctrine floors everything except the ceiling

`D3:65-78` proposes for `architecture.md`:

> …strictly inside an explicit **autonomy envelope** that agents can never widen,
> ending at the envelope's own terminal conditions. An envelope is owner-approved
> and states at minimum the mission's objective, its resource and time bounds,
> its risk limits, the surfaces and change classes it may not touch, and its stop
> and completion conditions; **the exact envelope fields are contract material,
> not doctrine.**

The move from a mirrored field list to a floor-plus-pointer is right, and the
reasoning at `D3:150` (one norm, one home) is correct. But observe what the floor
**omits**: it requires an envelope to state objective, resource bounds, time
bounds, risk limits, untouchable surfaces, stop and completion conditions. It
does **not** require the envelope to state a **maximum autonomy level**, and it
does not floor that level anywhere.

Consequence: once D3 is adopted, "how autonomous may a mission be?" is
permanently a **contract** question. VIS-4's always-human classes survive — but
merge and deploy are not VIS-4 classes. `RFC10-7`'s propose-only cap
(`RFC-0010:174-178`) is the only thing standing between doctrine and
autonomous deploy, and it is (a) in a candidate contract, (b) self-described as
temporary, (c) bound to an undefined term (§10.1), and (d) liftable by an owner
act on §8 q2 that is *not* framed as a doctrine amendment.

That is a material consequence of act 5 and it is disclosed nowhere in the
packet.

### 11.4 The sequencing residual

`D3:169-178` states the act-5-before-act-1 hazard accurately: adopted doctrine
would carry the terms *bounded mission* and *autonomy envelope* with no accepted
contract defining either, and — because `D3:150` deliberately names no contract
— with nothing pointing at where a definition would live. The packet's
recommendation (`D3:187-190`, act 1 first) is correct and I endorse it. Its
claim that "**Operational risk today is nil**" is also correct, since no
implementation exists.

The residual is not operational, it is that the D4 ruling changes the act
*order* from preference to requirement (`D3:181-185`), and the amendment text
pre-answers D4 (§11.2). So the owner is being asked to perform act 5 using a
text whose adoption would make the ordering analysis moot in the direction the
text chose.

### 11.5 Judgment

**D3 + RFC-0010 are substantively sufficient and procedurally not.** The
substance is right: the amendment fixes trigger grain and nothing else; the
gate-preservation sentence is genuine; VIS-4's classes and the bullet's second
half survive. The procedure assumes the conclusion in the adopted text, and the
floor omits the one bound (autonomy level) that would keep the question in
doctrine where the owner could see it next time.

---

# VERDICT

VERDICT: REVISE

---

## Findings, with proposed clause text

Proposed text is drafted in the corpus's voice for insertion **by owner act
after act 1**, since RFC-0010 is inside the act-1 frozen digest set and editing
it now churns the manifest. Where a finding can be closed by an owner *ruling*
rather than by clause text (F1's §8 q2, F10's D4), that is noted.

---

### [Blocking] F1 — The propose-only cap binds to an undefined term

`RFC-0010:159-161` declares the autonomy-level vocabulary unenumerated and
offers `propose-only` in a parenthetical `e.g.`; `RFC-0010:174-178` then makes
that same word the universal cap. `propose-only` is defined nowhere in the
corpus. Three deferred findings (F3/F4 of the prior review, and half of this
one) rest their "inert today" disposition on this cap.

**Proposed clause text — append to `RFC10-7`:**

> **`propose-only`, defined.** Until the autonomy-level vocabulary is enumerated
> by owner act, `propose-only` means exactly: a mission may read consented
> sources, compile context packets, run agents within its reserved budget, and
> author drafts, proposals, and submissions into `.syzygy/**` and `openspec/**`
> rendered unadopted (RFC3-16). It may **not** cause any effect outside those two
> namespaces: no version-control push or pull request, no merge, no deploy, no
> package or artifact publication, no mutation of an external service or
> database, and no RFC5-22 destructive-operation class **whether or not the
> granted execution profile standing-approved it**. Egress to a model provider
> remains permitted only under an RFC5-14 consent record naming the provider and
> content classes. A level above `propose-only` is inoperative until both the
> vocabulary is enumerated and each level's permitted effect set is stated.

---

### [Blocking] F2 — No budget reservation at dispatch; sanctioned unbounded overrun; no rule under cost uncertainty

`RFC10-7:164-165` states budgets as bare numbers. `reserve`, `committed`,
`spent`, `released`, `overrun` are **zero-occurrence** in RFC-0010. The
debit-at-grant invariant exists only for child missions (`RFC-0010:194-198`).
`RFC10-11:252-254` permits in-flight work to complete past an exhausted bound
with no size limit and no overrun record. `RFC8-19` guarantees spend will be
partly Unknown and forbids treating Unknown as zero; nothing states what the
runtime does then.

**Proposed clause text — new `RFC10-17`:**

> **RFC10-17. Budget is reserved, not merely observed.** Every budget in an
> envelope is accounted in five distinct quantities: **authorized** (the owner
> act's figure), **reserved** (committed at dispatch to work not yet complete),
> **spent** (measured consumption), **released** (reserved-but-unspent, returned
> on completion or termination), and **overrun** (spend exceeding authorized).
> **No work is dispatched without reserving its declared maximum cost against the
> envelope at dispatch time**, and reserved + spent never exceeds authorized —
> the sibling-sum invariant RFC10-8 states for child missions, applied to every
> dispatch. Work whose maximum cost cannot be declared is not dispatchable under
> that budget. **Where measured spend against a bound is Unknown (RFC8-19,
> RFC2-23), the bound is treated as reached**: the mission transitions per
> RFC10-11 and an Attention Item states the measurement gap. Any overrun is
> recorded as attributable evidence against the mission and mints its own
> Attention Item; a mission record showing a respected bound with unrecorded
> overrun is a violation of this clause.

**Consequential amendment to `RFC10-11`** — replace the final sentence
(`RFC-0010:252-254`):

> Partial work already lawfully dispatched completes or checkpoints per the
> envelope's recovery obligations, **strictly within the budget reserved for it
> at dispatch (RFC10-17); completion headroom is reserved in advance or the work
> is checkpointed and halted, never funded by spending past the exhausted
> bound.**

---

### [Blocking] F3 — Completion is self-adjudicable: no decider is named

`RFC10-5:134-138` names a human decider for exit from `blocked` under
RFC10-8/RFC10-11 and for no other transition; `running → completed` therefore has
no named decider. `RFC10-6:143-152` binds the predicate to evidence in the
passive voice. Mission state is not typed as a Claim anywhere, so `RFC2-25`'s
gate-backed-only rule does not evidently bind it (cf. `RFC8-12`'s explicit
not-a-Claim ruling for work state). "The strongest **applicable** tier"
(`RFC-0010:149-150`) leaves applicability to the executing agent.

**Proposed clause text — new `RFC10-18`:**

> **RFC10-18. Completion is reported by the executor and established by another.**
> A mission's executing agents, fleets, and workers **may report** that the
> completion predicate is satisfied and **may never establish it**. The
> `running → completed` transition is taken only by (a) an owner act, or (b) a
> declared, owner-approved evaluation that is independent of the executing
> principal under RFC11-10's independence property and whose supporting evidence
> is `gate-backed` (RFC2-25) — never by the principal that performed the work,
> and never by a principal routed by that principal. A mission's terminal state
> is an **authorization-bearing determination** under RFC3-16(a) where it
> discharges an owner act's objective. Where no independent establisher is
> available for a mission's objective class — including wherever RFC2-19 leaves
> reconciliation uncomputed — the mission terminates as `blocked` with an
> Attention Item, never as `completed`. An unstated minimum evidence tier means
> `gate-backed`; "the strongest applicable tier" is never a judgment the
> executing principal makes for itself.

---

### [Blocking] F4 — No reversibility declaration, no compensation, no failure semantics, no recovery owner, no resumption

`rollback`, `compensat`, `revert`, `irreversib` are **zero-occurrence** in
RFC-0010; `resume`/`resumption` **zero-occurrence**; `reversib` occurs once, on
the Attention Item (`RFC-0010:266`), never on the envelope. Every failure exit in
the contract halts the future and none addresses the past. `failed`
(`RFC-0010:127`) obliges nothing. Envelopes inherit `RFC5-22` standing-approved
destructive classes by profile reference without naming them.

**Proposed clause text — new `RFC10-19`:**

> **RFC10-19. Effects are classified before they are authorized.** Every effect
> class an envelope permits is declared **reversible**, **compensatable** (with
> the compensating action named), or **irreversible**. An effect class not so
> classified is not authorized — the unstated-is-narrowest rule of RFC10-7
> applied to effects. An envelope permitting any irreversible class states that
> class explicitly on its own face; **a destructive-operation class reaches a
> mission only where the envelope names it, never by inheritance from an
> execution profile's standing approval (RFC5-22)**. Where a mission enters
> `failed`, `cancelled`, or `expired` with effects already applied: every
> compensatable effect's compensating action is attempted and its outcome
> recorded as evidence; every irreversible effect is enumerated in a single
> Attention Item naming what cannot be undone; and the mission's terminal reason
> (RFC10-5) states the reversibility disposition of every applied effect. **Pause
> is not rollback**: transitioning to `paused` or `blocked` discharges no
> obligation under this clause. **A named recovery owner** — the owner, or a
> principal the envelope designates — is bound at approval time, and resumption
> from `paused` re-verifies the pinned inputs (RFC10-4), the remaining reserved
> budget (RFC10-17), and the envelope's continued act provenance (RFC10-9) before
> any dispatch.

---

### [Blocking] F5 — The unstated-is-narrowest rule covers grants, not obligations

`RFC-0010:169-171` reads: "An envelope field left unstated is the *narrowest*
reading, never the widest: absence of a budget is zero delegated spend of that
kind, absence of a path grant is no write access." Both worked examples are
**grants**. Applied to the envelope's obligation-shaped fields — "required gates
and independent reviews", "evidence and reconciliation requirements", "checkpoint
and recovery obligations", "escalation triggers" (`RFC-0010:166-169`) — the
"narrowest reading" of an *obligation* is the reading a self-interested fleet
prefers: none. Every obligation field currently fails **open**.

**Proposed clause text — insert into `RFC10-7` after the narrowest-reading
sentence:**

> The rule applies to grants and obligations in opposite directions and to the
> same effect: **an unstated grant is the narrowest grant; an unstated obligation
> is the strictest obligation.** Absence of a declared gate set means every
> otherwise-applicable gate is required; absence of declared checkpoint and
> recovery obligations means no effect outside `.syzygy/**` and `openspec/**` is
> authorized until they are declared; absence of declared escalation triggers
> means RFC10-13's minimum set binds in full. No field's absence ever relaxes a
> duty.

---

### [Blocking] F6 — Stop does not stop running work, has no latency bound, and guarantees no consistency

No clause binds mission `cancel`/`stop` to termination of in-flight runs;
`RFC10-5:127` states the state and no effect. The only sentence about in-flight
work says it **completes** (`RFC-0010:252-254`). `atomic` is **zero-occurrence**.
The real kill switches (`RFC5-21`, `RFC5-23`) hang off *different acts* —
execution-consent revocation — that nothing routes a mission stop to.

**Proposed clause text — new `RFC10-20`:**

> **RFC10-20. What stop guarantees.** A human stop, cancellation, or expiry of a
> mission (RFC10-5) has three effects, all immediate at the act (RFC5-11's
> acts-versus-claims rule): **(a)** no further work is dispatched and no further
> Syzygy-mediated act is admitted under that mission; **(b)** every run Syzygy
> launched under the mission is terminated together with its descendants, through
> the kill switch RFC5-21 requires of every isolation class — a stop that leaves
> Syzygy-launched runs executing does not conform; **(c)** each terminated run's
> partial state is checkpointed and recorded as evidence, and any effect already
> applied is classified and dispositioned under RFC10-19. The envelope declares a
> **maximum stop latency**; an undeclared latency means stop is synchronous —
> the act does not return until (a) and (b) hold. Effects produced outside
> Syzygy's mediation by externally-granted credentials are **not** covered by
> (b); the mission's stop record states that boundary explicitly rather than
> implying a completeness the runtime cannot deliver (RFC10-10).

---

### [Blocking] F7 — A cross-project composite has no rule selecting whose egress consent governs

`RFC5-15` (`rfcs/RFC-0005/consent-egress-secrets.md:154-160`) fixes the check as
"(provider, content classes, **project**)" — singular. `RFC5-12` makes consent
one record per *(Project, provider)*. `RFC5-14` supplies a composition rule for
**classes** and none for **projects**. `RFC11-1` identifies a packet's "project
and workspace identity" — singular. RFC-0010 creates, for the first time in the
corpus, an artifact that spans projects. A composite embedding B's
`code-content` can egress under A's consent with every field of the three-part
check reading as satisfied.

**Proposed clause text — new `RFC10-21`:**

> **RFC10-21. Cross-project composites carry every embedded project's consent
> requirement.** A context packet, prompt, summary, embedding, or any other
> composite assembled under a mission spanning more than one project is subject,
> at the RFC5-15 choke point, to the egress-consent record of **every project
> whose content it embeds** — not one of them, and never the project the
> composing step names for itself. A composite embedding content from a project
> for which the naming (project, provider) consent is absent, not in force, or of
> unverifiable provenance **fails closed and the refusal renders**, exactly as an
> undeterminable content class does (RFC5-14). Evidence gathered within one
> project never satisfies a completion predicate scoped to another. Where the
> workspace governance store's per-project budget and an envelope's budget both
> bind (RFC10-15, RFC10-7), **the lesser binds**, and a portfolio mission's spend
> against a project is debited from that project's budget as well as the
> mission's.

---

### [Blocking] F8 — The attention queue is unbounded in every dimension flooding exploits

`RFC10-12` binds all eight required Attention Item fields — verified 8/8 against
the live file. `RFC10-13:272-274` forbids streaming but supplies no volume
metric, no threshold, and no decider. No rate limit, no priority class, no
deduplication, no queue-depth bound, no overflow behavior; SLA and batching are
deferred at `RFC-0010:387`. Expiry is required but its **duration** is unbounded.
Combined with the (correct) anti-bulk rule, unbounded volume is a guaranteed
denial of owner attention; combined with safe-expiry, it is a reliable liveness
attack that requires no widening.

**Proposed clause text — new `RFC10-22`:**

> **RFC10-22. The attention queue is bounded.** Every Attention Item additionally
> carries an **urgency class** from a closed vocabulary fixed at surface
> specification, and the **envelope bound, gate, or protected surface it
> implicates** where one exists. Every envelope declares a **maximum outstanding
> attention count** and a **maximum item rate** for the missions under it; an
> undeclared maximum means one outstanding item — the narrowest reading (RFC10-7,
> as amended by F5). **On reaching either bound the mission pauses rather than
> enqueueing further items**: a mission may not convert the owner's finite
> attention into throughput. Items presenting the same decision are deduplicated
> into one item recording its multiplicity. Every item's expiry falls within a
> declared maximum beyond which its stated default is no longer presumed safe;
> an item whose expiry exceeds that maximum is not well-formed.

---

### [Blocking] F9 — Two disagreeing evidence sources have no rule

`RFC2-15`/`RFC1-21` scope Contradiction to co-unsatisfiable **claims**, not
evidence artifacts. `RFC2-25`'s tier ordering resolves only cross-tier cases.
`RFC10-13`'s "evidence unable to establish progress" is about inability, not
disagreement, and an agent holding one confirming artifact reads it as unfired.
Sweeps for `disagree`, `conflict`, `precedence`, `tie-break` find no
evidence-level rule anywhere in `rfcs/**`.

**Proposed clause text — append to `RFC10-6`:**

> Where two or more admitted evidence artifacts bearing on one completion
> predicate support opposing conclusions, **the predicate is not satisfied**: the
> disagreement is recorded as evidence, the predicate's conclusion renders
> Unknown, and the condition is an escalation trigger under RFC10-13. It is never
> resolved by recency, by tier where the tiers are equal, by the executing
> principal's selection among sources, or by any precedence rule. Where the
> disagreeing artifacts support co-unsatisfiable authoritative claims, RFC2-15's
> Contradiction machinery governs and owner adjudication is the only exit.

---

### [Blocking] F10 — D3's proposed `vision.md` text pre-answers D4, and its doctrine floor omits an autonomy ceiling

`D3:104-110` inserts, before the semicolon of the "Not autonomous" bullet, text
declaring a bounded mission to be a species of human trigger — thereby placing
missions inside VIS-4's bounds **by stipulation**, in the one sentence whose
second half exists to foreclose exactly that move (`D3:130-132` says so
itself). The packet argues the classification properly at `D3:31-44`, but that
argument is packet prose that is not adopted, while the conclusion is.
Separately, the `architecture.md` floor (`D3:65-78`) requires objective,
resource and time bounds, risk limits, untouchable surfaces, stop and completion
conditions — and **not** a maximum autonomy level, permanently moving "how
autonomous may a mission be" out of doctrine.

**This finding closes by an owner ruling, not only by text.** Rule D4 first;
then adopt whichever text the ruling implies.

**Proposed replacement for D3 §1.2's insertion (if D4 is ruled "a bounded
mission is not autonomy beyond VIS-4's bounds"):**

> - **Not autonomous.** The loop is human-triggered — a trigger may authorize one
>   propagate/sync pass or one bounded, envelope-limited mission
>   (architecture.md). Either grain is a deliberate human act; a mission is
>   authority to proceed inside every gate and never to skip one; and expiry or
>   exhaustion of a mission's envelope halts, never extends, its authority.
>   **A mission delegates execution and never adoption, approval, envelope
>   widening, or any always-human class, and is for that reason inside VIS-4's
>   stated bounds rather than an exception to them.** Autonomy beyond VIS-4's
>   stated bounds is licensed only through the mechanism VIS-4 names, never by
>   reinterpretation.

The bolded sentence states the *reason* rather than assuming it, so a fresh
reader can see the classification is an argued position and can see what would
falsify it. If D4 is ruled the other way, no `vision.md` insertion is lawful
without an accepted adjudication RFC (`vision.md:127-131`), and act 1 precedes
act 5 as a requirement.

**Proposed addition to D3 §1.1's `architecture.md` insertion, one clause:**

> …the exact envelope fields are contract material, not doctrine — **except that
> an envelope always states a maximum autonomy level, and raising the level at
> which merges or deployments may occur without a human act is itself a doctrine
> amendment event.**

---

### [Blocking] F11 — The §14 coverage review's stated digest never matched the artifact

`round-2026-08/MISSION-CONTROL-REVIEW.md:16` records RFC-0010 at
`8481335836115c…`; the live file, the manifest entry, and the only commit ever to
contain the file all read `dfcedbbf187cfc…`. `:21-23` then asserts `[Observed]`
that the live digest equals the manifest entry. The review's coverage totals
(14/2/0 and 8/0/0) are the evidence that RFC-0010 satisfies charter §14.

**Disposition:** re-run the review against the live digest, or correct the digest
table and re-derive the `[Observed]` label, before those totals are cited in the
act-1 offering. Do not edit the stored raw output — allowlist or supersede it. I
independently re-derived both totals against the live file and **agree with the
substantive marks**, which limits the damage to provenance; but the provenance
is what act 1 is being asked to rely on.

---

### [Non-blocking] F12 — `RFC10-4`'s stale-input escalation has a rule and no decider

`RFC-0010:116-119` states the rule; nothing names who detects a pinned-input
change, at what cadence, or whether the mission halts pending the answer.
`RFC11-6`'s staleness gate is compile-time only; `RFC11-2`'s re-mint rule is
permissive; `stale` is zero-occurrence in RFC-0010. The path self-heals via
`RFC10-12` safe-expiry **only if the item is raised at all**.

**Proposed clause text — append to `RFC10-4`:**

> Detection is Mission Control's, never the executing agent's: the mission's
> pinned input digests are re-verified at every dispatch and at a declared
> maximum interval; an undeclared interval means re-verification at every
> dispatch. A packet consumed by a mission-spawned run carries a **maximum age**
> beyond which it is recompiled (RFC11-2) rather than reused. On a detected
> change the mission transitions to `blocked` pending the escalation's
> resolution; it does not continue against superseded inputs while the item is
> open.

---

### [Non-blocking] F13 — Escalation-sourced `blocked` states have no human-exit rule

`RFC10-5:134-138` scopes the human-resolution requirement to blocks "where the
block arose under RFC10-8 or RFC10-11". A block arising from an `RFC10-13`
escalation is not covered, so on the clause's face an agent's "condition cleared"
assertion takes that transition. Weak in practice — a wrong self-certification is
re-refused at `RFC10-10`'s preventive choke point — but the exception's scoping
is what makes the general rule readable as narrow.

**Proposed amendment to `RFC10-5`** — replace "where the block arose under
RFC10-8 or RFC10-11" with:

> where the block arose under RFC10-8, RFC10-11, **or an RFC10-13 escalation
> whose Attention Item remains unresolved**

---

### [Non-blocking] F14 — The objective and completion predicate are not "bounds", so the anti-reinterpretation rule may not reach them

`RFC10-8:186` and `RFC10-7:171-174` both scope narrow-resolution and the
escalation trigger to a "**bound**". The objective (`RFC10-4`) and the completion
predicate (`RFC10-7`) are envelope fields but not obviously bounds. An agent that
reinterprets its objective downward until the predicate is met has widened no
bound. This is the residual self-widening route (§6), and with F3 closed it is
substantially defanged.

**Proposed amendment to `RFC10-7`** — after "genuine ambiguity in a load-bearing
bound is an escalation trigger", insert:

> For this rule and for RFC10-8's anti-reinterpretation limb, **"bound" includes
> the mission's objective and its completion predicate**: narrowing what the
> objective demands, or lowering what the predicate accepts, is a widening of the
> envelope and is an owner act.

---

### [Non-blocking] F15 — Context-packet identity reaches missions only through unnumbered §5 prose

`RFC-0010:371-372` carries "every mission-spawned agent run receives a governed
context packet; the envelope is a mandatory packet input" in the **integration
section**, which has no clause ID. `RFC11-1`
(`rfcs/RFC-0011-context-compiler.md:79-82`) carries the obligation independently,
so nothing is lost — but `RFC11-1` itself has context compiled by selecting "the
exact RFC clauses, **by clause ID**", and an obligation with no clause ID cannot
be selected by one. A compilation over RFC-0010's clauses alone would not surface
it. Concurs with `MISSION-CONTROL-REVIEW.md:417` (F5); recorded independently.

**Proposed clause text — append to `RFC10-6`:**

> Every mission-spawned agent run receives a governed context packet (RFC11-1),
> and the envelope is a mandatory packet input; a mission-spawned run dispatched
> without one is a violation of this clause as well as of RFC11-3.

---

### [Non-blocking] F16 — Portfolio and per-mission concurrency have no composition rule

`RFC10-15:297-299` puts "fleet capacity and concurrency" in the workspace store;
`RFC10-7:165` puts concurrency in the envelope. No clause states which binds.
Derivable (RFC10-8 forbids widening, so the lesser binds), but stated nowhere.
Closed by F7's proposed "**the lesser binds**" sentence if that text is adopted;
otherwise it needs its own. Concurs with `MISSION-CONTROL-REVIEW.md:419` (F7).

---

### [Non-blocking] F17 — `Recovery Action` remains an un-reified entity

RFC-0010 states recovery as an obligation (`RFC-0010:167-168`, `253`) and names
no record it produces. Entities without names are invented locally by
implementers, and the recovery record is the one that would carry the
compensating-action outcome F4 requires. Independently reached; the same
observation is carried forward at `MISSION-CONTROL-REVIEW.md:423-427`. If F4's
`RFC10-19` is adopted, the record it requires should be named there rather than
left to surface specification.

---

## Blocking seams, in one list

For foundational acceptance (act 1), the seams I judge **blocking** are
**F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11**.

F1 is the highest-leverage single fix: it is one sentence, and closing it
converts F4's and F8's exposure from "live today" to "genuinely inert under the
cap". F2, F3, and F6 are the three that bite **now**, under the cap, on day one —
because propose-only missions still spend money, still declare themselves
complete, and still cannot be reliably stopped.

*End of raw review. Nothing here rules on any act; every act remains the
owner's.*
