Title: Default-path docs and topology tree-style restyle — review 1
Verdict: REVISE
Reviewed: NEW-* vs OLD-* in review-docs/
Reviewer: independent fresh-context agent

**How I checked** [Observed]
- I read all 20 pairs in full.
- Scripted comparisons:
  - Every table row in every pair: identical in both versions.
  - Every OLD Mermaid block: still present, byte-identical, in NEW. That covers all eight topology views and the root README core-loop diagram.
  - Link targets, identifiers, dates, code spans, epistemic labels and content words: diffed per file.
  - I recomputed sha256 for every topology member file against both manifests. Each manifest matches its own member set.
- No link target was lost; the only one added is `#start-here`.
- No identifier was lost.
- One date pair (2026-08-17, 2026-09-01) moved out of root README source-map item 5. It still appears in that page's authority table.

## Material findings

**M1. `openspec/README.md` — NEW edits text the owner approved, and the banner still claims that approval.**
- OLD and NEW both keep: "**The owner approved this text 2026-09-08**; the reservation is discharged and this banner is not edited further to say so again."
- NEW then adds an opening above the banner ("Three changes live under `changes/`, each in force by a named owner act; … Read the act, never a proposal's head.") and rewrites three sections into bullets.
- A reader of NEW believes the owner approved these bytes. They did not. The file is also in the governed plane (`openspec/**`).
- Fix: revert this file to the OLD bytes, or get fresh owner review before landing. The banner cannot be amended to say so.

**M2. Topology bundle — the manifest's history line is now false, and every member banner claims reviews of bytes no review saw.**
- The NEW manifest differs only in digest lines, as the brief required. That leaves its Date line claiming the last regeneration was 2026-08-10: "member digests regenerated 2026-08-05 (P-6 second leg) and again 2026-08-10 after the second retired-acceptance-phrase correction in README.md". NEW regenerates them again with no dated entry.
- All nine NEW members keep "Reviewed fresh-context (reviews 5–7, dispositions recorded)" over changed bytes.
- The manifest digest is the argument of `ACCEPT TOPOLOGY: <digest>` (act 3). Changing it retires any confirmation bound to the prior digest.
- [Unknown] Whether the acceptance record or a packet quotes the prior manifest digest. That is outside this directory.
- Fix: either exclude the bundle from the restyle (revert all ten files), or treat the change as a semantic delta. The second route needs a dated regeneration clause in the manifest, which conflicts with the brief's "only digest lines" rule, plus a new review. The owner or lead must choose.

**M3. Root `README.md` "Why it exists" — the new diagram leaves execution state out of the difference and draws an edge for a negation.**
- OLD: keep three kinds of state distinct "and make the difference between them legible".
- NEW diagram: only `D --> G` and `O --> G`, plus `E -.->|never proof intent is satisfied| D`.
- A diagram reader concludes the difference is computed from desired and observed state only. The negated arrow also reads as a relationship from execution state to desired state.
- Fix: add `E --> G`. Replace the negated edge with a note on `E`, or drop it.

**M4. `PROCESS-GLOSSARY.md` lifecycle — the new diagram contradicts the text's ordering and adds a precondition.**
- Text (OLD and NEW): the four words "describe **increasing force**", with recorded listed after accepted.
- The diagram:
  - draws `recorded` as a detached node outside that order;
  - makes `candidate → confirmed (reviewer returns CONFIRM) → accepted (owner performs an act)` the only path, implying CONFIRM is a prerequisite of acceptance. The text never states that.
- Fix: draw all four on one increasing-force axis without transition semantics, or drop the diagram.

**M5. Provenance claims dropped or re-dated.**
- Root README:
  - OLD "*(added 2026-08-13, RD-50 f10 — both were unmentioned by this page)*" becomes NEW "(source: RD-50 f10, 2026-08-13)". The date now reads as the finding's date rather than the date this paragraph was added, and "both were unmentioned by this page" is lost.
  - The superseded paragraph drops "It stood because this page restated a status it does not own instead of citing the page that does."
- `SECURITY.md` superseded paragraph drops "and the page was not restated for either". OLD's "not left to age behind its own confidence" is shortened.
- Fix: restore the sentences verbatim, and restore "added 2026-08-13".

**M6. `docs/THREE-SURFACE-POC.md` "Evidence and re-observation" — the new opening claims a freshness value the body disclaims.**
- NEW: "Each evaluation discloses what revision it observed and how current that is".
- Body (OLD and NEW): "Currency bounds remain empty until their separately gated owner act … the probe is a disclosure, not a project claim or freshness value."
- Fix: "Each evaluation discloses its pinned revision, observation instant and a currency probe against the current Git head (a disclosure, not a freshness value); a new evaluation happens only on an explicit re-observe request."

## Minor findings

