# R-POLARIS-M4-OWNER-LOOP-FUNNEL — review 6 (raw, retained verbatim)

Independent fresh-context review. Read-only: no repository file was edited,
no state-changing git command was run, no bead was written, no daemon was
started, no network was used, and the observed repository was never read.
The only file written is this one.

**Worktree and commit.** `agent/syzygy-dov.4` at
`1dd56391c13c965eeba79a7b233e533e57588a2b`, working tree clean at review
time (`git status --porcelain` empty).

**Files reviewed** — bytes by `wc -c`, digests by `sha256sum`, both computed
this session, never transcribed:

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` | 220411 | `ef4528a37399f15107e45ffa9589596250ce46ac382f500760a32e1a7cbc41fb` |
| `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json` | 71802 | `cbbdeca05ce1a01419522ceb9aa9b85a1f2218a5320e45aad542282795666e5e` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 44722 | `5a3131af1a79d4e8cc7fc3791056a11c2ac9b64ac8453f3fd8ea3b51466cc11a` |

**Retained prior raws, re-hashed this session** — five files under
`docs/reviews/`, and all five figures the packet publishes for them match
value for value: `R-POLARIS-M4-OWNER-LOOP-FUNNEL-RAW.md` 47636 /
`6983034196c706c213e2a939e0ca7dfe4c3f75f958378403fbd115112c2966ec`;
`…-2-RAW.md` 39050 /
`a7b3782882e41cf954e1dda326f502e20eceea4acd05732625de9f9ee2654649`;
`…-3-RAW.md` 31656 /
`ebce963f86f302940cc78f98dbe91325ae5c7b0ffa88e423b1fe05669035ccfe`;
`…-4-RAW.md` 37790 /
`5f3e9c458b9b2cc7d0372a7e22ef25e7cc0e72bd1fa1c3c003448acc7af17783`;
`…-5-RAW.md` 31406 /
`14f49e290bc55424690e9717830d9bbd5ea9bf4befa13659a7552199f8a6a43e`.
The review-5 reviewed-commit digests the packet publishes were recomputed
with `git show e134a12:<path> | sha256sum` and all three match, value for
value: 190003 / `403def26…62bad`, 60920 / `30b2b2cd…1fbe7`, 40852 /
`751d3edb…45f33` (full values verified; abbreviated only in this sentence,
and each is quoted in full in the packet itself).

**Captures re-hashed and re-censused this session** — all five match the
packet's provenance table, byte count and digest: lane A tailnet
1,484,487 / `e8a04b46…0111`, lane A direct 1,478,637 / `2fecdd01…a094`,
pre-lane-A home 38,706 / `c2fd6d1a…5fca`, Trajectory 244,524 /
`fd802531…6ddde`, Orrery 37,048 / `e3ae5b79…82afe`.

**Invariants.** `python3 scripts/check_governance.py` ends
`32 OK, 20 WARN, 0 FAIL (52 checks)`. Every path-shaped backticked span in
the packet resolves on disk [predicate: backticked spans containing `/` and
a known extension; denominator 48; unresolved 0]. No non-fence line in the
packet carries an odd backtick count, so no code span is broken across a
reflow. No manifest row or truncated signed act digest is quoted; no
observed-repository path is backticked (the only backticked spans matching
`butler` are Syzygy's own `openspec/changes/polaris-project-wide-butlers-model/`
paths and the adapter-registry declaration). Over-width, re-derived last
[predicate: lines outside fenced blocks whose first non-space character is
not a pipe and whose length exceeds 78; denominator 2,064 lines, the whole
file]: **7** — line 1 (the H1, 126 characters) and six single-path-span
lines at **10, 540, 615, 811, 1022, 1074** — exactly the seven lines and
the denominator the F21 disposition publishes.

---

## Findings

### L1 — blocking — the review-5 slice-3 gate never reaches the `## Recommended handoff` section, which now contradicts the funnel summary's own handoff line

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:2017-2022` and `:2024-2029`,
against `:2002`, `:1566-1571` and `:2042-2049`; the disclosure claims at
`:1958` and `:1288-1292` and
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:210-214`.

