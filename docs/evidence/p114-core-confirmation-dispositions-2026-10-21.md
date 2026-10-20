# P-114 bounded core confirmation — separate disposition

[Observed] The fresh independent review of
`fbe90feb253e2d020b4974e3abf6755321f9063e` returned `CONFIRM` for the
bounded core implementation. It is retained verbatim as
`docs/reviews/R-P114-CORE-FBE-3-RAW.md`, SHA-256
`04889043fe6fe94f16aae228712b680f62050ceceefeb7f1ddb3eb3e57ebac35`. The overall merge verdict in that same
raw remains `WITHHELD` for final documentation, full exact-head verification
and the lead-owned tag/admission/measurement gates. This disposition does
not widen that verdict.

[Observed] Findings 1 and 2 are closed within the raw's executed predicate
populations: pre-validation snapshots and pre-write comparisons preserve
intervening inputs; rollback preserves independent bytes/deletions, restores
still-owned outputs and reports incomplete recovery with the original I/O
cause; exact complete-record regeneration rejects competing historical
field interpretations. Neither performed-act bytes nor the reviewed proposal
changed. Both preceding `REVISE` subjects and the f11 additive execution
disclosure remain preserved verbatim with separate dispositions.

[Observed] The independent campaigns contain 25 original replay controls,
29 extended cases and six additional recovery cases. These overlapping
campaign populations are kept separate; they are not a unique source-code
mutation count. The reviewer independently reports 80 dedicated-recorder
and 66 whole-history-builder outcome fixtures. Its retained artifact index
has SHA-256 `9c8b01e99110d357e93c3c9e7a57cdcbcdc89c98129a3be0944755173ffdf98b`. The index's
11 files were independently rechecked by Python SHA-256/byte length
and `sha256sum --check`; metadata and exact artifact hashes are retained in
`docs/evidence/p114-machine-ceiling-mutations-2026-10-21.json`.
Original resolved probes/scripts remain immutable in
`/home/tze/.cache/syzygy-p114-install-final-review-2026-10-20/`.

[Unknown] This core verdict does not establish final docs/partition/count,
canonical clean-clone battery, CI, actual main tag/equality, actual tagged
admission or private size-only measurement. Those require their own exact
final-head evidence. No further owner question is indicated by this bounded
review; the actual paired approval remains the governing scope.
