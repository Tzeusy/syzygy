# Vision pursuit — Polaris — 2026-09-22

Planning artifact only. Nothing here is authority, nothing here is a review verdict, and no
bead filed from it is runnable until the owner closes the gate bead named at the end. Claims
are labeled `[Observed]`, `[Inferred]` or `[Unknown]` as the agents labeled them, with the
critic's corrections applied where noted; every per-agent finding and move, with its full
evidence list, is in `docs/pursuits/2026-09-22-vision-pursuit-data.json` (access pattern
below). The raw harvest working file `docs/pursuits/2026-09-22-vision-pursuit-harvest.json`
sits beside it. Baseline: `docs/pursuits/2026-09-13-vision-pursuit.md`.

## Provenance

| Item | Value |
|---|---|
| Run | second Polaris pursuit; tier board carries movement against the 2026-09-13 baseline |
| Syzygy | audited at a4a3451 (clean main at capture); origin/main was already at 9d74185 (PR #52, five P-68…P-83 owner-gate packages; 46 files under docs/, scripts/ and .syzygy/, no POC source). Every "no code landed" claim survives the gap; every "nothing is drafted for gate X" claim does not, and is corrected below |
| Butlers | fresh private daemon rendered Butlers 65af1a0ea (as-of 2026-09-22T00:10Z); the owner's loopback daemon still served the evaluation of 2026-09-10 at Butlers 66ed58f |
| Captures | fresh `/polaris` 1,504,691 B (1,501,967 chars) against the 2,097,152 B ceiling; owner-daemon `/polaris` 2,090,025 B; `/api/poc` 5,600,304 B; Trajectory, Orrery and home captured but not tiered (see Gaps) |
| Fan-out | 16 surface audits (Sonnet), 1 lane A verification pass (Sonnet), 11 ideation lenses (Opus), 1 completeness critic (Opus): 29 agents in ten hourly batches of at most three, read-only against a private read-only daemon, deduped against the known ledger below; 0 agent errors |
| Owner brief | max 3 concurrent workers, staggered over twelve hours, Polaris focus, pending beads taken into account |

## North star (quoted)

From `.syzygy/governance/doctrine/vision.md`: "Showing the truth is the soul of the product."
The owner's own sentence: "open one place, understand what a project's vision and goals are,
tune or guide them if necessary, and know that the rest of the project will (eventually) mold
itself to fit around that goal." VIS-1 orders the values: truth and observation determinism,
then comprehension of the truth's presentation, then momentum, then breadth and fidelity, then
reproducibility of derived convenience; "comprehension is achieved by simplifying presentation,
never content." VIS-2: no evidence means Unknown, never success. VIS-3: every normative artifact
stays digestible by a human unfamiliar with the project. VIS-4: humans steer; agents draft,
never adopt; "Not autonomous. The loop is human-triggered." VIS-5: Syzygy writes no
implementation code. VIS-6: everything derived is rebuildable from the artifact that owns it.
VIS-7: every rendered link resolves and every encoding means what its legend says. Syzygy is
"not a documentation portal": the escape property is that intent changes produce dispatched
work, for two first-class consumers, the owner and agents. Product goal (2026-09-12):
generalizable LLM-assisted manifesto generation across projects; Butlers is a proving case.

## Tier board

Movement is against the 2026-09-13 tiers. `[Observed]` movement is confirmed by the lane A
verification pass (V1) or by the critic's independent check; `[Inferred]` movement is from
source reading alone. New-surface rows have no baseline and claim no movement. Two agent
movement claims were overturned by the critic and are shown as the orchestrator carries them
(details under Critic corrections). Full gap statements are in the data file under
`agents[].gap`.

| Surface | Agent | 09-13 | 09-22 | Movement | One-line gap |
|---|---|---|---|---|---|
| Lane A verification (2ef68f5, syzygy-dov.1) and P0-CEILING | V1 | n/a (verification pass) | functional | P0-CEILING resolved; up [Observed] | Lane A shipped exactly its authorized scope; P0-CEILING resolved (1,504,691 B against 2,097,152); per-item cost flat, so the 1.4 MB working-target shortfall grew 78,637 -> 104,691 B on Butlers population alone |
| First reading (opening through architecture) | S1 | solid | solid | up (within tier) [Observed] | Narrative script gone from the scroll path; tuple jargon still unglossed at word 249 with the legend at word 445, 29 of 52 disclosures bare-named, apparatus every ~210 words |
| Navigation shell and accessibility | S2 | functional | functional | none [Observed] | Legend renders after 718 identical tuples; the a11y checker sees 144 of ~1,471 focusables and has no duplicate-name check (390 'Exact text', 283 'Source record') |
| Architecture account and diagrams | S3 | solid | solid | none [Observed] | V1_READING_PLAN drifted silently to its fallback; four figure summaries share one name; fan-out relations flattened |
| Catalogs and claim states | S4 | functional | functional | none [Observed] | 729 tuple spans spend 425,354 chars (28.3%) to show 44 characters each, 718 identical; glossary names 15 states, 5 occur; the gaps band says 12 and lists 11 |
| Source provenance and exact-source route | S5 | functional | functional | none [Observed] | Requirement-scoped verbatim grain reaches 194 of 194 baseline sources; 390 'Exact text' links share one name and there is no inline preview; nothing changed since the baseline |
| Machine endpoints and human-machine parity | S6 | weak | weak | none [Observed] | Three provenance shapes on one channel; ~0 of workItems/codeStructure rendered for humans; narrative endpoint hardcodes citable:false beside 934 of 934 resolved anchors |
| PWB pipeline core | S7 | solid | solid | none [Observed] | Grammar-failure reason is computed then discarded; the rule-6 mutation evidence is stale; localeCompare ordering |
| Renderer modules (engineering) | S8 | functional | functional | none [Observed] | Per-claim attribute cost fell slightly (1,159 -> 1,154 chars) while the machine-metadata fraction rose to 55.9% because lane A shrank the denominator; the four-attribute framing quad alone is 300,210 B, larger than lane B's whole package |
| Generation kit and authoring path | S9 | weak | weak | none [Inferred] | Onramp commands succeed from the working checkout; run-contract fields absent from the types; example.json fails the landed validator |
| Daemon operability | S10 | weak | weak | none [Observed] | Zero request logging including the cause of a 500; build commit is not a status fact; tsc -b --force on every start (5.5 s); no timeouts or supervision |
| Visual language | S11 | weak | weak | none [Observed] | Focus ring is the amber semantic token; declared spacing scale used 0 of 173 times; 33-38 distinct font sizes depending on denominator; no print or forced-colors treatment |
| Portability lens (second project) | L1 | weak | weak | none [Observed] | A perfect M8 profile still fails on Syzygy's own doctrine shapes; authority set is a singleton; 52 of 95 proper-noun uses sit in repair routes no census counted |
| Owner core-loop lens | L2 | weak | weak | none [Observed] | The only action on any surface is a materialize button for a write P-71 Q5 foreclosed, and the page says the opposite; the one real dispatch is invisible; 26 pending rows on no surface |
| Generation-loop lens | L3 | weak | weak | none [Observed] | No front door (REQ-030/031 adopted, unbuilt); intermediate weaker than the kit's claim ledger; no evaluation runner; the prompt hash detects change, not regression |
| Evidence-currency lens | L4 | weak | weak | none [Observed] | 98 of 271 sources changed and 12 added while 729 of 729 claims say fresh; two staleness limbs (observed project vs observatory, 107 Syzygy commits) and the page names neither; Syzygy's own ~120 evidence records have no currency rule |
| Agent-consumer lens | L5 | weak | weak | none [Observed] | A work item is a dead end: no governing-intent edge, prohibitions untyped, return path closed at one member, 141 blocked rows with no blocker named |
| Cross-surface and three-state lens | L6 | weak | weak | none [Observed] | 0 of 1,460 cross-surface claim links; the join key renders as inert prose; Trajectory reads nine Beads columns, none naming an intent; two of four pages carry no evaluation identity |
| Owner decision path (gates, packets, register) | S12 | new-surface | weak | new-surface | 0 of 13 waiting gates appear on any surface; five gate packages (dov.18, .21, .22, .28, .30) are drafted, reviewed and merged in PR #52 and nothing says so; the register has no P-67..P-83 rows |
| Test rigor and evidence records | S13 | new-surface | functional | new-surface | 1,258 tests clean, but mutation tooling never ran in CI, the generation package has zero mutation evidence, ~120 evidence records have no staleness sweep, and 1z3.28's flake is uncharacterized |
| polaris-generation-core (engineering) | S14 | new-surface | functional | new-surface | 85/85 tests and a demo that runs; a bare catch at pipeline.ts:249-252 drops the failure code; zero mutation evidence; not adoptable from outside the repo |
| Owner walkthrough readiness | S15 | new-surface | weak | new-surface | 390 links and 283 toggles share names; the deep-dive capability shown is transport plumbing; the walkthrough has never been run (no run record) |
| Authority and consent boundary (credentials, state dir) | S16 | new-surface | weak | new-surface | State directory live at mode 755 not 700; ensureCredential trusts whatever exists; no rotation |
| Backlog-coherence lens | L7 | new-surface | functional | new-surface | WIP-one PocModel rule is one edge where three are needed (bd ready offers .2.1, .5.1, .8.1 together, confirmed by C1); 22 of 105 findings sit in no bead [unverified]; syzygy-mea has zero children |
| Boundary-probe lens (typed vs prose) | L8 | new-surface | weak | new-surface | One boundary is typed (30 refusals over 31 fixtures), the rest are prose; the write-guard exists and the materialize path does not use it; 27 governance check families check documents, not behaviour |
| Time-to-comprehension lens | L9 | new-surface | functional | new-surface | No reach-cost instrument; all nine cold-open answers arrive by body word 3,206 and the page says so nowhere; 1.23x source length with zero synthesis and zero Inferred; the repeated tuple is ~53% of the 9,403 flow-visible words (C1 correction of 28.2%) |
| Capability-composition lens | L10 | new-surface | weak | new-surface | Genome computes nothing; the generator accepts 0 of 283 source identities [unverified]; the only re-evaluation trigger is the materialize button; external_ref is written and never read; the same-revision path join (206/206) is unused |
| Growth, cadence and cost lens | L11 | new-surface | weak | new-surface | One re-evaluation costs 2.21 s and no verb spends it; maxParsePassesPerSource is at 14 of 16 and the roadmap spends the rest; 13.9% of the machine body is eight repeated constants; ceilings arrive ~2027-04 (page) and ~2027-07 (machine) [Inferred]; the page renders Butlers' cost discipline 45 times and Syzygy's own cost zero times |

Net: seventeen baseline rows, one moved within tier (S1), sixteen unchanged; eleven new rows
(three functional, eight weak); the orchestrator's P0-CEILING finding is resolved. The system is
more honest than nine days ago about what it does not know (lane A landed exactly its
authorized scope), and no better at telling the owner what it costs, what changed, or what to
decide.

## Systemic themes

Eight patterns recur across agents that did not read each other. Exemplar finding ids are in the data file under `themes[].exemplars`.

1. **The ceiling is beaten; the exponent is not.** P0-CEILING is resolved [Observed]: 1,504,691 B against 2,097,152 (V1-F1). But lane A removed a fixed cost, not a per-item cost, so growth reverted to tracking Butlers: the 1.4 MB working-target shortfall grew 78,637 -> 104,691 B in nine days on population alone (V1-F3), per-item cost is flat at ~1,473 B (V1-F2), and nine days of machine growth landed in projectShape as existing rows got fatter, not as new rows (L11-F3 [Inferred]). Straight-line arrival is ~2027-04 for the page and ~2027-07 for the machine body [Inferred] (L11-F6); P-80 Q1's 'complete population always served' forecloses paging, so the honest levers are per-item bytes: 729 tuple spans at 425,354 chars (S4-F1), the four-attribute framing quad at 300,210 B (S8-F1, direction corrected by C1-F2), and on the machine side two per-row fields that restate their own block header, 740,796 B or 13.2% of the body (L11-F4).

2. **Computed, then thrown away at the boundary.** The system already knows most of what the surfaces fail to say. The resource ledger computes bodies, bytes, 725 parse passes and a worst source at 14 of 16 and no renderer reads it (L11-F2, L11-F5); the grammar-failure reason is computed and discarded (S7-F1); external_ref is written on every materialization and never read back (L10-F4, L2-F2); the same-revision path join is exact for 206 of 206 anchors and unused (L10-F5); 934 of 934 narrative anchors resolve while the endpoint hardcodes citable:false (S6-F4); the reading plan's drift to its fallback is silent (S3-F1); a 500's cause is logged nowhere (S10-F1). By VIS-6 all of it is derived and free to render; by VIS-2 each absence is an Unknown rendered as nothing.

3. **Currency has no verb and no second limb.** A full re-evaluation costs 2.21 s and 145 MB and there is no way to ask for it: the only rebuild seam fires after a write into Butlers, which is why the owner's daemon served a twelve-day-old evaluation (L11-F1). M2 (ruled, dov.2.x) makes the page confess it is old; nothing makes it new. Staleness has two limbs the page names as one: the observed project moved (98 of 271 sources changed, 12 added) and the observatory itself moved 107 Syzygy commits (L4-F1, L4-F2, S10-F2). The fastest-growing block is read from a shared Dolt server on a clock the git revision does not pin, and its population is not monotonic (L11-F7), so 'what changed' cannot be a suffix. Syzygy's own ~120 evidence records have no currency rule at all (L4-F4, S13-F3).

4. **The owner's decisions have no surface, and the one action offered is foreclosed.** Thirteen gates wait and 0 of 13 appear anywhere (S12-F1); five of them (dov.18, .21, .22, .28, .30) were drafted, independently reviewed and merged in PR #52 eleven minutes before this run's capture, and no surface says so (S12-F2, confirmed by C1). The decision register has no rows for P-67..P-83 (S12-F3) and ~308k words of packets stand between the owner and a ruling. Meanwhile the product's only button offers the write P-71 Q5 foreclosed, and the panel says it is available (L2-F1); the write-guard that would refuse it exists and the materialize path does not call it (L8-F2). No owner sitting shortens the critical path today (L7-F3), because the ready slices are gated by pick order, not by rulings.

5. **Repetition is the reading cost, not only the byte cost.** The prior run counted the tuple in bytes; this run counts it in words. 718 identical tuples are ~5,026 visible words, about 53% of the 9,403 words readable in flow (C1-F2 correcting L9-F4). The tuple's jargon appears at word 249 and its legend at word 445 (S1-F1), after 718 uses (S2-F1); epistemic apparatus interrupts every ~210 words (S1-F3); 390 links and 283 toggles share two names (S15-F1, S2-F2); the source catalog is a 194-item flat list (S11-F5). All nine cold-open answers arrive by body word 3,206 and the page never says a reader may stop (L9-F1); the page is 1.23x its sources' length with zero synthesis and zero Inferred claims (L9-F3).

6. **Generality is asserted, not measured.** The product goal is generalizable manifesto generation and every measurement of it is on one repository. A profile that passes M8's census perfectly still fails Syzygy's own principle, success-criterion and craft-policy shapes (L1-F1); the authority set is a singleton (L1-F5); the generator has no front door (REQ-030/031 adopted, unbuilt) and no evaluation runner (L3-F1, L3-F3), accepts 0 of 283 observed source identities [unverified] (L10-F2), and its example fails its own validator (S9-F2). syzygy-mea, the epic that carries the goal, has zero children and two acceptance criteria that cannot be built without a second project (L7-F5).

7. **Boundaries are prose where they should be types or edges.** One boundary is typed with 30 refusals over 31 fixtures; the rest live in documents (L8-F1); 27 governance check families check documents, not behaviour (L8-F4). Prohibitions reach agents untyped (L5-F2); no observed column names a governing intent, so no intent-to-work edge exists and the join key renders as inert prose (L5-F1, L6-F3); 0 of 1,460 hrefs cross surfaces at claim level (L6-F1). The WIP-one rule for PocModel is one edge where three are needed and the collision is live in bd ready (L7-F1). The credential store trusts whatever it finds at mode 755 (S16-F1, S16-F2).

8. **Evidence discipline is a habit, not a mechanism.** Mutation tooling has never run in CI (S13-F1); polaris-generation-core has zero mutation evidence (S13-F2, S14-F2) and the rule-6 record is stale (S7-F2); ~120 evidence records have no staleness sweep (S13-F3); the reading plan drifted unnoticed (S3-F1); the owner walkthrough has no run record (S15 gap); the 1z3.28 flake is uncharacterized (S13-F4). Three agents independently proposed the same sha256 drift instrument against three populations (C1-F1 f). The run's own numbers show the same habit: five agents quoted a character count as bytes (C1-F2).

## Ranked moves

Ranking rule: owner_value first (VIS-1 order: truth, then comprehension, then momentum), then
the inverse of build_cost, then prerequisite class (none before spec amendment before doctrine
amendment), then how many independent agents converged on the move. Ids are N1…N15 so they
cannot be confused with the prior run's M1…M16, all sixteen of which are ruled and being
applied. Nothing here re-proposes a ruled move; where a move continues one (N5 continues the
S4-M1 remainder of M1, N9 rides M6's machine-view delta) it says so and files under that epic.
Every move was checked against the known ledger and the 74 open or in-progress rows under
`syzygy-dov`; increments that belong inside an existing slice are listed under Increments and
travel in N1, not as moves.

### N1 — Backlog coherence in one sitting: WIP-one as edges, ready slices re-sequenced, cross-epic edges, and this run's increments folded into the slices that already own them

- **What.** No code. (a) Encode the P-74 Q7 WIP-one rule for PocModel as edges: syzygy-dov.2.1 -> .8.1 and .5.1 -> .8.1, and label the four PocModel-touching slices shared-model, so bd ready cannot offer two of them at once (today it offers .2.1, .5.1 and .8.1 together; C1 confirmed). (b) Record the run order for the eighteen ready implementation slices on syzygy-dov so the first four change what the owner reads: .2.1, .11.1, .14.1, .13.1. (c) Cross-epic edges: 1z3.22 (cold-open walkthrough) behind .2.1/.3.1/.11.1/.13.1; syzygy-mea <-> dov.6.x/.7.1; .10.1 <-> u2a.6/e3e. (d) Fold this run's increments into the existing slices that own them, per C1-F1: distinct accessible names for the 390 'Exact text' links, 283 'Source record' toggles and four figure summaries into dov.13.1 ('interpolated labels in the copy oracle'); 'gate example.json against the landed validator' into dov.6.2; observerRevision in banner and status, a per-request log line with the 500 cause, dropping tsc --force and timeouts into dov.11.x; the thirteen repair-route template literals into dov.8.5's census denominator; the M2 slice-2 act-row wording (L4-M2) reconciled. (e) Write the 105-finding disposition record (which prior-run finding lives in which bead) beside the prior data file.
- **Why.** L7-F3: no owner sitting shortens the critical path today; the order slices are picked up in does. L7-F1: two parallel workers can take two PocModel slices this afternoon. C1-F1: four agents re-proposed one clause of dov.13.1 without naming it, which is what happens when increments are filed beside their owners instead of inside them. VIS-4 (agents draft, the graph is the owner's), VIS-3 (the plan stays digestible).
- **Evidence.** L7-F1, L7-F3, L7-F4, L7-F5, L7-F2, L4-F3, C1-F1. Merges agent moves L7-M1, L7-M4, L7-M5, L7-M2, L4-M2, S1-M2, S3-M2, S5-M1, S15-M1, S9-M1, S10-M1, S10-M2, S10-M3, S10-M4, L1-M5.
- **Prerequisite.** none. Doctrine: VIS-4, VIS-3. Theme 7.
- **Relates to.** `syzygy-dov`, `syzygy-dov.8.1`, `syzygy-dov.2.1`, `syzygy-dov.5.1`, `syzygy-dov.13.1`, `syzygy-dov.6.2`, `syzygy-dov.11.1`, `syzygy-dov.8.5`, `syzygy-1z3.22`, `syzygy-mea`, `syzygy-e3e`, `syzygy-u2a.6`.
- **owner_value 5 / build_cost 1.**
- **Slices.**
  1. File the two blocking edges and the shared-model labels; re-run bd ready and record that only one PocModel slice is offered.
  2. Write the run order and the cross-epic edges; record them on syzygy-dov and the affected slices.
  3. Append the fold-ins to dov.13.1, dov.6.2, dov.11.x and dov.8.5 descriptions, each citing this run's finding id.
  4. Write docs/pursuits/2026-09-13-vision-pursuit-coverage.json: 105 prior findings -> bead or 'no bead, reason'.

### N2 — A re-observe verb: human-triggered re-evaluation that mints a new evaluation identity and names which of the three clocks moved

- **What.** Extract buildModel() into a named re-evaluation with an explicit result (new evaluation identity, the three clock readings: Butlers git HEAD, working-tree digest, Dolt revision; the identity it supersedes). Add a human-open POST route through browserRequestAllowed and a --watch CLI mode that re-observes on the owner's Enter. No timer, no poller, no filesystem watcher: every trigger is a human act or a human-installed post-commit hook in the owner's own Butlers checkout that curls the loopback route. The status line and the response name the two staleness limbs separately: observed project moved (sources changed/added) vs observatory moved (Syzygy commits since build), plus the Dolt clock.
- **Why.** L11-F1 [Observed]: one re-evaluation is 2.21 s and 145 MB; the only rebuild seam (main.ts:200-201) fires after a write into Butlers, so the owner's daemon served a twelve-day-old evaluation. M2 discloses age; this removes it. L4-F1/F2: two limbs age independently (98 of 271 sources vs 107 Syzygy commits) and the page names one. VIS-1 (truth and observation determinism first), VIS-4 (human-triggered loop; P-69 forbids timers, which this honours), VIS-2 (a new identity, never a rewritten one; respects dov.2.1's asOf immutability).
- **Evidence.** L11-F1, L11-F7, L4-F1, L4-F2, L10-F3, S10-F2. Merges agent moves L11-M1, L10-M5, L4-M1.
- **Prerequisite.** none. Doctrine: VIS-1, VIS-4, VIS-2. Theme 3.
- **Relates to.** `syzygy-dov.2.1`, `syzygy-dov.11.1`, `syzygy-dov.28`, `syzygy-dov.19`.
- **owner_value 5 / build_cost 2.**
- **Slices.**
  1. Core: named re-evaluation function returning identity + clocks + superseded identity; test drives it twice, asserts two identities and an unchanged first.
  2. Route: POST /re-observe under browserRequestAllowed; new parity family with a declared empty machine denominator (P-77 Q6).
  3. CLI: --watch re-observes on Enter and prints clock deltas; docs + sample post-commit hook (a curl, installed by the owner).
  4. Status line: the two limbs and the Dolt clock beside M11's breach line; retention of superseded evaluations waits for dov.28 and says so.

### N3 — The resource ledger on the surface: headroom against all seven declared limits, a cost block, and a build-time guard on the pass budget at 14 of 16

- **What.** Extend ResourceLedgerSummary with per-limit headroom (declared, observed, remaining) and a derived cost record (bodies read, bytes, parse passes, worst-source passes, evaluation wall time, peak memory, the arrival date implied by the observed rate, and the generation half: stage prompt bytes and the corpus denominator a provider would be sent). One line on the human surfaces in M11's status slot; one block on the machine body as its own parity family. A test recomputes the worst-source pass count over the Butlers corpus and fails when a new registry pass identity would take a source past a declared margin, naming the source and the passes charged to it. Every retained page-size evidence record gains a population block (item count, claim-id count, Butlers revision) so growth is attributable without reconstruction.
- **Why.** L11-F2 [Observed]: maxParsePassesPerSource is at 14 of 16 on one source, the most-consumed limit in the system, the only one Syzygy's own roadmap spends (M2, M14, M15 and lane B each plausibly add a pass), and it is published nowhere. L11-F5: 0 occurrences of the ledger's vocabulary in 1,501,967 characters of page while Butlers' cost discipline renders 45 times. VIS-6 (purely derived, nothing new to own), VIS-2 (the owner's 'what does this cost me' is an Unknown rendered as nothing). V1-F2/F4: this pass had to reconstruct population attribution by hand and found the tailnet capture byte-identical to the direct one.
- **Evidence.** L11-F2, L11-F5, L11-F6, V1-F2, V1-F4. Merges agent moves L11-M2, L11-M4, V1-M1.
- **Prerequisite.** none. Doctrine: VIS-2, VIS-6, VIS-1. Theme 2.
- **Relates to.** `syzygy-dov.11.1`, `syzygy-dov.10.1`, `syzygy-dov.8.1`, `syzygy-dov.2.2`, `syzygy-dov.14.1`, `syzygy-dov.15.1`, `syzygy-dov.17`, `syzygy-dov.27`.
- **owner_value 4 / build_cost 2.**
- **Slices.**
  1. Core: headroom + cost record in resource-ledger.ts summary(); pure, no new observation or limit.
  2. Guard test on maxPassesOnOneSource with a declared margin; failure message names source and pass identities.
  3. Human line beside M11's breach line under its byte budget; machine block as a parity family (queues behind .8.1 then .10.1 under WIP-one; joins dov.10.1's digest exclusion decision).
  4. Population block in the M1 measurement script and evidence shape; re-measure and record beside the lane A record.

