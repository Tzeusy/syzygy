(part 1/3)

# Reviewer: validation (RD-17)
**Date:** 2026-08-09
**Commit:** 771965c (read-only clone; verified pristine at exit — `git status --porcelain` empty, `git rev-parse HEAD` = `771965c70f419465d13713f7654396a664234b47`)

**Files read**
`scripts/check_governance.py` (3,318 lines, full); `C/scripts/build_active_manifest.py`; `C/scripts/verify_final_prespec.py`; `C/scripts/build_contract_index.py`; `C/scripts/build_dependency_index.py`; `C/scripts/build_budget_report.py`; `C/ACTIVE-CONTRACT-MANIFEST.txt`; `C/wave-manifests/WAVE-{A,B,C1,C2,D1,D2}-MANIFEST.txt`; `C/05-CONTRACT-INDEX.yaml`; `C/CONTRACT-DEPENDENCY-INDEX.md`; `C/CONTEXT-BUDGET-REPORT.md`; `C/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`; `C/06-CONTEXT-LOAD-MAP.md`; `C/README.md`; `C/00-README.md`; `C/TASK-TO-CONTRACT-INDEX.md`; `C/10-EXIT-REPORT.md`; `C/03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`; `C/policy-candidates/TERM-REGISTRY.md`; `.syzygy/governance/policies/GOVERNANCE-SUBSTRATE-LOCK.yaml`; `.syzygy/governance/policies/craft-and-care/` (file list + targeted greps); `.gitignore`; `AGENTS.md`. Excluded per instruction: `C/round-2026-08d/`, `C/reviews/`, `C/history/`, `_bootstrap/`.

**Mutation testing** was performed only in a copy at `…/scratchpad/rd17-mutant` (and a git-stripped copy at `…/scratchpad/rd17-nogit`). Eleven mutations across five scripts; each is reported below with its observed output.

---

## Findings

### 1. A wave act's subject description is a transcribed count that nothing verifies — the owner can bind 20 modules under the words "the 19 modules" with the whole battery green — **blocking**

The acceptance record describes each wave act in prose that states a module count:

> `| A | ACCEPT FOUNDATIONAL WAVE A: 8d4f3e72… | **The 19 modules** of RFC 0001–0006 …, whose own digest is the act's argument |`
> — `C/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:22` (same shape at :23 "The 11 modules", :24–:27)

CG-7b compares the record's stated **sha256** to the wave manifest's sha256. Nothing compares the record's stated **count** to the manifest's row count. The two are edited by different hands at different times — the exact argument `check_governance.py:634-636` gives for CG-7 existing at all.

**[Observed] Mutation M10** (in the copy): added a twentieth module `rfcs/RFC-0005/extra-module.md`; regenerated all seven manifests, the contract index, the dependency index and the budget report; updated the record's Wave-A argument to the new manifest digest as a maintainer would. Result:

```
WAVE-A rows: 20   record prose: The 19 modules of RFC 0001–0006
--- full battery ---
check_governance: 25 OK, 15 WARN, 0 FAIL (40 checks) — counts derived, not asserted
build_active_manifest    all 7 manifests match regeneration
build_contract_index     index matches regeneration — no drift
build_dependency_index   dependency index matches regeneration — no drift
build_budget_report      fixture anchors match regeneration
verify_final_prespec     PASS — all checks clean
```

Six scripts, zero findings, against an offering that undercounts its own subject. This is RD-8's class verbatim — the record's own wave-history note calls routing an owner to a stale offering *"the finding that converts act 1 from a knowing act into a surprised one"* — and it is live for all six wave acts simultaneously.

**Repair.** Add a CG-7 predicate: for each `w` in `WAVE_IDS`, parse the integer preceding `module`/`modules` in the record's row for wave `w` and require it to equal `len([rows in WAVE-w-MANIFEST.txt])`; fail with both numbers named. The wave manifests already state the measured count in their own header line (`# 19 module(s); subset of ACTIVE-CONTRACT-MANIFEST.txt`), so the comparison needs no new measurement — only a comparison. Alternatively, remove the count from the record's prose and point at the manifest header; a count is a derived value and, per this repository's own rule 3, does not belong in a second artifact.

---

