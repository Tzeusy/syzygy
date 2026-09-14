# R-POLARIS-M3-HONEST-ENCODING-FUNNEL-5-RAW

Independent fresh-context review **5** of the M3 feature-request funnel packet
(bead `syzygy-dov.3`), its evidence record, and the P-70 note and row in the
pending-owner-decisions register. Read-only session: no file in any repository
or worktree was modified, no state-changing git command was run, no `bd` write,
no daemon, no network, no Butlers checkout read. The one file written is this
raw.

Reviews 1–4 are retained at `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md`
(F1–F14), `…-2-RAW.md` (G1–G9), `…-3-RAW.md` (H1–H11) and `…-4-RAW.md`
(J1–J9); every one of the four verdict words, copied exactly: **REVISE**.
This review binds the bytes named below and no others (verification rule 10).

## Header — commit and reviewed bytes

Worktree: `/tmp/claude-1000/-home-tze-GitHub-syzygy/6b8e9d74-3b46-4418-b725-5b74d21d660a/scratchpad/m3wt`,
branch `agent/syzygy-dov.3`, HEAD
**`76e897f46c50c90f368e629d8de55488d96b7c73`**
(`76e897f docs: M3 funnel review 4 retained and J1–J9 repaired; review-3 dispositions restated [syzygy-dov.3]`).
Working tree clean (`git status --porcelain` empty).
`git diff --stat a9f671e..76e897f` is seven files, 4,715 insertions, **0
deletions** — all of them this packet's own artifacts, so every source file
this packet cites by line is still at the baseline bytes [Observed].

Digests computed this session with `wc -c` and `sha256sum`, never transcribed
(verification rule 3):

| File | Bytes | Lines (`wc -l`) | sha256 |
|---|---|---|---|
| `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md` | 139,050 | 1,734 | `254f72e3308052944b7e19276d948d10c15132765ea4a2395c50a75705bcd45d` |
| `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json` | 50,219 | 856 | `52e14c419ad62a6ad603067152af250de4a887ee297d0315eaa24fecedea2f45` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 33,783 | 215 | `1754fe069c7635a0ae35b3b958a24e33e54f98c29b5ed4283d135a34daa0ef31` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md` (reference) | 31,503 | — | `1eca5fbac6fe95266ac4968f5b55ebf89e6e63544441383c545fb89b9140bc1f` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-2-RAW.md` (reference) | 48,381 | — | `a04b20517539e971c1e192015329dd39a2e2f536b52c06fffdce473177397012` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-3-RAW.md` (reference) | 42,726 | — | `7154f1f3972cfc73619694d48851f4368a8eb7fdce77cadb81493290f82c5aa6` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-4-RAW.md` (reference) | 40,037 | — | `2c3a91917d957ad58a16b5c2cddbcc5326c412e4c35b89531c317c41b6a4d947` |

The packet's stated digests for all four retained raws match mine exactly, and
its stated sizes for the three artifacts review 4 read at `f35a25f` —
129,183 / 42,787 / 32,136 — are exact against `git show f35a25f:<path> | wc -c`
this session, as are the review-3 figures 115,201 / 36,743 / 31,054 at
`b34fca7` [Observed].

Reference bytes read read-only outside this worktree, digests recomputed
before any measurement and identical to the record's:

| File | Bytes | sha256 |
|---|---|---|
| `.../scratchpad/m1/measure/after/polaris-tailnet.html` | 1,484,487 | `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` |
| `.../scratchpad/capture/home.html` | 38,706 | `c2fd6d1af7103e871c26dc65b76cc391fe2765a1c7391ac19ddf1656e57b5fca` |
| `.../scratchpad/capture/trajectory.html` | 244,524 | `fd802531b199084e7145932715150f4977335e49ca6aa168d68d5227c9d6ddde` |
| `.../scratchpad/capture/orrery.html` | 37,048 | `e3ae5b7901c599a04b685456e6070430edf72fcd025cd1f6afecf863153582fa` |
| `.../scratchpad/capture/api-poc.json` | — | read this session |

`python3 scripts/check_governance.py` from the worktree root ends
**`32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted`**
[Observed: run this session].

## What re-derived clean

Every load-bearing figure was re-derived independently this session from the
named bytes with Python `re` and literal `str.count`, never shell grep
(verification rule 1). All of the following are **exact**:

- Capture 1,484,487 bytes / 1,481,819 decoded characters.
- `class="claim-tuple"` **713**; distinct `data-claim-id` over those spans
  **703**; `data-epistemic-label="Observed"` **702** / `="Unknown"` **11**;
  `data-epistemic-tier="unstated"` **11**; `data-epistemic-freshness="fresh"`
  **713**; `data-challenge-state="unchallenged"` **713**.
