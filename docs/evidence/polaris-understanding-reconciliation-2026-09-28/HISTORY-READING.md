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
  - One exception: a subject may differ from its adopted bytes when a
    performed readability successor replaced it.
    - The successor must check as `performed-exact` under
      `scripts/readability_successor.py`; its recorded predecessor for that
      file must equal the adopted digest, and its row must equal today's
      bytes.
    - The recorder runs the tool only when its sha256 equals the digest pinned
      in the recorder (`SUCCESSOR_TOOL_SHA`), and executes the very bytes it
      hashed. A tool change needs a recorder change and a new history review.
    - A package that is unperformed, drifted, malformed (a deeply nested or
      wrongly typed config included) or fails to check grants nothing and
      blocks no other package.
    - Paths are normalized before they are compared, so `./x` and `x` are
      one path. Two performed-exact packages claiming one path are refused
      for that path, whatever their order or spelling; other paths are
      unaffected.
    - A second restyle of these subjects names the first restyle's bytes as
      its predecessor, so the recorder refuses it until it learns that chain.
    - What stays trusted: the act record, the acceptance-record block and the
      review raw the tool reads are read from the working tree, as the
      recorder reads its own act. A forged owner act is not detected here or
      anywhere else in the tooling.
- **What binds the recorder now.** Its current bytes must equal the digest
  that the latest `HISTORY-REVIEW-<n>-RAW.md` in this directory binds.
  - That raw carries exactly one `Verdict:` header, `CONFIRM` or
    `CONFIRM WITH EXCEPTIONS`.
  - It carries exactly one line
    `` - `scripts/record_polaris_understanding_adoption.py`: `<sha256>` ``.
  - "Latest" is the highest `<n>`, compared as a number; the raws are
    numbered 1 to n with no gap.
  - Any file in this directory or below whose basename matches the pattern
    `history[^a-z0-9]*review` (a case-insensitive search: the word history,
    any run of characters other than ASCII letters and digits, including
    none, then the word review) and is not exactly
    `HISTORY-REVIEW-<n>-RAW.md` at the top level with no leading zero, is
    refused, never skipped. So `HISTORY_REVIEW-5-RAW.md`,
    `History Review 5.md` and `HistoryReview-5-RAW.md` are refused, whether on
    disk or committed and later deleted.
