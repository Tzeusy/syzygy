# RD-47 — Structured launch-record schema and validator (round-2026-08f, frozen commit `f52c712`)

> **Provenance banner, added by the recording session — everything below the
> rule is the reviewer's raw output, copied verbatim and unedited.** The
> verdict word is copied exactly.
>
> | | |
> |---|---|
> | **Charter role** | §14 review 1 — structured launch-record schema and validator |
> | **Dispatched** | 2026-08-11 |
> | **Subject commit** | `f52c712` — bytes frozen; nothing in the subject was edited between dispatch and this record |
> | **Subject files** | `launch-gate-administration.schema.json`; `scripts/validate_launch_administration.py`; `scripts/render_launch_administration.py`; `round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.json` and `.md` |
> | **Governing references given** | `launch-gate-pre-specifications.md`; `round-2026-08f/LAUNCH-GATE-v2.0-SEMANTIC-DELTA.md` (given as claims to test, not as evidence) |
> | **Context** | fresh — the reviewer was given the subject, the governing references and the acceptance criteria, and no project history |
> | **Model family** | same family as the corpus authors. This review therefore **supports repair and is not the formal launch administration** (charter §2.15) |
> | **Verdict** | `REVISE` |
>
> **Disposition is not recorded here.** This file is the reviewer's bytes.
> What was repaired, declined, or deferred is recorded separately, and no
> repair may edit this file.

---

VERDICT: REVISE

---

## A. Can a record claim its own verdict?

**What I did.** Built a clean baseline record bound to the live instrument at `f52c712` (via `_base_record(git_bound=True)`; it computes `READY FOR Capability 1 …` with zero errors), then attacked the closure property by 13 structural routes plus 3 prose routes, running the real validator on each.

**What I observed.** Every structural route is refused, at every nesting depth:

| route | result |
|---|---|
| top-level `final_verdict` | rejected — *"unknown field 'final_verdict' — the verdict is computed, never claimed"* |
| `gate_verdict`, `FINAL_VERDICT`, `final-verdict`, `"final_verdict "` (trailing space) | rejected |
| nested in `e3`, `reviewer`, `g1`, `pilot_recurrence_check` | rejected |
| nested in a `question_results[]` row, an `evidence[]` entry, an `e4.fixed_case_results[]` item | rejected |
| nested in the `prior_record` object | rejected (`matches 0 of the oneOf branches`) |

Sweep with denominator: the schema declares `additionalProperties: false` on **14 of 14** object schemas (top level, `instrument`, `reviewer`, `materials`, `e3` + `trace_rows.items` + `reopen_items.items`, `e4` + `fixed_case_results.items`, `owner_deferrals.items`, `deferred_wave_findings.items`, `reopened_findings.items`, `pilot_recurrence_check`, `g1` + `proposed_missing_questions.items`, `prior_record` branch, `$defs/question_result` + `evidence.items`). No node is open.

**But the prose route works, and it reaches the human.** `falsification_summary` and `g1.critic_answer` are emitted as raw Markdown (`render_launch_administration.py:259`, `:273`). I built a record whose rows compute **NOT READY** (E5 `Not met`) and whose free text carries a forged verdict. It validates clean and renders **without** `--allow-invalid`:

```
132: ## Falsification
136: GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
187: ## Computed figures          <- forged, injected via g1.critic_answer
192: GATE VERDICT: READY FOR Capability 1
197: ## Computed figures          <- the real one
223: GATE VERDICT: NOT READY
```

**Judgement.** The *record* cannot claim a verdict — that property holds completely. The *report*, which is what §5 puts in front of the owner, can be made to display a forged verdict and a forged computed-figures section by schema-lawful free text. Finding 2.

## B. Can a record hide a failure?

Ran each named route against the passing baseline.