**Defect.** K2 changed a recommended answer: slice 3 now carries the same
open RFC2-26 gate as slices 4 and 5. The repair reached Q7's bolded
recommendation (`:119`), Gate 3's row 3 (`:663`), Gate 5's extended test
(`:1266-1299`), the funnel summary's G5, Acts, Open-questions and
Recommended-handoff lines (`:1997`, `:1999`, `:2000`, `:2002`), the
sequencing order (`:1566-1571`), the evidence record and the P-71 row. It
did not reach the prose `## Recommended handoff`, where the two paragraphs
that schedule slice 3 carry no gate:

1. `:2017-2022`, the Q7 paragraph: "the first of M2 slice 2, M3 slice 3 and
   M4 slice 3 to land builds the band container and its single ordering
   oracle" — a scheduling instruction under which M4 slice 3 may be the
   first to land, with no mention of the RFC2-26 ruling.
2. `:2024-2029`, the Q4 paragraph: "slice 3's band lists every reason
   present, ordered by the existing `foremost` array, and its total is
   asserted equal to the gaps section's on every fixture" — the slice's
   build instruction, ungated.

The adjacent Q6 paragraph at `:2042-2049` *was* repaired and now ends
"**Neither is built before Q7's RFC2-26 ruling**", with the superseded
wording quoted and dated. So within one section slices 4 and 5 carry the
gate and slice 3 does not, and the packet's two handoffs disagree with each
other: the funnel summary's line reads "the band and both of those slices
only after Q7's RFC2-26 ruling (added 2026-09-15, review 5, K1/K2)" while
the prose section says nothing.

Two live sentences assert the opposite. The K2 disposition at `:1958` says
the change "is disclosed in Q7, Gate 3, Gate 5, the funnel summary, the
recommended handoff, the evidence record, the register note and P-71 row";
`:1290-1292` repeats it; the register note at `:210-214` lists the eight
sites K1 repaired and names "the recommended handoff's Q6 paragraph" — the
only part of that section touched. The claim is true of the code block's
`Recommended handoff:` line and false of the section a reader reaches by
that name.

**Why the packet's own sweep could not catch it.** K1's re-derivation at
`:1957` swept six literal strings (`as sequenced`, `slices 1-5 and 7 none`,
`trace to recorded findings`, `2026-09-05 continuation`, `recorded-finding`,
`this is review 2`) and concluded "**no others**". I re-ran that exact
predicate over all three files this session [denominator: every line of the
packet (2,064), the record (1,083) and the register (321)] and the result
holds — every hit is either repaired-and-dated, a legitimate act mention
(`:126`), or a past pass's own record. But the predicate is a *pre-review-4*
one, and slice 3's gate is a *review-5* change; an omission carries no
literal, so no string sweep can reach it. The review-5 change needed its own
site sweep and did not get one.

**Repair.** Carry the gate into the Q7 and Q4 handoff paragraphs in the same
shape the Q6 paragraph already uses, with the superseded wording quoted and
dated; and either narrow the two disclosure sentences to name the funnel
summary's line rather than the section, or leave them once the section
carries it.

---

### L2 — non-blocking — Gate 5's lead sentence and its one-line slice-3 treatment still present slice 3 as covered conformance, unqualified, in the same gate that puts it under an open bar

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1018-1019` and `:1112-1113`,
against `:1281` and `:663`.

**Defect.** Gate 5 opens "**Slices 1, 2, 3 and 6: no spec delta. Each is
conformance with text that already binds.**" and treats slice 3 in one
sentence: "Slice 3 is PWB-REQ-010 and PWB-REQ-011 conformance and adds no
claim". Eighty lines later the same gate's RFC2-26 table finds slice 3's
own observable consequence maps to **no** approved requirement-and-scenario
pair, and Gate 3's row 3 states the distinction in the packet's own words:
"**preserving a requirement is not mapping to one**". "No spec delta"
remains true; "conformance with text that already binds" is the exact
inference the extended test withdraws for this slice, and it is the sentence
K2 already singled out ("its Gate 5 treatment is one sentence … with no
scenario named"). K2's repair added the test beside it and left it standing.

**Repair.** Qualify both sentences at the sentence, in the packet's own
shape — "no spec delta, and preserving PWB-REQ-010/011 is not mapping to
them; see the RFC2-26 test below" — rather than relying on a later
subsection of the same gate.

---

### L3 — non-blocking — Gate 4's slice headings for slices 3, 4 and 5 still read "no act", which Gate 3's rows for those same slices no longer do

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:820`, `:850`, `:866`, against
`:663`, `:664`, `:665`.

