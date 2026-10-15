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
- **Fixture.** Its browser test and entry point run over every Polaris page
  served at one whole-project evaluation, the pages listed from the
  machine answer, instead of a smaller fixture. *(Repaired 2026-10-14: this
  line first said "over a page rendered from a whole-project evaluation",
  the pre-repair one-page scope; round-2 finding 5.)*
- **Rendering.** `polaris.ts`, wherever a shared visible label (a source
  link, a disclosure toggle) needs an accessible name that begins with the
  label and, for an exact-source link, includes the source's path, and
  wherever a heading level skips. [Inferred] `polaris-markdown.ts` (line 179
  at `814fbcc1`) keeps Butlers' relative heading jumps when it re-bases
  levels, so it would need to close gaps too.
- **Machine answer.** [Unknown] Whether it already carries each listed
  source's path; if not, the shared-label rule needs it to (packet,
  question 7).

## Packages this collides with

- **Opening-index amendment** (P-98, `pwb-opening-index-amendment/`),
  drafted in the same change. It changes PWB-REQ-010 only. Its index rows
  are links, so they fall under this package's distinct-name check; that
  package now says each row's accessible name names its question.
  *(Marked 2026-10-14: no longer true. P-98's cycle-2 repair dropped that
  sentence; each row now shows its declared row name, and this package's
  rules bind the rows as they bind any link.)*
- **Anchor-resolution amendment** (P-96,
  `pwb-anchor-resolution-amendment/`, pursuit move N9), pending. It changes
  PWB-REQ-014 only. *(Marked 2026-10-14: signed v1.0 that day; no longer
  pending.)*
- **Class-granular extraction amendment** (P-86) and **release-label
  amendment** (P-85), pending. They change the reader definitions,
  PWB-REQ-001 and PWB-REQ-002.

All five spec patches touch different requirements and compose in any
order: this package's builder checks it against each of the other four,
and all 120 orders of the five were applied on 2026-10-03 to one identical
result. (An earlier version of this ledger said "the other three" and "24
orders of the four"; that population omitted P-96 and is superseded.)
P-85 and P-86 do overlap outside the spec (both add design decision
12 and capability row 34). All five rewrite the one
digest line of the generated dependency file and hash post-apply bytes
against the current tree, so whichever is signed second is regenerated with
`--write`, and its manifest reviewed again, before it is offered.
*(Marked 2026-10-14: P-96 is no longer pending. It was signed v1.0 that
day, so its patch is part of the signed `spec.md`, and the builder now
composes this package with the three still pending: P-98, P-86 and P-85.
This package was regenerated with `--write` over the moved `spec.md` in
the cycle-2 repair.)*

## Registry entry and policy

[Observed] `scripts/check_spec_reconciliation.py` reports that the observer
registry entry and the secret-classification policy pin a PWB spec digest
that is no longer current (PROJECT-STATUS.md, the reconciliation row's
2026-10-03 note). This package edits neither. Signing it moves the spec
digest again, so it interacts with the P-95 re-pin: pins re-written to the
tree-framing sign-off go stale once more when this package is signed, and
P-95's acts, if not yet performed, are regenerated against the new
`spec.md` first.
