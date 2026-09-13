# Vision pursuit — Polaris — 2026-09-13

Planning artifact only. Nothing here is authority, nothing here is a review verdict, and no
bead filed from it is runnable until the owner closes the gate bead named at the end. Claims
are labeled `[Observed]`, `[Inferred]` or `[Unknown]` as the agents labeled them; every
per-agent finding and move, with its full evidence list, is in
`docs/pursuits/2026-09-13-vision-pursuit-data.json` (access pattern below). The raw harvest
working file `docs/pursuits/2026-09-13-vision-pursuit-harvest.json` sits beside it.

## Provenance

| Item | Value |
|---|---|
| Run | first Polaris pursuit; no prior dossier, so the tier board carries no movement column |
| Syzygy | audited at f4589e2 (clean); main moved to 63f0e50 (PR #32, generator merged) and 1932f74 (PRs #33, #34) during the run; only the second move touched renderer-adjacent files and neither touched the renderer, core pipeline or routes |
| Butlers | rendered evaluation at Butlers commit 66ed58f (as-of 2026-09-10); machine captures at Butlers head 7c8743f63 (2026-09-12) |
| Captures | the owner's loopback daemon served a 2,087,400-byte `/polaris`; a fresh private daemon at f4589e2 / 7c8743f63 answered `/polaris` with HTTP 503 `response-limit-breached` |
| Fan-out | 11 surface audits (Sonnet) and 6 ideation lenses (Opus) in six hourly batches of at most three, read-only, deduped against the known ledger below; the orchestrator recorded one finding of its own (P0-CEILING) |
| Owner brief | max 3 concurrent workers, staggered over the day, Polaris focus, pending beads taken into account |

## North star (quoted)

From `.syzygy/governance/doctrine/vision.md`: "Showing the truth is the soul of the product."
The owner's own sentence: "open one place, understand what a project's vision and goals are,
tune or guide them if necessary, and know that the rest of the project will (eventually) mold
itself to fit around that goal." VIS-1 orders the values: truth and observation determinism,
then comprehension of the truth's presentation, then momentum, then breadth and fidelity, then
reproducibility of derived convenience. VIS-2: no evidence means Unknown, never success. VIS-3:
every normative artifact stays digestible by a human unfamiliar with the project. VIS-7: every
rendered link resolves and every encoding means what its legend says. Syzygy is "not a
documentation portal": the escape property is that intent changes produce dispatched work, for
two first-class consumers, the owner and agents. The product goal stated 2026-09-12:
generalizable LLM-assisted manifesto generation across projects; Butlers is a proving case.

## Tier board

First run: tiers only. Every tier is the auditing agent's verdict against the ideal, not a
pass/fail, and every gap statement in full is in the data file under `agents[].gap`.

| Surface | Agent | Tier | One-line gap |
|---|---|---|---|
| First reading (opening through architecture) | S1 | solid | Manifesto-voice prose and real progressive disclosure, but literal extraction plus hand-pinned byte offsets rather than generation; no Unknown ever shown in the first reading; 625 KB of narrative JSON before the first heading |
| Navigation shell and accessibility | S2 | functional | Keyboard mechanics are sound; the shell does not scale to the page it indexes (271 disclosures and 372 links each share one accessible name; h3 to h6 heading skips; about 228 Tab presses to reach the catalog) |
| Architecture account and diagrams | S3 | solid | Careful, provenance-bearing craft in a vocabulary that cannot express fan-in, fan-out or hierarchy; relations diagrams hide their only signal from assistive technology |
| Catalogs and claim states | S4 | functional | Honest (0 of 402 rows over-claim) but a records dump: 78% of catalog rows restate their own key as their statement, and baseline-spec alone is 17% of the page |
| Source provenance and exact-source route | S5 | functional | Genuinely good idea, screened and digest-verified, reaching 185 of 271 sources at whole-file grain; every one of 699 tuples says fresh by constant |
| Machine endpoints and human-machine parity | S6 | weak | The machine consumer gets the internal model dumped whole: no schema, no self-links, no query, no caching, no stable cross-revision id |
| PWB pipeline core | S7 | solid | Deterministic and disciplined; one grammar failure discards a source's already-succeeded classes, and an unenumerated heading is invisible rather than Unknown |
| Renderer modules (engineering) | S8 | functional | Escaping is real but caller-convention only; one 1,615-line module carries the page; 49.4% of bytes are machine metadata; the only mutation-kill record is bound to bytes that no longer exist |
| Generation kit and authoring path | S9 | weak | Well-written guidance around a path that breaks at its first documented command and whose flagship honesty field does not exist in the landed schema |
| Daemon operability | S10 | weak | World-class cold start, then blank: no status route, no request logging, failure detail discarded, no restart story |
| Visual language | S11 | weak | AA contrast and working density, but no design system: 12 of the claim-state glossary's states render through one CSS rule, palette colors carry unrelated meanings across surfaces, 35 ad hoc font sizes and 8 stray hex literals |
| Portability lens (second project) | L1 | weak | Architecture is portable, content is not: every project-specific value is a compiled constant with a test asserting byte-equality against the registry that already holds it |
| Owner core-loop lens | L2 | weak | World-class at cold-open, absent from notice, tune, dispatch, land and account: one link to Trajectory in 1,061, zero forms, no route from an Unknown to the one lawful action |
| Generation-loop lens | L3 | weak | A superb bounding layer around a hole where the honesty contract should be: no Unknown in the schema, silent deletion possible, review not independent, no owner exit |
| Evidence-currency lens | L4 | weak | 699 claims say fresh against evidence three days old; 71 of 271 sources have changed and the surface has no vocabulary for saying so |
| Agent-consumer lens | L5 | weak | A very good observation record with no briefing, no dispatch and no return path: the agent's orientation is 0.34% of a 5.5 MB payload, requirement text is only on the unauthenticated HTML channel, and the Inferred label reserved for agent output cannot be constructed by any module |
| Cross-surface and three-state lens | L6 | weak | Four pages sharing a stylesheet and a nav bar: 0 of 1,439 hrefs go from a claim to its subject on another surface; the word "desired" occurs once |

## Systemic themes

Seven patterns recur across independent agents. Each names its exemplars by agent finding id;
the finding text and evidence are in the data file.

1. **Page size is linear in the catalog, and the ceiling has already been crossed.** The
   orchestrator's P0-CEILING: at current Butlers head `/polaris` is 2,132,656 bytes against a
   2,097,152 ceiling and serves nothing. The cause is structural, not a Butlers quirk: 49.4% of
   the captured page is machine metadata (S8-F1), 699 claim-tuple spans spend 407,732 bytes to
   show 45 bytes each, two compliance flags are stamped on 2,615 elements individually (S8-F2),
   identical item tuples are never collapsed (S4-F1), 78% of catalog rows carry a statement
   byte-identical to their key (S4-F2), baseline-spec is 356,032 bytes for folder names (S4-F3),
   and a 625 KB narrative JSON blob sits before the first heading (S1-F3). The P-63 trim bought
   headroom that Butlers growth has consumed; the next trim must change the growth exponent.
2. **Time is invisible and freshness is a constant.** All 699 tuples render `fresh` from a
   literal in the model builder while `packages/cap1-core/src/staleness.ts` ships the engine the
   page's own legend describes (S5-F1, L4-F2); 71 of 271 sources changed since the rendered
   evaluation and 135 of 402 rows cite bytes that no longer exist (L4-F1); no instant is visible
   in the first 656,322 bytes (L4-F3); asOf is re-minted per build without re-observation (L4-F4);
   the legend promises three states the design cannot produce (L4-M7); 12 tier, freshness and
   challenge states render through one CSS rule, so none can be sensed before it is read (S11-F1).
3. **Honesty holds in the pipeline and leaks at the gates.** POC-REQ-060's encoding invariant is
   falsified live: 688 Observed and 11 Unknown claims share one grey, and the checker's
   denominator is 4 pages against 1,085 tuples (L6-F3). The generator's provider schema has no
   Unknown although its prompts instruct the model five times to use one (L3-F1, S9-F2); edit and
   repair can delete a supported claim silently (L3-F2); the fidelity verdict is the author's own
   severity (L3-F3, L3-F4). In the pipeline, one class's grammar failure erases a source's other
   classes (S7-F1) and an unenumerated heading is neither counted nor Unknown (S7-F2). On the machine channel `counts.unknown` is 0 beside a sibling claim whose own label is Unknown, with no denominator (L5-F6), and the colour for no-evidence also backs proposed-not-authority at a 1.11:1 contrast from the amber beside it (S11-F2).
4. **No route from an Unknown to the one lawful action.** The intent surface carries no owner
   action and three of four propagation edges are permanently Unknown (L2-F1, L2-F2); the
   generator loop is terminal at awaiting-rendered-review with no route serving the preview and
   no act binding output (L3-F5); the home page is a second index, advertising a Polaris two
   model-generations old (L2-M9, L6-F1).
5. **Portability is architectural, not actual.** Every stage is pure and injectable, yet 74 of
   133 modules name the proving case (L1-F11); locator, profile, ontology, precedence rows and
   the page's own identity are compiled literals (L1-F1, F3, F4, F5); the kit's one command fails
   from a fresh checkout and its example fails its own validator (S9-F1, S9-F2).
6. **Three surfaces share nothing at claim level.** Zero cross-surface claim links, one
   escape-property edge under three identities with no shared key, `model.surfaces` false for
   Polaris by two orders of magnitude (L6-F2, F4, F5); the machine endpoint is a raw model dump
   with no schema, no self-link and no stable join key (S6-F1, F2, F5); an agent downloads 5,508,208 bytes
   for an 18,710-byte briefing and still gets no requirement text, which only the unauthenticated HTML
   route serves (L5-F1, F2); three epistemic shapes share one payload and the weakest governs the
   propagation graph while the Inferred label reserved for agent output is unconstructible (L5-F4, F5).
7. **Operability is blind after minute one.** No status route, no non-2xx logging, and the
   ceiling breach in theme 1 is the clearest case: the 503 body is its only trace (S10-F1, F2;
   S7-F3 shows the ledger has no output-side field to wire into).

## Ranked moves

Ranking rule: the structural fix for the crossed ceiling first, because a page that serves
nothing serves no doctrine; then the VIS-2 honesty gaps in order of owner value over build cost;
then the moves that extend the loop toward the escape property; then engineering hygiene.
`owner_value` and `build_cost` are the agents' 1 to 5 estimates, merged where several agents
proposed the same move. Prerequisite classes: none (POC improvement-cycle bead), spec amendment
(CC-REV-2), owner act (a registry, policy or authorization change). Every move is planning; the
L2 lens's governance note applies to all of them: an implementation bead is lawful only when it
traces to a POC-REQ/PWB-REQ clause or a recorded review finding, so a pursued move re-enters
through the feature-request funnel, never straight into execution.

### M1 — Make page size sublinear in the catalog (the P0-CEILING answer)

- **What.** Collapse identical item tuples to one table-level statement (S4-M1); render
  statement-less extraction classes as a compact list, not a claim-tuple table (S4-M2); hoist the
  constant evaluation id and every page-invariant tuple field to one ancestor (S8-M1); make the
  two compliance flags ancestor-scoped with a documented inheritance rule (S8-M2); move the
  narrative JSON payload out of the reader's scroll path (S1-M1). Re-measure on a committed clean
  tree per the measurement lesson in `AGENTS.md`.
- **Why.** P0-CEILING [Observed]: declared 2,097,152, observed 2,132,656 at Butlers 7c8743f63;
  the page serves nothing and logs nothing. VIS-1 (comprehension by simplifying presentation,
  never content) and VIS-2 (a page that cannot be served renders no truth). Migration cost is
  waived inside the POC; the parity sweep's `<tbody>` and `<table>` assumptions in the guardrails
  are the one place a hoisted attribute silently zeroes a family, so hoist onto the region div.
- **Evidence.** `apps/three-surface-poc/src/polaris.ts` lines 306-336 and 541 (tuple emission),
  lines 582-606 (class block), line 314 (evaluation id per span);
  `packages/three-surface-poc-core/src/project-shape-extraction.ts` lines 491-497 (statement-less
  classes); capture: 699 identical `data-evaluation-id`, 2,615 flag pairs, baseline-spec 356,032
  bytes, narrative JSON bytes 30,920 to 656,251.
- **Prerequisite.** None. **owner_value 5 / build_cost 3.**
- **Slices.** (1) Measure per-class byte cost on the retained capture and write the target
  exponent. (2) Compact-list renderer for statement-less classes, keeping tuple and Exact-text
  link per item. (3) Tuple collapse with an `N x` count and a parity-sweep update that checks
  every rendered tuple against its machine claim by id. (4) Ancestor hoists with a build-time
  assertion that fails if a page ever carries two evaluation ids. (5) Narrative JSON as a tail
  script or a sibling route; browser tests re-run. (6) Re-measure both host forms; retire the
  2026-09-07 trim record as history, never edit it.

### M2 — Evidence currency: compute the horizon, wire `assessCurrency`, make the legend true

- **What.** Compute the evidence horizon at build time (rendered evaluation pin versus current
  Butlers head) and render drift as movement (L4-M1); put the horizon where the reader opens and
  give the machine payload an `evidence` block (L4-M2); forbid asOf from moving without a
  re-observation and make re-evaluation a cheap recurring operation (L4-M4); announce a lapsed
  reviewed reading selection instead of falling back silently (L4-M5); declare currency bounds
  per claim class as a registry input and route freshness through cap1-core's engine (S5-M1,
  L4-M3); until then, stop the legend promising states the design cannot produce (L4-M7).
