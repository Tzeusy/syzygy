Title: Specification policy tree-style restyle (CC-SPEC, CC-IMPACT) — review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: NEW-SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md, NEW-SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md and REPAIR-DIFF.txt, read against OLD-SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md, OLD-SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md and R-TREE-STYLE-SPEC-POLICY-1-RAW.md. All files are in /tmp/claude-1000/-home-tze-GitHub-syzygy/42f1d844-9fb6-4091-8261-544ed369daaf/scratchpad/review-spec2/.
Reviewer: independent fresh-context agent

## Material findings

None. No repair hunk changes the meaning of a rule. Two notes follow, neither material: the coverage-row diagram is still structurally loose (R2-1), and one repaired line exceeds the wrap width (R2-2).

## Disposition of review-1 findings

- **M1: RESOLVED, by the preferred fix.** Diagram 2 and its caption are deleted.
  - The CC-SPEC-10 section, from its lead to the CC-SPEC-11 lead, is now byte-identical to OLD.
  - The blockquote carries the structure again, including "RFC acceptance alone never opens it" and "No delegated mechanism ever reaches this class."
  - No other text referred to the deleted diagram. A sweep for "diagram" and "mermaid" found 1 caption left in the spec file and 2 in the impact file, and each caption heads its own block.
- **N1: RESOLVED in substance, with one structural note (R2-1).** The failure case is now drawn: `C -->|"neither, or N/A resting on say-so"| X["Clause not discharged;<br/>consequence unmapped, Unknown"]`.
  - This matches OLD "does not discharge this clause".
  - "Unknown" for the say-so case follows from "absent or invalid acts map nothing — the consequence remains unmapped and renders Unknown". That rests on RFC3-16(a) and VIS-2, and the block is captioned non-normative.
- **N2: RESOLVED.** NEW opener: "and a passing blind run against a named fixture precedes any reliance on the path."
  - The rule reads "the path is not relied on until a passing run exists … A recorded failing run … does not satisfy the clause."
  - The qualifier is now in the parent. Dropping the timing limb ("Before the first real shape amendment after specifications exist") is acceptable in a summary.
- **N3: RESOLVED, by deletion.** The unlabeled summary "f14 and f15 repaired, f1 (sibling) open" is gone. The "## Known open findings" section is byte-identical to OLD, and `[Observed]` opens it again.
- **N4: LEFT. This is reasonable.** The summary "leaves 'consumes its vocabulary' undefined" echoes the bullet's lead sentence "It does not define **'consumes its vocabulary'**." That sentence was already unlabeled in OLD and sits before the `[Unknown]` label. The labeled claim itself ("its undefinedness decides real cases") is not restated.
- **N5: RESOLVED.**
  - Spec file: "italic parentheticals mostly record dated history (CC-SPEC-11's also states its scope against CC-SPEC-8)."
  - Impact file: "Italic parentheticals mostly record dated history." All 6 italic parentheticals in the impact file are dated history (lines 103, 133, 169, 196, 219, 266), so "mostly" is a harmless hedge there. It adds no claim.
- **N6: LEFT. This is reasonable.** The three-way split from the population node is drawn in a flowchart captioned non-normative. The "exactly one set" discipline is in CC-IMPACT-7 item 2, which is byte-identical to OLD. The diagram does not contradict it.
- **N7, N8, N9: needed no action.** Nothing in REPAIR-DIFF touches them.

## Drift read of REPAIR-DIFF (5 hunks, 28 changed lines)

1. **Impact opener (N2):** It adds the qualifier "passing" and the phrase "named fixture", both taken from the rule. No modal was widened. "precedes any reliance" is equivalent to "not relied on until".
2. **Impact "mostly":** This narrows a claim; it does not widen one. There are no epistemic-label spans in this paragraph.
3. **Spec "mostly … (CC-SPEC-11's also states its scope against CC-SPEC-8)":** This is accurate to the parenthetical at lines 371–374.
4. **Spec coverage diagram: one edge added.**
   - It asserts non-discharge, which the text states.
   - It asserts "unmapped, Unknown", which the contract-cited limb states for an absent act.
   - It asserts nothing beyond the rules.
5. **Diagram 2 and the N3 summary deleted:** Both deletions restore OLD bytes in their sections.
6. **Positional references:** "the digest above" (CC-IMPACT-7) and "every sweep below" (CC-IMPACT-1) are both in unchanged text and still resolve.

