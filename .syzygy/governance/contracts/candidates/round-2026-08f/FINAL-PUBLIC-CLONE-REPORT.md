# Clean-clone battery — round-2026-08f, final commit

> **A clone report is valid only for the commit it was run at** (verification
> rule 7). This one names that commit in every claim below, and states what
> it does *not* establish. It is evidence, never an act, and it grades no
> artifact's content — only whether the repository's own checks run clean
> away from the machine that authored it.

## What was run, and where

| | |
|---|---|
| **Commit** | `5e8b286f30e57bc951b45dc4adc042ceadecf32e` (`5e8b286`, branch `main`) |
| **Clone source** | `git@github.com:Tzeusy/syzygy.git` — the published remote, cloned fresh, not a copy of the working tree |
| **Date run** | 2026-08-11 |
| **Interpreter** | CPython 3.10.12 (local clone) · CPython 3.11 (hosted job, same commit) |
| **Working tree** | `git status --porcelain` → **0 lines** |

The clone is from the remote deliberately. A clone taken from the local path
would prove the checks pass over the committed objects; a clone taken from
the remote also proves the push landed and that a reader who fetches the
project gets exactly these bytes.

### What is absent in the clone, checked rather than assumed

```text
_bootstrap/                                   absent
openspec/                                     absent
src/ · apps/ · packages/                      absent
.syzygy/governance/contracts/rfcs/            absent
.syzygy/map/topology/                         absent
.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md   absent
the session's owner charter (untracked)       absent
```

Each absence is the *correct* state, and each is here because at least one of
them has been wrong before. The founder machine has a git-excluded
`_bootstrap/` tree; at one commit a check asked the local filesystem whether
it existed and passed locally while failing in a clone. The post-install
homes (`rfcs/`, `topology/`) and `ACCEPTANCE-ACT-RECORD.md` are absent
because **no owner act has been performed** — their appearance would be the
loudest possible signal that something in this repository accepted on the
owner's behalf.

## Results — the fourteen checks, verbatim

Every line below is the check's own last line of output, copied from the run.
**Read the output, not the exit code** (verification rule 4): each check
prints its own denominator, and those denominators are the point.

```text
check_governance                          30 OK, 18 WARN, 0 FAIL (48 checks) — counts derived, not asserted
verify_final_prespec                      PASS — all checks clean
build_contract_index --check              index matches regeneration — no drift over 11 contract(s), 39 of 39 module(s) carry a front-matter id, 367 clause(s), 11 implementation-boundary declaration(s)
build_dependency_index --check            dependency index matches regeneration — no drift over 39 of 39 module(s) carry a front-matter id, 11 contract(s), 176 authored `depends_on` edge(s), 8 `constrains` edge(s)
build_budget_report --check               fixture anchors and the generated report match regeneration
build_active_manifest --check             all 7 manifests match regeneration — 7 manifest(s) over 39 module(s) in 6 wave(s)
build_task_router --check                 task router matches regeneration — 13 task classes validated
build_task_router --selftest              9 fixtures, 0 failing — a check that cannot fail is not a check
check_governance --selftest               121 fixtures, 0 failing — a check that cannot fail is not a check
launch_gate_results --selftest            329 fixtures, 0 failing — a check that cannot fail is not a check
validate_launch_administration --selftest 75 fixtures, 0 failing — a check that cannot fail is not a check
render_launch_administration --selftest   12 fixtures, 0 failing — a check that cannot fail is not a check
dry-run record validates                  record valid — the verdict above is computed from the rows
dry-run report regenerable                --check: …/round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.md matches the record's rendering
```

**0 FAIL across 48 governance checks and 546 fixtures** — 121 + 329 + 75 + 12
+ 9, a sum computed here from the five lines above and belonging to no other
document.

### The eighteen WARNs are declared, not ignored

`check_governance` classifies rather than silences. Each WARN family prints
its population and its reason; none is a suppressed failure. The two that
carry findings:

- **CG-8 — context budgets, 43 artifacts examined, 15 findings.**
  Report-only by design: the §7.3 default-load figures are printed every run
  and the §11.4 triggers are decomposition prompts, not failures.
