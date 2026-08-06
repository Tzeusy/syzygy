# RC-11 — Confirming review of the RC-10 repairs

**Reviewer role:** independent confirming reviewer, commissioned to read the
repairs made in response to RC-10. No authoring context. Did not read any
conversation transcript and did not read `_bootstrap/**`.

**Subject:** commits `f96ff6b~1..7f0efa4`, with particular attention to the
seven files inside act 1's digest set that changed.

**Question answered:** do the repairs fix what RC-10 found, without introducing
a new defect, and are the derived figures they carry correct?

---

# VERDICT

VERDICT: REVISE

---

## 0. Condition of the review

**[Observed] The working tree moved under me while this review ran, again.**
At session start `git status --porcelain` showed two untracked files. During
the review the following acquired uncommitted modifications, none by my hand:

```
scripts/check_governance.py                     (CG-8 rework: DEFAULT_LOAD, token estimates)
AGENTS.md                                       (rewrite of the router prose)
.syzygy/governance/policies/GOVERNANCE-SUBSTRATE-LOCK.yaml
round-2026-08b/SUBSTRATE-REPRODUCIBILITY-REPORT.md
.beads/issues.jsonl                             (staged)
```

This is the same condition RC-10 opened with. Two consequences:

1. **My first battery run used a modified `check_governance.py`** and is
   discarded. **Every figure in this report was produced in a pristine
   `git clone` of the repository checked out at `7f0efa4`**, with `_bootstrap/`
   confirmed absent. [Observed]
2. The substrate lock is being edited while `CG-19` — rebuilt this round
   specifically to parse it — is cited as evidence in three artifacts. Any
   CG-19 result quoted from the working tree is a result about a moving file.

