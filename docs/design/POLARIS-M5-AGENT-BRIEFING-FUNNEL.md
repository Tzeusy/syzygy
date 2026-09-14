
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

Baseline: Syzygy `a9f671e` (main) [Observed].
`git diff --stat f4589e2..a9f671e -- apps packages` touches 31 files,
all under `apps/three-surface-poc/src/polaris.ts`, `polaris-narrative.ts`, their
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

## The two questions for the owner

Batched, each with the recommended answer first. Everything below is
the evidence behind them. Slices 1 and 2 need no owner act on this
packet's own reading (Gate 3); both open questions belong to slice 3,
the new route. The first draft put four questions; review 1 (F16)
found Q3 and Q4 to be engineering and planning judgment rather than
hard human gates, and this packet agrees — they are decided below the
table with the reasoning shown, and keep their numbers so the evidence
file and the sibling packets' cross-references still resolve.

| # | Question | Recommended |
|---|---|---|
| Q1 | **Does `GET /api/poc/briefing`, a new machine-credentialed route, need a spec delta before it may be built, and if so to which spec?** The three-surface-poc-experience spec's own reader note is definitional: "the 'machine answer' is the authenticated `GET /api/poc` response" (`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` line 26, singular, definite article, under the heading "Reader notes, binding on how this file is read") [Observed]. A precedent already exists that was never spec'd this way: `POLARIS_PRESENTATION_PATH` (`/api/poc/polaris`) is a second `machine-credentialed` route, justified only by a code comment citing PWB-REQ-014/020, named by no POC-REQ or PWB-REQ heading — the literal `api/poc/polaris` occurs 0 times across every tracked file under `openspec/` and `.syzygy/`, over 17 PWB and 24 POC `### Requirement:` headings [Observed, swept this session]. | **Yes, a delta is needed, and it should cover both routes at once.** Draft a small PWB semantic delta (in the 2026-09-05 amendment shape) that names a closed category — "derived read-only machine view": composed only of fields already reachable from `/api/poc` at the same evaluation, independently oracle-verified as derivable, served under its own declared, digest-bound response ceiling — and place both `/api/poc/polaris` (retroactively) and `/api/poc/briefing` (prospectively) under it. This closes the same gap for two routes in one package instead of drafting a narrower POC-spec reader-note widening now and a PWB delta later when the next such route appears. **Two other lawful arms.** (b) A POC-only reader-note widening is smaller, touches no digest-bound PWB text, does not queue behind lane B's open PWB package (Collision), and unblocks sooner; it would need no owner act under the same continuation slices 1–2 ride, only a spec-authoring cycle. (c) **Serve the briefing on the route that already exists** — `GET /api/poc` with a selector query parameter — which mints no route, raises no reader-note question, needs no new `ResponseLimitIdentity`, and so moots Q1 and Q2 together (named after review 1, F17). Not recommended [Inferred]: a parameterised `/api/poc` makes the one route the reader note *defines* as "the machine answer" serve two different bodies, so PWB-REQ-020's parity oracle would have to be told which form is the reference; and the briefing would sit under the 8,388,608-byte `maxMachineResponseBytes` with no ceiling of its own, which is exactly Q2's default arm with its defect — the owner is entitled to weigh that against amending a signed spec. **Default if unanswered: slice 3 does not ship.** Slices 1 and 2 are unaffected and may proceed regardless of how Q1 is ruled. |
| Q2 | **If Q1 authorizes slice 3, how is its response ceiling declared, and does a third ceiling amend PWB-REQ-006?** `PwbResourceLimits` (`packages/three-surface-poc-core/src/project-shape-observation.ts` lines 65–73) is the registry's seven-field resource envelope, of which exactly two are response ceilings — `maxHumanResponseBytes` (2,097,152) and `maxMachineResponseBytes` (8,388,608), lines 81–82 — all seven digest-bound inside the registry entry that `PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md` adopted [Observed; the first draft said "exactly two fields", withdrawn after review 1, F4]. PWB-REQ-006 (Gate 2) says the registry declares "one evaluation-wide resource envelope" and that "final encoded human HTML and machine JSON SHALL each have an explicit byte ceiling", with a Case over "both final-output sinks". Reusing `maxMachineResponseBytes` as the briefing's hard bound would let a briefing grow to 8 MiB with nothing to stop it — the exact defect this move exists to fix. | **Mint `maxBriefingResponseBytes` in the registry entry, adopted by a superseding act in the 2026-09-05 shape (the same mechanism M2's Q2 already recommends for a currency bound), and rule at the same time whether the third ceiling also stales PWB-REQ-006's two-sink wording.** Two things are stated plainly that the first draft did not (review 1, F11, F12): first, this is **new code and a closed-type widening** — `ResponseLimitIdentity` (`routes.ts` line 111) is a closed union of two string literals and `PwbResourceLimits` a seven-field interface, and both grow by one; `boundedResponse` (`routes.ts` lines 137–142) is generic over the identity it is passed, so the enforcement path is reused, but the type is not untouched. The packet defends the widening because it happens **under an owner act over the registry entry** (escalation trigger, act line 92) — whereas Q3's `population` widening, declined below, would happen on the implementation's own authority with no act to warrant it; that is the asymmetry, and it is deliberate. Second, a third declared ceiling plausibly amends PWB-REQ-006's "each" over two sinks, in which case the registry delta **folds into Q1's PWB delta** as one package rather than a separate second act — a different cost from the two-step act the handoff describes, and the owner's call [Inferred]. Counter-argument: it is a second owner step queued behind Q1's spec delta, and until it lands slice 3 cannot ship at all. **Default if unanswered: slice 3 reuses `maxMachineResponseBytes` as its hard bound, with the ~20 KB figure enforced only by a test assertion** — a bound that could silently widen release by release with no registry gate to catch it, disclosed as such. |

### Decided in this packet, not put to the owner (Q3, Q4)

**Q3 — the breach body's `population` on a briefing-ceiling breach.**
Decided: reuse `ResponseLimitFailure` (`routes.ts` lines 113–124,
`population` at 120–122 — a closed two-arm union scoped to the whole
project shape) **unchanged**, and add one sentence to the body:
"population describes the whole evaluation, not this briefing's
subject." No third `population` arm is minted. Why this is not an
owner gate: the type is an implementation type in
`apps/three-surface-poc/src/routes.ts` bound by no act; PWB-REQ-006
asks the breach envelope for "population counts" and says nothing
about their scope; and both arms leave the type unchanged, so there is
no trade-off for the owner to hold. Why the sentence is worth having:
a response-ceiling breach serves nothing and logs nothing — no ledger,
stderr line or status record sees it, and the 503 body of the
breaching request is the only trace (AGENTS.md records this) — so the
body is the one place a reader can learn that the counts describe the
whole evaluation. The counter-argument stands and is accepted: a
mechanical reader still sees whole-model counts; if a later move needs
a subject-scoped count it re-enters this funnel. This is the same
restraint M2's Q5 and M4's Q2 apply to their own closed vocabularies.

**Q4 — sequencing against M4's routed-Unknown work
(`agent/syzygy-dov.4`, register row P-71).** Decided: ship slice 3
whenever Q1 and Q2 clear, independent of M4's landing order; no
ordering is enforced. M4 slice 1 gives nine currently routeless
Unknown disclosures (five relationships, four entities) a closed
RFC2-24 reason and a route; the briefing reads exactly those
structures. Its derivability oracle (Gate 4) reads the model's live
`PocEpistemic` and `resolutionRoutes` shape, not a hand-copied list,
so it improves automatically the moment M4 lands — no rework, no
second edit. The one cost, accepted: if slice 3 ships first, its
acceptance fixture briefly documents free-prose reasons as current
behavior, which a reviewer must recognize as pre-M4 rather than a
regression; the evidence file will say so. A sequencing preference
between two of the owner's own branches is planning judgment, not an
act (review 1, F16).

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
   `walkthroughJudgment`, `materializedBeadId` — is 18,710 bytes as one
   compact object with the dossier's short key names, 0.339%
   [Observed, computed this session; method and full breakdown in the
   evidence file]. The dossier's own share (0.340% of a 5,508,208-byte
   pre-lane-A capture) is confirmed on a different Butlers revision —
   the defect is unchanged in kind, and the two captures'
   `workItems`/`codeStructure` shares differ (71.9% pre-lane-A vs
   68.2% here) only because the two revisions' bead and file counts
   differ, not because Syzygy changed.
