# Feature request M4 — Close the owner loop: a route from every Unknown, home as the day-opening, and run the return path once

> **Candidate — binds nothing.** This is the feature-request funnel for the
> fourth move released from the 2026-09-13 vision pursuit. It proposes; the
> owner disposes (VIS-4). Nothing here authorizes implementation, and no bead
> becomes runnable by this file. Bead: `syzygy-dov.4`. Dossier:
> `docs/pursuits/2026-09-13-vision-pursuit.md`, section M4. It is written in
> the shape of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`, of the ruling
> that packet produced
> (`.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`,
> the M1 ruling), and of the M2 packet as reviewed four times on
> `agent/syzygy-dov.2`.

Date: 2026-09-14. Author: a funnel session (Claude), for the owner.

Size: **medium** for slices 1–5 (app and core renderer plus machine-payload
fields; observable behaviour changes; no governed artifact touched);
**medium** for slice 6, which builds nothing and runs an existing mechanism
once; **large** for slice 7 and for the deferred pair in slice 8, each of
which needs its own owner act before any code is written.

Baseline: Syzygy `a9f671e` (main; the only working-tree change is a
co-lead's in-flight `AGENTS.md`, unrelated) [Observed].

**The captures this packet measures, and their provenance.** Two sets, and
the packet says which is which at every use.

| Capture | Path | Bytes | sha256 (computed this session) | Provenance |
|---|---|---|---|---|
| Polaris, tailnet host form | the retained lane A *after* capture, `polaris-tailnet.html` | 1,484,487 | `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` | Butlers evaluation revision 2e3bac97790b, committed 2026-09-13T10:31:11Z, captured 2026-09-13T13:33:24.295Z; observer `2ef68f5` |
| Polaris, direct host form | `polaris-direct.html`, same directory | 1,478,637 | `2fecdd01e1a2ff577567495796ea7e59ab89f1420be6033e23314d26442ea094` | same daemon, same evaluation |
| Machine, full model | `api-poc.json`, same directory | 5,520,314 | `a89b0e059b5fdadc5f359c2bee58115cd50747399cfb00444703e0fafdfb466e` | same evaluation |
| Machine, presentation envelope | `api-polaris.json`, same directory | 640,592 | `ab3b517be1e62a0a7f4cabe73d870f9aa6bea7d2bbbadf0d27a2f00c34eca22e` | same evaluation |
| Home page | the pursuit capture directory, `home.html` | 38,706 | `c2fd6d1af7103e871c26dc65b76cc391fe2765a1c7391ac19ddf1656e57b5fca` | **pre-lane-A**: Syzygy `f4589e2`, Butlers 7c8743f63, 2026-09-13T02:03:33.040Z |
| Trajectory | same directory, `trajectory.html` | 244,524 | `fd802531b199084e7145932715150f4977335e49ca6aa168d68d5227c9d6ddde` | **pre-lane-A**, same run |
| Orrery | same directory, `orrery.html` | 37,048 | `e3ae5b7901c599a04b685456e6070430edf72fcd025cd1f6afecf863153582fa` | **pre-lane-A**, same run |
| Machine, pre-lane-A | same directory, `api-poc.json` | 5,508,208 | `8b8d8a3078f085d4d53aa3bcad9d5a06b5b0c064bb8cdc7b3832913a81bc44d0` | **pre-lane-A**, same run |

The retained lane A sha256 was verified against the figure recorded in the
M2 evidence file before any measurement was taken, and matched [Observed].

**Why the pre-lane-A home and Trajectory captures are still valid for this
packet.** `git diff --stat f4589e2..a9f671e` restricted to
`apps/three-surface-poc/src/routes.ts` and
`apps/three-surface-poc/src/trajectory.ts` returns **no rows**, and the same
diff over `packages/three-surface-poc-core/` returns no rows at all: lane A
touched exactly two rendering sources, `apps/three-surface-poc/src/polaris.ts`
(+25/−6) and `apps/three-surface-poc/src/polaris-narrative.ts`, plus tests and
the new `apps/three-surface-poc/src/polaris-generation/` directory [Observed:
`git diff --numstat` over both paths, this session]. So the home, Trajectory
and Orrery renderers at `a9f671e` are byte-identical to the ones that
produced those captures; only the observed Butlers revision differs
(7c8743f63 versus 2e3bac97790b), and every count this packet takes from them
is a count of *rendering structure*, not of Butlers content. Where a count
could move with the Butlers revision, it is taken from the lane A capture.

## The seven questions for the owner

Batched, each with the recommended answer first. Q1, Q3, Q5 and Q7 are owner
gates in the strict sense: Q1 decides whether rendered Unknowns across all
three surfaces are in breach of a requirement in force, Q3 decides whether a
new write effect is authorized at all, Q5 confirms what a run may honestly
be expected to produce **and**, since review 1 (F4), whether that run's
existing write into the observed repository's tracker is itself authorized,
and Q7 orders this move against three sibling packages **and**, since review
1 (F3, F6) and review 2 (G1, G2), reconciles the file-level collisions — now
three packages writing one page region, not two — and names the authorization
arm slices 4 and 5 rest on. **Superseded 2026-09-15 (review 2, G4).** This
preamble read: "Q6 is contract-determined on this packet's own reasoning — it
has one lawful arm and one that mints a vocabulary value no requirement enters
— and is put to the owner for confirmation and disclosure rather than as a
free choice." Both halves were wrong. Neither Q6 arm mints a vocabulary value;
that phrase belongs to Q2 alone, about `none-modelled`. And
"contract-determined" is the opposite of what this packet establishes about
`model.surfaces` in three other places — Gate 0, Gate 3's slice-4 row and Gate
5 all state that **no requirement in either signed spec governs the home route
or `model.surfaces`**, on three sweeps with their denominators. **Q6 is
therefore a genuine engineering choice, put to the owner *because* no
requirement reaches the field, not because one constrains it**: both arms —
derive the field, or delete it — are lawful today, exactly as Gate 5's own
consequence sentence says ("changing the home page freely is lawful today
precisely because nothing specifies it"), and the Q6 row states deletion's
cost rather than denying deletion is available. **Q2 is a genuine choice,
corrected from the draft's contract-determined framing** (review 1, F2): the
code models a routeless Unknown today, so minting `none-modelled` competes
with naming the existing arm rather than being foreclosed. Q4 is a real
choice between two lawful arms.

| # | Question | Recommended |
|---|---|---|
| Q1 | **Nine of the twenty-two Unknown disclosures Polaris renders carry no reason from the closed RFC2-24 twelve and no route. Is that a POC-REQ-060 non-conformance to be repaired, or the accepted shape of the entity-and-relationship graph?** [Observed: 22 `data-unknown-disclosure` elements on the retained Polaris capture; 13 contain a `data-unknown-reason` value and the literal `Route:` inside their own element; 9 contain neither — the four entity Unknowns and all five relationship Unknowns. Method and offsets in the evidence record. **Scope correction (review 1, F5):** POC-REQ-060 quantifies over "every epistemic encoding across the three surfaces", not Polaris alone. Measured this session on the other surfaces' retained captures, **raw and rendered** (corrected per review 2, G3) [predicate: literal occurrences of the string `epistemic-unknown`; denominator: the whole served page; then partitioned by enclosing tag, a partition that accounts for every occurrence on every page]: Trajectory **0** `data-unknown-disclosure` elements and **301 raw** `epistemic-unknown` occurrences = 1 stylesheet rule + 1 legend key item + **299** claim-carrying spans; Orrery **0** and **11 raw** = 1 + 1 + **9**; Home **0** and **18 raw** = 1 + 1 + **16**; Polaris **2 raw** = 1 + 1 + **0**, so the class marks no Polaris claim at all and the 22 `data-unknown-disclosure` elements (offsets 378,631 through 1,462,622) contain zero occurrences of it. Trajectory and Orrery render every occurrence of the literal `epistemic-unknown` as a bare class span, with no disclosure wrapper, no closed reason and no route at all — a *third* encoding, never before measured against this requirement. **Superseded 2026-09-15 (review 3, H1):** this clause read "Trajectory and Orrery render **every Unknown** through the bare `epistemic-unknown` class", which asserts that one class literal exhausts those surfaces' rendered Unknown population. The predicate actually run counts occurrences of that one literal, not that population, and a fourth family sits outside both censused ones. **Fourth encoding family, added 2026-09-15 (review 3, H1): `provenance-none`.** `apps/three-surface-poc/src/exact-tables.ts` line 10 emits `<span class="provenance-none">No positive provenance; this relationship remains Unknown.</span>` whenever an entity's or relationship's `provenance` array is empty. Counted this session [predicate: literal occurrences of the string `provenance-none`; denominator: the whole served page; then every occurrence assigned to its enclosing tag, a partition that accounts for every occurrence on every page]: Polaris **0** on both lane A forms; Trajectory **0**; Orrery **9**, all nine rendered spans with **0** occurrences inside `<style>`; home **10** = 1 stylesheet rule + **9** rendered spans. The nine Orrery spans sit inside the `<tr>` elements whose ids are `work:whatsapp-single-event-normalization`, `evidence:focused-pytest`, `runtime:live-satisfaction`, `region:unmapped-code`, `relationship:intent-to-work`, `relationship:work-to-code`, `relationship:code-to-evidence`, `relationship:code-to-runtime` and `relationship:capability-to-unmapped-region` — **exactly the nine objects this question is about**, the four entity Unknowns and the five relationship Unknowns, reached a third time and by neither censused family [Observed]. Two facts make this POC-REQ-060's own falsifier rather than a naming quibble. **First, `provenance-none` is in no declared token table:** `apps/three-surface-poc/src/design-tokens.ts` line 25 declares `className: 'epistemic-unknown'` and that file names `provenance-none` nowhere; its only style rule is `apps/three-surface-poc/src/routes.ts` line 73, `.provenance-none { color: var(--unknown); font-size: .8rem; }`, inside `HOME_STYLE` — declared at line 57 of that file and passed as `extraStyle` at line 90, the home route, and nowhere else. A span carrying the Unknown colour token under a class the declared table does not carry is the falsifier's second limb verbatim, "or a surface styling epistemic state ad hoc" (spec line 946). **Second, the same class renders differently on two surfaces:** `apps/three-surface-poc/src/orrery.ts` imports `exactTablesSection` at line 4 and calls it at lines 125 and 151 without `HOME_STYLE`, so home carries the rule and Orrery carries **0** style occurrences against its nine rendered spans — the falsifier's first limb, "one surface encoding Unknown (or Observed) differently from the declared table" [Observed, this session, over the retained captures and the four source files named]. Noted in passing, not itself a finding against this packet: the literal reads "this **relationship** remains Unknown" on all nine rows, four of which are entities. **Superseded 2026-09-15 (review 2, G3):** this cell reconciled the two marker families with the clause "`epistemic-unknown` counts a CSS/data class occurring on every surface, **including Polaris's own 22 disclosures**", and offered 301 and 11 as the population. The clause is false — Polaris carries exactly two occurrences, one inside `<style>` and one in the legend list, and none of the 22 disclosures carries it — and those same two non-claim occurrences sat inside every published figure, so a stylesheet declaration was inside the denominator of a requirement about what a surface *renders* (verification rule 4). **Superseded 2026-09-15 (review 3, H2).** This sentence read "**Re-checked against the corrected figures, the third encoding is still the largest of the three:** 299 + 9 = **308** rendered claim encodings across the two surfaces, against Polaris's 13 routed disclosures and 9 bare-prose ones". Ranking the encodings by size is the cross-family comparison the next sentence forbids, and the two terms count different objects — `epistemic-unknown` spans on Trajectory and Orrery against disclosure elements on Polaris. Restated as what was actually measured: **each surface's Unknowns are encoded by a marker the other two do not share**, and the per-family denominators are reported unranked [Observed, this session, over the four retained captures]. The two marker families are still not directly comparable (`data-unknown-disclosure` counts disclosure elements on Polaris; `epistemic-unknown` is a CSS/data class whose occurrences must be partitioned before they count as encodings), so each is reported against its own denominator, never combined into one total. Home's 16 is stated for completeness and sits outside POC-REQ-060's three-surface population.] | **A non-conformance, repaired by slice 1 — but slice 1's sweep must cover a marker the three renderers actually share, not `data-unknown-disclosure` alone.** POC-REQ-060 is an invariant in force over "every epistemic encoding across the three surfaces" and its falsifier is "one surface encoding Unknown (or Observed) differently from the declared table". Across the three surfaces there are at least **four** encodings today (**corrected 2026-09-15, review 3, H1**, which superseded "at least three encodings today"): Polaris's reason-span-plus-`Route:` (13 of 22), Polaris's bare prose (9 of 22), Trajectory/Orrery's bare `epistemic-unknown` span with no disclosure wrapper, reason or route (299 and 9 rendered claim encodings respectively, from 301 and 11 raw occurrences — unmeasured until this repair, and re-partitioned per review 2, G3), and Orrery's `provenance-none` span over the same nine objects (9 rendered, against 1 stylesheet rule and 9 rendered spans on home and 0 on Polaris and Trajectory). The prose comes from `unknown(reason: string)` at `packages/three-surface-poc-core/src/model.ts` line 305, which accepts any string; RFC2-24 closes the reason vocabulary at twelve and says a condition genuinely not among them "is disclosed as a **fact of the render** — named, expandable, routed to its resolving action — never dressed as a reason". Rule it a repair, not a redesign: the nine Polaris disclosures keep their existing sentences as the *basis* text and gain a closed reason and its route, and slice 1 must additionally either require Trajectory and Orrery to emit the same `data-unknown-disclosure`/`data-unknown-reason` marker pair the sweep checks, or the sweep is re-specified over a marker the three renderers already share (see slice 1's repaired Tests section). **Whichever arm the owner takes, the shared marker must cover the `provenance-none` rendering too** (added per review 3, H1): its nine Orrery spans are nine encodings of exactly the nine Unknowns this question is about, so a sweep blind to them would pass on every denominator published here while POC-REQ-060's falsifier still stands. Slice 1's Tests carry the corresponding rule-6 mutant. **The recommended arm itself does not change** [Observed: the remedy turns on the zero-denominator fact — Trajectory and Orrery emit 0 `data-unknown-disclosure` elements — which the fourth family neither creates nor removes; it widens the marker's required coverage, not the arm]. |
| Q2 | **L5-M4 proposes minting `none-modelled` as a third state so that an empty `resolutionRoutes` array "stops being legal". Mint it?** This is a genuine choice, not contract-determined as review 1 (F2) found the packet had wrongly framed it: `routesFor`'s actual code and cap1-core's `EpistemicState` type both already model a routeless Unknown, so `none-modelled` is not foreclosed by construction — it competes with an existing, narrower arm. | **Do not mint `none-modelled`; instead name and route the existing `basis: 'deferred'` arm.** Corrected facts (review 1, F2). `routesFor` (`packages/three-surface-poc-core/src/project-shape-model.ts:151`) is `if (state.label !== 'Unknown' \|\| !('reasons' in state)) return [];` — **two** return-`[]` branches, not one: not-Unknown, and Unknown-with-no-`reasons`. cap1-core's `EpistemicState` (`packages/cap1-core/src/epistemic.ts:50-67`) has exactly that second arm as a third union member: `{ label: 'Unknown', basis: 'deferred', tier?, freshness? }` — no `reasons` field, so it cannot borrow a route from RFC2-24's twelve either. So a routeless Unknown is *modelled today*, not "unreachable by construction"; what is true, and confirmed this session on both machine captures, is the narrower, data-only fact that **0 of 1,137** empty-array claims are Unknown — no claim in either retained evaluation exercises the deferred arm. Two measured facts still hold and still argue against minting a *new* value: (a) of the 1,149 objects carrying `resolutionRoutes`, 1,137 are empty (all `Observed`) and 12 are non-empty (all `Unknown`) [Observed: both machine captures, identical]; (b) the state L5-M4 wants a name for **already exists as declared copy** — `label.no-route`, text "No route declared" (`apps/three-surface-poc/src/polaris-copy.ts:193`), used as the fallback in `routeOf` (`polaris.ts:466`) and `reasonRouteHtml` (`polaris.ts:473`), and listed in the copy oracle's `UNREACHED_IN_FIXTURES` set (`polaris-copy.test.ts:297,299`, which also lists `label.deferred` — the row that names the arm this packet had missed). The revised recommendation: narrow slice 2's type-level prohibition to "an Unknown *carrying `reasons`*" (never the deferred arm), let the deferred arm render `label.deferred`/`label.no-route` as it already can, and treat this as two legal states at the type level — a populated route, or the declared no-route copy on either kind of routeless Unknown — the same count slice 2 already designs to, now correctly attributed. Minting `none-modelled` would still add a fourth spelling for a state the page can already render two ways; the owner may instead choose to mint it and retire `label.deferred`/`label.no-route`, which is the genuine choice this question now poses. |
| Q3 | **May Syzygy generate a drafted owner-act packet from a gap row, and if so, into whose tree?** The observed repository's write surface is empty and stays empty; Syzygy's own `.syzygy/**` is a lawful write root under VIS-5; but a drafted act about the observed project's gaps would sit in the governance tree of a project that does not govern it. | **Hold slice 7 until this rules; recommended arm is (a) with a narrow new act.** Arm (a): the drafter emits the packet into Syzygy's own `.syzygy/governance/decisions/`, marked `DRAFT, binds nothing`, under a fresh narrow owner direction naming the effect, the claim classes eligible, and a ceiling on drafts. Arm (b): the drafter is pure and emits packet *data* on request, writing no file at all; an operator command renders it. Arm (c): decline. (a) is recommended because v1.md lines 30–31 make first-pass drafting for owner sign-off V0's literal first action on an under-declared project and VIS-4 permits drafting and nothing more — but it is not available without a gate, for two reasons this packet found and neither move stated. First, the adapter registry entry's `typedAuthority.writeSurface` is `[]` and `executeObservedCode` is `false`, and the 2026-09-02 implementation authorization's "What this does not authorize" section reads "No write, egress, execution, deployment, release, recovery, or mission effect on Butlers or on any other repository. The observer registry entry the owner adopted declares an empty write surface; that remains the bound" — so nothing may be written toward the observed project, and the drafted packet's subject is that project's gaps. Second, writing a governance artifact of the observing project *about* the observed project is a new effect no act in force names; the 2026-09-02 act's escalation trigger "any scope beyond the signed change" is the hook. Arm (b) needs no act and is a lawful partial: the pure drafter can be built and tested with no filesystem at all, which is what slice 7 sketches. |
| Q4 | **The opening "what needs you" band: does it list every Unknown reason present, or only the owner-actionable subset?** Both arms are lawful; neither turns anything green. | **Every reason present, with the owner-actionable ones foremost.** L2-M2 proposed a closed actionable subset of four. On the retained capture the whole gap population is **one** reason over 12 claims (`excluded-content`), so a four-reason filter is untestable against today's evaluation and its counterexample test would have no negative case from real data [Observed: `data-polaris-gap` occurs once, `id="polaris-gap-excluded-content"`, and the list's own text reads "12 claim(s)"]. Listing every reason and ordering by the existing `foremost` array in `gapsList` (`apps/three-surface-poc/src/polaris.ts` lines 933–948, already ordering `missing-declaration` then `unconsented-source-or-provider`) reuses a tested ordering, keeps the band's denominator equal to the gaps section's, and needs no second closed constant to drift. The owner may prefer the filter if the band must never show a reason they cannot act on; say so and slice 3 adds the constant. |
| Q5 | **Run the return path once (slice 6): is it authorized, is its existing write into the observed repository's tracker authorized, and what may it honestly be expected to produce?** | **Expectation: rule in advance that one edge narrows and two stay Unknown — that is a pass.** Measured at `a9f671e`: `relationship:work-to-code` (`model.ts` line 588) and `relationship:code-to-evidence` (line 597) are **unconditional `unknown(...)` literals** — no input reaches them. `workerChange` and `testArtifactVerification` are computed at lines 418–437 and carried as top-level model fields at lines 701–702, and **no relationship reads either** [Observed: a `grep -n` sweep for both identifiers over the file returns lines 30, 42, 124, 125, 418–433 and 701–702, none inside the relationship array]. The reason is deliberate and recorded in the file: `WORKER_CHANGE_SEAM` (comment 26–29, const 30–33) is "distinct from ARTIFACT_PATHS.code/test below", and `WORKER_CHANGE_INTENT_ID` (comment 35–41, const 42) is exported so Trajectory can name it "on the one place this evidence is honestly scoped to: the worker-change badge, never the identity-resolution entity graph above" — the same false-`Verified` wiring AGENTS.md records as already reverted once. Only `relationship:intent-to-work` is conditional (line 570, on `materialization.beadId`). The dossier's "What" bullet (not its "Why" bullet, corrected per review 1 N6) says the next evaluation narrows three edges; the code says one, deliberately, and the honest-reporting caveat this correction leans on is already recorded in both the dossier's own slice-6 bullet and L5-M7's slice plan — the new, valuable measurement is *which* edges and *why*, not that under-reporting was undisclosed. **Authorization is genuinely contested and this packet does not resolve it (review 1, F4).** Two readings, both quoting the record: **Reading A — authorized.** The 2026-08-29 mode direction (`THREE-SURFACE-POC-MODE-DIRECTION.md` lines 18–22) requires the experiment to "demonstrate ... human-triggered work, a worker-authored real code/test change ..."; the materialize mechanism was built under that direction, which predates and is a separate authorization lane from the 2026-09-02 PWB act, whose **body section "What the recorder reads this as" (lines 44–52)** says the recorder reads the owner's "Authorized" reply as "the separate implementation authorization that task 1.8 requires, and nothing wider", authorizing "**Implementation planning and implementation** of the signed `polaris-project-wide-butlers-model` change — tasks §2 through §5 of its `tasks.md` — as one bounded improvement cycle of the Three-Surface POC" (quoted in source order and with the tasks-range clause restored, corrected per review 2, G5: the earlier citation said "header", which is the comment block at lines 1–17 and carries none of this, and its ellipsis reversed the source order rather than eliding within it) — so its "does not authorize" bullets bound the *PWB* grant, not a retroactive revocation of the earlier, separately authorized mechanism. **Reading B — a breach.** `apps/three-surface-poc/src/materialize-action.ts:33` sets `targetRepoRoot: model.project.root` (the observed Butlers root); `packages/three-surface-poc-core/src/materialization.ts:12` sets `MATERIALIZATION_TARGET_BEAD_PREFIX = 'bu'`, the observed project's own prefix, not Syzygy's; and `defaultRunCreate` (lines 186–208) runs `execFileSync('bd', ['-C', repoRoot, 'create', ...])` — a mutation of the observed repository's Beads database. `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` lines 70–72, quoted verbatim: "No write, egress, execution, deployment, release, recovery, or mission effect on Butlers or on any other repository. The observer registry entry the owner adopted declares an empty write surface; that remains the bound." Read as a general constraint on the POC's relation to Butlers rather than a PWB-task-scoped bullet, it forecloses running slice 6 today regardless of the 2026-08-29 direction, and it applies with the same force Q3 gives it against slice 7 — an argument this packet's own Gate 2 (VIS-5 paragraph) reads the opposite way when defending the same mechanism. **Recommended, [Inferred]: Reading A — rule the run authorized as an exercise of a pre-existing, separately authorized mechanism — with the counter-argument above stated for the owner, not resolved by this packet.** Slice 6 is conditional on this ruling: if the owner takes Reading B, slice 6 does not run until a continuation names the effect, the same arm Q3 offers for slice 7. |
| Q6 | **`model.surfaces` declares Polaris presents 4 entities; the page presents 415 items and 713 claim tuples ([Observed: `data-claim-id="` occurs 713 times on the lane A tailnet capture; the pre-lane-A figure was 699 — recorded here per review 1, N9]). Make the field true by construction, or delete it?** Both arms are lawful; deletion has a cost the move does not name, stated here so the choice is made knowing it (reworded 2026-09-15 per review 3, H8, which superseded "Disclosed for confirmation: deletion has a cost the move does not name" — readable as the framing review 2's G4 already superseded). | **True by construction (L6-M4's descriptor), not deleted.** `model.surfaces` is the only place in the shared model that states the surface-to-content mapping. `renderPocPage` (`apps/three-surface-poc/src/routes.ts` lines 77–96) reads `model.surfaces`, `model.project`, `model.entities`, `model.capabilityId` and `model.evaluation` — five fields, and nothing else [Observed: a sweep of the literal `model.` over the file yields **13** hits over nine lines — 35, 78, 87, 89 (×4), 92 (×2), 127, 133, 171, 172 — of which the **five** outside `renderPocPage` (lines 77–96) are `model.entities` (35), `model.projectShape` (127) and one each at 133, 171 and 172; corrected per review 1, N5 and again per review 2, G10, which superseded "89 (×2) … the four outside": line 89 carries four occurrences (`model.project`, `model.entities`, `model.capabilityId` twice) and the enumeration that followed named five lines, not four — the evidence file's earlier "only other hit" claim named just line 127]. Deleting `model.surfaces` therefore deletes **the only input for the three surface panels**, not the home page's every input — the eyebrow, lede, heading, footer and exact tables survive on the other four fields (corrected per review 1, N5). Keeping it and making it derived is still the smaller step and lands slice 5's descriptor for free, and slice 5's own design already reads it that way. Note that one of the three entries is **already** derived — Orrery's `entityIds` and `relationshipIds` are `entities.map(…)` and `relationships.map(…)` at `packages/three-surface-poc-core/src/model.ts` lines **747–748** (corrected per review 1, N1) — so the defect is two hand-written lists, not three. |
| Q7 | **Sequencing against M2 (`syzygy-dov.2`, P-69), M3 (`syzygy-dov.3`, P-70) and lane B (`syzygy-dov.17`, P-68); which M4 slices may start now; and which authorization arm slices 4 and 5 rest on.** | **Slices 1–2 after M3 slice 5; slice 3 only after the three-way opening-band reconciliation (below, revised per review 2, G2); slices 4–6 as sequenced; slice 7 waits on Q3; slice 8 is deferred behind its own acts.** No M4 slice opens a specification package, so none collides with P-68's pending PWB amendment. **Shared-file set, re-derived (review 1, F3) from both sibling packets' own Gate 3 tables, not asserted:** M2's Gate 3 (register row P-69) names `packages/three-surface-poc-core/src/model.ts` (its slices 2, 3), `apps/three-surface-poc/src/routes.ts` (slice 3), `apps/three-surface-poc/src/polaris.ts` (slices 1, 2 **and 6** — corrected per review 2, G9) and `apps/three-surface-poc/src/polaris-copy.ts` (slice 1), plus `packages/three-surface-poc-core/src/project-shape-model.ts` (slice 5). M4's own Gate 3 names `model.ts` (slices 1, 2, 4), `routes.ts` (slice 5), `polaris.ts` (slices 1, 3), `polaris-copy.ts` (slice 3) and `project-shape-model.ts` (slice 2). **The shared set with M2 is five files** — `model.ts`, `routes.ts`, `polaris.ts`, `project-shape-model.ts` and `polaris-copy.ts` [Observed, re-derived by hand this session from the two Gate 3 tables, with both denominators: M2's "Lives in" column names **9** distinct files (`polaris-copy.ts`, `polaris.ts`, `git-observation.ts`, `main.ts`, `model.ts`, `routes.ts`, `polaris-reading.ts`, `project-shape-model.ts` and the adapter-registry declaration JSON; its "copy-oracle test" and two "plus one test" phrases name no file), M4's names **13** (`model.ts`, `polaris.ts`, `orrery.ts`, `trajectory.ts`, `polaris-parity-sweep.test.ts`, `project-shape-model.ts`, `polaris-copy.ts`, `routes.ts`, `exact-tables.ts`, `routes.test.ts`, `capture-test-artifact-main.ts`, `scripts/check_governance.py`, `materialization.ts`), and the intersection is 5 of 9 against 5 of 13]. **Superseded 2026-09-15 (review 2, G1):** this sentence read "**The shared set with M2 is four files**" and the Collision section listed `polaris-copy.ts` among the M2 files "which M4 does not touch" — false, and contradicted thirty lines later in the same section, since M4 slice 3's own Gate 3 row names `polaris-copy.ts`. The fifth file is the sharpest of the five rather than an incidental: M2 slice 1 edits `polaris-copy.ts` lines 45–49 and M4 slice 3 adds the band's own rows to the same declared-copy array, and both are covered by the copy oracle in `apps/three-surface-poc/src/polaris-copy.test.ts`, whose `UNREACHED_IN_FIXTURES` set (line 296) each change must reconcile — **so M2 slice 1 and M4 slice 3 cannot land independently.** With M3 (register row P-70; cite it by row and by the two files, never by head — see review 2, G7) the shared set is **two** files, `polaris-copy.ts` and `polaris.ts`; M3's Gate 3 names `polaris.ts` in slices **1, 3, 5 and 6** and `polaris-copy.ts` in slices 3 and 5 (corrected per review 2, G9, which superseded "M3 slices 3 and 5 both edit `polaris.ts`"), not the one file this packet originally named. **The missed collision (F3(c)), widened to three packages (review 2, G2).** M2's slice 2, M3's slice 3 and M4's slice 3 all render into the **same region** — the opening band of `polaris.ts`, before the first catalog section — with three distinct payloads. M2 slice 2: an evaluation-currency disclosure carrying its own epistemic tuple (its Gate 3 row names "`polaris.ts` (the opening band)", its design body opens "Rendered in the opening band, before the first catalog section:", and its own honest target is that "the page's first human-visible instant moves from 58.0% depth into the opening band"). M3 slice 3, "One real Unknown in the first reading": the page's two existing whole-shape and class-level Unknown claims, oracled on "the first rendered Unknown precedes the first `data-polaris-group=\"catalog\"`". M4 slice 3, "The opening band": the `gapReasonCounts` projection, oracled on "the band's total equals the gaps section's total." **Superseded 2026-09-15 (review 2, G2), and this is a changed recommended answer, stated plainly:** this packet recommended "**One band, one owner, one oracle: M3 slice 3 should land first and M4 slice 3 should extend it**" — a two-way reconciliation derived from a pairing that never saw M2 slice 2, so it named the wrong population and pre-empted an ordering that is three-way. **Revised: one band, one owner, one oracle across all three packages.** The three payloads are distinct claims and none subsumes another, so they are three blocks and not one; but they are one *region*, and three independent "renders before the first catalog section" assertions are three oracles over a single piece of page order. So whichever of M2 slice 2, M3 slice 3 and M4 slice 3 lands first **builds the band container and owns its single ordering oracle** (the whole band precedes the first `data-polaris-group="catalog"` occurrence); the other two add a payload block inside that container plus their own payload-specific oracle (M3's first-rendered-Unknown, M4's band-total-equals-gaps-total), and neither builds a second band. The block order *within* the band is the owner's to set, not this packet's — a currency disclosure and an Unknown band are arguably separate regions, and if the owner rules them so, each still needs a stated position relative to the other two rather than three independent claims on "first". Reconcile explicitly before any of the three starts, and record the merged design in whichever packet lands last. **Authorization arm for slices 4 and 5 (F6):** both slices trace, on this packet's own Gate 3 account, to "the recorded-finding arm of the 2026-08-30 direction, naming L6-F5 / L6-F1" — an audit finding in `docs/pursuits/2026-09-13-vision-pursuit-data.json`, not in `docs/reviews/` as the direction's own worked example is written, and no requirement in either signed spec reaches the home route or `model.surfaces` [Observed, re-swept: 24 POC requirements, 17 PWB requirements, 0 whole-word `home` hits in the POC spec, 6 in the PWB spec all in the precedence table's `Home` column or the registry's governance-home field, 0 hits for the backticked `surfaces` or `model.surfaces` in either]. This reading is defensible — an L6 audit is a review/audit of the runnable POC in fresh context producing evidence-cited findings, which is the direction's own definition of a cycle's step (1) — but it is this packet's own [Inferred] reading, not something Q5 puts to the owner (Gate 3's and Gate 5's sentences claiming Q5 carries it are corrected below to point here instead). **Recommended: rule the audit-finding reading acceptable for slices 4 and 5**, on the basis stated, while naming it explicitly as the owner's call rather than assumed. M4's questions queue as **P-71**: main's last register note at `a9f671e` is P-67, and P-68, P-69 and P-70 exist only on `agent/syzygy-dov.17`, `agent/syzygy-dov.2` and `agent/syzygy-dov.3` respectively, so a reader following this packet's baseline to `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` finds none of the three [Observed: the register on main read this session; its last numbered row is P-53 and its text carries no P-6x row]. |

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine (heart-and-soul) | Yes, adopted: VIS-1…7, SEC-1…5 | VIS-1 (comprehension by simplifying presentation, never content), VIS-2 (no evidence means Unknown), VIS-4 (drafting is never adopting), VIS-5 (two write roots; Syzygy never writes code), plus the unnumbered "Not a documentation portal" paragraph at `.syzygy/governance/doctrine/vision.md` lines 61–64 and the success sentence at lines 234–236 |
| Decisions (legends-and-lore) | Yes | `THREE-SURFACE-POC-MODE-DIRECTION.md` (2026-08-29, the required demonstrations and the in-force invariants); `THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md` (2026-08-30, which lifts the eight-item and one-review caps for cycle work and fixes the trace rule); `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-02) and its 2026-09-05 continuation; P-52 (the eight-item cap question, superseded for cycle items by the 2026-08-30 direction and untouched here because M4 runs under `syzygy-dov.4`); the M1 ruling's sequencing sentence |
| Specification (openspec) | Yes, signed and digest-bound: `openspec/changes/three-surface-poc-experience/` and `openspec/changes/polaris-project-wide-butlers-model/` | POC-REQ-020 (client-rendered facts are the model's facts), POC-REQ-060 (one epistemic encoding), POC-REQ-061 (the accessibility floor); PWB-REQ-010 (Polaris opens with the whole project), PWB-REQ-011 (progressive reachability), PWB-REQ-014 (bounded, anchored, non-authoritative narrative claims), PWB-REQ-020 (parity), PWB-REQ-004 (the closed project-fact population no slice enters). **No requirement in either spec governs the home route or `model.surfaces`** — see Gate 5 |
| Topology (lay-and-land) | Candidate bundle only | Nothing beyond the core-versus-app placement already in force |
| Craft (craft-and-care) | Yes, owner-approved | CC-TEST-5/6 oracles, rule-6 mutation evidence, retained evidence, independent raw review |

## Gate 1 — Motif

**Problem.** The intent surface has no owner action on it and no route to the
one action that exists, and the Unknowns it renders most prominently are the
ones it routes least.

Three measurements say it, each with its denominator.

1. **Zero cross-surface deep links, over the four served pages — a fifth,
   unswept page already carries one.** Across the four served pages the
   non-fragment hrefs are, in every case, exactly the four global-nav links
   plus — on Polaris only — the exact-source routes: home 40 hrefs (36
   fragments + 4 nav), Trajectory 304 (300 + 4), Orrery 23 (19 + 4), Polaris
   1,089 (699 fragments + 386 `/polaris/source` routes + 4 nav) [Observed:
   an `href="…"` attribute sweep of the four captures, bucketed by prefix
   after stripping the query string; the three small pages are the
   pre-lane-A captures and the Polaris figure is the retained lane A
   tailnet capture]. **Widened to a fifth page (corrected per review 1,
   N7):** the retained exact-source capture (the owner's loopback-daemon
   capture, used again in measurement 2 below) was never censused for this
   motif claim. Swept this session: 6 hrefs, 1 fragment, 5 non-fragment —
   the four nav links plus
   `/polaris#polaris-source-openspec-specs-switchboard-identity-spec-md`, a
   non-fragment link into another page at a named anchor. Whether that
   counts as "cross-surface" is arguable (the exact-source route is a
   Polaris sub-route, so the link is Polaris → Polaris), but the product
   already contains one working instance of the deep-link-into-an-anchor
   mechanism slice 5 proposes — which strengthens slice 5's design rather
   than weakening the motif. The 2026-08-29 direction names cross-surface
   navigation among the things the experiment "must demonstrate"; what
   exists, over the population actually measured, is a four-item nav bar
   repeated five times plus the one anchor link just named.
2. **The only action in the product sits at 99.1% of the second page.**
   Across the five captured pages — home, Polaris, Trajectory, Orrery and one
   exact-source page (the last from the owner's loopback-daemon capture at an
   older evaluation, the only exact-source capture retained) — there is
   exactly one `<form>` and exactly one `<button type="submit">`, both inside
   `renderMaterializePanel`
   (`apps/three-surface-poc/src/materialize-action.ts` lines 55–81; the form
   at line 78 posts to `MATERIALIZE_HUMAN_PATH`, line 17). On the captured
   Trajectory page that panel begins at character 242,386 of 244,506 and runs
   2,120 characters to the end [Observed]. Polaris carries 0 forms and 1
   button, and that button is `type="button"` — the expand-declaration
   disclosure toggle; home, Orrery and the exact-source page carry 0 of each
   [Observed].
3. **Nine of twenty-two rendered Unknowns carry neither a closed reason nor
   a route.** See the table under "Measurements". The nine cluster between
   57.0% and 57.5% of the page — the entity list and the relationship list
   of "One capability in depth" — while the thirteen that *are* routed sit
   at 25.5%, 56.4–56.5%, 57.6%, 61.0% and then 95.7–98.7% [Observed].

**Who.** The owner, for whom the page is the day's first stop or is nothing
(`.syzygy/governance/doctrine/vision.md` lines 234–236: success is that the
observatory "displaces the README-and-ad-hoc-investigation ritual as the
owner's instinctive first stop"); and every agent reading `/api/poc` to
learn which gaps are its own work and which are the owner's, which today it
cannot do for nine of them
because their reason is a free-text English sentence outside every closed
vocabulary.

**Success, falsifiable.**

1. Every Unknown the POC renders on any surface carries a reason drawn from
   RFC2-24's closed twelve and a route, or renders the already-declared "No
   route declared" copy with its own stated reason. A sweep over the served
   pages reports **the denominator per surface** and zero exceptions on
   each — not one pooled figure (corrected per review 1, F5, and
   re-partitioned per review 2, G3: Trajectory and Orrery carry **299** and
   **9** rendered `epistemic-unknown` claim encodings — 301 and 11 raw,
   each figure including one stylesheet rule and one legend key item — and 0
   disclosure elements, a population the original single-denominator sweep
   could not see).
2. A reader who stops after the first reading knows what the project needs
   from them: the count of Unknown claims by reason and the route for each
   appears before the first catalog section, and each row links to the
   existing `#polaris-gap-<reason>` anchor.
3. `model.surfaces` states, for each surface, the population that surface
   actually renders, and a served-page test asserts declared count equals
   rendered population per surface with both denominators reported.
4. The home page answers, above the fold, which evaluation is current and as
   of when, what needs the owner, and which action is available now — with
   every row a deep link into the surface that owns it. With no prior
   evaluation the "what changed" region renders a named Unknown, never
   "nothing changed".
5. The materialize action has been run once end to end; the daemon stderr,
   the `TestArtifactRecord` and the before/after tuples for all five Unknown
   relationships are retained; and the record states plainly which edges
   narrowed and which did not and why.
6. No new epistemic vocabulary value exists anywhere in the implementation
   that RFC2-24, RFC2-25 or the POC's own declared encoding table does not
   already carry.

**Motif.** *A gap the owner cannot act on is a gap the page has not finished
rendering.* RFC2-24's own words for a condition outside the twelve are
"named, expandable, **routed to its resolving action**"; nine of Polaris's
twenty-two Unknowns are named and expandable and routed nowhere.

**What M4 is not.** It is not a proposal to make Syzygy dispatch work. Every
slice keeps dispatch human-triggered and keeps drafting separate from
adopting. **Slices 1–5 and 7 write nothing to the observed repository;
slice 6 does write there today (`bd -C <observed root> create`), and whether
that write is authorized is Q5's own question, not a settled property of
this packet's posture** (corrected per review 1, F4). It is not a re-opening
of the
page-size question, though it must state that question's arithmetic honestly
[Observed, computed 2026-09-14 against the M1 ruling's Q3 row and the lane A
measurement record
`docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`]: the page
at the retained capture is 1,484,487 bytes through the tailnet mount and
1,478,637 direct — 84,487 and 78,637 bytes **over** the M1
ruling's restated working target (its words are "1.4 MB"; the lane A record's
`q3Target.bytes` fixes it at 1,400,000 and that decimal figure is used here)
and 612,665 / 618,515 bytes under the 2,097,152-byte response ceiling. Of
that ceiling headroom the M1 ruling reserves 418–443 KB for the pending
Butlers P-60/P-61 repairs, read as 418,000–443,000 bytes on the same decimal
convention. Slice 1 adds a reason span and a route sentence to nine
disclosures and slice 3 adds an opening band; both are measured in hundreds
of bytes to low thousands [Inferred: a projection about unbuilt code, to be
replaced by the before/after measurement Gate 6 requires].

## Measurements on the retained capture

All computed this session. Polaris figures are from the lane A tailnet
capture (1,484,487 bytes; 1,481,819 decoded characters); home, Trajectory
and Orrery figures are from the pre-lane-A captures and are marked. Counts
are computed, never transcribed.

### Routes on the machine channel

| Measure | Value | Denominator |
|---|---|---|
| Objects carrying a `resolutionRoutes` field | 1,149 | the machine answer |
| …with an empty array | 1,137 | 1,149 |
| …with a non-empty array | 12 | 1,149 |
| Of the 1,137 empty, how many are `Unknown` | **0** | 1,137 |
| Of the 12 non-empty, how many are `Unknown` | **12** | 12 |
| Distinct non-empty route rows | 1: reason `excluded-content`, route "Policy change by the owner, or accept the exclusion" | 12 |
| `relationships` in the model | 9 | the machine answer |
| …labelled `Unknown` | 5 | 9 |
| …carrying a `resolutionRoutes` field at all | **0** | 9 |

Method: a recursive walk of the parsed JSON collecting every object with a
`resolutionRoutes` key, then a histogram of `epistemic.label` over that
population. The 1,149 decompose as 439 fact claims, 415 item claims, 278
source claims, 6 project-account claims, 9 class claims, the whole-shape
claim and the proposed-work current-authority claim. **The same eleven
figures hold, value for value, on the pre-lane-A machine capture** — a
different Butlers revision eight hours earlier — so they are facts about the
model's construction, not about the observed content [Observed: both
captures measured by the identical script].

This is the dossier's "1,137 of 1,149 route arrays empty" confirmed, and its
reading corrected. `routesFor`
(`packages/three-surface-poc-core/src/project-shape-model.ts` lines 150–154)
returns `[]` when the label is not `Unknown` and otherwise one route per
carried reason, taken from `UNKNOWN_REASON_ROUTES` (lines 89–102), whose
twelve keys the module's own test proves equal to cap1-core's
`UNKNOWN_REASONS`. So the empty array is the encoding of "this claim is
Observed", and the routeless Unknowns are somewhere else entirely: the nine
entity and relationship disclosures below, which carry no such field.

### Unknown disclosures on the rendered page

Every `data-unknown-disclosure` element on the retained capture, in document
order, with whether its own element contains a `data-unknown-reason` value
and the literal `Route:` [Observed; the predicate is "inside the same
element, from the opening tag to the first matching closing tag of the same
tag name"]. **Two offset conventions, both correct, named here per review
3, H6.** The "Offset" column below gives the position of the enclosing
element's opening angle bracket; Q1 and the review-2 disposition table give
the position of the `data-unknown-disclosure` attribute itself, 32 characters
later, so the same first and last disclosures read 378,599 and 1,462,590 here
and 378,631 and 1,462,622 there [Observed: both conventions re-derived this
session on the lane A tailnet capture; the delta is 32 at both ends, over all
22 elements]:

| Offset | Depth | Disclosure key | Closed reason | Route rendered |
|---|---|---|---|---|
| 378,599 | 25.5% | claim:class:roster-identity | `excluded-content` | yes |
| 836,380 | 56.4% | capability:whatsapp-transport-identity/doctrine | `missing-declaration` | yes |
| 837,314 | 56.5% | capability:whatsapp-transport-identity/non-goals | `missing-declaration` | yes |
| 844,800 | 57.0% | work:whatsapp-single-event-normalization | **none** | **no** |
| 845,421 | 57.1% | evidence:focused-pytest | **none** | **no** |
| 846,047 | 57.1% | runtime:live-satisfaction | **none** | **no** |
| 846,650 | 57.1% | region:unmapped-code | **none** | **no** |
| 850,888 | 57.4% | relationship:intent-to-work | **none** | **no** |
| 851,228 | 57.4% | relationship:work-to-code | **none** | **no** |
| 851,572 | 57.5% | relationship:code-to-evidence | **none** | **no** |
| 851,904 | 57.5% | relationship:code-to-runtime | **none** | **no** |
| 852,226 | 57.5% | relationship:capability-to-unmapped-region | **none** | **no** |
| 853,157 | 57.6% | claim:project-shape | `excluded-content` | yes |
| 903,530 | 61.0% | claim:source:about/lay-and-land/frontend.md | `excluded-content` | yes |
| 1,418,068 | 95.7% | claim:source:roster/chronicler/butler.toml | `excluded-content` | yes |
| 1,425,443 | 96.2% | claim:source:roster/education/butler.toml | `excluded-content` | yes |
| 1,432,759 | 96.7% | claim:source:roster/general/butler.toml | `excluded-content` | yes |
| 1,436,655 | 97.0% | claim:source:roster/health/butler.toml | `excluded-content` | yes |
| 1,443,938 | 97.4% | claim:source:roster/lifestyle/butler.toml | `excluded-content` | yes |
| 1,449,565 | 97.8% | claim:source:roster/qa/MANIFESTO.md | `excluded-content` | yes |
| 1,455,213 | 98.2% | claim:source:roster/relationship/butler.toml | `excluded-content` | yes |
| 1,462,590 | 98.7% | claim:source:roster/travel/butler.toml | `excluded-content` | yes |

Totals: **22 disclosures, 13 routed, 9 not** [Observed]. Separately, the
literal `Route:` occurs 18 times on the page and `data-unknown-reason="`
occurs 16 times — 14 `excluded-content` and 2 `missing-declaration` — the
difference from 13 being the gaps-list row and the per-cause sentences,
which carry the reason or the route outside a disclosure element [Observed:
both literals counted by `grep -F`-equivalent Python string count and by a
`re.finditer` sweep, agreeing].

**A note on the nine source-claim rows above.** They name observed-repository
paths in plain prose, uncoded (`check_governance.py`'s CG-1b bars backticked
Butlers paths only, so this passes mechanically); the evidence JSON
deliberately genericizes the same nine rows to "source claim, one excluded
source". Recorded here so a later reader does not mistake the two for
different measurements (added per review 1, E2).

### Where the actionable information sits

| Measure | Value | Denominator |
|---|---|---|
| `<h2>` sections on Polaris | 7 | the page |
| `<h3>` sections | 39 | the page |
| "Unknown, by reason" — its position | **6th `<h3>` of the 7th `<h2>`**, at character 1,474,935 | 10 `<h3>` under that `<h2>`; 1,481,819 characters |
| …its depth | **99.5%** | the page |
| `data-polaris-gaps` attributes | 1, value `"1"` | the page |
| `data-polaris-gap` rows inside it | 1, `id="polaris-gap-excluded-content"`, text "12 claim(s)" | the page |
| "One capability in depth" (`<h2>` 6) span | characters 811,016–852,703 = 41,687 | 1,481,819 (**2.8%**) |
| `<details>` elements | 359 | the page |
| `<form>` elements | 0 | the page |
| `<button>` elements | 1 | the page |

The gaps list's own anchor already exists and is already linked: `gapId`
(`apps/three-surface-poc/src/polaris.ts` line 136) mints
`polaris-gap-<reason>` and line 145 wraps a reason span in a link to it when
the reason is an active target. So slice 3's band needs no new anchor
scheme, only a second rendering of the same projection higher up.

### The home surface (pre-lane-A capture, renderer unchanged at `a9f671e`)

| Measure | Value | Denominator |
|---|---|---|
| Bytes | 38,706 | — |
| `href` occurrences | 40 | the page |
| …fragments | 36, over 10 distinct targets | 40 |
| …non-fragment | 4: home, Polaris, Trajectory, Orrery — the global nav | 40 |
| `<form>` / `<button>` / `<input>` | 0 / 0 / 0 | the page |
| `<h1>` | 1, the literal "One capability. Three honest views." | — |
| `<h2>` | 5: Polaris, Trajectory, Orrery, Exact entities, Exact relationships | — |
| The three surface panels, as characters | 6,438 (characters 7,632–14,070) | 38,682 decoded characters (**16.6%**) |
| The exact tables, as characters | 24,612 (character 14,070 to end) | 38,682 (**63.6%**) |
| `data-surface-entity` list items | 17 | — |
| `data-entity-id` / `data-relationship-id` | 9 / 9 | — |
| `epistemic-unknown` occurrences | 18 | — |

The seventeen panel items are the 4 + 4 + 9 of `model.surfaces`, and each
renders `<a href="#<entity id>">` — a fragment into the exact tables **on
the same page**, never a link into the surface the panel names
(`apps/three-surface-poc/src/routes.ts` lines 34–55). That is why the home
page's non-fragment href count is 4.

### The state of the return path

Identical in both machine captures [Observed]:

| Field | Value |
|---|---|
| `materializedBeadId` | `null` |
| `workerChange` | `{"kind":"unknown","reason":"no materialized work item to observe git activity against"}` |
| `testArtifactVerification` | `{"kind":"unknown","reason":"no observed changed-or-merged commit exists to bind test evidence against"}` |
| `walkthroughJudgment.evaluation.outcome` | `{"kind":"absent","what":"no-run-record","detail":"walkthrough execution record missing","criterion":"unknown-never-met"}` |

Audit finding **L5-F10**'s evidence list
(`docs/pursuits/2026-09-13-vision-pursuit-data.json`) reports this state as
`walkthroughJudgment.outcome`; the field is one level
deeper, at `walkthroughJudgment.evaluation.outcome`, and carries the same
four values [Observed]. (Corrected per review 1, N8: the shallower path is
L5-F10's, not the dossier's — `walkthroughJudgment` does not occur anywhere
in `docs/pursuits/2026-09-13-vision-pursuit.md`.)

### Source citations re-verified at `a9f671e`

The dossier's line numbers were taken at `f4589e2`. Every one below was
re-read at `a9f671e` this session; where lane A moved it, both are given.

| Citation | At `a9f671e` | Note |
|---|---|---|
| `packages/three-surface-poc-core/src/model.ts` `PocRelationship` | 80–88 | unchanged; the dossier's 80–88 holds |
| …`PocSurface` | 90–96 | unchanged |
| …`unknown()` helper | 305–307 | the free-prose constructor |
| …`workerChange` / `testArtifactVerification` computation | 418–423 / 431–437 | carried to the model at 701–702 |
| …the five Unknown relationships, by brace (corrected per review 1, N3 — one convention, stated) | 562–581, 582–590, 591–599, 600–608, 609–617 | whole five-block span 562–617; the dossier's "563–598" understates the end by nineteen lines, not one |
| …`surfaces` literal | **710–750**; the file ends at **752** (corrected per review 1, N4 — closes at 750, not 749) | the dossier's "710–756" overruns the file by four lines |
| …Orrery's derived id lists | **747–748** (corrected per review 1, N1 — not 745–746, which are `title:`/`question:`) | `entities.map` / `relationships.map` |
| `packages/three-surface-poc-core/src/project-shape-model.ts` `UNKNOWN_REASON_ROUTES` | 89–102 | the dossier's 89–102 holds |
| …`ResolutionRoute` | 115–118; used at 128 | the dossier's 115–128 spans both |
| …`routesFor` | 150–154 | the empty-array rule |
| `apps/three-surface-poc/src/materialize-action.ts` | 17, 55–81 (form at 78) | the dossier's 17 and 55–80 hold |
| `packages/three-surface-poc-core/src/materialization.ts` | 9–10, 43–65 | the dossier's 9–12 and 43–65 hold |
| `packages/three-surface-poc-core/src/owner-act-record.ts` | 1–18 header, 20–45 field types | the dossier's 1–45 holds |
| `packages/three-surface-poc-core/src/test-artifact-verification.ts` | 11–19, 73 | the dossier's 11–19 and 73 hold |
| `apps/three-surface-poc/src/capture-test-artifact.ts` | 3–7 | the dossier's 3–7 holds |
| `apps/three-surface-poc/src/routes.ts` | `surfacePanel` 34–55, `renderPocPage` 77–96 | the dossier's 34–96 and 33–55 hold |
| `apps/three-surface-poc/src/polaris.ts` `gapsList` | **933–948** (`gapReasonCounts` 922–931) | at `f4589e2` it was 916; lane A moved it +17, so the dossier's 916–931 no longer resolves |
| `apps/three-surface-poc/src/governance-inputs.ts` | 36–41, 48–52 | the dossier's 36–52 spans both |

## Gate 2 — Doctrine

Cited by identifier and quoted from the defined location, per verification
rule 8. VIS and RFC locations were resolved through `DIRECTIVE-REGISTER.md`
and then read; the register carries no spec-requirement family, so POC-REQ
and PWB-REQ clauses were located by heading sweep in their own spec files.

**VIS-1 — Comprehensible truth first; never comprehensible fiction**
(`.syzygy/governance/doctrine/vision.md`:82):

> Comprehension is achieved by simplifying *presentation*, never *content*:
> an honest view may aggregate, defer, or progressively disclose Unknowns,
> but may never substitute a confident state for an Unknown one. *Honest
> simplification:* collapsing forty Unknown-status modules into one region
> labeled "Unknown ×40."

The clause licenses slice 3 exactly: the opening band is an aggregate of
Unknowns with a count and a route, which is the clause's own worked example,
and it substitutes nothing.

**VIS-2 — No evidence means Unknown, not success**
(`.syzygy/governance/doctrine/vision.md`:96). Slice 6's expected result is
governed by it: two edges staying Unknown after a real run is the correct
output, and recording it as such is the requirement, not a failure to
report.

**VIS-4 — Humans steer the vision; agents shape within it**
(`.syzygy/governance/doctrine/vision.md`:122):

> Shape-defining deltas — heart-and-soul doctrine, craft-and-care standards,
> topology, and RFC acceptance — require owner sign-off, every time; Syzygy
> and its agents may draft them, never adopt them. … *Violation:* an agent
> sprouting specs inside an ambiguous vision; an agent certifying its own
> governing vision as unambiguous; an agent editing a spec to match code it
> just wrote; treating RFC acceptance alone as opening the gate.

**How each slice keeps it.** Slice 7's drafter emits a packet whose head
says `DRAFT, binds nothing`, never writes an `## Effect` or `## Ceremony`
section containing a performed phrase, never adds a row to
`ACCEPTANCE-ACT-RECORD.md`, and is invoked by an operator command rather
than by a request handler — the daemon writes no governance artifact on any
route. Slice 6 runs a human-triggered POST that a human clicks; nothing in
it is scheduled, polled or triggered by Syzygy. Slices 1–5 render and never
write. The deferred slice 8 pair are the only ones that would extend the
effect at all, and both are held behind their own act.

**VIS-5 — Syzygy never writes code; direct writes are confined to two
namespaces** (`.syzygy/governance/doctrine/vision.md`:141):

> Syzygy's **direct project-content writes** touch only `openspec/**` … and
> `.syzygy/**` … Syzygy may *read* declared implementation and evidence
> sources anywhere; it may never directly create, modify, move, or delete
> project content outside its two roots. Effects on every other authority —
> version-control metadata such as commits and tags, configured
> work-scheduler state, CI, runtime systems — occur only through **typed,
> explicitly authorized adapters**, governed by each authority's own
> contract.

**Whether the materialize action is lawful under this clause is contested,
not settled here** (corrected per review 1, F4): the registry entry quoted
below is the *project-shape observer* (`authorityType: "version-control"`,
`readAuthority` describing phase A/B reads only) and declares nothing about
a work-scheduler adapter, so it is the wrong instrument to cite for either
side of the question — it neither authorizes nor forbids the materialize
mechanism, and what VIS-5 requires is that the
work-scheduler effect occur "only through **typed, explicitly authorized
adapters**, governed by each authority's own contract". The materialize
mechanism *is* one such adapter in code; what is contested is whether any act
authorizes it, which is exactly Q5. **Superseded 2026-09-15 (review 2, G8):**
this sentence read "the two 'typed, explicitly authorized adapters' VIS-5
requires are the mode direction (for the mechanism's original authorization)
and, if the owner needs one, a continuation naming the effect" — but an owner
direction is the authorization *for* an adapter, never an adapter itself, and
VIS-5 names no number of adapters at all; the "two" in this paragraph's own
heading is two write *namespaces*, `openspec/**` and `.syzygy/**`, a different
pair entirely. The registry
entry's five values, quoted accurately regardless: `writeSurface: []`,
`databaseAccess: []`, `networkAccess: []`, `executeObservedCode: false` and
`workingTreeRead: false` [Observed: the `typedAuthority` block of
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`,
whose top-level `status` field (a governance lifecycle marker) reads
`candidate-amendment-no-effect-until-owner-act`
— the entry's own effectiveness rests on a separate act, not stated here].
Q5 puts the materialize question to the owner directly; see its two
readings there. Q3 exists on the same footing: a drafted act file is a
write, and the only root it could lawfully land in is Syzygy's own.

**The escape property** is not a numbered clause. It is the unnumbered
is/is-not paragraph at `.syzygy/governance/doctrine/vision.md` lines 61–64,
in the adopted doctrine file, quoted in full:

> **Not a documentation portal.** Rendering and drafting governance
> artifacts is a means; the escape property is that intent changes produce
> dispatched work. A Syzygy from which no work is ever dispatched has
> failed, regardless of how good its documents look.

Because it carries no VIS identifier, `DIRECTIVE-REGISTER.md` does not index
it and it cannot be cited as `VIS-n`; it is adopted doctrine prose and is
cited here by file and line [Observed: a `grep -F` for the literal
"documentation portal" across `.syzygy/governance/` returns **11 hits over 8
files** — the doctrine file once, RFC-0007's README and its candidate mirror
once each, one retired revision once, two round-review files three times
between them, and the two 2026-08-18 launch-gate administration records,
JSON and Markdown, twice each. The doctrine file is the definition; the
other seven are citers, and two of them are near-miss administrations that
tested the vision against exactly this phrase].

**Supporting clauses, quoted at their defined locations.**

- **RFC2-24 — Twelve reasons, closed**, at line 92 of
  `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`:
  "Every Unknown claim instance carries exactly one primary reason from this
  list (secondary reasons may annotate); the list changes only by amendment
  to this RFC …" (elided: ", and covers Unknown states only —" and the three
  sibling surface states). And, in the next paragraph (corrected per review
  1, N12 — not "three paragraphs on"): "A condition genuinely not among
  the twelve is disclosed as a **fact of the render** — named, expandable,
  routed to its resolving action — never dressed as a reason; the honest
  move is to amend this list, never to annotate outside it." **The clause's
  own table and `UNKNOWN_REASON_ROUTES` are NOT word for word equal**
  (corrected per review 1, F1 — the draft's claim here was false and is
  slice 1's most consequential defect). Extracted and compared key by key
  this session: of the twelve, **5 are identical**
  (`stale-beyond-currency-bound`,
  `unconsented-source-or-provider`, `excluded-content`,
  `contradicted-pending-adjudication`, `reference-unresolvable`) and **7
  differ** — `missing-declaration` (RFC adds "(v1.md)"), `missing-evidence`
  ("Produce/capture" vs "Produce or capture"), `no-currency-bound-declared`
  (RFC adds "[Observed — trust-and-evidence.md]"), `mapping-coverage-absent`
  ("Run/declare" vs "Run or declare"), `challenge-suspended` (RFC adds
  "(RFC2-13)"), `source-uncaptured-or-unreachable` ("observer/source" vs
  "observer or source"), and `execution-blocked` (RFC adds the parenthetical
  "(execution profile, consent, environment)"). Every difference is the
  RFC's prose gaining a citation or connective the implementation's short
  phrase drops — no route names a different resolving action — but the
  values are not verbatim equal, and RFC6-14 requires the machine answer to
  carry the reason **verbatim from the vocabulary**. Slice 1 renders its
  route strings from `UNKNOWN_REASON_ROUTES` — the table the page already
  renders — not from the RFC's own wording; see the corrected mapping table
  below. So the route vocabulary M4 wants to extend to nine more disclosures
  already exists, is already closed, and is already implemented, using the
  implementation's spellings; slice 1 is a widening of *coverage*, not of
  vocabulary or of spelling. Whether a `PocRelationship` is an "Unknown
  claim instance" in the clause's sense is the one thing this packet does
  not decide [Unknown]: the clause says "claim", the POC's relationships are
  typed `PocRelationship` and not `ProjectShapeClaim`, and no clause this
  packet found settles it. Slice 1 therefore rests on POC-REQ-060, which
  reaches every epistemic encoding on the three surfaces whatever the object
  is called, and cites RFC2-24 for the vocabulary it borrows.
- **RFC2-25 — Six tiers, closed** (same file, line 153) and **RFC2-23 —
  Six degradation states, closed** (line 70) are named here only to record
  that no slice adds a member to either [Observed: no slice below assigns a
  tier or a degradation state].
- **RFC2-9**, at line 187 of
  `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`,
  and **RFC2-10** (line 209) govern currency and freshness. **No M4 slice
  touches either**; they are M2's subject, and they are named here so a
  reviewer can see the boundary: slice 1 adds a reason and a route to a
  disclosure and assigns no freshness value.

**Conflict check.** None found [Inferred, labelled per review 3, H9:
checked slice by slice against all eight slice rows above; denominator 8].
Every slice adds a disclosure or a route, or
removes a hand-written list in favour of a derived one. None turns anything
green, none folds an Unknown into a total, none establishes a claim, and
slice 6's honest expected outcome is that two claims stay Unknown.

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Routes on every Unknown | `packages/three-surface-poc-core/src/model.ts` (a reason-and-route field on `PocEpistemic`'s Unknown arm, populated from a closed table beside the entity and relationship literals); `apps/three-surface-poc/src/polaris.ts` (render through the existing `unknownLine` shape); `apps/three-surface-poc/src/orrery.ts` and `apps/three-surface-poc/src/trajectory.ts` (the same encoding, POC-REQ-060); `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` (the denominator grows) | none |
| 2 The machine form of a route | `packages/three-surface-poc-core/src/project-shape-model.ts` (widen `ResolutionRoute`, keep `route` verbatim as the prose field); `packages/three-surface-poc-core/src/model.ts` (the same type on the relationship arm) | none |
| 3 The opening band | `apps/three-surface-poc/src/polaris.ts` (a second rendering of `gapReasonCounts`, reusing `gapId`), `apps/three-surface-poc/src/polaris-copy.ts` (the band's own copy rows) | none |
| 4 `model.surfaces` true by construction | `packages/three-surface-poc-core/src/model.ts` lines 90–96 and 710–750; each renderer imports its descriptor | none |
| 5 Home as the day-opening | `apps/three-surface-poc/src/routes.ts` lines 34–96, `apps/three-surface-poc/src/exact-tables.ts`, `apps/three-surface-poc/src/routes.test.ts` — **and these are exactly where the fourth Unknown encoding lives** (recorded per review 3, H1): the `provenance-none` span at `exact-tables.ts` line 10 and its only style rule at `routes.ts` line 73, inside `HOME_STYLE` (declared line 57, used at line 90 only). Slice 5 must not rewrite either without closing that encoding, and Q1's re-specified shared marker is what closes it | none |
| 6 Run the return path once | no source file; `docs/evidence/` gains one record | none |
| 7 Drafted-act generator | a new pure module in `packages/three-surface-poc-core/src/`; an operator entry point beside `apps/three-surface-poc/src/capture-test-artifact-main.ts`; `scripts/check_governance.py` registration | **potentially `.syzygy/governance/decisions/`** — the output, see Q3 |
| 8 (deferred) Packet per claim; the queue | `packages/three-surface-poc-core/src/materialization.ts` lines 9–65 | none directly; the effect is new |

Boundaries crossed: none new [Inferred, labelled per review 3, H9: checked
against all eight slice rows above; denominator 8]. Slice 1's route table
sits beside the
relationship and entity literals in the same module that already constructs
them; slice 2 widens a type `packages/three-surface-poc-core` already owns.
Slice 7 is the only slice that would give the core package a filesystem
dependency, and the design keeps it pure precisely so it does not.

Not touched by any slice [Inferred, labelled per review 3, H9: checked
against all eight slice rows above; denominator 8]: the body-read authority
gate, the observation
pipeline's classification, extraction and coverage stages, the registry's
`resourceLimits` and `typedAuthority` values, the response ceilings, the
consent act's pair and content class, the signed PWB specification text and
the signed POC specification text.

### The authorizing act, per slice

| Slice | Owner act needed | Named act, and the trigger test |
|---|---|---|
| 1 Routes on every Unknown | **No** | Rides `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` (2026-09-05). No escalation trigger of `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` ("Escalation triggers", lines 86–94) is crossed: no doctrine or contract change, no PWB spec amendment, no security/privacy/retention change, no registry-envelope change, no observation at all — the slice reads nothing new and renders a value the model already holds. It traces to POC-REQ-060 under the 2026-08-30 direction's trace rule |
| 2 Machine route form | **No** | Same continuation. It adds fields to a payload no act binds. If a reviewer reads a route as a "disclosure Polaris presents" under PWB-REQ-020 — this packet's own reading is that it is, see Gate 5 — the slice must render it in both channels, which it does; that is conformance, not amendment |
| 3 Opening band | **No** | Same continuation. PWB-REQ-010's opening order is preserved by placing the band after the project account and before the first catalog, and the existing outline oracle asserts it |
| 4 `model.surfaces` | **No** | Same continuation. **No requirement governs this field** (Gate 5), so it traces to the recorded-finding arm of the 2026-08-30 direction, naming L6-F5. **This reading is this packet's own [Inferred] argument, not something any question puts to the owner as drafted; Q7 now carries it explicitly** (corrected per review 1, F6) |
| 5 Home as day-opening | **No** | Same continuation, on the same recorded-finding arm naming L6-F1. **Q7, not Q5, carries this reading** (corrected per review 1, F6 — Q5 asks only about slice 6's run) |
| 6 Run the return path once | **Contested — see Q5** | `.syzygy/governance/decisions/THREE-SURFACE-POC-MODE-DIRECTION.md` lines 18–22 name the demonstration; the same file's invariant list (lines 26–32) keeps dispatch human-triggered; `THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md` lifts the item and review caps for cycle work. The run adds no mechanism and reads no new source, but it writes to the observed repository's Beads database via `bd -C <observed root> create` — **not** merely "through the adapter the 2026-09-02 act's own prohibition list already contemplates," which reads as a general prohibition on exactly that write (corrected per review 1, F4). Q5 puts both readings to the owner rather than assuming either |
| 7 Drafted-act generator | **Yes, on arm (a) — none on arm (b)** | **No act found** that authorizes Syzygy to write a governance artifact about the observed project into its own decisions directory. The hook is the 2026-09-02 act's "any scope beyond the signed change". Arm (b) — a pure drafter returning packet data, with no file written — crosses no trigger and rides the continuation |
| 8 Packet per claim; the queue | **Yes, both** | Each needs an owner act naming the effect, the claim classes eligible and the ceiling. L5-M5's own text warns that RFC-0010's propose-only shape (RFC10-7) is Wave D1 and that `DEFERRED-WAVE-POSTURE.md` forbids offering a C/D wave act while the posture stands, so the act must be narrow and may cite RFC10-7 only as design precedent. Not designed here |
| A poller, watcher or scheduler, had one been proposed | **None found** | and none is proposed. Every action in M4 is clicked by a human or typed by an operator |

P-52 is untouched: all slices run under `syzygy-dov.4`, the pursuit bead, so
no ninth POC bead is filed. The 2026-08-30 improvement-cycles direction lifts
the eight-item cap for cycle items in any case; this packet neither relies on
that lifting nor disputes P-52's row.

## Gate 4 — Design sketch, per slice

### Slice 1 — A reason and a route on every Unknown (medium; no act)

The nine routeless disclosures get the treatment the thirteen already have.
`PocEpistemic`'s Unknown arm (`packages/three-surface-poc-core/src/model.ts`
line 305's constructor) gains two fields beside its free-prose `reason`: the
closed RFC2-24 reason, and the route. The prose stays and becomes the
*basis* sentence — nothing the page says today is deleted.

The mapping, proposed, one row per disclosure, each reason taken from
RFC2-24's twelve and each route taken **verbatim from
`UNKNOWN_REASON_ROUTES`**
(`packages/three-surface-poc-core/src/project-shape-model.ts` lines 89–102)
— the table the page already renders through `routesFor` —
**not from RFC2-24's own prose**, which differs from the implementation on
7 of 12 route strings (Gate 2, corrected per review 1, F1). Rendering the
RFC's wording here while the existing thirteen disclosures render
`UNKNOWN_REASON_ROUTES`'s wording would put two different route sentences
for the same reason on one page, which is POC-REQ-060's own falsifier — the
exact defect Q1 asks the owner to rule a non-conformance:

| Disclosure | Proposed reason | Route (`UNKNOWN_REASON_ROUTES`, verbatim) |
|---|---|---|
| work:whatsapp-single-event-normalization | `missing-evidence` | Produce or capture evidence |
| evidence:focused-pytest | `missing-evidence` | Produce or capture evidence |
| runtime:live-satisfaction | `missing-evidence` | Produce or capture evidence |
| region:unmapped-code | `mapping-coverage-absent` | Run or declare the mapping |
| relationship:intent-to-work | `missing-evidence` | Produce or capture evidence |
| relationship:work-to-code | `missing-evidence` | Produce or capture evidence |
| relationship:code-to-evidence | `missing-evidence` | Produce or capture evidence |
| relationship:code-to-runtime | `missing-evidence` | Produce or capture evidence |
| relationship:capability-to-unmapped-region | `mapping-coverage-absent` | Run or declare the mapping |

If the owner instead wants the page to render RFC2-24's own prose, that is a
separate change touching all twelve existing route strings as well as these
nine, and must be proposed as one change, not mixed with slice 1.

Seven of the nine land on one reason, which is honest and unhelpful on its
own; the *action* route is what makes them different, and that is the second
half of the slice. Beside the closed route, `relationship:intent-to-work`
gains an `actionRoute` naming the materialize panel — the one lawful action
that exists — rendered mount-prefix-aware through
`withMountPrefix` (`apps/three-surface-poc/src/tailnet.ts`). Following the
link writes nothing: the panel is the read-only exact preview
(`apps/three-surface-poc/src/materialize-action.ts` lines 55–81, whose own
copy says "Nothing is written until the button below is explicitly clicked;
Syzygy never triggers this on its own"). The other eight carry no
`actionRoute`, because no route inside the POC leads anywhere for them; the
closed route sentence is what they get, and the band in slice 3 counts them.

**The same encoding on all three surfaces.** POC-REQ-060's scenario is
"WHEN the same Unknown relationship appears on Polaris, Trajectory, and
Orrery, THEN all three render it with the declared Unknown encoding from the
shared token set". The five Unknown relationships appear on Orrery
(`relationshipIds` of the Orrery surface include all nine) and three of them
on Trajectory, so slice 1 lands in three renderers or in none.

**Tests, restated per surface (corrected per review 1, F5).** The sweep as
originally specified — every `data-unknown-disclosure` element carries a
`data-unknown-reason` — has denominator **22 on Polaris and 0 on Trajectory
and Orrery**, because those two surfaces never emit a
disclosure wrapper at all. **Superseded 2026-09-15 (review 3, H1):** this
read "because those two surfaces render **every Unknown** through the bare
`epistemic-unknown` class alone". The predicate actually run counts
occurrences of one class literal, not those surfaces' rendered Unknown
population: **299** and **9** rendered `epistemic-unknown` claim encodings,
from 301 and 11 raw occurrences less one stylesheet rule and one legend key
item each (measured this session, re-partitioned per review 2, G3) — **plus a
fourth family the two-literal census never reached**, the `provenance-none`
span of `apps/three-surface-poc/src/exact-tables.ts` line 10, at **9**
rendered occurrences on Orrery and **0** on Polaris and Trajectory
[predicate: literal occurrences of the string `provenance-none`; denominator:
the whole served page; each occurrence assigned to its enclosing tag]. A
sweep with a zero denominator on two of three surfaces passes vacuously
there and cannot discharge POC-REQ-060's three-surface invariant. Slice 1
must therefore also make Trajectory and Orrery emit the same
`data-unknown-disclosure`/`data-unknown-reason` marker pair Polaris does
(the shared five relationships already appear on both), after which the
sweep's denominator is reported **per surface** — Polaris's 22, plus
Trajectory's and Orrery's own disclosure counts once the slice lands — and
zero exceptions is asserted against each denominator separately, never
pooled into one figure. **The re-specified shared marker must cover the
`provenance-none` rendering as well** (added per review 3, H1): its nine
Orrery spans encode exactly the nine Unknowns this slice is about, so a sweep
blind to them passes on every published denominator while POC-REQ-060's
falsifier still stands. Rule-6 mutants: blank one disclosure's reason on
each surface and confirm that surface's sweep fails; change one reason to a
thirteenth value and confirm it fails; **re-emit one `provenance-none` span
in place of the shared marker on an Orrery row and confirm the cross-surface
sweep fails** (review 3, H1); delete the `actionRoute` and confirm
the capability-detail test fails.

### Slice 2 — The machine form of a route (medium; no act)

`ResolutionRoute` becomes
`{ reason, prose, actor, verb, target }`, where `prose` carries today's
string **verbatim** so no rendered sentence changes, `actor` is one of
`owner | operator | agent`, `verb` is a short closed set, and `target` names
what the action is aimed at (an artifact path, an act identity, a policy, an
evaluation, or external work). The same type goes on the relationship arm,
so one widened type serves slice 1 and slice 2 — L5-M4's own note that the
two moves should build the type once, not twice.

**What the slice does not do, per Q2 (corrected per review 1, F2).** It does
not add a `none-modelled` value. It makes the empty array unrepresentable on
an Unknown **that carries `reasons`** — narrower than "an Unknown" at large,
because cap1-core's `EpistemicState`
(`packages/cap1-core/src/epistemic.ts:50-67`) also has a third arm,
`{ label: 'Unknown', basis: 'deferred' }`, with no
`reasons` field; the type-level prohibition must not make that modelled arm
unrepresentable. It leaves the empty array as the only legal value on an
Observed claim, and leaves `label.no-route` and its sibling `label.deferred`
(`polaris-copy.ts:192-193`, both listed in `UNREACHED_IN_FIXTURES` at
`polaris-copy.test.ts:297,299`) where they are, rendering either routeless
Unknown arm's fallback. If the owner rules the other way on Q2 and mints
`none-modelled`, both `UNREACHED_IN_FIXTURES` entries must be reconciled in
the same change, or the oracle will assert one or both rows are still
unreachable and fail.

**Parity.** Every route the page renders must be in the machine answer under
the same claim or relationship id. PWB-REQ-020's enumerated population
includes "disclosure Polaris presents", and a rendered route is one, so the
sweep's `unknown-disclosure` and `unknown-relationships` families
(`apps/three-surface-poc/src/polaris-parity-sweep.test.ts` lines 431–452)
grow a route family beside them [Inferred: this packet's reading of the
enumeration; if a reviewer reads a route as outside the enumerated
population, the slice's parity obligation narrows and nothing else changes].
Per the project's own rule, the check is per tuple against the machine claim
by id and over both id sets — never `tuples === distinct ids`.

**Where that obligation comes from (stated per review 3, H4).**
PWB-REQ-020's own **Mutation proof** bullet is the source of slice 2's
per-class injection duty — not this project's general practice — and it is
the bullet elided from the quotation in Gate 5 above. At
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
lines 920–923, quoted verbatim: "for each fact, authority-state,
judgment-state and disclosure marker class, independently inject a missing,
duplicated, changed, collapsed and wrong-evaluation marker and confirm the
comparator fails before restoration; report both channel denominators for
every run." Slice 2 adds a new disclosure marker class and therefore inherits
that clause directly; Gate 6 item 3 (rule-6 mutants per guard branch) and
item 4 (both denominators) are how it is discharged.

### Slice 3 — The opening band (medium; no act)

A band placed after the project account and before the first catalog
section, rendering the same `gapReasonCounts` projection the gaps section
already renders, every row linking to the existing `#polaris-gap-<reason>`
anchor and carrying the reason's route. On the retained capture that band
would have one row — `excluded-content`, 12 claims, "Policy change by the
owner, or accept the exclusion" — and, after slice 1, rows for the
relationship and entity Unknowns beside it, with the materialize link on
the one that has it.

**One count, two renderings, one denominator.** The band must not be a
second projection that can drift: it takes the same map and the same
ordering function, and a test asserts the band's total equals the gaps
section's total on every fixture. A counterexample fixture whose only
Unknown reason is `source-uncaptured-or-unreachable` must render that reason
in the band too, under Q4's recommended arm, and must render it *last*.

**Byte cost.** The band is the gaps list rendered twice, plus a heading and
a lede. On the retained capture the whole gaps `<ul>` is roughly 2 KB
including the per-cause sentences; the band would carry the generic routes
without the per-cause expansion, so low single-digit KB [Inferred; Gate 6
requires the measured figure before and after].

**PWB-REQ-010 and PWB-REQ-011 hold.** The band displaces no category and
adds no reading: PWB-REQ-011's promise is that a reader who stops after the
first reading is left with a true coarser account, and a count of Unknowns
by reason is coarser and true. The existing outline oracle asserts the
heading order is unchanged.

### Slice 4 — `model.surfaces` true by construction (medium; no act)

`PocSurface` gains a `renders` block: the route, the question, the state
(`desired | execution | observed`), the content root the surface projects,
and the count and denominator it renders. Each of the four renderers imports
its own descriptor for its eyebrow, question and denominator. Polaris's and
Trajectory's hand-written `entityIds` lists are derived from the same source
the renderers read, the way Orrery's already are
(`packages/three-surface-poc-core/src/model.ts` lines 747–748, corrected
per review 1, N1). A served-page
test asserts, per surface, that the declared count equals the rendered
population, reporting both denominators.

Keep both shapes for one commit, old derived from new, then delete the
hand-written lists once no renderer reads them.

### Slice 5 — Home as the day-opening (medium; no act)

`renderPocPage` (`apps/three-surface-poc/src/routes.ts` lines 77–96) stops
being an index of the three surfaces. It answers four questions, each row a
deep link into the surface that owns it: which evaluation is current and as
of when; what needs the owner (slice 3's band, same projection, third
rendering, same total); which action is available right now (the materialize
panel's status and a link to it — never the form itself, which stays on
Trajectory where the exact preview is); and, when a previous evaluation
exists, what changed since it.

**The two literals go.** The `<h1>` "One capability. Three honest views."
and the `lede` derived from `model.capabilityId` both describe a product
whose Polaris page now answers a different question entirely; they are
replaced by the descriptor's own question from slice 4.

**The exact tables stay**, one level down, as the no-script and parity
backstop. `apps/three-surface-poc/src/routes.test.ts` lines 188–243 already
sweeps the home page for entity-id and relationship-id set equality against
the model, asserts every fragment href resolves to a rendered id, and
compares `visibleParityTuples(html)` to `parityTuples(wireModel)`; the
sweep's denominator grows rather than forking, and the fragment-resolution
assertion is what keeps VIS-7's "every rendered internal link resolves"
true as rows become deep links.

**Counterexample.** With no prior evaluation the "what changed" region
renders a named Unknown with its reason and route, never "nothing changed".
That is the slice's rule-6 mutant: make it render an empty diff and confirm
the test fails.

**Depends on slices 3 and 4.** The home page should hold no truth of its
own; it is their composition.

### Slice 6 — Run the return path once (medium; no new act; Q5 confirms)

Run the built chain on the one seam it was designed for: a human clicks
materialize on Trajectory; a human-launched agent does the bounded work on
`WORKER_CHANGE_SEAM`; an operator runs the capture step
(`apps/three-surface-poc/src/capture-test-artifact.ts`, whose own comment at
lines 3–7 records that `main.ts` never imports it, so SEC-3 holds); the next
evaluation is taken.

**What the run is expected to produce, stated before it runs.**

| Signal | Before | Expected after | Why |
|---|---|---|---|
| `materializedBeadId` | `null` | the Bead id | `resolveMaterializationEpistemic` confirms the id against live-observed work items, never from the record file alone |
| `relationship:intent-to-work` | Unknown | **Observed** | `model.ts` line 570 is conditional on `materialization.beadId` |
| `workerChange` | `kind: unknown` | `kind: observed` | `observeWorkerChange` at lines 418–423 takes the bead id and the seam |
| `testArtifactVerification` | `kind: unknown` | a verified or failed record | lines 431–437 bind it to the observed commit |
| `relationship:work-to-code` | Unknown | **Unknown** | line 588 is an unconditional literal; no input reaches it, deliberately |
| `relationship:code-to-evidence` | Unknown | **Unknown** | line 597, same |
| `walkthroughJudgment…criterion` | `unknown-never-met` | unchanged by this run | it is the cold-open walkthrough, a different artifact |

The last two rows are the point. The dossier's M4 **"What" bullet** (not its
"Why" bullet — corrected per review 1, N6) expects three edges to narrow;
the code says one will, and says why in its own comments at `model.ts`
lines 26–42 (comment 26–29, const 30–33 for the seam; comment 35–41, const
42 for its intent — corrected per review 1, N2): the worker-change seam and
its intent are deliberately distinct from the identity-resolution graph, and
wiring one into the other is the false-`Verified` change AGENTS.md records
as already reverted once. The honest-reporting caveat this measurement
leans on is not new to this packet — it is already recorded in both the
dossier's own slice-6 bullet ("report honestly if an edge stays Unknown")
and L5-M7's slice plan ("Report honestly if an edge stays Unknown: that is
the measurement, not a failure") — what this packet adds is the specific
measurement of *which* edges and *why*, confirmed by an identifier sweep
this session with zero overlap between the worker-change/test-artifact
identifiers and the relationships array (corrected per review 1, N6, which
found the earlier framing implied the caveat itself was new). **The honest
result of the run is therefore a record that one edge narrowed, two did
not, and the two that did not are correctly scoped elsewhere** — which is
itself the strongest available evidence that the model does not manufacture
propagation. Q5 asks the owner to rule that this counts as the
demonstration before the run, not after.

**What is retained.** The daemon stderr (the fresh-checkout verdict requires
it empty), the `TestArtifactRecord`, the before/after machine captures, and
the before/after tuple for all five Unknown relationships. Per v1.md lines
119–120 (corrected per review 1, N13) the V0 agent-consumption artifact is
"the named workflows and the commits/sessions that used them", and the
criterion at lines 118–119 says "a workflow written
solely to satisfy this criterion does not count" — so the work must be a
real tracked task, not a demonstration written for the run.

**This slice builds nothing.** If any step needs a code change to complete,
that is a finding and the slice stops and reports it.

### Slice 7 — A drafted owner act, never performed (large; act on arm (a))

A pure function in `packages/three-surface-poc-core/src/` taking (a set of
claims sharing one reason, the target authority artifact, the act type) and
returning the packet as **data**: subject, the exact ceremony phrase the
owner would write, the frozen digest of the artifact the act would bind, and
the enumerated claim ids whose epistemic state the act would change and to
what. No filesystem in the pure layer. The inverse of
`packages/three-surface-poc-core/src/owner-act-record.ts`, whose parser
already turns an act record into typed fields and whose own header says it
"owns NO notion of validity" — the drafter owns none either.

**On arm (b), that is the whole slice** and it needs no act: the packet is
returned on request and printed by an operator command, and nothing is
written.

**On arm (a),** an operator command writes it into
`.syzygy/governance/decisions/` with a `DRAFT, binds nothing` head, and
three things must happen in the same change or CG-7d cannot see the packet
go stale: the phrase is registered in `scripts/check_governance.py`'s
`_act_subjects()`, its packet copies are registered in
`ACT_DIGEST_COPY_FILES` from an existence-gated activation function, and a
counterexample test asserts that a drafted packet carrying an accepted or
performed banner makes `check_governance.py` fail.

**Neither arm of slice 7 itself writes toward the observed repository** —
this sentence is about slice 7's drafter only, and does not extend to slice
6's existing materialize mechanism, whose own write is Q5's question
(corrected per review 1, F4, which found the draft's parallel sentences
read as a property of the whole packet). The registry entry cited for
slice 7 is the project-shape observer, not a work-scheduler adapter (see
Gate 2, VIS-5 and N10); its write surface is empty and stays empty for
*this* slice regardless of how Q5 resolves.

### Slice 8 — Deferred: the packet per claim and the queue (large; acts)

Named here so the funnel is complete, and not designed. L2-M4 would replace
`buildMaterializationPacket`'s hard-coded title, description, `externalRef`
and `governingIntent`
(`packages/three-surface-poc-core/src/materialization.ts` lines 43–65) with
a function of a selected claim; note that
`MaterializationGoverningIntent.requirementId` is a **literal type** at line
15, so the change widens a type, not just a value, and the frozen fixture
for the existing target must stay byte-identical so the current
demonstration's evidence survives. L5-M5 would generalize that into an
append-only queue with a released/unreleased state. Both are held behind
their own owner acts, and this packet recommends they stay held until slices
1–6 have run and the return path has produced its one real record — because
a queue of packets aimed at claims is worth much less before anyone knows
what one packet's round trip actually produces.

### Design bar for the human surface

No new interaction beyond one band, one set of deep links and one link to an
existing panel. PWB-REQ-016 comprehension without vision or a pointing
device holds: every route and every band row is text in reading order, never
colour. POC-REQ-061's floor holds: no fragment target moves inside a
`<details>` (the project's own recorded trap), keyboard paths stay complete,
direct and tailnet forms stay at parity, and the no-JS path stays complete.
Every new copy string is distinctive enough that a substring oracle cannot
match it by coincidence — the recorded `None` failure.

## Gate 5 — Specification

**Slices 1, 2, 3 and 6: no spec delta. Each is conformance with text that
already binds.**

Slice 1 is POC-REQ-060 conformance. The requirement is quoted verbatim from
`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`
lines 927–946 (range corrected per review 3, H4 from "lines 927–945", which
stopped one line short of the falsifier's second limb), with one elision
marked:

> The three surfaces SHALL draw from one declared set of design tokens, and
> SHALL encode epistemic states (Observed, Unknown, and their reasons)
> identically wherever they appear. Scope of quantification: every epistemic
> encoding across the three surfaces.
>
> - **Case (sweep)**: a checker enumerates every epistemic encoding on all
>   three surfaces — the denominator is that population — and compares each
>   against the declared token/encoding table.
> - **Observable**: identical states render with identical declared
>   encodings on every surface.
>
> *… elided here (marked per review 3, H4): **Oracle** at lines 941–942 —
> per-encoding equality with the declared table over the exhausted
> population, the table being a checked-in declaration — and **Oracle
> independence** at 943–944, the declared table as the expected value against
> a sweep that reads served output …*
>
> - **Falsifier**: one surface encoding Unknown (or Observed) differently
>   from the declared table, or a surface styling epistemic state ad hoc.

Nine disclosures encoding Unknown as bare prose while thirteen encode it as
a reason span plus a route is one surface encoding Unknown two ways, which
is the falsifier's first limb. Widened per review 1 (F5): Trajectory and
Orrery encode the same five relationships a *third* way, through the bare
`epistemic-unknown` class with no disclosure wrapper at all (**299** and
**9** rendered claim encodings, from 301 and 11 raw occurrences less one
stylesheet rule and one legend key item each — re-partitioned per review 2,
G3) — a second instance of the same falsifier, over
the requirement's full three-surface scope of quantification. A **third**
instance, added per review 3, H1: the `provenance-none` span
(`apps/three-surface-poc/src/exact-tables.ts` line 10) encodes the same nine
Orrery objects a fourth way, under a class the declared token table
(`apps/three-surface-poc/src/design-tokens.ts` line 25) does not carry, and
with its only style rule (`apps/three-surface-poc/src/routes.ts` line 73)
reaching the home route alone — so one epistemic assertion renders with the
declared Unknown colour on one served page and with no declared encoding on
another [Observed, this session: 9 rendered spans and 0 style occurrences on
the retained Orrery capture, 9 spans plus 1 rule on home, 0 on Polaris and
Trajectory]. The spec
already requires the repair, on all three surfaces.

Slice 2 is POC-REQ-020 and PWB-REQ-020 conformance. PWB-REQ-020 is quoted
verbatim from
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
lines 902–926, with one elision marked (per review 3, H4):

> Every project-shape identity, statement, source anchor, coverage state,
> denominator, contradiction, body-read authority state and
> walkthrough-judgment state or disclosure Polaris presents SHALL be
> recoverable from the same evaluation in the machine answer, preserving
> multiplicity and exact provenance state.
>
> - **Observable**: both populations contain equivalent multisets.
>
> *… elided here (marked per review 3, H4): **Oracle** at lines 916–917,
> **Oracle independence** at 918–919, and **Mutation proof** at 920–923 —
> the last of which is quoted in full and relied on under slice 2 below,
> because it is the source of that slice's per-class injection obligation …*
>
> - **Falsifier**: one fact, authority state, judgment state or disclosure
>   is missing, duplicated, changed, collapsed or associated with a
>   different evaluation in either channel.

A rendered route is a disclosure Polaris presents, so it must appear in both
channels under the same id and the same evaluation — which is what slice 2
builds, so the invariant is satisfied rather than amended [Inferred: the
reading of "disclosure" this packet relies on].

Slice 3 is PWB-REQ-010 and PWB-REQ-011 conformance and adds no claim; slice
6 adds no code at all.

**PWB-REQ-004 is not entered by any slice.** Its closed population is quoted
verbatim from lines 491–498 of the same file (range corrected per review 3,
H4 from "lines 490–498"; line 490 is blank):

> The POC SHALL admit project facts only from this closed population:
> `item:<class>:<declared-key>` and `count:<class>` for each of
> PWB-REQ-002's nine extraction classes; `catalog-count:<catalog-key>` for
> each of the nine literal V1 catalog headings; and `project-account:<key>`
> for `purpose`, `promises`, `refusals`, `architecture`, `v1-scope` and
> `v1-success`. Every declaration SHALL be emitted by the extractor assigned
> to an admitted source; an injected or unrecognized fact, class, key,
> catalog or account key SHALL mint nothing.

No slice mints a project fact. A resolution route is an attribute of an
existing claim's epistemic state, in none of the four admitted forms, and is
emitted by no extractor; the band's counts are counts of existing claims,
not new declarations; the home page renders facts the model already carries.
Were the owner or a reviewer to read a route or a band count as a project
fact, slice 2 or slice 3 would acquire a PWB-REQ-004 delta and would queue
behind P-68, and this packet says so here rather than discovering it later.

**Slices 4 and 5 have no spec delta because no requirement reaches them —
and that is itself a finding.** A heading sweep of both signed spec files
finds **no requirement governing the home route or the `surfaces` field**
[Observed, three sweeps with their denominators: `grep -c "^### Requirement"`
returns **24** on the POC spec and **17** on the PWB spec; a case-insensitive
whole-word search for `home` returns **0** hits in the POC spec and **6** in
the PWB spec, and all six are the precedence table's `Home` column or the
registry's "governance home" field, none of them the `/` route; and a search
for the field name as the spec would write it — the backticked literal
`surfaces`, or the string `model.surfaces` — returns **0** in both files.
The word "surfaces" does occur throughout both, always as "the three
surfaces", the human noun, never the model field]. The
three surfaces are specified; the fourth served page is not. So slices 4 and
5 trace to the 2026-08-30 direction's other arm — "Improvement-cycle work
must trace to POC-REQ-001..061 or to a recorded review finding" — naming
findings L6-F1 and L6-F5. **Q7 puts that reading to the owner** (corrected
per review 1, F6: Q5 asks only whether slice 6's run and its write are
authorized; it carries no limb about slices 4 or 5, and Q7 is where the
recorded-finding reading is now stated as an explicit, owner-facing choice).
The consequence a reviewer should see: changing the home page freely is lawful
today precisely because nothing specifies it, and the same silence means no
oracle but `routes.test.ts` protects it.

**Slice 7's output is a governance artifact, and the spec is silent there
too.** Nothing in either spec governs what Syzygy may draft into its own
decisions directory; that is doctrine and act territory, which is why Q3 is
an act question and not a spec question.

**Both specifications are digest-bound. No slice edits spec text.** A slice
that comes to want spec text stops and routes through CC-REV-2 and a new
owner act, as a question to the owner, never as a plan step.

### New WHEN/THEN scenarios (for the beads' acceptance contract, not the spec)

**S1 — Every rendered Unknown carries a closed reason and a route.**
WHEN any of the three surfaces renders an Unknown disclosure, THEN that
disclosure carries a reason from RFC2-24's closed twelve and either its
route or the declared "No route declared" copy, AND a sweep over the served
pages reports **its denominator per surface** and zero exceptions on each
(corrected per review 1, F5 — not one pooled denominator across surfaces
whose disclosure population today runs 22, 0 and 0; corrected again per review
2, G11, which read "differs by two orders of magnitude" — a ratio that is
undefined against a zero denominator, and one borrowed from the
`epistemic-unknown` family Q1 has just said may not be pooled with this one).

**S2 — The one available action is reachable from the Unknown that names
it.** WHEN `relationship:intent-to-work` renders Unknown because the
materialization step has not run, THEN its disclosure carries a link to the
materialize panel, mount-prefix correct on both host forms, AND following
that link writes nothing and changes no model field.

**S3 — An empty route array never means an unrouted Unknown.**
WHEN a claim or relationship is labelled Unknown **and carries `reasons`**
(corrected per review 1, F2 — not every Unknown; the `basis: 'deferred'` arm
carries no `reasons` and is out of this scenario's scope), THEN its
resolution-route array is non-empty, AND when it is labelled Observed, THEN
the array is empty; a type-level test and a machine-answer sweep assert both
directions with their denominators.

**S4 — The band and the gaps section cannot disagree.**
WHEN the opening band renders N Unknown claims across R reasons, THEN the
"Unknown, by reason" section renders the same N across the same R, AND a
test asserts equality of both totals and of the reason sets on every
fixture.

**S5 — A reason with no route still renders.**
WHEN a fixture carries an Unknown whose reason has no route in the closed
table, THEN the page renders the declared "No route declared" copy with the
reason beside it, never an omission, AND the copy oracle's unreachable-row
set no longer lists that row.

**S6 — A declared surface count equals its rendered population.**
WHEN a surface is served at evaluation E, THEN the count its descriptor
declares equals the population it renders, AND the test reports both
denominators per surface.

**S7 — The home page states what needs the owner.**
WHEN the home page is served, THEN it names the current evaluation and its
as-of instant, the Unknown counts by reason with their routes, and the one
available action, each row a link that resolves; AND no rendered internal
link on the page is dangling.

**S8 — With no prior evaluation, "changed" is a named Unknown.**
WHEN no previous evaluation exists, THEN the home page's "what changed"
region renders Unknown with its reason and route, AND never the sentence
"nothing changed".

**S9 — The return path runs, and the record says which edges moved.**
WHEN the materialize action, the worker change and the operator capture step
have each run once, THEN the next evaluation records, for all five Unknown
relationships, the before and after label; AND the record states that
`relationship:work-to-code` and `relationship:code-to-evidence` remain
Unknown, and cites the seam-scoping comment that makes that correct.

**S10 — A drafted act is never a performed act.**
WHEN the drafter produces a packet, THEN the packet's head says it binds
nothing, it carries no performed ceremony phrase and no acceptance-record
row, AND `scripts/check_governance.py` fails if a drafted packet ever
carries an accepted or performed banner.

**S11 — No GET writes anything.**
WHEN any surface or machine route is requested, THEN no governance artifact,
work item or record is written, AND a test asserts the state directory and
the governance tree are byte-identical before and after a full sweep of
every route.

**Out of scope, explicitly.** Amending either specification; amending
doctrine; any background timer, poller or watcher; any second repository;
any write toward the observed repository; a machine-channel *release*
action of any kind; scoring or judging the owner's walkthrough answers; the
catalog-route question the M1 ruling left closed; and the freshness and
currency work, which is M2's.

## Collision and sequencing

**Corrected this session (review 1, F3).** The draft's Q7 said "the one
shared file with M2 is none" while this section said, of M2, "the one
shared file is `project-shape-model.ts`" — a direct self-contradiction
inside one packet. The true set, re-derived from both sibling packets' own
Gate 3 tables rather than asserted:

**With M2 (`syzygy-dov.2`, register row P-69, PR #36).** M2's Gate 3 names
`packages/three-surface-poc-core/src/model.ts`
(its slices 2, 3), `apps/three-surface-poc/src/routes.ts` (slice 3, the
`/api/poc` and `/api/poc/polaris` handlers, cited near line 227+, outside
M4's touched region of that file),
`apps/three-surface-poc/src/polaris.ts` (slices 1, 2 **and 6** — line 357's
`claimStatesBlock` freshness group is slice 1, the opening band is slice 2,
and lines 506–510's reading block is slice 6; corrected per review 2, G9,
which superseded the attribution "slices 1, 2" against regions that are in
fact slices 1 and 6),
`apps/three-surface-poc/src/polaris-copy.ts` (slice 1, lines 45–49, plus the
copy-oracle test) and
`packages/three-surface-poc-core/src/project-shape-model.ts` (slice 5,
lines 162–193), plus `git-observation.ts`, `main.ts`,
`polaris-reading.ts` and the adapter-registry declaration JSON, which M4 does
not touch. **Superseded 2026-09-15 (review 2, G1):** this list placed
`polaris-copy.ts` among the files "which M4 does not touch" and the sentence
below read "**M4 shares four files with M2, not none:**" — both false, and the
first was contradicted thirty lines below by this section's own sentence that
M4 slice 3 adds band copy rows to that file. **M4 shares five files with M2,
not four and not none** [Observed, re-derived by hand this session: M2's Gate
3 names 9 distinct files, M4's names 13, the intersection is 5]:
`polaris-copy.ts` (M2 slice 1's lines 45–49 and M4 slice 3's band rows are
**rows of the same declared-copy array**, reconciled by the same copy oracle's
`UNREACHED_IN_FIXTURES` set at line 296 of
`apps/three-surface-poc/src/polaris-copy.test.ts` — the one genuine **shared
copy-oracle reconciliation site** of the five, so M2 slice 1 and M4 slice 3
cannot land independently),
`model.ts` (M4 slices 1, 2, 4 — cited regions 90–96, 305,
562–617, 710–750, none overlapping M2's cited `model.ts` lines 100–110),
`routes.ts` (M4 slice 5, lines 34–96 — outside M2's cited handler region),
`polaris.ts` (M4 slices 1, 3 — the `unknownLine` render and
`gapReasonCounts`/`gapsList` at 922–948, outside M2's cited lines 357 and
506–510) and `project-shape-model.ts` (M4 slice 2 widens `ResolutionRoute`
at 115–118 and `routesFor` at 150–154, adjacent to but not overlapping M2's
162–193). Every pairing above is adjacent by the line ranges each packet
itself cites; this repair did not re-audit every future edit inside those
files, so treat "adjacent, not overlapping" as holding for the cited
regions, not as a guarantee against the eventual diffs.

**The copy-array site, renamed 2026-09-15 (review 3, H7).** The
`polaris-copy.ts` entry above read "the one genuine **merge-conflict site**
of the five". The two edits sit 143 lines apart in that array — M2 slice 1's
cited region is lines 45–49, and M4 slice 3 adds rows beside
`label.deferred` / `label.no-route` at 192–193 — so they do not textually
conflict [Observed: both regions read this session]. The coupling that does
hold, and that carries the sequencing conclusion unchanged, is the one named
in the entry itself: both changes must reconcile the same
`UNREACHED_IN_FIXTURES` set, and M2's Gate 3 slice-1 row names the
copy-oracle test.

The one shared
*concept* is M2's `evidence` block on the machine payload and M4's route
fields: both grow `/api/poc`, and both must land in the parity sweep's
denominator rather than forking it. **M2's Q7 and M4's Q2 are the same
shape of question** — what an implementation does when a closed vocabulary
has no member for a state — and the owner should notice that this packet
now recommends *narrowing* an existing arm (review 1, F2) rather than
choosing between minting and an existing value outright; the two questions
still turn on RFC2-10's and RFC2-24's identical "never dressed as" sentence
and the owner may want to rule them together.

**With M3 (`syzygy-dov.3`, register row P-70; cite it by register row P-70
and by the two files, never by head — this packet named a head three times
while saying not to, and review 2's G7 found that head already stale: the M3
worktree has moved twice since, and M3's
Gate 3 table, slice 3 design and slice 3 oracle are unchanged across the
move; the head this sentence used to name is removed here per review 3, H3,
which found review 2's G7 disposition claiming that removal while the head
still stood).** M3's slice 5
generates the freshness, tier and challenge encoding tables and its slice 6
adds a render-disclosure family; both touch
`apps/three-surface-poc/src/polaris-copy.ts` and
`apps/three-surface-poc/src/polaris.ts` lines 346–361. M4 slice 1 adds a
reason and a route to nine disclosures and M4 slice 3 adds band copy rows —
in the same two files. **The real overlap is M3's "one declared encoding
table" and M4's "nine disclosures that do not use it".** They are the same
finding from two sides: M3 builds the table, M4 supplies the nine rows that
must be in it. **M3 should land slice 5 before M4 slice 1**, so slice 1
populates a generated table rather than a hand-written one; if M4 goes
first, M3's table must absorb nine rows it did not plan for.

**A second, head-on duplicate (review 1, F3(c); widened from two packages to
three by review 2, G2): M2 slice 2, M3 slice 3 and M4 slice 3 all render into
the same region — the opening band, in the same function of `polaris.ts`.**
M2's slice 2 renders an evaluation-currency disclosure there (its Gate 3 row
names "`polaris.ts` (the opening band)"; its design body opens "Rendered in
the opening band, before the first catalog section:"), which this packet's
earlier account attributed to M2 slice 2 without ever locating it — citing
instead line 357 and lines 506–510, which are M2's slices 1 and 6 — so the
collision analysis that exists to catch exactly this never reached it.
M3's slice 3, "One real Unknown in the first reading," renders the page's
two existing whole-shape and class-level Unknown claims before the first
catalog group, oracled on "the first rendered Unknown precedes the first
`data-polaris-group=\"catalog\"`" occurrence. M4's slice 3, "The opening
band," renders the `gapReasonCounts` projection after the project account
and before the first catalog section, oracled on "the band's total equals
the gaps section's total." Both are opening-band designs in `polaris.ts`,
both touch `polaris-copy.ts` for their own copy rows, and M4's own earlier
account of the collision named only M3's slices 5 and 6, never slice 3.
**Superseded 2026-09-15 (review 2, G2).** This section recommended:
"**Recommendation: one band, one owner, one oracle.** M3 slice 3 should land
first, exactly as designed; M4 slice 3 should then extend that band with the
gaps-derived rows … and its oracle becomes the union of both." That
recommendation was derived from a two-way pairing that never saw M2 slice 2,
so it is replaced — **a changed recommended answer, stated plainly.**
**Revised recommendation: one band, one owner, one oracle across all three
packages.** The three payloads (currency disclosure, the two existing Unknown
claims, the `gapReasonCounts` projection) are distinct claims and stay three
blocks; the *region* is one, so whichever of M2 slice 2, M3 slice 3 and M4
slice 3 lands first builds the band container and owns its single ordering
oracle — the whole band precedes the first `data-polaris-group="catalog"`
occurrence — and the other two add a payload block plus their own
payload-specific oracle (M3's first-rendered-Unknown, M4's
band-total-equals-gaps-total). None of the three builds a second band, and
none of the three keeps an independent claim on "first". The block order
inside the band is the owner's to set: if the owner rules that a currency
disclosure and an Unknown band are separate regions, each region still needs
a stated position relative to the others rather than three separate
first-position assertions. This packet no longer recommends an unconditional
M3-slice-3-first order for the band, and says so in the handoff; its
recommendation that **M3 slice 5 land before M4 slice 1** is a different
finding and is unchanged.

**With lane B (`agent/syzygy-dov.17`, PR #35, register row P-68).** Lane B
is a semantic-delta package amending PWB-REQ-007, 014 and 020 so that a
tuple field uniform across an enclosing scope may be carried once on the
scope. **No M4 slice writes a tuple field**, so the hoist does not reach
them. One interaction is worth naming: if lane B's scoping is later extended
to *disclosure* attributes, slice 1's nine new `data-unknown-reason` values
would become hoist candidates in a page where seven of nine carry the same
reason — and a hoisted reason with a differently-routed disclosure beneath
it is exactly lane B's own over-asserting-scope falsifier. Record it in
`syzygy-dov.17`'s notes; nothing blocks today.

**The order (corrected per review 1, F3, and again per review 2, G2, which
superseded step (3)'s "M3 slice 3, landing the one opening band; then M4
slice 3 as an *extension* of that band, not a second one" — that step named
two of the three packages that write the band).** (1) Rule P-68; open no spec
package meanwhile — M4 opens none, so this does not gate it. (2) M3 slice 5,
then M4 slice 1 and slice 2 together, since they share the widened type.
(3) The opening band, once, across M2 slice 2, M3 slice 3 and M4 slice 3: the
first of the three to land builds the container and the single ordering
oracle, and the other two add payload blocks inside it — the order among the
three is the owner's (Q7), and M4 slice 3 does not start before it is ruled.
Note that M2 slice 1 and M4 slice 3 also share the declared-copy array in
`polaris-copy.ts` (review 2, G1), so those two are sequenced by the same
ruling. Then slice 4, then slice 5 — the home page is the composition of the
two before it and should be built last. (4) M4 slice 6 at any time **once Q5's
authorization limb is ruled**; its value is highest early, because its
result is an input to every later judgment about whether the loop works.
(5) Slice 7 only after Q3; slice 8 only after its own acts.

## Gate 6 — Engineering bar

Acceptance, in the M1, M2, M3 and P-63 shape:

1. **Retained measurement, before and after**, direct and tailnet host
   forms, at a named Syzygy commit and Butlers revision, in `docs/evidence/`,
   from a private daemon on port 0 with its own state directory, never the
   loopback daemon, on a committed clean tree. Note the constraint recorded in
   AGENTS.md: the daemon serves only the registered locator, so a repaired
   Butlers page cannot be measured from a scratch clone. The M4 numbers to
   record: the disclosure census per surface with its own denominator
   (Polaris 22 today, 13 routed; Trajectory and Orrery measured separately
   at 0 disclosure elements and 299/9 rendered `epistemic-unknown` claim
   encodings respectively — 301/11 raw, each less one stylesheet rule and one
   legend key item — until slice 1 gives them the marker; corrected per review
   1, F5 and re-partitioned per review 2, G3, so a one-surface figure is never
   offered for the three-surface invariant, and raw and rendered counts are
   always published together), **the `provenance-none` census per surface —
   Polaris 0, Trajectory 0, Orrery 9 rendered against 0 style occurrences,
   home 9 rendered plus 1 style rule, added per review 3, H1** — the href
   census per surface with its buckets,
   the home page's byte size and composition, the band's byte cost, and the
   page's byte size on both forms against the 1,400,000-byte working target
   and the 2,097,152-byte ceiling.
2. **Every M1 invariant equal before and after** except the ones M4
   deliberately changes: claim id set, item and source populations, and zero
   dangling fragment targets stay equal; the href census, the disclosure
   census and the home page's composition are expected to move, and the
   evidence file records both sides. Computed by script, never transcribed.
3. **Rule-6 mutation evidence for every new guard branch**: each of slice 1's
   nine route rows (blank one, confirm the sweep fails); a thirteenth reason
   value; slice 2's empty-array-on-Unknown prohibition; slice 3's
   band-equals-gaps invariant (change one total, confirm it fails); slice 4's
   declared-equals-rendered assertion; slice 5's no-prior-evaluation
   counterexample; slice 7's drafted-packet banner check. Each mutant's
   `old`/`new` fragment and the commit it ran at are recorded — ids and
   outcomes alone are not re-runnable — and a mutant that throws at describe
   time reports zero tests and scores as survived, so fixtures are built in
   `beforeAll`.
4. **Both parity sweeps with both denominators**: the Polaris sweep's
   `unknown-disclosure`, `unknown-relationships` and the new route family,
   per tuple against the machine claim by id and over both id sets; and
   `routes.test.ts`'s home-page tuple comparison, whose denominator slice 5
   grows.
5. **Preflight populations, keyboard, no-JS and browser tests**, the app
   suite twice and the full suite pass; build the core package
   (`tsc -b packages/three-surface-poc-core`) before the app typecheck, or
   the app reports phantom errors.
6. **Slice 6's evidence is the run itself**: the daemon stderr (empty, per
   the fresh-checkout verdict), the `TestArtifactRecord`, the before and
   after machine captures with their sha256s, and the five-relationship
   before/after table including the two that stay Unknown.
7. **Independent review in fresh context** before close, raw retained as a
   `-RAW.md` file — the only suffix `check_governance.py` exempts from CG-1b
   and CG-15 — and a re-issued raw is a second `-RAW.md` file, never an
   overwrite.
8. **Conformance expected values hard-coded**, never imported from the
   module under test; every new copy label distinctive enough that a
   substring match cannot succeed by coincidence.

## Review 1 and repairs (2026-09-14)

An independent fresh-context review of this packet (read-only; only the
artifact, its governing references and the questionnaire invariant) is
retained verbatim at
`docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-RAW.md` (47636 bytes, sha256
`6983034196c706c213e2a939e0ca7dfe4c3f75f958378403fbd115112c2966ec`,
computed by `sha256sum` this session). It reviewed the packet at 83557
bytes, sha256
`8a28fadc7765f4715360bae36c8d0fbe312308a4657c42c3db086fe29862d7e4`, and the
evidence record at 25070 bytes, sha256
`ae753f560bfe04a65f49418fcd59d1d390cf36c75a12e902ccdb65764843d11d`, on
commit `61bd43b0498393495b71c4e8f43bf9fb51d89596` with both files
untracked. Its verdict word, copied exactly: **REVISE — six blocking,
fourteen non-blocking, two editorial**. Every one of the twenty-two
findings was re-derived against source and the retained captures — not
assumed correct — before being applied; where re-derivation is unusually
substantial (F1's key-by-key route comparison, F2's `routesFor`/
`EpistemicState` read, F3's shared-file recount against both sibling
packets' own Gate 3 tables, F4's write-target read against the 2026-09-02
act, F5's per-surface disclosure sweep) the method and result are quoted in
the repaired text itself, not only here. Every edit below was made after
that review, so by verification rule 10 the review binds the bytes it
names and not these; a second fresh-context review follows, and its raw
will be a second `-RAW.md` file, never an overwrite.

| Finding | Severity | Disposition |
|---|---|---|
| F1 RFC2-24's table and `UNKNOWN_REASON_ROUTES` are not word for word equal; slice 1's mapping table used the RFC's prose | blocking | Re-derived and confirmed (5 of 12 identical, 7 differ, extracted and compared this session): the "word for word" claim replaced with the measured split and method in Gate 2; slice 1's mapping table rewritten to use `UNKNOWN_REASON_ROUTES`'s own strings; a note added that rendering the RFC's prose instead is a separate, twelve-value change |
| F2 Q2's "unreachable by construction" is false; `routesFor` has two return-`[]` branches and cap1-core's `EpistemicState` already models a routeless Unknown | blocking | Re-derived and confirmed (`routesFor` quoted with both branches; `EpistemicState`'s `basis: 'deferred'` arm quoted; `label.deferred` found in `UNREACHED_IN_FIXTURES` beside `label.no-route`): Q2 rewritten as a genuine choice; slice 2's design and S3 narrowed to "Unknown carrying `reasons`" so the deferred arm stays representable |
| F3 the sequencing answer's collision analysis is wrong in both directions and misses M3 slice 3 duplicating M4 slice 3 | blocking | Re-derived and confirmed (M2 and M4 share four files, not none or one; M3 and M4 share two files; M3 slice 3 and M4 slice 3 are the same opening band, read from the `m3wt` worktree on 2026-09-14, committed head `b34fca7` with a review-3 repair uncommitted, read-only; an earlier wording here named the wrong head): Q7 and the Collision section rewritten with the corrected file sets and an explicit one-band recommendation; sequencing order updated |
| F4 slice 6 writes into the observed repository; the packet asserted "writes nothing" while its own Q3 argument would forbid the same write | blocking | Re-derived and confirmed (`materialize-action.ts:33`, `materialization.ts:12,186-208`, PWB act lines 70-72 quoted): Q5 rewritten with both readings quoted and a stated counter-argument, recommendation labeled [Inferred]; slice 6 made conditional; the "writes nothing" sentences and the VIS-5 "this is why it's lawful" paragraph corrected to state the question rather than assume an answer |
| F5 slice 1's sweep has denominator 0 on two of three surfaces; POC-REQ-060 quantifies over all three | blocking | Re-derived and confirmed (Trajectory 0 disclosure / 301 `epistemic-unknown`; Orrery 0 / 11; measured this session on the retained captures): Q1, slice 1's design and Tests, Success criterion 1, S1 and the Gate 6 numbers list all restated per surface with their own denominators |
| F6 Q5 is credited with a "recorded review finding" reading for slices 4-5 that it does not carry | blocking | Re-derived and confirmed (Q5's text carries no such limb; the 2026-08-30 direction's trace rule quoted): the reading moved to Q7 as an explicit limb; the two "Q5 puts that reading to the owner" sentences corrected to point to Q7 |
| F7 (N1) Orrery's derived id lists are at lines 747–748, not 745–746, repeated three times | non-blocking | Re-derived and confirmed: corrected in the source-citation table, Q6, slice 4's design text and the evidence JSON |
| F8 (N2) the two seam citations are off by one at both ends | non-blocking | Re-derived and confirmed (comment 26–29, const 30–33; comment 35–41, const 42): corrected in Q5's text and the evidence JSON |
| F9 (N3) the five relationship ranges mix two conventions and the dossier correction understates the end by nineteen lines, not one | non-blocking | Re-derived and confirmed (brace ranges 562–581, 582–590, 591–599, 600–608, 609–617; whole span 562–617): one convention stated, correct span given |
| F10 (N4) the `surfaces` literal closes at line 750, not 749 | non-blocking | Re-derived and confirmed: corrected in the source-citation table and the Gate 3 topology table |
| F11 (N5) `model.surfaces` is one of five fields `renderPocPage` reads, and the evidence JSON's hit-count claim was wrong by three | non-blocking | Re-derived and confirmed (hits at 35, 78, 87, 89×2, 92×2, 127, 133, 171, 172): Q6 restated to "the only input for the three surface panels"; the evidence JSON's sweep note corrected |
| F12 (N6) the "dossier overstates" correction is misattributed to the "Why" bullet and reads as if the caveat itself were new | non-blocking | Re-derived and confirmed (line 205, the "What" bullet; both the dossier's slice-6 bullet and L5-M7 already carry the caveat): slice 6's design text corrected on both points |
| F13 (N7) "zero cross-surface deep links" is measured over four pages while a fifth, uncensused page carries one | non-blocking | Re-derived and confirmed (6 hrefs on the exact-source capture, 1 fragment, 5 non-fragment including the anchor link): Gate 1 measurement 1 restated with the fifth page's census and the existing-instance note |
| F14 (N8) the `walkthroughJudgment.outcome` path is misattributed to "the dossier", which never names the field | non-blocking | Re-derived and confirmed (`walkthroughJudgment` has zero occurrences in the dossier `.md`; it is in L5-F10's evidence list): attributed to L5-F10 |
| F15 (N9) Q6's "713 claim tuples" has no evidence-file entry | non-blocking | Re-derived and confirmed (713 on the lane A tailnet capture, denominator the whole page; 699 pre-lane-A): recorded in a new evidence JSON field with the 699→713 movement noted |
| F16 (N10) the registry file cited for the write surface carries a candidate governance-lifecycle status and is the wrong instrument for the work-scheduler question | non-blocking | Re-derived and confirmed (top-level governance-lifecycle status field reads `candidate-amendment-no-effect-until-owner-act`; `typedAuthority` inside `entries[0]`): the VIS-5 paragraph rewritten to state both facts |
| F17 (N11) "a fourth vocabulary" and "three vocabularies" are unenumerated rhetorical counts | non-blocking | Re-derived and confirmed: resolved by Q2's full rewrite, which states the two legal states explicitly rather than counting vocabularies |
| F18 (N12) "three paragraphs on" is the next paragraph, and the RFC2-24 quote elides a continuation without an ellipsis | non-blocking | Re-derived and confirmed (the "fact of the render" sentence is in the paragraph starting at line 98, immediately after 92–96): corrected to "the next paragraph"; an ellipsis and the elided fragment added |
| F19 (N13) v1.md's artifact phrase spans lines 119–120, not 116–119 | non-blocking | Re-derived and confirmed: corrected in slice 6's design text and the recommended handoff, in both places |
| F20 (N14) the capture provenance table leaves Orrery's byte size blank | non-blocking | Re-derived and confirmed (37,048 bytes, matching the evidence JSON and `wc -c`): filled in |
| F21 five lines exceed 78 columns; the H1 is the one line a repair could shorten | editorial | Re-derived and confirmed: no repair applied to the H1, for consistency with the M2 and M3 sibling packets' own H1s (99 and comparable characters), also left unshortened; the path-span lines remain unfixable by AGENTS.md's own rule against reflowing a code span. **Superseded 2026-09-15 (review 3, H5):** this disposition said "five lines" and "the four path-span lines", figures read from review 1 rather than re-derived as the packet grew. Re-derived over the current bytes after every review-3 edit [predicate: lines that are outside fenced code blocks and are not table rows — a table row being a line whose first non-space character is a pipe — and whose length exceeds 78 characters; denominator: 1,657 lines, the whole file]: **7** — line 1, the H1, at 126 characters and disclosed here, plus six path-span lines at 10, 493, 568, 764, 975 and 1023 |
| F22 the nine source-claim rows name Butlers paths in plain prose while the evidence JSON genericizes the same rows | editorial | Re-derived and confirmed: one clarifying sentence added after the disclosure table |

**Recommended answers changed (stated plainly, none hidden).**
Q1 widened from Polaris-only to all three surfaces, with a remedy note about
the marker gap. Q2 changed from "do not mint `none-modelled`" argued as
contract-determined with one lawful arm, to a genuine choice recommending
"do not mint `none-modelled`; name and route the existing
`basis: 'deferred'` arm instead." Q5 gained a new, contested authorization
limb (two readings quoted, recommended answer labeled [Inferred] with a
counter-argument) that the draft did not carry at all; its expectation limb
is unchanged. Q6's recommendation is unchanged but its supporting claim is
corrected. Q7 widened from a sequencing-only question to also carry the
corrected file-intersection set, the M3/M4 slice-3 reconciliation, and the
slices 4–5 authorization-arm reading the draft had wrongly folded into Q5.
Q3 and Q4 are unchanged.

## Review 2 and repairs (2026-09-15)

A second independent fresh-context review of the repaired packet (read-only;
only the artifact, its governing references and the acceptance criteria) is
retained verbatim at
`docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-2-RAW.md` (39050 bytes, sha256
`a7b3782882e41cf954e1dda326f502e20eceea4acd05732625de9f9ee2654649`, computed
by `wc -c` and `sha256sum` this session, never transcribed). It reviewed
commit `6218726`, at which the three artifacts hashed as follows — recomputed
this session with `git show 6218726:<path> | sha256sum`:

| File reviewed | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` | 116002 | `95e72b30a7d496e963ae6a244dd421bd720d317fae126a3c027b07e0a4ee3d5b` |
| `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json` | 31201 | `54b22be504c58483a9d52bab26e4e89f62766eccc167bbc9eb8a8a10009e8f23` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 29879 | `7ff5bc37abe5f152bb9d02d6b891bcb24e8db47b141804485ada6e8106b87e97` |

Its verdict word, copied exactly: **REVISE**. Its counts, as the raw states
them: **blocking 4, non-blocking 5, editorial 2** — G1–G4 blocking, G5–G9
non-blocking, G10–G11 editorial. Every finding was re-derived against source
and the retained captures this session before being applied; none was applied
on the review's say-so, and the re-derivation method is stated in the repaired
text itself wherever it is load-bearing. Superseded wording is quoted and
dated in place rather than deleted.

| Finding | Severity | Re-derivation | Disposition |
|---|---|---|---|
| G1 the M2 shared-file set is one file short and the Collision section contradicts itself about `polaris-copy.ts` | blocking | **CONFIRMED.** Both Gate 3 "Lives in" columns intersected by hand this session with both denominators: M2 names **9** distinct files, M4 names **13**, the intersection is **5** — `model.ts`, `routes.ts`, `polaris.ts`, `project-shape-model.ts`, `polaris-copy.ts`. The review states M4's denominator as twelve; this pass enumerates thirteen (both `scripts/check_governance.py` and `capture-test-artifact-main.ts` appear in slice 7's row, and the review appears to have taken one of the two as an adjacency rather than a named file). The difference does not touch the intersection, and every one of the thirteen is enumerated in Q7 so a reader can re-derive it. M4 slice 3's own Gate 3 row names `polaris-copy.ts`, which the packet listed as untouched thirty lines above its own sentence saying M4 slice 3 edits it | Applied. Five files at Q7 and in the Collision section with both denominators published; `polaris-copy.ts` removed from the "M4 does not touch" list; the declared-copy array named as the site M2 slice 1 and M4 slice 3 share under one copy oracle, so those two cannot land independently; register row corrected. **Renamed 2026-09-15 (review 3, H7):** this cell called it "the merge-conflict site"; the two edits sit 143 lines apart in that array (M2 slice 1 at lines 45–49, M4 slice 3 beside `label.deferred` / `label.no-route` at 192–193) and do not textually conflict, so it is the **shared copy-oracle reconciliation site**. The sequencing conclusion is unchanged |
| G2 M2 slice 2 is a third opening-band design and the one-band recommendation does not see it | blocking | **CONFIRMED.** M2's Gate 3 slice-2 row names "`polaris.ts` (the opening band)"; its slice-2 design body opens "Rendered in the opening band, before the first catalog section:" and gives the currency-disclosure block; its own honest target names the band; three further mentions treat it as slice 2's. The packet attributed M2's `polaris.ts` to "slices 1, 2" and then cited line 357 and lines 506–510, which are M2's slices 1 and **6**, so slice 2's region was attributed and never located | Applied, **and it changed a recommended answer** — stated plainly in Q7, in the Collision section, in the funnel summary, in the handoff and in the register row. The reconciliation is now three-way: one band container, one ordering oracle owned by whichever of M2 slice 2 / M3 slice 3 / M4 slice 3 lands first, three payload blocks each with its own payload oracle. The M2 `polaris.ts` region citation is corrected to slices 1, 2 and 6 |
| G3 Q1's cross-family reconciliation sentence is false, the Polaris figure is `null` in the record, and the published denominators count a stylesheet rule as a rendered encoding | blocking | **CONFIRMED.** Predicate: literal occurrences of the string `epistemic-unknown`; denominator: the whole served page; then every occurrence assigned to its enclosing tag. Polaris **2** on both lane A forms (offsets 2,809 and 1,481,343 tailnet / 2,809 and 1,475,493 direct) — one `<style>` rule, one legend key item, and an element-inner sweep of all 22 `data-unknown-disclosure` elements (offsets 378,631 through 1,462,622) finds **0**. Trajectory **301** = 1 + 1 + 299; Orrery **11** = 1 + 1 + 9; home **18** = 1 + 1 + 9 `epistemic-label` spans + 7 bare Unknown spans. The partition accounts for every occurrence on every page | Applied. The "including Polaris's own 22 disclosures" clause superseded in place; raw and rendered counts published together with the difference named, at Q1, Success 1, S1 and the Gate 6 numbers list; the record's `null` replaced with the measured 2 plus the full partition. **Superseded 2026-09-15 (review 3, H2):** this cell went on to say **"'Largest of the three' re-checked and still holds:** 299 + 9 = **308** rendered claim encodings across the two surfaces, against Polaris's 13 routed and 9 bare-prose disclosures" — a ranking across two marker families that count different objects, which Q1's own next sentence forbids. Restated at Q1 as what was measured: each surface's Unknowns are encoded by a marker the other two do not share, reported per family and unranked. **And superseded again by review 3, H1:** the two-literal census reached neither the requirement's full population — see the review-3 section below for the fourth family |
| G4 Q6's preamble calls a lawful arm unlawful, in Q2's minting language | blocking | **CONFIRMED.** Neither Q6 arm mints a vocabulary value; the phrase is Q2's, about `none-modelled`. Gate 0, Gate 3's slice-4 row and Gate 5 all state that no requirement in either signed spec governs the home route or `model.surfaces`, and Gate 5 draws the consequence — changing the home page freely is lawful today precisely because nothing specifies it. The Q6 row itself already carried deletion honestly | Applied. The preamble sentence is quoted, dated and superseded; Q6 is restated as a genuine engineering choice put to the owner *because* no requirement reaches the field, with the minting clause returned to Q2 alone. The recommended answer (true by construction) is **unchanged** |
| G5 Reading A's quotation of the 2026-09-02 authorization is in the wrong place and spliced out of source order | non-blocking | **CONFIRMED.** The act's header is the comment block at lines 1–17 and contains none of it; the text is the body section "What the recorder reads this as", lines 44–52, where "and nothing wider" closes line 48 and "**Implementation planning and implementation**" opens line 50, and the elided clause is the tasks range that bounds the grant | Applied. Cited as the body section at lines 44–52, quoted in source order, tasks-range clause restored. The substance of Reading A is unchanged |
| G6 the register row ends with a collision the packet's own Collision section denies | non-blocking | **CONFIRMED.** `UNKNOWN_REASON_ROUTES` is declared at `packages/three-surface-poc-core/src/project-shape-model.ts` line 89 and closes at 102. M2 slice 5 cites 162–193 — the freshness and tier constants at 167–169 and the `claim` / `observedClaim` / `unknownClaim` constructors at 171–195. M4 slice 2 cites 115–118 and 150–154. Neither edits 89–102, exactly as the packet's Collision section says | Applied in the register row: the shared file and the shared `claim()` construction site at line 176 (`resolutionRoutes: routesFor(epistemic)`) replace the false reason, and the copy-array and opening-band collisions are named beside it. The conclusion — rule P-69, P-70 and P-71 together — is unchanged |
| G7 the M3 head is cited three times contrary to the sentence citing it, and is already stale | non-blocking | **CONFIRMED, and now doubly so.** The `m3wt` worktree has moved twice past `b34fca7` since this packet named it. `b34fca7` remains an ancestor of that worktree's head, and M3's Gate 3 table, slice-3 design and slice-3 oracle are unchanged across the move, so G2's and this packet's slice-3 findings stand on current bytes | Applied to Q7. **Restated 2026-09-15 (review 3, H3):** this disposition read "Applied. Head mentions removed from the Collision section and from Q7 … One head mention remains, in the review-1 disposition table" — false about the Collision section, where the head survived in live prose one screen above this table. True count when review 3 swept it [predicate: literal occurrences of the seven-character short head; denominator: the whole packet file]: **4 occurrences over 3 lines** — one in the Collision section (live prose), one in the review-1 disposition table and two in this row; and **2** in the evidence record, both inside its review-1 block. The Collision-section mention is removed in the review-3 pass, leaving **3 over 2 lines**, every one of them a historical record of what a named repair session read, which may not be rewritten. M3 is routed by register row P-70 and by the two files, as this packet's own sentence always said |
| G8 Gate 2 calls two owner directions "the two typed, explicitly authorized adapters VIS-5 requires" | non-blocking | **CONFIRMED.** VIS-5 (`.syzygy/governance/doctrine/vision.md` lines 141–152) requires effects on every other authority to occur "only through **typed, explicitly authorized adapters**, governed by each authority's own contract". It names no number of adapters; the "two" in the paragraph's own heading is two write namespaces | Applied. The sentence is quoted, dated and superseded; the paragraph now says VIS-5 requires the work-scheduler effect to run through a typed adapter governed by that authority's contract, that the materialize mechanism is one such adapter in code, and that what is contested is whether any act authorizes it — which is Q5 |
| G9 the slice attributions the re-derivation rests on are wrong for both siblings | non-blocking | **CONFIRMED.** M3's Gate 3 names `polaris.ts` in slices **1, 3, 5 and 6**, not "3 and 5". M2's `polaris.ts` belongs to slices **1, 2 and 6**, not "1, 2" | Applied in Q7 and in the Collision section, with M2 slice 2's region (the opening band) named. Neither correction changes the two-file M3 set; the M2 set changes by G1, not by G9 |
| G10 the `model.` hit arithmetic in Q6 is off in two places | editorial | **CONFIRMED.** Counted per line at `6218726`: 35:1, 78:1, 87:1, **89:4**, 92:2, 127:1, 133:1, 171:1, 172:1 — **13** occurrences over nine lines. `renderPocPage` spans lines 77–96, so **five** lines lie outside it, not four | Applied. The load-bearing claim — `model.surfaces` is the only input for the three surface panels — is re-derived and unchanged |
| G11 "two orders of magnitude" describes the wrong marker family | editorial | **CONFIRMED.** The disclosure populations are 22, 0 and 0; the ratio is undefined, and the 301/11 that would give roughly two orders of magnitude belong to the family Q1 has just said may not be pooled with this one | Applied. S1 now reads "runs 22, 0 and 0", with the superseded clause quoted and dated |

**Recommended answers changed after review 2 (stated plainly, none hidden).**
**One: Q7's opening-band reconciliation**, from a two-way "M3 slice 3 lands
first and M4 slice 3 extends it" to a three-way "one container, one ordering
oracle owned by whichever of M2 slice 2, M3 slice 3 and M4 slice 3 lands
first; three payload blocks, each with its own payload oracle; the block order
within the band is the owner's." Q7's shared-file figure also moves from four
files to five, and the sequencing order's step (3) is rewritten to match. Q1,
Q2, Q3, Q4, Q5 and Q6 keep the recommendations they carried into this review;
Q1's figures and Q6's framing and arithmetic were corrected without changing
which arm each recommends, and Q5's Reading A keeps its substance with its
citation repaired.

By verification rule 10, review 2 binds the bytes it names — the three digests
in the table above, at commit `6218726` — and not these. Every edit in this
section and above was made after it, so the repaired bytes are **uncovered
until a third review confirms them**; that raw will be a third `-RAW.md` file,
never an overwrite of either retained one.

## Review 3 and repairs (2026-09-15)

A third independent fresh-context review of the twice-repaired packet
(read-only; only the artifact, its governing references and the acceptance
criteria) is retained verbatim at
`docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-3-RAW.md` (31656 bytes, sha256
`ebce963f86f302940cc78f98dbe91325ae5c7b0ffa88e423b1fe05669035ccfe`, computed
by `wc -c` and `sha256sum` this session, never transcribed). It reviewed
commit `f911a45`, at which the three artifacts hashed as follows — recomputed
this session with `git show f911a45:<path> | sha256sum`:

| File reviewed | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` | 139094 | `09116fcfc1fb21127670813196b297705b2a7862edb18dd4fb713391899f0750` |
| `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json` | 38933 | `d7a7aaffd5a1e5a8fd5dc8a3997c9f56e72b4b762bdec42f108886acb7d5b7ed` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 32781 | `38ee2b8e01a2fd483caad90e0a07867a779edf7db1cef5deb7e09065a1eb8f9c` |

Its verdict word, copied exactly: **REVISE**. Its counts, as the raw states
them: **blocking 1, non-blocking 3, editorial 5 — nine findings, H1–H9**.
Every finding was re-derived against source and the retained captures this
session before being applied; none was applied on the review's say-so, and
the re-derivation method is stated in the repaired text itself wherever it is
load-bearing. Superseded wording is quoted and dated in place rather than
deleted. The raw's own G1–G11 verification table (G7 PARTIAL, the rest
REPAIRED) and its F1–F22 regression spot-check are read and carried here: G7
becomes H3 and F21 becomes H5; no other regression was found.

| Finding | Severity | Re-derivation | Disposition |
|---|---|---|---|
| H1 a fourth Unknown encoding on Orrery sits outside both censused marker families, inside POC-REQ-060's own population | blocking | **CONFIRMED.** Counted this session [predicate: literal occurrences of the string `provenance-none`; denominator: the whole served page of each retained capture; then every occurrence assigned to its enclosing tag]: Polaris tailnet **0**, Polaris direct **0**, Trajectory **0**, Orrery **9** rendered spans with **0** inside `<style>`, home **10** = 1 stylesheet rule + 9 rendered spans. The nine Orrery spans' enclosing `<tr>` ids are `work:whatsapp-single-event-normalization`, `evidence:focused-pytest`, `runtime:live-satisfaction`, `region:unmapped-code`, `relationship:intent-to-work`, `relationship:work-to-code`, `relationship:code-to-evidence`, `relationship:code-to-runtime` and `relationship:capability-to-unmapped-region` — exactly the nine objects Q1 asks about. Source read at HEAD: `apps/three-surface-poc/src/exact-tables.ts` line 10 emits the span on an empty `provenance` array; `apps/three-surface-poc/src/design-tokens.ts` line 25 declares `className: 'epistemic-unknown'` and never names `provenance-none`; its only style rule is `apps/three-surface-poc/src/routes.ts` line 73 inside `HOME_STYLE`, which is declared at line 57 of that file and used once, as `extraStyle` at line 90 (the home route); `apps/three-surface-poc/src/orrery.ts` imports `exactTablesSection` at line 4 and calls it at lines 125 and 151 without it. POC-REQ-060's falsifier, quoted from `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md` lines 945–946: "one surface encoding Unknown (or Observed) differently from the declared table, or a surface styling epistemic state ad hoc". Both limbs are met | Applied. `provenance-none` added as a **fourth census family** at Q1 with per-surface denominators and the Orrery-versus-home style asymmetry; "every Unknown" replaced at Q1 and in slice 1's Tests with the predicate actually run, the superseded wording quoted and dated; "at least three encodings" corrected to four; Q1's recommendation and slice 1's Tests now require the re-specified shared marker to cover this rendering, with a rule-6 mutant for it; Gate 3's slice-5 row records that `exact-tables.ts` and `routes.ts` lines 34–96 are where the encoding lives; Gate 5 and the Gate 6 numbers list carry it; the record gains a `provenance_none_census` block. **The recommended answer does not change** — see the paragraph below the table |
| H2 "largest of the three" is the cross-family comparison the next sentence forbids | non-blocking | **CONFIRMED.** The two terms count different objects: 308 counts `epistemic-unknown` spans on Trajectory and Orrery, while 13 and 9 count `data-unknown-disclosure` elements on Polaris — and Q1's own next sentence says the two families "are still not directly comparable … never combined into one total". Review 2's G11 removed "two orders of magnitude" for this reason and the superlative attached to it survived | Applied. The ranking is quoted, dated and superseded at Q1 and in the review-2 G3 disposition row, and restated as what was measured — each surface's Unknowns are encoded by a marker the other two do not share, reported per family and unranked. The record's `largest_of_three_recheck` field carries the same supersession. No recommended answer moves: the remedy turns on the zero-denominator fact |
| H3 G7's disposition says the head mention was removed from the Collision section; it is still there | non-blocking | **CONFIRMED.** Counted this session [predicate: literal occurrences of the seven-character short M3 head; denominator: the whole file]: **4 over 3 lines** of the packet — the Collision section's live prose, the review-1 disposition row and twice in the review-2 G7 row — plus **2** in the evidence record, both inside its review-1 block. The finding's substance was re-derived independently and holds: that head is an ancestor of the m3wt head and M3's Gate 3 table, slice-3 design and slice-3 oracle are unchanged across the move | Applied. The Collision-section mention is removed (the sentence carries its meaning without it, and the removal is noted in place), leaving **3 over 2 lines**, each a historical record of what a named repair session read and not rewritable. Review 2's G7 disposition is restated to the true count and says which mentions are historical; the record's own G7 field is corrected the same way |
| H4 two blockquotes introduced as "quoted verbatim" silently elide intermediate bullets | non-blocking | **CONFIRMED** at source. POC-REQ-060 read at spec lines 925–948: Oracle is 941–942, Oracle independence 943–944, and the Falsifier's second limb is line **946**, one past the cited range. PWB-REQ-020 read at 900–927: Oracle 916–917, Oracle independence 918–919, **Mutation proof** 920–923. PWB-REQ-004 read at 488–500: line 490 is blank and the clause runs **491–498** | Applied. Both elisions are marked with an ellipsis naming exactly what was elided and where; the POC-REQ-060 range is extended to 946 and the PWB-REQ-004 range corrected to 491–498, each with the superseded range quoted; and slice 2 now quotes PWB-REQ-020's Mutation proof bullet in full and states that it — not the project's general practice — is the source of the slice's per-class injection obligation, discharged by Gate 6 items 3 and 4 |
| H5 F21's over-78-column count is now six, not five | editorial | **CONFIRMED that the recorded figure had drifted**, and re-derived last, after every other review-3 edit. The count this pass reports is its own, with the predicate and denominator stated in the F21 disposition itself; it is not the review's figure, because the review measured bytes this pass has since changed | Applied in the F21 disposition, with the superseded "five lines" / "the four path-span lines" quoted and dated. Every over-78 line but the H1 is a single unbreakable path code span, which AGENTS.md's own rule forbids reflowing |
| H6 two offset conventions for the same population, unstated | editorial | **CONFIRMED**, both correct. Re-derived on the lane A tailnet capture: the 22 `data-unknown-disclosure` attributes sit at offsets 378,631 through 1,462,622 and their enclosing elements' opening brackets at 378,599 through 1,462,590 — a delta of exactly 32 at both ends | Applied. One sentence above the disclosure table names both conventions, says which is which, and gives the delta |
| H7 "merge-conflict site" overstates the mechanism the packet itself describes | editorial | **CONFIRMED.** M2 slice 1's cited region in `apps/three-surface-poc/src/polaris-copy.ts` is lines 45–49; M4 slice 3 adds rows beside `label.deferred` and `label.no-route` at 192–193 — 143 lines apart, so the two edits do not textually conflict. The coupling that does hold is the shared `UNREACHED_IN_FIXTURES` set at `apps/three-surface-poc/src/polaris-copy.test.ts` line 296 | Applied. Renamed to the **shared copy-oracle reconciliation site** in the packet, the record and the register note, with the superseded name quoted and dated. The sequencing conclusion — M2 slice 1 and M4 slice 3 cannot land independently — is unchanged |
| H8 Q6's question cell keeps the framing G4 superseded | editorial | **CONFIRMED.** "Disclosed for confirmation" reads either way, and a fresh reader meets the row before the preamble that review 2's G4 repaired | Applied. Q6 now opens "Both arms are lawful; deletion has a cost the move does not name, stated here so the choice is made knowing it", with the superseded phrase quoted and dated |
| H9 three absence and all-claims carry no predicate, denominator or label | editorial | **CONFIRMED.** The conflict check, the boundaries-crossed sentence and the not-touched-by-any-slice sentence each quantify over the eight slice rows one screen above and each was unlabelled, while the packet labels substantive claims everywhere else | Applied. Each carries an `[Inferred]` label naming the eight-slice denominator it was checked against |

**Recommended answers changed after review 3: none.** H1 is blocking and it
widens Q1's remedy — the shared marker the sweep is re-specified over must
cover the `provenance-none` rendering, with its own rule-6 mutant — but it
does not move which arm Q1 recommends. The recommendation turns on the
zero-denominator fact (Trajectory and Orrery emit 0 `data-unknown-disclosure`
elements, so the sweep as originally specified passes vacuously there), and
the fourth family neither creates nor removes that fact; it enlarges the
population the repaired sweep has to reach [Observed: the four censused
per-surface denominators, re-derived this session]. Q2 through Q7 keep the
recommendations they carried into this review; Q1's, Q6's and Q7's supporting
figures, framing and naming were corrected without changing any arm.

By verification rule 10, review 3 binds the bytes it names — the three digests
in the table above, at commit `f911a45` — and not these. Every edit in this
section and above was made after it, so the repaired bytes are **uncovered
until a fourth review confirms them**; that raw will be a fourth `-RAW.md`
file, never an overwrite of any retained one.

## Funnel summary

```
## Feature Request: M4 - Close the owner loop: a route from every Unknown, home as the day-opening, and run the return path once
Size: medium (slices 1-6) / large (slice 7, and the deferred slice 8 pair)
Baseline: Syzygy a9f671e; capture = lane A after/tailnet, 1,484,487 bytes, Butlers 2e3bac97790b
- G1 Motif: 9 of 22 rendered Unknowns on Polaris carry no closed reason and no route; Trajectory (299 rendered, 301 raw) and Orrery (9 rendered, 11 raw) carry a third, unmeasured-until-now encoding with no disclosure wrapper at all (re-partitioned per review 2, G3: raw less one stylesheet rule and one legend key item), and Orrery carries a fourth - the provenance-none span, 9 rendered against 0 style occurrences on that surface and 1 style rule on home, in no declared token table (added per review 3, H1); zero cross-surface deep links over four pages, one anchor deep-link found on a fifth, uncensused page; the product's one submit button sits at 99.1% of the second page [Observed: capture sweeps, denominators stated per surface]
- G2 Doctrine: aligned - VIS-1 (aggregate Unknowns, never substitute), VIS-2, VIS-4 (draft, never adopt - stated per slice), VIS-5 (two write roots; the materialize action's write is Q5's contested question, not a settled lawful-adapter reading), vision.md 61-64 the escape property (unnumbered doctrine prose), RFC2-24's closed twelve, 5 of 12 identical to UNKNOWN_REASON_ROUTES and 7 differing in prose only (review 1, F1)
- G3 Topology: apps/three-surface-poc + packages/three-surface-poc-core; no new boundary; no governed artifact touched by slices 1-5 or 7; slice 6 already writes into the observed repository's Beads database today and whether that write is authorized is Q5's question; slice 7's output is the only *new* write and it is gated
- G4 Design: closed reason + route (UNKNOWN_REASON_ROUTES's own wording, not RFC2-24's prose) on all nine unrouted Polaris Unknowns, extended to Trajectory/Orrery's marker; the materialize link on the one edge that has one; a machine route form with actor/verb/target, narrowing the empty-array prohibition to Unknown-with-reasons so the modelled `basis: 'deferred'` arm stays representable; one opening band across M2 slice 2, M3 slice 3 and M4 slice 3 - one container, one ordering oracle, three payload blocks (revised per review 2, G2); model.surfaces derived; home rewritten as their composition; the return path run once, conditional on Q5; a pure act drafter
- G5 Spec: no delta - POC-REQ-060 already requires slice 1 (over all three surfaces), PWB-REQ-020 already requires slice 2's parity; PWB-REQ-004 untouched; and NO requirement governs the home route or model.surfaces, so slices 4-5 trace to recorded findings L6-F1/L6-F5, a reading Q7 now puts to the owner explicitly
- G6 Bar: retained before/after measurement per surface, rule-6 mutants per guard branch, both parity sweeps with both denominators, independent review (this is review 2, pending, after review 1's repair)
Acts: slices 1-5 and 7 none (the 2026-09-05 continuation); slice 6 contested between the 2026-08-29 direction (authorized) and the 2026-09-02 act's write prohibition (breach) - see Q5; slice 7 one narrow act on arm (a), none on arm (b); slice 8 two acts, deferred; a poller: none found and none sought
Open questions: Q1-Q7 above (Q5 widened to cover slice 6's write; Q7 widened to cover the M2/M3 file collisions and the slices 4-5 authorization reading); queued as P-71 (P-68 lane B, P-69 M2, P-70 M3, each on its own branch)
Sign-off: pending - the owner's
Recommended handoff: Q1 "a non-conformance, per-surface sweep" and Q2 "narrow the prohibition, do not mint none-modelled" -> run slices 1 and 2 together after M3 slice 5; then the one opening band across M2 slice 2, M3 slice 3 and M4 slice 3, then M4 slices 4, 5 in order; run slice 6 once Q5's authorization limb is ruled; hold slice 7 for Q3 and slice 8 for its acts
```

## Recommended handoff

**If Q1 and Q2 are answered as recommended:** file no new bead. Build slices
1 and 2 as one change under `syzygy-dov.4`, after M3's slice 5 lands so the
nine new rows populate a generated encoding table rather than a hand-written
one, and extend slice 1's sweep to Trajectory and Orrery per Q1's scope
correction. Slice 1 alone closes the POC-REQ-060 breach that L2-F2 and
L6-F5 named and puts the product's one action one click from the Unknown
that describes its absence. Slice 2 narrows its type-level prohibition to
an Unknown carrying `reasons`, per Q2's corrected reading, rather than every
Unknown.

**If Q7's opening-band reconciliation is accepted (revised per review 2, G2
from a two-way M3/M4 reconciliation to a three-way one):** the first of M2
slice 2, M3 slice 3 and M4 slice 3 to land builds the band container and its
single ordering oracle; the other two add payload blocks inside it, each with
its own payload oracle. One band, one ordering oracle, three payloads — never
three bands and never three claims on "first".

**If Q4 is answered as recommended:** slice 3's band lists every reason
present, ordered by the existing `foremost` array, and its total is asserted
equal to the gaps section's on every fixture. If the owner prefers the
four-reason filter, the slice adds one closed constant and one counterexample
fixture, and the packet's warning stands: today's evaluation cannot exercise
the filter's negative case.

**If Q5 is answered as recommended (both the expectation and the
authorization-reading limbs):** run slice 6 early and independently of
everything else, and record its result honestly — one edge narrowed, two
correctly did not. If the owner takes Q5's Reading B instead, hold slice 6
for the continuation that reading requires, and run the rest of M4
regardless — no other slice depends on it. That record is the V0
agent-consumption artifact v1.md
lines 119–120 asks for (corrected per review 1, N13), and it is also the
only evidence anyone will have
about whether the rest of M4 is worth building.

**If Q6 is answered as recommended:** slice 4 lands the descriptor and slice
5 composes the home page from it and from slice 3. Build them in that order;
the home page should hold no truth of its own.

**If Q3 is answered as arm (b) or deferred:** build the pure drafter anyway.
It needs no act, it is independently testable, and it is the half of slice 7
that carries the design risk. The file-writing half is a twenty-line
operator command that can wait for the act.

**If Q1 is answered the other way** — that the nine bare-prose Unknowns are
the accepted shape of the entity-and-relationship graph — then slice 1
narrows to the single `actionRoute` on `relationship:intent-to-work`, slice
2 loses its relationship arm, and the POC records a permanent, disclosed
divergence between how it encodes a project-shape Unknown and how it encodes
a graph Unknown. That is a coherent outcome and should be written down as
one, in `.syzygy/governance/decisions/`, rather than left as silence — and
it would mean POC-REQ-060's falsifier is met on every served page, which the
owner should rule on explicitly rather than inherit.