**[Observed] My footprint on the repository is zero.** All mutation testing was
done in `/tmp/.../clone` and `/tmp/.../mut`, restored with `git checkout --`
after each mutation (`git status --porcelain` in the clone returned empty). The
file you are reading is the only file I created. I ran no script in its
writing mode; in particular I did **not** invoke `build_contract_index.py`
without `--check` (RC-10's disclosed foot-gun — it is still there).

### What I read

RFC-0010 in full; RFC10-5, RFC10-6, RFC10-7, RFC10-8, RFC10-11, RFC10-12,
RFC10-13, RFC10-17…22 clause-by-clause; the six package READMEs; RFC-0002's
RFC2-24 reason table; `RC-10-final-confirming-RAW.md` in full;
`MISSION-SAFETY-CLOSURE-REPORT.md`; `FINAL-OWNER-ACCEPTANCE-RECORD.md`;
`FINAL-PRE-SPECIFICATION-READINESS-REPORT.md`;
`FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md` and `FINAL-HUMAN-CLARITY-REVIEW.md`
diffs; `PUBLIC-CLONE-VERIFICATION-REPORT.md`; `PROJECT-STATUS.md`;
`ACTIVE-CONTRACT-MANIFEST.txt`; `scripts/check_governance.py` (CG-15, CG-16,
CG-17, CG-20, CG-21 read as source).

### What I did not read

`_bootstrap/**`; any authoring conversation; `history/`; RC-1…RC-9 raw reviews
(I read RC-10 only, plus RC-7 quotations as they appear inside RC-10);
RFC-0001…0009 as substantive contract text — my adversarial clause reading was
scoped to RFC-0010 as commissioned, so **the substantive correctness of the
other 31 modules is [Unknown] to me**. I did not re-run the semantic-equivalence
fixtures under GNU grep.

---

## 1. The bytes, first

**[Observed] Act 1's argument is correct for the corpus it names.**

| Check | Method | Result |
|---|---|---|
| Manifest body vs recomputation | `find rfcs -name '*.md' \| sort \| xargs sha256sum`, `diff`ed against the manifest body | **32 of 32 exact, zero differences** |
| `sha256sum ACTIVE-CONTRACT-MANIFEST.txt` | by hand | `ac07a06497cd72b8dd10a9a42776a6a41d7c45740ffec7905d4c27fbe7146b4f` |
| Matches `FINAL-OWNER-ACCEPTANCE-RECORD.md` act-1 row | by eye against the recomputed value | **yes** |
| Three modules recomputed individually | `sha256sum` on `RFC-0009/README.md`, `RFC-0010-…autonomy.md`, `RFC-0007/README.md` | all three match their manifest lines |
| CG-7a output | clone at `7f0efa4` | `OK … 32 entries examined, 0 findings — manifest sha256 ac07a064…` |
| CG-7b/7c/7d output | same | `OK`, 1 / 3 / 7 items examined, 0 findings |

**[Observed] CG-7a is able to fail.** I appended one word to
`RFC-0009/README.md` in the clone: `FAIL CG-7a — 32 entries examined, 1 finding`.
Restored. Note CG-7b stayed `OK` under that mutation, which is correct — 7b
compares the record's quoted argument to the manifest file, and the manifest
file did not move. The pair is only sound when read together, which the
acceptance record's gating rule ("a CG-7 failure means do not perform that
act") does correctly.

**Finding: none. This remains the strongest part of the package.**

---

## 2. RC-10 finding 1 — the RFC10-18 escape

### 2.1 What the repair actually did

The adopted text (`RFC-0010:388-404`) now reads, in the relevant part:

> Where no independent establisher is available for a mission's objective
> class … the mission **never reaches `completed`**. Which state it does reach
> depends on whether effects have been applied: with no applied effects it
> enters `blocked` with an Attention Item, awaiting the human resolution act
> RFC10-5 requires; **with effects already applied it enters `failed`**, so
> that RFC10-19's compensation, enumeration and disposition duties fire.

**[Observed] Two of RC-10's three limbs are genuinely closed.**

- **RC10-A closed.** The prior text said the mission "**terminates as
  `blocked`**". The word "terminates" is gone; the new text says "enters
  `blocked`". The contradiction with RFC10-5's `running → blocked (→ running
  on unblock)` edge is removed at the level of vocabulary.
- **RC10-B closed for the effect-bearing case.** An effect-bearing mission now
  enters `failed`, which is inside RFC10-19's closed trigger set
  (`failed`/`cancelled`/`expired`), so compensation attempts, irreversible-effect
  enumeration, and the terminal-reason disposition all fire. I re-read
  RFC10-19 against this and confirm the keying is exact.

### 2.2 FINDING RC11-A [Observed] — the repair introduced a false citation, inside act 1's digest set

The new text says the mission enters `blocked` "**awaiting the human resolution
act RFC10-5 requires**".

RFC10-5 (`RFC-0010:139-143`) states:

> exit from `blocked` **where the block arose under RFC10-8 or RFC10-11** is a
> **human resolution act** — an agent's "condition cleared" assertion never
> takes that transition.

An RFC10-18-sourced block arises under **RFC10-18**, under neither RFC10-8 nor
RFC10-11. RFC10-5 does not require a human resolution act for this class of
block. **RFC10-18 now cites RFC10-5 for an obligation RFC10-5's own stated
scope excludes.**

RFC10-5 was not amended — the diff `f96ff6b~1..HEAD` touches only RFC10-18's
body and the amendment log, and I confirmed RFC10-5's text is byte-unchanged.

This is not a quibble about referencing style. RC-10 stated this exact scope
mismatch in its §2.3, citing RC-7's non-blocking **F13** ("Escalation-sourced
`blocked` states have no human-exit rule"): *"an RFC10-18-sourced block arises
under neither, so even that exit rule does not reach it."* The repair read that
paragraph — the closure report quotes its neighbours — and closed the
effect-bearing half while converting the unaddressed half into a citation that
reads as though it were closed. A reader of RFC10-18 alone now believes a human
resolution act is owed. It is not.

**Consequence: the indefinite park survives in the no-applied-effects case.**
Nothing obliges anyone to resolve it. RFC10-13 requires the *Attention Item* to
terminate (resolution, expiry-to-safe-default, or dismissal) — but an item
expiring to its safe default resolves the item, not the mission's state, and
RFC10-12 requires the expiry default be safe, i.e. it "may narrow, pause, or
block". The mission stays `blocked`, with no terminal state and therefore no
terminal reason.

That has a concrete cost, not just an aesthetic one. RFC10-17 defines
**released** as "reserved-but-unspent, returned **on completion or
termination**". A mission parked in `blocked` reaches neither, so its
reservation is never released, and under RFC10-8's sibling-sum invariant the
parent envelope's headroom is consumed permanently. Parking is now a way to
hold budget.

### 2.3 FINDING RC11-B [Inferred] — the next escape: the branch selector is self-adjudicable

The repair pivots the whole correction plane on one predicate: **"whether
effects have been applied."** RFC10-18 assigns that determination to nobody.

The clause is meticulous about independence for the *other* determination in
the same paragraph — the `running → completed` transition is taken "never by
the principal that performed the work, and never by a principal that principal
routed", with `gate-backed` evidence required and an unstated tier defaulting
to `gate-backed`. **None of that attaches to the effects-applied
determination.** I swept RFC-0010 for every occurrence of `appl(y|ied|ies)`
(Python `re`, 14 hits, all read): the determination is never assigned to an
independent party, carries no evidence-tier requirement, and has no Unknown
rule.

The scenario I could not find a clause to stop:

> A mission with applied effects reaches its completion predicate. No
> independent establisher exists for its objective class. The executing
> principal — which is permitted to *report*, and whose report is the only
> input to this branch — asserts that no effects were applied. RFC10-18 routes
> it to `blocked`. RFC10-19's duties, keyed to `failed`/`cancelled`/`expired`,
> never fire: no compensation is attempted, no irreversible effect is
> enumerated, no terminal reason states any disposition. RFC10-5's exit rule
> does not reach the block (§2.2). The mission parks, and the applied effects
> stand, unreported.

The clause names this hazard in its own next sentence — "routing an
effect-bearing mission to `blocked` would place it outside the correction plane
entirely" — and then leaves the routing decision with the party that benefits
from taking it. This is RC-10's original finding relocated by one step, not
eliminated: before the repair the escape was *route to `blocked` to avoid
adjudicating completion*; after it, the escape is *assert no effects were
applied to avoid the correction plane*.

**The asymmetry with RFC10-17 is the sharpest evidence that this is an
oversight rather than a decision.** RFC10-17, written in the same pass, states
an explicit Unknown rule for exactly this failure shape: "**Where measured
spend against a bound is Unknown (RFC8-19, RFC2-23), the bound is treated as
reached** … Unknown spend is never read as zero spend." RFC10-18's new branch
states no such rule. Under VIS-2 and RFC2-23 the corpus-wide answer is that an
Unknown "were effects applied?" is not zero — so the fail-closed reading is
`failed`. The clause does not say so, and RC-10's own RC10-C criticised
RFC10-17 for the *narrower* version of this gap (who measures `spent`).

**[Inferred]** I rate this the more serious of the two, because it is live
under the propose-only cap in the same sense F3 already was.

### 2.4 Verdict on finding 1

**Partly closed.** RC10-A closed; RC10-B closed for effect-bearing missions as
determined by an honest executor. A new false citation was introduced inside
act 1's digest set, and the escape survives behind an unassigned, unevidenced,
Unknown-silent predicate.

The closure report's F3 row calls this "**Closed, after one repair**". On my
reading that is the same category of overstatement RC-10 penalised in the F4
and F6 rows, and the report demonstrated in those two rows that it knows how to
write the honest form.

**[Observed] Cosmetic, noted once and not weighed:** the repair left
`RFC-0010:402` unwrapped at 121 characters in a clause body otherwise wrapped
at ~76. It is a visible edit seam. Long lines exist elsewhere in the corpus
(front matter, headings), so this violates no rule I can find.

---

## 3. RC-10 finding 2 — the stale derived word counts

### 3.1 What the repair fixed, independently recomputed

I recomputed every module's word count with `wc -w` and, as a second method,
Python `len(open(f).read().split())` — the same operation the repository's
`words()` helper performs (`check_governance.py:174-175`). **The two methods
agreed on every file**, so the README's stated basis ("Counts are `wc -w`")
and the checker's basis do not diverge for this corpus.

**[Observed] All 19 module rows across the six package READMEs now recompute
exactly — 19 of 19.** Verified against my own `wc -w` sweep, not against CG-21.

| Package | Rows | All correct? |
|---|---|---|
| RFC-0002 | 4 (1,955 / 2,225 / 2,470 / 2,388) | yes |
| RFC-0004 | 4 (1,677 / 3,682 / 1,770 / 1,737) | yes |
| RFC-0005 | 3 (3,635 / 2,343 / 2,192) | yes |
| RFC-0007 | 2 (5,165 / 3,142) | yes |
| RFC-0008 | 3 (2,684 / 3,504 / 3,051) | yes |
| RFC-0009 | 3 (6,996 / 5,538 / 3,023) | yes |

**[Observed] The RFC-0007 package figures are correct, and the repair fixed
two RC-10 did not list.** `RFC-0007/README.md:45-48`: index 2,324 (actual
2,324); package union 10,631 (2,324+5,165+3,142 = 10,631); reading paths 7,489
and 5,466 (both exact). RC-10's table named only the first two; the repair also
corrected 7,493 → 7,489 and 5,469 → 5,466. Credit where due.

### 3.2 FINDING RC11-C [Observed] — nine stale derived values remain inside act 1's digest set, and the repair made the file self-contradictory

`RFC-0009/README.md` carries a second word-accounting section that the repair
did not touch. Every figure in it is stale, by the same `provides_to` removal
that caused the original twenty-one.

| Line | Claims | Actual | Method |
|---|---|---|---|
| `:204` | module 1 = 6,999 | **6,996** | `wc -w`, confirmed by Python `split()` |
| `:205` | module 2 = 5,540 | **5,538** | same |
| `:206` | module 3 = 3,027 | **3,023** | same |
| `:207` | modules total = 15,566 | **15,557** | computed sum of the three |
| `:208` | package index (this file) = 2,029 | **2,025** | `wc -w` |
| `:214` | "Where the −3,703 words went" | **−3,712** | 19,269 − 15,557 |
| `:231` | module 1 alone (6,999) | **6,996** | as above |
| `:231` | module 2 alone (5,540) | **5,538** | as above |
| `:232` | module 3 alone (3,027) | **3,023** | as above |

**Nine stale derived values, all inside act 1's digest set.** (The adjacent
"Net −19.2%" survives: 3,712/19,269 = 19.26%, which still rounds to 19.2%. The
"19,269", "14,305", "7,184", "4,500" and "1,580" figures describe the frozen
rev9 monolith and are not recomputable at this commit — **[Unknown]**, and not
counted above.)

**The file now contradicts itself.** I checked the pre-repair state at
`864718c`: every one of these lines said `6,999 / 5,540 / 3,027 / 15,566 /
2,029`, and so did `:49-51` and `:224`. The file was **uniformly stale and
internally consistent**. The repair corrected `:49-51` (the CG-21-covered rows)
and `:224` (a prose figure twenty lines above `:231`) and left the rest. The
result is a governed artifact that states module 1 is **6,996 words at `:49`
and `:224`, and 6,999 words at `:204` and `:231`** — with `verify_final_prespec.py`
printing `6996` for that same file in its own output.

This matters for the reason RC-10 gave and the repair itself endorsed:
correcting it changes `RFC-0009/README.md`'s digest and therefore act 1's
argument. It cannot be dispositioned as an accepted exception. It is a re-offer.

**Enumerated remainder, so this is not a bare "all" claim.** I swept all 32
modules twice: once for comma-formatted figures `\b\d{1,2},\d{3}\b` in
900–26,000, once for bare `\d{4,6}` in the same range. The second sweep
returned 24 hits, all of them the year `2026`. **`RFC-0009/README.md` is the
only module carrying a stale derived word count; the nine rows above are the
complete set.** [Observed]

### 3.3 FINDING RC11-D [Observed] — CG-21 cannot see the class it was written to close

CG-21's row matcher (`check_governance.py:2236`) is:

```
r"\|.*?\|\s*`([\w.\-]+\.md)`\s*\|.*?\|\s*([\d,]+)\s*\|"
```

It requires a **backticked module filename** in the row. The RFC-0009
word-accounting rows are `| module 1 | 6,999 |` — no filename — so CG-21 never
examines them. Nor does CG-20 (load-map figures, a different artifact). Nothing
covers the prose figures at `:214`, `:231`, `:232`.

**Mutation-tested, in the clone:**

| Mutation | CG-21 result |
|---|---|
| `RFC-0002/README.md:43` row falsified 1,955 → 9,999 | **CAUGHT** — `FAIL … 19 rows examined, 1 finding` |
| `RFC-0009/README.md:204` falsified 6,999 → **111,111** | **MISSED** — `OK … 19 rows examined, 0 findings`; CG-20 also `OK` |

So CG-21 is a real check — it can fail, and it does close the rows it covers.
It is also **currently reporting `OK` over nine values that are wrong**, at
`0 FAIL` across the whole battery. RC-10's diagnosis of the original defect
applies verbatim to its own repair: *"caught in one artifact class, uncaught in
another."*

The docstring the repair wrote for CG-21 says: *"A prior round fixed this same
class by hand. Hand-fixing a recurring class is how it recurs."* The repair
then hand-fixed `:224` and left `:204`.

### 3.4 Verdict on finding 2

**Partly closed.** Twenty-one values corrected (plus two RC-10 missed), with a
mechanical check that is demonstrably able to fail. Nine values of the same
class remain inside the same digest set, in a file the repair edited, now
self-contradicting.

---

## 4. RC-10 finding 3 — the four misdescribed seams

I re-derived every one of the eleven disposition rows from RFC-0010's clause
text. All string sweeps below used Python `re`, never `grep`.

**[Observed] All three of RC-10's zero-occurrence claims reproduce, and the
report's own zero-claim is true:**

| Token | Occurrences in `RFC-0010-mission-control-autonomy.md` |
|---|---|
| `owner-signed` | **0** |
| `sibling work` | **0** |
| `consistency` | **0** |
| `consistent` | **0** |
| `atomic` | 1 — `:554`, inside the amendment log, exactly as RC-10 reported |

### 4.1 The four corrected rows

| Row | RC-10's finding | My re-derivation of the current row | Closed? |
|---|---|---|---|
| **F1** (RC10-I) | claimed an "owner-signed dispatch" carve-out occurring 0 times | The row now enumerates: read consented sources, compile packets, run agents within reserved budget, author drafts into `.syzygy/**` and `openspec/**` rendered unadopted; no effect outside those namespaces; push, PR, merge, deploy, publication, external mutation and RFC5-22 classes excluded "whether or not a profile standing-approved them". **Every limb matches `RFC-0010:205-219` word for word in substance.** No carve-out is asserted | **Yes** |
| **F4** (RC10-J) | claimed RFC10-19 "defines the relationship between completed and failed sibling work" — 0 occurrences | Restated as "**Closed for four of the five**", with the unclosed limb named explicitly: "It does not state the relationship between a failed run's output and its completed siblings' output — the closure report previously claimed it did". I verified all five affirmative limbs against `:406-420` | **Yes** |
| **F6** (RC10-K) | claimed RFC10-20 "states the consistency claim" — 0 occurrences | Restated as "**Closed for two of the three**", says "It **makes no consistency claim** — the word does not occur in the contract — and the closure report previously said it did", and volunteers the child-mission gap RC-10 found separately (RC10-E) | **Yes**, with one caveat below |
| **F7** (RC10-L) | labelled the budget rule "the lesser binds" as the consent rule | Now states the conjunctive rule — "the egress consent of **every project whose content it embeds** — never the project the composing step names for itself" — fails closed on absence or unverifiable provenance, and explicitly relegates "the lesser binds" to the budget sentence. Matches `:435-448` | **Yes** |

**[Observed] The two "partly closed" rows are honestly scoped**, and the
summary line was restated rather than the rows softened: *"Nine of eleven
addressed by clause text — seven fully, and F4 and F6 partly, each with its
unclosed part named in its own row… The earlier form of this line said 'nine of
eleven closed'; RC-10 showed that overstated two rows, and the count is
restated rather than the rows softened."* That is the correct move and it is
stated against the round's own interest.

I also re-derived the seven rows RC-10 had scored accurate (F2, F3, F5, F8, F9,
F10, F11) and confirm F2, F5, F8, F9 against `:368-383`, `:194-203`, `:450-465`
and `:159-167` respectively. F3 I dispute on substance, not on description —
see §2.4.

### 4.2 FINDING RC11-E [Observed] — RC10-F was reframed into a different defect and thereby dropped

RC-10's **RC10-F** was: RFC10-20's default stop is synchronous, and if limb
(b) cannot be achieved — a run that will not die — the clause specifies **no
timeout, no failure disposition, and no Attention Item**. RC-10: *"The default
(undeclared latency) is the deadlocking one."*

The F6 row now says RFC10-20 "**bounds latency** (undeclared means
synchronous)". A synchronous act with no timeout and no failure path is not a
bounded latency; it is an unbounded one with a different name. The report's
"What this closure does not claim" section does mention the same default, but
as: *"RFC10-20's 'undeclared means synchronous' default is an obligation no
artifact in this repository can yet check."* **That is a statement about
checkability, not about the missing failure path** — a true sentence occupying
the place where RC10-F's finding should be.

I swept `MISSION-SAFETY-CLOSURE-REPORT.md` and
`FINAL-OWNER-ACCEPTANCE-RECORD.md` for any statement of the failure-path gap
and found none. `FINAL-OWNER-ACCEPTANCE-RECORD.md` imperfect-table row 9 names
"stop does not propagate to child missions" and "RFC10-19 does not state the
failed-run / completed-sibling relationship" — RC10-E and RC10-J's residue —
and not RC10-F.

**[Observed] Minor, in the opposite direction, recorded for symmetry.** F1's
row says "no effect outside those two namespaces **at all**". RFC10-7 also
permits "Egress to a model provider … under an RFC5-14 consent record naming
the provider and content classes", which is an effect outside both namespaces.
The row therefore describes a *stricter* cap than the clause carries. It errs
safe and I raise no finding on it, but "at all" is not exactly what `:213-217`
says.

### 4.3 Verdict on finding 3

**Closed.** This is the cleanly repaired finding of the three. All four rows
now describe the clauses as adopted; the two partial closures are named as
partial; the report corrects itself in the open rather than silently. The one
gap is that a fifth RC-10 finding about the same clause (RC10-F) was displaced
rather than disclosed.

---

## 5. New false or stale derived claims the repairs introduced

This was the specific pattern the commission asked me to hunt. I found three
beyond RC11-C.

### 5.1 FINDING RC11-F [Observed] — the offering states the wrong check and fixture counts, and contradicts `PROJECT-STATUS.md`

Run in a clean clone at `7f0efa4`, reading output not exit codes:

```
24 OK, 9 WARN, 0 FAIL (33 checks) — counts derived, not asserted
46 fixtures, 0 failing — a check that cannot fail is not a check
```

| Artifact | States | Actual | Correct? |
|---|---|---|---|
| `FINAL-OWNER-ACCEPTANCE-RECORD.md:119-120` | "**32 checks**, denominators printed" / "**19 fixtures**" | 33 / 46 | **No** |
| `FINAL-PRE-SPECIFICATION-READINESS-REPORT.md:117-118` | "**32 checks**" / "**19 fixtures**" | 33 / 46 | **No** |
| `PROJECT-STATUS.md` | "24 OK, 9 WARN, 0 FAIL over **33 checks**"; "`--selftest` **46 fixtures**" | 33 / 46 | **Yes** |
| `PUBLIC-CLONE-VERIFICATION-REPORT.md` | "24 OK, 9 WARN, **0 FAIL** over 33 checks"; "46 fixtures" | 33 / 46 | **Yes** |

Both wrong figures sit in **§5 "Evidence you can reproduce"** and the readiness
report's **"Evidence"** block — the two places an owner is told to go and run
the thing. `git log -S` places their origin at `f96ff6b` (which said 32/17,
correct at the time); `d8eec68`, `c4f54e6` and `7f0efa4` each added checks or
fixtures and neither document was recomputed. This is a derived value quoted
outside its owning artifact going stale silently — the failure class the round
built CG-21 to prevent, recurring in the round's own offering document, in the
same range of commits.

The offering now disagrees with `PROJECT-STATUS.md` about its own evidence.

### 5.2 FINDING RC11-G [Observed] — "each check shown able to fail" is still asserted and still false

Both documents carry the phrase verbatim beside the (wrong) fixture count. I
enumerated which checks the selftest actually exercises:

```
CG-13 CG-14 CG-15 CG-16 CG-17 CG-18 CG-19 CG-20 CG-21
```

**Nine check families.** The battery reports 33 results; the fixtures reach 11
of them. **CG-1 through CG-12 have no fixture at all — including all four CG-7
sub-checks**, the ones every act-verification instruction in the repository
depends on.

RC-10 raised this as §7.2 item **vi** and its minimum-to-CONFIRM item 5 asked
that the claim be corrected "to its true denominator". It was not corrected.
The repair instead added 29 new fixtures (all for CG-19, CG-20, CG-21, and the
CG-17/CG-18 hardening) — real work that makes the sentence *less* true as a
proportion of what it claims, because the new fixtures cluster in the range
that already had coverage.

### 5.3 FINDING RC11-H [Observed] — the RFC2-24 denominator repair replaced one unreproducible figure with two

RC-10 §3.4 reported that "all 13 `RFC2-24 #N` citations" does not reproduce; it
counted 15 (16 counting a second ordinal sharing one line). The repair's
response, at `FINAL-OWNER-ACCEPTANCE-RECORD.md:77-80`:

> the 13 ordinal citations **inside the 32 contract modules** now agree with the
> table, as do the **20 across all candidate material outside `history/` and
> `reviews/`**. Both denominators are stated because a bare "all 13" invites the
> reader to assume the sweep covered the corpus, and it covered the act.

I swept both populations myself, by two methods (a loose form allowing ≤40
characters between `RFC2-24` and `#N`, and a tight adjacency form):

| Population claimed | Claimed | Loose sweep | Tight sweep |
|---|---|---|---|
| Inside the 32 contract modules | **13** | **15** | **16** |
| All candidate material outside `history/`, `reviews/` | **20** | **28** | **28** |

Neither reproduces. I also tested the narrowest defensible definition — an
ordinal paired with a backticked reason name on the same line — which yields
**9**. **No definition I could construct yields 13 or 20.**

The repair took a figure a reviewer had flagged as unreproducible, kept it,
attached a *more specific* scope to it that is demonstrably false, added a
second figure that is also false, and appended a sentence explaining why
stating both denominators is the rigorous thing to do.

**[Observed] The substance is fine, and I confirm it independently.** I
extracted RFC2-24's twelve-reason table
(`RFC-0002/rendering-vocabularies.md:112-123`) and checked all 15 in-corpus
ordinal citations against it: **15 of 15 correct**, including
`RFC-0009/semantic-geography.md:270` (`missing-declaration` = #1), the
correction that prompted the sweep. Only the denominators are wrong.

---

## 6. What the repairs closed cleanly

Stated plainly, because several are substantial.

| RC-10 finding | Status | My evidence |
|---|---|---|
| **RC10-M** — `check_governance.py` FAILS (CG-1b, 2 findings) at the offered commit | **Closed** | Clone at `7f0efa4`: `OK CG-1b — 989 references examined, 0 findings`. Battery `0 FAIL` |
| **RC10-Q** — CG-14 examined **0** items | **Closed** | `OK CG-14 — 11 paths examined, 0 findings`; four CG-14 fixtures, including "git-excluded ceremony location detected" |
| **RC10-N** — CG-17 misses routed-but-undeclared; fiction inflates its denominator | **Closed** | Fixture "CG-17 routed-but-undeclared clause detected" passes; source at `:1393-1397` now checks `routed − declared` |
| **RC10-O** — CG-18 silently skips a de-anchored fixture and reports OK | **Closed** | Fixture "CG-18 unparseable fixture is not silently skipped" passes; CG-18 now examines 18 measurements across nine fixtures |
| **RC10-P** — CG-19 checks for a URL-shaped string, and its name overclaims | **Closed, and honestly** | Rebuilt over a parsed lock: 57 predicate evaluations, 28 fixtures, four negative. **Renamed** to "complete and well-formed; drift consistent". Fixture `F6e` keeps the residual limit *executable and visible*: "well-formed pin to a nonexistent repo passes — the residual limit, kept executable". That is the right way to record a limit |
| **RC10-R** — "199 routed clauses" mixes two populations; 6 ids no contract declares | **Resolved** | CG-17 now expands positively-declared sub-clause *ranges* (`RFC7-2(a)-(c)`) into `declared`, and explicitly refuses to read RFC-0008's "**No lettered sub-clauses**" sentence as a declaration. `declared` and `routed` now coincide at 199, and the figure reproduces |
| **Clone-vs-working-tree divergence** | **Closed** | My independent clone at `7f0efa4` reproduces `24 OK, 9 WARN, 0 FAIL (33)` and `46 fixtures` **check for check**, with `_bootstrap/` absent |

**[Observed] Other figures I recomputed and confirm:**

- `verify_final_prespec.py` — **PASS**, 328 numbered clauses, **100,862 words**.
  The corpus total reproduces by a second method (`find … | xargs wc -w` →
  `100862`). `FINAL-OWNER-ACCEPTANCE-RECORD.md` row 3's updated figure is
  **correct**, and it correctly tells the reader to recompute it.
- `build_contract_index.py --check` and `build_dependency_index.py --check` —
  **no drift**, both.
- CG-13: 146 edges, 0 findings. CG-17: 199 clauses, 0 findings. CG-20: 32
  figures, 0 findings.

**[Observed] The narrative artifacts are candid.** The clone report records
that a prior version of itself was patched in place and states the lesson ("a
clone report is only ever valid for the commit it was run at"). The human
clarity review upgrades "nine reviews" to ten and "six said REVISE" to "seven
— including the one commissioned specifically to confirm". The fixture report
records that fixture 9 **fails** its budget (24,025 w ≈ 32,433 tokens, above
the 20,000-token trigger) and names a lawful shard rather than trimming the
selection to flatter the number, and drops the `Compiler:` line because there
is no compiler. The readiness report's answer is still **Not ready**. None of
this is advocacy, and the pattern RC-10 identified — "a maturing verification
battery, not advocacy" — holds for this round too.

---

## 7. Checks I found unable to fail

1. **CG-21, over any README word figure not in a module row.** Demonstrated
   in §3.3: a value of **111,111** in `RFC-0009/README.md:204` passes. This is
   not hypothetical — nine real stale values sit under it right now at
   `0 FAIL`.
2. **CG-1 through CG-12 have no selftest fixture whatsoever** — 22 of the 33
   reported results, including CG-7a–7d. I did not attempt to break them
   individually; I did demonstrate CG-7a fails on a one-word mutation (§1), so
   at least CG-7a is *not* inert. For the other 21 I make no claim: **[Unknown]**.
3. **CG-17's routed-but-undeclared exemption is loose.** `:1394-1395` exempts a
   routed sub-clause when its parent is declared **and** the token appears
   anywhere in the concatenated module bodies. A fabricated row for a sub-clause
   letter mentioned anywhere in prose would still pass. Narrow, and much better
   than the state RC-10 found. Not a finding.

Every check I *did* rely on, I made fail first: CG-7a (§1), CG-21 (§3.3), and
the CG-17/CG-18/CG-19/CG-20 fixtures I read and re-ran.

---

## 8. RC-10 items still open, with their current disposition

| RC-10 §7.2 | Item | Now |
|---|---|---|
| i | 21 stale derived counts in the digest set | **Nine remain** — RC11-C |
| ii | `check_governance.py` FAILS | Fixed |
| iii | four misdescribed seams | Fixed |
| iv | "199" counts 6 undefined ids | Resolved in CG-17; not disclosed, but no longer wrong |
| v | CG-17/18/19 pass over their own defect | Fixed, all three |
| vi | "each check shown able to fail" true of a fraction | **Not fixed** — RC11-G |
| vii | CG-14 examined 0 items | Fixed |
| viii | RFC10-18 / `blocked`; F13 not re-examined | Partly — RC11-A, RC11-B |
| ix | stop does not reach child missions; synchronous stop has no failure path | Child missions disclosed (row 9); **failure path not** — RC11-E |
| x | RC-7 asked the clauses be inserted *after* act 1; deviation unrecorded | **Still unrecorded.** I swept both round-2026-08b offering documents for it and found only an unrelated act-ordering paragraph |

RC-10's minimum-to-CONFIRM item 6 asked that the `blocked` contradiction be
recorded as an owner item. No new `P-` entry was created (the only
`decisions/` change in the range is `PROCESS-LESSONS.md`). It was addressed by
clause text instead, which I judge the better choice — but §2.2 and §2.3 mean
it is not fully addressed, and it is now recorded nowhere as open.

**[Observed] RC-10's other clause-level findings are still undisclosed**:
RC10-C (RFC10-17's `spent` has no independent measurer), RC10-D (a *failed*
compensation is recorded and nothing more), RC10-G (RFC10-21's predicate keys
on mission scope, the harm on content provenance), RC10-H (RFC10-22's bound can
suppress notice of itself). None appears in the imperfect table. RC10-G in
particular sits under an F7 row still marked "**Closed**".

---

## 9. Findings I could not resolve

- **[Unknown]** Whether the effects-applied determination in RFC10-18 is
  *intended* to be independently established. The clause is silent and I have
  no authoring context. My finding (RC11-B) is that the text does not require
  it; whether that is an oversight or a deliberate deferral is an owner/author
  question.
- **[Unknown]** Whether "13" and "20" in the RFC2-24 sentence were computed
  against some definition I did not construct. I tried three and enumerated the
  hits for all of them; none matched.
- **[Unknown]** Whether CG-1…CG-6, CG-8…CG-12 are able to fail. Untested.
- **[Unknown]** The substantive correctness of the 31 modules other than
  RFC-0010, and every historical figure (19,269; 14,305; the nine compaction
  passes). Outside my commission and not reconstructible at this commit.
- **[Unknown]** Whether the uncommitted working-tree edits now in flight
  (`check_governance.py`, `AGENTS.md`, the substrate lock) preserve any result
  in this report. **Everything here is a claim about `7f0efa4` and nothing
  else.**

---

## 10. Why REVISE

I applied RC-10's own distinguishing test: **can the owner accept this, at this
digest, knowing everything material?**

The repairs are real and most of them are good. Finding 3 is fully closed.
Six named check defects are fixed and mutation-proven. The manifest is exact.
The offering's narrative artifacts are more honest after the repair than
before, not less.

Two things still say no, and neither can be cured by disclosure:

1. **RC11-C — nine stale derived values inside act 1's digest set.** This is
   RC-10's finding 2, not closed, in the same class, in a file the repair
   edited, now internally contradictory in a way the pre-repair file was not.
   Correcting it changes `RFC-0009/README.md`'s digest and therefore act 1's
   argument, so it cannot be accepted as a known exception — it is a re-offer.
   The check written to prevent recurrence is structurally unable to see it.

2. **RC11-A — a false citation introduced into a contract inside the digest
   set.** RFC10-18 now tells its reader that RFC10-5 requires a human
   resolution act for a block RFC10-5's own scope excludes. This was
   introduced *while repairing* the clause, from a review paragraph that stated
   the scope limit explicitly. Together with RC11-B, the escape RC-10 found is
   relocated rather than closed, and the closure report calls it "Closed".

Three further items are disclosable rather than disqualifying, but should be
fixed before the offer because all three are in the owner-facing evidence
sections: RC11-F (32/19 against a real 33/46, contradicting `PROJECT-STATUS.md`),
RC11-G ("each check shown able to fail", still false, RC-10 asked once already),
and RC11-H (two unreproducible denominators where there was one).

**What REVISE does not mean.** The contracts are not unsound and the round is
not drifting. The 32 modules verify byte-exact; 328 clauses and 100,862 words
recompute; every check I attacked either caught its defect or disclosed its
limit; and the round keeps finding its own errors and writing them down. The
recurring shape is narrow and specific: **corrections are applied to the
instances a reviewer enumerated rather than to the class**, and the report
describing the correction acquires a new derived figure that nobody
recomputes. That is the third round in which that exact shape has produced the
blocking finding.

### Minimum to reach CONFIRM

1. Correct the nine figures in `RFC-0009/README.md` §"Word accounting" and the
   selective-loading paragraph; regenerate the manifest **by script**; re-quote
   act 1's argument. (RC11-C)
2. Broaden CG-21 — or add a check — to cover README word figures that name no
   module file, and prose word figures. Make it fail before trusting it.
   (RC11-D)
3. Either amend RFC10-5 to reach RFC10-18-sourced blocks, or remove the claim
   that RFC10-5 requires a human resolution act for one. (RC11-A) *Digest-set
   change.*
4. Assign the effects-applied determination, and give it the Unknown rule
   RFC10-17 already models ("Unknown is never read as zero"). Or record it as
   an open owner item and stop calling F3 "Closed". (RC11-B)
5. Recompute the check and fixture counts in both offering documents, and
   correct "each check shown able to fail" to its true denominator.
   (RC11-F, RC11-G)
6. Recompute or drop the "13" and "20" RFC2-24 denominators. (RC11-H)
7. Disclose RC10-F (synchronous stop has no failure path) as itself, and decide
   whether RC10-C/D/G/H belong in the imperfect table. (RC11-E)
8. Let the concurrent session settle and re-verify. Two consecutive confirming
   reviews have now had to work from a pinned commit because the tree was
   moving. The offering must be stationary when it is offered.

Items 1 and 3 change act 1's argument. Items 2 and 4–8 do not.

---

**Verdict word, stated once more exactly:**

VERDICT: REVISE
