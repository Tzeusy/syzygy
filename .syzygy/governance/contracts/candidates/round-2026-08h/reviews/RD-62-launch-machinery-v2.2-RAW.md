# RD-62 — raw reviewer output, launch-gate machinery at v2.2

> **Provenance banner. Everything below the rule is the reviewer's raw
> output, copied verbatim and unedited** — including any error it contains.
> Corrections live in the disposition register, never here.
>
> | | |
> |---|---|
> | Review ID | RD-62 |
> | Role | Schema, validator and renderer reviewer — the machinery repair RD-56 asked for |
> | Dispatched | 2026-08-16 |
> | Subject commit | `918574c` (frozen worktree) |
> | Subject digests | schema `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` · validator `dbb8b69097df15a4bf60cc6fc0cef1043b838a22d30920f1914da31a91322977` · renderer `4ffa3c9ec83aad7951884be159eec81dde8374387fc45c4d7a6ba9b323a08e61` · instrument v2.2 `ac8751236ec7434c20606b404d41c885d29f67dd5f3dab8c9d0cbb90de670977` |
> | Context | Fresh — no prior contact with this repository's review history beyond the commission's two named context files |
> | Model family | **Same as the corpus's authors.** This review therefore supports **repair** and is **never** the formal launch administration (instrument §2, F5) |
> | Other reviews | Dispatched with no knowledge of any other review running today; none was sought, none was read |
> | Verdict | `REVISE` — copied exactly |

All four subject digests were verified against the commission before any
other work and re-verified at the end of the session; all four match, and
`git status --porcelain` in the frozen worktree is empty. No file in the
frozen worktree was written. Every probe lives under
`scratchpad/rd62-scratch/`.

`--selftest`, run from the frozen worktree: **validator 101 fixtures / 0
failing / 0 skipped; renderer 31 fixtures / 0 failing.** The `jsonschema`
second-method cross-check ran and passed.

Method: a probe harness built on the tools' own `_base_record(git_bound=True)`
bound to the instrument at `918574c`; a copy of the frozen tree at
`scratchpad/rd62-scratch/tree` for anything needing a writable repository; a
stub `git` returning exit 128 on `PATH` for the degradation path; **49
single-predicate reversions applied to copies of the scripts**, each running
both selftests, to measure fixture discrimination; `markdown_py` and `pandoc`
as independent Markdown readers.

---

## Findings

| # | Severity | Finding |
|---|---|---|
| f1 | **BLOCKING** | `_cell` and `_quoted` neutralize `\n` but not `\r`, so RD-47 f2 / RD-56 f2's forgery reproduces **verbatim** — two forged `GATE VERDICT: READY FOR …` lines and two forged `## Computed figures` sections above the real ones, in the report of a record that validates clean and needs no `--allow-invalid` |
| f2 | MATERIAL | `--prior` launders the §6 New-findings column from a file anywhere on the filesystem — RD-56 f6's exact attack through the sibling path the repair did not touch |
| f3 | MATERIAL | The declared `prior_record` identity does not control the file that is read: the commit-equality check `--prior` gets is not applied to `prior_record.path`, and that path need not be committed, tracked, or the record its own fields name |
| f4 | MATERIAL | The RD-56 f6 repair reintroduces RD-47 f3's false absence: an escaping prior path collapses to the "no prior declared" outcome, and the report asserts the record "declares no prior — it opens the log" about a record that declares one |
| f5 | MATERIAL | The schema is the one identity in the record's chain that is neither digest-bound nor resolved at `repository_commit`. RD-56 f3's repair compares `--schema` **paths**, not bytes; a drifted working-tree schema admits a record carrying `final_verdict: "READY FOR everything"`, which validates clean, is eligible, and prints `READY FOR …` as the formal gate result |
| f6 | MATERIAL | `record valid — the verdict above is computed from the rows` and **exit 0** for a record the tool has, three lines earlier, declared not fully validated |
| f7 | MATERIAL | The blocking repair's third eligibility limb has **no discriminating fixture**, and four other predicates have none. 49 reversions, 7 undetected, 5 of them live predicates. The delta's "each was verified to fail with its repair reverted" is refuted for the limb that matters most |
| f8 | MINOR | The false-witness fixture RD-56 f4 named is still in the suite, still green, and still passes against a validator with the fail-open restored |
| f9 | MINOR | `_sdr_exists` still excludes only `PENDING-OWNER-DECISIONS.md`; the comment "One list, both branches" states a property the code does not have. 33 SDR ids swept, 0 currently exploitable — latent, not live |
| f10 | MINOR | Placeholder coverage is 6 of 43 free-text sites. `counterexample` is tested for falsiness, never for placeholders, so `"none"` is a lawful counterexample — beyond disclosed limit 7, which discloses only `" "`. `falsification_summary` is unchecked and renders as the record's own answer |
| f11 | MINOR | Every schema `pattern` remains `^…$` under `re.search`, so trailing newlines still validate. The observable harm RD-56 f12 named is closed; the residual shows in the report heading as `2026-08-11 ,` |
| f12 | MINOR | The invisible-character repair is an **enumeration of five code points** — the shape the `_NON_WARRANT_FILES` repair in the same pass moved away from. 4 of 6 invisibles I tested still defeat the lexicon |
| f13 | MINOR | `--check` on a git-less machine against a git-capable render still reports "the report has been edited, or the record changed without regenerating". RD-56 f7's first half is closed; this half is not |

**2 BLOCKING, 5 MATERIAL, 6 MINOR at RD-56 → 1 BLOCKING, 6 MATERIAL, 6 MINOR
here.** The count is not the point; three of the six MATERIALs are the same
two repairs narrowed a second time.

---

### f1 — BLOCKING. Free text is data for `\n` and structure for `\r`

The delta states the repair as a class property, and the renderer's own
docstring restates it:

