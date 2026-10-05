# Review R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-3
Reviewed commit: b5ff7a3bf22dc6144e6d0161a2add410e8355a5c
Manifest SHA-256: b39d103263d6667e8ab5e10abec70fc0a53ed9a22fad00e4bc7532f1ce18c40e
Verdict: CONFIRM WITH EXCEPTIONS

Reviewer: fresh-context reviewer (CC-REV-1), dispatched by the lead for round
3, the confirming round. I did not author the change or share its session.
I read only git objects: the package at the reviewed commit (the subject
`proposed/polaris-generation/spec.md`, `proposal.md`, `design.md`, `tasks.md`,
`GOVERNING-DEPENDENCIES.md`, and in the candidate package `SEMANTIC-DELTA.md`,
`IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`, `REVIEW-BRIEF.md`); the six
`POLARIS-DOSSIER-LOCAL-AGENT-*-DIRECTION.md` records on origin/main; the
round-1 and round-2 raws on origin/main; D9's package at
`62c29093935c9370efe030d1a3a54672f50dbd72` (`SEMANTIC-DELTA.md` "Proposed
meaning" arm A, its packet and its round-2 dispositions); the base and
overlay specs and the base change's design files; RFC5-24, RFC5-18 and RFC7-20
at their defining clauses; `AGENTS.md`. No PR conversation, transcript,
drafting message or target-repository content was read. Network: `git fetch
origin`, `gh pr view 353` and `gh pr view 357` only.

[Observed] `gh pr view 353` reports head `b5ff7a3bf22dc6144e6d0161a2add410e8355a5c`,
draft, open; `gh pr view 357` reports head `62c29093935c9370efe030d1a3a54672f50dbd72`.
Subject digest: [Observed] `git show b5ff7a3b…:openspec/changes/polaris-dossier-local-agent-mode/proposed/polaris-generation/spec.md | sha256sum`.
[Observed] The base change, the overlay change, `.syzygy/governance/doctrine/`
and `.syzygy/governance/contracts/rfcs/` have identical tree ids at the
reviewed commit and at origin/main (`5126610b`), so every quotation check
below holds against both.

Paths are relative to the repository root. "spec" is the subject; "packet",
"delta", "design", "proposal", "ledger" are the package files of those names;
"D9" is D9 arm A at `62c29093`. Every quotation below was re-extracted by
Python substring match against the file at the commit named
(whitespace-normalised for hard-wrapped prose).

## Criterion results in brief

| # | Criterion | Result |
|---|---|---|
| 1 | Does what the directions authorize, no more | Yes [Observed]: no read, egress, write or execution is granted to Syzygy; provider mode parked, not withdrawn; no adoption language; sign-off gated on D9 (spec:3, packet:109-111, proposal:15-19, tasks:15-20) |
| 2 | Quotations exact | Yes [Observed]: 31 of 31 "Current meaning" blocks found byte-exact in their named files (base 17 including 3 also in the overlay, overlay 7 plus the 3 shared 006 blocks, `INTERFACES.md` 2, `SECURITY-CONTRACT.md` 1, `security.md` 1, `execution-record.md` 1, `narrative-contract.md` 1); all 29 double-quoted fragments of 12 or more characters in spec lines 11, 29, 203, 297 and 370 found in their named files; the `OWNER-FLOW.md` headings "Resolve warranted work" and "Materialize once, then execute" exist. The four requirement statements in the delta's "Proposed meaning" equal the spec's paragraph for paragraph (11, 7, 4, 3) |
| 3 | Displacement complete and bounded | Yes for the adopted requirements. Notes: `SOURCE-POLICY.md`'s execution-consent sentence (Finding 7); RFC5-12 and RFC5-24 not named (Finding 6). Nothing displaced for the provider mode |
| 4 | Contract or doctrine changed in effect | RFC7-20: my finding below (Finding 10), for the owner; three conditions applied exactly. SEC-2: 033 states the consent-record sentence and the (a)/(b) disclosures plainly; the four-condition predicate matches 032 and is stricter on `.syzygy/` (Finding 9 on a residue). SEC-3: nothing in spec, design or harness texts tells an agent to run observed code outside a profile while D9 is not in force; sign-off waits for D9 |
| 4a | Review independence as ruled | Yes. The frozen inventory read as part of "the criteria" is a faithful reading of the owner's purpose (006 measures coverage against it) and is flagged in the delta; the `!` form is shown to the owner as the lead's reading (packet O4, proposal:151-154) |
| 5 | Every Observed claim observable | Yes. Remaining Inferred-side gaps are in Findings 2, 4 and 8 |
| 6 | Scenarios falsifiable | Yes; minor falsifier gaps in Finding 2 |
| 7 | Change class | Normative is right |
| 8 | Impact ledger reproducible | Yes [Observed], every figure reproduced (below) |
| 9 | Rulings applied exactly; D9 carried | Rulings: yes, none widened or narrowed; open items are only D9's adoption and the v1.0 sign-off; carried findings named (round 1: 6-8; round 2: 4, 5, 7, 8). R1 applied without qualifier. D9: every arm A condition is carried, none widened (table below); the credential condition is carried as checks rather than as a keeping obligation (Finding 1) |
| 10 | `design.md` stays design | Yes, no code; skill and Codex texts are prose; consistency notes in Finding 9 |

## Round-2 findings: does the repair hold?

| R2 # | Repair | Holds? |
|---|---|---|
| 1 | spec:13 "At every later check, review check and render, Syzygy SHALL verify again that the recorded pinned revision is a revision the in-force observation consent names, and SHALL refuse the step otherwise"; brief, draft, inventory and packets name it; scenario "Recorded revision altered" (spec:47-51); falsifier arm (spec:186) | Yes |
| 2 | spec:295 Observed only "the packet Syzygy built and rebuilt from the frozen subject, its digest, and that the verdict names that digest"; Inferred "that the review context read the packet Syzygy emitted, unaltered"; packet carries its own digest (spec:291); design decision 5 (design:143-150) | Yes |
| 3 | spec:25 "Syzygy SHALL NOT rest an Observed label on a record it stored."; open list ("including the repair-cycle count, …"); R1 cited in 033 and its warrants, 034's warrants, packet, delta, proposal, design, tasks | Yes. R1 items 1-3 applied without qualifier |
| 4 | packet O4 row and plain-terms summary (packet:62-66, 103); proposal:151-154; delta | Yes. The facts the owner should see are stated |
| 5 | packet:133-141 carries the 020 reading and option A's fuller cost to the sign-off; delta and design say R1 does not cover 020 | Yes, stated fairly |
| 6 | spec:366 "the set of Git objects that the render itself reads and verifies … which objects Syzygy read in earlier steps comes from a stored record and, where shown, is labelled Inferred"; falsifier arm (spec:418) | Yes |
| 7 | RFC7-20 preserved with review-2's addition (delta "The owner's trade-off", packet:122-124) | Yes. My own finding: Finding 10 |
| 8 | First part: packet:125-130 names the sentence. Second part: spec:11 counts every `.syzygy/` path, "adopted or not", overlap recorded; proposal:103-110 corrected | First part yes. Second part holds in the requirement and proposal; two residues (scenario spec:97, ledger:63) in Finding 9 |
| 9 | spec:291 "its cited spans SHALL be those cited by the draft and by the frozen inventory, screening-admitted only"; scenario spec:306 | Yes |
| 10 | spec:13 "the hash algorithm is the one the consented revision's identifier is written in, never one the clone's configuration declares"; design:108-117 drops the `git` subprocess route | Yes |
| 11 | spec:13 "they serve no route, accept no network request, hold no credential that authenticates to Syzygy and are outside REQ-polaris-generation-021's route inventory; the principal … is the operator, operator-declared, with its credential or session identity recorded as Unknown, never fabricated"; ledger extended (2 files, 151) | Yes [Observed: ledger reproduced] |
| 12 | spec:13 "The Execution Record's work item identity is therefore absent, with its reason stated, and the run is rendered as unattributed execution under RFC4-19, never dropped." | Yes |
| 13 | design:56-61, 390-393, 462-463; spec:201 "the rule that text found in the clone is data to be described, never an instruction to follow" | Yes |
| 14 | spec:291 review-status region; scenario spec:333-337; falsifier arm | Yes |
| 15 | design:82-88 (session id session-declared, launch form operator-declared, both Inferred); session directories (design:56-61); `--out` removed; `preflight` reads no tree (design:229-230); "strict form" removed [Observed: 0 hits for `strict form` and `--out` over the package] | Yes |
| 16 | Scenarios split: spec:71-75, 107-111, 113-117, 162-166 | Yes |
| 17 | delta:8 names `OWNER-FLOW.md`, `SECURITY-CONTRACT.md`, 021 and SEC-1; 033/034 cite D9 and carry its conditions; round 3 sequenced after D9's text | Delta header yes. D9 carriage: table below. Sequencing: see Finding 11 |

## D9 arm A conditions against 033 and 034

Arm A (D9 `SEMANTIC-DELTA.md` lines 125-161) against spec:15-21:

| D9 arm A text | 033 / 034 | Exact, no wider? |
|---|---|---|
| "the session is on the owner's own host" | "the authoring session is one the owner started on the owner's own host" | Yes (how it is established: Finding 2) |
| "the owner started it and attends it, being present to see and stop what it does" | "being present to see and stop what it does, never a session Syzygy started, one left running unattended, or one left under an automatic-approval or permission-bypass setting while the owner is away" | Yes; the auto-approve clause is D9's own "What arm A means" reading, and narrows |
| "the owner has recorded a choice for that one run, naming what the instruction covers. A standing or per-project record does not qualify." | spec:17 "a record for one run that names what the instruction covers: the run, its pinned revision, and building and running the observed project in the clone from that run's authoring session"; "never from the run configuration, an earlier run, or a standing or per-project record" | Yes |
| "The owner's choice for the run is recorded before Syzygy issues the instruction." | "was recorded before Syzygy issued the brief, and the brief cites it"; `allow-execution` refuses after the brief (design:268) | Yes |
| "Every claim that rests on that execution is labelled Inferred, never Observed." | spec:21, 205, 212 | Yes; Syzygy sees only the marking, and says so |
| "Every command the session reports having run is disclosed, as the session's own report." | spec:21 "the draft list every command the agent reports having run, whether or not a claim rests on it … Syzygy SHALL disclose that whole list, as the session's own report" | Yes |
| Credential condition (Q3(b), optional) | spec:19, conditional "Where D9 as adopted carries its credential condition" | Carried as checks; see Finding 1 |
| "Syzygy never gives the instruction to a session it started or to one left running unattended, and never asks for a process that outlives the session. Work the session hands to its own subagents is part of the session." | spec:15 | Yes, and narrower: only the authoring brief may carry the permission, with a lapse statement and a stop-every-process requirement |
| The cost bullet | spec:21 "the cost D9 states" | Abridged; Finding 3 |
| Violations: "Syzygy instructing a session to run observed code before the owner's choice for that run is recorded, or on a standing record; a claim that rests on the session's execution rendered Observed." | spec:17 "Syzygy SHALL NOT instruct a session to run observed code before the owner's choice for that run is recorded, or on a standing record"; Inferred labelling | Yes |

[Observed] Nothing in 033 or 034 is wider than arm A. D9's round-2 direction
(`POLARIS-DOSSIER-LOCAL-AGENT-D9-ROUND-2-2026-10-06`, item 1) widens D9 to
"any Syzygy instruction, in any feature"; 033 uses only the dossier
authoring brief, which is narrower, as it may be.

### The three points D9 leaves to the spec, judged as drafter choices

- **Who records the per-run choice** (`syzygy dossier allow-execution`, typed
  by the operator in a new terminal or behind `!`). Sound in shape: per run
  and per revision, never a configuration value, refused after the brief,
  and its authorship honestly Inferred. Its weakness is that the agent the
  safeguard governs can operate it: the agent drives `init` and `brief`
  (design:37, 40) and could run the command, or write the record, itself;
  only the skill text forbids it. The packet's "Syzygy cannot see who typed
  it" is true but does not tell the owner that. Finding 4.
- **Which session may carry the permission and when it lapses** (authoring
  brief only; lapses if the owner stops attending, including under
  auto-approve or bypass while away). Sound and narrower than D9. The
  declaration on which the brief decides "attends", "own host" and "the
  owner started it" is not specified anywhere. Finding 2.
- **The OS-level credential readability check.** Right in kind (a real read
  as the operator's user; a tool's deny rule does not pass). Narrower than
  D9's obligation in four ways. Finding 1.

## Criterion 8: impact ledger reproduced

[Observed] Re-ran sweeps A, B, E, F, G and I exactly as published, by Python
`re`, over `git ls-tree -r -z --name-only ac35c998ec3f7b20c47adc19b22ac540f851b099`:
2,328 paths, 4 not UTF-8, 2,324 searched. Files per identifier: 001 48,
005 26, 006 52, 017 39, 018 17, 030 25, 031 19; A to G 104; I alone 31; 135
in all. Extension: 002 50, 003 33, 020 31, 022 15; union 63; 14 new (the 14
paths fall 3 raws, 4 evidence, 3 adopted, 1 sibling candidate, 1 script, 1
design history, 1 live doc, matching the ledger's classes); 149 in all. 021:
18 files, 2 new (`docs/reviews/R-POLARIS-GENERATOR-AUTHORITY-PAIRING-CONFIRMATION-2026-09-12-RAW.md`,
`openspec/changes/polaris-manifesto-generation/EFFECT-HOST-DESIGN.md`); 151
in all. The RFC7-20 regex returns 64 files. Every published figure matches.
I did not re-derive the 135-file path-rule classes beyond the 14 and the 2.

## Findings

**Finding 1 — The credential condition is carried as instant checks, not as D9's keeping obligation, and the checks miss part of the run** (note)

D9 (the conditions list): "Syzygy keeps every credential it holds for its
typed adapters where neither the session nor any process it starts, directly
or not, can read it at the operating-system level, for as long as any of
them runs." The owner's D9 round-2 direction, item 2: "The credential
condition reaches every process the session starts, for as long as any of
them runs."

spec:19: "Syzygy SHALL, before it issues a brief that permits execution, at
every later check and at close, attempt as the operator's user to read every
credential that Syzygy's configuration holds for its typed adapters."

[Inferred] Four gaps between the obligation and the check:

- **Which steps.** spec:13 distinguishes "every later check, review check and
  render", so "every later check" in spec:19 reads as `check` only
  (design:198-199 agrees: "repeated at every `check` and at `close`"). After
  the last clean `check`, the inventory, both reviews and the render
  (design steps 9-12) pass with no credential read, while the permitted
  session, and any server it started, may still be running.
- **After close.** D9's obligation lasts "for as long as any of them runs";
  the last read is at `close`. The agent's stopping of its processes is its
  own report (spec:15). Nothing in 033 obliges Syzygy not to make a
  credential readable after close.
- **No keeping obligation.** 033 only detects ("SHALL report the breach as a
  finding"); it never says Syzygy SHALL hold its typed-adapter credentials
  where the operator's user cannot read them while a permitting brief is in
  effect. D9 places the obligation on Syzygy as a whole, so another Syzygy
  component writing a readable credential mid-run is a D9 breach the spec
  frames only as a finding.
- **What is checked.** "every credential that Syzygy's configuration holds"
  is narrower than D9's "every credential it holds for its typed adapters"
  (a credential held outside the configuration, such as in a keyring or an
  environment, is not named), and the list is drawn from a configuration
  that on a single-user host is within the agent's, and observed code's,
  write reach: removing an entry makes the check pass. Separately, the read
  is attempted "as the operator's user" only; on a host where that user can
  escalate without a password, a process the session starts can read a
  credential that a plain read as the user cannot. The spec's disclosure,
  "by another route is Inferred and disclosed", covers this honestly, but
  the brief is then issued while D9's condition is false.

Proposed fix (only if the owner adopts D9's Q3(b)): run the read at every
step Syzygy takes after a permitting brief (`check`, `inventory-check`,
`review-check`, `render`, `close`); add "Syzygy SHALL NOT, from the issue of
a permitting brief, hold or write a typed-adapter credential where the
operator's user can read it"; take the credential list from a source the
disclosure names, and disclose that it is within reach; and either probe
password-less escalation or disclose it by name, and disclose that
readability after close is Inferred.

**Finding 2 — Three conditions of the permitted case have no stated source of declaration** (note)

spec:15 makes the permitting brief depend on: "the operator is the owner, and
the authoring session is one the owner started on the owner's own host and
attends". Of these, the spec says how two are known: "that the operator is
the owner: both rest on the operator's declaration" (spec:17), and "whether
the owner attended is the operator's declaration, labelled Inferred"
(spec:15). It names no source for "on the owner's own host" or "the owner
started" the authoring session, and does not say when or how the attendance
declaration is made. The run configuration carries `operatorIsOwner`
(design:290) and nothing for attendance, host or who started the session;
no command records them; and spec:25's Inferred list omits them.
[Inferred] Two implementers diverge: one issues the permitting brief on
`operatorIsOwner` plus the `allow-execution` record, one requires an
explicit attendance and host declaration. Falsifier gaps: spec:186 has no arm
for a permitting brief issued while attendance or host is undeclared, nor
for a permitting brief that omits the lapse statement (that is checked only
in the scenario at spec:129).

Proposed fix: name the declaration (for example, `allow-execution` records
that the owner started and attends the authoring session on the owner's
own host, operator-declared), add those values to spec:25's Inferred list
and to the disclosure, and add the two falsifier arms.

**Finding 3 — "The cost D9 states" is recorded abridged** (note)

D9: "the session runs with the owner's own credentials and network,
including Syzygy's endpoints and any Syzygy credential readable on that
host. Observed code it runs can reach them, and can change any file the
owner can, the clone it runs in included. Nothing contains it, so it gives
none of a profile's guarantees."

spec:21: "the cost D9 states: the session runs with the owner's own
credentials and network, including Syzygy's endpoints and any Syzygy
credential readable on that host, and observed code it runs can change any
file the owner can, the clone included." It drops "Observed code it runs can
reach them" and "Nothing contains it, so it gives none of a profile's
guarantees", the two parts that say what the exposure means. design:201-204
repeats the abridgement. Fix: have the run record carry D9's cost bullet as
adopted, quoted, rather than a restatement.

**Finding 4 — The per-run choice can be entered by the agent it governs; the packet says only that Syzygy cannot see who typed it** (note, for the owner's view)

spec:17: "The skill and agent texts SHALL tell the agent never to run that
command. Syzygy cannot observe who ran the command, or that the operator is
the owner". packet:44-47: "you typed the per-run choice yourself
(`syzygy dossier allow-execution`) before the brief … Syzygy cannot see who
typed it, so it shows that the choice was yours as Inferred."

[Inferred] The authoring agent runs `init` and `brief` (design:37, 40), so
it can also run `allow-execution` before `brief`, or write the choice record
into the state directory; an instruction is the only barrier. D9's whole
safeguard for arm A is the owner's per-run choice, so the owner should read
plainly that the agent can produce it. This is an honest design under R1,
and D9 leaves the mechanism to the spec; it is not revise-level.

Proposed fix: one sentence in the packet's "Running the project" bullet and
O3 row: the agent itself could run the command or write its record, which
Syzygy cannot tell apart. Optional strengthening for design: have
`allow-execution` require a typed confirmation from the controlling terminal
that shows the run, the revision and D9's cost [Inferred: agent tool shell
calls commonly have no controlling terminal; whether a `!` launch has one is
Unknown, so this may exclude the `!` form for this command].

**Finding 5 — "Quote SEC-3's rule" will not read as a prohibition once D9 is adopted** (note)

spec:15: "Otherwise the brief SHALL quote SEC-3's rule that observed-project
code runs only inside an explicit, opt-in execution profile". spec:201 and
the scenario at spec:122 say the same. That restates today's SEC-3 head
("Observed-project code runs only inside an explicit, opt-in execution
profile."). D9 arm A replaces it with "Syzygy runs observed-project code only
inside an explicit, opt-in execution profile." Once D9 is in force, every
non-permitting brief falls under "Otherwise" and quotes a sentence whose
subject is Syzygy, not the agent; an implementer must choose between the
adopted text (which does not tell the agent anything) and the spec's
paraphrase (which is no longer a quotation). Fix: the brief states the rule
in its own words ("do not build or run the observed project outside an
explicit, opt-in execution profile") and cites SEC-3, as the skill text
already does (design:380-382).

**Finding 6 — RFC5-12 and RFC5-24 change in effect in the permitted case; this package does not say so** (note)

RFC5-24 (`.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:354):
adapter credentials are "never visible to observed-project code." D9's
packet Q3 states: "RFC5-12 ("Absent: no observed code runs") and RFC5-24
("never visible to observed-project code") change in effect in the
permitted case", with (b) as the remedy for RFC5-24. [Observed] `RFC5-24`
and `RFC5-12` appear in no file of this package. 033 makes the credential
check conditional on D9 carrying it, so if the owner adopts D9 without
Q3(b), 033's permitting brief issues on a host where RFC5-24 may be false,
and the run record's cost sentence names "any Syzygy credential readable on
that host". The decision is D9's and the owner's; this package should name
the dependency so the sign-off is taken in view of it. Fix: one line in the
delta's "What explicitly does NOT change" (or the packet's carried items):
without Q3(b), RFC5-24's limb is untrue for this mode's permitted case, as
D9 discloses.

**Finding 7 — `SOURCE-POLICY.md`'s execution-consent sentence is neither read nor distinguished** (note)

`openspec/changes/polaris-manifesto-generation/SOURCE-POLICY.md`: "Execution
consent is per project for an exact approved execution-profile version." The
per-run choice of spec:17 is an execution permission that is not per
project and names no profile. [Inferred] It is not an "execution consent" in
that sense (it is D9's "choice"), but nothing says so, and an implementer
building the consent reader may file it as one. Fix: one sentence in 033 or
design decision 8 that the per-run choice is not an execution consent
(RFC5-12) and approves no profile.

**Finding 8 — Records Syzygy reads, not only those it stores, are within the agent's write reach** (note, for the owner)

R1 covers "Syzygy's own records". The gates of spec:13 and spec:15 also read
"the in-force observation consent", the registry entry, the policy acts,
the per-project statement, whether D9 is in force (design:264, `preflight`)
and whether the RFC7-20 ruling is effective. [Inferred] On a single-user
host those records live in a governed tree or state the operator's user can
write, so the authoring agent, and in the permitted case any observed code
it runs ("can change any file the owner can"), can alter them, and with them
whether Syzygy reads, whether a statement is required and whether execution
is invited. Quotation fidelity is unaffected (it rests on re-hashed objects
of the clone). The spec cites RFC3-16 in 033's warrants but does not say
that "in force" is established by the act cross-check, nor disclose that
the gate inputs are within reach. Fix: say how "in force" is established
(RFC3-16(a)), and add to the disclosure that the consent, statement and
act records Syzygy read are within the sessions' write reach; or carry it
to the owner with R1's costs.

**Finding 9 — Residues of the round-2 repairs** (note)

- spec:97, scenario "Governed subject without a per-project provider
  statement": "an adopted capability declaration". The requirement (spec:11)
  now counts "every path under a `.syzygy/` governance tree … adopted or
  not", and the round-2 repair exists because a path listing cannot decide
  "adopted". The scenario reintroduces the undecidable word. Fix: "a
  capability declaration or any `.syzygy/` path".
- ledger:62-64: "No overlap: 032 says how a non-governed narrative is
  composed". The proposal (proposal:106-110) and spec:11 now record the
  governed predicate as an overlap. Fix: align the ledger.
- delta:528-529: the second review is "retained by the lead"; it is on
  origin/main at `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-2-RAW.md`.
- proposal:60-64, "Modified in effect" lists 001, 002, 005, 006, 017, 018,
  020, 022, 030, 031 and `INTERFACES.md`, but not 021, `OWNER-FLOW.md` or
  `SECURITY-CONTRACT.md`, which delta:8 names after the round-2 repair.
- design:367, skill description: "for a public repository"; the owner chose
  "Any repo". Harmless, but the skill's trigger text is narrower than the
  mode.
- packet:48-50: "before the brief and at every check"; spec:19 also checks
  at close.

**Finding 10 — RFC7-20: my finding on the owner's reading** (note: reported for the owner, not resolved)

RFC7-20 (`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`):
"Computing a draft is inference: absent SEC-2 named-provider consent it is
**not computed**". The ruling (`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`,
item 1) reads the condition as governing "drafts that Syzygy computes".
[Inferred] I agree with rounds 1 and 2: the clause names no computing party,
so for an operator-computed draft the reading changes the clause's effect
rather than applying its text, and under 033 as written it does work only
for non-governed subjects. The packet states this fairly (packet:100,
122-124). Application check: spec:29 admits an operator-computed draft
"only when all three of that ruling's conditions hold" (disclosure;
declared and recorded tool and provider; byte-verified quotations), which
are the ruling's three; the added fallbacks narrow only. Applied exactly.

SEC-2 "scoped" (review-1 rulings, item 2): spec:11 states plainly that "The
statement is a consent record" and that "Neither the content classes the
statement names nor the observing project's classification and screening
policies (SEC-5) bind the agent sessions' own reads or sends". Whether an
unenforced class limit is SEC-2's "scoped" consent is the owner's; the
packet names the deciding sentence (packet:125-130). Reported, not resolved.

**Finding 11 — This confirmation is bound to D9 at `62c29093`, whose own round 3 is not retained** (note)

The brief says round 3 is "dispatched by the lead after D9's text is fixed
by its own review". [Observed] `docs/reviews/` on origin/main holds D9's
rounds 1 and 2 only, and PR #357's head is still `62c29093`. 033 and 034
enumerate arm A's conditions as frozen there. If D9's round 3 or the
owner's adoption changes arm A's conditions (or the owner adopts arm W, whose
term is "exception", not "permitted case"), 033 and 034 must be re-aligned,
and under verification rule 10 that retires this review. The lead should
re-check spec:15-21 against D9's adopted text before the sign-off offering.

## Blocking findings

None. Findings 1 to 11 are notes. Findings 4, 6 and 8 (in part) and 10 are
for the owner's view at sign-off.
