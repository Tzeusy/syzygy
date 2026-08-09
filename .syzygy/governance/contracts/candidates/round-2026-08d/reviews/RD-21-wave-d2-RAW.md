RD-21 — Wave D2 exact-package review (part 1/3)

Reviewer: independent fresh-context. Date 2026-08-09. Baseline commit 771965c (verified: `git rev-parse HEAD` in the frozen clone = 771965c70f419465d13713f7654396a664234b47). Subject: Wave D2 — RFC-0010 module 4, the correction plane. Read only from the frozen clone; excluded paths (round-2026-08d/, history/, reviews/, _bootstrap/) not opened.

## 1. Manifest verification

[Observed] `WAVE-D2-MANIFEST.txt` own sha256 = `ab590e3e553a2f1f2db92d1c676a0fd5c05d2283548163e5c3663df5a31382d8`. This is byte-identical to the argument in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 row D2 (`ACCEPT FOUNDATIONAL WAVE D2: ab590e3e…82d8`). Digest computed by `sha256sum`, never transcribed.

[Observed] The manifest lists exactly one row:
`9e765f9da54287eb0bf379ce229f69addfb475a7593c97e56a4a9baadeac7177  rfcs/RFC-0010/effects-recovery-and-stop.md`
Recomputed from the clone: identical. 1/1 rows match.

[Observed] Partition sweep of the RFC-0010 package, **denominator = 6 files** (`find rfcs/RFC-0010 -type f` = 6; README.md, budget-reservation.md, effects-recovery-and-stop.md, mission-identity-approval-and-lifecycle.md, portfolio-and-cross-project-consent.md, prevention-envelope-and-attention.md). Python set arithmetic over the D1 and D2 manifest row sets:
- D1 rows = 5, D2 rows = 1, sum = 6 = denominator
- overlap D1∩D2 = ∅ (nothing in both)
- files in neither = ∅
- manifest rows with no file on disk = ∅
- digest mismatches across all 6 = ∅
The two manifests partition RFC-0010 exactly.

[Observed] Both D2 and D1 rows are byte-consistent subsets of `ACTIVE-CONTRACT-MANIFEST.txt` (39 rows); the D2 row's digest matches that file's entry.

[Observed] Second method, per verification rule 2: `python3 scripts/check_governance.py` run in the clone reports
`OK CG-7a manifest digests valid; waves partition the set — 78 entries examined, 0 findings`
`OK CG-7b wave-act arguments match the wave manifests — 6 arguments examined, 0 findings`
Whole run: `25 OK, 15 WARN, 0 FAIL (40 checks)`. No FAIL. (Output read, not exit code.)

[Observed] Clause-partition check over the package, denominator = RFC10-1…RFC10-24 plus sub-clauses RFC10-17(a)/18(a)/19(a) = 27 identities. Every identity is defined in exactly one module; none defined nowhere, none in two modules, none defined outside the declared set. D2 defines exactly `RFC10-18, RFC10-18(a), RFC10-19, RFC10-19(a), RFC10-20, RFC10-23` — matching its own front-matter, README's clause-map row 4, and its end-of-module footer. **Manifest verification: clean.**

## 2. Outward references from the D2 module (task 3a)

[Observed] Regex extraction of every `RFCn-m` citation in `effects-recovery-and-stop.md` yields citations into exactly four external contracts: RFC 0002 (RFC2-19, RFC2-25), RFC 0003 (RFC3-16, RFC3-16(a)), RFC 0004 (RFC4-18, RFC4-21, plus one bare `RFC 0004`), RFC 0005 (RFC5-14, RFC5-15, RFC5-21, RFC5-22). All four are in `WAVE-A-MANIFEST.txt` — **bound at the time D2 is performed**.

[Observed] **Zero** citations to RFC 0011, RFC 0007, RFC 0008, RFC 0009, RFC 0001, or any candidate policy/topology artifact. Sweep denominator: every `RFC\d+-\d+` match in the file (86 occurrences, 29 distinct identities). D2 therefore makes **no forward reliance on unbound material**. This is a materially better posture than Wave B's (which the record notes binds text pointing at candidates).

