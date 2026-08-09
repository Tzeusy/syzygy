(part 1/4)

# RD-20 — Wave D1 exact-package review

Reviewer: independent fresh-context exact-package reviewer, round-2026-08d.
Date: 2026-08-09. Baseline commit: 771965c70f419465d13713f7654396a664234b47.
Subject: Wave D1 — RFC-0010 prevention plane, per `wave-manifests/WAVE-D1-MANIFEST.txt`.
Read from the frozen clone only; nothing written into it.
Position in ceremony: third, after Waves A and B are bound. RFC-0010 module 4 (Wave D2), RFC-0011, craft, and topology are NOT bound.

## 1. Manifest verification

**Manifest file's own sha256** (this is the act's argument):

```
570e617091bb41d8b34ca17b09e12f41d22e4d592a23249c8a737a698f8c0dff  wave-manifests/WAVE-D1-MANIFEST.txt
```

Recomputed by script (Python `hashlib.sha256` over file bytes), never transcribed. All five rows **MATCH**:

| File | sha256 | Result |
|---|---|---|
| `rfcs/RFC-0010/README.md` | `acda0236…733268` | MATCH |
| `rfcs/RFC-0010/budget-reservation.md` | `a83592cf…3d0dee` | MATCH |
| `rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md` | `8810f062…297809` | MATCH |
| `rfcs/RFC-0010/portfolio-and-cross-project-consent.md` | `cf82b5e7…f1823b6` | MATCH |
| `rfcs/RFC-0010/prevention-envelope-and-attention.md` | `9da45e57…4e2648` | MATCH |

[Observed] The D1 row in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1 quotes `570e6170…8c0dff` — identical to the recomputed manifest digest.

**Partition sweep, with denominator.** Population = every file in `C/rfcs/RFC-0010/` = **6** files (directory listing, not a glob assumption). D1 claims 5; D2's manifest claims 1 (`effects-recovery-and-stop.md`, `9e765f9d…ac7177`, MATCH). Set arithmetic: D1 ∩ D2 = ∅; D1 ∪ D2 = the full 6-file population; zero files in neither wave; zero manifest rows without a file on disk. [Observed] **The partition is exact and silent-orphan-free.**

Cross-checked against `ACTIVE-CONTRACT-MANIFEST.txt` (39 rows): its six RFC-0010 rows carry byte-identical digests to the two wave manifests. [Observed]

**Clause-definition sweep, with denominator.** Regex over clause-definition sites (`^\*\*RFC10-n…`) across all 6 package files: **27 definition sites, 27 unique, zero duplicates**. RFC10-1…RFC10-24 plus RFC10-17(a), RFC10-18(a), RFC10-19(a) — every expected identity defined exactly once, nothing unexpected. The README's clause-map assignment matches the definition sites file-for-file. [Observed] Note for the findings below: **README.md defines zero clauses.**

**Citation resolution.** Every load-bearing citation from the D1 set into Waves A/B was checked against clause-definition sites in `rfcs/` outside RFC-0010/0011: RFC1-7, RFC2-15/19/23/25, RFC3-15/16, RFC4-18, RFC5-3/5/6/12/14/15/18/21/22/25, RFC6-13/14, RFC8-12/19/28/30 — **24 of 24 resolve.** [Observed] No D1 clause cites a Wave B contract that is not bound. No module frontmatter declares `depends_on` outside A∪B (verified across all five: the union is RFC-0001…0006, 0008 — **RFC-0011 appears in no `depends_on`**).

## 2. Central question

**Is the prevention plane independently acceptable standing on A+B alone, before the correction plane exists?**

Short answer: **for effects, yes. For control, no — and the package's own justification for "yes" is what conceals the gap.**

The effects argument holds. RFC10-7's `propose-only` cap is a real clause, really binding, and it bounds every dimension of external mutation. The control argument does not hold: what a human *stop* guarantees, and who may *establish* that a mission completed, are entirely in Wave D2 — and both are duties that arise with **zero effect classes authorized**, which is precisely the condition under which the README says staged duties "cannot yet arise."

The guarantee that makes the wave safe is stated in the package index, which defines no clause; the clause that would have to carry it does not.

## 3. Cross-plane references, enumerated (task 3a)

Scripted sweep, Python `re` (the system `grep` is ugrep and its `[^]]` classes match nothing), over all five D1 files — denominator **1,011 lines**. Every occurrence of `RFC10-18`, `RFC10-18(a)`, `RFC10-19`, `RFC10-19(a)`, `RFC10-20` (and limbs), `RFC10-23`, plus `RFC 0011` / `RFC-0011`.

