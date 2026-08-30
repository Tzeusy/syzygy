# A6 scope-versus-capacity assessment

> **Recorded assessment, not a ruling.** `A6-RESOURCE-ENVELOPE-DECISION.md`
> states the envelope and explicitly defers this exact question: *"The
> scope-versus-capacity assessment is not performed here... that
> assessment is separate follow-on work, and its outcome is not
> presumed."* This record performs it. **It records facts only. It
> proposes nothing** — no recommendation, no scope change, no ceiling
> change, no next step. Every claim below is labeled `[Observed]`,
> `[Inferred]`, or `[Unknown]` per this repo's epistemic discipline
> (`AGENTS.md` "Epistemic and change discipline"); an Unknown is left
> Unknown, never smoothed into an assumed fit.
>
> As-of: this session, 2026-08-30. Evidence gathered from the repository
> and its Beads database only; nothing here observes the owner directly.

## The envelope, restated

Per `A6-RESOURCE-ENVELOPE-DECISION.md` (ruled 2026-08-19):

| Constraint | Owner's statement |
|---|---|
| Engineering attention | 2 hours/week |
| Review capacity/cadence | Claude-family agents plus the owner; occasional GPT 5.6-family review; no fixed cadence |
| Model/provider budget ceiling | $200/month (Codex monthly subscription) |
| Maximum concurrent supervised workstreams | 2–3 |
| Proving-project sequencing | Syzygy first, butlers second |

## 1. Engineering attention (2 hours/week)

**Assessment: Unknown.**

- `[Unknown]` This repository contains no record of the owner's actual
  wall-clock time spent per week. The repository can observe artifact
  timestamps, commit cadence, and agent activity, but none of these are
  the same measurement as owner engineering-attention-hours — a stated
  personal capacity constraint that only the owner can report
  (`A6-RESOURCE-ENVELOPE-DECISION.md` itself makes this same point about
  the envelope's rows: *"Only the owner knows the real values"* —
  `PROJECT-OPERATING-CONSTRAINTS-DECISION.md` line 9).
- `[Observed]` Commits touching `.syzygy/governance/decisions/` land on 8
  distinct calendar days across the 16-day window 2026-08-16 through
  2026-08-30 (`git log --since=2026-08-16 --until=2026-08-31 --format=%ad
  --date=short -- .syzygy/governance/decisions/`: 3 commits on 08-16, 9 on
  08-17, 2 each on 08-18/08-19/08-20/08-21, none from 08-22 through
  08-28 inclusive, 1 on 08-29, 7 on 08-30). This shows *when* governance
  artifacts changed, not how many owner-hours each change consumed —
  a burst of same-day agent output is consistent with anywhere from
  minutes to hours of owner engagement per day.
- `[Unknown]` Whether the observed commit-day pattern is compatible with a
  2-hour/week ceiling cannot be decided from repository evidence alone,
  because the owner's role in each commit (direct authorship, review,
  brief approval, or no involvement) is not separately recorded here.

## 2. Model/provider budget ceiling ($200/month, flat)

**Assessment: fit, with one Unknown the record does not resolve.**

- `[Observed]` The ceiling is stated as a flat monthly subscription cost,
  not a metered per-usage budget (`A6-RESOURCE-ENVELOPE-DECISION.md` line
  23: *"$200/month (Codex monthly subscription)"*). A flat subscription
  cost does not increase with usage volume within the subscription's own
  terms, so "stays within $200/month" is close to trivially true for
  activity billed under that one subscription, regardless of how much
  agent activity the subscription's usage terms permit.
- `[Observed]` A sweep of `.syzygy/governance/decisions/*.md` for cost,
  budget, spend, or subscription language (`grep -rniE
  '\$[0-9]+|budget|spend|subscription|cost'`, excluding this assessment
  file itself) returns 23 files. Checking dollar figures specifically
  (`grep -rniE '\$[0-9]+'` over the same tree) finds exactly two hits,
  both the same `$200/month` figure: the original statement in
  `A6-RESOURCE-ENVELOPE-DECISION.md` and its direct quote in
  `DECISION-HISTORY.md`'s P-45 row. No other decision record states a
  second dollar figure, a second subscription, or an additional spend
  competing for the same $200/month ceiling.
- `[Unknown]` The $200/month row names a **Codex** subscription
  specifically. The review-capacity row on the same line-item table names
  the actual workforce as *"Claude-family agents plus the owner;
  occasional GPT 5.6-family review"* — i.e., the model family doing most
  of the recorded work (this repository's agent activity, including this
  assessment) is not the model family the budget row names. Whether
  Claude-family usage draws on this same $200/month ceiling, a separate
  unstated arrangement, or a differently-metered plan is not stated
  anywhere in the governance record swept above. `A6-RESOURCE-ENVELOPE-
  DECISION.md`'s own boundary section states the figure "authorizes no
  spending... a ceiling that exists, not a budget granted" — it does not
  say which billed product(s) the ceiling covers.

## 3. Maximum concurrent supervised workstreams (2–3)

**Assessment: misfit, by count, against multiple independent countings; each counting is disclosed with its own basis.**

