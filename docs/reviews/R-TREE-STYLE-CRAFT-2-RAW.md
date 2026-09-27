Title: Craft-and-care tree-style restyle — confirmation review 2
Verdict: REVISE
Reviewed: NEW-*.md vs OLD-*.md in review-craft2/, against REVIEW-1-RAW.md
Reviewer: independent fresh-context agent

**Scope and method**

- I read all nine NEW files and all nine OLD files in full. I edited nothing.
- **Invariants re-run this session:**
  - Line-1 banner: identical in 9/9 pairs.
  - Heading lines (`^#`): identical and in the same order in 9/9 pairs.
  - CC-REV-8, from `## CC-REV-8` to the end of the file: byte-identical (`diff` empty).
- **Identifier sweep:**
  - Method: a Python `re` sweep outside Mermaid fences, with whitespace normalized.
  - Coverage: CC-*, VIS-n, SEC-n, SDR-n/§n, RFC n and RFCn-n(x), FD-n, E-codes, P-n, code spans, `.md`/`.yaml` names and `[Observed`/`[Inferred`/`[Unknown` labels.
  - Result: 395 OLD occurrences, and 0 missing from NEW in any file.
  - NEW extras are all in openings: README `th-engineering` ×2, engineering-bar VIS-1 ×1, performance `[Unknown` ×1, security SEC-1/4/5 ×1 each.
- **Violation form:** every `*Violation:*` line in NEW is a nested bullet. The one exception is CC-REV-8, which is deliberately unchanged. Per-file counts match OLD, except review-and-documentation, which is 7 bullets plus 1 paragraph against OLD's 8.

## A. Review 1 findings

