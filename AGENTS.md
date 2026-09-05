# Agent Instructions — Syzygy

This file is **repository operating procedure** — never citable as authority.
What the project *is* lives in `README.md` and `.syzygy/intent/OVERVIEW.md`.

## Current lifecycle stage: bounded Three-Surface POC mode

Doctrine is adopted; engineering policy is owner-approved. The Wave A/B
contracts and the CC-SPEC/CC-IMPACT craft policies are **accepted/in force
through their 2026-08-17 original acts and the 2026-09-01 trusted-bootstrap
amendment** (`PROJECT-STATUS.md` owns current state); deferred-wave contracts,
topology, overview and the remaining
policy additions are **candidates awaiting owner acts**. The one
OpenSpec change `project-registration-and-honest-shape-visibility` was
**adopted by the owner — act dated 2026-08-20, recorded at
`decisions/CAPABILITY-1-SPECIFICATION-ADOPTION-ACT.md`** at the exact
seven act-time digests that record quotes (VIS-4; CC-SPEC-10); its
`CONTRACT-COVERAGE.md` digest was separately amended by the 2026-09-01
transaction recorded in `decisions/ACCEPTANCE-ACT-RECORD.md`. It remains the
accepted behavioral authority for Capability 1 and supersedes the charter for
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

The owner separately performed the indivisible five-row general
trusted-bootstrap authorization transaction on **2026-09-01**, recorded in
`decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md` and
`decisions/ACCEPTANCE-ACT-RECORD.md`. RFC 0001–0009 remain accepted and their
current bytes are bound at the exact 30-module amendment manifest; seven signed
coverage artifacts and CC-SPEC-8 are amended. Valid exact-scope human acts may
be effective in state (1), `owner-adopted (bootstrap, uncorrelated)`, or state
(2), `Syzygy-verified`; only state (2) is independently verified.
At that transaction PWB-REQ-005 and PWB-REQ-022 remained state-(2)-only. The
owner separately signed their eleven-artifact state-(1) amendment on
**2026-09-02**, recorded in `decisions/PWB-STATE1-AMENDMENT-ACT.md`: both now
accept valid state (1) or state (2), preserve exact state and fail invalid acts
closed. Neither act granted consent, observation, write, egress, execution,
deployment, release, recovery, mission, or implementation authority. Later the
same day the owner performed the **three separate PWB effect acts** — Butlers
observation consent, secret-classification policy approval, observer
registry-entry adoption — each state (1), bound to its artifact's SHA-256
(`decisions/PWB-BUTLERS-OBSERVATION-CONSENT-ACT.md`,
`decisions/PWB-SECRET-CLASSIFICATION-POLICY-ACT.md`,
`decisions/PWB-OBSERVER-REGISTRY-ENTRY-ACT.md`). They close the effect gate for
the one Butlers project-shape content class. The owner then granted **PWB
implementation authorization** by direct direction the same day
(`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md`, closing task 1.8): tasks
§2–§5 of the signed change are dispatchable in the ordinary implementation
plane; the first Butlers body read is lawful only after the implementation
evaluates the three acts under PWB-REQ-005, and only for the consented
content class. Still no write, egress, execution, deployment, release,
recovery, or mission authority.

## Where authority lives

| Question | Authority | Path | Binding today? |
|---|---|---|---|
| Why — purpose, non-negotiables | Doctrine (VIS-1…7, SEC-1…5) | `.syzygy/governance/doctrine/` | **Yes** — adopted 2026-07-30, D1 in force |
| Prior owner rulings | Decisions (SDR-1…37, warrants, pending queue) | `.syzygy/governance/decisions/` | **Yes** |
| Engineering and evidence bar | Craft-and-care (CC-*) | `.syzygy/governance/policies/craft-and-care/` | **Owner-approved (D2)**; **CC-SPEC-1…11 and CC-IMPACT-1…7 are in force**. The original acts 6/7 were performed 2026-08-17; CC-SPEC-8 was amended in the separate 2026-09-01 transaction, while CC-IMPACT was unchanged. |
| Load-bearing how | Design contracts RFC 0001–0011 | `.syzygy/governance/contracts/` | **RFC 0001–0009: accepted and amended** — originally accepted by the 2026-08-17 Wave A/B acts; their current installed bytes are bound at the 2026-09-01 30-module contract-amendment manifest. The performed-wave manifests remain immutable act-time history. RFC 0010–0011: **candidate**, in `contracts/candidates/` (deferred waves) |
| Intended placement | Topology bundle | `.syzygy/map/topology-candidates/` | **No — candidate.** `map/topology/` exists only after act 3 |
| Public narrative | Overview | `.syzygy/intent/OVERVIEW.md` | Governed presentation — **never authority** |

`GOVERNANCE-SUBSTRATE-LOCK.yaml` is a record, never authority. `README.md`
carries the reader-facing view.

**Cite by identifier** — `VIS-2`, `SEC-4`, `SDR-9`, `CC-REV-3`, `RFC10-9`.
Identifiers are amended in place or retired, **never renumbered**. Candidate
clauses may be discussed, never cited as binding.

## Pending owner gates

**Nine foundational offerings remain open. Four original foundational acts
were performed — Waves A and B, then craft acts 6 and 7 (CC-SPEC, CC-IMPACT),
all 2026-08-17. A separate indivisible five-row amendment transaction was
performed 2026-09-01** (`decisions/ACCEPTANCE-ACT-RECORD.md` owns the
record); it does not close any of the nine foundational offerings.

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
2026-08-17) and owns every performed act and amendment transaction; the
2026-09-01 transaction also has the dedicated
`decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md`. Entries are
appended, never edited. Superseded offerings are banner-marked and retired
phrases satisfy nothing — never route an owner to a stale offering.

## Task routing — context is compiled, never accumulated

Load the minimum for one correct decision; never "read everything."

