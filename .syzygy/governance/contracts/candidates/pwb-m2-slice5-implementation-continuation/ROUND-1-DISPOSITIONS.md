# Round-1 dispositions — PWB M2 slice 5 continuation packet

> **Candidate — binds nothing.** This record dispositions one review round.
> It performs no act and authorizes nothing. It sits beside the packet so
> that the packet itself never carries review history.

- Raw: `docs/reviews/R-PWB-M2-SLICE5-CONTINUATION-PACKET-RAW.md`, retained
  byte-for-byte (CC-REV-6).
- Reviewed commit: `268f1773ab70ace456847be0cca5bc960082ffb7`.
- Verdict, copied from raw line 4: `REVISE`.
- Findings: six revise (R1–R6) and nine notes (N1–N9). The raw names no
  owner-only decision beyond the reply itself (raw lines 148–150).

Each disposition names where the repair lands. "Packet" is
`OWNER-DECISION-PACKET.md`, "ledger" is `IMPACT-LEDGER.md`, "brief" is
`REVIEW-BRIEF.md`, all in this directory. Every figure, commit and line
below was re-derived from the file named at the commit named, not copied
from the raw.

## Revise findings

**R1 — PR #489 overlap misdescribed. Taken.**

- Read at PR #489's head `8c334f67` (branch `agent/syzygy-sin5`, fetched
  2026-10-21; `git log` shows `8c334f67` → `e990c27e` → `9e63b856` over
  `29e036f4`). At that head the record grants no overlap. Every use of the
  missing-currency disclosure waits for this act, including item depth's
  relation claims (`syzygy-dov.14.4`) and the opening band's count of
  members under the no-bound condition (`syzygy-dov.4.2`).
- **Decision: the named behavior covers both.** New item B11 in the packet
  says how, and authorizes nothing else in either lane:
  - relation claims are in the arm through B2 and take B4's no-bound arm,
    with PWB-REQ-015's own rule in place of B4's secondary-reason rule
    (one primary, no `missing-declaration`);
  - the band's count is B5's one count mechanism;
  - neither lane builds its own judge, marker or count;
  - slice 5 lands ahead of both uses.
- B2 now matches family patterns against the whole id, never a prefix, so
  a relation claim id that embeds an item id never takes the item's row.
  B5 now covers aggregates with no row of their own, the band among them.
  B10 adds a synthetic no-row-class fixture and a prefix fixture.
- The "no live members" inference is revised. The arm is empty when slice
  5 lands with the registry act effective. Item depth fills it, one relation
  claim per contract band, and an ineffective registry act fills it too.
  This is in packet §"Live members of the arm" and in the ledger's effects.
- The decline text now says that, under PR #489's record, item depth and
  the band's count stay unbuilt too.
