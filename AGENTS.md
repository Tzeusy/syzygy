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
recovery, or mission authority. On **2026-09-05** the owner signed the
three-act PWB truth-and-policy amendment (behavior package,
secret-classification policy, observer registry entry; consent unchanged;
`decisions/PWB-TRUTH-READINESS-AMENDMENT-ACT.md`,
`decisions/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md`,
`decisions/PWB-OBSERVER-REGISTRY-ENTRY-AMENDMENT-ACT.md`; the 2026-09-02
records stay immutable history) and continued implementation authorization
for that amendment by direct direction
(`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`): the
amended semantics, policy and registry entry are the implementation target;
every 2026-09-02 exclusion is retained.

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
| "May I implement X?" | Capability 1 remains authorized under `decisions/CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md`. The bounded Three-Surface POC and its one Butlers proving slice are additionally authorized by `decisions/THREE-SURFACE-POC-MODE-DIRECTION.md`; the surface-redesign item `syzygy-z2b` is authorized by the signed-off `three-surface-poc-experience` spec (`decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`). The `polaris-project-wide-butlers-model` change is signed, its three effect acts are performed, and its implementation is authorized by `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` and continued for the 2026-09-05 amendment by `decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` (plan: `docs/PWB-IMPLEMENTATION-PLAN.md`; tasks §2–§5 against the 2026-09-05 signed package, one Butlers repository, content class `declared-project-shape-text`, body read only after in-implementation PWB-REQ-005 evaluation of the current consent, policy and registry acts). Anything outside these authorized scopes remains forbidden. |
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
the implementation has evaluated the current three effect acts (the
2026-09-02 consent and the 2026-09-05 policy and registry amendments) under
PWB-REQ-005 (`decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md` and its
2026-09-05 continuation bound the PWB implementation); read any new repository body before
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

Compacted 2026-09-05 (memory-hygiene pass): the previous version of this
section had grown into a slice-by-slice implementation diary (PWB P1–P4.6,
Three-Surface POC internals, etc.) that was mostly re-derivable from git log
or the code itself, plus facts already covered by the governance narrative
above or by `bd memories`. Three facts now live only in `bd memories`
(loaded automatically via `bd prime`, do not re-add here): Capability 1
implementation status, the FROZEN-files rule, and the tailscale
`--set-path` mount-prefix finding.

### Architecture (durable)

- `packages/cap1-core/src/`: 14 pure domain modules (zero I/O/clock/side
  effects), re-exported via `index.ts`. Conformance tests: one file per
  CAP1-REQ-NNN in `packages/cap1-conformance/src/`. Closed vocabularies as
  `as const` tuples; branded ID types; discriminated-union results. Parity
  by construction: one `FactModel`, `serveMachine`/`renderHuman` both read
  from it, an independent oracle compares channel outputs.
- Three-Surface POC: `packages/three-surface-poc-core/` (one shared
  `PocModel`) + `apps/three-surface-poc/` (SSR pages + `GET /api/poc`), both
  reading the same model instance — never split surface truth stores.
  `npm ci && npm run poc -- --repo <butlers>` is the fresh-checkout command.
  `build:poc` must keep `tsc -b --force`: ignored incremental outputs are
  executable inputs, so a normal up-to-date check isn't a safe trust boundary.
- PWB (Butlers project-shape reading) pipeline, in order, each stage pure
  and injectable: **P1** `body-read-authority.ts` gates every read (no
  Butlers body may be read before this evaluates true) → **P2.2**
  `project-shape-observation.ts` (injectable `GitRunner`, fixed command
  order) → **P2.3** `git-object-reader.ts` (path/type allowlist, hash
  verification against the tree, active-content scan) → **P2.4**
  `content-classification.ts` (policy-driven; produces hash-not-body
  records, never raw text, for excluded content) → **P2.5**
  `project-shape-extraction.ts` (literal grammar over classified text) →
  **P2.6** `project-shape-coverage.ts` (precedence only via a
  Butlers-declared `PrecedenceRule` — never a "newest wins" or
  "authoritative file" default) → **P2.7** composes all of it into
  `PocModel.projectShape`. Production binds the observer via
  `gitRunnerFor(repoRoot)`; a live Butlers body read is authorized only
  behind the P1 gate. Which owner acts/consents unlock which stage is
  governed content — read the file's main body above, not this section.
- Governance/contract-amendment state (which acts are performed, state (1)
  vs (2), etc.) is narrated once in this file's main body — do not restate
  it here; it will drift out of sync.

### Recurring gotchas (guardrails — keep even when old)

- **Worktree builds**: a fresh `git worktree` has no local `node_modules`.
  With no `paths` mapping in `tsconfig.base.json`, `NodeNext` resolution for
  `@syzygy/*` silently walks up to the *main* checkout's symlinks instead of
  the worktree's edits — no error, just confusing "property does not exist"
  failures. Run `npm ci` inside the worktree first.