- **Every history review is retained.**
  - Each raw's introducing commit holds the same bytes as today.
  - The population is every raw ever added on HEAD's history plus every raw on
    disk, so a deleted raw is refused, not skipped, and a raw on disk that no
    commit added is refused as not retained.
  - The Git query reads every commit and every merge parent, with rename
    detection off and merge commits' own additions shown. Its output is
    NUL-separated (`-z`), so a non-ASCII name is not quoted away and a name
    holding a newline is not split; a name committed and then deleted is
    refused as it is on disk. A raw renamed into
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
  one fails the run named by its row (the recorder selftest, except the one
  row that names the governance checker's selftest). Some fail by an
  exception or a fixture's own assertion rather than by their named refusal;
  each still fails closed. The Git query's flags and the disk listing are
  exercised on a scratch repository, not a fixture. The two round-3
  witnesses (dropping `| set(listed)`, and widening
  the checker's raw-review exemption from a full match to a search) and the
  guards for the NUL split and the near-miss pattern each have their own row.
  Three more rows (round 6) pin the separator class, `search` against `match`,
  and the NUL split against a newline split. Five more (round 7) pin the
  first form of the successor exception, and seven more (round 8) its second.
  Ten more (round 9) pin its third form, and twelve more (round 10) its
  fourth. Fourteen more (round 11) pin its current form: the predecessor
  test, the row test, the drift branch, the tool pin, the performed filter,
  both widths of the per-package exception scope, the frozen view's
  delegation, the missing-tool guard, path normalization, the contested
  marking, both halves of the stored row and the contested refusal. Three
  guards have no row:
  - The rows cache changes only how often the tool runs.
  - Executing the hashed bytes rather than re-reading the file closes a race
    between the hash and the load, which no deterministic fixture can open.
  - Two exact packages can make the same claim for a changed path: the same
    restyle recorded on two branches and merged. The code marks that path
    contested and refuses it, like any other pair of claimants, but no
    fixture builds two such branches, so the identical-claim case has no row
    of its own.

  Recorded refusals replace temporary directory names with `<tmpdir>`; row
  42 predates that form.
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
  - Round 4 (`HISTORY-REVIEW-4-RAW.md`, CONFIRM WITH EXCEPTIONS) bound the
    recorder as it stood then. Its four notes are answered as follows:
    - N1, a non-ASCII malformed name refused only while on disk, by the NUL
      split above.
    - N2, a near-miss name without `history-review` skipped, by the wider
      pattern above.
    - N3, two witnesses without a rule-6 row, by their own rows.
    - N4 is not a code change. A committed malformed or twice-added raw makes
      `--check` fail, and stays failing: that is the fail-closed polarity, and
      no clearing mechanism exists. Clearing one needs an owner decision; none
      has been taken.
  - Round 5 (`HISTORY-REVIEW-5-RAW.md`, CONFIRM WITH EXCEPTIONS) bound the
    recorder as it stood then. Its notes 1 to 3 (the separator class and
    `search` unpinned, no fixture for the NUL split, two benign survivors) are
    answered by round 6's change, recorded in
    [`RECORDER-REVIEW-NOTES.md`](RECORDER-REVIEW-NOTES.md); note 4 is enforced
    only by the dispatch brief.
  - Round 6 (`HISTORY-REVIEW-6-RAW.md`, CONFIRM) bound the recorder after
    round 5's three selftest fixtures (22 real-Git cases, was 16).
  - Round 7 (`HISTORY-REVIEW-7-RAW.md`, REVISE) reviewed the first form of
    the successor exception. M1, the tool ran unbound, is answered by the tool
    pin. N1, a malformed sibling package failing the whole check, by
    per-package isolation. N2, ranking by directory name, first by a
    displacement rule that round 8 showed false, and now by the two-claimant
    refusal. N3, trust in working-tree acts
    and raws, by the disclosure above. N4, four guards without a row, by the
    round-8 rows. N5, repeated tool loads, by the rows cache. N6 needed no
    change.
  - Round 8 (`HISTORY-REVIEW-8-RAW.md`, REVISE): M1, two packages could
    both check exact for one path with directory order deciding, is answered
    by the two-claimant refusal. N1, a deeply nested config escaping the
    exception scope, by catching `RecursionError`. N2, three guards without
    a row, by the round-9 rows. N3, a temporary path in
    a refusal, by the `<tmpdir>` form. N4, a second read of the tool, by
    executing the hashed bytes, which the selftest now loads the same way.
  - Round 9 (`HISTORY-REVIEW-9-RAW.md`, REVISE): M1, a wrongly typed
    sibling config escaping the per-package scope, is answered by containing
    every exception there and three wrongly typed fixtures. N1, guards
    without a row, by the round-10 rows and the two no-row statements above.
    N2, a stale count of exception failures, and N3, a stale reference, by
    this page. N4, a two-claimant refusal blocking unrelated paths, by
    refusing only the contested path. N5, an unused import, removed.
  - Round 10 (`HISTORY-REVIEW-10-RAW.md`, REVISE): M1, a differently
    spelled path escaping the contested refusal, is answered by path
    normalization and an aliased-claimant fixture. N1, an untested
    `AttributeError` and an untested identical-claim branch, by a
    listed-pins fixture and the no-row statement above. N2, one long line,
    by this page. N3 stands as round 9's N4.
  - Round 11 (`HISTORY-REVIEW-11-RAW.md`, REVISE): M1, a false claim that
    identical claims change no outcome, is answered by the corrected no-row
    statement above; the code already refused them. N1 (three long lines) by
    this page's line 87; lines 9 and 81 hold a link and a code span and stay
    whole. N2, one package naming a file twice, fails closed and needs no
    change. N3 stands as round 9's N4.
  - Round 12 (`HISTORY-REVIEW-12-RAW.md`, CONFIRM WITH EXCEPTIONS) binds
    the current recorder; it reviewed the same recorder bytes as round 11
    with this page corrected. Its notes need no recorder change:
    - N1: the tool finds a package's act block in the acceptance record by
      label substring, so a package whose label is contained in another's
      stops checking exact and neither grants nor contests. What is granted
      is still an exact successor's row from the adopted digest. It is a
      property of the tool, for the tool's next change.
    - N2: a failure in the package search itself, or a symlinked tool, fails
      the whole check rather than one package. That is fail-closed.
    - N3 stands as round 9's N4.
  - Notes answered here, not in code: round 1's N3 (this page quotes the
    frozen README sentence), N4 (a later verdict supersedes only as a fresh,
    retained review), N5 (two mutants fail by exception) and N6 (the raws
    are raw review output); round 2's N3 and round 3's N1 (this list).
  - Round 1's N1 (performance judged by line shape) is by design: the C1
    digest is fixed and already performed.
  - Round 1's N2, round 2's N2 and round 3's N4 (four inputs with no drift
    mutant) predate this change and stay open.
