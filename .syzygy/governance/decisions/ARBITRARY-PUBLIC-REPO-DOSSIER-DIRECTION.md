# Owner direction — Polaris dossiers for any public repository

Date: 2026-10-07

Owner: Tzeusy

Decision ID: `ARBITRARY-PUBLIC-REPO-DOSSIER-2026-10-07`

This is a plain owner direction. It binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing. It grants no read, egress,
write or execution, and it adopts no specification: it directs that a
candidate specification be drafted, which binds nothing until the owner
signs it off (VIS-4).

## The owner's words

On 2026-10-07, in the Claude Code CLI, the lead explained that each new
repository today needs its own consent act, statement, code change and
review. The owner answered as plain text (relayed by the lead):

> "Hmm this doesn't fit my vision necessarily; I want to apply this even to
> repositories that I don't own, part of the point is an expedited learning
> curve for any arbitrary git repository. Assume we can easily fork and
> maintain our own fork locally, but may not necessarily have 'authoritative
> knowledge' on the motivations behind the creation of the repository"

The lead then proposed three directions: a standing public-repository
admission, a rule-based governed-tree check, and motivations reconstructed
as Inferred. The lead asked "Want me to start it?" The owner answered:

> "Yes please."

## The direction

1. **Draft a candidate specification change** so that a Polaris dossier can
   be produced for any public Git repository the operator clones or forks
   locally, whoever owns it, without a per-repository code change or review
   round.
2. **Motivations may be reconstructed.** Where the maintainers have not
   written down why the project exists or what it trades off, the dossier
   may reconstruct it from the code and its history. Every such
   reconstruction is labelled Inferred and is never presented as the
   authors' stated intent.
3. **The candidate is drafted under bead `syzygy-mzge`** (PR #400). Every
   act it needs, including any reading or amendment of the per-repository
   consent clauses it identifies, waits for the owner's own sign-off.

## What this direction does not do

It performs no act. It does not admit any repository, does not amend
doctrine, a contract or a specification, and does not reverse ruling 10b of
`REDIS-LOCAL-AGENT-SITTING-DIRECTION.md`.
