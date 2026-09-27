# R-DOV29-4 — confirmation review of PR #121
Verdict: REVISE
Reviewed commit: b28bc184ac521335272c115b5ebbf370eccd9cb9
Manifest sha256: 9f4063d303e75b893bc7348df0aef9e5e84c381df6ae98b3d15b4b7c22af9838

Reviewer: fresh-context confirmation reviewer, read-only. Detached worktree
at the reviewed commit (branch `origin/agent/tier4-dov29`, tip `b28bc18`).
Chain on `96ee305` (`git merge-base HEAD origin/main`): `7d0049c` →
`def4d6a` → `21df27a` → `8307180` → `d47efe6` (round-3 repair) → `b28bc18`
(partition recount). Nothing committed, pushed or left edited; every
mutation below was reverted and `git status --short` was empty after each
group.

Head line 4 is the SHA-256 of the manifest **file**
`PWB-DISMISSAL-EXPIRY-MANIFEST.txt`, per `REVIEW-BRIEF.md` "## The raw's
head" (lines 99-114), computed by `sha256sum` and by Python `hashlib`
(both equal). It equals the packet copies at `OWNER-DECISION-PACKET.md:25`
and `:161`. The drafter-reported `9f4063d3…` is confirmed.

## Commands run and outputs read

All [Observed] at the reviewed commit unless labelled.

1. `python3 scripts/check_governance.py`: "32 OK, 20 WARN, 0 FAIL (52
   checks)". `--selftest`: "285 fixtures, 0 failing".
2. Builder `--check`: "manifest matches 11 proposed subjects (6 patched, 5
   unchanged); requirement, companion, dependency regeneration, 15 declared
   sibling-composition outcomes and the sequential sibling order verify".
   `--selftest`: "136 mutants killed — … 31 paragraph rules, … 14
   scenario-body rules, 12 forbidden wordings …". Counted independently:
   `len(PARAGRAPH_RULES)` 31, scenario rules 14, `FORBIDDEN` 12. `--diff`
   prints the six patches; the warrants hunk adds VIS-6 and RFC1-12,
   RFC1-20, RFC1-25, RFC2-1, RFC2-15.
3. `scripts/check_docs_review_campaign_partition.py`: total=251
   assigned=251 raw=226 other=25 unmatched=0 overlaps=0. The P-79 Q5 row
   (`docs/README.md:97`) cites round 3 as `REVISE` at `-3-RAW.md:2`, which
   matches the raw. The retained round-3 raw is byte-identical to the
   scratchpad copy (`cmp`).
4. Manifest (rule 3): `git archive` of the subject directory into a scratch
   tree, then `git apply` of all six `proposed/*.patch` (6/6 applied), then
   Python `hashlib` over each file. 11/11 rows match, and the rows are in
   codepoint order. File digest `9f4063d3…` as in the head.
5. Coverage totals, independent parse of the post-apply tree: 613 base
   `.cN` rows; 92 repair `.rN` rows; 77 superseded, 0 absent from base.
   Effective 613 − 77 + 92 = **628**: covered 141, unknown-uncovered 242,
   believed-not-applicable 245. These equal the generated
   `CONTRACT-COVERAGE.md:11` and the packet (`OWNER-DECISION-PACKET.md:207-208`).
   Hand reconciliation from the base dispositions: the six superseded base
   rows are 5 BNA (RFC1-12.c1, RFC1-20.c1, RFC1-25.c14, RFC2-15.c2,
   RFC6-14.c5) and 1 UU (RFC2-1.c12). The 12 added rows are 3 covered, 7 UU
   and 2 BNA, and RFC6-17.r7 moves UU→covered. So: 137+3+1=141,
   237−1+7−1=242, 248−5+2=245. The thirteen `REPAIR_DISPOSITIONS` match the
   patch rows.
