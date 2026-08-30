# Owner direction — Three-Surface POC improvement cycles

Date: 2026-08-30

Owner: Tzeusy

Recorded from direction the owner gave directly in session on
2026-08-30, after the bounded POC completed its eight items with all
three product assumptions NOT FALSIFIED
(`docs/reviews/R-POC-PRODUCT-REVIEW.md`) and the one repair pass
CONFIRMED (`docs/reviews/R-POC-CONFIRMATION-REVIEW.md`). The owner's
words: **"Let's extend the experiment, run several improvement cycles
over our POC"**.

## What this direction changes

Two bounds of the 2026-08-29 POC direction
(`THREE-SURFACE-POC-MODE-DIRECTION.md`) are superseded for this
extension:

1. **The eight-item cap is lifted for improvement-cycle items.** New
   POC beads may be created, but only as part of a recorded
   improvement cycle (below), and each must still alter the runnable
   demonstration or falsify/repair a named product finding.
2. **The one-review budget is lifted.** The "one product review, one
   consolidated repair, one confirmation" limit no longer bounds the
   experiment; each cycle carries its own review.

## Improvement-cycle structure

The owner said "several" cycles without naming a count. Recorded
default, halting anytime the owner says stop:

- **A cycle is:** (1) a review/audit of the runnable POC in fresh
  context producing evidence-cited findings; (2) bounded repair or
  improvement beads derived only from recorded findings; (3) a
  confirmation pass against the exact repaired commit.
- **Cycle 1 seeds** from the standing deferred findings PRF-2, PRF-3,
  PRF-4 in `docs/reviews/R-POC-PRODUCT-REVIEW.md`; its confirmation
  doubles as the next cycle's fresh review.
- The agent reports each completed cycle to the owner before starting
  the next; the owner may halt or redirect at any report.

## What this direction does not change

Everything else in the 2026-08-29 direction and the standing
prohibitions remains in force: one configured Butlers repository only;
no production release, deployment, or broad remote access; no
multi-user support; no autonomous intent adoption; Syzygy itself
writes no implementation code; WIP one for POC shared-model changes;
truth/evidence boundaries (no synthetic positive evidence; Unknowns
stay explicit); the signed `three-surface-poc-experience` artifacts
stay frozen at their act digests (spec changes route through CC-REV-2);
and the escalation triggers of the Capability 1 authorization act.
Improvement-cycle work must trace to POC-REQ-001..061 or to a recorded
review finding.
