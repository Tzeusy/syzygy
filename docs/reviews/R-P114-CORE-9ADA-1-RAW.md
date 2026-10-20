# Review — P-114 machine-ceiling installation core, first frozen checkpoint
Reviewed commit: 9adae4f2935f2e82bb295eb6d6683a8d1c3a2bda
Base commit: 03178a5483c5434780fc6c3b379b9006c9ae740e
Verdict: REVISE

[Observed] This is an independent core implementation review in a fresh isolated clone. The subject is the 17-file diff from the base above, after incorporation of landed P-110 `7c152bd64e4a3513917b409461f6ae25fd315871`. Governing inputs are the unchanged reviewed P-114 proposal, its round-2 raw/disposition, canonical paired approval direction, retained preliminary plan/review and the cited doctrine/craft/RFC predicates. This review does not cover final battery/workflow/count/status integration, final CI, the actual main version tag or private runtime measurement; those remain separately held.

[Inferred] The bounded implementation is coherent in its central path: one approved registry leaf and matching evaluated runtime constant move to 16 MiB, the registry gate follows the new exact act while retaining P-110's policy authority, and the recorder preserves the actual attended Codex reply `yes, approve both` without claiming the owner typed a digest or derived phrase. The preliminary tag-selector finding is corrected using exact expected refs. Two correctness gaps remain in transaction input preservation and the named historical link's malformed-field handling.

## Findings

**Finding 1 — The transaction snapshots inputs after stale aggregate output was constructed** (revise)

Severity: Important. Source: `scripts/record_pwb_registry_machine_ceiling_act.py:302–337`, especially lines 303, 310–311, 330 and 335–337.

[Observed] `record()` reads the aggregate before `expected()`, then constructs `aggregate + block`. `transaction()` separately reads the current files as its `before` snapshot only after those output bytes have been constructed. Its input-drift check therefore compares the staged operation with a later baseline, not with the inputs from which the approved output was derived.

[Observed] In the disposable unapplied accepting fixture, an independent append inserted at the transaction boundary is silently lost: `record()` returns successfully, installs the registry and new act, and replaces the aggregate with the earlier captured aggregate plus its block. The probe's inserted text is `Owner-preserved concurrent aggregate note.`. `core-independent-probes.json`, probe `aggregate-edit-after-validation-before-staging`, retains the input subject, exact mutation, before/after hashes and successful return. The aggregate hash immediately after the independent append differs from both its initial and final hashes; `concurrent_edit_retained` is false. A separate control, `during-stage-cas-control`, edits the aggregate while staging: that is correctly refused as `transaction input changed`, with the edit preserved and no dedicated record created. The defect is the earlier window, not lack of an existing drift predicate.

[Inferred] A user or another attended process can append an independent record during preflight and have that append overwritten even though the function appears to protect changed inputs. The same late-baseline pattern applies to a registry edit between its validation and transaction staging. This violates preservation of unrelated work and the approved recorder plan's preflight/atomic-failure discipline; canonical test-rigor rules 1 and 3 require the actual failure behavior at this filesystem seam. The owner packet Ask 2 item 5 authorizes only this transaction's recording machinery, not replacement of an independently changed aggregate.

Required bounded correction: carry the exact validated/read input snapshot into the transaction, require those same subject/record/aggregate inputs before replacement, and fail without overwriting an intervening edit. Keep the existing stage-time drift and six write-stage/replacement failure tests. Add an executing regression for the pre-transaction aggregate append and, where the same code path handles it, the validated-subject change. This requires no process-global lock system, changed act bytes or new owner choice.

**Finding 2 — The historical link accepts contradictory duplicate identity/type/target/tag fields** (revise)

Severity: Important. Source: `scripts/build_pwb_behavior_contract_repin.py:159–184`, called from `subject_at_act():309–326` and the approved currency/re-pin recorder recovery paths.

[Observed] `machine_ceiling_link()` requires one regex match for each expected identity, type, artifact and supersession line, and counts one occurrence of the expected recording-tag prefix. Those tests count occurrences of the correct value; they do not require exactly one total field value. Adding a conflicting line while retaining the expected line satisfies the predicate.

[Observed] Five independent disposable record mutations prepend a contradictory Act identity, Act type, Artifact identity, Supersession / revocation or recording-tag line to the corresponding correct line. For each of the five, `subject_at_act()` still returns the exact act-B registry digest. For each, the dedicated recorder's `check()` rejects the same tree as `dedicated record differs from exact regeneration`. Replacing the correct line with only the wrong line is refused by the historical link in each of the five paired controls. The complete old/new fragments, mutated record hashes and both layer outcomes are retained as `history-*-contradictory-duplicate` / `history-*-wrong-only` in `core-independent-probes.json`.

