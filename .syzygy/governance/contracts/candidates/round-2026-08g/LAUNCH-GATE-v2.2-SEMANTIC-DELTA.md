# Launch-gate instrument — v2.1 → v2.2 semantic delta

> **A delta, not an approval.** The instrument remains a **candidate**; its
> approval as process policy is **P-34**, ungranted.
>
> **Nothing here is confirmed.** v2.2 repairs two `REVISE` verdicts, made by
> the session that received them. A repair session cannot confirm its own
> repairs — a sentence this file has now written twice, about two successive
> versions, which is itself the most useful thing it says.
>
> The v2.1 delta is **not superseded and must not be edited**: RD-55 and
> RD-56 are bound to its bytes, and three of RD-55's findings are findings
> *against it*. Their corrections are recorded here, in §"Corrections to the
> v2.1 delta", and the reviewed bytes stay as they were.

## Why there is a v2.2

v2.1's two commissioned reviews both returned `REVISE`:

| Review | Subject | Verdict | Findings |
|---|---|---|---|
| RD-55 | policy semantics | `REVISE` | 1 blocking, 3 material, 6 minor |
| RD-56 | schema, validator, renderer | `REVISE` | 2 blocking, 5 material, 6 minor |

**They were dispatched separately, in fresh context, and neither saw the
other's output. They found the same blocking defect.** That convergence is
the most load-bearing fact in this file: a defect two independent readings
land on is not a matter of taste.

Both also confirmed what the v2.1 pass was commissioned to establish. RD-55
reproduced the v2.1 delta's byte-identity table exactly — *"9 of 9 rows
reproduce"* — and, over eight populations and a 25-record differential
battery against the v2.0 validator, found **no readiness question, verdict
word, trend column or conjunct dropped, renamed or weakened, and no record
that fails under v2.0 and passes under v2.1**. RD-56 reproduced all twelve
RD-47 attacks and found **seven cleanly closed**.

What failed was narrower and sharper: **the repairs were repeatedly narrower
than the claims made for them.**

## What did not change

**§1, §2, §3, §6, §7 and §8 are byte-identical to v2.1.** Reproduce it — the
method now includes the preamble, whose omission let the v2.1 delta assert a
byte-identity it could not check (RD-55 f3):

```text
v2.1   3afdffdab0d71d32a4e901f43db1c11ba096f699e240050e8cc6cbb95ada12c8
       launch-gate-pre-specifications.md at commit 939363f
v2.2   ac8751236ec7434c20606b404d41c885d29f67dd5f3dab8c9d0cbb90de670977
       the working-tree file — and the digest the formal packet seals
```

```python
import re, hashlib, subprocess
old = subprocess.run(["git", "show",
                      "939363f:launch-gate-pre-specifications.md"],
                     capture_output=True, text=True).stdout
new = open("launch-gate-pre-specifications.md").read()
def spans(t):
    p = re.split(r"(?m)^(## \d+\..*)$", t)
    d = {"0(preamble)": hashlib.sha256(p[0].encode()).hexdigest()}
    for i in range(1, len(p), 2):
        d[re.match(r"## (\d+)\.", p[i]).group(1)] = hashlib.sha256(
            (p[i] + p[i + 1]).encode()).hexdigest()
    return d
```

```text
§0(preamble) 08b200cd4581d4b9 -> 3cff94f230056b52    the version bump
§1           1f2d1d60a28ada2a   identical
§2           0d7340f2ee9a8b8c   identical
§3           fe0b051e136d2fee   identical
§4           84d5d3d456e7c05a -> 8af5dbc5b7d82af1
§5           0b63585544520df4 -> 1fd518196e437f6e
§6           9906fcac454062cd   identical
§7           9e17cb8de0458976   identical
§8           01209c0f052971f7   identical
§9           9301d992b12b889a -> 18029b54c3de4e61
```

**No question's text moved** (§3), **no protocol obligation changed** (§2),
**no parameter changed** (§8), and the trend-log rules are untouched (§6).
The §8 digest is the parameter-block digest the formal packet seals — so
every fixed input of an administration is what it was at v2.0.

---

## The blocking repair — eligibility has limbs, and now it has all of them

