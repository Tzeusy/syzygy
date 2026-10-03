# Gap analysis — "Please generate me a Polaris dossier for https://github.com/redis/redis"

Research note, read-only, 2026-10-03, Syzygy `main` at `ef5d5f03`. Binds nothing; not
authority. Labels per AGENTS.md. Paths are repo-relative. PR #215 files are read
from `origin/polaris/public-repo-admission` (head `c758d80e`).

## 0. Bottom line

- [Observed] The generator **engine skeleton exists and is real code**: six stages, one
  envelope per stage, durable receipts, budgets, cancellation, a strict-CSP static
  preview. It has **never called a model**: `scriptedGenerate` is the only `generate`
  port, and no provider SDK is imported anywhere in `apps/`, `packages/` or `scripts/`
  (`git grep -i 'agent-sdk|claude-agent|messages.create|api.anthropic'` → 0 hits).
- [Observed] It has **never read a non-Syzygy repo**. The only real-input reader is the
  self-corpus. It is pinned to `project:syzygy` and the `.syzygy/governance/**` Markdown
  roots (`apps/three-surface-poc/src/polaris-generation/self-corpus.ts:14-22,65`).
- [Observed] The governance path for public repositories is **drafted but not in force**.
  The owner answered Q1–Q7 on 2026-10-03 (decisions/PUBLIC-REPO-ADMISSION-OWNER-ANSWERS-2026-10-03.md (on PR #215's branch)
  on the PR branch). The package's round-4 repair is unreviewed, and no act exists. Redis
  is not yet an instance: only T1 = psf/requests is filled.
- [Inferred] The distance to the owner's sentence has three parts:
  - **(i) engine work** that is self-drivable under the 2026-09-12 implementation act:
    any-repo reader, chunking, hierarchical discovery, an Agent SDK adapter, consent-backed
    ports, a dossier profile, and multi-page output;
  - **(ii) one owner sitting** of about six acts plus two rulings;
  - **(iii) one spec-fit problem**. As adopted, the spec renders a non-governed
    project's capability catalog "predominantly Unknown". It is silent on "end-to-end
    workflows" and "competitive advantages".
- [Inferred] **"Simply declare" cannot mean zero ceremony.** SEC-2 is doctrine and
  requires "explicit, recorded, **per-project** consent" (`.syzygy/governance/doctrine/security.md:42-45`).
  The AGENTS.md hard prohibition requires per-repository consent plus registry and policy
  acts. The lawful floor is one option-selection per new target (Q5 form). Section 7
  proposes a standing ruling that shrinks it to "the sentence plus one click".

## 1. What exists for generation

### 1.1 Code

| Piece | Where | What it does today |
|---|---|---|
| Stage prompts | `packages/polaris-generation-core/src/prompts.ts:1-32` | [Observed] Six project-neutral system prompts (inventory, plan, author, edit, fidelity, repair). v2 adds tree form and the diagram criterion (`:27`). They forbid browsing and tools (`:4`). |
| Pipeline | `packages/polaris-generation-core/src/pipeline.ts:174-410` | [Observed] `runGenerationPipeline`: verifySources → admit/permitted/generate/validate/record per stage, with budget fields `maxCalls/maxInputBytes/maxOutputBytes/maxUsageUnits/maxElapsedMs/maxRepairCycles` (`:7-15`). It refuses a population of **0 or >200 quotable sources** (`:236`). The inventory envelope carries **all admitted bodies in one call** (`:238`); later stages get cited spans only (`:239-251`). |
| Source model | `packages/polaris-generation-core/src/generation-source.ts:7-21,89` | [Observed] A Git-observation-typed source with spans. A body over `SOURCE_TEXT_MAX_LENGTH` = 100,000 chars (`provider-draft.ts:25`) throws `source-too-long` and fails validation of the whole population. |
| Draft schema/validation | `packages/polaris-generation-core/src/provider-draft.ts` (401 lines), `admitted-input.ts`, `canonical-json.ts`, `parse-json.ts` | [Observed] Closed response schemas, bounded JSON, canonical digests. |
| Rendered-design check | `packages/polaris-generation-core/src/rendered-design.ts` | [Observed] Mechanical rendered-review seam. |
| Self-corpus reader | `apps/.../polaris-generation/self-corpus.ts:40-75` | [Observed] Reads only Syzygy governance `.md` at a pinned commit. Runs **scripted** stages (`:80,137`) and records `realProviderCalls: 0, networkCalls: 0, realProjectProof: false` (`:183`). |
| Synthetic demo | `pipeline-demo.ts`, `pipeline-demo-main.ts:8-24` | [Observed] Three synthetic projects plus a changed-source case. Writes `<id>.html` + `.json` + `report.json` to `--out` and declares `realProvider: false`. |
| Durable lifecycle | `durable-lifecycle.ts:7-8,50-95` | [Observed] A file journal (reserve/complete/uncertain/release) with replay refusal. Self-described as "private, synthetic-only … no network client or provider is installed". |
| Preview renderer | `draft-preview.ts:28,119` | [Observed] A single static HTML page with CSP `default-src 'none'`, an epistemic legend, inert SVG diagrams (`svg-inert.ts`) and layout (`diagram-layout.ts`). It is not served by any route: a sweep of `apps/three-surface-poc/src/*.ts` (outside `polaris-generation/`) finds `polaris-generation` imported only by 3 test files. |
| PWB adapter | `source-adapter.ts:11-36` | [Observed] Projects the Butlers PWB population into `GenerationSource`s without re-reading. |
| npm | `package.json:26-28` | [Observed] `test:polaris-generation`, `poc:generator-demo` (synthetic), `poc:generation-mutation-run`. No `poc:generate`/real-run script. |

### 1.2 Kit and tracker

- [Observed] `docs/polaris-generation/README.md` (228 lines) is candidate guidance: the run
  contract, six passes, and the portability proof. It says outright that "The current
  operator path calls no real model or provider."
- [Observed] `docs/polaris-generation/TARGETS.md` names the three targets:
  - **T1** requests @ `v2.34.2`;
  - **T2** Redis @ `8.10.2` (commit pinned in TARGETS.md), plus the licence trio `7.2.4`/`7.4.0`/`8.0.0`
    as the changed-source proof;
  - **T3** Sentry.

  The page itself says every target is unread.
- [Observed] `docs/polaris-generation/TRACKER.md` already lists the engine gaps G1–G5
  (any-repo CLI, real `generate` port, consent-backed ports, discovery under budget,
  evaluation harness) under Phase 1. Its Phase 3 is the Redis phase.

### 1.3 Evidence of real runs

- [Observed] **None.** Sweep: every file under `docs/evidence/` (239) plus
  `docs/polaris-generation/`, for the keys `realProviderCalls|providerCallPerformed|networkCalls`.
  - 3 files carry the keys, and each value is 0 or false: `polaris-m7-synthetic-successor-2026-09-23.json:80-81`,
    `example.json:3` and the kit README.
  - No file records a positive value.
- [Observed] The generator evidence that does exist is synthetic, mutation or coverage
  evidence: `polaris-generator-*-2026-09-12/23.json`, `polaris-generation-core-mutation-run-2026-09-23.json`
  and the M6/M7 funnels.

**What a run does today.** [Observed] There are two possible inputs:

- synthetic fixtures;
- Syzygy's own governance Markdown at a pinned commit.

Scripted responders stand in for the model, and the run produces a static draft HTML and
JSON stage receipts. No run has used Butlers through the generator. The Butlers `/polaris`
page is the separate, deterministic PWB renderer, not generated prose.

## 2. Governing specs versus the owner's content model

**Status.** [Observed] The adoption acts are:

- the base spec, `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`
  (REQ-001…029), adopted 2026-09-12
  (`decisions/POLARIS-GENERATOR-SPECIFICATION-ADOPTION-ACT.md`);
- the understanding amendment (overlay on REQ-002/004/006/009/012/014/019, adds 030/031),
  adopted 2026-09-13 (`decisions/POLARIS-UNDERSTANDING-SPECIFICATION-ADOPTION-ACT.md`);
- the tree-form/diagram amendment to REQ-004, adopted 2026-09-28
  (`decisions/POLARIS-TREE-FORM-AMENDMENT-ADOPTION.md`).

PROJECT-STATUS.md:30-62 routes to all three. The implementation authorization
(`decisions/POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md:42`) covers the full
EXECUTION-PHASES goal, but "Real-project reads, provider egress and destination writes
remain separately admitted".

| Owner wants | Spec coverage | Verdict |
|---|---|---|
| Core ideas | REQ-002 (amend `:9`): purpose, beneficiary, proposition, thesis, essential concepts, terminology. REQ-004 (amend `:78`): the opening depth must answer "purpose and central thesis". | **Covered** [Observed] |
| Underlying mechanisms | REQ-004: a component deep dive explains "purpose, responsibility, neighboring interactions and limits". REQ-002 amend: "component responsibilities and relationships". Diagrams for flow/lifecycle/state machine/boundary/dependency. | **Covered** [Observed] |
| Trade-offs | REQ-002 amend: "choices and alternatives, trade-offs, limits"; the "Distinctive argument" scenario (base `:62-66`) must preserve trade-offs. Prompts carry it (`prompts.ts:6,15`). | **Covered** [Observed] |
| End-to-end workflows | Sweep of both spec files for "workflow": base 5, amend 3 hits, **all about the generator's own workflow**. "end-to-end": 0/0. A product workflow is reachable only as a "flow/lifecycle" diagram that the rendered-design review enumerates (REQ-004 amend). | **Silent** [Observed]. Expressible as operator **reader questions / requested assets**: REQ-004 makes a requested asset required, with a produced/omitted/unresolved disposition [Inferred]. |
| Competitive advantages | "competit", "advantage", "benchmark", "performance", "marketing", "website": **0 hits in both files**. REQ-002 forbids unsupported motive or claims. The prompts forbid browsing (`prompts.ts:4`). | **Silent, and effectively constrained** [Inferred]. An advantage is sayable only where an admitted source states it, e.g. redis docs "sub-millisecond". Comparisons with named competitors need admitted competitor sources, which no consent covers, so they render omitted or Unknown. |
| A guided end-to-end tour | RFC7-13 V0 order: thesis → architecture story → capability catalog → deep dive → verbatim leaf (`contracts/rfcs/RFC-0007/narrative-contract.md:316-321`). Usable "unless the owner rules otherwise". | Covered in shape [Observed] |

**Spec-fit problems for a non-governed repository.** None of these is a prohibition
conflict; each is a fit gap.

1. **Capability catalog.** "Catalog membership SHALL come from declared capabilities"
   (REQ-004). Scenario base `:228-232`: "the model cannot invent a declared capability
   from code, and a predominantly Unknown catalog remains a normal honest presentation."
   [Inferred] For Redis, which has no Syzygy capability declarations, the catalog band is
   mostly Unknown unless an owner ruling or amendment defines what a non-governed
   project's "declaration" is. Candidates: maintainer docs, `src/commands/*.json`
   [Unknown whether these exist at 8.10.2, which is unread].
2. **Deep-dive bands.** These are RFC7-17's argument/contract/reality bands, with SDR-3
   mapping classes and adoption history. [Inferred] For Redis they are empty, so each
   deep dive carries "honest absence lines": noise for this reader.
3. **Verbatim leaf.** RFC7-14 renders "verbatim from `openspec/**`"
   (`narrative-contract.md:323-327`). Redis has no `openspec/`. [Inferred] It needs a
   ruling that the exact-source leaf is the admitted source span.
4. **Fixed entry.** REQ-023 places the narrative at `.syzygy/intent/OVERVIEW.md`. It does
   not apply to an observed public repo. The page is a draft, never published (Q6).
5. **"Dossier"** appears 0 times in either spec. The adopted term is "manifesto" or
   "editorial draft".
6. **No human-only interaction.** [Observed] REQ-031 lets a run leave questions
   Unknown or deferred. "An unsupported central thesis SHALL require clarification or
   remain explicitly unestablished", so a zero-interaction run is lawful but may carry
   Unknowns.
7. **Completion.** [Observed] REQ-014 completion needs two real projects plus
   changed-source regeneration and independent cold readers. That is not needed to
   *produce* a Redis page, but it is the bar for calling the generator done.

## 3. Authority gates for an arbitrary public repository

| Gate | Requirement | State for redis/redis |
|---|---|---|
| Observation consent per (observing project, repository) | SEC-2; RFC5-12; REQ-025 (base `:1400`) | [Observed] Template plus the requests instance only (instances/requests/OBSERVATION-CONSENT.md (on PR #215's branch)). **No Redis instance.** It would cover the snapshot objects of the listed revisions, shallow by commit, no execution, no writes. |
| Source-acquisition registry entry | REQ-017; RFC4-1/4-2 fields (`ADAPTER-DECLARATIONS.md:32-44`) | [Observed] Not drafted: "Drafted with the first implementation that reads it" (packet item 5). Per-target or one shared Git-hosting adapter is undecided [Inferred, as the packet labels it]. |
| Screening / secret / classification policy | REQ-025: screened "under the observing project's secret policy"; RFC5-14/5-16 | [Observed] There is a template only, templates/PUBLIC-SOURCE-POLICY-SCOPE-TEMPLATE.md (on PR #215's branch), extending `policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json`. The packet says the current active-content rule "would withhold any source file containing a `<tag`-shaped string" [Inferred: every C file with `#include <…>`]. It also sets `rawBodyHandling: never` for external egress. **This is a real policy change.** PR #120 patches the same file, so whichever lands second is re-drafted. |
| Content classes | RFC5-14's closed vocabulary | [Observed] Q2 answer: all but `work-history`. **Q7:** README, guides and LICENSE fit no class, so their egress is refused. Answer: amend RFC-0005 to add `project-documentation`, with its own act; **not drafted** (TRACKER Phase 0 open). For Redis this blocks `README.md`, LICENSE and likely the commented `redis.conf` [Unknown class]. |
| Provider egress consent | SEC-2; RFC5-12 "one record per (Project, provider)"; RFC5-15 single egress check + audit | [Observed] Instance `EGRESS-CONSENT-ANTHROPIC.md` v`0.1.0-candidate.6`. Subject `(project:syzygy, provider:anthropic)`, scope **psf-requests only**. Redis needs a new version. Conditions: **the route invokes no tools**, loads no CLAUDE.md, memory, MCP or settings, uses an empty cwd, turns telemetry off, and is accepted only when a captured request shows nothing but the generator's bytes. Retention is the run directory, outside git. |
| Provider execution route registry entry | REQ-017; RFC4-1 | [Observed] Not drafted (packet item 2). |
| Generator implementation authorization | `POLARIS-GENERATOR-IMPLEMENTATION-AUTHORIZATION-ACT.md:42` | [Observed] **In force.** Covers all the code below. Grants no read, egress or write. |
| Understanding/tree-form adoption | Acts above | [Observed] In force. Spec adoption only. |
| Self-reading exception | P-76 Q2 (`decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:62`) | [Observed] Syzygy reading its own tree needs no consent. This does **not** extend to Redis. |
| Draft serving route | PWB machine-view amendment, signed 2026-10-02 (`decisions/PWB-MACHINE-VIEW-AMENDMENT-ACT.md`) | [Observed] `GET /polaris/draft/<runId>` is spec'd (`openspec/changes/polaris-project-wide-butlers-model/specs/.../spec.md:1853-1862`) as **machine-credentialed only**, carrying no project-shape facts. Not implemented (sweep: `grep -rn polaris/draft apps --include=*.ts` → 0). |

**PR #215.** [Observed] It is a draft, rounds 1–4 each returned REVISE (4, 2, 1, 1
blocking), and the round-4 repair is unreviewed. The owner's answers:

| Question | Answer |
|---|---|
| Q1 | Anthropic **via Claude Code / Agent SDK** (not direct API) |
| Q2 | All classes but `work-history` |
| Q3 | Run directory outside git |
| Q4 | `project:syzygy` observes each target |
| Q5 | One option-selection per target at manifest rows, state (1) |
| Q6 | Local only, editorial draft: a static file now, `/polaris/draft/<runId>` later |
| Q7 | Amend RFC5-14; T1 runs without |

[Observed] Still open before any offering:

- the confirming review;
- the package manifest;
- the recorder;
- the `check_governance.py` registration (`_act_subjects`, `ACT_DIGEST_COPY_FILES`).

**Pending queue.** [Observed] `decisions/PENDING-OWNER-DECISIONS.md` has no open row
that names generation egress or public admission. Sweep: the `^| P-` rows; the
generation-related rows P-71/72/73/76 are ruled in the P-68…P-83 decision. The
admission questions live in the PR #215 packet and were answered by direction.

**Beads.** Sweep: `.beads/issues.jsonl`, 370 lines = 370 beads. The predicate is title
`/generat|egress|admission|provider|dossier|manifesto|TARGETS|public-repo|redis|requests/i`
**or** any field containing `syzygy-mea`, which gives 29 hits. The open or in-progress
ones that matter:

| Bead | Status | Scope |
|---|---|---|
| `syzygy-mea` (P1) | in progress | Umbrella. Its acceptance criteria include two real projects and changed-source regeneration. The tracker points here. |
| `syzygy-dov.7` / `dov.7.2` | in progress / open | M7 generation loop; slice 4 is the generation route, a pure drafter with no file write, "blocked on the machine-view delta and registry act". The delta is now signed (2026-10-02); the registry act is [Unknown] whether performed. |
| `syzygy-u05.13` | open | Claim-ledger intermediate, frozen case corpus, evaluation runner, quickstart (≈ G5). |
| `syzygy-u05.6` | open | Typed effect authority / boundary register (fits G3). |
| `syzygy-dov.6` | in progress | Generator honesty contract and kit onramp. |
| `syzygy-dov.16` | open | Renderer and visual system. |
| `syzygy-dov.23` | open | CC-REV-2 scenario for the edit-stage deletion. |

[Observed] No bead covers any of the following; the TRACKER.md checklist is their only home:

- the Agent SDK adapter;
- the any-repo reader;
- chunking;
- hierarchical discovery;
- the Redis admission;
- the RFC5-14 amendment.

The owner chose markdown tracking on 2026-10-03.

## 4. The surface

- [Observed] The daemon's `/polaris` serves **only Butlers**.
  `PWB_APPROVED_REPOSITORY_LOCATOR = '/home/tze/GitHub/butlers'` (`apps/three-surface-poc/src/git-observation.ts:6`),
  and any other realpath is `locator-mismatched` (`:43`). There is no per-project or
  multi-project route; the routes are built in `routes.ts:199-298` around one `PocModel`.
- [Observed] Ceilings live in `packages/three-surface-poc-core/src/project-shape-observation.ts:75-83`:
  `maxHumanResponseBytes` 2,097,152 and `maxMachineResponseBytes` 8,388,608. A breach
  serves a 503 and nothing else (AGENTS.md notes). `/polaris` for Butlers already sits
  near the ceiling (P-63 trim).
- [Inferred] **The realistic surface for Redis now is the static file** written by the
  generator into the run directory and opened locally (Q6). It is not bound by the daemon
  ceiling.
  - `renderDraftPreview` emits **one page** (`draft-preview.ts:119`). A Redis dossier
    with diagrams and deep dives may get large, and deep dives as separate pages need
    renderer work.
  - The tracker's "reader-facing performance budget" is an open owner question that
    needs a CC-REV-2 amendment.
- [Inferred] The later route, `/polaris/draft/<runId>`, is machine-credentialed only. A
  human browser read through the daemon therefore needs either that credential or a later
  amendment adding a human-open member. Under the membership clause, a route with "a byte
  ceiling of its own" may not be served before the registry declares that ceiling.

## 5. Scale

| Budget | Value | Where | Redis fit |
|---|---|---|---|
| Quotable sources per run | ≤200 | `pipeline.ts:236` | [Inferred] Redis has ~1.5–3k tracked files: `src/`, `tests/` (Tcl), `deps/` vendored jemalloc/lua/hiredis, `modules/`. Exact count [Unknown: unread]. **Does not fit** without ranked selection plus `deferred-by-budget` accounting (REQ-030; TRACKER G4). |
| Chars per source | ≤100,000 | `provider-draft.ts:25`; `generation-source.ts:89` | [Inferred] Several core `.c` files likely exceed this (`server.c`, `module.c`, `cluster_legacy.c` from general knowledge). **One oversize file fails the whole population.** Needs span chunking or per-file exclusion with a reason. |
| Inventory call | All admitted bodies in one envelope | `pipeline.ts:238`; `generation-source.ts:19-20` | [Inferred] Multi-MB C source cannot go in one call. Needs **hierarchical discovery**: map calls over subsystems → claim ledger → reduce. This is the main design change, and the one that makes a "1–2 h of Opus" budget useful. |
| `maxCalls` etc. | Caller-supplied; demos use 7 | `self-corpus.ts:132`; `pipeline-demo.ts:87` | [Inferred] One call per stage. A 1–2 h budget implies roughly 50–300 calls, so stage fan-out is required. |
| PWB reader ledger | `maxSources` 512, 1 MiB per source, 16 MiB total, depth 4 | `project-shape-observation.ts:75-83` | Butlers registry envelope; does not govern the generator. [Inferred] The source-acquisition registry entry for Redis must declare its own envelope. |
| Model context / rate limits | — | — | [Unknown] Opus 5.5 context window and subscription rate limits under the Agent SDK. Also [Unknown] whether the SDK on a subscription login can meet the egress record's "no tools, no context, telemetry off, captured request" conditions. The owner direction itself marks transcript persistence [Unknown]. |

**Content class per Redis area** [Inferred]:

| Area | Class |
|---|---|
| `src/**`, `tests/**` | `code-content` |
| Tree paths | `code-structure` |
| `README.md`, `LICENSE*`, guides | no class until the RFC5-14 amendment |
| `redis.conf` | [Unknown] class |

[Inferred] The product docs and the competitive positioning live on redis.io and in a
separate docs repository, outside `redis/redis`. Admitting it is a separate observation
consent plus registry entry; the project boundary is an owner choice under REQ-030. A
website is not a Git snapshot, so no adapter exists for it.

## 6. Gap list

Classes: **A** = self-drivable now · **A-d** = agent drafts, owner sign-off binds ·
**B** = owner act or ruling · **C** = external. Sizes: S ≤1 day, M 1–3 days, L 1–2 weeks
(agent time).

| # | Missing | Files / specs | Class | Beads | Size |
|---|---|---|---|---|---|
| 1 | **Any-repo source reader.** `--repo/--revision/--repositoryId`, include/exclude globs, Git-object reads at pinned commits, fetch shallow by commit into a run directory. | `self-corpus.ts` → new `repo-corpus.ts`; REQ-025/030 | A (code). Running it on Redis needs #12–#14 | `syzygy-mea`; TRACKER G1 | M |
| 2 | **Oversize handling.** Span chunking of bodies >100k chars, or a reasoned exclusion; never whole-run failure. | `generation-source.ts:89`, `provider-draft.ts:25`, `admitted-input.ts:106` | A | — | S |
| 3 | **Hierarchical, budgeted discovery** (REQ-030): ranked selection, `deferred-by-budget` accounting, map/reduce inventory into a claim ledger, stopping reason. | `pipeline.ts` (stage fan-out), `prompts.ts` (new discover/map prompts, versioned) | A | `u05.13` (ledger); TRACKER G4 | L |
| 4 | **Agent SDK `generate` adapter.** Structured output, usage, abort. No tools, settings, memory, MCP or telemetry; empty cwd; state in the run directory. Acceptance test against a **local capture endpoint** (base-URL override) so no byte leaves before consent. | new `provider-agent-sdk.ts`; REQ-017; egress record conditions | A (code + capture test). First real call needs B #13 | TRACKER G2 | M |
| 5 | **Consent-backed ports**: `permissionIdentity/admit/permitted` read effective act records; single egress check emits an RFC5-15 audit record; fail closed to Unknown `unconsented-source-or-provider`. | pipeline ports; `durable-lifecycle.ts` (generalize the synthetic-only journal) | A | `u05.6`; TRACKER G3 | M |
| 6 | **Public-source screening implementation**: apply the public scope (active-content and raw-body handling for public code) before admission; hash-not-body exclusions. | PWB screening modules; REQ-025 | A after policy act #12 | — | M |
| 7 | **Dossier run profile**: reader questions = the owner's five (core ideas, end-to-end workflows, mechanisms, advantages-as-stated, trade-offs) plus requested assets (workflow diagrams, component deep dives); zero-interaction REQ-031 mode (defer to Unknown). | config file; REQ-004 requested assets; REQ-031 | A | — | S |
| 8 | **Multi-page static output**: entry page plus a deep-dive page per component, contents/glossary, size report (bytes and words per depth). Written to the run directory, labelled non-release editorial draft. | `draft-preview.ts`, `pipeline-demo-main.ts` pattern | A | `dov.16` | M |
| 9 | **Orchestrator / one-line trigger**: a skill or CLI `poc:dossier <github-url>` that resolves and pins the tag/commit via `ls-remote`, generates the per-target instances (build_public_repo_admission.py), shows the one-question sitting, then runs and reports the file path. | new script and skill; PR #215 builder | A (code); each new target still B | — | M |
| 10 | **Evaluation harness**: frozen reader questions, fresh-context reader answers, fidelity review, reader-cost. Needed to *judge* the page, not to produce it. | REQ-006/014; `u05.13` | A | `u05.13`; TRACKER G5 | M–L |
| 11 | **PR #215 to offerable**: confirming review of the round-4 repair; manifest; recorder; `check_governance.py` phrase and copy registration; Redis instances (observation consent for redis/redis @ `8.10.2`, optionally the licence trio and the docs repo; egress v-next listing requests + Redis). | `contracts/candidates/public-repo-admission/**`, scripts/build_public_repo_admission.py, `scripts/check_governance.py` | A-d | `syzygy-mea` | M |
| 12 | **Public-source screening scope** instance (policy extension), reconciled with PR #120. | `policies/POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE.json` + template | A-d → **B** act | — | M |
| 13 | **Egress consent** (Anthropic via Agent SDK) covering requests + Redis. | PR #215 instance | A-d → **B** act | — | S |
| 14 | **Observation consent(s)** for redis/redis (and requests; optionally the Redis docs repo). | PR #215 instances | A-d → **B** acts | — | S |
| 15 | **Registry entries**: provider execution route; source acquisition (one shared Git-hosting adapter is recommended). | REQ-017; `ADAPTER-DECLARATIONS.md:32+` | A-d (with #1/#4) → **B** acts | — | M |
| 16 | **RFC5-14 `project-documentation` class** (README, guides, LICENSE). An accepted-contract amendment with its own ceremony. | `contracts/rfcs/RFC-0005/**` + candidate mirror; NORMATIVE-CHANGE-WORKFLOW | A-d → **B** (contract amendment act) | — | M (plus review rounds) |
| 17 | **Non-governed narrative profile**: (a) what counts as a "declared capability" for an observed public repo; (b) deep-dive bands may collapse when empty; (c) exact-source leaf = admitted span, not `openspec/**`; (d) altitude order for a dossier. | REQ-004 (amend `:78`, base `:228-232`); RFC7-13/14/17 | (d) **B ruling**, explicitly reserved to the owner ("unless the owner rules otherwise"). (a)–(c) **A-d** CC-REV-2 delta → **B** sign-off [Inferred: (c) may be an interpretation ruling] | — | M |
| 18 | **Competitive-advantage framing**: decide whether "advantages" = maintainer-stated advantages only (lawful now), or also admits external comparison sources (new consent + spec silence). | REQ-002; prompts forbid browsing | **B ruling** (cheap) | — | S |
| 19 | **Reader-facing page budget** (bytes/words per depth). | TRACKER open question; CC-REV-2 | A-d → **B** | — | S (after first measurement) |
| 20 | **Daemon draft route** `/polaris/draft/<runId>` (machine-credentialed). Optional: the static file suffices. | `routes.ts`; PWB machine-view member; registry ceiling | A (route); a ceiling declaration may need a **B** registry act | `dov.7.2` | M |
| 21 | **Agent SDK on the owner's subscription**: permitted by the provider's terms? Can tools, telemetry and transcripts be disabled? Rate limits for ~1–2 h of Opus? | — | **C** (verify; fallback: direct API needs a new egress record version naming that route, B) | — | S to verify |
| 22 | **Licence-trio regeneration** (7.2.4 → 7.4.0 → 8.0.0). Needs LICENSE, so #16. | TARGETS.md | A after #16 | `syzygy-mea` | S per run |

## 7. Ordered plan (one owner sitting)

**Phase 1: self-drivable, in parallel (≈2–3 weeks of agent time).** Nothing here reads
Redis or calls a model.

- **Lane E (engine):** #2 → #1 → #3 → #7 → #8 → #9. Test on synthetic fixtures and the
  self-corpus (P-76 Q2 permits Syzygy reading itself; it does **not** permit egress of
  Syzygy text — see the flag below).
- **Lane P (provider):** #4 against a local capture endpoint, then #5.
- **Lane G (governance drafting):** #11 → #12, #13, #14, #15 → #16 → #17(a–c) and #19
  as one CC-REV-2 delta. Each gets a fresh-context review to CONFIRM or notes-only, under
  the 2026-09-26 stopping rule. Register every phrase and copy in `check_governance.py`
  before offering.
- **Lane V:** #10 (a minimal reader-question runner first).
- **External check:** #21 before #13's bytes freeze. If the subscription route cannot
  meet the conditions, redraft #13 for the direct API before the sitting, not after.

**Phase 2: one owner sitting.** Batch every B item, and use the Q5 option-selection form
where the precedent allows. The owner would give:

1. **Policy act:** the public-source screening scope (#12).
2. **Registry acts:** the provider execution route and the source-acquisition adapter (#15).
3. **Egress consent act:** `(project:syzygy, anthropic)` covering psf/requests and
   redis/redis, plus the Redis docs repo if chosen (#13).
4. **Observation consent acts:** psf/requests @ v2.34.2, and redis/redis @ 8.10.2 plus the
   licence-trio tags (#14).
5. **Contract amendment act:** the RFC5-14 `project-documentation` class (#16). This
   likely needs a typed digest phrase, because accepted-contract amendments have so far
   been phrase-bound [Inferred]. If it is not ready, the sitting proceeds without it and
   Redis runs on code only (Q7(b)), losing README and LICENSE.
6. **Spec sign-off and ruling:** the non-governed narrative profile delta (#17 a–c,
   CC-REV-2), the altitude-order ruling (#17d), the advantages ruling (#18), and the page
   budget (#19, or defer it until after the T1 measurement).
7. **Optional standing direction (#9).** It shrinks every *future* target to the
   sentence plus one confirmation, and must say:
   - future per-target observation consent and egress-version instances are the builder's
     deterministic fill of the reviewed templates from (repository, revision);
   - the owner's per-target act may be a single option naming those generated rows;
   - template-identical instances need no fresh review round.

   This is a novel reading of Q5 [Inferred] and needs its own review. It **cannot**
   remove the per-target act, which is a SEC-2 floor.

**Phase 3: run (A).**

1. T1 requests: a smoke run, then fix the prompts and renderer.
2. Redis @ 8.10.2 with the dossier profile: hierarchical discovery, 1–2 h budget.
3. Static multi-page draft in the run directory; independent fidelity plus a
   rendered-reader review; repair; log lessons in the LEARNING-LOG.
4. Then the licence-trio regeneration (needs #16).

**Phase 4 (optional).** The `/polaris/draft/<runId>` route (#20); Sentry as T3 for scale.

**Sittings.** One for Redis, assuming #16 and #17 are ready by then; otherwise two
(admit and run on code-only first, then the class amendment and profile). After that,
zero or one quick click per new repository, given item 7.

## 8. Hard-prohibition and doctrine flags

- **"Never read a repository body without per-repository consent and the applicable
  registry and policy acts."** No Redis body may be fetched, listed or read until Phase 2
  items 1, 2 and 4 are in force. That includes the "1.5–3k files" estimate above, which
  is deliberately unverified. A `git ls-remote` (refs only) was already used in TARGETS.md;
  a tree listing is `code-structure` content [Inferred] and waits too.
- **SEC-2 per-project egress consent is doctrine.** A blanket "any public repo" consent
  would need a doctrine amendment. Not recommended; the per-target click is the floor.
- **Egress of Syzygy's own prompts.** Every request carries `prompts.ts` text, classified
  `code-content` of `project:syzygy`; the egress instance scopes it explicitly. Even a
  synthetic smoke test against the real provider is therefore egress and waits for #13.
  Before that, test only against a local capture endpoint.
- **The egress record forbids tools on the provider route.** The model cannot explore
  Redis agentically. All research must be orchestrated by Syzygy's code (#3), which is
  what makes the "1–2 hours" budget a fan-out design problem rather than a long agent
  session. Allowing a read-only tool over the admitted snapshot would be a new egress
  record version (B).
- **"Syzygy never adopts intent autonomously" / VIS-4.** The dossier is an editorial
  draft, never Redis's adopted intent or statement (egress condition; REQ-010). No
  conflict if it is labelled; it must never be published or presented as redis.io's
  account (Q6).
- **"The daemon never executes observed project code."** Redis is never built or
  benchmarked. Performance or "mechanism" claims come from source and docs text only,
  and measured claims stay Unknown.
- **No release or broad remote access.** The page stays local (Q6). Serving it on the
  tailnet or sharing it publicly would need its own act.
- **AGENTS.md routing note.** It still says the generator's "candidate guidance is not
  … permission for new source reads/provider egress". That is consistent: the
  permission comes only from the Phase 2 acts.
