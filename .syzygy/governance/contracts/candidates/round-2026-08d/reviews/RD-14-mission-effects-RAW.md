(part 1/2)

Reviewer: mission-effects (RD-14)
Date: 2026-08-09
Commit: 771965c
Files read:

- `C/rfcs/RFC-0010/budget-reservation.md` (170 lines) — RFC10-17, RFC10-17(a)
- `C/rfcs/RFC-0010/effects-recovery-and-stop.md` (319) — RFC10-18, RFC10-18(a), RFC10-19, RFC10-19(a), RFC10-20, RFC10-23
- `C/rfcs/RFC-0010/prevention-envelope-and-attention.md` (303) — RFC10-7..RFC10-13, RFC10-22
- `C/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md` (229) — RFC10-5 read as the lifecycle authority the stop and release rules key on
- `C/rfcs/RFC-0010/portfolio-and-cross-project-consent.md` (95) — RFC10-15, RFC10-21
- `C/rfcs/RFC-0010/README.md` (209) — clause map, plane seam
- `C/rfcs/RFC-0005/admission-and-boundary.md` (458) — RFC5-1..RFC5-11, RFC5-24..RFC5-27
- `C/rfcs/RFC-0005/execution-profiles.md` (271) — RFC5-18..RFC5-23
- `C/rfcs/RFC-0005/consent-egress-secrets.md` (291) — RFC5-12..RFC5-17
- `.syzygy/governance/doctrine/security.md`, `vision.md` (SEC-2, SEC-4, VIS-4 excerpts)

**Scope correction to the brief.** [Observed] The brief located "the RFC5-21 launch gate and RFC5-15 per-transmission predicate" in `RFC-0005/admission-and-boundary.md`. That module's own front matter reads `clauses: RFC5-1..RFC5-11, RFC5-24..RFC5-27`, and its closing line states "Clauses RFC5-1 … RFC5-11 and RFC5-24 … RFC5-27." RFC5-15 lives in `consent-egress-secrets.md`; RFC5-21 in `execution-profiles.md`. I read both rather than accept the cited clauses unread — findings 3 and 5 depend on their actual text.

---

## THE QUESTION — can a bounded, autonomous Mission cause an unrecoverable or unauthorized outcome without an owner act?

**YES.** One route is confirmed and closes only by a clause edit (finding 1); a second is open on the prevention side and closed only on the detection side (finding 3). Four of the seven surfaces I attacked are genuinely closed, and closed well.

Routes examined, with the outcome of each:

