# Impact ledger — the Butlers source grammar written into the registry entry

> **Candidate review input — never authority.** Companion to
> `SEMANTIC-DELTA.md`. Binds nothing.

Baseline: commit `08d4d023e0d3a12d0be21fe76550442607e70f4e`, the tip of
`main` this revision is rebased onto. The subject is byte-identical there
and in the tree this package was drafted in. (Round 1 used `23b486c`; its
table is replaced, not amended.)

## Discovery method

Two independent sweeps, run 2026-09-27 at the baseline (rules 2 and 9):

1. **Python `re`** over the UTF-8 text of every file in `git archive` of
   the baseline, matching the name as a whole word (not preceded or
   followed by a letter, digit or underscore). Four files do not decode
   and are skipped.
2. **`git grep -l -w -F <name> 08d4d02`**, which does not decode.

**Denominator: 1,545 tracked files** (1,541 decoded, 4 not). This
package's own files are not on `main` and are outside it. **The two
methods return the same file list for every name below.** [Observed]

**Population swept: every key name the proposed bytes contain that the
base bytes (current entry plus `.18`'s diff) do not — 48 names.** Fifteen
are plain words that occur throughout the corpus and cannot be separated
by a sweep: `classes`, `column`, `container`, `field`, `headings`, `key`,
`label`, `level`, `path`, `pillar`, `rule`, `scope`, `source`, `table`,
`text`. The other 33 are distinctive:

| Name | Files | Where, when not zero |
|---|---|---|
| `classGrammar` | 0 | |
| `containerShape` | 0 | |
| `containerShapes` | 0 | |
| `extractionBindings` | 0 | |
| `headingMatch` | 0 | |
| `indexChainDepth` | 0 | |
| `missingField` | 0 | |
| `pathPattern` | 0 | |
| `pillarIndexBasename` | 0 | |
| `pillarRootLinks` | 0 | |
| `pillarRootTable` | 0 | |
| `sharedReadingRules` | 0 | |
| `sourceGrammarSemantics` | 0 | |
| `sourceRules` | 0 | |
| `textsFrom` | 0 | |
| `treePopulations` | 0 | |
| `every-level-2-section` | 0 | |
| `first-table-rows` | 0 | |
| `ordinal-section-table-rows` | 0 | |
| `toml-table-field` | 0 | |
| `top-level-bulleted-list` | 0 | |
| `top-level-decimal-list` | 0 | |
| `top-level-list` | 0 | |
| `tree-path` | 0 | |
| `heading-section` | 2 | The two 2026-09-22 vision-pursuit records under `docs/pursuits/`; design notes, no code. |
| `itemKey` | 2 | The same two pursuit records. |
| `pillarColumn` | 1 | `project-shape-manifest.ts`, a local variable in the pillar-root table reader this field restates. |
| `directoryColumn` | 1 | The same file and function. |
| `companions` | 16 | Prose only (round records, reviews, the acceptance record); no code. |
| `relativePath` | 14 | 13 code files. One is `project-shape-manifest.ts`, where it is the parameter of `extractionClassesFor`, the function the bindings restate; the other twelve, in `packages/cap1-daemon/`, `apps/three-surface-poc/` and three `packages/three-surface-poc-core/` tests, use it as an unrelated path field. None reads the registry. |
| `rootIndex` | 12 | 7 code files in `packages/three-surface-poc-core/src/`: the source manifest's own `rootIndex` field (its path and read state). |
| `pillars` | 29 | 6 code files in the same package and its live test: the manifest's and model's `pillars` fields. |
| `sourcePopulation` | 6 | 4 code files: `resource-ledger.ts` and its test, and `polaris-generation-core`'s `pipeline.ts` and its test, as a local count. |

Twenty-four zeros: no reader can be broken by those names' meaning
[Observed]. Of the nine names already in use, three are code identifiers
with a nearby meaning — `rootIndex` and `pillars` in the source manifest,
`sourcePopulation` in the resource ledger — and none of those reads the
registry [Observed, read at source]. A loader built by limb 5 has to keep
the registry fields and those manifest fields apart; that is its
concern, not this act's [Inferred]. (Round 1 found `sourcePopulation` in
10 files at `23b486c`; that count was a substring sweep, and the
whole-word figure at this baseline is 6.)

Other names the package touches, same two methods, same denominator:

| Name | Files |
|---|---|
| `ProjectShapeProfile` | 5 |
| `PWB_ROOT_INDEX_PATH` | 11 |
| `extractionClassesFor` | 3 |
| `VISION_HEADINGS` | 4 |
| `V1_HEADINGS` | 4 |
| `CATALOG_HEADINGS` | 8 |
| `PWB_OBSERVER_IDENTITY` | 5 |
| `observationGrammar` | 17 (18 as a substring: the M8 funnel evidence record carries it only inside the longer key `observationGrammar_keys`) |
| `registryVersion` | 8 |
| `observerVersion` | 39 |
| subject basename stem | 68 |
| `rootIndexRequired` (M15's flag) | 5 |
| `rootIndependent` (round 1's flag, now removed) | 0 |

`ProjectShapeProfile` occurs only in the M8 funnel and four pursuit
records — a designed name with no code [Observed].

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

The builder's second witness compares the fields with these constants;
heading texts are found as quoted literals, not tied to their constant.
Which heading belongs to which row, at what level, is checked by the third
witness instead: it runs the observer's code over profile-built files and
compares the items read. When limb 5 deletes the constants, the second
witness is retired with them and limb 5's own loaded-profile test takes
its place; the third keeps working, because it needs only the code.

| Constant | File |
|---|---|
| `PWB_ROOT_INDEX_PATH`, `PWB_INDEX_DEPTH`, `PILLAR_KEYS`, `PILLAR_LABELS`, `SOURCE_RULES` | `project-shape-manifest.ts` |
| `extractionClassesFor` (eight bindings) | `project-shape-manifest.ts` |
| `BASELINE_SPEC`, `ROSTER_BUTLER` | `project-shape-manifest.ts` |
| `VISION_HEADINGS`, `V1_HEADINGS`, `CATALOG_HEADINGS`, `DESIGN_CONTRACT_HEADING`, `CRAFT_POLICY_HEADING` | `project-shape-extraction.ts` |

## Table 4 — sibling candidates

| Package | Relation |
|---|---|
| `pwb-registry-currency-briefing-amendment/` (`syzygy-dov.18`) | Same subject. This package's diff is drafted on top of it, so its builder needs `.18` applied first — a drafting constraint, not an owner ruling. |
| `pwb-self-observation-acts/` (`syzygy-dov.25`, PR #120) | Drafts a second registry entry; its packet asks whether to copy `.18`'s and this package's fields. Regenerated after this act. |
| N8 container-shape amendment (`syzygy-u05.8`) | A specification amendment that would point at `containerShapes`; not yet on main. Its shape sentences are the same text as this package's. |
| M15 pipeline-truthfulness delta (P-82, `.15.1`, after `.17`) | The owner's P-82 Q4 answer: "design the root-independence flags in the same delta" (the row's "What it means" column places that delta on `PWB-REQ-002`); M15's design names one, `rootIndexRequired`. This package adds no flag. The last clause of `sharedReadingRules` states today's root-blind tree enumeration; if M15's recommended arm is adopted, a later registry act replaces that clause. Packet question 9. |

The builder's composition check fails if any other candidate adds a patch
to the subject.
