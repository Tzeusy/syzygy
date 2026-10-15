# Review brief — D7 doctrine amendment packet, round 1

> **Candidate — binds nothing.** The brief for one fresh-context review of
> this package (CC-REV-1). A review is evidence for the owner; it adopts
> nothing and its verdict is not an owner act (VIS-4).

## Stopping rule, set before the round

One round. Whatever the verdict, the drafter repairs each finding once and
records each finding and its repair in `ROUND-1-DISPOSITIONS.md`; no round
2 is dispatched. Repaired bytes go to the owner marked as repaired and
unconfirmed. A verdict is never re-labelled.
*(Marked 2026-10-14: "no round 2 is dispatched" is no longer true. A round
2 ran on the owner's direction of 2026-10-14
(`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2026-10-14.md`;
raw `docs/reviews/R-DOCTRINE-AMENDMENT-D7-2-RAW.md`), and on the owner's
further direction the same day its findings were repaired and a round 3
is briefed in §"Round 3" below. This round-1 brief is otherwise unchanged.)*

## Subject

The tracked files of
`.syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7/`
at the reviewed commit, excluding this brief's own later edits (there are
none before the round): `OWNER-DECISION-PACKET.md`, `SEMANTIC-DELTA.md`,
`IMPACT-LEDGER.md`, `REVIEW-BRIEF.md`.

## Governing references

