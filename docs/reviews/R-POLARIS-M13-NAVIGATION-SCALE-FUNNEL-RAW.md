# R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-RAW

Independent fresh-context review 1 (no prior review) of the M13 feature-
request funnel. Read-only session; one file written, this one.

Worktree: `m13wt`, branch `agent/syzygy-dov.13`, HEAD
`97b37ee4f09ffa502bf5985935733bc3ac3bb58a`. The diff of tracked names
between `a9f671e` and HEAD is exactly the two reviewed files, so every
source figure below is equally a figure at `a9f671e` [Observed].

Reviewed files, computed with `wc -c` and `sha256sum`, never transcribed:

- `docs/design/POLARIS-M13-NAVIGATION-SCALE-FUNNEL.md` — 97,146 bytes,
  sha256 `5171385698b7d29f1b8ca0b1bfeda3729c888f75c07c965ebdf8765e01c8d507`
- `docs/evidence/polaris-m13-navigation-scale-funnel-2026-09-15.json` —
  39,197 bytes,
  sha256 `1a47e98419447353d01cd75fd974aacc9c7cb8f0989e9745cf72065aca901f9c`

Captures read (read-only, byte counts confirmed on disk): post-trim
`polaris-direct.html` 1,478,637 B, `polaris-tailnet.html` 1,484,487 B,
`api-poc.json` 5,520,314 B; pre-trim `polaris-7478.html` 2,090,025 B. The
credential under the pre-trim capture's state directory was never opened. No
daemon was started. No provider was called. `git status --short` in the
worktree is empty at the end of this session, and nothing under `dist/` or
`node_modules` was touched (no build and no test suite was run: the packet
proposes no code change and its claim 11 asserts none).

`python3 scripts/check_governance.py` in `m13wt`, tail line read, not
grepped: `32 OK, 20 WARN, 0 FAIL (52 checks) — counts derived, not asserted`
[Observed]. That is the packet's own claim 11, reproduced exactly.

## Summary

This is an unusually well-measured packet. Every load-bearing population
figure, every capture row, every contract and act quotation, every spec
requirement-and-scenario line anchor, the whole 13-row collision table
including its B-only column, the register sweep, the 913/66 digest-binding
denominators and the two retained-review hashes re-derive **exactly** under
the stated predicates. The three corrections it makes to the dossier are all
real, all reproduced here, and the dossier is not edited.

The defects are in a narrow band: one code-quote line anchor that is off by
two and is recorded in the evidence file as "unchanged"; one absence figure
that is false by an order of magnitude because its population was silently
narrowed; one unmarked elision in a quoted test predicate, whose elided half
is exactly the container the packet's largest open slice restructures; a
systematic character-offset-for-byte-offset slip against the packet's own
stated convention; one "exactly two" enumeration that misses a third item;
and one requirement named in Gate 0 and tested nowhere. None of them changes
a recommendation, a lawfulness reading, or an answer to Q1–Q5.

## Findings

### F1 — non-blocking — `polaris-markdown.ts` anchors are off by two, and the evidence record certifies the error as re-derived

