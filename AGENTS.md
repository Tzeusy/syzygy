# Agent Instructions — Syzygy

Repository operating procedure for any agent session, in any harness. It is
**never citable as authority** and restates no digest, verdict, or act
history. What the project *is*: `README.md` and `.syzygy/intent/OVERVIEW.md`.
What state it is in: `PROJECT-STATUS.md`. Where they and this file disagree,
they win.

## Orientation

Syzygy is a specification-driven control plane: humans define what should be
true, evidence shows what is true, agents do bounded work to close the gap,
and the gap is always rendered honestly. Two planes:

- **Governed** — `.syzygy/**` (doctrine, decisions, policies, contracts) and
  `openspec/**` (specifications). Changes travel as reviewed semantic deltas
  and bind only by owner act.
- **Implementation** — `apps/**`, `packages/**`, `scripts/`, root manifests.
  Code goes here and only here.

Everything is stage-gated. Each authorization is a dated owner act or
direction under `.syzygy/governance/decisions/` (`ACCEPTANCE-ACT-RECORD.md`
owns acceptance and amendment transactions). `PROJECT-STATUS.md` says which
are in force. As of 2026-09-05: Capability 1 is implemented; a bounded,
non-release Three-Surface POC (Polaris, Trajectory, Orrery) runs against one
Butlers repository, whose PWB project-shape slice may read one consented
content class behind the P1 authority gate. Anything no act covers is
forbidden — before implementing, find the act.

## Where authority lives

| Question | Authority | Path | Status |
|---|---|---|---|
| Why — purpose, non-negotiables | Doctrine (VIS-1…7, SEC-1…5) | `.syzygy/governance/doctrine/` | Adopted, in force |
| Prior owner rulings | Decisions (SDR-1…37, acts, pending queue) | `.syzygy/governance/decisions/` | In force |
| Engineering and evidence bar | Craft-and-care (CC-*) | `.syzygy/governance/policies/craft-and-care/` | CC-SPEC, CC-IMPACT in force; rest owner-approved |
| Load-bearing how | Design contracts RFC 0001–0011 | `.syzygy/governance/contracts/` | 0001–0009 accepted; 0010–0011 candidate in `contracts/candidates/` |
| Intended placement | Topology bundle | `.syzygy/map/topology-candidates/` | Candidate |
| Public narrative | Overview | `.syzygy/intent/OVERVIEW.md` | Presentation, never authority |

`GOVERNANCE-SUBSTRATE-LOCK.yaml` is a record, never authority. **Cite by
identifier** (`VIS-2`, `SDR-9`, `RFC10-9`); identifiers are amended in place
or retired, never renumbered. Candidate clauses, drafts, indexes, summaries,
and generated views are never authority.

## Task routing — context is compiled, never accumulated

Load the minimum for one correct decision; never "read everything."

| Your task | Start here |
|---|---|
| Current state, gates, next lawful step | `PROJECT-STATUS.md` |
| A doctrine question | the one doctrine file, via the `heart-and-soul` skill |
| An engineering-bar question | the one craft policy that owns it |
| A contract question | `contracts/candidates/TASK-ROUTER.md` (generated) |
| "May I implement X?" | the authorizing act in `decisions/`; plans: `docs/CAPABILITY-1-IMPLEMENTATION-PLAN.md`, `docs/PWB-IMPLEMENTATION-PLAN.md` |
| The Capability 1 specification | `openspec/changes/project-registration-and-honest-shape-visibility/` — adopted; amend only via CC-REV-2 |
| Authoring a new spec | `contracts/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md`; only owner sign-off binds it (VIS-4) |
| Which acts exist, their phrases and ceremony | `contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`; packets per `decisions/README.md` |
| Open owner questions | `decisions/PENDING-OWNER-DECISIONS.md` |
| A launch-gate administration | structured JSON (`launch-gate-administration.schema.json`); the Markdown report is generated, never parsed |
| Mission or Context-selection work | `contracts/candidates/DEFERRED-WAVE-POSTURE.md` first |
| What a term means | `governance/doctrine/README.md` glossary, then `PROCESS-GLOSSARY.md` |
| Avoiding a repeat mistake | `decisions/PROCESS-LESSONS.md` — not default context |

Historical material (`_bootstrap/`, `contracts/candidates/history/`,
`round-*`) is never on a default path and never authority. Superseded
offerings are banner-marked; retired phrases satisfy nothing — never route
an owner to a stale offering.

