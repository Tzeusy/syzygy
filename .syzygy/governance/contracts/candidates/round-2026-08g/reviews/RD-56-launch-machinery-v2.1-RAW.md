# RD-56 — raw reviewer output, launch-gate machinery at v2.1

> **Provenance banner. Everything below the rule is the reviewer's raw
> output, copied verbatim and unedited** — including any error it contains.
> Corrections live in the disposition register, never here.
>
> | | |
> |---|---|
> | Role | Schema, validator and renderer reviewer (charter §7.7, review 2 of 2) |
> | Dispatched | 2026-08-13 |
> | Subject commit | `939363f` |
> | Subject digests | schema `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` · validator `22178af793770255815c98f9c88f6cab158a66ce328be285afe5c4096d16b631` · renderer `c9f81cb42853872735fcc25727a7660742e9c5a9db257ce483766976b9141d10` |
> | Context | Fresh — no prior contact with this repository's review history |
> | Model family | **Same as the corpus's authors.** This review therefore supports repair and is **never** the formal launch administration (instrument §2, F5) |
> | Verdict | `REVISE` — copied exactly |
>
> Dispatched **after** RD-55 returned and against the identical frozen bytes,
> with no knowledge of RD-55's findings. The two reviews found the same
> blocking defect independently; that convergence is evidence, and it is
> recorded in the disposition register rather than here.

---

# RD — v2.1 launch-gate machinery: schema, validator, renderer

Subject re-verified at the end of the session: the three digests are byte-identical to those in the commission, `git status --porcelain` shows the one untracked root `.md` it showed at start, and no worktree was created. All probes live under the scratchpad. `--selftest`: 88 fixtures / 0 failing / 0 skipped (validator), 16 / 0 (renderer); the `jsonschema` second-method cross-check ran.

Method throughout: a probe harness built on the tools' own `_base_record(git_bound=True)`, bound to the live instrument at `939363f`; a scratch git repository at `scratchpad/fake` for instrument mutations; twelve single-repair reversions of *copies* of the scripts (`scratchpad/revert_matrix.py`) to measure fixture discrimination; a stub `git` returning exit 128 on `PATH` for the degradation path.

---

## A. RD-47 repair completeness — all twelve findings reproduced against the current bytes

Denominator: 12 of 12 findings attacked. Result: **7 repaired, 4 partly repaired, 1 not repaired.**

| # | RD-47's own words (quoted) | Status |
|---|---|---|
| 1 | *"LA-2/LA-3 fail open when the §8 parameter cannot be parsed."* | **Repaired in behaviour; unfixtured** — see f4 |
| 2 | *"The generated report can display a forged verdict and forged computed figures."* | **Partly repaired** — f2, reproduced verbatim |
| 3 | *"The §6 New-findings column can never be computed by the documented path, and renders as a false absence."* | **Repaired**, and the repair opened f6 |
| 4 | *"The pending-owner-decisions queue grants a deferral through the path branch."* | **Partly repaired** — f5 |
| 5 | *"The path test is `"/" in cite`, so real root-level paths are rejected and arbitrary non-decision files accepted."* | **Repaired** |
| 6 | *"`_audit_schema` does not require object schemas to close."* | **Partly repaired** — f3 |
| 7 | *"`e4.routing_authority` is recorded and rendered but never bound to §8."* | **Repaired** (and see f8) |
| 8 | *"Evidence paths are commit-anchored but never existence-checked, while deferral paths are."* | **Repaired** |
| 9 | *"A claim of absence with the wrong denominator."* | **Not repaired** — f9 |
| 10 | *"`--allow-invalid` crashes on a record with a schema error."* | **Not repaired, not disclosed** — f10 |
| 11 | *"A pass verdict is displayed for records that cannot support one."* | **Partly repaired** — f1 |
| 12 | *"Duplicate JSON keys are silently last-wins."* | **Repaired** (nested and `\u`-escaped both refused) |

