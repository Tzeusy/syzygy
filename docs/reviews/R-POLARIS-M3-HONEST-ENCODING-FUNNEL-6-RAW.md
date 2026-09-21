# R-POLARIS-M3-HONEST-ENCODING-FUNNEL-6-RAW

Independent fresh-context review **6** of the M3 feature-request funnel packet
(bead `syzygy-dov.3`), its evidence record, and the P-70 note and row in the
pending-owner-decisions register. Read-only session: no file in any repository
or worktree was modified, no state-changing git command was run, no `bd`
write, no daemon, no network, no Butlers checkout read. The one file written
is this raw.

Reviews 1–5 are retained at `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md`
(F1–F14), `…-2-RAW.md` (G1–G9), `…-3-RAW.md` (H1–H11), `…-4-RAW.md` (J1–J9)
and `…-5-RAW.md` (K1–K6). Each of the five verdict words, read off the last
line of each raw this session and copied exactly: **REVISE**, **REVISE**,
**REVISE**, **REVISE**, **REVISE**. This review binds the bytes named below
and no others (verification rule 10).

## Header — commit and reviewed bytes

Worktree: `/tmp/claude-1000/-home-tze-GitHub-syzygy/6b8e9d74-3b46-4418-b725-5b74d21d660a/scratchpad/m3wt`,
branch `agent/syzygy-dov.3`, HEAD
**`9cb4d65a830588c2caf078510e7f495ce20e88b4`**
(`9cb4d65 docs: M3 funnel review 5 retained, K1–K6 repaired; review-4 J7 disposition corrected [syzygy-dov.3]`).
Working tree clean (`git status --porcelain` empty) [Observed].
`git log --oneline a9f671e..HEAD` lists five commits, all this packet's own
artifacts; `git diff --stat 76e897f..HEAD` is four files, 623 insertions,
15 deletions [Observed].

Digests computed this session with `wc -c` and `sha256sum`, never transcribed
(verification rule 3):

| File | Bytes | Lines (`wc -l`) | sha256 |
|---|---|---|---|
| `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md` | 144,850 | 1,794 | `11766f08d8f227422021c2de7475f7ef20d50a8e2fd83f741f5506b94e310a45` |
| `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json` | 55,345 | 918 | `4c61e5ccc8f51fb03a814914b918069a67806e71b1ab1a5a1872e0e51a4068ee` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 35,006 | 220 | `be27c3bb880f6d8c08ed3015f0c708ef8419e481447edea30be2f42a3953d852` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md` (reference) | 31,503 | — | `1eca5fbac6fe95266ac4968f5b55ebf89e6e63544441383c545fb89b9140bc1f` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-2-RAW.md` (reference) | 48,381 | — | `a04b20517539e971c1e192015329dd39a2e2f536b52c06fffdce473177397012` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-3-RAW.md` (reference) | 42,726 | — | `7154f1f3972cfc73619694d48851f4368a8eb7fdce77cadb81493290f82c5aa6` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-4-RAW.md` (reference) | 40,037 | — | `2c3a91917d957ad58a16b5c2cddbcc5326c412e4c35b89531c317c41b6a4d947` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-5-RAW.md` (reference) | 36,904 | — | `cbc9deac4698656e9434694741fdf66e91c60c179cd3a6942c6036e9331146d7` |

The packet's stated size and digest for the retained review-5 raw (36,904 /
`cbc9dea…`) and its stated sizes and digests for the three artifacts review 5
read at `76e897f` (139,050 / 50,219 / 33,783, with the three sha256 values at
packet :1682, :1684, :1686) are exact against `git show 76e897f:<path>` piped
to `wc -c` and `sha256sum` this session. So are the review-4 figures at
`f35a25f` (129,183 / 42,787 / 32,136) and the review-3 figures at `b34fca7`
(115,201 / 36,743 / 31,054) [Observed].

Reference bytes read read-only outside the worktree, digest recomputed before
any measurement and identical to the record's:
`.../scratchpad/m1/measure/after/polaris-tailnet.html`, 1,484,487 bytes,
sha256 `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111`,
1,481,819 decoded characters. Also read: `.../scratchpad/capture/home.html`,
`trajectory.html`, `orrery.html`, `api-poc.json`.

`python3 scripts/check_governance.py` from the worktree root ends
**`32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted`**
[Observed: run this session].

## What re-derived clean

Every figure below was re-derived independently this session from the named
bytes with Python `re` and literal `str.count`, never shell grep (verification
rule 1). All are **exact** against the packet, record and register:

- Capture 1,484,487 bytes / 1,481,819 characters.
- `class="claim-tuple"` **713**; `data-claim-id` over those spans **713**,
  **703** distinct; `data-epistemic-label="Observed"` **702**, `="Unknown"`
  **11**; `data-epistemic-tier="unstated"` **11**;
  `data-epistemic-freshness="fresh"` **713**;
  `data-challenge-state="unchallenged"` **713**;
  `class="unknown-disclosure"` **22**; `class="unavailable-notice"` **0**;
  `class="proposal"` **0**; `class="proposal-label"` **1** at **56.29%**;
  declared badge spans `class="epistemic epistemic-observed"` **1** and
  `…-unknown` **1**, both in the legend, body **0**; `data-polaris-item="`
  **409**. 713 + 22 = **735**.