- **Why.** VIS-2's currency-bound sentence is bypassed by a constant; the two halves of Syzygy
  disagree about the same rule (L4-F2). 135 of 402 rows say fresh about bytes that have changed
  (L4-F1 [Observed], measured two ways). VIS-7: the freshness legend does not mean what it says.
- **Evidence.** `packages/cap1-core/src/staleness.ts` lines 87-155 (unused engine);
  `packages/three-surface-poc-core/src/project-shape-model.ts` lines 162-193 (two `FRESH`
  constants); `apps/three-surface-poc/src/polaris-copy.ts` lines 46-49 (legend); capture: 0 ISO
  instants before byte 656,322; `data-epistemic-freshness` is `fresh` 699 times.
- **Prerequisite.** None for the horizon, legend and asOf slices; owner act for the currency
  bounds (a registry `resourceLimits`-class amendment). **owner_value 5 / build_cost 2 to 3.**
- **Slices.** (1) Legend truth: remove or grey the two unreachable states with a copy-oracle
  test. (2) Horizon computation from the head resolution `git-observation.ts` already does;
  render "N sources changed since this evaluation" in the opening band. (3) `evidence` block in
  `/api/poc` and `/api/poc/polaris`. (4) asOf immutability test: mutate the wall clock, assert
  asOf unchanged without re-observation. (5) Registry bound declared, `assessCurrency` wired, a
  fixture whose asOf exceeds the bound renders stale at least once.