- `.syzygy/governance/doctrine/vision.md` (VIS-4, VIS-5, VIS-6, "What
  Syzygy is not", "Eventual mandate: live fleet observability"),
  `architecture.md` ("Snapshots and the loop"), `v1.md` (deferrals),
  `security.md` (SEC-2, SEC-3, SEC-5).
- `.syzygy/governance/decisions/D4-RULING-DECISION.md`;
  `BOUNDED-MISSION-DOCTRINE-INTERPRETATION-ACT.md`;
  `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` (P-69, P-71, P-79);
  `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md`;
  `POLARIS-TRUSTED-BOOTSTRAP-OBSERVATION-DIRECTION.md`;
  `DOCTRINE-AMENDMENT-LOG.md`.
- Accepted contracts: RFC2-19 (`contracts/rfcs/RFC-0002/reconciliation-chain.md`),
  RFC4-16 (`contracts/rfcs/RFC-0004/named-adapters.md`), RFC5-11
  (`contracts/rfcs/RFC-0005/admission-and-boundary.md`).
- `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` (Q3);
  `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` (Q4).
- `contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md`.
- `contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md` and
  `SEMANTIC-DELTA-TEMPLATE.md`.
- The pursuit's N14 section, `docs/pursuits/2026-09-22-vision-pursuit.md`,
  and its data file.

## Acceptance criteria (from bead `syzygy-u05.14`)

1. Drafted amendment text with a trigger test, a permitted list and
   prohibitions.
2. A blast-radius sweep over P-69, P-71 Q3, P-79 Q4 and VIS-6(a), each
   permitted effect mapped to a ruling that already allows it narrowly.
3. Entry criteria for the live fleet observability mandate.
4. An owner decision packet with a no-change arm.
5. Nothing adopted by agents; no doctrine byte edited; no code; the
   Butlers-side push trigger and the regeneration rehearsal described only
   as owner options or packet obligations, nothing installed, written or
   run.

## What to test, at least

- Is the change class (Normative) right? Is the non-expansion claim
  (section 3) honest about what D7 adds?
- Does any quoted text differ from its source? Are the anchors, line
  numbers and sha256 values right at the reviewed commit?
- Does the proposed text say what section 2's table says, no more, no
  less? Could it be read to license an effect the packet says it forbids?
- Is the VIS-4-bounds position (section 7) argued, and is the "beyond"
  arm's consequence stated correctly?
- Is the RFC2-19 reading right, and is anything else in force made false
  by arm A that the ledger missed? Re-run the ledger's sweeps.
- Does the composition with candidate D3 (section 1.3) hold?
- Are the entry criteria testable, and do they stay off doctrine as
  claimed?

## Output

Write the raw review to docs/reviews/R-DOCTRINE-AMENDMENT-D7-1-RAW.md (a
file this round creates).
Its first four non-blank lines must be exactly:

```text
# Review - D7 doctrine amendment packet (held derived computation, P-101)
Reviewed commit: <the full 40-hex commit you reviewed>
Package digest: <sha256 by the method below>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

Package digest method: at the repo root of a clone at the reviewed commit,
`sha256sum $(git ls-files .syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7 | LC_ALL=C sort) | sha256sum`.
Number every finding, label each `[Observed]`, `[Inferred]` or
`[Unknown]`, and mark each as revise-level or a note.

## Round 3

*(Added 2026-10-14, before the round, by the cycle-2 repair lane. Nothing
above this heading governs round 3 except where this section says so.)*

**Warrant.** The owner's direction of 2026-10-14, given in the lead session
and relayed to the repair lane: repair every round-2 finding, notes
included, then one fresh review under the same stopping rule [Observed: as
relayed; not yet recorded under `decisions/`]. *(Marked 2026-10-14, cycle
3: "not yet recorded" is no longer true; the direction is recorded in
`../../../decisions/OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`.
Round 3 ran and returned `REVISE`; round 4 is briefed below.)*

**Stopping rule, set before the round.** One round.

- A verdict with **no revise-level finding** (`CONFIRM`, or `CONFIRM WITH
  EXCEPTIONS` whose findings are all notes) clears the exact bytes it read,
  under the owner's 2026-09-26 ruling
  (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1).
  Its notes go in a sibling `ROUND-3-DISPOSITIONS.md`, and the package's
  other files are not edited.
- A verdict of **`REVISE`** (any revise-level finding) goes back to the
  owner with its findings open: no further repair and no round 4 without a
  new owner direction.
- A clearance is not adoption; the owner's questions Q1–Q5 stay the
  owner's (VIS-4). A verdict is never re-labelled.

**Subject.** Every tracked file of
`.syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7/`
at the reviewed commit: `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
`REVIEW-BRIEF.md`, `ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md`,
`SEMANTIC-DELTA.md`.

**Governing references.** Those listed above for round 1, plus: the two
earlier raws, `docs/reviews/R-DOCTRINE-AMENDMENT-D7-1-RAW.md` and
`docs/reviews/R-DOCTRINE-AMENDMENT-D7-2-RAW.md`; RFC2-17, RFC2-18 and RFC2-19
in `contracts/rfcs/RFC-0002/reconciliation-chain.md`, and RFC2-1 in
`contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`.

**What to test, at least.**

- Is each of the eight round-2 findings repaired as
  `ROUND-2-DISPOSITIONS.md` §"Repairs, 2026-10-14 (cycle 2)" says, and did
  any repair introduce a new inaccuracy?
- Finding 1: are both readings of "merge fact" in packet §4.1 stated
  fairly from the clause text, is the reading the packet relies on labelled
  and argued, and do §0, §2, §4, §6, the ledger and the delta now say the
  same thing about what arm A permits on each reading? Is Q5 a well-formed
  owner question with honest consequences?
- Finding 2: re-run the ledger §4 reader sweep at `66d42d09` and check the
  enumeration sums to its figure.
- Finding 3: is the page-open residual named without changing section 1's
  text, and does anything now claim a test exists?
- Are the dated status marks at the stale sentences, with the old text
  kept, and is any stale sentence left unmarked?
- Re-check that section 1's proposed doctrine bytes are unchanged from the
  bytes round 2 read, and that the anchors' sha256 values still hold.

**Output.** Write the raw review to
docs/reviews/R-DOCTRINE-AMENDMENT-D7-3-RAW.md (a file this round
creates; left out of code span so the path check does not ask it to exist
first). **Head contract:** its first four non-blank lines must be
exactly these, with nothing appended to the title line:

```text
# Review - D7 doctrine amendment packet (held derived computation, P-101), round 3
Reviewed commit: <the full 40-hex commit you reviewed>
Package digest: <sha256 by the method below>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

`Package digest` is the brief's scripted method **at the reviewed commit**,
unchanged from round 1: at the repo root of a clean clone or worktree
whose `git rev-parse HEAD` is the reviewed commit,
`sha256sum $(git ls-files .syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7 | LC_ALL=C sort) | sha256sum`,
over the six files above. It is the digest of the package's own tracked
bytes, not of any single file, and it includes this brief. Number every
finding, label each `[Observed]`, `[Inferred]` or `[Unknown]`, and mark
each as revise-level or a note; close with the count of each.

## Round 4

*(Added 2026-10-14, before the round, by the cycle-3 repair lane. Nothing
above this heading governs round 4 except where this section says so.)*

**Warrant.** The owner's cycle-3 direction of 2026-10-14 for P-101, given
in the lead session: "One more cycle" — "Make Q5 consistent: state that
choosing a reading of accepted text is a contract act matter (Unknown
otherwise), and align §4/§6 and the ledger. Then one fresh review."
[Observed: as relayed by the lead session to this repair lane; not yet
recorded under `decisions/`.]

**Stopping rule, set before the round.** One round.

- A verdict with **no revise-level finding** (`CONFIRM`, or
  `CONFIRM WITH EXCEPTIONS` whose findings are all notes) clears the exact
  bytes it read, under the owner's 2026-09-26 ruling
  (`../../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1).
  Its notes go in a sibling `ROUND-4-DISPOSITIONS.md`, and the package's
  other files are not edited.
