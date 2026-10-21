<!-- Owner direction, recorded verbatim. Never edit below the line.
     Act family: implementation authorization (same family as
     decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md and
     decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md, which it
     continues, and decisions/OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md).
     Offering: the candidate package
     contracts/candidates/pwb-m2-slice5-implementation-continuation/, cleared
     at commit 78d18444 by its round-3 review.
     Direction given 2026-10-21 by the owner; recorded 2026-10-21 on branch
     agent/syzygy-dov.19, rebased onto origin/main fe20dd5f.
     Gate bead: syzygy-dov.19. It is a plain owner direction in the sense of
     PROCESS-GLOSSARY.md, not a digest-bound act: it binds no artifact
     bytes, needs no manifest or recorder script, adds no row to the
     acceptance-act record and registers nothing in check_governance.py.
     The owner's words are quoted byte-for-byte; the scope reading that
     follows them is the recorder's and is labelled as such. -->

# OWNER DIRECTION — CONTINUATION OF PWB IMPLEMENTATION AUTHORIZATION FOR M2 SLICE 5

Date: 2026-10-21
Owner: Tzeusy
Repository state at recording: branch `agent/syzygy-dov.19`, rebased onto
`origin/main` at `fe20dd5f`
Continues: `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`
(2026-09-05), which continues `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`
(2026-09-02), both in this directory
Gate bead: `syzygy-dov.19`; implementation bead it unblocks:
`syzygy-dov.2.2` (M2 slice 5)
Offering: `.syzygy/governance/contracts/candidates/pwb-m2-slice5-implementation-continuation/OWNER-DECISION-PACKET.md`
at commit `78d18444`, which stays the question and is not edited

## Why a continuation was needed

`[Observed]` The 2026-09-05 continuation stops implementation at its
escalation triggers, among them "a further amendment to the signed PWB
specification beyond the 2026-09-05 package" and "a change to the
constraints or envelope the 2026-09-05 registry entry declares". M2 slice 5
crosses both: it consumes the per-class currency bounds the 2026-09-30
registry act added
(`PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`, this
directory), and it implements the missing-currency scenario signed v1.0 on
2026-10-02 (`PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0.md`,
this directory). The packet's section "Why a continuation is needed at
all" quotes the three records that say a separate continuation is owed.

