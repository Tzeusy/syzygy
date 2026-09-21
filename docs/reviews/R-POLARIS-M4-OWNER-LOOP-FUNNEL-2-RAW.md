# R-POLARIS-M4-OWNER-LOOP-FUNNEL-2-RAW

Independent fresh-context review, round 2, of the repaired packet.
Read-only session: no repository file was edited, no git state changed, no
daemon was run, no network was reached, and the observed repository's
checkout was never read. This file is the only file written.

## Header — what was reviewed, at which bytes

Worktree: `scratchpad/m4wt`, branch `agent/syzygy-dov.4`.
Commit under review: `6218726df459971e29af680f04f8f0cdf3e01e93`
(`docs: M4 funnel review 1 retained, F1–F22 repaired, P-71 owner questions`,
2026-09-14T09:23:55+08:00). `git status --porcelain` empty.

Reviewed artifacts — `wc -c` and `sha256sum`, computed this session, never
transcribed:

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` | 116002 | `95e72b30a7d496e963ae6a244dd421bd720d317fae126a3c027b07e0a4ee3d5b` |
| `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json` | 31201 | `54b22be504c58483a9d52bab26e4e89f62766eccc167bbc9eb8a8a10009e8f23` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 29879 | `7ff5bc37abe5f152bb9d02d6b891bcb24e8db47b141804485ada6e8106b87e97` |
| `docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-RAW.md` (review 1, retained) | 47636 | `6983034196c706c213e2a939e0ca7dfe4c3f75f958378403fbd115112c2966ec` |

The packet's own review-1 section cites the retained raw at 47636 bytes and
that sha256; both re-computed here and both match. Its statement that review
1 read the packet at 83557 bytes on commit `61bd43b…` matches review 1's own
header table.

Captures re-digested this session; every one matched the packet's provenance
table at `:28–37`:

| Capture | Bytes | sha256 |
|---|---|---|
| `m1/measure/after/polaris-tailnet.html` | 1484487 | `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` |
| `m1/measure/after/polaris-direct.html` | 1478637 | `2fecdd01e1a2ff577567495796ea7e59ab89f1420be6033e23314d26442ea094` |
| `capture/home.html` | 38706 | `c2fd6d1af7103e871c26dc65b76cc391fe2765a1c7391ac19ddf1656e57b5fca` |
| `capture/trajectory.html` | 244524 | `fd802531b199084e7145932715150f4977335e49ca6aa168d68d5227c9d6ddde` |
| `capture/orrery.html` | 37048 | `e3ae5b7901c599a04b685456e6070430edf72fcd025cd1f6afecf863153582fa` |
| `capture/source-sample-7478.html` | 23083 | `bf5257d626fe0c6e62dbb2a3ae708fac764052dc10e7a73997541c80fc433435` |

Sibling worktrees, read read-only this session:
`scratchpad/m2wt` at `f2f37dd`, clean; `scratchpad/m3wt` at `f35a25f`,
clean — **not** at `b34fca7`, the head the packet names. See G7.

Mechanical gates, run this session from the worktree root:

- `python3 scripts/check_governance.py` → **32 OK, 20 WARN, 0 FAIL (52
  checks)**. Invariant met [Observed].
- Hard wrap: 5 lines exceed 78 columns outside tables, block quotes,
  indented blocks and fences (denominator 1375 lines) — lines 1, 462, 537,
  909, 936. Four are single unbreakable path code spans; one is the H1.
  Unchanged from review 1's finding; see F21 [Observed].
- Code-span paths: 60 path-shaped spans; 46 resolve on disk directly and the
  14 that do not are glob patterns (`openspec/**`, `.syzygy/**`), served
  routes (`/api/poc`, `/api/poc/polaris`, `/polaris/source`, one anchored
  Polaris link), three `agent/syzygy-dov.*` branch names, and five
  `path:line` forms whose file half resolves. None is a broken file
  reference [Observed].
- No manifest argument and no truncated signed digest is quoted; no observed-
  repository path appears inside a code span (CG-1b clean, and
  `check_governance.py` agrees) [Observed].

---

## Findings

### G1 — blocking — the re-derived M2 shared-file set is still one file short, and the Collision section contradicts itself about that file thirty lines apart

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1104–1105` against `:1134–1135`
and `:554`; the same count at `:84` (Q7) and in the P-71 register row
(`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:209`).

**Defect.** The packet states, twice, "**M4 shares four files with M2**", and
the Collision section lists the M2 files "which M4 does not touch" as
"`polaris-copy.ts`, `git-observation.ts`, `main.ts` and `polaris-reading.ts`"
(`:1104–1105`).

M4 touches `apps/three-surface-poc/src/polaris-copy.ts`. Its own Gate 3 row
for slice 3 (`:554`) reads "`apps/three-surface-poc/src/polaris.ts` (a second
rendering of `gapReasonCounts`, reusing `gapId`),
`apps/three-surface-poc/src/polaris-copy.ts` (the band's own copy rows)". And
the Collision section says so itself thirty lines later, at `:1134–1135`:
"M4 slice 1 adds a reason and a route to nine disclosures and M4 slice 3 adds
band copy rows — in the same two files."

M2 touches it too. Its Gate 3 slice 1 row
(`m2wt`, `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md:361`, read this
session) reads "`apps/three-surface-poc/src/polaris-copy.ts` (lines 45–49),
`polaris.ts` line 357, plus the copy-oracle test".

Intersecting the two Gate 3 tables by hand, this session, over M2's nine
named files and M4's twelve: **the shared set is five** — `model.ts`,
`routes.ts`, `polaris.ts`, `project-shape-model.ts` and **`polaris-copy.ts`**.
And the fifth is not an incidental one: M2 slice 1 and M4 slice 3 both add
rows to the same declared-copy array, which is the literal merge-conflict
site, and both are covered by the same copy oracle whose
`UNREACHED_IN_FIXTURES` set each change must reconcile.

This is review 1's F3 in both of its limbs — the under-count and the
self-contradiction inside one packet about which file is shared — surviving
inside the repair that is offered as "re-derived from both sibling packets'
own Gate 3 tables, not asserted" (`:1093–1094`). F3's stated repair also
asked for the set "with its denominator"; no denominator is published in
either place.

**Repair.** Five files, at `:84`, `:1105` and in the register row; remove
`polaris-copy.ts` from the "M4 does not touch" list at `:1104`; state the
denominator (M2's nine Gate 3 files against M4's twelve); and name the
copy-array collision in the sequencing answer, since M2 slice 1 and M4
slice 3 cannot land independently.

---

### G2 — blocking — there is a third opening-band design, in M2 slice 2, and the "one band, one owner, one oracle" recommendation does not see it

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1101–1102` and `:1143–1161`;
the recommendation repeated at `:84`, `:1177–1178`, `:1321` and in the P-71
register row (`PENDING-OWNER-DECISIONS.md:209`).

**Defect.** The packet's headline F3(c) repair is that M3 slice 3 and M4
slice 3 are "two designs for the same band, in the same function of
`polaris.ts`", resolved as "**one band, one owner, one oracle**". I confirm
that pairing: M3's slice 3 at `f35a25f` is titled "One real Unknown in the
first reading", its design opens "The opening band renders, in place and
before the first catalog group…", its Gate 3 row names `polaris.ts` and
`polaris-copy.ts`, and its oracle is the first-rendered-Unknown-precedes-
first-catalog test — all exactly as the packet describes.

But there is a third. M2's Gate 3 row for its slice 2 (`m2wt`,
`POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md:362`) reads, in full for the
app file: "`polaris.ts` (**the opening band**)". M2's slice-2 design body at
`:485` reads "**Rendered in the opening band, before the first catalog
section:**" and then gives the full block — an evaluation-currency
disclosure with its own epistemic tuple. M2's own Q6 answer (`m2wt:50`) makes
it the slice's headline target: "the page's first human-visible instant moves
from 58.0% depth into the opening band". Three further mentions at
`m2wt:338`, `:348` and `:712` treat it as slice 2's band.

The packet names M2 slice 2 in its `polaris.ts` attribution (`:1101`,
"slices 1, 2") and then cites, as the regions, "line 357's
`claimStatesBlock` freshness group and lines 506–510's reading block" —
which are M2's slice 1 and slice **6**. Slice 2's band edit is attributed and
never located, so the collision analysis that exists to catch exactly this
never reaches it. Consequently the packet's "one band" recommendation, the
ordering at `:1174–1183`, the handoff at `:1336–1337` and the register row
all name two designs for a band that three packages are writing.

This is the same class as the F3(c) the repair fixed, reintroduced for the
other sibling, and it reaches the owner's answer to Q7 the same way.

**Repair.** State that M2 slice 2, M3 slice 3 and M4 slice 3 all render into
the opening band of `polaris.ts` and name their three distinct payloads
(currency disclosure, the two existing Unknown claims, the `gapReasonCounts`
projection). Give the one band one owner and one oracle across all three, or
say why a currency disclosure and an Unknown band are separate regions.
Correct the M2 `polaris.ts` region citation to slices 1, 2 and 6.

---

### G3 — blocking — Q1's cross-family reconciliation sentence is false, the figure it rests on is `null` in the evidence record, and the published denominators count a stylesheet rule as a rendered Unknown encoding

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:78` (Q1, both cells), repeated
at `:163–165` (Success 1), `:1196–1197` (Gate 6), `:1312` (funnel summary),
`PENDING-OWNER-DECISIONS.md:113` and `:209`; the record at
`docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json`,
`cross_surface_unknown_disclosure_populations`.

**Defect, two parts.**

(a) Q1 explains why the two marker families may not be pooled: "(`data-
unknown-disclosure` counts disclosure elements on Polaris; `epistemic-unknown`
counts a CSS/data class occurring on every surface, **including Polaris's own
22 disclosures**)".

Measured this session over the retained lane A captures (predicate: literal
occurrences of the string `epistemic-unknown`; denominator: the whole served
page): **2** on `polaris-tailnet.html` and **2** on `polaris-direct.html`.
Neither is a disclosure. Occurrence 1 is at character offset 2,809, inside
the `<style>` block — the rule `.epistemic-unknown { color: var(--unknown);
background: … }`. Occurrence 2 is at 1,481,343, the legend list item
`<span class="epistemic epistemic-unknown">? Unknown</span>`. The 22
`data-unknown-disclosure` elements carry none of them: an element-inner sweep
of all 22 (offsets 378,599 through 1,462,590, re-derived this session and
matching the packet's table row for row, 13 routed / 9 bare / 0 mixed) finds
`epistemic-unknown` in zero of them.

The evidence record the sentence points to carries
`polaris_lane_a_tailnet.epistemic_unknown: null` — the figure the prose
asserts was never measured, and the prose asserts it wrongly.

(b) The same two non-claim occurrences sit inside every published figure. On
each of the four pages, occurrence 1 is the stylesheet rule and occurrence 2
is the same legend item [Observed: offsets 2,808/7,137 on Orrery,
2,808/7,322 on home, 2,812/8,616 on Trajectory]. So the rendered Unknown
populations are Trajectory 299, Orrery **9**, home 16 — not 301, 11 and 18.
On Orrery that is 2 of 11, eighteen per cent of the figure. The packet offers
301 and 11 as the population POC-REQ-060 quantifies over and concludes from
them that the third encoding is "**the largest of the three**"; a denominator
that includes a CSS declaration inside `<style>` is not the population of a
requirement about what a surface renders (verification rule 4).

The finding underneath is sound and I confirm it: Trajectory, Orrery and home
carry **0** `data-unknown-disclosure` elements each, the sweep as originally
specified does have denominator 0 on two of three surfaces, and a third
encoding with no wrapper, reason or route is real. It is the reconciliation
and the arithmetic that are wrong.

**Repair.** Delete or correct the "including Polaris's own 22 disclosures"
clause and record Polaris's measured 2 in the evidence file in place of
`null`. State the predicate for the `epistemic-unknown` figures and subtract
the stylesheet rule and the legend item, or publish both the raw and the
rendered counts with the difference named. Re-check the "largest of the
three" claim against the corrected figures.

---

### G4 — blocking — Q6 is framed as contract-determined with one lawful arm, in Q2's minting language, against the packet's own four-times-stated finding that no requirement governs `model.surfaces`

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:67–69`, against `:92` (Gate 0),
`:580` (Gate 3), `:978–990` (Gate 5) and `:83` (the Q6 row itself).

**Defect.** The question preamble reads: "Q6 is contract-determined on this
packet's own reasoning — it has one lawful arm and one that mints a
vocabulary value no requirement enters — and is put to the owner for
confirmation and disclosure rather than as a free choice."

Q6 asks whether to make `model.surfaces` true by construction or delete it.
Neither arm mints a vocabulary value; that phrase is Q2's, about
`none-modelled`. And "contract-determined" is the opposite of what the packet
establishes everywhere else about this field: Gate 0 (`:92`) "**No
requirement in either spec governs the home route or `model.surfaces`**";
Gate 3 (`:580`) "**No requirement governs this field**"; Gate 5 (`:978–990`)
the same, with three sweeps and their denominators, which I re-ran and
confirm (24 POC requirements, 17 PWB requirements, 0 whole-word `home` in the
POC spec, 6 in the PWB spec, 0 hits for the backticked `surfaces` or
`model.surfaces` in either); and Gate 5 draws the consequence explicitly —
"changing the home page freely is lawful today precisely because nothing
specifies it".

Deletion is therefore a lawful arm, and the Q6 row itself carries it
honestly ("deletion has a cost the move does not name"). The preamble tells
the owner the opposite before they reach the row.

Read against the draft, this is the F2 defect relocated rather than removed:
review 1 found the contract-determined framing on Q2 resting on a false
premise; the repair moved the framing sentence to Q6 and left its wording
intact, where it now rests on no premise at all.

**Repair.** Rewrite `:67–69` to say what Q6 actually is on the packet's own
evidence — an engineering choice the owner is asked to rule *because* no
requirement reaches the field, which is the finding, not a constraint — and
drop the minting clause, which belongs to Q2 alone.

---

### G5 — non-blocking — Reading A's quotation of the 2026-09-02 authorization is in the wrong place in the file and spliced out of source order

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:82` (Q5, Reading A).

The packet writes: "the 2026-09-02 PWB act, whose own **header** says the
recorder reads the owner's 'Authorized' reply as covering 'implementation
planning and implementation of the signed `polaris-project-wide-butlers-
model` change … and nothing wider'".

At `.syzygy/governance/decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`
the header is the comment block at lines 1–17 and contains none of that. The
text is in the body section "## What the recorder reads this as", lines
44–52. And the fragment is re-ordered: "and nothing wider" closes line 48,
while "**Implementation planning and implementation** of the signed
`polaris-project-wide-butlers-model` change" opens line 50. The ellipsis
conceals a reversal, not an elision, and it elides "— tasks §2 through §5 of
its `tasks.md` —", the clause that actually bounds what the grant covers.

The substance survives — the recorder does read the grant as bounded to the
signed PWB change and nothing wider, and the packet does attribute it to the
recorder rather than to the owner — but this is the evidentiary anchor of the
recommended arm on a contested authorization question, and verification rule
8 wants the clause quoted where it is defined and as it reads.

Everything else in Q5's two readings checks out at HEAD: `materialize-
action.ts:33` is `targetRepoRoot: model.project.root`; `materialization.ts:12`
is `MATERIALIZATION_TARGET_BEAD_PREFIX = 'bu'`; `defaultRunCreate` at 186–208
is `execFileSync('bd', ['-C', repoRoot, 'create', …])`; the act's lines 70–72
are quoted verbatim; the mode direction's lines 18–22 are quoted verbatim.

**Repair.** Cite lines 44–52, quote in source order, keep the tasks-range
clause, and say "body section", not "header".

---

### G6 — non-blocking — the P-71 register row ends with a collision the packet's own Collision section denies

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:209`, last sentence:
"Rule P-69, P-70 and P-71 together: **M2's slice 5 and M4's slice 2 both edit
the reason-route table**, and M3 slice 3 and M4 slice 3 are one band."

The reason-route table is `UNKNOWN_REASON_ROUTES` at
`packages/three-surface-poc-core/src/project-shape-model.ts` lines 89–102.
M2's Gate 3 cites slice 5 at lines **162–193** of that file, which this
session's read shows to be the freshness and tier constants (167–169) and the
`claim` / `observedClaim` / `unknownClaim` constructors (171–195). M4's Gate 3
cites slice 2 at `ResolutionRoute` (115–118) and, per the Collision section,
`routesFor` (150–154). Neither edits 89–102.

The packet says as much itself, at `:1111–1113`: "M4 slice 2 widens
`ResolutionRoute` at 115–118 and `routesFor` at 150–154, **adjacent to but
not overlapping** M2's 162–193." Packet and register disagree, clause by
clause, on the one collision sentence the owner-facing row ends with.

The conclusion — rule the three rows together — survives on the shared file
and on the shared construction site at line 176, `resolutionRoutes:
routesFor(epistemic)`, which both changes flow through. Only the stated
reason is wrong.

**Repair.** In the register row: "both edit
`packages/three-surface-poc-core/src/project-shape-model.ts`, in adjacent
regions that meet at the `claim()` constructor" — or whatever the packet
means — and make the two texts agree.

---

### G7 — non-blocking — the M3 head is cited three times, contrary to the sentence citing it, and is already stale

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:84`, `:1127–1130`, `:1271`.

`:1127–1130` reads: "that worktree is under repair as of this review and was
read read-only on 2026-09-14 at committed head `b34fca7`, with a review-3
repair uncommitted; **cite it by register row P-70 and by the two files,
never by head**" — in the same parenthesis that names the head, which is then
named twice more, at `:84` and in the F3 disposition row at `:1271`. M2's
head `f2f37dd` is named twice, at `:84` and `:1097`.

The instruction was right and the practice already cost something:
`scratchpad/m3wt` is now at `f35a25f`
("M3 funnel review 3 retained and H1–H11 repaired"), so `b34fca7` is no
longer that worktree's tip and a reader checking the citation finds a head
that is one commit behind. I verified the substance holds anyway: `b34fca7`
is an ancestor of `f35a25f`, and M3's Gate 3 table and slice 3 design and
oracle are unchanged between them, so G2's and the packet's slice-3 findings
stand on current bytes.

**Repair.** One dated head mention at most, or none; route by register row
P-70 and by file, as the packet's own sentence says.

---

### G8 — non-blocking — Gate 2 calls two owner directions "the two typed, explicitly authorized adapters VIS-5 requires"

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:456–458`.

The sentence: "the two 'typed, explicitly authorized adapters' VIS-5 requires
are the mode direction (for the mechanism's original authorization) and, if
the owner needs one, a continuation naming the effect."

VIS-5, at `.syzygy/governance/doctrine/vision.md` lines 141–152, says that
effects on every other authority "occur only through **typed, explicitly
authorized adapters**, governed by each authority's own contract". An adapter
is the typed interface to the authority; an owner direction is the
authorization *for* one, never one itself. VIS-5 names no number of adapters
either — the "two" in the paragraph's own heading is two write *namespaces*
(`openspec/**` and `.syzygy/**`), a different pair entirely.

The surrounding paragraph is otherwise a good repair of F4 and F16: the
registry entry's `typedAuthority` block does sit inside `entries[0]`, its
`authorityType` is `"version-control"` with a `readAuthority` describing
phase A/B reads only, its five quoted values are exact, and the top-level
`status` does read `candidate-amendment-no-effect-until-owner-act` — all
re-read from the JSON this session.

**Repair.** Say that VIS-5 requires the work-scheduler effect to run through
a typed, explicitly authorized adapter governed by the work scheduler's own
contract, that the materialize mechanism is one such adapter in code, and
that what is contested is whether any act authorizes it — which is Q5.

---

### G9 — non-blocking — the slice attributions the re-derivation is offered on are wrong for both siblings

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:84` and `:1101–1102`.

`:84` says "(M3 slices 3 and 5 both edit `polaris.ts`)". M3's Gate 3 names
`polaris.ts` in slices **1, 3, 5 and 6**. `:1101–1102` attributes M2's
`polaris.ts` to "slices 1, 2" and then cites lines 357 and 506–510 — 357 is
M2's slice 1, 506–510 is M2's slice **6**, and slice 2's region is the
opening band (G2). Neither error changes the two-file and (corrected) five-
file sets, but these parentheticals are the evidence the re-derivation is
offered on, which is where a wrong attribution costs most — and at `:1101` it
is the proximate cause of G2.

**Repair.** M3: slices 1, 3, 5, 6. M2: slices 1, 2, 6, with slice 2's region
named.

---

### G10 — editorial — the `model.` hit arithmetic in Q6 is off in two places

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:83`.

"hits at lines 35, 78, 87, 89 (×2), 92 (×2), 127, 133, 171, 172; the four
outside `renderPocPage` are …". Line 89 of
`apps/three-surface-poc/src/routes.ts` carries **four** `model.` occurrences
(`model.project`, `model.entities`, `model.capabilityId` twice), not two. And
"the four outside" then enumerates five line numbers: 35, 127, 133, 171, 172.

The load-bearing claim is right and re-derived: `renderPocPage` (77–96) reads
exactly `model.surfaces`, `model.project`, `model.entities`,
`model.capabilityId` and `model.evaluation` — five fields — so "the only
input for the three surface panels" is the correct repair of N5.

---

### G11 — editorial — "two orders of magnitude" describes the wrong marker family

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1018` (S1): "not one pooled
denominator across surfaces whose disclosure population today differs by two
orders of magnitude".

The disclosure populations are 22, 0 and 0 — a ratio that is not two orders
of magnitude but undefined. The 301 and 11 that would give roughly that ratio
belong to the `epistemic-unknown` family, which Q1 has just said may not be
compared with the disclosure family. **Repair.** "differs from 22 to 0", or
drop the clause.

---

## F1–F22 verification

Load-bearing findings re-derived independently this session, from source and
the retained captures, not read off the packet.

| # | Review 1's finding | Status | Evidence |
|---|---|---|---|
| F1 | RFC2-24's table ≠ `UNKNOWN_REASON_ROUTES` | **REPAIRED** | Re-derived key by key from `rendering-vocabularies.md` rows 119–130 against `project-shape-model.ts` 89–102, denominator 12: **5 identical, 7 differ**, and the five named at `:506–508` are exactly the five I find (`stale-beyond-currency-bound`, `unconsented-source-or-provider`, `excluded-content`, `contradicted-pending-adjudication`, `reference-unresolvable`), with all seven diffs at `:509–515` exact. Slice 1's table (`:614–624`) now carries `UNKNOWN_REASON_ROUTES`'s own strings ("Produce or capture evidence", "Run or declare the mapping"), the column head says so, and the twelve-value alternative is named as a separate change at `:626–628` |
| F2 | "unreachable by construction" false | **REPAIRED** | `routesFor` at `project-shape-model.ts:151` quoted with both branches at `:79`; `EpistemicState`'s third arm confirmed at `epistemic.ts:62–67` with `basis: 'deferred'` and no `reasons`; `label.deferred` at `polaris-copy.ts:192` and `polaris-copy.test.ts:297` beside `label.no-route` at 193/299 — all four line numbers exact. Q2 re-opened as a genuine choice, slice 2 (`:680–694`) and S3 (`:1026–1029`) both narrowed to "Unknown carrying `reasons`". `routeOf` 466 and `reasonRouteHtml` 473 confirmed |
| F3 | collision analysis wrong in both directions; M3 slice 3 missed | **PARTIAL** | M3 set of two (`polaris.ts`, `polaris-copy.ts`) re-derived and correct; the M3-slice-3 / M4-slice-3 band duplicate re-derived at `f35a25f` and correct, including both titles and both oracles; the "shared with M2 is none" sentence is gone. But the M2 set is still one short (**G1**), M2 slice 2's opening band is still missed (**G2**), the slice attributions are wrong for both siblings (**G9**), and no denominator is published |
| F4 | slice 6 writes into the observed repository | **REPAIRED** | All three code facts re-read at HEAD (`materialize-action.ts:33`, `materialization.ts:12` and 186–208); act lines 70–72 verbatim; mode direction 18–22 verbatim. Q5 now carries both readings, recommends [Inferred], and makes slice 6 conditional; `:193–196`, `:866–873` and Gate 2's VIS-5 paragraph all corrected; Gate 3's slice 6 row (`:582`) retracts "already contemplates" by name. See **G5** on Reading A's citation |
| F5 | sweep has denominator 0 on two of three surfaces | **PARTIAL** | The per-surface restatement landed everywhere review 1 asked — Q1, slice 1's Tests (`:650–667`), Success 1 (`:158–165`), S1 (`:1012–1018`), Gate 6 (`:1194–1200`) — and the 0 / 0 / 0 disclosure counts are exactly right. But the reconciliation sentence is false, the Polaris figure is `null` in the evidence record, and the 301/11/18 denominators include a stylesheet rule and a legend item (**G3**) |
| F6 | Q5 credited with a reading it does not carry | **REPAIRED** | Q7 (`:84`) now states the recorded-finding arm as an explicit owner-facing limb with its [Inferred] label; Gate 3's rows for slices 4 and 5 (`:580–581`) and Gate 5 (`:993–996`) both point to Q7 and say Q5 asks only about slice 6. Q5's own text carries no slices-4/5 limb, correctly |
| F7 | Orrery's derived lists at 747–748 | **REPAIRED** | Confirmed at source: `model.ts:747` `entityIds: entities.map(…)`, `:748` `relationshipIds: relationships.map(…)`, 745–746 the title and question strings. Corrected at `:83`, `:379`, slice 4 and in the evidence JSON |
| F8 | seam citations off by one at both ends | **REPAIRED** | Confirmed: comment 26–29, const 30–33; comment 35–41, const 42; 25 and 34 blank. Corrected at `:82` and in the evidence JSON |
| F9 | five relationship ranges mix conventions | **REPAIRED** | `:377` states one convention ("by brace"), gives 562–581, 582–590, 591–599, 600–608, 609–617 and the whole span 562–617, and says the dossier understates the end by nineteen lines |
| F10 | `surfaces` closes at 750 | **REPAIRED** | Confirmed: opens 710, closes 750, file ends 752. Corrected at `:378` and `:555` |
| F11 | `model.surfaces` is one of five fields | **REPAIRED** | `:83` now says "the only input for the three surface panels", and the five-field set is exact. See **G10** on the hit arithmetic |
| F12 | "dossier overstates" misattributed | **REPAIRED** | Confirmed: the three-edges sentence is at `docs/pursuits/2026-09-13-vision-pursuit.md:205`, inside the "What" bullet. `:82` now says "What" bullet and credits the caveat to both the dossier's slice-6 bullet and L5-M7 |
| F13 | fifth page uncensused | **REPAIRED** | Re-swept this session: the retained exact-source capture has 6 hrefs, 1 fragment, 5 non-fragment — the four nav links plus `/polaris#polaris-source-openspec-specs-switchboard-identity-spec-md`. `:113–127` states exactly this and draws the honest conclusion. The four-page figures re-derive too: home 40 = 36 + 4, Trajectory 304 = 300 + 4, Orrery 23 = 19 + 4, Polaris 1,089 = 699 + 386 + 4 |
| F14 | `walkthroughJudgment.outcome` misattributed | **REPAIRED** | `:358–364` attributes it to L5-F10's evidence list and states that `walkthroughJudgment` does not occur in the dossier `.md`; confirmed |
| F15 | "713 claim tuples" had no evidence entry | **REPAIRED** | `claim_tuple_census` now records 713 lane A and 699 pre-lane-A with the 699→713 note. Re-derived: `data-claim-id="` occurs 713 times on both lane A captures, 0 on the three small pre-lane-A pages |
| F16 | registry file's candidate status; wrong instrument | **REPAIRED** | `:461–465` states both facts; confirmed from the JSON — top-level `status` is `candidate-amendment-no-effect-until-owner-act`, `typedAuthority` sits inside `entries[0]`, and all five quoted values are exact |
| F17 | unenumerated vocabulary counts in Q2 | **REPAIRED** | The Q2 rewrite states the two legal states explicitly and no longer counts vocabularies. But the framing sentence the count belonged to now sits on Q6 instead — see **G4** |
| F18 | "three paragraphs on"; missing ellipsis | **REPAIRED** | Confirmed: the "fact of the render" sentence is at `rendering-vocabularies.md:111–114`, in the paragraph opening at 98, immediately after the 92–96 declaration. `:497` says "the next paragraph" and `:496` supplies the ellipsis and the elided fragment |
| F19 | v1.md artifact phrase spans 119–120 | **REPAIRED** | Confirmed verbatim at both `:831–835` and the handoff `:1352–1353`: the artifact phrase at 119–120, the criterion sentence at 118–119 |
| F20 | Orrery byte size blank | **REPAIRED** | `:36` reads 37,048; `wc -c` agrees |
| F21 | five lines over 78 columns | **NOT REPAIRED — disclosed, and defensible** | Re-measured this session: 5 lines, at 1, 462, 537, 909, 936, over a denominator of 1375. Four are single unbreakable path code spans, which AGENTS.md forbids reflowing; the H1 is left long for consistency with the sibling packets, stated at `:1289` |
| F22 | observed-repository paths in plain prose | **REPAIRED** | `:296–301` adds the clarifying sentence; `check_governance.py` still passes 0 FAIL |

Figures re-derived beyond the F-list, all computed this session by script
over the retained captures and reads at commit `6218726`:

- 22 `data-unknown-disclosure` elements on both lane A Polaris captures;
  element-inner sweep gives 13 carrying both `data-unknown-reason="` and
  the literal `Route:`, 9 carrying neither, **0 mixed**; all 22 offsets,
  depths and keys in the packet's table at `:265–286` match row for row;
  page length 1,481,819 characters.
- Literal `Route:` 18, `data-unknown-reason="` 16, on both lane A forms.
- Capture sha256s: all six match the packet's provenance table.
- Register method re-run as the register itself defines it (split on `## `
  headings; at line start in each section, a table row whose first cell is
  `P-` followed by anything but a cell break): **5** acceptance-act rows
  (P-1…P-5), **0** in the reading aid, **22** open rows (P-10 through P-53
  including the sub-lettered `P-25(c)`, plus P-71), **27** in all. The
  register's stated 22 / 5 / 27 at `:128–130` is exact. P-68, P-69 and P-70
  are absent from this branch's copy, as the note and Q7 both say.
- Spec sweeps: 24 POC requirements, 17 PWB requirements, 0 whole-word `home`
  in the POC spec, 6 in the PWB spec, 0 hits for the backticked `surfaces`
  or `model.surfaces` in either. Gate 5's three sweeps hold.
- POC-REQ-060's scope-of-quantification sentence and falsifier quoted
  verbatim at the clause (`spec.md:927–946`); RFC2-24 at
  `rendering-vocabularies.md:92`; VIS-5 at `vision.md:141`; PWB act 70–72
  and 86–94; mode direction 18–22 and 26–32; v1.md 30–31 and 118–120 — all
  verbatim at their defined locations.
- `polaris.ts` citations re-read: `gapId` 136, the linking at 145,
  `gapReasonCounts` 922, `gapsList` 933–948 with `foremost` at 938,
  `routeOf` 462–467, `reasonRouteHtml` 472–476. All exact.

## Q1–Q7 assessment

| Q | Problem scope truthful? | Genuine owner gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | **Partly.** The 22 / 13 / 9 decomposition is exact and the three-surface widening is the right correction. But the sentence reconciling the two marker families is false and the third encoding's denominators are inflated by two non-claim occurrences per page (G3) | **Yes.** Ruling a rendered population in breach of an in-force invariant is the owner's, and the packet labels the `PocRelationship` question [Unknown] rather than deciding it | **Yes on the falsifier and on the remedy.** The F1 repair removes the self-defeating step review 1 found: slice 1 now renders the implementation's strings | **Yes**, and the register carries the same inflated figures (`:113`, `:209`) |
| Q2 | **Yes, now.** The code claim is corrected, both `routesFor` branches are quoted, the deferred arm is named and its copy row found | **Yes**, and correctly re-opened as a genuine choice with the mint-and-retire arm offered | **Yes.** "Narrow the prohibition to Unknown-carrying-`reasons`" follows from the type; S3 and slice 2 both carry it | **Yes**, clause for clause |
| Q3 | **Yes.** Unchanged from review 1, which found it the clearest gate in the packet | **Yes** | **Yes.** Three arms, each lawful, each costed; build-the-pure-drafter-regardless still sound | **Yes** |
| Q4 | **Yes.** `data-polaris-gap` once, `polaris-gap-excluded-content`, "12 claim(s)"; `foremost` at `polaris.ts:938` confirmed | **Yes**, and still the one question labelled a real choice between two lawful arms | **Yes** | **Yes** |
| Q5 | **Yes on both limbs now.** The expectation half re-verified; the authorization half states both readings, quotes Reading B's three code facts and the act's prohibition, and refuses to resolve it | **Yes**, and the [Inferred] label plus the stated counter-argument is the right shape for a contested authorization | **Defensible, not smoothed.** Reading A rests on a citation that is misplaced and re-ordered (G5), which weakens its footing without changing its substance | **Yes** |
| Q6 | **Yes on the defect.** The five-field reading is corrected and 747–748 is right | **Yes — but the preamble says otherwise.** `:67–69` calls it contract-determined with one lawful arm, against the packet's own four-times-stated finding that nothing governs the field (G4) | **Yes.** Derive-don't-delete follows, and the false "only input" step is gone | **Yes** — the register row states it as a free choice, so the register is *more* accurate than the packet's preamble here |
| Q7 | **No.** The register analysis is exact and the M3 band duplicate is a real catch. But the M2 shared set is still one file short, M2 slice 2's opening band is missed, and the slice attributions are wrong for both siblings (G1, G2, G9) | **Yes.** Ordering four packages is the owner's | **No.** "One band, one owner, one oracle" and the five-step order are derived from a two-way collision that is actually three-way, and from a file set that under-counts the copy-array conflict | **No** on one clause: the register's "M2's slice 5 and M4's slice 2 both edit the reason-route table" is denied by the packet's own Collision section (G6) |

**Smoothing check.** I found no owner trade-off smoothed into consensus
language, and several deliberately preserved: Q5's two readings are quoted
against each other and neither is resolved; Q4 states the owner's reason for
the arm the packet does not recommend, in the owner's terms; Q2 now offers
the mint-and-retire arm it previously foreclosed; Q1's other-way branch at
`:1366–1374` still states the divergence and where it would be written down;
Q6's row still names deletion's cost. The candour is intact. The defects
above are errors of fact, of arithmetic and of analysis.

**Lawful-arm check.** One lawful arm is called unlawful: deletion, in Q6's
preamble at `:67–69` (G4) — contradicted by the Q6 row itself, which is why
it is a framing defect rather than a foreclosure. No other arm is mislabelled
or missing; the two arms review 1 found missing (the `basis: 'deferred'`
treatment and the continuation-act arm) are both present now.

**Rule-2 and rule-9 check.** Every universal I tested carries a predicate and
a denominator run this session, with one class of exception: the
`epistemic-unknown` populations at 301 / 11 / 18, whose predicate is stated
("token occurrences") but whose denominator includes a stylesheet declaration
and a legend row, and whose Polaris counterpart is asserted in prose while
the evidence record holds `null` (G3). The "zero cross-surface deep links"
universal is now correctly bounded to its four-page population with the fifth
page censused. "M4 shares four files with M2" is an absence claim over a
population the packet was itself deriving, and it is wrong by one (G1).

**Rule-8 check.** Every contract quotation resolves at its defined clause and
is verbatim, with one exception of place and order: the PWB authorization
fragment in Q5's Reading A (G5). One doctrine claim is anchored to a clause
that does not say it: the "two adapters VIS-5 requires" sentence (G8).

**Act coverage.** Slice 7's arm-(a) act, slice 8's two acts, and the
DEFERRED-WAVE-POSTURE constraint on citing RFC10-7 are all carried correctly.
Slice 6 is now contested-and-conditional rather than asserted. The slices 4–5
recorded-finding arm is stated as an explicit owner-facing limb of Q7 with
its [Inferred] label, which is what F6 asked for.

## Counts

| Severity | Count |
|---|---|
| blocking | 4 |
| non-blocking | 5 |
| editorial | 2 |

## What the repair did well, for the record

F1 is the model of how to answer a finding: the claim was not merely deleted
but replaced with the measured split, the five identical and the seven
differing keys enumerated with their exact differences, the consequence for
slice 1 drawn, and the alternative named as the separate twelve-value change
it would be. My independent extraction agreed with it key for key. F2 is
nearly as good — the deferred arm is not just acknowledged but traced to its
declared copy row, and both the slice design and the acceptance scenario were
narrowed to match rather than patched in prose. F13's repair turned a
weakened universal into an argument *for* slice 5, which is the right
instinct.
And the packet's disclosure of what changed after review 1 — four recommended
answers, named, with Q3, Q4 and Q6's recommendations explicitly marked
unchanged — is exactly the shape a second reviewer needs and is rarer than it
should be.

The four blocking findings all sit in one place: the collision and
cross-surface *measurement* work, where a correction was applied to the
instance review 1 named and not to the class it belonged to.

Verdict: REVISE
