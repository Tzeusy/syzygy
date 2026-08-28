# Semantic delta 3 — focused specification acceptance and honest impact evidence

## Before and after, in plain language

**Before:** the specification policy explained how to accept a whole
capability but did not say how to accept one focused change to an already
accepted capability. It also used *warrant* for requirement provenance without
making clear that permission to start work is a separate question. Several
reader-facing passages carried old counts, a stale cross-reference, an
incomplete examples list that read as complete, and a historical exercise
result that the policy subject did not itself let a fresh reader verify.

**After, if the owner adopts this exact proposal:** a specification change must
declare whether acceptance covers the whole capability or one focused change,
and each unit has an explicit coverage population. The six provenance fields
remain closed; a confirmed finding may warrant corrective work through
RFC1-25's `motivates` edge but does not become a seventh provenance field.
The durable rules remain in the policies, while volatile measurements and
review provenance live in this record. The two policies make authority state
conditional on the active act record: proposal when no act names the exact
digest, confirmed successor from an act that does.

> **Authority boundary.** At this authoring revision no performed owner act
> names the edited policy digests, so they remain proposals. If a later act
> names those exact reviewed digests, the policies become confirmed successors
> without an edit. Drafting authorization is not review, adoption,
> implementation authorization, or permission to merge.

**Artifacts:**

- `../policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`
- `../policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`

**Stable IDs semantically affected:** `CC-SPEC-1`, `CC-SPEC-2`, `CC-SPEC-5`,
`CC-SPEC-8`, `CC-SPEC-10`, `CC-SPEC-11`, `CC-IMPACT-2`, `CC-IMPACT-3`,
`CC-IMPACT-4`, `CC-IMPACT-5`, and `CC-IMPACT-6`. Historical parentheticals are also removed from the bodies of
`CC-SPEC-3`, `CC-SPEC-4`, `CC-SPEC-6`, `CC-SPEC-9`, `CC-SPEC-10`,
`CC-IMPACT-1`, `CC-IMPACT-2`, `CC-IMPACT-3`, `CC-IMPACT-5`, and
`CC-IMPACT-7`; their obligations do not change. No identifier is added,
retired, or renumbered.

**Overall change class:** **Normative.** CC-SPEC-1 adds a defined acceptance
unit for a focused change. The remaining edits are Clarifying or Structural,
but the proposal takes the highest class present.

**Author:** Codex drafting worker for `syzygy-2dn`

**Date:** 2026-08-28

## Pre-edit integrity check

`[Observed]` Before either policy was edited, a Python script read the two files
as bytes, computed SHA-256, extracted the matching act phrases from
`../../../decisions/ACCEPTANCE-ACT-RECORD.md`, compared the values, and failed
closed on a mismatch.

```text
CC-SPEC
computed_sha256   9889b7e311ad941eec84d01dc2c035c7e2502a57cf18e68a1028a76d5b814871
act_record_sha256 9889b7e311ad941eec84d01dc2c035c7e2502a57cf18e68a1028a76d5b814871
equal             true

CC-IMPACT
computed_sha256   cd6ec838e701f0258889d0c3c2776fc91fe1686829379b789ae5b151b04c27c0
act_record_sha256 cd6ec838e701f0258889d0c3c2776fc91fe1686829379b789ae5b151b04c27c0
equal             true

population        2 policy subjects
matches           2
mismatches        0
```

Those are the predecessor bytes named by the 2026 acts. Whether they remain
current or have been superseded is answered by later entries in the active act
record. The proposed policy digests are intentionally not copied into this
record: until a new act exists, the
digest-copy checker correctly treats a successor digest beside an old act
phrase as an unregistered act-argument copy. The independent review and worker
handoff must compute both policy digests directly from the exact branch bytes.
Any later correction changes them and requires the review to bind to the new
values.

## Plain-language guide to necessary external terms

This guide is navigation, not a second authority. The named rules own the
meaning:

| Term in the changed reading path | Read it as |
|---|---|
| adopted / accepted / approved / recorded | An authority state eligible for requirement provenance under CC-SPEC-2. Candidate text and pending decisions are not eligible. |
| requirement provenance | Why requirement text belongs in the specification, recorded in CC-SPEC-2's six fields. It does not authorize work. |
| material governing authority | An authority whose removal would remove an accepted basis or change what the requirement can be read to require, permit, or prohibit. Unsettled materiality records `Unknown` beside the provenance declaration and blocks acceptance. |
| work warrant | Traceable authority to create or prioritize work. RFC1-25's `motivates` edge is the carrier; a finding-class warrant requires a recorded confirmation act. |
| reviewed N/A | Honor only when the owner Decision names the exact consequence/scope and independently kept evidence matches the local RFC3-16(b) bindings; absent, unresolvable, or mismatched evidence means no, leaving the row Unknown/unmapped. |
| coverage population | A source-enumerated set fixed before classification. Unknown, unmapped, or provenance-Unknown rows defer acceptance; retired entries receive an explicit retired disposition. |
| affected | An impact relationship established by a declaration match or the stated method. Requirement results propagate to exactly one parent-specification result. |
| Unknown / unmapped | Recorded in the owning requirement, coverage row, or impact-sweep row; human and machine views render the same result and link to what would settle it. |
| independent confirmation | The CC-SPEC-11 table and CC-IMPACT-5 sweep are checked by a party other than their author. The policies state that separation directly; no shorthand pattern must be imported. |
| same logical change | One merge transaction containing the shape delta and every required specification amendment, so mainline never contains one without the other (CC-REV-2, CC-IMPACT-6). |
| consumes its vocabulary | This amendment adds no definition. At each sweep's named revision, use an exact accepted definition if one exists; otherwise dependent cases route to `undecidable`/Unknown under CC-IMPACT-4. |
| act / predecessor / successor | Select exact-digest owner Decisions at the named revision and follow only explicit RFC3-16(b) supersession/revocation links. No record means proposal; one unsuperseded record supplies authority; incompatible unsuperseded records render contradiction/Unknown. |

## Change classifications

