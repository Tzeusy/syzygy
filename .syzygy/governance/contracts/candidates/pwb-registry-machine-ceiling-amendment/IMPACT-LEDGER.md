# Impact ledger — P-114, the 16 MiB machine-answer ceiling

> **Candidate — binds nothing.** What signing this package would move, and
> what must move with it. The proposal is `SEMANTIC-DELTA.md`.

## Method

All sweeps were run 2026-10-20 on this branch, off origin/main `8340fa22`:

1. **Literal sweep, first method.** A Python sweep over `git ls-files`
   counted lines matching `8388608|8,388,608`. It decoded 2,854 tracked
   files and skipped 4 undecodable ones. **40 files** carry the literal:
   22 under `docs/evidence/`, `docs/reviews/` and `docs/pursuits/`, and the
   18 listed in part A.
2. **Second method.** `git grep -l -F` for `8388608`, `8,388,608` and the
   key `maxMachineResponseBytes` returns 73 files. They are the 40 above,
   plus files that name the key without the value: code that passes the
   limit identity, tests that set a fixture value, and historical docs.
   `git grep -l -F -e "8 MiB" -e "8 MB"` returns 18 files, 7 of them
   outside those 73. Three of the seven name this machine ceiling in prose
   and are listed in part A. The other four are false positives (`128 MiB`,
   `256 MiB`, `2.13 MB`, size prose). *(Corrected after round 1, finding
   4a: the first version said the prose sweep added no file.)*
