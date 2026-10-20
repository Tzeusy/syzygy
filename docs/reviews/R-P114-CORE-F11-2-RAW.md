# Review — P-114 core correction at f11d6727
Reviewed commit: f11d6727fbc902a88fde600c988fb525c5385dce
Base commit: 9adae4f2935f2e82bb295eb6d6683a8d1c3a2bda
Verdict: REVISE

[Observed] This independent confirmation review covers the four-file correction in the isolated reviewer clone. The preceding raw remains verbatim at `docs/reviews/R-P114-CORE-9ADA-1-RAW.md`; its bytes match the reviewer cache raw. The prior verdict is not overwritten. Actual act, registry and aggregate bytes are unchanged from 9ada. The approved package, directions, doctrine/RFC/craft references and bounded acceptance criteria remain the governing scope. Final documentation, battery/workflow/count integration, CI, real main tag, actual tagged admission and measurement remain outside this core checkpoint.

[Inferred] The early input-snapshot correction and shared exact-record predicate correctly address their immediate reproductions. Historical Finding 2 is resolved for the tested population. Transaction Finding 1 remains open at rollback: the corrected pre-write guards preserve intervening inputs, but rollback still discards an independent edit to a file that the transaction has already replaced.

## Findings

**Finding 1 — Rollback overwrites or deletes a foreign edit to an already replaced output** (revise)

Severity: Important. Source: `scripts/record_pwb_registry_machine_ceiling_act.py:338–345`; the forward guards are lines 321–337.

[Observed] After a successful replacement is appended to `changed`, the exception handler restores `before[rel]` without comparing the current file with the transaction's own installed `outputs[rel]`. For an initially absent record it unlinks the current file unconditionally. The new compare-with-input guards protect files before their replacement; they do not establish ownership of those files later during rollback.

[Observed] Two executing disposable fixtures reproduce data loss through real `os.replace` operations and an injected later `OSError`:

1. The first replacement installs the proposed registry. An independent writer appends `Independent edit after owned replacement.` to that file. The second replacement raises `OSError('independent probe: later replacement fails')`. Rollback restores the old act-B registry bytes and loses the independent edit. The foreign edited registry hashes to `655c27d82e31f11c7b2316108db9f0d70534e925783e18e27a53b4668e644b7a`; the final file is act B's digest instead.
2. The first two replacements install the registry and new dedicated record. An independent writer appends the same marker to the record. The third replacement raises the same `OSError`. Because that record was absent before the transaction, rollback unlinks the independently edited file. Its foreign bytes hashed to `d80183ba603f4de1f529029bc5aa155c922f45ef8ac1834fbb3c29cb4ef6bdcb`; the final file is absent.

Both probes reach the intended injected I/O failure; neither is accepted via a changed function-signature `TypeError`. Exact input mutations, foreign/final hashes, final population and exception messages are in `repair-extended-probes.json`, IDs `rollback-after-independent-edit-to-POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json` and `rollback-after-independent-edit-to-PWB-OBSERVER-REGISTRY-MACHINE-CEILING-ACT.md`.

[Inferred] This is the remaining preservation defect in the same approved transaction seam, not a request for a new concurrency subsystem or owner gate. The preparation plan's atomic-failure predicate requires preserving independent bytes; canonical engineering-bar biases 3/6 require a diagnosable refusal rather than silent destructive restoration, and test-rigor rule 3 requires the failure path. Ask 2 item 5 confines the recorder to its own transaction's effects.

Required bounded correction: before restoring or unlinking each replaced output, confirm its current bytes are still exactly those written by this transaction. Preserve a divergent foreign edit, restore the other outputs still owned by this transaction, and report the path/recovery conflict honestly instead of claiming a complete rollback. Retain the original I/O failure context. Add both real replacement/edit/later-failure regressions while keeping the existing clean-failure restoration controls. No existing performed-act bytes need change.

## Prior finding confirmation and executed controls

[Observed] The original 25-probe campaign was replayed at the reviewed commit using `repair_original_probes.py`; only the subject identity and receipt filename changed from the retained original script. The previously lost early aggregate edit now refuses at `transaction input changed: ...ACCEPTANCE-ACT-RECORD.md` and is preserved. The original five wrong-only and five contradictory history cases refuse. The twelve frozen-source entry mutations preserve transaction outputs. The staging-time drift control and historical accepting control remain effective. Receipt: `repair-original-probes.json`.

[Observed] The additional 29-probe campaign in `repair_extended_probes.py` executes six early/staging cases across the registry, record absence and aggregate; each refuses at its intended `transaction input changed` predicate, preserves the foreign bytes, leaves the other inputs unchanged and cleans staged temporary files. Its late pending-aggregate control also refuses and restores the two owned outputs while preserving that foreign aggregate. The two late-owned-output cases above expose the remaining defect.

[Observed] The same campaign applies four distinct mutations to each of the five checked historical fields: identical additional value, contradictory additional value, malformed additional value and malformed sole value. All twenty reach `dedicated record differs from exact regeneration`. The complete canonical record remains an accepting control. The shared `exact_record()` compares the complete record rendered for the fixed manifest row, retained review/template and preserved valid UTC recording instant; malformed competing interpretations no longer pass the historical link. Finding 2 of the 9ada raw is therefore closed for this bounded predicate population.

[Observed] Independent checkpoint runs completed: dedicated recorder selftest, 68 fixture outcomes with 0 failing (`repair-recorder-selftest.log`); re-pin builder selftest, 66 outcomes with 0 failing (`repair-history-selftest.log`); current-tree public policy/admission/dossier selection, 149 tests passed across three files (`repair-closed-readers.log`). The fixture counts are outcome populations, not claims of 68 or 66 independent source-code mutants. Those successful runs do not cover or override the two rollback failures.

[Observed] The 184 protected baseline paths still match by SHA-256, byte length and Git blob; an independent restricted Git diff over that same population lists no changed member. The actual aggregate, registry and new dedicated act are byte-identical to their 9ada blobs. The retained 9ada raw matches SHA-256 `5f0e54cdc05871a5e8a1c9c0747142aec94e6c615cc919e4fb4a0031ae3ca35f`.

## Assessment and limits

[Inferred] Core verdict remains REVISE for the rollback-ownership defect. The earlier pre-write drift and strict history-field corrections are confirmed within the executed cases. This is a source/test correction under the same owner approval; no owner question, act rewrite, parser/allowlist change or additional read authority follows.

[Observed] Probe writes occurred only in disposable fixtures. No worker/source checkout bytes, act/tag, Beads, external application, provider, daemon or Butlers body were mutated or accessed by this review. The reviewer clone remains at the exact subject; the failed checkpoint and its probe artifacts are retained additively.

[Unknown] Final docs/count/battery/hosted verification, CI, real recording-tag equality and tagged admission, private size-only measurements and overall completion remain unestablished. In particular, a CG-26 OK must not stand in for the English count-sentence comparison; the named baseline parser limit and independent count checker remain final-head verification work. Overall merge verdict: WITHHELD.
