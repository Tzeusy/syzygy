Title: Route and status pages tree-style restyle — review 3
Verdict: CONFIRM
Reviewed: OLD-*/NEW-* of PROJECT-STATUS.md, CONTRIBUTING.md, decisions__README.md, contracts__candidates__README.md, contracts__candidates__HOW-TO-AUTHOR-A-SYZYGY-SPEC.md, contracts__candidates__DEFERRED-WAVE-POSTURE.md, contracts__candidates__ROUND-ESTATE.md, docs__CAPABILITY-1-IMPLEMENTATION-PLAN.md, docs__PWB-IMPLEMENTATION-PLAN.md, plus REPAIR-DIFF.txt and R-TREE-STYLE-ROUTE-2-RAW.md (in /tmp/claude-1000/-home-tze-GitHub-syzygy/42f1d844-9fb6-4091-8261-544ed369daaf/scratchpad/review-route3/)
Reviewer: independent fresh-context agent

## Material findings

None.

## Round-2 findings

**M1: RESOLVED.**
- The NEW caption (decisions__README.md lines 34–35) now reads: "How an open question moves through this directory (the queue path only; not every decision or act starts as a queue row):". This is round 2's suggested fix, word for word.
- **Checked against the whole NEW page.** The caption no longer says which records start where. It claims only that at least one decision or act did not start as a queue row. Nothing in the page contradicts that:
  - The page shows queue-origin records, for example "P-33 ruled…", "P-54…P-59 and P-66 ruled…" and the P-79 direction.
  - It also lists records that name no P-row, for example "Owner launch decision, 2026-08-20", `THREE-SURFACE-POC-MODE-DIRECTION.md` and `OPENSPEC-MULTI-CHANGE-DIRECTION.md`.
  - The page supports the claim by showing the two kinds side by side rather than by stating it. [Observed] `THREE-SURFACE-POC-MODE-DIRECTION.md` and `OPENSPEC-MULTI-CHANGE-DIRECTION.md` in the repository contain no `P-[0-9]+` token, so the claim is also true of the repository.
- **Checked against the whole OLD page.** OLD had no diagram and no caption. Its sentence "They are not the same thing, and this directory holds both kinds of record" survives in NEW as "Decisions and acts are different records, and this directory holds both kinds." The new caption only limits what the diagram covers; it adds no rule the page lacks.
- The diagram itself is unchanged since round 2, byte for byte.

**N1: RESOLVED.**
- PROJECT-STATUS lines 22–24 now read "…specification is adopted and its implementation authorized and in progress; / the Polaris project-wide Butlers (PWB) work is authorized for one consented / content class. Each section cites the record that owns its rows." The lines are 75, 75 and 64 columns, and the orphaned "work is" line is gone.
- CONTRIBUTING lines 43–44 now read "- **Who it binds:** the project's own agents today, and it would bind / contributors later." The lines are 69 and 21 columns.

## REPAIR-DIFF hunks read against OLD

1. **PROJECT-STATUS (reflow).** Only whitespace changed: the word sequences before and after the repair are identical by script (3,796 = 3,796 tokens). This hunk adds no drift.
2. **CONTRIBUTING (reflow).** Only whitespace changed: the word sequences are identical by script (989 = 989 tokens). It still matches OLD's "This binds the project's own agents today and would bind contributors later." No modal or scope changed.
3. **decisions/README (caption).** The wording changed, as assessed under M1. The claim is now narrower than round 2's, and it is supported. Lines 34–35 are 71 and 49 columns, and the hunk touches no code span.

## Notes

- **N1:** The caption's support in the page is implicit, as described under M1; the page never states it outright. This is acceptable for a sentence that only limits the diagram's scope, and no repair is needed.
- **N2:** My fence count disagrees with round 2's text. Round 2 reports "8/8 original blocks". My re-run of the same script over the same OLD files counts **7** original fenced blocks (PROJECT-STATUS 1, HOW-TO 2, candidates/README 1, decisions 1, CAP1 1, PWB 1), all byte-identical, plus 8 added Mermaid blocks. The OLD files are byte-identical to round 2's OLD files (`cmp`, 9/9). So this is a counting slip in the round-2 raw, not a change.

## Checks

The scope check used `diff` between the round-2 NEW files and the current NEW files, 9 of 9 files:
- Only three files differ: PROJECT-STATUS, CONTRIBUTING and decisions/README.
- Each differs only at the lines of its REPAIR-DIFF hunk.
- The other six files are byte-identical.
- The OLD files are unchanged since round 2 (`cmp`, 9 of 9 identical).

I re-ran round 2's `chk.py`, repointed at review-route3 (my copy is in `…/scratchpad/r3chk/`), over OLD vs NEW for all 9 pairs. Of the 45 structural comparisons (banners, headings, tables, fences and links, one each per pair), 0 report `False`.

| Check | OLD | NEW | Result |
|---|---|---|---|
| Banners | 103 lines in 8 files (CONTRIBUTING has none) | 103 lines | Byte-identical |
| Headings | 72 | 72 | Identical in text, level and order |
| Table rows | 241 | 241 | Byte-identical and in order |
| Fenced blocks | 7 | 7 original, plus 8 added Mermaid | Originals byte-identical (see N2) |
| Links | 89 | 89 | Identical target multisets |
| Identifiers | 551 | 565 | 0 lost in any section; the 14 additions are the same set round 2 listed |
| Dates | 297 | 300 | 0 lost; the same 3 additions as round 2 |
| Code spans | 1,253 | 1,261 | 0 lost; the same 8 additions as round 2 |
| Broken code-span lines | 40 | 32 | 0 new |
| Epistemic labels | Observed 34, Inferred 8, Unknown 7 | Same | Identical in every file |

Every figure except the fence count (see N2) equals the round-2 raw's.

Line length: none of the 7 lines the repair touched exceeds 78 columns. The over-78 lines that remain in these three files are banners, table rows and Mermaid lines, and none was touched by the repair.