1. **Cost enforcement — CLOSED.** [Observed] RFC10-17 no longer states the invariant over the ledger alone. It states it over admission: "**A reservation admits a dispatch only where it is bound to an enforced limit.** … **A declared maximum with no enforced limit admits nothing.**" The four-kind classification is exhaustive over the enforceability space (hard-enforceable / provider-quota-enforceable / monitoring-only / non-delegable), and monitoring-only is disposed of by the same sentence: no enforced limit, so no admission. RFC10-10's demand — "Mission Control MUST prevent every act it mediates from exceeding the approved authority and resource envelope" — is reconciled explicitly: "**For resource consumption this prevention is discharged by RFC10-17's enforced-limit admission rule**." [Inferred] The two sides now agree, and the residual-overrun rule keeps the ledger honest without letting the ledger substitute for prevention. Findings 5 and 6 are seam defects on this route, not holes in it.
2. **Effect classes — CLOSED.** [Observed] The class space is total by construction: "**any effect class that does not meet that definition and is not declared irreversible is compensatable by force. There is no generic `reversible` class.**" `atomically-reversible` is defined so narrowly that no risky effect fits — "reversal is performed automatically and atomically by the mediating transaction as part of the same act, such that no post-hoc action exists to attempt" — and it is "evidenced at classification time — never an assertion of the envelope author," with a runtime backstop reclassifying unverifiable reversals as irreversible. [Inferred] I could not construct a class an implementer would want and find undefined. Finding 2 is about *funding*, not about the taxonomy.
3. **Provider egress — CLOSED as a predicate, OPEN as a route.** [Observed] The predicate answers coherently: dimension (iii) disclosure is outside it, pre-authorized by the RFC5-14 consent record, and "Disclosure without a covering consent, or outside the consent's named content classes, is an external mutation for this predicate." Neither answer breaks the contract, and RFC10-23 forbids rendering an egress-only mission as "no effects." The route that remains open is finding 3: a Syzygy-granted egress path that never reaches the RFC5-15 choke point the predicate and RFC10-21 both assume.
4. **Stop — CLOSED.** [Observed] Finite: RFC10-20(d) declares a maximum stop latency with a stated finite default chain terminating in the wall-clock budget "every runnable mission has." Hang is classified: "**a hang is a failed stop, and this third exit is stated so that no reading leaves the act blocking forever**." A mission cannot survive its own kill: limb (b) propagates "transitively to every child mission derived from it (RFC10-8) and to their descendants," with "the **enumeration of the descendant missions reached**" part of the record. The isolation-class admission requirement is stated as this clause's own and not misattributed to RFC5-21 — [Observed] correctly, since RFC5-21's floor names "a kill switch terminating the run and its descendants" and no reporting interval. Finding 4 is a wording contradiction on this clause, not a gap.
5. **Compensation and rollback — CLOSED on containment, OPEN on sizing.** [Observed] Recovery cannot exceed the envelope: `recovery_reserve` is carved out of `authorized`, RFC10-11 fires on `authorized − recovery_reserve`, "work never dispatches into the reserve," and insufficiency escalates rather than borrows. Who pays is answered. Finding 2 is that the reserve is sized against the wrong denominator.
6. **Partial failure and terminal adjudication — OPEN.** Finding 1. A mission can end with effects applied and unadjudicated, and the effects need not even exist yet at the terminal record.
7. **Overrun — CLOSED.** [Observed] Overrun is a residual with exactly three enumerated non-mediated sources, "an overrun from any other source … is a violation of this clause," and "Every overrun is recorded as attributable evidence against the mission and mints its own Attention Item." No resource kind admits unbounded overrun without an item. Finding 7 is a narrow routing ambiguity for an item minted after the terminal record.

---

## Findings

### 1. A mission reaching `failed` by RFC10-18 or RFC10-18(a) neither halts dispatch nor terminates its in-flight runs, and RFC10-17(a) releases their reservation in full — severity: **blocking**

**Anchor — RFC10-20** (`effects-recovery-and-stop.md`):

> "**RFC10-20. What stop guarantees.** A human **stop, cancellation, or expiry** of a mission (RFC10-5) has three effects, all immediate at the act: **(a)** no further work is dispatched and no further Syzygy-mediated act is admitted under that mission; **(b)** every run Syzygy launched under the mission is terminated together with its descendants…"

**Anchor — RFC10-18(a)** (same file):

> "**Unknown fails closed: where whether effects were applied is Unknown, effects are treated as applied** … The mission **enters `failed`**, RFC10-19's duties fire…"

**Anchor — RFC10-17(a)** (`budget-reservation.md`), the `failed` row:

> "| `failed` | released **in full** after RFC10-19's compensating actions are attempted…"

compared with the row that does carry the guard:

> "| unrecoverable stop — RFC10-20 limb (b) not achieved | released at the stop record **except** for the runs that did not terminate, whose reservations are retained and **named individually**: **a reservation may not be returned while the work it funds may still spend** |"

**Sweep.** [Observed] Denominator: all six RFC-0010 module files, 1,325 lines, searched two ways — line-oriented Python `re` and a second pass over whitespace-normalized whole-file text (the first method misses the clause because `no / further work is dispatched` is line-wrapped; the second catches it). Results: the string "no further work is dispatched" occurs **once** in the package, in RFC10-20, whose trigger set is exactly "stop, cancellation, or expiry." `` `failed` `` occurs at nine sites; the four that are transitions into it — RFC10-18's effects branch, RFC10-18(a)'s Unknown rule, RFC10-19's disposition trigger, RFC10-20(d) — impose **duties** and none imposes termination of in-flight runs or a dispatch halt. No clause in the package keys run termination or dispatch cessation to `failed`.

