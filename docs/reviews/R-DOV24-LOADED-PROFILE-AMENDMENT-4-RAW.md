# R-DOV24-4 — confirmation review of PR #123
Verdict: CONFIRM WITH EXCEPTIONS
Reviewed commit: 1d5966c3fc40e3e54b5aff32757cc024dceaeb34
Manifest sha256: aa2bf7e1d5dd2e016a72369ab9003b3040597c5022c4ffe986acfe11251713d5

Fresh-context confirmation review, 2026-09-27. Subject: the candidate package
`.syzygy/governance/contracts/candidates/pwb-registry-loaded-profile-amendment/`
(6 files) and `scripts/build_pwb_registry_loaded_profile_amendment.py`, at
the commit above on `agent/tier4-dov24`. I ran everything in a detached
worktree and in `git archive` copies, and left the branch and the main
checkout untouched. There are no revise findings; the six findings below are
notes.

## Round-3 findings — resolution

| Finding | Status | How I checked it |
|---|---|---|
| F1 (revise): bytes outside the hunks changed | **Resolved** | I rebuilt the subject from `git archive` of the commit. I applied `.18`'s patch (sha256 `2356b9ed…`, equal to `.18`'s manifest row), then this patch, and got sha256 `aa2bf7e1d5dd2e016a72369ab9003b3040597c5022c4ffe986acfe11251713d5`, equal to this manifest's row. `diff` of the `.18`-applied file against the proposed file prints exactly `3c3` (registryVersion), `10c10` (observerVersion) and `261a262,554`, one pure insertion. Neither file contains a `\u` escape. Parsed: the six bound grammar keys are equal; only `registryVersion`, `observerVersion` and the six added keys differ. The five byte mutants are in `--selftest` (builder:1795–1807), and I killed my own trailing-space mutant on a base line (T5) and a changed line on each side of the insertion (lines 261 and 555). The claim at OWNER-DECISION-PACKET.md:48–50 holds for these bytes; see N-A for the inserted block. |
| F2 (revise): the second heading of `v1-scope` was not probed | **Resolved** | builder:1350–1375 now loops over every heading (`enumerate(headings)`). Builder mutant B3 (`headings[:1]`) is killed by `--selftest`. JSON mutant T15 (the two v1-scope headings swapped) is killed by the witness. |
| N1: extra keys | **Resolved** | There are key sets for `pillarRootTable` (builder:505–507), tree populations and `sourcePopulation` (533–534), and bindings (540–542). Builder mutant B6 (the pillarRootTable key set dropped) is killed. |
| N2: redundant pillar, padded TOML name, order | **Resolved** | The pillar-sharing rule is at builder:616–622 and the bare-key rule at 623–625. Builder mutants B4 and B5 are killed. JSON mutants T8 and T9 (`Name`, `Butler`) are killed. Order is stated free at OWNER-DECISION-PACKET.md:84–90. My order mutants T21 (pillars) and T22 (sourceRules) are killed by the code-constant check, and neither list is among the four the packet calls order-free. |
| N3: loose or strict clauses, and the consistent-rewrite gap | **Resolved** | (a) `LINK` (extraction.ts:324) takes only `"…"` titles, so the sentence is correct. The single-quoted probe is at builder:1324; builder mutant B7 inverts it and `--selftest` fails. (b) `TOML_TABLE` does not match `[[x]]`, so the sentence is correct and the probe passes. (c) `declaredPillarRoots` reads the table, then every link in the whole text, so the sentence is correct. JSON mutants T10 and T11 (either clause dropped) are killed by the pin. (d) The gap is stated at OWNER-DECISION-PACKET.md:77–82. |
| N4: P-82 recorder columns | **Resolved** | The quotes and columns are verified below under the attribution sweep. |
| N5: stale review sentence | **Resolved** | SEMANTIC-DELTA.md, Review section, ends with a dated "*Corrected 2026-09-27 (round-3 note N5)*" note. The stale sentence is kept quoted. The round counts it gives match the three raws' heads and headings: R1–R7 plus N1–N5; D1–D3 plus D4–D5; F1–F2 plus N1–N5. |

The round-2 D5 behaviours and the N3 sentences check out against
`project-shape-extraction.ts` and `project-shape-manifest.ts`. The
sentences state correctly `ATX`, the `TOML_TABLE` single-bracket form, the
single-backtick `LEADING_CODE`, the first-table-only root read, the
level-free `headedTable` match, and the catalog context equal to the
heading text. N-B and N-C list the remaining omissions.

## New findings