| Delta | Stable ID or carrier | Class | Meaning |
|---|---|---|---|
| D3-1 | CC-SPEC-1, CC-SPEC-5, CC-SPEC-8, CC-SPEC-10, and CC-SPEC-11 | **Normative** | Adds separate acceptance criteria, deterministic source extraction, independently enumerable coverage populations, explicit retirement handling, Unknown/unmapped deferral, and candidate-state handling for whole-capability and focused-change acceptance. |
| D3-2 | CC-SPEC-2 and CC-IMPACT-2 | **Normative** | Defines material provenance, adds an acceptance-blocking Unknown when materiality is unsettled, separates the six fields from the RFC1-25 work warrant, and removes work-authorization language from the impact trigger set. |
| D3-3 | CC-SPEC-2 evidence note | **Clarifying** | Keeps the durable exclusion rule and removes volatile corpus counts from policy prose. |
| D3-4 | CC-SPEC-8 | **Normative** | Makes the row unit consistently per observable consequence, adds a reproducible pre-applicability consequence denominator and segmentation blocker, states the reviewed-N/A verification decision, and marks five contract citations as examples. |
| D3-5 | CC-SPEC-11 | **Clarifying** | Removes stale confirmer shorthand while retaining the explicit requirement that a party other than the author confirms the table. |
| D3-6 | CC-IMPACT evidence carrier | **Clarifying** | Replaces an unverifiable repeated pass claim with a resolvable evidence pointer and no repeated verdict. |
| D3-7 | both status carriers | **Clarifying** | Makes exact-digest authority state conditional so the same bytes remain truthful before and after a later owner act. |
| D3-8 | CC-IMPACT-6 and limits | **Clarifying** | Records that the declined lag exception supplies no authority and removes the stale claim that all specifications are future. |
| D3-9 | policy history carriers | **Structural** | Removes finding codes and authoring-history parentheticals from reader-facing rule bodies while preserving their meanings in prior semantic deltas and frozen reviews. |
| D3-10 | CC-IMPACT-2, CC-IMPACT-5, CC-IMPACT-6, and current-state carriers | **Clarifying** | Defines necessary local reading terms, makes time-sensitive claims conditional or method-recorded, and exposes the unresolved vocabulary-consumption ambiguity without deciding it. |
| D3-11 | CC-IMPACT-3 and CC-IMPACT-4 | **Normative** | Freezes an independently enumerable two-level impact corpus, makes result sets disjoint and exhaustive, propagates requirement results to specifications, records Unknown locally, and blocks merge on undecidable or contradicted impact. |

## Readable current and proposed excerpts

The excerpts below explain the changed obligations in reading order. They are
not the completeness mechanism: **Appendix D defines the mechanically exact
current-to-proposed mapping over both policy files and every changed hunk.**
Historical review narration removed from the top banners remains preserved in
the predecessor bytes and the prior semantic-delta records; it is not rewritten
here as policy.

### D3-1 — acceptance unit

**Current text:**

```text
CC-SPEC-1 — Capability and scope are clear. The specification names
one coherent capability, what is in it, and what is out. A reader can say
what the capability is in one sentence without reading the requirements.
```

The current clause then quotes SDR-37's rule that one OpenSpec change governs
one coherent capability or one coherent change to one, but defines no separate
acceptance test for the latter unit.

```text
CC-SPEC-11 — The requirement set covers the capability, and the coverage
is demonstrated.

A specification demonstrates that its requirements cover the capability it
declares, with a coverage table produced with the spec. The table's
population is the declared capability obligations — each thing the
CC-SPEC-1 scope statement says the capability does, renders, records, or
refuses — counted, and declared by the spec itself.

The completeness test is bounded to the declared scope: no proof is
demanded over obligations the specification does not declare.
```

**Proposed text:**

```text
CC-SPEC-1 — Capability, scope, and acceptance unit are clear. The
specification names one coherent capability, what is in it, and what is out.
A reader can say what the capability is in one sentence without reading the
requirements. Each proposed specification change also says whether its
acceptance unit is the whole capability or one focused change to that
capability.

The two acceptance units are distinct:

1. Whole-capability acceptance. The owner-readable argument covers the
   complete capability declared by the specification. CC-SPEC-11 independently
   enumerates the coverage population from the scope, complete requirement
   inventory (including retired entries), and non-goals. The acceptance
   decision applies to that classified population at the exact digest recorded
   under CC-SPEC-10.
2. Focused-change acceptance. The owner-readable argument names the
   accepted capability baseline being changed and the exact obligations the
   change adds, modifies, retires, or makes newly relevant. CC-SPEC-11
   independently enumerates the coverage population from the exact
   baseline-to-proposal difference, the change scope and non-goals, and a stated
   affected-baseline sweep. The acceptance decision applies only to this
   classified coherent change at the exact digest recorded under CC-SPEC-10;
   it does not silently re-accept the whole capability or widen the change's
   declared scope.

Both units must satisfy CC-SPEC-2 through CC-SPEC-11. If a reviewer finds an
obligation omitted from the declared coverage population, the acceptance-unit
statement is incomplete; narrowing the population does not make the change
acceptable.

CC-SPEC-11 — The requirement set covers the declared acceptance unit, and
the coverage is demonstrated. This clause covers the acceptance unit's own
obligations; CC-SPEC-8 separately covers contract observable consequences.

A specification demonstrates that its requirements cover the acceptance unit
declared under CC-SPEC-1, with a coverage table produced with the
specification. The coverage population is independently enumerated before
classification; the table author may not define it merely by listing chosen
rows. Whole-capability enumeration reads the scope, complete requirement
inventory including retired entries, and non-goals. Focused-change enumeration
reads the exact baseline-to-proposal requirement difference, change scope and
non-goals, and a stated affected-baseline sweep over references, provenance,
coverage mappings, and defined vocabulary. Each row names a stable requirement
ID when one exists, or a table-local ID, source locator, and discovery method.

Each population member enters exactly one set: covered; lawfully out of scope
or retired (with the non-goal or retired entry named); or Unknown / unresolved.
A party other than the specification's author confirms that the independently
enumerated population and its partition are complete.
```

The existing exact SDR-37 quotation between the opening paragraph and the two
units remains unchanged. Appendix D provides the complete exact mapping,
including the full three-set definitions.

CC-SPEC-10's current closing sentence, `Until the adoption record exists the
spec is a candidate like everything else`, is proposed as:

```text
Until the adoption record exists, the proposed acceptance unit is a candidate.
For a focused change, the accepted capability baseline keeps its prior state;
only the proposed change remains a candidate.
```

### D3-2 — requirement provenance and work warrants

**Current text:**

```text
CC-SPEC-2 — Every requirement names all its material governing
warrants. The rule:

Every requirement names all material governing warrants. One may be
marked primary for navigation; none may be hidden merely because another
is more specific.
```

The current six fields are `doctrine[]`, `contracts[]`, `policies[]`,
`decisions[]`, `topology[]`, and `parent_requirements[]`; they remain
byte-for-byte unchanged.

**Proposed text:**

```text
CC-SPEC-2 — Requirement provenance names every material governing
authority. In this rule, a governing warrant means the accepted authority
that explains why a requirement belongs in the specification. It does not
authorize drafting, implementation, scheduling, or any other work. The rule:

Every requirement names all material governing warrants. One may be
marked primary for navigation; none may be hidden merely because another
is more specific.

