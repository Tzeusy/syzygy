Title: Route and status pages tree-style restyle — review 2
Verdict: REVISE
Reviewed: OLD-*/NEW-* of PROJECT-STATUS.md, CONTRIBUTING.md, decisions__README.md, contracts__candidates__README.md, contracts__candidates__HOW-TO-AUTHOR-A-SYZYGY-SPEC.md, contracts__candidates__DEFERRED-WAVE-POSTURE.md, contracts__candidates__ROUND-ESTATE.md, docs__CAPABILITY-1-IMPLEMENTATION-PLAN.md, docs__PWB-IMPLEMENTATION-PLAN.md, plus REPAIR-DIFF.txt and NOTES.md (in /tmp/claude-1000/-home-tze-GitHub-syzygy/42f1d844-9fb6-4091-8261-544ed369daaf/scratchpad/review-route2/)
Reviewer: independent fresh-context agent

The repair fixes M1–M5 and M6's decision-diamond problem, and the structural checks all hold. But the M6 repair's new caption adds a claim of its own, and the page and the repository contradict it. That is one material finding, and the fix is a single line.

## Material findings

**M1 (new, introduced by the M6 repair) — decisions/README.md: the diagram caption states an origin rule that the page contradicts.**
- OLD: "They are not the same thing, and this directory holds both kinds of record." There was no diagram and no caption.
- NEW: "How an open question moves through this directory (the queue path only; owner directions and foundational offerings do not start as queue rows):"
- Why it matters:
  - **Owner directions.** The page's own by-date table, which is unchanged, lists `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md` as "Retention posture for retained Polaris evaluation records (P-79 gate `syzygy-dov.28`)". [Observed] `DECISION-HISTORY.md:53` holds the resolved **P-79** row ("Ruled — A"), and the direction file's line 9 reads "Warrant for the question: row **P-79**". So at least one owner direction did start as a queue row.
  - **Foundational offerings.** The page's pending row counts "5 open acceptance-act rows" in the register, and says "P-1's row stays open for the deferred C/D waves". §3 lists **P-12** as the knowledge-hygiene craft policy, and the act row names "P-12 knowledge hygiene" as the ninth foundational offering. So foundational offerings sit in the queue as rows.
  - The body never makes the caption's claim about where things start. The round-1 fix asked only for "the queue path only, not every decision's origin".
- Fix: "(the queue path only; not every decision or act starts as a queue row)".

## Round-1 findings

- **M1 RESOLVED.** Now reads: "One row per file class; each file's head banner says what binds." It no longer claims the rows state binding.
- **M2 RESOLVED.** Now reads: "History is kept off the default path; a current decision should not need it." The "should" modal is restored and the claim no longer covers all history in absolute terms.
- **M3 RESOLVED.** Now reads: "Eight slices, S0 to S7; S1–S7 each claim a named set of requirements, and S0 claims none."
- **M4 RESOLVED.** Now reads: "The table names where each round's settlement lives now, and says **Nowhere current** or **Still open** where that is the answer."
- **M5 RESOLVED.** Now reads: "`[Observed]` The adopted registry entry … Vitest project entry changes. TypeScript on Node ≥22.15, Vitest, `tsc -b --force` for `build:poc`, exactly as today." Both sentences are in one labelled bullet, as in OLD. The code span `tsc -b --force`, broken across a line in OLD, is now joined.
- **M6 PARTIAL.**
  - Fixed: the resolved-row edge is now a separate dotted edge from the queue row, `Q -.->|"once ruled, the row moves"| H`, so outcomes are no longer shown as exclusive alternatives. The P-54 row supports it.
  - Not fixed: the caption overreaches (new M1 above).
- **N1 RESOLVED for PROJECT-STATUS.** Now reads: "Dated groups of acts, 2026-09-01 to 2026-09-05, define …". The other counts stay, as allowed.
- **N2 RESOLVED.** Now reads: "Each row names the question's owner; follow the row to it."
- **N3 RESOLVED.** Now reads: "One classification rule, in the block below, decides it."
- **N4 RESOLVED.**
  - "**Who it binds:** the project's own agents today, and it would bind contributors later."
  - The opener now reads "issues and discussion are welcome, and documentation or governance proposals follow the disciplines below", which matches OLD's "Issues and discussion are welcome; documentation and governance proposals follow the disciplines below."
