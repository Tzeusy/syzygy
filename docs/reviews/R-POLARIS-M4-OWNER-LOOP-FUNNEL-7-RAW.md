# R-POLARIS-M4-OWNER-LOOP-FUNNEL — review 7 (raw, retained verbatim)

Independent fresh-context review. Read-only: no repository file was edited,
no state-changing git command was run, no bead was written, no daemon was
started, no network was used, and the observed repository was never read.
The only file written is this one.

**Worktree and commit.** `agent/syzygy-dov.4` at
`4b431fbf8994c4cb66d0eeeb94c724757408ed52`, working tree clean at review
time (`git status --porcelain` empty).

**Files reviewed** — bytes by `wc -c`, digests by `sha256sum`, both computed
this session, never transcribed:

| File | Bytes | sha256 |
|---|---|---|
| `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md` | 236948 | `dae20e6538d5cbf692165f91ffb348f976ef92eb60d405924310b4ad049bc30e` |
| `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json` | 80636 | `4844e9a10d33425d00b6dc3a3269f42ee60a89a5124e6c152409f569ebee7011` |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 47510 | `c272f73b6f4ebfcfe21b799ab5f904d02bba94a9580f824e762a59ffd68942af` |

**Retained prior raws, re-hashed this session** — six files under
`docs/reviews/`, and the figures the packet publishes for the sixth match:
`…-6-RAW.md` **26182** /
`4d2035caa450bf5cdcfb220c2b0d3891459a3a05edc28c467eb01c75982f6abd`, the
values in the review-6 section and in the record's `review6` block. Byte
counts for the other five: 47636, 39050, 31656, 37790, 31406 — the figures
the earlier sections publish. **The review-6 reviewed-commit digests were
recomputed with `git show 1dd5639:<path> | sha256sum` and all three match,
value for value**: 220411 / `ef4528a3…c41fb`, 71802 / `cbbdeca0…66e5e`,
44722 / `5a3131af…cc11a` (verified in full; abbreviated only in this
sentence, and each is quoted in full in the packet itself).

**Captures re-hashed and re-censused this session** — lane A tailnet
1,484,487 / `e8a04b46…0111`; lane A direct 1,478,637 / `2fecdd01…a094`;
pre-lane-A home 38,706 / `c2fd6d1a…5fca`; Orrery 37,048 / `e3ae5b79…82afe`.

**Invariants.** `python3 scripts/check_governance.py` ends
`32 OK, 20 WARN, 0 FAIL (52 checks)`. Every path-shaped backticked span in
the packet resolves on disk [predicate: backticked spans containing `/` and
ending in one of .md .ts .py .json .yaml .yml .html .txt; denominator 44;
unresolved **0**]. No non-fence line in the packet carries an odd backtick
count [denominator: every line of the file], so no code span is broken
across a reflow. No manifest row and no truncated signed act digest is
quoted; no observed-repository path is backticked — the only backticked
spans matching `butler` are Syzygy's own
`openspec/changes/polaris-project-wide-butlers-model/` paths and the
adapter-registry declaration JSON. Over-width, re-derived last [predicate:
lines outside fenced blocks whose first non-space character is not a pipe
and whose length exceeds 78; denominator 2,197 lines, the whole file]:
**8**, at lines **1, 10, 540, 615, 811, 855, 1042, 1094** — exactly the
eight the F21 disposition now publishes, including the new eighth, the
Gate 4 slice-4 heading at 85 characters.

---

## Findings

### M1 — editorial — the L3 disposition's `](#` zero-claim is falsified by the sentence that states it

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:2065`.

**Defect.** The L3 row publishes an absence with its predicate and
denominator: "[predicate: the literal `](#`; denominator: the whole packet
and the whole register]: **0** occurrences in either file". Re-run this
session over both whole files at HEAD [same predicate, `grep -F`]: **1** in
the packet and **0** in the register. The single hit is line 2065 itself —
the code span in which the predicate is written. At `1dd5639` the figure is
genuinely **0** in both files (`git show 1dd5639:<path> | grep -c -F`), and
the cell is marked "**Checked before editing**", so the claim is honest
about when it was taken. It is nonetheless a published figure a reader who
re-runs the stated predicate cannot reproduce, and the one hit they get is
the claim's own bytes — the packet's own habit everywhere else is to say so
(F21 re-derives "last in that pass and after every other edit in it").