3. **Dry run.** Apply the one-value patch in the working tree, run two
   suites, then revert:
   - the whole PROJECT-STATUS battery (105 checks plus the `git tag` line).
     Before the patch, 0 non-zero commands. With the patch, **7 non-zero**;
   - the full non-browser vitest suites of both POC packages
     (`npx vitest run packages/three-surface-poc-core apps/three-surface-poc`,
     2,017 tests in 124 files). Before the patch, 0 failed. With the patch,
     **5 failed** in 2 files: 4 in `governance-inputs.test.ts` and 1 in
     `project-shape-observation.test.ts`. *(Widened after round 1, finding
     4b: the first dry run ran only the gate's two test files.)*

   Browser tests were not run. Every failure is listed in part B.

## A. Every place that hard-codes the value

| File | Line(s) | Kind | At sign-off |
|---|---|---|---|
| `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` | 271 | the subject | patched by this package |
| `packages/three-surface-poc-core/src/project-shape-observation.ts` | 82 | **the value the daemon enforces** (`PWB_RESOURCE_LIMITS`) | changed under ask 2 |
| `apps/three-surface-poc/src/response-limits.test.ts` | 302 | test literal (`toBe(8388608)`) | changed under ask 2 |
| `packages/three-surface-poc-core/src/resource-headroom.test.ts` | 34, 51 | test literals (declared ceiling) | changed under ask 2 |
| `packages/three-surface-poc-core/src/project-shape-model.test.ts` | 923 | test literal (declared ceiling) | changed under ask 2 |
| `scripts/build_pwb_registry_currency_briefing_amendment.py` | 362 | a selftest mutant of the `.18` package's subject | rewritten with that builder's successor (part B) |
| `openspec/changes/polaris-project-wide-butlers-model/design.md` | 380 | "Values recommended at drafting … The registry entry, not this design, declares the values in force." | unchanged. It records the drafting recommendation and defers to the entry. The file is act-bound and may not be edited |
| `.syzygy/governance/contracts/candidates/pwb-readability-successor/proposed/design.md.patch` | 302, 667 | the same design sentence inside a performed successor's patch | unchanged (performed history) |
| `.syzygy/governance/contracts/candidates/pwb-registry-currency-briefing-amendment/SEMANTIC-DELTA.md` | 81 | performed `.18` package prose | unchanged (performed history) |
| `.syzygy/governance/contracts/candidates/pwb-registry-currency-briefing-amendment/proposed/…json.patch` | 25, 26 | the performed `.18` patch's own `-`/`+` lines for this key (`.18` added the trailing comma and `maxBriefingResponseBytes`) | unchanged (performed history). **Its `+` line is the line this package changes**, so reversing `.18` directly over the patched subject no longer applies. Successors 1 and 2 (part B) must first reverse this package's patch to recover act B's bytes, then reverse `.18` |
| `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/SEMANTIC-DELTA.md` | 92 | performed package prose | unchanged (performed history) |
| `.syzygy/governance/contracts/candidates/pwb-truth-policy-amendment/OWNER-DECISION-PACKET.md` | 76, 85, 137 | "8 MiB" prose, performed packet | unchanged (performed history) |
| `docs/reviews/R-IMPL-P100-GOVERNING-INTENT-1-RAW.md` | 37 | "8 MiB" prose, raw review | never edited (CC-REV-6) |
| `docs/reviews/R-PWB-TRUTH-POLICY-COMPREHENSION-CONFIRMATION-RAW.md` | 21 | "8 MiB" prose, raw review | never edited (CC-REV-6) |
| `.syzygy/governance/decisions/POLARIS-RESPONSE-CEILING-READING-DECISION-PACKET.md` | 161 | the P-77 reading packet, which describes the ceiling at the time | unchanged. Its reading ("final encoded HTTP body") is value-independent, and `check_polaris_response_ceiling_reading.py` quotes only the semantics sentences, which this package keeps |
| `docs/design/POLARIS-M5-…`, `-M9-…`, `-M10-…`, `-M12-…` funnels | as listed by the sweep | design history | unchanged (dated design records) |
| `docs/plans/2026-10-03-smooth-example-roadmap.md` | 56 | plan history | unchanged |
| `docs/polaris-generation/REDIS-DOSSIER-GAP-ANALYSIS.md` | 216 | an analysis citing the Butlers ceiling | unchanged (dated analysis) |
| 22 files under `docs/evidence/`, `docs/reviews/`, `docs/pursuits/` | — | measurements, raws and harvests | never edited (rule 11; CC-REV-6 for raws) |

Tests that set the limit to a fixture value (`maxMachineResponseBytes: 64`,
`0`, `5`, `size - 1`, `400`) assert behaviour relative to the value they
set, not to 8 MiB. They are untouched.

**How the daemon reads the ceiling.** [Observed] It does not read the
registry entry. `PWB_RESOURCE_LIMITS` is a literal object in
`project-shape-observation.ts:75-83`, and `routes.ts` receives it as
`limits`. A signed entry alone therefore changes nothing served. The value
takes effect only through the code change in ask 2, so that change needs
its own owner authorization. The 2026-10-15 implementation direction
(`decisions/OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md`)
names its amendments one by one and does not cover this entry.

### A2. Readers of the entry's bytes *(added after round 1, finding 4b)*

| Reader | What it reads | Effect of the patch |
|---|---|---|
| `packages/three-surface-poc-core/src/project-shape-observation.test.ts` (lines 758–790, "registry-bound constants") | the installed entry's identity, `resourceLimits` and failure states, compared to the code constants | fails until item 1 of ask 2 lands, and fails on item 1 without the patch. This test is what keeps the entry and the constant in step |
| `packages/three-surface-poc-core/src/project-shape-manifest.test.ts` (line 576) | `maxIndexDepth` only | none |
| `apps/three-surface-poc/src/governance-inputs.ts` and `walkthrough-inputs.ts` (path only) | the entry's bytes, digested by the PWB-REQ-005 gate against the act record | refuses every Butlers read until the pointers move (B1) |
| the builders and recorders in B2 | the entry's bytes, against performed acts' arguments | fail until their successors land (B2) |
| `walkthroughEvaluationIdentity` (`walkthrough-readiness.ts`), through `resourceLimitsDigest` (`project-shape-observation.ts:622`) and the registry act identity | the limits the code carries, and the act | the `pwb-eval-…` identity changes, so a walkthrough record bound to the old identity reads as an evaluation mismatch [Inferred: expected, harmless] |

## B. What signing breaks unless it moves in the same commit

### B1. The body-read gate refuses every Butlers read [Observed, dry run]

`apps/three-surface-poc/src/governance-inputs.ts` points the registry
authority at act B: `PWB_ACT_RECORDS.registry` (line 61), its act identity
(line 110), its recording tag (line 113), and the supersession target
(`PWB_SUPERSEDED_ACT_RECORDS.registry`, line 66). Act B's record names the
entry's current digest. With the entry patched and the pointers unmoved, the
direction-C case of `governance-inputs.test.ts` (line 316) gets
`admits: false`, and 3 more cases in that file fail (4 in all). On a live daemon that
would be an Unknown project shape on every surface. It is fail-closed, but
it is still an outage.

Code moves under ask 2:

- the four pointers above, to the new record, its act identity, its tag
  `pwb-registry-machine-ceiling-amendment-v1.0` and the act B record as the
  supersession target. The scope anchors (`1.2.0-candidate.1` and the rest)
  stay, because the entry's versions do not move;
- the literals pinning act B in `governance-inputs.test.ts` (lines 188,
  262, 309, 311), plus the comment block above the pointers.

### B2. Battery checks that read this subject (7 non-zero in the dry run)

| Check | Dry-run failure | Successor (ask 2, item 4) |
|---|---|---|
| `check_governance.py` CG-7e | 5 findings: the act phrase `ADOPT POLARIS BUTLERS PROJECT-SHAPE OBSERVER REGISTRY ENTRY` is registered with act B's record, the re-pin manifest, `ACCEPTANCE-ACT-RECORD.md` and `PROJECT-STATUS.md` as copies of its current argument | **ask 2, item 5**: register the new record and its copies, and move act B's copies to performed history. This is the registration every digest-bound act gets |
| `build_pwb_registry_currency_briefing_amendment.py --check` | the subject with `.18` reversed no longer hashes to the `.18` act's argument | **successor 1**: name this package's manifest row explicitly as the one later performed act over the subject. Recover act B's bytes by reversing this package's patch, then reverse `.18` (its `+` line is the line this package changes). Same pattern as `PERFORMED_SUCCESSORS` in `build_pwb_registry_loaded_profile_amendment.py`, which names specific packages |
| `build_pwb_registry_currency_briefing_amendment.py --selftest` | same cause ("does not verify on current bytes") | covered by successor 1 |
| `record_pwb_registry_currency_amendment.py --check …` | same cause | **successor 2**: the same explicitly named row |
| `build_pwb_behavior_contract_repin.py --selftest` | `base_bytes` raises: the subject is not act B's argument | **successor 3**: `base_bytes` recognises this package's manifest row, named explicitly |
| `record_pwb_behavior_contract_repin_acts.py --check registry …` | "registry subject hashes to … not the owner argument" | **successor 4**: the same explicitly named row, for the registry act only |
| `check_spec_reconciliation.py --selftest` | raises through `build_pwb_behavior_contract_repin.base_bytes` | covered by successor 3; no change of its own |

The two `--check` lines for this package's own record and builder join the
battery (the CG-26 triple: battery block, hosted workflow, count sentence)
in the same commit.

### B3. The recording itself (named in ask 2 after round 1, finding 5)

The gate reads only a record carrying the phrase form
`<PREFIX>: <64-hex>` and an `Exact digest (SHA-256):` line
(`packages/three-surface-poc-core/src/body-read-authority.ts`, the `PHRASE`
pattern at line 336). A version-tagged sign-off record written by
`record_versioned_signoff.py` does not carry either today. Recording this
sign-off therefore needs a dedicated recorder. The precedent is
`record_public_source_screening_scope_v3_act.py` (2026-10-08). The owner
answers a structured question and types nothing. The recorder derives the
phrase argument from this package's manifest row, writes the record with
`Supersession / revocation:` naming act B for the registry role, appends
the aggregate block, and names the version tag
`pwb-registry-machine-ceiling-amendment-v1.0` as the recording tag. That
recorder is written by the signing lane, not by this package, and ask 2 item 5 names it. [Inferred] The
same holds for P-112, whose recorder does not exist yet either.

## C. Sibling packages on the same subject (unperformed)

- **P-112**, the loaded-profile amendment
  (`contracts/candidates/pwb-registry-loaded-profile-amendment/`). Its
  builder recognises a base only through `PERFORMED_SUCCESSORS`. After this
  sign-off its `--check` fails closed until this manifest is added there and
  its row is re-minted with `--write`, which needs a further review round.
  Its patch does not touch line 271 [Inferred, from reading its hunks], so
  only the row moves. It is not in the battery.
- **P-95**, the tree-framing re-pin
  (`contracts/candidates/pwb-behavior-contract-repin-tree-framing/`),
  already stale and awaiting redraft (`syzygy-fxro`). Its redraft rebases
  over whichever entry bytes are current.

Neither package is edited here.

## D. Not changed, and why

- `maxHumanResponseBytes`. [Observed] `/trajectory` is 1,672,253 of
  2,097,152 bytes on 2026-10-20 and growing about 84 KB a day [Inferred].
  The cause is Trajectory's selection rule ("all non-closed items, plus the
  N most recently closed"), which grows with the open-item count. Signed
  POC-REQ-042 does not fix that rule, so capping it is implementation under
  the existing authorization (bead `syzygy-blbu`). It is not a ceiling
  question.
- The P-100 implementation was reverted on 2026-10-20 (PR #474) to restore
  `/api/poc`. Re-landing it waits for this raise or for P-115.
- P-86 waits for this raise, per the owner's direction.