Excluding the README's own clause-map row and §1 summary (lookup apparatus, not reliances), there are **15 normative reference sites** from D1 into D2, plus **1** into RFC 0011:

| # | Site | Target | Staged honestly? |
|---|---|---|---|
| 1 | `mission-identity` L105 — lifecycle diagram `→ failed` | RFC10-18, RFC10-20(d) | Partly — RFC10-18 named by the README parenthetical; RFC10-20(d) is not. See M4 |
| 2 | `mission-identity` L133 — park rule source list | RFC10-18 | Yes — lifecycle text, named |
| 3 | `mission-identity` L146 — "It ends the mission and fires RFC10-19's duties" | RFC10-19 | **No** — unnamed by any staging note |
| 4 | `prevention` L53–54 — establisher/evaluator as required envelope fields | RFC10-18, RFC10-18(a) | **No** — see B3 |
| 5 | `prevention` L96 — "their own recorded dimensions … (RFC10-23)" | RFC10-23 | **No** — the substance survives in RFC10-7's own words; the dimension vocabulary does not |
| 6 | `prevention` L99 — "the predicate that engages the correction plane (RFC10-18(a))" | RFC10-18(a) | **No**, but direction safe (a relieving limb; relief from a non-existent duty is inert) |
| 7 | `prevention` L134–136 — child inherits establisher/evaluator | RFC10-18, RFC10-18(a) | **No** — though RFC10-8 carries a real D1-side substitute for children |
| 8–9 | `prevention` L262–263 — attention-queue exemption class (ii), a **closed** enumeration naming only D2 clauses | RFC10-19, RFC10-20(d) | **No**, but direction safe: class (ii) is empty under D1-only, which tightens the queue |
| 10 | `budget` L52 — `recovery_reserve` "so that RFC10-19's compensating actions are fundable" | RFC10-19 | **No** — see M3 |
| 11 | `budget` L60 — "the reserve is spendable only by RFC10-19's compensating actions" | RFC10-19 | **No** — see M3 |
| 12 | `budget` L107 — overrun source (i), "a declared unmediated effect surface (RFC10-18(a))" | RFC10-18(a) | **No** — the surface's *declaration rule* is D2 |
| 13 | `budget` L120 — "the same independence rule RFC10-18 states for completion" | RFC10-18 | **No** — the referenced rule does not exist under D1-only; the limb still works because `budget` restates the substance ("never from a self-report by the principal whose spend it is") |
| 14–17 | `budget` L145, L150, L152, L153 — release-table rows | RFC10-19, RFC10-20(b), RFC10-20 | **Yes** — named twice (module §1 and README parenthetical) |
| 18 | `budget` L160 — recovery_reserve sizing, "declared maximum cost (RFC10-19)" | RFC10-19 | **No** — see M3 |
| 19 | `README` L154–155 — "**RFC 0011:** every mission-spawned agent run receives a governed context packet; the envelope is a mandatory packet input" | RFC-0011 | **No** — indicative, no staging marker. Substantively harmless; see m5 |

**The staging apparatus covers 4 of these 15.** The README's parenthetical (`README.md` L69–70) names two categories — "the release table's recovery hooks, RFC10-18 naming in lifecycle text" — and `budget-reservation.md` §1 names one (the release table). Everything in rows 3–13 and 18 is unnamed.

**And the independent-acceptability claim itself is index prose.** Denominator sweep over all 1,011 D1 lines for `correction plane` / `module 4` / `accepted` / `acceptance` / `staged`: the conditional "**until the correction plane is accepted**" appears **exactly once in the whole D1 file set** — `README.md` L67, inside the §"Clause map and lookup rule" narrative. No clause states it.

(part 2/4)

# FINDINGS

## BLOCKING

### B1 — The cap that makes D1 safe is not conditioned on D2 by any clause; only the index says it is

**Anchor — README.md L66–68 (index prose, no clause identity):**

> "Effect-bearing autonomy levels are inoperative until the correction plane is accepted *and* the autonomy-level vocabulary is enumerated by owner act."

**Anchor — RFC10-7, `prevention-envelope-and-attention.md` §2.1 (the clause):**

> "Until the autonomy-level vocabulary is enumerated by owner act (§8 q2), the maximum autonomy level of every envelope is capped at **propose-only**: a stated higher level has no enumerated vocabulary to bind to and does not take effect."

and

> "A level above `propose-only` is inoperative until both the vocabulary is enumerated by owner act and each level's permitted effect set is stated **by that same owner act** — an OpenSpec requirement may specify behavior for a level; it never fixes a level's permitted effect set."

