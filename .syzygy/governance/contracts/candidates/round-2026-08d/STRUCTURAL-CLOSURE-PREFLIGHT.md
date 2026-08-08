# Structural-closure preflight — round 2026-08d

> **Historical record — frozen at commit `565aff7`.** Every digest quoted
> below is the value current *at preflight time*; the round this preflight
> opens edits the measured artifacts, so these values are expected to go
> stale and are preserved as the before-state, never as a live offer.

> Session preflight for the structural contract decomposition pass
> (owner work order: `syzygy_claude_structural_contract_decomposition_prompt.md`,
> untracked at session start). Recorded before any edit. Every figure below was
> measured this session at the stated HEAD; none is copied from an earlier
> report. This file is a process record, never authority.

## Repository state at session start

| Fact | Value | How established |
|---|---|---|
| Branch | `main` | `git branch --show-current` [Observed] |
| HEAD | `565aff7948b0c7f20122f0f80e545d463cb2025c` | `git rev-parse HEAD` [Observed] |
| Remote | local `main` == `origin/main` (nothing unpushed, nothing behind) | `git log origin/main..main` and inverse, both empty after fetch [Observed] |
| Working tree | `.beads/issues.jsonl` modified; `syzygy_claude_structural_contract_decomposition_prompt.md` untracked; nothing else | `git status --porcelain` [Observed] |
| Tags | `doctrine-adopted-2026-07-30` (sole tag) | `git tag --list` [Observed] |

## Candidate RFC module population

32 modules under `contracts/candidates/rfcs/` — RFC-0001 (1 file), RFC-0002
(5), RFC-0003 (3), RFC-0004 (5), RFC-0005 (4), RFC-0006 (1), RFC-0007 (3),
RFC-0008 (4), RFC-0009 (4), RFC-0010 (1), RFC-0011 (1). `find rfcs -name
'*.md' | sort` this session matches `ACTIVE-CONTRACT-MANIFEST.txt`'s
population exactly. [Observed]

`ACTIVE-CONTRACT-MANIFEST.txt` digest, computed this session by `sha256sum`:
`2862b2f54e39e6d477129147eb2e1d0cb4ca714c26edabd75505e2e38ff057d7` — matches
the act-1 argument quoted in
`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` (rev10). [Observed]

## Acceptance gates at session start

Five acts in `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`; **none
performed**; `decisions/ACCEPTANCE-ACT-RECORD.md` does not exist, which is
the correct state. Act 1 is monolithic: one phrase binds all 32 modules
(RFC 0001–0011) at one manifest digest. The owner work order for this pass
directs that the all-in-one act 1 **not** be performed and that the package
be decomposed into independently digest-bound acceptance waves. [Observed]

## Raw review verdicts in force (round-2026-08c, exact words)

| Review | Verdict |
|---|---|
| RD-1 (mission-safety confirming) | `REVISE` |
| RD-1b (mission-safety) | `REVISE` |
| RD-1b (mission-safety confirming) | `REVISE` |
| RD-2 (human clarity) | `REVISE` |
| RD-3 (vocabulary) | `REVISE` |
| RD-4 (contract relations) | `REVISE` |
| RD-5 (context selection) | `REVISE` |
| RD-6 (source of truth) | `REVISE` |
| RD-7 (public clone) | `EXCEPTIONS` |
| RD-8 (exact manifest) | `REVISE` |

Extracted from `# VERDICT` blocks of the raw files under
`round-2026-08c/reviews/` this session; words copied exactly. **No CONFIRM
verdict is bound to the currently offered bytes.** [Observed]

## Open owner decisions

`decisions/PENDING-OWNER-DECISIONS.md` "Open, and only the owner can
dispose": P-10, P-12, P-14, P-15, P-16, P-17, P-18, P-19, P-21 (with
sub-question c′), P-22, P-23, P-24, P-25, P-27, P-28 — fifteen open items.
[Observed]

## Beads process issues

Four open, none in progress, none blocked: `syzygy-5fj` (P1 — split the
RFC-0010 package, repair the six blocking Mission-safety findings),
`syzygy-kyt` (P1 — make RFC11-4 satisfiable and the golden fixtures
testable), `syzygy-0wf` (P2 — route the fourteen open source-of-truth
findings), `syzygy-vky` (P2 — close the reference defects act 1 would bind
or break). These are the previous round's filing of exactly the work this
pass's owner direction orders. [Observed]

## Governance CI / workflow state

- Workflow: `.github/workflows/governance-docs.yml` — push/PR on `main`,
  runs the four read-only checkers. [Observed]
