# Agent Instructions — Syzygy

This file is **repository operating procedure** — never citable as authority.
What the project *is* lives in `README.md` and `.syzygy/intent/OVERVIEW.md`.

## Current lifecycle stage: final pre-specification

Doctrine is adopted; engineering policy is owner-approved. Contracts,
topology, overview and the policy additions are **candidates awaiting owner
acts**. There is **no application code, no specification content, and no
implementation backlog** — none may be begun before the owner's launch
decision.

## Where authority lives

| Question | Authority | Path | Binding today? |
|---|---|---|---|
| Why — purpose, non-negotiables | Doctrine (VIS-1…7, SEC-1…5) | `.syzygy/governance/doctrine/` | **Yes** — adopted 2026-07-30, D1 in force |
| Prior owner rulings | Decisions (SDR-1…33, warrants, pending queue) | `.syzygy/governance/decisions/` | **Yes** |
| Engineering and evidence bar | Craft-and-care (CC-*) | `.syzygy/governance/policies/craft-and-care/` | **Owner-approved (D2)**; clause force begins at the acceptance acts |
| Load-bearing how | Design contracts RFC 0001–0011 | `.syzygy/governance/contracts/candidates/` | **No — candidate.** `contracts/rfcs/` exists only after the first wave act |
| Intended placement | Topology bundle | `.syzygy/map/topology-candidates/` | **No — candidate.** `map/topology/` exists only after act 3 |
| Public narrative | Overview | `.syzygy/intent/OVERVIEW.md` | Governed presentation — **never authority** |

`GOVERNANCE-SUBSTRATE-LOCK.yaml` is a record, never authority. `README.md`
carries the reader-facing view.

**Cite by identifier** — `VIS-2`, `SEC-4`, `SDR-9`, `CC-REV-3`, `RFC10-9`.
Identifiers are amended in place or retired, **never renumbered**. Candidate
clauses may be discussed, never cited as binding.

## Pending owner gates

**Thirteen acts are open; none has been performed**, and this file states no
more than that.

| Question | The one record that owns the answer |
|---|---|
| Which acts exist, their phrases, ceremony and arguments | `contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` |
| Current launch-path state — waves, gate, OpenSpec | `PROJECT-STATUS.md` |
| What each act would cost | the packet named in `decisions/README.md` |
| Process vocabulary — *act*, *argument*, *offer*, *confirmed* vs *accepted* | `PROCESS-GLOSSARY.md` |

Each digest belongs to the artifact it names, so verify with
`check_governance.py` (CG-7) before any act. **This file restates no digest
and no verdict.**

`decisions/ACCEPTANCE-ACT-RECORD.md` is created by the first act; its absence
is correct. The round-2026-08b/08c/08d offerings are superseded where
banner-marked and the retired rev9 / rev10 phrases satisfy nothing — routing
an owner to a stale offering turns act 1 into a surprised act.

## Task routing — context is compiled, never accumulated

Load the minimum for one correct decision; never "read everything."

| Your task | Start here |
|---|---|
| A doctrine question | the one doctrine file, via the `heart-and-soul` skill |
| An engineering-bar question | the one craft policy that owns it |
| A contract question | **`contracts/candidates/TASK-ROUTER.md`** — the one generated router; context-budget measurement stays with `06-CONTEXT-LOAD-MAP.md` / `scripts/context_load.py` |
| "May I implement X?" | `contracts/candidates/SURFACE-CLAUSE-ROUTING-MATRIX.md` — the answer is *no*, until accepted OpenSpec content exists |
| "How would a spec be authored?" | `contracts/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` — router only; authoring stays forbidden until the owner's launch decision |
| Current status | `PROJECT-STATUS.md` |
| "Is this ready for OpenSpec?" | **not ready**, and no formal administration has been run. `PROJECT-STATUS.md` owns the current verdict and launch target; the instrument is `launch-gate-pre-specifications.md` |
| A launch-gate administration | the record is **structured JSON** (`launch-gate-administration.schema.json`); the Markdown report is generated and **never parsed back**. Scripts: `validate_launch_administration.py`, `render_launch_administration.py`, and `launch_gate_results.py` for the historical Markdown records only |
| The launch-gate repair chain | `decisions/launch-gate/HISTORY.md` — **not default context**; the current policy is the instrument itself |
| Open owner questions | `decisions/PENDING-OWNER-DECISIONS.md` |
| Mission or Context-selection work | `contracts/candidates/DEFERRED-WAVE-POSTURE.md` first — deferred candidates route only through the router's deferred rows |
| What a term means | doctrine's glossary, `governance/doctrine/README.md`; then the candidate `policy-candidates/TERM-REGISTRY.md` |
| Maintenance, review, or avoiding a repeat mistake | `decisions/PROCESS-LESSONS.md` — **not default context** |

