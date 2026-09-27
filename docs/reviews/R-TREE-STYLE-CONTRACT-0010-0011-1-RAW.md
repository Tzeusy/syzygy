Title: Contract readability restyle — RFC 0010 and RFC 0011 — review 1
Verdict: REVISE
Reviewed: rfc2-draft/RFC-0010/{README.md, mission-identity-approval-and-lifecycle.md, prevention-envelope-and-attention.md, budget-reservation.md, effects-recovery-and-stop.md, portfolio-and-cross-project-consent.md}; rfc2-draft/RFC-0011/{README.md, packet-identity-provenance-and-memory.md, deterministic-selection-and-budget.md}. Each was compared against the same file under rfc2-orig/.
Reviewer: independent fresh-context agent

**Material findings**

**M1. RFC10-5: splitting a paragraph moved what "the paragraph above" points to** (`mission-identity-approval-and-lifecycle.md`, draft lines 175–191).

In the original, three sentences sit together as one paragraph, the one that begins "The rule covers **both** non-terminal states…":
- "…RFC10-11 offers."
- "Where a clause offers `paused` or `blocked` without a decider, the narrowest reading takes `blocked` — the state whose exit is a human act."
- "Expiry from a park is a **termination, never a resolution**: it widens nothing (RFC10-12), does not substitute for the human resolution act where the paragraph above owes one…"

The draft makes three paragraphs of these:
- "The rule covers … RFC10-11 offers."
- "Where a clause offers `paused` or `blocked` … the state whose exit is a human act."
- "Expiry from a park is a **termination, never a resolution** … where the paragraph above owes one…"

Why it matters:
- In the draft, "the paragraph above" now resolves to the narrowest-reading sentence. That sentence describes `blocked` as "the state whose exit is a human act".
- So the human resolution act "owed" can now be read as owed for every block reached by the narrowest reading. That is wider than the original's intended referent: the [Inferred] paragraph's human resolution act for blocks arising under RFC10-8 or RFC10-11.
- RFC10-18 depends on that scope, because it states that an RFC10-18-sourced block owes no human resolution act.
- This is a split that changes which text a condition covers (criterion 1).

Fix: restore the original paragraph. "The rule covers…", "Where a clause offers…" and "Expiry from a park…" should again form one paragraph. Restyle-only splitting does not preserve this deictic reference.

**M2. RFC10-21 diagram: the embedded-projects node reads as excluding the declared target** (`portfolio-and-cross-project-consent.md`, draft line 105).

- Old clause: "the egress-consent record of **every project whose content it embeds** — not one of them, never the project the composing step names for itself, and **regardless of how many projects the mission's declared target names**."
- New diagram node: `"every project whose content it embeds<br/>not the declared target; not the project<br/>the composing step names for itself"`

Why it matters:
- The clause keys the predicate on content, "regardless of" the declared target. It does not exclude the target.
- The node says "not the declared target", which reads as removing the target project's own content from the consent check. The diagram asserts an exclusion the clause does not make (criterion 4).
- "not the project the composing step names for itself" makes the same kind of error. The clause means the check is never limited to that one project, not that the project is exempt.

Fix: relabel the node, for example: `"every project whose content it embeds<br/>(keyed on content, not on the declared target;<br/>never only the project the composing step names)"`.

**Notes**

N1. **RFC10-5, "No park is indefinite".**
- The paragraph now ends "declared by the envelope;", followed by two bullets. The second bullet opens "and where the park minted none…".
- "The set is never empty…" is split into its own paragraph, away from the limb its "this limb" refers to.
- The meaning is preserved but the text reads badly. Rejoining the original paragraph as part of the M1 repair would also fix this.

N2. **RFC10-7.** "(Both worked examples above are grants…)" now sits two paragraphs below the examples, because the propose-only cap paragraph was split out between them. The reference still resolves, since nothing between them contains examples. Consider keeping the cap sentence in its original paragraph.

N3. **Effects orientation (criterion 3).** It says "every effect class an envelope permits is classified before it is authorized and dispositioned when the mission fails, is cancelled or expires".
- RFC10-19 dispositions applied effects, and only when the mission enters `failed`, `cancelled` or `expired` *with effects already applied*. It does not disposition effect classes.
- Suggest: "…classified before it is authorized, and applied effects are dispositioned when the mission fails, is cancelled or expires".

N4. **Portfolio orientation.** It says a composite "fails closed where one is missing". RFC10-21 also fails closed where the consent is not in force, lacks an effective exact-digest act, or the content cannot be attributed to a project of origin. The summary is short of the clause rather than false; consider "where any is missing or ineffective".