### N4 — Cost-1 page honesty fixes: legend before the first claim, jargon glossed at first appearance, a proof strip of counts, the gaps tally corrected, evaluation identity on Trajectory and Orrery, a distinct focus token

- **What.** Render legendHtml() at the top of <main> in the reading layout so the tuple's definition precedes its first of 729 uses; gloss the tuple vocabulary in one sentence at polaris.ts:1592-1601 where it first appears; add a proof strip of counts (sources, items, facts, Unknown) between Purpose and the first diagram; make gapsList's count equal the findable population and render 'By cause' as a list of eight; print the composite evaluation identity and as-of instant in the Trajectory and Orrery footers, naming what each substrate revision is a revision of; give --focus its own token distinct from --amber; resolve the 66ch/74ch measure contradiction; rewrite the nav copy as reader questions.
- **Why.** Every item is one edit and each closes a counted honesty or comprehension defect: 718 identical tuples precede the legend (S2-F1); jargon at word 249, legend at word 445 (S1-F1); '12 claim(s)' where 11 are findable, in the one band whose purpose is honesty (S4-F4); two of four pages carry no evaluation identity so a reader cannot tell they were computed together (L6-F4, RFC6-15); the focus ring is the semantic amber (S11-F2). VIS-1 comprehension, VIS-2 counts that are true, VIS-7 encodings that mean what the legend says.
- **Evidence.** S2-F1, S1-F1, S1-F2, S4-F4, S4-F5, L6-F4, S11-F2, S11-F4. Merges agent moves S2-M1, S1-M1, S1-M3, S4-M4, L6-M2, S11-M1, S11-M4, S2-M5.
- **Prerequisite.** none. Doctrine: VIS-1, VIS-2, VIS-7. Theme 5.
- **Relates to.** `syzygy-dov.13.1`, `syzygy-dov.3.1`.
- **owner_value 4 / build_cost 1.**
- **Slices.**
  1. page-shell.ts: legend into <main> when readingLayout; decide whether the footer copy stays.
  2. polaris.ts: first-appearance gloss, proof strip, gapsList count + list markup.
  3. trajectory.ts / orrery.ts: evaluation identity + as-of + substrate naming in footers; render skew when a surface answers at a different evaluation.
  4. design-tokens.ts: --focus token; measure fix; nav copy.