2. **The credentialed machine channel carries no requirement text; the
   only channel that does is unauthenticated.** Re-verified at
   `a9f671e`: `POLARIS_SOURCE_PATH` (`/polaris/source`) is
   `credentialClass: 'human-open'` (`routes.ts` line 221) and its only
   gate is `browserRequestAllowed` (`browser-origin.ts` lines 26–38),
   which checks the `Host` header's shape and, when present, the
   `Origin` header — no bearer token, no machine-client authentication
   of the kind SEC-1 requires for "non-browser agent and CLI clients."
   A plain `curl` with a correct `Host` header passes it. The two
   `machine-credentialed` routes (`POC_MACHINE_PATH`,
   `POLARIS_PRESENTATION_PATH`, `routes.ts` lines 225–238) require the
   bearer-token check at `packages/cap1-daemon/src/server.ts` lines
   187–200, and neither serves requirement prose: the one
   `switchboard-identity` item in `projectShape.items` carries a
   661-byte compact record (the `claim` sub-object 504 of them) of
   class, key, state, one anchor at line 1 of its source and the claim
   tuple — no requirement id, no statement text [Observed, recomputed;
   the first draft said 511, withdrawn after review 1, F10].
3. **The one dispatch artifact in the system is absent from the
   machine payload.** `externalRef`, `governingIntent` and
   `syzygy-poc:work:` occur **0** times in the 5,520,314-byte capture
   [Observed, `str.count` this session, agreeing with the dossier's
   pre-lane-A count]. `buildTrajectoryMaterializationPacket`
   (`materialize-action.ts` lines 31–37) is computed only inside
   `renderMaterializePanel` (lines 55–82), which only `trajectory.ts`
   line 187 calls — the packet is rendered exactly once, as HTML
   `<dd>` elements on the Trajectory page, and reaches `/api/poc`
   nowhere.
4. **The machine payload names zero prohibitions of Syzygy's own
   authority.** The literal `mayNot` occurs 0 times; `forbidden`
   occurs 3 times and `prohibit` 1 time on this capture, and the same
   3 and 1 on the dossier's pre-lane-A capture [Observed, `str.count`
   over the decoded text and `bytes.count` over the raw file agreeing,
   this session]. All four hits sit inside observed Butlers bead titles
   in `workItems` — statements Butlers makes about its own work, never
   a statement of what the consumer of this payload may not do. (The
   first draft of this item said `forbidden` occurred 0 times here and
   3 there and invented a catalog move to explain the difference;
   withdrawn after review 1, F1 — the count is 3 on both.) The only
   scope statement anywhere is
   `projectShape.identity.scope`, which describes what was read
   (repository `repository:butlers-configured-poc`, content class
   `declared-project-shape-text`, phase `A`), never what the consumer
   may do with it.

**A subject-naming finding not in the dossier.** Four work-related
subjects, each fixed in code or observed from the tree, sit inside one
evaluation, and they are not one subject:

1. `proposedWork.changeId` is `repair-whatsapp-identity-reconciliation`
   [Observed] — the one Butlers-side OpenSpec change PWB-REQ-013's own
   pipeline discovered at this revision; its `specKey` is
   `switchboard-identity` and its
   `currentAuthority.claim.claimId` is exactly
   `claim:item:baseline-spec:switchboard-identity` [Observed].
2. `MATERIALIZATION_EXTERNAL_REF`
   (`packages/three-surface-poc-core/src/materialization.ts` line 9:
   `'syzygy-poc:work:whatsapp-single-event-normalization'`), the fixed
   work item `buildMaterializationPacket` always describes.
3. `WORKER_CHANGE_INTENT_ID` (`model.ts` line 42:
   `'REQ-connector-base-spec-001'`), the intent the worker-change badge
   cites.
4. `MaterializationGoverningIntent.requirementId`
   (`materialization.ts` line 15: `'REQ-switchboard-identity-001'`),
   the fixed intent the dispatch packet cites, which is also the
   `intent:req-switchboard-identity-001` entity on the payload and the
   `from` end of `relationship:intent-to-work` [Observed].

