# Owner decision packet — PWB derived read-only machine views

> **Inert offering.** This packet performs nothing. It presents one decision,
> records nothing, and authorizes no implementation, no route and no registry
> edit. A commit, a merged pull request, a review, a manifest, silence or a
> general "approved" performs no act.

Date: 2026-09-21 (first draft). **Status as of 2026-09-23:** reviewed five
times in fresh context — round 1 `CONFIRM WITH EXCEPTIONS`
(`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-RAW.md`), round 2 over the repaired
bytes at `9d74185` `CONFIRM WITH EXCEPTIONS`
(`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-RAW.md`), round 3 over
the repaired bytes at `76b4beb` `CONFIRM WITH EXCEPTIONS`
(`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-2-RAW.md`), round 4
over the repaired bytes at `194f8cd` `CONFIRM WITH EXCEPTIONS`
(`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-3-RAW.md`), round 5
over the repaired bytes at `cd1fbd3` `CONFIRM WITH EXCEPTIONS`
(`docs/reviews/R-PWB-MACHINE-VIEW-DELTA-CONFIRMATION-4-RAW.md`); each
round's exceptions were prose, repaired after it, so the bytes you are
reading carry no confirmation (rule 10) until a round confirms them. Round
4's reviewer wrote that `RFC6-21`'s clause, literally, "reads more
naturally as a property of every endpoint" than as the narrow reading you
chose, "so the tension the delta flags is real", but did "not find the wide
reading compellingly *forced*"; no round has (see `SEMANTIC-DELTA.md`
§Review, round 4). The first draft said here "no review has been run against these bytes, and no
verdict exists for them"; true on 2026-09-21, superseded since.