Reproductions of the three clean repairs, for the record. f5: `.decisions/…/README.md` at root level now resolves and is refused with the correct reason, `.beads/issues.jsonl` refused as outside the decisions home. f8: `{"path":"NO/SUCH/FILE-INVENTED.md", …}` → `LA-6: A1 evidence[0] cites 'NO/SUCH/FILE-INVENTED.md', which is not a file at 939363f…`. f12: `{"…","administration_kind":"delta"}` → `LA-1: record is not valid JSON: duplicate key 'administration_kind'`; a duplicated `verdict` inside `question_results[0]` likewise. f3: a record naming a real prior with four newly-`Not met` rows now computes `4`, not `n/a`.

Two things the delta claims that the bytes do not support are called out at f4 and f9.

---

## Findings

### f1 — BLOCKING. Eligibility omits §4's fourth limb, so an **invalid** record still deposits `READY FOR …` in the §6 trend log and in the report's last line

§4, the clause this very pass added *(D-3)*, quoted:

> | **Administration eligibility** | Separately determined: a record is eligible to be cited as launch evidence only when it is `formal`, of kind `full`, declares fresh context, **and validates without error** |

and

> A delta, non-formal, stale or invalid administration may therefore produce a diagnostic row outcome. **It may never produce a `READY FOR` gate result.**

`_compute` (`scripts/validate_launch_administration.py:1069–1078`) computes eligibility from three of the four limbs. `errors` are not in scope at that call site and are never consulted:

```python
ineligible = []
if not rec["formal"]: …
if rec["administration_kind"] != "full": …
if not rec["reviewer"]["fresh_context"]: …
eligible = not ineligible
gate_result = verdict if eligible else "NO FORMAL GATE RESULT"
```

`trend_row` (`:1140–1156`) then branches on `computed["eligible"]` alone, and the renderer's terminal `GATE VERDICT:` line (`render_launch_administration.py:359–368`) on `computed.get("eligible")` alone.

**Attack run.** A `formal`/`full`/fresh-context record, every row `Met`, with a *forged instrument sha256* (`"a"*64`) — the one field LA-2 exists to bind:

```
$ python3 scripts/validate_launch_administration.py A1_invalid_eligible.json --trend-row
Row/formula outcome: READY FOR Capability 1 — Project registration and honest shape visibility
Formal gate result:  NONE — the record has 1 validation error(s); an invalid record supports no gate decision
  …
Trend row (§6):
| 2026-08-11 | 939363f | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | READY FOR Capability 1 — Project registration and honest shape visibility |

1 validation error(s):
  LA-2: instrument digest mismatch — the record quotes aaaaaaaaaaaa…, the committed instrument is 3afdffdab0d7…
```

The CLI's own two-line separation is correct. The **generated §6 row printed directly beneath it is not** — and §6 says *"The row is generated, not transcribed: `validate_launch_administration.py --trend-row` prints it from the source record"*, i.e. this string is what gets appended to `TREND-LOG.md`, the log §6 says *"F1 — which is answered from this log and only from it"*.

Rendering the same record through the documented inspection path is worse:

```
$ python3 scripts/render_launch_administration.py A1_invalid_eligible.json --allow-invalid -o A1.md
$ tail -3 A1.md
GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
```

The `THIS RECORD DOES NOT VALIDATE` stamp sits 207 lines above it. [Observed]

This is the residue of RD-47 f11, which the delta's D-3 claims to have closed *"every place a gate result is stated"*. It closed three of the four gates §4 names. `render()` already receives `valid` as a parameter and does not use it in this branch; `validate()` already has `errors` in scope at the `_compute` call.

### f2 — BLOCKING. RD-47 finding 2's forgery reproduces verbatim through any of 19 unblockquoted free-text sites

The delta states the repair as a class property:

> Free text is **data**: every line blockquoted, so no line can open a heading, table or fence at document level. **Structure is forbidden rather than a list of phrasings**

`_quoted` is applied at exactly two call sites — `render_launch_administration.py:305` (`falsification_summary`) and `:319` (`g1.critic_answer`) — the two fields RD-47 happened to name. **Sweep with denominator** (mechanical extraction of every `a(…)` statement inside `render()`, then manual classification): 34 statements interpolate record or computed data; 2 route through `_quoted`, 5 through `_cell` (which strips `|` and `\n`), and **27 emit raw**, of which **19 carry reviewer-authored free text** — `launch_target`, `instrument.path`, `required_waves`/`deferred_waves`, all three `reviewer` strings, all three `materials` arrays, `operationalization_notes`, `e3.reopen_items[].item`/`.why`, `e4.routing_authority`, `deferred_wave_findings[].defect`, `owner_deferrals[].decision_citation`/`.bounded_reduction_plan`, `reopened_findings[]` (three), `pilot_recurrence_check.method`, `unknown_reason`/`unknown_settlement`, `g1.proposed_missing_questions[]`. So the guard covers 2 of 21 free-text-bearing sites.

