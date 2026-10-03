# Polaris generalization — working tracker

Plain checklist for the open-source proving ground ([TARGETS.md](TARGETS.md)).
The owner chose markdown tracking for this work on 2026-10-03; the `bd` epic
`syzygy-mea` stays the umbrella and points here. Tick items in the same commit
as the work. Lessons go in [LEARNING-LOG.md](LEARNING-LOG.md), not here.

Legend: `[x]` done · `[ ]` open · `[~]` in progress · **(owner)** needs an
owner decision or act.

## Owner goal, 2026-10-03: "a Polaris dossier for redis/redis"

The owner's target sentence: *"Please generate me a Polaris dossier for
https://github.com/redis/redis"*. After 1–2 hours of Opus, a page should take
a reader through the core ideas, end-to-end workflows, underlying mechanisms,
competitive advantages and trade-offs.

The gap analysis is [REDIS-DOSSIER-GAP-ANALYSIS.md](REDIS-DOSSIER-GAP-ANALYSIS.md)
(research note, binds nothing). Its gap numbers (#1–#22) are cited below as
`[gap #n]`.

**The floor.** SEC-2 makes consent per project, so the sentence still needs one
owner sitting for the first target. After that, each new repository needs one
option-selection.

**Phase 1 lanes.** None of these reads Redis or calls a model:

- **Engine:** `[gap #2]` → G1 → G4 / `[gap #3]` → dossier profile → multi-page
  output → one-line trigger.
- **Provider:** G2, tested against a local capture endpoint, then G3.
- **Governance drafting:** Phase 0 items, then Redis instances, screening scope,
  registry entries, the RFC-0005 class and the non-governed narrative profile.

Engine and provider items additional to Phase 1 below:

- [ ] Oversize sources: chunk a body over 100,000 characters into spans, or
      exclude it with a reason. One file must never fail the run `[gap #2]`
- [ ] Hierarchical discovery: map calls over subsystems → claim ledger →
      reduce, with ranked selection and `deferred-by-budget` accounting. This
      is what makes a 1–2 hour budget useful `[gap #3]`
- [ ] Dossier run profile:
      - the owner's five reader questions (core ideas, end-to-end workflows,
        mechanisms, advantages as the maintainers state them, trade-offs);
      - requested assets (workflow diagrams, component deep dives);
      - a zero-interaction REQ-031 mode `[gap #7]`
- [ ] Multi-page static output: an entry page plus deep-dive pages, with
      contents, glossary and a size report, written to the run directory
      `[gap #8]`
- [ ] One-line trigger: `poc:dossier <github-url>` pins the revision, builds
      the per-target admission rows, names the one owner question, then runs
      `[gap #9]`
- [ ] External check: can the Agent SDK on the owner's login meet the
      egress record's conditions (no tools, no context, telemetry off,
      captured request), and what are the rate limits? Check this before
      the egress bytes freeze `[gap #21]`

Governance drafting for Redis. All of these bind nothing until the owner
acts:

- [ ] Redis instances for the admission package: observation consent for
      redis/redis at `8.10.2` and the licence trio, and the next egress
      version listing requests and Redis `[gap #11, #13, #14]`
- [ ] Public-source screening scope instance, reconciled with PR #120
      `[gap #12]`
- [ ] Registry entries: the provider execution route and one shared
      Git-hosting source-acquisition adapter `[gap #15]`
- [ ] Non-governed narrative profile, one CC-REV-2 delta covering three
      points `[gap #17 a–c]`:
      - what a "declared capability" is for an observed public repository;
      - empty deep-dive bands collapse;
      - the exact-source leaf is the admitted span
- [ ] **(owner)** Rulings:
      - altitude order for a dossier `[gap #17d]`;
      - advantages as maintainer-stated only, or with external comparison
        sources `[gap #18]`;
      - page budget, after the T1 measurement `[gap #19]`