- A verdict of **`REVISE`** (any revise-level finding) goes back to the
  owner with its findings open: no further repair and no round 5 without a
  new owner direction.
- A clearance is not adoption; the owner's questions Q1–Q6 stay the
  owner's (VIS-4). A verdict is never re-labelled.

**Subject.** Every tracked file of
`.syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7/`
at the reviewed commit: `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
`REVIEW-BRIEF.md`, `ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md`,
`ROUND-3-DISPOSITIONS.md`, `SEMANTIC-DELTA.md`.

**Governing references.** Those listed above for rounds 1 and 3, plus:
the round-3 raw, `docs/reviews/R-DOCTRINE-AMENDMENT-D7-3-RAW.md`;
`contracts/rfcs/RFC-0004/named-adapters.md` lines 414–436 and 486–496;
`scripts/record_polaris_understanding_adoption.py` (its `VISION`,
`FROZEN_PATHS` and `HISTORY_PATHS` constants and its `reviewed_template`
check); `decisions/DOSSIER-LOCAL-AGENT-RFC7-20-READING-IN-FORCE-ACT.md`;
and candidate D8's packet §7 Q-A1
(`../doctrine-amendment-inferred-first-class-d8/OWNER-DECISION-PACKET.md`).
The reviewer **SHOULD** read the earlier raws
(`docs/reviews/R-DOCTRINE-AMENDMENT-D7-1-RAW.md`,
`docs/reviews/R-DOCTRINE-AMENDMENT-D7-2-RAW.md` and
`docs/reviews/R-DOCTRINE-AMENDMENT-D7-3-RAW.md`) and
`ROUND-3-DISPOSITIONS.md`, and check each round-3 finding against the
current bytes, not against the dispositions' account of them.

**What to test, at least.**

- Is each of the six round-3 findings repaired as `ROUND-3-DISPOSITIONS.md`
  §"Repairs, 2026-10-14 (cycle 3)" says, and did any repair introduce a
  new inaccuracy?
- Finding 1: does the packet now state one position — choosing a reading
  of accepted RFC2 text is a contract-act matter, [Unknown] until a
  contract act fixes it — and apply it to every reading alike? Do §0, §2,
  §4, §4.1, §6, §7, §8, the ledger and the delta say the same thing about
  what arm A permits for each class of repository? Is restructured Q5 a
  well-formed owner question with honest consequences on each arm, and is
  the claim that the round-2 arms collapse argued?
- Note 2: is RFC4's reading of RFC2-19 weighed fairly in §4.1, and is the
  broadest reading's effect stated without overstatement?
- Note 3: is the page-open obligation labelled as the packet's reading,
  and is it independent of Q3 everywhere it appears?
- The recorder gate: re-run the probe the ledger §4 records (apply section
  1.1 alone, then section 1.2 alone, in a scratch clone at the reviewed
  commit) and check the ledger, the delta, §9 and Q6 against its output.
- Are the dated status marks at the stale sentences, with the old text
  kept, and is any stale sentence left unmarked?
- Re-check that section 1's proposed doctrine bytes are unchanged from the
  bytes rounds 2 and 3 read, and that the anchors' sha256 values still
  hold.

**Output.** Write the raw review to
docs/reviews/R-DOCTRINE-AMENDMENT-D7-4-RAW.md (a file this round
creates; left out of code span so the path check does not ask it to exist
first). **Head contract:** its first four non-blank lines must be
exactly these, with nothing appended to the title line:

```text
# Review - D7 doctrine amendment packet (held derived computation, P-101), round 4
Reviewed commit: <the full 40-hex commit you reviewed>
Package digest: <sha256 by the method below>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

`Package digest` is the brief's scripted method **at the reviewed commit**,
unchanged from round 1: at the repo root of a clean clone or worktree
whose `git rev-parse HEAD` is the reviewed commit,
`sha256sum $(git ls-files .syzygy/governance/contracts/candidates/doctrine-amendment-held-derived-computation-d7 | LC_ALL=C sort) | sha256sum`,
over the seven files above. It is the digest of the package's own tracked
bytes, not of any single file, and it includes this brief. Number every
finding, label each `[Observed]`, `[Inferred]` or `[Unknown]`, and mark
each as revise-level or a note; close with the count of each.
