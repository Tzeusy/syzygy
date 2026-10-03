# Polaris generalization — working tracker

Plain checklist for the open-source proving ground ([TARGETS.md](TARGETS.md)).
The owner chose markdown tracking for this work on 2026-10-03; the `bd` epic
`syzygy-mea` stays the umbrella and points here. Tick items in the same commit
as the work. Lessons go in [LEARNING-LOG.md](LEARNING-LOG.md), not here.

Legend: `[x]` done · `[ ]` open · `[~]` in progress · **(owner)** needs an
owner decision or act.

## Phase 0 — Set up the proving ground

- [x] Choose targets and pin revisions — requests, Redis, Sentry; Redis
      licence trio for regeneration (2026-10-03, TARGETS.md)
- [x] Study the three reference sites; first lessons L1–L5 (2026-10-03)
- [x] Start the learning log, seeded with Butlers lessons L6–L8
- [x] Draft the reusable public-repository admission template as a candidate
      package — branch `polaris/public-repo-admission`, with its
      instance builder script
- [x] **(owner)** Answer the packet's Q1–Q7 (2026-10-03): all recommendations
      taken except Q1 — Anthropic through the Claude Agent SDK runtime
- [~] Fresh-context review of the admission package (CONFIRM, or notes only).
      Rounds 1–4: REVISE (4, 2, 1, 1 blocking), each repaired. Round 4 ran over
      the owner's answers; its repair is unreviewed. Draft PR #215
- [ ] Draft the RFC-0005 amendment adding a project-documentation content
      class (Q7); T1 runs without it and records what it could not send
- [ ] Package manifest, recorder and `check_governance.py` registration for
      the sign-off (Q5)
- [ ] **(owner)** Sign off the template, then admit T1 (requests)

## Phase 1 — Make the engine able to run on an unfamiliar repo

Authorized implementation work (generator implementation authorization,
2026-09-12); needs no new act until a provider call.

- [x] Inventory what the generator core already does end to end (2026-10-03).
      Working today: the six stage prompts are real and project-neutral
      (`packages/polaris-generation-core/src/prompts.ts`); the pipeline and a
      single-page static preview with a strict CSP run on synthetic input and on
      Syzygy's own governance Markdown. Never run: a real model. Gaps, smallest
      first:
  - [ ] **G1 Any-repo CLI.** Make the self-corpus reader
        (`apps/three-surface-poc/src/polaris-generation/self-corpus.ts`, fixed to
        `project:syzygy`, `.syzygy/` roots and `.md`) take `--repo`,
        `--revision`, include globs and a repository id; reader questions,
        assets and budget from a config file.
  - [ ] **G2 Real `generate` port.** A Claude Agent SDK adapter behind
        `PipelinePorts.generate` (`pipeline.ts`): structured output for
        `responseSchema`, usage accounting, abort. Per the egress record:
        every tool off; no instruction, memory, settings, MCP or environment
        context; empty working directory and all runtime state inside the
        run directory; telemetry off; accepted only when a captured request
        shows nothing but what the generator built. Only `scriptedGenerate`
        exists.
  - [ ] **G3 Consent-backed ports.** `permissionIdentity` / `admit` /
        `permitted` read the admission records instead of returning `true`
        (blocked on Phase 0 sign-off for the first real call, not for the code).
  - [x] **G0 Oversize sources (gap #2).** A blob over 100,000 characters is
        split into contiguous `-pN` pieces (`segment` on `GenerationSource`,
        blob-absolute anchors, contiguity checked per population) or excluded
        as `oversize-source-excluded`; it no longer fails the population.
  - [ ] **G4 Discovery under budget (REQ-030).** The pipeline refuses more than
        200 quotable sources, and requests has more; needs ranked selection
        with `deferred-by-budget` exclusions.
  - [ ] **G5 Evaluation harness.** Reader-test runner, reader-cost (bytes and
        words per depth), page budget, REQ-031 clarification questions. A
        first run can happen without it; it cannot be judged without it.
- [ ] REQ-030 accounted discovery: walk an unfamiliar tree within a budget
      and say what was and was not read
- [ ] REQ-031 owner clarification: the consequential-questions step
- [ ] Real provider adapter behind the single egress check (refuses without
      consent; no call happens until admission)
- [ ] Evaluation runner: frozen reader questions, fresh-reader answers,
      fidelity check, reader-cost measurement (bytes and words to first level)
- [ ] Apply L1–L3 to the plan and author prompts: thesis first, a show-don't-
      tell artifact, intent-labelled reading depths
- [ ] Apply L6: epistemic label once per region, exceptions marked

## Phase 2 — T1: requests

- [ ] Admission records in force (observation + egress)
- [ ] Freeze the seven reader questions before generating
- [ ] Generate at `v2.34.2`; retain the run record
- [ ] Independent fidelity and rendered-reader review
- [ ] Reader test: generated page vs requests.readthedocs.io
- [ ] Log lessons; carry each into prompts, renderer or validator

## Phase 3 — T2: Redis and the licence change

- [ ] Admission covering `7.2.4`, `7.4.0`, `8.0.0`, `8.10.2`
- [ ] Generate at `7.2.4`, then regenerate at `7.4.0` and `8.0.0` with the
      unchanged process; check every licence-dependent statement moved
- [ ] Reader test vs redis.io

## Phase 4 — T3: Sentry at scale

- [ ] Admission
- [ ] Generate at `26.9.0` within declared discovery and page budgets
- [ ] Reader test vs develop.sentry.dev
- [ ] Portability evidence: diff of the three runs' inputs is profile only

## Open questions

- [ ] **(owner)** Reader-facing performance budget for generated sites (first
      reading level ≤ N KB / N words; deep dives as separate pages). The
      generator specification has no such requirement today, so this needs a
      CC-REV-2 amendment. Measure on T1 first, then propose the number.
- [ ] Manifesto layer vs evidence layer: does REQ-004's reading-depth
      structure already allow argument-first pages with evidence one level
      down, or does that need an amendment? Answer from the spec text.