`switchboard-identity` is therefore the **join point** of literals 1
and 4, not a subject outside them: a briefing for
`claim:item:baseline-spec:switchboard-identity` has an applicable
RFC8-21 chain (the intent entity and its two relationships,
`capability-to-intent` Observed and `intent-to-work` Unknown on this
capture). A briefing composed naively — "the subject's proposed work"
— would still conflate the four; slice 3's design (Gate 4) treats them
as four separate lookups, renders the joined tuples verbatim when a
selector names a joined subject, and renders "not applicable" rather
than guessing when it names one none of the four touch — a
`topology-component` claim, for instance (S6). (The first draft named
three literals and used `switchboard-identity` as the counterexample;
withdrawn after review 1, F2 — the capture joins it twice.)

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
   that does not resolve, a typed not-found disclosure as a fact of
   the render (RFC2-24; Gate 4 slice 3), carrying no Unknown reason
   and never an empty or fabricated briefing.
2. `/api/poc` carries the exact `MaterializationPacket` (nine fields,
   `materialization.ts` lines 20–30) beside `proposedWork`, with a
   `dispatchState` discriminant (`'undispatched'` or
   `{'dispatched', beadId, at}`). A parity test asserts, by value after
   HTML-unescaping, the **seven** packet fields the Trajectory panel
   renders (`materialize-action.ts` lines 69–75) and the bead id in the
   status line (lines 61–62); it records the **two** packet fields the
   panel never renders (`targetBeadPrefix`, `governingIntent.designPath`)
   and the state's `at` as machine-only, with both denominators (7 of 9
   packet fields; 1 of 2 state fields). A test issuing N machine `GET`
   requests against a fixture state directory asserts the directory's
   bytes are unchanged after the Nth. (The first draft said
   "byte-identical" over "the packet's seven fields"; withdrawn after
   review 1, F6.)
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
not change that architecture, only renders the joined tuples verbatim
where the four literals reach and discloses "not applicable" honestly
where they do not.

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
| Minimal orientation (14 fields listed in Gate 1, one compact object, short key names — `scope` for `projectShape.identity.scope`, the dossier's own spelling) | 18,710 | 0.339% |
| …dossier's own share, pre-lane-A capture (5,508,208 bytes) | — | 0.340% |
| …plus `projectShape.classes` and `projectShape.claim`, same spelling | 148,780 | 2.695% |
| …dossier's own share, pre-lane-A | — | 2.70% |
| One-claim briefing, **applicable chain**: `claim:item:baseline-spec:switchboard-identity` — `evaluation`, `projectShape.identity.scope`, `projectShape.authority`, the item record, the joined `intent:req-switchboard-identity-001` entity and its two relationships, empty Unknown and exclusion arms, one exact-source route entry with a placeholder href; `mayNot` not yet built | 5,449 | 0.099% |
| …plus the one matching `projectShape.sources` record (1,627 bytes) | 7,076 | 0.128% |
| One-claim briefing, **chain not applicable**: `claim:item:topology-component:1:Spawner`, same composition with a not-applicable chain disclosure | 3,347 | 0.061% |
| …plus its one matching source record (1,803 bytes) | 5,150 | 0.093% |

The byte figures on the two captures are compared only as shares:
composing the same fourteen fields with short key names reproduces the
dossier's 18,710 exactly on **this** capture, and spelling the keys as
the evidence file's field list (`identity.scope`) adds 9 bytes, so a
cross-capture byte difference at that scale is key spelling, not a
measurement (review 1, F8). The one-claim figures are new
measurements, not in the dossier, composed from exact field paths
(evidence file, `agent_briefing_sets.one_claim_briefing_examples`);
the route href is a 27-byte placeholder, so each is a floor. They are
the shape slice 3's oracle must hold to. The recommended 20 KB ceiling
(Q2) is 2.9× the larger composition (20,480 / 7,076) — headroom, not a
tight budget. (The first draft published one figure, 2,829 bytes, for a
selector spelled `claim:baseline-spec:switchboard-identity`, which
matches 0 of the 415 item ids, with a not-applicable chain the capture
contradicts and a composition no stated method reproduces; withdrawn
after review 1, F2, F7 and F9.)

### Literal-substring counts (method: `str.count`, two runs agreeing)

| Substring | This capture | Dossier's pre-lane-A capture |
|---|---:|---:|
| `externalRef` | 0 | 0 |
| `governingIntent` | 0 | 0 |
| `syzygy-poc:work:` | 0 | 0 |
| `mayNot` | 0 | not measured (field did not exist) |
| `forbidden` | 3 (Butlers bead titles, `workItems`) | 3 (Butlers bead titles) |
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

Every row below was re-derived mechanically after review 1 (F5) with
`grep -n` over the declaration and closing-brace lines, never by hand;
the four rows the first draft got wrong are marked.

| Citation | At `a9f671e` | Dossier said | Note |
|---|---|---|---|
| `routes.ts` `machineHandle` | 159–162 | 159–162 | holds |
| `routes.ts` `POLARIS_SOURCE_PATH` route registration | 221 (222 tailnet) | 196–200, 222–223 | **196–200 is `humanSurfaceRoutes`'s internal handle closure, a different route family (Trajectory/Orrery), not `POLARIS_SOURCE_PATH`'s own registration**; 222 is the tailnet variant, 223 is the next line's `...humanSurfaceRoutes(TRAJECTORY_...)` spread, not a `POLARIS_SOURCE_PATH` line |
| `routes.ts` `machine-credentialed` route block | 225–238 | 232–239 | the dossier's range starts inside the block (missing `POC_MACHINE_PATH`'s own direct registration at 225–229) and ends one line past the last route row (239 is outside the returned array) |
| `browser-origin.ts` `browserRequestAllowed` | 26–38 (doc comment from 24; file ends at 38) | not cited by line | — |
| `materialize-action.ts` `MATERIALIZE_HUMAN_PATH` | 17 | 17 | holds |
| `materialize-action.ts` `renderMaterializePanel` | 55–82 | 55–80 (dossier); 55–81 (form/button) | the function's closing brace is line 82; 78–80 is the form/button pair, correct as far as it goes |
| `materialization.ts` `MaterializationPacket` | 20–30 (nine fields) | not cited by line | first draft said 24–29; corrected after review 1 (F5) |
| `materialization.ts` `MaterializationGoverningIntent` | 14–18 | not cited by line | `requirementId` literal at 15 |
| `materialization.ts` `buildMaterializationPacket` | 43–65 | not cited by line | first draft said 41–64; corrected after review 1 (F5) |
| `materialization.ts` `MaterializationRecord` | 67–78 (`createdAt` at 71) | not cited by line | first draft said 67–76; corrected after review 1 (F22) |
| `materialize-action.ts` `buildTrajectoryMaterializationPacket` | 31–37 | not cited by line | first draft said 30–34; corrected after review 1 (F5) |
| `routes.ts` `ResponseLimitIdentity` | 111 | not cited by line | a closed union of two string literals |
| `routes.ts` `ResponseLimitFailure` | 113–124 (`population` at 120–122) | not cited by line | first draft said 113–121; corrected after review 1 (F22) |
| `routes.ts` `boundedResponse` | 137–142 | not cited by line | first draft said 111–121, which is the type above, not the function; corrected after review 1 (F5) |
| `polaris.ts` `authorityLine` (slice 2's edit site) | 707–713 | not cited by line | outside every region M3 cites (Collision) |
| `model.ts` `PocEpistemic` | 44–46 | not cited by line | — |
| `model.ts` `PocModel` interface | 98–155 | not cited by line | — |
| `body-read-authority.ts` `BodyReadAuthorityEvaluation` | 315–324 | not cited by line | — |
| `authority-disclosure.ts` `AuthorityDisclosure` | 39–46 | not cited by line | — |
| `project-shape-observation.ts` `PwbResourceLimits` / `PWB_RESOURCE_LIMITS` | 65–73 / 75–83 | not cited by line | seven fields; the two response ceilings are `maxHumanResponseBytes` 81 (2,097,152) and `maxMachineResponseBytes` 82 (8,388,608) |

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
lines 122–139). No slice moves the write boundary:
`POST /trajectory/materialize` keeps its human trigger and its
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
be called independently verified. State (1) SHALL render exactly:"
followed by the two-sentence owner-trusted-only wording (the sentence
is longer than one line and is not re-quoted here; read it at the cited
lines). This is the
clause `AuthorityDisclosure` (`authority-disclosure.ts`) already
implements exactly, and it is the ground for slice 2: `mayNot` is a
new field on the same disclosure object this requirement already
governs, not a new authority mechanism.