Spot-verified that the cited clauses exist and say what D2 attributes to them:
- RFC5-21 (`RFC-0005/execution-profiles.md:141`) — "…enforced resource limits, and **a kill switch terminating the run and its descendants**." D2's RFC10-20(b) cites it for exactly that. D2 then *disclaims* the extension honestly: "**this is this clause's own admission requirement on the isolation class, stated here and not attributed to RFC5-21** (RFC5-21 requires the kill switch; the failure-signal floor and its interval are this clause's)". [Observed] Accurate — RFC5-21 states no reporting interval. Model behaviour under verification rule 8.
- RFC5-22 (`execution-profiles.md:162`) — destructive-operation classes "**standing-approved** by the profile's approval Decision". D2's RFC10-19: "a destructive-operation class reaches a mission only where the envelope names it, never by inheritance from an execution profile's standing approval (RFC5-22)". Accurate.
- RFC2-25 — six-tier registry including `gate-backed` and `report-fact`; D2's use of both is accurate.
- RFC2-19 — reconciliation trigger/staging, the source of "uncomputed reconciliation"; D2's "wherever RFC2-19 leaves reconciliation uncomputed" is accurate.
- RFC4-18..RFC4-21 — `RFC-0004/execution-record.md` clause range, per that package's own README row. Accurate.

[Observed] `depends_on: [RFC-0002, RFC-0003, RFC-0004, RFC-0005]` in D2's front-matter is exactly the set of externally cited packages — no under- or over-declaration.

Nothing here is staged dishonestly. **Task 3(a): clean.**

RD-21 — Wave D2 exact-package review (part 2/3)

## 3. Seam integrity with D1 (task 3b)

[Observed] Sweep D1 → D2, denominator = all lines of the 5 D1 files, matching `RFC10-(18|19|20|23)(\([a-d]\))?`: **38 occurrences**. Excluding README's own clause-map/summary/footer rows (index prose, not reliance), **18 reference lines** carry substantive reliance: budget-reservation.md ×9, mission-identity-approval-and-lifecycle.md ×3, prevention-envelope-and-attention.md ×6, portfolio-and-cross-project-consent.md ×0.

I checked each of the 18 for connection when D2 binds. **17 connect cleanly; 1 does not** (finding B1/M1 below). Verified connections worth naming:

- RFC10-7's envelope minimum requires "the **completion establisher and effects-determination evaluator** (RFC10-18, RFC10-18(a))"; D2's RFC10-18 answers verbatim: "the **completion establisher is a required envelope field under RFC10-7's minimum**". Same vocabulary, same direction.
- RFC10-8: "A derived child **inherits the parent's declared completion establisher and effects-determination evaluator** (RFC10-18, RFC10-18(a))"; D2 RFC10-18: "a derived child mission **inherits its parent's declared establisher** (RFC10-8)", and RFC10-18(a): "inherited by derived children (RFC10-8)". Connects both ways.
- RFC10-5's park rule enumerates its sources — "RFC10-8, RFC10-11's `paused`-or-`blocked` disjunction, **RFC10-18**, and RFC10-22's pause-on-attention-bound" — and D2's RFC10-18 reciprocates: "What bounds this park is RFC10-5's **maximum park duration**, which holds for every block class". D2 also correctly reads RFC10-5's narrower human-resolution scope: RFC10-5 says "exit from `blocked` where the block arose under RFC10-8 or RFC10-11 is a **human resolution act**", and D2 says "RFC10-5's human-resolution rule is scoped to blocks arising under RFC10-8 or RFC10-11; an RFC10-18-sourced block arises under neither". Anchored to the clause, quoted correctly.
- RFC10-17's `recovery_reserve` ("held undispatchable so that RFC10-19's compensating actions are fundable") ↔ D2 RFC10-19 ("it may execute declared compensating actions within `recovery_reserve`"). RFC10-17(a)'s sizing rule ("each compensating action an envelope names carries a **declared maximum cost** (RFC10-19)") ↔ D2 RFC10-19 ("with the compensating action named and its **maximum cost declared**"). Exact both ways.
- RFC10-17(a)'s last row ("unrecoverable stop — RFC10-20 limb (b) not achieved … reservations are retained and **named individually**") ↔ D2 RFC10-20(d) ("each such run's reservation is retained and named under RFC10-17(a)"). Exact both ways.
- RFC10-17's overrun source (i) cites "a declared unmediated effect surface (RFC10-18(a))"; D2 RFC10-18(a) defines exactly one such term — "a declared, named **unmediated effect surface**". Vocabulary matches (1 occurrence each side).
- RFC10-22's exemption class (ii) names "RFC10-19's irreversible-effect enumeration and RFC10-20(d)'s failed-stop enumeration"; both exist in D2 verbatim.
- D2's RFC10-18(a) claims to govern four named sites. I verified all four verbatim (whitespace-normalised counts): RFC10-19's "with effects already applied" ✓, RFC10-19(a)'s "after applying effects" ✓, RFC10-20(c)'s "any effect already applied" ✓, RFC10-17(a)'s "applied-effects row selection" ✓ (that clause's rows do partition on applied effects). This is a well-built cross-reference and the "any future clause keying on this predicate is governed by this sub-clause by that fact alone" limb closes the extension hole.

