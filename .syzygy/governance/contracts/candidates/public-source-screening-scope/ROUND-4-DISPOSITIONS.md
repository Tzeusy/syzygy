# Round 4 dispositions — public-source screening scope

> **Candidate — binds nothing.** Notes record for
> `reviews/R-PUBLIC-SOURCE-SCREENING-SCOPE-4-RAW.md` (verdict CONFIRM WITH
> EXCEPTIONS; findings 1 to 5 are notes), written 2026-10-03 under the owner's
> 2026-09-26 ruling that a notes-only confirmation clears its bytes and the
> notes go in a sibling record. The raw is retained verbatim. No manifest-bound
> byte is touched by these repairs: the manifest file digest after them equals
> the one in the raw's head (compared by script, not transcribed here), and the
> patch is unchanged. The edits are to the builder, a new reader script, the
> ledger, the brief and this record. No digest is copied here.

| # | Finding | Disposition |
|---|---|---|
| 1 | The masking scanner failed open on a nested template literal and on a regex literal holding a quote; `export let` was accepted | Repaired by replacing the scanner. `scripts/read_ts_exported_string_array.mjs` parses the file with the TypeScript compiler API and requires: no syntax errors; exactly one top-level statement binding or exporting the symbol; an exported `const` variable statement with a single declaration, no type annotation, whose initializer is an array literal of string literals `as const`. Anything else is refused. The builder runs it with node and refuses when node, the `typescript` package or the file is missing; there is no text-scan fallback. The reviewer's fixtures A, B, C, D, E, G, H and I are in the selftest with their real-TypeScript verdicts (A and B refused, C, D, E and G read, H and I refused), plus a re-export, a function-body declaration and `satisfies`. |
| 2 | Two scanner branches had no killing fixture (escape skip, newline refusal) | Superseded: those branches are gone with the scanner. The new fixtures include an escaped quote before a live declaration (reads) and a string running over a newline (a syntax error, refused). The selftest carries seven mutants of the reader script, each a removed guard (syntax errors, second binding, unexported, `let`, `as` type, non-string member, type annotation), each caught by a named fixture. |
| 3 | The ledger's record-figure predicate yielded 49, not 61; "The five are" listed six | Repaired in the ledger: the predicate now lists the simulator's six literals (digest, version, the performed act's identity and tag, two act-record pointers) and says two alone give 49; the own-package count and its file list are restated. After retaining the round-4 raw the figure is 62 with seven own files. |
| 4 | The brief still called itself the round-3 brief and named the round-3 raw file | Repaired: header and recording section name round 5 and the round-5 raw; criterion 13 added. |
| 5 | The single-quoted half of the string-embedded fixture was not valid TypeScript | Repaired: the inner quotes are escaped so both halves parse, and the reader (not the scanner's accident) refuses them. |

## Also found

The reviewer of the generator branch reported that `--check` printed the
not-ready finding but exited 0. The builder's exit rule is now a function with
three selftest predicates (not-ready exits 1; `--pending-symbol` exits 0;
stale bytes exit 1 regardless). The round-4 raw records exit 1 for the same
run; a pipe such as `| head` hides the status. Run against the generator
branch's `generation-source.ts` (22 reasons) the new reader returns all 22.