- **`deferred-wave-only`** — works only as §4 permits: A–D only (`E5`/`F3` scoped → LA-5 error), and only with a `deferred_wave_findings` entry naming that question, whose `wave` is in `deferred_waves`, with an empty `blocking_conditions_met` (any of the five → LA-8 error; two findings on one row, one dirty → caught). Laundering costs four coordinated deliberate acts. The five blocking conditions are reviewer-declared and mechanically unverifiable — inherent to §4, not a code defect.
- **Owner deferral** — deferrals on `E3`, `A1`, `F4` all rejected by LA-11 (`NEVER_DEFERRABLE` = every E row + all 22 A–D rows + F1/F3/F4). A deferral on `F5` alone against a passing core → LA-12 error, NOT READY. **But** `decision_citation: ".syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md"` — the queue of decisions *not* made — is accepted with **zero errors** and turns a `Not met` F2 into `READY-WITH-DEFERRALS`. `_sdr_exists` explicitly excludes that file for `SDR-n` citations; the path branch does not. `.beads/issues.jsonl` is likewise accepted. Finding 4.
- **Unknown** — `Unknown` on all 22 A–D rows still computes READY. This is §4 exactly ("`Unknown` in launch-scope A–D does not block by itself"), and the count is visible in the Unknown trend column (22). Instrument property, not a defect. `Unknown` on any E row, F3 or F4 blocks.
- **Omitting a roster row** — LA-4 catches every case tested (drop A2; drop E5; drop F3; drop all five E1 sub-rows), and the renderer refuses. Roster sweep: §3 declares 35 questions; the roster is those 34 verdict questions plus E1's five sub-rows = 39; G1 is deliberately excluded (a section, not a row). 0 unaccounted.

**Judgement.** Three of four routes are closed as designed. The deferral-citation route has one live hole that converts NOT READY into a pass.

## C. Is the code's formula §4's formula?

§4, quoted:

> **READY FOR `<LAUNCH_TARGET>`** = every E question `Met` … AND no `Not met` in launch-scope A–D … AND F1 is `Met` or `Unknown` … AND F3 is `Met` AND F4 is `Met` AND (F2 is `Met` OR explicitly owner-deferred with a bounded reduction plan)

`validate_launch_administration.py:862–877`, quoted:

```python
e_all_met = all(verdict_of.get(q) == MET for q in E_ROWS)
ad_blockers = [q for q in AD_ROWS if verdict_of.get(q) == NOT_MET]
_c("F1 is Met or Unknown", verdict_of.get("F1") in (MET, UNKNOWN), …)
_c("F3 is Met", verdict_of.get("F3") == MET, …)
_c("F4 is Met", verdict_of.get("F4") == MET, …)
_c("E3's reopen list is empty", not rec["e3"]["reopen_items"], …)
```

Conjunct by conjunct:

| §4 conjunct | code | verdict |
|---|---|---|
| every E `Met` | `E_ROWS` = all 11 E rows incl. E1's five sub-rows | **same** (stricter only where §3 already requires it: "E1 is Met only when all five are") |
| no `Not met` in launch-scope A–D | `AD_ROWS` (22), plain `NOT_MET` only; scoped excluded | **same** — and LA-5 forces `launch_scope: in-launch-scope` on every plain `Not met`, so the two readings coincide |
| F1 `Met` or `Unknown` | identical | **same** |
| F3 `Met` | identical | **same** |
| F4 `Met` | identical | **same** |
| F2 `Met` OR owner-deferred | plain branch: `core and f2_met and n_deferred == 0`; deferrals branch: `core and f2_deferred and n_deferred > 0` | **same**, and matches §4's "plain `READY FOR` over a nonzero `Deferred count:` is a contradiction" |
| — | `E3's reopen list is empty` | **addition**, sourced from §3 ("the list is non-empty; 'ready' is then false regardless of every other verdict"), strictly fail-closed |

Behavioural spot-checks agreed in all 13 formula fixtures plus my own: `Not met` in A–D → NOT READY; scoped alone → READY; `Not met` E → NOT READY; `Unknown` F1 → READY; `Not met` F1/F3/F4 → NOT READY; `Not met` F2 + cited deferral → READY-WITH-DEFERRALS; `Unknown` F2 + deferral → READY-WITH-DEFERRALS; deferral beside a Met F2 → NOT READY + error (correct by elimination: neither §4 pass predicate is satisfiable).

**Judgement. No discrepancy in the permissive direction.** The one addition is more conservative than §4's literal text and is anchored in §3. This is the criterion where a finding would have been most serious, and there is none.

## D. Does the validator silently ignore unimplemented schema keywords?

**What I did.** 16 keyword injections into scratch copies of the schema, run through the real validator via `--schema`.

**What I observed.** All 16 hard-error: `maxLength`, `propertyNames` (nested three levels into `$defs`), `allOf`, `if`/`then`, `not`, `maxItems`, `format`, `dependentRequired`, `patternProperties`, `unevaluatedProperties`, `prefixItems`, `anyOf`, `$comment`, `definitions`, `exclusiveMinimum`, and `additionalProperties: true`. The claim is true and the recursion reaches every schema-valued position (`properties`, `$defs`, `items`, `oneOf`).