- `class="unknown-disclosure"` **22**; `class="unavailable-notice"` **0**;
  `class="proposal"` **0**; `class="proposal-label"` **1**, at **56.29%**
  depth. Polaris declared badge spans **2**, both in the legend, body **0**.
- Served stylesheet: one `<style>` block, **206** rules; exactly **2** name
  `.claim-tuple` — one colour treatment over all 713. Literal probes
  `claim-tuple[`, `[data-epistemic-label`, `[data-epistemic-tier`,
  `[data-epistemic-freshness`, `[data-challenge-state` each return **0** over
  all 206 selectors. `var(--unknown)` in **5** rules, `var(--cyan)` in **17**.
- Cross-surface population, recomputed from the four capture files under the
  packet's stated predicate: home 35, trajectory 299, orrery 18, Polaris 735;
  four-page **1,087**, declared **352**; three-surface **1,052**
  (735 + 299 + 18); 735/1052 = **69.87%**, 735/1087 = **67.62%**.
- First reading: boundary at the first `data-polaris-group="catalog"`,
  character **281,986** = **19.03%**; **126** tuples in the region, **all
  Observed**; **0** `unknown-disclosure` blocks. First rendered Unknown of any
  kind at **25.55%**; first Unknown *tuple* `claim:class:roster-identity` at
  **25.70%**; the whole-shape Unknown at **57.72%** — the register's 25.70%
  and the packet's 25.55% are each correct for their own referent.
- Item and source rows: `data-polaris-item="` **409**, bare
  `data-polaris-item` **417**, `data-polaris-items` **8**.
- Machine channel, re-walked independently: **1,149** objects carrying both
  `claimId` and `epistemic` over **1,148** distinct ids; **12** carry an
  `epistemic` with no `tier` key, **all 12 labelled Unknown**, keyset exactly
  `['freshness','label','reasons']`; all **11 of 11** human-side Unknown tuple
  ids match one of them. Tier histogram `report-fact` **1,137**, absent **12**.
  `unstated` occurs **0** times in the machine answer.
- Colour: 10 tokens at `design-tokens.ts`:46–55 read line for line, **9**
  distinct values, **36** pairs over the distinct set. Recomputed (CIE76 over
  CIE Lab, D65): `--amber`/`--unknown` **7.8462** is the smallest over the five
  foreground tokens and `--ink`/`--muted` **26.7371** the next; over the full
  distinct nine, **seven** pairs sit strictly below the 26.7371 floor
  (3.9753, 4.8231, 7.8462, 8.7759, 14.9639, 19.5580, 23.2692). `--focus`
  equals `--amber` exactly (ΔE76 0.00), which is why the distinct set is 9.
- Byte arithmetic: 1,484,487 − 1,400,000 = **84,487**; 2,097,152 − 1,484,487 =
  **612,665**; 702×19 + 11×18 + 702×4 + 11×2 = **16,366**; 409 × 32 =
  **13,088**.
- Checker: `surface-routes.test.ts`:64–101 reads `const denominator =
  pages.length` over `['/', POLARIS, TRAJECTORY, ORRERY]` = **4**, tests each
  page with `page.html.includes('class="epistemic epistemic-observed"')` /
  `-unknown`, and `continue`s a page carrying neither — the legend alone
  satisfies it [Observed: file read this session].
- Source citations re-read at HEAD and exact: `polaris.ts` 305–308 (the two
  `?? 'unstated'` mints at 306–307), 346–361 (`claimStatesBlock`, freshness
  group at 357), 506–510, 1307 (`.claim-tuple`), 1328 (`.proposal`), 1329
  (`.proposal-label`, `color: var(--unknown)`); `design-tokens.ts` 46–55;
  `polaris-copy.ts` 34–51 (**15** state sentences — 3 label + 7 tier +
  4 freshness + 1 challenge — plus **3** group labels, so Q5's "twelve
  tier/freshness/challenge states" and "9 unreachable" both re-derive);
  `packages/cap1-core/src/staleness.ts` 18 and 98–104.
- Contract and spec quotes re-verified verbatim against source under
  whitespace and blockquote normalisation, with the source's own emphasis and
  no additions: RFC2-10's mint prohibition, its disclosure remedy and its
  orthogonality sentence (`snapshot-and-evaluation-core.md` 209–223); RFC2-25's
  bare-label remedy, its three-member sibling list (:169) and "a tier never
  becomes a fourth epistemic label"; RFC7-34 (`rendering-and-surface.md`
  241–243); CC-VIZ-1's legend clause; `doctrine/trust-and-evidence.md`:101;
  PWB-REQ-007 (spec 439, 443–446, with `…` between retained bullets) and
  PWB-REQ-020 (:902, with `…`); the 2026-09-02 authorization's full
  escalation-trigger sentence, matched as an exact substring of
  `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`.
