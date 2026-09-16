# R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL REVIEW 2 (RAW)

Independent fresh-context second review. Read-only. This review confirms
review 1's eleven exception repairs (verification rule 10) and looks for
new defects. All figures below were computed this session against the
worktree bytes; digests are scripted, never transcribed.

Worktree: scratchpad/m13wt   Branch: agent/syzygy-dov.13   HEAD: 893cbda
git status --short: clean before and after.
Governance battery in this worktree (tail line, read not grepped):
  32 OK, 20 WARN, 0 FAIL (52 checks) - counts derived, not asserted

## Reviewed files (wc -c ; sha256sum, computed this session)

docs/design/POLARIS-M13-NAVIGATION-SCALE-FUNNEL.md
  133570  5e808cfe8dfc062c0a49842f708a84258d28be486dc1ddd7227e2775d1afa8ed
docs/evidence/polaris-m13-navigation-scale-funnel-2026-09-15.json
   62481  4c975d9a4fee7d0fdc3f83abd22af11e472280357f2e32ac45855f5bf7cf4b41
.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md
   35734  3ca492e0dbc790d40859ca8932dc7535ab56c51ca6161f13ec48eca1d147a8fa

Review 1 (retained verbatim, verdict CONFIRM WITH EXCEPTIONS: 0 blocking,
non-blocking F1-F6, editorial F7-F11) was bound to 97b37ee, where the
packet was 97146 B and the evidence record 39197 B - different bytes.
Every edit of this pass post-dates it, so its repairs were uncovered
until this review; this review covers them.

## Part (a) - Review-1 repair verification (F1-F11)

