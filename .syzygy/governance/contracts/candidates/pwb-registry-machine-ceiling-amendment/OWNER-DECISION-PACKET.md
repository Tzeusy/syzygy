# Owner decision packet — P-114, the Butlers machine-answer ceiling to 16 MiB

> **Candidate — binds nothing.** Drafted under
> `decisions/OWNER-DIRECTION-MACHINE-CEILING-2026-10-15.md`. This file
> offers a sign-off. It is not one, and it labels nothing accepted. Only the
> owner signs (VIS-4). No digest appears here. The builder's `--digests`
> prints the manifest row.

## In one paragraph

Since 2026-10-20 the Butlers machine answer (`/api/poc`) is refused. It is
8,497,943 bytes against an 8,388,608-byte ceiling, so the daemon serves a
503 and nothing else [Observed,
`docs/evidence/syzygy-59s5-live-size-2026-10-20.json`]. The growth is not
code. It comes from the live work-item read, about 114 KB a day [Inferred].
The P-100 implementation was reverted to bring the answer back under the
ceiling (PR #474), and that buys time, not a fix. This package changes one
number in the Butlers observer registry entry, the machine-answer ceiling,
from 8 MiB to 16 MiB, and nothing else. The daemon hard-codes that number
and its read gate checks the entry's exact bytes, so the sign-off needs one
narrow code change in the same commit. Ask 2 asks for it.

## Ask 1 — the sign-off

> **Sign registry entry v1.0 (ceiling 16 MiB)**: the Butlers observer
> registry entry with `maxMachineResponseBytes` 16,777,216 and every other
> byte unchanged, as `pwb-registry-machine-ceiling-amendment-v1.0`.

- **Recommended: sign.** 16 MiB restores about 72 days of headroom at the
  observed rate [Inferred]. P-115 (serve governedBy once) lengthens that, and
  P-100 re-landing or P-86 shortens it. Memory is on the order of 50 MB per
  request and transfer about 1–13 s over the tailnet [Inferred]. Both are
  tolerable for one owner on one tailnet (`SEMANTIC-DELTA.md`, "Why 16 MiB").
- **Decline.** `/api/poc` stays bounded only by the P-100 revert and the
  growth rate. P-86 keeps waiting. Paging the machine answer becomes the
  next question.
- **What signing does.** The sign-off lane applies the patch, then writes a
  superseding `adopt-registry-entry` record in the form the PWB-REQ-005 gate
  reads (you type nothing; the record names the manifest row) and the tag
  above. The 2026-10-02 act B stays as immutable history.

## Ask 2 — the implementation authorization that has to travel with it

> **Authorize the ceiling's code change**: exactly the following, nothing
> else, no new Butlers read or egress.

1. `PWB_RESOURCE_LIMITS.maxMachineResponseBytes` 8388608 → 16777216
   (`packages/three-surface-poc-core/src/project-shape-observation.ts:82`).
2. The gate's registry act pointers in
   `apps/three-surface-poc/src/governance-inputs.ts`: record path, act
   identity, recording tag, and supersession target (now act B). Scope
   anchors are unchanged.
3. The test literals that pin the old value or act B
   (`IMPACT-LEDGER.md`, parts A and B1).
4. The four builder and recorder successors that read this entry
   (`IMPACT-LEDGER.md`, part B2): each accepts a later performed act's row
   over the subject.

**Why it is separate.** [Observed] The daemon does not read the registry
entry's limits. A signature changes nothing served until item 1 changes.
And until item 2 changes, the gate refuses every Butlers read (dry run:
`admits: false`). No implementation direction in force covers this entry.

**How the two combine.** Sign plus authorize: one commit applies,
records, implements and re-runs the battery, then `/api/poc` is measured on
a private daemon. Sign without authorizing: the sign-off is **not
recorded**. Recording without item 2 would refuse every Butlers read, so it
waits for the authorization. Authorize without signing: nothing is built,
because item 1 never runs ahead of the signed entry (the builder fails
closed on that).

## Not asked here

- The human ceiling (`maxHumanResponseBytes`, 2 MiB). `/trajectory` is at
  79.7% and growing because its selection includes every open item. Signed
  POC-REQ-042 lets that selection be capped, so it is implementation
  (`syzygy-blbu`), not a question for you.
- Sibling order. P-112 (loaded-profile) and P-95 (tree-framing re-pin)
  patch the same entry. Both are unperformed, and this one goes first by
  your "ceiling first". Each is regenerated and reviewed again after it
  (`IMPACT-LEDGER.md`, part C).
- Version numbers. The entry keeps `1.2.0-candidate.1`, following the act B
  precedent (`SEMANTIC-DELTA.md`). The review is asked to test this.

## Review record

| Round | Raw | Verdict (copied from the raw) | Disposition |
|---|---|---|---|
| 1 | (pending; it will be retained under `docs/reviews/`) | (pending) | (pending) |
