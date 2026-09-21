# R-POLARIS-M3-HONEST-ENCODING-FUNNEL-4-RAW

Independent fresh-context review **4** of the M3 feature-request funnel packet
(bead `syzygy-dov.3`), its evidence record, and the P-70 note and row in the
pending-owner-decisions register. Read-only session: no file in any repository
or worktree was modified, no state-changing git command was run, no `bd` write,
no daemon, no network, no Butlers checkout read. The one file written is this
raw.

Reviews 1–3 are retained at `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md`
(F1–F14, verdict word copied exactly: **REVISE**), `…-2-RAW.md` (G1–G9,
**REVISE**) and `…-3-RAW.md` (H1–H11, **REVISE**). This review binds the bytes
named below and no others (verification rule 10).

## Header — commit and reviewed bytes

Worktree: `/tmp/claude-1000/-home-tze-GitHub-syzygy/6b8e9d74-3b46-4418-b725-5b74d21d660a/scratchpad/m3wt`,
branch `agent/syzygy-dov.3`, HEAD
**`f35a25fb927f7ae926d9e039649786670a5d1423`**
(`f35a25f docs: M3 funnel review 3 retained and H1–H11 repaired [syzygy-dov.3]`).
Working tree clean (`git status --porcelain` empty). `git diff --stat a9f671e..f35a25f`
is six files, 4,064 insertions, 0 deletions — all of them this packet's own
artifacts; no source file cited by line in the packet moved between the stated
baseline and HEAD [Observed].

Digests computed this session with `wc -c` and `sha256sum`, never transcribed
(verification rule 3):

| File | Bytes | Lines | sha256 |
|---|---|---|---|
| `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md` | 129,183 | 1,661 | `99e95b1773884661017352a17826bf40c74e9b21ba074b12f56c5695a2f649c4` |
| `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json` | 42,787 | 824 | `03ea7e0eea4d752c30557faa5ab30465d27d5518e422f426521a68065b49bdad` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 32,136 | 212 | `4165ebc80d1c69b8bab30bb6d579b7dce7fab09ced1f108568098e99310b6991` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md` (review 1, reference) | 31,503 | — | `1eca5fbac6fe95266ac4968f5b55ebf89e6e63544441383c545fb89b9140bc1f` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-2-RAW.md` (review 2, reference) | 48,381 | — | `a04b20517539e971c1e192015329dd39a2e2f536b52c06fffdce473177397012` |
| `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-3-RAW.md` (review 3, reference) | 42,726 | — | `7154f1f3972cfc73619694d48851f4368a8eb7fdce77cadb81493290f82c5aa6` |

Reference bytes read read-only outside this worktree:

| File | Bytes | sha256 (first 16) |
|---|---|---|
| retained lane A after/tailnet capture, `.../scratchpad/m1/measure/after/polaris-tailnet.html` | 1,484,487 | `e8a04b4631dedbda159dd162d25f4e8a7ed4f9f4059a37ca1bca87b717790111` (full, recomputed) |
| retained machine answer, `.../scratchpad/m1/measure/after/api-poc.json` | — | read this session |
| `.../scratchpad/capture/home.html` | 38,706 | `c2fd6d1af7103e87…` |
| `.../scratchpad/capture/trajectory.html` | 244,524 | `fd802531b199084e…` |
| `.../scratchpad/capture/orrery.html` | 37,048 | `e3ae5b7901c599a0…` |

The capture digest is identical to the one the packet and the evidence record
name, recomputed here before any measurement [Observed]. The three
cross-surface capture sizes and digest prefixes are identical to the record's
`cross_surface_population.pages` fields [Observed].

`python3 scripts/check_governance.py` from the worktree root ends
**`32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted`**
[Observed: run this session; identical to the record's
`governance_check.baseline_last_line`].

## What re-derived clean

Every load-bearing figure was re-derived independently this session from the
named bytes with Python `re` and literal `str.count`, never shell grep
(verification rule 1). All of the following are **exact**:

- Capture: 1,484,487 bytes, 1,481,819 decoded characters.
- `class="claim-tuple"` **713**; distinct `data-claim-id` over those spans
  **703**; `data-epistemic-label="Observed"` **702** / `="Unknown"` **11**;
  `data-epistemic-tier="unstated"` **11**; `data-epistemic-freshness="fresh"`
  **713**; `data-challenge-state="unchallenged"` **713**.
- `class="unknown-disclosure"` **22**; `class="unavailable-notice"` **0**;
  `class="proposal"` **0**; `class="proposal-label"` **1**, at **56.29%**
  depth.
