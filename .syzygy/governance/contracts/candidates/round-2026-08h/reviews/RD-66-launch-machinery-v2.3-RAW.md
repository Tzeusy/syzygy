# RD-66 — raw reviewer output, launch-gate machinery at v2.3

**Review:** RD-66 — launch-gate machinery, v2.3 (third administration of the RD-56 commission)
**Subject commit:** `494acab` — *round-2026-08h: launch-gate v2.3 — the v2.2 review pair repaired, and the re-review dispatched in the same round*
**Worktree:** `/tmp/claude-1000/-home-tze-GitHub-syzygy/071ee54b-8af1-4670-8c6c-3f5f842de360/scratchpad/frozen-494acab`
**Reviewer:** fresh context, no prior knowledge of this project. Adversarial posture: every claim below is something I ran, or is labelled as reasoning.
**Sibling review:** RD-65 owns policy semantics; I did not read it and make no policy-semantics claim.

## Digest verification

`sha256sum` run in the frozen worktree before anything else. **All four match the commission exactly.** [Observed]

| Artifact | Observed sha256 | Matches commission |
|---|---|---|
| `launch-gate-administration.schema.json` | `e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb` | yes |
| `scripts/validate_launch_administration.py` | `c3e20de8304430ff94ad68f65b1ec62695779a632b09fff8a64d1be94f40e52c` | yes |
| `scripts/render_launch_administration.py` | `678dab0a232958116993c6736af9f3b2d72120db8de93e6880aa480e9df13ceb` | yes |
| `launch-gate-pre-specifications.md` | `3e65aaa39bd6525c70ce589fb3f0c029af91b1bb74b29966563d3f3dcf376294` | yes |

`git log --oneline -1` in the worktree returns `494acab`. `git status --porcelain` is empty apart from the two untracked files present at session start. [Observed]

## Methodology

Read the three subject artifacts end to end (2658 + 858 + 449 lines) and the governing instrument's §8 and v2.1–v2.3 changelog entries. Then:

1. Ran both selftests and read their **output**, not their exit codes.
2. Built attack inputs in `rd66-scratch/` and ran the *worktree's own* scripts against them. Where an attack needed a repository the record could point at, I built throwaway git repos in the scratch directory and rebound `V.REPO`, following the pattern the selftest itself uses. **I never wrote to the worktree or to `/home/tze/GitHub/syzygy`.**
3. For reversion testing I loaded **patched in-memory copies** of each script under the worktree's own `__file__` (so `REPO = Path(__file__).resolve().parent.parent` still resolves to the frozen worktree) and ran their selftests. No file in the worktree was modified — verified by re-running `sha256sum` after all work: all four digests unchanged. [Observed]
4. For the renderer I did a **mechanical AST sweep** of every f-string interpolation in `render()`, `_new_findings_cell()` and `_unrenderable()`, classifying each by whether its outermost expression is a sanitizer call, rather than reading for injection by eye.
5. Where the question was "does this Markdown actually open structure", I rendered with `pandoc -f gfm -t html` rather than asserting from the raw bytes.

Verification-rule discipline: every "zero / all / none" claim below carries the sweep and its denominator, per VIS-2 and the repository's rule 9.

---

## Findings

| # | Severity | Finding |
|---|---|---|
| **1** | **BLOCKING** | `_new_findings_cell` interpolates `prior_record.path` with **no sanitizer**. A record that validates with **zero errors and exit 0**, with no `--allow-invalid`, renders a document-level forged `GATE VERDICT: READY FOR …` and a second `## Computed figures` section with forged counts, **above** the real ones. RD-47 f2 / RD-56 f2 / RD-62 f1's forgery, reproduced verbatim at the one free-text site none of the 34 renderer fixtures cover |
| **2** | **MATERIAL** | The Cf/Cc category strip excludes **Mn**. `U+034F` (the exact code point RD-62 f12 named, and the exact two-line fix it handed over — `("Cf", "Mn")`) defeats every placeholder guard in the tool at once, producing an **eligible `READY FOR …`** with zero errors on a record whose every row attempted no falsification, whose G1 critic answered nothing, and whose falsification summary asserts nothing |
| **3** | **MATERIAL** | `instrument.path` is chosen by the record. The entire §8 binding — `LAUNCH_TARGET`, the wave lists, `E4_CASES`, `E4_ROUTING_AUTHORITY` — is anchored to a path the untrusted input selects. Demonstrated: an **eligible** `READY FOR The entire product, all six waves, shipped and supported`, zero errors. Latent at `494acab` (451 files, 1 accepted), not live |
| **4** | **MATERIAL** | The prior record is the one path resolved against the **filesystem**, not the commit. It need not be committed, tracked, or a conformant record. An **untracked two-key file** inside the repository zeroes §6's New-findings column, 3 → 0, with zero errors. RD-62 f3's "need not be committed, tracked" half stands |
| **5** | MINOR | `_unrenderable` interpolates `Path(record_path).name` raw. A record file *named* with newlines, plus `--allow-invalid`, puts a document-level `GATE VERDICT: READY FOR everything` in the report — and the run **exits 0** |
| **6** | MINOR | `render … --allow-invalid` on a record with N validation errors exits **0**. RD-62 f6 established that "the summary line and return code are surfaces too"; the validator was repaired, this sibling surface was not |

