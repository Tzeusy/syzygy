# Agent Instructions — Syzygy

This file is **repository operating procedure** — never citable as authority.
What the project *is* lives in `README.md` and `.syzygy/intent/OVERVIEW.md`.

## Current lifecycle stage: bounded Three-Surface POC mode

Doctrine is adopted; engineering policy is owner-approved. The Wave A/B
contracts and the CC-SPEC/CC-IMPACT craft policies are **accepted/in force
as of 2026-08-17**; deferred-wave contracts, topology, overview and the
remaining policy additions are **candidates awaiting owner acts**. The one
OpenSpec change `project-registration-and-honest-shape-visibility` was
**adopted by the owner — act dated 2026-08-20, recorded at
`decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`** at the exact
seven digests that record quotes (VIS-4; CC-SPEC-10); it is the accepted
behavioral authority for Capability 1 and supersedes the charter for
required behaviour. The owner's **implementation-authorization act —
dated 2026-08-21, recorded at
`decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`** —
authorized implementation planning and implementation for **Capability 1**:
plan first (`docs/CAPABILITY-1-IMPLEMENTATION-PLAN.md` names the
selected stack and layout), bounded Beads backlog, code in ordinary root
implementation paths (`apps/**`, `packages/**`, tooling, root
manifests) — **never inside `openspec/**` or `.syzygy/**`**, which stay
the governed project-artifact plane. The in-force craft policies and the
vendored `th-engineering` standards govern implementation.

The owner's direct direction dated **2026-08-29**, recorded at
`decisions/THREE-SURFACE-POC-MODE-DIRECTION.md`, now authorizes a bounded,
non-release proof of concept across Polaris, Trajectory, and Orrery using one
external Butlers repository. For this experiment only, it supersedes the
Capability-1-only and no-external-project-onboarding restrictions. It does not
authorize production release/deployment, autonomous intent adoption,
Syzygy-authored implementation code, broad remote access, multi-user support,
or changes to adopted doctrine or accepted contracts. All other prohibitions
and truth/evidence boundaries below remain in force.

## Where authority lives

| Question | Authority | Path | Binding today? |
|---|---|---|---|
| Why — purpose, non-negotiables | Doctrine (VIS-1…7, SEC-1…5) | `.syzygy/governance/doctrine/` | **Yes** — adopted 2026-07-30, D1 in force |
| Prior owner rulings | Decisions (SDR-1…33, warrants, pending queue) | `.syzygy/governance/decisions/` | **Yes** |
| Engineering and evidence bar | Craft-and-care (CC-*) | `.syzygy/governance/policies/craft-and-care/` | **Owner-approved (D2)**; clause force begins at the acceptance acts. **CC-SPEC-1…11 and CC-IMPACT-1…7 in force as of 2026-08-17** (acts 6/7, recorded in `INSTALL-RECORD.md`; the files bind at `contracts/candidates/policy-candidates/`, uncopied and unedited) |
| Load-bearing how | Design contracts RFC 0001–0011 | `.syzygy/governance/contracts/` | **RFC 0001–0009: accepted** — the Wave A and B acts were performed 2026-08-17 and recorded in `decisions/ACCEPTANCE-ACT-RECORD.md`, with the 30 modules installed at `contracts/rfcs/` as of 2026-08-17 (owner-adopted bootstrap, uncorrelated). RFC 0010–0011: **candidate**, in `contracts/candidates/` (deferred waves) |
| Intended placement | Topology bundle | `.syzygy/map/topology-candidates/` | **No — candidate.** `map/topology/` exists only after act 3 |
| Public narrative | Overview | `.syzygy/intent/OVERVIEW.md` | Governed presentation — **never authority** |

`GOVERNANCE-SUBSTRATE-LOCK.yaml` is a record, never authority. `README.md`
carries the reader-facing view.

**Cite by identifier** — `VIS-2`, `SEC-4`, `SDR-9`, `CC-REV-3`, `RFC10-9`.
Identifiers are amended in place or retired, **never renumbered**. Candidate
clauses may be discussed, never cited as binding.

## Pending owner gates

**Nine acts are open. Four acts have been performed — Waves A and B, then
craft acts 6 and 7 (CC-SPEC, CC-IMPACT), all 2026-08-17**
(`decisions/ACCEPTANCE-ACT-RECORD.md` owns the record); this file states no
more than that.

