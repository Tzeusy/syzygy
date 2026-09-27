Title: Contract readability restyle — RFC 0010 and RFC 0011 — review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: rfc2-draft/RFC-0010/{README.md, mission-identity-approval-and-lifecycle.md, prevention-envelope-and-attention.md, budget-reservation.md, effects-recovery-and-stop.md, portfolio-and-cross-project-consent.md}; rfc2-draft/RFC-0011/{README.md, packet-identity-provenance-and-memory.md, deterministic-selection-and-budget.md}. Each is compared against the same file under rfc2-orig/.
Reviewer: independent fresh-context agent

## Round-1 findings

**M1 — RESOLVED.** RFC10-5's "The rule covers…" paragraph is one paragraph again, as in the original. It runs from "The rule covers **both** non-terminal states…" through "…the state whose exit is a human act. Expiry from a park is a **termination, never a resolution**: it widens nothing (RFC10-12), does not substitute for the human resolution act where the paragraph above owes one, and does not mark the condition cleared. It ends the mission and fires RFC10-19's duties."

- `diff -u` shows no hunk anywhere between the `text` fence and the two new diagrams, so the region is byte-identical to the original.
- "The paragraph above" again points to the "No park is indefinite" paragraph. That is its original referent.

**M2 — RESOLVED.** The RFC10-21 node now reads `"every project whose content it embeds<br/>(keyed on content, not on the declared target;<br/>never only the project the composing step names)"`.

- The draft no longer says the declared target or the composing step's project is excluded.
- The fence matches `rfc2-mmd/RFC-0010-portfolio-and-cross-project-consent-0.mmd`. The re-rendered SVG (03:41) contains "keyed on content" and no parse error.

**N1 — RESOLVED.** The paragraph is restored byte-for-byte: "…declared by the envelope; where none is declared the maximum is the expiry of the Attention Item that park minted (RFC10-12), and where the park minted none it is the envelope's shortest declared **duration-typed** maximum — counts and rates (RFC10-22's queue bounds) are not durations and are outside this limb. The set is never empty: …this limb always has a referent."

**N2 — RESOLVED.** The sentence has rejoined its paragraph: "…never a call the running agent adjudicates for itself. Until the autonomy-level vocabulary is enumerated by owner act (§8 q2), the maximum autonomy level of every envelope is capped at **propose-only**…". "(Both worked examples above are grants…)" again sits in the paragraph directly after the examples.

**N3 — RESOLVED.** The effects orientation now reads "every effect class an envelope permits is classified before it is authorized, and applied effects are dispositioned when the mission fails, is cancelled or expires".

**N4 — RESOLVED.** The portfolio orientation now reads "keyed on the content rather than on the mission's declared target, and fails closed where any is missing or ineffective (**RFC10-21**)". The unattributable-origin limb is still not mentioned. That is acceptable in a summary that is non-normative and defers to the clauses.

**N5 — RESOLVED.** The selection orientation now reads "from a stated minimum set of inputs, and always includes what each selected contract's implementation-boundary declaration names".

**N6 — RESOLVED.** The mission orientation now reads "a Mission binds, at minimum, its objective, target, pinned inputs and initiating owner act".

**N7 — RESOLVED.** The edges now run `M1 -.->|"staged references:…"| M4`, `M2 -.-> M4` and `M3 -.-> M4`, with no edge from M5. The caption reads "…and the staged references from modules 1, 2 and 3 into module 4."

**N8 — RESOLVED.** The failure node now ends "…each such run's reservation is retained and named;<br/>the stop record states the boundary". This matches RFC10-20(d)'s "and the stop record states the boundary".

## Material findings

None. The word-level diff over all 9 file pairs finds no normative change (check 2 below).

## Notes

**N1. Four splice lines exceed the wrap width.** The brief asks for about 78 columns. These four lines were left unwrapped by the repair:
- mission orientation, line 35 (90 columns): "target, pinned inputs and initiating owner act; its lifecycle is a candidate vocabulary in";
- effects orientation, line 33 (100): "effects are dispositioned when the mission fails, is cancelled or expires; and a stop is synchronous";
- RFC10-7, prevention line 85 (100): "adjudicates for itself. Until the autonomy-level vocabulary is enumerated by owner act (§8 q2), the";
- selection orientation, line 32 (100): "implementation-boundary declaration names; dependency traversal follows defined, recorded rules, and".

These are cosmetic only. Mission line 168 (100) is the restored original line, so it is correct as it stands.

**N2. Two "RFC 000N" citations are now split across a line break by the reflow.** Neither is a code span and no token is lost. However, a line-oriented sweep for the citation would now miss them. That is the wrapped-citation class named in AGENTS.md.
- RFC10-6, mission line 233–234. The original had "entirely\nRFC 0008/0002 semantics"; the draft has "entirely RFC\n0008/0002 semantics".
- RFC10-12 bullet, prevention line 300–301. The original had "(Unknowns rendered as Unknowns, RFC 0002)" on one line; the draft has "…Unknowns, RFC\n  0002);".

Suggest re-wrapping both so each citation stays on one line.