A work warrant is separate. RFC1-25 defines the `motivates` edge from a
permitted authority to a work item or proposal as the work-warrant carrier. A
confirmed review finding may warrant corrective work through that edge, but it
is not a seventh requirement-provenance class and is not inserted into the six
fields above. RFC1-25 requires a recorded confirmation act before a
finding-class warrant can motivate work. If an adopted, accepted, approved, or
recorded authority later incorporates the finding's substance, a requirement
cites that authority in the matching provenance field. A work warrant never
makes proposed requirement text accepted.
```

The paired CC-IMPACT-2 wording now calls the same six fields the
*requirement-provenance set* and says explicitly that they do not authorize
creating or prioritizing work. Its sweep-trigger identity is unchanged; only
the work-authorization reading is removed.

### D3-3 — durable rule, volatile evidence removed

**Current text:**

```text
`lawfully admitted user need` is deliberately not a class. It appeared
in this clause until 2026-08-13 and is removed: no admission act, register,
or record class for a user need is defined by any authority in this
repository. [Observed] — the sweep, re-run 2026-08-13 in the session that
made this amendment rather than quoted from the review that prompted it.
Python re `user\s+need`,
case-insensitive, over `.syzygy/**` `*.md|*.yaml|*.json` — 371 files
scanned, 2 files with hits: this clause's own discussion of the class, and
the review that found it. Second method, repo-wide over
`.md|.py|.json|.yaml|.yml|.txt` — 784 files scanned, 3 files with hits:
those two, plus an untracked file absent from every commit. No admission
act, register, or record class is defined by any authority. A class whose
satisfying record an author may name at will is an unbounded escape hatch in
the clause whose purpose is to close one. Admitting the class requires first
defining the admitting authority and record in the shape layer — queued as a
question, not assumed here.
```

**Proposed text:**

```text
`lawfully admitted user need` is deliberately not a class. This policy
defines no authority or record that could admit such an entry. Adding it first
requires a shape-layer definition of the admitting authority and record, then
an amendment to this closed set. Exact sweep evidence belongs in the amendment
record, not in this binding rule.
```

The exact current sweep evidence is preserved above; it is historical evidence,
not a current corpus claim.

### D3-4 — observable-consequence coverage

**Current text:**

```text
CC-SPEC-8 — Applicable contract clauses are covered or lawfully N/A.
The clause-to-requirement coverage matrix (the phase-rule clauses'
obligation) is produced with the spec; every applicable clause is covered
by requirements or carries a reviewed N/A judgment. The matrix's unit is
the contract's, not this clause's: rows are per observable consequence,
not per clause (RFC1-33, RFC6-28) — a clause with five observable
consequences and one mapped requirement is not covered.

"Applicable", defined. A contract clause is applicable to a
specification when the capability uses the entity, behavior, authority
boundary, state vocabulary, or interface the clause governs. A reviewer
applies this test clause by clause against the specification's CC-SPEC-1
scope statement; a clause governing something the capability neither
renders, stores, transitions, queries, nor crosses is not applicable, and
saying so is an N/A judgment, not an omission.

The reviewed-N/A judgment's home, gate, unit, and effect rule are the
contract's, not this clause's. They are stated by the confirmed contract
modules RFC1-33, RFC6-28, RFC7-38, RFC8-32, and RFC9-52:
```

The ellipsis above begins only after the unchanged owner-gate sentence; the
changed current text ends at the colon after `RFC9-52`.

**Proposed text:**

```text
CC-SPEC-8 — Applicable contract observable consequences are covered or
lawfully N/A. The observable-consequence-to-requirement coverage matrix is
produced with the specification; every applicable observable consequence is
covered by requirements or carries a reviewed N/A judgment. Rows are per
observable consequence, not per clause (RFC1-33, RFC6-28) — a clause with
five observable consequences and one mapped requirement is not covered.

"Applicable", defined. A contract clause's observable consequence is
applicable to a specification when the capability uses the entity, behavior,
authority boundary, state vocabulary, or interface that consequence
governs. A reviewer applies this test consequence by consequence against the
specification's CC-SPEC-1 scope statement. A consequence governing something
the capability neither renders, stores, transitions, queries, nor crosses is
not applicable, and saying so is an N/A judgment, not an omission.

The reviewed-N/A judgment's home, gate, unit, and effect rule are the
contract's, not this clause's. Examples of confirmed contract modules that
state the rule include RFC1-33, RFC6-28, RFC7-38, RFC8-32, and RFC9-52;
this is an examples list, not a completeness claim.
```

The text immediately after these exact changed sentences remains unchanged and
defines the owner gate, provenance check, Unknown effect, and
specification-side production duty.

### D3-5 — stale cross-reference

**Current text:**

```text
The table is confirmed by a party other than the specification's author
(the CC-TEST-4 pattern, as CC-SPEC-8).
```

**Proposed text:**

```text
The table is confirmed by a party other than the specification's author; that
explicit separation is the rule, with no external pattern needed to interpret
it.
```

### D3-6 — prior exercise evidence

**Current text:**

```text
The blind exercise CC-IMPACT-7 requires has been run and passed (RD-59,
`../round-2026-08g/reviews/DISPOSITION-REGISTER.md`), bound to the
fixture digest quoted in CC-IMPACT-7.
```

**Proposed text:**

```text
The historical blind-propagation evidence record is
`../round-2026-08g/reviews/DISPOSITION-REGISTER.md`; this banner does not repeat
or independently assert that record's verdict.
```

### D3-7 — post-act status

**Current CC-SPEC status text:**

```text
Candidate. Binds nothing until its own `CONFIRM CRAFT AMENDMENT`
act. Proposed at the 2026-08-10 launch-closure pass to close
launch-gate question E5 (no acceptance criteria existed for a
specification itself — "spec acceptance would be a vibe check").
```

**Current CC-IMPACT status text:**

```text
Candidate. Binds nothing until its own `CONFIRM CRAFT AMENDMENT`
act. Proposed at the 2026-08-11 structured-closure pass to close
launch-gate question E6.