| Item | Status | Current text (NEW) |
|---|---|---|
| M1 | RESOLVED | provenance L5–8: "every run leaves captured evidence, only raw transcripts and verbose logs may expire under a declared retention policy, and execution reports are rendered without manufacturing green." |
| M2 | RESOLVED | review L73–76: "…in the same logical change; if doctrine would be invalidated, the change instead stops, routes to the owner, and does not merge while the contradiction is open." |
| M3 | RESOLVED | testing L108: "Each failure carries a recorded disposition naming a cause outside the code under test, confirmed by the reviewer (or the owner where no reviewer exists)?" L107: "Not blocked by retries<br/>(CC-TEST-2 still applies)" |
| M4 | RESOLVED | perf L6–7: "anything a viewer could plausibly read as data either is data or is identifiable as decoration"; L91: "**Any element a viewer could plausibly read as data**" |
| M5 | RESOLVED | perf L49–51: "carries a retained measurement artifact with its conditions, or it is labeled [Unknown]." |
| 1 | RESOLVED | obs L116–120: the [Inferred — … this cluster's addition.] label now ends the CC-OBS-6 opening paragraph. |
| 2 | RESOLVED | security L30–31: "**from their first commit** (a Syzygy addition)." |
| 3 | RESOLVED | provenance L47–48: "produces a structured run summary [Observed — FD-020 E6-b: …], and compaction and retention preserve a closed set" |
| 4 | SKIPPED | Review 1 recorded this as a note only and requested no change. obs L19–22 still carries [Observed — VIS-7; architecture.md temporal model] on the opening. Acceptable. |
| 5 | RESOLVED | perf L20–22: "its only legal currency is declared scope [Observed — vision.md, Performance]." |
| 6 | RESOLVED | testing L53–55: "*(Amended 2026-08-02, … The rest of this bullet, including its sub-bullets, is the amended text.)*". The marker's scope matches OLD's parenthetical, which runs from "this emitter-distinct requirement" through the route-3/4 text to "remains a report fact under every route". |
| 7 | RESOLVED | testing L78: "run at least twice" |
| 8 | RESOLVED | testing L138: "Suites that feed alignment/convergence claims" |
| 9 | RESOLVED | testing L45: "**Captured by an observer distinct from the emitter.**" |
| 10 | RESOLVED | provenance L73–75: "nothing in the preserved set may require a transcript to resolve." |
| 11 | RESOLVED | provenance L117: "**Cost aggregates over partially-instrumented runs**" |
| 12 | RESOLVED | provenance L13: the dashed edge is removed. The T node now reads "nothing in the preserved set may require a transcript to resolve". |
| 13 | RESOLVED | interfaces L25: `C["Any candidate dependency<br/>(experimental or not)"] -->|"recorded promotion decision…"| S` |
| 14 | RESOLVED | perf L69–72: "declares its source, units/scale, legend, Unknown behavior, and freshness." / "**Encodings include:**" |
| 15 | RESOLVED | security L108: "repository observation" |
| 16 | RESOLVED | review L80: "Does it invalidate doctrine text?" |
| 17 | RESOLVED | README L5–6: "standards that constrain any future Syzygy implementation"; L104: "Read in this order."; L69–70: "re-pinned 2026-08-06 to commit `f4cf1c7`, and a re-check found no override conflicts." |
| 18 | RESOLVED | obs L5–8: "…its failures leave labelled, durable traces, re-running it is safe, and…" |
| 19 | RESOLVED | review L5–7: the opening uses OLD's wording ("single truthful authority"), and the duplicate "additions" bullet is gone. |
| 20 | RESOLVED | security L86: "Every Syzygy write into a governed repository follows SEC-4." The engineering consequence now appears only in its bullet. |
| 21 | PARTIAL | eng-bar L121–126: "Seven floors bound every change: an implementing agent may strengthen them but never lower them." The first bullet repeats this with more detail ("may **strengthen** … never weaken, waive, special-case, or 'temporarily' bypass"). The duplication is reduced, not gone. This is a note, not a meaning change. |
| 22 | SKIPPED | perf L15–16 and L63–65 keep their section openings. **The skip is acceptable:** CC-REV-8 requires "each section opens with its conclusion", and `## Performance` and `## Visual discipline` are sections. The retained Performance opening does misstate CC-PERF-3, however; see N1. |
| 23 | RESOLVED | perf L176: "Correction (review 8): an earlier two-input wording omitted the **baseline**…" |
| 24 | RESOLVED | security L78–79: "'Run the project's own test command to get better evidence' is exactly the tempting violation." |
| 25 | RESOLVED | Every Violation line is a nested bullet, apart from CC-REV-8 (deliberately unchanged). The CC-BAR-1 re-check record is also a bullet, so the form is consistent. |
| 26 | RESOLVED | The CC-SEC-5 diagram (security L106–111) and the CC-DEP-1 diagram (interfaces L22–27) now sit directly after their section openings. |

## B. Repaired and moved passages: new drift

**Material**

**N1. NEW-performance-and-visual-discipline.md, `## Performance` section opening (L15–16). It repeats the M5 drift one level up.**

- NEW: "Performance spends only declared scope, treats caches as sacrificial, and **backs every claim with a measurement**."
- CC-PERF-3 body (L49–51 and L55–56): "a retained measurement artifact with its conditions, **or the claim is labeled [Unknown]**."
- The opening drops the [Unknown] alternative, which changes the answer. A reader who stops here would treat an unmeasured performance claim as forbidden, when the rule permits it if labelled [Unknown].
- It also drops "with its conditions", the same omission M5 was raised for.
- It says "every claim" where the rule covers performance claims only.
- CC-REV-8 applies: "A caveat that changes the answer belongs in the parent." This passage stayed in NEW because of the item-22 skip, so it falls in scope here.
- Fix: "…treats caches as sacrificial, and backs every performance claim with a retained measurement artifact and its conditions, or labels it [Unknown]."

**Minor (notes)**

- **N2. Provenance, CC-PROV-3 (L73–75 vs L81–82).** The item-10 repair put the exact sentence "nothing in the preserved set may require a transcript to resolve" in both the opening and the "one-way" bullet. The meaning is correct; the duplication is a concision regression. Consider trimming the bullet to "The dependency is one-way:" plus its expiry child.
- **N3. Provenance, file diagram (L12–13).** P and T are now two sibling outputs with no edge between them. This asserts nothing beyond the text. Correct.
- **N4. The CC-DEP-1 diagram after the repair (L22–27) matches the text:** unpromoted experimental dependencies are pruned on the declared cadence, any candidate needs a recorded, non-author-reviewed promotion, and rent-delinquent promoted dependencies are pruned. It omits seam-wrapping, which is an omission, not an assertion. Correct.
- **N5. The CC-REV-2 and CC-TEST-4 diagrams after the repair** now match their text. A change that invalidates doctrine and other artifacts routes to "Stop", as OLD requires.
- **N6. Moved labels (items 1, 3, 5, 6):** each label now covers the same span it covered in OLD, or its parent. No label was separated from its claim.

## C. Spot-check of the rest (notes only)

- **N7. `## Visual discipline` opening (perf L63–65):** "Every encoding declares what it means…" is coarser than CC-VIZ-1's five declarations, and "Unknowns stay visible" omits the aggregate-disclosure obligation. Both are coarsening rather than a changed answer. Consider "Every encoding declares its source, units, legend, Unknown behavior and freshness…", to match the item-14 repair one level down.
- **N8. README, Citation convention opening (L88–89):** "every clause binds equally whatever its epistemic label". The body qualifies this with "On owner approval". The opening's point is equality across labels, and the banner states approval, so this is a note.
- **N9. CC-REV-6 opening (review L163–164):** "every revise-severity finding is fixed or explicitly overruled". It omits "with recorded rationale by the accountable authority", which appears in the bullet at L167–169. Review 1 passed this passage and no repair touched it. Consider carrying "by the accountable authority" into the opening.
- **N10. CC-TEST-5 opening (testing L138):** "declare their scope" omits "and coverage", which is in the bullet. This is coarsening only.
- No other drift was found in the openings of CC-BAR-*, CC-DEP-*, CC-OBS-*, CC-SEC-*, CC-PROV-* or CC-REV-1/3/4/5/7. The CC-VIZ-5 and CC-DEP-4 diagrams still match their text.

## Summary

- All five review-1 material items are resolved.
- 23 of the 26 minor items are resolved. Item 21 is partial, and items 4 and 22 are skipped acceptably.
- One new material item, N1, stands: the retained `## Performance` section opening drops CC-PERF-3's [Unknown] alternative and "with its conditions".
- N2–N10 are notes.
- The verdict is REVISE on N1 alone. Its one-sentence fix is given above.
