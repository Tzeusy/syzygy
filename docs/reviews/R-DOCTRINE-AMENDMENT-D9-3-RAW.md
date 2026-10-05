# Review - D9 doctrine amendment packet, round 3 (SEC-3 attended agent session)
Reviewed commit: 62c29093935c9370efe030d1a3a54672f50dbd72
Package digest: 7168a3e2f062b6c9d96ac0d9cb6bcee69900d49785261e44b02a0f950fbfe413
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context reviewer (CC-REV-1), not the drafter, round 3 (the
last confirming round). Brief: `REVIEW-BRIEF.md` in the package at the
reviewed commit. Work was done in a scratch clone checked out at the reviewed
commit, plus a second clone with arm A applied. `gh pr view 357` reports head
`62c29093935c9370efe030d1a3a54672f50dbd72`, draft, open. PR #353 was read only
from this repository's own ref `origin/openspec/polaris-dossier-local-agent-mode`
(head `b5ff7a3b`). No external or target repository content was fetched. The
owner's 2026-10-06 scope (any feature, per-run recorded choice naming what it
covers, no standing approval) is treated as the owner's choice, not a defect.

Package digest re-derived by the brief's method at the clone root over the six
tracked files (IMPACT-LEDGER.md, OWNER-DECISION-PACKET.md, REVIEW-BRIEF.md,
ROUND-1-DISPOSITIONS.md, ROUND-2-DISPOSITIONS.md, SEMANTIC-DELTA.md).

Summary: **0 revise-level findings, 7 notes (N1-N7).** Round 2's F1 and F2 are
resolved, and N1-N9 are resolved.
Criteria 1-6 are met. Every note is either for the owner's information (N1,
N2, N5, N6) or editorial (N3, N4, N7); none requires the package to change
before the owner can decide. Under the stopping rule, notes go to a sibling
record and the reviewed bytes are not repaired.

## What was re-derived (all [Observed], this session, at the reviewed commit)

- **Anchors.** `security.md` sha256
  `c2be53d1e25c18f9329e9e18caea2256773f584e7fd45077b9caa6323aaf4892`,
  `v1.md` sha256
  `99d3164f2150a0faeebe0221fe0a977cb6c9c07e8d456f328f42717b247e1505`;
  `sed -n 61,70p security.md | sha256sum` gives
  `71ab005a4ad61cd18be74cf4b601382dae9016f3a9acef22de54c8d302a4c05a`, and
  `sed -n 119,120p v1.md | sha256sum` gives
  `3826334a2fc50fd29ff36fdd3c3f44f4318a5a133bfcada093b65437e319d033`. All as
  stated. `git diff 5126610b HEAD` over the doctrine, `contracts/rfcs/`,
  `policies/` trees and `PROJECT-STATUS.md` is empty; `5863d470..5126610b`
  touches only the four files the ledger names.
