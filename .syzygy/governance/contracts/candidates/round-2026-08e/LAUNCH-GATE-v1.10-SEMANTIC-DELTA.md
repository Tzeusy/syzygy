# Launch-gate v1.9 → v1.10 — semantic delta record

> **Process record for a candidate instrument amendment.** The instrument
> (`launch-gate-pre-specifications.md`, repo root) is a process-policy
> candidate, never authority. This delta records every change of meaning so
> "no question was weakened" stays a reviewable claim. Owner approval of
> v1.10 is prepared, not performed:
> `.syzygy/governance/decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34) —
> and the offer waits on a fresh-context re-review of this delta
> (**RD-38**), because the session that authored these bytes may not
> confirm them.

Baseline: v1.9 as re-reviewed by RD-37 (subject sha256
`bc1363bffedb5d908c2345369ce44dbc3a286649c0e3ff18862b74e6d482b10d` at
commit `95a41ea`; raw review `reviews/RD-37-instrument-v19-RAW.md`,
`VERDICT: REVISE`, 0 BLOCKING / 2 MAJOR / 4 MINOR — and all seven RD-36
repairs verified present, both decisive ones re-proven by mutation, §1–§8
byte-identical per-section for the third amendment running). Every delta
below closes an RD-37 finding; dispositions in
`reviews/DISPOSITION-REGISTER.md`. **This is a validator-and-records batch
a third time: no question block, no verdict word, and no section §1–§8 of
the instrument changed.** The instrument bytes that move are the
`effective_version:` header and the §9 v1.10 entry — nothing else; the §9
v1.9 entry needed no correction marker, because RD-37 found it "true as
far as it goes" (the false sentence lives in the v1.9 *delta*, corrected
below in the D-10 convention). Validator changes carry fixtures
(`scripts/launch_gate_results.py --selftest`, **86 fixtures**); all four
decisive repairs re-proven by mutation, each failing exactly the fixtures
it added.

RD-37's diagnosis, adopted as this batch's discipline — the first
diagnosis to move in five administrations: *"the fixture set tests one
predicate at a time, and a shared predicate has more than one consumer …
the discipline that ends this chain is not another direction of fixture;
it is uniformity of application: when a predicate or a parsing rule is
repaired, it is repaired for every consumer and every field, and the
fixture asserts the uniformity rather than the instance."* This batch
splits the shared predicate, applies the field-parsing rule to every
declared field, and adds a source-scan meta-fixture that fails any future
field reverting to a first-match read. Like RD-35, RD-36 and RD-37, this
record predicts nothing about whether the batch is the last.

## D-1 — correction of the v1.9 delta's D-4 (the frozen record is not edited)

The v1.9 delta's D-4 states: *"One disclosed edge: a genuine finding line
led by a negation clause would be wrongly classed as empty — loudly, as a
rejection the administrator sees, never as a silent pass."* **RD-37
measured that sentence false of LG-13** — the check D-4's own preceding
sentence is about: on LG-9 and LG-12 the edge is a loud rejection; on
LG-13 "names nothing" is the *no-error* branch, so the same edge is
exactly a silent pass, and a regression — four records the v1.8 validator
rejected validated clean at v1.9 (RD-37 §5, the cross-version execution
table). Per the D-10 convention the frozen v1.9 delta is not edited; this
entry is the correction of record, and the repair itself is D-2.

## D-2 — LG-13's emptiness becomes a positive closed-marker test; the shared predicate is split (RD37-01, MAJOR)

At v1.9, `_names_nothing()` served LG-9/LG-12 (where "names nothing" IS
the error) and LG-13 (where it was the no-error branch) — consumers of
opposite polarity, so RD36-04's widening tightened two checks and
silently loosened the third. At v1.10:

- LG-13 reads emptiness **positively**: the reopen-list is empty iff its
  value full-line-matches the closed marker vocabulary §5's own template
  slot names — `empty`, `none`, `none identified` (case-insensitive,
  optional trailing period). Anything else — a negation clause leading an
  enumeration, an unfilled template slot — is a non-empty reopen-list,
  and the failure is loud (both branches: beside `E3 | Met`, and under
  any READY verdict).
- `_names_nothing()` now serves LG-9 and LG-12 only, the two checks of
  one polarity; the comment above it records why.
- Fixtures in the newly-blind direction: the negation-led enumerated
  list rejects beside `E3 | Met` and under READY; the unfilled template
  slot rejects; the three lawful markers accept. Executed against
  RD-37's own four attack records: 2 LG-13 errors each; the markers 0.
- Mutation-proven: reverting LG-13 to the negated placeholder test fails
  exactly the three RD37-01 fixtures.

No instrument sentence changes: §5's slot already reads
`<empty | enumerated items>`, and the marker vocabulary is validator
policy beneath it, stated here and in the validator's own comment.

## D-3 — every declared field parses uniformly; the meta-fixture asserts the rule (RD37-02 MAJOR, RD37-06 MINOR)

RD36-03's repair collected all occurrences for four fields of fifteen;
the three §5 content fields driving LG-9, LG-12 and LG-13 stayed on
first match, so a decoy above the declared line silently discarded the
honest answer — three clean passes over contradictory records, on the
three checks §3 and §4 call decisive. At v1.10:

- One helper, `_decl()`, parses **every** declared field — `Launch
  target:`, both counts, `Owner deferral decision:`, the deferred-wave
  findings line, `Unknowns and what would settle them:`, `E3
  reopen-list:`, and the label-shaped §2 integrity anchors (`Instrument
  version:`, its `sha256:`, `Parameter block sha256:`) — collecting all
  occurrences, erroring on disagreement **in both orders**, taking the
  last (declared) value.
- A **source-scan meta-fixture** enumerates the declared labels and
  fails the selftest if any is ever read by a raw `re.search` again —
  the fixture asserts the uniformity, not the instance, which is
  RD-37's own prescription verbatim.
- Fixtures: decoy-above for E3 (RD-37's exact demonstration), decoy for
  Unknowns, decoy for the findings line, a disagreeing duplicate §2
  anchor, and an agreeing duplicate accepting (no false rejection).
- Mutation-proven: reverting the E3 field to `re.search` fails the
  decoy fixture AND the meta-fixture.

**Scope decision, stated rather than silent (RD37-06):** the two
prose-shaped header patterns — the administration date and the named
commit — stay first-match, outside `_decl`. They are not `Label:` fields:
a lawful record names other commits in evidence and narrative ("repaired
at commit `x`"), so a disagreement test over the prose shape would reject
lawful records. The header is the first occurrence by §5's own
construction, and RD-37 measured the blind direction benign for these
two. The comment at the parse site records the same.

## D-4 — LG-4 anchors to the G1 heading's own shape (RD37-03, MINOR)

`^#+ .*G1` was satisfied by any heading that mentioned G1, so a record
with its completeness-critic section deleted validated clean on the
strength of an incidental mention. At v1.10 the test is `^#+\s*G1\b` —
G1 leads the heading text. Fixtures both directions: the
mention-only record rejects; a bare `### G1` heading accepts.
Mutation-proven.

