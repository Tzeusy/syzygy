# R-DOV29-5 — confirmation review of PR #121
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: b8ca8413e508d43f494e0214a35a45ee6f9a5b13
Manifest sha256: 0d063de03be54bd9b8b10edbc8362d864010c1a11225cbc6401091cee9c37f4e

Subject: `.syzygy/governance/contracts/candidates/pwb-dismissal-expiry-amendment/`
and `scripts/build_pwb_dismissal_expiry_amendment.py`, read in a detached
worktree at the commit above. Brief: that package's `REVIEW-BRIEF.md`,
criteria 1–16. Reviewer: fresh-context confirmation reviewer, round 5.
No branch byte was edited, committed or pushed; every mutant below ran on a
restored tree and `git status --short` was empty (0 lines) afterwards.

Line 4 is the sha256 of the manifest *file*
`PWB-DISMISSAL-EXPIRY-MANIFEST.txt`, computed by script (Python hashlib and
`sha256sum` agree). It equals the digest quoted at
`OWNER-DECISION-PACKET.md:25` and `:171`.

## Checks run (commit b8ca841)

| Check | Result |
|---|---|
| `python3 scripts/check_governance.py` | 32 OK, 20 WARN, 0 FAIL (52 checks), exit 0 |
| `python3 scripts/check_governance.py --selftest` | 285 fixtures, 0 failing |
| builder `--check` | exit 0: 11 subjects (6 patched, 5 unchanged); requirement, companion, dependency regeneration, 15 composition outcomes and the sequential order verify |
| builder `--selftest` | exit 0: 174 mutants killed (equals `EXPECTED_KILLED`) |
| builder `--diff` | 309 non-blank lines over the 6 patched subjects; content matches the six patches |
| `check_docs_review_campaign_partition.py` | total=252 assigned=252 unmatched=0 overlaps=0 |
| Manifest re-derivation | 11 rows; each row's sha256 re-derived by applying the patches to a scratch copy of the tree; all 11 match |
| Coverage totals | 613 base rows + 15 repair rows = 628 effective; 141 covered / 242 / 245 split as stated at `SEMANTIC-DELTA.md:404`; repair totals 92/77/65/22/5 at `:403` re-derived. (First attempt with regex `RFC\d+-\d+\.c\d+` gave 611 base rows, missing `RFC3-7.c2a`/`c2b`; the loosened regex gives 613.) |

## Round-4 findings: resolution

| # | Round-4 kind | Resolution in round 5 |
|---|---|---|
| R2 | REVISE | **Resolved.** `proposed/spec.md.patch:44-51`: a record "that does not itself state that its author is a human" is refused, and the evaluation "never infers" the author's kind. Scenario 2 lists the model-authored record; the Case line (`:79`) names it. VIS-4 is in the warrants. Every author state falls into exactly one class under either packet Q3 answer (the class table at `OWNER-DECISION-PACKET.md:110-113`). |
| N-A4 | NOTE | **Resolved.** Scenario 3's third record "neither carries nor records as retired", so it cannot also meet the retired-identity test. |
| N-A5 | NOTE | **Resolved.** An unreadable expiry and a reason outside the closed Unknown list are refused (`spec.md.patch:48-50`). The disclosure of refused records is placed at `:51-53`. The Unknown-only reason test rests on RFC2-24, which is quoted at `SEMANTIC-DELTA.md:303-305`. I checked it against `RFC-0002/rendering-vocabularies.md:92` ("covers Unknown states only"). |
| N-A6 | NOTE | **Resolved.** `OWNER-DECISION-PACKET.md:63` says "its expiry has been reached". This matches the lapsed test "not earlier than its expiry instant". |
| N-B2 | NOTE | **Resolved in substance.** The whole-file pin holds. I wrote 10 spec mutants S1–S10: all 10 fail `--check`, and S6 and S9 fail only on the pin. End-to-end patch mutants E1 and E2 (spec) fail `--check` even after `--write`. E5 (repair-delta text) fails the CONTRACT-COVERAGE regeneration. E3 (the proposal reversed to "may count as resolved or favourable") and E4 (the capability header) pass `--check` after `--write` and are caught only by the CG-7d/CG-7e digest copies. That is exactly the scope the docstring states at builder lines 18–27. Builder mutant B19′ (the author rule string weakened) passes `--check` and fails `--selftest` with "rule tables changed without their pinned digest", which matches "their digest is pinned". The remaining gaps are in N-B3. |

## New findings

No revise. Every docstring and packet claim I tested is literally true at
these bytes. Every state in criterion 6 maps to exactly one class under both
Q3 answers:

- refused, for a non-human author, an unreadable expiry or an unknown reason
- bound to a retired identity
- lapsed
- in effect
- never matched
- several in effect
- an unreadable record set

