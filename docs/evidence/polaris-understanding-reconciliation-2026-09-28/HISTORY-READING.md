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
  - Any file in this directory or below whose name contains
    `history-review`, in any case, and is not exactly
    `HISTORY-REVIEW-<n>-RAW.md` at the top level with no leading zero, is
    refused, never skipped.
- **Every history review is retained.**
  - Each raw's introducing commit holds the same bytes as today.
  - The population is every raw ever added on HEAD's history plus every raw on
    disk, so a deleted raw is refused, not skipped, and a raw on disk that no
    commit added is refused as not retained.
  - The Git query reads every commit and every merge parent, with rename
    detection off and merge commits' own additions shown. A raw renamed into
    place, added on a branch whose merge dropped it, or added by a merge
    commit itself still counts.
  - Each raw is added exactly once. A number added on two branches, so that a
    merge could keep either verdict, is refused.
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
  - Round 3 (`HISTORY-REVIEW-3-RAW.md`, REVISE): M1, a raw replaced through
    a merge or added by a merge commit, is answered by the added-once rule and
    by showing merge commits' additions; N2, lowercase or nested names, by
    the wider malformed-name refusal; N3, two surviving mutants, by an
    uncommitted-raw witness and a narrower exemption test.
  - Notes answered here, not in code: round 1's N3 (this page quotes the
    frozen README sentence), N4 (a later verdict supersedes only as a fresh,
    retained review), N5 (two mutants fail by exception) and N6 (the raws
    are raw review output); round 2's N3 and round 3's N1 (this list).
  - Round 1's N1 (performance judged by line shape) is by design: the C1
    digest is fixed and already performed.
  - Round 1's N2, round 2's N2 and round 3's N4 (four inputs with no drift
    mutant) predate this change and stay open.