Note on staging: README's staging sentence — "Cross-module references from the prevention plane into module 4 (the release table's recovery hooks, RFC10-18 naming in lifecycle text) are **staged references**" — is universally quantified over the class; the parenthetical is illustrative and names 2 of the ~18 edges. Not a defect, but a reader should not treat the parenthetical as the enumeration.

---

## FINDINGS

### B1 — BLOCKING. RFC10-20's trigger enumeration does not reach `failed`, so the mission state the correction plane *itself creates* carries no dispatch-halt or run-termination consequence.

**Clause anchor, quoted (D2, RFC10-20):**
> "**RFC10-20. What stop guarantees.** A human stop, cancellation, or expiry of a mission (RFC10-5) has three effects, all immediate at the act: **(a)** no further work is dispatched and no further Syzygy-mediated act is admitted under that mission; **(b)** every run Syzygy launched under the mission is terminated together with its descendants…"

The trigger set is closed and human-keyed: *human stop*, *cancellation*, *expiry*. It does not include `failed`.

**But D2 itself routes missions into `failed` by two paths that are neither a stop, a cancellation, nor an expiry:**
> RFC10-18: "Where no independent establisher exists for a mission's objective class — including wherever RFC2-19 leaves reconciliation uncomputed — the mission **never reaches `completed`** … **With effects already applied it enters `failed`**, so that RFC10-19's compensation, enumeration and disposition duties fire."
> RFC10-18(a): "**Unknown fails closed: where whether effects were applied is Unknown, effects are treated as applied** … The mission enters `failed`, RFC10-19's duties fire…"

**Absence sweep, with denominator.** Over all **6 files** of the RFC-0010 package, matched with Python `re` (not ugrep):
- the string `no further work is dispatched` occurs **exactly once** — in RFC10-20(a).
- `halt` occurs on 7 lines; the only dispatch-halting one outside RFC10-20 is RFC10-11 ("Reaching any envelope bound … halts further materialization and execution under that mission"), keyed to **bound exhaustion**, not to a terminal state.
- `terminat*` in a run-termination sense occurs only inside RFC10-20 limbs (b)/(c)/(d).
- RFC10-5 (D1) says only "every terminal state is recorded with its reason". Its one "ends the mission" sentence is scoped to park expiry.

[Observed] **No clause in the package halts dispatch or terminates runs on the `failed` transition that RFC10-18/RFC10-18(a) create.**

**Failure scenario.** A mission is `running` with Syzygy-launched runs active. Adjudication finds no independent establisher (or the effects-applied predicate resolves Unknown). The mission enters `failed`. RFC10-19's duties fire and compensating actions are attempted. Meanwhile nothing has stopped the runs — they continue to dispatch and apply new external-mutation effects *while the compensation is running against the effects already applied*. Then RFC10-17(a)'s `failed` row applies: "released in full **after** RFC10-19's compensating actions are attempted". The reservation funding the still-executing runs is returned to headroom — in direct tension with the principle that same clause states one row later: "a reservation may not be returned while the work it funds may still spend."

