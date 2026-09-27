# R-DOV29-2 — confirmation review of PR #121
Verdict: REVISE
Reviewed commit: 82cc6c4cd22037fdd33c15894a4e116afad4d042
Manifest sha256: dec888c6399cad83d35da6b7a24a63ed458ae5ab2db272dda6d16ab6c670c91d

Reviewer: fresh-context confirmation reviewer, read-only. Worktree of
`origin/agent/tier4-dov29` at the reviewed commit, parent `origin/main`
`66114ac`. Nothing edited on any branch; nothing pushed. Subject: the package
`.syzygy/governance/contracts/candidates/pwb-dismissal-expiry-amendment/`,
`scripts/build_pwb_dismissal_expiry_amendment.py`, its `check_governance.py`
registration, and the campaign row. Binding is to the manifest digest above,
not to the commit (the packet names `9b18409` → `f5f97b8`; the branch now
sits on `8cf689d`, see note N10).

## Commands run and outputs read

All [Observed] at the reviewed commit unless labelled.

1. Manifest digest, two methods: `sha256sum PWB-DISMISSAL-EXPIRY-MANIFEST.txt`
   and Python `hashlib.sha256(open(...,'rb').read())` both give
   `dec888c6399cad83d35da6b7a24a63ed458ae5ab2db272dda6d16ab6c670c91d`, equal
   to the copy in `OWNER-DECISION-PACKET.md:22` and the phrase line at `:133`.
   Manifest: 11 rows.
2. `python3 scripts/build_pwb_dismissal_expiry_amendment.py --check` — exit 0;
   output reads "11 proposed subjects (6 patched, 5 unchanged)" and "15
   declared sibling-composition outcomes and the sequential sibling order
   verify". `--selftest` — exit 0, 102 mutants, 102 killed (read per-line).
   `--diff` — exit 0, diff equals the six proposed patches.
3. `python3 scripts/check_governance.py` — 52 checks: 32 OK, 20 WARN, 0 FAIL,
   exit 0. Same headline at base `66114ac`; the diff of the two outputs is
   denominators (1542 → 1555 files) plus the new subject/registration lines.
   CG-1b OK (6927 refs), CG-7d WARN (62 quotations, 0 findings), CG-7e OK
   (40 files), CG-15 OK, CG-22 OK, CG-26 OK (36/36). `--selftest`: 268
   fixtures, 0 failing.
4. `python3 scripts/check_docs_review_campaign_partition.py` — total=243
   assigned=243 raw=218 other=25 unmatched=0 overlaps=0; `docs/README.md`
   states 54 rows over 243 files. Consistent at this commit (it will move by
   one when this raw lands).
5. IMPACT-LEDGER counts at the ledger's pinned base `3ee61c7` (1,537 tracked
   files, 4 undecodable PNGs excluded), two methods (`git grep -l`/`git grep
   -o | wc -l`, and a Python bytes sweep over `git ls-files`):
   `PWB-REQ-007` 113 files / 540 occurrences; `dismissed-by-decision` 39/48;
   `CHALLENGE_STATES` 8/33; `RFC2-15` 45/150; signed spec path 72/163;
   generated-dependencies path 20/37. All equal the ledger. Spec digest pins
   (full and 12-char): 19 files, list equal to the ledger's. Subject paths are
   unchanged `3ee61c7` → `66114ac`.
6. Continuation and range forms. Regex used (Python `re`, case-sensitive):
   `(?:,|/|\.\.|\band)\s*007\b` on lines containing `PWB-REQ-` but not
   `PWB-REQ-007` → 7 lines / 6 files, equal to IMPACT-LEDGER.md:41-44. Range
   regex `PWB-REQ-(\d{3})\s*(?:\.\.|–|-|…|to)\s*(?:PWB-REQ-)?(\d{3})` → 13
   lines / 9 files, of which 7 lines / 6 files span 007, equal to the ledger.
   A broader form sweep finds a hyphen-suffix form `-007` in 3 lines / 3
   files (see N8); none is substantive.
