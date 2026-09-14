# Feature request M3 — Honest encoding at the gate: POC-REQ-060 on Polaris and a real sweep

> **Candidate — binds nothing.** This is the feature-request funnel for the
> third move released from the 2026-09-13 vision pursuit. It proposes; the
> owner disposes (VIS-4). Nothing here authorizes implementation, and no bead
> becomes runnable by this file. Bead: `syzygy-dov.3`. Dossier:
> `docs/pursuits/2026-09-13-vision-pursuit.md`, section M3. It is written in
> the shape of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`, of the ruling
> that packet produced
> (`.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`),
> and of the M2 packet on branch `agent/syzygy-dov.2`.

Date: 2026-09-14. Author: a funnel session (Claude), for the owner.

Size: **medium** for slices 1–4 (the Polaris renderer, its CSS, one checker
and one fixture; observable behavior changes; no governed artifact touched);
**medium–large** for slices 5 and 6 (they declare encoding tables, which
CC-VIZ-1 makes legend-bearing, and they touch the shared token set every
surface imports).

Baseline: Syzygy `a9f671e` (main; the worktree branches from `a9f671e`, and
the only commits on it are this packet's own artifacts, so every source
citation below is at the baseline bytes; the only pre-existing working-tree
change on main is a co-lead's in-flight `AGENTS.md`, unrelated) [Observed;
corrected after review 3, finding H8, which replaced an "at the same
commit" claim with a two-commit enumeration, and generalised after review 4,
finding J8, because that enumeration was itself one commit stale by the time
it was reviewed — no count of the packet's own commits is stated; `git log
--oneline a9f671e..HEAD` in the worktree lists them]. The retained capture
this packet measures is the lane A *after* capture, tailnet host form, at
Butlers evaluation revision 2e3bac97790b, committed 2026-09-13T10:31:11Z and
captured 2026-09-13T13:33:24.295Z: 1,484,487 bytes, sha256
`e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111`
[Observed: recomputed this session with `sha256sum`, identical to the digest
recorded in the M2 evidence file of the same date, which exists only on
branch `agent/syzygy-dov.2` and so is named here in prose rather than as a
path this clone can resolve; every count below is recorded beside this file
in `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`].

**Line numbers.** Lane A moved the Polaris renderer. Every `file:line`
citation below was re-verified at `a9f671e` this session; where the dossier's
figure differs it was taken at `f4589e2` and both are named.

## The seven questions for the owner

Batched, each with the recommended answer first. Everything below is the
evidence behind them. Q1, Q2, Q4, Q5 and Q6 are owner gates in the strict
sense: Q1 rules whether today's page is conformant or in breach, Q2 settles a
contract reading no agent may settle, Q4 decides what the owner's first stop
opens with, and Q5 and Q6 decide how far the declared encoding table reaches.
Q3 and Q7 order this move against two queued owner decisions and are put as
choices because both arms are lawful and they change a figure already in
front of the owner.

| # | Question | Recommended |
|---|---|---|
| Q1 | **Is Polaris's present rendering of epistemic state a non-conformance with POC-REQ-060, or does that requirement's "epistemic encoding" reach only the two declared badge spans?** On the retained capture Polaris renders 735 body epistemic encodings and **0** of them carry a declared encoding *class*; the two spans that do are both inside the page legend, at 99.96% and 99.97% depth. Split by treatment, because the single figure flattens two different defects [Observed, re-derived this session over the capture]: **713 of the 735 — the claim tuples — carry no declared class and no distinguishing treatment at all**, rendering Observed and Unknown in one colour (`var(--muted)`); the remaining **22 are `unknown-disclosure` blocks, which carry the declared Unknown *token* under an undeclared class** (`.unknown-disclosure { color: var(--unknown); border-left: 3px solid var(--unknown); … }`) — visually distinct already, but styled by hand rather than from the table, and carrying no legend entry. The requirement's Falsifier names "a surface styling epistemic state ad hoc" [Observed: quoted at Gate 2]. | **A non-conformance, disclosed and repaired by slices 1 and 2.** POC-REQ-060's Case fixes the population itself — "every epistemic encoding on all three surfaces — the denominator is that population" — and the checker carrying the identifier uses a denominator of 4, against 1,052 body encodings on the requirement's own three surfaces (735 of them on Polaris, 69.87%), or 1,087 over the four pages this packet sweeps (67.62%; the sweep adds Home deliberately because it imports the token set slices 5 and 6 change — the requirement's denominator is the three-surface one) [Observed]. Verification rule 4 (read a check's output, not its exit code, and check its denominator against the whole population) is the project's own name for this defect. Rule it a breach to be repaired in the implementation, **not** a reading under which the page is already conformant; no spec text changes either way (Gate 5). The 713/22 split sharpens the finding rather than softening it: the 22 are the Falsifier's ad-hoc limb in its purest form — the declared token applied outside the declared table, with no legend row — and the 713 are the population that renders indistinguishably. |
| Q2 | **The renderer mints `unstated` into two closed-vocabulary fields, not one.** `apps/three-surface-poc/src/polaris.ts` lines 306–307 read `const tier = claim.epistemic.tier ?? 'unstated';` and `const freshness = claim.epistemic.freshness ?? 'unstated';`. On this capture the tier twin fires 11 times and the freshness twin fires 0 (all 713 tuples carry `fresh`) [Observed] — but the governing clauses differ, and the freshness one is stricter. RFC2-25 closes the tiers at six and supplies a *rendering* remedy for absence, inside the tuple ("an untier'd claim renders at its bare label"); RFC2-10 closes freshness at four, forbids the minting in terms ("no implementation may mint, spell, or force-fit a freshness value it does not carry"), and separately supplies a *disclosure* remedy of its own, outside the freshness slot ("a condition genuinely outside the four is disclosed as a fact of the render, never dressed as a freshness state" — quoted in full in Gate 2). Arm (a): out-of-vocabulary — drop the value and render the bare label. Arm (b): an explicit *absence* marker — the field is present and says no value applies — distinct from the closed set and never an extra row of any encoding table. Arm (c): amend PWB-REQ-007 to provide for it. | **Arm (b) for the tier field. For the freshness field, three lawful arms follow from RFC2-10's own text, and the owner should choose among them — none is unlawful.** For tier: (b) is what the page already does in substance (the glossary reads "unstated — no tier applies to an Unknown that has no evidence"), it keeps PWB-REQ-007's "carry the closed label, tier … that govern it" satisfied with a present field, and it keeps RFC2-25's six closed; (a) would drop a field PWB-REQ-007's Falsifier calls absent, and (c) is a spec amendment that collides with lane B head-on (Q7). The tier encoding table therefore gets **six** rows and one absence treatment, never seven. For freshness the tier reasoning does not carry: RFC2-10's prohibition is on minting, spelling or force-fitting *any* value the closed four do not carry, so a rendered `unstated` in `data-epistemic-freshness` is the forbidden act itself. Three lawful arms follow: **(b-i)** the renderer supplies one of the closed four (M2's Q7, recommending `stale` with the reason kept distinct); **(b-ii)** the claim is held Unknown and the tuple is not rendered as though it had a freshness state; or **(b-iii)** the condition is disclosed as a fact of the render, in a carrier that is not `data-epistemic-freshness` and is not dressed as a freshness state — RFC2-10's own remedy (Gate 2). There is a live, unresolved tension between (b-ii)/(b-iii) and PWB-REQ-007's Falsifier ("a tuple field is absent/out of vocabulary") and its SHALL ("carry the closed label, tier … that govern it", spec :443–446): does a freshness-governed field require a value in `data-epistemic-freshness` even when no freshness state genuinely governs the claim, or does RFC2-10's disclosure route discharge the obligation outside that slot? **This is the owner's question; this packet does not resolve it.** [Inferred] recommendation: **(b-iii)**, the arm RFC2-10's own text supplies for exactly this condition, keeping the freshness table at four rows and no absence row without contradicting the clause that closes it — but (b-i) is a live, lawful alternative (M2's Q7 already recommends it for the specific `no-bound-declared` case) and (b-ii) remains available if the owner reads PWB-REQ-007's SHALL as tolerating an unpopulated field under a disclosed condition. Either way the freshness table gets **four** rows and no absence row, and slice 5 must assert over the *renderer*, not over the table. The mint fires 0 times today and is one branch away from firing on every unbounded class (Gate 2). **M2's Q3, Q5 and Q7 rest on this same RFC2-10 sentence** (quoted there against its own Q7), so P-69 and P-70 must be read together (collision section). |
| Q3 | **Does the per-claim encoding ride an attribute lane B may hoist away, or a carrier lane B may not touch?** Lane B's container-mode estimate hoists `data-epistemic-label` off **409 of 713** tuples [Observed: `hoistedPerField` in the lane B estimate record on `origin/agent/syzygy-dov.17`]. A CSS rule or a sweep keyed on that attribute at the tuple would then see a population of 304 and fail nothing. Arm (a): the encoding inherits through the scope, with a descendant rule, so lane B keeps the hoist. Arm (b): the label becomes a non-hoistable per-claim carrier, costing lane B at least 409 × 32 = **13,088** attribute bytes of its 188,902-byte estimate. | **Arm (a), inheritance — designed in now, not retrofitted.** It preserves the saving already in front of the owner as P-68, and lane B's own amended text supplies the inheritance rule the CSS and the sweep would both read ("a claim's value for a field it does not carry itself is the value of the nearest enclosing scope that carries the field"). The cost is a discipline: **every sweep M3 writes must expand scopes before counting**, and slice 2's denominator must be asserted equal to the tuple count, so a silent drop to 304 fails loudly. Arm (b) is available and honest but spends a ruling the owner has not yet made. |
| Q4 | **Does the opening band render a real Unknown in place?** No rendered Unknown of any kind appears in the first reading: over the four opening groups (document start to the first catalog group, 19.03% of the page) there are 126 claim tuples, **all Observed**, and **0** Unknown-disclosure blocks; the first rendered Unknown is at 25.55% depth and the whole-shape Unknown — the claim that Butlers' shape is not fully known — is at 57.72% [Observed]. | **Yes: surface the whole-shape Unknown and the one class-level Unknown in the opening band, in place, with their routes.** Nothing is fabricated — both claims already exist on the page and are merely late. CC-VIZ-3 forbids a "clean" default view that presents a fully-green project over a half-observed one; by analogy — its own subject there is a superseded observation record, not an Unknown — `trust-and-evidence.md`:101 puts staleness "on the primary surface, not buried in drill-down" (review 2, G8). The alternative the owner may prefer — leave the opening band positive and let the catalogs carry it — is coherent but makes the page's own first impression the least honest part of it. |
| Q5 | **Does the declared encoding table extend from the two epistemic labels to tier, freshness and challenge?** Twelve tier/freshness/challenge states are defined in prose in one collapsed disclosure and **none** has a colour, badge or icon; the glossary carries 15 state sentences and **9** of them describe values no tuple on this capture carries [Observed]. | **Yes — extend it, and generate the glossary from it.** CC-VIZ-1 requires every visual encoding to declare "a legend stating exactly what it means", and generating both directions from one table is the only way a legend entry and a live encoding cannot drift (which is POC-REQ-061's falsifier, "a legend entry matching no rendered encoding", and its mirror). Three constraints ride on the answer: the tier table gets six rows plus Q2's absence treatment; the freshness table gets the four RFC2-10 closes it at, with **no** absence row and a guard that fails if the renderer emits a fifth value (Q2's freshness limb — the closure must be asserted over the rendered output, not over the table, or it cannot see line 307); and unreachable values are **marked in place, never deleted** — which is M2's ruling shape, so slice 5 must rebase onto M2's markers rather than replace them (Q7). |
| Q6 | **Does the page's proposal disclosure get a token of its own, out of the Unknown token's way?** On the retained capture the sentence "Proposed change — not current authority." renders **once**, at 56.29% depth, in `var(--unknown)` — the token the page's own legend declares to mean "? Unknown … No verifying evidence exists yet" [Observed]. Five CSS rules use that one token for four declared meanings, of which two render zero times here (`class="unavailable-notice"` 0, `class="proposal"` 0); the live reuse is 22 `unknown-disclosure` blocks and 1 proposal label beside the legend's 2 declared Unknown badges [Observed: literal counts this session]. **What this question does not ask.** It adds no member to any closed vocabulary. RFC2-25 closes the epistemic labels at three, the rendering tiers at six, and the sibling surface states at three: "*Deliberately outside the registry — **three** sibling surface states, closed:* `dismissed-by-decision`, `unadopted-draft` and `editorial-draft`" (`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`:169, quoted verbatim with the source's own emphasis). The capture renders **0** occurrences of each of those three, and 0 of `challenge-pending` [Observed: literal counts, denominator the whole 1,481,819-character page]. The proposal treatment is **not** one of them and is not proposed as a fourth: it is a render disclosure of narrative provenance. An earlier draft of this packet framed Q6 and slice 6 as a sibling-state family and attributed to RFC2-25 a phrase it does not contain; review 1 (F3) was right that as written it pointed an implementer at a closed three-member vocabulary. | **Yes — a `--proposed` token, declared as a render-disclosure encoding, at a stated perceptual distance.** VIS-7's "every encoding means what its legend says" is falsified today by one sentence a reader can point at, and RFC7-34 is its Polaris-binding form. The new family is a **fourth declared encoding table** — render disclosures — and mints nothing: no fourth epistemic label (RFC2-25: "a tier never becomes a fourth epistemic label"), no seventh tier, no fourth sibling surface state. Contradiction is **not** in this family: a contradicted item renders tier `suspended`, one of RFC2-25's six, and slice 4's fixture is what makes it render — that belongs to slice 4 and the tier table, not here. The measurable bar slice 6 must clear, with its population named: over the five tokens carrying foreground meaning, `--amber` ↔ `--unknown` at ΔE76 **7.85** is the smallest pair and `--muted` ↔ `--ink` at **26.74** the next, so a new foreground token must sit ≥ 26.7 from `--unknown` and meet POC-REQ-061's AA contrast on both page grounds. That floor holds over the foreground population only: over the full declared set of nine distinct colours the smallest pair is 3.98 and seven pairs sit below the `--ink`↔`--muted` floor (26.74 to two decimals, 26.7371 computed), because the ground tokens are adjacent by design (Measurements). Alternative arm: keep one token and legend the reuse explicitly — lawful under CC-VIZ-1, but it asks the reader to hold four meanings for one colour. |
| Q7 | **Sequencing against M2 (register row P-69) and lane B (P-68).** M3 slice 5 generates the freshness glossary that M2 slice 1 marks by hand; both edit `apps/three-surface-poc/src/polaris-copy.ts` freshness sentences and the block at `apps/three-surface-poc/src/polaris.ts` lines 346–361 (`claimStatesBlock`), whose freshness group — the exact collision — is line 357. | **M2 first, then M3 slices 1–4 in parallel with P-68, then M3 slices 5–6.** M2's packet is further along (six reviews retained, M2 at `f2f37dd` with review 6 CONFIRM WITH EXCEPTIONS; the earlier "five" corrected after review 6, L3, from the M2 worktree's `docs/reviews/` listing) and its markers are the *content* slice 5's table must carry; reversing the order means M3 generates a glossary M2 then hand-edits, and the copy oracle is written twice. Slices 1–4 touch none of those bytes and may run at any time. **No M3 slice opens a PWB specification package until P-68 is ruled** — and on the recommended answers none needs one at all. M2's Q3, Q5 and Q7 and this packet's Q2 all turn on the same RFC2-10 sentence (Gate 2; collision section), so P-69 and P-70 should be ruled together, not independently. |

## Gate 0 — Baseline

| Pillar | Present | Constrains this request |
|---|---|---|
| Doctrine (heart-and-soul) | Yes, adopted: VIS-1…7, SEC-1…5 | VIS-2 (no evidence means Unknown, never success), VIS-7 (every encoding means what its legend says), VIS-1's "comprehension is achieved by simplifying presentation, never content" |
| Decisions (legends-and-lore) | Yes | P-52 (the eight-item POC cap — M3 runs under `syzygy-dov.3`, so no new POC bead is filed); the M1 ruling's Q3 restated 1.4 MB target; P-68 and P-69, both queued on their own branches and unruled |
| Specification (openspec) | Yes, signed and digest-bound: `openspec/changes/three-surface-poc-experience/` and `openspec/changes/polaris-project-wide-butlers-model/` | POC-REQ-060 (the declared encoding and its sweep), POC-REQ-061 (the accessibility floor and legend-to-encoding comparison), PWB-REQ-007 (the complete tuple and its fixture Case), PWB-REQ-010 (the first reading), PWB-REQ-016 (comprehension without vision), PWB-REQ-020 (parity) |
| Contracts | Yes, RFC 0001–0009 accepted | RFC2-25 (six tiers, closed), RFC7-34 (non-visual recoverability; visual encodings are legended), RFC7-28 (speculated structure never looks like existing structure). RFC 0009's `applies_to` is `[orrery, machine-clients]`, so RFC9-24/27 do not bind Polaris directly — see Gate 2 |
| Topology (lay-and-land) | Candidate bundle only | Nothing beyond the core-versus-app placement already in force |
| Craft (craft-and-care) | Yes, owner-approved | CC-VIZ-1 (every encoding declares its legend), CC-VIZ-3 (Unknowns visible, never disappeared), CC-TEST-5/6 oracles, rule-6 mutation evidence, retained evidence, independent raw review |

## Gate 1 — Motif

**Problem.** Polaris carries two thirds of the POC's epistemic encodings and
is the only surface whose body encodings draw on none of the declared encoding
*classes*; where the declared Unknown *token* does appear in the body, on the
22 disclosure blocks, it appears under an undeclared class with no legend
entry. On the retained
capture, 713 claim tuples — 702 Observed and 11 Unknown — render through a
**single** CSS rule, `.claim-tuple { … color: var(--muted) … }`, with no
selector anywhere in the served stylesheet keyed on `data-epistemic-label`,
`data-epistemic-tier`, `data-epistemic-freshness` or `data-challenge-state`
[Observed: every rule in the one served `<style>` block parsed this session;
four literal probes each return 0]. The declared table the surfaces are meant
to import — `● Observed` in cyan, `? Unknown` in amber on a tint — is used
exactly twice on the page, and both uses are inside the legend in the footer.
Meanwhile the checker that carries the POC-REQ-060 identifier sets
`denominator = pages.length` and counts a page "consistent" on a
`String.includes` that the legend alone satisfies.

**The dossier's M3 findings, re-measured on the lane A capture.** L6-F3 said
688 Observed and 11 Unknown claims render in one grey against a checker
denominator of 4 pages and a population of 1,085. Re-derived 2026-09-14 on
the retained lane A capture: **702 Observed and 11 Unknown, 713 tuples, one
colour treatment, denominator still 4**, and the cross-surface body
population is **1,052** over POC-REQ-060's three surfaces and **1,087**
over the four pages this packet sweeps, under a stated predicate (review 4,
J4). The kind is unchanged; the
counts moved because lane A changed what Polaris renders. The three
non-Polaris figures come from the 2026-09-13 fresh captures at `f4589e2`,
which is pre-lane-A; `git diff f4589e2..a9f671e` over `apps` and `packages`
changes no home, Trajectory, Orrery, `page-shell.ts` or `design-tokens.ts`
source, so those three renderers are unchanged at `a9f671e` and only their
model data is one Butlers revision older [Observed].

**Who.** The owner, for whom PWB-REQ-021's cold open asks how strongly
Polaris claims to know a chosen fact — a question whose first visual answer
on this page is the same grey for a claim backed by a read source and a claim
backed by nothing; the reader who leaves the first reading having met the
word "Unknown" fourteen times and a rendered Unknown zero times; and every
later reader of a page whose legend promises a distinction the body never
draws.

**Success, falsifiable.**

1. Every epistemic encoding rendered on any surface carries a class from the
   declared table, and a sweep whose denominator is that population — not the
   page count — says so and reports the number.
2. Observed and Unknown are distinguishable on Polaris by at least two
   carriers that are not colour alone, and the distinction survives the
   scope-inheritance rule lane B proposes.
3. A reader who stops at the end of the first reading has met at least one
   rendered Unknown in place, with its route.
4. The item-level Unknown route renders at least once under test, against a
   fixture that does not depend on live Butlers content.
5. Every tier, freshness and challenge value the page renders carries a
   declared visual treatment, and every treatment has a legend entry, both
   generated from one table; unreachable values are marked, not deleted.
6. No two tokens carrying different meanings sit closer than the stated
   perceptual threshold **over a stated population** — the tokens that carry
   foreground meaning, ground tokens excluded and the exclusion named — and
   the full pairwise matrix is in the evidence record.

**Motif.** *A legend that promises a distinction the page never draws is an
unfaithful encoding, and a checker whose denominator is the number of pages
cannot see it.* This is VIS-7's own violation clause applied to the surface
that carries most of the POC's claims, and verification rule 4 applied to the
check that carries the requirement's identifier.

**What M3 is not.** It is not a claim that any tuple is *wrong*: every label,
tier and reason on the page is earned, and the machine channel carries them
all. It is a claim that the page renders them indistinguishably. It is not a
re-opening of the page-size question either, though it must state that
question's arithmetic honestly [Observed, computed this session]: the page at
the retained capture is 1,484,487 bytes on the tailnet form, which is
**84,487 bytes over** the M1 ruling's 1,400,000-byte working target and
612,665 bytes under the 2,097,152-byte response ceiling, of which 418,000 to
443,000 bytes are reserved for the pending Butlers P-60/P-61 repairs. The
recommended slice 1 design adds bytes measured in hundreds, not thousands
(Gate 4); the per-tuple alternative would add 16,366 and is not recommended.

## Measurements on the retained capture

All computed this session from the lane A tailnet capture named above
(1,484,487 bytes; 1,481,819 decoded characters) [Observed]. Counts are
computed, never transcribed; every sweep is Python `re` or a literal
`str.count`, never shell grep (verification rule 1).

| Measure | Value | Denominator |
|---|---|---|
| Claim-tuple spans on the page (three methods agreeing: span-open regex, literal split, `class="claim-tuple"` count) | 713 | the page |
| …over distinct claim ids (10 ids render twice) | 703 | 713 |
| `data-epistemic-label` values rendered | Observed 702, Unknown 11 | 713 |
| `data-epistemic-tier` values rendered | `report-fact` 702, `unstated` 11 | 713 |
| `data-epistemic-freshness` values rendered | `fresh` 713 | 713 |
| `data-challenge-state` values rendered | `unchallenged` 713 | 713 |
| Distinct tuple shapes | 2 | 713 |
| **CSS rules whose selector names `.claim-tuple`** | **2** (the base rule and one mobile override changing only `letter-spacing` and `font-size`) | the one served `<style>` block |
| **Distinct colour treatments over the 713 tuples** | **1** (`color: var(--muted)`, #8ca3a4) | 713 |
| CSS selectors keyed on `claim-tuple[`, `[data-epistemic-label`, `[data-epistemic-tier`, `[data-epistemic-freshness`, `[data-challenge-state` | 0, 0, 0, 0, 0 | the served stylesheet |
| Declared-encoding badge spans on Polaris | 2 | the page |
| …of which inside the page legend | 2 | 2 |
| …in the page body | **0** | 735 body epistemic encodings |
| Legend depth | 99.95% (character 1,481,009) | 1,481,819 characters |

**The cross-surface population, with its predicate.** A *body epistemic
encoding* is one of: a `<span class="epistemic epistemic-*">` badge outside
the page legend; a `<span class="claim-tuple">` span; an element with
`class="unknown-disclosure"`. Under that predicate:

| Page | Body encodings | Carrying a declared class |
|---|---|---|
| Home | 35 | 35 |
| Trajectory | 299 | 299 |
| Orrery | 18 | 18 |
| Polaris | **735** (713 tuples + 22 Unknown disclosures) | **0** (of the 735: 713 carry no declared class *and* no distinguishing treatment; the 22 carry the declared Unknown token under an undeclared class) |
| **Total** | **1,087** | **352** |

Two denominators, stated because they answer different questions
[Observed, both re-derived this session from the table above]. POC-REQ-060's
Case names "all three surfaces" — Polaris, Trajectory and Orrery — so the
requirement's own population is **1,052** (735 + 299 + 18), and **69.87%**
of it carries no declared encoding. The sweep this packet runs covers Home as
well, deliberately: Home imports the same design-token set slices 5 and 6
change, so a token regression there is in scope even though the requirement
does not count it. Over that four-page population of **1,087** the share is
**67.62%**. Either way every undeclared encoding is on Polaris; Home,
Trajectory and Orrery use the declared table for every body encoding they
render; this is a Polaris defect, not a POC-wide one, which is why the
checker's per-page predicate hides it. The dossier's 1,085 was the same shape measured over the
pre-lane-A captures and is not corrected by this figure, only superseded for
this capture population.

**The checker's denominator against the population.**
`apps/three-surface-poc/src/surface-routes.test.ts` lines 64–101 sets
`const denominator = pages.length` (4), tests each page with
`page.html.includes('class="epistemic epistemic-observed"')`, `continue`s any
page carrying neither substring, and asserts
`consistent > 0 && consistent <= denominator` — true by construction on any
page that renders the legend
[Observed: read at `a9f671e`]. Its companion,
`apps/three-surface-poc/src/cross-cutting.test.ts` lines 47–64, iterates pages
**and** the two entries of the declared table: for each page it asserts that
both declared badge spans and both descriptions are present, and additionally
that every `epistemic-*` class name it finds is one of the table's two. An
earlier draft of this packet described it as iterating pages "rather than
encodings", which understates it (review 1, F11). Its defect is narrower and
more precise: its denominator is `pages(model)`, and it enumerates the
**declared table**, never the rendered encoding population — the only rendered
markup it looks at is what `<span class="epistemic (epistemic-\w+)">` matches,
which is the legend's own. So a page carrying 735 body encodings in no
declared class passes it. Neither check can see those encodings. POC-REQ-060's
Case names the population: "a checker enumerates every epistemic encoding on
all three surfaces — the denominator is that population".

**The first reading.** Predicate: document start to the first occurrence of
`data-polaris-group="catalog"` — the four opening groups (overview,
boundaries, V1, architecture), ending at character 281,986, 19.03% of the
page.

| Measure | Value | Denominator |
|---|---|---|
| Claim tuples in the region | 126 | 713 |
| …labelled Unknown | **0** | 126 |
| Unknown-disclosure blocks in the region | **0** | 22 on the page |
| Occurrences of the word "Unknown" in the region's visible text | 14 | — |
| …that are a rendered Unknown state | **0** | 14 |
| First rendered Unknown of any kind (an Unknown-disclosure block) | 25.55% depth | — |
| First Unknown tuple (a class-level roster-identity claim) | 25.70% depth | — |
| The whole-shape Unknown tuple | 57.72% depth | — |
| "No member claim carries an Unknown reason." occurrences on the page | 8 | — |

All fourteen mentions are a navigation label, a glossary definition, the
sentence "No member claim carries an Unknown reason.", or a coverage line
reading "0 Unknown, 0 contradicted" [Observed: each context inspected]. This
is S1-F1 re-measured on the post-lane-A page with a sharper predicate: the
trim moved bytes, not the finding.

**Item and source rows.** Rows are matched to tuples **by claim id**, never
by an enclosing-element regex — one item row contains a nested `</li>` from
its own markdown prose and defeats a non-greedy row matcher, which is how a
first pass this session produced 408 of 409 [Observed: the failure was
reproduced and the method changed].

| Measure | Value | Denominator |
|---|---|---|
| `data-polaris-item="` attribute occurrences (the bare substring `data-polaris-item` counts 417; 8 are the distinct `data-polaris-items` attribute) | 409 | the page |
| Item rows matched to a tuple by claim id | 409 | 409 |
| …labelled Unknown | **0** | 409 |
| `data-polaris-source="` attribute occurrences | 278 | the page |
| …labelled Unknown | 9 | 278 |
| Unknown tuples on the page | 11 | 713 |
| …that are a single item | **0** | 11 |

S4-F6 confirmed on the lane A capture: the per-item Unknown branch —
`unknownRoutes(item.claim, '')` at `apps/three-surface-poc/src/polaris.ts`
lines 536 and 555 — is taken by **0 of 409** live item rows. The eleven live
Unknowns are nine withheld source claims, one class aggregate and the
whole-shape claim.

**Vocabulary against what renders.**

| Family | Closed vocabulary | Rendered here | Glossary sentences |
|---|---|---|---|
| Label | 3 (Observed, Inferred, Unknown) | 2 | 3 |
| Tier | **6**, closed by RFC2-25 (`packages/cap1-core/src/epistemic.ts` lines 23–30) | 2, one of which (`unstated`) is **not in the six** | 7 |
| Freshness | **4**, closed by RFC2-10 (`packages/cap1-core/src/staleness.ts` line 18 is the implementation's echo, not the authority) | 1 | 4 |
| Challenge | — | 1 | 1 |
| **Total** | | **6 values rendered** | **15 sentences** |

Nine of the fifteen glossary sentences describe a value no tuple on this
capture carries, and **none** of the fifteen has a visual treatment
[Observed]. `unstated` is minted by the renderer in **two** fields, at
`apps/three-surface-poc/src/polaris.ts` lines 306 and 307: into
`data-epistemic-tier` (fires 11 times on this capture) and into
`data-epistemic-freshness` (fires 0 times here, because all 713 tuples carry
`fresh`). Both are Q2; the freshness twin is governed by RFC2-10, which is
stricter than RFC2-25 and supplies its remedy as a disclosure outside the
freshness slot rather than a value inside it (Gate 2).
The page's own completeness check,
`apps/three-surface-poc/src/polaris-first-reading.test.ts` lines 96–99,
asserts that every rendered tier, freshness, challenge and label value has a
`"<term> —"` sentence — proving the gap is measured on the text axis and
never on the visual one.

**Token reuse.** `var(--unknown)` (#f3c56f) appears in five CSS rules in the
served stylesheet, carrying four meanings: the declared Unknown badge; an
unavailable notice; the Unknown-disclosure block; and the proposal treatment
and its label. **Two of the five render zero times on this capture**
[Observed, re-derived this session by literal `str.count` over the capture]:
`class="unavailable-notice"` occurs 0 times and `class="proposal"` occurs 0
times, while `class="unknown-disclosure"` occurs 22 times and
`class="proposal-label"` once. So five rules exist, four meanings are
declared, and the **live** reuse of `var(--unknown)` is three renderings of
two meanings besides the legend's own: 22 disclosure blocks and 1 proposal
label, against the 2 declared Unknown badge spans in the legend. An earlier
draft disclosed only the notice's zero and listed "the proposal treatment and
its label" as though both rendered (review 1, F10). `var(--cyan)` appears in
17 rules, exactly **one** of which is the declared Observed encoding — the
other sixteen are links, summaries, kickers, borders and code spans
[Observed]. `--amber` and `--focus` are the same hex value under two names.

**The colour-token population, named — and the universal that was false.**
ΔE76 is defined only over colour-valued tokens, so the population is the ten
colour tokens declared in `DESIGN_TOKENS_CSS` at
`apps/three-surface-poc/src/design-tokens.ts` lines 46–55: `--ink` #dfe9e7,
`--muted` #8ca3a4, `--void` #071012, `--panel` #0c181b, `--panel-raised`
#102126, `--line` #294248, `--cyan` #78e1d1, `--amber` #f1b85b, `--unknown`
#f3c56f, `--focus` #f1b85b. `--focus` duplicates `--amber` exactly, so the set
holds **nine distinct colours** and 36 distinct-value pairs.

An earlier draft of this packet asserted — and its evidence record repeated —
that 7.85 is "the smallest distance between any two named tokens" and that
"every other pair of named tokens is ≥ 26.7". Both were universals over an
unstated population, and both are **false over the full declared set** (review
1, F2; verification rules 2 and 9). Recomputed this session over all 36 pairs,
seven sit below the `--ink` ↔ `--muted` floor (26.74 to two decimals, 26.7371
computed — review 2, G7) and 7.85 is the **third**-smallest:

| Rank | Pair | ΔE76 |
|---|---|---|
| 1 | `--panel` ↔ `--void` | 3.98 |
| 2 | `--panel` ↔ `--panel-raised` | 4.82 |
| 3 | `--amber` ↔ `--unknown` | **7.85** |
| 4 | `--panel-raised` ↔ `--void` | 8.78 |
| 5 | `--line` ↔ `--panel-raised` | 14.96 |
| 6 | `--line` ↔ `--panel` | 19.56 |
| 7 | `--line` ↔ `--void` | 23.27 |
| 8 | `--ink` ↔ `--muted` | 26.74 |

Review 1's own enumeration of that tail listed six pairs and concluded "five
pairs sit below 26.74"; it omitted `--line` ↔ `--void` at 23.27. The figure
over the nine distinct colours is **seven**, re-derived here over the complete
36-pair matrix, which is recorded in full in the evidence file [Observed]. And
counting `--focus` as a named token in its own right, the smallest distance in
the declared set is **0.00**.

**The predicate the bar needs, stated.** The population that matters for slice
6 is the tokens carrying *foreground* meaning — the colours a reader reads a
mark in. The four ground tokens (`--void`, `--panel`, `--panel-raised`,
`--line`) are deliberately adjacent: near-identity is their purpose, and a
perceptual floor over them would forbid the page's own surfaces. Over the five
foreground tokens `{--cyan, --amber, --unknown, --muted, --ink}` — ten pairs,
all ten enumerated in the evidence record — 7.85 **is** the smallest and 26.74
is the next:

| Colour measure (population: the five foreground tokens) | Value | Method |
|---|---|---|
| Contrast `--amber` : `--unknown` | 1.109 : 1 | WCAG 2.x relative luminance |
| Smallest ΔE76 over the ten foreground pairs (`--amber` ↔ `--unknown`) | **7.85** | CIE76 over CIE Lab, D65, sRGB |
| Next smallest over the same ten (`--muted` ↔ `--ink`) | 26.74 | same |
| ΔE76 `--cyan` ↔ `--unknown` | 64.85 | same |
| Contrast `--unknown` on `--void` / `--panel` | 11.93 / 11.21 : 1 | WCAG 2.x |
| Contrast `--muted` on `--void` / `--panel` | 7.23 / 6.79 : 1 | WCAG 2.x |

S11-F2's 1.11 : 1 is confirmed. The sharper figure for slice 6 is ΔE76: over
the foreground population the two ambers are the closest pair by a factor of
3.4, and every other foreground pair is a comfortable distance apart, so 26.7
is an empirically grounded floor for a *foreground* token rather than an
invented one — and it is a floor over that population only, never over the
declared set as a whole. Note that `--cyan` and
`--unknown` differ by only 1.035 : 1 in *contrast*: they are far apart in
hue and close in luminance, so a reader who cannot separate hue gets no
signal from colour at all — which is why every slice below carries the
symbol and the label text, and why POC-REQ-061's AA obligation is about text
contrast on the ground, not between the two encodings [Inferred].

## Gate 2 — Doctrine

Cited by identifier and quoted from the defined location, per verification
rule 8. Doctrine and RFC locations were resolved through
`DIRECTIVE-REGISTER.md` and then read; the register carries no
spec-requirement family, so POC-REQ and PWB-REQ clauses were located by
heading in their own spec files.

**VIS-2 — No evidence means Unknown, not success**
(`.syzygy/governance/doctrine/vision.md`:96):

> No surface may declare a project aligned, converged, or genome-complete —
> nor turn anything green — without current evidence. … *Violation:*
> "spec-aligned ✓" computed from a stale index; a stale view silently green;
> a status flipping with no new identified evaluation.

The limb that bites is the first. A page whose first reading renders 126
Observed tuples and no Unknown, and whose Observed and Unknown tuples are
visually identical thereafter, is not "turning anything green" by assertion —
it is doing it by encoding. Slices 1, 3 and 4 answer it.

**VIS-7 — The observatory itself must be trustworthy**
(`.syzygy/governance/doctrine/vision.md`:183):

> … every rendered internal project-entity link resolves to its identified
> target …; every encoding means what its legend says; no secret material
> appears in any surface or store. Release-blocking for Syzygy's own releases
> … *Violation:* a dangling internal link; an unfaithful heatmap; two runs of
> one identified evaluation disagreeing in the deterministic layer.

Two encodings on Polaris mean something other than what the legend says. The
legend declares cyan `● Observed` and amber `? Unknown` and the body draws
neither; and the amber the legend assigns to Unknown also carries "Proposed
change — not current authority." at 56.29% depth. Slices 1, 5 and 6 answer
it.

**POC-REQ-060 — One design language, one epistemic encoding**, defined at
line 927 of
`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`:

> The three surfaces SHALL draw from one declared set of design tokens, and
> SHALL encode epistemic states (Observed, Unknown, and their reasons)
> identically wherever they appear. Scope of quantification: every epistemic
> encoding across the three surfaces.
>
> - **Case (sweep)**: a checker enumerates every epistemic encoding on all
>   three surfaces — the denominator is that population — and compares each
>   against the declared token/encoding table.
> - **Observable**: identical states render with identical declared encodings
>   on every surface.
> - **Oracle**: per-encoding equality with the declared table over the
>   exhausted population; the table is a checked-in declaration.
> - **Oracle independence**: the declared table is the expected value; the
>   sweep reads served output.
> - **Falsifier**: one surface encoding Unknown (or Observed) differently
>   from the declared table, or a surface styling epistemic state ad hoc.

Its scenario, at line 948:

> #### Scenario: Unknown looks the same everywhere
>
> - **WHEN** the same Unknown relationship appears on Polaris, Trajectory,
>   and Orrery
> - **THEN** all three render it with the declared Unknown encoding from the
>   shared token set

This is the whole of Q1 and the whole of Gate 5. The requirement already
fixes the sweep's denominator, already names ad-hoc styling as its falsifier,
and its scenario already says Polaris must render Unknown with the declared
encoding. **Nothing in M3's first two slices needs a word of new
specification.**

**POC-REQ-061 — The accessibility floor holds on every surface**, defined at
line 966 of the same file:

> Every surface SHALL be navigable by keyboard with visible focus, SHALL meet
> WCAG AA contrast for text and epistemic encodings, SHALL respect
> reduced-motion preferences, and SHALL carry legends whose text matches
> every visual encoding in use. … **Falsifier**: an unreachable interactive
> element, a failing measured pair, an animation surviving reduced-motion
> preference, or a legend entry matching no rendered encoding.

The falsifier's last limb is Q5's ground and cuts both ways: adding twelve
visual encodings without legending them fails it, and legending states the
page cannot render fails it too. Generating both from one table is the only
design in which neither can happen; marking the unreachable entries rather
than deleting them is M2's answer to the second limb, and slice 5 must carry
it forward, not overwrite it.

**PWB-REQ-007 — Every project claim carries its complete epistemic state**,
defined at line 439 of
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`:

> Every project entity and project-fact claim SHALL have a stable semantic
> Claim identity plus an evaluation instance, be challengeable with
> resolvable support, and carry the closed label, tier, exactly one primary
> reason, zero or more closed secondary reasons, freshness, challenge state
> and evaluation identity that govern it. …
>
> - **Case (sweep)**: enumerate every project entity, claim and aggregate
>   across two evaluations of the same semantic subjects, including
>   fixtures for every admitted label, tier, reason, freshness, challenge and
>   sibling state plus out-of-vocabulary and missing-currency cases.
> …
> - **Falsifier**: a positive claim lacks current support, a tuple field is
>   absent/out of vocabulary, a reason has no route, Unknown is folded into
>   a total, or an aggregate claims its own headline status.

Two limbs reach M3. The Case's fixture clause is slice 4's warrant in the
signed text itself: the requirement already demands fixtures for **every**
admitted tier and label, and the live page exercises two tiers of six and
zero item-level Unknowns. The Falsifier's "absent/out of vocabulary" is Q2 in
the spec's own words.

**PWB-REQ-020 — Project-wide facts remain identical across human and machine
views**, at line 902 of the same file:

> - **Observable**: both populations contain equivalent multisets.
> …
> - **Falsifier**: one fact, authority state, judgment state or disclosure is
>   missing, duplicated, changed, collapsed or associated with a different
>   evaluation in either channel.

M3 adds no fact to either channel. Slices 1, 5 and 6 change how an existing
fact is *styled*; slice 2 adds a checker; slice 3 moves two existing claims
earlier in reading order; slice 4 adds a test fixture. The parity population
is therefore unchanged in both channels, which is why no slice acquires a
PWB-REQ-020 delta [Inferred: the reading is that a CSS class and a symbol are
presentation of a fact already in both channels, not a new fact; if a
reviewer or the owner reads a rendered symbol as a new "disclosure" in
PWB-REQ-020's sense, slice 1 acquires a parity obligation and the sweep must
carry the symbol into the machine answer too]. The project's own recorded
lesson applies to slice 2's sweep regardless: **parity is per tuple, never
per id** — 713 tuples over 703 distinct claim ids on this capture, so
`tuples === distinct ids` is a false invariant.

**The machine side of Q2's tier limb, disclosed here.** Matched by claim id
against the retained machine answer (`api-poc.json`, 1,149 objects over
1,148 distinct ids carrying both `claimId` and `epistemic`), all **11 of
11** human-side Unknown tuples have an `epistemic` object with exactly
`['freshness', 'label', 'reasons']` — no `tier` key at all — while the
human page renders `data-epistemic-tier="unstated"` for every one of them
[Observed, re-derived this session; review 3, finding H6]. Q2's arm (b) for
tier is justified partly by PWB-REQ-007's tuple SHALL ("carry the closed
label, tier … that govern it"), and that justification holds on the human
channel only: the field the owner is asked to keep present in the render
has no counterpart at all in the machine channel's own object. This is not
resolved here — it is the same disclosure this section makes for slices 1
and 5's styling change, extended to the tier field's absence, and it
strengthens rather than weakens Q2: the divergence Q2 asks the owner to
rule on is already live and previously unmeasured.

**PWB-REQ-016 — Project comprehension works without vision or a pointing
device**, at line 864:

> Every project distinction and summary-to-source path SHALL be recoverable
> by text and operable by keyboard without relying on color, position or
> layout. … **Falsifier**: a color/layout-only distinction, unreachable
> target, pointer-only action, keyboard trap, missing mode flag or failed
> cold-open path.

This is the constraint on every slice below, and it cuts *against* a naive
reading of M3: today's uniform grey is not a PWB-REQ-016 breach, because the
label word is present in the tuple text. M3's repair must not create one by
carrying the new distinction in colour alone. Every slice therefore adds the
declared symbol and keeps the label text; colour is the third carrier, never
the first.

**RFC2-25 — Six tiers, closed, each inside exactly one parent label**, at
line 153 of
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`:

> A tier qualifies how a claim renders and may only *restrict* its parent
> label's authority, never extend it. **No new tier without an amendment to
> this RFC, and a tier never becomes a fourth epistemic label** — the
> three-label rule is exclusive and exhaustive; an untier'd claim renders at
> its bare label.

The last clause is arm (a) of Q2 for the *tier* field, and the reason arm (c)
is expensive.

**RFC2-26 — This contract schedules nothing**, at line 196 of the same file
(review 2, G6):

> This contract schedules nothing: **it is not a specification of record
> from which implementation work may be scheduled**. No implementation work
> for user-observable consequences of this contract — evaluation and
> snapshot displays, claim and challenge rendering, Unknown-reason and
> rendering-tier presentation, reconciliation-chain and gap surfaces, API
> answers over epistemic state — may be scheduled solely from this RFC.
> Before implementation, every observable consequence either maps to an
> approved OpenSpec requirement and scenario in the governance root's
> `openspec/**` plane, or carries a reviewed N/A judgment proving it purely
> structural with no independently testable behavior.

Slices 5 and 6 are "rendering-tier presentation" and "Unknown-reason …
presentation" in that list. Gate 5 names POC-REQ-061 as the approved
OpenSpec requirement their observable consequences map to, discharging this
clause's obligation explicitly rather than by implication.

**RFC2-10 — Identity-bearing freshness**, at line 209 of
`.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:

> **RFC2-10 — Identity-bearing freshness.** Logical freshness state —
> `fresh`, `stale`, `broken`, `superseded` — changes status and therefore
> participates in the VIS-7 identity test: two runs of one evaluation must
> agree on every freshness state. [Observed — architecture.md.] **Four
> values, closed.** The list changes only by amendment to this RFC; no
> implementation may mint, spell, or force-fit a freshness value it does
> not carry. The closure is required for the same reason RFC2-24's is: a
> machine answer carries the freshness state verbatim (RFC6-14), aggregates
> count per freshness value (RFC6-17), and a disagreement between two
> renderings over one declared scope is release-blocking (RFC6-22/23) — a
> value existing in no vocabulary can be neither carried verbatim nor
> checked for parity, and leaving it unstated is how the value gets chosen
> by whoever implements the render first. A condition genuinely outside the
> four is disclosed as a fact of the render, never dressed as a freshness
> state. Freshness is orthogonal to the three labels and the tier registry;
> it never substitutes for either.

The quote now runs the clause's full extent, lines 209–223 (the next clause,
RFC2-11, begins after a blank line), so "quoted in full" below and in Q2 is
now literally true; before this repair it stopped one sentence short, at
"freshness state." (review 3, finding H11). The closing sentence matters for
Q2's freshness limb: it is an argument against arm **(b-ii)** — holding the
claim Unknown rather than disclosing the condition — because it says
freshness is *orthogonal* to the labels and never substitutes for either,
so a reader could take it to mean the Unknown label is not itself a
freshness disclosure and cannot discharge RFC2-10's obligation on its own.
It is not an argument against **(b-iii)**, which discloses the condition
outside the freshness slot rather than through the label. Q2 states this
weighing directly.

This is the clause the freshness family is closed by, and this packet's first
draft never cited it (review 1, F9): it anchored the closure to
`packages/cap1-core/src/staleness.ts` line 18, which is an implementation and
not an authority — a citation, not a reliance (verification rules 5 and 8).
The constant is retained below only as the implementation's echo, labelled as
such.

RFC2-10 is also **stricter than RFC2-25**, though the shapes of their
remedies differ rather than one simply having none. RFC2-25 forbids a new
*tier* and supplies a *rendering* remedy for absence, inside the tuple ("an
untier'd claim renders at its bare label"). RFC2-10 forbids the *minting* in
terms — "no implementation may mint, spell, or force-fit a freshness value
it does not carry" — and supplies its own remedy as a *disclosure*, outside
the freshness slot: "a condition genuinely outside the four is disclosed as
a fact of the render, never dressed as a freshness state" (quoted in full
above). Review 1's F4 named the asymmetry; review 2 (G1) found this packet's
own account of it — "supplies no absence marker at all" — false against the
clause's own text, which the packet had quoted only as far as its minting
prohibition and not to its remedy. Q2 below states the corrected asymmetry
and puts RFC2-10's disclosure route to the owner as a named arm. The
renderer mints `unstated` into both fields, on consecutive lines
(`apps/three-surface-poc/src/polaris.ts`):

```
306:  const tier = claim.epistemic.tier ?? 'unstated';
307:  const freshness = claim.epistemic.freshness ?? 'unstated';
```

On this capture the freshness twin never fires — all 713 tuples render `fresh`
[Observed] — so every measurement in this packet stands. The hazard is live
rather than theoretical, and it is one branch away: M2's Q7 records that
`assessCurrency`'s `no-bound-declared` arm returns no `freshness` field at
all, and M2 slice 5 routes freshness through that engine, so on the day it
lands line 307 mints a fifth freshness value on every class with no declared
bound [Observed: M2's packet and evidence record on branch
`agent/syzygy-dov.2` (register row P-69), read this session; the arm is at
`packages/cap1-core/src/staleness.ts` lines 98–104 in this worktree]. Q2 below
therefore covers both fields, and slice 5's freshness table has to catch the
mint rather than assert over the declared table alone.

**RFC7-34 — Non-visual recoverability**, at line 241 of
`.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md` (the
module whose front matter reads `applies_to: [polaris]`):

> Every such distinction is recoverable **without colour, position, or
> layout** — by label, text, or structure; visual encodings are legended
> and mean exactly what the legend says (VIS-7); every curated diagram has
> a text equivalent … an epistemic state a reader cannot perceive is
> comprehensible fiction for that reader.

This is the Polaris-binding form of VIS-7's legend limb, and it is the clause
Q6 rests on: an amber left rule and an amber label are visual encodings, and
the page's only legend assigns that amber to Unknown.

**CC-VIZ-1 — Every encoding declares source, units, legend, Unknown
behavior, and freshness**
(`.syzygy/governance/policies/craft-and-care/performance-and-visual-discipline.md`:48):

> Every visual encoding (color, height, size, position, motion) declares: the
> data source it renders, its units/scale, a legend stating exactly what it
> means, how Unknown values render, and the freshness of the underlying
> evaluation. An encoding means exactly what its legend says — the trust
> floor (VIS-7) makes an unfaithful legend release-blocking.

**CC-VIZ-3 — Unknowns are visible, aggregated honestly, never disappeared**
(same file, :74):

> *Violation:* a "clean" default view that filters out Unknown regions
> entirely, presenting a fully-green city over a half-observed project.

Slice 3's warrant. The first reading does not filter Unknowns out — they are
further down the same document — but a reader who stops at the catalogs has
been shown exactly the view this violation describes.

**A scope note, stated rather than assumed.** RFC 0009 carries
`applies_to: [orrery, machine-clients]` in its own front matter, so RFC9-24
(the reserved state palette, which reserves Proposed/speculative), RFC9-26
(the channel registry) and RFC9-27 ("No epistemic state is carried by color
alone: each carries at least two of {surface treatment, plate/badge, label}")
do not bind Polaris directly [Observed: the front matter].

**How far RFC 0009 actually reaches these two requirements.** An earlier draft
of this packet claimed, labelled `[Observed]`, that "POC-REQ-060 and
POC-REQ-061 name RFC9-3, RFC9-46 and RFC9-48 among their own warrants". That
is false and review 1 caught it (F1). Each requirement's own `warrants` block
is the fenced block that *follows* its scenario. Read at `a9f671e` in
`openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md`,
POC-REQ-060's block is at lines 955–964:

> ```yaml
> warrants:
>   primary: VIS-3
>   doctrine: [VIS-1, VIS-3]
>   contracts: [RFC6-18, RFC6-22, RFC8-31]
>   policies: []
>   decisions: [POC-DIR-2026-08-30]
>   topology: []
>   parent_requirements: []
> ```

and POC-REQ-061's is at lines 999–1008 of the same file:

> ```yaml
> warrants:
>   primary: VIS-3
>   doctrine: [VIS-1, VIS-3]
>   contracts: [RFC7-34, RFC8-31, RFC9-48]
>   policies: []
>   decisions: [POC-DIR-2026-08-30]
>   topology: []
>   parent_requirements: []
> ```

So POC-REQ-060 names **no RFC 0009 clause of any kind**, and POC-REQ-061 names
**RFC9-48 only** [Observed: both blocks read and quoted at `a9f671e`]. The
block carrying `[RFC1-26, RFC6-20, RFC9-3, RFC9-46, RFC9-48]` sits at line 920
and closes the *preceding* (Orrery) requirement, whose scenario ends at line
914; POC-REQ-060's heading is line 927. The defect was the standing misread of
this file's layout — the yaml block above a heading taken for the block below
it.

The corrected bridge is narrower, and the conclusion it supports is unchanged
and in fact better supported: no RFC 0009 clause reaches this work except
RFC9-48, through POC-REQ-061's warrants. The design below therefore takes
RFC9-27's two-carrier rule as a **design standard adopted voluntarily**, not
as a clause that binds Polaris [Inferred]; the binding obligations are VIS-7,
RFC7-34, PWB-REQ-016, POC-REQ-060 and POC-REQ-061, and each slice is justified
on those alone.

**Conflict check.** None found. Every slice makes an existing state more
visible or an existing encoding more truthful; none turns anything green,
none folds an Unknown into a total, none adds or removes a fact from either
channel, and none reads a Butlers body. Slice 3 changes what a reader meets
first, in the direction doctrine permits (toward Unknown, never away).

## Gate 3 — Topology

| Slice | Lives in | Governed artifact touched |
|---|---|---|
| 1 Declared encoding on the tuple | `apps/three-surface-poc/src/design-tokens.ts` (the table gains the selector form), `apps/three-surface-poc/src/polaris.ts` (the CSS block near line 1307) | none |
| 2 The population sweep | `apps/three-surface-poc/src/surface-routes.test.ts` (lines 64–101 replaced), `apps/three-surface-poc/src/cross-cutting.test.ts` (lines 47–64 extended) | none |
| 3 A first-reading Unknown in place | `apps/three-surface-poc/src/polaris.ts` (the opening band), `apps/three-surface-poc/src/polaris-copy.ts` (one new sentence) | none |
| 4 An item-level Unknown fixture | `apps/three-surface-poc/src/test-project-shape-fixture.ts` (a new texts variant), `apps/three-surface-poc/src/polaris-project-shape.test.ts` or a new test file | none |
| 5 Tier/freshness/challenge encoding tables and a generated glossary | `apps/three-surface-poc/src/design-tokens.ts`, `apps/three-surface-poc/src/polaris-copy.ts` (lines 34–51), `apps/three-surface-poc/src/polaris.ts` lines 346–361 (`claimStatesBlock`; the freshness group is line 357), `apps/three-surface-poc/src/polaris-first-reading.test.ts`; and `apps/three-surface-poc/src/walkthrough-preflight.ts` as an **unchanged but binding input** — it reads the generated block and is the PWB-REQ-021 readiness gate over it (see the slice) | none |
| 6 A render-disclosure family and a `--proposed` token | `apps/three-surface-poc/src/design-tokens.ts` (the colour tokens at lines 46–55 and the table), `apps/three-surface-poc/src/polaris.ts` lines 1328–1329 | none |

Boundaries crossed: **none**. Every file is inside `apps/three-surface-poc`.
No slice touches `packages/three-surface-poc-core`, the body-read authority
gate, the observation pipeline, the adapter-registry entry, the response
ceilings, the consent act's pair or content class, or any specification text.
Slice 4 adds a fixture to the app's own test fixture module and reads no
repository. [Observed: the file list above, each path resolved at `a9f671e`.]

### The authorizing act, per slice

| Slice | Owner act needed | Named act |
|---|---|---|
| 1 Declared encoding | **No** | rides `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` (2026-09-05), which continues `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (2026-09-02) |
| 2 Population sweep | **No** | same continuation; it adds a check and reads served output |
| 3 First-reading Unknown | **No** | same continuation; it reorders rendering of claims the model already carries |
| 4 Item-level Unknown fixture | **No** | same continuation; a fixture is test material and observes nothing |
| 5 Encoding tables and generated glossary | **No** | same continuation; copy and CSS, no governed artifact |
| 6 Render-disclosure family and token | **No** | same continuation |
| Any spec amendment, had one been proposed | **None found** | and none is sought — see Gate 5 and Q7 |

The 2026-09-02 authorization's escalation triggers, quoted verbatim from its
"Escalation triggers" section: "a change to doctrine or an accepted contract;
an amendment to the signed PWB specification; a change to security, privacy,
or retention posture beyond the approved secret-classification policy; a
change to the constraints or envelope the registry entry declares; any
observation outside the consented content class or repository; or any scope
beyond the signed change." **No slice crosses any of the six** [Observed for five of the
six: no doctrine or contract text is edited; no spec text is edited; no
secret, privacy or retention behaviour changes — slice 4's fixture is
synthetic text in the app's own test module; the registry entry is untouched;
no observation is added, and slice 4 removes the need for one. Inferred for
the scope limb: that every slice implements behaviour the signed change
already requires is a reading of that change's own requirement text, argued
at Gate 5, not a textual absence — split after review 4, finding J9].

P-52 is not touched: all six slices run under `syzygy-dov.3`, the pursuit
bead, so no ninth POC item is filed — the route the M1 ruling took for
`syzygy-dov.1`.

## Gate 4 — Design sketch, per slice

### Slice 1 — The declared encoding reaches the tuple (medium; no act)

**Design.** `EPISTEMIC_ENCODING` already carries, per label, a `className`
and a `symbol` (`apps/three-surface-poc/src/design-tokens.ts` lines 16–29).
The table gains one generated CSS fragment: for each entry, a rule of the
form `.claim-tuple[data-epistemic-label="<label>"]` setting the entry's
colour, and a `::before` rule emitting the entry's symbol. The rules are
**generated from the table**, never hand-authored, so POC-REQ-060's Oracle
("the table is a checked-in declaration") holds by construction.

**Why an attribute selector rather than a class on the span.** Cost. The
attribute is already on all 713 spans. Adding
`epistemic-observed`/`epistemic-unknown` to each `class` attribute plus a
literal symbol costs **16,366 bytes** (702 × 19 + 11 × 18 for the class, plus
702 × 4 + 11 × 2 for the symbol in UTF-8) on a page already 84,487 bytes over
the M1 ruling's working target; the generated CSS costs a few hundred bytes
once [Observed: both figures computed this session]. The visible result is
identical.

**Why it survives lane B — Q3.** If lane B hoists `data-epistemic-label` onto
a scope for 409 tuples, the tuple-level attribute selector stops matching
them. The rule set therefore carries **both** forms from the start: the
tuple-level selector, and a descendant selector of the form
`[data-epistemic-scope-label="<label>"] .claim-tuple:not([data-epistemic-label])`,
expressing exactly the inheritance rule lane B's own text states ("a claim's
value for a field it does not carry itself is the value of the nearest
enclosing scope that carries the field"). Written now, lane B needs no second
pass; written later, it is a silent 57% hole.

**The three carriers.** Label text (already present), declared symbol (new,
via `::before`), colour (new). PWB-REQ-016's falsifier is a
*colour-only* distinction; the label text alone already answers it and the
symbol adds a second non-colour carrier. The symbol is decorative
reinforcement, so it is `::before` content and never the sole carrier of
meaning — a screen reader that skips generated content still reads the label.

**Oracle.** An independent sweep over served output: for every element whose
expanded `data-epistemic-label` is *L*, the served stylesheet contains a rule
selecting it and that rule's declarations equal the declared table's entry
for *L*. Expected values are hard-coded literals in the test, never imported
from `design-tokens.ts`.

**Rule-6 mutants.** (a) Delete the Unknown rule from the generated fragment →
the sweep fails. (b) Swap the two entries' colours → fails. (c) Emit the
tuple-level selector only (the pre-lane-B form) and hoist one label in the
fixture → fails with a denominator smaller than the tuple count. (d) Change
`::before` content to an empty string → the symbol assertion fails. Each
mutant's `old`/`new` fragment and the commit it ran at are recorded.

### Slice 2 — A population sweep with a real denominator (medium; no act)

**Design.** Replace `surface-routes.test.ts` lines 64–101 with a sweep that,
for each served page, enumerates the **encoding population** — every
`class="epistemic epistemic-*"` badge, every `class="claim-tuple"` span and
every `class="unknown-disclosure"` element — expands scopes per the
inheritance rule, and asserts per member that its rendered treatment equals
the declared table's entry for its expanded label. It reports the population
count and the per-page breakdown, and asserts the total is non-zero **and
equal to an independently computed count**, so a predicate that silently
matches nothing fails rather than passes.

**Denominators reported.** Per page and in total, in the shape the
PWB-REQ-020 parity sweep already uses. The measured baseline is in the
evidence record beside this packet: 1,087 body encodings over four pages
(1,052 over POC-REQ-060's own three surfaces), 352 carrying a declared class. After slice 1 the second figure should equal the
first.

**Why the population predicate must be declared, not inferred.** The three
element families above are this packet's stated predicate; a future family
(say a new disclosure block) would be invisible to it. The sweep therefore
also asserts that **no element carries a colour drawn from the epistemic
token set outside the enumerated families** — a negative sweep with its own
denominator, so a fourth family cannot appear unmeasured. [Inferred: this is
the packet's design for closing rule 9's false-absence class at the checker,
not a clause requirement.]

**Oracle.** Hard-coded expectations; the sweep reads served bytes only,
importing no rendering code — POC-REQ-060's own Oracle-independence clause.

**Rule-6 mutants.** (a) Style one tuple ad hoc in the renderer → the sweep
fails (this is the requirement's named falsifier, live today and currently
unseeable). (b) Set the denominator to the page count → the equality
assertion fails. (c) Remove one element family from the predicate → the
independent count disagrees. (d) Add an epistemic-token colour to an element
outside the families → the negative sweep fails.

**The negative sweep has one known live positive on day one.**
`class="proposal-label"` renders once, at 56.29% depth, and its served rule
is `.proposal-label { …; color: var(--unknown); }` (`polaris.ts`:1329) —
exactly what the negative sweep in the previous paragraph asserts against,
and exactly what slice 6 exists to repair (review 3, finding H7). Run as
sequenced, slice 2 is red the day it lands against an element the same
packet defers to slice 6. Rather than declare a dated exception for it,
this packet pulls slice 6's token change for that **one** rule forward into
this slice: `.proposal-label` moves to the `--proposed` token now, before
the rest of slice 6's encoding table exists. It touches neither of M2's two
files and needs no act, so it can run with slices 1–4 while the rest of
slice 6 still waits on nothing but its own measurable bar (Q6). This is
this packet's stated choice, not the only lawful one — a declared, dated
exception naming the element and the reason is the alternative, and would
leave slice 2 red until slice 6 lands.

### Slice 3 — One real Unknown in the first reading (medium; no act)

**Design.** The opening band renders, in place and before the first catalog
group, the two Unknown claims the page already carries at 25.70% and 57.72%
depth: the whole-shape claim and the class-level roster-identity claim. Each
renders as the existing `unknown-disclosure` block — its reason verbatim, its
route as an affordance — with its tuple beside it, so the first reading
contains at least one rendered Unknown with the declared encoding slice 1
gives it.

**Nothing is invented.** These are existing claims with existing reasons and
routes; the change is reading order. The band states the count of Unknowns on
the page and links to them, so the reader who stops at the catalogs has met
the page's honesty rather than only its coverage counts. The four "No member
claim carries an Unknown reason." sentences stay exactly where they are and
stay true.

**Why not a summary number alone.** VIS-1's honest simplification permits
"Unknown ×40"; CC-VIZ-3 requires the count, the reason and expandable detail
together. A count with no member rendered in place is the half of the pattern
the page already has.

**Oracle.** A copy-and-position test: the first occurrence of a rendered
Unknown state precedes the first `data-polaris-group="catalog"` occurrence,
and the rendered block carries a route string that matches the claim's route
in the model by claim id. Labels are distinctive strings — never a short word
like "None" that a substring match reaches by coincidence.

**Rule-6 mutants.** (a) Move the band after the catalogs → the position
assertion fails. (b) Render the count without the member → the member
assertion fails. (c) Render the member without its route → the route
assertion fails.

### Slice 4 — A fixture that forces an item-level Unknown (medium; no act)

**Design.** `itemClaim` in
`packages/three-surface-poc-core/src/project-shape-model.ts` lines 376–378
has three arms: `modeled` → Observed, `contradicted` → Unknown at tier
`suspended`, otherwise Unknown with the item's own reason. Live Butlers
content reaches only the first. The fixture module already parameterises the
shape by a text map (`projectShapeFixtureGit(texts)`), and already has
variants for excluded and active content, so the new variants are text maps:
one whose root index declares an item whose source is missing or unreadable,
and one that produces a contradiction. Both are synthetic text in the app's
own test module; neither reads a repository.

**What it proves.** That `unknownRoutes(item.claim, '')` renders in the item
cell with its reason and route, that the row's tuple carries Unknown, that
the parity sweep still matches the row to its machine claim by id, and — with
the contradiction variant — that a **third** tier value (`suspended`) renders
at least once anywhere in the POC. PWB-REQ-007's own Case asks for exactly
this: "fixtures for every admitted label, tier, reason, freshness, challenge
and sibling state".

**Scope note.** The full "every admitted tier" fixture set is larger than M3;
this slice delivers the two arms the renderer has that live content never
reaches, and records the remaining gap (three of six tiers still unfixtured)
rather than claiming the Case is met.

**Rule-6 mutants.** (a) Make the Unknown arm fall through to Observed → the
fixture test fails. (b) Drop the route from the item cell → fails. (c) Build
the fixture at describe time rather than in `beforeAll` → recorded as a
guard, because a mutant that throws at describe time reports zero tests and
scores as survived.

### Slice 5 — Encoding tables for tier, freshness and challenge (medium–large; no act)

**Design.** Three new declared tables beside `EPISTEMIC_ENCODING`, each a
checked-in array of `{ value, treatment, sentence }`: six tier rows (RFC2-25's
closed six), four freshness rows (the four RFC2-10 closes the family at — the
clause is the authority; `packages/cap1-core/src/staleness.ts` line 18 is the
implementation's echo of it), and the challenge rows.
The glossary block at `apps/three-surface-poc/src/polaris.ts` lines 346–361
(`claimStatesBlock`; the tier group is line 356, the freshness group line 357)
is **generated** from them, replacing the hand-authored sentences at
`apps/three-surface-poc/src/polaris-copy.ts` lines 34–51 — the 15 state
sentences run 34–51, three label plus seven tier plus four freshness plus one
challenge, with the three group labels interleaved, so a narrower 38–51
understates what is replaced by three lines — so a value with no
encoding cannot be legended and an encoding with no legend entry cannot
render. That is POC-REQ-061's falsifier closed in both directions by
construction, and CC-VIZ-1's "a legend stating exactly what it means"
satisfied by generation rather than by discipline.

**Q2's constraint, in both fields.** The tier table has **six** rows.
`unstated` is not a seventh row; on the recommended answer to Q2 it is an
*absence treatment* — the field renders, the reader is told no tier applies,
and the closed six stay six. An implementation that adds a seventh row has
minted a tier, which RFC2-25 forbids in terms and which no implementer may do.

The freshness table has **four** rows and **no absence row**, and this is
where a table-only assertion is one line short (review 1, F4). RFC2-10 forbids
minting, spelling or force-fitting any value the closed four do not carry, and
the renderer mints one at `apps/three-surface-poc/src/polaris.ts` line 307
(`claim.epistemic.freshness ?? 'unstated'`) — a line the earlier draft of this
slice never looked at, because it asserted closure over the declared table and
the declared table cannot see the renderer. The slice's closure assertion is
therefore over **served output**: no `data-epistemic-freshness` value outside
the four may appear on any page, with the tuple count as the denominator. On
this capture the assertion passes trivially (713 `fresh` of 713) and is a
guard against a value one branch away: M2's `assessCurrency` wiring reaches
the `no-bound-declared` arm, which returns no `freshness` field
(`packages/cap1-core/src/staleness.ts` lines 98–104), for every class with no
declared bound.

**The readiness gate this slice regenerates under.**
`apps/three-surface-poc/src/walkthrough-preflight.ts` reads the exact block
slice 5 generates and is the PWB-REQ-021 readiness check over it; the earlier
draft named the file nowhere (review 1, F6). Read at `a9f671e`, its
`claimStrength` arm (lines 203–226) requires: exactly one
`<details id="polaris-claim-states"`; `id="polaris-claim-states-lede"` present
exactly once; a `"<term> —"` sentence inside that block for every label, tier,
freshness and challenge value of every presented claim; the
`states.strengthen` text present; and
`aria-describedby="polaris-claim-states-lede"` on every claim tuple. A
generated glossary that drops the lede id, the strengthen sentence, or the
`aria-describedby` binding breaks readiness without breaking any test slice
5 writes. Dropping the `unstated —` sentence, which Q2 arm (b) makes
tempting to delete, does **not** break this preflight (review 2, G2): its
required-term set is built from `claim.epistemic.tier`/`.freshness` on the
*model*, never from the render, and `unstated` is never a model value, so
the term never enters it. The guard that actually holds the `unstated —`
sentence is `apps/three-surface-poc/src/polaris-first-reading.test.ts` line
88, which hard-codes it in its own list of required terms; slice 5 must keep
that guard rather than rely on the preflight for it. The preflight file is
unchanged by this slice and binding on it; it is in the Gate 3 row and in
Gate 6's re-run list.

**M2's constraint.** M2 slice 1 marks the three unreachable freshness
sentences in place with the reason it is unreachable and, where one exists,
the route (M2's `superseded` marker has a reason and no route, by design —
review 2, G4), under a copy oracle. Slice 5 must carry those markers into
the generated table as a per-row *reachability* field, not delete them; the
copy oracle M2 writes becomes an assertion over the generated output. If M3
lands first, M2's hand edit lands on generated copy and is lost. This is the
whole of Q7's first half.

**The textual sweep becomes a visual one.**
`apps/three-surface-poc/src/polaris-first-reading.test.ts` lines 96–99 already
assert every rendered value has a sentence; slice 5 adds the mirror — every
rendered value has a declared treatment, and every treatment in the tables
appears in the generated glossary.

**Rule-6 mutants.** (a) Add a seventh tier row → a closure assertion against
the hard-coded six fails. (b) Delete one freshness row → the generated
glossary loses a sentence and the completeness assertion fails. (c) Mark a
reachable value unreachable, and an unreachable one reachable → both
directions of the reachability oracle fail. (d) Give two rows the same
treatment → a distinctness assertion fails. (e) Force
`claim.epistemic.freshness` undefined in a fixture claim → the served-output
assertion fails on a fifth `data-epistemic-freshness` value, which is the
RFC2-10 guard and the one the declared-table assertion cannot see. (f) Remove
the `states.strengthen` sentence from the generated block →
`walkthrough-preflight.ts` reports the glossary does not say how a claim is
strengthened, and readiness fails. Each mutated pillar is given the reason
already on the page, so a page-wide substring check cannot survive by
coincidence.

### Slice 6 — A render-disclosure family and a `--proposed` token (medium; no act)

**Design.** A fourth declared encoding table, beside the label, tier and
freshness/challenge tables slice 5 adds: **render disclosures** — page-level
statements about the *status of the narrative material being shown*, as
distinct from the epistemic state of a claim. The page renders exactly one
today: the proposal treatment (`.proposal`, `.proposal-label` at
`apps/three-surface-poc/src/polaris.ts` lines 1328–1329), which stops
borrowing `var(--unknown)` and takes a `--proposed` token with a generated
legend row.

**What this family is not, stated so no implementer mints anything.** It is
not a set of sibling surface states. RFC2-25 closes those at three —
`dismissed-by-decision`, `unadopted-draft`, `editorial-draft` — and this page
renders none of them (0 occurrences of each on the capture, and 0 of
`challenge-pending`) [Observed]. Slice 6 adds no member to that family, no
seventh tier, and no fourth epistemic label. It is also not where
contradiction lives: `itemClaim` at
`packages/three-surface-poc-core/src/project-shape-model.ts` line 377 returns
an Unknown claim at tier `suspended` for a contradicted item, which is one of
RFC2-25's six, so contradiction belongs to slice 5's tier table and slice 4's
fixture. An earlier draft of this packet placed both in a "sibling surface
states" family and contradicted slice 4 in the same sentence (review 1, F3).

**Its governing clauses.** CC-VIZ-1 (a declared encoding carries a legend
stating exactly what it means), VIS-7's legend limb, RFC7-34's Polaris-binding
form of it, and POC-REQ-061's legend-to-encoding falsifier in both directions.
RFC7-28's "speculated structure never looks like existing structure" is the
nearest clause in spirit, but its stated subject is a *curated diagram*, so it
is cited here as an analogue rather than as the warrant [Inferred].

**The measurable bar, with its population named.** The new token must sit at
**ΔE76 ≥ 26.7** from `--unknown` and meet WCAG AA (≥ 4.5 : 1) against both
`--void` and `--panel`. The 26.7 floor is derived from the existing palette,
but over a stated population: the five tokens that carry foreground meaning
(`--cyan`, `--amber`, `--unknown`, `--muted`, `--ink`), where `--amber` ↔
`--unknown` at 7.85 is the smallest of ten pairs and `--muted` ↔ `--ink` at
26.74 is the next. It is **not** a floor over the whole declared token set:
seven of the 36 pairs over the nine distinct declared colours sit below the
`--ink` ↔ `--muted` floor (26.74 to two decimals, 26.7371 computed — review
2, G7), because ground tokens are adjacent on purpose (Measurements; the
full matrix is in the evidence file). Both numbers are computed by the test
from the token values, with the formula and the colour space stated, and
recorded in the
evidence file. The existing foreground near-collision — `--amber` and
`--unknown` at 7.85 — is either repaired in the same pass or recorded as a
known reuse with its legend row, because `--amber` carries the notice
treatment and `--focus` is the same value again under a third name.

**Not colour alone.** The proposal keeps its sentence ("Proposed change — not
current authority.") and gains a marker in the declared family, so the state
has a text carrier and a structural one before colour is counted — RFC7-28's
"speculated structure never looks like existing structure" read through
RFC7-34's recoverability limb.

**Rule-6 mutants.** (a) Set `--proposed` equal to `--unknown` → the distance
assertion fails. (b) Drop the proposal's legend row → the generated-legend
completeness assertion fails. (c) Lower the token's contrast below AA → the
contrast assertion fails.

### Design bar for the human surface

No new interaction. Every contract input carries forward unchanged:
PWB-REQ-016 comprehension without vision or a pointing device (every new
distinction has a text carrier before colour); no fragment target inside a
`<details>`; keyboard paths complete with visible focus; direct and tailnet
parity; the no-JS path complete; the glossary still explaining every rendered
tuple term, now by generation. Page size is measured before and after on both
host forms (Gate 6); the recommended designs add hundreds of bytes, and the
alternative that adds 16,366 is named and declined.

## Gate 5 — Specification

**No slice requires a specification delta**, and that is this packet's most
useful finding.

**Slices 1 and 2 are conformance with text that already binds.** POC-REQ-060
states the invariant ("SHALL encode epistemic states … identically wherever
they appear"), fixes the sweep's denominator ("the denominator is that
population"), names the falsifier that is live today ("a surface styling
epistemic state ad hoc"), and its scenario already says Polaris renders
Unknown "with the declared Unknown encoding from the shared token set". There
is nothing to add; the implementation does not yet meet it. Ruling Q1 the
other way would not create a delta either — it would make the current
rendering conformant and withdraw slices 1 and 2 — which is why Q1 is a
conformance ruling rather than a spec question.

**Slice 3** implements VIS-2 and CC-VIZ-3 inside PWB-REQ-010's ordering
("Polaris … SHALL first present Butlers' purpose, promises, non-goals,
architecture, V1 scope and success criteria before presenting any single
capability's detail"). Rendering an existing project-level Unknown in the
opening band is a project-level fact, so it sits inside that ordering rather
than against it [Inferred: PWB-REQ-010 names the categories the first reading
must answer and does not enumerate what else it may carry].

**Slice 4** is asked for by PWB-REQ-007's Case in terms.

**Slices 5 and 6** add visual encodings beyond the two POC-REQ-060 names.
POC-REQ-060's scope of quantification is "every epistemic encoding across the
three surfaces", and a tier or freshness treatment is an encoding of a tuple
field rather than of an epistemic label, so the new families sit alongside
the requirement rather than inside it [Inferred: this is the reading this
packet relies on]. They are governed instead by CC-VIZ-1 (every visual
encoding declares its legend), POC-REQ-061's legend-to-encoding falsifier and
VIS-7. POC-REQ-061 is also the approved OpenSpec requirement RFC2-26 requires
an observable consequence of that contract to map to before implementation
(Gate 2); its legend-to-encoding falsifier is exactly that mapping for
slices 5 and 6, so RFC2-26's scheduling bar is discharged, not left open.
**If the owner or a reviewer reads POC-REQ-060's "one declared set of
design tokens" as closing the token set at its current members**, slices 5
and 6 acquire a POC spec delta, join Q7's collision, and must queue behind
P-68 — which is the condition under which Q5 and Q6 change answer.

**What would need an amendment.** Q2 arm (c) only: providing for `unstated`
in PWB-REQ-007's text. That is a digest-bound spec, amendable only by an
owner-gated CC-REV-2 route, and it edits the same requirement lane B's
package rewrites. It is named here as a question, never as a plan step, and
the recommended answer avoids it.

### New WHEN/THEN scenarios (for the beads' acceptance contract, not the spec)

**S1 — Every epistemic encoding carries a declared class.**
WHEN any surface renders an epistemic state, THEN the element's treatment
equals the declared table's entry for its expanded label, AND a sweep whose
denominator is the enumerated encoding population — reported per page and in
total — fails if any member does not.

**S2 — The sweep's denominator is the population, not the page count.**
WHEN the POC-REQ-060 checker runs, THEN it reports a population count equal
to an independently computed enumeration of the encoding elements, AND a
mutant that reduces the denominator to the number of pages fails the check.

**S3 — Ad-hoc styling fails the check.**
WHEN one surface styles an epistemic state outside the declared table, THEN
the sweep fails and names the element — the requirement's own falsifier,
which no check can see today.

**S4 — Observed and Unknown are distinguishable without colour.**
WHEN a reader without colour perception reads any tuple, THEN the state is
recoverable from the label text alone, AND the declared symbol is a second
non-colour carrier, AND no assertion anywhere depends on colour being
perceived.

**S5 — The encoding survives scope inheritance.**
WHEN a tuple's label is carried by an enclosing scope rather than by the
tuple, THEN the tuple still renders the declared treatment for its expanded
label, AND the sweep's denominator is unchanged by the hoist.

**S6 — A rendered Unknown appears in the first reading.**
WHEN Polaris is opened, THEN at least one Unknown claim renders in place,
with its reason verbatim and its route, before the first catalog group, AND a
test asserts the position and both halves.

**S7 — The item-level Unknown route renders.**
WHEN a fixture declares an item whose source is missing, unreadable or
contradicted, THEN that item's row renders the Unknown route in place, its
tuple carries Unknown with the item's own reason, and the parity sweep still
matches the row to its machine claim by id.

**S8 — The legend and the encodings are generated from one table.**
WHEN a value has a declared treatment, THEN the glossary carries its
sentence; WHEN a value has a glossary sentence, THEN it has a declared
treatment or a rendered mark saying why it is unreachable, AND neither can be
edited without the other.

**S9 — The closed vocabularies stay closed.**
WHEN an implementation adds a row to the tier table, THEN a closure assertion
against the six hard-coded values fails; the same for the four freshness
values. AND WHEN the renderer emits any `data-epistemic-freshness` value
outside the closed four — including the `unstated` its own line 307 mints when
the field is absent — THEN a sweep over served output, with the tuple count as
its denominator, fails; a closure asserted over the declared table alone
cannot see that line.

**S10 — No two meanings share a token.**
WHEN two declared foreground treatments carry different meanings, THEN their
tokens sit at or beyond the stated perceptual distance over the named
foreground population, AND each meets AA contrast on both page grounds, AND
the full pairwise matrix and the population's definition are in the evidence
record.

**Out of scope, explicitly.** Amending any specification; amending doctrine
or any contract; a reserved-state registry in RFC9-26's sense (Polaris is not
in RFC 0009's `applies_to`); moving catalogs to their own routes; any change
to the machine payload's field set; any change to the observation pipeline,
the registry envelope, the consent scope or the response ceilings; any second
repository; scoring or judging the owner's walkthrough answers; and the
freshness *values* themselves, which are M2's subject.

## Collision and sequencing

**With M2 (register row P-69; overlap confined to the two files listed
below).** This packet's first draft recorded M2's head as `ec30494`, then
`e0ecdc8` (review 1, F7), then `68123fc` (review 2, G4), then `da1497b`
(this repair's own first draft) — four consecutive readings, each correct
when written and stale by the next one, which is the cost of citing a
branch by head rather than by register row (review 3, finding H4). This
section stops doing it: M2 is cited below by register row (P-69) and the
two shared files only. **One dated exception, for the record:** M2 is now
`f2f37dd` ("M2 funnel review 6 CONFIRM WITH EXCEPTIONS retained; L1–L4
applied"), one commit past `da1497b` [Observed: `git log --oneline
da1497b..HEAD` in the M2 worktree, read this session, 2026-09-14]. M2 still
has **six** slices at that head, slice 6's two files
(`polaris-reading.ts` line 44, `polaris.ts` lines 506–510) are untouched by
any M3 slice, and M2's slice 1 wording and its Q5 "mark, do not delete"
ruling are confirmed unchanged [Observed: the branch read read-only at
`f2f37dd` this session].

M2's slice 6 ("A lapsed reviewed selection announces itself") touches
`apps/three-surface-poc/src/polaris-reading.ts` line 44 and
`apps/three-surface-poc/src/polaris.ts` lines 506–510 — **neither of which any
M3 slice touches** — and M2's slice 1 wording and its Q5 "mark, do not delete"
ruling are confirmed unchanged at the current head (M2's own Gate 3 row and
Q5 text read this session, at `f2f37dd`, per the one dated line above). So
the shared surface is unchanged and M3's collision conclusion and
recommended sequence survive; only the head hash moved, again. M2's
review 3 withdrew a PWB-REQ-020 precedent its own review-2 repair had
asserted; this packet never relied on that precedent — its PWB-REQ-020
reading is its own, stated at Gate 2 and labelled Inferred.

The overlap is exact and small, and it is in two files [Observed: both read
this session on both branches]:

1. `apps/three-surface-poc/src/polaris-copy.ts` lines 46–49, the four
   freshness sentences. M2 slice 1 edits each unreachable one to carry the
   reason it is unreachable and, where one exists, the route that would
   make it reachable (M2's `superseded` marker has a reason and no route,
   by design; M2's copy oracle enforces the marker, not the route —
   review 2, G4). M3 slice 5 generates those same sentences from a
   freshness encoding table.
2. `apps/three-surface-poc/src/polaris.ts` lines 346–361, `claimStatesBlock`,
   which renders them — and specifically **line 357**, the freshness group,
   which is where the two changes meet. An earlier draft cited 346–353 in
   three places, a range that stops before the overlap and lands a reader on
   the lede and the Observed sentence (review 1, F8). M2 leaves the function
   alone and changes its input; M3 replaces its input with a generated one.
3. **M2 slice 5 and M3's freshness closure.** M2 slice 5 wires
   `assessCurrency`, whose `no-bound-declared` arm returns no `freshness`
   field, and M2's own Q7 recommends `stale` with the reason kept distinct
   precisely because RFC2-10 forbids a fifth value and PWB-REQ-007 forbids an
   absent field. Until M2's Q7 is ruled,
   `apps/three-surface-poc/src/polaris.ts` line 307 would mint `unstated`
   into `data-epistemic-freshness` on every
   unbounded class the moment that wiring lands. M3 slice 5's served-output
   closure assertion is what makes that fail loudly instead of rendering.
   **Slice 5's guard holds under either ruling, but the two packets'
   recommendations are not complementary — they are mutually exclusive for
   the same claims** (review 3, finding H3, folded in here rather than
   filed separately, since the repair is one clause). If the owner grants
   M2's Q7 as recommended, `claim.epistemic.freshness` is `'stale'` and
   `polaris.ts` line 307 never fires, foreclosing this packet's (b-iii) for
   those claims; if the owner grants this packet's Q2 as recommended, no
   value enters `data-epistemic-freshness` for them and M2's `stale` is
   contradicted. Granting both as recommended is not available. M2 decides
   the *value*, M3 guards the *vocabulary* — that much is true of the guard
   alone; the two recommendations stand as the owner's choice between them,
   not as a reconciled pair.

**Cross-packet note (review 2, G1).** M2's Q3, Q5 and Q7 all rest on the
same RFC2-10 sentence this packet's Q2 relies on — "a condition genuinely
outside the four is disclosed as a fact of the render, never dressed as a
freshness state" — and M2's own Q7 text already questions its own `stale`
recommendation against that sentence ("`stale` here is a candidate for
exactly that dressing"). P-69 and P-70 must therefore be ruled together: the
owner is reading one accepted clause across two packets, not answering two
independent questions.

**M2 lands first.** Its markers are content — a reason and, where one
exists, a route per unreachable value — that slice 5's table must carry as a
per-row field. In that order M3 inherits a tested invariant and converts
M2's copy oracle into an oracle over generated output. In the other order
M2's hand edit lands on generated copy and the next regeneration erases it.
M3 slices 1–4 touch neither file and may run at any time, including now, in
parallel with M2.

**With lane B (`syzygy-dov.17`, register row P-68, branch head `4090f98`).**
Lane B's semantic delta lets a tuple field "whose value is the same for every
claim under one enclosing scope" be carried once on that scope [Observed:
quoted from the branch's `proposed/spec.md.patch`]. Three consequences:

1. **The attribute M3 keys on is one lane B hoists.** Container mode hoists
   `data-epistemic-label` for **409 of 713** tuples and `data-challenge-state`
   and `data-evaluation-id` for all 713 [Observed: `hoistedPerField` in the
   branch's estimate record]. Any CSS rule or sweep keyed at the tuple would
   silently address 304. Q3's recommended answer builds the inheritance form
   from the start.
2. **Slice 1 does not change lane B's saving; a later choice might.** On the
   recommended design the encoding rides the existing attribute and adds no
   per-tuple bytes, so the 188,902-byte estimate stands. Arm (b) of Q3 — a
   non-hoistable per-claim carrier — would remove at least 409 × 32 = 13,088
   attribute bytes from it, plus a text component this packet has not
   separated out [Inferred: the estimate's `textBytesRemoved` is 25,397 across
   all seven fields and is not broken down per field in the record].
3. **Slice 4's fixture does not touch the live estimate, but slice 1 changes
   what a future hoist may do.** All 409 item rows are Observed today, which
   is exactly why the label is hoistable for them; the first live item-level
   Unknown inside one of those tables makes that scope's label non-hoistable.
   The pending Butlers P-60/P-61/P-62 repairs change which sources parse, so
   the figure should be re-derived after they land rather than assumed stable
   [Inferred].

**The sequence.**

1. **Rule P-68 first** (lane B), as M2's packet already recommends, because a
   PWB behaviour-amendment manifest binds post-apply bytes and only one such
   package can be open at a time.
2. **Run M3 slices 1–4 now**, in parallel with P-68 and M2. They touch no
   governed artifact, no spec text, no manifest and neither of M2's two files.
3. **Land M2's slice 1**, then **M3 slices 5–6** rebased onto its markers.
4. **Tell lane B's implementer that slice 1 exists** before the hoist is
   built, so the descendant selector and the expanding sweep are in the same
   change rather than a follow-up.
5. **If Q5 or Q6 is ruled to need a POC spec delta**, both queue behind P-68
   as a separate package, never as a second hunk in the first.

**Register rows.** Main's last note at `a9f671e` is P-67; **P-68 exists only
on `origin/agent/syzygy-dov.17`** and **P-69 only on
`origin/agent/syzygy-dov.2`**, so a reader following this packet's baseline to
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` finds neither
[Observed: both branches read this session]. This packet's questions would
queue as **P-70**.

## Gate 6 — Engineering bar

Acceptance, in the M1, M2 and P-63 shape:

1. **Retained measurement, before and after**, direct and tailnet host forms,
   at a named Syzygy commit and Butlers revision, in `docs/evidence/`, from a
   private daemon on port 0 with its own state directory — never the loopback
   daemon on 7478 — on a committed clean tree, because the observer refuses
   uncommitted inputs. The M3 numbers to record: the encoding population and
   how many members carry a declared class, per page and in total; the tier,
   freshness, challenge and label histograms with denominators; the depth of
   the first rendered Unknown; and the page's byte size on both forms against
   the 1,400,000-byte working target and the 2,097,152-byte ceiling.
2. **Every M1 invariant equal before and after** except what M3 deliberately
   changes: claim id set, tuple count, item and source populations, fragment
   targets with zero dangling, and the mount-prefixed link count stay equal;
   the declared-class count and the first-Unknown depth are expected to move,
   and the evidence file records both sides. Computed by script, never
   transcribed.
3. **Rule-6 mutation evidence for every new guard branch** — the four mutants
   named under each slice above — with each mutant's `old`/`new` fragment and
   the commit it ran at recorded, since ids and outcomes alone are not
   re-runnable. Fixtures are built in `beforeAll`, because a mutant that
   throws at describe time reports zero tests and scores as survived.
4. **Denominators on every sweep**, and an equality assertion against an
   independently computed population count, so a predicate that matches
   nothing fails instead of passing (verification rules 2, 4 and 9).
5. **PWB-REQ-020 parity checked per tuple, never per id** — 713 tuples over
   703 ids on this capture — with both id sets compared and both denominators
   reported.
6. **Accessibility re-run**: the keyboard and no-JS browser tests, contrast
   measured from served styles by a generic tool over every declared pair
   (POC-REQ-061's Oracle-independence clause), and the nonvisual path checked
   after slice 3 moves content into the opening band. CDP headless needs
   `Emulation.setFocusEmulationEnabled`, and no new fragment target may sit
   inside a `<details>`. **The walkthrough preflight
   (`apps/three-surface-poc/src/walkthrough-preflight.ts`) is re-run after
   slices 3 and 5**: it binds the generated glossary block, the
   `states.strengthen` sentence, the lede id and the `aria-describedby` on
   every tuple, and slice 5 regenerates exactly what it reads. It is
   mechanical readiness and never an owner verdict — readiness, execution
   record, owner judgment and act validity stay four states.
7. **`tsc -b packages/three-surface-poc-core` before the app typecheck**, the
   app suite twice and the full suite green; a fresh worktree needs `npm ci`
   inside it first.
8. **Conformance and oracle expected values hard-coded**, never imported from
   the module under test; every copy-oracle label a distinctive string, since
   a short label is "reached" by coincidence and proves nothing.
9. **Independent review in fresh context** before close, raw retained as a
   file whose name ends in `-RAW.md`; a re-issued raw is a second `-RAW.md`
   file, never an overwrite.

## Review 1 and repairs (2026-09-14)

An independent fresh-context review of this packet is retained verbatim at
`docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md` (31,503 bytes,
sha256 `1eca5fbac6fe95266ac4968f5b55ebf89e6e63544441383c545fb89b9140bc1f`;
both figures computed this session with `wc -c` and `sha256sum`). It reviewed
the packet at 71,765 bytes, sha256
`a5e4cc4f6aaf40031131dda2c8366e931f5bea7a8a2b9a45e2ec5da41d2a6383`, and the
evidence record at 16,677 bytes, sha256
`886cf48ef0e11c7ed72033b8334b1f61fd8db71cd3af5c5a3e97e2aeff9fb7ea`, on commit
`a9f671e` with both files untracked — the sizes and digests the raw itself
records, and the bytes those digests name. Its verdict word, copied exactly:
**REVISE**. Findings by severity as the raw states them: 4 blocking (F1–F4),
6 non-blocking (F5–F10), 4 editorial (F11–F14).

The review re-derived every load-bearing figure in the packet independently
and found them exact, including the three-method tuple count, the 1,087-member
cross-surface population, the 409/409 item-row sweep, the byte arithmetic and
the governance battery's last line. The defects are in the prose that reasons
over those figures.

| Finding | Severity | Disposition |
|---|---|---|
| F1 false `[Observed]` claim about POC-REQ-060/061 warrants | blocking | Accepted and repaired: the claim is withdrawn and both `warrants` blocks are quoted verbatim at their line numbers (955–964 and 999–1008), with the line-920 block identified as the preceding requirement's. POC-REQ-060 names no RFC 0009 clause; POC-REQ-061 names RFC9-48 only. The RFC9-46 "co-equal product surfaces" bridge is dropped with it. The paragraph's conclusion is unchanged and better supported |
| F2 false universal about ΔE76 over "named tokens" | blocking | Accepted and repaired, and extended: the colour-token population is named (ten declared colour tokens at `design-tokens.ts` lines 46–55, nine distinct values, 36 pairs), the full matrix recomputed this session, and the sub-26.74 tail enumerated. 7.85 is the **third**-smallest over the declared set and **seven** pairs sit below 26.74 — not five: review 1's own enumeration omitted `--line` ↔ `--void` at 23.27, and that correction is stated in place. The bar is restated over the five foreground tokens with the exclusion of the four ground tokens argued, where 7.85 is the smallest and 26.74 the next. Both JSON fields now carry the predicate, and the full matrix and the foreground subset are enumerated in the evidence record. The ≥ 26.7 bar survives |
| F3 vocabulary misassignment: a fourth member of a closed three | blocking | Accepted and repaired: "sibling surface states" is dropped from Q6 and slice 6 and RFC2-25's three-member list is quoted verbatim at `rendering-vocabularies.md`:169 with the statement that the proposal treatment is not one of them and is not being added to that family. The invented quotation is withdrawn and replaced with the clause's actual words ("a tier never becomes a fourth epistemic label"). The family is renamed **render disclosures** and stated to mint nothing — no fourth label, no seventh tier, no fourth sibling state. Contradiction is moved back to the tier table and slice 4, with `project-shape-model.ts` line 377 cited for tier `suspended`. Q6 is reframed so neither arm mints anything; the recommendation's substance survives |
| F4 closed-vocabulary guard one line short of RFC2-10 | blocking | Accepted and repaired: RFC2-10 is quoted verbatim at `snapshot-and-evaluation-core.md`:209 in Gate 2, lines 306–307 are shown together, and Q2's scope now covers both fields. The asymmetry is stated: RFC2-25 supplies an absence remedy, RFC2-10 forbids the minting in terms and supplies none, so arm (b) governs tier and is **not** lawfully available for freshness — the owner is shown the two arms that are (the renderer supplies one of the closed four, per M2's Q7; or the claim is held Unknown), and that PWB-REQ-007's Falsifier forbids simply omitting the field (the asymmetry as stated here was withdrawn after review 2, finding G1 — RFC2-10 supplies a disclosure remedy at lines 220–222 and arm (b) is not called unlawful for freshness; Q2 now states three arms, not two; this row stood unmarked until review 6, L1). Slice 5's freshness closure moves from the declared table to **served output** with the tuple count as denominator, mutant (e) forces `claim.epistemic.freshness` undefined, S9 gains the same limb, and the M2 slice-5 interaction is item 3 of the collision section |
| F5 the "735 … 0" headline flattens two defects | non-blocking | Accepted and repaired: Q1, the Motif, the cross-surface table, the funnel summary and the Q1-other-way paragraph now split 713 (no declared class **and** no distinguishing treatment) from 22 (the declared Unknown token under an undeclared, unlegended class), with the served rule quoted. Q1's recommendation is unchanged and the split is stated to sharpen it |
| F6 `walkthrough-preflight.ts` never named | non-blocking | Accepted and repaired: the file is added to slice 5's Gate 3 row as an unchanged-but-binding input, its `claimStrength` requirements (lines 203–226) are stated in the slice, Gate 6 item 6 re-runs it after slices 3 and 5, and mutant (f) removes the strengthen sentence and confirms readiness fails |
| F7 M2 head stale | non-blocking | Accepted and repaired at the time, and re-derived past the review twice since: M2 was `68123fc` when review 1 was answered, then review 2 (G4) found it stale a third time at `1befd6f`; re-derived again this repair pass at **`da1497b`** (reviews 4 and 5 retained, findings J1–J8 and K1–K9 repaired), still with six slices. Slice 6's two files (`polaris-reading.ts` line 44, `polaris.ts` lines 506–510) are untouched by any M3 slice at every head checked; M2's slice 1 wording and Q5 ruling are confirmed unchanged; the shared surface is unchanged and M3's conclusion and sequence survive. M2's review 3 withdrawal of a PWB-REQ-020 precedent is noted as one this packet never relied on. Per review 2's own note on this class, the collision section now cites M2 by register row (P-69) and the two shared files rather than repeating the head hash |
| F8 cited line range excludes the whole overlap | non-blocking | Accepted and repaired in all three places (Q7, the Gate 3 slice-5 row, collision item 2): 346–361, with line 357 named as the freshness group where the two changes meet |
| F9 freshness closure anchored to a source constant | non-blocking | Accepted and repaired: RFC2-10 is quoted in Gate 2 and named as the authority in the vocabulary table and in slice 5; `staleness.ts` line 18 is retained and labelled the implementation's echo |
| F10 "five rules, four meanings" omits that two never render | non-blocking | Accepted and repaired: the Measurements paragraph and Q6 now state that `class="unavailable-notice"` and `class="proposal"` each render 0 times on this capture and that the live reuse is 22 disclosure blocks and 1 proposal label beside the legend's 2 badges, all re-derived this session |
| F11 `cross-cutting.test.ts` characterised imprecisely | editorial | Accepted and repaired: restated in the review's terms — it iterates pages **and** the declared table's two entries, asserts every rendered `epistemic-*` class name is in the table, and its denominator is `pages(model)` over the declared table, never the rendered population |
| F12 emphasis added inside verbatim quotes of bound text | editorial | Accepted and repaired: the added bold is removed from all five quotes (PWB-REQ-007 ×2, PWB-REQ-016 ×2, VIS-7, CC-VIZ-1, POC-REQ-061), and, after review 2 (G3), from the RFC7-34 quote as well. RFC2-25's bolding matched the source and was already untouched; RFC7-34's did not until this repair — review 1 asserted it matched and was wrong. The new RFC2-10 and RFC2-25 quotes carry the source's own emphasis only |
| F13 evidence JSON `colour_method` names the wrong line range | editorial | Accepted and repaired: 46–55 in the evidence record, matching the measured population |
| F14 slice 5 cites `polaris-copy.ts` 38–51 | editorial | Accepted and repaired: 34–51 in the slice and in the Gate 3 row, with the composition stated (3 label, 7 tier, 4 freshness, 1 challenge, three group labels interleaved) |

**Two recommended answers changed their wording; five did not.** Q1, Q3, Q4,
Q5 and Q7 keep their recommendations word for word, with scope and citations
sharpened. Q2's recommendation was "**Arm (b).**" and is now "**Arm (b) for
the tier field; arm (b) is not lawfully available for the freshness field, and
the owner should see why**" — the tier ruling is unchanged; the freshness half
is new and is the substance of F4 (that freshness wording was itself
withdrawn after review 2, finding G1; see the review-2 section). Q6's recommendation was "**Yes, with a
`--proposed` token at a stated perceptual distance**" and is now "**Yes — a
`--proposed` token, declared as a render-disclosure encoding, at a stated
perceptual distance**" — the answer is the same and its framing no longer
routes an implementer into a closed vocabulary (F3), and its measurable bar
now names the population it holds over (F2). Q5's recommendation is unchanged
but now carries three constraints rather than two. (Q2's freshness
recommendation changes again after review 2 — see below.)

**Every repair above post-dates the review.** By verification rule 10 the
review binds the bytes it names — the 71,765-byte packet and the 16,677-byte
evidence record whose digests it records — and not these. The current bytes
are uncovered until a second independent fresh-context review confirms them;
its raw will be retained as a second `-RAW.md` file, never an overwrite of the
first.

## Review 2 and repairs (2026-09-14)

A second independent fresh-context review of this packet — of the packet,
its evidence record and the P-70 note and row — is retained verbatim at
`docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-2-RAW.md` (48,381 bytes,
sha256 `a04b20517539e971c1e192015329dd39a2e2f536b52c06fffdce473177397012`;
both figures computed this session with `wc -c` and `sha256sum`, matching
the raw's own header exactly). It reviewed the packet, the evidence record
and the register at commit `573abb0` — the four files review 1 also named,
all tracked at that commit. Its verdict word, copied exactly: **REVISE**.
Findings by severity as the raw states them: 1 blocking (G1), 5
non-blocking (G2–G6), 3 editorial (G7–G9) (review 3, finding H9: the
earlier "REVISE — one blocking, five non-blocking, three editorial" read as
a verbatim copy but was assembled from two places in the raw — the verdict
line at :567 is exactly "Verdict: REVISE," with the counts stated
separately at :564–566).

The review re-derived every load-bearing figure in the packet a second time
— all 36 ΔE76 pairs, the three-method tuple count, the 1,087-member
cross-surface population, the 409/409 by-id item sweep, the lane B hoist
figures, the byte arithmetic and the governance battery — and found them
exact. It also verified all fourteen review-1 findings against the current
bytes: **10 REPAIRED, 4 PARTIAL** (F4, F6, F7, F12 partial; **0 NOT
REPAIRED**), computed from the raw's own F1–F14 table
(`...-2-RAW.md`:461–474, one row per finding, denominator 14; review 3,
finding H5) — the partials being exactly the sites this repair pass closes.
The raw's own totals line (:476, "9 REPAIRED, 5 PARTIAL") and its summary
sentence (:546–547, "eleven ... repaired cleanly") both disagree with the
table and with each other; none of the raw's three figures agree, and this
packet had transcribed the totals line instead of counting the table.

| Finding | Disposition |
|---|---|
| G1 blocking — RFC2-10 supplies the absence route the packet said it lacked, foreclosing a lawful third arm on Q2's freshness limb | Accepted and repaired: the Gate 2 quote is extended through the clause's remedy sentence (`snapshot-and-evaluation-core.md`:220–222, verbatim, no added emphasis); "supplies no absence marker at all" is withdrawn from the packet's four prose sites and the register row — but **not** from the evidence record's own `vocabulary_versus_rendered.freshness_mint_hazard` field, a fifth site this repair pass missed and review 3 found still standing (finding H1; corrected in the review-3 section below), nor from two further sites review 6 found (L1) — the F4 row of the review-1 disposition table above and its record twin `review1.dispositions.F4`, both stating the withdrawn proposition unmarked in the present tense until marked in place after review 6, seven sites in all; the asymmetry is restated as a rendering remedy (RFC2-25) against a disclosure remedy outside the slot (RFC2-10); Q2's freshness limb now states three lawful arms (b-i/b-ii/b-iii), puts the PWB-REQ-007 tension to the owner unresolved, and recommends (b-iii) labelled `[Inferred]` without calling (b-i) or (b-ii) unlawful; the cross-packet link to M2's Q3/Q5/Q7 is stated in Q2, Q7 and the collision section |
| G2 non-blocking — the preflight does not require the `unstated —` sentence; an existing test does | Accepted and repaired: slice 5's readiness paragraph now names `aria-describedby` as the preflight's third true example and states that `walkthrough-preflight.ts` builds its required-term set from the model, never the render, so `unstated` never enters it; the guard is restated as `polaris-first-reading.test.ts` line 88 |
| G3 non-blocking — F12 was not fully repaired: added bold survives in the RFC7-34 quote, and the disposition row asserted otherwise | Accepted and repaired: the second bold span is dropped from the RFC7-34 quote at Gate 2, matching `rendering-and-surface.md`:241–243 verbatim; the F12 disposition row is corrected to say RFC7-34's bolding did not match until this repair |
| G4 non-blocking — the M2 head is stale a third time, and one thing M3 relies on changed (M2's marker wording) | Accepted and repaired: the collision section now names M2's head once, as `da1497b` (2026-09-14, reviews 4 and 5 retained, J1–J8 and K1–K9 repaired), and cites M2 elsewhere by register row (P-69) and the two shared files; the structural collision and sequence are confirmed unchanged by reading M2's own Gate 3 row and Q5 text at `da1497b`; the marker description in slice 5 and collision item 1 is weakened to "the reason and, where one exists, the route" |
| G5 non-blocking — the P-70 register row states a depth (25.55%) that belongs to a different object than the one it names | Accepted and repaired in the register: the row now reads "57.72% and 25.70%" |
| G6 non-blocking — RFC2-26 is never cited, though it is the clause Gate 5 discharges for slices 5–6 | Accepted and repaired: RFC2-26 is quoted at Gate 2 (`rendering-vocabularies.md`:196), and Gate 5's slices-5/6 paragraph names POC-REQ-061 as the mapping requirement that discharges it |
| G7 editorial — "below 26.74" is 0.0029 off the pair's own computed value (26.7371) | Accepted and repaired: all three packet sites now read "below the `--ink` ↔ `--muted` floor (26.74 to two decimals, 26.7371 computed)"; the evidence record gains a precision note beside the existing `pairs_below_26_74` fields |
| G8 editorial — a doctrine quote with no anchor, applied to a different subject by analogy | Accepted and repaired: `trust-and-evidence.md`:101 is anchored and the citation is marked "by analogy" with its actual subject (a superseded observation record) stated |
| G9 editorial — the register softens a lower-bound cost into an approximate one | Accepted and repaired in the register: Q3's arm (b) now reads "at least 13,088 attribute bytes plus an unseparated text component" |

**F-partial note.** Review 2 confirmed F4, F6, F7 and F12 as PARTIAL against
the bytes it read (the mechanical repairs held; each had one remaining
defect — respectively G1, G2, G4 and G3). This repair pass closes all four
partials at their named sites; it does not re-litigate the REPAIRED findings
above it.

**Q2's freshness recommendation changed, plainly.** Before this repair the
recommendation read "arm (b) is not lawfully available for the freshness
field, and the owner should see why" — foreclosing a third arm on a
truncated quote (G1). It now reads (Q2's Recommended column, in full): "Arm
(b) for the tier field. For the freshness field, three lawful arms follow
from RFC2-10's own text, and the owner should choose among them — none is
unlawful," recommending **(b-iii)** — RFC2-10's own render-fact disclosure,
outside the `data-epistemic-freshness` slot — while naming (b-i) and (b-ii)
as live, lawful alternatives. The earlier "not lawfully available" is
withdrawn, not merely reworded: a third arm exists now that did not before
this repair.

**Every repair above post-dates review 2.** By verification rule 10, review
2 binds the 102,085-byte packet and 30,747-byte evidence record it read at
`573abb0` — and not the current bytes. The current bytes are uncovered
until a third independent fresh-context review confirms them; its raw will
be retained as a third `-RAW.md` file, never an overwrite of the first two.

## Review 3 and repairs (2026-09-14)

A third independent fresh-context review of this packet — of the packet,
its evidence record and the P-70 note and row — is retained verbatim at
`docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-3-RAW.md` (42,726 bytes,
sha256
`7154f1f3972cfc73619694d48851f4368a8eb7fdce77cadb81493290f82c5aa6`; both
figures computed this session with `wc -c` and `sha256sum`, matching the
raw's own header table). It reviewed the packet, evidence record and
register at commit `b34fca7`. Its verdict word, copied exactly: **REVISE**.
Findings by severity as the raw states them: one blocking (H1); six
non-blocking (H2–H7); four editorial (H8–H11).

Every finding was re-derived against source this session before being
applied, never taken on the raw's word alone — the sha256 above, the
RFC2-10 clause text at `snapshot-and-evaluation-core.md` lines 209–223, the
M2 worktree's head (`git log --oneline -1` and `da1497b..HEAD`), the
`api-poc.json` machine answer (1,149 objects, 1,148 distinct ids), the
retained capture's `.proposal-label` count and depth, review 2's own F1–F14
table (`...-2-RAW.md`:461–474), and the literal search for
"together"/"ruled together"/"read together" over the P-70 note and row
were each independently run this session, not copied from the raw's
narration. All eleven findings confirmed.

| H | Severity | Verdict | Evidence |
|---|---|---|---|
| H1 | blocking | **CONFIRMED — PARTIAL at `f35a25f`, completed after review 4 (J1, J3, J7)** | The evidence record's `vocabulary_versus_rendered.freshness_mint_hazard` field (json :282) still asserted "supplies no absence marker" and "arm (b) of Q2 is not available for freshness" after review 2's repair pass withdrew the same wording from the packet's four sites and the register row. Re-derived: the field was rewritten to state RFC2-10's remedy at lines 220–222 (this row first said 220–223, taking in the separate orthogonality sentence at 222–223 — one extent settled after review 5, K3) and three arms — but the three it enumerated did not match the packet's and register's (b-i)/(b-ii)/(b-iii) (review 4, J3; now the packet's wording verbatim, the mismatched text kept and marked); this row's earlier claim that `closed_freshness_vocabulary_authority` "is extended through the remedy sentence with the elision marked" was **false** — the field still ended at line 214 with no marker (review 4, J1; now extended through line 223); and of the two disposition rows that claimed the withdrawal was complete, only the packet's review-2 G1 row was corrected — the record's `review2.repairs.G1` still claimed "withdrawn at all four packet sites and the register row" with no fifth site (review 4, J1; now corrected). Swept the packet, record and register for `supplies no`, `no absence`, `not lawfully available`, `unlawful`, `no remedy` and `supplies none`: 25 literal occurrences over 2,482 lines across the three files as of `b34fca7`, the bytes review 3 read — 2,482 counting each file's trailing line, 2,479 by `wc -l` (the stamp review 4, J7, asked for; the review-4 repair wrote instead that the figure was "taken on the working tree … reproducible from no commit", which review 5, K1, showed false — the figure is exact at `b34fca7`, and only the line-count convention differed; re-derived at `f35a25f` under the same convention: 41 over 2,700 lines, 2,697 by `wc -l`, with the same six literals, the growth being review-history text quoting the withdrawn wording); of those, only the one field above was a live, non-historical false assertion, one more pair (the two disposition rows) wrongly claimed completeness, and `review1.recommended_answers_changed.Q2` (H2) lacked an in-place marker — every other occurrence is either current lawful-arms language, an existing in-place withdrawal marker, or a review-history quote already framed as superseded — a three-way classification review 6 (L1) showed incomplete: two hits fit none of the three, the review-1 disposition table's F4 row and its record twin, review-history text that stated the withdrawn proposition in the present tense with no marker; both are now marked, and the sort rule has a fourth box (review-history text stating the withdrawn proposition unmarked), which held the two L1 hits and, after the repair, holds 0 of the 45 hits over 3,051 lines (3,054 counting each file's trailing line): box (1) current lawful-arms language 6, box (2) in-place withdrawal markers 13, box (3) review-history text framed as superseded, the sweep's own literal lists included, 26 (review-6 section) |
| H2 | non-blocking | **CONFIRMED — REPAIRED** | The evidence record's `review1.recommended_answers_changed.Q2` field carried the withdrawn "not lawfully available for the freshness field" wording with no marker, unlike the packet's own parallel passage (:1393 area), which marks it in place. Appended the same in-place marker to the JSON field, without deleting the superseded wording |
| H3 | non-blocking | **CONFIRMED — REPAIRED** | The packet states three times that P-69 and P-70 must be ruled together; the P-70 row and note carried none of it — swept for "together", "ruled together" and "read together": 0 hits in both, confirmed this session. Added one clause to the P-70 row. Collision item 3's "the two moves are complementary" read, in context, as though M2's `stale` and this packet's (b-iii) recommendations were reconciled; they are mutually exclusive for the same claims. Restated in place, without smoothing: both recommendations stand as the owner's choice, not as a reconciled pair |
| H4 | non-blocking | **CONFIRMED — REPAIRED** | M2's head was named as `da1497b`, a fourth stale reading; `git -C .../scratchpad/m2wt log --oneline -1` this session returns `f2f37dd` (M2 funnel review 6, CONFIRM WITH EXCEPTIONS), one commit past `da1497b`. The collision section now cites M2 by register row and the two shared files as its rule, with `f2f37dd` named once, dated, as the one exception, and the substance (six slices, slice 6's two untouched files, Q5's ruling) re-confirmed at that head this session |
| H5 | non-blocking | **CONFIRMED — PARTIAL at `f35a25f`, completed after review 4 (J2)** | Review 2's own F1–F14 table (`...-2-RAW.md`:461–474) counts to 10 REPAIRED / 4 PARTIAL by row (verified this session, denominator 14); its totals line (:476) says "9 REPAIRED, 5 PARTIAL" and its summary (:546–547) says "eleven ... repaired cleanly" — three disagreeing figures in one raw. The packet and record had copied the totals line. The packet's review-2 section now states 10/4, computed from the table, with the raw's internal disagreement noted; the record's `review2.f_verification_against_review_1` still read `"REPAIRED": 9` at `f35a25f`, and its `review3.repairs.H5` claimed "stated in both places" — both corrected after review 4, finding J2, with the denominator 14 stated in the record |
| H6 | non-blocking | **CONFIRMED — REPAIRED** | Re-derived from the retained `api-poc.json`: all 11 of 713 human-side Unknown tuples match a machine object whose `epistemic` carries no `tier` key at all (`['freshness','label','reasons']` only), confirming Q2's tier-limb justification (PWB-REQ-007's "carry the closed label, tier … that govern it") holds on the human channel only. Added to Gate 2's PWB-REQ-020 paragraph as a disclosure, not a resolution |
| H7 | non-blocking | **CONFIRMED — REPAIRED** | Re-derived on the retained capture: `class="proposal-label"` renders once, at 56.29% depth, styled `color: var(--unknown)` — exactly the negative sweep's own falsifier and exactly what slice 6 exists to repair, so slice 2 would land red against an element the packet defers to slice 6. Named in slice 2 with the count and depth; this packet's stated choice is to pull `.proposal-label`'s one rule into slice 6's `--proposed` token now, alongside slices 1–4, rather than carry a declared exception — the alternative is named as lawful too |
| H8 | editorial | **CONFIRMED — REPAIRED** | The baseline sentence claimed the worktree was "at the same commit" as `a9f671e`; it is two commits ahead (`573abb0`, then `b34fca7`). Corrected to state the worktree branches from `a9f671e` with only this packet's own artifacts on top |
| H9 | editorial | **CONFIRMED — REPAIRED** | Review 2's exact verdict line (`...-2-RAW.md`:567) is "Verdict: REVISE"; the severity counts are a separate sentence at :564–566. The packet and record had assembled "REVISE — one blocking, five non-blocking, three editorial" from both and labelled it a verbatim copy — that exact string occurs 0 times in the raw. Split into the bare verdict word plus the counts, matching how the review-1 section already does it |
| H10 | editorial | **CONFIRMED — REPAIRED** | The PWB-REQ-007 and PWB-REQ-020 block quotes drop Observable, Oracle and Oracle-independence bullets between the retained ones with no marker, while the packet's other elisions are marked. Added `…` between the retained bullets in both quotes |
| H11 | editorial | **CONFIRMED — REPAIRED** | The Gate 2 RFC2-10 quote stopped at "freshness state." (line 222), one sentence short of the clause's own end at line 223 ("Freshness is orthogonal to the three labels and the tier registry; it never substitutes for either."), while two sites called it "quoted in full". Extended the quote through line 223 — the clause's full extent, confirmed against source this session — so "quoted in full" is now accurate at both sites, and added a paragraph weighing the orthogonality sentence against Q2's arm (b-ii) |

**No recommended answer changed.** All seven questions' recommendations are
word for word what they were after review 2's repairs; this pass corrects
the evidence record, the register and the collision framing, not the
packet's substantive conclusions. Q2's freshness recommendation — (b-iii),
with (b-i) and (b-ii) named as live and lawful — stands unchanged; it is
now also disclosed as mutually exclusive with M2's `stale` recommendation
for the same claims (H3), which is a sharpening of the owner's choice, not
a change to either side of it.

**Every repair above post-dates review 3.** By verification rule 10,
review 3 binds the 115,201-byte packet, 36,743-byte evidence record and
31,054-byte register it read at `b34fca7` — and not the current bytes. The
current bytes are uncovered until a fourth independent fresh-context review
confirms them; its raw will be retained as a fourth `-RAW.md` file, never
an overwrite of the first three.

## Review 4 and repairs (2026-09-15)

A fourth independent fresh-context review of this packet — of the packet,
its evidence record and the P-70 note and row — is retained verbatim at
`docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-4-RAW.md` (40,037 bytes,
sha256
`2c3a91917d957ad58a16b5c2cddbcc5326c412e4c35b89531c317c41b6a4d947`; both
figures computed this session with `wc -c` and `sha256sum`). It reviewed
the packet (129,183 bytes), evidence record (42,787 bytes) and register
(32,136 bytes) at commit `f35a25f`. Its verdict word, copied exactly:
**REVISE**. Findings by severity as the raw states them: three blocking
(J1–J3); three non-blocking (J4–J6); three editorial (J7–J9).

Every finding was re-derived against source this session before being
applied — the record's fields at their cited lines, the RFC2-10 clause
text at `snapshot-and-evaluation-core.md` lines 209–223, review 2's own
F1–F14 table (`...-2-RAW.md`:461–474) recounted by row, the cross-surface
table above re-summed both ways, the retained `api-poc.json` machine
answer re-walked for objects lacking a `tier` key, the three files' line
counts at `b34fca7` and `f35a25f`, and the worktree's own commit list —
never taken on the raw's word alone. All nine findings confirmed (the
J7 disposition this pass then wrote was itself wrong — review 5, K1). The
common shape of the three blocking findings is one the review-3 repair
pass owns: it reported three record repairs as done that were done in the
packet only, or done differently in the record, and review 3's own
disposition table recorded them as REPAIRED on the strength of that
report. The H1 and H5 rows above are now restated to what was actually
done and marked PARTIAL at `f35a25f`.

| J | Severity | Verdict | Evidence |
|---|---|---|---|
| J1 | blocking | **CONFIRMED — REPAIRED** | The record's `closed_freshness_vocabulary_authority` (json :279) still ended at `snapshot-and-evaluation-core.md` line 214 ("it does not carry.") with no elision marker, while the H1 row above said it had been "extended through the remedy sentence with the elision marked", and the record's `review2.repairs.G1` (json :741) still claimed the withdrawal complete at "all four packet sites and the register row" with no fifth site. Both corrected: the quote now runs verbatim from line 209 to the clause's end at 223; G1 names the record as the fifth site the review-2 pass missed; the H1 row states the three things that were and were not done, and its verdict is PARTIAL at `f35a25f` |
| J2 | blocking | **CONFIRMED — REPAIRED** | Recounted review 2's F1–F14 table by its fifth column: REPAIRED = F1, F2, F3, F5, F8, F9, F10, F11, F13, F14 (10); PARTIAL = F4, F6, F7, F12 (4); denominator 14. The record's `review2.f_verification_against_review_1` (json :730) still read `"REPAIRED": 9` and its `review3.repairs.H5` (json :808) said 10/4 was "stated in both places". Corrected to 10 with the denominator and the raw's disagreeing totals noted in the record; H5's disposition and the H5 row above restated; H5 marked PARTIAL at `f35a25f` |
| J3 | blocking | **CONFIRMED — REPAIRED** | The record's `freshness_mint_hazard` (json :282) enumerated three freshness arms — "render only the four declared states and no absence", "disclose … beside the tuple", "the disclosure route with the absence named in the legend" — that matched neither Q2's nor the register's (b-i) renderer supplies one of the closed four / (b-ii) held Unknown and not rendered as though it had a freshness state / (b-iii) disclosed as a fact of the render outside the `data-epistemic-freshness` slot. The record now carries the packet's wording verbatim, with the mismatched enumeration quoted and marked withdrawn in the same field |
| J4 | non-blocking | **CONFIRMED — REPAIRED** | POC-REQ-060's Case counts "all three surfaces"; Home is not one of them. The population offered as the requirement's was the four-page 1,087. Re-summed: three-surface 1,052 (735 + 299 + 18), Polaris share 69.87%; four-page 1,087, 67.62%. Both now stated, with the reason the sweep is deliberately wider (Home imports the token set slices 5 and 6 change), in the population prose, Q1, the funnel summary, the denominators paragraph, the register row and the record's `cross_surface_population`; "the other three surfaces" is replaced by the three pages' names |
| J5 | non-blocking | **CONFIRMED — REPAIRED** | Gate 2's H6 disclosure (the tier field has no machine-channel counterpart for the 11 Unknown tuples) reached the packet and not the P-70 row. Re-derived: 12 of 1,149 machine objects carry an `epistemic` without a `tier` key, all labelled Unknown; each of the 11 human-side Unknown tuples matches one. One clause added to the row's Q2 limb naming the PWB-REQ-020 parity question arm (b) carries, disclosed and not resolved |
| J6 | non-blocking | **CONFIRMED — PARTIAL at `76e897f`, completed after review 5 (K2)** | The handoff conditioned the immediate run of slices 1, 2 and 4 on Q1, Q3 and Q4, while slice 2 as sequenced pulls one rule of slice 6's `--proposed` token forward — a Q6 dependency. Q6 added to the condition, with the dated-exception alternative named for the case where Q6 is answered otherwise |
| J7 | editorial | **CONFIRMED — REPAIRED, and the repair corrected after review 5 (K1)** | This row first read: "The H1 row's sweep figure (25 over 2,482 lines) was taken on the working tree during the review-3 repair; the three files sum to 2,479 lines at `b34fca7` and 2,697 at `f35a25f`, so the figure is reproducible from no commit." That was false, and review 4's own J7 text had already said so (`…-4-RAW.md`:359–361: "at `b34fca7`, 25 occurrences over 2,482 lines — exact"). Re-derived after review 5: at `b34fca7` the six literals occur 25 times and the three files carry 2,479 lines by `wc -l`, 2,482 counting each file's trailing line — the same population under two conventions, and the figure matches that one commit exactly. The H1 row now carries the stamp J7 asked for, both conventions named, with the `f35a25f` pair (41 over 2,700, or 2,697 by `wc -l`) given like for like |
| J8 | editorial | **CONFIRMED — REPAIRED** | The H8 correction enumerated two commits above `a9f671e`; there were three at `f35a25f` and one more after this repair. The bracket now states that the worktree carries only this packet's own commits and points at `git log` instead of counting them |
| J9 | editorial | **CONFIRMED — REPAIRED** | Gate 3's six-limb `[Observed]` bracket ended with the scope limb ("every slice implements behaviour the signed change already requires"), which Gate 5 argues and the packet labels `[Inferred]` elsewhere. Split: Observed for the five textual absences, Inferred for the scope limb with the pointer to Gate 5 |

**No recommended answer changed.** All seven questions' recommendations
are word for word what they were after review 2's repairs; this pass
corrects the evidence record, two disposition rows that overstated the
review-3 repair, the population framing and the register's Q1 and Q2
limbs. Q1 now carries the requirement's own three-surface denominator
beside the four-page one, and Q2's register limb now carries the
machine-channel tier disclosure the packet already made — neither moves a
recommendation.

**Every repair above post-dates review 4.** By verification rule 10,
review 4 binds the 129,183-byte packet, 42,787-byte evidence record and
32,136-byte register it read at `f35a25f` — and not the current bytes.
The current bytes are uncovered until a fifth independent fresh-context
review confirms them; its raw will be retained as a fifth `-RAW.md` file,
never an overwrite of the first four.

## Review 5 and repairs (2026-09-15)

A fifth independent fresh-context review — of the packet, its evidence
record and the P-70 note and row — is retained verbatim at
`docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-5-RAW.md` (36,904 bytes,
sha256
`cbc9deac4698656e9434694741fdf66e91c60c179cd3a6942c6036e9331146d7`; both
figures computed this session with `wc -c` and `sha256sum`). It reviewed
the packet (139,050 bytes, sha256
`254f72e3308052944b7e19276d948d10c15132765ea4a2395c50a75705bcd45d`),
evidence record (50,219 bytes, sha256
`52e14c419ad62a6ad603067152af250de4a887ee297d0315eaa24fecedea2f45`) and
register (33,783 bytes, sha256
`1754fe069c7635a0ae35b3b958a24e33e54f98c29b5ed4283d135a34daa0ef31`) at
commit `76e897f`. Its verdict word, copied exactly: **REVISE**. Findings
by severity as the raw states them: one blocking (K1); three non-blocking
(K2–K4); two editorial (K5–K6). It verified J1–J9 against the current
bytes as 7 REPAIRED, 1 PARTIAL (J6, the funnel-summary handoff line, K2)
and 1 NOT REPAIRED (J7, K1) over a denominator of 9 — both complete at
this commit — and spot-checked every earlier finding; nothing previously
accepted regressed, and no recommendation is touched by any finding
(the counts added after review 6, L4).

Every finding was re-derived this session before being applied. K1: the
six literals over the three files at `b34fca7` give 25 occurrences, and
the files carry 2,479 lines by `wc -l`, 2,482 counting each file's
trailing line — so the review-4 repair's "reproducible from no commit"
was false, and review 4's own J7 text (`...-4-RAW.md`:359–361) had
already said the figure was exact at `b34fca7`; the same pair at
`f35a25f` is 41 over 2,697 / 2,700, and at `76e897f` 42 over 2,805 /
2,808. K2: the funnel summary's handoff line named Q1 and Q3 only and
"slices 1-4 now" against the handoff section's four answers and "1, 2
and 4 now, slice 3 next". K3: `snapshot-and-evaluation-core.md` line 219
carries the parity rationale; the prohibition sentence runs 212–214; the
remedy sentence 220–222; the orthogonality sentence 222–223. K4:
`review3.repairs.H1` carried no marker while its siblings did. K5: the
note's stamp and its "every finding repaired" against the packet's own
10 REPAIRED / 4 PARTIAL. K6: the record's arm text matches the packet
character for character and the register's wording differs.

| Finding | Severity | Disposition |
|---|---|---|
| K1 | blocking | **CONFIRMED — REPAIRED.** The H1 row now carries the stamp J7 asked for — 25 over 2,482 as of `b34fca7`, both conventions named — with the `f35a25f` pair given like for like; the J7 row quotes its own false text and restates it; the record's `review4.re_derived_before_applying.J7` and `review4.repairs.J7` are marked superseded on their lines; the review-4 section's "All nine findings confirmed" now notes that the J7 disposition it wrote was itself wrong |
| K2 | non-blocking | **CONFIRMED — REPAIRED.** The summary block's handoff line names Q1, Q3, Q4 and Q6 and "slices 1, 2 and 4 now, slice 3 next", with its earlier text quoted in place |
| K3 | non-blocking | **CONFIRMED — REPAIRED.** The record's `freshness_mint_hazard` anchors the prohibition at lines 212–214 (the reviewer wrote 213–214; the sentence's first word sits at the end of line 212) and quotes it; the remedy's extent is 220–222 at the G1 row, the H1 row and `review3.repairs.H1`, with 222–223 named separately as the orthogonality sentence |
| K4 | non-blocking | **CONFIRMED — REPAIRED.** `review3.repairs.H1` carries the J3 marker its siblings carry |
| K5 | editorial | **CONFIRMED — REPAIRED.** The P-70 note is stamped for both dates, its review-1 clause and the row's review-1 citation read "fourteen findings, ten repaired in that pass and four closed after review 2 (10 REPAIRED / 4 PARTIAL as review 2 verified)" |
| K6 | editorial | **CONFIRMED — REPAIRED.** The record says the arms are in the packet's own words, which the P-70 row paraphrases clause for clause; `review4.repairs.J3` marked on its line |

No recommended answer changed: all seven recommendations stand word for
word as after review 2. The sweep the H1 row names, re-run over the three
files at the bytes this section describes: 42 occurrences over
2,932 lines by `wc -l` (2,935 counting each file's trailing
line), every one inside review-history or lawful-arms text — a
classification review 6 (L1) found too coarse: "inside a review-history
section" and "framed as superseded" are different tests, and two of
the 42 were review-history text stating the withdrawn proposition
unmarked (see the review-6 section).

**Every repair above post-dates review 5.** By verification rule 10,
review 5 binds the 139,050-byte packet, 50,219-byte evidence record and
33,783-byte register it read at `76e897f` — and not the current bytes.
The current bytes are uncovered until a sixth independent fresh-context
review confirms them; its raw will be retained as a sixth `-RAW.md` file,
never an overwrite of the first five.

## Review 6 and repairs (2026-09-15)

A sixth independent fresh-context review — of the packet, its evidence
record and the P-70 note and row — is retained verbatim at
`docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-6-RAW.md` (39,570 bytes,
sha256
`384f398c3041dc9e59031c84976e61419cedc904c193f3c249af865eebe48ead`; both
figures computed this session with `wc -c` and `sha256sum`). It reviewed
the packet (144,850 bytes, sha256
`11766f08d8f227422021c2de7475f7ef20d50a8e2fd83f741f5506b94e310a45`),
evidence record (55,345 bytes, sha256
`4c61e5ccc8f51fb03a814914b918069a67806e71b1ab1a5a1872e0e51a4068ee`) and
register (35,006 bytes, sha256
`be27c3bb880f6d8c08ed3015f0c708ef8419e481447edea30be2f42a3953d852`) at
commit `9cb4d65`. Its verdict word, copied exactly: **REVISE**. Findings
by severity as the raw states them: one blocking (L1); three non-blocking
(L2–L4); two editorial (L5–L6). It verified K1–K6 against the current
bytes as 6 REPAIRED over a denominator of 6, re-derived the sweep pair at
three commits without a discrepancy, and spot-checked every earlier
finding; nothing previously accepted regressed, and no recommendation is
touched by any finding.

Every finding was re-derived this session before being applied. L1: the
review-1 disposition table's F4 row (:1461) and the record's
`review1.dispositions.F4` both stated the reading review 2's G1 withdrew
— present tense, no marker — while the G1 row counted the sites at four
plus the register plus a fifth and the H1 row sorted every sweep hit into
three boxes that neither occurrence fits; the correct reading with its
marker sits at :1476. L2: the record's `m2_collision` block still carried
`da1497b` as M2's head in four fields after review 3's H4 moved the packet
to `f2f37dd`; the M2 worktree's head was read read-only this session and
is `f2f37dd`. L3: Q7's recommended answer said "five reviews retained"
for M2 against six `…-RAW.md` files in the M2 worktree's `docs/reviews/`
and the collision section's own "review 6" line. L4: the J6 row read a
bare "REPAIRED" while review 5 verified it PARTIAL, and the review-5
section carried no J1–J9 counts. L5: `snapshot-and-evaluation-core.md`'s
orthogonality sentence begins on line 222, so "line 223 adds" was one
line short. L6: the record's two sibling offset fields anchored on
different characters (the class attribute at 378,604 for the first
Unknown; the element's opening `<` at 380,767 for the first tuple).

| Finding | Severity | Disposition |
|---|---|---|
| L1 | blocking | **CONFIRMED — REPAIRED.** The F4 row and `review1.dispositions.F4` are marked in place, the withdrawn text kept; the G1 row now counts seven sites; the H1 row's classification has a fourth box — review-history text stating the withdrawn proposition in the present tense unmarked — and states how many hits it held (two) and holds now (none); `review5.sweep_after_repair.result` is marked superseded on its line and the review-5 section's closing sweep sentence says the same; the record's `review6.sweep_after_repair` publishes the sort rule and the count per box |
| L2 | non-blocking | **CONFIRMED — REPAIRED.** `m2_collision.head` reads `f2f37dd` with the ladder extended on the same line, `head_note` in the past tense, the shared-surface key re-keyed to `f2f37dd`, `structural_collision_confirmed_by` dated to both reads; `review1.dispositions.F7` carries the H4 marker |
| L3 | non-blocking | **CONFIRMED — REPAIRED.** Q7's parenthetical reads six reviews retained, M2 at `f2f37dd` with review 6 CONFIRM WITH EXCEPTIONS, the earlier "five" kept and marked; the recommendation's premise and answer are unchanged |
| L4 | non-blocking | **CONFIRMED — REPAIRED.** The J6 row reads "PARTIAL at `76e897f`, completed after review 5 (K2)"; the review-5 section states 7 REPAIRED, 1 PARTIAL, 1 NOT REPAIRED over 9 |
| L5 | editorial | **CONFIRMED — REPAIRED.** `freshness_mint_hazard` reads "lines 222–223 add" with the earlier single line kept on the line |
| L6 | editorial | **CONFIRMED — REPAIRED.** One anchor adopted, the element's opening `<`: the first-Unknown offset reads 378,599 with the earlier 378,604 kept, an `offset_anchor` field sits beside both offsets, and the depth percentages are unchanged at two decimals |

No recommended answer changed: all seven recommendations stand word for
word as after review 2; Q7's parenthetical count was corrected without
moving its premise or its answer. The sweep the H1 row names, re-run over
the three files at the bytes this section describes and every hit sorted
by the four-box rule the record's `review6.sweep_after_repair` states:
45 occurrences over 3,051 lines by `wc -l` (3,054
counting each file's trailing line) — box (1) current lawful-arms language 6, box (2) in-place withdrawal markers 13, box (3) review-history text framed as superseded, the sweep's own literal lists included, 26 — and box (4), the box
review 6 found occupied, holds 0.

**Every repair above post-dates review 6.** By verification rule 10,
review 6 binds the 144,850-byte packet, 55,345-byte evidence record and
35,006-byte register it read at `9cb4d65` — and not the current bytes.
The current bytes are uncovered until a seventh independent fresh-context
review confirms them; its raw will be retained as a seventh `-RAW.md`
file, never an overwrite of the first six.

## Funnel summary

```
## Feature Request: M3 - Honest encoding at the gate: POC-REQ-060 on Polaris and a real sweep
Size: medium (slices 1-4) / medium-large (slices 5-6)
Baseline: Syzygy a9f671e; capture = lane A after/tailnet, 1,484,487 bytes, Butlers 2e3bac97790b
- G1 Motif: 735 of Polaris's body epistemic encodings carry no declared class - 713 of them (the claim tuples) with no distinguishing treatment at all, one grey over Observed and Unknown alike, and 22 (the Unknown-disclosure blocks) carrying the declared Unknown token under an undeclared, unlegended class - while the checker carrying the identifier uses a denominator of 4 pages against a 1,052-member population on POC-REQ-060's three surfaces (1,087 over the four pages this packet sweeps) [Observed: three tuple-count methods agreeing; a full CSS-rule parse; a four-page sweep with a stated predicate]
- G2 Doctrine: aligned - VIS-2, VIS-7, POC-REQ-060 (Case, Observable, Falsifier, Scenario), POC-REQ-061, PWB-REQ-007, PWB-REQ-016, RFC2-25, RFC7-34, CC-VIZ-1, CC-VIZ-3; RFC 0009 applies_to is [orrery, machine-clients] and is used as a voluntary standard, not a binding clause
- G3 Topology: apps/three-surface-poc only; no boundary crossed, no core change, no governed artifact, no spec text; every slice rides the 2026-09-05 implementation-authorization continuation and crosses none of the six escalation triggers
- G4 Design: the declared table generates CSS attribute selectors (hundreds of bytes, not 16,366) in both tuple and scope-inherited forms; a population sweep with a reported denominator; two existing Unknowns rendered in the opening band; a fixture forcing the item-level Unknown and a third tier value; tier/freshness/challenge encoding tables generating the glossary, with the freshness closure asserted over served output so the renderer's second `unstated` mint fails loudly; a render-disclosure family (no vocabulary gains a member) with a token at a measured distance over a named population
- G5 Spec: no delta on any slice - POC-REQ-060 already states the invariant, the denominator and the falsifier, and PWB-REQ-007's Case already asks for the fixtures; ten WHEN/THEN scenarios for the beads' acceptance contract; out of scope: any spec or contract amendment, a reserved-state registry, catalog routes, machine-payload fields, freshness values (M2's subject)
- G6 Bar: retained before/after measurement on both host forms, denominators on every sweep, rule-6 mutants per guard branch, parity per tuple not per id, accessibility re-run, independent review with the raw retained
Acts: none on any slice (the 2026-09-05 continuation); a spec amendment: none found and none sought
Open questions: Q1-Q7 above; would queue as P-70 (P-68 is lane B, P-69 is M2, each on its own branch)
Sign-off: pending - the owner's
Recommended handoff: Q1 "a non-conformance", Q3 "inheritance", Q4 "yes" and Q6 "a --proposed token" -> run slices 1, 2 and 4 now under syzygy-dov.3, in parallel with P-68 and M2, slice 3 next; hold slices 5-6 until M2 slice 1 has landed so the generated glossary carries its markers; open no specification package at all (this line first named Q1 and Q3 only and "slices 1-4 now"; brought level with the Recommended handoff section after review 5, K2)
```

## Recommended handoff

**If Q1, Q3, Q4 and Q6 are answered as recommended:** file no new bead.
(Q6 is on the list because slice 2 as sequenced pulls one rule of slice 6's
`--proposed` token forward; if Q6 is answered otherwise, run slice 2 with
the dated exception named in its own section instead, and it lands red until
slice 6 — review 4, finding J6.) Run
slices 1, 2 and 4 under `syzygy-dov.3` immediately — they are self-contained,
they touch no governed artifact and none of M2's files, and slice 2 alone
turns POC-REQ-060's own falsifier from invisible into failing. Slice 2's own
negative sweep needs `.proposal-label`'s one rule moved to slice 6's
`--proposed` token pulled forward with it (slice 2, "one known live
positive"), or it lands red. Run slice 3 next, with the opening-band design
and the position oracle.

**If Q2 is answered as recommended:** slice 5's tier table has six rows and
an absence treatment, and the closure assertion against the hard-coded six is
written before the table is. If the owner prefers arm (a), slice 5 is
unchanged but the renderer drops `unstated` from the tier field and renders
the bare label, which is a small change to `claimTuple` and a change to what
11 tuples say — measurable, and worth re-running the parity sweep over.

**If Q5 and Q6 are answered as recommended:** slices 5 and 6 wait for M2's
slice 1 and then generate the glossary from the tables with M2's markers as a
per-row field. Record in `syzygy-dov.2`'s notes that its copy oracle becomes
an oracle over generated output, so whoever implements M3 does not delete a
tested invariant.

**If Q7 is answered as recommended:** nothing in M3 opens a specification
package, lane B keeps the floor until P-68 rules, and
`syzygy-dov.17`'s notes gain one line: the scoped-attribute implementation
must carry the scope-inherited form of the epistemic encoding selector, or
57% of the tuples lose their declared treatment silently on the day the hoist
lands.

**If Q1 is answered the other way** — that POC-REQ-060's "epistemic encoding"
reaches only the declared badge spans, so the page is already conformant —
then slices 1 and 2 are withdrawn, the 735 body encodings — 713 with no
treatment, 22 styled ad hoc from the declared Unknown token — become a
recorded, accepted gap rather than a defect, and the four-page checker
stands. That is
a coherent outcome and should be written down as one, not left as silence; it
would also mean the requirement's scenario "Unknown looks the same
everywhere" is satisfied by a page on which Observed and Unknown look the
same as each other, which is worth the owner seeing before answering.