- Code-span sweep over the packet outside fenced blocks: 44 path-shaped spans;
  every fully-qualified path resolves in the worktree, and the 8 non-resolving
  spans are git refs, shell commands, a glob, an HTML fragment and a
  `proposed/spec.md.patch` shorthand — not paths. **No Butlers repository path
  appears in backticks**: the only two `butlers`-matching spans are the Syzygy
  `openspec/changes/polaris-project-wide-butlers-model/…` paths [Observed:
  denominator every backtick span outside fences].
- No manifest row, act argument or truncated signed digest is quoted anywhere
  in the packet, record or register.

The measurement work remains exceptional, and survives a fifth independent
re-derivation with **no discrepancy in any figure taken from the captures, the
machine answer, the token set or the source files.** Every finding below is in
prose that reasons *about* the repairs.

## Findings

### K1 — blocking — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:1588 and :1652, with `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:837 — the J7 repair publishes a false provenance claim that the review it cites disproves, on a sweep figure it now states under two incompatible denominators

**Defect.** J7 (editorial) asked the H1 row's sweep figure to be date-stamped
or re-derived. The repair instead asserts that the figure is not reproducible
at all. The H1 row (:1588) now reads, in full:

> Swept the packet, record and register for `supplies no`, `no absence`, `not
> lawfully available`, `unlawful`, `no remedy` and `supplies none`: 25 literal
> occurrences over 2,482 lines across the three files — a figure taken on the
> working tree during the review-3 repair, between `b34fca7` and `f35a25f`, so
> **reproducible from no commit** (review 4, J7; re-derived at `f35a25f`: 41
> over 2,697 lines with the same six literals …)

and the J7 disposition row (:1652) says "the three files sum to 2,479 lines at
`b34fca7` and 2,697 at `f35a25f`", with the evidence record (:837) recording
the confirmation as `"wc -l over the three files: 2,479 at b34fca7, 2,697 at
f35a25f; the H1 row's 2,482 matches neither - confirmed"`.

Three things are wrong, all in the bytes:

1. **The claim is false, and its own cited authority says so.** Review 4's J7
   reads: *"Re-run this session with those six literals over the three files:
   at `b34fca7`, **25 occurrences over 2,482 lines** — exact."*
   (`…-4-RAW.md`:359–361). I reproduce the same pair independently this
   session: at `b34fca7`, the six literals give **25** occurrences over the
   three files, and the three files carry **2,482** lines counting each file's
   trailing line (2,479 by `wc -l`; 2,479 + 3 = 2,482). The figure is
   reproducible at exactly one commit — `b34fca7`, the bytes review 3 read —
   which is what J7 asked to be stamped.
2. **The "matches neither" confirmation is a method switch presented as a
   fact.** 2,482 and 2,479 are the same population counted two ways. The repair
   pass adopted `wc -l`, got 2,479, and concluded the figure matched no commit;
   it did not state either method, and did not test the convention that
   produces 2,482.
3. **The packet now carries two incompatible denominators for one population
   at one commit, in one document**: 2,482 in the H1 row and 2,479 in the J7
   row, both for the same three files at `b34fca7`. The H1 row's own before/after
   pair is mixed — 2,482 (trailing-line convention) against 2,697 (`wc -l`);
   under one convention the growth is 2,482 → 2,700, under the other
   2,479 → 2,697. Neither convention is disclosed at either site.

Verification rule 3 says totals are computed; rule 9 says a claim of absence
needs a sweep with a denominator — and "reproducible from no commit" is a
claim of absence over commits, made without testing the one convention that
reproduces it. It is published in a disposition row marked **CONFIRMED —
REPAIRED**, and the review-4 section's "All nine findings confirmed" (:1637)
rests on it. This is the class reviews 2, 3 and 4 each blocked on — a
disposition row asserting something untrue of the bytes — recurring for the
fifth time, this time introduced *by* the repair rather than left standing by
it. Nothing here moves a recommendation, a gate or an owner question; what it
damages is the one property this packet's review history is for.

