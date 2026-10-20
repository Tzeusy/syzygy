# Tasks — one-command Polaris dossier run

> **Candidate — binds nothing.** This repair schedules no implementation.
> The separately authorized prototype is described in `design.md`; this
> candidate still needs the owner's sign-off.

## Before sign-off

- [x] Owner direction recorded 2026-10-14, answering Q0 and Q1
      (`decisions/POLARIS-DOSSIER-ONE-COMMAND-RUN-DIRECTION.md`).
- [x] Owner answered Q2 to Q7 with the recommendations, and authorized a
      prototype of slices 1 to 5 (direction follow-up, 2026-10-14). Each
      answer took the drafted arm, so no requirement was struck or narrowed.
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
- [x] Round 1 fresh-context review, REQ-045 included, returned `REVISE`;
      verbatim raw retained in `docs/reviews/` as
      `R-POLARIS-DOSSIER-ONE-COMMAND-RUN-1-RAW.md`, with its campaign row.
- [x] Round 2 confirming review returned `REVISE`; raw retained as
      `R-POLARIS-DOSSIER-ONE-COMMAND-RUN-2-RAW.md`, with the unchanged
      `ROUND-2-DISPOSITIONS.md` recording that lane's stop.
- [x] Lead selected one bounded source-design repair and fresh round 3,
      recorded separately in `ROUND-3-REPAIRS.md`; no owner act is claimed.
- [ ] Round 3 fresh-context review of the frozen repaired commit, using
      `REVIEW-BRIEF-ROUND-3.md`; retain its raw unchanged. A `REVISE` verdict
      ends this bounded cycle with dispositions and a report, not another
      repair or an offered sign-off.
- [ ] Re-check that requirement numbers 040 to 045 remain unique to this
      candidate across `main` and active changes
      (the candidate retains its six identities; re-check at the frozen
      review head and before any installation).
- [ ] Owner sign-off by version tag.

## After sign-off

File one epic and the eight slices in `design.md`, "Implementation slices",
as beads with the dependencies stated there.