`[Observed]` The 2026-09-21 P-69 ruling
(`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, this directory)
prepared the gates slice 5 waits for, a registry-entry amendment act, a
continuation act, P-68's ruling and the Q7a scenario's sign-off and act. It
did not perform the continuation. Nothing before the reply below continued
anything for slice 5: not that ruling, not the 2026-10-20 questionnaire
answer that selected "missing-currency", not the packet, its reviews or any
commit.

## Verification before recording

`[Observed]` The packet's readback of the predecessor gates (its section
"The predecessor gates, read back at `29e036f4`", method in the package's
`IMPACT-LEDGER.md` section "Readback of the predecessor gates") was re-run
by script at the recording head, over the tree and the named tags:

| Gate | Readback at recording |
|---|---|
| P-68 (`syzygy-dov.17`) | Ruled 2026-09-21, then lane B declined 2026-10-02 (`POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md`, this directory); no M2 spec package waits on it |
| Registry-entry act (`syzygy-dov.18`) | The registry entry's `currencyBounds` (13 rows) and `currencyBoundSemantics` (7 keys) parse equal at the tags `pwb-adopt-registry-entry-signed-2026-09-30`, `pwb-adopt-registry-entry-signed-2026-10-02` and `pwb-registry-machine-ceiling-amendment-v1.0` and in the tree; each tag's entry bytes hash to the argument its own act record names, and the tree's to the argument of `PWB-OBSERVER-REGISTRY-MACHINE-CEILING-ACT.md` (this directory), the registry act `apps/three-surface-poc/src/governance-inputs.ts` names as current |
| Q7a scenario (`syzygy-dov.20`) | The heading "No effective currency bound is disclosed outside freshness" occurs once in the PWB `spec.md` at the tag `pwb-missing-currency-disclosure-scenario-v1.0` and once in the tree, and its block is byte-identical between them |
| Continuation (`syzygy-dov.19`) | Given by the reply below |

`[Observed]` The packet at the recording head is byte-identical to the
packet at `78d18444`, compared by script. Its review history: round 1
`REVISE` over `268f1773`
(`docs/reviews/R-PWB-M2-SLICE5-CONTINUATION-PACKET-RAW.md`), round 2
`REVISE` over `04e86895`
(`docs/reviews/R-PWB-M2-SLICE5-CONTINUATION-PACKET-2-RAW.md`), and round 3
`CONFIRM WITH EXCEPTIONS` over `78d18444`, notes only
(`docs/reviews/R-PWB-M2-SLICE5-CONTINUATION-PACKET-3-RAW.md`, verdict at
line 4), which cleared those bytes under the owner's notes-only stopping
rule (`POLARIS-GATE-SITTING-2026-09-26-DECISION.md`, this directory). The
round-3 notes are dispositioned in the package's `ROUND-3-DISPOSITIONS.md`,
never in the packet. The commit and the raw are named here as provenance
only; this record carries no digest argument.

## The exchange, verbatim

The packet's question, quoted exactly from the packet at `78d18444` (its
section "The question", lines 98–128):

> **Continue PWB implementation authorization for M2 slice 5?** The
> 2026-09-05 continuation stops at registry and signed-spec changes. The
> 2026-09-30 registry act
> (`.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`,
> the currency bounds), read through its 2026-10-20 successor
> (`.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-MACHINE-CEILING-ACT.md`),
> and the missing-currency scenario v1.0 (tag
> `pwb-missing-currency-disclosure-scenario-v1.0`, signed 2026-10-02)
> changed exactly those. Do you continue implementation authorization so
> that M2 slice 5 (`syzygy-dov.2.2`) is built exactly as B1–B11 of the
> packet
> `.syzygy/governance/contracts/candidates/pwb-m2-slice5-implementation-continuation/OWNER-DECISION-PACKET.md`
> describe, at the commit its clearing review names: reading (i) of
> `measuredFrom`; its five contract-coverage gaps routed as it states (each
> stays `unknown-uncovered`); and the scenario's disclosure used by item
> depth's relation claims (`syzygy-dov.14.4`) and by the opening band's
> count (`syzygy-dov.4.2`) only as B11 states, authorizing no other part of
> those lanes. Once you confirm the 2026-10-20 direction drafted in PR
> #489, this reply is what releases those two uses, and it is one reply:
> slice 5 cannot be given without them. It authorizes no briefing route
> (`syzygy-dov.5.2`) and leaves `maxBriefingResponseBytes` unread, although
> `syzygy-dov.19` is that bead's last open blocker too. All of it for the
> one configured Butlers repository and
> content class `declared-project-shape-text`, with every original
> exclusion retained: no release, deployment, Butlers write, second
> repository, wider content class, consent amendment, egress,
> observed-code execution, recovery, mission, autonomy or multi-user
> authority?
>
> Reply with the exact line below to grant it. Any other wording, or
> silence, continues nothing.

The owner replied, in full:

> Continue PWB implementation authorization for M2 slice 5 as drafted

`[Observed]` The reply is byte-identical to the packet's offered line
(line 133 at `78d18444`). It was given by the owner directly, as a single
line with no other text, in the owner's own Claude Code lead session (local
session `49123ca9-8529-48cf-8e46-2ac45afbd82a`), at about
2026-10-21T12:00:00Z, the UTC instant `date -u` gave at receipt, after
round 3 had cleared the packet at `78d18444`. The recording session did not
witness the exchange: the reply and its instant reach this record as the
lead session relayed them, and as the lead's comment of 2026-10-21 12:00 on
bead `syzygy-dov.19` states them. `[Unknown]` Whether the lead session
displayed the question to the owner in exactly the packet's words, or
offered the packet by reference.

## The exact built behavior, as answered

The packet's sections that the reply answers, copied byte-for-byte from the
packet at `78d18444`, so that this record holds the bytes the owner
answered and does not depend on the packet staying unedited. Each block
below is the named line range of that file, unchanged; in them, "you" is
the owner and "this packet" is the offering named above.

### B1–B11 (section "The exact built behavior", lines 153–406)

````markdown
What the reply would authorize, and nothing beyond it. "The registry entry"
is `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`;
"the scenario" is PWB-REQ-007's "No effective currency bound is disclosed
outside freshness", as signed in v1.0; "the arm" is the condition that
scenario names, a claim whose class has no currency-bound declaration with
effective owner-act provenance at the evaluation's as-of instant.

- **B1 — Where the bounds come from.** The implementation reads
  `currencyBounds` and `currencyBoundSemantics` from the registry entry
  bytes whose `adopt-registry-entry` act the PWB-REQ-005 body-read gate
  evaluates as effective for that evaluation, and from nowhere else: no
  constant, default, fallback or nearest-class bound. When that act is not
  effective, no bound is effective. A later superseding registry act that
  leaves both fields byte-identical needs no further continuation; one that
  changes either field is again a registry escalation trigger.
  `maxBriefingResponseBytes` stays unread (B9).
- **B2 — Which row governs a claim.** Each project-shape claim is assigned
  a row by its full claim id under `claimClassAssignment`, through a closed
  table of the claim-id families that sentence names, each matched against
  the whole id and never against a prefix of it. A claim whose class the
  signed specification names directly takes that class's row or none:
  PWB-REQ-015's relation claims belong to the class
  `governing-intent-relation`, which has no row, so they are in the arm
  whatever item identity their id embeds, and never take an item's row
  (B11). A claim id that matches no family is in the arm too; it is never
  given a default or nearest class. `[Inferred]` That last rule is the
  drafter's composition of `undeclaredClass`, which speaks of "a claim
  whose class has no row here", with the naming by full claim id in
  `claimClassAssignment`. The currency probe (`claim:currency-probe`,
  slice 2) is outside these bounds, as `outsideTheseBounds` says: it is not
  judged, gains no freshness and is not in the arm.
- **B3 — What age is measured.** Evidence age runs from the committer
  instant of the evaluated revision, which the model already carries as
  the revision's source-claimed instant, to the evaluation's own as-of
  instant (the observation instant), never to a wall clock. `[Inferred]`
  This is the drafter's reading of `measuredFrom`, "the committer instant
  of the exact Git object the declaration was extracted from": only a
  commit carries a committer instant, and the one commit an extraction
  reads through is the evaluated revision. It reads no new Git object.
  Where the model carries no evaluated-revision instant (a refused or
  failed evaluation), the judge is given no readable instant (B4). The
  alternative reading is option O1 below; this reply does not choose it.
- **B4 — The judge.** `assessCurrency` is imported from
  `packages/cap1-core` unchanged and called once per assigned claim of an
  identified evaluation with its class, its evidence instant, the effective
  rows and the as-of instant. The model's `fresh` constant and the comment
  arguing that "the evaluation itself is the currency" are removed; no code
  path sets a freshness value except from the judge. Its arms map as
  follows:
  - `current`: freshness `fresh`; label, tier and reasons as otherwise
    derived.
  - `stale`, on any of its three bases (`age-exceeds-bound`,
    `unreadable-instant`, `future-dated-instant`): freshness `stale` and
    reason `stale-beyond-currency-bound`, with the basis carried
    machine-readably, as the entry's `outOfBoundResult` requires. An
    Observed claim becomes Unknown with that primary reason and renders
    untiered: its `report-fact` tier sits inside the Observed label only
    (RFC2-25), so it never travels on an Unknown, and RFC2-25 lets an
    untiered claim render at its bare label. A claim already Unknown keeps
    its primary reason and its tier (`suspended` or none) and gains
    `stale-beyond-currency-bound` as a secondary. `[Inferred]` Both the
    reason precedence and the tier result are the drafter's composition;
    RFC2-24 states no precedence.
  - `no-bound-declared`, and every claim B1 or B2 places in the arm: the
    scenario, exactly. The claim renders Unknown with primary reason
    `no-currency-bound-declared` and the route
    `Declare the bound in quality policy`. Any reason it would otherwise
    carry is kept as a secondary, never dropped, except where the signed
    text says otherwise: a PWB-REQ-015 relation claim reports no second
    primary reason and never reports `missing-declaration` in that state
    (B11). It retains its challenge state, semantic claim identity and
    evaluation identity. `[Inferred]` The scenario says it "retains its
    tier"; the drafter reads that as keeping any tier RFC2-25 allows on an
    Unknown (`suspended`), while a claim that would otherwise be Observed
    with `report-fact` renders untiered, as in the stale arm, because
    keeping `report-fact` on an Unknown would break RFC2-25, whose row
    RFC2-25.r1 is `covered:PWB-REQ-007`. It carries **no freshness
    value**: the field is absent from the model and the machine answer, and
    the human tuple has no freshness attribute. Instead the model marks the
    claim as in the arm by a named field, and that field, never an absent
    freshness value, is what renders the missing bound as a named,
    expandable fact outside the freshness slot. Where a declaration is
    present but its act is not effective, the RFC2-9 contradiction route to
    the owner renders beside the Declare route, and neither replaces the
    other. No fifth freshness value, no `null` spelled as a value, and no
    sentinel string is minted.
  - **Refused and failed evaluations.** A refused (`not-admitted`) or
    failed (`observation-failed`) evaluation is still an identified
    evaluation with an as-of instant, so its whole-shape claim is judged
    like any other. When the registry act is not effective, no row is
    effective (B1) and the claim is in the arm:
    `no-currency-bound-declared` becomes its primary reason and the gate's
    own reason is kept as a secondary with its route, beside the RFC2-9
    contradiction route where a declaration is present. `[Inferred]` The
    scenario's WHEN compels that displacement, and the drafter does not
    exempt gate refusals from it. When the act is effective but the model
    carries no evidence instant, the judge's `unreadable-instant` basis
    applies: the claim keeps its primary reason, gains
    `stale-beyond-currency-bound` as a secondary and carries freshness
    `stale`. `[Inferred]` So an evaluation refused for consent or policy,
    with the registry act still effective, renders its whole-shape claim
    `stale` about evidence that was never read. The gate's reason stays
    primary, and the stale basis says only that no evidence instant could
    be read; the drafter accepts this result of B3 and the judge rather
    than exempting the claim, which would need a freshness value from
    somewhere other than the judge.
  - **No evaluation.** The not-evaluated shape (evaluation id
    `evaluation:not-evaluated`) has no identified evaluation and no as-of
    instant. `[Inferred]` The scenario's WHEN has nothing to be read at,
    so the judge is not called: the claim keeps its one reason
    `unconsented-source-or-provider`, carries no freshness value and no
    arm marker, and the not-evaluated statement Polaris already renders
    (`apps/three-surface-poc/src/polaris.ts` lines 784–785) is the fact of
    the render that says why (RFC2-10).
- **B5 — Aggregates.** One mechanism in the core package counts an
  aggregate's members by freshness: one count for each of `fresh`,
  `stale`, `broken` and `superseded` and, apart from them, the count of
  members in the arm, so that these counts together equal the membership.
  Slice 5 builds it and uses it on the two aggregate claims that render
  reason counts today, each over the member population its reason counts
  already use [Observed: `apps/three-surface-poc/src/polaris.ts` lines 762
  and 1214]:
  - each class aggregate `claim:class:<class>`, over its members, its
    declaring sources and the undiscovered-member entries that its reason
    count already takes from the aggregate's own claim
    (`packages/three-surface-poc-core/src/project-shape-model.ts` lines
    456–460);
  - the whole-shape claim `claim:project-shape`, over the population its
    reason-count block is taken over.

  `[Observed]` A third site renders reason counts: the gap list
  (`gapReasonCounts` and `gapsList`, `polaris.ts` lines 1070–1105, rendered
  at 1192 and 1239). It is a list over every shape claim, not an aggregate
  claim, so it gains no freshness counts. A claim in the arm reaches it
  as a primary-reason count of `no-currency-bound-declared` with its route,
  as the scenario's "omits its primary reason count or hides its route"
  limb requires.

  `[Inferred]` The judge never returns `broken` or `superseded`, so their
  counts can only be zero. Each of them renders with the same unreachable
  marker and reason that B7 keeps on the legend, never as a bare `0`, so
  that no reader takes an unreachable value for a checked zero. A zero
  count of `fresh` or `stale`, which the judge can return, renders as `0`.

  Members in the arm are presented only through the same outside-slot
  named disclosure, carrying their count and the reason
  `no-currency-bound-declared`, never as a freshness value and never as
  zero; their primary-reason count and route stay visible in the existing
  reason counts. No aggregate folds an Unknown into a favourable total.
  Per-label and per-tier counts are not built: no PWB aggregate carries
  them today, and slice 5 adds none.

  **An aggregate's own freshness.** Both families above are claims with a
  row of their own (each class's row, and `project-shape`), so each takes
  its own freshness from the judge under B4, over its own row and the
  evaluation's evidence instant, and never from its members. `[Inferred]`
  The scenario forbids deriving a freshness value from the other members
  and presenting the unbounded members as a freshness value of the
  aggregate's own; it does not forbid the aggregate's own judged value.
  When the aggregate's own row is not effective, it is itself in the arm.
  An aggregate with no row of its own (none exists today; the opening band
  would be one, B11) carries no freshness value while it has a member in
  the arm, because any value would be derived from its other members.
- **B6 — Both channels, identically.** The human page and the machine
  answers carry the same tuple, the same arm marker and outside-slot
  disclosure for each claim, and the same freshness and arm counts for
  each aggregate; the PWB-REQ-020 parity sweep covers the disclosure and
  the counts as their own families. The machine evidence block's
  `currencyBounds`, empty until now, carries the effective rows exactly as
  declared. `[Inferred]` Their owner-act provenance state is the registry
  authority's state and disclosure sentence, which the authority line
  already renders (`apps/three-surface-poc/src/polaris.ts` lines 850–861)
  and the machine answer already carries; the drafter reads that as
  RFC2-9's "with its exact provenance state rendered", so slice 5 adds no
  second rendering.
- **B7 — The legend stays true.** The slice-1 copy oracle keeps every
  freshness legend sentence either reachable or marked unreachable with its
  reason; a value that slice 5 makes reachable (such as `stale`) loses its
  marker without a separate copy edit. The aggregate counts of a value
  that is still unreachable carry the same marker (B5).
- **B8 — Determinism.** One identified evaluation served twice is
  byte-identical. No timer, poller or watcher is added; a new judgment
  happens only through a new identified evaluation, which stays
  human-triggered.
- **B9 — Not consumed.** `maxBriefingResponseBytes` and
  `governingBehaviorContract` stay unread. No briefing route is served.
- **B10 — How it is shown to work.** Every falsifier limb of the scenario
  and of B1–B9 and B11 has a test whose expected values are literals
  independent of the module under test, and a rule-6 mutant that makes it
  fail, with the mutant's old and new fragments and its commit recorded.
  Fixtures reach every judge arm through the PWB model, at least:
  - an out-of-bound class that renders `stale` at least once;
  - an unassigned claim id, and an id that embeds an assigned family's
    prefix without matching its whole pattern;
  - a synthetic claim of a class with no row, such as
    `governing-intent-relation`, with and without other reasons;
  - an ineffective registry act, on which the refused whole-shape claim
    carries `no-currency-bound-declared` as primary and the gate's reason
    as a secondary;
  - an evaluation refused for consent with the registry act effective, on
    which the whole-shape claim keeps the gate's reason as primary and
    carries `stale` on the `unreadable-instant` basis;
  - the not-evaluated shape, with no judge call and no arm disclosure;
  - `broken` and `superseded` counts rendering with the unreachable
    marker, never as `0`;
  - a class aggregate and the whole-shape claim with members in the arm,
    whose freshness counts and arm count sum to the membership while the
    aggregate keeps its own judged freshness;
  - no Unknown claim carrying `report-fact`, and `suspended` surviving
    both arms.

  The number of claims in each arm at a live evaluation is measured and
  recorded with its subject and digest (rule 11), never assumed. `/polaris`
  is measured on both host forms. The 2,097,152-byte response ceiling is
  the hard limit, and a breach serves nothing. `[Inferred]` Crossing the
  1,650,000-byte working target on either host form also stops the lane
  and returns to you, because that target is the margin you set for
  pending Butlers repairs; this is the drafter's choice. The machine
  answer is measured against `maxMachineResponseBytes` (16,777,216 bytes)
  and a breach stops the lane too. No limit is ever met by omitting a
  disclosure.
- **B11 — The two lanes that wait for this act.** `[Observed]` The
  2026-10-20 direction drafted in PR #489 (head `8c334f67`) makes every
  use of the scenario's disclosure in item depth (`syzygy-dov.14.4`) and
  in the opening band (`syzygy-dov.4.2`) wait for this act and lets each
  be built "only as far as the behaviour that act names". The behavior
  named here covers both, as follows, and nothing else in either lane:
  - **Item depth's relation claims.** Each relation claim is in the arm
    through B2 and is judged by B4's no-bound arm, with PWB-REQ-015's own
    composition in place of B4's secondary rule: the single primary
    reason `no-currency-bound-declared`, its route and the outside-slot
    disclosure, no second primary reason, and no `missing-declaration`
    reported in that state. Its tier follows B4. Slice 5 builds no
    relation claim, contract band or item detail; those are item depth's,
    under that lane's own authority.
  - **The opening band's count.** The band's count of members in the arm
    is B5's count over the band's members, rendered through B5's
    disclosure. The band has no row of its own, so B5's last sentence
    applies to it. Slice 5 builds no part of the band. If the band's own
    freshness disclosure cannot then be built without deriving a value from
    its members, that lane stops and returns to you.
  - **One mechanism.** Neither lane builds its own judge, arm marker or
    count. `[Inferred]` Each uses them only after slice 5 has landed, so
    the WIP-one chain needs slice 5 ahead of item depth and ahead of the
    band's count arm. The band itself may land earlier without the count,
    as that direction allows.

  If the 2026-10-20 direction is not confirmed, B11 authorizes nothing by
  itself: it says how the mechanism is used, and it authorizes neither
  lane.

Slice 5 changes the shared Three-Surface POC model, so it takes the
shared-model WIP-one slot in its turn; the coordinator orders it behind the
chain the 2026-10-15 direction fixes, and ahead of the B11 uses.
````

### The gap table (section "The five contract-coverage gaps, and how this routes them", lines 410–496)

````markdown
`[Observed]` The signed missing-currency amendment marked five rows of
`openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE-REPAIR-DELTA.md`
`unknown-uncovered`, because each asks for freshness on every claim and the
scenario's arm has none. That file is a signed subject. Making any row
`covered` again would need a further PWB amendment (CC-REV-2) or a contract
change, and **this packet asks for neither**. None of the five needs a
specification amendment to be *built*; each is routed, not closed.

Each consequence is quoted from its row in that file; each clause from its
definition site.

1. **RFC6-14.r1** — "Every project claim carries label, tier,
   primary/secondary reasons and freshness". RFC6-14 (Label parity) asks
   each claim instance in a machine answer to carry "the freshness state
   (RFC2-10)".
2. **RFC6-14.r3** — "Machine answers retain the complete epistemic tuple
   and never fold Unknown into totals". RFC6-14: "A machine answer never
   omits epistemic state".
3. **RFC6-17.r1** — "Aggregate composition retains label, tier, reason and
   freshness counts". RFC6-17 (Aggregation discloses) names
   "per-label, per-tier, per-Unknown-reason and per-freshness-state
   counts".
4. **RFC7-16.r1** — "Status is evaluation-bound and carries label, tier,
   reason and freshness with visible staleness". RFC7-16: every rendered
   status "carries the label + tier + reason + freshness vocabulary
   **verbatim** (RFC6-14)".
5. **RFC7-33.r1** — "Label, tier, reason and freshness travel identically
   in human and machine views". RFC7-33 lists "label + tier + reason +
   freshness" among the distinctions served identically to machines.

| Gap | What the build does (resolution: built behavior) | What stays Unknown (resolution: Unknown row) | Excluded |
|---|---|---|---|
| RFC6-14.r1 | Every claim carries label, tier where it has one, and primary and secondary reasons; every claim judged under an effective row carries one of the four freshness values from the judge (B4) | Freshness on the arm, which carries the outside-slot disclosure instead; freshness on the not-evaluated shape's one claim, which carries neither a value nor the arm disclosure, only the not-evaluated statement (B4) | Nothing |
| RFC6-14.r3 | The machine tuple equals the human tuple; the arm marker and disclosure are carried in the machine answer; no Unknown folds into a total (B4–B6) | Whether an absent freshness value plus the disclosure is "the complete epistemic tuple" | Nothing |
| RFC6-17.r1 | Each class aggregate and the whole-shape claim gain per-freshness-state counts plus the arm count, which together equal the membership; reason counts are unchanged (B5) | Whether the separate arm count meets "per-freshness-state counts" | Per-label and per-tier aggregate counts: none exists today and slice 5 builds none |
| RFC7-16.r1 | Each rendered status is kernel-judged at an identified evaluation; staleness (`stale`) is visible on the narrative page itself (B4, B8) | Freshness on the arm and on the not-evaluated shape's claim | Nothing |
| RFC7-33.r1 | The same attributes, disclosure and counts travel in both views, under the parity sweep (B6) | Freshness on the arm and on the not-evaluated shape's claim | Nothing |

`[Inferred]` RFC2-10 itself says "A condition genuinely outside the four is
disclosed as a fact of the render, never dressed as a freshness state",
and that sentence is what the scenario relies on. Whether it makes the arm
conform to the four rows above that ask for freshness is a reading of
accepted contracts. Verification rule 8 does not let an implementation
adopt it, so **the build claims no conformance on the arm**, and all five
rows stay `unknown-uncovered` in the signed matrix.

Five further rows that slice 5 newly reaches, none of them one of the
five gaps:

- **RFC2-25.r1** (`covered:PWB-REQ-007`): B4's tier result keeps
  `report-fact` off every Unknown, so the closed tier meanings hold.
- **RFC2-9.r1** (`covered:PWB-REQ-007`): B1 honours bounds only under an
  effective act, and B6 relies on the authority line for the provenance
  state.
- **RFC2-10.r1** (already `unknown-uncovered` before v1.0): slice 5 makes
  `fresh` and `stale` judged and deterministic (B4, B8). The arm, which
  carries no value, is still why the row is not claimed.
- **RFC1-18.r2** (already `unknown-uncovered`; "the complete accepted
  tuple"): RFC1-18 lists the freshness state among a claim instance's
  fields, and neither the arm nor the not-evaluated shape's claim carries
  one. Slice 5 claims nothing on it.
- **RFC6-14.r2** (`covered:PWB-REQ-007`; "Project aggregates carry no
  headline epistemic status of their own"): `[Inferred]` B5 gives the two
  aggregate claims their own judged freshness, which the drafter reads as
  the tuple each already carries as a claim, not a headline status; the
  aggregates gain no headline, maturity or success.

**Live members of the arm.** `[Inferred]` When slice 5 lands, with all
thirteen classes declared, every minted claim-id family assigned and the
registry act effective, the arm has no live member. It gains them in two
ways:

- once item depth lands, every relation claim is in the arm, one per
  contract band, until a bound for `governing-intent-relation` is
  declared by an owner act over the registry entry;
- whenever the registry act is not effective, every claim of that
  evaluation is in the arm, the refused whole-shape claim included.

B10 measures the arm at slice 5's landing; the item-depth lane measures
its own.

**The one choice of substance here is yours, and the reply makes it:**
whether to build across five accepted-contract consequences whose
conformance on one arm stays Unknown, an arm that item depth will fill.
The alternative is to wait for a contract reading or amendment first;
that is not offered here, and declining (the default) keeps the current
constant, which is itself a disclosed non-conformance to RFC2-9.
````

### O1 (section "Your option inside this packet", lines 500–533)

````markdown
**O1 — what `measuredFrom` measures.** B3 takes reading (i). Reading (ii)
is the other lawful reading, and you may prefer it.

| Reading | Age of a claim's evidence | Cost | Consequence |
|---|---|---|---|
| (i) **drafted** | as-of instant minus the evaluated revision's committer instant; one age for every claim of an evaluation, compared to each class's own bound | none: the instant is already captured | a declaration unchanged for years reads `fresh` while the observed revision is recent; a class goes stale only when the revision is older than its bound |
| (ii) | as-of instant minus the committer instant of the newest commit, at or before the evaluated revision, that changed the declaring source | a new Git history read per source (metadata, not body), a rule for merges, and an authority step beyond this packet (below) | each source ages separately, as the per-class values (four distinct, 30 to 365 days) suggest; `[Inferred]` a source's last change is usually older than the revision, so more claims would go `stale` on a live evaluation; how many is not measured |

`[Inferred]` Reading (i) is drafted because the claims are report facts
("the source declares X" at the evaluated revision), so the evidence
behind them is as old as the snapshot, and because it reads nothing new.
A blob has no committer instant, and the evaluated revision is the only
commit an extraction reads through, so (i) is arguably the more literal
reading of "the exact Git object the declaration was extracted from".

`[Observed]` The design points the other way in two places. The M2 funnel
designed the field as "what the bound is measured from (the source's
committer instant)"
(`docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` line 650). Its
rejected trade-off (a) refuses one bound for all classes because "the
classes genuinely differ" (lines 703–704), a difference that reading (i)
largely flattens.

**What (ii) would cost in authority.** Reading per-source Git history
beyond the evaluated revision is a new observation. This packet's Bounds
and its escalation trigger on "any observation outside the consented
content class or repository" bar it, as the 2026-09-05 continuation's
triggers do. So (ii) needs more than a revised packet: it needs an owner
decision that admits that history read, reviewed on its own, before any
packet could offer it. `[Inferred]` Under the 2026-10-15 standing autonomy
direction as applied, the lead may choose (i), because it reads nothing
new; it is shown to you here so that you can refuse it. If you prefer
(ii), do not give the reply: say so, and that decision is drafted first.
The reply above authorizes (i) only.
````

## What the recorder reads this as

`[Inferred]` The reply answers the one question put, so it is read as the
continuation of the 2026-09-05 continuation across its signed-spec and
registry escalation triggers for M2 slice 5, and nothing wider.
Concretely:

1. **M2 slice 5 is unblocked, and it alone.** `syzygy-dov.2.2` may be built
   exactly as B1–B11 above describe, under reading (i) of `measuredFrom`
   (B3; O1's reading (ii) is not chosen and stays unauthorized), with the
   five contract-coverage gaps routed as the gap table states, each row
   staying `unknown-uncovered` and no conformance claimed on the arm. It
   takes the shared-model WIP-one slot in its turn.
2. **The B11 uses are conditional, not unblocked.** B11 names how item
   depth's relation claims (`syzygy-dov.14.4`) and the opening band's count
   (`syzygy-dov.4.2`) use slice 5's mechanism. Those uses take effect only
   after the owner confirms the 2026-10-20 direction drafted in PR #489
   (head `8c334f67`, branch `agent/syzygy-sin5`), which at recording is
   open, unconfirmed and not on `main`, and is still pending in the owner's
   questionnaire. Until then this direction authorizes nothing in either
   lane, and B11's own last sentence says so. Even then it authorizes only
   those two uses, never the rest of either lane.
3. **The briefing route stays gated.** `syzygy-dov.19` is also the last
   open blocker of `syzygy-dov.5.2` (M5 slice 3, the briefing route), and
   this direction does not authorize that route: B9 keeps
   `maxBriefingResponseBytes` and `governingBehaviorContract` unread. The
   bead is held behind its own gate, `syzygy-bivj`. This record does not
   lift the 2026-09-30 read-gate direction's bar on
   `maxBriefingResponseBytes`
   (`OWNER-INSTRUCTIONS-2026-09-29-30-READABILITY-AND-REGISTRY.md`, this
   directory, "The direction, as issued"), which "remains gated on
   `syzygy-dov.19` and the further gates the 2026-09-21 rulings name"; for
   that field those further gates stay open. For the currency bounds and
   the currency semantics block, the bar is lifted only as far as B1–B11.
4. **Scope is otherwise unchanged from 2026-09-05.** The same one
   configured Butlers repository and content class
   `declared-project-shape-text`, the same ordinary implementation plane,
   and the same review, repair, confirm and owner-report cycle.

Closing `syzygy-dov.19` is the coordinator's bookkeeping once this record
lands; it is the reply, recorded here, that continues anything.

## Bounds, as answered

Copied byte-for-byte from the packet at `78d18444`, section "Bounds",
lines 537–550:

````markdown
Every bound of the 2026-09-02 authorization and its 2026-09-05
continuation holds, and these with them:

- **Exactly the built behavior above.** No requirement, scenario or
  behavior beyond it, and no other M2 slice. B11 names uses of slice 5's
  mechanism by two other lanes and authorizes nothing else in them.
- **No new Butlers content class, body read, Git history read or provider
  egress.** Butlers bodies are read only as the acts in force already
  allow, behind the implementation's PWB-REQ-005 evaluation. Under
  reading (i) no new Git object is read either.
- **The daemon executes no observed code.** Separate operator commands run
  tests.
- **Reviewed and verified per craft-and-care**, with the battery run at a
  committed tree in a clone (rule 7).
````

## What this does not authorize

Copied byte-for-byte from the packet at `78d18444`, section "What this
direction would not authorize", lines 554–578:

````markdown
- No edit to any act-bound or signed byte: not the registry entry, not the
  eleven PWB subjects (including the five `unknown-uncovered` rows), not
  any act or sign-off record.
- No change to `packages/cap1-core` or CAP1-REQ-062; the judge is imported
  as it is.
- No registry value, bound or semantics change, no consent amendment, no
  policy change, and no re-pin of the stale `governingBehaviorContract`
  pins (row P-95's own acts). In particular, no bound for
  `governing-intent-relation`.
- No briefing route (M5 slice 3, `syzygy-dov.5.2`) and no reading of
  `maxBriefingResponseBytes`. `[Observed]` The machine-view package
  (`syzygy-dov.22`) is signed and its gate closed, and its act says "the
  briefing member stays unservable until its ceiling is declared and the
  route is separately authorized". So the route waits for its own
  separate authorization, and this direction is not it.
- No part of item depth or the opening band beyond B11.
- No write, egress, observed-code execution, deployment, release,
  recovery or mission effect on Butlers or any repository; no second
  repository; no multi-user support, broad remote access or autonomous
  behavior; no unattended agent coordination.
- No doctrine or contract change, and no reading of an accepted contract
  adopted as conformance.
- No independent verification: like the acts it rests on, this would be a
  state-(1) owner direction. It is a warrant, not evidence, and proves no
  read, judgment, render or result.
````

Every exclusion of the 2026-09-02 authorization and its 2026-09-05
continuation is retained unchanged. This record adds no digest, manifest,
recorder script, acceptance-act row or governance-check entry, and it
claims no independent verification: it is a state-(1) owner direction, a
warrant and not evidence, and it proves no read, judgment, render or
result.

## Escalation triggers

Copied byte-for-byte from the packet at `78d18444`, section "Escalation
triggers", lines 622–629:

````markdown
Stop and return to you before proceeding if slice 5, or a B11 use, would
need any of: a change to doctrine or an accepted contract; a further
amendment to the signed PWB specification; a change to security, privacy
or retention posture; a change to any value or semantics sentence the
effective registry entry declares, or any field B9 leaves unread; any
observation outside the consented content class or repository, including
a Git history read; a Polaris size breach under B10; or any behavior beyond
B1–B11.
````

## Withdrawal and owner correction

Copied byte-for-byte from the packet at `78d18444`, section "Withdrawal",
lines 633–635:

````markdown
A later direction may narrow or withdraw this one at any time. Withdrawal
defeats grant: on withdrawal no further slice-5 work or B11 use proceeds,
and whether to revert what landed is a question for that later direction.
````

`[Unknown]` Whether the owner intended any narrower or wider reading than
the four points above. The recorder's reading stands only until a later
direction narrows or withdraws it, and withdrawal defeats grant.
