Title: Contract readability restyle — RFC 0001 and RFC 0002 — review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: rfc-draft/RFC-0001-project-graph-identity-state-planes.md; rfc-draft/RFC-0002/README.md; rfc-draft/RFC-0002/snapshot-and-evaluation-core.md; rfc-draft/RFC-0002/challenge-lifecycle.md; rfc-draft/RFC-0002/reconciliation-chain.md; rfc-draft/RFC-0002/rendering-vocabularies.md. Each was compared against the same path under rfc-orig/, using review-0001-0002-2/DIFF.txt and REPAIR-NOTES.md.
Reviewer: independent fresh-context agent

**Material findings**

None.

**Status of the round-1 findings**

- **M1: RESOLVED.**
  - Clause RFC2-8 (unchanged): "it may never establish, raise, or independently satisfy a positive status claim."
  - Diagram edge now: `never establish, raise or independently satisfy a positive status claim`.
- **N1: PARTIAL.** The repair accepts this change and does not revert it.
  - The draft still carries the span on one line: `` `merged → reconciliation-pending → (reconciliation evaluation) → reconciled@E | unsatisfied | contradiction-raised | Unknown(reason)` `` (reconciliation-chain.md:143).
  - The only change is whitespace, and it repairs a span the original broke across lines. It remains a change to a byte-frozen code span, so the owner still needs to accept it explicitly.
- **N2: RESOLVED.**
  - The whole RFC2-15 paragraph is now byte-identical to the original: "…routes to owner adjudication, is never resolved by precedence, never auto-scheduled into work."
- **N3: RESOLVED.**
  - The RFC2-26 opening paragraph is byte-identical to the original: "No implementation work for user-observable consequences of this contract — evaluation and snapshot displays, … API answers over epistemic state — may be scheduled solely from this RFC."
  - Only the "Before implementation, every observable consequence either" pair is a list. Each branch keeps its own verb: "- maps to …," and "- or carries …".
- **N4: NOT RESOLVED, by the repair's choice.** RFC2-10 still splits "**Four values, closed.**" into its own paragraph. The nested list is followed by "— a value existing in no vocabulary…". The meaning is preserved, and the `[Observed — architecture.md.]` label still covers exactly the text before it.
- **N5: NOT RESOLVED, by the repair's choice.**
  - The draft has "- §3 is the contract (RFC1-1 … RFC1-32):" at line 108, and "§3.11 the OpenSpec authority boundary — RFC1-33" beneath it at line 119.
  - This mismatch existed before the restyle, in a non-normative section.
- **N6: NOT RESOLVED, by the repair's choice.** The RFC 0002 captions are 86–90 columns wide. See N4 below.

**New drift in the DIFF.txt hunks**

I read all 12 hunks against rfc-orig.

- 10 of the 12 hunks restore the whole original paragraph, byte for byte. Checked by script: the paragraph is identical in rfc-orig and rfc-draft.
  - RFC1-1's governance-root count paragraph.
  - RFC2-3, RFC2-4, RFC2-6, RFC2-9, RFC2-12, RFC2-15 and RFC2-16.
  - RFC2-13's "Expiry is eligibility" and "A sweep policy is required" paragraphs.
  - RFC2-21.
  - RFC2-24's secondary-annotation paragraph.
- The other two hunks are the RFC2-26 restoration (N3 above) and the M1 edge change.
- I found none of the following:
  - a detached qualifier;
  - SHALL/MUST/never/only softened or strengthened;
  - a scope change;
  - a change in list distribution;
  - a diagram asserting more than its clause.

**Notes**

- **N1. RFC2-13's `challenge-pending` label is handled inconsistently with the repair's own criterion.**
  - Original: the paragraph ends "…`rejected` clears the disclosure with the rejection record standing. [Inferred — the name and its categorisation are this RFC's; the rendering obligation is the clause's original text.]"
  - Draft: the label sits alone on its own line after a nested list, and the bold lead "**Declared bounds and policies are authorization-bearing.**" follows it.
  - The repair restored 12 paragraphs because a label "sat on its own line where it read as leading the next sentence". This one has the same shape but was kept.
  - The label's own wording ("the name", "the rendering obligation") pins its span to the whole paragraph, so the meaning survives. Restoring the original paragraph would make the treatment consistent.
  - Twenty lines later, "[Inferred — the split's justification.]" is also a label alone on a line, but that one is correctly a leading label in both versions. Two "alone" labels with opposite directions in one file is the ambiguity the repair set out to remove.
