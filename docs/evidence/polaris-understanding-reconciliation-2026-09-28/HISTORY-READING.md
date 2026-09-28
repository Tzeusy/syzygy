# Reading the reconciliation's frozen inputs as history

The reconciliation review froze thirteen inputs at C1. Two of them move on
lawfully after C3: CC-SPEC takes owner-adopted successors, and the recorder
itself changed to read CC-SPEC that way. The recorder therefore reads both, as
it already read the status pages and the governance checker, at C1.

- **Owner ruling.** "R1: read as history", recorded in
  [`OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md`](../../../.syzygy/governance/decisions/OWNER-ADOPTION-2026-09-28-TREE-STYLE-RESTYLES.md).
- **What this replaces.** The package [`README.md`](README.md) says "The
  checker remains subject to review retirement". That sentence is frozen with
  C1. The checker is no longer retired by its own change; a history review
  binds it instead (below).
- **What stays checked.**
  - Every C1 input still hashes, at C1, to the digest the confirming review
    bound (`REVIEW-RAW.md`).
  - The C1 CC-SPEC digest must appear in the acceptance record on a line of
    its own, `CONFIRM CRAFT AMENDMENT: CC-SPEC@<digest>`, so the review stays
    bound to CC-SPEC bytes a performed act confirmed. The test is the line's
    shape; the C1 digest is fixed and already performed.
  - The other inputs, and every subject, are still compared against today's
    bytes.
- **What binds the recorder now.** Its current bytes must equal the digest
  that the latest `HISTORY-REVIEW-<n>-RAW.md` in this directory binds.
  - That raw carries exactly one `Verdict:` header, `CONFIRM` or
    `CONFIRM WITH EXCEPTIONS`.
  - It carries exactly one line
    `` - `scripts/record_polaris_understanding_adoption.py`: `<sha256>` ``.
  - "Latest" is the highest `<n>`, compared as a number; the raws are
    numbered 1 to n with no gap.
  - A name that starts `HISTORY-REVIEW` but is not exactly
    `HISTORY-REVIEW-<n>-RAW.md`, with no leading zero, is refused, never
    skipped.
- **Every history review is retained.**
  - Each raw's introducing commit holds the same bytes as today.
  - The population is every raw ever added on HEAD's history plus every raw on
    disk, so a deleted raw is refused, not skipped. The Git query reads every
    commit and every merge parent with rename detection off, so a raw renamed
    into place, or added on a branch whose merge dropped it, still counts.
  - A later change to the recorder needs a new, higher-numbered raw; earlier
    raws stay unchanged. A later review of the same bytes supersedes an
    earlier verdict only by being a fresh review, retained beside it.
- **Where the raws live.** Here, beside the package. `check_governance.py`
  classifies `HISTORY-REVIEW-<n>-RAW.md` in this directory as raw review
  output, like `docs/reviews/*-RAW.md`, so a raw is stored unchanged.
- **Rule-6 evidence.** [`history-reading-rule6.json`](history-reading-rule6.json)
  records each guard's mutant, its fragments and the commit it ran at; each
  one fails the selftest. Two fail by an exception rather than by their named
  refusal; both still fail closed. The Git query's flags are exercised on a
  scratch repository, not a fixture.
- **Review rounds.**
  - Round 1 (`HISTORY-REVIEW-1-RAW.md`, REVISE): M1, a deleted raw was not
    refused, is answered by the Git population; M2, untested predicates, by
    the ten-raw fixture.
  - Round 2 (`HISTORY-REVIEW-2-RAW.md`, REVISE): M1, a raw renamed away or
    dropped by a merge, is answered by the Git query's flags and the
    scratch-repository selftest; N1, malformed names, by their refusal.
  - Round 1's N2 and round 2's N2 (four inputs with no drift mutant) predate
    this change and stay open.