**The complementary gap is open.** The audit rejects keywords it does not implement; it never asserts that an object schema *closes*. Deleting `additionalProperties` from `$defs/question_result` and adding `final_verdict: "READY FOR everything"` to a row → **0 errors, verdict `READY FOR …`**. Since `--schema` is an operator-supplied path, the single guard the "a verdict cannot be claimed" property rests on can be removed with nothing noticing. Finding 6.

## E. Does anything in the correctness path parse generated Markdown or classify HTML/Markdown visibility?

**Sweep with denominator.** 12 `re.*` sites in `validate_launch_administration.py`, 0 in `render_launch_administration.py`. Classified:

- 4 operate on record strings/identifiers (schema `pattern`, `_sdr_exists`, the two citation `fullmatch`es) — no Markdown.
- 1 is whitespace normalisation.
- **7 read the instrument's Markdown**, in 5 functions: `param_block_bytes` (376, 380), `instrument_version` (389), `launch_target_forms` (395), `_yaml_list` (401), `e4_cases` (421, 425).
- 0 read a generated `.md`. `--check` compares bytes (`out.read_text() != text`), never structure. Grep for `html|bs4|visibility|hidden|DOM|display:` finds only docstring prose. `launch_gate_results.py` takes an explicit CLI path and never globs; `check_governance.py` has no reference to these files.

**The documented exception** is `e4_cases`, whose docstring claims to be "the one place the validator reads the instrument's own prose." It is bounded and fail-closed as claimed: it anchors at the `` `E4_CASES` `` marker, consumes numbered quoted items only while their numbers run consecutively from 1, and returns `None` → LA-10 error, never "no cases to check". Verified: it parses exactly 6 cases from §8 at HEAD.

**But the "one place" claim is false by a denominator of 5**, and two of the other four fail *open*:

| instrument reader | on failure to parse | |
|---|---|---|
| `param_block_bytes` | `None` → LA-2 error | fail-closed |
| `launch_target_forms` | falls back to the whole block → mismatch error | fail-closed |
| `e4_cases` | `None` → LA-10 error | fail-closed |
| `instrument_version` | `None` → `if ver and …` skips the check | **fail-open** |
| `_yaml_list` | `None` → `if want is not None` skips the check | **fail-open** |

**Judgement.** The stated class property (no generated Markdown parsed, no HTML/visibility classifier) holds absolutely. The bounded-exception claim is understated, and two unmentioned instrument readers are silent no-ops on failure. Findings 1 and 9.

## F. VIS-2 — can a count that should be non-zero render as zero or absent?

Two live routes, both demonstrated:

1. **New-findings-vs-prior always renders as an affirmative absence.** §6: *"the New-findings column is computed against the record the `prior_record` field names."* The code computes it against the `--prior` **CLI argument** (`validate:909`), never the field — and `render_launch_administration.py` has no `--prior` option at all (`error: unrecognized arguments: --prior`). A record declaring a real ancestor prior and carrying **4 new `Not met` rows** renders:

   ```
   - New findings vs prior: n/a (no prior record)
   | 2026-08-11 | f52c712 | 4 | 0 | 0 | 0 | 0 | n/a (no prior record) | NOT READY |
   ```
   With `--prior` supplied to the validator directly, the same record yields `4`. The rendered string is not "not computed" but "**no prior record**" — a false claim of absence, in the column §6 says F1 is answered from "and only from it". Finding 3.

2. **The wave/version binding silently green.** End-to-end in a scratch git repo: reformat §8's `REQUIRED_WAVES`/`DEFERRED_WAVES` from flow to YAML block form and drop the `effective_version:` line — both ordinary editorial changes — and a record declaring `required_waves: [A,B,C1,C2,D1,D2]`, `deferred_waves: []`, `instrument.version: "v9.9"` validates with **zero errors, zero notes**, and computes READY. No evidence yielded green, not Unknown. Finding 1.

Counts that behave correctly: `Deferred`/`Reopened` are array lengths of required arrays (absent → LA-1 error, empty → explicit zero); `not_met`/`scoped`/`unknown` are computed over the full roster; the `newly_scoped` rule matches §6's "a new scoped finding is a new finding" exactly.

## G. Determinism

