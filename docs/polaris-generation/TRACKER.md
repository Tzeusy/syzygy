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
- [~] Draft the reusable public-repository admission template as a candidate
      package — branch `polaris/public-repo-admission`
- [ ] Fresh-context review of the admission package (CONFIRM, or notes only)
- [ ] **(owner)** Decide the open questions in the admission packet: provider
      and model, retention of sent content and replies, and whether
      version-tag sign-off (Scope A) extends to admission records
- [ ] **(owner)** Sign off the template, then admit T1 (requests)

## Phase 1 — Make the engine able to run on an unfamiliar repo

Authorized implementation work (generator implementation authorization,
2026-09-12); needs no new act until a provider call.

- [ ] Inventory what the generator core already does end to end on the
      synthetic corpus; write the gap list here
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
