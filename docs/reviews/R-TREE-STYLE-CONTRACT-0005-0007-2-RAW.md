Title: Contract readability restyle — RFC 0005, 0006 and 0007 — review 2
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed: RFC-0005/README.md, RFC-0005/admission-and-boundary.md, RFC-0005/consent-egress-secrets.md, RFC-0005/execution-profiles.md, RFC-0006-cross-surface-selection-query-drawer.md, RFC-0007/README.md, RFC-0007/narrative-contract.md, RFC-0007/rendering-and-surface.md (rfc-orig/ against rfc-draft/, with review-0005-0007-2/before/ and DIFF.txt)
Reviewer: independent fresh-context agent

There are no material findings. Everything below is notes only.

## Round-1 findings

- **M1 — RESOLVED.** The RFC5-15 diagram now has `CP --> P1`, `CP --> P2` and `CP --> P3`, each feeding `ALL{"All three pass?"}`. From there:
  - `ALL -->|yes| OK["Egress permitted (a warrant, never evidence of success)"]`
  - `ALL -->|"no: any one fails"| NO["Refused: the transmission is blocked"]`
  - `P3 -->|"no: record in the governed tree without a valid act"| CX["Contradiction minted"]`
  - The diagram no longer implies an order. The contradiction no longer depends on P1 or P2.
  - The caption reads: "which must all pass; a consent record without a valid act also mints a contradiction, whatever the other two parts return."
  - The clause says "Three parts must all pass" and "…does not authorize an egress, blocks the transmission, and mints a contradiction". The diagram matches it. It renders cleanly and I viewed the PNG.
- **M2 — RESOLVED.** RFC 0006 §0 now reads: "RFC6-22 (the equivalence definition over which RFC6-23 forbids contradiction)". This matches the RFC6-22 lead "The equivalence definition." and RFC6-23's "What no pair of equivalent renderings may do is disagree".
- **N1 — RESOLVED.** Module-1 §0 reads: "…effective at the next act without disturbing RFC 0002's evaluation determinism". This matches the RFC 0005 README Scope wording: "without disturbing RFC 0002's evaluation determinism".
- **N2 — RESOLVED.** "Either act may be state (1) or state (2), and each exact state remains visible." is now a 4-space-indented continuation paragraph of the "One egress choke point" bullet, after the nested list of three parts. It is no longer a sibling of those parts. Under CommonMark it belongs to the parent item. No Markdown parser was available, so this is checked by reading the indentation only.
- **N3 — RESOLVED.** The opener of RFC 0007 README §2 is now a pointer: "Doctrine and the owner's rulings SDR-13 to SDR-18 ground this package; each point below carries its own epistemic label." The [Observed], [Inferred], [Inferred] and [Observed] bullets are unchanged.
- **N4 — RESOLVED.** "A secret reproduced in any surface, store, or endpoint is a trust-floor violation … (trust-and-evidence.md floor bullet 4)." now closes RFC5-17, and the redaction diagram follows it. The paragraph's text is unchanged.
- **N5 — RESOLVED.** The RFC5-25 diagram now draws `subgraph GT["Governed tree: .syzygy/**"]` containing only `GR["governance/records/"]`, with `FW["Fleet worker (untrusted actor class)"] -->|can write| GR`. The node `AT` reads "outside .syzygy/** and outside the untrusted class's write reach". This matches the clause's "outside `.syzygy/**` and outside the untrusted actor class's write reach" and its "(including `governance/records/`, which the untrusted class can write)".
- **N6 — RESOLVED.** The edges now read `M1 -->|"admits the principal"| M2/M3` and `M2/M3 -->|"emits into its audit trail"| M1`. RFC5-25 lists both egress and run launch among the acts that emit audit records.
- **N7 — SUPERSEDED, correctly.** The RFC6-5 paragraph "**first** of the following … RFC6-26/27.]" is byte-identical to the original. I found it by paragraph search and it matches.
- **N8 — Unchanged, acceptable.** The RFC7-11(a) span is still rejoined. The original has an odd-backtick pair at lines 246–247; the draft has none.
- **N9 — Superseded.** RFC5-5 from its lead through "…the silence was the defect]." is byte-identical to the original, so the "and" is back.
- **N10 — RESOLVED.** I rendered all 13 mermaid blocks, extracted from the draft files, with mmdc 12.0.0. All 13 render with no errors. The 4 `.mmd` files in `review-0005-0007-2/mmd/` are byte-identical to the corresponding draft blocks.

## New-drift review of DIFF.txt

- DIFF.txt is complete. I regenerated `diff -ru before rfc-draft` myself and it matches DIFF.txt exactly, apart from the file headers.
- `execution-profiles.md` and `narrative-contract.md` have the same hash in before/ and draft/, so neither was touched by the repair.
- I read all 11 hunks against rfc-orig:
  - 4 restore original bytes (RFC5-5 and RFC6-5) or move a paragraph without changing it (RFC5-17).
  - 3 change §0 or README-opener text, all non-normative.
  - 4 change diagrams or captions.
