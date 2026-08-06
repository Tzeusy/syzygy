# Dispositions — reviews RC-11 and RC-12

> **Non-authoritative round record.** Raw reviewer output is in `reviews/` and
> is never edited. Where this file and a raw review disagree about what a
> reviewer said, **the raw review wins**; where this file and a contract
> disagree about what a clause says, the clause wins.
>
> Verdict words are copied, not summarised. `EXCEPTIONS` is not `ACCEPT`, and
> `REVISE` is not "passed with findings".

| Review | Commission | Verdict, copied |
|---|---|---|
| **RC-11** | Confirming review of the RC-10 repairs, over the exact bytes act 1 binds, with no authoring context | **`VERDICT: REVISE`** |
| **RC-12** | Independent ruling on the context-packet budget waivers (charter §12.4) | **`VERDICT: EXCEPTIONS`** |

Neither verdict licenses an act. RC-11 is the review criterion 8 was waiting
for, and it returned REVISE — so criterion 8 is **unmet**, now for a stated
reason rather than for absence of a review.

---

## RC-11 — eight findings

### Fixed in this session

| # | Finding | What was done |
|---|---|---|
| **RC11-C** | Nine stale derived word counts remain in `RFC-0009/README.md`'s word-accounting section, of the same class the prior repair corrected elsewhere **in the same file** — leaving it stating module 1 as 6,996 at `:49` and 6,999 at `:204`. Inside act 1's digest set | All nine corrected (6,996 / 5,538 / 3,023 / 15,557 / 2,025, delta −3,712, and the three inline repeats), each recomputed by two methods. A tenth of the same class — the package-index self-count at `:208` — was found by the widened check below and is included. `ACTIVE-CONTRACT-MANIFEST.txt` regenerated, and **act 1's argument re-quoted a third time** |
| **RC11-D** | CG-21 cannot see the class it was written to close: its row matcher requires a backticked module filename, so `\| module 1 \| 6,999 \|` passed. Mutation-tested by the reviewer at `111,111` — `OK, 19 rows, 0 findings` | CG-21 gained **pass B**: every comma-formatted figure in a package README must equal a quantity recomputable from the package now (a module count, their sum, the index's own count, the package union, or index-plus-one-module), or its window must mark it as a frozen pre-compaction source or a threshold. Two marker classes with different windows — a `~9,500 target` two lines away had exempted the stale `2,029` before they were separated |
| **RC11-F** | The offering and the readiness report state "32 checks / 19 fixtures" where the battery reports far more, in the two **"Evidence you can reproduce"** blocks an owner is sent to. They also contradicted `PROJECT-STATUS.md` | Every frozen figure **withdrawn** rather than refreshed, in all four documents. The commands stay; each check prints its own denominator. A derived value quoted outside its owning artifact is what went stale — twice — and refreshing it a third time would only reset the clock |
| **RC11-G** | "each check shown able to fail" is asserted and false: fixtures reached 9 of 33 check families. RC-10 raised it as item vi; the repair added 29 fixtures, all in the range that already had coverage, making the sentence *less* true as a proportion | **CG-24** computes the denominator instead. It reads the fixture names out of the checker's own `selftest()` and compares them against the identifiers the battery reported this run — currently **14 of 24 check families covered**, with the ten uncovered enumerated every run. Adding a check with no fixture now shows up on the same run. Prose corrected in all four documents |
| **RC11-H** | The RFC2-24 denominator repair replaced one unreproducible figure with two: "13 inside the 32 modules" and "20 across all candidate material" reproduce as 15/16 and 28 | Both figures **withdrawn** and marked `[Unknown]`. A third independent sweep in this session got 17/14 and 31/21 — the count moves with how much text may sit between `RFC2-24` and `#N`. The claim that is stable, and is the one that matters, is stated instead: **no ordinal disagrees with the table**, under every sweep run so far |
| **RC11-E** | RC-10's finding **RC10-F** was reframed into a different defect and thereby dropped: the F6 row says RFC10-20 "bounds latency (undeclared means synchronous)", when RC10-F was that a synchronous stop whose run will not die has *no timeout, no failure disposition, and no Attention Item* | The F6 row now states RC10-F as open, in the reviewer's own terms: a synchronous act with no failure path is an unbounded latency with a different name |

### Open — contract text, and not closable in this pass

| # | Finding | Why it is open |
|---|---|---|
| **RC11-A** | The RFC10-18 repair **introduced a false citation inside act 1's digest set**: it says the mission enters `blocked` "awaiting the human resolution act RFC10-5 requires", but RFC10-5 scopes that act to blocks arising under RFC10-8 or RFC10-11. An RFC10-18-sourced block arises under neither. A reader of RFC10-18 alone now believes a human resolution act is owed; it is not — and the indefinite park survives in the no-applied-effects case, holding its budget reservation, since RFC10-17 releases only on completion or termination | Repairing it is a normative edit to a clause written to close RC-10's finding, and any repair needs its own fresh review. Doing it here would mean this session drafting a fix to its own commissioned review's finding and then declaring it closed — the loop RC-10 and RC-11 have each already caught once |
| **RC11-B** | **The next escape.** RFC10-18 pivots its whole correction plane on "whether effects have been applied" and assigns that determination to nobody: no independent party, no evidence tier, no Unknown rule — while the *other* determination in the same paragraph is meticulous about all three. An executing principal that asserts no effects were applied routes itself to `blocked`, outside the correction plane, and RFC10-19's duties never fire. RFC10-17, written in the same pass, states the fail-closed Unknown rule for exactly this shape ("Unknown spend is never read as zero spend"); RFC10-18 states none | Same reason, and the reviewer rates this the more serious of the two. The corpus-wide answer under VIS-2 and RFC2-23 is that an Unknown "were effects applied?" is not zero — so the fail-closed reading is `failed`. Writing that into the clause is the obvious repair and is still a normative edit needing review |

Both are now owner-visible as **P-27** in
`../../../decisions/PENDING-OWNER-DECISIONS.md`. RC-10's minimum-to-CONFIRM
item 6 asked that the `blocked` contradiction be recorded as an owner item; it
was addressed by clause text instead and, RC-11 notes, was therefore *recorded
nowhere as open*. That is now fixed regardless of how the clause is repaired.

### Also carried, from RC-11 §8

RC-11 re-checked RC-10's ten open items and found two further classes this
session did not close:

- **RC-10 item x** — RC-7 asked that the RFC-0010 correction-plane clauses be
  inserted *after* act 1; they were inserted before, and the deviation is
  still unrecorded in either offering document. [Observed by RC-11's sweep.]
- **RC-10's other clause-level findings remain undisclosed** in the imperfect
  table: RC10-C (RFC10-17's `spent` has no independent measurer), RC10-D (a
  *failed* compensation is recorded and nothing more), RC10-G (RFC10-21's
  predicate keys on mission scope, the harm on content provenance — under an
  F7 row still marked "Closed"), RC10-H (RFC10-22's bound can suppress notice
  of itself).

Both are carried into **P-27** rather than fixed here, for the same reason.

### Checks RC-11 found unable to fail

1. **CG-21 over any README figure outside a module row** — closed above.
2. **CG-1 through CG-12 have no fixture at all**, 22 of the then-33 reported
   results, including all four CG-7 sub-checks. RC-11 demonstrated CG-7a *is*
   able to fail and made no claim about the other 21: **[Unknown]**. This is
   now printed every run by CG-24 rather than left to a sentence.
3. CG-17's routed-but-undeclared exemption is loose — raised as narrow, not a
   finding.

---

## RC-12 — four waivers ruled, and its own exceptions

**All four breaching fixtures ruled `WAIVER SOUND`**: fixture 2 (24,680 est.
tokens, +23.4%), fixture 7 (21,246, +6.2%), fixture 8 (30,026, +50.1%),
fixture 9 (32,433, +62.2%). None was ruled `DECOMPOSE` or `WAIVER REJECTED`.

Every waiver in the set previously recorded its reviewer as **unassigned** —
which is what charter §12.4's "explicit **reviewed** waiver" turns on. RC-12's
signature, scope, and expiry fields are now installed in all four fixtures:

| Fixture | What was installed |
|---|---|
| 2 | **All five fields** — it had no waiver block at all, only prose against the wrong line (RC-12 finding **F-1**: it named the 15–20k *working target* and never the 20,000-token *decomposition trigger* it actually crossed, the only fixture in the breach set not to name the line it crossed, and the only one in the accepted set). The trigger is now named first, the correction is stated, and the block carries three early-revisit conditions |
| 7 | Reviewer; scope tightened to CC-BAR-5-floor-7-classified identity work; expiry made conditional on **RFC-0001 becoming divisible** — 53% of the packet is that one file, so divisibility voids the justification rather than weakening it |
| 8 | Reviewer; scope narrowed to capabilities whose surface contract is **RFC-0007**; expiry made unconditional at the **creation of `openspec/**`** — the packet renders the absent house conventions as an RFC11-6 Unknown, and the moment conventions exist the measured floor changes |
| 9 | Reviewer; scope narrowed to warrants spanning the **retention × cause coupling**; expiry made conditional on **owner act 2**, since CC-TEST-2 is in the packet and is act 2's subject |

**RC-12's verdict was `EXCEPTIONS`, not `ACCEPT`,** and its exceptions are not
discharged by installing the fields. Read `reviews/RC-12-budget-waiver-RAW.md`
§5 and §7 in full; the two that bear hardest:

- **The threshold these waivers are granted against is installed nowhere.**
  `CC-BUDGET-1` lives in a candidate policy with no owner act, and no
  `CC-BUDGET-*` identifier resolves to a governed artifact today. A waiver
  against a rule that does not bind is a different object from a waiver
  against one that does, and RC-12 says so about its own signature.
- **Four of nine fixtures breach, one by 62%** — RC-12 questions whether an
  absolute 20,000-token line is the right instrument at all, as a
  *recommendation*, explicitly not a finding.

RC-12 also raised **F-5**: fixture 9's declared Shard 1 is incomplete for its
own warrant, with a corrected split measured at 18,943 tokens. That correction
is **not** installed — it changes the fixture's proposed decomposition, which
is a design choice the fixture's author should make with the measurement in
hand. Carried in P-27.

---

## What these two reviews change about readiness

**Criterion 5** (context packets complete and automatic) — the *complete* half
moves: the class map is eight-for-eight, and every breaching packet now
carries a reviewed waiver with a named reviewer and a real expiry. The
*automatic* half does not move and cannot in this phase: there is still no
compiler, and every selection in the set is hand-authored.

**Criterion 8** (the exact package passes a fresh semantic review) — **unmet.**
RC-11 is that review and it returned `REVISE`. Six of its eight findings are
fixed above; two are contract-text defects inside act 1's digest set, one of
which the repairs introduced. Fixing those needs another confirming review,
which is the shape criterion 8 has held for two rounds: **a repair pass and
the review of that pass cannot be the same pass.**