## Hard prohibitions

- No implementation code inside `openspec/**` or `.syzygy/**`.
- Nothing beyond the acts in force: no deferred waves (C1/C2/D1/D2), Mission
  Control, production deployment, release, broad remote access, multi-user
  support.
- Never read a repository body without per-repository consent and the
  applicable registry and policy acts (Butlers: the consented content class
  only, after the implementation's PWB-REQ-005 evaluation).
- The daemon never executes observed project code or test suites; separate
  operator commands do.
- Syzygy never writes implementation code or adopts intent autonomously.
- Never adopt doctrine, accept contracts, approve policy, or label anything
  accepted on the owner's behalf (VIS-4); never install candidate material
  into an accepted home.
- Never edit an artifact after an act has bound its digest.
- An OpenSpec change is one coherent category overlapping no other change,
  binding nothing until owner sign-off.
- An act's escalation triggers (doctrine or contract change, spec amendment,
  security/privacy/retention posture, scope) need a new owner act.
- No unattended agent coordination.

## Epistemic and change discipline

Label substantive claims `[Observed]`, `[Inferred]`, or `[Unknown]`. No
evidence yields Unknown — never green, never zero (VIS-2). An LLM assertion
is Inferred. Preserve the owner's trade-offs; never smooth them into
consensus language. Normative edits travel as semantic deltas
(`policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`); "editorial" is a
reviewable claim. Reviews run in fresh context with only the artifact, its
governing references, and the acceptance criteria; raw output is stored
verbatim and verdict words are copied exactly.

## Verification rules

Each paid for by an incident in `decisions/PROCESS-LESSONS.md`. Numbering
is stable; reviews cite rules by number.

1. `grep` here is ugrep; `[^]]`-style classes silently match nothing. Use
   `grep -F` or Python `re` for anything load-bearing.
2. No "zero / all / 100%" claim without running that exact sweep this
   session, confirmed by a second method. Enumerate remainders.
3. Digests are scripted, never transcribed; totals are computed.
4. Read a check's output, not its exit code, and check its denominator
   against the whole population.
5. A citation is not a reliance; a status banner is not a dependency edge.
6. Mutate the input and confirm the check fails, per predicate, before
   trusting it (`--selftest` holds the fixtures).
7. Run the battery in a clone before calling it green; the report is valid
   only for that commit.
8. Anchor a contract claim to a defined clause and quote it; nearby prose is
   not the clause.
9. A claim of absence needs a sweep with a denominator.
10. Freeze the bytes a review is bound to; any later edit retires the review.

A generator that quotes prose has re-opened the door it closed.

## Validation

`PROJECT-STATUS.md` §"How to verify this page" owns the canonical battery;
run that block, never a copy. Everyday: `python3 scripts/check_governance.py`
(`--selftest` runs the fixtures). All read-only; run before claiming clean.

## Beads scope

`bd` tracks housekeeping, the Capability 1 backlog, and POC improvement
cycles (review → repair beads from recorded findings → confirmation, reported
to the owner before the next cycle). POC shared-model changes have WIP one.
Commits land at stable gates; never commit a normative artifact while its
adoption gate is unresolved.

## Notes to self

Durable lessons only; status and narrative belong in git log, `bd`, or
`PROJECT-STATUS.md`. Capability 1 status, the FROZEN-files rule, and the
tailscale `--set-path` finding live in `bd memories` — do not re-add them.
Last compacted 2026-09-05; C5 seams and recorder notes added the same day.

### Architecture

- `packages/cap1-core/`: pure domain modules; one conformance file per
  CAP1-REQ in `packages/cap1-conformance/`. One `FactModel` feeds both
  channels; an independent oracle compares their outputs.
- Three-Surface POC: `packages/three-surface-poc-core/` (one shared
  `PocModel`) and `apps/three-surface-poc/` read the same instance — never
  split surface truth stores. `build:poc` keeps `tsc -b --force`: ignored
  incremental outputs are executable inputs.
- PWB pipeline (pure, injectable, in order): `body-read-authority` gates
  every Butlers read → observation → `git-object-reader` → classification
  (excluded content yields hash-not-body records) → extraction (literal
  grammar) → coverage (precedence only via a Butlers-declared
  `PrecedenceRule`, never "newest wins") → `PocModel.projectShape`.
  Since the 2026-09-05 amendment the precedence input is the root index's
  own seven-row `Precedence Order When Layers Disagree` table, admitted
  only when every row matches the registry literal grammar; a row decides
  a disagreement only when exactly one declaration lies under its home.
