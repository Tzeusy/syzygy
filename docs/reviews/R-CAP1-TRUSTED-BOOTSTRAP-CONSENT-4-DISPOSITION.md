# R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-4 — disposition (notes only)

Reviewed record: docs/reviews/R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-4-RAW.md

[Observed] The verdict is `CONFIRM WITH EXCEPTIONS` (raw line 4). It covers
commit 591950c76805f34886e7052adb9753c58b5ef737, whose candidate bytes are
identical to main at 6ff755671d743f289c59d8a26b7f68f6e09d55d6, bound by
docs/evidence/cap1-trusted-bootstrap-consent-2026-10-15/review-4-subject.json.
The round has two findings, and both are notes for the owner. Under the
owner's 2026-09-26 stopping rule, a notes-only round clears the bytes it
read. The candidate package is unedited, and both notes are carried here for
the adoption change.

1. **Finding 1 (note, for the owner): what adoption must supersede is wider
   than one row and the totals.** The amendment adds RFC3-16(b) and
   RFC3-16(c) to the contract dependencies, taking them from 38 to 40. On
   adoption, these parts of the bound predecessor would state stale truth
   and must be superseded in the same transaction (CC-REV-2):
   - in `CONTRACT-COVERAGE.md`: the RFC3-16(a) row, the Part A totals, the
     family table, the "38 mapped / 286 unmapped" sentences, the RFC3 line
     in Part B, and the file's own self-check;
   - the generated `GOVERNING-DEPENDENCIES.md`.

   This record carries round 3's note 2 forward and replaces it. The
   adoption change must name every one of these surfaces, or carry a
   coverage and dependency successor. Disposition: deferred to the adoption
   change. Nothing changes now.
2. **Finding 2 (note, for the owner): RFC3-16(a)'s "blocking is not
   deletion" consequence has no row in the consent overlay.** CAP1-REQ-046's
   disclosure sentence ends "or the precise refusal reason". Read alone, that
   would let a refusal answer leave out the refused artifact's identity and
   digest. The rest of the amendment fails closed, so nothing becomes less
   safe. Disposition: reported for the owner and not resolved. If the owner
   wants it closed, the fix is a v1.1 that adds the row and the identity
   clause, and that version needs its own review round. v1.0 is offered as
   reviewed.
