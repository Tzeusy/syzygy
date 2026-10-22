# R-GP-IMPL-RECORDER-LINE-SLOT-1 — CC-REV-1 implementation review of syzygy-bpyt.8.17, round 1
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 18f9557f
Subject: r1-review.diff sha256 a7901624d36912a8b6486dbd39740b8fec024d7255ea680837e64076e59e1b05

Reviewer: fresh-context CC-REV-1 reviewer, default model, 2026-10-22. I did not author this change and did not
share the authoring session's context. Inputs: the brief, the subject diff, the PR body, the bead, and the
governing references named below. No observed repository was read; no credential file was opened; no bd
mutation, push, PR comment or merge was made.

Verdict basis: no finding must change the reviewed bytes before merge, and no input I found reads a different
verdict or a different captured value under the two patterns. Four notes follow (N1–N4). N1 matters for the
owner notice: the change removes the stall the bead names, but a crafted record can still stall the same reads,
quadratically, through the one template row that holds two line slots.

## 1. Subject identity checks

- [Observed] `sha256sum` of the subject file prints
  `a7901624d36912a8b6486dbd39740b8fec024d7255ea680837e64076e59e1b05`. It matches the brief.
- [Observed] In a scratch clone, `git diff 5837512f5be2cba4fa5caa7fd493b457ded744c8 18f9557f4dc4e0077492a2819b511f7eb4c717a8 | sha256sum`
  prints the same digest. `--stat` lists the 9 files the brief names (17,463 insertions, 3 deletions).
- [Observed] The PR head is `18f9557f4dc4e0077492a2819b511f7eb4c717a8` (`gh pr view 508 --json headRefOid`).
  Its parents are `41a8d3d6` (the lane) and `5837512f` (main).
- **The merge brought only main's bytes.** [Observed] `git diff 3000698f 41a8d3d6 | sha256sum` prints the same
  `a7901624…` digest. So the lane's change against its own base (`3000698f`, the #500 merge) is byte-identical
  to the subject diff against `5837512f`.
  - [Inferred from that equality] Every path outside the 9 files is `5837512f`'s at `18f9557f`. On the 9 paths, the
    two bases carry the same pre-image blobs, because the `index` lines of the two diffs are the same.
- [Observed] `3000698f..5837512f` changes 93 files, every one under `apps/three-surface-poc/` or `docs/`.
- [Observed] `5837512f..0d4d5098` (main now) changes 50 files. Under `packages/polaris-generation-consent`,
  `packages/polaris-dossier`, `.syzygy` and `openspec`, it changes only `packages/polaris-dossier/src/launched.test.ts`.
- [Observed] Tree and blob ids, by `git rev-parse <commit>:<path>`, at `3000698f`, `5837512f`, `0d4d5098`,
  `a7a3a365` and `18f9557f`:

  | Path | Ids |
  |---|---|
  | `packages/polaris-generation-consent/src` | `92b20dfb` at the first three; `616c76ea` at `a7a3a365`, `d1c03e9f` and `18f9557f` |
  | `packages/polaris-dossier/src/gate-sources.ts` | `a5ce7c22` at all five |
  | `.syzygy/governance/decisions` | `e3b60eb1` at all five |
  | `packages/polaris-dossier/src` | `1f5a0d53` at `a7a3a365`, `d1c03e9f` and `18f9557f` |

- [Observed] `gate-sources.ts` imports only `@syzygy/polaris-generation-consent`, `node:fs/promises`, `node:path`
  and `import type` from `./governed.js`.
  - [Inferred] #503's `three-surface-poc-core` changes therefore cannot reach the twelve readers, and #506 touches
    only a dossier test.
  - So `3000698f` is a valid "old" for the merged base `5837512f` and for main at `0d4d5098`. None of
    `3000698f..0d4d5098` touches a reader, a template, the recorder template module or a decisions record.
- [Observed] These files are byte-identical at `3000698f`, `5837512f`, `18f9557f` and `0d4d5098`:
  - `docs/evidence/consent-gate-recognition-models-2026-10-21.md` (blob `a5039e87`);
  - `docs/reviews/R-GP-IMPL-CONSENT-RECOGNITION-2-RAW.md` (`1b60e19c`);
  - `scripts/measure_slot_line_backtracking.mjs` (`f84cd333`);
  - `docs/evidence/consent-gate-slot-line-timing-2026-10-21.json` (`dd0cba01`).

  The #500 review's bytes stand.
- [Observed] `git diff --name-only 5837512f 18f9557f -- .syzygy openspec | wc -l` prints `0`.

## 2. Clauses relied on (quoted)