| Question | The one record that owns the answer |
|---|---|
| Which acts exist, their phrases, ceremony and arguments | `contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` |
| Current launch-path state — waves, gate, OpenSpec | `PROJECT-STATUS.md` |
| What each act would cost | the packet named in `decisions/README.md` |
| Process vocabulary — *act*, *argument*, *offer*, *confirmed* vs *accepted* | `PROCESS-GLOSSARY.md` |

Each digest belongs to the artifact it names, so verify with
`check_governance.py` (CG-7) before any act. **This file restates no digest
and no verdict.**

`decisions/ACCEPTANCE-ACT-RECORD.md` exists since the first act (Wave A,
2026-08-17) and owns every performed act; entries are appended, never
edited. Superseded offerings are banner-marked and retired phrases satisfy
nothing — never route an owner to a stale offering.

## Task routing — context is compiled, never accumulated

Load the minimum for one correct decision; never "read everything."

| Your task | Start here |
|---|---|
| A doctrine question | the one doctrine file, via the `heart-and-soul` skill |
| An engineering-bar question | the one craft policy that owns it |
| A contract question | **`contracts/candidates/TASK-ROUTER.md`** — the one generated router; context-budget measurement stays with `06-CONTEXT-LOAD-MAP.md` / `scripts/context_load.py` |
| "May I implement X?" | Capability 1 remains authorized under `decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`. The bounded Three-Surface POC and its one Butlers proving slice are additionally authorized by `decisions/THREE-SURFACE-POC-MODE-DIRECTION.md`. Anything outside both scopes remains forbidden. |
| "How would a spec be authored?" | `contracts/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` — router only; Capability 1's spec is **authored and adopted**; every other capability's authoring stays forbidden |
| The Capability 1 specification | the change `openspec/changes/project-registration-and-honest-shape-visibility/` — **ADOPTED by the owner (act dated 2026-08-20)** at the exact digests in `decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`; the seven adopted artifacts may not be edited (an edit breaks the adopted digests — route changes through CC-REV-2's amendment path); its warrants-union is generated (`build_capability_1_spec_dependencies.py`) |
| Current status | `PROJECT-STATUS.md` |
| "Is this ready for OpenSpec?" | Authoring was authorized by the owner's 2026-08-20 launch decision, made with Administration 1's `NOT READY` verdict (2026-08-18, out-of-family, v2.4) in hand as diagnostic evidence — that record stands unaltered in `decisions/launch-gate/`. `PROJECT-STATUS.md` owns the current state |
| A launch-gate administration | the record is **structured JSON** (`launch-gate-administration.schema.json`); the Markdown report is generated, **never parsed back**. Scripts: `validate_launch_administration.py`, `render_launch_administration.py`; `launch_gate_results.py` covers the historical Markdown records only |
| The launch-gate repair chain | `decisions/launch-gate/HISTORY.md` — **not default context**; the current policy is the instrument itself |
| Open owner questions | `decisions/PENDING-OWNER-DECISIONS.md` |
| Mission or Context-selection work | `contracts/candidates/DEFERRED-WAVE-POSTURE.md` first — deferred candidates route only through the router's deferred rows |
| What a term means | doctrine's glossary, `governance/doctrine/README.md`; then the candidate `policy-candidates/TERM-REGISTRY.md` |
| Maintenance, review, or avoiding a repeat mistake | `decisions/PROCESS-LESSONS.md` — **not default context** |

Historical process material lives in the git-excluded `_bootstrap/` tree,
`contracts/candidates/history/`, and the `round-*` trees — never on a default
path, never authority.

## Hard prohibitions

Do **not**: place implementation code inside `openspec/**` or
`.syzygy/**` (the governed plane — Capability 1 code lives in the plan's
named root paths, `apps/**`/`packages/**`/tooling, per the 2026-08-21
authorization act); implement, plan, or backlog anything beyond Capability 1
**except the eight-item Three-Surface POC authorized on 2026-08-29**; extend
that POC beyond one configured Butlers repository; implement deferred Waves
C1/C2/D1/D2 or substantive Mission Control; perform production deployment,
release, broad remote access, or multi-user support; allow Syzygy to write
implementation code; autonomously adopt intent; create any OpenSpec changeset **other than
the one adopted Capability 1 change**
(`project-registration-and-honest-shape-visibility` — adopted at exact
digests, `decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`) **and
the one owner-authorized candidate POC change**
(`three-surface-poc-experience` — authoring authorized 2026-08-30,
`decisions/THREE-SURFACE-POC-SPEC-AUTHORIZATION.md`; candidate, binds
nothing until owner sign-off, which also gates syzygy-z2b
implementation), or edit
that change's seven adopted artifacts (spec changes route through
CC-REV-2's amendment path); exceed the escalation triggers the
authorization act names (doctrine/contract change, spec amendment,
security/privacy/retention posture, constraints/envelope, scope beyond
Capability 1) without a new owner act; treat a draft, candidate, index,
summary, or generated view as authority; adopt doctrine, accept
contracts, or approve policy on the owner's behalf (VIS-4); install
candidate material into an accepted home or label it accepted; run
unattended agent coordination; **edit an artifact after an act has bound
its digest.**

## Epistemic and change discipline

Label substantive claims `[Observed]`, `[Inferred]`, or `[Unknown]`. No
evidence yields Unknown — never green, never zero (VIS-2). An LLM assertion
is Inferred. Preserve the owner's trade-offs; never smooth them into
consensus language.

Normative edits travel as **semantic deltas**
(`policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`); "editorial" and "no
semantic change" are reviewable claims. Reviews run in fresh context, given
only the artifact, its governing references and the acceptance criteria; raw
output is stored verbatim and **verdict words are copied exactly**.

## Verification rules

Ten rules, each paid for by a recorded incident. The incidents are in
`decisions/PROCESS-LESSONS.md`; read them before trusting a check.

1. **`grep` here is ugrep.** `[^]]`-style classes silently match nothing. Use
   `grep -F` or Python `re` for anything load-bearing.
2. **No "zero / all / 100%" claim without running that exact sweep this
   session**, confirmed by a second method. Enumerate remainders.
3. **Digests are scripted, never transcribed; totals are computed.**
4. **Read a check's *output*, not its exit code**, and check its denominator
   against the whole population.
5. **A citation is not a reliance** — a status banner or "(Shape-parallel
   with …)" is not a dependency edge.