`docs/design/POLARIS-M13-NAVIGATION-SCALE-FUNNEL.md:271` ("At `a9f671e`,
`apps/three-surface-poc/src/polaris-markdown.ts` lines 156–160 read, in
full:") and `:172` ("The cause is one expression, … line 157:").

**Defect.** The five quoted lines of
`apps/three-surface-poc/src/polaris-markdown.ts` are **158–162**, not
156–160. Line 156 is a closing brace and line
157 is the heading regex `/^ {0,3}(#{1,6}) +(.+?)(?: +#+)? *$/`. The
expression `const level = Math.min(6, heading[1]!.length + 3);` is line
**159** [Observed, `sed -n '156,163p'` at HEAD, which equals `a9f671e` for
this file]. The quoted *bytes* are correct; only the index is wrong. The
same wrong anchor is carried at packet lines 546 (Gate 3 topology row, "lines
156–160"), 654 and 666 (Gate 4 slice 2, "line 157" twice, including mutant
(a)), and in the funnel summary as `polaris-markdown.ts:157`.

The aggravating part is in the evidence record: its dossier-difference list
carries, for the figure "polaris-markdown.ts heading expression", a dossier
value of 157-160 and an at-`a9f671e` value of "157-160 — unchanged", quoted
from its dossier-difference list. The packet re-derived the
dossier's anchor, found it "unchanged", and published that — but the dossier
was wrong and so is the packet. Every other line anchor in that list was
genuinely re-derived and corrected (818→835, 1530→378/1549, 1510-1538→1529-…).
This is the one row where the re-derivation did not happen.

**Repair.** 158–162 for the block; line 159 for the expression; correct the
evidence row to a real difference (dossier 157-160 → 158-162 at `a9f671e`).

### F2 — non-blocking — the digest-binding sweep's second clause is a false near-absence, produced by a substring that means "manifesto"

Packet lines 123–131 (Gate 0 bound-byte constraint (b)) and 1141–1146 (Gate 6
item 7): "Swept this session over the 913 tracked files under `.syzygy/`,
`openspec/`, `docs/` and `scripts/`: of the 15 implementation files in this
packet's candidate surface, **0** appear as a row of any of the 66 manifest-
named files in that population under a digest, and **2** appear as a path in
one evidence record".

**Re-derived.** 913 tracked files ✓. 66 files whose path contains "manifest"
case-insensitively ✓. 0 of the 15 surface files appears as a digest row of
any real manifest ✓ — the act claim stands and is the load-bearing one.

The second clause does not. Over `docs/evidence/` in that same 913-file
population (96 records), **13 of the 15** surface files appear as a path, in
**20 distinct records**; `apps/three-surface-poc/src/polaris.ts` alone
appears in 18, `polaris-project-shape.test.ts` in 9,
`polaris-first-reading.test.ts` in 4 [Observed, Python `in` test over the
literal `apps/three-surface-poc/src/<basename>` against every tracked file
under `docs/evidence/`]. The packet's "2 … in one evidence record" is what
you get if the second clause is silently restricted to the 66 "manifest-
named" files — where the only match is
`docs/evidence/polaris-manifesto-example-mutation-2026-09-09.json`, a file
the predicate catches because "manifest" is a substring of "manifest**o**".
It is not a manifest at all. A denominator artifact has been published as a
finding about the world.

**Why it matters beyond arithmetic.** Those 20 records are retained mutation
runs and measurement records. AGENTS.md already records that the one dated
mutation-kill run covering `polaris.ts` is bound to a hash the file no longer
matches; the packet raises exactly that obligation for the fidelity review in
Gate 0(c)/item 8 and does not raise it for any of the 20. A reader of item 7
would conclude two files carry evidence-record exposure. Thirteen do.

**Repair.** State the second clause's population explicitly, give the real
figure over `docs/evidence/`, and say (as item 8 does for the fidelity
review) which of those records an implementing bead must re-run or re-anchor.

### F3 — non-blocking — the parity-sweep predicate is quoted with an unmarked elision, and the elided half is slice 5's own container

Packet lines 694–700 (Gate 4 slice 3, "Two guardrails this slice must hold,
both from AGENTS.md"): the file
`apps/three-surface-poc/src/polaris-parity-sweep.test.ts` "line 494 finds
class tables by `section.inner.includes('<tbody>')`".

**Defect.** Line 494 reads, in full:

```
    if (section.inner.includes('<tbody>') || section.inner.includes('<ul class="item-list"')) classesWithTables.push(section.value);
```

[Observed]. The quotation drops the second disjunct with no
elision mark. Under verification rule 8 a predicate quoted at half its length
is not the predicate.

**Why the missing half is the important half.** Lane A converted five of the
eight classes to `<ul class="item-list">` (the packet's own Measurement 5
table says so), and the class-population detector now keys off that literal
as well as `<tbody>`. Slice 5 is the slice that restructures precisely those
five lists — arm (a) nests a remainder disclosure inside them, arm (b) adds a
control and a count element beside them. Yet the AGENTS.md "Where a trimmed
byte may not come from" guardrail (AGENTS.md line 296 at `a9f671e`) appears
in this packet only under slice 3, and slice 5's oracle and its four rule-6
mutants never name the class-population detector at all. The elision is what
makes the gap invisible: with the full line quoted, the reader sees that
slice 5 touches the same predicate slice 3 is being careful about.

For the record, I checked the adjacent hazard and it does **not** hold: no
item entry carries an `id` (0 of 409 `data-polaris-item` elements have one,
0 are `href="#…"` targets), so arm (a)'s nested disclosure does not trip the
fragment-target guardrail [Observed, post-trim capture].

**Repair.** Quote line 494 whole; add the guardrail paragraph and one mutant
to slice 5 over the class-population detector.

### F4 — non-blocking — character offsets published as byte offsets, against the packet's own stated convention

The packet states at line 21: "A byte count is the UTF-8 length." Four
figures are not.

| Figure | Packet | UTF-8 byte offset |
|---|---:|---:|
| Catalog-heading cut, pre-trim (line 364) | 912,381 | **912,823** |
| Catalog-heading cut, post-trim (line 364) | 281,945 | **282,383** |
| h3 "V1 scope" (line 283) | 88,024 | **88,131** |
| h6 "Core Infrastructure" (line 283) | 88,501 | **88,608** |

All four are character indices [Observed; the post-trim capture is 1,478,637
bytes over 1,475,969 characters]. The two line numbers attached to the cut
(1,039 pre / 1,031 post) are right. The pre-trim pair is inherited verbatim
from the dossier's F3, which made the same slip.

**The corollary is the packet's own best finding, undiagnosed.** The packet
records (evidence record line 58) that "the inherited posture file states
2,087,400 bytes for this file; the file on disk is 2,090,025", and rules for
2,090,025. That is **correct**: 2,090,025 is the byte count and 2,087,400 is
that same file's *character* count, to the byte [Observed, `len(h)` vs
`len(h.encode())`]. Saying so would retire the discrepancy instead of
carrying it as an unexplained difference — and would have caught the four
offsets above in the same pass.

**Repair.** Recompute the four offsets in bytes, or relabel them character
indices; add the one-sentence diagnosis of 2,087,400.

### F5 — non-blocking — "exactly two affordances stop working" undercounts by one

Packet lines 407–414 (Measurement 6): "exactly two affordances stop working:
the drawer no longer opens itself on a wide screen, and the expand-all button
becomes an inert control."

**Defect.** A third does. `SECTION_NAV_SCRIPT` (`polaris.ts` 1243–1260)
opens a component guide's `<details>` when the location hash names that
guide — on click, on `hashchange`, and at `DOMContentLoaded`. Without script,
a reader who follows any `#polaris-guide-…` link, including the ten the
outline itself emits, lands on the guide wrapper with its disclosure still
closed and must find and operate the summary [Observed, script source plus
0 `<details open>` in the served markup]. A fourth behaviour, the
`aria-current="location"` update on scroll, is also lost, though it is a cue
rather than an affordance.

The conclusion the measurement exists to establish — "Polaris requires no
script to be read" — survives intact: nothing becomes unreachable, and no
region renders empty, so POC-REQ-022's bar is still met. But "exactly two" is
a zero/all-shaped enumeration and it is wrong as stated, in the one
measurement Q1 rests on.

**Repair.** Say three, and keep the conclusion.

### F6 — non-blocking — POC-REQ-030 is named in Gate 0 as constraining and is tested nowhere, and it is the requirement nearest slice 5's arm (c)

Gate 0's Specification row (packet line 114) lists the constraining
requirements as "PWB-REQ-011, 012, 016, 020; POC-REQ-021, 022, 030, 061".
The literal string "POC-REQ-030" occurs **0 times** in the packet and **0
times** in the evidence record [Observed; it is named only in that
continuation form — which is itself the AGENTS.md continuation-form lesson
arriving in a packet that otherwise sweeps carefully].

**Defect.** POC-REQ-030 — "Polaris renders a multi-page long-form narrative
from intent facts", spec line 496 — has a requirement text ("in multiple
titled pages/sections"), an Observable limb at line 507 reading "a
paginated/sectioned document whose sections carry entity references", and a
scenario "Narrative covers the intent entities" at line 518. Gate 5's
RFC2-26 table tests all five slices and never reaches it. Its slice 5 row
instead says "No scenario in either specification describes a windowed or
paged catalog route", which is narrowly true — POC-REQ-030's is an Observable
limb about document layout, not a windowed route — but the packet's own
keyword table counts **2** "paginat" hits in the POC tree and then reads only
"details", "outline", "source record" and "filter", leaving the two hits
nearest to slice 5's own name unopened. Both are POC-REQ-030's (design.md:25
and spec.md:507) [Observed].

This cuts both ways for the owner and the packet does not say so: if
POC-REQ-030's "multiple titled pages/sections" already contemplates a
sectioned Polaris, arm (c)'s windowed route has a requirement to argue from
after all, and Q1's third arm is stronger than the packet's own Gate 5 row
allows.

**Repair.** Add a POC-REQ-030 row (or one sentence per slice) to Gate 5, read
the two "paginat" hits alongside the four terms already read, and say what
POC-REQ-030 does and does not reach for arm (c).

### F7 — editorial — a heading-attribute sentence that is over-broad and contradicts the packet's own Gate 1

Packet line 658 (Gate 4 slice 2): "The change is invisible to every parity
marker: heading elements carry no `data-parity-field`, no `data-claim-id`
and no id."

Re-derived over the post-trim capture's 80 heading tags: 0 carry
`data-parity-field`, 0 carry `data-claim-id` — the load-bearing half is
exact — but **51 carry an `id`**, including the 39 h3s that Gate 1 (packet
line 160) says have one each [Observed]. The 18 bare markdown-derived
headings slice 2 actually retypes carry no attributes at all, which is the
true and sufficient claim.

**Repair.** Scope the sentence to the 18 markdown-derived headings.

### F8 — editorial — the ≤78-column self-audit mischaracterises at least one of its 20 exceptions

Packet lines 1174–1177: "**20** lines exceed 78 columns outside fences,
tables, block quotes and headings, each of them a single unbreakable code
span or quoted literal."

The count is exactly right: 20 [Observed, reproduced with the stated
exclusions]. The characterisation is not. Line 1166 is ordinary prose at 90
columns — "packet's two files appears in any finding. No test suite was run:
this packet proposes" — carrying no code span and freely reflowable. (Line
1016 is prose plus a short span and could also rewrap.) Every other exception
I checked is genuinely a single long path, digest-free filename or quoted
literal.