- Served stylesheet: one `<style>` block, **206** rules. Exactly **2** name
  `.claim-tuple` (base rule `font-family … color: var(--muted); letter-spacing:
  .04em;` and one override of `letter-spacing`/`font-size` only) — **one**
  colour treatment over all 713 tuples. Literal probes `claim-tuple[`,
  `[data-epistemic-label`, `[data-epistemic-tier`, `[data-epistemic-freshness`,
  `[data-challenge-state` each return **0** over all 206 selectors.
  `var(--unknown)` in **5** rules (`.epistemic-unknown`, `.unavailable-notice`,
  `.unknown-disclosure`, `.proposal`, `.proposal-label`); `var(--cyan)` in
  **17**. `.unknown-disclosure`'s served rule matches `polaris.ts`:1317 and
  `.proposal-label`'s matches `polaris.ts`:1329 exactly.
- Declared badge spans on Polaris: **2**, first at 99.96% depth, **0** in the
  body.
- Cross-surface population **1,087** = home 35 + trajectory 299 + orrery 18 +
  Polaris 735, declared-class total **352**, recomputed from the three capture
  files and the Polaris capture (badges − 2 legend badges per page).
- First reading: boundary at character **281,986** = **19.03%**; **126** tuples
  in the region, all `Observed`; **0** `unknown-disclosure` blocks.
- Item and source rows: `data-polaris-item="` **409**, bare `data-polaris-item`
  **417**, `data-polaris-items` **8**.
- Machine channel (H6's predicate re-run independently): **1,149** objects
  carrying both `claimId` and `epistemic` over **1,148** distinct ids; all
  **11 of 11** human-side Unknown tuple ids matched, and all **11 of 11** have
  an `epistemic` object with exactly `['freshness','label','reasons']` — no
  `tier` key. Machine-side tier histogram `report-fact` **1,137**, absent
  **12**. `unstated` occurs **0** times in the machine answer.
- Colour: 10 tokens at `design-tokens.ts`:46–55 (read line for line), **9**
  distinct values, **36** pairs. All recomputed (CIE76 over CIE Lab, D65):
  `--panel`/`--void` 3.9753, `--panel`/`--panel-raised` 4.8231,
  `--amber`/`--unknown` 7.8462, `--panel-raised`/`--void` 8.7759,
  `--line`/`--panel-raised` 14.9639, `--line`/`--panel` 19.5580,
  `--line`/`--void` 23.2692, `--ink`/`--muted` **26.7371** — **seven** pairs
  strictly below the `--ink`/`--muted` floor. Over the five foreground tokens
  (10 pairs) **7.85** is smallest and **26.74** next. `--focus` equals
  `--amber` exactly (ΔE76 0.00), which is why the distinct set is 9.
- Byte arithmetic: 1,484,487 − 1,400,000 = **84,487**; 2,097,152 − 1,484,487 =
  **612,665**; 702×19 + 11×18 + 702×4 + 11×2 = **16,366**; 409 × 32 =
  **13,088**.
- Checker: `surface-routes.test.ts`:64–101 reads `const denominator =
  pages.length` over `['/', POLARIS, TRAJECTORY, ORRERY]` = **4**, tests each
  page with `page.html.includes('class="epistemic epistemic-observed"')`, and
  `continue`s a page carrying neither — the legend alone satisfies it
  [Observed: file read this session].
- Lane B, read read-only from `origin/agent/syzygy-dov.17` at `4090f98`:
  `hoistedPerField` container mode gives `data-epistemic-label` **409**;
  `netSavingBytesTailnet` **188,902**; `textBytesRemoved` **25,397** with no
  per-field breakdown. The second (strict) mode in the same record gives 410 —
  the packet correctly says "container-mode".
- M2 is at **`f2f37dd`** this session (`git log --oneline -1` in the M2
  worktree and `origin/agent/syzygy-dov.2`), which is the head the packet's
  one dated exception names.
- Source citations re-read at HEAD and exact: `polaris.ts` 306–307 (the two
  `?? 'unstated'` mints), 346–361 (`claimStatesBlock`, freshness group at 357),
  506–510, 1307 (`.claim-tuple`), 1329 (`.proposal-label`);
  `design-tokens.ts` 46–55; `polaris-first-reading.test.ts` line 88 (the
  hard-coded `'unstated —'` term); `staleness.ts` 18.
- Contract and spec quotes re-verified verbatim against source, with the
  source's own emphasis and no additions: RFC2-10
  (`snapshot-and-evaluation-core.md` 209–223, **the full clause extent** —
  RFC2-11 begins after the next blank line), RFC2-25 (`rendering-vocabularies.md`
  153), RFC2-26 (:196), the sibling-states sentence (:169), RFC7-34
  (`rendering-and-surface.md` 241–243, front matter `applies_to: [polaris]`),
  CC-VIZ-1 (`performance-and-visual-discipline.md`:48), CC-VIZ-3 (:74),
  `trust-and-evidence.md`:101, POC-REQ-060 and its warrants block (spec
  955–964), POC-REQ-061's warrants block (999–1008), PWB-REQ-007 (439/443–446,
  Case and Falsifier bullets), PWB-REQ-016, PWB-REQ-020 (902, Observable and
  Falsifier bullets). Every retained segment matched as an exact substring.