### M3 — Honest encoding at the gate: POC-REQ-060 on Polaris and a real sweep

- **What.** Give Polaris the declared Observed/Unknown encoding and replace the four-page checker
  with the sweep the requirement specifies over every rendered tuple (L6-M1); show one real
  Unknown before the reader leaves the first reading (S1-M2); exercise the per-item Unknown route
  with a fixture independent of live Butlers content (S4-M5); extend the encoding-table pattern to
  the seven tier, four freshness and one challenge values so legend and rendered class cannot drift
  (S11-M1); give proposed-not-authority its own token out of the no-evidence colour's way (S11-M2).
- **Why.** L6-F3 [Observed]: 688 Observed and 11 Unknown claims render in one grey; the checker
  denominator is 4 pages against 1,085 tuples (verification rule 4). VIS-2 and VIS-7 together:
  Unknown must never look like success, and an encoding must mean what its legend says.
- **Evidence.** `apps/three-surface-poc/src/design-tokens.ts` lines 16-29 and 130-131;
  `apps/three-surface-poc/src/polaris.ts` lines 305-316, 1290, 1300;
  `apps/three-surface-poc/src/surface-routes.test.ts` lines 64-100; `apps/three-surface-poc/src/polaris-copy.ts` lines 30-52 (twelve states) against one `.claim-tuple` rule at `polaris.ts` lines 1296-1299; capture bytes 656,326 to
  912,385 contain zero visible Unknown occurrences; the item-row Unknown branch is exercised by 0
  of 402 live rows (S4-F6 [Inferred]).
