# Specification-policy restyle — review notes

The binding review,
[`R-TREE-STYLE-SPEC-POLICY-PACKAGE-1-RAW.md`](../../../../../docs/reviews/R-TREE-STYLE-SPEC-POLICY-PACKAGE-1-RAW.md),
is `CONFIRM WITH EXCEPTIONS` with five notes and no material finding. Under
the owner's notes-only stopping rule
(`POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1) that clears the exact
bytes it read, so the notes live here, never in the reviewed package.

- **N1 — two older status sentences survive the banner fix.** After
  adoption, each policy still carries one sentence written before acts 6
  and 7, beneath a banner that says the opposite:
  - CC-IMPACT's `## Acceptance` section: "This is a candidate … Nothing in it
    binds today";
  - CC-SPEC's amendment row f15: "Awaits the confirming review".

  The banners and the acceptance record decide status; these two sentences
  are history. Correcting them needs a new manifest and another review, so
  they ride along with the next amendment of either policy.
- **N2 — the adopting commit regenerates more than the packet names.** It
  also regenerates `DIRECTIVE-REGISTER.md` and `05-CONTRACT-INDEX.yaml`
  (their battery checks fail until it does) and updates the PROJECT-STATUS
  battery comment. These are generated views and status, not rewrites of
  governed bytes.
- **N3 — the prerequisite review.** The understanding-reconciliation
  recorder's history review 4 is `CONFIRM WITH EXCEPTIONS`
  (`docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-4-RAW.md`),
  and its `--check` passes on main. Resolved.
- **N4 — two recorder guards have no fixture:** the partial-record guard and
  the already-installed-bytes guard. Both matter only when the steps are run
  by hand out of order. Open, as a follow-up.
- **N5 — wording.** The CC-IMPACT banner's "later performed acts amend them"
  becomes true when this act is performed. The builder's "row 7" counts
  manifest lines and the recorder's "row 5" counts the transaction's act
  rows; both are right.
