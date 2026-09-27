Title: Polaris tree-form amendment — confirmation review 3
Verdict: REVISE
Reviewed: SPEC-DIFF.patch and PACKET.md in review-pg3/, against REVIEW-2-RAW.md
Reviewer: independent fresh-context agent

## A. Status of REVIEW-2 findings

| ID | Status | Current text |
|---|---|---|
| N1 | RESOLVED | Scenario 3 WHEN: "enumerates a relationship that a diagram would explain better than prose and the draft has no diagram for it". AND: "a relationship the review judges prose to explain as clearly needs neither a diagram nor a disposition". The per-relationship quota is gone. See m-2 below for one leftover edge. |
| N2 | PARTIAL | Clause: "each is a required relationship asset with its own identity under REQ-polaris-generation-019". The review, not the author, now fixes the list, and Scenario 5 matches it ("the asset being required, readiness is blocked"). That settles who owns requiredness. But making these assets required clashes with REQ-004's existing rule for required assets. See M-1. |
| N3 | RESOLVED (packet) | PACKET: "PWB-REQ-006 binds the POC, not just `/polaris`. The SVG reading is now owner question 2, with an HTML/CSS fallback." The implementation section is conditional on that answer. How question 2 is framed is a separate problem. See M-2. |
| m-a | RESOLVED | Scenario *Partly supported diagram*: "only the supported elements are drawn and the unsupported edges are disclosed beside the diagram as a gap". Two parts of the review 2 fix are missing: the disposition the diagram carries, and disclosure of unsupported nodes. See m-4. |
| m-b | PARTIAL | Clause: "an unsupported relationship is never drawn, and each drawn element's Observed, Inferred or Unknown marking carries into the render". Scenario 4: "an unsupported edge is never drawn, whether marked Inferred, Unknown or not at all". The proposed sentence defining a drawn Unknown element ("Unknown marks a supported element whose state is Unknown") was not added. See m-3. |
| m-c | RESOLVED | "every node, edge and label it draws has admitted support". This covers labels and every edge. |
| m-d | RESOLVED | "it asserts no relationship the account does not state". |
| m-e | RESOLVED | "tree form keeps REQ-polaris-generation-002's coherent project-specific argument". |
| m-f | PARTIAL | "a generated opening above verbatim text is marked generated and never replaces or paraphrases it". The qualifier "as its text" from the review 2 fix was dropped. That creates a conflict inside the clause. See m-1. |
| m-g | RESOLVED | "The independent rendered-design review" … "is a blocking finding". This matches REQ-006's "independent fidelity and rendered-design reviews". |
| m-h | RESOLVED | PACKET: "Review 2 — … verdict **REVISE**" and "Review 3 — pending". The verdict matches REVIEW-2-RAW.md line 2. |
| m-i | PARTIAL | The review 1 recount is correct: "M3, M5 and ten minor findings resolved; M1, M2, M4, m2 and m12 partial". That is m1 and m3–m11, which is 10. But the new line "Its minor findings are repaired: … m-b … m-f" overstates, because both are partial (above). See m-6. |
| m-j | RESOLVED | PACKET: "REQ-004's clause gains about 230 words". Measured: 402 → 634 words, +232. |
| m-k | RESOLVED | PACKET: "labels now need support too; support now covers every drawn edge, not only factual ones." |
| m-l | RESOLVED as far as checkable | PACKET: "both hunks succeed at an offset of 49 lines (checked with `patch --dry-run`)". The second hunk is now `-156,6 +156,55`, which adds 49 lines, so the offset is consistent. The P-73 patch is not in the review set, so I did not re-run the dry run. |
| M1 (review 1 PARTIAL) | PARTIAL | Now depends on M-1: the dispositions and requiredness contradict REQ-004's existing required-asset rule. |
| M2 (review 1 PARTIAL) | RESOLVED | Resolved through N1. |
| M4 (review 1 PARTIAL) | RESOLVED except framing | Resolved through N3. The framing of question 2 is open. See M-2. |
| m2 (review 1 PARTIAL) | RESOLVED | Resolved through m-a. |
| m12 (review 1 PARTIAL) | OPEN, note only | The clause still paraphrases CC-REV-8, and it grew by 232 words. It was a note only in review 2 and stays one. |

## Material

