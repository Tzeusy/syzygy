Title: Polaris tree-form amendment — confirmation review 4
Verdict: REVISE
Reviewed: SPEC-DIFF.patch and PACKET.md in review-pg4/, against REVIEW-3-RAW.md
Reviewer: independent fresh-context agent

## A. Status of REVIEW-3 findings

| ID | Status | Current text |
|---|---|---|
| M-1 | PARTIAL | Clause: "An enumerated relationship whose premises do not support drawing it is not a required asset: the review records a reasoned omission with the gap disclosed, and the required-asset sentence above does not apply to it." This settles the case the review raised: an enumerated relationship that is required only because the review enumerated it. But the exception has no condition. It now also exempts a visual that the request or acceptance criteria require on another basis. See N-1. |
| M-2 | RESOLVED | PACKET gives each reading its own textual basis. For "permitted": "'Active' can govern the whole list". For "banned": "the same requirement's input sentence lists bare 'SVG', with no 'active'". It states the scope assumption ("This packet conservatively assumes PWB-REQ-006 reaches the preview; you may rule that it does not"). It gives both costs, labels the recommendation ("Drafter's recommendation, not a finding"), and says how the answer is recorded ("recorded as a dated owner direction under `decisions/`"). The circular argument is gone. One leftover wording issue is noted at n-1. |
| m-1 | RESOLVED (spec); packet stale | Clause: "a generated summary above verbatim text is marked generated, never replaces that text or presents a paraphrase as it, and leaves the leaf as the owning text". Scenario 1 matches: "never presented as that text". The PACKET summary still has the old wording. See n-2. |
| m-2 | RESOLVED for the prose-sufficient branch | "a relationship judged prose-sufficient needs no diagram unless the request, a reading obligation or frozen acceptance criteria require one on another basis". The same qualifier is missing from the unsupported-premises branch. See N-1. |
| m-3 | RESOLVED | "may be Unknown only where admitted support establishes the element and its state is Unknown". |
| m-4 | RESOLVED as worded, but the repair introduced N-2 | Scenario *Partly supported diagram*: "the unsupported ones are disclosed beside the diagram as a gap, and the asset is produced with that gap recorded". |
| m-5 | RESOLVED, one wording note (n-3) | "its review record retains that enumeration and the relationships it judged prose-sufficient"; "with its own identity under REQ-polaris-generation-019, issued by the repair's authoring operation". |
| m-6 | RESOLVED (spec and packet status line); the packet's implementation text still lags | Scenario 5: "static output containing only shapes, paths, text and styling, with no script, event-handler attribute, animation, `foreignObject`, link, or external or unsafe-scheme reference". PACKET: "Its minor findings were repaired as follows (review 3 found m-b and m-f partial)". See n-4. |
| m-7 | RESOLVED | "Authoring may propose structural relationships for diagrams, but only the independent rendered-design review fixes which ones require a diagram". This agrees with the existing scenario, where "the author/design review identifies the question". |
| N2 (review 2, PARTIAL) | RESOLVED subject to N-1 | Requiredness is owned by the review, and the clash with the required-asset rule is resolved for enumeration-only requiredness. |
| m-b (review 2, PARTIAL) | RESOLVED | Resolved through m-3 (above). |
| m-f (review 2, PARTIAL) | RESOLVED | Resolved through m-1 (above). |
| m-i (review 2, PARTIAL) | RESOLVED | PACKET: "(review 3 found m-b and m-f partial)". |
| M1 (review 1, PARTIAL) | PARTIAL | This finding tracks M-1, which is still partial through N-1. |
| m12 (review 1) | OPEN, note only | The clause still paraphrases CC-REV-8. It is now about 338 words longer than the predecessor clause (measured 402 → 740). |

## Material

**N-1. The reasoned-omission exception overrides a visual that the request or acceptance criteria require. This contradicts *Required visual unavailable* and the packet's own claim. The M-1 repair introduced it.**
- Quotes:
  - Clause: "An enumerated relationship whose premises do not support drawing it is not a required asset: the review records a reasoned omission with the gap disclosed, and the required-asset sentence above does not apply to it."
  - Existing scenario *Required visual unavailable*: "WHEN a requested or acceptance-required visual lacks source support … THEN … the corresponding readiness criterion remains unmet".
  - PACKET, "What stays fixed": "REQ-004's required-asset sentence and *Required visual unavailable* still govern every required visual."
- Problem:
  - Take a relationship that the frozen acceptance criteria require a diagram for, which the review also enumerates, and whose premises do not support drawing it.
  - The existing scenario says readiness stays unmet.
  - The new clause says the required-asset sentence "does not apply to it", so it passes as a reasoned omission.
  - The review's enumeration therefore turns an acceptance-required visual into a passing omission. That is the laundering path the existing rule closes.
  - The m-2 repair qualified only the prose-sufficient branch with "unless … on another basis". It did not qualify this branch.
  - The packet's sentence "still govern every required visual" is therefore false for this overlap.
- Fix:
  - Change the clause to: "An enumerated relationship whose premises do not support drawing it is not a required asset on the strength of the enumeration alone: … and the required-asset sentence above does not apply to it unless the request, a reading obligation or frozen acceptance criteria require that visual on another basis, in which case it remains unmet."
  - Mirror this in Scenario 3's AND clause, which currently reads "a relationship whose premises cannot support a diagram takes a recorded reasoned omission instead".