**Repair.** Restore the stamp J7 asked for: "as of `b34fca7`, the bytes review
3 read: **25** occurrences over **2,482** lines counting each file's trailing
line (**2,479** by `wc -l`)", and give the `f35a25f` re-derivation the same
convention (41 over 2,700, or 41 over 2,697 by `wc -l`) so the pair is
like-for-like. Correct the J7 disposition row and record `:837` — the figure
matches `b34fca7`; it was the line-count convention, not the commit, that
differed.

### K2 — non-blocking — packet :1687 (funnel summary) against :1692 (handoff) — J6's repair reached the handoff section and not the funnel-summary block the owner copies

**Defect.** J6's repair added Q6 to the handoff's condition line, correctly and
with the lawful alternative named (:1692–1697, verified this session). The
funnel summary's own handoff line (:1687), inside the fenced block that is the
owner's copy-out artifact, is unchanged:

> `Recommended handoff: Q1 "a non-conformance" and Q3 "inheritance" -> run
> slices 1-4 now under syzygy-dov.3, in parallel with P-68 and M2; …`

Two answers short (Q4 and Q6), and it also still says "run slices 1-4 now"
where the repaired handoff says slices 1, 2 and 4 immediately with slice 3
next. `git diff f35a25f..76e897f` touches the handoff section and not this
line [Observed].

This is precisely H3's and J5's shape — a repair that reaches one statement of
a recommendation and not the other — applied to J6's own repair, and the site
it missed is the block most likely to be read alone.

**Repair.** Bring :1687 into line: `Q1 "a non-conformance", Q3 "inheritance",
Q4 "yes" and Q6 "a --proposed token" -> run slices 1, 2 and 4 now …, slice 3
next`, or cite the handoff section rather than restating its condition.

### K3 — non-blocking — `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:282 — RFC2-10's mint prohibition is anchored to a line that does not carry it, and the same clause's remedy is given two different extents in the packet

**Defect.** `vocabulary_versus_rendered.freshness_mint_hazard` reads "RFC2-10
forbids the mint in terms (line 219)". Line 219 of
`snapshot-and-evaluation-core.md` is `verbatim nor checked for parity, and
leaving it unstated is how the value gets` — the parity rationale, not the
prohibition. The prohibition is at **213–214**: "The list changes only by
amendment to this RFC; no implementation may mint, spell, or force-fit a
freshness value it does not carry" [Observed: source read line by line this
session]. The pointer was introduced in the review-3 repair pass (absent at
`b34fca7`, present at `f35a25f`) and review 4 did not reach it.

AGENTS.md verification rule 8: *anchor a contract claim to a defined clause and
quote it; nearby prose is not the clause.* The clause identifier is right and
the sentence is quoted verbatim in the sibling field
(`closed_freshness_vocabulary_authority`, :279, which I matched character for
character against 209–223 this session) and in Gate 2, so the substance holds —
but the field the P-70 row names by path as Q2's substance sends a reader to
the wrong sentence.

Second limb, same clause: the remedy sentence runs **220–222** ("A condition
genuinely outside the four is disclosed as a fact of the render, never dressed
as a freshness state."), with 222–223 carrying the separate orthogonality
sentence. The packet's G1 row (:1528) says "`snapshot-and-evaluation-core.md`:220–222";
the H1 row (:1588) and record `review3.repairs.H1` (:804) say "lines 220–223".
One extent for one sentence.

**Repair.** Change "(line 219)" to "(lines 213–214)" and quote the six words;
settle the remedy's extent at 220–222, with 222–223 named separately as the
orthogonality sentence, at all three sites.

### K4 — non-blocking — `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:804 — `review3.repairs.H1` still describes the H1 repair as complete, unmarked, while its sibling `review3.repairs.H5` carries J2's correction

**Defect.** The record's `review3.repairs.H1` reads, in full:

> "this record's vocabulary_versus_rendered.freshness_mint_hazard rewritten to
> RFC2-10's actual remedy (lines 220-223) **and the three lawful arms**, with
> the withdrawn wording quoted and marked in place"

J3 found those three arms matched neither the packet nor the register, and the
field was rewritten again in this pass. The sentence carries no marker. Its
sibling `review3.repairs.H5` (:808) *was* restated in the same pass — "was NOT
corrected in the same pass and still read 9 - corrected after review 4, finding
J2" — as was `review2.repairs.G1` (:741), and the packet's H1 row (:1588) names
J3 explicitly. So the correction exists in three places and not in this one,
which is the only one an automated reader of `review3.repairs` would see.

Not blocking: no substantive claim is wrong, and the arm text itself is now the
packet's verbatim (confirmed by exact string comparison this session). But it
is the same "the record is repaired last" shape in its smallest form, and the
in-place-marking discipline the packet applies everywhere else was skipped
here.

**Repair.** Append the marker the sibling fields carry: "(the three arms
enumerated here did not match the packet's or the register's — corrected after
review 4, finding J3)".

