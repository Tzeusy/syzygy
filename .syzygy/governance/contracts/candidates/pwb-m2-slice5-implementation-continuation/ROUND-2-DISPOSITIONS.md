# Round-2 dispositions — PWB M2 slice 5 continuation packet

> **Candidate — binds nothing.** This record dispositions one review round.
> It performs no act and authorizes nothing. It sits beside the packet so
> that the packet itself never carries review history.

- Raw: `docs/reviews/R-PWB-M2-SLICE5-CONTINUATION-PACKET-2-RAW.md`,
  retained byte-for-byte (CC-REV-6).
- Reviewed commit: `04e86895902ef1d3f9a1d6df19f976f08aef9f1d`. The branch
  was later rebased onto `main` at `fdc866af`. The rebased commit
  `d7b2d7e5` carries the same package, raw and README bytes:
  `git diff 04e86895 d7b2d7e5` over `.syzygy`, `docs/reviews` and
  `docs/README.md` is empty. The reviewed commit is kept as provenance
  only.
- Verdict, copied from raw line 4: `REVISE`.
- Findings: one repairable (1) and seven notes (2–8). The raw names no
  owner-only decision beyond the reply itself (raw lines 97–99).

"Packet", "ledger" and "brief" are the three files of the same names in
this directory. Every bead state and line below was re-read at the commit
named, not copied from the raw.

## Repairable finding

**1 — `syzygy-dov.19` also blocks `syzygy-dov.5.2`. Taken.**

- Re-read with the read-only `bd show syzygy-dov.5.2` on 2026-10-21. Its
  dependencies are `syzygy-dov.18` (closed), `syzygy-dov.19` (in
  progress), `syzygy-dov.22` (closed) and `syzygy-dov.5.1` (closed). So
  `syzygy-dov.19` is its last open blocker.
- The packet's record section gains the paragraph "The briefing-route
  bead". It says:
  - closing `syzygy-dov.19` would make that bead show as ready;
  - nothing authorizes the route: B9, the exclusions, the machine-view
    act's sentence and PR #489's Bounds all keep it unbuilt;
  - the coordinator holds `syzygy-dov.5.2`, by a dependency or a gating
    note, before closing `syzygy-dov.19`;
  - the record does not lift the 2026-09-30 read-gate bar on
    `maxBriefingResponseBytes`, which "remains gated on `syzygy-dov.19`
    and the further gates the 2026-09-21 rulings name" (quote verified in
    `OWNER-INSTRUCTIONS-2026-09-29-30-READABILITY-AND-REGISTRY.md`).
- "Nothing else is unblocked" is now "Nothing else is authorized", which
  is true even though the bead graph would show `syzygy-dov.5.2` as ready.
- The stale "wait for the machine-view package (`syzygy-dov.22`) and M5
  slice 3" is corrected in the packet's exclusions, and the ledger's
  matching interaction row is rewritten. Both now say the route waits for
  its own separate authorization. They quote the machine-view act ("the
  briefing member stays unservable until its ceiling is declared and the
  route is separately authorized", `PWB-MACHINE-VIEW-AMENDMENT-ACT.md`
  lines 86–88, verified).
- I checked before editing the ledger: no `*MANIFEST*`, `.txt`, `.yaml`,
  `.json` or `scripts/` file names this package (`git grep -l -F`, 0
  files), so no manifest row binds it.
- The question now says the reply authorizes no briefing route although
  `syzygy-dov.19` is that bead's last blocker. Brief criterion 15 asks the
  next round to check all of this.
- Note 5's rewording is folded in (below).

## Notes

**2 — B11 releases more than slice 5, and the reply is bundled. Taken as
a disclosure; B11 is kept.**

- The question now says that, once the owner confirms the 2026-10-20
  direction drafted in PR #489, "this reply is what releases those two
  uses, and it is one reply: slice 5 cannot be given without them".
