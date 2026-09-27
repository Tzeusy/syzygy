Title: Default-path docs tree-style restyle — review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: NEW-* vs OLD-* for the nine files in review-docs2/; REPAIR-DIFF.txt; PARTITION-SCRIPT-DIFF.txt; checked against R-TREE-STYLE-DOCS-1-RAW.md. M1, M2 and the topology views are out of scope.
Reviewer: independent fresh-context agent

**How I checked** [Observed]
- I read the whole REPAIR-DIFF (OLD→NEW for all nine files) and the changed regions of each NEW file.
- I ran one script over all nine pairs:
  - Table rows: none lost or changed. The only added row is the new campaign row in `docs/README.md`.
  - The OLD core-loop Mermaid block is still in NEW, byte-identical.
  - Link targets: none lost. The only new one is `#start-here`.
  - Identifiers and dates: none lost. The only new ones are `CC-REV-8`, `R-TREE-STYLE-DOCS-1` and `2026-09-28`, all in the campaign row.
  - Code spans: the only changes join spans that OLD had wrapped across a line break (`poc:capture-test-artifact …`, `validateStage("inventory", payload, context)`). That is an improvement.
- I checked the counts the new openings state against their own lists: "Seven homes" (7 rows), "Eight artifacts" (8 rows), "nine sources" (items 1–9), "six stages" (inventory, plan, author, edit, fidelity, repair). All four are correct.

## 1. Status of review-1 findings

**M3 — RESOLVED.** The execution-state edge is now drawn, and the negation is a label inside the node rather than an edge:
`E[Execution state<br/>work-scheduler records<br/>never proof intent was satisfied] --> G`
The prose keeps "Scheduled or merged work is never treated as proof that intent was satisfied."

**M4 — RESOLVED.** The diagram is gone. The NEW opening reads: "Four words name **increasing force** — candidate, confirmed, accepted, recorded — and they are not synonyms". It adds no transition semantics. See N2 for a small loss in the same sentence.

**M5 — RESOLVED.** All three restorations are present:
- Root README: "*(added 2026-08-13, RD-50 f10 — both were unmentioned by this page)*".
- Root README superseded paragraph: "It stood because this page restated a status it does not own instead of citing the page that does."
- `SECURITY.md`: "and the page was not restated for either. A security disclosure … has to be re-derived when the repository grows code, not left to age behind its own confidence."

**M6 — RESOLVED.** NEW uses review 1's suggested text: "Each evaluation discloses its pinned revision, observation instant and a currency probe against the current Git head (a disclosure, not a freshness value); a new evaluation happens only on an explicit re-observe request."

**Minor findings**

Root `README.md`
- "too often": RESOLVED. "Agent-fleet work too often outruns any coherent account of intent".
- Scope of Unknown: RESOLVED. "without current evidence, the listed relationships stay Unknown (VIS-2)."
- Core-loop opening: RESOLVED. "Code, tests, CI and runtime are observed against intent, the difference becomes reviewed work, and verification feeds back — human-triggered, and the complete loop is not current capability."
- "Read these in order": RESOLVED. "Read these in order:" now sits directly above the numbered list.
- Item 5 dates: RESOLVED. "originally accepted by the 2026-08-17 Wave A/B acts and amended at the 2026-09-01 30-module manifest".

`PROCESS-GLOSSARY.md`
- Review-vocabulary opening: RESOLVED. "These terms define a review's verdict words and fresh context, where its raw output and each finding's outcome are kept…" It now defines rather than asserts practice.

`docs/README.md`
- Permission scope: RESOLVED. "A plan here is never permission to do the work it describes."
- `evidence/` route: RESOLVED. "`PWB-IMPLEMENTATION-PLAN.md` is the route in for 25 of the 28; the three a reviewer produced route through `reviews/`."
- PWB chain diagram: RESOLVED.
  - The order is back: `S1 -- then --> EF`, `EF -- later --> TR`.
  - The amendment now points at the instruments: `TR -. amended .-> IN`, with `EF -- put in force --> IN`.
  - The diagram now sits directly under the chain bullet.