6. **Mutate the input and confirm the check fails**, per predicate, before
   trusting it. `--selftest` holds the fixtures.
7. **Run the battery in a clone** before calling it green; a clone report is
   valid only for the commit it was run at.
8. **Anchor a claim about a contract to a *defined clause*, and quote it.**
   Section prose near a clause is not the clause.
9. **A claim of absence needs a sweep with a denominator.** VIS-2 applies to
   your own claims first.
10. **Freeze the bytes a review is bound to.** Editing the subject after a
    review names its digest retires the review, however small the edit.
    Batch the fix into the next pass.

**A generator that quotes prose has re-opened the door it closed.** Owning a
measurement means nothing inside the generated file was copied.

## Validation

All read-only; run before claiming anything is clean.

**`PROJECT-STATUS.md` §"How to verify this page" owns the canonical battery.**
Run that block, never a copy: `CG-26` compares it against hosted CI,
and nothing compares a third list. Everyday:
`python3 scripts/check_governance.py`; `--selftest` runs the fixtures (CG-24
prints coverage).

## Beads scope in this phase

`bd` tracks process housekeeping, the bounded Capability 1 backlog, **and at
most eight outcome-oriented Three-Surface POC items** authorized on 2026-08-29.
POC shared-model changes have WIP one. Apart from the initial mode-switch item,
each POC item must alter the runnable demonstration or falsify a named product
assumption. Unknowns remain explicit; they do not authorize synthetic positive
evidence. Commits land at stable gates; **never commit a normative artifact
while its adoption gate is unresolved.**

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:7510c1e2 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Session Completion

**MANDATORY — work is NOT complete until `git push` succeeds:**

1. **File issues** for remaining work; close finished issues, update
   in-progress ones
2. **Run quality gates** (if code changed)
3. **Push**: `git pull --rebase && git push`; `git status` must show
   "up to date with origin"
4. **Clean up** (stashes, stale branches) and **hand off** context for the
   next session

NEVER stop before pushing — that strands work locally. If push fails,
resolve and retry until it succeeds.
<!-- END BEADS INTEGRATION -->

## Notes to self

### Three-Surface POC architecture

- The bounded POC lives in `packages/three-surface-poc-core/` (one concrete,
  immutable Butlers graph) and `apps/three-surface-poc/` (SSR HTML plus
  authenticated `GET /api/poc`). Both human and machine routes consume the
  same model instance; do not split surface truth stores.
- `npm ci && npm run poc -- --repo /home/tze/GitHub/butlers` is the fresh
  checkout command. Observation is fixed to five configured intent/code/test
  files, outputs hashes and metadata only, and writes credentials solely to an
  OS-temp state directory unless `--state-dir` is explicit.