- **N2. README §2 (non-normative): an ambiguous bare label was resolved in one direction.**
  - Original: "…inference holding challenge authority only (trust-and-evidence.md). [Observed] What doctrine deliberately leaves to RFCs…". This can be read either as trailing the first sentence or as leading the second.
  - The draft makes it lead the second bullet, which leaves the "What doctrine already commits Syzygy to" list unlabelled.
  - This matches how the package uses a leading `[Observed]` elsewhere, for example §1's "[Observed] No surveyed substrate…". The section is non-normative, so this is not material.
- **N3. REPAIR-NOTES.md contradicts itself.** It says "**No change to RFC 0001.**", but DIFF.txt and the label section of the same notes show that RFC1-1's `[Inferred]` paragraph was restored. The restored paragraph is byte-identical to the original, so the result is correct; only the statement is wrong.
- **N4. The caption rationale for round-1 N6 does not hold across the group.**
  - The repair says each caption must be on one line.
  - The three RFC 0001 captions (lines 158, 520, 802; 68–76 columns) each wrap over two lines.
  - The six RFC 0002 captions are single lines of 76–90 columns. Five of them run past about 78 columns: README 121 (88), reconciliation 231 (90), rendering 247 (88), and snapshot 146 (87) and 201 (86).
  - This is cosmetic.
- **N5. The diagram edge cites RFC2-12 for "propose or challenge only (RFC2-12)".** The clause cites RFC2-12 for challenge alone. This existed in round 1, is not new, and is not material.

**Checks run**

All checks are Python scripts under `scratchpad/rv2/`.

- **Front matter:** byte-identical in 6 of 6 files.
- **Preamble:** 18 of 18 paragraphs byte-identical (6 Status, 6 Serves, 3 Date, 3 Package).
- **Clause leads:** the bold lead strings `^\*\*RFC\d+-\d+…` are identical in order, 67 of 67 (RFC 0001: 39; RFC 0002: 0, 3, 9, 5 and 11 across README, challenge, reconciliation, rendering and snapshot). Round 1 counted 65 with a narrower regex; the two sequences are equal either way.
- **Headings:** 64 of 64 `#` headings identical in order (19, 11, 6, 9, 9, 10).
- **Item order:** 163 of 163 tokens match in sequence in every file. The tokens are `(a)`, `(i)`, `(1)`, `item N`, `items N–M` and `#N`, taken after whitespace normalization and outside fences.
- **Parentheticals:** all `*(…)*` italic parentheticals are identical in sequence, 36 of 36 (15, 3, 3, 8, 4, 3). The narrower History/Amended/added/ruled set is 3 of 3.
- **Code spans:**
  - 282 original spans; 0 lost after whitespace normalization.
  - 4 spans added, all in non-normative prose: `RFC2-n` twice, `admitted` once, `gate-backed` once.
  - 1 span changed bytes (the reconciliation chain span; see round-1 N1).
- **Broken code spans:** 0 non-fence lines with an odd backtick count, over 2,732 draft lines.
- **Links and fences:**
  - Links: 0 in the originals, 0 in the drafts.
  - Original fences: 0.
  - Mermaid blocks in the drafts: 9. Each has the required caption.
- **Epistemic labels:**
  - The label sequence is identical in all 6 files, 60 of 60 (21, 5, 7, 10, 6, 11).
  - 27 labels end a paragraph in the original. For 24 of them, the whole normalized paragraph is identical in the draft.
  - I read the other 3 by hand:
    - RFC 0001 §1 doctrine grounding: per-item inline labels, and the `[Inferred]` paragraph is unchanged.
    - README §2: see N2.
    - RFC2-13 `challenge-pending`: see N1.
  - A second pass compared every label's position (start, middle, end, alone) and its neighbouring text. 9 of 60 differ, and I read all 9. The other 6 are:
    - two RFC 0001 labels in the non-normative §1 doctrine-grounding list;
    - README §1 `[Observed]`, still leading "No surveyed substrate…";
    - the leading label on the split justification, now leading its list;
    - the non-normative reconciliation "What is new here" bullet;
    - RFC2-10's trailing label, with unchanged text before it.
  - None of them changes the span in a normative section.
- **DIFF hunks:** each hunk's new side was located in rfc-orig. 7 matched directly. For the rest I compared paragraphs, and every normative paragraph came back byte-identical except RFC2-26, which I read by hand (identical opening paragraph, list below it).
- **Mutation self-test (rule 6):** each predicate was run against a mutated copy of the drafts and failed as it should. The mutations were:
  - clause lead;
  - code span, which tripped the span and broken-line checks;
  - front matter;
  - preamble;
  - heading;
  - item letter;
  - parenthetical;
  - label split, which dropped the identical-paragraph count from 24 to 23.