**1 BLOCKING, 3 MATERIAL, 2 MINOR.**

---

### f1 — BLOCKING. One unsanitized free-text site, and it is enough

**The class property the v2.3 changelog claims:**

> The renderer's free-text neutralizers cover the full vertical-whitespace class — a bare `\r` is a CommonMark line ending, and the RD-47 f2 forgery reproduced verbatim through it (RD-62 f1).

That is true **of the sanitizers**. It is not true **of the sites**.

**Sweep with denominator.** Mechanical AST extraction of every `FormattedValue` in the renderer's three emitting functions: **74 interpolations; 55 wrapped in `_inline` / `_cell` / `_quoted` / a derived-value helper; 19 not.** Of the 19 unsanitized, 17 are module constants, computed integers, `ROSTER` identifiers, or schema-enum values (`reviewer_classification`, `routing_authority_says`, `blocking_conditions_met`, the `conjuncts` strings — all built in `_compute` from enums and `len()`). **Exactly two carry attacker-controlled free text:**

- `render_launch_administration.py:89` — `_new_findings_cell`: `return f"Unknown (prior record \`{p}\` could not be read)"` where `p = rec["prior_record"]["path"]`
- `render_launch_administration.py:123` — `_unrenderable` (finding 5)

`prior_record.path` is schema-typed `{"type": "string", "minLength": 1}` — no pattern, no constraint. [Observed]

**Reaching the branch.** `new_findings == "unknown"` requires a declared prior that resolves inside the repository and cannot be read. A path containing newlines satisfies both: `(REPO / path).resolve()` stays inside, and the read raises `OSError`. No error is appended on that route.

**Attack input.** `a1_forge.json`: `_base_record(True)` bound to the live instrument at `494acab`, made `formal: true` / `full` / fresh-context so eligibility is maximal, with `E5` set to `Not met` so the formula computes `NOT READY`, and:

```json
"prior_record": {
  "path": "prior.json\n\nGATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility\n\n## Computed figures\n\n- Not met (plain): 0\n- Unknown: 0\n\nx",
  "repository_commit": "014fd48e88cde545bb794017c1867919545e2a56",
  "date": "2026-01-01"
}
```

The prior commit is `HEAD~1` — a real ancestor, so LA-15's existence and ancestry limbs both pass.

**Observed output.**

```
$ python3 scripts/validate_launch_administration.py …/a1_forge.json
Row/formula outcome: NOT READY
Formal gate result:  NOT READY
  [NO ] every E question Met — E5='Not met'
  …
record valid — the verdict above is computed from the rows
VALIDATOR EXIT=0
```

Zero errors. Eligible. Exit 0.

```
$ python3 scripts/render_launch_administration.py …/a1_forge.json -o …/a1_forge.md
wrote …/a1_forge.md (8712 bytes) — generated from a1_forge.json
RENDER EXIT=0

$ grep -n "^GATE VERDICT\|^## Computed figures\|^ROW/FORMULA" a1_forge.md
186:## Computed figures
197:GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility
199:## Computed figures
221:ROW/FORMULA OUTCOME: NOT READY
223:GATE VERDICT: NOT READY
```

The stored artifact, lines 189–202:

```text
- Not met (plain): 1
- Not met (out of launch scope): 0
- Unknown: 0
- Deferred: 0
- Reopened: 0
- New findings vs prior: Unknown (prior record `prior.json

GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility

## Computed figures

- Not met (plain): 0
- Unknown: 0

x` could not be read)
```

The opening backtick cannot form a code span across the blank lines, so the forged lines are Markdown at document level. Confirmed against a real GFM renderer rather than asserted:

```
$ pandoc -f gfm -t html a1_forge.md | grep -n "Computed figures\|GATE VERDICT"
517:<h2 id="computed-figures">Computed figures</h2>
527:<p>GATE VERDICT: READY FOR Capability 1 — Project registration and honest shape visibility</p>
528:<h2 id="computed-figures-1">Computed figures</h2>
579:<p>GATE VERDICT: NOT READY</p>
```

**Two `<h2>Computed figures</h2>` sections. A forged `GATE VERDICT: READY FOR …` paragraph fifty lines above the real `GATE VERDICT: NOT READY`. The forged section says `- Not met (plain): 0`; the real one, two lines above it, says `1`.** [Observed]