This is a candidate. It comes into force only by its own
`CONFIRM CRAFT AMENDMENT` act, at a digest computed at the act — the route
the craft cluster defines. Nothing in it binds today, and no verdict of the
launch gate may cite it as in force until that act is performed. Its queue
row is P-42 in `../../../decisions/PENDING-OWNER-DECISIONS.md`, and it
is offered together with the specification-acceptance policy (P-41).
```

**Proposed CC-SPEC status text:**

```text
Candidate before an exact-digest act; confirmed successor after one. Authority
state resolves from the active acceptance record. These bytes are a proposal
while no performed owner act names their exact sha256.
If such an act later names this exact digest, these same bytes are the confirmed
successor from that act; no banner edit is needed. The 2026 acts identify the
predecessor digests they confirmed and do not bind a different digest. Whether
those predecessor bytes are current or superseded is likewise answered by the
act record, never inferred from this banner. Drafting, review, a commit, or a
pull request changes no authority state.
```

**Proposed CC-IMPACT status text:**

```text
Candidate before an exact-digest act; confirmed successor after one. Authority
state resolves from the active acceptance record. These bytes are a proposal
while no performed owner act names their exact sha256.
If such an act later names this exact digest, these same bytes are the confirmed
successor from that act; no banner edit is needed. The 2026 acts identify the
predecessor digests they confirmed and do not bind a different digest. Whether
those predecessor bytes are current or superseded is likewise answered by the
act record, never inferred from this banner. Drafting, review, a commit, or a
pull request changes no authority state.
```

**Proposed CC-IMPACT closing text:**

```text
The active acceptance record determines this exact file's state as the top
banner describes: proposal when no performed owner act names its digest,
confirmed successor from an act that does. It must be reviewed and offered
with the specification-acceptance policy. Drafting, review, a commit, or a pull
request is not that act.
```

### D3-8 — declined exception and stale future claim

**Current text:**

```text
This clause creates no alternative. A lagging specification is lawful
only if CC-REV-2 is itself amended, in place, through the craft
cluster's own amendment act. That amendment is offered separately —
`CC-REV-2-LAGGING-SPECIFICATION-AMENDMENT-OFFER.md` in this directory,
queued as P-44 — and it carries five required elements plus a confirmer
distinct from the change's author. Until that act is performed, no lawful
lag exists, and a shape change whose spec amendments cannot land with it
does not merge.

It does not create, imply, or authorize `openspec/`. Every specification
it speaks of is future.
```

**Proposed text:**

```text
This clause creates no alternative. The owner declined the previously
offered lagging-specification exception, so it supplies no authority and this
amendment does not revive it. A lagging specification could become lawful only
if CC-REV-2 were itself amended in place through a new craft act. Until such an
act is performed, no lawful lag exists, and a shape change whose specification
amendments cannot land with it does not merge.

