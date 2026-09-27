Title: Craft-and-care tree-style restyle — review 1
Verdict: REVISE
Reviewed: NEW-*.md vs OLD-*.md in review-craft/
Reviewer: independent fresh-context agent

**Scope and method**

- I read all nine OLD/NEW pairs in full and edited nothing.
- **Headings:** every `#`/`##`/`###` heading in OLD is present in NEW, byte-identical and in the same order, in all 9 pairs (a scripted comparison of heading lines).
- **Identifiers and links:** I extracted identifiers per section, outside Mermaid fences, covering CC-*, VIS-n, SEC-n, SDR-n, SDR §n, RFC n and RFCn-n(x), FD-n, E-codes, P-n, `.md`/`.yaml` paths, Markdown links, code spans and `[Observed/[Inferred/[Unknown` labels.
  - That sweep checked 349 OLD occurrences. None is missing from its own section in NEW.
  - NEW has a few extra occurrences, which come from the new openings.
- **Banner:** line 1 is identical in all 9 pairs.
- **CC-REV-8:** the section from `## CC-REV-8` to the end of the file is byte-identical, confirmed with `diff`.
- **Dropped words:** I compared word counts per section to find words that disappeared. Each case was checked by hand; the ones that matter are listed below.

## Material findings

**M1. NEW-agent-provenance-and-execution-evidence.md, file opening: it widens what may expire and drops the retention-policy condition.**
- OLD (CC-PROV-3): "Raw transcripts and verbose logs may expire under a declared retention policy (SDR-10)… Prompt **hashes** are retained, prompt bodies are not".
- NEW opening: "every run leaves captured evidence, only bulk material may expire".
- The problem: "bulk material" is undefined and wider than "raw transcripts and verbose logs". The "under a declared retention policy" condition is gone. A reader who stops here could let any large artifact expire, with no declared policy.
- Fix: "every run leaves captured evidence, only raw transcripts and verbose logs may expire under a declared retention policy, and execution reports are rendered without manufacturing green."

**M2. NEW-review-and-documentation.md, CC-REV-2 opening: it implies the rest of the change goes ahead.**
- OLD: "When a change would invalidate doctrine text, the change stops and routes to the owner as a contradiction — it does not edit doctrine in-change, and it does not merge while the contradiction is open."
- NEW opening: "…updates **every** invalidated authoritative artifact in the same logical change; doctrine alone is routed to the owner instead."
- The problem: "doctrine alone… instead" reads as "update everything else in-change and send only the doctrine part to the owner". In OLD the whole change stops and cannot merge. Under CC-REV-8, a caveat that changes the answer belongs in the parent.
- Fix: "…in the same logical change; if doctrine would be invalidated, the change instead stops, routes to the owner, and does not merge while the contradiction is open."

**M3. NEW-testing-and-verification.md, CC-TEST-4 diagram: it asserts more than the text.**
- OLD: "a recorded disposition naming a cause outside the code under test, confirmed by the change's reviewer (or the owner where no reviewer exists)".
- NEW diagram node D: "Each failure carries a recorded infrastructure disposition, confirmed by the reviewer (or owner)?"
- The problem: the diagram offers owner confirmation as an unconditional alternative to the reviewer, and drops "naming a cause outside the code under test". The CC-REV-8 rule the restyle applies says "A diagram asserts nothing the text does not."
- Also: the "no → May satisfy a status claim" edge can read as sufficient on its own, though CC-TEST-2's capture requirements still apply. This part is minor.
- Fix: relabel D to "Each failure carries a recorded disposition naming a cause outside the code under test, confirmed by the reviewer (or the owner where no reviewer exists)?"
  - Optionally relabel P to "Not blocked by retries (CC-TEST-2 still applies)".

**M4. NEW-performance-and-visual-discipline.md, file opening: it drops "plausibly" and so widens CC-VIZ-2.**
- OLD (CC-VIZ-2): "Any element a viewer could **plausibly** read as data must either be data… or be identifiable as decoration."
- NEW opening: "anything a viewer could read as data either is data or is identifiable as decoration."
- The problem: without "plausibly", the file-level summary states the rule more broadly than its body. The body bullet also changes "Any element" to "Anything", which is minor on its own.
- Fix: "…and anything a viewer could plausibly read as data either is data or is identifiable as decoration." In CC-VIZ-2, restore "Any element a viewer could plausibly read as data".