This is RD-47 f2's harm exactly: *"a record computing `NOT READY` whose report rendered both forgeries above the real ones"* — the sentence `_quoted`'s own docstring uses to explain why it exists.

**Why the fixtures miss it.** The renderer's forgery suite enumerates 8 `SITES` and 3 `CR_SITES`. `prior_record.path` is in neither. This is the failure mode RD-56 f2 named and RD-62 f1 renamed: *"`_quoted` was applied to the two fields the previous reviewer happened to name, and the delta then described the repair as a class property."* v2.3 widened the sanitizers and widened the site list to the fields the previous two reviewers named. The property is still enumerated, not structural. [Inferred]

**Fix shape.** One call: `_new_findings_cell` returns `f"Unknown (prior record \`{_inline(p)}\` could not be read)"`. The durable repair is a fixture that drives the forgery through **every** schema-declared string field mechanically, rather than through a hand-maintained `SITES` tuple.

---

### f2 — MATERIAL. `Cf`/`Cc` is not "the classes that render as nothing", and the gap yields an eligible READY

**The code**, `validate_launch_administration.py:258–266`:

```python
def _strip_invisible(raw: str) -> str:
    """Zero-render characters are stripped by Unicode category, never by
    enumeration: the RD-56 f13 repair enumerated five code points and
    RD-62 f12 defeated it with a sixth (`Cf` alone holds over 150). `Cf`
    and `Cc` are the classes that render as nothing; …"""
    return "".join(ch for ch in raw
                   if not (unicodedata.category(ch) in ("Cf", "Cc")
                           and ch not in "\t\n\r"))
```

RD-62 f12's own hand-over sentence: *"the shape rule is two lines (`unicodedata.category(ch) in ("Cf", "Mn")`)"*. The repair substituted `Cc` for `Mn`. RD-62's own table lists `CGJ U+034F Mn NOT caught` as one of its six probes. **That probe still fails.** Zero-advance-width combining marks (`Mn`) render as nothing just as `Cf` does.

**Probe, run against the worktree's `_is_placeholder`:** [Observed]

| character | category | `_is_placeholder("none"+ch)` |
|---|---|---|
| U+200B ZWSP | Cf | True |
| U+FEFF BOM | Cf | True |
| U+00AD SOFT HYPHEN | Cf | True |
| U+180E MONGOLIAN VS | Cf | True |
| U+2063 INVISIBLE SEPARATOR | Cf | True |
| U+0000 NUL | Cc | True |
| **U+034F CGJ** | **Mn** | **False** |
| **U+FE00 VARIATION SELECTOR-1** | **Mn** | **False** |
| **U+17B4 KHMER VOWEL INHERENT AQ** | **Mn** | **False** |
| U+3164 HANGUL FILLER | Lo | False |

**Attack.** The lexicon is the *only* substance guard the tool has. It gates LA-6 (`falsification_attempt`, `counterexample`, `unknown_reason`, `unknown_settlement`), LA-11 (`bounded_reduction_plan`), LA-14 (`g1.critic_answer`, `falsification_summary`) and LA-16 (`pilot_recurrence_check.method`). Defeat it once and all of them fall together.

Record: `_base_record(True)` bound to the live instrument, `formal: true`, `full`, fresh-context, every row `Met` — with every row's `falsification_attempt`, `g1.critic_answer`, `falsification_summary` and `pilot_recurrence_check.method` set to an emptiness assertion carrying one invisible.

**Observed, with a control run at each suffix:**

```
ctl_plain.json    errors= 42  eligible=False  gate=NONE — the record has 42 validation error(s)
                  first error: LA-6: A1's falsification_attempt asserts emptiness — …
zwsp.json  (Cf)   errors= 42  eligible=False  gate=NONE — the record has 42 validation error(s)
cgj_Mn.json       errors=  0  eligible=True   gate=READY FOR Capability 1 — Project registration and ho…
vs1_Mn.json       errors=  0  eligible=True   gate=READY FOR Capability 1 — Project registration and ho…
khmer_Mn.json     errors=  0  eligible=True   gate=READY FOR Capability 1 — Project registration and ho…
hangul_Lo.json    errors=  0  eligible=True   gate=READY FOR Capability 1 — Project registration and ho…
```

The plain and `Cf` controls raise **42 errors** and are ineligible. The `Mn` forms raise **zero** and print `READY FOR Capability 1 — Project registration and honest shape visibility` as the **eligible formal gate result**.

This is a false eligible `READY FOR` — the exact outcome review question 1 asks about — on an administration that, by its own fields, attempted no falsification anywhere, answered §3's completeness critic with nothing, and recorded no pilot-recurrence method.