- CC-REV-1, `.syzygy/governance/policies/craft-and-care/review-and-documentation.md:18-20`: "Changes touching any of
  seven classes require review by an independent, fresh-context reviewer, and the agent performing the change never
  finally decides which classes it touches."
  - Class 4, line 37: "**security** — anything under SEC-1…SEC-5, auth surfaces, egress paths;".
  - Line 51: "**A reviewer or the owner** may reclassify at any time."
  - I do not reclassify. The change sits in the consent gate's act-record recognition (SEC-2 consent), so class 4 is
    right, and no other class is touched: no write universe, identity, observation, migration, public endpoint or
    certificate.
- CC-REV-6, same file:
  - line 167: "**Raw reviewer output** is stored unchanged before synthesis.";
  - lines 171-172: "**A useful review** names concrete risks even when accepting; rubber-stamp reviews are themselves
    findings."
- GP-Q0 part 1, `.syzygy/governance/decisions/OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21.md`:
  - lines 52-55: ""Behavior-preserving" means none of the following changes:" / "a rendered byte, a wire format, a
    refusal string or an exit code;" / "a signed or digest-bound artifact;" / "a consent, security or retention
    decision.";
  - lines 64-66, the further checks: "an old-versus-new differential over a mutated-record corpus that includes records
    with altered prose;" / "a rule-6 mutant for each predicate;" / "a non-blocking owner notice in the cycle report.";
  - lines 95-96: "Any change not listed here to what a gate accepts or refuses stops and returns to the owner."
- `AGENTS.md` at `18f9557f`, verification rules (lines 120-135):
  - 2. "No "zero / all / 100%" claim without running that exact sweep this session, confirmed by a second method.
    Enumerate remainders."
  - 4. "Read a check's output, not its exit code, and check its denominator against the whole population."
  - 6. "Mutate the input and confirm the check fails, per predicate, before trusting it".
  - 9. "A claim of absence needs a sweep with a denominator."
  - 10. "Freeze the bytes a review is bound to; any later edit retires the review."
  - 11. "An evidence record names its subject and the subject's digest; a record that names neither cannot be
    re-checked against the bytes it describes."
- `AGENTS.md` guardrail, lines 263-265: "A rule-6 evidence record must store each mutant's `old`/`new` fragment and the
  commit it ran at; ids and outcomes alone are not re-runnable, and a rebase-merge leaves the recorded commit reachable
  from no ref."
- Bead `syzygy-bpyt.8.17` acceptance (`bd show --json`, read-only):
  1. "The failing read of the provider v2 record completes in under 100 ms (recorded timing)."
  2. "Differential over every recorded act and the altered-prose corpus: 0 verdicts changed."
  3. "Rule-6 mutant restoring the ambiguous slot is killed by a timing-bounded test."
  4. "Independent default-model review raw retained; owner notice posted."
- Test-rigor bar (`th-engineering/subskills/test-rigor/SKILL.md`):
  - core rule: "A test is worth keeping only if some plausible bug makes it fail.";
  - bar 2: "Every bugfix ships a regression test";
  - bar 4: "Expected values are literals or independently derived.";
  - bar 6: "Deterministic or quarantined".

## 3. What I ran, and the results

All work was in scratch clones of `/home/tze/GitHub/syzygy` under `…/scratchpad/rev-508/`:

| Clone | Commit | Purpose |
|---|---|---|
| `new` | `18f9557f` | the reviewed tree |
| `old` | `3000698f` | the base |
| `mut` | a copy of `new` | dist-level negative controls only |

Each clone had `npm ci` and `npx tsc -b packages/polaris-generation-consent packages/polaris-dossier` run in it. My
own scripts are in `…/scratchpad/rev-508/tools/`: `eq.mjs`, `adversarial.mjs`, `ac1.mjs`, and `diff_copy.mjs`, a copy
of the lane's differential with an env pattern override and a sample filter. Node is `v24.6.0`. The 1-minute load
average, where quoted, comes from `os.loadavg()` or `uptime` at the time; the host carried other lanes throughout.

### 3.1 Equivalence, by argument

Notation:
- B is {CR, LF}.
- W is the code points `\s` matches other than B. [Observed: a scan of every code point under `u` finds 25 `\s`
  code points, all in the BMP, so W has 23 members.]
- N is the complement of `\s`.
- A is `[^\r\n]` = W ∪ N.
- Under the template regexes' only flag, `u` (`new RegExp(\`${source}$\`, 'u')`, `recorder-template.ts:24`,
  unchanged by the diff), the old slot is `A* N A*` and the new one is `W* N A*`.
- No template uses `m`, `s`, `i`, `g`, `y` or `v`. `^` and `$` therefore anchor the whole text, and U+2028/U+2029
  are ordinary members of W inside a slot under both patterns.

**Language.** [Inferred, proved here] W ⊂ A, so L(new) ⊆ L(old). Conversely, a string in L(old) has no B and at least
one N. Cut it before its first N: the prefix has no N and no B, so it is in W*. So L(old) = L(new).