**Both reviewers, independently.** RD-55 f1 and RD-56 f1, quoting the clause
v2.1 itself added:

> a record is eligible to be cited as launch evidence only when it is
> `formal`, of kind `full`, declares fresh context, **and validates without
> error**

`_compute` implemented three of the four. The fourth lived at exactly one
consumer — the CLI's own printed line — and the two consumers that produce
*stored artifacts* did not have it. RD-56's run, on a record whose only
defect is a forged instrument digest:

```text
Trend row (§6):
| … | 0 | 0 | 0 | 0 | 0 | n/a | READY FOR Capability 1 — … |

1 validation error(s):
  LA-2: instrument digest mismatch — …
```

That row is what gets appended to the log §6 says *"F1 — which is answered
from this log and only from it."* The same record rendered
`GATE VERDICT: READY FOR Capability 1 …` as its last line, 207 lines below
the `THIS RECORD DOES NOT VALIDATE` stamp.

**What changed, and why in that order:**

1. `_compute` takes the errors raised before it and is **computed last**, so
   it can count the errors — including its own `LA-12` errors. Placement is
   the repair as much as the predicate is; computing eligibility early is
   what made the fourth limb unreachable.
2. A **fifth limb** is added and stated: with git unavailable, identity,
   binding, case-text, deferral and evidence existence do not run. RD-56 f7
   passed a record with a nonexistent commit, forged digests, six paraphrased
   E4 cases and 43 fabricated evidence paths — 40 errors with git, `record
   valid` and `READY FOR` without it. That was a *disclosed limit* that
   nothing acted on. An unverified record is now ineligible.
3. The CLI's private `and not errors` is **deleted**. Every consumer reads
   one answer. A limb implemented at a consumer is a limb the next consumer
   will not have.

**Direction: a strengthening.** No lawful record loses a pass: an eligible
record's gate result is still its formula outcome, and a record with zero
errors under a working git is unaffected.

## The second blocking repair — free text is data at every site, not at two

RD-56 f2 quotes v2.1's own claim and refutes it with a denominator:

> Free text is **data**: every line blockquoted, so no line can open a
> heading, table or fence at document level. **Structure is forbidden rather
> than a list of phrasings**

`_quoted` was applied at **2 of 21** free-text-bearing sites — the two fields
RD-47 happened to name. RD-56 re-ran RD-47's forgery through
`operationalization_notes` and got it back character for character: a forged
`## Computed figures` section and a forged `GATE VERDICT: READY FOR …` line,
both **above** the real ones, in a report of a record that validates clean
and needs no `--allow-invalid`.

The repair is the class property, honestly this time. Every Markdown block
construct must *start a line*; so reviewer text emitted inline has its
newlines removed (`_inline`), and multi-line blocks stay blockquoted
(`_quoted`). Eight sites are fixtured, one per structural shape, and each
fails with `_inline` reverted to the identity function.

**A lesson worth the space:** v2.1 fixed the two fields a reviewer named and
then described the fix as covering a class. Naming a class is not achieving
one, and the fixture bound to the named fields could not tell the
difference.

## Every other tool repair

Each has a fixture, and each fixture was verified to fail with its repair
reverted — twelve reversions run against copies of the scripts.

