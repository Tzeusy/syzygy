Title: Contract readability restyle — RFC 0009 — review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: rfc-draft/RFC-0009/README.md, rfc-draft/RFC-0009/semantic-geography.md, rfc-draft/RFC-0009/visual-grammar-and-lenses.md, rfc-draft/RFC-0009/interaction-parity-and-release.md (each compared against rfc-orig/RFC-0009/; the repair was read through review-0009-2/DIFF.txt and review-0009-2/before/)
Reviewer: independent fresh-context agent

The repair holds and I found no material findings. Every round-1 item is resolved and the frozen elements are intact. Three notes below concern diagram wording only.

**Round-1 findings**

| Finding | Status | Current draft text |
|---|---|---|
| M1 RFC9-17 | RESOLVED | The paragraph is restored byte-identical and ends "…never a licence to relocate. [Inferred, from RFC9-4/14; reserved-extent device adopted from the research disposition of O-F3.]". The label covers the churn list again. |
| M1 RFC9-11 | RESOLVED | Restored: "…attach to home only. A view that binds position to a metric without the analytical-plane marker is a violation identical in class to an unlegended channel (VIS-7). [Inferred]" |
| M1 RFC9-18 | RESOLVED | Restored: "(RFC3-18): version registry and reorganisation-event records are governed; computed geometry is rebuildable projection (`cache/`, RFC3-20); … **Registry entries fix which layout version…**". This is one paragraph again. |
| M1 RFC9-26, first `[Inferred]` | RESOLVED | Restored: "…its **source metric**, **unit or category domain** … and **legend semantics**. … no generated legend can account for. [Inferred]" |
| M1 RFC9-26, second `[Inferred]` | RESOLVED | Restored: "…bound to the registry's exact digest. A valid state-(1) or state-(2) act is effective, … the channel does not render. [Inferred] A forged entry is the sharper failure…" |
| M1 RFC9-32 | RESOLVED | Restored: "…always-available overlays **work/construction** (…) and **freshness/staleness** [Observed: SDR-20]." |
| M1 RFC9-37 | RESOLVED | Restored: "…contract cannot relax them: the capture window renders at all times; … never contribute to status claims [Observed: vision.md]." |
| M1 RFC9-44 (borderline) | RESOLVED | Restored: "…for owner sign-off [Observed: v1.md; SDR-25]. *(Rejected alternative — individual buildings by default — history file, §6.)*" |
| M1 RFC9-49 (borderline) | RESOLVED | Restored: "…never rank 1 [Observed: vision.md, Performance]. **Truth is never purchased with frame rate.**" |
| M2 RFC9-19/20 diagram | RESOLVED | `H["stands at its declared home;<br/>RFC9-19(c) link markers are available here<br/>(never a clone)"]` |
| M3 RFC9-45 diagram | RESOLVED | `SF{"Judgment class, judge, scope or freshness<br/>not qualifying under the effective policy<br/>(or B12(b)'s default)?"}`. This matches item 3: "**which judgment classes qualify and who may judge**", and "**owner decision B12(b) binds directly**". |
| M4 scenario diagram | RESOLVED | `PS["Proposed scene: never looks like existing structure;<br/>where proposals share an exclusivity group or compatibility<br/>is undeclared: N candidate futures, one at a time (RFC9-40)"]`. The repairer departed from the round-1 wording and was right to: RFC9-40's "**proposed structure never looks like existing structure** in any profile at any zoom" is unconditional, and the node now keeps it outside the condition. |
| N1 | RESOLVED | "…the owner-gated full regeneration that writes a new baseline (RFC9-15(b), RFC9-16(d))." |
| N2 | RESOLVED, with a residual (see new N-b) | The yes-node is gone. `X["Forbidden, unconditionally:<br/>silent decimation, silent entity dropping,<br/>stripping epistemic carriers for speed"]` now stands on its own. |
| N3 | RESOLVED | Fixed by the RFC9-49 restore. |
| N4 | RESOLVED, with a residual (see new N-a) | `U --> CM` is removed. The node reads `U["Unmapped and Unknown, never covered:<br/>implementation work may not be scheduled"]`. |
| N5 | RESOLVED | Restored: "— never independently authoritative; its vocabulary … is RFC 0002's, … and its selection, drawer, and query semantics are RFC 0006's, not re-defined here." |
| N6 | RESOLVED | Restored order: "…and edge weight — each under RFC9-26. … Exactly one lens is active at a time." |
| N7 | RESOLVED | The RFC9-43 paragraph is byte-identical to the original. The original's own odd wrap ("counts covering all six⏎of RFC2-25's tiers (`gate-backed`,⏎") comes with it and was not introduced by the draft. |
| N8 | RESOLVED | "…and no implementation work for user-observable Orrery behavior may be scheduled solely from this RFC (RFC9-52)." |
| N9 | RESOLVED | The paragraph is restored as one paragraph, so "the routing sentence carries the information" is true again. |
| N10 | RESOLVED | The four rewraps (semantic-geography §0 opener, "Those declared relations…", "*(Mechanism (c)…", "Write authority…") change whitespace only. The token sequence was checked by script. No new prose line exceeds 80 columns in any of the 4 files. |
| N11 | RESOLVED (superseded) | RFC9-10 is restored byte-identical, and its label ends the paragraph again. |
| N12, N13 | No action needed | — |

**Material findings**

None.

**Notes**

- **N-a. The RFC9-52 diagram's unmapped node drops the clause's scope qualifiers.**
  - Draft: "implementation work may not be scheduled".
  - Original clause: "No implementation work for **user-observable Orrery behavior** may be scheduled solely from this RFC: before implementation, every observable consequence … must either map … or carry an **explicit, reviewed N/A judgment**".
  - Read in isolation, the node could suggest that any implementation work is blocked. The diagram's entry node limits the scope to RFC 0009 consequences, and the caption subordinates the diagram to the clause, so I judge this non-material.
  - Suggested wording: "no implementation work for user-observable Orrery behavior may be scheduled solely from this RFC".
- **N-b. The RFC9-49 diagram adds two small words that are not in the clause.**
  - "Forbidden, unconditionally": the clause sentence ("Silent decimation, silent entity dropping, and stripping epistemic carriers for speed are forbidden") has no condition, so "unconditionally" adds nothing false. It is still an adverb the clause does not use. Plain "Forbidden:" would be exact.
  - "Select one narrowing scope": the clause says "the surface may select only among those declared scopes". "One" is not stated. This node text predates the repair and round 1 did not flag it.
- **N-c. RFC9-45 item 2 continuation line (predates this repair).** A sub-bullet wrap leaves a line beginning "(1) remains visibly uncorrelated." In CommonMark, `(1)` is not a list marker, so it renders correctly. Naive item-marker regexes do flag it, and my own did.
- **N-d. Eleven labels sit in a restyled paragraph that is not identical to the original.** I read each one against the original. Each still ends the same sentence or item it ended in the original, so none is narrowed.
  - RFC9-5: two labels.
  - The "Epistemic class" bullet: that list existed in the original.
  - RFC9-19: `[Observed: SDR-22]` still ends the lead sentence before the colon.
  - RFC9-23: three labels. The original series already carries labels per item (SEC-2 and SEC-3 are item-local), so `[Observed: SEC-5]` binding the secret-exclusion item is a fair reading. It is the least certain of the eleven, and I agree with the repairer's disposition.
  - RFC9-24: two labels.
  - RFC9-29: `[Observed: SEC-5]` is still mid-sentence in the same sentence.
  - RFC9-38: `[Observed: architecture.md]` still ends the lead sentence.

**Checks run**

My scripts are in `rv9r2/` in the scratchpad: `frozen.py`, `labspan.py`, `laball.py` and `labspan_before.py`.

- **Front matter:** byte-identical, 4/4.
- **Preamble:**
  - Status: 4/4.
  - Package: 3/3 (absent in the README, as in the original).
  - Serves: 4/4.
- **Clause leads** (every line-start `**RFCn-m…` through the first period): identical text and order, 2 + 8 + 33 + 23 = 66 (README, interaction-parity, semantic-geography, visual-grammar).
- **Headings (`#`–`######`), fences excluded:** identical text and order, 8 + 10 + 12 + 12 = 42.
- **Item markers:**
  - The original sequence is an in-order subsequence of the draft in 3/3 module files: 3, 20 and 8 markers.
  - The README's one original "marker" is a wrapped "state (1)" (orig line 136), not an item.
  - The extra draft markers are RFC9-16's (a)–(d) and RFC9-19's (a)–(c), promoted in their original order, plus the N-c continuation line.
- **Parentheticals, `*(History…)*` and `*(Amended…)*`:** 0 = 0 in all 4 files. With a denominator of 0 this check could not be mutation-tested.
- **Code spans:**
  - All 173 original spans are kept as a multiset (14 + 32 + 72 + 55).
  - 3 spans are new, all already noted in round 1: README `n` and `RFC9-n`, and semantic-geography `map/`. None is `status`.
- **Broken code spans:** 0 lines with an odd backtick count, fences excluded, in all 4 drafts.
- **Relative links:** 0 = 0.
- **Epistemic labels:** 56 = 56 (0 + 5 + 30 + 21), same sequence and text.
- **Label span, paragraph-final:**
  - 29 of the 56 labels end a paragraph in the original.
  - For all 29, the draft block holding the label equals the whole original paragraph after whitespace and list-marker normalisation. The block is split at list items, so a label confined to a bullet would fail.
  - Mutation check: the same script run on `review-0009-2/before/` flagged 5 of these 29 (RFC9-10, 11, 17, 26 first `[Inferred]`, 37), so the predicate does detect narrowing.
- **Label span, all labels:** 45/56 sit in a containing block identical to the original. I read the other 11 by hand (N-d).
- **Repair diff:**
  - 26 draft paragraphs differ from the pre-repair snapshot.
  - 15/15 claimed restores are byte-identical paragraphs of `rfc-orig`.
  - 4 are whitespace-only rewraps.
  - 1 is the §0 sentence of N8, which adds "implementation work for".
  - 1 is the N1 caption, which changes "rewrites its" to "writes a new".
  - 5 are Mermaid blocks, each read against its clause: M2, M3, M4, N2, N4.
  - The diff contains no hunk that detaches a qualifier, changes modal strength, changes scope, or changes list distribution.
- **Mutation tests (rule 6) on `frozen.py`:** 8/8 mutants detected. They changed the front matter, the Status preamble, a clause lead, a heading, an item number, a code span, a code span broken across lines, and a label.