- The 2026-09-02 authorization's escalation-trigger sentence quoted at Gate 3 is
  verbatim from `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`:88–94 [Observed].
- RFC 0009 front matter reads `applies_to: [orrery, machine-clients]`
  [Observed].
- Code-span path sweep over the packet (fenced blocks excluded, 50 path-shaped
  spans): every fully-qualified path resolves in the worktree; the 18
  "unresolved" spans are bare basenames used as shorthand after the full path
  appears earlier. **No Butlers repository path appears in backticks** — the
  only `butlers`-matching spans are the Syzygy `openspec/changes/polaris-project-wide-butlers-model/…`
  paths [Observed: denominator every backtick span outside fences].
- No manifest row, act argument or truncated signed digest is quoted anywhere
  in the packet, record or register; `check_governance.py` ends `0 FAIL`.

The measurement work remains exceptional. Every discrepancy below is in prose
that reasons about the repairs, not in a figure.

## Findings

### J1 — blocking — `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`:1575 against `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:279 and :741 — the H1 row asserts three repairs; two of them are not in the bytes

**Defect.** The review-3 section's H1 row is marked **CONFIRMED — REPAIRED**
and states three repairs. Checked one by one against the current record:

1. *"the field is rewritten to state RFC2-10's remedy at lines 220–222 and the
   three lawful arms"* — **true.** `vocabulary_versus_rendered.freshness_mint_hazard`
   (json :282) now carries the remedy, the three arms, and the withdrawn
   wording quoted and marked in place [Observed].
2. *"`closed_freshness_vocabulary_authority` is extended through the remedy
   sentence with the elision marked"* — **false.** json :279 still reads, in
   full: `RFC2-10, .syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md
   line 209: "Four values, closed. The list changes only by amendment to this
   RFC; no implementation may mint, spell, or force-fit a freshness value it
   does not carry."` The quote stops at the same place it always did, there is
   no ellipsis, and the remedy sentence is absent [Observed: the field read
   this session; literal comparison against the source at 209–223].
3. *"the two disposition rows that claimed the withdrawal was complete (packet,
   review-2 section; record `review2.repairs.G1`) are corrected to name the
   record as a fifth site"* — **half false.** The packet's own review-2 G1 row
   (:1515) is corrected and now names the record explicitly as a fifth site
   [Observed]. The record's `review2.repairs.G1` (json :741) is **not**: it
   still reads "'supplies no absence marker at all' withdrawn at all four
   packet sites and the register row" [Observed].

Limb 2 is precisely the field review 3 identified as the mechanism by which
the false universal survived review 2's pass ("the record's quote was never
extended the way Gate 2's was"). Limb 3 is the third consecutive recurrence of
one defect class: a disposition row asserting a completeness the evidence
record does not have (G1 asserted it, H1 found it false and re-asserted it,
J1 finds it false again). The questionnaire invariant this violates is the
same one both times — a contract claim anchored to a defined clause and
quoted, and a repair claim that must be true of the bytes it is published in.

**Repair.** Extend `closed_freshness_vocabulary_authority` through
`snapshot-and-evaluation-core.md`:223 or mark the truncation with `…`; correct
`review2.repairs.G1` to name the record as a fifth site; and restate the H1
row to match what was actually done. H1's verification verdict is **PARTIAL**,
not REPAIRED.

### J2 — blocking — `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:730 with :808 and packet :1579 — H5's corrected total reached the packet and not the record, and both artifacts say otherwise

**Defect.** H5's repair was to state 10 REPAIRED / 4 PARTIAL "in both the
packet and the record." The packet does (:1502–1511, with the denominator of
14 and the raw's internal disagreement disclosed) [Observed]. The record does
not: `review2.f_verification_against_review_1` (json :730) is still

```
{"REPAIRED": 9, "PARTIAL": ["F4","F6","F7","F12"], "NOT_REPAIRED": 0}
```

— 9 + 4 = 13 over a population of 14, the exact arithmetic H5 was filed about
[Observed: the field read this session].

Two separate assertions say it was fixed: the packet's H5 row (:1579) —
"Both now state 10/4, computed from the table" — and the record's own
`review3.repairs.H5` (json :808) — "10 REPAIRED / 4 PARTIAL stated in both
places, with the raw's own disagreeing totals disclosed."

I recounted review 2's F1–F14 table (`…-2-RAW.md`:459–474, one row per
finding, denominator 14) independently this session: F1 R, F2 R, F3 R, F4 P,
F5 R, F6 P, F7 P, F8 R, F9 R, F10 R, F11 R, F12 P, F13 R, F14 R = **10
REPAIRED, 4 PARTIAL, 0 NOT REPAIRED** [Observed]. The packet's figure is
right; the record's is the transcribed one, and verification rule 3 says
totals are computed.

**Repair.** Set the field to `{"REPAIRED": 10, "PARTIAL": [...4...],
"NOT_REPAIRED": 0, "denominator": 14}` with the raw's disagreement noted;
correct `review3.repairs.H5` and the packet's H5 row. H5's verification
verdict is **PARTIAL**, not REPAIRED.