**PWB-REQ-006 — Project-shape content stays contained, inert and
bounded** (spec lines 340–386, quoted in relevant part): "The registry
SHALL declare one evaluation-wide resource envelope... Final encoded
human HTML and machine JSON SHALL each have an explicit byte ceiling...
A final-output breach SHALL return only a bounded typed failure
envelope carrying evaluation identity, limit identity, declared value,
observed value and population counts; it SHALL NOT truncate or emit a
success-shaped model." Its Case sweeps "both final-output sinks". This
is the requirement Q2 and the breach-body decision (Q3) both land
inside: slice 3 adds a third final-output sink, Q2 proposes a third
declared ceiling for it, and the breach body's `population` is the
"population counts" this clause names. It was not cited in the first
draft (review 1, F11); reading it changes Q2's shape — see that row.

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
machine views** (spec lines 902–927, quoted in relevant part — the
SHALL, Observable and Falsifier; the Case, Oracle, Oracle-independence
and Mutation-proof bullets are at the cited lines):

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
under this Case's own enumeration [Inferred — a reading of a
digest-bound clause's scope, not its text], so PWB-REQ-020 reaches
them: they must render on the human surface too, not only on
`/api/poc`, or the Falsifier's "missing... in either channel" fires.
Slice 2's own design already renders them from one field for exactly
this reason (Gate 4). The dispatch packet (slice 1) is **not** in this
enumeration — it is the PWB-REQ-013-typed proposed-work artifact, not
a project-shape identity, statement, anchor, coverage state,
denominator, contradiction, authority state or judgment state — so the
two packet fields and the `at` timestamp that reach `/api/poc` without
a Trajectory-panel counterpart (success criterion 2) do not fire this
Falsifier on this packet's reading [Inferred]. That is the same
machine-more-than-page reading M4 slice 2 already names for its route
form, and it is put to the owner inside Q1 rather than assumed.

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
chain over four fixed-or-observed work literals
(`WORKER_CHANGE_SEAM`/`WORKER_CHANGE_INTENT_ID`,
`MATERIALIZATION_EXTERNAL_REF`,
`MaterializationGoverningIntent.requirementId`, and `proposedWork`'s
dynamically observed `changeId`), not generally over "whatever the
selector names." Slice 3 must therefore render the joined tuples
verbatim where those literals reach the subject
(`claim:item:baseline-spec:switchboard-identity` is joined by two of
them) and the chain as **not applicable** for a subject none of the
four touch (a `topology-component` claim, for instance), per RFC8-22's
"a broken join renders; it
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