| Your task | Start here |
|---|---|
| A doctrine question | the one doctrine file, via the `heart-and-soul` skill |
| An engineering-bar question | the one craft policy that owns it |
| A contract question | **`contracts/candidates/TASK-ROUTER.md`** — the one generated router; context-budget measurement stays with `06-CONTEXT-LOAD-MAP.md` / `scripts/context_load.py` |
| "May I implement X?" | Capability 1 remains authorized under `decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`. The bounded Three-Surface POC and its one Butlers proving slice are additionally authorized by `decisions/THREE-SURFACE-POC-MODE-DIRECTION.md`; the surface-redesign item `syzygy-z2b` is authorized by the signed-off `three-surface-poc-experience` spec (`decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`). The `polaris-project-wide-butlers-model` change is signed, its three effect acts are performed, and its implementation is authorized by `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` (plan: `docs/PWB-IMPLEMENTATION-PLAN.md`; tasks §2–§5, one Butlers repository, content class `declared-project-shape-text`, body read only after in-implementation PWB-REQ-005 evaluation). Anything outside these authorized scopes remains forbidden. |
| "How would a spec be authored?" | `contracts/candidates/HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` — router only; Capability 1's spec is **authored and adopted**; every other capability's authoring stays forbidden |
| The Capability 1 specification | the change `openspec/changes/project-registration-and-honest-shape-visibility/` — **ADOPTED by the owner (act dated 2026-08-20)**; the 2026-09-01 transaction superseded only `CONTRACT-COVERAGE.md`'s digest. The current seven-artifact set may not be edited outside CC-REV-2's amendment path; its warrants-union is generated (`build_capability_1_spec_dependencies.py`). See the original act plus `decisions/ACCEPTANCE-ACT-RECORD.md`. |
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
**except the Three-Surface POC authorized on 2026-08-29 and its
improvement cycles authorized on 2026-08-30
(`decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`)**; extend
that POC beyond one configured Butlers repository; read Butlers body
content outside the consented `declared-project-shape-text` class, or before
the implementation has evaluated the three 2026-09-02 effect acts under
PWB-REQ-005 (`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` bounds the
PWB implementation); read any new repository body before
per-repository consent and the applicable registry/policy acts; implement
deferred Waves C1/C2/D1/D2 or substantive Mission Control; perform production
deployment, release, broad remote access, or multi-user support; allow Syzygy
to write implementation code; autonomously adopt intent; create an OpenSpec
changeset that overlaps another change or is not a coherent, clearly
scoped category (the owner's 2026-08-30 direction
`decisions/OPENSPEC-MULTI-CHANGE-DIRECTION.md` permits multiple
changes under exactly those two conditions; every new change is a
candidate binding nothing until owner sign-off, VIS-4); edit the current
Capability 1 change's seven adopted artifacts (the original act plus the
2026-09-01 coverage amendment in `decisions/ACCEPTANCE-ACT-RECORD.md`) or the
current six signed `three-surface-poc-experience` artifacts
(`decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md` — signed off
2026-08-30, which also unblocked syzygy-z2b implementation; spec
changes route through CC-REV-2's amendment path); exceed the escalation triggers the
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

`bd` tracks process housekeeping, the bounded Capability 1 backlog, the
**closed eight-item Three-Surface POC** (2026-08-29), **and POC
improvement-cycle items** (owner direction 2026-08-30,
`decisions/THREE-SURFACE-POC-IMPROVEMENT-CYCLES-DIRECTION.md`): each cycle is
review → repair beads derived only from recorded findings → confirmation,
reported to the owner before the next cycle starts. POC shared-model changes
have WIP one. Each POC item must alter the runnable demonstration or
falsify/repair a named, recorded product finding. Unknowns remain explicit; they do not authorize synthetic positive
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

### Three-surface redesign (syzygy-z2b): Polaris/Trajectory/Orrery

- Two new pure-ish observers in `packages/three-surface-poc-core/src/`:
  `code-structure.ts` (git `ls-tree -r -l` at an exact revision — metadata
  only, never opens blob content) and `work-items.ts` (shells `bd sql
  --json` against the live Dolt server; **never** reads the JSONL export —
  asserted by a static-source sweep, not just runtime behavior). Both
  return an `{kind:'observed'|'unknown', ...}` union and take an injectable
  `runGit`/`runQuery` for hermetic tests. `PocModel` now carries
  `codeStructure`, `workItems`, `orrery`, `trajectory` fields, computed
  inside `buildButlersPocModel` — still one shared model, still
  parity-by-construction (`GET /api/poc` is `JSON.stringify(model)`
  verbatim).
- `apps/three-surface-poc/src/{polaris,trajectory,orrery}.ts` are the three
  new human routes; `page-shell.ts` + `design-tokens.ts` are the one
  shared chrome/token/legend source all four pages (home included) render
  from. Orrery is the only surface with real client-side rendering (an
  inline, self-served `<script>` — no separate bundle, no CDN); Polaris and
  Trajectory are plain SSR since nothing in the spec requires otherwise.
  `exact-tables.ts` holds the entity/relationship table renderer shared by
  the home page and Orrery's no-script/route-resolution backstop.
- **`tailscale serve --set-path /butlers-syzygy <target>` strips the mount
  prefix before forwarding and adds no header naming it** — verified
  empirically (a throwaway second `--set-path` mount to a raw echo
  listener). A browser request to `.../butlers-syzygy/polaris` reaches the
  daemon as literal path `/polaris`; the `TAILNET_MOUNT_PREFIX`-prefixed
  routes registered in `routes.ts`/`polaris.ts`/`trajectory.ts`/`orrery.ts`/
  `materialize-action.ts` are therefore unreachable through this real
  deployment (harmless leftovers for a hypothetical path-preserving proxy).
  The one signal that survives the hop is the Host header, which `tailscale
  serve` does forward faithfully — `tailnet.ts`'s `mountPrefixForRequest`
  keys off it (via `browser-origin.ts`'s exported `TAILNET_HOST`, the same
  constant its origin-admission check already uses) to decide whether
  every internal href/form-action a page renders needs the
  `/butlers-syzygy` prefix. A **Fetch API/undici test client silently
  drops an overridden `Host` header** — `apps/three-surface-poc/src/
  test-http-client.ts`'s `fetchWithHost` uses `node:http` directly to
  simulate a request that genuinely carries a different Host.
- **Worktree gotcha**: a freshly created `git worktree` under
  `.worktrees/parallel-agents/<id>` has no local `node_modules`. Since this
  repo has no `paths` mapping in `tsconfig.base.json`, `NodeNext` module
  resolution for `@syzygy/*` packages walks up to the *main* checkout's
  `node_modules/@syzygy/*` symlinks (which point at the main checkout's own
  `packages/*`/`apps/*`) — so `tsc -b`/`vitest` silently type-check and run
  against the wrong (stale) package copy instead of the worktree's edits,
  with no error, just confusing "property does not exist" failures. Fix:
  run `npm ci` inside the worktree once before trusting any cross-package
  build or test there.
- Honest gaps from the first implementation pass (see
  `openspec/changes/three-surface-poc-experience/tasks.md` §3.5/4.1/4.2 for
  the precise state): no automated WCAG AA contrast measurement or
  browser-driven keyboard-traversal E2E (structural accessibility checks
  only); no single sweep that counts and diffs *every* parity marker across
  all three surfaces against the machine answer in one pass (existing
  per-surface parity tests are structural/by-construction, not an
  exhaustive marker sweep like `routes.test.ts` already does for the home
  page); the fresh-checkout demo was run manually against the real Butlers
  repo this session, not from a truly fresh `git clone`.

### Test-artifact verification (syzygy-0r9)

- `packages/three-surface-poc-core/src/test-artifact-verification.ts` is the
  ingestion/verification module: a file-backed `TestArtifactRecord` (command,
  exit status, capture time, commit, scope, digest, safe summary — never raw
  test body/exceptions, AC5), parsed from a real JUnit artifact by reading
  only the opening `<testsuite>`/`<testsuites>` tag's attributes (never
  descending into `<testcase>`/`<failure>` content). `resolveTestArtifactVerification`
  is pure and fail-closed: Verified only when the record's commit exactly
  matches the git-observed `changed-or-merged` commit from
  `worker-change-observation.ts`, the scope matches the bounded seam, the
  exit code is 0, and capture time is neither future-dated nor earlier than
  the commit itself.
