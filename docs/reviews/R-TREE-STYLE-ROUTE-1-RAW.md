Title: Route and status pages tree-style restyle — review 1
Verdict: REVISE
Reviewed: OLD-*/NEW-* of PROJECT-STATUS.md, CONTRIBUTING.md, decisions__README.md, contracts__candidates__README.md, contracts__candidates__HOW-TO-AUTHOR-A-SYZYGY-SPEC.md, contracts__candidates__DEFERRED-WAVE-POSTURE.md, contracts__candidates__ROUND-ESTATE.md, docs__CAPABILITY-1-IMPLEMENTATION-PLAN.md, docs__PWB-IMPLEMENTATION-PLAN.md (in /tmp/claude-1000/-home-tze-GitHub-syzygy/42f1d844-9fb6-4091-8261-544ed369daaf/scratchpad/review-route/)
Reviewer: independent fresh-context agent

The structural checks all pass. Every banner, heading, table row, fenced block, link, identifier, date and script-read literal is intact. PROJECT-STATUS is still a faithful status page. The problem is in six new answer-first openers and one diagram: each says more, or something slightly different, from what the body says. Under criterion 1 that counts as a meaning change, so the verdict is REVISE. Each fix is a single-line edit.

## Material findings

**M1 — candidates/README.md, §Layout: the opener claims something the table does not do.**
- OLD: (no opener) → NEW: "One row per file class; each row says whether that class binds anything."
- Why it matters: 7 of the 21 Layout rows say nothing about whether they bind:
  - `wave-manifests/`
  - `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`
  - `fixtures/`
  - `reviews/`
  - `scripts/`
  - `DEFERRED-WAVE-POSTURE.md`
  - `FIRST-OPENSPEC-SEQUENCE.md`

  Some other rows qualify only through a name or a word such as "candidate". A reader who stops at the opener would take silence in a row to mean "binds nothing".
- Fix: "One row per file class." Or make it: "…; the head banner says what binds."

**M2 — decisions/README.md, §4: the opener strengthens and widens the body.**
- OLD: (no opener); the body says "You should be able to make every decision above without opening any of them" (meaning the raw review bytes), and the table tells readers to read `PROCESS-LESSONS.md` "before writing or trusting a check".
- NEW: "History is kept but never needed to make a current decision."
- Why it matters: the body's "should be able to" becomes an absolute "never needed". It is also widened from raw reviews to all history, which contradicts the PROCESS-LESSONS row just below it.
- Fix: "History is kept off the default path; a current decision should not need it."

**M3 — CAPABILITY-1-IMPLEMENTATION-PLAN.md, §slices: the opener misstates slice S0.**
- OLD: (no opener) → NEW: "Eight slices, S0 to S7, each claiming a named set of requirements."
- Why it matters: S0's row reads "(foundations for all; no requirement claimed implemented)". "Each" is therefore false for S0.
- Fix: "Eight slices, S0 to S7; S1–S7 each claim a named set of requirements, and S0 claims none."

**M4 — ROUND-ESTATE.md, §The eleven rounds: an inferred characterization is stated as fact.**
- OLD: (no opener) → NEW: "Most rounds' settlements now live in acts, decisions, or the launch-gate instrument; …"
- Why it matters: the body makes no such claim, and the table barely supports "most":
  - At most 6 of the 11 rows land in an act, a decision or the instrument: 08d, 08e, 08g, 08h, 08i, 08k.
  - Five land elsewhere:
    - 08 is "Nowhere current".
    - 08b's home is `scripts/check_governance.py`.
    - 08c is "Still open".
    - 08f is a superseded packet plus a live CI input.
    - 08j's settlement is the round's own reports.
  - This is new, unlabelled synthesis on a page where every other figure is derived and labelled.
- Fix: drop "Most … instrument;" and keep "The table names where each round's settlement lives now, and says **Nowhere current** or **Still open** where that is the answer."

**M5 — PWB-IMPLEMENTATION-PLAN.md, §1: the `[Observed]` label covers less than it did.**
- OLD, one paragraph: "**No new language, package, runtime dependency or route.** `[Observed]` The adopted registry entry names … so no `tsc -b` project list or Vitest project entry changes. TypeScript on Node ≥22.15, Vitest, `tsc -b --force` for `build:poc`, exactly as today."
- NEW: the text is split into two sibling bullets. `[Observed]` is on the first; "TypeScript on Node ≥22.15, … exactly as today." is now an unlabelled sibling.
- Why it matters: the page's header says unlabelled statements are "`[Inferred]` planning". Moving that sentence out of the labelled paragraph re-labels a claim about the current stack from Observed to Inferred. Elsewhere the restyle correctly nests follow-on sentences under their labelled parent (PROJECT-STATUS generator bullets; PWB §3 items 4–6); this is the one sibling split.
- Fix: nest the TypeScript bullet under the `[Observed]` bullet, or keep the two sentences in one bullet.

**M6 — decisions/README.md: the new diagram asserts a flow the text does not.**
- NEW diagram: `O{"Owner rules"}` branches `-->|recorded prose| D`, `-->|ceremony phrase + digest| A`, `-->|resolved row| H["DECISION-HISTORY.md"]`.
- Why it matters:
  - A decision diamond reads as mutually exclusive outcomes. The text shows a ruling producing both a record and a history move: P-54…P-59/P-66 were "Ruled 2026-09-07 — record `DOCUMENTATION-ESTATE-OWNER-RULINGS-DECISION.md`; the seven rows have left `PENDING-OWNER-DECISIONS.md` for `DECISION-HISTORY.md`".
  - It also implies every decision and act starts as a queue row. The page never says that; the owner directions and foundational offerings, for example, do not.