**M5. NEW-performance-and-visual-discipline.md, CC-PERF-3 opening: it drops a required element of the evidence.**
- OLD: "a retained measurement artifact **with its conditions**, or the claim is labeled [Unknown]."
- NEW opening: "carries a retained measurement, or it is labeled [Unknown]."
- The problem: a reader who stops at the opening would accept a measurement recorded without its conditions. That is narrower than the rule body.
- Fix: "…carries a retained measurement artifact with its conditions, or it is labeled [Unknown]."

## Minor findings

**Label and marker scope** (the label or marker survives but covers a different span; no rule changes):

1. **Observability, CC-OBS-6.** OLD's closing "[Inferred — … extending it to self-status is this cluster's addition.]" covers the whole self-status rule. NEW attaches it only to the Health/status bullet, so the main claim in the opening ("Operational claims about Syzygy itself… follow the same rules…") now carries no label.
   - Fix: move the [Inferred …] label to the end of the opening sentence, or repeat it there.
2. **Security, CC-SEC-1.** OLD attaches "(a Syzygy addition: …)" directly to "from their first commit". NEW's opening states "from their first commit" with no marker and puts the marker in a child bullet. The file's own preamble requires such a sentence to say it is an addition.
   - Fix: "…**from their first commit** (a Syzygy addition)."
3. **Agent provenance, CC-PROV-2.** OLD attaches [Observed — FD-020 E6-b…] to "produces a structured run summary". NEW places it after "and compaction and retention preserve a closed set of provenance", so FD-020 E6-b now seems to source the closed-set claim, which OLD grounds in SDR-10.
   - Fix: put the label right after "run summary".
4. **Observability, CC-OBS-1.** [Observed — VIS-7; architecture.md temporal model] moved from the identity-test sentence, which includes "extending that exclusion is a doctrine amendment", to the opening. The span is roughly the same; this is noted only.
5. **Performance, CC-PERF-1.** [Observed — vision.md, Performance] now sits on the "What it may never do" bullet only. In OLD it closed the whole currency sentence. Consider placing it on the opening.
6. **Testing, CC-TEST-2.** OLD's italic amendment parenthetical enclosed the whole route-1/2 and route-3/4 text. NEW closes the parenthetical after "…amendment.)", so the route text reads as ordinary body text. This affects provenance marking only.
   - Fix: note "(the following text is the 2026-08-02 amendment)", or keep the route text inside the amendment marker.

**Openings and diagrams slightly off the body** (no rule changes):

7. **Testing, CC-TEST-3.** The opening says "run twice", but the body says "at least twice".
   - Fix: "run at least twice".
8. **Testing, CC-TEST-5.** The opening says "Suites that feed alignment claims", but the body says "alignment/convergence claims".
   - Fix: say "alignment/convergence".
9. **Testing, CC-TEST-2.** The bullet label "The artifact must be captured by someone else" is looser than the body's "observer distinct from the emitter", since an observer may be a system.
   - Fix: "Captured by an observer distinct from the emitter."
10. **Agent provenance, CC-PROV-3.** The opening "nothing in the preserved set may depend on them" extends the one-way rule to verbose logs. OLD states it for transcripts only, though OLD also calls both "non-load-bearing". This is stricter, not looser.
    - Fix: "nothing in the preserved set may require a transcript to resolve."
11. **Agent provenance, CC-PROV-5.** "Cost aggregates" became "Aggregates over partially-instrumented runs". The word "cost" was dropped; context covers it.
    - Fix: restore "Cost aggregates".
12. **Agent provenance, file-level diagram.** The dashed edge P -.-> T labelled "never requires to resolve" draws a dependency arrow to express a *non*-dependency, and there is no legend.
    - Fix: remove the edge and state the rule in the T node ("nothing in the preserved set may require these to resolve"), or add a legend line.
13. **Interfaces, CC-DEP-1 diagram.** The only way into "Shipped or authoritative path" is from experimental scope, which implies every dependency must first be experimental. OLD requires only a recorded promotion decision.
    - Fix: add a note to that effect, or draw a separate "candidate dependency" source node.