**Attack run.** RD-47's own forgery, routed through `operationalization_notes` instead. A record with `E5 = Not met`, computing `NOT READY`, validating with **zero errors** and rendered **without** `--allow-invalid`:

```
$ grep -Fn "GATE VERDICT" B1.md
52:GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
227:GATE VERDICT: NOT READY
$ grep -Fn "## Computed figures" B1.md
43:## Computed figures     <- forged
199:## Computed figures     <- real
```

Rendered region, at document level:

```markdown
## Operationalization notes

- nothing unusual

## Computed figures

*Every figure below is computed from the record by `validate_launch_administration.py`; none is transcribed.*

- Not met (plain): 0
- Unknown: 0

ROW/FORMULA OUTCOME: READY FOR Capability 1 — …

GATE VERDICT: READY FOR Capability 1 — …
```

That is finding 2's failing case, character for character in effect, against the bytes that claim to repair it. [Observed] §5 puts this file in front of the owner (*"a presentation for human reading"*), so the defect is exactly as severe as RD-47 judged it.

### f3 — MATERIAL. `--schema` is unauthenticated, so LA-1 can be turned off wholesale — a strictly easier version of RD-47 f6

The closure repair itself is sound. **Sweep with denominator, two methods:** walking the schema tree finds 111 nodes, 18 declaring `properties`, 18 declaring `additionalProperties`, all `false`; a literal text count of `"additionalProperties": false` also returns 18, and `"type": "object"` also 18. Mutating a **copy** and deleting `additionalProperties` at each of the 18 nodes in turn: the audit fires at **18/18**, and RD-47's exact exploit (`$defs/question_result` + `question_results[0].final_verdict`) is now refused.

But `_audit_schema` is vacuous on a schema that declares no `properties` at all, and `--schema` is a documented operator flag bound to nothing — no digest, no path check, no comparison with `DEFAULT_SCHEMA`. With `scratchpad/weak.json` containing `{"type": "object"}`:

```
$ python3 scripts/validate_launch_administration.py A3_weakschema.json --schema weak.json --trend-row
Row/formula outcome: READY FOR Capability 1 — Project registration and honest shape visibility
Formal gate result:  READY FOR Capability 1 — Project registration and honest shape visibility
| 2026-08-11 | 939363f | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | READY FOR Capability 1 — … |
record valid — the verdict above is computed from the rows       (exit 0)
```

The record carried `final_verdict: "READY FOR everything"` at top level and rows reading `"Met with caveats"` and `"Not met, mostly"` — the latter is an A–D row that would have blocked as `Not met` and does not, because `_compute` tests string equality against `NOT_MET`. [Observed]

The docstring's claim for LA-1 — *"schema conformance against the committed JSON Schema"* — is false on this path, silently. The renderer is unaffected (it has no `--schema`).

### f4 — MATERIAL. The RD-47 f1 repair has **no discriminating fixture**, and the fixture that claims to test it passes against the unrepaired v2.0 validator

The validator's docstring: *"Checks (each with at least one `--selftest` mutation fixture)"*. §5: *"(`LA-1` … `LA-16`, each with at least one mutation fixture)"*. The delta: *"Thirteen new fixtures, **one per repaired predicate**"*.

**Method.** Twelve single-repair reversions applied to *copies* of the scripts, each running both selftests. Denominator: 12 reverted repairs.

| reverted repair | validate fails | render fails |
|---|---|---|
| f1a — wave binding fails open again | **0** | 0 |
| f1b — instrument version fails open again | **0** | 0 |
| f6 — closure audit removed | 1 | 0 |
| f4/f5 — deferral home + queue checks removed | 3 | 0 |
| f8 — evidence path existence removed | 1 | 0 |
| f12 — duplicate keys last-wins | 1 | 0 |
| f7 — LA-3b removed | 1 | 0 |
| f3 — `prior_record.path` not consulted | 1 | 0 |
| f3b — unreadable prior collapses to absence | 1 | 0 |
| D-3 — eligibility always true | 3 | 0 |
| D-3 — trend row always carries the verdict | 1 | 0 |
| f2 — free text emitted raw | 0 | 3 |