**N-C4 (note), P-79/VIS-4 rationale.** The rationale at
`OWNER-DECISION-PACKET.md:105-108` quotes VIS-4's "draft them, never adopt
them" without its scope. At `vision.md:122-125` that sentence governs
shape-defining deltas, and a behavioral spec record sits below that line. The
same passage also reads the owner's feature-level P-79 Q5 answer
(`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:67`, "dismissal is an
amendment") as a statement about each record. `SEMANTIC-DELTA.md:355-364`
quotes the scope and says "in principle", so the delta is accurate and the
packet is the weaker copy. It is labelled [Inferred], and the author rule
stands on RFC2-15 alone ("a recorded, attributed human decision"), so no
claim is false. Suggested repair: carry the scope into the packet's Q3.
Separately, the [Inferred] label at `:105` covers the reasoning but not the
class sentences at `:110-113`. Those sentences are observed consequences of
the drafted text, so this is fine, but it could be said.

**N-A7 (note), forged human attribution.** A record that an agent commits and
that states a human author is in effect, because the author's kind is "taken
from the record alone" (`spec.md.patch:47-48`). The package gives Syzygy no
write path (packet Q2), so this is a governed-plane integrity question and not
an evaluation defect. It is not disclosed. Suggested: name it in Q2 or Q3 as
what the stated-author test cannot detect.

**N-A8 (note), Falsifier and Case completeness.** The Falsifier
(`spec.md.patch:89-97`) forbids disclosing a non-dismissing record "in any
class but the first … whose test it meets". It does not name the inverse: a
record that meets a refused, retired or lapsed test is shown as a dismissal in
effect. "Takes effect without a governed-plane record" covers only the
missing-record case. The Case line (`:73-80`) lists the author and
unreadable-expiry refusals but not "a reason outside the closed Unknown list"
(refused at `:49-50`). The ordering sentence in the requirement body implies
both, so nothing is false.

**N-B3 (note), builder self-test reach.** These mutants of the builder survive
both `--check` and `--selftest`:

- B12–B17 and B21–B22: `check()` wiring, the content comparison in
  `verify_manifest`, the undeclared-subject branch, the "Population: 32"
  token, and the composition and sequential re-checks.
- B23: the whole-spec pin narrowed to the text from PWB-REQ-007 onward.

`selftest()` never calls `check()`, so a wiring regression in `--check`
cannot fail the self-test. `--check` is correct at these bytes: E1–E5,
S1–S10 and B19′ behave as stated. For B23, the one "byte added outside
PWB-REQ-007" self-test mutant sits after the requirement, so the pin's
leading edge is untested. The drafter's "pin blind past PWB-REQ-007"
(`OWNER-DECISION-PACKET.md:351-356`) tests the trailing edge only. Suggested
repair: add one pre-requirement byte mutant and one self-test case that runs
`check()` end to end on a mutated scratch tree.

## Sweeps

- **Owner attribution.** The pattern was
  `\b(ruling|rulings|ruled|chose|decided|answer\w*|you|your)\b`,
  case-insensitive, over the package's 11 files (5 `.md` files including
  the manifest, and 6 patches). It hit 69 lines, and I read every hit.
  - Each attribution names a real owner act:
    - P-79 Q4 and Q5: decision file `:67`.
    - The 2026-09-23 retention direction:
      `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:104-107`.
    - The landing order ".21 → .30 → .22 → lane B" (packet `:149`): the
      same file at `:111-116`, verbatim.
  - Every reading of an answer as direction carries [Inferred] (packet
    `:17`, `SEMANTIC-DELTA.md:6`).
  - No sentence says the owner chose anything the owner did not.
- **VIS-4 and adoption.** The pattern was
  `\b(adopted|accepted|approved|in force|binds|bound|signed off)\b` over
  the same 11 files. It hit 38 lines.
  - Each hit is one of:
    - the class name "bound to a retired identity"
    - a "Candidate — binds nothing" banner
    - accepted RFC 0001–0009 contracts, which is true
    - "current signed behavior stays in force", which is true
    - a conditional ("An adopted successor stales both pins")
  - No sentence claims this package is adopted, accepted or in force. The
    phrase is not offered (packet `:167-178`), and `:175` says replying now
    performs nothing.
- **VIS-2.** An unreadable record set never yields a zero dismissed or class
  count (Falsifier, `:96-97`). A lapsed or refused record never renders as
  resolved or favourable. Unknown stays Unknown.
- No observed-repository path is backticked in this raw.

## Severity

0 revise, 4 notes (N-C4, N-A7, N-A8, N-B3). Under the owner's 2026-09-26
stopping rule, this notes-only round clears the reviewed bytes.

Verdict: CONFIRM WITH EXCEPTIONS