It does not create, imply, or authorize specification work. Specification
authoring, adoption, and implementation each require their own authority;
this policy only governs propagation once the relevant artifacts exist.
```

### D3-9 — review history leaves the rule bodies

**Current text:** dated italic parentheticals inside the rule bodies identify
the predecessor review findings for CC-SPEC-2, CC-SPEC-3, CC-SPEC-4,
CC-SPEC-6, CC-SPEC-9, CC-SPEC-10, CC-IMPACT-1, CC-IMPACT-2, CC-IMPACT-3,
CC-IMPACT-5, CC-IMPACT-6, and CC-IMPACT-7. The exact paragraphs remain
preserved at the predecessor digests recorded by acts 6 and 7 and in the prior
semantic-delta records.

**Proposed text:** no replacement rule text. The parentheticals are removed;
the operative text on both sides joins without alteration. Appendix A lists
the moved finding codes and their evidence homes. This is a structural
reader-surface change, not a claim that the historical findings disappeared.

### D3-10 — durable current-state claims and local reading terms

**Current text and ambiguity:** CC-SPEC-10 says that owner adoption follows
from the "current doctrine state" because delegated-gate prerequisites do not
exist. CC-IMPACT-2 calls requirement provenance the "warrant set", uses the
undefined phrase `consumes its vocabulary`, CC-IMPACT-5 imports a
`CC-TEST-4 pattern`, CC-IMPACT-6 says there is no exception "today", and the
limits section says there is no script "today". These statements either
conflate two authority classes, require external context, or become stale as
repository state changes.

**Proposed meaning:**

- CC-SPEC-10 applies VIS-4 conditionally at the adoption act and makes no
  ambient claim that the delegated-gate prerequisites are present or absent.
- CC-IMPACT-2 calls its six identities the requirement-provenance set and says
  explicitly that this is not the work-warrant set.
- This amendment adds no definition for `consumes its vocabulary`; each sweep
  resolves definition availability at its named revision and routes dependent
  cases to `undecidable` under CC-IMPACT-4 when none exists.
- CC-SPEC-11 and CC-IMPACT-5 state non-author confirmation directly rather
  than importing a test-policy shorthand.
- CC-IMPACT-6 defines *same logical change* as one merge transaction and states
  durably that this policy creates no exception.
- The limits section neither asserts nor denies a script; every sweep record
  states the method it actually used.

### D3-11 — independently enumerable impact and determinate propagation

**Current meaning:** CC-IMPACT-3 defines its population as the specifications
and requirements "examined", so matching can silently choose the denominator.
It does not define `affected`, make the three result sets exhaustive, or state
how a requirement result determines its parent specification. CC-IMPACT-4
requires Unknown rendering but does not name the owning row or say whether an
undecidable specification blocks the shape delta.

**Proposed meaning:** the sweep freezes every accepted specification and every
stable requirement entry at one named revision before matching. Each
requirement enters exactly one of `affected`, `explicitly unaffected`, or
`undecidable`, using the locally stated direct-match rule while undefined
vocabulary relationships remain undecidable. Each specification then enters
exactly one corresponding set: an affected requirement makes its parent
affected; absent an affected child, an undecidable child makes its parent
undecidable. The sweep row owns Unknown, all projections link to it, and an
Unknown or contradicted specification blocks the shape delta from satisfying
CC-IMPACT-6.

## What explicitly does not change

- No decision is made for the unresolved convention tracked as P-43.
- The declined P-44 exception is not revived, re-offered, or installed.
- No accepted contract is edited, including RFC-0010 or RFC-0011 material.
- No deferred capability, Mission, or context-selection work is authored,
  planned, backlogged, or implemented.
- No historical review, raw output, prior semantic delta, install record, or
  acceptance-act record is edited.
- No policy identifier is added, retired, renumbered, or reused.
- The six CC-SPEC-2 provenance fields do not change.
- CC-IMPACT-1's generated union and CC-IMPACT-2's trigger-set identity do not
  change.
- CC-REV-2's same-logical-change rule remains unmodified and uncarved.
- This amendment does not define `consumes its vocabulary`; it records the
  pre-existing ambiguity, requires a revision-bound definition lookup, and
  preserves CC-IMPACT-4's fail-closed route when none exists.
- VIS-4's delegated-gate conditions, RFC1-25's work-warrant classes,
  the contract-owned reviewed-N/A gate, and the independent-confirmation
  obligations are explained locally but not changed.
- This proposal is not adoption, merge authority, or implementation authority.

## Warrant

The owner authorized drafting on 2026-08-28. That instruction authorizes this
proposal and its review only. It does not authorize adoption or merge. The
substantive warrant is the confirmed review finding set carried forward from
the 2026 acceptance cycle; the exact finding-to-delta mapping is in Appendix A.
After two correction cycles, the owner explicitly selected Option A on
2026-08-28, authorizing the bounded human-reviewability pass itemized in
Appendix F over the same three files. That choice grants no merge or adoption
authority.

## Evidence or decision basis

- VIS-3 requires a fresh reader to restate a normative artifact correctly on
  material amendment.
- VIS-4 reserves craft-policy adoption to the owner and distinguishes drafting
  from adoption.
- Doctrine's trust-and-evidence rule distinguishes requirement/evidence status
  from a work warrant; RFC1-25 defines the `motivates` edge as its carrier and
  requires a recorded confirmation act for a finding-class warrant.
- SDR-37 defines one owner-readable product argument and one acceptance decision
  for one coherent capability or one coherent change to one.
- The 2026-08-17 acts identify the exact predecessor policy bytes they
  confirmed; the active record and any later act determine whether those bytes
  remain current or have been superseded.

## Terms introduced or retired

None. *Acceptance unit*, *whole-capability acceptance*, *focused-change
acceptance*, and *requirement provenance* are explanatory uses of existing
concepts, not new closed-vocabulary values. *Work warrant* and `motivates` use
the existing doctrine and RFC1-25 terms rather than minting a record class.
*Coverage population* is an existing CC-SPEC-11 term whose enumeration is made
operationally independent by D3-1. *Same logical change* is CC-REV-2's existing
term. D3-11 gives *affected* and the impact input corpus local operational
tests for this policy without admitting new closed-vocabulary values.
`Consumes its vocabulary` receives no definition from this amendment and is
not admitted as a new term; each sweep resolves availability at its named
revision.
Independent review must challenge this classification if any phrase functions
as a new durable term.

## Downstream impact

Method and final results are recorded in Appendix B. The sweep covers every
text-readable tracked or proposed file, not only default-path governance files.
Because every stable identifier remains unchanged, citations continue to
resolve. No dependent rule is proposed for edit in this drafting pass.

The only deliberately invalidated binding relation is digest identity: the
2026 acts name the predecessor bytes, not these successor bytes. Therefore the
current-act digest and copy checks are expected to fail while run against this
branch proposal. That failure is the guard proving the proposal has not been
silently laundered into the old act.

## Migration and supersession plan

While no performed owner act names the successor digests, there is no migration
and the branch and draft pull request are only proposal carriers. The active
act record continues to determine which predecessor bytes apply.

If independent review fails, or the owner declines the proposal, rollback is
to close the draft pull request and abandon this branch. No authority record or
mainline policy changes, so no compensating edit is required.

If the owner chooses to adopt a reviewed exact version, the later
owner-authorized acceptance transaction must recompute both policy digests,
append the owning act and install records through their prescribed ceremony,
and identify the predecessor digests as superseded historical authority. That
transaction is outside this drafting bead. Editing either policy after its
review or act retires the review or act for the edited file.

## Expected pre-act verification ledger

`[Observed]` The working-tree governance check examined 659 files and reported
31 OK, 18 WARN, and exactly 2 FAIL check families. Both failures are expected
pre-act guards:

| Check | Denominator | Findings | Exact classification |
|---|---:|---:|---|
| CG-7d, act digests quoted anywhere match their subjects | 18 quotations | 7 | Four predecessor CC-SPEC copies and three predecessor CC-IMPACT copies no longer equal the edited subjects. |
| CG-7e, act-argument copies enumerated and current | 7 registered files | 7 | The same four CC-SPEC and three CC-IMPACT act-bound copies do not contain the successor subject digests. |

The seven locations are the foundational acceptance record (both subjects),
the performed owner-act record (both), the specification-acceptance decision
(CC-SPEC), and the craft install record (both). All are existing authority or
historical records that this proposal is forbidden to edit. They return to
consistency only through a new owner act over independently reviewed exact
bytes. No other check family reported FAIL. A successful exit code alone is
never sufficient; the output, predicate name, and denominator are retained.

## Author fresh-reader self-checks — not a confirmation

`[Inferred]` The author re-read only the two proposed policy subjects from the
top, without using the finding appendix as an explanation, and attempted the
fresh-reader restatement. That pass first exposed a contradiction: CC-SPEC-1
had a focused-change coverage population while CC-SPEC-11 still named only a
whole-capability population. Both clauses were then corrected together, which
invalidated the earlier draft digest.

The independent new-context reader then returned `FRESH-READER REVISE` at
`e44b5bc673121d74a44052199d39e37cc148e213`. The second correction addresses
its direct amendment findings. On the resulting authoring bytes, the author's
restatement is:

- a proposed spec change declares whole-capability or focused-change
  acceptance; a fresh reader independently enumerates the coverage population
  from named sources before classification, including retired requirement
  entries, then places each member in exactly one set; any Unknown, unmapped,
  or provenance-Unknown row records `Unknown` and defers acceptance;
- the six CC-SPEC-2 fields explain requirement provenance, while RFC1-25's
  `motivates` edge carries the separate work warrant; a confirmed finding can
  motivate corrective work only after its recorded confirmation act;
- CC-IMPACT-2 reuses the provenance set only as its sweep-trigger set and does
  not claim that those six fields authorize work;
- CC-SPEC-8 evaluates and records coverage per observable consequence, and
  its five contract citations are explicitly examples; a reviewed N/A is an
  owner judgment with verifiable act provenance, not reviewer approval;
- CC-SPEC-11 and CC-IMPACT-5 state their independent-confirmer rule directly,
  without requiring a reader to import a CC-TEST-4 shorthand;
- CC-IMPACT-6 defines *same logical change* as one merge transaction;
  this amendment adds no `consumes its vocabulary` definition, so a sweep with
  none at its named revision routes dependent cases to `undecidable`;
- CC-IMPACT-3 freezes the accepted specification and stable-requirement corpus
  before matching, partitions both requirement and specification populations
  exactly once, and propagates every requirement result to its parent;
- CC-IMPACT-4 records Unknown in the sweep row and all projections, and an
  undecidable or contradicted specification blocks the shape delta;
- delegated-gate presence and sweep-script existence are no longer asserted as
  ambient current state; the act or sweep record supplies the current fact;
- the impact policy points to historical exercise evidence without repeating a
  verdict; and
- both top banners remain conditional: proposal without an act naming the
  exact digest, confirmed successor from an act that does.

This is an author self-check, not fresh independent review, not a VIS-3 pass,
and not confirmation. It does not turn the new-context `FRESH-READER REVISE`
into a pass. The independent review requirements below remain open.

## Review requirements

1. **Independent semantic review of exact bytes.** The reviewer must not have
   authored this proposal or shared its authoring session. Give the reviewer
   the two policy subjects, this delta, VIS-3, VIS-4, the trust-and-evidence
   warrant distinction, SDR-37, and the acceptance criteria — not the authoring
   conversation or a desired verdict.
2. **Fresh-reader check.** Without the finding codes or prior review history,
   the reader must accurately explain: the two acceptance units; how each
   coverage population is independently enumerated and how retirement is
   classified; why Unknown or unmapped coverage defers acceptance; requirement
   provenance versus a work warrant; the reviewed-N/A owner gate; independent
   confirmation; the frozen impact corpus and disjoint result sets;
   requirement-to-specification propagation; where Unknown is recorded and
   rendered; same-logical-change semantics; the explicit unresolved
   vocabulary-consumption limit; the evidence pointer's limited claim; and how
   the same authority-state banner remains true before and after an act.
3. **Exact verdict and findings.** Store raw review output verbatim, copy the
   verdict word exactly, and disposition every finding. The author performs no
   confirmation of their own draft.
4. **Repair invalidates review.** Any substantive repair changes the subject
   digests and requires fresh independent review of the new exact bytes.
5. **Owner act last.** Only after all findings are resolved and the final
   digest-bound review is complete may the exact bytes be presented for owner
   adoption. A draft pull request must remain unmerged before that act.

## Appendix A — finding provenance and excluded routes

Finding codes and source paths live here so the policy rules remain readable
without review-history jargon.

| Source | Finding | This proposal's disposition |
|---|---|---|
| `../round-2026-08i/reviews/RD-69-DISPOSITION-REGISTER.md` | RD69-N1 | D3-1 defines focused-change acceptance separately from whole-capability acceptance. |
| same register | RD69-N3 | D3-2 distinguishes requirement provenance from the work warrant and places confirmed findings on RFC1-25's `motivates` edge without adding a seventh field. |
| same register | policy-owned part of RD69-N5 | D3-3 removes volatile sweep counts; D3-6 removes the repeated exercise verdict. |
| same register | RD70-N1 | D3-5 removes the stale CC-SPEC-8 cross-reference. |
| same register | RD70-N2 | D3-4 aligns CC-SPEC-8's heading, opening, applicability test, and row unit. |
| same register | RD70-N3 | D3-4 says explicitly that the five cited modules are examples. |

Predecessor history moved out of the rule bodies is preserved in
`../round-2026-08g/SPEC-ACCEPTANCE-AND-IMPACT-SEMANTIC-DELTA.md`, its review
register, and the frozen raw review it cites. The moved references cover RD-51
f1, f2, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f16, f17, f20, the
stable-identity and sweep-actor findings described there, and its unresolved
vocabulary-consumption finding. No historical file is edited.

Excluded routes:

- RD69-N2 remains owned by P-43; this draft does not decide it.
- RD69-N4 was superseded when the owner declined P-44's exception; D3-8 only
  removes stale policy wording and does not revive the offer.
- RD70-N4 remains on the deferred RFC-0010/RFC-0011 route; this draft does not
  edit either contract.

## Appendix B — downstream and focused verification evidence

The post-edit sweep method was:

1. enumerate the proposed corpus with
   `git ls-files --cached --others --exclude-standard`;
2. read every text-decodable file with Python and count files containing each
   affected stable ID and each subject filename;
3. reproduce each file count independently with `rg -l -F` over the same
   enumerated path set;
4. enumerate every remainder rather than reporting only a total;
5. classify default-path authority, historical/review evidence, generated or
   derived artifacts, scripts, and adopted specification artifacts separately;
6. run literal checks for the stale CC-SPEC-8 cross-reference, volatile policy
   counts, banner state, and examples marker by Python and `rg` independently.

`[Observed]` The proposed corpus contained 659 files; all 659 decoded as text.
Python and `rg -l -F` returned identical file sets for every reference:

| Reference | Files / 659 | Second method |
|---|---:|---|
| CC-SPEC-1 | 54 | exact set equality |
| CC-SPEC-2 | 21 | exact set equality |
| CC-SPEC-5 | 8 | exact set equality |
| CC-SPEC-8 | 26 | exact set equality |
| CC-SPEC-10 | 22 | exact set equality |
| CC-SPEC-11 | 19 | exact set equality |
| CC-IMPACT-2 | 13 | exact set equality |
| CC-IMPACT-3 | 10 | exact set equality |
| CC-IMPACT-4 | 5 | exact set equality |
| CC-IMPACT-5 | 5 | exact set equality |
| CC-IMPACT-6 | 14 | exact set equality |
| CC-SPEC subject filename | 37 | exact set equality |
| CC-IMPACT subject filename | 25 | exact set equality |

The remainders were enumerated in the command output. They span active routing
and decision artifacts, adopted Capability 1 specification artifacts, scripts,
historical semantic deltas, and frozen review evidence. Stable identifiers were
preserved, so those citations remain resolvable; changing their wording does
not require rewriting frozen evidence or adopted artifacts. The seven
digest-bound copies listed in the expected-failure ledger are the only
downstream byte-identity relations invalidated by this draft.

`[Observed]` Focused literal sweeps were run over both policy subjects with
Python `str.count` and `rg -F -o`; every count agreed:

| Predicate | Occurrences / 2 subjects |
|---|---:|
| stale `CC-TEST-4 pattern, as CC-SPEC-8` cross-reference | 0 |
| old per-clause CC-SPEC-8 heading | 0 |
| new observable-consequence CC-SPEC-8 heading | 1 |
| per-observable-consequence opening | 1 |
| `observable consequence, not per clause` unit | 1 |
| explicit examples-only marker | 1 |
| repeated claim that the blind exercise `has been run and passed` | 0 |
| stale `Nothing in it binds today` claim | 0 |
| stale P-42 queue marker | 0 |
| stale P-44 queue marker | 0 |
| conditional candidate/successor banner | 2 |
| proposal-without-act condition | 2 |
| confirmed-successor-with-act condition | 2 |
| old unconditional proposed-post-act banner | 0 |
| old unconditional binding-mainline statement | 0 |
| whole-capability acceptance unit | 1 |
| focused-change acceptance unit | 1 |
| acceptance-unit CC-SPEC-11 heading | 1 |
| confirmed-finding `motivates`-edge placement | 1 |
| undefined `work-warrant record` carrier | 0 |
| RFC1-25 `motivates`-edge carrier in policy prose | 1 |
| independently enumerable coverage-population definition | 1 |
| explicit retired-entry source and disposition | 2 |
| material-authority test | 1 |
| determinate acceptance rule | 1 |
| no-Unknown-to-acceptance-exception sentence | 1 |
| unmapped-coverage blocker | 1 |
| requirement/matrix/table Unknown ownership paragraph | 1 |
| pre-applicability contract-consequence population | 1 |
| contract-consequence local-ID rule | 1 |
| consequence-segmentation Unknown blocker | 1 |
| deterministic scope/non-goal extraction rule | 1 |
| non-semantic deduplication prohibition | 1 |
| active requirement cannot self-cover | 1 |
| old `declared acceptance-unit population` phrase | 0 |
| requirement-provenance trigger heading | 1 |
| old `trigger set is the warrant set` heading | 0 |
| external `CC-TEST-4 pattern` shorthand | 0 |
| explicit undefined-vocabulary disclosure | 1 |
| same-logical-change one-merge explanation | 1 |
| frozen impact input corpus | 1 |
| requirement result-set disjoint/exhaustive rule | 1 |
| specification result-set exhaustive rule | 1 |
| requirement-to-parent propagation rule | 1 |
| contradicted-in-partition precedence rule | 1 |
| impact Unknown owning-row rule | 1 |
| impact Unknown/contradiction merge blocker | 1 |
| owner-Decision adoption corpus rule | 1 |
| explicit-supersession-only selection rule | 1 |
| reviewed-N/A local yes/no rule | 1 |
| revision-bound vocabulary-definition lookup | 1 |
| stale `current doctrine state`, `neither exists`, `no script today`, `exception today`, `candidate, P-12` phrases | 0 each |
| removed volatile values `371 files`, `784 files`, `398-file` | 0 each |
| review finding codes matching `RD-[0-9]` | 0 |

The classification-table sweep parsed 11 of 11 D3 rows and found only the
canonical values: four `Normative`, six `Clarifying`, and one `Structural`.

`[Observed]` The five example citations were then resolved independently in
the accepted contract tree. RFC1-33, RFC6-28, RFC7-38, RFC8-32, and RFC9-52
all define an OpenSpec-seam phase rule that requires observable consequences
to map to approved requirements or to a reviewed N/A owner judgment with
verifiable provenance; RFC1-33 and RFC6-28 also state the row unit explicitly
as one row per observable consequence.

`[Observed]` The CC-SPEC-2 declaration block still says `closed set of six`,
contains each of `doctrine[]`, `contracts[]`, `policies[]`, `decisions[]`,
`topology[]`, and `parent_requirements[]` exactly once, and contains no other
array-shaped field token.

`[Observed]` The removed user-need evidence was refreshed outside binding
policy prose. Method 1 scanned 461 `.syzygy/**` Markdown, YAML, and JSON files;
method 2 scanned 555 repository files with Markdown, Python, JSON, YAML, YML,
or text extensions. Both found the same five files: this delta, the CC-SPEC
subject, the prior semantic delta, and two preserved raw review records. None
defines an additional provenance field; the live policy mention states the
exclusion, while the other four preserve proposal or review history.

## Appendix C — expected-failure classification rules

An expected failure must satisfy all of these conditions:

- it names one or both edited policy subjects;
- it compares the subject to a predecessor act digest or an act-bound copy;
- its observed value is one of the proposed successor digests, not an unrelated
  value;
- it would return to pass only through a new owner act over the exact final
  bytes, not by weakening the checker or editing a historical record.

Anything else — unresolved links, vocabulary drift, missing identifiers,
malformed Markdown, stale non-act prose, self-test failure, denominator loss,
or a canonical battery failure unrelated to the two predecessor digests — is
an amendment defect, not an expected exception.

## Appendix D — complete exact current-to-proposed mapping

This appendix owns the exact-text requirement for every changed rule and
carrier in both policy subjects. The readable excerpts above are explanatory;
they are not substitutes for this mapping.

**Current text identity.** The baseline is annotated tag
`craft-acts-6-7-confirmed-2026-08-17`, commit
`71e598607d8db161a34e99eae453253152692915`. Scripted reads of the two tagged
subjects produce the act-record digests:

```text
CC-SPEC   9889b7e311ad941eec84d01dc2c035c7e2502a57cf18e68a1028a76d5b814871
CC-IMPACT cd6ec838e701f0258889d0c3c2776fc91fe1686829379b789ae5b151b04c27c0
```

**Proposed text identity.** The proposed text is the complete content of the
same two paths at the exact review head containing this delta. A reviewer uses
the PR's exact head SHA in place of `HEAD`; a moved head invalidates the output.

**Mechanically complete mapping.** This command emits every current and
proposed line, not only changed-line context, for exactly the two subjects:

```sh
BASE=craft-acts-6-7-confirmed-2026-08-17
git diff --no-ext-diff --unified=100000 "$BASE" HEAD -- \
  .syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md \
  .syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md
```

Completeness checks:

```sh
git diff --name-only craft-acts-6-7-confirmed-2026-08-17 HEAD -- \
  .syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md \
  .syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md
git diff --check craft-acts-6-7-confirmed-2026-08-17 HEAD -- \
  .syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md \
  .syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md
```

The first command must enumerate exactly two paths, the two policy subjects;
the second must print nothing. Because the full-file diff is generated from the
act-bound baseline and exact review head, it covers the full CC-SPEC-11
three-set text, every removed historical parenthetical, the CC-SPEC-8 repair
history carrier, both banners, and every other changed hunk without relying on
an author's excerpt selection.

## Appendix E — correction-review dispositions

The independent review examined PR head
`31422229bbdf646f53a3f81fb33b331bce40b9b3` and returned four inline
`correction-required` findings. Those inline comments did not state an overall
verdict. The complete structured reviewer report for the same review did:

```text
Verbatim-Verdict: VERDICT: REVISE
Status: corrections-required
```

The verdict is therefore copied exactly as **`VERDICT: REVISE`**. The complete
raw structured report has not been stored in the tracked corpus, a PR comment,
or a review body; the Beads review issue carries only a summary and is not a
clone-resolvable raw evidence home. That evidence-home gap is disclosed rather
than replaced with the four inline comments. The corrections below moved the
head and therefore required a new independent exact-head review.

| Thread | Verified basis | Correction |
|---|---|---|
| [work-warrant carrier](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3874165236) | Doctrine defines the authorization class; RFC1-25 defines `motivates` as its carrier. The draft's `work-warrant record` existed nowhere authoritative. | CC-SPEC-2 now cites the `motivates` edge consistently and requires RFC1-25's recorded confirmation act for a finding-class warrant. |
| [coverage-population contradiction](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3874165462) | The draft defined the population as in-unit obligations while also placing explicit exclusions inside it. | CC-SPEC-1 and CC-SPEC-11 now define one pre-classification coverage population containing candidates for inclusion and explicit exclusions, then partition it exactly once. |
| [incomplete exact-text mapping](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3874165726) | The normative-change workflow requires exact current and proposed text; the readable excerpts omitted changed carrier text. | Appendix D now generates a full-file diff from the act-bound tag to the exact review head and mechanically checks its two-path denominator. |
| [non-canonical change classes](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3874165999) | The semantic-delta template closes the class vocabulary to Editorial, Clarifying, Normative, and Structural. | Every D3 row now selects exactly one canonical class; D3-5 is Clarifying because the unchanged confirmer obligation is made harder to misread. |

The next semantic review examined
`e44b5bc673121d74a44052199d39e37cc148e213` and returned **`VERDICT: REVISE`**
for the inaccurate verdict account above; its resolvable inline finding is
[the semantic-verdict thread](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3874346977).
An independent new-context reader at the same head returned
**`FRESH-READER REVISE`** with the direct amendment and external-term findings
accounted for in D3-1, D3-2, D3-5, D3-10, and the reading guide. Its complete
raw report is also not stored in a clone-resolvable home; the review issue
retains only a summary. Neither REVISE is restated as a pass, and this second
correction requires another independent exact-head review.

## Appendix F — owner-authorized human-reviewability pass

At `b0fefad232f07dab6bfce6998d90e3660250b42f`, the new-context semantic
review returned **`VERDICT: REVISE`** and the new-context reader returned
**`FRESH-READER REVISE`**. Their complete raw reports are not stored in a
clone-resolvable home; the canonical review issue retains a summary. The owner
then selected Option A on 2026-08-28: address every material active-rule
reviewability finding inside the same two policies and change record, without
creating a subsystem or deciding excluded owner questions.

| Finding from the new-context reports | In-scope disposition |
|---|---|
| Both authority banners become false when the exact bytes are adopted. | D3-7 makes authority state conditional on whether the active act record names the exact digest, so the same bytes remain truthful before and after an act. The resolvable semantic finding is [the banner thread](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3874602301). |
| Unknown or unmapped coverage has no determinate acceptance outcome. | D3-1 makes every provenance Unknown, unmapped CC-SPEC-8 row, or CC-SPEC-11 Unknown row block acceptance; the acceptance review records `Unknown`, names settling conditions, and leaves the unit a candidate. |
| Coverage enumeration is still author-selected; retirement is incomplete. | D3-1 enumerates whole-capability sources and a full focused-change baseline denominator before classification, gives each row identity/source/method, and places retired entries explicitly in `lawfully out of scope / retired`. |
| The impact sweep population is defined by what was examined. | D3-11 freezes every accepted specification and stable requirement entry at a named source revision before matching, with revision, method, and both denominators recorded. |
| Impact sets are not disjoint/exhaustive and requirement results do not propagate to specifications. | D3-11 partitions every requirement once, derives every specification once, and states that affected and undecidable requirement results propagate to the parent specification. |
| Unknown has no operational record/render home. | D3-1 uses the requirement, CC-SPEC-8 matrix row, and CC-SPEC-11 table row as owners; D3-11 uses the impact-sweep row. Human and machine projections render the same Unknown and link to that row. |
| Mutable current-state prose remains in the active path. | D3-7 and D3-10 make authority claims act-conditional, make sweep methods record-owned, remove queue-state prose, and state historical evidence as a fixed record pointer rather than a repeated current verdict. |
| Necessary external terms cannot be applied locally. | CC-SPEC-2 defines materiality and the work/provenance split; CC-SPEC-8 states the reviewed-N/A owner gate; CC-IMPACT-3 defines affected; CC-IMPACT-6 defines same logical change; the reading guide gives the local consequence for each. |
| Vocabulary consumption has no definition in this amendment. | Explicit residual, not repaired by invention: CC-IMPACT-2 checks the named revision for an eligible accepted definition and, when none exists, CC-IMPACT-4 routes every dependent relationship to `undecidable`/Unknown pending separately authorized definition. |

No row above changes accepted contract text, decides P-43, revives P-44, or
opens deferred Mission or context-selection scope. These corrections move the
head and require entirely new semantic and fresh-reader reviews; this authoring
pass claims neither verdict.

## Appendix G — Option A correction-cycle-1 dispositions

At `5f4e6a9cf7fbbe4c12db84dfe63bb36a569e120d`, the entirely new semantic
review returned **`VERDICT: REVISE`** and the entirely new reader returned
**`FRESH-READER REVISE`**. The semantic inline thread is resolvable below; the
complete raw reports are not stored in a clone-resolvable home, and the review
issue carries only their structured summary.

| Finding | Disposition in this correction |
|---|---|
| [D3-2 class is not Clarifying](https://github.com/Tzeusy/syzygy/pull/5#discussion_r3876818681) | Verified against the act-bound predecessor: the materiality test and acceptance-blocking Unknown are new obligations. D3-2 is now `Normative`. The same class test makes D3-4 `Normative` because it adds a mandatory consequence denominator and segmentation blocker. |
| CC-SPEC-8 has no reproducible initial consequence population. | D3-4 enumerates every accepted contract module, defined clause, and deterministic source unit before applicability; assigns local consequence IDs; records module/clause/consequence denominators; and makes segmentation uncertainty Unknown that defers acceptance. |
| CC-SPEC-11 extraction, segmentation, and deduplication remain subjective. | D3-1 defines source units, falsifiable splitting, source ordinals, stable/table-local IDs, exact-locator deduplication only, and an Unknown result for unsettled segmentation. |
| CC-SPEC-11 source relationships permit circular self-mapping. | D3-1 states source-type relations: scope rows map to requirement IDs; active requirement rows map back to independently extracted scope/change rows and cannot self-cover; non-goals must not be claimed by active requirements; retired rows stay retired; circular or contradictory relations are Unknown and block acceptance. |
| `contradicted` floats outside CC-IMPACT's exhaustive partition. | D3-11 adds `contradicted` as the highest-precedence fourth result at both requirement and specification level. Each population member occupies exactly one result set. |
| Active adoption records have no locally applicable corpus or supersession selection. | D3-7 selects owner Decisions in `.syzygy/governance/decisions/` at the named revision, matches stable artifact identity/digest, follows only explicit RFC3-16(b) supersession/revocation, and treats incompatible unsuperseded records as contradiction/Unknown. CC-IMPACT-3 reuses that selection for its accepted-specification corpus. |
| Reviewed-N/A verification lacks a local yes/no decision. | D3-4 says yes only when exact consequence/scope and independently kept evidence resolve and match the local RFC3-16(b) bindings; any absent, unresolvable, or mismatched binding means no, records Unknown, and leaves the consequence unmapped. |
| Mutable current-state claims remain. | Definition availability is now resolved at each sweep's named revision; authority state and supersession are record-derived; queue and ambient script/gate claims remain absent. Historical evidence stays a fixed record pointer rather than a repeated current verdict. |

These corrections alter no accepted contract and introduce no owner-selected
precedence. They move the head and require another entirely new semantic and
fresh-reader review; this correction pass claims neither pass.
