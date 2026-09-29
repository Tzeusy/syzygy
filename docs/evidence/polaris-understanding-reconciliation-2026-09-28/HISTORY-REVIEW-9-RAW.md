# History review 9 — reconciliation recorder
Verdict: REVISE
Reviewed commit: 5df8dd317d5acc9db43cfc281ebf1861cc5cb1a0
- `scripts/record_polaris_understanding_adoption.py`: `addc80c5617599601f7ecbcbed396f3485a4cdd7be7f83d85134b27007133ba3`

Reviewer: an independent fresh-context agent, 2026-09-29. I cloned
`/home/tze/GitHub/syzygy`, fetched `recorder/successor-rows` and checked out
the reviewed commit.
- Subject: `git diff origin/main 5df8dd3`. It touches 5 files, +755/−6; the
  recorder is +174/−6.
- I computed the recorder digest above with `sha256sum` in the clone
  [Observed].
- `scripts/readability_successor.py` hashes to `88358478…8256`, which equals
  `SUCCESSOR_TOOL_SHA` at recorder line 34 [Observed].
- `90f12ae` and `5df8dd3` have identical recorder bytes. Their diff touches
  only `HISTORY-READING.md` and `history-reading-rule6.json` [Observed].

## Criteria results

1. **Fail-closed.** Every path I found refuses; none grants. One claim does
   not hold: some malformed siblings block the whole check (M1). In detail:
   - **Tool pin.** An edited tool is refused (`:44-45`, row 45).
   - **Executed bytes.** The recorder executes the bytes it hashed
     (`:50`, `exec(compile(source, …))`) [Observed].
   - **Foreign predecessor and non-row bytes.** Both are refused by the
     exact-pair test (`:444-448`, rows 43/44).
   - **Unperformed packages** grant nothing (`:310`, row 46). **A drifted
     performed package** makes `check()` raise, so it is skipped [Observed by
     the selftest's last case].
   - **Two claimants.** Two performed-exact claimants of one path are refused
     by `require(path not in rows, …)` (`:316`, row 51). This does not depend
     on order: the refusal fires on the second insertion, whichever package
     comes second [Inferred from the code; the selftest exercises one order].
   - **Scope of the widening.** Only the drift branch of `baseline_proof`
     is widened. `Frozen` delegates to the same live rows (`:552-553`), and
     every other gate is unchanged in the diff [Observed].
   - **End-to-end positive case** [Observed]. In a scratch clone I performed
     the real `polaris-understanding-readability-successor` with
     `readability_successor.py --record` (the phrase was the label plus the
     manifest sha256). `--all --check` then reported it `performed-exact`.
     `check()`, with only `history_review`/`history_reviews` stubbed,
     returned C1 `9322656dcfcc…`.
2. **HISTORY-READING claims.** One sentence on the exception, and the
   round-8 N2 disposition, are false against the pinned tool (M1). The other
   exception sub-bullets hold (see M1 and the notes).
3. **Selftest and check** [Observed].
   - `--selftest` exits 0 and prints four PASS lines, including `56
     trust-boundary mutations refused`, `22 real-Git cases` and `PASS
     successor rows selftest: absent tool, unperformed, performed, malformed
     and deeply nested siblings, edited tool, two claimants and drifted
     packages`.
   - `--check` exits 1 with exactly `FAIL exact digest reconciliation
     unresolved: latest history review not confirming:
     docs/evidence/polaris-understanding-reconciliation-2026-09-28/HISTORY-REVIEW-8-RAW.md`.
     This is the designed state.
4. **Rule-6 rows.** `history-reading-rule6.json` has 53 mutants. The 10
   rows at `90f12ae` are indices 43–52.
   - Method: a fresh clone for each row, checked out at the row's commit.
     `old` occurred exactly once, `old→new` was applied, and the file's
     `command` (`python3 scripts/record_polaris_understanding_adoption.py
     --selftest`) was run. For row 50, `<tmpdir>` was matched as `/tmp/[^/]+`.
   - Rows 43–52: 10/10 exit 1 and print their recorded refusal [Observed].
   - Spot-check of earlier post-round-6 rows 31, 33, 35, 36, 38, 40 and 41:
     7/7 exit 1 and print their recorded refusal [Observed].
   - Guards with no row are listed in N1.
5. **Governance checks** [Observed].
   - `python3 scripts/check_governance.py` prints `31 OK, 21 WARN, 0 FAIL
     (52 checks)`.
   - `--selftest` prints `347 fixtures, 0 failing`.
   - `readability_successor.py --all --check` reports 3 packages, all
     `candidate-unperformed`.

Round-7 and round-8 dispositions (HISTORY-READING lines 128-143) checked
against the code:

| Finding | Disposition | Result |
|---|---|---|
| R7 M1 | tool pin | Answered (`:33-34`, `:44-45`, row 45) [Observed] |
| R7 N1 | per-package isolation | Answered for syntax errors and wrong key sets only. Wrong-typed values escape (M1) [Observed] |
| R7 N2 | "displacement rule above (one exact package per path)" | Answered in code by the two-claimant refusal. The pointer to a "displacement rule above" is stale (N3) [Observed] |
| R7 N3 | disclosure | Answered (lines 38-41) [Observed] |
| R7 N4–N6 | rows, cache, none | Answered [Observed] |
| R8 M1 | two-claimant refusal | Answered. The fixture now gives the second package its own raw and asserts that both check `performed-exact` (`:1110-1119`) [Observed] |
| R8 N1 | catch `RecursionError` | Answered (`:313`, rows 47/48) [Observed] |
| R8 N2 | round-9 rows; "`KeyError` and `TypeError` left the scope: the tool reports config errors as `ValueError`" | Rows present. **The stated reason is false** (M1) [Observed] |
| R8 N3 | `<tmpdir>` | Answered (row 50) [Observed] |
| R8 N4 | execute the hashed bytes | Answered in code (`:50`). No row pins it (N1) [Observed] |

## Blocking findings

**M1 — A malformed sibling package with wrong-typed config values escapes the
per-package scope and blocks the whole check. HISTORY-READING and the
docstring say it blocks nothing, and the round-8 disposition's reason is
false.** [Observed]

What the page and the code say:
- HISTORY-READING.md lines 32-34: "A package that is unperformed, drifted,
  malformed (including a deeply nested config) or fails to check grants
  nothing and blocks no other package."
- Lines 140-141 (the round-8 N2 disposition): "`KeyError` and `TypeError`
  left the scope: the tool reports config errors as `ValueError`".
- Recorder docstring `:295-296`: "a package that fails to load or check
  contributes nothing and blocks no other."
- The code catches only `except (ValueError, OSError, RecursionError)`
  (`:313`).

The pinned tool does not report every config error as `ValueError`.
`Package.__init__` checks only the key *set* (`readability_successor.py:83`)
and the pins key set (`:85`). It then uses the values untyped:
- `re.escape(self.label)` (`:88`);
- `sorted(self.predecessor)` (`:87`);
- `self.root / self.act` (`:236`);
- `pins.values()` (`:158`).

Probe (`probe1.py`, scratch clone at `5df8dd3`, the repository's three
real packages plus one sibling `zz-*/SUCCESSOR.json` holding all nine keys)
[Observed]. `Evidence(root).successor_rows()` behaved as follows:
- `"label": 5` → **escapes** `TypeError`;
- `"predecessor": 5` → **escapes** `TypeError`;
- `"act": 5` → **escapes** `TypeError`;
- `"pins": ["manifest_sha","review","review_sha"]` with an existing act →
  **escapes** `AttributeError`, which is not in `main`'s tuple either, so the
  result is an uncaught traceback;
- `"predecessor": ["a.md"]` → isolated;
- a key-name array → isolated.

End to end (`probe2.py`) [Observed]:
- Clone with the understanding successor performed and no sibling:
  `check()` (history review stubbed) returned `9322656dcfcc`.
- Same clone plus one draft sibling with `"label": 5`: `check()` refused
  with `TypeError decoding to str: need a bytes-like object, int found`.

So an unrelated, half-drafted package blocks this recorder on every
`--check` once the understanding successor is performed.

Round 8 had already observed this isolation working: "a config with
`"label": 5` raised `TypeError` inside `Package` and was isolated"
(HISTORY-REVIEW-8-RAW.md, N1). The round-9 change removed `TypeError` from
the tuple and justified that with the false sentence above. This is a
regression of round-7 N1's disposition.

Severity:
- Fail-closed. Nothing is granted: a grant still needs `check() ==
  'performed-exact'` and the exact `(adopted, current)` pair.
- It is blocking under acceptance criteria 1 ("malformed … or erroring
  packages … block nothing else") and 2. A HISTORY-READING claim, a
  disposition's stated reason and the recorder's docstring are all false
  against the pinned tool.

Required, either of:
- (a) Make the claim true. For example, catch `Exception` in the per-package
  `try`. I applied `except Exception:` at `:313` and `--selftest` still
  passes [Observed], so the selftest does not pin the tuple's width in that
  direction. Add a fixture for a wrong-typed sibling (for example
  `"label": 5`) and a rule-6 row that narrows the tuple back.
- (b) Or narrow the claims to what holds: syntax errors, wrong key sets and
  deep nesting are isolated, while wrong-typed values block the check
  (fail-closed). Remove "the tool reports config errors as `ValueError`".

## Notes

**N1 — Guards in the diff with no killing row, other than the rows cache.**
Each mutant was applied once at `5df8dd3` and `--selftest` was run
[Observed].
- **Hashed bytes are the executed bytes.** Mutant: `exec(compile(source, …))`
  → `exec(compile(open(module.__file__,'rb').read(), …))` (`:50`). It
  **survives** (exit 0). The HISTORY-READING claim at lines 30-31 is true of
  the code, but nothing pins it. A check-then-use gap is hard to fixture;
  disclose it on the page or add a fixture that swaps the file between the
  read and the exec.
- **The drift branch itself.** Mutant: `if current != adopted:` →
  `if False:` (`:444`). It is killed by `mutation accepted: …/spec.md`, but
  no row pins it: rows 43/44 each drop only one half of the pair test.
- **The predecessor half of the row value.** Mutant: `(path,
  package.predecessor[path], …)` → `(path, installed[path], …)`, and also
  swapping the stored pair. Both are killed by `performed successor row`.
  Row 52 pins only the successor half.

**N2 — The rule-6 paragraph's "Two fail by an exception rather than by
their named refusal" (line 82) is now stale.** That sentence predates the
successor rows and names rows 5 and 6. Other rows now also fail through an
exception message rather than a named refusal:
- row 47 (`RecursionError` traceback);
- rows 40/48 (a `JSONDecodeError` message);
- rows 42/50 (`[Errno 2]`).

All of them fail closed [Observed].

**N3 — The round-7 bullet's "by the displacement rule above (one exact
package per path)" (lines 131-132) points at a rule the page no longer
states.** The page now has the two-claimant refusal. Round 8 found the
displacement rule false. Say that round 7's N2 is answered by round 8's
two-claimant refusal.

**N4 — Two further robustness notes.**
- **Unrelated paths.** The two-claimant refusal (`:316`) also fires for paths
  outside this recorder's eight subjects. Two performed successors sharing,
  say, a Capability 1 file would block this recorder. This is fail-closed,
  and the page's wording ("refused") covers it [Observed from the code].
- **Import resolution.** The executed tool imports `difflib`, which the
  recorder itself never imports. It resolves through `sys.path[0]`
  (`scripts/`). A planted `scripts/difflib.py` ran when `successor_rows`
  loaded the tool [Observed]. The recorder already trusted `scripts/` the
  same way: a planted `scripts/zoneinfo.py` ran before any gate [Observed].
  So this adds a name, not a class.

**N5 — `import importlib.util` (`:10`) is now unused.** It is cosmetic.
