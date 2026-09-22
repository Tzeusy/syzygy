# Review — PWB missing-currency disclosure scenario delta

Reviewed commit: 0bb7bee7bed3dcd72f1787351872149514a5eb71
Manifest SHA-256: 42dd4f91314f7aed074f21095743ba7ed175ba9518a0d8766cf38d18568209d7
Verdict: REVISE

## Findings

### Finding 1 — Blocking

IMPACT-LEDGER.md:37-48 claims 3 files/3 occurrences of continuation-form
PWB-REQ-007; independent 1,376-file sweep found 7 files/8 occurrences,
omitting docs/design/POLARIS-M13-NAVIGATION-SCALE-FUNNEL.md:1065,
docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md:108,
docs/reviews/2026-09-05-pwb-live-exact-head-packet.md:84, and
docs/reviews/R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-RAW.md:415-416; retained
raw review is counted/classified, never edited.

### Finding 2 — Medium

build_pwb_missing_currency_disclosure_scenario.py:417-419 changes the heading
so heading-count fails before the placement predicate at :166-173; repair
mutation to keep the unique intact scenario heading and move the whole block
across the requirement boundary.

Owner sign-off may not be offered until repair/regeneration/fresh exact-byte
review.