7. Coverage totals, two methods over post-apply bytes.
   (a) Arithmetic: base 613 rows (220+183+210); repair rows 80/71/61/16/3 →
   91/77/65/20/6 (11 new repair rows; 6 newly superseded base rows: RFC1-12.c1
   BNA, RFC1-20.c1 BNA, RFC1-25.c14 BNA, RFC2-1.c12 unknown-uncovered,
   RFC2-15.c2 BNA, RFC6-14.c5 BNA; plus the RFC6-17.r7 flip). Effective
   622−6+11 = 627; covered 137+4 = 141; unknown 237−1+5−1 = 240; BNA
   248+3−5 = 246.
   (b) Parse: applied `CONTRACT-COVERAGE-REPAIR-DELTA.md.patch` to a scratch
   copy, parsed every matrix row with ID regex `^RFC\d+-\S+\.c\d+[a-z]?$`
   (base 613; a first pass without `[a-z]?` missed `RFC3-7.c2a`/`c2b` and was
   discarded) and every repair row `^RFC\d+-\S+\.r\d+[a-z]?$` (91), removed
   77 superseded base IDs (0 superseded IDs absent from base) → 627 effective:
   covered 141, unknown-uncovered 240, believed-not-applicable 246. Equal to
   (a) and to the generated `CONTRACT-COVERAGE.md` line.
   Dependencies: 100 distinct (doctrine 9, contracts 71, policies 13,
   decisions 2, topology 0, parent requirements 5), was 96.
8. Quotations (rule 8): every blockquote in `SEMANTIC-DELTA.md` was located,
   whitespace-folded, at its definition site — RFC1-5, RFC1-12, RFC1-18,
   RFC1-20, RFC1-25, RFC2-1 item 9, RFC2-13, RFC2-15, RFC2-24 rows 8-9,
   RFC2-25, RFC6-14, RFC6-17, doctrine `vision.md` :174 and :181, the M12
   funnel arms 1-3 and slice-4 lines 1298-1301, and the retention direction
   (elision marked). Owner-attributed quotes match ruled text: P-79 Q5 and Q4
   words, the retention direction, and the landing order, which the packet
   quotes only as ".21 → .30 → .22 → lane B" (POLARIS-GATE-PACKAGE-OWNER-
   VALUES-2026-09-23-DECISION.md :110-120).
9. Sequential composition (scratch tree from `66114ac`): `.21` spec; `.30`
   spec + capability + design; `.22` spec; `.20` spec + capability +
   proposal; then this package's spec + capability + proposal — every patch
   applied cleanly with `git apply`. PWB-REQ-007 scenario order after all
   five: "No effective currency bound…", "Missing current evidence…", then the
   three dismissal scenarios. Capability totals 26/6/32.
10. VIS-4 sweep: the phrase is marked not offered (packet :135-136); a sweep
    for `adopted|accepted|approved|signed off` over the package returns hits
    only in contract/act context, none claiming this package binds. No
    `PWB_SUCCESSOR_CHAIN` link added. CG-26 untouched.
11. Rule-6 mutations by this reviewer (mutate the post-apply spec, regenerate
    the spec and dependency patches, `--write`, then `--check` and
    `check_governance.py`):
    - KILLED: P1 expiry boundary flipped ("not earlier than" → "later than");
      P2 aggregate "remain in" → "leave"; P6 retired record "never
      transferred" → "transferred"; P7 drop "identically in the human and
      machine views"; P8 insert read-time expiry; S2 Scenario 3 "neither …
      refused" → "both … refused"; S3 drop Scenario 2 aggregate line; W1 drop
      the RFC2-1 warrant; W2 drop the VIS-2 warrant (generator error); C1
      RFC2-15.r1 → covered; C2 RFC6-17.r7 → BNA; M1 one hex flip in the
      manifest; K1 a composition outcome compose → collide; phrase-line
      digest flip in the packet (CG-7d FAIL).
    - SURVIVED (`--write` 0, `--check` 0, governance 0 FAIL): P3 add "A
      dismissed Unknown claim is removed from the aggregate's Unknown total.";
      P4 drop "including because the claim is no longer Unknown" (arguably
      equivalent); P5 "It is a lapsed record when" → "It is a refused record
      also when"; P9 add "a model assertion MAY dismiss"; P10 drop a fact from
      the disclosure list; S1 add to Scenario 1 "once the expiry passes, the
      first evaluation renders the claim without the sibling state".
    - The bare digest copy at `OWNER-DECISION-PACKET.md:22` mutated by one hex
      character passes every check (CG-7d and CG-7e 0 findings); the same is
      true of the missing-currency packet's `:22` at base (N11).

