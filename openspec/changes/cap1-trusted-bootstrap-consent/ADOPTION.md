# Adoption overlay — cap1-trusted-bootstrap-consent v1.0

> **GENERATED at adoption — do not edit.** Written by
> `python3 scripts/build_cap1_trusted_bootstrap_consent_adoption.py --apply`
> in the sign-off change and re-checked by its `--check`. Figures are
> computed from the tree, never transcribed. This file binds nothing on its
> own: the adoption is the owner's selection recorded in
> `.syzygy/governance/decisions/CAP1-TRUSTED-BOOTSTRAP-CONSENT-SIGNOFF-v1.0.md`, bound by the annotated tag `cap1-trusted-bootstrap-consent-v1.0`.

## What is adopted

Version 1.0 of this change, the bytes the round-4 review read
(`docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-4-RAW.md`, `CONFIRM WITH EXCEPTIONS`, notes only; subject
`docs/evidence/cap1-trusted-bootstrap-consent-2026-10-15/review-4-subject.json`). It fully replaces **CAP1-REQ-011** and
**CAP1-REQ-046**. Every other Capability 1 requirement stays as adopted.

**The effective Capability 1 specification** is the composition
`GOVERNING-DEPENDENCIES.json` declares: the bound predecessor
`openspec/changes/project-registration-and-honest-shape-visibility/specs/project-registration-and-honest-shape-visibility/spec.md` with exactly the CAP1-REQ-011 and CAP1-REQ-046
blocks replaced by this change's `specs/…/spec.md`. [Observed, computed by
the builder] It has 42 requirements and 57 scenarios (the bound
file alone has 47), and its generated warrant union is
`GOVERNING-DEPENDENCIES.json`. [Observed] `scripts/check_spec_reconciliation.py`
still counts the bound file alone for CAP1; composing this overlay there is
bead `syzygy-5oqc`.

## Predecessor surfaces this adoption supersedes

CC-REV-2 forbids leaving an invalidated authoritative artifact asserting
the old truth. The predecessor's `CONTRACT-COVERAGE.md` and its generated
`GOVERNING-DEPENDENCIES.md` are act-bound and may not be edited, so this
overlay supersedes the following statements in place. Each is read as
written below for the effective composition; the bound bytes stay as
history. The set is the one round-4 finding 1 names
(`docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-4-DISPOSITION.md`, note 1).

[Observed, computed by the builder] The composed contract union has
40 identifiers; the bound union has 38. The difference is exactly `RFC3-16(b)` and `RFC3-16(c)`.

In `openspec/changes/project-registration-and-honest-shape-visibility/CONTRACT-COVERAGE.md`:

| Surface | Where | Superseded by |
|---|---|---|
| RFC3-16(a) row, valid/invalid act states, **Unknown** | line 109 | The consent consequences map to the amended CAP1-REQ-011/046 in this change's `CONTRACT-COVERAGE.md`; the general non-consent owner-act admission consequence stays **Unknown** (its last row). |
| Family table, RFC3 row `38 \| 11 \| 27` | line 36 | RFC3: 38 accepted, **13 mapped, 25 not mapped**. |
| Family table total `324 \| 38 \| 286` | line 43 | **324 accepted, 40 mapped, 284 not mapped**. |
| "The 38 mapped clauses are exactly the `contracts[]` union in the generated `GOVERNING-DEPENDENCIES.md`" | line 45 | The 40 mapped clauses are exactly the `contracts` union in this change's generated `GOVERNING-DEPENDENCIES.json`. |
| "The 286 unmapped clauses are disposed in Part B." | line 47 | 284 unmapped clauses; `RFC3-16(b)` and `RFC3-16(c)` leave Part B. |
| Part A totals, "65 consequence rows over 38 clauses — 63 covered, 2 Unknown" | line 141 | Part A is the bound table without the RFC3-16(a) row above, plus this change's 21 overlay rows (19 whose disposition opens "covered", 1 "Unknown", 1 in other words, each as written there). The composed covered/Unknown totals are not restated here: [Unknown] the 1 other-worded row(s) are not classified by this builder. |
| Part B applicability sentence, "the 286 unmapped clauses" | line 148 | 284 unmapped clauses. |
| Part B "RFC 0003 remainder \| 27" | line 160 | RFC 0003 remainder: 25. |
| Part B total 286 | line 167 | 284. |
| Self-check: "`contracts[]` union (38 identifiers), and 38 + 286 = 324" | line 175 | The composed union has 40 identifiers and 40 + 284 = 324; check it with this builder's `--check`. `build_capability_1_spec_dependencies.py --check` still checks the bound file against the bound spec, which remains true of those bytes. |

In `openspec/changes/project-registration-and-honest-shape-visibility/GOVERNING-DEPENDENCIES.md` (generated, bound): it is the union of the bound
specification, not of the effective composition. The effective union is
`GOVERNING-DEPENDENCIES.json` here.

## Known gap carried with v1.0

Round-4 note 2 (`docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-4-DISPOSITION.md`): CAP1-REQ-046's refusal
disclosure is a disjunction that does not on its own require the refused
artifact's identity and digest, and RFC3-16(a)'s "blocking is not deletion"
consequence has no overlay row. The owner adopted v1.0 as reviewed; closing
it needs a v1.1 with its own review round (bead `syzygy-0v4l`).

## What this does not do

It edits no act-bound byte, grants no consent for any repository, reads no
target repository and authorizes nothing. Implementation is authorized
separately and bounded by `.syzygy/governance/decisions/OWNER-DIRECTION-CAP1-CONSENT-IMPLEMENTATION-2026-10-15.md`; the route is
`.syzygy/governance/decisions/OWNER-DIRECTION-SCOPE-A-CAP1-TRUSTED-BOOTSTRAP-CONSENT-2026-10-15.md`.
