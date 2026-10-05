# Review - D9 doctrine amendment packet, round 2 (SEC-3 attended agent session)
Reviewed commit: 63e4196885544d4b78e1995eb43c9f31359653c3
Package digest: c9b9d750eb7b959dac7cd005cce0cd95ee0654394970c95c1535cea20bc804c7
Verdict: REVISE

Reviewer: fresh-context reviewer (CC-REV-1), not the drafter, round 2 (the
confirming round). Brief: `REVIEW-BRIEF.md` in the package at the reviewed
commit. Work was done in a scratch clone checked out at the reviewed commit;
`gh pr view 357` reports head `63e4196885544d4b78e1995eb43c9f31359653c3`,
draft, base `main`. No external or target repository content was fetched.
PR #353 (`origin/openspec/polaris-dossier-local-agent-mode`, head
`20ad6f9d`) was read from this repository's own refs, for how the dossier
brief is issued.

Package digest re-derived by the brief's method at the clone root over the
five tracked files (IMPACT-LEDGER.md, OWNER-DECISION-PACKET.md,
REVIEW-BRIEF.md, ROUND-1-DISPOSITIONS.md, SEMANTIC-DELTA.md).

Summary: 2 revise-level findings (F1, F2), 9 notes (N1-N9). Round 1's R1 and
R3 are resolved. R2 and R4 are partly resolved, and their residues are F1 and
F2. Criteria 2, 3, 4 and 6 are met. Criterion 1 is not met as the packet
claims it (F1). Criterion 5 is met for identification, but one stated effect
(RFC5-24 under Q3(b)) is overstated (F2). Both revise-level findings concern
what the packet tells the owner. Each could be repaired with a few sentences.
Under the brief's stopping rule, though, this verdict sends the package to the
owner with both raws.

## What was re-derived (all [Observed], this session, at the reviewed commit)

- **Anchors.** `security.md` sha256
  `c2be53d1e25c18f9329e9e18caea2256773f584e7fd45077b9caa6323aaf4892` and
  `v1.md` sha256
  `99d3164f2150a0faeebe0221fe0a977cb6c9c07e8d456f328f42717b247e1505` match
  the delta. Lines 61-70 hash to
  `71ab005a4ad61cd18be74cf4b601382dae9016f3a9acef22de54c8d302a4c05a`, and
  `v1.md` 119-120 hash to
  `3826334a2fc50fd29ff36fdd3c3f44f4318a5a133bfcada093b65437e319d033`, both
  as stated. `git diff --quiet eb7be564 HEAD` over the doctrine,
  `contracts/rfcs/` and `policies/` trees is clean. Neither doctrine digest
  occurs in any tracked file except `SEMANTIC-DELTA.md` (`git grep -F`).