**Failure scenario.** [Inferred, from the quoted text] A mission is approved with a decomposition grant and three concurrent runs. Run 1 reports the completion predicate satisfied. The effects-determination evaluator finds the granted tools reach beyond declared adapter coverage, so RFC10-18(a)'s predicate resolves Unknown; the fail-closed rule fires and the mission **enters `failed`**. RFC10-19's duties fire *at that transition* — "Where a mission enters `failed`, `cancelled`, or `expired` with effects already applied: every compensatable effect's compensating action is attempted … and the mission's terminal reason (RFC10-5) states the disposition of every applied effect." The terminal reason is written once. Runs 2 and 3 were never named by a stop act, so limb (b) never fires; nothing bars their next dispatch, because limb (a) is likewise keyed to a stop. RFC10-17(a) releases their reservation **in full**, returning headroom that the admission inequality `reserved_remaining + spent ≤ authorized − recovery_reserve` will now admit further dispatch against. Runs 2 and 3 continue, spend against released budget, and **apply effects after the terminal record** — effects that are never classified, never compensated, and absent from a terminal reason already written. This is precisely the outcome RFC10-19 was built to prevent and precisely the guard the unrecoverable-stop row states and the `failed` row omits.

**Anticipated defence, and why it fails.** One may argue that terminality implies no dispatch. [Observed] The contract does not treat that as implied: `cancelled` and `expired` are already terminal states under RFC10-5's vocabulary, and RFC10-20 still states limb (a) for them, and still says "A stop record reporting (a) and (b) complete while any descendant mission may still dispatch does not conform." If terminality carried limb (a), limb (a) would be dead text for two of the three states it names. The one safe route to `failed` is RFC10-20(d) itself, where limbs (a) and (b) have already been attempted — which is exactly why the RFC10-18 route's silence is a gap rather than a redundancy.

**Repair.** Two edits, both small. (i) In RFC10-20, replace the trigger with every terminal transition: *"A human stop, cancellation, or expiry of a mission (RFC10-5), **and every transition to a terminal state under RFC10-18 or RFC10-18(a)**, has three effects…"* — with the note that where the terminal state was itself produced by RFC10-20(d), limbs (a) and (b) have already run and (d)'s enumeration governs. (ii) In RFC10-17(a), give the `failed` row the retention carve-out the unrecoverable-stop row carries: no reservation returned while the work it funds may still spend, with any such run named individually. Both belong in Wave D2 (correction plane) and neither touches an accepted digest.

(part 2/2)

### 2. `recovery_reserve` is sized per effect *class* while effect *instances* are unbounded, so compensatable effects are structurally underfunded — severity: **major**

**Anchor — RFC10-17(a)** (`budget-reservation.md`):

> "**`recovery_reserve` is sized, not merely present**: each compensating action an envelope names carries a **declared maximum cost** (RFC10-19), and `recovery_reserve` is not less than **the sum of those declared maxima over every effect class the envelope permits**…"

**Anchor — RFC10-19** (`effects-recovery-and-stop.md`), which prices recovery per instance:

> "**Every effect instance records: its effect class and dimension, the surface it touched, the acting principal, the establishing evidence, its reversal or compensation action and that action's funding, and the outcome.**"

**Doctrinal anchor — SEC-4:** "every write is attributed to Syzygy, atomic, and **individually revertable**."

**Sweep.** [Observed] Denominator: six RFC-0010 module files. `recovery_reserve` occurs at nine sites; exactly one states its sizing, and it sums over classes. The token "instance" occurs twice in the package, both in RFC10-19, and both require per-instance treatment — the record above, and "Where compensation succeeds for some effects and fails for others, the outcome is recorded **per effect**." No clause bounds the number of effect instances a mission may apply: RFC10-7's minimum envelope fields enumerate "**budgets** — token, monetary, wall-clock, retry, and concurrency," and no effect-instance count among them.