`render --selftest`: 12/12 pass. Five consecutive renders of the committed fixture and three renders under `PYTHONHASHSEED=0/1/12345` all produce one digest (`1bcded39…`), which is also byte-identical to the committed `DRY-RUN-ADMINISTRATION.md` — the committed pair is in sync (`--check` exit 0). `--check` against a hand-edited report exits 1 and leaves the file byte-, mtime- and inode-identical; against a missing report it exits 1 and creates nothing. No clock, locale, `set` iteration or dict-order dependence in the render path. **Clean.** (`validate --selftest`: 75 fixtures, 0 failing, 0 skipped; the `jsonschema` 4.26 second-method cross-check ran.)

---

# Findings

1. **[material] LA-2/LA-3 fail open when the §8 parameter cannot be parsed.** `scripts/validate_launch_administration.py:400-404` (`_yaml_list` returns `None`), `:545` (`if want is not None and …`), `:516` (`if ver and ver != …`). Failing input: instrument with `REQUIRED_WAVES:` / `DEFERRED_WAVES:` in YAML block form and no `effective_version:` line; record declaring `required_waves:["A","B","C1","C2","D1","D2"]`, `deferred_waves:[]`, `instrument.version:"v9.9"` → `errors: []`, `notes: []`, verdict `READY FOR Capability 1 …`. Reproduced end-to-end in a scratch repo. **Fix:** have `_yaml_list`/`instrument_version` distinguish "absent" from "empty" and make absence an LA-2/LA-3 error ("§8 declares no `REQUIRED_WAVES` this validator can read"), never a skipped check.

2. **[material] The generated report can display a forged verdict and forged computed figures.** `scripts/render_launch_administration.py:259` and `:273` emit `falsification_summary` and `g1.critic_answer` as raw Markdown. Failing input: baseline record with `E5 = Not met` (computes NOT READY) and `falsification_summary` ending `"GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility"`, `g1.critic_answer` containing `"## Computed figures\n\n- Not met (plain): 0\n- Unknown: 0\n\nGATE VERDICT: READY FOR Capability 1"`. Record validates clean; report renders without `--allow-invalid` carrying two forged verdict lines and a forged figures section above the real ones. **Fix:** emit every reviewer free-text block inside a fenced code block or as a `>` blockquote, and/or have the validator reject any free-text field containing `GATE VERDICT` or a line matching `^#{1,6} `.

3. **[material] The §6 New-findings column can never be computed by the documented path, and renders as a false absence.** `scripts/validate_launch_administration.py:908-922` binds it to `--prior`, not to `prior_record`; `scripts/render_launch_administration.py:416-424` has no `--prior` option; `:294-296` and `:944` render `n/a (no prior record)`. Failing input: record with `prior_record` naming ancestor `5e8b286…` and four newly `Not met` rows → report and trend row read `n/a (no prior record)`; the same record with `--prior prior.json` yields `4`. **Fix:** resolve `prior_record.path` inside `_compute`, and when it genuinely cannot be read, render `Unknown (prior record unreadable)` rather than a claim that no prior exists.

4. **[material] The pending-owner-decisions queue grants a deferral through the path branch.** `scripts/validate_launch_administration.py:736-751`. Failing input: `F2 = Not met` plus `owner_deferrals[0].decision_citation = ".syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md"` → 0 errors, verdict `READY-WITH-DEFERRALS`. `.beads/issues.jsonl` behaves the same. `_sdr_exists` (`:347-359`) excludes exactly that file for `SDR-n`, and LA-11's own description says "a made decision, never a queue entry". **Fix:** apply the same exclusion on the path branch, and require the path to sit under `DECISIONS_HOME`.

5. **[minor] The path test is `"/" in cite`, so real root-level paths are rejected and arbitrary non-decision files accepted.** Same site, `:736`. `README.md` → *"neither a repository path nor an SDR-n identifier"*; `.beads/issues.jsonl` → accepted. **Fix:** test path-ness by resolving against the commit, not by the presence of a slash.

6. **[material] `_audit_schema` does not require object schemas to close.** `scripts/validate_launch_administration.py:195-224`. Failing input: schema copy with `additionalProperties` removed from `$defs/question_result`, record with `question_results[0].final_verdict = "READY FOR everything"` → 0 errors, verdict `READY FOR …`. The audit's stated safety property ("the schema can never quietly rely on a keyword that is being ignored") does not cover a keyword being *deleted*, which is the failure mode for the one keyword the design depends on. **Fix:** in `_audit_schema`, emit an error for any node carrying `properties` without `additionalProperties: false`.