### J3 — blocking — `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`:282 against packet :52 and `PENDING-OWNER-DECISIONS.md`:208 — the evidence record enumerates a different (b-i)/(b-ii)/(b-iii) than the packet and the register, on the one question the packet declares the owner's

**Defect.** Q2's freshness limb is the question the packet says twice it does
not resolve ("**This is the owner's question; this packet does not resolve
it.**"). The three arms are labelled identically in three artifacts and denote
different things in one of them.

Packet Q2 (:52), verbatim: "**(b-i)** the renderer supplies one of the closed
four (M2's Q7, recommending `stale` with the reason kept distinct);
**(b-ii)** the claim is held Unknown and the tuple is not rendered as though
it had a freshness state; or **(b-iii)** the condition is disclosed as a fact
of the render, in a carrier that is not `data-epistemic-freshness` and is not
dressed as a freshness state".

P-70 row (:208), verbatim: "(b-i) the renderer supplies one of the closed
four, which is P-69's Q7; (b-ii) the claim is held Unknown and not rendered as
though it had a freshness state; or (b-iii) the condition is disclosed as a
fact of the render outside the `data-epistemic-freshness` slot, never dressed
as a freshness state". **Packet and register agree clause by clause**
[Observed].

Evidence record `freshness_mint_hazard` (json :282), verbatim: "So arm (b) of
Q2 has three lawful readings for the freshness field - (b-i) render only the
four declared states and no absence, (b-ii) disclose the no-bound-declared
condition as a fact of the render beside the tuple, (b-iii) the disclosure
route with the absence named in the legend, the packet's recommendation".

The record's **(b-ii)** is the packet's **(b-iii)**; the record's **(b-iii)**
— "the disclosure route with the absence named in the legend" — appears
nowhere in the packet or the register and is in tension with the packet's own
Q5 constraint that the freshness table gets "four rows and **no** absence
row". An owner who opens the evidence record the P-70 row names by path for
the substance behind Q2 reads the recommendation `(b-iii)` as a different arm
from the one the row recommends, and reads a fourth description of the arm
space that no reviewed artifact carries. This is not a stale string: the field
was rewritten in this pass, after review 3.

**Repair.** Rewrite `freshness_mint_hazard`'s arm enumeration to the packet's
and the register's wording verbatim, or drop the enumeration from the record
and cite the packet's Q2 for it.

### J4 — non-blocking — packet :181–192, :52 (Q1), :1609 and record `cross_surface_population` — the population offered as POC-REQ-060's is one page wider than the requirement's own scope of quantification, and the requirement's denominator is never stated

**Defect.** POC-REQ-060's text, quoted by the packet itself at Gate 2 and
re-read at source (`three-surface-poc-experience/spec.md`:931–938): "The
**three surfaces** SHALL draw from one declared set of design tokens … Scope
of quantification: every epistemic encoding across the **three surfaces**." Its
Case: "a checker enumerates every epistemic encoding on **all three surfaces**
— the denominator is that population".

The packet's 1,087 is over **four** pages — home 35, trajectory 299, orrery
18, Polaris 735 [Observed: recomputed this session from the three capture
files and the Polaris capture]. Home is not one of the three surfaces. The
requirement's own population is therefore **1,052**, and Polaris's share of
it is **69.87%**, not the 67.62% the packet reports; neither figure appears
anywhere in the packet, the record or the register.

The packet's predicate is stated and its per-page table is exact, so the
reader can recover this — but the prose does not, and at :189 it calls Home
one of "the other three surfaces". Q1's recommended answer then sets the
requirement's "the denominator is that population" against the four-page
1,087 directly, and the funnel summary carries "a denominator of 4 pages
against a 1,087-member population" as the headline. That is the same
population-versus-denominator mismatch verification rule 4 names, on the
smaller scale, inside the finding that invokes rule 4.

It does not change any conclusion: 735 of the missing encodings are on
Polaris either way, and including home in slice 2's sweep is the better
engineering choice. It is a stated-scope defect, not an arithmetic one.

**Repair.** State both denominators — POC-REQ-060's three-surface 1,052
(69.87% on Polaris) and the four-page 1,087 the slice-2 sweep will use — and
say in one clause why the sweep is deliberately wider than the requirement.
Drop the phrase "the other three surfaces"
(wrapped across :190–191).

### J5 — non-blocking — packet :507–521 (Gate 2) against `PENDING-OWNER-DECISIONS.md`:208 — H6's disclosure reaches the packet and not the register row the owner rules from

**Defect.** H6's repair added to Gate 2 (:507–521) the measured fact that all 11
human-side Unknown claims have **no `tier` key at all** in the machine answer,
so Q2's arm (b) justification — "it keeps PWB-REQ-007's 'carry the closed
label, tier … that govern it' satisfied with a present field" — holds on the
human channel only. I re-derived it independently: 11/11 matched, 11/11 with
`epistemic` keys exactly `['freshness','label','reasons']`, machine-side tier
absent 12 of 1,149, `unstated` 0 times in the machine answer [Observed].

The packet calls this "a second, independent reason the owner is being asked a
real question rather than shown a formality" (review 3's words, adopted). The
P-70 row carries none of it: sweeping the row and the 21-line note for `tier
key`, `machine channel`, `api-poc` and `1,149` returns **0** in both
[Observed: literal `str.count`, denominator the row and the note]. The row
still states arm (b)'s justification without the qualification the packet
attached to it.

This is H3's defect class recurring at a different site: a repair that reaches
the packet and not the register. The register is the artifact the owner works
from.

**Repair.** One clause in the P-70 row's Q2 limb: that the tier field the
owner is asked to keep present has no counterpart in the machine channel for
those 11 claims, and that arm (b) therefore carries a parity question the
packet does not resolve.

### J6 — non-blocking — packet :1623–1630 (handoff) against :874–889 (slice 2) and Q6 — the recommended immediate run is conditioned on Q1, Q3 and Q4 but now depends on Q6 as well

**Defect.** H7's repair chose, for slice 2's one live negative-sweep positive,
to "pull slice 6's token change for that **one** rule forward into this slice:
`.proposal-label` moves to the `--proposed` token now". The `--proposed` token
is Q6's entire subject, and Q6 is one of the five questions the packet calls
"owner gates in the strict sense". Q6's alternative arm — "keep one token and
legend the reuse explicitly — lawful under CC-VIZ-1" — would make the
pull-forward wrong.

The handoff opens "**If Q1, Q3 and Q4 are answered as recommended:** … Run
slices 1, 2 and 4 under `syzygy-dov.3` immediately", then states the
`.proposal-label` dependency mechanically without saying that acting on it
presupposes Q6's recommended answer. Slice 2 does name the lawful alternative
(a declared, dated exception), so no arm is foreclosed and nothing unlawful is
proposed — but the condition line as written tells the owner three answers buy
the immediate run, when on the packet's own stated choice it is four.

**Repair.** Either add Q6 to the handoff's condition line for slice 2, or make
the declared dated exception the handoff's default and the token pull-forward
the Q6-conditional variant.

### J7 — editorial — packet :1575 — the H1 row's sweep figure is exact for the commit it was taken at and stale in the bytes it is published in, with no as-of marker

**Defect.** The H1 row reports: "Swept the packet, record and register for
`supplies no`, `no absence`, `not lawfully available`, `unlawful`, `no remedy`
and `supplies none`: **25 literal occurrences over 2,482 lines** across the
three files".

Re-run this session with those six literals over the three files: at
`b34fca7`, **25 occurrences over 2,482 lines** — exact. At `f35a25f`, the
commit the sentence is published in, **41 occurrences over 2,700 lines**
[Observed: Python `str.count` per term, denominator every line of all three
files, run at both commits]. The repair pass that wrote the sentence is the
pass that added the other 16 occurrences.

Nothing is misleading about the reasoning — the 16 additions are all the new
review-3 section's own lawful-arms and withdrawal-marker language — but the
figure reads as current and is not. This is the project's own recorded lesson
in miniature: a count over a population the current pass is still editing has
to be re-derived, never read.

**Repair.** Date-stamp the sweep ("as of `b34fca7`, the bytes review 3 read")
or re-derive it at the publishing commit.

### J8 — editorial — packet :21–23 — the H8 correction enumerates two commits; there are three at HEAD

**Defect.** The baseline bracket now reads "[Observed; corrected after
review 3, finding H8 — the worktree is two commits ahead of `a9f671e` at
`573abb0` then `b34fca7`, not at the same commit as stated before this
repair]". At `f35a25f` the worktree is three commits ahead. The load-bearing
clause survives and I verified it: `git diff --stat a9f671e..f35a25f` is six
files, 4,064 insertions, **0 deletions**, all of them this packet's own
artifacts, so every source citation is still at the baseline bytes [Observed].

This is the fifth iteration of the same pattern the packet itself diagnoses at
:1240–1246 for M2's head: a commit named in the commit that moves past it. The
prose remedy the packet adopted there — cite the invariant, not the hash —
applies here too.

**Repair.** "the worktree branches from `a9f671e` and carries only this
packet's own artifacts" — drop the commit enumeration, which is what the
sentence is actually asserting.

### J9 — editorial — packet :775–781 (Gate 3) — an `[Observed]` bracket whose last limb is a scope reading the packet labels `[Inferred]` elsewhere

**Defect.** Gate 3 asserts "**No slice crosses any of the six** [Observed: no
doctrine or contract text is edited; … and every slice implements behaviour
the signed change already requires]". The first five limbs are observations.
The sixth — "every slice implements behaviour the signed change already
requires", discharging the trigger "any scope beyond the signed change" — is a
reading, and the packet knows it: Gate 5 labels the parallel claim for the
same slices `[Inferred]` ("a tier or freshness treatment is an encoding of a
tuple field rather than of an epistemic label, so the new families sit
alongside the requirement rather than inside it [Inferred: this is the reading
this packet relies on]"), and names the condition under which it fails.

**Repair.** Split the label: `[Observed]` for the five textual limbs,
`[Inferred]` for the scope limb, with a pointer to Gate 5's stated reading and
its contrary condition.

## H1–H11 verification against the current bytes

Each re-derived from source or the retained captures this session, not taken
from the review-3 section's own account.

| H | Severity (review 3) | Verified verdict | Evidence |
|---|---|---|---|
| H1 | blocking | **PARTIAL** | `freshness_mint_hazard` (json :282) rewritten with RFC2-10's remedy, the three arms and the withdrawn wording marked in place — repaired. `closed_freshness_vocabulary_authority` (:279) **still stops at "…does not carry."** with no ellipsis and no remedy. `review2.repairs.G1` (:741) **still says "all four packet sites and the register row"**, naming no fifth site. The packet's H1 row asserts both as done — **J1** |
| H2 | non-blocking | **REPAIRED** | `review1.recommended_answers_changed.Q2` (json :674) now carries the in-place marker "(marker appended after review 3, finding H2; the superseded text above is kept, not deleted)" with the withdrawn wording preserved, matching the packet's own handling [Observed: field read this session] |
| H3 | non-blocking | **REPAIRED** | The P-70 row (:208) now ends "**P-69's Q3, Q5 and Q7 and this row's Q2 are one reading of one accepted clause, RFC2-10, and should be ruled together, not independently — and P-69's Q7 (`stale`) and this row's Q2 (`(b-iii)`) are not two compatible rulings on the same claims**". Collision item 3 (:1284–1305) restates the two recommendations as mutually exclusive rather than complementary, with both arms kept. Swept row and note for `together`: 3 hits in the row (0 before) [Observed] |
| H4 | non-blocking | **REPAIRED** | The collision section (:1239–1253) cites M2 by register row P-69 and the two shared files, with one dated exception naming `f2f37dd`. Confirmed current this session: `git log --oneline -1` in the M2 worktree and `origin/agent/syzygy-dov.2` both return `f2f37dd` [Observed]. Slice 6's two files (`polaris-reading.ts`:44, `polaris.ts`:506–510) are untouched by any M3 slice — `polaris.ts`:506–510 read this session |
| H5 | non-blocking | **PARTIAL** | The packet (:1502–1511) states **10 REPAIRED, 4 PARTIAL**, computed, with denominator 14 and the raw's three disagreeing figures disclosed — repaired, and my own recount of `…-2-RAW.md`:459–474 agrees exactly. The record's `f_verification_against_review_1` (json :730) is **still 9/4** — **J2** |
| H6 | non-blocking | **REPAIRED** | Gate 2 (:507–521) states the machine-side absence with its predicate and denominator. Re-derived independently: 11/11 Unknown tuple ids matched in `api-poc.json`; 11/11 carry `['freshness','label','reasons']` and no `tier`; 1,149 objects / 1,148 distinct ids; `unstated` 0 times [Observed]. It is a disclosure, not a resolution, as H6 asked. (Not carried to the register — **J5**) |
| H7 | non-blocking | **REPAIRED** | Slice 2 (:874–889) names `.proposal-label` as its one known live positive, with count 1 and depth 56.29% (both re-derived this session) and the served rule at `polaris.ts`:1329 (read this session), states the packet's choice to pull slice 6's token change forward for that one rule, and names the declared-exception alternative as lawful. The handoff (:1623–1627) carries the dependency. (Its Q6 dependency is undisclosed — **J6**) |
| H8 | editorial | **REPAIRED** | The baseline sentence (:21–23) no longer says "at the same commit"; it says the worktree branches from `a9f671e` with only this packet's artifacts on top, which `git diff --stat a9f671e..f35a25f` confirms (6 files, 0 deletions, all packet artifacts). (The bracket's commit list is one short at HEAD — **J8**) |
| H9 | editorial | **REPAIRED** | The review-2 section (:1489–1497) now reads "Its verdict word, copied exactly: **REVISE**. Findings by severity as the raw states them: 1 blocking (G1), 5 non-blocking (G2–G6), 3 editorial (G7–G9)", with the composite disclosed. `…-2-RAW.md`:567 is exactly `Verdict: REVISE` and the counts are at :564–566 [Observed]. The record's `verdict_word_copied_exactly` is `"REVISE"` with a separate note field |
| H10 | editorial | **REPAIRED** | Both block quotes now carry `…` between the retained bullets: PWB-REQ-007 (:464–477, ellipses at :470 and :474) and PWB-REQ-020 (:488–492, ellipsis at :489). All retained segments re-matched as exact substrings of the spec at 443–446, 452–455, 460–462, 915, 924–926 [Observed] |
| H11 | editorial | **REPAIRED** | The Gate 2 RFC2-10 quote (:575–589) now runs 209–223 inclusive and matches source under whitespace normalisation, with the source's own two bold spans and nothing added; RFC2-11 begins after the next blank line, so "the clause's full extent" (:591–592) is exact and "quoted in full" (:592, :618 and Q2) is now true. The orthogonality sentence is weighed against arm (b-ii) at :593–602, and correctly not against (b-iii) [Observed] |

