Title: Contract readability restyle — RFC 0003 and RFC 0004 — review 1
Verdict: REVISE
Reviewed: rfc-draft/RFC-0003/{README.md, manifests-and-namespace.md, governance-homes-and-owner-acts.md}; rfc-draft/RFC-0004/{README.md, general-contract.md, named-adapters.md, execution-record.md, fidelity-joins-and-mappings.md}, each compared with its rfc-orig counterpart
Reviewer: independent fresh-context agent

**Material findings**

M1. The RFC3-30 diagram (manifests-and-namespace.md) turns a necessary condition into a sufficient one, and implies a write into A's plane.
- Clause: "Project A observing repository R **requires** A's own consent record for R".
- Diagram: `CON -->|"permits observation"| BT`. "Permits" reads as sufficient.
- Also, `BT -->|"read-only; data about B…"| AR` ends on the subgraph whose node is "A's whole direct-write universe". That suggests B's content lands in A's plane. The clause says it is only read, and is never a policy-role snapshot input.
- Fix: relabel the edge "required for observation (necessary, not sufficient)". Point the read edge at a separate node such as "A's evaluations (data about B)", outside the A-root subgraph.

M2. The RFC4-13 diagram (named-adapters.md) drops a necessary condition from route 3.
- The edge label says "3 scoped, unexpired oracle policy".
- The clause makes that policy "authorization-bearing and therefore honored only under RFC3-16(a)".
- As drawn, scope and expiry alone look sufficient for `gate-backed`.
- Fix: "3 scoped, unexpired oracle policy with an effective owner act (RFC3-16(a))".

M3. A list conversion in RFC4-20 (execution-record.md) changes what the colon distributes over.
- Old: "…capture are **optional enrichment**: their absence never blocks a record, … deferred entirely). Multiple runs against one work item are distinct records — …"
- New: "…capture are **optional enrichment**:" followed by two bullets, the second being "multiple runs against one work item are distinct records — …"
- The distinct-records rule was a free-standing sentence. It now reads as a sub-property of enrichment being optional.
- Fix: keep the first bullet, and restore "Multiple runs against one work item are distinct records — …" as its own paragraph after the list, with a capital M.

M4. RFC3-15 (governance-homes-and-owner-acts.md) is paraphrased inside the constitutional clause, which is not restructure-only.
- Old: "hold, exclusively — "exclusively" bounding what each category may contain, and the five-category set itself being closed except by…"
- New: "hold, exclusively, what the table below assigns them:", then "- "exclusively" bounds …; - the five-category set itself is closed except …"
- It adds a new referent ("what the table below assigns them"). It also turns two participial glosses into independent assertions.
- No change in outcome is evident, but this is the most-cited homes clause and new words there read as rule.
- Fix: restore the original sentence. If a list is wanted, split only at "the two lawful widenings this RFC records:", keeping "bounding" and "being".

M5. RFC3-2 (manifests-and-namespace.md) gains a new sentence inside a normative clause: "What does not mint a record:". It introduces the owner-resolution-acts and eligibility bullets.
- The content is consistent with the clause, which already says "exactly **two triggers**, and no others".
- But it is a new normative-reading summary line, which the addendum forbids.
- Fix: delete the line. Let the two bullets follow the numbered list directly, or leave them as the original's running sentences.

**Notes**

N1. The RFC3-2 transition-rule items were rewritten from "**(1)** …; **(2)** …" to a Markdown "1." / "2." list.
- The numbers and order are preserved, but the item form changed.
- `git grep` for `RFC3-2 (1|2)` and `RFC3-2 item` outside `round-*` found no citers.
- Consider keeping the "(1)"/"(2)" form, to match the frozen-item rule.

N2. Bulleting now bounds some `[Inferred]` labels to exactly one bullet, where before their paragraph-internal reach was ambiguous. Places:
- RFC4-13 route 4 ("[Inferred] Determinism and re-runnability…");
- RFC4-13 unverifiable-origin ("[Inferred] Format, retention…");
- RFC4-20 ("[Inferred] This is SDR-6's…").

I read each as sentence-scoped in the original too, so there is no change. Flagged for the owner's awareness.

N3. RFC3-33 and RFC4-30 put "This clause creates no OpenSpec content now" and "This clause binds the whole … package" as bullets under the bold lead "**Rows are per observable consequence, not per clause.**". "This clause" could now be read as that sub-rule. The original paragraph had the same grouping, but separating these two sentences would be clearer.
- The two clauses are also handled inconsistently: RFC4-30 attaches "(Shape-parallel with …)" to its last bullet, while RFC3-33 keeps it as a separate paragraph.

N4. RFC4-29's list ends "- approximated run boundaries —" and continues in a new paragraph starting in lowercase ("everything else renders Unknown…"). The scope is preserved but the result is an orphaned continuation. Consider ending the list with ";" and starting "Everything else…" as its own sentence, which would still be restructuring.

