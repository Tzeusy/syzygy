# Review R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-2
Reviewed commit: af97611ddfc5b42f0893837c726a82a9e7a3bb9b
Subject SHA-256: 9cf7da3eca7600eecb922ed541f67198202e7d11be2a3e3936830d301ce2d3fd
Verdict: REVISE

Reviewer: fresh-context reviewer (CC-REV-1), dispatched by the lead for round
2; did not author the change or share its session. Read only git objects: the
package at the reviewed commit, the governing references `REVIEW-BRIEF.md`
names, the round-1 raw (`docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1-RAW.md`,
origin/main), the R1 ruling
(`.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-DIRECTION.md`,
origin/main) and `AGENTS.md`. No PR conversation, transcript, drafting message
or target-repository content was read. Network use: `git fetch origin` and
`gh pr view 353` only.

Subject digest: [Observed] `git show af97611d:openspec/changes/polaris-dossier-local-agent-mode/proposed/polaris-generation/spec.md | sha256sum`.
[Observed] `gh pr view 353` reports head `af97611ddfc5b42f0893837c726a82a9e7a3bb9b`, draft, open.

Timing note: [Observed] the R1 ruling was committed in `eb7be564`
(2026-10-06 00:02 +0800), six minutes after the reviewed commit
(2026-10-05 23:56 +0800), and `git merge-base --is-ancestor eb7be564 af97611d`
fails. The package therefore cannot cite R1 and still presents it as open; I
check the spec's text against the ruling as the lead asked, and treat the
missing citation as a repair to make, not as the drafter's error.

Paths are relative to the repository root. "spec" is the subject; "base" is
`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`;
"overlay" is `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`;
"design", "packet", "delta", "proposal" are the package files of those names.
Every quotation below was re-extracted by Python substring match against the
file at the reviewed commit (whitespace-normalised for hard-wrapped prose).

## Criterion results in brief

| # | Criterion | Result |
|---|---|---|
| 1 | Does what the direction authorizes, no more | Yes for grants [Observed]: no read, egress, write or execution is granted to Syzygy; provider mode parked, not withdrawn; no adoption language. One design command contradicts 033's write rule (Finding 15) |
| 2 | Quotations exact | Yes [Observed]: all 27 "Current meaning" blocks found verbatim (base only 13, overlay only 6, both base and overlay 4, `INTERFACES.md` 2, `SECURITY-CONTRACT.md` 1, RFC-0007 1); every double-quoted predecessor fragment in spec lines 23, 142, 236 and 303 found verbatim in its named file; SEC-2's "explicit, recorded, per-project consent" found at `.syzygy/governance/doctrine/security.md`:45 |
| 3 | Displacement complete and bounded | Round-1 gaps closed. New: 021 and SEC-1 for the agent-invoked CLI (Finding 11), RFC4-19's required work-item field (Finding 12). Nothing displaced for the provider mode |
| 4 | Contract or doctrine changed in effect | Reported, not resolved: RFC7-20 (Finding 7), SEC-2 "scoped" (Finding 8). RFC7-20's three conditions applied exactly. SEC-3 gate holds in the spec, packet and harness texts (round-1 Finding 8, below); Finding 13 on tool-loaded configuration in the clone |
| 4a | Review independence as ruled | Substance yes; the `!` launch form is a lead reading the packet does not show the owner (Finding 4); the fidelity packet's span population is ambiguous (Finding 9). The frozen inventory as part of "the criteria" is a faithful reading of the owner's purpose, and is flagged |
| 5 | Every Observed claim observable | No: Findings 1 and 2; Finding 6 (note) |
| 6 | Scenarios falsifiable | Yes, with bundling notes (Finding 16) |
| 7 | Change class | Normative is right |
| 8 | Impact ledger reproducible | Yes [Observed], all figures reproduced (below) |
| 9 | Rulings applied exactly | R1 narrowed (Finding 3); `!` launch form not shown to the owner (Finding 4); 020 reading not covered by R1 as asked (Finding 5) |
| 10 | `design.md` stays design | Yes, no code; consistency defects in Finding 15 |

## Round-1 findings: does the repair hold?