- The overlap section is rewritten as "Composition with the 2026-10-20
  direction (PR #489)". It quotes `8c334f67`, says what `e990c27e` granted
  and `8c334f67` removed, and says that the first draft's description was
  wrong. The question now names both B11 uses.
- **Why cover them rather than leave them waiting.** That record says item
  depth "starts only once … the behaviour that act names covers the
  relation claims"; otherwise the lane escalates. Leaving the relation
  claims out would force a second continuation for behavior this mechanism
  already decides. You selected item depth, the opening band and
  missing-currency together on 2026-10-20. [Inferred]

**R2 — B4 against B5 for aggregates that are claims. Taken.**

B5 now states the precedence. The class aggregates and the whole-shape
claim each have a row of their own, so each takes its own freshness from
the judge under B4 and never from its members. An aggregate whose own row
is not effective is itself in the arm. An aggregate with no row of its own
carries no freshness value while it has a member in the arm.

The omitted limb is restored, in the packet's words: members in the arm
are presented "only through the same outside-slot named disclosure,
carrying their count and the reason `no-currency-bound-declared`", after
the scenario's "presents them only through the same outside-slot named
disclosure, carrying that count and the stated reason". B10 adds an
aggregate fixture that keeps its own judged freshness.

**R3 — Per-freshness counts do not exist. Taken.**

- Re-derived at `29e036f4`. `ReasonCounts` holds only `primary` and
  `secondary` (`packages/three-surface-poc-core/src/project-shape-model.ts`
  lines 176–179).
- The only aggregates that render counts are the class aggregates and the
  whole-shape claim. Both go through `reasonCountsBlock`
  (`apps/three-surface-poc/src/polaris.ts` lines 371–386, called at 762
  and 1214).
- **Decision: slice 5 builds per-freshness counts.** It adds one core
  mechanism counting each of the four freshness values plus the arm, on
  those two aggregate families, over the populations their reason counts
  already use.
- Per-label and per-tier counts are not built.
- The RFC6-17.r1 row is corrected: built behavior, Unknown, and
  "Excluded: per-label and per-tier aggregate counts".
- The ledger's consumer table gains rows for `ReasonCounts` and
  `countReasons`/`classAggregate`, and for `reasonCountsBlock` and its two
  call sites.

**R4 — Tier result. Taken.**

- B4 now states the tier result for both arms. An Observed `report-fact`
  claim that becomes Unknown renders untiered, which RFC2-25 allows ("an
  untier'd claim renders at its bare label", `rendering-vocabularies.md`
  line 172, RFC-0002). A claim already Unknown keeps `suspended` or no tier.
- "Retains its tier" is read as keeping any tier that RFC2-25 allows on an
  Unknown. That reading is labelled `[Inferred]` and tied to row
  RFC2-25.r1, which is `covered:PWB-REQ-007`.
- B10 adds two checks: no Unknown carries `report-fact`, and `suspended`
  survives both arms. The new "further rows" paragraph names RFC2-25.r1.

**R5 — The reply points at bytes that will change. Taken.**

- The question now says "built exactly as B1–B11 of the packet … describe,
  at the commit its clearing review names".
- The planned record now quotes B1–B11, the gap table and O1 verbatim from
  this file at the reviewed commit. It names the reviewed commit and the
  retained raw as provenance only, with no digest argument, so bead
  criterion 5 still holds. It cites the retention-posture precedent's "the
  direction text as issued"
  (`POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DECISION-PACKET.md`
  line 589, verified).
- The packet's "Review" section now points to this sibling record and says
  later raws and dispositions never go into the packet. The brief's closing
  line says the same.

**R6 — O1 framing. Taken.**

- O1 now quotes the design evidence for (ii): the funnel's "(the source's
  committer instant)" (`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`
  line 650) and "the classes genuinely differ" (lines 703–704), both
  verified.
- The unlabelled "many more claims render Unknown" is replaced by an
  `[Inferred]` statement that more claims would likely go `stale`, and that
  it is not measured. The ledger is matched.
- (ii)'s authority cost is stated. A per-source history read is a new
  observation, and the packet's Bounds (which now name "Git history read")
  and its escalation trigger bar it. (ii) therefore needs an owner decision
  that admits the read, reviewed on its own, before any packet can offer
  it.
- The 2026-10-15 autonomy reading is cited
  (`OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md` lines
  124–130, verified). The lead may choose (i), and it is shown to you so
  you can refuse it.

## Notes

**N1 — Ineffective registry act and not-evaluated claims. Taken.**

B4 has two new limbs:

- **Refused and failed evaluations.** A refused (`not-admitted`) or failed
  (`observation-failed`) evaluation is identified, so its whole-shape claim
  is judged.
  - With the registry act ineffective, `no-currency-bound-declared`
    displaces the gate's reason as primary. The gate's reason is kept as a
    secondary, beside the RFC2-9 contradiction route. This is labelled
    `[Inferred]`, as compelled by the scenario's WHEN.
  - With the act effective but no evidence instant, the `unreadable-instant`
    basis applies.
- **Not-evaluated shape.** It has no identified evaluation, so it falls
  outside the scenario `[Inferred]`. The judge is not called and no arm
  marker is set. Polaris's existing not-evaluated statement
  (`apps/three-surface-poc/src/polaris.ts` lines 784–785) is the fact of
  the render.

Repairing this note exposed a related defect, which is also fixed. The
existing `freshness-absence` span (`polaris.ts` lines 348–350) says
"Currency bound not declared" for any Unknown without freshness. B4 now
keys the disclosure to a named arm marker, not to an absent freshness
value, so the not-evaluated claim does not reach it. The ledger's
`claimTuple` row says so.

