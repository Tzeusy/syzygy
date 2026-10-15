# Owner direction — a second repair-and-review cycle for eight amendment packets (2026-10-14)

> **A plain owner direction.** It binds no digest, adds no row to
> `ACCEPTANCE-ACT-RECORD.md`, registers nothing in
> `scripts/check_governance.py`, and performs no act. It signs, adopts and
> rules nothing on any packet's content questions (VIS-4). It records why a
> second repair and a further review round ran for the eight packets the
> first cycle left `REVISE`, and what each round returned.

## The direction

The first cycle
([`OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`](OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md))
left eight packets `REVISE`: P-84, P-85, P-86, P-98, P-99, P-100, P-101 and
P-102. Later on 2026-10-14, in the lead Claude Code session and in answer
to a structured question, the owner selected the option:

> "One more cycle (Recommended)" — "Repair each packet's findings, notes
> included, then one fresh review, under the same stopping rule. Anything
> that comes back notes-only clears, and anything still REVISE comes back
> to you."

[Observed: the option label and its text as the lead session relayed them
to this integration; the owner's answer itself is in that session, not in
this repository.]

**The stopping rule, stated with the direction:** one repair of every
finding, notes included, and one fresh review per packet.

- A round with no revise-severity or blocking finding (`CONFIRM`, or
  `CONFIRM WITH EXCEPTIONS` with notes only) clears the exact bytes it
  read, under the owner's 2026-09-26 ruling
  (`POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1). Its notes go in a
  sibling record beside the package, and the package is not edited.
- A round still `REVISE` comes back to the owner with its findings open.
  The package is not repaired again, and no further round is dispatched
  without a new owner direction.
- A verdict is never re-labelled. A clearance is not a sign-off.

Each package's review brief carried this rule in a section written before
its round ran. This record is the `decisions/` record that those sections,
and the D7 round-3 raw's note 6, say was missing.

## The repairs

Each repair was one pull request, rebase-merged to `main` on 2026-10-14.

| Packet | Package | Repair PR | Merged commit |
|---|---|---|---|
| P-101 | `doctrine-amendment-held-derived-computation-d7` | #417 | `7071a7440fbf85e8d12f13e804dbd57af400a453` |
| P-102 | `doctrine-amendment-inferred-first-class-d8` | #419 | `b913d1ef37b8e6fc5dffe65b113285f00eb8ab8c` |
| P-84 | `three-surface-poc-identity-amendment` | #421 | `0ea9b4912aceb2b18fd9c080c0a660350140d3d7` |
| P-86 | `pwb-class-granular-extraction-amendment` | #422 | `c88a621f483b8a702c15b3bcb6f894252a9b0af5` |
| P-100 | `three-surface-poc-governing-intent-amendment` | #423 | `52c1d0f5536260628de7633126ef21748fe5e95e` |
| P-85 | `pwb-release-label-amendment` | #424 | `8acb0795562c548201e24eb6a20d8eddc66f04d1` |
| P-98, P-99 | `pwb-opening-index-amendment`, `pwb-accessible-name-amendment` | #425 | `d6b3784f5b7f09b27ffb41f57785282b7393c4d1` |

[Observed 2026-10-14: each PR number and merge commit from `gh pr list
--state merged`; each commit is an ancestor of this record's branch.] The
P-97 sign-off (`7f43802f`, #420) moved the signed POC and PWB trees between
these repairs, so the later repairs were regenerated over it.

## What each round returned

Every verdict word below is copied from the raw file at the line cited.
Each head digest is the one on the raw's own head line. Every raw is
retained verbatim under `docs/reviews/` (CC-REV-6); there are eight, one
per package (P-98 and P-99 share a brief but each has its own raw).

| Packet | Round | Raw | Reviewed commit | Head digest (raw line) | Verdict (raw line) | Revise / notes |
|---|---|---|---|---|---|---|
| P-84 | 6 | `R-M9-POC-IDENTITY-AMENDMENT-6-RAW.md` | `0ea9b4912aceb2b18fd9c080c0a660350140d3d7` | Manifest SHA-256 `a1c00c7cba872468df752427d358199101a34b62f0ffe77eabe369e23e4b9867` (3) | `REVISE` (4) | 2 / 3 |
| P-85 | 4 | `R-PWB-RELEASE-LABEL-AMENDMENT-4-RAW.md` | `8acb0795562c548201e24eb6a20d8eddc66f04d1` | Manifest SHA-256 `73cca446620b99bc6626adcc2530817fb4ef2c55d6a428d20f16150077fbca61` (3) | `REVISE` (4) | 1 / 7 |
| P-86 | 4 | `R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-4-RAW.md` | `c88a621f483b8a702c15b3bcb6f894252a9b0af5` | Manifest SHA-256 `4d398a75284cf1dd56d6f0e3a71af68f9daacfea6457b609ff5d319b10518be2` (3) | `CONFIRM WITH EXCEPTIONS` (4) | 0 / 4 |
| P-98 | 3 | `R-PWB-OPENING-INDEX-AMENDMENT-3-RAW.md` | `d6b3784f5b7f09b27ffb41f57785282b7393c4d1` | Manifest SHA-256 `b091f9dcd646bbe25f3eaa2b8086463595ad76c8f328c4935ec8efcf5c2662e2` (3) | `REVISE` (4) | 1 / 9 |
| P-99 | 3 | `R-PWB-ACCESSIBLE-NAME-AMENDMENT-3-RAW.md` | `d6b3784f5b7f09b27ffb41f57785282b7393c4d1` | Manifest SHA-256 `8dfd6d836402b81a995c44f1435354d3ce2bef735daa399692e6c4dbe9f8bae0` (3) | `CONFIRM WITH EXCEPTIONS` (4) | 0 / 10 |
| P-100 | 3 | `R-N10-POC-GOVERNING-INTENT-3-RAW.md` | `52c1d0f5536260628de7633126ef21748fe5e95e` | Package digest `9d97c13d78689784f0f85556821e04ae72b0dd338b372d7bdb8ccc651a8bbbcc` (3) | `CONFIRM WITH EXCEPTIONS` (4) | 0 / 7 |
| P-101 | 3 | `R-DOCTRINE-AMENDMENT-D7-3-RAW.md` | `7071a7440fbf85e8d12f13e804dbd57af400a453` | Package digest `cc9709730aeab80f51256b57f1ac5d27515d9be229f3e957df6c66524af1490f` (3) | `REVISE` (4) | 1 / 5 |
| P-102 | 3 | `R-DOCTRINE-AMENDMENT-D8-3-RAW.md` | `b913d1ef37b8e6fc5dffe65b113285f00eb8ab8c` | Package digest `801ad3c05edb70f87784e8129ea2da6414518fe48a6f4c2cb5a096dfde35eaad` (3) | `REVISE` (4) | 1 / 4 |

[Observed 2026-10-14] Every revise and note count above was re-derived by
script from each raw's finding headings and their severity words. It
agrees with each raw's own closing count where it has one (P-84 raw line
364, P-85 line 206, P-86 line 122, P-100 line 59, P-101 line 262, P-102
lines 310–311). The P-98 raw has no closing count; its line 119 says "The
one revise finding is against criterion 3". The P-99 raw has none either;
its line 130 says "Every finding below is a note." No round raised a
blocking finding. The P-84 raw numbers its findings 39–43, continuing from
round 5.

[Observed 2026-10-14] Each head digest was recomputed from the bytes at
the reviewed commit, and each matches:

- for the five manifest-bound packages, the manifest file's sha256;
- for P-100, P-101 and P-102, each brief's directory method: `sha256sum`
  over the sorted `git ls-files` of the package directory, hashed again.
  That is ten files for P-100 and six each for P-101 and P-102.

## Outcome

- **P-86, P-99 and P-100 clear.** Each returned notes only, which clears
  the exact bytes it read at the digest above. The notes are dispositioned,
  open, in a sibling record beside each package:
  - P-86: `pwb-class-granular-extraction-amendment/ROUND-4-DISPOSITIONS.md`;
  - P-99: `pwb-accessible-name-amendment/ROUND-3-DISPOSITIONS.md`;
  - P-100: `three-surface-poc-governing-intent-amendment/ROUND-3-DISPOSITIONS.md`.

  No other file in those three packages is edited. Their stale "pending
  round N" sentences are corrected in the sibling records instead. A
  clearance is not a sign-off: each packet's content questions are still
  the owner's to answer.
- **P-84, P-85, P-98, P-101 and P-102 are `REVISE` and come to the owner
  with their findings open.** Under the stopping rule none is repaired
  again and no further round is dispatched. Each has a dispositions record
  for this round beside its package, which classifies its findings and
  repairs nothing:
  - P-84: `ROUND-6-DISPOSITIONS.md`;
  - P-85: `ROUND-4-DISPOSITIONS.md`;
  - P-98, P-101 and P-102: `ROUND-3-DISPOSITIONS.md`.
- Register rows P-84…P-86 and P-98…P-102 in `PENDING-OWNER-DECISIONS.md`
  say this, with one dated header note and a recount. Nothing is ruled,
  signed or adopted.

## Integration facts

These are [Observed 2026-10-14] on branch
`governance/confirmation-cycle-2-2026-10-14` over `origin/main`
`8acb0795`.

- **The three cleared packages are unchanged since their reviewed
  commits.** `git diff --stat` from each reviewed commit to this branch's
  base is empty over the P-86 package directory and its builder, over the
  P-99 package directory, its builder and the shared brief in
  `pwb-opening-index-amendment/REVIEW-BRIEF.md`, and over the P-100
  package directory.
- **Sibling composition holds at this base.** All four pending PWB
  builders' `--check` pass here: release-label, class-granular,
  accessible-name and opening-index. That includes the release-label
  builder, which every PWB raw of this cycle except P-85's own found
  failing at its reviewed commit. P-85's regeneration (`8acb0795`) landed
  after those reviews. The P-84 builder's `--check` passes. P-100's four
  patches pass `git apply --check` against the signed tree. This
  discharges, at this commit only, the composition step the P-86 raw's
  note 4 and the P-98 and P-99 raws' note 10 asked to re-run. It does not
  touch the `design.md` and `CAPABILITY-COVERAGE.md` collision between
  P-85 and P-86 (the P-85 raw's note 8), which P-86's Q5 still routes to
  regeneration.
- **Status marks.** In the five `REVISE` packages, the stale "unconfirmed
  pending round N" sentences in the packet, delta, ledger and latest
  dispositions record were marked at the sentence, dated, with the old
  text kept. Raws, review briefs and act-bound files are not edited.
  Before editing, each target file's sha256 was swept across all 2,691
  tracked files. None was cited in full or by a 12-character prefix.
- **Package digests that move.** The P-101 and P-102 directory digests
  cover every tracked file in their packages, so the new dispositions
  records and the status marks move them away from the digests above:
  - P-101: `cc9709730aeab80f51256b57f1ac5d27515d9be229f3e957df6c66524af1490f`
    → `059a5119071b07f06a0e785d8bd75c97c3f512c39064f5e4d33274f5b4f45b44`
    (seven files);
  - P-102: `801ad3c05edb70f87784e8129ea2da6414518fe48a6f4c2cb5a096dfde35eaad`
    → `1d2508948989c46e3dbd72c74dad349faf2eb59b51655b6b289ca3d27a20fba2`
    (seven files).

  Neither is cleared, so no clearance is retired. The P-100 directory now
  also holds `ROUND-3-DISPOSITIONS.md`, which its round-3 brief placed
  there, so the brief's command over the whole directory gives
  `b9c9c5b4335da12c663cfd7cab85649638761a088a43981b1bdb37cfdfb72b66`
  (eleven files). The cleared digest stays the one over the ten files the
  round read; over those ten on this branch the method still gives
  `9d97c13d78689784f0f85556821e04ae72b0dd338b372d7bdb8ccc651a8bbbcc`. The
  sign-off recorder treats sibling `ROUND-<n>-DISPOSITIONS.md` records as
  outside the package bytes (`scripts/record_versioned_signoff.py`,
  docstring item 5).

## Residuals for the sign-off recorder

[Observed 2026-10-14] None of the three cleared packages is registered in
`scripts/record_versioned_signoff.py`'s package table yet, so none can be
recorded until it is. Run against the raws:

- the P-86 and P-99 raws parse: one `Manifest SHA-256:` and one `Verdict:`
  line each in the head, and every finding a note;
- the P-100 raw's head carries `Package digest:`, not `Manifest SHA-256:`,
  so `parse_head` refuses it: "review head does not carry exactly one
  `Manifest SHA-256:` line". Its findings section parses (seven findings,
  all notes). Signing P-100 on this raw needs recorder support for a
  directory-digest head. The raw is not edited.
