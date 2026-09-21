> **Candidate — binds nothing.** The impact record for a drafted CC-REV-2
> semantic delta. It performs no act, adopts nothing and authorizes no
> implementation. It would take effect only through an owner act over this
> package's behavior manifest, named in
> `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`.

# Impact ledger — PWB exact-source render mode

What this change reaches, how that was found, and what each reached artifact
does about it. Companion to `SEMANTIC-DELTA.md`; the exact bytes are the
patches under `proposed/`, printed by
`python3 scripts/build_pwb_exact_source_render_mode_amendment.py --diff`.

## Discovery method

Run in this session, on this worktree, over the 1,334 files tracked here
(verification rule 2 wants the exact sweep run this session and confirmed by
a second method; rule 9 wants a denominator).

1. **Method 1 — Python `re` over every tracked file.** Two patterns: the
   literal `PWB-REQ-011`, and the continuation forms this corpus writes
   identifiers in (`PWB-REQ-010, 011`, `PWB-REQ-011/015`,
   `PWB-REQ-010..012`), because a full-identifier sweep alone has produced a
   false absence in this repository before. Result: 82 full-form citers and
   4 files that cite it only in continuation form.
2. **Method 2 — a recursive fixed-string sweep** (`grep -rF -l`, which is
   ugrep here; `-F` because rule 1 makes bracket classes unsafe) over the
   same tree, excluding `.git`, `node_modules` and `dist`. Result: the same
   82 files plus one file this package itself creates
   (`proposed/CAPABILITY-COVERAGE.md.patch`) and nothing else.
3. **Remainders, enumerated.** 4 tracked files are not decodable as UTF-8
   and are excluded from method 1; method 2 reads them as binary and
   reported no match in them either. No claim here is a "zero" claim over
   the whole tree: the population below is 86 files, and the two methods
   agree on it.

Neighbouring requirements were swept the same way, because a route that
reaches more sources plausibly reaches them: PWB-REQ-014 (anchor identity),
PWB-REQ-020 (parity), PWB-REQ-015 (verbatim-intent band), PWB-REQ-003,
PWB-REQ-005 and PWB-REQ-006. What each of them does is in
`SEMANTIC-DELTA.md` §"What explicitly does NOT change"; none is amended.

A citation is not a reliance (rule 5). The classes below say which citers
are dependencies of the amended text and which merely name the identifier.

## Classes

| Class | Count | Disposition |
|---|---:|---|
| A. Bound behavior artifacts that cite PWB-REQ-011 | 8 | 4 of them move in this change; the rest, and the 3 bound artifacts that do not cite it, are byte-identical manifest rows |
| B. Implementation and test modules under `apps/` | 18 | Unchanged here. They are the work an implementation bead would do after the act; listed again below |
| C. Retained evidence, measurement and pursuit records | 19 | Never edited. They record what was measured when it was measured |
| D. Retained reviews | 20 | Never edited (CC-REV-6 stores raw reviewer output unchanged) |
| E. Design funnels and implementation plans | 6 | Unchanged. The M14 funnel is this change's evidence and stays as measured; the implementation plan gains rows only when a bead opens |
| F. Other governance pages under `.syzygy/` | 9 | Unchanged. One of them, the scoped-attributes candidate, collides with this package on one generated line; see §"Merge and effect boundary" |
| G. Advisory, generated or another change's | 6 | Unchanged |

Total: 86.

## The four artifacts that move

| Artifact | What moves | Why it must move in the same logical change |
|---|---|---|
| `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` | PWB-REQ-011 gains one invariant paragraph, a rewritten Case/Observable/Oracle/Oracle-independence/Falsifier list, a Mutation-proof bullet and three scenarios | It is the obligation |
| `openspec/changes/polaris-project-wide-butlers-model/design.md` | §8 gains two paragraphs | §8 is the standing argument that the route needs no wider content class, and it currently argues only the baseline case. Left alone it would contradict the amended requirement |
| `openspec/changes/polaris-project-wide-butlers-model/CAPABILITY-COVERAGE.md` | Row 10's obligation text | Row 10 declares the obligation PWB-REQ-011 covers, in the population's own words. Left alone it would under-declare what the requirement now obliges — and CC-SPEC-11 makes the table a reviewed artifact, not a summary |
| `openspec/changes/polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES.md` | The generated source-digest line only | It is generated from the specification and carries its sha256. Any specification edit moves it. The patch is a regeneration output, re-derived and never hand-edited |

The population count in `CAPABILITY-COVERAGE.md` stays 31 and its totals stay
25 covered, 6 lawfully out of scope, 0 Unknown: the amendment restates one
obligation, it does not add one to the table.

