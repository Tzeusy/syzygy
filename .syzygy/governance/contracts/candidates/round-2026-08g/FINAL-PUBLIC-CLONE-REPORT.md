# Clean-clone battery — round-2026-08g

> **A clone report is valid only for the commit it was run at** (verification
> rule 7). This one names that commit in every claim below and states what it
> does *not* establish. It is evidence, never an act, and it grades no
> artifact's content — only whether the repository's own checks run clean away
> from the machine that authored them.

## What was run, and where

| | |
|---|---|
| **Commit** | `ccaf95e83e944be15c314c1d1daf833df5fc050d` (`ccaf95e`, branch `main`) |
| **Clone source** | `https://github.com/Tzeusy/syzygy.git` — the published remote, cloned fresh, **not** a copy of the working tree |
| **Date run** | 2026-08-13 |
| **Interpreter** | CPython 3.10.12 (local clone) · the hosted job's own Python at the same commit |
| **Working tree in the clone** | `git status --porcelain` → **0 lines** |
| **Tracked files** | 429 |

The clone is taken from the remote deliberately. A clone from the local path
proves the checks pass over the committed objects; a clone from the remote
also proves the push landed and that a reader who fetches the project gets
exactly these bytes. Both were run this session — the local-path clone first,
the public clone second — and they agree.

### What is absent in the clone, checked rather than assumed

```text
_bootstrap/                                             absent
openspec/                                               absent
src/ · apps/ · packages/                                absent
.syzygy/governance/contracts/rfcs/                      absent
.syzygy/map/topology/                                   absent
.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md   absent
the session's owner charter (untracked by instruction)  absent
```

Each absence is the *correct* state and each is checked because at least one
has been wrong before. The post-install homes (`rfcs/`, `topology/`) and
`ACCEPTANCE-ACT-RECORD.md` are absent because **no owner act has been
performed** — their appearance would be the loudest possible signal that
something here accepted on the owner's behalf.

### What is present, checked because it is new

```text
CAPABILITY-1-CHARTER.yaml                 present
CAPABILITY-1-GENERATED-VIEWS.md           present
scripts/build_capability_1_views.py       present
```

The Capability 1 generator reads the charter, the contract index and the
pending-decisions queue, and writes two files. A generator that resolved a
founder-local path would pass in the working tree and fail here; it does not.

## Results — the sixteen checks

**All sixteen exit `0` in the public clone.** The counts the four
count-printing checks report there are identical to the working tree:

```text
scripts/check_governance.py            32 OK, 18 WARN, 0 FAIL (50 checks)
scripts/check_governance.py --selftest              149 fixtures, 0 failing
scripts/launch_gate_results.py --selftest           329 fixtures, 0 failing
build_capability_1_views.py --check   6 rows, 29 clauses, 13 blocking decisions
```

The remaining twelve print regeneration or validity statements rather than
counts; each was run and each exited `0`. The battery's canonical list is
`PROJECT-STATUS.md` §"How to verify this page", and `CG-26` is what asserts
that list equals the hosted one — this report does not restate either list.

## Hosted CI at this exact commit

**A hosted run exists for `ccaf95e` and it succeeded.**

| | |
|---|---|
| Workflow | `governance-docs` |
| Run | `31707657489` |
| Head SHA | `ccaf95e83e944be15c314c1d1daf833df5fc050d` |
| Conclusion | **success** |
| Steps | **16 check steps**, every one `success` |

The step list was read from the run itself, not from the workflow file, and it
matches the published battery one-for-one. `CG-26` checks the *files* agree;
this checks that the run that actually happened did what the file says.

### Two red runs immediately before, and why they were red

`[Observed]` from the same run list: `10f41a8` and `128eb79` both concluded
**failure** on 2026-08-13. Both were caused by one thing — `10f41a8` untracked
`.beads/issues.jsonl`, and a launch-gate fixture was bound to that path, so
`validate_launch_administration.py --selftest` reported `101 fixtures, 1
failing`. It was repaired in `622481a` by repointing the fixture to a path
that exists at HEAD, and the three runs since have all been green.

This is recorded rather than passed over because it is the *only* evidence in
this report that the hosted battery can go red at all, and a check that has
never failed in CI is a check nobody has watched fail.

## What this report does not establish

- **It does not grade any artifact's content.** Every check here is
  structural: paths resolve, digests recompute, generated views match their
  sources, fixtures discriminate. Nothing here says a contract clause is
  *right*.
- **It does not make the repository ready for anything.** The launch gate has
  never been formally administered, and green checks are not a `READY`
  verdict. `PROJECT-STATUS.md` owns that state.
- **It is valid for `ccaf95e` and no other commit.** Any commit after this one
  needs its own run. That is verification rule 7, and it is the reason this
  file names the commit six times rather than saying "current".
- **`0 FAIL` is not `0 WARN`.** Eighteen checks warn at this commit, including
  three advisory downgrades whose rules have no binding home. The warnings are
  printed with their denominators on every run; read the output, not the
  summary line.
