Title: Contract readability restyle — RFC 0008 — review 1
Verdict: REVISE
Reviewed: rfc-draft/RFC-0008/README.md, rfc-draft/RFC-0008/identity-authority-materialization.md, rfc-draft/RFC-0008/state-vocabulary-and-cost.md, rfc-draft/RFC-0008/accounting-reconciliation-and-release.md, each against its rfc-orig/RFC-0008/ counterpart
Reviewer: independent fresh-context agent

**Material findings**

- **M1 — README §2: an Inferred claim is restated with no label.**
  - Old: "[Inferred] Three failure modes are guarded against, each individually attractive to an implementer…"
  - New: the new section opener says "The surface exists because doctrine separates the three state planes and rules that work is never proof; three tempting failure modes would break that." The labelled claim is then repeated under "**Three guarded failure modes.** [Inferred] Each is…"
  - Why it matters: the opener states the inferred claim as plain fact. It also adds a causal claim ("exists because") that the original did not make. Labels must stay attached to the claims they label.
  - Fix: end the opener's second clause with "[Inferred]", or cut it and open with the doctrine sentence only.

- **M2 — Four paragraphs ending in "[Inferred]" were split into bullets, so each label now visibly covers one bullet.** The text just before each label is unchanged. But in the original, each label closed a whole paragraph and could be read as covering all of it. That is the scope change acceptance criterion 1 forbids.
  - RFC8-21 is the clearest case. The claim most in need of a label is the factual one, "**Against today's actuator toolchain this chain is honest but thin**: several links resolve only by naming convention…". It is now bullet 2, while "[Inferred]" sits at the end of bullet 3, the normative "must render as thinness".
  - RFC8-25: "[Inferred — left undeclared and permissive, 'small' is decided by the worker…]" gives the reason for the whole fail-closed rule. It is now confined to the "Size, count, and scope-breadth bounds…" bullet.
  - RFC8-12 (state-vocabulary-and-cost.md): "…README §5 restates it for orientation. [Inferred]" now covers only bullet 3 of the separate-field paragraph.
  - RFC8-7, the "Capturing that a withdrawal…" paragraph (identity-authority-materialization.md): "[Inferred]" now covers only the second bullet.
  - Fix: leave these four paragraphs as unsplit prose. The alternative is to move each label so it provably covers the same text as before.

**Notes**

- **N1 — RFC8-27 (accounting): a colon now covers one more sentence.** "An artifact simply **gone** drops tier…" was a separate sentence after the colon clause. It is now a sub-bullet under "Artifact resolvability alone is still not the test (…):". It still reads coherently as resolvability being necessary but not sufficient, but the grouping is new. It would be safer as its own top-level bullet.
- **N2 — Small wording changes inside normative sections.**
  - Words added to turn phrases into sentences:
    - "— joined on" became "It is joined on" (RFC8-21).
    - "— the closure RFC8-12 cites" became "This is the closure RFC8-12 cites" (RFC8-28/29).
  - Bold emphasis added to text that was not bold, so it now looks like a clause lead:
    - "**The substrate-to-normalized mapping**" (RFC8-12).
    - "**Preserved summaries render at their recorded tier:**" (RFC8-27).
  - None changes meaning. Each is slightly more than pure restructuring.
- **N3 — §5 "Relies on" and "Provides to" labels reworded.**
  - The labels were regrouped: "**Relies on RFC 0001:**" became "**Relies on:**" with "- **RFC 0001:**" nested under it, and "**To RFC 0010:**" became "**RFC 0010:**".
  - In accounting, "Also to RFC 0009:" became "also" nested under RFC 0009. This is the one lost "RFC 0009" token.
  - Scope is equivalent. §5 is not marked non-normative, so this is a relabelling, not pure restructuring.
