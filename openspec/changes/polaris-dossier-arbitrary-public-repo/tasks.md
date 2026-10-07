# Tasks — Polaris dossier for an arbitrary public repository

> **Candidate — binds nothing.** No task starts before the owner's acts in
> `OWNER-PACKET.md` are recorded.

## Before sign-off

- [x] Round 1 fresh-context review (REVISE), retained as
      `docs/reviews/R-ARBITRARY-PUBLIC-REPO-1-RAW.md`; repaired per the
      lead's dispositions.
- [x] Round 2 fresh-context review (REVISE), retained as
      `docs/reviews/R-ARBITRARY-PUBLIC-REPO-2-RAW.md`; repaired per the
      lead's dispositions.
- [ ] Round 3 fresh-context review of these bytes (dispatched by the lead;
      the last round before the lead decides).
- [ ] Owner answers Q0 to Q8 in `OWNER-PACKET.md`; strike REQ-039 if Q6 is
      answered no; narrow REQ-038's first sentence if Q5 is answered no;
      strike every passage naming the history option (packet Q2), and A4's
      history clause, if Q2 is answered no.
- [ ] Package and review the amendments in `AMENDMENTS.md` (A1, A1b, A2 to A4) as
      installable patches with manifests, rebased over D7 and D8 if those
      land first.
- [ ] Re-check that requirement numbers 037 to 039 are still free on `main`.

## After sign-off

The implementation slices, in order, are in `design.md`, "Implementation
slices". They are not filed as beads until the owner signs; the change's own
bead, `syzygy-mzge`, tracks the gate.
