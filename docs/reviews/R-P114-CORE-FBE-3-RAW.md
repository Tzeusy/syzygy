# Review — P-114 core confirmation at fbe90feb
Reviewed commit: fbe90feb253e2d020b4974e3abf6755321f9063e
Base commit: f11d6727fbc902a88fde600c988fb525c5385dce
Verdict: CONFIRM

Scope: bounded core implementation confirmation. Overall merge verdict: WITHHELD pending final documentation, full exact-head verification and the lead-owned post-merge tag/admission/measurement gates.

[Observed] This independent review reads the four-file correction in the isolated reviewer clone, after the preceding core reviews of 9ada and f11. The accepted review basis remains the frozen P-114 proposal/round-2 notes, actual canonical paired Codex approval, preparation plan and recorded engineering findings. The correction changes the dedicated recorder's rollback handling, retains both f11 raws unchanged and adds a separate disposition. It changes none of the actual registry, dedicated act or aggregate bytes. The former REVISE verdicts remain preserved as findings about their respective subjects.

[Inferred] Both recorded core findings are closed within the executed predicate populations. The approved transaction remains one registry leaf, the matching runtime constant and registry gate pointers, strictly named history recovery, and the dedicated recorder/governance registration. The actual owner reply, state-(1) provenance, explicit A1 absence, registry-only predecessor and immutable reviewed/predecessor material remain intact. This confirmation neither creates authority nor claims a read, service result or overall merge gate passed.

## Finding 1 confirmation — preserve independent state during forward failure and rollback

[Observed] `transaction()` now receives the pre-validation input snapshot and compares it before staging, after staging and before each forward replacement. During rollback it compares current bytes with the exact bytes the transaction installed. A divergent file or independent deletion is retained and named as a rollback conflict. Restoration of a prior file has a second ownership comparison after staging its backup. An individual restoration I/O failure is recorded without stopping restoration of other still-owned outputs. The raised incomplete-rollback error retains the original forward failure as its explicit cause. Ordinary clean failures still restore the original population and bytes.

[Observed] The two f11 data-loss reproductions now preserve the independent registry/record edits, restore the other inputs and refuse with `rollback incomplete`, naming the path. The original forward replacement `OSError` remains `__cause__`; these tests do not pass by an incidental `TypeError` or a wrong predicate. The retained extended campaign also confirms six early/staging input-drift cases across all three input kinds and the late pending-aggregate control, with foreign bytes preserved and staged temporary files removed.

[Observed] Six additional independent filesystem cases confirm the added recovery behavior:

| Case | Required observed state |
|---|---|
| Registry deleted after its replacement, then next replacement fails | Deletion retained; other inputs restored; incomplete rollback identifies registry and original failure |
| Newly created act deleted after its replacement, then aggregate replacement fails | Deletion retained; registry restored; incomplete rollback identifies record and original failure |
| Registry independently edited while a restoration backup is being staged | Second ownership comparison preserves the edit; the other output is restored |
| Registry restoration staging fails with `OSError` | Current proposed registry remains; the other output is restored; both forward and recovery failures are reported |
| Registry restoration replacement fails with `OSError` | Same explicit incomplete-restoration outcome and original cause, with backup cleanup |
| Owned new-record rollback unlink fails with `OSError` | Record remains; registry is restored; the failed record recovery is named with original cause |

These six cases require exact resulting byte/population comparisons, the original `OSError` as explicit cause, the relevant conflict/recovery reason and no remaining `.p114-*` temporary files. They are retained in `confirmation-recovery-probes.json` with the exact script `confirmation_recovery_probes.py`.

[Inferred] The implementation now respects the boundary between its own recoverable outputs and another writer's later state. It reports incomplete recovery honestly rather than overwriting that state or claiming a complete rollback. These are bounded filesystem-seam corrections under the existing recording approval; no process-global coordination mechanism or broader write authority was introduced. Finding 1 is closed for the tested pre-write, staging, late-edit/deletion and recovery-I/O populations.

## Finding 2 confirmation — one exact interpretation of the historical record

