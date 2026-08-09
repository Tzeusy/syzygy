# Shape-to-spec propagation fixture (E6 dry run)

> **Non-product governance fixture.** Everything below is deliberately
> fictitious: the "specifications" are mock stubs that exist only inside
> this file, no `openspec/` tree exists or is implied, and no mock
> requirement describes real intended behavior. The fixture exists so the
> propagation path (shape delta → affected-spec enumeration → interim
> contradiction/Unknown → responsible amendment → same logical change or
> recorded exception → re-evaluation) can be exercised and reviewed
> **before** real specifications exist. A reviewer derives the impacted
> set blind from the TASK section; the ANSWER section is the fixture's
> golden result. Do not read past the boundary marker when administering.

## Governing description (what the path is; owners cited, nothing invented)

1. **Shape delta** — an amendment to an accepted contract clause lands as
   a semantic delta (NORMATIVE-CHANGE-WORKFLOW shape).
2. **Affected-spec enumeration** — a blast-radius sweep over the spec
   corpus for every requirement citing the amended clause or consuming
   its vocabulary; the sweep's denominator is recorded (verification
   rule 9).
3. **Interim contradiction/Unknown** — until amendments land, each
   affected requirement renders as contradicted/Unknown, never silently
   stale (VIS-2; CC-REV-2 forbids leaving mainline asserting the old
   truth).
4. **Responsible amendment** — the shape change's author owns the spec
   amendments (CC-REV-2's same-logical-change merge invariant), or
   records an explicit exception with its reason and expiry condition.
5. **Re-evaluation** — affected acceptance criteria are re-judged; the
   re-evaluation is recorded with the change.

## TASK (give the reviewer everything above and below, up to the boundary)

**The mock corpus.** Four mock specifications, each with three mock
requirements citing mock clause IDs of the real corpus's *shape* (clause
IDs are real; the requirements are fictitious):

- **SPEC-REG (registration):** REG-1 cites RFC3-5 (closed declaration
  field set); REG-2 cites RFC3-9; REG-3 cites RFC1-3 (consent).
- **SPEC-FACETS (shape visibility):** FAC-1 cites RFC6-18 (one fact set
  per selection); FAC-2 cites RFC6-19 (facet folding rules); FAC-3 cites
  RFC2-24 (Unknown reasons).
- **SPEC-ENTRY (human entry):** ENT-1 cites RFC7-39 (fixed entry);
  ENT-2 cites RFC7-40 (discoverability finding); ENT-3 cites VIS-5
  (write boundary).
- **SPEC-QUERY (machine parity):** QRY-1 cites RFC6-13 (one truth, two
  consumers); QRY-2 cites RFC6-14; QRY-3 cites RFC5-5 (endpoint set).

**The mock shape amendment.** RFC6-19 is amended to add one facet-folding
prohibition, and RFC2-24's reason vocabulary gains one owner-approved
reason (a lawful amendment to the closed list, performed by the owner).

**The reviewer's task.** From the mock corpus and the amendment alone,
enumerate: (a) the impacted requirement set that must be re-examined;
(b) the unaffected set; (c) what renders as contradicted/Unknown in the
interim; (d) who owns the amendment under the path above. Record the
denominator of your sweep (12 mock requirements).

---- TASK/ANSWER BOUNDARY — administering sessions stop here ----

## ANSWER (golden result)

- **Impacted (4 of 12):** FAC-2 (cites the amended RFC6-19 directly);
  FAC-3 (cites RFC2-24, whose reason vocabulary changed); FAC-1
  (consumes RFC6-19's folding semantics through RFC6-18's fact-set
  contract — impacted at one remove; a sweep matching only literal
  clause citations misses it, which is why the enumeration must follow
  declared vocabulary consumption, not string match alone); QRY-1
  (renders facet answers to both consumers; the new prohibition changes
  what a lawful rendered answer is).
- **Unaffected (8 of 12):** REG-1/2/3, ENT-1/2/3, QRY-2, QRY-3 — none
  cites or consumes the amended vocabulary.
- **Interim rendering:** FAC-1/2/3 and QRY-1 render
  contradicted/Unknown from the delta's land until their amendments
  land; the other eight render normally.
- **Responsibility:** the shape amendment's author, in the same logical
  change, or a recorded exception naming FAC-1's one-remove impact
  explicitly (the likeliest candidate for an honest exception, and the
  row a lazy sweep drops).

**Expected divergence worth catching:** a reviewer who enumerates only
FAC-2 and FAC-3 has performed the string-match sweep; the fixture's
value is that FAC-1 and QRY-1 are impacted through consumption, and any
real propagation mechanism must catch that class or say it cannot.
