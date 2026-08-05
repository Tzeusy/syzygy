# Agent Instructions — Syzygy

**Syzygy** (provisional codename) is a specification-driven software control
plane: specifications define *desired state*, evidence defines *observed
state*, the difference becomes reconciliation work, and agent fleets are
actuators that close it. This file is **repository operating procedure** — not
project truth, and never citable as authority.

## Current lifecycle stage: final pre-specification

Doctrine is adopted; engineering policy is owner-approved. The foundational
design contracts, topology, overview, and two policy additions are
**candidates awaiting explicit owner acts**. There is **no application code,
no `openspec/`, and no implementation backlog** — and none may be created.

## Where authority lives

| Question | Authority | Path | Binding today? |
|---|---|---|---|
| Why — purpose, non-negotiables | Doctrine (VIS-1…7, SEC-1…5) | `.syzygy/governance/doctrine/` | **Yes** — adopted 2026-07-30, tag `doctrine-adopted-2026-07-30`, D1 in force |
| Prior owner rulings | Decisions (SDR-1…33, warrants, pending queue) | `.syzygy/governance/decisions/` | **Yes** |
| Engineering and evidence bar | Craft-and-care (CC-*) | `.syzygy/governance/policies/craft-and-care/` | **Owner-approved (D2)**; clause force begins at act 1 |
| External baselines adopted by reference | Substrate lock | `.syzygy/governance/policies/GOVERNANCE-SUBSTRATE-LOCK.yaml` | Record, never authority |
| Load-bearing how | Design contracts RFC 0001–0011 | `.syzygy/governance/contracts/candidates/` | **No — candidate.** `contracts/rfcs/` is created only by act 1 |
| Intended placement | Topology bundle | `.syzygy/map/topology-candidates/` | **No — candidate.** `map/topology/` is created only by act 3 |
| Public narrative | Overview | `.syzygy/intent/OVERVIEW.md` | Governed presentation — **never authority** |
| Required observable behavior | OpenSpec | *does not exist yet* | — |
| What exists | Code, tests, CI, runtime | *none* | — |

**Cite by identifier** — `VIS-2`, `SEC-4`, `SDR-9`, `CC-REV-3`, `RFC10-9`.
Identifiers are amended in place or retired, **never renumbered**. Candidate
clauses may be discussed, never cited as binding.

## Pending owner gates

Five acts are open; **none has been performed**. The acceptance record owns
the phrases and the ceremony. Each digest belongs to the artifact it names, so
any quoted copy is stale the moment it disagrees — verify with
`check_governance.py` (CG-7) before any act. This file restates no digest.

| Act | Accepts | Digest source |
|---|---|---|
| 1 | The 32 compacted foundational contract modules | `ACTIVE-CONTRACT-MANIFEST.txt` |
| 2 | Craft amendment CC-TEST-2 | `craft-and-care/INSTALL-RECORD.md` |
| 3 | The topology bundle | `topology-candidates/BUNDLE-MANIFEST.md` |
| 4 | The project overview | the acceptance record |
| 5 (optional) | Doctrine amendment D3 — bounded missions | none — VIS-4 adoption of the D3 packet, rev1 |

The owner-facing offering is
`contracts/candidates/round-2026-08b/FINAL-OWNER-ACCEPTANCE-RECORD.md`.
`decisions/ACCEPTANCE-ACT-RECORD.md` does not exist yet — it is created by the
first act, and its absence is correct. **Never edit an artifact after an act
has bound its digest.** The rev9 phrase `ACCEPT FOUNDATIONAL RFCS` is retired
and satisfies nothing.

## Task routing — context is compiled, never accumulated

Load the minimum for one correct decision. Never "read everything."