Boundaries crossed: none new for slices 1–2. The existing edge from
`three-surface-poc-core` to `cap1-daemon` (the `Route` and
credential-class types) already carries the
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
| 3 Briefing route | **Yes, per Q1; and per Q2 if the ceiling is minted** | No act found that authorizes a new machine-credentialed route as read; the escalation triggers are "any scope beyond the signed change" (`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` lines 93–94) and, for Q2, "a change to the constraints or envelope the registry entry declares" (line 92), together with the act's own bullet "No edit to any act-bound artifact... Spec changes route through CC-REV-2's amendment path and a new owner act" (lines 76–79) and this packet's reading of the POC spec's reader note (Gate 5). On Q1's existing-route arm no trigger is crossed and no act is needed |
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
(the record already carries `createdAt`, `materialization.ts` line 71
inside `MaterializationRecord`, lines 67–78). `renderMaterializePanel`
is refactored to read
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
repo, governing intent as `requirementId` plus `proposalPath`, title,
description, labels, type/priority, external ref — already rendered
today, `materialize-action.ts` lines 69–75) plus the
`materialize-status`/`materialize-trigger` pair against
`model.dispatch.packet` and `.state` by field, **by value after
HTML-unescaping, never by bytes**, reporting both denominators: 7 of
the packet's 9 fields have a panel counterpart (`targetBeadPrefix`,
`materialization.ts` line 12, and `governingIntent.designPath`, line
17, are built at `materialize-action.ts` line 35 and rendered nowhere
[Observed, grep over `trajectory.ts` and `materialize-action.ts`]),
and 1 of the state's 2 fields does (the bead id at lines 61–62; `at`
has no panel counterpart). The test asserts the machine-only remainder
explicitly so the asymmetry is a recorded denominator, not a silent
gap. The panel's appearance is unchanged by slice 1; whether the two
unrendered fields should also be shown there is a human-surface
change this packet does not propose, and the reading that the
asymmetry does not fire PWB-REQ-020's Falsifier is [Inferred] (Gate
2). Today no such test exists (only `materialize-action.test.ts`
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
underlying JSON declares an empty `writeSurface` and
`executeObservedCode` false
(`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
lines 125 and 128, already validated by `body-read-authority.ts` lines
677–684) yields a row citing that authority's own `actIdentity` and
`artifactDigest` — zero new reads, since the daemon already holds
these values. **(b)** The implementation-authorization act's own "What
this does not authorize" bullets (`PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`
lines 68–84, **six bullets** [Observed, counted this session]: (1) no
write, egress, execution, deployment, release, recovery or mission
effect on Butlers or any other repository, lines 70–72; (2) no second
repository, no wider content class, no reading of excluded or
unclassifiable content, 73–74; (3) no production release, broad remote
access or multi-user support, 75; (4) no edit to any act-bound
artifact — spec changes route through CC-REV-2 and a new owner act,
76–79; (5) no doctrine or contract change, no autonomous intent
adoption, no Syzygy-authored implementation code, no unattended agent
coordination, 80–81; (6) no independent verification — a state-(1)
human direction, 82–84) are proposed as a hand-typed, **closed** table
of exactly six rows in the shape of `UNKNOWN_REASON_ROUTES` — the first
draft listed the contents of three bullets and would have seeded the
table at half strength (review 1, F14) — each row carries
`actIdentity: 'PWB-IMPLEMENTATION-AUTHORIZATION-ACT'` and
`artifactDigest: undefined` (the act's digest is never quoted in this
table or in this packet, per AGENTS.md's guardrail against quoting a
performed act's argument outside `ACT_DIGEST_COPY_FILES`; the row
cites the record by path). Per Gate 3's engineering note, this table's
entry count — **six** — should be registered wherever
`check_governance.py` would notice the source act change (a new
function alongside `_act_subjects()`, or a dedicated fixture asserting
the table's row count against a fresh read of the act file's bullet
count under the "What this does not authorize" heading) so an
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
first cut, `for=<claimId>` where the value is the full id as it appears
in `projectShape.items` — every one of the 415 item claim ids on this
capture has the form `claim:item:<class>:<key>`, with `item` the only
second segment present [Observed, swept this session over 415 of 415]
— so the worked example is `for=claim:item:baseline-spec:switchboard-identity`
(query-parameter handling already
precedented by `SOURCE_IDENTITY_PARAM`,
`apps/three-surface-poc/src/polaris-source.ts` lines 33 and 41–42), and
composes, for the named claim:

- the evaluation identity (`snapshot`, `asOf` — a subset of what
  `/api/poc` already carries, never re-derived);
- `identity.scope` (consent scope, verbatim);
- `authority` in full, including `mayNot` (slice 2);
- the claim's own tuple, from `projectShape.items`/`.facts`/`.classes`
  by id;
- an RFC8-21 chain state for the subject: the joined entity and its
  relationships' epistemic tuples by id, verbatim, when the subject is
  one the four fixed-or-observed work literals name (Gate 1's
  subject-naming finding — `switchboard-identity` is the worked case,
  joined by two of the four); **`not-applicable`** with a named
  fact-of-render disclosure when it is not (a `topology-component`
  claim, for instance);
- every Unknown touching the subject (its own claim if Unknown; any
  relationship or entity naming it, once M4 lands with routes on all
  22, or with today's free-prose reasons if it lands first — Q4,
  decided);
- exclusions touching the subject's anchors, by path;
- the exact-source route for each cited requirement, built with the
  existing pure `sourceRouteHref(mountPrefix, identity)`
  (`polaris-source.ts` lines 41–42) — no new URL-construction logic.

An unresolvable selector (a `claimId` absent from every population)
is **not an Unknown claim and carries no `reason` slot**. RFC2-24
closes the Unknown-reason vocabulary at twelve values
(`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
lines 44–50, quoted): "no implementation may mint, spell, or force-fit
a value the list does not carry... A condition genuinely outside the
twelve is disclosed as a **fact of the render**, never dressed as a
reason." A selector that names nothing is exactly such a condition —
there is no claim whose epistemic state could carry a reason — so the
route answers with a typed not-found disclosure: `served: 'nothing'`,
the raw selector echoed verbatim, the population it was resolved
against (`projectShape.items` by `claim.claimId`, with the item count
as denominator), and a route to the resolving action (list the claim
ids from `/api/poc`). It is never an empty or partial briefing
(success criterion 1). The first draft of this paragraph minted
`no-such-claim` as a reason; withdrawn after review 1 (F3), and
PWB-REQ-007's own sentence — "Unknown reasons SHALL use RFC2-24 values
verbatim and expose their resolution routes" (spec lines 447–448) —
is the clause that forbids it.

**Ceiling.** Served through `boundedResponse`
(`routes.ts` lines 137–142, generic over which `ResponseLimitIdentity`
and `PwbResourceLimits` field it is passed — but see Q2: adding a third
identity widens that closed two-literal union at `routes.ts` line 111
and the seven-field `PwbResourceLimits` interface, which is new code)
with `maxBriefingResponseBytes` if Q2 mints it, or
`maxMachineResponseBytes` as the interim hard bound with a test-only
20 KB assertion if not (Q2's default). Either way, the two measured
one-claim compositions (7,076 bytes for
`claim:item:baseline-spec:switchboard-identity` with its applicable
chain, 5,150 bytes for `claim:item:topology-component:1:Spawner` with
the chain not applicable; Measurements, "The briefing an agent needs")
are published alongside the ceiling as the requirement's denominator,
in the M1/M2 shape.

**Breach body (Q3, decided in this packet).** On a briefing-ceiling
breach the existing `ResponseLimitFailure` shape (`routes.ts` lines
113–124; `population` at 120–122) is reused unchanged and one
sentence is added to the body: "population describes the whole
evaluation, not this briefing's subject." No third `population` arm is
minted. The reasons are in "Decided in this packet" below the owner
questions.

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
guaranteed stable — PWB-REQ-007 (spec lines 443–446, quoted): "Every
project entity and project-fact claim SHALL have a stable semantic
Claim identity plus an evaluation instance"; a path or change selector
would need its own resolution step this packet does not design);
folding the briefing into `/api/poc/polaris` (that route
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
refactors where its data comes from, and the two packet fields the
panel has never rendered stay unrendered (slice 1's parity test
records them as machine-only; see success criterion 2).

## Gate 5 — Specification

**Slices 1 and 2: no spec delta.** PWB-REQ-013 already types the
dispatch packet's subject matter as "described here as a distinct
machine type"; serving it as a sibling field on the existing `/api/poc`
adds no new route, no new credential class, and no new project fact
(PWB-REQ-004's closed population is untouched — the packet is not a
project-shape claim). For `mayNot` the question that actually decides
whether an act is needed is not parity but minting: **may the
implementation add a disclosure no requirement names?** This packet's
answer [Inferred]: yes, on two grounds — PWB-REQ-005 already requires
"every human and machine rendering of the authorization basis" to
"expose each authority's exact state", and `mayNot`'s rows are derived
from exactly those already-parsed states plus one closed table of the
act's own words, so it is a rendering of the authorization basis this
requirement governs, not a new authority mechanism or a new project
fact; and the payload's field set is bound by no act (the same ground
M2 slice 3's `evidence` block and M4 slice 2's route form rest on).
Once the field exists, PWB-REQ-020 reaches it (Gate 2, an [Inferred]
scope reading) and requires it on both channels, which slice 2's
design satisfies from one field. If a reviewer reads `mayNot` instead
as a new disclosure class, the fallback is the recorded-finding arm
M4's slices 4–5 already rest on, naming L5-F9 — an [Inferred] reading
that would then be put to the owner. The first draft argued this
circularly from PWB-REQ-020 alone (review 1, F13).

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
  line 26 of
  `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`
  from "the 'machine answer' is the authenticated `GET /api/poc`
  response" to name a family of derived views under the same
  authentication and equivalence discipline. Touches one sentence
  under the heading "Reader notes, binding on how this file is read" —
  binding prose, not scaffolding, and not a numbered requirement.

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

**S2 — An unresolvable subject is a typed not-found disclosure, never
an Unknown reason.** WHEN the selector names no claim in any
population, THEN the response serves nothing, echoes the raw selector,
names the population it was resolved against with its count, and
routes to the resolving action, AND carries no `reason` field and no
value outside RFC2-24's twelve (Gate 4 slice 3), never an empty or
partial briefing. (The first draft's S2 minted `no-such-claim`;
withdrawn after review 1, F3.)

**S3 — A GET never writes.** WHEN `GET /api/poc` or
`GET /api/poc/briefing` is issued any number of times with no
intervening `POST /trajectory/materialize`, THEN the state directory's
bytes are unchanged.

**S4 — The dispatch packet cannot diverge across channels.** WHEN the
Trajectory panel and `/api/poc`'s `dispatch.packet` are read from one
evaluation, THEN each of the 7 packet fields the panel renders (of 9)
and the 1 state field it renders (of 2) matches by value after
HTML-unescaping, AND the test asserts both denominators and names the
three machine-only values.

**S5 — Withdrawing an authority hardens `mayNot`, never empties it.**
WHEN one of the three authorities moves from `valid` to `absent` or
`invalid`, THEN its `mayNot` row's text changes to the stricter form
and the array's length does not decrease.

**S6 — A subject with no RFC8-21 relationship gets an honest
"not applicable."** WHEN the briefing's subject (for instance
`claim:item:topology-component:1:Spawner`) is named by none of the
four fixed-or-observed work literals, THEN the chain field renders a
not-applicable disclosure as a fact of the render (no `reason` slot;
RFC2-24), never a fabricated eight-link Unknown ladder; AND WHEN it is
named by one (`claim:item:baseline-spec:switchboard-identity`, joined
by two), THEN the chain field carries the joined entity's and
relationships' tuples verbatim.