- **CG-20 — routing artifacts state no measurement, 310 lines examined, 52
  findings across 3 artifacts.** Advisory, and honestly so: the rule is
  stated only inside `check_governance.py` and has no written owner until the
  knowledge-hygiene policy (P-12) is adopted. CG-25 downgrades it for exactly
  that reason and says so in its own output.

### The coverage figure to quote, and the one never to quote

```text
CG-24  18 of 25 check families have at least one fixture
       no --selftest fixture: CG-3, CG-5, CG-6, CG-9, CG-10, CG-11, CG-12
```

`--selftest` covers **the checks that have a fixture**, not every check. The
seven families above are named here so that "121 fixtures, 0 failing" is
never read as "every check is proven". CG-24 computes this itself; the figure
is not transcribed from anywhere.

## Hosted CI — observable, and green at this commit

```text
workflow   governance-docs
run        31452287396
head       5e8b286f30e57bc951b45dc4adc042ceadecf32e
conclusion success
url        https://github.com/Tzeusy/syzygy/actions/runs/31452287396
```

All **fourteen** governance steps succeeded — the same fourteen listed above,
in the same order. The charter's `Hosted CI status: Unknown` fallback does
not fire, and nothing here is inferred from the presence of a workflow file:
the conclusion is read from the run, at this commit.

**This is a second method, not a repetition.** The hosted job runs on a
different machine, from a fresh checkout, under CPython **3.11** where the
local clone ran **3.10.12**. Two interpreters, two filesystems, same result —
which is what verification rule 2 asks for before a "0 FAIL" claim is
allowed to stand.

**Its denominator moved at this commit, and that is worth stating.** Before
`5e8b286` the hosted workflow ran **eleven** steps while `PROJECT-STATUS.md`
published a battery of **fourteen**; the three missing were the wave-manifest
drift check and the task router's drift check and selftest. The router is
this round's own new artifact, so its single hosted witness was the one
absent. A reader who took a green hosted run before this commit for "the
battery is clean" was over-reading it by three checks — including the only
one that would notice a silently misrouted reader. The lists are now one
list, and the workflow header says it must stay one list.

## What this report does not establish

It is mechanical evidence about checks, and nothing more. In particular:

- **It grades no content.** A generated index matching regeneration says the
  generator is deterministic; it says nothing about whether the contract it
  indexes is right.
- **It substitutes for none of the eight fresh-context reviews the charter
  commissioned (§14).** Zero were obtained — the authoring session could not
  spawn reviewer agents — and a passing battery is not a reader.
  `FINAL-CAPABILITY-1-READINESS-REPORT.md` records all eight as not
  dispatched.
- **It answers neither F3 nor F4.** Owner-packet comprehension and
  default-path hygiene are human judgements about human reading, and this
  pass cannot grade its own work on either. Both stand `[Unknown]`.
- **It moves no readiness conjunct.** The answer to *"Is Syzygy ready to
  author Capability 1 in OpenSpec?"* is **No**, on the eleven-conjunct
  standard, and a clean clone changes not one of them.

## Reproducing it

```sh
git clone git@github.com:Tzeusy/syzygy.git && cd syzygy
git checkout 5e8b286f30e57bc951b45dc4adc042ceadecf32e
python3 scripts/check_governance.py
python3 scripts/check_governance.py --selftest
python3 scripts/launch_gate_results.py --selftest
python3 scripts/validate_launch_administration.py --selftest
python3 scripts/render_launch_administration.py --selftest
CS=.syzygy/governance/contracts/candidates/scripts
python3 $CS/verify_final_prespec.py
python3 $CS/build_contract_index.py --check
python3 $CS/build_dependency_index.py --check
python3 $CS/build_budget_report.py --check
python3 $CS/build_active_manifest.py --check
python3 $CS/build_task_router.py --check
python3 $CS/build_task_router.py --selftest
F=.syzygy/governance/contracts/candidates/round-2026-08f/fixtures/DRY-RUN-ADMINISTRATION.json
python3 scripts/validate_launch_administration.py $F
python3 scripts/render_launch_administration.py $F --check
```

**This file is the only change made after `5e8b286`.** A clone report cannot
name the commit that contains it, so it names the commit it was run at and
declares what followed. Any later commit re-opens the question, and the
answer for that commit is whatever this battery prints there.