### N5 — State the epistemic tuple once per class and the framing quad once per region: the visible-text and framing-attribute families lane B does not touch

- **What.** Visible text: state the shared tuple once per class with its population count and denominator, render the per-claim tuple only where a field differs, and keep every claim's data-epistemic-* attributes so the complete population is still served (P-80 Q1). Add the one-sentence class summary and derive the glossary's counts from the population so it names 5 states that occur, not 15. Attributes: collapse the four-attribute framing quad (data-copy-role, claim-role, presentation-artifact, non-citable) to one token on the region ancestor with a documented inheritance rule, and add the three missing renderer tests. Re-measure on a committed clean tree and record beside the lane A record. This is the unshipped remainder of prior M1's S4-M1 merge, re-justified on the reading axis; file it as a lane-C slice under dov.1 beside lane B (dov.17), never as a competitor.
- **Why.** C1-F2 corrected L9-F4 upward: 718 identical tuples are ~5,026 words, ~53% of the 9,403 flow-visible words, not 28.2%; the byte share (425,354 chars, 28.3%) stands as S4-F1 measured it. S8-F1: the framing quad is 300,210 B (19.95%), larger than lane B's whole epistemic family. Together they are roughly 3.8x lane B's expected saving and, unlike lane A, per-item. VIS-1 (simplify presentation, never content), VIS-2 (an exceptional state that is noticeable is more honest than one buried in 718 identical siblings).
- **Evidence.** S4-F1, L9-F4, S8-F1, S4-F2, S4-F3, C1-F2. Merges agent moves S4-M1, L9-M3, S8-M1, S4-M2, S4-M3, L9-M5, S8-M2.
- **Prerequisite.** none. Doctrine: VIS-1, VIS-2. Theme 1.
- **Relates to.** `syzygy-dov.1`, `syzygy-dov.17`, `syzygy-dov.27`.
- **owner_value 4 / build_cost 2.**
- **Slices.**
  1. polaris.ts itemEntry/itemRow/classBlock: once-per-class tuple with count/denominator; exception-only per-claim rendering; test asserts attribute multiset unchanged.
  2. Glossary counts derived from population; class summary sentence.
  3. page-shell.ts/polaris.ts: framing quad -> one region token; inheritance rule documented; parity sweep denominators declared (P-77 Q6); three renderer tests.
  4. Measurement record with population block (N3) beside pwb-m1-polaris-lane-a-measurement.