- **This evidence is scoped to the `WORKER_CHANGE_SEAM`
  (`whatsapp_user_client.py`, intent `REQ-connector-base-spec-001`, exported
  as `WORKER_CHANGE_INTENT_ID`) — a different capability/code file than
  `code:identity-resolution`/`REQ-switchboard-identity-001`.** It is
  surfaced only through the top-level `PocModel.testArtifactVerification`
  field and the Trajectory worker-change badge; it must never be wired into
  the `evidence:focused-pytest` entity or `relationship:code-to-evidence` in
  `model.ts`, since those belong to the unrelated identity-resolution
  capability — doing so would render a false "Verified" claim against code
  the captured test never touches. (First implementation pass made exactly
  this mistake and had to be reverted before commit — watch for it in
  review.)
- Real capture tool: `apps/three-surface-poc/src/capture-test-artifact.ts`
  (pure orchestration, injectable) + `capture-test-artifact-main.ts` (real
  CLI, `npm run poc:capture-test-artifact -- --repo <butlers> --scope <path>
  --state-dir <dir> [--python <bin>]`). It is a separate, manually-invoked
  binary — `main.ts` (the running daemon) never imports it and never shells
  the observed test suite itself (SEC-3). Butlers' pytest needs its own venv
  interpreter (`/home/tze/GitHub/butlers/.venv/bin/python`, not bare
  `python3`) or collection fails with `ModuleNotFoundError: No module named
  'butlers'` before any JUnit file is written.
- Verified end-to-end this session with a real, live-gated test
  (`test-artifact-verification.live.test.ts`, `SYZYGY_POC_BUTLERS_REPO`- and
  `SYZYGY_POC_BUTLERS_PYTHON`-gated): ran the real focused pytest suite
  against real Butlers HEAD (83 passed), ingested the real artifact, and
  rendered Verified through the full shared model. Because the git-based
  worker-change observer only matches commits carrying a literal
  `[<materialized-bead-id>]` marker, and no real historical Butlers commit
  carries a live Syzygy bead marker, the *composed* live proof injects
  `runGit` to bind the observer to the real captured commit — the observer's
  own real-git marker-matching is separately covered by
  `worker-change-observation.test.ts`.

### Contract-amendment manifest discipline

- Performed Wave A/B manifests are immutable act-time arguments. Current
  amendments to accepted RFC modules use a separate amendment manifest;
  `build_active_manifest.py` regenerates the active view and unperformed waves,
  but verifies performed manifests by recorded digest and path membership
  without rewriting or comparing their historical row digests to current
  module bytes.
- The generalized trusted-bootstrap transaction was performed 2026-09-01 and
  keeps state (1) and state (2) distinct: both may carry a valid, exact-scope
  effective human act, only state (2) is independently verified, and an act is
  always a warrant rather than evidence of effect success. It amended the
  accepted 30-module RFC 0001–0009 set, seven signed coverage artifacts and
  CC-SPEC-8, but granted no effect-specific or implementation authority.
- The owner signed the eleven-artifact PWB state-(1) amendment on 2026-09-02.
  PWB-REQ-005 and PWB-REQ-022 now accept valid state (1) or state (2), preserve
  exact state, fail invalid acts closed and keep acts as warrants. The sign-off
  supplies no consent, policy, registry, body-read or implementation authority.

### PWB slice P1 — body-read authority gate (syzygy-1z3.26, 2026-09-03)

- `packages/three-surface-poc-core/src/body-read-authority.ts` is the
  PWB-REQ-005 evaluator: 85 `// mutation-point:` predicate sites (55 common,
  shared by the three authorities, plus 30 authority-specific) carry the 195
  invalid case instances; the first failing predicate names the case, so
  predicate ORDER is load-bearing (false substitutes → binding fields →
  association → provenance → lifecycle → state mechanics → phrase/tag →
  specific fields). Adding a predicate means adding its case to the closed
  vocabulary, the hand-typed table in `body-read-authority.test.ts`, and
  re-running the mutation proof. Scope anchors are matched after collapsing
  whitespace because real act records wrap prose at 80 columns.