**Defect.** The three design headings read "### Slice 3 — The opening band
(medium; no act)", "### Slice 4 — `model.surfaces` true by construction
(medium; no act)" and "### Slice 5 — Home as the day-opening (medium; no
act)". Gate 3's rows for all three now read "**No act found for the
continuation itself; an RFC2-26 gate is open — see Q7**", and one of the
three routes the packet offers for clearing that gate is limb 2's "reviewed
N/A judgment … honored by an effective owner act" (`:1222-1227`, quoted
from the clause). So an act may well be needed for each. K1's literal
predicate does not contain the string "no act" and could not reach these.
The parenthetical is a size-and-act label, and Gate 3 is the table that owns
the act question and is correct, which is why this is not blocking.

**Repair.** "(medium; act — see Gate 3 and Q7)" for the three, or drop the
act half of the parenthetical and let Gate 3 own it.

---

### L4 — non-blocking — the RFC2-26 table's "None found" for slice 3 is an absence claim with no stated denominator, in the subsection whose whole repair was to state a denominator

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1281`;
`docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json`,
`review5.re_derived_before_applying.K2_all_slice_test.slice_3`.

**Defect.** K2's repair states the *slice* denominator (8, from Gate 3's
table, the ninth row excluded) and states it well. The slice-3 cell's
conclusion, though, is a claim of absence over a different population — the
approved requirements and scenarios of the two signed specs — and names only
the five requirements it checked. Rule 9 wants the denominator of that
population. The contrast is inside the same table: slices 4 and 5 rest on
"the three sweeps above", which do publish theirs (24 POC requirements, 17
PWB requirements, 0 and 6 `home` hits, 0 backticked `surfaces`).

**The conclusion holds — re-derived here, with the denominator the cell
omits.** [Predicate: `^### Requirement:` and `^#### Scenario:` at line start;
denominator: both signed spec files whole.] The POC spec carries **24**
requirements and **24** scenarios; the PWB spec **17** and **31** — **41**
requirements and **55** scenarios in all. I read every one of the 55 scenario
headings and then the bodies of every candidate: none states an aggregate of
Unknown-reason counts in the opening. The five the cell names are the right
candidates and its account of each is exact at source: PWB-REQ-010 (596) has
exactly **one** scenario, 615; PWB-REQ-011 (632) exactly **two**, 651 and
657; PWB-REQ-007 (439) exactly **one**, 470, and it is the per-claim case
while the requirement's aggregate sentence ("Aggregates SHALL disclose label,
tier, freshness and separate primary/secondary reason counts without a
headline status") carries no scenario of its own; POC-REQ-032 (574) exactly
**one**, 599, requiring the Unknown disclosed in place in the narrative flow;
PWB-REQ-012's scenario is at 705. So slice 3's limb 1 is genuinely
unavailable, and the recommended answer stands.

**Repair.** One bracket in the cell: the predicate, 41 requirements / 55
scenarios, and that every scenario heading was read.

---

### L5 — editorial — Gate 3's row 3 sends the reader to "the four requirements checked"; the cell it points at discusses five

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:663`, against `:1281` and the
record's `…K2_all_slice_test.slice_3`.

**Defect.** Row 3 closes "see Gate 5's RFC2-26 test for the four
requirements checked and why each falls short". Gate 5's slice-3 cell names
five — PWB-REQ-010, PWB-REQ-011, PWB-REQ-007, POC-REQ-032 and PWB-REQ-012 —
and the evidence record's own `slice_3` field enumerates the same five. Four
is defensible if PWB-REQ-012 is read as a constraint rather than a candidate
mapping (the cell says so: "a constraint the band must satisfy, never a
mapping"), but nothing at the cross-reference says which reading gives four.

**Repair.** "the five requirements read, four of them as candidate
mappings", or drop the count.

---

### L6 — editorial — the P-71 row's Q5 question drops the packet's first clause

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:317`, against
`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:117`.