**10 of 12 discriminate. The two that do not are RD-47 finding 1** — the delta's own first row, and the finding whose attack ("a record could declare any wave set and pass") is the most direct route to a false pass.

The fixture that names it is a false witness:

```python
case("LA-3 an unreadable REQUIRED_WAVES is an error, not a skip",
     lambda r: r.update(required_waves=["A", "B", "C1", "D1"]),
     "LA-3", git=True)
```

It mutates the *record*, so §8 stays perfectly readable and it hits the pre-existing mismatch branch; its expectation is the bare substring `"LA-3"`, which the mismatch message also contains. Run against the v2.0 validator recovered from `efa6d63`:

```
v2.0 validator, v2.1 fixture mutation:
   expectation substring 'LA-3' present? True
   errors: ["LA-3: required_waves is ['A','B','C1','D1'] but §8's REQUIRED_WAVES is ['A','B'] — …"]
```

[Observed] It passed before the repair existed. `instrument_version`'s unreadable branch received no fixture at all.

The repair *is* real — I verified it end-to-end in a scratch repo whose §8 uses YAML block form and whose `effective_version:` line is renamed, which is RD-47's original failing input. Current bytes emit three errors naming `REQUIRED_WAVES`, `DEFERRED_WAVES` and `effective_version`; the reverted copy emits none of them and computes `READY FOR Capability 1` with all six waves declared required. So the tool is right and the fixture set does not know it. Repo verification rule 6 — *"Mutate the input and confirm the check fails, per predicate, before trusting it"* — is unmet for this predicate, and the delta's "one per repaired predicate" is a claim the bytes refute.

### f5 — MATERIAL. RD-47 f4 is partly repaired: three decisions-home files that record no owner decision still grant a deferral, including one §4 names explicitly

The repair replaced *"anything with a slash"* with *"any blob under `.syzygy/governance/decisions/` whose basename is not one of three"* (`_NON_WARRANT_FILES`, `:132–136`).

**Sweep with denominator.** All 20 files under the decisions home at `939363f`, each cited as `owner_deferrals[0].decision_citation` against a `Not met` F2. **16 accepted, 4 refused.** Of the 16 accepted, at least three record no owner ruling:

- `.syzygy/governance/decisions/LICENSE-DECISION-PACKET.md` — 0 errors, `READY-WITH-DEFERRALS`. Its own bytes: *"The license choice is the owner's and remains PENDING"* and *"**Status: no licence is declared, and this packet does not choose one.**"* §4, as amended at v2.1 by this very pass, quoted: *"neither is a queue entry, a Beads issue, or **a candidate decision packet**, each of which records that the owner has **not** ruled."* The clause was added; the check that would enforce it was not.
- `.syzygy/governance/decisions/launch-gate/TREND-LOG.md` — 0 errors. The trend log is *F1's evidence*; citing it as the warrant for deferring F2 is circular and passes clean.
- `.syzygy/governance/decisions/launch-gate/HISTORY.md` — 0 errors. A repair-chain history, which `AGENTS.md` routes as *"not default context"*.

Related, same site: the refusal message is wrong for two of the four rejects — `PROCESS-LESSONS.md` and `launch-gate/README.md` are both reported as *"is the pending-decision queue, not a decision"*, which neither is.

And the comment above `_NON_WARRANT_FILES` claims *"One list, both branches."* It is not: `_sdr_exists` (`:412–424`) hardcodes an exclude pathspec for `PENDING-OWNER-DECISIONS.md` only, so an `SDR-n` appearing solely in `README.md` or `PROCESS-LESSONS.md` would be accepted by the identifier branch and refused by the path branch. I swept all 33 distinct `SDR-n` identifiers in the decisions home at HEAD and **none is currently in that position**, so there is no live exploit — but the comment states a property the code does not have. [Observed]

