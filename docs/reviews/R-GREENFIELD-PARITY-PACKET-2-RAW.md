# Round-2 adversarial review: greenfield-parity owner questionnaire

I recommend only one of the four asked items as drafted: none. Q0, Q1 and Q7 are Revise on both scope and recommendation. Q8's recommendation is Reject. In the table, Q3 and Q6 pass, Q2 and Q4 need revising, and Q5 should go back to the owner.

**Subject.** `/home/tze/GitHub/syzygy/.syzygy/local/questionnaires/2026-10-21-greenfield-parity.md`, 305 lines, at main `eba011dfbe254c09a88ccc374b3efe5ff5df1762`. I read round 1's raw but did not rely on it. Paths below are relative to `/home/tze/GitHub/syzygy`.

**Method.** All commands were read-only, using `grep -F`, Python, `git ls-tree -z`, `git cat-file --batch`, and `bd show`/`bd ready`. I made no file, bd, git or network writes. I read no Butlers or other observed-repository content. Scratch scripts are in `/tmp/claude-1000/-home-tze-GitHub-syzygy/9297eba3-858b-4aca-a313-05ea0802ad02/scratchpad/review2/`.

## Packet-level findings

**P1. Counts hold, but two of the 46 can't start yet.** [Observed] There are 64 `syzygy-bpyt*` beads, all open: 54 non-epic, 8 owner-gated, so 46, plus `0kq` (open, parent `bpyt.9`). Two of the 46 wait on gated beads: `9.5` waits on `9.2`, and `10` waits on `1.7`. So a "confirm" releases 44 plus `0kq`, not 46.

**P2. The default "no `syzygy-bpyt` bead dispatches" is not enforced.** [Observed] `bd ready` already lists `2.1`, `4.1`, `4.2`, `4.5`, `4.6`, `5.4`, `5.5`, `6.1`, `6.2`, `7.2`, `8.1`, `8.3`, `8.4`, `9.1` and `9.4`. That includes the trust-boundary beads `6.2` and `8.4`. Every bead's cold start says "Authority: the owner's 2026-10-20 direction … behavior-preserving simplification". That presents the session's [Inferred] reading as the owner's words. Until those beads are gated on `1.2` or the cold start is reworded, any parallel or worker lane can pick them up.

**P3. "Decided without asking" contradicts two written records.** [Observed]
- **The direction file.** `OWNER-DIRECTION-GREENFIELD-PARITY-SIMPLIFICATION-2026-10-20.md` item 4 lists all seven topics for the owner, each "done only as answered". The table does Q2's repair and Q5's move without an answer. Q0's boundary only confirms "items 2–3 as recorded", so the narrowing of item 4 is never put to the owner.
- **Bead `1.2`.** Its text reads: "Agent decides the low-risk ones: rejected; none of the nine is an implementation-plane choice." The table is a direct conflict with written bead text, which is a decision-autonomy hard gate.
- **Fix.** Q0 should carry an explicit "confirm the table as listed" line that the owner answers (silence is not enough), and bead `1.2`'s rationale should be corrected in the same pass.

**P4. The autonomy direction is cited in the wrong place, and too strongly.** [Observed] The table and Q0's options cite "owner direction of 2026-10-15 recorded in agent memory". It is in the repository: `.syzygy/governance/decisions/OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md` §2, lines 34–44. Lines 122–130 of the same record limit it:
- the application is "[Inferred: the lead session's reading…]";
- "authorizing implementation" still goes to the owner;
- "This record … authorizes nothing by item 2";
- "A later direction may narrow or withdraw this one."

So option B's con, "contradicts the 2026-10-15 autonomy direction", is not a con. An owner who chooses B narrows the direction lawfully.

**P5. Round-1 findings 3 and 4 are still open.** [Observed]
- Bead `1.1` asks for the packet to have "a row in .syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md pointing at it".
- The packet sits under `.syzygy/local/`, which `.gitignore:11` ignores. So no register row can point at it, and its raws are untracked.

**P6. The table doesn't say what happens to the implementing beads.** [Observed] Beads `1.3`, `1.4` (titled "with shims") and `1.5` get no disposition, even though the table changes what they would do (for example, Q5 is now "no shims").

---

## GP-Q0: confirm the reading of the 2026-10-20 request

