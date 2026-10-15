> # Record beside the package — not authority, binds nothing
>
> Dispositions of the fifth fresh-context review of the PWB opening-index
> amendment package (PWB-REQ-010, P-98, slice A), a regeneration
> confirmation over the P-99 sign-off. This record is not a package
> artifact: the manifest does not hash it and no builder reads it. It is the
> sibling record the owner's 2026-09-26 ruling provides for a notes-only
> round (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
> §1), named by the brief (`REVIEW-BRIEF.md` §"Round 5"). It offers nothing
> and performs no act (VIS-4).

# Round 5 dispositions — PWB opening-index amendment

Reviewed record: docs/reviews/R-PWB-OPENING-INDEX-AMENDMENT-5-RAW.md

Manifest SHA-256: 1afaa59d9e127c575c00770f8c6b2dffcaf099300dac23ec4c5e202b893178de

Revise-severity findings: 0

- **Reviewed commit (raw line 2):**
  `eda0e345b032ef279d0db231a983f1d963fe9c8f`, the merge of the
  regeneration (PR #448).
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`. Four findings, every
  one a note; no revise and no blocking finding (raw line 168: "Count: 4
  findings — 0 blocking, 0 revise, 4 note.").
- **Head digest.** [Observed 2026-10-15] `git show eda0e345:<manifest> |
  sha256sum` re-derives the digest above, which is the raw's line 3.
- **What clears.** Under the 2026-09-26 ruling, a round with no
  revise-severity finding clears the exact bytes it read: the manifest whose
  file digest stands above, at the reviewed commit, the proposed bytes it
  hashes, and the package prose beside it.
- **The carry-over conditions.** The owner's "Carry if review clears"
  (`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-3-2026-10-14.md`)
  carries Q1 "Sign v1.0" to this version on two conditions. [Observed
  2026-10-15] Both hold: this round is notes-only, and
  `proposed/spec.md.patch` is blob `9e9d9efbc831c739d559962f85c7c2ed3995dba9`
  at round 4's reviewed commit `83b29c96` and at `eda0e345` (`git
  rev-parse` of both). The sign-off is recorded in
  `../../../decisions/PWB-OPENING-INDEX-AMENDMENT-SIGNOFF-v1.0.md`.
- **Nothing in the package is edited.** Every note below is dispositioned
  here, not in the reviewed bytes.

## Dispositions

### 1 — `ROUND-4-DISPOSITIONS.md` is wholly new since round 4, not only its dated section (note)

**Dispositioned.** Raw line 121. The file was created after round 4 as
that round's sibling record (`e5cf8124`), and the regeneration added its
dated section. Neither is package bytes. Nothing to repair; a later brief
names both commits.

### 2 — Package prose still calls P-99 pending (note)

**Open, carried here.** Raw line 131. These sentences in the cleared bytes
are no longer true as of 2026-10-15, and this record carries the
correction instead of an edit: `IMPACT-LEDGER.md` lines 86 and 92,
`SEMANTIC-DELTA.md` line 311 and `OWNER-DECISION-PACKET.md` line 282 call
P-99 pending, and P-99 is signed v1.0
(`../../../decisions/PWB-ACCESSIBLE-NAME-AMENDMENT-SIGNOFF-v1.0.md`). Their
"regenerated … in the cycle-3 repair" is no longer the latest
regeneration: this package was last regenerated over the P-99 sign-off
(`ROUND-4-DISPOSITIONS.md` §"Regenerated over the P-99 sign-off,
2026-10-15"). `SEMANTIC-DELTA.md` line 255 and the packet row at line 203
are conditioned on P-99 being signed, which it now is.

### 3 — "Its distinct-name rule covers them" is true of accessible names, not of visible text (note)

**Open.** Raw line 145. Signed PWB-REQ-016 makes differently targeted
links' accessible names differ. It does not stop another link from showing
a row's visible words. Add that clause when the packet or its
implementation notes are next revised. The reviewer found no contradiction
between the two requirements (raw criterion 6).

### 4 — P-85 and the P-95 pins remain stale over the signed tree (note)

**Open, outside this package.** Raw line 158. Signing this version moves
PWB `spec.md` again. The release-label package (P-85) is regenerated over
it before its round 6, and the P-95 re-pin stays stale (`syzygy-fxro`,
`syzygy-2g0d`), as the sign-off record says.
