# Polaris understanding reconciliation review 1 — D8 (d2) vision.md
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 01fa6d66215472d0a5e58fa8a3f8e84511337e7e
- `.syzygy/governance/doctrine/vision.md`: `ff8410443dee3b53e4c8aad2e3b4072239e18ca9c16e3bef2518c8a44ae9ceeb`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/README.md`: `57a6af1c4a56c5307c6455d5597e634463a21472386f421e0f8b04f1856bb66d`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/documentation-images.json`: `4feab500ead279f8ff6d9a2926bc670d59c47aa9a4a5856fcd7fb49fe41eb75f`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/final-documentation.patch`: `ed48053cd991a2c5703d485aa9958bbdef458d1b38d34858b9a6a3b92e20c5de`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/proof.json`: `0d61eb32066d9ceebc41e2f8ff9ce964cd47cd6162f843cbb9caf9ef264e1712`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/review-inputs.json`: `821058ffe4f190b189e77901100aa00fa83abf0322228c4e78403e23ad1bc8e0`
- `docs/evidence/polaris-understanding-reconciliation-2026-09-28/technical-record-template.json`: `582f5be9a744254e7ebc3c0ea79907d1dca92d9511c78c4807a7ea257ead9ecb`

Reviewer: independent fresh-context agent, 2026-10-15. This review is
evidence for the owner, never an owner act (VIS-4). It reviews the amended
`vision.md` and the reconciliation's frozen inputs; the recorder change is
out of scope beyond interpreting its inputs.

## Method

Scratch clone of `/home/tze/GitHub/syzygy`, branch
`doctrine/d8-d2-reconciliation` fetched, detached at the reviewed commit;
`git rev-parse HEAD` returned `01fa6d66215472d0a5e58fa8a3f8e84511337e7e`
and `git status --porcelain` was empty before and after the checks
[Observed]. All digests above and below were computed by `sha256sum` and by
a Python `hashlib` script over `git show <rev>:<path>` blobs and the on-disk
files (both agreed; the on-disk `vision.md` equals the HEAD blob)
[Observed]. The comparison base is `a4a864e6` (origin/main at the branch
point, the parent chain of the three branch commits).

## Revise-level findings

None.

## Tests

**T1 — What the C1 reconciliation relied on `vision.md` for, and whether
(d2) alters it.**
[Observed] `vision.md` appears in the C1 package only as a row of
`review-inputs.json` and as a binding line of `REVIEW-RAW.md` (at the
digest 93cc5fbbfe8ba07643d097007500f772c7b4ba1f3d5a1ac792c6e4bf74f0506d).
A case-insensitive grep for `vision` and `VIS-` over `proof.json`,
`technical-record-template.json`, `review-inputs.json`,
`final-documentation.patch` and `documentation-images.json` finds only that
one `review-inputs.json` row; `POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`
contains neither string. The only doctrine reliance in the package's prose
is the package `README.md` quoting CC-SPEC-10: "Lawful adoption under VIS-4
is recorded at the exact digest, and the record quotes what was adopted at
which digest." The C1 raw's substantive judgment is that the owner-to-blob
correspondence satisfies CC-SPEC-10; it quotes no `vision.md` text.
[Inferred] So C1 relied on `vision.md` as the governing reference for VIS-4
(owner adoption authority, which CC-SPEC-10 cites), frozen so that its
review would retire if that authority text moved.
[Observed] The whole diff `a4a864e6..HEAD` on `vision.md` is one hunk,
`@@ -234,0 +235,10 @@`: ten added lines, no deleted line. VIS-4 begins at
line 168 and VIS-5 at 193, both before the insertion point, so VIS-4's bytes
are untouched; VIS-6 heading stays at 229 and VIS-7 moves from 250 to 260.
[Inferred] (d2) adds a destination rule for content Syzygy authors about an
observed-only project. It says nothing about owner adoption, specification
acceptance, exact-digest recording, or supersession, which is everything
the reconciliation's CC-SPEC-10 judgment turns on. It therefore changes
nothing the C1 reconciliation relied on `vision.md` for. See N1 for the one
adjacent question it does raise, which is outside the reconciliation.

**T2 — (d2) bytes equal the packet's Insert 2 fence and sit after
pre-amendment line 234, as a sub-bullet.**
[Observed] The packet has exactly one `**Insert 2**` heading
("after line 234, as a sub-bullet of that bullet:"). The script extracted
the `markdown` fence body under it: 10 lines, 709 bytes, sha256
e57f84b0cfa770802bcd880009d3875feb3096384b6e4407d4aad73b80adb3db. Base
`vision.md` lines 232–234 equal the packet's Anchor 2 quote exactly ("- **Syzygy's
databases and views are projections.** Content it authors is / committed
out to the governed plane, which then becomes the authoritative / source.").
The assertion `HEAD bytes == base lines 1–234 + fence + base lines 235–end`
is true, and the lengths agree (17167 + 709 = 17876). The fence's only
non-ASCII character is U+2014 (em dash), identical in both. The inserted
first line is indented two spaces with `- `, under a top-level `- ` bullet
at line 232, so it is a sub-bullet of "**Syzygy's databases and views are
projections.**", before "**The only exceptions:**".
[Observed] `OWNER-DECISION-PACKET.md` is byte-identical at `a4a864e6` and
HEAD, and `git diff --stat 79f51fdfa5350feb747162af91137758dc3b38ed HEAD`
over the D8 package directory shows only `ROUND-4-DISPOSITIONS.md` added
(104 lines); the packet itself is unchanged since the round-4 reviewed
commit cited in row D8 of `DOCTRINE-AMENDMENT-LOG.md`. So the applied bytes
are the bytes that round cleared and the owner adopted.

**T3 — No other `vision.md` byte moved.**
[Observed] Base `vision.md` at `a4a864e6` hashes to
93cc5fbbfe8ba07643d097007500f772c7b4ba1f3d5a1ac792c6e4bf74f0506d, the C1
binding and the brief's anchor digest. The T2 reconstruction is exact over
the whole file, and the diff has zero deleted lines; no other byte differs.
HEAD hashes to ff8410443dee3b53e4c8aad2e3b4072239e18ca9c16e3bef2518c8a44ae9ceeb,
the digest the brief's 2026-10-15 probe predicted for (d2) applied.

**T4 — The six other frozen inputs are unchanged since C1.**
[Observed] Parsed from `REVIEW-RAW.md` (13 binding lines) and compared by
script; each file's on-disk bytes, HEAD blob and `a4a864e6` blob are equal:

| File (under the evidence directory) | Equals C1 binding |
|---|---|
| README.md | yes |
| documentation-images.json | yes |
| final-documentation.patch | yes |
| proof.json | yes |
| review-inputs.json | yes |
| technical-record-template.json | yes |

The full digests are the binding lines in this file's head.
`review-inputs.json` still lists `vision.md` at the C1 digest, consistent
with `HISTORY-READING.md`'s statement that the original freeze reads
`vision.md` at C1.

**T5 — The dismissal is dropped from (d2) as the owner directed.**
[Observed] `OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md` line 31,
P-102 (D8): "Drop dismissal from (d2)", with the rationale "Dismissals of an
observed-only project's gaps can't live in the observing project's tree, so
VIS-6 stays intact." The applied (d2)'s example list of content committed to
the observing project is "a promoted annotation, an attributed answer"; "a
dismissal" is gone from it (the packet's repair note records the replaced
text "a promoted note, a dismissal, an attributed answer"). (d2) adds
"never suppresses a gap of the project" and closes: "A dismissal of such a
project's gap is not committed there: it takes effect only in the project's
own governed plane, so it waits for an act that names that write."
[Inferred] That is the owner's direction carried out: dismissals are no
longer among the content (d2) sends to the observing project's tree, and
the remaining mention excludes them, restating the owner's own rationale
and VIS-6's existing violation sentence ("a dismissal taking effect without
living in the governed plane"). See N2.

**T6 — Recorder state at the reviewed commit (context only).**
[Observed] `python3 scripts/record_polaris_understanding_adoption.py --check`
in the clone printed
`FAIL exact digest reconciliation unresolved: review retired by changed input: .syzygy/governance/doctrine/vision.md`
and exited 1. [Inferred] That is the expected state before a fresh
reconciliation raw is retained; per `HISTORY-READING.md` the recorder reads
such raws only at `docs/reviews/R-POLARIS-UNDERSTANDING-RECONCILIATION-<n>-RAW.md`.
This review did not test the recorder's acceptance of this raw.

## Notes

**N1 — (d2) may bear on Polaris output about Butlers; not a reconciliation
question.** [Inferred] The D8 packet treats Butlers (empty `writeSurface`)
as the case an observed-only project names. Polaris generation authors
content about Butlers, so a later reader may ask whether (d2) now governs
where committed Polaris output lives. That is a doctrine-to-specification
impact question for the Polaris generation specification, not part of the
CC-SPEC-10 digest correspondence this package reconciles, and row D8
records Q-C3's answer that a Polaris synthesis stays an `editorial-draft`.
[Unknown] Whether any committed Polaris artifact is "content Syzygy
authors about such a project" under (d2) was not evaluated here.

**N2 — "Drop dismissal" read as dropping it from what (d2) commits, not
from (d2)'s text.** [Inferred] The word "dismissal" still occurs twice in
(d2), both in the excluding sentence. A strictly literal reading of "Drop
dismissal from (d2)" could expect no mention at all; the owner's rationale
and the round-4 clearance support the reading taken here. Flagged so the
owner can confirm the reading if it matters.

**N3 — A stale qualifier in the bound packet.** [Observed] The packet's
repair note under Insert 2 says the owner ruling is "[Observed: as relayed
by the lead session to this repair lane; not yet recorded under
`decisions/`.]"; it is now recorded in
`OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`. The packet is a
cleared, adopted subject and must stay unedited; this affects no byte under
review.

**N4 — Retention path.** [Observed] This raw was written to a scratchpad
path as dispatched. The recorder admits it only once retained verbatim at
`docs/reviews/R-POLARIS-UNDERSTANDING-RECONCILIATION-1-RAW.md`, on a commit
satisfying `HISTORY-READING.md`'s retention rules, with the
`docs/README.md` campaign row the same bullet anticipates.