| R1 # | Repair | Holds? |
|---|---|---|
| 1 | 033 (spec:13): reads "SHALL honour no replacement objects, grafts, repository-local configuration, hooks or alternates" and recompute every identifier on the path; scenario "Object store altered after pinning" (spec:41-45); falsifier arm (spec:125) | Yes. Two residual points in Finding 10 (hash algorithm; design route 1 still reads `.git/config`) |
| 2 | 033 (spec:19): records in the state directory, no Observed on a writable stored record, re-derivation at check and render, Inferred integrity | Holds for quotations and check results. Does not hold for the pinned revision (Finding 1) or the review packet (Finding 2); wording narrower than R1 (Finding 3) |
| 3 | 036 (spec:303) reads both 030 sentences; scenario "Syzygy's reads wait for its start gates" (spec:327-331); both in delta "Current meaning" | Yes |
| 4 | 035 (spec:236) reads both 006 sentences; completeness Inferred | Yes. Finding 9 on which spans the packet carries |
| 5 | 033 reads the 005 scenario; 034 (spec:142) requires the understanding record reading 002 | Yes |
| 6 | RFC7-20 preserved for the owner | Yes, in delta, packet and proposal. My own finding: Finding 7 |
| 7 | (a) and (b) stated plainly in 033; (c) consent record; (d) 032's four conditions | (a), (b), (c): yes, verbatim at spec:11 ("Neither the content classes the statement names nor the observing project's classification and screening policies (SEC-5) bind the agent sessions' own reads or sends"; "The statement is a consent record"). (d): the four conditions match, the input differs (Finding 8) |
| 8 | Execution rule gated on an adopted SEC-3 amendment; sign-off waits | Yes [Observed]: spec:3 ("this change may not be signed off until the owner has adopted ... an amendment to SEC-3"), spec:15, spec:89-93, packet:112, tasks:14-18; skill (design:310-313) and Codex text (design:372-374) say "Unless it says otherwise, do not build or run ... outside an explicit, opt-in execution profile". Nothing in spec, design or harness texts tells an agent to run observed code outside a profile. Finding 13 is adjacent |
| 9 | Headless form dropped; `!` and new terminal count; launch form recorded and refused otherwise | In the spec and skill, yes (spec:230, 234, 256; design:64-73, 337-342). Packet and proposal still describe only "a new terminal" (Finding 4); declaration path inconsistent in design (Finding 15) |
| 10 | Limits: positive deadline and budgets, nonnegative repair and question limits | Yes (spec:17, 53-57) |
| 11 | Inventory session-id refusal, scenario arm, drafter's-choice disclosure | Yes (spec:234, 256; delta; packet O4) |
| 12 | Model identity and version operator-declared; 003 relied on | Yes (spec:17; delta "Current meaning" 003 block) |
| 13 | Anchor class named, recomputed blob id as identifier and digest | Yes (spec:155), matching RFC7-10's "an **evidence artifact identifier** with integrity digest" (`narrative-contract.md`:217-229) and `SCHEMA-CONTRACT.md`:88. Finding 10 on the hash algorithm's source |
| 14 | Citation duty by block kind | Yes (spec:144, 151, 199-201) |
| 15 | Execution check applies to marked claims; page says marking is self-reported | Yes (spec:151, 113-117) |
| 16 | Disclosure scenario complete | Yes (spec:95-99) |
| 17 | 020 and work home read in 033 | Done in text; owner coverage of the 020 reading: Finding 5 |
| 18 | Packet carries findings 6 to 8 | Yes (packet:120-123) |
| 19 | Ledger extension | Yes [Observed], reproduced (Criterion 8 below) |
| 20 | Duplicate open question | Yes, merged (design:273-276) |
| 21 | Warrant decisions | Yes [Observed]: the four warrant blocks' union equals `GOVERNING-DEPENDENCIES.md` for primary (4), doctrine (7), contracts (11), policies (2), decisions (4) and parent requirements (17). R1's identifier now needs adding (Finding 3) |

## Criterion 8: impact ledger reproduced