**Defect.** The packet's Q5 asks three things: "is it authorized, is its
existing write into the observed repository's tracker authorized, and what
may it honestly be expected to produce?" The register row asks two: "what
may it honestly produce, and is its existing write into the observed tracker
authorized?" The dropped clause — whether the *run* is authorized, as
distinct from the write — is the one Reading A and Reading B actually differ
about, and it is present in the row's recommendation body ("Authorization is
contested and not resolved here … slice 6 is conditional on this ruling"),
so nothing is lost to a reader who reads the whole cell. The question line
alone understates the gate. Q1–Q4, Q6 and Q7 match the packet clause by
clause; Q7 matches including the widened limb, its "slices 3, 4 and 5" and
its dated supersessions.

**Repair.** Restore the clause to the row's Q5 question.

---

## Verification of K1–K7 against the current bytes

Every load-bearing figure below was re-derived by this review, not read from
the packet.

| # | Sev | Verdict | Evidence |
|---|---|---|---|
| K1 | blocking | **PARTIAL** | All eight named sites carry the gate with superseded wording quoted and dated: the funnel summary's Acts (`:1999`), G5 (`:1997`), Open-questions (`:2000`), G6 Bar (`:1998`, restated to "five raws are retained … this pass follows review 5 … pending a sixth" — 5 raw files confirmed on disk) and Recommended-handoff (`:2002`) lines; Q7's bolded recommendation (`:119`); the sequencing order's slice-4/5 step (`:1574-1580`, and step (3) at `:1569-1571` additionally gates slice 3); and the handoff's Q6 paragraph (`:2042-2049`). The six-literal sweep re-run here over all three whole files reproduces the packet's result exactly. **Short in one respect:** the review-5 change the repair was carrying never reached the prose `## Recommended handoff`'s Q7 and Q4 paragraphs, and two live sentences plus the register note say it did — L1 |
| K2 | blocking | **REPAIRED** | Clause extent re-derived independently: `DIRECTIVE-REGISTER.md:260` defines `RFC2-26` at `rendering-vocabularies.md`:196; read at source the `###` heading is 194, the clause runs **196–221** (196–210, blank 211, 212–221) and the next `##` heading is 223 — the packet's figures exactly. The blockquote at `:1212-1238` compared **word for word** against source 196–221 after whitespace normalisation: **identical**, both paragraphs, no elision. The introduction quotes and dates the superseded "196–210". The denominator is stated (8 Gate 3 slice rows, the ninth excluded) and the test is run over all eight. Every citation in the table resolves at source and covers what the cell says: slice 1 — POC-REQ-060 at POC spec 927 and scenario "Unknown looks the same everywhere" at 948, quoted verbatim against 950–951; PWB-REQ-007 at PWB spec 439, its "Unknown reasons SHALL use RFC2-24 values verbatim and expose their resolution routes" sentence exact, scenario at 470 quoted verbatim against 472–474. Slice 2 — POC-REQ-020 at 377, scenario at 400 quoted verbatim against 402–403; PWB-REQ-020 at 902, scenario at 928. Slice 3 — independently confirmed unavailable, see L4. Slice 3's Gate 3 row is widened with "**No**" quoted; Q7 is widened; the change is disclosed at Q7, Gate 3, Gate 5, the summary, the record and the P-71 row (the prose handoff excepted — L1) |
| K3 | non-blocking | **REPAIRED** | `:96-104`: the test is scoped to the derive arm ("Only the *derive* arm is designed as a slice here, so only it is tested at Gate 5") and the deletion arm's own limbs are stated and labelled `[Inferred]` — limb 2 plausibly reachable for deletion, still needing a reviewed N/A judgment homed in `.syzygy/governance/decisions/` and an effective owner act, "so deletion is not free of the clause either". The arm is not called unlawful |
| K4 | editorial | **REPAIRED** | The convention sentence stands at `:1650-1656`, above the review-1 section, and says a `:NNN` anchor inside a review section is a line number at that review's own reviewed commit. J1's three present-tense anchors (`:91`, `:698-719`, `:1009-1018`) are replaced by section and heading names with the superseded anchors quoted (`:1882`). The past-tense anchors in J2, J3, J4 and J9 and the record's `review2.disposition_summary.G6` are left as those passes wrote them, as the disposition says |
| K5 | editorial | **REPAIRED**, value for value | Re-run this session [predicate: `(?i)\bhome\b`; denominator: each whole spec file]: **0** in the POC spec, **6** in the PWB spec, at lines **247, 277, 510, 511, 518, 523** — exactly the six the packet enumerates. The restated three-way partition at `:1141-1148` assigns 247/277 to the registry's governance-home field, 510/518 to the precedence table's `Home` column and its semantic text, and 511/523 to the layer-home rules that table governs; I read all six and each falls where the packet puts it. The superseded two-way partition is quoted and dated; none of the six is the `/` route |
| K6 | editorial | **REPAIRED** | The convention is stated once and named at each of the three sites (`:1023-1027`, `:1080-1082`, `:1116-1120`). Verified at source: POC-REQ-060 heading 927, Group/Form 929, normative text begins **931**, falsifier ends 946; PWB-REQ-020 heading 902, Group/Form 904, text begins **906**, falsifier ends 926; PWB-REQ-004 heading 487, Group/Form 489, quoted text **491–498** exact. All three blockquotes compared against source after whitespace normalisation: **identical** in every segment (POC 931–940 and 945–946; PWB 906–915 and 924–926; PWB-004 491–498), and every elision marked and accurately described against source (POC Oracle 941–942, Oracle independence 943–944; PWB Oracle 916–917, Oracle independence 918–919, Mutation proof 920–923). The Mutation proof bullet quoted in full at `:812-817` matches source 920–923 word for word |
| K7 | editorial | **REPAIRED** | Re-counted this session [predicate: literal occurrences of the seven-character short M3 head; denominator: each whole file]: **1** in the packet (`:1756`, the review-2 G7 row), **1** in the evidence record, **0** in the register — exactly the figures the disposition publishes. The remaining occurrence is restated as what review 2 found, with the superseded present-tense sentence quoted and dated |