- Served stylesheet: **1** `<style>` block, **206** rules; exactly **2** name
  `.claim-tuple`. Literal probes `claim-tuple[`, `[data-epistemic-label`,
  `[data-epistemic-tier`, `[data-epistemic-freshness`, `[data-challenge-state`
  each **0** over all 206 selectors. `var(--unknown)` in **5** rules,
  `var(--cyan)` in **17**. The `.unknown-disclosure` rule the packet quotes at
  Q1 is byte-identical to the served one.
- Cross-surface population under the packet's predicate (declared epistemic
  spans, legend pair excluded): home **35**, trajectory **299**, orrery
  **18**, Polaris **735**; three-surface **1,052**, four-page **1,087**;
  735/1052 = **69.87%**, 735/1087 = **67.62%**.
- First reading: boundary at the first `data-polaris-group="catalog"`,
  character **281,986** = **19.03%**; **126** tuples in the region, **all
  Observed**; **0** `unknown-disclosure` blocks. First rendered Unknown of any
  kind at character 378,604 = **25.55%**; first Unknown *tuple*
  `claim:class:roster-identity` at **25.70%**; whole-shape Unknown
  (`claim:project-shape`) at **57.72%**; the 22-entry disclosure offset list
  matches the record entry for entry. The packet's 25.55% (Q4) and the
  register's 25.70% are each correct for their own referent, and the packet's
  measurement table (:242–243) names both objects.
- Machine channel re-walked independently: **1,149** objects carrying both
  `claimId` and `epistemic` over **1,148** distinct ids; **12** carry an
  `epistemic` with no `tier` key, **all 12 labelled Unknown**, keyset exactly
  `('freshness','label','reasons')`; tier histogram `report-fact` **1,137**,
  absent **12**; `unstated` occurs **0** times in the whole machine answer.
- Colour: `design-tokens.ts` 46–55 read line by line — **10** tokens,
  `--focus` equal to `--amber`, **9** distinct values, **36** pairs.
  Recomputed (CIE76 over CIE Lab, sRGB → D65): `--amber`/`--unknown`
  **7.8462** smallest over the five foreground tokens, `--ink`/`--muted`
  **26.7371** next; over the distinct nine, **seven** pairs strictly below
  26.7371 (3.9753, 4.8231, 7.8462, 8.7759, 14.9639, 19.5580, 23.2692).
- Byte arithmetic: 702×19 + 11×18 + 702×4 + 11×2 = **16,366**; 409 × 32 =
  **13,088**.
- Source citations re-read at HEAD and exact: `polaris.ts` 305–308 (the two
  `?? 'unstated'` mints at **306–307**), 346–361 (`claimStatesBlock`, the
  freshness group at **357**; 7 tier ids, 4 freshness, 1 challenge = 12),
  506–510, 1307 (`.claim-tuple`), 1328 (`.proposal`), 1329
  (`.proposal-label`, `color: var(--unknown)`); `polaris-copy.ts` 34–51 =
  **15** state sentences (3 label + 7 tier + 4 freshness + 1 challenge) plus
  **3** group labels.
- Checker: `surface-routes.test.ts`:64–101 reads `const denominator =
  pages.length` over `['/', POLARIS, TRAJECTORY, ORRERY]` = **4**, tests each
  page with `page.html.includes('class="epistemic epistemic-observed"')` /
  `-unknown` and `continue`s a page carrying neither — the legend alone
  satisfies it.
- Contract and spec quotes re-matched verbatim against source under
  whitespace normalisation, with the source's own emphasis and no additions:
  RFC2-10 (`snapshot-and-evaluation-core.md` 209–223, read line by line);
  RFC2-25:169 exact; PWB-REQ-007 at spec :439 and 443–446; PWB-REQ-020 at
  :902; POC-REQ-060's Case at 936–938 ("a checker enumerates every epistemic
  encoding on all three surfaces — the denominator is that population");
  the 2026-09-02 authorization's full six-trigger escalation sentence,
  matched as an exact whitespace-normalised substring of
  `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`. Both act paths cited in the
  Gate 3 table exist.
- Code-span sweep over the packet outside fenced blocks: **619** backtick
  spans, **85** path-shaped; every fully-qualified path resolves against
  `git ls-files` or the filesystem, and the **11** non-resolving spans are git
  refs (6), an HTML fragment, a glob, two shell commands and a
  `proposed/spec.md.patch` shorthand — not paths. **No Butlers repository path
  appears in backticks**: the only two `butler`-matching spans are the Syzygy
  `openspec/changes/polaris-project-wide-butlers-model/…` paths [Observed:
  denominator every backtick span outside fences].