- [ ] **(owner)** One sitting: policy, two registry entries, egress, the
      observation consents, the RFC-0005 class and the profile sign-off

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
  - [x] **G1 Any-repo CLI.** `repo-corpus.ts` / `repo-corpus-main.ts` take
        `--repo`, `--revision`, `--repository-id`, include/exclude globs and a
        JSON config (reader questions, assets, budget, oversize policy); the
        read happens only after an admission port answers `allowed: true`
        (default port refuses). `readSelfCorpus` is unchanged. Every git call runs
        with an allowlisted environment and `--no-replace-objects`
        (`isolated-git.ts`); an ambient `GIT_DIR` or a `refs/replace` entry
        cannot change what the pinned commit reads.
  - [~] **Public-source screening** (`syzygy-vjqd`, gap #12).
        `readScreenedRepoCorpus` (`public-source-screening.ts`) loads the
        secret-classification policy by the public-source scope act record,
        refuses the run when the record is absent or the policy bytes do not
        hash to its argument, and runs the policy's denied-path rules, every
        detector and the active-content scan over each selected blob. A
        withheld row has a per-run HMAC id and no path, object id or body.
        Review repairs (reviewer-6 B1–B4): a blob whose final segment ends
        in none of the scope's `sourceExtensions` is withheld unread as
        indeterminate; the detectors also run over every path; with a screen
        in force, binary, empty and oversize-excluded rows are withheld rows
        too; a test pins a match past the first 100,000-character piece.
        One run key keys every withheld id (#278, #323). A path carrying a
        control character (tab, CR, LF, DEL and every other C0 code point),
        a backslash or non-UTF-8 bytes is unquotable: under a screen it is
        counted only, and a path-detector match on it is counted separately
        (#333). Policy residuals, pinned by tests: an encoded or line-split
        secret passes the detectors. Screening scope v2 (package #326, draft
        PR, `project-documentation.ts`): the policy's root, docs/doc and
        licenses rules map `project-documentation` under the v2 act, only
        while the RFC5-14 class act is in force (otherwise those paths stay
        indeterminate); every screen still runs first; parity with the
        builder's reference reader over 126 fixtures and 4,592 generated
        paths per variant. Not yet: the trigger wiring (#268), the
        run-profile and instruction-text rules, and consent filtering by
        class. Nothing passes the gate until the owner performs the acts.
  - [ ] **G2 Real `generate` port.** A Claude Agent SDK adapter behind
        `PipelinePorts.generate` (`pipeline.ts`): structured output for
        `responseSchema`, usage accounting, abort. Per the egress record:
        every tool off; no instruction, memory, settings, MCP or environment
        context; empty working directory and all runtime state inside the
        run directory; telemetry off; accepted only when a captured request
        shows nothing but what the generator built. Only `scriptedGenerate`
        exists. The durable lifecycle around it is now generic
        (`createDurableLifecycle` in `durable-lifecycle.ts`, injected
        `generate`, same dispatch-claim crash semantics); the scripted
        version is a thin wrapper.
  - [ ] **G3 Consent-backed ports.** `permissionIdentity` / `admit` /
        `permitted` read the admission records instead of returning `true`
        (blocked on Phase 0 sign-off for the first real call, not for the code).
  - [x] **G0 Oversize sources (gap #2).** A blob over 100,000 characters is
        split into contiguous `-pN` pieces (`segment` on `GenerationSource`,
        blob-absolute anchors, contiguity checked per population) or excluded
        as `oversize-source-excluded`; it no longer fails the population.
  - [x] **G4 Discovery under budget (REQ-030).** `discovery.ts`
        (`packages/polaris-generation-core`): partition into subsystems, map
        to a claim ledger, reduce to a ranking, select under the 200 cap;
        every unselected file stays counted as `deferred-by-budget`. Model
        ports are injected and egress-gated; the report names the ranking
        basis. Every call is permitted per call and leaves a durable receipt;
        a report replays from receipts alone, bound to each call's request
        digest. Wiring to a real model is still G2/G3.
  - [x] **Discovery on a large-C-server-shaped tree (syzygy-mea.1).** A
        synthetic 510-file fixture (`redis-shaped-fixture.ts`; built from
        public layout knowledge, no real repository read) measured heuristic
        discovery at the default budget: before, a vendored README outranked
        first-party code and ties fell to path order, deferring the data-type
        files and `src/server.c`. `heuristicScore` now puts vendored and
        generated directories in a strict tier below all first-party files
        (still counted `deferred-by-budget`) and adds a capped size bonus.
        After: no vendored file selected, all 18 core-mechanism files
        selected, selected plus deferred equals the candidates. Evidence
        `docs/evidence/redis-shaped-discovery-2026-10-04.json`;
        `npm run poc:redis-shaped-discovery`.
  - [x] **Closed exclusion reasons.** `GENERATION_EXCLUSION_REASONS`
        (`generation-source.ts`, a plain literal array) lists every reason an
        excluded source may carry; `validateGenerationSources` refuses any
        other reason and any excluded row whose id is not `s-` plus 24 hex
        digits (the validator checks that shape only). The PWB adapter
        keys an excluded row's id as HMAC-SHA256 of a per-run random key over
        the source identity, so it is stable within a run and not across runs;
        non-excluded rows keep the unkeyed identity hash. It maps its closed
        withholding reasons onto the set (a detector match with no closed
        reason is `secret-detector-match`) and falls back to
        `unclassified-exclusion`; it never passes the classifier's sentence
        through.
  - [x] **One-line trigger (gap #9).** `npm run poc:dossier -- <github-url>`
        pins the revision with `git ls-remote` (metadata), prints which
        admission records (observation consent, public-source policy, egress
        consent) are missing, and stops (exit 3). It reads and generates only
        once an injected record store satisfies all three; none is wired yet,
        and no generate port exists (exit 5 after recording the corpus). Git
        runs with a minimal environment and a bare, template-free fetch;
        discovery calls are permitted only while the egress record holds;
        the repository id admitted and used for the run is the one the single
        observation record whose `Upstream:` is the canonical URL carries,
        read through `AdmissionRecordsPort.repositoryIdsFor` (zero or several
        records: exit 3, nothing read); the URL-derived spelling is only a
        label. The run directory is pre-flighted before any fetch; one created
        after that check is refused at write time and the run is not recorded
        elsewhere. The run is written by `writeDossierRun` (realpath parent, fail-closed
        git check, atomic staging) and rendered by `renderDossier`
        (polaris-dossier-v1), which `dossier-main` wires as the default `render`
        port.
        A stopped run (usage, wall clock, refused stage) is rendered from its
        completed stage outputs (`artifacts` on the stopped result) alongside
        `run-record.json` and exits 7; when the renderer cannot render it
        (`DossierRenderError`), only the record is written and the exit is 6
        (syzygy-k4t2). `dossier-main` passes `requestedAssets`, which the
        renderer requires for a stopped result; a page-level test runs a
        scripted pipeline out of usage budget after two stages and checks the
        banner and every requested asset as Unknown `deferred-by-budget`.
  - [~] **G5 Evaluation harness.** Reader-test runner, reader-cost (bytes and
        words per depth), page budget, REQ-031 clarification questions. A
        first run can happen without it; it cannot be judged without it.
        Landed (2026-10-03): `evaluateDossier` and `poc:dossier-evaluation`
        over the `polaris-dossier-v1` input — reader cost against an optional
        budget, quote and label fidelity, a scripted reader-test port, and
        coverage per owner topic. Open: a real reader port, answer grading,
        REQ-031 clarification questions.
- [x] Multi-page static output `[gap #8]`: `renderDossier` /
      `poc:dossier-render` (2026-10-03) writes an entry page, contents,
      deep dives, glossary, one page per quotable source routed by anchor
      and a size report, in `polaris-dossier-v1` markup; the run directory is
      refused inside a Git work tree; round-trips through `evaluateDossier`
      with 0 fidelity failures on synthetic runs
- [~] REQ-030 accounted discovery: walk an unfamiliar tree within a budget
      and say what was and was not read (engine built and tested on synthetic
      trees; no real tree walked)
- [~] REQ-031 owner clarification: the consequential-questions step
      (`dossier-profile.ts`: question budget, no repeats, attributed
      non-adopting answers, zero-interaction mode that records the questions
      it would have asked; reuses an unchanged prior disposition and
      re-asks when the question's content digest changed; reader questions
      are `{id, topics, text}` objects validated at the pipeline entry by
      `validateReaderQuestions`; synthetic only)
- [x] Dossier run profile `dossier-v1`: five reader questions (core ideas,
      end-to-end workflows, underlying mechanisms, maintainer-claimed
      advantages, trade-offs) and their requested assets;
      `profile: "dossier"` in the reader config
- [ ] Real provider adapter behind the single egress check (refuses without
      consent; no call happens until admission)
- [~] Evaluation runner: frozen reader questions, fresh-reader answers,
      fidelity check, reader-cost measurement (bytes and words to first level)
      — landed except a real fresh reader: scripted answers only (G5)
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