**Repair.** One clause: "(re-running the predicate at this commit matches
once, in this cell's own code span)".

---

### M2 — non-blocking — the slice-3 "None found" cell enumerates five candidates and omits PWB-REQ-002, the one approved scenario in either spec that requires rendered Unknown counts in aggregate

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1307`, against the PWB spec's
`### Requirement: PWB-REQ-002` at line 115 and its scenario "Declared shape
reconciles" at 142.

**Defect.** L4's repair states the population denominator well, and I
re-derived it: **41** approved requirements and **55** scenarios [predicate
`^### Requirement:` / `^#### Scenario:` at line start; denominator both
signed spec files whole — POC **24**/**24**, PWB **17**/**31**]. Running
that predicate myself and reading all 55 scenario headings, the nearest
candidate the cell does not name is PWB-REQ-002, whose scenario at 142
reads "**THEN** Polaris accounts for all D items exactly once / **AND**
every category reports modeled, Unknown and contradicted counts that sum to
its denominator", and whose Observable is "per-category identities and
reconciling counts are visible in the machine answer and reachable from
Polaris". That is an approved requirement-and-scenario pair requiring
*rendered aggregate Unknown counts* — the class slice 3's band sits in.

**The conclusion still holds, re-derived here.** PWB-REQ-002 partitions by
extraction *category* into the three coverage states; slice 3's band
partitions by RFC2-24 *reason* (`gapReasonCounts`, Gate 4 at `:828`), which
is a different projection of a different population, and PWB-REQ-002's
observable is satisfied today by the existing gaps section — "reachable
from Polaris", not an opening band. So limb 1 remains unavailable and the
recommended answer is unchanged. But the cell closes "The five requirements
named above are the candidates", and a reader running L4's own predicate
reaches PWB-REQ-002 and has to construct that distinction unaided — the
same defect L4 corrected one level up.

**Repair.** One sentence in the cell naming PWB-REQ-002 as the sixth
candidate read and why it does not map: category-and-coverage-state, not
reason; already satisfied by the gaps section; no opening-position claim.

---

### M3 — editorial — the Q7 cell restates the reconciliation rule ungated at the sentence, the shape L1 repaired in the Collision section and the prose handoff

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:119`, against `:1575-1578` and
`:2143-2150`.

**Defect.** Inside the Q7 cell the revised reconciliation reads "So
whichever of M2 slice 2, M3 slice 3 and M4 slice 3 lands first **builds the
band container and owns its single ordering oracle** … Reconcile explicitly
before any of the three starts" — word for word the sentence L1 found
ungated in the Collision section and in the prose handoff's Q7 paragraph,
and which this pass gated at both of those sites ("**None of that schedules
M4 slice 3: it is not built before Q7's RFC2-26 ruling either**", `:1575`;
"**M4 slice 3 is not built before both that reconciliation and Q7's RFC2-26
ruling**", `:2143`). The Q7 cell's own copy took no such clause.

**Why this is editorial and not a repeat of L1.** The cell *opens* with the
gate — its bolded recommendation is "slice 3 only after the three-way
opening-band reconciliation … *and* the RFC2-26 ruling this question asks
for" — and *closes* with the K2 widening paragraph that puts slice 3 under
the gate and says so twice. A reader cannot act on the middle sentence
without having read the recommendation two screens above it in the same
cell. L1's site had no gate anywhere in the section.

**Repair.** The same four words the other two sites took, or nothing, on
the ground that the cell brackets the sentence with the gate.

---

### M4 — editorial — the packet's rule-10 paragraphs are never re-tensed, while the register's parallel paragraphs are

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1812`, `:1869`, `:1946`,
`:2019`, against
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:161`, `:191`,
`:221`.

**Defect.** Each review section closes with a rule-10 paragraph asserting a
present coverage state: "the repaired bytes are **uncovered until a sixth
review confirms them**" (`:2019`), and the same at `:1812`, `:1869`,
`:1946` for the third, fourth and fifth. All four are discharged — review 6
is retained and verified the review-5 repairs 6 REPAIRED / 1 PARTIAL over 7.
The register treats the identical claim differently: its paragraphs read
"**uncovered until a fifth review confirms them** — which has since
happened; see the next paragraph (re-tensed 2026-09-15 per review 5)"
(`:191`), and likewise at `:161` and `:221`. So the same sentence is dated
in one artifact and live in the other. The anchor convention at `:1686-1692`
covers `:NNN` anchors, and its one tense rule points the other way: "Where
a disposition speaks in the present tense about what the packet *now*
carries, it names the section or heading instead."

This is what AGENTS.md's own lesson calls marking staleness at the stale
sentence; the adjacent `## Review N+1` heading supersedes it in practice,
which is why this is editorial and not more.

