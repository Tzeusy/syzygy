# Agent Instructions — Syzygy

**Syzygy** (provisional codename) is a specification-driven software control
plane. Human-readable specifications define *desired state*; code and
evidence define *observed state*; the difference becomes reconciliation work;
agent fleets are actuators that move reality toward approved intent. This
file is repository operating procedure for agents — it is not project truth
and must never be cited as authority.

## Current lifecycle stage: final pre-specification

Doctrine is adopted and engineering policy is owner-approved. The
foundational design contracts, topology, overview, and two policy additions
are **candidates awaiting explicit owner acts**. There is **no application
code, no `openspec/`, and no implementation backlog**, and none may be
created yet.

## Where authority lives

| Question | Authority | Path | Binding today? |
|---|---|---|---|
| Why — purpose, non-negotiables | Doctrine (VIS-1…7, SEC-1…5) | `.syzygy/governance/doctrine/` | **Yes** — adopted 2026-07-30, tag `doctrine-adopted-2026-07-30`, amendment D1 in force |
| Prior owner rulings | Decisions (SDR-1…33, extracted warrants, pending queue) | `.syzygy/governance/decisions/` | **Yes** |
| Engineering and evidence bar | Craft-and-care (CC-*) | `.syzygy/governance/policies/craft-and-care/` | **Owner-approved (D2)**; clause-level force begins at foundational-contract acceptance (see `INSTALL-RECORD.md`) |
| Load-bearing how | Design contracts RFC 0001–0011 | `.syzygy/governance/contracts/candidates/` | **No — candidate.** Accepted home `.syzygy/governance/contracts/rfcs/` is created only by act 1 |
| Intended placement | Topology bundle | `.syzygy/map/topology-candidates/` | **No — candidate.** Accepted home `.syzygy/map/topology/` is created only by act 3 |
| Public narrative | Overview | `.syzygy/intent/OVERVIEW.md` | Governed presentation — **never authority** |
| Required observable behavior | OpenSpec | *does not exist yet* | — |
| What exists | Code, tests, CI, runtime | *none* | — |

**Cite by identifier** — `VIS-2`, `SEC-4`, `SDR-9`, `CC-REV-3`, `RFC10-9`.
Identifiers are stable: amended in place, retired, **never renumbered**.
Candidate clauses may be discussed but never cited as binding authority.

## Pending owner gates

Five acts are open; **none has been performed**. The acceptance record in
`contracts/candidates/` owns the act phrases and the ceremony. Each digest is
owned by the artifact it names, so any quoted copy is stale the moment it
disagrees — verify with `scripts/check_governance.py` (CG-7) before any act.
This file deliberately restates no digest:

| Act | Accepts | Digest source |
|---|---|---|
| 1 | The 32 compacted foundational contract modules | `ACTIVE-CONTRACT-MANIFEST.txt` (its own sha256 is the argument) |
| 2 | Craft amendment CC-TEST-2 | `policies/craft-and-care/INSTALL-RECORD.md` current-digest block |
| 3 | The topology bundle | `.syzygy/map/topology-candidates/BUNDLE-MANIFEST.md` |
| 4 | The project overview | digest stated in the acceptance record |
| 5 (optional) | Doctrine amendment D3 — bounded missions | No digest. VIS-4 adoption of `candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` rev1, which supersedes `…-DRAFT.md`; adopt/amend/decline, no magic phrase |

The owner-facing offering — what each act covers, what is knowingly imperfect
inside it, and the round residual to read before act 1 — is
`contracts/candidates/round-2026-08/FINAL-OWNER-ACCEPTANCE-RECORD.md`.

`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` does not exist yet —
it is created by the first act, and its absence is the correct current state.
**Never edit an artifact after an act has bound its digest** — an artifact
edited after its act is, for the record, an artifact with no act. The rev9
phrase `ACCEPT FOUNDATIONAL RFCS` is retired and satisfies nothing.

## Selective reading — context is compiled, not accumulated

Load the minimum needed for one correct decision; never "read everything."

- Doctrine question → the one doctrine file, via the `heart-and-soul` skill.
- Engineering-bar question → the one craft policy that owns it.
- Contract question → start at `contracts/candidates/06-CONTEXT-LOAD-MAP.md`,
  or compute a task's load with `scripts/context_load.py` (below).
