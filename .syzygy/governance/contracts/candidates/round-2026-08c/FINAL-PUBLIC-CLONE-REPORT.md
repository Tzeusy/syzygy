# Public clone verification — final report

> **Non-authoritative round record.** The raw review is
> `reviews/RD-7-public-clone-RAW.md` and is never edited. Where this file and
> the raw review disagree about what the reviewer found, **the raw review
> wins**. Verdict words are copied, not summarised.

## The commission and the verdict

An independent reviewer cloned the repository, ran everything **inside the
clone**, and attempted each of the five acceptance acts using nothing but what
git tracks — no `_bootstrap/`, no founder-local settings, no working-tree
state.

**`VERDICT: EXCEPTIONS`.**

> **5 of 5 acts performable from a fresh clone.** All five arguments recompute
> from clone bytes; all 32 module digests match; both `sha256sum -c` ceremony
> steps execute as written; the battery is clone-identical, fails when it
> should, degrades honestly without git, and writes nothing.

**Criterion 11 — acceptance ceremony executable from a clean clone — is met.**

## What the clone proved

- **All 32 module digests recomputed independently**, not a sample. The
  reviewer widened its own commission — it was asked for six — and reports
  every one matching.
- **Both `sha256sum -c` ceremony steps execute as written.** The ceremony is
  not merely described; it runs.
- **The battery is clone-identical**, and **degrades honestly without git**:
  CG-11 declines to run and says so, rather than guessing tracked status.
- **Nothing founder-local is load-bearing.** No tracked file depends on, or
  instructs a reader to open, anything a clone does not contain — with one
  exception recorded below (S9-class identifiers, found by RD-8).
- **No script writes outside the repository.**

## The exceptions, in the reviewer's severity order

### E-1 · The link checker could not detect a wrong-depth path — **closed**

`_resolve`'s suffix fallback ended with `str.lstrip("./")` on the normalized
target — which strips **characters, not a prefix**, so every `../` was
discarded and the reference matched any file with that name anywhere.

**Mutation-proved**: a markdown link **seven levels up, pointing outside the
repository**, over which the battery reported `0 findings` while the
denominator incremented.

**Closed.** `_resolve` now refuses the suffix fallback for any target that
states its own depth: *an author writing `../../history/...` has made a claim
about where the file sits, and a wrong claim must fail rather than be rescued
by a filename match somewhere else in the tree.*

**Mutation-tested both ways this session**, in a tracked-files copy: a
wrong-depth markdown link fails CG-1a, a wrong-depth code span fails CG-1b,
and the source tree returns to `0 FAIL` when they are removed.

**What the fix surfaced — 15 references that had been invisible:**

| Class | Disposition |
|---|---|
| Raw reviewer output and superseded round records | **Classified into CG-1f**, which was widened from raw review to a *frozen lane*. RD-7 noted the asymmetry that CG-1a had **no** frozen-lane branch at all while CG-1b did; CG-1a now has one |
| The rev9 clause-migration matrix's nested module paths | `HISTORICAL_PACKET_TARGET` widened; same frozen tree as the paths it already covered |
| **`CONTEXT-BUDGET-REPORT.md` → `../round-2026-08b/reviews/RC-12-…`**, ×4 | **Genuinely broken, and closed at the generator** |

### The generator defect E-1 uncovered, and it is the round's pattern again

The four broken pointers were **transcribed out of the fixtures' waiver
fields**. A fixture lives one level *below* the report, so `../round-2026-08b/`
is correct where it was written and points above the package where it was
copied.

**This is the measurement defect in a different currency: a value correct in
its own frame, transcribed into a frame where it is false.** The generator now
re-parents one leading `../` and **prints every rewrite**.

**And the audit trail became the defect on the first attempt.** Printing the
original path in a backtick span reproduced the broken reference inside the
report auditing it — caught immediately by the newly-fixed check. The listing
now prints `old → new` in plain text.

**That is twice in one session** that writing down a broken pointer reproduced
it (the other was `PROCESS-LESSONS.md`). The check was right all three times.

### E-2 · A module inside act 1's digest set points at its history at a depth that exists nowhere — **open, disclosed**

`rfcs/RFC-0010-mission-control-autonomy.md` cites its amendment history at
**four lines**, at a depth that resolves in neither the candidate tree nor the
governed tree after the act.