Contract coverage does not move. The contract-coverage builder
(`scripts/build_polaris_project_wide_contract_coverage.py --check`)
was run over the proposed bytes in a scratch tree and reports the same 324
represented clauses; the coverage rows that name PWB-REQ-011 check
row-to-warrants, and no requirement's warrants change [Observed, run this
session].

## Implementation sites, for the bead that follows adoption

None of these is edited by this package. They are listed so the reviewer can
judge whether the amendment is implementable within the acts in force, and so
the implementing bead starts from a real list rather than a search.

| Site | What an implementation would do |
|---|---|
| `apps/three-surface-poc/src/verbatim-route.ts` | Choose a mode from the source's class instead of refusing every non-baseline class; keep the excluded-outcome refusal ahead of every mode; run the existing detectors on the complete transient body in both modes |
| `apps/three-surface-poc/src/capability-detail.ts` | Keep the requirement-section selector for the baseline mode only; its "no requirement heading" refusal is exactly why a second mode exists |
| `apps/three-surface-poc/src/polaris-source.ts` | Continue to carry the exact-source identity in the route `href`, which is its single carrier |
| `apps/three-surface-poc/src/polaris-source-route.test.ts`, `verbatim-route.test.ts` | Extend to the served/refused partition over the complete source population, with both denominators reported |
| `apps/three-surface-poc/src/polaris-reachability.test.ts` | Extend the reachability sweep to the anchor parameter |
| `apps/three-surface-poc/src/polaris-copy.ts` | The one legend sentence P-81 Q3 rules on, which is not part of this amendment |

The parity sweep's extension over the anchor parameter is an obligation of
the amended PWB-REQ-011, not an edit to PWB-REQ-020; see the delta.

## Merge and effect boundary

**Nothing in this package changes any tracked byte under `openspec/`.** CG-7h
binds the current `openspec/` bytes to the latest performed act, so the
proposed bytes live as diffs and the manifest hashes the post-apply bytes.
The tree and the manifest disagree on four rows until `--apply --at-adoption`
runs inside the change that records the act.

**One collision with the parallel lane, by construction.** The
scoped-attributes candidate
(`.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/`)
amends the same specification. Its `GOVERNING-DEPENDENCIES.md` patch and this
one both rewrite the single line that carries the specification's sha256, so
they cannot both apply. That is a regeneration, not a merge conflict to
resolve by hand: whichever amendment lands second re-runs
`python3 scripts/build_polaris_project_wide_spec_dependencies.py` and
regenerates its manifest before its phrase is offered.

The sentence above is scoped to that candidate landing **whole**. Round-1
review finding F3 showed that a *partial* landing — its `spec.md.patch`
alone — collides with nothing, in any tool or order, and leaves the
generated file naming a digest for a `spec.md` that is not on disk. That
tree is now detected rather than prevented; see `SEMANTIC-DELTA.md`
§"Migration / supersession plan" for the caveat and §Review for the
disposition.

`scripts/build_pwb_exact_source_render_mode_amendment.py --check` asserts this
rather than assuming it. It applies the scoped-attributes diffs to a scratch
copy of the eleven subjects, then requires that the three semantic patches
here still apply and that the generated one does **not**. `--selftest` proves
both halves fail closed: a wide-context design diff (which would collide with
the scoped-attributes design addition at the same insertion point) is
rejected, and a lane-B tree without the dependency regeneration — where no
collision exists — is rejected too. A third pair covers F3: the check
builds the partial tree, confirms all four patches apply to it without
objection, and asserts the dependency digest is detectably inconsistent with
the `spec.md` beside it; `--selftest` proves the inverse, that a
self-consistent partial tree is reported.

**Two digest pins go stale on any specification amendment.** The approved
secret-classification policy candidate and the adapter-registry observer
candidate each carry a `governingBehaviorContract.version` naming the current
specification's sha256 [Observed, both files read this session]. This package
does not touch either: both are act-bound artifacts with their own amendment
ceremony, and the owner has already sequenced a registry-entry amendment act.
Named here so the staleness is announced before it happens rather than
discovered afterwards. [Inferred — that the refresh belongs to that act and
not to this one.]

## Every citing file

Enumerated so the reviewer can contradict the classification file by file.

### A. Bound behavior artifacts (8)

