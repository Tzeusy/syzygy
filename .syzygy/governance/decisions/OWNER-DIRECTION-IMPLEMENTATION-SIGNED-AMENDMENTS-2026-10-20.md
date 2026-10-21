# Owner direction — implementation of five more signed PWB amendments (2026-10-20)

Date: 2026-10-20 (the owner's answer); recorded 2026-10-21

Owner: Tzeusy

Decision ID: `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-20`

Predecessor: `OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md`
(this directory), which stays in force unchanged. This record adds rows; it
narrows, edits and withdraws nothing in that one.

This is a plain owner direction in the sense of `PROCESS-GLOSSARY.md`, in
the family of `PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md` and the
2026-10-15 predecessor. It binds no artifact digest, adds no row to
`ACCEPTANCE-ACT-RECORD.md` and registers nothing in
`scripts/check_governance.py`. It signs nothing, and it edits no signed
byte.

**In force only once the owner confirms it.** The owner gave the answer on
2026-10-20. Everything below that is not a quotation is the recorder's
reading: the mapping from each option to one signed version, the beads, the
shared-model classifications, the chain order and the sequencing against
`syzygy-dov.19`. The owner confirms that reading through the lead session's
owner questionnaire. A GitHub approval cannot carry it, because the pull
request is authored from the owner's own account. Before merge, the lead
adds one dated line in the "Owner confirmation" section below. No lane
starts on this record until that line exists and the file is on `main`.

## Owner confirmation

"Confirmed by the owner on 2026-10-21T11:59:04+00:00, channel owner via
questionnaire web form (token-gated, from 127.0.0.1), over commit
8c334f67e6883a5d229bf04512c65eeaa878a5ea, record SHA-256
f669546c788d5ed598b916cf1369d58b65e1825bd53adc33dec2b2f2ab963166."

- `<commit>` is the commit that carries the bytes the owner was shown.
- `<sha256>` is the SHA-256 of this file at that commit, computed by script
  before the line is added.

Any correction the owner makes is applied to the body of this record first,
at a new commit. The owner is then shown those bytes, and the line names that
commit and its digest. A correction is never listed beside the line.

## The owner's words

[Observed: the lead Claude Code session, 2026-10-20, a structured question
(AskUserQuestion) with the owner present, asked 14:03Z and answered 14:05Z.
The question, option texts and answers below are copied from that session's
own record of the call. The owner's local questionnaire for
2026-10-20 (in `.syzygy/local/`, git-ignored; item
`dov35-impl-authorization`) logs the same answer in its "Owner decision log"
row.] The question had two parts, each multi-select.

### Part 1

The question:

> Decision 3 of 6 (syzygy-dov.35, P2): your 2026-10-15 direction authorized implementation of P-96/97/86/100/99/98 and tree-framing. Which of the other signed PWB amendments should I authorize for implementation? Each authorization is exactly the signed text, the same bounds as 10-15 (one Butlers repo, no new content class/read/egress, no observed code), placed in the shared-model WIP-one chain after tree-framing. Dependents that also need acts or a registry amendment stay blocked.

The options offered:

> - **Machine-view**: PWB machine-view amendment (act line 86 says no implementation).
> - **Opening-band**: Opening-band scenario (M4 slice 3); touches shared model.surfaces.
> - **Exact-source render-mode**: M14 exact-source render-mode amendment.
> - **Dismissal + item-depth**: The two sign-offs of 2026-10-01/02 that cover dismissal and item depth.

The owner selected:

> Machine-view, Opening-band, Dismissal + item-depth

### Part 2

The question:

> Same decision, second part: the two amendments tied to the registry-entry act (P-74 Q2 puts that act before slice 5's last limb).

The options offered:

> - **Missing-currency**: PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0 (bead dov.8.2).
> - **Container-shape profile**: PWB-CONTAINER-SHAPE-PROFILE-AMENDMENT-SIGNOFF-v1.0 (bead dov.8.3).

The owner selected:

> Missing-currency, Container-shape profile

### Two corrections to the question's own labels

- **The beads named in part 2 are wrong.** `syzygy-dov.8.2` and
  `syzygy-dov.8.3` are both M8 container-shape work. Neither implements the
  missing-currency scenario. [Observed: the questionnaire's background for
  this item names them as container-shape beads; `syzygy-dov.8.2`'s notes,
  2026-10-03, say it must be re-shaped over the signed container-shape
  amendment; `syzygy-dov.8.3` follows `syzygy-dov.8.2`.] The
  missing-currency scenario's implementation is M2 slice 5,
  `syzygy-dov.2.2`. This record maps each option to an amendment by the
  sign-off record or act that the option names, never by the bead label.
- **Missing-currency is tied to a continuation act, not to P-74 Q2's registry
  act.** See "Selected but not authorized here" below.

## What each selection maps to

Each option names exactly one signed version, except "Dismissal + item-depth",
which names two sign-offs in its own text. No option maps to no signed
version, and none is open to more than one reading. [Observed:
`git tag -l 'pwb-*'` returns one tag for each of the six; each package has
one sign-off record or act in this directory.]

| Option | Register row | Signed version (tag) | Sign-off record or act |
|---|---|---|---|
| Machine-view | P-72 Q1, with P-76 Q3 folded in | `pwb-machine-view-amendment-signed-2026-10-02` | `PWB-MACHINE-VIEW-AMENDMENT-ACT.md` (its "authorizes no implementation" sentence is at line 86, which the option cites) |
| Opening-band | P-71 Q7 | `pwb-opening-band-scenario-signed-2026-10-01` | `PWB-OPENING-BAND-SCENARIO-ACT.md` |
| Dismissal + item-depth (dismissal half) | P-79 Q5 | `pwb-dismissal-expiry-amendment-v1.0` | `PWB-DISMISSAL-EXPIRY-AMENDMENT-SIGNOFF-v1.0.md` (2026-10-02) |
| Dismissal + item-depth (item-depth half) | P-81 Q5 | `pwb-item-depth-amendment-v1.0` | `PWB-ITEM-DEPTH-AMENDMENT-SIGNOFF-v1.0.md` (2026-10-02) |
| Missing-currency | P-69 Q7a | `pwb-missing-currency-disclosure-scenario-v1.0` | `PWB-MISSING-CURRENCY-DISCLOSURE-SCENARIO-SIGNOFF-v1.0.md` (2026-10-02) |
| Container-shape profile | none of its own (N8, gate `syzygy-u05.8`; drafted on the owner's 2026-09-26 answer) | `pwb-container-shape-profile-amendment-v1.0` | `PWB-CONTAINER-SHAPE-PROFILE-AMENDMENT-SIGNOFF-v1.0.md` (2026-10-02) |

The register rows are those of
`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`; that is where the rows
live now.

## What is authorized

Implementation, under the normal implementation workflow, of exactly the
signed text of each amendment below. "Signed" means the version named by its
tag and its record in this directory. Nothing is included that a package's
notes, open dispositions or unanswered questions would add.

| Register row | Amendment (tag) | Sign-off record or act | State on 2026-10-21 | Implementation bead | Shared model? |
|---|---|---|---|---|---|
| P-72 Q1 / P-76 Q3 | PWB-REQ-020 machine-view categories (`pwb-machine-view-amendment-signed-2026-10-02`) | `PWB-MACHINE-VIEW-AMENDMENT-ACT.md` | signed 2026-10-02; covered on confirmation | `syzygy-dov.10.3`, `syzygy-dov.7.2` (fenced, below); `syzygy-dov.11.2` only has its wait removed and is not authorized here (Bounds); not `syzygy-dov.5.2` | no (a reading, below) |
| P-71 Q7 | PWB-REQ-010 opening-band aggregate (`pwb-opening-band-scenario-signed-2026-10-01`) | `PWB-OPENING-BAND-SCENARIO-ACT.md` | signed 2026-10-01; covered on confirmation, **M4 slice 3 only**, without any count of members under the no-bound condition (which waits for `syzygy-dov.19`'s act; see below) | `syzygy-dov.4.2`, slice 3 | yes |
| — (N8) | PWB-REQ-002 container-shape profile (`pwb-container-shape-profile-amendment-v1.0`) | `PWB-CONTAINER-SHAPE-PROFILE-AMENDMENT-SIGNOFF-v1.0.md` | signed 2026-10-02; covered on confirmation, M8 slice 5 limbs 1–4 and slices 1, 3, 4 and 6 (design) only | `syzygy-dov.8.2`, then `syzygy-dov.8.3` | `syzygy-dov.8.3` yes; `syzygy-dov.8.2` no |
| P-81 Q5 | PWB-REQ-015 item depth (`pwb-item-depth-amendment-v1.0`) | `PWB-ITEM-DEPTH-AMENDMENT-SIGNOFF-v1.0.md` | signed 2026-10-02; covered on confirmation, but **sequenced after `syzygy-dov.19`'s act**: its text cannot be split from the missing-currency disclosure (below) | `syzygy-dov.14.4` | yes |
| P-79 Q5 | PWB-REQ-007 dismissal with live expiry (`pwb-dismissal-expiry-amendment-v1.0`) | `PWB-DISMISSAL-EXPIRY-AMENDMENT-SIGNOFF-v1.0.md` | signed 2026-10-02; covered on confirmation, no-home arm only, other behaviour on synthetic fixtures (Bounds); its bead has other open blockers | `syzygy-dov.12.3` | yes |

**How "shared model" is decided.** The test is the 2026-10-15 rule: a row
joins the chain if it changes the shared Three-Surface POC model
(`packages/three-surface-poc-core`, `PocModel`) or is computed against its
machine answer. It is applied as written to every row except machine-view,
where it is read narrowly and the reading is stated for the owner to
confirm. The evidence for each row:

- **Machine-view: no.** The package's impact ledger names the implementation
  sites: `apps/three-surface-poc/src/routes.ts`, the route's derivability
  test, and new view modules. The one core file it names,
  `project-shape-observation.ts`, is touched only for the briefing ceiling,
  which belongs to `syzygy-dov.5.2`, and that bead is not released here. No
  derived view adds a field to the machine answer. Each one reads the answer
  as it stands, and its oracle checks against that answer. The review brief
  also says a generated draft "is not composed from the machine answer".
  **This is a reading, and it narrows the 2026-10-15 rule.** That rule
  takes in any row "computed against its machine answer", and a derived view
  is computed against it. The narrower reading counts only rows that change
  the model or the answer. It follows P-77, whose row in
  `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md` gives the slot to M10's
  digest field and puts "the route table and conditional GET after it; the
  schema document additionally after P-72's delta". The same record's
  cross-cutting order (line 81) names only the digest field as taking the
  slot "next", and says "Nothing else touches `PocModel` while either is
  open". [Inferred, from those sources. The owner confirms or overrules this
  reading at confirmation. If overruled, the machine-view beads join the
  chain directly after tree framing, ahead of opening-band, in the order
  `syzygy-dov.10.3`, `syzygy-dov.11.2` (position only; its authority is
  P-78, under Bounds), `syzygy-dov.7.2`.]
- **Opening-band: yes.** The scenario's last bullet requires that "the
  machine answer carries the same aggregate under PWB-REQ-020" (the
  package's `SEMANTIC-DELTA.md`, quoting the signed patch), and the option
  text itself says the change "touches shared model". [Observed]
- **Container-shape: `syzygy-dov.8.3` yes, `syzygy-dov.8.2` no.** Limbs 1–4
  thread a profile parameter through the core extraction and coverage
  modules, whose current constants remain the default. Those modules feed
  `PocModel.projectShape`, the same class of change as P-86 in the
  predecessor chain. `syzygy-dov.8.2` touches the app's governance-input and
  Git-binding code, a report-only probe, a schema document and a design.
  None of these is a model change. [Inferred, from the beads' designs and
  the package ledger's Table 2]
- **Item-depth: yes.** The package ledger's first future consumer is
  `packages/three-surface-poc-core/src/project-shape-model.ts`, which must
  "carry a separate fixed-role item-to-intent relation identity and tuple".
  [Observed]
- **Dismissal: yes.** Dismissal records become identified inputs to an
  evaluation (ledger row RFC2-1.r3), and `dismissed-by-decision` "travels
  beside the unchanged tuple in machine views" (row RFC6-14.r4). [Observed]

## The WIP-one chain, extended

The 2026-10-15 chain stands as written: P-97 (`syzygy-u05.19`) → P-100
(`syzygy-u05.20`) → P-86 (`syzygy-dov.15.2`) → P-96 (`syzygy-u05.21`) →
tree framing (`syzygy-73e.20`). The shared-model rows here are appended
after tree framing, in this order:

1. opening-band, M4 slice 3 (`syzygy-dov.4.2`);
2. container-shape limbs 1–4 (`syzygy-dov.8.3`), after `syzygy-dov.8.2`
   lands outside the slot;
3. M12 slices 1–2 (`syzygy-dov.12.1`), position only;
4. dismissal (`syzygy-dov.12.3`);
5. item depth (`syzygy-dov.14.4`), not before `syzygy-dov.19`'s act is
   performed (see "The missing-currency disclosure" below).

**A link whose own gate is still open yields the slot** to the next link in
this order that can start. It takes the slot back at its listed place once
its gate closes.

**Link 3 is placed here and authorized by nothing here.** `syzygy-dov.12.1`'s
own notes mark it "Shared-model: WIP-one". Its authority is P-79 together
with the 2026-09-23 retention-posture direction, and its lane is stopped for
the owner on two retention questions. It is placed here so the slot has a
stated holder when those questions are answered. It runs immediately before
dismissal, because `syzygy-dov.12.3` depends on it.

**Why this order.** It starts from the order the amendments were signed and
applied: the opening band on 2026-10-01, then dismissal, container shape and
item depth on 2026-10-02, each regenerated over the one before. Two changes
follow from gates:
- Dismissal sits behind container shape, with link 3 ahead of it, because
  its bead also waits on `syzygy-dov.12.1`.
- Item depth is last because it waits for `syzygy-dov.19`'s act.

[Inferred: the recorder's ordering; the owner may reorder at confirmation.]
The rows that do not touch the model (the machine-view beads, on the reading
above, and `syzygy-dov.8.2`) are outside the chain.

## Selected but not authorized here

**Missing-currency (`pwb-missing-currency-disclosure-scenario-v1.0`).** The
owner selected it. This record does not authorize its implementation bead,
M2 slice 5 (`syzygy-dov.2.2`), because a plain direction cannot supply what
that slice needs. How the same gate holds parts of the authorized rows is
stated below.
[Observed] The signed package's own `OWNER-DECISION-PACKET.md`
§"Remaining separate gates for M2 slice 5" says that, even after the
specification act, slice 5 stays blocked on three gates. The first, the
registry act at `.18`, was performed 2026-09-30. The other two are open:

> - the plain implementation-continuation direction at `.19`;
> - a fresh implementation authorization that resolves the five disclosed
>   contract-coverage gaps and names the exact built behavior.

`syzygy-dov.19` requires an exact phrase. Its design reads: "The owner must
reply with one exact offered phrase; silence, “Agreed,” the 2026-09-21
option ruling, merge, CI, or another act continues nothing."

In the bead graph, the only open blocker of `syzygy-dov.2.2` (M2 slice 5) is
`syzygy-dov.19`. The packet's third gate, the gap-resolving authorization,
has no bead. The owner's selection supplies neither: it carries no exact
phrase and resolves none of the five gaps. The owner's choice is therefore
routed to `syzygy-dov.19`, to be offered as that bead's exact act. Until
then, M2 slice 5 stays unbuilt and the signed behaviour stays in force.

### The missing-currency disclosure: every use waits for `syzygy-dov.19`'s act

**Rule.** No row of this record builds any part of the missing-currency
scenario. That includes the per-claim reason, route and outside-slot
disclosure, and the aggregate count of members under the no-bound condition.
Any part of an authorized row that needs them waits until `syzygy-dov.19`'s
act is performed. It is then built only as far as the behaviour that act
names; anything beyond that is an escalation.

[Observed] The reasons:

- The missing-currency packet says the act "does not weaken those contracts
  or authorize implementation across the gaps" (`OWNER-DECISION-PACKET.md`,
  §"Owner-visible consequences", item 1).
- The five gaps are the contract rows RFC6-14.r1, RFC6-14.r3, RFC6-17.r1,
  RFC7-16.r1 and RFC7-33.r1. The package's `SEMANTIC-DELTA.md` (lines
  121–125) says they are "no longer honestly `covered:PWB-REQ-007`" and that
  its repair delta marks each one `unknown-uncovered`.
- The gap-resolving authorization is the drafted `syzygy-dov.19`
  continuation, which an owner act has not performed.

**Item depth (`syzygy-dov.14.4`) is sequenced after `syzygy-dov.19`'s act.**
It cannot be built as "exactly the signed text" before then, because the
text cannot be split from the disclosure:

- PWB-REQ-015 says "Each contract band SHALL carry an item-to-intent
  relation claim".
- While the claim's class has no effective bound, every relation claim must
  be "Unknown with the single primary reason `no-currency-bound-declared`,
  its exact resolution route and the outside-slot disclosure PWB-REQ-007
  requires".
- The class `governing-intent-relation` is not among the 13 classes the
  registry entry declares a bound for. [Observed: the `currencyBounds` list
  in `.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`]
- So every relation claim is under the condition.

Building item depth without the disclosure would build less than the signed
text, so it waits. It starts only once two things hold:

- `syzygy-dov.19`'s act is performed;
- the behaviour that act names covers the relation claims.

If that act does not cover them, the lane escalates. [Observed: the drafted
continuation package, `pwb-m2-slice5-implementation-continuation` in draft
PR #492 at `268f1773`, names neither item depth nor the opening band in any
of its three files.]

**Opening band, M4 slice 3 (`syzygy-dov.4.2`), may be built before that
act**, without any count of members under the no-bound condition. The
scenario reaches an aggregate only through its last bullet: "an aggregate
that has a member under this condition discloses, apart from its
per-freshness-state counts, the count of members under this condition".
Under the current model no project-shape claim is under the condition, so
the band has no member that bullet would count. [Observed: both claim
constructors in
`packages/three-surface-poc-core/src/project-shape-model.ts`,
`observedClaim` and `unknownClaim`, set `freshness: FRESH` on every claim.]

The band reads each member's freshness as the model supplies it, and builds
no count arm for the condition. If a member under the condition ever reaches
it, the band renders nothing; the act says "Nothing requires the band to be
built". The count arm is then built only after `syzygy-dov.19`'s act, as far
as that act names.

**A mismatch that exists before this record.** The registry entry in force
declares 13 per-class currency bounds, adopted 2026-09-30. The code reads
none of them:

- `PocEvaluationEvidence.currencyBounds` is typed `readonly []`, and its
  comment says it "stays empty until the separately gated owner-act slice
  5" (`packages/three-surface-poc-core/src/model.ts`, lines 152–159).
- Every project-shape tuple carries the constant `FRESH`.

So today's freshness values are not derived from the declared bounds, and
the classes with no bound do not render the no-bound condition. [Observed]

This record neither repairs nor relies on that mismatch. Repairing it is M2
slice 5's deliverable (`syzygy-dov.2.2`), behind `syzygy-dov.19`. The opening
band's freshness counts reproduce the members' values, mismatch included.
That is disclosed here rather than claimed as derived.

The per-claim `freshness-absence` span in
`apps/three-surface-poc/src/polaris.ts` predates this record. It was built
2026-09-23 under P-70 for M3 (`syzygy-dov.3.1`) and is neither extended nor
reused for a new claim class here. [Observed]

**Exact-source render-mode (`pwb-exact-source-render-mode-amendment-signed-2026-10-02`).**
Not selected and **not authorized**. `syzygy-dov.14.3` stays blocked.

## Bounds

Every bound here holds for every row above.

- **Exactly the signed text.** No requirement, scenario or behaviour beyond
  it. Not authorized:
  - M4 slices 4 and 5 (the opening-band act, lines 87–89, keeps them gated
    elsewhere);
  - M8 slice 5 limb 5 (`syzygy-dov.8.4`, waiting on the registry-entry act
    `syzygy-dov.24`) and slice 2 (`syzygy-dov.8.5`, behind it);
  - any briefing route (`syzygy-dov.5.2`; the machine-view act keeps the
    briefing member unservable until its route is separately authorized,
    and the 2026-09-30 registry fields stay unread until `syzygy-dov.19`);
  - the exact-source render-mode amendment;
  - any part of the missing-currency scenario, in any row, before
    `syzygy-dov.19`'s act (above);
  - `syzygy-dov.11.2`, which this record does not authorize (next bullet).
- **Machine-view fences.**
  - The status machine route (`syzygy-dov.11.2`) is in neither signed
    category. Under PWB-REQ-020 a route enters a category "only by a later
    amendment to this specification naming it as a member", and "A route in
    neither category is neither admitted nor forbidden by this requirement".
    [Inferred: the recorder's reading of those two sentences.] The route's
    authority is therefore P-78 (ruled 2026-09-21), under the PWB
    implementation act as continued 2026-09-05
    (`PWB-IMPLEMENTATION-AUTHORIZATION-CONTINUATION-ACT.md`). This record
    only removes the wait on P-72's category ruling, which is now signed.
  - The draft view (`syzygy-dov.7.2`, `/polaris/draft/<runId>`) is built
    only as far as the signed category text goes. The machine-view act
    (lines 90–92) leaves "The second category's record-level fields and its
    relation to the exact-source anchors" to "the later route amendment
    that names the member". Neither may be designed or shipped on this
    record. A lane that needs either one stops and escalates.
    `syzygy-dov.7.2` is probably not buildable until that later route
    amendment is signed; its lane is expected to stop at this escalation.
    [Inferred]
- **Ceilings before members.** A machine-view member that needs a ceiling of
  its own is not served before the registry entry's resource envelope
  declares it, as the signed text says. A lane that finds the draft view
  `/polaris/draft/<runId>` needs a ceiling not yet declared stops there.
- **Dismissal adds no write and no retention change.** The signed package
  leaves open questions 2 (where dismissal records live and who writes them;
  "write act deferred") and 7 (whether keeping a dismissal reachable from a
  retained evaluation is a retention change). This record answers neither.
  [Unknown: whether the 2026-10-02 selection "Sign off v1.0 (Recommended)"
  answered them; its record quotes only the selection.] The build uses only
  the signed no-home arm: "When an evaluation cannot read that record set,
  or no governed-plane home for dismissal records is designated, it
  dismisses no claim and SHALL disclose its dismissed count and the count of
  each record class below as Unknown, never as zero" (PWB-REQ-007,
  "Dismissal records"). Every other dismissal behaviour is exercised only on
  synthetic fixtures. No lane may:
  - build a write path for dismissal records;
  - read dismissal records from Butlers;
  - choose, designate or hard-code a governed-plane home for dismissal
    records in code or configuration (question 2's "where" half);
  - decide that dismissal bytes stay reachable from a retained evaluation,
    or re-read a dismissal through a retained evaluation (question 7);
  - change what the 2026-09-23 retention direction keeps.

  The retained re-read limb stays **unbuilt**, on fixtures as well as live.
  It is the clause of "A dismissal lapses only through a new evaluation"
  that says "reading the first evaluation again after the expiry instant has
  passed renders the same claim state". It depends on question 7, so a lane
  that reaches it stops and escalates. The scenario's other limbs run on
  synthetic fixtures only.

  If the signed text cannot be built without one of the items in the list
  above, that is an escalation.
- **No new Butlers content class, body read or provider egress.** Butlers
  bodies are read only as the acts in force already allow: the consented
  class `declared-project-shape-text`, behind the implementation's
  PWB-REQ-005 evaluation. A case the signed text names but Butlers may not
  exhibit (a second container shape, a dismissed claim) is tested on a
  synthetic fixture, never by a new read.
- **The daemon executes no observed code.** Separate operator commands run
  tests.
- **Shared-model changes WIP one**, in the chain order above.
- **Every lane reviewed and verified per craft-and-care.** Each signed oracle
  passes as tests whose expected values are independent of the module under
  test; each falsifier limb has a rule-6 mutant that fails; the battery is
  run at a committed tree (rule 7); any change to the size of `/polaris` is
  measured against the ceiling.
- **Escalation.** A lane that finds the signed text cannot be built as
  written stops and returns to the owner: an amendment travels under
  CC-REV-2 and needs its own sign-off. No release, deployment, second
  repository, write into Butlers, or act-bound byte edit.
- **Withdrawal.** A later direction may narrow or withdraw this one;
  withdrawal defeats grant.