> Every Markdown block construct (heading, fence, table row, list item,
> thematic break) must START a line. Reviewer text emitted inline is
> therefore neutralized by removing its ability to start one: newlines
> collapse to spaces.

**Sweep with denominator.** Mechanical extraction of every `a(…)` statement
in `render()`: **151 statements. 107 are pure literals. 8 interpolate record
or computed data with no sanitizer — and all 8 are booleans, integers or
`len()` counts, so RD-56 f2's 19 raw free-text sites are genuinely closed.
The remaining 36 route through a sanitizer: 29 through `_inline`, 5 through
`_cell`, 2 through `_quoted`.** Then, mechanically, what each sanitizer
neutralizes:

```text
_quoted   handles CR=False  LF=True   pipe=False
_cell     handles CR=False  LF=True   pipe=True
_inline   handles CR=True   LF=True   pipe=False
trend_row.cell            CR=True   LF=True   pipe=True
```

`_inline` and `trend_row.cell` were taught about `\r` in this pass.
`_cell` and `_quoted` were not — and between them they carry
`unknown_reason`, `counterexample`, `unknown_settlement`, every evidence
`path`/`locator`/`quote`, all three E3 `trace_rows` strings, `e4.case_text`,
every row's `falsification_attempt`, `falsification_summary` and
`g1.critic_answer`. That is the majority of the reviewer's substantive prose.

**Attack run.** RD-47's own forgery, CR-separated instead of LF-separated,
placed in `falsification_summary` (a `_quoted` site) and in
`question_results[0].falsification_attempt` (a `_cell` site), on a record
with `E5 = Not met` that computes `NOT READY`:

```
$ python3 scripts/validate_launch_administration.py CR_forge.json | tail -1
record valid — the verdict above is computed from the rows

$ python3 scripts/render_launch_administration.py CR_forge.json -o CR_forge.md
wrote CR_forge.md (8767 bytes) — generated from CR_forge.json
```

Zero errors. No `--allow-invalid`. The stored artifact's physical lines
132–150:

```text
132 ''
133 '> plausible'
134 ''
135 '## Computed figures'
136 ''
137 '- Not met (plain): 0'
138 ''
139 'GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility'
140 ''
141 '| Q | What was tried |'
142 '|---|----------------|'
143 '| A1 | plausible'
144 ''
145 '## Computed figures'
146 ''
147 '- Not met (plain): 0'
148 ''
149 'GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility |'
150 '| A2 | tried to find a contradicting artifact |'
```

The real ones are at 197/201/225 and read `- Not met (plain): 1` and
`GATE VERDICT: NOT READY`. [Observed]

**Rendered, by an independent reader.** `markdown_py` (Python-Markdown,
installed on this machine) on the same file:

```html
<h2>Falsification</h2>
<h2>Computed figures</h2>        <- forged
<p>GATE VERDICT: READY FOR Capability 1 — …
<h2>Computed figures</h2>        <- forged
<p>GATE VERDICT: READY FOR Capability 1 — … |
<h2>G1 — completeness critic</h2>
<h2>Computed figures</h2>        <- real
<p>GATE VERDICT: NOT READY
```

Three `<h2>Computed figures</h2>`; two forged `GATE VERDICT: READY FOR …`
paragraphs at document level, **above** the real one. [Observed]

**The renderer dependence, stated honestly.** `pandoc -f commonmark` and
`pandoc -f gfm` discard a bare `\r` and produce no injection — I ran both on
a minimal case and on the full report. `markdown_py` injects. The CommonMark
specification §2.1 defines a line ending as "a newline (U+000A), **a carriage
return (U+000D) not followed by a newline**, or a carriage return and a
following newline", so a spec-conforming reader — which is what `cmark-gfm`,
and therefore a git host's rendering, is — is [Inferred] to split. Pandoc's
reader deviates from the spec here.

I rate this BLOCKING rather than MATERIAL for three reasons that do not
depend on which renderer the owner happens to use:

1. **The repair's own acceptance criterion fails.** The renderer's fixtures
   assert the class property with
   `not any(ln.startswith("GATE VERDICT: READY") for ln in fout.split("\n"))`
   and `[ln for ln in outF.splitlines() if …]`. Python's `splitlines()`
   splits on `\r`. Run against the CR forgery, the fixture's own predicate
   is violated — the suite passes only because every fixture's `FORGERY`
   constant is spelled with `\n`.
2. **It is a plain drift path, not a hostile one.** CRLF-authored JSON is
   what a reviewer working on Windows, or pasting from a Windows editor,
   produces by default. `_cell` turns `"a\r\nb"` into `"a\r b"` — the `\r`
   survives mid-cell in ordinary use.
3. It is the third pass at the same defect, and the fix is one
   `.replace("\r", " ")` in each of two functions — the same edit already
   made in `_inline` and `trend_row.cell` ten lines away.

### f2 — MATERIAL. `--prior` launders the §6 New-findings column from outside the repository

RD-56 f6's repair resolves `rec["prior_record"]["path"]` against `REPO` and
errors when it escapes. `_compute` reads:

```python
new_findings = None
src = prior_path                       # <- the CLI flag, unconditioned
if src is None and rec.get("prior_record"):
    cand = (REPO / rec["prior_record"]["path"]).resolve()
    ...containment check...
```

`prior_path` is `--prior`. It takes **precedence** over the resolved
declared path, and nothing resolves, contains, or commits it. LA-15's only
guard is that the supplied file's `repository_commit` equals the record's
declared `prior_record.repository_commit` — a value the same author writes.

**Attack run.** A record with four genuinely new `Not met` rows (A1, A2, B3,
C5), `prior_record.repository_commit` set to a real ancestor of `918574c`,
and a five-line hand-written JSON at `/tmp/forged-prior-outside.json`
asserting every roster row was already `Not met`:

