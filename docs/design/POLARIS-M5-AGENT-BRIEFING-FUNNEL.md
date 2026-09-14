
# Feature request M5 — The agent's briefing: a task-scoped route, the dispatch packet and the prohibitions on the machine channel

> **Candidate — binds nothing.** This is the feature-request funnel for
> the fifth move released from the 2026-09-13 vision pursuit. It
> proposes; the owner disposes (VIS-4). Nothing here authorizes
> implementation, and no bead becomes runnable by this file. Bead:
> `syzygy-dov.5`. Dossier: `docs/pursuits/2026-09-13-vision-pursuit.md`,
> section M5. It is written in the shape of
> `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`, of the M1 ruling
> (`.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`),
> and of the M2 and M4 packets as reviewed on `agent/syzygy-dov.2` and
> `agent/syzygy-dov.4`.

Date: 2026-09-14. Author: a funnel session (Claude), for the owner.

Size: **medium** for slices 1–2 (app and core changes to fields already
served on `/api/poc`, no new route, no governed artifact touched);
**large** for slice 3, because it adds a new machine-credentialed route
and, per this packet's Gate 5 reading, a new route inside a signed spec
is a spec delta through CC-REV-2 and needs its own owner ruling before
any code is written (Q1). Slice 4 (path and change selectors) is
deferred and not designed here.

Baseline: Syzygy `a9f671e` (main) [Observed]. `git diff --stat
f4589e2..a9f671e -- apps packages` touches 31 files, all under
`apps/three-surface-poc/src/polaris.ts`, `polaris-narrative.ts`, their
tests, and a new `packages/polaris-generation-core/` package — none of
the files this packet cites
(`apps/three-surface-poc/src/routes.ts`, `browser-origin.ts`,
`materialize-action.ts`,
`packages/three-surface-poc-core/src/model.ts`, `proposed-work.ts`,
`body-read-authority.ts`, `authority-disclosure.ts`,
`project-shape-observation.ts`, `materialization.ts`). A restricted
`git diff --stat f4589e2..a9f671e` over exactly those nine files
returns **no rows** [Observed, this session], so every line number
below is current at `a9f671e` and was current at `f4589e2` too — the
dossier's own citations were not re-derived from a moved file, they
were imprecise at their own baseline (see "Line numbers re-verified"
under Measurements).

## The four questions for the owner

Batched, each with the recommended answer first. Everything below is
the evidence behind them. Slices 1 and 2 need no owner act on this
packet's own reading (Gate 3); every open question below belongs to
slice 3, the new route.

| # | Question | Recommended |
|---|---|---|
| Q1 | **Does `GET /api/poc/briefing`, a new machine-credentialed route, need a spec delta before it may be built, and if so to which spec?** The three-surface-poc-experience spec's own reader note is definitional: "the 'machine answer' is the authenticated `GET /api/poc` response" (line 26, singular, definite article) [Observed]. A precedent already exists that was never spec'd this way: `POLARIS_PRESENTATION_PATH` (`/api/poc/polaris`) is a second `machine-credentialed` route, justified only by a code comment citing PWB-REQ-014/020, named by no POC-REQ or PWB-REQ heading. | **Yes, a delta is needed, and it should cover both routes at once.** Draft a small PWB semantic delta (in the 2026-09-05 amendment shape) that names a closed category — "derived read-only machine view": composed only of fields already reachable from `/api/poc` at the same evaluation, independently oracle-verified as derivable, served under its own declared, digest-bound response ceiling — and place both `/api/poc/polaris` (retroactively) and `/api/poc/briefing` (prospectively) under it. This closes the same gap for two routes in one package instead of drafting a narrower POC-spec reader-note widening now and a PWB delta later when the next such route appears. The counter-argument: a POC-only reader-note widening is smaller, touches no digest-bound PWB text, and unblocks sooner; it would need no owner act at all under the same continuation slices 1–2 ride, only a spec-authoring cycle. **Default if unanswered: slice 3 does not ship.** Slices 1 and 2 are unaffected and may proceed regardless of how Q1 is ruled. |
| Q2 | **If Q1 authorizes slice 3, how is its response ceiling declared?** `PwbResourceLimits` (`packages/three-surface-poc-core/src/project-shape-observation.ts` lines 65–73) has exactly two fields, `maxHumanResponseBytes` (2,097,152) and `maxMachineResponseBytes` (8,388,608), both digest-bound inside the registry entry that `PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` adopted [Observed]. Reusing `maxMachineResponseBytes` as the briefing's hard bound would let a briefing grow to 8 MiB with nothing to stop it — the exact defect this move exists to fix. | **Mint `maxBriefingResponseBytes` in the registry entry, adopted by a superseding act in the 2026-09-05 shape (the same mechanism M2's Q2 already recommends for a currency bound).** It reuses an act phrase, a recorder and a `--check` that already exist, and a declared, digest-bound number is the only form of "ceiling" `boundedResponse` (`routes.ts` lines 111–121) already enforces without new code — the function is generic over which `ResponseLimitIdentity` it is passed. Counter-argument: it is a second owner step queued behind Q1's spec delta, and until it lands slice 3 cannot ship at all. **Default if unanswered: slice 3 reuses `maxMachineResponseBytes` as its hard bound, with the ~20 KB figure enforced only by a test assertion** — a bound that could silently widen release by release with no registry gate to catch it, disclosed as such. |
| Q3 | **When the briefing route's own ceiling is breached, should the typed `503` body's `population` field describe the whole model (as it does today for the two existing ceilings) or the one subject the briefing was scoped to?** `ResponseLimitFailure.population` (`routes.ts` lines 113–121) is a closed two-member union, `{kind:'counted', sources, items, facts, exclusions}` or `{kind:'unknown', reason}`, both scoped to the whole project shape [Observed]. Reusing it verbatim for a one-claim briefing's breach would report "415 items, 439 facts" for a failure that has nothing to do with the whole model. | **Disclose the mismatch in prose; do not mint a third union member.** Add one sentence to the breach body — "population describes the whole evaluation, not this briefing's subject" — rather than widening a closed type on this packet's own authority, which is the same restraint M2's Q5 and M4's Q2 apply to their own closed vocabularies. Counter-argument: the sentence is a workaround, not a fix, and a reader parsing the JSON mechanically still sees whole-model counts. **Default if unanswered: reuse the existing `population` shape unchanged, with the disclosure sentence added** — no type change either way. |
| Q4 | **Sequencing against M4's routed-Unknown work (branch `agent/syzygy-dov.4`).** M4 slice 1 gives nine currently routeless Unknown disclosures (five relationships, four entities) a closed RFC2-24 reason and a route; M5's briefing (slice 3) reads exactly those same entities and relationships to compose "every Unknown touching the subject with its route." Building slice 3 before M4 lands means a briefing for `capability:whatsapp-transport-identity` echoes free-prose reasons M4 is in the process of closing. | **Ship slice 3 whenever Q1 and Q2 clear, independent of M4's landing order.** The briefing's own derivability oracle (Gate 4) reads the model's live `PocEpistemic`/`resolutionRoutes` shape, not a hand-copied list, so it improves automatically the moment M4 lands — no rework, no second edit. Counter-argument: shipping first means the briefing's own acceptance fixture briefly documents free-prose reasons as the current behavior, which a reviewer must then recognize as pre-M4 rather than a regression. **Default if unanswered: ship slice 3 on its own schedule; no ordering is enforced.** |

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine (heart-and-soul) | Yes, adopted: VIS-1…7, SEC-1…5 | VIS-1 rank order; VIS-3 (drafting a spec delta is not adopting it); VIS-4 (the trigger stays human); VIS-5 (Syzygy never writes code; a briefing route is a read, not a write); SEC-1 (the machine-credentialed authentication mechanism this move rides) |
| Decisions (legends-and-lore) | Yes | `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` and its escalation triggers; the 2026-09-05 continuation; P-52 (the eight-item POC cap — M5 runs under `syzygy-dov.5`, so untouched) |
| Specification (openspec) | Yes, signed and digest-bound: `openspec/changes/polaris-project-wide-butlers-model/` and `openspec/changes/three-surface-poc-experience/` | PWB-REQ-005 (authority states, quoted below); PWB-REQ-013 (proposed work stays subordinate); PWB-REQ-020 (parity, quoted below); PWB-REQ-004 (closed project-fact population, not entered by this move); the POC spec's reader note defining "the machine answer" as `GET /api/poc` (line 26) — the clause Q1 turns on |
| Topology (lay-and-land) | Candidate bundle only | Nothing beyond the core-versus-app placement already in force |
| Craft (craft-and-care) | Yes, owner-approved | CC-TEST-5/6 oracles, rule-6 mutation evidence, retained evidence, independent raw review |

