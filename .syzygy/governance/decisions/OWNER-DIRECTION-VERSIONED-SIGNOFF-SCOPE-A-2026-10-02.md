# Owner direction — version-tagged sign-off for implementation-phase artifacts (Scope A)

Date: 2026-10-02

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02`

This is a plain owner direction in the shape of
`POLARIS-RESPONSE-CEILING-READING-DIRECTION.md`. It binds no artifact digest,
adds no row to `ACCEPTANCE-ACT-RECORD.md` and registers nothing. It records a
direction; it does not itself change a check or a recorder.

## The owner's words

On 2026-10-02, in the Claude Code CLI, the owner wrote: "Why is this project
so fixated on contract phrases? Can we do away with that and exact-checksum
signoffs? In this phase of development (greenfield, rapid improvement cycles)
this impedes development velocity; in a future iteration we can implement
this, on a sign-off-major-minor-version mechanism."

The assistant answered that the phrase-and-digest form exists for VIS-4 and
rule 10, named the cost, and asked which scope. The owner selected
"Scope A (Recommended)" with its description as shown: "I record this as a
plain owner direction, then remove the digest and phrase machinery for those
artifacts in one governed PR. Already-performed acts stay as they are."

## The direction

1. **Scope A.** For implementation-phase governed artifacts, namely the PWB
   specification deltas, the observer registry entry and the contract
   successors queued behind them, an owner sign-off is the owner's selection
   of an option in a structured question that names the package and the
   version being signed. No typed phrase and no digest argument is required.
2. **Binding.** A sign-off binds a git tag naming a `major.minor` sign-off
   version of the package (`<package>-v<major>.<minor>`), applied to the commit
   that carries the package bytes the owner was shown. A later edit is a new
   version; it does not retire the earlier sign-off, and the owner signs the
   new version when they choose.
3. **Review.** Fresh-context review is unchanged in kind: a package is offered
   only after a round that returns CONFIRM, or CONFIRM WITH EXCEPTIONS with
   notes only. The review binds the commit it read; a later edit needs a new
   round before the next version is offered.
4. **Mechanical checks stay.** Patches apply, manifests and derived bytes
   regenerate exactly, and the battery stays green. What goes is the
   digest-argument ceremony: exact-phrase validation, manifest-digest copies
   in packets, and the cascade that re-pinned every sibling after each act.
5. **Unchanged.** VIS-4 (only the owner adopts), the review requirement,
   epistemic labels and honest Unknown. Doctrine, accepted contracts and every
   act already performed keep their digests and their records; nothing here
   edits an act-bound byte. Scope B (all artifacts) is not issued.
6. **Withdrawal.** A later direction may narrow or withdraw this one;
   withdrawal defeats grant.

## What this does not do

It changes no check, recorder or packet. The replacement mechanism and the
removal of the digest machinery for the covered artifacts travel as one
governed change after this record. Until that change lands, the existing
phrase-and-digest acts remain the only way to perform the queued packages.
