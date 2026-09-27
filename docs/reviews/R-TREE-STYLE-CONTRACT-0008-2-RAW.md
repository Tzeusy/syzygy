Title: Contract readability restyle — RFC 0008 — review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: rfc-draft/RFC-0008/README.md, rfc-draft/RFC-0008/identity-authority-materialization.md, rfc-draft/RFC-0008/state-vocabulary-and-cost.md, rfc-draft/RFC-0008/accounting-reconciliation-and-release.md, each against its rfc-orig/RFC-0008/ counterpart, with review-0008-2/REPAIR-NOTES.md and review-0008-2/DIFF.txt
Reviewer: independent fresh-context agent

**Round-1 findings**

- **M1: RESOLVED.** The added opener sentence is gone.
  - §2 now opens with the original first sentence, word for word: "Doctrine keeps desired, observed-implementation, and execution state semantically distinct, and rules that scheduled or completed work is never proof intent is satisfied [Observed: vision.md, Thesis]."
  - The last bullet reads: "[Inferred] **Three failure modes are guarded against**, each individually attractive to an implementer and each manufacturing exactly the comprehensible fiction VIS-1 forbids:".
  - The label again leads and covers exactly the text of its original paragraph.
  - The "exists because" causal claim no longer appears anywhere.
- **M2: RESOLVED.** A script confirmed that all four paragraphs match `rfc-orig` byte for byte, from their first character through the label:
  - RFC8-7 "Capturing that a withdrawal…" (ends "…nothing here licenses that loss. [Inferred]");
  - RFC8-12 separate-field paragraph (ends "…README §5 restates it for orientation. [Inferred]");
  - RFC8-21 (ends "…complete and weak. [Inferred]");
  - RFC8-25 "Small" (ends "[Inferred — left undeclared and permissive, … argument in history.]").
- **N1: RESOLVED.** The draft now reads "…lists "`gate-backed` on retention and format alone" as Rejected): a preserved hash with no capture artifact and no other satisfied route **caps at `report-fact`**, with the cap visible." Then comes a separate top-level bullet: "- An artifact simply **gone** drops tier in the next evaluation with the dangling reference rendered broken."
- **N2: RESOLVED, all four.**
  - "It is joined on" is gone; "— joined on the RFC1-25 relations" is restored.
  - The "**Six values, closed.**" paragraph matches the original byte for byte ("— the closure RFC8-12 cites this clause for").
  - "The substrate-to-normalized mapping is a **declared, versioned derivation artifact**" is no longer bold.
  - "- Preserved summaries render at their recorded tier:" is no longer bold.
- **N3: RESOLVED.**
  - Identity: "**Relies on RFC 0001:**", "**Provides to RFC 0007:**" and "**To RFC 0010:**".
  - State: "**Provides to RFC 0009:**" and "**To RFC 0010:**".
  - Accounting: "**Provides to RFC 0009:**", "Also to RFC 0009: the touched-components measure's dependence…", "**To RFC 0010:**" and "**To RFC 0011:**".
  - The lost "RFC 0009" token is back, and the token check shows 0 lost.
- **N4: RESOLVED.** RFC8-20 is back as one paragraph, byte-identical to the original ("…absent fields Unknown. **Deferred entirely**: … nothing at V0 may simulate telemetry.").
- **N5: RESOLVED (caption).** The caption now reads "…; it shows only those rows, not RFC8-16's Unknown for worker liveness between signals." See N-b below for a small wording tension.
- **N6: RESOLVED (caption).** The caption now reads "…a change exceeding a declared threshold is not drawn."
- **N7: RESOLVED, all three parts.**
  - The outcome node is `COV["Covered"]`.
  - The N/A node now includes "state (1) or (2),<br/>with that state rendered?".
  - The caption now reads "before implementation work for user-observable Trajectory behavior may be scheduled."
- **N8: RESOLVED.** Both solid edges now read `-- "reading order" -->`. The caption says "every edge is reading order, not dependency, and modules 2 and 3 are each independently readable given module 1". That matches README line 80: "Modules 2 and 3 are independently readable given module 1."
- **N9: RESOLVED** by the M1 fix. The "rules that" wording is back and the "Doctrine." bullet is gone.
- **N10:** no action was needed, and none was taken.

**Material findings**

None. Every hunk in DIFF.txt restores original text or rewords a caption or diagram node to say less. I found none of these kinds of drift in the diff:
- a qualifier moved away from its rule;
- SHALL, MUST, never or only softened or strengthened;
- a scope widened or narrowed;
- an epistemic label covering more or less text than before;
- a list redistributed;
- a diagram asserting more than its clause.

The two extra restorations are also byte-identical to the original:
- README "Module sizes are deliberately **not stated here**…", back in its original place after the table;
- README §5 "Stated as **two fields**…".

**Notes**