## Gate 1 — Motif

**Problem.** Doctrine names agents a first-class consumer "from day one"
(`vision.md` lines 39–41: "It serves two first-class consumers from day
one: the owner (spatially, visually) and agents (machine-queryable
endpoints)"). Today an agent that wants to start work pays for the
whole `/api/poc` body to learn a handful of facts, receives no
requirement text on the credentialed channel it is meant to use, never
sees the one dispatch artifact the system can produce, and reads zero
machine-legible statements of what it may not do.

Four measurements, re-derived this session against the retained lane A
capture (`api-poc.json`, 5,520,314 bytes, sha256
`a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e`,
Butlers evaluation revision `2e3bac97790b`, verified against the M4
packet's own table before use):

1. **The orientation an agent needs is 0.339% of the payload; two
   task-irrelevant blocks are 68.2%.** `workItems` (2,273,467 bytes,
   7,396 beads presumably, 41.18%) and `codeStructure` (1,493,219
   bytes, 27.05%) together are 68.2% of the body; the same minimal
   orientation set the dossier named — `evaluation`, `project`,
   `observerRevision`, `projectShape.identity.scope`,
   `projectShape.authority`, `entities`, `relationships`,
   `proposedWork`, `projectShape.exclusions`, `projectShape.counts`,
   `projectShape.rootSummary`, `walkthroughReadiness`,
   `walkthroughJudgment`, `materializedBeadId` — is 18,719 bytes as one
   compact object, 0.339% [Observed, computed this session; method and
   full breakdown in the evidence file]. The dossier's own figure
   (18,710 bytes, 0.340% of a 5,508,208-byte pre-lane-A capture) is
   confirmed at the same order of magnitude on a different Butlers
   revision — the defect is unchanged in kind, and the two captures'
   `workItems`/`codeStructure` shares differ (71.9% pre-lane-A vs
   68.2% here) only because the two revisions' bead and file counts
   differ, not because Syzygy changed.
2. **The credentialed machine channel carries no requirement text; the
   only channel that does is unauthenticated.** Re-verified at
   `a9f671e`: `POLARIS_SOURCE_PATH` (`/polaris/source`) is
   `credentialClass: 'human-open'` (`routes.ts` line 221) and its only
   gate is `browserRequestAllowed` (`browser-origin.ts` lines 24–38),
   which checks the `Host` header's shape and, when present, the
   `Origin` header — no bearer token, no machine-client authentication
   of the kind SEC-1 requires for "non-browser agent and CLI clients."
   A plain `curl` with a correct `Host` header passes it. The two
   `machine-credentialed` routes (`POC_MACHINE_PATH`,
   `POLARIS_PRESENTATION_PATH`, `routes.ts` lines 225–238) require the
   bearer-token check at `packages/cap1-daemon/src/server.ts` lines
   187–200, and neither serves requirement prose: the one
   `switchboard-identity` item in `projectShape.items` carries a
   511-byte record of class, key, state, one anchor
   (`{path, line: 1}`) and the claim tuple — no requirement id, no
   statement text.
3. **The one dispatch artifact in the system is absent from the
   machine payload.** `externalRef`, `governingIntent` and
   `syzygy-poc:work:` occur **0** times in the 5,520,314-byte capture
   [Observed, `str.count` this session, agreeing with the dossier's
   pre-lane-A count]. `buildTrajectoryMaterializationPacket`
   (`materialize-action.ts` lines 30–34) is computed only inside
   `renderMaterializePanel` (lines 55–82), which only `trajectory.ts`
   line 187 calls — the packet is rendered exactly once, as HTML
   `<dd>` elements on the Trajectory page, and reaches `/api/poc`
   nowhere.
4. **The machine payload names zero prohibitions.** The literal
   `mayNot` occurs 0 times; `forbidden` occurs 0 times on this capture
   (3 on the dossier's pre-lane-A capture, all inside Butlers bead
   titles that moved with the catalog — not a Syzygy change);
   `prohibit` occurs 1 time on both captures [Observed, both `str.count`
   this session]. The only scope statement anywhere is
   `projectShape.identity.scope`, which describes what was read
   (`{repositoryId: 'repository:butlers-configured-poc', contentClass:
   'declared-project-shape-text', phase: 'A'}`), never what the
   consumer may do with it.

**A subject-naming finding not in the dossier.** This evaluation's
`proposedWork.changeId` is `repair-whatsapp-identity-reconciliation`
[Observed] — the one Butlers-side OpenSpec change PWB-REQ-013's own
pipeline discovered in the tree at this revision. This is **not** the
same subject as `MATERIALIZATION_EXTERNAL_REF`
(`packages/three-surface-poc-core/src/materialization.ts` line 9:
`'syzygy-poc:work:whatsapp-single-event-normalization'`), the fixed,
hardcoded work item `buildMaterializationPacket` always describes,
which in turn is a different subject again from
`WORKER_CHANGE_INTENT_ID` (`model.ts` line 42:
`'REQ-connector-base-spec-001'`), the intent the worker-change badge
cites. Three distinct, hardcoded-or-observed subjects sit inside one
evaluation. A briefing composed naively — "the subject's proposed work"
— would silently conflate them; slice 3's design (Gate 4) treats them
as three separate lookups and renders "not applicable" rather than
guessing when a selector names a subject none of the three literals
describe.

**Who.** The owner, whose RFC7-30 cold-open walkthrough
(`syzygy-1z3.22`) is one reading level above this; every agent
consuming `/api/poc` to learn what its own work is and what it may not
do, which today it cannot do for any of the four items above; and the
next agent an owner dispatches through the materialize panel, who
today cannot discover from the machine channel that a dispatch is
pending at all.

**Success, falsifiable.**

1. A credentialed `GET /api/poc/briefing?for=<selector>` (once Q1/Q2
   clear) returns, for a subject that exists, a document under its
   declared ceiling composed only of fields independently derivable
   from `/api/poc`'s own bytes at the same evaluation; for a subject
   that does not resolve, a named Unknown, never an empty or
   fabricated briefing.
2. `/api/poc` carries the exact `MaterializationPacket` beside
   `proposedWork`, with a `dispatchState` discriminant
   (`'undispatched'` or `{'dispatched', beadId, at}`), byte-identical
   to what the Trajectory panel renders, asserted by a parity test; a
   test issuing N machine `GET` requests against a fixture state
   directory asserts the directory's bytes are unchanged after the
   Nth.
3. `authority.mayNot` (nested under `projectShape.authority`) is a
   non-empty array whenever an authority evaluation was supplied, each
   row naming its source artifact and act identity; withdrawing one
   authority in a fixture (an `absent` or `invalid` `AuthorityState`)
   makes its corresponding row **harden**, never disappear — the
   fail-closed polarity AGENTS.md records as the project's rule.
4. Zero new epistemic or closed-vocabulary values exist anywhere in
   the implementation that RFC2-10, RFC2-24, RFC2-25 or PWB-REQ-004's
   closed population do not already carry.

**Motif.** *A consumer doctrine names first-class gets a channel with
its own scope, not the whole truth store metered by nothing.* This
extends VIS-1's simplification clause ("comprehension is achieved by
simplifying presentation, never content") to a second reader — an
agent — for whom "presentation" is a byte budget, not a layout.

**What M5 is not.** It is not a new dispatch mechanism: the one write
effect in this corner of the POC, `POST /trajectory/materialize`, keeps
its human trigger and its browser-origin gate unchanged in every slice.
It is not autonomous agent coordination: nothing here lets one agent
read another agent's pending work and act on it without a human click
in between — AGENTS.md's "no unattended agent coordination" and VIS-4's
"the trigger stays human" both hold across all three slices. It is not
a re-opening of the page-size question (M1) or the currency question
(M2): the briefing route composes existing fields, mints no new claim,
and touches no `data-epistemic-*` attribute anywhere. It does not
generalize RFC8-21's chain to arbitrary subjects — the chain's own
relationships are fixed literals in `model.ts` today (see the
subject-naming finding above and Gate 4 slice 3), and this move does
not change that architecture, only discloses "not applicable" honestly
when a selector names a subject none of them touch.

## Measurements on the retained capture

All computed this session from `api-poc.json`
(5,520,314 bytes; sha256
`a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e`;
Butlers evaluation revision `2e3bac97790b`, the retained lane A "after"
capture at
`scratchpad/m1/measure/after/`) unless marked otherwise. sha256
verified against the M4 packet's own table before use, and against the
M2 evidence file's `polaris-tailnet.html` hash, both matching
[Observed].

### Bytes per top-level key (compact re-serialization, method: `json.dumps(v, separators=(",", ":"))` per key, summed against the whole file's own compact size)

| Key | Bytes | Share |
|---|---:|---:|
| `workItems` | 2,273,467 | 41.18% |
| `projectShape` | 1,657,461 | 30.02% |
| `codeStructure` | 1,493,219 | 27.05% |
| `trajectory` | 80,130 | 1.45% |
| `entities` | 4,899 | 0.09% |
| `relationships` | 4,547 | 0.08% |
| `orrery` | 2,588 | 0.05% |
| `proposedWork` | 2,278 | 0.04% |
| `surfaces` | 1,440 | 0.03% |
| `evaluation` | 595 | 0.01% |
| `walkthroughReadiness` | 322 | 0.01% |
| `walkthroughJudgment` | 291 | 0.01% |
| `project` | 106 | 0.00% |
| `testArtifactVerification` | 103 | 0.00% |
| `workerChange` | 87 | 0.00% |
| `observerRevision` | 42 | 0.00% |
| `capabilityId` | 40 | 0.00% |
| `schema` | 29 | 0.00% |
| `materializedBeadId` | 4 | 0.00% |

Sum of per-key compact sizes, 5,521,648 bytes, against the whole file's
own compact serialization, 5,521,960 bytes — the 312-byte gap is
key-name and separator overhead double-counted across the per-key
sweep, immaterial to the shares above.

### The briefing an agent needs, two denominators

| Set | Bytes | Share |
|---|---:|---:|
| Minimal orientation (14 fields listed in Gate 1, one compact object) | 18,719 | 0.339% |
| …dossier's own figure, pre-lane-A capture (5,508,208 bytes) | 18,710 | 0.340% |
| …plus `projectShape.classes` and `projectShape.claim` | 148,815 | 2.695% |
| …dossier's own figure, pre-lane-A | 148,785 | 2.70% |
| A realistic **one-claim** briefing (`claim:baseline-spec:switchboard-identity`: evaluation identity, consent scope, full authority block, the claim's own tuple, its one matching source, one exact-source route, an RFC8-21 chain marked not-applicable; `mayNot` not yet built) | 2,829 | 0.051% |

The one-claim figure is a new measurement, not in the dossier: it is
the shape slice 3's oracle must hold to, and it shows the recommended
20 KB ceiling (Q2) has roughly sevenfold headroom over a realistic
single-claim payload — a safety margin, not a tight budget.

### Literal-substring counts (method: `str.count`, two runs agreeing)

| Substring | This capture | Dossier's pre-lane-A capture |
|---|---:|---:|
| `externalRef` | 0 | 0 |
| `governingIntent` | 0 | 0 |
| `syzygy-poc:work:` | 0 | 0 |
| `mayNot` | 0 | not measured (field did not exist) |
| `forbidden` | 0 | 3 (Butlers bead titles) |
| `prohibit` | 1 | 1 |
| `materializedBeadId` | 1 (the key; value is `null`) | 1 |

### `projectShape.counts` and `authority`, this evaluation

| Field | Value |
|---|---|
| `counts.sources` / `.items` / `.facts` / `.exclusions` | 278 / 415 / 439 / 9 |
| `authority.authorizationMode` | `owner-trusted-bootstrap` |
| `authority.authorities[].state` (all three) | `owner-adopted (bootstrap, uncorrelated)` |
| `authority.authorities[].independentlyVerified` (all three) | `false` |
| `authority.authorities[].actIdentity` | `PWB-BUTLERS-OBSERVATION-CONSENT-2026-09-02`; `PWB-SECRET-CLASSIFICATION-POLICY-APPROVAL-AMENDMENT-2026-09-05`; `PWB-OBSERVER-REGISTRY-ENTRY-ADOPTION-AMENDMENT-2026-09-05` |
| `identity.scope` | `{repositoryId: 'repository:butlers-configured-poc', contentClass: 'declared-project-shape-text', phase: 'A'}` |
| `proposedWork.changeId` | `repair-whatsapp-identity-reconciliation` |
| `proposedWork.currentAuthority.kind` / `.key` | `baseline-spec` / `switchboard-identity` |

### Route table, re-verified at `a9f671e` (`routes.ts`)

| Route | Credential class | Gate |
|---|---|---|
| `/`, Polaris, Trajectory, Orrery (direct + tailnet) | `human-open` | `browserRequestAllowed`: `Host` shape + optional `Origin` match |
| `/polaris/source` (direct + tailnet) | `human-open` | same — no bearer token |
| `/api/poc` (direct + tailnet) | `machine-credentialed` | bearer token, `packages/cap1-daemon/src/server.ts` lines 187–200 |
| `/api/poc/polaris` (direct + tailnet) | `machine-credentialed` | same bearer-token check |

### Line numbers re-verified at `a9f671e` (all files byte-identical to `f4589e2`)

| Citation | At `a9f671e` | Dossier said | Note |
|---|---|---|---|
| `routes.ts` `machineHandle` | 159–162 | 159–162 | holds |
| `routes.ts` `POLARIS_SOURCE_PATH` route registration | 221 (222 tailnet) | 196–200, 222–223 | **196–200 is `humanSurfaceRoutes`'s internal handle closure, a different route family (Trajectory/Orrery), not `POLARIS_SOURCE_PATH`'s own registration**; 222 is the tailnet variant, 223 is the next line's `...humanSurfaceRoutes(TRAJECTORY_...)` spread, not a `POLARIS_SOURCE_PATH` line |
| `routes.ts` `machine-credentialed` route block | 225–238 | 232–239 | the dossier's range starts inside the block (missing `POC_MACHINE_PATH`'s own direct registration at 225–229) and ends one line past the last route row (239 is outside the returned array) |
| `browser-origin.ts` `browserRequestAllowed` | 24–38 (file ends at 38) | not cited by line | — |
| `materialize-action.ts` `MATERIALIZE_HUMAN_PATH` | 17 | 17 | holds |
| `materialize-action.ts` `renderMaterializePanel` | 55–82 | 55–80 (dossier); 55–81 (form/button) | the function's closing brace is line 82; 78–80 is the form/button pair, correct as far as it goes |
| `materialization.ts` `MaterializationPacket` | 24–29 | not cited by line | — |
| `materialization.ts` `buildMaterializationPacket` | 41–64 | not cited by line | — |
| `model.ts` `PocEpistemic` | 44–46 | not cited by line | — |
| `model.ts` `PocModel` interface | 98–155 | not cited by line | — |
| `body-read-authority.ts` `BodyReadAuthorityEvaluation` | 315–324 | not cited by line | — |
| `authority-disclosure.ts` `AuthorityDisclosure` | 39–46 | not cited by line | — |
| `project-shape-observation.ts` `PwbResourceLimits` / `PWB_RESOURCE_LIMITS` | 65–73 / 75–83 | not cited by line | `maxHumanResponseBytes` 81 (2,097,152); `maxMachineResponseBytes` 82 (8,388,608) |

## Gate 2 — Doctrine

Cited by identifier and quoted from the defined location (rule 8).

**VIS-1 — Comprehensible truth first** (`vision.md` lines 82–94, quoted
in the Motif section above by its "simplify presentation, never
content" clause). This move's whole warrant: an agent's presentation
is a byte budget as much as a human's is a layout, and the same rank
order applies — rank 1 (truth and observation determinism) is
untouched; the briefing composes, never mints, facts.

**"Two first-class consumers from day one"** (`vision.md` lines 39–41,
quoted in full in Gate 1). This is the doctrine sentence L5-M1's own
"Why" cites; it is unnumbered prose, not a `VIS-n` rule, and is cited
here as context for VIS-1 and VIS-4, never as an independent authority
(AGENTS.md: "Cite by identifier").

**"Not a documentation portal"** (`vision.md` lines 61–64): "Rendering
and drafting governance artifacts is a means; the escape property is
that intent changes produce dispatched work. A Syzygy from which no
work is ever dispatched has failed, regardless of how good its
documents look." Slice 1 is this sentence turned into a machine-visible
fact: today the dispatch packet exists only where a human eye can find
it.

**VIS-4 — Humans steer the vision; agents shape within it** (`vision.md`
lines 122–139). No slice moves the write boundary: `POST
/trajectory/materialize` keeps its human trigger and its
`browserRequestAllowed` gate in every slice; nothing here lets an agent
call it. Drafting the Q1 spec-delta sketch (Gate 5) is drafting, never
adoption, per this rule and per VIS-3.

**VIS-5 — Syzygy never writes code; direct writes are confined to two
namespaces** (`vision.md` lines 141–165). Every slice is a read: no
slice writes to Butlers, to `openspec/**`, or to `.syzygy/**` at
runtime. The Q1 spec-delta sketch below, if the owner authorizes
drafting it, would itself be committed only into `.syzygy/**` or
`openspec/**` as a governance artifact — never as implementation code —
exactly as this rule requires.

**SEC-1 — Authenticated by default** (`security.md` lines 10–23):
"non-browser agent and CLI clients are admitted only through an
explicit machine-client authentication mechanism." This is the exact
gap L5-F2 names: `POLARIS_SOURCE_PATH` has no such mechanism (only the
`Host`/`Origin` check any browser satisfies), while the two
`machine-credentialed` routes do. Slice 3 rides the same mechanism;
it adds no new authentication surface.

**SEC-3 — Observed code is untrusted, everywhere** (`security.md`
lines 39–45). Not directly reached by this move — no slice executes
observed code — but it is the doctrine ground for the "no unattended
agent coordination" language slice 1's dispatch-state discriminant is
careful not to violate: an agent may *read* that a dispatch is
pending; nothing in this move lets it *trigger* one.

**PWB-REQ-005 — Consent and policy authority precede every body read**
(`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
lines 202–271, quoted in relevant part): "Every human and machine
rendering of the authorization basis and every dependent body-derived
result SHALL expose each authority's exact state. Only state (2) MAY
be called independently verified. State (1) SHALL render exactly:
`Owner-trusted only; same-tree forgeable from Syzygy's perspective.
Digest detects drift, not authorship or attendance.`" This is the
clause `AuthorityDisclosure` (`authority-disclosure.ts`) already
implements exactly, and it is the ground for slice 2: `mayNot` is a
new field on the same disclosure object this requirement already
governs, not a new authority mechanism.

**PWB-REQ-013 — Proposed work stays subordinate to current project
truth** (cited by its own file header comment,
`packages/three-surface-poc-core/src/proposed-work.ts` lines 8–19,
since the register does not carry a spec-requirement family and the
requirement's own heading was located by sweep). `ProposedWork` is
already "described here as a distinct machine type, never as a
project-account statement or a catalog item." Slice 1's dispatch
packet is a **different** artifact from `proposedWork` — see the
subject-naming finding in Gate 1 — and is proposed as its sibling on
the model, never merged into it, so PWB-REQ-013's subordination
property is undisturbed.

**PWB-REQ-020 — Project-wide facts remain identical across human and
machine views** (spec lines 902–927, quoted in full):

> Every project-shape identity, statement, source anchor, coverage
> state, denominator, contradiction, body-read authority state and
> walkthrough-judgment state or disclosure Polaris presents SHALL be
> recoverable from the same evaluation in the machine answer,
> preserving multiplicity and exact provenance state.
>
> — **Observable**: both populations contain equivalent multisets.
> — **Falsifier**: one fact, authority state, judgment state or
>   disclosure is missing, duplicated, changed, collapsed or
>   associated with a different evaluation in either channel.

`mayNot` rows are a form of "body-read authority state" disclosure
under this Case's own enumeration, so PWB-REQ-020 reaches them
directly: they must render on the human surface too, not only on
`/api/poc`, or the Falsifier's "missing... in either channel" fires.
Slice 2's own design already renders them from one field for exactly
this reason (Gate 4).

**RFC8-21 — The change-accounting chain**
(`.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`
lines 79–91, quoted): "Trajectory must walk, in both directions, the
chain: **warrant (normative reference or Decision) → approved plan
item (execution-intent Proposal) → materialization record → work item
→ execution run(s) → commits/PR → merge fact → reconciliation
verdict**... Against today's actuator toolchain this chain is honest
but thin: several links resolve only by naming convention... That
thinness must render as thinness, and must never be presented... as a
chain awaiting completion rather than one that is complete and weak."
This is the exact chain L5-M1's "chain state for the subject" names.
As Gate 1's subject-naming finding shows, today's model wires this
chain over three fixed, hardcoded literals
(`WORKER_CHANGE_SEAM`/`WORKER_CHANGE_INTENT_ID`,
`MATERIALIZATION_EXTERNAL_REF`, and `proposedWork`'s dynamically
observed `changeId`), not generally over "whatever the selector
names." Slice 3 must therefore render the chain as **not applicable**
for a subject none of the three literals touch (a `baseline-spec`
catalog claim, for instance), per RFC8-22's "a broken join renders; it
is never silently skipped" — a subject with no chain relationship
gets an explicit "not applicable," never a fabricated eight-link
Unknown ladder.

**RFC6-14 — Label parity**
(`.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`
lines 237–249, quoted in relevant part): "Every entity and claim
instance in a machine answer carries its epistemic state verbatim from
the RFC 0002 vocabulary." The briefing composes existing tuples
verbatim; it re-labels nothing.

**RFC6-22 — The equivalence definition** (same file, lines 390–402,
quoted): "Two renderings... are equivalent iff they present: the same
evaluation identity, the same declared filters, the same underlying
graph..., the same epistemic states..., the same sibling surface
states..., the same challenge-pending disclosure..., and the same
chain state... Equivalence is over semantics and query results, never
over pixels." This is the ground for slice 3's own oracle: a briefing
is a *query result* over the same graph `/api/poc` already carries, so
every field it renders must be independently checkable against
`/api/poc`'s own bytes — never a second, divergent truth store.

**Conflict check.** None found. Every slice discloses a fact the model
already holds; none turns anything green, none claims independent
verification where state (1) applies, and slice 2 can only make a
constraint more visible, never less — the same "may only degrade,
never improve" direction `architecture.md` states for currency applies
here by extension to disclosure completeness [Inferred].

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Dispatch packet + state | `packages/three-surface-poc-core/src/model.ts` (a `dispatch` field beside `proposedWork` in the `PocModel` interface, ~line 140, and in `buildModel`'s returned object, ~line 700); `apps/three-surface-poc/src/routes.ts` (no route change — the existing `machineHandle` already serializes the whole model); a new parity test comparing Trajectory's `data-parity-field="materialize-*"` markers against the new field | none |
| 2 `mayNot` | `packages/three-surface-poc-core/src/authority-disclosure.ts` (a `mayNot` field on `AuthorityDisclosure`, populated from the three already-parsed `AuthorityState`s plus a hand-typed, registration-guarded table of the implementation-authorization act's "What this does not authorize" bullets); `apps/three-surface-poc/src/polaris.ts` (render the same field on the page, per PWB-REQ-020) | none |
| 3 Briefing route | a new module in `apps/three-surface-poc/src/` (e.g. `polaris-briefing.ts`) composing the fields named in Gate 1's success criteria; `apps/three-surface-poc/src/routes.ts` (one new `machine-credentialed` route, `GET /api/poc/briefing`); `packages/three-surface-poc-core/src/project-shape-observation.ts` (`maxBriefingResponseBytes` on `PwbResourceLimits`, contingent on Q2) | **contingent on Q1/Q2: the adapter-registry entry, if Q2 mints a new ceiling; the PWB or POC specification, per Q1** |
| 4 (deferred) Path and change selectors | not designed here | not designed here |

Boundaries crossed: none new for slices 1–2. `three-surface-poc-core →
cap1-daemon` (the `Route`/credential-class types) already carries the
`machine-credentialed` vocabulary slice 3 would reuse, so a new route
under it is a use of an existing boundary, not a new one — the
registry/spec question in Q1/Q2 is about the *content* the route
serves and the *ceiling* it declares, not about a new architectural
edge.

Not touched by any slice: the body-read authority gate itself (only
its already-computed output is read), the observation pipeline's
classification and extraction stages, `POST /trajectory/materialize`'s
handler or its browser-origin gate, the consent act's pair and content
class, and — for slices 1 and 2 — every digest-bound spec and registry
artifact.

### The authorizing act, per slice

| Slice | Owner act needed | Named act, and the trigger test |
|---|---|---|
| 1 Dispatch packet | **No** | Rides `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` (2026-09-05). No escalation trigger of `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (lines 86–94) is crossed: the packet is already computed from `model.project.root` and fixed artifact paths, with zero new observation; no PWB spec amendment (PWB-REQ-013 already types this exact artifact); no registry-envelope change (`maxMachineResponseBytes`, 8,388,608 bytes, comfortably covers a ~2.3 KB packet addition — see Gate 1's per-key table); no route added |
| 2 `mayNot` | **No**, with one implementation note | Same continuation. The three `AuthorityState`s are already daemon-computed; no new observation. The fourth source — the implementation-authorization act's own prose bullets, which the daemon does not parse at runtime — is proposed as a hand-typed, closed table, in the shape of `UNKNOWN_REASON_ROUTES` (`project-shape-model.ts` lines 89–102). Per AGENTS.md's own governance-recorder ritual ("register a new act phrase... before the packet exists, or CG-7d cannot see them go stale"), this table's entries should be registered the same way so an amendment to that act is caught, not silently stale — a Gate 6 engineering-bar item, not an escalation trigger |
| 3 Briefing route | **Yes, per Q1; and per Q2 if the ceiling is minted** | No act found that authorizes a new machine-credentialed route as read; the escalation trigger is "any scope beyond the signed change" (`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` line 93) together with this packet's own reading of the POC spec's reader note (Gate 5) |
| 4 (deferred) | not evaluated | not evaluated |

P-52 is untouched: all slices run under `syzygy-dov.5`, the pursuit
bead, so no ninth POC bead is filed.

## Gate 4 — Design sketch, per slice

### Slice 1 — Dispatch packet and state beside `proposedWork` (medium; no act)

`PocModel` gains a `dispatch` field, a sibling of `proposedWork` (not a
member of it — see the subject-naming finding), typed:

```
interface DispatchDisclosure {
  readonly packet: MaterializationPacket; // buildTrajectoryMaterializationPacket's exact output
  readonly state:
    | { readonly kind: 'undispatched' }
    | { readonly kind: 'dispatched'; readonly beadId: string; readonly at: string };
}
```

`buildModel` computes it once, from the same
`buildTrajectoryMaterializationPacket(model)` call `renderMaterializePanel`
already makes, and from `currentMaterializedBeadId(model)` /
`readMaterializationRecordFile` for the state's `beadId`/`at` fields
(the record already carries `createdAt`, `materialization.ts` lines
67–76). `renderMaterializePanel` is refactored to read
`model.dispatch.packet` instead of recomputing it, so the two channels
cannot diverge by construction — the same discipline `authority-disclosure.ts`
already applies to authorization text.

**Nothing is written on `GET`.** `buildTrajectoryMaterializationPacket`
is already a pure function of `model.project.root` and two fixed
paths; `currentMaterializedBeadId` already only reads
`model.materializedBeadId`. Adding `dispatch` to the model changes
nothing about how or when the model is built — `buildModel` is called
at startup and again only on `POST /trajectory/materialize`
(`main.ts`, unchanged by this move), never inside `machineHandle`.

**Test.** A fixture state directory, `GET /api/poc` issued five times
against a private daemon, asserted byte-identical before and after
(the directory's `mtime`s and contents unchanged) — the counterexample
the dossier names. A parity test in the shape of
`polaris-parity-sweep.test.ts` but scoped to `trajectory.html`,
comparing the seven `data-parity-field="materialize-*"` values (target
repo, governing intent, title, description, labels, type/priority,
external ref — already rendered today, `materialize-action.ts` lines
69–75) plus the `materialize-status`/`materialize-trigger` pair against
`model.dispatch.packet` and `.state` by field, reporting both
denominators; today no such test exists (only `materialize-action.test.ts`
checks the panel's own render, with no machine-channel counterpart).

**Rule-6 mutants.** Change one packet field in the model (e.g. mutate
`title`) and confirm both the new parity test and `materialize-action.test.ts`
fail; flip `dispatch.state.kind` without a matching `materializedBeadId`
and confirm a consistency assertion fails; issue a `GET` after
mutating the state-directory read path to (incorrectly) write a
placeholder file, and confirm the byte-identity test catches it.

### Slice 2 — `authority.mayNot` (medium; no act)

`AuthorityDisclosure` (`authority-disclosure.ts` lines 39–46) gains:

```
readonly mayNot: readonly {
  readonly id: string;              // e.g. 'no-write-to-observed-repository'
  readonly statement: string;       // the exact prohibition, human-readable
  readonly actIdentity: string;     // which act/artifact it comes from
  readonly artifactDigest: string | undefined; // present for the three parsed authorities; absent for the hand-typed source
}[];
```

Two sources feed it. **(a)** The three `AuthorityState`s
`discloseAuthority` already computes: a `valid` registry state whose
underlying JSON declares `writeSurface: []` and `executeObservedCode:
false`
(`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
lines 125 and 128, already validated by `body-read-authority.ts` lines
677–684) yields a row citing that authority's own `actIdentity` and
`artifactDigest` — zero new reads, since the daemon already holds
these values. **(b)** The implementation-authorization act's own "What
this does not authorize" bullets (`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`
lines 68–84: no write/egress/execution/deployment/release/recovery/
mission effect on Butlers or any other repository; no second
repository or wider content class; no doctrine or contract change; no
autonomous intent adoption; no Syzygy-authored implementation code; no
unattended agent coordination) are proposed as a hand-typed, **closed**
table in the shape of `UNKNOWN_REASON_ROUTES` — each row carries
`actIdentity: 'PWB-IMPLEMENTATION-AUTHORIZATION-ACT'` and
`artifactDigest: undefined` (the act's digest is never quoted in this
table or in this packet, per AGENTS.md's guardrail against quoting a
performed act's argument outside `ACT_DIGEST_COPY_FILES`; the row
cites the record by path). Per Gate 3's engineering note, this table's
entry count should be registered wherever `check_governance.py` would
notice the source act change (a new function alongside
`_act_subjects()`, or a dedicated fixture asserting the table's row
count against a fresh read of the act file's bullet count) so an
amendment to the act cannot silently leave `mayNot` stale.

**Render on both channels from one field**, per PWB-REQ-020 (Gate 2):
`polaris.ts`'s existing authority-disclosure block gains a `mayNot`
list, sourced from the same `AuthorityDisclosure.mayNot` the machine
channel serves — no second copy of the prohibition text.

**Test.** A fixture with all three authorities `valid` asserts three
rows plus the fixed table's rows, non-empty. A fixture with the
registry authority `absent` (per `AuthorityState`'s `absent` arm)
asserts the registry-derived row's text **hardens** — e.g. from "the
registry declares an empty write surface" to "no registry act is in
force; assume the broadest prohibition until one exists" — never
disappears, per the counterexample named in success criterion 3.

**Rule-6 mutants.** Delete one row from the hand-typed table and
confirm the row-count registration check fails; flip one authority
from `valid` to `invalid` and confirm the corresponding row's text
changes and the array does not shrink; render the page and the machine
answer from two different builds of the same evaluation and confirm
the parity test catches a diverged `mayNot` list.

### Slice 3 — `GET /api/poc/briefing?for=<selector>` (large; act per Q1/Q2)

Contingent on Q1 and Q2. The route accepts exactly one selector form at
first cut, `for=claim:<claimId>` (query-parameter handling already
precedented by `SOURCE_IDENTITY_PARAM`,
`apps/three-surface-poc/src/polaris-source.ts` lines 33 and 41–42), and
composes, for the named claim:

- the evaluation identity (`snapshot`, `asOf` — a subset of what
  `/api/poc` already carries, never re-derived);
- `identity.scope` (consent scope, verbatim);
- `authority` in full, including `mayNot` (slice 2);
- the claim's own tuple, from `projectShape.items`/`.facts`/`.classes`
  by id;
- an RFC8-21 chain state for the subject: **`not-applicable`** with a
  named reason when the subject is not one of the three hardcoded
  work-related literals (Gate 1's subject-naming finding), or the
  relevant relationships' epistemic states by id when it is;
- every Unknown touching the subject (its own claim if Unknown; any
  relationship or entity naming it, once M4 lands with routes on all
  22, or with today's free-prose reasons if it lands first — Q4);
- exclusions touching the subject's anchors, by path;
- the exact-source route for each cited requirement, built with the
  existing pure `sourceRouteHref(mountPrefix, identity)`
  (`polaris-source.ts` lines 41–42) — no new URL-construction logic.

An unresolvable selector (a `claimId` absent from every population)
renders a named Unknown — `{kind: 'unknown', reason:
'no-such-claim', subject: <the raw selector>}` — never an empty
document, matching success criterion 1.

**Ceiling.** Served through `boundedResponse`
(`routes.ts` lines 111–121, already generic over which
`ResponseLimitIdentity` and `PwbResourceLimits` field it is passed) with
`maxBriefingResponseBytes` if Q2 mints it, or `maxMachineResponseBytes`
as the interim hard bound with a test-only 20 KB assertion if not
(Q2's default). Either way, the measured one-claim figure (2,829 bytes
for `claim:baseline-spec:switchboard-identity`, Gate 1) is published
alongside the ceiling as the requirement's denominator, in the M1/M2
shape.

**Oracle.** Every field the briefing renders must be independently
derivable from `/api/poc`'s own bytes at the same evaluation — a test
walks both, by field, and fails if the briefing states anything
`/api/poc` does not already carry (RFC6-22's equivalence definition,
Gate 2). This forecloses the briefing ever becoming a second truth
store, the same discipline M2 slice 2's currency probe and M4 slice 2's
machine route form both apply to their own additions.

**Trade-offs rejected.** Accepting `for=path:` or `for=change:` now
(deferred to slice 4 — RFC8-21's chain and the exact-source route both
need a stable claim identity to key off, and only `claimId` is
guaranteed stable per PWB-REQ-007-adjacent identity rules; a path or
change selector would need its own resolution step this packet does
not design); folding the briefing into `/api/poc/polaris` (that route
is explicitly "never... part of `/api/poc`" and a presentation
artifact, `polaris-narrative.ts` lines 193–198 — a briefing is neither);
letting the briefing accept an authority override or a wider content
class (SEC-1/PWB-REQ-005 apply unchanged; the briefing composes,
never widens, what the evaluation already admits).

### Slice 4 — Path and change selectors (deferred)

Not designed here. The dossier's own slice plan places it "after"
slice 3, and this packet agrees: it needs a resolution mechanism
(mapping a path or change id to the claim identities that touch it)
this packet has not built or measured. Re-enter this funnel once slice
3 is measured against real traffic shapes.

### Design bar for the human surface

No new interaction beyond slice 2's `mayNot` list, which renders as
plain text beside the existing authority-disclosure block — no new
`<details>`, no fragment target inside one, keyboard paths unaffected,
direct/tailnet parity unaffected, the no-JS path unaffected (nothing
here is client-scripted). The dispatch packet's *existing* rendering
(the Trajectory panel) is unchanged in appearance; slice 1 only
refactors where its data comes from.

## Gate 5 — Specification

**Slices 1 and 2: no spec delta.** PWB-REQ-013 already types the
dispatch packet's subject matter as "described here as a distinct
machine type"; serving it as a sibling field on the existing `/api/poc`
adds no new route, no new credential class, and no new project fact
(PWB-REQ-004's closed population is untouched — the packet is not a
project-shape claim). PWB-REQ-020 already *requires* `mayNot` to
render on both channels once it exists, per Gate 2's reading; adding
the field is conformance with a Case this requirement's own text
already reaches, not an amendment to it.

**Slice 3: a spec delta is needed, per this packet's reading of the
POC spec's reader note and per the rule stated in this move's own
brief — a new route in a signed spec is a spec delta through CC-REV-2,
and that determination is an owner question, never a plan step (Q1).**
Two candidate shapes, neither drafted to package form here (that is
the point of Q1 — which spec, and whether to draft at all, is the
owner's call):

- **PWB delta (recommended).** Add a short paragraph near PWB-REQ-020
  naming a closed category, "derived read-only machine view": composed
  only of fields reachable from `/api/poc` at the same evaluation,
  oracle-verified as derivable, served under its own declared ceiling.
  Retroactively names `/api/poc/polaris` as the first instance and
  `/api/poc/briefing` as the second. **Stable IDs affected:** none
  minted; a clarifying paragraph near PWB-REQ-020, not a new
  requirement. **Change class:** clarifying (it names an existing,
  unspec'd pattern; it does not change what any requirement's Case,
  Observable or Falsifier already says). **What explicitly does not
  change:** PWB-REQ-004's closed project-fact population; PWB-REQ-020's
  equal-multiset Observable; every existing route's credential class or
  ceiling.
- **POC delta (the cheaper alternative).** Widen the reader note at
  spec line 26 from "the 'machine answer' is the authenticated `GET
  /api/poc` response" to name a family of derived views under the same
  authentication and equivalence discipline. Touches one sentence of
  scaffolding prose, not a numbered requirement.

Either way: **review required** — a fresh-context spec review before
any owner act, per the project's own review discipline; the act, if
the PWB shape is chosen, in the 2026-09-05 continuation shape once the
delta is queued and ruled.

### New WHEN/THEN scenarios (for the beads' acceptance contract, not the spec)

**S1 — The briefing is a bounded query, never a second truth store.**
WHEN `GET /api/poc/briefing?for=claim:<id>` is served for an existing
claim, THEN every field in the response is independently derivable
from `/api/poc`'s own bytes at the same evaluation, AND the response
fits its declared ceiling.

**S2 — An unresolvable subject is a named Unknown.** WHEN the selector
names no claim in any population, THEN the response is
`{kind: 'unknown', reason: 'no-such-claim', subject: <selector>}`,
never an empty or partial briefing.

**S3 — A GET never writes.** WHEN `GET /api/poc` or `GET
/api/poc/briefing` is issued any number of times with no intervening
`POST /trajectory/materialize`, THEN the state directory's bytes are
unchanged.

**S4 — The dispatch packet cannot diverge across channels.** WHEN the
Trajectory panel and `/api/poc`'s `dispatch.packet` are read from one
evaluation, THEN every one of the packet's seven fields matches by
value, AND a test asserts both denominators.

**S5 — Withdrawing an authority hardens `mayNot`, never empties it.**
WHEN one of the three authorities moves from `valid` to `absent` or
`invalid`, THEN its `mayNot` row's text changes to the stricter form
and the array's length does not decrease.

**S6 — A subject with no RFC8-21 relationship gets an honest
"not applicable."** WHEN the briefing's subject touches none of the
three hardcoded work-related literals, THEN the chain field renders
`{kind: 'not-applicable', reason: ...}`, never a fabricated eight-link
Unknown ladder.

## Collision and sequencing

**With M2 (`syzygy-dov.2`, register row P-69, PR #36).** M2's slice 3
adds an `evidence` block as a sibling of `evaluation` inside `model.ts`
and inside `routes.ts`'s handling of `/api/poc` and `/api/poc/polaris`,
for the same reason M5 slice 1 adds `dispatch`: both grow the
`PocModel` interface and both grow `machineHandle`'s serialized output
with a new sibling field, and both must land in the same parity
denominator rather than forking it. **No line range overlaps**: M2's
own Gate 3 table cites `model.ts`'s "evaluation block" for its
`currencyProbe`/`evidence` additions, distinct from `PocModel`'s
`proposedWork`/`dispatch` region this packet edits (interface lines
~139–140, `buildModel`'s return ~line 700) — adjacent, not
overlapping, in the same shape M4 already found for its own overlap
with M2's `project-shape-model.ts` edit. Land either first; a merge
conflict, if any, is a two-line hunk in one interface and one return
statement, not a semantic collision.

**With M3 (the honest-encoding-at-the-gate packet, register
row P-70; not present on this worktree's own branch).** M3's slices touch `polaris-copy.ts` and `polaris.ts` lines
346–361 (`claimStatesBlock`) to build the tier/freshness/challenge
encoding tables. M5 slice 2 touches `polaris.ts`'s authority-disclosure
block to add `mayNot` — a different function, a different concept
(prohibitions, not epistemic-state encoding). No file overlap with
M3's core edits is expected beyond both packets touching `polaris.ts`
in different regions; re-check the exact function boundaries once
either lands, in the style M4 already recommends for its own M3
overlap.

**With M4 (the owner-loop packet, branch
`agent/syzygy-dov.4`, would queue as P-71; not present on this
worktree's own branch).** The real dependency is
conceptual, not textual: M4 slice 1 widens `PocEpistemic`'s Unknown arm
with a closed RFC2-24 reason and a route for the nine currently
routeless disclosures (`model.ts` line 305's `unknown()` constructor
and the entity/relationship literals near lines 562–616); M4 slice 2
widens `ResolutionRoute` to `{reason, prose, actor, verb, target}`
(`project-shape-model.ts` lines 115–118, 150–154). M5 slice 3's
briefing *reads* exactly these same structures to compose "every
Unknown touching the subject with its route" (Gate 1's success
criteria). **No file lines actually collide** — M5 slice 3 lives in a
new module and a new route registration, not inside `model.ts`'s
`PocEpistemic` declaration or `project-shape-model.ts`'s
`ResolutionRoute` type — but the *richness* of what slice 3 can render
depends on M4's landing order, which is exactly Q4's subject. Also
worth naming: M5 slice 1's `dispatch` field and M4's routed-Unknown
work both eventually touch the same `capability:whatsapp-transport-identity`
detail region a reader might expect to see on one screen (M4's
`actionRoute` on `relationship:intent-to-work` already points at "the
materialize panel — the one lawful action that exists," per M4's own
Gate 4 slice 1) — no code overlap, but the two moves' end states are
complementary: M4 routes the reader *to* the materialize panel; M5
makes that panel's contents visible on the machine channel too.

**With lane B (`agent/syzygy-dov.17`, register row P-68, a PWB
semantic-delta package for scoped attributes on the human-channel
claim tuple).** No collision on the recommended answers: `mayNot` and
`dispatch` are not claim-tuple fields (`data-evaluation-id`,
`data-epistemic-*`), so lane B's hoisting mechanism does not reach
them, and slice 3's briefing renders complete tuples, never a hoisted
scope. **A real collision arises only if Q1 is ruled toward the PWB
delta**: lane B's package is already open against the digest-bound
PWB spec, and per the manifest-binding mechanics M2's own collision
section states ("a second package drafted concurrently against the
same pre-amendment bytes could not be performed after the first"), a
PWB delta for M5 would have to **queue behind lane B**, exactly as M2
and M3 already must. If Q1 is instead ruled toward the cheaper
POC-spec reader-note widening, no such queueing applies — a further,
practical argument for that arm beyond the one stated in Q1's own row,
worth the owner weighing alongside the "close the gap once, for both
routes" argument the recommendation makes.

**The order.** (1) Land slices 1 and 2 now — they touch no governed
artifact, collide with nothing above beyond adjacent-not-overlapping
file regions, and slice 2 alone closes the "zero prohibitions" finding
(L5-F9) VIS-1/SEC-1 already warrant. (2) Rule Q1; if a PWB delta is
chosen, queue it behind P-68 (lane B) per the one-manifest-at-a-time
rule; if a POC delta is chosen, it may proceed independently. (3) Once
Q1 clears, rule Q2 and Q3, then build slice 3, in either order
relative to M4 (Q4) since the oracle self-corrects. (4) Re-enter this
funnel for slice 4 once slice 3 is measured against real traffic
shapes.

## Gate 6 — Engineering bar

Acceptance, in the M1/M2/M4 shape:

1. **Retained measurement, before and after**, direct and tailnet host
   forms, at a named Syzygy commit and Butlers revision, in
   `docs/evidence/`, from a private daemon on port 0 with its own
   state directory, never the loopback daemon, on a committed clean
   tree. The M5 numbers to record: `dispatch`/`mayNot` byte cost added
   to `/api/poc` (both well under the 8,388,608-byte
   `maxMachineResponseBytes` headroom shown in Gate 1's per-key table);
   the briefing route's measured size for at least three real subjects
   (a `baseline-spec` claim, a `topology-component` claim, and — once
   M4 lands or with today's free-prose reasons — a relationship claim)
   against its declared or interim ceiling.
2. **Every M1 invariant equal before and after**: claim id set, item
   and source populations, fragment targets with zero dangling, and
   the mount-prefixed link count. `dispatch`, `mayNot` and the
   briefing route add fields and a route; they change no existing
   claim.
3. **Rule-6 mutation evidence for every new guard branch**: the
   byte-identity-after-N-GETs counterexample (slice 1); the
   `mayNot`-hardens-on-withdrawal invariant (slice 2); the
   registration check tying the hand-typed table to the act's own
   bullet count (slice 2); the briefing's derivability oracle, the
   ceiling breach, the unresolvable-selector Unknown, and the
   not-applicable chain state (slice 3). Each mutant's `old`/`new`
   fragment and the commit it ran at are recorded, per the evidence
   rule.
4. **Both a Trajectory-scoped parity test (new, slice 1) and the
   existing Polaris parity sweep**, extended to `mayNot`, each with
   both denominators, per-tuple against the machine claim by id.
5. **Preflight populations, keyboard, no-JS and browser tests**, the
   app suite twice and the full suite pass; `tsc -b
   packages/three-surface-poc-core` before the app typecheck.
6. **Independent review in fresh context** before close, raw retained
   as a `-RAW.md` file; for slice 3, an independent review of the
   spec-delta package (whichever shape Q1 selects) *before* any owner
   act, in the 2026-09-05 packet shape.
7. **Conformance expected values hard-coded**, never imported from the
   module under test; every new label distinctive enough that a
   substring match cannot succeed by coincidence.

## Funnel summary

```
## Feature Request: M5 - The agent's briefing: a task-scoped route, the dispatch packet and the prohibitions on the machine channel
Size: medium (slices 1-2) / large (slice 3, pending Q1); slice 4 deferred
Baseline: Syzygy a9f671e; capture = lane A after, api-poc.json 5,520,314 bytes
- G1 Motif: agent orientation is 0.339% of the payload (18,719 of
  5,520,314 bytes); the credentialed channel carries no requirement
  text; externalRef/governingIntent/syzygy-poc:work: occur 0 times;
  mayNot occurs 0 times [Observed, re-measured this session]
- G2 Doctrine: aligned - vision.md's two-first-class-consumers and
  not-a-documentation-portal prose, VIS-1/4/5, SEC-1/3, PWB-REQ-005,
  PWB-REQ-013, PWB-REQ-020 (quoted), RFC8-21 (quoted), RFC6-14/6-22
- G3 Topology: apps/three-surface-poc + packages/three-surface-poc-core;
  no new boundary; slice 3's registry/spec touch is contingent on Q1/Q2
- G4 Design: dispatch packet as proposedWork's sibling with a
  dispatch-state discriminant; authority.mayNot from the three parsed
  authorities plus a registration-guarded hand-typed table; a briefing
  route whose every field is oracle-derivable from /api/poc, RFC8-21
  chain rendered not-applicable off the three fixed literals
- G5 Spec: slices 1-2 no delta (PWB-REQ-013/020 already reach them);
  slice 3 needs one, per this move's own rule that a new route in a
  signed spec is a spec delta through CC-REV-2 - an owner question (Q1),
  never a plan step
- G6 Bar: retained before/after measurement, rule-6 mutants per guard
  branch, a new Trajectory-scoped parity test plus the extended Polaris
  sweep, independent review before close and before any Q1 act
Acts: slices 1-2 none (the 2026-09-05 continuation); slice 3 one on Q1
  (spec delta) and possibly a second on Q2 (registry ceiling); slice 4
  not evaluated
Open questions: Q1-Q4 above; would queue as P-72 (P-68 lane B, P-69 M2,
  P-70 M3, P-71 M4, each on its own branch; main's register still ends
  at P-67)
Sign-off: pending - the owner's
Recommended handoff: land slices 1 and 2 now under syzygy-dov.5; rule
  Q1 (recommended: a PWB delta covering /api/poc/polaris and
  /api/poc/briefing together) and, if it clears, Q2 (recommended: mint
  maxBriefingResponseBytes) and Q3 (recommended: disclose, do not mint
  a new population shape); build slice 3 once ruled, on either side of
  M4's landing (Q4); defer slice 4
```

## Recommended handoff

**Slices 1 and 2 need no owner act and no sequencing wait.** File no
new bead; run them under `syzygy-dov.5`. Slice 2 alone closes L5-F9
(zero prohibitions on the machine channel) and is the cheapest item in
this packet, matching the dossier's own assessment of L5-M6.

**If Q1 is answered as recommended** (a PWB delta covering both
existing and new derived-view routes): draft the delta as a small
package in the 2026-09-05 amendment shape, queue it behind lane B
(P-68) per the one-manifest-at-a-time rule (Collision section), get an
independent fresh-context review with the raw retained, and put the
resulting act to the owner. Only then build slice 3.

**If Q1 is answered toward the cheaper POC-spec reader-note widening
instead**: the delta is smaller and does not queue behind lane B,
since it touches a different signed document; slice 3 can build
sooner, at the cost of leaving `/api/poc/polaris` itself still
unspec'd for a future third such route to raise again.

**If Q2 is answered as recommended** (mint `maxBriefingResponseBytes`):
draft the registry delta in the M2-slice-5 shape (a semantic delta, an
impact ledger, a review brief, an owner decision packet, a manifest),
get its independent review, and put the two-step act — adopt the
amended entry, then a continuation across the registry escalation
trigger — to the owner as one batched decision.

**If Q2's default holds instead** (reuse `maxMachineResponseBytes`):
slice 3 ships as soon as Q1 clears, with the 20 KB figure enforced only
by a test assertion, disclosed in the evidence file as a bound without
a registry gate behind it.

**If Q4 is answered as recommended** (ship on its own schedule):
nothing in this packet blocks slice 3 on M4's landing order; record in
`syzygy-dov.4`'s notes that the briefing's own oracle will pick up
M4's routed reasons automatically once it lands, so no rework is
expected either way.
