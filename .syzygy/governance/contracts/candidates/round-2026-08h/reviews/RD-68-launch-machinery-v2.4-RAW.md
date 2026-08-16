# MACHINERY REVIEW — Launch-gate administration tooling **v2.4**

**Frozen commit:** `4dd6e2085237278b9f89e72be7755f5bf5c795c7`
**Date:** 2026-08-16
**Reviewer:** independent machinery reviewer, fresh context

**Digests verified (computed from `git show 4dd6e208:<path>`, all three match the brief):**

| Path | sha256 |
|---|---|
| `launch-gate-administration.schema.json` | `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` |
| `scripts/validate_launch_administration.py` | `047098326af2f415558f0ca748a98a5889d91e9cfecaa67d700ef1ba883ba497` |
| `scripts/render_launch_administration.py` | `44d568e397271ff897dc13fd4cc46a9d1a9404d0d32db19b5b22dad69fa351c5` |

**Selftest counts observed (run, not inferred):** validator `123 fixtures, 0 failing`; renderer `38 fixtures, 0 failing`. Both exit 0.

---

## f1 — BLOCKING — `[Observed]` — a record with no falsification account at all validates with **zero errors** and produces `GATE VERDICT: READY FOR …`

**Location:** `scripts/validate_launch_administration.py:278–306`, `_strip_invisible` — the category tuple `("Cf", "Cc", "Mn")` plus `_ZERO_WIDTH_FILLERS` (four `Lo` characters).

**Defect.** The strip is presented as a category sweep ("never by an enumeration of code points"), but it is an enumeration *of categories*. **`U+2800 BRAILLE PATTERN BLANK` has Unicode general category `So`.** It renders as blank in every font and — unlike the `Zs` spaces — it is **not** whitespace, so it also survives the `str.split()` normalization the placeholder lexicon applies. It therefore passes through both defences. `U+FFFC OBJECT REPLACEMENT CHARACTER` (also `So`) behaves identically.

**Concrete failing input.** Take a record that is otherwise the passing baseline (`formal: true`, `administration_kind: "full"`, `fresh_context: true`, every roster row `Met`), and set:

```
falsification_summary                = "none" + "⠀"*30
g1.critic_answer                     = "n/a"  + "⠀"*30
pilot_recurrence_check.method        = "TBD"  + "⠀"*30
question_results[*].falsification_attempt = "none" + "⠀"*30   (all 39 rows)
```

Each of those four fields is, **without** the padding, a validation error — I ran each control:

| control (unpadded) | errors | padded with U+2800 | errors |
|---|---|---|---|
| `falsification_summary = "none"` | 1 (LA-14) | same + `⠀`×30 | **0** |
| `g1.critic_answer = "none"` | 1 (LA-14) | same + `⠀`×30 | **0** |
| all 39 `falsification_attempt = "none"` | 39 (LA-6) | same + `⠀`×30 | **0** |
| `pilot_recurrence_check.method = "none"` | 1 (LA-16) | same + `⠀`×30 | **0** |

**Observed end-to-end through the shipped CLIs, from the repo root:**

