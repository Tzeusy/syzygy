# R-PUBLIC-SOURCE-SCREENING-SCOPE-4 — fresh-context round-4 review of the public-source screening scope package
Reviewed commit: 895f1622ebf55fa397f7552ad3b5a85c6ad9dc7b
Manifest SHA-256: 1cbf45a0da07a4cf769a17b6ac98960c6ae214c2d88a4f974e7b9d5026bc4f83
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context agent, 2026-10-03. I used a detached scratch worktree
at the reviewed commit read-only. Mutations, `--write` runs and the independent
patch application used `git archive` copies of that commit. The simulation
used the script's own `git clone --shared` scratch clone, with TMPDIR in the
scratchpad. I edited no tracked file, read no external repository and called
no model provider. The head digest is `sha256sum` of the manifest file. It
agrees with `--manifest-digest --pending-symbol`.

## What was run

- Builder `--selftest`: `selftest: 54 of 54 predicates held`.
- `--check` printed `public-source screening scope: current`, then
  `FINDING not ready for an act: GENERATION_EXCLUSION_REASONS is not declared in packages/polaris-generation-core/src/generation-source.ts`.
  Exit 1.
- `--check --pending-symbol` printed the same line as `NOTE`. Exit 0.
- `--manifest-digest` without the flag refused. Exit 1.
- `--manifest-digest --pending-symbol` printed the head digest. Exit 0.
- `python3 scripts/check_governance.py`:
  `31 OK, 21 WARN, 0 FAIL (52 checks)`, exit 0.
- Independent application: `patch -p1` over an archive copy hashes the policy
  to the manifest row (`d42defca…`). Parsed as JSON:
  - added `['publicSourceScope']`, one position after `scope`;
  - removed none;
  - changed `['policyVersion']` only.
- Manifest independence: in an archive copy I appended
  `export const GENERATION_EXCLUSION_REASONS = ['oversize-source-excluded', 'body-not-retained-for-generation'] as const;`
  to `generation-source.ts` and ran `--write`.
  - The patch and manifest hashes were byte-identical to the committed ones.
  - `--check` then exited 0 and printed both reasons.
  - `--manifest-digest` printed the head digest.
  - I added a third member (`'empty-file'`) and re-ran `--write`. The hashes
    were still identical, and `--check` printed three reasons.

  The manifest bytes are independent of the constant's values.
- `simulate_public_source_screening_scope_act.py --tests --json`, exit 0. It
  reported 2002 tracked files and `recordHitCount` 61. Six of the 61 are under
  this package:
  - `IMPACT-LEDGER.md`;
  - `SEMANTIC-DELTA.md`;
  - the patch;
  - the three raws.

  Failed:
  - repin builder `--check`;
  - repin recorder `--check policy`;
  - `check_governance` (CG-7e, 6 findings);
  - Vitest `governance-inputs.test.ts` (`expected 'policy:exact-digest-wrong' to be 'policy:superseded'`),
    `content-classification.test.ts` and `git-object-reader.test.ts`.

  Passed: `npm ci` and `project-shape-model.test.ts`. These agree with the
  ledger's check table row by row.
- Second method for the record count: Python over `git ls-files -z` in the
  worktree. It excludes the pin prefixes and the policy file itself, which the
  simulated act replaces. Results:
  - the simulator's six literals give 61;
  - the ledger's stated two literals give 49 (Finding 3).
- Sweeps 1 and 2 were re-run by Python over `git ls-tree -r -z` plus
  `git show`:

  | Commit | Files | Sweep 1 | Code | Sweep 2 |
  |---|---|---|---|---|
  | `c540438d` | 1975 | 52 | 14 | 15 |
  | reviewed | 2002 | 57 | 15 | 15 |

  The figures at `c540438d` match the ledger.
