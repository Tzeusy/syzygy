# Review brief — continue PWB implementation authorization for M2 slice 5

> **Candidate — binds nothing.** This commissions one independent
> fresh-context review. It carries no verdict and performs no act. The
> reviewer must not receive the drafting conversation or a desired verdict.

## The head the raw must carry

Round 1 is retained as
`docs/reviews/R-PWB-M2-SLICE5-CONTINUATION-PACKET-RAW.md` (`REVISE`, over
`268f1773`). This brief commissions round 2, whose raw is retained
verbatim under `docs/reviews/` as
R-PWB-M2-SLICE5-CONTINUATION-PACKET-2-RAW.md, a file that does not exist
yet (a further run is a further `-RAW.md` under a distinct name, never an
overwrite). Its first
four non-blank lines are, in this order and with no other line between
them:

```text
# Review — PWB M2 slice 5 implementation-continuation packet
Reviewed commit: <the full 40-hex commit the reviewer checked out>
Artifact SHA-256: <SHA-256 of OWNER-DECISION-PACKET.md at that commit>
Verdict: <CONFIRM | CONFIRM WITH EXCEPTIONS | REVISE>
```

**The digest is the SHA-256 of the exact bytes of this package's
`OWNER-DECISION-PACKET.md`** at the reviewed commit, which is the text the
owner answers. It is **not** a manifest digest (the package has none), not
an act argument and not a digest of this brief or the ledger. The reviewer
computes it by script at the checked-out commit (`sha256sum` of that one
file) and does not copy it from anywhere. The review covers all four
package files at that commit (the three below and
`ROUND-1-DISPOSITIONS.md`); an edit to any of them after it retires the
review (rule 10). The commit that retains the raw also adds its campaign row
to `docs/README.md`, so `scripts/check_docs_review_campaign_partition.py`
keeps passing.

## Exact review inputs

Give the fresh reviewer only:

- this package in full, at one commit: `OWNER-DECISION-PACKET.md`,
  `IMPACT-LEDGER.md`, this brief and `ROUND-1-DISPOSITIONS.md`;
- the round-1 raw `docs/reviews/R-PWB-M2-SLICE5-CONTINUATION-PACKET-RAW.md`;
- the 2026-10-20 direction drafted in PR #489, read at its head
  `8c334f67` with
  `git show 8c334f67:.syzygy/governance/decisions/OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-20.md`
  (fetch branch `agent/syzygy-sin5` first);
- the authorization it continues and its precedents, in
  `.syzygy/governance/decisions/`:
  `PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`,
  `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`,
  `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md` and
  `POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DECISION-PACKET.md`;
