# Review R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1
Reviewed commit: f1bd0b5ccb09056905e85270037eb8cd92efa918
Subject SHA-256: f71ffd71f3cff86abe46197e8657d0690b0172edff21b71db72e30c7566a036a
Verdict: REVISE

Reviewer: fresh-context reviewer, dispatched by the lead; did not author the
change or share its session. Read only the artifact, its package files, the
governing references named in `REVIEW-BRIEF.md` and the three owner records.
No PR conversation, transcript or target-repository content was read.

Subject digest: [Observed] recomputed by `sha256sum` and by Python `hashlib`
over `openspec/changes/polaris-dossier-local-agent-mode/proposed/polaris-generation/spec.md`
at the reviewed commit; both give the value in the head, which equals the
expected value.

Commit note: this round first read dc85c2786436906b3592e0bcb04b9f335b167260.
The lead then moved the frozen head to f1bd0b5ccb09056905e85270037eb8cd92efa918.
[Observed] `git diff --stat dc85c278 f1bd0b5c` shows one file changed,
`openspec/changes/polaris-dossier-local-agent-mode/design.md` (13
insertions, 4 deletions, all in the hand-over paragraph after the loop
diagram). The subject at f1bd0b5c hashes to the same value. Every other
package file and governing reference is byte-identical between the two
commits, so findings about them stand as read. `design.md` line numbers
below are at f1bd0b5c, and Finding 9 is re-assessed against the new text.

Paths below are relative to the repository root. "spec" means the subject;
"base" means `openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`;
"overlay" means `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`.

## Criterion results in brief

| # | Criterion | Result |
|---|---|---|
| 1 | Does what the direction authorizes, no more | Yes, for grants: no read, egress, write or execution is granted to Syzygy, the provider mode is not withdrawn, no adoption language. Doctrine reach of owner rulings reported in Findings 6-8 |
| 2 | Quotations exact | Yes [Observed]: all 16 "Current meaning" blocks found verbatim (base 7, overlay 3, base-and-overlay 3, `INTERFACES.md` 2, RFC-0007 1); all 4 "Proposed meaning" blocks are byte-substrings of the spec; all 15 displaced fragments the spec names are present in the effective file |
| 3 | Displacement complete and bounded | No: Findings 3, 4 and 5. Nothing is displaced for the provider mode |
| 4 | Contract or doctrine changed in effect | Reported for the owner, not resolved: Findings 6 (RFC7-20), 7 (SEC-2 / "Any repo"), 8 (SEC-3); "unattended agent coordination" in Finding 9. The three RFC7-20 conditions are applied exactly (Finding 6) |
| 4a | Review independence as ruled | Yes in substance, with notes (Finding 11) |
| 5 | Every Observed claim observable | No: Findings 1 and 2 |
| 6 | Scenarios falsifiable | Mostly; Findings 10, 15 and 16 |
| 7 | Change class | Normative is right |
| 8 | Impact ledger reproducible | Yes [Observed], Finding 19 |
| 9 | Five rulings applied exactly | Yes, with notes on O2 (Finding 7, item c) and O4 (Finding 11); the packet's only open question is the sign-off, but see Finding 18 |
| 10 | `design.md` stays design | Yes; no code. Finding 20 |

## Findings

**Finding 1 — "Read by object identifier at the pinned revision" does not establish that the bytes read are the consented revision's bytes** (blocking)

