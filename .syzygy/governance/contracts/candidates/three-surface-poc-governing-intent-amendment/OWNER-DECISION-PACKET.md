# Owner decision packet — which work comes from which intent (P-100)

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts three questions to the owner; only the owner's
> answer binds anything (VIS-4).

**Status:** drafted 2026-10-03 for bead `syzygy-u05.10` under the overnight
direction of the same date. The review round's verdict and its dispositions
are recorded in `ROUND-1-DISPOSITIONS.md` beside this file, which also says
whether this version is ready to offer.

## The problem in one paragraph

Trajectory shows Butlers' work items, about eight thousand of them, but none
says which piece of intent it serves. Without that link, a change to intent
cannot be followed to the work it should affect. The vision pursuit of
2026-09-22 (move N10) proposed reading three more text fields from the Butlers
work database (`external_ref`, `description` and `design`) and pulling intent
identifiers out of them. That is a new kind of Butlers content for Syzygy to
read, so it needs you.

## What the contracts already say

These are facts from the accepted contracts, quoted so you can check them.

- **The work database is not where intent lives.** RFC4-15 says the work
  database's authority is "work lifecycle state, after materialization only
  (SDR-7) — never intent, never observed behavior, never why the work
  exists".
- **Two of the three fields are outside the read contract.** RFC4-15's read
  list names `external_ref` but not `description` or `design`. Reading those
  two would need a contract amendment as well as your consent.
- **Syzygy's own record is where the link belongs.** RFC4-17 says that when
  Syzygy creates a work item it writes the intent reference into the work
  item as a copy, and that Syzygy's own creation record "stays
  authoritative". Syzygy has created one work item in Butlers so far. Its
  stored record does not yet keep the intent reference, although the request
  it was made from carries one. [Observed in the POC code.]
- **Work with no traceable intent is shown, counted and never green.**
  RFC8-23 calls this state "Unknown-provenance". RFC8-22 forbids guessing the
  link "by similarity, interpolation, or inference".

**What is not known.** Whether any Butlers work item holds an intent
reference in `external_ref` or any other unread field is **[Unknown]**.
Syzygy reads nine fields today, and those three are not among them.

## What is already drafted, and what it does not do

The delta in this directory (`SEMANTIC-DELTA.md`, patches under `proposed/`)
adds one requirement, POC-REQ-014, to the Three-Surface POC specification:

- Every work item shows its intent link, or **Unknown** with a reason.
- Trajectory counts the Unknown items, marks each one, and lets you filter
  to them.
- No link is ever guessed from a title or any other text.

It reads **no new field**. Until you answer Question 1, every item would show
Unknown, because nothing Syzygy may read carries the link. It is drafted so
that the board tells the truth now, whatever you decide below.

## Question 1 — should Syzygy read any more work-item fields?

| Option | What it means | What else it needs |
|---|---|---|
| **None** (drafter's recommendation) | Syzygy reads no new Butlers work field. The link comes only from Syzygy's own creation record, which a later change extends to keep the intent reference. Butlers' existing items stay Unknown until someone supplies their intent through Syzygy. | No consent or policy act. A separate implementation change to the creation record, under its own authorization. |
| **`external_ref` only** | Syzygy reads one more field, which RFC4-15 already allows. It reads the field as an identifier only, never as intent, and only links an item when the value matches a record Syzygy itself made. | Three owner acts (PWB-REQ-005): extending your consent to this field, extending the secret policy to cover it, and a registry entry. Then a specification amendment and an implementation authorization. |
| **`external_ref`, `description` and `design`** | Syzygy reads free text written by people and agents in Butlers, and pulls intent identifiers out of it by a strict grammar. | Everything in the row above, plus an RFC 0004 amendment, because RFC4-15 says this database is "never intent". The text may hold secrets, so the secret policy has to classify it before any read. |

**Why the drafter recommends None.** It is the only option that agrees with
the contracts as written. It needs no new Butlers content, and it makes the
one link Syzygy can actually vouch for, the one it wrote itself. The cost is
plain: Butlers' existing backlog will show Unknown intent for the foreseeable
future. That is the honest answer, not a failure. [Inferred]

**If unanswered,** nothing new is read and every item stays Unknown.

## Question 2 — sign the drafted requirement, POC-REQ-014?

| Option | Meaning |
|---|---|
| **Sign v1.0** (once the review clears) | The patches are applied at sign-off, and the POC specification gains POC-REQ-014. Implementation still needs its own authorization. |
| Decline | Trajectory stays as it is, with no intent field and no count. |
| Revise | Name what to change; a new version gets a new review round. |

**By which route.** The 2026-10-02 versioned sign-off direction (Scope A)
covers "the PWB specification deltas, the observer registry entry and the
contract successors queued behind them". A Three-Surface POC amendment is not
in that list; P-84 asks the same question for the identity amendment.

| Option | Meaning |
|---|---|
| **Extend Scope A to this package** (recommended, the same answer as P-84) | You sign by choosing a version. No phrase or digest is needed. |
| Phrase and digest | A recorder is written, and you type a phrase naming the manifest digest. |

**Order against P-84.** Both packages change the same four POC files at
neighbouring lines. Whichever you sign second is regenerated on top of the
first before it is applied. Neither changes the other's requirements.

## Question 3 — the deferred part

The pursuit move also asked for a "source-to-claims" index, so a change to one
intent source shows every claim that rests on it (`claimsBySourceAnchor`).
That belongs to the PWB specification and the shared model, where one change
runs at a time. It is **deferred**, not drafted. It takes its turn in that
one-at-a-time slot, and then needs its own PWB delta and sign-off.

| Option | Meaning |
|---|---|
| **Keep it deferred** (recommended) | It is drafted as a PWB delta after the shared-model queue clears. |
| Drop it | The move is closed without the index. |

## Related, filed separately

Syzygy already reads each work item's title, which is free text, and no
declared secret policy covers that field. That gap is filed for you as
`syzygy-jytt` and is not decided here.