### f6 — MATERIAL. The §6 New-findings column can be laundered to `0` against an arbitrary file outside the repository

RD-47 f3's repair binds the comparison to `rec["prior_record"]["path"]` (`:1104–1110`):

```python
if src is None and rec.get("prior_record"):
    src = str(REPO / rec["prior_record"]["path"])
```

LA-15 (`:948–983`) anchors `prior_record.repository_commit` (must exist, must be an ancestor) and `prior_record.date`. It never checks that `path` exists, that it is committed, that it is a record, or that its own `repository_commit` equals the one the record declares. The read is `Path(src).read_text()`, and `REPO / "../../../…"` escapes the repository.

**Attack run.** A record with four genuinely new `Not met` rows (A1, A2, B3, C5), `prior_record.repository_commit` set to a real ancestor of `939363f`, and `prior_record.path` traversing out to a five-line hand-written JSON asserting every roster row was already `Not met`:

```
errors: 0 | not_met= 4 | new_findings= 0
| 2026-08-11 | 939363f | 4 | 0 | 0 | 0 | 0 | 0 | NOT READY |
- New findings vs prior: 0
```

[Observed] §6: *"A **new** scoped finding is a **new finding** … so rendering a defect scoped never zeroes the delta column."* The column is zeroed here by a different route, and the tool that computes it reports no error. Note the asymmetry the repair created: evidence paths and deferral paths are now resolved at the named commit (f8, f4/f5 repairs); the prior-record path — the only path whose content is *read and arithmetic performed on* — is not.

### f7 — MATERIAL. With `git` unavailable, a wholly forged record validates clean and the generated report carries no trace of it

Disclosed limit 3 covers the first half. What is undisclosed is that (a) eligibility does not consider it, and (b) the *report* — the artifact stored in the canonical result home — is unchanged and unmarked, so `--check` misdiagnoses the difference.

**Attack run.** Stub `git` on `PATH` returning exit 128. Record: nonexistent commit `d…d`, forged instrument and parameter-block digests, `instrument.version: v9.9`, all six waves declared required and none deferred, invented `e4.routing_authority`, all six E4 `case_text`s replaced with *"I paraphrased this case"*, and all 43 evidence entries citing `NO/SUCH/FILE-INVENTED.md`.

```
git present :  40 validation errors
git broken  :  note: LA-2: git unavailable — …
               Row/formula outcome: READY FOR Capability 1 — …
               Formal gate result:  READY FOR Capability 1 — …
               | 2026-08-11 | ddddddd | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | READY FOR … |
               record valid — the verdict above is computed from the rows      (exit 0)
```

The rendered report's only occurrence of the string "git" is `Canonical source:` — the note goes to stdout and never into the file. [Observed]

The `--check` consequence, demonstrated on the f1 record: rendering it on a git-capable machine and a git-less machine produces **different digests** (`bdd4c22a…` vs `e7ae91fe…`) — the `THIS RECORD DOES NOT VALIDATE` stamp appears only on the former — and `--check` reports the difference as *"the report has been edited, or the record changed without regenerating"*, which is false in both directions.

### f8 — MINOR. `LA-3b` is a check the tool runs that §5 does not name — a finding by §5's own construction

§5, quoted (amended at v2.1, D-5):

> **The enumeration below is this instrument's**; the tool implements it, and **a check the tool runs that this list does not name is a finding against the tool.**

**Sweep, both directions, with denominators.** Regex extraction of every `LA-…` identifier emitted from `validate()`: **17 distinct** — `LA-1, LA-2, LA-3, LA-3b, LA-4 … LA-16`. §5's enumeration is a 16-clause list introduced as `(LA-1 … LA-16)`.

- *Tool runs, §5 does not name*: **1 of 17 — `LA-3b`.** §5's third clause is *"the launch-target and wave binding"*; the E4 routing authority is neither, and no `LA-3b` lies in the range `LA-1 … LA-16`. The string `LA-3b` does not occur anywhere in the instrument.
- *§5 names, tool does not run*: **0 of 16.** Each of the 16 clauses maps onto an emitted identifier. Two are implemented more narrowly than their words — clause 11, *"deferral citation (a made decision, never a queue entry)"* (see f5), and clause 15, *"prior-record anchoring"* (see f6) — but neither is absent.

