# Impact ledger — each project's profile declares its container shapes

> **Candidate review input — never authority.** Companion to
> `SEMANTIC-DELTA.md`. Binds nothing.

Baseline: commit `08d4d02` (`origin/main` when this round was repaired).
The subject is byte-identical there and in the tree this package was
drafted in. Every sweep below reads that commit, so this package's own files
are outside it.

## Discovery method

Two independent sweeps, run 2026-09-27 at the baseline (rules 2 and 9):

1. **Python** over the UTF-8 text of every path from
   `git ls-tree -r -z --name-only 08d4d02`, each read with
   `git show 08d4d02:<path>`. Four paths do not decode and are skipped. The
   six phrases in lower case below were matched ignoring case; every other
   name is matched as a case-sensitive substring.
2. **`git grep -l -F <name> 08d4d02`** (with `-i` for the same six).

**Denominator: 1,545 tracked files.**

| Name | Python | `git grep` |
|---|---|---|
| `PWB-REQ-002`, literal | 49 | 49 |
| `PWB-REQ-002` in a run or range only | 13 | 13 |
| `heading-section` | 2 | 2 |
| `every-level-2-section`, `top-level-decimal-list`, `top-level-list`, `top-level-bulleted-list`, `first-table-rows`, `ordinal-section-table-rows`, `tree-path`, `toml-table-field` | 0 each | 0 each |
| `containerShapes`, `classGrammar` | 0 each | 0 each |
| `leading-bold` | 2 | 2 |
| `leading-bold-or-code`, `prefixed-ordinal`, `first-cell-link-text`, `tree-key`, `ordinal-and-label`, `link-target-basename` | 0 each | 0 each |
| project profile | 7 | 7 |
| key form | 1 | 1 |
| item key form, grammar row | 0 each | 0 each |
| container shape | 11 | 11 |
| the sign-off phrase | 0 | 0 |

The key form `fixed` is an ordinary English word and was not swept.

**The run and range forms of `PWB-REQ-002`.** The corpus writes
requirement lists as runs (`PWB-REQ-001/002/003`) and ranges
(`PWB-REQ-001..007`), so a literal sweep misses them. Method 1 matched

```
PWB-REQ-(\d{3}(?:SEP(?:PWB-REQ-)?\d{3})*)
SEP = (?:\s*(?:/|,|\.\.|–|—|-|\bto\b|\bthrough\b|,?\s*\band\b|,?\s*\bor\b)\s*)
```

(Python `re`, case-sensitive, any run length) and counted a file when 002 is
a member of a run or lies inside a range. Method 2 was `git grep -l -P`
with the independent pattern
`PWB-REQ-001(?:/0\d\d)*/002|PWB-REQ-001\s*(?:\.\.|–|-)\s*(?:PWB-REQ-)?0(?:0[2-9]|[1-9]\d)`.
Both give the same 13 files beyond the literal 49, 62 in all:

- code: `apps/three-surface-poc/src/pwb-mutation-sweep-main.ts` (line 226,
  `PWB-REQ-001/002/003/004/005/010/012/020/022`);
- `AGENTS.md`;
- the ledgers of `pwb-machine-view-amendment/` and
  `pwb-opening-band-scenario/`, and the latter's semantic delta;
- four evidence records under `docs/evidence/`: the 2026-09-04 model
  mutation run and three mutation-sweep parity records;
- four review files under `docs/reviews/`: the 2026-09-05 live exact-head
  packet and its engineering raw, and both opening-band confirmation raws.

**Error term.** A name hard-wrapped across a line is invisible to both
sweeps. For the multi-word phrases a join pass (the phrase split at any
word, joined across one newline and a leading `>`, `#`, `*`, `/` or `-`)
found one more "project profile": the historical rev9 copy of RFC 0005,
which wraps "per-project" / "profile" — the same execution-profile sense as
below. The single-token names were not join-swept.

