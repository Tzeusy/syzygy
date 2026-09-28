Title: Specification policy tree-style restyle (CC-SPEC, CC-IMPACT) — review 1
Verdict: REVISE
Reviewed: NEW-SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md, NEW-SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md (against their OLD-* counterparts; NOTES.md read as context), all in /tmp/claude-1000/-home-tze-GitHub-syzygy/42f1d844-9fb6-4091-8261-544ed369daaf/scratchpad/review-spec1/
Reviewer: independent fresh-context agent

The prose restyle changes no meaning. One diagram does, and that alone is why the verdict is REVISE.

## Material findings

**M1 — The CC-SPEC-10 adoption diagram (spec file, lines 361–370) shows an exclusivity and a sufficiency that neither the rule nor VIS-4 contains.** (Criterion 4; NOTES flag 13.)

- **OLD text, which the diagram depicts (unchanged in NEW, lines 342–348):** "VIS-4 opens the delegated gate only on **both** of two conditions … and neither exists." The rule states a necessary condition only. It never says what happens once the gate is open, beyond keeping the always-human-gated class.
- **NEW diagram:**
  - `G{"Delegated gate open? …"}` `-->|"yes"| D["Delegated adoption under VIS-4"]`
  - `G -->|"no: neither exists today"| O`
- **Exclusivity:** in a gate-open future, a change outside the human-gated class has no path to "Owner adoption". Neither the rule nor VIS-4 takes owner adoption away.
- **Sufficiency:** "gate open" leads straight to delegated adoption. VIS-4 (`.syzygy/governance/doctrine/vision.md` lines 174–186) only says LLM adoption is "permitted in principle". Each delegated adoption would also still be subject to the adjudication RFC: independent adversarial judgment, a recorded ambiguity determination, and classification settled without a human "only while an opened gate is in force".
- **Why this matters here:** the diagram also drops "RFC acceptance alone never opens it". CC-SPEC-10's own history (NEW lines 372–381) records that RD-51 f12 was exactly this kind of gloss: "a reader in a gate-open future, reading CC-SPEC-10 alone, would conclude…". The diagram brings that picture back, in a block placed directly above the sentence "The clause now quotes both limbs rather than glossing them."
- **Suggested fix, preferred:** delete diagram 2. The blockquote already carries the structure.
- **Suggested fix, minimal:**
  - point the "yes" edge at a terminal such as `"Not today; delegated adoption would be governed by VIS-4 and the adjudication RFC"`, with no edge into R;
  - keep the owner path reachable from every branch;
  - add "RFC acceptance alone never opens it" to the gate node.

## Notes

- **N1 — Coverage-row diagram (spec file, lines 305–313; NOTES flag 12).**
  - The `C -->|"no"| NA["Reviewed N/A row …"]` edge implies that every uncovered consequence becomes a cited N/A row. The text states an obligation ("covered … or carries a reviewed N/A judgment"). It does not describe a pathway.
  - The failure case is not drawn: an uncovered consequence with no N/A row, or with an N/A resting on "say-so" ("does not discharge this clause").
  - Suggested fix: add a branch `"neither, or N/A without an owner record" → "clause not discharged; consequence unmapped, Unknown"`.
  - Leaving out the not-applicable branch is acceptable, because the caption scopes the diagram to an applicable clause.
  - `yes → N/A honored` reads as sufficient where the text says "only through". This is tolerable because the text itself splits the cases into effective versus absent or invalid.
- **N2 — The impact opener (line 42) drops the qualifier that CC-IMPACT-7 exists for.**
  - NEW: "the path is run blind against a fixture before it is relied on".
  - Rule: "the path is not relied on until a **passing** run exists … A recorded failing run … does not satisfy the clause."
  - CC-REV-8 says a caveat that changes the answer belongs in the parent.
  - Suggested fix: "…and a passing blind run against a named fixture precedes any reliance on the path." Strongly recommended.
- **N3 — The summary in "Known open findings" (spec file, lines 427–428) drops qualifiers and sits outside the `[Observed]` label.**
  - NEW: "f14 and f15 repaired".
  - The table says "the confirming review … has the last word, not this file" and "Awaits the confirming review".
  - The summary is also placed above the `[Observed]` paragraph, so it restates observed content without a label.
  - Suggested fix: "f14 and f15 repaired, pending the confirming review; f1 (sibling) open". Either move the summary after the label paragraph or accept it as an unlabeled summary.
