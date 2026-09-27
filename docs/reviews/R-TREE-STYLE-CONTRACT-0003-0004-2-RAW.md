Title: Contract readability restyle — RFC 0003 and RFC 0004 — review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: rfc-draft/RFC-0003/{README.md, manifests-and-namespace.md, governance-homes-and-owner-acts.md}; rfc-draft/RFC-0004/{README.md, general-contract.md, named-adapters.md, execution-record.md, fidelity-joins-and-mappings.md}, each compared with its rfc-orig counterpart, plus review-0003-0004-2/{REPAIR-NOTES.md, DIFF.txt}
Reviewer: independent fresh-context agent

The five material findings from round 1 are resolved. The repair introduces no new drift in meaning. What remains is three cosmetic notes, so there are no new material findings.

**Round-1 findings**

- **M1: RESOLVED.** The consent edge now reads "required for observation<br/>(necessary, not sufficient)". The read edge now ends on a new node, `AE["A's evaluations<br/>(data about B)"]`, which sits outside the `AR` subgraph.
  - "Not sufficient" is backed by the clause's own text: R must also be "a declared observed-source repository".
  - `AE` matches "data about B … never a snapshot input to A's evaluations in the policy-version role". The edge carries "never governing policy for A".
- **M2: RESOLVED.** The route-3 edge now reads "3 scoped, unexpired oracle policy<br/>with an effective owner act (RFC3-16(a))".
- **M3: RESOLVED.** The draft now reads "…capture are **optional enrichment**:" followed by one bullet ending "…deferred entirely)." The free-standing paragraph "Multiple runs against one work item are distinct records — redispatches and attempts are countable only from records, never inferred from a mutation trail." follows it. After normalizing whitespace, both passages are identical to the original.
- **M4: RESOLVED.** The draft now reads "hold, exclusively — "exclusively" bounding what each category may contain, and the five-category set itself being closed except by the two lawful widenings this RFC records:". The two bullets that follow are "the owner amendment that minted `records/` (B19, RFC3-15(a)) and" and "the **reservation** of `declarations/` at RFC3-17, …". With list markers stripped, this is token-identical to the original. "What the table below assigns them" is gone.
- **M5: RESOLVED.** "What does not mint a record:" is deleted. The draft reads "**Owner resolution acts** — … never minted into `records/`. **Kernel-computed expiry *eligibility*** — … the *eligibility* mints **no record**, … that pure recomputation created." This paragraph is identical to the original, including the semicolon.
- **N1: RESOLVED.** The draft reads "- **(1) an actor's submission** — …;" and "- **(2) the pre-declared deterministic challenge-sweep policy …**". The (1)/(2) markers are back inside the bold, as in the original.
- **N2: RESOLVED.** Route 4, the unverifiable-origin paragraph ("A retained, well-formed, … oracles Syzygy cannot itself confirm.") and the RFC4-20 derivation-collision paragraph are each identical to the original after normalizing whitespace. That was checked by script, over 1,122 characters for the unverifiable-origin paragraph. Each `[Inferred]` is back to its original position in the sentence.
- **N3: RESOLVED.** Both files now close with one paragraph: "This clause creates no OpenSpec content now (none may exist during bootstrap). This clause binds the whole RFC 000[34] package, not this module alone. (Shape-parallel with …)". The two files use the same form, and the text is identical to the original.
- **N4: RESOLVED.** The draft reads "- approximated run boundaries." and then "Everything else renders Unknown with its reason …". Only punctuation and case changed.
- **N5: RESOLVED.** The draft reads "Doctrine and RFC 0002 route facts through typed adapters, durable evidence and versioned snapshot inputs; [Inferred] this contract applies that …". This is in a non-normative section, and the bullets beneath cite RFC2-1 and RFC2-2.
- **N6: RESOLVED.** The node now reads "binding RFC3-16(b) items 1–9<br/>(item 9 decides the state)". See note N-b.
- **N7: RESOLVED.** The node now reads "Marker-adoption policy for that project<br/>with an effective owner act<br/>under RFC3-16(a)?". This matches "adopted marker-sourced declarations for that project".
- **N8: RESOLVED.** The draft now reads "these adapters must satisfy the general contract" and "observers producing these records must satisfy the general contract".
- **N9a: RESOLVED.** The caption now reads "*Diagram (non-normative; the clauses govern):* the same edges as the list above, adding nothing to it."
- **N9b: RESOLVED.** The sentence now stands as its own closing paragraph, beginning "This section is navigational …". In the original, that paragraph was the entire section, so "section" and "paragraph" cover the same text and the scope is unchanged.
- **N9c and N9d: declined by the repairer.** I accept both reasons. The "A one-off capture…" sentence sits inside the *Reads:* segment in the original. The "On"/"To" words are carried by the list leads.