- **Prerequisite.** None. **owner_value 5 / build_cost 2 to 3.**
- **Slices.** (1) Distinct token for Unknown in the design tokens and the tuple span. (2) A
  population sweep over every `data-claim-id` on every page with a stated denominator. (3) One
  first-reading Unknown rendered in place with its route. (4) A fixture that forces an item-level
  Unknown and asserts the route renders. (5) Tier, freshness and challenge encoding tables driving
  the tuple class and a generated legend, with the first-reading textual-completeness sweep extended
  to them. (6) A proposed-state token at real perceptual distance from amber and unknown.

### M4 — Close the owner loop: a route from every Unknown, home as the day-opening, and run the return path once

- **What.** Give the propagation Unknowns a route and make that route the one lawful action
  (L2-M1); open with a "what needs you" band derived from the actionable Unknown routes (L2-M2);
  one click from an Unknown to a drafted owner act, drafted and never performed (L2-M3); make `/`
  the day-opening rather than a second index, and make `model.surfaces` true or delete it (L2-M9,
  L6-M4); give a resolution route a machine form with actor, verb and target, and make
  "no route modelled" a value so an empty array stops being legal (L5-M4); run the built, lawful
  return path once end to end (materialize, a human-launched agent on the worker change seam, the
  operator capture step, the next evaluation narrowing three edges from Unknown) and record it as
  the V0 agent-consumption artifact (L5-M7); later, the owner-released packet queue (L5-M5).
- **Why.** "Not a documentation portal": the escape property is dispatched work, and today the
  intent surface has no owner action at all (L2-F1 [Observed]: 1 Trajectory href in 1,061, zero
  forms). VIS-4 is respected by drafting, never performing. VIS-5 and doctrine v1 lines 38-43
  name the loop this move restores.
- **Evidence.** `packages/three-surface-poc-core/src/model.ts` lines 563-598;
  `packages/three-surface-poc-core/src/project-shape-model.ts` lines 89-128;
  `apps/three-surface-poc/src/materialize-action.ts` lines 17 and 55-80;
  `packages/three-surface-poc-core/src/owner-act-record.ts` lines 1-45;
  `apps/three-surface-poc/src/routes.ts` lines 34-96 (home);
  `packages/three-surface-poc-core/src/test-artifact-verification.ts` lines 11-19 and 73;
  `apps/three-surface-poc/src/capture-test-artifact.ts` lines 3-7; captured `api-poc.json`: 1,137 of
  1,149 route arrays empty, test-artifact verification `unknown`; capture: gaps section is the 6th h3
  of the 7th h2; home is 38,706 bytes of three panels plus Orrery's exact tables.
- **Prerequisite.** None for routes, band, drafted act, machine-form routes and the one run (confirm
  the run is covered as an improvement-cycle exercise of built capability first); owner act for making
  the materialize packet a function of the selected claim (L2-M4) and for the packet queue (L5-M5).
  **owner_value 5 / build_cost 2 to 3.**
- **Slices.** (1) Enumerate the Unknown reasons and map each to its lawful route. (2) Opening
   band listing actionable Unknowns with counts and routes. (3) Drafted-act generator that emits
   a packet under the decisions README's ceremony with a `DRAFT, binds nothing` head. (4) Home
   rewritten from `model.surfaces` after that field is made true by construction. (5) Widen the
   twelve-entry route table once, shared with the relationship routes. (6) Run the return path once,
   retain stderr, the test-artifact record and the before/after tuples; report honestly if an edge
   stays Unknown. (7) Packet queue behind its act.

### M5 — The agent's briefing: a task-scoped route, the dispatch packet and the prohibitions on the machine channel

- **What.** One credentialed `GET /api/poc/briefing?for=<selector>` returning a bounded document
  composed only of fields the model already holds: evaluation identity and consent scope, authority
  rows with independence disclosures, the RFC8-21 chain state for the subject with each link
  Observed or Unknown-with-reason, every Unknown touching the subject with its route, the exclusions
  touching it, and the exact-source route for each cited requirement, measured against a 20 KB
  ceiling (L5-M1); serve the exact materialization packet read-only beside `proposedWork` with a
  dispatch-state discriminant, keeping the POST and its human trigger unchanged (L5-M3); a
  top-level `authority.mayNot` array of constraint identities each carrying its act and digest, so
  absence of a constraint is never permission (L5-M6).
- **Why.** Doctrine names agents a first-class consumer from day one. Today the agent pays
  5,508,208 bytes for an 18,710-byte briefing (L5-F1 [Observed], 0.34%), gets no requirement text on
  the credentialed channel while the unauthenticated HTML route serves it (L5-F2), never sees the
  dispatch packet (L5-F3), and reads zero prohibitions in the contract it consumes (L5-F9). VIS-1,
  VIS-3, VIS-4 (the trigger stays human), VIS-5, SEC-1.
- **Evidence.** captured `api-poc.json` (5,508,208 bytes; `workItems` 2,400,832 bytes for 7,396
  beads, `codeStructure` 1,557,863 bytes for 6,466 paths; `externalRef` and `governingIntent` occur
  0 times; `materializedBeadId` null); `apps/three-surface-poc/src/routes.ts` lines 196-200,
  222-223 and 232-239 (credential classes per route); `apps/three-surface-poc/src/browser-origin.ts`
  lines 27-37; `apps/three-surface-poc/src/materialize-action.ts` lines 17 and 55-80;
  `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` line 81.
