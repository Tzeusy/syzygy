# Impact ledger — PWB derived read-only machine views

> **Candidate — binds nothing.** Companion to `SEMANTIC-DELTA.md`. It takes
> effect only if the owner performs the PWB behavior amendment act over the
> digest of `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`. Nothing here authorizes an
> implementation.

Baseline: commit `a4a34510a5582edbd38c1df57a064ba3ac0a33f2`. None of the
eleven behavior subjects changes between it and the commit that carries this
draft; the builder recomputes every manifest row from the tree it runs in, so
a moved baseline fails `--check` rather than passing silently.

## Discovery method

Two sweeps over every tracked file at the baseline, run 2026-09-21
(verification rules 2 and 9; enumerated below, nothing sampled).

1. Python `re` over the UTF-8 text of every tracked path: `PWB-REQ-020\b`
   counted per file, plus a second pattern for continuation forms —
   `PWB-REQ-\d{3}(?:\s*[/,]\s*(?:and\s+)?\d{3})*\s*[/,]\s*(?:and\s+)?020\b`
   and a `..` range form.
2. `grep -l -F` for the literal `PWB-REQ-020` over the same tracked listing.

Method 1's full-form pattern and method 2 both return **112 files**. The
continuation pattern adds **9 files** the full form misses; each of the nine
was confirmed by printing its matched text, so none is a regex artefact:

| File | Matched form |
|---|---|
| `.syzygy/governance/decisions/DECISION-HISTORY.md` | `PWB-REQ-007/014/020`, `PWB-REQ-011/020` |
| `.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md` | `PWB-REQ-007, 014, 020` |
| `apps/three-surface-poc/src/polaris.ts` | `PWB-REQ-005/020` |
| `apps/three-surface-poc/src/pwb-mutation-sweep-main.ts` | `PWB-REQ-001/002/003/004/005/010/012/020` |
| `apps/three-surface-poc/src/routes.ts` | `PWB-REQ-014/020` |
| `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-09-named-absent-file-dropped.json` | `PWB-REQ-001/002/003/004/005/010/012/020` |
| `docs/reviews/2026-09-05-pwb-live-exact-head-packet.md` | `PWB-REQ-014/015/020` |
| `docs/reviews/R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-RAW.md` | `PWB-REQ-011, 012, 016, 020` |
| `docs/reviews/R-POLARIS-READING-ASSETS-REPAIR-2026-09-10-RAW.md` | `PWB-REQ-014/020` |

**Citer population: 121 files over a denominator of 1,334 tracked files.**
`.beads/issues.jsonl` is an untracked export and is outside the denominator;
the bead this package serves is `syzygy-dov.22`, read directly.

This ledger's own files, once committed, join the citer population. The table
above is the **baseline** table and is not re-derived here; a reader who
re-runs the sweep at a later commit will get a larger figure, and the
difference is this package.

## What the population needs, and why the answer is "nothing to repair"

The proposed specification patch has **no removed line**: it inserts one block
of prose between PWB-REQ-020's `Group:` line and its SHALL sentence, and
changes no existing sentence, bullet, scenario or warrant. [Observed — the
patch file contains zero lines beginning with `-` other than its `---` header,
and the builder's `--check` compares the changed-subject population against
the declared one.]

It follows that no sentence in the 121 files becomes false. Every statement
about PWB-REQ-020's parity invariant, its oracle, its falsifier or its
denominators stays exactly as true after adoption as before. The impact is
**work created**, not **text invalidated** — which is the opposite of the
sibling scoped-attributes package, whose patch rewords existing clauses.

## Classes

| Class | Files | What adoption does to them |
|---|---|---|
| 1 The amended package itself | 9 | Two are patched subjects; the other seven are manifest rows that equal current bytes and are re-hashed, not edited |
| 2 Other specifications | 1 | Cites PWB-REQ-020 as context; unaffected |
| 3 Decisions and act records | 4 | Historical records of prior PWB acts; never edited |
| 4 Other governed candidates | 8 | Two sibling candidate packages; the scoped-attributes one shares the manifest subject (see "Ordering") |
| 5 Implementation and tooling | 12 | Cite the requirement in comments and test names; none becomes wrong, and none is the site of the new obligation — see below |
| 6 Retained raw reviews and review packets | 48 | Uneditable under CC-REV-6 |
| 7 Evidence and pursuit records | 26 | Dated records of what was true when run; never retrofitted |
| 8 Docs prose | 12 | Plans and funnels; the implementation plan gains a line when the follow-on bead is filed, after adoption, never before |
| 9 Operating procedure | 1 | `AGENTS.md`; no change |