| ID | Verdict | Evidence (this session) |
|----|---------|-------------------------|
| F1 | REPAIRED | polaris-markdown.ts source: 156 `}`, 157 the |
|    |          | regex `/^ {0,3}(#{1,6}) +(.+?)(?: +#+)? *$/`, |
|    |          | 158 `if (heading) {`, 159 the level expression |
|    |          | `Math.min(6, heading[1]!.length + 3)`. Packet |
|    |          | now anchors "lines 158-162 / line 159"; old |
|    |          | "lines 156-160"/"line 157" survive only inside |
|    |          | dated [Superseded ... F1] brackets (L332-338, |
|    |          | 218, 730). Record: original anchor kept, dated |
|    |          | sibling `expression_2026-09-15_review1`. The |
|    |          | close-out worker is RIGHT: review 1's sixth |
|    |          | site does not exist; five sites repaired, and |
|    |          | mutant (a) quotes the expression not a line. |
| F2 | REPAIRED | Re-derived at a9f671e under the stated |
|    |          | predicate (four prefixes .syzygy/ openspec/ |
|    |          | docs/ scripts/): 913 tracked files; 66 whose |
|    |          | path contains "manifest" case-insensitively; |
|    |          | 0 of the 15 surface files as a digest row. |
|    |          | Over 96 docs/evidence files: polaris.ts in 18, |
|    |          | polaris-project-shape.test.ts 9, polaris-copy |
|    |          | .ts / .test.ts / polaris-first-reading.test.ts |
|    |          | 4 each, polaris-reading-plan.ts and |
|    |          | polaris-accessibility.ts in none - every cited |
|    |          | figure reproduces. The published "2" is |
|    |          | polaris-manifesto-example-mutation-2026-09-09 |
|    |          | .json ("manifest" substring of "manifesto"). |
|    |          | 15 re-run / 5 re-anchor partition predicate is |
|    |          | stated in the record and is sound. |
| F3 | REPAIRED | polaris-parity-sweep.test.ts:494 quoted whole: |
|    |          | `if (section.inner.includes('<tbody>') ||` |
|    |          | `section.inner.includes('<ul class="item-`    |
|    |          | `list"'))`. 0 of 409 data-polaris-item carry |
|    |          | an id (record's negative check reproduces). |
|    |          | Slice 5 gains the guardrail paragraph + fifth |
|    |          | rule-6 mutant over the class-population code. |
| F4 | REPAIRED | The four numbers are CHARACTER indices; the |
|    |          | UTF-8 byte offsets are the dated sibling keys. |
|    |          | Packet now labels 912,381 / 281,945 / 88,024 / |
|    |          | 88,501 as character indices (L353, L422) and |
|    |          | old "byte" wording sits in the correction. |
|    |          | Record keeps original values unedited with |
|    |          | `*_utf8_byte_offset_2026-09-15_review1` keys. |
| F5 | REPAIRED | Packet now says THREE affordances stop without |
|    |          | script: SECTION_NAV_SCRIPT drawer, aria-current |
|    |          | cue, and the hash-driven guide opening |
|    |          | (polaris.ts 1243-1258). Record F5 sibling |
|    |          | records the third; 0 <details open> + 10 |
|    |          | href="#polaris-guide-" on the post-trim page. |
| F6 | REPAIRED | POC-REQ-030 present at POC spec 496/507/518 and |
|    |          | design.md 25; Gate 5 reads it per slice and |
|    |          | strengthens Q1 arm (c) without choosing it - |
|    |          | it reads, does not rule, for Q1. |
| F7 | REPAIRED | Heading-attribute sentence scoped; no over- |
|    |          | broad "all headings carry an id" claim stands. |
| F8 | REPAIRED | Over-78 re-derived last = 19 under the stated |
|    |          | predicate (outside fences; first non-space |
|    |          | char not `|` `>` `#`; >78 cols; denominator |
|    |          | every line). This MATCHES the worker's stated |
|    |          | predicate. Old "20" and its mischaracterisation |
|    |          | of lines 1166/1016 sit in the [Superseded F8] |
|    |          | note; both were rewrapped. |
| F9 | REPAIRED | decisions denominator disclosed: 67 top-level, |
|    |          | 73 whole tree (6 under launch-gate/). Sweep |
|    |          | `\b(?:script|javascript|progressive\w*)\b` |
|    |          | over 73 files = 9 lines (7 over the 67), all |
|    |          | nine read, 0 constrain Polaris scripting. All |
|    |          | three worker figures reproduce: 9 word-bounded |
|    |          | matched-lines is the published pattern's count. |
| F10 | REPAIRED | Source: tableRegion polaris.ts 159-161; |
|    |           | depthNav 1529-1558 (1557 closes <nav>, 1558 |
|    |           | the fn); exactTextLink def 377, calls 533/552/ |
|    |           | 836/1081 = 4 call sites over 5 lines. "5 call |
|    |           | sites" is absent; "1529-1556" survives only in |
|    |           | dated supersession notes. |
| F11 | REPAIRED | PWB spec line 679 read in full: PWB-REQ-012 |
|    |           | closes four roles (project-fact, epistemic- |
|    |           | disclosure, action-label, scope-instruction), |
|    |           | a 6-word heading limit, 20-word lede limit, a |
|    |           | 6-term prohibited list, two cardinalities; no |
|    |           | closed set of strings, does not govern |
|    |           | POLARIS_COPY. Q3's old "closed copy table" |
|    |           | conflation survives only in [Superseded F11]; |
|    |           | live Q3 sentence is correct. |

Q1-Q5 recommendation, arms and default are byte-identical to
`git show 97b37ee:<packet>`: Q2-Q5 rows identical; Q1's question column
changed only in its measurement prose (F1/F9 repairs), and its
recommendation/arms/default segment is byte-identical. Review 1 moved no
arm, recommendation or default.

## Part (b) - load-bearing measurements re-run at review-2 bytes

All reproduce exactly. polaris-copy.ts 129 'Source record' / 134 'Exact
text', row of POLARIS_COPY at line 25. Captures (pre/post-trim): 'Exact
text' 372/386 links over 185/192 distinct targets, source-record 271/278,
<details> 353/359, <details open> 0, h6 15/14, table/tbody 10/10 & 5/5.
Scripting posture: <script 2 pre / 1 post (SECTION_NAV_SCRIPT, polaris.ts
1232-1289), 0 <noscript> on the page (Orrery's at orrery.ts 144-146).
Register/script sweep, byte offsets, tab stops and per-class catalogs all
re-derive as review 1 reported. RFC9-13.c1 coverage row at
openspec/changes/polaris-project-wide-butlers-model/contract-coverage-
matrix/RFC-0007-0009.md is bound in the 2026-09-05 truth-and-readiness
act's manifest (that file is a manifest row). Two retained fidelity-review
hashes reproduce: polaris-reading.ts = bea0e59d... and polaris-reading-
plan.ts = 732e410c... match the retained -CONFIRMATION- raw exactly, while
polaris.ts current b6dd1a90... no longer matches its listed hash - exactly
as the packet states (rule-10 forward). Continuation act triggers at
lines 150-156 are quoted verbatim and complete. Collision table: 15
surface files, 13 rows, predicates disagree on 7, polaris.ts collides in
11 under predicate B, M3 (6574600, P-70) 6 under A / 7 under B; all 13
sibling HEADs read match the expected list.

## Part (c) - the register

P-80 row (line 216) is a faithful one-line rendering of the packet's
Q1-Q5 table after the repairs: each Q's recommendation, every lawful arm
and the default are carried through verbatim, with the counter-arguments
and the F6/F11 additions. The "Updated 2026-09-15" blockquote's verdict
word and counts are exact: "CONFIRM WITH EXCEPTIONS - 0 blocking, 6 non-
blocking, 5 editorial, F1-F11" (line 126), matching the retained raw.
Recount reproduces by a stated predicate (count `^| P-` rows partitioned
by `##` section): acceptance section = 5 (P-1,2,3,4,24); open section = 22
(P-10..P-52, P-34, P-80); 27 in all. main at a9f671e = 21 open + 5 = 26,
no P-80 - the blockquote's basis. Twelve sibling registers each carry 27
P-rows and NONE carries P-80; each has exactly one row at or above P-68
(P-68 lane B ... P-79 M12). The P-80 row quotes no digest and backticks no
Butlers path (CG-7e/CG-15/CG-1b clean). check_governance names the
register in exactly two WARN lines, at its own lines 9 and 13 - both
inside the 2026-08-17 header blockquote, neither the P-80 row - as the
packet's own sentence states.

## Part (d) - the five questions

Scope truthful; each is a genuine hard human gate; each recommendation
follows from the evidence; every lawful arm is named and none called
unlawful; no owner trade-off is smoothed into consensus language (the
counter-argument to Q1 is ranked above the packet's own recommendation,
and Q2's comprehension trade-off is preserved). No owner question is
hidden as decided: heading normalization is a no-trade-off a11y repair
(slice 2) and is properly decided in-packet, while the subtle label-
interpolation question it touches is surfaced as Q3. The dossier
prerequisite line ("None") is fairly tested - it survives for slices 1-4
and is corrected for slice 5 via the bound RFC9-13.c1 row and Q4. The
packet rules where it may (slices 1,2,4) and asks where authority or a
trade-off is at stake (Q1-Q5, slices 3 and 5).

## Part (e) - new-defect sweep

Self-referential convention figures are true of the bytes that carry
them: 133,570 bytes (wc -c); 1,631 newline segments (wc -l 1630 + final
line); 1,589 non-fence lines; 0 odd-backtick non-fence lines; 19 over-78
under the stated predicate; 304 distinct code spans with 20 slash-bearing
and non-resolving (os.path.exists from worktree root) - all reproduced.
The worker's own additions check out: the check_governance sentence names
the two WARN lines at register lines 9 and 13 correctly; the 232/15 ->
304/20 code-span census re-derives under its stated predicate. Every stale
phrase the prompt listed survives ONLY as marked, dated, superseded text
or as a faithful quotation of a review-1 finding - none stands as a live
claim; "2 appear as a path", "5 call sites" and "no independent review"
are absent as live literals. No zero/all claim lacks a predicate and
denominator; no unlabeled substantive claim; every code-span path
resolves except the 20 the record enumerates as non-path spans; no
superseded wording is deleted rather than marked; the evidence JSON gives
every review-1 correction a dated sibling key and keeps each prior-bound
value unedited (the first-draft packet digest and the collision.register_
rows block are preserved per rule 10, with current state in the prose and
the appended review1 block). No new defect found.

## New findings

None.

## Q1-Q5 table

| Q | Scope truthful? | Genuine gate? | Rec. follows? | Arms named? |
|---|-----------------|---------------|---------------|-------------|
| Q1 | yes | yes | yes | yes (a/b/c) |
| Q2 | yes | yes | yes | yes (2 arms) |
| Q3 | yes | yes | yes | yes (2 arms) |
| Q4 | yes | yes | yes | yes (2 arms) |
| Q5 | yes | yes | yes | yes (2 readings) |

All eleven review-1 exception repairs (F1-F11) are confirmed REPAIRED
against current bytes and source; no repair is partial or missing; no new
blocking, non-blocking or editorial defect was found; Q1-Q5's
recommendations, arms and defaults are unchanged from 97b37ee. The
packet's rule-10 obligation (a second independent review of the eleven
repairs) is satisfied by this review.

Verdict: CONFIRMED
