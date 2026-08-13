# Round-2026-08g — the default human path, and a check for stale current-state prose

> **Candidate account. Binds nothing.** It records what was built and what was
> measured. It adopts no doctrine, accepts no contract, approves no policy,
> rules no queue row, and creates no `openspec/`.

Owner charter §11 in five parts. Three were already satisfied by earlier
passes and are recorded here as verified rather than done again; two were not.

## What was already in place, verified this session

| Charter item | State | Evidence |
|---|---|---|
| **§11.1** README names `doctrine/v1.md` and introduces the root process instruments | satisfied | `README.md` Start-here item 3 is `doctrine/v1.md` with the "yes, but what does it *do*?" framing; the two root instruments are named in their own block, added under RD-50 f10. The strengthened Trajectory subtitle stands |
| **§11.2** a literal process glossary, separate from the product-term registry | satisfied | `PROCESS-GLOSSARY.md` — **all twelve** charter-named terms carry an entry: *act, argument, wave, offer, `P-nn`, `RD-nn`, `E1`–`E6`, formal administration, candidate, confirmed, accepted*. Checked term by term this session, not assumed |
| **§11.3** `decisions/README.md` answers the four newcomer questions | satisfied | its §"The four questions this directory answers" carries them in the charter's own words, each with its owning file and a short answer |

## §11.4 — the currency check, which did not exist

**The rule already had a home.** `CC-KNOW-11` ¶2 of the candidate
knowledge-hygiene policy: *"Prose asserting what is currently true carries its
as-of revision and is never the sole source for the fact it states."* Its
violation example is the charter's target almost exactly — *"a status file
describing 'the current gates' in three hand-maintained places, two of them a
revision behind, none saying as of when it was true."*

What did not exist was anything that looked.

**`CG-27`** now does, over a declared population of **eight** default-path
files. `PROJECT-STATUS.md` is deliberately outside it: that file *owns* wave,
gate and launch state, and requiring the owner to cite itself is circular.

Four claim classes, each with the record that owns the answer:

| Class | Owner |
|---|---|
| wave state | `PROJECT-STATUS.md` |
| launch-gate version | `launch-gate-pre-specifications.md` |
| gate verdict | `PROJECT-STATUS.md` |
| first-spec prerequisite | `PENDING-OWNER-DECISIONS.md` |

A claim is satisfied if its paragraph is about the past, if the paragraph or
the file's **leading** banner names the owning record, or if the claim carries
its own as-of date.

### What it deliberately does not do

- **It never checks whether a claim is true.** It checks whether a reader who
  doubts the claim can tell where to go. A file citing `PROJECT-STATUS.md`
  beside a sentence that flatly contradicts it passes; what fails is the
  sentence standing alone with nothing to check it against.
- **It enforces less than its clause.** `CC-KNOW-11` requires *both* an as-of
  *and* a non-sole source; `CG-27` accepts *either* a derivation *or* a
  visible precedence banner, which is the charter's disjunction. A check that
  under-enforces its clause is safe; one that over-enforces invents obligation
  nobody approved.
- **It is advisory.** Charter §11.4's own condition — *"the rule must have an
  authoritative policy home before the validator is binding"* — is not met: the
  home is a candidate queued as `P-12`. `CG-27` therefore downgrades to WARN,
  printing its findings and its reason, and cannot `exit 1` on a rule nobody
  has ruled on.

The downgrade mechanism was generalised to say this honestly. It previously
had one table, `PYTHON_ONLY_RULES` — *"rule stated only in
check_governance.py"* — which is false of `CG-27`. A second table,
`CANDIDATE_HOME_RULES`, now carries rules whose home is written but not
binding, and `CG-25` reports the two populations separately. **A rule nobody
wrote and a rule nobody ruled on are different states**, and this repository
is largely about that difference.

### Fixtures and mutation

