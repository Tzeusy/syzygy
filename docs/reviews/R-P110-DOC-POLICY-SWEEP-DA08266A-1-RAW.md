# P-110 final documentation regression — policy act sweep

Reviewed commit: `da08266afda81c1493ab61cc2c870cde3b61f336`
Base commit: `dd520e8dd2e857814d9cf5ab1ac55eb79b83da33`
Verdict: REVISE

[Observed] **Important — route the register's policy transaction through the owning aggregate record.** `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:1343` now names the v4 act filename in both a Markdown link label and its URL. Both occurrences contain the closed reader's `public-source-scope` stem. `packages/polaris-generation-consent/src/package-reader.ts:381–383` deliberately treats any non-aggregate decisions file with that stem as an unknown possible policy record, and `readPolicyActs` refuses the whole read at line 419. This is fail-closed behavior of the existing reader; the new routing citation triggers it.

The complete clean-clone Node suite at this subject reports four failures in three files: the real-tree policy read, two local dossier current-policy screen checks and the default app policy-port check. The result is `invalid-records`, and the public-source port refuses with no screening-scope policy in force. This blocks the legitimate installed v4 public-source/dossier policy chain. The exact full-unit log path and digest are in `subject-evidence.json`; the log reports 4 failed, 4,742 passed, 5 skipped out of 4,751 tests. No final overall merge attestation had been issued; the earlier bounded documentation assessment missed this runtime stem reliance and is superseded by this finding.

I independently reproduced the cause using the actual policy reader and chain evaluator over the frozen cache clone, with only an in-memory filesystem override. No repository file was edited. The reader source is byte-identical to the independently typechecked 1cdb source; the compiled reader used for the probe is identified by digest. Seven cases all produced their literal expected outcomes:

1. Frozen register: policy reader throws `AdmissionRecordError: invalid-records`, chain refused, final policy file read is the pending register.
2. Route only the label to the aggregate: still refused.
3. Route only the link target to the aggregate: still refused.
4. Route both occurrences to `ACCEPTANCE-ACT-RECORD.md`: reader returns the exact v4 act and chain is `ok`.
5. Blank only the pending register in memory: chain is `ok`, independently isolating that file.
6. Route both occurrences, then add a synthetic unknown withdrawal form: reader and chain still refuse.
7. Restore the frozen original register: refusal returns.

[Inferred] The narrow correction is a link to the owning `ACCEPTANCE-ACT-RECORD.md` plus the existing installation direction. Preserve the dated selection/authorization and the in-row historical qualification. Remove both raw act-filename occurrences from the register's new sentence; changing only link text or only target is insufficient. Do not expand the citation allowlist, exempt the register, weaken the policy sweep, alter an act, or edit the frozen package.

This preserves the acceptance criteria and REQ-polaris-generation-025: existing admission and policy gates remain intact, and missing or invalid policy authority still blocks ingestion. The aggregate already owns act history and is intentionally the reader's aggregate home; the plain owner direction owns installation scope. The positive/withdrawal negative pair confirms the proposed routing can restore the valid chain without admitting an unknown withdrawal.

Retained evidence: `reproduce-reader-isolation.mjs`, `reader-isolation-results.json`, and `subject-evidence.json`. Run the reproduction against a disposable clone at this subject after its local workspace build; it changes only its own result file. All cases use synthetic metadata and local repository governance files, with no observed Butlers body, provider, daemon, external comment or Beads action.

Final merge attestation remains withheld. A corrected exact head must pass the current-tree checks, complete clone battery and exact-head hosted CI.