## Implementation sites, for the bead that follows adoption

Adoption authorizes no code. These are the sites the follow-on bead would
touch, named so the owner can see the size of what the act sets up.

| Site | Why | State today |
|---|---|---|
| `apps/three-surface-poc/src/polaris-presentation-route.test.ts` | The derivability oracle the inserted text requires: every served value verified against the machine answer's bytes at the same evaluation, by a checker importing no rendering code | Two cases today — credential refusal with page-anchor citation, and typed failure under the machine ceiling. Neither is that oracle. **This file is not one of the 121**: it cites PWB-REQ-014, not PWB-REQ-020 [Observed] |
| `apps/three-surface-poc/src/routes.ts` | Registers the one existing member; would register the briefing view and, later, the draft view | Member 1 registered `machine-credentialed` under `maxMachineResponseBytes`, in the direct and tailnet-mount forms |
| `packages/three-surface-poc-core/src/project-shape-observation.ts` | Where the registry resource limits are read; a briefing ceiling would arrive here after the registry act | Two ceilings today |
| A new briefing view module | Member 2 does not exist | `/api/poc/briefing` occurs in 25 of 1,440 tracked files at `66da9f2` (byte-literal match over `git ls-files`), none of them an installed registry file or implementation source [Observed]; the first draft's "12 tracked files, all under `docs/design/`, `docs/evidence/`, `docs/pursuits/` and `docs/reviews/`" went stale as sibling packages and raws landed (round 5 finding R5-2) |
| A new draft view module | Category 2's member does not exist | `/polaris/draft` occurs in 15 of 1,440 tracked files at `66da9f2`, same predicate, none of them implementation source [Observed]; the first draft said 4 (R5-2) |

## The ceiling this delta depends on but does not mint

`maxBriefingResponseBytes` occurs in **24** of 1,440 tracked files at
`66da9f2` (byte-literal match over `git ls-files`) [Observed]: owner ruling
and decision records, one design funnel, pursuit data, this package, the
sibling registry-currency candidate (whose proposed patch would mint it, with
its builder script) and retained raw reviews. **No installed registry file
names it**; only that sibling's unperformed patch does. These counts are over
a live population and go stale as files land; re-derive with the stated
predicate rather than reading them. (The first draft said 7 files and "No
registry file names it"; round 5 finding R5-2.) The
inserted specification text therefore does not name it either: it says the
adapter-registry entry's resource envelope must declare the member's ceiling
before the member is served, and leaves the field identity to the registry
act (P-72 question 2, gate bead `syzygy-dov.18`). Adopting this delta before
that act leaves no dangling literal in the specification — only an unserved
route, which is the intended state.

## Ordering against the sibling candidate

`.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/` is
pending against the same eleven subjects.

- **The two specification patches compose, in either order, to identical
  bytes**, and the composed specification's warrants still validate
  [Observed — `build_pwb_machine_view_amendment.py --check` verifies both
  orders on every run; its `--selftest` mutates a context line of the sibling
  patch and confirms the check then fails].
- **The generated dependency declaration does not compose.** Both packages
  rewrite its single `Source:` digest line. Whichever package the owner signs
  second must be regenerated with `--write` against the tree after the first
  lands, and its packet's quoted manifest digest updated before the second
  act.
  Re-derived at `76b4beb` (2026-09-23): **five** candidates under
  `.syzygy/governance/contracts/candidates/` carry a `proposed/spec.md.patch`
  against the PWB `spec.md` — this one, `pwb-scoped-attributes-amendment/`,
  `pwb-exact-source-render-mode-scenario/`, `pwb-opening-band-scenario/` and
  `pwb-missing-currency-disclosure-scenario/` — so "second" reads as "each
  one signed after the first". (An earlier sentence here counted three on
  the same date; the fourth sibling had landed before it was committed,
  §Review round 3 F6.) The builder composes against scoped-attributes only.
  This package's patch was also composed with each of the other three in
  both orders this session, by `git apply` in a scratch tree, each pair to
  one digest [Observed]. Two limits on "regenerate": `--write` repairs the
  generated `Source:` line only and does not make a sibling's
  *specification* patch apply (among the siblings, missing-currency applied
  before scoped-attributes fails; every order with scoped-attributes first
  composes to one digest [Observed]); and the order itself is the owner's,
  fixed in
  `.syzygy/governance/decisions/POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md`
  §6 with lane B last, which this package cites and does not restate. This
  is arithmetic, not disagreement: neither package's prose touches the
  other's sentences.