## Regression spot-check, F1–F22 / G1–G11 / H1–H9 / J1–J9

J2 was PARTIAL at review 5; it is now complete but for the site L1 names —
the clause is quoted whole, the denominator stated, the test run over all
eight slices, and Q7's bolded recommendation, the order and the handoff's Q6
paragraph all carry the gate. J1 and J3–J9 hold. Re-derived independently
this session:

- **Censuses, all five captures** [predicate: literal occurrences;
  denominator: the whole served page]. Polaris tailnet and direct:
  `data-unknown-disclosure` **22**, `epistemic-unknown` **2**,
  `provenance-none` **0**, `data-claim-id="` **713**,
  `data-unknown-reason="` **16**, `Route:` **18** — identical on both forms.
  Trajectory: 0 / **301** / 0. Orrery: 0 / **11** / **9**. Home: 0 / **18** /
  **10**. Every figure the packet, the record and the P-71 row publish.
- **J4 / H6 offsets.** For each of the 22 `data-unknown-disclosure`
  occurrences, the distance back to the nearest preceding `<` [denominator
  22]: **30** for **6**, **31** for **5**, **32** for **11**; 6+5+11 = 22.
  First attribute offset **378,631**, last **1,462,622**. The packet's
  partition matches value for value and the superseded universal is quoted.
- **Disclosure split.** Under the packet's own element-inner predicate
  (a disclosure counts as routed when its own element contains both
  `data-unknown-reason` and the literal `Route:`), by nesting-aware scan of
  each element: **13 routed / 9 unrouted** over 22.
- **Q2 / Q6 machine figures.** Recursive walk of `api-poc.json` collecting
  every object with a `resolutionRoutes` key: **1,149**, of which **1,137**
  are empty and all `Observed`, and **12** non-empty and all `Unknown` —
  so 0 of 1,137 empty-array claims are Unknown, as Q2 says. The decomposition
  the packet publishes sums: 439+415+278+6+9+1+1 = **1,149**.
- **Register recount**, by the register's own stated method [predicate:
  split on `## ` headings, then a line-start table row whose first cell is
  `P-` followed by anything but a cell break]: acceptance-act section **5**,
  launch-scope reading aid **0**, open section **22** — **27** in all, and
  the 22 ids are exactly those the note enumerates, P-25(c) included. The
  note's as-of date is **2026-09-15**.
- **F21 over-width**: 7, the published seven, at the published lines, over
  the published denominator 2,064 — see Invariants above.
