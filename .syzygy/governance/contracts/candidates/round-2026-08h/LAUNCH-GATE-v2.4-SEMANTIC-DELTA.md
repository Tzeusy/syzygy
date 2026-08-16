# Launch-gate instrument — v2.3 → v2.4 semantic delta

> **A delta, not an approval.** The instrument remains a **candidate**; its
> approval as process policy is **P-34**, ungranted.
>
> **Nothing here is confirmed.** v2.4 repairs two `REVISE` verdicts, made by
> the session that received them. A repair session cannot confirm its own
> repairs — the fourth time this file family has written that sentence, about
> four successive versions. The changed bytes go back under fresh review in
> this same round.
>
> **This is the round the owner ruled arm (c).** After the v2.3 reviews
> returned the fourth consecutive `REVISE` pair, the P-34 packet's arm (c)
> put the convergence question to the owner rather than absorbing it as
> another automatic round. The owner authorized a **structural** repair —
> one aimed at the root cause the prior three rounds shared, not another
> instance patch. That framing is what this delta is accountable to.
>
> The v2.3 delta is **not superseded and must not be edited**: RD-61/RD-62's
> repairs are accounted there, and RD-65/RD-66 verified that account against
> the bytes (nothing weakened v2.2→v2.3; six of eleven RD-61 findings and
> eight of thirteen RD-62 findings closed outright). This file accounts only
> for what v2.4 changes.

## Why there is a v2.4

v2.3's two commissioned reviews — the third administration of the RD-55/RD-56
commission — both returned `REVISE`:

| Review | Subject | Verdict | Findings |
|---|---|---|---|
| RD-65 | policy semantics | `REVISE` | 0 blocking, 3 material, 2 minor |
| RD-66 | schema, validator, renderer | `REVISE` | 1 blocking, 3 material, 2 minor |

Dispatched concurrently, in fresh context, against frozen commit `494acab`,
neither seeing the other. The pattern broke from "narrower each round":
**RD-66's blocking finding is the RD-47 f2 / RD-56 f2 / RD-62 f1
document-forgery class reproduced at a new address** — `prior_record.path`,
a free-text render site the v2.3 forgery suite did not enumerate — in a
record that validated with zero errors and exited 0. RD-65's third finding is
the same shape: RD-61 f1's eligible-`READY` outcome surviving at the schema's
new `HEAD` binding. RD-66 named the mechanism directly: each pass repairs the
*instances* its reviewers name and restates the result as a *class property*,
so the next review finds the class at a new address.

Both reviews also confirmed the v2.3 repairs they were commissioned to check:
RD-65's 31-case differential found **nothing weakened** v2.2→v2.3; RD-66
reverted sixteen repairs and watched fourteen fixtures fail, verifying the
other two as non-defects. The new findings are in the v2.3 additions and in
the class the prior three rounds kept re-opening.

## The blocking repair — the forgery sweep is mechanical, not enumerated

RD-66 f1's `prior_record.path` is neutralized (`_inline`, so newlines cannot
start a Markdown block). But the durable repair is not that one call — it is
the fixture. The renderer's forgery suite now **walks every string leaf of a
populated record** (both `\n`- and `\r`-spelled forgeries) and asserts each
opens no document-level structure, rather than iterating a hand-maintained
`SITES` tuple that was short by exactly the field nobody named. A reversion of
the `_inline` call now fails the sweep at `prior_record.path` with the exact
RD-47 f2 signature (two `## Computed figures` sections, a forged
`GATE VERDICT: READY FOR …`). The next unnamed string field fails **this
suite**, not the next review — which is the class defect closed, not another
instance.

## Every other repair