RD-62 rated its f12 MINOR on the grounds that the harm was cosmetic and movie-plot inputs are out of scope. I rate this MATERIAL on the harm I measured rather than the code shape: it is a single character in one JSON field that converts a wholly unfalsified record into an eligible pass, and the fix was written out verbatim in the review being repaired.

**Secondary, same site:** the docstring sentence *"`Cf` and `Cc` are the classes that render as nothing"* is a completeness claim about a population, and it is false. The v2.3 changelog restates it compressed — *"invisible characters strip by Unicode category (RD-62 f12)"* — with no residual disclosed and nothing in §8's disclosed limits covering it. [Observed — I read the v2.3 entry at `launch-gate-pre-specifications.md:1023–1053` and grepped the disclosed-limit lines.]

---

### f3 — MATERIAL. The instrument is located by a path the record chooses

LA-2 is the identity check. Every downstream binding flows from it: `param_block_bytes` → `LAUNCH_TARGET`, `REQUIRED_WAVES`, `DEFERRED_WAVES`, `E4_CASES`, `E4_ROUTING_AUTHORITY`. All of them are read from:

```python
blob = _git_show(commit, rec["instrument"]["path"])
```

Schema: `"path": {"type": "string", "minLength": 1}`. **No `const`, no pattern, nothing pins it to `launch-gate-pre-specifications.md`.** [Observed]

Contrast the schema's own identity, repaired at v2.3 for precisely this reason (RD-61 f1 / RD-62 f5): `SCHEMA_NAME` is a **module constant**, read from `HEAD` by fixed name, because a record must not choose the rules it is judged by. The instrument — which owns the launch target, the wave binding, the fixed cases and the routing authority — is still chosen by the record.

**Attack.** Scratch repository containing the real instrument at its canonical path *and* a decoy at `docs/launch-gate-pre-specifications.md`, differing only in §8: `LAUNCH_TARGET` rewritten, `REQUIRED_WAVES: [A]`, `DEFERRED_WAVES: [B, C1, C2, D1, D2]`. Both committed; HEAD is the commit. Record rebound to the decoy — digest, version, parameter-block digest, target and waves all read from it, so the record is perfectly self-consistent.

**Observed:**

```
=== control: record bound to the canonical instrument ===
 errors: 0 eligible: True | gate: READY FOR Capability 1 — Project registration and honest shape visibility

=== attack: record bound to a DECOY instrument at a different path ===
 errors: 0
 eligible: True
 GATE RESULT: READY FOR The entire product, all six waves, shipped and supported
```

Zero errors, eligible, and the formal gate result names a launch target no owner ever bound.

**Denominator — is it live?** Every `.md` file at `HEAD` (451 tracked files) run through `instrument_version()` and `param_block_bytes()`; a file is exploitable if both parse. **1 of 451: `launch-gate-pre-specifications.md` itself.** [Observed] So this is **latent, not live** at `494acab` — the same status RD-62 gave its f9.

Two reasons I do not discount it to MINOR on that basis. First, the exploit does not need malice: a *stale copy* of the instrument left in the tree — in `history/`, in a round directory, in a superseded delta — would bind an administration to superseded parameters with zero errors and no note, and the repository's own AGENTS.md records that superseded material does live in-tree. Second, `question_digest` accepts the literal `"instrument-bound"`, meaning question *text* is never compared and identity rests entirely on the instrument digest — so the instrument path is load-bearing for the whole roster, not just §8. [Inferred, from reading the schema's `question_digest` description and confirming no check consults question text.]

**Fix shape.** `INSTRUMENT_NAME` as a module constant beside `SCHEMA_NAME`, with the record's `instrument.path` checked to equal it — or a `const` in the schema.

---

### f4 — MATERIAL. The prior record need not be committed, tracked, or a record

RD-62 f3 stated three defects: the declared `prior_record` path *"need not be committed, tracked, or the record its own fields name."* v2.3 repaired the third (`_compute`, lines 1364–1373 — the declared-identity equality). The first two stand.

`_compute` resolves `(REPO / rec["prior_record"]["path"]).resolve()` and reads it **off the filesystem**. Every other cited path in the record is resolved *at the commit*: evidence via `_path_kind(commit, rel)` (LA-6), deferrals via `_path_kind` and `_git_show` (LA-11). The prior record — the one path whose **contents** are read and arithmetic performed on — is the exception.

**Attack.** Scratch repository at HEAD. An administration that regresses `A1`, `A2`, `A3` from `Met` to `Not met`. Two candidate priors, both inside the repository, both naming the record's declared `repository_commit` so the v2.3 identity check is satisfied:

- `honest_prior.json` — the truth: all rows `Met`
- `forged_prior.json` — a **two-key, untracked, never-committed** file: `{"repository_commit": <head>, "question_results": [{A1: Not met}, {A2: Not met}, {A3: Not met}]}`