**The defect.** RFC10-7 states **two** conditions for the cap to lift, and Wave D2 is neither of them. The README states **three**, and the third — correction plane accepted — is the one carrying the wave's independent acceptability. README.md defines zero clauses (verified: 27 clause-definition sites, all in modules 1–5, none in README). Verification rule 8 applies directly: section prose near a clause is not the clause, and this prose is not even near one — it is in a different file.

**The reachable state.** The owner performs Wave D1 (act available now). The owner performs act 5, adopting D3 — the acceptance record's own §1 row marks act 5 "**Optional**: RFC-0010/0011 do not depend on it," so nothing sequences it after D2. RFC10-24's precondition is discharged; missions may now leave `awaiting-approval`. The owner then answers §8 q2 — an ordinary owner act that RFC10-7 invites and that no clause gates on D2. The cap lifts. Effect-bearing missions now operate under a corpus in which:

- **RFC10-19's classification gate does not bind.** "Every effect class an envelope permits is declared atomically-reversible, compensatable …, or irreversible. **An effect class not so classified is not authorized**" is a *prevention* rule sitting on the correction side of the seam.
- **RFC10-18's independence rule does not bind** (see B3).
- **RFC10-20's stop guarantee does not bind** (see B2).

VIS-5 supplies a doctrine floor on *direct writes* ("Syzygy's direct project-content writes touch only `openspec/**` … and `.syzygy/**`"), but not on adapter-mediated effects, which VIS-5 routes to "each authority's own contract" — and for missions that contract is RFC-0010, half of which is unbound in this state.

**Severity: blocking.** The wave's central claim is carried by a file that carries no clause, and the clause it summarizes says something narrower.

**Repair.** Amend RFC10-7 by semantic delta, adding a third limb to the cap: the cap holds, whatever level enumeration exists, until the correction-plane clauses (RFC10-18, RFC10-18(a), RFC10-19, RFC10-19(a), RFC10-20, RFC10-23) are in force by owner act. Alternatively state the constraint as an act-scope condition in the acceptance record's D1 row *and* in RFC10-7 — but a constraint in the record alone repeats the same defect one level up, since the record is not part of the bytes the act binds.

### B2 — What a human stop guarantees is entirely in Wave D2, and D1 supplies no substitute for even limb (a)

**Anchor — RFC10-20, `effects-recovery-and-stop.md` (Wave D2, unbound):**

> "**(a)** no further work is dispatched and no further Syzygy-mediated act is admitted under that mission; **(b)** every run Syzygy launched under the mission is terminated together with its descendants … **and the stop propagates transitively to every child mission derived from it (RFC10-8)**"

**Anchor — RFC10-5, `mission-identity-approval-and-lifecycle.md` §2.2 (D1):**

> "`any non-terminal state → cancelled | expired   (human act)`"

and

> "every terminal state is recorded with its reason; `expired` and `cancelled` are always reachable by human act"

**Anchor — RFC10-7 (D1), the envelope's minimum:** "**stop, pause, cancellation, and expiry conditions**" — the *conditions*, never the effect.

**The defect.** Denominator sweep over all 1,011 D1 lines for `dispatch|stop|cancel|terminate|terminal|halt` (62 matching lines, all read): **no D1 clause states that a cancelled, expired, or completed mission ceases dispatching, terminates its runs, or stops its derived children.** The only halting rules in D1 are RFC10-11 (bound exhaustion), RFC10-17's dispatch admission inequality, RFC10-22's pause-on-attention-bound, and RFC10-5's park expiry — none keyed to a human stop. RFC10-5 makes the *state transition* reachable and says nothing about what it does.

RFC10-20(a) is not correction. It is the purest prevention sentence in the package — refusing a future act — and it is on the wrong side of the seam. The same is true of RFC10-20(b)'s transitive child-stop: RFC10-8 (D1) makes child missions reservations against the parent, and `budget-reservation.md`'s release table relies on RFC10-20(b) to make a parent's terminal state release child grants. Without it, a stopped parent's children keep running, the row's precondition never occurs, and the only remaining bound on them is their own wall-clock budget exhausting — i.e. the human's stop is discharged by the budget, not by the act.

**This falsifies the README's staging justification directly.** The justification is:

> "…mark duties that cannot yet arise because no effect class that would trigger them is authorized."

The duty to stop a running propose-only mission arises with **no** effect class authorized. It arises on the first mission.

**Severity: blocking.** VIS-4 is the doctrine this package serves; the ability to actually stop is the operative content of human control, and under D1-only it has no clause.

