# Impact ledger — the Butlers source grammar written into the registry entry

> **Candidate review input — never authority.** Companion to
> `SEMANTIC-DELTA.md`. Binds nothing.

Baseline: commit `23b486c668e34d3343054e7845905edd5b85f715`. The subject is
byte-identical there and in the tree this package was drafted in.

## Discovery method

Two independent sweeps, run 2026-09-26 at the baseline (rules 2 and 9):

1. **Python `re`** over the UTF-8 text of every path from `git ls-files -z`.
   Four paths do not decode and are skipped.
2. **`git grep -l -F <identifier> HEAD`**, which does not decode.

**Denominator: 1,540 tracked files.** This package's own files were
untracked when both ran and are outside it. **The two methods agree on
every identifier and return the same file lists.** [Observed]

| Identifier | Files (both methods) |
|---|---|
| `containerShapes` | 0 |
| `classGrammar` | 0 |
| `sourceGrammarSemantics` | 0 |
| `extractionBindings` | 0 |
| `treePopulations` | 0 |
| `pillarRootTable` | 0 |
| `ProjectShapeProfile` | 5 |
| `PWB_ROOT_INDEX_PATH` | 11 |
| `extractionClassesFor` | 3 |
| `VISION_HEADINGS` | 4 |
| `V1_HEADINGS` | 4 |
| `CATALOG_HEADINGS` | 8 |
| `PWB_OBSERVER_IDENTITY` | 5 |
| `observationGrammar` | 18 |
| `registryVersion` | 8 |
| `observerVersion` | 39 |
| subject basename stem | 68 |

Six zeros: none of the new key names is used anywhere yet, so no reader
can be broken by their meaning [Observed]. `ProjectShapeProfile` occurs
only in the M8 funnel and four pursuit records — it is a designed name
with no code [Observed].

**Error term.** A name hard-wrapped inside a code span is invisible to both
sweeps. These are single tokens without separators, so a wrap is unlikely;
no join pass was run.

## Table 1 — code that must change in the adoption change

| File | Why |
|---|---|
| `packages/three-surface-poc-core/src/project-shape-observation.ts` | `PWB_OBSERVER_IDENTITY.observerVersion` must equal the entry's new value. |
| `packages/three-surface-poc-core/src/project-shape-observation.test.ts` | The parity test that enforces the line above; it fails until the constant moves, which is the check working. |
| `apps/three-surface-poc/src/governance-inputs.ts` | Names the registry act record the daemon verifies the entry's digest against. |
| `scripts/check_governance.py` | A new `PWB_EFFECT_AMENDMENT_ACTS` row with the act-time digest. |

## Table 2 — code that reads the grammar and is not changed by this act

`project-shape-extraction.ts`, `project-shape-coverage.ts` and
`apps/three-surface-poc/src/polaris.ts` cite `observationGrammar` in
comments only, and read the six existing keys through hand-copied
constants [Observed, `grep -n`]. They keep working on adoption because the
six keys are unchanged. Slice 5's fifth limb is the change that makes them
read the entry.

## Table 3 — the restated constants

The builder's second witness checks these exact lines. When limb 5 deletes
them, the witness is retired with them and limb 5's own loaded-profile
test takes its place.

| Constant | File |
|---|---|
| `PWB_ROOT_INDEX_PATH`, `PWB_INDEX_DEPTH`, `PILLAR_KEYS`, `PILLAR_LABELS`, `SOURCE_RULES` | `project-shape-manifest.ts` |
| `extractionClassesFor` (eight bindings) | `project-shape-manifest.ts` |
| `BASELINE_SPEC`, `ROSTER_BUTLER` | `project-shape-manifest.ts` |
| `VISION_HEADINGS`, `V1_HEADINGS`, `CATALOG_HEADINGS`, `DESIGN_CONTRACT_HEADING`, `CRAFT_POLICY_HEADING` | `project-shape-extraction.ts` |

## Table 4 — sibling candidates

| Package | Relation |
|---|---|
| `pwb-registry-currency-briefing-amendment/` (`syzygy-dov.18`) | Same subject; lands first. This package's diff is drafted on top of it. |
| `pwb-self-observation-acts/` (`syzygy-dov.25`, PR #120) | Drafts a second registry entry; its packet asks whether to copy `.18`'s and this package's fields. Regenerated after this act. |
| N8 container-shape amendment (`syzygy-u05.8`) | A specification amendment that would point at `containerShapes`; not yet on main. |

The builder's composition check fails if any other candidate adds a patch
to the subject.