**Scope verdict: Revise.** Several problems:
- The definition is misquoted.
- The packet states a "named finding" reading that the recorded reading does not contain.
- The trust-boundary list was set by the agent and is incomplete.
- Beads that change output are under-counted.
- The class of bug fixes and fail-closed tightening contradicts the packet's own boundary.
- Item 4's narrowing is not asked.

**Recommendation verdict: Revise.** A's direction is right: proceed, gated by independent review, and per-bead owner stops add little. But the reasons are circular, the "new" safeguard is policy already in force (CC-REV-1), and the class it releases contradicts the boundary.

**Material corrections:**
1. **The definition drops two words.** [Observed] Direction item 2 says "a signed or digest-bound artifact"; packet line 41 drops "signed or". Restore them.
2. **The "named finding" reading is not recorded.** [Observed] Item 3 admits POC beads "because the owner put 'everything' up for refactoring". No recorded text counts PA-/DC-/PD- IDs as named findings, yet the boundary confirms "items 2–3 as recorded". Either drop line 55 or put it to the owner as a new reading. Also, PD-* findings are dossier work, not POC work. They fall under item 2 (the acts in force), not under the POC cycle direction.
3. **`6.2` is listed twice.** [Observed] It appears as behavior-preserving (line 47) and as changing refusal reasons (line 54). Refusal strings are inside the definition, so it belongs only in the output-changing class.
4. **`4.1` is not a fix toward a signed spec.** [Observed] It repairs the test guard after incident `syzygy-w90k` and cites no requirement. Reclassify it.
5. **Undisclosed output changes.** [Observed]
   - `5.4` removes routes.
   - `2.2` and `2.3` change the canonical battery and retire tooling.
   - `9.4` edits `PENDING-OWNER-DECISIONS.md`. That is the governed plane, outside item 2's implementation-plane scope.
6. **The trust-boundary set is incomplete.** [Observed]
   - `7.3` moves `credentials.ts`, which its bead calls "the client-class boundary (RFC 0005…)"; the bead says "review with the default model".
   - `7.2` deletes or fixes `write-guard.ts` and `write-boundary.ts` (the write universe, CC-REV-1 class 1). Its arm "keep it and fix startsWith (normalize first)" changes what `authorizeWrite` accepts.
   - `6.3` touches `canonicalJson`/`sha256`; its acceptance criterion 3 is "responseIdentity digests … identical" (class 3).
   - CC-REV-1 (`.syzygy/governance/policies/craft-and-care/review-and-documentation.md:16`) says "the agent performing the change never finally decides which classes it touches", and "The change record states which classes the change touches, or 'none'". Replace the list of six with that predicate.
7. **The review is not new.** [Observed] CC-REV-1 already requires an independent, fresh-context reviewer for classes 1, 3 and 4 ("anything under SEC-1…SEC-5, auth surfaces, egress paths"). A adds only the model tier, so say A relies on the policy in force.
8. **The rationale is circular, and goldens are not enough.** [Inferred] "Change no accept or refuse outcome by definition" assumes what it should prove. For the parser and evaluator rewrites (`8.4`, `7.4`, `6.5`, `6.2`), a golden of today's fixtures proves only today's fixtures. Require an old-versus-new differential over a mutated-record corpus, including Q6's altered-prose records, plus a rule-6 mutant per predicate.
9. **Tightening contradicts the boundary.** [Observed] Option A releases "fail-closed tightening"; the boundary says "any change to what a gate accepts or refuses stops and returns to the owner". Enumerate the tightening beads for owner approval, or route each one.
10. **Option C is mislabelled.** [Observed] M1a, M1b and M2 contain `2.2` and `3.2`, both trust-boundary beads, so "Smallest blast radius" is false.
11. **A middle option is missing.** A, plus a non-blocking owner notice at each trust-boundary merge (PR link and class statement, carried in the cycle report). That gives the owner sight without a stop.
12. Ask about item 4 and the table (P3); enforce the default mechanically (P2); use the right count (P1).

**Evidence freshness:** `eba011df`; the direction file, the POC cycles direction, CC-REV-1, and a bd local Dolt read plus `bd ready` on 2026-10-21. Not inspected:
- bd remote `refs/dolt/data`;
- other sessions' claims (two `.claude/worktrees/agent-*` checkouts exist);
- GitHub PR and CI state;
- the 2026-10-20 owner message, which lives in another session.

