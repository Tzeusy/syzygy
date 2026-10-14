# Impact ledger — PWB release-label amendment

> **Candidate — binds nothing.** A census of what the amendment touches and
> what cites the requirement it amends. It decides nothing.

## Predicate and population

[Observed, re-measured 2026-10-14 at `8f1fbec7` for the round-2 repair]

- **Population:** every tracked file at that commit, 2,658 paths
  (`git ls-tree -r -z --name-only 8f1fbec7`).
- **Predicate:** Python `re`, run form included:
  `PWB-REQ-(\d{3})((?:[ \t]*(?:/|,|–|\.\.|…|and)[ \t]*\d{3}\b)*)`. A file
  counts when any match's first number or any continuation number is `001`.
- **Result:** 95 files cite PWB-REQ-001. The same script at `0a10977b` gives
  1,947 paths and 74 files, the figures this ledger first published on
  2026-10-03.
- **Second method, implementation files only:** `git grep -l PWB-REQ-001`
  over `apps` and `packages` gives 8 files at `8f1fbec7` and 7 at
  `0a10977b`, equal to the script's rows below.

| Area | Files | Effect of this amendment |
|---|---:|---|
| `docs/reviews/` | 21 | None. Raw output is never edited (CC-REV-6). Two of them are this package's round-1 and round-2 raws. |
| Other `docs/` (plans, designs, evidence, pursuits) | 17 | None. Evidence records name the bytes they measured. |
| `.syzygy/governance/contracts/candidates/` | 29 | Nine are this package's own files. Four are files of three pending PWB packages: the accessible-name, class-granular (two files) and opening-index amendments, which name this package as a pending sibling; each of their builders' `--check`, which composes every pending spec patch in every order, passes over the repaired spec patch. One is the SEC-3 doctrine amendment's ledger, which cites PWB-REQ-001 and does not patch the PWB spec. The other fifteen belong to performed packages and repins: none. |
| `openspec/changes/polaris-project-wide-butlers-model/` | 11 | Five patched (spec, capability coverage, design, proposal, contract-coverage repair delta) and two regenerated (`GOVERNING-DEPENDENCIES.md`, `CONTRACT-COVERAGE.md`). The three matrix files, the three parts files and `tasks.md` are unchanged. |
| `scripts/` | 7 | At sign-off, `check_spec_reconciliation.py` changes twice: its literal census (17 requirements, 55 scenarios, PWB-REQ-001 at 5) and the PWB child's successor chain. This package's builder is the guard itself. The others are unchanged: the coverage and dependency builders regenerate, and the three sibling builders are history. |
| `packages/three-surface-poc-core/src/` | 5 | Implementation consumers. Sign-off authorizes no change to them. |
| `apps/three-surface-poc/src/` | 3 | The mutation sweep (two files) cites PWB-REQ-001's oracle, and `polaris-reconciliation.test.ts` cites the requirement. Sign-off authorizes no change. |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 1 | Register row P-85 itself. |
| `AGENTS.md` | 1 | None. |

## Files a later implementation would touch

[Inferred — named for planning, not authorized]

- **Observer.** `apps/three-surface-poc/src/git-observation.ts` captures only
  `rev-parse HEAD` today (lines 62 and 106). It needs the tag set and commit
  ancestry, but only after the registry entry admits them.
- **Model.** `packages/three-surface-poc-core/src/project-shape-observation.ts`
  and `project-shape-model.ts` need the label value.
- **Polaris rendering.** It needs the label with the full object id beneath.
- **Not covered by this package.** `apps/three-surface-poc/src/page-shell.ts`
  line 41 renders the project revision in the footer shared by all surfaces,
  and `apps/three-surface-poc/src/orrery.ts` line 187 renders it in Orrery's
  eyebrow. Both are POC-governed on Trajectory and Orrery.

## Registry entry

[Observed]
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
admits no tag ref and no commit-ancestry input. This package does not edit it.
See `SEMANTIC-DELTA.md` §"The read the owner's direction did not see".
