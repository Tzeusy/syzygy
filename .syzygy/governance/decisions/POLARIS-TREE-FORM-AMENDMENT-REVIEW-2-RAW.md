Title: Polaris tree-form amendment — confirmation review 2
Verdict: REVISE
Reviewed: SPEC-DIFF.patch and PACKET.md in review-pg2/, against REVIEW-1-RAW.md
Reviewer: independent fresh-context agent

## A. Status of REVIEW-1 findings

| ID | Status | Current text |
|---|---|---|
| M1 | PARTIAL | Clause: "that diagram is a requested relationship asset with its own identity and requiredness (REQ-polaris-generation-019) and one of the three dispositions above. A reasoned omission is admissible only when the premises do not support the relationship or the prose explains it at least as clearly; missing renderer capability or permission leaves it unresolved." The dispositions, the admissible reasons and the split scenarios are fixed. What is left: requiredness is never stated. See new finding N2. |
| M2 | PARTIAL | Clause: "Where a diagram would explain a structural relationship the account explains — a flow, lifecycle, state machine, boundary, dependency or placement — better than prose". The clause is now conditional and uses CC-REV-8's list. But Scenario *Explained relationship left without a diagram* is unconditional again. See N1. |
| M3 | RESOLVED | "The independent design review, not the authoring stage, enumerates the structural relationships the rendered account explains and judges diagram coverage against that enumeration, never by figure count." The scenario also has "a relationship the authoring stage never listed is still a finding". |
| M4 | PARTIAL | PACKET: "It emits nothing on `/polaris`" and "That question belongs to the Butlers page package". The `/polaris` claim is withdrawn. But the draft preview sits inside the POC app, which PWB-REQ-006 may govern. See N3. |
| M5 | RESOLVED | "Required headings, the altitude order, authority bands and verbatim exact-source text keep their structure; tree form governs the generated account around them". |
| m1 | RESOLVED | Both the clause and Scenario 1 say "opens with its answer in one sentence or one bullet". |
| m2 | PARTIAL | The supported case is now its own scenario. The partly supported case was not given one. Instead "an unsupported edge is omitted with its gap disclosed rather than drawn" moved into the *no-diagram* scenario, whose WHEN ("a relationship… that has no diagram") does not cover a partly drawn diagram. |
| m3 | RESOLVED | "an Inferred edge renders with its Inferred marking in both the diagram and its text equivalent". |
| m4 | RESOLVED | "no script, event-handler attribute, `foreignObject`, or external or unsafe-scheme reference". |
| m5 | RESOLVED | "when no inert renderer is available or rendering fails". |
| m6 | RESOLVED | "A diagram's declarative source SHALL be retained with the asset for review". |
| m7 | RESOLVED | The packet now says "The new clauses add to REQ-004. Where they overlap … they only narrow them". The clause points back ("the support required above") rather than restating. |
| m8 | RESOLVED | The packet cites the command and the population. Figures are verified in section C. |
| m9 | RESOLVED | "Every edge needs a support reference. Its labels must also appear in the section text. That is a necessary check, not a sufficient one." |
| m10 | RESOLVED | Clause: "keeps REQ-polaris-generation-002's connections between motives, promises and capabilities". The packet matches. See m-c for a wording note. |
| m11 | RESOLVED | PACKET: "REQ-012: it still governs inert rendering and diagram text equivalents for every page, including the new diagrams." |
| m12 | PARTIAL | The clause now cites "under CC-REV-8" but still paraphrases the policy. The paragraph grew from 402 to 625 words (+223). Review 1 estimated about 150. This is a note only. |

## Material

**N1. Scenario 3 brings back the per-relationship quota that the clause removed (M2).**
- Quotes:
  - Clause: "Where a diagram would explain a structural relationship … better than prose, that diagram is a requested relationship asset".
  - Scenario 3: "WHEN the independent design review enumerates an explained structural relationship that has no diagram / THEN the omission passes only as a reasoned omission … AND a relationship the authoring stage never listed is still a finding".
