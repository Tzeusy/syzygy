# Owner decision packet — Three-Surface POC identity amendment

> **Candidate — binds nothing.** Nothing here is signed, adopted or labelled
> accepted. This packet puts two questions to the owner; only the owner's
> answer binds anything (VIS-4).

**Status:** drafted 2026-10-03 under ruling P-75 (A). Each review round's
verdict and dispositions are recorded in the package's
`ROUND-<n>-DISPOSITIONS.md` records beside this file, and the latest one says
whether this version is ready to offer.

**State on 2026-10-14:** four fresh-context rounds were each `REVISE`. On
your direction of 2026-10-14, round 4's findings 26–32 were **repaired once
on 2026-10-14**. The repaired bytes are **unconfirmed, pending round 5**, one
fresh confirmation review. This version is not yet recommended for signing.
Each repair is mapped in `ROUND-4-DISPOSITIONS.md`, and none needed a choice
from you.
*(Marked 2026-10-14: "pending round 5" is no longer true. Round 5 read the
repaired bytes and returned `REVISE`, one revise finding (33) and five
notes (34–38) (`docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-5-RAW.md` line 4).
Under the stopping rule recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md` the
package is not repaired again and comes to you with those findings open;
`ROUND-5-DISPOSITIONS.md` beside this file classifies them.)*
*(Marked 2026-10-14, later the same day: "not repaired again" and "with
those findings open" are superseded. On your further direction that day,
relayed by the lead session, one more cycle ran: **round-5 findings
repaired once on 2026-10-14, unconfirmed pending round 6**. Every round-5
finding, notes included, is repaired and mapped in `ROUND-5-DISPOSITIONS.md`
§"Repairs, 2026-10-14 (cycle 2)"; round 6 is briefed in `REVIEW-BRIEF.md`
§"Round 6" and not yet run. A notes-only round 6 clears these bytes; a
`REVISE` comes back to you. No repair needed a choice from you, and no
question was added.)*
*(Marked 2026-10-14, round 6: "unconfirmed pending round 6" and "not yet
run" are no longer true. Round 6 ran and returned `REVISE`
(`docs/reviews/R-M9-POC-IDENTITY-AMENDMENT-6-RAW.md` line 4): two revise
findings (39, the declared identifier field is written by the slice under
test while the RFC6-1 covered row keeps its claim; 40, the new
unattributed-carrier limb falsifies seeded subjects such as POC-REQ-051's
region) and three notes, all open in `ROUND-6-DISPOSITIONS.md`. Under the
stopping rule the package is not repaired again and this version is not
offered for sign-off; it comes to you with those findings open.)*

## What you would be signing

One amendment to the signed Three-Surface POC specification, the one P-75
ruled. Read `SEMANTIC-DELTA.md` for the full account. In short:

- **POC-REQ-054 (new).** Every subject has one identity, the same on Polaris,
  Trajectory, Orrery and the machine answer. Links between surfaces resolve by
  it. Where a surface shows one claim's desired, execution and observed states
  together (the "ribbon"), a slot nothing fills says Unknown with a reason and
  a route; it is never blank and never a score.
- **POC-REQ-055 (new).** Every relationship the POC emits either carries a
  name from RFC1-25's closed table, in a role pair the table assigns it, or
  carries a flag saying it is outside that table. **None of today's nine
  relationships complies.** Seven kinds are outside the table. The eighth,
  `contains`, joins a project to a capability, a pair its row does not
  assign. The signed coverage row that mapped this to POC-REQ-052 stays as it is. Beside
  it, an added row and a disclosure say that the flag is the repair you
  ruled. Closure itself — no outside kind emitted at all — stays Unknown.
  The role-pair check reads each POC kind through a declared mapping to
  RFC 0001's classes. Whether that mapping is true is not decided by any
  check, so it stays Unknown too, as does whether a named relationship
  honours its row's semantic class and rule.
- **POC-REQ-060 (amended).** The one-encoding rule now names all three labels,
  Observed, Inferred and Unknown, and one record shape. Inferred is allowed
  only for an agent's assertion and never counts as Observed. Nothing
  produces one today.

**Two departures from the design you adopted.**

**Departure 1 — the join key.** The M9 design said
POC-REQ-054 "Declares the canonical join key". This package does not: it
requires one identity per subject but leaves the identity's *form* to the
implementation slice.

- **Why.** The design's proposed key, `repository:<repo>@<rev>:<path>#<objectId>`,
  contains a file path. RFC6-1 bars a file path from being a selection
  identity, so writing that key into the signed text would put the
  specification against a contract clause. [Inferred]
- **The consequence if you sign.** Slice 6b picks the form under POC-REQ-054
  with no further act from you. It also declares, per source, which field
  of that source's records is the identity the source owns. Until it does,
  that source's subjects are of Unknown ownership: the check reports their
  identity equality as Unknown, never as passing. *(Added 2026-10-14,
  cycle 2.)*
- **If you would rather settle the form in the specification,** answer
  "Revise" below and name it.

**Departure 2 — role pairs, not only kinds.** The M9 design said "Every
emitted kind is either an RFC1-25 name or carries an explicit
out-of-vocabulary flag". POC-REQ-055 also checks that a named relationship
joins the kinds of thing the table allows for that name.

- **Why.** RFC1-26 forbids re-typing, so a correct name between the wrong
  kinds of thing is not compliant either. This is why `contains`, from a
  project to a capability, is flagged too. [Inferred]
- **The consequence if you sign.** Slice 8 also writes a declaration
  mapping the POC's kinds to RFC 0001's classes. Whether that mapping is
  true stays Unknown.
- **If you want the kind check alone,** answer "Revise" and say so.

**What signing does not do.**

- It starts no implementation. M9 slices 4–8 become eligible to start under
  your ruling only after this sign-off.
- It does not make the Inferred arm constructible in production. Under your
  ruling (P-75 Q4) the arm stays a typed landing zone with no production
  constructor, and a production constructor needs its own act.

## Question 1 — sign this version?

| Option | Meaning |
|---|---|
| **Sign v1.0** (recommended once the review clears) | The patches are applied in the sign-off change, and the specification reads 26 requirements. |
| Decline | The specification stays at 24 requirements, and M9 slices 4–8 stay blocked. |
| Revise | Name what to change; a new version gets a new review round. |

## Question 2 — by which route? (answered 2026-10-14)

**Answered by your direction of 2026-10-14.** In answering P-97's own
Question 2 you selected "Extend Scope A to POC", recorded in
`../../../decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`.
That direction extends the Scope A version-tag route to Three-Surface POC
specification amendments generally and names this package as following it
when it clears. So this package is signed, if you sign it, by selecting a
version under Question 1; no phrase or digest is needed, and the signing
change registers it with `scripts/record_versioned_signoff.py`, naming that
direction as its Scope A extension. Only Question 1 is still open. The text
and table below are kept as drafted.

The 2026-10-02 versioned sign-off direction (Scope A) covers "the PWB
specification deltas, the observer registry entry and the contract
successors queued behind them". A Three-Surface POC specification amendment
is not in that list. *(Marked 2026-10-14: true of the 2026-10-02 direction
alone; the 2026-10-14 extension above adds POC specification amendments.)*

| Option | Meaning |
|---|---|
| **Extend Scope A to this package** (recommended) | You sign by selecting a version in a structured question. No phrase and no digest are needed. The sign-off change registers the package with `scripts/record_versioned_signoff.py`. This is the same kind of artifact as the PWB deltas, an implementation-phase specification amendment, and it carries the same review requirement. |
| Phrase and digest | A dedicated recorder is written, and you type a phrase naming the manifest digest, as for the 2026-09-29 readability successor act. |

**If unanswered,** nothing is signed and the package stays a candidate.
*(Marked 2026-10-14: Question 2 is answered, above; the sentence still
holds for Question 1.)*