14. **Performance, CC-VIZ-1.**
    - The opening "declares everything a viewer needs to read it" is vague and could be read as more than the five listed items. Fix: "declares its source, units/scale, legend, Unknown behavior, and freshness."
    - The label "Covered encodings:" makes OLD's parenthetical examples read as an exhaustive list. Fix: "Encodings include:".
15. **Security, CC-SEC-5 diagram.** The node says "observation"; the text says "repository observation".
16. **Review, CC-REV-2 diagram.** "Is it doctrine?" is ambiguous for a change that invalidates doctrine *and* other artifacts.
    - Fix: "Does it invalidate doctrine text?"
17. **README.**
    - The opening "standards every Syzygy implementation must meet" reads as binding now, while the banner defers binding force to the acceptance act. Consider "must meet once in force" or "constrain any future implementation".
    - "Read the engineering bar first, then the files it leans on" asserts a relationship OLD does not state. Fix: "Read in this order."
    - In "The adopted baseline is pinned", "re-pinned … after a re-check found no override conflicts" asserts an order OLD only implies. Acceptable, but "and a re-check found…" is safer.
18. **Observability, file opening.** It omits CC-OBS-5 (idempotence), so it does not summarize the whole file as CC-REV-8 asks. Add "and re-running is safe".

**Concision and clarity regressions:**

19. **Review, file preamble.** The "Syzygy's additions" bullet repeats the opening almost word for word. "Readable authority" is new wording in the opening.
20. **Security, CC-SEC-4.** The opening's second clause duplicates the "Engineering consequence" bullet verbatim.
21. **Engineering bar, CC-BAR-5.** The opening and the three may/never/who bullets say the same thing twice.
22. **Performance.** The new `## Performance` and `## Visual discipline` section openings repeat the file opening and the rule headings.
23. **Performance, CC-VIZ-5.** "Source:" is used as the label for a correction note ("Source: corrected after review 8"). Fix: "Correction (review 8):".
24. **Security, CC-SEC-3.** "The tempting violation: 'Run the project's own test command…' is exactly it" is awkward. Fix: "'Run the project's own test command to get better evidence' is exactly the tempting violation."
25. **Placement of `*Violation:*` lines is inconsistent.** They are nested bullets in CC-BAR-1, CC-TEST-1…4, CC-PERF-1…3, CC-VIZ-1…4 and CC-SEC-1…6, but standalone paragraphs elsewhere. The CC-BAR-1 re-check record is also a bullet. Pick one form.
26. **Diagram placement.** The CC-SEC-5 diagram sits after the Violation line, and the CC-DEP-1 diagram interrupts the bullet list. Place each diagram right after its section's opening.

**Improvement noted:** the CC-DEP-5 violation's code span `status: unknown (no current evidence)` was wrapped across a line break in OLD and is on one line in NEW.

## No drift found

- **NEW-README.md:** no material drift. Minor items 17 and 23-adjacent only. The precedence diagram matches the text: doctrine prevails over the SDRs within tier 1, which prevails over the cluster, which prevails over the bar.
- **NEW-engineering-bar.md:** no drift found. Minor items 21 and 25 only. CC-BAR-3's bullet label "No confident state over Unknown (VIS-1)" is narrower than its bullet, which also covers content-vs-presentation; this is a note only.
- **NEW-interfaces-and-dependencies.md:** no material drift. Minor items 13 and 26. The CC-DEP-4 diagram matches the text.
- **NEW-observability-and-operations.md:** no material drift. Minor items 1, 4 and 18.
- **NEW-security-and-secrets.md:** no material drift. Minor items 2, 15, 20 and 24.
- **NEW-testing-and-verification.md:** material item M3. Minor items 6–9.
- **NEW-review-and-documentation.md:** material item M2. Minor items 16 and 19. CC-REV-8 is unchanged.
- **NEW-performance-and-visual-discipline.md:** material items M4 and M5. Minor items 5, 14, 22 and 23. The CC-VIZ-5 diagram matches the text.
- **NEW-agent-provenance-and-execution-evidence.md:** material item M1. Minor items 3 and 10–12. The CC-PROV-6 diagram matches the text.