Ruling of record: **P-72** (question 1) and **P-76** (question 3), both ruled
arm A on 2026-09-21 in
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`.
This packet opens no new register row; it is the drafted realization of
rulings already made, on gate bead `syzygy-dov.22`.

Behavior manifest: `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt` (this directory),
eleven rows, hashing the eleven PWB behavior artifacts **as they will be
after** the two patches under `proposed/` are applied. Two rows differ from
the tree today; nine equal it.

Behavior manifest SHA-256:
`2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c`

This packet wrapper is not an act subject. Its bytes will be bound by the
retained review of the package; changing this packet after that review
retires the review.

## Why this is here

You ruled on 2026-09-21 that one PWB semantic delta should name a closed
"derived read-only machine view" category covering the machine Polaris route
and the briefing (P-72), with the generation draft route folded in as a
second declared category (P-76). Your cross-cutting reading made this the
widest gate: four pursuit slices wait on it.

The reason a category is needed at all is that the signed specification names
no route and says nothing about a second machine response derived from the
machine answer. Today `/api/poc/polaris` is served anyway —
`machine-credentialed`, under the machine-JSON ceiling — with no stated rule
and no check that what it serves is derivable from the machine answer
[Observed: its route test covers credential refusal, page-anchor citation and
typed failure under the ceiling, and does not compare the envelope against
the machine answer's bytes]. The delta states the rule once, names the
members, and makes the unminted briefing ceiling a precondition of service
rather than something discovered after the route ships.

## What the package changes

One block of prose inserted into PWB-REQ-020, between its `Group:` line and
its SHALL sentence. Nothing is removed and no existing sentence is reworded;
the patch contains no removed line. The second patched artifact is the
generated `GOVERNING-DEPENDENCIES.md`, whose one `Source:` digest line
follows the specification automatically.

The inserted text says, in four paragraphs:

1. This requirement compares the human surface against the machine answer;
   two closed categories of derived, read-only machine view sit beside it;
   the comparison ranges over neither; an unnamed route is a member of
   neither.
2. **Derived read-only machine view** — composes only values reachable from
   the machine answer at the same evaluation, mints no project fact, writes
   nothing, is machine-credentialed in every mount form, subtracts nothing.
   Every value it serves must be independently verified as derivable, by a
   checker that imports no rendering code. Members: the Polaris presentation
   view `GET /api/poc/polaris` (under the ceiling the registry already
   declares) and the agent briefing view `GET /api/poc/briefing` (under a
   ceiling of its own).
3. **Generated editorial draft view** — composes only the recorded bytes of
   one identified generation run over sources it was already admitted to
   read; mints nothing, writes nothing, sends nothing outside the observing
   project; carries no project-shape field and so contributes to neither
   compared multiset. Member: `GET /polaris/draft/<runId>`.
4. A member with a ceiling of its own may not be served before the registry
   declares that ceiling. A route joins a category only by a later amendment
   naming it. A route in neither category is neither admitted nor forbidden
   by this requirement.

## What the package does not change

PWB-REQ-004's closed project-fact population; every existing sentence of
PWB-REQ-020, including its Observable, oracle, falsifier and warrants; every
existing route's credential class and ceiling; the adapter-registry entry;
PWB-REQ-011, PWB-REQ-014 and PWB-REQ-016; `design.md`; the contract-coverage
matrix; every RFC clause; and every consent, retention or egress posture. The
full enumeration, with the reasons a reader might expect otherwise, is in
`SEMANTIC-DELTA.md`.

## The change class, stated against its own source

The analysis this delta comes from records the class as *clarifying*. The
delta records **Normative** and says why: it adds a verification obligation
the one existing member does not meet today, adds a precondition on serving a
future member, and narrows the parity oracle's population. Someone who
complied before does not comply on the day the amendment takes effect. The
classification does not change what you must do — the specification is
digest-bound and needs your act at either class — but it changes what the
reviewer is told to test.

## Values in this draft that are really yours

Everything in this table is a drafting proposal, not something your ruling
settled. Arm (b) below is how you change any of them.

| Value | Drafted as | Why, and what else was available |
|---|---|---|
| First category's name | "derived read-only machine view" | Your words in P-72's ruled arm; carried unchanged |
| Second category's name | "generated editorial draft view" | The analysis's words; your ruling folds the category in without naming it. Alternatives: "generation draft view", "editorial draft response" |
| Membership, category 1 | `/api/poc/polaris` (retroactive), `/api/poc/briefing` (prospective) | Exactly P-72's arm A |
| Membership, category 2 | `/polaris/draft/<runId>` | The route shape the generation analysis proposes; the runId form is a proposal |
| How a later instance enters | A later amendment to this specification naming it as a member | Keeps the category closed. The alternative — a membership test anyone may apply — would make "closed" untrue |
| Routes in neither category | "neither admitted nor forbidden by this requirement" | Keeps the schema document and the machine status route open, which your P-77 and P-78 rulings hold behind this gate. The alternative — forbidding them — would force a third category now |
| Registry field names in the specification | None. The text says "the adapter-registry entry's resource envelope declares that ceiling" | Naming `maxBriefingResponseBytes` in the specification would create a literal that dangles until the registry act. The identity stays with the registry act |
| Where the block sits | Inside PWB-REQ-020, before its SHALL sentence | Keeps the parity scoping next to the parity obligation, and does not collide with the sibling package's patch |

## Risk

- **The `RFC6-21` reading.** "Endpoints always serve the full set" can be
  read as a property of every endpoint, in which case a task-scoped briefing
  needs an `RFC-0006` amendment and a second act. The delta takes the narrow
  reading (the full set stays served by the machine answer; a derived view
  hides nothing at rest) and discloses the wide one for the reviewer to
  decide. If the wide reading holds, this becomes a two-act package like the
  sibling.
- **A closed category ages.** Every new machine view needs an amendment to a
  signed specification. That is the cost of closure; the alternative is a
  test a future agent applies on its own.
- **Adopting before the registry act** leaves the briefing member named and
  unservable. That is the intended state, not a defect — but it means the
  specification will, for a period, name a route that returns nothing.

## The decision

**Does this package, as drafted, realize your P-72 and P-76 rulings?**

**(a) Yes — as drafted.** Fresh-context review runs per `REVIEW-BRIEF.md`;
findings are repaired; a sign-off phrase is offered to you only once a round
confirms the repaired bytes and a recorder entry exists. (For the rounds
run so far see the status line at the head of this packet; the patches and
manifest never moved, so no regeneration was needed. The first draft of this arm read "send it to
fresh-context review as drafted … the manifest is regenerated", written
before any round ran.)

**(b) Yes, with named changes.** Name the rows in the table above you want
different — a category name, a member, the route shape, the closure rule, or
the placement — and the package is redrafted and then reviewed. The manifest
digest below is retired by any such change.

**(c) No.** The drafted realization is declined and the rulings return to you
for re-statement. The 2026-09-05 package stays the PWB authority; nothing
renders or serves differently.

Silence, a partial answer, a commit or a merge performs nothing. In every
case above, the signed specification stands unamended until an act says
otherwise.

## Not yet offered: the sign-off phrase

The behavior act phrase for this manifest would be:

```
SIGN OFF PWB MACHINE-VIEW AMENDMENT: 2a49a8d1d473d4347dadda1489488bc6556102c14e98e18bc58688ffeeb3ed6c
```

It is written here so that the governance checks can see it go stale, and it
is **not offered**: the two fresh-context rounds confirm the commits they
reviewed, not these repaired bytes (rule 10), and the behavior recorder
(`scripts/record_pwb_behavior_amendment_acts.py`, added 2026-09-23) carries
no entry for this package yet. If you reply with this phrase now, nothing is
performed. (The first draft gave the reason as "no fresh-context review has
confirmed these bytes, and no recorder exists"; the first half is now the
rule-10 form above.)

## Two acts, and why their order is free

1. **The registry act** (P-72 question 2, gate bead `syzygy-dov.18`) — a
   superseding act over the adapter-registry entry that mints the briefing
   ceiling. Its subject is the registry entry, not this manifest.
2. **The behavior amendment act** over the manifest digest above — a
   dedicated recorder in the 2026-09-05 shape verifies the phrase against the
   manifest bytes, applies the two patches with the builder's
   `--apply --at-adoption`, confirms every row now hashes the tree, writes
   the dedicated record and the aggregate section of
   `ACCEPTANCE-ACT-RECORD.md`; the same change registers the chain link in
   `check_governance.py`.

Either may be performed first. If the behavior act is performed alone, the
briefing view is named and may not be served. If the registry act is
performed alone, a ceiling exists for a route the specification has not yet
placed in a category. Nothing is implemented after either act; an
implementation bead is opened separately, under its own authorization.

## One more ordering, which is arithmetic

The sibling candidate
`.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/` is
pending against the same eleven subjects. The two specification patches
compose in either order and the builder verifies both compositions on every
run. Re-derived at `76b4beb` (2026-09-23), five candidates carry a
`proposed/spec.md.patch` against the PWB `spec.md` (this one, lane B,
`pwb-exact-source-render-mode-scenario/`, `pwb-opening-band-scenario/` and
`pwb-missing-currency-disclosure-scenario/`); this builder composes against
lane B only, so read "second" below as "each one signed after the first".
(An earlier sentence here counted three; it was false when committed,
§Review round 3 F6.) The generated dependency declaration does not compose
— both packages rewrite its one `Source:` digest line — so **whichever
package you sign second must be regenerated against the tree after the
first lands**, and its packet's quoted digest updated before its act.
`--write` repairs that line only and does not make a sibling's
specification patch apply. Neither package's prose touches the other's
sentences, so this is a rebuild, not a disagreement. The order itself you
have already fixed, in
`.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
§6; this packet cites it and does not restate it.

## How to check this packet

```
python3 scripts/build_pwb_machine_view_amendment.py --check
python3 scripts/build_pwb_machine_view_amendment.py --selftest
python3 scripts/build_pwb_machine_view_amendment.py --diff
```

The first recomputes all eleven rows from the current tree and re-derives the
dependency declaration from the proposed specification; the second mutates
its own inputs and confirms each check fails closed; the third prints the
proposed bytes as diffs. All three are read-only.
