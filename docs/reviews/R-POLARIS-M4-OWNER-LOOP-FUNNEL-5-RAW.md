# R-POLARIS-M4-OWNER-LOOP-FUNNEL — review 5 (raw, retained verbatim)

Independent fresh-context review. Read-only: no repository file was edited,
no state-changing git command was run, no bead was written, no daemon was
started, no network was used, and the observed repository was never read.
The only file written is this one.

**Worktree and commit.** `agent/syzygy-dov.4` at
`e134a12646cc1fda1ba5cdbb6c5cb37d2eed3a5a`, working tree clean at review
time.

**Files reviewed** — bytes by `wc -c`, digests by `sha256sum`, both computed
this session, never transcribed:

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` | 190003 | `403def26d19e348e5b29f8874ef49f636d26de7de80fa0c05aaca7ab00362bad` |
| `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json` | 60920 | `30b2b2cd27b8646eb5732d6007e4c78d9cad57330ef663e45a7b84c9fa21fbe7` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 40852 | `751d3edbed9573c5f5d43bb1d2a38ad4aa8bf53ed01c8d9139003cecf41f45f3` |

**Retained prior raws, re-hashed this session** — all four match the figures
the packet publishes for them, value for value:
`R-POLARIS-M4-OWNER-LOOP-FUNNEL-RAW.md` 47636 /
`6983034196c706c213e2a939e0ca7dfe4c3f75f958378403fbd115112c2966ec`;
`…-2-RAW.md` 39050 /
`a7b3782882e41cf954e1dda326f502e20eceea4acd05732625de9f9ee2654649`;
`…-3-RAW.md` 31656 /
`ebce963f86f302940cc78f98dbe91325ae5c7b0ffa88e423b1fe05669035ccfe`;
`…-4-RAW.md` 37790 /
`5f3e9c458b9b2cc7d0372a7e22ef25e7cc0e72bd1fa1c3c003448acc7af17783`.
The three predecessor-commit digests the packet publishes were recomputed
with `git show <commit>:<path> | sha256sum` and all three match: `6218726`
116002 / `95e72b30…d5b`, `f911a45` 139094 / `09116fcf…750`, `181797a`
162860 / `267278fa…411` (full values verified; abbreviated here only in this
sentence, and each is quoted in full in the packet itself).

**Captures re-hashed this session** — all five match the packet's provenance
table: lane A tailnet `e8a04b46…0111` (1,484,487 B), lane A direct
`2fecdd01…a094` (1,478,637 B), pre-lane-A home `c2fd6d1a…fca`, Trajectory
`fd802531…dde`, Orrery `e3ae5b79…afe`.

**Invariants.** `python3 scripts/check_governance.py` ends
`32 OK, 20 WARN, 0 FAIL (52 checks)`. Every code-span path in the packet
that is path-shaped resolves on disk (sweep over all backticked spans
matching a `/` and a known extension; denominator 0 unresolved). No
non-fence line in the packet carries an odd backtick count, so no code span
is broken across a reflow. No manifest row or truncated signed act digest is
quoted; no observed-repository path is backticked.

---

## Findings

### K1 — blocking — the J2 repair never reaches the packet's operative texts: the funnel summary, the sequencing order, Q7's own bolded recommendation and the handoff all still carry the pre-review-4 answer

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:108`, `:1477-1481`,
`:1817-1822`, `:1862-1864`.

**Defect.** Review 4's J2 changed a recommended answer: slices 4 and 5 no
longer ride the audit-finding reading alone, Gate 3's rows 4 and 5 were
widened from "**No**" to "**No act found for the continuation itself; an
RFC2-26 gate is open — see Q7**", and Gate 5 gained "The RFC2-26 test for
slices 4 and 5". That repair reached Gate 3, Gate 5, Q7's body prose, the
register note and the P-71 row. It did not reach four live sites that a
reader acts on:

1. **The funnel summary's Acts line** (`:1819`) still reads "Acts: slices
   1-5 and 7 none (the 2026-09-05 continuation)". That is the exact
   formulation the repair widened at Gate 3 rows 4 and 5, left standing
   unquoted and undated in the one block shaped for lifting out of the
   packet. The packet's own discipline is that superseded wording is quoted
   and dated in place, never left live.