[Inferred] These are malformed records accepted by the shared historical predicate as the named performed successor, while its owning recorder rejects them. This is not an observed runtime authorization bypass: the dedicated recorder/actual evaluator remain distinct gates. It is a defect in the specifically approved fail-closed historical recovery predicate. Ask 2 item 4 confines each successor to this explicitly named performed amendment row; the preparation plan lines 132–139 and 185 require its expected record identity/type/tag/registry predecessor and refusal of forged or wrong link inputs. RFC3-16(b) binds the stable artifact identity, act type and supersession relationship; a contradictory duplicate is no single such binding.

Required bounded correction: extract and count the total population of each checked field, require exactly one, then compare its value with the named P-114 expectation. A strict bounded shared predicate is also acceptable. Cover identical duplicates, contradictory duplicates and malformed field values separately from the existing wrong-only tests; preserve the accepting control, exact digest/manifest/patch checks and registry-only scope. Do not edit predecessor records, reviewed package bytes, the policy chain or a generic parser/allowlist to accommodate malformed input.

## Verified scope and retained evidence

[Observed] Independent checks in the clean source clone completed as follows; outputs are retained beside this raw:

| Check | Observed result | Artifact |
|---|---|---|
| `npm ci`, then `npm run build:poc` | Completed; forced project build succeeded | `core-npm-ci.log`, `core-build.log` |
| Dedicated recorder `--selftest` | 54 fixtures, 0 failing; includes the six stage/replace failures and exact restoration controls | `core-recorder-selftest.log` |
| Dedicated recorder `--check` | Exact regeneration succeeds for installed row, retained review/selection and one aggregate block | `core-recorder-check.log` |
| Frozen proposal builder `--check` | Applied, verifies | `core-builder-check.log` |
| Recorder `--builder-selftest` | Runs the unchanged builder, not the recorder, through the existing helper at exact pre-install commit `03178a5483c5434780fc6c3b379b9006c9ae740e`; 22 of 22 predicates held | `core-builder-replay.log` |
| Re-pin builder `--selftest` | 51 fixtures, 0 failing, including named P-114 recovery | `core-history-selftest.log` |
| Focused parity, body-read authority, model/headroom, registry gate and HTTP boundary selection | 336 tests passed in six files, no skips in this run | `core-authority-parity-http.log` |
| Current-tree public screening, package policy/admission and dossier screen selection | 149 tests passed in three files; includes actual current decisions-tree positive reads and injected refusal controls | `core-closed-readers.log` |
| Independent record/history probes | 25 probes: twelve frozen-input record-entry refusals preserve outputs, staging-time drift refuses, the early drift is accepted/lost, valid history recovers, five wrong-only histories refuse and five contradictory duplicates recover | `core-independent-probes.json`, `core_independent_probes.py` |

[Observed] The six focused TypeScript files were `project-shape-observation.test.ts`, `body-read-authority.test.ts`, `resource-headroom.test.ts`, `project-shape-model.test.ts`, `governance-inputs.test.ts` and `response-limits.test.ts`, selected under the two POC projects. The three closed-reader files were app `polaris-generation/public-source-screening.test.ts`, consent package `real-tree.test.ts` and dossier `screen.test.ts`, selected under their three exact projects. The real governance-tree test in the focused run exercised the missing-new-version-tag branch; its Git stderr `Needed a single revision` is retained. It proves fail-closed behavior in this checkout, not actual tagged admission. Synthetic current-record positives remain separate.

[Observed] The root's 184-entry protected baseline was independently checked against this subject by SHA-256, byte length and Git blob identity; an independent `git diff` restricted to those same 184 paths lists no changed path. The proposal, reviewed raw/disposition, existing acts, canonical direction, policy and owner parser in that declared population remain unchanged. The preliminary raw retained at `docs/reviews/R-P114-IMPLEMENTATION-PREPARATION-137C-1-RAW.md` is byte-identical to the reviewer cache raw, SHA-256 `ca70afc58bf14e5586972f685e7d0dd2e1b847af2702b5abb2343db0beaa9acb`.

[Inferred] The test growth is bounded to three new TypeScript `it` cases, the dedicated recorder's 54 fixture outcomes and 14 historical-link fixture outcomes. These protect the new ceremony/tag discovery, transaction and named history behavior rather than duplicating the numeric constant's existing parity test. The two findings demonstrate missing edge coverage within that accepted behavior, so fixes belong in this change.

[Observed] Source review and probes changed no implementation or governed bytes in the frozen clone. Probe mutations occurred only in disposable fixtures outside the source checkout. No helpers were spawned, no provider or daemon started, no Butlers body read, no repository act/tag recorded by this reviewer, and no Beads, external comment or real branch/tag mutation occurred.

## Assessment

[Inferred] Core confirmation is withheld pending Findings 1 and 2 and independent review of the repaired frozen subject. Both are bounded source/test corrections under the existing approval; neither requires an owner question or a performed-act edit. The sign-off, evidence, security and truth floors remain the relevant review classes under CC-BAR-2/5.

[Unknown] Final documentation/battery/hosted/count integration, canonical clean-clone battery, terminal CI, actual main recording tag and tag-record equality, actual tagged authority admission and private size-only measurements are outside this checkpoint and remain unestablished here. Overall merge verdict: WITHHELD.
