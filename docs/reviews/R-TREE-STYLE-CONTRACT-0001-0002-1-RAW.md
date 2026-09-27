Title: Contract readability restyle — RFC 0001 and RFC 0002 — review 1
Verdict: REVISE
Reviewed: rfc-draft/RFC-0001-project-graph-identity-state-planes.md; rfc-draft/RFC-0002/README.md; rfc-draft/RFC-0002/snapshot-and-evaluation-core.md; rfc-draft/RFC-0002/challenge-lifecycle.md; rfc-draft/RFC-0002/reconciliation-chain.md; rfc-draft/RFC-0002/rendering-vocabularies.md. Each was compared against the same path under rfc-orig/.
Reviewer: independent fresh-context agent

**Material findings**

- **M1. One diagram drops a qualifier from the clause it illustrates (criterion 4).**
  - Where: `snapshot-and-evaluation-core.md`, the "RFC2-7 seam and the RFC2-8 ceiling" diagram, on the overlay → claim-instances edge.
  - Clause RFC2-8 says an overlay "may never establish, raise, or **independently** satisfy a positive status claim".
  - The diagram says: `never establish, raise or satisfy a positive status`.
  - Why it matters: without "independently" the diagram asserts a stronger prohibition than the clause does. That is an outcome the clause does not state.
  - Fix: change the edge label to `never establish, raise or independently satisfy a positive status claim`.

**Notes**

- **N1. RFC2-18: a code span changed bytes.** In `reconciliation-chain.md`, the chain span `` `merged → … Unknown(reason)` `` was wrapped over three lines in the original. The draft puts it on one 134-column line. The span's content changes (newlines become spaces), but it renders the same, and the change repairs a code span that was broken across lines. Criterion 2 lists code spans as byte-frozen, so the owner should accept this change explicitly.
- **N2. RFC2-15: a bullet lost its verb.** The draft splits "it … is never resolved by precedence, never auto-scheduled into work" into two bullets. The last one now reads "- never auto-scheduled into work.", so "is" no longer carries over to it. The meaning holds, but the bullet is ungrammatical. Fix: merge the two into one bullet, "is never resolved by precedence, never auto-scheduled into work."
- **N3. RFC2-26: words were reordered inside a normative sentence.**
  - Original: "No implementation work for user-observable consequences of this contract — [list] — may be scheduled solely from this RFC."
  - Draft: "… of this contract may be scheduled solely from this RFC: [list]".
  - The meaning and the list are preserved, and the list is still an apposition to "user-observable consequences". But this is a word move, not only list conversion. RFC1-33, its shape-parallel clause, needed no such move.
- **N4. RFC2-10: awkward list structure.** The draft nests a three-item sub-list and then continues with "— a value existing in no vocabulary…" as an indented paragraph. It renders correctly but reads oddly. The meaning is preserved.
- **N5. RFC 0001 §1 reader map has a mismatched range.** The parent line keeps the original "§3 is the contract (RFC1-1 … RFC1-32)", but its new children list "§3.11 … RFC1-33". This mismatch already existed; the new tree makes it visible. Either fix it as "noticed, not changed" or leave it, since the section is non-normative.
- **N6. Diagram captions run over the wrap width.** They reach 86–90 columns: snapshot lines 156 and 219, reconciliation line 245, rendering line 254, README line 121. This is cosmetic.
- **N7. New §0 sentences are accurate (criterion 3).** Each was checked against its clauses:
  - challenge-lifecycle: "four resolutions, each via a new snapshot and a new evaluation" matches RFC2-13 (resolution authority, the expiry paragraph, and the provider-revocation paragraph).
  - reconciliation-chain: matches RFC2-15, RFC2-17 and RFC2-18.
  - rendering-vocabularies: "all three closed … only `gate-backed`" matches RFC2-23, RFC2-24 and RFC2-25.
  - snapshot: matches RFC2-3 and RFC2-4.
  - RFC 0001: the weight given to RFC1-22, RFC1-24 and RFC1-25/26 matches those clauses.
  - README: the package summary and the "modules 2–4 independently readable given it" claim restate original README lines 68–69.
- **N8. The other seven diagrams were checked and are faithful:**
  - RFC1-1, governance-root count;
  - RFC1-22, what occupies a plane;
  - RFC1-29, materialization authority;
  - RFC2-4, degradation over time;
  - RFC2-13, challenge states;
  - RFC2-18, the chain;
  - RFC2-26, "Precondition for implementation met", which correctly shows a necessary condition rather than a sufficient one.

**Checks run**

- **Front matter and preamble.** A Python script checked the YAML front matter plus the Status, Package, Date and Serves paragraphs. All present items are byte-identical across the 6 files: 6/6 front matter, 6/6 Status, 6/6 Serves, 5/5 Date, and 4/4 Package (the only files that have one).
- **Headings.** The sequence of all `#` headings is identical in order, 64 of 64 (RFC 0001: 19; README: 11; challenge-lifecycle: 6; reconciliation-chain: 9; rendering-vocabularies: 9; snapshot: 10).
- **Clause leads.** The full `^\*\*RFC…\*\*` lead strings are identical in order, 65 of 65 (RFC 0001: 37; RFC 0002: 0 + 3 + 9 + 5 + 11). This includes RFC2-19(a) and the RFC1-18(a)/(b) and RFC1-25(a)–(d) sub-clauses.
- **Identifiers.** A per-file multiset of identifiers (RFCn-m with sub-letters, VIS, SEC, SDR, CC, P-n, A/B decisions) found **0 lost** in all 6 files. All additions are in §0, §1 and README reader-map prose.
- **Code spans.** 282 original spans across 6 files. After whitespace normalization, none were lost or altered. The additions are 4 spans in non-normative prose: `RFC2-n` twice, `admitted` once and `gate-backed` once. One span changed bytes (N1).
- **Draft code-span integrity.** 0 non-fence lines with an odd backtick count across all 6 drafts.
- **Links, History/Amended parentheticals and fenced blocks.** None exist in the originals (0/0/0). 9 Mermaid blocks were added, each with the required caption.
- **Item numbers and letters.** The order of `(a)…(viii)` and `item N` tokens is identical in all 6 files. The README showed one apparent reorder, which on inspection was a line-wrap artifact of the check ("item" at a line end in the original).
- **Word-level diff.** Mermaid blocks and captions were stripped and list markers dropped, then the token streams were compared with `difflib`. Every flagged hunk was read (RFC 0001: 22 hunks; RFC 0002 modules and README: 81 hunks). Every normative-section hunk is punctuation only (`,` → `:`/`;`, `.` → `;`), apart from the RFC2-26 word move (N3).
- **Line diff.** Every normative clause changed by list conversion was read against its original (RFC1-1, 7, 8, 9, 16, 20, 23, 27, 31, 33; RFC2-3, 4, 6, 9, 10, 12, 13, 15, 16, 18, 19(a), 21, 23, 24, 26; README §1, §2, §5 and §6). For each one I checked that qualifiers stay attached, that "each"/"either"/"and" distribute over the same items, and that epistemic labels cover the same text. No change was found beyond N2 and N3.