## Resolution of round-1 findings 1–18

| # | Round 1 | Status | Evidence |
|---|---|---|---|
| 1 | revise | Resolved | Quotes at source; inferences labelled; RFC1-20.r1, RFC1-25.r1, RFC2-15.r1 held unknown-uncovered; routed to packet Q4 |
| 2 | revise | Resolved, with N2 caveat | Three disclosure classes defined (spec.md.patch:33-46); classes overlap (N2) |
| 3 | revise | Partially resolved | Lapsed-vs-refused now defined, but Scenario 2 contradicts the paragraph and Scenario 3 (N1) |
| 4 | revise | Resolved | Retired identity never transferred; successor needs new record (:43-46) |
| 5 | revise | Resolved | Same facts, human and machine (P7 killed) |
| 6 | revise | Resolved in text; guard overstated | :31-33 keeps members in every per-label, tier, reason count; P3 survives (N4); freshness omitted (N3) |
| 7 | revise | Resolved by routing | Record home and author routed to packet Q2/Q7 (see N5) |
| 8 | revise | Resolved in delta; packet partial | SEMANTIC-DELTA maps drafted arm to funnel arm 2; packet Q1 does not (N6) |
| 9 | revise | Resolved for unadopted-draft | Residual polarity mismatch for editorial-draft/challenge-pending (N7) |
| 10 | revise | Resolved | 113/540 reproduced two ways (command 5) |
| 11 | revise | Resolved | Q10 text matches the continuation act's trigger quote |
| 12 | note | Partially resolved | Scenario body rules and forbidden wordings added; mutants P3, P5, P9, S1 survive (N4) |
| 13 | note | Resolved | Boundary exact ("not earlier than"); Scenario 1 tests equality; P1 killed |
| 14 | note | Resolved | challenge-suspended exclusion argued; routed to Q12 |
| 15 | note | Resolved | Coverage totals 627/141/240/246 reproduced two ways |
| 16 | note | Resolved | Dependencies 100, family split verified |
| 17 | note | Resolved, residual | Continuation forms counted; predicate in words only (N8) |
| 18 | note | Resolved | Sequential composition check present in builder and reproduced (command 9) |

## New findings

### N1 — revise — Scenario 2 contradicts the paragraph and Scenario 3

[Observed] The paragraph defines refused as a record that "names a primary
reason that may not be dismissed" (`proposed/spec.md.patch:38`) and lapsed as
a record "otherwise complete" where "the claim's primary reason is no longer
the one it dismissed" (:38-41). Scenario 3 ("A record that no longer applies
is lapsed or retired, never refused", :102-111) confirms that a complete
record whose dismissed reason is no longer the claim's reason is lapsed and
"neither record is disclosed as refused" (:111). Scenario 2 (:97-100) says "a
record naming a claim whose primary reason is
`contradicted-pending-adjudication` or `challenge-suspended`, each dismiss
nothing and are disclosed as refused records". A complete record that
dismissed a dismissable reason, on a claim whose current primary reason has
since become `contradicted-pending-adjudication`, is lapsed by the paragraph
and Scenario 3 and refused by Scenario 2. The builder hard-codes the Scenario
2 sentence as a required rule
(`scripts/build_pwb_dismissal_expiry_amendment.py:188-191`), so the
contradiction is locked in. Repair: Scenario 2 should say the record *names*
(dismisses) such a reason, not that it names a claim whose reason is one.
This is the residue of round-1 finding 3.

### N2 — revise — "exactly one of three classes" over overlapping definitions

[Observed] :33-35 require each non-dismissing record to be disclosed "in
exactly one of three classes, each distinct from the others". The refused
test (:35-38) and the lapsed test ("otherwise complete", :38-39) exclude each
other, but the retired-identity test (:43-45) has no completeness or expiry
guard and no precedence: (a) an incomplete record naming a retired identity
satisfies refused and retired; (b) a complete record naming a retired
identity whose expiry has passed satisfies lapsed and retired. The Falsifier
(":71" "discloses a lapsed or retired-identity record as refused") cannot be
decided on case (a). Repair: state a precedence (for example refused, then
retired, then lapsed) or guard the retired test.

### N3 — note — freshness counts not named

