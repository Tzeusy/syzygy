# Capability 1 readability successor — review notes

Review 2 (`docs/reviews/R-CAP1-READABILITY-SUCCESSOR-2-RAW.md`) confirms the
manifest with exceptions; its six notes are non-blocking. Under the owner's
stopping rule a notes-only round clears the reviewed bytes, so the notes are
answered here rather than by another edit to the package.

- **N1 — the act record's descriptive text is not digest-bound.** The scope,
  supersedes, title and artifact strings come from `SUCCESSOR.json`, which
  neither the owner's argument nor the review covers. The installed bytes are
  bound; the words around them are not. The record's fixed sentence that the
  act widens no implementation authority still applies. Binding the
  descriptive text is tracked as tool work for the next successor package.
- **N2 — "every claim is kept".** Two Impact sentences are dropped: "No code,
  APIs, or systems exist to be affected" and "Implementation impact is
  deliberately unplanned". Both have been false since the implementation
  authorization, and the restyled Impact section names that authorization
  instead.
- **N3 — banner wording.** "Lists every bound digest" is kept as written.
- **N4 — act-record template.** The record says every requirement block is
  unchanged. For this package that is true of the whole file: the
  specification is not a subject that changes, so its row equals its
  predecessor. The tool itself guards requirement headings, scenario headings
  and warrant blocks; the template wording is tracked with N1.
- **N5 — three selftest mutants** are killed by a traceback rather than a
  fixture's own assertion. They still fail closed.
- **N6 — minor leftovers:** small glosses dropped, one cross-cutting item
  numbered "7" under "six groups", and the date in the `docs/README.md` row.
  The README date is corrected; the other two stay as reviewed.
