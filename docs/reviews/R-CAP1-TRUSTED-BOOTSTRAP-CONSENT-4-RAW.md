# R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-4 — confirmation review of cap1-trusted-bootstrap-consent
Reviewed commit: 591950c76805f34886e7052adb9753c58b5ef737
Manifest SHA-256: e590ee3beaa4a4c11e8e3794dde9f6cc550bc888b2ddac5f4b32460ff74be82a
Verdict: CONFIRM WITH EXCEPTIONS

Fresh-context CC-REV-1 (security/authority-boundary) and CC-REV-4 (fresh-reader)
confirmation review of the candidate package cap1-trusted-bootstrap-consent,
round 4, after the round-3 REVISE and its single repair.

## Summary

[Observed] Subject freeze: `sha256sum` of
docs/evidence/cap1-trusted-bootstrap-consent-2026-10-15/review-4-subject.json is
e590ee3beaa4a4c11e8e3794dde9f6cc550bc888b2ddac5f4b32460ff74be82a, equal to the
expected value. The manifest names 14 paths. `git ls-files -s` over
openspec/changes/cap1-trusted-bootstrap-consent/ lists exactly those 14 paths and
`ls` shows no untracked extra. All 14 per-file `sha256sum` values equal the
manifest (14/14).

[Observed] Change since round 3: comparing review-3-subject.json (sha256
1a9f76df2a6e29f9f8e724138c7687900357f8248ca2d3f8093eadefe99ea8a8, the value
R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-3-RAW.md:3 records) with review-4-subject.json,
13 of 14 rows are equal and only REVIEW-DISPOSITION.md differs.
`git diff 70af85e86dc17e8f6d1378f36575781c55084ec0 591950c76805f34886e7052adb9753c58b5ef737
-- openspec/changes/cap1-trusted-bootstrap-consent` shows one hunk in that file,
replacing one sentence of the rebase section (REVIEW-DISPOSITION.md:35-39). Between
6ff755671d743f289c59d8a26b7f68f6e09d55d6 and the reviewed commit the only change
is the added review-4-subject.json (`git diff --stat`), so the candidate bytes
equal that main commit's.

