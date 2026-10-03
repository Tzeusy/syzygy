# R-PUBLIC-SOURCE-SCREENING-SCOPE-3 — fresh-context round-3 review of the public-source screening scope package
Reviewed commit: 31790ac7572c6866fe59fcefc7aae070340e4fa3
Manifest SHA-256: eec6e163390564d91ed7a55e64ee261118c08668d2a364e5385129be49c9ece3
Verdict: REVISE

Reviewer: fresh-context agent, 2026-10-03. A detached scratch worktree at the
reviewed commit was used read-only. Mutations and `--write` runs used a
`git archive` copy. The simulation used the script's own `git clone --shared`
scratch clone. No tracked file was edited, no external repository was read
and no model provider was called. Another branch of this repository was read
by ref: `origin/polaris/public-repo-admission` at `8bcec860` (the admission
package, PR #215). The head digest is `sha256sum` of the manifest file. It
agrees with `--manifest-digest --pending-symbol`.

## What was run

- `build_public_source_screening_scope.py --check` printed `public-source screening scope: current`,
  then `FINDING not ready for an act: GENERATION_EXCLUSION_REASONS is not exported from packages/polaris-generation-core/src/generation-source.ts`.
  Exit 1.
- `--check --pending-symbol` printed the same line as `NOTE`. Exit 0.
- `--manifest-digest` without the flag refused. Exit 1.
- `--manifest-digest --pending-symbol` printed the digest in the head. Exit 0.
- `--selftest`: `selftest: 39 of 39 predicates held`, exit 0.
- Independent application: `patch -p1` over a `git archive` copy of the policy
  hashes to the manifest row (`1780d59f…`). Parsed as JSON:
  - added `['publicSourceScope']`, one position after `scope`;
  - removed none;
  - changed `['policyVersion']` only.
- `python3 scripts/check_governance.py` at the reviewed commit:
  `31 OK, 21 WARN, 0 FAIL (52 checks)`, exit 0.
- `simulate_public_source_screening_scope_act.py --tests --json`, with TMPDIR
  in the scratchpad. Failed:
  - repin builder `--check`;
  - repin recorder `--check policy`;
  - `check_governance` (CG-7e, 6 findings);
  - Vitest `governance-inputs.test.ts`, `content-classification.test.ts` and
    `git-object-reader.test.ts`.

  Passed: `npm ci` and Vitest `project-shape-model.test.ts`.

  The script reported 2000 tracked files and 60 record files. These agree with
  the ledger's check table row by row.
- Sweeps were run by Python over `git ls-tree -r -z` plus `git show`, a method
  different from the ledger's:

  | Commit | Tracked files | Sweep 1 hits | Sweep 1 code | Sweep 2 | `1.1.0-candidate.1` files | Of them under `scripts/` |
  |---|---|---|---|---|---|---|
  | `c540438d` | 1975 | 52 | 14 | 15 | 8 | 3 |
  | Reviewed commit | 2000 | 57 | 15 | 15 | 8 | 3 |

  The 14 code paths at `c540438d` are the ledger's 14 names.
- Criterion 8: the four package Markdown files carry 0 standalone 64-hex tokens.
  Each retained raw carries 1, its own head. The `adopted`/`accepted`/`approved`
  hits are the provenance-state label `owner-adopted (bootstrap, uncorrelated)`
  (packet :19) and the brief's own criterion text. Nothing is labelled accepted.
- Criterion 11, independence: I appended
  `export const GENERATION_EXCLUSION_REASONS = ['oversize-source-excluded', 'body-not-retained-for-generation'] as const;`
  to `generation-source.ts` in the archive copy and re-ran `--write`. Patch and
  manifest hashes were byte-identical to the committed ones. `--check` then
  exited 0, and `--manifest-digest` printed the same digest. I added a third
  member (`'empty-file'`) and re-ran `--write`: still identical. The manifest
  bytes are independent of the constant's values.
- Rule-6 mutations of my own on `exclusion_reasons`, each on a fresh copy of
  the script:

  | Mutation | Result |
  |---|---|
  | drop `or len(set(reasons)) != len(reasons)` | `FAIL a repeated reason is refused`, 38 of 39, exit 1 |
  | drop `leftover` from the refusal condition | `FAIL a non-literal member is refused`, 38 of 39 |
  | `if not re.search(rf"export\s+const\s+{sym}\b", text):` replaced by `if False:` | survives, 39 of 39 (Finding 4) |

  The script was restored and `diff -q` against the worktree copy was clean.
- Reader probes over 14 source shapes (Finding 1). Refused as claimed:
  - double-quoted members;
  - a missing semicolon;
  - `satisfies`;
  - `Object.freeze`;
  - an uppercase member;
  - a `]` inside a comment;
  - a block-commented member.

## Criteria

1. **The diff is exactly the stated change: holds.** See the independent
   application above.
2. **No contradiction with an inherited base rule: holds.** `inheritedRules`
   (patch :169) gives one reading of `classificationOrder` and
   `classificationSuccess`. Active content is unchanged (patch :144).
3. **Each loosening is stated and bounded: holds.** The loosenings are storage
   in the run directory, rendering in a local draft, and two routes beside
   `networkEgress: false`. Logging and machine response stay `never`.
4. **RFC5-14 soundness: holds, with notes.** The instruction-text rule is
   closed. `promptForStage` and `stageSchema` also yield the two
   envelope-control version labels (`prompts.ts:31`, `provider-draft.ts:70`,
   used at `pipeline.ts:258`). See Findings 6 and 7.
5. **Extension list labelled [Inferred]: holds.** It is labelled in delta :32,
   packet Q3 and builder :63.
6. **Read-gate consequence: holds.** The simulation shows `policy:exact-digest-wrong`
   where the test expected `policy:superseded`, so the digest refuses first.
7. **Sweeps honest: hold.** The figures are above; for the record count, see
   Finding 5.
8. **Authority: holds.**
9. **Round-1 repairs hold at these bytes:**
   - F1: see criterion 10, F1.
   - F2: delta :90-97.
   - F3: delta :70-86, builder docstring :14-20.
   - F4: patch :144 and predicate "active content loosened".
   - F5: patch :93 and predicate "indeterminate reading dropped".
   - F6: delta :59-68, packet Q5.
   - F7: patch :57.
   - F8: delta :39.
   - F9: delta :99-106.

   No round-1 repair introduced a defect.
10. **Round-2 repairs hold at these bytes, except where noted:**
    - F1: the ledger tables match the simulation output (see Finding 5).
    - F2: `targetMetadataRule.fields` equals the `sourcePopulation` entry at
      `pipeline.ts:237-238`. Both the inventory `sourcePopulation` row and the
      plan `sources` row of the confirmed egress table
      (`EGRESS-CONSENT-ANTHROPIC.md` rows at :79 and :82, admission branch
      `8bcec860`) send that object (`pipeline.ts:393-394`). `exclusionMetadata`
      is gone, and its return is a selftest predicate.
    - F3: builder :14-20 and :63-64.
    - F4: ledger :68-70 / :25-27.
    - F5: "the other way round".
    - F6: packet Q8.
    - F7: packet Q6.
    - F8: brief :49-51.

    Round 3 adds the reason-symbol change, which introduced Findings 1 and 2.
11. **The exclusion-reason set is structural: partly.**
    - The rule lists no reason and names the symbol (patch :121-124).
    - The symbol must exist before the act: `--check` exits 1 without
      `--pending-symbol`.
    - The manifest is independent of the constant's values.
    - Packet Q7 asks only to confirm.
    - Two things fail:
      - the reader does not fail closed on an absent symbol in every shape
        (Finding 1);
      - one sentence of the rule is false (Finding 2).

## Findings

**Finding 1 — The constant reader accepts commented-out and string-embedded declarations and members** (revise)
`scripts/build_public_source_screening_scope.py:98-105` matches the
declaration and the members with regexes over raw text. Neither comments nor
strings are removed first. Probed on a scratch `generation-source.ts`:

| Source shape | Reader result |
|---|---|
| `// export const GENERATION_EXCLUSION_REASONS = ['a'] as const;` (no live declaration) | `['a']` |
| `/* export const … = ['a'] as const; */` (no live declaration) | `['a']` |
| a string literal containing the declaration | `['a']` |
| a live array with `// 'retired',` as a commented line | `['a', 'retired']` |
| a commented old declaration above the live one | `['old']`, the stale values rather than the code's |

`:104`'s `findall` runs over the whole bracket body, comments included. In the
first two shapes the symbol is absent from code, yet `readiness()` returns
`[]` and `--check` reports the package act-ready. In the last two, the set
printed for the owner to confirm at act time (Q7, "read its values at the act
commit") differs from what the code holds.

The selftest's "an absent symbol is refused" (:475) tests only a differently
named symbol, so the shapes above are unexercised. The docstring (:90-92) and
the brief (criterion 11, "fails closed on an absent … set") claim fail-closed
behaviour that the reader does not have. Fix: strip `//` and `/* */` comments
and string bodies other than the members before matching, require exactly one
live declaration, and add a fixture for each shape above.

Violates: brief criterion 11; AGENTS.md verification rule 6, because a
predicate exists for "absent" but no mutation reaches the commented form.

**Finding 2 — `reasonRule` states that the set "cannot differ from what the generator emits", and its next sentence contradicts that** (revise)
Patch :125 (manifest-bound bytes) says: "this policy lists no reason, so the
set cannot differ from what the generator emits. A reason outside that
constant is not carried, and the generator's validator refuses it". The second
sentence, and packet Q7 (:72-84), contemplate an emitted reason outside the
constant. The base already emits reasons that no constant holds yet (Finding
3). What the rule achieves is that the set cannot differ from what the
constant declares. These bytes become the act argument, and once an act binds
them no edit is lawful. Replace "what the generator emits" with "the values
the constant declares" before review closes.

Violates: brief criterion 11 ("whether the rule's wording is sound"); RFC5-14
"Classification is determinable" only indirectly. The operative rule (outside
the constant, not carried) is unambiguous.

**Finding 3 — Q7 understates what the base already emits as an exclusion reason** (note)
`OWNER-DECISION-PACKET.md:76-78` says the engine emits
`oversize-source-excluded` "on the base" and other reasons on other branches.
[Observed] At the reviewed commit, the app adapter
`apps/three-surface-poc/src/polaris-generation/source-adapter.ts:17-22` also
emits `body-not-retained-for-generation`. It also passes the PWB classifier's
`unknownReason` through as `reason` for excluded and unavailable sources. The
type is `string` (`generation-source.ts:20`), and no closed set exists. The
constant the generator's lane must write therefore has to enumerate reasons
that originate outside `generation-source.ts`, in the app and in the PWB
classifier. Otherwise the validator Q7 describes refuses real runs. This does
not change the bytes; it scopes the lane request.

Violates: none; owner-facing precision.

**Finding 4 — The reader's `export` pre-check is redundant, so its mutation survives** (note)
Replacing the `:98` guard with `if False:` leaves `selftest` at 39 of 39,
because the `:100` regex also requires `export\s+const`. The unexported case
is still refused (with the "cannot read … as a literal array" message instead
of "is not exported"). There is no behavioural gap. The distinct message
`--check` prints today has no predicate of its own.

Violates: none; AGENTS.md rule 6 hygiene.

**Finding 5 — The ledger's record count and one status-page row** (note)
- `IMPACT-LEDGER.md:53-54`: "59 governance records that cite the old bytes;
  they bind and are not edited". At the reviewed commit the simulation reports
  60. Five of them are this package's own candidate files, which bind nothing:
  `IMPACT-LEDGER.md`, `SEMANTIC-DELTA.md`, the patch and both raws. The
  population should be stated, or the package excluded.
- `:62` names only the re-pin act's `--check policy` line in
  `PROJECT-STATUS.md` (:378). The simulation also fails
  `build_pwb_behavior_contract_repin.py --check`, which is battery line :376
  and carries no digest literal. Packet Q2 says "battery lines", plural, so
  the continuation covers it. The table does not.

Violates: AGENTS.md verification rules 4 and 9 (denominator), minor.

**Finding 6 — "one per population" counts three rules for four populations** (note)
`SEMANTIC-DELTA.md:55-57` says the three rules are "one per population the
generated carried-content table names". The confirmed table also names
`envelope-control` (`promptVersion`, `responseSchemaVersion`). It is covered,
because `instructionTextRule`'s two symbols produce both labels (see criterion
4), but by the instruction-text rule rather than a fourth rule. Suggested
wording: "the three rules cover the four Syzygy-side and metadata populations;
envelope-control is produced by the instruction-text symbols".

Violates: none; legibility.

**Finding 7 — "A path of an excluded source is not carried" rests on an unconstrained `sourceId`** (note)
Patch :120 promises that no excluded-source path is carried. `sourceId` is in
the field list, but the rule does not constrain how it is derived.
`SOURCE_ID_PATTERN` (`provider-draft.ts:20`, `^[A-Za-z0-9][A-Za-z0-9_.:-]*$`)
admits flat basenames such as `README.md`. The PWB adapter hashes an identity
(`source-adapter.ts:15`), but the public-target reader is not written, and
nothing in the bytes requires it to do the same. A public target's path is
`code-structure` either way, so no class is breached. The promise, however,
is enforced only by an implementation choice.

Violates: none; the promise should name the derivation ("an opaque id not
derived from the path or body") or be dropped.

## Verdict

REVISE. Findings 1 and 2 are revise. Findings 3 to 7 are notes. The rule's
structure is sound: it names a symbol, lists no reason, and its bytes are
independent of the values. The act-readiness gate it relies on fails open on
commented and string-embedded shapes, and one sentence of the to-be-signed
rule is false.
