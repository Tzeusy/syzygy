> **Candidate transaction packet — unperformed.** This page and its recorder
> prepare a later owner act. No phrase or act instant has been supplied.

# Three-Surface POC readability successor — transaction packet

## Exact subject and authority

This packet prepares one readability-only successor to the six subjects of
`three-surface-poc-experience`. It changes no current signed byte before a
separate owner act. The original 2026-08-30 POC sign-off act and the later
2026-09-01 trusted-bootstrap act remain byte-identical history. The latter
supplies the effective predecessor for `CONTRACT-COVERAGE.md`.

| Binding | Exact value |
|---|---|
| Candidate parent PR/head | Draft PR #136, `7b4d8749c55257fb05fea94f6d2a82cf473ffe41` |
| Reviewed candidate commit | `ab31201ad3844de197d89b67cda47df0e7928982` |
| Six-row manifest | `THREE-SURFACE-POC-READABILITY-SUCCESSOR-MANIFEST.txt` |
| Manifest file SHA-256 | `221f1ececa321bf0cc6cd5e01f401e9eada38466c3c00dde43095f8cb8a0cd4d` |
| Semantic/fresh-reader review | `docs/reviews/R-POC-READABILITY-SUCCESSOR-REVIEW-4-RAW.md`, SHA-256 `7434a6be2adeb827e1110efd35535f9972d8fde749370d27622e0d7800aa33ef`, verdict `CONFIRM` |
| Original POC act | `.syzygy/governance/decisions/THREE-SURFACE-POC-SPEC-SIGNOFF-ACT.md`, SHA-256 `289d4e358aaeb9d2ea2f4e80b507bf376c15b7f8141c2da9337cb7618b73f004` |
| Later coverage act | `.syzygy/governance/decisions/GENERAL-TRUSTED-BOOTSTRAP-AUTHORIZATION-ACT.md`, SHA-256 `3534db031087eb1de0f5eaae8fcfbc50e8f546e44b8440e0a5e4936e394ede8c` |

The manifest's six codepoint-sorted paths are rooted at
`openspec/changes/three-surface-poc-experience/`:

| Subject | Effective predecessor SHA-256 | Proposed SHA-256 |
|---|---|---|
| `.openspec.yaml` | `9187547d8cc17017ebd44132527d2d5e096d1ef9705de80cc4f1cf34531f6976` | same |
| `CONTRACT-COVERAGE.md` | `f29a01f6a5725f4ac7085fa04a62de757fd16153d507ae5e415ae0b501fdc0a4` | same |
| `GOVERNING-DEPENDENCIES.md` | `4bdcf6c6dbd07aad7d44fb1d6fbb9ae37ea56bed2ed66532231cdc37a71c1da4` | `f8b66a710f9e3242f79b26b9c02eb4f44c55cd8368b517cd856da80b2ecbe1c5` |
| `design.md` | `0847bf5f78155712c13535a3de4a25be300ee6a726b5199e84e318103c28695c` | `6d39ea6f6111abaea32c74ce96c975ae53e077485f0ed8f7c97545e64d7ba295` |
| `proposal.md` | `6459f56cba26e0bc38c71a4a93ea571aa11eabdc847c96c81f8afcf30b72eddb` | `0650a6a3bc50158dc793802b9dcd40057b3199b3f7e9f8341a5bdc79cbea941a` |
| `specs/three-surface-poc-experience/spec.md` | `f0eda5b9ec8766e2b4b961fb2940c4ece7aa97b1c397e10d570abb04f5dd960e` | `bb9112a55a1cf2afdd6911815e80fa645f517f8a4e8b1b262ecf7381be515410` |

The original POC act's older coverage digest is act-time history. Neither the
recorder nor rollback may reinstall it. `tasks.md` is outside this transaction.

## Owner gate and deterministic outputs

