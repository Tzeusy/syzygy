# Review - D9 doctrine amendment packet (SEC-3 attended agent session)
Reviewed commit: c691c6a037098b86046958e0ed023e804edb626c
Package digest: efb43ad981c30a385ce06732c1e5d470e7bf6e9872d9980d3bb6de91b7886fd5
Verdict: REVISE

Reviewer: fresh-context reviewer (CC-REV-1), not the drafter. Brief:
`.syzygy/governance/contracts/candidates/doctrine-amendment-sec3-attended-agent-session-d9/REVIEW-BRIEF.md`
at the reviewed commit. Work done in a scratch clone checked out at the
reviewed commit (draft PR #357, `gh pr view` head = the reviewed commit). No
external or target repository content was fetched.

Package digest re-derived by the brief's method at the clone root:
`sha256sum $(git ls-files .syzygy/governance/contracts/candidates/doctrine-amendment-sec3-attended-agent-session-d9 | LC_ALL=C sort) | sha256sum`
over the four tracked files (IMPACT-LEDGER.md, OWNER-DECISION-PACKET.md,
REVIEW-BRIEF.md, SEMANTIC-DELTA.md).

Summary: 4 revise-level findings (R1-R4), 12 notes (N1-N12). Criteria 2, 4
and 6 are met. Criterion 3 is met in form, but the distinguishing sentence
leans on a property the operative text does not guarantee (R1). Criterion 1
is not met as drafted (R2, R3). Criterion 5 is not met: two accepted clauses
and one live implementation are missing or misstated (R3, R4). R3 and R4
report possible changes to an accepted contract's effect. They are for the
owner and are not resolved here.

## What was re-derived (all [Observed], this session, at the reviewed commit)

- Anchors. `security.md` sha256 `c2be53d1…4892` and `v1.md` sha256
  `99d3164f…1505` match the delta. `sed -n '61,70p' security.md | sha256sum`
  = `71ab005a…4c05a`, and `sed -n '119,120p' v1.md | sha256sum` =
  `3826334a…d033`, both as the delta states. The doctrine, `contracts/rfcs/`
  and `policies/` trees show no diff between `eacb85d1` and the reviewed
  commit. The delta's "Current meaning" quotation, with the `> ` prefixes
  stripped, equals lines 61-70 exactly.
- Proposed blocks. Hashed with their trailing newline, the bytes between the
  fences give `857184d8…3e74` for (a), 37 lines, and `73b2036b…9b68` for (b),
  3 lines, as stated. Each of the seven kept lines of the old SEC-3 occurs
  verbatim in block (a). Block (a) replaces 10 lines with 37, so 27 lines are
  added, as ledger section 2 says. Block (b) rewraps v1.md line 120: the old
  line is a prefix of the new one, so the old sentence survives byte for byte,
  but line 120's bytes do change.
- Ledger section 1. Its predicates, re-implemented in Python `re` over
  `git ls-tree -r -z` at `b60e6cd2`: 2,346 paths, 4 not UTF-8, 2,342 searched,
  240 hits (exact 201, ccsec 4, range 58, slash 5). That is an exact
  reproduction. My lane assignment gives the same counts for doctrine 3,
  contracts 21, craft 4, decisions 4, openspec 9, candidates 86, topology and
  intent 5, root 6, code 5, design 8 and evidence 20, and 69 for reviews plus
  historical together (my precedence splits them 49/20 where the ledger has
  27/42). The lanes sum to 240. At the reviewed commit the same sweep gives
  2,350 paths, 2,346 searched and **245** hits (exact 206, ccsec 9, range 59,
  slash 6). The diff against `b60e6cd2` is the package's four files plus
  `decisions/PENDING-OWNER-DECISIONS.md`, whose new P-103 row cites SEC-3
  (see N6).
- Ledger section 4 (application probe) was re-run at the reviewed commit, not
  at `eacb85d1`. The `PROJECT-STATUS.md` "How to verify this page" block
  (78 commands) ran in two clones. In the unapplied clone, 78 commands gave
  0 nonzero, and `check_governance.py` gave "32 OK, 21 WARN, 0 FAIL". In the
  clone with (a) and (b) applied from the fenced bytes and committed, 4 were
  nonzero, exactly the four the ledger names:
  - `check_governance.py` gave "31 OK, 21 WARN, 1 FAIL", the FAIL being CG-18
    with 8 findings;
  - `build_budget_report.py --check` gave DRIFT on fixtures 2, 4, 6 and 9 and
    on `CONTEXT-BUDGET-REPORT.md`;
  - `build_contract_index.py --check` gave DRIFT on `05-CONTRACT-INDEX.yaml`;
  - `build_directive_register.py --check` reported the register stale.

  In the applied file SEC-3 stays at 61, SEC-4 is at 99 and SEC-5 at 112.
  `record_polaris_understanding_adoption.py --check` and `--selftest` both
  exited 0 in the applied clone. The probe holds at the reviewed commit.
- Neither doctrine digest occurs in any tracked file outside the package
  (`git grep -F`). At the reviewed commit, `SEMANTIC-DELTA.md` itself carries
  both.
- Criterion 6. The commit touches only the four package files and
  `PENDING-OWNER-DECISIONS.md` (+10 lines). No doctrine byte changed
  (`git diff --quiet HEAD~1 HEAD -- .syzygy/governance/doctrine`), and there
  is no code.

## Revise-level findings

**R1 [Observed] (revise). The violation sentence distinguishes the attended
session by a "recorded choice" that the exception itself does not require.**
The operative grant in block (a) reads: "may build and run observed-project
code outside a profile when the owner has chosen that." Only the first
condition mentions recording: "Syzygy never instructs such a session to run
observed code unless the owner's choice is recorded first". So recording is
required only when Syzygy instructs. The distinguishing sentence then says:
"The attended session is not such a profile: it claims no containment, it
runs observed code only on the owner's recorded choice, and nothing resting
on it renders as more than Inferred." For any attended session that Syzygy
did not instruct (the general case the packet itself discloses in section 2
and ledger section 5 item 5), the choice need not be recorded. The sentence
therefore states, as a universal property, one the operative text does not
guarantee. The packet repeats it ("It runs the project only on your recorded
choice"), and so does the commit message ("may run observed code on the
owner's recorded choice"). Either the grant must require a recorded choice,
or the violation sentence must say "chosen" and confine "recorded" to the
case Syzygy instructs. This is the sentence criterion 3 depends on, so it
has to be exact.

**R2 [Observed] (revise). The drafted exception is wider than the owner's
ruling, and the packet's recommendation calls it the smallest.** The ruling
being implemented is scoped to the mode. `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`
line 56: "In the local-agent mode the operator's agent session may build and
run the observed project". `…-REVIEW-1-RULINGS-DIRECTION.md` item 1: "keeps
'Allow, disclose' for the operator's agent session, on the host, and directs
that an amendment to SEC-3 be drafted and reviewed to permit it". Block (a)
names no mode. Any agent session the owner starts and attends may run
observed code "when the owner has chosen that", whether or not Syzygy is
involved and with no record. The ledger (section 5 item 5) and the packet
(section 2, "One thing to know before adopting") disclose this honestly.
Criterion 1, however, is "permits the owner's ruling and nothing more".
Packet Q1 recommends **A** because "It is the smallest text that carries your
ruling". That is smallest in bytes, not in what it permits: arm C is the arm
that permits only the ruling. Arm C is also priced as "a redraft and a new
review" while A is priced as free, which leans the choice toward the wider
grant. Whether a general exception is wanted is the owner's call. The packet
has to present it as a widening beyond the ruling, which the owner may want,
and not as the minimal carrier. If A stays the recommendation, it needs a
reason other than minimality.

**R3 [Observed] facts, [Inferred] reading (revise; reported for the owner).
The closed "one exception" form, with "agent session" as its subject, leaves
existing lawful-looking executions forbidden or undetermined. The ledger
misses the live implementation that executes observed code.**

- Block (a) opens "Observed-project code runs only inside an explicit, opt-in
  execution profile, with one exception: the owner's own attended agent
  session". The current text names no actor, and the drafter reads it as
  binding everyone ("Current meaning"). Naming exactly one exception turns
  that reading from an ambiguity into an explicit rule: every other
  execution of observed code anywhere, outside a profile, is a SEC-3
  violation. That would include:
  1. the observed project's own CI. RFC5-19 treats its artifacts as lawful
     evidence "produced **outside Syzygy** (the project's own CI artifacts, a
     worker's retained gate artifact)", and that presupposes such runs are
     not doctrine violations;
  2. the owner typing a test command by hand. That is not an "agent
     session", so the owner's own hand is the only actor the exception
     excludes while the owner's agent is admitted;
  3. a worker the owner starts and leaves running, which D9 excludes by
     name ("one left running unattended");
  4. Syzygy's own operator tool, below.
- **Missed implementation.** `apps/three-surface-poc/src/capture-test-artifact-main.ts`
  (run as `npm run poc:capture-test-artifact`, `package.json` line 18) is
  Syzygy-authored code. Its `runCommand` calls
  `spawnSync(bin, [...rest, \`--junitxml=${artifactPath}\`], { cwd: repoRoot, … })`
  on a Butlers checkout: the real focused pytest suite, per
  `docs/THREE-SURFACE-POC.md` "Capturing test-run evidence". It passes no
  profile and inherits the caller's environment. That document says
  verification then renders `Verified` when the captured commit matches and
  the exit code is 0. Its sibling `capture-test-artifact.ts` is one of the 5
  files in the ledger's "Code and generators" lane, which the lane table
  routes to section 3.6. Section 3.6 has no row for code. Under block (a),
  "Syzygy itself, and any process Syzygy launches or schedules, still runs
  observed code only inside a profile". This tool is Syzygy code that
  launches observed code, so D9 either explicitly forbids it, or admits it
  only when an attended agent session invokes it. In that second case,
  condition 2 ("labelled Inferred, never Observed") conflicts with rendering
  `Verified` [Inferred: I did not establish which epistemic label the POC
  attaches to `Verified`]. The ledger states neither effect.
- The ledger's `AGENTS.md` 89 row says D9 "gives 'separate operator commands'
  a doctrine footing for the attended case". Operator commands typed by
  hand, and this Syzygy-authored capture command, are not "an agent session
  the owner starts and attends". The footing claimed does not exist for the
  commands that sentence actually describes.
- `AGENTS.md` itself instructs agent sessions in this repository to run
  Butlers' tests ("Butlers' pytest needs its own `.venv/bin/python`"). Under
  condition 1, whether a Syzygy repository instruction file is "Syzygy
  instructing" a session to run observed code is unaddressed.

Criterion 5 requires each citer's effect to be stated. The owner should
decide whether SEC-3 is meant to bind actors outside Syzygy at all (CI,
hand-run commands). The drafter's reading says it does, and the "one
exception" text would make that reading explicit. That is a larger normative
choice than the ruling asked for, and the packet does not put it to the
owner. Repair: state D9's effect on the capture tool and on CI-produced
evidence, and either scope the rule's actor or ask the owner.

**R4 [Observed] text, [Inferred] effect (revise; reported for the owner, not
resolved). Two accepted clauses that are not scoped to Syzygy's launches are
misstated as unchanged. Q3 frames only RFC5-18 and the reader map.**

- **RFC5-24** (`contracts/rfcs/RFC-0005/admission-and-boundary.md` from line
  354). It says the credentials Syzygy holds for typed adapters "are: … never
  visible to observed-project code." That limb is a clause, and it is not
  limited to profiles: the profile-specific prohibition is the separate
  "injection prohibition" sentence that follows it. D9's cost bullet concedes
  that observed code run by the attended session can reach "any Syzygy
  credential or endpoint on that host". On a host where Syzygy's adapter
  credentials are readable by the owner's user, D9 permits exactly the state
  RFC5-24 says never occurs. The ledger row says "unchanged for profiles" and
  routes the matter to the specification lane (section 5 item 3) as an
  optional operating step. Either RFC5-24's effect changes, or every
  attended session must run where no Syzygy-held credential is readable, and
  that would then be a condition D9 does not state.
- **RFC5-12** (`consent-egress-secrets.md` lines 108-109): "**Execution
  consent** — per project: the owner's approval Decision for a specific
  execution-profile version (RFC5-18). Absent: no observed code runs." The
  delta says "The owner's recorded choice is not an RFC5-12 execution consent
  and approves no profile". Under D9, then, observed code runs with no
  execution consent, which is literally what RFC5-12's "Absent:" limb rules
  out. The ledger row for RFC5-12 says "unchanged" and does not quote that
  limb. A reading confining RFC5-12 to consent given *to Syzygy* is available
  [Inferred]. Unlike RFC5-18's, though, it has no RFC5-19-style scoping
  sentence to rest on.
- Packet Q3 asks only whether RFC5-18 reaches the attended session, and says
  "A reviewer who finds that should report it to you". RFC5-18 is adequately
  scoped (N1). These two clauses are the ones a reviewer has to report: under
  D9, as drafted, they may change effect. Whether to accept that, amend
  RFC 0005, or add a D9 condition (for example, "no Syzygy-held credential is
  readable by the session") is the owner's decision. The packet must put it
  to the owner, as a Q3 arm or a new question.

## Notes

**N1 [Inferred] (note). Contract fit for RFC5-18 holds.** RFC5-19's last
bullet, "profiles govern only code Syzygy itself launches", scopes the gate.
So do RFC5-18(d), "the launching principal is authenticated and authorized",
and the non-normative diagram ("Code Syzygy itself launches" → "Profile
required (RFC5-18 gate)"). A Syzygy brief that a session started by the
owner may act on is not Syzygy launching, provided Syzygy does not start the
session. Whether the dossier mode (#353, not on `main`) starts the session
through any Syzygy command is [Unknown] at this commit. If it does, block
(a) itself excludes it ("A session Syzygy starts"). Three smaller points:

- The ledger's justification for `execution-profiles.md` 30-31 ("The map
  says 'If this map and a clause disagree, the clause wins'") is placed
  wrongly. Those lines sit in the module head, *above* that module's §0,
  "*If this section and a clause disagree, the clause wins.*" The README
  rule covers README 105-107 only. Both are still non-clause prose.
- The packet says "Two reader-map sentences". There is a third: README
  130-131, "**No observed-project code runs without an approved execution
  profile** (module 3, RFC5-18) — the owner's own repositories included."
- README 199-205 names the guarded failure mode as including "the test
  runner inheriting the host's SSH agent". D9 permits exactly that in the
  attended case. The ledger files README 196-208 under "citations".

**N2 [Observed] (note).** `execution-profiles.md` §4 case 7 ("the owner's
own repository running unprofiled 'because trust is assumed.'") appears in
no ledger row. D9 is distinguishable, because block (a) keeps the code
untrusted. The row should say so.

**N3 [Inferred] (note). CC-SEC-3 (packet Q2).** The preamble supports arm A.
It says "Where a sentence goes beyond what SEC-1…SEC-5 themselves require,
it is a Syzygy addition and says so", and the "tempting violation" sentence
carries no such marker, so it reads as a paraphrase that "Doctrine's text
prevails over" (line 21). The packet should tell the owner plainly that the
dossier brief (a Syzygy change, which CC-SEC-3 binds: "Every change must
exhibit…") is literally the case that sentence names: "'Run the project's
own test command to get better evidence' is exactly the tempting violation".

**N4 [Inferred] (note). "Attends" and "the owner's own host" are
undefined.** Cases the text does not settle:

- a process the session starts that outlives it (a daemonized
  `redis-server`);
- a subagent the attended session spawns;
- a remote VM the owner rents;
- a cloud-hosted agent session, which is not the owner's host.

Q4 recommends no glossary entry. At least the outliving-process case
deserves a sentence, because it is unattended observed code running on the
host after the attended session ends.

**N5 [Observed] (note). Condition 3 is narrower than the owner's words.**
Block (a) says "the commands the session reports having run are disclosed
with the claims they support". The ruling says "the run record lists the
commands the agent reports having run" (`…-RULINGS-DIRECTION.md` line 60),
without restriction. Under D9's wording, a reported command that supports no
rendered claim need not be disclosed. A specification can be stricter, but
the doctrine floor is lower than the ruling.

**N6 [Observed] (note). Ledger figures.**

- The section 1 figures reproduce exactly at `b60e6cd2`. At the reviewed
  commit they are 245 of 2,346, and decisions becomes 5 (the P-103 row).
  The packet's "240 files cite SEC-3" should name its commit.
- Section 1's "Second method" says it ran "over the same population", but
  it ran at `eacb85d1` (2,331 tracked paths; 248 hits reproduce there). The
  section 1 population is at `b60e6cd2` (2,346 paths; 249 hits there).
- Section 2 says the predicate "finds 57 line-cited references. All except
  the five `DIRECTIVE-REGISTER.md` rows…". Re-run at `b60e6cd2`, it finds 62
  matches in 28 files, 5 of them register rows, so 57 is the count *without*
  the register. The cited lines run from 10 to 59.

**N7 [Observed] (note). Quotation fidelity.** Every anchored quotation and
both clause quotations checked (RFC5-19, CC-SEC-3 line 21, the
review-1-rulings item 1 text, `AGENTS.md` 89, rulings line 61) match their
sources, whitespace-normalized. The packet's "the forbidden 'ambient
credentials for convenience' profile" is presented as a quotation but is not
one. The source is: credentials "for convenience."

**N8 [Inferred] (note). The violation sentence is a real distinction, and
the cost is stated plainly enough.** The named violation is false
containment: a profile that looks contained and is not. The attended session
claims none. The credential exposure is the same in both, though. The packet
says so ("The credential exposure is real either way"), but the doctrine
text says it only indirectly, through the cost bullet. Placing one clause in
the violation bullet, such as "the ambient-credential exposure is the same;
what differs is that nothing claims otherwise", would keep a reader of SEC-3
alone from taking the distinction as a mitigation. Subject to R1.

**N9 [Inferred] (note). Clause (b).** `v1.md` line 119 sits under "Platform
and audience" and describes Syzygy's platform, so it remains true of Syzygy
without (b). The case for (b) is that it stops a reader taking the line as
universal. A cost is that (b) puts a non-Syzygy execution path inside a list
describing Syzygy's platform. Optional either way. Packet arm B is a fair
offering.

**N10 [Observed] (note). Change class.** "Normative" is correct per
`SEMANTIC-DELTA-TEMPLATE.md` line 103 ("An obligation is added, removed,
narrowed, or widened"). The amendment both narrows a prohibition and adds
obligations, namely the two new violations. "Widened" describes the
permission, not the obligations. The delta's own explanation makes that
clear.

**N11 [Observed] (note).** The retained bullet "**The profile contract is a
blocking RFC:** no observed-project code runs until it is accepted." stays
unscoped beside the exception. Since RFC 0005 is accepted, this is moot.

**N12 [Inferred] (note). Readability for the owner.** The packet is plain
and can be decided without the delta, and its section 1 preserves the three
options and the owner's choice faithfully (criterion 4 is met in both the
packet and block (a)). What the owner cannot learn from the packet:

- R3: the capture tool, CI, and hand-typed commands;
- R4: RFC5-24 and RFC5-12;
- that arm A is wider than the ruling (R2).

Each of these bears on the owner's decision.
