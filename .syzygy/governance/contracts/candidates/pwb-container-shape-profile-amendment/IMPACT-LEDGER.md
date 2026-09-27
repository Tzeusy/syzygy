# Impact ledger — each project's profile declares its container shapes

> **Candidate review input — never authority.** Companion to
> `SEMANTIC-DELTA.md`. Binds nothing.

Baseline: commit `23b486c668e34d3343054e7845905edd5b85f715`. The subject is
byte-identical there and in the tree this package was drafted in.

## Discovery method

Two independent sweeps, run 2026-09-27 at the baseline (rules 2 and 9):

1. **Python `re`** over the UTF-8 text of every path from
   `git ls-tree -r -z --name-only HEAD`, read from the worktree. Four paths
   do not decode and are skipped. The three phrases in lower case below were
   matched ignoring case.
2. **`git grep -l -F <identifier> HEAD`** (with `-i` for the same three).

**Denominator: 1,540 tracked files.** This package's own files were
untracked when both ran and are outside it.

| Identifier | Python `re` | `git grep` |
|---|---|---|
| `PWB-REQ-002` | 49 | 48 |
| `heading-section` | 2 | 2 |
| `every-level-2-section` | 0 | 0 |
| `top-level-decimal-list` | 0 | 0 |
| `top-level-list` | 0 | 0 |
| `top-level-bulleted-list` | 0 | 0 |
| `first-table-rows` | 0 | 0 |
| `ordinal-section-table-rows` | 0 | 0 |
| `tree-path` | 0 | 0 |
| `toml-table-field` | 0 | 0 |
| `containerShapes` | 0 | 0 |
| project profile | 7 | 7 |
| key form | 1 | 1 |
| container shape | 11 | 11 |
| the sign-off phrase | 1 | 0 |

**The two differences are accounted for** [Observed]:

- `PWB-REQ-002`: the Python sweep reads the worktree, where this package's
  registration comment in `scripts/check_governance.py` names the
  requirement; `git grep` reads `HEAD`. Without that file the two lists are
  identical. (A plain worktree `grep -rlF` missed
  `project-shape-coverage.test.ts`; both methods above list it.)
- The sign-off phrase: the same registration, present only in the worktree.

**Error term.** A name hard-wrapped inside a code span is invisible to both
sweeps. The shape names are single hyphenated tokens; no join pass was run.

## What the counts mean

- **The nine shape names are unused.** Only `heading-section` occurs, twice,
  in the 2026-09-22 pursuit's data and harvest records, as one of the L1-M1
  move's proposed shape names [Observed]. No reader can be broken by their
  meaning.
- **"Container shape"** occurs in eleven files: the sitting record; the
  2026-09-22 pursuit's report, data and harvest; the N8 synthetic-corpus
  code, fixture, test, runner and evidence; the N8 slice 2 review raw; and
  `round-2026-08e/reviews/RD-45-instrument-v117-RAW.md`. All but the last
  use it in this draft's sense; RD-45 means an HTML container (a blockquote
  or list item) [Observed, read at the review hits; the code and pursuit
  hits were read by name only].
- **"Project profile" collides twice** [Observed]:
  - RFC 0005 (accepted and candidate copies, `README.md` line 86 and
    `execution-profiles.md` line 31) uses "a per-project profile" for a SEC-3
    execution profile — what a project's code may run, not how it is read.
  - The subject's own `contract-coverage-matrix/RFC-0007-0009.md` row
    `RFC7-5.c3` says "External-project POC does not bootstrap a
    governed-project profile" — RFC 0007's presentation profile.

  Neither is the thing this draft names. Packet question 9 asks whether to
  rename.
- **"Key form"** occurs once, in a review raw, in an unrelated sense.

## Table 1 — the subject

| File | Change |
|---|---|
| `specs/polaris-project-wide-butlers-model/spec.md` | Reader definitions and `PWB-REQ-002`, by `spec.md.patch`. |
| `GOVERNING-DEPENDENCIES.md` | Regenerated; only the specification digest moves. |
| `CAPABILITY-COVERAGE.md` | Row 4 reworded; totals unchanged at 31. |
| `CONTRACT-COVERAGE.md`, three matrix parts | Regenerate byte-identical (checked). |
| `proposal.md`, `design.md`, `.openspec.yaml`, `CONTRACT-COVERAGE-REPAIR-DELTA.md` | Unchanged. |

## Table 2 — code that cites `PWB-REQ-002` and is not changed by this act

| File | Why it keeps working |
|---|---|
| `packages/three-surface-poc-core/src/project-shape-extraction.ts` and its test | Reads Butlers through built-in constants equal to the Butlers profile. It does not load a profile; that is the disclosed gap (Semantic delta, impact 1). |
| `packages/three-surface-poc-core/src/project-shape-coverage.ts` and its test | Counts what extraction yields; unchanged. |
| `packages/three-surface-poc-core/src/synthetic-corpus-coverage.ts` | N8's synthetic census. Measures cells; asserts no conformance. |
| `apps/three-surface-poc/src/pwb-mutation-sweep.ts`, `pwb-n8-synthetic-corpus-coverage-matrix-main.ts` | Tooling; unchanged. |
| `scripts/record_pwb_behavior_amendment_acts.py` | Out of scope for this lane; not touched. |

The remaining citers are specifications, reviews, evidence, plans and
pursuit records, which quote the requirement and are not re-read by code.

## Table 3 — governed records whose pins go stale on adoption

| Record | Pin |
|---|---|
| `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` | `governingBehaviorContract` names today's `spec.md` digest. |
| `.syzygy/governance/policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` | The same pin. |

Every adopted specification successor stales both; this package does not
repair them.

## Table 4 — sibling candidates

| Package | Relation |
|---|---|
| `.21`, `.30`, `.22`, lane B, `.20` | Specification acts that land first. Each collides on `GOVERNING-DEPENDENCIES.md`; `.30` and `.20` also edit `CAPABILITY-COVERAGE.md` in rows that compose with row 4. This manifest is regenerated with `--write` after each. |
| `pwb-dismissal-expiry-amendment/` (`syzygy-dov.29`, PR #121) | Also proposes to land last; composes on `spec.md` (different requirement), collides on `GOVERNING-DEPENDENCIES.md`. |
| `pwb-registry-loaded-profile-amendment/` (`syzygy-dov.24`, PR #123) | Drafts the registry fields a profile would live in. Its specification witness checks heading texts in the reader definitions; with this package's `spec.md.patch` applied in its worktree, its `--check` still passed [Observed, 2026-09-27, at PR #123's head `31305bc`]. |
| `pwb-self-observation-acts/` (`syzygy-dov.25`, PR #120) | A second project's registry entry; would need a profile under this text. |

The builder's `--check` applies every shared patch in both orders against
each sibling's `proposed/` directory and compares the result with twelve
declared outcomes; a missing sibling directory is a finding.
