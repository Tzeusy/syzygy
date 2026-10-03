# Review brief — D7 doctrine amendment packet, round 1

> **Candidate — binds nothing.** The brief for one fresh-context review of
> this package (CC-REV-1). A review is evidence for the owner; it adopts
> nothing and its verdict is not an owner act (VIS-4).

## Stopping rule, set before the round

One round. Whatever the verdict, the drafter repairs each finding once and
records each finding and its repair in `ROUND-1-DISPOSITIONS.md`; no round
2 is dispatched. Repaired bytes go to the owner marked as repaired and
unconfirmed. A verdict is never re-labelled.

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