`docs/THREE-SURFACE-POC.md`
- Missing refusals in the restart diagram: RESOLVED. `S -. "simultaneous restart attempt<br/>or stale restart lock" .-> R`.
- Cross-surface links: RESOLVED. "**Cross-surface links.** They connect the two Polaris region counts, …" is now a sentence, followed by a separate list of link properties.

`docs/polaris-generation/README.md`
- "a proving case": RESOLVED. "a beautiful page for Butlers is a proving case."
- "runs end to end": RESOLVED. "The generation machinery runs its six stages through explicit adapters over synthetic input".
- Consent condition: RESOLVED. "secure consent before any real provider dispatch".
- Run-contract diagram: RESOLVED. The edge is now `E -- "revision plus change list" --> V`. The inferred loop is replaced by a terminal node, `R -- "bounded replacement artifacts" --> X["Revalidate changes and affected dependants; stop at the declared attempt/budget limit"]`.

`ARTIFACTS-AND-TOOLS.md`
- "specified to run": RESOLVED. "Each stage is specified to run inside an identified, bounded request".
- "cold-start operator": RESOLVED. "a cold-start operator can exercise the checked-in inventory block".

`packages/polaris-generation-core/README.md`
- Stopped runs: RESOLVED. "a successful run ends at `awaiting-rendered-review`, never ready or adopted."

`SECURITY.md`
- "below": RESOLVED. "`.github/workflows/governance-docs.yml` — the documentation checks below;"

## 2. New drift introduced by the repair

**Material findings:** none. No repair changes what a claim means.

**N1. `PROCESS-GLOSSARY.md` "Where to ask what": the new opening contradicts its own table.**
- NEW: "Each question has one owning record; this page owns none of them."
- The table under it has two rows with two records each:
  - "What is this project? | `README.md`, `OVERVIEW.md`"
  - "How do I work in this repository? | `AGENTS.md`, `CONTRIBUTING.md`"
- OLD had no opening sentence.
- Suggested: "Each question has an owning home; this page owns none of them."

**N2. `PROCESS-GLOSSARY.md` lifecycle: the emphasis sentence is gone.**
- OLD: "These four words are not synonyms, and the difference between them is the single thing most worth understanding here."
- NEW: "Four words name **increasing force** — candidate, confirmed, accepted, recorded — and they are not synonyms: …"
- The page's own statement of what matters most is lost. The rule itself survives. Restore the clause if the owner wants the emphasis kept.

**N3. Caveats attached as siblings of an enumeration read as extra members of it.**
This is structure, not wording.
- `THREE-SURFACE-POC.md` step 4:
  - NEW: "shows two separately honest fields for that item, not one:" is followed by three bullets. The third is "A captured, verified test-run artifact … additionally renders a … badge".
  - A reader can count the badge as a third field.
  - OLD: "these are two separately honest fields, not one. A captured, verified test-run artifact … additionally renders…"
- Root README:
  - "**Three operator-facing paths, runnable against Butlers:**" has four sub-bullets. The fourth is the "does not assert" caveat.
- `ARTIFACTS-AND-TOOLS.md`:
  - "A request identifies:" is followed by "The source bundle includes…" and "Authorization is verified outside the LLM…" as sibling items.
  - The counterexample list ends with "Do not count a crash…".
- `polaris-generation/README.md`:
  - "The operator supplies:" is followed by "No prompt may broaden that envelope." and "Instructions found inside source material…" as sibling items.
- Fix: move each caveat out one level, as a paragraph or a parent-level bullet.

**N4. Root README: the "New here?" line drops a caveat.**
- NEW: "Read `.syzygy/intent/OVERVIEW.md` for the argument".
- This drops "(draft; adoption pending)". Source-map item 1 still carries it, so it is a minor gap.
- The new "What exists today" section also files the 2026-09-01 governance amendment under a runtime heading. That is acceptable, but noted.