| Finding | Defect | Repair |
|---|---|---|
| RD-56 f3 | `--schema` was bound to nothing: `--schema weak.json` holding `{"type":"object"}` turned `LA-1` off, and a record with a top-level `final_verdict` and rows reading `"Not met, mostly"` printed a `READY FOR` **gate result** | A schema other than the committed one is an `LA-1` error — and therefore, via the fourth eligibility limb, ineligible. A schema declaring no root `properties` is refused: the closure audit is vacuous on it |
| RD-56 f4 | The fixture claiming to cover RD-47 f1 **passed against the unrepaired v2.0 validator**. It mutated the *record*, so §8 stayed readable and it hit the pre-existing mismatch branch; its expectation was the bare substring `LA-3`, which that branch also emits | The fixture mutates the **instrument**, in a scratch git repository, into the exact unreadable forms RD-47 built, and its expectation names the *unreadable* wording — because the mismatch message mentions the parameter too, which is how the old one passed for the wrong reason |
| RD-56 f5 | Deferral warrants were "any decisions-home file not in a three-name list", which accepted **16 of the home's 20 files** — a trend log (F1's own evidence, so citing it to defer F2 is circular), a repair history, and a decision packet whose own bytes read *"remains PENDING"*, the class §4 names explicitly | Classified by **shape**: logs and indexes by name, packets and drafts by name pattern, and — the part that survives the next file being added — anything whose own text declares its status pending, open, candidate, proposal or "binds nothing". Refusal messages name the actual reason; two of four used to report the wrong one |
| RD-56 f6 | The prior-record path was the only path whose **content is read and arithmetic performed on**, and the only one not resolved against the repository. A traversal to a hand-written file outside the repo zeroed the §6 new-findings column with four genuinely new `Not met` rows and no error | The path resolves inside the repository or it is an `LA-15` error |
| RD-56 f8 | §4's `READY-WITH-DEFERRALS` predicate ends *"AND the citation resolves"*; the branch was selected from the deferral **count** alone, so a record computed the pass word beside its own citation error | The branch requires an F2 citation that actually resolved. `LA-12` says so when it does not |
| RD-56 f10 | `--allow-invalid` — the documented inspection path — ended in a traceback for the commonest invalid record, and a second traceback class was *introduced* by the v2.1 duplicate-key repair | An unrenderable record gets a short honest report naming why. It carries no verdict, no figures and no trend row |
| RD-56 f7 | The git-unavailable note reached stdout and never the stored artifact, so `--check` reported the byte difference between a git-capable and a git-less machine as a hand edit | The note is stamped into the report body as `**UNVERIFIED:**` |
| RD-56 f12 | `trend_row` sanitized `|` but not `\n`, and every schema `pattern` is anchored with `$`, which matches before a trailing newline — so a `launch_target` differing from §8 by one newline split the §6 row across two lines | Every cell is sanitized, not only the verdict |
| RD-56 f13 | `"none​"` defeated the placeholder lexicon: `str.split()` does not split on a zero-width space | Invisible characters are stripped before tokenizing. An invisible character is not a word the lexicon must learn |
| RD-56 f9 | *"This is the one place the validator reads the instrument's own prose"* — false when RD-47 raised it, and v2.1's replacement figure of **five** was falsified by v2.1's own `LA-3b` repair, which added the sixth | The docstring names all six, beside the population it counts, and the figure is stated nowhere else |

## Instrument repairs

| Finding | v2.1 said | v2.2 says |
|---|---|---|
| RD-55 f4 | §4 annotated the `(LG-6/LG-7)` citation as *"corrected at v2.1"* and left the literal standing — while the v2.1 delta, its D-4 table and §9 all reported it corrected | The citation is `(LA-12)`. The note says what actually happened at v2.1 |
| RD-55 f2, RD-56 f8 | §5 took back the check enumeration *"a check the tool runs that this list does not name is a finding against the tool"* — in the same pass that added `LA-3b`, which the list did not name. `LA-3b` occurred **0 times** in the instrument | §5 names `LA-3b`, the schema's own identity, and what a deferral warrant is not |
| RD-55 f7 | *"A delta, non-formal, **stale** or invalid administration…"* — `stale` defined no limb and was computed nowhere | The five limbs are the list. `stale` is gone |
| RD-55 f8 | The fourth outcome existed in prose as *"none"* and three tool surfaces spelled it three ways | The word is `NONE`, defined in §4, used by every surface |
| RD-55 f6 | *"A record may not contain any of them"* — unenforced, and unenforceable without forbidding a reviewer from quoting a verdict word | Narrowed to what is enforced: **a record carries no verdict field**, which the schema's closure does enforce |

## Corrections to the v2.1 delta *(RD-55 f3, f5, f10)*

The v2.1 delta is frozen — RD-55 is bound to it. Its three defects are
corrected here rather than there.