N5. **Selection orientation.** It says selection is "from a stated minimum set of inputs, including each selected contract's implementation-boundary declaration".
- RFC11-4's input list does not include the declaration.
- The declaration is something the mandatory set *always includes* for a selected contract.
- Suggest: "…from a stated minimum set of inputs, and always includes what each selected contract's implementation-boundary declaration names".

N6. **Mission orientation.** It says "a Mission binds its objective, target, pinned inputs and initiating owner act". RFC10-4 says "binding at minimum" and also lists rationale, parent mission, lifecycle state and terminal outcome. Adding "at minimum" or "among other things" would fix this.

N7. **RFC-0010 README diagram.** The edge runs from the whole prevention-plane subgraph to module 4. That implies module 5 has staged references into module 4, but RFC10-15 and RFC10-21 cite no module-4 clause. The README text names the examples in modules 1 and 3, and module 2 also cites RFC10-18 through RFC10-23. Consider drawing the edges from M1, M2 and M3 only.

N8. **RFC10-20(d) diagram.** The failure node leaves out "the stop record states the boundary". This is minor and does not mislead. Adding it would make the node complete.

**Epistemic-label span** (per RFC-REPAIR-BRIEF.md)

There are 6 labels in the scope:
- RFC-0010 README §2: [Observed]
- RFC10-2: [Observed — owner direction]
- RFC10-5: [Inferred]
- RFC-0011 README §2: [Observed] and [Inferred]
- RFC11-11: [Inferred]

"([Observed]/[Inferred]/[Unknown] discipline included)" in RFC11-8 mentions the labels but labels nothing, so it is excluded.

In all 6 of 6 cases, the whole paragraph containing the label is byte-identical in the draft after whitespace normalization. The paragraph before each is also unchanged. The paragraph after each is unchanged in 5 cases; the one exception is RFC10-5's [Inferred], which is followed by the restructured park rule. The original already had a paragraph break there, so the label's span is unchanged. No label now covers more or less text.

**Checks run**

1. **Word-level token diff** of the normative text over 9 of 9 file pairs, with list markers dropped and the added *Orientation* and *Diagram* paragraphs and fences excluded.
   - Result: 0 token changes in the 7 modules.
   - In the two READMEs, the only changes are 6 inserted bold lead-ins in the non-normative §0 ("Not a truth surface.", "Decisions, not streams.", "Portfolio authority is walled off.", "Selection.", "Provenance.", "Memory.").
2. **Paragraph-structure sweep.** 54 of 255 original paragraphs are not reproduced verbatim in the draft (7+6+6+8+2+10+7+2+6 by file). I read all 54 against the draft for:
   - qualifier attachment;
   - how "each", "all", "either" and "and" distribute over converted lists;
   - positional references.
   Findings: M1, N1, N2.
3. **Positional-reference sweep.** Swept "above / below / preceding / following / previous / next / this paragraph" over all 9 drafts: 25 hits. 1 hit's referent shifted (M1), 1 was weakened (N2), and 23 are unchanged or not references.
4. **Frozen elements** (Python, whitespace-normalized, excluding the added paragraphs). All match:

   | Element | Result |
   |---|---|
   | Front matter | identical 9/9 |
   | **Status:**, **Package:** and **Serves:** paragraphs | identical 9/9 |
   | `#` headings | 63/63 identical, same order |
   | Clause leads | 43/43 identical, same order |
   | Original fenced blocks | 4/4 byte-identical |
   | Code spans | 167/167 identical, same order |
   | Inline item letters and numerals (a)–(d), (i)–(iv) | identical, same order |
   | Numbered list items | identical |
   | Links | 0 in the originals, 0 in the drafts |
   | History/Amended parentheticals | 0 in the originals, 0 in the drafts |
   | Lines with an odd backtick count (broken code spans) | 0 |
   | Identifier tokens (RFCn-m, VIS, SEC, SDR, CC, OD) | 0 lost in any file (554 in the originals) |

5. **Orientation paragraphs (criterion 3).** Checked 9 of 9 against the clauses they cite. Every clause named exists and carries the weight claimed. Findings: N3–N6.
6. **Diagrams (criterion 4).**
   - 17 of 17 read against their clauses. Findings: M2, N7, N8.
   - All 17 are placed after their clause and captioned with the required non-normative line.
   - `mmdc` is not installed, so I could not re-render them. Instead, all 17 fence bodies match the pre-rendered `rfc2-mmd/*.mmd` sources exactly, and each has a non-error SVG.
   - I screenshotted the RFC10-5 state diagram in headless Chrome. It confirms awaiting-approval renders inside the "any non-terminal state" composite.