Criterion 1 (round-3 finding 1) [Observed]: resolved. The repaired sentence reads
"Until 2026-10-15 the candidate was never committed to main or to any pushed ref;
it sat untracked in the main checkout. (One local, unpushed commit,
c596fda4ab35edd0a99c85cb3fec26895bd33f3d of 2026-10-04 on the local branch
governance/redis-sitting-simulation, carries all 14 files with blobs equal to
review 2's subject, per review 3, finding 1.)" (REVIEW-DISPOSITION.md:35-39).
`git branch -a --contains c596fda4ab35edd0a99c85cb3fec26895bd33f3d` returns only
`governance/redis-sitting-simulation`, with no remote-tracking ref. `git show -s`
gives author and committer date 2026-10-04 07:53:32 +0800. `git ls-tree -r` lists
14 files under the candidate directory. `git log --all` over the candidate
README.md finds exactly three commits containing the package:
c596fda4ab35edd0a99c85cb3fec26895bd33f3d (2026-10-04), and
5fbd608770cae69209233442489b45422f55b6cd and
16f4bf1dfc17fbd961139c62325e3a2018ee3141, both dated 2026-10-15. The first of
those two is on remotes/origin/agent/cap1-trusted-bootstrap-consent and the second
on remotes/origin/main. So "until 2026-10-15 … never … any pushed ref" and "one
local, unpushed commit" both hold over the local refs. The blob-equality clause is
attributed to review 3 and matches what round 3 reported
(R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-3-RAW.md:18-24, :105-113). I did not re-hash
c596fda4ab35edd0a99c85cb3fec26895bd33f3d's blobs against the review-2 manifest,
which is outside my file list. [Inferred] The six files round 3 called unchanged
since review 2 have blob ids equal to the reviewed commit's in that tree, which is
consistent with that attribution. The repair adds no new false statement I could
find. "It sat untracked in the main checkout" is a claim about past working-tree
state that git cannot confirm or refute. [Unknown] It is not falsified.

Criterion 2 (rebase correctness) [Observed]:
- All 15 BASELINE.json protected-predecessor sha256 values equal the current
  files (15/15, one `sha256sum` run over all 15 paths).
- `git merge-base --is-ancestor 2d6a36328f638d3ce52605e88328c1ac7b4c9895
  591950c76805f34886e7052adb9753c58b5ef737` exits 0.
- Both GOVERNING-DEPENDENCIES.json source_files hashes match: the candidate
  spec.md is 359ff741742902f0b07bbf1b4ec9aa997d17145cd56805fb49d6e683a12776e7
  and the adopted spec.md is
  65b66c913cd2650881a9df8cb34a3c63b3f518041e83f45d2451980d9f1d0448.
- A scripted line-list comparison shows that PREDECESSOR-REQUIREMENTS.md lines
  5-51 equal adopted spec.md lines 359-405 exactly (the full CAP1-REQ-011 body,
  ending before CAP1-REQ-012 at :406). Lines 52-94 equal adopted spec.md lines
  1501-1543 exactly (the full CAP1-REQ-046 body, ending before CAP1-REQ-050 at
  :1544).
- CAPABILITY-1-READABILITY-SUCCESSOR-ACT.md:40 states "The specification, both
  coverage tables and the generated dependencies are unchanged", consistent with
  REVIEW-DISPOSITION.md:43-45.

Criterion 3 (consent and trust boundary) [Observed, with Inferred judgments marked]:
the two replacements are faithful to RFC3-16(a/b/c) as written in
governance-homes-and-owner-acts.md today.
- State (1) only on an explicit human act. RFC3-16(b) reads "A state-(1) act
  satisfying items 1–8 and explicitly recording item 9 absent is effective under
  RFC3-16(a)" (:301-302), and state (1) is available after A1 "only when the human
  owner explicitly chooses trusted-bootstrap provenance in the act itself"
  (:303-305). The candidate says "A human act explicitly selecting state (1),
  with all nine bindings and explicit absence of the A1 audit identity, SHALL
  admit its in-force, scope-matched consent without an independent provider"
  (spec.md:7) and gives the positive scenario at spec.md:20-23.
- Omission versus absence. RFC3-16(b) item 9 reads "Omitting the field is
  invalid; explicit absence is not independent verification" (:296-297). The
  candidate says "An omitted audit-identity field is invalid; explicit absence is
  permitted only for state (1)" (spec.md:7), and "omitted audit field" is a named
  invalid case at spec.md:32.
- State (2) needs correlation (spec.md:7, :25-28). Failed correlation never
  downgrades. RFC3-16(b) reads "A failed, unavailable or indeterminate A1 attempt
  never creates state (1) and never changes a record claiming state (2) into state
  (1)" (:306-307). The candidate carries this at spec.md:7 ("Failed or unavailable
  state-(2) correlation SHALL NOT create state (1)") and spec.md:35-38 (which adds
  "indeterminate" and "no … automatic retry").
- Fail closed before reads. RFC3-16(a) reads "Missing, digest-mismatched,
  wrong-scope, stale, expired, superseded, revoked, unattributed or non-human act
  state blocks the dependent effect, renders the authorization Unknown and mints a
  contradiction routed to owner adjudication" (:319-322). Every term is in
  spec.md:7 and spec.md:32, which adds malformed binding, identity/project/act-type
  mismatch, missing instant and future instant, and refuses "before reading the
  dependent repository content". [Inferred] "stale under an applicable declared
  bound" is a qualification, not a narrowing. Staleness in this corpus is relative
  to a declared currency bound, and the positive case separately requires the act
  to be "current" (spec.md:22), as RFC3-16(a)'s "current, attributable,
  scope-matched" (:218-220) requires.
- Withdrawal polarity holds. A valid withdrawal defeats a grant, and invalid or
  unresolvable withdrawal "SHALL leave the pair refused rather than revive a
  grant" (spec.md:7, :45-48; design.md:55-57). This is fail-closed and stricter
  than the clause.