- the gate records: `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
  (row P-69), `POLARIS-LANE-B-DECLINED-AND-TARGET-REVISED-DIRECTION.md`,
  the three registry act records
  (`PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`,
  `PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md`,
  `PWB-OBSERVER-REGISTRY-MACHINE-CEILING-ACT.md`), the two read-gate
  directions (`OWNER-INSTRUCTIONS-2026-09-29-30-READABILITY-AND-REGISTRY.md`,
  `OWNER-INSTRUCTIONS-2026-10-02-PWB-BEHAVIOR-CONTRACT-REPIN.md`) and
  `PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0.md`;
- the registry entry
  `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`;
- the signed missing-currency package
  `.syzygy/governance/contracts/candidates/pwb-missing-currency-disclosure-scenario/`;
- PWB-REQ-007 with its scenarios, PWB-REQ-010's opening-aggregate
  scenario and PWB-REQ-015's "Relation claim" and "Relation results" in the
  PWB `spec.md`, and
  `openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE-REPAIR-DELTA.md`;
- RFC2-9, RFC2-10, RFC2-24, RFC2-25, RFC6-14, RFC6-17, RFC7-16, RFC7-33,
  CAP1-REQ-062, VIS-2 and VIS-7 at their definition sites (find them with
  `DIRECTIVE-REGISTER.md`);
- `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md` (Q1, Q2, Q7 and
  "Slice 5");
- `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`;
- the consumer files the ledger's table names, and
  `packages/cap1-core/src/staleness.ts`;
- `_act_subjects()` and `ACT_DIGEST_COPY_FILES` in
  `scripts/check_governance.py`;
- `AGENTS.md`;
- the acceptance criteria of bead `syzygy-dov.19`, which the coordinator
  pastes into the reviewer's prompt from `bd show syzygy-dov.19` (round 1
  did not receive them and read them itself), and the criteria below.

## Criteria

1. **Gate readback.** Re-run the ledger's three readback steps at the
   reviewed commit. Confirm or contradict that the currency fields are
   byte-equal across the three registry tags and the tree, that the tree's
   registry bytes are the current act's argument, and that the signed
   scenario block is byte-identical at its sign-off tag and in the tree.
   Confirm the packet says the 2026-09-21 ruling prepared gates but
   performed no continuation.
2. **Quotation fidelity.** Every quoted passage matches its source; nearby
   prose does not stand in for a clause (rule 8).
3. **Instrument.** Decide independently whether a plain owner direction is
   the right instrument. Report any B item that would actually change a
   signed or act-bound byte, an accepted contract, a registry value or
   semantics sentence, consent or policy, since any of those needs an act
   this direction cannot be.
4. **Built behavior against the scenario.** B4 and B5 must neither add to
   nor drop from the signed scenario's obligations. Check in particular:
   - the drafter's precedence compositions (B4's stale and no-bound arms);
   - the tier result and the reading of "retains its tier" against RFC2-25;
   - the treatment of refused, failed and not-evaluated shapes;
   - the absent freshness field and the arm marker that replaces inference
     from it;
   - B5's per-freshness counts, the populations they are taken over, and
     the rule for an aggregate's own freshness;
   - that nothing mints a fifth value, a `null`-as-value or a sentinel.
5. **The five gaps.** Each row is quoted from its file and each clause from
   its definition site; the routing claims no conformance on the
   scenario's arm; the statement that none needs a specification amendment
   to be built is true; no other contract consequence is newly crossed by
   B1–B11 and left unrouted (the packet names RFC2-25.r1, RFC2-9.r1 and
   RFC2-10.r1).
6. **Option O1.** Is reading (i) of `measuredFrom` a lawful reading of the
   entry's sentence, are both readings presented fairly with their costs,
   the design evidence for (ii) and (ii)'s authority cost, and does the
   reply authorize (i) only? Say whether this is in fact an owner question
   or one the lead may decide.
7. **Scope and exclusions.** The question names the one repository and
   content class and retains every exclusion bead criterion 2 lists
   (wider repository or content class, consent, write, egress,
   observed-code execution, deployment, release, recovery, mission,
   autonomy, multi-user). `maxBriefingResponseBytes` and
   `governingBehaviorContract` stay unread.
8. **Wording and default.** One exact reply; silence, "Agreed", an option
   selection, the ruling, the questionnaire answer, merge or CI continue
   nothing; declining leaves current behavior and is described honestly.
9. **Overlap.** The section on PR #489 describes that record accurately at
   `8c334f67`; B11 composes with it (one mechanism, the relation claims'
   own reason rule, the band's count and freshness) and authorizes nothing
   else of either lane; and the two directions cannot widen each other.
10. **Impact sweep.** Re-run the ledger's published predicates at its
    baseline (2,939 tracked files, four decode skips) if practical. Check
    the consumer table's line ranges, the pin finding and the claim-id
    family enumeration.
11. **Precedent fidelity.** The package follows the 2026-09-05 continuation
    and the retention-posture packet: no manifest, digest, recorder,
    acceptance-record row or governance registration, and it says why. The
    planned record quotes B1–B11, the gap table and O1 verbatim and names
    the reviewed commit and raw as provenance.
12. **Governance hygiene.** No bound byte edited; no performed act's
    argument copied; no observed-repository path in a code span; no code
    span broken across a line; candidate banners explicit;
    `python3 scripts/check_governance.py` and
    `python3 scripts/check_quotations.py` report no finding naming these
    files.
13. **Authority boundary.** Nothing here signs, adopts, records, unblocks or
    authorizes; nothing says slice 5 may be built now.
14. **Round-1 dispositions.** For each of R1–R6 and N1–N9, check that the
    disposition in `ROUND-1-DISPOSITIONS.md` matches what the packet,
    ledger and brief now say, and that every figure, commit and population
    in it was re-derived rather than copied from the round-1 raw.

## Required report

Start with the four-line head above. Then provide:

- the instrument decision and its rationale;
- numbered findings mapped to the criteria and verification rules, each
  marked revise or note, with exact file and line;
- the commands actually run, with their denominators;
- any owner-only decision still preventing these bytes from being offered.

Findings are dispositioned in a sibling dispositions record
(ROUND-2-DISPOSITIONS.md for this round), never in
`OWNER-DECISION-PACKET.md`; verdict words are copied exactly, never
softened.
