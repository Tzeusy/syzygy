> # Record beside the package — not authority, binds nothing
>
> Dispositions of the one fresh-context review of the PWB class-granular
> extraction amendment package (M15). This record is not a package artifact:
> the manifest does not hash it and no builder reads it. It offers nothing
> and performs no act (VIS-4).

# Round 1 dispositions — PWB class-granular extraction amendment

- **Reviewed commit:** `14db1a988e08b24e83bbc931eb66680d36a425f6`.
- **Verdict (raw line 4):** `REVISE`. The review has three revise findings
  (1–3) and seven notes (4–10), with no blocking finding.
- **Stopping rule, set in `REVIEW-BRIEF.md` before the round ran.** One round
  only. A notes-only round clears the bytes it read; any other verdict is
  repaired, no second round is dispatched, and the package goes to the owner
  with the repaired bytes unreviewed.
- **Applied here:**
  - Findings 1–9 are repaired in the package; finding 10 names residual
    risks and changes nothing.
  - The repair retires the round-1 review (rule 10), so **the repaired bytes
    have not been reviewed.**
  - No second round is dispatched.
- **Status: not cleared.** This version is not ready for owner sign-off in
  the sense Scope A item 3 requires: "a package is offered only after a round
  that returns CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only". It goes
  to the owner as pending row P-86 with this disposition. The drafter
  recommends one fresh round over the repaired bytes before the sign-off
  question is asked.
- **Re-derived figures** [Observed], from the repaired bytes by
  `scripts/build_pwb_class_granular_extraction_amendment.py`:
  - `--check`: 11 proposed subjects, 5 patched; 17 requirements and 54
    scenarios; contract coverage regenerates byte-identical;
  - `--selftest`: 34 structure mutants (22 at the reviewed commit), patch
    drift and an unclassified sibling, each failing on its own predicate;
  - the spec patch still has 10 hunks.

Reviewed record: docs/reviews/R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-1-RAW.md

## Dispositions

### 1 — root-summary and precedence headings dropped from Q3 without asking (revise)

**Accepted.** The scope is not widened; the choice is put to the owner.

- `OWNER-DECISION-PACKET.md` gains question 6, with two options: defer the
  root grammars to a separate PWB-REQ-004 delta (recommended), or widen this
  package.
- `SEMANTIC-DELTA.md` §2 now names the open half of the ruling and says the
  narrowing came from the record's gloss, not the owner's words. Residual 5
  carries it.

### 2 — the SHALL sentence obliged more than the defined term (revise)

**Accepted.** The PWB-REQ-002 clause now reads "an unenumerated heading SHALL
be surfaced, never skipped", using the defined term. The builder pins the
new phrase, and the selftest mutant "SHALL broadened" restores the broad
form and fails.

### 3 — no rule for a source's own denominator when its only defect is an unenumerated heading (revise)

**Accepted.**

- The reader definitions now say that a source's own item denominator is
  Unknown whenever any class it is assigned is Unknown in it, for any
  reason. A source whose every class reads but one carries an unenumerated
  heading is *extracted*, not partially extracted, and its own denominator
  is still Unknown. The partially-extracted sentence no longer carries its
  own denominator rule; the general rule covers it.
- PWB-REQ-002 gains the matching SHALL clause, an oracle limb, and a
  falsifier limb ("a source with a class whose item denominator is Unknown
  presents its own item denominator as known").
- The scenario "An unenumerated heading is surfaced, not skipped" now names
  the V1 index's own item denominator in its AND line.

### 4 — the counted-and-Unknown sentence covers no source of the rules that need the root index (note)

**Accepted.** The flag is now stated as belonging to the rule, set by a
loaded profile for each tree population it declares. The counted-and-Unknown
half is scoped to "where that rule is a tree population", and the text says
the pillar rules name no source without the root index, so they admit none.

### 5 — rule provenance had no oracle, falsifier or scenario (note)

**Accepted.**

- Oracle: every source names the rule that an independent derivation of the
  source-path population admits it under.
- Falsifier: "a source names no rule or a rule other than the one that
  admitted it".
- Scenario "Counts derived without a read root index say so" gains two AND
  lines: one for rule provenance, and one for the loaded-profile default (a
  tree population that does not declare `rootIndexRequired` mints no item).
- [Observed at `ef5d5f03`] `ManifestSource` already carries `rule`
  (`project-shape-manifest.ts` line 81); the delta says so.

### 6 — the builder's guards missed six of seven mutants (note)

**Accepted, by phrase guards rather than a whole-spec pin.** Each of the
reviewer's six survivors is now a required phrase with its own selftest
mutant, and so is each phrase the repairs for findings 2, 3, 5 and 7 added:

| Reviewer's survivor | Selftest mutant |
|---|---|
| "and its category's" dropped | category clause dropped |
| root admission inverted | root admission inverted |
| denominator falsifier limb removed | denominator falsifier dropped |
| qualification falsifier limb removed | qualification falsifier dropped |
| Observable additions removed | observable additions dropped |
| scenario THEN weakened | scenario category weakened |

Each mutant's expected finding names the phrase it removes, so it fails on
its own predicate (rule 6). The structure-mutant count went from 22 to 34.
[Inferred] A whole-spec pin would be stricter, but `--write` regenerates the
manifest, so a pin in the builder would need hand-editing at every repair;
the manifest digest and the review head still pin the exact bytes.

### 7 — the oracle checked that headings were found, not how many; population totals unqualified (note)

**Accepted.** The oracle now requires that the count per source and class
equals the count the answer gives, and the falsifier adds "or is
miscounted". The root-index qualification in the reader definitions now
reaches "every source-path population total" that counts a source admitted
without the root index.

### 8 — unlabelled factual claim about Butlers in the packet (note)

**Accepted.** The sentence is now labelled [Observed] and cites
`docs/evidence/smooth-example-live-run-2026-10-03.json` at Butlers
`32f38feb`: 9 sources with an Unknown item denominator, equal per source to
the 9 withheld ones (that record's `unknownDenominatorWithheldComparison`,
added in `b044a756`), so none is Unknown for a grammar failure.

### 9 — Hunk 8's "Current" block joined two separate lines (note)

**Accepted.** The delta's hunk quotes now mark every gap between replaced
lines with "[… signed lines between are unchanged …]", on both sides. Hunks
8 and 9 carry the marker; the other eight replace or add one run each.

### 10 — residual risks (note)

**Noted; no change.**

- The [Unknown] about the V1 index is still stated in the delta and packet;
  the packet now adds that the V1 index's own count would also read Unknown.
- The P-85 ordering and the `PENDING_SIBLINGS` hand-edit stand; packet
  question 5 asks the order.
- This file is the forward reference the reviewer found missing.
- The `check_spec_reconciliation.py` failure after `--apply` is residual 2,
  for the signing change.