---

## GP-Q1: may evidence leave the tree for a tag?

**Scope verdict: Revise.** It is right that this is the owner's call, but the authority is mis-anchored and the bead estimate is misread.

**Recommendation verdict: Revise.** Separate the principle from the mechanics. The stated family key and CI rule do not do what the packet claims, and the tag is not what makes a file resolvable.

**Material corrections:**
1. **The quoted rules are about one claim, not all evidence.** [Observed]
   - SDR-9 (`SURFACE-DECISION-RECORD.md:92-95`) and CC-TEST-2 (`testing-and-verification.md:31-48`) govern the claim "tests passed". The packet's quote drops that subject.
   - The clause that covers all evidence is `.syzygy/governance/policies/craft-and-care/engineering-bar.md:57`: "Verification evidence is a retained, resolvable artifact".
   - The packet omits an act: the Capability 1 implementation-authorization act, line 65, "verification claims require retained, resolvable evidence".
   - It also omits SDR-10, "evidence identities and hashes".
   - Round 1's "not retention posture" overcorrected. [Inferred] The same act's escalation list, line 39 (written for stack and layout choices), names "retention obligations".
2. **Counts confirmed, but the predicate must be stated.** [Observed] At `eba011df`: 403 files, 20,792,364 B; 150 and 227 under the basename predicate. A full-path predicate gives 175 and 249. At `dd520e8d`: 388 files, 20,450,788 B; 148 and 218.
3. **The burst is shorter than stated.** [Observed] The 15 additions span 23:32:47 to 03:37:07 (+08:00), about 4h05m, not "about 4.5 hours".
4. **Bead `9.2`'s estimate is misread.** [Observed] Its three numbers are disjoint and sum to 388 at `dd520e8d`: 168 free to move, 36 that move after a citer repair, 184 that stay. So about 204 can move, 36 of them after repairs. The packet's "168, of which 36" was copied from round 1.
5. **The family key bounds almost nothing.** [Observed]
   - It yields 394 families for 403 files, with only 5 multi-member families (14 files).
   - Only 9 files are non-newest members, 4 of them uncited outside `docs/evidence/`.
   - Bead `9.1`'s prefix glob counts 27 `fresh-checkout-demo` members; the key finds 5.
   - Every new single file stays its family's newest forever.
6. **The CI rule contradicts the monthly cadence.** [Inferred] The rule fails a non-newest file on the commit that adds a newer one, so archiving cannot wait for the monthly pass.
7. **Main's history makes a body resolvable, not the tag.** [Inferred] Any body ever on main resolves as `<commit>:<path>`; a tag only guards against history rewrite. Index rows should name commit, path and sha256. Moving bodies out does not shrink `.git` or a clone, only the working tree and sweep surface, so option A's "Bounds the tree" should say that.
8. **Unverified safeguard.** [Unknown] Whether origin protects tags from deletion. Option A's "no tag is ever deleted" depends on it.

**Evidence freshness:** `eba011df` and `dd520e8d`, read through git object reads; bead text from local Dolt on 2026-10-21. Not inspected: origin's tag-protection settings, citers outside this repository (other worktrees, PR bodies), and CI.

---

## GP-Q7: the dossier's execution-permitting arm

**Scope verdict: Revise.**
- Most of the question is already answered by signed text and the D9 adoption.
- The packet omits two SEC-3 clauses and the 2026-10-07 rulings on the D9 notes.
- It overstates how a Syzygy-launched run gets exposed.

**Recommendation verdict: Revise.** Conditional A is the right direction. But its preconditions mostly restate signed text, it leaves a fail-open read in place until the flip, and it does not name the standing cost the flip starts.

**Material corrections:**
1. **Two load-bearing SEC-3 clauses are missing** (`.syzygy/governance/doctrine/security.md:61-111`). [Observed] The packet's other quotes are exact.
   - "A standing or per-project record does not qualify." (lines 78–79)
   - "Syzygy keeps every credential it holds for its typed adapters where neither the session nor any process it starts, directly or not, can read it at the operating-system level, for as long as any of them runs." (lines 86–88)