- Last **green** hosted run: 2026-08-06T04:06Z (run 31070314563). The two
  runs after it (31120563149, 31127270334; 2026-08-06) **failed on runner
  acquisition** — annotation: "The job was not acquired by Runner of type
  hosted even after multiple attempts" — an infrastructure failure, not a
  check failure. [Observed]
- **No hosted run exists for any of the three 2026-08-07 commits**
  (`c70540e`, `99e141a`, `565aff7`/HEAD). Hosted-check status for HEAD is
  therefore **Unknown** — the workflow file's presence is not a green run.
  [Observed]

## Battery output at HEAD (this session, working tree)

- `check_governance.py`: **24 OK, 14 WARN, 2 FAIL** (40 checks). Both FAILs
  are CG-22 (unqualified `status` code spans) inside the untracked owner
  work-order file at repo root — not in any governed artifact. The 14 WARNs
  are the declared-by-design report-only families. [Observed]
- `check_governance.py --selftest`: 77 fixtures, 0 failing; CG-24 reports
  **16 of 24 check families have at least one fixture** (uncovered: CG-1,
  CG-2, CG-3, CG-4, CG-5, CG-6, CG-9, CG-10). [Observed]
- `verify_final_prespec.py`: **PASS** — 328 numbered clauses; RFC-0001 over
  the 7,000-word ceiling with recorded justification; total 102,623 words
  over the 35–50k target band, owner-facing justification required per
  charter. [Observed]
- `build_contract_index.py --check`, `build_dependency_index.py --check`,
  `build_budget_report.py --check`: all clean, no drift. [Observed]

## Fixture population

`contracts/candidates/fixtures/`: nine context-selection fixtures
(`context-selection-1…9`) plus `semantic-equivalence-fixtures.md`.
**The fixtures are not members of `ACTIVE-CONTRACT-MANIFEST.txt`** — the
manifest enumerates `rfcs/**` only (header regeneration command scopes to
`find rfcs`). Act 1's scope statement in the acceptance record confirms:
"not history/, not fixtures/, not the reports." Repairing fixtures therefore
does not move any act digest. [Observed]

## Clone-verification currency

`round-2026-08c/FINAL-PUBLIC-CLONE-REPORT.md` is bound to commit `99e141a`.
HEAD (`565aff7`) changed only `.beads/*` and the clone report file itself —
no governed or validation artifact — so the clone result's coverage carries
to HEAD's governed corpus, while remaining formally a report about
`99e141a`. A new clone run is owed at this pass's close in any case.
[Observed]

## Explicit verifications the work order demands

| Question | Answer |
|---|---|
| Does the current clone report apply to current HEAD? | Formally no (bound to `99e141a`); materially yes (HEAD changed no governed artifact — file list above). A fresh clone run is owed at this pass's close. [Observed] |
| Did hosted CI run for current HEAD? | **No run exists.** Unknown, not green. [Observed] |
| Is every act argument generated or reproducibly derived? | The manifest is reproducible by the header's `find \| sha256sum` command, but there is **no checked-in generator with `--check` mode and negative fixtures**; act arguments in the acceptance record are hand-quoted from the manifest (CG-7 verifies the copies). Reproducibly derived: yes. Generated by a guarded script: no. Workstream G owes the generator. [Observed] |
| Does the candidate package README describe the current package? | Deferred to the source-of-truth inventory (RD-6/RD-8 found it stale in places); answered in this round's source-of-truth closure work. [Unknown at preflight] |
| Are fixtures in the RFC manifest? | No (see above) — so the "frozen under act-1 digest" premise for not repairing them is false, exactly as the work order states. [Observed] |
| Does the install simulation preserve internal links? | **No install simulation has ever been run.** No post-install link report exists anywhere under `candidates/`. Unknown; Workstream A §8.7 owes it. [Observed — absence, swept `candidates/` for `*INSTALL*` and `*LINK*` reports, zero matches] |

## Known blocking defects carried into this pass (from PROJECT-STATUS.md, verified against owning records)

1. **Mission safety not closed** — RFC10-10's prevention MUST vs RFC10-17's
   ledger-only invariant; RFC-0010 frozen at its current digest because two
   reviews bind those bytes. This pass splits the package (per RFC-0010 §4's
   own naming of the split) and repairs the findings in the split modules —
   review rule 10's "batch the fix into the next pass" is satisfied: this is
   the next pass.
2. **Deterministic context selection unsatisfiable** — RFC11-4 demands the
   phase-rule clause of every selected contract; RFC 0001–0005 have none, so
   a conformant selector fail-closes on all nine fixtures. RFC11-4 also still
   names the deleted `provides_to` key among selection inputs, and does not
   name `constrains` (P-21 c′).

## What this pass will not do

No owner act is performed; no OpenSpec changeset, product bead, stack
choice, or application code is created; no adopted doctrine is edited. Stop
is at exact prepared gates.
