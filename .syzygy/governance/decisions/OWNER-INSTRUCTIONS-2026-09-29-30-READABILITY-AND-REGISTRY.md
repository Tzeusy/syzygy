# Owner instructions — how the 2026-09-29 and 2026-09-30 acts were given

Date: 2026-09-30

Owner: Tzeusy

Decision ID: `OWNER-INSTRUCTIONS-READABILITY-AND-REGISTRY-2026-09-30`

This record states exactly how the owner gave five digest-bound acts. It
performs no act, binds no digest and edits no act record. Each act record
listed below keeps its own bytes; its recorder regenerates them exactly.

## Why this record exists

Each of the five act records says the owner performed the act "by writing
exactly" its phrase. That wording comes from the recorder templates and
describes the phrase form an act takes. It does not describe what happened
here: in every case the owner **selected an option** in a structured
question in the Claude Code CLI and did not type the phrase. This record
states what the owner was shown and what the owner selected, and it is the
account to read beside those five records.

## The four readability successors — 2026-09-29

On 2026-09-29 the owner answered one question. The question as put:

> Do you sign off the four readability rewrites (Three-Surface POC,
> Capability 1, Polaris generator base, Polaris understanding amendment) as
> written in their owner packets? Each rewrites only the proposal and
> design text; every specification stays byte-identical, and each rewrite
> was independently reviewed and simulated with the full battery green.

The option the owner selected, with its description as shown:

| Label | Description |
|---|---|
| "Sign off all four" | "I record four acts with the exact phrases and digests from the packets, install the rewritten files, run the battery and merge." |

The four exact phrases, with their digests, were in the four owner packets
and in the assistant message just before the question. The question text
did not carry them. The selection is the instruction, and it named those
packets' phrases.

Acts recorded from that selection:

- `THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md`
- `CAPABILITY-1-READABILITY-SUCCESSOR-ACT.md`
- `POLARIS-GENERATOR-BASE-READABILITY-SUCCESSOR-ACT.md`
- `POLARIS-UNDERSTANDING-READABILITY-SUCCESSOR-ACT.md`

## The registry currency-and-briefing amendment — 2026-09-30

On 2026-09-30 the owner answered this question, as put. The act argument
is elided here and appears only in the act record:

> Registry currency and briefing (.18). This writes into the Butlers
> observer registry entry the values you chose on 2026-09-23 and
> 2026-09-26: 13 per-source maximum-age bounds and a 20,480-byte briefing
> response ceiling. Review 3 was a plain CONFIRM, the recorder validates,
> and it sits outside the eleven-file PWB spec chain. Adopt it? (Phrase:
> ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY: *[the
> argument recorded in the act record below]*)

| Label | Description |
|---|---|
| "Adopt (Recommended)" | "I record the act with that exact phrase and install the registry entry." |

In this case the question itself carried the full phrase. Act recorded:
`PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`.

## The read-gate direction that followed — 2026-09-30

Recording the registry act showed a consequence the packet did not state.
The daemon's body-read gate still expected the 2026-09-05 registry act.
Once the entry carried its new bytes, that act's digest no longer matched,
so the gate refused every Butlers read. The owner was asked:

> Adopting the new registry entry makes the Butlers read gate fail closed,
> because it still expects the 2026-09-05 act. Do you direct the
> implementation to evaluate the 2026-09-30 registry act instead? This
> covers only the act pointer, version anchor, tag and tests, and the new
> currency and briefing fields stay unread until dov.19.

| Label | Description |
|---|---|
| "Yes, re-point only (Recommended)" | "Plain owner direction, recorded dated: the gate evaluates the 2026-09-30 act and the 1.2.0 anchor. No new field is consumed, and every original exclusion stays. Polaris keeps reading Butlers." |

### The direction, as issued

A plain owner direction. It binds no digest, needs no manifest or
recorder, and adds no row to `ACCEPTANCE-ACT-RECORD.md`.

- **Permitted:** the implementation's body-read authority expectations for
  the registry role name the 2026-09-30 act record, its act identity and
  recording tag, the entry's `1.2.0-candidate.1` version anchor, and the
  2026-09-05 amendment record as the superseded target. Tests change to
  match.
- **Not permitted:** reading, evaluating or rendering the entry's
  per-class currency bounds, its currency semantics block, or
  `maxBriefingResponseBytes`. That remains gated on `syzygy-dov.19` and
  the further gates the 2026-09-21 rulings name. No briefing route is
  served.
- **Unchanged:** consent, content class, configured repository, write,
  egress, execution, deployment, release and multi-user exclusions, and
  the 2026-09-05 implementation continuation's other terms.

[Inferred] The re-point needs no new authority for the entry's unchanged
fields. The gate still evaluates the same repository, content class,
discovery grammar and read-only, empty-write-surface scope it evaluated
before.

## What this record does not do

It does not edit, re-date or supersede any act record, and it does not
change what any act bound. An act's validity rests on its exact argument
and its record, as before. This record corrects only the account of how
the owner gave each instruction.