2. **The D9 review notes were ruled on 2026-10-07.** [Observed] N1, N2 and N6 were ruled in "1.1 signed off with N6, N1 and N2 as recommended" (`REDIS-LOCAL-AGENT-SITTING-DIRECTION.md:20-28`; `POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.1.md`, "Options: n6").
   - N2, accepted, means: "once Syzygy holds a credential, it is kept from your user account permanently" (v1.1 packet, question 3 (a)). The flip starts that cost, and the packet should say so.
   - Separately, the D9 row of `DOCTRINE-AMENDMENT-LOG.md` still says the notes "remain the owner's to rule on". That has been stale since 2026-10-07.
3. **The owner's intent is already on record.** [Observed]
   - Signed REQ-033 requires the permitting brief (`openspec/changes/polaris-dossier-local-agent-mode/specs/polaris-generation/spec.md:137-140`).
   - D9's packet question 4, "CC-SEC-3 follows after D9; the dossier brief is its named case", was adopted with "Adopt D9", which was read as adopting the packet's recommendations (`DECISION-HISTORY.md:185-190`).
   - So option C reverses owner acts, and the real open decision is whether to draft the CC-SEC-3 amendment now or hold.
4. **The launched-run exposure is narrower than stated.** [Observed]
   - `isLaunchedRun` is fail-open (`launched.ts:31-37`) and only `allow-execution` checks it (`cli.ts:365`).
   - But the supervisor writes `launched.json`, then issues the brief before any session starts (`polaris.ts:303-306`), and a run is briefed once (`brief.ts:217`, 'issued-already').
   - So a permitting brief in a launched run needs a choice record planted in advance, or deleted brief files.
   - The real defect is the fail-open read at `cli.ts:365`. [Inferred] Whether a session can alter `launched.json`.
5. **Precondition (2) is already signed text.** [Observed]
   - REQ-033 (`spec.md:15`) permits only when the session is "never a session Syzygy started, one left running unattended, or one left under an automatic-approval or permission-bypass setting while the owner is away".
   - Candidate REQ-044 (P-111) repeats it for launched runs.
   - [Inferred] With `PERMITTING_ARM_ENABLED = false` every brief already carries SEC-3's rule, so the fix changes no output and can land now under GP-Q0, at both sites (brief issuance and `allow-execution`).
6. **Precondition (3) is largely signed text too.** [Observed] REQ-033 already requires disclosing the honour system ("are labelled Inferred and are disclosed … within the agent sessions' write reach") and the credential-list source. Reword (3) to "verify the implementation discloses what REQ-033 requires". [Unknown] Whether today's brief and UI do; I rendered nothing.
7. **The empty credential list is documented, not hidden.** [Observed] `CONFIGURED_ADAPTER_CREDENTIALS = []` follows the 2026-10-07 sweep, and the probe's pass discloses that the list is operator-declared and Inferred. The real risk is that the hand-kept list goes stale once Syzygy holds a credential. Fail closed when any configured adapter declares a credential missing from the list, or derive the list.
8. **The code comment's unlock condition is stale.** [Observed] `execution-rule.ts:15` says "Off until S4 (syzygy-qkea.5) is merged". `qkea.5` is closed (PR #380). The flag's real gate is CC-SEC-3; write that at the flag.
9. **Two preconditions add nothing new.** [Observed] Precondition (4) is already mandatory under CC-REV-1 class 4. RFC5-12 (c) is queued and does not block, per D9 (a); the packet should say "non-blocking".
10. **Name the posture change in one owner act.** [Inferred] The CC-SEC-3 sign-off packet should state that signing enables the flip and starts N2's cost.
11. **Disclose the attendance limit.** [Observed for this review session; Inferred for dossier sessions] Attendance and the permission-bypass lapse are operator declarations Syzygy cannot observe. Sessions in this repository run with permissions bypassed, so the lapse clause is often the only control.

**Evidence freshness:** `eba011df`; dossier source files `execution-rule`, `launched`, `cli`, `credential-probe`, `polaris` and `brief`; the D9 log; the v1.1 sign-off; the D9 notes; candidate REQ-044. Not inspected: run-directory permissions and whether a session can write the marker, agent sandbox behaviour, any live run, and CI.

---

## GP-Q8: the parked provider island