**Repair.** Rewrap line 1166 and restate the sentence as 19, or say "all but
one".

### F9 — editorial — the decisions denominator is undisclosed, and Gate 6 restates a filtered zero as a raw zero

Q1 (packet line 43) gives "the **67** of `.syzygy/governance/decisions`" and
Gate 6 item 3 gives "'No decision constrains client-side scripting' is 0 over
67 decision files."

67 is the count of **top-level** files in that directory; the tree holds
**73** tracked files, the difference being the six under
`decisions/launch-gate/`, excluded with no predicate stated [Observed].
Re-run over all 73 with a case-insensitive `script|javascript|progressive`
pattern: **9** matching lines, **0** of them constraining Polaris's own
scripting (they are digest-generation prose, a `script --flag` shell lesson,
a progressive-disclosure refactor row, and two HISTORY notes). So Q1's
careful wording — "**0** sentences constraining the page's own scripting" —
survives exactly. Gate 6 item 3's "0 over 67 decision files" does not: it
reads as zero hits, and there are nine.

**Repair.** State the predicate (top-level, or all 73) and keep Gate 6's
restatement in Q1's filtered form.

### F10 — editorial — three line-range slips

- `tableRegion` is `polaris.ts` **159–161**, not "lines 158–160" (packet line
  703). Line 158 is the last line of its doc comment.