- Problem:
  - The review lists *every* explained structural relationship.
  - Under the clause, a relationship that prose explains at least as well has no diagram asset, so it has no disposition to pass on.
  - Under Scenario 3, that same relationship fails unless the author pre-recorded a reasoned omission. If the author never listed it, it is a finding even when prose is clearly enough.
  - So the author must list and disposition every structural relationship, including ones a single sentence covers. That is the per-relationship paperwork M2 objected to, and the scenario contradicts its own clause.
- Fix: make Scenario 3's WHEN say "enumerates an explained structural relationship that, in its judgment, a diagram would explain better than prose, and that has no diagram". Change the AND to "a relationship meeting that condition that the authoring stage never listed is still a finding". State in the clause that the review may accept "prose at least as clear" on its own judgment, with no prior author record.

**N2. Requiredness is left open, so readiness depends on a value nobody is assigned to set.**
- Quotes:
  - Clause: "with its own identity and requiredness (REQ-polaris-generation-019)".
  - REQ-004: "An asset required by the request, reading obligation or frozen acceptance criteria SHALL remain unmet when … renderer capability is unavailable".
  - Scenario 4: "its disposition is unresolved and any readiness criterion requiring it remains unmet".
- Problem:
  - If the author marks a relationship diagram optional, an unresolved diagram (for example, because the renderer failed) does not block readiness under Scenario 4. It fails under Scenario 3 ("passes only as a reasoned omission").
  - The spec does not say which scenario controls, or who assigns requiredness.
  - If the authoring stage assigns it, the author sets its own gate, which REQ-006 forbids: "SHALL NOT define or narrow its own review denominator". The M1 dodge then comes back through requiredness instead of through the disposition reason.
- Fix: "that diagram is a required relationship asset, a reading obligation with its own identity under REQ-polaris-generation-019". Alternatively, state that requiredness is fixed by the independent design review's enumeration and never by the authoring stage. Then align Scenario 4's AND with that.

**N3. PWB-REQ-006 binds "the POC", not just `/polaris`, and the draft preview is in the POC app. [Inferred]**
- Quotes:
  - PWB-REQ-006: "The POC SHALL … NOT … emit active HTML, SVG, scripts, event handlers or unsafe URL schemes".
  - PACKET: "**Draft preview** (`apps/three-surface-poc/src/polaris-generation/draft-preview.ts`): Mermaid renders to SVG on the server, and the SVG is inlined".
  - PACKET: "It emits nothing on `/polaris`".
- Problem:
  - The packet routes the SVG question to the Butlers `/polaris` package. But the requirement's subject is the POC.
  - The draft preview lives in `apps/three-surface-poc/`, and Butlers is the proving case, so a preview of a Butlers page is plausibly POC output built from Butlers content.
  - Whether PWB-REQ-006 reaches the draft preview, and whether "active" qualifies "SVG", is not settled by these files.
  - The single adoption phrase also authorizes implementation ("Adopt and implement"), so this unresolved reading would be authorized by the act itself.
- Fix: choose one.
  - (a) State, with the basis, why the draft preview is outside PWB-REQ-006's subject.
  - (b) Use an inert non-SVG preview form (HTML/CSS) for this package.
  - (c) Make "implement" exclude inline SVG until an owner ruling reads PWB-REQ-006.

## Minor

**m-a. The partly supported diagram has no scenario of its own** (remainder of m2).
- Quote: "an unsupported edge is omitted with its gap disclosed rather than drawn" sits under a WHEN about a relationship "that has no diagram".
- Fix: add a WHEN such as "a diagram's premises support some edges but not others". Its THEN would draw only the supported edges, disclose the gap, and carry the diagram's disposition.

**m-b. Unknown markings versus unsupported elements are unclear.**
- Quotes:
  - "every node, edge and label SHALL have the support required above, and each element's Observed, Inferred or Unknown marking SHALL carry into the render".
  - Scenario 3: an unsupported edge is "omitted … rather than drawn".