- No manifest row, act argument or truncated signed digest is quoted in the
  packet, record or register; `check_governance.py` (which owns CG-1b, CG-7e
  and CG-15) ends 0 FAIL.

The measurement work survives a sixth independent re-derivation with **no
discrepancy in any figure taken from the captures, the machine answer, the
token set, the source files or the contract text.** Every finding below is in
prose that reasons *about* the packet's own repair history.

## Findings

### L1 — blocking — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:1461 and `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json` `review1.dispositions.F4`, against packet :1528 (G1 row) and :1588 (H1 row) — the withdrawn RFC2-10 reading still stands unmarked at a sixth packet site and a seventh record site, and the two rows that count the sites are wrong about how many there are

**Defect.** Review 2's G1 withdrew the proposition that RFC2-10 supplies no
absence route, so arm (b) is unavailable for the freshness field. The G1 row
(:1528) records the withdrawal as covering "the packet's four prose sites and
the register row", plus "a **fifth** site this repair pass missed" (the
record's `freshness_mint_hazard`, review 3's H1). The H1 row (:1588) closes
its literal sweep with the classification: "every other occurrence is either
current lawful-arms language, an existing in-place withdrawal marker, or a
review-history quote already framed as superseded."

Two occurrences fit none of the three, and both state the withdrawn
proposition in the present tense with no marker of any kind.