1. **f3 — the preamble is not byte-identical.** D-8 of the v2.1 delta claims
   *"§2 and the preamble are byte-identical at v2.1"*. The preamble changed
   in exactly one line, `effective_version: v2.0` → `v2.1`, and the delta's
   published script **structurally could not see it**: the split discards
   `p[0]`, so the table's denominator was §1–§9 while the prose made a claim
   about the file. The instrument's own §9 entry claimed only §1/§2/§3/§6/§8
   and was correct. The script above digests the preamble.
   **The correct statement is: §2 is byte-identical; the preamble changed by
   its version bump and nothing else.**
2. **f5 — D-8's "equivalent-or-stronger" holds for row verdicts, not gate
   verdicts.** The schema `verdict` enum is the *row* vocabulary; the gate
   verdict is not a schema field at all. For gate verdicts the successor to
   the deleted §2 sentence is §4's prose, so prose replaced prose. The
   not-restoring decision stands; **its stated reason was too broad**, and
   RD-55 is right that this half is unestablished rather than established.
3. **f10 — "stated nowhere else" was unscoped.** The v2.1 delta's own
   Fixtures block states four counts a hundred lines later. The correct
   scope: the fixture count is stated in no artifact that must stay current.

## Disclosed limits — what v2.2 still does not do

1. **Presence tests on free-text fields are content-blind by design.** A
   reviewer who writes a plausible false evidence quote defeats this tool.
   Neutralizing structure does not make text true.
2. **The JSON Schema interpreter is a documented subset**, whose safety
   property is that it rejects any keyword it does not implement — and, from
   v2.2, any schema that constrains nothing.
3. **The validator reads the instrument's own prose in six places.** Two
   failed open at v2.0 and are repaired; all six remain prose reads.
4. **No administration has been performed under v2.0, v2.1 or v2.2.** The
   verdict path is fixture-proven, not field-proven.
5. **RD-47's E4 asymmetry is unrepaired.** A scoped row must be disclosed;
   an E4 case laundered from "disagree" to `"silent"` plus
   `needed_by_launch_target: false` requires no disclosure and no cross-read
   of the routing authority. RD-56 reproduced it and it passes clean.
6. **`question_digest`'s sha256 form binds nothing** (RD-56 f11). No check
   computes or compares it, so a record may set 43 arbitrary hex strings.
   The `instrument-bound` literal *is* covered, by `LA-2`. Removing the hex
   alternative is a **schema** change, which would move the schema digest the
   formal packet seals and has been deliberately **not** made in a repair
   pass — the schema has been byte-stable across three instrument versions,
   and that stability is worth more than closing a form nobody uses. It is
   recorded as open, not as repaired.
7. **`counterexample: " "` satisfies the emptiness check** (RD-56 f13,
   second half). A single space is a concrete counterexample to `minLength`
   and to nothing else.
8. **`blocking_conditions_met` is reviewer-authored** and checked for
   consistency, never for truth.
9. **What constitutes an owner warrant is not defined by any adopted
   convention.** `LA-11` now refuses logs, indexes, packets and
   self-declared-pending documents, which is a defensible *shape* rule, and
   it is not the same thing as a rule the owner has established for what
   records a decision. Until one exists, `SDR-n` remains the only citation
   form with an owner-side meaning. **This is an open question, not a
   repair**, and a repair session may not invent the convention.

## Fixtures

```text
validate_launch_administration --selftest   101 fixtures   (88 at v2.1)
render_launch_administration  --selftest     31 fixtures   (16 at v2.1)
```

The count is printed by `--selftest` and is stated in no artifact that must
stay current. Each repair above has at least one fixture; each was verified
to fail with its repair reverted, by mutating a copy of the script — the
discipline RD-56 f4 showed had been claimed rather than performed.

## What must happen next

**Two more reviews, and nothing else first** — one on policy semantics, one
on the machinery, both in fresh context against the repaired bytes. Until
they return, v2.2 is an unreviewed amendment made by the session that
received the verdicts it responds to, and **P-34 must not be offered on it.**

The honest summary of this instrument's maturity, which the formal packet now
also carries: **four reviews, four `REVISE` verdicts, two repair passes, and
the repaired bytes have never been reviewed at any version.** The trend is
real — v2.0's reviews found a fail-open in the wave binding; v2.1's found
claims that outran their repairs — but a trend toward correctness is not
correctness, and F6 is where that belongs, not here.
