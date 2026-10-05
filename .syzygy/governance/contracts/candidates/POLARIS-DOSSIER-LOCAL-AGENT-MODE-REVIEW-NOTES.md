# Polaris dossier local-agent mode — round-3 review notes and how to sign off

> **Candidate — binds nothing.** This is the sibling record for the notes of
> the third fresh-context review of the `polaris-dossier-local-agent-mode`
> amendment (draft PR #353). Under the owner's notes-only rule
> (`../../decisions/POLARIS-GATE-SITTING-2026-09-26-DECISION.md` §1), a round
> with no revise-level finding clears the exact bytes it read, and its notes
> go in a sibling record, never into the reviewed bytes. So this file sits
> outside the package directory and edits nothing in it. It signs nothing
> off: only the owner's own selection does that (VIS-4). The sign-off is
> version-tagged and binds no act digest, so nothing here is registered in
> `check_governance.py`.

Reviewed record: docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-3-RAW.md

## What was confirmed

- **Package:** the change directory openspec/changes/polaris-dossier-local-agent-mode/
  and the candidate package
  .syzygy/governance/contracts/candidates/polaris-dossier-local-agent-mode/,
  both on draft PR #353 and neither on `main` yet, which is why neither is
  written as a code span here.
- **Reviewed commit:** `b5ff7a3bf22dc6144e6d0161a2add410e8355a5c`, which is
  PR #353's head [Observed, `gh pr view 353`, 2026-10-06].
- **Subject:** `proposed/polaris-generation/spec.md` in the change
  directory, sha256
  `b39d103263d6667e8ab5e10abec70fc0a53ed9a22fad00e4bc7532f1ce18c40e`, 45
  scenarios [Observed: `git show b5ff7a3b:<path> | sha256sum`, and a count of
  `#### Scenario` lines, both re-run for this record].
- **Verdict:** `CONFIRM WITH EXCEPTIONS`, on line 4 of the raw named on the
  `Reviewed record:` line above. The raw's "## Blocking findings" section
  reads "None. Findings 1 to 11 are notes." [Observed: the raw opens 11
  findings, numbered 1 to 11, each tagged as a note.]
- Rounds 1 and 2 returned `REVISE`, over `f1bd0b5c` and `af97611d`. Their
  dispositions are in the package's `REVIEW-BRIEF.md`; their raws are on
  `main` as `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1-RAW.md` and
  `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-2-RAW.md`.
- **D9, the dependency:** the review bound 033 and 034 to D9 arm A at
  `62c29093935c9370efe030d1a3a54672f50dbd72`. D9's own round 3 returned
  `CONFIRM WITH EXCEPTIONS` over that same commit
  (`docs/reviews/R-DOCTRINE-AMENDMENT-D9-3-RAW.md:4`), with its notes in
  `DOCTRINE-AMENDMENT-D9-REVIEW-NOTES.md` beside this file. D9 is not
  adopted.

Every claim re-checked for this record is marked [Observed]. Each
recommendation is the drafter's [Inferred].

## How to sign off

**Sign-off waits on D9.** The amendment may not be signed until you have
adopted D9 by your own act (`../../decisions/POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md`,
item 1). Adopt D9 first, as `DOCTRINE-AMENDMENT-D9-REVIEW-NOTES.md`
describes.

**Then, before the offering, the lead checks D9's adopted text against
033 and 034** (round-3 finding 11, below). If you adopt arm A as reviewed,
with or without Q3(b), the confirmed bytes need no change: 033 applies its
credential check only "where D9 as adopted carries its credential
condition". If the adopted text differs in any other way, 033 and 034 are
re-aligned, that edit retires this confirmation (verification rule 10), and a
new round runs before anything is offered.

**The words.** The sign-off is an option selection, not a typed phrase
(`../../decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`,
item 1; the scope and review direction's "Option pick, v1.0",
`../../decisions/POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`,
item 3). You will be offered one structured question, and you select this
option, as the package's own `OWNER-DECISION-PACKET.md` words it:

> Sign off `polaris-dossier-local-agent-mode` v1.0, and extend version-tag
> sign-off (`OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`) to
> Polaris generator specification deltas.

The question will also put each item in "What the sign-off decides" below
to you; a sign-off is taken with them in view. The second half of the
option, the extension, takes effect only through that selection; the scope
direction does not extend Scope A by itself.

**What the recording commit does.** It runs
`scripts/record_versioned_signoff.py --record polaris-dossier-local-agent-mode
--version 1.0 --date <date> --review docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-3-RAW.md
--disposition .syzygy/governance/contracts/candidates/POLARIS-DOSSIER-LOCAL-AGENT-MODE-REVIEW-NOTES.md
--owner-selection-quote "<the question and the option you selected>"`.
Before it writes anything, the recorder:

- reads the raw's first four non-blank lines: the reviewed commit, the
  subject digest (as information only) and the verdict;
- requires every finding to be a note, and this record to name the raw on
  its `Reviewed record:` line and to carry exactly the raw's finding numbers
  (here, the `### <n> —` headings 1 to 11);
- requires the candidate package at the working tree to equal the package at
  the reviewed commit, and the package's own builder check to pass.

It then applies the package through its builder, which moves the four
requirements from the change's `proposed/` directory into `specs/` and
regenerates the effective-scenario recount, writes the record
POLARIS-DOSSIER-LOCAL-AGENT-MODE-SIGNOFF-v1.0.md in `../../decisions/` (not
written as a path until it exists), appends
one block to `../../decisions/ACCEPTANCE-ACT-RECORD.md`, and prints the tag.

**Then, in the same commit, the reconciliation is re-derived.** Run
`python3 scripts/check_spec_reconciliation.py --regenerate`. It writes two
generated files, and no signed subject:

- the change's `GOVERNING-DEPENDENCIES.md`, which replaces the hand-held
  union as `tasks.md` asks;
- the reconciliation census, `census.json`.

It refuses while an installed Polaris addition has no sign-off record. Three
hand edits remain, because no script writes prose routes or the battery:

- name the new record on the change's row in `openspec/README.md`, whose
  status cell still says candidate;
- name it beside the Polaris composition figure in `PROJECT-STATUS.md`;
- add the recorder's `--check polaris-dossier-local-agent-mode --version 1.0`
  line to the battery, the hosted workflow and the count sentence, together
  (CG-26).

The reconciliation's R5 fails until both routes cite the record. The
canonical battery then runs clean [Inferred: from a scratch-clone dry run
that recorded nothing real].

**What it binds.** The git tag `polaris-dossier-local-agent-mode-v1.0`, on
the commit that carries the package bytes you were shown, which must equal
the bytes this review read. No phrase and no digest argument. A later edit is
v1.1 and needs its own review; it does not retire v1.0. The recorded
extension then lets later Polaris generator deltas (the narrative profile
among them) be signed the same way.

**Three things the recording commit needs that do not exist yet** [Observed
on `main` at `4ab58f24`]:

- PR #353 merged to `main` with its reviewed bytes unchanged.
- A builder module for this package and its entry in the recorder's
  `real_packages()`. The packet calls the builder post-sign-off work; it
  must exist before the record is written, but not before you select.
- **A recorder fix.** The recorder reads each finding's severity with a
  pattern that accepts only a bare `(note)`. Three of this raw's findings
  are tagged `(note, for the owner's view)`, `(note, for the owner)` and
  `(note: reported for the owner, not resolved)` (findings 4, 8 and 10).
  [Observed: run against the raw, the recorder's `SEVERITY_RE` matches
  findings 1, 2, 3, 5, 6, 7, 9 and 11 only.] The raw cannot be edited
  (CC-REV-6), so as written the recorder refuses with "review findings
  [4, 8, 10] carry no (blocking|revise|note) severity". The fix is to accept
  a qualifier after the severity word, with a selftest fixture for each
  form. That is a change to `scripts/`, which is outside this record.

## What the sign-off decides

These were reported for you, and neither the drafter nor the lead resolves
them. Each has a recommendation. Accepting a recommendation changes no byte.
Choosing otherwise is a change to the package, and so a new version and a new
review round, before or after v1.0.

| Finding | In plain terms | Recommendation |
|---|---|---|
| Round 1, finding 6; round 2, finding 7; round 3, finding 10 (first part) | **RFC7-20.** The contract says a draft is "**not computed**" without named-provider consent, and names no computing party. Your ruling reads that as covering only drafts Syzygy computes, so a draft your own agent session computes is admitted (with disclosure, the declared tool and provider, and byte-verified quotes). All three reviewers agree that this changes what the clause does, rather than applying it. Under 033 the reading matters only for non-governed projects, because a governed one already needs your per-project statement | Keep the ruling, which round 3 found "Applied exactly", and accept knowingly that it changes the clause's effect for operator-computed drafts. If the contract should say so itself, queue an RFC 0007 amendment naming the computing party; it does not block v1.0 |
| Round 1, finding 7; round 2, finding 8 (first part); round 3, finding 10 (second part) | **SEC-2 "scoped" and SEC-5.** For a governed project, 033 makes your per-project statement the "explicit, recorded, per-project consent" SEC-2 asks for. But SEC-2's head says "explicit, scoped consent", and nothing can stop your agent reading or sending more than the classes the statement names; SEC-5's screening does not bind it either. 033 says this plainly. The deciding sentence is 033's "The statement is a consent record" | Accept, consistent with your "Any repo" and "Keep any repo, disclose" choices: the statement is consent, and the unenforced class limit is disclosed, not hidden. If you want SEC-2's "scoped" to mean enforced, choose the option you declined after review 1, "Public repos for now"; that is a new version |
| Round 1, finding 8 | **SEC-3.** Letting your agent build and run the project needs a doctrine change | Answered by D9. Adopt D9 before you sign; this item then closes |
| Round 2, finding 4 | **The `!` launch form.** Admitting a review session that you start by typing `!` in the authoring session's terminal is the lead's reading of your words "A second top-level Claude Code/Codex session you start", not your ruling. Facts: the printed command is headless (`claude -p` or `codex exec`); typed after `!` it runs as a child of the authoring tool's shell, inherits its environment, and its whole output lands in the authoring agent's context. The only difference from the excluded headless launch is who typed it, which Syzygy cannot observe | Accept the reading. The review reads only its digest-bound packet, and its independence is labelled Inferred either way. If you want the review's output kept out of the authoring context, say "new terminal only"; that is a new version |
| Round 2, finding 5 | **The 020 reading and option A's full cost.** 033 reads REQ-polaris-generation-020's Proposal, approval, scheduler and materialization gates as not applying to a run that makes no provider dispatch and no scheduler effect; R1 did not ask about that. Option A ("Re-derive, label Inferred") also means the audit evidence 022 asks for is agent-editable (a refusal can be erased), and that the pinned revision and the emitted packets are stored records, so which revision a run used is Inferred. The consent check on that revision, and the packet bindings, are re-done at each step | Accept both. The run starts no scheduler work and dispatches nothing, so the gates have nothing to gate, and the costs are disclosed on every page |

### 4 — The per-run execution choice can be entered by the agent it governs

In plain terms: you record the per-run choice to let your agent build and
run the project by typing `syzygy dossier allow-execution` yourself. But the
authoring agent runs the neighbouring commands (`init`, `brief`), so it
could run this one too, or write its record into the state directory.
Syzygy cannot tell the difference; only the skill text forbids it. The
packet says "Syzygy cannot see who typed it" but does not say plainly that
the agent could. D9 leaves the mechanism to the specification, and the
reviewer calls the design honest under R1.

Recommendation: accept, with this sentence as the plain statement the
packet lacks. A stronger design (a typed confirmation from a controlling
terminal) may exclude the `!` form, which 033 allows, so it is a later
CC-REV-2 amendment, not an implementation choice.

### 8 — Records Syzygy reads, not only those it stores, are within the agent's reach

In plain terms: R1 covered Syzygy's own records. But Syzygy's gates also
read the observation consent, the registry entry, the policy acts, your
per-project statement, whether D9 is in force, and whether the RFC7-20
ruling is effective. On a one-user machine all of those are files your
agent, and in the permitted case any code it runs, can change. Changing them
changes whether Syzygy reads, whether a statement is needed, and whether
execution is invited. Quotation fidelity is unaffected: it rests on
re-hashed Git objects.

Recommendation: accept it as part of R1's cost, with two follow-ups:

- **Implementation obligation:** "Syzygy SHALL establish that a consent,
  registry entry, policy act, per-project statement, D9 or the RFC7-20
  ruling is in force by the act cross-check of RFC3-16(a), never by a status
  word or a file's presence, and SHALL disclose that the records it read for
  its gates are within the sessions' write reach."
- **Later amendment:** the disclosure sentence, in 033.

### 10 — RFC7-20 and SEC-2, the reviewer's own view

Folded into the first two rows of the table above. The reviewer found the
three conditions of your RFC7-20 reading "Applied exactly", and left the
SEC-2 "scoped" question to you.

## The other round-3 notes

Finding 8's follow-ups sit with it above. For each of the rest: an
**implementation obligation** is carried into the beads with
the exact sentence given, and binds the `syzygy dossier` implementation
without changing the specification. A **later amendment** is a CC-REV-2
change to the signed specification, offered as v1.1 or later. Some notes
are both: the obligation keeps the implementation honest now, and the
amendment makes it normative.

### 1 — The credential condition is carried as instant checks

Applies only if you adopt D9's Q3(b).

- **Implementation obligation:** "From the issue of a brief that permits
  execution until the run is closed, Syzygy SHALL attempt the
  typed-adapter credential read at every step it takes (`check`,
  `inventory-check`, `review-check`, `render`, `close`), SHALL NOT hold or
  write a typed-adapter credential where the operator's user can read it,
  SHALL take the credential list from a source the disclosure names and say
  that the source is within the sessions' write reach, and SHALL disclose
  that readability after close, and through privilege escalation, is
  Inferred." 033 already allows each of these; none narrows it.
- **Later amendment:** make the keeping obligation, the step list and the
  escalation disclosure normative in 033.

### 2 — Three conditions of the permitted case have no stated source of declaration

- **Implementation obligation:** "`syzygy dossier allow-execution` SHALL
  record the operator's declaration that the owner started the authoring
  session on the owner's own host and attends it; Syzygy SHALL issue no
  permitting brief without that declaration, SHALL label it Inferred and
  attributed to the operator, and SHALL disclose it beside the choice; tests
  SHALL cover a permitting brief refused for each missing declaration and a
  permitting brief that omits the lapse statement." 033's Inferred list is
  open ("including"), so this fits the signed text.
- **Later amendment:** name the declaration in 033 and add the two
  falsifier arms.

### 3 — "The cost D9 states" is recorded abridged

- **Implementation obligation:** "The run record and the disclosure SHALL
  carry D9's cost bullet as adopted, quoted verbatim from the adopted
  `security.md`, never a restatement."
- **Later amendment:** replace 033's restatement with a reference to the
  adopted bullet.

### 5 — "Quote SEC-3's rule" stops reading as a prohibition once D9 is adopted

- **Implementation obligation:** "A brief that does not permit execution
  SHALL quote SEC-3's head sentence as adopted, cite SEC-3, and state the
  agent-directed rule in its own words: do not build or run the observed
  project outside an explicit, opt-in execution profile." This satisfies 033's
  "quote SEC-3's rule" and tells the agent what the rule means for it.
- **Later amendment:** have 033 require the agent-directed statement with a
  citation, instead of a quotation.

### 6 — RFC5-12 and RFC5-24 change in effect in the permitted case

The reviewer lists this one for your view at sign-off as well.

- **Later amendment**, and only if you decline D9's Q3(b): add to the
  delta's "What explicitly does NOT change" that RFC5-24's "never visible to
  observed-project code" is untrue for this mode's permitted case, as D9
  discloses. No implementation obligation. Stated here so that the sign-off
  is taken in view of it.

### 7 — `SOURCE-POLICY.md`'s execution-consent sentence is neither read nor distinguished

- **Implementation obligation:** "The per-run execution choice recorded by
  `allow-execution` SHALL NOT be read, stored or reported as an execution
  consent (RFC5-12, `SOURCE-POLICY.md`), and approves no execution profile."
- **Later amendment:** one sentence in 033 saying the same.

### 9 — Residues of the round-2 repairs

- **Implementation obligation:** "The governed-subject predicate SHALL count
  any capability declaration and any `.syzygy/` path, adopted or not, as
  033's requirement says; the scenario wording 'an adopted capability
  declaration' is not the test." And: "The `/polaris-dossier` skill's
  description SHALL name any repository the operator holds the consents
  for, not only public ones."
- **Later amendment:** the scenario's wording, the impact ledger's "No
  overlap" line, the proposal's "Modified in effect" list (021,
  `OWNER-FLOW.md`, `SECURITY-CONTRACT.md`), the delta's "retained by the
  lead" (the round-2 raw is on `main`), and the packet's credential-check
  timing ("and at close"). All are editorial; none changes a requirement.