- `[Observed]` `bd list --status in_progress --json` returns 5 issues as
  of this session: `syzygy-kyt` ("Make RFC11-4 satisfiable and the golden
  fixtures testable"), `syzygy-5fj` ("Split the RFC-0010 package, then
  repair the six blocking Mission-safety findings"), `syzygy-mdo` (this
  assessment), `syzygy-3m5` ("Retune remaining 'no openspec/ exists'
  banners..."), `syzygy-0wf` ("Route the fourteen open source-of-truth
  findings to homes"). Literal Beads `in_progress` count: 5, against a
  stated ceiling of 2–3.
- `[Observed]` Two of those five (`syzygy-mdo`, `syzygy-3m5`) carry an
  identical `[beads-heartbeat] owner=coordinator:goal-20260830T060447Z`
  tag, meaning both are dispatched sub-work of one coordinating goal
  rather than two independently-supervised workstreams. `syzygy-5fj`'s
  notes describe its own further fan-out ("Fresh-context reviews (rd13
  mission-prevention, rd14 mission-effects, plus wave D1/D2 exact-package
  reviewers) are running..."). `syzygy-kyt` and `syzygy-0wf` carry no
  heartbeat/owner annotation in their current notes. Whether "workstream"
  in the envelope's sense means a Beads issue, a coordinating goal, or
  something coarser is not defined in `A6-RESOURCE-ENVELOPE-DECISION.md`
  or elsewhere in the swept governance record — this is an `[Inferred]`
  gap in the term's definition, not a resolved count.
- `[Observed]` Independent of Beads state, this session's own runtime
  roster (the "Other agents active in this session" list available to
  this assessment) names 23 other concurrently addressable agents beyond
  this one, spanning role prefixes `main`, `correction-`, `planner-`,
  `reviewer-`, and `worker-`. This is a direct, same-session observation
  of concurrently active agent processes, not an inference from Beads
  metadata. `[Inferred]` The role-prefix diversity (planning, review, and
  worker-execution roles running simultaneously) suggests more than one
  distinct effort is in flight at once, though the roster alone does not
  establish a one-to-one mapping between named agents and "workstreams"
  in the envelope's sense.
- `[Observed]` By the top-level status accounting in `AGENTS.md` and
  `PROJECT-STATUS.md`, Capability 1 is complete (all RT1–RT9 closed,
  fresh-clone bar met) and the Three-Surface POC is complete (8/8 items
  closed, confirmation verdict **CONFIRMED** at
  `docs/reviews/R-POC-CONFIRMATION-REVIEW.md`, dated 2026-08-30). Neither
  of the two named authorized-scope programs is itself an open
  workstream today by that reading. The open-workstream evidence above
  (in-progress Beads issues, the live agent roster) is process/governance
  and deferred-wave-contract work (RFC-0010/0011 repair, launch-gate
  finding routing, banner retuning), not further Capability-1 or POC
  product work.

## 4. Proving-project pacing (syzygy first, then butlers)

**Assessment: fit, on the evidence available.**

- `[Observed]` A case-insensitive sweep of
  `.syzygy/governance/decisions/*.md` for "butlers" finds the name first
  appearing, outside the 2026-08-19 envelope statement itself and its
  citing `DECISION-HISTORY.md` entry, in
  `THREE-SURFACE-POC-REDESIGN-DIRECTION.md` and
  `THREE-SURFACE-POC-SPEC-AUTHORIZATION.md` — both part of the
  2026-08-29-dated Three-Surface POC authorization. No decision record
  dated before 2026-08-29 names Butlers as an object of implementation,
  observation, or access.
- `[Observed]` All Capability 1 implementation work (authorized
  2026-08-21, complete 2026-08-23 per `AGENTS.md` "Capability 1
  implementation status") ran entirely inside the syzygy repository; the
  POC direction record (`THREE-SURFACE-POC-MODE-DIRECTION.md`) states
  Butlers involvement is bounded to "one external Butlers repository" and
  `AGENTS.md`'s hard prohibitions repeat the same one-repository bound.
- `[Observed]` This matches the stated order — syzygy engaged first and
  exclusively for ten days (2026-08-19 to 2026-08-29), butlers engaged
  only from 2026-08-29 onward, and only within the one-repository bound
  the authorization states.

## Review cadence, against what the envelope states

**Assessment: Unknown fit against the stated "no fixed cadence," with dense observed activity in the recent window.**

- `[Observed]` The envelope states review cadence as "no fixed cadence."
  A record that states no cadence cannot itself be in fit or misfit
  against a frequency, since it names none.
- `[Observed]` `docs/reviews/` (the implementation-phase review record,
  distinct from the OpenSpec-authoring `contracts/candidates/round-*`
  review trees) holds 8 files: `R-RT-RUNTIME-REVIEW.md`,
  `R-RT-CONFIRMATION-REVIEW.md`, `R-S2-RISK-FLOOR-REVIEW.md`,
  `R-S5-RISK-FLOOR-REVIEW.md`, `R-S6-RISK-FLOOR-REVIEW.md`,
  `R-S7-RISK-FLOOR-REVIEW.md`, `R-POC-PRODUCT-REVIEW.md`,
  `R-POC-CONFIRMATION-REVIEW.md`. Their commit
  dates (`git log --since=2026-08-16 --until=2026-08-31 --format=%ad
  --date=short -- docs/reviews/`) cluster on 2026-08-21, 08-22 (3),
  08-23 (3), and 08-30 (2) — four distinct days across the 16-day window,
  each with either one or several reviews landing the same day.
  `R-POC-CONFIRMATION-REVIEW.md` (`docs/reviews/R-POC-CONFIRMATION-
  REVIEW.md`) records a review, a named repair, and a same-day
  confirmation review all completing within the single day 2026-08-30.
- `[Inferred]` The pattern — zero-review days interspersed with single
  days carrying multiple independent review passes — is consistent with
  "no fixed cadence" as stated (cadence is genuinely irregular by this
  evidence), but is a separate claim from whether that irregular cadence
  fits inside 2 hours/week of owner attention, which is the Unknown
  recorded in Section 1.

## Boundary

This record states facts only, gathered from the repository and Beads
database available to this session. It authorizes no scope change, no
ceiling change, no workstream reduction, and no cadence policy. It
answers no question this session did not evidence, and where evidence
could not decide a row, that row is recorded Unknown rather than assumed
to fit.
