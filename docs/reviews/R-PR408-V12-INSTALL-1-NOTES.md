# PR 408 v1.2 recording and install — review notes

> **Sibling notes record.** This file dispositions the five notes of the
> fresh-context review of the v1.2 recording and install on PR #408. Under
> the owner's notes-only rule
> (`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
> §1), a round with no revise-level finding clears the exact bytes it read,
> and its notes go in a sibling record, never into the reviewed bytes. It
> signs nothing off (VIS-4) and is registered nowhere in
> `check_governance.py`.

Reviewed record: docs/reviews/R-PR408-V12-INSTALL-1-RAW.md

## What was confirmed

- **Subject:** the five commits from `a3cdb3e6` to
  `5a2b2f6b3b00f42d480e475655d66398f933f87c` on PR #408, the head that
  merged as `068d5f1f`: the round-3 and round-4 raws, the notes record, the
  v1.2 recording and install, the authority-sweep test change, and
  `5a2b2f6b`'s citation of the filed beads. The raw was re-issued at
  `5a2b2f6b` after a first pass at `e9ab09f8`; criteria 1–5 rest on
  `e9ab09f8`, which `5a2b2f6b` does not change, and the Python battery was
  re-run at `5a2b2f6b` (the raw's criterion 6).
- **Verdict:** `CONFIRM WITH EXCEPTIONS`, on line 2 of the raw named above,
  with five findings, each tagged `(note)`. PR #408 merged at `068d5f1f`,
  and the tag `polaris-dossier-local-agent-mode-v1.2` sits on the rebased
  recording commit `77fc9f6e`.

## The notes and what happens to each

### 1 — The sign-off record binds a review that finished after the owner's selection

Repaired in this change, in an unbound carrier and never in the sign-off
record: the P-107 row of
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` gains a dated
note. It says the owner was offered round 3 and selected at
2026-10-14T03:32:23Z; that round 4 ran afterwards over the same bytes and
the same subject digest, because round 3's head carried no
`Manifest SHA-256:` line and so could not be bound; and that round 4 is
therefore the review of record.

### 2 — The declaration-line regex is loosened for every `Decision ID:` line

Not repaired here. The lead appends it to `syzygy-syoj`.

### 3 — The Claude Code skill states confinement and "walk away" without qualifiers

Not repaired here. The lead appends it to `syzygy-syoj`, beside round-4
finding 2, which is the same class.

### 4 — The edit at `5a2b2f6b` to the notes record is lawful, but rewrites in place

The review covers the edit: commit `5a2b2f6b` touched only `docs/README.md`
(the campaign row) and `docs/reviews/R-PR408-WAITING-SESSIONS-4-NOTES.md`,
replacing "to be filed" with `syzygy-syoj` and `syzygy-zzt5`, and the raw
finds no digest of that record bound anywhere and the recorder's `--check`
passing at that commit.

One fact the raw could not see: it says the tag would freeze the
`5a2b2f6b` bytes once created. [Observed] The tag
`polaris-dossier-local-agent-mode-v1.2` was created after the merge, on
`77fc9f6e`, the rebased recording commit, whose copy of the notes record
still carries the original "to be filed" text
(`git show 77fc9f6e:docs/reviews/R-PR408-WAITING-SESSIONS-4-NOTES.md`). The
tag therefore freezes the pre-rewrite text; `main` carries the rewrite.

The two remaining points are not repaired here. The record is not edited
again: a rewrite to restore the old text with a dated addition would be a
second in-place edit of the same file. The bead notes that call the record
bound and unedited, and `syzygy-syoj`'s stale path to the deleted round-3
notes file, are in the tracker, outside this change, and go to the lead.

### 5 — The partition sentence carries the new count under the old date

Repaired in this change: the `docs/README.md` partition sentence is dated
2026-10-14, the date of the derivation that produced its count, which this
change re-derives with the two new files.