- **N4 — The "Four limits" summary (impact file, lines 277–279) restates the `[Unknown]` "consumes its vocabulary" limb without its label.** The bullet keeps the label, so nothing is lost. The parent simply carries an unlabeled echo.
- **N5 — "Italic parentheticals record dated history."** (spec file line 61; impact file line 66). The CC-SPEC-11 lead parenthetical also carries a scope distinction: "Distinct from CC-SPEC-8, which covers contract clauses; this clause covers the capability's own obligations." Calling every such parenthetical "history" could demote that distinction. Suggested wording: "…record dated history (CC-SPEC-11's also states its scope against CC-SPEC-8)", or "mostly record".
- **N6 — The propagation diagram (impact file, lines 49–61) draws the population as split three ways** into affected, explicitly unaffected and undecidable. CC-IMPACT-3 names four sets but does not itself state exclusivity; only the answer key, quoted in CC-IMPACT-7, says "exactly one set". This is minor. Otherwise the diagram matches CC-IMPACT-2 through 6.
- **N7 — The declaration diagram (impact file, lines 95–101) is accurate.** It does not claim the sweep reads only the declaration; the sweep also covers "consume its vocabulary". Fine as captioned ("what reads it").
- **N8 — Prose splits (NOTES flags 1–10) preserve meaning.**
  - CC-SPEC-3: the appositive now opens as a verbless fragment ("CC-REV-7's discipline extended to requirement identifiers, including its retirement limb:"). It reads as the heading of the bullets and is equivalent.
  - Both "and"-joined limbs became sibling bullets under one parent. Conjunction is kept and no modal moved.
  - "only" (CC-SPEC-8), "never finally made" (CC-SPEC-6), "Until that act is performed" (CC-IMPACT-6) and the "if declaration-matching…" condition (CC-IMPACT-3) each stay in the bullet they qualify.
  - "What this policy is not" moved its maxim to the front; the meaning is unchanged.
- **N9 — Openers otherwise claim nothing new.** The spec opener's "which generates each specification's declaration from CC-SPEC-2" follows the banner's own figure of speech ("CC-IMPACT-1 generates…").

## Checks run (Python scripts in the scratchpad; denominators given)

1. **Word diff of each whole file (`difflib` over whitespace tokens).**
   - Spec file: 2917 old words, 3263 new. Impact file: 2221 old words, 2558 new.
   - Every non-equal opcode is one of four kinds: an inserted summary sentence, a list marker, a punctuation or connective change at a split, or a mermaid block with its caption.
   - The connective changes are "and" → ";"/"-", "; a" → ". - A", "(RFC3-15)," → "(RFC3-15); - it is", and the CC-SPEC-3 and "One fact, one home" moves.
   - No other word in rule text changed.
2. **Headings:** identical and in order (spec 5/5 sections, impact 6/6).
3. **Non-mermaid fences:** identical (spec 5/5, impact 3/3). There are 2 new mermaid fences per file, each captioned "*Diagram (non-normative; the rules govern):*".
4. **Per-section multisets (mermaid stripped), OLD versus NEW**, over code spans, dates, 64-hex digests, `.md` paths, epistemic labels, bold rule leads, table rows and blockquote lines:
   - Spec file: code 25/25, dates 24/24, paths 10/10, labels 2/2, leads 11/11, table rows 5/5, blockquote lines 57/57.
   - Impact file: code 23/23, dates 9/9, digests 1/1, paths 10/10, labels 1/1, leads 7/7, table rows 9/9, blockquote lines 34/34.
   - Identifiers only increase (spec 129→147, impact 90→95). Every addition sits in the new summary sentences or captions; none was removed.
5. **Banners:** the head banner of each file is byte-identical (2/2).
6. **Frozen regions:** from the CC-IMPACT-7 lead through the end of its history parenthetical is byte-identical. The rationale table and "## Acceptance" are byte-identical.
7. **Broken code spans:** no non-fence line in either NEW file has an odd backtick count (0 lines found).
8. **Rule leads:** every `**CC-…-n —` lead opens a paragraph. The only 2 matches that do not open a paragraph are mid-paragraph bold references (`**CC-KNOW-16**`, `**CC-IMPACT-2**`), and they are identical in OLD.
9. **Epistemic labels:** the 2 `[Observed]` paragraphs and 1 `[Unknown]` bullet are unchanged in text and still single paragraphs. The label scope is the same.
10. **Positional references:** "every sweep below", "the digest above", "this list", "this limb" and "as CC-SPEC-8" each still resolve to the same text (5/5).
11. **Diagram claims:** checked against VIS-4 in the doctrine and against RFC9-52's N/A text (`RFC-0009/interaction-parity-and-release.md` lines 305–320).

Not done: I did not re-render the Mermaid diagrams, because `mmdc` is not installed here. That leaves the restyler's render claim unverified.
