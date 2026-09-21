# Owner decision packet — retention posture for retained Polaris
evaluation records

> **Candidate — binds nothing.** This packet is an inert offering. It
> performs no act, records no ruling, adopts nothing, authorizes no
> implementation and changes no accepted artifact. It presents **one**
> decision and the exact text of the dated owner direction that would
> give it effect; until you issue that direction in your own words, in
> your own session, nothing here has any effect. A commit, a merged pull
> request, a review, a manifest, a bead closing, silence, or a general
> "approved" performs nothing.

Date drafted: 2026-09-21. Drafted by an agent session under the owner's
2026-09-21 rulings, which authorize drafting only.

Warrant for drafting: `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`
(this directory), row **P-79**, arm **A**: "Q1 yes, a retention-posture
change needing an owner act before slice 1". That row also records the
consequence this packet exists to remove — "Nothing in M12 is ready:
slices 1–2 wait for the retention act" — and names the gate bead
`syzygy-dov.28`. This packet does not restate what is ready; `bd ready`
owns that.

Subject of the decision: the retained evaluation record designed as slice
1 of `docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md`. That funnel
packet remains the question P-79 was ruled on; this packet is the gate it
named, and it repeats none of the funnel's arms.

## Why an owner act is needed at all

The escalation trigger is named, by its own noun, in the act in force.
`PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` (this directory),
§"Escalation triggers", quoted whole:

> Stop and return to the owner before proceeding if implementation would
> need any of: a change to doctrine or an accepted contract; a further
> amendment to the signed PWB specification beyond the 2026-09-05
> package; a change to security, privacy, or retention posture beyond the
> 2026-09-05 approved secret-classification policy; a change to the
> constraints or envelope the 2026-09-05 registry entry declares; any
> observation outside the consented content class or repository; or any
> scope beyond the signed change.

`[Observed]` The daemon today retains, across restarts, no evaluation at
all. Slice 1 would write one file per identified evaluation and keep
every one of them. Whether "beyond" the approved policy reaches a derived
record the policy does not describe in either direction was the funnel's
Q1; **you ruled it does**, so this gate exists and the direction below is
what closes it.

