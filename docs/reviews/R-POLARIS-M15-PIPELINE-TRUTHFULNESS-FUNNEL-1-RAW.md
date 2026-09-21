# Independent fresh-context review — Polaris M15 pipeline-truthfulness funnel packet

Verdict: **CONFIRM WITH EXCEPTIONS**

Reviewer: independent fresh-context session (Claude), 2026-09-17.
Subject bytes: commit `bdc2fda` on branch `agent/syzygy-dov.15`, worktree
`/tmp/claude-1000/-home-tze-GitHub-syzygy/6b8e9d74-3b46-4418-b725-5b74d21d660a/scratchpad/m15wt`.
Artifacts reviewed:
- `docs/design/POLARIS-M15-PIPELINE-TRUTHFULNESS-FUNNEL.md`
- `docs/evidence/polaris-m15-pipeline-truthfulness-funnel-2026-09-17.json`
- `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` (P-82 row)

All figures below were re-derived independently this session (source read at the
committed bytes; capture magnitudes recomputed by a JSON walk over the retained
`api-poc.json`; packet self-referential figures recomputed over the committed
bytes). Every load-bearing figure the packet leans on reproduced exactly. The
three exceptions are citation-precision (rule 8) imprecisions where the quoted
text is verbatim-correct and correctly attributed but the line pointer lands on
an adjacent or header line; none blocks the owner from acting and none changes a
verdict, magnitude, or the drafting-only posture.

## Independently recomputed figures

- Packet bytes: **33748** (matches evidence `packet_measured.bytes` and
  committed file).
- Packet sha256: **0733d7271a707ebaf04d969275e0c5811c7fb5f479b2017d4f6bb1b52f2e18d4**
  (matches evidence `packet_measured.sha256` and a fresh hash of the committed
  bytes).
- total_lines: **390** by `wc -l` / `sed` convention (the packet's stated
  "line N" convention). A naive `split('\n')` yields 391 segments and 366
  non-fence lines; the extra one is the trailing-newline empty final segment.
  Excluding it gives non_fence_lines **365** and total **390**, matching Gate 6
  and the evidence JSON.
- non_fence_lines: **365** (matches).
- over_78: **0** (predicate: non-fence line whose first non-space char is not
  `|`, `>`, `#`, length > 78; denominator every line). Matches Gate 6 and JSON.
- odd_backtick non-fence lines: **0** (no code span broken across a line
  break). Matches Gate 6 and JSON.
- `check_governance.py` tail: **`32 OK, 20 WARN, 0 FAIL (52 checks) — counts
  derived, not asserted`**. 0 FAIL. (The 20 WARN include the always-downgraded
  CG-20/CG-21/CG-27 advisories; none is a new failure.)

## Per-criterion findings

### 1. Planning-only integrity — PASS
Nothing authorizes implementation. Each of Q1–Q4 carries a recommended answer,
lettered lawful arms (a/b/c), and an explicit "Default if unanswered: nothing
happens" clause. Q1's recommended arm is *drafting* a CC-REV-2 semantic delta
only, explicitly "binds nothing (VIS-4)." The spec-amendment escalation trigger
is correctly flagged in Gate 3's per-slice table (each slice mapped to "a
further amendment to the signed PWB specification"), and the "Decided in this
packet" section states once that all four slices are downstream of the
PWB-REQ-002 contract change with no slice buildable under the acts in force.

### 2. Epistemic labels — PASS
Substantive claims carry `[Observed]`/`[Inferred]`/`[Unknown]`. The structural
defect and its magnitude on the capture are `[Observed]`; the live bite at
Butlers `13d269b` is `[Observed]` on that named revision; the tenth-category and
second-project harms are `[Inferred]` counterfactuals, stated as not present in
Butlers today. Trade-offs are preserved, not smoothed: each question carries a
"Counter-argument, and it is real" clause (Q1's intricacy cost, Q2's oracle
reconciliation burden, Q3's under-count-vs-flag tension, Q4's mis-stamping
risk), and the two Butlers revisions (clean at capture, whole-source-Unknown at
`13d269b`) are held distinct rather than collapsed.

### 3. Sourcing (rule 8) — PASS with three non-blocking/editorial exceptions
Verified against the committed bytes:
- `extractSource` at `project-shape-extraction.ts` lines 628–662 — confirmed.
- Discard `if (result.kind === 'failed') return { kind: 'unknown', path,
  classes, failure: result.failure };` at **line 646** — confirmed exact.