**N-2. A "partly supported" diagram can be nodes with no edges and still count as "produced". That discharges a blocking requirement with the decorative approximation that REQ-004 forbids. There is also no test for where "partly supported" ends and "does not support drawing it" begins.**
- Quotes:
  - Scenario *Partly supported diagram*: "only the supported elements are drawn, the unsupported ones are disclosed beside the diagram as a gap, and the asset is produced with that gap recorded".
  - Clause: "An enumerated relationship whose premises do not support drawing it is not a required asset".
  - Existing clause: "silent omission, decorative approximation or an unapproved textual substitute SHALL NOT discharge a required asset".
  - Existing scenario *Meaningful visual instead of decorative quota*: "inserting boxes with supported nouns but unsupported or meaningless arrows cannot close the finding".
- Problem:
  - Suppose every edge of an enumerated dependency is unsupported but its nodes are supported.
  - Under Scenario 4, that case reads as "partly supported". The result is boxes with no arrows, and the gap is disclosed.
  - That result is "produced", which clears the blocking finding.
  - The existing text forbids exactly this: boxes that show supported nouns without the relationship.
  - The same input could instead fall under "premises do not support drawing it", which gives a reasoned omission. Nothing says which branch applies, and nothing requires the review to record which branch it chose.
  - Two reviewers could reach different dispositions on identical premises, and neither could be shown wrong. That makes the rule untestable.
- Fix:
  - Add to the clause: "A diagram is produced only when its drawn elements include at least one supported edge of the enumerated relationship. Otherwise the premises do not support drawing it. The review record names which branch applied."
  - Add to Scenario 4's AND clause: "a diagram of supported nodes with none of the relationship's edges is not produced".

## Minor

**n-1. The drafter's recommendation still undercuts the "banned" reading.**
- Quote: "Server-rendered SVG is the only way to get a readable diagram under the preview's `default-src 'none'` CSP."
- Problem: the "banned" cost line says HTML/CSS boxes work but are "plainer". Calling SVG "the only way to get a readable diagram" suggests the other reading yields an unreadable page, which the packet does not show.
- Fix: "Server-rendered SVG is the most legible option under the preview's `default-src 'none'` CSP; HTML/CSS boxes also work but are plainer."

**n-2. The packet summary of the verbatim guard is the pre-m-1 wording.**
- Quote: PACKET "What changes": "It never replaces or paraphrases that text."
- Problem: the clause now allows a generated summary. It forbids only presenting a paraphrase as the verbatim text. The packet describes the rule that review 3 found untestable.
- Fix: "It never replaces that text or presents a paraphrase as it; the verbatim leaf remains the owning text."

**n-3. The identity route names only "the repair's" authoring operation.**
- Quote: "with its own identity under REQ-polaris-generation-019, issued by the repair's authoring operation".
- Problem 1: a relationship that the author proposed and drew in the first draft, and that the review then enumerates, gets its identity from the original authoring operation. No repair is involved.
- Problem 2: REQ-019 also says "Each requested asset SHALL have its own identity … resolving to one produced, omitted or unresolved disposition". The clause is silent on whether a reasoned-omitted enumerated relationship carries an identity.
- Fix: "issued by the trusted recorded authoring operation that introduces it (the original or a repair)". Also state whether a reasoned omission under the unsupported branch carries an asset identity with an "omitted" disposition.

**n-4. The packet's implementation text is still a deny-list and does not match Scenario 5.**
- Quote: PACKET: "stripped to static shapes and text: no script, no event handler, no `foreignObject`, and no external or unsafe-scheme reference".
- Problem: Scenario 5 also excludes "animation" and "link", and it allows "paths" and "styling". The packet's list is shorter on both counts.
- Fix: copy Scenario 5's allow-list and exclusions into the implementation bullet, and say that the sanitizer's mutation tests cover each excluded class.

**n-5. Where the reasoned omission's gap is disclosed is not stated.**
- Quote: "the review records a reasoned omission with the gap disclosed".
- Problem: it is unclear whether the gap is disclosed in the review record or in the rendered account. The existing rule is "Supported gaps remain explicit at the depth they affect". A review cannot edit the draft.
- Fix: "… with the gap disclosed in the rendered account at the depth it affects".

## B. Other checks

- **Repairs versus the rest of the effective spec:** N-1 and N-2 are the only contradictions I found that the repairs introduced.
  - Scenario 3 THEN, the clause's "an unresolved or missing one is a blocking finding" and Scenario 5's "readiness is blocked" agree.
  - The m-7 phrase agrees with *Meaningful visual instead of decorative quota*.
- **Falsifiability:**
  - The recorded enumeration (m-5) gives the Oracle a checkable object.
  - The Unknown definition (m-3) is checkable.
  - The branch choice in N-2 is the remaining untestable point.

## C. Packet accuracy

- **Word count:** "about 340 words" holds. The clause measures 402 → 740 words, +338.
- **Counts:** "31 requirements and 177 scenarios to 31 and 182" holds.
  - The amendment has 61 scenario headings, 5 of them new.
  - 154 − 33 + 61 = 182. The pre-change total is therefore 177.
  - The counting script is outside the file set and was not run.
- **P-73 offset:** "both hunks succeed at an offset of 54 lines" is consistent with the diff.
  - Hunk 2 is `-156,6 +156,60`, which adds 54 lines.
  - Hunks 1 and 3 add no net lines.
  - The P-73 patch is not in the review set, so the dry run was not re-run.
- **Diff scope:** all three hunks fall inside the REQ-004 block, so "the other 30 requirements … are unchanged" holds.
- **PWB-REQ-006 quotes:** accurate.
  - The output quote matches the source text: "emit active HTML, SVG, scripts, event handlers or unsafe URL schemes".
  - The input sentence does list bare "SVG".
  - The title and the subject "The POC" are quoted correctly.
- **Inaccurate claims:**
  - "still govern every required visual". See N-1.
  - "It never replaces or paraphrases that text". See n-2.
  - The implementation-bullet list of what the sanitizer strips. See n-4.
- **Framing of question 2:** fair to both readings, apart from n-1.
