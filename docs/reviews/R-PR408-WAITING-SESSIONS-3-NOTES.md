# PR 408 waiting sessions, version 1.2 — round-3 review notes

> **Sibling notes record.** This file dispositions the five notes of the
> third fresh-context review of PR #408, which carries version 1.2 of the
> `polaris-dossier-local-agent-mode` amendment. Under the owner's notes-only
> rule (`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
> §1), a round with no revise-level finding clears the exact bytes it read,
> and its notes go in a sibling record, never into the reviewed bytes. So
> this file edits nothing in the package or the code the review read. It
> signs nothing off: only the owner's own selection does that (VIS-4). The
> sign-off is version-tagged and binds no act digest, so nothing here is
> registered in `check_governance.py`.

Reviewed record: docs/reviews/R-PR408-WAITING-SESSIONS-3-RAW.md

## What was confirmed

- **Subject:** PR #408 at
  `a3cdb3e644258561e1630eae0436905819e0ddb8`: the candidate package
  `.syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode-v1-2/`,
  the wait-mode code in `packages/polaris-dossier/` and the recording
  tooling.
- **Reviewed spec:** the change's `specs/polaris-generation/spec.md` with
  `proposed/spec.md.patch` applied to the installed v1.1 bytes, sha256
  `d6bce6b3aca13098f8d7ca28cee6aed5475e7522b2305958580eb17c4ffc3ea2`,
  which the reviewer re-derived by script (the raw's section B, item 1).
- **Verdict:** `CONFIRM WITH EXCEPTIONS`, on line 2 of the raw named on the
  `Reviewed record:` line above, with five findings, each tagged `(note)`.
  Rounds 1 and 2 returned `REVISE`; their raws are retained beside this
  file and their repairs are on the same branch.

## The notes and what happens to each

None changes what version 1.2 requires. Each is carried here, not repaired
in the reviewed bytes. Two follow-up beads are **to be filed** by the lead:
one for the code and printed-text follow-ups (notes 1, 2, 3 and 5), and one
to evaluate the settings-layer flags (note 4). This record files neither.

### 1 — The link checks are check-then-use

The sessions root and the session directory are checked, then resolved
again or written through by path. A writer racing in the state root between
the two could still redirect a write. Deferred to the first bead (to be
filed): resolve once and write only through the resolved, checked path, or
at least name the race in the code comment. The window is a few synchronous
calls wide, and the writer is the party the F1 threat already names
[Inferred: the raw did not reproduce it].

### 2 — The gate accepts a forged record with a forged two-line raw

`appliedSubjectHolds` reads only the raw's `Manifest SHA-256`, not its
`Verdict:`, its `Reviewed commit:` or the package key that the recorder's
`parse_head` and `review_binds` require. Deferred to the first bead (to be
filed): mirror the recorder's head predicate in the gate. The residual is
the one `RECORDS_WITHIN_REACH` already discloses: anything that can write
Syzygy's checkout can forge a record.

### 3 — A recorded sign-off over a drifted spec is refused as unsigned

When the record exists but the installed spec no longer hashes to the
reviewed digest, every wait-mode step says the owner has not signed off.
Failing closed is right; only the stated reason is wrong in that state.
Deferred to the first bead (to be filed): tell "no record" apart from "a
record whose applied subject no longer matches" in the refusal.

### 4 — The settings-layer residual reads as unclosable

`claude --help` (2.1.295) lists `--setting-sources` and `--restricted`, and
either might drop the user, project and local allow rules that the
disclosure names as the residual. The owner was told this limit stands and
that a flag which might lift it would be evaluated as a follow-up (the
sign-off question, residual (1)). Deferred to the second bead (to be
filed): evaluate `--setting-sources` and `--restricted --tools …` in a
session, including what else they drop (the operator's model or
authentication settings), then print one or reword the owner packet's
"cannot switch it off" to "does not switch it off", with the reason.

### 5 — The Codex note states unconditionally that a session asks first

The printed Codex note says a waiting Codex session asks before each call;
an operator's `~/.codex/config.toml` may set an approval policy of `never`.
The owner was told this limit (the sign-off question, residual (3)).
Deferred to the first bead (to be filed): say in the printed note that it
depends on the operator's Codex configuration, as the Claude Code
disclosure does for its settings layers.
