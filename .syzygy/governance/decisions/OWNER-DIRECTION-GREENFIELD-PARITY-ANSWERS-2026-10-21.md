# Owner direction — answers to the greenfield-parity packet

Date: 2026-10-21

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-GREENFIELD-PARITY-ANSWERS-2026-10-21`

This is a plain owner direction in the sense of `PROCESS-GLOSSARY.md`, in the
same family as `OWNER-DIRECTION-GREENFIELD-PARITY-SIMPLIFICATION-2026-10-20.md`,
which it confirms and narrows.
- It binds no artifact digest.
- It adds no row to `ACCEPTANCE-ACT-RECORD.md`.
- It registers nothing in `scripts/check_governance.py`.
- It signs nothing, adopts nothing and edits no signed byte.

## How the answers were given

[Observed: the owner's selections in a Claude Code session on 2026-10-21 at
04:10:58 UTC, made with the session's question tool. The session is not in this
repository.]

The questions came from an owner packet (bead `syzygy-bpyt.1.1`). That packet was
reviewed adversarially in four rounds, by independent subagents in fresh context.
Their raw output is retained verbatim:

| Raw | Covers |
|---|---|
| `docs/reviews/R-GREENFIELD-PARITY-PACKET-1-RAW.md` | Round 1, all nine draft questions |
| `docs/reviews/R-GREENFIELD-PARITY-PACKET-2-RAW.md` | Round 2, the reworked packet |
| `docs/reviews/R-GREENFIELD-PARITY-PACKET-3-RAW.md` | Round 3, narrow verification |
| `docs/reviews/R-GREENFIELD-PARITY-PACKET-4-RAW.md` | Round 4, GP-Q0's prescribed fix only |

The verdicts the owner answered over, in the raws' own words:
- **GP-Q0:** "Scope verdict: Pass" and "Recommendation verdict: Pass" (`R-GREENFIELD-PARITY-PACKET-4-RAW.md:7,9`). Round 3 had given the recommendation "Revise", and the fix that round 4 confirms was applied in between.
- **GP-Q1:** "Scope verdict: Pass" and "Recommendation verdict: Pass" (`R-GREENFIELD-PARITY-PACKET-3-RAW.md:53,64`).
- **GP-Q7:** the same two verdicts (`R-GREENFIELD-PARITY-PACKET-3-RAW.md:79,88`).
- **The six rows of the status-quo table:** each "Pass" (`R-GREENFIELD-PARITY-PACKET-3-RAW.md:105-125`).

The working packet was a local, gitignored file in the operator's checkout and
is not authority; this record is self-contained. Each selection below is the option label exactly as it was
presented to the owner.

## GP-Q0 — how the greenfield-parity beads proceed

Selected: **"Confirm all three (Recommended)"**. That option had three parts.

### Part 1 — the reading of 2026-10-20 is confirmed

Items 2–3 of the 2026-10-20 direction stand as recorded.
- Behavior-preserving refactors may proceed under the acts already in force. They may touch `apps/**`, `packages/**`, `scripts/**`, tests, CI and root manifests.
- "Behavior-preserving" means none of the following changes:
  - a rendered byte, a wire format, a refusal string or an exit code;
  - a signed or digest-bound artifact;
  - a consent, security or retention decision.
- POC beads are admitted as improvement-cycle work. Bead `syzygy-bpyt.10` is the cycle report, and POC shared-model work stays at WIP one.
- Dossier beads proceed under the dossier acts already in force.

**Review rule.** It applies to every pull request in this work.
- Each pull request states which CC-REV-1 classes it touches. Any pull request whose classes are not "none" gets the CC-REV-1 independent review, from a fresh-context reviewer on the default model.
- Some pull requests also get three further checks:
  - **Which ones:** pull requests touching class 1 (authority boundaries), class 3 (deterministic observation) or class 4 (security), and class-6 pull requests that remove an endpoint.
  - **The checks:**
    - an old-versus-new differential over a mutated-record corpus that includes records with altered prose;
    - a rule-6 mutant for each predicate;
    - a non-blocking owner notice in the cycle report.
- Beads known to touch a class: `2.2`, `3.2`, `5.4`, `6.1`, `6.2`, `6.3`, `6.5`, `7.2`, `7.3`, `7.4` and `8.4`.

### Part 2 — the status-quo table is confirmed

Item 4 of the 2026-10-20 direction listed seven topics for the owner. Six of
them stay as they are. The seventh, the dossier's execution arm, is GP-Q7 below.

| Topic | Confirmed disposition |
|---|---|
| Spent governed estate | **No moves.** One generated exclusion predicate is allowed, driven by `ROUND-ESTATE.md`, for agent routing only. It is never applied to citer, reliance or digest sweeps, and governance outputs stay byte-identical. A dated mark goes on `ROUND-ESTATE.md`'s pointer to a packet that never held this question |
| Installed/candidate RFC mirror | **Both copies kept.** P-33 shape (M), CG-1i and CG-7h depend on them |
| `05-CONTRACT-INDEX.yaml`, `CONTEXT-BUDGET-REPORT.md` | **Both stay committed.** Generators and installed READMEs read them |
| The ten scripts under `.syzygy/**` | **Kept in place.** This is disclosed as a standing remainder of the `AGENTS.md` prohibition. The reason is that `contracts/candidates/scripts/` is a self-rooted bundle, and a bound ledger cites three of the scripts by path |
| How the consent gate recognizes an act | **Kept as is.** The two-copy template stays, held by the independent oracle test. Bead `8.4` never moves a byte-exact act onto field parsing, and bead `2.2` keeps the act-record hashes. A finding bead covers field-parsed act records whose prose has been altered |
| The parked provider island | **Kept parked.** Bead `8.1` decouples it. Deletion is revisited at the next audit |

### Part 3 — these output-changing beads are approved as listed

| Bead | What changes |
|---|---|
| `6.1` | `git ls-tree -z`, so quoted paths are recorded, not dropped |
| `6.2` | One non-human-principal rule. Refusal reasons change for inputs that are already refused |
| `7.2` | Paths are normalized before the `startsWith` check, if `write-guard.ts` is kept. This narrows what `authorizeWrite` accepts |
| `9.4` | `PENDING-OWNER-DECISIONS.md` is split into a live register and its history |
| `5.4` | The eight path-prefixed tailnet routes are removed. The bead's premise check still applies, and the remaining routes stay byte-identical |
| `2.2` | The battery is rewritten around a frozen act ledger |
| New | `isLaunchedRun` is read fail-closed, at both `allow-execution` and brief issuance |

Any change not listed here to what a gate accepts or refuses stops and returns
to the owner.

## GP-Q1 — evidence leaving the working tree

Selected: **"Yes, with verified index (Recommended)"**.

An evidence body removed from the working tree still counts as a "retained,
resolvable artifact" in the sense of:
- `engineering-bar.md:57`;
- `CAPABILITY-1-IMPLEMENTATION-AUTHORIZATION-ACT.md:65`;
- SDR-10.

It counts only when all four of these hold:
1. an in-tree index row names the body's commit, path and sha256;
2. CI verifies each row against git objects;
3. a protected tag pins the commits;
4. tag protection on origin is confirmed before the first move.

What happens next, and what stays out of scope:
- **Who moves bodies:** bead `syzygy-bpyt.9.2`, after bead `9.1` has measured the estate and set the move rule from that measurement.
- **Never moves:** a frozen (R0) file or a relied-on (R1) file.
- **Never happens:** a history rewrite, or the deletion of a tag.
- **Out of scope:** governed-plane files.

## GP-Q7 — the CC-SEC-3 conforming amendment

Selected: **"Draft it now (Recommended)"**.

The answer authorizes drafting the CC-SEC-3 conforming amendment packet. The
amendment is the one that D9's packet, in its question 4, said would follow D9.

The sign-off packet must state three things:
1. Signing it enables the execution-permitting arm of `packages/polaris-dossier/src/execution-rule.ts`. The flag flips only after the implementation is verified to disclose what REQ-polaris-generation-033 requires, and after a CC-REV-1 class-4 review.
2. Once signed, SEC-3's credential clause binds. Under the accepted note N2, that is permanent once Syzygy holds a credential.
3. The per-run choice and the owner's attendance stay operator declarations, which Syzygy cannot verify.

Separate beads cover:
- the stale unlock comment on the flag;
- a credential list that fails closed when a configured adapter declares a credential the list lacks.

This answer is not any of the following:
- the CC-SEC-3 sign-off;
- a flip of the flag;
- a per-run `allow-execution` choice.

No daemon executes observed code.

## What this does not do

- It signs, adopts or accepts nothing (VIS-4).
- It amends no doctrine, contract, policy or specification, and edits no digest-bound file. The CC-SEC-3 amendment binds only when the owner signs it.
- It lifts no standing prohibition in `AGENTS.md`.
- It releases no deployment, release, provider call or egress.

## Withdrawal

A later direction may narrow or withdraw this one; withdrawal defeats grant.
Withdrawal reaches only beads not yet merged.