- **N4 — RFC8-20 bullets sit under the V1 lead.** The "**Deferred entirely**" and "**V0** renders…" bullets now hang under the V1 lead sentence. Each names its own scope, so nothing is misread, but the nesting suggests they are part of V1.
- **N5 — RFC8-16 diagram (liveness) leaves out two cases.** It omits "Between signals, worker liveness renders **Unknown**", and it has no path for a claimed item with a declared bound that has never had any signal. The clause does not settle the second case either, so the diagram asserts nothing false. Consider saying in the caption that it shows only the RFC8-13 rows.
- **N6 — RFC8-25 diagram (inherited mutations) has an unlabelled gap.** The edge "yes, and within it" implies another branch, "declared but exceeded", which has no edge. Add a branch saying it is outside this clause, or reword the caption.
- **N7 — RFC8-32 diagram (coverage) is slightly off in three places.**
  - It labels the outcome "Covered — a row of the clause-to-requirement coverage matrix", but the clause says the matrix is "review material, never authority". The mapping is what covers, not the row.
  - The node for the reviewed N/A judgment leaves out "with that state rendered".
  - The caption leaves out the "user-observable Trajectory behavior" scope.
- **N8 — README module diagram edges are unlabelled.** The solid M1→M2 and M1→M3 edges can be read as dependency edges. Module 3 also cites module 2 (RFC8-28 relies on RFC8-12), and that link is shown only as a dotted "reading order" edge. This matches "independently readable given module 1", but labelling the solid edges "reading order" too would avoid the dependency reading.
- **N9 — README §2 "Doctrine." bullet drops "rules that".** "Doctrine … rules that scheduled or completed work is never proof" became a bare assertion under a "**Doctrine.**" lead. The [Observed: vision.md, Thesis] label is still attached. The attribution now comes only from the lead.
- **N10 — The §0 reader maps and README opener are otherwise accurate.**
  - The clauses each names exist and carry the weight claimed: RFC8-12, RFC8-16 and RFC8-18; RFC8-2(a), RFC8-7, RFC8-8, RFC8-10 and RFC8-11; RFC8-22, RFC8-25, RFC8-27, RFC8-28 and RFC8-32.
  - The lookup rule as stated in the README opener matches the clause map.
  - The module 3 opener says the module decides "at what cost". That echoes the original reader question, but the cost measures themselves are in module 2 (RFC8-18).

**Checks run**

- Front matter byte-identical: 4/4 files.
- Preamble paragraphs byte-identical: 12/12 (README Status, Date and Serves; Status, Package and Serves in each of the 3 modules).
- Headings: 47/47, same text, level and order (10 + 12 + 11 + 14).
- Clause leads (the brief's regex): 32/32, same order (0 + 9 + 11 + 12). Leading bold runs: 33/33, same order.
- Code spans: 277 in the originals, 0 lost. 9 added, all in §0, the README opener or diagram captions, and none is a bare `status`. Draft lines with an odd backtick count (a code span broken across a line): 0 of 1,921.
- Links: 0 in the originals, 0 in the drafts.
- *(…)* italic parentheticals: 17/17 unchanged (2 + 6 + 4 + 5). None is a History or Amended parenthetical.
- Fenced blocks: 0 in the originals. 8 Mermaid blocks added, 8/8 captioned with the required non-normative line, each placed after its clause or in a non-normative or README section.
- Item numbers and letters ((a)–(c), (1)–(3), "item N", numbered list starts): 84/84, same order across the 4 files.
- Identifiers (RFC, VIS, SEC and SDR IDs, RFC numbers, A/B decision codes, q-numbers), per section and as a whole: 0 lost apart from one "RFC 0009" (see N3). Additions are confined to §0 and captions.
- Epistemic labels: for each of the 19 original [Observed/Inferred/Unknown] labels, the 40 characters before it are still present before it in the draft: 18/19. The exception is the README [Inferred] (M1). Paragraph scope was reviewed by hand for all 4 trailing [Inferred] labels (M2).
- Word-level diff with list markers dropped: 149 flagged changes (55 + 23 + 33 + 38), every one read in context.
- Every diagram was compared by hand with its clause: 8/8.
- Lines over 80 columns: 32, all in front matter, Mermaid blocks or unchanged frozen text, except one 81-column line in README §5 and one in RFC8-17 (cosmetic).