- `git ls-tree` must be run with `-z` — without it the parser breaks on
  quoted paths.
- The mutation-check tooling (`npm run poc:pwb-*-mutation-*`) rewrites
  source files in place while running (the full sweep takes ~35 min): never
  edit those files or commit while it's running.
- CDP/headless-browser testing: `Emulation.setFocusEmulationEnabled` is
  required or headless never moves focus; re-navigate before Tab/Enter if
  the target fragment already matches the URL hash (otherwise a no-op);
  Tab lawfully wraps to the browser chrome after the last focusable element;
  `<summary>` is focusable and needs its own `:focus-visible` rule.
- The Write tool has emitted mixed NFC/NFD bytes for composed characters
  (e.g. an accented letter) — use explicit Unicode escapes in fixtures when
  NFC-exact matching matters.
- A mutation that throws during describe-time fixture construction reports
  zero tests, which a naive "any test failed" verdict scores as survived —
  build fixtures in `beforeAll` so crashes count as failures.
- Fail-closed polarity: withdrawal defeats grant (consent); future-dated
  evidence fails to stale; no evidence → Unknown, never green.
- Oracle independence: conformance-test expected values are hard-coded
  literals, never imported from the vocabulary modules they check.
- Rule-6 mutation check: temporarily break the fix, confirm the falsifier
  test fails, then restore — proves the test can actually catch the defect.
- No-build Vitest seam: root `test.projects` must alias both
  `@syzygy/cap1-core` and `@syzygy/cap1-daemon` to source — built `dist/`
  output can mask a missing alias; verify after `npm ci` with every
  project's `dist/` absent.
- Butlers' pytest suite needs its own venv interpreter
  (`.venv/bin/python`, not bare `python3`) or collection fails.
- Never wire `WORKER_CHANGE_SEAM` test-artifact evidence
  (`whatsapp_user_client.py`) into the unrelated `evidence:focused-pytest`/
  identity-resolution entities in `model.ts` — it renders a false "Verified"
  claim against code the captured test never touches. (Made and reverted
  once already.)
- Never quote a performed governance act's argument or a truncated digest
  of a signed artifact inside a new artifact unless it's in
  `ACT_DIGEST_COPY_FILES` — CG-7e/CG-15 fail it. Cite the act record by
  path instead. Never name a Butlers file path in backticks in a packet
  (CG-1b resolves it as a repo path).
- `authorizeWrite` uses raw `startsWith` for path containment — traversal
  like `openspec/../README.md` currently passes; callers must normalize
  first (tracked, not yet fixed).

### Open/known gaps

- syzygy-ydr: non-blocking S2/S5 review findings still outstanding
  (consent-reference resolution, admissibility bar, grant-state rendering
  citations, unreachable-vs-observer-failure split).
- Butlers-side data quirks affecting PWB extraction as of `a3dd1fe`: `v1.md`
  is whole-source Unknown (one catalog row uses a colon after its bold
  label, outside the signed dash grammar) and Lay and Land's index is
  excluded (its dependent denominator stays Unknown). Don't relax the
  extraction grammar to paper over either without an owner gate.

### Governance recorders (PWB amendment acts, 2026-09-05)

- Digest-bound owner acts are recorded by dedicated recorder scripts that
  hard-code the frozen subject / packet head, validate the owner's argument
  against current bytes, write a dedicated record, append an aggregate
  section to `ACCEPTANCE-ACT-RECORD.md`, and offer `--check`/`--selftest`:
  `scripts/record_pwb_truth_amendment.py` (Decision 1) and
  `scripts/record_pwb_effect_amendment_acts.py --record
  <approve-policy|adopt-registry-entry> <sha> --date <date>` (Decisions 2/3).
  `--check` must tolerate later appended aggregate sections (count exactly
  one copy of its block, never assume it is the file tail). Superseded acts'
  recorders (`record_pwb_effect_acts.py`, `record_pwb_state1_amendment.py`)
  fail `--check` against current bytes by design.
- A superseding act gets a **new** dedicated record; never append to or edit
  the superseded record (`governance-inputs.ts` parses the 2026-09-02
  records as one act each; re-pointing it at successor records is
  implementation work). `check_governance.py`'s existence-gated
  `_activate_pwb_effect_amendment_act_copy_registries()` moves the
  superseded copies into `ACT_HISTORICAL_DIGEST_COPY_FILES` (exact act-time
  quotation line pinned) once the amendment record exists; before that,
  their CG-7e findings are the intended pre-act state.
- New act phrases must be registered in `_act_subjects()` and their packet
  copies in `ACT_DIGEST_COPY_FILES` before the packet exists, or CG-7d
  cannot see them go stale; files that appear only after an act are
  registered from an existence-gated activation function, not at import.
- Plain owner directions (implementation authorization and its
  continuation) are recorded verbatim with a labeled recorder reading; they
  bind no digest, add no acceptance-record row and register nothing in
  CG-7e.
