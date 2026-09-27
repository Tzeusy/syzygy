# R-DOV29 — PWB-REQ-007 dismissal-with-live-expiry delta — raw review

REVISE

- Reviewed commit: `9b1840941ab5b118cce9fff08326a6d0eb61c6aa` (PR #121, `agent/tier4-dov29`)
- Baseline: `3ee61c7` (the package's declared base); also merged onto `origin/main` `23b486c` for a drift check
- Package: `.syzygy/governance/contracts/candidates/pwb-dismissal-expiry-amendment/`
- Reviewer context: fresh; read-only; detached scratch worktrees only (`rv-121`, `rv-121-base`, `rv-121-mut`). Nothing on the branch or in the main checkout was edited.
- Packet argument recomputed by script: sha256(`PWB-DISMISSAL-EXPIRY-MANIFEST.txt`) = `460cb535e43e0921f470298dcf5546a1aa53ae92d01332c74c8d3b2b7da85d46`, equal to OWNER-DECISION-PACKET.md:21 and :112. [Observed]

## Commands run and results (with denominators)

| # | Command (worktree) | Result |
|---|---|---|
| C1 | `python3 scripts/check_governance.py` @9b18409 | `32 OK, 20 WARN, 0 FAIL (52 checks)`, exit 0. Same headline at 3ee61c7; diff of the two outputs changes only denominators (CG-7d → 28 subjects / 62 quotations; CG-7e → 39 files). No new WARN. [Observed] |
| C2 | `python3 scripts/check_governance.py --selftest` | 268 fixtures, 0 failing (base 265; +3 are the dismissal-expiry rows). [Observed] |
| C3 | `python3 scripts/build_pwb_dismissal_expiry_amendment.py --check` | exit 0: "11 proposed subjects (6 patched, 5 unchanged) … 15 declared sibling-composition outcomes verify". [Observed] |
| C4 | builder `--selftest` | exit 0, 67 mutants killed of 67. [Observed] |
| C5 | builder `--diff` | exit 0. [Observed] |
| C6 | C1 + C3 + C4 after merging PR onto `origin/main` 23b486c | all clean; no drift on any of the 11 subject paths since 3ee61c7. [Observed] |
| C7 | Sequential composition: apply .21, .30, .22, .20 spec patches in order, then this spec patch | applies; scenario order: .20 "No effective currency bound…", "Missing current evidence…", then the two dismissal scenarios. [Observed] |
| C8 | Every SEMANTIC-DELTA blockquote vs its definition site (whitespace-folded exact match) | all match; RFC2-13 "the claim's deterministic status is restored" found. [Observed] |
| C9 | Impact sweep at 3ee61c7 over 1,537 tracked files (4 undecodable, skipped and counted), Python `str.count` and `git grep -o` as two methods | see finding 10 and table below. [Observed] |
| C10 | Coverage totals, second method (base matrix − superseded rows + repair rows) | Δ +3 rows, +6 covered, −1 Unknown, −2 BNA; equals generator 622/137/237/248 → 625/143/236/246; repair rows 88 = 67/16/5; regenerated == applied. [Observed] |
| C11 | Hygiene sweeps | no backticked Butlers paths in the package (CG-1b clean); `PROJECT-STATUS.md` and `.github/**` untouched by the PR. [Observed] |

Impact sweep (C9), both methods agreeing:

| Token | Files / occurrences at 3ee61c7 | Ledger |
|---|---|---|
| `PWB-REQ-007` | 113 / 540 (`git grep -c` counts lines: 515) | 114 / 541 — mismatch |
| `dismissed-by-decision` | 39 / 48 | match |
| `CHALLENGE_STATES` | 8 / 33 | match |
| `RFC2-15` | 45 / 150 | match |
| spec path | 72 / 163 | match |
| dependencies path | 20 / 37 | match |
| spec digest pins | 19 files | match (IMPACT-LEDGER.md:85-91) |
| continuation forms | 7 lines / 6 files | match (IMPACT-LEDGER.md:37-43) |

No `dismissed-by-decision` in `apps/`, `packages/`, `scripts/`; `CHALLENGE_STATES = ['unchallenged']` at `packages/three-surface-poc-core/src/project-shape-model.ts:83`. [Observed]

## Rule-6 mutations run by the reviewer (independent of the builder's 67)

Method: apply patches to a scratch tree, mutate the post-apply spec (or package file), regenerate the patch with `git diff -U1`, run builder `--check`; revert after each. 12 mutants.

| id | Mutation | Outcome |
|---|---|---|
| M1 | "SHALL not change" → "MAY change" in the new paragraph | killed ("lacks no tuple change") |
| M2 | delete Scenario 1's "reading the first evaluation again after the expiry instant has passed renders the same claim state" | killed only by dependencies digest + manifest; survives after `--write` (see M2+M5) |
| M3 | drop RFC2-15 from the warrants | killed |
| M4 | coverage row RFC6-14.r5 → unknown-uncovered | killed (totals) |
| M5 | add "A page MAY hide a dismissal once the reader's clock passes its expiry instant." | killed only by digest + manifest |
| M2+M5 | both, then regenerate GOVERNING-DEPENDENCIES patch and `--write` | **survived** `--check` (exit 0). Only the packet digest (CG-7d) would then catch it. |
| M6 | aggregate clause folded ("count dismissed members separately" removed) | killed |
| M7 | flip one hex digit in a manifest row | killed |
| M8 | drop one manifest row | killed |
| M9 | declared lane-B outcome → "compose" | killed |
| M10 | drop one DECLARED_COMPOSITION pair | killed |
| M11 | delete .21's spec patch (sibling drift) | killed |
| M12 | weaken REQUIRED_WARRANTS in the builder itself | survived (expected: the builder cannot guard its own rule table) |
| Mpk | mutate one digest copy in OWNER-DECISION-PACKET.md | CG-7d FAIL and CG-7e FAIL |

## Findings

### 1. REVISE — The paragraph binds a Claim; the contract's `dismisses` edge targets a Gap. The equation of the two is unquoted and unlabelled in the delta.

Criteria: contract fit, rule 8, labels.

Evidence:
- `RFC-0001-project-graph-identity-state-planes.md:514`, the `dismisses` row, types the edge Decision → Gap (durable identity).
- RFC1-5's entity table (same file, §3.2, from :147) lists "Gap | Kernel (derived) | V0 surfaces absence; V1 computes gaps", and :870 has "Gap computation (V1) — V0 surfaces absence".
- RFC1-18 (:326-331) gives Claim and Gap separate two-level identity. Its sentence "a dismissal recorded at one evaluation still binds the same gap at a later one" is about a gap.
- `proposed/spec.md.patch` (new paragraph, patch lines 7-32) binds the dismissal to "semantic Claim identity".
- `proposed/CONTRACT-COVERAGE-REPAIR-DELTA.md.patch` marks RFC1-25.r1 ("`dismisses`… a decision with mandatory reason and expiry") and RFC2-15.r1 covered.
- The claim-equals-gap reading appears only as an inference in OWNER-DECISION-PACKET.md Q4 (:66-69). SEMANTIC-DELTA.md never quotes RFC1-18 or the Gap row.

A "covered" row that rests on an unquoted inference is rule 8 in its plainest form.

Fix:
- Quote RFC1-18 and the Gap entity row in SEMANTIC-DELTA.md.
- Label the claim-as-gap mapping `[Inferred]` in the delta and in the r1 rows.
- Either hold RFC1-25.r1 and RFC2-15.r1 at unknown-uncovered until the owner answers Q4, or add a clause stating which gap a claim-level dismissal binds. Consider whether RFC1-26 (edge re-typing) is engaged.

### 2. REVISE — RFC1-12 is omitted. After an identity change, a predecessor's dismissal must render as bound-to-retired-identity, but the paragraph refuses it.

Criteria: contract fit, impact completeness.

Evidence:
- RFC-0001 RFC1-12 (:277-283; violation example :790): after a split or merge, the predecessor's dismissal "renders as bound-to-retired-identity", and re-dismissal is an owner act.
- The new paragraph: "A record that lacks an author, reason or expiry instant, names no claim the evaluation carries, … dismisses nothing, and the evaluation discloses it as a refused record."

A record whose claim identity was retired by split or merge falls under "names no claim the evaluation carries", so it would be disclosed as *refused*. RFC1-12 requires the distinct bound-to-retired-identity rendering. Neither the ledger nor the coverage rows name RFC1-12.

Fix: add the RFC1-12 case, distinct from a refused record, plus a scenario, a warrant, and a ledger/coverage row.

### 3. REVISE — Refused and lapsed are conflated between the paragraph and Scenario 2.

Criteria: faithfulness, VIS-2 honesty of rendering.

Evidence:
- The paragraph: "its reason is current only while the claim's primary reason is still the one the record dismissed". That is a lapse condition, and its refused enumeration (quoted in finding 2) does not include it.
- Scenario 2 (patch lines 71-80) lists "a record whose dismissed primary reason no longer matches" among records that "dismiss nothing and are disclosed as refused records".

Consider a claim that becomes Verified or Contradicted by new evidence. A valid, owner-authored record would then be shown as "refused", which misstates the owner's act. The paragraph and the scenario also disagree with each other: the scenario asserts a disclosure class the normative text does not define.

Fix: define a *lapsed* (no-longer-applicable) disclosure distinct from *refused*, and align Scenario 2. Either keep the reason-drift case in its own scenario or move it into the paragraph's enumeration deliberately.

### 4. REVISE — Scenario 1's "with the same tuple values" is false for a conforming implementation.

Evidence:
- Scenario 1 (patch lines 59-69): "**AND** the second evaluation renders the claim without the sibling state and with the same tuple values".
- Freshness is as-of-dependent (RFC2-10). The primary reason can move to `stale-beyond-currency-bound` (RFC2-24 #4) purely because the second evaluation's as-of instant is later.

The scenario therefore mandates that the second evaluation reproduce the first one's freshness and reason. That contradicts the clauses it sits among, and it also contradicts .20's currency scenario, which lands just before it (C7).

Fix: condition the claim, e.g. "over the same snapshot, every tuple value the claim carries is unchanged by the dismissal", or assert only that the sibling state is absent and that the dismissal changed no tuple value.

### 5. REVISE — RFC2-15's "on the primary surface" is not carried into the paragraph.

Criterion: rule 8, a quote that is present but not implemented.

Evidence:
- RFC-0002 `reconciliation-chain.md` RFC2-15 (:71-95): "Dismissal is not erasure… stay visible beside the dismissal **on the primary surface**, for the whole time the dismissal stands."
- The new paragraph says the facts "stay visible and unchanged beside the dismissal's reason, expiry instant, author and record identity, identically in the human and machine views".

"Stay visible" admits a collapsed `<details>` or a secondary route, which is exactly what RFC2-15 excludes. The delta quotes the clause but the proposed text drops its operative qualifier.

Fix: add "on the same surface as the claim, without further disclosure" (or the clause's own words).

### 6. REVISE — The aggregate sentence can be read to let dismissed Unknowns leave the Unknown counts (VIS-2).

Evidence:
- The paragraph: "aggregates SHALL count dismissed members separately and expand to them".
- RFC6-17 requires aggregate disclosure. "Separately" can be read as *instead of*, which would take a dismissed Unknown out of an aggregate's per-label Unknown count and its reason tallies. The aggregate would then show fewer Unknowns than the population holds. Under VIS-2 a dismissal must never turn an Unknown into anything but Unknown, at any level.
- M6 shows the builder guards the sentence's presence, not its reading.

Fix: "Dismissed members SHALL remain in every per-label, tier and reason count of the aggregate, and SHALL additionally be counted and expandable as a sibling state."

### 7. REVISE — "No retention question arises" is an unsupported [Inferred] claim, and Scenario 1's re-read obligation depends on it.

Evidence:
- OWNER-DECISION-PACKET.md:132-135: "no retention question arises. [Inferred]".
- SEMANTIC-DELTA.md:146-153 quotes the retention direction: "the claim identity, the epistemic tuple, and the challenge state… Nothing else".
- POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md keeps "exactly three things" per claim. It also says "No record is committed out to any governed plane".
- Scenario 1 requires "reading the first evaluation again after the expiry instant has passed renders the same claim state".

The sibling state, including the dismissal's reason, expiry, author and record identity that the paragraph requires beside the claim, is none of the three retained fields. If the record is later withdrawn or amended, a retained evaluation cannot reproduce it unless the record bytes, or a fourth per-claim field, are retained. That is a retention-posture change, which is an escalation trigger. The "[Inferred]" label is honest, but the inference is not argued, and a scenario depends on it.

Fix: either argue from a quoted clause that the record is reachable by retained digest for the retention window, or state in Q7 and the delta that Scenario 1 needs retained record bytes (or a fourth field) and route it as an owner gate.

### 8. REVISE — The delta's arm framing misstates the M12 funnel.

Criterion: preserve the owner's trade-offs.

Evidence:
- SEMANTIC-DELTA.md:126: "The M12 funnel framed question 5 as widening the challenge-state vocabulary".
- `docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md:97` (row Q5) names three arms. The second is "implement the dismissal **beside** the tuple… needs no amendment but is exactly the 'view filter over a rendered list' shape L2-M8 argues would violate VIS-6(a)".

The drafted arm, a sibling state beside an unchanged tuple, is closest to that second arm. The delta neither names it nor answers L2-M8's objection. The objection is answerable: the governed-plane record, input-bound per RFC2-1, is not a view filter. But packet Q4 defers the write path, so the answer is not yet on the page. OWNER-DECISION-PACKET.md Q1 (:51-56) describes the arms in the package's own terms.

Fix: list all three funnel arms verbatim, place the drafted arm against arm 2, and state why L2-M8's VIS-6(a) objection does not apply, or why it survives if Q4 answers against a governed-plane record.

### 9. REVISE — RFC6-14.r5 marks `unadopted-draft` travel believed-not-applicable while RFC6-17.r2 calls the same state "used".

Criteria: evidence disposition, fail-closed polarity.

Evidence:
- The coverage patch, line 164: "| RFC6-14.r5 | RFC6-14.c5 | RFC6-14 | `challenge-pending`, `unadopted-draft` and `editorial-draft` travel beside the epistemic tuple | believed-not-applicable |".
- The existing repair delta, line 55 (RFC6-17.r2): "Aggregate composition retains the used `unadopted-draft` sibling state | unknown-uncovered".
- IMPACT-LEDGER.md:75-77 sees the tension and routes it to packet Q10.

This is an evidence disposition, not an owner question: a state the matrix itself calls used cannot be believed-not-applicable in the same matrix. Routing it to the owner hands them a reviewer's job.

Fix: split r5 so that `unadopted-draft` travel is its own unknown-uncovered row (fail-closed), recompute totals by script, and drop Q10 or narrow it to what is actually owner-level.

### 10. REVISE (rules 2, 3) — The ledger's headline `PWB-REQ-007` count does not reproduce.

Evidence:
- IMPACT-LEDGER.md:30: "`PWB-REQ-007` | 114 files | 541 occurrences".
- IMPACT-LEDGER.md:25-26 claim method 2 reproduced the counts.
- At 3ee61c7, over 1,537 tracked files, both methods give **113 files / 540 occurrences**. `git grep -c` gives 515, because it counts lines, which may be the ledger's second method conflated. Every other figure in the table matches (C9).

A figure off by one, with a claimed second-method confirmation, means the confirmation did not run on the same population.

Fix: re-derive by script at the declared base, publish the command, the population and the exclusions (undecodable files: 4), and correct the row.

### 11. REVISE — Packet Q11 attributes to the owner an order the owner did not fix.

Criterion: VIS-4, attribution honesty.

Evidence:
- OWNER-DECISION-PACKET.md:97-98: "You fixed `.21 → .30 → .22 → lane B`, then `.20` and `.18`."
- POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:110-120 fixes only ".21 → .30 → .22 → lane B". No decision record read places .20 or .18 (the gate-sitting record :158 does not either).

The tail of the sentence is the package's proposal, presented as the owner's ruling.

Fix: "You fixed `.21 → .30 → .22 → lane B`. This package proposes `.20` then `.18` after it [Inferred]; C7 shows the spec patch composes along .21 → .30 → .22 → .20."

### 12. NOTE — The builder's paragraph rules are presence-only, and its scenario checks cover headings only.

Evidence: M2+M5 survives `--check` after regeneration. PARAGRAPH_RULES in `scripts/build_pwb_dismissal_expiry_amendment.py` are substring presence checks. Scenarios are checked by heading, count and position only.

Today the packet digest is the only guard. Once the phrase is offered and the digest is re-cut, nothing mechanical would stop a wall-clock hiding sentence.

Fix:
- Add scenario-body rules for the re-read and no-tuple-change clauses.
- Add a forbidden-phrase rule (clock, hide, collapse, expire-on-read) with a selftest fixture for each.

### 13. NOTE — The expiry boundary is unspecified.

The paragraph does not say whether a record whose expiry instant equals the evaluation's as-of instant is in effect.

Fix: "in effect while as-of < expiry", plus one boundary scenario line.

### 14. NOTE — The paragraph permits dismissing a `challenge-suspended` (RFC2-24 #9) claim without argument.

It excludes only `contradicted-pending-adjudication` (#8). This is moot while `CHALLENGE_STATES = ['unchallenged']`, but interaction with RFC2-13 `resolved-dismissed` is unreasoned.

Fix: state the #9 disposition or list it as an open question.

### 15. NOTE — The input binding is scoped to records the evaluation "reads".

The paragraph says a record is "bound as an identified input of every evaluation that reads it". RFC2-1 item 9 makes recorded dismissals evaluation inputs through snapshot closure. As written, an evaluation could avoid binding a record by not reading it.

Fix: "every dismissal record present in the governed plane at the evaluation's snapshot is an identified input".

### 16. NOTE — The retention quote's ellipsis spans record-level fields.

SEMANTIC-DELTA.md:146-153 ellipses from the per-claim triple to "Nothing else", which in the source follows several record-level fields. The meaning is preserved, but a reader cannot see the span.

Fix: mark the elision, e.g. "[record-level fields omitted]".

### 17. NOTE — The continuation-form sweep omits range forms.

`PWB-REQ-001..022` appears in 4 lines across 3 files: two pursuit JSONs and `docs/reviews/R-PWB-LIVE-EXACT-HEAD-TRUTH-RAW.md:72`. None is substantive for this delta, but the form set in IMPACT-LEDGER.md:37-43 should name ranges (per the AGENTS.md continuation-form lesson).

### 18. NOTE — Composition is declared and checked pairwise only.

DECLARED_COMPOSITION holds 15 pairs, each checked against the baseline. The reviewer's sequential check (C7) composes along .21 → .30 → .22 → .20. Lane B's declared collision forces regeneration with `--write` anyway.

Fix: say in the packet that whichever of this package and lane B lands second must be regenerated first, and consider a sequential-apply check in the builder.

## Confirmed (no finding)

- Classification Normative is correct: the delta adds SHALL text to an adopted requirement. [Observed]
- No tuple value changes, and the challenge-state vocabulary is untouched. `resolved-dismissed` (RFC2-13) is kept distinct from the sibling state. [Observed]
- VIS-2 in the per-claim path: an Unknown claim stays Unknown with its reason. Only Unknown claims may be dismissed, and never `contradicted-pending-adjudication`. The residual VIS-2 risks are the aggregate (finding 6) and the rendering (finding 5). [Observed]
- VIS-4: the phrase is marked not offered, no act is claimed, and no candidate bytes are installed. [Observed]
- Tooling registration matches the AGENTS.md candidate-packet pattern:
  - `_act_subjects()` pair, `ACT_DIGEST_COPY_FILES` row, and an existence-gated activation are present.
  - There is no `PWB_SUCCESSOR_CHAIN` link and CG-26 is untouched.
  - The selftest adds the absent-act fixture. [Observed]
- All 11 manifest subjects exist and hash as listed, and the digest copies are exact. [Observed]
- Q1-Q8 and Q12 are genuine owner gates. Q10 is not (finding 9), and Q11 misstates the owner's record (finding 11). [Inferred]

## Rule 1-10 summary

- Rule 2/3 violation: finding 10.
- Rule 8 violations: findings 1 and 5.
- Rule 9 is adequate except the range-form note (finding 17).
- Rule 6: the builder's 67 mutants are real, but the scenario-body gap is shown (finding 12).
- Rule 10: nothing in the package claims a prior review (SEMANTIC-DELTA.md:242-246), and this review binds 9b18409 only. Any edit retires it.
- Rule 1: the reviewer used Python `str.count` and `git grep -F -o`, not ugrep classes.

## Owner-only items versus drafter repairs

- Drafter repairs, needing no owner: findings 2-6 and 8-18.
- Needs an owner answer before r1 can be marked covered: finding 1 (packet Q4).
- May need an owner act, as an escalation trigger: finding 7 (retention posture).

Verdict: REVISE