**Failure scenario.** [Inferred] An envelope permits one compensatable class — an external row insert, compensating action "delete the row," declared maximum cost one adapter call. `recovery_reserve` is therefore sized at one adapter call and satisfies the stated inequality. The mission inserts 40,000 rows within its token and wall-clock budgets. At `failed`, compensation is funded for one. The remaining 39,999 route to RFC10-19's shortfall limb — "the shortfall is an escalation trigger under RFC10-13, every uncompensated effect joins the single Attention Item naming what cannot be undone, and the terminal reason states it as uncompensated-for-want-of-budget." That limb is written as an exception path for the case where recovery *turns out* to cost more than declared. Under the per-class sizing rule it is the **normal** path for any class applied more than once. The contract's own promise — that a declared-compensatable effect is a funded one — holds only for missions that apply each class exactly once, a restriction the contract nowhere states. [Inferred] For the subset of effects that are governed-repository writes, this also puts SEC-4's "individually revertable" on a reserve that funds one revert.

**Repair.** Size the reserve against the instance ceiling, and give the ceiling a home. Either (i) amend RFC10-7's minimum envelope fields to include a **maximum effect-instance count per permitted effect class**, and amend RFC10-17(a) to require `recovery_reserve ≥ Σ over classes (declared maximum compensation cost × declared maximum instance count)`; or (ii) mirror the dispatch rule onto effects — reserve each instance's compensation cost from `recovery_reserve` at the moment the effect is applied, and refuse the effect where the reserve has no headroom. Option (ii) is the more consistent with this module's own thesis that reservation is enforcement rather than accounting, and it makes the shortfall limb an exception again.

### 3. The prevention plane's honesty carve-out covers only *externally*-granted credentials, while RFC10-18(a) knows Syzygy-granted profiles can reach past mediation — a duty with no choke point — severity: **major**

**Anchor — RFC10-10** (`prevention-envelope-and-attention.md`):

> "The MUST is scoped honestly to **Syzygy's own choke points**: an actor holding **externally-granted** toolchain credentials can act outside Syzygy's mediation, and those effects are bounded by the adapter and credential authorization (VIS-5) — not by this runtime."

**Anchor — RFC10-18(a)** (`effects-recovery-and-stop.md`), which scopes the same boundary differently:

> "**and equally where the granted credentials, tools, and execution profiles reach beyond what declared adapter coverage observes: the Unknown keys on established coverage, never on the envelope's own declaration alone**"

**The mechanism — RFC5-20** (`execution-profiles.md`), verified verbatim:

> "**Network policy** — default-deny egress, the allowed set declared from a closed grammar: `none`, `loopback-only`, or an enumerated destination list (named hosts/services, no wildcards). **Every declared policy excludes Syzygy's own listening interfaces**…"

**Sweep.** [Observed] Denominator: four RFC-0005 module files, 1,273 lines. The injection prohibition (RFC5-24) is bounded to credentials that authenticate to Syzygy: "**no execution profile may name as an injectable any credential that authenticates to Syzygy itself.**" Nothing forbids enumerating a model provider as an allowed destination, and nothing forbids injecting that provider's credential. RFC5-18's gate is five-part, (a) acceptance, (b) profile exists, (c) owner-approved with verified provenance, (d) principal authenticated and authorized, (e) run captured as an Execution record — **no part checks the profile's destination list against the egress choke point**. Sweep for `token|monetar|cost|spend` across the whole RFC-0005 package returns five hits, none normative on egress metering.

