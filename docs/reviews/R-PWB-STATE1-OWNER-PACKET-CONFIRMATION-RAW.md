# Raw independent owner-packet confirmation — PWB state-(1) amendment

> **FINAL OWNER-PACKET REVIEW VERDICT: REVISE. DO NOT PRESENT THIS PACKET TO
> THE OWNER AT THE REVIEWED PACKET HEAD.** The three signed-subject review
> classes returned `CONFIRM`, but this later packet/check-path review found one
> BLOCKER and two MAJOR defects.

## Review identity

- [Observed] Exact packet-head commit:
  `c772869a20d86a20c14dacb797ea345594f8c917`.
- [Observed] Exact frozen signed-subject commit:
  `8847feef1442bf55fd5276a73248d3c58409e4db`.
- [Observed] Exact eleven-artifact manifest:
  `.syzygy/governance/contracts/candidates/pwb-state1-amendment/PWB-AMENDMENT-MANIFEST.txt`.
- [Observed] Manifest SHA-256:
  `14a84abadf0ba96d968e99bd5b60302895e8a44e6e005b4d2fc76345e7863b1e`.
- [Observed] Generated candidate-report SHA-256:
  `ae194fbc85bd6e799aeab1b25cf552acf5ad54316f135e7b665a4b990c24499d`.
- [Observed] Generated owner-packet SHA-256:
  `3f4411644cb438c599b004721152b0afbdb01ca39da358c28f5942d166f53223`.
- [Observed] Desired verdict supplied: no.
- [Observed] No signed subject was edited during this review. This raw review is
  outside the eleven-row manifest.

## Findings

### Finding 1 — BLOCKER — the offered post-act path fails CG-7e

[Observed] CG-7h correctly keeps the unsigned candidate inert and accepts a
successor only when matching aggregate and dedicated act records bind the exact
eleven-row manifest. However, `ACT_DIGEST_COPY_FILES` does not declare the PWB
successor label for the aggregate acceptance record and does not register the
dedicated `PWB-STATE1-AMENDMENT-ACT.md` record at all.

[Observed] An in-memory simulation added the exact offered phrase and manifest
digest to both required records, without editing repository files. CG-7e then
reported `FAIL`, 2 findings:

1. the aggregate acceptance record carried the recognized PWB act argument but
   did not declare that copy; and
2. the dedicated PWB act record carried the recognized argument but was absent
   from both act-copy registries.

The CG-7h `valid-successor` self-test exercises CG-7h alone and therefore does
not detect this cross-check failure. Consequently, recording the owner act in
the packet's two named homes is not sufficient to make the full governance
battery pass. Packet lines 57–59 describe an incomplete transition path.

### Finding 2 — MAJOR — final-review confirmation is substring-based

[Observed] `final_review_rows()` accepts each raw review when the target commit
and manifest digest occur anywhere in the file and any bold `CONFIRM` marker
occurs anywhere. It does not establish that those identifiers are the review's
declared subject or that `CONFIRM` is its effective final verdict. A synthetic
body with the target identifiers and a historical `CONFIRM` example, but an
exact final verdict of `REVISE`, satisfies the current predicates. No
packet-finalization self-test mutation-proves exact review subject/verdict
binding.

The three current reviews were manually checked and do carry exact `CONFIRM`
for the right frozen bytes, but the generator cannot justify that generated
claim by its own check path.

### Finding 3 — MAJOR — finalized manifest verification ignores extra content

[Observed] `verify()` extracts matching digest rows but does not reject an
additional non-comment, non-row line. Inserting `THIS IS NOT A DIGEST ROW` into
an otherwise exact rendered manifest returned an empty finding list. Ordinary
`--check` catches this through whole-render equality, but `finalized_outputs()`
uses `verify()` without requiring equality to `render()`. Standalone
`--check-finalized` can therefore accept a committed manifest with uncontrolled
non-row content. No malformed-line finalization self-test covers this path.

Severity totals:

- BLOCKER: 1
- MAJOR: 2
- MINOR: 0

## Exact regeneration and digest confirmation

- [Observed] A clean detached clone at packet head
  `c772869a20d86a20c14dacb797ea345594f8c917` reported:
  `PWB amendment manifest matches regeneration — 11 artifacts` and
  `PWB candidate report and owner packet match regeneration — commit
  8847feef1442…`.
- [Observed] The manifest self-test passed its closed 11-row population,
  determinism, subject-byte mutation and subject-path mutation predicates.
- [Observed] An independent row sweep parsed 11 unique, codepoint-sorted paths.
  All 11 stated digests matched both the packet-head worktree bytes and the
  corresponding blobs at frozen subject commit
  `8847feef1442bf55fd5276a73248d3c58409e4db`; residual mismatches were zero.
  The manifest file itself had the same exact SHA-256 at the frozen subject,
  packet head and reviewed worktree.
- [Observed] The packet's three final-review rows match the packet-head blobs:

| Raw review | Exact verdict | sha256 |
|---|---|---|
| `docs/reviews/R-PWB-STATE1-FINAL-SECURITY-RAW.md` | `CONFIRM` | `bb97a69c2dccb9f11b11867b3961211da36da539c1ebf3acde318a4680963748` |
| `docs/reviews/R-PWB-STATE1-FINAL-ORACLES-RAW.md` | `CONFIRM` | `6d247c65420f2a3ea686a1a7cd0bbea09510e88fc21cdf053e201474d694c6aa` |
| `docs/reviews/R-PWB-STATE1-FINAL-TRANSACTION-RAW.md` | `CONFIRM` | `f503efbad51d26c15dace2682da669f3e0ebb6f93953d87115c72759a4fadcfe` |

- [Observed] Each final review binds the same frozen subject commit and exact
  manifest digest. Each carries exact `CONFIRM`; no desired verdict was
  supplied to those review classes.

## Owner ceremony and candidate-only state

- [Observed] The packet contains exactly one exact owner-response line:

```text
SIGN OFF PWB STATE-(1) AMENDMENT: 14a84abadf0ba96d968e99bd5b60302895e8a44e6e005b4d2fc76345e7863b1e
```

- [Observed] No dedicated
  `.syzygy/governance/decisions/PWB-STATE1-AMENDMENT-ACT.md` exists. The
  aggregate acceptance record contains no performed digest for this successor
  phrase. CG-7d reports one candidate quotation, zero findings and zero
  performed digests for `SIGN OFF PWB STATE-(1) AMENDMENT`.
- [Observed] `scripts/check_governance.py` activates the eleven-row successor
  only when both the aggregate act record and the dedicated successor act
  record carry the latest exact manifest digest and all eleven current rows
  match the closed path population. Its self-tests reject an unsigned
  successor, a one-record-only act, conflicting act digests, 10-row, 12-row,
  duplicate, reordered and escaping manifests, and post-successor subject
  drift; the exact valid successor passes at 89 predicates.
- [Observed] That CG-7h success is not sufficient for full-governance success:
  the exact two-record simulation then fails CG-7e as Finding 1 describes.
- [Inferred] The packet and report are therefore candidate-only and perform no
  owner act. The quoted phrase is an offer, not evidence that the owner has
  performed it.

## Supersession, state-(1) risk and authority boundary

- [Observed] The supersession description is exact. The 2026-08-31 PWB sign-off
  originally bound eleven artifacts. The 2026-09-01 general trusted-bootstrap
  transaction superseded five coverage-artifact digests only, leaving six
  original PWB digests current. This eleven-row amendment would supersede that
  current six-plus-five set together, while preserving both earlier acts,
  manifests, digests and bytes as immutable historical evidence.
- [Observed] The packet exposes the selected state-(1) risk: state-(1) consent,
  policy, registry and judgment records are owner-trusted, uncorrelated and
  same-tree forgeable from Syzygy's perspective. Exact digests detect drift but
  establish neither authorship nor owner attendance. Only state (2) is
  independently verified, and acts remain warrants rather than effect-success
  evidence.
- [Observed] The packet states that sign-off creates or approves no observation
  consent, concrete secret policy, adapter-registry entry or walkthrough
  judgment; authorizes no repository-body read or PWB implementation; and
  grants no write, egress, execution, deployment, release, recovery, mission,
  another-repository, autonomous-behavior or multi-user authority. Separate
  effect-specific owner acts and separate implementation authorization remain
  mandatory.

## Validation evidence at packet head

- [Observed] In the clean detached clone, the ordinary governance run reported
  exactly `32 OK, 19 WARN, 1 FAIL (52 checks)`. The only failing check was
  CG-7h: 76 predicates examined and exactly five findings, one for each current
  PWB coverage artifact differing from its immutable 2026-09-01 historical
  manifest row while no successor act exists. No other governance check failed.
- [Observed] `python3 scripts/check_governance.py --selftest` reported `178
  fixtures, 0 failing`. Finding 1 demonstrates that this fixture set does not
  cover the cross-check interaction between successor recording and CG-7e.
- [Observed] The performed general trusted-bootstrap transaction remained
  frozen and valid over 30 contract paths, 5 historical PWB paths and 5
  owner-act rows; all 10 transaction mutations passed.
- [Observed] Strict OpenSpec validation reported
  `Change 'polaris-project-wide-butlers-model' is valid`.

## Exact verdict and owner gate

**EXACT VERDICT: REVISE**

**OWNER PACKET MAY BE PRESENTED TO THE OWNER: NO, not at packet-head commit
`c772869a20d86a20c14dacb797ea345594f8c917`.** Repair the CG-7e successor-act
registrations and add a cross-check self-test; make final-review binding exact;
reject uncontrolled manifest lines on the finalized path; regenerate the
packet and obtain a fresh owner-packet confirmation. The frozen signed subject
`8847feef1442bf55fd5276a73248d3c58409e4db` and manifest SHA-256
`14a84abadf0ba96d968e99bd5b60302895e8a44e6e005b4d2fc76345e7863b1e` may remain
unchanged if those repairs do not alter any of the eleven signed subjects.
This review performs no owner act, makes no candidate effective and grants no
downstream authority.