- **Prerequisite.** None. **owner_value 5 / build_cost 2 to 3.**
- **Slices.** (1) Packet and dispatch state lifted into the model beside `proposedWork`; parity
  sweep denominator extended to its seven fields; counterexample that a GET never creates a record.
  (2) `mayNot` rows derived from the three authority artifacts the body-read authority already
  parses, rendered on the human surfaces from the same field; withdraw one authority in a fixture
  and assert its row changes. (3) Briefing route for `for=claim:<id>` only, served through the
  existing bounded response with its own declared ceiling and a published measurement; every field
  asserted derivable from `/api/poc`'s own bytes. (4) Path and change selectors after that.

### M6 — Generator honesty contract and kit onramp

- **What.** Give the provider schema somewhere to put Unknown and make omission impossible to
  express by silence (L3-M1, S9-M2); per-entry fidelity disposition with a verdict that is a
  function of the denominator (L3-M2); edit and repair account for what they changed and may not
  delete silently (L3-M3); make the documented one-command onramp succeed and add a fresh-install
  check (S9-M1); restate the no-egress boundary where an operator acts (S9-M4); close the
  diagram, deep-dive and glossary promise-to-schema gap in one deliberate direction (S9-M3).
- **Why.** VIS-2 inside the product's stated goal: the kit's flagship honesty claim does not
  exist in the code it points to (S9-F2 [Observed]) and the prompts ask for a representation the
  schema cannot hold (L3-F1). VIS-3: an onramp that fails on its own command is not digestible.
- **Evidence.** `packages/polaris-generation-core/src/provider-draft.ts` lines 18, 30, 33,
  109, 131-152; `packages/polaris-generation-core/src/prompts.ts` lines 6, 18, 22;
  `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md` lines 52, 302
  and 1015; `packages/polaris-generation-core/README.md` demo command fails with TS2307 from a
  fresh checkout; `docs/polaris-generation/example.json` fails the landed validator.
- **Prerequisite.** None; these are already-authorized generator implementation tasks that the
  landed code missed, so confirm against `openspec/changes/polaris-manifesto-generation/tasks.md`
  before filing to avoid a duplicate of an unchecked task. **owner_value 5 / build_cost 2 to 3.**
- **Slices.** (1) Install line plus CI fresh-install assertion. (2) `disposition` field on
  inventory, plan and draft; validator requires one per requested asset; regenerate the example
  from a real validation. (3) Per-entry coverage disposition; verdict computed, never
  self-declared. (4) Edit/repair diff record; deletion requires an explicit disposition. (5)
  Boundary restatement in the two authoring files.

### M7 — Close the generation loop: structural independence, observation-typed sources, self-corpus proof, an exit

- **What.** Per-stage provider routes and a fidelity envelope that cannot contain the authoring
  conversation (L3-M4); type the generator's source as an observation with durable citation
  identities, not a string pair (L3-M5); prove the whole loop on Syzygy's own corpus with a
  scripted provider before asking for egress (L3-M6); serve the draft at a route and make the
  owner's one action a drafted act (L3-M7); name the egress act the loop waits on and what it
  buys (L3-M9); stage-scoped inputs and resumable attempts so regeneration is cheap (L3-M8).
- **Why.** The loop has no owner and no exit (L3-F5 [Observed]); citations are array indices
  (L3-F6); the review is the same route one stage later (L3-F3). The product goal is a loop
  that runs on a second project; a loop nobody can finish on the first project cannot.
- **Evidence.** `packages/polaris-generation-core/src/pipeline.ts` lines 19, 263, 272;
  `apps/three-surface-poc/src/polaris-generation/draft-preview.ts` lines 11 and 23;
  `apps/three-surface-poc/src/polaris-generation/pipeline-demo.ts` lines 33-37;
  `apps/three-surface-poc/src/routes.ts` lines 21-22 (no generation route);
  `.syzygy/governance/decisions/POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md` line 42.
- **Prerequisite.** None for independence, typing, self-corpus proof and the route; owner act
  for any egress. **owner_value 5 / build_cost 3.**
- **Slices.** (1) Source type carries repository, revision, path, object id; preview cites by
  identity. (2) Separate provider port per stage; fidelity envelope built from the draft alone.
  (3) Scripted provider over Syzygy's own doctrine and specs; record as evidence. (4) Draft route
  behind the machine credential; drafted-act packet. (5) Egress act named in the kit's start
  path with its cost. (6) Stage-scoped resume.

### M8 — Portability: the profile as a loaded, digest-bound registry input

- **What.** Load the observation profile from the registry instead of hard-coded copies
  (L1-M1); bind the locator from the consent record's declared mapping (L1-M2); derive the
  rendered project identity from the model and template every project noun out of the copy
  table (L1-M3); converge on one profile schema with the generator's admitted-input profile
  (L1-M6); a portability predicate that fails when a proper noun enters POC source outside the
  profile (L1-M9); prove portability against the Syzygy repository itself under a test-only
  self-profile (L1-M5); separate seeded Butlers entities from observed shape (L1-M7).
- **Why.** The stated product goal is generalization; 74 of 133 modules name Butlers (L1-F11
  [Observed]) and the registry is a checksum, not a source (L1-F1). VIS-1 and SEC-1 (locator).
