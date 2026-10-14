> # Record beside the package — not authority, binds nothing
>
> Dispositions of the third fresh-context review of the Three-Surface POC
> governing-intent amendment (POC-REQ-014, P-100). This record is not one
> of the ten files the round read and no builder reads it. It is the
> sibling record the owner's 2026-09-26 ruling provides for a notes-only
> round (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
> §1), named by this package's round-3 brief (`REVIEW-BRIEF.md` §"Round
> 3"). It offers nothing and performs no act (VIS-4).

# Round 3 dispositions — Three-Surface POC governing-intent amendment

Reviewed record: docs/reviews/R-N10-POC-GOVERNING-INTENT-3-RAW.md

Package digest: 9d97c13d78689784f0f85556821e04ae72b0dd338b372d7bdb8ccc651a8bbbcc

Revise-severity findings: 0

- **Reviewed commit (raw line 2):**
  `52c1d0f5536260628de7633126ef21748fe5e95e`.
- **Verdict (raw line 4):** `CONFIRM WITH EXCEPTIONS`. Seven findings,
  every one a note; no revise and no blocking finding (raw line 59).
- **Why the round ran.** The owner's direction of 2026-10-14 for a second
  cycle, recorded in
  `../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`:
  repair every finding, notes included, then one fresh review under the
  same stopping rule. The brief's §"Round 3" set that rule before the
  round. It carries the warrant as "[Observed: as relayed; not recorded
  under `decisions/` at the commit this section was written]"; the
  direction record now holds it.
- **What clears.** Under the 2026-09-26 ruling, a round with no
  revise-severity finding clears the exact bytes it read. Those are the ten
  tracked files of this directory at the reviewed commit, whose directory
  digest stands above. [Observed 2026-10-14] That digest re-derives by the
  brief's method from the bytes at the reviewed commit. `git diff --stat
  52c1d0f5` over this directory was empty on the integration branch before
  this record was added, and the four patches pass `git apply --check`
  against the signed tree there.
- **This record and the digest.** The brief places this record in the
  package directory, so the brief's command run over the directory now
  counts eleven files and gives a different value. The cleared digest is
  the one over the ten files the round read. The sign-off recorder treats
  a sibling `ROUND-<n>-DISPOSITIONS.md` record as outside the package bytes
  (`scripts/record_versioned_signoff.py`, docstring item 5).
- **Nothing else in the package is edited.** Every note below is
  dispositioned here, not in the reviewed bytes. Repairing any of them in
  the package would retire the clearance (rule 10). Each is **open** for
  the owner, with the repair the raw suggests.
- **What the clearance is not.** It is not a sign-off. Q1–Q3 stay the
  owner's (VIS-4). This version may now be offered for sign-off by version
  tag under `../../../decisions/OWNER-DIRECTION-SCOPE-A-POC-AMENDMENTS-2026-10-14.md`,
  once the residual below is met.

## Corrections carried here instead of in the package (finding 6)

These sentences in the cleared bytes are no longer true as of 2026-10-14.
This record, not an edit, carries the correction:

- `OWNER-DECISION-PACKET.md` lines 23–27, "**Round-2 findings repaired
  once on 2026-10-14, unconfirmed pending round 3.** … Round 3 is briefed
  in `REVIEW-BRIEF.md` §"Round 3" and has not run." Round 3 has run and
  returned `CONFIRM WITH EXCEPTIONS` with notes only, so the repaired bytes
  are cleared, not unconfirmed.
- `SEMANTIC-DELTA.md` lines 12–13 and `IMPACT-LEDGER.md` lines 8–9, each
  "**State:** round-2 findings repaired once on 2026-10-14, unconfirmed
  pending round 3". The same correction applies.
- `IMPACT-LEDGER.md` lines 110–112, "P-84 is being repaired in a separate
  lane on 2026-10-14", and `SEMANTIC-DELTA.md` lines 356–358, "P-84 is
  being repaired in a separate lane the same day". P-84's repair had
  already landed (`0ea9b491`, the reviewed commit's parent). Its round 6
  has since returned `REVISE`, so P-84 is not cleared.
- `ROUND-2-DISPOSITIONS.md` head mark (lines 6–10) and stopping-rule mark
  (lines 41–50), "unconfirmed pending round 3" and "round 3 is briefed".
  The same correction applies.

Register row P-100 and `docs/README.md`'s N10 row sit outside the package
and are updated directly.

## A residual for the sign-off recorder

[Observed 2026-10-14] This package is not registered in
`scripts/record_versioned_signoff.py`'s package table. Its raw's head
carries `Package digest:`, not `Manifest SHA-256:`, so `parse_head`
refuses it: "review head does not carry exactly one `Manifest SHA-256:`
line". Its findings section parses: seven findings, all notes. Recording
a sign-off on this raw needs the package registered and recorder support
for a directory-digest head. The raw is not edited.

## Dispositions

### 1 — the narrowing and expansion arms cannot tell a working filter from a no-op (note)

**Open.** Raw line 38. Every served item's `governedBy` is the same
Unknown, so a narrowing control that does nothing passes the oracle's
narrowing arm. A filter that drops or adds items still fails. Suggested
repair: one clause in the RFC8-23 covered row and the RFC8-24 aggregation
row, or in the delta's §"How each Trajectory arm is decided", saying the
filter is exercised only over an all-Unknown population.

### 2 — the resolution-statement procedure has a judgment step, and RFC8-31 is cited unquoted (note)

**Open.** Raw line 41. "In a statement that supplying it resolves an
item" is a reading, not a literal. The delta cites "read as text alone
(RFC8-31)" without quoting the clause (verification rule 8). No covered
row changes. Suggested repair: a declared sentence or key phrase for the
statement, and the RFC8-31 quotation with its anchor.

### 3 — two "outside" figures may appear on Trajectory (note)

**Open.** Raw line 44. Signed POC-REQ-042 reconciles against the Dolt
total and POC-REQ-014 against the served Unknown count. Neither says
whether POC-REQ-014's outside figure is POC-REQ-042's excluded count.
Suggested repair: one Scope sentence.

### 4 — P-84 composition: a new semantic dependency on POC-REQ-060 is unrecorded (note)

**Open.** Raw line 47. The four-file patch conflict with P-84 is the
declared mutually exclusive pair, not a new conflict. What the overlap
sections miss: POC-REQ-014's encoding arm is now decided against
POC-REQ-060's declared table, which P-84 amends. If P-84 is signed first,
this package's encoding arm and its RFC2-24 and RFC8-24 rows are to be
re-judged against the amended POC-REQ-060, not only regenerated.
[Observed 2026-10-14] P-84's round 6 returned `REVISE`, so P-84 is not
offered for sign-off at present.

### 5 — the packet does not say which route Trajectory will display (note)

**Open.** Raw line 50. Every count on Trajectory would also show the
RFC2-24 #10 route "Repair the observer/source; new snapshot", which the
delta says cannot resolve this Unknown by itself. Suggested repair: one
sentence under the packet's "What is already drafted".

### 6 — status sentences this round makes stale (note)

**Dispositioned by this record.** Raw line 53. The stale sentences inside
the package are listed under "Corrections carried here" above and are not
edited, as the raw advises. Register row P-100 and `docs/README.md`'s N10
row are updated outside the package.

### 7 — items confirmed without exception (note)

**No action.** Raw line 56. The raw records criteria 1–7 as met, subject
to findings 1, 4 and 5. Nothing to disposition.
