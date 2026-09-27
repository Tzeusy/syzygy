RAW FRESH-CONTEXT REVIEW — PR #128
Reviewed commit: 4d9bc74215a8a22562f3ff3fcba4655483c2e0e2
Base commit: 3c915991fbb0eebc38f8daaaea4d05679914b6b8
Manifest-file SHA-256: 2d071b73b0e3cb50dafa2fa80ac103d0079b855fcbbd9728c04eb99a166fbf7e
Verdict: REVISE

Reviewer identity: /root/dov62 (Codex), GitHub @Tzeusy
Risk tier: high
Current origin/main inspected: 1b2adb8c033214f7e3ab7354f3915a27733279a0. The 11 manifest source blobs are unchanged from the PR base to current main.

Fresh-context inputs: the exact candidate package and patches at the reviewed commit; the signed PWB package; P-81 Q5 and M14 Q5; VIS-1/2/3/4/7, CC-REV-2/8, PWB-REQ-007/011/013/014/015/016/020, RFC2-24; current D5/D6 records; and the stated acceptance criteria. No prior raw review was used as evidence; the resolved thread text defined the three dispositions below.

Disposition of the three previous blockers:

1. Repaired. The proposed requirement assigns the item-to-intent relation a separate stable identity and complete tuple, names RFC2-24's `missing-declaration` and `contradicted-pending-adjudication` reasons/routes, and preserves PWB-REQ-007/020 parity. The item tuple is explicitly preserved. See `proposed/spec.md.patch:31-43` and the impact/coverage/design records. Prior thread: https://github.com/Tzeusy/syzygy/pull/128#discussion_r4114090317.
2. Repaired. Proposal material is limited to a matching declared capability detail; non-capability details carry none. PWB-REQ-013 is reached in the impact ledger, design, packet, semantic delta, review brief and coverage patch. Prior thread: https://github.com/Tzeusy/syzygy/pull/128#discussion_r4114088059.
3. Repaired for late-patch preflight. `check()` materializes and validates the complete proposed map before `apply_at_adoption()` writes any of its five changed subjects. The 18-predicate selftest includes a corrupted final patch and confirms all scratch target bytes remain unchanged. Prior thread: https://github.com/Tzeusy/syzygy/pull/128#discussion_r4114084978.

Other review checks: the manifest has 11 rows and builder `--check` passes; 5 tracked sibling spec patches compose. Current open PR #121 at `2b29d6197e9e414033814875ae3a0d4024c92bf7` and PR #124 at `5e7a55d1b2a759433976f374a15cade34a0fffae` each compose with the candidate patch in both orders. The separate exact-source scenario says the PWB-REQ-015 delta is downstream and not drafted there. The candidate preserves the three bands and classes, relation and item tuple separation, exact-source authority, capability-only proposal scope, and shared-model reality. Current D5/D6 are adopted; I assessed the current doctrine clauses directly, and D6 governs the answer-first and diagram form. No signed PWB source subject, performed act, product runtime file in `apps/**` or `packages/**`, or successor-chain link changed; the PR does add candidate tooling in `scripts/**`. The phrase is explicitly not offered. CG-26's PROJECT-STATUS / hosted-workflow / battery-count triple is untouched; `docs/README.md` records the fresh raw in the review-campaign partition. Hosted `checks` and `node` both passed on reviewed head 4d9bc742. The PR remains Draft.

Finding 1 — BLOCKING — the standalone writer can write act-bound bytes with no verified owner act.

`scripts/build_pwb_item_depth_amendment.py:449-453` accepts `--apply --at-adoption` as sufficient authorization and calls `apply_at_adoption()` with its default live repository root. That function validates the candidate patch, manifest, generated dependencies and sibling composition, but never reads a performed act, exact act argument, successor-chain position or recorder transaction. A tracked-file sweep found no item-depth recorder/callsite, and the dedicated act record and acceptance-record row do not exist. I invoked the actual CLI dispatch in a scratch mirror only; it returned 0 and wrote all five proposed signed subjects without act input. The live signed subjects remained unchanged.

P-81 Q5 authorizes drafting only, and the owner has not selected the successor position. Keep this draft incapable of applying signed bytes until a dedicated recorder verifies the exact performed act, chain position and manifest transaction before any target write; add a test that refuses absent or mismatched act evidence with every target byte unchanged. Thread: https://github.com/Tzeusy/syzygy/pull/128#discussion_r4116213793.

No Beads lifecycle state was changed. No owner phrase was offered, no adoption was performed, and no merge or ready action was taken.