- `depthNav` runs **1529–1558**, not "1529–1556" (packet lines 351, 545,
  funnel summary). 1556 is the last content line of the template, 1557 closes
  the `<nav>` and 1558 closes the function. The correction the packet makes to
  the dossier (1510-1538 → 1529-…) is right in direction and short by two at
  the end.
- "The helper has **5** call sites in `polaris.ts` — its own definition at
  377 plus lines 533, 552, 836 and 1081" (packet line 232): there are **4**
  call sites over 5 lines. The packet discloses the composition in the same
  breath, so this is wording, not a miscount.

### F11 — editorial — Q3's first sentence conflates the implementation copy table with PWB-REQ-012's closed role set

Q3 (packet line 45): "Those two strings are rows of the closed copy table
PWB-REQ-012 governs."

PWB-REQ-012 (spec line 679, read in full) closes a set of **roles** —
`project-fact`, `epistemic-disclosure`, `action-label`, `scope-instruction` —
and then imposes word limits, a prohibited-term list and two cardinalities.
It nowhere declares a closed set of strings, and it does not govern
`POLARIS_COPY`, which is Syzygy's own implementation table — as the packet's
own act table says two pages later ("the copy table is implementation",
packet line 552). Q3's counter-argument states the relationship correctly
("declares a *closed* set of roles"); only the opening sentence overstates.
The question remains a legitimate ask, because the hand-typed oracle's reach
predicate is what slice 1 leans on.