- The controlled expectations live only in
  `apps/three-surface-poc/src/governance-inputs.ts`, never read from the
  artifacts. The real-tree test is tag-aware: hosted CI's shallow checkout
  has no `pwb-*-signed-2026-09-02` tags, so every act fails closed on
  `recording-tag-mismatched` there; locally all three acts evaluate as valid
  state (1). State (2) is unreachable (`A1_CORRELATION_UNAVAILABLE`).
- `npm run poc:pwb-mutation-run` is the rule-6 proof: 86 predicate
  disablings + 11 literal mutations, each run against the two independent
  test files with digest-verified restore, evidence at
  `docs/evidence/pwb-mutation-run-<date>.json`. Never run it while editing
  the core sources (it rewrites them in place during the run) and never
  commit while it runs. Vitest test names contain `→`; grep on the `×`
  glyph, not the arrow, to list failures.
- `project-shape-observer.ts` is the registry-named module; its first
  statement is the admits gate. No Butlers body is read anywhere in P1.

### PWB slice P2.1 — revision-bound source manifest (syzygy-1z3.2, 2026-09-03)

- `packages/three-surface-poc-core/src/project-shape-manifest.ts` is phase A
  discovery as a pure function over injected `tree` (parsed `ls-tree -r -z`
  via `git-tree.ts`) and `readSeed`; it reads nothing itself and asks
  `readSeed` only for tree-present blobs among the root index and the five
  pillar READMEs, in `PILLAR_KEYS` order (`manifest.phaseAReads` records
  exactly those). Tree-only rules (baseline specs, roster) never read.
- The population never shrinks: a named-but-absent file is a source with
  anchor `missing-at-revision`, a symlink/submodule is recorded by mode/type
  (the P2.3 reader rejects it), an unreadable index leaves the pillar
  `unknown` with its reason while the index itself stays counted.