B10 adds both fixtures. The model lines checked were 379–390, 495–502 and
694–706 at `29e036f4`.

**N2 — Two gates, one reply; "sign-off and act". Taken.**

- "Answering both with one reply" is now labelled `[Inferred]` as the
  drafter's reading, with the option to decline.
- The gate table's Q7a row is now titled "sign-off and act". It says that
  under Scope A the version-tagged sign-off is that act, citing the Scope A
  direction item 1 and the sign-off record line 25 ("no phrase or digest
  argument exists", verified).

**N3 — Successor records unnamed in the question. Taken.**

The question now names
`PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`,
`PWB-OBSERVER-REGISTRY-MACHINE-CEILING-ACT.md` (by full path) and the tag
`pwb-missing-currency-disclosure-scenario-v1.0`.

**N4 — Wording tensions. Taken.**

- The banner now reads "until you give that exact line yourself, in your
  own session", which no longer suggests that other wording counts.
- The record section now says the coordinator may close the gate bead once
  the record exists. It adds: "The bead closing is bookkeeping: it is your
  reply, recorded, that continues anything."

**N5 — Continuation-form sweep missed the slash run. Taken.**

- The broad pattern `dov\.19\b|(?<![\w.])\.19\b(?!\.\d)` was re-run with
  Python `re` over `git ls-files -z` of a clone checked out at `29e036f4`.
  The denominator is 2,939 tracked files with 4 PNG decode skips. The
  result is 16 files and 31 occurrences.
- That is the 14 files already listed plus
  `pwb-missing-currency-disclosure-scenario/REVIEW-BRIEF.md` (line 88) and
  `docs/pursuits/2026-09-22-vision-pursuit-harvest.json` (seven).
- The ledger table gains that row and the two files. "None of these
  fourteen" becomes "sixteen".

**N6 — "Four test files" wrong. Taken.**

`git grep -n currencyBounds 29e036f4 -- apps packages` finds:

- the literal `currencyBounds: []` in `production-reobserve.test.ts`:43,
  `reobserve-session.test.ts`:32 and the fixture module
  `test-model-fixture.ts`:218;
- the assertion `toEqual([])` in `polaris-parity-sweep.test.ts`:627.

The ledger row now names those three files and gives the parity-sweep
assertion its own row.

**N7 — RFC2-9 provenance and RFC2-10.r1. Taken.**

- B6 now says, `[Inferred]`, that the authority line satisfies RFC2-9's
  "with its exact provenance state rendered"
  (`snapshot-and-evaluation-core.md` lines 230–231, RFC-0002). That line
  renders each authority's state, the registry among them, and its
  disclosure (`polaris.ts` lines 850–861), and the authority kinds are
  `consent`, `policy` and `registry` (`body-read-authority.ts` line 47).
- A new paragraph names RFC2-10.r1, which is already `unknown-uncovered`
  (`CONTRACT-COVERAGE-REPAIR-DELTA.md` line 48), together with RFC2-9.r1
  and RFC2-25.r1.

**N8 — Which limit stops the lane; machine size. Taken.**

- B10 now says the 2,097,152-byte ceiling is the hard limit, and a breach
  serves nothing.
- Crossing the 1,650,000-byte working target also stops the lane. This is
  `[Inferred]`, the drafter's choice, because the 2026-10-02 lane B
  direction sets that target as the margin for pending Butlers repairs.
- The machine answer is measured against `maxMachineResponseBytes`
  (16,777,216; registry entry line 271 at `29e036f4`), and a breach stops
  the lane too.

**N9 — B2's unmatched-id rule unlabelled. Taken.**

The rule is now labelled `[Inferred]` as the drafter's composition of
`undeclaredClass` with the naming by full claim id in
`claimClassAssignment`.

## What this round leaves for the owner

`[Inferred]` No repair needs an owner choice of substance beyond the reply.
Five drafter's choices are now in the bytes the owner would answer, each
labelled:

- B11's coverage of the two waiting lanes;
- B5's per-freshness counts;
- B4's tier and refused-claim results;
- B4's treatment of the not-evaluated shape;
- the working-target stop.

Declining the reply declines all five.