**Observed:**

```
forged_prior.json tracked in git? False

honest prior             errors=0  New-findings-vs-prior = 3
    trend row: | 2026-08-11 | 522b8f2 | 3 | 0 | 0 | 0 | 0 | 3 | NOT READY |
FORGED untracked prior   errors=0  New-findings-vs-prior = 0
    trend row: | 2026-08-11 | 522b8f2 | 3 | 0 | 0 | 0 | 0 | 0 | NOT READY |
```

Zero errors either way. The §6 column reads **3** against the truth and **0** against a file that exists nowhere in the repository's history and conforms to no schema.

This does not move the verdict — `NOT READY` in both runs — which is why it is MATERIAL and not BLOCKING. It falsifies the **trend log**, which §6 makes F1's evidence, and it does so through the failure mode the surrounding comment explicitly names: *"the new-findings column is computed from it, so it is evidence, and evidence lives in the repository."* Evidence also lives **at a commit**; the comment stops one word short of the rule the rest of the file applies.

**Fix shape.** Read the prior through `_git_show(commit_or_HEAD, rel)` as every other cited path is read, so an uncommitted prior is Unknown rather than authoritative.

---

### f5 — MINOR. The record's *filename* reaches the report unsanitized

`render_launch_administration.py:123`, in `_unrenderable`:

```python
L = [f"# Launch-gate record — UNRENDERABLE: `{Path(record_path).name}`", …]
```

`_inline` guards the same value at line 186 (`src`) and not at line 123. POSIX filenames may contain newlines.

**Attack.** A file literally named `bad\n\nGATE VERDICT: READY FOR everything\n\n## Computed figures\n\nx.json` containing `{not json`, rendered with `--allow-invalid`. **Observed:**

```
exit: 0
# Launch-gate record — UNRENDERABLE: `bad

GATE VERDICT: READY FOR everything

## Computed figures

x.json`
…
--- document-level forgeries: ['GATE VERDICT: READY FOR everything', '## Computed figures']
```

The suite's own fixture for this path asserts `"GATE VERDICT" not in outX`; it holds only because `NamedTemporaryFile` never produces such a name. MINOR because it needs both filename control and `--allow-invalid`, and the report carries no true verdict for the forgery to contradict.

### f6 — MINOR. `--allow-invalid` exits 0

Observed in the run above: a record with validation errors, rendered with `--allow-invalid`, **exits 0**. `main()` returns 0 on the write path unless git was unavailable. RD-62 f6's principle — *"the summary line and return code are surfaces too"* — was applied to the validator and to the git-unavailable render, not to this sibling. A chain that renders with `--allow-invalid` reads green. The artifact does carry `THIS RECORD DOES NOT VALIDATE`, which is why this is MINOR.

---

## Per-RD-62-finding repair table

All 13 RD-62 findings. "Reversion" refers to the evidence section below.