- **Fenced blocks** (Python `re`, bytes between ```` ```markdown ```` and the
  closing fence, trailing newline included):
  - arm A (a): 50 lines,
    `cd2d0372263cb48e38fb6fdbbc401f2d8284c027fad957eddb7e03d6d1cce5fd`;
  - arm A (b): 4 lines,
    `ee3c8b36fe57185ccac0d49ca8336179f64a1c5db7e188d689ff587e32a42743`;
  - arm W (a): 47 lines,
    `6f30724b09cbee5ad09e73ac69b13842ede9ad234a0d30d1547ed832c188e881`;
  - arm W (b): 3 lines,
    `73b2036b7978622f3b2d16841df52ec65ce3417fcc6dc3be740d352ebefc9b68`;
  - credential lines: 3 lines,
    `d28c1b72723ded7ca73098e2ef27ee3eb9927d844da486ae2c898759c9300fab`.

  All five match the delta. Widest line: 76 (arm A), 78 (arm W).
- **Removability.** The credential block occurs exactly once in each arm.
  Deleting it gives arm A (a) 47 lines,
  `7eaf25dab5ddaea366397571ee0d1db14a53659e108a04d7f814439a4ef4c01a`, and arm
  W (a) 44 lines,
  `d6b9cf9c50399f029195cb2d6f83a65ab00bc075639c680336f6e1a6bc2777a9`, both
  equal to the delta's no-credential digests. Read in full, both results are
  grammatical: arm A's list ends "as the session's own report." and is
  followed by "**Whom the case binds:**", which names no condition; arm W's
  list ends "report." and is followed by "**What the exception does not
  cover:**". No remaining sentence in either arm refers to the condition (the
  only remaining "credential" hits are the profile bullet, the cost bullet
  and the violation sentence). The delta's claim holds.
- **Ledger §1.** Re-implemented in Python `re` over `git ls-tree -r -z` blobs
  and `git cat-file --batch`:
  - `eb7be564`: 2,348 paths, 4 undecodable, 2,344 searched; **241** hits
    (exact 202, ccsec 4, range 58, slash 5); term sweep **250**. Exact.
  - `5863d470`: 2,353 / 2,349; **244** hits (exact 205, ccsec 5, range 59,
    slash 5); term **252**. The additions over `eb7be564` are exactly
    `docs/README.md`, `R-DOCTRINE-AMENDMENT-D9-1-RAW.md` and
    `R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-2-RAW.md`, as stated; none removed.
  - code-lane term hits at `5863d470` (extensions `.ts .tsx .js .mjs .py .sh
    .json .yaml .yml`, excluding `docs/evidence/` and `docs/pursuits/`):
    **17** files, the same 17 the ledger names.
  - `5126610b` (the branch base): 246 hits. Reviewed commit: 2,361 / 2,357;
    **253** hits (exact 214, ccsec 12, range 60, slash 6); term 261. The 9
    files over `5863d470` are the six package files, the register, the
    round-2 direction and the round-2 raw, matching the ledger's description.
- **Ledger §2.** The citation predicate at `eb7be564` gives **66** matches in
  **29** files. Exact.
- **Ledger §4, arm A application probe, re-run at the reviewed commit**
  (not at `5863d470`). Canonical battery read from `PROJECT-STATUS.md` "How
  to verify this page" and executed line by line:
  - unapplied clone: **78 commands, 0 nonzero**; `check_governance.py` "32
    OK, 21 WARN, 0 FAIL (53 checks)";
  - applied clone (arm A (a) and (b) from the fenced bytes, credential lines
    kept, committed; applied SEC-3 block hashes to `cd2d0372…` per the delta;
    SEC-3 at 61, SEC-4 at 112, SEC-5 at 125): **78 commands, 4 nonzero**,
    exactly the ledger's four: `check_governance.py` "31 OK, 21 WARN, 1 FAIL"
    (CG-18, 8 findings over fixtures 2, 4, 6, 9, digest and word count each);
    `build_contract_index.py --check` DRIFT on `05-CONTRACT-INDEX.yaml`;
    `build_budget_report.py --check` DRIFT on fixtures 2, 4, 6, 9 and
    `CONTEXT-BUDGET-REPORT.md`; `build_directive_register.py --check` stale,
    and on regeneration the only register diff is SEC-4 72 → 112 and SEC-5
    85 → 125. `record_polaris_understanding_adoption.py --check` exits 0.
  - The no-credential line figures (SEC-4 at 109 under arm A) follow from 47
    block lines (61..107, blank 108); not probed, as the ledger says.
- **Register.** Rows by `^\| P-[0-9]+[^ |]*` per `##` section: 31 open, 5
  acceptance-act, 36 in all, as the round-2 note states.
- **Quotations.** The quotations new or moved in this repair were located in
  their sources: "That was the lead's reading, not the doctrine's text"
  (review-1 rulings direction 23-24), "Separate OS user" (records direction
  32), "Doctrine's text prevails over any paraphrase here" (CC-SEC-3 file
  line 21), "Run the project's own test command to get better evidence"
  (line 78), "POC never executes Butlers code, only observes it"
  (`three-surface-poc-experience/CONTRACT-COVERAGE.md` 351), and the round-2
  direction's option labels "Any feature, per-run choice", "Dossier briefs
  only", "Any feature, standing choice", "Close the gap, one more round",
  "Accept the gap, adopt soon". The RFC 0005 quotations are in an unchanged
  tree and were confirmed in round 2.
- **Criterion 6.** The branch over `5126610b` touches only the six package
  files and `PENDING-OWNER-DECISIONS.md`. No doctrine byte, no code.

## Round-2 findings: does each repair hold?

**F1 - resolved [Observed text; Inferred reading].** The owner chose the
width; the test is whether the package states it everywhere.
- Arm A (a) text: "the owner has recorded a choice for that one run, naming
  what the instruction covers. A standing or per-project record does not
  qualify." Condition 1: "The owner's choice for the run is recorded before
  Syzygy issues the instruction." Violation sentence: "Syzygy instructs it
  only on the owner's recorded choice for that run"; new violation: "before
  the owner's choice for that run is recorded, or on a standing record".
- Delta arm A heading: "Arm A, recommended: any feature, on a choice recorded
  per run", "wider than the owner's dossier ruling", the dispatched-work-item
  example, "needs no new doctrine act".
- Packet §1 (the answers), §2 ("This is wider than your dossier ruling, by
  your 2026-10-06 choice", the work-item example, "needs no new doctrine
  act"), §3 ("The packet no longer calls it minimal"), Q1 ("It is wider than
  your dossier ruling") and the preserved trade-off paragraph.
- P-103 row: "on a choice the owner records for that one run, naming what it
  covers; a standing or per-project record does not qualify. This is wider
  than the dossier ruling, by the owner's choice, and a future feature needs
  no new doctrine act."
- No sentence in the package now calls arm A minimal or says it matches the
  ruling as a claim; the remaining occurrences are quotations of the retired
  claim (see N4). The granularity residue is N1.

**F2 - resolved [Observed text; Inferred effect; the RFC5-24 effect is
reported for the owner].** Condition 4 now reads "Syzygy keeps every
credential it holds for its typed adapters where neither the session nor any
process it starts, directly or not, can read it at the operating-system
level, for as long as any of them runs." This reaches a server or background
job the session leaves behind, reaches grandchildren ("directly or not"), and
the delta and packet fix the reading at the operating-system level, excluding
agent tool-permission rules. Q3's cost no longer says "during attended runs";
it says "your user account must not be able to read it while any process the
session started is still running, which in practice means a separate OS user
or a protected store", and names that as the mechanism the owner declined for
records on 2026-10-05. Q3's cost is honest. A practical residue on duration is
N2.

**N1 (Q1/Q2 one choice) - resolved [Observed].** Q2 is folded into Q1 with the
row kept for numbering; packet §3 and the delta say arm A makes "the lead's
reading" the doctrine's text for execution and that this restores the premise
of the owner's first answer.

**N2 (whom the case binds) - resolved [Observed].** The text's bullet is
"**Whom the case binds:** Syzygy." and ends "Once the instruction is given,
SEC-3 governs what Syzygy does about the session, not what the session
does." Packet §2 says the limits are "limits on Syzygy's instruction", that
SEC-3 does not forbid the owner walking away or the session leaving a server
running, and that condition 4 stays Syzygy's duty. A smaller corollary is in
N6.

**N3 (definition of instruction) - resolved [Observed; Inferred
classification].** The definition is in arm A's text ("every instruction a
Syzygy feature gives an agent (a brief, prompt, skill or work item)"), and
ledger §3.6 classifies `AGENTS.md`, shipped skills and prompt kits, and a
typed CI adapter. A corollary for static skills is N5.

**N4 (provenance) - resolved [Observed].** Granularity is fixed in the text;
provenance is left to the specification and said so in packet §3, the delta
and ledger §5 item "6".

**N5 (false absence claim) - resolved [Observed].** Ledger §1 now names the
false sentence, states which lanes round 1 read, and lists the 17 code-lane
files; the 17 re-derive exactly.

**N6 ("shows Verified") - resolved [Observed].** Packet §3: "Verification can
then show `Verified`, when the commit matches, the run exits 0 and the capture
time is in range."

**N7 (digest-checkable deletion) - resolved [Observed].** Both no-credential
digests are given and re-derive; packet §7 step 2 and the delta's migration
step 2 say to check against them.

**N8 (attends) - resolved [Observed].** Arm A defines it positively ("being
present to see and stop what it does"); packet Q5 and the delta say an
auto-approve or permission-bypass session with the owner away is not
attended; ledger §5 notes Syzygy cannot observe attendance.

**N9 (commit date) - resolved [Observed].** Ledger: "committed 2026-10-05
23:57 +0800".

## Revise-level findings

None.

## Notes

**N1 [Inferred] (note, for the owner). "Run" is the unit of the owner's
per-run choice, and nothing defines it.**
- In arm A (a), "a choice for that one run" has no antecedent noun: the only
  earlier "run" is the verb in "build and run observed-project code". Arm A
  (b) for `v1.md` reads "on the owner's recorded choice for that run", where
  no run has been mentioned at all.
- The owner's words were "that one run", so the text is faithful. But the
  bound that separates "per run" from "standing" now rests on what each
  feature calls a run. A feature that defined a long-lived run (a dispatch
  batch, a standing monitoring run) would satisfy the letter while
  approaching a standing approval. "Naming what the instruction covers"
  bounds this partly.
- PR #353 closes it for the dossier: its proposed requirement makes the
  choice "a record for one run that names what the instruction covers: the
  run, its pinned revision, and building and running the observed project in
  the clone from that run's authoring session".
- The packet says who records the choice is left to the specification; it
  does not say that what a run is is also left there. One sentence in Q1 or
  Q5 would put it to the owner. Not revise-level: the text implements the
  owner's words, and the owner can decide with this note.

**N2 [Inferred] (note, for the owner). In practice condition 4 is permanent
from the first permitted run.**
- "For as long as any of them runs" bounds the duty in time, and Q3's cost
  reads as a window ("while any process the session started is still
  running").
- Syzygy cannot observe which processes a session started or when the last
  of them ends, any more than it can observe attendance. Observed code can
  also install persistence it then re-launches from (a cron entry, a user
  service, a login item), since the cost bullet says it "can change any file
  the owner can". Whether a job the scheduler starts is a process the
  session "starts, directly or not" is a reading, not a stated rule.
- So once any permitted run has happened, the only way Syzygy can know the
  condition holds is to keep the credential unreadable by the owner's user
  from then on. The packet's "in practice means a separate OS user or a
  protected store" already implies a standing mechanism, so the cost is not
  misstated, but it could say "from the first such run on" plainly.
- Q3's "That keeps RFC5-24 true, including for a server the session leaves
  running" holds on the reading that scheduler-started jobs count as started
  "not directly". Observed code that a process *not* started by the session
  later executes (an owner's own command running a file the session
  rewrote) is outside condition 4. It is also outside arm A's scope, as a
  hand-typed command, and it would expose a credential readable by the
  owner's user with or without D9.

**N3 [Observed] (note). The violation lists name "a standing record" but not
"a per-project record".** Arm A: "before the owner's choice for that run is
recorded, or on a standing record"; arm W the same. The case condition
excludes both ("A standing or per-project record does not qualify"), so an
instruction on a per-project record is still forbidden, by "What this binds"
under arm A and by condition 1 under arm W. This is an asymmetry, not a gap.

**N4 [Observed] (note). ROUND-2-DISPOSITIONS F1's absence claim is false as
literally stated.**
- It reads: ""Nothing more" and "matches the ruling" are gone (0 occurrences
  in the package)."
- Predicate: Python `re.escape`, case-insensitive, over whitespace-normalized
  text of the six package files. "nothing more" occurs 5 times in 3 files:
  OWNER-DECISION-PACKET.md 1 (§3 lines 147-148, quoting the retired claim),
  REVIEW-BRIEF.md 2 (criterion 1 and its round-2 test), and
  ROUND-2-DISPOSITIONS.md 2. "matches the ruling" occurs 2 times, both in
  ROUND-2-DISPOSITIONS.md.
- No occurrence is an assertion that arm A is minimal, so the substance of
  the repair holds. The claim needed its predicate stated (rule 9),
  "0 occurrences used as a claim", not a bare zero.

**N5 [Inferred] (note, for the specification lane). A shipped skill cannot
satisfy condition 1 itself.** Arm A counts a skill as an instruction and
requires "The owner's choice for the run is recorded before Syzygy issues the
instruction." A static skill is issued when it ships, before any run's choice
exists, so a skill can only defer to a per-run instruction; it can never carry
the permission itself. Ledger §3.6 says such a skill "is lawful only as the
permitted case" without drawing that consequence. PR #353's design already
complies ("Follow the execution rule in `brief.md`. Unless it says otherwise,
do not …"). Worth one line in ledger §3.6 or §5 for future features.

**N6 [Inferred] (note, for the owner). "Naming what the instruction covers"
limits the instruction, not what the session runs.** Under arm A, a session
that runs more than the recorded choice names is not a SEC-3 violation, by
the same "SEC-3 governs what Syzygy does about the session, not what the
session does". Packet §2 states the general rule and the walking-away and
server examples, but a reader could take the named coverage as a limit on the
session. Syzygy's duties still apply to what the session reports (every
claim Inferred, every reported command disclosed).

**N7 [Observed] (note, editorial).**
- `SEMANTIC-DELTA.md` line 43 is 128 columns, an unwrapped join in the arm A
  bullet; every other prose line in the delta is at most 83.
- `IMPACT-LEDGER.md` §5's ordered list is numbered 1, 2, 3, 6, 7, 4, 5 in
  source. CommonMark renders an ordered list from its first number, so the
  rendered page shows "Who records the owner's choice" as 4 and "Attendance
  is not observable" as 5, while ROUND-2-DISPOSITIONS N4 and N8 cite them as
  §5 items 6 and 7. The brief's round-1 pointer "§5 item 5" now lands on
  "Hosts".
- The register's round-2 note says it was counted "on this branch over
  `origin/main` `5863d470`", whereas the branch now sits on `5126610b`. The
  count (31 / 5 / 36) re-derives at the reviewed commit, so only the
  provenance phrase is stale.

## Other test points from the brief

- **Arm A against criterion 1 [Inferred].** Observed code still never runs
  inside Syzygy, or under anything Syzygy launches or schedules, outside a
  profile ("What this binds"). The permitted case requires the owner's own
  host, a session the owner started and attends, and a per-run recorded
  choice naming coverage; Syzygy never instructs without it (condition 1 and
  the violation); claims are Inferred; commands are disclosed. The packet
  states plainly that this is wider than the dossier ruling. Met, within the
  owner's 2026-10-06 scope.
- **Arm W consistency [Observed].** Arm W's condition 1 ("unless the owner's
  choice for that run, naming what the instruction covers, is recorded
  first. A standing or per-project record does not qualify.") and its
  violation sentence ("on a choice recorded for that run wherever Syzygy
  instructs it"; "before the owner's choice for that run is recorded, or on
  a standing record") match arm A's per-run wording. Arm W's "A process it
  leaves running after it ends does not [stay part of the session]" is
  consistent with condition 4, which binds Syzygy's credential handling, not
  the session's extent.
- **Whom the case binds (N2) [Observed].** Clear in the text, the packet §2
  bullet, the delta's "What arm A means" and the P-103 row ("The case's
  limits bind Syzygy's instruction, not the session").
- **Contract fit, CC-SEC-3, change class.** Unchanged from round 2 and still
  right [Inferred]: RFC5-18 is scoped by RFC5-19's "profiles govern only code
  Syzygy itself launches"; a brief acted on by a session the owner started is
  not Syzygy launching; the reader-map sentences are prose and Q3(c) is a
  fair route; CC-SEC-3's "Doctrine's text prevails over any paraphrase here"
  governs until a policy amendment; Normative is right.
- **Accepted-contract effects, reported for the owner, not resolved.**
  RFC5-12's "Absent: no observed code runs" changes effect in the permitted
  case under either arm, and Q3(a) puts that to the owner accurately.
  RFC5-24's "never visible to observed-project code" is kept true by Q3(b)
  on the reading in N2, and fails in effect without it, which Q3 states.
  Both are correctly placed owner items.
- **Criteria 2-4 [Observed].** "**It is untrusted whoever owns the
  project.**" and the violation sentence are verbatim in both arms; the
  distinguishing sentence and "Its exposure to the owner's credentials is the
  same" keep the distinction honest; both declined options are named in the
  cost bullet.
- **Readability.** The packet can be decided without the delta.