### N6 — Refuse the foreclosed write and type the effect boundary: dispatchAuthorization, effectAuthority(registryEntry, effect) fail-closed, a generated boundary register, and a credential store that verifies before it trusts

- **What.** A pure dispatchAuthorization()/effectAuthority(registryEntry, effect) in three-surface-poc-core that returns authorized or foreclosed with the citation (P-71 Q5 for the Butlers write), fail-closed for any effect the registry entry does not name; route the materialize path through it and through the existing write-guard it currently bypasses; render the foreclosed state with its citation and disable or replace the button. Generate a boundary register (sibling of build_directive_register.py) listing every effect the code can perform and the clause that authorizes it, so a prose NOT-boundary with no typed refusal is a lint failure. In credentials.ts verify the state directory's mode and owner before trusting an existing credential, and log modes at startup.
- **Why.** L2-F1 [Observed]: the product's only action offers a write the owner foreclosed on 2026-09-21 and the panel says it is available; a page whose thesis is 'showing the truth' cannot present a foreclosed act as an offer. L8-F1/F2: one boundary of many is typed; the guard exists and the mutating path does not call it. S16-F1/F2: mode 755 live, trust-on-find. VIS-2, VIS-4 (agents draft, never adopt), VIS-5 (the write universe is closed), SEC-1/SEC-3.
- **Evidence.** L2-F1, L8-F1, L8-F2, L8-F3, S16-F1, S16-F2. Merges agent moves L2-M1, L8-M1, L8-M2, S16-M1, S16-M2.
- **Prerequisite.** none. Doctrine: VIS-2, VIS-4, VIS-5, SEC-1, SEC-3. Theme 4.
- **Relates to.** `syzygy-dov.4.1`, `syzygy-u2a`, `syzygy-u2a.2`.
- **owner_value 5 / build_cost 2.**
- **Slices.**
  1. Core: effectAuthority + fixtures for every named effect (authorized/foreclosed/unknown -> refused).
  2. materialize-action.ts: call the guard; render foreclosed state with citation; button disabled.
  3. scripts/build_boundary_register.py + governance check that every NOT-boundary maps to a typed refusal or is listed as prose-only.
  4. credentials.ts: verify mode/uid before trust; startup log of modes; test with a 755 fixture.