Fifteen fixtures. The charter names five stale classes; each ships with an
**accepting twin**, because a rejecting fixture alone proves only a check that
says no to everything:

```text
stale Wave A state          stale Wave B state
stale launch-gate version   stale first-spec prerequisite
stale gate verdict          correctly bannered historical statement
```

Plus three predicate fixtures the charter does not name and the check would be
weaker without: a banner naming the *wrong* owner must not launder a claim; a
precedence banner *below* the prose does not count; and a zero-claim
population reports WARN, never PASS.

Each satisfaction limb was then disabled and the fixtures re-run — 1, 4, 1, 1
and 1 failures respectively across the five limbs. **Every predicate has
coverage**, which is the property two of Workstream E's predicates lacked
while running and being believed.

### What it found, and one thing the repair taught

Six findings on the live corpus at first run, all real, all repaired:

- **`PROCESS-GLOSSARY.md`** asserted wave state and the gate verdict under a
  banner that said *"the owning record wins"* without saying **which** record.
  The banner now names `PROJECT-STATUS.md`.
- **`TASK-ROUTER.md`** asserted wave state and prerequisite state in generated
  prose. Repaired in the **generator**, not the output.

Then the repair itself misbehaved, and this is the part worth keeping: naming
`PENDING-OWNER-DECISIONS.md` in the router's sentence made it longer, pushing
its state word outside the check's proximity window — so the claim **left the
denominator** and the count fell from 17 to 16. A repair that quiets a check
instead of satisfying it is the failure `CC-KNOW-17` names, and it took a
before/after denominator comparison to see it at all. The window was widened
to a paragraph scale and the claim is back in, satisfied rather than invisible.

*`17` and `16` are the **transient** figures of that one before/after
comparison, kept because the comparison is the lesson. They are **not** the
settled denominator — the remaining repairs moved it again, and the current
figure is whatever `CG-27` prints when you run it. Do not quote these two.*

## §11.5 — AGENTS.md within its band

`# Notes to self` was already relocated to `decisions/PROCESS-LESSONS.md`,
which records the move.

The size band was not met: **1,498 authored words** against a 900–1,200 target,
and over the 1,500-word review trigger. `CC-BUDGET-1` makes crossing a budget
a decomposition review rather than a failure, and the review's finding was
that most of the excess was **restatement**, not procedure:

| Cut | Words | Why it was restatement |
|---|---:|---|
| the whole battery listing | ~110 | a third hand-maintained copy of `PROJECT-STATUS.md`'s block, with `CG-26` comparing only two of the three |
| four rows of the authority table | ~50 | `README.md` carries the reader-facing table; the rows cut were ones no task routes on |
| incident narratives inside four verification rules | ~90 | `decisions/PROCESS-LESSONS.md` owns the incidents and is routed to two lines above |
| the launch-gate and OpenSpec-readiness routing cells | ~55 | restated the verdict and the script layout that `PROJECT-STATUS.md` and the scripts own |
| a compression note about a *previous* compression | ~50 | session narrative |

The per-row figures are **estimates of what each cut removed**, and they do
not sum to the measured change: several cuts replaced a block with shorter
prose rather than deleting it. The measured figure is the only one to quote —
**1,498 → 1,200 authored words, a reduction of 298**, computed by the same
`CG-8` counter before and after.

**1,200 authored words** — inside the band, and the 1,500-word trigger is
clear. One clause moved rather than being cut: *never edit an artifact after
an act has bound its digest* is now a hard prohibition, where it belongs.

`CG-27` saw two fewer claims afterwards, because AGENTS.md stopped restating
`GATE VERDICT: NOT READY` and started pointing at the record that owns it.
That is the check's subject working in the direction it is meant to work.

## Battery

Unchanged at **sixteen** commands — `CG-27` lives inside
`check_governance.py`, which was already in the list. What changed are the
counts it reports: **50 checks** (was 49) and **149 fixtures** (was 134).