- **Evidence.** `packages/three-surface-poc-core/src/project-shape-observation.ts` line 21;
  `packages/three-surface-poc-core/src/project-shape-manifest.ts` lines 38 and 47;
  `packages/three-surface-poc-core/src/project-shape-extraction.ts` line 689;
  `apps/three-surface-poc/src/git-observation.ts` lines 6 and 40;
  `apps/three-surface-poc/src/polaris-copy.ts` lines 26, 27, 60, 235;
  `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`.
- **Prerequisite.** None for the predicate, identity, locator and self-profile proof; owner act
  for loading the registry as an input (it changes what the registry binds). **owner_value 5 /
  build_cost 5, sliced so the first three land at cost 2.**
- **Slices.** (1) Predicate first: enumerate the 74 modules, allowlist the profile, fail on the
  75th. (2) Identity from the model. (3) Locator from consent. (4) One profile schema shared with
  the generator before two exist. (5) Registry-loaded profile under an owner act. (6) Self-profile
  proof over Syzygy.

### M9 — One identity, one epistemic shape, one vocabulary across the surfaces

- **What.** Emit the cross-surface links whose addresses already exist (L6-M2); name desired,
  execution and observed on the surfaces that hold them (L6-M3); one claim identity across
  surfaces with `data-claim-id` on every page (L6-M5); the per-claim tri-state ribbon with Unknown
  and a route in the two empty slots (L6-M6); move Polaris's observed band to the surface that
  owns it (L6-M7); one epistemic record shape across the model with an Inferred arm that is the
  agent's landing zone, excluded from every Observed denominator (L5-M2); adopt RFC1-25's names for
  the edges the POC emits and flag the three outside the closed set (L5-M8).
- **Why.** The doctrine's three states are the product's spine and the word "desired" occurs
  once across four pages (L6-F7 [Observed]); 0 of 1,439 hrefs cross surfaces at claim level
  (L6-F2). Three epistemic shapes share one payload and the weakest governs the propagation graph
  (L5-F4); the label doctrine reserves for agent output cannot be constructed (L5-F5); 1 of 8 edge
  kinds matches RFC1-25, so a name join silently returns nothing (L5-F8). VIS-1, VIS-2, VIS-7.
- **Evidence.** `apps/three-surface-poc/src/polaris.ts` lines 256-295 and 1156-1171;
  `packages/three-surface-poc-core/src/model.ts` lines 43-45; `packages/cap1-core/src/vocabulary.ts`
  lines 64-65; `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`
  line 463;
  `apps/three-surface-poc/src/trajectory.ts` lines 137-192; `apps/three-surface-poc/src/orrery.ts`
  line 157; capture: `data-claim-id` 699 on Polaris, 0 on the other three pages.
- **Prerequisite.** None for links and naming; spec amendment for the shared identity and the
  ribbon (the cross-surface identity system is a declared deferral in the POC spec).
  **owner_value 5 / build_cost 2 for the first two, 4 for the rest.**
- **Slices.** (1) Links from each claim to its subject on the other surfaces, with an oracle
  over POC-REQ-053. (2) State labels in each surface's header and legend. (3) Spec delta for the
  join key, the unified epistemic tuple (PWB-REQ-007) and the RFC1-25 edge names, drafted together
  so one join key is built, not two. (4) Shape unification with no Inferred arm and no behaviour
  change; then the Inferred arm with its exclusion battery. (5) Ribbon behind the delta.

### M10 — The machine consumer gets a contract

- **What.** Publish a versioned schema for `/api/poc` and `/api/poc/polaris` stating which
  declared enum members are populated (S6-M1); self-link the endpoints from the route table so
  they cannot drift (S6-M2); conditional GET keyed on `inputsDigest` and gzip (S6-M3); a stable
  cross-revision logical id beside the revision-scoped anchor id (S6-M6); document the
  equality contract in-payload (S6-M5); the `evidence` block from M2 (L4-M2).
- **Why.** Agents are a first-class consumer from day one and today read TypeScript to learn a
  field's meaning (S6-F2 [Observed]). VIS-1 and VIS-3.
- **Evidence.** `apps/three-surface-poc/src/routes.ts` lines 159-162 (the handler is
  `JSON.stringify(model)`); `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` lines 4-6;
  captured `api-poc.json` 5.5 MB with no links field; anchor vocabulary 99.8% one class.
- **Prerequisite.** None; populate-or-prune of the declared vocabulary (S6-M4) is a spec
  amendment and is listed, not scheduled. **owner_value 4 / build_cost 2.**
- **Slices.** (1) Static schema emitted at build from TSDoc, served unauthenticated. (2) Links
  map from the route table. (3) ETag and compression. (4) Stable id derived beside `targetId`.

### M11 — Operability: a status route, structured non-2xx logging, an output-side ledger

- **What.** One status route, human and machine, answering "what am I serving, from which
  commits, how old, and is it healthy" (S10-M1); log every non-2xx outcome as one structured
  stderr line and stop discarding DaemonStart failure detail (S10-M2); add `maxOutputBytes` and
  `chargeOutput` to the resource ledger so the response ceiling is budget-owned end to end
  (S7-M3); document and script the restart and upgrade path (S10-M3).
- **Why.** The ceiling breach in theme 1 left no trace but its own 503 body (P0-CEILING
  [Observed]); the ledger has no output-side field to wire into (S7-F3). VIS-2 applied to the
  operator: a daemon that cannot say it failed renders a false green.
- **Evidence.** `packages/three-surface-poc-core/src/resource-ledger.ts` lines 81-121;
  `apps/three-surface-poc/src/routes.ts` lines 99-151 (`boundedResponse`);
  `apps/three-surface-poc/src/main.ts` (failure `.detail` dropped); grep of both source trees
  finds no status or health route.
