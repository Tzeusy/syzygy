# Impact ledger — PWB release-label amendment

> **Candidate — binds nothing.** A census of what the amendment touches and
> what cites the requirement it amends. It decides nothing.

## Predicate and population

[Observed, computed 2026-10-03 at `0a10977b`]

- **Population:** every tracked file, 1,947 paths (`git ls-files -z`).
- **Predicate:** Python `re`, run form included:
  `PWB-REQ-(\d{3})((?:[ \t]*(?:/|,|–|\.\.|…|and)[ \t]*\d{3}\b)*)`. A file
  counts when any match's first number or any continuation number is `001`.
- **Result:** 74 files cite PWB-REQ-001.

| Area | Files | Effect of this amendment |
|---|---:|---|
| `docs/reviews/` raw reviews | 19 | None. Raw output is never edited (CC-REV-6). |
| Other `docs/` (plans, designs, evidence, pursuits) | 16 | None. Evidence records name the bytes they measured. |
| `.syzygy/governance/contracts/candidates/` sibling packages | 15 | None. Every sibling is performed or declined; none is pending against the PWB spec. The builder's sibling classification checks this. |
| `openspec/changes/polaris-project-wide-butlers-model/` | 11 | Four patched (spec, capability coverage, design, proposal) and one regenerated (`GOVERNING-DEPENDENCIES.md`). The contract-coverage matrix, parts, repair delta, `CONTRACT-COVERAGE.md` and `tasks.md` are unchanged. |
| `scripts/` | 5 | `check_spec_reconciliation.py`'s literal census changes at sign-off (17 requirements, 55 scenarios, PWB-REQ-001 at 5). The others are unchanged: the coverage and dependency builders regenerate, and the two sibling builders are history. |
| `packages/three-surface-poc-core/src/` | 5 | Implementation consumers. Sign-off authorizes no change to them. |
| `apps/three-surface-poc/src/` | 2 | The mutation sweep cites PWB-REQ-001's oracle. Sign-off authorizes no change. |
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