**Root `README.md`**
- The "Why it exists" opening "Agent-fleet work outruns any coherent account of intent" drops OLD's "too often". Fix: "too often outruns".
- The "What is not implemented" opening "every positive relationship stays Unknown" broadens OLD's enumerated list: alignment, convergence, regeneration, deployment health, conformance, release. Fix: "the listed relationships".
- The "Core loop" opening "Intent is observed" misreads the diagram: code, tests, CI and runtime are what is observed.
- "Read these in order; for an unfamiliar word, pick the glossary…" sits above the glossary table, so "these" first attaches to the table rather than the numbered list.
- Item 5 now defers its acceptance and amendment dates to "the table above". Acceptable, but noted.

**`PROCESS-GLOSSARY.md`**
- The Review-vocabulary opening "Reviews run in fresh context…" asserts as practice what OLD only defines as a term.

**`docs/README.md`**
- "None of them is permission to do the work it describes" extends OLD's claim about plans to every home, including reviews and evidence.
- The `evidence/` opening "`PWB-IMPLEMENTATION-PLAN.md` is the route in" omits the three reviewer-produced files that route through `reviews/`.
- PWB chain diagram:
  - it drops the order ("then", "later");
  - `TR -- amends the two instruments they put in force --> EF` points at the acts rather than the instruments;
  - it sits after the third bullet, away from the chain bullet.

**`docs/THREE-SURFACE-POC.md`**
- The restart diagram omits two refusals: the simultaneous restart attempt and the stale restart lock. Prose keeps both.
- "Cross-surface links. They connect:" mixes the connection list with link properties in one bullet list.

**`docs/polaris-generation/README.md`**
- "a beautiful page for Butlers is only the proving case": OLD says "a proving case".
- "The generation machinery runs end to end" overstates a synthetic run. Suggested: "runs its six stages through explicit adapters over synthetic input".
- The Start-here opening lists "secure consent" unconditionally. OLD step 4 applies only "Before any real provider dispatch".
- Run-contract diagram:
  - `Edit -- frozen bundle --> Verify` asserts that Edit produces the frozen bundle; the table gives Edit's output as a revision plus change list;
  - the `Repair --> Verify` loop is inferred from "Revalidate".

**`ARTIFACTS-AND-TOOLS.md`**
- "Every stage runs inside an identified, bounded request" states as fact what the page calls a candidate convention. Suggested: "Each stage is specified to run…".
- "cold-start operator" was dropped.

**`packages/polaris-generation-core/README.md`**
- The top bullet "ending at `awaiting-rendered-review`" ignores stopped runs. Suggested: "a successful run ends at…".
- Note, an improvement: moving the SEC-2 paragraph before the command makes OLD's dangling "the synthetic command below" correct.

**`SECURITY.md`**
- OLD's "(the documentation checks below)" loses "below". OLD's forward reference had no target, so this is harmless.

**Topology views**

| File | Finding |
|---|---|
| `README.md` | Drops "drawn while the whole RFC set was still in flight". |
| `01` | "Three SEC boundaries enclose Syzygy" conflicts with the unchanged diagram: SEC-2 encloses owner infrastructure and SEC-4 encloses governed projects. "Who consumes it: the single owner" narrows the owner, who also adopts, grants and triggers. |
| `02` | The opening "All of this is target" sits over Observed and Inferred bullets. |
| `03` | The opening drops "at one evaluation" from the one-drawer rule. |
| `04` | "each written under one of four write-authority classes" conflicts with the table's "Typical" column and its dual entries. The opening names the reserved `declarations/` category without its OPEN status. The no-second-store opening drops "mutable" ("every externally owned field"). The two new diagrams are faithful. |
| `05` | "each failure has a defined rendering" broadens OLD's enumerated six. |
| `06` | "Five human gates" is a new count, and the unchanged diagram shows four hexagons. "split between V0 and V1" overstates partial target lists. "separates planned work from scheduled work" is inferred. |
| `07` | "unsafe configurations fail closed" broadens "an unauthenticated network-exposed configuration". |
| `08` | "mediates one external authority" is loose next to inference providers, whose authority is "None over truth". |

## No drift found

- `openspec/specs/README.md`: meaning preserved. It is still governed-plane bytes, so it needs the same approval check as M1.
- Every table row in all 20 pairs is byte-identical.
- Every pre-existing Mermaid block is unchanged: topology 01–08 and the root README core loop.
- `BUNDLE-MANIFEST.md`: only digest lines differ, and each NEW digest matches its NEW member file (subject to M2).
- `SECURITY.md`: the SEC-1…SEC-5 table and the "does not claim" section are unchanged.
- `docs/README.md`: the review-campaign table, the partition sentence, the superpowers table and the maintenance contract are preserved.
- No link target, identifier or epistemic label was lost in any pair.