| RD-62 | Status at v2.3 | Evidence |
|---|---|---|
| **f1** BLOCKING — `\r` defeats `_cell`/`_quoted` | **Partially repaired** | `_VERT = re.compile("[\r\n\v\f\x85  ]")` (renderer:47) covers the class; `_quoted` now uses `splitlines()` (renderer:75). REVERT 9 → 2 fixtures fail; REVERT 10 → 1 fails; REVERT 11 (`_inline`) → 7 fail. **But the class property is still enumerated, not structural: `prior_record.path` (finding 1, BLOCKING) and `record_path.name` (finding 5) reach the document unsanitized.** The `\r` spelling is closed; the site coverage is not |
| **f2** MATERIAL — `--prior` launders §6 from anywhere | **Repaired** | `validate:1177–1187` — `Path(prior_path).resolve()` + `is_relative_to(REPO)`. Verified live: `--prior /etc/passwd` and `--prior <symlink-inside→outside>` both error, exit 1. REVERT 7 → 1 fixture fails |
| **f3** MATERIAL — declared identity does not control the file read | **Partially repaired** | `_compute:1364–1373` adds the commit-equality check; REVERT 6 → 2 fixtures fail. Verified live: a prior file naming a different commit errors and yields `new_findings='unknown'`. **The "need not be committed, tracked" half stands — finding 4** |
| **f4** MATERIAL — escaping prior collapses to false absence | **Repaired** | `_compute:1357` sets `new_findings = "unknown"` on the escape path. Fixture *"a declared prior that escapes the repository computes Unknown, not absence"* present and passing; verified live (`prior_record.path = /etc/passwd` → 1 error, `nf='unknown'`) |
| **f5** MATERIAL — schema not digest-bound | **Repaired** | `validate:674–692` reads the schema from `_git_show("HEAD", SCHEMA_NAME)` and raises a distinct error on working-tree drift. REVERT 4 → 2 fixtures fail (*"an in-place schema edit does not admit a forbidden verdict word"*, *"working-tree schema drift is its own error"*) |
| **f6** MATERIAL — `record valid` + exit 0 for an unvalidated record | **Repaired** | `validate:2644–2651`. Verified live with git stubbed to fail: `record NOT fully validated — git was unavailable…` and **exit 2**. Renderer likewise exits 2 with the `**UNVERIFIED:**` banner in the file |
| **f7** MATERIAL — 5 live unfixtured predicates | **Repaired** | `fresh_context` limb: new fixture at `validate:2415–2428`, REVERT 5 → 1 fails. `_is_ancestor`: REVERT 3 → 2 fails (the scratch-repo `dangling` commit reaches the ancestry branch, which `"f"*40` never did). E4 `case_index` run: new fixture at `validate:2407–2410`, REVERT 8 → 1 fails. `--prior` commit equality: REVERT 13 → **0 fail**, but I verified the branch is now **redundant** — deleting it leaves the property enforced by the f3 repair in `_compute` (observed: 1 error, `new_findings='unknown'`, unchanged). The two dead branches (LA-4 extra-row, LA-12 plain-over-deferrals) were removed with the unreachability argued in place at `_compute:1309–1315` |
| **f8** MINOR — false-witness fixture still green | **Repaired** | `validate:1660–1666` — renamed to *"LA-3 a wave set differing from §8's is an error"* with a comment stating it exercises the §8-**mismatch** branch and that the unreadable-parameter branch is covered by the instrument-mutating scratch fixture. The name no longer asserts a property it does not test |
| **f9** MINOR — "one list, both branches" untrue | **Repaired** | `_sdr_exists:509–528` now resolves only against `SURFACE-DECISION-RECORD.md` with a `**SDR-n**` definition shape, and the comment states that accurately (*"the identifier branch does not consult it"*). Stricter than the exclusion list it replaces. REVERT 14 → 0 fixtures fail; I checked whether that is a gap: **22 files in the decisions home, 37 distinct SDR ids, all 37 resolve identically under both forms at `494acab`** — the change has no observable witness at this commit, so no fixture can exist. Not a defect |
| **f10** MINOR — placeholder coverage 6 of 43 | **Partially repaired** | Both fields RD-62 named are now checked: `counterexample` at `validate:878–880` (REVERT 15 → 1 fails) and `falsification_summary` at `validate:1144` (REVERT 16 → 1 fails). Coverage 6 → 8 of 43; the other 35 stand and are not disclosed. **And finding 2 shows the lexicon itself is bypassable, which subsumes the coverage question** |
| **f11** MINOR — `$` admits a trailing newline | **Repaired** | `_instance_errors:436` uses `re.fullmatch`; `_audit_schema:352–357` refuses any unanchored pattern so the two implementations cannot diverge. REVERT 1 → 1 fixture fails. The cosmetic `2026-08-11 ,` artifact is gone |
| **f12** MINOR — invisible strip by enumeration | **Partially repaired** | Enumeration → `unicodedata.category(ch) in ("Cf", "Cc")`. REVERT 2 → 2 fixtures fail. **But RD-62 handed over `("Cf", "Mn")` and the repair substituted `Cc` for `Mn`, so RD-62's own named residual `U+034F` still defeats the lexicon — and finding 2 shows the harm is an eligible `READY FOR`, not the cosmetic issue RD-62 rated MINOR** |
| **f13** MINOR — `--check` misdiagnoses an environment difference | **Repaired** | `renderer:828–834`. Verified live: rendered **with** git, `--check`ed **without** → *"Unknown(git unavailable): the regeneration ran without git, so the difference may be the environment, not an edit"*, **exit 2** |

**Tally: 8 repaired, 4 partially repaired, 0 unrepaired, 1 (f7) repaired with one redundant-branch reversion verified as a non-defect.**

---

## Selftest and fixture-reversion evidence

### Selftests, as run in the frozen worktree

```
$ python3 scripts/validate_launch_administration.py --selftest
…
  pass  a declared-but-unreadable prior record computes Unknown, not absence
  pass  the base record validates identically under the reference jsonschema implementation

119 fixtures, 0 failing — a check that cannot fail is not a check
EXIT=0
```

```
$ python3 scripts/render_launch_administration.py --selftest
…
  pass  a report of an unverified record says so in the file, not only on stdout
  pass  --check detects a hand-edited report

34 fixtures, 0 failing — a check that cannot fail is not a check
EXIT=0
```

**119 and 34 confirmed, zero failing, no `SKIP` lines and no git-skip warning** — every git-dependent fixture ran. The reference-implementation cross-check (`jsonschema`) ran and agreed. [Observed]

### Reversion battery — 16 reversions, 14 detected