```
$ python3 scripts/validate_launch_administration.py A_newfindings.json --trend-row
| 2026-08-11 | 918574c | 4 | 0 | 0 | 0 | 0 | unknown  | NOT READY |

$ python3 scripts/validate_launch_administration.py A_newfindings.json \
      --prior /tmp/forged-prior-outside.json --trend-row
| 2026-08-11 | 918574c | 4 | 0 | 0 | 0 | 0 | 0        | NOT READY |
record valid — the verdict above is computed from the rows        (exit 0)
```

[Observed] Zero errors, `record valid`, exit 0, four new findings reported as
zero. §6: *"The row is generated, not transcribed: `--trend-row` prints it
from the source record"* — this is the string that gets appended to the log
§6 says *"F1 — which is answered from this log and only from it."*

The comment above the repair reads *"`--prior`, when given, still overrides
for inspection"*, which is a description of the hole rather than a
justification for it: the flag that overrides is the one with no
containment, and it feeds the same generated row.

### f3 — MATERIAL. The declared `prior_record` identity does not control the file that is read

LA-15 anchors `prior_record.repository_commit` (must exist, must be an
ancestor) and `prior_record.date` (must not follow). The file at
`prior_record.path` is then read and arithmetic performed on it, and it is
checked for exactly one thing: that it resolves inside the repository. It is
never checked to exist at any commit, to be tracked, or to be the record
those two anchored fields identify.

The `--prior` branch **does** carry that check:

```python
if pj is not None and pj.get("repository_commit") != prior["repository_commit"]:
    errors.append("LA-15: --prior names commit … but the record's prior_record names …")
```

The declared path — the documented path, the one the renderer uses — does
not.

**Attack run.** The same four-new-findings record, `prior_record` naming a
real ancestor commit and `2026-08-01`; the file at the declared path is an
**uncommitted** JSON inside the working tree whose own
`repository_commit` is `deadbeef…` and whose own date is `1999-01-01`:

```
| 2026-08-11 | 918574c | 4 | 0 | 0 | 0 | 0 | 0 | NOT READY |
record valid — the verdict above is computed from the rows
```

[Observed] Zero errors. The two halves of "the prior record" — the identity
LA-15 anchors and the bytes `_compute` reads — are disjoint and wear one
name. Every other path in the record was moved to commit resolution by the
v2.1/v2.2 repairs (evidence paths, deferral paths, the instrument); this one
was moved only as far as the working tree.

### f4 — MATERIAL. The f6 repair reintroduces RD-47 f3's false absence

The repair's own comment, three lines above it:

```python
#   an integer   the comparison ran
#   None         no prior is declared — this record opens the log
#   "unknown"    a prior IS declared and could not be read
```

and then:

```python
src = str(cand) if inside else None
```

An escaping path is precisely "a prior IS declared and could not be read",
and it is assigned the value that means "no prior is declared".

**Attack run.** `prior_record.path: "../../../../tmp/forged-prior-outside.json"`,
four genuinely new `Not met` rows:

```
1 validation error(s):
  LA-15: the prior record's path '…' resolves outside the repository …

Trend row (§6):
| 2026-08-11 | 918574c | 4 | 0 | 0 | 0 | 0 | n/a (no prior record) | NONE — not eligible; … |

$ grep "New findings vs prior" escape_prior.md
- New findings vs prior: n/a (this record declares no prior — it opens the log)
```

[Observed] The record declares a prior. The report states, in a full
sentence, that it does not. That is RD-47 f3's defect verbatim — a false
claim of absence, VIS-2 — reintroduced by the repair for RD-56 f6, in the
one column §6 says F1 is answered from. §4 is explicit that eligibility does
not blank the counting columns: *"§6's counting columns are unaffected — a
diagnostic administration's findings are findings."*

`_new_findings_cell` already has the correct string for this case; the
repair simply routes past it. `src = None` should be a third state.

### f5 — MATERIAL. The schema is not digest-bound to the named commit

RD-56 f3's repair is reasoned in the source as:

```python
# … a record validated against anything other than the committed schema is
# an INVALID record, and therefore — via §4's fourth eligibility limb — an
# ineligible one.
if Path(schema_path).resolve() != Path(DEFAULT_SCHEMA).resolve():
```

That compares **paths**. §5 says the schema is *"committed beside this
instrument and digest-bound in the administration packet"* — and I confirmed
the digest `e0167fb8…` is stated in `FORMAL-CAPABILITY-1-LAUNCH-PACKET/README.md`
and `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md`. Nothing
in the three subject files reads that digest, and `scripts/check_governance.py`
does not mention the schema file at all (`grep` returned nothing).

The instrument is digest-checked against `git show <repository_commit>:…`.
The schema is read with `Path(schema_path).read_text()` from the working
tree. So for any record whose `repository_commit` is not the checkout's
HEAD — which is the ordinary case for re-validating a past administration —
the tool validates against a schema that is not the one at the named commit,
and says nothing.

**Attack run.** In a copy of the tree, the working-tree schema is edited to
add a closed, implemented-keyword-only `final_verdict` property (digest
`81cefece…`, not the `e0167fb8…` the packet seals). A record carries
`final_verdict: "READY FOR everything"`:

```
$ python3 scripts/validate_launch_administration.py schema_drift.json --trend-row
| 2026-08-11 | 918574c | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | READY FOR Capability 1 — … |
record valid — the verdict above is computed from the rows

# same record, frozen committed schema:
  LA-1: $: unknown field 'final_verdict' — the verdict is computed, never claimed
```

[Observed] The keyword audit and the closure audit both pass on the drifted
schema, because the drift is well-formed. The fix is the one the tool
already applies to the instrument: `hashlib.sha256(_git_show(commit,
"launch-gate-administration.schema.json"))` compared against the bytes
actually used.

Schema closure itself is sound and I could not reopen it. **Sweep with
denominator, three methods:** 111 nodes walked, 18 declaring `properties`,
18 declaring `additionalProperties: false`; a literal text count of
`"additionalProperties": false` is 18 and of `"type": "object"` is 18;
deleting `additionalProperties` at each of the 18 in turn fires the audit
**18/18**. The root-`properties` audit fires on `{"type": "object"}`, and the
unsupported-keyword audit fires on `propertyNames`.

