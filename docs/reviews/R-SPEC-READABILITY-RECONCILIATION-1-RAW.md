# Independent exact-head review: spec-readability reconciliation (syzygy-73e.5.6)
Reviewed commit: 4b289382601b168cfe8c1ce878a37e96d1ac6af4
Manifest SHA-256: 4250cdc714119fd299991a7a7c753dfe0702605bd4f316c2f07f46c4ed3652cb
Verdict: CONFIRM WITH EXCEPTIONS

Method: detached worktree at the reviewed commit, no edit to the repository. The census.json hash above was computed with sha256sum at that commit. Mutations were run in the throwaway worktree and reverted.

## Parity result

**Denominators [Observed, independent method].** I counted with a separate script: heading prefixes by line, with no reuse of the checker's code. For Polaris I composed by requirement name and confirmed the unmatched count is 0.

| Family | Requirements | Scenarios | Identities |
|---|---|---|---|
| CAP1-REQ | 42 | 47 | 42 distinct, matches the stated runs |
| POC-REQ | 24 | 24 | 24 distinct |
| PWB-REQ | 17 | 44 | 17 distinct, 001-007, 010-016, 020-022 |
| Polaris base | 29 | 154 | |
| Polaris overlay | 7 MODIFIED (54 scenarios) + 2 ADDED (7) | | ADDED are REQ-polaris-generation-030 and -031 |
| Polaris effective | 29 + 2 = 31 | 154 - 33 + 61 = 182 | |

- A sweep for any heading-like line (any `#`-level "scenario" or "requirement", case-insensitive) agrees with the counts, so there is no remainder.
- The tracked-file count across the five change directories is 59. Adding the four pages gives 63, matching R4's file denominator.
- My own pattern over those 63 files finds 1,871 full-form identifier mentions. The checker reports 1,917 including continuation forms, which is plausible and unverified beyond that.

**Acts.** For the five successors I recomputed the manifest sha256 and every manifest row against disk.
- All four digest acts: the manifest digest appears exactly once in the act record and exactly once in `ACCEPTANCE-ACT-RECORD.md`. Row counts are 7, 6, 23 and 8, with 0 bad rows.
- PWB: 11 rows hash to the bytes on disk and to the blobs at the annotated tag `pwb-readability-successor-v1.0` (tag type is `tag`; `bd47409` is an ancestor of `4b28938`).
- PWB: the sign-off record names package, version 1.0, tag and the owner selection, and ties the binding to the tag. Consistent with `OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`.
- 7 + 6 + 23 + 8 + 11 = 55, matching R2's denominator.

**Checker [Observed].** `--check`: R1-R5 OK; R6 and R7 print WARN with findings.
- R6: two pins at `sha256:42d073cd...`, current PWB `spec.md` `sha256:0d50f8f4...`.
- R7: the understanding amendment lacks CC-REV-8.

`--selftest`: 23 of 23 mutants killed by their expected predicate. The witnesses file records the commit `5a0df90`, whose tree equals `acba8a4`'s (311f9db6...), reachable via origin `reconcile/73e.5.6-readability-successors`. The branch head `cdeb17c` is tree-identical to `4b28938`, so the bead's "clean-clone battery at cdeb17c" is valid for this tree.

**My own rule-6 mutants (in the scratch worktree).**

| Mutation | Result |
|---|---|
| One byte appended to the POC `design.md` | R2 FAIL only |
| `Tag:` line deleted from the PWB sign-off | R1 FAIL only |
| Understanding act filename renamed in `PROJECT-STATUS.md` | R5 FAIL |
| Base-change row deleted from `openspec/README.md` | R5 FAIL, 2 findings |

Each failed the intended predicate, and the others stayed OK.

**Stale items [Observed].**
- The two registry/policy pins and the missing CC-REV-8 are reported as WARN/Unknown, never green, with beads `syzygy-jloi` and `syzygy-c51h`.
- The remaining items in §5 of the record (three candidate banners, POC "21", MG-01..17 mapping) match the bytes I read.
- `AGENTS.md` and `PROJECT-STATUS.md` carry no residual "three changes" or "only coverage" wording (grep).

**Page edits [Observed].**
- `git diff --check` is clean.
- The `openspec/README.md` banner is untouched; the diff starts at the section heading.
- No file under `.syzygy/`, `openspec/changes/` or `docs/reviews/` was touched by the PR.
- `PROJECT-STATUS.md` and `README.md` edits match the act records. Capability 1: `proposal.md` and `design.md` superseded, `spec.md` unchanged. The three `spec.md` files still carrying a candidate banner are exactly the POC, the Polaris base and the understanding amendment; the CAP1 and PWB `spec.md` files carry none.
- Every proposal's head has no candidate or "binds nothing" text.
- The CG-26 triple is consistent: block, workflow steps and the count sentence all say 59 (57 + 2).
- `check_governance.py`: 0 FAIL. Docs partition: `unmatched=0 overlaps=0`.

## Findings

**Finding 1: the `openspec/README.md` edit exceeds the cited direction and landed before its review** (note, owner acknowledgement needed)

The 2026-09-28 rollout direction (`OWNER-DIRECTION-2026-09-28-TREE-STYLE-ROLLOUT.md`) says:
- "Presentation and route pages (READMEs, guides, plans, candidate views): restyles that preserve meaning land once a fresh-reader review returns CONFIRM, or CONFIRM WITH EXCEPTIONS with notes only".
- It excludes "Changes of meaning: a rule, scope, qualifier or permission that changes goes to the owner as its own packet".
- It excludes "Errors found while restyling: a wrong citation or a stale count is listed in the change's packet or commit. It is not fixed silently."

The evidence README (§4) justifies the edit as "for currency under the 2026-09-28 tree-style direction's route-page arm". But the edit is a currency repair, not a meaning-preserving restyle: two new rows, "three" to "five", "amended twice" to "a chain", and a rewritten banner paragraph.

Mitigations:
- The stale items are listed in the commit and in evidence §4, so the "not silently" clause is met.
- The page is navigation-only and bound by no act: its digest appears in no act manifest, only in the review baseline `docs/evidence/polaris-generator-approval-offer-2026-09-12.json`.
- `polaris_generator_approval.py --check --offer ...` fails identically before and after the PR ("owner argument does not match exact offer bytes").
- The page was owner-approved on 2026-09-08 under P-57. Its banner is untouched.

The arm requires the review to come first. The PR merged before this review, so the arm was not satisfied in order. If this review's verdict stands as that fresh-reader review, the notes-only condition is met going forward.

Recommendation: the owner should acknowledge the edit as a route-page currency repair. Alternatively, evidence §4 could stop calling it a use of the restyle arm.

**Finding 2: a green summary line sits beside unresolved Unknowns** (note)

`--check` ends "7 of 7 predicates without FAIL; PASS" while R6 and R7 print 3 findings. Each is labelled WARN and "Unknown", and the record states this design (§7), so nothing is false. A hurried reader of the last line could still miss them. Consider printing "PASS with 2 report-only WARN" and the open count. No parity effect.

**Finding 3: wording drift in two places** (note)

- The evidence README says the Polaris approval check "was already failing off-battery on baseline drift". The actual failure message is "owner argument does not match exact offer bytes". That is the same family of cause, but the message differs from the paraphrase.
- The `openspec/README.md` banner says the page "restates no requirement, no digest and no verdict". The new understanding row states "modifies seven generator requirements and adds two", a restated count. It is harmless and checkable, but it brushes the stated rule.

Neither changes any parity conclusion. No blocking findings. Semantic, act and denominator parity are confirmed at this head.
