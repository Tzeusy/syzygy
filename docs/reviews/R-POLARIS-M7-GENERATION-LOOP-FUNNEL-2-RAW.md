# R-POLARIS-M7-GENERATION-LOOP-FUNNEL — review 2 (raw, retained verbatim)

Reviewer: independent fresh-context session, 2026-09-15. Read-only; no
tracked file edited, no state-changing git command, no daemon, no network,
no provider call. Review 1 is retained at
`docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-RAW.md` and was read in
full before this pass.

Worktree: scratchpad `m7wt`, branch agent/syzygy-dov.7, HEAD
`1803608` ("docs: M7 funnel review 1 retained, F1-F12 dispositioned, P-76
registered [syzygy-dov.7]"). Baseline the packet measures at: `a9f671e`.
`git status --short` was empty before this session's work and empty after
it; the only files written are this raw and scratch files under the
session's own scratch directory.

## Bytes reviewed (computed with `wc -c` and `sha256sum`, never transcribed)

| File | Bytes | sha256 |
|---|---:|---|
| `docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md` | 139264 | c45d12c01be340321fbe6286e316cbf1eee4fb9c0129f0b32851dad5008c33bc |
| `docs/evidence/polaris-m7-generation-loop-funnel-2026-09-15.json` | 46936 | 668b14a5cd00cceb694fec35f11c3a643c8a5bec4dd5bc306058401d22754e5d |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 34761 | 4ba0e3624d8c68bb5b7200dd6166a48ebeddc743b9b98bdb672b8115ceced5eb |
| `docs/reviews/R-POLARIS-M7-GENERATION-LOOP-FUNNEL-RAW.md` | 33233 | 93aabafeaf50933c8ff03cfe448bbd5b13a7f289bad872d75a819485f8e85943 |

The retained raw's digest equals the one the packet publishes at its
"Review 1 and repairs" head [Observed, recomputed this session], so review
1's own bytes are unaltered.

`git diff --name-status a9f671e HEAD` returns four rows: `M` on the
register, `A` on the packet, the evidence record and the retained raw
[Observed, run this session].

Commands run in the worktree: `npm run build:poc` (exit 0), `npm test`
(**123 test files passed, 3 skipped; 1686 tests passed, 3 skipped**),
`npm run poc:generator-demo -- --out <scratch>` (exit 0; three synthetic
previews written under the scratch directory, never into the worktree),
`python3 scripts/check_governance.py` — tail line read in full: "32 OK, 20
WARN, 0 FAIL (52 checks) — counts derived, not asserted".

Rule 1 observed throughout: every load-bearing sweep below was run with
Python `re` or exact substring counting, never a bracket class.

---

## (a) Review-1 exception repairs, verified against the current bytes

| # | Verdict | Evidence |
|---|---|---|
| F1 | **REPAIRED** | `git ls-files` this session: `packages/polaris-generation-core/src` + `apps/three-surface-poc/src/polaris-generation` = **17** (11 + 6); `packages/polaris-generation-core` + the same app directory = **20** (14 + 6). Over both sets the three plane literals occur **0** times and the network literals **0** times; `https://` occurs **3** times, at `packages/polaris-generation-core/src/provider-draft.test.ts` (1) and `apps/three-surface-poc/src/polaris-generation/draft-preview.test.ts` (2), all test fixtures. The packet now says "the 20 tracked files of `packages/polaris-generation-core` and …" at every site I found (Gate 1 item 1 line 206, Q3 line 37, Gate 2 line 564, Gate 6 item 2 line 1303, the summary lines 1510 and 1511) and in both evidence fields, with the superseded wording marked and dated |
| F2 | **REPAIRED** (one sub-claim of the disposition is wrong — see **G4**) | The module predicate re-derives **exactly** at `a9f671e`: 6 doctrine + 71 decisions (67 top-level + 4 under `launch-gate/`) + 28 RFC modules = **105 files / 1,266,454 bytes / 1,258,724 characters / 0 over the 100,000-character cap / largest 55,836**. The review's reading gives **107 / 1,369,266 / 1,360,678 / 0 / 63,903**, also as published. Both exclusions are now named at the packet's two sites and in the record's predicate |
| F3 | **REPAIRED** (the reproduction count is wrong — see **G3**) | I re-encoded the `inventory` envelope over the same 105 files at `a9f671e`, with `promptForStage('inventory')`, `stageSchema('inventory')` and the envelope `pipeline.ts` line 176 constructs, varying only the `sourceId` scheme and the reader-question array. **All eighteen published values reproduce byte for byte**: 1300688/1300601, 1297209/1297122, 1296894/1296807, 1298693/1298606, 1294916/1294829, 1294914/1294827, 1294601/1294514, 1294391/1294304, 1294181/1294094. None is 1,294,284; nearest 1,294,304, distance **20**. The limit probe re-derives (1,000,000 rejected `byte-limit`; 2,000,000 and 4,000,000 accepted). The table row now reads "about 1.29 MB, ± the id and question bytes" and the ×5 floor is restated on the approximate figure with the superseded exact one marked |
| F4 | **REPAIRED** | `.syzygy/governance/decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md` lines **29–30**, inside the Scope paragraph at **28–32**, read "REQ-polaris-generation-002, 004, 006, 009, 012, 014 and 019 take their full amended clauses and preserved scenarios" [Observed, opened at source]. Gate 5's opening sentence now places 009 with the overlay-cited half and lists only 003, 008, 010 and 020 as unamended; the superseded sentence is marked. REQ-009's overlay heading is at **241** and its text at **243**, both opened |
| F5 | **REPAIRED** | The population is named: the four envelopes carrying the plan today are `author`, `edit`, `fidelity` and `repair`, the last because `pipeline.ts` line **267** hands `repair` the accumulated `context` — verified at source: `context.draft = await stage('repair', { ...context, findings: verdict.findings });`. Reconciled at the site with Gate 4's "Exactly two envelopes change" |
| F6 | **REPAIRED** | Q1 now states the observed part exactly (RFC7-10 names five target classes and names no class for a file inside an observed repository) and carries the negative as `[Inferred]`, with the superseded `[Observed]` wording marked. Mirrored in the P-76 row. RFC7-10 read at source, `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md` 204–213; the packet's block quote of 204–213 and 215–223 is verbatim with no unmarked elision |
| F7 | **REPAIRED** in the prose and the intersection columns; **PARTIAL** in the table's two method columns (**G8**) and **NOT REPAIRED** in the evidence record's measurement block (**G9**) | The 27-file touch-set is correct: 24 (11 + 6 + 4 under `docs/polaris-generation` + `routes.ts` + the core README + `package.json`) plus the three Gate 3 paths, and I rebuilt both sets independently. Recomputed under membership at every current head — all nine intersection pairs reproduce exactly: M1 1/1, lane B 0/0 by span, M2 1/1, M3 0/0, M4 1/**2**, M5 1/**3**, M6 11/11, M8 4/**6**, M9 2/**3**. Lane B's diff predicate: `git diff -U0 a9f671e HEAD -- PROJECT-STATUS.md` in its worktree gives hunks at new lines **252** and **263**; M7 slice 5's target paragraph is `PROJECT-STATUS.md` **38–44**, both read at source — exactly as the repaired row says. M6's floor re-derives: 10 bare `pipeline.ts` spans, 0 full-path |
| F8 | **REPAIRED** in the prose; one resolved `[Unknown]` left standing (**G6**) and two sibling counts left stale (**G7**) | The unlabeled "disjoint by design" sentence is superseded in place with the measured rows beside it. Both rows hold at heads **later** than the packet names: M8 has moved `4b2e8cb` → **`bce9039`** and M9 `3e764d8` → **`65de02b`**, and recomputing at those heads gives the same figures — M8 **4** / **6**, M9 **2** / **3** [Observed, recomputed this session]. The claimant restatement is right: six packets place `apps/three-surface-poc/src/routes.ts` in a Gate 3 "Lives in" column — M2 slice 3, M4 slice 5, M5 slices 1 and 3, M7 slice 4, M8 slice 2 (its line 697), M9 slices 2, 4a and 6 (its lines 663, 665, 668), all opened this session at the current heads. M1's quoted sentence does begin on line **143** of `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md` and end on 144 |
| F9 | **REPAIRED** in the body; the superseded wording is reinstated unmarked in the funnel summary (**G2**) | `.syzygy/governance/doctrine/security.md` 25–37 names **two** of the five: "Onboarding consent must name the providers permitted for a governed project and the content classes that may be sent" (lines 30–32) [Observed, read at source]. Slice 5 now attributes two to SEC-2, one to REQ-001 (base line 12, quoted exactly — I opened it) and the route and retention to this packet's own proposal, labelled `[Inferred]`. The Gate 2 paragraph carries the same repair with the "field for field" wording marked superseded |
| F10.1 | **REPAIRED** | Registry line **53** is `"class": "git-tree-entry"`, line **54** the `identityScheme`. Corrected at Q1 (line 35) and Gate 3 slice 1 (line 587); the literal-sweep hit is left at 53, correctly. Both acts carry the path as "Artifact identity" at line 13 of each |
| F10.2 | **REPAIRED** | `openspec/changes/polaris-manifesto-generation/EXECUTION-PHASES.md` line **13** begins "It does not create or mutate live scheduler items," and line 14 completes it. Cited as 13–14 at both sites (Q2 line 36, Gate 3 line 620) |
| F10.3 | **NOT REPAIRED — and the close-out's NOT CONFIRMED judgment is CORRECT** | Opened myself. `apps/three-surface-poc/src/routes.ts`: line **136** is the comment "// Serves `body` only when its UTF-8 encoding fits the named ceiling.", line **137** is `export function boundedResponse(…)`, and line **142** is its closing brace (143 is blank). The packet's "lines 137–142" is exact and review 1's "declared at 138, closes at 143" is off by one in both directions. The close-out's recorded reason matches the bytes word for word |
| F10.4 | **REPAIRED** | `draft-preview.ts` line 23 is quoted in full at packet line 266, including the bracketed ordinal and the closing tag; byte-compared against source |
| F10.5 | **REPAIRED** | Base line 400 begins "An uncertain attempt SHALL continue to reserve its maximum charge…"; the packet writes "[a]n", marking the alteration |
| F11 | **REPAIRED** | Slice 5 now writes `.syzygy/governance/decisions/README.md` in full (it resolves), and names the bare spelling without a code span with the reason given. The record's note is corrected rather than left standing over the one entry it was false for |
| F12 | **REPAIRED** | `openspec/changes/polaris-manifesto-generation/tasks.md` §3 carries **seven** boxes — 3.1 (45), 3.2 (46), 3.3 (47), 3.4 (48), **3.4a (49)**, 3.5 (50), 3.6 (51) [Observed, enumerated with `^- \[[ xX]\] `]. 3.4a is on the buys side and the partition is stated over all seven. Whole file: **24** boxes, **0** checked, 51 lines by `wc -l` |

**Two findings of review 1's own are correctly corrected rather than
copied**, as the close-out claims: F4's anchor (29–30 inside 28–32, not
29–32) and F2's reading of "71" (which is the every-level count, 67 + 4).
Both hold at source.

---

## (b) Load-bearing measurements re-derived this session

Every figure below was recomputed in the worktree by driving the built
modules or by exact substring counting, never carried forward.

| Claim | Re-derives? | My figure |
|---|---|---|
| 17-file and 20-file censuses; 3 plane literals 0 / 5 network literals 0 / `https://` 3 on each | Yes, exactly | identical; `XMLHttpRequest` is also 0 on both (see **G13**) |
| Self-corpus 105 / 1,266,454 / 1,258,724 / 0 over cap / largest 55,836 | Yes, exactly, **at `a9f671e`** | identical; at HEAD it is 105 / 1,277,862 / 1,270,122 — see **G5** |
| The 107-file variant, 1,369,266 / 1,360,678 / 0 / 63,903 | Yes, exactly, at `a9f671e` | identical |
| The eighteen envelope encodings and the limit probe | Yes, exactly, all eighteen | identical; count mislabelled "twelve" — **G3** |
| Per-stage `inputBytes` 3,422 / 4,297 / 7,971 / 8,807 / 6,283, total 30,780 | Yes, exactly | identical, via a capturing `admit` port over the shipped garden fixture |
| Corpus 439 bytes; 70.1× | Yes | 439; 70.11 |
| Slope 439→30,780, 3,439→65,780, 6,439→100,780; 11.67 | Yes, exactly | identical; 70,000/6,000 = 11.667 |
| Envelope `inputs` key sets per stage | Yes, exactly | inventory {readerQuestions, sources}; plan +inventory; author +plan; edit +draft; fidelity {draft, inventory, plan, readerQuestions, sources} |
| Sentinel 1 / 2 / 2 / 4 / 4 = 13 | Yes — **only** with the sentinel in `mechanism`; in `purpose` it is 1/2/2/3/3 = 11 | identical to review 1's note, which is still unaddressed — **G14** |
| System prompts 1,971 / 2,371 / 2,459 / 1,968 / 2,515 (+repair 1,847); five-stage 11,284 | Yes, exactly | identical |
| Six schemas 14,155; author/edit/repair share one 3,961-byte object | Yes, exactly | identical, and the three JSON encodings are byte-equal |
| Prompt transmitted twice, billed once | Yes | `pipeline.ts` 176 embeds `system`, 219 passes it separately, 177–179 charge `Buffer.byteLength(encoded)` only |
| `routes.ts` 240 lines, 15 entries, 15 distinct paths, 4 machine-credentialed = 2 logical routes twice, 11 human-open | Yes, exactly | `pocRoutes()` on the built module returns 15 entries over 15 distinct paths; the four machine paths are `/api/poc`, `/api/poc/polaris` and their tailnet-mount twins |
| `generation` and `draft` 0 times case-insensitively in `routes.ts` | Yes | 0 and 0 over the 240-line file |
| The seven amended requirements include 009 | Yes | opened at the act, lines 29–30 |
| `git-tree-entry` occurrences across `.syzygy/` and `openspec/` | **Not at HEAD** | **3** over 619 tracked files at `1803608`; **1** at `a9f671e` — **G5** |
| 15 Gate 3 paths vs 21-file manifest population + the acceptance record: 0 hits each | Yes, exactly | 14 `*-MANIFEST.txt` + 7 `docs/evidence/*manifest*.json` = 21; 0 hits for all 15 |
| Synthetic-verification record: 17 rows, all 17 equal current bytes | Yes, exactly | 17 matching, 0 mismatching, sha256 recomputed per row |
| Generator scope record: 21 rows, all under the package directory, 0 implementation paths, `implementedGenerator` false | Yes, exactly | identical |
| `tasks.md` 24 boxes, 0 checked, 51 lines | Yes, exactly | identical |
| Packet self-census: 298 distinct spans, 78 slash-bearing, 19 not resolving, 0 odd-backtick non-fence lines, 10 over-width | Yes, exactly, and the 19 enumerated entries match one for one | identical; over-width at lines 1, 6, 205, 266, 652, 717, 806, 848, 975, 986 |
| Collision table: nine intersection pairs and the M6 floor | Yes, exactly, at every current head | see F7/F8 above |
| Register recount 21/5/26 at `a9f671e` and 22/5/27 here | Yes, exactly | identical under `^| P-` partitioned by `##` section |
| `check_governance.py` ends `0 FAIL` | Yes | tail line read in full |

### Contract and specification citations opened at source (rule 8)

All exact unless a finding says otherwise.

- **RFC7-10**, `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`
  204–213 with its target-state paragraph 215–223: the packet quotes both
  whole, verbatim, no unmarked elision.
- **RFC7-21**, same file 398–406: the packet's "The adopter attests per
  claim block… no draft is adopted by signature over an unattested whole"
  is verbatim with the elision marked.
- **RFC2-26**,
  `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`
  196–221 under the `###` heading at 194: both paragraphs verbatim, and
  the package-scope sentence does sit at 219–220.
- **SEC-2**, `.syzygy/governance/doctrine/security.md` 25–37: verbatim,
  source emphasis preserved, none added.
- **VIS-1** at `vision.md` 82; **VIS-2** at 96–106 with a marked ellipsis;
  **VIS-4** at 122–139, its RFC-acceptance sentence at 122–124 and its
  always-human-gated sentence at 131–132; **VIS-5**'s "materialization is
  exclusively a worker action against scheduled work" at 158–159.
- **Implementation act line 42**, the "Real-project reads, provider egress
  and destination writes remain separately admitted" sentence: verbatim.
- **EXECUTION-PHASES.md** lines 4, 13–14, 18 and 19: all verbatim.
- **Base spec**: REQ-001 at 12; REQ-003 at 98 with scenarios 105–109 and
  111–115; REQ-006 at 302; REQ-008 at 400 with scenarios 407–411 and
  413–417; REQ-010 at 528; REQ-020 at 1083. **Overlay**: REQ-006 at 180;
  REQ-009 at 241/243 with "Changed source" at 250–254; REQ-014 at 367.
- **Source anchors**: `pipeline.ts` 19, 60–64/65, 90–96, 103–115, 122, 137,
  170, 176–179, 180–185, 219, 253, 259–269, 272 (276 lines);
  `provider-draft.ts` 15, 90–98, 109–112, 137, 148–152 (152 lines);
  `prompts.ts` 9 and 21 (29 lines); `pipeline.test.ts` 73–76 with the
  5-send assertion at 76; `polaris-source.ts` 31–42 and `sourceRouteHref`
  at 41–43 under its doc comment at 40; `draft-preview.ts` 11 and 23;
  `packages/polaris-generation-core/README.md` 39 carries "It has no
  default network client"; `PROJECT-STATUS.md` 38–44;
  `docs/polaris-generation/README.md` line 4 and "Start here" 37–44. All
  resolve as cited.

---

## New findings

### G1 — non-blocking — the funnel summary still says four packets edit `routes.ts`

`docs/design/POLARIS-M7-GENERATION-LOOP-FUNNEL.md` line 1518.

**Defect.** The summary's Collision line reads "routes.ts shared with M2,
M4 and M5 - four packets propose editing the same 240-line file". F8's
repair restated that to **six** (M2, M4, M5, M7, M8, M9) at the body site
(line 1210) with the superseded wording marked, and I verified all six at
source. The summary carries the pre-repair count with **no** supersession
mark, in a fenced block whose neighbouring lines 1510, 1512, 1515 and 1517
all carry one — so this is an omission of the same pass, not a convention.
[Observed, both sites read this session.]

**Repair.** Restate as six and mark the superseded four in place, as lines
1515 and 1517 already do.

### G2 — non-blocking — the summary reinstates the exact wording F9 superseded

Line 1511: "SEC-2 as the whole content of slice 5".

**Defect.** F9's finding was that "That sentence is the whole content of
slice 5: it names, field for field, what the egress act would have to say"
is a contract claim wider than the clause it is anchored to — SEC-2 names
two of the five fields. The Gate 2 paragraph (557–563) and slice 5
(850–869) are repaired and the superseded wording is marked at both. The
funnel summary restates the superseded claim in five unmarked words. A
reader who reads only the summary — which is the block written to be
lifted out — gets the finding back. [Observed, SEC-2 read at source;
`security.md` 30–32 names providers and content classes and nothing else.]

**Repair.** "SEC-2 naming two of slice 5's five fields, the other three
attributed at the site".

### G3 — non-blocking — "twelve reproductions" is eighteen

Packet lines 376, 387, 394 and the F3 disposition row at 1470; evidence
record `review1.disposition_summary.F3`.

**Defect.** The F3 repair says "Twelve reproductions were run" and "every
one of the twelve variants". What is published beside the sentence is
**nine** `sourceId` schemes each at **two** reader-question arrays — the
record's `review1.f3_reproduction.bytes_by_scheme` has nine keys, each with
`demo_3` and `empty` — i.e. **eighteen** encodings, and the packet's own
list at 379–386 prints eighteen values. I reproduced all eighteen exactly
(see (b) above). This is a count that does not re-derive over the data
printed next to it, inside the repair of a finding about a figure that did
not re-derive, in a packet whose Gate 6 item 1 claims every count carries
its predicate and denominator. [Observed, eighteen encodings run this
session against the built package over the `a9f671e` corpus.]

**Repair.** "Eighteen reproductions — nine `sourceId` schemes × two
reader-question arrays", at all four sites and in the record.

### G4 — non-blocking — the "101" attributed to the record's literal predicate is 103

Packet line 1460 and the F2 disposition row at 1469; record key
`measurements.self_corpus` → `review1.f2_predicate_variants.`
`as_written_top_level_decisions_plus_all_rfc_md`.

**Defect.** The close-out says the superseded record predicate, "read
literally (top-level decisions + every `.md` under `rfcs/`)", gives **101**
files / 1,206,681 bytes, and uses that to correct review 1's reading. Run
at `a9f671e`: 6 doctrine + **67** top-level decisions + **30** tracked
`.md` under `rfcs/` = **103 files / 1,309,493 bytes / 1,301,412 characters
/ 0 over the cap / largest 63,903**. The published {101 / 1,206,681 /
1,199,458 / 0 / 55,836} is 6 + 67 + the **28 RFC modules** — the strict
reading of the decisions half combined with the *corrected* reading of the
rfcs half, which is not what "read literally" names. The record's key name
asserts the same composition. [Observed, all four compositions computed at
`a9f671e` from `git ls-tree` blobs this session.]

**Not a defect in the outcome.** The adopted 105-file figures are
unaffected and re-derive exactly, and the conclusion that both halves of
the superseded phrase were wrong stands.

**Repair.** Either restate the literal reading as 103 / 1,309,493 /
1,301,412 / largest 63,903, or rename the variant to what it actually is
(top-level decisions + RFC modules) and add the true literal reading.

### G5 — non-blocking — two self-referential measurements are falsified by this packet's own register commit

(a) Q1, packet line 35; (b) Q2 line 36, "What a real corpus costs" 341–370,
slice 3 line 771, oracle line 788, S6 line 1118.

**Defect (a).** Q1 states, as part of its load-bearing evidence, "the
literal `git-tree-entry` occurs **1** time across every tracked file under
`.syzygy/` and `openspec/`, at line 53) [Observed, literal sweep this
session, denominator the two governed trees]". At HEAD it occurs **3**
times over **619** tracked files: the registry entry line 53, and
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` lines **114** and
**221** — the P-76 blockquote and row this same commit added. At `a9f671e`
it is 1. The claim carries no commit anchor at its site and the packet's
own close-out falsified it. [Observed, swept this session at both trees.]

**Defect (b).** The self-corpus byte figures are taken over a corpus that
*includes* `.syzygy/governance/decisions/`, so the P-76 row moved them:
105 / **1,266,454** / **1,258,724** at `a9f671e` and `0c4b4a9`, but 105 /
**1,277,862** / **1,270,122** at `1803608` — 11,408 bytes. The file count,
the cap result and the largest source are unchanged. The "Measurements at
`a9f671e`" heading anchors the table; the Q2 table row, slice 3's corpus
paragraph, slice 3's oracle and S10's sibling S6 are not anchored, and Q2
is what the owner reads. [Observed, computed at all three revisions.]

**Repair.** Anchor both at the site — "1 at `a9f671e`; 3 at this commit,
the two additions being this packet's own register row" and "1,266,454
bytes at `a9f671e`" — rather than relying on a section heading 300 lines
above. This class will recur: every future decision row moves the corpus.

### G6 — non-blocking — the packet's own "Not verifiable this session" block carries an `[Unknown]` the same packet resolved

Line 1289.

**Defect.** "**[Unknown]** Whether M8 or M9 will claim any file in M7's
24." That question is answered twenty lines earlier, at 1256–1269, with
measured rows (M8 4 of the 24 and 6 of the 27; M9 2 and 3) — figures I
recomputed and which hold even at the two later heads. The evidence
record's twin entry *is* marked, "[RESOLVED 2026-09-15; see
review1.could_not_verify_resolved]"; the prose is not. This is precisely
the failure mode F8 named and the close-out quoted approvingly: "The
`could_not_verify` entry covers this honestly; the prose sentence does not,
and a later reader will read the sentence, not the record."

**Repair.** Mark the line resolved in place, pointing at the measured rows.

### G7 — non-blocking — two sibling counts went stale when the table grew from seven rows to nine

Lines 1199 and 1286; record `could_not_verify[0]`.

**Defect.** Line 1199: "The other **six** siblings have committed **0**
implementation-plane files". The collision table now has nine rows, so the
others are **eight** — M1, M2, M3, M4, M5, M6, M8 and M9 — and all eight
have committed zero implementation-plane files [Observed, `git diff
--name-only a9f671e HEAD` in each worktree this session: M2–M6, M8 and M9
each touch only the register, their own `docs/design` packet, their own
`docs/evidence` record and their own retained raws]. Line 1286 and the
record's first `could_not_verify` entry both say "five of the six have
committed no implementation file at all"; it is now seven of the eight.

**Repair.** Re-derive both against the nine-row table and mark the
superseded counts.

### G8 — non-blocking — the collision table's two method columns do not re-derive under the method the repair states

The method paragraph at 1144–1147, the supersession at 1157–1163, the table
header at 1165, and the F7 disposition row at 1474.

**Defect.** The stated method is "extract every code span from each
sibling's packet file and keep those that resolve as a real **file** in
this worktree (`os.path.isfile`); intersect with M7's own **27-file
touch-set**", and both the supersession note and the F7 row say the prefix
filter "is dropped in favour of membership". But the table's second and
third columns are still headed "Prefixed spans" / "Resolving as files" and
still carry the prefix-filtered figures. Run under the stated method the
resolving counts are **M1 4, lane B 9, M2 25, M3 28, M4 39, M5 20, M6 30,
M8 75, M9 37**; the published 1 / 0 / 11 / 13 / 22 / 9 / 13 / 51 / 13
reproduce **only** with the prefix filter applied [Observed, both sweeps
run this session over all nine]. A reader re-running the stated method
gets different numbers in two of six columns — rule 2's shape.

**Not a defect in the result.** The two intersection columns are correct
under membership and I reproduced all nine pairs exactly; the prefix filter
changes no intersection now that `PROJECT-STATUS.md` is reached by
membership.

**Repair.** Say at the table that the two span columns keep the first
draft's prefix predicate and only the intersections use membership, or
recompute the two columns under membership.

### G9 — non-blocking — the evidence record's `file_set_intersection` measurement block is unrepaired and unmarked

`docs/evidence/polaris-m7-generation-loop-funnel-2026-09-15.json`,
`measurements.file_set_intersection`.

**Defect.** `predicate` still reads "code spans … that begin `apps/`,
`packages/`, `scripts/`, `docs/polaris-generation/` or `package.json` AND
resolve as a file … intersected with M7's **24-file candidate surface**";
`m7_surface_size` is **24**; `rows` holds **seven** entries with no 27-file
column and no M8 or M9 row. The repaired figures live only in
`review1.f7_collision_recomputed`. The sibling blocks
`measurements.plane_disjointness` and `measurements.egress_surface` both
took an inline "[corrected 2026-09-15, review 1 F1 …]" bracket; this one
took none, and nothing in `measurements` points at the repaired block. A
consumer reading the measurement section gets the superseded predicate with
no signal that it is superseded. [Observed, record parsed this session.]

**Repair.** Mark the block in place and point at
`review1.f7_collision_recomputed`, as the two sibling blocks are marked.

### G10 — non-blocking — the record's `shared_governance_file` block is false in four respects and unmarked

Same file, `measurements.file_set_intersection.shared_governance_file`.

**Defect.** `touched_by_M7` is `false` — this commit modifies
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`. `touched_by`
lists six siblings; it is eight. And `disclosure` still reads, in the
present tense and unmarked: "This packet writes exactly two files and no
register row, by instruction… This worktree's register ends at P-53, as do
M8's and M9's. The next free number at the time of writing is P-74;
whoever files it should re-derive it". All three sentences are now false.
Recounted this session at every current head, predicate `^| P-`
partitioned by the `##` section: **all nine registers hold 27 rows (22
open + 5 acceptance-act)** and each carries exactly one row above P-53 —
P-68 lane B `4090f98`, P-69 M2 `f2f37dd`, P-70 M3 `6574600`, P-71 M4
`63b8e33`, P-72 M5 `ba9ca61`, P-73 M6 `83c9f60`, **P-74 M8 `bce9039`**,
**P-75 M9 `65de02b`**, P-76 M7 `1803608`.

**Not a defect in the packet.** The prose superseded all of this correctly
at 1241–1254 and `review1.register_row` carries the recount (21/5/26 at
`a9f671e`, 22/5/27 here — both reproduce exactly). Only the measurement
field was left behind.

**Repair.** Mark the three sentences in place and set `touched_by_M7` and
`touched_by` from the current heads.

### G11 — editorial — `packet_measured.measured` asserts a currency its own sibling key denies

Same file, `packet_measured`.

**Defect.** The block reports the first draft's figures — 109383 bytes, the
`0c4b4a9` sha256, 1312 lines, 264 distinct spans, 35 non-resolving,
over-width lines [205, 889]. The disclaimer that these describe `0c4b4a9`
is appended to the **end of `slash_bearing_note`**, a key about a different
subject; one key below it, `measured` still reads "after every other edit
in this pass, so the figures are true of the bytes they describe", which is
false of these bytes. A reader who opens `bytes`, `sha256` or
`over_width_lines` never reaches the note.

**Not a defect in the figures.** `review1.post_repair_measurements` carries
the current census and every value in it re-derives exactly: 139264 bytes,
1584 lines, 298 distinct spans, 78 slash-bearing, 19 not resolving with the
list matching entry for entry, 0 odd-backtick non-fence lines, and
over-width count 10 at lines 1, 6, 205, 266, 652, 717, 806, 848, 975, 986
[Observed, all recomputed this session].

**Repair.** Move the "describes `0c4b4a9`" clause into `measured` (or into
a `describes_commit` key), so the assertion of currency does not stand.

### G12 — editorial — the packet states its over-width predicate two ways and the published list satisfies only one

Gate 6 item 11 (line 1363) against line 1499–1501.

**Defect.** Gate 6 says over-width lines are counted "outside fences,
tables, block quotes and headings"; the count is published at 1501 as
**10** under "lines outside fenced code blocks whose first non-space
character is not a pipe". Under Gate 6's words the figure is **4** (lines
205, 266, 975, 986); the published 10 includes line **1** (the H1 title,
162 columns) and line **6** (a banner block-quote line, 79) [Observed, both
predicates run over the file this session]. The record's
`packet_measured.over_width_predicate` uses a third spelling (excluding
pipe, `#` and `>`), while `post_repair_measurements` uses the pipe-only
one, so the number and its description disagree in the record too.

**Repair.** Make Gate 6 item 11 name the pipe-only predicate the published
number is taken under.

### G13 — editorial — the SEC-2 sweep enumerates five network literals where the record and the packet's own F1 row say six

Packet lines 566–567 against the F1 disposition row (1468) and the record's
`measurements.egress_surface.predicate`.

**Defect.** Gate 2 lists `fetch(`, `node:http`, `node:https`, `undici` and
`axios` — five. The record's predicate adds `XMLHttpRequest`, and the F1
row says "the **six** network primitives **0** times on each". A reader
re-running the enumerated five is running a weaker sweep than the one the
figure is claimed over.

**Not a defect in the result.** All six are **0** over both the 17-file and
the 20-file sets [Observed, recomputed this session].

**Repair.** Add `XMLHttpRequest` to the enumeration at line 566.

### G14 — editorial — a third review-1 observation is neither applied nor disclosed

Review 1's "Measurements re-derived" table, sentinel row; packet 1418–1429;
record `measurements.stage_envelopes.method`.

**Defect.** Review 1 recorded that the sentinel figure re-derives "only
with the sentinel in the **mechanism** source" and that with it in
`purpose` the counts are 1/2/2/3/3 = 11 rather than 1/2/2/4/4 = 13 —
"worth one clause in the evidence record". I reproduced both. The close-out
says "**Two** observations in that table are not among F1–F12 and are
carried here rather than applied", which is accurate about the
five-question table but leaves this third observation, from the
measurements table, neither applied, carried nor mentioned; the record's
method still says only "a sentinel string placed in one source text".

**Repair.** Name `mechanism` in the record's method, or carry the
observation as a third unapplied one.

### G15 — editorial — the register renders the raw's gate column without its two qualifiers

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` line 221 (the
P-76 row's sources column) and the blockquote at 127–128.

**Defect.** Both say the review "found all five questions to be genuine
hard gates". The raw's column answers are, exactly: Q1 "**Yes.**"; Q2
"**Yes, but the weakest of the five.**"; Q3 "**Yes**, though it is a
question *about* a question already before the owner"; Q4 "**Weakest as a
gate.** … the recommended path dissolves the question. The gate is real
only on the file-writing limb"; Q5 "**Yes.**". Q4's cell never says yes.
The packet's review-1 section carries both qualifiers verbatim (1410–1412);
the register — which is where the owner meets P-76 — flattens them.

**Repair.** Add "Q2 called the weakest of the five and Q4 weakest as a
gate, with the recommended arm dissolving Q4 except on its file-writing
limb" to the row's one-line review summary, as the packet already does.

### G16 — editorial — Q1's fourth lawful arm is disclosed 1,390 lines below Q1

Packet Q1 row (line 35) against 1418–1429 and the P-76 row.

**Defect.** The five-question table's Q1 row names three lawful arms and a
default. The fourth arm review 1 identified — rule RFC7-10 **not engaged** —
and the disclosure that Q1's default is the only one of the five that ships
rather than holds appear only in the review-1 section and in the register
row. Both are carried **faithfully and unsmoothed** in both places, and the
decision not to fold them into the question is correctly reasoned (adding
an arm changes what is put to the owner). But an owner reading the question
table alone sees three arms and a ship-by-default with no flag.

**Repair.** One clause in the Q1 row pointing at the review-1 section.

---

## (c) The register

| Question | Answer |
|---|---|
| Is the P-76 row a faithful one-line rendering of Q1–Q5 after the repairs? | **Yes.** All five questions, each with its recommended arm, every named lawful arm, its default-if-unanswered and its counter-argument at strength; Q1's `[Observed]`/`[Inferred]` split is mirrored; the "20 tracked files" denominator is the corrected one; the six-packet `routes.ts` restatement is carried. Compared clause by clause against the packet's table this session |
| Are the two carried owner-facing observations in the row? | **Yes**, both, in Q1's paragraph and named as unapplied and as the owner's own reading — "Review 1 names **a fourth lawful arm this packet does not offer**… and notes that Q1's default is **the only one of the five that ships rather than holds**" |
| Does the blockquote's verdict word match the raw? | **Yes, exactly**: "CONFIRM WITH EXCEPTIONS". Counts "0 blocking, 9 non-blocking, 3 editorial, F1–F12" match the raw's summary exactly |
| Is the recount reproducible by a stated predicate? | **Yes.** Predicate `^| P-` partitioned by the `##` section each row falls under: `a9f671e` gives **21 open / 5 acceptance-act / 26**, `1803608` gives **22 / 5 / 27** [Observed, run against both trees this session] |
| Does it correctly state which sibling rows live only on their branches? | **Yes**, and I recounted all nine registers at their current heads. Each holds 27 rows and carries exactly one row above P-53: P-68 lane B `4090f98`, P-69 M2 `f2f37dd`, P-70 M3 `6574600`, P-71 M4 `63b8e33`, P-72 M5 `ba9ca61`, P-73 M6 `83c9f60`, **P-74 M8 `bce9039`**, **P-75 M9 `65de02b`**, P-76 M7 `1803608`. M8 does carry P-74 and M9 P-75 |
| Does the row quote a digest or backtick an observed-repository path? | **No** to both. The only long hex in the register is one pre-existing value outside this row; the P-76 row carries none, and no observed-repository path appears in it. `check_governance.py` ends `0 FAIL` |
| Anything wrong in the row? | One: **G15**, the unqualified "all five … genuine hard gates" |

The blockquote is dated and marks itself as an update; it does not restate
any claim it does not own beyond the recount, which it derives at the site.

---

## (d) The five questions, re-examined

| # | Scope truthful? | Genuine hard human gate? | Recommendation follows? | Every lawful arm named? |
|---|---|---|---|---|
| Q1 `git-tree-entry` vs RFC7-10 | Yes. Clause, registry entry (53/54) and both binding acts are exactly where the repaired text says, and neither artifact may be edited. One measurement inside the row is now false at HEAD — **G5(a)** — without touching the argument | **Yes.** Reading a sixth target kind into a list RFC7-10 closes with "No target class exists for narrative content, renderings, or editorial drafts" is an accepted-contract reading, and VIS-4's first sentence names RFC acceptance shape-defining (read at source, 122–124) | Yes, and F6's split sharpens it rather than moving it: the recommended arm, the three arms and the default are unchanged | **Three in the row, the fourth disclosed elsewhere.** The fourth arm (clause not engaged) and the ship-by-default disclosure are carried faithfully at 1418–1429 and in the P-76 row, unsmoothed — but not in the Q1 row itself (**G16**). Q1's ship-by-default posture **does stand disclosed**, in both carrying places, in the raw's own words |
| Q2 self-corpus read | Yes. The act's reservation is verbatim at line 42; the corpus figures re-derive exactly at the baseline (**G5(b)** on currency) and both exclusions are now named | **Yes**, and the raw's "weakest of the five" is carried in the packet but not the register (**G15**) | Yes; the counter-argument ("building the pipe before the egress act exists") is given its full weight | Yes — rule it a self-read, or the narrow direction; declining folds into the default, "slice 3 does not ship" |
| Q3 draft route category | Yes. P-72's Q1 is quoted from M5's packet at `ba9ca61`, and the membership test genuinely fails: 0 references to the observation plane across the 20 tracked files, recomputed | **Yes**, with the packet's own honest caveat that it is a question about a question already before the owner | Yes | Yes for the two numbered, plus the disclosure that P-72's arm (c) has no counterpart here |
| Q4 drafted act | Yes. P-71's arms are reported as they stand at `63b8e33`, and RFC7-21 398–406 is quoted correctly | **Qualified**, as the raw says: the recommended arm "needs no act on anyone's reading", so the gate is real only on the file-writing limb. Carried in the packet, flattened in the register (**G15**) | Yes; the counter-argument ("satisfies the letter and strains the intent") is not smoothed | Yes: arm (b) now, wait for P-71, or the file-writing limb under P-71's arm (a) |
| Q5 admit port reserve/complete | Yes. The comment at `pipeline.ts` 60–64, the declaration at 65, the test pin at `pipeline.test.ts` 73–76 with the 5-send assertion at 76, and REQ-008's scenario at base 407–411 are all exactly as described, and the mismatch is genuine | **Yes.** A reviewed safety property at the one boundary where a mistake spends real provider effects; VIS-4's always-human-gated class reaches normative data contracts | Yes, with the retained-prohibition condition carried into the recommendation | Yes, and the default is the conservative arm |

**No lawful arm is called unlawful anywhere** [Observed, all five rows and
the register row read against each other this session]. **No owner
trade-off is smoothed in the packet**; the one flattening is in the
register's summary of the *review*, not of a question (**G15**). **Every
question states a default-if-unanswered**, and four of the five default to
not shipping. **RFC2-26's reviewed-N/A-judgment arm is named where a slice
could reach it** — slice 2, at Gate 5's Limb-1 column, with the clause's
own two repair routes quoted and the packet declining to choose; the other
slices either map to a requirement-and-scenario pair or enumerate no
RFC-0002 consequence, so the arm is not reachable for them. **No P-71, P-72
or P-73 question is re-asked.**

---

## Note on this file's own name

AGENTS.md's guardrail is that a retained raw's filename must end in
`-RAW.md`, because `check_governance` exempts only that suffix from CG-1b
and CG-15. This raw is written to the scratch path the brief names; if it
is retained in the repository it must land as a second `-RAW.md` file
beside the first (never an overwrite of it), in the siblings' shape.

---

## Summary

- blocking: **0**
- non-blocking: **10** (G1–G10)
- editorial: **6** (G11–G16)

Eleven of review 1's twelve exceptions are **REPAIRED** against source; the
twelfth, F10 item 3, is correctly **NOT** applied — I opened
`apps/three-surface-poc/src/routes.ts` myself and the packet's "lines
137–142" is exact, with the comment at 136, the declaration at 137 and the
closing brace at 142. Two of the repairs are incomplete rather than wrong:
F7's method columns still carry the dropped prefix filter (G8) and its
evidence-record block was not touched at all (G9). Everything the packet
publishes as a measurement re-derives exactly at the commit it names —
every byte figure, every anchor, all eighteen envelope encodings, all nine
collision pairs at heads later than it read, both register recounts, the
whole self-census of its own bytes — with two exceptions, both of which the
packet's own register commit created (G5) and one of which is a "1 time
across every tracked file" claim that is now 3.

The new findings are of three kinds: wording the repair pass reinstated or
left behind in the funnel summary and the "Not verifiable" block (G1, G2,
G6, G7); counts and predicates inside the repairs themselves that do not
re-derive over the data printed beside them (G3, G4, G8, G12, G13); and an
evidence record whose `measurements` section was largely not carried
forward with the packet (G9, G10, G11). None of them moves an arm, a
recommendation or a default, and none of them is a reason to hold P-76.

Verdict: CONFIRM WITH EXCEPTIONS
