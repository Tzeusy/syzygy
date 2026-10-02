# Owner direction — lane B declined; the Polaris page-size target revised

Date: 2026-10-02

Owner: Tzeusy

Decision ID: `POLARIS-LANE-B-DECLINED-TARGET-REVISED-2026-10-02`

Gate bead: `syzygy-dov.17`. Answers row **P-68** of the pending register,
option (c), and revises Q3 of `POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`.

This is a plain owner direction in the shape of
`POLARIS-RESPONSE-CEILING-READING-DIRECTION.md`. It binds no artifact digest,
adds no row to `ACCEPTANCE-ACT-RECORD.md` and registers nothing.

## The owner's words

On 2026-10-02, in the Claude Code CLI, the owner answered one structured
question after the narrowed lane B was drafted and re-measured at about 50 KB
[Inferred], about 28 KB short of the 1.4 MB target:

> Is that worth a spec and contract change?

The option selected, with its description as shown, byte-for-byte:

| Label | Description |
|---|---|
| "Close it, revise target (Recommended)" | "50 KB doesn't reach the target and costs two governed changes. I decline lane B, set the working target to the ceiling minus the pending repairs' margin, and leave the spec and RFC7-33 untouched." |

Earlier the same day the owner chose to narrow lane B to page-invariant values
only ("Narrow lane B (Recommended)"); this direction supersedes that choice
after the re-measurement.

## The direction

1. **Lane B is declined.** The scoped-attributes behavior package and the
   RFC-0007 scoped-values contract successor are not offered for sign-off and
   are banner-marked declined. The specification, RFC7-33 and RFC7-16 stand
   unamended. Nothing was ever applied.
2. **The target is revised.** The working target for the Polaris human page is
   the 2,097,152-byte response ceiling less the 443 KB margin the pending
   Butlers repairs may add [Inferred], that is 1,650,000 bytes on both host
   forms, replacing the 1,400,000-byte figure of Q3. The 1,000-bytes-per-new-item
   slope target is withdrawn with it. The response ceiling itself and the
   refusal on breach are unchanged.
3. **Not affected.** Lane A's trim, the P-63 shape and every other M1 ruling
   stand. Compression (see `POLARIS-RESPONSE-CEILING-READING-DIRECTION.md`)
   changes bytes sent, not the checked size.
4. **Reversible.** A later direction may reopen scoped values; the declined
   packages and their review raws remain as the record.
