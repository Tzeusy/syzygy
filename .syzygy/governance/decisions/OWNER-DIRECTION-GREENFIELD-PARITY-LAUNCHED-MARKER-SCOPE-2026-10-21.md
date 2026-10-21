# Owner direction — scope of the launched-marker approval

Date: 2026-10-21

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-GREENFIELD-PARITY-LAUNCHED-MARKER-SCOPE-2026-10-21`

This is a plain owner direction in the sense of `PROCESS-GLOSSARY.md`. It
narrows one row of `OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`
and edits nothing in that record.
- It binds no artifact digest.
- It adds no row to `ACCEPTANCE-ACT-RECORD.md`.
- It registers nothing in `scripts/check_governance.py`.
- It signs nothing, adopts nothing and edits no signed byte.

## Why it was asked

The GP-Q0 Part 3 row of the answers record reads: "`isLaunchedRun` is read
fail-closed, at both `allow-execution` and brief issuance". The next sentence
reads: "Any change not listed here to what a gate accepts or refuses stops and
returns to the owner."

The round-1 review of bead `syzygy-bpyt.8.8`
(`docs/reviews/R-GP-IMPL-LAUNCHED-MARKER-1-RAW.md`, finding F2) found that the
same reader feeds three more gates the row does not name:
- `launch-form`;
- the inventory of-record counter;
- the review of-record counter.

By the record's own rule, that question returned to the owner.

## How the answers were given

[Observed: the owner's selections in a Claude Code session on 2026-10-21 at
11:32:21 UTC, made with the session's question tool. The session is not in this
repository.] The same answers are recorded as a comment on bead
`syzygy-bpyt.8.8`. Each question and each selection below is quoted exactly as
it was presented.

### Question 1

"Bead 8.8 (the launched-run marker): you approved reading `isLaunchedRun`
fail-closed "at both allow-execution and brief issuance". The review found that
the same reader also feeds three other gates: `launch-form` and the two counters
that decide which inventory and review sessions count as of record. The approval
assumed `allow-execution` was the only caller, which was wrong. With the
fail-closed reader, a marker that is present but can't be read as Syzygy's
(corrupt, wrong format, a link, a FIFO) means a terminal or bang launch form is
refused at `launch-form`, and no session counts at those two counters. Every
change refuses more, and nothing that was permitted before stays permitted.
Should the approval cover every reader of the marker?"

Selected: **"Cover every reader (Recommended)"**.

**Effect.** The GP-Q0 Part 3 approval of reading the launched-run marker
fail-closed covers every reader of that marker:
- `allow-execution`;
- brief issuance;
- `launch-form`;
- the inventory and review of-record counters.

[Inferred, from the round-2 review: `docs/reviews/R-GP-IMPL-LAUNCHED-MARKER-2-RAW.md`,
section 6, item 2.] Three gates read the marker only through those counters, so
they inherit the counters' refusals:
- the fidelity packet build;
- render;
- the supervisor's poll.

The question put every change as one that refuses more, so this record reads the
approval as covering only such changes. A change at any of these gates that would
permit something the base refused is not covered. Neither is a change at a gate
that does not read the marker. Either one returns to the owner.

### Question 2

"Same bead, separate point (review note N1): the library function
`allowExecution` has no marker check of its own; only the CLI wrapper refuses a
launched run. Today the brief-issuance check already stops a stray choice from
ever permitting execution, so the exposure is a stray record, not a permission.
Moving the check into the library would add a `disclosures` field to the CLI's
refusal JSON, which is an output change. What should happen to it?"

Selected: **"File a follow-up bead (Recommended)"**.

**Effect.**
- The library-level check is bead `syzygy-bpyt.8.11`.
- Its change to the CLI's refusal JSON is not approved by this direction. It
  returns to the owner before that bead merges.

## What this does not do

- It signs, adopts or accepts nothing (VIS-4).
- It amends no doctrine, contract, policy or specification, and edits no
  digest-bound file.
- It does not switch on the execution-permitting arm.
- It lifts no standing prohibition in `AGENTS.md`.

## Withdrawal

A later direction may narrow or withdraw this one; withdrawal defeats grant.
Withdrawal reaches only beads not yet merged.