### N7 — The owner's decision path on a surface: the five merged gates as one sitting, the P-67..P-83 register rows, the last-ruling closure band, and (later, under amendment) an owner in-box panel

- **What.** Collect the five gates whose packages are drafted, reviewed and merged (PR #52: dov.18, .21, .22, .28, .30) into one plain-English screen with each gate's sign-off phrase, consequence and dov.21's two precondition questions inline, so the owner can clear them in one sitting under their own batch-decision directive. Add the P-67..P-83 rows to the decision register (doc-only). Render a closure band on the page: the last ruling and what it closed (P-67 -> lane A landed), which discharges or supersedes 1z3.25's 'report the completed cycle'. Slice 4, an owner in-box panel listing every waiting gate on a surface, is vision-extending and waits for its doctrine amendment.
- **Why.** S12-F1/F2 [Observed]: 0 of 13 waiting gates appear on any surface; five are ready today and nothing says so; only S12 and the critic noticed PR #52 landed. S12-F3: the register the owner consults has no rows for the last seventeen rulings. VIS-4 (the owner adopts; the system's job is to make adopting possible), VIS-3 (~308k words of packets is not digestible), VIS-2 (a page that shows truth about a project should show the truth about its own pending decisions).
- **Evidence.** S12-F1, S12-F2, S12-F3, S12-F4, L7-F3, C1-F5. Merges agent moves S12-M2, S12-M3, S12-M4, S12-M1.
- **Prerequisite.** none for slices 1-3; doctrine amendment for slice 4. Doctrine: VIS-4, VIS-3, VIS-2. Theme 4.
- **Relates to.** `syzygy-dov.18`, `syzygy-dov.21`, `syzygy-dov.22`, `syzygy-dov.28`, `syzygy-dov.30`, `syzygy-1z3.25`.
- **owner_value 5 / build_cost 2.**
- **Slices.**
  1. Doc: one-sitting screen for the five gates (sign-off phrases, consequences, dov.21 preconditions) under docs/decisions or PENDING-OWNER-DECISIONS.md.
  2. Doc: register rows P-67..P-83.
  3. Page: closure band 'last ruling and what it closed'; decide with the owner whether it discharges syzygy-1z3.25.
  4. Vision-extending: owner in-box panel; enters the feature-request funnel with its doctrine amendment drafted first.

### N8 — Measure generality: a shape-coverage matrix over synthetic second-project corpora, a typed admitted-input seam, container-shape vocabulary in the profile, and an authority set keyed by observed project

- **What.** Author two or three synthetic corpora as test fixtures in container shapes Butlers does not use (principle lists, success-criterion tables, craft-policy prose), run the extraction pipeline against each and print a per-class coverage matrix as a retained evidence record; zero egress, zero new consent, no second repository. Give the profile a container-shape vocabulary (rides M15's delta) so a shape is a profile row, not a code path. Introduce a typed admitted-input boundary module (packages/polaris-generation-core/src/admitted-input.ts) and a SourcePopulation port so discovery is a produced denominator rather than a hardcoded one. Key the authority set by observed project. Check first whether syzygy-u2a.7's repository discoverability already supplies the locator.
- **Why.** L1-F1 [Observed]: a profile that passes M8's census still fails on Syzygy's own doctrine shapes, so the census measures the wrong thing. L7-F5: syzygy-mea's AC4/AC6 cannot be built or scored without a second project, and the second real project is gated (dov.25 plus a consent record); this buys most of the number as ordinary fixtures. L3-F1: no front door means no denominator. VIS-1 breadth and fidelity, VIS-5 (no new write, no egress), VIS-3.
- **Evidence.** L1-F1, L1-F2, L1-F3, L1-F5, L3-F1, L7-F5, L10-F2. Merges agent moves L1-M3, L1-M1, L1-M2, L1-M4, L3-M1.
- **Prerequisite.** none. Doctrine: VIS-1, VIS-5, VIS-3. Theme 6.
- **Relates to.** `syzygy-mea`, `syzygy-dov.8`, `syzygy-dov.15`, `syzygy-dov.25`, `syzygy-u2a.7`.
- **owner_value 5 / build_cost 3.**
- **Slices.**
  1. Fixtures: three synthetic corpora in non-Butlers shapes; extraction run; coverage matrix as docs/evidence record.
  2. Profile: container-shape rows; profile-driven repair routes (L1-M5's denominator fix travels in N1).
  3. admitted-input.ts + SourcePopulation port; generator front door consumes it (relates syzygy-mea, REQ-030/031).
  4. Authority set keyed by observed project; reconcile with u2a.7 before building a locator.

### N9 — An honest machine channel: one provenance shape, citable computed from the anchors, and the two per-row fields that restate their block header deleted (740,796 B)

- **What.** Collapse the three provenance shapes on the machine channel to one; compute citable from the 934 resolved anchors instead of hardcoding false, and link each narrative block to its anchors by id; assert in a test what fraction of workItems and codeStructure the human page renders so the gap is a number, not a surprise. Stop emitting doltRevision on each of 7,527 work items and revision on each of 6,749 files (both byte-identical to their block header) and land the rule that a row may not repeat a value its block declares. The machine contract is not waived by this run's redesign licence, so this travels as a machine-view delta (dov.22's family) and must land before dov.10.1 publishes the response-identity digest over the canonical body.
- **Why.** L11-F4 [Observed]: 13.2% of the machine body is two derivable fields, 3.9x lane B's expected saving on the channel lane B does not touch, scaling with row count; 78 days of machine-ceiling runway at the observed rate. S6-F4/S4-F6: citable:false on 730 of 730 blocks beside 934 of 934 resolved anchors is a false statement on the honesty channel. VIS-2, VIS-6 (rebuildable from the artifact that owns it, here the block header), VIS-7.
- **Evidence.** S6-F1, S6-F2, S6-F4, S6-F5, L11-F4, S4-F6. Merges agent moves S6-M1, S6-M2, S6-M3, L11-M3.
- **Prerequisite.** spec amendment. Doctrine: VIS-2, VIS-6, VIS-7. Theme 2.
- **Relates to.** `syzygy-dov.10.1`, `syzygy-dov.10.3`, `syzygy-dov.22`, `syzygy-dov.8.1`, `syzygy-dov.5`.
- **owner_value 4 / build_cost 2.**
- **Slices.**
  1. Spec: machine-view delta naming the single provenance shape, the citable rule and the no-row-restates-block rule (CC-REV-2, dov.22 family).
  2. Core: drop the two per-row fields; test asserts recoverability from the block header; parity denominators declared empty (P-77 Q6).
  3. Narrative endpoint: citable from anchors; block -> anchor ids; unrendered-fraction assertion.
  4. Re-measure the machine body and record the delta beside the lane A record; sequence before dov.10.1's digest under WIP-one.

### N10 — Governing intent as an observed edge: read description and design text back, extract intent identifiers by the literal grammar, and render governedBy or Unknown on every work item

- **What.** Widen the work-item SQL projection (work-items.ts:86-88, nine expressions today; C1 corrected L6-F3's seven) to read external_ref, description and design text; extract governing-intent identifiers by the literal grammar only; add a governedBy edge to WorkItemFact, rendering Unknown with a counted denominator when no identifier is present. Re-derive the one real dispatch from external_ref so it is visible again. Add the source->claims direction (claimsBySourceAnchor) so an intent change shows its blast radius. Name which of the three clocks a re-derivation reflects (N2).
- **Why.** L5-F1/L6-F3 [Observed]: no observed column names an intent, so the escape property (intent change -> dispatched work) has no observable edge and 141 blocked rows name no blocker. L10-F4: external_ref is written on every materialization and never read back. VIS-1 (observation before inference), VIS-2 (Unknown with a denominator, never silence), VIS-6 (derived from the artifact that owns it).
- **Evidence.** L5-F1, L6-F3, L2-F2, L10-F4, L5-F5, C1-F4. Merges agent moves L6-M3, L2-M2, L10-M3, L5-M1, L2-M3.
- **Prerequisite.** spec amendment. Doctrine: VIS-1, VIS-2, VIS-6. Theme 7.
- **Relates to.** `syzygy-dov.7.1`, `syzygy-dov.12`, `syzygy-dov.20`, `syzygy-u2a.6`.
- **owner_value 4 / build_cost 3.**
- **Slices.**
  1. Spec: CC-REV-2 delta admitting description/design/external_ref to the work-item observation and defining the governedBy edge and its Unknown.
  2. Core: projection + literal-grammar extraction + WorkItemFact.governedBy; fixture over the 7,527-row capture.
  3. Trajectory: render governedBy / Unknown(n of N); re-derive the dispatch from external_ref.
  4. claimsBySourceAnchor and the intent-delta blast radius on Polaris.

### N11 — One drift-sweep instrument and a scheduled mutation gate: sha256 drift over reading plans, evidence records and mutation records; mutation markers for polaris-generation-core; failure codes carried, not swallowed

- **What.** Build the sha256 drift sweep once (scripts/check_evidence_currency.py) and point it at three populations: V1_READING_PLAN's anchors via /polaris/source, the ~120 docs/evidence/*.json subject digests with a uniform baseline key, and the retained mutation records; land the written rule (AGENTS rule 11) that an evidence record names its subject digest. Add a scheduled mutation-gate workflow and extend the pwb mutation tooling to polaris-generation-core's four files with a docs/evidence record; re-run the rule-6 mutation. Carry the failure code out of the bare catch at pipeline.ts:249-252 and replace localeCompare with ordinal compare. Characterize the 1z3.28 flake as part of the first scheduled run.
- **Why.** C1-F1(f): three agents proposed the same instrument for three populations; build it once. S13-F1/F2 [Observed]: mutation tooling has never run in CI and the generation package has zero mutation evidence; S7-F2: the rule-6 record is stale; S3-F1: the reading plan drifted silently. VIS-2 (a stale evidence record is a claim without evidence), VIS-6, trust-and-evidence rule 6.
- **Evidence.** S3-F1, S13-F1, S13-F2, S13-F3, S13-F4, S14-F1, S14-F2, S7-F2, L4-F4. Merges agent moves S3-M1, S13-M3, L4-M3, S7-M2, S13-M1, S13-M2, S14-M2, S14-M1, S7-M3.
- **Prerequisite.** none. Doctrine: VIS-2, VIS-6, trust-and-evidence rule 6. Theme 8.
- **Relates to.** `syzygy-1z3.28`, `syzygy-dov.11`.
- **owner_value 4 / build_cost 2.**
- **Slices.**
  1. scripts/check_evidence_currency.py over the three populations; rule 11 in AGENTS.md; first run recorded.
  2. Scheduled mutation gate workflow; generation-core mutation markers + evidence record; rule-6 re-run.
  3. pipeline.ts failure code; ordinal compare; tests.
  4. 1z3.28 flake characterization from the scheduled run's output.

### N12 — Reach-cost and reading-budget instruments: the nine cold-open answers indexed with their word offsets, a stated stopping point, a scripted comprehension probe, and a population-scale a11y fixture with duplicate-name and heading checks, run against all four pages

- **What.** Record reach cost in the PWB-REQ-021 walkthrough record: for each of the nine cold-open questions, the body word at which the page answers it, with a nine-row index rendered in the contents list and an explicit stopping point ('the nine answers end here'). Make the walkthrough a scripted comprehension probe that runs against a capture and leaves a run record, and select the deep-dive capability by demonstrated value rather than transport. Replace the a11y checker's 144-focusable fixture with a population-scale one and add duplicate-accessible-name and heading-skip checks. Run the reach-cost probe against Trajectory, Orrery and the home page, which no agent tiered this run (C1-F5), and state the word denominator (C1-F2: 9,403 flow-visible / 26,630 expanded; the 10,173 figure is not reproducible).
- **Why.** L9-F1 [Observed]: all nine answers arrive by body word 3,206 and the page says so nowhere; a reader has no licence to stop. S15 gap [Observed]: the owner walkthrough has never been run. S2-F2/F3: the checker's denominator is ~10% of the page and it cannot see 390 same-named links. VIS-1 comprehension, VIS-3 digestible by an unfamiliar human, VIS-7 encodings mean what the legend says.
- **Evidence.** L9-F1, L9-F2, L9-F3, S15-F1, S15-F2, S2-F2, S2-F3, C1-F5. Merges agent moves L9-M1, L9-M2, S15-M3, S15-M2, S2-M2, S2-M3, S2-M4.
- **Prerequisite.** spec amendment. Doctrine: VIS-1, VIS-3, VIS-7. Theme 5.
- **Relates to.** `syzygy-1z3.22`, `syzygy-dov.13`, `syzygy-dov.3.1`.
- **owner_value 4 / build_cost 2.**
- **Slices.**
  1. Spec: PWB-REQ-021 delta adding reach cost and the run record; word-denominator method stated.
  2. Probe script over a capture: nine questions -> word offsets; contents-list index + stopping point on the page.
  3. a11y checker: population-scale fixture, duplicate-name and heading checks; fix what they find.
  4. Run the probe on Trajectory, Orrery, home; tier them in the next dossier.

### N13 — Generation loop evidence: restore the claim ledger as the intermediate, a frozen-case corpus with an evaluation runner that detects regression not change, generated prose over claim ids with a computed tuple, and the run-contract envelope fields landed

- **What.** Make the generator's intermediate the kit's claim ledger (spans, state, meaning, edges) instead of the weaker record it holds now; freeze a case corpus under docs/evaluation/ with an evaluation runner that scores each case so a prompt change is judged by outcome, not by hash; generate prose over claim ids so every sentence carries a computed tuple; land the run-contract envelope fields in the types so example.json validates; ship a quickstart an outside adopter can run.
- **Why.** L3-F3 [Observed]: there is no evaluation runner, so the prompt hash detects change and not regression; L3-F2: the intermediate is weaker than the ledger the kit already defines. S9-F1/F2: the flagship example fails the landed validator because the envelope fields do not exist in the types. VIS-2 (every generated sentence carries its state), VIS-1, VIS-3.
- **Evidence.** L3-F2, L3-F3, L3-F4, L3-F5, S9-F1, S9-F2, S14-F3. Merges agent moves L3-M2, L3-M3, L3-M4, S9-M2, S14-M3.
- **Prerequisite.** spec amendment. Doctrine: VIS-2, VIS-1, VIS-3. Theme 6.
- **Relates to.** `syzygy-mea`, `syzygy-dov.6`, `syzygy-dov.6.1`, `syzygy-dov.6.2`, `syzygy-dov.23`.
- **owner_value 4 / build_cost 3.**
- **Slices.**
  1. Spec: CC-REV-2 delta naming the claim ledger as the intermediate and the tuple-per-sentence rule (dov.23 family).
  2. Core: claim-ledger intermediate; envelope fields in types; example.json regenerated from the demo and validated in tests (fold-in to dov.6.2 travels in N1).
  3. docs/evaluation/: frozen cases + runner; first scored run recorded.
  4. Quickstart for an outside adopter; run it from a true git clone (settles S9's tier and one limb of P-52).

### N14 — Doctrine amendment packet A, the molding half: a lawful boundary for unprompted derived computation, a regeneration rehearsal, and a Butlers-side push trigger

- **What.** Draft, for the owner to adopt or reject, one amendment to VIS-4 and the 'Not autonomous' clause: a closed class of unprompted derived computation (observe, compute the delta, stage a draft, hold) is lawful when its trigger is a human act or a human-installed hook firing on a human act, and unlawful when its trigger is a clock Syzygy owns; explicitly forbidden unprompted: notify, dispatch, adopt, self-wake. Show it is non-expanding by mapping each permitted effect to a ruling that already allows it narrowly (P-71 Q3, P-79 Q4, VIS-6(a)); state the entry criteria it gives the live-observability mandate v1.md:82 leaves unstated. Under it: a regeneration rehearsal (re-run generation against the current corpus, diff against the last adopted output, hold) and a Butlers-side post-merge hook as the lawful push trigger for N2.
- **Why.** The owner's north-star sentence says the project will eventually mold itself around a tuned goal; today 'Not autonomous. The loop is human-triggered' plus P-69's no-timer rule leave no lawful unprompted computation at all, so the molding half has no mechanism to grow into and every cadence slice relitigates the boundary (L11-F1, L11-F8). Naming it once at minimum width is cheaper than not. VIS-4, VIS-5 (no widening of the write universe), VIS-6.
- **Evidence.** L11-F1, L11-F8, L10-F3, L4-F2. Merges agent moves L11-M5, L10-M6, L4-M4.
- **Prerequisite.** doctrine amendment. Doctrine: VIS-4, VIS-5, VIS-6. Theme 3.
- **Relates to.** `syzygy-dov.28`, `syzygy-dov.4.1`.
- **owner_value 4 / build_cost 2.**
- **Slices.**
  1. Draft amendment text with trigger test, permitted list, prohibitions; blast-radius sweep over existing rulings.
  2. Entry criteria for the live-observability mandate.
  3. Owner decision packet with the no-change arm spelled out.
  4. If adopted: regeneration rehearsal and the push-trigger hook enter the feature-request funnel.

### N15 — Doctrine amendment packet B, Inferred as a first-class rendered state: a synthesis copy role that carries Inferred, an AttributedAnswer record, a typed Inferred correspondence claim, an observed-only project under VIS-6, and a reflexive-observation clause

- **What.** One drafted packet: (a) a synthesis copy role the page may use for sentences that combine sources, always rendered Inferred with its inputs cited; (b) an AttributedAnswer record for agent-produced answers; (c) a typed Inferred correspondence claim linking a claim on one surface to its subject on another; (d) naming the observed-only project's position under VIS-6; (e) a reflexive-observation clause for Syzygy observing itself; (f) a generator figures stage. Each is non-expanding on the write universe and is offered with its no-change arm.
- **Why.** L9-F3 [Observed]: the page is 1.23x its sources' length with zero synthesis and zero Inferred claims, and S4-F3/C1-F4 confirm 0 of 729 tuples are Inferred (the word appears twice, both in the legend); the state the doctrine reserves for agent output is unconstructible by any module. L6-F2: cross-surface correspondence has no claim type to be true or false in. VIS-1 comprehension needs synthesis; VIS-2 needs it labeled; VIS-6 needs to say who owns it.
- **Evidence.** L9-F3, L6-F2, L2-F5, L8-F5, S4-F3, C1-F4, C1-F5. Merges agent moves L9-M4, L3-M7, L6-M4, L2-M4, L8-M3, S3-M4.
- **Prerequisite.** doctrine amendment. Doctrine: VIS-1, VIS-2, VIS-6. Theme 5.
- **Relates to.** `syzygy-dov.7`, `syzygy-dov.12`, `syzygy-mea`.
- **owner_value 4 / build_cost 3.**
- **Slices.**
  1. Draft the six clauses with citations and blast radius; show each is representable in the current tuple vocabulary.
  2. Owner decision packet, batched with packet A under the owner's batch-decision directive.
  3. If adopted: synthesis copy role and correspondence claim enter the feature-request funnel (Gate 2).

## Increments folded into existing beads (not moves)

The critic (C1-F1) found four agents re-proposing one clause of `syzygy-dov.13.1` and others
re-proposing slices of `dov.6.2`, `dov.11.1` and `dov.8.5` without naming them. These travel in
N1 slice 3 as description appends to the owning bead, each citing this run's finding id:

- `syzygy-dov.13.1` (interpolated labels in the copy oracle): distinct accessible names for the
  390 "Exact text" links (S5-M1), the 283 "Source record" toggles (S1-M2, S15-M1) and the four
  figure summaries sharing one name (S3-M2).
- `syzygy-dov.6.2`: gate `docs/polaris-generation/example.json` in tests against the landed
  validator (S9-M1 residue; the envelope fields themselves are N13).
- `syzygy-dov.11.x` (operability): `observerRevision` in banner and status (S10-M2, L4-F2), one
  request log line per response carrying a 500's cause (S10-M1), drop `tsc -b --force` from
  start (S10-M3), request timeouts and a supervision note (S10-M4). Link `syzygy-u2a`, do not
  duplicate it.
- `syzygy-dov.8.5` (proper-noun census): add the thirteen repair-route template literals to the
  denominator (L1-M5; 52 of 95 uses sit in routes the census never counted).
- `syzygy-dov.2.x` (M2 slice 2): reconcile the act-row wording with L4-M2's two-limb reading.

## Unranked moves retained in the data file

Agent moves the orchestrator did not rank, with the reason class. They are in `unranked_moves[]` and in each agent's `moves[]`; they are not filed.

- S3-M3: one-to-many relations fence (spec amendment)
- S7-M1: surface the grammar-failure reason as Unknown-with-cause (agent said doctrine amendment; likely spec)
- S11-M2: print and forced-colors treatment (none)
- S11-M3: group/index the 194-item source list (none)
- S5-M2: git distance since evaluation at each citation (owner act)
- L3-M5: loopback-only provider port (owner act)
- L3-M6: egress dossier dry run (none)
- L5-M2: challenge channel via PR under .syzygy/governance/challenges/ (spec amendment)
- L5-M3: typed prohibitions from the literal grammar (none)
- L5-M4: frontier and lane register (none)
- L5-M5: per-agent credentials (doctrine amendment)
- L7-M6: second real project as syzygy-mea's own gate (owner act)
- L10-M1: Orrery cover map from anchors with counted Unknown (none)
- L10-M2: change ledger over the 59 active OpenSpec changes (spec amendment)
- L10-M4: Genome inventory instrument (spec amendment)
- L2-M3: folded into N10 (-)
- S8-M2: folded into N5 (-)

## Critic corrections applied

One Opus critic read all 27 outputs available at its hour (L11 and its own output excepted) and re-derived the load-bearing numbers against the captures. The orchestrator applied these:

- Page size is 1,504,691 bytes (1,501,967 characters after UTF-8 decode); five agents quoted the character count as bytes. Ceiling arithmetic in this dossier uses bytes. Prior capture: 2,090,025 B / 2,087,400 chars.
- S5 movement 'up' is disproven (files unchanged since f4589e2); carried as none [Observed].
- S9 movement 'up' is not a measurement of change and did not reproduce the fresh-checkout condition; carried as none [Inferred].
- S14 'up' against a new-surface baseline is read as new-surface/functional.
- L9-F4's '28.2% of visible reading' is the byte share; the reading share of the 718 identical tuples is ~53% of 9,403 flow-visible words (~19% of 26,630 expanded). L9-F2's 10,173-word denominator is not reproducible; reach costs derived from it are re-derived in N12.
- S8-F1's direction is a denominator artifact: per-claim attribute cost fell 1,159 -> 1,154 chars; the fraction rose because lane A removed a 639,806 B non-attribute blob. The old capture measures 38.8%, not the baseline's 49.4%.
- S11-F1's 'grew' is denominator-dependent (33 font sizes on Polaris alone, below the baseline's 35); the standing fact (high fragmentation, unused scale) holds.
- L6-F3 'seven columns' is nine (work-items.ts:86-88); L5/L6's '286 rendered work items' is 291 by the critic's sweep; L4-F1's '699 of 699' is the old daemon, 729 of 729 on the fresh page; both 100% fresh.
- Baseline commit a4a3451 was one commit behind origin/main (9d74185, PR #52, docs/scripts/.syzygy only, 46 files). No POC source is in the diff, so 'no code landed' claims survive; 'nothing is drafted for gate X' claims do not: dov.18, .21, .22, .28 and .30 have merged packages.
- Unverified by the critic and carried with their agents' labels: L7-F2 (22 of 105), L4-F1 (98 of 271), L10-F2 (0 of 283), L9-F3 (81.6%), S2-F2 ('roughly 10x'), and the whole L11 lens (it completed after the critic ran; its denominators are stated in its verification_notes).

## Gaps this run leaves

- Trajectory, Orrery and the home page were captured and never tiered; N12 slice 4 tiers
  them next run. Only L6 and L2 read them at all.
- The theme-3 encoding checker of the prior run (POC-REQ-060; 4-page fixture against 1,085
  tuples) was not re-measured.
- P-52 (pending owner row) is cited by six agents and probed by none; N13 slice 4 settles its
  third limb.
- VIS-5 was cited by 5 of 27 agents and VIS-6 by 8; `v1.md` and the directive register were
  barely cited. The posture file for run 3 should carry both.
- L11 completed after the critic ran; its denominators are stated in its own
  `verification_notes` and were not independently re-derived.

## Pending beads, taken into account

The owner asked for pending beads to be considered. At run start `bd list --limit 5000`
showed 94 rows with status open, in_progress, blocked or deferred: 74 under `syzygy-dov`
(13 of them the gate beads dov.18…dov.30, all open), 7 under `syzygy-u2a`, 4 under
`syzygy-1z3`, and one each for mea, e3e, son, blu, kyt, 5fj, 2dn, 0wf, 8de. How the moves
relate:

- **syzygy-dov (epic) and its 56 children.** Prior run's ruled plan. 18 implementation slices are ready; two in progress (dov.6, dov.17 lane B). N1 changes only the graph (edges, order, fold-ins). N5 files under dov.1 as lane C. N3/N9 queue behind the WIP-one PocModel order (.8.1 then .10.1).
- **syzygy-dov.18-.30 (13 gates).** Owner acts and CC-REV-2 scenarios. Five (dov.18, .21, .22, .28, .30) have drafted, reviewed, merged packages (PR #52); N7 puts them on one screen. N9 travels in dov.22's family; N13 in dov.23's; N2 respects dov.19/dov.28.
- **syzygy-mea (P1, generalized generation).** Zero children (L7-F5). N8 and N13 are the pursuit's reading of what its acceptance criteria still lack; file them as dependents of mea, not competitors, when released.
- **syzygy-1z3.22 (cold-open walkthrough).** Ready with zero edges. N1 sequences it behind .2.1/.3.1/.11.1/.13.1; N12 makes it a scripted probe with a run record.
- **syzygy-1z3.25 (report the completed cycle).** N7's closure band renders exactly this; decide with the owner whether it discharges or duplicates the bead.
- **syzygy-1z3.28 (vitest flake).** N11's first scheduled mutation run characterizes it.
- **syzygy-u2a (runtime hardening; children .2, .6, .7, .8, .9 open).** Blocked on the human gate u2a.1. N6 relates to u2a.2 (snapshot binding); N8 must check u2a.7 (repository discoverability) before building a locator; N10 relates to u2a.6. S10's operability increments fold into dov.11.x with a link to u2a, not a duplicate.
- **syzygy-e3e (consent reference-unresolvable, reason #11).** Same shape as S4-F3 (glossary names 15 states, 5 occur); N1 adds the .10.1 <-> e3e edge; not merged.
- **syzygy-son, 0wf, 5fj, 2dn, blu, 8de.** Not Polaris-facing; zero mentions across 29 agents (C1-F5); untouched.
- **Pending owner row P-52.** Cited by six agents, probed by none. N13's true-clone quickstart run settles its third limb and S9's tier.

## Known ledger the run deduped against

Every agent read and applied the ledger in the harvest file under `ledger`. In brief: the
sixteen ruled moves M1…M16 with their rulings P-68…P-83 and every slice and gate bead under
`syzygy-dov`; lane A of M1 (2ef68f5, landed) and lane B (dov.17, in progress); the foreclosed
M4 slice 6 (P-71 Q5, 2026-09-21); the P-77 Q6 parity denominators; the P-74 Q7 WIP-one PocModel
rule; the P-80 Q1 complete-population rule; the generalized generator and its `tasks.md`; PRs
#28…#34; the P-60…P-63 Butlers-side repairs; the literal-grammar strictness that makes
`v1.md` whole-source Unknown. Main moved once before capture (9d74185, PR #52, docs only);
the captures remained valid.

## Reading the data file

```
jq '.tier_board[] | {agent, baseline_tier, tier, movement, movement_label}' docs/pursuits/2026-09-22-vision-pursuit-data.json
jq '.agents[] | select(.label=="L11-growth-cadence-cost")' docs/pursuits/2026-09-22-vision-pursuit-data.json
jq '.agents[] | .findings[] | select(.severity=="high") | {id, title, claim_label}' docs/pursuits/2026-09-22-vision-pursuit-data.json
jq '.ranked_moves[] | {id, title, merges, prerequisite, owner_value, build_cost}' docs/pursuits/2026-09-22-vision-pursuit-data.json
jq '.ranked_moves[] | select(.id=="N2")' docs/pursuits/2026-09-22-vision-pursuit-data.json
jq '.themes[] | {n, title, exemplars}' docs/pursuits/2026-09-22-vision-pursuit-data.json
jq '.critic_corrections[]' docs/pursuits/2026-09-22-vision-pursuit-data.json
jq '.agents[] | select(.label|startswith("C1"))' docs/pursuits/2026-09-22-vision-pursuit-data.json
```

## Gate

Filed 2026-09-22 as a gated epic in `bd` (embedded Dolt, committed). Closing the gate bead is the
owner's move; nothing in this dossier authorizes execution.

| Bead | Role |
|---|---|
| `syzygy-dca` | `[HOLD]` owner gate (task, P1, assigned to the owner). Every child below depends on it. |
| `syzygy-u05` | Epic (P1, assigned to the owner so it stays off `bd ready`). |
| `syzygy-u05.1` … `syzygy-u05.8` | N1 … N8 (P1) |
| `syzygy-u05.9` … `syzygy-u05.13` | N9 … N13 (P2) |
| `syzygy-u05.14`, `syzygy-u05.15` | N14, N15 doctrine amendment packets (P3) |

Child `k` is move `Nk`. Each child carries the move's slices as design notes and a testable
acceptance list. `bd ready` at filing time showed only the gate and the epic; `bd blocked` listed
all fifteen children; `bd lint` reported nothing new. Memory: `bd memories polaris-vision-pursuit`
(key `polaris-vision-pursuit-2026-09-22`, chained to the 2026-09-13 key). Release:
`bd close syzygy-dca`.