## What the counts mean

- **The nine shape names and the new key-form names are unused.**
  `heading-section` and `leading-bold` occur only in the 2026-09-22
  pursuit's data and harvest records, as parts of the L1-M1 move's proposed
  shape names (`ordered-list-with-leading-bold`) [Observed]. No reader can
  be broken by their meaning.
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

  The other two hits are a Polaris product-understanding design note and a
  generator readiness review raw. Neither is the thing this draft names.
  Packet question 10 asks whether to rename.
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
| `packages/three-surface-poc-core/src/project-shape-extraction.ts` and its test | Reads Butlers through built-in constants equal to the Butlers grammar written in the reader definitions. It loads no profile, and the text names that grammar as Butlers' built-in default until a profile is loaded (Semantic delta, item 4). |
| `packages/three-surface-poc-core/src/project-shape-coverage.ts` and its test | Counts what extraction yields; unchanged. |
| `packages/three-surface-poc-core/src/synthetic-corpus-coverage.ts` | N8's synthetic census. Measures cells; asserts no conformance. |
| `apps/three-surface-poc/src/pwb-mutation-sweep.ts`, `pwb-mutation-sweep-main.ts`, `pwb-n8-synthetic-corpus-coverage-matrix-main.ts` | Tooling; unchanged. `pwb-mutation-sweep-main.ts` cites the requirement only in a run (line 226). |
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
| `.21`, `.30`, `.22`, lane B | The owner answered "Readiness order, lane B last (Recommended)", an option presented as `.21` → `.30` → `.22` → lane B (2026-09-23 owner-values record, §6). Where this package falls is not ruled; the drafter proposes after lane B. Each collides on `GOVERNING-DEPENDENCIES.md`; `.30` also edits `CAPABILITY-COVERAGE.md` in rows that compose with row 4. This manifest is regenerated with `--write` after each act that lands before it. |
| `.20` | Not in the ruled order. Edits `CAPABILITY-COVERAGE.md` in rows that compose with row 4 and collides on `GOVERNING-DEPENDENCIES.md`; regenerate after it if it lands first. |
| `pwb-dismissal-expiry-amendment/` (`syzygy-dov.29`, PR #121) | Also proposes to land last; composes on `spec.md` (different requirement), collides on `GOVERNING-DEPENDENCIES.md`. |
| `pwb-registry-loaded-profile-amendment/` (`syzygy-dov.24`, PR #123) | Drafts the registry fields a profile would live in. Its specification witness checks heading texts in the reader definitions; with this package's `spec.md.patch` applied in its worktree, its `--check` still passed [Observed, 2026-09-27, re-run with this round's patch at PR #123's head `1395d44`]. The two packages share the shape and key-form sentences word for word; this builder compares them once `syzygy-dov.24`'s builder is in the tree. |
| `pwb-self-observation-acts/` (`syzygy-dov.25`, PR #120) | A second project's registry entry; would need a profile under this text. |
| M15 (`syzygy-dov.15.1`, P-82), not drafted | P-82's answer (decision record line 70, Ruled column): "Q1 arm (b), draft the delta only; Q2 design `partially-extracted` inside it, build only after sign-off and a fresh authorization; Q3 design the `unenumerated-heading` reason as surface-flag (a counted, routed Unknown); Q4 design the root-independence flags in the same delta". That it is one CC-REV-2 delta to `PWB-REQ-002`, behind lane B's open manifest, is the recorder's "What it means" gloss, not the answer. It would likely edit the exactness sentence this package moves into its own bullet, so whichever lands second is regenerated and re-reviewed. The meanings stay apart: this package defers the size of a source failure to that sentence. Packet question 8. Not in the builder's composition outcomes, because no package exists. |

The builder's `--check` applies every shared patch in both orders against
each sibling's `proposed/` directory and compares the result with twelve
declared outcomes; a missing sibling directory is a finding.