- `const result = extractClass(cls, path, text);` at **line 645** — confirmed.
- `all.push(...result.items);` at **line 647** (the accumulator filled on the
  success path) — confirmed; the drafter's dossier note that the discard is at
  :646 (not the dossier's :645-646) is correct.
- Module comment "A source never yields a partial item set" at lines 14–17 —
  confirmed verbatim.
- `EXTRACTION_FAILURES` at lines 33–41, **7** reasons — confirmed.
- `CATALOG_HEADINGS` at lines 56–66, **9** literals — confirmed.
- `extractCatalogEntries` at lines 438–460, iterates only
  `for (const headingText of CATALOG_HEADINGS)` with no document-heading scan —
  confirmed.
- `project-shape-manifest.ts`: `BASELINE_SPEC`/`ROSTER_BUTLER` at lines 354–355;
  Rule 2 `pillars` map begins at line 419 and branches on `rootIndex.state`
  (2 occurrences in its region); Rules 3–4 at lines 491–506 loop
  `for (const entry of input.tree)` with **0** occurrences of `rootIndex` in the
  block — all confirmed.

Exceptions (F1–F3 below): the pinning-test range, the line-250 class-assignment
citation, and the falsifier line pointer.

### 4. Rule 2 / 9 (no unbounded "zero/all/every/only" without a swept, enumerated
denominator) — PASS
Every count re-derived by an independent second method:
- `projectShape.items` = **415** across **9** classes — confirmed.
- Exactly **two** multi-class item-bearing sources, enumerated: `v1.md`
  (catalog-entry 65, project-account-section 2, success-criterion 8 = **75**)
  and `vision.md` (project-account-section 3, principle 7, success-criterion 5 =
  **15**) — confirmed by grouping items by first-anchor path and class.
- `CATALOG_HEADINGS` = **9**; `EXTRACTION_FAILURES` = **7** — confirmed two ways.
- `baseline-spec` class = **192** items (the packet's "192 baseline-spec
  sources"; item and source counts coincide here, one item per baseline-spec
  source) — confirmed.
- `rootIndex` occurrences in Rules 3–4 block = **0**; in Rule 2 region ≥ 1 —
  confirmed. Remainders enumerated in every case.

### 5. Rule 3 / 4 (computed digests; read outputs and denominators) — PASS
The packet's sha256 is a full file-content hash of a Syzygy file, recomputed and
matching (not transcribed). check_governance output (not exit code) read:
0 FAIL over 52 checks with the denominator printed. The evidence JSON's
`packet_measured` bytes and sha256 equal the committed packet.

