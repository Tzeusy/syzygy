Title: Contract readability restyle package — binding review
Verdict: CONFIRM WITH EXCEPTIONS
Manifest SHA-256: 6e83675fd61bf72a1912152dbc3c6dda64303e892eeadcf1273ce6aebe6ab134
Reviewer: independent fresh-context agent

The patched bytes, the manifest and the act digest are all correct. There are no material findings. The exceptions are three notes on the packet's prose. The packet is not a manifest row, so repairing it would not change the act argument.

## Findings

**Material:** none.

**N1. One "found, not changed" item points to the wrong clause.** The packet says: "RFC 0009 §7 case 3 cites RFC9-11/16; the prohibition is in RFC9-17."
- In rfc-orig, RFC9-17 (semantic-geography.md:616) is the forbidden-churn clause. It bars "any metric change in any lens" from moving home coordinates. It does not bar placement by observed coupling.
- That bar is in RFC9-9 (line 222–224): "no undeclared *signal* may be an input to placement: adjacency-by-observed-coupling … are barred". Line 298 names RFC9-14's closed input tuple as the enforcement point.
- Case 3 names "RFC9-9 reading 2" itself (line 753).
- The underlying point stands: RFC9-16, the relocation-trigger set, is a loose citation. But the packet sends the owner to RFC9-17 when it should say RFC9-9 (and RFC9-14).

**N2. Two items are worded loosely.**
- "RFC9-45 says 'that vocabulary is closed at twelve'" states no defect. RFC2-24 does hold exactly 12 reasons: its heading says "Twelve reasons, closed" and the table has 12 rows. So the item is a quotation with no stated problem. It is presumably flagging a count restated outside the clause that owns it, and should say so.
- "RFC 0007's … RFC7-2(a)–(c) and RFC7-9(a)–(c), which the body marks only as '(a)'" can be misread. The body marks all three letters for both clauses:
  - RFC7-2 has inline **(a) anchored**, (b) and (c).
  - RFC7-9 has **(a) Covers.**, **(b) Minimality.** and **(c) Bounding.**
  - The finding is true only in this sense: the qualified form "RFC7-2(a)" appears only in the front matter and in the §-closing line 605.

**N3. "Every link and code span" frozen needs qualifying.**
- The 30 original modules contain no Markdown `](…)` links (0 in both orig and draft).
- For code spans, 1,461 original spans survive in whitespace-collapsed order in 28 of 29 files. The exception is RFC-0004/named-adapters.md: its §0 reader map (non-normative) swaps the order of `gate-backed` and `report-fact`, with the same multiset.
- The drafts add new spans in 16 files, mostly in README and reader maps and in new list prose (for example `RFC2-n`, `.syzygy/**`, `active`).
- None of this changes meaning, and round 2 saw all of it. The packet's frozen list reads more absolute than the evidence.

## Checks run

**1. Reviewed bytes**
- All 29 patches pass strict `git apply --check` against the installed `rfcs/` tree (29/29).
- Each patch was applied separately to both mirrors. The result is byte-identical to `../rfc-draft/<relpath>` in 58 of 58 cases.
- `rfc-draft` holds 30 files. The 30th, `RFC-0007/rendering-and-surface.md`, is byte-identical to rfc-orig, as the exclusion requires.
- No draft file has an mtime after 2026-09-27T18:43:43Z (0 of 30). The latest is 18:41:07Z.
- Additional check: no round-2 review input under `review-*-2/` changed after the cutoff. I regenerated each round-2 `DIFF.txt` (5 of 5 groups) from its `before/` or `snap-*` inputs against the current `rfc-draft`, and every one matches, hunk content only.
- rfc-orig matches both `rfcs/` and `candidates/rfcs/` byte for byte (30 of 30).

**2. Manifest**
- 29 rows, sorted by codepoint. Each hash was re-derived by script from the patched bytes: 0 mismatches.
- Both mirrors produce the same hash for every row.
- The population equals the 30 rows of the bootstrap `CONTRACT-AMENDMENT-MANIFEST.txt` minus `rfcs/RFC-0007/rendering-and-surface.md`, with an empty symmetric difference.
- The manifest file's sha256 is `6e83675f…ab134`, as in the head above.

**3. Builder and checks**
- `build_contract_readability_restyle.py --check` exits 0. It prints: "contract readability-restyle manifest matches 29 patched modules on both identical mirrors; clause leads, front matter and headings unchanged; verify_final_prespec, CG-13 and CG-17 pass on the patched tree".
- `check_governance.py` exits 0 with "32 OK, 20 WARN, 0 FAIL (52 checks)". Its CG-7d output lists `ADOPT CONTRACT READABILITY RESTYLE — 1 quotation(s), 0 finding(s)`.
- The worktree stayed clean at 69a9e74 throughout.

**4. Packet**
- **Act phrase:** the digest in the act phrase (line 12) equals the manifest sha256.
- **Status:** it is labelled "Proposal. It binds nothing until the owner performs the act". Nothing in it is labelled accepted or adopted.
- **Round-1 verdicts:** line 2 of each of the 5 raws reads `Verdict: REVISE`.
- **Round-2 verdicts:** line 2 of each of the 5 raws reads `Verdict: CONFIRM WITH EXCEPTIONS`.
- **Code-span joins:** a scripted comparison of every changed span found exactly the three whitespace-only joins the packet names. Each one collapses to the same text, contains a newline in the original, is one line in the draft, and appears exactly once in the draft:
  - RFC2-18 (reconciliation-chain.md:135, inside the clause that starts at line 133);
  - RFC7-11(a) (narrative-contract.md:246, inside the clause that starts at line 241);
  - `owner-adopted (bootstrap, uncorrelated)` in RFC 0003's "The predicate" paragraph (governance-homes-and-owner-acts.md:204–208).
- **"Found, not changed":** I checked 14 items against rfc-orig. Twelve are accurate:
  - RFC2-5's "RFC2-17…20" when the chain is RFC2-18.
  - RFC4-11 cites RFC4-28, while the closed cause list is in RFC4-24.
  - RFC8-8's "§8 q4": module 1's §8 has only q2, and README line 243 routes q4 to module 3.
  - RFC 0001 §1 says "RFC1-1 … RFC1-32", while RFC1-33 sits in §3.11.
  - RFC 0004 README says "gates six", while RFC4-30 also invokes RFC3-16(a).
  - RFC 0009 §8 says "RFC 0001–RFC 0006" (line 805), while RFC9-8(a) says "RFC 0001–RFC 0009" (line 176).
  - RFC 0005 module 3 §5 names only RFC 0010, while the README names RFC 0010 and RFC 0011.
  - RFC 0005 module 2 §5 names only the choke point.
  - RFC4-23 items 2–3.
  - RFC5-12 "(Project, provider)" at line 87 against "(project, provider)" at line 291.
  - RFC4-19 "Execution record" against "Execution Record".
  - RFC 0009 README count claims.
- The other two items are N1 and N2 above.

My scratch scripts are `rv-final.py`, `rv-spans.py` and `rv-final-cg.txt` in /tmp/claude-1000/-home-tze-GitHub-syzygy/42f1d844-9fb6-4091-8261-544ed369daaf/scratchpad/. I made no edits to the worktree.