**M-1. A required relationship diagram with no premise support is both "reasoned-omitted and passing" and "unmet". The repair for N2 caused this.**
- Quotes:
  - Existing REQ-004 clause: "An asset required by the request, reading obligation or frozen acceptance criteria SHALL remain unmet when support, permission or renderer capability is unavailable."
  - Existing scenario *Required visual unavailable*: "WHEN a requested or acceptance-required visual lacks source support … THEN its disposition names the unresolved condition and the corresponding readiness criterion remains unmet".
  - New clause: "each is a required relationship asset … Such an asset is produced, reasoned-omitted only because its premises do not support drawing it, or unresolved".
  - Scenario 3: "a blocking finding is raised unless the asset is reasoned-omitted because its premises do not support drawing it".
- Problem:
  - Missing support is a case the existing required-asset sentence and *Required visual unavailable* both cover.
  - For a *required* asset, those texts say lack of support leaves it unresolved and unmet.
  - The new text says the same case is a passing reasoned omission.
  - Before the N2 repair these assets were only "requested", so no clash existed. Calling them "required" created it.
  - PACKET says *Required visual unavailable* is unchanged ("Everything else in REQ-004 is unchanged: … *Required visual unavailable*"). That is true of its bytes, but it is now contradicted in effect.
- Fix. Choose one.
  - (a) Unsupported premises remove the obligation. Suggested wording: "an enumerated relationship whose premises do not support drawing it is not a required asset; it takes a reasoned omission with the gap disclosed, and the required-asset sentence above does not apply to it". The review, not the author, would record that judgment.
  - (b) Keep the existing rule. Drop the reasoned-omission branch and let unsupported relationships stay unresolved and blocking. Then fix Scenario 3's THEN to match.
  - Either way, name *Required visual unavailable* in the clause as the controlling or excepted case, and correct PACKET's "What stays fixed" to match.

**M-2. Owner question 2 is not framed fairly to both readings.**
- Quotes:
  - PACKET: "**Recommended: permitted.** The spec's own inert-rendering scenario already names each active element to strip."
  - PACKET: "The draft preview lives in the POC app, so the ruling decides how diagrams render there."
  - PWB-REQ-006, second sentence of the same paragraph: "Outside inert-code contexts, an HTML element, comment or declaration; SVG; script; event-handler attribute; or an unsafe … scheme … SHALL exclude the whole source."
  - PWB-REQ-006 title: "Project-shape content stays contained, inert and bounded".
- Problem:
  - The case for "permitted" rests partly on the amendment's own scenario. That scenario is the thing question 1 adopts, so it cannot be evidence for how an already-adopted PWB requirement should be read. The argument is circular.
  - The strongest textual point for "banned" is left out. In the same requirement, bare "SVG" (no "active") is listed among constructs treated as active content. A fair framing must show this.
  - The practical reason ("the only way to draw a diagram … without layout code of our own") is offered for one side only. The cost of "permitted" is not given: sanitizer correctness becomes a security boundary.
  - The packet also settles a third question without asking it. The title limits PWB-REQ-006 to project-shape content, and the packet asserts that it reaches the generator's draft preview. That is the N3 scope question. Taking the conservative side is reasonable, but the packet should say it is a choice, not a given.
  - Nothing says how the plain-words answer to question 2 is recorded. It changes the security posture of POC output, which the act escalation triggers treat as needing an owner act.
- Fix:
  - Give each reading its own textual basis. For "permitted": "active" plausibly governs the list. For "banned": bare "SVG" appears in the input-exclusion sentence.
  - Remove the circular argument, or mark it as conditional on question 1.
  - State the scope assumption openly: "the packet assumes PWB-REQ-006 reaches the generator's draft preview; the owner may rule otherwise".
  - Keep a recommendation if wanted, but label it as the drafter's.
  - Say the answer is recorded as a dated owner direction under `decisions/`.

## Minor

**m-1. The verbatim guard conflicts with "each parent block truly summarizes its children".**
- Quote: "each parent block truly summarizes its children … a generated opening above verbatim text is marked generated and never replaces or paraphrases it".
- Problem: an answer-first opening over a verbatim leaf is that leaf's parent, so it must summarize the leaf. The guard forbids paraphrasing the leaf. It is not clear where summary ends and paraphrase begins, so the rule cannot be tested. This is the "as its text" qualifier from review 2's m-f fix, which was dropped.
- Fix: "never replaces the verbatim text or presents a paraphrase as its text; its summary is marked generated and the leaf remains the owning text".

