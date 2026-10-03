# Impact ledger — PWB accessible-name amendment (PWB-REQ-016)

> **Candidate — binds nothing.** A census of what the amendment touches and
> what cites the requirement it amends. It decides nothing.

## Predicate and population

[Observed, computed 2026-10-03 at `c371339d`, before this package existed]

- **Population:** every file tracked at that commit, 2,006 paths
  (`git ls-tree -r -z --name-only`), each read from the commit's blob.
- **Predicate:** Python `re`, run form included:
  `PWB-REQ-(\d{3})((?:[ \t]*(?:/|,|–|\.\.|…|and)[ \t]*\d{3}\b)*)`. A file
  counts when any match's first number or any continuation number is `016`.
- **Result:** 92 files cite PWB-REQ-016.

| Area | Files | Effect of this amendment |
|---|---:|---|
| `docs/reviews/` raw reviews | 27 | None. Raw output is never edited (CC-REV-6). |
| Other `docs/` (plans, designs, evidence, pursuits) | 22 | None. Evidence records name the bytes they measured. |
| `.syzygy/governance/contracts/candidates/` sibling packages | 28 | None. Each is another package's record. The one pending PWB package among them, release-label, cites PWB-REQ-016 only in its regenerated dependency patch; the pending class-granular package does not cite it. |
| `openspec/changes/polaris-project-wide-butlers-model/` | 5 | `spec.md` patched; `GOVERNING-DEPENDENCIES.md` regenerated (its digest line only). `CAPABILITY-COVERAGE.md`, `CONTRACT-COVERAGE-REPAIR-DELTA.md` and `tasks.md` are unchanged. |
| Other `openspec/` | 1 | None. `polaris-manifesto-generation/design.md` cites it as a neighbour. |
| `scripts/` | 2 | None. Two performed sibling builders name it as history. |
| `apps/three-surface-poc/src/` | 7 | Implementation consumers: the accessibility checker, its entry point and browser test, the keyboard sweep, the reachability test, the browser driver and `polaris.ts`. Sign-off authorizes no change to them. |

Second method for the openspec, scripts and implementation rows [Observed]:
a fixed-string `git grep -l -F "PWB-REQ-016" c371339d -- openspec packages
apps scripts` returns 14 of the predicate's 15 files there. The one it
misses, `apps/three-surface-poc/src/polaris.ts`, cites the requirement only
in run form (`PWB-REQ-011/016`, line 129).

## Files a later implementation would touch

[Inferred — named for planning, not authorized]

- **Checker.** `apps/three-surface-poc/src/polaris-accessibility.ts` gains
  a distinct-name check (group by computed name, compare targets) and a
  heading-order check, each reporting its denominator, beside its existing
  unnamed-node check.
- **Fixture.** Its browser test and entry point run over a page rendered
  from a whole-project evaluation instead of a smaller fixture.
- **Rendering.** `polaris.ts`, wherever a repeated visible label (a source
  link, a disclosure toggle) needs an accessible name that names its item
  or source, and wherever a heading level skips.

## Packages this collides with

- **Opening-index amendment** (P-98, `pwb-opening-index-amendment/`),
  drafted in the same change. It changes PWB-REQ-010 only. Its index rows
  are links, so they fall under this package's distinct-name check; that
  package now says each row's accessible name names its question.
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