### N-A — note — the inserted block's bytes are checked only after parsing, so a shadowed duplicate key passes

`byte_findings` (builder:424–457) counts one insertion (445–447, 455) but
never looks at its content. Everything else parses the document, and
`json.loads` keeps the last of two duplicate keys. I ran three mutants with
the manifest row regenerated, each through the full battery
(unchanged/byte/structure/spec/code/behaviour). All three **survived**:

- T1: a `"rootIndex": {"path": "BOGUS.md"}` member placed before the real one;
- T2: `"container": "every-level-2-section"` placed before row 0's real `container`;
- T3: a false `"tree-path"` sentence placed first in `containerShapes`.

Blank-line reformatting inside the block (T4) also survived; it is harmless.
The current bytes contain no duplicate key: I checked both files with an
`object_pairs_hook`, and found 0 duplicates. So the statements hold for the
bytes under review:

- OWNER-DECISION-PACKET.md:48–50 ("outside the two version lines and the one
  inserted block … The builder checks both the parsed values and the bytes");
- SEMANTIC-DELTA.md:79–80;
- REVIEW-BRIEF.md:72–75.

Any later redraft is protected only by the review of the frozen bytes. A
strict duplicate-key refusal in the parse would close this.

### N-B — note — three item-key sentences omit the trim the code applies

`declarationKey` is `nfc(value.trim().replace(/\s+/g, ' '))`
(extraction.ts:326), and the topology key is `${ordinal}:${nfc(label.trim())}`
(extraction.ts:519). I ran the real code under Node:

- `1. **  A  b  ** rest` gives the key `A b`;
- `| ** A ** | x |` gives `1:A`.

The sentences say only "NFC-normalized with whitespace runs collapsed" for
leading-bold and leading-bold-or-code (builder:168–175), and nothing about
trimming for ordinal-and-label (builder:183–185). Read literally, they give
` A b ` and `1: A `. The `whitespace runs collapsed` probe (builder:1303)
uses `**A  b**`, which cannot tell the two apart. The existing gap statement
(OWNER-DECISION-PACKET.md:77–82, "Nor can a check show that the code has no
rule these fields leave out") covers this, so it is a note. It is the same
class as round-2 D5.

### N-C — note — CRLF stripping is unstated

`parseDoc` strips a trailing `\r` from every line (extraction.ts:160). Under
Node, a CRLF `vision.md` extracts `principle` `A` exactly as LF does.
Neither `sharedReadingRules` nor `headingMatch` says this. It is shared and
not per-project, so it belongs in `sharedReadingRules`, which claims to list
"the reading rules every project shares" (SEMANTICS at builder:247 onward;
prop.json:553).

### N-D — note — "a space or tab" before a link title is one-or-more in code

`LINK` takes `[ \t]+` (extraction.ts:324). Under Node,
`[t](t.md \t  "x")` reads the key `t`. The first-cell-link-text sentence
(builder:179) says "optionally with a space or tab and a title". This is
minor and in the looser-code direction, like round-3 N3.

### N-E — note — `--selftest` does not guard the presence of the new N3 probes

Removing the `[[other]]` probe (builder mutant B8) leaves `--selftest`
passing, at 262 predicates. So does removing the link-before-table probe
(B9, 267 predicates). What catches their removal is the stated probe count,
"123 probes" (OWNER-DECISION-PACKET.md:64), which I re-derived as 123 with
`len(probes(g))`. Nothing pins that count. This is the same class as the
disclosed consistent-rewrite gap, which only a diff review closes.

### N-F — note — `--selftest` has no mutant for a changed base line next to the insertion

Builder mutant B2 lets a multi-line `replace` count as the insertion. It
survives `--selftest`: all five byte mutants are still caught through
`inserts != 1` or the version-pair rule. The unmutated `byte_findings` does
kill my adjacent-line mutants: a trailing space on base line 261 or 262
gives "bytes outside the permitted hunks differ … found 0". So the check is
sound today, but its selftest would not notice this regression.

## Checks run

**`check_governance` at the worktree.**

- Default run: "32 OK, 20 WARN, 0 FAIL (52 checks)".
- `--selftest`: "282 fixtures, 0 failing".
- The WARN set is the same as at base `96ee305` apart from CG-1f's
  reference count (203 against 202), which has 0 findings.

**Builder at the worktree.** `--check`, `--selftest` ("268 predicates") and
`--diff` all exit 0.

**Builder in the three states.** Each state is a `git archive` copy.

- **`.18` pending** (subject `0765f4d5…`): `--check` 0, `--selftest` 268,
  `--diff` 0. `--apply --at-adoption` exits 1: "the .18 act has not been
  applied".
- **`.18` applied** (subject `2356b9ed…`): `--check` 0, `--selftest` 268,
  `--diff` 0. `--apply --at-adoption` succeeds and the subject then hashes to
  `aa2bf7e1…`.
- **This package applied**: `--check` 0, `--selftest` 268, `--diff` 0.
  `--apply --at-adoption` exits 1: "already carries this package's bytes".
- `--apply` without `--at-adoption` exits 2 in both refusing states.
- All three `--diff` outputs are byte-identical: md5 `c6390fe4…`, 320 lines.

**`check_docs_review_campaign_partition.py`.** "total=251 assigned=251
raw=226 other=25 unmatched=0 overlaps=0".

**Row digest.** I re-derived it independently, as recorded under F1.

**Mutants.**

- **JSON.** There were 43 text-level mutants of the proposed bytes plus 2
  adjacent-line byte mutants. Each ran through the full battery with the
  manifest regenerated.
  - 41 were killed.
  - 4 survived: T1–T3 (N-A) and T4 (harmless reformatting).
  - The killed mutants include one per `--check` claim I could test:
    - E1: a heading literal absent from the spec;
    - E2: a consistent roster rename, caught by the code constants;
    - E3: the catalog row given the principle's key sentence;
    - E4: the vision success row given another row's shape;
    - E5: pillars swapped across bindings;
    - T18: an unread field on a row;
    - T36: the ordinal prefix changed;
    - T28: a *true* trim clause added, which the pin kills.
- **Builder.** There were 11 mutants, each run under `--selftest`. 8 were
  killed. 3 survived: B2 (N-F), B8 and B9 (N-E).

**`--check` claims tested.** These claims are literally true under the
mutants above:

- the builder docstring (builder:25–39);
- OWNER-DECISION-PACKET.md:48–82;
- the round-3 disposition rows (OWNER-DECISION-PACKET.md:328–336).

The exception is the inserted-block qualification in N-A. I re-derived two
figures: 17 round-1 mutants (M1–M18 without M8) and 123 probes.

## Owner-attribution sweep (criterion 7)

I ran Python `re`, case-insensitive,
`\b(rul(?:ing|ings|ed)|chose|decided|answer\w*|you|your)\b`, over 5 files:

| File | Hit lines |
|---|---|
| OWNER-DECISION-PACKET.md | 38 |
| SEMANTIC-DELTA.md | 12 |
| REVIEW-BRIEF.md | 6 |
| IMPACT-LEDGER.md | 2 |
| builder | 1 |
| **Total** | **59** |

Every string presented as the owner's is in the answer column of its
record. I located each one by string search and cell index in
`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, where the header at
line 53 is Row | Ruled | What it means | Applied by:

- P-74, Ruled cell (line 64, cell 1), quoted at packet:19–20, 197–199 and
  SEMANTIC-DELTA.md:141–143;
- P-72, Ruled cell (line 60), quoted at packet:233–235;
- P-82, Ruled cell (line 70), Q1 and Q4, quoted at packet:243–244,
  SEMANTIC-DELTA.md:195–196 and IMPACT-LEDGER.md:150;
- `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md:114`, the
  owner's-answer cell, quoted at packet:139–140 and SEMANTIC-DELTA.md:29–31.

Every "What it means" and "Applied by" text is labelled the recorder's:

- P-74 cell 2 (line 64) at packet:194–196 and SEMANTIC-DELTA.md:144–147;
- P-78 cell 2 (line 66; the sentence also appears in P-77's row, line 65)
  at packet:209;
- P-82's `PWB-REQ-002` and `.15.1` at packet:245–247,
  SEMANTIC-DELTA.md:197–199 and IMPACT-LEDGER.md:150.

The `.18`-first order is called a builder or drafting constraint, not a
ruling, in four places: builder:10–11, packet:24 and 145–149,
SEMANTIC-DELTA.md:29 and 224, and IMPACT-LEDGER.md:147. I found no
misattribution.

## VIS-4 sweep

The population is all 6 package files. The one 64-hex digest is the manifest
row, in `PWB-LOADED-PROFILE-AMENDMENT-MANIFEST.txt`, which carries no act
phrase beside it. I found 22 hits for
`adopted|accepted|approved|in force|binds|is binding|signed off|performed`,
and read every one. They are all one of:

- "binds nothing" banners;
- conditional adoption ("if … adopted", "until that act is performed");
- references to the act in force.

Nothing is labelled accepted or adopted.
