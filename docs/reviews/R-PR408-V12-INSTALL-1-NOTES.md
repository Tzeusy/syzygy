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

- **Subject:** the four commits from `a3cdb3e6` to
  `e9ab09f8f405e201e54fdd2305b07527abc3e9d7` on PR #408: the round-3 and
  round-4 raws, the notes record, the v1.2 recording and install, and the
  authority-sweep test change.
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

### 4 — The notes record's "to be filed" is not digest-bound

[Observed] The review read `R-PR408-WAITING-SESSIONS-4-NOTES.md` as it
stood at `e9ab09f8`, saying the two follow-up beads were "to be filed".
Commit `5a2b2f6b` (merged as `068d5f1f`) then rewrote those words in place
to cite `syzygy-syoj` and `syzygy-zzt5`, at the lead's direction and
before this review's suggestion to add a dated line instead was known. The
record is not digest-bound: the sign-off record names it by path only, and
the recorder checks only that it names the reviewed raw and carries the
same finding numbers, which still holds. Nor did the rewrite move the tag:
`polaris-dossier-local-agent-mode-v1.2` sits on the recording commit
`77fc9f6e`, whose notes record still carries the original "to be filed"
text this review confirmed. The current bytes differ from the reviewed ones
only in naming the filed beads. They are not re-reviewed, and the record is
not edited further.

### 5 — The partition sentence carries the new count under the old date

Repaired in this change: the `docs/README.md` partition sentence is dated
2026-10-14, the date of the derivation that produced its count, which this
change re-derives with the two new files.