**Scope verdict: Revise.**
- Both owner-word claims are wrong.
- Two recorded "nothing is deleted" texts are omitted.
- Signed text and acts in force are omitted.
- The spec and code scope are wrong.

**Recommendation verdict: Reject.** The corrected facts favour A, on reversibility, blast radius and greenfield rule 4 (once bead `8.1` lands, the island sits behind one narrow interface and is cheap to delete later). B should be offered honestly: as a re-specification of an adopted capability plus narrowing an in-force act, against two recorded directions.

**Material corrections:**
1. **The 2026-10-05 quote is wrong.** [Observed] The owner selected "Yes, as drafted (Recommended)", whose quoted draft says "The provider-route and egress packages are parked." (`POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md:41-51`). "parked: not offered for sign-off, not deleted" is the drafter's item 4 (lines 80–83). Round 1 made the same error.
2. **The 2026-10-15 characterization is wrong.** [Observed] The owner "selected none of them and answered in free text". Nothing records a decline of "Keep parked" alone. Full quote: "Syzygy should run *our local codex or claude cli binary* like a subprocess with explicit workspace/instructions/artifacts path and skill/mcp guidance, no custom SDK or API tooling".
   - That direction's item 1 says "Nothing is deleted".
   - The 2026-10-20 direction repeats: "It deletes no parked code."
   - Both are drafter text, but they are the recorded directions, uncontested. B overrides them.
3. **The rejected tooling was the offered adapters.** [Observed] Those were "Messages API adapter #264" and "Agent SDK adapter #258". No SDK or HTTP provider client is on main; the island is a pipeline behind `ProviderReply`. "The owner's own words reject" the island is [Inferred].
4. **Signed text is omitted.** [Observed] The v1.2 delta (`spec.md:3`) says "The provider mode is parked by the owner direction of 2026-10-05, not withdrawn" and "for a run in the provider mode every predecessor requirement and scenario keeps its bytes and its meaning". `proposal.md:94` says "Parked, not withdrawn". v1.2 was signed 2026-10-14.
5. **The spec scope is wrong.** [Observed]
   - No requirement set is provider-only: the adopted generator capability *is* the provider mode.
   - The operator-agent mode displaces named text in REQ-001/003/005/017/018/020/021/022/025 and reads all the rest.
   - The signed scenario "Provider-mode draft keeps the adopted rule" sits at `spec.md:191`.
   - The packet's "[Unknown] how many" can be counted now.
6. **Acts in force are omitted.** [Observed] The 2026-09-12 POLARIS-GENERATOR specification-adoption, applicability and implementation-authorization acts read "Authorize the full EXECUTION-PHASES.md implementation goal…". PROJECT-STATUS's completion bar is "the unchanged generator on two separately admitted real projects". Deletion needs an owner act narrowing that authorization, not only CC-REV-2.
7. **The code scope is incomplete.** [Observed] It leaves out the parked egress half: `EGRESS_V2_INSTANCE` and `readInForceEgress` in `packages/polaris-generation-consent/src/package-reader.ts`, and `consent-ports.ts`. Bead `8.4` defers these to "owner packet Q8" under a stale path.
8. **The island is smaller than stated.** [Observed] By bead `8.1`'s module list it is 3,803 source lines, not about 4.8k.

**Evidence freshness:** `eba011df`; the 2026-10-05, 2026-10-15 and 2026-10-20 directions; the v1.2 spec and proposal; beads `8.1` and `8.4`. Not inspected: PRs #258 and #264 on GitHub, and the owner transcripts (in the repository only as relayed text).

---

## Decided-without-asking rows

**Row Q2 verdict: Revise.** The reasons need correcting:
- "No moves" holds. [Observed] `package-reader.ts:28,29,782` and `gate-sources.ts:82,204` read the performed candidate packages. `public-source-classification.ts` names the package only in a comment, so replace that citation.
- The precedents are overreached. P-66 (b), "the next audit should not re-raise it", is about the CC-SPEC banner, and P-55 is about the OpenSpec archive. Only P-56 (b) is on point.
- The disposal of the round estate was never a register row. `ROUND-ESTATE.md:255-257` points at a packet that never held that question. The repair is a dated mark at that sentence saying so; the file is not digest-bound or quoted elsewhere.
- The exclusion predicate must apply to routing only. It must never apply to citer, reliance or digest sweeps (rule 9), and governance outputs must stay byte-identical (bead `1.1`, guardrail 10).