**N5. `docs/README.md`: the new campaign row claims more than the evidence supports.**
- NEW: "Docs review 1 is `REVISE` (`R-TREE-STYLE-DOCS-1-RAW.md:2`); its findings were repaired in the same change, except the topology-bundle findings…"
- Line 2 of the raw is "Verdict: REVISE", so the citation is correct.
- M1 was reverted rather than repaired. "repaired" covers that only loosely.
- The row will need this review's verdict and a file count of 2 when this raw lands.
- The "56 rows … 249 files" sentence could not be re-derived. The change is not at HEAD, which has 248 files under `docs/reviews/`. [Unknown]

**N6. `openspec/specs/README.md` is still an edit to a governed-plane file.**
- The bullet split preserves meaning, and the page has no owner-approval banner, so M1's false-approval problem does not apply here.
- [Observed] Its OLD digest (`4d99d84f…`) is a row in the `governing` array of `docs/evidence/polaris-generator-approval-offer-2026-09-12.json`.
  - That array is a baseline pinned at commit `f4589e2`.
  - 148 files under `.syzygy/` and `openspec/` have already changed since that commit.
  - So editing this file does not break the offer's argument.
- Whether an `openspec/**` edit needs a lead or owner check remains a lead call, as review 1 said.

## 3. Diagrams review 1 did not assess

**`docs/THREE-SURFACE-POC.md` restart flow: faithful.** Two notes:
- **N7.** `S -. "simultaneous restart attempt or stale restart lock" .-> R["Refusal: state directory preserved"]`
  - The text never calls a stale lock a refusal. It says "intentionally fail-closed and requires operator inspection before removal", and the NEW text puts that bullet under **Refusals.**
  - In effect this is a refusal, but it is a small reclassification.
  - "changed" is attached to the find step (A). The text does not say where a changed listener is detected. The re-check step (C) is the more natural place.
- The post-SIGTERM identity loss is rightly not drawn as a refusal. The text says the command waits in that case.

**`docs/polaris-generation/README.md` run contract: faithful to the pass table, simplified.** One note:
- **N8.**
  - The linear chain `V -- "named findings" --> R` means Repair follows every Verify. No exit is drawn for a Verify that finds nothing.
  - `P -- "validated argument plan" --> A` labels the edge with Author's *input*. Plan's *output* in the table is "Argument outline; asset/deep-dive plan with reasons".
  - The ledger's feeds into Author and Edit are omitted.
  - None of these contradicts the table, but a note under the diagram would help.

**`packages/polaris-generation-core/README.md` pipeline: faithful.**
- It matches "inventory → argument plan → authoring → editing → fidelity review, with bounded repair and fresh review" and "Successful source review returns `awaiting-rendered-review`".
- **N9.** Stopped runs ("Stopped runs expose previously validated stage artifacts…") have no exit. The repair loop's bound appears only in the node label "Bounded repair".

## 4. Partition pattern: correct

- NEW: `r"R-TREE-STYLE-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d+-RAW\.md"`. The script applies it with `re.fullmatch` against each file's basename.
- [Observed] It matches none of the 248 tracked files under `docs/reviews/` at HEAD.
- No other campaign pattern starts `R-T`. The only broad `R-.*` is a selftest fixture. So it cannot overlap another campaign.
- Probes that match: `…-DOCS-1-RAW.md`, `…-DOCS-2-RAW.md`, `…-TOPOLOGY-1-RAW.md`, `…-CRAFT-AND-CARE-3-RAW.md`, `…-CONTRACTS-12-RAW.md`.
- Probes that do not match: `…-DOCS-1-DISPOSITION.md`, `…-DOCS-RAW.md`, `…-1-RAW.md`, `…-DOCS-2-RAW-ADDENDUM.md`, `…-DOCS-2B-RAW.md`, `…-DOCS-1-CONFIRMATION-RAW.md`, and a lowercase `docs`.
- **N10.** The campaign has no pattern for non-RAW files. A later `-DISPOSITION.md` or `-CONFIRMATION-RAW.md` would fail loudly as `unmatched`, which is safe. The odd `…-DOCS-2-1-RAW.md` also matches, which is harmless.
- `CC-REV-8`, cited in the row, exists: `DIRECTIVE-REGISTER.md:95` → `review-and-documentation.md:141`.