Each reversion is a single targeted edit to an in-memory copy of the script, loaded under the worktree's own `__file__`. Denominators are the number of fixtures that flipped to FAIL.

| # | Repair reverted | Suite | Fails | Fixtures that caught it |
|---|---|---|---|---|
| 1 | `re.fullmatch` → `re.search` (f11) | validate | **1** | *LA-1 a trailing newline does not satisfy an anchored pattern* |
| 2 | Cf/Cc category → 5-codepoint enumeration (f12) | validate | **2** | *a function-application character (Cf)…*; *a C1 control character (Cc)…* |
| 3 | `_is_ancestor` → `return True` (f7-2 / RD-61 f2) | validate | **2** | *a record anchored to an off-branch commit is an error, not an anchor*; *a prior commit outside this history is a stale prior (ancestry, not existence)* |
| 4 | Schema from working tree, not HEAD bytes (f5) | validate | **2** | *an in-place schema edit does not admit a forbidden verdict word*; *working-tree schema drift is its own error* |
| 5 | Delete the `fresh_context` eligibility limb (f7-1) | validate | **1** | *no fresh context alone makes an otherwise-passing record ineligible (limb, not error count)* |
| 6 | Drop prior declared-identity equality (f3) | validate | **2** | *a prior file whose own commit differs from the declared identity is refused*; *…and the new-findings column reads Unknown, not a number* |
| 7 | Drop `--prior` containment (f2) | validate | **1** | *--prior outside the repository is an error, not a comparison* |
| 8 | Drop the E4 case-index run check (f7-4) | validate | **1** | *LA-10 duplicate E4 case indices at the right count are an error* |
| 9 | `_VERT` → `\n` only (f1) | render | **2** | *a \r-spelled forgery in `launch_target (inline, \r)`…*; *…in `evidence quote (cell, \r)`…* |
| 10 | `_quoted` → `split("\n")` (f1) | render | **1** | *a \r-spelled forgery in `falsification_summary (quoted, \r)`…* |
| 11 | `_inline` stops flattening (RD-56 f2) | render | **7** | all six named free-text sites + the `\r` inline site |
| 12 | `_cell` stops escaping pipes | render | **1** | *a pipe inside evidence text does not add a column* |
| 13 | Drop `--prior` commit equality (f7-3) | validate | **0** | **redundant branch — verified non-defect** (below) |
| 14 | `_sdr_exists` → whole-home grep (f9) | validate | **0** | **behaviourally equivalent at this commit — verified non-defect** (below) |
| 15 | `counterexample` → falsiness only (f10) | validate | **1** | *LA-6 a placeholder counterexample is no counterexample* |
| 16 | Drop the `falsification_summary` check (f10) | validate | **1** | *LA-14 a placeholder falsification_summary is an error* |

**16 reverted, 14 detected, 2 undetected — and I checked both rather than assuming, per the discipline RD-62 applied to its own two dead branches:**

- **#13 is redundant, not unfixtured.** With the `--prior` commit-equality branch deleted, I re-ran the failing input: `--prior` pointing at a file whose `repository_commit` is `f*40` against a record declaring `522b8f2…`. Result: **1 error** — `LA-15: the prior record read from prior.json names commit ffff… but prior_record declares 522b8…` — and `new_findings: unknown`. The f3 repair in `_compute` reads the same file and enforces the same property, so no fixture can discriminate. The property is enforced. [Observed]
- **#14 has no witness at this commit.** Sweep with denominator: 22 files in `.syzygy/governance/decisions/` at `HEAD`, **37** distinct `SDR-n` identifiers across them, and **37 of 37** resolve under the new `**SDR-n**`-in-the-owning-record form. **0 divergent.** The hardening is real but unobservable at `494acab`; the fixture that would witness it cannot be written from the current corpus. [Observed]

**The three security-relevant reversions the commission asked for are #2, #3 and #4** (the Cf/Cc strip, LA-2 ancestry, and schema-from-committed-bytes) — each demonstrably caught, with the named fixtures above. #5, #6, #7, #9 and #10 extend the demonstration across the rest of the v2.3 repair set.

**Integrity check.** `sha256sum` re-run on all four subject artifacts after every reversion and attack: **unchanged, all four.** No file in the worktree or in `/home/tze/GitHub/syzygy` was created, edited or deleted. [Observed]

---

## Attack log — what I ran and what happened