7. **[minor] `e4.routing_authority` is recorded and rendered but never bound to §8.** Schema `properties/e4/properties/routing_authority`; no comparison site exists in the validator. Denominator: of the ~28 substantive §8 parameters, 4 are bound (`LAUNCH_TARGET`, `REQUIRED_WAVES`, `DEFERRED_WAVES`, `E4_CASES`); `E4_ROUTING_AUTHORITY` is the only one the record restates without binding — a figure quoted outside its owning artifact. **Fix:** parse the `E4_ROUTING_AUTHORITY` row from §8 and compare, as LA-3 does for the launch target.

8. **[minor] Evidence paths are commit-anchored but never existence-checked, while deferral paths are.** `scripts/validate_launch_administration.py:596-602`. Failing input: `A1 = Met` with `evidence[0] = {"path":"NO/SUCH/FILE-INVENTED.md","commit":<record commit>,"locator":"line 4000","quote":"whatever I want"}` → clean. **Fix:** run `_path_kind` over each evidence path (the machinery already exists); leave quote truthfulness to the reader, as documented.

9. **[minor] A claim of absence with the wrong denominator.** `scripts/validate_launch_administration.py:414-419`: *"This is the one place the validator reads the instrument's own prose."* There are 5 such functions and 7 regex sites. **Fix:** restate as "the E4 case walk is the only instrument read whose output is compared clause-by-clause; the other four are `param_block_bytes`, `instrument_version`, `launch_target_forms`, `_yaml_list`", and fix the two that fail open (finding 1).

10. **[minor] `--allow-invalid` crashes on a record with a schema error.** `scripts/render_launch_administration.py:441`; `validate` returns `computed = {}` and the record's fields may be absent. Failing input: baseline record with `g1` removed, `--allow-invalid` → `KeyError: 'g1'` traceback. The documented inspection path does not work for the commonest invalid record. **Fix:** guard `render` on `computed` being populated and on missing fields, or refuse with a message.

11. **[minor] A pass verdict is displayed for records that cannot support one.** `scripts/validate_launch_administration.py:1473-1478` prints `Computed gate verdict: READY FOR …` *above* the error list for an invalid record; and a `administration_kind: delta`, `formal: false` record renders a report ending `GATE VERDICT: READY FOR Capability 1 …` whose only disclaimer is an Identity bullet ~190 lines earlier — though §2 says a delta record "is rejected as gate evidence". **Fix:** prefix the CLI verdict line when errors exist, and stamp the report's verdict line for non-formal or delta records.

12. **[minor] Duplicate JSON keys are silently last-wins.** `json.loads` with no `object_pairs_hook` (`:461`, and `render:63`). Failing input: a record file with `"administration_kind": "full"` early and `"administration_kind": "delta"` appended — the tool uses the second, a human reading the file sees the first. **Fix:** parse with an `object_pairs_hook` that errors on duplicate keys.

---

# What I could not test and why

- **Whether the reviewer-declared judgement fields are true.** `blocking_conditions_met`, `needed_by_launch_target`, `routing_authority_says: "silent"`, `same_family_as_corpus_authors`, `fresh_context`, and every evidence quote are self-declared and content-blind by design. I confirmed the *mechanics* around them; their truthfulness is unfalsifiable from the record. Note the asymmetry: a scoped row must be disclosed in `deferred_wave_findings`, but an E4 case laundered from "disagree" to `"silent" + needed_by_launch_target: false` requires no disclosure anywhere and no cross-read of the routing authority.
- **Whether the committed `DRY-RUN-ADMINISTRATION.json` answers its 39 questions correctly.** I verified it validates clean, is `delta`/`formal: false`, carries `Unknown` on all 39 rows, computes NOT READY, and that its `.md` is byte-identical to a fresh render. The substantive correctness of an all-Unknown dry run was not in scope.
- **The instrument's own soundness** (whether §4's conjunct set is the right one, whether `Unknown` across all 22 A–D rows *should* pass). I tested code-against-instrument, not instrument-against-reality.
- **Behaviour with `git` absent.** The `_git=False` path emits an explicit note ("this record is not fully validated") and I exercised it through the selftest, but I did not run the CLI on a machine without git.
- **The digest binding of the schema and record inside the administration packet.** I verified the instrument and parameter-block digests are enforced against the named commit; whether the packet correctly digest-binds `launch-gate-administration.schema.json` itself (which finding 6 makes load-bearing) is outside the four subject files.