Summary: **9 REPAIRED, 2 PARTIAL, 0 NOT REPAIRED**, over a denominator of 11.
Both partials are in the evidence record, and in both cases an assertion in the
packet or the record says the repair is complete.

## F and G findings — regression spot-check

I did not re-litigate accepted repairs; I checked that the bytes prior reviews
confirmed are still those bytes.

- **F1 / warrants**: both blocks read at spec 955–964 and 999–1008;
  POC-REQ-060's `contracts: [RFC6-18, RFC6-22, RFC8-31]` and POC-REQ-061's
  `[RFC7-34, RFC8-31, RFC9-48]` are as the packet states. No RFC9-46 bridge
  survives [Observed].
- **F2 / G7 / colour**: all pairs recomputed; "26.74 to two decimals, 26.7371
  computed" appears at 4 sites, no bare "below 26.74" survives [Observed].
- **F3 / sibling states**: RFC2-25:169 quoted with the source's emphasis;
  the three sibling states and `challenge-pending` each re-swept at **0** over
  the 1,481,819-character capture [Observed].
- **F5 / F10 / counts**: the 713/22 split and the 0/0/22/1 token-reuse counts
  re-derived exactly [Observed].
- **F8 / line ranges**: `claimStatesBlock` at 346–361 with the freshness group
  at 357, read this session [Observed].