This is the exact property task 3(c) asks about, and it is the plane's own stated purpose. D2 §1: "This module addresses the *past*: work already dispatched, money already spent, effects already applied, and **a human who needs to be able to stop all of it**." The plane does not close on the terminal state it mints itself.

**Two further callers rely on the same too-narrow trigger:**
1. RFC10-19(a)'s closed disposition set: "`halt-siblings`   active siblings stop under RFC10-20" and "`compensate-all`  active siblings stop". A machine-initiated sibling halt is not a human stop, a cancellation, or an expiry, so RFC10-20's own trigger sentence does not admit it. The strictest default under RFC10-7's obligation limb — "**`halt-siblings` plus an escalation (RFC10-13) before any further dispatch**" — is the *default* case, so this is the common path, not the exotic one.
2. RFC10-17(a)'s parent row (see M1).

**Concrete repair (D2 is still unbound and editable).** Re-key RFC10-20's opening so its limbs attach to the transition rather than to the human act, e.g.: "A human stop, a mission's cancellation or expiry, **and every other transition into a terminal state — including the `failed` transitions RFC10-18 and RFC10-18(a) take and the sibling halt RFC10-19(a) directs — have three effects, all immediate at the transition**: (a) … (b) … (c) …", and state that on `completed` limbs (a) and (b) hold at the terminal record. Then RFC10-17(a)'s `failed`/`completed`/parent rows and RFC10-19(a)'s two halting dispositions all have a clause that actually delivers what they cite. This repair is inside D2's own clause; it needs no amendment to any bound artifact.

**Severity: blocking.** Binding D2 as written completes the *duty* side of the correction plane (compensation, enumeration, dimensions) but leaves the *containment* side open on the one terminal state the plane creates for itself. A correction plane whose `failed` missions may keep dispatching is not a correction plane.

Lesser limb, same root cause, recorded for completeness: `completed` likewise carries no stated dispatch-halt. RFC10-18 permits an independent establisher to take `running → completed` while runs execute; RFC10-17(a) then releases the reservation "in full at the terminal record", and RFC10-17's admission inequality `reserved_remaining + spent ≤ authorized − recovery_reserve` re-opens headroom for a new dispatch. [Inferred] Lower practical risk than the `failed` case, but the repair above closes both at no extra cost.

RD-21 — Wave D2 exact-package review (part 3/3)

### M1 — MAJOR. RFC10-17(a)'s parent-terminal row is a dangling limb: it cites RFC10-20(b) for a propagation RFC10-20(b) does not perform on two of the five terminal states.

**Clause anchor, quoted (D1, RFC10-17(a) release table, `budget-reservation.md:152`):**
> "| the **parent** of outstanding child grants reaches **any terminal state** | the stop propagates to every derived child (RFC10-20(b)); each child grant is released at that child's resulting terminal record, to the parent's terminal accounting. **No child grant survives its parent's terminal record** except a reservation retained for a run that did not terminate…"

**What D2 actually delivers (RFC10-20(b)):**
> "…**and the stop propagates transitively to every child mission derived from it (RFC10-8) and to their descendants**: a descendant mission is stopped as if the act had named it, its own runs terminated under this same limb, and its reservation dispositioned under RFC10-17(a)."

The limb is excellent — and it fires only on the trigger RFC10-20 declares. Terminal-state denominator from RFC10-5's vocabulary block: `completed`, `failed`, `cancelled`, `expired` = 4. RFC10-20(b) reaches `cancelled` and `expired` (and a human stop). It does **not** reach `completed` or `failed` — **2 of 4**. The row says "any terminal state" and asserts "the stop propagates", but on a parent reaching `completed` or `failed` there is no stop for RFC10-20(b) to propagate.