### 11 — This confirmation is bound to D9 at `62c29093`

Neither an obligation nor an amendment: it is a precondition of the
offering. D9's round 3 has since confirmed `62c29093` itself, so the bytes
this review compared against are the bytes D9's review cleared [Observed:
the D9 raw's `Reviewed commit:` line]. What remains is the check in "How to
sign off": compare D9's adopted text with 033 and 034 before the offering.

### D9 note N5 — a shipped skill cannot carry the permission

From `DOCTRINE-AMENDMENT-D9-REVIEW-NOTES.md`, routed to this
specification. Arm A counts a skill as an instruction, and its first
condition requires the choice for a run to be recorded before the
instruction is given. A skill ships before any run exists, so it can never
carry the permission itself; it can only defer to the per-run brief.
The design already does this ("Follow the execution rule in `brief.md`").

- **Implementation obligation:** "The `/polaris-dossier` skill and the
  Codex instructions SHALL NOT grant execution themselves. They SHALL only
  defer to the execution rule in the run's `brief.md`, and absent that brief
  SHALL state that the project is not to be built or run outside an
  explicit, opt-in execution profile."
- **Later amendment:** the same sentence in 033, beside "The skill and
  agent texts SHALL tell the agent never to run that command."

D9's N6 (compare reported commands against the choice's named scope and flag
any outside it) is the owner's to rule on with D9. If accepted, it becomes a
later amendment to 033 here.

## Routing

- Round 1, findings 6 to 8; round 2, findings 4, 5 and 8 (first part); and
  round 3, findings 4, 8 and 10: to the owner with the sign-off offering.
  Each has a recommended answer above.
- Round 3, findings 1, 2, 3, 5, 7, 8 (its follow-up) and 9, and D9's N5:
  implementation obligations, carried into the implementation beads with the sentences
  above once v1.0 is signed. Finding 6 and every "later amendment" line: a
  v1.1 amendment queued after sign-off.
- Round 3, finding 11: the lead's check before the offering.
- The recorder fix in "How to sign off": a separate change to `scripts/`,
  needed before the record can be written.