- Problem: a reader cannot tell whether an Unknown-marked edge may be drawn.
- Fix: "Unknown marks a supported element whose state is Unknown; an unsupported relationship is never drawn."

**m-c. "the support required above" does not cover labels.**
- The sentence it points to says "support for factual edges as well as nodes" and says nothing about labels.
- The new clause also extends support from *factual* edges to *every* edge.
- Fix: state label support directly, and say whether non-factual edges (for example, reading order) need it.

**m-d. CC-REV-8's "A diagram asserts nothing the text does not" is not carried into the clause.**
- The packet's label check only partly implements it.
- Fix: add "and asserts no relationship the account does not state".

**m-e. REQ-002 is paraphrased more narrowly than it reads.**
- REQ-002 requires "purpose, thesis, motives, promises, boundaries, essential concepts and capability relationships in a coherent project-specific argument". The clause keeps only "connections between motives, promises and capabilities".
- Fix: "keeps REQ-polaris-generation-002's coherent project-specific argument".

**m-f. The opening summary above verbatim text needs a guard.**
- "Each section SHALL be an abstraction tree" reaches sections whose body is a verbatim leaf or contract-band owning text.
- A generated one-sentence answer there sits close to REQ-012's "generated prose SHALL NOT substitute for the owning artifact's text".
- Fix: add "a generated opening above verbatim text is marked generated and never replaces or paraphrases the leaf as its text".

**m-g. The review is named inconsistently.**
- REQ-006 says "independent fidelity and rendered-design reviews". The clause says "independent design review".
- Scenario 3 also does not say whether the missing-diagram finding is blocking under REQ-006.
- Fix: use "independent rendered-design review" and say "blocking finding".

**m-h. PACKET: "Review 2 confirms the revised bytes" is written before Review 2 exists and is false at this verdict.**
- Fix: write "Review 2: `<verdict as copied from the raw>`" only after the raw is retained.

**m-i. PACKET: "All of its findings are addressed" and "Minor findings m1–m12: fixed" overstate.**
- M1, M2, M4, m2 and m12 are partial (table above).
- Fix: re-state the dispositions after repair.

**m-j. PACKET: "REQ-004 gains one paragraph of clauses" is inaccurate.**
- The text is appended to the existing single-paragraph clause (same line of the diff). It is not a new paragraph.
- Fix: "REQ-004's clause gains about 220 words".

**m-k. PACKET: "Every node, edge and label has the support REQ-004 already requires" is inaccurate.**
- REQ-004 previously required support for factual edges and nodes only (see m-c).

**m-l. The P-73 offset claim could not be checked here.**
- PACKET: "its patch still applies after this change, at an offset". The second hunk now adds 38 lines (`-156,6 +156,44`), not the 26 Review 1 checked.
- Fix: re-apply P-73's patch and record the offset and the result.

## C. Count verification

- **Requirements:** 31 in the effective composition, as claimed. The predecessor has 29 (REQ-001 to REQ-029). The amendment MODIFIES 7 (002, 004, 006, 009, 012, 014, 019) and ADDS 2 (030, 031).
- **Scenarios, method 1:** composing by requirement name gives 181.
- **Scenarios, method 2:** 154 predecessor `#### Scenario:` headings, minus 33 in the seven replaced blocks (3+8+3+5+4+3+7), plus 60 amendment headings, gives 181.
- **Before this change:** REQ-004 has 15 amendment scenarios now, 4 of them new, so the pre-change total is 181 − 4 = 177, as claimed.
- **Not run:** `scripts/count_polaris_effective_scenarios.py` is outside the permitted file set, so the packet's command itself was not executed.
- **Scope of the diff:** all three hunks fall inside the REQ-004 block, so "the other 30 requirements … are unchanged" holds.
- **PWB-REQ-006 reading:** the packet's statement "PWB-REQ-006 lists SVG among the content `/polaris` may not emit" is accurate as far as it goes. The requirement's subject is the POC, which is the point of N3.
