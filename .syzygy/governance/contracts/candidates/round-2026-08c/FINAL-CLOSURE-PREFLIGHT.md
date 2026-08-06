# Final-closure preflight — the state this round started from

> **Non-authoritative round record.** This file records what was observed at
> one commit, before any change. It accepts nothing, licenses nothing, and
> goes stale the moment the round edits anything. Where it and a current
> artifact disagree, the artifact wins and this file is a historical
> observation, correctly so.

## 1. Position

| | |
|---|---|
| Branch | `main` |
| HEAD at preflight | `cbb5253ac87dade3c1d72ef682df9fba2b1180a7` — *governance: vendor th-engineering in-tree, re-pin to close P-26 (owner override)*, committed 2026-08-07T00:38+08:00 |
| Remote | `git@github.com:Tzeusy/syzygy.git`; `origin/main` = HEAD (no divergence) |
| Working tree at preflight | clean except `.beads/*.jsonl` (tracker export, not governance) and one untracked file: this round's charter prompt |
| Tracked files | 232 total; 201 under `.syzygy/` |
| Git-excluded | `_bootstrap/`, `.syzygy/cache/`, `.syzygy/local/`, `.dolt/`, `__pycache__/`, `.beads/` local state, and the local settings file under `.claude/` |
| Lifecycle stage | final pre-specification. No `openspec/`, no accepted-contract home, no source tree. **No owner act has been performed** — `decisions/ACCEPTANCE-ACT-RECORD.md` does not exist, which is correct |

## 2. The finding this preflight exists to surface

**HEAD is red, and its CI run did not discover that.**

Two of the four steps `.github/workflows/governance-docs.yml` runs fail at
HEAD, in the working tree and reproducibly:

```text
check_governance.py           FAIL  CG-18  context fixtures recompute — 18 measurements examined, 6 findings
build_contract_index.py --check   DRIFT: 05-CONTRACT-INDEX.yaml differs from regeneration
```

Both have one cause. Commit `cbb5253` edited four owner-approved craft files
(`INSTALL-RECORD.md`, `README.md`, `engineering-bar.md`,
`testing-and-verification.md`, adding CC-TEST-7 and its cross-references) and
did not regenerate the two projections that measure those files:

- `05-CONTRACT-INDEX.yaml` carries a `governance_sources` row per craft file
  with its word count and the rule identifiers it mentions. Four rows are
  stale — e.g. `testing-and-verification.md` recorded at 1,113 words where it
  is now 1,276, and `CC-TEST-7` missing from three `rule_ids` lists.
- Context fixtures 7, 8 and 9 carry craft files in their mandatory sets, so
  each one's declared packet digest and word count moved. CG-18 reports all
  six measurements: fixture 7 claims 15,738 words against 15,784; fixture 8
  claims 22,242 against 22,405; fixture 9 claims 24,025 against 24,188.

Neither is a semantic defect. Both are the exact failure class this
repository has now shipped four times — **a derived value quoted outside its
owning artifact, gone stale silently** — and this is the first time it landed
in a *check* rather than in prose. That is an improvement: the check saw it.
Nothing else did.

### Why nothing else did: the CI run

`gh run list` shows a `governance-docs` run **does** exist for HEAD
(`31120563149`, push, 2026-08-06T16:38:54Z) and its conclusion is **failure**.
It is not a check failure. The log ends:

```text
Getting action download info
Failed to resolve action download info. Error: Service Unavailable
Retrying in 11.005 seconds
Failed to resolve action download info. Error: Service Unavailable
Retrying in 20.705 seconds
##[error]Service Unavailable
##[error]Failed to resolve action download info.
```

The job died resolving `actions/checkout@v4` and `actions/setup-python@v5`
against a GitHub service that was unavailable for ~2m45s. It never checked
out the repository and never ran a single governance check. So:

- **[Observed]** HEAD has a workflow run, and it is red.
- **[Observed]** It is red for a GitHub infrastructure reason, not a repository
  reason.
- **[Observed]** HEAD is *also* independently red on two of the four steps,
  which that run would have caught had it started.
- **[Inferred]** A reader who saw only the red X would have diagnosed the
  outage and stopped, concluding the repository was fine. It was not. Two
  independent red signals coincided and the loud one hid the quiet one.

No product tooling is added in response. The repair is to regenerate the two
projections and re-push; the durable lesson is recorded for
`PROCESS-LESSONS.md`, not fixed by machinery this phase may not build.

## 3. Check battery at HEAD — read the output, not the exit code

`python3 scripts/check_governance.py` — scope: clone, 233 files examined (232
tracked, 1 untracked-not-ignored).

**24 OK, 13 WARN, 1 FAIL (38 checks) — counts derived by the battery, not
asserted here.**

The one FAIL is CG-18, above. The 13 WARNs are all declared-by-design and each
prints its own rationale: forward references an act will create (CG-1c),
frozen-packet pointers into the git-excluded `_bootstrap/` (CG-1d), vendored
substrate scope gaps (CG-1e), two allowlists (CG-2b, CG-2d, CG-12b, CG-22b),
report-only budget and pin and vocabulary populations (CG-8, CG-19b, CG-23),
superseded records holding old digests (CG-15b), the pending register's as-of
(CG-10), and selftest coverage (CG-24).

