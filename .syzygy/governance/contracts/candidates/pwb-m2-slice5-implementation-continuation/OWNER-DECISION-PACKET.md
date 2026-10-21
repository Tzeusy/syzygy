# Owner decision packet — PWB implementation continuation for M2 slice 5

> **Candidate — binds nothing.** This packet is an inert offering. It
> performs no act, records no direction, authorizes no implementation and
> changes no signed byte. It puts **one** question and offers **one** exact
> reply. The reply is offered only after a fresh-context review has cleared
> these exact bytes; until you give it, in your own words in your own
> session, nothing here has any effect. A commit, a merged pull request, a
> review, a passing check, a bead closing, silence, "Agreed", an option
> selection, the 2026-09-21 P-69 ruling, the 2026-10-20 questionnaire
> answer or any other act continues nothing.

Date drafted: 2026-10-21. Gate bead: `syzygy-dov.19`. Implementation bead
it would unblock: `syzygy-dov.2.2` (M2 slice 5, the declared currency bound
and `assessCurrency`). Drafted at Syzygy `29e036f4` (`origin/main`).

**What kind of thing this is.** The reply is a plain owner direction in the
family of `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`,
which it continues, and of
`.syzygy/governance/decisions/OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md`.
It binds no artifact digest, needs no manifest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and is registered in no governance check; no
recorder script exists or is needed for it. That precedent says of itself
that it "binds no artifact bytes, adds no row to the acceptance-act record
and registers nothing in CG-7e", and this packet follows it.

## Why a continuation is needed at all

`[Observed]` The 2026-09-05 continuation stops implementation at its
escalation triggers, quoted from its section "Escalation triggers":

> Stop and return to the owner before proceeding if implementation would
> need any of: a change to doctrine or an accepted contract; a further
> amendment to the signed PWB specification beyond the 2026-09-05 package;
> a change to security, privacy, or retention posture beyond the 2026-09-05
> approved secret-classification policy; a change to the constraints or
> envelope the 2026-09-05 registry entry declares; any observation outside
> the consented content class or repository; or any scope beyond the signed
> change.

Slice 5 crosses two of them: it consumes registry declarations added after
the 2026-09-05 entry, and it implements a PWB scenario signed after the
2026-09-05 package. Three records say in terms that a separate continuation
is still owed:

- the 2026-09-30 registry act
  (`.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`,
  "What this act does not authorize"): "No implementation consumes the new
  fields until the owner issues the separate plain continuation direction
  the ruling record names";
- the 2026-09-30 read-gate direction
  (`.syzygy/governance/decisions/OWNER-INSTRUCTIONS-2026-09-29-30-READABILITY-AND-REGISTRY.md`,
  "The direction, as issued"), which does not permit "reading, evaluating
  or rendering the entry's per-class currency bounds, its currency
  semantics block, or `maxBriefingResponseBytes`. That remains gated on
  `syzygy-dov.19` and the further gates the 2026-09-21 rulings name.";
- the signed missing-currency package's owner packet
  (`.syzygy/governance/contracts/candidates/pwb-missing-currency-disclosure-scenario/OWNER-DECISION-PACKET.md`,
  "Remaining separate gates for M2 slice 5"), which names "the plain
  implementation-continuation direction at `.19`" and "a fresh
  implementation authorization that resolves the five disclosed
  contract-coverage gaps and names the exact built behavior".

This one direction is offered as both: the continuation across the two
triggers, and the authorization that routes the five gaps and names the
built behavior. It does not need a third.

## The predecessor gates, read back at `29e036f4`

The 2026-09-21 P-69 ruling
(`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`)
says slice 5 "waits for a registry-entry amendment act, a continuation act,
P-68's ruling before any M2 spec package, and the Q7a scenario's sign-off
and act". That ruling prepared these gates; it performed no continuation.

| Gate | State | How it was read back |
|---|---|---|
| P-68 (lane B, `syzygy-dov.17`) | Ruled 2026-09-21; lane B then **declined** by owner direction 2026-10-02, so no M2 spec package waits on it | `.syzygy/governance/decisions/POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md` [Observed] |
| Registry-entry act (`syzygy-dov.18`) | Performed 2026-09-30; superseded for the `adopt-registry-entry` role on 2026-10-02 (behaviour-contract re-pin) and again on 2026-10-20 (machine ceiling), each successor leaving the currency fields byte-identical | [Observed] the registry entry's `currencyBounds` (13 rows) and `currencyBoundSemantics` (7 keys) are equal, parsed as JSON, at the three recording tags `pwb-adopt-registry-entry-signed-2026-09-30`, `pwb-adopt-registry-entry-signed-2026-10-02` and `pwb-registry-machine-ceiling-amendment-v1.0` and in the tree; the entry's SHA-256 in the tree equals the argument recorded in `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-MACHINE-CEILING-ACT.md`, the act the body-read gate evaluates today |
| Q7a scenario (`syzygy-dov.20`) | Signed v1.0 on 2026-10-02 (version-tagged sign-off, tag `pwb-missing-currency-disclosure-scenario-v1.0`) | [Observed] the scenario heading occurs once in the PWB `spec.md`, and its block, heading to next heading, is byte-identical at that tag and in the tree; record `.syzygy/governance/decisions/PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0.md` |
| Continuation (`syzygy-dov.19`) | **Not given.** This packet offers it | — |