**Captures, in any context.** [Inferred, proved here]
- From a slot start p, let m be the first B (or the end of the text) at or after p, and f the first N in [p, m).
- The new pattern's `W*` cannot pass f (text[f] is N) and cannot stop before f (then `\S` would face a W). So the
  split is unique, and the tail tries the ends e = m, m-1, …, f+1, in that order, once each.
- The old pattern picks its `N` at i, from the last N in [p, m) down to f, and for each i tries e = m, …, i+1. Its
  first visits to the ends are therefore e = m, …, f+1 in the same descending order; every later visit repeats an end
  it has already tried.
- The ECMAScript matcher is a pure function of (position, captures). A revisit hands the continuation the same
  position and the same capture for that group (the span p..e, whatever the internal split), so it fails again
  wherever it failed the first time.
- So both patterns return the same first success: the same end, the same capture, and the same everything after it.
  This holds whatever follows the slot (literal, another slot, a `\k<name>` backreference, or the end anchor). By
  induction over the slots left to right, `fields` and `templateFields` agree on every input.
- The slot is never inside a quantifier in a template: templates are literal text, groups and backreferences. So the
  RepeatMatcher empty-check cannot interact with it.

The lane's argument (doc comment and report, "The same slot values") is this one. I found no gap in it.

### 3.2 Equivalence, by my own checks (independent of the lane's scripts and tests)

**(a) Exhaustive, synthetic contexts.** `node eq.mjs x x contexts 4`, plain `RegExp`s with `u`.
- Alphabet of 16: `x`, space, tab, CR, LF, `"`, `|`, U+3000, U+00A0, U+2028, U+FEFF, U+0085, U+200B, U+1F600,
  U+D800, U+DC00.
- Every string up to length 4: 69,905 per context.
- Compared: `exec` groups, index and match length, with the old pattern under a `node:vm` timeout.
- [Observed]

  | Context | Strings | Matched | Differ |
  |---|---|---|---|
  | `^(?<a>P)$` | 69,905 | 39,816 | 0 |
  | `^(?<a>P)(?<b>P)$` | 69,905 | 31,815 | 0 |
  | `^(?<a>P) (?<b>P)$` | 69,905 | 2,560 | 0 |
  | `^(?<a>P)\n\k<a>$` | 69,905 | 8 | 0 |
  | `^(?<a>P)\r?\n(?<b>P)$` | 69,905 | 2,688 | 0 |
  | `^(?<a>P)(?:x\|y)$` | 69,905 | 2,696 | 0 |
  | table row, tab literal, three ideographic | 69,905 each | 0 each (too short to match) | 0 |

- Every one of the 25 `\s` code points, in a space-separated two-slot context, over every string up to length 5 of
  {x, that code point, space, LF}: "spaces": 25, "total": 34125, "differ": 0.

**(b) Random, structured contexts.** `node eq.mjs x x random-contexts 20000`. Seven contexts, 20,000 strings each,
half built to the context's shape from tokens including `" | "`, `" |`, `" by selecting the`, CR, LF and the blanks.
[Observed]

| Context | Matched | Differ |
|---|---|---|
| table-row `^"(?<a>P)" \| "(?<b>P)" \|$` | 2,647 | 0 |
| tab-literal | 2,340 | 0 |
| three-ideographic | 1,323 | 0 |
| space-separated | 4,962 | 0 |
| three-adjacent | 4,599 | 0 |
| repeated-then-slot | 2,387 | 0 |
| opening-line | 4,923 | 0 |