N5. The new opener in the RFC 0004 README §2 (a non-normative section) says "Doctrine routes facts through typed adapters, durable evidence and versioned snapshot inputs; [Inferred] this contract applies that…".
- "Versioned snapshot inputs" is partly sourced from RFC2-1/RFC2-2, not doctrine alone.
- The opener adds a second `[Inferred]` label to a new sentence.
- Allowed in a non-normative section, but "Doctrine and RFC 0002 route…" would be more exact.

N6. The RFC3-16(c) diagram labels the common node "Human owner act binding RFC3-16(b) items 1–8". But both states bind item 9: state (1) binds its explicit absence, and state (2) binds the audit identity ("Both paths bind RFC3-16(b)'s nine items"). Consider "items 1–9 (item 9 decides the state)".

N7. The RFC4-26 marker diagram (`AP -->|yes| C1`) omits "for that project" from the adoption condition. That is minor.

N8. Changes to the non-normative §0 sections of execution-record.md and named-adapters.md:
- "Observers producing these records **must** satisfy…" became "observers … satisfy…".
- "These adapters **must** satisfy…" became "these adapters satisfy…".

Not normative, but the reader map is now softer than the clauses it summarizes. Restore "must".

N9. Minor structural points, with no meaning change:
- The RFC 0003 README diagram uses the caption "The same edges as a picture (it adds nothing to the list above)", not the standard non-normative caption form. That is acceptable in an index but inconsistent.
- Its forward-reference bullet "This paragraph is navigational…" now sits inside a bullet.
- The RFC4-14 sentence "A one-off capture is legitimate evidence…" is nested under *Reads*.
- The Integration sections drop "On"/"To" under the new "Relies on:"/"Provides to:" leads.

N10. The remaining diagrams were checked against their clauses and found faithful:
- the RFC3-2 expiry path;
- the RFC3-16(a) gate;
- RFC4-5 (both limbs);
- RFC4-7/RFC4-8 admission;
- RFC4-13 tiering, apart from M2;
- RFC4-19/RFC4-20 run identity;
- the RFC4-30 mapping gate;
- the RFC 0004 README module graph;
- the RFC 0003 README edges, which match the five bullets.

N11. The §0 and README openers are true, and every clause they name exists and carries the weight claimed:
- RFC3-2, RFC3-3 and RFC3-4;
- RFC3-16(a), (b) and (c);
- RFC4-1, RFC4-5 and RFC4-7;
- RFC4-13;
- RFC4-19, RFC4-20 and RFC4-21 (the collision rule sits in RFC4-20);
- RFC4-22, RFC4-23, RFC4-27 and RFC4-30 (RFC4-30 says it "binds the whole RFC 0004 package").

The RFC 0003 README lookup sentence matches its Deterministic lookup rule. The RFC 0004 README lookup sentence matches its clause map.

**Checks run** (Python: `rv34/frozen.py` and `rv34/tok.py` in the scratchpad; each count is across all 8 files unless stated)

- **Front matter:** byte-identical in 8/8 files.
- **Preamble paragraphs:**
  - Status: identical in 8/8.
  - Package: identical in 6/6 (the two READMEs have none).
  - Serves: identical in 7/7 (the RFC 0003 README has none).
- **Clause leads** (the regex from the style brief, with an optional list marker): 70/70 identical, in the same sequence. Per file: 30 + 8 + 9 + 9 + 4 + 10 across the six modules; 0 in the READMEs.
- **Headings:** 76/76 have identical text in identical order; none added, none lost.
- **History/Amended parentheticals:** 1/1 identical.
- **Links:** 0 in the originals and 0 in the drafts.
- **Code spans:** 403/403 original spans kept (multiset, whitespace-unwrapped); none lost. 7 new spans were added, all in non-normative text or captions: 4 in the RFC 0003 README, `records/` in a manifests caption, and 2 in the RFC 0004 README.
- **Fenced blocks:** 0 in the originals. 12 Mermaid blocks were added; 11 carry the standard caption and 1 (the RFC 0003 README) has its own.
- **Broken code spans** (lines with an odd backtick count, outside fences): 0 in the drafts. The originals had 2, in governance-homes; the rewrap fixed them without changing any span.
- **New prose lines over 80 columns:** 0.
- **Word-level diff:** markers and fenced blocks stripped, then token streams compared over 84 sections (76 headed sections plus 8 preambles). 61 sections are token-identical; 23 differ. I read all 23 against the line diff.
- **Line-level read:** I read the line diff of every restructured passage in all 8 files, including token-identical sections, looking for list-distribution and qualifier-scope changes. M3 and N3 are the only scope findings.
- **Citer sweep:** `git grep` for citations of the RFC3-2 numbered items, excluding `round-*`: 0 hits.