**Repair.** Either (i) move RFC10-20 into a prevention-plane module and into Wave D1's manifest (renumbering is forbidden; moving a clause between modules is not renumbering, and the README's lookup rule already handles non-contiguity); or (ii) add a limb to RFC10-5 stating stop's D1 minimum — at a human stop, cancellation, or expiry no further work is dispatched, no further Syzygy-mediated act is admitted, and the stop propagates to derived children — with RFC10-20 stating the fuller guarantee (kill switch, latency bound, failed-stop routing) at D2; or (iii) withdraw the independent-acceptability claim and offer D1 and D2 as one act.

### B3 — Under D1-only the `running → completed` transition is governed by no clause; the executing principal may establish its own completion

**Anchor — RFC10-18 (Wave D2, unbound):**

> "A mission's executing agents, fleets, and workers **may report** that the completion predicate is satisfied and **may never establish it**. The `running → completed` transition is taken only by (a) an owner act, or (b) a declared, owner-approved evaluation independent of the executing principal…"

**Anchor — RFC10-7 (D1):** the envelope's minimum includes "the **completion establisher and effects-determination evaluator** (RFC10-18, RFC10-18(a))".

**The defect.** Denominator sweep for `complet` across all 1,011 D1 lines (21 matches, all read). RFC10-7 requires the establisher to be **named**; the rule that it must not be the executing principal, and the transitivity of that independence, exist only in RFC10-18. RFC10-6 (D1) governs the *predicate* (evidence tier, opposing artifacts → Unknown → escalation) but not *who takes the transition*. RFC10-8 (D1) carries a partial substitute — "an establisher named by the deriving agent binds nothing, and a child left without an inherited establisher never reaches `completed`" — but that limb is scoped to **derived children**; it says nothing about the top-level mission whose establisher the envelope names.

So under D1-only, an owner-approved envelope may name the executing principal as its own completion establisher, and no bound clause refuses it. The mission renders `completed` on its own say-so. This is the exact escape RFC10-18 exists to close, it arises with no effect class authorized, and it is outside the README's justification for the same reason B2 is.

**Severity: blocking.** Under VIS-2 this produces a green rendering with no established basis — the failure mode doctrine names first.

**Repair.** Add to RFC10-7 (or RFC10-6, whose subject is the completion predicate) a D1-side limb: the completion establisher named in an envelope is never the executing principal nor a principal it routed, and an envelope naming one authorizes no `running → completed` transition — with RFC10-18 stating the full adjudication rule at D2. Same shape as RFC10-8's existing child-side substitute, which shows the pattern already works.

(part 3/4)

## MAJOR

### M1 — The README's staging enumeration is stated as exhaustive and covers 4 of 15 sites

**Anchor — README.md L68–72:**

> "Cross-module references from the prevention plane into module 4 (the release table's recovery hooks, RFC10-18 naming in lifecycle text) are **staged references**: they bind when module 4 is accepted and, until then, mark duties that cannot yet arise because no effect class that would trigger them is authorized."

The parenthetical reads as a complete accounting of the seam. Swept denominator (15 normative D1→D2 sites, table in part 1 §3): it covers the four release-table rows and the two lifecycle-text RFC10-18 mentions. It does not name RFC10-23 (`prevention` L96), RFC10-18(a) (`prevention` L99, L135; `budget` L107), RFC10-18 (`prevention` L54, L135; `budget` L120), RFC10-19 (`mission-identity` L146; `budget` L52, L60, L160), or RFC10-20(d) (`mission-identity` L105; `prevention` L263).

This is a claim of absence without a denominator — verification rule 9 — inside the artifact whose purpose is to tell an owner what the seam is.

**Severity: major.** An owner reading the parenthetical would conclude the seam is two narrow things. It is fifteen.

**Repair.** Replace the parenthetical with a generated, complete cross-plane reference table (a script owning the measurement, not prose transcribing it — a generator that quotes prose has re-opened the door it closed), or drop the enumeration and state the rule categorically over all references.

### M2 — RFC10-16's own coverage-matrix range contradicts the README's restatement of it, inside one wave

**Anchor — RFC10-16, `mission-identity-approval-and-lifecycle.md` §2.4:**

> "No implementation work for user-observable Mission Control behavior … may be scheduled solely from this RFC — **including everything RFC10-17..22 requires of a runtime**. … At surface specification a clause-to-requirement coverage matrix over **RFC10-1..RFC10-22** is produced"

**Anchor — README.md §"Phase boundary":**

> "The clause text is in `mission-identity-approval-and-lifecycle.md` §2.4, and its clause-to-requirement coverage matrix must cover **RFC10-1…RFC10-24 across all five modules**, not module 1 alone."

[Observed] Direct contradiction. The clause's matrix stops at RFC10-22 and therefore excludes **RFC10-23** (D2) and **RFC10-24** — a clause defined in RFC10-16's *own module*, three sections above it. The index asserts a wider range than the clause it summarizes. Under rule 8 the clause is authority, so the effective coverage requirement is the narrower one, and the README misstates the binding scope of the package's phase gate.

