# R-POLARIS-M3-HONEST-ENCODING-FUNNEL-3-RAW

Independent fresh-context review **3** of the M3 feature-request funnel packet
(bead `syzygy-dov.3`), its evidence record, and the P-70 note and row in the
pending-owner-decisions register. Read-only session: no file in any repository
or worktree was modified, no state-changing git command was run, no `bd` write,
no daemon, no network, no Butlers checkout read. The one file written is this
raw.

Review 1 is retained at `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md`
(F1-F14, verdict word copied exactly: **REVISE**). Review 2 is retained at
`docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-2-RAW.md` (G1-G9, verdict
word copied exactly: **REVISE**). This review binds the bytes named below and
no others (verification rule 10).

## Header - commit and reviewed bytes

Worktree: `.../scratchpad/m3wt`, branch `agent/syzygy-dov.3`, HEAD
**`b34fca7ec5388b0b363a69f8567221896efc3244`**
(`b34fca7 docs: M3 funnel review 2 retained and G1-G9 repaired; Q2 freshness arm revised [syzygy-dov.3]`,
2026-09-14 09:04:59 +0800). Working tree clean. `git diff --stat a9f671e..b34fca7`
is five files, 3,295 insertions, 0 deletions - all of them this packet's own
artifacts; no source file cited by line in the packet moved between the stated
baseline and HEAD [Observed].