### K5 — editorial — `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`:107–115 — the P-70 note's date stamp predates the review-4 material it now carries, and its review-1 clause states a completeness the packet itself scores 10/4

**Defect.** The note opens `> **Updated 2026-09-14 (Polaris honest encoding):**`
and was edited in this commit (dated 2026-09-15 in the packet's own
"## Review 4 and repairs (2026-09-15)" heading) to change "three independent
reviews" to "four" and to add review 4's summary [Observed: `git diff
f35a25f..76e897f` on the register]. The stamp now covers content added a day
later — the staleness-at-the-sentence problem the project has recorded, in a
note whose whole function is to date what changed.

Second limb: the note describes review 1 as "(REVISE, four blocking, **every
finding repaired after it**, two recommended answers reworded)", and the row's
review-1 citation as "all fourteen findings repaired after it". The packet's
own review-2 section (:1516–1520) records the verified result as **10
REPAIRED, 4 PARTIAL** over a denominator of 14 — the figure J2 was filed to get
right, and which I recounted from `…-2-RAW.md`:461–474 independently this
session (REPAIRED F1, F2, F3, F5, F8, F9, F10, F11, F13, F14; PARTIAL F4, F6,
F7, F12; NOT REPAIRED 0). The four were closed by the review-2 pass, so the end
state is defensible — but the register, which is what the owner rules from,
reads cleaner than the packet on exactly the point two reviews spent findings
on.

**Repair.** Add a second date to the note line ("updated again 2026-09-15 for
review 4"), and qualify the review-1 clause: "fourteen findings, ten repaired
in that pass and four closed after review 2 (10 REPAIRED / 4 PARTIAL as review
2 verified)".

### K6 — editorial — record :282 and `review4.repairs.J3` — "the packet's and register's own words" is true of the packet only

**Defect.** `freshness_mint_hazard` says its arms are "stated here in the
packet's **and register's** own words", and `review4.repairs.J3` says they were
"rewritten in the packet's and register's words". The text is the packet's
verbatim — I matched it character for character against packet Q2 this session
— and the register's wording differs throughout ("which is P-69's Q7" for
"(M2's Q7, recommending `stale` …)"; "outside the `data-epistemic-freshness`
slot, never dressed as" for "in a carrier that is not
`data-epistemic-freshness` and is not dressed as"). The three arms denote the
same three things in all three artifacts — that is J3 discharged — but the
record claims a verbatim identity with the register it does not have.

**Repair.** "stated here in the packet's own words, which the P-70 row
paraphrases clause for clause".

## J1–J9 verification against the current bytes

Each re-derived from source, the retained captures or the retained raws this
session, not taken from the review-4 section's own account.

| J | Severity (review 4) | Verified verdict | Evidence |
|---|---|---|---|
| J1 | blocking | **REPAIRED** | `closed_freshness_vocabulary_authority` (json :279) now quotes from "Four values, closed." to the clause's end; I extracted the quoted span and matched it as an exact string against `snapshot-and-evaluation-core.md` 212–223 under whitespace and ASCII normalisation — **identical** — with the truncation disclosed in place ("until then this field stopped at line 214 with no elision marker"). `review2.repairs.G1` (:741) now names "this record's own vocabulary_versus_rendered.freshness_mint_hazard field, a fifth site the review-2 repair pass missed". The packet's H1 row (:1588) is restated to the three limbs and marked PARTIAL at `f35a25f`. (Its sweep sentence is **K1**; `review3.repairs.H1` is **K4**) |
| J2 | blocking | **REPAIRED** | `review2.f_verification_against_review_1` (json :730) now reads `{"REPAIRED": 10, "denominator": 14, "PARTIAL": ["F4","F6","F7","F12"], "NOT_REPAIRED": 0}` with the raw's three disagreeing figures noted. I recounted `…-2-RAW.md`:461–474 by parsing the table's verdict column, one row per finding: **10 / 4 / 0 over 14**, identical to the record and the packet. `review3.repairs.H5` (:808) is restated; the packet's H5 row is marked PARTIAL at `f35a25f` |
| J3 | blocking | **REPAIRED** | `freshness_mint_hazard` (json :282) now carries the packet's (b-i)/(b-ii)/(b-iii) — string-compared against packet Q2 this session, **character for character identical** after ASCII normalisation — with the mismatched review-3 enumeration quoted and marked withdrawn in the same field. The register's paraphrase denotes the same three arms (Q-table below). (The "and register's own words" overreach is **K6**) |
| J4 | non-blocking | **REPAIRED** | Both denominators stated with the reason for the wider sweep, at the population prose (:195–201), Q1 (:57), slice 2 (:865), the funnel summary (:1678) and the register's Q1 limb (:211); `cross_surface_population` carries `three_surface_total_per_poc_req_060: 1052`, `three_surface_pages`, both percentages and `why_four_pages`. Re-summed from the four captures: 1,052 and 1,087, 69.87% and 67.62%. The phrase "the other three surfaces" survives only inside the J4 row that withdraws it |
| J5 | non-blocking | **REPAIRED** | The P-70 row's Q2 limb now carries the clause. Re-derived independently: 12 of 1,149 machine objects have an `epistemic` with no `tier` key, **all 12 labelled Unknown**; each of the 11 human-side Unknown tuples matches one; keyset exactly `['freshness','label','reasons']`. The row states it as a PWB-REQ-020 parity question "this packet discloses and does not resolve" — a disclosure, not a resolution |
| J6 | non-blocking | **PARTIAL** | The handoff's condition line (:1692) now reads "If Q1, Q3, Q4 and Q6 are answered as recommended", with the dated-exception alternative named for the other arm — repaired. The funnel summary's own handoff line (:1687) still conditions on Q1 and Q3 and still says "run slices 1-4 now" — **K2** |
| J7 | editorial | **NOT REPAIRED** | The stamp J7 asked for was not applied; in its place the H1 row (:1588) and the J7 row (:1652) assert the figure is "reproducible from no commit", which review 4's own J7 disproves and which I disprove again this session at `b34fca7` (25 occurrences, 2,482 lines counting each file's trailing line). The packet now states 2,482 and 2,479 for the same population at the same commit — **K1** |
| J8 | editorial | **REPAIRED** | The baseline bracket (:19–25) no longer counts the packet's own commits: "the worktree branches from `a9f671e`, and the only commits on it are this packet's own artifacts … `git log --oneline a9f671e..HEAD` in the worktree lists them". Confirmed: four commits, seven files, 4,715 insertions, **0 deletions**, all packet artifacts [Observed] |
| J9 | editorial | **REPAIRED** | Gate 3's bracket (:783–792) is split: "[Observed for five of the six: …" — I counted the five textual limbs — "Inferred for the scope limb: that every slice implements behaviour the signed change already requires is a reading of that change's own requirement text, argued at Gate 5, not a textual absence". The Gate 5 pointer is present |

Summary: **7 REPAIRED, 1 PARTIAL, 1 NOT REPAIRED**, over a denominator of 9.

## H, G and F findings — regression spot-check

I did not re-litigate accepted repairs; I checked that the bytes prior reviews
confirmed are still those bytes, and specifically the six record line numbers
the packet cites.

- **The cited record lines still point where the packet says**, despite the
  record growing 824 → 856 lines: `:279` is
  `closed_freshness_vocabulary_authority`, `:282` `freshness_mint_hazard`,
  `:674` `review1.recommended_answers_changed.Q2`, `:730`
  `review2.f_verification_against_review_1`, `:741` `review2.repairs.G1`,
  `:808` `review3.repairs.H5` [Observed: each line printed this session].
- **H1 / H5 restatement**: both rows now read "CONFIRMED — **PARTIAL** at
  `f35a25f`, completed after review 4", naming J1/J3/J7 and J2 respectively —
  accurate as to J1, J2 and J3.
- **H2**: `review1.recommended_answers_changed.Q2` (:674) still carries the
  in-place marker with the superseded text kept.
- **H3**: the P-70 row still ends with the mutual-exclusivity clause ("P-69's
  Q7 (`stale`) and this row's Q2 ((b-iii), the disclosure route) are not two
  compatible rulings on the same claims"); collision item 3 unchanged.
- **H4**: the collision section still cites M2 by register row P-69 with one
  dated exception naming `f2f37dd`; `polaris.ts`:506–510 read this session and
  untouched by any M3 slice.
- **H6**: Gate 2 (:518–532) states the machine-side absence with its predicate
  and denominator; re-derived above.
- **H9**: the review-2 section states the bare verdict word plus the counts
  separately; `…-2-RAW.md`:567 is exactly `Verdict: REVISE`.
- **H10 / H11**: both spec block quotes carry `…` between retained bullets; the
  Gate 2 RFC2-10 quote runs 209–223 and matches source, and RFC2-11 begins
  after the next blank line, so "quoted in full" is true.
- **F2 / G7 / colour**: full 36-pair matrix recomputed; seven below the
  26.7371 floor; "26.74 to two decimals, 26.7371 computed" intact.
- **F3 / sibling states**: RFC2-25:169 quoted with the source's emphasis; the
  three sibling states and `challenge-pending` each **0** over the
  1,481,819-character capture.
- **F5 / F10 / counts**: the 713/22 split and the 0/0/22/1 token-reuse counts
  re-derived exactly.
- **F8 / F13 / F14**: `claimStatesBlock` 346–361 with the freshness group at
  357; `design-tokens.ts` 46–55 exactly the ten colour tokens; `polaris-copy.ts`
  34–51 the 15 sentences plus three labels.
- **F9 / G1**: RFC2-10 is the named authority; `staleness.ts`:18 retained and
  labelled the implementation's echo; `staleness.ts` 98–104 is the
  `no-bound-declared` arm returning no freshness field.
- **F12 / G3**: the RFC7-34 quote carries only the source's own
  `**without colour, position, or layout**`; every governed quote I re-matched
  carried the source's emphasis and nothing added.
- **G5 / G8 / G9 / register**: the P-70 row reads "57.72% and 25.70%";
  `trust-and-evidence.md`:101 anchored and marked "by analogy" with its actual
  subject stated; Q3's arm (b) reads "at least 13,088 attribute bytes plus an
  unseparated text component".

**No regression found.** Nothing reviews 2, 3 or 4 confirmed has moved, and
every figure re-derives exactly.

## Q1–Q7

| Q | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | Yes, and J4's repair fixed the one defect: the requirement's own three-surface denominator (1,052, 69.87%) is now stated beside the four-page sweep (1,087, 67.62%) with the reason the sweep is deliberately wider. Both re-summed exactly this session | Yes — a conformance ruling, with the "already conformant" arm written out as a coherent recorded outcome rather than left as silence | Yes. The 713/22 split sharpens rather than softens the finding, and the other arm's consequence ("the four-page checker stands", the 735 become an accepted gap) is stated | **Yes, clause by clause**, including both denominators and the Home rationale |
| Q2 | Yes. Both mints at `polaris.ts` 306–307; tier fires 11, freshness 0; RFC2-25's rendering remedy and RFC2-10's disclosure remedy distinguished at their clauses; the PWB-REQ-007 tension put to the owner unresolved; the machine-channel tier absence disclosed and re-derived (K3 is a line pointer inside the record, not a substance error) | Yes — the strongest gate in the packet, and the packet twice declines to settle it | Yes, and correctly `[Inferred]`. No arm is called unlawful; (b-i) credited to P-69, (b-ii) kept live against the orthogonality sentence | **Yes.** The record's arms are now the packet's verbatim (J3), and the row's paraphrase denotes the same three: (b-i) closed four / P-69's Q7; (b-ii) held Unknown, not rendered as though it had a freshness state; (b-iii) disclosed outside the `data-epistemic-freshness` slot, never dressed as a freshness state. The machine-channel clause is now in the row too (J5) |
| Q3 | Yes. 409/713 from lane B's own record, container mode named; 409 × 32 = 13,088 recomputed; `data-polaris-item="` 409 re-derived from the capture | Framed as a choice; both arms lawful, and arm (b) is said to "spend a ruling the owner has not yet made" | Yes, with the discipline it costs stated as a hard requirement on every M3 sweep | Yes, and the register is stricter ("plus an unseparated text component") |
| Q4 | Yes. 126 tuples, all Observed, 0 disclosures in the 19.03% opening band; 25.55% / 25.70% / 57.72% all re-derived to the exact character offset | Yes — a design ruling on what the owner's first stop opens with | Yes, and the contrary arm is stated as coherent, not strawmanned; CC-VIZ-3 cited for its own subject and `trust-and-evidence.md`:101 marked "by analogy" | Yes; 25.70% names the claim to be surfaced and 25.55% the first disclosure block — each correct for its referent |
| Q5 | Yes. 12 tier/freshness/challenge states in one collapsed disclosure, 0 with a visual encoding, 15 glossary sentences of which 9 unreachable — all four figures re-derived from `polaris-copy.ts` 34–51 and the capture | Yes — a copy-and-encoding ruling binding two later slices | Yes, and it carries three constraints forward, including M2's "mark, do not delete" shape | Yes |
| Q6 | Yes. 1 proposal label at 56.29% in `var(--unknown)`, 5 rules on that token for 4 meanings, 2 rendering 0 times; the closed-vocabulary disclaimer quoted at RFC2-25:169 and the family mints nothing | Yes in form, and J6's repair now discloses in the handoff that slice 2 pulls one rule of Q6's token forward — but the funnel-summary handoff line still omits Q6 (**K2**) | Yes; the ΔE76 floor is stated over a named population with the full matrix in evidence (7.8462 smallest, 26.7371 next, both recomputed), and the alternative arm is named lawful under CC-VIZ-1 | Yes |
| Q7 | Yes. The collision is exact (`polaris.ts`:357, `polaris-copy.ts` freshness sentences, both read this session), and the P-69/P-70 coupling states mutual exclusivity | Framed as a sequencing choice, correctly | Yes. It does not smooth M2's `stale` and this packet's (b-iii) into a reconciled pair | Yes, including the mutual-exclusivity clause |