Notable denominators, quoted from the run and not from any document:

| Check | Denominator | Result |
|---|---|---|
| CG-1b code-span path references | 1,053 references | 0 findings |
| CG-13 dependency edges | 146 edges | 0 findings |
| CG-17 surface clauses routed exactly once | 199 clauses | 0 findings |
| CG-18 context fixtures recompute | 18 measurements | **6 findings** |
| CG-20 load-map figures | 32 figures | 0 findings |
| CG-21 package README word counts | 19 figures | 0 findings |
| CG-24 selftest coverage | 24 check families | **14 of 24 have a fixture**; the 10 without are CG-1, 2, 3, 4, 5, 6, 7, 9, 10, 12 |

`verify_final_prespec.py`: **PASS** — 100,862 words across 32 modules, 328
numbered clauses defined; two standing notes (RFC-0001 over its 7,000-word
ceiling with a recorded justification; corpus total over the 35–50k target
band).

`build_dependency_index.py --check`: **no drift.**

## 4. Digests at HEAD

Snapshot only. **Do not transcribe these into an act** — three of the five
change during this round by construction, and CG-7a…d is the only correct way
to read an act argument.

| Act | Subject | Argument at HEAD |
|---|---|---|
| 1 | the 32 contract modules | `2922de1c21354ad3a804acebcfdf665d9a8986d4fa8b3df42c62169f207ed98d` (sha256 of `ACTIVE-CONTRACT-MANIFEST.txt`) |
| 2 | craft amendment CC-TEST-2 | `3858820f64768ef20e6514fe8adb28076263f071ac77e66a5520a612f3bcb26d` |
| 3 | topology bundle | `7a3b22494a08d888901c1f0cec76833dc926e89b6f510b5abf8963071fbaeb45` |
| 4 | project overview | `01d629515993188338f6a0e2d84d67543d8569003759a7c8f571a90b129c7cd1` |
| 5 | doctrine amendment D3 (optional) | `e973e8e025c93b5d1e59d16d8661b0ae1f9804304c8f8de8957950acf3d8f9c9` |

CG-7a…7d all pass at HEAD, so every quoted copy of these five agrees with its
subject. That is the state a normative edit breaks and must restore.

## 5. Raw review verdicts carried in

Copied, not summarised. `EXCEPTIONS` is not `ACCEPT`; `REVISE` is not "passed
with findings".

| Review | Commission | Verdict, copied |
|---|---|---|
| RC-1…RC-9 | the 2026-08-05b vertical battery | see each raw file; RC-7 returned **eleven blocking findings F1–F11** |
| **RC-10** | final confirming review over act 1's exact bytes | **`VERDICT: REVISE`** |
| **RC-11** | confirming review of the RC-10 repairs, same terms | **`VERDICT: REVISE`** |
| **RC-12** | independent ruling on the four context-packet budget waivers | **`VERDICT: EXCEPTIONS`** — all four ruled `WAIVER SOUND`, on a verdict whose own exceptions stand |

**Open review findings at HEAD, all inside act 1's digest set:**

- **RC11-A** — RFC10-18 cites RFC10-5 for a human resolution act RFC10-5's own
  scope excludes; the indefinite `blocked` park survives in the no-applied-
  effects case, holding its budget reservation.
- **RC11-B** — RFC10-18 pivots the correction plane on "whether effects have
  been applied" and assigns that determination to nobody: no independent party,
  no evidence tier, no Unknown rule. Rated by the reviewer the more serious of
  the two.
- **RC10-C** — RFC10-17's `spent` is "measured consumption" by nobody named,
  with no independence requirement. Also unconstrained: who declares the
  "declared maximum cost" that sizes a reservation.
- **RC10-D** — a *failed* compensating action is recorded and nothing more:
  not reclassified, not enumerated in the irreversible-effects Attention Item.
- **RC10-E / F6** — stop reaches runs and their descendants, not **child
  missions**.
- **RC10-F** — undeclared stop latency means synchronous, with no timeout, no
  failure disposition, and no Attention Item if the run will not die.
- **RC10-G** — RFC10-21's predicate keys on *mission scope* ("spanning more
  than one project"); the harm keys on *content provenance*. A single-project
  mission embedding foreign content is not reached.
- **RC10-H** — RFC10-22's own bound can suppress notice of itself: at the
  default of one outstanding item, the mission pauses and may not enqueue the
  item that says so.
- **RC-7 F4 residual** — RFC10-19 does not state the failed-run /
  completed-sibling relationship.
- **RC-10 item x** — RC-7 asked that the correction-plane clauses be inserted
  *after* act 1; they were inserted before, and the deviation is recorded in
  neither offering document.
- **RC-12 F-5** — fixture 9's declared Shard 1 is incomplete for its own
  warrant; a corrected split measures 18,943 tokens. Not installed.

All are carried as **P-27**.

## 6. Open owner items at HEAD

`decisions/PENDING-OWNER-DECISIONS.md`, as-of 2026-08-06c.