- `openspec/changes/polaris-project-wide-butlers-model/CAPABILITY-COVERAGE.md` — **moves in this change**
- `openspec/changes/polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES.md` — **moves in this change**
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0001-0003.md` — byte-identical manifest row
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0004-0006.md` — byte-identical manifest row
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0007-0009.md` — byte-identical manifest row
- `openspec/changes/polaris-project-wide-butlers-model/design.md` — **moves in this change**
- `openspec/changes/polaris-project-wide-butlers-model/proposal.md` — byte-identical manifest row
- `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md` — **moves in this change**

### B. Implementation and test modules (18)

- `apps/three-surface-poc/src/capability-detail.ts`
- `apps/three-surface-poc/src/main.ts`
- `apps/three-surface-poc/src/polaris-accessibility-main.ts`
- `apps/three-surface-poc/src/polaris-accessibility.browser.test.ts`
- `apps/three-surface-poc/src/polaris-accessibility.ts`
- `apps/three-surface-poc/src/polaris-capability-detail.test.ts`
- `apps/three-surface-poc/src/polaris-copy.ts`
- `apps/three-surface-poc/src/polaris-first-reading.test.ts`
- `apps/three-surface-poc/src/polaris-project-shape.test.ts`
- `apps/three-surface-poc/src/polaris-proposed-work.test.ts`
- `apps/three-surface-poc/src/polaris-reachability.test.ts`
- `apps/three-surface-poc/src/polaris-source-route.test.ts`
- `apps/three-surface-poc/src/polaris-source.ts`
- `apps/three-surface-poc/src/polaris.ts`
- `apps/three-surface-poc/src/routes.ts`
- `apps/three-surface-poc/src/test-project-shape-fixture.ts`
- `apps/three-surface-poc/src/verbatim-route.test.ts`
- `apps/three-surface-poc/src/verbatim-route.ts`

### C. Retained evidence, measurement and pursuit records (19)

- `docs/evidence/polaris-generator-host-overlap-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v2-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v3-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v4-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v5-2026-09-12.json`
- `docs/evidence/polaris-m11-operability-funnel-2026-09-15.json`
- `docs/evidence/polaris-m13-navigation-scale-funnel-2026-09-15.json`
- `docs/evidence/polaris-m14-provenance-depth-funnel-2026-09-17.json`
- `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json`
- `docs/evidence/polaris-manifesto-example-mutation-2026-09-09.json`
- `docs/evidence/polaris-pipeline-synthetic-verification-2026-09-13.json`
- `docs/evidence/pwb-c5-readiness-verbatim-mutation-run-2026-09-05.json`
- `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`
- `docs/evidence/pwb-p3-8-reachability-mutation-run-2026-09-04.json`
- `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-04.json`
- `docs/evidence/pwb-p4-4-accessibility-browser-run-2026-09-04.json`
- `docs/pursuits/2026-09-13-vision-pursuit-data.json`
- `docs/pursuits/2026-09-13-vision-pursuit-harvest.json`

### D. Retained reviews (20)

- `docs/reviews/2026-09-05-pwb-live-exact-head-packet.md`
- `docs/reviews/2026-09-09-polaris-editorial-repair.md` (continuation form only)
- `docs/reviews/R-POLARIS-EDITORIAL-CODE-RAW.md`
- `docs/reviews/R-POLARIS-GUIDE-NAVIGATION-RACE-2026-09-10-RAW.md`
- `docs/reviews/R-POLARIS-M11-OPERABILITY-FUNNEL-2-RAW.md`
- `docs/reviews/R-POLARIS-M11-OPERABILITY-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-3-RAW.md` (continuation form only)
- `docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-5-RAW.md`
- `docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-6-RAW.md`
- `docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-7-RAW.md`
- `docs/reviews/R-POLARIS-PROJECT-WIDE-SPEC-REVIEW-RAW.md`
- `docs/reviews/R-POLARIS-READING-ASSETS-CODE-2026-09-10-RAW.md`
- `docs/reviews/R-PWB-LIVE-EXACT-HEAD-ENGINEERING-RAW.md`
- `docs/reviews/R-PWB-LIVE-EXACT-HEAD-TRUTH-RAW.md`
- `docs/reviews/R-PWB-LIVE-EXACT-HEAD-UX-RAW.md`
- `docs/reviews/R-PWB-RECOVERY-RECONCILIATION-GEN1-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-2-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-3-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-4-RAW.md`

### E. Design funnels and implementation plans (6)

- `docs/PWB-IMPLEMENTATION-PLAN.md`
- `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`
- `docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md`
- `docs/design/POLARIS-M13-NAVIGATION-SCALE-FUNNEL.md`
- `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md`
- `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md`

### F. Other governance pages (9)

- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/OWNER-DECISION-PACKET.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/REVIEW-BRIEF.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/SEMANTIC-DELTA.md`
- `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/IMPACT-LEDGER.md` (continuation form only)
- `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/OWNER-DECISION-PACKET.md`
- `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/SEMANTIC-DELTA.md`
- `.syzygy/governance/decisions/DECISION-HISTORY.md`
- `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`
- `.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`

### G. Advisory, generated or another change's (6)

- `AGENTS.md`
- `openspec/changes/polaris-manifesto-generation/design.md` (continuation form only)
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0001-0003.md`
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0004-0006.md`
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0007-0009.md`
- `openspec/changes/polaris-project-wide-butlers-model/tasks.md`

