# Craft-and-care tree-style restyle

> **Status:** Adopted by the owner on 2026-09-28
> ([`OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md`](OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md)).

The nine craft-and-care rule files are restyled to CC-REV-8. No rule,
identifier, scope or citation changes.

- **Direction:**
  [`OWNER-DIRECTION-2026-09-28-TREE-STYLE-ROLLOUT.md`](OWNER-DIRECTION-2026-09-28-TREE-STYLE-ROLLOUT.md).
  Policy is authority, so the owner adopts it separately.

## What changes

- **Answer first.** Each file and each section opens with its answer.
- **Rule form.** Rule bodies become shallow trees: a statement, then
  conditions, then examples. Every *Violation:* line is a nested bullet.
- **Seven diagrams:**
  - README: the precedence of doctrine, SDRs, this cluster and the bar;
  - CC-PROV: the preserved set against the expiring transcripts, and the
    intent-to-realization mapping;
  - CC-DEP-1: the promotion and pruning of dependencies;
  - CC-DEP-4: the kernel reaching an external authority through an
    adapter;
  - CC-TEST-4: the retry rule;
  - CC-REV-2: invalidated artifacts, and doctrine stopping the change;
  - CC-VIZ-5: the layout inputs, and the owner-gated re-layout;
  - CC-SEC-5: exclusion at the ingest boundary.
- **Provenance notes** (amendment and correction notes) stay attached to
  their text, in compact present-tense form.

## What stays fixed

- Every heading, byte for byte, including the `## CC-…` rule titles.
- Every banner.
- Every identifier, link, code span and epistemic label, in its own section.
- CC-REV-8, byte for byte.

## Found while restyling, not changed

These would change meaning. They are left for the owner.

- **engineering-bar.md, CC-BAR-2 item 2:** it cites CC-TEST-3 for a
  "retained, resolvable artifact". That rule is CC-TEST-2; CC-TEST-3 is
  determinism.
- **README.md:** the tier-1 range reads SDR-1…SDR-33, but decisions now run
  to SDR-37. Its "adopted home" passage is written as a future event, though
  the banner says the directory already is the canonical home. "No stack has
  been selected" predates the Capability 1 implementation.
- **testing-and-verification.md, CC-TEST-7:** it says "this lock's vendored
  scope" in a file that is not the lock.

## Pending act 2

Act 2 (`CONFIRM CRAFT AMENDMENT: CC-TEST-2`) is unperformed, and its argument
is the digest of `testing-and-verification.md`.

- The restyle re-quotes that argument in the acceptance record and in
  `INSTALL-RECORD.md`, as act 4's was for OVERVIEW.
- The owner performs act 2 later, against the restyled bytes.

## Review

Every review is a fresh-reader review, stored raw under `docs/reviews/`:

- Review 1 —
  [`R-TREE-STYLE-CRAFT-1-RAW.md`](../../../docs/reviews/R-TREE-STYLE-CRAFT-1-RAW.md),
  verdict **REVISE**.
  - Five material findings, all repaired: openings stated rules more
    broadly or narrowly than their bodies, and one diagram overstated.
  - 24 of 26 minor findings were repaired, and two were skipped with
    reasons.
- Review 2 —
  [`R-TREE-STYLE-CRAFT-2-RAW.md`](../../../docs/reviews/R-TREE-STYLE-CRAFT-2-RAW.md),
  verdict **REVISE**.
  - One material finding, repaired: the `## Performance` opening dropped
    the [Unknown] alternative.
  - Notes N7, N9 and N10 were also applied.
- Review 3 —
  [`R-TREE-STYLE-CRAFT-3-RAW.md`](../../../docs/reviews/R-TREE-STYLE-CRAFT-3-RAW.md),
  verdict **REVISE**.
  - One material finding, repaired: commas in the CC-REV-6 opening let
    "by the accountable authority" reach fixes as well as overrulings.
- Review 4 —
  [`R-TREE-STYLE-CRAFT-4-RAW.md`](../../../docs/reviews/R-TREE-STYLE-CRAFT-4-RAW.md),
  verdict **CONFIRM WITH EXCEPTIONS**, notes only. Under the owner's
  notes-only stopping rule this clears the bytes.
  - Open notes, not applied: review 4's N1 (the CC-REV-6 opening says "raw
    output is kept" without "unchanged"; the body carries the full rule)
    and review 3's R2 (the `## Visual discipline` opening coarsens the
    legend-fidelity and aggregate-disclosure duties stated below it).