- **Prerequisite.** None for the route and logging; owner act for the registry
  `resourceLimits` schema change. **owner_value 5 / build_cost 3.**
- **Slices.** (1) Structured non-2xx line, including the 503. (2) Status route reading the
  same footer facts plus last-request outcomes. (3) Ledger output counter behind the registry
  amendment. (4) Restart script and doc.

### M12 — Retained evaluations, rendered delta, and the owner's note

- **What.** Retain the observation record and render a claim-state delta between two identified
  evaluations (L2-M6); the owner note as a Syzygy-unpromoted annotation promoted only by
  committing out to the governed plane (L2-M7); a dismissal with a live expiry (L2-M8).
- **Why.** "What changed since I last looked" is unanswerable (L2-F5 [Observed]) and VIS-6a, the
  owner recording that a rendered claim is wrong, is wholly unimplemented (L2-F4). Depends on M2's
  horizon and M10's stable id.
- **Evidence.** `apps/three-surface-poc/src/main.ts` line 134 (single observation at start);
  `packages/three-surface-poc-core/src/body-read-authority.ts` lines 754-766;
  `packages/three-surface-poc-core/src/walkthrough-judgment.ts` lines 810-823; the state
  directory holds only the machine credential.
- **Prerequisite.** None for retention and delta; owner act for the note (retention posture);
  spec amendment for dismissal. **owner_value 5 / build_cost 4.**
- **Slices.** (1) Write each evaluation to the state directory under its `inputsDigest`. (2)
  Delta view keyed on the stable id. (3) Note and dismissal behind their gates.

### M13 — Navigation at population scale

- **What.** Collapse the 271 source-record disclosures into one filterable, grouped source
  table (S2-M1); interpolate the item identity into every "Exact text" and "Source record"
  label (S2-M2); normalize markdown heading levels to the anchoring h3 (S2-M3); promote the
  outline from a collapsible to an always-reachable jump list (S2-M4); paginate or filter the
  largest catalog tables (S4-M6).
- **Why.** VIS-3: 271 disclosures and 372 links each share one accessible name (S2-F2
  [Observed]); about 228 Tab presses to the catalog (S2-F3). Interacts with M1: do the byte
  work first, then the shell.
- **Evidence.** `apps/three-surface-poc/src/polaris.ts` lines 818 and 1510-1538;
  `apps/three-surface-poc/src/polaris-copy.ts` lines 129 and 134; capture: zero h5 on the page.
- **Prerequisite.** None. **owner_value 4 / build_cost 3.**
- **Slices.** (1) Labels. (2) Heading normalization with a test on the h-level sequence. (3)
  Source table. (4) Jump list, with the fragment-in-details guardrail re-tested.

### M14 — Provenance depth: every digest reachable, every citation targeted, every catalog item deep

- **What.** Extend the exact-source route to every class the digest already covers (S5-M2);
  scope the route to the one requirement a citation names and scroll to it (S5-M3); one legend
  sentence decoding the source-identity grammar (S5-M4); state the item-count reconciliation
  beside the catalog (S4-M4); route catalog items into per-item depth pages instead of one
  hard-coded capability (S4-M3).
- **Why.** 86 of 271 sources show a digest nobody can verify against anything (S5-F2
  [Observed]); a hash is not provenance. VIS-3 and VIS-7.
- **Evidence.** `apps/three-surface-poc/src/verbatim-route.ts` lines 78-79 (the class gate);
  `apps/three-surface-poc/src/polaris-source.ts` lines 41-43;
  `apps/three-surface-poc/src/capability-detail.ts` lines 97-115 and 256-260.
- **Prerequisite.** None for the route work; spec amendment for per-item depth pages
  (PWB-REQ-015 band semantics). **owner_value 4 / build_cost 3.**
- **Slices.** (1) Drop the class gate for body-classified classes; say explicitly which classes
  remain digest-only. (2) Requirement parameter with scroll anchor. (3) Legend sentence and
  reconciliation line. (4) Depth-page template behind its amendment.

### M15 — Pipeline truthfulness at class granularity

- **What.** Narrow whole-source Unknown to whole-class Unknown per independently-extractable
  class (S7-M1); detect and flag an unenumerated catalog or root heading instead of skipping it
  (S7-M2); make tree-population rules declare their root-independence so an unread root index
  cannot leave modeled facts standing alone (L1-M4).
- **Why.** One grammar defect wipes three independent facts (S7-F1 [Observed]); a tenth
  category is invisible rather than Unknown (S7-F2), which VIS-2 rules out entirely.
- **Evidence.** `packages/three-surface-poc-core/src/project-shape-extraction.ts` lines 14-17,
  438-460 and 628-662; `packages/three-surface-poc-core/src/project-shape-extraction.test.ts`
  lines 778-786; `packages/three-surface-poc-core/src/project-shape-manifest.ts` lines 354,
  404, 419, 491.
- **Prerequisite.** Spec amendment (PWB-REQ-002's "a source never yields a partial item set"
  is the current, tested contract). **owner_value 4 / build_cost 3.**
- **Slices.** (1) Semantic delta for PWB-REQ-002 via the normative-change workflow. (2)
  `partially-extracted` outcome with per-class failure records. (3) `unenumerated-heading`
  failure reason with a tenth-category fixture. (4) Root-independence declared per tree rule.

### M16 — Renderer, diagram and visual-system engineering

