# Owner direction — what the Polaris response ceilings measure under compression

Date: 2026-09-30

Owner: Tzeusy

Decision ID: `POLARIS-RESPONSE-CEILING-READING-DIR-2026-09-30`

Gate bead: `syzygy-dov.27`; unblocks `syzygy-dov.10.4` (M10 slice 4b).
Warrant for the question: row **P-77**, question 2, of
`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` (this directory).
Offering: `POLARIS-RESPONSE-CEILING-READING-DECISION-PACKET.md` (this
directory). The packet remains the question and is not edited.

This is a plain owner direction in the shape of
`POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md`. It binds no
artifact digest, needs no manifest or recorder script, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing in `check_governance.py`.

## The owner's words

On 2026-09-30, in the Claude Code CLI, the owner answered one structured
question on this packet. The question as put:

> Response ceilings once compressed (PR #117). Polaris refuses pages over
> 2 MiB and machine answers over 8 MiB. With gzip, 'size' could mean before
> or after compression. Recommended answers: Q1(a) the ceiling measures the
> body before compression (what the code does today, so no limit weakens);
> Q2(a) the same reading covers later ceilings such as .18's briefing
> ceiling; Q3(a) the difference is recorded in the direction and bead only,
> with no new header; Q4(a) no PWB-REQ-006 amendment needed; Q5(a) gzip
> only, only when it shrinks the body; Q6(a) issued as a plain dated
> direction. Issue that direction?

The option selected, with its description as shown, byte-for-byte:

| Label | Description |
|---|---|
| "Yes, all (a) (Recommended)" | "I record the plain dated direction with Q1–Q6 (a); gzip compression (slice 4b) may then ship." |

The owner did not type an issuing line. The selection is the issuing
instruction, and this record quotes it without substituting any other
wording for it. The direction below is the packet's proposed text for
Q1 (a) through Q6 (a), with the date filled in and nothing else changed.

Repository state at recording: Syzygy `origin/main` at `6583045`.

## The direction, as issued

```
OWNER DIRECTION — WHAT THE POLARIS RESPONSE CEILINGS MEASURE UNDER
COMPRESSION

Date: 2026-09-30
Owner: Tzeusy
Continues: decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md and
decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md, whose
registry-envelope escalation trigger this direction answers and does
not widen. Answers P-77 Q2
(decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md).

1. THE READING. [Q1] Each response ceiling in the observer registry
   entry's resource envelope whose sentence reads "the final encoded
   HTTP body" measures the response body in its final character
   encoding, before any HTTP content coding is applied. Today that is
   maxHumanResponseBytes and maxMachineResponseBytes. [Q2] It is also
   any such ceiling adopted after this direction. The number checked is
   the one routes.ts checks today.

2. WHAT MAY SHIP. [Q5] gzip response compression, applied only when the
   client accepts gzip and only when the compressed body is smaller than
   the body that passed its ceiling, with Vary: Accept-Encoding set.
   Because of that rule the bytes sent never exceed the bytes checked.

3. WHAT DOES NOT CHANGE. The declared values, the refusal on breach (a
   bounded typed failure, nothing truncated, nothing success-shaped),
   the breach record and readiness false on breach. A response that is
   refused today is refused after compression ships.

4. DISCLOSURE. [Q3] The size sent and the size checked are deliberately
   different numbers. This direction and the slice-4b bead say so. No
   new header or machine field carries the checked size.

5. WHAT THIS DOES NOT DO. It edits no registry, specification or policy
   byte [Q4: no PWB-REQ-006 amendment is needed]. It sets no new or
   relaxed ceiling, adds no route, reads no new source and widens no
   act. Every exclusion of the 2026-09-02 authorization and its
   2026-09-05 continuation stands.

6. WHAT THIS IS NOT. It binds no artifact digest, adds no row to the
   acceptance-act record and registers nothing. It is a warrant, not
   evidence: it proves no response was measured or served.

7. WITHDRAWAL. A later direction may narrow or withdraw this one.
   Withdrawal defeats grant: on withdrawal no response is compressed.
```

## Notes on the record

- [Observed] The same day, the owner adopted the registry
  currency-and-briefing amendment
  (`PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`), which
  declares `maxBriefingResponseBytes` with the "final encoded HTTP body"
  sentence. Under paragraph 1's Q2 clause that ceiling bears the same
  reading. No route is served under it until its machine-view
  specification is signed off.
- The confirmation review's notes N2–N4 stay routed to `syzygy-dov.31`.
  Issuing this direction does not discharge them.
