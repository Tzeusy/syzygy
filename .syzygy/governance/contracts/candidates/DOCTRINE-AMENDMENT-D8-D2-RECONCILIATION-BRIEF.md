# D8 clause (d2) — what applying it needs, and the reconciliation review brief

> **Candidate — binds nothing.** Written 2026-10-15 by the session that
> recorded the owner's D8 adoption, for whoever applies clause (d2). It
> dispatches no review and authorizes nothing. A review is evidence for the
> owner, never an owner act (VIS-4).

## Where (d2) stands

*(Marked 2026-10-20: this section, and "adopted and not applied" below,
describe the state before (d2) landed. All four items under "What the Q-A1
path therefore needs" are done and (d2) is applied; row D8 of
`../../decisions/DOCTRINE-AMENDMENT-LOG.md` records how, with the reviews.
The text below is kept as written.)*

The owner adopted clause (d) on 2026-10-15 (Q4, "Adopt (Recommended)") and
answered Q-A1 "Fresh reconciliation review" — "Re-review over the amended
vision.md." (`../../decisions/DOCTRINE-AMENDMENT-LOG.md`, row D8). Insert 1,
(d1), is applied in `architecture.md`. Insert 2, (d2), is **adopted and not
applied**: it changes `vision.md`, and that edit retires the reconciliation
review the Polaris understanding adoption recorder binds. Until (d2) lands,
VIS-6 names no second destination, and (d1)'s closing parenthetical points
at text not yet in force. Tracked as bead `syzygy-5rxi`.

The bytes to apply are the `markdown` fence under "Insert 2" in
`doctrine-amendment-inferred-first-class-d8/OWNER-DECISION-PACKET.md`
§1 (d): a sub-bullet inserted after `vision.md` line 234, under the VIS-6
bullet "**Syzygy's databases and views are projections.**" (lines 232–234).
The anchor holds while `vision.md` hashes to
`93cc5fbbfe8ba07643d097007500f772c7b4ba1f3d5a1ac792c6e4bf74f0506d`. If D7
or anything else changes `vision.md` first, the anchor is a changed review
subject: re-anchor through a fresh review (rule 10), never by judgment at
the keyboard. The packet stays unedited; round-4 note 5 (who must name the
write in (d2)'s last sentence) is a residue of cleared bytes, and changing
those bytes makes them a new review subject.

## What the recorder does today [Observed]

Probe, 2026-10-15, in this worktree at `origin/main` `60995b23`, with
(b), (d1) and (e) applied: (d2) was inserted into `vision.md` by script
(anchor lines and the digest above asserted; `vision.md` then hashed
`ff8410443dee3b53e4c8aad2e3b4072239e18ca9c16e3bef2518c8a44ae9ceeb`),
`scripts/record_polaris_understanding_adoption.py --check` was run, and
`vision.md` was restored with `git checkout`. The output was:

```text
FAIL exact digest reconciliation unresolved: review retired by changed input: .syzygy/governance/doctrine/vision.md
```

Without (d2) the same command prints `PASS`, and `--selftest` passes.

Why, from the recorder's source at that commit:

- `VISION` (line 240) is one of `FROZEN_PATHS` and not one of
  `HISTORY_PATHS` (line 250), so `reviewed_template` requires its current
  digest to equal the digest the C1 review bound ("review retired by changed
  input", line 592).
- The C1 review is one fixed path, `RAW = EVIDENCE + 'REVIEW-RAW.md'`
  (line 234). Its current bytes must equal the blob at its single
  introducing commit ("retained C2 review changed"; `introduction` refuses
  a reintroduced file), and `technical-record.json` must equal the template
  filled with that raw's digest.
- `candidate_check` separately requires every row of `review-inputs.json`
  to hash today as it did ("candidate input drift").
- The numbered `HISTORY-REVIEW-n-RAW.md` reviews bind only the recorder's
  own bytes (`history_review`), and readability-successor rows apply only
  to the adoption subjects.

So the recorder as written reads no second reconciliation review
[Inferred: from reading every review path the recorder names — `REVIEW`,
`RAW`, `HISTORY_REVIEW`, `TREE_REVIEWS` — not tested by mutation]. This
agrees with the D7 round-4 reviewer's note (docs/reviews/R-DOCTRINE-AMENDMENT-D7-4-RAW.md, note 2,
also [Inferred]).

## What the Q-A1 path therefore needs

1. **A reviewed recorder change that admits a fresh reconciliation
   review**, never one that overwrites `REVIEW-RAW.md`. For example: a
   numbered successor raw retained beside it in the evidence directory,
   whose head names its reviewed commit and verdict and whose binding list
   re-binds the non-history frozen inputs (at least `vision.md`) to the
   digests that review confirmed; `check` then accepts a changed frozen
   input only when the latest successor review confirms its current
   digest. Selftest fixtures and rule-6 mutants for each new refusal go with
   it. Adding `VISION` to `HISTORY_PATHS` is the other Q-A1 arm, which the
   owner did not choose.
2. **A history review of the changed recorder.** `SCRIPT` is in
   `HISTORY_PATHS` and is bound by the latest `HISTORY-REVIEW-n-RAW.md`
   (17 retained at `60995b23`), so the changed recorder needs
   an eighteenth history review confirming its new digest, in the binding
   line form `history_review` reads (the recorder's path and sha256, each
   in a code span).
3. **(d2) applied and the fresh reconciliation review run over the amended
   `vision.md`**, at a commit where (d2) is applied, retained verbatim
   (CC-REV-6).
4. **The derived artifacts again.** `vision.md` feeds the context fixtures,
   the budget report and the contract index, and moving VIS-7 makes the
   directive register stale; regenerate them in the same change
   (`build_budget_report.py`, `build_contract_index.py`,
   `build_directive_register.py`). The D8 ledger's probe put VIS-7 at line
   260 after (d2); re-derive it, do not copy it.

Items 1–3 may share one branch; the battery stays red there until the
fresh review is retained. D7's Q6 asks the same question for D7's
`vision.md` insertion; one recorder change can serve both, but each
`vision.md` edit needs its own confirmation over the bytes it produces.

## Brief for the fresh reconciliation review (when dispatched)

- **Subject:** the amended `vision.md` (with (d2)) and the recorder's
  frozen reconciliation inputs at the reviewed commit; the recorder change
  is reviewed separately under item 2.
- **Governing references:** the evidence directory
  `docs/evidence/polaris-understanding-reconciliation-2026-09-28/`
  (`README.md`, `REVIEW-RAW.md`, `HISTORY-READING.md`); the D8 package; VIS-6
  as amended; the Polaris understanding adoption act
  (`../../decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`).
- **What to test, at least:** whether the amended VIS-6 changes anything
  the C1 reconciliation relied on `vision.md` for; that the (d2) bytes in
  `vision.md` equal the packet's Insert 2 exactly and sit after line 234;
  that no other `vision.md` byte moved; that every other frozen input is
  unchanged.
- **Output head:** whatever the item-1 recorder change specifies, quoted in
  the dispatch brief as a predicate, never inferred by the reviewer.