## Questionnaire invariant

- **Problem scope and recommendation hold against the project's shape and
  engineering bar** — yes. Every slice is app-local, rides the 2026-09-05
  continuation, crosses none of the six escalation triggers (the act's sentence
  quoted verbatim and matched against source this session), and Gate 6 carries
  retained measurement, denominators, rule-6 mutants per guard branch,
  per-tuple parity and an independent review.
- **No owner trade-off smoothed into consensus** — yes, in all three artifacts.
- **No lawful arm called unlawful** — yes, now in the packet, the register
  **and** the evidence record; J3 closed the last divergence.
- **Every substantive claim labelled** — yes; J9 split the one unlabelled
  scope reading.
- **Contract claims quoted at a defined clause** — yes as to text: every quote
  re-matched verbatim against source this session, and RFC2-10 now runs the
  clause's full extent in both the packet and the record. One *pointer* is
  wrong (**K3**), and one clause's extent is stated two ways.
- **Zero/all claims carry a predicate and denominator run this session** — yes
  for every measurement figure, all of which I re-derived. **No** for the one
  sweep figure in the H1 row, which now carries a false non-reproducibility
  claim and two incompatible denominators (**K1**).
- **Digests computed** — yes; every digest in this raw was computed this
  session with `wc -c` and `sha256sum`, and the packet's stated digests for the
  four retained raws and for the three artifacts at `f35a25f` and `b34fca7`
  all match mine exactly.