Credit where due: the packet catches the *real* PWB-REQ-012 hazard in slice
1, at Gate 4 item (b) — a Butlers path interpolated into a label could carry
`document` or `section`, which the prohibited-term regex would miss because
`polaris-copy.test.ts:132` gates on `frame.kind !== undefined` and a summary
has no kind. That is an accurate reading of line 132 and the right
instruction to the implementing bead.

## Q1–Q5

| Q | Scope truthful? | Genuine gate? | Recommendation follows? | Lawful arms all named? |
|---|---|---|---|---|
| Q1 | **Yes.** 1 `<script` post-trim, 2 pre-trim, 0 `<noscript>`, Orrery's at `orrery.ts` 144–146, all re-derived | **Yes.** Whether the page may host script a reader does not need is a posture question, and arm (b) creates the first hidden content on the page, which is a new invariant a checker must hold | **Yes**, and the counter-argument is correctly called the strong one | **Yes** — (a) no script, (b) progressive enhancement, (c) route paging; none called unlawful; default (nothing ships) stated and lawful. See F6: arm (c) may have more requirement cover than the packet allows |
| Q2 | **Yes.** `polaris.ts:836` returns one `<tr>` per source and `:835` builds the disclosure inside its second cell — verified at source; "details" is 0 over 7+15 files — verified | **Yes** on the comprehension half (removing a reading level is the owner's to weigh). The CC-REV-2 half is nearer a delegate's call given the 0 hits, and the packet says so while still routing the ruling to the owner — erring toward asking, which is the right error | **Yes**; the 53,376 B scaffolding figure re-derives exactly (278 × (182 + 10)) | **Yes** — hoist, or half-hoist keeping the level; default is the conservative arm |
| Q3 | **Yes** on measurement (129/134, 278 summaries, 386 links). **Overstated** on framing — see F11 | **Weakest of the five**, and legitimate: the oracle is hand-typed and the packet changes what "reached" means | **Yes.** The suffix form is admitted by `polaris-copy.test.ts:308`'s `startsWith` limb, verified verbatim | **Yes** — inherit, or rule it a vocabulary change through CC-REV-2 first |
| Q4 | **Yes, exactly.** `RFC-0007-0009.md:175` carries `RFC9-13.c1`, applicability cell "No camera/filter/bookmark state", verdict `believed-not-applicable`; that file is one of the eleven rows the 2026-09-05 act signed, and the act record says all eleven were verified against the frozen subject — all confirmed at source | **Yes.** A bound row's standing judgment is an owner's, not a delegate's | **Yes.** Stateless keeps the row true by construction | **Yes** — stateless, or stateful through CC-REV-2 and a new act, which is what the continuation act's own lines 138–139 require; default (nothing ships) lawful |
| Q5 | **Yes.** The escalation-trigger sentence is quoted **verbatim and complete** at `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` 150–156; the 2026-09-02 point 1 at 50–52 and the continuation point 3 at 110–114 are exact; the "does not authorize" list is at 125–146 as stated | **Yes** for slices 3 and 5 | **Yes**, and the packet declines to choose between the two readings, which is the correct posture for a delegate | **Yes.** Both readings stated, neither called unlawful, default (1/2/4 proceed, 3/5 hold) lawful |

No owner trade-off is smoothed into consensus language anywhere in the five;
each carries a stated counter-argument and Q1's is explicitly ranked above
its own recommendation.

**"Decided in this packet, not put to the owner" (packet line 49).** Each of
the four is a delegate's to make, and no owner question is hidden in them:

- The prerequisite correction *escalates* slice 5 rather than deciding it.
- **Heading normalization** is ordinary engineering, and the sweep that
  establishes it re-derives exactly: 0 matching lines over the 7 POC files,
  0 over the 6 doctrine files, **16** over the 15 PWB files, and I read all
  sixteen — every one is about the Butlers source grammar (spec.md 32–57 and
  501/508, design.md 98/102), none about a rendered level. PWB spec line 57
  is exactly as quoted and sits inside the extraction bullet list at 36–62.
  Heading levels carry no parity marker (F7 notwithstanding). Delegate's.
- The three dossier corrections are measurement corrections, all three
  reproduced here, and the dossier is not edited — `git diff a9f671e 97b37ee`
  is the two packet files and nothing else.
- The one decision I looked at hardest is **"no command palette"** (packet
  line 761), because the dossier's S2-M4 proposes "a jump list / command
  palette" and the packet keeps half. It is adequately handled: the packet
  names it as a packet decision, gives the reason (a palette makes Q1 arm (b)
  a prerequisite for navigation rather than convenience), and routes the
  owner to Q1 arm (b) to overrule it. Disclosed, reversible, and cheaper than
  the alternative.

**The prerequisite line.** The dossier's machine record gives M13
`"prerequisite": "none"` over all five moves, and S4-M6's `slice_plan` opens
with exactly "Confirm the page's no-required-JS posture before adding
client-side filtering" — both verified in
`docs/pursuits/2026-09-13-vision-pursuit-data.json`. The packet's reading —
true as the dossier meant it, incomplete as a reader would take it, corrected
for slice 5 — is fair, and slice 5's correction is the right one: the
`RFC9-13.c1` row is bound, it may not be edited, and the packet asks rather
than rules. It rules where it should rule and asks where it should ask.

## Measurements

| Claim | Re-derived? | My figure |
|---|---|---|
| `polaris-copy.ts` 129 / 134 literals | exact | both quoted lines are byte-identical |
| `label.source-record`: 2 lines, 2 files; `label.exact-text`: 3 lines, 2 files; denominator 86 `.ts` files | exact | 86/86 files are `.ts`; 129+835; 134+378+1549 |
| `exactTextLink` "5 call sites" at 377, 533, 552, 836, 1081 | lines exact; wording loose | 4 call sites over 5 lines (F10) |
| `polaris.ts:836` returns one `<tr>` per source; `:835` builds the disclosure inside it | exact | quoted opening is byte-identical |
| `polaris-markdown.ts` "lines 156–160", expression "line 157" | **no** | block is 158–162; expression is 159 (F1) |
| `polaris-reading.ts:112` synthesizes `'### '` | exact | line 112 ends as quoted |
| `depthNav` head 1529, sidebar call 1629 | exact | function closes at 1558, not 1556 (F10) |
| `SECTION_NAV_SCRIPT` at 1232–1289; 5 behaviours; 1 `expand-declaration` | exact | all five present; 1 instance on the page |
| Populations, pre-trim: 353 details / 271 source-record / 271 summaries / 372 links / **185** distinct / 1,061 hrefs / 1,7,39,19,0,15 / 4h4+15h6 bare / 10 tables / 10 tbody / 2 script / 0 noscript / 0 open / 10 tabindex | **every row exact** | identical |
| Populations, post-trim: 359 / 278 / 278 / 386 / **192** / 1,089 / 1,7,39,19,0,14 / 4h4+14h6 bare / 5 / 5 / 1 / 0 / 0 / 5 | **every row exact** | identical |
| Tailnet form agrees on every row; 5,850 B larger | exact | 1,484,487 − 1,478,637 = 5,850 |
| `data-polaris-item` 402 pre / 409 post | exact | the plural `data-polaris-items` (8) is correctly excluded |
| Per-class items and forms (7/13/65/87/6/32/185→192/7; five lists post-trim) | exact | bounding by `id="polaris-class-…"` reproduces every cell |
| 5 post-trim tables: 8 / 14 / 66 / 279 / 8 `<tr>` | exact | identical |
| 80 headings post-trim; 3 adjacent skips; h3→h6 is V1 scope → "Core Infrastructure"; h4→h6 pair; h6 predecessors 1 h3, 1 h4, 12 h6 | exact | identical; 81 headings pre-trim |
| h6 split 9 under v1-scope, 5 under the passages block | exact | 9 + 5 = 14, by anchor |
| `api-poc.json`: 6 strings carry a markdown heading, 1 distinct value, `projectAccount[4]`, 9 lines all at depth 3 | exact | identical; file is 5,520,314 B |
| depth nav 8,746 B direct / 8,761 tailnet; 35 anchors = 2 + 33; 7/4/5/10/1/5/1 | **every figure exact** | identical |
| 11 of 39 h3 ids are nav targets, 28 are not; all 7 h2 ids are | exact | identical (the 11th is the quick-link, outside the drawer) |
| Tab stops: 172+53+3 = 228 pre, 172+52+2 = 226 post | exact, addend by addend | identical |
| Focusable: 9+53+0 = 62 pre, 9+52+0 = 61 post; 163 of 172 anchors inside closed disclosures | exact | identical, with the summary exemption as stated |
| Cut at "byte 912,381 / 281,945", lines 1,039 / 1,031 | lines exact; offsets are characters | 912,823 / 282,383 bytes (F4) |
| Architecture group: 89 anchors, 2 distinct hrefs, one accounting for 88, identical on both captures | exact | identical |
| Slice byte estimates: 13,010 / 17,874 / 0 / −45,800 / +5,479 / net −9,437 | arithmetic consistent; means exact | path mean 43.83, identity path-part mean 43.31, full identity mean 159.31, scaffold mean 182; 278×192 = 53,376 exactly. Slice 4's 5,479 sits between 28×195.3 and 28×196 |
| Ceiling arithmetic: 2,097,152; headroom 612,665; target 84,487 away | exact | both differences check; the lane A record carries 612665 and 84487 |
| Keyword sweep, 14 terms × 3 trees, denominators 7 / 15 / 6 | **every cell exact** as a per-line count | identical; the unit (lines, not occurrences) is not stated in the table |
| "details" 0 and "outline" 0 across both spec trees and doctrine | exact | 0/0/0 both terms |
| 2 "source record" and 12 PWB "filter" hits are all in coverage files | exact | RFC4-5 row; RFC6-15/16/22/23 and RFC9-13.c1 |
| Heading sweep: 0 POC / 16 PWB / 0 doctrine, all sixteen about the Butlers source | exact, and I read all sixteen | identical |
| Decisions: 67 files, 0 constraining sentences | conclusion exact; denominator narrowed silently | 73 tracked, 9 hits, 0 constraining (F9) |
| PWB spec: 17 requirements, 31 scenarios, 1,152 lines | exact | identical |
| POC spec: 24 requirements, 24 scenarios, 1,008 lines | exact | identical |
| PWB-REQ-001@69, 003@160 (scenario 184–189), 007@439, 011@632 (651, 657), 012@679 (705–710), 016@864 (885–889, text 868–870), 020@902 | **every anchor exact**, every quotation byte-identical | identical |
| "the 5 scenarios under PWB-REQ-001/003/007/011 are at 98, 184, 470, 651, 657" | exact | identical |
| PWB spec line 57 inside the grammar bullets 36–62 | exact | identical |
| POC-REQ-021@417, 022@456 (scenario 478–483), 061@966 (scenario 993–997) | exact, quotations byte-identical | identical |
| RFC2-26 at line 196 under the `###` heading at 194; "binds the whole RFC 0002 package" at 219–220; both paragraphs, no elision | **exact — whitespace-normalised string equality against lines 196–220** | identical |
| RFC7-34 at line 241; RFC9-13 at line 442, both sentences | exact | identical |
| `RFC9-13.c1` at coverage line 175, cell "No camera/filter/bookmark state", `believed-not-applicable`; bound by the 2026-09-05 act's eleven-row manifest | exact | act record confirms all eleven rows verified |
| Act quotations: 2026-09-02 point 1 at 50–52; continuation point 3 at 110–114; exclusions 125–146; triggers 150–156 | **every anchor exact**, triggers verbatim and complete | identical |
| VIS-1 82–95, VIS-2 96–106, VIS-3 108–121, VIS-5 141–160, VIS-7 183–193, all quotations | exact | identical |
| 913 tracked files; 66 manifest-named; 0 surface files as digest rows | exact | identical |
| "2 appear as a path in one evidence record" | **no** | 13 of 15, in 20 records (F2) |
| `polaris-reading.ts` and `polaris-reading-plan.ts` still hash to the retained review's values; `polaris.ts` no longer does; verdict PASS | **exact** — both recomputed and matched, the third recomputed and did not; no digest reproduced here | identical |
| Collision table: 13 rows, each head, each A, each B, each B-only cell | **every cell exact** | heads 4090f98, f2f37dd, 6574600, 63b8e33, ba9ca61, 83c9f60, f97baf4, bce9039, 65de02b, 95f31cb, bbd6837, 49b70bc, all as expected |
| "predicates disagree on 7 of 13 rows" | exact | M1, lane B, M2, M3, M4, M5, M12 |
| `polaris.ts` by 11 of 13, `polaris-copy.ts` by 7, `polaris-source.ts` by 5, `design-tokens.ts` by 4; M8 on 10, M3 on 7 | **every figure exact** | identical |
| Register: 27 rows in each of the twelve, 26 here, exactly one row at or above P-68 in each; P-68…P-79 as listed | **exact** | identical; P-80 is consistent — the maximum anywhere is P-79 |
| Pre-trim capture 2,090,025 B on disk vs 2,087,400 inherited | **the packet is right** | 2,090,025 bytes = 2,087,400 characters (F4) |
| Conventions: 1,209 non-fence lines, 0 odd-backtick, 20 over 78 columns, 232 distinct code spans, 15 with `/` unresolved | **every figure exact** | identical, including the 15th (a template fragment inside a fence); the characterisation of the 20 is not (F8) |
| `check_governance.py`: 32 OK, 20 WARN, 0 FAIL over 52 checks | exact | identical, tail line read |

**Two predicates, not three.** The prompt for this review describes a
predicate A defined as `git diff --name-only a9f671e <sibling HEAD>` against
the 15-file surface, and a B split into full-path and basename forms. The
packet publishes **two** predicates, both over sibling *packet text*
(packet lines 1008–1014), and it discloses the limitation itself under "Not
verifiable this session": the table is computed over packet text, not over
branch diffs. I ran the branch-diff predicate anyway as an independent check:
**every one of the twelve sibling branches changes 0 files under `apps/` or
`packages/`** [Observed, `git diff --name-only a9f671e HEAD -- apps packages`
in each worktree]. So today's file-level collision is empty and the packet's
table measures prospective collision, which is the useful thing to measure
and is labelled correctly.

**Sequencing.** Lane A/lane B, M5, M9, M10 and M14 are each stated fairly and
none re-asks a sibling's owner question: lane B stays under P-68, M5 under
P-72, M9 under P-75, M10 under P-77, and the packet forecasts P-80 for its
own five rather than claiming any sibling's. M14 is correctly called a
sequencing note rather than a collision, and its consequence — that slice 1's
uniqueness sweep must read its denominator off the page rather than from a
constant — is the right instruction.

## What a fresh reader would still ask

1. Slice 3's "−45,800" is the only slice byte figure carrying an [Inferred]
   tag. Slices 1 and 4's figures are derived exactly the same way — a
   measured mean times a measured population, against a render that does not
   exist yet — and the closing sentence labels them "[Observed] for every
   measured addend". The addends are observed; the products are not. Label
   all four the same way.
2. Gate 4 slice 3's mutant (b) is a self-test of an existing guard and says
   so: "if hoisting an attribute onto the `<table>` tag does not fail the
   reachability assertion, the assertion is the defect and must be repaired
   before the slice lands." That is the right instruction and it is the best
   single paragraph in the packet.
3. Every code-span path in the file resolves except the 15 the packet itself
   enumerates, and all 15 are genuinely non-paths (F4's count aside, the
   enumeration is exact). No observed-repository path is backticked anywhere
   in the file [Observed, checked span by span]. No manifest digest, act
   argument or truncated signed digest is reproduced.

Verdict: CONFIRM WITH EXCEPTIONS