- None of them detaches a qualifier, softens or strengthens a modal, changes a scope, changes list distribution or changes a label span.

## Notes

- **N1 — "Revocation forces an evaluation" label placement (admission-and-boundary.md, RFC5-11). Carried over from round 1; not a repair regression.**
  - Original: one paragraph ending "…never as current. [Inferred — the forced trigger is the owner's decision; its reconciliation with RFC2-4 is this RFC's, and is why the trigger is lawful rather than a carve-out.]"
  - Draft: a lead paragraph, then two bullets, then the label as its own paragraph.
  - This is the only paragraph-ending label out of 14 whose unit is not identical in the draft.
  - It does not narrow the span. The label no longer sits on a tail sentence; it stands alone after the whole block, and its text names both the trigger (in the lead) and the RFC2-4 reconciliation (in the first bullet). So I accept it.
  - The repair restored RFC5-5 and RFC6-5 byte-for-byte for a label-span reason, but chose a standalone label here. The two treatments are consistent in effect, but not in method.
- **N2 — The RFC5-25 caption compresses the clause slightly.**
  - New caption: "…and RFC3-16(a) verifies against it there."
  - The clause says RFC3-16(a)'s *class of acceptable mechanisms includes* correlation recorded in this trail, and that "RFC3-16(b) item 9 requires the binding to be verifiable against it".
  - The diagram's gate node already names "RFC3-16(b) item 9". The caption is non-normative, and it overstates only the "includes" permissiveness. No change is needed. An optional tighter wording would be "…and the RFC3-16(a) gate can verify against it there."
- **N3 — The totals for some checks differ between round 1, the repair and this review because each used a different regex. No run found a loss.**
  - Italic parentheticals: round 1 counted 73, the repair 69, and this review 71. My regex also catches the `*(… ).*` form, such as "*(rev10 scoping, directive §2 / OD-R10-5).*".
  - Lettered and roman items: the repair counted 140. This review counted 141 in every form, including citation forms such as `RFC3-16(a)`, and 47 as stand-alone markers.

## Checks run (my own scripts in `r567b/`)

**Unchanged file.** `RFC-0007/rendering-and-surface.md`: `cmp` passes. The orig, draft and before/ copies all have sha256 `d4ab9646269e4f22…`.

**Frozen elements** (`r567b/check.py`, orig against draft, 8 files): 0 failures.

| Element | Result |
|---|---|
| Front matter | 8/8 byte-identical |
| Preamble paragraphs (Status, Package, Serves) | 20/20 byte-identical |
| Headings | 93, same sequence |
| Clause leads (addendum regex, taken through the first period after the title) | 96, same set and order: 0/15/6/6/28/0/26/15 |
| Numbered items | 56, exact sequence per file |
| Stand-alone lettered or roman items | 47, exact sequence |
| All-form lettered items | 141, original sequence preserved; +4 insertions in draft, round-1 known |
| Bold item numbers (`**n**`) | 8, exact |
| `*(History…)*` / `*(Amended…)*` parentheticals | 1, identical |
| All italic parentheticals (whitespace-normalized) | 71, 0 lost, 0 gained |
| Markdown links | 0 in the originals |
| Code spans, whole file | 0 of 325 lost |
| Code spans, per section | 0 lost across 101 sections |
| Identifier tokens (RFCn-m, VIS, SEC, SDR, CC, P, FD, OD, "RFC nnnn"), per section | 0 lost across 101 sections |
| Code spans broken across lines, draft | 0 in 8/8 files |

**Rule-6 mutation test.** I mutated 9 predicates one at a time on a scratch copy: heading, clause lead, code span, broken span, front matter, parenthetical, item number, identifier token and preamble. Each mutation failed its own predicate.

**Epistemic labels** (`r567b/labels.py`):

- There are 46 label occurrences in the originals. Per-file counts are identical between orig and draft, except the RFC 0007 README, which goes from 4 to 5 because the [Inferred] label was distributed across two bullets (round-1 known).
- 14 labels end a paragraph or list unit. 13 of those units are identical in the draft after normalization; the 14th is N1 above, read by hand.
- 46/46 labels stay contiguous with their own sentence in the draft.

**Other checks:**

- **Mermaid:** 13/13 draft blocks render with no errors. I viewed the rendered RFC5-15 diagram.
- **Prose lines over 80 columns, outside fences and tables:** the before/ and draft counts are equal in 8/8 files (3/4/3/3/2/4/4/6).
- **Bare `status` code span:** 0 in all 16 files.
- **New number-with-unit in the repair hunks:** 0.