| Your task | Start here |
|---|---|
| A doctrine question | the one doctrine file, via the `heart-and-soul` skill |
| An engineering-bar question | the one craft policy that owns it |
| A contract question | `contracts/candidates/06-CONTEXT-LOAD-MAP.md`, or compute the load with `scripts/context_load.py` |
| "May I implement X?" | `contracts/candidates/SURFACE-CLAUSE-ROUTING-MATRIX.md` — the answer is *no*, until OpenSpec exists |
| Current status | `PROJECT-STATUS.md` |
| "Is this ready for OpenSpec?" | `round-2026-08b/FINAL-PRE-SPECIFICATION-READINESS-REPORT.md` — the answer is **not ready**, with the two unmet criteria named |
| Open owner questions | `decisions/PENDING-OWNER-DECISIONS.md` |
| What a term means | doctrine's glossary, `governance/doctrine/README.md`; then the candidate `policy-candidates/TERM-REGISTRY.md` |
| Maintenance, review, or avoiding a repeat mistake | `decisions/PROCESS-LESSONS.md` — **not default context** |

Historical process material lives in the git-excluded `_bootstrap/` tree and
in `contracts/candidates/history/`: never on a default path, never authority.

## Hard prohibitions

Do **not**: write application or library code, or create `src/`, `apps/`,
`packages/`, UI components, or toolchain manifests; choose a language,
framework, database, or platform; create OpenSpec changesets, implementation
issues, epics, or a backlog; treat a draft, candidate, index, summary, or
generated view as authority; adopt doctrine, accept contracts, or approve
policy on the owner's behalf (VIS-4); install candidate material into an
accepted home or label it accepted; run unattended agent coordination.

## Epistemic and change discipline

Label substantive claims `[Observed]`, `[Inferred]`, or `[Unknown]`. No
evidence yields Unknown — never green, never zero (VIS-2). An LLM assertion is
Inferred, never Observed. Preserve the owner's actual trade-offs; never smooth
them into consensus language.

Normative edits travel as **semantic deltas**
(`policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`); "editorial" and "no
semantic change" are reviewable claims. Reviews run in fresh-context sessions
given only the artifact, its governing references, and acceptance criteria —
never the authoring conversation. Store raw reviewer output verbatim and
**copy verdict words exactly** (`EXCEPTIONS` never becomes "pass with
findings").

## Verification rules

Each was paid for by a recorded incident (`decisions/PROCESS-LESSONS.md`):

1. **`grep` here is ugrep** — `[^]]`-style classes silently match nothing. Use
   `grep -F` or Python `re` for anything load-bearing.
2. **Never write a "zero / all / 100%" claim without running that exact sweep
   in the same session**, confirmed by a second method. Enumerate remainders.
3. **Digests are scripted, never transcribed; totals are computed.** A derived
   value quoted outside its owning artifact goes stale silently.
4. **Read a check's *output*, not its exit code.** A PASS over zero examined
   items verified nothing — and a green drift check can sit over a knowingly
   inconsistent graph.
5. **A citation is not a reliance.** Two shapes look like dependencies and
   are not: the boilerplate `RFC3-16` status banner every module carries, and
   the `(Shape-parallel with …)` parenthetical. Both fooled a dependency
   sweep here; four wrong edges shipped before a reviewer caught them.
6. **Before writing a new check, decide what would make it fail** — then make
   it fail. `--selftest` holds one fixture per check for this reason. Two
   checks in this repository reported OK over **zero** examined items.
7. **Run the battery in a clone before claiming it is green.** The working
   tree has the git-excluded `_bootstrap/`, absent from every clone. A check
   that resolves paths against local disk verifies the machine, not the
   repository — one did, and read a founder-only ceremony step as executable.
   Clone reports are valid only for the commit they were run at; re-run them,
   never patch their figures.

## Validation

All read-only; run before claiming anything is clean.

```sh
python3 scripts/check_governance.py                       # repo-wide
python3 scripts/check_governance.py --selftest            # each check shown able to fail
CS=.syzygy/governance/contracts/candidates/scripts
python3 $CS/verify_final_prespec.py                       # clauses, citations, ceilings
python3 $CS/build_contract_index.py --check               # index drift
python3 $CS/build_dependency_index.py --check             # dependency-edge drift
python3 $CS/context_load.py rfcs/RFC-0002/README.md doctrine:vision.md
```

## Beads scope in this phase

`bd` tracks **process housekeeping only**: no implementation issues, epics, or
product backlog. Record unknowns as open questions in
`decisions/PENDING-OWNER-DECISIONS.md`, not as issues. Commits are
documentation-only and land at stable gates; **never commit a normative
artifact while its adoption gate is unresolved.**

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:7510c1e2 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