- No claim of verified attendance. RFC3-16(a)'s trust premise reads "State (1)
  relies on the owner's trust in the recorded tree and does not prove the tree
  could not forge the record … If an implementation accepts a forged record as an
  act, the resulting effect is unauthorized and is a trust-floor violation, not
  authority granted by this clause" (:245-252). The candidate restates this at
  spec.md:7 ("never a default, inferred permission or proof of attendance;
  accepting a forged record remains unauthorized") and spec.md:75. RFC3-16(c)'s
  "never 'verified'" (:391-392) is carried by spec.md:92 ("only successfully
  correlated state (2) SHALL be labelled Syzygy-verified").
- The machine-only and non-human cases are refused with distinguishable
  diagnostics (spec.md:40-43). That respects "A machine may prepare an act for
  owner attendance; it may not mint, impersonate, approve, widen, revoke or
  reinterpret one" (:248-250). Correlation reaching only a new evaluation
  (spec.md:92, :115-118) matches RFC3-16(c) at :403-407. Warrant versus success
  (spec.md:92, :108) matches :408-411.
- [Inferred] I found no widening of authority, no consent implied from absence or
  default, and no admission by a machine-only act. Legacy records do not
  auto-upgrade (design.md:83-85). The scope is limited to consent and is not a
  general authority-input subsystem (spec.md:92; CONTRACT-COVERAGE.md:43).

Criterion 4 (CC-SPEC-4/8/11) [Observed]:
- CC-SPEC-4. Each added limb names a producible controlled case, literal expected
  tuples "specified independently of the implementation", intercepted-read
  observables, a denominator of "the enumerated scenario/input-variant matrix,
  never the implementation's accepted subset", and a falsifier (spec.md:75, :77,
  :135). That satisfies "the oracle is not defined by, and does not consult, the
  implementation under test" (SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:194-195).
- CC-SPEC-11, re-derived with a Python `re` sweep. The candidate
  CAPABILITY-COVERAGE.md has 15 distinct rows: A-01..A-10 (10, each naming a
  covering scenario) and X-01..X-05 (5, each naming a proposal.md non-goal), with
  0 unresolved. The 10 A rows correspond one-to-one with the 10 added scenario
  titles in spec.md. The predecessor CAPABILITY-COVERAGE.md has 26 row-anchored
  ids, 26 distinct (O-01..O-21, U-01, X-01..X-04). A second, unanchored
  word-boundary sweep over the whole file returns the same 26-id set. The file's
  sha256 equals its BASELINE.json row, so it is preserved. O-05, O-10, O-19 and
  U-01 exist as the candidate cites them (predecessor :32, :37, :46, :66).
- CC-SPEC-8. Rows are per consequence (CONTRACT-COVERAGE.md:21-43). The quoted
  predecessor row (:10) is identical to predecessor CONTRACT-COVERAGE.md:109.
  General non-consent admission stays Unknown (:43). No N/A is minted (:6, :46).
  The composed dependency union has 40 contract ids. The predecessor
  GOVERNING-DEPENDENCIES.md has 38; the difference is exactly RFC3-16(b) and
  RFC3-16(c), and both are mapped by overlay rows. See Finding 2 for one unmapped
  consequence row.

Criterion 5 (fresh-reader restatement) [Inferred]: a reader can restate it.
Adoption would replace CAP1-REQ-011 and CAP1-REQ-046 so that an explicit human
state-(1) consent act, with all nine bindings and A1 explicitly absent, admits
exactly its project/repository observation scope without an audit provider. State
(2) stays distinct and never falls back. Every invalid act state is refused before
dependent reads, with authorization Unknown and an owner route. Provenance renders
in both channels as "owner-adopted (bootstrap, uncorrelated)" or "Syzygy-verified".
Adoption would not build a provider, authorize implementation, grant consent for
any repository, or detect a byte-identical forgery. The trade-off is kept, not
smoothed away: "The practical cost is trust in the owner's recorded tree: hashes
detect changed bytes, not forgeries" (proposal.md:19-20), and "Byte-identical
forgeries are not a mechanically distinguishable fixture" (spec.md:75). The packet
repeats it (packet:58-62).

Criterion 6 (no overclaim; packet carry) [Observed]:
- No adoption claim: README.md:3-6, proposal.md:3-5 and :67-70.
- No implementation authority: APPLYING.md:44-49 matches
  CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md:37-40.
- No consent for any repository: APPLYING.md:48-49, packet:114.
- No battery pass: VALIDATION.md:4 and :21-22.
- The packet carries round 3's finding 2 faithfully under Question 1
  (packet:73-80). It says that the RFC3-16(a) row and the Part A totals go stale,
  that the bytes are act-bound, and that adoption must name the overlay as
  superseding them or carry a coverage successor, citing CC-REV-2. This matches
  R-CAP1-TRUSTED-BOOTSTRAP-CONSENT-3-RAW.md:122-134. The packet's status sentence
  "The candidate reached no pushed ref until 2026-10-15" (packet:13-14) is
  consistent with the refs above. Finding 1 says that the set the adoption must
  supersede is wider than round 3 named.

## Findings

**Finding 1 — The predecessor coverage text that adoption must supersede is wider than the row and totals the packet names** (note, for the owner)
[Observed] The composed dependency union in the candidate GOVERNING-DEPENDENCIES.json
has 40 contract identifiers. The predecessor's generated GOVERNING-DEPENDENCIES.md
has 38, and the scripted set difference is exactly RFC3-16(b) and RFC3-16(c).
Adoption would therefore leave several more predecessor statements asserting the
pre-amendment truth, beyond the row-109 disposition and the Part A totals at
:140-142. In predecessor CONTRACT-COVERAGE.md:
- the family table's RFC3 row, "38 | 11 | 27", and its total, "324 | 38 | 286"
  (:36, :43);
- "The 38 mapped clauses are exactly the `contracts[]` union in the generated
  `GOVERNING-DEPENDENCIES.md`" and "The 286 unmapped clauses" (:45-47);
- Part B's "RFC 0003 remainder | 27" and its total of 286 (:160, :167), which
  still count RFC3-16(b) and RFC3-16(c) as unmapped;
- the verification predicate "Part A's clause column must equal the generated
  `contracts[]` union (38 identifiers), and 38 + 286 = 324" (:173-175).
The predecessor GOVERNING-DEPENDENCIES.md itself, generated and bound, would no
longer be the composed union. The candidate does not hide this. Its
CONTRACT-COVERAGE.md:16-17 says no historical clause count is restated as freshly
measured, and APPLYING.md:23 asks for "exact reviewed coverage/dependency
consequences before the act". The packet's carried note (packet:73-80), faithful to
round 3, names only "Its RFC3-16(a) row (Unknown) and its Part A totals". [Inferred]
Under CC-REV-2 ("No merge may leave mainline with an invalidated authoritative
artifact still asserting the old truth", review-and-documentation.md:93-94), the
adoption record or coverage successor should name this whole set, not only the row
and totals. Otherwise the default-route counts stay stale after adoption. This does
not block the candidate specification.

**Finding 2 — RFC3-16(a)'s "blocking is not deletion" consequence has no row in the consent overlay** (note, for the owner)
[Observed] RFC3-16(a) states, as one of its failure-effect consequences, "Blocking
is not deletion: the artifact and its invalid act state both remain rendered"
(governance-homes-and-owner-acts.md:328-329). The candidate CONTRACT-COVERAGE.md
overlay (:21-43) has no row for that consequence. The nearest row, "Each named
invalid act state refuses effect, yields authorization Unknown and owner route"
(:26), does not name continued rendering. The overlay's own rule is that "A
reviewer finding another used contract consequence must add a scoped row or retain
an explicit Unknown" (:47-49), and CC-SPEC-8 counts rows "per observable
consequence, not per clause" (SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md:272-275).
[Inferred] The behaviour itself is substantially specified:
- the retained first sentence of CAP1-REQ-011 makes records' "scope, attribution,
  and grant state render with the coverage boundary" (spec.md:7);
- the invalid case makes "its specific failure and owner contradiction route …
  available" (spec.md:33);
- design.md:83-85 keeps refused legacy records "visible as recorded facts with
  authorization Unknown".
However, CAP1-REQ-046's disclosure sentence is a disjunction: it exposes "the
consent artifact identity and digest, owner-act basis, provenance state and
evaluation identity, or the precise refusal reason with authorization Unknown"
(spec.md:92). Read alone, it would let a refusal answer omit the refused artifact's
identity and digest. The owner may want the adoption version to add one overlay row
mapping this consequence to CAP1-REQ-011/046, and optionally to make 046 expose the
artifact identity in the refusal case too. Alternatively the owner may record that
this is folded into the row at :26. Either way, the omission should be recorded
rather than left silent. No widening of authority follows from the omission:
refusal remains fail-closed.

Read-only review; no fixes authored. Preserve this raw output unchanged under CC-REV-6.
