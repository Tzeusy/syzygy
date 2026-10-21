# Launched-marker reader: round-2 review dispositions

[Observed] This record dispositions the notes of
`docs/reviews/R-GP-IMPL-LAUNCHED-MARKER-2-RAW.md`, the round-2 CC-REV-1 review
of `syzygy-bpyt.8.8`.

- Verdict: `CONFIRM WITH EXCEPTIONS` (line 2 of the raw).
- Reviewed commit: `cf3ba3fe` (line 3).
- Subject: `r2-review.diff` sha256
  `42f082bd2852be4e0ef0ba35e75cb44656621e885b0f635601afd182127dd9bd` (line 4),
  equal to `git diff fe20dd5f cf3ba3fefb3969e2293afb0038685b4cd41e6788`.

The raw says "No finding is blocking. Each of the following is a note."
(section 5). Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them and holds every correction the notes ask
for. It is an implementation record and binds nothing.

Revise-severity findings: 0

## R2-N1: the 4096-byte bound is checked at `fstat` but not enforced on the read

[Observed by the reviewer] A regular file that grows after `fstat` is read to
end-of-file. The reviewer saw a 4 GiB growth abort the process. That residual
reaches `allow-execution`, `launch-form`, both of-record counters and arm-on
brief issuance, though no reader is worse than at base.

The type documentation at `packages/polaris-dossier/src/launched.ts:30-32`
says a "file larger than any marker" is `unreadable`. That is true only for a
file that is already that large when it is opened.

**Disposition:**
- Filed as `syzygy-bpyt.8.12` (P2): a bounded read through the descriptor,
  together with the reviewer's growth test.
- Recorded on `syzygy-bpyt.1.6` as a precondition of switching on the
  execution-permitting arm.

## R2-N2: the `any-file-type` survivor is not equivalent

**Correction.** `docs/evidence/launched-marker-fail-closed-mutants-2026-10-21-r2.json`,
key `equivalentSurvivors.any-file-type` (line 350), calls the mutant
"Equivalent at every fixture an unprivileged test can build". That is wrong.
- [Observed by the reviewer] With the mutant applied, a FIFO that holds the
  marker's bytes reads `launched`, and a `syzygy-launched` form counts.
- A test with that fixture kills the mutant: `Tests  1 failed | 230 passed (231)`.
- The `!stat.isFile()` predicate at `launched.ts:52` is therefore load-bearing.
  No test kills its removal yet.
- The same record's other survivor, `inventory-brief-marker-not-read`, is truly
  equivalent (raw, section 4, N4).

**Disposition:** the killing fixture and a successor mutants record belong to
`syzygy-bpyt.8.12`. Neither round-2 record is edited.

## R2-N3: the owner's widening of the approval was recorded only in a bead comment

**Disposition:** recorded as the plain owner direction
`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-LAUNCHED-MARKER-SCOPE-2026-10-21.md`.
- It quotes both questions and both selections as presented, with the session
  timestamp 2026-10-21 11:32:21 UTC.
- It is indexed in `decisions/README.md`.
- It edits nothing in `OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`.

## R2-N4: nothing at the brief call sites holds "never opens the marker"

[Observed by the reviewer] The property holds at this head (raw, section 3,
item 10). No test would notice if a call site read the marker eagerly again.

**Correction.** The comment at `brief.test.ts:227` says the arm-off FIFO and
`/dev/zero` cases show "the arm-off brief never opens the marker". Those cases
prove less: issuing the brief does not hang, and the brief's bytes are the same.

**Disposition:** an open-counting test, or a corrected comment, belongs to
`syzygy-bpyt.8.12`.

## Round-1 notes still open

| Note | Status | Where it is carried |
|---|---|---|
| N2 (check-then-act at `allow-execution`) | Still a note. The arm-on brief check stays load-bearing. | The differential's `notCovered` list |
| N3 (trust on absence) | Open by design. | No action |
| N5 (`review.ts:664` wording untested) | Still a note. | `syzygy-bpyt.8.12` |
| N7 (the `isLaunchedRun` export removed) | Still a note: a private package, so not an endpoint removal. | No action |
| N8 (process items outside the subject) | Answered by the pull request text, this record and the cycle-report owner notice on `syzygy-bpyt.10`. | — |
| N9 (one altered-prose variant) | Still a note. The reader compares only `format`. | No action |

N1 (the library `allowExecution`) is `syzygy-bpyt.8.11`, at the owner's
direction.
