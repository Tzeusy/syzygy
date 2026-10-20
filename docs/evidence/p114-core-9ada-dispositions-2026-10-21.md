# P-114 core review at 9ada — separate correction disposition

[Observed] `docs/reviews/R-P114-CORE-9ADA-1-RAW.md` retains the fresh core
review of `9adae4f2935f2e82bb295eb6d6683a8d1c3a2bda` verbatim. Its verdict
is `REVISE`; that verdict and its failures are not retired or rewritten by
this disposition. Raw SHA-256: `5f0e54cdc05871a5e8a1c9c0747142aec94e6c615cc919e4fb4a0031ae3ca35f`.

[Observed] The independent probe JSON and script remain immutable in the
review cache at `/home/tze/.cache/syzygy-p114-install-final-review-2026-10-20/`:
`core-independent-probes.json` SHA-256
`4cc4a1ab521650f9782136850c6dea654261f5185fd468f372ddc4634d1fa0ee`;
`core_independent_probes.py` SHA-256
`03d8d2302595c4cb3ec1dd15ee171aadacba222f2192e2ffea869295ba83b955`. Their old/new fragments and failed
subject remain evidence of the first source checkpoint. Corrected-source
mutation evidence is additive, not a replacement for those probes.

| Finding | Bounded correction | Executed verification |
|---|---|---|
| 1 — late transaction snapshot can overwrite an intervening input | Capture the registry bytes, dedicated-record absence and aggregate bytes before validation or output construction. Pass that snapshot into the transaction; compare it before staging, after staging and immediately before each replacement. | All three input kinds drift before the transaction and during staging: six refusals preserve the foreign bytes and other two inputs. A late aggregate edit after the first replacement refuses, restores the owned outputs and preserves the foreign aggregate. The six existing stage/replace failure and restoration pairs remain. |
| 2 — named history accepts contradictory fields | The historical link now uses the owning recorder's exact complete-record regeneration predicate. It preserves the actual recording instant and compares the complete record with the named fixed row, retained review and approval template. | Five field kinds each receive a contradictory duplicate, identical duplicate and malformed extra value: fifteen separate refusal cases. The prior wrong-only, digest/manifest/patch/subject controls and exact accepting recovery remain. |

[Observed] Corrected source identities are
`scripts/record_pwb_registry_machine_ceiling_act.py`, SHA-256
`e455a498bc3a50071e6674f88441b951b31faef37a4e9cba51aa6a56c0e8701d`, and
`scripts/build_pwb_behavior_contract_repin.py`, SHA-256
`2c0168653772fa0b48ba41306ed6fc4bf31b90e1dd51034d89143ae26d8aa57b`.
The recorder's `--selftest` reports 68 fixture outcomes with zero failures;
the historical builder's `--selftest` reports 66 with zero failures. Counts
were checked both against the summary and the individual `PASS` lines.

[Observed] All four affected historical helpers pass their applicable checks.
Their unchanged selftest populations are 24 currency-builder predicates,
16 currency-recorder fixtures and 38 re-pin-recorder fixtures; the shared
re-pin builder's current population is the 66 above. The dedicated `--check`
and frozen proposal builder `--check` pass. The adapter runs the unchanged
builder's actual 22 pre-install fixture predicates at the named pre-install
commit; this historical seed does not substitute for current applied checks.
Logs are retained outside the repository under
`/home/tze/.cache/syzygy-59s5-implementation-2026-10-20/repair-*.log`.

[Observed] The declared 184 protected files match their baseline by SHA-256,
byte length and Git blob identity. An independent restricted Git diff names
no changed member of that population. The actual dedicated act, installed
registry and aggregate match their bytes at the failed source checkpoint;
these corrections change the recorder and history validation, not the
performed transaction, reviewed proposal, directions or predecessor acts.

[Unknown] These local corrections establish no fresh independent verdict,
final documentation/count/CI result, main tag or runtime admission. Those
remain separate final gates. The existing CG-26 count-sentence parser does
not cover the three-word number at the current count; `syzygy-8tsz` tracks
that separate enforcement gap. Final battery parity, physical command
counts and the sentence's explicit parsed number require independent
comparison and a rejecting count mutation; this disposition does not claim
that CG-26 validates that sentence.