The later owner gate requires **two verbatim lines in the same owner response**:
the exact ASCII phrase grammar
`SIGN OFF THREE-SURFACE POC READABILITY SUCCESSOR: <64 lowercase hex manifest SHA-256>`
and `ACT INSTANT: YYYY-MM-DDTHH:MM:SSZ`. The phrase's argument must equal the
manifest file SHA-256 above. The instant must be a real UTC calendar instant;
there is no agent clock/default. Owner identity is exactly `Tzeusy`.

The act constants are fixed: type `adopt specification amendment
(readability-only successor)`, project `project:syzygy`, artifact
`specification:syzygy:three-surface-poc-experience`, and identity
`act:syzygy:three-surface-poc-readability-successor:` followed by the full
manifest digest. Both performed records say exactly `Provenance state:
owner-adopted (bootstrap, uncorrelated)` and `A1 audit-record identity:
explicitly absent`. No record claims independent verification.

`scripts/record_three_surface_poc_readability_successor.py` owns the four
deterministic performed templates: `dedicated_body`, `aggregate_block`,
`router_row`, and `status_statement`. `--render-performed` prints the exact
eight-output digest manifest for the two supplied lines, without writing.
The later operator must render twice, compare bytes/digests, and pass that
output-manifest digest back to `--record`. The recorder regenerates and
compares it under its exclusive lock before staging.

The fixed eight-target install order is:

1. `GOVERNING-DEPENDENCIES.md`
2. `design.md`
3. `proposal.md`
4. `specs/three-surface-poc-experience/spec.md`
5. The dedicated THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md record
6. `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`
7. `.syzygy/governance/decisions/README.md`
8. `PROJECT-STATUS.md`

The two identical manifest subjects are checked and never written. The
decisions `README.md` is the human act router; the generated contract
`TASK-ROUTER.md` is outside this transaction.

## Recoverable logical transaction

All modes use the same `fcntl.flock` file in the canonical common Git
directory. Reads take a shared lock; record/recovery take an exclusive lock.
The common journal records the initiating worktree's canonical root, Git-dir,
common-dir identity and device/inode, exact target paths, preimage/staged
digests, phase and next index. It is fsynced before installation and after
each replacement. A live journal makes every read check fail `recovery
required`, including reads from another linked worktree.

Before the fsynced `committed` phase, locked recovery checks every backup and
staged output, restores the exact inert predecessor and removes the absent
dedicated act. At and after that phase it checks all successor outputs,
installs the repository-wide completion receipt, and retains the performed
state. A missing or corrupt journal-bound root, backup, staged file, target
or receipt refuses and preserves evidence. After successful completion,
`git worktree remove` may retire the recording root and its Git-dir metadata.
The retained receipt then validates against the performed bytes in the
current worktree and still blocks replay across the common Git directory;
a present but identity-mismatched recording root remains a refusal. The two
tracked act records and six signed subjects are portable authority. A clean
clone can check a performed commit without a local receipt.

These are eight ordered filesystem writes with journaled logical
recoverability. A process killed between writes can leave a physically
partial tree until exclusive recovery completes; no checker reports that
partial state as valid. The rollback boundary is the fsynced `committed`
phase. After the owner act, reversal needs a new reviewed owner-signed
successor. Earlier inert preparation may be reverted normally.

## Before and after the owner gate

Phase A requires the candidate builder, recorder preflight/check/selftest,
strict OpenSpec, governance and its selftest, docs campaign partition,
task-router check, and the canonical clean-clone battery. An independent
transaction review must pin the exact recorder and template source bytes,
the manifest, review 4, and reviewed commit before any owner presentation.
Changing a pinned source requires a fresh exact-byte review.

After the owner supplies both lines, the performed transaction commit comes
first. A separate post-act raw in a later pre-merge commit pins the prior
transaction commit and its output blobs. The Draft parent PR cannot merge to
main before those steps. The act grants no new implementation, repository
body-read, provider, deployment or release authority. Merge, CI, review,
silence and earlier readability direction perform no act.
