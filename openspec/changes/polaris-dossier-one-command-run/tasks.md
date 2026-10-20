# Tasks — one-command Polaris dossier run

> **Candidate — binds nothing.** No implementation task starts before the
> owner's acts in `OWNER-PACKET.md` are recorded.

## Before sign-off

- [x] Owner direction recorded 2026-10-14, answering Q0 and Q1
      (`decisions/POLARIS-DOSSIER-ONE-COMMAND-RUN-DIRECTION.md`).
- [x] Owner answered Q2 to Q7 with the recommendations, and authorized a
      prototype of slices 1 to 5 (direction follow-up, 2026-10-14). Nothing
      to strike; strike or narrow requirements per the answers (Q2 changes
      REQ-041's disclosure; Q4 no changes REQ-042's refusal; Q5 no adds a
      pause rule to REQ-043; Q6 renames the command throughout).
- [x] REQ-045 (the local agent CLI subprocess runner) folded in 2026-10-20
      from the cleared candidate
      `contracts/candidates/dossier-local-cli-subprocess-runner/`, with its
      round-5 notes (`ROUND-5-NOTES.md`) carried in; the warrant-family
      gap is closed in `apps/three-surface-poc/src/polaris-authority-sweep.test.ts`.
- [ ] Generate `GOVERNING-DEPENDENCIES.md` with
      `scripts/build_polaris_dependency_unions.py` over the proposed spec
      (the script reads installed additions only, so this follows the
      sign-off that installs the spec in `specs/`).
- [ ] Draft `IMPACT-LEDGER.md`: every artifact the change touches (REQ-035
      readings, `inventory.ts`, `session-handover.ts`, `gate-sources.ts`
      disclosure, the runbook, the polaris-dossier skill).
- [ ] Design-bar pass on the attended view (REQ-043) before review.
- [ ] Round 1 fresh-context review of these bytes, REQ-045 included; raw
      retained in `docs/reviews/` as
      `R-POLARIS-DOSSIER-ONE-COMMAND-RUN-1-RAW.md`, with its campaign row.
- [ ] Re-check that requirement numbers 040 to 045 are still free on `main`
      (040 to 045 found only in this change's proposed spec, 2026-10-20).
- [ ] Owner sign-off by version tag.

## After sign-off

File one epic and the eight slices in `design.md`, "Implementation slices",
as beads with the dependencies stated there.