## D-5 — the `--prior` record is validated before it is trusted (RD37-04, MINOR)

The prior side of the trend comparison ran no checks, so an arbitrary
file — including one carrying rows a current record would reject — could
suppress the New-findings column F1 is answered from. At v1.10 the prior
must cover the full question roster with no alien rows; otherwise the
validator errors, names what failed, and the trend column reads
`n/a — prior record failed validation` instead of a number. A bespoke
fixture proves both halves; the two existing lawful-prior fixtures prove
no false rejection. Mutation-proven.

## D-6 — the SDR existence guard: anchored, and scoped to made decisions (RD37-05, MINOR)

The v1.9 guard was a fixed-string substring search over the whole
decisions home. Two latent weaknesses, neither exploitable against the
live population: an unminted `SDR-3` would ride on a minted `SDR-33` if
the population ever had gaps, and the corpus included
`PENDING-OWNER-DECISIONS.md` — the queue of decisions **not yet made**,
whose mentions rule nothing. At v1.10 the match is anchored at
identifier boundaries and the pending queue is excluded from the
searched corpus, matching the guard's stated purpose ("only families
that name MADE decisions may claim a granted deferral").

**Honest cap, stated rather than silent:** the live SDR population
(SDR-1…SDR-33, gapless — RD-37's sweep, denominator 18 files) makes the
substring direction unfixturable against the real corpus: every
identifier that is a substring of a minted one is itself minted. The
anchoring is asserted structurally in the validator's own docstring and
this delta; the existing both-direction fixtures (`SDR-33` accepted,
`SDR-9999` rejected, tree rejected, real path accepted) all still
execute against the scoped corpus.

## What did not change

- **No section §1–§8 of the instrument changed** — verify per-section
  against `git show 95a41ea:launch-gate-pre-specifications.md`. The §8
  parameter block hashes identically across all six instrument versions
  (RD-37 §0's measurement; recompute it with the validator's own
  `param_block_bytes`, never from this record).
  The instrument bytes that move: the `effective_version:` header and
  the appended §9 v1.10 entry. The §9 v1.9 entry carries **no**
  correction marker — RD-37: "the §9 v1.9 entry's account of the
  RD36-04 repair is true as far as it goes and asserts nothing false."
- **No frozen record is edited.** The v1.4–v1.9 deltas and the RD-33 …
  RD-37 raw reviews are byte-identical to their pre-batch state; the
  v1.9 delta's false D-4 is corrected by this delta's D-1, in the D-10
  convention.
- **No question weakened, no ID renumbered, no verdict word changed.**
- The newly rejected records are those §3, §4 and §5 already condemned
  in prose — and this time the claim covers **both directions**: the
  batch also newly *accepts* nothing. D-2 through D-6 each only reject
  records v1.9 accepted or refuse inputs v1.9 trusted; the sole
  accepting change is the agreeing-duplicate non-rejection in D-3,
  which v1.9 also accepted (verified by running the fixture against
  the v1.9 code path). A lawful record under a correct v1.9 reading
  remains lawful under v1.10.

## Fixture arithmetic

74 → **86**: +3 RD37-01 (negation-led enumeration ×2 branches, template
slot), +5 RD37-02/06 (three decoys, one §2 anchor decoy, one agreeing
duplicate accept), +2 RD37-03 (mention rejected, bare heading accepted),
+1 RD37-04 bespoke (prior refused), +1 the RD37-02 meta-fixture. All
LG-1…LG-13 checks still fire; the four decisive repairs are
mutation-proven, each failing exactly the fixtures it added.