- **Fenced blocks** (Python, the bytes between ```` ```markdown ```` and the
  closing fence, trailing newline included):
  - arm A (a), 43 lines,
    `af06d7151abe8257e3783423143bc8d0d86ba01e46119edd9af1b4e85ea132b9`;
  - arm A (b), 4 lines,
    `a481b5a41bbc8fae940d989a723d597f5441b1aaff69aaebdb8a7fb5c677be2f`;
  - arm W (a), 44 lines,
    `3b932aec500e2582933836a0f64b60f3e48754f8391ca2ce2d45697a1f9cf5dc`;
  - arm W (b), 3 lines,
    `73b2036b7978622f3b2d16841df52ec65ce3417fcc6dc3be740d352ebefc9b68`;
  - the credential lines, 2 lines,
    `2316b61d2bce82b795845ce1ab810cea6b01dc2bcbeb7564a3710ad61948ee17`.

  All five are as stated. The credential lines occur exactly once in each
  arm. Every non-blank kept line of the old SEC-3 occurs verbatim in each
  arm, except where a line was rewrapped:
  - the opening sentence, which arm A rewords and arm W extends;
  - the last violation line, which now continues the sentence on the same
    line.

  The violation sentence itself survives byte for byte in both arms. The
  widest line is 77 columns in arm A and 78 in arm W; `security.md`'s widest
  is 83.
- **Ledger §1, at `eb7be564`.** Re-implemented in Python `re` over
  `git ls-tree -r -z` blobs:
  - 2,348 paths, 4 not UTF-8, 2,344 searched;
  - **241** hits: exact 202, ccsec 4, range 58, slash 5;
  - lanes: historical 42, reviews 28, doctrine 3, contracts 21, craft 4,
    decisions 4, openspec 9, candidates 86, topology and intent 5,
    evidence 20, design 8, code 5, root 6. The sum is 241. This reproduces
    the ledger exactly, lane by lane.

  The term sweep gives 250, also exact. **At the reviewed commit**:
  2,353 paths, 2,349 searched, **247** hits (exact 208, ccsec 10, range 59,
  slash 6). The extra 6 are the five package files plus
  `decisions/PENDING-OWNER-DECISIONS.md` (decisions 4 → 5, candidates
  86 → 91), as the ledger says. `git diff --name-only eb7be564 HEAD` lists
  exactly those six files.
- **Ledger §2.** The citation predicate at `eb7be564` gives 66 matches in 29
  files, 5 of them `DIRECTIVE-REGISTER.md` rows. The others cite lines 10 to
  85. The only one past 61 is
  `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1-RAW.md:290`,
  "(security.md:85-96)". This is exact.
- **Ledger §4, arm A application probe, re-run at the reviewed commit** (not
  at `eb7be564`). In the unapplied clone, the `PROJECT-STATUS.md` block gave
  78 commands with 0 nonzero, and `check_governance.py` gave "32 OK, 21 WARN,
  0 FAIL (53 checks)". In the second clone, arm A (a) and (b) were applied
  from the fenced bytes (credential lines kept) and committed. The applied
  SEC-3 block hashes to the arm A digest above. SEC-3 stays at 61, SEC-4 is
  at 105 and SEC-5 at 118. That clone gave **78 commands, 4 nonzero**,
  exactly the ledger's four:
  - `check_governance.py`, "31 OK, 21 WARN, 1 FAIL": CG-18, 8 findings over
    fixtures 2, 4, 6 and 9;
  - `build_contract_index.py --check`, DRIFT on `05-CONTRACT-INDEX.yaml`;
  - `build_budget_report.py --check`, DRIFT on fixtures 2, 4, 6 and 9 and
    on `CONTEXT-BUDGET-REPORT.md`;
  - `build_directive_register.py --check`, stale.

  `record_polaris_understanding_adoption.py --check` exits 0. The seven
  derived files hold. Arm W was not probed (the ledger says so too).
- **Quotations.** Each was checked whitespace-normalized against its source
  at the cited lines, and each matches:
  - RFC5-12 (`consent-egress-secrets.md` 108-109);
  - RFC5-24's two limbs (`admission-and-boundary.md` 354-362);
  - RFC-0005 README 105-107, 130-131 and 199-205;
  - `execution-profiles.md` 30-31, 139-143 (RFC5-19's last bullet) and
    263-265 (§4 case 7);
  - rulings direction 56-57, 60 and 61;
  - review-1 rulings 23-24, 74-77;
  - CC-SEC-3 (78-79) and its line 21;
  - `AGENTS.md` 89;
  - dossier review-1 finding 8 (raw line 323);
  - doctrine README 91-92.

  RFC5-20 "no ambient credential is ever inherited" is at
  `execution-profiles.md` 172, with bold markup stripped. `contracts/rfcs/`
  and `contracts/candidates/rfcs/` differ only by `RFC-0010` and `RFC-0011`.
- **Criterion 6.** The branch over `eb7be564` touches only the five package
  files and the register (+17 lines). No doctrine byte changed, and there is
  no code.

## Round-1 findings: does each repair hold?

**R1 - resolved [Observed].**
- **Arm A.** The permitted case is defined as Syzygy's instruction. Its
  first condition is "The owner's choice is recorded before Syzygy issues the
  instruction". The violation sentence, "Syzygy instructs it only on the
  owner's recorded choice", is therefore exact.
- **Arm W.** The grant reads "when the owner has chosen that". The sentence,
  "it runs observed code only because the owner chose that (on a recorded
  choice wherever Syzygy instructs it)", now matches it exactly.
- **Packet and register.** Packet §2 ("runs only on your recorded choice")
  is stated of "the case", which under arm A is Syzygy-instructed, so it
  holds. The P-103 row says "recorded" only of arm A.

**R2 - partly resolved; the residue is F1.** Arm A fixes the actor
dimension: the general exception is gone, and arm W is declared a widening.
Arm A is still not scoped to the ruling's mode, though, and the packet's
recommendation now claims it is ("A permits what you ruled and nothing
more"). See F1.

**R3 - resolved [Observed facts, Inferred readings].**
- Arm A names Syzygy as the actor, so CI and hand-typed commands fall
  outside the execution rule. The packet says plainly that this means "not
  governed", not "permitted", and puts the question to the owner as Q2.
- The capture tool now has a full ledger entry (§3.6) and a packet bullet.
  Its reading is right [Inferred]:
  - `capture-test-artifact-main.ts` lines 76-84 `spawnSync` the pytest
    command with `cwd: repoRoot` and no `env` option, so it inherits the
    caller's environment;
  - no file under `decisions/` or the POC change names it (sweep:
    `capture-test-artifact|test-run (evidence|capture)|focused pytest`,
    with 1 hit, the P-103 row);
  - under the actor-free text it is observed code outside a profile, and
    under RFC5-19 it is "code Syzygy itself launches" with RFC5-18 unmet.

  Its effect under each arm is stated correctly. Arm A's case is an
  instruction to a session, not a Syzygy spawn. Arm W's "any process Syzygy
  launches" keeps it forbidden. One consequence follows, and it is correct,
  if odd: under arm A the attended session may run pytest itself, but not
  through Syzygy's capture tool.
- The `AGENTS.md` 89 row is corrected.
- The instruction-file question is answered, by reading the brief in PR #353
  (`design.md`: `syzygy dossier brief <run>`, "Writes `brief.md` … with the
  execution rule in force"). The dossier's execution instruction is emitted
  by Syzygy's software, so arm A reaches it, as intended. A residue on
  static Syzygy-shipped instruction files is in N3. The ledger also has an
  absence claim that is false (N5).

**R4 - partly resolved; the residue is F2.** Both clauses are quoted exactly
and their effects are stated under each arm. RFC5-12's effect change ("Absent:
no observed code runs") is correctly put to the owner as Q3(a). The claim that
Q3(b) "keeps RFC5-24 true" overstates what condition 4's text does. See F2.

**Round-1 notes.** The repairs hold:
- N1: the placement is fixed; README 130-131 and 199-205 are added and
  quoted exactly;
- N2: the case-7 row is added;
- N3: packet §3 and Q4;
- N5: arm A has no "with the claims they support" restriction;
- N6: figures reproduce, see above;
- N7: the packet's quotation is now real;
- N8: in both violation bullets;
- N9 and N10: done;
- N11: kept as moot;
- N12: packet §3.

N4 is partly addressed: subagents and outliving processes are now covered,
and cloud and VM go to Q5. "Attends" itself is still undefined (N8 below).

## Revise-level findings

**F1 [Observed] text, [Inferred] reading (revise). Arm A permits more than
the owner's ruling, and the packet tells the owner it does not.**

- The ruling is mode-scoped. `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`
  line 56 reads: "In the local-agent mode the operator's agent session may
  build and run the observed project". The review-1 rulings (item 1) direct
  an amendment "to permit it", the dossier case.
- Arm A's permitted case names no mode, no feature and no instruction type:
  "On the owner's recorded choice, Syzygy may issue an instruction that lets
  an agent session on the owner's own host, which the owner started and
  attends, build and run observed-project code outside a profile."
  "Instruction" is defined in the delta as "a brief, prompt or work item that
  Syzygy's software emits". So any Syzygy-issued instruction qualifies, in
  any present or future feature, once a choice is recorded. That includes
  dispatched work items. The package's own ledger says so: §5 item 1, "a
  work item Syzygy dispatches that tells a worker to run tests is 'an
  instruction Syzygy's software issues'. It is lawful only as the permitted
  case".
- The doctrine text fixes no granularity for "the owner's recorded choice"
  (per run, per project, per mode, or standing). One standing record could
  cover every later instruction.
- Against that, the packet's Q1 recommendation reads "A permits what you
  ruled and nothing more". The delta heads arm A "recommended, matches the
  ruling". The ledger's own §5 item 1 contradicts both. Criterion 1 is
  "permits the owner's ruling and nothing more", and the brief asks this
  exact question.
- This is not a call for a mode-named doctrine clause. Doctrine naming a
  specification mode would be unusual, and a general permission gated per
  use by the owner's recorded choice may well be what the owner wants. The
  defect is the claim. The owner is told the text is minimal when it is
  general along the instruction axis, and the one consequence that shows
  this (dispatch) is visible only in the ledger.
- **Repair:** in Q1 and the delta's arm A heading, say that arm A permits any
  Syzygy instruction, in any feature, on a recorded choice, and give
  dispatched work items as the example. Either state the granularity the
  recorded choice must have or put it to the owner. Alternatively, narrow
  the case (for example, "an instruction that names its scope and is recorded
  per run"). That choice is the owner's.

**F2 [Observed] text, [Inferred] effect (revise; an accepted contract's
effect, reported for the owner, not resolved). Q3(b) is said to keep RFC5-24
true, but condition 4 and the packet's own cost text leave a population of
observed code it does not reach.**

- RFC5-24's limb is "never visible to observed-project code." Condition 4
  reads: "No credential Syzygy holds for its typed adapters is readable by
  the session." Arm A's "Where the case ends" bullet reads: "A process it
  leaves running after it ends does not [stay part of it]". So observed code
  that the session starts and leaves running, such as a daemonized server or
  a background job, is observed-project code outside "the session" once the
  session ends. Condition 4 says nothing about it.
- Under arm A, nothing else does either. The process was started by the
  session, not by Syzygy, and arm A's execution rule binds only Syzygy, what
  Syzygy launches or schedules, and Syzygy's instructions. ("Syzygy's
  instruction never asks for one" constrains the instruction, not the
  process.)
- The packet's Q3 cost text names the mechanism that opens the gap: "Once
  Syzygy holds an adapter credential, it must be unreadable by your user
  **during attended runs**". A credential unreadable only during attended
  runs is readable afterwards by any observed process left running under the
  owner's user. RFC5-24's "never" then fails.
- Under arm W the same process is excluded from the exception and so
  forbidden, but the clause can still fail in fact.
- A second, smaller point: "readable by the session" is satisfied, on one
  reading, by an agent tool-permission rule that denies the session's file
  tools. Child processes ignore such a rule. The packet's cost text implies
  the OS-level reading ("a separate OS user or a protected store"), but the
  doctrine text does not say which.
- **Effect on the owner's decision.** Q3 recommends (b) "for RFC5-24" on the
  stated ground "That keeps RFC5-24 true". As drafted it keeps RFC5-24 true
  for the session's own processes while they run, not for observed code the
  session leaves behind.
- **Repair:** make condition 4 reach every process the session starts, for
  as long as any runs (for example, "is readable by the session or by any
  process it starts"), and drop "during attended runs" from the cost.
  Alternatively, state the residual in Q3 so that the owner accepts it, as
  under (a). Whether to accept a residual is the owner's call.

## Notes

**N1 [Inferred] (note). Q1 and Q2 are one choice presented as two, and Q2's
recommendation adopts a reading the owner was told was mistaken.**
- Arm A is the "No" answer to Q2, written as doctrine. Arm W is a "Yes"
  without the list of lawful outside executions. So "A + Yes" and "W + No"
  are incoherent, and the packet does not say so.
- Q2's "Yes" is priced "needs a new draft and a new review" without noting
  that arm W is that draft, minus the list.
- `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md` 21-26
  discloses that "SEC-3 only binds Syzygy's own execution" "was the lead's
  reading, not the doctrine's text". Q2's "No" makes that reading the
  doctrine's text (for execution).
- That is a fair thing to recommend, and it arguably restores the premise
  under which the owner first chose "Allow, disclose" (rulings direction
  line 33). The owner should be told so in the packet, not only in the
  delta's evidence list.

**N2 [Inferred] (note). Under arm A, the case's limits bind only what Syzygy
may instruct.**
- The packet §2 "Where the case ends" reads as limits on the session ("A
  session … left running unattended does not count. … A process left running
  after the session ends is not"). Under arm A's actor clause, they constrain
  only to whom Syzygy may issue the instruction, and what it may ask.
- Once the instruction is lawfully issued to an attended session, SEC-3 says
  nothing about that session if the owner walks away, or about what it
  leaves running. Syzygy also cannot observe attendance.
- This is the same consequence as Q2's "not governed", and the packet should
  state it at the bullet, so the owner does not read those lines as
  prohibitions.

**N3 [Inferred] (note). "An instruction Syzygy's software issues" is defined
only in the delta, and its edge reaches further than the ledger says.**
- The definition ("a brief, prompt or work item that Syzygy's software
  emits"; `AGENTS.md` excluded) is in the delta's terms section, not in the
  arm A text. A reader of `security.md` alone will not have it, and Q5's
  "keep the definitions in place" does not cover it.
- Two edges are unclassified:
  - Static instruction text that Syzygy ships but does not emit at run time:
    the `/polaris-dossier` skill named in PR #353's `design.md`, and the
    prompt kit under `docs/polaris-generation/`. Under the `AGENTS.md`
    reasoning these are not "issued", so arm A would not govern a Syzygy-
    authored skill that told an agent to run observed code.
  - A typed CI adapter. RFC5-24 lists "CI" among the external authorities
    whose adapters Syzygy may hold, so a Syzygy-triggered CI run of the
    observed project is plausibly "an instruction Syzygy's software issues".
    Arm A would then forbid it, while RFC5-19 treats "the project's own CI
    artifacts" as outside Syzygy.

  Ledger §5 item 1 squares dispatch only.

**N4 [Inferred] (note). "The owner's recorded choice" has no stated
provenance.**
- In PR #353's design the choice is made at step 3 and recorded by the
  *agent* running `syzygy dossier init --config <answers>`. It lands in a
  state directory that the owner's records ruling
  (`POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-DIRECTION.md` item 2) treats as
  agent-editable.
- Neither arm requires the record to be attributable to the owner. Condition
  1, and the violation sentence's "Syzygy instructs it only on the owner's
  recorded choice", can therefore be satisfied by a record the session
  itself wrote.
- The specification may close this. The packet should tell the owner that
  doctrine leaves it open.

**N5 [Observed] (note). The ledger's absence claim about the capture tool is
false.**
- §1 says: "Neither sweep finds `capture-test-artifact-main.ts`. That file
  names no identifier and no term." The term predicate matches it at
  `eb7be564` and at the reviewed commit: line 16, "executing observed", in
  the usage text "see AGENTS.md "Syzygy executing observed code"". The sweep
  found the file; the read of its hits skipped the code lane (§1 lists the
  lanes read).
- Rule 9: correct the sentence, and say which lanes' term hits were read.
- A spawn-call sweep found no other observed-code executor. It covered
  `spawnSync|execFileSync|spawn\(|execSync|child_process|subprocess` over
  non-test files under `apps/`, `packages/` and `scripts/` at `eb7be564`, and
  the four non-git candidates were inspected [Inferred; the sweep is not
  exhaustive of indirect execution].

**N6 [Observed] (note). The packet's capture-tool bullet overstates one
fact.** "Verification then shows `Verified`" is unconditional, but
`docs/THREE-SURFACE-POC.md` ("When verification renders `Verified`") gives
three conditions: matching commit, exit 0, and a capture time in range. Say
"can show".

**N7 [Observed] (note). The credential-line deletion is clean, but the
result is not digest-checkable.**
- Deleting the two lines leaves both arms grammatical and exact:
  - each list then ends at "as the session's own report." (arm A) or
    "report." (arm W);
  - no other proposed sentence refers to condition 4;
  - the cost bullet's "any Syzygy credential readable on that host" still
    reads correctly.
- Without the lines, arm A (a) is 41 lines, sha256
  `478e046ec2601b205809d7cb77c9cb672f97c5dabc8b7175346ac344ecf47069`, and
  arm W (a) is 42 lines,
  `cd918d478d047c0e2db3b883a63643891298e28a5ffac9cb4409ca5778015865`.
  SEC-4 then lands at 103 under arm A, not 105.
- The delta gives neither digest. The migration step "delete the credential
  lines" therefore cannot be verified by script (rule 3).

**N8 [Inferred] (note). "Attends" is still defined only by exclusion.**
- The text says what is not attended (a session left running unattended),
  not what attending is. It leaves open, for example, a session in an
  auto-approve or permission-bypass mode with the owner away from the
  terminal.
- In PR #353's design the authoring session is interactive. The inventory
  and review sessions run as `claude -p` / `codex exec` and are not given the
  execution rule, so the dossier does not hit the gap today.
- Q5 is a fair offering. The owner should know this case is the one it
  leaves open.

**N9 [Observed] (note).** Ledger "Commits used below" dates `eb7be564` as
2026-10-06. Its commit date is 2026-10-05 23:57 +0800. This is trivial.

## Other test points from the brief

- **Contract fit (RFC5-18).** It holds as round 1 found [Inferred]. In PR
  #353, `brief` is run by the agent and emits text; no Syzygy command starts
  the authoring session. At steps 9, 10 and 12, `session-prompt` prints a
  command that the operator types. A Syzygy brief that a session started by
  the owner acts on is not "code Syzygy itself launches". The reader-map
  sentences are prose, under their own "clause wins" rules, and Q3(c) is a
  fair way to conform them.
- **CC-SEC-3 (Q4).** The packet's reading is right [Inferred]. The "tempting
  violation" sentence carries no "Syzygy addition" marker, so line 21,
  "Doctrine's text prevails over any paraphrase here", governs until a
  policy amendment. CC-BAR-5 floor 6 ("untrusted observed code") is owned by
  doctrine, and "Only the owner can change them, through the artifact that
  owns each floor (doctrine amendment …)", so D9 is the lawful route.
- **Change class.** Normative is right.
- **Criteria 2-4.** Met in both arms. "**It is untrusted whoever owns the
  project.**" and the violation sentence are verbatim. The distinguishing
  sentence and "Its exposure to the owner's credentials is the same; what
  differs is that nothing claims otherwise" make the distinction honest
  (false containment versus disclosed exposure). The two declined options
  are named in the text.
- **Readability.** Apart from F1, F2 and N1, the packet can be decided
  without the delta.