[Observed] Re-ran sweeps A, B, E, F, G and I exactly as published, by Python
`re`, over `git ls-tree -r -z --name-only ac35c998ec3f7b20c47adc19b22ac540f851b099`:
2,328 paths, 4 not UTF-8, 2,324 searched. Files per identifier: 001 48, 005 26,
006 52, 017 39, 018 17, 030 25, 031 19; A to G 104; I alone 31; 135 in all.
Path-rule classes: 1 = 22, 2 = 26, 3 = 21 (16 under the two adopted changes and
`decisions/`, 5 under the readability and union successor packages), 4 = 31,
5 = 26, 6 = 5, 7 = 3, 8 = 1. Extension: 002 50, 003 33, 020 31, 022 15; union
63; 14 new (class 1: 3, 2: 4, 3: 3, 4: 1, 5: 1, 6: 1, 7: 1); 149 in all. The
RFC7-20 regex returns 64 files. Every published figure matches. The ledger's
populations do not cover 016 or 021 (Finding 11); extend sweep A if those are
named.

## Findings

**Finding 1 — The pinned revision is a stored record on which every Observed label rests, and nothing re-binds it after the brief** (blocking)

Where: spec:13, "Before it issues a brief, Syzygy SHALL verify that the clone's
checked-out HEAD commit equals a revision that the in-force observation
consent for the repository names, and SHALL record that commit as the run's
pinned revision."; spec:19 (re-derivation "from objects it verifies at that
step"); spec:21 (disclosure of "the pinned revision"); spec:299 (second
discovery population, Observed); design:220-242 (`run.json` in the state
directory).

Problem. The consent comparison happens once, before the brief. Every later
read, re-hash, quotation location and source page is "at the pinned
revision", which after `init` is a value in `run.json`, a file the spec itself
says the agent can write on a same-user host (spec:19). An agent that rewrites
the recorded revision to another commit present in the clone moves every
later check and render to that commit. Re-derivation at render re-derives
from objects reached *from* the stored commit, so it does not detect this.
Two consequences:

- [Inferred] Syzygy may read objects at a revision the observation consent
  does not name, contrary to the mode direction item 3 ("Those reads still
  need the target's observation consent ... This direction relaxes none of
  them") and to base:1201, retained unchanged by 033: "Current credentials,
  consent and applicable profile state SHALL be checked at each attempted
  act". Whether an implementer reads that 022 sentence as revision-specific
  is not settled by 033, so two implementers diverge on a consent behaviour.
- Every rendered Observed quotation and the second discovery population rest
  on a stored record, contrary to R1 item 1 ("No Observed label in a dossier
  rests on a record Syzygy stored on the operator's machine.") and to 033's
  own sentence.

Proposed fix. In 033: at every check, review check and render, Syzygy
re-verifies that the recorded pinned revision is named by the in-force
observation consent, and refuses the step otherwise (withdrawal of the
observation consent refuses further steps, as the statement's withdrawal
already does). Bind the revision into what is checked: the draft and the
inventory name the pinned revision, the brief and packets carry it, and a
mismatch refuses. Disclose that which consented revision the run used rests
on a stored record. Add a scenario ("Recorded revision altered") and a
falsifier arm.

**Finding 2 — "The packet's exact contents" are labelled Observed, but what the reviewer read is a writable directory Syzygy cannot observe** (blocking)

Where: spec:234, "The record SHALL distinguish what Syzygy observed, which is
the packet's exact contents and the verdict's binding to it,"; spec:269, "the
review page states that the packet contents and the verdict's binding are
Observed"; design:125-128, "rebuilding the packet from the frozen subject at
`review-check` and again at `render`, so what the reviewer was given is
Observed."; design:237 (`reviews/<kind>-packet-<digest>/` in the state
directory); design:353-354 (the reviewer reads "only the packet directory it
names").

Problem. The reviewer reads the emitted packet directory, which lies in the
state directory the authoring agent can write. The authoring agent can edit
the packet files after Syzygy emits them and before the review session reads
them; the reviewer then reviews altered content and writes a verdict naming
the digest printed for the original packet. At `review-check` and `render`
Syzygy rebuilds the packet from the frozen subject, the digest matches, and
the review page says the packet contents were Observed. What Syzygy observes
is the packet it built; what the reviewer was given is not observable. The
spec's Inferred list (spec:234) includes "that the review context saw nothing
beyond its packet" but not that it saw the packet unaltered. Design decision
5 states the unobservable fact as Observed in so many words. Criterion 5:
blocking. It also conflicts with R1 item 1 (the emitted packet is a stored
record).

Proposed fix. In 035, name as Observed only "the packet Syzygy built and
rebuilt from the frozen subject, its digest, and that the verdict names that
digest"; add to the Inferred list "that the review context read the packet
Syzygy emitted, unaltered". Make the scenario at spec:266-270 say the same.
Correct design decision 5. Optionally have the packet carry its own digest so
the reviewer re-hashes before reading (still Inferred, but a cheap check).

**Finding 3 — R1 is not applied exactly: the spec narrows "no Observed label rests on a stored record" to records "that the agent sessions can write", and the ruling is not cited** (blocking)

The ruling (`POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-DIRECTION.md`, origin/main):
item 1, "No Observed label in a dossier rests on a record Syzygy stored on the
operator's machine. `check` and `render` re-derive every quotation and every
check from re-hashed git objects on each run."; item 2, "Repair counts,
timestamps and run history are labelled Inferred, because the operator's
agent could have edited them."; item 3, "No separate OS user or sandbox is
required for the dossier mode's records."

The spec (spec:19 and 21):

- "Syzygy SHALL NOT rest an Observed label on a stored record that the agent
  sessions can write." The ruling has no qualifier. On a host where the state
  directory is not agent-writable (a separate user, which the owner declined
  to require but did not forbid), the spec permits Observed labels on stored
  records; the ruling does not. This narrows the ruling.
- "What Syzygy cannot re-derive, which is the repair-cycle count, the
  instants of earlier steps and the run record's own history, SHALL be shown
  with its integrity labelled Inferred." The ruling labels the values
  Inferred; the spec labels their integrity, and closes the list with "which
  is". Other non-re-derivable stored values fall outside the list: the pinned
  revision (Finding 1), the emitted packets (Finding 2), the brief text and
  the execution rule it carried, the statement citation, and the record of
  which objects were read (Finding 6).
- "the integrity of Syzygy's stored records is Inferred where they lie within
  the agent sessions' write reach" carries the same qualifier.
- Item 3 is met: nothing requires a separate user or sandbox.
- Item 1's re-derivation "on each run" matches "At render, and at each
  check" (spec:19). Applied.

[Observed] The ruling postdates the reviewed commit, so the package cannot
cite it: the spec's warrants (spec:133) lack
`POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-2026-10-05`; packet:86-108, tasks:11-13,
proposal:124-128, design:186-189 and the delta still present R1 as open.

Proposed fix. Drop the qualifier ("Syzygy SHALL NOT rest an Observed label on
a record it stored"), make the Inferred list open ("including the
repair-cycle count, the instants of earlier steps and the run record's own
history") or enumerate every stored input, label the values Inferred as the
ruling says, cite the ruling in 033's text and warrants, regenerate the
dependency union, and update the packet, brief, delta, proposal, design and
tasks to record R1 as answered.

**Finding 4 — The `!` launch form is a lead reading of the owner's words, and the packet and proposal tell the owner only "a new terminal"** (blocking)

Where: spec:230 ("a session the operator starts in a new terminal, or by
typing the command Syzygy printed behind the agent tool's shell-escape prefix
(in Claude Code, `!`) in the authoring session's terminal, is a session the
operator starts"); delta (Proposed meaning, review section): "After round 1
the owner's lead ruled on the launch forms (finding 9)"; packet:49-50,
"Separate top-level sessions that you start, in a new terminal, write the
inventory and the reviews"; proposal:129-130, "Separate top-level sessions
the operator starts in a new terminal, never a subagent or a process of the
author"; packet O4 row (no mention of the launch form).

Problem. The owner's option text is "A second top-level Claude Code/Codex
session you start". Whether a `!`-launched process counts is a reading of
those words. Round 1 recommended it; the lead ruled it; no owner record
exists. That may be a lawful process call, but the owner's decision surface
does not show it: the packet's plain-terms summary and the proposal both say
"in a new terminal", so the owner signs over a description narrower than
035. [Inferred] Facts the owner should see: the printed command is
`claude -p "<prompt>"` or `codex exec "<prompt>"` (design:53), a headless
invocation; launched with `!`, it runs as a child of the authoring tool's
shell, inherits its environment, and its whole output lands in the authoring
agent's context. The only difference from the forbidden "headless session it
starts and whose output it reads" is who typed the command, which Syzygy
cannot observe (the launch form is operator-declared, correctly Inferred).

Proposed fix. State in the packet's O4 row and plain-terms summary, and in
the proposal, that 035 admits the `!` form as a reading of the owner's words
taken by the lead, with the facts above, so the owner's sign-off covers it;
or offer it to the owner as a batched question.

**Finding 5 — The R1 question as asked does not cover the drafter's reading of REQ-polaris-generation-020; the packet's description of option A omits costs** (note, for the owner)

The packet put three readings under R1: "033 reads both sentences [018, 022]
for this mode, and reads REQ-polaris-generation-020's work-item gates as not
applying ... Those are security-posture readings, so they are yours."
(packet:94-97). The delta says the 020 reading "is the drafter's and goes to
the owner with the record-location question". The question the owner
answered (R1 record) speaks only of "Syzygy's own records" and asks how the
mode "should ... handle Syzygy's own records". [Inferred] It answers the 018
work-home and 022 trail readings by implication (item 3), not the 020
Proposal/approval/materialization reading. Under CC-SPEC-6 ("If a
requirement's content would settle an open owner question, the spec is
blocked on that question"), the package's own classification leaves 020
open. Also, option A's stated cost (packet:101: "An agent could rewind the
repair count or the deadline start") omits that the 022 audit evidence of
admissions, denials and refusals becomes agent-editable (a refusal can be
erased; base:1201 retained: "Pending-event recovery SHALL use trustworthy
records, never mutable work files as invented ceremony evidence"), and the
pinned revision and packets (Findings 1, 2). Fix: carry the 020 reading, and
these costs, to the owner with the sign-off offering, as findings 6 to 8 are
carried; do not record 020 as ruled by R1.

**Finding 6 — The second discovery population's membership is history from a stored record, labelled Observed** (note)

spec:299: "The second population is the set of Git objects Syzygy itself read
and verified for the run, verified again when it renders them, ... labelled
Observed." Each object's identity and screening outcome is re-derived at
render; which objects "Syzygy read for the run" in earlier steps is the read
log in the state directory, which the agent can prune. Fix: define the
population as the objects render itself reads and verifies (re-derived), or
label membership drawn from earlier steps Inferred under R1 item 2.

**Finding 7 — RFC7-20: my finding on the owner's reading** (note: reported for the owner, not resolved)

The clause (`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`,
RFC7-20): "Computing a draft is inference: absent SEC-2 named-provider consent
it is **not computed** — the draft layer renders Unknown
(`unconsented-source-or-provider`), visibly a policy state". The ruling
(`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`, item 1) reads the
condition as governing "drafts that Syzygy computes".

[Inferred] I agree with round 1 that the clause names no computing party, so
for an operator-computed draft that Syzygy renders, the reading changes the
clause's effect rather than applying its text. Under the spec as now written
the reading's work is confined: for a governed subject 033 requires a
statement it calls "the 'explicit, recorded, per-project consent' that SEC-2
requires", naming the operator's agent provider (spec:11), which would meet
RFC7-20's condition on its own text; the reading therefore does work only for
non-governed subjects, where SEC-2's coverage ("governed-project content",
security.md:43-45) is itself the question. Reported for the owner.

Application check: spec:23 admits an operator-computed draft "only when all
three of that ruling's conditions hold": disclosure of how the draft was
computed; tool and provider declared and recorded; every rendered quotation
byte-verified. These are the ruling's three conditions. The added
consequences (Unknown on failure or loss of effect; Syzygy-computed drafts
outside the reading) narrow only. Applied exactly.

**Finding 8 — SEC-2: the statement is declared to *be* SEC-2's consent, and the governed predicate reads a different input from 032's** (note: first part for the owner)

- spec:11: "The statement is a consent record: it is the \"explicit,
  recorded, per-project consent\" that SEC-2 requires before governed-project
  content reaches a model provider". The review-1 ruling, item 2, says only
  that "the statement is a consent record". SEC-2's head reads "explicit,
  scoped consent" (security.md:42-43); the spec quotes the body phrase. The
  delta calls "Whether a consent whose class limit nothing enforces is SEC-2's
  'scoped' consent" open for the owner, while the normative text asserts the
  answer. Reported, not resolved; the packet should name this sentence as the
  point the sign-off decides.
- Governed predicate: 033 decides from "the source classes of the tree at the
  pinned revision, as Syzygy's own path listing of that tree exposes them";
  032 decides from "its admitted source inventory, as the source classes that
  discovery exposes". [Inferred] 033's input is a superset, so 033 is never
  less strict, which is the safe direction. Two residual points: "an adopted
  capability declaration" is an adoption state, not a path property, so a
  path listing cannot decide it and implementers will diverge; and with both
  candidates adopted, one capability carries two definitions of "governed".
  The proposal's "overlaps it nowhere" (proposal:94) is no longer accurate
  (AGENTS.md: "An OpenSpec change is one coherent category overlapping no
  other change"). Fix: say how "adopted" is decided from the path listing
  (or that any capability declaration path counts), and record the shared
  predicate as an overlap to be reconciled at whichever adoption is second.

**Finding 9 — Which spans the fidelity packet carries** (note)

spec:230: the packet contains "the cited spans as Syzygy read them", and the
reviewer records "the accuracy of every inventory entry against the cited
spans in its packet". If "cited spans" means the draft's citations, the
reviewer cannot judge inventory accuracy. Fix: the fidelity packet carries
the spans cited by the draft and by the frozen inventory, screening-admitted
only.

**Finding 10 — Object reader: the hash algorithm's source, and design route 1** (note)

- spec:155 names "the blob's object identifier as Syzygy recomputed it ...
  with its hash algorithm named". The algorithm (SHA-1 or SHA-256) is
  declared in the clone's repository-local configuration, which 033 says is
  not honoured. Fix: the algorithm is fixed by the consented revision's
  identifier, and a clone whose objects do not hash under it refuses.
- design:100 says route 1 "still reads the clone's own `.git/config`, so it
  needs an allowlist check", and design:277 says "either meets 033". Reading
  and allowlisting the file is honouring part of it; 033 says "honour no ...
  repository-local configuration". Either relax 033 to "honour no
  repository-local configuration beyond a stated allowlist" or drop route 1's
  claim.

**Finding 11 — 021 and SEC-1 for the agent-invoked `syzygy dossier` commands, and 022's principal field** (note)

SEC-1 (security.md:23): "Non-browser agent and CLI clients are admitted only
through an explicit machine-client authentication mechanism". base:1139
(021): "Every authenticated generator act SHALL bind exactly one explicit
principal" and "Machine clients SHALL use their own explicitly scoped
credentials". base:1201 (022): audit evidence "with principal,
credential/session identity". 033 issues no credential, and the commands are
invoked by the agent. [Inferred] A local binary run as the operator's user
serves no endpoint and is likely outside SEC-1 and 021's route inventory,
but the package does not say so, and 022's principal for an admission or
refusal is unobservable (agent or operator). Fix: state in 033 that the
`syzygy dossier` commands are not served routes, hold no Syzygy credential
and are outside 021's inventory; record the audit principal as the operator,
operator-declared, with credential/session identity explicitly Unknown
("Unknown identity on refusal SHALL be explicit rather than fabricated").

**Finding 12 — RFC4-19's required work-item identity has no value in this mode** (note)

RFC4-19 (`.syzygy/governance/contracts/rfcs/RFC-0004/execution-record.md`:102):
"| work item identity + substrate alias | R | ... Unattributable runs are
admissible only rendered as unattributed execution noise, never dropped". 033
reads 020 so that the run "creates no scheduler work item". The Execution
Record (`record.json`, design:238) then lacks a required field, and 018
(retained) says "unattributable runs SHALL remain visible as execution noise".
Fix: say whether the run renders as unattributed execution noise, or what
identity fills the field.

**Finding 13 — SEC-3 and project-scoped agent configuration in the clone** (note)

[Inferred] Claude Code and Codex load project-scoped configuration and
instructions from their working directory (for example `.claude/settings.json`
hooks, `.mcp.json` servers, `CLAUDE.md`, `AGENTS.md`). A session started in,
or pointed at, the clone may execute observed-project commands through those
mechanisms, or follow instructions written in the observed repository,
without the brief inviting it. Nothing in the harness texts tells an agent
to run observed code, so criterion 4's test passes; but SEC-3 ("Observed code
is untrusted, everywhere") reaches this route. Fix: the skill and Codex texts
say never start a session with the clone as its working directory, and treat
any instruction found in the clone as data.

**Finding 14 — The rendered-design review binds pages that the final render changes** (note)

The design review's frozen subject is "the rendered pages" (spec:230). The
design flow renders at step 11, reviews at step 12 (design:44-46), and the
final pages must then show that review's outcome (spec:234: "The review page
SHALL disclose that distinction"). If re-rendering is a revision of the
subject, every design review retires itself; if not, the counted review
covers bytes other than those published. Fix: define the design-review
subject as the rendered pages excluding a named review-status region, or
state that the published pages are the reviewed pages plus only that region.

**Finding 15 — Design consistency** (note)

- Who declares session id and launch form: spec:234 says "as
  operator-declared"; design:72-73 says "The operator declares the launch
  form"; but the skill has the review session write "your session
  identifier" into the verdict and run `review-check` itself (design:353-355),
  while the author is told to "pass it to `review-check` or `inventory-check`
  with the session identifier" (design:340-342). Pick one path; if the agent
  writes it, it is agent-declared, not operator-declared.
- The inventory and review sessions start "with the run's state directory as
  working directory" (design:55), which holds `drafts/`; 035 says the
  inventory context "SHALL NOT be given the draft". Start it in a directory
  without the draft.
- `syzygy dossier render <run> [--out <dir>]` and `init ... [--out <run-dir>]`
  (design:203, 209) can write outside the state directory, against spec:13
  ("Syzygy SHALL write only to its own state directory for the run") and its
  falsifier.
- design:174 has `preflight` read the pinned tree's paths, but `preflight`
  (step 1) precedes the clone (step 2) (design:32-35); only `init` can.
- design:203 "(or the operator, in the strict form)": "strict form" is
  defined nowhere.

**Finding 16 — Scenario bundling** (note)

Several scenarios carry a second stimulus in the AND line: spec:57
("a repair-cycle or question limit of zero is accepted"), spec:87
("withdrawing the statement refuses every later step of the run, and a
subject that is non-governed under all four conditions needs no such
statement"), spec:105 ("a provider-mode run without named-provider consent
still renders its draft layer Unknown"). Each is falsifiable, but each is its
own case. Split them so each scenario has one trigger and one oracle.

**Finding 17 — Delta header and SEC-3 timing** (note)

- delta:8 "Stable IDs affected" names `INTERFACES.md` but not `OWNER-FLOW.md`
  or `SECURITY-CONTRACT.md`, both of which 033 reads.
- 033 keys the brief's execution rule to "an owner-adopted amendment to SEC-3
  ... in force and permits it", whose text does not exist. Sign-off already
  waits for the adoption (spec:3). [Inferred] If the amendment imposes
  conditions (disclosure, operator acknowledgement, limits on host
  execution), 033 and 034 may need to carry them; a confirming round before
  the amendment's text exists may be retired by it. Consider sequencing the
  confirming round after the amendment's text is fixed, or require 033 to
  cite the adopted amendment by identifier.

## Blocking findings

1, 2, 3 and 4. Findings 5 (in part), 7 and 8 (first part) are for the owner
and block nothing in this review.
