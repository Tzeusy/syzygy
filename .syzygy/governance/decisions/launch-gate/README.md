# Launch-gate result home

This directory is the canonical home the instrument's header names
(`launch-gate-pre-specifications.md`, `canonical_result_home:`). It holds:

- **Administration records**, stored verbatim, one file per administration,
  named `ADMINISTRATION-<n>-<date>.md`. A record here is **evidence, never
  an owner act** — no verdict in this directory adopts, accepts, approves,
  or authorizes anything (VIS-4; the instrument's three-artifact-class
  rule).
- **`TREND-LOG.md`** — one appended line per administration (instrument
  §6); F1's evidence.

Nothing else belongs here. The 2026-08-09 pilot record predates this home
and remains immutable at
`.syzygy/governance/contracts/candidates/round-2026-08d/reviews/`.

Empty today, correctly: no formal administration has been run. The first
record to land here is "Administration 1" — the first administration
meeting the instrument's §2 integrity requirements.

> **Superseded 2026-08-18; marked here 2026-09-06.** The two paragraphs
> above are kept unedited because a stored review cites the last one
> verbatim as evidence of the project's own epistemic discipline
> (`../../contracts/candidates/round-2026-08e/reviews/RD-28-spec-authoring-RAW.md`),
> and a review's referent may not be edited out from under it. They are
> both false now, in three ways.
>
> **This directory is not empty, and Administration 1 has been run.** It
> was administered 2026-08-18 against commit `71e5986` under instrument
> v2.4, and the gate verdict was `NOT READY` (10 not met, 2 scoped, 5
> Unknown). `TREND-LOG.md` carries its row. `NOT READY` is the honest
> answer the pilot predicted, not a failure of this home; what it forbids
> is a launch decision resting on this gate, and nothing in the project
> claims one.
>
> **The record is JSON, and the Markdown beside it is generated.**
> `ADMINISTRATION-2026-08-18-CAPABILITY-1.json` is the canonical record,
> validated against `launch-gate-administration.schema.json`; the
> `.md` file of the same stem is rendered from it and is **never parsed
> back**. Read or check the JSON. This is the whole point of the v2.0
> change — thirteen consecutive `REVISE` verdicts were spent learning that
> a Markdown record cannot be parsed safely (`HISTORY.md` is that
> chronology).
>
> **The naming convention above was never followed, and two other file
> classes live here.** The record's stem is
> `ADMINISTRATION-<date>-<subject>`, not `ADMINISTRATION-<n>-<date>`; the
> ordinal lives in `TREND-LOG.md` and the record body, not in the
> filename. Beside the record and the trend log sit two further files, both
> intended: `HISTORY.md`, the non-authoritative v1.3→v1.18 review
> chronology moved here on 2026-08-11 under the owner charter's §6.1, and
> `ADMINISTRATION-2026-08-18-CAPABILITY-1-VALIDATION-TRANSCRIPT-RAW.txt`,
> the validator's unedited output at that administration — the evidence
> that the record passed schema, roster, verdict-vocabulary and
> integrity-binding checks at the commit it names. Store the transcript
> beside every future record: a JSON record with no retained validation
> transcript is a record no later reader can confirm was ever checked, and
> a transcript is valid only for the commit it names (verification rule 7).
