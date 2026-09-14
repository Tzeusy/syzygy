# R-POLARIS-M3-HONEST-ENCODING-FUNNEL — review 7 (raw, retained verbatim)

Independent fresh-context review. Read-only session; no repo byte was edited,
no state-changing git command run, no `bd` write, no daemon, no network, no
Butlers checkout read. This file is the only output.

## Header — what was read, and at what bytes

Worktree `/tmp/claude-1000/-home-tze-GitHub-syzygy/6b8e9d74-3b46-4418-b725-5b74d21d660a/scratchpad/m3wt`,
branch `agent/syzygy-dov.3`, **HEAD `cfcb745`** ("docs: M3 funnel review 6
retained, L1–L6 repaired [syzygy-dov.3]"), working tree clean
(`git status --porcelain` empty) [Observed].

All figures below computed this session with `wc -c`, `wc -l`, `sha256sum` and
Python `str.count` / `re` — never transcribed (verification rules 1 and 3).

| Artifact | Bytes (`wc -c`) | Lines (`wc -l`) | sha256 |
|---|---|---|---|
| `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md` | 152,072 | 1,867 | `0dc635903b94382d4f3167af3c1f957913a54712cb7f9a3e46bcbb00a8dcde31` |
| `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json` | 61,335 | 958 | `6599db53eeb3fa7a62ab570f09b503a890dd3263292a6201c03e00755ce0e366` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 35,994 | 226 | `44ac06919896b79028a60ce9839dc6bccdf67358a6f76c56e2875096717e7493` |

Line total: **3,051** by `wc -l`; **3,054** counting each file's trailing line
(`len(s.split('\n'))`). Both conventions are the packet's own and both are
reported below.

Retained review 6, as the packet's review-6 section and the record's
`review6.raw` describe it: `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-6-RAW.md`,
**39,570** bytes, sha256
`384f398c3041dc9e59031c84976e61419cedc904c193f3c249af865eebe48ead` — both
recomputed this session, **identical** to the two figures the packet and the
record state [Observed]. Its final line is `Verdict: REVISE`, its summary line
`**1 blocking** (L1), **3 non-blocking** (L2, L3, L4), **2 editorial** (L5,
L6)`, and its K table's summary is `**6 REPAIRED, 0 PARTIAL, 0 NOT REPAIRED**,
over a denominator of 6` — each matching the packet's review-6 section and
`review6.findings` / `review6.k_verification_by_review_6` word for word
[Observed].

The bytes review 6 bound, recomputed from `git show 9cb4d65:<path>` this
session [Observed]: packet **144,850** /
`11766f08d8f227422021c2de7475f7ef20d50a8e2fd83f741f5506b94e310a45`; record
**55,345** / `4c61e5ccc8f51fb03a814914b918069a67806e71b1ab1a5a1872e0e51a4068ee`;
register **35,006** / `be27c3bb880f6d8c08ed3015f0c708ef8419e481447edea30be2f42a3953d852`.
All six figures match the packet's review-6 section exactly. The packet's
rule-10 paragraph ("review 6 binds … and not the current bytes … uncovered
until a seventh independent fresh-context review") is therefore true and
correctly scoped; this review is that seventh, and it covers the bytes in the
table above and nothing later.

Capture: `…/scratchpad/m1/measure/after/polaris-tailnet.html`, **1,484,487**
bytes, sha256 `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111`,
**1,481,819** decoded characters — all three recomputed this session and
identical to `capture` in the record [Observed].

`python3 scripts/check_governance.py` in the worktree ends
**`32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted`**
[Observed, run this session].

## Findings

Two findings, both **editorial**. No blocking finding. No non-blocking
finding. Neither touches a recommended answer, a denominator, a quoted clause
or a figure.

### M1 — editorial — `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:327, against :169, :174 and :948 — the record's third character offset still uses the anchor L6 retired, and the L6 repair sentence is written as if it were record-wide

**Defect.** The record carries four character-offset fields. Three are
consistent after the L6 repair; the fourth is not, and is unmarked.

Re-derived over the capture this session (Python, exact indices) [Observed]:

| Field | Line | Value | What that index actually is |
|---|---|---|---|
| `declared_encoding_use.legend_offset_chars` | :81 | 1,481,009 | the `<` of `<ul class="legend"` — element's opening `<` |
| `first_reading.boundary_offset_chars` | :156 | 281,986 | the index of the literal `data-polaris-group="catalog"`, which its own `predicate` names in terms, so it self-describes |
| `first_reading.first_rendered_unknown_of_any_kind.offset_chars` | :169 | 378,599 | the `<` of the element whose class attribute sits at 378,604 — the L6 repair, with its `offset_anchor` |
| `first_reading.first_unknown_tuple.offset_chars` | :174 | 380,767 | the `<` of the tuple span whose class attribute sits at 380,773 — with its `offset_anchor` |
| `token_reuse.proposal_label_offset_chars` | **:327** | **834,155** | **the `class="proposal-label"` attribute index. The element's opening `<` is at 834,152** |

So :327 is the one field still on the abandoned anchor, and it is the only
offset field carrying neither an `offset_anchor` nor a self-describing
predicate. Meanwhile `review6.repairs.L6` (:948) reads "one anchor adopted
(the element's opening <)" and names only the two `first_reading` siblings —
a sentence a fresh reader will read as a statement about the record, which it
is not.

Nothing downstream moves: 834,152 and 834,155 both give **56.29%** at two
decimals, which is what `proposal_label_depth_percent` and Q6 state, and
which I recomputed [Observed]. This is a consistency-of-convention defect, not
a wrong figure — which is why it is editorial and not more.

**Repair.** Either put an `offset_anchor` beside :327 (adopting the element's
`<` at 834,152, with 834,155 kept on the line as the L6 siblings keep theirs),
or scope `review6.repairs.L6` explicitly to the two `first_reading` fields and
say the `token_reuse` offset is deliberately the attribute index. Do not
silently change 834,155 without keeping it.

### M2 — editorial — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:1475–1479, and `…json`:952 (`review6.sweep_after_repair.predicate`) — the four-box rule does not state the unit it sorts by, and the one hit whose box turns on that unit is written in the present tense

**Defect.** The packet's review-1 section reads, across four hard-wrapped
lines (quoted with the wrap shown, because the wrap is the point):

```
:1475  sharpened. Q2's recommendation was "**Arm (b).**" and is now "**Arm (b) for
:1476  the tier field; arm (b) is not lawfully available for the freshness field, and
:1477  the owner should see why**" — the tier ruling is unchanged; the freshness half
:1478  is new and is the substance of F4 (that freshness wording was itself
:1479  withdrawn after review 2, finding G1; see the review-2 section). …
```

The hit `not lawfully available` falls on :1476. The marker falls on
:1478–1479 — same sentence, three lines away. The four-box rule as the record
states it (:952) sorts hits into, box 4, "review-history text stating the
withdrawn proposition in the present tense with **no marker**", without saying
whether "no marker" is evaluated over the line, the sentence or the section.
The packet's own L1 disposition applies the rule to JSON with a line unit
("`review5.sweep_after_repair.result` is marked superseded **on its line**"),
and AGENTS.md's hard-wrap lesson is precisely that a line unit over 78-column
prose measures the wrapper, not the text.

Under a sentence unit — which is how review 6 read it ("the correct reading
with its marker sits at :1476") and how I sort it below — :1476 is box 2 and
box 4 holds 0. Under a line unit it is box 4's shape and box 4 holds 1. The
figure the packet publishes is only reproducible once the unit is stated.
Separately, "**is now** …" is present tense about a recommendation the packet
withdrew, and a reader who stops at the em-dash carries away the withdrawn
reading; the marker rescues it, but only for a reader who finishes the
sentence.

**Repair.** State the unit in `review6.sweep_after_repair.predicate` (I
recommend: "a marker anywhere in the same sentence, hard wrap disregarded"),
and reword :1475 from "and is now" to "and was then" with the same marker
kept. Neither changes a count under the sentence unit.

### Not findings — checked and cleared

- **Q3's register limb carries a clause the packet's Q-table does not**
  ("plus an unseparated text component", the G9 repair). The packet states it
  at :1351 ("plus a text component this packet has not …"), and the packet's
  own figure is already a lower bound ("at least 409 × 32 = **13,088**"), so
  the two do not disagree.
- **Q4's register limb pairs 57.72% and 25.70% where the packet's Q4 prose
  gives 25.55%.** These name different objects — the first rendered Unknown of
  *any* kind (a disclosure block, 25.55%) versus the first Unknown *tuple*
  (the class-level roster-identity claim, 25.70%). Both are in the
  Measurements table at :242–243 and both in slice 3 at :906; the register's
  pair matches the two objects Q4 *recommends surfacing*. That is G5's
  disposition working, not a drift.
- **Bare-basename code spans** (`polaris.ts`, `staleness.ts`, `…-4-RAW.md`,
  etc.) do not resolve as paths in isolation. Each is introduced by its full
  path earlier in the packet; this is the corpus convention and prior reviews
  accepted it. 58 path-shaped code spans swept; every distinct full path
  resolves on disk [Observed].
- **`butlers` in backticks.** The only backticked spans containing "butler"
  are `openspec/changes/polaris-project-wide-butlers-model/` and its
  `specs/…/spec.md` — Syzygy repository paths, not Butlers repository paths.
  CG-1b is satisfied; `check_governance.py` returns `0 FAIL`.

## L1–L6 verification against the current bytes

Denominator 6. Each row re-derives what the finding rests on rather than
reading the packet's own disposition (verification rule 4).

| L | Severity (raw) | Verdict at `cfcb745` | Evidence re-derived this session |
|---|---|---|---|
| **L1** | blocking | **REPAIRED** | Packet :1461 (F4 row) now carries the marker in line: "…(the asymmetry as stated here was withdrawn after review 2, finding G1 — RFC2-10 supplies a disclosure remedy at lines 220–222 and arm (b) is not called unlawful for freshness; Q2 now states three arms, not two; **this row stood unmarked until review 6, L1**)". Record `review1.dispositions.F4` (:661) carries "[superseded 2026-09-15: … this entry stood unmarked until review 6, L1]". The G1 row (:1528) now counts "**seven sites in all**" and names the two new ones. The H1 row (:1588) carries the fourth box, its former occupancy (two) and its present occupancy, and the per-box counts. `review5.sweep_after_repair.result` (:914) is marked superseded **on its line** with the withdrawn text kept, and the review-5 section's closing sweep sentence says the same. The record's `review6.sweep_after_repair` publishes predicate, denominator and result. **I re-ran the sweep independently** (below): 45 hits over 3,051 / 3,054, boxes **6 / 13 / 26 / 0** — reproducing the packet's published sort exactly. See M2 for the one unstated degree of freedom in the rule |
| **L2** | non-blocking | **REPAIRED** | `git -C …/m2wt log --oneline -1` read **read-only** this session: `f2f37dd docs: M2 funnel review 6 CONFIRM WITH EXCEPTIONS retained; L1–L4 applied [syzygy-dov.2]`. Record `m2_collision.head` (:542) = `f2f37dd`, with `head_re_derived_after_review_3_at_f2f37dd` and `head_re_confirmed_after_review_6` on the same line; `head_note` (:543) is past tense and keeps `da1497b` with its history; `shared_surface_unchanged_at_f2f37dd: true` beside `shared_surface_unchanged_at_da1497b_superseded_key` (:562); `structural_collision_confirmed_by` (:563) dates both reads and the 2026-09-15 re-confirmation. `review1.dispositions.F7` carries "[superseded: … `f2f37dd` after review 3 (H4), confirmed unchanged after review 6 (L2)]" |
| **L3** | non-blocking | **REPAIRED** | The M2 worktree's `docs/reviews/` holds **6** files matching `R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL*-RAW.md` (listed read-only). The M2 review-6 raw's final line is `Verdict: CONFIRM WITH EXCEPTIONS`. Packet Q7 (:63) reads "six reviews retained, M2 at `f2f37dd` with review 6 CONFIRM WITH EXCEPTIONS; the earlier 'five' corrected after review 6, L3" — count, commit and verdict word all confirmed independently. Q7's premise and recommendation are unmoved |
| **L4** | non-blocking | **REPAIRED** | `…-5-RAW.md`:348 reads exactly `Summary: **7 REPAIRED, 1 PARTIAL, 1 NOT REPAIRED**, over a denominator of 9.` (read this session). Packet J6 row now reads "**CONFIRMED — PARTIAL at `76e897f`, completed after review 5 (K2)**"; the review-5 section states "verified J1–J9 … as 7 REPAIRED, 1 PARTIAL (J6, the funnel-summary handoff line, K2) and 1 NOT REPAIRED (J7, K1) over a denominator of 9 — both complete at this commit … (the counts added after review 6, L4)" |
| **L5** | editorial | **REPAIRED** | `snapshot-and-evaluation-core.md` read line by line: the remedy sentence "A condition genuinely outside the four is disclosed as a fact of the render, never dressed as a freshness state." begins mid-line **220** and ends mid-line **222**; the orthogonality sentence "Freshness is orthogonal to the three labels and the tier registry; it never substitutes for either." begins on **222** and ends on **223**. `freshness_mint_hazard` (:282) now reads "…at lines 220-222, supplies the remedy … and **lines 222-223 add** (the single line 223 named here until review 6, L5) that freshness never substitutes…". Both extents now match the source exactly |
| **L6** | editorial | **REPAIRED** (for the two fields it named; see **M1**) | Computed over the capture: `class="unknown-disclosure"` first at 378,604, its element's `<` at **378,599**; the first Unknown-labelled `<span class="claim-tuple"` at **380,767**, its class attribute at 380,773, claim id `claim:class:roster-identity`. Record :169 = 378,599 with an `offset_anchor` naming the convention and keeping 378,604; :174 = 380,767 with the matching `offset_anchor`. Depths recomputed: **25.55%** and **25.70%** — unchanged at two decimals, as the record says. The one remaining offset on the other anchor is M1 |

**6 REPAIRED, 0 PARTIAL, 0 NOT REPAIRED over a denominator of 6.**

## The six-literal sweep, re-derived and re-sorted from scratch

Predicate, run this session: Python `str.count` of exactly `supplies no`,
`no absence`, `not lawfully available`, `unlawful`, `no remedy`,
`supplies none` (case-sensitive, no word boundaries) over the three files at
`cfcb745`; then every hit located by line and sorted by hand into exactly one
of the packet's four boxes. I did not read the packet's sort before producing
mine.

Totals [Observed]: packet **27**, record **14**, register **4** — **45** over
**3,051** lines by `wc -l` / **3,054** counting each file's trailing line.
Both figures match the packet's review-6 section and `review6.sweep_after_repair`
exactly.

| Box | Rule | My count | Packet's |
|---|---|---|---|
| (1) | current lawful-arms language | **6** | 6 |
| (2) | an in-place withdrawal marker | **13** | 13 |
| (3) | review-history text framed as superseded (the sweep's own literal lists included) | **26** | 26 |
| (4) | review-history text stating the withdrawn proposition in the present tense with no marker | **0** | 0 |

My box (1), enumerated so it can be checked: packet :58 ×3 ("none is
unlawful"; "four rows and no absence row" ×2), packet :993 ×1 ("**no absence
row**"), register :222 ×2 ("none is unlawful"; "four rows and no absence row").
Box (2): packet :1461 ×3, :1476 ×1, :1528 ×3, :1545 ×1, :1552 ×1; record :661
×1, :674 ×1; register :222 ×2. Box (3): packet :631 ×2, :1550 ×1, :1588 ×9,
:1589 ×1, :1649 ×1; record :282 ×3, :741 ×3, :791 ×2, :792 ×1, :818 ×2, :935
×1.

**Box (4) test, stated as a predicate rather than a conclusion** (verification
rule 9): I took every one of the 45 hits and asked whether it asserts, in the
present tense and as the packet's own voice, that RFC2-10 supplies no absence
remedy or that arm (b) is not lawfully available for the freshness field, with
no withdrawal marker attached. **Zero hits qualify.** The nearest is packet
:1476, whose marker is in the same sentence three wrapped lines later — the
subject of **M2**, and box (2) under the sentence unit review 6 used.

The one class of hit worth naming for a later pass: 26 of the 45 are the
*sweep's own literal lists* and the review-history quotes of the withdrawn
wording. This population grows every review (25 at `b34fca7`, 41 at
`f35a25f`, 42 at `76e897f`, 45 here), which the H1 row already discloses. The
figure is honest; it is simply no longer a measure of live risk.

## Regression spot-check — F through K, and the cited line numbers

I did not re-litigate accepted repairs. I checked that the bytes prior reviews
confirmed are still those bytes.

**Every record line number the packet cites resolves to the field the packet
names** [Observed, each read with `sed -n 'Np'` this session]:

| Cited | Resolves to |
|---|---|
| :279 | `closed_freshness_vocabulary_authority` — quotes RFC2-10 lines 209–223 to the clause's end, with the J1 extension note (J1) |
| :282 | `freshness_mint_hazard` — prohibition at 212–214, remedy at 220–222, orthogonality at 222–223, the three arms, three withdrawal markers (H1/J3/K3/K6/L5) |
| :674 | `review1.recommended_answers_changed.Q2` — carries the H2 in-place marker |
| :730 | `review2.f_verification_against_review_1` (J2) |
| :741 | `review2.repairs.G1` — names the record as the fifth site (J1) |
| :791, :792 | `review3.re_derived_before_applying.H1` / `.H2` |
| :804, :808 | `review3.repairs.H1` (with the K4 marker) / `.H5` |
| :818 | `review2.sweep_after_repair.predicate` — the three-literal grep |
| :829 | `review4.findings` — J1–J3 blocking, J4–J6 non-blocking, J7–J9 editorial |
| :837, :848 | `review4.re_derived_before_applying.J7` / `review4.repairs.J7` — both marked superseded on their lines (K1) |
| :856 | `review5` block opens |
| :895 | `review5.re_derived_before_applying.K1` — 25 / 2,479 / 2,482 at `b34fca7` |
| :914 | `review5.sweep_after_repair.result` — marked superseded on its line (L1) |

Source and clause citations re-read at `cfcb745` [Observed]:

- `polaris.ts` **306–307** are exactly `const tier = claim.epistemic.tier ?? 'unstated';` and `const freshness = claim.epistemic.freshness ?? 'unstated';`.
- `claimStatesBlock` spans **346–361**; the freshness group — the named M2 collision — is **line 357** (`${group('states.freshness', [...])}`). F8's correction holds.
- `polaris.ts` **506–510** is the reading/component-guides block M2 slice 6 touches; **1307** is `.claim-tuple { … color: var(--muted); … }`; **1328–1329** are `.proposal` and `.proposal-label`, both on `var(--unknown)`.
- `polaris-copy.ts` **34–51** is 18 lines composing exactly 3 label + 1 tier group label + 7 tier + 1 freshness group label + 4 freshness + 1 challenge group label + 1 challenge — the F14 composition, confirmed by count.
- `staleness.ts` **98–104** is the `no-bound-declared` arm returning `{state,label,reason,claimClass}` with **no** `freshness` field — the mint hazard as described.
- `surface-routes.test.ts`:82 is `const denominator = pages.length;` — the packet's central Q1 claim, confirmed at source.
- POC-REQ-060's Case and Falsifier quoted verbatim against the spec: "a checker enumerates every epistemic encoding on all three surfaces — the denominator is that population", "or a surface styling epistemic state ad hoc". Both exact.
- RFC2-10 at `snapshot-and-evaluation-core.md` 209–223 and RFC2-25's sibling-state sentence at `rendering-vocabularies.md`:169–170 read verbatim; the packet's quotes carry the source's own emphasis and add none (F12/G3 hold).

Capture-derived figures, all recomputed independently this session and all
exact [Observed]: 713 claim tuples; `data-epistemic-label` Observed **702** /
Unknown **11**; `data-epistemic-tier` `report-fact` **702** / `unstated`
**11**; `data-epistemic-freshness` `fresh` **713**; `data-challenge-state`
`unchallenged` **713**; `class="unknown-disclosure"` **22**; declared badge
spans **2**, at **99.96%** and **99.97%** depth, legend at **99.95%** (char
1,481,009); first-reading boundary at char **281,986** = **19.03%**;
`class="proposal-label"` **1** at **56.29%**, `class="proposal"` **0**,
`class="unavailable-notice"` **0**; `dismissed-by-decision`,
`unadopted-draft`, `editorial-draft`, `challenge-pending` **0 / 0 / 0 / 0**
over the whole 1,481,819-character page.

ΔE76 recomputed from `design-tokens.ts` (`--ink` #dfe9e7, `--muted` #8ca3a4,
`--cyan` #78e1d1, `--amber` #f1b85b, `--unknown` #f3c56f), sRGB → D65 XYZ →
CIELAB, all ten foreground pairs [Observed]: `amber|unknown` **7.8462**
(smallest), `ink|muted` **26.7371** (next), then 31.78, 32.00, 50.99, 56.47,
57.82, 61.73, 64.85, 71.97. Q6's "7.85", "26.74 to two decimals, 26.7371
computed" and "≥ 26.7" are exact, and the population exclusion (ground tokens
out, named) is stated where the figure is used.

Byte arithmetic recomputed: 1,484,487 − 1,400,000 = **84,487** over the M1
target; 2,097,152 − 1,484,487 = **612,665** under the ceiling. Both exact.

**Nothing previously accepted regressed.** J1–J9 specifically: J1 (record
:279 runs to the clause's end at 223) holds; J2 (:730 reads 10 REPAIRED /
denominator 14) holds; J3 (:282 carries the packet's own (b-i)/(b-ii)/(b-iii),
with the withdrawn enumeration marked) holds; J4 (1,052 / 69.87% and 1,087 /
67.62%, both stated with the reason for the wider sweep, in Q1, the population
prose, the summary and the register) holds; J5 (the P-70 row's Q2 limb carries
the machine-channel tier-parity disclosure, 12 of 1,149, all Unknown) holds;
J6 now reads PARTIAL-then-completed (L4); J7's row quotes its own false text
and carries the `b34fca7` stamp under both conventions (K1); J8's baseline
bracket still enumerates no commit count and points at `git log`; J9's Gate 3
bracket is still split Observed-five / Inferred-scope.

## Q1–Q7 — packet against the P-70 row, clause by clause

| Q | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| **Q1** | Yes. 735 = 713 + 22 recomputed; 0 declared classes in the body; the two declared spans are both legend-internal. The 713/22 split is stated in both directions and does not soften the finding | Yes — a conformance ruling on a signed requirement is the owner's, and the packet says so | Yes. POC-REQ-060's Case fixes the population; `denominator = pages.length` is at source; verification rule 4 names the defect. "No spec text changes either way" is argued at Gate 5 and holds | **Yes.** Both carry 735 / 713 / 22, both denominators (1,052 · 69.87%; 1,087 · 67.62%), the checker path, the recommended arm and the "no spec text" clause |
| **Q2** | Yes, and it is the packet's most careful passage. Both mint sites quoted at source; the two governing clauses quoted at defined clauses; the PWB-REQ-007 tension put to the owner **unresolved** | Yes — a contract reading no agent may settle (VIS-4), explicitly left open | Yes. (b) for tier; three arms for freshness with **none called unlawful**; (b-iii) recommended and labelled `[Inferred]`; (b-i) and (b-ii) named live and lawful. No trade-off smoothed | **Yes**, clause for clause: tier arm (b) + six rows + one absence treatment "never seven"; the three freshness arms in the same order and substance; "none is unlawful"; (b-iii) `[Inferred]`; the PWB-REQ-007 tension unresolved; four rows / no absence row either way; closure over served output; the PWB-REQ-020 machine-channel disclosure (J5) |
| **Q3** | Yes. 409 of 713 and 13,088 = 409 × 32 both stated as a lower bound, sourced to the lane B estimate record by branch | Yes — it spends or preserves a ruling (P-68) the owner has not made | Yes. Arm (a) preserves the queued saving; the cost is named as a discipline (expand scopes before counting; assert the denominator equals the tuple count) | **Yes.** The register adds "plus an unseparated text component" (G9); the packet states the same at :1351 and its Q-table figure is already "at least". No disagreement |
| **Q4** | Yes. 126 tuples all Observed over 19.03%; 0 disclosure blocks in the band; 25.55% and 25.70% and 57.72% all recomputed | Yes — what the owner's first stop opens with is a design ruling | Yes, and the alternative arm is stated as coherent rather than dismissed. CC-VIZ-3 applied with the by-analogy caveat on the `trust-and-evidence.md`:101 citation (G8) | **Yes.** The register's "57.72% and 25.70%" names the two objects the recommendation surfaces (G5); the packet's 25.55% names the first Unknown of *any* kind, and both sit in the Measurements table at :242–243 |
| **Q5** | Yes. Twelve prose-only states, none encoded; 15 glossary sentences, 9 unreachable — the glossary read at source | Yes — how far the declared table reaches is the owner's | Yes. Generation in both directions is tied to POC-REQ-061's falsifier and its mirror; the three riders (six tier rows + absence treatment; four freshness rows + a guard over **rendered output**; unreachable values marked never deleted, rebasing onto M2's markers) are all carried | **Yes**, all four clauses present and in the same terms, including "P-69's Q5 shape, so slice 5 rebases onto M2's markers" |
| **Q6** | Yes. One rendered proposal label in `var(--unknown)`; five rules on one token for four meanings, two rendering zero times — all recounted. The "what this question does not ask" paragraph quotes RFC2-25's closed three verbatim and shows 0 renders of each | Yes — a new declared encoding family is a design ruling | Yes. VIS-7 and RFC7-34 anchored; the family is declared a **fourth table** that mints no member of any closed vocabulary; the ΔE floor is stated **with its population** and the full matrix is in the record; the one-token alternative is named lawful | **Yes.** "a fourth declared encoding table that mints no fourth epistemic label, seventh tier or fourth sibling surface state, at ΔE76 ≥ 26.7 from `--unknown` over the five foreground tokens (today's smallest pair is `--amber`/`--unknown` at 7.85) and AA contrast on both grounds, rather than keep one token and legend the reuse" — every limb in the packet |
| **Q7** | Yes. The collision is named at file and line (`polaris.ts`:357, `polaris-copy.ts` freshness sentences) and verified at source; the M2 head, review count and verdict word all confirmed independently | Yes — sequencing against two queued decisions, put as a choice because both arms are lawful | Yes, and it does **not** smooth: the packet states at :1305–1315 that M2's Q7 (`stale`) and this packet's Q2 ((b-iii)) "are mutually exclusive for the same claims" and "granting both as recommended is not available" (H3) | **Yes**, including the H3 sentence in the register's own bold: "not two compatible rulings on the same claims: granting both as recommended is not available, and which one the owner grants is not decided here" |

Also checked on the register row: the review-6 citation ("verdict copied
exactly: REVISE; one blocking, three non-blocking, two editorial as the raw
counts them") matches the raw's own summary line; the P-70 note's stamp reads
"Updated 2026-09-14, and again 2026-09-15 for reviews 4, 5 and 6" (K5,
extended for L-series); the "Default if unanswered: nothing" clause is present
and enumerates what stays broken. No arm on any question is called unlawful
that is not; VIS-4 is respected throughout — nothing is labelled accepted,
adopted or ruled on the owner's behalf.

## Questionnaire invariant

- Problem scope and recommendation hold against the project's shape and
  engineering bar; Gate 6 carries denominators, rule-6 mutants per guard
  branch, parity per tuple, retained evidence and independent review.
- No owner trade-off smoothed: Q2's three arms and Q7's H3 exclusivity are the
  two places it could have happened, and neither does.
- No lawful arm called unlawful — the sweep above is the check, and box (4)
  holds 0.
- Substantive claims carry `[Observed]` / `[Inferred]`; Q2's recommendation is
  explicitly `[Inferred]`.
- Contract claims are quoted at defined clauses (RFC2-10, RFC2-25, POC-REQ-060,
  PWB-REQ-007, VIS-7, CC-VIZ-1, CC-VIZ-3, RFC7-34), each verified verbatim.
- Zero/all claims carry a predicate and a denominator, each run this session:
  the four CSS probes, the four closed-vocabulary literals, the box-(4) sort,
  the four-page population, the tuple counts.
- Digests computed, never transcribed.
- No manifest argument or truncated signed digest is quoted; no Butlers
  repository path appears in backticks; `check_governance.py` ends `0 FAIL`.

## Summary

Findings by severity: **0 blocking**, **0 non-blocking**, **2 editorial**
(M1, M2). Two findings over two artifacts. L1–L6: **6 REPAIRED over 6**.
The 45/3,051 sweep and its 6/13/26/0 sort reproduce exactly from a blind
re-derivation. No recommended answer is touched by either finding.

Verdict: CONFIRM WITH EXCEPTIONS
