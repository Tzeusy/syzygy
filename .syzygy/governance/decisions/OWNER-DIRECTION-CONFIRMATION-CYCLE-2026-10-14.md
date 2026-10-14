# Owner direction — one confirmation round per amendment packet (2026-10-14)

> **A plain owner direction.** It binds no digest, adds no row to
> `ACCEPTANCE-ACT-RECORD.md`, registers nothing in
> `scripts/check_governance.py`, and performs no act. It signs, adopts and
> rules nothing on any packet's content questions (VIS-4). It records why
> review rounds ran that the packets' own stopping rules said would not, and
> what each round returned.

## The direction

On 2026-10-14, in the lead Claude Code session and in answer to a structured
question, the owner directed, for the ten amendment packets P-84, P-85,
P-86, P-96, P-97, P-98, P-99, P-100, P-101 and P-102:

> "run one fresh confirmation review on each, and repair them where needed,
> before asking you their questions"

[Observed: the wording as the lead session relayed it to this integration;
the owner's answer itself is in that session, not in this repository.]

**The lead session's stopping rule, stated with the direction:** one repair
and one review per packet. A packet still `REVISE` after its review goes to
the owner with its findings, not into another loop.

How it was applied:

- **P-84, P-85 and P-86** had review findings open with no repair since
  their last round, so each was repaired once (draft PRs #413, #414 and
  #415, landed with this record) and then had its one review.
- **P-96…P-102** had each been repaired once after round 1 already, so each
  had its one review over those repaired bytes.
- A round with no revise-severity finding clears the exact bytes it read,
  under the owner's 2026-09-26 ruling
  (`POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1); its notes go in a
  sibling record beside the package, and the package is not edited.

Earlier in the same sitting the owner also directed applying six 2026-09-27
answers; that is recorded separately in
`OPEN-REGISTER-OWNER-RULINGS-2026-09-27-DECISION.md`.

## What each round returned

Every verdict word below is copied from the raw file at the line cited. Each
head digest is the one on the raw's own head line. Every raw is retained
verbatim under `docs/reviews/` (CC-REV-6).

| Packet | Package | Round | Raw | Reviewed commit | Head digest (raw line) | Verdict (raw line) | Revise / notes |
|---|---|---|---|---|---|---|---|
| P-84 | `three-surface-poc-identity-amendment` | 5 | `R-M9-POC-IDENTITY-AMENDMENT-5-RAW.md` | `e7fd5301daf1c52a8e8ddab08cb1e50ddf4169d8` | Manifest SHA-256 `998215c3aad0483f9862432cddfec6e1b263cd69dc5803e6b9c3a1e1f69b391c` (3) | `REVISE` (4) | 1 / 5 |
| P-85 | `pwb-release-label-amendment` | 3 | `R-PWB-RELEASE-LABEL-AMENDMENT-3-RAW.md` | `7baea99151f68ac883f27d1ed4c79e608dce08bd` | Manifest SHA-256 `610880fd9ce477bf094856dee7c4af90f5231d4186b4e413bdf242fc015c1dd1` (3) | `REVISE` (4) | 2 / 5 |
| P-86 | `pwb-class-granular-extraction-amendment` | 3 | `R-PWB-CLASS-GRANULAR-EXTRACTION-AMENDMENT-3-RAW.md` | `00e24fd2dd10e8ffa8ba9cbecf88f58443fe72df` | Manifest SHA-256 `4562e028fc56b8b87aead03080aa9c515ce0308806a693977b9fcb35d8750abb` (3) | `REVISE` (4) | 1 / 4 |
| P-96 | `pwb-anchor-resolution-amendment` | 2 | `R-N9-MACHINE-CHANNEL-AMENDMENTS-2-RAW.md` | `ae8c074066d8e6c511d8064b505e3f89e3f2b43d` | PWB manifest SHA-256 `e7f304c79959341a9735516e87ccb991c012e695c2a16a90ee18ad2f1928c8f9` (3) | `CONFIRM WITH EXCEPTIONS` (5) | 0 / 9 |
| P-97 | `three-surface-poc-block-provenance-amendment` | 2 | `R-N9-MACHINE-CHANNEL-AMENDMENTS-2-RAW.md` | `ae8c074066d8e6c511d8064b505e3f89e3f2b43d` | POC manifest SHA-256 `c16bbb9bebdf82df37a40cbf070910a254ec47b0ca459e538bfe872993b28a50` (4) | `CONFIRM WITH EXCEPTIONS` (6) | 0 / 8 |
| P-98 | `pwb-opening-index-amendment` | 2 | `R-PWB-OPENING-INDEX-AMENDMENT-2-RAW.md` | `ae8c074066d8e6c511d8064b505e3f89e3f2b43d` | Manifest SHA-256 `4cee1b0c8120448bdda6bba1047d7ad06f51b1a7a18fec12c0cb4cd07475e518` (3) | `REVISE` (4) | 2 / 7 |
| P-99 | `pwb-accessible-name-amendment` | 2 | `R-PWB-ACCESSIBLE-NAME-AMENDMENT-2-RAW.md` | `ae8c074066d8e6c511d8064b505e3f89e3f2b43d` | Manifest SHA-256 `0509c31999aa65cee90bc2814120693f907fd530329837c0d6d8638641788d51` (3) | `REVISE` (4) | 1 / 6 |
| P-100 | `three-surface-poc-governing-intent-amendment` | 2 | `R-N10-POC-GOVERNING-INTENT-2-RAW.md` | `8f1fbec7723a4e60b8c00f03f260a1979e3d7738` | Package digest `9dd50df37859406bb813a44b0b5cc553c8cf5c87d2d875c53ccd410b301b6640` (3) | `REVISE` (4) | 4 / 5 |
| P-101 | `doctrine-amendment-held-derived-computation-d7` | 2 | `R-DOCTRINE-AMENDMENT-D7-2-RAW.md` | `8f1fbec7723a4e60b8c00f03f260a1979e3d7738` | Package digest `63f16c10a03f34a91eac5499261dd42c0a7b8c834d954ca386d1fd8eb79f377d` (3) | `REVISE` (4) | 1 / 7 |
| P-102 | `doctrine-amendment-inferred-first-class-d8` | 2 | `R-DOCTRINE-AMENDMENT-D8-2-RAW.md` | `8f1fbec7723a4e60b8c00f03f260a1979e3d7738` | Package digest `bf095a565049e4900a0744b2cb82a39f7bec9b5d59791307bb79f6560e091c34` (3) | `REVISE` (4) | 3 / 9 |

Nine raws cover the ten packets: the N9 raw judges P-96 and P-97 in one
file. Its findings 12, 13 and 14 apply to both halves and are counted under
each (raw lines 390–393), so the N9 raw holds fourteen distinct findings.
Every revise and note count above was re-derived 2026-10-14 by script from
each raw's finding headings and their severity words, and agrees with each
raw's own closing count where it has one. No round raised a blocking
finding.

[Observed 2026-10-14] Each head digest was recomputed from the bytes at
the reviewed commit and matches: the manifest file's sha256 for the seven
manifest-bound packages, and the brief's directory method
(`sha256sum` over the sorted `git ls-files` of the package directory,
hashed again) for the three doctrine and governing-intent packages.

## Outcome

- **P-96 and P-97 clear.** Both N9 manifests are cleared at the digests
  above. The notes are dispositioned, open, in the sibling
  `../contracts/candidates/pwb-anchor-resolution-amendment/ROUND-2-DISPOSITIONS.md`,
  and neither package is edited. Their content questions are still the
  owner's to answer.
- **The other eight are `REVISE` and go to the owner with their findings
  open.** Under the stopping rule none is repaired again and no further
  round is dispatched. *(Marked 2026-10-14, later the same day: "none is
  repaired again and no further round is dispatched" is no longer true.
  The owner then directed one more cycle for all eight — repair every
  finding, notes included, then one fresh review under the same stopping
  rule — recorded in
  [`OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md`](OWNER-DIRECTION-CONFIRMATION-CYCLE-2-2026-10-14.md),
  which also records what each further round returned.)* Each has a
  dispositions record for this round beside its package, which classifies
  its findings and repairs nothing:
  - P-84: `ROUND-5-DISPOSITIONS.md`.
  - P-85 and P-86: `ROUND-3-DISPOSITIONS.md`.
  - P-98, P-99, P-100, P-101 and P-102: `ROUND-2-DISPOSITIONS.md`.
- Register rows P-84…P-86 and P-96…P-102 in `PENDING-OWNER-DECISIONS.md`
  say this, with one dated header note and a recount.

## Integration facts

These are [Observed 2026-10-14] on branch
`governance/confirmation-cycle-2026-10-14` over `origin/main` `ae8c0740`.

- **Manifest digests survived the rebase.** The three repair commits
  (`e7fd5301`, `7baea991`, `00e24fd2`, each on `8f1fbec7`) were replayed
  onto `ae8c0740`. Each manifest file still hashes to the digest its raw
  carries, and, before the status marks below were added, every file each
  commit touched equalled that commit's blob, except
  `PENDING-OWNER-DECISIONS.md`. In that file each branch changed only
  its own row, and the rows were merged by row identity.
- **Sibling composition holds with the repaired patches landed.** Every
  pending builder's `--check` passes on this branch:
  - PWB: anchor-resolution, opening-index, accessible-name, release-label
    and class-granular;
  - POC: identity and block-provenance, the latter with its declared
    P-84/P-100 exclusive-pair warning.

  This discharges, at this commit only, the sign-off-time step the N9,
  opening-index and accessible-name raws named (re-run once the repaired
  P-84, P-85 and P-86 patches land).
- **Status marks.** The stale "no round 2 was dispatched", "pending round
  3/5" and "no decision record holds it yet" sentences that the raws name
  were marked at the sentence, dated, with the old text kept, in the P-84,
  P-85, P-98, P-99, P-100, P-101 and P-102 packages. Raws, review briefs and
  act-bound files are not edited. Before editing, each target file's sha256
  was swept across all 2,659 tracked files; none was cited in full or by a
  12-character prefix.

  Two packages are exceptions, and their dispositions records carry the
  corrections instead:
  - The N9 packages are cleared, so editing them would retire the
    clearance.
  - P-86's brief set its round-3 rule before the round: "the package is not
    edited" on any verdict but a notes-only one.
- **Package digests that moved.** The P-100, P-101 and P-102 directory
  digests cover every tracked file in the package, so the new
  dispositions records and the status marks move them:
  - P-100: `9dd50df37859406bb813a44b0b5cc553c8cf5c87d2d875c53ccd410b301b6640`
    → `640e24f3769d0328668a6deec87ebc5d47c438215f6bf15bdbe8c85f530ac8bf`;
  - P-101: `63f16c10a03f34a91eac5499261dd42c0a7b8c834d954ca386d1fd8eb79f377d`
    → `2bfbe119c6f7e3a7430661aa426162ad984271e260f8e53495fed1eb48991c09`;
  - P-102: `bf095a565049e4900a0744b2cb82a39f7bec9b5d59791307bb79f6560e091c34`
    → `5d6697075d8f0b334ea6536c81bd49567a1e936472d52c9d3450173f88b2a25d`.

  None of the three was cleared, so no clearance is retired. The bytes the
  rounds read stay retrievable at the reviewed commit. The seven
  manifest-bound packages' manifests do not hash their prose or
  dispositions records and are unchanged.

## A residual for the sign-off recorder

[Observed 2026-10-14] `scripts/record_versioned_signoff.py`'s `parse_head`
refuses the N9 raw: "review head does not carry exactly one `Manifest
SHA-256:` line". The raw's head carries `PWB manifest SHA-256:` and `POC
manifest SHA-256:` lines, and its `PWB verdict:` / `POC verdict:` lines are
its fifth and sixth non-blank lines. Its findings section parses: fourteen
findings, all notes. Neither N9 package is registered in that recorder yet.
Signing either half on this raw therefore needs recorder support for a
two-package head. The raw is not edited.