### 2. `build_budget_report.py --check` returns 0 on a falsified generated report — the sole home of every volatile measurement has no failing check — **major**

The script's docstring states the rule it exists to enforce: *"a measurement has exactly one home, and that home is generated"* (`build_budget_report.py:11`), and the artifact's own banner reads *"Do not edit by hand, and do not copy a figure out of it."* `AGENTS.md` lists `build_budget_report.py --check` under Validation as the check for *"every volatile measurement."*

It is not. `build_budget_report.py:437`:

```python
anchor_drift = [d for d in drift if "CONTEXT-BUDGET-REPORT" not in d]
```

Every drift finding about the report itself is filtered out of the exit code. The stated justification (`:433-436`) is *"The as-of commit line makes the report differ whenever HEAD moves, which is correct for a generated file and useless as a drift signal"* — but `_without_asof()` at `:393-404` **already strips that line before the comparison**. The exemption therefore suppresses nothing except real content drift.

**[Observed] Mutation M4** (in the copy): hand-edited the report's §3 headline `**39 modules, 110,081 words.**` → `**32 modules, 99,067 words.**` and one module row `8,556` → `1,234`:

```
-- build_budget_report --check:
DRIFT: CONTEXT-BUDGET-REPORT.md — differs from regeneration
note: report-only drift (as-of commit / corpus figures); regenerate before quoting
fixture anchors match regeneration
rc=0
-- check_governance: 25 OK, 15 WARN, 0 FAIL (40 checks)   exit=0
-- build_active_manifest/contract_index/dependency_index/verify_final_prespec: all clean
```

The values I injected are the *actual* rev10-era figures still living elsewhere in the package (see finding 4), so this is not a synthetic scenario: the hole permits precisely the regression the report was built to end. Related: the shipped report's as-of line reads `565aff7948b0…`, one commit behind HEAD `771965c…` — the currency claim rests entirely on discipline, with no check behind it.

**Repair.** Delete the `anchor_drift` filter; return 1 on any drift, `_without_asof` having already removed the only legitimately volatile line. If the pre-commit ordering makes the as-of line genuinely unmanageable, drop it from the artifact rather than exempting the whole file from its own check.

---

### 3. CG-24 — the one check whose job is honest coverage reporting — over-credits itself by two families — **major**

CG-24 prints `16 of 24 check families have at least one fixture — quote this figure, never 'every check'`. The true figure is **14**. The `--selftest` run names fixtures for exactly 14 families:

```
$ python3 scripts/check_governance.py --selftest | grep -oE 'CG-[0-9]+[a-z]?' | sort -u
CG-13 CG-14 CG-15 CG-16 CG-17 CG-18 CG-19 CG-20 CG-21 CG-22 CG-23 CG-24 CG-7e CG-8
```

CG-11 and CG-12 appear in neither the fixture list nor the uncovered list. The cause is `CASE_NAME` at `:3203`:

```python
CASE_NAME = re.compile(r'"(?:F\d+[a-z]?\s+)?(CG-\d+)[a-z]? (?! )')
```

The `(?! )` lookahead is meant to exclude `res.add` check names, which conventionally use two spaces. Three string literals in the file break that convention and are credited as fixtures:

- `:3297` — `res.add("WARN", "CG-11 ignore rules", 0, 0, unit="rule",` — a check name
- `:3274` — `"CG-11 cannot run and \`--scope tracked\` is not honored. Every "` — prose inside a `print`
- `:1327` — `res.add("WARN", "CG-12b \`_bootstrap/\` citation allowlist", …)` — a check name

CG-24 has a fixture named *"a check's own name is not a fixture for it"*, and it passes — because its synthetic input (`'res.add(status, "CG-13  deps resolve",'`, `:2711`) uses two spaces. The fixture proves the rule on an input the real corpus does not match.

**[Observed] Mutation M9** (in the copy): reformatted only those three string literals to two spaces — no fixture added, no check altered:

```
before: 16 of 24 check families have at least one fixture
        no `--selftest` fixture: CG-1, CG-2, CG-3, CG-4, CG-5, CG-6, CG-9, CG-10
after:  14 of 24 check families have at least one fixture
        no `--selftest` fixture: CG-1, CG-2, CG-3, CG-4, CG-5, CG-6, CG-9, CG-10, CG-11, CG-12
```