**Repair.** Either the register's clause on each of the four, or one line
in the anchor-convention paragraph extending it to the rule-10 tense.

---

### M5 — editorial — "and in the pull request" names a disclosure site outside the reviewed bytes, unlabelled

`docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md:1319`, and the same phrase in
the K2 disposition at `:1994`.

**Defect.** Gate 5's "What the extended test changes" paragraph lists where
the slice-3 gate is disclosed and ends "in the register note and P-71 row,
and in the pull request". Every other item in that list is a named site in
one of the three artifacts and checkable from the bytes; the last is a
present-tense claim about an artifact outside them, carrying no `[Observed]`
label, no date and no identifier. A read-only reviewer cannot verify it —
this pass could not — and a pull-request body is editable after the fact.

**Repair.** Drop the clause, or give it the PR number and a date the way the
sibling references are given (`syzygy-dov.2`, P-69, PR #36).

---

## Verification of L1–L6 against the current bytes

Every load-bearing figure below was re-derived by this review, not read from
the packet.

| # | Sev | Verdict | Evidence |
|---|---|---|---|
| L1 | blocking | **REPAIRED** | All three ungated scheduling sites now carry the gate, in the Q6 paragraph's shape, with the added wording dated and the superseded paragraph ends described: the prose handoff's Q7 paragraph (`:2143-2150`, "**M4 slice 3 is not built before both that reconciliation and Q7's RFC2-26 ruling**" + "**Added 2026-09-15 (review 6, L1)**"), its Q4 paragraph (`:2152-2162`, "**Either way the slice is not built before Q7's RFC2-26 ruling**" + the same dated note), and the Collision section's revised reconciliation rule (`:1575-1578`), which L1 did not name and the packet's own sweep found. The Q6 paragraph (`:2175-2182`) is unchanged. **Both disclosure sentences are narrowed and dated**: the K2 row (`:1994`) now names "the funnel summary's G5, Acts, Open-questions and Recommended-handoff lines, the prose handoff's Q6 paragraph" and quotes the superseded "the funnel summary, the recommended handoff"; Gate 5's paragraph (`:1315-1321`) names the four summary lines, the prose handoff's Q7, Q4 **and** Q6 paragraphs and the Collision section, quoting the superseded "in the recommended handoff". **The register note's site list was correctly NOT narrowed** — `:210-214` names "the recommended handoff's Q6 paragraph", which is exactly the part review 5 touched; I read it and it is true of the bytes. **The sweep re-run.** [Predicate as published: `(?i)slice 3\b` or the literal `M4 slice 3`.] At `1dd5639` I reproduce the packet's figures exactly: denominator 2,064 + 1,083 + 321 = **3,468**, **60** hits (51 / 6 / 3). At HEAD the denominator is 2,197 + 1,190 + 343 = **3,730** — **262 lines more**, the review-6 section, the L2/L3/L4/L5 repairs, the record's `review6` block and the register's sixth paragraph — and **79** hits (64 / 11 / 4), **19** more, every one of them in text this pass added. Classifying all 79 myself: **8 distinct live scheduling sites**, all gated — Q7's bolded recommendation (`:119`), the order's step (3) (`:1602-1607`), the Collision rule (`:1565-1578`), the funnel summary's Recommended-handoff line (`:2123`), the prose handoff's Q7 (`:2139-2150`), Q4 (`:2152-2162`) and Q6 (`:2175-2182`) paragraphs, and the P-71 row's Q7 recommendation (register `:339`, "**and** the RFC2-26 ruling below"). The packet counts seven, excluding the Q6 paragraph because it schedules slices 4 and 5 rather than slice 3; on either count **no live scheduling site is left ungated**. The remainder are historical (superseded text quoted and dated, or a review section's record) or descriptive. One sentence inside site 1 restates the rule ungated — M3, editorial |
| L2 | non-blocking | **REPAIRED** | Both sentences qualified at the sentence, not deferred to a later subsection. The gate's lead (`:1033-1039`) now reads "no spec delta. Each is conformance with text that already binds — except that for slice 3 no spec delta is not the same as a mapping: preserving PWB-REQ-010 and PWB-REQ-011 is not mapping to them … see the RFC2-26 test below", with "**Qualified 2026-09-15 (review 6, L2)**" naming the superseded ending. The one-line treatment (`:1132-1139`) now carries "**preserving a requirement is not mapping to one**" and the open gate, with the superseded sentence quoted whole. The literal "conformance with text that already binds" survives nowhere else as an unqualified claim [1 further occurrence in the file, the L2 finding row at `:2064`] |
| L3 | non-blocking | **REPAIRED** | The three Gate 4 headings read "### Slice 3 — The opening band (medium; act — see Gate 3 and Q7)" (`:820`), "### Slice 4 — `model.surfaces` true by construction (medium; act — see Gate 3 and Q7)" (`:855`) and "### Slice 5 — Home as the day-opening (medium; act — see Gate 3 and Q7)" (`:876`), each with a dated italic note beneath quoting the superseded "(medium; no act)". Slices 1 and 2 correctly keep "(medium; no act)" — their Gate 3 cells read "**No**" and both map to named requirement-and-scenario pairs. The new over-78 line is disclosed and enumerated (see Invariants; F21 now publishes 8 over denominator 2,197, and my sweep returns the same eight lines). The anchor check is true at the commit it was taken and self-falsified at HEAD — M1 |
| L4 | non-blocking | **REPAIRED**, and the figures re-derived value for value | The cell (`:1307`) carries "[Absence predicate and denominator, added 2026-09-15, review 6, L4: `^### Requirement:` and `^#### Scenario:` at line start; denominator both signed spec files whole — **41** approved requirements and **55** scenarios (POC spec 24 and 24, PWB spec 17 and 31)…]". Re-run here: POC **24**/**24**, PWB **17**/**31** — **41**/**55**. Every one of the five candidates is exact at source, checked line by line this session: PWB-REQ-010 heading 596, its **one** scenario 615; PWB-REQ-011 632, **two** at 651 and 657; PWB-REQ-007 439, **one** at 470; POC-REQ-032 574, **one** at 599; PWB-REQ-012 679, **one** at 705. I read all 55 scenario headings and the bodies of every candidate and reach the same conclusion. One candidate is unnamed — M2 |
| L5 | editorial | **REPAIRED** | Gate 3's row 3 (`:663`) reads "see Gate 5's RFC2-26 test for the five requirements read, four of them as candidate mappings, and why each falls short", with "(corrected 2026-09-15, review 6, L5, which superseded 'the four requirements checked': …)" naming the five and identifying PWB-REQ-012 as the constraint. The count now agrees with the cell and with the record's `slice_3` field. The literal "four requirements" survives only in the L5 finding row |
| L6 | editorial | **REPAIRED** | The P-71 row's Q5 question (register `:339`) reads "Run the return path once (slice 6): is it authorized, is its existing write into the observed tracker authorized, and what may it honestly be expected to produce?", with "(first clause restored 2026-09-15 after review 6, L6, which superseded 'what may it honestly produce, and is its existing write into the observed tracker authorized?')" and the reason. Compared clause by clause with the packet's Q5 at `:117`: three clauses, same order, same sense; the register drops only the word "repository's" from "the observed repository's tracker", which it cannot backtick and which changes no clause |

## Regression spot-check, F1–F22 / G1–G11 / H1–H9 / J1–J9 / K1–K7

**K1, PARTIAL at review 6, is now complete**: the only respect in which it
fell short was L1's three sites and two sentences, and all five are
repaired above. K2–K7 hold on current bytes; J1–J9, H1–H9, G1–G11 and
F1–F22 show no regression. Re-derived independently this session:

- **RFC2-26, quoted whole (K2).** `DIRECTIVE-REGISTER.md:260` defines the
  clause at `rendering-vocabularies.md`:196; read at source, the `###`
  heading is 194, the clause runs **196–221**, and the next `##` heading is
  223 — the packet's figures. The blockquote at `:1238-1263` compared word
  for word against source 196–221 after whitespace normalisation:
  **identical**, both paragraphs, **no elision, marked or unmarked**.
- **Censuses, four captures re-hashed and re-counted** [predicate: literal
  occurrences; denominator: the whole served page]. Polaris tailnet and
  direct, identical on both forms: `data-unknown-disclosure` **22**,
  `epistemic-unknown` **2**, `provenance-none` **0**, `data-claim-id="`
  **713**, `data-unknown-reason="` **16**, `Route:` **18**. Orrery: 0 /
  **11** / **9**. Home: 0 / **18** / **10**. Every figure the packet, the
  record and the P-71 row publish.
- **Disclosure split (F-series, Q1).** By nesting-aware scan of each
  element under the packet's own predicate (own element contains both
  `data-unknown-reason` and the literal `Route:`): **13 routed / 9
  unrouted** over 22.
- **J4 / H6 offsets.** For each of the 22 `data-unknown-disclosure`
  occurrences, the distance back to the nearest preceding `<` [denominator
  22]: **30** for **6**, **31** for **5**, **32** for **11**; 6+5+11 = 22.
  First attribute offset **378,631**, last **1,462,622**. The packet's
  partition matches value for value.
- **Q2 / Q6 machine figures.** Recursive walk of `api-poc.json` collecting
  every object with a `resolutionRoutes` key: **1,149**, of which **1,137**
  are empty and every one carries `epistemic.label` `Observed`, and **12**
  non-empty and every one `Unknown` — so 0 of 1,137 empty-array claims are
  Unknown, as Q2 says.
- **Gate 3's denominator (K2).** The "authorizing act, per slice" table has
  nine rows, eight of them slices and the ninth ("A poller, watcher or
  scheduler, had one been proposed") proposing none — denominator **8**,
  counted here.
- **Evidence record.** `review5` is **byte-identical** to its state at
  `1dd5639` (block extracted from both and compared), and so is every other
  top-level block; `review6` is the only addition, and its twelve keys
  mirror `review5`'s twelve exactly, name for name and in the same order,
  with `j1_j9_…` replaced by `k1_k7_verification_as_review6_states_it`. Its
  `raw`, `bytes`, `sha256`, `reviewed_commit` and
  `reviewed_files_at_that_commit` match the files on disk and `1dd5639`.
- **The funnel summary's review line.** `docs/reviews/` holds **six**
  `…M4…-RAW.md` files; G6 reads "six raws are retained … this pass follows
  review 6, verdict copied exactly REVISE, and is itself pending a seventh",
  with the superseded five-raw wording quoted and dated.
- **The register note's ordinal paragraphs.** Six, one per review, in order;
  the sixth records REVISE, 1/3/2, L1–L6, "**6 REPAIRED and 1 PARTIAL over
  7** — K1 partial", "**No recommended answer changed after review 6**",
  and each of L1–L6's repair. The fifth is re-tensed per review 6. The
  P-71 row's review-6 entry carries the same verdict word, counts and
  finding list and closes "**uncovered until a seventh review confirms
  them**".
- **Sibling-packet references.** M2 by bead `syzygy-dov.2`, register row
  P-69 and PR #36; M3 by `syzygy-dov.3` and row P-70; lane B by
  `syzygy-dov.17`, PR #35 and row P-68 (4, 8 and 5 mentions of the three
  rows). Dated head mentions of a sibling: **one**, `b34fca7` at `:1792`,
  historical, in the review-2 G7 disposition. Every other short head in the
  file is M4's own reviewed commit or the baseline.
- **Digests.** Every published byte count and sha256 I could recompute —
  four captures, the six retained raws, the three review-6 reviewed files
  at `1dd5639` — recomputed and matched.

## Q1–Q7

| Q | Scope truthful? | Genuine gate? | Recommendation follows? | Register matches packet? |
|---|---|---|---|---|
| Q1 | **Yes.** Per-surface censuses re-derived here value for value on the captures available to this pass; the cell is hedged at "at least four" with its reason stated | Yes — a conformance ruling only the owner can make, both arms written out, the second arm's consequence carried into the handoff | Yes. The arm turns on the zero-denominator fact (0 disclosure elements off Polaris), reproduced here | Yes — "at least four", clause by clause, including the open-population caveat |
| Q2 | Yes. 1,149 / 1,137 / 12 reproduced on the machine capture, with the label split checked at `epistemic.label` | Yes — the mint-and-retire arm is named as available, not foreclosed | Yes | Yes |
| Q3 | Yes. The empty write surface and the act's own prohibition quoted at their lines | Yes — three arms, (b) correctly identified as needing no act | Yes | Yes |
| Q4 | Yes. One gap reason over 12 claims | Yes — both arms lawful and stated as such | Yes, with the filter arm's missing negative case named, and the slice now gated in the handoff | Yes |
| Q5 | Yes. Both readings quoted at their lines and neither resolved | Yes — the recommendation is labelled `[Inferred]` and Reading B is left standing | Yes | **Yes, now on the question line too** — L6 repaired; three clauses, same order |
| Q6 | Yes on every figure (4 declared, 415 item claims, 713 tuples) | Yes — an engineering choice put to the owner, deletion's cost stated and deletion not denied | Yes; K3's deletion-arm limbs still stand | Yes |
| Q7 | Yes on the file sets, the three-way band, the clause's full extent and the eight-slice test, each re-derived here | Yes — sequencing, the collision set, the authorization arm and the RFC2-26 ruling each named as the owner's call | **Yes.** The slice-3 limb now reaches every live scheduling site: Q7's recommendation, Gate 3's row 3, Gate 4's heading, Gate 5's lead, one-line treatment and table, the order's step (3), the Collision rule, the funnel summary's four lines, the prose handoff's Q7, Q4 and Q6 paragraphs, and the P-71 row | Yes on the Q7 limb, clause by clause, including "slices 3, 4 and 5" and the dated supersessions |

**Owner trade-offs.** None smoothed into consensus. Q1's "accepted shape"
arm, Q2's mint-and-retire arm, Q3's three arms, Q4's filter arm, Q5's
Reading B, Q6's deletion arm and Q7's narrow-scope reading of RFC2-26 are
each written out with a consequence. **No lawful arm is called unlawful in
the current bytes**: `:1324` ("This packet still calls no slice unlawful")
and `:1332-1343` say so explicitly, and the narrow-scope reading is
preserved beside the clause's own scope sentence at line 221, quoted. L2's
qualification narrows a claim *against* the packet's own preferred reading,
which is the honest direction.

**Epistemic labelling.** Substantive claims carry `[Observed]`, `[Inferred]`
or `[Unknown]`, including slice 8's `[Unknown]` in the RFC2-26 table and
both readings the slice-1 and slice-2 mappings rest on. Every zero/all claim
I tested carries a predicate and a denominator I could re-run, with the two
exceptions at M1 (true at its stated commit, self-falsified at HEAD) and M5
(a site outside the reviewed bytes).

**Rule 10.** This review binds the three digests named in the header, at
`4b431fb`, and nothing later. Any edit made in response to it is uncovered
until an eighth review confirms it; that raw must be an eighth `-RAW.md`
file, never an overwrite of any retained one.

## Counts

blocking 0, non-blocking 1, editorial 4 — five findings, M1–M5.

Verdict: CONFIRM WITH EXCEPTIONS
