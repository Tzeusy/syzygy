# P-114 core review at f11 — separate rollback disposition

[Observed] The independent core review of
`f11d6727fbc902a88fde600c988fb525c5385dce` returned `REVISE`.
`docs/reviews/R-P114-CORE-F11-2-RAW.md` retains that output verbatim,
SHA-256 `27a91fa07d7fae4f2c55759e5ebcd3b161764011b09862126b62b509f8e3dadf`.
Its additive execution disclosure is retained verbatim as
`docs/reviews/R-P114-CORE-F11-2-DISCLOSURE-RAW.md`, SHA-256
`bf38b4f001b6c32fc1eb340c7dc7570ddf74af27003de8320587a14692fc7fd4`.
The disclosure corrects an overbroad access/mutation sentence; neither raw's
verdict or finding is changed. The earlier 9ada raw and disposition remain
unchanged.

[Observed] The two independent probe populations remain distinct in the
review cache `/home/tze/.cache/syzygy-p114-install-final-review-2026-10-20/`:
`repair-original-probes.json` has 25 controls, SHA-256
`809c4ca7eceea536f56642173621c0f5569bc03eee85297389b6c99de407cd6e`;
`repair-extended-probes.json` has 29 cases, SHA-256
`49af7e1c864d9f242cb928015b9d303b4db89aed3f7586a893de7c022c8d995f`. Their overlapping controls are not
added together as one population. Their two reproduced late-rollback data
losses remain failed-checkpoint evidence with their original exact
mutations and hashes.

[Observed] Finding 1 is corrected in `scripts/record_pwb_registry_machine_ceiling_act.py`, SHA-256
`79f6af07c2dcd113eaa718e7051b1d9d41fee2d583efdbb9ab797643dd44bc0e`. Rollback compares each replaced file with this transaction's
exact installed output before restoration or unlink. It checks again after
preparing a restoration file. Independent changed bytes and deletions are
preserved; other outputs still owned by this transaction are restored.
A conflict reports `rollback incomplete`, names its path and retains the
original failure text and exception cause. A recovery I/O failure is also
reported as incomplete rather than silently claiming full restoration.

[Observed] Five new real-filesystem regressions execute the intended later
`OSError`: independent edits and deletions of the replaced registry and
new dedicated record, plus a registry edit during restoration staging.
Each has a refusal assertion and a separate state/population, temporary-file
cleanup and original-I/O-cause assertion. The existing six clean
stage/replacement failure/restoration pairs and seven pre-write/late-pending
input-preservation cases remain. The recorder reports 80 outcome fixtures,
zero failures, verified against both its summary and individual `PASS`
lines in the outside-repository `rollback-recorder-selftest.log`.
An additional recovery-I/O-failure case verifies partial-state reporting,
restoration of the other still-owned output and both failure contexts.
These are outcome fixtures, not a claim of 80 source-code mutants.

[Observed] The fresh f11 review confirms the early-snapshot and exact
complete-record history corrections for its tested population. This
rollback correction does not modify that history predicate, the recorded
registry transaction, proposal, directions, predecessor acts, policy chain
or owner parser. The performed transaction still has its original UTC
recording instant.

[Unknown] Local correction is not an independent confirmation. A fresh
exact-head core verdict, final docs/partition/count integration, canonical
clean-clone battery, CI, actual main tag/equality, tagged admission and
private measurement remain separate gates. Final docs and full battery
remain held. The independent count comparison still owns this change's
109 sentence verification; `syzygy-8tsz` tracks the existing CG-26
count-sentence parser limit.