- Fix: make "resolved row → DECISION-HISTORY" a separate edge from the queue row that fires alongside D or A, not a third alternative. Or add a one-line caption saying the diagram shows the queue path only, not every decision's origin.

## Notes

- **N1 — Accurate counts introduced.** Each is correct today, but each is a new figure that can go stale:
  - PROJECT-STATUS: "Four dated groups of acts, 2026-09-01 to 2026-09-05" (the fourth group, "Later on 2026-09-02", is out of date order in the body, as before).
  - CAP1 plan: "Eight slices"; "The five escalation triggers".
  - PWB plan: "eight slices P1–P8"; "Four observed items and one inferred assumption".
  - HOW-TO: "the five questions".
  - Consider dropping the PROJECT-STATUS one, since the page will gain further act groups.
- **N2 — HOW-TO §E1 opener** "Each question has one owner" sits over rows whose owners are compound: "P-39 + the adapter contract", "RFC 0003 / RFC 0004", "CC-REV-2 + … workflow". Suggest "Each row names the question's owner."
- **N3 — HOW-TO §E4 opener** gives only two of the four routes in the fenced rule (it omits craft policy and informative text). Suggest "One classification rule, in the block below, decides it."
- **N4 — CONTRIBUTING.** Two small shifts:
  - "This binds the project's own agents today and would bind contributors later" became "**Who it binds:** the project's own agents today; contributors later". The conditional "would" is gone; suggest restoring it.
  - The page opener says documentation and governance proposals "are welcome", where the body only said they "follow the disciplines below". Mild.
- **N5 — PROJECT-STATUS page opener.** "the generalized Polaris generator is adopted": it was the specification that was adopted, not the generator. Suggest "the generator specification is adopted and its implementation authorized and in progress".
- **N6 — PWB §3 numbered list.** Turning the eight-check run into items 1–8 puts "item 3" (meaning RFC3-16(b) item 3) inside list item 2, next to a list item 3. That invites misreading; suggest "RFC3-16(b) item 3".
- **N7 — PWB §4 diagram** hangs "resource-limit breach" off the read-guard node. The text does put the `resourceLimits` paragraph under the read-guard bullet, but some of the limits (parse time, rendered bytes) apply later in the pipeline. Acceptable; a looser attachment would be more accurate.
- **N8 — Code spans broken across a line (criterion 3).** 32 remain after the restyle:
  - 28 in the PWB plan, 2 in the CAP1 plan (lines 27–28, an `[Inferred — …]` span), 2 in ROUND-ESTATE (lines 164–165).
  - Every one is byte-identical to a line that was already broken in OLD (40 broken lines in OLD).
  - The restyle repaired 8 in the PWB plan and introduced none. NOTES.md's "No new line with an unpaired backtick" is accurate but does not disclose the 32 left over.
- **N9 — Existing problems, not caused by the restyle.** Adding lines shifts the line-number citations into these pages from `docs/evidence/*` logs and JSON, the pursuit JSONs and `DOCUMENTATION-ESTATE-DECISION-PACKET.md:22`: 54 citations, all already stale at OLD or historical evidence. The stale statements NOTES.md lists are real and remain in the pages:
  - HOW-TO says "implementation stays forbidden".
  - candidates/README gives CC-SPEC as "Act 7".
  - It also says "Five directories" of act packages.

## Checks run (Python, OLD vs NEW, 9 file pairs)

- **Banners:** 8 files have a head `>` banner (103 lines in all), all byte-identical; CONTRIBUTING has no banner.
- **Headings:** 72/72 identical in text, level and order.
- **Table rows:** 241/241 byte-identical and in order.
- **Fenced blocks:** 8/8 original blocks byte-identical, including PROJECT-STATUS "How to verify this page". 8 Mermaid blocks were added. Each diagram was compared with its page's text: 7 are consistent (for the PWB §4 diagram, see N7), and the decisions/README diagram is M6.
- **Links:** 89 in OLD, 89 in NEW, same targets.
- **Identifiers:** 535 occurrences, 322 distinct per file. Checked globally and per section (keyed by heading): none lost, no count decreased, none added.
- **Dates:** checked globally and per section: none lost, no count decreased.
- **Code spans:** 1,213 in OLD; none lost, apart from 4 fragments of formerly broken spans in the PWB plan. Each rejoined span was checked against OLD's whitespace-normalized text and found verbatim. The 6 other spans added are repeats of existing literals.
- **Broken code spans:** every NEW line with an odd backtick count is verbatim in OLD (see N8).
- **Epistemic labels:** counts are identical in every file (Observed / Inferred / Unknown). Each label's context was read; one span change found (M5).
- **Script-read literals:** 13,301 string literals (25–300 characters) from 347 script, app, package and CI files. 504 of them appear in the OLD pages; 0 are missing from NEW.
- **Deleted words:** a word-level SequenceMatcher listed every deleted run (253 words over the 9 files). Each was traced to a move or a list-punctuation change, apart from "would bind" (N4).
- **Modal and quantifier word counts:** compared per file. Every addition sits in a reviewed opener.
- **PROJECT-STATUS (criterion 4):** every act, date, digest prefix, figure and in-force/pending state is unchanged. The only new figure is "Four dated groups" (N1).
