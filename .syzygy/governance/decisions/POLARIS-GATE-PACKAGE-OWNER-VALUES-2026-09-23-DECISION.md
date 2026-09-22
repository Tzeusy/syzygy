# Polaris gate packages — the owner's values for `syzygy-dov.18`, `.21`, `.22`, `.30` and their landing order (2026-09-23)

> **Plain owner direction. Performs no act.** This record carries the values
> the owner chose for four candidate gate packages drafted under
> `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, and the order in which
> the spec-touching packages land. It binds no digest, amends no
> specification, policy or registry byte, adds no row to
> `ACCEPTANCE-ACT-RECORD.md` and registers nothing. Each package still takes
> effect only through its own owner act, performed with its own phrase over
> its own regenerated manifest, after its own review. Nothing here is that
> act, and no phrase quoted in any packet was offered or given.

## How the values were given

Date: 2026-09-23. Owner: Tzeusy. Channel: the owner, in the Claude Code CLI,
asked to be walked through the pending decisions "with /th-projects
questionnaire", and answered one structured question at a time. Each answer
below is the option label the owner selected, quoted byte-for-byte; the
owner made no edits and added no notes. Every selection was the option
presented as recommended.

Evidence snapshot: Syzygy `origin/main` at `57863cc`. The five packets were
read at that commit and none had moved on `origin` since the local `9d74185`
(`git diff HEAD origin/main` over `contracts/candidates/` and `decisions/`
was empty).

Items were presented from the drafting lead's summary of the five packets
and the packets themselves. They were **not** re-reviewed adversarially
before presentation in this sitting; each packet's own review status is
stated beside it, and each still owes the review its packet names before
any phrase is offered.

## 1. Registry currency bounds and briefing ceiling — `syzygy-dov.18`

Packet: `contracts/candidates/pwb-registry-currency-briefing-amendment/OWNER-DECISION-PACKET.md`.

| Question | Owner's answer (verbatim) |
|---|---|
| Currency bounds (`maxAgeMs`) for the 13 claim classes? | "Four tiers as drafted (Recommended)" |
| Briefing response ceiling (`maxBriefingResponseBytes`)? | "20480 B (Recommended)" |
| Should the superseding registry act also move the entry's two governance-lifecycle strings off their candidate values? (packet open question 3) | "Leave unchanged (Recommended)" |

Reading: the fourteen values in the packet's two tables stand as proposed —
365 days for `project-account-section`, `principle`, `success-criterion`,
`project-account-statement`; 180 days for `design-contract`,
`baseline-spec`, `craft-policy`; 90 days for `catalog-entry`,
`topology-component`, `project-fact-declaration`, `source-coverage`; 30 days
for `roster-identity`, `project-shape`; and a 20,480-byte briefing ceiling.
The packet's open question 3 is answered: the act argument does not widen to
the lifecycle strings. Open questions 1, 2, 4, 5 and 6 were not put and stay
open. The gates `.19` (continuation direction) and `.20` (Q7a scenario)
become draftable.

## 2. Derived read-only machine views — `syzygy-dov.22`

Packet: `contracts/candidates/pwb-machine-view-amendment/OWNER-DECISION-PACKET.md`.
Review status at presentation: none run.

| Question | Owner's answer (verbatim) |
|---|---|
| Name for the second declared category (the generation draft)? | "generated editorial draft view (Recommended)" |
| Route shape for the draft member? | "/polaris/draft/<runId> (Recommended)" |
| RFC6-21 'endpoints always serve the full set' — which reading? | "Narrow (Recommended)" |

Reading: every drafted value stands, which is the packet's arm **(a)** —
send it to fresh-context review as drafted. The narrow `RFC6-21` reading is
the owner's instruction to the drafter; the reviewer remains free to find
that the wide reading holds, which would make this a two-act package and
return it to the owner.

## 3. Opening-band aggregate scenario — `syzygy-dov.21`

Packet: `contracts/candidates/pwb-opening-band-scenario/OWNER-DECISION-PACKET.md`.
Review status at presentation: one review, `CONFIRM WITH EXCEPTIONS`,
repaired in prose; a confirmation over the repaired bytes has not run.

| Question | Owner's answer (verbatim) |
|---|---|
| OQ-1: how do slices 4 and 5 get spec coverage? | "Fold into dov.26 package (Recommended)" |
| OQ-2: which requirement hosts the scenario? | "(A) Under PWB-REQ-010 (Recommended)" |

Reading: OQ-1 takes the packet's route (a) — slices 4 and 5 obtain their
RFC2-26 coverage from a further OpenSpec amendment inside the P-75 Q1
three-surface package at gate `syzygy-dov.26`, and wait for it. OQ-2 keeps
the drafted placement, so no patch byte moves and the reviewed manifest is
unchanged. OQ-3, OQ-4 and OQ-5 were not put and stay open; OQ-5 (block order
within the band) is reserved to the owner by P-71 Q7 and must be answered
before slice 3 is scheduled.

## 4. Exact-source render mode — `syzygy-dov.30`

Packet: `contracts/candidates/pwb-exact-source-render-mode-scenario/OWNER-DECISION-PACKET.md`.
Review status at presentation: round 1 `CONFIRM WITH EXCEPTIONS`, repaired;
round 2 outstanding.

| Question | Owner's answer (verbatim) |
|---|---|
| Render-mode package: proceed as drafted? | "(a) Yes, two modes (Recommended)" |

Reading: the closed two-mode vocabulary stands; round 2 runs on the repaired
bytes before the phrase is offered. The packet's second choice — which of
this and lane B lands first — is answered by §6.

## 5. Retention posture — `syzygy-dov.28`

Recorded separately, because the owner issued it as a direction in the same
sitting: `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md`
(this directory).

## 6. Landing order of the spec-touching packages

| Question | Owner's answer (verbatim) |
|---|---|
| Landing order for lane B and the three spec-touching packages? | "Readiness order, lane B last (Recommended)" |

As presented, that option read: ".21 → .30 → .22 → lane B. Nothing waits on
lane B's long ceremony; each later package regenerates mechanically. Departs
from the .21 packet's 'after lane B' suggestion."

Reading: the PWB successor-chain positions, when each act is performed, run
opening band (`.21`), then exact-source render mode (`.30`), then machine
views (`.22`), then lane B (`syzygy-dov.17`). Each package after the first
is regenerated with its builder's `--write` against the tree its
predecessor's act left, and its packet's quoted digest updated, before its
phrase is offered. This fixes order only: it does not advance any package
past a review it owes, and if an earlier package stalls, the owner — not an
agent — decides whether a later one may overtake it. The `.21` packet's
recommendation to chain after lane B is superseded by this answer, not
edited.

## What this does not do

It performs no act, offers no phrase, and authorizes no implementation. It
does not waive any review a packet names. It does not answer any open
question not quoted above. P-68's own ceremony for lane B (RFC-0007
successor, contract act, then behavior act) is unchanged; only its position
relative to the other three moves.
