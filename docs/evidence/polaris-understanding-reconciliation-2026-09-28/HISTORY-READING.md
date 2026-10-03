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
      bytes. Where several performed successors replaced the file in turn,
      their pairs compose into one: see the chain below.
    - The recorder runs the tool only when its sha256 equals the digest pinned
      in the recorder (`SUCCESSOR_TOOL_SHA`), and executes the very bytes it
      hashed. A tool change needs a recorder change and a new history review.
    - A package that is unperformed, or whose config does not load (a
      malformed, deeply nested or wrongly typed config included), grants
      nothing and blocks no other package.
    - Any other package whose tool check fails grants nothing and
      **contests every file it names**: a drifted package whose act record
      and block verify (since round 16, `syzygy-t69g`), and, since round 17
      (`syzygy-lmjg`), one whose act record or block does not verify. The
      recorder refuses those files rather than compose the other packages'
      pairs around them (round 15's N1). Before round 16 a drifted package
      was skipped like a malformed one; before round 17 an act that did not
      verify was skipped too, so editing a refused package's act record
      turned it back into a skipped one (round 16's N1, tree P5). A copy of
      a performed package that names that package's act and fails its check
      contests too, as the tool refuses it.
    - **A file written back to its adopted bytes** is refused when a
      performed successor names it (round 16's N1, tree P10; round 14's N1).
      The row is consulted whenever one exists, not only when the bytes
      differ from the adopted ones, and a written-back file passes only when
      the row keeps the adopted bytes. Before round 17 such a file was
      never compared with its row.
    - **What the recorder alone still accepts** [Inferred, from the code
      at `d9f14202`]: a refused package whose config is then made unloadable
      or whose directory is removed. It is skipped, so the others compose
      around it. Isolating a malformed sibling is the round-7 design (N1),
      so this is not closed here. The tool refuses an unloadable config; a
      removed directory is outside both. The battery, never the recorder
      alone, is the claim.
    - Paths are normalized before they are compared, so `./x` and `x` are
      one path.
    - **The chain** (since round 14). A later successor of a file names the
      earlier successor's row as its predecessor.
      - The tool keeps the earlier package `performed-exact` for that file
        only when today's digest is one a chain of later performed packages
        installed over the earlier row: each step's recorded predecessor is
        the digest the chain has reached, each step's act instant is strictly
        later than the step before (so neither the package itself nor an
        earlier one counts), and each step's own act record and
        acceptance-record block verify. Any other digest is still drift, and
        a package that is unperformed, partial or malformed extends no chain.
        A tie in act instants extends nothing, so it fails closed.
      - The recorder composes every performed-exact package's pair for the
        file into one pair, from the first predecessor to the last row. A
        pair that keeps the bytes composes only when its digest lies on the
        chain. Each step is walked at most once, so a repeated step, two
        steps from one digest, a cycle with no first digest, or a second
        chain or cycle beside the first makes the file contested and
        refused, whatever the packages' order or spelling; other files are
        unaffected. A chain may return to a digest it passed (a step back).
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
  fourth. Fourteen more (round 11) pin its fifth form: the predecessor
  test, the row test, the drift branch, the tool pin, the performed filter,
  both widths of the per-package exception scope, the frozen view's
  delegation, the missing-tool guard, path normalization, the contested
  marking, both halves of the stored row and the contested refusal. Fifteen
  more (round 14, at `ab2a58b`) pinned the chain's first form. Seventeen
  more (round 15) pin its current form. Nine are in the tool: the history
  branch, the predecessor step, the later-instant test, its strictness, the
  performed test, the walk, the per-package scope, the start digest and the
  path key. Eight are in the recorder's composition: the single first
  digest, the walked-step count, the off-chain test, the no-step case, the
  step filter, the last digest, the use of the composition and the
  walk's stop. The tool rows run its own selftest,
  except the path-key row, which runs the recorder's selftest with the tool
  pin moved to the mutant. Nine more (round 16, at `bec7a87c`, rows 112 to
  120) pin the contested marking of a refused performed package: the
  pre-fix composition under both new fixtures, and again under the tie
  fixture alone; a refused package contesting nothing; the contested set
  not applied, or applied only to unclaimed paths; an unperformed package,
  or one whose act does not verify, contesting its paths; the contested
  paths' normalization; and the tool's strict later-instant test, which
  the tie fixture needs (recorder selftest, tool pin moved to the mutant).
  Six more (round 17, at `d9f14202`, rows 121 to 126) pin the two
  residuals of round 16's N1: the pre-fix load scope that skipped an
  unverified act (P5) and an unperformed package contesting its paths; the
  pre-fix row consultation (P10), the written-back test dropped, the same
  test refusing a row that keeps the adopted bytes, and the contested test
  skipped for written-back bytes. Row 123 fails by the fixture's own
  assertion; row 125 fails on the real tree's first kept row, before the
  fixture. Rows with more than one edit carry the rest under
  `further_edits`. One round-16 guard is equivalent and has no row:
  requiring `check()` to return `performed-exact`, since past
  `performed_rows()` it either returns that or raises. Two of the tool's
  guards are equivalent and have no row:
  - Normalizing a later package's path: an aliased later claim can only
    keep its bytes (a changed subject's proposed file has the normal name),
    and a kept claim adds no digest to the chain.
  - Skipping a package with no record: without it, reading its rows raises
    inside the per-package scope, so it still grants nothing.

  Three guards of the earlier forms have no row:
  - The rows cache changes only how often the tool runs.
  - Executing the hashed bytes rather than re-reading the file closes a race
    between the hash and the load, which no deterministic fixture can open.
  - Two exact packages can make the same claim for a changed path: the same
    restyle recorded on two branches and merged. The code marks that path
    contested and refuses it, like any other pair of claimants, but no
    fixture builds two such branches, so the identical-claim case has no row
    of its own.

  Recorded refusals replace temporary directory names with `<tmpdir>`; row
  42 predates that form. Row 120's refusal embeds a set-ordered dict, so
  only its text before the colon reproduces byte for byte (round 16's N2).
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
  - Round 12 (`HISTORY-REVIEW-12-RAW.md`, CONFIRM WITH EXCEPTIONS) bound
    the recorder as it stood then; it reviewed the same recorder bytes as round 11
    with this page corrected. Its notes need no recorder change:
    - N1: the tool finds a package's act block in the acceptance record by
      label substring, so a package whose label is contained in another's
      stops checking exact and neither grants nor contests. What is granted
      is still an exact successor's row from the adopted digest. It is a
      property of the tool, for the tool's next change.
    - N2: a failure in the package search itself, or a symlinked tool, fails
      the whole check rather than one package. That is fail-closed.
    - N3 stands as round 9's N4.
  - Round 13 (`HISTORY-REVIEW-13-RAW.md`, CONFIRM WITH EXCEPTIONS) bound
    the recorder as it stood then. A simulated adoption of the understanding
    successor had shown the recorder's own selftest refusing the installed
    restyle, because its fixture granted no successor rows. The fixture now
    starts from today's performed successors and builds its successor cases
    from the adopted bytes, so the selftest passes before and after the
    successor is performed. Its notes:
    - N1: once the successor is performed, row 68 (the drift branch forced
      on) survives, since every subject then has a successor row. That
      mutation only makes the check stricter; the row reproduces before
      adoption.
    - N2: after adoption, rows 66, 73, 77 and 79 are still killed, with
      different refusal text. Each row's refusal describes the tree at its
      recorded commit.
  - Round 14 (`HISTORY-REVIEW-14-RAW.md`, REVISE) reviewed the chain's
    first form. M1, a repeated step padding the recorder's walk to the step
    count, is answered by walking each step at most once (which also refuses
    a step back beside a separate cycle). M2, the tool following earlier
    packages' steps, and M3, the tool following the package's own step from
    a second spelling of one file, are answered by requiring each step's act
    instant to be strictly later than the step before. N1, the recorder
    ignoring a later package that fails its tool check, predates the chain
    for an undone honest chain, but not for every case: see round 15's N1.
    N2 is answered by the docstring; N3 by the act-instant ordering; N4
    needed no change.
  - Round 15 (`HISTORY-REVIEW-15-RAW.md`, CONFIRM WITH EXCEPTIONS, notes
    only) bound the recorder as it stood then. Under the 2026-09-26 stopping
    rule its notes are answered here, not in the reviewed bytes:
    - N1: after A→B, B→C, C→B at increasing instants and a no-act edit
      back to C, the tool refuses the C→B package, and the recorder, which
      skips any package the tool fails, composes (A, C) from the other two
      and passes. Both earlier recorders refused that tree. It is a
      recorder-only false green: the canonical battery stays red because it
      also runs `readability_successor.py --all --check`, so the battery,
      never the recorder alone, is the claim. The repair (a package whose
      act verifies but whose check fails contests its paths) is tracked as
      `syzygy-t69g`, for the tool's next change. Answered in round 16 by
      that repair and its fixture.
    - N2: two acts recorded within one second leave the earlier package
      refused, since a tie extends no chain. That fails closed; the remedy
      is a successor recorded at a later instant.
    - N3: a two-package tie fixture joins N1's follow-up. Answered in
      round 16 by that fixture.
    - N4 and N5 describe the review's own probes and need no change.
  - Round 16 (`HISTORY-REVIEW-16-RAW.md`, CONFIRM WITH EXCEPTIONS, notes
    only) binds the current recorder, with the contested marking above.
    Under the 2026-09-26 stopping rule its notes are answered here, not in
    the reviewed bytes:
    - N1: this page claimed the recorder could no longer accept any tree
      the tool refuses. The claim is narrowed above, naming both residuals;
      the battery, never the recorder alone, is the claim. Both residuals
      are closed in round 17's change (`syzygy-lmjg`).
    - N2: row 120's refusal is not byte-reproducible; noted at the
      rule-6 rows above.
    - N3: a refused package contests every path it names, so drift on a
      path no adopted subject depends on can contest an adopted one. That
      matches the tool and fails closed.
  - Notes answered here, not in code: round 1's N3 (this page quotes the
    frozen README sentence), N4 (a later verdict supersedes only as a fresh,
    retained review), N5 (two mutants fail by exception) and N6 (the raws
    are raw review output); round 2's N3 and round 3's N1 (this list).
  - Round 1's N1 (performance judged by line shape) is by design: the C1
    digest is fixed and already performed.
  - Round 1's N2, round 2's N2 and round 3's N4 (four inputs with no drift
    mutant) predate this change and stay open.