- **F9 / G1 / RFC2-10 authority**: RFC2-10 is the named authority;
  `staleness.ts`:18 retained and labelled the implementation's echo [Observed].
- **F12 / G3 / added bold**: the RFC7-34 quote now carries only the source's
  own `**without colour, position, or layout**`; PWB-REQ-007, PWB-REQ-016,
  VIS-7, CC-VIZ-1, CC-VIZ-3, POC-REQ-061, RFC2-25, RFC2-26 and RFC2-10 quotes
  all matched their sources' emphasis exactly [Observed].
- **F13 / F14**: `design-tokens.ts` 46–55 is exactly the ten colour tokens;
  `polaris-copy.ts` 34–51 is the 15 state sentences plus three group labels
  [Observed].
- **G2 / preflight**: `polaris-first-reading.test.ts`:88 hard-codes
  `'unstated —'` in its required-terms list, as the packet says [Observed].
- **G5 / G8 / G9 / register**: the P-70 row reads "57.72% and 25.70%",
  `trust-and-evidence.md`:101 is anchored and marked "by analogy" with its
  actual subject stated, and Q3's arm (b) reads "at least 13,088 attribute
  bytes plus an unseparated text component" [Observed].

**No regression found.** Nothing review 2 or review 3 confirmed has moved.

