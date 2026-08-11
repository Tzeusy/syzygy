# Formal Capability 1 launch administration — sealed packet

> **Prepared, not administered.** This packet is everything a reviewer
> needs to run **one full, formal administration** of the launch gate
> against the launch target below. **No administration has been run under
> it**, and this repository's authoring sessions may not run one: an
> administration by the corpus's own authors is not the evidence a launch
> decision needs (instrument §2 — *"A repair session may not administer the
> gate over its own repaired bytes"*).
>
> Nothing in this packet is an owner act. A `READY` verdict authorizes
> nothing; the owner's launch decision is separate and comes after.

## 1. What is being asked

Administer `launch-gate-pre-specifications.md` **v2.0**, in full, at the
named commit, against:

```text
LAUNCH TARGET
    Capability 1 — Project registration and honest shape visibility

REQUIRED WAVES
    A, B

DEFERRED WAVES
    C1, C2, D1, D2
    candidate; not accepted; not used by the launch target; excluded from
    default task routing. Posture and per-wave reasons:
    .syzygy/governance/contracts/candidates/DEFERRED-WAVE-POSTURE.md
```

## 2. What is bound — verify every digest before you begin

```text
repository commit    5c3013f0784bc76236cfe2380d21701a625079cf

launch-gate-pre-specifications.md (v2.0)
    05ecaa954e81ef95f6e2e2b409fbcb5bd5391037c10d9624ab4af3217a00f6d2
§8 parameter block (as bound for this administration)
    01209c0f052971f794e1f35827a002aa8d80420aad471d10fde000abb6366ff6
launch-gate-administration.schema.json
    e0167fb8af6a903c527d402d56c4fb85ebdfed9608de1a485f4f1563aa6a69fb
scripts/validate_launch_administration.py
    d6b203f7c276aa4e58e0b1d0bb4d4cf947158dea34255370a2683bc981e0c745
scripts/render_launch_administration.py
    9f90fa6ad6f6feaed175b78fe9e0901a2e3279586ffbf73b7854ead6140f9ed3
```

Verify, in a fresh clone at that commit:

```sh
git log --oneline -1
git status --porcelain                       # must print nothing
sha256sum launch-gate-pre-specifications.md launch-gate-administration.schema.json \
          scripts/validate_launch_administration.py scripts/render_launch_administration.py
```

**If any digest differs, stop.** The packet is stale and the administration
would bind bytes nobody offered. Report the mismatch rather than proceeding.

## 3. How the record is produced

**The record is JSON, not prose.** Author a file conforming to
`launch-gate-administration.schema.json`, then:

```sh
python3 scripts/validate_launch_administration.py <record>.json --trend-row
python3 scripts/render_launch_administration.py  <record>.json
```

The validator computes the verdict from your rows. **There is no field in
which to write a verdict** — the schema rejects one. The Markdown report is
generated and is never read back as authority.

Set `"formal": true` and `"administration_kind": "full"`. A delta
administration cannot support a gate decision, and the validator refuses
the combination.

## 4. Who may administer this

- **Fresh context.** No prior contact with this repository's review
  history, no summaries of "how it's going", no prior administrations
  (except the trend log, and only when answering F1).
- **Preferably a different model family from the corpus's authors**, or a
  human. This corpus was authored by Claude models and every administration
  to date has been by that family. If you are also that family, the record
  must say so — `reviewer.same_family_as_corpus_authors: true` — and the
  disclosure travels into the trend row. This is launch-gate **F5**'s own
  example, and hiding it would fail the question the record is answering.
- **Not an authoring session of this repository**, under any circumstance.

## 5. The materials you are given

```text
1. launch-gate-pre-specifications.md              the instrument, in full
2. .syzygy/governance/doctrine/                   the adopted goal statement
3. .syzygy/intent/OVERVIEW.md                     the public entry document
4. read access to the repository at the named commit
5. §8 of the instrument                           the parameter block
6. .syzygy/governance/decisions/launch-gate/TREND-LOG.md   for F1 only
```

**Withheld — do not read for content:** authoring history, prior review
results, prior administrations, and any summary of the project's progress.
Trees holding reviews and administrations are in scope as *objects* of the
F2/F4/C3 sweeps — they are files, and a stale claim in one is a finding —
but their findings and narratives must not inform any other question's
answer. If you read them for content, record it as a materials deviation.

**The materials list is fixed by this packet and the instrument. It is not
curated per administration.** Anything added, missing, or unreadable goes
in `materials.deviations`.

## 6. Fixed inputs you must use as given

**The D2 routing tasks** (parameter block; chosen before the
administration, never by you mid-run):

```text
routine    "add an evidence adapter for a new CI system"
authority  "change what counts as a completed Mission"
seam       "trace a merged change from its work record to its reconciled
            status"                    — crosses the work/evidence seam
```

**The E4 fixed cases** are the six statements in §8's `E4_CASES` list.
Classify each from its text alone (shape side or spec side — two-valued),
then compare against the routing authority named in §8. The validator
checks your `case_text` against the instrument's own bytes: a paraphrased
case carries no verdict.

**The A3 near-misses** and **A5's closed `MAJOR_SHAPE_COMMITMENTS` list**
are likewise fixed in §8. Do not invent softer near-misses, and do not build
A5's population yourself.

## 7. What the owner has and has not decided

**No owner acceptance act has been performed**, and
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` does not exist —
that absence is correct, not a gap. Ten owner decisions are open and
listed in
`.syzygy/governance/contracts/candidates/round-2026-08f/CAPABILITY-1-OWNER-DECISION-PACKET.md`.

This matters for your verdicts in a specific way: **an unruled decision is
not a defect of the corpus** — it is a recorded open question, which is
what VIS-4 requires. What *would* be a defect is a document presenting an
unruled decision as settled. Judge that, not the existence of the queue.

## 8. Spot-review requirements

D2, E3 and E4 are exercises, not document judgments. Their results are to
be **human spot-reviewed** before the record is treated as gate evidence:

- **D2** — did the route actually answer the task, or did it require
  reading the corpus?
- **E3** — is the reopen-list empty because nothing must reopen, or because
  the reading was shallow? The trace table exists to make that visible, and
  the validator refuses `E3 | Met` without it.
- **E4** — do your classifications and the routing authority's actually
  disagree where you say they do?

## 9. What this packet does not contain, deliberately

- **Prior verdicts and repair summaries.** Withheld by §5. If you have seen
  them, say so in `materials.deviations`.
- **A recommended verdict.** There is none, and any document that offered
  one would be inviting the failure the gate exists to catch.
- **The two v2.0 reviews.** They have not been obtained
  (`.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` records
  this). **P-34 is not approved**, so this administration would be run
  under a *candidate* policy. That is disclosed here rather than discovered:
  an administration under an unapproved instrument is evidence the owner may
  weigh, and it is not the "launch-gate v2.0 is owner-approved" conjunct of
  the readiness standard.

## 10. Deliverable

```text
<record>.json    the source record — the deliverable
<record>.md      its generated report
one trend row    printed by --trend-row, appended to TREND-LOG.md
```

Store both verbatim in `.syzygy/governance/decisions/launch-gate/`. Never
edit a past administration; supersede it.