| Finding | Repair |
|---|---|
| RD-66 f2 — the `Cf`/`Cc` invisible strip excludes `Mn`; `U+034F` makes a wholly-unfalsified record an eligible `READY` | the strip sweeps `Cf`, `Cc`, **`Mn`** (zero-width combining marks) and the four zero-width Hangul fillers (category `Lo`, listed as the named tail the category sweep cannot reach); the docstring's false completeness claim is corrected to a disclosed approximation. Probe of all ten invisibles RD-66 named now returns placeholder, with no false positive on real or Thai text |
| RD-66 f3 — the instrument is located by a record-chosen path | `INSTRUMENT_NAME` is a module constant beside `SCHEMA_NAME`; `LA-2` errors if the record's `instrument.path` is anything else, so a decoy or a stale in-tree copy cannot bind its own §8. Fixture: a decoy path is refused |
| RD-65 f3 — the schema read at `HEAD` while everything else read at the record's commit | the record is parsed first; the schema is read via `git show <record-commit>:`, exactly as the instrument is, with a working-tree drift against **that** an error of its own. A widening committed at `HEAD` no longer governs a record anchored at an ancestor. Two-commit fixture: schema widened at `HEAD`, record at the ancestor, forbidden word rejected |
| RD-66 f4 — the prior record read from the working tree, not the commit | the record-declared prior is read via `git show <record-commit>:`, so an untracked, never-committed file cannot forge the new-findings column; an uncommitted prior is `Unknown`. `--prior` keeps its filesystem read as the explicit inspection override. Two-commit fixtures: a committed prior computes an integer; an uncommitted one is refused and reads `Unknown` |
| RD-65 f2 — "never of the environment" false, and false permissively | the `SDR-n` deferral branch resolves **only** when git can verify the warrant; with git unavailable it does not resolve, so the row/formula outcome is `NOT READY`, never a falsely-permissive `READY-WITH-DEFERRALS`. §4's claim is corrected to name the one fail-closed environment dependence. Fixtures: the git-verified path resolves (git=True, real `SDR-9`); the git-unavailable path does not (reversion detector) |
| RD-66 f5 — the record filename reaches the unrenderable report raw | `_inline(Path(record_path).name)`; fixture drives a newline-spelled filename through `_unrenderable` |
| RD-66 f6 — `--allow-invalid` exits 0 on an invalid record | the write path returns non-zero when the record did not validate — the sibling of RD-62 f6's validator and git-unavailable fixes. Fixture asserts a non-zero exit through `main()` |
| RD-65 f4 — §4 names `LA-11` where `LA-12` also fires | the prose says "a validation error" and names both checks and the two roster rows (F5/F6) that route to `LA-12`; the outcome claim was already true |
| RD-65 f5 — §4 line specified the column as `NONE — not eligible`, a suffix RD-61 m3 had already replaced | restated as the one `NONE — <limbs>` string of §4's fourth outcome; §4 specifies the column once now |
| RD-65 f1 — §2 claimed the trend log carried the family reading "through the reports its rows link"; the rows link nothing | the claim is removed. The disclosure lives in the record (`reviewer.model_family`, `same_family_as_corpus_authors`) and the generated report; the trend log's silence on family is a **disclosed limit** (F5 is a disclosure, never a formula conjunct), not a claim |

## What did not change

The **schema** is byte-identical (unchanged full digest in the table below) —
RD-56 f11's deliberately-open `question_digest` alternative stays open for the
reason recorded there. The **roster**, the **question texts** (§1, §3), §8's
**parameter block** (byte-identical, as at every version since v1.5), the **verdict
vocabulary**, and the **§4 formula's conjuncts and branches** are untouched.
Every §2/§4/§5 change is a scoping or strengthening argued beside its clause;
the readiness meaning of every verdict word is unchanged. The §6 trend table
keeps its nine columns — RD-65 f1 is repaired by correcting a false claim
about them, not by adding a tenth (F5 is disclosure-only, so this is a
disclosed limit rather than a missing column).

## Disclosed limits carried forward, and one new

Carried: RD-56 f11 (`question_digest` sha256 form binds nothing —
schema-frozen); content-blindness of the placeholder lexicon (a plausible
false evidence quote defeats the tool, and no version claims otherwise);
one-place §8 prose read for E4; the JSON-Schema subset interpreter.

New at v2.4 (RD-66 f2 / RD-65 f1): the invisible-character strip sweeps
`Cf`/`Cc`/`Mn` and a named filler set — a documented approximation of
Unicode's Default_Ignorable population, not a complete model of "invisible";
and the trend log carries no family column, so F5's disclosure lives in the
record and report alone. Both are disclosed here rather than claimed absent.

## Fixtures

`--selftest`: validator 119 → **123**, renderer 34 → **38**. Every new
fixture was mutation-tested by hand in this pass — reverted on a copy and its
fixture watched to fail: the mechanical forgery sweep (reverting `_inline`
re-opens `prior_record.path` with the RD-47 f2 signature), the `Mn` strip,
the record-commit schema read (schema widened at `HEAD`, record at an
ancestor), the committed-vs-uncommitted prior read, the git-unverifiable-SDR
row outcome, the decoy instrument path, and the `--allow-invalid` exit code.

## Digests at this delta

```text
launch-gate-pre-specifications.md          1852c2c3d31eff3afa0924b6b72e855481ab2516ba8fde5eda7b2ae8772f01e8
launch-gate-administration.schema.json     e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb  (unchanged since v2.0)
scripts/validate_launch_administration.py  047098326af2f415558f0ca748a98a5889d91e9cfecaa67d700ef1ba883ba497
scripts/render_launch_administration.py    44d568e397271ff897dc13fd4cc46a9d1a9404d0d32db19b5b22dad69fa351c5
```

The formal launch packet seals digests that this delta moves; it is **stale
against v2.4** and is re-sealed only after the v2.4 reviews return, not
before — sealing unreviewed bytes is how its stop rule fired last round.

## What must happen next

One fresh policy-semantics review and one fresh machinery review of the
**v2.4 bytes** (the RD-55/RD-56 commission, fourth administration —
RD-67/RD-68). If both confirm: freeze v2.4, update the P-34 packet, re-seal
the formal packet, and P-34's approve/decline returns to the owner. If either
finds a real false-`READY` path: repair that bounded issue, re-review the
changed bytes, and record honestly that a fifth `REVISE` happened — which,
following the arm (c) reasoning the owner has now invoked once, is itself
further evidence on whether this instrument converges. This round dispatches
the pair itself, in the same round as the repair.