## Q1–Q7

| Q | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | Yes on the facts; the population it sets against POC-REQ-060's "the denominator is that population" is one page wider than the requirement's own three-surface scope (**J4**) | Yes — a conformance ruling, and the packet states the other arm as a coherent recorded outcome rather than silence | Yes. The 713/22 split is presented as sharpening the finding, not softening it, and the "already conformant" arm is written out honestly | Yes, clause by clause |
| Q2 | Yes. Both mints shown at `polaris.ts` 306–307; tier fires 11, freshness 0; RFC2-25's rendering remedy and RFC2-10's disclosure remedy distinguished at their clauses; the PWB-REQ-007 tension put to the owner unresolved; the machine-channel tier absence now disclosed | Yes — the strongest gate in the packet, and the packet explicitly declines to settle it | Yes, and correctly `[Inferred]`. No arm is called unlawful; (b-i) is credited to P-69 and (b-ii) is kept live against the orthogonality sentence that argues against it | **Row yes; evidence record no** — the record enumerates a different (b-ii)/(b-iii) under the same labels (**J3**), and omits the machine-channel disclosure (**J5**) |
| Q3 | Yes. 409/713 re-derived from lane B's own record at `4090f98`, container mode named; 409×32 = 13,088 recomputed | Framed as a choice; both arms lawful, and the packet says arm (b) "spends a ruling the owner has not yet made" rather than pretending only one arm exists | Yes, with the discipline it costs stated as a hard requirement on every M3 sweep | Yes, and the register is stricter ("plus an unseparated text component") |
| Q4 | Yes. 126 tuples, all Observed, 0 disclosures in the 19.03% opening band, all re-derived | Yes — a design ruling on what the owner's first stop opens with | Yes, and the contrary arm ("leave the opening band positive") is stated as coherent, not strawmanned. CC-VIZ-3 is cited for its own subject and `trust-and-evidence.md`:101 is marked "by analogy" | Yes; the row's 25.70% names the claim to be surfaced and the packet's 25.55% names the first disclosure block — both correct for their referents |
| Q5 | Yes. 12 states in one collapsed disclosure, 0 with a visual encoding, 15 glossary sentences of which 9 unreachable — the sentences read at `polaris-copy.ts` 34–51 | Yes — a copy-and-encoding ruling that binds two later slices | Yes, and it carries three constraints forward rather than one, including M2's "mark, do not delete" shape | Yes |
| Q6 | Yes. 1 proposal label at 56.29% in `var(--unknown)`, 5 rules on that token for 4 meanings, 2 rendering 0 times; the closed-vocabulary disclaimer is quoted at RFC2-25:169 and the family explicitly mints nothing | Yes in form — but slice 2's H7 repair now implements the recommended answer's token for one rule ahead of the ruling, and the handoff does not disclose the dependency (**J6**) | Yes; the ΔE76 floor is stated over a named population with the full matrix in evidence, and the alternative arm is named lawful under CC-VIZ-1 | Yes |
| Q7 | Yes. The collision is exact (`polaris.ts`:357, `polaris-copy.ts` freshness sentences), M2's head re-confirmed at `f2f37dd`, and the P-69/P-70 coupling now states mutual exclusivity rather than complementarity | Framed as a sequencing choice, correctly | Yes. It does not smooth M2's `stale` and this packet's (b-iii) into a reconciled pair — it says granting both as recommended is not available and leaves the choice to the owner | Yes, including the mutual-exclusivity clause |

