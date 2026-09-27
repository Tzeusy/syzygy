Title: Contract readability restyle — RFC 0009 — review 1
Verdict: REVISE
Reviewed: rfc-draft/RFC-0009/README.md, rfc-draft/RFC-0009/semantic-geography.md, rfc-draft/RFC-0009/visual-grammar-and-lenses.md, rfc-draft/RFC-0009/interaction-parity-and-release.md (each compared against rfc-orig/RFC-0009/)
Reviewer: independent fresh-context agent

**Material findings**

**M1. Splitting paragraphs into lists has narrowed what several epistemic labels cover (criterion 1: an epistemic label now covers less text).**

In the original, each label below ends a single paragraph, so it covers the whole clause paragraph. The restyle breaks the paragraph into a lead, a list and a tail. The label now sits in only the last piece.

- **RFC9-17.** `[Inferred, from RFC9-4/14; reserved-extent device …]` used to cover the forbidden-churn list, the sentence "Any of these causing movement is a defect", and the reservation sentence. It is now attached only to the "**Reservation policy must be unbounded in principle:**" paragraph. The label's own "from RFC9-4/14" is the basis of the churn list it no longer reaches.
- **RFC9-11.** `[Inferred]` used to cover the whole mode-boundary clause. Now it covers only "A view that binds position to a metric …". The four bullets above it (default scene, explicit entry, marker, spatial memory) are left unlabelled.
- **RFC9-18.** `[Inferred]` no longer covers the lead or the three bullets (governed / `cache/` / `local/`).
- **RFC9-26, first `[Inferred]`.** It no longer covers the lead or the seven-field declaration list.
- **RFC9-26, second `[Inferred]`.** Old: "…bound to the registry's exact digest. A valid state-(1) … An entry without a valid act is treated exactly as an absent one — the channel does not render. [Inferred] A forged entry …". New: the bold lead is its own paragraph and the label ends bullet 2 only. The lead and bullet 1 lose it.
- **RFC9-32.** `[Observed: SDR-20]` used to end the sentence listing both the primary lenses and the overlays. It now ends the overlays bullet only. The Architecture/Verification bullet loses its source.
- **RFC9-37.** `[Observed: vision.md]` used to end the list of all five Factory obligations. It now ends the last bullet only.
- **Borderline, same mechanism.**
  - RFC9-44 `[Observed: v1.md; SDR-25]` is now confined to the last bullet.
  - RFC9-49 `[Observed: vision.md, Performance]` is now confined to the "Silent decimation…" bullet.
- **Fix.** For each clause above, either restore the original single paragraph, or keep the list and end the list's closing paragraph with the label so its span matches the original. Do not move the label itself.

**M2. The RFC9-19/20 diagram makes a necessary condition look like a mandated outcome (criterion 4).**

- The branch `"one, determinate"` leads to "stands at its declared home; other mapped districts render link markers (RFC9-19(c)), never a clone".
- RFC9-19 says the map must *support all three* mechanisms, and that mechanism (c) "is available only where a **determinate** declared home exists". A determinate home is necessary for (c). It is not sufficient, and (c) is not required.
- A single declared shared-infrastructure membership puts the component in the shared-infrastructure district, which is mechanism (b).
- **Fix.** Change the node to "stands at its declared home; RFC9-19(c) link markers are available here (never a clone)". Or show (a), (b) and (c) as the supported options.

**M3. The RFC9-45 diagram leaves out a condition, so its pass branch looks sufficient (criterion 4).**

- The path `L -->|yes| SF{"Scope or freshness rejected by the policy?"}` → pass → "Walkthrough gate cleared" skips a requirement.
- Item 3 has the policy fix "**which judgment classes qualify and who may judge**", and the gate "requires a lawful **qualifying** pass". A pass by a non-qualifying judgment class or judge clears nothing.
- **Fix.** Reword SF to "Judgment class, judge, scope or freshness not qualifying under the effective policy (or B12(b)'s default)?".

**M4. The scenario diagram states a limited outcome as if it always applied (criterion 4).**

- `PROP --> PS["N candidate futures, selectable one at a time; …"]` presents this as what every Proposed scene looks like.
- RFC9-40 limits it: the kernel "refuses to union proposals in one exclusivity group or of undeclared compatibility — the honest render is *N candidate futures*".
- **Fix.** Change the node to "Where proposals share an exclusivity group or compatibility is undeclared: N candidate futures, one at a time; never looks like existing structure (RFC9-40)".

**Notes**

- **N1. Layout diagram caption.** RFC9-14/15(b) caption: "the owner-gated full regeneration that rewrites its baseline". RFC9-14(a) says the baseline is "written by the regeneration act, immutable thereafter". Use "writes a new baseline", matching the diagram's own edge label, "writes".
- **N2. RFC9-49 diagram.**
  - The `yes → "Render without narrowing"` node is not stated by the clause.
  - The `never` edge hangs off the budget decision, but the prohibition is unconditional.
  - Consider dropping the yes-node, or labelling it "(clause silent)".
- **N3. RFC9-49 bullets.** The "Silent decimation … forbidden" bullet now visually hangs under "When a budget cannot be met…". The original also ran on in the same paragraph, so this is tolerable. A separate paragraph would avoid implying the prohibition is conditional.
- **N4. RFC9-52 diagram.**
  - `U --> CM` shows an unmapped consequence as an ordinary matrix row, but the clause requires every clause to be mapped.
  - The diagram also omits the actual effect: no implementation work may be scheduled.
  - Consider "unmapped: blocks scheduling; a matrix defect".