- Current status → `PROJECT-STATUS.md`; open decisions →
  `decisions/PENDING-OWNER-DECISIONS.md`.
- Historical process material lives in the git-excluded `_bootstrap/` tree
  and in `contracts/candidates/history/`. It is never on a default reading
  path and never authority; tracked files may cite `_bootstrap/**` only as
  unavailable history.

## Hard prohibitions

Do **not**:

- write application or library code; create `src/`, `apps/`, `packages/`, UI
  components, or toolchain manifests;
- choose a language, framework, database, or platform — stack choices require
  an accepted contract;
- create OpenSpec changesets, implementation issues, epics, or a backlog;
- treat a draft, candidate, index, summary, or generated view as authority;
- adopt doctrine, accept contracts, or approve policy on the owner's behalf —
  drafts are agent work, adoption is the owner's (VIS-4);
- install candidate material into an accepted home (`contracts/rfcs/`,
  `map/topology/`) or label it accepted;
- run unattended agent coordination.

## Epistemic discipline

Label substantive claims `[Observed]`, `[Inferred]`, or `[Unknown]`. No
evidence yields Unknown — never green, never zero (VIS-2). An LLM assertion
is Inferred, never Observed. Preserve the owner's actual trade-offs; never
smooth them into consensus language. Normative artifacts must pass
fresh-reader review at adoption and material amendment (VIS-3).

## Change discipline

Normative edits travel as **semantic deltas** — see
`contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`.
"Editorial" and "no semantic change" are reviewable claims. Whole-file
rewrites are exceptional and need a mapping. Reviews use fresh-context
sessions given only the artifact, its governing references, and acceptance
criteria — never the authoring conversation. Store raw reviewer output
verbatim; **copy verdict words exactly** (`EXCEPTIONS` never becomes "pass
with findings").

## Verification hazards (current, this machine)

- `grep` here is **ugrep**: `[^]]`-style classes silently match nothing. Use
  `grep -F` for literals, or Python `re` for anything load-bearing. A
  zero-result sweep supporting a universal claim needs a second method.
- Never write a "zero / all / 100%" claim without running that exact sweep in
  the same session. Enumerate remainders instead of rounding.
- Digests are scripted, never hand-transcribed; totals are computed. A fix
  batch invalidates the self-counts of every file it touches.
- **A derived value quoted for convenience is a promise.** Any copy of a
  digest or count outside its owning artifact goes stale silently: keep one
  copy, or check every copy against its source (CG-7d does this for acts).
- Copy a reviewer's verdict word, never re-label it; never edit stored raw
  reviewer output — allowlist it instead.
- In batch replacement, assert all anchors match before writing anything;
  anchors break on line wrap, so normalize whitespace or use short substrings.
- Use non-interactive flags (`cp -f`, `mv -f`, `rm -f`); aliases add `-i` and
  hang. Use absolute paths when appending under `_bootstrap/**` — it is
  git-excluded, so a stray relative write is invisible to `git status`.
- The owner sometimes runs two parallel leads: before respawning "dead"
  reviewers or editing tracked files after a resume, check the bootstrap
  checkpoint tail and recent review-file mtimes.

Incident history behind these rules:
`contracts/candidates/round-2026-08/PROCESS-LESSONS.md`.

## Validation

All read-only; run before claiming anything is clean. Read a check's
*output*, not its exit code — a PASS over zero examined items verified
nothing.

```sh
# Candidate contract package: clause continuity, citations, ceilings
python3 .syzygy/governance/contracts/candidates/scripts/verify_final_prespec.py

# Contract and dependency index drift
python3 .syzygy/governance/contracts/candidates/scripts/build_contract_index.py --check
python3 .syzygy/governance/contracts/candidates/scripts/build_dependency_index.py --check

# What one task must load (paths relative to candidates/; doctrine:/craft:
# prefixes resolve to canonical homes)
python3 .syzygy/governance/contracts/candidates/scripts/context_load.py \
  rfcs/RFC-0002/README.md doctrine:vision.md craft:engineering-bar.md

# Repository-wide governance checks (links, IDs, banners, budgets)
python3 scripts/check_governance.py
```

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

**Beads scope in this phase:** `bd` tracks process housekeeping only. Do not
create implementation issues, epics, or a product backlog; record unknowns as
open questions in the pending-decision queue, not as issues. Commits are
documentation-only, at stable gates; never commit a normative artifact while
its adoption gate is unresolved.
