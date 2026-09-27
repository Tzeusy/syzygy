Title: Contract readability restyle — RFC 0005, 0006 and 0007 — review 1
Verdict: REVISE
Reviewed: RFC-0005/README.md, RFC-0005/admission-and-boundary.md, RFC-0005/consent-egress-secrets.md, RFC-0005/execution-profiles.md, RFC-0006-cross-surface-selection-query-drawer.md, RFC-0007/README.md, RFC-0007/narrative-contract.md, RFC-0007/rendering-and-surface.md (compared under rfc-orig/ and rfc-draft/)
Reviewer: independent fresh-context agent

**Material findings**

- **M1 — The RFC5-15 choke-point diagram adds an order and drops an outcome** (consent-egress-secrets.md §3.7).
  - Clause: "Three parts must all pass". Separately, "A consent record present in the governed tree without a valid act does not authorize an egress, blocks the transmission, and mints a contradiction."
  - Diagram: the three parts run in sequence, P1 → P2 → P3. Only `P3 -->|"no: also mints a contradiction"| NO` mints the contradiction.
  - Why it matters:
    - The clause sets no order for the three parts.
    - The contradiction is minted whenever the record lacks a valid act, whatever the other two parts return.
    - In the diagram, a record that fails P1 or P2 and also lacks its act ends at "Refused" with no contradiction. That outcome is omitted in a misleading way, which fails criterion 4.
  - Fix:
    - Draw the three parts as parallel conjuncts feeding a single "all pass?" node.
    - Or add a separate edge: "consent record without a valid act → blocked, contradiction minted", independent of P1 and P2.
- **M2 — The RFC 0006 §0 overstates RFC6-22** (RFC-0006 §0).
  - New §0 text: "RFC6-22 (the equivalence definition every pair of renderings must satisfy)".
  - RFC6-22 is a definition: two renderings are "**equivalent** iff…".
  - RFC6-23 expressly allows a non-3D rendering to "expose **finer detail** than an aggregated 3D scene", provided the difference is disclosed. Such a pair differs in declared filters, so it is not equivalent under RFC6-22.
  - The obligation is RFC6-23's: "no pair of equivalent renderings may… disagree". The §0 turns a definition into a universal duty, so it fails criterion 3.
  - Fix: "RFC6-22 (the equivalence definition over which RFC6-23 forbids contradiction)", or name RFC6-23 as the weight-bearing clause.

**Notes**

- **N1 — RFC 0005 module-1 §0 wording.** "RFC5-11 makes revocation effective at the next act without disturbing RFC 0002's evaluations."
  - RFC5-11 also forces a new evaluation (owner decision B4).
  - The package Scope's wording is "without disturbing RFC 0002's evaluation **determinism**". Use that.
- **N2 — Consent-egress §0 list nesting.** "Either act may be state (1) or state (2)…" is a sibling bullet of the three check parts, so it reads as a fourth part. Move it out of the list of parts.
- **N3 — RFC 0007 README §2 (Doctrine grounding) opener.**
  - New text: "Polaris must become the owner's first stop without becoming either a document browser or a detached brochure…"
  - This fuses [Observed] content (the vision.md quote) with [Inferred] content (the two failures) in a sentence that carries no label.
  - The bullets below do distribute the labels correctly: [Inferred] is repeated on both bullets that it originally covered.
  - Fix: label the opener, or phrase it as a pointer rather than a claim.
- **N4 — RFC5-17 diagram placement.** The redaction diagram sits inside RFC5-17, ahead of the clause's own last paragraph ("A secret reproduced in any surface… trust-floor violation…"). That paragraph now reads as detached from the clause. The addendum says diagrams go after the clause.
- **N5 — RFC5-25 diagram.**
  - It draws all of `.syzygy/**` inside the untrusted write reach, with "Fleet worker —can write→" the governed tree.
  - The clause itself lists the two exclusions separately ("outside `.syzygy/**` and outside the untrusted actor class's write reach").
  - The premise matches the corpus: RFC 0005 README "the governed plane is writable by fleet workers", and RFC2 and RFC7 say the same. So the diagram is not wrong, but it asserts slightly more than RFC5-25 alone does.