**Failure scenario.** A parent mission with decomposition granted mints a child; the child holds a grant debited from the parent's envelope (RFC10-8) and is dispatching. The parent then enters `failed` via RFC10-18(a)'s Unknown-fails-closed rule. RFC10-17(a) says no child grant survives the parent's terminal record, citing RFC10-20(b) — but nothing stops the child, which keeps dispatching and spending a grant the release table has just accounted as returned to the parent's terminal accounting. Only the child's own "maximum time to first dispatch" bound would ever catch it, and that row is scoped to "a child mission holding a grant **it has not yet run under**" — a child already running is outside it.

**Severity: major.** The defect sits on the bound D1 side (RFC10-17(a)), so only D2 can close it: the repair is B1's — widen RFC10-20's trigger so the row's citation is honest. If B1 is fixed as proposed, M1 closes with it. If the owner prefers to accept D2 as-is, this must be recorded as a known dangling reliance from a *bound* clause, which is a worse posture than leaving it unbound.

### M2 — MAJOR. "A human stop" is a trigger with no lifecycle state, so its reservation-release row and RFC10-19's duty keying are under-determined.

**Anchors.** RFC10-20 triggers on "**A human stop**, cancellation, or expiry". RFC10-5's lifecycle vocabulary (D1) contains no `stopped` state; its human-act row is "any non-terminal state → cancelled | expired (human act)". RFC10-19's duties are keyed elsewhere: "Where a mission enters `failed`, `cancelled`, or `expired` with effects already applied…". RFC10-17(a)'s rows are keyed to `completed | failed | cancelled | expired | blocked | paused | draft | awaiting-approval | approved` plus the "unrecoverable stop" row.

Nothing states that a human stop *is* a cancellation. If it is not, a bare stop lands the mission in no named state, RFC10-19's trigger list does not name it, and RFC10-17(a) has no row for it (only the *unrecoverable* stop row). RFC10-20(c) partially rescues the duty side — "any effect already applied is classified and dispositioned under RFC10-19" — but nothing rescues the reservation side.

