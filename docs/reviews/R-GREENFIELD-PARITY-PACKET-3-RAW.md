# Round-3 verification: greenfield-parity questionnaire

**Verdict:** GP-Q1, GP-Q7 and all six table rows clear with notes only. GP-Q0 still has one material defect: it narrows CC-REV-1's mandatory review from seven classes to three. Under the packet's own stopping rule, GP-Q0 either goes to the owner with that defect stated, or takes a one-sentence fix.

**Subject:** `/home/tze/GitHub/syzygy/.syzygy/local/questionnaires/2026-10-21-greenfield-parity.md`, 279 lines, sha256 `16e2dfdcd513f6ba69cd2ae24e1bffb138b79bca85c3c4b6294716545a4696c2`. HEAD is `eba011dfbe254c09a88ccc374b3efe5ff5df1762`. The tracked tree is unmodified; only the two pre-existing untracked files are present. Everything I ran was read-only.

## Packet-level

- **P3 landed.** GP-Q0 now asks the owner to confirm the table, and an objection turns a row back into its own question.
- **P4 landed.** The "agent memory" citation and option B's "contradicts the autonomy direction" con are gone.
- **P1 landed.** The count is 44 plus `0kq`.
- **Note (P2, mis-applied count):** "Twelve … already show in `bd ready`" is wrong. [Observed] `bd ready` lists 15 non-epic bpyt beads besides `1.1` (16 with it): `2.1`, `4.1`, `4.2`, `4.5`, `4.6`, `5.4`, `5.5`, `6.1`, `6.2`, `7.2`, `8.1`, `8.3`, `8.4`, `9.1`, `9.4`.
- **Note (P2, still unenforced):** "No lane dispatches any of them" is a promise. Nothing in the tracker gates these beads, so a parallel lead session can still dispatch them.
- **Note (P5, not landed):** The packet is still in the ignored `.syzygy/local/`. Bead `1.1`'s required row in `PENDING-OWNER-DECISIONS.md` therefore cannot point at it. This must be resolved before `1.1` closes.
- **Note (P6, partly landed):** `1.5`'s disposition is now stated. `1.3` (Q2–Q4) and `1.4` (Q5, "with shims") still have none. Under bead `1.2`, each would close "declined by owner <date>".

---

## GP-Q0

**Scope verdict: Pass.** The three-part question (the reading, the table, and the listed output-changing beads) is the right one. These corrections landed:
- "signed or" is back in the definition.
- The named-finding reading is gone, and PD beads are routed to item 2.
- `6.2` is no longer listed as behavior-preserving.
- `4.1` is reclassified.
- Unlisted accept/refuse changes now return to the owner, which resolves the tightening contradiction.
- Option C is relabelled.
- The middle option (A with an owner notice) is now part of A.

**Recommendation verdict: Revise.** One material defect.

**Material corrections:**
1. **CC-REV-1 is narrowed to three classes.** [Observed]
   - The background says CC-REV-1 "requires an independent fresh-context review for classes 1, 3 and 4". The recommendation calls it "the policy already in force for exactly these classes".
   - But CC-REV-1 (`review-and-documentation.md:16`) reads: "Changes touching any of seven classes require review…"
   - Option A attaches the independent review, the differential and the owner notice only to "a class 1/3/4 PR". Once the owner confirms it, that answer becomes the lane instruction, and it reads as narrowing an owner-approved policy. Two counterexamples in the same packet:
     - `5.4` removes machine-credentialed endpoints (`${TAILNET_MOUNT_PREFIX}${POC_MACHINE_PATH}` and the prefixed presentation route, `routes.ts:286-319`). That is class 6, public interface. The packet describes it as "unreachable routes only"; they are unreachable only through the deployment's tailscale config, per `tailnet.ts`.
     - `6.1` changes which paths the observer records. That is class 3, snapshot composition, yet `6.1` is missing from the "known" class list.
   - **Fix:** Every PR states its classes. Any PR with a class other than "none" gets the CC-REV-1 independent review. Class 1/3/4 PRs, and class-6 PRs that remove an endpoint, additionally get the differential and the owner notice. Add `6.1` and `5.4` to the known list.

