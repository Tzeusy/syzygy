# Impact ledger — PWB class-granular extraction amendment (M15)

> **Candidate — binds nothing.** A census of what the amendment touches and
> what cites the requirement it amends. It decides nothing.

## Predicate and population

[Observed, computed 2026-10-03 at `ef5d5f03`, before this package existed]

- **Population:** every tracked file, 1,970 paths (`git ls-files -z`).
- **Predicate:** Python `re`, run form included:
  `PWB-REQ-(\d{3})((?:[ \t]*(?:/|,|–|\.\.|…|and)[ \t]*\d{3}\b)*)`. A file
  counts when any match's first number or any continuation number is `002`.
- **Result:** 96 files cite PWB-REQ-002.

| Area | Files | Effect of this amendment |
|---|---:|---|
| `docs/reviews/` raw reviews | 23 | None. Raw output is never edited (CC-REV-6). |
| Other `docs/` (plans, designs, evidence, pursuits) | 22 | None. Evidence records name the bytes they measured. The M15 funnel packet is the question this package answers and is not edited. |
| `.syzygy/governance/contracts/candidates/` sibling packages | 23 | None. Every sibling but one is performed or declined. The pending one, the release-label amendment, cites PWB-REQ-002 only in its regenerated dependency patch. |
| Other `.syzygy/` | 5 | None. Decision records and registers cite the requirement as history. |
| `openspec/changes/polaris-project-wide-butlers-model/` | 10 | Four patched (spec, capability coverage, design, proposal) and one regenerated (`GOVERNING-DEPENDENCIES.md`). `CONTRACT-COVERAGE.md`, the three matrix files, the three parts files and `tasks.md` are unchanged. |
| `scripts/` | 4 | At sign-off, `check_spec_reconciliation.py` changes its literal census and the PWB successor chain. `record_pwb_behavior_amendment_acts.py` and the container-shape builder are history. The release-label builder now lists this package as a pending sibling. |
| `packages/three-surface-poc-core/src/` | 5 | Implementation consumers. Sign-off authorizes no change to them. |
| `apps/three-surface-poc/src/` | 3 | The mutation sweep and the synthetic-corpus matrix cite PWB-REQ-002's oracle. Sign-off authorizes no change. |
| `AGENTS.md` | 1 | None. |

Second method for the openspec and implementation rows [Observed]: a
fixed-string `git grep -F -l "PWB-REQ-002"` over `openspec/`, `packages/`,
`apps/` and `scripts/` at `ef5d5f03` returns 21 of the predicate's 22 files
there. The one it misses, `apps/three-surface-poc/src/pwb-mutation-sweep-main.ts`,
cites the requirement only in run form (`PWB-REQ-001/002/003/…`, line 226),
which is why the predicate carries the run form.

## Files a later implementation would touch

[Inferred — named for planning, not authorized]

- **Extraction.** `packages/three-surface-poc-core/src/project-shape-extraction.ts`:
  `extractSource` keeps the classes that read and returns a third outcome,
  partially extracted; `extractCatalogEntries` scans the level-2 sections
  that hold the nine catalog headings for an unenumerated level-3 heading.
  Its test pins the current discard ("a failing class withholds the items of
  the classes that succeeded") and is rewritten to assert per-class
  outcomes.
- **Coverage.** `project-shape-coverage.ts` treats a partially extracted
  source's failed classes as class-scoped Unknown, and never lets a class
  that read mask a failed sibling in a class or category total.
- **Manifest.** `project-shape-manifest.ts` does not cite PWB-REQ-002 by
  name, but its Rules 3 and 4 (the baseline-spec and roster tree rules) are
  where root independence is declared and stamped. The funnel's falsifier
  for that slice applies: Butlers' manifest digest must not move.
- **Parity.** Each new machine field (per-class outcome, unenumerated
  heading, root-index qualification) joins the PWB-REQ-020 parity sweep as
  its own family.
- **Shared-model order.** These are shared-model changes, so they take the
  WIP-one slot in the order the 2026-09-21 rulings set.

## Packages and fields this collides with

- **The release-label amendment** (P-85,
  `contracts/candidates/pwb-release-label-amendment/`), pending. Both
  packages patch `spec.md`, `design.md`, `proposal.md`,
  `CAPABILITY-COVERAGE.md` and the regenerated dependency file. The spec
  hunks do not overlap: that package changes PWB-REQ-001 only and this one
  the reader definitions and PWB-REQ-002. But both add design decision 12
  and capability row 34, and both recompute the capability totals. So
  whichever is signed second is regenerated over the first's applied bytes,
  renumbered, and re-reviewed. Each builder lists the other as a pending
  sibling, so neither check fails on the other's presence.
- **The loaded-profile registry fields** (`syzygy-dov.24`, PR #123, open).
  It drafts `containerShapes` and `classGrammar`. A profile's tree population
  would also carry `rootIndexRequired`. Until a loader exists the built-in
  Butlers grammar applies, so nothing reads the field yet.
- **M8's profile slices** (P-74, `syzygy-dov.8.*`). They thread a profile
  parameter through the extractor. They change no specification text, but
  share the extractor this amendment's implementation would change.

## Registry entry and policy

[Observed] The observer registry entry and the secret-classification policy
each pin a PWB spec digest that is already not the current one, and are
Unknown until their own act (`syzygy-jloi`); `check_spec_reconciliation.py`
reports both. This package edits neither. Signing it moves the spec digest
again.
