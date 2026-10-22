# Island decoupling: review dispositions, round 1

[Observed] This record dispositions the CC-REV-1 review of `syzygy-bpyt.8.1`
(pull request #510). That change decouples the live `syzygy` CLI's dossier
path from the parked provider island. It does this in four parts:
- leaf modules in `polaris-generation-core`, behind a new `/live` subpath;
- a standalone `DOSSIER_GUIDANCE` template;
- an operator-agent renderer, `renderLocalDossier` in `dossier-site.ts`, with
  its own input;
- `island-boundary.test.ts`, which fails when a CLI-reachable module imports
  the island.

Nothing is deleted or moved out of its package (GP-Q8).

| Round | Raw | Verdict (line 2) | Reviewed commit (line 3) | Subject (line 4) |
|---|---|---|---|---|
| 1 | `docs/reviews/R-GP-IMPL-ISLAND-DECOUPLING-1-RAW.md` | `CONFIRM WITH EXCEPTIONS` | `6ac21f2c` | `r1-review.diff` sha256 `3edfd5f6278f7eb1c593141c9d671e85e2571be1c2b1c80534c5e1433511bd82` |

The subject equals `git diff c55acb73 6ac21f2c`. Main then moved to
`68c553b8` (#508 and #505), and the branch merged it at landing. After that
merge, `git diff origin/main HEAD | sha256sum` printed the same digest, so the
merge brought only main's bytes. The reviewer's trial merge with `68c553b8`
was clean too: typecheck passed and the boundary test passed 4/4 (raw section
3, item 15).

The reviewer found "There are no blocking findings (no F ids)." (section 4),
with six notes. Under the owner's notes-only stopping rule
(`.syzygy/governance/decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md`
section 1), the round clears the exact bytes it read, and those bytes are not
edited. This record sits beside them. It is an implementation record and binds
nothing.

Revise-severity findings open: 0

## Retained review evidence

The reviewer's tools and the outputs this record relies on are retained
under `docs/evidence/island-decoupling-review-2026-10-22/`:
- `tools/`, including `reviewer-mutants-spec.json` with the fragments of
  mutants R1 to R9;
- `mutants-reviewer.json` and `mutants-lane-rerun.json`;
- `static-*.json`, the reviewer's independent reachability sweep, before and
  after, with and without `consent-ports.ts` followed;
- `differential-mine.json`, `consent-differential-mine.json` and
  `consent-after-reproduce.json`;
- `exports-old.json` and `exports-new.json`.

Not retained: the build and test logs, the regenerated diff, the
`check_governance` and `check_quotations` transcripts, and the provider
sent-text outputs. The raw records the result of each, and the sent-text
digests in section 3, item 18.

## N1: the CLI still loads the core island through `consent-ports.ts`

[Observed by the reviewer] At the head, the CLI's dossier branches load the 7
core island modules, and they load them only through `consent-ports.js` →
core `index.js`. With `consent-ports.js` stubbed, 0 load. Reached importers of
the core root fall from 22 to 1.

**Disposition:** this is the residual the pull request declares. The bead's
outcome, "no module reachable from the syzygy CLI imports a provider-mode
module", is **not yet fully met**. The bead closes with this residual named,
and `syzygy-bpyt.8.19` (step (e), the consent `./live` subpath) removes the
edge. The finding is posted on `syzygy-bpyt.8.19`.

## N2 and N3: the boundary test's reach

[Observed by the reviewer] The test sees literal specifiers only, from one
entry, with one exports-condition choice. Reviewer mutants R1 (a computed
`import()`), R4 (a `node` condition ahead of `import`), R5 (an import in
`broker-client.ts`), R6 (`createRequire`) and R9 (a new island import inside
the unfollowed `consent-ports.ts`) all survive. None of these forms occurs
today: the reviewer's sweep finds 0 non-literal `import()`, 0 `require` and 0
workers over the 143 reached modules.

**Disposition:** filed as `syzygy-bpyt.8.23` (P3, test-only). The pull
request body's "It follows every edge: static, type-only, re-export and
dynamic" overstates the test. The test's own comment, "dynamic with a literal
specifier", is the accurate one: the test follows **literal specifiers
only**.

## N4: the owner notice

[Observed by the reviewer] The pull request's GP-Q0 list names the
differential and the mutants, but not the owner notice.

**Correction:** the reviewer read `syzygy-bpyt.10` with `bd show --json`,
which does not return comments, and reported "0 comments". [Observed by the
coordinator] `bd comments syzygy-bpyt.10 --json` returns 13 comments, each an
owner notice for one merged bead of this epic, from PR #494 to PR #505.

**Disposition:** the 8.1 notice is posted on `syzygy-bpyt.10` at landing. It
covers:
- the classes;
- the additive exports;
- the CLI's renderer injection;
- the `consent-ports.ts` residual and `syzygy-bpyt.8.19`.

## N5: `prompts.ts` is in `/live`

[Observed by the reviewer] `prompts.ts` (`promptForStage` and the stage
illustrations) is exported from `/live` and loaded at runtime, but no CLI-path
module uses it since `brief.ts` stopped calling it. It is not on the bead's
island list, which governs this change.

**Disposition:** kept as reviewed. Narrowing `/live` now would change the
reviewed bytes. Nothing outside the workspace consumes `/live`. Whether
`prompts.ts` joins the island is decided in `syzygy-bpyt.8.19`, which
rewrites the same boundary; the question is posted there. If the answer is to
drop it from `/live`, that review rules on whether the removal is an endpoint
removal under GP-Q0.

## N6: load-sensitive timeouts

[Observed by the reviewer] The `package-reader.test.ts` world-sweep test
times out at main `68c553b8` alone, without this pull request. Two
`start-gates.test.ts` cases time out under load and pass alone.

**Disposition:** added to `syzygy-bpyt.4.13`, which this pull request's lane
reported.

## Risk class

Classes 1, 3, 4 and 6 (additive), by the reviewer's ruling, which agrees with
the pull request. GP-Q0's checks:
- the differential: met. Reproduced by the reviewer:
  - local renders 16/16 (15 distinct);
  - provider renders 26/26 (16 distinct);
  - briefs 3/3, with altered prose;
  - validators 62/62 (51 refusals);
  - the 8.10 consent census 15/15 records over 1,890 fixtures;
  - provider sent text and the egress table byte-identical.
- a rule-6 mutant per predicate: met for every predicate the test
  implements. The lane's 25 mutants reproduce (23 killed, 2 equivalent), and
  the reviewer's R2, R3, R7 and R8 are killed. The forms the test does not
  implement are N2 and N3.
- the owner notice: posted at landing (N4).