Back to owner: no.

**Row Q3 verdict: Pass.** P-33 shape (M), CG-1i, CG-7h and `CONTRACT-AMENDMENT-MANIFEST.txt:4` are verified. One attribution is off: "to both mirrors" comes only from the RFC5 act (line 66); the restyle act (line 33) says "take the same bytes". Record the P-33 constraint in audit delta row 58. Back to owner: no.

**Row Q4 verdict: Revise.** "Keep committed" holds, but one citation is wrong:
- The `05-CONTRACT-INDEX` readers are confirmed (`build_capability_1_views.py:47`, `build_polaris_project_wide_contract_coverage.py:22`, `pwb_requirement_amendment.py:63`, and the six `build_pwb_*` builders).
- `check_governance.py` lines 5655, 10722 and 10815 do not read `CONTEXT-BUDGET-REPORT`: they are an exemption entry, a docstring and the `MEASUREMENT_POINTER` string.
- The real constraints are elsewhere: installed RFC READMEs (0002, 0004, 0005, 0007, 0008, 0009) route to the report, `install_redis_sitting.py:118` uses it, and `build_budget_report --check` compares against it.

Back to owner: no.

**Row Q5 verdict: Revise.** The row's claims don't hold, and its plan conflicts with written bead text:
- **Digest claim false.** [Observed] "Their only digest citer is the approval-offer baseline" is false: four other evidence files cite the current digests of `build_active_manifest`, `build_budget_report`, `build_contract_index`, `build_task_router` and `verify_final_prespec`. The 150-of-585 drift is confirmed.
- **"No shims" conflicts with written bead text.** [Observed] Bead `1.1` guardrail 3 says "Keep the path (thin re-export or shim) when a bound file cites it". The bound `general-trusted-bootstrap-authorization/IMPACT-LEDGER.md`, a row of the package's transaction manifest, cites three of these scripts by full path at lines 190–192. `SIGNED_PACKAGE_MOVED_TARGETS` is defined for "a path that a later act moved", not for an agent's move.
- **The same-basename rationale is wrong.** [Observed] The candidates `scripts/` directory is "Self-rooted, portable" (candidates `README.md:101`), so embedded `scripts/X.py` strings already resolve. The real reason for same basenames is that line 3 of the act-bound WAVE-A/B manifests stays valid.
- **Code readers are not listed:**
  - `install_redis_sitting.py:117`, whose `is_file()` guard would skip silently after a move;
  - `build_contract_readability_restyle.py:92`, which runs in the battery;
  - `governance-docs.yml`, 10 lines;
  - the `CS=` variable form in `PROJECT-STATUS.md`;
  - `SECURITY.md:43`.
- **The 08j exception.** The "recorded exception" for the two `round-2026-08j` sweeps should be a disclosed remainder, not an exception the agent grants itself.
- **It is a change on a reserved item.** Unlike the status-quo rows, this one acts, on an item the direction reserves for an answer.

Back to owner: yes.

**Row Q6 verdict: Pass.** Verified:
- The oracle: `gate-acts.test.ts:602-606` compares against the testkit, which spawns python3 (`recorder-fixtures.testkit.ts:19`).
- The field-parsed record forms: `recorderLines`, `parsePolicyAct`, and a registry form with no template.

Add three things:
- The CI recorder `--check` lines are what currently catch an altered record on main.
- Bead `2.2`, which replaces the battery's re-verifiers with a frozen act ledger, must keep the act-record hashes, or it removes that safeguard for this very finding.
- Record bead `1.5`'s disposition.

Back to owner: no.

---

## Overall evidence freshness

- Main at `eba011dfbe254c09a88ccc374b3efe5ff5df1762`; audit commit `dd520e8d`; bd local Dolt read on 2026-10-21.
- Not inspected:
  - bd remote and GitHub PR or CI state;
  - other sessions' worktrees;
  - live daemon or CLI runs;
  - run-directory permissions and agent sandbox behaviour;
  - origin tag protection;
  - the owner transcripts for 2026-10-05, 2026-10-15 and 2026-10-20 (relayed text only).