[Observed] Historical recovery continues to call the owning recorder's complete `exact_record()` predicate. The retained original five wrong-only and five contradictory-field cases now refuse. The expanded cases independently apply identical extra, contradictory extra, malformed extra and malformed sole values to each of Act identity, Act type, Artifact identity, Supersession / revocation and recording tag. Those twenty mutations reach `dedicated record differs from exact regeneration`; the complete canonical record still recovers the exact act-B registry. The missing/wrong manifest, patch, digest and subject controls remain in the history selftest. The recovery interpretation is shared by the four approved successors and remains registry-only, with the P-110 policy path preserved.

[Inferred] A malformed competing field can no longer satisfy the named history link merely because one correct line remains. Finding 2 is closed within that explicit field population. The strict historical predicate establishes the bounded link, not independent human attendance or actual runtime admission.

## Retained independent verification

[Observed] At the reviewed commit:

- `confirmation-original-probes.json` replays the original 25 observations/controls. The twelve frozen-input entry mutations preserve outputs; the earlier aggregate drift is now refused and retained; the historical positive and paired wrong-only/contradictory cases have the required outcomes.
- `confirmation-extended-probes.json` replays 29 cases, including the six early/staging input kinds, pending-aggregate control, two now-preserved late owned-output edits and twenty strict history-field mutations.
- `confirmation-recovery-probes.json` adds the six cases above. Together these are 60 probe observations, computed from the three retained campaign populations, not 60 independent source-code mutants.
- The dedicated recorder selftest reports 80 fixture outcomes and the re-pin builder selftest 66, with no failing outcome. Summary counts agree with an independent enumeration of the literal `PASS`/`FAIL` lines. Logs: `confirmation-recorder-selftest.log`, `confirmation-history-selftest.log`.
- The dedicated recorder `--check` independently regenerates the installed row, exact record, retained selection/review and one aggregate block. Log: `confirmation-recorder-check.log`.

[Observed] `confirmation-summary.json` names the exact subject and campaign populations, records the two independent fixture-count methods, and confirms a clean source clone. The declared 184 protected baseline paths still agree by SHA-256, byte length and Git blob identity; an independent restricted Git diff over that same population has no changed member. The actual transaction's three files remain byte-identical to their 9ada blobs. The retained 9ada raw, f11 raw and f11 execution-disclosure raw each match the corresponding immutable reviewer-cache bytes. Their failed-subject evidence is not replaced by these new successful receipts.

[Observed] Earlier core evidence remains commit-specific: the 9ada build and 336 focused TypeScript tests across six files, and the f11 current-tree public policy/admission/dossier 149 tests across three files, were independently observed in their respective reviews. Those outcomes are not relabeled as new full fbe or final-head test runs. The correction changes neither the TypeScript implementation/test blobs nor the decisions-tree transaction bytes those cases consumed. The final committed subject still needs its own full verification as the plan requires.

## Assessment and remaining gates

[Inferred] Bounded core verdict: CONFIRM. The two recorded correctness findings have executing regressions and independent reproductions with the corrected outcomes. The sign-off, evidence, security and truth floors remain relevant under CC-BAR-2/5; this code confirmation does not lower or substitute for those gates. No further owner question is indicated by the reviewed correction.

[Observed] The reviewer read only frozen code in its isolated clone and advanced its detached HEAD to the supplied commit. It edited no implementation or governed file bytes in that clone or the worker checkout. Probe writes were confined to disposable fixtures and retained outside-repository review artifacts. No main branch/tag, actual act, Beads or external application was mutated by this reviewer; no provider or daemon was started and no Butlers body was read.

[Unknown] The final documentation/battery/workflow/count triple, exact-head full clean-clone output, terminal CI, actual main recording tag and record-blob equality, actual tagged authority admission and private size-only measurement remain separate and unestablished by this review. The existing CG-26 English-count parser limitation remains a disclosed final-verification constraint: CG-26 OK alone cannot prove the count sentence. Independent command-set/count/sentence validation and its rejecting mutations must be checked at the final head. Overall merge verdict remains WITHHELD.