- Criterion 8: I swept every Markdown file of the package with Python `re`.
  - Package Markdown outside `reviews/` carries 0 standalone 64-hex tokens.
  - Each raw carries 1, its head.
  - The `accepted|approved|adopted` hits outside `reviews/` are:
    - packet :19 (the provenance label `owner-adopted (bootstrap, uncorrelated)`);
    - brief :49 (criterion text);
    - ROUND-3-DISPOSITIONS :12 ("The constant reader accepted …").

  Nothing is labelled accepted.
- Reader adversarial fixtures (not in the selftest), written to a scratch
  `generation-source.ts` and read by `exclusion_reasons`. Fixtures A and B load
  as ES modules under Node with **zero exports**.

  | # | Source | Real JS/TS | Reader |
  |---|---|---|---|
  | A | ``const x = `${`; export const GENERATION_EXCLUSION_REASONS = ['a'] as const; `}`;`` (nested template in `${}`) | no live declaration | `['a']`, fails open |
  | B | `const r = /'/; // '; export const GENERATION_EXCLUSION_REASONS = ['a'] as const;` (regex holding a quote, declaration in a line comment) | no live declaration | `['a']`, fails open |
  | C | `const r = /[//]/; export const … = ['a'] as const;` | live | refused "not declared" (fail closed, false refusal) |
  | D | `const s = '/*'; export const … = ['a'] as const; const t = '*/';` | live | `['a']`, correct |
  | E | `` const u = `${a ? 'x' : "y"}`; `` then a live declaration | live | `['a']`, correct |
  | F | `` const v = `/* export const … */`; `` | no live declaration | refused, correct |
  | G | `const w = /\/*x*\//; export const …` | live | refused "unterminated block comment" (fail closed) |
  | H | `export let GENERATION_EXCLUSION_REASONS = ['a'];` | live, mutable | `['a']`, accepted |
  | I | `const …` plus `export { … };` | exported | refused "not exported" (fail closed) |
  | J | declaration only inside a function body | not exported | refused "not exported", correct |