- **N6 — RFC 0005 README module diagram.** The edge label "admits the principal; receives every audit record" on M1 → M2 and M1 → M3 reads backwards: audit records flow from modules 2 and 3 into module 1's trail. "Emits into its audit trail" on a reversed edge would be clearer.
- **N7 — RFC6-5 precedence formatting.** The inline "**1** `excluded` · … · **8** `resolved`" became a numbered Markdown list 1–8. Numbers and order are preserved; only the bold markup was dropped. Acceptable.
- **N8 — RFC7-11(a) code span.** The original broke `anchored — target changed since authorship` across a line. The draft joins it onto one line. This is a byte change inside a code span, but the rendered output is identical and it repairs a style-brief violation. Acceptable.
- **N9 — RFC5-5 wording.** "…never the owner's (RFC5-1) — and none is admitted by…" became a bullet list with "None is admitted by…". The "and" was dropped with no change of meaning. This and N7 are the only non-punctuation token changes in normative text outside the diagrams.
- **N10 — Mermaid not rendered.** No mermaid CLI is available, so the 13 blocks were checked by eye only.

**Checks run**

- **Unchanged file:** RFC-0007/rendering-and-surface.md is byte-identical. `cmp` passes and both sha256 values start `d4ab9646269e`.
- **Front matter:** identical in 8/8 files.
- **Preamble paragraphs:**
  - **Status:** identical in 8/8.
  - **Serves:** identical in 8/8.
  - **Package:** identical in the 5 files that have one; the other 3 have none in either version.
- **Headings:** the sequence is identical in all 8 files, 93 headings in total.
- **Clause leads** (regex from the addendum, compared through the closing `**`): identical set and order, 96 in total (0 / 15 / 6 / 6 / 28 / 0 / 26 / 15).
- **Italic parentheticals** (`*(…)*`, whitespace-normalized): 73 in total, all identical.
- **Fenced blocks:**
  - There were none in the originals.
  - 13 mermaid blocks were added (1 / 3 / 3 / 2 / 2 / 0 / 2), each preceded by the exact caption.
  - 12 of 13 sit after their clause; the exception is N4.
- **Code spans** (per section, multiset):
  - 0 lost in all sections of the 8 files.
  - Gains: 4 in the new RFC 0005 README note, 2 in the new RFC 0007 README guide, and the 1 rejoined span from N8.
- **Identifier tokens** (RFCn-m, VIS, SEC, SDR, CC, P, FD, "RFC nnnn"), per section: 0 lost in all sections. Gains occur only in §0, README openers and diagram captions.
- **Numbered items:** identical sequences in 8/8 files. RFC 0006 adds the 1–8 list noted in N7.
- **Lettered and roman items:** every original item survives in order in 8/8 files. There are 4 insertions, all from RFC3-16(a) or RFC7-11(a) cited in non-normative text or captions.
- **Broken code spans:** 0 odd-backtick lines outside fences, across the 7 changed files.
- **Line length:** 0 new prose lines over 80 columns outside tables and fences.
- **Bare `status` code span:** 0 in all 16 files (orig and draft).
- **Word-level diff** (list markers stripped, whitespace token streams, per section, all 7 changed files): every flagged place was read. Outside §0, README openers, non-normative sections and diagram captions, all normative-section changes are punctuation, capitalization or list structure, apart from N7 and N9.
- **Distribution check:** every list conversion was read for scope changes. All preserve "all of" / "either" / "each" distribution and keep qualifiers and [Inferred] / [Observed] labels on their original text. The conversions checked:
  - RFC5-1 (a)–(c); RFC5-3; RFC5-4; RFC5-5; RFC5-7 (a)–(d); RFC5-8; RFC5-15; RFC5-16; RFC5-17; RFC5-18 (a)–(e); RFC5-21; RFC5-22; RFC5-24; RFC5-25; RFC5-27;
  - RFC6-5; RFC6-14; RFC6-17; RFC6-19 classes (i)/(ii); RFC6-28;
  - RFC7-2 (a)–(c); RFC7-10; RFC7-18.
- **§0 and README clause maps:** the "where each clause lives" lists in the three RFC 0005 modules were checked by script against the actual section of each clause lead. All 27 RFC5 clauses are placed correctly.
- **§0 claims:** each clause named in a §0 as carrying the weight was checked against its text. The RFC5 modules and RFC7-2 / 3 / 11(a) match; the exceptions are M2 and N1.
- **Diagrams:** 13 of 13 read against their clauses. The two defects are M1, and N5/N6 at note level.