- Digest is sha256 over canonical (key-sorted) JSON of every field but
  `digest`; capture instant is deliberately NOT in the manifest (it is the
  observer's stamp, P2.2), so the same revision + indexes give the same
  identity. Constants `PWB_DISCOVERY_VERSION`/`PWB_ROOT_INDEX_PATH` are
  proven byte-equal to the act-bound registry/policy JSON in the test.
- Always take tree listings with `-z`; the parser rejects quoted paths.

### PWB slice P2.2 — injectable phase A observer (syzygy-1z3.3, 2026-09-03)

- `packages/three-surface-poc-core/src/project-shape-observation.ts` wraps
  the manifest with an injected `GitRunner` (`(args) => Uint8Array`, throws
  on failure). Command order is fixed and ledgered: `rev-parse --verify
  <rev>^{commit}` → `show -s --format=%cI` (committer instant = the
  source-claimed instant, kept distinct from the injected `capturedAt`) →
  `ls-tree -r -z -l` → one `cat-file blob <oid>` per admitted seed. Any
  failure before the tree is `gitCaptureFailed` / "Observer failed".
- `admitPhaseARead` is the allowlist and runs before every read: root index
  or a `README.md` whose directory basename is a pillar key, tree-present,
  object id equal to the tree's, mode 100644/100755. Returned bytes must
  hash to the tree's object id (`gitBlobObjectId`), be NUL-free and strict
  UTF-8; over-limit seeds (`maxBytesPerSource`, `maxTotalBytes`) are never
  opened. Refusals leave the pillar `index-unavailable` with the reason as
  `detail`; the population never shrinks.
- `observationDigest` excludes `capturedAt` everywhere (top level and every
  source stamp) so the same inputs at different capture times share a digest.
  `PWB_OBSERVER_IDENTITY`, `PWB_RESOURCE_LIMITS`, `PWB_FAILURE_STATES` and
  `PWB_CONTENT_CLASS` are hard-coded copies proven byte-equal to the
  act-bound registry entry and consent record in the test.
- `gitRunnerFor(repoRoot)` is the production binding; nothing calls it yet.
  The first real Butlers observation stays in P4 behind the P1 gate.

### PWB slice P2.3 — exact Git object reader (syzygy-1z3.4, 2026-09-04)

- `packages/three-surface-poc-core/src/git-object-reader.ts` is the
  PWB-REQ-006 read guard for phase B bodies. `admitExactObjectRead` refuses,
  in order: escaping paths (absolute, NUL, `..` above root), unnormalized
  paths (`.`/`..`/empty segments, trailing slash — the caller must already
  hold the normalized form), the policy's denied basename/prefix/suffix
  rules on the final segment (case-insensitive), not-in-tree, and any entry
  that is not a regular blob (symlink 120000, submodule 160000, tree —
  checked by type *and* mode). Only then does it issue exactly one
  `cat-file blob <oid>`; bytes must hash to the tree's object id, be
  NUL-free, strict UTF-8, and free of active content.
- Active content is a closed seven-form vocabulary scanned over the whole
  body (fences and spans included): html-tag, comment/declaration, script,
  svg, event-handler attribute, unsafe URL scheme at a link/attribute/
  autolink position (javascript/vbscript/data/file, whitespace-tolerant),
  and an HTML entity inside a Markdown link destination. A finding names
  form + line + column, never bytes. Records carry `contentDigest`
  (sha256 of the exact bytes) and never a `text` field; the body reaches
  only the caller's `consume` callback.
- `evaluateLimit(limits, name, observed, path?)` is the shared comparison
  for all six registry limits (`observed <= declared` passes). The reader
  applies maxSources, maxBytesPerSource and maxTotalBytes (declared size
  first; unsized listings are bounded after the read and the bytes
  dropped). `readManifestSources` never shrinks the population: one result
  per manifest source, in manifest order.
- Test spy discipline: the fixture Git runner throws on anything but
  `cat-file blob <40-hex>`, so an escaped request fails loudly. 22 rule-6
  mutations killed (manual python loop, digest-verified restore); the two
  equivalent mutants found were removed as dead code, not waived.

### PWB slice P2.4 — secret policy before admission (syzygy-1z3.5, 2026-09-04)

- `packages/three-surface-poc-core/src/content-classification.ts` runs the
  act-bound policy's six-step `classificationOrder` over the P2.3 reader's
  transient body. The policy is a parameter (`PWB_SECRET_POLICY` is the
  byte-equal default; the test proves it against the JSON); detectors are
  compiled from the policy strings and an uncompilable policy throws.
  Global-flag regexps have `lastIndex` reset before every test — removing
  that reset is a killed mutation, not a nicety.
- Three body-free outcomes: `classified` (text reaches only the consumer
  callback), `excluded` (hash-not-body RFC5-17 record: digest, path, policy
  id/version, `detectorId` or a closed `exclusionReason`, optional closed
  `detail` word) and `unavailable` (missing/non-blob/unreadable; not an
  exclusion; registry reason `source-uncaptured-or-unreachable`). A denied
  path or never-opened over-limit source has no content digest. Over-limit
  is `unclassifiable-excluded` per the policy but carries the registry's
  `Partial snapshot` reason (the two act-bound artifacts differ; recorded in
  the plan's P2.4 note).
- `classifyManifestSources` returns one result per manifest source in order;
  the earlier population guard was removed as unreachable (equivalent
  mutant). 25 rule-6 mutations killed, digest-verified restore, evidence at
  `docs/evidence/pwb-p2-4-classification-mutation-run-2026-09-04.json`.
- The classifier is constructed by nothing before P4; no Butlers body is
  read.

### PWB slice P2.5 — literal item extraction (syzygy-1z3.6, 2026-09-04)

- `packages/three-surface-poc-core/src/project-shape-extraction.ts` is the
  PWB-REQ-002 grammar: `extractSource(source, text)` dispatches each of the
  source's manifest classes to one literal extractor and returns either
  `extracted` (items + per-class denominators) or `unknown` (one closed
  failure reason, class, line, detail). A failing class withholds every
  class's items for that source — never a partial set. Duplicate keys
  within one source are a failure here; cross-source duplicates are 2.6's
  contradictions.
- Parsers are column-0 anchored and fence-masked; heading text is matched
  exactly after NFC (no case folding), so a grammar mismatch against the
  real Butlers tree will surface in P4 as `missing-heading`, not as a
  silently empty set. Expect to widen fixtures, never the matcher, when
  that happens: the grammar is the spec's, not ours.
- The test's oracle is a regex-only extractor written from the spec; both
  must agree on identities and denominators. Test fixtures spell composed
  characters as `\u0301` escapes so NFC is observable — the Write tool
  emitted mixed NFC/NFD bytes for a literal "é", which is why. 35 rule-6
  mutations killed (evidence in `docs/evidence/`); two equivalent mutants
  (an unreachable indented-line guard) were removed as dead code.

### PWB slice P2.6 — coverage and precedence (syzygy-1z3.7, 2026-09-04)

- `packages/three-surface-poc-core/src/project-shape-coverage.ts` turns
  `ClassifiedSource<SourceExtraction>` entries (2.4's population with 2.5's
  `extractSource` as the consumer) into `ProjectShapeCoverage`: sources in
  input order with known/Unknown item denominators, one `ItemCoverage` per
  identity, per-class counts that reconcile to the declared count, and
  reconciled facts. Grammar failures route through
  `parseFailureExclusion`, so the coverage object never carries a body.
- Precedence is data, never heuristics: a `PrecedenceRule` names its
  Butlers anchor, its words and two selectors (`{path}` or `{basis}`). It
  applies only when the anchor is an admitted source and each side matches
  exactly one declaration; anything else is a recorded rejection and the
  fact stays `contradicted-pending-adjudication` with every declaration
  kept. Do not add a default rule, a "newest wins" or "authoritative file"
  fallback — the spec forbids a winner without a Butlers-declared rule.
- Production wiring (2.7) passes no rules and no stated declarations
  until the live run shows Butlers declaring some; the design's
  eight-versus-nine domain-butler conflict is the fixture in the test.
- Mutation-loop gotcha: a mutation that throws during describe-time
  fixture construction reports zero tests, which a naive "any test
  failed" verdict scores as survived. Build fixtures in `beforeAll` (or
  lazily) so crashes are counted failures.

### PWB slice P2.7 — project shape on the one PocModel (syzygy-1z3.8, 2026-09-04)

- `packages/three-surface-poc-core/src/project-shape-model.ts` composes the
  P1 gate → P2.2 observer → phase-B tree re-list at the resolved commit →
  P2.3 reader → P2.4 classifier → P2.5 extractor → P2.6 coverage into one
  `ProjectShape` union (`not-evaluated` / `not-admitted` /
  `observation-failed` / `observed`). `model.ts` puts it on
  `PocModel.projectShape`; `/api/poc` is unchanged (`JSON.stringify` of the
  model), so the machine answer grows by construction. The proving slice's
  `inputsDigest` deliberately excludes it.
- `main.ts` builds the authority from `process.cwd()`'s governance tree
  (`governance-inputs.ts` → `evaluateBodyReadAuthority`) on every model
  build and passes `projectShape: { authority }`; a loader throw becomes
  `projectShapeDetail` and the shape is `not-evaluated`. Tests inject an
  in-memory `runGit`; production uses `gitRunnerFor(repoRoot)`. Hosted CI's
  shallow checkout lacks the signing tags, so there every act fails closed
  and the daemon's shape is `not-admitted` — expected, not a defect.
- Claim tuples reuse cap1-core vocabularies verbatim (three labels, six
  tiers, twelve reasons, four freshness states); `UNKNOWN_REASON_ROUTES` is
  keyed by `UnknownReason` so a vocabulary drift fails typecheck. Observed
  = `report-fact` + `fresh`; contradiction = `suspended`; whole-shape claim
  derives from sources + reconciled facts (not the observer's degradation
  flag, which is data beside it). Item-level contradicted/unknown states are
  unreachable through the grammar — tested at the exported `itemClaim` and
  `countReasons` seams, not by fixture.
- Fixture discipline for this module: pillar READMEs must link only files
  present in the fixture tree, or the population honestly grows by
  named-but-absent Unknown sources; the fixture Git runner throws on any
  `ls-tree` not at the resolved commit and on any `cat-file` it does not
  hold. Item keys follow the P2.5 grammar (`vision:1`, `1:Daemon`,
  `cc-spec.md`, directory name for roster and specs). Mutation evidence:
  `docs/evidence/pwb-p2-7-model-mutation-run-2026-09-04.json` (38/38).

### PWB slice P3.1 — project-level Polaris sequence (syzygy-1z3.9, 2026-09-04)

- `apps/three-surface-poc/src/polaris.ts` opens with seven groups in fixed
  order (`POLARIS_GROUPS`: overview, boundaries, architecture, v1, catalog,
  capability-detail, evidence-and-gaps), each rendered once with
  `data-polaris-group`; the WhatsApp entity sections sit under
  capability-detail behind `data-polaris-capability-scope`. The
  movements/tally scaffolding is gone — do not reintroduce
  `data-polaris-movement` or a hand-written claim tally.
- Unobserved shapes render every project group as Unknown in place
  (`data-polaris-section="shape:<group>"`, `data-unknown-disclosure=
  "claim:project-shape"`, reason + route); an observed shape renders account
  statements (`claim:project-account:<key>`), class blocks
  (`claim:class:<cls>`, `data-polaris-class`), item rows
  (`data-polaris-item`), source rows (`id="polaris-source-<slug>"`),
  exclusions (hash-not-body) and an Unknown-by-reason list
  (`data-polaris-gap`). Every rendered shape claim carries a `claim-tuple`
  span (claim id, label, tier, freshness, evaluation id) that the test
  compares to the JSON machine answer per claim id.
- Surface tests get an `observed` shape from
  `test-project-shape-fixture.ts` (in-memory Git runner over Butlers-shaped
  texts + `ADMITTING_AUTHORITY`/`REJECTING_AUTHORITY`) through
  `buildFixtureModel(cleanups, { projectShape })`; without the option the
  fixture shape stays `not-evaluated`. Do not use `class="epistemic …"` for
  new spans — the cross-cutting legend sweep treats that class as a legend
  entry.
- The model stamps every claim `fresh`, so a renderer mutation hard-coding
  freshness is an equivalent mutant today; the tuple test still binds
  label/tier/evaluation id per claim.
- Task 3.2's guarantee lives in `polaris.test.ts`: the capability slice
  (from `data-polaris-capability-scope` to the evidence group) must be
  byte-identical between an unevaluated and an observed shape, and each
  entity section must carry exactly the model's provenance. Any change that
  makes the slice depend on `projectShape` breaks it by design.
- Task 3.3: every fixed Polaris string is a row of `polaris-copy.ts` with one
  PWB-REQ-012 role; the renderer and the shared shell mark each carrying
  element with `data-copy-role`, and `polaris-copy.test.ts` sweeps the
  rendered text (own extractor, word counter and prohibited set) over five
  fixtures covering all four shape arms. A new fixed string must be a table
  row; a new element carrying model text must declare a role or the sweep
  fails `unclassified`. No group ledes: a group header is one `<h2>` only.
  `data-scope="poc-bound"` may appear once, on the capability scope
  instruction. Rows the fixtures cannot reach are listed by hand in
  `UNREACHED_IN_FIXTURES` — remove an id there when a fixture reaches it.
- Task 3.4: `PocModel.proposedWork` (`proposed-work.ts`) is the followed
  OpenSpec change as its own type — lifecycle from tree paths, current
  authority looked up in `projectShape`'s baseline-spec items. Polaris
  renders it only inside capability detail (after the entities, before the
  relationships, which now live there too), current authority first. Its
  marker ids are `proposed-work:<changeId>` plus `/current-authority` and
  `/lifecycle`; add them to any marker-resolution sweep. Never render it as
  an entity or in a project group — `polaris-proposed-work.test.ts` slices
  the page and fails on any proposed identity outside the detail group.
- Task 3.5: tuples carry `data-epistemic-{label,tier,primary-reason,
  secondary-reasons,freshness}`, `data-challenge-state` and
  `data-evaluation-id`; aggregates render `reasonCountsBlock` (separate
  primary/secondary `<ul data-reason-counts-*>` lists) and coverage counts
  only inside `<details class="coverage-counts">`.
  `polaris-epistemic-tuples.test.ts` hard-codes the vocabularies and a
  status-word regex; when adding page copy, avoid `healthy`, `score`,
  `maturity`, `trend`, `on track`, `at risk` and percentages. Class-level
  Unknown/secondary reasons are unreachable via fixtures, so
  `denominatorText`/`reasonCountsBlock` are exported and tested directly.
- Task 3.6: `roleAttr(copyRole, claimRole?)` now emits `data-claim-role`,
  `data-presentation-artifact` and `data-non-citable` on every copy-role
  element (page-shell/design-tokens carry the literals). An anchored project
  fact must go through `anchoredBlock`/`shapeClaimBlock` in `polaris.ts` so
  the `NarrativeRegistry` (module state for one synchronous render) records
  its claims and anchors and the `<cite>` gets `anchorAttrs`. The oracle in
  `polaris-narrative.test.ts` re-derives every block's anchor set from the
  model — a new anchored site needs its rule added there too, or covering
  fails. Never render `data-claim-provenance` outside an anchored block, and
  never put narrative/anchor/view fields on `PocModel`.
- Task 3.7: `capability-detail.ts` is the data side of the three-band deep
  dive; `polaris.ts` composes it. Every `<section>` inside the dive goes
  through `DeepDiveLedger.block(band, id)` so it carries exactly one
  `data-band` and lands in the machine form's band population — a section
  built without the ledger fails the exhaustion test. Proposals are
  **non-anchored** (no `anchoredBlock`, no `data-anchor-*`, role
  non-normative-framing); the narrative oracle throws if a proposal ever
  registers as an anchored block. Verbatim requirement text comes only from
  `PolarisRenderInputs.verbatim` at render (production passes none — the
  baseline spec is outside the consented class — so the page shows
  `unconsented-source-or-provider` beside the leaf identity); bytes must hash
  to the leaf's `#<object id>` or `sha256:` identity or nothing renders. The
  Unknown markers `<capabilityId>/{current-authority,adoption,
  requirement-text,doctrine,non-goals}` are listed in
  `test-deep-dive-markers.ts` for the marker sweeps. Copy-table rows nested
  inside a `FACT` paragraph must themselves be `project-fact`, or the copy
  test reports them never rendered under their role.
- Task 4.6: `walkthrough-inputs.ts` loads the PWB-REQ-022 pair (run record
  under `records/`, judgment + act record under `decisions/`) with the
  helpers `governance-inputs.ts` now exports; `PWB_WALKTHROUGH_SCHEDULE`
  is the controlled expectation table (serial identities, not dates). The
  run record's `Evaluation identity:` must match `/^[a-z0-9][a-z0-9-]*$/`,
  so the recording session assigns a slug and sets it in the schedule
  when it writes the record — the daemon's `evaluation:…` id is not
  usable there. `main.ts` evaluates the pair every build; absent →
  `absent`/Unknown, loader throw → `not-evaluated`. The real-tree test
  pins "no record yet" and must be re-pinned when one lands. The owner
  packet is `contracts/candidates/pwb-walkthrough/OWNER-WALKTHROUGH-PACKET.md`;
  it quotes no digest, so no act-phrase registration was needed yet —
  register `ADOPT POLARIS COLD-OPEN WALKTHROUGH JUDGMENT` in
  `check_governance.py` before any file quotes it with a digest. Future
  paths in packets go unbackticked (CG-1b resolves backticked paths).
- Task 4.5: `fresh-checkout-demo-main.ts` (`npm run poc:fresh-checkout-demo
  -- --repo <butlers>`) clones `HEAD` with tags into a temp dir, runs
  `npm ci`/`build`/the full Vitest suite (JUnit root tag only), starts the
  clone's own daemon with cwd = clone, fetches the five routes, and checks
  Polaris claim-tuple parity against the machine answer under the 4.3
  presented-population rule (reconciled facts and project-account-section
  items omitted by design). Committed evidence is body-free and carries no
  act digests; the raw route bodies and JUnit file are retained only under
  `~/.local/state/syzygy/pwb-p4-5-fresh-checkout-demo-<date>/` (CG-7e and
  no-egress consent). Live findings from the first run are in the plan's
  P4.5 note: shape `observed`, 256 sources / 134 Unknown (132
  `active-content` exclusions under the act-bound policy, incl. one pillar
  index), 389/389 parity. Those are 5.x review findings, not 4.5 defects.
- Task 4.4: `cdp-browser.ts` drives a locally installed Chrome/Chromium
  headless over the DevTools protocol with Node's global `WebSocket` (no
  dependency, no download; `SYZYGY_POC_BROWSER` overrides the PATH search).
  `polaris-accessibility.ts` is the PWB-REQ-016 oracle: real Tab/Shift+Tab
  traces, real Enter activation of every fragment link, the browser's own
  accessibility tree, and WCAG AA contrast against composited backdrops
  (gradient stops are candidates; the worst wins). `polaris-accessibility.
  browser.test.ts` is `describe.skipIf`-gated — skipped is not passed —
  and `npm run poc:accessibility-check` writes the evidence JSON. Gotchas
  learned from the first run: `Emulation.setFocusEmulationEnabled` is
  required or headless never moves focus; scripted `focus()` + Enter on a
  link whose fragment is already the URL hash is a no-op (no focus start
  point moves), so re-navigate first; after the last focusable, Tab
  lawfully wraps to the browser chrome (`activeElement` null) before the
  first link; `<summary>` is focusable and must be in the `:focus-visible`
  rule (it was not — a real 1.01:1 finding, fixed in `design-tokens.ts`);
  unique landmarks (banner/main/contentinfo) need no accessible name; use a
  fresh page target per variant: in the first run, later variants on a
  reused target stopped receiving Enter/Shift+Tab (cause not isolated; a
  fresh target removed it). Mutation loop is manual
  (`docs/evidence/pwb-p4-4-accessibility-mutation-run-<date>.json`).