1. **Packet :1461**, the F4 row of the review-1 disposition table, reads in
   full: "Accepted and repaired: … **The asymmetry is stated: RFC2-25 supplies
   an absence remedy, RFC2-10 forbids the minting in terms and supplies none,
   so arm (b) governs tier and is **not** lawfully available for freshness —
   the owner is shown the two arms that are** (the renderer supplies one of
   the closed four, per M2's Q7; or the claim is held Unknown), and that
   PWB-REQ-007's Falsifier forbids simply omitting the field."
   "The asymmetry is stated" is a claim about the packet as it now stands, and
   it is false three ways: RFC2-10 does supply a remedy (quoted at Gate 2
   :627–629 and at record :279 from the clause's own 220–222); arm (b) is not
   called unlawful for freshness anywhere in the current Q2; and the owner is
   shown **three** arms, not two.
2. **Record `review1.dispositions.F4`** reads "… Q2 scope extended to
   freshness with **arm (b) ruled unavailable there** …", unmarked, while its
   sibling `review1.recommended_answers_changed.Q2` (:674) carries the H2
   marker for the same wording and `review2.repairs.G1` (:741),
   `review3.repairs.H1` (:804) and `review3.repairs.H5` (:808) all carry
   theirs.

The literal sweep the H1 row runs *does* reach both (they match `supplies
none`, `not lawfully available`); it is the classification of the hits that is
wrong, so the count of sites published in two disposition rows — four prose
sites plus the register plus one fifth — understates by two. The record's
`review5.sweep_after_repair.result` (:914) repeats it: "every one inside
review-history or lawful-arms text; **0 stand as a live claim that any arm is
unavailable**." Occurrence 1 does stand as one.

This is the class reviews 2, 3, 4 and 5 each blocked on — a disposition row
asserting something untrue of the bytes, and a claim of absence over sites
without a predicate that reaches them (verification rules 4 and 9). Nothing
here moves a recommendation, a gate or an owner question, and the correct
reading sits twelve lines below at :1476–1479 with its marker; what it damages
is the one property this packet's review history exists to protect, and it
does so in the table a reader consults to learn what the packet concluded.

I note in mitigation that the F4 row's *first* clause is accurate history and
that the row sits under a "Review 1 and repairs" heading. That is exactly why
:1476 was marked rather than rewritten, and the same treatment was owed here.

**Repair.** Mark both in place, without deleting either: append to :1461
"(the asymmetry as stated here was withdrawn after review 2, finding G1 —
RFC2-10 supplies a disclosure remedy at lines 220–222 and arm (b) is not
called unlawful for freshness; Q2 now states three arms, not two)", and the
same to `review1.dispositions.F4`. Then correct the two counts: the G1 row's
"four prose sites and the register row … a fifth site" and the H1 row's
three-way classification, which must name the disposition-table occurrences as
a fourth category (review-history text that states the withdrawn proposition
in the present tense) and say how many there are. Re-derive
`review5.sweep_after_repair.result`'s "0 stand as a live claim" with a
predicate that separates "inside a review-history section" from "framed as
superseded" — they are not the same test, and the whole finding is the gap
between them.

### L2 — non-blocking — `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:542, :543, :562, :563 — the record's `m2_collision` block still carries `da1497b` as M2's head, unmarked, six days and three reviews after H4 moved the packet to `f2f37dd`

**Defect.** Review 3's H4 found `da1497b` a fourth stale reading and repaired
the packet's collision section, which now names `f2f37dd` once, dated
(:1259–1267), and cites M2 by register row P-69 otherwise. The record's own
current-state fields were not brought with it:

- `"head": "da1497b"` (:542), sitting above the historical ladder
  `head_at_packet_first_draft` / `head_at_review_1` / `head_at_review_2`, so
  it reads as the current head.
- `"head_note"` (:543): "re-derived **this repair pass** (review 2, G4) …".
- `"shared_surface_unchanged_at_da1497b": true` (:562).
- `"structural_collision_confirmed_by": "M2's own Gate 3 row and Q5 text, read
  **this session** at da1497b"` (:563).

`review3.re_derived_before_applying.H4` (:794) and `review3.repairs.H4` (:807)
both name `f2f37dd`, so the record contradicts itself, and the field an
automated reader of `m2_collision` would take is the stale one. I confirmed
M2's head is still `f2f37dd` this session (`git -C .../scratchpad/m2wt log
--oneline -3`, read-only) — so the substance (six slices, slice 6's two
untouched files, the Q5 ruling, the shared surface unchanged) is true at both
heads and no conclusion moves. `review1.dispositions.F7` has the same shape in
its smallest form ("M2 head is 68123fc", present tense, unmarked).

This is the "the record is repaired last" shape that J1, J2, J3 and K4 each
closed, at the one current-state block nobody swept.

**Repair.** Set `m2_collision.head` to `f2f37dd` with the ladder extended
(`head_re_derived_after_review_3_at_f2f37dd`), restate `head_note` in the past
tense, rename or re-key `shared_surface_unchanged_at_da1497b`, and date
`structural_collision_confirmed_by` to the head and session it was actually
read at. Append the H4 marker to `review1.dispositions.F7`.

### L3 — non-blocking — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:63 (Q7, recommended answer) against :1260 — the packet's owner-facing question table says M2 has five retained reviews; the packet's own collision section names M2's review 6

**Defect.** Q7's recommendation reads: "**M2 first, then M3 slices 1–4 in
parallel with P-68, then M3 slices 5–6.** M2's packet is further along (**five
reviews retained**, P-69 queued) …". The collision section 1,197 lines below
says M2 is at `f2f37dd` — "M2 funnel review **6** CONFIRM WITH EXCEPTIONS
retained; L1–L4 applied" — the head review 3's H4 established on 2026-09-14
and which I confirmed unchanged this session. M2's worktree carries six
retained raws under `docs/reviews/` [Observed: directory listing, read-only,
denominator every `R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL*-RAW.md` file].

The premise survives the correction — six is still further along than one — so
the recommendation does not move. But this is a stale figure inside a
recommended answer, contradicted by the packet's own later section, in the
table the owner rules from; and it is the same class the packet has repaired
four times for M2's head hash (F7, G4, H4), left standing in the one place the
head hash was replaced by a count.

**Repair.** "six reviews retained (M2 at `f2f37dd`, review 6 CONFIRM WITH
EXCEPTIONS)", or drop the count and cite the collision section's dated line,
which is where the packet decided such facts belong.

### L4 — non-blocking — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:1652 (J6 row) and :1689–1691 — review 5 verified J6 as PARTIAL and J7 as NOT REPAIRED; J7's row carries that and J6's does not, and the review-5 section omits review 5's J1–J9 summary

**Defect.** Review 5's J-verification table gives "**7 REPAIRED, 1 PARTIAL, 1
NOT REPAIRED**, over a denominator of 9" (`…-5-RAW.md`:348), with J6 PARTIAL
(the funnel-summary handoff line, K2) and J7 NOT REPAIRED (K1). The packet
carried that verdict into the J7 row — "**CONFIRMED — REPAIRED, and the repair
corrected after review 5 (K1)**" (:1653) — but the J6 row (:1652) still reads
a bare "**CONFIRMED — REPAIRED**" with no note that the repair reached the
handoff section only until review 5, exactly as the H1 and H5 rows were
restated to "**PARTIAL at `f35a25f`**, completed after review 4" when reviews
found them short. And the review-5 section's own account (:1689–1691) says "It
verified J1–J9 against the current bytes and spot-checked every earlier
finding; nothing previously accepted regressed" without the 7/1/1 counts,
while the review-2 section states 10 REPAIRED / 4 PARTIAL and the review-4
section states its severities.

Nothing substantive is false — both repairs are complete at HEAD, and K2's
disposition row (:1713) records what was done. But H5 and J2 were filed
precisely to stop the packet reading cleaner than the raw it retains on a
verification count, and this is the same page reading cleaner than the raw it
retains on a verification count.

**Repair.** Restate the J6 row as "CONFIRMED — PARTIAL at `76e897f`, completed
after review 5 (K2)", and add review 5's own summary to :1689–1691: "it
verified J1–J9 as 7 REPAIRED, 1 PARTIAL (J6) and 1 NOT REPAIRED (J7) over a
denominator of 9; both are complete at this commit."

### L5 — editorial — `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:282, last limb — the K3 repair settles RFC2-10's remedy at 220–222 and then gives the orthogonality sentence a one-line extent the same pass fixed everywhere else

**Defect.** K3's second limb asked for one extent for one sentence. The repair
delivered it at the packet's G1 row, the H1 row and `review3.repairs.H1`, all
of which now read "the remedy sentence runs 220–222, with 222–223 the separate
orthogonality sentence" — and I confirm both extents line by line against
`snapshot-and-evaluation-core.md` this session. The prose of
`freshness_mint_hazard` itself, repaired in the same pass, says "**line 223**
adds that freshness never substitutes for the labels or the tier registry".
The sentence it names begins at 222 ("Freshness is orthogonal to the three
labels and the tier registry; it") and ends at 223 ("never substitutes for
either."). Same clause, fourth site, one line short.

Not substantive: the prohibition pointer (212–214) and the remedy extent
(220–222) are both right here, and the fourth-limb wording is a description
rather than a citation. It is listed because it is the one spot the K3 repair
did not reach, and because a reader chasing "line 223" gets half a sentence.

**Repair.** "lines 222–223 add that freshness never substitutes …".

### L6 — editorial — `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:167–176 — the two sibling offset fields anchor on different characters, and neither says which

**Defect.** `first_rendered_unknown_of_any_kind.offset_chars` is **378,604**,
which is the offset of `class="unknown-disclosure"` (its element start is
378,599). `first_unknown_tuple.offset_chars` is **380,767**, which is the
element start of the tuple's `<span` (the `class="claim-tuple"` substring
begins at 380,773). Two conventions in adjacent fields of one block, with no
`method` or anchor stated, in a record whose own `sweep_methods` block
enumerates rules 1, 2, 4 and 9.

It changes one published value: `unknown_tuple_offsets_percent` lists
**97.49**, which is the element-start rounding; the `class=`-anchored
rounding is 97.50. Every other entry in both lists is identical under either
anchor, and I reproduced the 22-entry disclosure list exactly. No conclusion
depends on it.

**Repair.** State the anchor once in `first_reading` ("offsets are the
character index of the element's opening `<`") and re-derive both fields under
it, or name the two conventions where they differ.

## K1–K6 verification against the current bytes

Each re-derived from source, the retained captures or the retained raws this
session, not taken from the review-5 section's own account.

| K | Severity (review 5) | Verified verdict | Evidence |
|---|---|---|---|
| K1 | blocking | **REPAIRED** | I re-ran the six literals (`supplies no`, `no absence`, `not lawfully available`, `unlawful`, `no remedy`, `supplies none`) over the three files with Python `str.count` at three commits: `b34fca7` **25** occurrences, 2,479 lines by `wc -l`, **2,482** counting each file's trailing line; `f35a25f` **41**, 2,697 / **2,700**; `76e897f` **42**, 2,805 / **2,808** — every figure the H1 row (:1588), the J7 row (:1653), the review-5 section (:1693–1700) and record `review5.re_derived_before_applying.K1` (:895) state. The H1 row now carries the stamp J7 asked for, "as of `b34fca7`, the bytes review 3 read", with **both conventions named at both commits**, like for like. The J7 row quotes its own false text, cites `…-4-RAW.md`:359–361 (which I read: "at `b34fca7`, **25 occurrences over 2,482 lines** — exact", and "**41 occurrences over 2,700 lines**" at `f35a25f`, so review 4 used the trailing-line convention throughout), and restates the disposition. Record :837 and :848 are marked superseded on their own lines with the withdrawn text kept. The review-4 section's "All nine findings confirmed" (:1636) now appends "(the J7 disposition this pass then wrote was itself wrong — review 5, K1)". (The H1 row's *classification* of the hits is **L1**; the figure is right) |
| K2 | non-blocking | **REPAIRED** | The funnel summary's handoff line (:1747) now reads `Q1 "a non-conformance", Q3 "inheritance", Q4 "yes" and Q6 "a --proposed token" -> run slices 1, 2 and 4 now under syzygy-dov.3, in parallel with P-68 and M2, slice 3 next`, with its earlier text quoted in place. Compared clause by clause against the Recommended handoff section (:1752–1763): four answers, same three slices immediate, slice 3 next, same hold on 5–6, same "open no specification package". Both now match |
| K3 | non-blocking | **REPAIRED** | `freshness_mint_hazard` (:282) anchors the prohibition at "lines 212-214" and quotes its six words, with the line-219 pointer quoted and marked withdrawn. Verified against source read line by line: the prohibition sentence's first word "The" sits at the end of line **212** and it ends "it does not carry." on **214**; line **219** is "verbatim nor checked for parity, and leaving it unstated is how the value gets" — the parity rationale. The remedy's extent is 220–222 at the G1 row (:1528), the H1 row (:1588) and `review3.repairs.H1` (:804), with 222–223 named separately. (One fourth-limb line-extent remains: **L5**) |
| K4 | non-blocking | **REPAIRED** | `review3.repairs.H1` (:804) now ends "(the three arms enumerated here did not match the packet's or the register's - corrected after review 4, finding J3; and the remedy sentence runs 220-222, with 222-223 the separate orthogonality sentence)" — the marker its siblings `review3.repairs.H5` (:808) and `review2.repairs.G1` (:741) carry |
| K5 | editorial | **REPAIRED** | The P-70 note now opens "**Updated 2026-09-14, and again 2026-09-15 for reviews 4 and 5 (Polaris honest encoding):**" and its review-1 clause reads "REVISE, four blocking; fourteen findings, ten repaired in that pass and four closed after review 2 — 10 REPAIRED / 4 PARTIAL as review 2 verified". The row's review-1 citation carries the same sentence. I recounted `…-2-RAW.md`:461–474 by the table's verdict column: REPAIRED F1, F2, F3, F5, F8, F9, F10, F11, F13, F14 (**10**); PARTIAL F4, F6, F7, F12 (**4**); NOT REPAIRED **0**; denominator **14** — matching the register, the packet's review-2 section and record :730 |
| K6 | editorial | **REPAIRED** | `freshness_mint_hazard` now reads "stated here in the packet's own words, which the P-70 row paraphrases clause for clause", with the overreach quoted and marked; `review4.repairs.J3` carries the same marker on its line. I string-compared the (b-i)/(b-ii)/(b-iii) text against packet Q2 (:58) after ASCII normalisation — **character for character identical** — and read the register's Q2 limb, which is a paraphrase denoting the same three arms |

Summary: **6 REPAIRED, 0 PARTIAL, 0 NOT REPAIRED**, over a denominator of 6.
The K1 repair, which review 5's summary singled out as the one that had to be
got right, is exact at all three commits under both conventions.

## J1–J9 and earlier findings — regression spot-check

I did not re-litigate accepted repairs; I checked that the bytes prior reviews
confirmed are still those bytes, and specifically the record line numbers the
packet cites, which had to survive the record growing 856 → 918 lines.

- **The cited record lines still point where the packet says** [Observed: each
  line printed this session]: `:279` `closed_freshness_vocabulary_authority`
  (cited at packet :1647), `:282` `freshness_mint_hazard` (:1588, :1649),
  `:674` `review1.recommended_answers_changed.Q2`, `:730`
  `review2.f_verification_against_review_1` (:1648), `:741`
  `review2.repairs.G1` (:1647), `:808` `review3.repairs.H5` (:1648). All six
  unchanged in target despite 62 lines being appended below :854.
- **J1** — `:279` quotes RFC2-10 from "Four values, closed." to the clause's
  end; I extracted the quoted span and matched it against source 212–223 under
  whitespace normalisation: identical, with the truncation disclosed in place.
- **J2** — `:730` reads 10 / 14 / PARTIAL F4, F6, F7, F12 / NOT_REPAIRED 0;
  recounted from the raw's table above.
- **J3** — `:282`'s arms are the packet's verbatim (string-compared).
- **J4** — both denominators re-summed from the four captures: 1,052 and
  1,087, 69.87% and 67.62%, stated at Q1 (:57), the population prose, slice 2,
  the funnel summary (:1738) and the register's Q1 limb, each with the reason
  the sweep is deliberately wider.
- **J5** — 12 of 1,149, all Unknown, keyset exact, all 11 human-side matches;
  the register's Q2 limb states it as a PWB-REQ-020 parity question "this
  packet discloses and does not resolve".
- **J6** — complete at HEAD (both handoff statements agree); the row's own
  disposition word is **L4**.
- **J7** — complete at HEAD (K1 above).
- **J8** — the baseline bracket points at `git log` rather than counting;
  confirmed five commits on the branch, all packet artifacts.
- **J9** — Gate 3's bracket (:786–793) is split five Observed limbs / one
  Inferred scope limb with the Gate 5 pointer; I counted the five.
- **H1 / H5** — both rows read "CONFIRMED — PARTIAL at `f35a25f`, completed
  after review 4", naming J1/J3/J7 and J2.
- **H2** — `:674` still carries the in-place marker with the superseded text.
- **H3** — the P-70 row still ends with the mutual-exclusivity clause; the
  packet states the P-69/P-70 coupling at Q2, Q7 and the collision section.
- **H4** — the collision section cites M2 by register row with one dated
  exception naming `f2f37dd`, which I confirmed is still M2's head. (The
  record's own block is **L2**.)
- **H6** — Gate 2's machine-side absence carries its predicate and
  denominator; re-derived above.
- **H9 / H10 / H11** — `…-2-RAW.md`:567 is exactly `Verdict: REVISE`; both
  spec block quotes carry `…` between retained bullets; the Gate 2 RFC2-10
  quote runs 209–223 and RFC2-11 begins after the next blank line, so "quoted
  in full" is true.
- **F2 / G7** — 36-pair matrix recomputed; seven below 26.7371; "26.74 to two
  decimals, 26.7371 computed" intact.
- **F3** — RFC2-25:169 quoted with the source's own emphasis; the three
  sibling states and `challenge-pending` each **0** over the whole capture.
- **F5 / F10** — the 713/22 split and the 0/0/22/1 token-reuse counts exact.
- **F8 / F13 / F14** — 346–361 with 357, 46–55, 34–51 all exact.
- **G5 / G8 / G9** — the register reads "57.72% and 25.70%"; Q3's arm (b)
  reads "at least 13,088 attribute bytes plus an unseparated text component".

**No regression found.** Nothing reviews 2–5 confirmed has moved, every cited
record line still resolves, and every figure re-derives exactly. The three
findings above that touch repair history (L1, L2, L4) are sites earlier passes
did not reach, not sites that moved.

## Q1–Q7

| Q | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | Yes. 735 = 713 + 22 re-derived three ways; both denominators (1,052 / 69.87% on the requirement's three surfaces; 1,087 / 67.62% over the four pages swept) re-summed exactly, with the Home rationale stated; the checker's denominator of 4 read at `surface-routes.test.ts`:82 | Yes — a conformance ruling, with the "already conformant" arm written out as a coherent recorded outcome rather than left as silence | Yes. The 713/22 split sharpens rather than softens it, and the other arm's consequence (the four-page checker stands, the 735 become an accepted gap) is stated at :1785–1794 | **Yes, clause by clause**, including both denominators, the Home rationale and the J4 attribution |
| Q2 | Yes. Both mints at `polaris.ts` 306–307; tier fires 11, freshness 0; RFC2-25's rendering remedy and RFC2-10's disclosure remedy distinguished at their clauses and quoted verbatim; the PWB-REQ-007 tension put to the owner unresolved; the machine-channel tier absence disclosed and re-derived (12 of 1,149, all Unknown) | Yes — the strongest gate in the packet, and the packet twice declines to settle it | Yes, and correctly `[Inferred]`. No arm is called unlawful **in Q2, the register or the record's live analysis field**; (b-i) credited to P-69, (b-ii) kept live against the orthogonality sentence. The one place the withdrawn "not lawfully available" still stands unmarked is the review-1 disposition table — **L1**, a history site, not the recommendation | **Yes.** The record's arms are the packet's verbatim; the row's paraphrase denotes the same three: (b-i) closed four / P-69's Q7; (b-ii) held Unknown, not rendered as though it had a freshness state; (b-iii) disclosed outside the `data-epistemic-freshness` slot, never dressed as a freshness state. The machine-channel clause is in the row |
| Q3 | Yes. 409 of 713 from lane B's own record, container mode named; 409 × 32 = 13,088 recomputed; `data-polaris-item="` 409 re-derived from the capture | Framed as a choice; both arms lawful, and arm (b) is said to "spend a ruling the owner has not yet made" | Yes, with the discipline it costs stated as a hard requirement on every M3 sweep and on slice 2's denominator | Yes, and the register is stricter ("plus an unseparated text component", G9) |
| Q4 | Yes. 126 tuples all Observed and 0 disclosures in the 19.03% opening band; 25.55% / 25.70% / 57.72% re-derived to the exact character offset, and the packet's measurement table names both objects so the register's 25.70% and Q4's 25.55% reconcile on the page | Yes — a design ruling on what the owner's first stop opens with | Yes, and the contrary arm is stated as coherent, not strawmanned; CC-VIZ-3 cited for its own subject and `trust-and-evidence.md`:101 marked "by analogy" | Yes; 25.70% names the claim to be surfaced and 25.55% the first disclosure block — each correct for its referent |
| Q5 | Yes. 12 tier/freshness/challenge states in one collapsed disclosure (7 + 4 + 1 read at `polaris.ts` 356–358), none with a visual encoding, 15 glossary sentences of which 9 unreachable — all re-derived from `polaris-copy.ts` 34–51 and the capture | Yes — a copy-and-encoding ruling binding two later slices | Yes, and it carries three constraints forward, including M2's "mark, do not delete" shape | Yes |
| Q6 | Yes. 1 proposal label at 56.29% in `var(--unknown)`, 5 rules on that token for 4 meanings, 2 rendering 0 times; RFC2-25:169 quoted at its clause and the family mints nothing | Yes, and the handoff now discloses that slice 2 pulls one rule of Q6's token forward — at **both** statements of the handoff since K2 | Yes; the ΔE76 floor is stated over a named population with the full matrix in evidence (7.8462 smallest, 26.7371 next, both recomputed), and the alternative arm is named lawful under CC-VIZ-1 | Yes |
| Q7 | Mostly. The collision is exact (`polaris.ts`:357, the `polaris-copy.ts` freshness sentences, both read this session) and the P-69/P-70 coupling states mutual exclusivity — but the recommendation's parenthetical says M2 has five retained reviews where the packet's own collision section and M2's branch say six (**L3**) | Framed as a sequencing choice, correctly | Yes. It does not smooth M2's `stale` and this packet's (b-iii) into a reconciled pair, and the premise survives the L3 correction | Yes, including the mutual-exclusivity clause; the register does not restate the review count |

## Questionnaire invariant

- **Problem scope and recommendation hold against the project's shape and
  engineering bar** — yes. Every slice is app-local, rides the 2026-09-05
  continuation, crosses none of the six escalation triggers (the act's
  sentence matched verbatim against source this session), and Gate 6 carries
  retained measurement, denominators, rule-6 mutants per guard branch,
  per-tuple parity and an independent review.
- **No owner trade-off smoothed into consensus** — yes, in all three
  artifacts.
- **No lawful arm called unlawful** — yes in Q2, the register row and the
  record's live analysis field. **No** at one unmarked history site in the
  packet's review-1 disposition table and its record twin (**L1**).
- **Every substantive claim labelled** — yes.
- **Contract claims quoted at a defined clause** — yes. Every quote I
  re-matched verbatim against source, with the source's own emphasis and
  nothing added; RFC2-10's prohibition is now anchored at 212–214 and its
  remedy at 220–222, with one fourth-site line-extent drift (**L5**).
- **Zero/all claims carry a predicate and denominator run this session** — yes
  for every measurement figure, all re-derived above; the sweep figure K1
  contested is now exact at its commit under both stated conventions. **No**
  for the classification the H1 row and record :914 put on that sweep's hits
  (**L1**), which is a claim of absence over sites whose predicate does not
  reach two of them.
- **Digests computed** — yes; every digest in this raw was computed this
  session with `wc -c` and `sha256sum`, and the packet's stated digests for the
  five retained raws and for the three artifacts at `76e897f`, `f35a25f` and
  `b34fca7` all match mine exactly.
- **No manifest or truncated signed digest quoted outside the raws; no Butlers
  path in backticks; every code-span path resolves** — all confirmed, with
  denominators above.
- **`python3 scripts/check_governance.py` ends `0 FAIL`** — confirmed:
  `32 OK, 20 WARN, 0 FAIL (52 checks)`.

## Summary

All six of review 5's findings are repaired in the bytes, and the one that
mattered — K1 — is done properly: the sweep figure is stamped to `b34fca7`
with both line-counting conventions named at both commits, the false
"reproducible from no commit" text is quoted and corrected rather than
deleted, the two record fields that carried it are marked superseded on their
own lines, and the review-4 section now says its own J7 disposition was wrong.
I re-derived the pair at three commits (25 / 2,479 / 2,482; 41 / 2,697 /
2,700; 42 / 2,805 / 2,808) and every figure is exact. K3's line pointer, K4's
marker, K5's two-date stamp and 10/4 clause, K6's "the packet's own words" and
K2's funnel-summary line are all in place. Nothing previously confirmed
regressed, all six cited record line numbers still resolve after the record
grew 62 lines, and the measurement work survives a sixth independent
re-derivation without a single discrepancy.

The blocking finding is the same proposition reviews 2, 3 and 4 chased across
five sites, standing unmarked at a sixth and a seventh — the F4 disposition
row in the packet's review-1 table and its twin in the record — while two rows
publish a count of the sites and a classification of the sweep's hits that
neither occurrence fits. The literal sweep found them every time; what failed
is the step after the sweep, where each hit is put in a box. "Inside a
review-history section" and "framed as superseded" were treated as the same
test for five passes, and they are not: :1476 got a marker and :1461, twelve
lines above it, did not.

The rule this packet has now paid for six times is one step further on from
review 5's. Review 5's was: re-derive the figure with the predicate stated,
including the counting convention, before writing the sentence that disposes
of it. This one is: **a sweep's predicate is only half of it — publish the
rule that sorts the hits, and test that rule against every hit, because a
classification is an absence claim about each box you did not put a hit in**
(verification rule 9). Three of the four non-blocking and editorial findings
below it (L2, L4, L5) are single sites an earlier pass's own discipline
already names; L3 is a stale count in a recommended answer that the packet
contradicts 1,197 lines later.

Findings by severity: **1 blocking** (L1), **3 non-blocking** (L2, L3, L4),
**2 editorial** (L5, L6). Six findings over two artifacts.

Verdict: REVISE