**N3. Two list splits leave a dangling "and,".** In RFC10-12 ("what work is **blocked** and whether the situation is **reversible**; and," followed by the bullet "- on resolution, the **resolution act**…") and RFC11-4 ("- the declared kind and named clause, always; and,"), the trailing "and," now ends a bullet. The meaning and the distribution over the list are unchanged: every item is still bound by "at minimum" / "always includes". The wording reads awkwardly and is the same as in round 1; the draft was not changed there.

## New-drift sweep (task 2; there is no DIFF.txt, so I read every `diff -u` hunk across all 9 files)

Nothing was found in any category:
- **Detached qualifiers.** None. Each split keeps its conditions with its lead. Examples:
  - RFC10-6 "never resolved / - by recency, …";
  - RFC10-16 and RFC11-12 "No implementation work … — [list] — may be scheduled solely from this RFC";
  - RFC10-24 "unless / - …, and / - every other independent mission gate passes";
  - RFC11-6 "If required context / - … / the packet is marked…".
- **SHALL/MUST/never/only.** None changed. The token diff is 0 in the 7 modules.
- **Scope.** No widening or narrowing. In RFC10-20, "Effects produced outside Syzygy's mediation … are **not** covered by (b)" is now its own paragraph after limbs (a)–(c). It names (b) explicitly, so its reach is unchanged.
- **List distribution.** Unchanged. I checked RFC10-4, RFC10-7, RFC10-8, RFC10-9, RFC10-12, RFC10-13, RFC10-17 (six quantities, three overrun sources, the provider-spend steps), RFC10-18(a) (four predicate sites), RFC10-19, RFC10-19(a), RFC10-20, RFC10-22 (i)/(ii), RFC11-1, RFC11-4, RFC11-6, RFC11-9 and RFC11-10.
- **Diagrams.** All 17 were re-read against their clauses and none asserts more than its clause. Spot-checks:
  - RFC10-17: "same amount, atomically" matches the original's "by the same amount, atomically".
  - RFC10-17(a): the child release to "the parent's remaining envelope" is in the clause.
  - RFC10-23: "terminal record states all four dimensions" and "bounds to nothing" are the clause's own words.
  - RFC10-22: "undeclared means one outstanding item" is in the clause.
  - RFC11-13: "missing declaration or non-existent named clause → incomplete" is in the clause.
- **Positional references.** 25 hits in the originals and 27 in the drafts. The 2 new hits are the READMEs' orientation phrase "the clause map below", which is correct. Every original hit keeps its referent, including "the branch above" (RFC10-18(a)), "the Unknown rule above … this limb" (RFC10-17), "the paragraph above" (RFC10-5) and "Both worked examples above" (RFC10-7).

## Epistemic-label span (task 3)

The regex `\[(Observed|Inferred|Unknown)[^\]]*\]` finds 9 hits in the originals and 9 in the drafts. 3 of the hits are RFC11-8's "([Observed]/[Inferred]/[Unknown] discipline included)", which mentions the labels but labels nothing. That leaves 6 labels:
- RFC-0010 README §2: [Observed];
- RFC10-2: [Observed — owner direction];
- RFC10-5: [Inferred];
- RFC-0011 README §2: [Observed] and [Inferred];
- RFC11-11: [Inferred].

For 6 of 6, after whitespace normalization, the paragraph holding the label is verbatim in the draft, and so are both the paragraph before it and the paragraph after it. No label covers more or less text than it did in the original.

## Checks run (Python, `rv1011r2/check.py` and `rv1011r2/labels.py` in the scratchpad; permitted additions removed before comparing: 9 Orientation paragraphs, 17 Diagram captions and 17 mermaid fences)

1. **Frozen elements.** All match:

   | Element | Result |
   |---|---|
   | Front matter | byte-identical 9/9 |
   | **Status:**, **Package:** and **Serves:** paragraphs | 25/25 identical |
   | `#` headings (fences excluded) | 63/63, same order |
   | Clause leads | 43/43, same order |
   | Original fenced blocks | 4/4 byte-identical |
   | Code spans | 167/167 identical, same order |
   | Lines with an odd backtick count | 0 |
   | Code spans broken across lines | 0 |
   | *(History/Amended)* parentheticals | 0 in the originals, 0 in the drafts |
   | Inline item markers (a)–(d), (i)–(iv) | 86/86, same order |
   | Numbered item numerals | 26/26, same order |
   | Links | 0 in the originals, 0 in the drafts |

2. **Word-level token diff** over 9/9 file pairs, with list markers dropped. The 7 modules show 0 changes. The only changes are 6 inserted bold lead-ins in the non-normative §0 of the two READMEs.

3. **Identifier tokens per section.** 610 in the originals. 2 are reported "lost", and both are false positives from the line splits in N2: the tokens are still present in their sections.

4. **Paragraph structure.** 241 original paragraphs (split on blank lines, fences removed). 52 are not reproduced verbatim in the draft, split 7/6/6/6/2/10/7/2/6 across the files. All 52 were read in the diffs.

5. **Mermaid.** All 17 fences match their `rfc2-mmd/*.mmd` sources. All 17 SVGs contain no "syntax error" or "parse error". The three changed SVGs are dated 03:41 and contain the new text. `mmdc` is not installed here, so I did not re-render them myself.

6. **Line width.** Prose lines over 78 columns were swept in drafts and originals. Findings: N1.