**RD-7 swept all 32 modules: RFC-0010 is the only module with the defect.** The
other three flat modules are clean — the `../../` form is correct for the
*nested* modules and was carried onto a flat one.

**Not repaired.** RFC-0010 is frozen at `7f823aa3…` against two Mission-safety
reviews bound to those bytes. The target is explicitly **non-normative
rationale**, and the pointer's brokenness changes neither what act 1 binds nor
whether its digest verifies — but **the owner is being asked to bind bytes in
which the contract's own route to its rationale is dead.** Stated in the
acceptance packet; batched with the RFC-0010 package split.

*(The check classifies these four into CG-1d's frozen-packet bucket rather than
failing, because `../../history/` matches the rev9 pattern. That
classification is wrong on its reason and right on its effect; the reference is
printed every run either way.)*

### E-3 · Performing act 1 breaks eight pointers, and the record claimed it fixes them — **the claim is corrected; the pointers are not**

RD-7 **simulated the install exactly as documented** and swept the installed
modules: **81 relative backlinks examined, 12 unresolved, 8 breaking as a
direct consequence of the act.**

Six package READMEs and one more point two levels up at the context budget
report and the 03 compaction report. Both resolve today, where two levels up is
the candidates package, and stop resolving after the act, where two levels up
is `governance/` — because the install copies `history/` and `matrix-rows/` and
not the package-level reports.

**The record's install paragraph said the install exists so those backlinks
*resolve* from the governed tree.** For these eight it does the opposite.

**Corrected in the acceptance record**, which now states the measurement, names
the two ways to close it, and says neither is done. **The pointers themselves
are inside act 1's digest set and are not touched.**

**`CG-14` checks install *routes*, not installed content's internal links.**
RD-7 recommends a post-install link-resolution pass; **that check does not
exist**, and this report does not claim it does.

### E-4 · Act 5's phrase form exists only as a retired value and a template — **open, carried**

CG-7d's act-5 predicate has a **zero live denominator**, leaving CG-7e as its
sole guard. Carried from review RC-9, unrepaired. **A predicate with no
population verified nothing** — verification rule 4, applied to the check
battery's own coverage.

## What this closes

**Criterion 11 is met**: five of five acts performable from a clone, all 32
digests recomputed there, both ceremony steps executed, the battery
clone-identical and honestly degrading.

**And the review paid for itself twice over.** E-1 was a defect *in the
instrument* — the check that the whole repository leans on for pointer
integrity could not fail on the one class of error a human most often makes.
Fixing it surfaced a real broken pointer inside a generated artifact, a real
broken pointer inside act 1's digest set, and a false claim in the acceptance
record about what the install does.

**A check that cannot fail is not a check**, and this one had been passing for
every commit of this round.

## What remains open

| # | Finding | State |
|---|---|---|
| **E-2** | RFC-0010's history pointer is dead at four lines, inside act 1's digest set | Frozen, disclosed in the acceptance packet, batched with the package split |
| **E-3** | Act 1's install leaves eight dead pointers in the accepted tree | Claim corrected; pointers frozen. **No post-install link check exists** |
| **E-4** | Act 5's digest-bound phrase form has a zero live denominator in CG-7d | Carried from RC-9 |

## Clone re-run at the round's close

RD-7's review was performed at `a7b3375`. The repairs above landed after it, so
the battery was re-run in a **fresh clone taken at `99e141a`** — the commit
carrying every repair this round made.

```text
26 OK, 14 WARN, 0 FAIL (40 checks) — counts derived, not asserted
77 fixtures, 0 failing — a check that cannot fail is not a check
PASS — all checks clean                       (verify_final_prespec.py)
index matches regeneration — no drift         (build_contract_index.py --check)
dependency index matches regeneration         (build_dependency_index.py --check)
fixture anchors match regeneration            (build_budget_report.py --check)
CG-7a…CG-7e — all OK, 0 findings
```

**Clone-identical to the working tree at that commit.** Per verification rule
7, **this clone report is valid only for `99e141a`** and says nothing about any
later commit.

**It is not a substitute for RD-7.** A clone run by the session that wrote the
repairs verifies that the checks pass; it does not verify that the repairs are
right. The three open exceptions above are unchanged by it.