**Notes:**
- **2.2 is not listed.** It is on the class list but not the output list. It rewrites the PROJECT-STATUS battery, `governance-docs.yml` and the CG-26 sentence by design. List it now, or its lane will hit the "unlisted change" stop.
- **The rationale is off for two beads.** "The enumerated output changes are fixes or fail-closed tightening" does not describe `9.4` (restructuring a governed file) or `5.4` (route removal).
- **The class glosses aren't the clause's words.** "Digests and identity" is not CC-REV-1's wording for class 3, which reads "deterministic observation — snapshot composition, evaluation identity, the deterministic/inferred seam". Use the clause's names.
- **Option C's count is low.** It says "about eleven more questions"; it is 12–13.

**Evidence freshness:** `eba011df`. CC-REV-1 and beads `2.2`, `5.4`, `6.1` and `9.4` were read from the local Dolt export, and `bd ready` was run on 2026-10-21. Not inspected: bd remote, other sessions' claims and worktrees, GitHub.

---

## GP-Q1

**Scope verdict: Pass.** These corrections landed:
- The general clause (`engineering-bar.md:57`), the Capability 1 act's line 65, and SDR-10.
- SDR-9 and CC-TEST-2 are now limited to "tests passed".
- Predicates are stated (150/227 and 175/249).
- The burst is "about 4 hours" (measured 4h05m).
- Bead `9.2` is read correctly: 168 + 36 + 184 = 388.
- History, not the tag, is what makes a body resolvable.
- `.git` does not shrink.
- The family key is said to bind almost nothing, and the mechanics move to `9.1`.
- Tag protection is marked [Unknown].

**Recommendation verdict: Pass.** The reframed principle, "an index row names commit, path and sha256 and CI verifies it", is sound and matches rule 11.

**Material corrections:** None.

**Notes:**
- "removes most of the files sweeps read for nothing" is unmeasured. At `dd520e8d`, 204 of 388 files were movable, and nobody has measured how many of those are uncited.
- "up to about 36 docs citers" counts files that need a repair, not citers.
- CI verifying "against git objects" needs a full-history checkout. This belongs in `9.2`'s mechanics.

**Evidence freshness:** `eba011df` and `dd520e8d`, via git object reads. Not inspected: origin tag protection, CI checkout depth.

---

## GP-Q7

**Scope verdict: Pass.** The narrowed question, draft now or hold, is right, and these landed:
- the per-project-record clause;
- the 2026-10-07 N2 ruling;
- the owner's intent on record (REQ-033 scenario, D9 question 4);
- what actually blocks the flip (CC-SEC-3, the stale comment, RFC5-12 (c) non-blocking);
- the narrower launched-run exposure;
- the fail-closed fix moved into GP-Q0;
- the attendance limit.

**Recommendation verdict: Pass.** Drafting binds nothing, follows D9 question 4, and leaves the security decision at sign-off.

**Material corrections:** None.

**Notes:**
- **The credential clause is paraphrased, not quoted.** "Unreadable by the session" drops "neither the session nor any process it starts, directly or not" and "at the operating-system level" (`security.md:86-88`). That dropped part is exactly why N2's cost is permanent. Quote the clause verbatim before presenting.
- **"Today Syzygy holds none" is labelled [Observed].** N2's own text marks it "[Inferred, from the package's code search]".
- **The bypass claim is over-general.** "Sessions in this repository run with permissions bypassed" was observed for this review session only; for other sessions it is [Inferred].
- **Adoption is a recorded reading.** For "was adopted with D9", the record says the bare "Adopt D9" "is read as the packet's recommendations" (`DECISION-HISTORY.md:185-190`). Say "read as adopted".
- **The flip conditions depend on GP-Q0.** Option A's flip conditions do not include the `isLaunchedRun` fail-closed fix, which now lands only through GP-Q0. If the owner narrows GP-Q0, the CC-SEC-3 sign-off packet should list that fix as a flip condition.