- Task 4.3: `polaris-parity-sweep.test.ts` is the exhaustive PWB-REQ-020
  oracle: it parses Polaris back with its own attribute-tolerant extractor
  (boolean attributes such as `data-non-citable` must be allowed, or every
  claim tuple silently extracts as nothing) and compares each marker family
  to the machine answer as a multiset with both denominators, across the
  shape × judgment matrix. Add a new `data-parity-field` and the sweep
  reports it under `<uncovered>` until an expectation names it. Keep leaf
  markers leaf (one text node) — nested markup goes through `containers`,
  not `leafMarkers`. `PocModel.walkthroughJudgment` is `not-evaluated` in
  production until 4.6 supplies a run/judgment pair;
  `test-walkthrough-judgment-fixture.ts` reaches all five judgment states
  (state (2) via an injected correlator). The mutation sweep's
  parity-markers group names matrix cells as must-fail substrings (e.g.
  `observed shape / lawful-state-1 judgment`).
- Task 4.2: `apps/three-surface-poc/src/pwb-mutation-sweep.ts` is the one
  rule-6 plan over the nine named mutation classes; `npm run
  poc:pwb-mutation-sweep` (`--group <id>` / `--only <mutation-id>`) runs it
  and writes `docs/evidence/pwb-p4-2-mutation-sweep-<date>.json`. Adding a
  mutation means an exact fragment that occurs once in its subject plus a
  must-fail test-name substring; `pwb-mutation-sweep.test.ts` rejects
  drift. A killed mutation whose named test did not fail is reported as
  SURVIVED with the actual failing names in the evidence — fix the name,
  or, when nothing failed, strengthen the test (never waive). The full run
  takes ~35 minutes and rewrites subjects in place: run it in the
  background, edit nothing it lists, and never commit while it runs.