- Two render-time seams sit beside the shape, both pure and injectable:
  `walkthrough-readiness.ts` (core; PWB-REQ-021 nine answer identities,
  ten arms, never a verdict or score, never touches the PWB-REQ-022
  evaluator) and `verbatim-route.ts` (app; PWB-REQ-011 exact-requirement
  route, derived per render from the model, caches nothing). Phase B
  classifies baseline specs path-only, so the route runs the unchanged
  secret detectors and active-content scan on the transient body itself.

### Guardrails (keep even when old)

- Fresh `git worktree`: run `npm ci` inside it first, or `NodeNext` silently
  resolves `@syzygy/*` to the main checkout's `node_modules`.
- `git ls-tree` needs `-z`, or quoted paths break the parser.
- `npm run poc:pwb-*-mutation-*` rewrites sources in place (~35 min): never
  edit or commit while it runs.
- CDP headless: enable `Emulation.setFocusEmulationEnabled` or focus never
  moves; re-navigate before Tab/Enter when the fragment already matches the
  hash; `<summary>` needs its own `:focus-visible` rule.
- The Write tool has emitted mixed NFC/NFD bytes; use Unicode escapes in
  fixtures when exact matching matters.
- A mutation that throws at describe time reports zero tests and scores as
  survived — build fixtures in `beforeAll`.
- Fail-closed polarity: withdrawal defeats grant; future-dated evidence is
  stale; no evidence → Unknown.
- Conformance expected values are hard-coded literals, never imported from
  the module under test.
- Root Vitest `test.projects` must alias both `@syzygy/cap1-core` and
  `@syzygy/cap1-daemon` to source; verify with every `dist/` absent.
- Butlers' pytest needs its own `.venv/bin/python`.
- Never wire `WORKER_CHANGE_SEAM` test-artifact evidence into the unrelated
  identity-resolution entities in `model.ts` — false "Verified" (reverted
  once already).
- Never quote a performed act's argument or a truncated signed digest in a
  new artifact unless it is in `ACT_DIGEST_COPY_FILES` (CG-7e/CG-15); cite
  the record by path. Never backtick a Butlers path in a packet (CG-1b).
- `authorizeWrite` uses raw `startsWith` for containment; callers must
  normalize paths first (tracked, unfixed).
- App typecheck (`tsc --noEmit -p apps/three-surface-poc`) resolves core
  through `dist` declarations: run `tsc -b packages/three-surface-poc-core`
  first after a core type change, or the app reports phantom errors.
- Ledger semantics: a refused read is not a counted pass; phase-B breaches
  are typed findings and do not set the degradation state; catalog
  extraction keys off the basename `v1.md`. The tailnet mount is detected
  by `Host`, never by path.
- Copy-oracle tests match by substring: a very short label (`None`) is
  "reached" by coincidence and proves nothing — give every label a
  distinctive string or drop it.

### Known gaps

- syzygy-ydr: non-blocking S2/S5 review findings outstanding.
- Butlers data quirks (as of `a3dd1fe`): `v1.md` is whole-source Unknown
  (one row uses a colon outside the signed dash grammar); Lay and Land's
  index is excluded. Do not relax the grammar without an owner gate.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:7510c1e2 -->
### Governance recorders (digest-bound acts)

- Each digest-bound owner act has a dedicated recorder script that
  hard-codes the frozen subject and packet head, validates the owner's
  phrase against current bytes, writes a new dedicated record and appends
  one aggregate section to `ACCEPTANCE-ACT-RECORD.md`; `--check` must
  count exactly one copy of its block, never assume it is the file tail.
  A superseding act gets a new record; the superseded record is never
  edited, and its recorder fails `--check` by design.
- Register a new act phrase in `check_governance.py`'s `_act_subjects()`
  and its packet copies in `ACT_DIGEST_COPY_FILES` before the packet
  exists, or CG-7d cannot see them go stale; files that appear only after
  an act are registered from an existence-gated activation function.
- Plain owner directions (implementation authorization, continuation)
  bind no digest, add no acceptance-record row and register nothing.

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