2. **The funnel summary's G5 line** (`:1817`) ends "slices 4-5 trace to
   recorded findings L6-F1/L6-F5, a reading Q7 now puts to the owner
   explicitly" — the pre-J2 statement of Q7's limb, with no RFC2-26 bar.
   The "Open questions" line (`:1820`) is the same: "Q7 widened to cover the
   M2/M3 file collisions and the slices 4-5 authorization reading".
3. **Q7's own bolded recommended answer** (`:108`) opens "**Slices 1–2 after
   M3 slice 5; slice 3 only after the three-way opening-band
   reconciliation …; slices 4–6 as sequenced; slice 7 waits on Q3**". Slice
   6 is elsewhere conditioned on Q5 and slice 7 on Q3, but slices 4 and 5
   carry no condition, although the same cell later establishes that neither
   RFC2-26 limb is available to them as designed.
4. **The sequencing order and the handoff.** The order's step after (3)
   (`:1480-1481`) reads "Then slice 4, then slice 5 — the home page is the
   composition of the two before it and should be built last", with no gate,
   while step (4) gates slice 6 on Q5 and step (5) gates slice 7 on Q3. The
   handoff's Q6 paragraph (`:1862-1864`) reads "slice 4 lands the descriptor
   and slice 5 composes the home page from it and from slice 3. Build them
   in that order" — an unconditional build instruction for the two slices
   the packet has just told the owner may be unschedulable.

This is the J1 defect repeated one review later and one layer out: a
blocking repair applied to the analysis and not to the text that carries the
analysis into action. An owner who reads the summary, or an implementer who
reads the order and the handoff, gets the answer review 4 withdrew.