**Failure scenario.** [Inferred] An approved profile enumerates the model provider as a destination and injects the provider credential — both lawful under RFC5-20 and RFC5-24. The sandboxed agent transmits governed content directly. That path's egress is enforced by the isolation mechanism's "enforced network policy" (RFC5-21), not by RFC5-15's choke point, so neither RFC5-15's three-part consent check nor RFC10-17's remaining-headroom predicate stands on it. Disclosure is unrecoverable and, on this path, unauthorized — the SEC-2 outcome. RFC10-6 does prohibit it — "No mission bypasses evidence, reconciliation, consent (RFC5-12), egress (RFC5-14), or execution-profile (RFC5-18) gates" — and RFC10-21 assumes the composite meets "the RFC5-15 choke point." But a prohibition is not a choke point, and this package's own standard is that it must be: "Guardrail enforcement is **preventive**, not merely observational: an out-of-envelope act is refused at the choke point … not performed-then-flagged." The cost half of this route *is* closed, by RFC10-17's "A declared maximum with no enforced limit admits nothing." The disclosure half is closed only by detection — RFC10-18(a) resolves the predicate Unknown for exactly this configuration, routes the mission to `failed`, and mints the item. Detection after an unrecoverable disclosure is the correction plane doing its job; it is not prevention, and RFC10-10 currently reads as though prevention held.

**Repair.** Narrow RFC10-10's carve-out to what it can honestly claim, and give RFC10-6's prohibition an admission point. Suggested: amend RFC10-10 so the carve-out covers only credentials and routes **Syzygy did not grant**, and state that a route Syzygy itself grants through an execution profile is either mediated or **declared as an unmediated effect surface on the envelope** (the term RFC10-18(a) already defines). Then add the corresponding admission condition — a mission may not launch under a profile whose network policy reaches a destination not traversing RFC5-15 unless the envelope names that surface. The alternative repair sits in RFC-0005 (require sandbox egress to a provider to be proxied through the RFC5-15 choke point); either closes it, but RFC-0010 should not assert prevention it does not hold.

### 4. RFC10-20's "all immediate at the act" is contradicted by limb (d)'s own latency bound — severity: **minor**

**Anchor — RFC10-20:** "A human stop, cancellation, or expiry of a mission (RFC10-5) has three effects, **all immediate at the act**" — against limb (d): "The act does not return until (a) and (b) hold **or that bound elapses**: synchronous, and bounded."

[Inferred] Limb (b) is bounded, not immediate; limb (c)'s checkpointing cannot be immediate either, and (c) itself contemplates completing later ("(c)'s determination completes when that run's records exist or resolves Unknown"). On the package's most safety-critical clause, the two sentences give an implementer two readings of the same guarantee. **Repair:** replace "all immediate at the act" with "all initiated at the act and completing within limb (d)'s bound," leaving (d) as the sole statement of latency.

### 5. "the RFC5-21 launch gate" names the wrong clause, and the limits RFC5-21 enforces do not include the two budget kinds RFC10-7 names first — severity: **minor**

**Anchor — RFC10-17:** "**hard-enforceable** — a Syzygy choke point (**the RFC5-21 launch gate**, the RFC5-15 egress gate) can refuse the act that would exceed the bound *before it happens*," and "its declared maximum cost is bound to an **enforced runtime limit at the launch gate** — **RFC5-21's enforced resource limits for the run**."

[Observed] The launch gate is RFC5-18 ("**RFC5-18.** **The gate.**"); RFC5-21 is the isolation-class floor, which supplies enforced limits to an already-launched run. The two are conflated. More substantively, RFC5-20 — the clause that enumerates what those limits are — reads verbatim: "**Resource limits** — bounds on **CPU time, memory, disk, wall clock, and process count**; exceeding any bound terminates the run, recorded." Token and monetary spend are absent, and a sweep of the whole RFC-0005 package (denominator: four files) finds no normative treatment of either. So for two of the five budget kinds RFC10-7 names — "**budgets** — token, monetary, wall-clock, retry, and concurrency" — there is no launch-side enforced limit to bind to.

[Inferred] This is a seam defect, not a hole, because RFC10-17's definition of `hard-enforceable` is behavioural ("can refuse the act … *before it happens*") rather than nominal, and its monetary limb routes the residue correctly: "where neither is enforceable, the kind is **non-delegable**" — which requires per-act human approval. An honest implementer lands in the right place. A careless one reads "enforced runtime limit at the launch gate" and believes RFC5-21 caps token spend. **Repair:** cite RFC5-18 for the gate and RFC5-21 for the floor; state that RFC5-20's enumerated limits cover the wall-clock and process-count kinds only, and that token spend takes the same trichotomy the monetary limb already states.