- Task 4.1: `packages/three-surface-poc-core/src/walkthrough-judgment.ts`
  is the PWB-REQ-022 evaluator (2 absent + 84 present-invalid cases, one
  `// mutation-point:` per case, predicate order load-bearing: homes →
  run-record fields → judgment fields → the 55 common act predicates
  restated from P1). Run record grammar: backticked `Record identity:`
  (`PWB-WALKTHROUGH-…`), `Surface version:` (`polaris@<v>`), `Evaluation
  identity:`, `Mode:` (`nonvisual-keyboard-only`|`visual-pointer`) and a
  `## Traversed paths` list of backticked routes. Judgment grammar:
  `Verdict:` `` `<criterion>=met|not-met` ``, `Judging party:` (plain, the
  owner), `Run record:` `` `<identity>@<sha256>` `` and a `## Rationale`
  section; its owner act binds the judgment's SHA-256 like the three effect
  acts. Never share the 55 common predicates with `body-read-authority.ts`
  — the duplication keeps the risk floor's act-bound bytes untouched.
  Nothing consumes the evaluator before 4.6.
- Task 3.8: Polaris's depth list, gap-entry ids, contradiction ids and
  named scroll regions are the keyboard/text reachability surface. Link
  targets are page state (`activeTargets` in `polaris.ts`): a reason or
  source path outside the rendered population renders as text, never as a
  link — RFC7-31 makes a dangling internal link a release-blocking floor,
  and `polaris-reachability.test.ts` sweeps every `href="#"` against the id
  population in four shape states. Add a new in-page link only through
  `unknownReasonRef`/`sourceRef` or with a target the same render emits.
  `ProjectShapeModelInput.statedDeclarations`/`rules` exist for tests only
  (the contradiction path); `main.ts` must keep passing neither until a
  live run shows Butlers declaring them. The oracle's `text()` collapses
  tags to spaces, so match `reason ?:`-style, not exact punctuation.