## Collision and sequencing

Denominators, stated after review 1 (F15): every slice row of each
sibling's own Gate 3 table was read — M2's 6 slices, M3's 4 slices
plus the five `polaris.ts` regions its packet cites (306–307, 346–361,
506–510, 1307, 1328–1329), M4's 8 slices, and lane B's package —
against M5's three edit regions (`model.ts` interface line ~140 and
`buildModel`'s return at line 707, `polaris.ts` `authorityLine` at
707–713, and a new route inside `routes.ts`'s 225–238 block plus a new
module). The M4 and M2 worktrees were read read-only at their register
rows' heads on 2026-09-14.

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
row P-70; not present on this worktree's own branch).** M3's slices
touch `polaris-copy.ts`, `design-tokens.ts`, two test files, a fixture
and `polaris.ts` in the five regions above (`claimStatesBlock` at
346–361, the opening band, the CSS block near 1307, and the tier
lines at 306–307 and 1328–1329). M5 slice 2 edits `authorityLine`
(`polaris.ts` lines 707–713) to add `mayNot` — a different function,
outside all five regions [Observed, this worktree], and a different
concept (prohibitions, not epistemic-state encoding). Whether M3's
actual diff, once committed, stays inside the regions its packet
cites is [Unknown] until it lands — only M3's Gate 3 table and cited
lines were read, not a full diff; re-check the function boundaries
then, in the style M4 already recommends for its own M3 overlap.

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
depends on M4's landing order, which is exactly the sequencing point
decided as Q4 below the owner questions. Three further M4 slices sit
near M5's regions and were not examined in the first draft (review 1,
F15): **M4 slice 8 (deferred), "packet per claim; the queue", edits
`materialization.ts` lines 9–65** — the very artifact M5 slice 1
exposes, and the direct successor to Gate 1's four-subject finding;
it is behind its own owner acts, so M5 slice 1 lands first and slice 8
would then generalize a field that already exists on the machine
channel rather than introduce one — a semantic relationship, not a
textual collision. **M4 slice 4** edits `model.ts` lines 710–750
(`surfaces:` opens at 710, three lines below the `proposedWork:` line
707 where M5 slice 1 inserts `dispatch`) — adjacent, not overlapping
[Observed, `model.ts` at the same commit in both worktrees]. **M4
slice 5** edits `routes.ts` lines 34–96 (the home route); M5 slice 3
adds one row to the machine-credentialed block at 225–238 — no
overlap. Also
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
rule; if a POC delta is chosen, it may proceed independently; if the
existing-route arm is chosen, no delta at all. (3) Once Q1 clears,
rule Q2, then build slice 3 with the breach body as decided (Q3), in
either order relative to M4 (Q4, decided) since the oracle
self-corrects. (4) Re-enter this funnel for slice 4 once slice 3 is
measured against real traffic shapes.