**(c) The 8 exported templates.** `node eq.mjs <old> <new> templates 2000`.
- Enumerated by form, not by export walk, then de-duplicated by object identity: D9, RFC7-20, drawer, the two
  statement forms, the provider v2 template (the statement form's exempt record), the v1 sitting template held as
  provider v2's exempt record, and the sign-off. 8 objects.
- Slot names were read by rendering through a `Proxy`. Slot types were checked by a clean round trip.
- Each template got 2,000 records: random slot values over 32 tokens (all the blanks, `"`, `|`, `" | "`, `" |`,
  `" by selecting the`, `"; the selection is the`, lone surrogates, astral), and 65% then mutated 1–3 times.
  Mutations: whole record to CRLF, one line given a CR, a line deleted or duplicated, an edit inside a quoted line, or a
  random insert, replace or delete.
- Compared: `JSON.stringify([fields, templateFields])`, with the old reads batched under a `vm` timeout.
- [Observed] `{"templates":8,"timeouts":0}`, and per template:

  | Template | Read | Refused | Differ | CRLF records | Raw reads with a shifted line value |
  |---|---|---|---|---|---|
  | d9 | 353 | 1,647 | 0 | 483 | 30 |
  | rfc7-20 | 330 | 1,670 | 0 | 441 | 30 |
  | drawer:redis-redis | 353 | 1,647 | 0 | 445 | 28 |
  | stmt:redis-redis:0 | 355 | 1,645 | 0 | 447 | 33 |
  | provider v2 (stmt 0 exempt) | 260 | 1,740 | 0 | 415 | 12 |
  | stmt:redis-redis:1 | 358 | 1,642 | 0 | 463 | 29 |
  | provider-v2:exempt0 (v1 sitting) | 310 | 1,690 | 0 | 449 | 21 |
  | signoff | 334 | 1,666 | 0 | 422 | 3 |

  The last column counts records whose raw read gives a line slot a value other than the one rendered: the
  label/description split moved, or an edit landed inside a slot. Those are the ambiguous captures where a capture
  difference would show.
- **Negative controls on this check** (rule 6). The same command against `mut`, whose compiled `SLOT.line` I replaced
  in `dist/recorder-template.js`:
  - tail made lazy (`[^\S\r\n]*\S[^\r\n]*?`): differ 27, 26, 34, 32, 11, 32, 16 and 0. The 0 is the sign-off, whose
    line slots each end at a line's end, so laziness is equivalent there.
  - leading run dropped (`\S[^\r\n]*`): differ 251, 234, 230, 257, 196, 250, 217 and 220.

  The check detects both.

**Result.** Over 663,270 exhaustive context strings (9 × 69,905 + 34,125), 140,000 structured strings and 16,000
template records, 819,270 inputs in all: 0 differences. [Observed] My own checks therefore agree with the proof. I found no input whose verdict or captured value
differs.

### 3.3 Termination (adversarial inputs), new tree versus old

`node adversarial.mjs <tree> <sizes> 60000`. Each case renders a template with every line slot shaped as named
(other slots fixed and valid), reads it (`good`), and reads it again with its last byte replaced (`bad`, failing at the
last byte), inside a 60 s `vm` timeout. Load 23–29. [Observed]

| Template | Line-slot shape | L | Record bytes | New tree, bad | Old tree, bad |
|---|---|---|---|---|---|
| provider-v2 | label = `x" \| "` repeated, others `x` | 100 | 4,358 | — | 166.6 ms |
| provider-v2 | same | 1,000 | 5,258 | 4.9 ms | >60 s (timeout) |
| provider-v2 | same | 10,000 | 14,258 | **252.7 ms** | not run |
| provider-v2 | same | 100,000 | 104,258 | **16,079 ms** | not run |
| d9 | same | 10,000 | 13,620 | **396.0 ms** | not run |
| d9 | same | 100,000 | 103,620 | **17,449 ms** | not run |
| provider-v2 / d9 / signoff | every line slot `x` × L | 100,000 | ≈300–400 KB | 16.6 / 7.3 / 10.5 ms | provider-v2 >60 s at L = 100 |
| provider-v2 / d9 / signoff | every line slot `x ` × L/2 | 100,000 | ≈300–400 KB | 18.7 / 12.2 / 16.0 ms | provider-v2 47.7 s at L = 100 |
| provider-v2 / d9 / signoff | every line slot blanks × L then `x` | 100,000 | ≈300–400 KB | 20.0 / 11.4 / 37.3 ms | ≤ 23.5 ms |
| synthetic `{a} {b} {c} {d}\nEND\n` (not exported) | `x ` × L/2 | 1,000 | — | 21,786 ms | >60 s |

- [Observed] The new slot is linear in every shape I tried except the one row in 7 of the 8 exported templates that
  holds two line slots: `| "{label}" | "{description}" |`. The sign-off has no such row.
- [Inferred, from the regex] There, the label may end before any `" | "` in the line, and for each such end the
  description scans to the line's end: about L × k steps for k separators. The measured growth fits that: 10× the
  length, 64× and 44× the time.
- Long blank runs, long non-space runs and "near-match at the last byte" are linear.
- The old pattern is far worse on every shape but the blank run. The change is a strict improvement here too; see N1.

### 3.4 AC1, reproduced

`node ac1.mjs <tree> 20`: `templateFields` over `PROVIDER_V2_FORM.template`, on
`.syzygy/governance/decisions/DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md` (4,795 bytes, the same at every commit
compared) and its alterations. Each run is wrapped in `vm.runInNewContext`, so the times include creating a context.

[Observed] New tree (load 18.6), worst of 20:

| Case | Answer | Worst |
|---|---|---|
| as recorded | read | 5.058 ms |
| effect-widened | refused | 2.456 ms |
| limits-removed | refused | 3.232 ms |
| selection-replaced | read | 1.852 ms |
| withdrawal-appended | refused | 1.167 ms |
| date-field-altered | refused | 0.917 ms |
| last-line-altered | refused | 1.468 ms |
| last-byte-altered (mine) | refused | 2.988 ms |
| CRLF (mine) | refused | 20.98 ms |

[Observed] Old tree, one run each:
- `{"case":"date-field-altered","said":"refused","runs":1,"maxMs":2.502,…,"load1":"17.4"}`;
- `{"case":"last-line-altered","said":"refused","runs":1,"maxMs":93796.683,…,"load1":"16.0"}`.

The lane's timing record (`docs/evidence/recorder-line-slot-timing-2026-10-22.json`) agrees with its table and its
prose:
- failing template reads in the new tree at most 0.04 ms, against 110.2–193.4 s in the old;
- "answersAgree": true;
- 44 load samples, 19.8 to 36.54.

### 3.5 Rule 6, re-run

`python3 -I scripts/run_line_slot_rule6_mutants.py <mut> --out <tools>/mutants-rerun.json`, at `18f9557f`. The subject
digests it recorded equal the lane's record (`070db202…` for `recorder-template.ts`, `6022b23b…` for the test file),
so the code under test is byte-identical to `a7a3a365`'s. [Observed]

- `baseline {'selected': 5, 'passed': 5, 'failed': [], 'wallSeconds': 8.1}`.
- `restore-ambiguous killed ['the line slot (syzygy-bpyt.8.17) refuses a record that fails after four long line slots within a second']`.
  Its first error line is `Error: Script execution timed out after 1000ms`.
- `tail-lazy killed`, by the slot-value test only.
- `lead-lazy survived []`.
- `totals {'mutants': 8, 'asExpected': 8, 'killed': 7, 'restoreAmbiguousKilledByTimingTestAlone': True}`.
- The tree was clean afterwards (`git status --porcelain --untracked-files=no` printed 0 lines).

`lead-lazy` (`[^\S\r\n]*?\S…`) is equivalent: a lazy blank run can still stop only at f.

### 3.6 The GP-Q0 differential (AC2)

- **Counts.** [Observed] `node scripts/differential_line_slot.mjs --old <old> --new <new> --count`, at `18f9557f`:
  `{"jobs":1696,"byInput":{"templates:file":905,"templates:line":746,"readers:world":45},"decisionsFiles":184,"templates":8,"readers":12,"subjects":7}`.
  This equals the record's totals. The record also gives 14,288 answers compared, 0 mismatches, 34 distinct answer
  vectors, and `templatesRead` 17.
- **Corpus coverage.**
  - [Observed] Every file under `.syzygy/governance/decisions/` (184; the tree is `e3b60eb1` at the old, reviewed and
    main commits) is run through every template.
  - The seven subject records are the only files the readers apply a template to (`findActRecord` applies the form's
    template to `form.file` and an exempt template only to `exempt.file`). Of those, five are recorded and two are
    recorder-rendered.
  - The altered-prose corpus is `PROSE_ALTERATIONS` (effect-widened, limits-removed, selection-replaced,
    withdrawal-appended) and `HEAD_FIELD_ALTERATION`, imported from `--new`'s `dist/testing.js`, which this diff leaves
    unchanged. It also adds a last-line alteration and a line-by-line append/delete.
  - So "every recorded act and the altered-prose corpus" is met.
- **Sampled re-run, old versus new.** `SAMPLE=1 node tools/diff_copy.mjs --old <old> --new <new> --workers 6`, the
  lane's script with a filter. It keeps every input except the provider v2 subject's: of those it keeps every 10th
  template input (13 of 129) and the last-line-altered world (1 of 6).
  - That is 1,575 of the 1,696 inputs: 899 file, 636 line, 40 world.
  - Reason for the sample: the 121 inputs left out are the old pattern's slowest. The lane's record puts them at
    14,554 s of old template time and 3,828 s of old reader time, up to 18 min for one world. Every one is a refusal
    in both trees there. Their equivalence is covered by 3.1 and 3.2(c).
  - Trees, as the script's guard recorded them: old `3000698f`, clean, `[^\r\n]*\S[^\r\n]*`; new `18f9557f` (the
    reviewed commit, not the lane's `a7a3a365`), clean, `[^\S\r\n]*\S[^\r\n]*`. Each dossier build resolves its own
    consent build.
  - Result, [Observed]: `1575 inputs, 13240 answers compared, 0 mismatches, 32 distinct answer vectors`. Exit 0, 6
    workers, 1,626 s wall.
  - `templatesRead` is 16. Old template maximum 399,586 ms against new 10 ms; old reader-world maximum 1,129,042 ms
    against new 168,396 ms. The new tree's reader time is the decisions sweep under load (lane residual 1).
  - Against the lane's record: for each of the 32 answer keys (8 templates, 12 readers × 2 instants), every answer
    label my run produced is in the record's `answersPerKey` for that key (0 keys with a label the record lacks).
- **Sensitivity of the lane's differential** (rule 6, negative control).
  - Method: `TEMPLATES_ONLY=1 node tools/diff_copy.mjs --old <new> --new <mut>` over the lane's 1,651 template inputs,
    with `mut`'s compiled slot replaced. Reader worlds were not run in this control.
  - [Observed] For the slot made lazy, the leading run dropped, and a blank line accepted (`[^\S\r\n]*[^\r\n][^\r\n]*`),
    each printed: `1651 inputs, 13208 answers compared, 0 mismatches, 18 distinct answer vectors`.
  - [Observed] For a bounded tail (`[^\S\r\n]*\S[^\r\n]{0,10}`): `1651 inputs, 13208 answers compared, 15 mismatches, 18 distinct answer vectors`.
  - So the comparison works, but the corpus cannot tell apart the changes that matter most here. See N2.

### 3.7 Suites and checks at `18f9557f`

Each was run with a private `TMPDIR` under `/tmp/r508-<n>`. [Observed]

- `npx vitest run --project @syzygy/polaris-generation-consent packages/polaris-generation-consent/src/recorder-template.test.ts`:
  - "Tests  14 passed (14)";
  - the five new tests took 102, 127, 73, 207 and 6 ms.
- `npx vitest run --project @syzygy/polaris-generation-consent`: "Test Files  5 passed (5)", "Tests  419 passed (419)".
- `npx vitest run --project @syzygy/polaris-dossier`: "Test Files  29 passed (29)", "Tests  1195 passed | 1 skipped (1196)".
  - Together with the consent project, that is the PR's "1614 passed, 1 skipped".
- `npm run typecheck`: exit 0. The log holds only the 4-line npm header.
- `python3 scripts/check_governance.py`: exit 0, "32 OK, 21 WARN, 0 FAIL (53 checks) — counts derived, not asserted".
  `FAIL` appears only in that summary line.
- `python3 scripts/check_quotations.py`: exit 0, "OK    QC-1  a quotation beside a path:line locator was said by that
  file — 33 quotations examined in 15 of 924 .md files scanned … 0 findings".
- Not run: the canonical 110-command battery. The PR's "commands=110 nonzero=0" is lane-reported, [Unknown] to me.

### 3.8 Evidence records (rules 6 and 11)

[Observed] `sha256sum` of the committed scripts equals the digests each record carries:
- `differential_line_slot.mjs` `36a8fba4…`;
- `measure_line_slot_reads.mjs` `6b804e9c…`;
- `run_line_slot_rule6_mutants.py` `4ce9d52c…`.

[Observed] My builds' `dist/recorder-template.js` hash to the records' `recorderTemplateJsSha256`: `4f9d4362…` (new)
and `b20a4e74…` (old). The old source hashes to `0066184f…`, as recorded.

- **Mutant record.** It stores per mutant `old`, `new`, expected outcome, outcome, failed tests and first error line,
  plus the subject commit (`a7a3a365`) and the file and test digests. It meets the guardrail.
- **Commits that will not survive.** `a7a3a365` and `d1c03e9f` will become unreachable after a rebase-merge. The
  records stay re-checkable through the file digests they carry, which equal `18f9557f`'s.
- **Differential.**
  - It names both trees by commit and by the source and compiled digests of `recorder-template`.
  - It names the corpus root `old` (`3000698f`, a main merge commit) and the alteration module (path and tree, no
    digest; the module is unchanged by this diff).
- **Reproduction.** My re-runs reproduce the mutant record exactly and the differential's counts. The timing record
  reproduces within load: same answers, the same order of magnitude.

### 3.9 The report's correction

[Observed] Two files still state the old pattern as the current `SLOT.line`:
- the 2026-10-21 report's residual 2 (line 345-346: "`SLOT.line` is `[^\r\n]*\S[^\r\n]*`");
- `scripts/measure_slot_line_backtracking.mjs:8`.

[Observed] `git grep -l -F '[^\r\n]*\S[^\r\n]*'` at `18f9557f` returns 6 files. The other four are this change's own
files, which name the old pattern as the old one. So the new report's residual 3 names the right two files and
describes them accurately. It leaves out one consequence: see N3.

## 4. Findings

No blocking findings (F-series): none.

### N1 — The one template row with two line slots is still quadratic, so a crafted record can still stall the gate; the report's "nothing multiplies across slots" is false for that row

- **Severity:** note, medium. Availability on the consent gate (class 4). It changes no verdict and no capture. It was
  there before this change, and the change shrinks it by orders of magnitude.
- **Evidence:** 3.3. The row `| "{label}" | "{description}" |` appears in 7 of the 8 exported templates. In the new
  tree, a record that fails at its last byte, after a label holding `" | "` k times, refuses in:
  - 252.7 ms at a 14 KB record, provider v2;
  - 396.0 ms at 13.6 KB, D9;
  - 16.1 s and 17.4 s at about 104 KB.
- **Quoted overstatements:**
  - [Observed] The report says: "[Inferred] The new pattern has one way to match a given end, so each slot tries each
    end once and the literal after it rejects all but the few where that literal appears; nothing multiplies across
    slots." That does not hold when the literal after the label (`" | "`) appears many times on the line.
  - [Observed] The PR title says "so a failing record refuses in milliseconds".
  - The production doc comment makes no such claim and is accurate.
- **Failure scenario:**
  - Any writer of `DOSSIER-AGENT-PROVIDER-V2-REDIS-ANTHROPIC-ACT.md`, or of the other sitting-form records the
    readers apply a template to, agent sessions included, is the bead's own threat model. Such a writer puts a label
    row of a few hundred KB of `" | "` into the record with any later byte wrong.
  - Every `readDigestBoundActState` over it then spends tens of seconds to minutes refusing, and `statementsFor` twice
    that (two template evaluations). [Inferred: extrapolated from 16 s at 100 KB on the quadratic fit; not measured
    past 104 KB.]
  - The commands syzygy-bpyt.8.10 named (preflight, init, reverify, session-handover, session-statement) are stalled
    again. Every such read still refuses.
- **Proposed fix (follow-up bead, not these bytes):**
  1. The owner notice should say the stall is closed for the 8.10 corpus and the real record, and reduced but not
     closed for a crafted label row. The dispositions record should mark the report's sentence as wrong for that row,
     quoting it.
  2. A follow-up class-4 bead should make that row linear without changing the language or the captures. The
     description's end is fixed by the line's final `" |`. Neither slot is repeated by a backreference, so what follows
     the row does not depend on where the label ends. One right-to-left scan for the last `" | "` that leaves a
     description holding a non-space reproduces the regex's greedy split. Alternatively, a size bound on act records
     would change verdicts for oversized records, which GP-Q0 sends to the owner.
  3. Extend the timing-bounded test to a real exported template's label row, so the row is pinned too.

### N2 — The GP-Q0 differential cannot tell apart the slot changes that matter here, and records no negative control

- **Severity:** note, low to medium (evidence strength). AC2 stands: the claim is "0 verdicts changed", and the proof,
  the property tests and my independent check all support it.
- **Evidence:** 3.6.
  - Over its 1,651 template inputs, three plausible slot mutants each give "0 mismatches": lazy tail (changes label
    and description captures), leading run dropped (refuses a selection that starts with a blank), and blank accepted
    (accepts a blank selection). Only a gross bounded-tail mutant gives "15 mismatches".
  - The record itself shows how little of the corpus is read: `templatesRead` 17 of 1,651, 3 distinct answers per
    sitting/provider template (6 for the sign-off), and 34 distinct answer vectors over 1,696 inputs.
  - The corpus has no label holding `" | "`, no line slot that starts with a blank, and no blank slot.
  - Rule 6 asks that a check be shown to fail on a mutated input "before trusting it". The record and report show no
    such run for the differential. The property tests were mutation-tested; the differential was not.
- **Failure scenario:** a later change to `SLOT.line` or `recorderTemplate` that moves a label/description split, or
  admits a blank owner selection, passes this differential with "0 differ". A reader who cites "0 of 14,288" as the
  evidence of capture equivalence then overstates it.
- **Proposed fix:**
  1. The dispositions record should state that the capture-equivalence evidence is the structural argument, the five
     property tests (which kill the lazy-tail, leading-run and blank mutants) and this review's check (3.2(c), with its
     negative controls). The differential's role is "no recorded act or altered-prose record changes verdict".
  2. If the script is reused, add corpus records whose label holds `" | "`, whose slot starts with a blank, and whose
     slot is blank, plus one recorded negative-control run that must report mismatches.