```
$ python3 scripts/validate_launch_administration.py /tmp/lgrev/forged-ready.json
Formal gate result:  READY FOR Capability 1 — Project registration and honest shape visibility
record valid — the verdict above is computed from the rows
EXIT: 0

$ python3 scripts/render_launch_administration.py /tmp/lgrev/forged-ready.json -o …
EXIT: 0
  | 2026-08-11 | 4dd6e20 | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | READY FOR Capability 1 — … |
  GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

The report's §Falsification section reads, verbatim, `> none⠀⠀⠀…`, and all 39 falsification-attempt cells read `none⠀⠀⠀…`.

**Second method (VIS-2):** re-run with a *different* escaping character, `U+FFFC`, through the CLI only, with no helper of mine in the path — identical result (`exit=0`, `record valid`, `Formal gate result: READY FOR …`).

**Why this is not a disclosed residual.** `_strip_invisible`'s docstring closes with: *"A novel zero-width character outside these categories and this filler set is a disclosed residual, not a silent pass — the eligibility limbs, not this strip, are what a gate result rests on."* That sentence is **falsified by the mechanism it describes**: the fourth eligibility limb *is* the error count (`_compute`:1508–1518, `if n_err: ineligible.append(...)`), and LA-6/LA-14/LA-16 are exactly what produce those errors. Defeating the strip therefore does not merely degrade a lexicon — it removes the errors, restores eligibility, and promotes the row outcome to a formal gate result. It is a silent pass to `READY`, by the route the disclaimer claims is closed.

This is the same defect RD-66 f2 named (`U+034F` making a wholly-unfalsified record an eligible `READY`), reproduced one Unicode category over. The repair history is `5 code points` → defeated by a 6th → `(Cf, Mn)` → `Mn` dropped → `(Cf, Cc, Mn)` + 4 `Lo` → **defeated by `So`**. The shape has not changed: an enumeration is being presented as a class.

---

## f2 — MATERIAL — `[Observed]` — the "structural" forgery sweep is mechanical over `_base_record`, not over the schema; 18 schema-reachable string field shapes lie outside it

**Location:** `scripts/render_launch_administration.py:697–748` — `_maximal()` / `_string_leaves` / the sweep and its coverage assertion.

**Defect.** The sweep's denominator is `list(_string_leaves(_maximal()))`, and `_maximal()` is `_base_record(False)` plus a synthetic `prior_record`. That record leaves `operationalization_notes`, `materials.deviations`, `owner_deferrals`, `deferred_wave_findings`, `reopened_findings`, `e3.reopen_items`, `g1.proposed_missing_questions` and `pilot_recurrence_check.findings` **empty**, and every row `Met`, so `counterexample` / `unknown_reason` / `unknown_settlement` are `null`. A string field that is absent from the record is not a string leaf, so the walk cannot reach it.

**Denominators.** I built a maximally-populated valid record and diffed leaf shapes: **405** string leaves vs the sweep's **390**; **20** field shapes present in a valid record and absent from the sweep. Two of those (`operationalization_notes`, `materials.deviations`) are covered by the surviving hand-maintained `SITES` tuple, leaving **18 field shapes covered by neither the mechanical sweep nor the hand list** — including every string in `owner_deferrals`, `deferred_wave_findings`, `reopened_findings`, `e3.reopen_items`, `g1.proposed_missing_questions`, `pilot_recurrence_check.findings`, and all three per-row optional strings.

**Demonstration that the guard is absent, not merely narrow.** In a scratch clone at `4dd6e208`, I removed `_inline` from **only two** call sites — `owner_deferrals` (`render:345–347`) and `e3.reopen_items` (`render:301`), a plausible targeted regression:

```
=== SHIPPED v2.4 renderer selftest, with _inline REVERTED at owner_deferrals + e3.reopen_items ===
38 fixtures, 0 failing — a check that cannot fail is not a check
```

My maximal sweep on the same mutated renderer reports **5 forgery-bearing field shapes**, each emitting a document-level `GATE VERDICT: READY FOR everything` and a forged table. So the delta's claim — *"The next unnamed string field fails **this suite**, not the next review"* (`LAUNCH-GATE-v2.4-SEMANTIC-DELTA.md`, §"The blocking repair") — is false for 18 of the schema's string field shapes. The class the last four rounds kept re-opening is closed for the leaves `_base_record` happens to populate, not for the record shape the schema admits.

**Important scope limit, stated plainly:** this is a *fixture-coverage* defect, not a live forgery. **No forgery exists in v2.4's actual bytes.** I swept all **405** string leaves × **4** spellings (`\n`, `\r`, `\r\n`, ` `) = **1620** leaf/spelling combinations through the shipped renderer and found **0** forged document constructs; **399** of the 405 leaves were separately confirmed to reach the rendered report via unique markers (the 6 that do not are `e3.concepts[]`, `e4.fixed_case_results[].evidence`, `prior_record.repository_commit`, `prior_record.date`). My detector is mutation-validated: it reports 0 on the shipped renderer, **30** field shapes with `_inline` reverted globally, and **39** with `_VERT` reverted to `\n`-only.

**Fix direction (not prescriptive):** derive the sweep's denominator from the schema's string-bearing paths and assert every one is populated in the fixture record, so an unpopulated field is a fixture failure rather than a silent gap.

---

## f3 — MATERIAL — `[Observed]` — the delta's mutation-test claim for the `Mn` strip is false; two limbs of the RD-66 f2 repair are protected by no fixture

**Location:** `scripts/validate_launch_administration.py:303–306`; claim at `LAUNCH-GATE-v2.4-SEMANTIC-DELTA.md` §"Fixtures": *"Every new fixture was mutation-tested by hand in this pass — reverted on a copy and its fixture watched to fail: … the `Mn` strip, …"*

**Observed, by reversion on a scratch clone:**

| reversion | validator selftest |
|---|---|
| `("Cf","Cc","Mn")` → `("Cf","Cc")` — **the `Mn` repair removed** | **123 fixtures, 0 failing** |
| `_ZERO_WIDTH_FILLERS` limb removed entirely (all 4 `Lo` chars) | **123 fixtures, 0 failing** |
| → `("Cf","Mn")` | 1 failing (the `Cc` fixture) |
| → `("Cc","Mn")` | 3 failing (the three `Cf` fixtures) |
| → `("Cf",)` | 1 failing (the `Cc` fixture) |

The suite has three `Cf` fixtures and one `Cc` fixture and **no `Mn` fixture and no filler fixture**. The named repair for RD-66 f2 — restoring `Mn`, the category `U+034F` lives in — can be deleted with the suite fully green. Under this repository's own rule 6 and the delta's own banner ("a check that cannot fail is not a check"), that limb is unchecked, and the delta's account of having watched it fail cannot be correct.

---

## f4 — MINOR — `[Observed]` — two record-derived values reach a table row with no neutralizer, safe only by the schema enum

**Location:** `scripts/render_launch_administration.py:324–326` — `r['reviewer_classification']` and `auth` (`r['routing_authority_says']`) are interpolated into the E4 table row raw, while `case_text` beside them goes through `_cell`.

I confirmed the schema enums (`["shape","spec"]`, `["shape","spec","silent"]`) are enforced: a pipe-and-newline payload in either field yields `LA-1` and **0** forged rows. So there is no exploit today. It is noted only because the file's stated class property is *"every reviewer string reaches the document through a neutralizer"*, and these two are the exceptions — held by a different mechanism, one schema widening away from a table-corruption site.

---

## What I verified as sound

All `[Observed]`, each by reverting the fix on a scratch copy and watching the named fixture fall — **12 reversions performed in total**, none against a tracked file:

- **RD-66 f1 (the delta's headline claim):** reverting *only* the `_inline(p)` call in `_new_findings_cell` → **2 fixtures fail**, at `prior_record.path`, both spellings, with the exact RD-47 f2 signature (two `## Computed figures`, a forged `GATE VERDICT: READY FOR everything`). The claim is true as stated.
- **RD-65 f3 (schema at the record's commit):** `_git_show(schema_commit, …)` → `_git_show("HEAD", …)` → **1 fixture fails**. A widening committed at HEAD does not govern a record anchored at an ancestor; working-tree drift is its own error.
- **RD-66 f4 (prior read from the commit, not the working tree):** reverting to a filesystem read → **2 fixtures fail**.
- **RD-66 f6 (`--allow-invalid` exit code):** removing the `return 1` on the write path → **1 fixture fails** with `exit 0`. An invalid record cannot exit 0 through `main()`; git-unavailable exits 2.
- **RD-62 f1 / RD-56 f2 (the `\r` and inline neutralizers):** reverting either fires 39 and 30 field shapes respectively in my independent sweep.
- **Structural false-READY probes, 5 constructed, 5 caught:** duplicate `question_id` (LA-4), omitted roster row (LA-4), a genuine failure relabelled `Not met (out of launch scope)` (LA-8, both limbs), an invisible-padded `Not met` counterexample (LA-6), a duplicated `F6` (LA-4). A scoped row disclosed with any of §4's five blocking conditions is refused (LA-8); disclosed with none, it correctly does not block.

---

## Verdict

The v2.4 structural claim for the *renderer* is substantially real — the sanitizer holds across all 1620 leaf/spelling combinations I drove through it, and the delta's headline mutation test reproduces exactly as described. But the sweep that is supposed to make it durable is mechanical over a record, not a schema, and leaves 18 field shapes ungoverned (f2); the `Mn` and filler limbs of the invisible-character repair are protected by no fixture at all (f3); and, decisively, the invisible-character strip is still an enumeration wearing a class's name — a single `So` character produces a record with **no falsification account, no G1 answer, no pilot method and no per-row falsification attempt** that validates with **zero errors**, exits **0**, and renders **`GATE VERDICT: READY FOR Capability 1 — …`** into both the report and the §6 trend log (f1). That is a false-READY path, reproduced through the shipped CLIs and confirmed by a second character.

VERDICT: REVISE