### 6. Governance conventions — PASS
- CG-1b: the only backticked path in the packet is `.syzygy/governance/
  doctrine/vision.md` (a Syzygy path). No Butlers repository path is backticked
  anywhere; Butlers sources are named in prose ("the Butlers v1 index", "the
  Butlers vision file"). PASS.
- CG-7e / CG-15: no truncated signed governance-act digest, performed-act
  argument, or manifest row is quoted. The two backticked hex strings are the
  full 40-char Butlers git revision `2e3bac97790b4bd8906dcac63eadb5642a0bb1ac`
  and the short Butlers revision `13d269b` — git revisions of the observed
  repository, not signed governance digests — and the packet's own full-content
  sha256, which the rules explicitly allow. check_governance enforces CG-1b/
  CG-15 and returns 0 FAIL. PASS.
- CG-27: 0 FAIL; tables stand. No code span is broken across a line break
  (odd-backtick non-fence lines = 0). PASS.

### 7. Self-referential figures (re-derived) — PASS
over_78 = 0, odd_backtick = 0, non_fence_lines = 365, total_lines = 390, all
recomputed over the committed bytes and equal to Gate 6 and the evidence JSON.

### 8. Evidence record — PASS
Valid JSON. `packet_measured.bytes` (33748) and `.sha256` equal the committed
packet. `self_referential_figures` agree with the packet. No `reviewN`
verdict block is present (correct for a first draft). No CG-15/CG-7e violation
in the JSON: it carries the full Butlers revision and the packet's own content
sha256, neither a signed governance digest.

### 9. Register — PASS
`^| P-` rows total = **27** (26 predecessors + P-82), matching the evidence
claim. P-82 is a faithful one-line rendering: it names all four questions with
their recommended arms and lettered alternatives, states "No arm authorizes
implementation; drafting binds nothing (VIS-4)," and records the default "no
delta is drafted … none of the four slices is designed or built." It quotes no
digest and backticks no Butlers path (its backticks are identifiers —
`PWB-REQ-002`, `partially-extracted`, `unenumerated-heading`, `rootIndexRequired`
— and Syzygy paths).

### 10. Doctrine fit — PASS
VIS-2 (no-evidence → Unknown, never silence/zero) and VIS-1 (an unqualified
partial truth is the worst failure) are applied correctly to all three findings.
"One grammar defect wipes three independent facts" is accurate: `v1.md` declares
exactly three extraction classes (manifest line 250) and `extractSource` returns
whole-source `unknown` on the first failing class, discarding the two that
succeeded — verified in code and by the capture's 65+2+8 split. "Tenth category
invisible not Unknown" is accurate: `extractCatalogEntries` iterates only the
nine closed headings and never scans the document's own level-3 headings, so a
tenth heading yields neither an item nor an Unknown. L1-F2's "modeled facts
beneath an unread root" is accurate: Rules 3–4 mint sources over the whole tree
with no `rootIndex` dependence.

## Findings

**F1 — non-blocking (rule 8, minor).** Packet line 65 (and lines 82–83, 147–151,
339) cites the pinning test at "lines 778–786." In the committed bytes the test
`it('a failing class withholds the items of the classes that succeeded', …)`
begins at **line 779** and its block runs 779–786; line 778 is the blank
separator before it. The test's name, its two `extractClass(...).kind` ===
`'items'` assertions, and its `expect(r.kind).toBe('unknown')` are all present
and exactly as the packet characterizes them. Minimal repair: cite "lines
779–786" (or note the range includes the leading blank). Off-by-one on the range
start only; substance correct.

**F2 — non-blocking (rule 8).** Packet line 163 (Measurements §1) states "the
manifest's class assignment (`project-shape-manifest.ts` line 250) independently
shows both the v1 index and the vision file declaring exactly three extraction
classes each," and the evidence JSON `s7_f1…meaning` says the same. At the
committed bytes, **line 250** carries only `v1.md`'s three classes
(`['project-account-section', 'success-criterion', 'catalog-entry']`); the
`vision.md` three-class declaration
(`['project-account-section', 'principle', 'success-criterion']`) is on the
adjacent **line 249**. Both facts are true, but the single line-250 pointer does
not cover the vision-file half of the claim. Minimal repair: cite "lines
249–250" (or 249 for vision.md, 250 for v1.md).

**F3 — editorial (rule 8, defensible as written).** Packet Q1 cites
"PWB-REQ-002's own **Falsifier** (…spec.md, the requirement at line 115) lists
'a malformed source emits a partial population.'" Line 115 is the
`### Requirement: PWB-REQ-002 …` header; the Falsifier bullet carrying the quoted
phrase is at spec **lines 137–138**. The quote is verbatim and correctly
attributed to PWB-REQ-002, and "the requirement at line 115" reads as citing the
requirement's location rather than the phrase's, so this is defensible. A strict
rule-8 reader would prefer the exact falsifier line (137–138). Minimal repair
(optional): add the falsifier bullet line.

## Note on the packet's contract phrasing (not a finding)
The packet is careful to attribute "A source never yields a partial item set" to
the code comment (extraction.ts:14–17) and "a malformed source emits a partial
population" to the spec falsifier, and Gate 4's Slice 1 design correctly names
the actual amendment target as rescoping that spec falsifier from "source" to
"class." The phrase "a source never yields a partial item set" does not appear
in the spec (confirmed by sweep); the packet does not claim it does. The
"PWB-REQ-002's tested … contract" shorthand in the Gate 3 table conflates the
code paraphrase with the spec byte, but the two are equivalent in meaning and
the amendment is aimed at the real spec byte, so this is not a misstatement.

## Summary
The packet's structural claims and every load-bearing magnitude are correct and
independently reproduced; the drafting-only, spec-amendment-gated posture is
sound and correctly flagged; governance conventions pass with 0 FAIL; the
evidence record and register row are faithful. The three exceptions are
line-pointer precision matters (F1 off-by-one range start; F2 a single line
cited for a two-line fact; F3 requirement-header vs falsifier-bullet line), all
non-blocking or editorial. Verdict: **CONFIRM WITH EXCEPTIONS**.