### 6. "supports no autonomous dispatch **on its own**" leaves monitoring-only a combination reading — severity: **minor**

**Anchor — RFC10-17:** "**monitoring-only** — consumption is measurable but not refusable at any choke point. A monitoring-only kind is never rendered as a hard bound and **supports no autonomous dispatch on its own**."

[Inferred] "On its own" implies some combination under which a monitoring-only kind *does* support autonomous dispatch, and no clause states what that combination is. The operative sentence two paragraphs earlier resolves it correctly and absolutely — "A declared maximum with no enforced limit admits nothing" — so the closed reading is available and is the one an implementer applying the admission rule per budget will reach. But this contract's own discipline is that a bound stated ambiguously resolves narrow and "genuine ambiguity in a load-bearing bound is an escalation trigger" (RFC10-7); the phrase invites the wide reading in the one kind where the wide reading is unsafe. **Repair:** delete "on its own," or replace the sentence with "a dispatch whose declared maximum cost is bound to a monitoring-only budget is refused."

### 7. RFC10-22's terminal exemption names two instances beside a closure statement, and RFC10-17's post-terminal overrun item is not among them — severity: **minor**

**Anchor — RFC10-22:** "**Exactly two classes of item are exempt from both bounds, and the enumeration is closed.** … **(ii)** An item another clause mandates **at or after a terminal transition** — RFC10-19's irreversible-effect enumeration and RFC10-20(d)'s failed-stop enumeration — because a terminal mission cannot take this clause's pause response," with the held-item rule scoped to the other case: "Where a mandated mint meets a full queue on a **non-terminal** mission … the mandated item is **held and minted when a slot frees**."

[Observed] RFC10-17 mandates an item for every overrun, and its second overrun source is "measurement lag within a declared, bounded telemetry interval" — lag that "**defers knowledge of spend**," so the item is frequently mandated *after* the mission is terminal. [Inferred] Two readings compete. On the better one, class (ii) is defined by its opening sentence and the em-dash pair is illustrative, so the overrun item is exempt and the queue bound does not swallow it. On the reading a careful implementer may take from "the enumeration is closed" one sentence earlier — reinforced by "An exemption not in this enumeration returns the queue to unbounded; adding one is an amendment to this clause, never a reading of it," which explicitly forbids reading an exemption in — the overrun item is neither exempt nor coverable by the held rule (that rule is scoped to non-terminal missions) nor able to trigger the pause response (the mission is terminal). It has no route, and dropping it is the RFC10-13 violation of a silent disappearance. **Repair:** state that class (ii) is defined by its predicate and that the two named clauses are examples, and add RFC10-17's overrun item to the examples.

---

## Assessment

[Inferred] Against earlier bytes, three of the prior round's routes look genuinely closed, and closed by the right mechanism rather than by assurance prose: the budget invariant now sits on admission rather than on the ledger, the effect-class space is total with `atomically-reversible` narrowed past the point an implementer could abuse it, and stop is finite with a hang classified as failure and a stated third exit. Those are substantive repairs and the module is stronger for them.

Finding 1 is the reason this is not a CONFIRM. It is not a philosophical gap: the correction plane's whole premise is that a mission which has gone wrong is stopped and its effects adjudicated, and on the one route to `failed` that does not pass through a stop act, the mission is adjudicated while it is still running. The repair is two sentences in clauses already open for Wave D2 revision. Findings 2 and 3 are real and should travel with it; findings 4–7 are wording and citation defects of the kind this repository's rule 8 exists to catch.

I record one limit on my own sweeps [Unknown]: my absence claims are measured over the ten RFC-0005 and RFC-0010 module files named above, 2,598 lines. I did not read RFC 0002, 0003, 0004, 0008 or 0011, so a clause outside that denominator could bear on findings 1 or 3 — though for finding 1 the duty is one RFC-0010 states about its own lifecycle states, and no other contract owns RFC10-5's vocabulary.

VERDICT: REVISE
