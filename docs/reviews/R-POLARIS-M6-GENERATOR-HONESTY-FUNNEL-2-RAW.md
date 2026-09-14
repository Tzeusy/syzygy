# R-POLARIS-M6-GENERATOR-HONESTY-FUNNEL-2 — raw review

Review 2 of the M6 generator-honesty funnel packet. Fresh context,
read-only, independent reviewer (Claude), 2026-09-15. This review verifies
the review-1 repairs and re-runs the load-bearing measurements so that its
own bytes carry their own verification.

## Bound bytes

Worktree: the M6 review worktree on branch `agent/syzygy-dov.6`, HEAD
`e318cbd` ("docs: M6 funnel review 1 (REVISE) repaired, raw retained, P-73
registered"). Its parent is `91b1343` and its grandparent `a9f671e`, the
packet's stated baseline. `git status --short` was empty before this review
and empty after it; no tracked file and no `node_modules` entry was
modified. The demo was run twice with `--out` under this session's scratch
directory only.

| Artifact | Bytes (`wc -c`) | sha256 (`sha256sum`) |
|---|---:|---|
| `docs/design/POLARIS-M6-GENERATOR-HONESTY-FUNNEL.md` | 116325 | da54c37407644627352e835dcf15bf182da40ba723ea9a673efcd5ff329075aa |
| `docs/evidence/polaris-m6-generator-honesty-funnel-2026-09-15.json` | 51469 | a90840448f34c85102e13cd89c1cadc311c91c66eaf8c3fb20efa5221aa4149c |
| `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` | 30541 | 52ba85289540edefa5f83d8b74be35fd6bc11f34f13b0e5ab7fae2a1a876b826 |
| `docs/reviews/R-POLARIS-M6-GENERATOR-HONESTY-FUNNEL-RAW.md` | 35780 | c6e307a55e9215a2d9d884936cb295cef7b6ae1a8fff6a01c60905de78bb581b |

All four digests computed with `sha256sum` this session, never transcribed.
No act argument, no manifest row and no truncated signed digest is
reproduced anywhere in this review; every digest record consulted is cited
by path. No observed-repository path is backticked.

Rule 10: this review is bound to those exact bytes. Any later edit to any
of them retires it.

## What was re-run and reproduced exactly

[Observed, all this session in the worktree at `e318cbd`.]

- **Schema field census** (the prompt's 25/0/2). Imported `stageSchema`
  from the package's own built `dist/provider-draft.js`, walked all six
  stage schemas, collected every `properties` key and every `enum`. Per
  stage: `inventory` 5, `plan` 5, `author` 15, `edit` 15, `repair` 15,
  `fidelity` 6 — and the field *names* in each row match the packet's
  table one for one. Distinct across all six: **25**. Enums: **2**
  (`entries[].kind`, 9 values; `findings[].severity`, 2), **11** enum
  values. Under the packet's predicate, **0** of the 25 and 0 of the 11
  qualify. Second method (rule 2): Python `re`, case-insensitive, for
  `disposition`, `unresolved` and `unnecessary` over `provider-draft.ts`
  and `pipeline.ts` returns 0 and 0 in both files. The two methods agree.
- **`author`, `edit` and `repair` are one object.** The three returned
  schemas are byte-equal under `JSON.stringify` once `version` is removed;
  declaration at `packages/polaris-generation-core/src/provider-draft.ts`
  line 33, as quoted.
- **`example.json` 19 of 19.** 18 `validateStage` calls (six landed stages
  × `illustrativeOutput`, `illustrativeLaterDraft`, whole file) all throw
  `invalid-fields`, 0 passes, plus `stageSchema('understand')` throwing
  `invalid-stage`. `illustrativeOutput`'s five keys are exactly
  `editorialState`, `claims`, `unresolved`, `assetDispositions`,
  `coverage`, none of them in the 25-name census; `check()` at lines 61–63
  rejects on key-set inequality before contents. `exampleKind` is
  `synthetic-documentation-handoff` and `schemaStatus` is
  `candidate-not-registered`, both as stated.
- **`tasks.md` 24/0.** Predicate `^- \[[ xX]\] `: **24** boxes, **0**
  checked, over a 52-line file under the packet's stated split-on-newline
  convention (`wc -l` 51). Tasks 1.4, 2.2, 2.4 and 3.5 are at lines 11,
  22, 24 and 50 and their quoted texts are verbatim.
- **Demo exit code and output bytes.** Run as-is after `npm ci`: exit
  **0**, stdout exactly the success line the packet quotes. Two runs into
  two separate scratch directories: **7** files and **87,940** bytes both
  times, and the per-file list (11,308 + 15,713 + 11,395 + 15,981 +
  11,313 + 15,655 + 6,575) matches the packet's addends exactly. Output is
  deterministic.
- **Prompt directive count and sweeps.** `prompts.ts` is 30 split-lines
  and 7,517 bytes. The five directives are at lines 6, 13, 18, 21 and 22
  and each is verbatim at source. Corroborating sweeps reproduce exactly:
  `unresolved` 6 (lines 6×2, 10, 13, 21, 22), `disposition` 5 (10, 13, 16,
  21, 22), `omission` 2 (10, 20), `unsupported` 5, `omitted` 0, `unknown`
  1 (line 27, the error string).
- **Absence claim.** `context.draft` occurs at exactly lines 124 and 126
  of `provider-draft.ts`, both inside the `fidelity` branch; `priorDraft`
  0; the `else` branch at 131–144 reads `context.plan` at 133, 134 and
  137 only. File is 152 lines by `wc -l`, 153 split-on-newline, as the
  stated convention says.
- **Register recount.** Predicate `^| P-` partitioned by the `##` section
  each row falls under: at `a9f671e` 21 open + 5 acceptance-act = 26; at
  `e318cbd` **22 open + 5 = 27**, the single new id being P-73. The
  blockquote's figures are exactly reproducible by the predicate it
  states. (Incidental, and not M6's doing: the file carries 27 rows over
  26 distinct ids at this head and 26 over 25 at `a9f671e`, so one P-id is
  duplicated on both sides. It does not move the partitioned counts.)
- **Governance battery.** `python3 scripts/check_governance.py` in this
  worktree ends `32 OK, 20 WARN, 0 FAIL (52 checks)`, matching the record's
  stated last line. No finding names the packet, the evidence record or
  the P-73 row.
- **Packet convention self-checks, Gate 6 item 11.** All reproduce to the
  digit at the current bytes: **1,299** non-fence lines, **0** with an odd
  backtick count, **2** lines over 78 columns outside fences, tables and
  headings (at 760 and 890, matching the record's `lines_over_78_at`),
  **6** under the prompt's predicate that keeps headings, **295** distinct
  code spans, and **10** slash-bearing spans that do not resolve — exactly
  the ten enumerated.

### Contract and doctrine quotations, spot-checked at the cited line (rule 8)

All verbatim at the defined clause unless noted under Findings.

- Overlay requirement paragraphs at lines 9 (REQ-002, heading 7), 78
  (REQ-004, heading 76), 180 (REQ-006, heading 178) and 453 (REQ-019,
  heading 451). Predecessor: REQ-002 at 52, REQ-003 at 98, REQ-004's
  disposition sentence at 186, REQ-006's coverage sentence at 302,
  REQ-019's disposition sentence at 1015. Every sentence the packet
  block-quotes is contiguous at its cited line, tested by substring after
  whitespace normalisation.
- Both REQ-003 quotations — "distinguish source claims, supported
  inference and non-normative framing…" and "The versioned bundle SHALL
  distinguish narrative sections, contents, glossary…" — are in the same
  paragraph at base line 98.
- `SCHEMA-CONTRACT.md`: heading at 26, the requested/output distinction
  at 28–31 including "Requiredness cannot be downgraded by provider
  output", the declaration "Each request resolves to exactly one
  disposition:" at **33**, and the three-row table at 35–39 with every
  payload and invariant the packet quotes field-for-field.
- `EXECUTION-PHASES.md`: Phase A's scope sentence at 10–11 and
  "Requirements 001-012, 014-019 and 025" at **18**, both verbatim.
- `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md` line 42 is
  quoted verbatim, whole.
- **RFC2-26**: heading at 194, clause at **196–221**. The packet's block
  quote is byte-identical to the source after whitespace normalisation,
  with no elision. The scope sentence "This clause binds the whole RFC
  0002 package, not this module alone." does span **219–220**, with line
  221 carrying the shape-parallel list — the F7(a) correction is exact.
  The reviewed-N/A-judgment arm (RFC3-15 home, honored only through an
  effective owner act under RFC3-16(a)) is present in the slice-4 row.
- Doctrine: VIS-2 at 96–106 including "a stale view silently green";
  VIS-3 at 108–121; VIS-4's "One class is always human-gated, gate open or
  not: … normative data contracts" at 131–133; VIS-5's "materialization is
  exclusively a worker action against scheduled work" at 158–159; SEC-1 at
  line 10; SEC-2 at 25–37. The S9-F4 tag correction from SEC-1 to SEC-2 is
  right. One emphasis deviation, G9.
- Bound-byte constraint (b): `SCHEMA-CONTRACT.md`'s current sha256 does
  equal the value recorded for that path under `subjectBindings` in the v2
  coverage record. Verified by comparison; neither value reproduced.
- Bound-byte constraint (c): the scope record's `status` is "unadopted;
  awaiting final independent review and owner acts", `implementedGenerator`
  is false, over **21** file rows, and all five named package-contract
  files are rows.
- F10's record: `docs/evidence/polaris-pipeline-synthetic-verification-2026-09-13.json`
  carries **17** source rows; **17 of 17** equal their files' current
  bytes, including `provider-draft.ts` and `draft-preview.ts`. Compared,
  neither value reproduced.

## Review-1 repair verification, F1–F13

| # | Severity (rev 1) | Verdict | Evidence |
|---|---|---|---|
| F1 | blocking | **REPAIRED** | All four sub-repairs verified against source, not against the review. (a) The act's lines 39–41 are quoted at Gate 0 ("What the understanding act does not grant") and again in Q6; I read the file: line 39 is "Revocation relationship: none. Existing implementation and applicability acts retain their own exact scopes.", 40–41 carry "This act grants no implementation extension, source/provider/content permission, write consent, deployment or release." The Scope paragraph does end at line 32, so "seven lines below" is exact. (b) Gate 3's act table gains a per-slice **Named clause** column and its entries are correct: my own Python `re` sweep of both specification files, whitespace-normalised, gives slice 4's "The original finding, repair, dispositions and input/output identities SHALL remain traceable" **1 in the overlay (line 180), 0 in the predecessor** — and no near-variant exists, the only base hits for `traceab` being REQ heading 1659 and scenario lines 1687–1688. Slice 6's glossary clause is likewise **1 (overlay 78) / 0**. REQ-004 base **186**, REQ-006 base **302**, REQ-019 base **1015** all present, so slices 2, 3 and 5 do rest on predecessor text. (c) Both readings are stated, each labelled `[Inferred]`, and reading (ii)'s consequence for deferred slice 6 is carried. (d) The second-arm handoff now reads "**most** gated", with the first draft's "least gated" retained inside a dated supersession note at packet lines 35 and 1340. (e) Q6's recommendation now follows the evidence, and the superseded recommendation is quoted and dated in place rather than deleted |
| F2 | non-blocking | **REPAIRED** | Demo re-run twice into separate scratch directories: 7 files, **87,940** bytes both times, addend-for-addend as the packet lists them; exit 0; deterministic. The superseded 41,940 is retained and dated at packet line 218 and in the record. The record's `runs[0].output_bytes_total` is 87940 |
| F3 | non-blocking | **PARTIAL** | Packet fully repaired and verified: `index.ts` lines 1–14 re-export exactly **eleven** runtime values (CANONICAL_JSON_ENCODING, CanonicalJsonError, digestCanonicalJson, encodeCanonicalJson, parseBoundedJson, BoundedJsonError, promptForStage, runGenerationPipeline, stageSchema, validateStage, reviewVerdict) beside **thirteen** type-only exports, and `src/` holds **six** non-test sources. The superseded enumeration is retained and dated. **Residue:** the evidence record's `measurements.M4_edit_repair_and_the_absent_comparison.other_exports` array (record line 399) still carries the wrong four values, unmarked, while the `export_sweep_method` string in the same object says eleven — G4 |
| F4 | non-blocking | **PARTIAL** | Packet fully repaired and verified: `git diff --name-status f4589e2 a9f671e` over the four paths gives **20 A and 2 M**, the two M rows being the kit README and `package.json`; the three files the packet names are blob-identical at `f4589e2` and appear in no row; `1932f74..a9f671e` over the four implementation paths returns **0** rows and over `openspec`/`.syzygy` returns **3**, all under `decisions/` and none a specification file. **Residue:** the record's `commit.dossier_audit_commit_discrepancy.finding` (record line 21) still reads "shows 22 files added with 0 deletions, including every file L3 and S9 cite" — the exact sentence F4 found false — unmarked — G4 |
| F5 | non-blocking | **PARTIAL** | Six of the seven instances repaired and each verified at source: core README sentence at **52** (53 is blank, command at 55); AUTHORING diagram sentence **45–47** (the word "placement" is on 47, so S9-F3's 45–49 was indeed closer than the first correction); deep-dive clause **62–63**; glossary clause **26–27**; Plan-prompt sentence **101–102**; ARTIFACTS-AND-TOOLS **40–41** exact and **42–43**. **Not repaired:** the instance F5 named explicitly — the product-promise sentence is still cited at "`docs/polaris-generation/README.md` line 70" (packet line 133) when it begins on line **69** — plus the record's five narrow `promises[].at` values. G5, G4 |
| F6 | non-blocking | **REPAIRED** | Case-insensitive Python `re`: `glossar` occurs **2** times in `prompts.ts`, at lines 13 and 20 (line 20 inside the fidelity prompt), **0** in `provider-draft.ts`, **0** in `pipeline.ts`; the six-file denominator is stated. Corrected in packet and record |
| F7 | non-blocking | **REPAIRED** | (a) The scope sentence spans **219–220**, line 221 the shape-parallel list; the packet now cites 219–220 and marks the superseded 221. (b) The reviewed-N/A-judgment arm is added to the slice-4 row, with the packet's own `[Inferred]` view that it is probably unreachable because a change account is independently testable |
| F8 | non-blocking | **REPAIRED** (classification) | Q5's cell now states in terms that it is a cost trade-off the owner may delegate rather than a gate, labels that `[Inferred]`, keeps the `build:poc` limb as a stated decision, and keeps the question in the batch; the "genuine gates" sentence now names Q1, Q3 and Q6 with the first draft's wording retained and dated. The disposition cell's own self-sweep is, however, now false — G6 |
| F9 | non-blocking | **REPAIRED** | The Q3 cell carries the added sentence naming the deferred conformance with "unresolved material omissions SHALL prevent readiness", its lawfulness while Phase A is unfinished (all 24 boxes unchecked, re-counted), and the bead's obligation to record it; labels are split `[Observed]` for the quotation and `[Inferred]` for the consequence. The quotation is verbatim at overlay 180 and base 302 |
| F10 | non-blocking | **REPAIRED** | Gate 3 gains "What landing slices 2, 3 and 4 retires", naming the synthetic-verification record by path and the re-run obligation; Gate 6 item 8's heading is narrowed to act-bound bytes with the superseded wider heading retained. Verified: that record carries 17 source rows, all 17 match current bytes, and neither value is reproduced in the packet |
| F11 | non-blocking | **PARTIAL** | (a) **REPAIRED**: five sibling registers, each carrying exactly one row, P-68/P-69/P-70/P-71/P-72; the packet says five. (b) **PARTIAL**: the five named sibling heads are the current heads of the five sibling worktrees (`f2f37dd`, `6574600`, `63b8e33`, `ba9ca61`, `4090f98`), so no branch advanced. Recomputing the packet's own method over each sibling's funnel packet, I reproduce **M1 3/1, M2 17/11, M3 15/13, M4 26/22, M5 11/9** exactly, and the directory-span breakdown exactly (M2 six, M4 four, M3 two, M5 two, M1 two), and **intersection 0 under both predicates for all six**. The lane-B row does not re-derive under either predicate — G3. The record's M9 block still publishes one predicate and no sibling commit — G4 |
| F12 | editorial | **PARTIAL** | (b) banner reworded with the superseded sentence retained and dated — verified. (c) run 2 re-executed by the repairing session and recorded as 42 = 5 `TS2307` + 32 `TS7006` + 4 `TS2339` + 1 `TS7053`. (d) the split-on-newline convention is stated once at packet lines 187–194 and the one `wc -l` denominator is marked where it appears; I confirm `prompts.ts` 30, `tasks.md` 52, `provider-draft.ts` 153 split / 152 `wc -l`. (a) **not repaired**: the list now says six against a record array that now carries **seven** — G1 |
| F13 | non-blocking | **REPAIRED** | Q1 now states that of the three bound artifacts only `SCHEMA-CONTRACT.md` declares a closed vocabulary (verified: line 33, then the table at 35–39) while REQ-004 and REQ-019 describe the dispositions in prose, labels the forcing step `[Inferred]`, and stands on the measured divergence. The Recommended-handoff sentence is restated with its superseded wording quoted and dated |

Tally: **9 REPAIRED, 4 PARTIAL, 0 NOT REPAIRED.** Every partial is a
residue in the companion evidence record or one named instance of F5, not
a failure of the packet's argument.

## New findings

### G1 — non-blocking

Packet lines 485–489; record line 879.

**Defect.** "**Six figures that differ from the dossier**, collected — the
same six the companion record's `figures_that_differ_from_the_dossier`
array carries, in the same order". The array carries **seven** entries:
the F5 repair appended a corrected fifth entry (record entry 6) beside the
retained stale one, which is the right way to supersede, but the packet's
reconciliation sentence was not re-derived afterwards. So the repair for
F12(a) re-creates F12(a): a list "whose whole purpose is to be complete"
asserts identity with a machine array it no longer matches, and "in the
same order" is false from the fifth entry on. [Observed, both counted this
session.]

**Repair.** Say seven and name the appended corrected entry, or state that
the packet's six collapse the record's two S9-F3 entries into one and say
so explicitly.

### G2 — non-blocking

Record lines 644–645.

**Defect.** `measurements.M9_file_set_intersection.shared_governance_file`
still carries `"touched_by_M6": false` and the disclosure "This packet
writes exactly two files and no register row, so its six owner questions
are unregistered as of this commit. Whoever lands this packet should file
them." Both are false at `e318cbd`: P-73 is registered and
`git diff --name-only a9f671e e318cbd` shows this branch changing
`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`. Neither field is
marked stale, and `touched_by` still lists five. The packet's own prose was
corrected at packet lines 1092–1095; the record was not. A reader acting on
the record alone would file P-73 a second time. [Observed.]

**Repair.** Set `touched_by_M6` true, add M6 to `touched_by`, and mark the
disclosure sentence in place with its date rather than deleting it.

### G3 — non-blocking

Packet lines 1057–1075 (the collision table's lane-B row and the paragraph
above it); record lines 563 and 610–620.

**Defect.** The lane-B row reports 3 resolving spans under `os.path.exists`
and 1 under `os.path.isfile`, and the paragraph above explains every such
gap as directory spans: "M2 names six, M4 four, M3 two, M5 two, M1 and lane
B two each." For lane B that is not what the gap is. The record itself
names lane B's three paths —
`scripts/build_pwb_scoped_attributes_amendment.py`,
`scripts/check_governance.py` and
`scripts/estimate_pwb_scoped_attributes_saving.py` — and in this worktree
only the middle one exists at all; the other two are lane-B branch files
and are neither files nor directories here. Under the record's own stated
method ("resolve as a real file **in this worktree**") lane B is **1**
under both predicates, not 3 and 1, and the gap is branch content rather
than predicate. No lane-B document reproduces 3/1 either: over its four
amendment-package files I get 26/24, 0/0, 0/0 and 2/0, and over
`PROJECT-STATUS.md` 4/2. The only file in that worktree that yields 3/1 is
the M1 funnel packet, which is also the M1 row's source. So the published
figure cannot be re-derived under either predicate the packet publishes,
and the explanation offered for the divergence is false for that row —
which is the half of F11(b) the repair reported as resolved. The
load-bearing claim survives: I get **intersection 0** for lane B under both
predicates, as for all five others. [Observed, recomputed this session
against all six sibling worktrees at the heads the table names.]

**Repair.** Recompute the lane-B row against the lane-B packet in the lane-B
worktree and say which worktree each count was taken in, or drop the two
count columns for that row and keep the intersection, which is the figure
that carries weight.

### G4 — non-blocking

Record lines 21, 399, 563, 592–612, 644–645, 915 and 925–930, and
`measurements.M5_kit_promises_vs_schema.promises[1..5].at`.

**Defect.** The review-1 repairs were applied thoroughly to the packet and
only partly to the companion evidence record, and the record's first-draft
fields carry the corrected sentences' predecessors **unmarked**, so the
JSON and the Markdown now disagree at seven places. The pattern is the
repository's own lesson — mark staleness at the stale sentence — inverted:
the corrections exist, but in a sibling string or in the packet, while the
false field stands clean.

- Line 21, the F4 sentence ("22 files added with 0 deletions, including
  every file L3 and S9 cite"), unmarked; the corrected version lives only
  in `review1.re_derived_before_applying.baseline_diff`.
- Line 399, `other_exports`, the F3 four, unmarked; the corrected count
  lives in the adjacent `export_sweep_method` string, which now contradicts
  the array beside it.
- The five `promises[].at` values still narrow (AUTHORING "line 62", "line
  26", "line 102"; ARTIFACTS-AND-TOOLS "line 40", "line 43") — the F5
  defect — while `promises[0].at` was widened to 45–47 and the sibling
  `line_corrections_to_the_finding` block names 62–63 and 40–41.
- Line 563, M9's `method`, still one predicate; lines 592–612, the
  per-sibling counts, still unlabelled as to predicate and carrying no
  sibling commit, both being F11(b)'s repair.
- Line 915, `cg_1b_note`, still says the first review's path "is named
  without a code span … because it does not exist yet"; the packet now
  backticks it and it resolves, which the packet says in terms.
- Lines 925–930, `packet_measured`, still names 86188 bytes, the
  pre-repair sha256 and `total_lines` 1122, under a note reading "measured
  this session **after the last edit** to the packet; verification rule 10
  binds a review to exactly these bytes". The current packet is 116325
  bytes and 1348 split-lines. The correct current values do exist, under
  `review1.packet_after_repairs` (116325 and a sha256 I confirm matches
  the file), so the record contains both a true and a false statement of
  the same fact and marks neither. [Observed, all compared this session.]

**Repair.** Mark each stale field in place with its date, as the packet
does and as `promises[0].at` and `export_sweep_method` already do, rather
than leaving the correction to a sibling key.

### G5 — non-blocking

Packet lines 133 and 557.

**Defect.** Two wrapped-citation instances of the F5 class remain, one of
them named by F5 itself.

- Packet line 133: "`docs/polaris-generation/README.md` line 70 states the
  product promise — 'Missing evidence is Unknown; unsupported assets are
  unresolved with a reason'". The sentence begins on line **69** ("Stop
  before a provider call without its required admission. Missing evidence
  is") and ends on 70. F5 named this instance explicitly and noted the
  dossier's S9-F2 is more precise here; every other instance it listed was
  widened, and this one was not.
- Packet line 557: RFC2-24 is cited at "line 92: 'Every Unknown claim
  instance carries exactly one primary reason from this list'". Line 92
  ends at "carries"; the quotation ends on line **93**.

Both matter for the reason the packet itself gives two paragraphs later:
these files are hard-wrapped and a citation naming only the distinctive
half understates its span. [Observed, both read at source.]

**Repair.** Cite 69–70 and 92–93.

### G6 — non-blocking

Packet line 1238 (the F8 disposition cell).

**Defect.** The cell states, in the present tense about the file it sits
in: "the one occurrence of 'six questions' is the section heading (sweep
for 'six questions' and 'six gates' over this file: 1 hit and 0)". Over the
current bytes the sweep returns **3** and **1**, and all three of the extra
hits are inside that same cell — two "six questions" and one "six gates"
written by the sentence reporting the sweep. The figure was true of the
first draft (I confirm 1 and 0 at `91b1343`) and was not re-derived over
the bytes that carry it. This is rule 2's shape: a count over a population
the current pass is still editing has to be re-derived, never carried
forward. [Observed, swept over both versions this session.]

**Repair.** Restate as a sweep over the first draft, naming that commit, or
re-derive it over the current file and give the new figures.

### G7 — non-blocking

Packet lines 242–245, and the same claim in Q5 at packet line 34.

**Defect.** "`build:poc` (`package.json` line 15) is `tsc -b --force` over
four projects, and `packages/polaris-generation-core` is **not one of
them**. The package is built only because `apps/three-surface-poc/tsconfig.json`
declares a project reference to it." The first sentence is exact. The
second is not: `package.json` line **14** (`build`) and line **21**
(`typecheck`) both name `packages/polaris-generation-core` explicitly, so
the package is built directly by two of the repository's own scripts, and
what depends solely on the tsconfig reference is the `build:poc` chain the
demo runs, not the package. The same over-wide wording reaches Q5's cell
and Gate 4's "removes the dependence on a single `references` entry".
Review 1 noticed this and recorded it as a parenthetical rather than a
finding; it was therefore never repaired. The defect Q5's third limb
addresses is real either way — the demo chain is the one that breaks —
but as written the packet overstates it. [Observed, `package.json` read at
source this session.]

**Repair.** Qualify to the `build:poc` chain, and note that `build` and
`typecheck` already name the package.

### G8 — editorial

Packet lines 102–105 and line 35.

**Defect.** Both sites introduce the quotation as "lines 39–41 read,
verbatim: 'Existing implementation and applicability acts retain their own
exact scopes. …'". Line 39 opens "Revocation relationship: none." and that
sentence is not quoted, so the span named is wider than the text given —
the mirror of the F5 class, and in the sentence on which the whole F1
repair rests. The quoted text itself is verbatim, and the packet elsewhere
calls the paragraph "the same act's revocation paragraph", so nothing
substantive turns on it.

**Repair.** Cite 39–41 and quote from "Revocation relationship: none.", or
cite the sentence span.

### G9 — editorial

Packet lines 543–548.

**Defect.** The SEC-2 quotation, introduced as "quoted at the load-bearing
sentence", renders "**including prompts**" in bold. The source does not
bold that phrase; it bolds only "**Model providers are such services.**",
which the packet also carries. The words are verbatim — I compared the
whole quotation against lines 25–37 with emphasis stripped and it matches —
but a quotation that adds emphasis the clause does not carry is an
alteration a reader cannot detect.

**Repair.** Drop the added emphasis, or mark it as the packet's own.

### G10 — editorial

Packet line 1071.

**Defect.** The intersection table's M1 row names the head read as
"`91b1343` (this worktree)", and the paragraph above it says "Every sibling
head below is the head this session read". This worktree is at `e318cbd`;
`91b1343` is its parent. The M1 packet's bytes are unchanged between the
two (`git diff --name-only 91b1343 e318cbd` over that path is empty, and
the M1 figures reproduce), so nothing measured moves — but the row names a
commit that is no longer the head it claims to be, which is the staleness
F11(b) asked the column to prevent. [Observed.]

**Repair.** Name `e318cbd`, or say the M1 packet's bytes are identical at
both.

### G11 — editorial

Packet lines 1140–1141 (Gate 6 item 7).

**Defect.** "In the worktree, `git status` with `--short` is clean of
everything but this packet's two files." At `e318cbd` the branch carries
four files, all committed, and `git status --short` is empty. The sentence
was true when written and is now stale, and unlike every other superseded
sentence in the packet it carries no date or marker. [Observed; the short
git status was run before and after this review, empty both times.]

**Repair.** Mark it in place, or restate it as clean.

### G12 — editorial

Packet lines 105–108 (Gate 0).

**Defect.** "Every clause this packet's slices 2, 3 and 5 rest on is
predecessor text carried through the amendment unchanged, **so those slices
are covered on either reading of that sentence**." The first half is
Observed and I verified it; the second half is a reading of what the
implementation act authorizes, which is precisely the question Q6 declines
to settle and labels `[Inferred]` in both arms. At Gate 0 it stands
unlabelled and flat. The paragraph's trailing bracket is an edit-history
note, not an epistemic label.

**Repair.** Label the consequence `[Inferred]`, or point to Q6 where it is
labelled.

## The six questions, after the repairs

| # | Scope truthful? | Genuine gate? | Recommendation follows? | Lawful arms all named? |
|---|---|---|---|---|
| Q1 | **Yes.** Field census, the three bound artifacts, the vocabulary declaration at `SCHEMA-CONTRACT.md` line 33 and the spelling divergence all verify at source. | **Yes.** Conforming code to a normative data contract is squarely VIS-4's always-human-gated class, quoted correctly at lines 131–133. | **Yes.** F13 is applied: the forcing step is labelled `[Inferred]`, the divergence carries the argument, and the counter-argument no longer overstates. | **Yes** — implementation arm, CC-REV-2 amendment arm, stated default. |
| Q2 | **Yes.** `references()` is existence-only at lines 90–98; the REQ-002 and REQ-003 quotations are verbatim at overlay 9 and base 98. | **Partly**, and the packet says so — a large scoping decision rather than a gate. | **Yes.** Defer-with-a-strong-counter, honestly put. | **Yes** — defer, or take it now as slice 2b. |
| Q3 | **Yes.** `minItems` 0 at line 31, `reviewVerdict` at 148–152, `same()` at 86–89 and 127–128, REQ-006 at overlay 180 — all verified. | **Yes.** It moves an owner-visible readiness state. | **Yes.** F9 applied: the second arm's deferred conformance is named, its lawfulness stated, and the bead's obligation recorded. | **Yes** — polarity change, rows-only with its cost disclosed, default stated. |
| Q4 | **Yes.** 19 of 19 reproduces exactly, and the fairness qualification against the packet's own interest stands. | **No, and the packet does not claim otherwise.** Both arms are cheap and the file is bound by nothing. | **Yes.** | **Yes** — regenerate, or one routing sentence, with the default named. |
| Q5 | **Yes**, except G7's over-wide "built only because" sentence; every measurement reproduces, including the counterexample in both directions. | **No — and the packet now says so.** F8 applied: the cell calls it a delegable cost trade-off, labels that `[Inferred]`, and keeps the `build:poc` limb as a stated decision. | **Yes**, on the merits. | **Yes** — both arms and the third limb named. |
| Q6 | **Yes.** The gap that made this "partly" in review 1 is closed: the limiting sentence is quoted at Gate 0 and in Q6 and verified at source, and the per-slice predecessor/overlay-only status is recorded in Gate 3 and is correct under my own sweep of both specification files. | **Yes.** Still the one question that could stop every slice. | **Yes.** The recommendation now follows the evidence, the superseded recommendation is quoted and dated rather than deleted, and the second-arm handoff is corrected to "most gated" with its predecessor retained. | **Yes.** Both previously missing arms are named: the overlay-only-clause arm (F1) and RFC2-26's own reviewed-N/A-judgment arm (F7b), the latter with the packet's `[Inferred]` view of its reachability. |

Trade-offs smoothed: none found. The packet keeps every counter-argument
it had, and the repairs added three more disclosures that cut against its
own recommendations (Q3's deferred conformance, Q5's reclassification, Q6's
reversed handoff).

## The register

- **Faithfulness.** The P-73 row renders all six questions with the
  post-repair recommendations, second arms and defaults, including Q3's
  added conformance disclosure, Q5's delegable-cost reclassification with
  its `[Inferred]` label, Q6's changed recommendation and Q1's F13
  restatement. I compared cell by cell against the packet's table; nothing
  is dropped, softened or promoted. [Observed.]
- **Verdict word and counts.** The blockquote and the row both say
  "verdict copied exactly: REVISE — one blocking, eleven non-blocking, one
  editorial". The raw's closing lines are "Findings by severity: 1
  blocking, 11 non-blocking, 1 editorial." and "Verdict: REVISE". The
  verdict word is copied exactly; the counts are spelled out rather than
  in digits, which the "copied exactly" phrase attaches to the verdict
  word and not to them. Matching.
- **Recount reproducible.** Yes, under the stated predicate. See above:
  22 open / 5 act / 27 total on this branch, 21/5/26 at `a9f671e`.
- **No digest, no observed-repository path.** The row and the blockquote
  quote no digest, no act argument and no manifest row, and backtick no
  observed-repository path. `check_governance.py` ends `0 FAIL` with no
  finding against this file's new lines.

## Overall

The review-1 repairs are, in the packet, thorough and honest. The blocking
finding is fully discharged and independently re-derived: I swept both
specification files myself and the per-slice predecessor/overlay-only
column is correct in every row, the act's sentence is quoted where it
belongs, both readings are stated and labelled, and the recommendation that
F1 reversed is reversed with its predecessor quoted and dated rather than
deleted. Nine of the thirteen findings are fully repaired, the packet's own
convention self-checks reproduce to the digit at the new bytes, every
contract and doctrine quotation is verbatim at its defined clause, and the
P-73 row is a faithful rendering whose recount reproduces under its own
predicate.

What it does not do is carry the repairs into the companion evidence
record. Four of the thirteen dispositions are partial for that reason, and
four of the seven non-blocking findings below are the same shape: a
corrected sentence in the Markdown standing beside its uncorrected
predecessor in the JSON, unmarked. One of those — the register disclosure
telling a reader the questions are unfiled — could cause a duplicate P-73.
One further figure, the lane-B intersection row, cannot be re-derived under
either predicate the packet publishes, though the claim resting on it
(intersection zero) holds under both. None of this touches an owner
recommendation, so none of it blocks.

Findings by severity: 0 blocking, 7 non-blocking, 5 editorial.

Verdict: CONFIRM WITH EXCEPTIONS