This is the third recurrence of a specific figure: the acceptance record's own §3 correction note (RD-8 finding S2) records that the record said "RFC10-1..16" where the script reported RFC10 running to 22. The package now runs to 24 and two sites in the D1 bytes still say 22 (this one and m1 below).

**Severity: major.** RFC10-16 is the phase rule the README says "binds the whole package," and D1 would bind both statements at once.

**Repair.** Semantic delta amending RFC10-16 to "RFC10-1..RFC10-24" and its inner limb to "RFC10-17..23"; README then quoting the clause verbatim rather than restating its range. Per verification rule 10, batch with the other repairs — this review is bound to `570e6170…`, and editing the subject afterwards makes it worth nothing.

### M3 — `recovery_reserve` is un-evaluable standing alone, and the module's staging note claims a narrower dependency than the module has

**Anchor — `budget-reservation.md` §1 (the staging note):**

> "What happens *after* something goes wrong is module 4, `effects-recovery-and-stop.md`, which **this module's release table** names where a release depends on recovery duties having fired."

**Anchor — RFC10-17, closing paragraph (outside the release table):**

> "**`recovery_reserve` is sized, not merely present**: each compensating action an envelope names carries a **declared maximum cost** (RFC10-19), and `recovery_reserve` is not less than the sum of those declared maxima over every effect class the envelope permits; an envelope failing that inequality — including a derived child grant with no recovery_reserve of its own — authorizes no effect class that requires compensation."

**Anchor — RFC10-17, opening (also outside the release table):** "**recovery_reserve** (carved out of `authorized` … held undispatchable so that RFC10-19's compensating actions are fundable…)" and "the reserve is spendable only by RFC10-19's compensating actions."

**The defect.** The §1 note scopes the module's D2 dependency to the release table. Three of the module's five RFC10-19 references are outside it, and two of them are load-bearing on RFC10-17's own conformance test. Under D1-only no clause requires effect classification or names compensating actions, so the sum is over an empty set, `recovery_reserve = 0` conforms, and "authorizes no effect class that requires compensation" is vacuous — a conformance test a reviewer cannot run. The admission inequality degrades from `reserved_remaining + spent ≤ authorized − recovery_reserve` to `… ≤ authorized`.

Direction is safe under RFC10-7's cap (nothing to compensate), so this is not blocking on its own — but it is exactly the class of silent lean B1 makes dangerous the moment the cap lifts.

**Severity: major.**

**Repair.** Extend §1's staging sentence to name the `recovery_reserve` limbs alongside the release table, and add an explicit fail-closed statement to RFC10-17: until RFC10-19 is in force by owner act, no effect class outside RFC10-7's `propose-only` grant is authorized under any envelope, whatever the envelope declares.

### M4 — RFC10-5 binds a lifecycle whose failure path has no producing clause in this wave

**Anchor — RFC10-5, the vocabulary block:**

> "`running | paused | blocked → failed              (RFC10-18, RFC10-20(d))`"

Both producers are Wave D2. Under D1-only, `failed` is unreachable, RFC10-17(a)'s `failed` row never fires, and RFC10-19(a)'s sibling disposition never engages. The only terminal exits D1 can actually reach are `completed` (ungoverned — B3), `cancelled` (human act, no stated effect — B2), and `expired` (park expiry).

RFC10-5's own hedge — "[Inferred] This list is **provisional at this contract's acceptance**" — stages the *freezing* of the vocabulary against RFC 0008, not the absence of producers for a state the wave binds. And `mission-identity` L146 ("It ends the mission and fires RFC10-19's duties") states a consequence of park expiry that does not exist under D1-only, with no staging marker.

**Severity: major** — the wave binds a state vocabulary a third of which is inert, and says so nowhere in a clause.

**Repair.** Note in RFC10-5, at the vocabulary block, that `failed`'s producing clauses live in the correction plane and the transition is unavailable until that plane is in force; or fold into the B2 repair.

### M5 — The acceptance record's ordering guidance for act 5 names a gate that no longer exists