**Repair.** One sentence in RFC10-20: state that a human stop takes the mission to `cancelled` (or `failed` where limb (d) applies), so RFC10-19's trigger list and RFC10-17(a)'s rows both have a referent. **Severity: major** (reservation disposition undefined for the plane's headline act).

### M3 — MAJOR. RFC10-23 falls outside RFC10-16's stated coverage-matrix range, and README asserts the opposite.

**Clause anchor (D1, RFC10-16, `mission-identity-approval-and-lifecycle.md:191–199`):**
> "…may be scheduled solely from this RFC — **including everything RFC10-17..22 requires of a runtime**. … At surface specification a **clause-to-requirement coverage matrix over RFC10-1..RFC10-22** is produced…"

**README §Phase boundary (same bound wave) says otherwise:**
> "…its clause-to-requirement coverage matrix **must cover RFC10-1…RFC10-24 across all five modules**, not module 1 alone."

Per verification rule 8 the clause governs and the index prose does not. Of D2's six clause identities, RFC10-18/18(a)/19/19(a)/20 fall inside `RFC10-17..22`; **RFC10-23 does not** — and RFC10-23 is the clause that mandates a four-dimension terminal record, which is squarely observable behaviour. Binding D2 therefore adds a clause the package's own phase-gate matrix does not enumerate, and leaves two bound artifacts contradicting each other about the denominator.

Harm is bounded — RFC10-16's general prohibition ("This contract schedules nothing") is unqualified and does cover RFC10-23, and RFC10-16 itself says the matrix "is review material, never authority". But a coverage matrix with a wrong denominator is exactly the failure verification rule 4 exists for.

**Repair.** Since RFC10-16 is bound, the honest repair is either (i) a sentence in D2 §1 stating that RFC10-23's observable consequences are within RFC10-16's phase rule and are to be carried in that matrix notwithstanding its stated range, plus a recorded item to amend RFC10-16's range post-act; or (ii) record the discrepancy in the acceptance record as a known defect of the D1 bytes with a scheduled amendment. **Severity: major.**

### m4 — MINOR. RFC10-18(a)'s Unknown branch uses a definite article with no guaranteed referent.

> "The mission enters `failed`, RFC10-19's duties fire, and **the Attention Item** states that the disposition rests on an unresolved determination rather than on an observed effect…"

RFC10-19 mints "a **single** Attention Item naming what cannot be undone" only where irreversible effects exist. Where the Unknown branch fires and every declared class is atomically-reversible or compensatable, no such item is minted and "the Attention Item" has no referent — so the disclosure the clause depends on ("so a compensation record never implies an effect was seen") may not be made. **Repair:** "…and **an Attention Item is minted stating** that the disposition rests on an unresolved determination".

### m5 — MINOR. RFC10-22's exemption list does not name the new terminal-transition item D2 adds.

RFC10-22 (bound): "**Exactly two classes of item are exempt from both bounds, and the enumeration is closed.** … **(ii)** An item another clause mandates **at or after a terminal transition** — RFC10-19's irreversible-effect enumeration and RFC10-20(d)'s failed-stop enumeration — … **An exemption not in this enumeration returns the queue to unbounded**". Class (ii) is generally worded, so m4's item (once repaired) qualifies; but the em-dash list reads as exhaustive to a careful reader, and RFC10-22's own warning invites that reading. **Repair:** D2 states, at the m4 site, that the item is a class-(ii) exempt item under RFC10-22.

### m6 — MINOR (D1-side, record only). RFC10-17(a) has no row for `paused` **with** applied effects.

Rows cover `blocked` or `paused`, **no** applied effects; `blocked` or `paused` after Attention-Item expiry; `blocked` **with** applied effects. The 2×2 cell {`paused`} × {applied effects} has no row. Harm is bounded: the backstop "**No non-terminal state holds a reservation indefinitely**" plus RFC10-5's park maximum plus RFC10-19's keying on `expired` make the outcome derivable. Binding D2 is what makes the partition live (the predicate is RFC10-18(a)'s). No repair available in D2; record for the post-act amendment list.

---

## 4. Acceptance-record accuracy (task 3d)

[Observed] §1 row D2 reads: "RFC-0010 module 4 (effects, recovery, stop — the correction plane), per `wave-manifests/WAVE-D2-MANIFEST.txt`." Accurate: the file is `effects-recovery-and-stop.md`, README's clause map calls it "4 — completion adjudication, effects, recovery, stop", and the manifest header says "mission control correction plane (RFC-0010 module 4) — 1 module(s)". Argument digest matches (§1 above).

[Observed] The wave-history note is accurate about D2's own review state and does not overclaim: "…the effects/recovery/stop module rebuilt against reviews RD-1/RD-1b's blocking findings … **no confirming review is yet bound to any wave argument above** — the round's fresh-context review pass is owed before any wave act is performed". The D2 row itself repeats "awaits its own fresh confirming review". Correct and honest; this review is that pass for D2, and it does not confirm.

[Observed] Package self-descriptions accurate for the D2 set: front-matter `clauses`, `depends_on`, "module 4 of 5", README clause-map row 4, footer, and the "no gaps, no retired numbers" claim all verified by the 27-identity partition check. D2 owns no §8 owner question, and README's §8 table correctly assigns q1/q2/q3 to modules 1, 2, 5. **No count, range, or clause-map defect found in the D2 set.**

## 5. Judgment

Manifest and self-description are clean; no forward reliance on unbound material; the outward citations are accurate and, where D2 extends a bound clause, it says so on its face rather than attributing the extension upstream. The seam with D1 connects in 17 of the 18 substantive reliance sites I swept.

The central question — does binding D2 complete the correction plane coherently — answers **no, not yet**. The plane's duties are complete; its containment is not. RFC10-20's trigger set is closed to human-initiated acts, while three of the package's own mechanisms (RFC10-18/18(a)'s route to `failed`, RFC10-19(a)'s sibling halt, RFC10-17(a)'s parent-terminal row) route into it from machine-initiated transitions. The result is a mission that can be `failed`, have its compensation run, have its reservation released in full — and still be dispatching. All of B1, M1 and the `completed` limb close with a single edit inside RFC10-20, which is D2's own unbound text.

VERDICT: REVISE