- **N5. RFC9-1.** "never independently authoritative;" became "…authoritative:" with the two RFC 0002 / RFC 0006 statements as sub-bullets. That makes them read as elaborations rather than sibling statements. Keep the semicolon form, or make them siblings.
- **N6. RFC9-31.** "Exactly one lens is active at a time." moved from the end to the lead, and "each under RFC9-26" moved from after the list into the lead. Meaning is kept, but this reorders normative sentences rather than only restructuring them.
- **N7. RFC9-43.** The enumeration was reordered.
  - "— never label and Unknown reason alone" is now the lead.
  - The tier-coverage and primary-reason elaborations are nested under the counts bullet in swapped order.
  - The sibling-surface-state gloss moved up to its bullet.
  - Tokens are identical and I found no change in what "and" distributes over, but the code-span order in the file changes as a result. A re-reviewer should know this is a reorder and not only a split.
- **N8. §0 of interaction-parity-and-release.md.** It says "no user-observable Orrery behavior may be scheduled solely from this RFC". RFC9-52 says "No implementation work for **user-observable Orrery behavior** may be scheduled…". Restore "implementation work for".
- **N9. README "Violation cases — distribution".** It still says "the routing sentence carries the information", but that sentence is now three bullets. Say "the routing above".
- **N10. Over-long lines.** A few lines exceed about 78 columns: the §0 opener of semantic-geography.md, "SDR-28) is a rendering over those declarations … **Portfolio arrangement is", and several short dangling lines after list splits (RFC9-11, RFC9-18, RFC9-19). Cosmetic only.
- **N11. RFC9-10.** The label `[Observed: SDR-21; obligations (a)–(d) Inferred …]` also moved to a trailing paragraph. Because it names (a)–(d) explicitly, its coverage still reads correctly, so it is not in M1.
- **N12. §0 and README openers are true.** Every clause each opener names exists and carries the weight claimed:
  - semantic-geography: RFC9-4, RFC9-9 with its sub-clauses, RFC9-14 with RFC9-15(b), and the section ranges RFC9-8(a) in §2 and RFC9-13(a) in §3.
  - visual-grammar: RFC9-26, RFC9-27/43, RFC9-45, and the §2 promotion predicate, which is in RFC9-35.
  - interaction-parity: RFC9-46, RFC9-47/47(a), RFC9-49, RFC9-52.
  - README Orientation: follows the lookup rule.
- **N13. Diagrams checked and found faithful.** Beyond N1–N4, these assert nothing the clauses do not:
  - the lookup diagram (1..23 / 24..45 / 46..52 matches the module table);
  - the spatial-hierarchy diagram (RFC9-4);
  - the nearness diagram (RFC9-9(a) parts 1–2, including the "undecidable at this fidelity" branch);
  - the channel-registry diagram (RFC9-26).

**Checks run**

- **Front matter byte-identical:** 4/4 files.
- **Status paragraph identical:** 4/4. **Package paragraph identical:** 3/3 (the README has none). **Serves paragraph identical:** 4/4.
- **Headings (`#`–`###`), same text and order:** 42/42 (8 + 12 + 10 + 12).
- **Clause leads, `**RFC9-n…` through the first period, same text and order:** 29/29 (0 + 12 + 4 + 13).
- **Fenced blocks:** 0 in the originals. 10 added in the drafts, all Mermaid (README 1, semantic-geography 4, interaction-parity 2, visual-grammar 3). Each of the 10 is preceded by the exact caption `*Diagram (non-normative; the clauses govern):*`.
- **Code spans:** all 173 originals are kept as a multiset (14 + 72 + 32 + 55). 3 new, none of them a bare `status`: README `n` and `RFC9-n`, semantic-geography `map/`. Order changed only in visual-grammar, from the RFC9-43 reorder (N7).
- **Lines with an odd backtick count (broken code span), fences excluded:** 0 in all 4 drafts.
- **Relative links:** 0 in the originals, 0 in the drafts.
- **`*(History…)*` / `*(Amended…)*` parentheticals:** 0 in both versions.
- **Line-start item markers:**
  - All 31 original markers are kept in order.
  - The additions are the (a)–(d) markers of RFC9-10, RFC9-16 and RFC9-19 promoted from inline text in their original order.
  - The one README "(1)" difference is a wrapped "state (1)", not an item.
  - Inline `(x)` markers are unchanged, apart from new sub-clause citations in the 10 diagram captions and §0 maps.
- **Identifier tokens** (RFCn-m, VIS, SEC, SDR, CC, P, FD): 827 in the originals. None lost in any file. The gains are all in §0 maps, captions and diagrams.
- **Word-level token diff per section**, with list markers and fences dropped, over all 4 files and 44 sections: every flagged change was read.
  - Normative sections differ only in punctuation (—/;/: swaps), the RFC9-31 and RFC9-43 reorders, and the inserted captions.
  - No word was added or deleted inside a normative sentence.
- **Epistemic-label sweep:** 56 labels in the originals, 56 in the drafts, same sequence. Block-scope comparison flagged 9 paragraph-final labels. Two more mid-paragraph cases (RFC9-26 second `[Inferred]`, RFC9-32 `[Observed: SDR-20]`) were found by reading. The dispositions are in M1 and N11.
- **Diagram fidelity:** each of the 10 diagrams was read against its governing clause text in rfc-orig. Findings are M2–M4 and N1, N2, N4.

The scripts are in the scratchpad at `rev9/chk.py`, `rev9/wd.py`, `rev9/lab.py` and `rev9/lab2.py`.
