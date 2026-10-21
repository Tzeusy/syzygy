# Round-3 dispositions — PWB M2 slice 5 continuation packet

> **Candidate — binds nothing.** This record dispositions one review round.
> It performs no act and authorizes nothing. It sits beside the packet so
> that the packet itself never carries review history, and it edits none of
> the reviewed bytes.

- Raw: `docs/reviews/R-PWB-M2-SLICE5-CONTINUATION-PACKET-3-RAW.md`,
  retained byte-for-byte (CC-REV-6).
- Cleared commit: `78d18444f8728762cdf3ed2ff28397c9030af4ef`.
- Cleared packet digest (SHA-256 of `OWNER-DECISION-PACKET.md` at that
  commit, computed by script):
  `1449eadca4f5eca3b6dd731de4f01c0d373193d83a77446e5ea72389ad013c97`.
  It is not an act argument, since this package binds no digest.
- Verdict, copied from raw line 4: `CONFIRM WITH EXCEPTIONS`.
- Findings: five, all notes; no revise-severity finding. The raw says "this
  round has notes only, so it clears these bytes" (raw line 85).

**These bytes are cleared.** Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
§1), a round with no revise-severity finding clears the exact bytes it
read. The notes go here, and none of the five package files reviewed at
`78d18444` is edited. Repairing note 3 or 4 inside the packet would retire
the clearance (rule 10).

Each note below is carried to the implementer of `syzygy-dov.2.2` or to
the lead. None changes what the reply would authorize. Line numbers are
those at `78d18444`. I confirmed that `apps/three-surface-poc/src/design-tokens.ts`
and `apps/three-surface-poc/src/polaris.ts` are unchanged between that
commit and this record's (`git diff --stat` is empty).

## Notes

**1 — B7's `stale` marker becomes false once slice 5 lands. Carried to
the implementer.**

- `[Observed]` The legend drops a value's unreachable marker only when
  some claim carries that value (`used(entry)`, `polaris.ts` lines
  403–407). The `stale` marker reads "Not reachable at this evaluation: no
  claim freshness is judged against a currency bound; declare the bound
  and route freshness through the currency assessor."
  (`design-tokens.ts` lines 91–92).
- After slice 5 every judged claim is judged against a bound. On an
  evaluation where the judge returns no `stale`, that sentence would still
  print, and it would be false.
- B7's own purpose ("keeps every freshness legend sentence either
  reachable or marked unreachable with its reason") already requires the
  rewrite, so this is an over-short clause, not new behavior.
- **For the implementer.** Rewrite the `stale` unreachable reason in
  `design-tokens.ts` to a sentence that is true once the judge runs, for
  example that no claim's evidence is older than its class's bound at this
  evaluation. Make the slice-1 copy oracle and B10's legend check assert
  the new reason, and give it a rule-6 mutant.
- `[Inferred]` Re-read the other three markers against slice 5's
  behavior too. The reviewer judged `fresh`, `broken` and `superseded`
  still true. The `fresh` marker ("no claim was captured at this
  evaluation") should be checked against an evaluation where every judged
  claim is `stale`.

**2 — B5's "never a bare `0`" has no stated machine-channel form. Carried
to the implementer.**

- B5 renders the `broken` and `superseded` counts with the unreachable
  marker and never as a bare `0`, and B6 requires the same counts in both
  channels. A JSON count field cannot carry a number and a marker together
  without a chosen form.
- **For the implementer.** Choose one typed form for an unreachable count
  in the machine answer. It must not be a sentinel string or a `null`
  spelled as a count, which B4's rule against minted values forbids for
  freshness. Add it to the PWB-REQ-020 parity family that B6 names, so a
  machine `0` beside a human marker fails the sweep.
- `[Inferred]` One form that meets both rules is an unreachable-value
  entry that carries the value, the marker reason and no count field. The
  lane may choose another, so long as both channels carry the same one. If
  no form can be found inside B5 and B6, the lane stops and returns to the
  owner (packet "Escalation triggers").

**3 — The RFC6-14.r3 cell was not widened with its three siblings. Recorded;
the packet is not edited.**

- `[Observed]` Round 2 added the not-evaluated shape's claim to the
  RFC6-14.r1, RFC7-16.r1 and RFC7-33.r1 "What stays Unknown" cells
  (packet lines 442, 445 and 446). The RFC6-14.r3 cell (line 443) still
  names only "Whether an absent freshness value plus the disclosure is
  'the complete epistemic tuple'".
- Read here as widened: the not-evaluated claim's machine tuple also lacks
  freshness and carries no arm disclosure, so it too stays Unknown under
  RFC6-14.r3.
- Nothing is built differently. The build claims no conformance on
  RFC6-14.r3 either way, and the row stays `unknown-uncovered`.
- A recorder who copies the gap table verbatim into the direction record
  (packet §"The record a recorder would write") copies line 443 as it
  stands, and cites this note beside it.

**4 — The packet header still says "repaired after review round 1".
Recorded; the packet is not edited.**

- `[Observed]` Packet line 13 reads "Date drafted: 2026-10-21; repaired
  after review round 1 the same day."
- The bytes were also repaired after round 2. The clause is true but
  incomplete. It is review history inside the packet, which the packet's
  own Review section says lives in sibling records.
- The full history is: round 1 `REVISE` over `268f1773`, round 2 `REVISE`
  over `04e86895` (rebased twin `d7b2d7e5`), round 3
  `CONFIRM WITH EXCEPTIONS` over `78d18444`. The dispositions are in
  `ROUND-1-DISPOSITIONS.md`, `ROUND-2-DISPOSITIONS.md` and this file.

**5 — Bead bookkeeping. Carried to the lead, who is handling it; no bytes
here.**

The raw names three coordinator steps:

- **(a)** Add the explicit gate dependency to `syzygy-dov.5.2` before
  `syzygy-dov.19` closes. The raw observed only the HOLD note so far.
- **(b)** `syzygy-dov.5.2`'s title still says "blocked on the
  machine-view delta and the registry act", both of which are done.
- **(c)** Comment on `syzygy-dov.19` pointing to
  `ROUND-2-DISPOSITIONS.md` note 2, so that a later reader does not take
  acceptance criterion 6 as met literally.

The coordinator owns every `bd` mutation, so this record changes no bead.

## What this round leaves for the owner

Nothing beyond the reply. The bytes at `78d18444` are cleared. The reply
may be offered as the packet's question states, with this record and the
two earlier dispositions beside it.