- **No manifest or truncated signed digest quoted outside the raws; no Butlers
  path in backticks; every code-span path resolves** — all confirmed, with
  denominators above.
- **`python3 scripts/check_governance.py` ends `0 FAIL`** — confirmed:
  `32 OK, 20 WARN, 0 FAIL (52 checks)`.

## Summary

The packet's measurement work survives a fifth independent re-derivation with
no discrepancy anywhere: the tuple counts, the CSS-rule parse, the
cross-surface population under both denominators, the first-reading boundary
and every Unknown offset, the machine-channel tier histogram, the full ΔE76
matrix, the byte arithmetic, the glossary counts and every contract and spec
quote. Seven of review 4's nine findings are repaired in the bytes, and the
three that mattered most are done well: the RFC2-10 quote in the record now
runs to the clause's end, the review-2 repair count is computed rather than
transcribed, and — the one an owner would have tripped over — the record's
freshness arms are now the packet's verbatim, so (b-iii) means the same thing
in all three artifacts.

The one blocking finding is a new defect the repair introduced rather than an
old one it left. J7 asked for a date stamp on a sweep figure. The pass switched
line-counting conventions without saying so, found 2,479 where the figure said
2,482, and concluded in three places — the H1 row, the J7 row and the record —
that the figure is "reproducible from no commit" and that this was "confirmed".
Review 4's J7 says the opposite in as many words: at `b34fca7`, 25 occurrences
over 2,482 lines, *exact*. I reproduce it again here. The packet now asserts a
non-reproducibility that its own cited authority disproves, and carries two
denominators for one population at one commit.

The rule this packet has now paid for five times is unchanged, and it is not
about which artifact gets edited last. It is: **re-derive the figure with the
predicate stated, including the counting convention, before writing the
sentence that disposes of it.** A repair that contradicts the finding it cites
is worse than the stale figure it replaced, because the stale figure was at
least true of a commit.

Findings by severity: **1 blocking** (K1), **3 non-blocking** (K2, K3, K4),
**2 editorial** (K5, K6). Six findings over three artifacts.

Verdict: REVISE