The readback method is published in `IMPACT-LEDGER.md` so it can be
re-run. The 2026-10-20 questionnaire answer that selected
"missing-currency" among the amendments to authorize is evidence of your
intent and is not this act
[Observed: item `dov35-impl-authorization` of a git-ignored local
questionnaire dated 2026-10-20, not in this repository's history].

## The question

This is the text that would be put to you, unchanged:

> **Continue PWB implementation authorization for M2 slice 5?** The
> 2026-09-05 continuation stops at registry and signed-spec changes. The
> 2026-09-30 registry act (currency bounds, read through its 2026-10-20
> successor) and the 2026-10-02 missing-currency scenario v1.0 changed
> exactly those. Do you continue implementation authorization so that M2
> slice 5 (`syzygy-dov.2.2`) is built exactly as the packet
> `.syzygy/governance/contracts/candidates/pwb-m2-slice5-implementation-continuation/OWNER-DECISION-PACKET.md`
> describes under "The exact built behavior", with its five contract
> coverage gaps routed as it states (each stays `unknown-uncovered`), for
> the one configured Butlers repository and content class
> `declared-project-shape-text`, with every original exclusion retained: no
> release, deployment, Butlers write, second repository, wider content
> class, consent amendment, egress, observed-code execution, recovery,
> mission, autonomy or multi-user authority?
>
> Reply with the exact line below to grant it. Any other wording, or
> silence, continues nothing.

The exact reply, on one line:

```text
Continue PWB implementation authorization for M2 slice 5 as drafted
```

This line is **not** an act phrase. It binds no digest, it is registered in
no governance check, and no recorder script exists or is needed for it.

**If you do not give it** (the default): slice 5 is not built. The
project-shape model keeps assigning `fresh` to every claim from a constant,
which the M2 funnel recorded as a disclosed non-conformance to RFC2-9, and
the legend keeps marking the freshness states no claim reaches. The signed
scenario stays signed and
unimplemented; no claim renders its disclosure route. Nothing is unwound,
because nothing has been written.

## The exact built behavior

What the reply would authorize, and nothing beyond it. "The registry entry"
is `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`;
"the scenario" is PWB-REQ-007's "No effective currency bound is disclosed
outside freshness", as signed in v1.0.

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
  table of the claim-id families that sentence names. A claim id that
  matches no family takes the scenario's arm; it is never given a default
  or nearest class. The currency probe (`claim:currency-probe`, slice 2)
  is outside these bounds, as `outsideTheseBounds` says: it is not judged,
  gains no freshness and does not take the scenario's arm.
- **B3 — What age is measured.** Evidence age runs from the committer
  instant of the evaluated revision, which the model already carries as
  the revision's source-claimed instant, to the evaluation's own as-of
  instant (the observation instant), never to a wall clock. `[Inferred]`
  This is the drafter's reading of `measuredFrom`, "the committer instant
  of the exact Git object the declaration was extracted from": only a
  commit carries a committer instant, and the one commit an extraction
  reads through is the evaluated revision. It reads no new Git object. The
  alternative is your option O1 below; this reply does not choose it.
- **B4 — The judge.** `assessCurrency` is imported from
  `packages/cap1-core` unchanged and called once per assigned claim with
  its class, its evidence instant, the effective rows and the as-of
  instant. The model's `fresh` constant and the comment arguing that "the
  evaluation itself is the currency" are removed; no code path sets a
  freshness value except from the judge. Its arms map as follows:
  - `current`: freshness `fresh`; label, tier and reasons as otherwise
    derived.
  - `stale`, on any of its three bases (`age-exceeds-bound`,
    `unreadable-instant`, `future-dated-instant`): freshness `stale` and
    reason `stale-beyond-currency-bound`, with the basis carried
    machine-readably, as the entry's `outOfBoundResult` requires. An
    Observed claim becomes Unknown with that primary reason. A claim
    already Unknown keeps its primary reason and gains
    `stale-beyond-currency-bound` as a secondary. `[Inferred]` That
    precedence is the drafter's composition; RFC2-24 states none.
  - `no-bound-declared`, and every claim B1 or B2 leaves without an
    effective row: the scenario, exactly. The claim renders Unknown with
    primary reason `no-currency-bound-declared` and the route
    `Declare the bound in quality policy`; any reason it would otherwise
    carry is kept
    as a secondary, never dropped (`[Inferred]` the drafter's composition
    of the scenario's fixed primary reason with the tuple's other
    reasons). It carries **no freshness value**: the
    field is absent from the model and the machine answer, and the human
    tuple has no freshness attribute. The missing bound is a named,
    expandable fact of the render outside the freshness slot. Where a
    declaration is present but its act is not effective, the RFC2-9
    contradiction route to the owner renders beside the Declare route.
    No fifth freshness value, no `null` spelled as a value, and no
    sentinel string is minted.
- **B5 — Aggregates.** Every aggregate that has members under the
  scenario's arm discloses, apart from its per-freshness counts, the count
  of those members, so that the counts together equal its membership. It
  carries no freshness value of its own, derives none from its other
  members, never shows the unbounded members as zero, and keeps their
  primary-reason count and route visible. No aggregate folds an Unknown
  into a favourable total.
- **B6 — Both channels, identically.** The human page and the machine
  answers carry the same tuple and the same outside-slot disclosure for
  each claim, and the PWB-REQ-020 parity sweep covers the disclosure as its
  own family. The machine evidence block's `currencyBounds`, empty until
  now, carries the effective rows exactly as declared.
- **B7 — The legend stays true.** The slice-1 copy oracle keeps every
  freshness legend sentence either reachable or marked unreachable with its
  reason; a value that slice 5 makes reachable (such as `stale`) loses its
  marker without a separate copy edit.
- **B8 — Determinism.** One identified evaluation served twice is
  byte-identical. No timer, poller or watcher is added; a new judgment
  happens only through a new identified evaluation, which stays
  human-triggered.
- **B9 — Not consumed.** `maxBriefingResponseBytes` and
  `governingBehaviorContract` stay unread. No briefing route is served.
- **B10 — How it is shown to work.** Every falsifier limb of the scenario
  and of B1–B8 has a test whose expected values are literals independent
  of the module under test, and a rule-6 mutant that makes it fail, with
  the mutant's old and new fragments and its commit recorded. Fixtures
  reach every judge arm through the PWB model, including an out-of-bound
  class that renders `stale` at least once, an unassigned claim id, an
  ineffective registry act and an aggregate with unbounded members. The
  number of claims in each arm at a live evaluation is measured and
  recorded with its subject and digest (rule 11), never assumed. `/polaris`
  is measured on both host forms against the 2,097,152-byte ceiling and the
  1,650,000-byte working target; a breach stops the lane and returns to
  you, and is never repaired by omitting a disclosure.

Slice 5 changes the shared Three-Surface POC model, so it takes the
shared-model WIP-one slot in its turn; the coordinator orders it behind the
chain the 2026-10-15 direction fixes.

## The five contract-coverage gaps, and how this routes them

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
| RFC6-14.r1 | Every claim carries label, tier and primary and secondary reasons; every claim with an effective row carries one of the four freshness values from the judge (B4) | Freshness on the scenario's arm, which carries the outside-slot disclosure instead | Nothing |
| RFC6-14.r3 | The machine tuple equals the human tuple; the disclosure is carried in the machine answer; no Unknown folds into a total (B4–B6) | Whether an absent freshness value plus the disclosure is "the complete epistemic tuple" | Nothing |
| RFC6-17.r1 | Per-freshness counts plus the unbounded-member count equal membership; label, tier and reason counts are unchanged (B5) | Whether the separate unbounded-member count meets "per-freshness-state counts" | Nothing |
| RFC7-16.r1 | Each rendered status is kernel-judged at an identified evaluation; staleness (`stale`) is visible on the narrative page itself (B4, B8) | Freshness on the scenario's arm | Nothing |
| RFC7-33.r1 | The same attributes and the same disclosure travel in both views, under the parity sweep (B6) | Freshness on the scenario's arm | Nothing |

`[Inferred]` RFC2-10 itself says "A condition genuinely outside the four is
disclosed as a fact of the render, never dressed as a freshness state",
and that sentence is what the scenario relies on. Whether it makes the
scenario's arm conform to the four freshness members above is a reading of
accepted contracts. Verification rule 8 does not let an implementation
adopt it, so **the build claims no conformance on that arm**, and all five
rows stay `unknown-uncovered` in the signed matrix. `[Inferred]` With all
thirteen classes declared and every minted claim-id family assigned, the
arm should have no live members; that is what B10's measurement tests,
and it may come back otherwise.

**The one choice of substance here is yours, and the reply makes it:**
whether to build across five accepted-contract consequences whose
conformance on one arm stays Unknown. The alternative is to wait for a
contract reading or amendment first; that is not offered here, and
declining (the default) keeps the current constant, which is itself a
disclosed non-conformance to RFC2-9.

## Your option inside this packet

**O1 — what `measuredFrom` measures.** B3 takes reading (i). Reading (ii)
is yours to prefer instead.

| Reading | Age of a claim's evidence | Cost | Consequence |
|---|---|---|---|
| (i) **drafted** | as-of instant minus the evaluated revision's committer instant; one age for every claim of an evaluation, compared to each class's own bound | none: the instant is already captured | a declaration unchanged for years reads `fresh` while the observed revision is recent; a class goes stale only when the revision is older than its bound |
| (ii) | as-of instant minus the committer instant of the newest commit, at or before the evaluated revision, that changed the declaring source | a new Git history read per source (metadata, not body), and a rule for merges | each source ages separately, as the per-class values (four distinct, 30 to 365 days) suggest; many more claims render Unknown on a live evaluation |

`[Inferred]` Reading (i) is drafted because the claims are report facts
("the source declares X" at the evaluated revision), so the evidence
behind them is as old as the snapshot, and it reads nothing new. If you
prefer (ii), do not give the reply: say so, and a revised packet is drafted
and reviewed. The reply above authorizes (i) only.

## Bounds

Every bound of the 2026-09-02 authorization and its 2026-09-05
continuation holds, and these with them:

- **Exactly the built behavior above.** No requirement, scenario or
  behavior beyond it, and no other M2 slice.
- **No new Butlers content class, body read or provider egress.** Butlers
  bodies are read only as the acts in force already allow, behind the
  implementation's PWB-REQ-005 evaluation. Under reading (i) no new Git
  object is read either.
- **The daemon executes no observed code.** Separate operator commands run
  tests.
- **Reviewed and verified per craft-and-care**, with the battery run at a
  committed tree in a clone (rule 7).

## What this direction would not authorize

- No edit to any act-bound or signed byte: not the registry entry, not the
  eleven PWB subjects (including the five `unknown-uncovered` rows), not
  any act or sign-off record.
- No change to `packages/cap1-core` or CAP1-REQ-062; the judge is imported
  as it is.
- No registry value, bound or semantics change, no consent amendment, no
  policy change, and no re-pin of the stale `governingBehaviorContract`
  pins (row P-95's own acts).
- No briefing route and no reading of `maxBriefingResponseBytes`, which
  wait for the machine-view package (`syzygy-dov.22`) and M5 slice 3.
- No write, egress, observed-code execution, deployment, release,
  recovery or mission effect on Butlers or any repository; no second
  repository; no multi-user support, broad remote access or autonomous
  behavior; no unattended agent coordination.
- No doctrine or contract change, and no reading of an accepted contract
  adopted as conformance.
- No independent verification: like the acts it rests on, this would be a
  state-(1) owner direction. It is a warrant, not evidence, and proves no
  read, judgment, render or result.

## Overlap with the dov.35 successor direction

`[Observed]` Bead `syzygy-sin5` is drafting a successor to the 2026-10-15
implementation direction from the same 2026-10-20 answer, and its
selection includes "missing-currency". That direction would authorize the
signed text; it would not by itself cross the registry trigger or route the
five gaps. If both are given, they cover the same slice and neither widens
the other; this one names the built behavior. `[Inferred]` The cleaner
order is for that successor to name missing-currency as covered through
this direction rather than on its own.

## Escalation triggers

Stop and return to you before proceeding if slice 5 would need any of: a
change to doctrine or an accepted contract; a further amendment to the
signed PWB specification; a change to security, privacy or retention
posture; a change to any value or semantics sentence the effective
registry entry declares, or any field B9 leaves unread; any observation
outside the consented content class or repository; a Polaris size breach;
or any behavior beyond B1–B10.

## Withdrawal

A later direction may narrow or withdraw this one at any time. Withdrawal
defeats grant: on withdrawal no further slice-5 work proceeds, and whether
to revert what landed is a question for that later direction.

## The record a recorder would write

The record would be a new file in `.syzygy/governance/decisions/`, named
PWB-M2-SLICE-5-IMPLEMENTATION-CONTINUATION-DIRECTION.md, in the shape of
the 2026-09-05 continuation record: date, owner, repository state at
recording, the question and your reply quoted byte-for-byte, the recorder's
reading of scope labeled `[Inferred]`, the bounds and exclusions above,
and a citation of the 2026-09-02 authorization and the 2026-09-05
continuation it continues. **This packet does not write it, and no such
file exists.** Recording it would add no manifest, no recorder script, no
`ACCEPTANCE-ACT-RECORD.md` row and no entry in `scripts/check_governance.py`;
afterwards, documentation cites the record and restates none of it. The
gate bead `syzygy-dov.19` closing is what would unblock `syzygy-dov.2.2`;
nothing else is unblocked.

## Review

No review has run on these bytes. `REVIEW-BRIEF.md` commissions one; its
raw output, verdict and dispositions are recorded here only after it runs.
