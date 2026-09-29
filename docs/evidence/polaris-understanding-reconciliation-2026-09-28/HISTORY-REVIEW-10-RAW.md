# History review 10 — reconciliation recorder
Verdict: REVISE
Reviewed commit: 7f363bc75eda5b6ddc4a9cb129b177e1edbdcff1
- `scripts/record_polaris_understanding_adoption.py`: `ffea484622cb54bdd678ae60af874c6bdcd028f07af9df4d059415defe45f0d6`

Reviewer: an independent fresh-context agent, 2026-09-29. I cloned
`/home/tze/GitHub/syzygy`, fetched `recorder/successor-rows` and checked out
the reviewed commit.
- Subject: `git diff origin/main 7f363bc`. It touches 6 files; the recorder
  is +186/−8 lines in `--stat` terms [Observed].
- I computed the recorder digest above with `sha256sum` in the clone
  [Observed].
- `scripts/readability_successor.py` hashes to `88358478…8256`, equal to
  `SUCCESSOR_TOOL_SHA` (recorder `:34`) [Observed].

## Criteria results

1. **Fail-closed.** Every path I found refuses rather than grants, except
   one: the two-claimant refusal can be sidestepped by spelling one path two
   ways (M1). In detail:
   - **Any failing package.** The per-package `try` now catches `Exception`
     (`:313`). Malformed, deeply nested, wrongly typed, erroring,
     unperformed and drifted packages are skipped and block nothing else
     [Observed: the selftest fixtures at `:1084-1093` and the drifted case,
     and the narrowing mutants below].
   - **Foreign predecessor and non-row bytes** are refused by the exact-pair
     test (`:448`, rows 53/54) [Observed].
   - **Edited tool** is refused (`:44-45`, row 56). The executed bytes are
     the hashed bytes (`:50`, `exec(compile(source, …))`) [Observed].
   - **Only the contested path is refused.** The selftest asserts that the
     uncontested path of the second package keeps its row (`:1135-1137`), and
     the marking at `:316` is order-independent: whichever package comes
     second (or third) finds the path already present [Observed in code;
     the fixture exercises one order].
   - **Scope of the widening.** Only the drift branch of `baseline_proof`
     (`:442-448`) is widened. `Frozen` delegates to the same live rows
     (`:552-553`, row 59). No other gate changed in the diff [Observed].
2. **HISTORY-READING claims.** One claim is false for a reachable input (M1:
   lines 35-36). The other exception sub-bullets (lines 23-34, 36-42) hold
   against the code and the pinned tool. The chain sentence (lines 36-38)
   is true: once a second restyle performs, the first package's subjects
   drift, so its `check()` raises and it is skipped. The second package's
   predecessor is not the adopted digest, so the pair test refuses
   [Inferred from `readability_successor.py` `check()` and `:448`].
3. **Selftest and check** [Observed].
   - `--selftest` exits 0. It prints four PASS lines, including `57
     trust-boundary mutations refused`, `22 real-Git cases` and `PASS
     successor rows selftest: absent tool, unperformed, performed,
     malformed, deeply nested and wrongly typed siblings, edited tool, two
     claimants and drifted packages`.
   - `--check` exits 1 with exactly `FAIL exact digest reconciliation
     unresolved: latest history review not confirming:
     docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-9-RAW.md`.
     This is the designed state.
4. **Rule-6 rows.** `history-reading-rule6.json` has 65 mutants. The 12
   rows at `1d5b534` are indices 53–64.
   - Method: a fresh clone for each row, checked out at the row's commit.
     `old` occurred exactly once, `old→new` was applied, and the file's
     `command` (`python3 scripts/record_polaris_understanding_adoption.py
     --selftest`) was run. `<tmpdir>` was matched as `/tmp/[^/]+`.
   - Rows 53–64: 12/12 exit 1 and print their recorded refusal [Observed].
   - Spot-check of earlier post-round-6 rows 31, 33, 36, 38, 40, 42, 45, 47,
     49, 51 and 52: 11/11 exit 1 [Observed]. Ten print their recorded
     refusal verbatim. Row 42 (round 7, before the `<tmpdir>` form) records
     a literal `/tmp/tmp3n25cwo5/…` path. The run printed the same refusal
     under a different temporary name, which is expected.
   - Guards with no killing row beyond the two the page names (the rows
     cache and executing the hashed bytes, both confirmed surviving) are
     listed in N1.
5. **Governance checks** [Observed].
   - `python3 scripts/check_governance.py` prints `31 OK, 21 WARN, 0 FAIL
     (52 checks)`.
   - `--selftest` prints `347 fixtures, 0 failing`.
   - `readability_successor.py --all --check` reports 3 packages, all
     `candidate-unperformed`.

Round-7, round-8 and round-9 dispositions (HISTORY-READING lines 132-154)
checked against the code:

| Finding | Disposition | Result |
|---|---|---|
| R7 M1 | tool pin | Holds (`:34`, `:44-45`, row 56) [Observed] |
| R7 N1 | per-package isolation | Holds, now for every `Exception` (`:313`, row 58) [Observed] |
| R7 N2 | two-claimant refusal (displacement rule withdrawn) | Holds for identical spellings. An aliased spelling escapes (M1) [Observed] |
| R7 N3 | disclosure | Holds (lines 39-42) [Observed] |
| R7 N4–N6 | rows, cache, none | Hold [Observed] |
| R8 M1 | two-claimant refusal | Holds for identical spellings; see M1 [Observed] |
| R8 N1 | `RecursionError` contained | Holds, subsumed by `Exception` (row 58 is killed by the `RecursionError` fixture) [Observed] |
| R8 N3 | `<tmpdir>` | Holds (rows 60 and 50) [Observed] |
| R8 N4 | execute the hashed bytes | Holds in code (`:50`); disclosed as having no row (lines 96-100) [Observed] |
| R9 M1 | catch every exception; three wrongly typed fixtures | Answered. Narrowing back to round 9's `(ValueError, OSError, RecursionError)` is killed by `decoding to str: need a bytes-like object, int found` [Observed]. See N1 for a narrower width that survives |
| R9 N1 | round-10 rows; two no-row statements | Answered (rows 53–64 pin the drift branch, both halves of the stored pair and the contested refusal) [Observed]. See N1 |
| R9 N2 | rule-6 paragraph reworded | Answered (lines 82-84) [Observed] |
| R9 N3 | round-7 bullet reworded | Answered (lines 135-137) [Observed] |
| R9 N4 | refuse only the contested path | Answered (`:316`, `:447`, `:1135-1137`) [Observed] |
| R9 N5 | unused import removed | Answered: `importlib` no longer appears in the recorder [Observed] |

## Blocking findings

**M1 — Two performed-exact packages claiming one file escape the
two-claimant refusal when one of them spells the path differently.
HISTORY-READING lines 35-36 and the docstring at `:297-298` say such a path
is refused.** [Observed]

What the page and the code say:
- HISTORY-READING.md lines 35-36: "Two performed-exact packages claiming one
  path are refused for that path, whatever their order".
- `successor_rows` keys `rows` by the raw string from each package's
  `predecessor` (`:312`, `:316`). `baseline_proof` looks the row up by the
  recorder's canonical path (`:446`).

The pinned tool accepts non-canonical spellings of the same file:
- `readability_successor.py:70` refuses only absolute paths and `..`.
- `Path('a/./b').parts` and `Path('a//b').parts` both normalize to
  `('a', 'b')`, so `read()` opens the same file.
- `Package.subjects` is `sorted(self.predecessor)` (`:87`), and the manifest
  row regex accepts any non-blank path (`:52`).

Probe (`probe_alias.py`, scratch temp root, the recorder's own
`successor_rows_selftest` construction with one change) [Observed]:
- The second package keys the shared file as
  `openspec/changes/example/./proposal.md` instead of
  `openspec/changes/example/proposal.md`.
- `module.packages(root)` reports both packages `performed-exact`.
- `Evidence(root).successor_rows()['openspec/changes/example/proposal.md']`
  is the first package's `(predecessor, successor)` pair, not `CONTESTED`.
  It equals the pair the first package grants alone.
- The same result holds for the spelling `openspec/changes/example//proposal.md`.
- The unmodified construction (same spelling) returns `CONTESTED`, as the
  selftest asserts.

So with two performed successors of one file, the recorder does not refuse.
It accepts the canonically spelled package's row, which ranks by spelling
where the design says "refused, not ranked" (`:1104`).

Severity:
- Nothing without an owner act is granted. The accepted pair is one that a
  performed-exact package certifies from the adopted digest, and the
  aliased package can never grant, because the recorder never looks up its
  key.
- It is still blocking under acceptance criteria 1 ("a path two
  performed-exact packages claim is refused regardless of order") and 2. The
  page's claim is false for a reachable input, and this is the same class
  as round 8's M1: two performed successors of one file, with something
  other than a refusal deciding.

Required, either of:
- (a) Canonicalize before keying. For example, key `rows` by
  `PurePosixPath(path).as_posix()`, or treat any package whose subject keys
  are not already canonical as failing (it grants nothing). Add an aliased
  fixture to `successor_rows_selftest` and a rule-6 row that drops the
  canonicalization.
- (b) Or narrow the claim to what holds: "two packages naming one path by
  the same spelling". Say that an aliased spelling is not detected.

## Notes

**N1 — Guards with no killing row beyond the two the page names.** Each
mutant was applied once at `7f363bc` and `--selftest` was run [Observed].
- **The full width of the per-package scope.** `except Exception:` →
  `except (ValueError, OSError, RecursionError, TypeError):` (`:313`)
  **survives** (exit 0). The fixtures raise `JSONDecodeError`,
  `RecursionError`, `TypeError` (`label`, `predecessor`) and `ValueError`
  (`pins: []` fails the key-set test at tool `:85`). None raises
  `AttributeError`. Round 9's probe did: `"pins": [<the three key names>]`
  with an existing act reached `pins.values()` (tool `:158`). Row 58 pins
  only a narrowing to `(ValueError, OSError)`. The code is correct, and
  HISTORY-READING's "containing every exception" (line 149) is true of it.
  But "Two guards have no row" (line 96) understates: the scope's width beyond
  `TypeError` has none. A `pins`-as-list fixture with an act file present
  would close it.
- **Identical claimants.** `rows[path] = CONTESTED if path in rows else …`
  → `… if path in rows and rows[path] != (predecessor, successor) else …`
  (`:316`) **survives**. The fixture's two claimants have different pairs.
  That mutant would let two packages with the same pair grant, contrary to
  "whatever their order" and "refused". Row 61 pins only the removal of
  the marking.
- **Named on the page and confirmed surviving:** disabling the rows cache
  (`:301`, `if False:`), and re-reading the tool file instead of executing
  the hashed bytes (`:50`). Both exit 0, as lines 96-100 disclose.

**N2 — HISTORY-READING line 36 is not wrapped.** It runs to about 120
columns ("… other paths are unaffected. A second restyle of these subjects
names the first"). This is cosmetic. Per the repository's wrapped-citation
lesson, it does not break a code span.

**N3 — Carried from round 9 N4, still true.** The executed tool resolves
`difflib` through `sys.path[0]` (`scripts/`). This is the same trust class
as the recorder's own imports, so it adds a name, not a class [Inferred;
not re-probed this round].
