# Round 7 dispositions — public-source screening scope, version 2

> **Candidate — binds nothing.** Record for
> `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-7-RAW.md` (verdict CONFIRM WITH
> EXCEPTIONS; findings 1 to 5, all notes), written 2026-10-07. The raw is
> retained verbatim. No digest is copied here.

## Stopping rule

Round 7 was run on the owner's direction of 2026-10-07 ("run round 7 on
screening scope version 2 now"; `decisions/REDIS-LOCAL-AGENT-SITTING-DIRECTION.md`).
Under the owner's notes-only rule, a notes-only round clears its bytes. None of
the five notes is repaired in the reviewed bytes: each is carried here, so the
bytes the recorder freezes are the bytes round 7 read, apart from the packet's
review-state statement (note 5). This record dispatches no round 8. Item D of
the sitting brief can be offered at the structured-question step.

## Machine-readable binding

Reviewed record: .syzygy/governance/contracts/candidates/public-source-screening-scope-v2/reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-V2-7-RAW.md
Revise-severity findings: 0

## What changed after the review

One edit, in the commit that retains the raw: the packet's review-state
statement (its lines 7 to 11), replaced by a dated statement naming this raw
and its verdict. It replaces the sentence note 3 faults ("the policy bytes were
confirmed correct"), so that stale sentence is gone rather than marked. No
policy byte, patch, manifest row, generated block, semantic delta, brief or
ledger byte changed.

## Dispositions

### 1 — the review brief was not updated for round 7 (note)

Carried, not repaired. The lead's dispatch stood in for the brief: it named
the narrow delta (the repair commit over the round-6 reviewed commit) and the
round number. The brief's heading ("round 6, narrow delta") and its recording
section's round-6 raw name are stale. They are left as they are because the
brief is one of the files the recorder freezes, and an edit here would put
text into the frozen set that no round read. The recorder takes the round
number as an argument to `--freeze`, so the stale name does not affect
recording.

### 2 — Q4's default overstates which READMEs are mapped (note)

Carried, not repaired. The packet's Q4 default (packet, question 4) says "a
README under the docs or doc folder or directly under the licenses folder".
Read it as the reviewer's correction: a README ending .md, .rst or .txt under
the docs or doc folder, or ending .md or .txt directly under the licenses
folder. The error overstates, so it fails closed, and the generated lists,
which the semantic delta names as the only statement of what is sendable, are
correct. A later version of the package should take the corrected wording.

### 3 — "confirmed" in the review-state statement (note)

Resolved by the review-state replacement described above. Round 6's verdict
was REVISE; no round before round 7 confirmed these bytes.

### 4 — "ending .md or .txt" omits "longer than it" (note)

No repair needed. The policy bytes require a name longer than the suffix, so
licenses/.md and licenses/.txt are withheld. The prose is not a contradiction.

### 5 — `--freeze` hashes the packet as it stands at the freeze commit (note)

Disclosed. The freeze commit is the commit that retains this raw. In it, the
only change to the packet is the dated review-state statement, which names
this raw and its verdict and says that no review read it. The act's subject is
the manifest row, and the builder checks the generated block, so what is
signed is unchanged.