### f6 — MATERIAL. `record valid` and exit 0 for a record the tool has just said is not validated

RD-56 f7 is repaired where it was aimed — the eligibility fifth limb exists,
the trend row carries `NONE`, the report body carries `**UNVERIFIED:**`.
What was not repaired is the terminal's last line and the process's exit
status.

**Attack run.** Stub `git` on `PATH` returning exit 128. Record: nonexistent
commit `d…d`, forged instrument and parameter-block digests,
`instrument.version: v9.9`, `required_waves: ["Z"]`, invented
`e4.routing_authority`, every E4 `case_text` replaced with *"I paraphrased
this case"*, and all 39 evidence entries citing `NO/SUCH/FILE.md`:

```
note: LA-2: git unavailable — identity, binding, E4 case text and deferral-citation
      existence were NOT verified; this record is not fully validated
Row/formula outcome: READY FOR Capability 1 — Project registration and honest shape visibility
Formal gate result:  NONE — diagnostic only (git was unavailable, …)
| 2026-08-11 | ddddddd | 0 | 0 | 0 | 0 | 0 | n/a (no prior record) | NONE — not eligible; row outcome was READY FOR … |

record valid — the verdict above is computed from the rows
$ echo $?
0
```

[Observed] The gate lines are correct. The **last line printed** asserts the
record is valid, and the **exit status** — the thing a CI job, a `&&` chain
or a script reads — is success, for a record the tool's own note three lines
earlier says *"is not fully validated"*. The renderer likewise exits 0 and
writes the report without refusing.

"Valid" here means "no errors were raised", and no errors were raised
because the checks did not run. That is VIS-2's own sentence: no evidence
yields Unknown, never green. The record is ineligible on the fifth limb, so
the fix is available at zero cost — the same limb that already reaches the
row and the report should reach the summary line and the return code.

### f7 — MATERIAL. Fixture discrimination: 49 reversions, 7 undetected, and one of them is the blocking repair's third limb

The delta:

> Each repair above has at least one fixture; each was verified to fail with
> its repair reverted, by mutating a copy of the script — the discipline
> RD-56 f4 showed had been claimed rather than performed.

**Method, with denominator.** 49 single-predicate reversions applied to
copies of the two scripts, one at a time, each running both selftests to
completion and reading the printed failure count (never the exit code). 20
reversions targeted the v2.2 repairs; 29 targeted individual `LA-*`
predicates.

Repair reversions (20):

| reverted repair | validate fails | render fails |
|---|---|---|
| eligibility limb: `formal` | 1 | 0 |
| eligibility limb: `administration_kind` | 1 | 0 |
| **eligibility limb: `fresh_context`** | **0** | **0** |
| eligibility limb: zero errors | 1 | 1 |
| eligibility limb: git ran | 1 | 0 |
| f3a `--schema` path check | 1 | 0 |
| f3b root-`properties` audit | 1 | 0 |
| f5 non-warrant classification | 5 | 0 |
| f5b self-declared-pending shape rule | 1 | 0 |
| **f6 prior-path containment (behaviour half)** | **0** | **0** |
| f8 F2 citation resolves | 1 | 0 |
| f12 trend-row cell sanitizer | 0 | 2 |
| f13 invisible-char stripping | 2 | 0 |
| RD-47 f1 `_yaml_list` fail-open | 1 | 0 |
| RD-47 f1b `instrument_version` fail-open | 1 | 0 |
| f2 `_inline` flattening | 0 | 6 |
| f2b `_quoted` blockquoting | 0 | 5 |
| f7 `**UNVERIFIED:**` note | 0 | 1 |
| f10 unrenderable guard | 0 | 1 |
| f1 renderer eligibility branch | 0 | 2 |

Predicate reversions (29): 24 detected. Undetected: `_is_ancestor` (LA-15),
`--prior` commit equality (LA-15), the E4 `case_index` run (LA-10), the
LA-4 extra-row branch, and LA-12's plain-READY-over-deferrals branch.

**Combined: 49 reverted, 7 undetected.** Two of the seven are dead code and
are not defects — I checked both rather than assuming:

- LA-4's extra-row branch is unreachable. The `question_id` pattern's
  alternation enumerates to **39 identifiers; `ROSTER_SET` has 39; the
  difference is empty.** The fixture that names this branch says so in a
  comment.
- LA-12's `branch == "plain" and n_deferred` is unreachable: `branch` is
  `"plain"` only when `n_deferred == 0`.

The five live ones:

1. **`fresh_context`, the third limb of the blocking repair.** Deleting it
   entirely leaves 101/101 and 31/31 green. The fixture that names fresh
   context (`LA-13 a formal administration without fresh context is an
   error`) asserts the LA-13 *error string*; the record is then ineligible
   through the *fourth* limb (error count), so the third limb is masked and
   the suite cannot tell whether it exists. This is precisely RD-56 f4's
   failure mode — a fixture that passes for the wrong reason — recurring on
   the repair the delta calls its blocking one. A discriminating fixture is
   three lines, in the exact shape the fourth and fifth limbs already use:
   `_compute(rec, rows, None, git_ok=True)` with `formal=True, kind="full",
   fresh_context=False`, asserting `not eligible`.
2. **`_is_ancestor`.** Making it return `True` unconditionally is
   undetected. The fixture named `LA-15 a prior commit outside this history
   is a stale prior` sets the prior commit to `"f"*40`, which does not
   exist, so the `elif` short-circuits at the *existence* branch and the
   ancestry branch is never entered. The fixture's name claims the predicate
   it does not reach.
3. **`--prior` commit equality.** The only guard on the flag in f2 has no
   fixture at all.