Digests computed this session with `wc -c` and `sha256sum`, never transcribed
(verification rule 3):

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md` | 115,201 | `fa8e4e71d8f0d73ede9157e776ecd11fb7ec1d22f8a7783e44b629e943411eb6` |
| `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json` | 36,743 | `cb9a8d97d24f74022d61e5c2fa168a5f12401711b8f1fd1b18332fed7efac6eb` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 31,054 | `19c567a0a6d2c3c7b39e32e5aaad8eaa98ca75c092585c4f9d5eeb98d30d268a` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md` (review 1, reference) | 31,503 | `1eca5fbac6fe95266ac4968f5b55ebf89e6e63544441383c545fb89b9140bc1f` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-2-RAW.md` (review 2, reference) | 48,381 | `a04b20517539e971c1e192015329dd39a2e2f536b52c06fffdce473177397012` |

Reference bytes read read-only outside this worktree:

| File | Bytes | sha256 |
|---|---|---|
| retained lane A after/tailnet capture, `.../scratchpad/m1/measure/after/polaris-tailnet.html` | 1,484,487 | `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` |
| M2 packet, `.../scratchpad/m2wt/docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` at `f2f37dd` | 93,086 | `29352c4b324e8a021c77f5feb89f7f287d05ec0fbde3273940a2af2e1ba3d03a` |

The capture digest is identical to the one the packet and the evidence record
name, recomputed here before any measurement [Observed]. The two review raws'
byte sizes and digests are identical to the ones the packet states at :1356-1357
and :1417-1418 [Observed]. The three files review 2 records itself as having
read at `573abb0` are identical to the bytes at that commit:
102,085 / `bf526da8...f560cf`, 30,747 / `5370f6cd...3d2ea6f5`,
29,780 / `cac255f5...987d37e7` [Observed: `git show 573abb0:<path>` piped to
`wc -c` and `sha256sum`].

`python3 scripts/check_governance.py` from the worktree root ends
**`32 OK, 20 WARN, 0 FAIL (52 checks) - counts derived, not asserted`**
[Observed: run this session; identical to the record's
`governance_check.baseline_last_line`].

## What re-derived clean

Every load-bearing figure in the packet was re-derived independently this
session from the named bytes, with Python `re` and literal `str.count`, never
shell grep (verification rule 1). All of the following are **exact**:

- Tuple count by three agreeing methods: span-open regex 713, literal split
  713, `class="claim-tuple"` count 713. Distinct claim ids 703 of 713.
- Attribute histograms over the 713 tuples: label Observed 702 / Unknown 11;
  tier `report-fact` 702 / `unstated` 11; freshness `fresh` 713; challenge
  `unchallenged` 713. Two distinct tuple shapes.
- `class="unknown-disclosure"` 22; `class="unavailable-notice"` 0;
  `class="proposal"` 0; `class="proposal-label"` 1.
- Declared badge spans on Polaris: 2 under three predicates (strict, attribute-
  tolerant, class-substring), both inside the legend, at 99.96% and 99.97%
  depth; 0 in the body. Legend opens at character 1,481,009 = 99.95%.
- Served stylesheet, parsed rule by rule (206 rules, `@media` flattened):
  exactly **2** rules name `.claim-tuple` - the base rule
  (`font-family: var(--font-mono); font-size: .78rem; color: var(--muted);
  letter-spacing: .04em;`) and one override changing only `letter-spacing` and
  `font-size`. **1** colour treatment over all 713 tuples. Literal probes
  `claim-tuple[`, `[data-epistemic-label`, `[data-epistemic-tier`,
  `[data-epistemic-freshness`, `[data-challenge-state` each return **0** over
  all 206 selectors. `var(--unknown)` in **5** rules
  (`.epistemic-unknown`, `.unavailable-notice`, `.unknown-disclosure`,
  `.proposal`, `.proposal-label`); `var(--cyan)` in **17**.
- Cross-surface population **1,087** with the packet's stated predicate and its
  named files, whose digests match the record: home 35 body encodings of 37
  badges, trajectory 299 of 301, orrery 18 of 20, Polaris 735 (713 + 22).
  Declared-class total **352**. 735/1,087 = 67.62%. The strict pattern the
  packet's predicate is written in matches only 19 / 2 / 2 on those three
  pages, because their badges carry further attributes; the attribute-tolerant
  form reproduces 37 / 301 / 20 exactly. The figure is right; the *written*
  predicate is one character short of the sweep that produced it (noted, not
  filed - the record's `predicate` field has the same shorthand and no reader
  has been misled by it).
- First reading: boundary at character 281,986 = 19.03%; 126 tuples in the
  region, **0** Unknown, **0** Unknown-disclosure blocks, **14** occurrences of
  the word "Unknown" in the region's visible text. First Unknown-disclosure at
  25.55%, first Unknown tuple (`claim:class:roster-identity`) at 25.70%,
  whole-shape Unknown (`claim:project-shape`) at 57.72%. The 11 Unknown tuples
  are 9 source claims, 1 class aggregate and the whole-shape claim - enumerated,
  not inferred. "No member claim carries an Unknown reason." occurs 8 times.
  `class="proposal-label"` at 56.29%.
- Item and source rows: `data-polaris-item="` 409, bare `data-polaris-item` 417,
  distinct `data-polaris-items` 8; `data-polaris-source="` 278.
- Colour: 10 declared tokens at `design-tokens.ts`:46-55 (confirmed line for
  line), 9 distinct values, 36 pairs. All 36 ΔE76 recomputed (CIE76 over CIE Lab,
  D65, sRGB, D50-free): rank 1 `--panel`/`--void` 3.9753, 2 `--panel`/
  `--panel-raised` 4.8231, 3 `--amber`/`--unknown` 7.8462, 4 `--panel-raised`/
  `--void` 8.7759, 5 `--line`/`--panel-raised` 14.9639, 6 `--line`/`--panel`
  19.5580, 7 `--line`/`--void` 23.2692, 8 `--ink`/`--muted` **26.737100596**.
  **Seven** pairs strictly below the `--ink`/`--muted` floor. Over the five
  foreground tokens (10 pairs) 7.85 is smallest and 26.74 next. Contrast
  `--amber`:`--unknown` 1.109; `--cyan`:`--unknown` 1.035 with ΔE76 64.85;
  `--unknown` on `--void`/`--panel` 11.93 / 11.21; `--muted` 7.23 / 6.79.
- Byte arithmetic: 1,484,487 - 1,400,000 = 84,487 over; 2,097,152 - 1,484,487 =
  612,665 under; 702x19 + 11x18 + 702x4 + 11x2 = **16,366**; 409 x 32 = **13,088**.
- Lane B, read read-only from `origin/agent/syzygy-dov.17` at `4090f98`:
  `hoistedPerField` container mode gives `data-epistemic-label` **409**,
  `data-challenge-state` **713**, `data-evaluation-id` **713**;
  `netSavingBytesTailnet` **188,902**; `textBytesRemoved` **25,397**, not broken
  down per field. The inheritance sentence the packet quotes is verbatim in
  `proposed/spec.md.patch`. 713 - 409 = 304; 409/713 = 57.4%.
- `git diff f4589e2 a9f671e -- apps packages` touches 31 files, none of them a
  home, Trajectory, Orrery, `page-shell.ts` or `design-tokens.ts` source - the
  packet's caveat for the three pre-lane-A captures holds [Observed].
- Every source line citation in the packet resolves exactly: `polaris.ts`
  306/307, 346-361 with the tier group at 356 and the freshness group at 357,
  536, 555, 1307, 1328-1329; `polaris-copy.ts` 34-51 (15 state sentences plus
  three interleaved group labels: 3 label, 7 tier, 4 freshness, 1 challenge) and
  46-49 (the four freshness sentences); `design-tokens.ts` 16-29 and 46-55;
  `surface-routes.test.ts` 64-101 with `const denominator = pages.length` at 82;
  `cross-cutting.test.ts` 47-64; `walkthrough-preflight.ts` 203-226;
  `polaris-first-reading.test.ts` 88 and 96-99; `epistemic.ts` 23-30 (the six
  tiers); `staleness.ts` 18 and 98-104; `project-shape-model.ts` 376-378 and 377.
- Every code-span path in the packet resolves at HEAD (0 unresolved of the
  qualifying spans). The P-70 row's and note's eight code-span paths all resolve.
  No Butlers path appears in backticks in any of the three artifacts (0 hits over
  `butler.toml`, `MANIFESTO.md`, `about/lay-and-land`, `roster/`, `v1.md`,
  `components.md`). No manifest row or truncated signed digest is quoted; the
  only digests quoted are full 64-hex sha256 of the two retained review raws,
  both correct.
- Every block quote of governed text is verbatim at its stated line. Checked by
  whitespace-normalised substring match against the source file, per segment:
  VIS-2 (`vision.md`:96), VIS-7 (:183), POC-REQ-060 and its scenario
  (spec :927, :948), POC-REQ-061 (:966), PWB-REQ-007 (:439), PWB-REQ-020 (:902),
  PWB-REQ-016 (:864), RFC2-25 (`rendering-vocabularies.md`:153) and its
  three-sibling-state sentence (:169), RFC2-26 (:196), RFC2-10
  (`snapshot-and-evaluation-core.md`:209), RFC7-34
  (`rendering-and-surface.md`:241), CC-VIZ-1 (:48), CC-VIZ-3 (:74),
  `trust-and-evidence.md`:101, and both `warrants` blocks (spec :955-964 and
  :999-1008, with the `[RFC1-26, RFC6-20, RFC9-3, RFC9-46, RFC9-48]` block at
  :920 belonging to the preceding Orrery requirement whose scenario ends at 914).
  Emphasis in every quote matches the source: RFC7-34 now carries exactly one
  bold span (`without colour, position, or layout`), matching :241-242 - G3 is
  repaired; RFC2-10 carries exactly the source's two bold spans; PWB-REQ-007,
  PWB-REQ-016, VIS-7, CC-VIZ-1, POC-REQ-061 and VIS-2 carry no added bold.

Not re-derived: nothing load-bearing. Two figures rest on records I read but
did not regenerate - lane B's `netSavingBytes` (read from the branch's estimate
JSON, labelled `[Inferred]` there and cited as such) and the 2026-09-13
dossier's superseded 1,085, which the packet correctly declines to call a
correction.

## Findings

### H1 - blocking - `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:282 (`vocabulary_versus_rendered.freshness_mint_hazard`) - the sentence G1 blocked on is still standing, in the artifact the packet says it was removed from

**Defect.** The evidence record's `freshness_mint_hazard` field ends:

> "RFC2-10 forbids the mint in terms and supplies no absence marker, so arm (b)
> of Q2 is not available for freshness"

That is the exact false reading review 2 blocked on. RFC2-10 does supply an
absence route, in its own terms, eleven lines below the line the field cites:
"A condition genuinely outside the four is disclosed as a fact of the render,
never dressed as a freshness state" (`snapshot-and-evaluation-core.md`:220-222,
read in full this session). The sentence therefore (a) states a false thing
about an accepted contract clause and (b) forecloses an arm the packet itself
now recommends - (b-iii) - as unavailable. Both halves of the questionnaire
invariant it violates are explicit: contract claims are anchored to a defined
clause and quoted, and no lawful arm is called unlawful.

It is not an isolated stale string. The packet's own G1 disposition row
(:1437) says the phrase "is withdrawn from all four packet sites and the
register row", and the record's own `review2.repairs.G1` (:723) repeats it. Both
statements are true of the packet and the register - I swept all three artifacts
for `supplies no`, `no absence`, `not lawfully available`, `unlawful`,
`no remedy`, `supplies none` and confirmed the packet's only survivals are the
two passages that quote the withdrawn wording *as withdrawn* (:584, :1454) and
one historical disposition row (:1379), and the register carries only the
explicit withdrawal note. The record is the one place the claim still stands as
an assertion, and the two repair rows assert otherwise. The record is not an
internal scratch file: review 2 read it as one of its four reviewed artifacts,
and the P-70 row names it to the owner by path as the packet's evidence.

The companion field two lines above, `closed_freshness_vocabulary_authority`,
quotes RFC2-10 truncated at exactly the same place ("...force-fit a freshness
value it does not carry.") with no ellipsis and no remedy - which is how the
false universal survived the repair pass: the record's quote was never extended
the way Gate 2's was.

**Repair.** Rewrite `freshness_mint_hazard`'s final clause to state RFC2-10's
remedy at :220-222 and the three lawful arms, dropping "supplies no absence
marker" and "arm (b) of Q2 is not available for freshness"; extend
`closed_freshness_vocabulary_authority`'s quote through the remedy sentence or
mark its truncation. Then correct the two disposition rows that claim the
withdrawal was complete (packet :1437 and record :723) so they name the record
as a fifth site, or the same defect recurs the next time a repair pass trusts
them.

### H2 - non-blocking - `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:674 (`review1.recommended_answers_changed.Q2`) - a superseded recommendation recorded as the current one

**Defect.** The field reads: `"Q2": "was \"Arm (b).\"; now \"Arm (b) for the
tier field; arm (b) is not lawfully available for the freshness field, and the
owner should see why\" - the tier ruling unchanged, the freshness half new
(F4)"`. The "now" wording is the one withdrawn after review 2. The packet's
parallel passage (:1393-1404) marks the withdrawal *at the stale sentence*, in
place - "(that freshness wording was itself withdrawn after review 2, finding
G1; see the review-2 section)" - which is the right shape. The record has no
such marker, so a reader who opens the evidence file for the Q2 history is told
the withdrawn wording is current.

**Repair.** Append the same in-place marker to the field. Do not delete the
superseded wording - the packet's own handling is the model.

### H3 - non-blocking - packet :52, :57, :1237-1244 against `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`:205 - the one instruction G1's repair produced does not reach the register

**Defect.** The packet tells the owner three times that P-69 and P-70 turn on
one accepted clause and must be ruled as one: Q2 ("**M2's Q3, Q5 and Q7 rest on
this same RFC2-10 sentence**... so P-69 and P-70 must be read together"), Q7
("P-69 and P-70 should be ruled together, not independently"), and the collision
section's cross-packet note ("the owner is reading one accepted clause across two
packets, not answering two independent questions"). Review 2's G1 disposition
records exactly this as part of the repair.

The P-70 register row carries none of it. Sweeping the row and the note for
`together`, `ruled together` and `read together` returns **0** in both
[Observed: literal `str.count`, denominator the row and the 21-line note]. The
row names P-69 twice, once as the home of arm (b-i) and once in Q7's sequence,
and never says the two rows are one reading. The register is the artifact the
owner works from; a coupling stated only in the packet is a coupling the queue
does not enforce. This is the project's own recorded failure mode - a page that
restates state it does not own goes stale silently, and here the register omits
state the packet does own.

**Repair.** One clause in the P-70 row, in Q2 or Q7: that P-69's Q3/Q5/Q7 and
P-70's Q2 are one reading of RFC2-10 and should be ruled together. A matching
clause in the P-69 row when M2 lands.

### H4 - non-blocking - packet :1192, :1382, :1440 and record `review2.repairs.G4` - M2's head is stale a fourth time

**Defect.** The collision section names M2's head once, as `da1497b`, "re-read
this session". `origin/agent/syzygy-dov.2` is now **`f2f37dd`**
(`docs: M2 funnel review 6 CONFIRM WITH EXCEPTIONS retained; L1-L4 applied`),
one commit past it; `git log --oneline da1497b..HEAD` in the M2 worktree is that
single commit [Observed]. This is the fourth consecutive stale reading of the
same citation (`ec30494`, `e0ecdc8`, `68123fc`, `1befd6f`, `da1497b`), and the
packet already diagnoses the cause correctly at :1194-1196.

The substance survives, re-verified at `f2f37dd` this session: M2 still has six
slices (`### Slice 1`...`### Slice 6`, enumerated); slice 6's two files are still
`polaris-reading.ts` line 44 and `polaris.ts` lines 506-510, neither of which any
M3 slice touches; Q5 still reads "**Mark, do not delete.**" with the
"reason ... and a route" wording M3 relies on; Q7 still recommends
"**`stale`, with primary reason `no-currency-bound-declared` kept distinct**"
and still carries the RFC2-10 counter-argument M3 quotes. M2's Gate 3 row 1 cites
`polaris-copy.ts` lines 45-49 where M3 cites 46-49; both are correct for their own
scope (45 is the `states.freshness` group label, 46-49 the four sentences).

**Repair.** Stop naming a head. The packet's own remedy - cite by register row
and by the two shared files - is already applied everywhere except this one
sentence; finish it, or date-stamp the reading rather than presenting it as
current.

### H5 - non-blocking - packet :1432-1433 and record `review2.f_verification_against_review_1` - a transcribed total that its own parenthetical contradicts

**Defect.** The packet states review 2's F-verification as "**9 REPAIRED, 5
PARTIAL** (F4, F6, F7, F12 partial; **0 NOT REPAIRED**)", and the record's
`f_verification_against_review_1` is `{"REPAIRED": 9, "PARTIAL": ["F4","F6","F7","F12"], "NOT_REPAIRED": 0}`.
Both give a REPAIRED count and a PARTIAL count that do not correspond to the
four partials they name: 9 + 4 = 13 over a population of 14.

Counted from review 2's own verification table (`...-2-RAW.md`:461-474, one row
per finding, denominator 14): F1 REPAIRED, F2 REPAIRED, F3 REPAIRED, F4 PARTIAL,
F5 REPAIRED, F6 PARTIAL, F7 PARTIAL, F8 REPAIRED, F9 REPAIRED, F10 REPAIRED, F11
REPAIRED, F12 PARTIAL, F13 REPAIRED, F14 REPAIRED = **10 REPAIRED, 4 PARTIAL,
0 NOT REPAIRED**. The raw's own totals line at :476 says "9 REPAIRED, 5 PARTIAL"
and its summary at :546 says "Eleven of review 1's fourteen findings are repaired
cleanly" - three figures in one document, no two agreeing, and the packet copied
the middle one. Verification rule 3: totals are computed, not transcribed; the
packet had the table and did not count it.

The raw itself may not be edited (CC-REV-6, and rule 10 binds its bytes).

**Repair.** State 10 REPAIRED / 4 PARTIAL in both the packet and the record,
computed from the raw's table with the denominator named, and note in one clause
that the raw's own totals line and summary sentence disagree with its table and
with each other.

### H6 - non-blocking - packet :52 (Q2's tier limb) and Gate 2 :488-499 - arm (b)'s justification is true of the human channel only, and the machine channel's absence is not disclosed

**Defect.** Q2 recommends arm (b) for the tier field partly because "it keeps
PWB-REQ-007's 'carry the closed label, tier ... that govern it' satisfied with a
present field". On the retained capture the field is present in the human channel
only.

Measured this session. Predicate: every `<span class="claim-tuple">` carrying
`data-epistemic-label="Unknown"` on the retained tailnet capture, matched by
`data-claim-id` against every object in the retained machine answer
(`.../m1/measure/after/api-poc.json`) carrying both `claimId` and `epistemic` -
1,149 such objects over 1,148 distinct ids. Result: **11 of 713** human tuples
are Unknown; **11 of 11** are Unknown in the machine answer; and **11 of 11**
carry no `tier` key there at all - their `epistemic` objects have exactly
`['freshness','label','reasons']`. Machine-side tier histogram over all 1,149:
`report-fact` 1,137, absent 12. The twelfth machine Unknown
(`claim:fact:count:roster-identity`) renders no tuple on Polaris; the human set
is a strict subset of the machine set, so no human-only id exists [Observed].
The string `unstated` occurs **0** times in the machine answer.

So the human page renders `data-epistemic-tier="unstated"` for exactly the
claims whose machine tuple has no tier, and PWB-REQ-007's Observable is "human
and machine views expose identical complete tuples". Gate 2's PWB-REQ-020
paragraph is correct that *M3* adds no fact to either channel; what is missing is
that the divergence Q2's arm (b) would ratify is already live and unmeasured, and
that arm (b)'s stated justification holds on one side of the parity only. This
also cuts the other way and strengthens Q2: it is a second, independent reason
the owner is being asked a real question rather than shown a formality.

**Repair.** State the machine-side absence in Q2 with this predicate and
denominator, and make arm (b) explicit that the absence marker must land in both
channels - or that the parity sweep names it as a declared, legended exception.
A one-clause addition to the Gate 2 PWB-REQ-020 paragraph, and a line in slice 1
or slice 2's oracle.

### H7 - non-blocking - packet :819-826 (slice 2) with :1491-1495 (handoff) - the negative sweep has a live positive that the recommended sequence leaves in place

**Defect.** Slice 2's design adds a negative sweep: "the sweep therefore also
asserts that **no element carries a colour drawn from the epistemic token set
outside the enumerated families**", with mutant (d) confirming it fails when such
an element appears. The recommended handoff says to run slices 1, 2 and 4
"immediately", and deliberately holds slices 5 and 6 behind M2's slice 1.

On the retained capture one such element already exists: `class="proposal-label"`
renders **once**, at 56.29% depth, and its served rule is
`.proposal-label { ...; color: var(--unknown); }` (`polaris.ts`:1329, confirmed
in the parsed stylesheet) [Observed: literal `str.count` = 1, denominator the
1,481,819-character capture; the rule read from the one served `<style>` block].
`var(--unknown)` is the declared Unknown encoding's own colour - this is exactly
what Q6 and slice 6 exist to repair, and slice 6 is the last thing sequenced.

So slice 2, run as recommended, is red on the day it lands, against an element
whose repair the same packet defers. The packet never says so. This is not a
false claim - it is an omission in a design sketch, and it is the kind that costs
an implementer a day and then gets "fixed" by weakening the assertion.

**Repair.** Name `.proposal-label` in slice 2 as its one known live positive,
with the count and the depth, and say how it is handled until slice 6 - either a
declared, dated exception carrying the element and the reason, or slice 6's token
change pulled forward for that one rule (it touches neither of M2's two files and
needs no act, so it can run with slices 1-4 even though the rest of slice 6 waits).

### H8 - editorial - packet :21-23 - the baseline sentence is false at HEAD

**Defect.** "Baseline: Syzygy `a9f671e` (main; the worktree is `agent/syzygy-dov.3`
at the same commit ...)". The worktree is two commits ahead (`573abb0`, then
`b34fca7`). Harmless in substance - `git diff --stat a9f671e..b34fca7` is five
files, all this packet's own artifacts, so every source line the packet cites is
still at the measured bytes [Observed, and re-verified line by line above] - but
a fresh reader checks the sentence first and finds it wrong.

**Repair.** "the worktree branches from `a9f671e`; the only commits on it are
this packet's own artifacts, so every source citation below is at the baseline
bytes."

### H9 - editorial - packet :1422-1423 and record `review2.verdict_word_copied_exactly` - a composite presented as an exact copy

**Defect.** "Its verdict word, copied exactly: **REVISE - one blocking, five
non-blocking, three editorial**." Review 2's verdict line is exactly
`Verdict: REVISE` (`...-2-RAW.md`:567). The string "one blocking, five
non-blocking, three editorial" does not occur in the raw at all [Observed:
literal sweep, 0 hits]; the raw's count sentence at :545 reads "Findings by
severity: **1 blocking** (G1), **5 non-blocking** (G2-G6), **3 editorial**
(G7-G9)". The packet has assembled a phrase from two places and labelled it a
verbatim copy of a verdict word. The record repeats it verbatim as
`verdict_word_copied_exactly`. The packet does the same thing correctly for
review 1 two sections earlier ("Its verdict word, copied exactly: **REVISE**.
Findings by severity as the raw states them: ...").

**Repair.** Split it the way the review-1 section already does.

### H10 - editorial - packet :460-472 and :483-486 - bullets elided from a quoted list with no ellipsis

**Defect.** The PWB-REQ-007 quote runs the requirement sentence, an ellipsis,
then the Case bullet, then the Falsifier bullet - silently dropping Observable,
Oracle and Oracle-independence, with no marker between the two bullets it keeps.
The PWB-REQ-020 quote drops Oracle and Oracle-independence between Observable and
Falsifier the same way. Each retained segment is verbatim [Observed: all 7
segments of the three PWB quotes matched as exact substrings of the spec]; the
elisions are unmarked. The packet marks its other elisions with `...` correctly,
including inside these same quotes, so the omission reads as inconsistency rather
than intent.

**Repair.** An `...` between the elided bullets.

### H11 - editorial - packet :552-566 with :582 - the RFC2-10 quote stops one sentence short of the clause, unmarked, and is called "in full"

**Defect.** The Gate 2 quote is verbatim from the clause's first word through
"never dressed as a freshness state." - source lines 209-222, with the source's
own two bold spans and nothing added. I verified this as whitespace-normalised
string equality; the only difference is the twelve words the packet stops before
[Observed]. **G1's substance is repaired.**

But the clause does not end there. Line 222-223 continues: "Freshness is
orthogonal to the three labels and the tier registry; it never substitutes for
either." There is no ellipsis marking the stop, and :582 describes the quote as
"quoted in full above".

The omitted sentence is not decorative for this packet. Q2's arm (b-ii) is "the
claim is held Unknown and the tuple is not rendered as though it had a freshness
state" - and the clause's own closing sentence says freshness is *orthogonal* to
the labels and never substitutes for either, which is an argument against (b-ii)
supplied by the same clause the arm is drawn from. Review 2's G1 was precisely
that a truncation hid an arm; the repair reproduces the pattern one sentence
further along, this time hiding a counter-argument rather than an arm.

**Repair.** Extend the quote through line 223 and weigh the orthogonality
sentence in (b-ii)'s statement; drop "in full" from :582 if any truncation
remains.

## G1-G9 verification against the current bytes

| G | Severity in review 2 | Verdict | Evidence |
|---|---|---|---|
| G1 | blocking | **PARTIAL** | Gate 2's quote is extended and verbatim through :222 with no added emphasis (string-equality check). "Supplies no absence marker at all" is gone from all four packet sites and the register row. Q2's freshness limb states three arms, each called lawful ("none is unlawful"), puts the PWB-REQ-007 tension (spec :443-446 and its Falsifier) to the owner unresolved ("**This is the owner's question; this packet does not resolve it.**"), labels the recommendation `[Inferred]`, and carries the counter-argument to it. The cross-packet link is in Q2, Q7 and the collision section. **But the evidence record :282 still asserts the withdrawn reading and still calls arm (b) unavailable for freshness - H1** - and the disposition rows in both the packet (:1437) and the record (:723) assert the withdrawal was complete. See also H11 (the extended quote is itself one sentence short) and H3 (the register does not carry the ruling-together instruction) |
| G2 | non-blocking | **REPAIRED** | Slice 5's readiness paragraph (:943-964) now names `aria-describedby` as the preflight's third true requirement and states that `walkthrough-preflight.ts` builds its required-term set from `claim.epistemic.tier`/`.freshness` on the model, never from the render. Confirmed at `walkthrough-preflight.ts`:203-226: the term set is built from `presentedShapeClaims(shape)`, so `unstated` - never a model value - cannot enter it. The guard is correctly restated as `polaris-first-reading.test.ts`:88, which hard-codes `'unstated —'` in its own required-term list (read at that line) |
| G3 | non-blocking | **REPAIRED** | The RFC7-34 quote now carries exactly one bold span, matching `rendering-and-surface.md`:241-242. I re-enumerated the bold spans in all 17 block quotes in the packet and compared each against its source: every one matches. The F12 disposition row (:1387) is corrected and now says RFC7-34's bolding "did not [match] until this repair - review 1 asserted it matched and was wrong" |
| G4 | non-blocking | **REPAIRED at the named head; stale again** | The head is named once, as `da1497b`, and M2 is cited by register row P-69 and the two shared files everywhere else; the marker wording is weakened to "the reason and, where one exists, the route" in slice 5 and collision item 1, matching M2's Q5 text. M2 is now `f2f37dd` - H4. Substance re-verified unchanged at the new head |
| G5 | non-blocking | **REPAIRED** | The P-70 row's Q4 now reads "at 57.72% and 25.70% depth". Both re-derived: whole-shape Unknown tuple 57.72%, class-level roster-identity Unknown tuple 25.70%. The 25.55% figure remains in the packet's Measurements table and Q4 correctly labelled "first rendered Unknown **of any kind** (an Unknown-disclosure block)" - a different object, correctly named |
| G6 | non-blocking | **REPAIRED** | RFC2-26 is quoted at `rendering-vocabularies.md`:196, verbatim with the source's one bold span (:533-542), and Gate 5's slices-5/6 paragraph (:1100-1103) names POC-REQ-061's legend-to-encoding falsifier as the approved OpenSpec mapping that discharges the scheduling bar |
| G7 | non-blocking (editorial) | **REPAIRED** | Both substantive sites (:316 and :1035) read "below the `--ink` ↔ `--muted` floor (26.74 to two decimals, 26.7371 computed)". The third occurrence of the bare "26.74" (:331) is inside a verbatim quotation of review 1's own wrong conclusion and is correctly left alone. The record gains `floor_precision_note`, whose arithmetic (0.0029; the count of 7 unaffected; 26.7371 >= 26.7) I recomputed as exact. `--ink`/`--muted` = 26.737100596500156 |
| G8 | non-blocking (editorial) | **REPAIRED** | Q4 anchors `trust-and-evidence.md`:101, marks the citation "by analogy", and states the clause's actual subject ("its own subject there is a superseded observation record, not an Unknown"). Line 101 read: "visible on the primary surface, not buried in drill-down" |
| G9 | non-blocking (editorial) | **REPAIRED** | The P-70 row's Q3 now reads "costing lane B at least 13,088 attribute bytes plus an unseparated text component". 409 x 32 = 13,088 recomputed; the lane B estimate's `textBytesRemoved` is 25,397 across seven fields and is not broken down per field, so "unseparated" is exact |

## F4 / F6 / F7 / F12 - the four review-2 partials

| F | Verdict | Evidence |
|---|---|---|
| F4 | **PARTIAL** | Its mechanical half was already sound and remains so (lines 306-307 shown together and confirmed at source; the closure assertion over served output with the tuple count as denominator; mutant (e); S9's second limb; collision item 3). Its reasoning half was G1 and is repaired **in the packet and the register**; the false reading survives in the evidence record - H1. The packet's own "F-partial note" (:1447-1451) claims this repair pass "closes all four partials at their named sites"; for F4 that is true of the named sites and false of the record the same repair pass rewrote |
| F6 | **REPAIRED** | The preflight is in slice 5's Gate 3 row as an unchanged-but-binding input, its `claimStrength` requirements are stated and confirmed at 203-226, Gate 6 item 6 re-runs it after slices 3 and 5, mutant (f) removes the strengthen sentence, and G2's correction of the wrong example is applied |
| F7 | **REPAIRED as far as a head hash can be** | Six slices, slice 6's two files untouched, Q5 unchanged, sequence unchanged - all re-confirmed at `f2f37dd`. The citation itself is stale a fourth time (H4), which is the class of defect, not an instance of it |
| F12 | **REPAIRED** | Re-enumerated every bold span in all 17 packet block quotes against its source. No added emphasis anywhere, RFC7-34 included. The disposition row is corrected |

## Q1-Q7

| Q | Problem scope truthful? | A genuine owner gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | **Yes.** 735/713/22/0, the four-page denominator, the two legend badges at 99.96-99.97%, and the single `var(--muted)` treatment all re-derived exact. The 713/22 split is stated in five places and does soften nothing | **Yes** - a conformance ruling, and the packet states the other arm's consequences honestly at :1517-1526, including that it would satisfy "Unknown looks the same everywhere" by making Observed and Unknown look the same as each other | **Yes.** POC-REQ-060's Case fixes the denominator in the signed text; verification rule 4 names the defect; no spec delta either way | **Yes** - clause for clause |
| Q2 | **Yes**, and it is the sharpest section in the packet: two fields, two clauses, the stricter one identified and quoted to its remedy. Tier mint 11, freshness mint 0 of 713, both re-derived | **Yes**, and now genuinely open on the freshness limb: three arms, each called lawful, the PWB-REQ-007 tension put to the owner unresolved, the recommendation labelled `[Inferred]` and carrying its counter | **Yes for tier.** For freshness, (b-iii) follows from the clause the packet quotes - but its justification for the *tier* limb holds on the human channel only (H6), and the clause is quoted one sentence short of an argument against (b-ii) (H11) | **Yes** on the arms, the recommendation, the withdrawal note and the four-rows-no-absence-row conclusion. **No** on the ruling-together instruction, which the row omits (H3) |
| Q3 | **Yes.** 409 of 713, 304 remainder, 57%, 13,088, 188,902 and the inheritance sentence all re-derived from the lane B branch at `4090f98` | **Yes** - two lawful arms, and it changes a figure already in front of the owner as P-68 | **Yes.** Arm (a) preserves the queued saving and the discipline it costs is stated as a hard requirement (expand scopes before counting; assert the denominator equals the tuple count) | **Yes**, and the row is slightly *more* complete than the Q3 cell - it carries "plus an unseparated text component", which the packet states in collision item 2 rather than in Q3 |
| Q4 | **Yes.** 126 tuples, 0 Unknown, 0 disclosures, 14 mentions, 25.55 / 25.70 / 57.72 - all re-derived, each context correctly characterised | **Yes** - and the alternative is named as coherent rather than dismissed | **Yes.** CC-VIZ-3 is the warrant; the `trust-and-evidence.md` citation is correctly marked as analogy with its real subject stated | **Yes**, with G5's depth correction applied |
| Q5 | **Yes.** 12 states in prose, 15 glossary sentences, 9 describing unrendered values, 0 with a visual treatment - each re-derived from `polaris-copy.ts` 34-51 and the capture's six rendered values | **Yes** - it decides how far a declared table reaches | **Yes.** POC-REQ-061's falsifier cuts both ways and generation is the only design in which neither direction can fail; the three constraints (six tier rows, four freshness rows asserted over the renderer, markers preserved) are each traceable to a clause | **Yes** |
| Q6 | **Yes**, and honestly bounded: the sentence renders once; two of the five `var(--unknown)` rules render zero times; the three sibling surface states and `challenge-pending` render zero times; the family is stated to mint nothing. All re-derived | **Yes** | **Yes**, and the bar is now stated over a named population with the exclusion argued and the full 36-pair matrix behind it. The alternative arm is named as lawful | **Yes** |
| Q7 | **Yes** on the mechanical collision - `polaris.ts`:357 and `polaris-copy.ts`:46-49, both confirmed on both branches | **Yes**, though it is the weakest-framed of the seven: Q7's headline recommends "M2 first, then M3 slices 1-4 in parallel with P-68", while the sequence section's step 1 is "Rule P-68 first". Each qualifies itself and they reconcile, but two orderings of three items are presented as one recommendation | **Yes.** M2's markers are content slice 5's table must carry, and the reverse order loses a tested invariant | **Yes** on the sequence and the collision. **No** on "P-69 and P-70 should be ruled together" (H3) |

## Cross-packet: do P-69 and P-70 still give contradictory readings of RFC2-10?

**No - the readings now agree; the divergence has moved, and is disclosed but
framed too softly.** M2 at `f2f37dd` reads RFC2-10 as closing the vocabulary at
four *and* supplying the render-fact disclosure route: Q5 ("RFC2-10 ... requires
a condition outside the four to be 'disclosed as a fact of the render'"), Q3 (the
evaluation-scoping limb), and Q7, which quotes the disclosure sentence in full
as "the strongest counter-argument" to its own recommendation. M3's Q2 now reads
it identically. The false asymmetry G1 found is gone from both packets' prose.

What remains is a divergence in the *PWB-REQ-007 interaction*, and the two
packets resolve it opposite ways over the same claims:

- M2's Q7 resolves it: `stale`, "because PWB-REQ-007 requires the freshness field
  on every project-shape tuple ..., which the disclosure route cannot satisfy on
  these claims."
- M3's Q2 declines to resolve it ("This is the owner's question; this packet does
  not resolve it") and recommends (b-iii), the disclosure route - the arm M2 rules
  out - while listing M2's `stale` as arm (b-i), lawful and live.

Both disclose the tension, both quote the same sentence, neither calls the other
unlawful. That is the honest shape. **The one thing not said plainly is that the
two recommendations are mutually exclusive for the same population**: if the owner
grants P-69's Q7 as recommended, `claim.epistemic.freshness` is `'stale'` and
`polaris.ts`:307 never fires, which forecloses M3's (b-iii) for those claims; if
the owner grants P-70's Q2 as recommended, no value enters
`data-epistemic-freshness` for them and M2's `stale` is contradicted. Collision
item 3's closing sentence - "The two moves are complementary: M2 decides the
*value*, M3 guards the *vocabulary*" - is exactly right about slice 5's *guard*
(which holds under either ruling) and reads, in context, as though it were also
true of the two *recommendations*. It is not. Folded into H3 rather than filed
separately, because the repair is the same clause: say in the P-70 row and in
collision item 3 that P-69's Q7 and P-70's Q2 are one question with two proposed
answers, and that granting both as recommended is not available.

## Questionnaire invariant

- **Problem scope holds against the project's shape and engineering bar.** Every
  slice is inside `apps/three-surface-poc`; the Gate 3 boundary claim and the
  six-escalation-trigger check were both re-read against the named acts and hold.
- **Recommendation holds.** Each of the seven follows from its stated evidence,
  with the exceptions at H6 (Q2's tier justification) and H7 (slice 2's sweep).
- **No owner trade-off smoothed.** Q1's other arm, Q3's arm (b), Q4's
  leave-it-positive arm, Q6's one-token arm and Q2's (b-i)/(b-ii) are all stated
  as coherent and lawful. The one soft edge is collision item 3's "complementary"
  (above).
- **No lawful arm called unlawful** in the packet or the register. **One is in
  the evidence record - H1.**
- **Labels.** `[Observed]` / `[Inferred]` / `[Unknown]` are applied to every
  substantive claim I checked, including the three places the packet's reading is
  its own (PWB-REQ-020's presentation/fact distinction, RFC9-27 as a voluntary
  standard, RFC7-28 as analogue).
- **Contract claims quoted at a defined clause.** All 17 block quotes verified
  verbatim at their stated lines with source emphasis preserved; see H10 and H11
  for two unmarked truncations.
- **Zero/all claims carry a predicate and a denominator run this session.** Every
  one I relied on was re-run here with its denominator stated.
- **Digests computed**, never transcribed; the capture digest verified before
  measuring.
- **No manifest row or truncated signed digest outside the raws; no Butlers path
  in backticks; every code-span path resolves;** `check_governance.py` ends
  `0 FAIL`.

## Summary

The measurement work survives a third independent re-derivation with **zero**
discrepancies - all 36 ΔE76 pairs, the three-method tuple count, the 1,087-member
cross-surface population over four named captures with matching digests, the
409/409 by-id item sweep, the full CSS rule parse, the lane B hoist figures, the
byte arithmetic, the governance battery and every one of the 30-odd `file:line`
source citations. Review 2's nine findings are repaired at every site review 2
named, and all four of its partials are closed in the packet. G1's substance -
the hardest of the three reviews' findings - is genuinely repaired: the quote is
extended and verbatim, three lawful arms are stated, the PWB-REQ-007 tension is
put to the owner unresolved, and the recommendation is labelled and carries its
counter-argument.

The one blocking defect is that the sentence G1 blocked on is still standing in
the evidence record, in the field that reasons about the freshness mint, and two
disposition rows - one in the packet, one in the record itself - assert it was
removed everywhere. The record is a reviewed artifact the P-70 row hands the
owner by path. It is a one-field repair, and the reasoning above it is already
correct in the packet.

Findings by severity: **1 blocking** (H1), **6 non-blocking** (H2-H7),
**4 editorial** (H8-H11).

Verdict: REVISE