Also unenforced from §4: the `READY-WITH-DEFERRALS` predicate ends *"AND the citation resolves"*, but `_compute` selects the branch from `len(f2_deferrals)` alone and never consults whether LA-11 accepted the citation. Demonstrated at f7's `.beads/issues.jsonl` probe: `errors=1`, `verdict=READY-WITH-DEFERRALS`.

### f9 — MINOR. RD-47 finding 9 stands unrepaired verbatim, and the delta's replacement figure is itself stale

`scripts/validate_launch_administration.py:502`, unchanged:

> `This is the one place the validator reads the instrument's own prose,`

RD-47 f9: *"There are 5 such functions and 7 regex sites."* The delta neither lists f9 in its repair table nor claims it, and instead writes in disclosed limit 4: *"The validator reads the instrument's own prose in **five** places."* That figure is now wrong too: v2.1's own LA-3b repair added a sixth, `_param_path` (`:483–496`). The current population is `param_block_bytes`, `instrument_version`, `launch_target_forms`, `_yaml_list`, `_param_path`, `e4_cases` = **6** (12 `re.*` call sites in the file overall). A denominator quoted outside its owning artifact went stale inside the same commit that changed it — the repo's rule 3 and the pass's own D-7 lesson.

### f10 — MINOR. RD-47 finding 10 unrepaired and undisclosed

`--allow-invalid` on a record missing a required field still ends in an unhandled traceback, at the same site:

```
File "…/render_launch_administration.py", line 319, in render
    a(_quoted(rec["g1"]["critic_answer"]))
KeyError: 'g1'
```

Same path, on a record with a duplicate key, now raises an uncaught `ValueError` out of `_no_duplicate_keys` — a new instance of the same class introduced by the f12 repair. `validate()` returns `computed = {}` on any schema error and `render()` indexes it unconditionally (`computed['not_met']`, `computed['conjuncts']`), so the documented inspection path does not work for the commonest invalid record. This finding appears in neither the delta's repair table nor its disclosed limits. [Observed]

### f11 — MINOR. `question_digest` in its sha256 form binds nothing

Schema: *"sha256 of the question's verbatim text as administered, or the literal `instrument-bound` …"*. §2: *"a verdict rendered against a paraphrased question is void."* No check computes or compares it — a record setting `question_digest: "c"*64` on all 43 rows validates with 0 errors and computes `READY FOR`. The `instrument-bound` form is genuinely covered by LA-2; the hex form is a transcribed digest wearing the appearance of a scripted one, which is precisely the failure repo rule 3 names. Either compute it or drop the alternative.

### f12 — MINOR. Newline-bearing scalars survive validation and split the generated §6 row and the report's terminal verdict line

LA-3 compares the launch target **whitespace-normalized** (`_norm_ws`), and the renderer emits it raw. A `launch_target` differing from §8 only by an embedded newline validates with 0 errors and yields:

```
| 2026-08-11 | 939363f | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | READY FOR Capability 1 — Project
registration and honest shape visibility |
…
GATE VERDICT: READY FOR Capability 1 — Project
registration and honest shape visibility
```

`trend_row` sanitizes `|` (`col.replace("|", "/")`) but not `\n`, and does not use `_cell`, which handles both. The same applies to `date`: **sweep, 10 patterns in the schema, all 10 anchored `^…$`, and all 10 accept a trailing newline** under Python `re.search` (`$` matches before a final `\n`) — so `"date": "2026-08-11\n"` validates and produces `| 2026-08-11\n | 939363f | …`. The `jsonschema` reference behaves the same, so this is not a subset-interpreter divergence; it is a gap between what the pattern is read as promising and what it enforces.

### f13 — MINOR. The placeholder lexicon is defeated by one invisible character, and `counterexample` accepts whitespace

`falsification_attempt: "none​"` (zero-width space) validates clean: `str.split()` does not split on ZWSP and `_is_placeholder`'s `strip` set does not remove it, so the token misses the lexicon. `"none "` (NBSP) *is* caught, since `split()` treats NBSP as whitespace — an inconsistency worth knowing. Separately, and beyond disclosed limit 8: `counterexample: " "` satisfies `minLength: 1` and LA-6's `not row["counterexample"]`, so a `Not met` row can carry a single space as its counterexample. §2: *"Not met requires a concrete counterexample."*