4. **The E4 `case_index` run.** `sorted(idx) != list(range(1, len(idx)+1))`
   is undetected. The fixture that gets near it pops the last result, which
   the *count* check catches first. Without the run check a record can
   answer case 1 twice and case 2 never, at the right count.
5. (LA-4/LA-12 above, dead.)

Against RD-56's own figure — 10 of 12 discriminating — this is 42 of 49.
The direction is right. What is not right is that the exception is the same
class of exception, on the repair the pass exists for.

### f8 — MINOR. The false witness RD-56 f4 named is still in the suite, still green

`scripts/validate_launch_administration.py:1505–1507`, unchanged:

```python
case("LA-3 an unreadable REQUIRED_WAVES is an error, not a skip",
     lambda r: r.update(required_waves=["A", "B", "C1", "D1"]),
     "LA-3", git=True)
```

v2.2 added the correct instrument-mutating fixture beside it and left this
one in place. Restoring the `_yaml_list` fail-open on a copy:

```
  pass  LA-3 an unreadable REQUIRED_WAVES is an error, not a skip
  FAIL  an UNREADABLE §8 parameter is an error, not a skipped check (instrument mutated, not the record)
101 fixtures, 1 failing
```

[Observed] The predicate is now genuinely covered — that is the repair, and
it holds. But a green line whose name asserts a property it does not test is
the thing RD-56 f4 was about, and it is still printed on every run.

### f9 — MINOR. "One list, both branches" is still not true

The comment above `_NON_WARRANT_FILES`:

> `_sdr_exists` already excluded the queue for `SDR-n` citations, and the
> path branch did not — so the same file granted nothing by identifier and
> everything by path (review RD-47 finding 4). **One list, both branches.**

`_sdr_exists` still hardcodes an exclude pathspec for
`PENDING-OWNER-DECISIONS.md` alone, and does not consult
`_NON_WARRANT_FILES`, `_PACKET_NAME` or `_PENDING_SELF_DECLARATION`. So an
`SDR-n` occurring **only** in `TREND-LOG.md`, `HISTORY.md`, a `README.md`,
`PROCESS-LESSONS.md` or a decision packet is accepted by the identifier
branch and would be refused by the path branch.

**Sweep with denominator.** All 22 files in the decisions home at `918574c`,
33 distinct `SDR-n` identifiers, each classified by whether any *warrantable*
file contains it: **0 of 33 are currently in the exploitable position.** No
live exploit; the comment states a property the code does not have, and the
gap is filled by whichever file is added next.