- **Sibling-packet references.** M2 by bead `syzygy-dov.2`, register row
  P-69, PR #36 and the five shared files; M3 by bead `syzygy-dov.3`,
  register row P-70 and the two shared files; lane B by branch, PR #35 and
  register row P-68. Dated head mentions: **one**, historical, in the
  review-2 G7 disposition row.
- **Digests.** Every published byte count and sha256 in the packet — five
  captures, five retained raws, three review-5 reviewed files at `e134a12` —
  recomputed and matched.

## Q1–Q7

| Q | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | **Yes.** Every per-surface census re-derived here, value for value, on all five captures; the cell is hedged at "at least four" with its reason stated | Yes — a conformance ruling only the owner can make, both arms written out, the second arm's consequence carried into the handoff | Yes. The arm turns on the zero-denominator fact (0 disclosure elements on Trajectory and Orrery), reproduced here | Yes — "at least four", clause by clause, including the marker-coverage caveat |
| Q2 | Yes. 1,149 / 1,137 / 12 and the label histogram reproduced on the machine capture; the two return-`[]` branches and the third `EpistemicState` arm verified at source by prior passes and unchanged | Yes — the mint-and-retire arm is named as available, not foreclosed | Yes | Yes |
| Q3 | Yes. The empty write surface and the act's own prohibition quoted at their lines | Yes — three arms, (b) correctly identified as needing no act | Yes | Yes |
| Q4 | Yes. One gap reason over 12 claims; `data-polaris-gaps` occurs once on the capture | Yes — both arms lawful and stated as such | Yes, with the filter arm's missing negative case named | Yes |
| Q5 | Yes. Both readings quoted at their lines and neither resolved | Yes — the packet's most honest passage; the recommendation is labelled `[Inferred]` and Reading B is left standing | Yes | **Yes on substance, not on the question line** — the row's Q5 drops "is it authorized" for the run itself, which the body then supplies — L6 |
| Q6 | Yes on every figure (4 declared, 415 item claims, 713 tuples) | Yes — an engineering choice put to the owner because no requirement reaches the field, with deletion's cost stated and deletion not denied | Yes, and K3's deletion-arm limbs now close the "either arm" over-promise | Yes; the preamble rewording and the K3 addition are disclosed in the register note |
| Q7 | Yes on the file sets, the three-way band, the clause's full extent and the eight-slice test, each re-derived here | Yes — sequencing, the collision set, the authorization arm and the RFC2-26 ruling each named as the owner's call | **Not fully.** The limb is correct in Q7's cell, Gate 3, Gate 5, the order and the funnel summary, but the prose `## Recommended handoff` still schedules slice 3 with no gate while gating slices 4 and 5 two paragraphs later — L1 | Yes on the Q7 limb, clause by clause, including "slices 3, 4 and 5" and the dated supersessions |

**Disclosure of the Q7 change (slice 3).** Carried in Q7's cell (`:119`),
Gate 3's row 3 (`:663`), Gate 5's extended test (`:1288-1292`), the review-5
section (`:1958`, `:1965-1979`), the funnel summary's G5, Acts,
Open-questions and Recommended-handoff lines, the evidence record
(`review5.recommended_answers_changed.Q7`, which quotes the superseded
wording), the register note (`:194-223`) and the P-71 row's Q7 text. The one
place it is **not** carried is the prose `## Recommended handoff` — L1.

**Owner trade-offs.** None smoothed into consensus. Q1's "accepted shape"
arm, Q2's mint-and-retire arm, Q3's three arms, Q4's filter arm, Q5's
Reading B, Q6's deletion arm (now with its own limbs) and Q7's narrow-scope
reading of RFC2-26 are each written out with a consequence. **No lawful arm
is called unlawful anywhere in the current bytes**: `:1293` ("This packet
still calls no slice unlawful") and `:1301-1312` say so explicitly, and the
narrow-scope reading is preserved as an arm beside the clause's own scope
sentence at line 221, now quoted.

**Epistemic labelling.** Substantive claims carry `[Observed]`, `[Inferred]`
or `[Unknown]`, including slice 8's `[Unknown]` in the RFC2-26 table and
both readings the table rests on. Every zero/all claim I tested carries a
predicate and a denominator I could re-run, with the one exception at L4.

## Counts

blocking 1, non-blocking 3, editorial 2 — six findings, L1–L6.

Verdict: REVISE