## Notes

- **R2-1: the coverage-row diagram is still structurally loose.**
  - The decision node is binary ("Covered by requirements?") but now has three exits: "yes", "no" (to the N/A row) and "neither, or N/A resting on say-so".
  - The edge label "no" still reads as if every uncovered consequence gets an owner-cited N/A row. The new edge also mixes in a property of the N/A row ("resting on say-so").
  - Its "say-so" names only one of OLD's two insufficient grounds, "the author's or a reviewer's say-so, a judgment recorded only inside the spec". The second is implicitly excluded, because the NA node requires a "record in decisions/".
  - Optional tidy-up:
    - relabel the "no" edge as "no: N/A row citing an owner record";
    - relabel the new edge as "no: no N/A row, or N/A resting on less";
    - or move the say-so case to a branch off the NA node.
  - The diagram is non-normative and does not contradict the rule, so none of this is material.
- **R2-2: one repaired line breaks the wrap width.** Impact-file line 42 is 89 columns, and it is the only prose line in the repair over 78. No code span is broken, so a reflow is purely cosmetic.
- **R2-3: Mermaid was not rendered.** `mmdc` is not installed here. By eye, the added edge is valid syntax: quoted labels, and the node ID `X` is unused elsewhere in that block.

## Checks run (Python, OLD vs NEW with mermaid blocks removed and compared per `##` section; script at scratchpad/chk2.py)

- **REPAIR-DIFF is complete.**
  - `diff` from review-spec1/NEW-* to review-spec2/NEW-* gives 28 changed lines, the same as REPAIR-DIFF's 28.
  - The two line sets are identical.
  - spec-draft/* is byte-identical to review-spec2/NEW-*.
  - The OLD files are byte-identical across the review-spec1 and review-spec2 directories.

| Check | Spec file (OLD / NEW) | Impact file (OLD / NEW) |
|---|---|---|
| Banners | identical, 38 lines | identical, 34 lines |
| Headings (`#` lines outside fences) | 4 / 4, identical and in order | 5 / 5, identical and in order |
| Non-mermaid fences | 5 / 5, identical | 3 / 3, identical |
| Mermaid blocks in NEW | 1 (was 2) | 2 |
| Code spans | 25 / 25 | 23 / 23 |
| Dates | 24 / 24 | 9 / 9 |
| 64-hex digests outside fences | 0 / 0 | 0 / 0 (the one digest is inside the CC-IMPACT-7 fence, which is identical) |
| `.md` paths | 10 / 10 | 8 / 8 (my regex; review 1's counted 10) |
| Epistemic labels | 2 / 2 | 1 / 1 |
| Rule leads | 11 / 11 | 7 / 7 |
| Table rows | 5 / 5 | 9 / 9 |
| Blockquote lines | 57 / 57 | 34 / 34 |

All per-section multisets in the table are equal.

- **Identifiers only increase.** Spec file 127 → 142, impact file 90 → 95, all in the head summary and "## The rule" intro sentences. None was removed.
- **Modal and qualifier words.** Spec file 109 → 115, impact file 91 → 95. Every addition sits in an inserted summary or intro sentence, and none was removed from rule text.
- **Word diff.**
  - Spec file: 2917 → 3113 words. Impact file: 2221 → 2424 words.
  - Every non-equal opcode falls into one of five kinds: an inserted summary or intro sentence, a caption, a list marker, a connective change at a split, or the CC-SPEC-3 and "One fact, one home" moves review 1 already accepted.
- **CC-IMPACT-7 is byte-identical to OLD.** This covers the lead through "## What this rule set does not do".
- **Byte-identical regions.** The spec file's "## Known open findings" section, the impact file's "## Acceptance" section and the spec file's CC-SPEC-10 section all match OLD.
  - The impact file's "Why each rule" section differs only by the inserted line "One line per clause: the failure it prevents." Its table rows are equal.
- **No code span is broken across a line.** 0 lines outside fences have an odd backtick count, in either NEW file.
- **Epistemic-label paragraphs are unchanged:** 2/2 in the spec file and 1/1 in the impact file, all identical after whitespace normalization. The spec file's CC-SPEC-2 `[Observed]` paragraph is a reflow only, as it already was at review 1.
- **Nothing outside REPAIR-DIFF changed since review 1.** That follows from the completeness check above, so review 1's reading of the remainder stands.
