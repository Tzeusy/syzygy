CONFIRM WITH EXCEPTIONS

Independent fresh-context review of the M16 renderer/visual-system funnel packet at
commit 429924a on branch agent/syzygy-dov.16. Subject bytes:
- docs/design/POLARIS-M16-RENDERER-VISUAL-SYSTEM-FUNNEL.md
- docs/evidence/polaris-m16-renderer-visual-system-funnel-2026-09-17.json
- .syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md (row P-83)
All source re-derived read-only against a9f671e (the branch parent). No repo file
edited; no PR touched; no Butlers checkout read; no daemon started.

VERDICT RATIONALE. Every load-bearing figure reproduces exactly (polaris.ts line
count; the four mutation-subject recorded-vs-current digests and the rule-10 gap;
the five HTML-string helper signatures and their line anchors; 0 <svg / 0 <canvas
over three captures with byte denominators; eight stray hex in design-tokens.ts and
nineteen app-wide including the 8-digit RGBA; forced-dark theme with no
prefers-color-scheme and no recorded decision; all Gate-6 self-referential figures;
the register at exactly 27 anchored P- rows with P-83 once). The packet is
planning-only, each question carries a recommended arm + all lawful arms + a real
counter-argument + a default of "nothing happens", the first-draft rule-10 posture
is present in banner, Gate 6, funnel summary and register row, and no CG violation
was found (no truncated signed digest, no backticked Butlers path, no CG-27 row
leaning on a sibling's as-of token). The exceptions are three non-blocking accuracy
defects in second-method narration and anchoring, plus two editorial nits. None
touches a load-bearing figure or the build/design classification.

================================================================================
FINDINGS
================================================================================

F1 — non-blocking. Measurement 2's stated second method misdescribes its own grep
output.
  Packet claim (Measurement 2, ~line 178-182; Q2, line 70): "a grep for
  `function .*: string {` across the band returns these five plus `causeRoutes`
  (448), which returns `readonly string[]` and is not an HTML-string helper — five
  HTML-string helpers".
  Derived: `causeRoutes` (a9f671e:polaris.ts:448) does NOT match `function .*: string {`
  — its signature is `function causeRoutes(reason: string, paths: ReadonlySet<string> |
  undefined): readonly string[] | undefined {`, which contains no `: string {` substring.
  Running the exact pattern band-scoped (416-490) returns EXACTLY the five helpers
  (excludedCauseRoute 416, unavailableCauseRoute 440, routeOf 462, reasonRouteHtml 472,
  unknownRoutes 480) with NO causeRoutes false positive. The next function that does
  match, `readingFigure` (`... anchorId?: string): string {`), is at line 491 — one
  line outside the band. So the packet invents a false-positive it then excludes; the
  grep is cleaner than described.
  Anchor: a9f671e:apps/three-surface-poc/src/polaris.ts:448 (causeRoutes), :491
  (readingFigure).
  Delta: the load-bearing conclusion ("five HTML-string helpers") reproduces by BOTH
  methods; only the narration of the second method is wrong. Non-blocking.

F2 — non-blocking. The byte-offset-stitching sub-claim (S3-M2) is true but is not
anchored to the file:line where it actually lives.
  Packet claim (Q5, line 73; Gate 4 slice 5, line 295): "The fence path stitches
  diagram bodies from byte offsets rather than the literal fence content", with Q5's
  measured evidence anchored to polaris-markdown.ts flowDiagram (108-113) and
  relationshipDiagram (115-127).
  Derived: polaris-markdown.ts:144-154 (the fence renderer) collects LITERAL fence
  lines (`body.push(lines[i++])`, then `body.join('\n')`); there is no offset/slice
  logic in polaris-markdown.ts (grep for `offset|stitch` returns only CSS and
  trajectory time-offsets). The actual offset stitching is in
  apps/three-surface-poc/src/polaris-reading.ts:107-111: `applyReadingPlan` builds the
  ```relations / ```flow fence source with `text.slice(from.start, from.end)` /
  `text.slice(body.start, body.end)` over `SourceSpan { start; end }` (defined :26-30).
  So the claim is CORRECT, but its locus is polaris-reading.ts, and the packet gives
  it no file:line (Q5 anchors 108-127 only to the correct "renders as list, never a
  graph" claim). A reader following the packet's anchors will not find the stitching
  at 108-127.
  Anchor: a9f671e:apps/three-surface-poc/src/polaris-reading.ts:26-30, :107-111.
  Delta: true claim, missing/misleading anchor. Also minor: these are JS string
  (UTF-16 code-unit) offsets via .slice, not "byte" offsets. Non-blocking.

F3 — editorial. Band label names a non-existent function.
  Packet claim (Q2, line 70): "The five HTML-returning helpers in the
  `escapedCauseRoute`…`unknownRoutes` band".
  Derived: no function named `escapedCauseRoute` exists anywhere in polaris.ts (grep
  0 hits); the band's first helper is `excludedCauseRoute` (416), which the same
  sentence then names correctly. A typo in the band label only.
  Anchor: a9f671e:apps/three-surface-poc/src/polaris.ts:416.
  Delta: name typo, corrected in the same clause. Editorial.

F4 — editorial. Off-by-one on the token-block line span.
  Packet claim (Measurement 4, ~line 197-198; Q6, line 74): "`design-tokens.ts`
  defines ten `:root` colour tokens (lines 45–55)".
  Derived: line 45 is `color-scheme: dark;`; the ten colour tokens (--ink … --focus)
  are lines 46-55. My sweep classifies exactly ten :root token-definition rows at
  46-55. The count (ten) is correct; the start line is off by one (45 vs 46). Note
  Measurement 5 separately and correctly places `color-scheme: dark` at line 45.
  Anchor: a9f671e:apps/three-surface-poc/src/design-tokens.ts:45-55.
  Delta: line-span start off by one; count exact. Editorial.

F5 — editorial. "two contrast-threshold pairs" excluded as non-colours is two values,
not two pairs.
  Packet claim (Measurement 4, line 208): "Three matches were excluded as
  non-colours: two contrast-threshold pairs in `polaris-accessibility.browser.test.ts`
  … and one `#0000…` fragment identifier".
  Derived: the test file contributes exactly two hex matches (#777777 line 37,
  #767676 line 39) plus the one #0000 in polaris-source-route.test.ts:130 — three
  excluded total, which is right, but "two pairs" implies four values; there are two
  values. The exclusion total (3) and the load-bearing stray counts (8 / 19) are
  unaffected.
  Anchor: a9f671e:apps/three-surface-poc/src/polaris-accessibility.browser.test.ts:37,39.
  Delta: wording ("pairs"); counts correct. Editorial.

================================================================================
INDEPENDENTLY DERIVED LOAD-BEARING VALUES (all reproduced)
================================================================================

polaris.ts line count: 1634 (matches packet's corrected 1,634; dossier's "1,615" not
independently checked, but 1634 is the true value). git-blame not needed; wc -l over
`git show a9f671e:apps/three-surface-poc/src/polaris.ts` = 1634.

Mutation-subject digests (record docs/evidence/pwb-p3-6-narrative-mutation-run-2026-09-04.json;
record has keys date/subjects/tests/results/killed/total, subjects is a per-file
sha256 map, NO `commit` key, killed 17 total 17 — confirms the packet's "binds by
per-file content sha256, no commit"):
  polaris.ts          recorded e5367575…5674  current b6dd1a90…f2a6  -> DIFFER
  polaris-narrative.ts recorded 0b0733ef…2e0b  current a97a80db…f3d   -> DIFFER
  polaris-copy.ts     recorded f6ab0f2a…c7e5  current 6a0dce8f…6d95  -> DIFFER
  page-shell.ts       recorded 5fb5a4cd…c39f  current c969d244…2da4  -> DIFFER
  All four recorded digests match the record's subjects block; all four current
  (sha256sum this session over a9f671e bytes) differ. Rule-10 gap is real. Second
  method: `git log --since=2026-09-04 a9f671e -- …/polaris.ts` = 14 commits (packet
  says "7 or more" — true and conservative). Full digests all 64 hex, file-content,
  not truncated/signed (CG-15 clean).

Five HTML-string helpers (a9f671e:polaris.ts): excludedCauseRoute 416,
unavailableCauseRoute 440, routeOf 462, reasonRouteHtml 472, unknownRoutes 480 — all
`: string`, signatures match the packet verbatim. escapeHtml import at line 3.
causeRoutes 448 returns `readonly string[]` (not an HTML-string helper). See F1/F3.

<svg / <canvas over the three captures (grep -c -F AND python str.count, byte
denominators = wc -c):
  polaris-direct.html   1,478,637 bytes  svg 0/0  canvas 0/0
  polaris-tailnet.html  1,484,487 bytes  svg 0/0  canvas 0/0
  polaris-7478.html     2,090,025 bytes  svg 0/0  canvas 0/0
  (SVG CSS does exist in polaris-generation/draft-preview.ts, which is the separate
  generation-kit page — NOT /polaris; the packet correctly scopes 0-SVG to the
  manifesto captures and the flowDiagram/relationshipDiagram renderers.)

Stray hex sweep (Python re `#(?:[0-9a-fA-F]{8}|{6}|{4}|{3})(?![0-9a-fA-F])` over
non-test src .ts, excluding `--token:` :root definition rows; second method: per-line
`#` count minus the ten token-def rows):
  design-tokens.ts stray = 8, lines 68,95,99,100,131,144,147,148 (line 131 = the
  8-digit RGBA `#3d2f1322`, which a {3,6} sweep misses — the {3,4,6,8} sweep catches
  it; confirmed).
  App-wide stray = 19: the other 11 in materialize-action.ts(4), orrery.ts(1),
  routes.ts(3), trajectory.ts(3). Ten :root token defs at 46-55. Total hex
  occurrences 32 = 19 stray + 10 defs + 3 test-excluded. All reproduce.

Dark theme: design-tokens.ts:45 `color-scheme: dark;` inside a single :root;
`prefers-color-scheme` = 0 matches across the whole app src;
docs/POLARIS-READING-LAYOUT.md (45 lines) has no theme/dark/light/color-scheme token
(case-insensitive). Forced, undocumented — confirmed.

Fence byte-offset stitching: polaris-reading.ts:107-111 over SourceSpan{start,end}
(see F2). polaris-markdown.ts:144-154 renders literal fence lines.

Gate 6 self-referential (committed packet bytes):
  bytes 39136; sha256 f6be38e10f7c8ac7b1129ccebe83f7e340ea234ed4718921713b9a82c7a11365;
  total_lines 430; non_fence 397; over_78 0; odd_backtick_non_fence 0.
  All match Gate 6 prose AND the JSON packet_measured / self_referential_figures
  blocks exactly.

Register: PENDING-OWNER-DECISIONS.md has exactly 27 lines starting `| P-` (two extra
`| P-` substrings at lines 51,81 are inside prose, correctly not rows). P-83 present
once, after P-82's section. (Aside, pre-existing and NOT a P-83 defect: P-25 appears
on two anchored rows.) P-83's row does NOT transcribe a digest — it points to "the
packet's Measurement 1 table lists each recorded-versus-current pair in full". P-83's
verdict/arms/default faithfully mirror the packet, and it carries the first-draft
rule-10 posture. CG-1b clean (no backticked Butlers path). CG-27 clean (the dated
tokens in table rows are act dates and the digest table's own column headers, none
leaning on a sibling row).

Six questions: each has Recommended + "Every lawful arm: (a)(b)(c)" +
"Counter-argument" + "Default if unanswered". Build/design classification defensible:
Q5 (model-derived SVG graph) = design; Q6 palette + curation halves = design; Q2's
Html brand is build because it strengthens SEC-1 CONFORMANCE without changing the
security POSTURE (the escaping already happens), so it trips no continuation-act
escalation trigger — a defensible reading. Q1/Q3/Q4 build arms are defensible
(evidence re-run edits no source; a11y is additive with no PWB-REQ pinning it;
module split is mechanical/byte-identical).

================================================================================
COUNTS: blocking 0 / non-blocking 2 / editorial 3
================================================================================