**m-2. The review's judgment can waive a diagram that the request or acceptance criteria require.**
- Quote: Scenario 3: "a relationship the review judges prose to explain as clearly needs neither a diagram nor a disposition".
- Problem: the existing clause says "Every requested asset SHALL have an explicit … disposition". A relationship diagram that the request or frozen acceptance criteria require on some other basis would lose its disposition obligation through the review's prose judgment.
- Fix: add "unless the request, reading obligation or frozen acceptance criteria require it on another basis".

**m-3. What a drawn Unknown element means is still undefined (remainder of m-b).**
- Quote: "each drawn element's Observed, Inferred or Unknown marking carries into the render".
- Problem: Scenario 4 forbids drawing an unsupported edge "marked … Unknown". A reader still cannot tell what kind of element may be drawn with an Unknown marking.
- Fix: "a drawn element may be Unknown only where admitted support establishes the element and its state is Unknown".

**m-4. The *Partly supported diagram* scenario leaves out unsupported nodes and the disposition.**
- Quote: "only the supported elements are drawn and the unsupported edges are disclosed beside the diagram as a gap".
- Problem: unsupported nodes and labels are left undrawn but are not disclosed. The scenario also does not say whether a partly drawn required diagram is "produced".
- Fix: say "unsupported elements are disclosed". Add "the asset is produced with its gap recorded, and the gap is not a reasoned omission of the whole".

**m-5. The review's enumeration is a judgment, and nothing requires it to be recorded.**
- Quote: "enumerates the structural relationships … that, in its judgment, a diagram would explain better than prose".
- Problem: the Oracle checks "the bound review record and verdict". Without a recorded enumeration, a review that looked and found nothing cannot be told apart from one that did not look. This weakens the Falsifier. Also, REQ-019 says a "trusted recorded authoring operation SHALL issue opaque presentation identities". So an asset the review adds needs a stated route to its identity.
- Fix: "the review record retains its enumeration and the relationships it judged prose-sufficient; a repair's authoring operation issues each enumerated asset's identity".

**m-6. The Scenario 5 guard is a deny-list, and PACKET overstates the repair status.**
- Quote: Scenario 5: "no script, event-handler attribute, `foreignObject`, or external or unsafe-scheme reference".
- Problem: SVG animation elements (`set` / `animate`) and link elements are not named. The implementation text is an allow-list ("stripped to static shapes and text"), but the spec text is a deny-list.
- Fix: state the allow-list in the spec. Also change PACKET's "Its minor findings are repaired" to list m-b and m-f as partial until they are fixed.

**m-7. Note: the existing scenario *Meaningful visual instead of decorative quota* says "the author/design review identifies the question".**
- Problem: the new clause says the review, "not the authoring stage", enumerates.
- Fix: this is reconcilable, since authors may still flag relationships. A clause phrase would settle it: "authoring may propose relationships; only the review's enumeration fixes requiredness".

## B. Other checks

- **Over-reach beyond CC-REV-8:** none found.
  - "Answer first", "every level summarizes its subtree", "deeper levels … never new conclusions" (Scenario 1), "Format requirements win" and "asserts nothing the text does not" are all carried into the clause.
  - The inert-render list comes from REQ-012 and VIS-7, not CC-REV-8. Both are already warrants.
  - Making a missing diagram a blocking finding only places CC-REV-8's form rule within REQ-006's existing review gate.
- **Falsifiability:** apart from m-1 and m-5, the truncation test, per-element support and the render prohibitions can be checked.

## C. Packet accuracy

- **Requirements:** 31, as claimed. The predecessor has 29, the amendment modifies 7 and adds 2.
- **Scenarios:** 182, as claimed.
  - Method 1, composing by requirement name: 182.
  - Method 2: 154 predecessor headings − 33 replaced + 61 amendment headings = 182.
  - REQ-004 now has 16 amendment scenarios, 5 of them new, so the pre-change total is 177. The claim "177 → 182" holds.
  - `scripts/count_polaris_effective_scenarios.py` is outside the file set and was not run.
- **Diff scope:** all three hunks fall inside the REQ-004 block, so "the other 30 requirements … are unchanged" holds.
- **Inaccurate or overstated claims:**
  - "Everything else in REQ-004 is unchanged: … *Required visual unavailable*". See M-1.
  - "Its minor findings are repaired" (m-b, m-f). See m-6.
  - The framing of question 2. See M-2.