## Every citing file

Enumerated so the figure above can be checked rather than believed.

### 1 The amended package itself (9)

- `openspec/changes/polaris-project-wide-butlers-model/CAPABILITY-COVERAGE.md`
- `openspec/changes/polaris-project-wide-butlers-model/CONTRACT-COVERAGE-REPAIR-DELTA.md`
- `openspec/changes/polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES.md`
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0004-0006.md`
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-matrix/RFC-0007-0009.md`
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0004-0006.md`
- `openspec/changes/polaris-project-wide-butlers-model/contract-coverage-parts/RFC-0007-0009.md`
- `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`
- `openspec/changes/polaris-project-wide-butlers-model/tasks.md`

### 2 Other specifications (1)

- `openspec/changes/polaris-manifesto-generation/design.md`

### 3 Decisions and act records (4)

- `.syzygy/governance/decisions/DECISION-HISTORY.md`
- `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`
- `.syzygy/governance/decisions/POLARIS-M1-PAGE-SIZE-OWNER-RULING-DECISION.md`
- `.syzygy/governance/decisions/PWB-STATE1-AMENDMENT-ACT.md`

### 4 Other governed candidates (8)

- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/IMPACT-LEDGER.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/OWNER-DECISION-PACKET.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/SEMANTIC-DELTA.md`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/GOVERNING-DEPENDENCIES.md.patch`
- `.syzygy/governance/contracts/candidates/pwb-scoped-attributes-amendment/proposed/design.md.patch`
- `.syzygy/governance/contracts/candidates/pwb-state1-amendment/IMPACT-LEDGER.md`
- `.syzygy/governance/contracts/candidates/pwb-state1-amendment/REVIEW-BRIEF.md`
- `.syzygy/governance/contracts/candidates/pwb-state1-amendment/SEMANTIC-DELTA.md`

### 5 Implementation and tooling (12)

- `apps/three-surface-poc/src/fresh-checkout-demo-main.ts`
- `apps/three-surface-poc/src/fresh-checkout-verdict.ts`
- `apps/three-surface-poc/src/polaris-accessibility.ts`
- `apps/three-surface-poc/src/polaris-first-reading.test.ts`
- `apps/three-surface-poc/src/polaris-parity-sweep.test.ts`
- `apps/three-surface-poc/src/polaris-reachability.test.ts`
- `apps/three-surface-poc/src/polaris.ts`
- `apps/three-surface-poc/src/pwb-mutation-sweep-main.ts`
- `apps/three-surface-poc/src/pwb-mutation-sweep.ts`
- `apps/three-surface-poc/src/routes.ts`
- `packages/three-surface-poc-core/src/project-shape-model.ts`
- `scripts/record_pwb_state1_amendment.py`

### 6 Retained raw reviews and review packets (48)

- `docs/reviews/2026-09-05-pwb-live-exact-head-packet.md`
- `docs/reviews/R-POLARIS-M10-MACHINE-CONTRACT-FUNNEL-2-RAW.md`
- `docs/reviews/R-POLARIS-M10-MACHINE-CONTRACT-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-M11-OPERABILITY-FUNNEL-2-RAW.md`
- `docs/reviews/R-POLARIS-M11-OPERABILITY-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-M13-NAVIGATION-SCALE-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-2-RAW.md`
- `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-3-RAW.md`
- `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-4-RAW.md`
- `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-5-RAW.md`
- `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-6-RAW.md`
- `docs/reviews/R-POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-2-RAW.md`
- `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-3-RAW.md`
- `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-4-RAW.md`
- `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-5-RAW.md`
- `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-6-RAW.md`
- `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-7-RAW.md`
- `docs/reviews/R-POLARIS-M3-HONEST-ENCODING-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-3-RAW.md`
- `docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-4-RAW.md`
- `docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-5-RAW.md`
- `docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-6-RAW.md`
- `docs/reviews/R-POLARIS-M4-OWNER-LOOP-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-2-RAW.md`
- `docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-3-RAW.md`
- `docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-4-RAW.md`
- `docs/reviews/R-POLARIS-M5-AGENT-BRIEFING-FUNNEL-RAW.md`
- `docs/reviews/R-POLARIS-READING-ASSETS-CODE-2026-09-10-RAW.md`
- `docs/reviews/R-POLARIS-READING-ASSETS-REPAIR-2026-09-10-RAW.md`
- `docs/reviews/R-PWB-LIVE-EXACT-HEAD-TRUTH-RAW.md`
- `docs/reviews/R-PWB-M1-POLARIS-LANE-A-RAW.md`
- `docs/reviews/R-PWB-RECOVERY-RECONCILIATION-GEN1-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-2-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-3-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-4-RAW.md`
- `docs/reviews/R-PWB-SCOPED-ATTRIBUTES-DELTA-RAW.md`
- `docs/reviews/R-PWB-STATE1-ACT-SECURITY-RAW.md`
- `docs/reviews/R-PWB-STATE1-FINAL-ORACLES-RAW.md`
- `docs/reviews/R-PWB-STATE1-FINAL-SECURITY-RAW.md`
- `docs/reviews/R-PWB-STATE1-FINAL-TRANSACTION-RAW.md`
- `docs/reviews/R-PWB-STATE1-ORACLES-CONFIRMATION-RAW.md`
- `docs/reviews/R-PWB-STATE1-ORACLES-RAW.md`
- `docs/reviews/R-PWB-STATE1-SECURITY-CONFIRMATION-RAW.md`
- `docs/reviews/R-PWB-STATE1-SECURITY-RAW.md`
- `docs/reviews/R-PWB-STATE1-TRANSACTION-CONFIRMATION-RAW.md`
- `docs/reviews/R-PWB-STATE1-TRANSACTION-RAW.md`

### 7 Evidence and pursuit records (26)

- `docs/evidence/polaris-generator-host-overlap-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v2-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v3-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v4-2026-09-12.json`
- `docs/evidence/polaris-generator-rfc7-coverage-v5-2026-09-12.json`
- `docs/evidence/polaris-m10-machine-contract-funnel-2026-09-15.json`
- `docs/evidence/polaris-m11-operability-funnel-2026-09-15.json`
- `docs/evidence/polaris-m12-retained-evaluations-funnel-2026-09-15.json`
- `docs/evidence/polaris-m2-evidence-currency-funnel-2026-09-14.json`
- `docs/evidence/polaris-m3-honest-encoding-funnel-2026-09-14.json`
- `docs/evidence/polaris-m4-owner-loop-funnel-2026-09-14.json`
- `docs/evidence/polaris-m9-one-identity-funnel-2026-09-15.json`
- `docs/evidence/polaris-manifesto-example-mutation-2026-09-09.json`
- `docs/evidence/polaris-pipeline-synthetic-verification-2026-09-13.json`
- `docs/evidence/pwb-m1-polaris-lane-a-measurement-2026-09-13.json`
- `docs/evidence/pwb-p2-7-model-mutation-run-2026-09-04.json`
- `docs/evidence/pwb-p3-8-reachability-mutation-run-2026-09-04.json`
- `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-04-parity-markers.json`
- `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-04.json`
- `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-06-parity-markers.json`
- `docs/evidence/pwb-p4-2-mutation-sweep-2026-09-09-named-absent-file-dropped.json`
- `docs/evidence/pwb-p63-polaris-trim-measurement-2026-09-07.json`
- `docs/evidence/pwb-recon-gen2-reviewer-mutation-run-2026-09-06.json`
- `docs/pursuits/2026-09-13-vision-pursuit-data.json`
- `docs/pursuits/2026-09-13-vision-pursuit-harvest.json`

### 8 Docs prose (12)

- `docs/PWB-IMPLEMENTATION-PLAN.md`
- `docs/design/POLARIS-M1-PAGE-SIZE-FUNNEL.md`
- `docs/design/POLARIS-M10-MACHINE-CONTRACT-FUNNEL.md`
- `docs/design/POLARIS-M11-OPERABILITY-FUNNEL.md`
- `docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md`
- `docs/design/POLARIS-M13-NAVIGATION-SCALE-FUNNEL.md`
- `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md`
- `docs/design/POLARIS-M2-EVIDENCE-CURRENCY-FUNNEL.md`
- `docs/design/POLARIS-M3-HONEST-ENCODING-FUNNEL.md`
- `docs/design/POLARIS-M4-OWNER-LOOP-FUNNEL.md`
- `docs/design/POLARIS-M5-AGENT-BRIEFING-FUNNEL.md`
- `docs/design/POLARIS-M9-ONE-IDENTITY-FUNNEL.md`

### 9 Operating procedure (1)

- `AGENTS.md`