### PWB truth-and-readiness amendment — Decision 1 performed 2026-09-05

- `scripts/record_pwb_truth_amendment.py --record <sha>` wrote
  `decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md` and appended the aggregate
  section; `--check <sha>` regenerates both and diffs. It hard-codes the
  frozen subject, packet head and final-evidence head and binds the presented
  packet bytes to the final owner-packet review's own `[Observed]` lines.
  Its `--check` tolerates later appended aggregate sections (exactly one
  copy of its block, not the tail of the file).
- Decisions 2 and 3 use `scripts/record_pwb_effect_amendment_acts.py
  --record <approve-policy|adopt-registry-entry> <sha> --date <date>`: same
  frozen subject/packet head as Decision 1, the effect manifest instead of
  the behavior manifest, and a **new** dedicated record per act
  (`PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md`,
  `PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`, tag
  `pwb-<act-type>-signed-<date>`). The 2026-09-02 dedicated records are
  never appended to or edited: the implementation's `governance-inputs.ts`
  parses them as one act each, and re-pointing it at the successor records
  is the syzygy-8i7 continuation's work, not the recorder's. Decision 2 was
  performed 2026-09-05.
- `_activate_pwb_effect_amendment_act_copy_registries()` re-registers the
  four frozen `pwb-effect-acts/*` copies and the superseded dedicated record
  as `ACT_HISTORICAL_DIGEST_COPY_FILES` entries pinned at the 2026-09-02
  digest once the amendment record exists, and keeps their other labels
  current. Before that record exists the same files are current copies and
  their CG-7e findings are the intended pre-act state.
- `check_governance.py` now models the PWB behavioral package as a successor
  chain (`PWB_SUCCESSOR_CHAIN`: state-(1) act → truth act). CG-7h binds
  current bytes to the latest validly performed link, preserves earlier links
  as `[historical]`, and fails a later link recorded without its predecessor
  as a chain gap. A third amendment appends one tuple to the chain plus its
  `truth_*`-style injected fixture inputs; do not special-case it elsewhere.
- Until Decision 3 is recorded, CG-7e's 6 findings on the registry-label
  copies are the expected pre-act state on this branch: the candidate
  registry digest in `PWB-EFFECT-AMENDMENT-MANIFEST.txt` is registered as the
  current argument, so every 2026-09-02 registry copy reads stale. Nothing
  else in the battery fails. `record_pwb_state1_amendment.py --check` also
  fails against current bytes by design — it is a superseded act's recorder.

### PWB effect-act packet (task 1.7) — performed 2026-09-02

- The three effect-specific authorities live at their final bytes:
  `decisions/BUTLERS-PROJECT-SHAPE-OBSERVATION-CONSENT.md`,
  `policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`,
  `declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`.
  Each was performed as a **separate state-(1) act whose argument is the
  artifact's own SHA-256** (RFC3-16(b) item 3 binds directly); all three are
  recorded (tags `pwb-<act-type>-signed-2026-09-02`), so those three files
  are now act-bound and may not be edited outside a new act. Task 1.8 was
  closed the same day by the owner's direct "Authorized" reply, recorded at
  `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` with the recorder's
  explicit scope reading — a plain direction, not a digest-bound act, so it
  adds no acceptance-record row and registers nothing in CG-7e. Packet,
  report, manifest and `ACT-SEMANTICS.md` sit in
  `contracts/candidates/pwb-effect-acts/`; `build_pwb_effect_acts_packet.py`
  generates/verifies them and `record_pwb_effect_acts.py --record <act-type>
  <sha> --date <date>` writes the dedicated record plus the aggregate
  section. Both scripts hard-code the frozen subject and packet head; a new
  freeze means editing those constants and re-running the reviews.
- **Never quote a performed act argument (or a truncated digest of a signed
  artifact) inside a new artifact.** CG-7e fails any file carrying a
  recognized act argument that is not in `ACT_DIGEST_COPY_FILES`, and CG-15
  fails a truncated digest that prefixes no current argument or manifest
  entry. Cite the act record by path instead. Also never name a Butlers
  file path in backticks in a packet (CG-1b resolves it as a repo path).
- New act phrases must be registered in `check_governance.py`'s
  `_act_subjects()` and their packet copies in `ACT_DIGEST_COPY_FILES`
  before the packet exists, or CG-7d cannot see them go stale; generated
  files that appear only after `--finalize` are registered from an
  existence-gated activation function, not from import time.