**Unknowns carried from the evidence file** (review 1, F18; VIS-2
governs the document the owner reads, not only its sidecar):

- [Unknown] Which Q1 arm the owner will choose; all three are lawful
  on this packet's reading.
- [Unknown] The exact byte cost of `authority.mayNot` once built —
  estimated at a few hundred bytes for six table rows plus three
  authority rows; not implemented, so not measured.
- [Unknown] Whether M3's committed diff stays inside the five
  `polaris.ts` regions its packet cites (above).
- [Unknown] The registry entry's digest as currently recorded in
  `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`
  was neither quoted nor re-derived here, per the guardrail against
  quoting a signed digest outside the recorder's copy files.

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
   app suite twice and the full suite pass;
   `tsc -b packages/three-surface-poc-core` before the app typecheck.
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
- G1 Motif: agent orientation is 0.339% of the payload (18,710 of
  5,520,314 bytes); the credentialed channel carries no requirement
  text; externalRef/governingIntent/syzygy-poc:work: occur 0 times;
  mayNot occurs 0 times and every forbidden/prohibit hit (3 + 1) is an
  observed Butlers bead title [Observed, re-measured this session]
- G2 Doctrine: aligned - vision.md's two-first-class-consumers and
  not-a-documentation-portal prose, VIS-1/4/5, SEC-1/3, PWB-REQ-005,
  PWB-REQ-013, PWB-REQ-020 (quoted), RFC8-21 (quoted), RFC6-14/6-22
- G3 Topology: apps/three-surface-poc + packages/three-surface-poc-core;
  no new boundary; slice 3's registry/spec touch is contingent on Q1/Q2
- G4 Design: dispatch packet as proposedWork's sibling with a
  dispatch-state discriminant (7 of 9 fields have a panel counterpart,
  recorded as such); authority.mayNot from the three parsed
  authorities plus a registration-guarded six-row hand-typed table; a
  briefing route whose every field is oracle-derivable from /api/poc,
  RFC8-21 chain rendered verbatim where the four work literals join
  the subject and not-applicable where they do not; an unresolvable
  selector is a fact-of-render disclosure, never an Unknown reason
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
Open questions: Q1-Q2 above, queued as P-72 on this branch (P-68 lane
  B, P-69 M2, P-70 M3, P-71 M4, each on its own branch; main's register
  still ends at P-67); Q3 and Q4 decided in the packet, not put to the
  owner
Sign-off: pending - the owner's
Recommended handoff: land slices 1 and 2 now under syzygy-dov.5; rule
  Q1 (recommended: a PWB delta covering /api/poc/polaris and
  /api/poc/briefing together; the existing-route arm named) and, if it
  clears, Q2 (recommended: mint maxBriefingResponseBytes, with the
  PWB-REQ-006 fold-in question attached); build slice 3 once ruled,
  with the breach body as decided (Q3), on either side of M4's landing
  (Q4); defer slice 4
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
trigger — to the owner as one batched decision. If the owner also
rules that a third ceiling stales PWB-REQ-006's two-sink text, the
registry delta folds into Q1's PWB delta and the two-step act becomes
one act over one package.

**If Q2's default holds instead** (reuse `maxMachineResponseBytes`):
slice 3 ships as soon as Q1 clears, with the 20 KB figure enforced only
by a test assertion, disclosed in the evidence file as a bound without
a registry gate behind it.

**Sequencing against M4 (Q4, decided in this packet):** nothing here
blocks slice 3 on M4's landing order; record in `syzygy-dov.4`'s notes
that the briefing's own oracle will pick up M4's routed reasons
automatically once it lands, so no rework is expected either way.

## Review 1 and repairs (2026-09-14)

An independent fresh-context review of this packet (read-only; only the
artifact, its governing references and the questionnaire invariant) is
retained verbatim at
`docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-RAW.md` (34023 bytes,
sha256
`73b1596137fe2e02f5d6af781e896b33296d8871059715f582cafcb7f14b3aed`,
computed by `sha256sum` this session). It reviewed the packet at 62830
bytes, sha256
`bd93b4f3dd65c3e57c8d749cceb2e70d150141caf7d24f973f7f725088eeebeb`, and
the evidence record at 11502 bytes, sha256
`7e733323b7f8b6ebf4a76c775b2ca7f0cf1b534e8fbecb5a0502324058c437e9`, both
tracked at commit `1afa3d0`. Its verdict word, copied exactly: **REVISE —
six blocking, twelve non-blocking, four editorial**. Every one of the
twenty-two findings was re-derived against source and the retained
capture — not assumed correct — before being applied: the literal counts
by `bytes.count` over the raw file and `str.count` over the decoded
text, the 415 item ids by class, the joins of `switchboard-identity`
through `proposedWork` and the intent entity, both one-claim
compositions from exact field paths, the 18,710 / 18,719 key-spelling
pair, the act's six bullets, the nine-field packet against the seven
rendered `data-parity-field` values, and every line-number row by
`grep -n`. One finding's figure was not adopted as stated: F7's
3,198-byte composition is one lawful method among several, so this
packet publishes its own two compositions with their field paths rather
than the reviewer's number, and withdraws the first draft's figure and
its "sevenfold" claim. Every edit below was made after that review, so
by verification rule 10 the review binds the bytes it names and not
these; a second fresh-context review follows, and its raw will be a
second `-RAW.md` file, never an overwrite.