- The first slice intentionally keeps the work item, test-run evidence, live
  runtime relationship, and unmapped code region Unknown. Later POC items may
  raise only the relationship whose authoritative artifact they actually add.
- The launcher permits unrelated dirty Syzygy files (for example `.gitignore`)
  but refuses uncommitted changes to the POC, reused Capability 1 runtime
  packages, or root build manifests; keep that classification path-based and
  covered by the real-Git regression test. `build:poc` must retain
  `tsc -b --force`: ignored incremental outputs are executable inputs, so a
  normal up-to-date check is not a sufficient trust boundary.

### Capability 1 implementation status

**Complete end-to-end (2026-08-23), with the first runtime-hardening leaves
merged 2026-08-24.** [Observed] Domain: S0–S7
(296 conformance tests). Runtime vertical slice: epic syzygy-zal RT1–RT9
all closed — real filesystem observation, exact fail-closed
consent-reference loading, credential-backed local daemon (127.0.0.1,
bearer token 0600, constant-time compare), JSON machine endpoint
(`GET /api/project`), server-rendered human page + "Why this answer?"
(`GET /`, `GET /entry`), write-boundary normalization/traversal/symlink
protection, true process/filesystem/HTTP system tests
(`npm run test:system`; fresh-clone test gated by `SYZYGY_FRESH_CLONE=1`),
and hosted `node-ci` (green on main; verified by step output, not exit
code). The fresh-clone bar is met and automated: clone → `npm ci` →
`npm run build` → daemon start → same seven facts via browser-equivalent
GET and authenticated machine request, wire-parity sweep 7/7. Runtime
review cycle: R-RT review **CONFIRM WITH EXCEPTIONS** at f0a0f45 (one
non-blocking finding RTF-1), one repair (00d6020), confirmation
**CONFIRMED** — records in `docs/reviews/R-RT-*.md`. Current verified
denominator including the POC slice: 58 unit/conformance files with 427 tests,
plus 8 system files
with 33 tests when the guarded fresh-clone case is enabled. Node floor is
>=22.15 (Node 20 is EOL); CI runs Node 24.

Known honest gaps (follow-up bead, not defects): pipeline does not yet
compute discoverability findings / authority exposures (page renders
disclosed absence); `evaluateProject` runs once at startup (snapshot
semantics, as-of disclosed). The snapshot/coverage/discoverability chain
remains blocked on human gate `syzygy-u2a.1`: a lawful independently kept
RFC5-25 consent-audit source must be identified before repository observation
can be authorized.

### Implementation architecture

- 14 pure domain modules in `packages/cap1-core/src/`, re-exported via
  `index.ts`. Zero I/O, zero clock reads, zero side effects.
- Conformance tests in `packages/cap1-conformance/src/`, one file per
  CAP1-REQ-NNN plus `req-integration.conformance.test.ts`.
- Closed vocabularies as `as const` tuples; branded ID types (`ProjectId`,
  `RepositoryId`, `EvaluationId`); discriminated-union results with named
  failure arms.
- Parity by construction: one `FactModel`, `serveMachine`/`renderHuman`
  both from the same source; independent oracle compares channel outputs.

### Lessons learned (durable)

- **FROZEN rule**: workers must declare files FROZEN after final report;
  orchestrator re-verifies staged bytes match tested bytes before commit
  (the S3 mutation race, fixed in bd84cf0).
- **Fail-closed polarity**: withdrawal defeats grant (consent); future-dated
  evidence fails to stale; no evidence → Unknown, never green.
- **Oracle independence in tests**: expected values are hard-coded string
  literals in conformance tests, never imported from vocabulary modules.
- **Rule-6 mutation check**: temporarily break the fix, confirm the
  falsifier test fails, restore — proves the test can catch the defect.
- **No-build Vitest seam**: root `test.projects` must alias both
  `@syzygy/cap1-core` and `@syzygy/cap1-daemon` to source. Built `dist/`
  output can mask a missing alias, so verify after `npm ci` with every project
  `dist/` absent; the pre-POC denominator was 53 files / 417 tests.

### Open follow-up work

- Bead syzygy-ydr: non-blocking S2/S5 review findings (consent-reference
  resolution, admissibility bar, grant-state rendering citations, and
  unreachable-vs-observer-failure split).
- Review WARNING: `authorizeWrite` uses raw `startsWith` — path traversal
  like `openspec/../README.md` passes. Caller must normalize.
