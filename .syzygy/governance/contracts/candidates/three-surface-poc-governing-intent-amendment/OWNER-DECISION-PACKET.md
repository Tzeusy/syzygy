# Owner decision packet — which work comes from which intent (P-100)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts three questions to the owner; only the owner's
> answer binds anything (VIS-4).

**Status:** drafted 2026-10-03 for bead `syzygy-u05.10` under the overnight
direction of the same date. The review round's verdict and how each finding
was handled are in `ROUND-1-DISPOSITIONS.md` beside this file, which also
says whether this version is ready to offer.

## The problem in one paragraph

Trajectory shows Butlers' work items, about eight thousand of them, but none
says which piece of intent it serves. Without that link, a change to intent
cannot be followed to the work it should affect. The vision pursuit of
2026-09-22 (move N10) proposed reading three more text fields from the Butlers
work database (`external_ref`, `description` and `design`) and pulling intent
identifiers out of them. That would mean Syzygy reading a new kind of Butlers
content, so it needs you.

## What the contracts already say

These are facts from the accepted contracts, quoted so you can check them.

- **The work database is not where intent lives.** RFC4-15 says the work
  database's authority is "work lifecycle state, after materialization only
  (SDR-7) — never intent, never observed behavior, never why the work
  exists".
- **Two of the three fields are outside the read contract.** RFC4-15's list
  of what may be read names `external_ref` but not `description` or `design`.
  Reading those two would need a contract amendment as well as your consent.
- **Syzygy's own record is where the link belongs.** RFC4-17 says that when
  Syzygy creates a work item it also writes the intent reference into that
  item as a copy, and that Syzygy's own creation record "stays
  authoritative". Syzygy has created one work item in Butlers so far. Its
  stored record does not yet keep the intent reference, although the request
  it was made from carries one. [Observed in the POC code.]
- **Work with no traceable intent is shown, counted and never green.**
  RFC8-23 calls this state "Unknown-provenance". RFC8-22 forbids guessing the
  link "by similarity, interpolation, or inference".

**What Syzygy reads today.** For each Butlers work item it reads nine
fields: its identifier, title, state, type, priority and three timestamps,
plus the database version. When Syzygy itself creates a work item, it later
finds that item again by looking for the `external_ref` value it wrote. That
search returns only the item's identifier; it brings no other item's
`external_ref` into Syzygy. [Observed in the POC code.]

**What is not known.** Whether any Butlers work item holds an intent
reference in `external_ref` or any other unread field is **[Unknown]**.

## What is already drafted, and what it does not do

The delta in this directory (`SEMANTIC-DELTA.md`, patches under `proposed/`)
adds one requirement, POC-REQ-014, to the Three-Surface POC specification:

- Every work item shows its intent link as **Unknown**, with the reason "the
  input that would say was not captured".
- Trajectory counts these items ("N of N"), marks each one, says that an item
  is resolved by supplying its intent, and lets you filter to them.
- Nothing is ever guessed from a title.

It reads **no new field**, and it does not yet allow a link to be shown at
all. Showing real links needs one more amendment, whichever way you answer
Question 1. The point of this one is that the board tells the truth now.

## Question 1 — where should a work item's intent link come from?

| Option | What it means | What it needs before anything is built |
|---|---|---|
| **Syzygy's own records only** (drafter's recommendation) | Syzygy reads no new Butlers field. It keeps the intent reference in its own record whenever it creates a work item, and shows the link from there. Butlers' existing items stay Unknown until someone supplies their intent through Syzygy. | A specification amendment adding the link and naming Syzygy's record as its source, your sign-off of it, and an implementation authorization. No consent or secret-policy act. |
| **Also read `external_ref`** | Syzygy reads one more Butlers field, which RFC4-15 already allows. It treats the value as an identifier only, never as intent, and shows a link only when the value matches a record Syzygy itself made. | Three owner acts first, because this is a new kind of Butlers content (PWB-REQ-005): you extend your consent to this field, the secret-scanning rules are extended to cover it, and the list of what Syzygy may read from Butlers (the registry entry) gains it. Then everything in the row above. |
| **Also read `external_ref`, `description` and `design`** | Syzygy reads free text written by people and agents in Butlers, and pulls intent identifiers out of it by a strict grammar. | Everything in the row above, plus a contract amendment to RFC 0004, because RFC4-15 says this database is "never intent". The text may hold secrets, so the secret-scanning rules must handle it before any read. |

**Why the drafter recommends Syzygy's own records only.** It is the only
option that agrees with the contracts as written, and it needs no new Butlers
content. It shows the one link Syzygy can actually vouch for: the one it wrote
itself. The cost is plain: Butlers' existing backlog will show Unknown intent
for the foreseeable future. That is the honest answer, not a failure.
[Inferred]

**If unanswered,** nothing new is read and every item stays Unknown.

## Question 2 — sign the drafted requirement, POC-REQ-014?

| Option | Meaning |
|---|---|
| **Sign v1.0** (once the review clears) | The patches are applied at sign-off, and the POC specification gains POC-REQ-014. Building it still needs its own authorization. |
| Decline | Trajectory stays as it is, with no intent field and no count. |
| Revise | Name what to change; a new version gets a new review round. |

**How you would sign.** On 2026-10-02 you agreed a short way to sign some
specification changes: you pick a version number from a list, and nothing
else is needed. That agreement (called "Scope A") named the PWB specification
changes, the Butlers read list and the contract changes queued behind them. It
did not name changes to the Three-Surface POC specification, which this is.
P-84 asks the same question for the other pending POC change.

| Option | Meaning |
|---|---|
| **Use the same short way for this change** (recommended, the same answer as P-84) | You sign by picking a version. |
| The longer way | A small script is written for this one change, and you type a fixed sentence that includes a long checksum identifying the exact text you approve. |

**Order against P-84.** Both changes edit the same four POC files at
neighbouring lines. Whichever you sign second is redone on top of the first
before it is applied. Neither changes the other's requirements.

## Question 3 — the deferred part

The pursuit move also asked for a "source-to-claims" index: given one intent
source, list every claim that rests on it, so a change to that source shows
everything it touches. That belongs to the PWB specification and the shared
model, where only one change runs at a time. It is **deferred**, not drafted.
It takes its turn in that one-at-a-time slot, and then needs its own PWB
change and sign-off.

| Option | Meaning |
|---|---|
| **Keep it deferred** (recommended) | It is drafted as a PWB change when its turn comes. |
| Drop it | The move closes without the index. You lose the ability to see, from one intent source, which claims a change to it would affect. |

## Related, filed separately

Syzygy already reads each work item's title, which is free text, and no
declared secret-scanning rule covers that field. That gap is filed for you as
`syzygy-jytt` and is not decided here.