Acts: **P-1…P-5** (none performed). Open and owner-only: **P-10** (review
coverage of the routing matrix), **P-12** (knowledge-hygiene policy — two
versions offered), **P-14** (license), **P-15** (founder decision log),
**P-16** (vocabulary), **P-17** (eight public terms with no adopted
definition), **P-18** (three doctrine/contract vocabulary seams), **P-19**
(mission-envelope residuals), **P-20** (round residuals), **P-21** (contract
relation seams), **P-22** (registry authority home), **P-23** (mission stage
placement), **P-24** (D4 before act 5), **P-25** (the "README glossary"
citation), **P-27** (the RC-11/RC-12 residue above).

Resolved and recorded: P-6…P-9, P-11, P-13 (2026-08-05 round), **P-26**
(2026-08-06 owner override — `th-engineering` re-pinned to `f4cf1c7` and
vendored in-tree).

## 7. Governance CI configuration

`.github/workflows/governance-docs.yml` — `push` and `pull_request` on `main`,
`permissions: contents: read`, `ubuntu-latest`, Python 3.11. Four steps, all
read-only: `check_governance.py`, `verify_final_prespec.py`,
`build_contract_index.py --check`, `build_dependency_index.py --check`. It
installs nothing beyond a Python interpreter, by deliberate design — adding a
linter or a build here would be a stack choice requiring an accepted contract.

Recent history: 5 runs listed, 4 `success`, 1 `failure` — the failure being
HEAD's, diagnosed in §2.

## 8. Word / token measurement source at HEAD — three places, no owner

There is no single measurement artifact. Measurements are produced by four
different mechanisms and **copied into prose in at least four registers**:

| Mechanism | What it measures | Where its output is copied |
|---|---|---|
| `verify_final_prespec.py` | per-module and corpus word counts, clause counts, ceiling breaches | acceptance record §3 rows 2–3; package READMEs; `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` |
| `scripts/context_load.py` | word count × 1.35 for a **given** path list | every fixture's measurement block |
| `check_governance.py` CG-8 | context-budget report | report-only |
| `check_governance.py` CG-20 / CG-21 | load-map figures (32) and package README word counts (19), recomputed | the artifacts they police |

**[Observed]** Nineteen module-row word counts live inside act 1's digest set,
in package READMEs. Every craft or contract edit therefore moves an act
argument for a reason that has nothing to do with the contract's meaning.
CG-21 keeps them honest; it does not stop them being there. This is the
recursion Workstream F exists to end.

## 9. Contract relation metadata at HEAD — one key, three meanings

Front matter across all 32 modules carries exactly one relation key:

```text
depends_on:   present in every module
constrains:   absent — zero occurrences
cites:        absent — zero occurrences
provides_to:  absent — removed in the 2026-08-05b round, now derived by reversal
```

`build_dependency_index.py` derives the inverse (`provides_to`) from
`depends_on` and reports no drift. 146 edges resolve. The three relation
*kinds* P-21 names — load dependency, one-way semantic constraint, ordinary
citation — are all being carried by, or excluded from, the single
`depends_on` key. That is the seam Workstream B opens.

## 10. Context fixtures at HEAD

Nine fixtures, `fixtures/context-selection-1…9`. Class coverage is
eight-for-eight against the charter's required classes with no double count
(`round-2026-08b/FINAL-CONTEXT-COMPILER-FIXTURE-REPORT.md`).

- **Three are stale** (7, 8, 9) — see §2.
- **Seven still carry a fictional compiler line.** Fixtures 1, 2, 4, 5, 6, 7, 8
  end with `Compiler: context_load.py, selection rules rev10-fixtures`.
  `context_load.py` measures a set it is handed; it does not select one. The
  identifier `rev10-fixtures` resolves to nothing anywhere in the repository.
  Fixtures 3 and 9 have already dropped the line and say why.
- **Four breach the 20,000-token decomposition trigger** (2, 7, 8, 9), each now
  carrying an RC-12-signed waiver with scope and expiry — against a threshold
  (`CC-BUDGET-1`) that is installed nowhere, which RC-12 says about its own
  signature.

## 11. D3 state at HEAD

`DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` **rev1** — proposed, not adopted,
superseding `…-DRAFT.md` whose `vision.md` insertion cannot be applied as
written. Digest above. §6 discloses RC-7's F10 objection (the insertion
settles open question **D4** by stipulation) and carries the reviewer's
alternative wording, unadopted. The `architecture.md` floor as drafted omits
any maximum autonomy level. **P-24** must be ruled before act 5.

## 12. What this preflight commits the round to

1. Regenerate the two stale projections and say so in the commit that does it
   (§2) — before anything else, so the round does not build on red.
2. Repair RFC-0010 (§5's first ten items), then **freeze the bytes and
   commission a reviewer that did not author them**.
3. Open the relation key (§9) into three, and regenerate every index and
   fixture that reads it.
4. Move measurement (§8) out of active prose into one generated report that
   owns it.
5. Take the fictional compiler line off the seven fixtures that carry it (§10).
6. Leave every owner item in §6 open, and add the ones this round surfaces.

*Recorded 2026-08-06 (UTC), before the first edit of this round.*