**Anchor — `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1, act-5 row:**

> "**Optional**: RFC-0010/0011 do not depend on it. **Recommended ordering: perform act 1 before act 5.**"

**Anchor — same file, §1 restructure note:**

> "the single **act 1** over the whole contract package **is replaced by six wave acts**"

[Observed] "Act 1" is retired. The act-5 row's ordering guidance points at a gate identifier that §1 itself abolished eleven lines earlier, so it resolves to nothing — and this is not cosmetic: act 5 is what discharges RFC10-24, and RFC10-24 is the D1 row's **entire stated safety property** (see part 4 §5). The one sentence telling an owner how to sequence the D3 act against the wave acts cannot be followed.

**Severity: major** (record-level, not in the D1 bytes — does not by itself block the act, but it sits on the D1 row's safety argument).

**Repair.** Restate as "perform Waves A, B, D1 and D2 before act 5," and add the D1↔D2 ordering constraint the B1/B2 repairs establish.

### M6 — The record's §7 item 9 anchors the no-self-widening prohibition on a clause that does not contain it and on an unbound wave

**Anchor — record §7 item 9:**

> "RFC 0001–0009 never cite RFC-0010/0011, so the no-self-widening rule has no redundant restatement inside the nine earlier contracts. … the corpus relies on **RFC10-15/RFC11-4 loading rules** to carry the prohibition into every mission context."

[Observed] `portfolio-and-cross-project-consent.md`, which defines RFC10-15, contains **zero** occurrences of "load", **zero** of "self-widening", and its two uses of "widening" are about minting the workspace governance store ("minting the store is an authority-plane widening that requires an RFC3-15-style recorded owner widening"). RFC10-15 has no loading rule and does not carry RFC10-8's prohibition anywhere. The other half of the item, RFC11-4, is Wave **C2** — unbound, and performed *after* D1 in the ceremony order.

So an owner-attention item at the gate rests on one mis-citation and one forward reliance into a wave that will not exist when D1 is performed.

**Severity: major** (record-level). This is the RD-8 class again: an item a reader consults to learn what the package relies on, never swept after the split.

**Repair.** Re-anchor item 9 to the clauses that actually carry the reach (RFC10-8's own text plus whatever RFC-0011 clause states the packet-loading duty), and mark the RFC-0011 limb as unavailable until Wave C1/C2.

## MINOR

### m1 — README §6 says the package has twenty-two clauses; it has twenty-four

> "Keeping the contract in one file — rejected at rev12: **twenty-two clauses and three sub-clauses** across two planes had reached the per-module word ceiling"

Verified by clause-definition sweep: **24 numbered + 3 lettered = 27**. Same stale-22 figure as M2, and the README's own frontmatter says "RFC10-1..RFC10-24". Repair: correct to twenty-four, or point at the generated count rather than transcribing one.

### m2 — README §4 says "one per clause" over a count that cannot be one per clause

> "**Moved to `../../history/RFC-0010-history.md` §"Violation cases"** — twenty-one worked scenarios, **one per clause**"

Twenty-one scenarios cannot be one per clause across twenty-four clauses, whatever the history file contains (not read; outside the wave and non-normative). Repair: drop "one per clause" or state the actual coverage.

### m3 — README has no §3

Sections run 0, 1, 2, **4**, 5, 5a, 6, 7, 8. A reader following a "§3" pointer from anywhere finds nothing and no note records the removal. Repair: renumber, or add a one-line "§3 removed at rev12" marker.

### m4 — README §5 Integration omits RFC 0004, which the README's own frontmatter declares a dependency

`depends_on: [RFC-0001, RFC-0002, RFC-0003, **RFC-0004**, RFC-0005, RFC-0006, RFC-0008]`. §5 has bullets for 0001, 0002, 0003, 0005, 0006, 0008, 0011 — no 0004 — while `budget-reservation.md` leans on it substantively ("or from an adapter-backed provider record (RFC 0004)"). The one section a reader consults for integration omits a declared edge. Repair: add the bullet.

### m5 — The RFC 0011 reference is a forward reliance into an unbound wave, stated with no staging marker

README §5: "**RFC 0011:** every mission-spawned agent run receives a governed context packet; the envelope is a mandatory packet input." Indicative mood, no "staged", no "when accepted" — unlike the module-4 references, which at least get a staging paragraph. Substantively harmless: RFC10-7's `propose-only` grant permits packet compilation on its own terms, and RFC10-21 (D1) supplies the load-bearing gate ("A context packet, prompt, summary, embedding, or any other composite assembled **under any mission** is subject, at the RFC5-15 choke point, to the egress-consent record of **every project whose content it embeds**"). Frontmatter is honest — **no D1 module declares `depends_on` RFC-0011** (verified across all five). Repair: mark the bullet staged.

### m6 — The record calls RFC10-17..22 "correction-plane clauses"

Record §3 correction note (RD-8 finding S2): "The gap was exactly **the six correction-plane clauses RFC10-17..22**." By the package's own clause map, RFC10-17 is module 3, RFC10-18..20 module 4, RFC10-21 module 5, RFC10-22 module 2 — four of the six are prevention plane, and three of them are in Wave D1. The mislabel is inside the note written to fix a stale figure. Record-level; does not touch the D1 bytes. [Observed]

### m7 — The record gives two counts for the 2026-08-07 review pass

§1 wave-history note: "closed with **two** independent 2026-08-07 reviews returning `REVISE`". §6: "**eight** independent reviews ran on 2026-08-07 and every verdict was `REVISE`". The D2 row's "both … reviews" agrees with two. [Inferred] These are probably a subset ("two concentrated on module 4") and a total, but neither sentence says so, and the reader cannot tell which number answers "how much review is bound to these bytes." Repair: state the denominator in the wave-history note.

(part 4/4)

## 4. Package self-description accuracy for the D1 set (task 3d)

**Accurate** [Observed, each verified by script or full read]:

- Clause map ↔ definition sites: exact, all 27, one home each, zero duplicates.
- Module frontmatter `clauses:` fields ↔ actual definitions: exact for all five.
- Module numbering ("module N of 5") and file names: consistent across all five.
- README §1 summary enumerates all of RFC10-1…RFC10-24 with no omission.
- README §8 lists q1/q2/q3 and each lives in the module owning its clause (RFC10-5 → module 1, RFC10-7 → module 2, RFC10-15 → module 5): correct.
- "the split is the package convention **seven of eleven** contracts already follow" — verified on disk: RFC-0002/0003/0004/0005/0007/0008/0009 are packages, RFC-0001 and RFC-0006 single files, RFC-0010/0011 the subjects. Seven. Correct.
- README declines to state module sizes and points at the generated budget report — correct discipline; no transcribed measurement anywhere in the set.
- The manifest header's own self-description ("RFC-0010 modules 1-3, 5 + package index; 5 module(s)") matches its rows and the disk.

**Inaccurate:** M2 (matrix range), m1 (clause count), m2 ("one per clause"), m3 (missing §3), m4 (missing RFC 0004 integration bullet).

## 5. Does the acceptance record describe Wave D1 accurately? (task 3c)

**Anchor — record §1, D1 row:**

> "`ACCEPT FOUNDATIONAL WAVE D1: 570e6170…8c0dff` | RFC-0010 modules 1, 2, 3, 5 (mission identity/approval/lifecycle; envelope/attention; budget reservation; portfolio/consent) plus the package index, per `wave-manifests/WAVE-D1-MANIFEST.txt`. Even accepted, RFC10-24 holds every mission in `awaiting-approval` until the D3 question (act 5) is ruled — this act is never an operating license"

**Accurate on scope** [Observed]: the argument equals the recomputed manifest digest; the module list matches the manifest and the disk; "plus the package index" correctly accounts for README.md.

**Accurate on the RFC10-24 claim** [Observed]: RFC10-24 says "no mission leaves `awaiting-approval`" until D3 or an owner ruling, and it is a defined clause in the D1 set. The record quotes its effect correctly.

**But the record's safety rationale is single-limbed and expires.** RFC10-24 is the *only* protection the D1 row names, and act 5's own row invites the owner to discharge it ("Optional … RFC-0010/0011 do not depend on it"). Once act 5 is performed, the D1 row's stated safety property is spent, and neither the record nor any clause supplies the successor — which is B1. The record also states no ordering between D1 and D2 anywhere: the §1 table's row order is A, B, C1, C2, D1, D2; only C1's row carries an ordering hint; and the one explicit ordering sentence in the whole record (act 5's) points at the retired "act 1" (M5).

**Correctly stated and worth recording:** the wave-history note's "**no confirming review is yet bound to any wave argument above**" is accurate as of `771965c` and correctly frames this review's status.

**Repair for the record.** Add to the D1 row: (i) the ordering constraint that Wave D2 be performed before any autonomy-level enumeration act, and (ii) an honest statement of what D1-only does *not* provide — stop guarantees, completion establishment, effect classification — rather than resting the whole safety case on RFC10-24. Fix M5's dangling "act 1". Fix M6's mis-citation.

## 6. What a mission can DO under D1-only, tested (task 3b)

Assuming act 5 ruled (so RFC10-24 no longer blocks) and the cap still at `propose-only` — the state the package intends:

**Bounded, clause-anchored, and I could not break it:**

| Capability | Bounded by | Wave |
|---|---|---|
| Drafts into `.syzygy/**`, `openspec/**` of declared targets, rendered unadopted | RFC10-7 `propose-only`; RFC3-16 | D1 + A |
| No push/PR/merge/deploy/publish/external mutation; no RFC5-22 class "whether or not the granted execution profile standing-approved it" | RFC10-7 | D1 |
| Provider egress | RFC5-14/RFC5-15 consent gates; RFC10-21's content-keyed composite rule | A + D1 |
| Cross-project composites | RFC10-21 — keyed to content, not to declared scope; fails closed on absent/unverifiable consent | D1 |
| Spend | RFC10-17's enforced-limit admission at the RFC5-21 launch gate and the RFC5-15 transmission predicate; Unknown spend treated as bound reached | D1 + A |
| Envelope widening | RFC10-8, including child-mission debiting and attention-allowance debiting | D1 |
| Guardrail prevention at the choke point | RFC10-10, honestly scoped to Syzygy's mediation | D1 |
| Parks | RFC10-5's maximum park duration, with a non-empty referent guaranteed by the wall-clock-budget argument | D1 |
| Attention volume | RFC10-22, whose class-(ii) exemption is *empty* under D1-only — tighter, not looser | D1 |

The README's claim that a `propose-only` mission's effects are "drafts inside the two governed namespaces, consented provider disclosure, and reserved spend — each bounded by modules 1–3 and 5" **survives testing.** [Observed] I could not construct a dimension-(ii) effect reachable under D1-only.

**Not bounded:**

1. **Stopping it.** B2. The human act exists; its guarantee does not.
2. **Completing it.** B3. The transition has no gatekeeper.
3. **Everything, the moment §8 q2 is answered.** B1. No clause holds the cap against a level-enumeration act performed before Wave D2.

The pattern is consistent: the package bounds what a mission may **cause**, and leaves what a human may **do about it** in the other wave. The README's justification is written entirely in the vocabulary of the first — "no effect class that would trigger them is authorized" — which is why the second slipped through.

## 7. Method statement

- All digests recomputed in-session by script (`hashlib`), never transcribed.
- All searches used Python `re`, never the system `grep` (ugrep; `[^]]`-style classes silently match nothing).
- Every absence claim in this review carries its sweep and denominator: the cross-plane enumeration (1,011 lines / 5 files), the stop sweep (1,011 lines, 62 matching lines all read), the completion sweep (1,011 lines, 21 matches all read), the staging-language sweep (1,011 lines), the clause-definition sweep (27 sites / 6 files), the partition sweep (6-file population), the citation-resolution sweep (24 of 24 targets).
- Every finding is anchored to a defined clause and quotes it. Where I rely on the README, I say it is not a clause — that is the finding.
- All six package files read in full, including the D2 module (seam evaluation only; no acceptance judgment rendered on it).
- Exclusions honored: `round-2026-08d/`, `history/`, all `reviews/`, `_bootstrap/` unread. The history file's contents are therefore [Unknown] to me, and m2 is stated as an internal inconsistency, not a claim about it.

## 8. Disposition

The manifest is clean, the partition is exact, the citations resolve, and the prevention plane is a genuinely rigorous piece of contract drafting — RFC10-7's narrowest-reading rule in both directions, RFC10-8's sibling-sum invariant over attention as well as budget, RFC10-17's enforced-limit admission, RFC10-21's content-keyed consent, and RFC10-5's park bound are each better than the defect they close. Nothing here suggests the wave is unsalvageable, and nothing suggests the split was the wrong idea.

But the wave is offered on a claim — that the prevention plane stands alone — whose one statement lives in a file that defines no clause, and which two concrete duties falsify. Accepting D1 at these bytes would bind an index sentence the owner would reasonably read as a guarantee, and a clause set that does not make it one. The repairs are small and local: one limb on RFC10-7, one limb on RFC10-5 (or a module move for RFC10-20), one limb on RFC10-6 or RFC10-7, a generated seam table, and a range correction in RFC10-16. Batch them — this review is bound to `570e6170…8c0dff` and editing the subject afterwards makes it worth nothing.

VERDICT: REVISE

---

**[Storage note — not part of the review of record.]** After the four parts
above were delivered and stored, the reviewer sent one further handoff
message before approving shutdown (2026-08-09). It is procedural guidance
for the repair pass, stored verbatim below on the same terms as the review:

> Acknowledged — approving shutdown next. One standing note for whoever handles the repairs:
>
> RD-20 is bound to `WAVE-D1-MANIFEST.txt` sha256 `570e617091bb41d8b34ca17b09e12f41d22e4d592a23249c8a737a698f8c0dff`. Any edit to any of the five D1 files retires this review (verification rule 10). Batch B1, B2, B3 and M1–M4 into a single repair pass, regenerate the manifest by script, and re-review at the new argument — the repairs are small and local, so one pass should carry all of them.
>
> M5 and M6 are record-level (`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`), outside the D1 bytes, and can be fixed without disturbing the digest.