RD-56 f5's substance **is** closed. Re-running its 20-file sweep at
`918574c` (now 22 files): **8 refused, 14 accepted**, against RD-56's 4/16.
All three files RD-56 named are now refused —
`LICENSE-DECISION-PACKET.md` ("is a decision *packet*"),
`launch-gate/TREND-LOG.md` and `launch-gate/HISTORY.md` ("an index, a queue
or a log") — and the two refusals RD-56 said carried the wrong reason
(`PROCESS-LESSONS.md`, `launch-gate/README.md`) now carry an accurate one.
The shape predicate independently refuses
`DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md` on its self-declared status. Of
the 14 accepted, I swept for unruled language (`remains pending|open`,
`owner has not ruled|decided`, `binds nothing`, `does not choose|decide`) and
found 1 hit across 8 spot-checked files; disclosed limit 9 covers that
residual explicitly and correctly.

### f10 — MINOR. Placeholder coverage is 6 of 43, and `counterexample` is the one that shows

The validator's docstring:

> Every free-text field this tool relies on is checked against a placeholder
> lexicon.

**Sweep with denominator.** The schema declares **43** string sites with
`minLength` — i.e. 43 free-text fields. `_is_placeholder` is called at 5
sites covering **6** of them: `unknown_reason`, `unknown_settlement`,
`falsification_attempt`, `owner_deferrals[].bounded_reduction_plan`,
`g1.critic_answer`, `pilot_recurrence_check.method`.

Two of the 37 uncovered are fields the tool *does* rely on and *does* render
as the record's own answer:

- **`counterexample`.** LA-6 tests `not row["counterexample"]` — falsiness,
  not the lexicon, in the same function where every other presence test uses
  the lexicon. So a scoped row can read
  `Not met (out of launch scope)` with `counterexample: "none"`, and it
  validates clean. Disclosed limit 7 discloses only that `" "` satisfies
  `minLength`; a literal placeholder *word* is a wider hole than the one
  disclosed. §4 makes that cell the scoped form's honesty: *"the disclosure
  is the scoped form's honesty, so it is checked, not trusted."*
- **`falsification_summary`.** `"none"` validates clean and renders under
  `## Falsification` as `> none`. §2 makes a genuine falsification attempt a
  requirement of the administration; the per-row field is checked and the
  record-level summary is not.

```
$ python3 scripts/validate_launch_administration.py ce_word.json | tail -1
record valid — the verdict above is computed from the rows
$ python3 scripts/validate_launch_administration.py fs_none.json | tail -1
record valid — the verdict above is computed from the rows
```

[Observed]

### f11 — MINOR. The `$`-anchor residual, closed in effect

RD-56 f12's second half — every schema `pattern` is `^…$` under
`re.search`, so a trailing newline validates — is unrepaired and undisclosed,
but the harm it produced is closed by `trend_row.cell`. `"date":
"2026-08-11\n"` still validates with zero errors; the §6 row no longer
splits, and the residual surfaces only as a cosmetic artifact in the report
heading:

```
# Launch-gate administration — 2026-08-11 , commit `918574c`
```

[Observed] I swept the other newline-admitting scalars (`repository_commit`,
`instrument.sha256`, `parameter_block_sha256`, `question_id`) and each
produces a validation error downstream rather than a false pass. Recorded
because the delta's f12 row describes the repair as "Every cell is
sanitized" without noting that the pattern half stands.

### f12 — MINOR. The invisible-character repair classifies by enumeration

```python
_INVISIBLE = "​‌‍⁠﻿"
```

Five code points. The same pass's `_non_warrant_reason` repair states the
right principle in its own comment — *"Classify by SHAPE, never by
enumeration: a per-file list is short by exactly the file added next"* — and
this site does the opposite.

```
ZWSP    U+200B  Cf  caught
BOM     U+FEFF  Cf  caught
SOFT HYPHEN U+00AD Cf  NOT caught   _is_placeholder("none­") == False
MONGOLIAN VS U+180E Cf NOT caught
CGJ     U+034F  Mn  NOT caught
INVISIBLE SEPARATOR U+2063 Cf NOT caught
```

[Observed] 4 of 6 tested invisibles defeat the lexicon. I do not rate this
higher: nobody types a soft hyphen into `falsification_attempt` by accident,
and the commission is explicit that movie-plot inputs are out of scope. It
is recorded because the shape rule is two lines
(`unicodedata.category(ch) in ("Cf", "Mn")`) and because the pass demonstrably
knows the principle.

### f13 — MINOR. `--check` still misdiagnoses an environment difference as an edit

RD-56 f7's second half. The note now reaches the file, which is the repair —
but the two renders still differ byte-for-byte, and `--check` still names
the wrong two causes:

```
$ python3 scripts/render_launch_administration.py chk.json -o chk.md         # git present
$ PATH=stub:$PATH python3 scripts/render_launch_administration.py chk.json --check -o chk.md
note: LA-2: git unavailable — …
--check: chk.md differs from the record's rendering — the report has been edited,
         or the record changed without regenerating. The record is the source; regenerate.
```

[Observed] Neither stated cause is true. The delta's claim for f7 — *"The
note is stamped into the report body"* — is accurate and I confirmed it; the
`--check` consequence RD-56 raised in the same finding is not addressed, and
is not in the disclosed limits either. The rendering is a pure function of
the record **and the rendering machine's git availability**, which is a
property `--check` should name rather than guess around.

---

## RD-56 closure — independent verification, finding by finding

Denominator: 13 findings. **9 closed, 2 closed in part, 2 open by disclosure
(correctly).**

| RD-56 | Severity there | v2.2 status | Evidence |
|---|---|---|---|
| f1 — eligibility omits §4's fourth limb; an invalid record deposits `READY FOR …` in the trend log and the report's last line | BLOCKING | **Closed** | `_compute` takes `prior_errors` and is computed last; a fifth limb (git) added. Reproduced RD-56's attack: a forged instrument digest now yields `Formal gate result: NONE`, `\| … \| NONE — not eligible; row outcome was READY FOR … \|`, and `GATE VERDICT: NONE` as the report's last line. Reverting either the error limb or the git limb fails fixtures. **But see f7 above: the `fresh_context` limb has no fixture, and f6 above: the CLI's last line and exit status are still green.** |
| f2 — the forgery reproduces through any of 19 unblockquoted free-text sites | BLOCKING | **Closed for `\n`; reopened for `\r`** | Sweep: 151 `a(…)` statements, 8 raw interpolations and all 8 are booleans/ints — the 19 raw free-text sites are gone. Eight sites fixtured, and reverting `_inline` fails 6, `_quoted` 5. **f1 above: `_cell` and `_quoted` do not neutralize `\r`, and the forgery reproduces verbatim.** |
| f3 — `--schema` unauthenticated; a schema constraining nothing turns LA-1 off | MATERIAL | **Closed in part** | Both fixtures discriminate; `--schema other.json` and `{"type": "object"}` are both LA-1 errors and therefore ineligible. **f5 above: the check compares paths, not bytes, so a drifted schema at the default path is undetected.** |
| f4 — the RD-47 f1 repair has no discriminating fixture | MATERIAL | **Closed** | The new instrument-mutating fixture is the only one that fails when `_yaml_list`'s fail-open is restored (101 fixtures, 1 failing) and its expectation names the *unreadable* wording. **f8 above: the old false witness is still in the suite.** |
| f5 — three decisions-home files that record no owner decision still grant a deferral | MATERIAL | **Closed** | 22-file sweep at `918574c`: 8 refused / 14 accepted, against 4/16. All three named files refused, by name pattern and by name list; the shape predicate independently refuses a fourth. Refusal messages now name the actual reason. **f9 above: the `_sdr_exists` half of "one list, both branches" is still not true — latent, 0 of 33 live.** |
| f6 — the New-findings column can be laundered against a file outside the repository | MATERIAL | **Closed for the declared path; open through `--prior`; and the repair introduced a false absence** | f2, f3 and f4 above. |
| f7 — with git unavailable a forged record validates clean and the report carries no trace | MATERIAL | **Closed in part** | Fifth eligibility limb added; `**UNVERIFIED:**` stamped in the report body; the wholly forged record now yields `GATE VERDICT: NONE`. **f6 above (`record valid`, exit 0) and f13 above (`--check` misdiagnosis) are the residue.** |
| f8 — `LA-3b` is a check the tool runs that §5 does not name; and READY-WITH-DEFERRALS never checks that the citation resolves | MINOR | **Closed** | §5 at v2.2 names `LA-3b` explicitly (instrument line 768). `_f2_citation_resolves` gates the branch; reverting it fails a fixture; `_compute(…, resolved_deferrals=set())` yields `NOT READY` with the LA-12 error. |
| f9 — "the one place the validator reads the instrument's own prose", and the replacement figure is stale | MINOR | **Closed** | `e4_cases`'s docstring names all six (`param_block_bytes`, `instrument_version`, `launch_target_forms`, `_yaml_list`, `_param_path`, and itself), beside the population it counts; disclosed limit 3 states six. I counted the population independently: six. |
| f10 — `--allow-invalid` crashes on a record with a schema error | MINOR | **Closed** | `_unrenderable` returns a short refusal; three fixtures (missing required object, not-JSON, duplicate key) and all three fail when the guard is removed. I ran the documented path by hand on each and got a refusal, never a traceback, and never a `GATE VERDICT` line. |
| f11 — `question_digest`'s sha256 form binds nothing | MINOR | **Open, disclosed accurately** | Disclosed limit 6, with the reasoning (the schema digest is sealed by the packet) stated. `grep question_digest scripts/*.py` returns exactly one hit, the fixture's `"instrument-bound"` literal — nothing computes or compares it. The disclosure matches the code. |
| f12 — newline-bearing scalars split the §6 row and the terminal verdict line | MINOR | **Closed in effect** | `trend_row.cell` sanitizes `\|`, `\r`, `\n` and strips; the newline fixture discriminates. **f11 above: the `$`-anchor half is unrepaired and undisclosed, with no remaining false-pass path that I could find.** |
| f13 — the placeholder lexicon is defeated by one invisible character; `counterexample` accepts whitespace | MINOR | **First half closed for 5 code points; second half open, disclosed** | ZWSP and BOM fixtures discriminate. Disclosed limit 7 states the `" "` case exactly. **f12 above (enumeration, not shape) and f10 above (`"none"` is wider than the disclosed `" "`).** |

Neither deliberately-open item was re-flagged as new: **f11** is checked
against disclosed limit 6 and the disclosure is accurate and complete;
**f13's second half** is checked against disclosed limit 7, and the
disclosure is accurate but *narrower than the hole* — it discloses the
whitespace case and not the placeholder-word case, which is why f10 above
exists as a finding rather than a re-flag.

---

## Attack log

Every command was run from the frozen worktree unless noted. Outputs are
read, never exit codes, except where the exit code is itself the finding.

| # | Attack | Command | Observed |
|---|---|---|---|
| 1 | Digest verification, start and end | `sha256sum` on the four subjects | All four match the commission, both times; `git status --porcelain` empty |
| 2 | Both selftests | `--selftest` on each script | 101/0/0 and 31/0; jsonschema cross-check ran |
| 3 | New-findings laundering, declared path (control) | `validate … A_newfindings.json --trend-row` | `unknown` in the column — correct |
| 4 | New-findings laundering via `--prior` outside the repo | `validate … --prior /tmp/forged-prior-outside.json --trend-row` | Column `0` against 4 new `Not met`; 0 errors; `record valid`; exit 0 → **f2** |
| 5 | New-findings laundering via an uncommitted in-repo file whose own identity contradicts `prior_record` | `validate …` in a copied tree | Column `0`; 0 errors → **f3** |
| 6 | Escaping `prior_record.path` | `validate`/`render --allow-invalid` | `n/a (no prior record)` and "this record declares no prior — it opens the log" → **f4** |
| 7 | CR-separated forgery through `_quoted` and `_cell` | `render CR_forge.json -o CR_forge.md`; `markdown_py`; `pandoc -f commonmark/-f gfm` | 2 forged `GATE VERDICT: READY FOR …` + 2 forged `## Computed figures` above the real ones; 3 `<h2>Computed figures</h2>` under markdown_py; pandoc drops the CR → **f1** |
| 8 | Minimal CR line-ending probe | `printf 'para\r\r## Injected\r'` through both readers | markdown_py: real `<h2>`. pandoc: concatenated |
| 9 | Drifted working-tree schema at the default path | edit schema in a copied tree; record carries `final_verdict` | `record valid`, eligible, `READY FOR …` in the row and the gate line → **f5** |
| 10 | Wholly forged record under a stub `git` (exit 128) | `PATH=stub:$PATH validate … --trend-row`; `render` | Gate lines correct (`NONE`), report stamped `**UNVERIFIED:**`; last line `record valid`, exit 0 → **f6**; RD-56 f7 otherwise closed |
| 11 | `--check` across git-capable and git-less renders | `PATH=stub:$PATH render … --check` | "the report has been edited, or the record changed without regenerating" → **f13** |
| 12 | 20 repair reversions | `scratchpad/rd62-scratch/revert.py` | 18 detected, 2 not (`fresh_context` limb, prior-path behaviour half) → **f7** |
| 13 | 29 predicate reversions | `scratchpad/rd62-scratch/matrix2.py` | 24 detected, 5 not (2 of them dead code) → **f7** |
| 14 | Which fixture covers RD-47 f1 | restore `_yaml_list` fail-open on a copy, run `--selftest` | Only the instrument-mutating fixture fails; the old one still passes → **f8** |
| 15 | Schema closure, three methods + 18 deletions | tree walk, text counts, per-node deletion | 111 nodes / 18 with `properties` / 18 closed; detection 18/18 |
| 16 | Unsupported keyword and vacuous schema | `_audit_schema` on `propertyNames` and on `{"type":"object"}` | Both refused |
| 17 | Deferral-warrant sweep, whole decisions home | 22 records built, one per file, each with `Not met` F2 | 8 refused / 14 accepted; the three RD-56 named are refused |
| 18 | SDR identifier-vs-path asymmetry | 33 ids × 22 files at `918574c` | 0 currently exploitable → **f9** (latent) |
| 19 | Placeholder coverage | 43 schema `minLength` sites vs 5 `_is_placeholder` call sites | 6 of 43; `counterexample: "none"` and `falsification_summary: "none"` both validate clean → **f10** |
| 20 | Trailing-newline scalars | `date`, `repository_commit`, digests, `question_id` | `date` validates; row no longer splits; heading reads `2026-08-11 ,` → **f11** |
| 21 | Invisible characters beyond the five stripped | 6 invisibles through `_is_placeholder` | 2 caught, 4 not → **f12** |
| 22 | `question_id` pattern vs `ROSTER` | enumerate the alternation | 39 = 39, difference empty; LA-4's extra-row branch is dead |
| 23 | `--allow-invalid` on three unrenderable records | via the tools' own path | Refusal, no traceback, no `GATE VERDICT` — RD-56 f10 closed |
| 24 | Is the schema digest bound anywhere | `grep -rl e0167fb8…`; `grep schema scripts/check_governance.py` | Bound in the packet and the authority decision; **not** by `check_governance.py`, and not by the validator → **f5** |

---

## What I did not test, and why

- **Whether any reviewer-declared judgement field is true** —
  `blocking_conditions_met`, `needed_by_launch_target`,
  `routing_authority_says`, `fresh_context`,
  `same_family_as_corpus_authors`, every evidence quote and locator.
  Content-blind by design and disclosed as limit 1 and limit 8. I tested the
  mechanics around them. [Unknown]
- **The E4 "disagree → silent + not-needed" laundering** — reproduced by
  RD-56 and disclosed as limit 5. I confirmed the disclosure matches the
  code (`disagree` is computed only from non-`silent` rows) and did not
  re-flag it. [Observed]
- **The instrument's own soundness** — whether §4's conjunct set is the
  right one, whether `Unknown` across 22 A–D rows should pass. I tested code
  against instrument, per the commission.
- **A genuinely absent `git` binary** (the `OSError` path) rather than one
  returning nonzero. Both funnel through `_git_available() → False`; I
  exercised the latter. [Inferred] equivalent.
- **`launch_gate_results.py`** — §5 scopes it to historical Markdown records
  and it is not a subject.
- **Whether `cmark-gfm` splits on a bare CR.** Not installed here. The claim
  in f1 about a git host's renderer is [Inferred] from the CommonMark
  specification's definition of a line ending, not observed.

---

## Confirmation — every file opened

Subject bytes, in the frozen worktree at
`/tmp/claude-1000/-home-tze-GitHub-syzygy/8a4c1d91-a90d-4b95-a6ee-8a433a87fc1b/scratchpad/frozen-918574c/`:

1. `launch-gate-administration.schema.json` — read in full (449 lines)
2. `scripts/validate_launch_administration.py` — read in full (2213 lines)
3. `scripts/render_launch_administration.py` — read in full (785 lines)
4. `launch-gate-pre-specifications.md` — heading index of the whole file;
   §4, §5 and the head of §6 read in full (lines 478–807)

Context, read but not subjects:

5. `.syzygy/governance/contracts/candidates/round-2026-08g/LAUNCH-GATE-v2.2-SEMANTIC-DELTA.md`
   — read in full
6. `.syzygy/governance/contracts/candidates/round-2026-08g/reviews/RD-56-launch-machinery-v2.1-RAW.md`
   — read in full

Read mechanically, inside sweeps, never as authority:

7. `scripts/check_governance.py` — `grep` only, for the schema-binding
   question (f5). Not read.
8. The 22 files under `.syzygy/governance/decisions/` at `918574c`, via
   `git show`, inside the deferral-warrant sweep (attack 17) and the SDR
   sweep (attack 18). Machine-classified; not read as documents.
9. `FORMAL-CAPABILITY-1-LAUNCH-PACKET/README.md` and
   `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` — located
   by `grep -rl` for the schema digest only; contents not read.

Nothing else in the repository was opened. No other review dispatched today
was seen, sought, or is known to me.

Probe artifacts, all under
`scratchpad/rd62-scratch/`: `mk.py`, `revert.py`, `matrix2.py`,
`A_newfindings.json`, `escape_prior.json`, `CR_forge.json`, `CR_forge.md`,
`CR_forge.html`, `schema_drift.json`, `forged_nogit.json`, `date_nl.json`,
`fs_none.json`, `ce_{space,word,zwsp}.json`, `chk.json`, `chk.md`,
`stubbin/git`, `tree/` (a writable copy of the frozen worktree), `rev*/`.

---

## Summary

v2.2 is a substantially better pass than v2.1, and I could not reopen most
of it. **Nine of RD-56's thirteen findings are cleanly closed**, including
both blockers as they were stated: eligibility now has all five limbs and
reaches the trend row, the report body and the terminal gate lines; the
free-text class property is true of every site for the character the repair
was aimed at; `--allow-invalid` no longer crashes; the deferral-warrant rule
is now a shape rule and refuses 8 of 22 files where it refused 4 of 20; the
`--schema` and prior-path holes are closed on the paths RD-56 demonstrated;
and 42 of the 49 predicates I reverted are caught by a fixture. The two
deliberately-open items are disclosed, and their disclosures match the code.

What stops this from being a confirm is that **the same three repairs are
narrow a second time, in the same shape**:

- The free-text repair generalized from *two fields* to *all sites*, and
  stopped at *one line-ending character*. `_inline` learned about `\r`;
  `_cell` and `_quoted`, which carry most of the reviewer's prose, did not —
  and RD-47's forgery comes back through them character for character, in a
  report of a record that validates clean.
- The prior-record repair bound the *declared path* to the repository and
  left the *flag that overrides it* unbound, left the declared path bound to
  no commit and to no identity, and introduced a false claim of absence in
  the column §6 says F1 is answered from and only from.
- The schema repair bound the *path* and not the *bytes*, in a file whose
  every other identity is digest-checked against the named commit.

And the fixture discipline the pass names as its lesson — *"each was
verified to fail with its repair reverted"* — is refuted for the third limb
of its own blocking repair, by the same mechanism RD-56 f4 described: a
fixture masked by a check that fires first.

None of the thirteen is deep. f1 is two `.replace` calls; f2 and f3 are the
containment and equality tests that already exist ten lines away; f4 is a
third state the code's own comment already names; f5 is the digest
comparison LA-2 already performs on the instrument; f6 is the eligibility
value the same function already computed; f7 is three lines of fixture. But
f1 is the third pass at RD-47 finding 2, and f2/f3/f4 are the second pass at
RD-56 finding 6. The instrument's own §5 puts the generated report in front
of the owner and §6 makes the trend row F1's only evidence; those are the two
artifacts these findings land on.

Findings: 1 BLOCKING, 6 MATERIAL, 6 MINOR.

VERDICT: REVISE
