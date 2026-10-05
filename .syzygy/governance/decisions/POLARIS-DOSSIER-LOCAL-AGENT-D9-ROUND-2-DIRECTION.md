# Owner direction — D9 (SEC-3) after its second review

Date: 2026-10-06

Owner: Tzeusy

Decision ID: `POLARIS-DOSSIER-LOCAL-AGENT-D9-ROUND-2-2026-10-06`

This direction follows the `POLARIS-DOSSIER-LOCAL-AGENT-*` directions of
2026-10-05. The candidate doctrine amendment D9 (SEC-3 and the owner's
attended agent session, draft PR #357) received a second `REVISE`
(`docs/reviews/R-DOCTRINE-AMENDMENT-D9-2-RAW.md`, over the bytes at
`63e41968`). Its review brief's stopping rule sends a second `REVISE` to the
owner before any further round.

It is a plain owner direction. It binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing. It does not adopt D9 and
edits no doctrine byte; only the owner's adoption act does that (VIS-4).

## The owner's words

On 2026-10-06, in the Claude Code CLI, the owner answered two structured
questions. For each, the selected option is reproduced with its description
as shown.

**Q1.** "The SEC-3 amendment (D9) got a second REVISE, so by our stopping
rule it comes to you. Main issue: the recommended text lets ANY Syzygy
instruction (any feature, incl. future dispatched work items telling a
worker to run tests) permit your attended agent to run the target project,
once you've recorded a choice — wider than your dossier-only ruling, and the
packet wrongly called it minimal. How wide should the permission be?"

| Label | Description |
|---|---|
| "Any feature, per-run choice (Recommended)" | "Any Syzygy instruction may permit it, but only on a choice you record for that one run, naming what it covers; no standing approval. Packet states plainly it's wider than the dossier ruling. Future features need no new doctrine act." |

Options not taken: "Dossier briefs only" and "Any feature, standing choice".

**Q2.** "Second issue: the 'no Syzygy credential readable' condition only
covers the session itself, not a server/background job it leaves running
afterwards, so RFC5-24 ('never visible to observed-project code') could
still fail. How to proceed?"

| Label | Description |
|---|---|
| "Close the gap, one more round (Recommended)" | "Extend the condition to every process the session starts, for as long as any runs; fix the packet wording per your scope answer; one confirming round 3. A third REVISE comes back to you." |

Option not taken: "Accept the gap, adopt soon".

## The direction

1. D9's recommended arm may permit execution through any Syzygy
   instruction, in any feature, only on a choice the owner records for that
   one run, naming what it covers. No standing or per-project record
   qualifies. The packet states that this is wider than the dossier ruling.
2. The credential condition reaches every process the session starts, for as
   long as any of them runs.
3. The package is repaired once, and one confirming round 3 is dispatched. A
   third `REVISE` returns to the owner.
