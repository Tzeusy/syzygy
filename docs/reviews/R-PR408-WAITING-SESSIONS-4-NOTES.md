# PR 408 waiting sessions, version 1.2 — review notes, rounds 3 and 4

> **Sibling notes record.** This file dispositions the notes of the third
> and fourth fresh-context reviews of PR #408, which carries version 1.2 of
> the `polaris-dossier-local-agent-mode` amendment. Under the owner's
> notes-only rule (`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
> §1), a round with no revise-level finding clears the exact bytes it read,
> and its notes go in a sibling record, never into the reviewed bytes. So
> this file edits nothing in the package or the code the reviews read. It
> signs nothing off: only the owner's own selection does that (VIS-4). The
> sign-off is version-tagged and binds no act digest, so nothing here is
> registered in `check_governance.py`.

Reviewed record: docs/reviews/R-PR408-WAITING-SESSIONS-4-RAW.md

## What was confirmed

- **Subject:** PR #408 at
  `a3cdb3e644258561e1630eae0436905819e0ddb8`: the candidate package
  `.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode-v1-2/`,
  the wait-mode code in `packages/polaris-dossier/` and the recording
  tooling.
- **Reviewed spec:** the change's `specs/polaris-generation/spec.md` with
  `proposed/spec.md.patch` applied to the installed v1.1 bytes, sha256
  `d6bce6b3aca13098f8d7ca28cee6aed5475e7522b2305958580eb17c4ffc3ea2`.
  Both reviewers re-derived it by script; round 4 carries it on its
  `Manifest SHA-256:` head line.
- **Round 4** (the raw named on the `Reviewed record:` line above):
  `CONFIRM WITH EXCEPTIONS`, four findings, each tagged `(note)`. It is the
  record of this sign-off, because its head carries the digest line the
  recorder binds.
- **Round 3** (`docs/reviews/R-PR408-WAITING-SESSIONS-3-RAW.md`):
  `CONFIRM WITH EXCEPTIONS` over the same bytes, five notes. Its head
  carries no `Manifest SHA-256:` line, which the review brief required, so
  the recorder cannot bind it; it is retained verbatim and its notes are
  carried below. Rounds 1 and 2 returned `REVISE`; their raws are retained
  beside this file and their repairs are on the same branch.

## Where the notes go

None changes what version 1.2 requires. Each is carried here, not repaired
in the reviewed bytes. Two follow-up beads are **to be filed** by the lead;
this record files neither.

- **First bead (to be filed):** code and printed-text follow-ups: round-4
  findings 1, 2 and 4, and round-3 notes 1, 2, 3 and 5.
- **Second bead (to be filed):** settings layers and the heredoc hand-over:
  round-3 note 4 and round-4 finding 3.

## Round 4 findings

### 1 — The Codex note and the owner packet say a waiting Codex session asks before each call

Under an approval policy of `on-request`, Codex leaves the decision to ask
to the model, so the printed sentence can be false for a call made while
nobody is present [Inferred: from `codex --help`, not observed in a
session]. The spec's residual list names settings layers, not the agent
tool's own approval behaviour. Deferred to the first bead (to be filed):
say in the printed note and the packet that what a waiting Codex session
runs without asking depends on Codex's approval policy, and in a later
version add that dependence to the requirement's Inferred list. Same root
as round-3 note 5.

### 2 — The owner packet's cost paragraph says a waiting session "cannot" write a file or run the project

An allow rule in the operator's own settings can still run unattended,
which the packet itself says earlier. Deferred to the first bead (to be
filed): qualify the "cannot" as "cannot, through anything the printed
command pre-approves" wherever that sentence is printed or carried forward.
The packet's own bytes are reviewed and stay as they are.

### 3 — Whether Claude Code's prefix rule admits the multi-line heredoc hand-over without asking is Unknown

If the matcher asks, the failure is safe, but the submission stalls
unattended, which is what option B removes. Deferred to the second bead
(to be filed): record one attended observation of a real waiting session's
submission before relying on unattended runs.

### 4 — The continuity item renders whatever the sign-off state

`continuationOf` renders a review-page item for every counted verdict
without consulting `waitModeSignedIn`, so "v1.1 behaviour is unchanged
while this package is unsigned" overstates for the rendering. It adds a
disclosure, never a permission, and the merge order (code merges only
after the v1.2 sign-off) makes it moot. Deferred to the first bead (to be
filed): scope the sentence to every wait-mode step, or gate the render
item.

## Round 3 notes

### Round-3 note 1 — The link checks are check-then-use

The sessions root and the session directory are checked, then resolved
again or written through by path. A writer racing in the state root between
the two could still redirect a write. Deferred to the first bead (to be
filed): resolve once and write only through the resolved, checked path, or
at least name the race in the code comment. The window is a few synchronous
calls wide, and the writer is the party the F1 threat already names
[Inferred: the raw did not reproduce it].

### Round-3 note 2 — The gate accepts a forged record with a forged two-line raw

`appliedSubjectHolds` reads only the raw's `Manifest SHA-256`, not its
`Verdict:`, its `Reviewed commit:` or the package key that the recorder's
`parse_head` and `review_binds` require. Deferred to the first bead (to be
filed): mirror the recorder's head predicate in the gate. The residual is
the one `RECORDS_WITHIN_REACH` already discloses: anything that can write
Syzygy's checkout can forge a record.

### Round-3 note 3 — A recorded sign-off over a drifted spec is refused as unsigned

When the record exists but the installed spec no longer hashes to the
reviewed digest, every wait-mode step says the owner has not signed off.
Failing closed is right; only the stated reason is wrong in that state.
Deferred to the first bead (to be filed): tell "no record" apart from "a
record whose applied subject no longer matches" in the refusal.

### Round-3 note 4 — The settings-layer residual reads as unclosable

`claude --help` (2.1.295) lists `--setting-sources` and `--restricted`, and
either might drop the user, project and local allow rules that the
disclosure names as the residual. The owner was told this limit stands and
that a flag which might lift it would be evaluated as a follow-up (the
sign-off question, residual (1)). Deferred to the second bead (to be
filed): evaluate `--setting-sources` and `--restricted --tools …` in a
session, including what else they drop (the operator's model or
authentication settings), then print one or reword the owner packet's
"cannot switch it off" to "does not switch it off", with the reason.

### Round-3 note 5 — The Codex note states unconditionally that a session asks first

The printed Codex note says a waiting Codex session asks before each call;
an operator's `~/.codex/config.toml` may set an approval policy of `never`.
The owner was told this limit (the sign-off question, residual (3)).
Deferred to the first bead (to be filed): say in the printed note that it
depends on the operator's Codex configuration, as the Claude Code
disclosure does for its settings layers.