Secondary, and disclosed rather than hidden (`:3224-3227`): the rollup is per family, so **CG-7 counts as covered on the strength of CG-7e's two fixtures while CG-7a/7b/7c/7d — the four checks guarding every owner act argument — have none.** Of the 40 reported checks, the fixture set names 14 families; CG-1a–1f, CG-2a–2d, CG-3, CG-4, CG-5, CG-6, CG-7a–7d, CG-9, CG-10, CG-11, CG-12, CG-12b, CG-15b and CG-19b are named by no fixture. (CG-7a's partition predicates *do* fail correctly under mutation — see finding 10 — but that is my evidence, not the battery's.)

**Repair.** Anchor `CASE_NAME` to the actual fixture construct (`cases.append((` ) rather than to a quoting convention, or require two spaces in `res.add` names and add a check for it. Then add at least one fixture each for CG-7a and CG-7b, whose subjects are the act arguments.

(part 2/3)

### 4. The stale "32 modules" figure survives in four active-lane artifacts, including the default-path load map; CG-20/CG-21's regex cannot see a corpus count — **major**

The real population is 39 modules (`verify_final_prespec.py`: *"active corpus (RFC files): 110081 words across 39 modules"*; `ACTIVE-CONTRACT-MANIFEST.txt`: 39 rows; `CONTRACT-DEPENDENCY-INDEX.md:37`: *"Coverage: **39 modules** across **11 contracts**"*). Active-lane artifacts still state 32:

- `C/06-CONTEXT-LOAD-MAP.md:15` — `11 contracts → **32 modules** (7 packages + 2 single-file RFCs + RFC-0010 + RFC-0011 + 7 package READMEs)`. This is the artifact `AGENTS.md` routes every contract question to, and its banner reads *"Derived measurement record"*, not superseded.
- `C/README.md:20` — `| rfcs/ | The 32 active candidate contract modules (RFC 0001–0011) — the act-1 subject |` (also still says "act-1 subject" after round-2026-08d retired the single act)
- `C/README.md:43` — `sha256sum -c ACTIVE-CONTRACT-MANIFEST.txt          # all 32 modules OK` — a reproduction instruction that will print 39
- `C/TASK-TO-CONTRACT-INDEX.md:22` — `of the 32 modules** (verified 2026-08-05 by a front-matter sweep of every …)`

(`10-EXIT-REPORT.md:18` and `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md:24` also say 32 but carry explicit historical/frozen banners — correctly out of scope.)

CG-20 is *named* for this rule — `"CG-20  load-map states no measurement"`, docstring: *"The context-load map states no measurement of the corpus it routes"* — and reports `73 lines examined, 0 findings`. The reason is `CONTRACT_MEASUREMENT` (`:2886-2892`), which matches only comma-formatted 4–5 digit figures, `\d{3,}\s*(words?|tokens?)`, `` `wc -w` `` and `word count`. A count of *modules*, *contracts* or *clauses* — the corpus measurements most likely to move under a wave restructure — is invisible to it. Same for CG-21 over the 39 contract modules.

**Repair.** Extend `CONTRACT_MEASUREMENT` to `\b\d{1,3}\s*(modules?|contracts?|clauses?|fixtures?|checks?)\b` (the pointer exemption `MEASUREMENT_POINTER` already gives the escape hatch), and widen CG-20's subject from `LOAD_MAP` alone to the active-lane package artifacts that state corpus figures — at minimum `C/README.md` and `C/TASK-TO-CONTRACT-INDEX.md`. Then correct the four figures above.

---

### 5. Both remaining generators transcribe figures into their generated output; the budget report contradicts its own §4 — **major**

The question was whether a generator quotes rather than measures. Two do.

**`build_budget_report.py:308-309`** emits into `CONTEXT-BUDGET-REPORT.md:55-56`:

> `counted 88 measurement-shaped figures across **the nine fixtures** and found **CG-18 covering 18** of them`

There are **ten** fixtures — the same file's §1 table measures ten rows and prints `**6 of 10 fixtures are above the proposed 20,000-token trigger.**` twenty-eight lines above. CG-18's current coverage is **20 measurements**, not 18. And §4 of that same generated file states:

> `- **No check counts, fixture counts, or coverage denominators.** … Copying them here would recreate the class this report exists to end, one register further out.`

The file contains a fixture count and a coverage denominator, both stale, both hard-coded in the generator. `CONTEXT-BUDGET-REPORT.md:65` likewise emits `*"RFC-0001 is indivisible (8,353 w)"* disagreed by eleven words` while its own §3 measures RFC-0001 at 8,556 — an audit trail about a stale figure that has itself gone stale.

**`build_dependency_index.py:369`** emits into `CONTRACT-DEPENDENCY-INDEX.md:175`:

> `disagree — the 20 asymmetric edges this section used to report were …`

a hard-coded count of a prior state, in a file whose header is `# Contract dependency index — derived, never authority`.

**Repair.** In the budget report, replace `the nine fixtures` / `covering 18` with `{len(measures)}` and a value computed in-script (or drop the sentence and cite the review by name only — a narrative does not need the numbers). Compute the `8,353`/`eleven words` clause from the current measurement or delete it. In the dependency index, either state `20` as an explicitly dated historical figure with the round record cited, or drop the number.

---

### 6. No banner check covers the package's front-door README or any of the 39 contract modules; a candidate can present as accepted with the battery green — **major**

CG-4's population is 8 files: `C/00-README.md`, the six `C/policy-candidates/*.md`, and `topology-candidates/TRACKING-NOTE.md`. It does **not** cover `C/README.md`, `C/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`, `C/DOCTRINE-AMENDMENT-*.md`, or any of the 39 modules under `C/rfcs/` — the actual act subjects.

**[Observed] Mutation M8b** (in the copy): edited only `C/README.md`, `# Candidate contract package — NOT ACCEPTED` → `# Accepted contract package — IN FORCE`, and its banner body from *"is candidate material. No owner acceptance act has been performed over any of it. Nothing here binds"* → *"is accepted and binding. The owner acceptance acts have all been performed. Everything here binds"*:

```
-- FAILs: (none)
   summary: 25 OK, 15 WARN, 0 FAIL (40 checks)   exit=0
```

The check itself is sound — **[Observed] Mutation M8c**, stripping "candidate" from `00-README.md`'s first ten lines, gives `FAIL  CG-4 … 8 files examined, 1 finding / … — no 'candidate' in the first 10 lines`. The defect is the denominator, not the predicate. This is the AGENTS.md hard prohibition *"install candidate material into an accepted home or label it accepted"* going unguarded on the file a reader meets first.

**Repair.** Extend CG-4's target set to every `.md` directly under `C/` and, for `C/rfcs/`, apply the directory-marker pattern CG-4 already uses for the topology bundle (`C/README.md` as the directory-level candidate marker, since per-module banners would churn the digest-bound bytes). Add the inverse predicate CG-5 already has for craft: fail on an accepted/binding/in-force claim inside the candidate tree, not merely on a missing word.

---

### 7. `wave-manifests/` is never enumerated: an extra, internally false wave manifest is invisible to every check — **minor**

`build_active_manifest.py` diffs only the seven files it generates (`run()`, `:172-191`); CG-7a iterates `WAVE_IDS` and reads only those six paths (`:688-705`). Neither treats `C/wave-manifests/` as a population.

**[Observed] Mutation M5** (in the copy): dropped a `WAVE-C-MANIFEST.txt` into `wave-manifests/`, relabelled, with one digest row zeroed so the file is genuinely false:

```
-- generator: all 7 manifests match regeneration            rc=0
-- check_governance FAILs: (none)   25 OK, 15 WARN, 0 FAIL (40 checks)
```

The directory is where the acceptance record sends an owner for each wave act's argument, and `wave-manifests/` is a declared act install home (`FORWARD_REFS`, `:203`). A leftover from an earlier wave design would sit there unnoticed.

**Repair.** In `build()`, list `wave-manifests/` and error on any file not in the generated set; mirror it as a CG-7a finding so a hand-added file fails without waiting for a regeneration.

---

### 8. `build_active_manifest.assign()` silently admits a stray top-level module into Wave A, contradicting the rule its own docstring states — **minor**