[Observed] The aggregate sentence (:31-32), Scenario 2 and the Falsifier keep
dismissed members in "per-label, tier and reason" counts only. RFC6-17
(RFC-0006 :273-296) requires per-freshness-state counts in the aggregate as
well. [Inferred] A reading that lets a dismissal move a member out of a
freshness count is not excluded; mutant P10 survives. Interacts with `.20`'s
outside-slot disclosure.

### N4 — note — builder still presence-only for VIS-2 aggregate removal

[Observed] Mutants P3 (adds "A dismissed Unknown claim is removed from the
aggregate's Unknown total."), P5, P9 and S1 survive every check. The four
forbidden patterns are clock, hide, collapse and expire-on-read
(`build_pwb_dismissal_expiry_amendment.py:200-205`); none concerns aggregates.
The packet's disposition of finding 6 ("a Falsifier line and a
forbidden-wording rule check it", `OWNER-DECISION-PACKET.md:224`) and of
finding 12 (":230") overstate the guard. The only guard on those bytes is the
manifest digest itself. [Inferred] Adding forbidden patterns for "removed
from", "leave the Unknown", "refused record also", "model assertion MAY" and a
Scenario-1 post-expiry-render rule would kill them.

### N5 — note — packet Q2 pre-answers part of the question

[Observed] `OWNER-DECISION-PACKET.md:69-71` glosses "committed to the governed
plane" as "in Syzygy's own governed files, never in the observed repository",
unlabelled. [Inferred] The M12 funnel's Q4 reading of VIS-6(a) promotion is
into the observed project's governed plane; the gloss narrows the owner's
choice before asking it. Label it [Inferred] or present both readings.

### N6 — note — packet Q1 does not map the arm to the funnel

[Observed] :62-67 describe the arms in package terms and attribute only the
challenge-widening arm to "the M12 funnel's framing". SEMANTIC-DELTA now says
the drafted arm is closest to funnel arm 2 and carries L2-M8's objection; the
packet does not tell the owner so.

### N7 — note — residual polarity mismatch in RFC6-14.r5

[Observed] RFC6-14.r5 is believed-not-applicable for editorial-draft and
challenge-pending travel, while RFC6-17.r8 (editorial-draft aggregate) and
RFC6-17.r5 (challenge state) are unknown-uncovered. Same class as round-1
finding 9, not repaired for these two states.

### N8 — note — continuation predicate published in words

[Observed] IMPACT-LEDGER.md:41-43 publishes the continuation predicate in
words; the regex in command 6 reproduces it (7/6). The hyphen-suffix form
`-007` occurs in 3 lines / 3 files (`docs/design/POLARIS-M11-OPERABILITY-
FUNNEL.md:1658`, `docs/evidence/polaris-m11-operability-funnel-2026-09-15.json:1011`,
`docs/reviews/R-POLARIS-M11-OPERABILITY-FUNNEL-2-RAW.md:66`), outside the
predicate; none is substantive. Publish the regex (AGENTS.md lesson).

### N9 — note — "deferred" misstates the question-4 ruling

[Observed] `OWNER-DECISION-PACKET.md:147` says promoting notes into
governance was deferred by "your question-4 answer". The ruling declined
promotion and deferred the write act; promotion was not deferred.

### N10 — note — review record names a stale repair base

[Observed] :212-213 say the branch was rebased to `f5f97b8` and the repair
made there. The reviewed commit's parent is `8cf689d`; `f5f97b8` is on no
remote branch. Package and builder bytes are identical between the two, so
the manifest binding is unaffected.

### N11 — note (systemic, pre-existing) — bare packet digest unguarded

[Observed] A one-character change to the bare digest at
`OWNER-DECISION-PACKET.md:22` passes CG-7d and CG-7e with 0 findings; so does
the same edit to the missing-currency packet's `:22` at base. AGENTS.md says
CG-7e catches bare copies; for these files it does not. Not a defect of this
package; file separately.

## Confirmed without finding

[Observed] VIS-2 per claim: only Unknown claims are dismissable; the Unknown
label and tuple are unchanged; dismissed members stay in per-label, tier and
reason counts. RFC2-13 `resolved-dismissed` stays distinct.
`CHALLENGE_STATES` and implementation files untouched. No adoption claim
(VIS-4). No Butlers path is quoted in this raw.

## Verdict

REVISE — N1 and N2 make the class rules contradictory or undecidable for
reachable record states. Notes N3–N11 do not block on their own.
