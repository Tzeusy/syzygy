# Polaris dossier local-agent mode v1.1 — round-2 review notes

> **Candidate — binds nothing.** This is the sibling record for the notes of
> the second fresh-context review of version 1.1 of the
> `polaris-dossier-local-agent-mode` amendment (draft PR #368). Under the
> owner's notes-only rule
> (`../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), a round
> with no revise-level finding clears the exact bytes it read, and its notes
> go in a sibling record, never into the reviewed bytes. So this file sits
> outside the package directory and edits nothing in it. It signs nothing
> off: only the owner's own selection does that (VIS-4). The sign-off is
> version-tagged and binds no act digest, so nothing here is registered in
> `check_governance.py`.

Reviewed record: docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-2-RAW.md

## What was confirmed

- **Package:** the candidate package
  .syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode-v1-1/
  (patches under its `proposed/` and four prose files), on draft PR #368,
  not on `main` yet.
- **Reviewed commit:** `1110512435f34c35b0337282ba9f69e671dc8af6`.
- **Subject:** the change's `specs/polaris-generation/spec.md` after
  `proposed/spec.md.patch` alone is applied to the v1.0 bytes, sha256
  `b5564fe4f52b98716349c72307e123090952986cfd45dd7e2aab3fbf68765204`; with
  the optional N6 hunk,
  `6414597d73572c903b0f876fd31d58f04d1b42a8c1a68361aa3a5f30feb598ee`.
- **Verdict:** `CONFIRM WITH EXCEPTIONS`, on line 4 of the raw named on the
  `Reviewed record:` line above, with five findings, each a note, and
  "None" under "Blocking findings". The raw finds the N6 hunk's round-1 note
  repaired and raises nothing on it.
- Round 1 returned `REVISE` over `afd789a9` (1 revise, 8 notes); its
  dispositions are in the package's `REVIEW-BRIEF.md`, and its raw is
  retained by the lead as
  docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-V1-1-1-RAW.md.

## The notes and what happens to each

None changes what 1.1 requires. Each is carried here, not repaired in the
reviewed bytes.

| # | Note | Disposition |
|---|---|---|
| 1 | The N5 sentence defers the skill to "the run's `brief.md`", the authoring brief, though the same skill serves inventory and review sessions | Implementation obligation: the skill and Codex texts defer each session to the brief or packet it was given (the run's `brief.md` only for the authoring session), as 033's "Only the authoring session's brief may carry the permission" already requires. Wording for a later version: "defer to the execution rule in the brief or packet the session was given" |
| 2 | `design.md` keeps "its configuration holds" where the spec now reads "Syzygy holds" | Later version, editorial; the requirements control |
| 3 | The packet quotes D9 as "names what the instruction covers"; SEC-3 as adopted reads "naming what the instruction covers" | The owner should read SEC-3's words: "the owner has recorded a choice for that one run, naming what the instruction covers". The lead's batch to the owner carries the correction beside question 2 |
| 4 | The packet's prerequisite line omits the selftests | Immaterial to the owner; the delta and ledger name them |
| 5 | "Consent or policy record without its owner act" asserts a standing page disclosure in its AND | Later version: move the AND to "Mode disclosed on every page"; the scenario is falsifiable as written |