**Evidence freshness:** `eba011df`. Text checked: `security.md:61-111`, REQ-033 (`spec.md:15`), the v1.1 sign-off and sitting direction, and the D9 notes. Not inspected: live runs, run-directory permissions.

---

## Status-quo table

**Row Q2 verdict: Pass.** Landed: the precedents are trimmed to P-56 (b); the `public-source-classification.ts` citation is dropped; the predicate is routing-only, outside citer and digest sweeps, with byte-identical outputs; the dated mark is at `ROUND-ESTATE.md:255-257`. Note: P-56 (b) was not about avoiding churn. It kept one spent root prompt in place because a decision record's citation pins it (`DECISION-HISTORY.md:270`); say that. Back to owner: no.

**Row Q3 verdict: Pass.** The "to both mirrors" attribution is fixed (RFC5 act line 66). Note: "The constraint is recorded in audit delta row 58" is false at `eba011df`. The audit file is unmodified, and row 58 still reads "residue | duplicated concept | OG-2". Write "will be recorded". Back to owner: no.

**Row Q4 verdict: Pass.** The wrong `check_governance.py` line citations are gone, replaced by the six installed RFC READMEs and `install_redis_sitting.py:118`. Back to owner: no.

**Row Q5 verdict: Pass.** "Keep in place" is the status quo, and the conflict with bead `1.1` guardrail 3 is gone. The "self-rooted, portable" claim checks out: `candidates/README.md:101` reads "Self-rooted, portable verification and generation (…)", and since `DEFAULT_ROOT` is the script's parent, a move would need code edits. `IMPACT-LEDGER.md:190-192` is right. Notes:
- "Repointing 50–96 citers each" is wrong. [Observed] Basename citers per script are 50, 52, **19**, 83, 57, **37**, 50 and 96 (`build_capability_1_views` 19, `build_task_router` 37); full-path citers are 3–13; each 08j sweep has 3.
- "Act-preserved ground" for the 08j sweeps is unsupported. No decision or act text names them; their only citers are their two reports and the approval-offer snapshot. Use `ROUND-ESTATE.md:94`: "settlements of record" for Administration 1.
- "Recorded … in audit delta row 50" is false at `eba011df`; row 50 still reads "residue | tooling sprawl | OG-3".
- Bead `1.4`'s disposition is unstated.

Back to owner: no.

**Row Q6 verdict: Pass.** These landed: the constraint that `2.2` keep the act-record hashes, the CI `--check` caveat, and `1.5`'s disposition. Notes:
- "today only the CI recorder `--check` lines catch that" is an absence claim with no stated sweep (rule 9). Say "are what currently catch".
- "Closes as justified excess" differs from bead `1.2`'s prescribed close reason, "declined by owner <date>".

Back to owner: no.

**Row Q8 verdict: Pass.** These landed: the misquotes are removed; the signed v1.2 text, the 2026-09-12 acts and both "nothing is deleted" directions are cited; the egress half is included; the size is 3,803 lines. Bead `8.1` checks out as behavior-preserving: its acceptance criteria are "Brief, render and provider goldens byte-identical", and deletion is a non-goal. Notes:
- "Keeps every predecessor requirement's bytes and meaning" drops the spec's qualifier, "for a run in the provider mode".
- Audit delta row 21 still reads "about 4.8k" and attributes "parked, not deleted" to the owner on both 2026-10-05 and 2026-10-15. Correct it when the answers are applied.

Back to owner: no.

## Evidence freshness

- Main at `eba011df`, with the packet bytes as hashed above.
- I measured the script citers live over all tracked files.
- `bd ready` and the bead text come from the local Dolt read on 2026-10-21.
- Not inspected: bd remote, GitHub PR and CI state, origin tag protection, other sessions' worktrees, live CLI or daemon runs.