### N3 — #500's timing tool now measures the new slot twice

- **Severity:** note, low (rule 11 re-runnability of #500's evidence).
- **Evidence:** [Observed] `scripts/measure_slot_line_backtracking.mjs:33` takes `SLOT` from the built consent package,
  and `:53` times `['SLOT.line', SLOT.line]` against `['unambiguous', UNAMBIGUOUS]`. At or after this change, both are
  `[^\S\r\n]*\S[^\r\n]*`. The new report's residual 3 says the header comment is stale. It does not say that a re-run
  no longer reproduces `docs/evidence/consent-gate-slot-line-timing-2026-10-21.json`.
- **Failure scenario:** someone re-checks #500's 30–93 s figures by re-running the script on main, gets 0 ms for both
  patterns, and reads it as a contradiction of #500's record or as a broken tool.
- **Proposed fix:** in the dispositions record, say that #500's timing reproduces only at a commit before `40d5de76`
  (for example `3000698f`). The script cannot be edited: its digest is carried by its timing record.

### N4 — One load figure in the report has no record

- **Severity:** note, low (rule 11).
- **Evidence:** [Observed] The report says "Forty-nine `uptime` samples, taken once a minute while the differential ran
  and not retained, ranged from 18.6 to 54.2." No retained file carries these figures; the differential record's
  `pool` holds no load. [Unknown] whether the figures are right.
- **Failure scenario:** a reader takes 54.2 as the measured worst-case load for the differential's timings, and no
  record exists to check it against.
- **Proposed fix:** in the dispositions record, either retain the samples or mark the sentence as unretained and not
  evidence. The timing record's own 44 load samples (19.8–36.54) are retained and suffice.

## 5. Every changed output, or the evidence that there is none

None. [Observed and Inferred, as labelled]

- **Verdicts and captured values.** [Inferred] The proof in 3.1 shows they are unchanged. [Observed] So do:
  - my checks in 3.2: 0 differences over 819,270 strings and records;
  - the lane's differential: 0 of 14,288;
  - my sampled re-run of it (3.6);
  - the five property tests.
- **Refusal strings.** `fromTemplate` calls the same `refuse()` whichever pattern is in force. The lane's differential
  and my sampled re-run compare the readers' whole answers (JSON, `why` strings included) by sha256.
- **Bytes.** No rendered byte, wire format, exit code, or signed or digest-bound artifact changes:
  - 0 files under `.syzygy/**` and `openspec/**`;
  - the 2026-10-21 report, the #500 raws and #500's scripts and records are byte-identical (section 1);
  - the three new scripts run in no battery line or workflow: 0 hits for their names over `PROJECT-STATUS.md` and the
    3 files in `.github/workflows/`.
- **Speed.** What changes is how fast a non-matching record is refused (3.3, 3.4). That is availability, not a decision.

## 6. Verdict per acceptance criterion

1. **AC1: met**, under the coordinator's agreed reading (the template read of the failing v2 record).
   - [Observed] Failing reads take at most 3.2 ms here (vm context creation included) and at most 0.04 ms in the lane's
     record, against 93.8 s here and 110–193 s in the lane's record for the old tree.
   - Under a wider reading, "any failing provider v2 record", it is not met: a crafted 14 KB record takes 252.7 ms
     (N1). That is a pre-existing residual of the template, not of the slot.
2. **AC2: met.** 0 verdicts changed over every recorded act and the altered-prose corpus, in the lane's run and in my
   sample. The evidence for capture equivalence rests on 3.1–3.2, not on the differential (N2).
3. **AC3: met.** [Observed] The restore mutant is killed by the timing-bounded test alone, with
   `Error: Script execution timed out after 1000ms`, reproduced at `18f9557f`. The other six non-equivalent mutants are
   killed, and the one equivalent mutant survives.
4. **AC4: in progress.** This raw is the independent default-model review. The owner notice is not in these bytes,
   [Unknown]; it should carry N1.

## 7. Test quality

Judged against the test-rigor bar.

- **Regression test (bar 2): present.** `refuses a record that fails after four long line slots within a second` fails
  on the pre-fix slot by the vm bound (3.5).
  - The pass margin is wide: 0.16 ms worst of 20 under load 30.4 in the lane's record; 6 ms for the whole test in my run.
  - The kill margin is wide: 711 s for the old slot on that record.
  - [Inferred] Flake risk at 1,000 ms is negligible. Context creation happens before the `vm` watchdog starts, and the
    measured work is three to four orders of magnitude under the bound.
  - The 20 s `within` bounds on the old-pattern batches in the property tests have a margin of about 100× (each test
    took ≤ 207 ms in my run).
- **Expected values (bar 4): literal and independently derived.** I re-derived each:
  - 69,905 = (16^5 − 1)/15;
  - 33,990 = Σ_{n=1..4} (14^n − 9^n), 14 non-break and 9 blank code points in the alphabet;
  - 502 = Σ_{n=1..8} (2^n − 1).
- **Vacuity guards: present.** `accepted` lies in (400, 3600), and `matched > 1000` and `refused > 1000` over 9,000 records.
  `blanks` is built in `beforeAll` (the guardrail against a throw at describe time), and the RNG is seeded.
- **Mutation sensitivity (core rule): shown.** Every non-equivalent mutant is killed (3.5). The lazy tail is caught only
  by the multi-slot test, which is the right test for it.
- **Gaps (non-blocking):**
  - None of the five tests runs a real exported template; the multi-slot test uses six synthetic ones. The real
    templates' label row is exactly where N1 lives, and the lane's differential does not exercise its ambiguity (N2).
  - The second exhaustive test asserts its accepted count (502) but not its population (87,381). The accepted count
    pins the population well enough.
- **Growth (bar 10).** Net test delta +5, all in the nearest existing file. Each catches a plausible bug no earlier test
  caught: 9 → 14 tests, the 9 earlier ones unchanged except the import line.

## 8. Cleanup

- The scratch clones (`new`, `old`, `mut`) under `…/scratchpad/rev-508/` and the private TMPDIRs `/tmp/r508-1`,
  `/tmp/r508-2` and `/tmp/r508-3` were deleted after this file was complete. The only files kept are this raw and my
  tool scripts and outputs under `…/scratchpad/rev-508/tools/`.
- No worktree under `/home/tze/GitHub/syzygy/.worktrees/` was touched.
- No process was killed by pattern. My own background runs ended on their own or were stopped by their task ids.
