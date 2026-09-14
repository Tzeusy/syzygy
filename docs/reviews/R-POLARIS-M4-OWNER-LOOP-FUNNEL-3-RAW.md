# R-POLARIS-M4-OWNER-LOOP-FUNNEL — review 3 (raw, retained verbatim)

Independent fresh-context review. Read-only throughout: no file in any repo
or worktree was edited, no state-changing git command was run, no `bd`
write, no daemon, no network, no read of the observed repository's
checkout. The single file written is this one.

## What was reviewed

Worktree `…/scratchpad/m4wt`, branch `agent/syzygy-dov.4`, HEAD
`f911a45c751e87d442d38baa81120b6f71301656` ("docs: M4 funnel review 2
retained, G1–G11 repaired [syzygy-dov.4]"), working tree clean
(`git status --porcelain` empty), so all three artifacts are tracked at
that commit.

Byte sizes and digests computed this session with `wc -c` and
`sha256sum`, never transcribed:

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` | 139094 | `09116fcfc1fb21127670813196b297705b2a7862edb18dd4fb713391899f0750` |
| `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json` | 38933 | `d7a7aaffd5a1e5a8fd5dc8a3997c9f56e72b4b762bdec42f108886acb7d5b7ed` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 32781 | `38ee2b8e01a2fd483caad90e0a07867a779edf7db1cef5deb7e09065a1eb8f9c` |

Retained captures re-hashed this session; all eight rows of the packet's
own provenance table match, byte count and digest, including the lane A
tailnet capture at 1,484,487 bytes /
`e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111`
[Observed].

Sibling packets read read-only for re-derivation: M2 at
`…/scratchpad/m2wt` HEAD `f2f37ddfe9290fd3c067e445d2dfe9b537405a54`; M3 at
`…/scratchpad/m3wt` HEAD `9cb4d65a830588c2caf078510e7f495ce20e88b4`.

Invariant checks run this session: `python3 scripts/check_governance.py`
in the worktree ends **32 OK, 20 WARN, 0 FAIL (52 checks)** [Observed].
Every code-span path in the packet that contains a `/` resolves, except
glob patterns (`.syzygy/**`, `openspec/**`), HTTP routes (`/api/poc`,
`/api/poc/polaris`, `/polaris/source`, one anchor URL) and three git
branch refs — none of which is a filesystem path [Observed: an existence
sweep over every backticked span]. No wrapped code span: every non-fence
line has an even backtick count [Observed].

## Findings

### H1 — blocking — a fourth Unknown encoding on Orrery sits outside both censused marker families, inside POC-REQ-060's own population

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:91` (Q1), and the same
figures at `:154-158` (Gate 1 measurement 3), `:171-180` (Success 1),
`:677` (slice 1 Tests), `:944-953` (Gate 5), `:1272-1286` (Gate 6
numbers), `:1416` (G3 disposition), and
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:224` and
`:107-145`.

**Defect.** The census that Q1 offers as POC-REQ-060's per-surface
denominator enumerates occurrences of exactly two literals —
`data-unknown-disclosure` and `epistemic-unknown` — and concludes there
are "at least three encodings today", with Q1 asserting that "Trajectory
and Orrery render **every** Unknown through the bare `epistemic-unknown`
class, with no disclosure wrapper, no closed reason and no route at all".
POC-REQ-060's scope of quantification is "every epistemic encoding across
the three surfaces". A third marker class exists and is in neither
family:

`apps/three-surface-poc/src/exact-tables.ts:10` emits
`<span class="provenance-none">No positive provenance; this relationship
remains Unknown.</span>` whenever an entity or relationship has empty
provenance. On the retained Orrery capture that span occurs **9** times;
on Polaris **0**; on Trajectory **0**; on home **9** rendered spans plus
one stylesheet rule [Observed, this session, over the four retained
captures; predicate: literal occurrences of the string `provenance-none`,
denominator the whole served page, each occurrence then assigned to its
enclosing tag — the same partition method G3 used].

The nine Orrery spans are, by the id of their enclosing `<tr>`:
`work:whatsapp-single-event-normalization`, `evidence:focused-pytest`,
`runtime:live-satisfaction`, `region:unmapped-code`,
`relationship:intent-to-work`, `relationship:work-to-code`,
`relationship:code-to-evidence`, `relationship:code-to-runtime`,
`relationship:capability-to-unmapped-region` [Observed]. **Those are
exactly the nine objects Q1's own question is about** — the four entity
Unknowns and the five relationship Unknowns. The packet's census reached
them on Polaris (as bare prose inside a disclosure) and on Orrery (as an
`epistemic-unknown` label span) and missed a third rendering of the same
nine on Orrery entirely.

Two further facts make this POC-REQ-060's falsifier and not a naming
quibble:

1. **`provenance-none` is not in the declared token table.**
   `apps/three-surface-poc/src/design-tokens.ts:25` declares
   `className: 'epistemic-unknown'`; `provenance-none` appears nowhere in
   that file. Its only style rule is
   `apps/three-surface-poc/src/routes.ts:73` —
   `.provenance-none { color: var(--unknown); font-size: .8rem; }` —
   inside `HOME_STYLE`, a per-route style block. A span carrying the
   Unknown colour token under a class the declared table does not carry
   is POC-REQ-060's second falsifier limb verbatim: "a surface styling
   epistemic state ad hoc" [Observed; the requirement text quoted from
   `openspec/changes/three-surface-poc-experience/specs/three-surface-poc-experience/spec.md:945-946`].
2. **The same class renders differently on two surfaces.** `HOME_STYLE`
   reaches the home route only; `apps/three-surface-poc/src/orrery.ts:4`
   imports `exactTablesSection` and calls it at lines 125 and 151 without
   it. On the retained captures, home carries the `.provenance-none` rule
   inside `<style>` and Orrery carries **zero** style occurrences against
   its nine rendered spans [Observed]. So one epistemic assertion renders
   with the declared Unknown colour on one served page and with no
   declared encoding at all on another — POC-REQ-060's first falsifier
   limb, "one surface encoding Unknown (or Observed) differently from the
   declared table".

**Why it is blocking rather than an addendum.** The per-surface
denominators (Polaris 22, Trajectory 0/299, Orrery 0/9) are published in
five places as the measurement POC-REQ-060's sweep is to be run against,
and Gate 6 item 1 lists them as the numbers a slice-1 implementation must
record before and after. Slice 1's designed remedy — "require Trajectory
and Orrery to emit the same `data-unknown-disclosure`/`data-unknown-reason`
marker pair" (`:677-686`) — touches none of the nine `provenance-none`
spans, so a slice built and accepted to this packet's figures would land,
pass its sweep on every published denominator, and leave the breach
standing and undetected. An owner ruling Q1 "a non-conformance, repaired
by slice 1" would be authorizing a repair whose acceptance evidence is
blind to a quarter of the population it is about. This is the third
consecutive review at which the denominator of this one census was wrong
in a different way — F5 found it was one surface instead of three, G3
found a stylesheet rule and a legend item inside it, and this pass finds
that neither family is the requirement's population.

Note in passing, not itself a finding against the packet: the literal
says "this **relationship** remains Unknown" on all nine rows, four of
which are entities, not relationships.

**Repair.** (a) Add `provenance-none` to the cross-surface census as a
fourth family, with its own per-surface denominator (Polaris 0,
Trajectory 0, Orrery 9 rendered, home 9 rendered plus 1 rule) and the
Orrery-versus-home style asymmetry stated. (b) Replace "every Unknown" at
`:91` and `:677` with the predicate actually run — "every occurrence of
the literal `epistemic-unknown`" — or run a sweep whose denominator is
the rendered Unknown population per surface rather than one class
literal. (c) State in Q1's recommendation and in slice 1's Tests that the
shared marker the sweep is re-specified over must cover the
`provenance-none` rendering, and add the corresponding rule-6 mutant. (d)
Record in Gate 3 that `exact-tables.ts` and `routes.ts` lines 34–96 —
both already named as slice 5's files — are where this fourth encoding
lives, so slice 5 does not rewrite them without closing it.

### H2 — non-blocking — "largest of the three" is the cross-family comparison the next sentence forbids

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:91`, and the same claim in
the G3 disposition at `:1416` and in the evidence record's
`cross_surface_unknown_disclosure_populations.largest_of_three_recheck`.

**Defect.** Q1 states "the third encoding is still the largest of the
three: 299 + 9 = **308** rendered claim encodings across the two
surfaces, against Polaris's 13 routed disclosures and 9 bare-prose ones",
and then, one sentence later, "The two marker families are still not
directly comparable … so each is reported against its own denominator,
never combined into one total." Ranking the three encodings by size is a
comparison across the two families; declining to add them into one total
does not make the ranking sound. The two terms also count different
objects: 308 counts `epistemic-unknown` spans (on Trajectory, per work
item and per parity field, e.g. `work-item-verification`), while 13 and 9
count disclosure elements on Polaris. G11 removed "two orders of
magnitude" for this exact reason and the superlative it was attached to
survived.

Not blocking: the remedy Q1 recommends turns on the zero-denominator
fact, not on which encoding is largest, so no recommended answer moves.

**Repair.** Drop the superlative, or restate it as what was actually
measured — "each surface's Unknowns are encoded by a marker the other
two do not share" — and keep the three per-family denominators
unranked.

### H3 — non-blocking — G7's disposition says the head mention was removed from the Collision section; it is still there

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1420` (G7 disposition:
"Head mentions removed from the Collision section and from Q7 … One head
mention remains, in the review-1 disposition table") against `:1179`,
which is in the Collision section and reads "…the M3 worktree has moved
twice since, though `b34fca7` remains an ancestor…".

**Defect.** The short head occurs three times in the packet — `:1179`
(Collision section, live prose), `:1352` (review-1 disposition table) and
`:1420` (review-2 disposition table) — not once. The evidence record
repeats the same false disposition sentence ("head mentions removed from
the Collision section") while its own
`M3_slice_3_and_M4_slice_3_duplicate` field still carries the head. The
prompt's own criterion for this pass is at most one dated head mention;
the count is three in the packet plus two in the record.

The *substance* is sound and was re-derived: `b34fca7` is an ancestor of
the m3wt head `9cb4d65` (`git merge-base --is-ancestor` exits 0), three
commits back, and M3's Gate 3 table, slice-3 design and slice-3 oracle
are unchanged across the move [Observed, read-only in m2wt/m3wt]. So the
defect is the disposition's own accuracy, not the finding it records — a
disposition claiming a repair the bytes do not show is the class of
defect this packet exists to prevent.

**Repair.** Either remove the head from `:1179` (the sentence works
without it: "the M3 worktree has moved twice since, and M3's Gate 3
table, slice-3 design and slice-3 oracle are unchanged across the move"),
or restate G7's disposition to the true count and say which mentions are
historical records that may not be rewritten. Correct the same sentence
in the evidence record.

### H4 — non-blocking — two blockquotes introduced as "quoted verbatim" silently elide intermediate bullets

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:934-953` (POC-REQ-060) and
`:963-976` (PWB-REQ-020).

**Defect.** Review 1's F18 found the RFC2-24 quote eliding a continuation
without an ellipsis, and repaired it there. The same defect stands at two
of the three spec quotations this packet's conformance arguments rest on:

- POC-REQ-060, introduced "quoted verbatim from … lines 927–945": the
  quote runs Case → Observable → Falsifier, dropping **Oracle** (lines
  941–942) and **Oracle independence** (943–944) with no ellipsis
  [Observed: source lines 927–946 read this session].
- PWB-REQ-020, introduced "quoted verbatim from … lines 902–926": the
  quote runs Case (partial) → Observable → Falsifier, dropping **Oracle**
  (916–917), **Oracle independence** (918–919) and **Mutation proof**
  (920–923) with no ellipsis.

The PWB-REQ-020 elision is not cosmetic. The dropped Mutation proof
bullet reads, at
`openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md:920-923`:
"for each fact, authority-state, judgment-state and disclosure marker
class, independently inject a missing, duplicated, changed, collapsed and
wrong-evaluation marker and confirm the comparator fails before
restoration; report both channel denominators for every run." Slice 2
adds a new disclosure marker class and therefore inherits that
obligation; Gate 6 item 3 lists rule-6 mutants and item 4 lists both
denominators, but the packet never states that this is the requirement's
own mutation clause rather than the project's general practice. A reader
checking slice 2's conformance against the quoted text cannot see the
obligation at all. Verification rule 8 is anchoring *and* quoting the
clause; an unmarked elision is nearby prose standing in for the clause.

Also in this finding: the cited range 927–945 for POC-REQ-060 stops one
line short — the Falsifier's second limb, "or a surface styling epistemic
state ad hoc", which the packet quotes and which H1 turns on, is line
946. And PWB-REQ-004 is cited at "lines 490–498" (`:987`) where line 490
is blank and the clause runs 491–498.

**Repair.** Mark both elisions with an ellipsis and name what was elided,
as F18's repair did; extend the POC-REQ-060 range to 946; correct the
PWB-REQ-004 range to 491–498; and state explicitly under slice 2 that
PWB-REQ-020's Mutation proof bullet is the source of its per-class
injection obligation.

### H5 — editorial — F21's over-78-column count is now six, not five

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1370`. Swept this session
over the current bytes [predicate: lines outside fenced blocks and
outside table rows whose length exceeds 78 characters; denominator 1,516
lines]: **6** — line 1 (the H1, 126 chars, disclosed) and five path-span
lines at 10, 486, 561, 935 and 964. F21's disposition says "five lines"
and "the four path-span lines". The packet grew by ~55 KB across two
repair passes and the figure was not re-derived. This is the recorded
lesson that an absence or count figure over a population the current pass
is still editing has to be re-derived, never read.

**Repair.** Re-derive the figure and state the predicate (outside fences,
outside table rows) with its denominator.

### H6 — editorial — two offset conventions for the same population, unstated

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:280-301` (the disclosure
table's "Offset" column begins 378,599 and ends 1,462,590) against `:91`
and `:1416` ("offsets 378,631 through 1,462,622"). Both are correct: the
table gives the enclosing element's `<` position and Q1 gives the
`data-unknown-disclosure` attribute position, 32 characters later
[Observed: both re-derived this session]. Neither says so, and review 1's
N3 was about exactly this — a citation mixing two conventions without
stating one.

**Repair.** One sentence naming the two conventions, or one convention
throughout.

### H7 — editorial — "merge-conflict site" overstates the mechanism the packet itself describes

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1153` and `:97` call the
declared-copy array in `apps/three-surface-poc/src/polaris-copy.ts` "the
one genuine merge-conflict site of the five". M2 slice 1's cited region
is lines 45–49 and M4 slice 3 adds rows beside `label.deferred` /
`label.no-route` at 192–193 [Observed: both read this session] — 145
lines apart, so the two edits do not textually conflict. The real
coupling is the one the packet states in the same breath and which does
hold: both changes must reconcile `UNREACHED_IN_FIXTURES` at
`apps/three-surface-poc/src/polaris-copy.test.ts:296`, and M2's Gate 3
slice-1 row names the copy-oracle test, so the sequencing conclusion
("cannot land independently") stands.

**Repair.** Call it the shared copy-oracle reconciliation site, not a
merge-conflict site.

### H8 — editorial — Q6's question cell keeps the framing G4 superseded

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:96` still opens "Disclosed
for confirmation: deletion has a cost the move does not name." The
preamble repaired under G4 (`:68-82`) supersedes "put to the owner for
confirmation and disclosure rather than as a free choice" and establishes
that both Q6 arms are lawful and the question is a genuine engineering
choice. "Disclosed for confirmation" is readable either way — as a
disclosure offered for the owner to confirm, or as the superseded framing
of the question's character — and a fresh reader meeting the row before
the preamble gets the second.

**Repair.** "Both arms are lawful; deletion has a cost the move does not
name, stated here so the choice is made knowing it."

### H9 — editorial — three absence and all-claims carry no predicate, denominator or label

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:567` ("**Conflict check.**
None found. … None turns anything green, none folds an Unknown into a
total, none establishes a claim"), `:585` ("Boundaries crossed: none
new.") and `:591` ("Not touched by any slice: the body-read authority
gate, …"). Each quantifies over the eight slices and each is unlabeled.
The population is small and enumerated one screen above, so the claims
are defensible — but the packet labels substantive claims everywhere else
and a reader cannot tell whether these were checked slice by slice or
asserted.

**Repair.** One `[Inferred]` label each, or "checked against all eight
slice rows above".

## G1–G11 verification

Every load-bearing finding re-derived independently this session from
source and the retained captures, not read from the disposition table.

| # | Verdict | Evidence |
|---|---|---|
| G1 five-file M2 set | **REPAIRED** | Re-derived by hand from both Gate 3 "Lives in" columns with both denominators. M2's names 9 distinct files (`polaris-copy.ts`, `polaris.ts`, `git-observation.ts`, `main.ts`, `model.ts`, `routes.ts`, `polaris-reading.ts`, `project-shape-model.ts`, the adapter-registry JSON); M4's names 13 (`model.ts`, `polaris.ts`, `orrery.ts`, `trajectory.ts`, `polaris-parity-sweep.test.ts`, `project-shape-model.ts`, `polaris-copy.ts`, `routes.ts`, `exact-tables.ts`, `routes.test.ts`, `capture-test-artifact-main.ts`, `scripts/check_governance.py`, `materialization.ts`); intersection **5**, exactly as published. `polaris-copy.ts` no longer appears in the "M4 does not touch" list at `:1143`; the copy-array coupling is stated at `:97` and `:1150-1156`. The register row carries five |
| G2 three-way band | **REPAIRED** | M2's Gate 3 slice-2 row names "`polaris.ts` (the opening band)" and its slice-2 design body opens "Rendered in the opening band, before the first catalog section:" [Observed, m2wt, read-only]. M3's slice 3 is titled "One real Unknown in the first reading" and its oracle is "precedes the first `data-polaris-group=\"catalog\"` occurrence" [Observed, m3wt]. The revised three-way reconciliation appears at Q7, in the Collision section, in the funnel summary, in the handoff and in the P-71 row, each naming it as a changed recommended answer |
| G3 raw/rendered split | **REPAIRED** | Re-measured independently on all five retained captures. Raw `epistemic-unknown`: Polaris tailnet **2** (offsets 2,809 and 1,481,343), Polaris direct **2** (2,809 and 1,475,493), Trajectory **301**, Orrery **11**, home **18**. Exactly one occurrence per page inside `<style>`; the first non-style occurrence on every page is the legend key item `<span class="epistemic epistemic-unknown">? Unknown</span>`. Rendered = raw − 2 on all four: 0 / 299 / 9 / 16. An element-inner sweep of all 22 Polaris disclosures (attribute offsets 378,631–1,462,622) finds **0**. The record's `null` is replaced by the measured 2 with the full partition. Every figure the packet publishes is correct **for the two literals it counts** — see H1 for the population it does not reach |
| G4 Q6 preamble | **REPAIRED** | The superseded sentence is quoted and dated in place at `:68-72`; Q6 is restated as a genuine engineering choice put to the owner because no requirement reaches the field, with both arms named lawful; the minting language appears only under Q2. The recommended answer is unchanged. Residue at the row's own opening — see H8 (editorial) |
| G5 PWB act citation | **REPAIRED** | Re-read at source. `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` lines 1–17 are the comment block and carry none of the quoted text; the section "What the recorder reads this as" is line 44, "and nothing wider" closes line 48, "**Implementation planning and implementation**" opens line 50, and the tasks-range clause "tasks §2 through §5 of its `tasks.md`" is line 51. The packet now cites the body section at lines 44–52, quotes in source order, and restores the tasks range. Lines 70–72 are quoted verbatim and correctly |
| G6 P-71 collision clause | **REPAIRED** | Re-derived at source: `UNKNOWN_REASON_ROUTES` spans lines 89–102 of `packages/three-surface-poc-core/src/project-shape-model.ts`; M2 slice 5 cites 162–193 (freshness/tier constants at 167–169, the `claim`/`observedClaim`/`unknownClaim` constructors at 171–195); M4 slice 2 cites 115–118 (`ResolutionRoute`) and 150–154 (`routesFor`). Neither edits 89–102. The register row now names the shared file and the shared construction site — line 176, `resolutionRoutes: routesFor(epistemic)` — verbatim and correctly, and the rule-together conclusion is unchanged |
| G7 M3 head | **PARTIAL** | The finding's substance is confirmed and the routing is repaired (M3 is cited by register row P-70 and by the two files at `:97` and `:1176`). But the head survives in the Collision section at `:1179`, and the disposition's own sentence says it was removed from there. See H3 |
| G8 VIS-5 adapters | **REPAIRED** | The "two typed, explicitly authorized adapters" sentence is quoted, dated and superseded at `:475-482`. VIS-5 (`.syzygy/governance/doctrine/vision.md`:141) names no number of adapters; the "two" in its own heading is two write namespaces, as the repaired text says. The paragraph now states that the effect must run through a typed adapter governed by that authority's contract, that the materialize mechanism is one such adapter in code, and that whether any act authorizes it is Q5. The registry entry's five `typedAuthority` values and its `candidate-amendment-no-effect-until-owner-act` lifecycle status are both stated |
| G9 slice attributions | **REPAIRED** | Re-derived from both Gate 3 tables. M3 names `polaris.ts` in slices **1, 3, 5 and 6** and `polaris-copy.ts` in slices **3 and 5**; M2's `polaris.ts` belongs to slices **1, 2 and 6**. Both corrections appear at Q7 and in the Collision section with M2 slice 2's region named |
| G10 `model.` arithmetic | **REPAIRED** | Counted per line at HEAD: 35:1, 78:1, 87:1, **89:4**, 92:2, 127:1, 133:1, 171:1, 172:1 — **13** over nine lines. `renderPocPage` spans 77–96, so **five** lines lie outside it. The load-bearing claim re-derived and holding: `renderPocPage` reads exactly five model fields, `model.surfaces` feeds line 78's `surfacePanel` map and nothing else does, and `exactTablesSection(model)` at line 82 keeps the exact tables alive without it |
| G11 "two orders of magnitude" | **REPAIRED** | S1 at `:1044-1048` now reads "runs 22, 0 and 0" with the superseded clause quoted and dated. The superlative it was attached to survives one cell away — see H2 |

## F1–F22 regression spot-check

No regression found. Independently re-derived: F1 (RFC2-24's twelve
route strings extracted and compared key by key against
`UNKNOWN_REASON_ROUTES` — **5 identical**: `stale-beyond-currency-bound`,
`unconsented-source-or-provider`, `excluded-content`,
`contradicted-pending-adjudication`, `reference-unresolvable`; **7
differ**, each by a citation or connective, exactly as the packet
enumerates); F2 (`routesFor` at 150–154 with the two-branch guard at 151;
`EpistemicState`'s `basis: 'deferred'` third arm at
`packages/cap1-core/src/epistemic.ts:62-66`; `label.deferred` and
`label.no-route` at `polaris-copy.ts:192-193` and in
`UNREACHED_IN_FIXTURES` at `polaris-copy.test.ts:297,299`; 0 of 1,137
empty-array claims Unknown and 12 of 12 non-empty Unknown, identical on
both machine captures); F4 (`materialize-action.ts:33`,
`materialization.ts:12` and the `execFileSync('bd', ['-C', repoRoot, …])`
at 186–208); F7/N1 (747–748); F8/N2 (comment 26–29 / const 30–33;
comment 35–41 / const 42); F9/N3 (brace ranges 562–581, 582–590, 591–599,
600–608, 609–617); F10/N4 (`surfaces` closes at 750, file ends at 752);
F11/N5 (five fields); F13/N7 (the fifth capture: 6 hrefs, 1 fragment, 5
non-fragment including the anchor deep link); F14/N8
(`walkthroughJudgment.evaluation.outcome`, four values as stated); F15/N9
(713 `data-claim-id="` on the lane A tailnet capture, 699 pre-lane-A);
F20/N14 (Orrery 37,048 bytes). F21 has drifted — see H5.

Gate 1's other censuses re-derived and correct: home 40 hrefs (36
fragments + 4 nav), Trajectory 304 (300 + 4), Orrery 23 (19 + 4), Polaris
1,089 (699 + 386 source routes + 4 nav); Trajectory's materialize panel
at character 242,386 of 244,506, 2,120 characters to the end; Polaris 0
forms, 1 `<button type="button">`, 7 `<h2>`, 39 `<h3>`, 359 `<details>`,
1 `data-polaris-gaps`, 1 `data-polaris-gap`; "Unknown, by reason" the 6th
`<h3>` of the 7th `<h2>` at 99.5%; "One capability in depth" spanning
811,016–852,703 = 41,687 characters = 2.8%. Page-size arithmetic exact:
1,484,487 − 1,400,000 = 84,487; 1,478,637 − 1,400,000 = 78,637;
2,097,152 − 1,484,487 = 612,665; 2,097,152 − 1,478,637 = 618,515. The
1,149 decomposition sums: 439 + 415 + 278 + 6 + 9 + 1 + 1 = 1,149.
F19/N13 could not be checked: its source is in the observed repository,
which this review may not read [Unknown].

Every doctrine and RFC anchor resolves at the line cited: vision.md 82
(VIS-1), 96 (VIS-2), 122 (VIS-4), 141 (VIS-5), 61–64 (the unnumbered
escape-property paragraph), 234–236 (the success sentence); RFC2-23 at
line 70 and RFC2-24 at line 92 of `rendering-vocabularies.md`, with the
"fact of the render" sentence in the immediately following paragraph
(line 98 onward) exactly as N12's repair says; RFC2-25 at 153; RFC2-9 at
187 and RFC2-10 at 209 of `snapshot-and-evaluation-core.md`. Both spec
requirement counts hold: 24 POC and 17 PWB `### Requirement` headings; 0
whole-word `home` in the POC spec and 6 in the PWB spec; 0 hits for the
backticked `surfaces` or for `model.surfaces` in either. Every
requirement the packet names by identifier exists and its paraphrase
matches the requirement's own text, including PWB-REQ-010, 011, 016 and
POC-REQ-020, 061, which the packet names without quoting.

## Q1–Q7

| Q | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | **No — understated.** The 22/13/9 split and the three per-surface figures are exact for the two literals counted, but the population offered as POC-REQ-060's is not the requirement's (H1) | Yes — a conformance ruling only the owner can make, and both arms are written out, including the consequence of the second at `:1509-1516` | Yes on the arm; the remedy's scope is short by the fourth encoding (H1) | Yes, clause by clause, including the marker-coverage caveat — and the register inherits the same gap |
| Q2 | Yes. Both return-`[]` branches, the third `EpistemicState` arm and the two declared copy rows re-derived at source | Yes — reframed from contract-determined to a real choice, with the mint-and-retire arm named as available | Yes. The narrowing to "Unknown carrying `reasons`" follows from the deferred arm being modelled | Yes |
| Q3 | Yes. The empty write surface and the act's own prohibition are quoted accurately; the two reasons a gate is needed are distinct and both stand | Yes — three arms, (b) correctly identified as needing no act | Yes, and the handoff's "build the pure drafter anyway" is consistent with (b) | Yes |
| Q4 | Yes. One gap reason over 12 claims, `data-polaris-gap` occurring once, the `foremost` ordering at `polaris.ts:933-948` — all re-derived | Yes — both arms lawful, stated as such | Yes, with the filter arm's cost named | Yes |
| Q5 | Yes. The unconditional literals at lines 588 and 597, the conditional at 570, the seam comments, and both readings' quotations verified at source | Yes — and the authorization limb is the packet's most honest passage: two readings quoted, the recommendation labeled [Inferred], the counter-argument left standing rather than resolved | Yes. Reading A's citation is now in the right section and in source order | Yes |
| Q6 | Yes. 4 declared against 415 items and 713 tuples; the `model.` arithmetic and the five fields re-derived | Yes — both arms lawful after the G4 repair | Yes; deletion's cost is stated without denying deletion is available | Yes |
| Q7 | Yes. Both Gate 3 intersections re-derived with both denominators; the three-way band confirmed against M2's and M3's own bytes | Yes — sequencing, the collision set and the slices 4–5 authorization arm, each named as the owner's call | Yes, and the changed answer is stated plainly in five places | Yes. The register's Q7 carries the five-file correction, the three-way reconciliation, the "changed after review 2, G2" marker and the corrected G6 collision sentence |

**Register note counts.** Counted this session by the register's own
stated method — split on `## ` headings, then match at line start a table
row whose first cell is `P-` followed by anything but a cell break:
acceptance-act section **5** (P-1…P-5), reading aid **0**, open section
**22** (P-10, P-12, P-15, P-17, P-18, P-19, P-20, P-21, P-23, P-25,
**P-25(c)**, P-27, P-29, P-30, P-32, P-43, P-49, P-50, P-51, P-52, P-53,
P-71). **22 open, 5 acceptance, 27 in all — the note's figures are
right**, and the sub-lettered row is included, as the register's own
corrected predicate requires [Observed].

**Sibling-packet references.** M2 is cited as `syzygy-dov.2` / register
row P-69 / PR #36 and by file; M3 as `syzygy-dov.3` / register row P-70
and by the two files; lane B as `syzygy-dov.17` / PR #35 / register row
P-68. Routing is by row and file throughout. The head-mention count fails
the "at most one" bar — see H3.

**Owner trade-offs.** None found smoothed into consensus. Q5's two
readings, Q2's mint-and-retire arm, Q3's three arms, Q4's filter arm,
Q6's deletion arm and Q1's "accepted shape" arm are each written out with
their consequence, and the two changed recommended answers are disclosed
in the packet, in the register note, in the register row, in the funnel
summary and in the handoff. No lawful arm is called unlawful anywhere in
the current bytes.

## Counts

blocking 1, non-blocking 3, editorial 5 — nine findings, H1–H9.

Verdict: REVISE