- **N5 RESOLVED.** Now reads: "the generalized Polaris generator specification is adopted and its implementation authorized and in progress".
- **N6 RESOLVED.** Now reads: "2. then the nine RFC3-16(b) items (RFC3-16(b) item 3 by recomputing …". This adds one repeat of the `RFC3-16` identifier in §3; it is a clarifying repeat.
- **N7 LEFT.** The reason given (the review called it acceptable) is valid; the diagram is unchanged.
- **N8 LEFT.** The reason given is valid. I confirmed 32 broken lines remain (28 PWB, 2 CAP1, 2 ROUND-ESTATE), every one byte-identical to an OLD line, with none new.
- **N9 LEFT.** The reason given is valid: the problems predate the restyle and are for the owner.

## Notes

- **N1 — Reflow damage in PROJECT-STATUS from the N5 repair.** NEW line 22 is 116 columns long, and line 23 is just "work is". No code span is affected, so this is cosmetic, but it needs reflowing. CONTRIBUTING line 43 (the N4 repair) is 82 columns.
- **N2 — PROJECT-STATUS "How to verify" opener** (not touched by the repair): "Run the block below from the repository root … it is the canonical battery."
  - "from the repository root" and "canonical" are not in the page body. The first is implied by the relative paths; the second is AGENTS.md's word.
  - It is mild, and consistent with the body's "Run it in a clone" and "Read the output, not the exit code".
- **N3 — Spot-read of openers and diagrams the repair did not touch: no further meaning drift found.**
  - PROJECT-STATUS: closed-gates opener (all 15 rows ✅) and open-gates opener (matches the heading "beyond the launch path").
  - DEFERRED-WAVE: the wave answer (C1's "launch-scope priority only") and "Every route except the deferred-labelled ones avoids them" (matches "no other route reaches them").
  - CAP1: "Done means both" (OLD line 84) and "The riskier the class, the more independent the review" (the class table).
  - PWB: the §6 opener (the independence column, and "Each predicate … carries a mutation-point") and the §7 P4 first-read claim (row P4 and the existing bullet).
  - ROUND-ESTATE: the partition diagram (74 + 2 + 1 + 19 = 96).
  - candidates/README: the placement diagram.

## Checks run (Python, OLD vs NEW, 9 file pairs)

- **Banners:** 8 files have a head banner, 103 lines in all, and all are byte-identical. CONTRIBUTING has none.
- **Headings:** 72/72 identical in text, level and order.
- **Table rows:** 241/241 byte-identical and in order.
- **Fenced blocks:** 8/8 original blocks are byte-identical. There are 8 added Mermaid blocks: PROJECT-STATUS 1, candidates/README 1, ROUND-ESTATE 1, decisions/README 1, CAP1 1, PWB 3.
- **Links:** 89 → 89, with identical target multisets.
- **Identifiers**, per section keyed by heading (my regex covers `X-n` forms, RFC-nnnn, SDR, P-n and syzygy-* beads):
  - 551 → 565 occurrences; 0 lost in any section.
  - All 14 additions are repeats inside openers or diagrams:
    - VIS-5 (CONTRIBUTING)
    - PWB-REQ-005 (the PROJECT-STATUS diagram)
    - CC-SPEC-1 (HOW-TO)
    - 8 in candidates/README (answer line, diagram, section answers)
    - CC-REV-6 (ROUND-ESTATE)
    - RFC3-15 (decisions/README)
    - RFC3-16 (the N6 repair)
- **Dates:** 297 → 300; 0 lost per section. The additions are 2026-09-01 and 2026-09-05 in the PROJECT-STATUS act-group opener and 2026-08-17 in the candidates/README diagram, all repeats of dates already in the body.
- **Code spans**, extracted with line breaks joined so that previously broken spans count whole: 1,253 → 1,261, 0 lost. The 8 additions are repeats of existing literals in openers (`craft-and-care/`, `REVISE`, `policy-candidates/`, `contracts/rfcs/`, `reviews/DISPOSITIONS.md`, `decisions/PROCESS-LESSONS.md`, `ACCEPTANCE-ACT-RECORD.md`, `PocModel`).
- **Broken code-span lines** (odd backtick count, outside fences): OLD 40, NEW 32; every NEW one is present verbatim in OLD, so 0 are new.
- **Epistemic labels:** counts are identical in every file (Observed 34, Inferred 8, Unknown 7). I re-read the M5 span in context: restored.
- **REPAIR-DIFF.txt:** all 10 hunks read against OLD. There is one new drift, material M1 above, plus the reflow in N1. The other 8 hunks are faithful.
- **PROJECT-STATUS (criterion 4):** tables are byte-identical (43 rows), and no act, date, digest prefix or in-force/pending state changed. The repair removed the "Four" count; the only other repair edit is the opener fix.

The check scripts are in `/tmp/claude-1000/-home-tze-GitHub-syzygy/42f1d844-9fb6-4091-8261-544ed369daaf/scratchpad/r2chk/`: `chk.py` for the structural checks and `ins.py` for the word-level diff.