6. Impact sweep (Python over `git ls-tree -r -z` + `git show`). At `3ee61c7`:
   1,537 files, 1,533 decoded. `PWB-REQ-007` 113 files / 540 occurrences;
   `dismissed-by-decision` 39/48; `CHALLENGE_STATES` 8/33; `RFC2-15` 45/150.
   The published continuation regex gives 7 lines / 6 files, and the
   published range regex 13 lines / 9 files, of which 7 / 6 span 007. All
   equal `IMPACT-LEDGER.md:36-73`. At `b28bc18` (1,563 files), the extra
   occurrences are all in this package or its three raws, plus one
   range-spanning line in the round-1 raw. The ledger discloses that it did
   not re-run on later bases (`IMPACT-LEDGER.md:7-11`). 12-char spec-digest
   pin `42d073cdeaf7`: 19 files at `3ee61c7`. At HEAD there are 20, the one
   addition being this package's own `proposed/GOVERNING-DEPENDENCIES.md.patch`.
   The only file under `apps/`, `packages/` or `scripts/` that names
   `dismissed-by-decision` is this package's builder.
7. CG-7e / CG-7d: changing one hex character of the bare digest at
   `OWNER-DECISION-PACKET.md:25` gives "FAIL CG-7e … 1 finding". The same
   change at `:161` (the phrase copy) gives "FAIL CG-7d … 1 finding".
   Both restored.
8. Registration diff in `scripts/check_governance.py` (vs `96ee305`) has
   label, dir, subject, act path, `_act_subjects()` entry, an
   `ACT_DIGEST_COPY_FILES` packet row, existence-gated activation and a
   selftest row. It adds no `PWB_SUCCESSOR_CHAIN` link and leaves the CG-26
   lists untouched. The only files outside the package and its raws that
   change are `docs/README.md`, `scripts/check_docs_review_campaign_partition.py`
   and `scripts/check_governance.py`.
9. Commit claims (N-A3): `82cc6c4` and `8cf689d` are only on
   `origin/review-pr-121`, and `82cc6c4`'s parent is `8cf689d`. `6e6d60c`,
   `28b88a3`, `9b18409` and `f5f97b8` are on no remote branch and are not
   ancestors of `b28bc18`. `7d0049c`, `def4d6a`, `21df27a` and `8307180` are
   ancestors. This matches `OWNER-DECISION-PACKET.md:245-260`.
