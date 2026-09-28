# RFC 0010 and RFC 0011 restyle — review notes

> **Candidate notes. They bind nothing.** RFC 0010 and RFC 0011 are
> deferred-wave candidates (`DEFERRED-WAVE-POSTURE.md`); this page records
> what the binding review left open on their restyled bytes.

Both packages are restyled to CC-REV-8 under
[`OWNER-DIRECTION-2026-09-28-TREE-STYLE-ROLLOUT.md`](../../decisions/OWNER-DIRECTION-2026-09-28-TREE-STYLE-ROLLOUT.md).
The owner adopted the restyle on 2026-09-28
([`OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md`](../../decisions/OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md));
the packages stay deferred-wave candidates.
No clause text changes. Each module gains an orientation paragraph and
non-normative diagrams, 17 in all.

- **Offers.** The four wave offers C1, C2, D1 and D2 in
  `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` quote the regenerated
  wave manifests; each row says so, dated.
- **Reviews.** Every review is stored raw under `docs/reviews/`:
  - [`R-TREE-STYLE-CONTRACT-0010-0011-1-RAW.md`](../../../../docs/reviews/R-TREE-STYLE-CONTRACT-0010-0011-1-RAW.md)
    is `REVISE`, with two material findings, both repaired: a paragraph split
    moved what "the paragraph above" points to (RFC10-5), and a diagram
    node read as excluding the declared target (RFC10-21).
  - [`R-TREE-STYLE-CONTRACT-0010-0011-2-RAW.md`](../../../../docs/reviews/R-TREE-STYLE-CONTRACT-0010-0011-2-RAW.md)
    is `CONFIRM WITH EXCEPTIONS`, notes only, which clears the bytes under
    the owner's notes-only stopping rule.
- **Open notes from review 2, not applied** (applying them would retire the
  review):
  - four repaired lines run past 78 columns;
  - two `RFC 000N` citations wrap across a line break (RFC10-6 and RFC10-12),
    so a line-oriented sweep for them misses those two;
  - two list splits leave a trailing "and," at the end of a bullet (RFC10-12
    and RFC11-4); the list's meaning is unchanged.
- **Context cost.** The orientation paragraphs and diagrams are part of each
  module, so they count toward every context packet that loads one. Two
  fixtures grow: `context-selection-5-cross-project-mission.md` and
  `context-selection-10-trajectory-lifecycle.md`. `CONTEXT-BUDGET-REPORT.md`
  carries the current figures.
- **One checker exemption.** `round-2026-08g/FINAL-OWNER-AND-SPEC-CLOSURE-PREFLIGHT.md`
  is a frozen measurement that quotes the four wave digests as they were
  measured then. CG-15 now exempts that file, with its reason recorded in
  `scripts/check_governance.py`.
