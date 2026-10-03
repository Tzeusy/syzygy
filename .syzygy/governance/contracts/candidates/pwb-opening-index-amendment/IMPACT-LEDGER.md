# Impact ledger — PWB opening-index amendment (PWB-REQ-010)

> **Candidate — binds nothing.** A census of what the amendment touches and
> what cites the requirement it amends. It decides nothing.

## Predicate and population

[Observed, computed 2026-10-03 at `c371339d`, before this package existed]

- **Population:** every file tracked at that commit, 2,006 paths
  (`git ls-tree -r -z --name-only`), each read from the commit's blob.
- **Predicate:** Python `re`, run form included:
  `PWB-REQ-(\d{3})((?:[ \t]*(?:/|,|–|\.\.|…|and)[ \t]*\d{3}\b)*)`. A file
  counts when any match's first number or any continuation number is `010`.
- **Result:** 99 files cite PWB-REQ-010.

| Area | Files | Effect of this amendment |
|---|---:|---|
| `docs/reviews/` raw reviews | 31 | None. Raw output is never edited (CC-REV-6). |
| Other `docs/` (plans, designs, evidence, pursuits) | 20 | None. Evidence records name the bytes they measured. |
| `.syzygy/governance/contracts/candidates/` sibling packages | 25 | None. Each is another package's record. The one pending PWB package among them, release-label, cites PWB-REQ-010 only in its regenerated dependency patch; the pending class-granular package does not cite it. |
| Other `.syzygy/` | 5 | None. Decision records and the register cite the requirement as history; P-98 is added by this change. |
| `openspec/changes/polaris-project-wide-butlers-model/` | 6 | `spec.md` patched; `GOVERNING-DEPENDENCIES.md` regenerated (its digest line only). `CAPABILITY-COVERAGE.md`, the two RFC-0007–0009 coverage files and `tasks.md` are unchanged. |
| Other `openspec/` | 1 | None. `polaris-manifesto-generation/design.md` cites it as a neighbour. |
| `scripts/` | 3 | None. Two performed sibling builders and the performed-act recorder name it as history. |
| `apps/three-surface-poc/src/` | 6 | Implementation consumers (`polaris.ts`, its tests, the mutation sweep). Sign-off authorizes no change to them. |
| `AGENTS.md`, `PROJECT-STATUS.md` | 2 | None. |

Second method for the openspec, scripts and implementation rows [Observed]:
a fixed-string `git grep -l -F "PWB-REQ-010" c371339d -- openspec packages
apps scripts` returns 15 of the predicate's 16 files there. The one it
misses, `apps/three-surface-poc/src/pwb-mutation-sweep-main.ts`, cites the
requirement only in run form (`PWB-REQ-001/002/…/010/…`, line 226).

## Files a later implementation would touch

[Inferred — named for planning, not authorized]

- **Rendering.** `apps/three-surface-poc/src/polaris.ts`, whose project-shape
  renderers already cite PWB-REQ-010 (line 315 at `c371339d`): the index
  rows, the offsets and the stopping line at the head of the first reading
  level.
- **Offsets.** A word counter over the served HTML for the index, and a
  second one, sharing no code, for the oracle.
- **Copy.** The PWB-REQ-012 copy sweep, so the new strings carry their roles
  and stay inside its word and term rules.
- **Not touched.** The walkthrough readiness seam
  (`packages/three-surface-poc-core/src/walkthrough-readiness.ts`), the
  PWB-REQ-020 parity sweep and the machine answer: the offsets enter none of
  them.

## Packages this collides with

- **Accessible-name amendment** (P-99, `pwb-accessible-name-amendment/`),
  drafted in the same change. It changes PWB-REQ-016 only.
- **Class-granular extraction amendment** (P-86) and **release-label
  amendment** (P-85), pending. They change the reader definitions,
  PWB-REQ-001 and PWB-REQ-002.

All four spec patches touch different requirements and compose in any
order: this package's builder checks it against each of the other three,
and all 24 orders of the four were applied on 2026-10-03 to one identical
result. P-85 and P-86 do overlap outside the spec (both add design decision
12 and capability row 34). All four rewrite the one
digest line of the generated dependency file and hash post-apply bytes
against the current tree, so whichever is signed second is regenerated with
`--write`, and its manifest reviewed again, before it is offered.

## Registry entry and policy

[Observed] `scripts/check_spec_reconciliation.py` reports that the observer
registry entry and the secret-classification policy pin a PWB spec digest
that is no longer current (PROJECT-STATUS.md, the reconciliation row's
2026-10-03 note). This package edits neither. Signing it moves the spec
digest again.