10. Owner-attribution sweep. Python `re`, case-insensitive,
    `\b(ruling|rulings|ruled|chose|decided|answer\w*|you|your)\b`, over the
    10 package files (4 `.md`, 6 patches): 61 hit lines, all read. Every
    owner-attributed quotation was checked against its source:
    - P-79 Q4 ("no promotion, … write act deferred") and Q5 ("dismissal is
      an amendment — CC-REV-2 delta plus a new act before any dismissal
      touches a tuple") match the Ruled cell at
      `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:67`.
    - "slice 4 waits for the dismissal delta, its sign-off and act" is in
      the What-it-means cell. `SEMANTIC-DELTA.md:46-47` now names it "the
      recorder's words rather than the owner's answer".
    - The retention quotes ("the claim identity, the epistemic tuple, and
      the challenge state", "Nothing else", "No record is committed out to
      any governed plane") are in `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md`.
    - ".21 → .30 → .22 → lane B" is the text of the option the owner
      selected verbatim ("Readiness order, lane B last (Recommended)",
      `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:114-118`).
    - "Direction to draft" is labelled the drafter's reading [Inferred] at
      `OWNER-DECISION-PACKET.md:14-18` and `SEMANTIC-DELTA.md:3-8`.
    - `OWNER-DECISION-PACKET.md:176-177` ("ruled 'no promotion' and deferred
      only the write act") and `:97` (quotes "write act deferred") are
      faithful.

    No package proposal is attributed to the owner.
11. VIS-4 sweep: `adopted|accepted|approved|signed off|in force|binds` over
    the same 10 files, excluding "binds nothing" and "signed
    PWB/spec/behav…": 15 hits, all read. All are in contract or clause
    context ("accepted contracts", "binds a record to a claim", "An adopted
    successor stales both pins"). None claims that this package binds or is
    adopted. The phrase is marked not offered (`OWNER-DECISION-PACKET.md:157-168`).

### Rule-6 mutations by this reviewer

Harness A (in-process): take the builder's own `proposed_bytes()`, mutate
`spec.md`, and run `requirement_findings`. The unmutated bytes give 0
findings.

Round-3 survivors and round-3 repairs, re-run: 5/5 killed.
- M2 (in-effect "and" → "or"): KILLED ("lacks in-effect conjunction").
- M7′ (add a refusal route "or names a claim identity the evaluation does
  not carry"): KILLED ("forbidden refusal by an absent claim").
- M14 (Scenario 3 "as lapsed" → "as lapsed and as refused"): KILLED.
- M1 ("not counted in the aggregate's Unknown headline"): KILLED.
- M9 ("A model assertion SHALL dismiss…"): KILLED.

New spec-text mutants: 22 attempted, 22 hit, 11 KILLED, 11 SURVIVED.
- KILLED:
  - Q1: class order swapped.
  - Q2: lapse "not earlier" → "later".
  - Q3: in-effect "earlier than" → "not later than".
  - Q4: claim identity dropped from the refused list.
  - Q6: unreadable set "as Unknown, never as zero" → "as zero".
  - Q7: "counted once" → "counted once per record".
  - Q8: Scenario 3 third record also refused.
  - Q10: uncarried-identity lapse dropped.
  - Q11: "not Unknown" → "neither Unknown nor Inferred".
  - Q21: author dropped from the lapsed disclosure.
  - Q22: Scenario 1 re-read renders "as lapsed".
- SURVIVED, additive contradictions:
  - Q5: add "A record whose author is a model is in effect like any other."
  - Q9: Scenario 1 add "until it is re-read, then with it".
  - Q12: add "(though it renders green)".
  - Q13: add "A page read after the expiry instant shows the claim
    undismissed."
  - Q14: Scenario 2 "refused records" → "refused records or as lapsed
    records".
  - Q20: add "and the Unknown headline shows only undismissed members".
- SURVIVED, substitutions or deletions of required semantics:
  - Q15: "and dismissing a successor needs a new record" → "and the record
    then applies to the successor".
  - Q16: "identically in the human and machine views" dropped from the
    record-class sentence.
  - Q17: Oracle "with the checker's own statement of the rule" dropped.
  - Q18: Case "and a record set that cannot be read" dropped.
  - Q19: Falsifier "or an unreadable record set yields a dismissed or
    record-class count of zero" dropped.

Builder-source mutants: 11 run with `--check` and `--selftest`; 9 KILLED,
2 SURVIVED.
- KILLED:
  - B1: delete a `PARAGRAPH_RULES` entry. The selftest fails "135 mutants
    killed, expected 136".
  - B2: weaken the "retired identity" rule to its last clause. The selftest
    fails "round-3 mutation passed: world-side retirement".
  - B4, B5: delete a `FORBIDDEN` entry ("forbidden fixtures do not cover
    every forbidden wording").
  - B6: skip the scenario forbidden-wording check.
  - B7: drop RFC1-12 from `REQUIRED_WARRANTS`.
  - B8: expect RFC1-12.r3 `covered`. `--check` fails.
  - B9: lane-B spec "collide" → "compose".
  - B11: `EXPECTED_KILLED` 136 → 135.
- SURVIVED:
  - B3: weaken the "unreadable record set" rule to "When an evaluation
    cannot read that record set". `--check` 0 and `--selftest` 0, still
    reporting 136.
  - B10: remove `re.IGNORECASE` from `forbidden_findings`. `--check` 0 and
    `--selftest` 0.

## Resolution of round-3 findings

| # | Round 3 | Status | Evidence |
|---|---|---|---|
| R1 | revise | Resolved | Refusal now tests only the record itself: it "lacks an author, reason, expiry instant, claim identity or dismissed primary reason, or itself names … a primary reason that may not be dismissed; a record is never refused because of the state of the claim it names" (`proposed/spec.md.patch:43-47`). Retirement is evaluation-side ("the evaluation records the claim identity it names as retired by a split or merge", :47-48), in the same words as Scenario 3's WHEN (:123-124). An uncarried identity is a lapse condition (:52). Scenario 3 adds the third record (:125, :131-132). The packet gloss now says "no longer shows the claim it names — for example because the declaration behind it was deleted" (`OWNER-DECISION-PACKET.md:60-62`). My mutants Q4, Q10 and M7′ are killed. |
| N-A1 | note | Resolved | The lapse tests say "is not" (:51-54). The condition "names the test that failed and never states whether the record once took effect" (:58-60). |
| N-A2 | note | Resolved | See command 10. |
| N-A3 | note | Resolved | See command 9. A dated correction at `OWNER-DECISION-PACKET.md:253-259`, and `IMPACT-LEDGER.md:7-11` records both later bases. |
| N-B1 | note | Resolved as stated | M2, M7′ and M14 are killed. The `SCENARIO_ONCE` population is asserted as a literal (`scripts/build_pwb_dismissal_expiry_amendment.py:1056-1059`) and the total is fixed at 136 (:284, :1060-1061). B1 and B11 confirm the fixed total catches a removed rule. The weakening of a rule's *string* is still not caught (B3 below). |
| N-C1 | note | Resolved | RFC1-12.r1 is narrowed to the no-transfer rule, and RFC1-12.r3 is `unknown-uncovered` (`proposed/CONTRACT-COVERAGE-REPAIR-DELTA.md.patch:29-30`). The conditional credit is labelled in `IMPACT-LEDGER.md` and at `OWNER-DECISION-PACKET.md:197-203`. The builder pins RFC1-12.r3's disposition (B8 killed). |
| N-C2 | note | Resolved in the bytes | `proposed/spec.md.patch:12-15`; Case (:70) and Falsifier (:88-89). The builder guard on these lines is weak (Q18, Q19, B3; see N-B2). |
| N-C3 | note | Resolved | "When more than one record is in effect for the same claim, each is disclosed that way beside the claim and the claim is counted once as dismissed" (:33-34). Q7 is killed. |

## New findings

### R2 — revise — a complete record with a non-human (or non-owner) author is in no class, or else it is in effect (criterion 8; criterion 6 consistency)

[Observed] The paragraph admits the sibling state "only under a dismissal
record: an attributed human decision" (`proposed/spec.md.patch:7-8`). It
says "Nothing else dismisses a claim: not … an owner note or a model
assertion" (:19-20). The in-effect test lists three conditions only: the
identity is carried, the as-of instant is before the expiry, and the reason
matches (:21-24). The refused test checks only that an author is *present*
("lacks an author", :44). No test asks whether the author is a human
decision-maker.

[Inferred] Take a complete record in the governed plane whose author field
names a model or agent. Agents commit governed-plane files in this
repository, and the packet's question 2 contemplates Syzygy one day
writing records. If the record names a carried Unknown claim, a dismissable
primary reason and a future expiry, it meets none of the three class tests:
- not refused: it has an author, and its own reason is dismissable;
- not retired;
- not lapsed: every lapse test passes.

That leaves two readings, and both break a stated claim:
- It is in effect, because the three in-effect conditions hold. This
  contradicts "only under … an attributed human decision" and "Nothing
  else dismisses a claim: … a model assertion", and the packet's "never …
  a model" (`OWNER-DECISION-PACKET.md:37-38`).
- It is not a dismissal record, so it dismisses nothing. It is then
  disclosed in no class, which contradicts "A record that dismisses nothing
  is disclosed in exactly one of three classes" (:39-40) and the packet's
  "shown as exactly one of three things" (`OWNER-DECISION-PACKET.md:54`).

Criterion 8 asks that "the refused-record cases close every way a record
could dismiss without authority". An unauthorized author is the most direct
such way, and the refused test does not close it. The same gap reopens with
a different predicate if the owner answers question 3 with "the owner"
(`OWNER-DECISION-PACKET.md:100-104`): a record by any other human would then
be unclassified or in effect.

Mutant Q5 ("A record whose author is a model is in effect like any other.")
survives every check.

Repair options (drafter's choice, or route to the owner as part of question 3):
- Make author authority a refused test on the record itself. For example,
  "or names an author who is not [a human decision-maker | the owner]".
  This keeps refusal record-intrinsic, consistent with "never refused
  because of the state of the claim it names".
- State in the paragraph how an evaluation decides "human", or that it
  cannot. If it cannot, say which class an unverifiable author falls in.
- Add the case to Scenario 2's refused list and to the Case sweep.

### N-A4 — note — Scenario 3's third record does not exclude a retired identity

[Observed] Scenario 3 says the third record "names a claim identity the
evaluation does not carry" and is disclosed "as lapsed"
(`proposed/spec.md.patch:125`, :131-132). Under the stated order, a record
whose identity the evaluation does not carry *and* records as retired is
bound to a retired identity (:41-48). [Inferred] Read literally, the
third-record WHEN admits a retired identity, and the THEN would then
contradict the paragraph. The contrast with the second record makes the
intended reading clear, so this is not blocking. "a claim identity the
evaluation neither carries nor records as retired" would close it. The
builder rule "uncarried identity lapses" pins the THEN only.

### N-A5 — note — malformed-but-present values and where refused records are shown

[Inferred] Three small gaps:
- A record whose dismissed primary reason is outside RFC2-24's twelve (or
  whose expiry instant is present but unparseable) is not refused, because
  the refused test lists absence and the two undismissable reasons only. It
  falls to lapsed ("the claim's primary reason is not the one it
  dismissed"). A malformed record is then shown as a valid record that
  lapsed. It never dismisses anything, so VIS-2 polarity is safe.
- The paragraph says where lapsed records are disclosed (:55-57) and where
  retired ones are (:49), but not where a refused record is disclosed.
  That matters most for one that lacks a claim identity.
- The in-effect test does not itself require the claim to be Unknown. It
  relies on RFC2-24 "cover[ing] Unknown states only" to make "including
  because the claim is not Unknown" (:54) a case of reason mismatch. That is
  sound under RFC2-24 as accepted, but unstated.

### N-A6 — note — plain-language "its expiry has passed" at the boundary

[Observed] `OWNER-DECISION-PACKET.md:60` glosses the first lapse test as
"its expiry has passed". The spec lapses a record at an as-of instant
*equal* to the expiry (:51), and Scenario 1 tests equality (:97). "Has been
reached" would be exact. The packet's own line 44 ("before the expiry") is
exact.

### N-B2 — note — builder guards: Case, Oracle and Falsifier extensions are unpinned; rule strings can be weakened

[Observed] None of the three extended bullets (`proposed/spec.md.patch:66-70`,
:75-77, :82-89) is a builder rule. Deleting the N-C2 Case clause (Q18), the
N-C2 Falsifier clause (Q19) or the Oracle clause (Q17) survives. Q15 (the
successor-transfer reversal) and Q16 (dropping parity from the
record-class sentence) survive because each rule pins only a prefix of its
sentence. A rule string weakened in the builder (B3) survives both
`--check` and `--selftest`, because each rule's selftest mutant is derived
from the rule itself. Only the round-3-specific fixture caught B2.
Case-insensitivity of `FORBIDDEN` is not self-tested (B10).

[Inferred] The manifest digest remains the real guard on these bytes. The
packet does not claim more (`OWNER-DECISION-PACKET.md:321` describes what
is pinned, accurately). The N-C2 disposition's "The Case and Falsifier lines
cover it" (`:323`) is true of the spec bytes, not of the builder.

## Confirmed without finding

[Observed] The following hold at the reviewed commit:
- No wall clock. The in-effect test uses the evaluation's own as-of
  instant (:21-26). Scenario 1 re-reads the first evaluation after the
  expiry and requires the same claim state (:100-101). "Earlier than" (:23)
  and "not earlier than" (:51) are exact complements, and equality means
  lapsed.
- No tuple value changes (:35). The challenge vocabulary is untouched.
  RFC2-13's `resolved-dismissed` is kept distinct (`SEMANTIC-DELTA.md:246-252`).
- VIS-2 per claim and per aggregate. Dismissed members stay in every
  label, tier, freshness and reason count (:37-38). An unreadable or
  homeless record set gives Unknown counts, never zero (:12-15).
- Every record state named in the brief maps to one disclosed class under
  the stated order:
  - refused (record-intrinsic);
  - retired (evaluation records a split or merge);
  - lapsed (expiry reached, identity uncarried, reason mismatch including
    never-matched);
  - in effect;
  - several in effect (each disclosed, counted once);
  - unreadable set (Unknown counts).

  The exception is R2's state.
- Scenario 2's refused cases agree with the paragraph.
- Proposal, capability row 32 and totals 26/6/32 are consistent.
- The six patched and five unchanged subjects match (command 4).
- No adoption is claimed (VIS-4), and no bound byte outside the package is
  edited.
- No observed-repository path appears in this raw.

## Verdict

REVISE. R2 blocks. A reachable record state, a complete governed-plane
record whose author is not a human decision-maker, is either in effect,
against the paragraph's own source rule, or in no class, against "exactly
one of three classes". Criterion 8's requirement that refusal closes every
unauthorized route is not met. It can be repaired in the bytes with a
record-intrinsic refused test on author authority, or folded into packet
question 3 with the class stated for each answer. Notes N-A4, N-A5, N-A6
and N-B2 do not block. The owner-only questions still open are the packet's
Q1 to Q12.