- **What.** Re-run and re-date the mutation-kill sweep for the renderer (S8-M4); a branded
  `Html` type so escaping is enforced by the compiler (S8-M3); split the 1,615-line module along
  its section seams (S8-M5); model-derived inline SVG diagrams over a graph shape that can
  express fan-in, fan-out and hierarchy, with a real legend (S3-M1); an assistive-technology
  text equivalent for relations diagrams (S3-M3); a visible marking for non-normative nodes
  (S3-M4); feed the fence renderer literal fences instead of byte-offset-stitched ones (S3-M2);
  generalize figure and passage curation alongside generation (S1-M4); name a type scale and retire
  the eight stray hex literals in favour of tokens (S11-M3); resolve the forced dark theme by a light
  palette or one recorded sentence (S11-M4).
- **Why.** Verification rules 7 and 10: the only mutation evidence for the highest-traffic
  module is bound to bytes that no longer exist (S8-F4 [Observed]). SEC-1 and VIS-7 for the
  type. VIS-1 and VIS-3 for diagrams that can say what the architecture is.
- **Evidence.** `docs/evidence/pwb-p3-6-narrative-mutation-run-2026-09-04.json` versus the
  current digest; `apps/three-surface-poc/src/polaris.ts` lines 417-490 (raw helpers);
  `apps/three-surface-poc/src/polaris-markdown.ts` lines 108-127; capture: 0 svg elements.
- **Prerequisite.** None. **owner_value 4 / build_cost 3 to 5.**
- **Slices.** (1) Mutation re-run, dated record, old record untouched (about 35 minutes, no
  edits while it runs). (2) `Html` brand and the five helpers fixed. (3) Text equivalent and
  non-normative marking with a counterexample. (4) Module split. (5) SVG diagrams as a
  feature-request candidate. (6) Type-scale tokens and a grep check for stray literals; the theme
  decision recorded in `docs/POLARIS-READING-LAYOUT.md` or implemented.

## Pending beads, taken into account

The owner asked for pending beads to be considered. Of the 20 open beads at run start, the
Polaris-relevant ones and how the moves relate:

- syzygy-mea (P1, generalized Polaris generation and verification): M6, M7 and M8 are the
  pursuit's reading of what its acceptance criteria still lack in the landed code; they
  should be filed as children of, or dependents on, that epic rather than a competing one when
  the owner releases the gate.
- syzygy-1z3 and children 1z3.22, 1z3.25, 1z3.28, 1z3.29: the cold-open walkthrough (1z3.22)
  is the natural first exercise of M3 and M4; the seed-allowlist fix (1z3.29) is upstream of
  M15's root-independence slice; the cycle report (1z3.25) should carry P0-CEILING.
- syzygy-e3e (consent reference-unresolvable in coverage rendering): adjacent to M14, not
  merged into it.
- syzygy-u2a and children (runtime hardening, blocked on human gate u2a.1): M11's logging slice
  overlaps its scope; file M11 with a link, not a duplicate.
- syzygy-0wf, 2dn, 5fj, 8de, blu, kyt, s9q: not Polaris-facing; untouched.
- Closed during the run: syzygy-8t9 and syzygy-vrq (PRs #33 and #34); not proposed.
- Pending owner decision P-52 (no automated contrast or keyboard E2E, no single cross-surface
  parity sweep) is the standing home for the parts of M3 and M13 that need a ruling.

## Known ledger the run deduped against

Every agent read and applied this ledger; its full text is in the harvest file. In brief: the
generalized generator (now on main since PR #32) and every unchecked task in its `tasks.md`;
the seed-allowlist fix on branch agent/syzygy-1z3.29; PRs #28 to #31 (contract amendment,
navigable manifesto, diagrams, authoring kit); the P-63 trim and the 503 mechanism itself; the
Butlers-side repairs P-60, P-61, P-62 and the withheld active-content files; the bounded
non-release POC constraints; the literal-grammar strictness that makes v1.md whole-source
Unknown. Main moved twice during the run (63f0e50, 1932f74); neither move touched the renderer,
core pipeline or routes, so the captures remained valid.

## Reading the data file

```
jq '.agents[] | select(.label=="S4-catalogs-claim-states")' docs/pursuits/2026-09-13-vision-pursuit-data.json
jq '.agents[] | {label, tier}' docs/pursuits/2026-09-13-vision-pursuit-data.json
jq '.agents[] | .moves[] | select(.owner_value>=5 and .build_cost<=2) | {agent: input_filename, id, title}' docs/pursuits/2026-09-13-vision-pursuit-data.json
jq '.orchestrator.findings[]' docs/pursuits/2026-09-13-vision-pursuit-data.json
jq '.ranked_moves[] | {id, title, merges, prerequisite}' docs/pursuits/2026-09-13-vision-pursuit-data.json
```

## Gate

Filed 2026-09-13 as a gated epic in `bd`. Closing the gate bead is the owner's move; nothing
in this dossier authorizes execution.

| Bead | Role |
|---|---|
| `syzygy-oc2` | `[HOLD]` owner gate (task, P1, assigned to the owner). Every child below depends on it. |
| `syzygy-dov` | Epic (P1, assigned to the owner so it stays off `bd ready`). |
| `syzygy-dov.1` … `syzygy-dov.6` | M1 … M6 (P1) |
| `syzygy-dov.7` … `syzygy-dov.12` | M7 … M12 (P2) |
| `syzygy-dov.13` … `syzygy-dov.16` | M13 … M16 (P3) |

Child `n` is move `Mn`. `bd ready` at filing time showed only the gate and the epic; `bd blocked`
listed all sixteen children. Release: `bd close syzygy-oc2`.