`[Inferred]` Because the trigger is crossed by the *posture*, not by any
governed byte, the instrument that closes it is a **plain owner
direction**: it binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md`, needs no manifest, no recorder script, no
act-phrase registration and no ceremony. That is the shape of
`THREE-SURFACE-POC-MODE-DIRECTION.md` and
`POLARIS-TRUSTED-BOOTSTRAP-OBSERVATION-DIRECTION.md` (both this
directory), and of the continuation act quoted above, which says of
itself that it "binds no artifact bytes, adds no row to the
acceptance-act record and registers nothing".

## The one decision

**Question: do you issue the dated direction below, so that a retained
evaluation record may be written at all?**

- **(a) Issue it as drafted** *(what this packet offers)*. Slice 1 becomes
  lawful within the four corners of the direction; slice 2 stays gated on
  its own bead order and on nothing in this packet.
- **(b) Issue it with your edits.** Every number, field name and boundary
  below is yours to change; the drafter's choices are listed in "What is
  the drafter's and not yours" so you can see which are which.
- **(c) Decline, or say nothing.** **Default if unanswered: no record is
  retained.** Slice 1 does not ship and slice 2 with it; the daemon keeps
  forgetting every evaluation at exit, which is the state today and
  violates nothing.

Declining costs the project the thing the pursuit found missing, and
nothing else: no code is unwound, because none has been written.

## What the record would hold — the exact fields

Per your P-79 Q2 ruling: "claim identity plus epistemic tuple and
challenge state only".

**Per claim, the payload is closed at exactly three fields.** Named
against the shipped model, `project-shape-model.ts` in
`packages/three-surface-poc-core/src/`, whose `ProjectShapeClaim` carries
six:

| Field | Retained? | What it is |
|---|---|---|
| `claimId` | **yes** | the stable semantic claim identity |
| `epistemic` | **yes** | label, tier, freshness, and the closed reason set (or the deferred basis) |
| `challenge` | **yes** | the challenge state, closed at one admitted value today |
| `evaluationId` | no — carried once | the instance identity; it is the same for every claim in one record, so it lives in the record envelope, never repeated per claim |
| `resolutionRoutes` | **no** | derivable from the tuple by the module's own route function; storing it costs 26,348 bytes per evaluation and adds no fact |
| `support` | **no** | the support anchors, which is where source coordinates would live |

**Once per record, the envelope.** A per-claim map alone would not be an
observation record: doctrine requires one to be *evaluation-identified*
(VIS-6(b), quoted below). The envelope is therefore closed at: the schema
name; the evaluation identity the model already computes
(`snapshot`, `snapshotLabel`, `inputsDigest`, `asOf`); the observer
revision; the observed project's revision; and two counts (claim objects,
distinct identities). Nothing else. `[Inferred]` The envelope is the
drafter's reading of what "claim identity plus epistemic tuple and
challenge state only" must carry to be a record at all rather than a
loose map; if you want it narrower, that is edit (b).

**What is excluded, and why.**

- **Source bodies and body bytes of any kind.** The approved
  secret-classification policy's own retention clause reads `"never"` on
  all five members of `rawBodyHandling` — storage, logging, rendering,
  machine response, external egress [Observed, read at the policy file
  this session]. Storing a body would breach the policy this direction is
  careful not to touch.
- **Secrets and anything the policy excludes or cannot classify.** SEC-5
  makes a secret reproduced "in any Syzygy surface, store, or endpoint" a
  trust-floor violation, and a retained record is a **new store**. An
  excluded or unclassifiable item is already absent from the model, so it
  is absent from a projection of the model by construction.
- **Support anchors and resolution routes.** Anchors are where a source
  path and offset would enter; routes are redundant. Dropping both is
  what keeps the record a projection of already-served epistemic state
  rather than a second, quieter copy of the observation.
- **Any observed repository's file content.** No slice reads anything new:
  the record is built from the in-memory model of an observation already
  made under the consented content class, and reads no file to build it.

**Disclosed, because the absence claim would otherwise be false.** The
claim identities themselves are *interpolated from observed-project text*
for the great majority of claims — at the funnel's baseline, 1,117 of
1,148 distinct identities, of which 278 are repository-relative source
paths and 415 are declared item class-and-key pairs [Observed by the
funnel packet at commit `a9f671e`; not re-measured in this session]. That
is precisely the substance of your Q1 and the reason this is a posture
change and not a formality: **derived observed-project metadata becomes
durable**. The epistemic tuple and the challenge state carry no observed
text at all — every admitted value is a closed vocabulary fixed in
Syzygy's own source.

## Where it lives, how long it lives, and what says so

**Where.** The daemon's own state directory — the path given to the
running daemon by its state-directory option, defaulting to an operating
system temporary directory. It is the same directory, under the same
posture, that already holds the materialization record and the
test-artifact record [Observed, both writers read at source this
session]. Never an observed repository, and never inside `openspec/**`
or `.syzygy/**`.

`[Inferred]` How the drafter reads the write boundary. Doctrine's write
rule is **VIS-5** (`.syzygy/governance/doctrine/vision.md` lines 141–166),
whose opening sentences, through line 145, are:

> **VIS-5 — Syzygy never writes code; direct writes are confined to two
> namespaces.** Syzygy's **direct project-content writes** touch only
> `openspec/**` (in OpenSpec-compatible form — architecture.md, schema
> ownership) and `.syzygy/**` (its native, schema-versioned namespace).
> No governance manifest, configuration, or convention may extend that
> direct-write universe.

A runtime state file in the daemon's own state directory is not
project-content, is not committed out, and is authored by nobody's
governance; the two existing records there were written under the same
authority and no act has been read as extending the write universe by
them. The operating procedure the repository gives agents states the same
boundary in its own words — "No implementation code inside `openspec/**`
or `.syzygy/**`" (`AGENTS.md`, hard prohibitions) — and that file says of
itself that it is never citable as authority, so it is quoted here as
procedure, not as warrant.

**SEC-4 does not reach this write, and the packet says so rather than
leaning on it.** `.syzygy/governance/doctrine/security.md` lines 47–52:

> **SEC-4 — Writes are consented, attributed, and revertable.** Syzygy
> writes into a governed repository only after recorded per-repository
> consent (onboarding), and every write is attributed to Syzygy, atomic,
> and individually revertable. Syzygy never overwrites existing
> governance artifacts it did not author without surfacing the conflict.
> *Violation:* first-pass doctrine drafting silently replacing an
> existing `.syzygy/governance/` tree.

`[Inferred]` SEC-4 governs writes *into a governed repository*. The
retained record is written into neither the observed repository nor
Syzygy's governed plane, so SEC-4 is not the clause that permits it and
is not the clause that forbids it; it is the clause that would govern the
note promotion this direction explicitly does not authorize. Its
discipline is nonetheless met in substance: the write is atomic, its
author is the daemon, and deleting the state directory reverts it
entirely.

**How long.** **Unbounded** — no record is ever pruned, discarded or
overwritten, per your P-79 Q2 ruling. The cost is visible rather than
argued: about **177,031 bytes per evaluation** at the funnel's measured
population [Observed by the funnel packet at `a9f671e`], plus the file's
envelope.

**And therefore, disclosure.** Your ruling attaches a condition to the
unbounded arm: "the on-disk total rendered beside the delta". The delta
band is slice 2, which lands after slice 1. So the direction below states
the obligation in a form slice 1 alone can satisfy: **from the first
build that retains a record, the retained-record count and the on-disk
byte total are rendered on the surface, and when the delta band lands the
total renders beside it.** `[Inferred]` That reading is the drafter's; the
alternative — retention runs silently until slice 2 catches up — is
available to you and is edit (b).

## What the direction would **not** authorize

Each is a separate gate; none of them moves because this one does.

1. **The dismissal.** P-79 Q5: a dismissal acting on a claim's own tuple
   is an amendment to the signed PWB requirement's closed challenge
   vocabulary, and needs its own CC-REV-2 semantic delta, its own review
   and its own owner act. Nothing in this direction widens that
   vocabulary, and the specification bytes are act-bound.
2. **Promotion of the owner's note.** P-79 Q4 defers it. No note is
   promoted, committed out, or written anywhere but the daemon's own
   state directory; the stage-1 unpromoted note remains what VIS-6(a)
   permits as personal presentation state and nothing more. The write act
   for promotion is a separate, later question.
3. **Any write into an observed repository.** P-71-Q5 was ruled on the
   reading that the 2026-09-02 act forecloses the return path; the
   observer registry entry declares an empty write surface [Observed,
   read at the registry entry this session] and those bytes are
   digest-bound. This direction touches neither, and a future
   write would need a dated act naming it *and* a registry-entry
   amendment act, in that order.
4. **Any new route, and any new or relaxed ceiling.** Nothing is served
   from the retained record by this direction: no machine route, no human
   route, no download, no listing. The two response ceilings the registry
   already declares are unchanged, and a response-ceiling breach serves
   nothing, so the disclosure line above must be costed in bytes by the
   implementing bead like any other rendered text.
5. **Anything else the continuation act excludes.** No second repository,
   no wider content class, no consent amendment, no egress, no
   observed-code execution, no deployment, release or mission effect, no
   doctrine or contract change, no autonomous adoption.

## Invariants a reviewer can check after slice 1 lands

Each row names the property and the mutation that must make a test fail —
verification rule 6's discipline, stated before the code exists so the
tests cannot be written to the code's shape. `[Inferred]` The list is the
drafter's; it is offered as the acceptance floor for the implementing
bead, not as part of what you would be authorizing.

| # | Invariant | Mutation that must falsify it |
|---|---|---|
| I1 | The per-claim payload is closed at three keys | add `resolutionRoutes` to the stored payload — the key-set assertion must fail |
| I2 | The record contains no body bytes, no support anchor and no credential value | store one support anchor — the byte-scan assertion must fail |
| I3 | The envelope is closed at the declared keys | add any seventh envelope key — the key-set assertion must fail |
| I4 | Records are append-only: an existing record is never rewritten | rewrite in place on a second build with different content — the duplicate-identity refusal must fail |
| I5 | One record per identified evaluation, named by the evaluation's own input digest | name the file by the as-of instant — the two-builds-one-record test must fail |
| I6 | Nothing is ever pruned | discard the oldest record above any threshold — a "no record is ever removed" test must fail |
| I7 | Every write lands inside the daemon's state directory and nowhere else | point the writer at the repository root or at the observed project's root — the containment test must fail |
| I8 | Directory mode `0700`, file mode `0600` | write with mode `0644` — the posture test must fail |
| I9 | Absent history and unreadable history are distinguishable, and neither renders as "no change" | read a corrupt record as an empty history — the fail-closed test must fail |
| I10 | The retained-record count and on-disk byte total are rendered | render the page with the total omitted — the copy-oracle assertion must fail |
| I11 | Nothing is served from the record: no new route exists | add a route that answers with a retained record — the route-population test must fail |
| I12 | The stored tuple is compared field by field, including challenge | compare on the label alone — a challenge-only difference must still be caught |

I7 and I11 are the two that keep this direction's boundary mechanical
rather than editorial. I6 is the one that makes "unbounded" a tested
property instead of an omission.

## The doctrine test

Every clause below is quoted from `.syzygy/governance/doctrine/` at its
own site, located through `DIRECTIVE-REGISTER.md`; none is paraphrased,
and no clause is summarized and then quoted as if whole.

**VIS-6 is the warrant, and it is quoted entire.** `vision.md` lines
167–181:

> **VIS-6 — Syzygy is derived, with two closed exceptions.** Every fact
> Syzygy holds must be rebuildable from the artifact that owns it; its
> databases and views are projections, and content it authors is
> committed out to the governed plane, which becomes the authoritative
> source. The exceptions, closed: (a) the owner's **personal presentation
> state** (layouts, filters, bookmarks, unpromoted notes), which may never
> affect truth, work, status, or certificates — promoting a note into
> governance (an annotation or a dismissal) commits it out to the
> governed plane, attributed and reasoned, dismissals carrying an expiry
> (a dismissal without a reason current at the evaluation's as-of instant
> renders the gap again — expiry acts only through a new identified
> evaluation, architecture.md); (b) **observation records** — historical
> evidence, immutable, evaluation-identified, marked stale, exempt from
> rebuildability. *Violation:* any other fact living only inside Syzygy; a
> view preference influencing a status claim; a dismissal taking effect
> without living in the governed plane.

`[Inferred]` Exception (b) is what makes a durable evaluation store
something other than a VIS-6 violation: an observation record is exempt
from rebuildability, which is the whole of the warrant. It gives three
obligations with it — **immutable** (invariant I4), **evaluation-
identified** (the envelope), **marked stale** (the staleness clause
below) — and it gives no retention bound, which is why the bound was
yours to set and why "unbounded" and "immutable" are the arm that does
not destroy historical evidence doctrine has just exempted from
rebuilding.

**The retention and staleness clauses of `trust-and-evidence.md` carry no
identifier**, so they are cited by file and line. Lines 10–16, stopping
mid-line where the sentence ends — the definition the record must satisfy
to be evidence at all:

> **Evidence is a durable, identified, integrity-verifiable artifact
> carrying its source, capture time, scope, and provenance** — a test
> run, a tool exit status, a file hash, a commit SHA, an observation
> record, a captured runtime trace or incident record. **Reproducibility
> is a separately declared property of an evidence class, not a
> prerequisite for evidence status**: a one-off runtime observation or
> anomalous external response, durably captured and identified, is
> evidence.

Lines 99–107, the staleness rule, whole:

> An **observation record** (the immutable result of an identified status
> evaluation — source snapshot + as-of instant, architecture.md) may
> still be displayed after its evaluation is superseded, but its
> staleness must be visible on the primary surface, not buried in
> drill-down; it cannot contribute to a current convergence certificate
> *(future-tagged, post-V1)*; and it cannot silently remain green.
> Staleness itself is judged at the current evaluation's as-of instant,
> never by an ambient wall clock. Broken observers degrade to their
> last-good observation record, clearly marked stale/broken; they never
> fail invisibly.

`[Inferred]` Two consequences the direction states rather than leaves to
the implementer: a retained record is superseded the moment a later
evaluation exists, so nothing rendered from one may be rendered as
current; and every time-sensitive judgment over retained records is
computed at an evaluation's own as-of instant, never at the wall clock.

**VIS-2 bounds what the retained record may be used to say.**
`vision.md` lines 96–106:

> **VIS-2 — No evidence means Unknown, not success.** No surface may
> declare a project aligned, converged, or genome-complete — nor turn
> anything green — without current evidence. Evidence is a durable,
> identified, integrity-verifiable artifact (trust-and-evidence.md;
> reproducibility is a declared property of an evidence class, not a
> prerequisite); aligned, converged, and genome-complete are defined in
> architecture.md. Currency is judged at a status evaluation's identified
> as-of instant (architecture.md) — the wall clock never silently changes
> a displayed status. Until a claim class declares its currency bound,
> its evidence is not current and the claim renders Unknown. *Violation:*
> "spec-aligned ✓" computed from a stale index; a stale view silently
> green; a status flipping with no new identified evaluation.

`[Inferred]` Applied at the smallest scale, this is invariant I9: *no
history* and *no change* are different states, and a surface that
rendered the first as the second would be a stale view silently green.

**SEC-5 bounds what the record may contain.** `security.md` lines 54–60:

> **SEC-5 — Secrets are never indexed.** Observation applies a declared
> secret-detection policy (`.syzygy/governance/`); content matching it is
> excluded and the exclusion is rendered; content that cannot be
> classified is excluded, not indexed — unclassifiable fails closed. A
> secret reproduced in any Syzygy surface, store, or endpoint is a
> trust-floor violation (trust-and-evidence.md, floor bullet 4).
> *Violation:* a connection string appearing in a map tooltip or API
> response.

`[Observed]` The retained record is a new store in SEC-5's sense. It is
kept clean by construction — it is a projection of the served model, and
the fields that could carry source content are the two the direction
excludes — and by invariant I2, which tests it rather than assuming it.

**SEC-4** is quoted and read above, under "Where it lives": it is the
clause a promoted note would have to satisfy, and promotion is exactly
what this direction does not authorize.

**The temporal rule is the clause that keeps a retained record from
becoming a clock.** `architecture.md` lines 221–229:

> **Time is an explicit input, never an ambient one.** A **status
> evaluation** is identified by the pair (source snapshot, **as-of
> instant**); every time-sensitive judgment — evidence currency,
> staleness, dismissal expiry — is computed at the evaluation's as-of
> instant. A wall clock never silently alters a displayed status: the
> passage of time changes a status only through a new identified
> evaluation, and it may only degrade a claim (toward stale or Unknown),
> never establish or improve one — **improvement requires a new source
> snapshot containing a permitted authoritative input, such as new
> evidence or an adjudication result**.

And lines 231–235 say what an observation record is, which is what the
retained file must be:

> An **observation record** is the immutable result of one identified
> evaluation and contains deterministic facts only. Determinism (VIS-7)
> is asserted per identified evaluation, over the deterministic observed
> graph and base layout — **including logical freshness state (fresh,
> stale, broken, superseded), which changes status and is therefore
> identity-bearing**.

`[Inferred]` The record stores freshness rather than recomputing it for
exactly this reason: freshness is identity-bearing, so a record that
dropped it would not be the result of the evaluation it names.

## What is the drafter's and not yours

Listed so you can take any of them back. `[Inferred]` on all four.

1. **The envelope's key set** (schema name, evaluation identity, observer
   revision, observed revision, two counts). Your ruling closed the
   per-claim payload at three fields and said nothing about the envelope;
   the drafter closed it at six keys because VIS-6(b) requires an
   observation record to be evaluation-identified.
2. **The disclosure timing.** Your ruling says the on-disk total renders
   "beside the delta"; the delta is slice 2. The drafter's reading makes
   the count and total render from the first retained record, so
   retention is never silent. The alternative is yours.
3. **The invariant list.** Twelve rows, offered as the implementing
   bead's acceptance floor rather than as authorization text.
4. **Nothing else.** The three retained fields, the unbounded retention,
   the location and every exclusion come from your P-79 ruling and from
   the acts in force.

**And one number that is explicitly *not* in this direction.** The delta
band's row cap is your P-79 **Q3**, and it is chosen at **slice 2**, when
the band is designed and its bytes can be measured against the page's
measured headroom. This direction neither sets it nor constrains it, and
an implementer may not read a cap into it.

## The proposed direction text

This is the text the direction would carry. It is offered for you to
issue, edit or decline; as printed here it is candidate text and binds
nothing.

```
OWNER DIRECTION — RETENTION POSTURE FOR RETAINED POLARIS EVALUATION
RECORDS

Date: <the day you issue it>
Owner: Tzeusy
Continues: decisions/PWB-IMPLEMENTATION-AUTHORIZATION-ACT.md and
decisions/PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md, whose
retention-posture escalation trigger this direction answers and does not
widen.

1. WHAT IS AUTHORIZED. The Three-Surface POC daemon may retain, in its
   own state directory, one durable record per identified evaluation.
   Per claim, that record holds exactly three things: the claim
   identity, the epistemic tuple, and the challenge state. Once per
   record it holds the schema name, the evaluation identity (snapshot,
   snapshot label, inputs digest, as-of instant), the observer revision,
   the observed project's revision, and the two counts (claim objects
   and distinct claim identities). Nothing else.

2. WHAT IT MAY NEVER HOLD. No source body or body bytes of any kind; no
   support anchor; no resolution route; no credential or secret
   material; no content the approved secret-classification policy
   excludes or cannot classify. The approved policy's retention clause
   is unchanged by this direction and remains binding.

3. WHERE IT LIVES. The daemon's own state directory only, under the same
   directory and file modes the existing records there use. Never in an
   observed repository. Never in openspec/** or .syzygy/**. No record is
   committed out to any governed plane.

4. HOW LONG IT LIVES. Unbounded. No record is pruned, discarded,
   overwritten or rewritten. A record under an evaluation identity that
   already exists with different content is refused, not replaced.

5. DISCLOSURE. From the first build that retains a record, the surface
   renders the number of retained records and their total on-disk bytes;
   when the claim-state delta band lands, that total renders beside it.
   Retention is never silent.

6. HONESTY OBLIGATIONS CARRIED IN. A retained record is an observation
   record under VIS-6(b): immutable, evaluation-identified, and marked
   stale once superseded. No judgment over a retained record is computed
   against a wall clock; every one is computed at an evaluation's own
   as-of instant. An absent history and an unreadable history are
   distinct states and neither renders as "no change".

7. WHAT THIS DOES NOT AUTHORIZE. No dismissal and no widening of the
   challenge vocabulary — that is a specification amendment needing its
   own semantic delta, review and act. No promotion of an owner note, no
   annotation, and no write of any kind into an observed repository or
   into any governed plane; the observer registry entry's empty write
   surface stands. No new served route, no listing or download of a
   retained record, and no new or relaxed response ceiling. No second
   repository, no wider content class, no consent amendment, no egress,
   no observed-code execution, no deployment, release or mission effect,
   no doctrine or contract change, no autonomous adoption. Every
   exclusion of the 2026-09-02 authorization and its 2026-09-05
   continuation is retained unchanged.

8. WHAT THIS IS NOT. This direction binds no artifact digest, amends no
   specification, policy or registry byte, adds no row to the
   acceptance-act record and registers nothing. It is a warrant, not
   evidence: it proves no read, no write, no render and no result.

9. WITHDRAWAL. This direction may be narrowed or withdrawn at any time
   by a later direction. Withdrawal defeats grant: on withdrawal the
   daemon retains no further record, and what to do with records already
   written is a question for that later direction.
```

**The wording that would issue it**, if you prefer to reply rather than
to write the text yourself. Replying with this line, in your own session,
is what a recorder would quote verbatim:

```
Authorize retained Polaris evaluation records as drafted: claim identity, epistemic tuple, challenge state only, unbounded, in the daemon's state directory
```

Any other wording, a partial answer, or silence authorizes nothing. This
line is **not** an act phrase: it binds no digest, it is registered in no
governance check, and no recorder script exists or is needed for it.

## The record the recorder would write, and what it would not do

**The record file** would be
POLARIS-RETAINED-EVALUATIONS-RETENTION-POSTURE-DIRECTION.md, in this
directory, in the shape of
`POLARIS-TRUSTED-BOOTSTRAP-OBSERVATION-DIRECTION.md`. **This packet does
not write it, and no such file exists.** It would carry: the date, the
owner, the repository state at recording, the owner's words quoted
byte-for-byte, the direction text as issued, and — labeled as the
recorder's and not the owner's — the reading of its scope.

**What recording it would *not* touch**, stated because a reader who has
seen the digest-bound acts will expect otherwise: no manifest, because no
bytes are bound; no dedicated recorder script, because there is no phrase
to validate against a frozen subject; no `ACCEPTANCE-ACT-RECORD.md` row,
because no acceptance transaction occurs; no entry in
`scripts/check_governance.py`'s act-subject or act-digest-copy
registries, because neither has anything to see. `[Observed]`
`check_governance.py` was run over this packet in the drafting session and
reports no rule that a decision packet in this directory must satisfy
beyond the rules every tracked Markdown file satisfies.

`[Inferred]` The one downstream bookkeeping consequence: the gate bead
`syzygy-dov.28` closes when the direction is recorded, which unblocks the
slice-1 bead. This packet files no bead and closes none.

## Provenance of the figures quoted here

`[Observed]` Every measured figure in this packet — the per-evaluation
byte cost, the 26,348-byte route redundancy, the claim-identity counts and
their split — is quoted from
`docs/design/POLARIS-M12-RETAINED-EVALUATIONS-FUNNEL.md`, which computed
them at Syzygy commit `a9f671e` and carries their predicates. **None was
re-measured in this drafting session**, and no claim here rests on a
"zero", "all" or "100%" sweep of its own. Where this packet and that
funnel packet disagree about a number, the funnel packet is the one with
the method written down.

`[Unknown]` Whether the population those figures were measured over is
the population the first retained record will see. The observed project's
content moves; the implementing bead re-measures the on-disk cost at the
commit it lands on, and the disclosure obligation in clause 5 is what
makes the real number visible rather than the estimate.
