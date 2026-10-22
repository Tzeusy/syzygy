# The recorder line slot, read one way (syzygy-bpyt.8.17)

Evidence report, not authority. It records why the consent gate's recorder
templates now read a line slot with `[^\S\r\n]*\S[^\r\n]*` instead of
`[^\r\n]*\S[^\r\n]*`, why no verdict and no slot value changes, and what
was run to check that. CC-REV-1 class 4 (availability on the consent gate),
under GP-Q0 of
`.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`.

## The change

`SLOT.line` in `packages/polaris-generation-consent/src/recorder-template.ts`
is the pattern every owner-selection and review-provenance slot of the
recorder templates takes (`opening`, `label`, `description`, `quote`,
`review`, `disposition`). The templates built from it are the five
local-agent sitting acts, the provider statement version 2 act and the
local-agent source-acquisition sign-off (`packages/polaris-dossier/src/gate-sources.ts`
and `packages/polaris-generation-consent/src/package-reader.ts`). No other
byte of the gate changes.

| | Pattern |
|---|---|
| before | `[^\r\n]*\S[^\r\n]*` |
| after | `[^\S\r\n]*\S[^\r\n]*` |

[Observed] Before, a record that matched a template up to and past several
line slots and then failed took tens of seconds to refuse: 30 to 93 s for
one read of the provider statement version 2 record altered after its four
slots (`docs/evidence/consent-gate-slot-line-timing-2026-10-21.json`, PR
#500), and every such read refused. The cause is that the earlier pattern
could place its one `\S` at any non-space character of the line, so the
engine retried the rest of the template once per placement, in every slot,
multiplied.

## Why the verdicts cannot change

Write B for the two breaks (CR, LF), W for the characters `\s` matches
other than B, N for the characters `\s` does not match, and A for `[^\r\n]`,
that is W and N together. Under the `u` flag the template regexes are built
with, each is a set of code points. The old pattern is `A* N A*`, the new
one `W* N A*`.

**The same lines.** Every string the new pattern matches, the old one
matches, since W lies inside A. Conversely, take a string the old pattern
matches: it holds no break and at least one N. Cut it before its first N.
What comes before holds no N and no break, so it is in `W*`; then comes
that N; then the rest, which holds no break, so it is in `A*`. So both
patterns match exactly the break-free strings with a non-space, which is
what the doc comment says a line is.

**The same slot values.** A template regex is literal text, named slot
groups, and `\k<name>` backreferences for a slot the template repeats,
anchored at both ends. The engine returns the first success in its
backtracking order, and a slot's captured value is the span from where the
group starts to where it ends, whatever way the pattern split it inside.

- Starting at position p, let f be the first N at or after p and m the
  end of the run of A from p. The new pattern's `W*` can only stop at f
  (stopping earlier asks `\S` to match a space), so it tries each end e
  from m down to f + 1, once each.
- The old pattern tries, for each N it may pick from the last to the
  first, every end from m down to just past that N. Its ends are therefore
  the same set, and the first time it tries each end is in the same
  descending order; it only revisits an end after it has tried every larger
  one.
- What follows the slot gets the same position and the same captures on a
  revisit, so it fails again, as it did the first time (had it succeeded,
  the search would have stopped). So both patterns stop at the largest end
  at which the rest of the template succeeds, with the same value.
- By induction from the last slot to the first, every slot reads the same
  value and every read the same verdict; `templateFields` renders the same
  fields back to the same text.

[Inferred] That is an argument over the regex structure, not a measurement.
The checks below test it.

**Why it is fast.** [Inferred] The new pattern has one way to match a given
end, so each slot tries each end once and the literal after it rejects all
but the few where that literal appears; nothing multiplies across slots.

## What was run

The host is shared with other lanes; every timing below is wall time under
that load, on 12 cores. The timing record states the 1-minute load average
at the start of each measurement: 19.8 to 36.5. Forty-nine `uptime` samples,
taken once a minute while the differential ran and not retained, ranged
from 18.6 to 54.2. Times are upper bounds for an unloaded run.

### Same lines, same slot values: generated strings

Five tests in
`packages/polaris-generation-consent/src/recorder-template.test.ts`, named
`the line slot (syzygy-bpyt.8.17) …`, hold the old pattern as a literal and
compare it with `SLOT.line`. Every run of the old pattern is wrapped in a
`node:vm` timeout, which V8 honours inside a backtracking regular
expression. [Observed] All five pass.

- Every string of up to 4 characters over 16 characters, 69,905 strings:
  - the characters are a non-space; space, tab, VT and FF; CR and LF; NEL
    and ZWSP, which are not `\s`; NBSP, the line and paragraph separators,
    the ideographic space and ZWNBSP, which are; an astral character; and a
    lone surrogate;
  - 0 disagree;
  - the new pattern accepts 33,990, the count a line's definition gives
    (14^n - 9^n of the strings of length n). The count is written in the
    test as a literal.
- Every string of up to 8 characters over a non-space, a space, CR and LF,
  87,381 strings: 0 disagree, and 502 are accepted (2^n - 1 of each
  length).
- 4,000 seeded random strings of up to 159 characters, drawn from the 23
  characters other than CR and LF that the engine reads as `\s` (scanned
  from the BMP when the test runs), nine non-spaces and the two breaks:
  0 disagree.
- Template slot values: six templates, with slots on their own lines, two
  or three slots on one line (split by a space, a tab, an ideographic space
  or nothing), and a repeated slot. Each template gets 1,500 generated
  records, half of them edited once or twice. Over the 9,000 records, the
  raw slots and `templateFields` are identical under both patterns; more
  than 1,000 are read and more than 1,000 refused.

### The timing-bounded test

`refuses a record that fails after four long line slots within a second`
reads a record of four 160-character slots that fails on its last literal,
inside a 1,000 ms `vm` timeout.

[Observed] From `docs/evidence/recorder-line-slot-timing-2026-10-22.json`,
at `d1c03e9f`:

| Pattern | Time on that record | Margin |
|---|---|---|
| new | 0.16 ms (worst of 20) | passes the bound 6,250 times over |
| old | 711,106 ms, once (11.9 minutes) | misses the bound 711 times over |

The load average was 30.4 when these ran.

### Rule 6

`scripts/run_line_slot_rule6_mutants.py` mutated the slot eight ways, at
`a7a3a365`, and ran the five tests under each mutant. The record is
`docs/evidence/recorder-line-slot-mutants-2026-10-22.json`.

[Observed] Seven mutants were killed, and one survived as expected:

| Mutant | Outcome | Killed by |
|---|---|---|
| the old pattern restored | killed | the timing test alone: `Error: Script execution timed out after 1000ms` |
| CR allowed in the leading run | killed | the generated-string and slot-value tests (4) |
| CR allowed in the tail | killed | the same tests (4) |
| leading run of space and tab only | killed | the 16-character, random and slot-value tests (3) |
| leading run dropped | killed | the generated-string and slot-value tests (4) |
| a blank line accepted | killed | the generated-string and slot-value tests (4) |
| tail made lazy | killed | the slot-value test alone: same lines, shorter values |
| leading run made lazy | survived, as expected | none |

The lazy leading run is equivalent to the new pattern: it still stops only
at the first non-space.

The record keeps each mutant's old and new fragment and each failed test's
first error line. The restore mutant's error is the `vm` timeout, not a
load timeout.

### Acceptance 1: the failing provider statement version 2 read

The bead's acceptance 1 reads "The failing read of the provider v2 record
completes in under 100 ms (recorded timing)". That read is the template
read syzygy-bpyt.8.10 timed, so the bound applies to it and not to the
whole gate call. The whole call also sweeps every decisions file, and that
sweep, not the template, takes the seconds below. The whole-call timings
stand beside the template timings so the two can be compared.

[Observed] From `docs/evidence/recorder-line-slot-timing-2026-10-22.json`:
the real record (as recorded, altered by the syzygy-bpyt.8.10 corpus, and
with its last line altered), new tree `d1c03e9f`, old tree `3000698f`.

The template read is `templateFields` over `PROVIDER_V2_FORM.template`. New
is the worst of five runs; old is one run. The "whole calls" columns are the
production path: `statementsFor('redis-redis')` and `readDigestBoundActState`
over `PROVIDER_V2_FORM`, new the worst of three runs, old one run.

| Case | Template read, new | Template read, old | Whole calls, new | Whole calls, old | 1-min load (new / old) |
|---|---|---|---|---|---|
| as recorded (holds) | 0.59 ms | 0.58 ms | 7.5 s / 1.9 s | 5.8 s / 1.7 s | 28.1 / 26.5 |
| effect-widened | 0.02 ms | 112.7 s | 3.6 s / 2.1 s | 213.4 s / 106.0 s | 24.4 / 23.8 |
| limits-removed | 0.04 ms | 111.7 s | 4.2 s / 2.3 s | 212.0 s / 106.4 s | 19.8 / 20.1 |
| selection-replaced (holds) | 0.23 ms | 0.21 ms | 5.7 s / 2.1 s | 5.5 s / 1.6 s | 21.6 / 20.5 |
| withdrawal-appended | 0.02 ms | 193.4 s | 4.4 s / 2.9 s | 236.1 s / 132.7 s | 20.2 / 19.9 |
| date-field-altered | 0.01 ms | 0.01 ms | 6.4 s / 3.6 s | 7.5 s / 1.9 s | 25.5 / 25.2 |
| last-line-altered | 0.03 ms | 110.2 s | 5.9 s / 3.4 s | 284.8 s / 117.3 s | 26.3 / 26.4 |

The load column is the 1-minute load average when the `statementsFor`
measurement started. The record has the load for each measurement
separately.

- Each failing template read in the new tree took at most 0.04 ms, under
  the 100 ms bound.
- In the old tree, the four alterations after the slots took 110 to 193 s
  each. The date alteration fails before the first slot, so it is quick in
  both trees.
- Every answer, template and whole call, is the same in both trees.
- The new tree's whole calls on a failing record take what they take on the
  record that holds. The old tree's carry the stall: one template evaluation
  per `readDigestBoundActState`, two per `statementsFor`.

### The GP-Q0 differential

`scripts/differential_line_slot.mjs` ran with old `3000698f` and new
`a7a3a365`, 8 workers, in 3,052 s. Before running, it checked that the two
loaded modules carry the old and the new pattern, and that each tree's
dossier build resolves its own consent build. The record is
`docs/evidence/recorder-line-slot-differential-2026-10-22.json`.

The inputs:

- **Every recorded act.** Each of the 184 files under
  `.syzygy/governance/decisions/`, and the two rendered records below, was
  read through every template the two packages export. There are 8
  templates, found by walking the exports. Each file was read as recorded,
  altered by each of the four `PROSE_ALTERATIONS`, altered by
  `HEAD_FIELD_ALTERATION`, and with its last line altered, skipping any
  alteration that leaves the file unchanged: 905 inputs. The corpus is imported from the consent
  package's test support, `recorder-fixtures.testkit.ts` (syzygy-bpyt.8.10).
- **Line by line.** The seven records those templates are written for each
  had every non-blank line in turn appended to and deleted: 746 inputs.
  - Five of the seven are recorded.
  - The other two, the Redis no-evidence drawer and the OpenAI statement,
    have no record in the checkout. They were rendered by the real
    recorder over their artifacts' digests.
- **Readers.** Twelve readers apply a template: the digest-bound reads,
  the sign-off read, and the gate sources' D9, RFC7-20, registry-entry,
  drawer and statement reads. Each ran at two instants over 45 worlds:
  - the checkout;
  - the checkout with each rendered record added;
  - each of the seven records altered by the named corpus.

[Observed] 1,696 inputs; 14,288 answers compared; **0 differ**. The inputs
give 34 distinct answer vectors. 17 template inputs are read by some
template; the rest are refused by all of them. The slowest template input
took 11 ms in the new tree and 314.5 s in the old.

## Residuals

1. [Inferred] The argument and the checks cover the regex engine Node 24
   ships (V8 irregexp, `u` flag). A future engine change would not change
   the language. It could only change how fast either pattern runs.
2. [Observed] A whole provider statement read still takes seconds under
   this load, as it does on a record that holds. That time is the
   decisions-directory sweep, outside this bead.
3. [Observed] `docs/evidence/consent-gate-recognition-models-2026-10-21.md`
   (residual 2) and the header of `scripts/measure_slot_line_backtracking.mjs`
   give `SLOT.line` as `[^\r\n]*\S[^\r\n]*`. That was true when
   syzygy-bpyt.8.10 measured it and is not true after this change. Neither
   file is edited here:
   - the first is that bead's retained record;
   - the second's digest is carried by
     `docs/evidence/consent-gate-slot-line-timing-2026-10-21.json`.

   Read them as describing the pattern before this change.

## Re-running

```sh
(in each tree) npm ci && npx tsc -b packages/polaris-generation-consent packages/polaris-dossier
node scripts/differential_line_slot.mjs --old <base tree> --new <this tree> --out <file.json>
node scripts/measure_line_slot_reads.mjs <this tree> --out <file.json> --old <base tree>
python3 -I scripts/run_line_slot_rule6_mutants.py <this tree> --out <file.json>
npx vitest run --project @syzygy/polaris-generation-consent packages/polaris-generation-consent/src/recorder-template.test.ts -t syzygy-bpyt.8.17
```

[Observed] The three scripts are evidence tools. No battery line and no
workflow runs them: 0 hits for the three script names over
`PROJECT-STATUS.md` and the 3 files under `.github/workflows/`.