- **The departure from bead criterion 6 is recorded here.** That criterion
  asks the record to identify "only M2 slice 5 as unblocked". With B11
  the reply also releases item depth's relation claims (`syzygy-dov.14.4`)
  and the opening band's count arm (`syzygy-dov.4.2`), conditional on
  PR #489's confirmation. Those beads are related to slice 5 through
  PR #489, not unrelated work, so criterion 6's purpose holds and its
  wording does not. Criterion 6 is not met literally and must not later be
  read as met.
- B11 is not split into a separate offered line. `[Inferred]` The
  2026-10-20 answer selected item depth, the opening band and
  missing-currency together, and a second line would add a second owner
  question to the batch for one mechanism. The owner who wants slice 5
  without B11 can decline and say so.

**3 — Routing gaps: the not-evaluated shape, RFC1-18.r2 and RFC6-14.r2.
Taken.**

- The RFC6-14.r1, RFC7-16.r1 and RFC7-33.r1 rows' "What stays Unknown"
  cells now name the not-evaluated shape's claim beside the arm.
- "Three further rows" becomes "Five further rows". It adds:
  - RFC1-18.r2 (`unknown-uncovered`, `CONTRACT-COVERAGE-REPAIR-DELTA.md`
    line 42). RFC1-18 lists "freshness state" among an evaluation
    instance's fields (`RFC-0001-project-graph-identity-state-planes.md`
    line 407, verified).
  - RFC6-14.r2 (`covered:PWB-REQ-007`, line 52). The aggregate's own
    judged freshness is read `[Inferred]` as the tuple it already carries
    as a claim, not a headline status.

**4 — "The only two" is not the whole population. Taken.**

- B5 now says "the two aggregate claims that render reason counts today".
- It names the gap list (`gapReasonCounts` and `gapsList`, `polaris.ts`
  lines 1070–1105, rendered at 1192 and 1239, verified) as a third
  reason-count site that gets no freshness counts. A claim in the arm
  reaches it as a primary-reason count with its route.
- The ledger's consumer table gains the gap-list row, which also cites
  line 1815.

**5 — The Review section would be false once these bytes clear. Taken.**

The packet's Review section now says only what stays true before and
after any round:

- rounds, raws and dispositions live in sibling records;
- the first raw is named;
- the brief names the round that reviews these bytes;
- the reply is offered only once a round has cleared them.

**6 — B4's refused-for-consent-or-policy case. Taken.**

- B4's refused-evaluation limb now says, `[Inferred]`, that an evaluation
  refused for consent or policy with the registry act still effective
  renders the whole-shape claim `stale` on the `unreadable-instant` basis,
  with the gate's reason still primary. The drafter accepts this rather
  than take a freshness value from somewhere other than the judge.
- B10 adds a consent-refused fixture with an effective registry act.
- The ledger's effects list the result. The three authority kinds were
  re-read as `consent`, `policy` and `registry` (`body-read-authority.ts`
  line 47).

**7 — How the zero `broken` and `superseded` counts render. Taken.**

- B5 now says, `[Inferred]`, that the judge never returns those two
  values. Their counts therefore render with the same unreachable marker
  and reason that B7 keeps on the legend, never as a bare `0`.
- A zero count of `fresh` or `stale` renders as `0`.
- B7 says the same, and B10 adds the check.

**8 — O1: the lead may decide (i); (ii) is the owner's. No change.**

The reviewer confirms reading (i) is lawful and fairly presented, and
raises no finding. Reading (ii) stays the owner's: the packet already says
it cannot be offered without an owner decision admitting a Git history
read.

## What this round leaves for the owner

`[Inferred]` No repair needs an owner choice of substance beyond the reply.
Round 1's five drafter's choices stand. This round adds two, both labelled:

- the consent-refused `stale` result;
- the marker on unreachable counts.

It also discloses B11's bundling in the question itself. The briefing-route
hold is the coordinator's bead step, not the owner's.