Docstring rule 1: *"Every `.md` under `rfcs/` is assigned to exactly one wave by the tables below; a file the tables do not assign is a hard error, never silently included or skipped … adding a module and adding it to a wave are one deliberate act."* The implementation (`:87`) is a prefix match:

```python
contract = name[:8] if name.startswith("RFC-") else None
```

**[Observed] Mutation M6** (in the copy): created `rfcs/RFC-0006-scratch.md`, then called `enumerate_modules()` directly:

```
errors: []
assigned wave for the stray: A
total modules now: 40
```

No error; silent admission into Wave A — the owner's act argument. `--check` does report `DRIFT`, so it is not invisible, but the drift message says "regenerate", and a regeneration enlarges the wave with no deliberate assignment. The generator's own selftest case 2 uses `RFC-9999-unassigned.md`, a name chosen so its prefix collides with nothing — the fixture passes on the one input shape that cannot exercise the hole.

**Repair.** Require an exact key in `WAVE_OF_MODULE` for every top-level `rfcs/*.md`, using `WAVE_OF_RFC` only for paths of the form `rfcs/RFC-00nn/…`. Change the selftest fixture to a colliding name (`RFC-0006-scratch.md`).

(part 3/3)

> [Storage note, not reviewer text: this part was never delivered by message — the reviewer's session hit a platform limit after part 2/3. It is recovered verbatim from the reviewer's own composed final report in its session transcript (d35824df…), whose text was verified byte-identical to the delivered parts over the finding-8 overlap. Content below is the reviewer's, unedited.]

### 9. The generator's "partition asserted on every run" is a check that cannot fail — **minor**

Docstring rule 3: *"**The waves partition the package.** … the partition is recomputed and asserted on every run."* The assertion is `:131-134`:

```python
union = sorted(r for w in WAVES for r, _ in per_wave[w])
if union != sorted(assigned):
    return None, ["wave partition does not equal the active set — …"]
```

`per_wave` is populated only by `for rel in sorted(assigned): per_wave[assigned[rel]].append(...)`, so `union == sorted(assigned)` by construction.

**[Observed] Mutation M7** (in the copy, by direct import): the only way the comparison can differ is a wave label outside `WAVES`, and that path raises first —

```
labels outside WAVES (the only way the assert can fire): []
with a bad label, build() raises KeyError 'Z' — the assert is never reached
```

The real partition coverage exists and works, but it lives in CG-7a, not here — **[Observed] Mutations M2a/M2b** (in the copy) confirm it:

```
M2a (row duplicated into WAVE-B):
FAIL  CG-7a … 79 entries examined, 1 finding
      rfcs/RFC-0001-project-graph-identity-state-planes.md — appears in waves A/B; the partition overlaps
FAIL  CG-7b … wave B — record offers daa6a5dd37b7… but the wave manifest hashes to b7cdeb79bce4…
M2b (row deleted from WAVE-D1):
FAIL  CG-7a … 77 entries examined, 1 finding
      rfcs/RFC-0010/budget-reservation.md — in the active manifest but in no wave manifest; the partition is incomplete
```

**Repair.** Either delete the unreachable branch and let the docstring credit CG-7a for the partition, or make it a real check by building `per_wave` from an independent second pass over the tree.

---

### 10. CG-18's denominator shrinks silently when a fixture drops its `Measured:` anchor — **minor**

`check_governance.py:1868-1875`:

```python
claimed = re.search(r"Measured:\s*\*\*([\d,]+)\s*words", body)
if claimed:
    examined += 1
```

The word-count predicate is skipped, without a finding, when the anchor is absent.

**[Observed] Mutation M3b** (in the copy): replaced one fixture's `Measured: **14,112 words ≈ …**` with prose —

```
-- check_governance CG-18: OK    CG-18  context fixtures recompute — 19 measurements examined, 0 findings
```

20 → 19, still `OK`. `build_budget_report.py --check` and `verify_final_prespec.py` both do catch it (`DRIFT: … no 'Measured:' anchor to write` and `✗ … missing 'estimate' section`), so it is not unguarded — but CG-18's own line is exactly the failure mode its neighbouring comment warns about (*"a parser that examines 4 of 8 while reporting a count is the failure mode here"*). The falsification direction works correctly (**M3**: `FAIL CG-18 … claims 111,111 words; the declared mandatory set is 14,112`).

**Repair.** Make a missing `Measured:` anchor a finding, not a skipped predicate; CG-18's denominator should be `2 × len(fixtures)`, computed and stated.

---

### 11. Hidden rules: three FAIL-severity checks encode normative editorial rules that no clause, policy or doctrine owns — **minor**

I swept the whole corpus for citations of any `CG-\d+` identifier: **70 files, 692 citations.** Not one is in `.syzygy/governance/doctrine/`, in `.syzygy/governance/policies/craft-and-care/`, or in any `rfcs/` module. The only active-lane, non-round citations are `decisions/PROCESS-LESSONS.md` (22 — explicitly *"not default context"*), the acceptance record (5), `CONTEXT-BUDGET-REPORT.md` (5), `TASK-TO-CONTRACT-INDEX.md` (4), `PENDING-OWNER-DECISIONS.md` (4), `PROJECT-STATUS.md` (2), `AGENTS.md` (2), the fixtures, `TERM-REGISTRY.md` (2), `06-CONTEXT-LOAD-MAP.md` (1), and the substrate lock (1, itself "record, never authority"). **There is no check-to-owning-clause register anywhere in the repository.** [Observed]

Most checks need none — CG-1 (links resolve), CG-7 (digests match subjects), CG-11 (ignore rules), CG-13/14 need no normative owner because they verify mechanical self-consistency. Three do:

| Check | Rule it enforces at FAIL severity | Nearest written owner |
|---|---|---|
| **CG-21** | *"a contract module states no measurement"* | None. The only prose statement I found is `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md:167` — *"Current measurement has exactly one home: `CONTEXT-BUDGET-REPORT.md`, generated"* — inside a round narrative report, not a clause. The rule's normative statement is the script's docstring: *"So the rule is now: **a contract module states no measurement.**"* [Observed] |
| **CG-20** | Same rule applied to the load map | Same — no clause. |
| **CG-22** | *"no unqualified `status` in the active lane"* | `C/policy-candidates/TERM-REGISTRY.md:162-165`, whose own line 3 reads **"Status: CANDIDATE. This file binds nothing."** and whose banner adds *"none of its 31 entries acquires force from appearing here."* [Observed] |

`verify_final_prespec.py` adds two script-local numeric rules: the hard `words > 7000` gate — the written owner says *"~7,000"* (`02-OWNER-DIRECTION-RECORD.md:47`; `COMPACTION-CHARTER.md:154`), an approximation enforced as an exact bound with an inline `JUSTIFIED_OVERSIZE` allowlist — and `total_words > 57000` (`:283`), a threshold with no written owner anywhere; it fires today (`note: total 110081 exceeds the 35–50k target band`) and is a note, never a failure, while `PASS — all checks clean` prints below it.

This is not an argument that the rules are wrong. It is that the battery cannot distinguish, in its own output, a FAIL against doctrine from a FAIL against a candidate that says it binds nothing — and a reader has no register to consult.

**Repair.** Add a `CHECK_OWNERS` table mapping each check id to its owning identifier (or the literal string `mechanical — no normative owner`, or `candidate: <path>`), print the owner alongside any FAIL, and fail the battery if a check has no entry. Route CG-20/CG-21's rule into the normative-change workflow so it acquires a clause, or downgrade both to WARN until it does.

---

### 12. `check_governance.py`'s stated portability invariant is contradicted inside the file — **minor**

`:13`: *"**Repository-relative.** The repo root is derived from this file's own location; **no founder-machine absolute path appears anywhere.**"*

Three do: `:2482` `gitpin(paths=[("/home/tze/.claude/skills/th/SKILL.md", H64)])`, `:2487` `gitpin(repo="/home/tze/.dotfiles/ai-bootstrap", …)`, `:2490` `gitpin(root="~/.claude/skills/th", …)`. [Observed] All three are inert synthetic YAML strings inside CG-19 selftest fixtures — they are the *inputs* the check must reject, and no filesystem access occurs. The behaviour is correct; the claim is false as written, in a repository whose own term registry says *"an artifact must not contradict itself in the first line and the third."*

**Repair.** One-line amendment: *"no founder-machine absolute path is ever resolved; the only ones present are inert fixture inputs CG-19 exists to reject (see F4b, F5a, F5b)."*

---

### 13. Three of the six scripts have no `--selftest` at all, and none of the generators states a denominator on `--check` — **minor**

`verify_final_prespec.py`, `build_contract_index.py` and `build_dependency_index.py` ship no mutation fixture; `build_active_manifest.py` and `build_budget_report.py` do (both pass). Their `--check` output states no population:

```
index matches regeneration — no drift
dependency index matches regeneration — no drift
```

against `check_governance.py`'s own design constraint: *"Every summary line states its denominator. A check that examined zero items reports WARN."* Both index builders `continue` silently on a module with no front-matter `id` (`build_contract_index.py:86-87`; `build_dependency_index.py:98-99`), so a corpus that lost its front matter would regenerate to a smaller index and `--check` would say "no drift" against the smaller committed file.

I did verify these scripts *can* fail — **[Observed] Mutation M11** (in the copy), removing a clause definition from `rfcs/RFC-0011/deterministic-selection-and-budget.md`, gives `verify_final_prespec.py` → `✗ … unresolved citation RFC11-16` ×4; **M1** (module byte change) gives `build_active_manifest --check` → `DRIFT: ACTIVE-CONTRACT-MANIFEST.txt` + `DRIFT: wave-manifests/WAVE-A-MANIFEST.txt`, rc=1, and `FAIL CG-7a … 2 findings`.

**Repair.** Add a `--selftest` to each (one fixture per predicate class), and print `N contracts / M modules / K clauses examined` on `--check` so a shrunken population is visible.

---

## Explicit non-findings

**Clone-path sensitivity (question 5) is clean.** [Observed] `ROOT` derives from `__file__` (`:74`); `.gitignore` is parsed rather than hardcoded (`_git_excluded_roots`, `:1431-1449`); no `os.environ`, `getenv` or `expanduser` call appears in any of the six scripts. `python3 scripts/check_governance.py` in the clone reports `scope: clone — 286 file(s) examined (286 tracked, 0 untracked-not-ignored)` and `25 OK, 15 WARN, 0 FAIL (40 checks)`, exit 0. In a git-stripped copy the walk fallback examines the same 286 files, degrades exactly one check with a printed disclosure — `WARN CG-11 ignore rules — 0 rules examined … git unavailable — ignore status is Unknown, not clean` — and reports `24 OK, 16 WARN, 0 FAIL (40 checks)`. Only `build_budget_report.head_commit()` reads git, and its output is excluded from comparison by `_without_asof`. Nothing here answers differently in a fresh clone.

**CG-7's core predicates are real.** Mutations M1, M2a and M2b each produced a `FAIL` with an accurate, specific message (quoted in findings 1 and 9). CG-7e's registration predicate — the RD-6 H-1 closure — is well-constructed: predicate 2 (an unregistered file carrying a current act digest fails) is what makes predicate 1 non-circular.

**Manifest enumeration is otherwise total.** `enumerate_modules` correctly hard-errors on a non-`.md` file under `rfcs/`, on an unknown `RFC-nnnn` directory, and on a new module inside `RFC-0010/` or `RFC-0011/` (whose per-module tables demand explicit assignment). The 39-module population matches across `ACTIVE-CONTRACT-MANIFEST.txt`, `verify_final_prespec.py`, `module_words()` and the six wave manifests (19+11+2+1+5+1 = 39, verified by row count). Finding 8 is the sole enumeration hole I found.

---

**Summary.** The validation layer is unusually strong where it was recently attacked — the act-digest population (CG-7d/7e), the substrate lock (50 fixtures), the measurement-in-prose inversions — and it fails honestly under mutation on every predicate I tested that it claims to hold. What it does not yet cover is the seam *around* the digests: the prose that describes what a digest binds (finding 1), the generated artifact that owns every measurement (finding 2), the banner on the file a reader meets first (finding 6), and its own coverage claim (finding 3). Findings 1 and 2 are the ones that would let an owner act on a false description with the documented battery green.

VERDICT: REVISE