- **N-a: conjunctions dropped by list conversion.** These are outside DIFF.txt, left from round 1, and found by my word diff. Three "and"s were removed where one sentence became two bullets:
  - accounting RFC8-32 "Why the judgment is gated at all." Original: "…(SEC-3, as RFC3-16(a) extends it to committed artifacts), and an N/A judgment that class could commit is the one artifact…". Draft: two bullets with no "and".
  - README "Phase boundary". Original: "…§3.16, and its clause-to-requirement coverage matrix must cover…". Draft: "- The clause text is in … §3.16." followed by "- Its clause-to-requirement coverage matrix must cover…".
  - README §5 "Provides to", in the RFC 0010 list: "…, and RFC8-30's prohibition" became a bullet.

  None changes meaning; in each case the two parts still read as a conjunction. The RFC8-32 one is the closest to paraphrase, because the "and" joined a premise to its conclusion. Restoring it is a single-sentence edit.
- **N-b: the RFC8-16 caption says "it shows only those rows".** The diagram also draws RFC8-16's own "never admissible as signal" edge. The caption does begin "decided under RFC8-16 and the RFC8-13 rows", so this is only loose wording. It asserts nothing false.
- **N-c: README §2 (non-normative) drops "lived".** "The lived failure this surface ends is…" became "**The failure this surface ends.**". This is allowed in a non-normative section, and the label is still attached.
- **N-d: four `[Observed…]` labels end a paragraph in the original but sit inside the final sentence's period.** They are in RFC8-16, RFC8-18 (Genome-complete note), RFC8-19 and RFC8-27. In the draft each still ends that same whole sentence, now in a bullet or a split paragraph. Each label's content is specific to its sentence. I agree with the repair's reading that these labels cover a sentence, not the paragraph, so I raise no finding.

**Checks run** (my own scripts are in the scratchpad: `r8v2_frozen.py`, `r8v2_labels.py`, `r8v2_restored.py`, `r8v2_wd.py`, `r8v2_paras.py`)

- **Front matter** byte-identical: 4/4.
- **Preamble paragraphs** (Status, Date, Package, Serves) byte-identical: 12/12.
- **Headings** outside fences, same text, level and order: 47/47.
- **Clause leads** (the brief's regex, through the first `.**`), same order: 32/32 (0 + 11 + 9 + 12).
- **Item numbers and letters** ((a), (1), "item N", numbered-list starts), same sequence: 84/84, with none added.
- **Italic parentheticals** `*(…)*`, including those ending `.*`: 18/18 kept. My regex catches one more than round 1's 17, because it also matches the `).*` form of "*(ruled at acceptance…)*".
- **Code spans** (whitespace-normalized multiset): 277 in the originals, 0 lost.
  - 9 added: `n`, `RFC8-n`, `reconciled` and `reconciled@E` in the README opener and captions; `materialized` in the identity §0 and a caption; `active`×2, `activity-undetermined` and `stale-or-dead` in the state §0 and a caption.
  - None is a bare `status`.
- **Code spans broken across lines:** 0 lines with an odd backtick count, over 1,806 non-fence lines.
- **Links:** 0 in the originals, 0 in the drafts.
- **Identifier tokens** (RFCn-m with limb, RFC NNNN, VIS, SEC, SDR, CC, A/B codes, q-numbers, *.md paths), checked per heading section: 784 occurrences, 0 lost.
- **Mermaid:** 8 blocks, 8/8 preceded by the required non-normative caption.
- **Mutation test (rule 6)** on a scratch copy: 7/7 mutants were caught. They covered a clause-lead title change, a parenthetical edit, a code span broken across a line, a limb letter removed (caught both as item order and as a lost token), and "Also to RFC 0009:" removed (caught as a lost token). I then deleted the scratch copy.
- **Restored paragraphs:** 8/8 byte-identical to the original (M2 ×4, RFC8-20, Six values, README two-fields, README module sizes). The README §2 opener matches the original paragraph's first sentence exactly.
- **Epistemic labels:** 19 in the originals and 19 in the drafts, in the same sequence in every file (5 + 3 + 6 + 5).
  - For every label, the 60 characters before it are still in the same draft block: 19/19.
  - 8 are paragraph-final in the original. The 4 standalone `[Inferred]` ones sit in paragraphs that are byte-identical. The other 4 are the sentence-internal `[Observed]` labels in N-d, which I read by hand.
- **Word-level diff of normative sections** (list markers, emphasis and edge punctuation ignored, §0, reader-map and non-normative sections excluded):
  - The README's untitled top section inserts the package-opener summary, which the addendum allows in a package README.
  - Otherwise, 3 deleted "and"s (N-a) and nothing else.
- **DIFF.txt:** all 479 lines and 19 hunks, read against `rfc-orig`.
- **Line length:** 0 draft lines over 80 columns outside front matter, tables and Mermaid that are not also in the original.
