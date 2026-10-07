# Tasks — Polaris dossier for an arbitrary public repository

> **Candidate — binds nothing.** No task starts before the owner's acts in
> `OWNER-PACKET.md` are recorded.

## Before sign-off

- [x] Round 1 fresh-context review (REVISE), retained as
      `docs/reviews/R-ARBITRARY-PUBLIC-REPO-1-RAW.md`; repaired per the
      lead's dispositions.
- [ ] Round 2 fresh-context review of these bytes (dispatched by the lead).
- [ ] Owner answers Q0 to Q8 in `OWNER-PACKET.md`; strike REQ-039 if ruling
      10b is kept; narrow REQ-038's first sentence if Q5 is answered no; if
      Q2 (history) is answered no, the history paragraphs of REQ-037 stay as
      the disabled option or are struck, at the owner's choice.
- [ ] Package and review the amendments in `AMENDMENTS.md` (A1 to A4) as
      installable patches with manifests, rebased over D7 and D8 if those
      land first.
- [ ] Re-check that requirement numbers 037 to 039 are still free on `main`.

## After sign-off

The implementation slices, in order, are in `design.md`, "Implementation
slices". They are not filed as beads until the owner signs; the change's own
bead, `syzygy-mzge`, tracks the gate.
