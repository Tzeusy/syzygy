# P-114 machine-ceiling installation evidence

[Observed] The owner's paired version and implementation direction is at
`decisions/OWNER-DIRECTION-MACHINE-CEILING-INSTALL-2026-10-20.md`; the
performed registry transaction routes through
`decisions/ACCEPTANCE-ACT-RECORD.md`. This report records engineering
verification, not another owner act. The immutable proposal and its three
round-2 notes remain preserved.

[Observed] The source checkpoint reviewed first was
`9adae4f2935f2e82bb295eb6d6683a8d1c3a2bda`. Its independent core review
returned `REVISE` and is retained verbatim at
`docs/reviews/R-P114-CORE-9ADA-1-RAW.md`. The separate disposition is
`docs/evidence/p114-core-9ada-dispositions-2026-10-21.md`. The first local
fixture passes did not cover the two independently reproduced failures;
the rejected snapshot and probe evidence remain historical evidence.

[Observed] The next checkpoint
`f11d6727fbc902a88fde600c988fb525c5385dce` captures the three transaction
inputs before validation/output construction and refuses drift before
staging, after staging and before each replacement. Named historical
recovery now uses the owning recorder's complete exact-record predicate.
Its second independent core review is also `REVISE`, preserved as
`docs/reviews/R-P114-CORE-F11-2-RAW.md` with the additive
`docs/reviews/R-P114-CORE-F11-2-DISCLOSURE-RAW.md`. Two real filesystem
probes showed rollback discarding independent edits to outputs already
replaced by this transaction. The 25 original replay controls and 29
extended cases overlap and are not summed.

[Observed] Corrected source checkpoint
`fbe90feb253e2d020b4974e3abf6755321f9063e` checks ownership before each
rollback restoration or unlink, and again after preparing restoration.
Independent changed bytes/deletions are preserved; still-owned outputs
roll back. Conflicts report incomplete rollback with the original I/O
exception cause. Its separate disposition is
`docs/evidence/p114-core-f11-dispositions-2026-10-21.md`. The actual
recorded act, installed registry and aggregate remain unchanged from the
first checkpoint; correction dispositions identify the source by SHA-256.


[Observed] The fresh bounded core verdict at that exact source is `CONFIRM`
in `docs/reviews/R-P114-CORE-FBE-3-RAW.md:4`, with separate scope disposition
in `p114-core-confirmation-dispositions-2026-10-21.md`. Its 25 original
replay controls, 29 extended cases and six additional recovery cases remain
distinct campaign populations. The overall merge verdict is still `WITHHELD`;
this core confirmation establishes no later documentation or runtime gate.

[Observed] `p114-machine-ceiling-mutations-2026-10-21.json` names the frozen
source and its two source digests. It records executing input mutations and
actual temporary filesystem failures, with literal old/new fragments or
explicit exact constant substitutions. The recorder has 80 fixture outcomes:
57 rejection stimuli, six clean filesystem-fault restoration assertions,
seven pending-input preservation assertions, five rollback foreign-state
preservation assertions, one recovery-I/O-failure partial-state assertion
and four accepting controls. These are outcome fixtures, not 80 independent
source-code mutants. The named
history link has 29 outcomes, one accepting recovery and 28 refusals; the
whole re-pin builder has 66 outcomes. These are distinct populations, not
counts to sum with another reviewer or an overlapping selection.

[Observed] The four authorized historical helpers pass their applicable
checks after the named amendment. Their preserved currency-builder,
currency-recorder and re-pin-recorder selftests report 24, 16 and 38
outcomes. The unchanged proposal builder passes its applied `--check`.
The new recorder's `--builder-selftest` calls the existing replay helper
with the actual frozen builder path and exact pre-install commit
`03178a5483c5434780fc6c3b379b9006c9ae740e`; all 22 historical predicates
execute. That pre-install fixture seed contains landed screening controls
and the old registry gate, and is separate from current applied checks.
Missing/shallow seed refusal and the no-nested-archive boundary remain in
the unchanged replay helper. The replay helper and frozen proposal
builder remain unchanged.

[Observed] The source checkpoint's public-reader selection passes 149 tests
in three files: app screening 36, consent real-tree 3 and dossier screening
110. It includes actual current-tree positive reads and injected refusal
controls. The earlier TypeScript selection at the first checkpoint passed
329 tests across six files, with governance-inputs separately 26 after
commit. Those old runs do not become a test run of the corrected commit.
The correction changes only Python and retained review/disposition evidence;
the dedicated review reports its own exact-head selection separately.

[Observed] The declared 184 protected files match their baseline by
SHA-256, byte length and Git blob; a restricted Git diff independently
names no changed member. The eight proposal files, prior reviewed raw and
dispositions, canonical directions, previous acts and installed screening
chain remain preserved. No new version tag has been made by this worker.
Actual tagged admission and private size-only measurement belong to the
root's post-landing handoff.

[Observed] Four commands are added to both the published canonical battery
and hosted workflow: unchanged proposal `--check`, new recorder
`--builder-selftest`, `--check` and `--selftest`. The independent comparator
reads the workflow as YAML, expands shell assignments and parses shell
arguments. For the paired documented files it derives 109 unique commands on
each side, 109 physical Python invocations on each side and both count
sentence values as 109. Changing either sentence value to 110 is refused.
`p114-machine-ceiling-battery-counts-2026-10-21.json` binds those file bytes
and retains the rejecting mutations. The lead still rechecks the counts at
the final committed subject.

[Observed] Existing CG-26 compares the two command lists, but its numeric
word reader is limited to 0..99 and its count-sentence regex does not match
the number-word form here. `syzygy-8tsz` owns that separate enforcement
gap. The independent count/sentence comparison and rejecting mutations
above cover this change's sentence; no claim is made that CG-26 itself
validated that word count.

[Unknown] Canonical clean-clone battery, final CI, actual main version tag/equality,
actual tagged authority admission and private measurement remain separate
unestablished gates in this engineering checkpoint. No runtime or provider process was
started, no observed repository body read and no external publication done
by this worker. Final results must name their exact committed subject.