| Finding | Severity | Disposition |
|---|---|---|
| F1 `forbidden` is 3 on this capture, not 0 | blocking | Re-derived and confirmed (3 and 3, `bytes.count` and `str.count` agreeing; all hits Butlers bead titles). Gate 1 item 4, the literal table and the summary restated: zero prohibitions of Syzygy's own authority, with the withdrawn sentence kept |
| F2 the worked example's chain is applicable, and the subject count is four, not three | blocking | Re-derived and confirmed (`currentAuthority.claim.claimId` equals the subject; `intent:req-switchboard-identity-001` and two relationships join it; `MaterializationGoverningIntent.requirementId` was the missing fourth). Subject-naming finding rewritten as four literals with `switchboard-identity` the join point; `claim:item:topology-component:1:Spawner` is the not-applicable illustration; slice 3, RFC8-21 reading, S6 and the summary follow |
| F3 S2 mints an Unknown reason outside RFC2-24's closed twelve | blocking | Re-derived and confirmed (`no-such-claim` occurs 0 times in `rendering-vocabularies.md`; lines 44–50 quoted). Slice 3's unresolvable-selector design, success criterion 1 and S2 restated as a typed not-found disclosure with no `reason` slot; PWB-REQ-007 lines 447–448 quoted |
| F4 `PwbResourceLimits` has seven fields, not two | blocking | Re-derived and confirmed. Q2 and the line-number table say "seven fields, of which exactly two are response ceilings" |
| F5 the line-number re-verification table is itself unreliable | blocking | Re-derived by `grep -n` over every row; four rows were wrong (`MaterializationPacket` 20–30, `buildMaterializationPacket` 43–65, `buildTrajectoryMaterializationPacket` 31–37, `boundedResponse` 137–142 — the first draft cited the type's range for the function). Corrected in the table and at each in-text cite, withdrawn values kept in the table |
| F6 the dispatch packet has nine fields, the page renders seven, so "byte-identical" parity is unachievable | blocking | Re-derived and confirmed (7 of 9 packet fields and 1 of 2 state fields have a panel counterpart; `targetBeadPrefix`, `governingIntent.designPath` and `at` do not). Success criterion 2, slice 1's parity test, S4, the design bar and Gate 2's PWB-REQ-020 reading restated: by value after unescaping, both denominators, the machine-only remainder recorded; why the Falsifier does not reach the packet stated and labelled [Inferred] |
| F7 the one-claim figure is not re-derivable and the two artifacts disagree | non-blocking | Re-derived; method-dependent (see the paragraph above). Two compositions published with exact field paths: 5,449 / 7,076 bytes (applicable chain) and 3,347 / 5,150 bytes (not applicable); "sevenfold" withdrawn; headroom stated as 20,480 / 7,076 |
| F8 the cross-capture comparison is a key-naming artifact | non-blocking | Re-derived and confirmed (18,710 with the dossier's `scope` key, 18,719 with `identity.scope`, on this capture). Table and Gate 1 item 1 now compare shares only and say so; the classes-plus-claim set recomputed the same way (148,780) |
| F9 the worked-example selector matches no claim in the population | non-blocking | Re-derived and confirmed (0 of 415; every id is `claim:item:<class>:<key>`). Spelled correctly everywhere; slice 3's selector paragraph states the id form with its denominator |
| F10 the 511-byte item record does not reproduce | non-blocking | Re-derived and confirmed: 661 bytes compact, `claim` sub-object 504. Corrected, withdrawn value kept |
| F11 PWB-REQ-006 is never cited, and it governs two of the four questions | non-blocking | Confirmed. PWB-REQ-006 quoted in relevant part in Gate 2; Q2 now also asks whether a third ceiling amends its two-sink text and folds into Q1's delta; Q3's decision cites its "population counts" wording |
| F12 Q2's "without new code" is false, and the restraint is applied asymmetrically | non-blocking | Confirmed (`ResponseLimitIdentity` is a closed two-literal union at `routes.ts` 111). Q2 states the closed-type widening plainly and defends the asymmetry: Q2 widens under an owner act, Q3 declines to widen on the implementation's own authority |
| F13 Gate 5's warrant for slice 2 is circular, and the reading is unlabelled | non-blocking | Confirmed. Gate 5 now answers the minting question on PWB-REQ-005's "every human and machine rendering of the authorization basis" ground, labelled [Inferred], with the recorded-finding fallback naming L5-F9; Gate 2's PWB-REQ-020 scope reading labelled [Inferred] |
| F14 slice 2's enumeration of the act's prohibitions is three bullets short | non-blocking | Re-derived and confirmed (six bullets, lines 70–84). All six enumerated with their lines; the table is "exactly six rows" and the registration fixture asserts six |
| F15 the collision analysis reads 2 of 8 M4 slices and 1 of 6 M2 slices | non-blocking | Re-derived and confirmed. Denominators stated (8 of 8, 6 of 6, 4 of 4 with M3's five `polaris.ts` regions); M4 slice 8 (`materialization.ts` 9–65), slice 4 (`model.ts` 710–750, adjacent to 707) and slice 5 (`routes.ts` 34–96) added; M3's committed diff marked [Unknown] |
| F16 Q3 and Q4 are not genuine hard human gates | non-blocking | Accepted. Both decided in the packet under "Decided in this packet, not put to the owner", reasoning shown, numbers kept; the owner table is Q1 and Q2; summary, order, handoff and the P-72 row follow |
| F17 a lawful, cheaper arm for Q1 is never named | non-blocking | Accepted. The existing-route arm (`GET /api/poc` with a selector) named in Q1 with why it is not recommended, labelled [Inferred]; the order and register follow |
| F18 zero [Unknown] labels in the document the owner reads | non-blocking | Accepted. The evidence file's four `not_verifiable_this_session` entries carried into Collision and sequencing as four [Unknown] bullets |
| F19 ten code spans are broken across a line break | editorial | Confirmed; all ten rejoined or rephrased so no span crosses a line |
| F20 nine over-width lines outside tables and fences | editorial | Confirmed; line 795 reflowed, and the 79-column baseline line with it; the remaining over-width lines are single unbreakable paths or headings, as the review allows |
| F21 PWB-REQ-020 is introduced as "quoted in full" and is not | editorial | Confirmed; "quoted in relevant part", naming which bullets are omitted |
| F22 four remaining citation imprecisions | editorial | Confirmed; `ResponseLimitFailure` 113–124 with `population` at 120–122, `MaterializationRecord` 67–78 with `createdAt` at 71, and the POC spec file named at each line-26 cite |

Recommended answers changed by this review: Q3 and Q4 are withdrawn as
owner questions and decided above; Q1 gains a third lawful arm, named
and not recommended; Q2 gains the PWB-REQ-006 fold-in question and
states the closed-type widening it had denied. Q1's and Q2's
recommendations themselves are unchanged.