Where: spec:11 ("Every read Syzygy makes for the run SHALL be a Git object
read by object identifier at the pinned revision through the registered
observer, never a read of the working tree"); spec:26-27; spec:101
(falsifier); spec:129 and spec:144 (rendered quotations labelled Observed);
spec:267 (second discovery population labelled Observed); `design.md`:78-86.

Problem. The clone, including its `.git` directory, is under the write
control of the agent session, and under ruling item 2 also of whatever
observed-project code that session builds and runs as the operator's user.
Pinning HEAD to a consented commit identifier and then reading objects by
identifier from that object store does not bind the bytes to the consented
revision. I checked this on a throwaway local repository (no target content;
git 2.53.0) [Observed]:

- After `git replace <blob> <other>`, the commit identifier is unchanged, and
  both `git cat-file -p <commit>:<path>` and `git cat-file --batch` given
  the consented blob identifier return the substitute bytes ("forged quote")
  under the original identifier. Only with `GIT_NO_REPLACE_OBJECTS=1` do the
  true bytes come back.
- After overwriting the loose-object file of the consented blob with the
  compressed file of a different blob, `GIT_NO_REPLACE_OBJECTS=1 git cat-file
  --batch` returns the substitute bytes under the consented identifier with
  exit status 0: the read does not re-hash.

So an implementation that meets spec:11 as written can render a quotation as
Observed, issue a source page, record an Observed object read, and run
classification and screening, over bytes that are not the consented
revision's. The 033 falsifier ("an object is read from the working tree or
at another commit") does not catch it. [Inferred] Syzygy's own `git`
invocations in that directory also consume the repository-local
configuration, alternates and grafts the agent or observed code can write.
[Unknown] whether the reader the design names (`readGitBlobsBatch`) already
disables replacement or verifies hashes; the requirement must say so either
way, since two implementers would diverge on a VIS-2 and SEC-5 relevant
behaviour.

Proposed fix. In 033, require that every object Syzygy uses is verified
against the pinned commit by content: replacement objects and grafts are
ignored, the identifier of every commit, tree and blob read on the path from
the pinned commit is recomputed from the bytes read and a mismatch refuses
the step, and repository-local configuration, hooks and alternates are not
honoured (or objects are copied into a Syzygy-owned store at `init` and
verified there). Add a scenario ("Object store altered after pinning") and
falsifier arms for a replacement ref and a swapped object file.

**Finding 2 — Syzygy's own records sit, as far as the specification says, within reach of the agent and of observed code, yet carry the Observed labels** (blocking)

Where: spec:13 (repair-cycle and deadline enforcement), spec:124 ("Syzygy
records the span's byte range"), spec:129 ("Every rendered quotation SHALL
be the span Syzygy read from the blob at the recorded byte range"), spec:200
and spec:202 ("what Syzygy observed, which is the packet's exact contents and
the verdict's binding to it"); `design.md`:183-190 and 255-257 (the agent
writes inside the run directory; "Never edit `run.json` after `init`" is an
instruction to the agent, not an enforcement).

Problem. The specification never says where the run record, check results,
recorded byte ranges, repair-cycle count, deadline start, packet digests and
counted verdicts live, or that the agent cannot rewrite them. The design puts
them in a run directory the agent session writes to, on a host where the
agent may run observed code as the same user. Adopted text that binds here
and is neither displaced nor read:

- base:959, REQ-polaris-generation-018: "Each execution run SHALL retain one
  immutable, identified, integrity-verifiable Execution Record in its
  governing work home".
- base:1201, REQ-polaris-generation-022: "Every admission, denial, egress, run
  launch, adapter effect, consent grant/revocation and credential
  issuance/rotation/revocation SHALL emit durable, identified,
  integrity-verifiable audit Evidence" and "The trail SHALL reside outside the
  governed plane and untrusted actor write reach; work records or a same-user
  writable directory SHALL NOT substitute." Also: "Credentials authenticating
  to Syzygy SHALL NOT be injectable into observed-project execution."

An agent that edits a recorded byte range shifts which blob bytes render as
the Observed quotation; one that edits a check result, cycle counter or
verdict record changes readiness. One implementer will re-verify at render
from Syzygy-held state; another will trust the files. That divergence is on
the label of record (VIS-2).

Proposed fix. Add to 033 that every record on which an Observed label,
a limit or readiness rests is held where neither the agent sessions nor
observed code can write, or is integrity-bound and re-verified by Syzygy at
each later step and at render; that `render` re-locates or re-verifies every
quotation against the verified blob rather than trusting a recorded range;
and state how REQ-polaris-generation-022's audit trail and credential rule
apply to `init`, `check`, `review-check` and `render` in this mode (or name
022 as displaced, with the reason). Add the falsifier "an agent edit to a
recorded byte range, check result, cycle count or verdict changes a rendered
Observed quotation, a limit or readiness".

**Finding 3 — 036 keeps REQ-polaris-generation-030's read and execution sentence unchanged while making the agent's unrestricted, possibly executing exploration the 030 discovery** (blocking)

Where: spec:267 (the agent's account is the discovery account that 030
requires) and spec:271 ("Every other sentence and scenario of
REQ-polaris-generation-030 and 031 is unchanged"); overlay:584.

Problem. Overlay:584, REQ-polaris-generation-030, contains: "The generator
SHALL perform question-directed, bounded discovery for a selected project
only after the applicable metadata-only start preparation, work/admission
gates and effect permissions; investigation SHALL NOT read sources to
authorize itself." and "Body, code, history and other content reads SHALL
remain individually covered by applicable consent and classification; no
shell or observed-project execution is implied." In this mode the discovery
that 030 governs is performed by the agent, which by the owner's rulings
reads the whole clone without classification (mode direction Q1 and item 1)
and may build and run the project (rulings item 2), and which in the design
clones and may explore before `init` and the brief (`design.md`:34, 38).
Retaining those sentences unchanged makes every operator-agent run violate
030 on its face, or forces an implementer to read "the generator" as
excluding the agent, which the spec never says. Two implementers diverge on
whether the agent's reads must be classified.

Proposed fix. Name these two sentences in 036's displacement paragraph and
read them explicitly: in this mode the agent's reads and execution are the
operator's own act under the rulings and are disclosed as such; the start
gates and the "individually covered" rule bind every read Syzygy itself
makes, and the brief is issued only after them. Add 030's sentence to the
semantic delta's "Current meaning".

**Finding 4 — 035 keeps 006's requirement that the fidelity reviewer verify the inventory against the admitted sources, but the packet it mandates holds only cited spans** (blocking)

Where: spec:198 (packet "containing only the frozen subject ..., the cited
spans as Syzygy read them, the governing criteria, and the verdict schema";
fidelity packet also carries the frozen inventory), spec:204 ("Every other
sentence and scenario of REQ-polaris-generation-006 ... is unchanged");
overlay:235; `design.md`:295-297 ("read only the packet directory it names").

Problem. Overlay:235, REQ-polaris-generation-006, retains: "The fidelity
reviewer SHALL verify inventory accuracy and completeness against the owning
admitted sources rather than trusting preparation output." and "The bounded
workflow SHALL prepare or validate the independent inventory and questions
from admitted sources". 035 reads only the words "covering the entire
admitted source population" and "accounting for those calls in its run
budget". A reviewer limited to the packet cannot verify the inventory's
completeness against the sources: it holds the inventory's own cited spans
and the draft's, nothing else. The inventory is also prepared by an agent
reading the unrestricted clone, not from admitted sources. The owner's
ruling fixes the packet ("only the draft, the cited spans and the
criteria"), so this is a tension between the ruling and retained adopted
text, and the spec must resolve it in words rather than leave both. As
written, one implementer will give the reviewer the clone, against the
ruling, and another will report a verification the reviewer could not do.

Proposed fix. Name both sentences in 035's reading paragraph: in this mode
the fidelity reviewer verifies the accuracy of each inventory entry against
the cited spans in its packet, and the inventory's completeness and its
preparation from the whole source population are the inventory context's
self-report, labelled Inferred, never verified; readiness does not claim
otherwise. Add both sentences to "Current meaning". If the owner wants
completeness verified, that needs a change to the ruled packet, which is the
owner's.

**Finding 5 — Retained 005 scenario and the amended 002 ask for stage inputs and a producer understanding that an operator-agent run cannot supply as written** (blocking)

Where: spec:17 ("Every other sentence and scenario of
REQ-polaris-generation-001, 005, 017, 018 and 025 is unchanged"); base:272;
overlay:9; spec:116 (brief contents); `design.md`:192-204 (draft schema).

Problem. Base:272, REQ-polaris-generation-005 scenario "Inspectable
successful run": "its record identifies source understanding, narrative
construction, fidelity review, rendered design review and any repairs with
their actual inputs and outputs". The actual inputs of source understanding
and narrative construction are the agent's unrestricted reads, which 036
says Syzygy cannot observe; the scenario is retained unchanged, so it is
unmeetable in this mode. Overlay:9, REQ-polaris-generation-002 as amended:
"Before drafting the central argument, the generator SHALL expose a
reviewable understanding of supported purpose, beneficiary, proposition,
capabilities, ..." 002 is not named as affected or relied on, the brief in
034 does not ask for that understanding, and the design's draft schema has
no place for it. One implementer will add an understanding record to the
schema; another will not.

Proposed fix. In 033, read the 005 scenario's "actual inputs" for the
authoring stages as the pinned revision, the brief and the agent's
self-reported account (Inferred), with Syzygy's own steps' inputs and outputs
Observed. In 034, require the draft to carry the 002 understanding as a
self-reported record, or name 002's sentence and say how it reads; add 002
to the stable IDs relied on, and to the impact ledger if its sweep should
cover it.

**Finding 6 — RFC7-20: the owner's reading, and whether it is a contract change** (note: reported to the owner, not resolved)

The clause, `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:416-430,
in the part that matters: "Computing a draft is inference: absent SEC-2
named-provider consent it is **not computed** — the draft layer renders
Unknown (`unconsented-source-or-provider`), visibly a policy state". The
rulings record, item 1, reads that condition as governing "drafts that
Syzygy computes".

My finding [Inferred]: the clause carries no qualifier about who computes
the draft. Its subject is the act of computing a draft, and its consequence
falls on the draft layer Syzygy renders. Reading it as limited to Syzygy's
own computation adds a qualifier the text does not carry, so for an
operator-computed draft rendered by Syzygy I find the reading to be a change
to the clause's effect, not an application of its text. Two qualifications,
for the owner:

- For a governed subject the reading may do no work. 033 already requires an
  in-force per-project statement naming the operator's agent provider
  (spec:9). If that statement is the "SEC-2 named-provider consent", the
  RFC7-20 condition is met on its own text and no reading is needed.
- For an observed, non-governed subject, SEC-2 covers "governed-project
  content" only (`.syzygy/governance/doctrine/security.md`:42-44). A second
  reading is open: RFC7-20's condition, which names SEC-2 consent, may not
  reach content SEC-2 does not cover. RFC2-24 reason 6's condition is "SEC-2/SEC-4
  consent absent or withdrawn for a needed repository or model provider".
  On that reading the owner's ruling would be unnecessary rather than a
  change. Which reading holds is a contract question for the owner.

Check of application (criterion 4, second part): spec:17 admits an
operator-computed draft "only when all three of that ruling's conditions
hold": disclosure of how it was computed; tool and provider declared and
recorded; every rendered quotation byte-verified. These are the ruling's
three conditions, no wider. The added consequences (Unknown when a condition
fails or the ruling ceases to be effective; Syzygy-computed drafts governed
without the reading) narrow, never widen. Applied exactly.

**Finding 7 — SEC-2 and "Any repo": whether 033's reconciliation meets SEC-2's text** (note: reported to the owner, not resolved)

The clause, `.syzygy/governance/doctrine/security.md`:42-56: "No
governed-project content, or anything derived from it, is sent to a store or
service the owner does not control — model providers included — without
explicit, recorded, per-project consent." and "Onboarding consent must name
the providers permitted for the project and the content classes they may
receive; Syzygy renders that consent on the project's surface." and
"Without consent, the inferred layer renders Unknown instead of being
computed."

033 (spec:9) requires, for a governed or silent subject, an in-force
recorded per-project statement naming the agent provider and the content
classes it may receive, separately revocable and renderable. On its words
that matches "What consent must say". For the owner:

- (a) The content-class limit is unenforceable and unobservable in this mode.
  The agent reads the clone without restriction and sends what it reads.
  Syzygy can record which classes the operator consented to, but nothing
  confines the sends to them. Whether a consent whose class limit nothing
  enforces is SEC-2's "scoped consent" is a doctrine question.
- (b) In a governed project the agent may read and send content that SEC-5's
  policy would exclude, including secrets. SEC-5's text binds "any Syzygy
  surface, store, or endpoint" (security.md:85-96), which the agent's
  provider is not. The interaction is unaddressed in the package.
- (c) The option the owner selected was described as "Also usable on
  governed projects ... their content would then reach your agent's
  provider without a Syzygy egress record." 033 lets the statement be "held
  in the existing egress-consent class of REQ-polaris-generation-025". That
  is arguably a Syzygy egress record, so the drafter's reconciliation may
  narrow the selection as it was described to the owner. The owner should
  see this.
- (d) "Governed" is decided from the admitted project input alone (spec:9).
  The sibling candidate 032 decides it from four conditions, including an
  `openspec/**` tree in the admitted inventory
  (`openspec/changes/polaris-non-governed-narrative-profile/proposed/polaris-generation/spec.md`:9).
  If both are adopted, one subject can be non-governed for 033's SEC-2 gate
  and governed for 032. Overlap note: align the predicates, or have 033 adopt
  032's.

Whether "Any repo" reaches doctrine: on SEC-2's text, with a per-project
statement required for governed subjects, I do not find that "Any repo"
itself edits SEC-2. Items (a) and (b) are where it may reach SEC-2's "scoped"
and SEC-5. Reported, not resolved.

**Finding 8 — SEC-3 and the agent's execution of the observed project** (note: reported to the owner, not resolved)

The clause, `.syzygy/governance/doctrine/security.md`:61-70: "**SEC-3 —
Observed code is untrusted, everywhere.** Observed-project code runs only
inside an explicit, opt-in execution profile." and "It is untrusted whoever
owns the project." Its violation example is "an execution profile that
inherits the host user's ambient credentials 'for convenience.'"

The rulings record, item 2, permits the agent session to build and run the
observed project. The question put to the owner stated "SEC-3 only binds
Syzygy's own execution". 033 (spec:11) makes Syzygy's brief say so. My
finding [Inferred]: SEC-3's text is not limited to code Syzygy runs. A brief
Syzygy issues that permits running the project on the operator's host with
ambient credentials and no profile reads, on that text, as observed code
running outside a profile. The ruling rests on a reading of doctrine.
`AGENTS.md` ("The daemon never executes observed project code or test suites;
separate operator commands do.") supports operator-run execution as this
repository's operating procedure; it is not doctrine. Reported for the owner;
the ruling is not treated as wrong. Findings 1 and 2 are the
specification-level consequences this ruling makes urgent. They do not depend
on how this question is answered.

**Finding 9 — "Unattended agent coordination", and the new optional launch forms** (note: the headless form reported to the owner)

Where: `design.md`:50-70 at f1bd0b5c; skill text `design.md`:284 and Codex
text `design.md`:321-322; spec:198, 202.

[Inferred] I do not find agent-to-agent coordination in the specification.
035 (spec:198) requires each inventory and review session to be "a separate
top-level agent session that the operator starts". The design's default path
(`design.md`:50-61) has the operator open a new terminal and start the
session with the prompt Syzygy printed. That meets the ruling and keeps the
operator at each hand-over.

The new "optional convenience" paragraph (`design.md`:63-70) offers two
other forms:

- (a) The operator launches the printed command from inside the authoring
  session with Claude Code's `!` prefix. The operator still types the launch
  and the prompt is Syzygy's. I find it compatible with "a second top-level
  ... session you start", with one cost: the review's output comes back into
  the author's context. That harms nothing in the review itself.
- (b) The operator approves the authoring session "running it headless". In
  this form the authoring agent starts the review process and receives its
  output. The owner's option text was "A second top-level Claude Code/Codex
  session you start ... A subagent spawned by the authoring session does not
  count". The scope record, item 2, says "runs in a separate top-level
  session that the operator starts". A headless process that the authoring
  agent launches and whose output it consumes is not, on those words, a
  session the operator starts. It differs from a subagent only in its
  process boundary. It is also one agent dispatching and reading another,
  which is the case AGENTS.md's "No unattended agent coordination" asks
  about. The operator's per-launch approval makes it attended. Whether form
  (b) satisfies the ruling is the owner's question, and the design is right
  to flag it rather than decide it. The design must not, however, present
  form (b) as meeting 035 before the owner rules, since 035's text ("that
  the operator starts") does not admit it.

Consistency defects introduced by the change:

- The skill (`design.md`:284: "never start it yourself and never use a
  subagent for it") and the Codex text (`design.md`:321-322: "Never start it
  yourself or delegate it to a sub-agent") still forbid the authoring
  session from starting the session. Form (b) contradicts both.
- "The run record notes which form ran, as operator-declared" has no home in
  the specification: 035 records tool, version and session identifier only.

Proposed fix. Either drop form (b), or keep it marked as pending an owner
ruling, outside the default skill and Codex texts. If the owner admits it,
amend 035's statement to say so, and add the launch form to the
operator-declared fields 035 records, labelled Inferred. Keep form (a), and
say in 035 or the design that a `!`-prefixed launch counts as
operator-started.

**Finding 10 — Limit rules contradict each other at zero** (note)

Where: spec:13 ("positive finite limits: ... a finite nonnegative
repair-cycle limit and a finite clarification-question limit" and "A
configuration that ... states an unlimited or non-positive value, SHALL be
refused"); spec:43.

Problem. A repair-cycle limit of 0 is "nonnegative" (allowed) and
"non-positive" (refused). Nothing says whether a question limit of 0 is
allowed. The "Limits declared by the operator" scenario has two contradictory
expected outcomes at 0.

Proposed fix. State per limit: deadline and token or turn budget positive;
repair-cycle and question limits nonnegative integers, 0 allowed; refuse
only unlimited, negative, non-integer or (for the first two) zero values.

**Finding 11 — Review independence: faithful in substance; three readings to make explicit** (note)

Where: spec:198, 202, 224-226; scope record item 2.

- The owner's text is "given only the draft, the cited spans and the
  criteria". The fidelity packet adds the frozen inventory "as the criterion
  against which REQ-polaris-generation-006 measures coverage", and every
  packet adds the verdict schema. Treating the inventory as part of "the
  criteria" is faithful to the purpose, since 006 cannot be reviewed without
  it. It is still a reading of the owner's words, and the delta flags it
  correctly (SEMANTIC-DELTA.md:257-261). The verdict schema is a format,
  not content, and is harmless. Say so in the delta too.
- The ruling speaks of "the fresh-context fidelity review". 035 extends the
  separate-session rule to the inventory and the rendered-design review, and
  the session-identifier rule to the inventory session. Each extension is
  stricter, not wider, but it is the drafter's choice, and the packet's O4
  row should say so.
- Syzygy refuses a verdict whose declared session identifier equals the
  author's or the inventory's (spec:202), but nothing refuses an inventory
  whose declared session identifier equals the author's. Add that refusal and
  a scenario arm for it.

**Finding 12 — Inference provenance lacks the model identity** (note)

Where: spec:13 (declared: operator, agent tool and version, agent's model
provider); spec:118 (agent claims are Inferred); spec:129 (editorial-draft
state).

RFC7-20 requires the editorial draft to be "machine-marked with its
inference provenance (model, version, inputs ...)". RFC7-2 (c) requires
"Inferred with its inference provenance". Base:98, REQ-polaris-generation-003
(unchanged, not named): "Requested model identity and provider-reported
version SHALL be distinguished; unavailable version information SHALL be
explicit, not guessed." The configuration names the tool and the provider,
not the model. Add the model identity, and its version where the tool shows
one, as operator-declared and Inferred. State that a provider-reported
version is unavailable in this mode. Add 003 to "relied on".

**Finding 13 — RFC7-10 target class not named** (note)

Where: spec:129 ("Each anchor SHALL take RFC7-10's form, with the blob's
object identifier as the target identifier, the byte range as the fragment
and the pinned revision as the target state").

RFC7-10 (narrative-contract.md:217-233) types an anchor as "(target class,
target identifier, optional fragment, target state)", with the class drawn
from a closed list of five. The base change's
`SCHEMA-CONTRACT.md`:80-88 maps them to variants. The only plausible variant
is "Evidence artifact: Owning evidence identifier, integrity digest, optional
fragment and captured artifact revision". The spec does not name the class,
and it does not say whether a blob identifier is both the "owning evidence
identifier" and the "integrity digest". Name the class and the mapping so
the anchor conforms without an implementer's choice. Given Finding 1, the
integrity digest should be one Syzygy verified.

**Finding 14 — "Every claim block SHALL cite at least one source" is ambiguous for non-normative and Unknown blocks** (note)

Where: spec:118.

Base:98 (REQ-polaris-generation-003): "non-normative framing SHALL NOT carry
unused anchors"; RFC7-9 (b): "A surplus anchor is a defect". If a
non-normative block is a "claim block" under spec:118, it must cite a
source it does not rely on. An Unknown block (for example, purpose not
stated anywhere) may have no source to cite. State which block kinds must
cite, and that a non-normative block carries no citation.

**Finding 15 — The execution-basis check can only see claims the agent marks** (note)

Where: spec:118, 125, 89-93, 101.

Syzygy can tell a claim "rests on execution" only if the agent marks it
(`basis: execution` in `design.md`:203). An unmarked claim that rests on
execution passes every check, and the scenario's WHEN ("a claim rests on
what it observed") is not observable by Syzygy. The label stays Inferred
either way, so the harm is to the disclosure, not the label. Restate the
check and scenario as applying to claims the agent marks as resting on
execution, and say on the page that the marking is self-reported.

**Finding 16 — Disclosure scenario omits two items the statement requires** (note)

Where: spec:15 versus spec:73-75.

The statement requires disclosure of the reported build and run commands
and that every rendered quotation was verified by Syzygy. The scenario "Mode
disclosed on every page" lists neither. The falsifier ("a disclosure is
absent") covers them only by implication. Add both to the scenario's THEN.

**Finding 17 — Work home, start gates and materialization left to implementation planning** (note)

Where: SEMANTIC-DELTA.md:219-222; `design.md`:218-223.

REQ-polaris-generation-018's "governing work home" and REQ-polaris-generation-020's
Proposal and materialization gates are said to be undisplaced, with their
application to a local run "decided in implementation planning". If they
bind unchanged, an operator-agent run needs a materialized work item and a
governing work home before the brief. If they do not, the spec must say how
they read. Leaving it to planning means two implementers may differ on
whether a run is authorized to start. At minimum, state in 033 whether
`init` requires 020's materialization record, and which home holds the
Execution Record. This interacts with Finding 2.

**Finding 18 — The packet's "one remaining question" should carry this review's owner findings** (note)

Where: OWNER-DECISION-PACKET.md:48-83.

The packet says all five rulings are applied and that only the sign-off
remains. Findings 6, 7 and 8 are questions the rulings left for the owner by
design ("A reviewer who finds it to be one should report it, not resolve
it"). The packet should say that the review's findings on RFC7-20, SEC-2 and
SEC-3 go to the owner with the sign-off offering, and that sign-off is taken
with them in view. Neither the drafter nor the lead should absorb them.

**Finding 19 — Impact ledger reproduced** (note)

[Observed] Re-ran the ledger's published regexes (A, B, E, F, G, I) by Python
`re` over `git ls-tree -r -z --name-only ac35c998ec3f7b20c47adc19b22ac540f851b099`:
2,328 tracked paths, 4 not UTF-8, 2,324 searched. Files per identifier:
001 48, 005 26, 006 52, 017 39, 018 17, 030 25, 031 19. Union A-G 104, I
alone 31, total 135. Path-rule classification: raws 22, evidence/pursuits
26, class 3 21 (16 under the two adopted changes and `decisions/`, 5 under
the readability and union successor packages), class 4 31, class 5 26,
class 6 5, class 7 3 (`README.md`, `REDIS-DOSSIER-GAP-ANALYSIS.md`,
`TARGETS.md`), class 8 1 (the CAP1 spec). All match. The RFC7-20 sweep returns
64 files over the same 2,324. The ledger's populations do not include 002,
003, 020 or 022 (Findings 2, 5, 12, 17). If those are named, extend sweep A.

**Finding 20 — `design.md` small items** (note)

Where: `design.md`:215 and 227.

No implementation code; the skill and Codex texts are prose. The
"Session identifiers" open question appears twice (lines 215 and 227); merge
them. The design's "Built from (existing code)" column names functions and is
not a behaviour claim. No command claims behaviour the requirements do not
require, except that the skill's "Never edit `run.json` after `init`"
(line 256) is the only stated protection of a record Syzygy relies on (see
Finding 2).

**Finding 21 — Warrant blocks declare no decisions although the statements rest on three owner directions** (note)

Where: spec:109, 191, 260, 321 (`decisions: []`); spec:9, 11, 17, 198 cite
`POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05`,
`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05` and
`POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`;
`GOVERNING-DEPENDENCIES.md`:31-33.

The requirement text relies on the directions by identifier, and 033's
draft-layer admission depends on a ruling's continued effect. The warrants
are the only home for dependencies (`GOVERNING-DEPENDENCIES.md`:6-13), so a
generated union will not show that the requirements depend on those
directions. List them under `decisions`, or say why a plain direction is not
a decision warrant. [Observed] The hand-held union otherwise equals the union
of the four warrant blocks, for primary, doctrine, contracts, policies and
parent requirements.

## Blocking findings

1, 2, 3, 4 and 5. Findings 6, 7 and 8 are for the owner and block nothing in
this review.