| Attack | Result |
|---|---|
| Forgery via `prior_record.path` (unsanitized render site) | **SUCCEEDED** — finding 1, BLOCKING |
| `Mn` invisible defeating the placeholder lexicon → eligible `READY FOR` | **SUCCEEDED** — finding 2 |
| Decoy instrument at a second repository path → eligible `READY FOR <attacker target>` | **SUCCEEDED** — finding 3 |
| Untracked 2-key prior file zeroing §6's New-findings column | **SUCCEEDED** — finding 4 |
| Forgery via the record's filename (`--allow-invalid`) | **SUCCEEDED** — finding 5 |
| `repository_commit` = tip of an unmerged branch | Refused: *"not reachable from the repository's current HEAD"*, 40 errors, ineligible |
| `repository_commit` = dangling `commit-tree` object | Refused, same error, ineligible |
| `--prior /etc/passwd` | Refused: *"resolves outside the repository"*, exit 1 |
| `--prior` via a symlink inside the working directory targeting outside | Refused — `resolve()` follows the symlink; exit 1 |
| `prior_record.path` absolute (`/etc/passwd`) | Refused: `pathlib` absolute-override caught by containment; `new_findings='unknown'` |
| `prior_record` content naming a commit ≠ declared | Refused: *"the declared identity controls the comparison"*; `new_findings='unknown'` |
| `--prior` inside repo with commit mismatch | Refused twice, by both branches |
| Backslash-pipe (`\|`) in a counterexample, to split a table column | **No split.** `_cell` emits `\\|`; `pandoc -f gfm` renders one cell containing a literal `\|`, full text intact |
| `date: "2026-08-11\n"` (the `$`-anchor residual) | Refused by `fullmatch` |
| Git unavailable (stubbed `git` returning 1) — validator | `record NOT fully validated…`, **exit 2**, ineligible via the fifth limb |
| Git unavailable — renderer | `**UNVERIFIED:**` banner **in the file**, **exit 2** |
| Render with git, `--check` without git | `Unknown(git unavailable)`, **exit 2** — not "edited" |
| `NONE — <limbs>` on every surface, ineligible record | All three carry the literal: validator `Formal gate result: NONE — \`formal: false\``; trend row last cell `NONE — \`formal: false\`; row outcome was READY FOR …`; report `GATE VERDICT: NONE — \`formal: false\` — not eligible to be cited as launch evidence`. The limb strings are built from enums and integers, so none is attacker-controlled |

## What I did not test, and why

- **Policy semantics** — whether §4's formula, the roster, or the eligibility limbs are the *right* rules. RD-65 owns that; I checked only that the tool implements what §4 states. [Unknown]
- **The truthfulness of any evidence quote.** Documented as content-blind by design; I did not attempt to measure it. [Unknown]
- **cmark-gfm specifically.** The table-escaping analysis was confirmed under `pandoc -f gfm`; other GFM implementations are [Unknown] to me.
- **A malicious `git` on `PATH`.** An attacker who controls the interpreter's `PATH` controls everything; out of any useful threat model.
- **The 35 uncovered placeholder sites individually** (RD-62 f10's residual). Finding 2 makes the coverage question moot until the lexicon itself is closed.
- **`launch_gate_results.py`** and the historical Markdown records — not subject artifacts.

## Confirmation — every file I opened

`launch-gate-administration.schema.json` (449 lines, whole); `scripts/validate_launch_administration.py` (2658 lines, whole); `scripts/render_launch_administration.py` (858 lines, whole); `launch-gate-pre-specifications.md` §8 parameter block, the v2.1/v2.2/v2.3 changelog entries, and the disclosed-limit lines; `round-2026-08h/reviews/RD-62-launch-machinery-v2.2-RAW.md` (findings table and f1–f13 in full).

## Summary

The v2.3 pass is substantial and mostly honest work. Eight of RD-62's thirteen findings are cleanly repaired, each with a fixture I verified fails when its repair is reverted — including the three the commission named as security-relevant, and including the four predicates RD-62 caught with no discriminating fixture at all. The fixture suite is materially stronger than the one RD-62 measured: 16 targeted reversions, 14 detected, and both undetected ones verified as non-defects rather than assumed to be.

What blocks is that the pass repaired the **instances** its reviewers named and restated the result as a **class property** — the third consecutive pass to do exactly that on exactly this mechanism. RD-56 f2 said it about two fields. RD-62 f1 said it about two sanitizers. v2.3 widened both sanitizers to the full vertical-whitespace class and widened the fixture site list to eleven named fields — and `prior_record.path`, which nobody had named, still carries the RD-47 f2 forgery into the report of a record that validates with zero errors and exits 0. The same shape recurs twice more: RD-62 f12 wrote out the two-line fix and the repair applied it with one of the two categories swapped, which is enough to convert a wholly unfalsified administration into an eligible `READY FOR`; and the instrument, unlike the schema repaired in the same pass for the same reason, is still located by a path the untrusted record chooses.

Four of these are one root cause with four addresses: **a property is asserted over a population that was never enumerated.** The durable repair is not four more fixtures but two mechanical ones — drive the forgery through every schema-declared string field, and assert the sanitizer-coverage sweep itself — so that the next unnamed site fails the suite instead of the next review.

VERDICT: REVISE