**Also stale in the same block, separately:** `:1818` reads "independent
review (this is review 2, pending, after review 1's repair)". Four reviews
are retained and this is the fifth. The block's G1 and G4 lines *were*
carried forward (H1's fourth family at `:1813`, G2's three-way band at
`:1816`), which is what makes the untouched lines read as current rather
than as a frozen draft.

**Repair.** Carry J2 into the four sites: quote and date the Acts line's
superseded text and state the open RFC2-26 gate for slices 4 and 5; add the
gate to Q7's bolded recommendation, to the order's slice-4/5 step and to the
handoff's Q6 paragraph in the same shape slices 6 and 7 already use; update
G5 and the Open-questions line; and re-state the G6 Bar line to the true
review position.

---

### K2 — blocking — the RFC2-26 quotation stops unmarked halfway through the clause, and the test it introduces is run over two of the packet's eight slices with no stated denominator

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1155-1224`;
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md:196-221`.

**The clause's true line extent, stated as this review derived it.**
`DIRECTIVE-REGISTER.md:260` defines `RFC2-26` at
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`:196
(the candidate mirror at `:574` names the same line in the mirrored copy,
and the two files are byte-identical — `diff` reports no difference). Read
at source: the clause sits under the `###` heading "Authority boundary at
the OpenSpec seam (binding phase rule)" at line 194 and runs **196 through
221**, in two paragraphs — 196–210 and 212–221 — with the next `##` heading
("4. Violation cases") at line 223. Review 4's raw cited 196–206; the packet
corrected that to 196–210 and **196–210 is exact for the first paragraph**.
I compared the packet's blockquote at `:1170-1185` word for word against
source lines 196–210 after whitespace normalisation: **identical**. So the
quotation itself is faithful and the packet's line figure for what it quotes
is right.

**Defect.** The packet introduces the blockquote as "Quoted verbatim at the
defined clause, … lines 196–210 (verification rule 8)" and stops there. The
clause does not stop there. Lines 212–221 are the same clause — they say so
in their own words, "This clause binds the whole RFC 0002 package, not this
module alone" — and they are dropped with no ellipsis, no marker and no
mention, in a subsection whose entire purpose is to run this clause as a
test. This is precisely the class of defect H4 found twice and J3 found
again in this packet; it has now recurred in the passage the last blocking
finding created.

The unquoted half is not decorative. It carries the two sentences that fix
the test's *denominator*:

- "**Rows are per observable consequence, not per clause.** A clause with
  five observable consequences and one mapped requirement is not covered;
  the matrix discloses the consequences it enumerates for each clause, so a
  complete-looking matrix over under-enumerated consequences is a defect of
  the matrix."
- "This clause binds the whole RFC 0002 package, not this module alone."

**The consequence, which is the blocking half.** The packet runs RFC2-26
over slices 4 and 5 only, and states no denominator anywhere. Its own Gate 3
table has eight slice rows. Three of the other six sit squarely inside
RFC2-26's own enumerated consequence classes, quoted from the clause: slice
1 is "Unknown-reason … presentation"; slice 3 is a "gap surface"; slice 2 is
"API answers over epistemic state". The second unquoted sentence says the
clause reaches the whole RFC 0002 package, so RFC2-24 — the vocabulary slice
1 renders from, cited eighteen times in this packet — is inside its scope
too. For those three slices limb 1 is plausibly available and the packet
gestures at it ("Slices 1, 2, 3 and 6: no spec delta. Each is conformance
with text that already binds"), but it never runs the test: it names no
approved **scenario** for any of them, which is what limb 1 requires ("maps
to an approved OpenSpec requirement **and scenario**"), and the first
unquoted sentence says one mapped requirement does not cover a slice with
several observable consequences. Slice 3 is the sharpest case — its Gate 5
treatment is one sentence, "Slice 3 is PWB-REQ-010 and PWB-REQ-011
conformance and adds no claim", with no scenario named, for a slice the
clause's own list calls a gap surface.

This matters for the ruling in front of the owner. The packet asks the owner
to rule RFC2-26 for two slices while presenting three others as needing no
act at all (Gate 3 rows 1–3 read "**No**", unchanged). If the owner accepts
the packet's own framing — that this clause is in force and that silence is
a bar — they cannot tell from the packet whether the other three cleared it,
because the test was never run over them and the clause text that would have
forced the question was cut without a mark.

One further asymmetry worth the owner's eye: Gate 5's preserved caveat that
"the clause's scope is 'user-observable consequences **of this contract**',
which is itself a reading the owner may take narrowly" is offered as a route
out, while the clause's own scope sentence — the one at line 221 — is the
half not quoted.

**Repair.** Quote the clause to 221, or mark the elision naming exactly what
is elided and where, in the shape H4 already established in this packet.
Then state RFC2-26's denominator: run the test over all eight slice rows,
and for each of slices 1, 2, 3 and 6 name the approved requirement **and**
the approved scenario each observable consequence maps to, or say plainly
that the test was scoped to the two slices with no mapping requirement and
why that scoping is defensible. Neither repair requires changing a
recommended answer.

---

### K3 — non-blocking — Q6's preamble routes "whether either arm may be scheduled" to Q7, but nothing analyses the deletion arm

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:92-93`, against `:1187-1211`.

**Defect.** The reworded Q6 preamble closes: "So what the three sweeps
establish is that the arms are *unconstrained by any requirement*; whether
either may be *scheduled* is the RFC2-26 question Q7 now puts to the owner."
Q7's limb and Gate 5's "Which limb each slice relies on" cover slice 4 (the
derive arm) and slice 5. Neither covers Q6's other arm — deleting
`model.surfaces` — anywhere in the packet, so the preamble's "either"
promises an analysis that does not exist. The omission is understandable
(deletion is designed as no slice) but the sentence over-promises, and a
reader weighing deletion because the derive arm now carries an open gate
will look for its limb and find none.

**Repair.** Either say that only the derive arm is designed here and so only
it was tested, or add one sentence on deletion's limbs — plausibly limb 2 is
reachable for it in a way it is not for slice 4, which would be material to
the owner's choice and is currently unsaid.

---

### K4 — editorial — the review-4 disposition table enumerates what the packet "now carries" using line anchors from the reviewed commit, none of which resolve in the current bytes

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1775`, `:1776`, `:1777`,
`:1778`; evidence record `review2.disposition_summary.G6`.

**Defect.** J1's disposition reads "**Which acceptance text now carries the
fourth family, enumerated:** … Q1 at `:91`, Gate 3's slice-5 row, slice 1's
Tests at `:698-719`, Gate 5 at `:1009-1018`". Those anchors are the reviewed
commit `181797a`'s, not this file's: in the current bytes Q1 is line 102,
slice 1's Tests run 723–756, Gate 5's POC-REQ-060 passage runs 1036–1055.
Line 91 is mid-sentence in the Q6/Q7 preamble. J2 (`:1091-1093`, `:80-82`,
`:97`), J3 (`:749-758`), J4 (`:279-283`) and J9 (`:1436`, `:1504`) carry the
same convention, as does the record's G6 field ("the packet at :264 and
:402"). Where the sentence is a record of what the review read, the
reviewed-commit anchor is correct; where it is present-tense "now carries",
it sends a reader to unrelated prose. Nothing in the packet states the
convention.

**Repair.** One sentence above the review tables saying that `:NNN` anchors
in a review section are that review's commit, and re-anchoring or
de-anchoring the three present-tense enumerations in J1's disposition.

---

### K5 — editorial — Gate 5's `home` sweep publishes a closed partition that two of its six hits do not fit

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1124-1129`.

**Defect.** The sweep says "a case-insensitive whole-word search for `home`
returns **0** hits in the POC spec and **6** in the PWB spec, and all six are
the precedence table's `Home` column or the registry's 'governance home'
field". Re-run this session [predicate: `(?i)\bhome\b`; denominator: each
whole spec file]: 0 and 6, exactly as published. But enumerating the six,
two are neither of the two named categories — "every layer/home is unique"
in the precedence-table emission rule, and "one declaration must be under
the lowest-numbered expanded home with at least one admitted source" in the
coverage rule. Both are layer-home rule prose. The load-bearing conclusion
is untouched: none of the six is the `/` route.

**Repair.** "All six are the precedence table's `Home` column, the
layer-home rules that table governs, or the registry's governance-home
field — none is the `/` route", or enumerate the six.

---

### K6 — editorial — three spec quotations, two citation conventions, under one "quoted verbatim from lines X–Y" formula

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1010-1014`, `:1057-1066`,
`:1097-1099`.

**Defect.** POC-REQ-060 is introduced as "quoted verbatim from … lines
927–946"; source line 927 is the `### Requirement:` heading and 929 is
"Group: Cross-cutting experience. Form: **invariant**." — neither is in the
blockquote and neither is marked elided; the quoted text begins at 931.
PWB-REQ-020 is the same: cited 902–926, quoted from 906. PWB-REQ-004 is
cited 491–498 and is exact to the byte, because H4 corrected it to the
quoted text's own span. So the same formula names the requirement's span in
two cases and the quotation's span in the third. Everything inside each
blockquote is verbatim — I compared all three against source after
whitespace normalisation and all three are identical, and every bullet is
either present or marked (J3's restoration of the Case (sweep) bullet
verified at source lines 912–914).

**Repair.** Pick one convention and say which, or add "(the requirement runs
927–946; the normative text quoted here begins at 931)".

---

### K7 — editorial — two M3 short-head literals remain on one line, where one records the fact

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1649`.

**Defect.** Counted this session [predicate: literal occurrences of the
seven-character short head; denominator: the whole file]: **2 occurrences
over 1 line** in the packet, **1** in the evidence record, **0** in the
register — exactly as J9's disposition states, so J9 is repaired as written.
The remaining pair sits in the review-2 G7 row: "The `m3wt` worktree has
moved twice past `<head>` since this packet named it. `<head>` remains an
ancestor of that worktree's head". The first occurrence records what that
session read; the second is a present-tense claim about the sibling
worktree's current state, which is the kind of claim the packet's own rule
("cite it by register row P-70 and by the two files, never by head") exists
to prevent, and which will go stale on the sibling's next rebase.

**Repair.** Route the second to "that head remains an ancestor of the M3
worktree's head as review 2 found it", or drop it.

---

## Verification of J1–J9 against the current bytes

Every load-bearing figure below was re-derived by this review, not read from
the packet.

| # | Sev | Verdict | Evidence |
|---|---|---|---|
| J1 | blocking | **REPAIRED** | `provenance-none` swept over the packet: **29 occurrences over 19 lines** (102 ×8, 195, 206, 625, 734, 737, 748, 753, 1045, 1239, 1241, 1247, 1503, 1519, 1520, 1702 ×3, 1714, 1775 ×2, 1813). The three named sites all now carry the family: **Gate 1 Success 1** at `:188-198` gives four per-surface denominators including `provenance-none` — Polaris 0, Trajectory 0, Orrery 9 against 0 style occurrences, home 9 plus 1 style rule — with the two-literal parenthetical quoted and dated at `:199-207`; **S1b** at `:1239-1255` names the span, its source site, its own oracle ("the count of `provenance-none` occurrences not carrying the shared marker is zero", per surface, against that surface's own denominator) and its own re-emit mutant; **Gate 6 item 3** at `:1519-1522` carries the re-emit mutant in the rule-6 list. Censuses re-derived on the retained captures [predicate: literal occurrences of `provenance-none`; denominator: the whole served page; each occurrence then assigned to its enclosing tag]: Polaris tailnet **0**, Polaris direct **0**, Trajectory **0**, Orrery **9** rendered with **0** inside `<style>`, home **10** = 1 style rule + 9 rendered. The nine Orrery spans' enclosing `<tr>` ids are the nine objects Q1 is about, reproduced exactly. Source re-read: `exact-tables.ts:10` emits the span; `design-tokens.ts:25` declares `epistemic-unknown` and the file names `provenance-none` **0** times; its only style rule is `routes.ts:73` inside `HOME_STYLE`, declared at `:57` and used **once**, at `:90`; `orrery.ts` imports `exactTablesSection` at line 4 and calls it at 125 and 151 without it. Every value holds |
| J2 | blocking | **PARTIAL** | The subsection exists at `:1155-1224`, the clause is quoted word for word against source 196–210, RFC-0002's force re-checked at `PROJECT-STATUS.md:147` (Wave A, RFC 0001–0006, 19 modules, **ACCEPTED**, act performed 2026-08-17), the withdrawn sentence is quoted and dated at both sites (`:1138-1144` Gate 5, `:82-93` the Q6 preamble), Gate 3 rows 4 and 5 are widened with the superseded cell kept, each slice's limb is stated, neither slice is called unlawful (`:1213-1224`), and the P-71 row's Q7 text matches the packet clause by clause on this limb. **Short in two respects:** the clause is truncated at 210 with no mark though it runs to 221, and the test is run over two of eight slices with no denominator — K2. And the repair did not reach the summary, the order, Q7's bolded recommendation or the handoff — K1 |
| J3 | non-blocking | **REPAIRED** | PWB-REQ-020's blockquote now runs requirement text → **Case (sweep)** → Observable → one marked ellipsis (Oracle 916–917, Oracle independence 918–919, Mutation proof 920–923) → Falsifier. Compared against source lines 906–915 and 924–926: identical. The Mutation proof bullet quoted in full at `:803-806` under slice 2 matches source 920–923 word for word. The true elision count is one, as the introduction now says. (The cited range's first four lines are heading and Group/Form — K6, editorial) |
| J4 | non-blocking | **REPAIRED** | Re-derived on the lane A tailnet capture [predicate: for each of the 22 occurrences of `data-unknown-disclosure`, the distance back to the nearest preceding `<`; denominator 22]: **30** for the **6** opening `<p class="unknown-disclosure"`, **31** for the **5** `<li`, **32** for the **11** `<div`; 6+5+11 = 22, accounting for every element. Attribute offsets 378,631–1,462,622; element-open offsets 378,599–1,462,590; both endpoints are `<div>`s, so both read 32. The packet's partition at `:312-316` matches value for value, and the superseded universal is quoted and dated |
| J5 | non-blocking | **REPAIRED** | The P-71 row at `PENDING-OWNER-DECISIONS.md:286` reads "**at least four** encodings for one label", with the closed "four" quoted and dated as superseded and the reason stated (no sweep has enumerated POC-REQ-060's own population). Matches the packet's Q1 wording |
| J6 | editorial | **REPAIRED** | `review1.re_derived_before_applying.file_intersections` now opens with `note_2026_09_15` naming the fifth file and the corrected sibling field; the historical four-element array is kept unedited |
| J7 | editorial | **REPAIRED** | `review2.disposition_summary.G6` now says 89–102, with "88-102" quoted as superseded. Source confirms: line 88 is the third line of the preceding comment, line 89 opens `export const UNKNOWN_REASON_ROUTES`, the closing `};` is line 102 |
| J8 | editorial | **REPAIRED** | The register note is re-dated **2026-09-15** and recounted by the register's own stated method, which I re-ran independently [predicate: split on `## ` headings, then match at line start a table row whose first cell is `P-` followed by anything but a cell break]: acceptance-act section **5**, launch-scope reading aid **0**, open section **22** — and the 22 ids the note enumerates are exactly the 22 my sweep returns, P-25(c) included. **27** in all. Correct for this branch's copy |
| J9 | editorial | **REPAIRED** | 2 head occurrences over 1 line in the packet, 1 in the record, 0 in the register — exactly as the disposition states. The review-1 disposition mention is routed by register row P-70. (One of the two remaining is a live present-tense claim — K7, editorial) |

## Regression spot-check, F1–F22 / G1–G11 / H1–H9

The three findings review 4 marked PARTIAL are now complete:

- **H1 complete.** See J1 above: the fourth family reaches Success 1, S1b
  and Gate 6 item 3, each with the census re-derived here.
- **H4 complete.** Both blockquotes carry every bullet, present or marked;
  all three spec quotations verbatim at source; PWB-REQ-004's range 491–498
  confirmed (line 490 is blank).
- **H6 complete.** The partition is exact over the denominator it names.
- **G7 complete**, as review 4 recorded: the head no longer appears in the
  Collision section (0 occurrences outside the review-2 G7 row).

No regression found elsewhere. Re-derived independently this session:

- **F1.** RFC2-24's table (source lines 118–130) against
  `UNKNOWN_REASON_ROUTES` (`project-shape-model.ts:89-102`), key by key:
  **5 identical** — `stale-beyond-currency-bound`,
  `unconsented-source-or-provider`, `excluded-content`,
  `contradicted-pending-adjudication`, `reference-unresolvable` — and **7
  differ**, each exactly as the packet describes them. Slice 1's nine
  proposed routes are verbatim from the implementation table.
- **F2 / Q2.** `routesFor`'s guard at `project-shape-model.ts:151` is
  `if (state.label !== 'Unknown' || !('reasons' in state)) return [];` —
  two branches. `epistemic.ts:50-67` carries three union members, the third
  `{ label: UNKNOWN, basis: 'deferred' }` with no `reasons`.
  `polaris-copy.ts:192-193` are `label.deferred` and `label.no-route`, both
  in `UNREACHED_IN_FIXTURES` at `polaris-copy.test.ts:297,299`.
- **F5 / G3 / H2.** `epistemic-unknown` occurrences [same predicate, whole
  served page, then partitioned by enclosing tag]: Polaris **2** on both
  lane A forms (1 in `<style>`), Trajectory **301**, Orrery **11**, home
  **18** — so 0 / 299 / 9 rendered claim encodings on the three surfaces,
  exactly as published. No ranking across families survives anywhere.
- **Gate 1 censuses.** href sweep over the four captures: home 40 (36
  fragments + 4 nav), Trajectory 304 (300 + 4), Orrery 23 (19 + 4), Polaris
  1,089 (699 fragments + 386 exact-source routes + 4 nav). Polaris carries
  **359** `<details>`, **0** `<form>`, **1** `<button>`, **713**
  `data-claim-id="`, **18** `Route:`, **16** `data-unknown-reason="`, **1**
  `data-polaris-gaps`.
- **Disclosure table.** All 22 rows reproduce: **13 routed / 9 unrouted**
  under the packet's own element-inner predicate, and every offset and
  disclosure key in the table matches.
- **G10 / Q6.** `model.` per line of `routes.ts`: 35:1, 78:1, 87:1, **89:4**,
  92:2, 127:1, 133:1, 171:1, 172:1 = **13** over nine lines; `renderPocPage`
  spans 77–96, so five lines lie outside. Orrery's derived id lists at
  `model.ts:747-748`.
- **Q5 quotations.** `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` lines 70–72
  and the body section 44–52 both quoted accurately and in source order;
  escalation triggers at 86–94; mode direction 18–22 verbatim.
  `materialize-action.ts:33`, `materialization.ts:12` and `model.ts` lines
  570 / 588 / 597 / 701–702 all read as the packet states.
- **Q7 file sets.** Re-derived by intersecting both sibling packets' own
  Gate 3 "Lives in" columns: M4 ∩ M2 = **5** (`model.ts`, `routes.ts`,
  `polaris.ts`, `project-shape-model.ts`, `polaris-copy.ts`); M4 ∩ M3 = **2**
  (`polaris-copy.ts`, `polaris.ts`). Both hold.
- **F21 / H5 over-width.** Re-derived last, after reading every byte
  [predicate: lines outside fenced blocks whose first non-space character is
  not a pipe and whose length exceeds 78; denominator: 1,879 lines, the whole
  file]: **7** — line 1 (the H1, 126 characters) and six path-span lines at
  **10, 529, 604, 800, 1011, 1059**, which is the exact seven-line set the
  F21 disposition publishes. Every one but the H1 is a single unbreakable
  path code span.

## Q1–Q7

| Q | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | **Yes.** All four per-surface censuses re-derived here, value for value, and the cell is hedged at "at least four" with its reason. The acceptance text J1 was about now carries the family | Yes — a conformance ruling only the owner can make, both arms written out, the second arm's consequence carried into the handoff | Yes. The arm turns on the zero-denominator fact (0 disclosure elements on Trajectory and Orrery), which I reproduced, and the fourth family widens coverage without moving the arm | Yes — "at least four" restored, clause by clause identical including the marker-coverage caveat |
| Q2 | Yes. Both return-`[]` branches, the third `EpistemicState` arm, the two copy rows and their `UNREACHED_IN_FIXTURES` entries all verified at source | Yes — the mint-and-retire arm is named as available, not foreclosed | Yes. The narrowing to "Unknown carrying `reasons`" follows from the deferred arm being modelled | Yes |
| Q3 | Yes. The empty write surface and the act's own prohibition quoted accurately at their lines | Yes — three arms, (b) correctly identified as needing no act | Yes, and the handoff's "build the pure drafter anyway" is consistent with (b) | Yes |
| Q4 | Yes. One gap reason over 12 claims confirmed on the capture; `gapsList` at 933–948 | Yes — both arms lawful and stated as such | Yes, with the filter arm's cost and its missing negative case named | Yes |
| Q5 | Yes. The unconditional literals at 588 and 597, the conditional at 570, the seam comments and both readings' quotations all verified at source | Yes — the packet's most honest passage: two readings quoted, the recommendation labelled `[Inferred]`, the counter-argument left standing | Yes | Yes |
| Q6 | Yes on every figure (4 declared, 415 items, 713 tuples, the five fields, 13 over nine lines) | Yes — restated as an engineering choice put to the owner because no requirement reaches the field, with deletion's cost stated and deletion not denied | Yes on the arm. The preamble's routing of "either arm" to Q7 over-promises — K3 | Yes; the preamble rewording is disclosed in the register note |
| Q7 | Yes on the file sets, the three-way band, the intersections and the RFC2-26 limbs as far as they are run | Yes — sequencing, the collision set and the authorization arm each named as the owner's call | **Not fully.** The limb is now correct in Q7's body prose, but Q7's own bolded recommendation, the order and the handoff still schedule slices 4 and 5 unconditionally — K1 — and the clause behind the limb is quoted at half its extent and tested over a quarter of the slices — K2 | Yes on this limb, clause by clause; the register row and note both carry the RFC2-26 change and name it as a changed recommended answer |

**Disclosure of the Q7 change.** Carried in the packet's review-4 section
(`:1776`, `:1785-1799`), in the evidence record
(`review4.recommended_answers_changed.Q7`, which quotes the superseded
wording), in the register note (`:167-190`) and in the P-71 row's Q7 text
and sources cell. Q6's preamble rewording is disclosed in all four as well.
The one place it is **not** carried is the funnel summary, the order and the
handoff — K1.

**Register note counts.** 22 open / 5 acceptance / **27** in all, re-derived
by the register's own stated method this session, with the 22 row ids
matching the note's enumeration exactly. Correct for this branch's copy, and
now correctly dated.

**Sibling-packet references.** M2 by bead, register row P-69 and PR #36 and
by the five shared files; M3 by bead, register row P-70 and by the two
shared files; lane B by branch, PR #35 and register row P-68. Head literals:
two, both on one line, both inside the review-2 G7 disposition — one
historical and correct, one a live present-tense claim (K7).

**Owner trade-offs.** None smoothed into consensus. Q1's "accepted shape"
arm, Q2's mint-and-retire arm, Q3's three arms, Q4's filter arm, Q5's
Reading B, Q6's deletion arm and Q7's narrow-scope reading of RFC2-26 are
each written out with a consequence. **No lawful arm is called unlawful
anywhere in the current bytes**, and the RFC2-26 subsection says so
explicitly at `:1213-1224`.

**Epistemic labelling.** Substantive claims carry `[Observed]`, `[Inferred]`
or `[Unknown]`, including the four H9 sites and the four `unverified`
entries in the record. Every zero/all claim I checked carries a predicate
and a denominator and I was able to re-run each one.

## Counts

blocking 2, non-blocking 1, editorial 4 — seven findings, K1–K7.

Verdict: REVISE