---

## B. New attacks — coverage summary

Every surface the commission named was exercised. Eligibility and its four consumers (CLI, `--trend-row`, renderer, `--allow-invalid`): f1. Deferral citations: f5, plus 20-file denominator sweep. Evidence paths: repaired, verified. E4 fixed cases: `case_index` duplication/zero/out-of-range all caught by the `sorted(idx) != range(1, n+1)` test; paraphrase caught; the "disagree → `silent` + `needed_by_launch_target: false`" laundering passes with 0 errors, matching disclosed limit 6 exactly. Wave binding: repaired (f4 for its fixture). `question_digest`: f11. G1: the lexicon catches `"none"`, `"n/a"`, `"tbd"`, `"None."`; misses `"no gaps"`, `"Nothing of consequence was identified"` and f13's ZWSP. Duplicate keys: fully closed, including `\u`-escaped and nested. Unicode/escape: f12, f13. Git-unavailable: f7.

## C. Schema closure — answered above under f3

18 object nodes, 18 closed, by two methods; deletion detected at 18/18 on mutated copies; residual hole is the unbound `--schema` path.

## E. Fixture quality — answered above under f4

13 new validator fixtures, 4 new renderer fixtures; 12 reverted repairs; 10 discriminate, 2 do not, both belonging to RD-47 finding 1.

## F. Determinism and safety

Within a fixed environment the renderer is deterministic: 8 renders of one record (5 plain, 3 under `PYTHONHASHSEED=0/1/12345`) produce **1 distinct digest**; `--check` exits 0 against a fresh render and 1 against an edit. No clock, locale, `set`-iteration or dict-order dependence in the render path, and nothing in the correctness path parses generated Markdown.

But the answer to the question as asked is **no**: the output is not a pure function of the record plus the repository at the named commit. It is additionally a function of whether `git` is invocable on the rendering machine (f7), which changes the presence of the `THIS RECORD DOES NOT VALIDATE` banner, and `--check` reports the resulting byte difference as an edit. And there are three paths on which a report misrepresents its record: f2 (forged verdict and figures above the real ones, no flag needed), f1 (`GATE VERDICT: READY FOR …` on a record that does not validate), and f7 (a wholly unverified report that says nothing about it).

---

## What I did not test, and why

- **Whether reviewer-declared judgement fields are true** — `blocking_conditions_met`, `needed_by_launch_target`, `routing_authority_says`, `fresh_context`, `same_family_as_corpus_authors`, every evidence quote. Content-blind by design and documented as such; I tested the mechanics around them only. [Unknown]
- **Whether the administration packet digest-binds the schema file.** f3 makes that binding load-bearing, and it lives outside the three subject files. [Unknown]
- **The instrument's own soundness** — whether §4's conjunct set is right, whether `Unknown` across 22 A–D rows should pass. I tested code against instrument.
- **Behaviour under a genuinely absent `git` binary** (`OSError` path) as opposed to a `git` returning nonzero. Both funnel through `_git_available() → False`; I exercised the latter. [Inferred] that they are equivalent.

## Summary

The repair pass is real work and most of it holds: seven of RD-47's twelve findings are cleanly closed and I could not reopen them. What stops this from being a confirm is that the three most consequential repairs are each *narrower than the claim made for them* — f2 was fixed at the two fields the reviewer named rather than for the class the delta describes; f4/f5 was fixed to a three-file denylist rather than to "a made owner decision"; f6 was fixed against keyword deletion rather than against an unbound schema — and that the eligibility separation D-3 calls its central strengthening implements three of the four limbs §4 states, so an invalid record still writes `READY FOR …` into the trend log and into the report's last line. Alongside that, the pass's own fixture claim ("one per repaired predicate") is refuted by its own selftest, for the finding whose attack is the most direct route to a false pass.

f1, f2 and f4 all bear on artifacts §5 puts in front of the owner or §6 says F1 is answered from and only from. None is deep; each is a few lines. But they are the same lines the last review already bought once.

Findings: 2 BLOCKING, 5 MATERIAL, 6 MINOR.

VERDICT: REVISE
