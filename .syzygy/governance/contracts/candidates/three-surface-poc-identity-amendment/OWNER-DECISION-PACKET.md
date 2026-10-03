# Owner decision packet — Three-Surface POC identity amendment

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts two questions to the owner; only the owner's
> answer binds anything (VIS-4).

**Status:** drafted 2026-10-03 under ruling P-75 (A). Each review round's
verdict and dispositions are recorded in the package's
`ROUND-<n>-DISPOSITIONS.md` records beside this file, and the latest one says
whether this version is ready to offer.

## What you would be signing

One amendment to the signed Three-Surface POC specification, the one P-75
ruled. Read `SEMANTIC-DELTA.md` for the full account. In short:

- **POC-REQ-054 (new).** Every subject has one identity, the same on Polaris,
  Trajectory, Orrery and the machine answer. Links between surfaces resolve by
  it. Where a surface shows one claim's desired, execution and observed states
  together (the "ribbon"), a slot nothing fills says Unknown with a reason and
  a route; it is never blank and never a score.
- **POC-REQ-055 (new).** Every relation kind the POC emits is either a name
  from RFC1-25's closed table, in the right direction, or carries a flag
  saying it is outside that table. Seven of today's eight are outside. The
  signed coverage row that mapped this to POC-REQ-052 stays as it is. Beside
  it, an added row and a disclosure say that the flag is the repair you
  ruled. Closure itself — no outside kind emitted at all — stays Unknown.
- **POC-REQ-060 (amended).** The one-encoding rule now names all three labels,
  Observed, Inferred and Unknown, and one record shape. Inferred is allowed
  only for an agent's assertion and never counts as Observed. Nothing
  produces one today.

**One departure from the design you adopted.** The M9 design said
POC-REQ-054 "Declares the canonical join key". This package does not: it
requires one identity per subject but leaves the identity's *form* to the
implementation slice.

- **Why.** The design's proposed key, `repository:<repo>@<rev>:<path>#<objectId>`,
  contains a file path. RFC6-1 bars a file path from being a selection
  identity, so writing that key into the signed text would put the
  specification against a contract clause. [Inferred]
- **The consequence if you sign.** Slice 6b picks the form under POC-REQ-054
  with no further act from you.
- **If you would rather settle the form in the specification,** answer
  "Revise" below and name it.

**What signing does not do.** It starts no implementation. M9 slices 4–8
become eligible to start under your ruling only after this sign-off.

## Question 1 — sign this version?

| Option | Meaning |
|---|---|
| **Sign v1.0** (recommended once the review clears) | The patches are applied in the sign-off change, and the specification reads 26 requirements. |
| Decline | The specification stays at 24 requirements, and M9 slices 4–8 stay blocked. |
| Revise | Name what to change; a new version gets a new review round. |

## Question 2 — by which route?

The 2026-10-02 versioned sign-off direction (Scope A) covers "the PWB
specification deltas, the observer registry entry and the contract
successors queued behind them". A Three-Surface POC specification amendment
is not in that list.

| Option | Meaning |
|---|---|
| **Extend Scope A to this package** (recommended) | You sign by selecting a version in a structured question. No phrase and no digest are needed. The sign-off change registers the package with `scripts/record_versioned_signoff.py`. This is the same kind of artifact as the PWB deltas, an implementation-phase specification amendment, and it carries the same review requirement. |
| Phrase and digest | A dedicated recorder is written, and you type a phrase naming the manifest digest, as for the 2026-09-29 readability successor act. |

**If unanswered,** nothing is signed and the package stays a candidate.