**Material findings:** none.

**Notes**

- **N-a:** RFC4-20 now has a list with a single bullet: "…**optional enrichment**:" followed by one "- their absence never blocks a record, …". Meaning is preserved. For readability, a plain running sentence would be better than a one-item list.
- **N-b:** In the RFC3-16(c) diagram, "(item 9 decides the state)" slightly compresses the rule. State (1) also requires trusted-bootstrap to be explicitly chosen in the act. The edge label says this ("item 9 explicitly absent; trusted-bootstrap chosen in the act"), and the caption defers to the clauses, so this is not material.
- **N-c (not introduced by this repair; for awareness only):** in RFC4-15, the paragraph-ending bare `[Observed]` now sits on the last *Degraded modes* bullet, "replace-in-place note fields …". Reading it as covering that sentence only is consistent with the original. The repair notes list it the same way.

**Checks run** (scripts in scratchpad `rv2-34/`)

- **Diff integrity:**
  - I re-generated `diff -ru` from `review-0003-0004-2/before/` to `rfc-draft/`. It matches DIFF.txt apart from header paths: 16 hunks over 7 files, and `general-contract.md` is unchanged.
  - I read all 16 hunks against `rfc-orig`, checking for:
    - qualifiers detached from their rule: none;
    - SHALL/MUST/never/only softened or strengthened: none. The two "must" edits restore the original;
    - scope widened or narrowed: none;
    - list distribution: M3 and N3 are restored, and RFC3-15 splits only at the original colon;
    - label reach: none changed;
    - diagrams asserting more than their clause: none.
  - Every hunk except the RFC3-16(c) diagram node and the README-caption hunks either restores original wording or changes only punctuation and case (RFC4-28).
- **Restored-passage identity** (`verb.py`): 8 passages, 8 identical to the original after normalizing whitespace and list markers.
- **Epistemic labels** (`labels_end.py`):
  - The population is 48 labels over 8 files.
  - 8 of them end a paragraph in the original.
  - 2 of those paragraphs are unchanged: the RFC3-16(c) bracket and RFC4-25.
  - 5 were split into a lead, bullets and a closing label line. I read each one, and each label still covers the same text with nothing inserted: RFC3-14 collision, RFC3-16(b) bootstrap, RFC3-17(a) consequences, RFC4-13(a) snapshot, and RFC4-13(b) separation.
  - 1 is sentence-scoped and still attached to the same sentence (RFC4-15; see N-c).
- **Frozen elements** (`frozen.py`, 8 files):
  - front matter identical in 8/8;
  - Status identical in 8/8, Package in 6/6 and Serves in 7/7;
  - clause leads 70/70, same sequence (0/30/8/0/9/10/4/9);
  - headings 76/76, same order;
  - History/Amended parentheticals 1/1;
  - links 0/0;
  - code spans: 403 in the originals, 0 lost. 7 were added, all in non-normative text or captions, and they are the same 7 as in round 1;
  - numbered and lettered items: 118 markers, same sequences in 8/8;
  - lines with an odd backtick count in the drafts (a broken span): 0;
  - new bare `status` spans: 0;
  - fences: 0 in the originals and 12 Mermaid blocks in the drafts.
- **Rule-6 mutation of `frozen.py`:** 4 of 4 mutants were detected:
  - an altered lead;
  - an altered code span;
  - a renumbered item;
  - an altered Status line.
- **Line length:** 3 added lines exceed 80 columns (added lines checked over all 16 hunks). All 3 are inside Mermaid fences.
- **Mermaid:** the 5 changed `.mmd` sources are byte-present in the drafts (5/5, out of 12 blocks in the group). The 5 rendered SVGs contain 0 "Syntax error" strings. I did not re-render them, because `mmdc` is not installed.