Historical process material lives in the git-excluded `_bootstrap/` tree and
`contracts/candidates/history/` — never on a default path, never authority.

## Hard prohibitions

Do **not**: write application or library code, or create `src/`, `apps/`,
`packages/`, UI components, or toolchain manifests; choose a language,
framework, database, or platform; create OpenSpec changesets, implementation
issues, epics, or a backlog; treat a draft, candidate, index, summary, or
generated view as authority; adopt doctrine, accept contracts, or approve
policy on the owner's behalf (VIS-4); install candidate material into an
accepted home or label it accepted; run unattended agent coordination; **edit
an artifact after an act has bound its digest.**

## Epistemic and change discipline

Label substantive claims `[Observed]`, `[Inferred]`, or `[Unknown]`. No
evidence yields Unknown — never green, never zero (VIS-2). An LLM assertion is
Inferred, never Observed. Preserve the owner's trade-offs; never smooth them
into consensus language.

Normative edits travel as **semantic deltas**
(`policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`); "editorial" and "no
semantic change" are reviewable claims. Reviews run in fresh context, given
only the artifact, its governing references and the acceptance criteria; raw
output is stored verbatim and **verdict words are copied exactly**
(`EXCEPTIONS` never becomes "pass with findings").

## Verification rules

Ten rules, each paid for by a recorded incident. The incidents are in
`decisions/PROCESS-LESSONS.md`; read them before trusting a check.

1. **`grep` here is ugrep.** `[^]]`-style classes silently match nothing. Use
   `grep -F` or Python `re` for anything load-bearing.
2. **No "zero / all / 100%" claim without running that exact sweep this
   session**, confirmed by a second method. Enumerate remainders. A mutation
   that silently stops mutating is a check that silently stops checking.
3. **Digests are scripted, never transcribed; totals are computed.** A derived
   value quoted outside its owning artifact goes stale silently.
4. **Read a check's *output*, not its exit code**, and check its denominator
   against the whole population.
5. **A citation is not a reliance** — the `RFC3-16` status banner and
   `(Shape-parallel with …)` are not dependency edges.
6. **Mutate the input and confirm the check fails**, per predicate, before
   trusting it. `--selftest` holds the fixtures.
7. **Run the battery in a clone** before calling it green; a clone report is
   valid only for the commit it was run at.
8. **Anchor a claim about a contract to a *defined clause*, and quote it.**
   Section prose near a clause is not the clause.
9. **A claim of absence needs a sweep with a denominator.** "No clause defines
   X" is a measurement. VIS-2 applies to your own claims first.
10. **Freeze the bytes a review is bound to.** Editing the subject after a
    review names its digest makes the review worth nothing, however small the
    edit. Batch the fix into the next pass.

**A generator that quotes prose has re-opened the door it closed.** Owning a
measurement means nothing inside the generated file was copied.

## Validation

All read-only; run before claiming anything is clean.

**`PROJECT-STATUS.md` §"How to verify this page" owns the canonical battery.**
Run that block, never a copy: `CG-26` compares it against hosted CI,
and nothing compares a third list. Everyday:
`python3 scripts/check_governance.py`; `--selftest` runs the fixtures (CG-24
prints coverage).

## Beads scope in this phase

`bd` tracks **process housekeeping only** — no implementation issues, epics or
backlog. Unknowns become open questions in `decisions/PENDING-OWNER-DECISIONS.md`,
not issues. Commits are documentation-only and land at stable gates; **never
commit a normative artifact while its adoption gate is unresolved.**

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

# Notes to self

- **CG-15 examines only ellipsis-marked truncated digests (`‹hex›…`) and wants
  each to prefix a *current act argument*.** An instrument/schema/§8-sub-block
  digest (bound by a *recorded decision*, not an act) FAILs it. Fix: quote the
  full 64-hex, or drop the ellipsis (`01209c0f052971f7`), or keep digests in the
  artifact's own table, not sprinkled in prose.
- **An owner may lawfully APPROVE with disclosed residuals — not a `CONFIRM`.**
  When a review pair is `REVISE` and the owner still approves (P-34 arm a),
  record "approved *with* the named residuals"; never launder to "clean" or
  imply the reviews flipped. The transaction is a recorded decision, so
  transcribing the owner's selection (provenance + verified digests + F5 y/n) is
  faithful recording, not approving for them (VIS-4).
- **Instance-vs-class is the launch-gate's signature failure:** a fix that
  closes the named *instance* and restates it as a *class property* recurs one
  address/category over (invisible strip `Cf/Cc/Mn`→`So`; 40-hex schema read→
  abbreviated commit). Only a fixture mechanical over the whole population
  (RD-66 f1's every-string-leaf sweep) held. Prefer schema-derived/allowlist
  fixtures over blocklists, and mutation-test every limb.