- Rule-6 mutations of my own, each on a fresh archive copy of the script.
  The script was restored after each, and `diff -q` against the worktree was
  clean.

  | Mutation | Result |
  |---|---|
  | `if not decls[0].group(1):` → `if False:` | killed: `FAIL an unexported symbol is refused`, `FAIL an unexported symbol says so`, 52 of 54 |
  | `if len(decls) > 1:` → `if False:` | killed: 2 FAIL, 52 of 54 |
  | unterminated block comment tolerated (`raise` → `j = n - 2`) | killed: `FAIL an unterminated comment is refused`, 53 of 54 |
  | backslash-escape skip in strings (`if text[j] == "\\":` → `if False:`) | **survives**, 54 of 54 (Finding 2) |
  | newline-in-quoted-string refusal (`if j < n and text[j] == "\n" and c != "`":` → `if False:`) | **survives**, 54 of 54 (Finding 2) |

## Criteria

1. **The diff is exactly the stated change: holds.** See the independent
   application. `--check` reports the package current.
2. **No contradiction with an inherited base rule: holds.** `inheritedRules`
   (builder :244, patch) gives one reading of `classificationOrder` and
   `classificationSuccess`. The active-content rule is unchanged (:226).
3. **Each loosening is stated and bounded: holds.** Storage is limited to the
   run directory and rendering to a local draft. Two routes sit beside
   `networkEgress: false`. Logging and machine response stay `never` (builder
   :230-242).
4. **RFC5-14 soundness: holds.** `work-history` is never classified,
   `project-documentation` is absent and indeterminate content fails closed.
   The instruction-text rule is closed at two symbols.
5. **Extension list labelled [Inferred]: holds.** It is labelled at builder
   :63 and in the delta's Classification row.
6. **Read-gate consequence: holds.** `body-read-authority.ts:444`
   (`exact-digest-wrong`) refuses first, which the simulated Vitest failure
   shows.
7. **Sweeps honest: hold for Sweeps 1 and 2.** For the record figure's
   predicate, see Finding 3.
8. **Authority: holds.**
9. **Round-1 repairs: hold.** No change since round 3 touched them, and I
   found no regression.
10. **Round-2 repairs: hold.**
    - `targetMetadataRule.fields` is still read from `pipeline.ts`.
    - `exclusionMetadata` stays absent and is guarded by a selftest predicate.
11. **The exclusion-reason set is structural: holds, with notes.**
    - The rule names the symbol and lists no reason.
    - `--check` exits 1 without `--pending-symbol`.
    - The manifest is independent of the values.
    - The selftest refuses an absent, unexported, computed, empty or repeating
      set.
    - Q7 asks only to confirm.
    - The fail-closed claim is overstated for two exotic shapes (Finding 1).
12. **Round-3 repairs hold at these bytes, except where noted:**
    - **F1 (revise): repaired for every shape the round-3 raw named.**
      `mask_source` (builder :89-122) blanks comments and replaces string
      bodies. The reader requires exactly one live, exported declaration
      (:137-143).
      - Each of the five round-3 shapes now has a fixture (:532-538), and each
        passes.
      - The two built-in mutants are killed.
      - Residual gaps are in Findings 1 and 2. They are notes because the
        reader is not part of the bound bytes (see the independence result) and
        can be repaired after an act without moving the argument.
    - **F2 (revise): repaired.**
      - Patch :125 now reads "so the set cannot differ from the values the
        constant declares. A reason outside that constant is not carried".
      - "generator emits" occurs nowhere in the patch or the builder. A
        `grep -F` over both found it only in the brief, the dispositions and
        the round-3 raw.
      - The rule no longer contradicts itself.
    - **F3: repaired.** Packet Q7 (:72-89) names
      `body-not-retained-for-generation` and the free-string pass-through of
      `unknownReason`. Both are confirmed at
      `apps/three-surface-poc/src/polaris-generation/source-adapter.ts:18-22`.
      Q7 also asks that the constant cover reasons from outside
      generation-source.ts.
    - **F4: repaired.** There are three distinct messages, each with its own
      fixture (:552-554). My `if False:` mutant of the export guard is now
      killed (52 of 54).
    - **F5: the figure is repaired; its predicate is not.**
      - 61 and the 6 own-package files re-derive exactly from the simulator.
      - The predicate written beside them yields 49 (Finding 3).
      - The status-page row now names both battery lines (ledger :69).
    - **F6: repaired.** Delta :56-58 says "three rules for the four
      populations", with envelope-control produced by the two
      `instructionTextRule` symbols.
    - **F7: repaired.**
      - The rule (builder :214) says that an excluded source's `sourceId` "is
        an opaque identifier not derived from its path or body".
      - It labels that [Inferred], enforced only by the reader implementation.
      - The delta's Target metadata row (:36) carries it.

## Findings

**Finding 1 — The masking scanner still fails open on two valid shapes: a nested template literal and a regex literal holding a quote** (note)
`scripts/build_public_source_screening_scope.py:109-119` treats a backtick
string as running to the next backtick, so it ignores `${ … }` nesting. It
also does not recognise regex literals, so a quote inside `/…/` opens a
"string".

- **Fixture A:**
  ``const x = `${`; export const GENERATION_EXCLUSION_REASONS = ['a'] as const; `}`;``.
  This is a template whose `${}` expression is itself a template literal. Node
  loads it with zero exports, yet the reader returns `['a']`.
- **Fixture B:**
  `const r = /'/; // '; export const … = ['a'] as const;`. The declaration is
  in a line comment. Node loads it with zero exports, yet the reader returns
  `['a']`.

In both cases `readiness()` would report the package act-ready while the
symbol is absent from code.

The docstring (:93-94) discloses that "regex literals are not recognised" and
says that "a source it cannot scan to the end is refused". Neither covers a
source it scans to the end wrongly, and template nesting is not disclosed at
all. Criterion 11 ("fails closed on an absent … set") and dispositions F1
therefore overstate the guarantee.

The shapes are contrived. The reader is outside the act-bound bytes. Q7 also
has the owner read the values at the act commit. For those three reasons this
is a note.

Two repairs would work:
- refuse, fail-closed, any source in which a template contains `${` or a `/`
  survives masking outside a comment;
- or read the symbol through the TypeScript compiler API already in
  `node_modules`, or by importing the built module and comparing.

Separately, fixture H (`export let …`) is accepted. The rule and Q7 say
"exported constant", so `let`/`var` at :137 should be refused.

Violates: brief criterion 11 (fail-closed claim, overstated); AGENTS.md
verification rule 6 (no fixture reaches these shapes).

**Finding 2 — Two scanner branches have no killing fixture** (note)
Two mutants survive at 54 of 54:
- the backslash-escape skip inside strings (builder :112-113, guard replaced
  by `if False:`);
- the newline-in-quoted-string refusal (:114-115, replaced by `if False:`).

Both branches decide where a string ends, so a regression in either can move
live code into a "string" or out of one. Add one fixture each: an escaped
quote before a live declaration, and an unterminated single-quoted string
across a newline.

Violates: AGENTS.md verification rule 6.

**Finding 3 — The ledger's record figure states a predicate that does not produce it; "The five are" lists six** (note)
`IMPACT-LEDGER.md:55-59` gives the predicate of the 61 as "a `str.count` above
zero of the old policy file's SHA-256 or of `1.1.0-candidate.1`". Over the
same population that predicate gives **49**.

The 61 comes from the simulator's six literals
(`simulate_public_source_screening_scope_act.py:106-117`): the digest, the
version, the performed act's `actIdentity` and `recordingTag`, and the two
act-record pointers. The ledger's own :37-39 lists those six. The 12 files
reached only by the four extra literals include
`pwb-truth-policy-amendment/OWNER-DECISION-PACKET.md` and `SEMANTIC-DELTA.md`,
`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md` and nine `docs/evidence/` files.

Separately, :59 says "The five are" and then names six files: the ledger, the
delta, the patch and three raws. Six is correct, as :54 says.

Restate the predicate as the simulator's six literals and change "five" to
"six". This is ledger prose, outside the manifest.

Violates: AGENTS.md verification rule 9 and the "publish the regex" lesson.
The figure is right and its stated predicate is wrong.

**Finding 4 — The brief still calls itself the round-3 brief and records to `-3-RAW.md`** (note)
`REVIEW-BRIEF.md:1` ("(round 3)") and :3-4 ("this is the round-3 brief") are
stale now that criterion 12 asks for round 4. The Recording section
(:81-82) names `R-PUBLIC-SOURCE-SCREENING-SCOPE-3-RAW.md`, a file that already
exists. A reviewer following the brief literally would collide with a
retained raw. Its "(a re-issue is a further `-RAW.md`)" saves it only
partly.

Violates: none; legibility and CC-REV-6 hygiene.

**Finding 5 — The single-quoted half of the string-embedded fixture is not valid TypeScript** (note)
Builder :534 writes `const t = '{decl}';`, where `decl` itself contains
`'a-b', 'c'`. Real TS would reject the line as a syntax error. It passes
because the scanner happens to tokenise it so that the declaration falls
inside a string.

Only the double-quoted half exercises the claim, and the round-3 disposition
counts the fixture as covering string embedding generally. Use an escaped or
double-quoted inner form so the fixture is valid source.

Violates: none; rule-6 fixture hygiene.

## Verdict

CONFIRM WITH EXCEPTIONS. Findings 1 to 5 are notes. There is no revise-level
finding.

Both round-3 revise findings are repaired in the bytes:
- The patch's `reasonRule` sentence is now true.
- The reader no longer accepts any of the five commented or string-embedded
  shapes the round-3 raw named.

The manifest digest re-derives. Its bytes are independent of the constant's
values. The 61/6 record figure reproduces under the simulator.

The residual reader gaps (Findings 1 and 2) concern a builder tool outside the
argument. They should be closed before the constant lands and an act is
offered.
