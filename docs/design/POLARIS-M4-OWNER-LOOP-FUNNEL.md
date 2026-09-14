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
| Orrery | same directory, `orrery.html` | — | `e3ae5b7901c599a04b685456e6070430edf72fcd025cd1f6afecf863153582fa` | **pre-lane-A**, same run |
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
gates in the strict sense: Q1 decides whether nine rendered Unknowns are in
breach of a requirement in force, Q3 decides whether a new write effect is
authorized at all, Q5 confirms what a run may honestly be expected to
produce, and Q7 orders this move against three sibling packages. Q2 and Q6
are contract-determined on this packet's own reasoning — each has one lawful
arm and one that mints a vocabulary value a contract closes — and are put to
the owner for confirmation and disclosure rather than as free choices. Q4 is
a real choice between two lawful arms.

| # | Question | Recommended |
|---|---|---|
| Q1 | **Nine of the twenty-two Unknown disclosures Polaris renders carry no reason from the closed RFC2-24 twelve and no route. Is that a POC-REQ-060 non-conformance to be repaired, or the accepted shape of the entity-and-relationship graph?** [Observed: 22 `data-unknown-disclosure` elements on the retained capture; 13 contain a `data-unknown-reason` value and the literal `Route:` inside their own element; 9 contain neither — the four entity Unknowns and all five relationship Unknowns. Method and offsets in the evidence record.] | **A non-conformance, repaired by slice 1.** POC-REQ-060 is an invariant in force over "every epistemic encoding across the three surfaces" and its falsifier is "one surface encoding Unknown (or Observed) differently from the declared table". Polaris today encodes Unknown two ways on one page: a `data-unknown-reason` span plus a `Route:` sentence for project-shape claims, and a bare free-prose sentence for entities and relationships. The prose comes from `unknown(reason: string)` at `packages/three-surface-poc-core/src/model.ts` line 305, which accepts any string; RFC2-24 closes the reason vocabulary at twelve and says a condition genuinely not among them "is disclosed as a **fact of the render** — named, expandable, routed to its resolving action — never dressed as a reason". Rule it a repair, not a redesign: the nine keep their existing sentences as the *basis* text and gain a closed reason and its route. |
| Q2 | **L5-M4 proposes minting `none-modelled` as a third state so that an empty `resolutionRoutes` array "stops being legal". Mint it?** Disclosed for confirmation: on this packet's measurement the premise does not hold and the value is already declared elsewhere. | **Do not mint it.** Three measured facts. (a) Of the 1,149 objects carrying `resolutionRoutes` in the machine answer, 1,137 are empty and 12 are not — and **every one of the 1,137 is `Observed`, every one of the 12 is `Unknown`, and no Unknown carries an empty array** [Observed: both machine captures, identical]. `routesFor` at `packages/three-surface-poc-core/src/project-shape-model.ts` lines 150–154 returns `[]` exactly when the label is not Unknown, so the empty array is the correct encoding of "not Unknown", not a missing route. (b) Each of RFC2-24's twelve reasons carries a resolution route in the RFC's own table, so an Unknown project-shape claim with no modelled route is unreachable by construction. (c) The state L5-M4 wants **already exists as declared copy**: `label.no-route`, text "No route declared", at `apps/three-surface-poc/src/polaris-copy.ts` line 193, used as the fallback in `routeOf` (line 466) and `reasonRouteHtml` (line 473) of `apps/three-surface-poc/src/polaris.ts`, and listed by name in the copy oracle's `UNREACHED_IN_FIXTURES` set at `apps/three-surface-poc/src/polaris-copy.test.ts` line 299 — a row the oracle asserts is *not* reachable and requires to be removed from that set the moment it becomes reachable. So: forbid an empty array on an Unknown at the type level (slice 2), keep it on an Observed claim, and let the already-declared "No route declared" copy be the render of a route-less Unknown if one ever arises. Minting a third array state would be a fourth vocabulary in a page that already has three. |
| Q3 | **May Syzygy generate a drafted owner-act packet from a gap row, and if so, into whose tree?** The observed repository's write surface is empty and stays empty; Syzygy's own `.syzygy/**` is a lawful write root under VIS-5; but a drafted act about the observed project's gaps would sit in the governance tree of a project that does not govern it. | **Hold slice 7 until this rules; recommended arm is (a) with a narrow new act.** Arm (a): the drafter emits the packet into Syzygy's own `.syzygy/governance/decisions/`, marked `DRAFT, binds nothing`, under a fresh narrow owner direction naming the effect, the claim classes eligible, and a ceiling on drafts. Arm (b): the drafter is pure and emits packet *data* on request, writing no file at all; an operator command renders it. Arm (c): decline. (a) is recommended because v1.md lines 30–31 make first-pass drafting for owner sign-off V0's literal first action on an under-declared project and VIS-4 permits drafting and nothing more — but it is not available without a gate, for two reasons this packet found and neither move stated. First, the adapter registry entry's `typedAuthority.writeSurface` is `[]` and `executeObservedCode` is `false`, and the 2026-09-02 implementation authorization's "What this does not authorize" section reads "No write, egress, execution, deployment, release, recovery, or mission effect on Butlers or on any other repository. The observer registry entry the owner adopted declares an empty write surface; that remains the bound" — so nothing may be written toward the observed project, and the drafted packet's subject is that project's gaps. Second, writing a governance artifact of the observing project *about* the observed project is a new effect no act in force names; the 2026-09-02 act's escalation trigger "any scope beyond the signed change" is the hook. Arm (b) needs no act and is a lawful partial: the pure drafter can be built and tested with no filesystem at all, which is what slice 7 sketches. |
| Q4 | **The opening "what needs you" band: does it list every Unknown reason present, or only the owner-actionable subset?** Both arms are lawful; neither turns anything green. | **Every reason present, with the owner-actionable ones foremost.** L2-M2 proposed a closed actionable subset of four. On the retained capture the whole gap population is **one** reason over 12 claims (`excluded-content`), so a four-reason filter is untestable against today's evaluation and its counterexample test would have no negative case from real data [Observed: `data-polaris-gap` occurs once, `id="polaris-gap-excluded-content"`, and the list's own text reads "12 claim(s)"]. Listing every reason and ordering by the existing `foremost` array in `gapsList` (`apps/three-surface-poc/src/polaris.ts` lines 933–948, already ordering `missing-declaration` then `unconsented-source-or-provider`) reuses a tested ordering, keeps the band's denominator equal to the gaps section's, and needs no second closed constant to drift. The owner may prefer the filter if the band must never show a reason they cannot act on; say so and slice 3 adds the constant. |
| Q5 | **Run the return path once (slice 6): is it authorized, and what may it honestly be expected to produce?** | **Authorized, and it narrows exactly one of the three edges — which is the measurement.** Authorization: the 2026-08-29 owner direction (`.syzygy/governance/decisions/THREE-SURFACE-POC-MODE-DIRECTION.md` lines 18–22) says the experiment "must demonstrate desired intent, human-triggered work, a worker-authored real code/test change, an unverified intermediate state, captured test evidence, verification against the named intent revision, cross-surface navigation, visible Unknown regions, and a machine-queryable view of the same facts", and lists "work dispatch is human-triggered" among the invariants in force; the 2026-08-30 improvement-cycles direction lifts the eight-item and one-review caps for cycle work and requires only that cycle work "trace to POC-REQ-001..061 or to a recorded review finding". Running a built, human-triggered mechanism is an exercise of built capability, not a new effect, and needs no further act. **The honest expectation is the part the dossier overstates.** M4's "Why" says the next evaluation narrows three edges from Unknown to Observed. Measured at `a9f671e`: `relationship:work-to-code` (`model.ts` line 588) and `relationship:code-to-evidence` (line 597) are **unconditional `unknown(...)` literals** — no input reaches them. `workerChange` and `testArtifactVerification` are computed at lines 418–437 and carried as top-level model fields at lines 701–702, and **no relationship reads either** [Observed: a `grep -n` sweep for both identifiers over the file returns lines 30, 42, 124, 125, 418–433 and 701–702, none inside the relationship array]. The reason is deliberate and recorded in the file: `WORKER_CHANGE_SEAM` (lines 25–32) is "distinct from ARTIFACT_PATHS.code/test below", and `WORKER_CHANGE_INTENT_ID` (lines 34–42) is exported so Trajectory can name it "on the one place this evidence is honestly scoped to: the worker-change badge, never the identity-resolution entity graph above" — the same false-`Verified` wiring AGENTS.md records as already reverted once. Only `relationship:intent-to-work` is conditional (line 570, on `materialization.beadId`). So: rule the run authorized, and rule in advance that **one edge narrowing and two staying Unknown is a pass**, recorded as such. |
| Q6 | **`model.surfaces` declares Polaris presents 4 entities; the page presents 415 items and 713 claim tuples. Make the field true by construction, or delete it?** Disclosed for confirmation: deletion has a cost the move does not name. | **True by construction (L6-M4's descriptor), not deleted.** `model.surfaces` is the only place in the shared model that states the surface-to-content mapping, and it is the one field the home page reads: `renderPocPage` (`apps/three-surface-poc/src/routes.ts` lines 77–96) reads `model.surfaces`, `model.project`, `model.entities`, `model.capabilityId` and `model.evaluation`, and nothing else [Observed: a sweep of the literal `model.` over the file yields exactly those five plus one `model.projectShape` at line 127, outside `renderPocPage`]. Deleting it deletes the home page's only input, so deletion and slice 5 are the same change; keeping it and making it derived is the smaller step and lands slice 5's descriptor for free. Note that one of the three entries is **already** derived — Orrery's `entityIds` and `relationshipIds` are `entities.map(…)` and `relationships.map(…)` at `packages/three-surface-poc-core/src/model.ts` lines 745–746 — so the defect is two hand-written lists, not three. |
| Q7 | **Sequencing against M2 (`syzygy-dov.2`, P-69), M3 (`syzygy-dov.3`, P-70) and lane B (`syzygy-dov.17`, P-68), and which M4 slices may start now.** | **Slices 1–6 may start now; slice 7 waits on Q3; slice 8 is deferred behind its own acts.** No M4 slice opens a specification package, so none collides with P-68's pending PWB amendment. The one shared file with M3 is `apps/three-surface-poc/src/polaris-copy.ts`; the one shared file with M2 is none. M4's questions queue as **P-71**: main's last register note at `a9f671e` is P-67, and P-68, P-69 and P-70 exist only on `agent/syzygy-dov.17`, `agent/syzygy-dov.2` and `agent/syzygy-dov.3` respectively, so a reader following this packet's baseline to `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` finds none of the three [Observed: the register on main read this session; its last numbered row is P-53 and its text carries no P-6x row]. |

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

1. **Not one link on any surface points at anything on another surface.**
   Across all four served pages the non-fragment hrefs are, in every case,
   exactly the four global-nav links plus — on Polaris only — the exact-source
   routes: home 40 hrefs (36 fragments + 4 nav), Trajectory 304 (300 + 4),
   Orrery 23 (19 + 4), Polaris 1,089 (699 fragments + 386
   `/polaris/source` routes + 4 nav) [Observed: an `href="…"` attribute
   sweep of the four captures, bucketed by prefix after stripping the query
   string; the three small pages are the pre-lane-A captures and the Polaris
   figure is the retained lane A tailnet capture]. The 2026-08-29 direction
   names cross-surface navigation among the things the experiment "must
   demonstrate"; what exists is a four-item nav bar repeated four times.
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
   pages reports the denominator and zero exceptions.
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
slice keeps dispatch human-triggered, keeps drafting separate from adopting,
and writes nothing to the observed repository. It is not a re-opening of the
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
tag name"]:

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

The dossier reports this state as `walkthroughJudgment.outcome`; the field is
one level deeper, at `walkthroughJudgment.evaluation.outcome`, and carries
the same four values [Observed].

### Source citations re-verified at `a9f671e`

The dossier's line numbers were taken at `f4589e2`. Every one below was
re-read at `a9f671e` this session; where lane A moved it, both are given.

| Citation | At `a9f671e` | Note |
|---|---|---|
| `packages/three-surface-poc-core/src/model.ts` `PocRelationship` | 80–88 | unchanged; the dossier's 80–88 holds |
| …`PocSurface` | 90–96 | unchanged |
| …`unknown()` helper | 305–307 | the free-prose constructor |
| …`workerChange` / `testArtifactVerification` computation | 418–423 / 431–437 | carried to the model at 701–702 |
| …the five Unknown relationships | 562–581, 583–590, 592–599, 601–607, 609–616 | the dossier's "563–598" understates by one line at each end |
| …`surfaces` literal | **710–749**; the file ends at **752** | the dossier's "710–756" overruns the file by four lines |
| …Orrery's derived id lists | 745–746 | `entities.map` / `relationships.map` |
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

This is why the materialize action is lawful — a work-scheduler effect
through a typed adapter, with the observer registry entry declaring
`writeSurface: []`, `databaseAccess: []`, `networkAccess: []`,
`executeObservedCode: false` and `workingTreeRead: false` [Observed: the
`typedAuthority` block of
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`]
— and why Q3 exists: a drafted act file is a write, and the only root it
could lawfully land in is Syzygy's own.

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
  to this RFC". And, three paragraphs on: "A condition genuinely not among
  the twelve is disclosed as a **fact of the render** — named, expandable,
  routed to its resolving action — never dressed as a reason; the honest
  move is to amend this list, never to annotate outside it." The clause's
  own table carries a **Resolution route** column whose twelve cells are,
  word for word, the twelve values of `UNKNOWN_REASON_ROUTES`. So the route
  vocabulary M4 wants to extend to nine more disclosures already exists, is
  already closed, and is already implemented; slice 1 is a widening of
  *coverage*, not of vocabulary. Whether a `PocRelationship` is an "Unknown
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

**Conflict check.** None found. Every slice adds a disclosure or a route, or
removes a hand-written list in favour of a derived one. None turns anything
green, none folds an Unknown into a total, none establishes a claim, and
slice 6's honest expected outcome is that two claims stay Unknown.

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Routes on every Unknown | `packages/three-surface-poc-core/src/model.ts` (a reason-and-route field on `PocEpistemic`'s Unknown arm, populated from a closed table beside the entity and relationship literals); `apps/three-surface-poc/src/polaris.ts` (render through the existing `unknownLine` shape); `apps/three-surface-poc/src/orrery.ts` and `apps/three-surface-poc/src/trajectory.ts` (the same encoding, POC-REQ-060); `apps/three-surface-poc/src/polaris-parity-sweep.test.ts` (the denominator grows) | none |
| 2 The machine form of a route | `packages/three-surface-poc-core/src/project-shape-model.ts` (widen `ResolutionRoute`, keep `route` verbatim as the prose field); `packages/three-surface-poc-core/src/model.ts` (the same type on the relationship arm) | none |
| 3 The opening band | `apps/three-surface-poc/src/polaris.ts` (a second rendering of `gapReasonCounts`, reusing `gapId`), `apps/three-surface-poc/src/polaris-copy.ts` (the band's own copy rows) | none |
| 4 `model.surfaces` true by construction | `packages/three-surface-poc-core/src/model.ts` lines 90–96 and 710–749; each renderer imports its descriptor | none |
| 5 Home as the day-opening | `apps/three-surface-poc/src/routes.ts` lines 34–96, `apps/three-surface-poc/src/exact-tables.ts`, `apps/three-surface-poc/src/routes.test.ts` | none |
| 6 Run the return path once | no source file; `docs/evidence/` gains one record | none |
| 7 Drafted-act generator | a new pure module in `packages/three-surface-poc-core/src/`; an operator entry point beside `apps/three-surface-poc/src/capture-test-artifact-main.ts`; `scripts/check_governance.py` registration | **potentially `.syzygy/governance/decisions/`** — the output, see Q3 |
| 8 (deferred) Packet per claim; the queue | `packages/three-surface-poc-core/src/materialization.ts` lines 9–65 | none directly; the effect is new |

Boundaries crossed: none new. Slice 1's route table sits beside the
relationship and entity literals in the same module that already constructs
them; slice 2 widens a type `packages/three-surface-poc-core` already owns.
Slice 7 is the only slice that would give the core package a filesystem
dependency, and the design keeps it pure precisely so it does not.

Not touched by any slice: the body-read authority gate, the observation
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
| 4 `model.surfaces` | **No** | Same continuation. **No requirement governs this field** (Gate 5), so it traces to the recorded-finding arm of the 2026-08-30 direction, naming L6-F5 |
| 5 Home as day-opening | **No** | Same continuation, on the same recorded-finding arm naming L6-F1. Q5's confirmation is what makes that arm explicit rather than assumed |
| 6 Run the return path once | **No** | `.syzygy/governance/decisions/THREE-SURFACE-POC-MODE-DIRECTION.md` lines 18–22 name the demonstration; the same file's invariant list (lines 26–32) keeps dispatch human-triggered; `THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md` lifts the item and review caps for cycle work. The run adds no mechanism, reads no new source, and writes only to the work scheduler through the adapter the 2026-09-02 act's own prohibition list already contemplates. Q5 puts the reading to the owner rather than assuming it |
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
RFC2-24's twelve and each route from that clause's own Resolution route
column:

| Disclosure | Proposed reason | Route (RFC2-24's own words) |
|---|---|---|
| work:whatsapp-single-event-normalization | `missing-evidence` | Produce/capture evidence |
| evidence:focused-pytest | `missing-evidence` | Produce/capture evidence |
| runtime:live-satisfaction | `missing-evidence` | Produce/capture evidence |
| region:unmapped-code | `mapping-coverage-absent` | Run/declare the mapping |
| relationship:intent-to-work | `missing-evidence` | Produce/capture evidence |
| relationship:work-to-code | `missing-evidence` | Produce/capture evidence |
| relationship:code-to-evidence | `missing-evidence` | Produce/capture evidence |
| relationship:code-to-runtime | `missing-evidence` | Produce/capture evidence |
| relationship:capability-to-unmapped-region | `mapping-coverage-absent` | Run/declare the mapping |

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

**Tests.** A served-page sweep over all three surfaces: every element
carrying `data-unknown-disclosure` must carry a `data-unknown-reason` whose
value is one of the twelve, and either a route sentence or the declared
`label.no-route` copy; the sweep reports its denominator (22 on the retained
capture's population). Rule-6 mutants: blank one disclosure's reason and
confirm the sweep fails; change one reason to a thirteenth value and confirm
it fails; delete the `actionRoute` and confirm the capability-detail test
fails.

### Slice 2 — The machine form of a route (medium; no act)

`ResolutionRoute` becomes
`{ reason, prose, actor, verb, target }`, where `prose` carries today's
string **verbatim** so no rendered sentence changes, `actor` is one of
`owner | operator | agent`, `verb` is a short closed set, and `target` names
what the action is aimed at (an artifact path, an act identity, a policy, an
evaluation, or external work). The same type goes on the relationship arm,
so one widened type serves slice 1 and slice 2 — L5-M4's own note that the
two moves should build the type once, not twice.

**What the slice does not do, per Q2.** It does not add a `none-modelled`
value. It makes the empty array unrepresentable on an Unknown at the type
level, leaves it as the only legal value on an Observed claim, and leaves
`label.no-route` where it is. If the owner rules the other way on Q2, the
slice mints the value and the copy oracle's `UNREACHED_IN_FIXTURES` entry at
`apps/three-surface-poc/src/polaris-copy.test.ts` line 299 must be removed
in the same change, or the oracle will assert the row is still unreachable
and fail.

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
(`packages/three-surface-poc-core/src/model.ts` lines 745–746). A served-page
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

The last two rows are the point. The dossier's M4 text expects three edges
to narrow; the code says one will, and says why in its own comments at
`model.ts` lines 25–42: the worker-change seam and its intent are
deliberately distinct from the identity-resolution graph, and wiring one
into the other is the false-`Verified` change AGENTS.md records as already
reverted once. **The honest result of the run is therefore a record that one
edge narrowed, two did not, and the two that did not are correctly
scoped elsewhere** — which is itself the strongest available evidence that
the model does not manufacture propagation. Q5 asks the owner to rule that
this counts as the demonstration before the run, not after.

**What is retained.** The daemon stderr (the fresh-checkout verdict requires
it empty), the `TestArtifactRecord`, the before/after machine captures, and
the before/after tuple for all five Unknown relationships. Per v1.md lines
116–119 the V0 agent-consumption artifact is "the named workflows and the
commits/sessions that used them", and the criterion says "a workflow written
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

**Neither arm writes toward the observed repository.** The registry entry's
write surface is empty and stays empty.

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
lines 927–945:

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
> - **Falsifier**: one surface encoding Unknown (or Observed) differently
>   from the declared table, or a surface styling epistemic state ad hoc.

Nine disclosures encoding Unknown as bare prose while thirteen encode it as
a reason span plus a route is one surface encoding Unknown two ways, which
is the falsifier's first limb. The spec already requires the repair.

Slice 2 is POC-REQ-020 and PWB-REQ-020 conformance. PWB-REQ-020 is quoted
verbatim from
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
lines 902–926:

> Every project-shape identity, statement, source anchor, coverage state,
> denominator, contradiction, body-read authority state and
> walkthrough-judgment state or disclosure Polaris presents SHALL be
> recoverable from the same evaluation in the machine answer, preserving
> multiplicity and exact provenance state.
>
> - **Observable**: both populations contain equivalent multisets.
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
verbatim from lines 490–498 of the same file:

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
findings L6-F1 and L6-F5. Q5 puts that reading to the owner. The
consequence a reviewer should see: changing the home page freely is lawful
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
pages reports its denominator and zero exceptions.

**S2 — The one available action is reachable from the Unknown that names
it.** WHEN `relationship:intent-to-work` renders Unknown because the
materialization step has not run, THEN its disclosure carries a link to the
materialize panel, mount-prefix correct on both host forms, AND following
that link writes nothing and changes no model field.

**S3 — An empty route array never means an unrouted Unknown.**
WHEN a claim or relationship is labelled Unknown, THEN its resolution-route
array is non-empty, AND when it is labelled Observed, THEN the array is
empty; a type-level test and a machine-answer sweep assert both directions
with their denominators.

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

**With M2 (`syzygy-dov.2`, register row P-69, PR #36).** M2's six slices
touch `apps/three-surface-poc/src/polaris-copy.ts` (the four freshness
sentences), `apps/three-surface-poc/src/polaris.ts` line 357
(`claimStatesBlock`'s freshness group),
`apps/three-surface-poc/src/git-observation.ts`,
`apps/three-surface-poc/src/main.ts`,
`apps/three-surface-poc/src/polaris-reading.ts`,
`packages/three-surface-poc-core/src/model.ts`'s evaluation block,
`packages/three-surface-poc-core/src/project-shape-model.ts` lines 162–193,
and the adapter registry entry. **M4 touches none of those regions.** The one
shared file is `packages/three-surface-poc-core/src/project-shape-model.ts`,
where M2 rewrites the freshness constant at lines 162–193 and M4 slice 2
widens `ResolutionRoute` at lines 115–118 and `routesFor` at 150–154 —
adjacent, not overlapping. The one shared *concept* is M2's `evidence` block
on the machine payload and M4's route fields: both grow `/api/poc`, and both
must land in the parity sweep's denominator rather than forking it. **M2's
Q7 and M4's Q2 are the same shape of question** — what an implementation
does when a closed vocabulary has no member for a state — and the owner
should notice that this packet recommends *not* minting where M2 recommends
choosing an existing value; the two recommendations are consistent, and both
turn on RFC2-10's and RFC2-24's identical "never dressed as" sentence.

**With M3 (`syzygy-dov.3`, register row P-70).** M3's slice 5 generates the
freshness, tier and challenge encoding tables and its slice 6 adds a
render-disclosure family; both touch
`apps/three-surface-poc/src/polaris-copy.ts` and
`apps/three-surface-poc/src/polaris.ts` lines 346–361. M4 slice 1 adds a
reason and a route to nine disclosures and M4 slice 3 adds band copy rows —
in the same two files, in different functions. **The real overlap is M3's
"one declared encoding table" and M4's "nine disclosures that do not use
it".** They are the same finding from two sides: M3 builds the table, M4
supplies the nine rows that must be in it. **M3 should land slice 5 before
M4 slice 1**, so slice 1 populates a generated table rather than a
hand-written one; if M4 goes first, M3's table must absorb nine rows it did
not plan for. This packet recommends M3 slice 5 first and says so in the
handoff.

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

**The order.** (1) Rule P-68; open no spec package meanwhile — M4 opens
none, so this does not gate it. (2) M3 slice 5, then M4 slice 1 and slice 2
together, since they share the widened type. (3) M4 slice 3, then slice 4,
then slice 5 — the home page is the composition of the two before it and
should be built last. (4) M4 slice 6 at any time; it is independent of
everything above and its value is highest early, because its result is an
input to every later judgment about whether the loop works. (5) Slice 7 only
after Q3; slice 8 only after its own acts.

## Gate 6 — Engineering bar

Acceptance, in the M1, M2, M3 and P-63 shape:

1. **Retained measurement, before and after**, direct and tailnet host
   forms, at a named Syzygy commit and Butlers revision, in `docs/evidence/`,
   from a private daemon on port 0 with its own state directory, never the
   loopback daemon, on a committed clean tree. Note the constraint recorded in
   AGENTS.md: the daemon serves only the registered locator, so a repaired
   Butlers page cannot be measured from a scratch clone. The M4 numbers to
   record: the disclosure census with its denominator (22 today, 13 routed),
   the href census per surface with its buckets, the home page's byte size
   and composition, the band's byte cost, and the page's byte size on both
   forms against the 1,400,000-byte working target and the 2,097,152-byte
   ceiling.
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

## Funnel summary

```
## Feature Request: M4 - Close the owner loop: a route from every Unknown, home as the day-opening, and run the return path once
Size: medium (slices 1-6) / large (slice 7, and the deferred slice 8 pair)
Baseline: Syzygy a9f671e; capture = lane A after/tailnet, 1,484,487 bytes, Butlers 2e3bac97790b
- G1 Motif: 9 of 22 rendered Unknowns carry no closed reason and no route; zero cross-surface deep links on any of four pages; the product's one submit button sits at 99.1% of the second page [Observed: five capture sweeps, denominators stated]
- G2 Doctrine: aligned - VIS-1 (aggregate Unknowns, never substitute), VIS-2, VIS-4 (draft, never adopt - stated per slice), VIS-5 (two write roots; empty write surface on the observed repo), vision.md 61-64 the escape property (unnumbered doctrine prose), RFC2-24's closed twelve and its own Resolution route column
- G3 Topology: apps/three-surface-poc + packages/three-surface-poc-core; no new boundary; no governed artifact touched by slices 1-6; slice 7's output is the only write and it is gated
- G4 Design: closed reason + route on all nine unrouted Unknowns, with the materialize link on the one edge that has one; a machine route form with actor/verb/target and no new array state; an opening band from the existing gaps projection; model.surfaces derived; home rewritten as their composition; the return path run once; a pure act drafter
- G5 Spec: no delta - POC-REQ-060 already requires slice 1, PWB-REQ-020 already requires slice 2's parity; PWB-REQ-004 untouched; and NO requirement governs the home route or model.surfaces, so slices 4-5 trace to recorded findings L6-F1/L6-F5
- G6 Bar: retained before/after measurement, rule-6 mutants per guard branch, both parity sweeps with both denominators, independent review
Acts: slices 1-6 none (the 2026-09-05 continuation; slice 6 additionally the 2026-08-29 direction lines 18-22 and the 2026-08-30 improvement-cycles direction); slice 7 one narrow act on arm (a), none on arm (b); slice 8 two acts, deferred; a poller: none found and none sought
Open questions: Q1-Q7 above; queued as P-71 (P-68 lane B, P-69 M2, P-70 M3, each on its own branch)
Sign-off: pending - the owner's
Recommended handoff: Q1 "a non-conformance" and Q2 "do not mint none-modelled" -> run slices 1 and 2 together after M3 slice 5; then 3, 4, 5 in order; run slice 6 independently and early; hold slice 7 for Q3 and slice 8 for its acts
```

## Recommended handoff

**If Q1 and Q2 are answered as recommended:** file no new bead. Build slices
1 and 2 as one change under `syzygy-dov.4`, after M3's slice 5 lands so the
nine new rows populate a generated encoding table rather than a hand-written
one. Slice 1 alone closes the POC-REQ-060 breach that L2-F2 and L6-F5 named
and puts the product's one action one click from the Unknown that describes
its absence.

**If Q4 is answered as recommended:** slice 3's band lists every reason
present, ordered by the existing `foremost` array, and its total is asserted
equal to the gaps section's on every fixture. If the owner prefers the
four-reason filter, the slice adds one closed constant and one counterexample
fixture, and the packet's warning stands: today's evaluation cannot exercise
the filter's negative case.

**If Q5 is answered as recommended:** run slice 6 early and independently of
everything else, and record its result honestly — one edge narrowed, two
correctly did not. That record is the V0 agent-consumption artifact v1.md
lines 116–119 asks for, and it is also the only evidence anyone will have
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