## Questionnaire invariant

- **Problem scope and recommendation hold against the project's shape and
  engineering bar** — yes. Every slice is app-local, rides the 2026-09-05
  continuation, and Gate 6 carries retained measurement, denominators,
  rule-6 mutants per guard branch, per-tuple parity and an independent review.
- **No owner trade-off smoothed into consensus** — yes, and this pass improved
  it: collision item 3 now states mutual exclusivity where it previously read
  as reconciled.
- **No lawful arm called unlawful** — yes in the packet and the register.
  The evidence record no longer forecloses (b), but describes three arms that
  are not the packet's three (**J3**).
- **Every substantive claim labelled** — yes with one exception (**J9**).
- **Contract claims quoted at a defined clause** — yes; every quote re-matched
  verbatim against source this session, and RFC2-10 now runs the clause's full
  extent. The one remaining unmarked truncation is in the evidence record
  (**J1**, limb 2).
- **Zero/all claims carry a predicate and denominator run this session** — yes
  in the packet; one published count is stale at its own commit (**J7**), and
  one denominator is wider than the requirement it is set against (**J4**).
- **Digests computed** — yes; every digest in this raw was computed with
  `wc -c` and `sha256sum` this session, and the packet's stated digests for the
  three retained raws match mine exactly.
- **No manifest or truncated signed digest quoted outside the raws; no Butlers
  path in backticks; every code-span path resolves** — all confirmed, with
  denominators above.
- **`python3 scripts/check_governance.py` ends `0 FAIL`** — confirmed:
  `32 OK, 20 WARN, 0 FAIL (52 checks)`.

## Summary

The packet's measurement work survives a fourth independent re-derivation with
no discrepancy: the tuple counts, the CSS-rule parse, the 1,087-member
cross-surface population, the first-reading boundary, the machine-channel tier
histogram, the full 36-pair ΔE76 matrix, the byte arithmetic, the lane B hoist
figures and every one of the nineteen contract and spec quotes. Nine of review
3's eleven findings are repaired in the bytes, and the two repairs that most
mattered — RFC2-10 quoted to its actual end, and the P-69/P-70 coupling stated
as mutual exclusivity rather than complementarity — are done well.

J1 and J2 share one shape, and it is the shape review 2 and review 3 each
blocked on: the evidence record is repaired last, or not at all, while a
disposition row asserts it was. `closed_freshness_vocabulary_authority` still
stops one sentence short of RFC2-10's remedy; `review2.repairs.G1` still says
the withdrawal reached four sites; `f_verification_against_review_1` still
says 9 REPAIRED over a population of 14. Each is a one-line edit. J3 is new
and is the one an owner would actually trip over: the
evidence record, which the P-70 row names by path as the substance behind Q2,
gives three lawful arms under the labels (b-i)/(b-ii)/(b-iii) that are not the
three the packet and the register give, with the recommended label `(b-iii)`
pointing at a different arm in each.

The rule for this packet, now paid for four times: **a repair pass is not done
when the packet is edited.** Sweep the record and the register for every site
before writing the disposition row, and write the row from the post-edit
sweep, not from the plan.

Findings by severity: **3 blocking** (J1, J2, J3), **3 non-blocking**
(J4, J5, J6), **3 editorial** (J7, J8, J9). Nine findings over three
artifacts.

Verdict: REVISE
