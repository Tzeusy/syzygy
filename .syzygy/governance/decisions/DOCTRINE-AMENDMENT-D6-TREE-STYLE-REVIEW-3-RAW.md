Title: Doctrine D6 tree-style restyle — confirmation review 3
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: NEW-*.md vs OLD-*.md in review-d6c/, against REVIEW-2-RAW.md
Reviewer: independent fresh-context agent

**Scope and method.**
- I read `REVIEW-2-RAW.md` in full.
- I diffed every `review-d6b/NEW-*.md` against the matching `review-d6c/NEW-*.md`. The diff contains only the N1–N8 repairs, and `NEW-trust-and-evidence.md` is unchanged.
- I read each repaired passage with its surrounding section, next to the matching OLD text.
- `cmp` confirms `NEW-README.md` is byte-identical to `OLD-README.md`.
- No Mermaid diagram changed between d6b and d6c.
- I edited nothing.

## Part A — Status of REVIEW-2 findings

| # | Status | Current NEW text |
|---|---|---|
| N1 (material) | RESOLVED | vision.md and architecture.md, both: "**Reading reaches declared sources anywhere in the project; direct writing is confined to two roots.** Syzygy may *read* declared implementation and evidence sources anywhere…". The heading now matches OLD's "*declared* … sources", and no longer contradicts architecture.md's caption "Every edge from Syzygy is gated: each observed repository, governance root included, has consented (SEC-4)". |
| N2 | RESOLVED (see M1, editorial) | "The primary user is an owner running a portfolio of projects built largely by agent fleets, and who suffers the failures below." |
| N3 | RESOLVED (see M2, note) | "Syzygy is not merely an issue tracker with a code browser, not a documentation portal, not a replacement for its substrate, not an outward enforcer, and not autonomous." |
| N4 | RESOLVED | SEC-2: "No governed-project content, or anything derived from it, is sent to a store or service the owner does not control — model providers included — without explicit, recorded, per-project consent." The enumeration is kept under "**What is covered:** source structure, specs, work history, and anything derived from them, including prompts." |
| N5 | RESOLVED | SEC-3: "Observed-project code runs only inside an explicit, opt-in execution profile." followed by the bullet "**It is untrusted whoever owns the project.**" |
| N6 | RESOLVED | "One shared kernel holds the semantics every surface uses, and the three surfaces are only projections of it." This matches OLD "The kernel's shared semantics … must never fork across surfaces" and "all are projections over the one shared kernel". The claim "computes every truth" is gone, so the rule "There is no single universal source of truth" is no longer contradicted. |
| N7 | RESOLVED | "Three further points apply to V0:" |
| N8 | RESOLVED | "V0 shows whatever Genome artifacts and evidence each governed project has, marks everything else Unknown…". The bullet below keeps OLD's full list: "**whatever Project Genome artifacts and evidence exist** — doctrine and declared topology…, spec structure…, work-scheduling state, and code structure, including test and CI artifacts on disk." |
| Item 11 (REVIEW-1) | RESOLVED | The lead-in is now "Three further points apply to V0:", so the Trust floor release block is no longer framed as a limit on claims. |
| B16 (REVIEW-1) | RESOLVED | Items 9, 10 and 11 are all resolved now. |

## Part B — Drift check of the repaired passages

### Material

None. None of the repairs adds a rule, drops a qualifier, or narrows a scope compared with OLD. None contradicts other text in the same file:
- **N1:** vision.md's heading sits directly under the bullet naming the two roots, and above "Every other authority Syzygy affects only through typed, explicitly authorized adapters". Both agree with it. In architecture.md, the heading is consistent with the bullet above it ("confined to exactly two namespaces") and with the plane diagram and its caption.
- **N5:** the moved qualifier now attaches to the trust status, as in OLD. The run rule has no stray qualifier left.
- **N6:** the new opening agrees with the paragraph that follows it and with the kernel diagram (`K["Shared kernel<br/>definitions in .syzygy/governance/"]`).
- **N8:** "shows" in place of OLD's "observes" is a presentation verb. The bullet keeps "observes".

### Minor (notes only)

**M1. vision.md, "The human problem" opening: grammar.**
- Current: "an owner running a portfolio of projects built largely by agent fleets, and who suffers the failures below."
- "and who" has no earlier "who" clause to pair with. The meaning is acceptable: the listed failures are in the owner's own voice ("I don't know what my agents are doing").
- Fix: "…an owner who runs a portfolio of projects built largely by agent fleets and who suffers the failures below." Alternatively, restore OLD's split: "…agent fleets. The failures Syzygy exists to end:".

**M2. vision.md, "What Syzygy is not": the summary and the bullet differ.**
- Summary: "not merely an issue tracker with a code browser". Bullet: "**Not an issue tracker with a code browser.**" (OLD's wording).
- They are compatible: the bullet body explains the "more than" reading. But the summary hedges where the bullet does not.
- Fix, either:
  - leave as is (the bullet is authoritative OLD text); or
  - drop "merely" from the summary and qualify only "a replacement for its substrate", which is the item REVIEW-2 actually flagged.

**M3. vision.md line 304: B6 editorial carry-over (from REVIEW-2).**
- Current: "**Why it waits:** it waits only because live monitoring means nothing…"
- This is editorial only.
- Fix: "**Why it waits:** only because live monitoring means nothing…"

**M4. Reflow artifacts (cosmetic).**
- The N1 repair leaves a short line, "is confined to two roots.** Syzygy may *read*", in both files.
- Several lines are over 78 columns. Examples:
  - v1.md line 15, 80 columns, from the N8 repair;
  - vision.md line 209, 86 columns;
  - vision.md line 304, 98 columns.
- No code span is broken, so this is not the wrapped-citation hazard.
- Fix: reflow those paragraphs, keeping code spans whole.

## Part C — Spot check

In the sections I read around the repairs, I noticed nothing else beyond REVIEW-2's "No drift found" list. SEC-4 and SEC-5 still match OLD, and so do VIS-5's proposal and materialization bullets. REVIEW-2's material finding N1 is resolved, and so are its minor findings N2–N8. What remains is notes-only (M1–M4).
