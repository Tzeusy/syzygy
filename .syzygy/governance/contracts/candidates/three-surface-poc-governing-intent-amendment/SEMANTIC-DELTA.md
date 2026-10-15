# Semantic delta — governing intent on every work item (Three-Surface POC)

> **Candidate — binds nothing.** These bytes were drafted under the owner's
> 2026-10-03 overnight direction,
> `.syzygy/governance/decisions/OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md`,
> for bead `syzygy-u05.10` (vision pursuit 2026-09-22, move N10). That
> direction permits drafting; it performs no act. Only the owner's sign-off of
> this package amends the signed three-surface-poc-experience specification
> (VIS-4). This candidate edits no signed byte and authorizes no
> implementation.

**State:** round-2 findings repaired once on 2026-10-14, unconfirmed pending
round 3. The mapping from each round-2 finding to its repair is in
`ROUND-2-DISPOSITIONS.md` §"Repairs, 2026-10-14 (cycle 2)".

**Artifact(s):** four of the six signed artifacts of
`openspec/changes/three-surface-poc-experience/`, bound since 2026-09-29 by
`.syzygy/governance/decisions/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md`:
`specs/three-surface-poc-experience/spec.md`, `CONTRACT-COVERAGE.md`,
`GOVERNING-DEPENDENCIES.md` and `proposal.md`. Two of them, `spec.md` and
`GOVERNING-DEPENDENCIES.md`, changed again on 2026-10-14 when the owner
signed the block-provenance amendment v1.0 (P-97,
`.syzygy/governance/decisions/THREE-SURFACE-POC-BLOCK-PROVENANCE-AMENDMENT-SIGNOFF-v1.0.md`).
Proposed bytes exist only as the four unified diffs under `proposed/`,
regenerated on 2026-10-14 over those signed bytes at `origin/main`
`814fbcc1`. `.openspec.yaml` and `design.md` stay byte-identical.

**Stable IDs affected:**

- **Minted:** `POC-REQ-014`, in the *Work-item observation* group, whose
  reader-note range becomes 010–014.
- **Amended in place:** none.
- **Not touched:** no other requirement, contract clause, reason or
  identifier is minted, retired or renumbered.

**Change class:** **Normative.** It adds an obligation the POC does not meet
today: no served work item carries a governing-intent field at all.
[Observed: the `WorkItemFact` projection in
`packages/three-surface-poc-core/src/work-items.ts` at `c371339d` reads no
such field. Inferred: the compliance consequence.]

**Author:** Claude worker lane for `syzygy-u05.10`.

**Date:** 2026-10-03

## Why the package is narrower than the bead

The bead, as written by the pursuit, asked for a delta that widens the
work-item read to the `external_ref`, `description` and `design` columns and
extracts governing-intent identifiers from their text. The premise check
found that this needs owner acts the overnight direction does not cover, so
the coordinator narrowed the work on 2026-10-03 (bead notes, `syzygy-u05.10`):

- **(a)** this drafting-only delta: `governedBy` renders Unknown over a
  counted denominator with a closed reason, and no new column is read;
- **(b)** an owner decision packet, register row P-100, on whether to open a
  Beads-text content class at all (`OWNER-DECISION-PACKET.md` here);
- **(c)** the source-to-claims direction (`claimsBySourceAnchor`) deferred,
  because it belongs to the PWB category and the shared-model work-in-progress
  order.

The conflicts the premise check found, quoted from the accepted clauses:

1. **Beads is not an intent source.** RFC4-15, the Beads adapter's read
   contract, gives its authority as "work lifecycle state, after
   materialization only (SDR-7) — never intent, never observed behavior, never
   why the work exists". Its *Reads* list names "assignee; dependency edges
   with their types; labels; `external_ref`; notes blocks as opaque annotated
   text; created/updated/closed instants; and transition history". It names
   neither `description` nor `design`. Reading those two columns as intent
   would need an RFC 0004 amendment, not only consent. [Observed: the clause
   text at `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`.]
2. **Syzygy's own record is where the warrant lives.** RFC4-17 says that at
   materialization the adapter writes the warrant reference "into the
   substrate's provenance field (`spec_id`/metadata) as a **derived,
   re-derivable pointer**", and that "the `.syzygy/work/**` materialization
   record stays authoritative". [Observed: same file.] No `.syzygy/work/`
   directory exists at `c371339d`. The POC's own materialization record type,
   `MaterializationRecord` in
   `packages/three-surface-poc-core/src/materialization.ts`, carries no
   governing-intent field, although the packet it is written from does.
   [Observed.]
3. **No new Butlers content class without three owner acts.** Reading any
   work-item column beyond the nine the POC reads today is a new class of
   Butlers content. It needs the owner's consent scope, a secret-policy
   extension and a registry entry (PWB-REQ-005; SEC-5). [Inferred from the
   consent record's scope, which names Git objects selected by the PWB
   specification's closed source population, and the secret policy's single
   content class, `declared-project-shape-text`.]

## What the delta says

POC-REQ-014 requires every served work item to carry a `governedBy` field
whose value, under this specification, is always **Unknown** with the reason
`source-uncaptured-or-unreachable` and the route RFC2-24 gives that reason.

- Both channels serve how many items carry that Unknown, over the served item
  set ("N of N").
- Trajectory shows that count beside how many of the items its rendered
  selection holds and how many fall outside it. Signed POC-REQ-042 lets
  Trajectory render a bounded selection (its scenario: 192 of 6,964 items),
  so the item-level arms reach only the items Trajectory renders; the rest
  are counted, not shown.
- Beside the count, Trajectory states the reason, its route and that an item
  is resolved by supplying its warrant. It marks every item it renders, and
  lets a reader narrow the board to the marked items.
- Every item Trajectory renders shows its governing intent with the encoding
  POC-REQ-060's declared table gives Unknown, never an encoding for a
  warranted, green or complete state.
- Nothing served takes a governing intent from a title. A fixture item whose
  title names a requirement must still read Unknown.

It admits no column or other input, and it **defines no edge**. Its *Scope*
says the projection stays as POC-REQ-010 to POC-REQ-013 bound it, and that an
edge to a warrant, and the input that would carry one, need a further
amendment. This is deliberate: an edge arm with no admitted source would be
an arm no oracle can reach (CC-SPEC-4). Whatever P-100 decides, the edge comes
in its own amendment, with the input it rests on.

The same reasoning removes the orphaned-work sentence round 1 added. The POC
detects no orphaned work, so "no Unknown marker SHALL replace or hide an
orphaned-work Contradiction" was a SHALL no checker could produce a case for.
The *Scope* now says the requirement makes no claim about orphaned work, and
that RFC8-23's rule (the Contradiction governs) is left to the amendment that
specifies orphaned-work detection. The matrix keeps that limb as Unknown.

**Form.** The requirement is one invariant over the served item set and
Trajectory's rendered selection. Its "never" sentences are stated as
properties every item holds, so they are checked by the same sweeps, not as
separate prohibitions.

**Denominators.** The oracle has two, each the checker's own enumeration.
The machine-answer arms run over the served item set, as in POC-REQ-011. The
Trajectory arms run over the items Trajectory renders, before and after
narrowing; Trajectory's inside figure must equal that enumeration, and inside
plus outside must equal the served count. An item dropped before serving is
invisible to this oracle; POC-REQ-042 reconciles the rendered and excluded
counts against the database total, and the matrix lists the "never an
ingest rejection" limb of RFC8-23 as Unknown.

**How each Trajectory arm is decided.** Round 2 found that the oracle named
the marker, the resolution sentence and the non-green rendering only in the
observable and falsifier. Each now has a stated procedure:

- **The marker and the non-green rendering** are one check: every rendered
  item's governing-intent encoding equals the encoding POC-REQ-060's
  checked-in table gives Unknown, and none carries an encoding the table
  gives another state. This is how POC-REQ-043 decides its verification
  encoding: against a declared expected value, not by eye.
- **The resolution statement**: the region holding the count, read as text
  alone (RFC8-31), contains the reason name and its RFC2-24 route literally,
  and the word "warrant" in a statement that supplying it resolves an item.
  The exact wording is the implementation's; the literal parts are not.
- **Narrowing**: the narrowed board lists exactly the items the un-narrowed
  board renders, because every one carries the Unknown.

## Why each choice

**The clauses mapped.** Each newly covered row claims only what POC-REQ-014's
oracle observes; every other limb of a newly mapped clause has its own Unknown
amendment row in `CONTRACT-COVERAGE.md`.

- **RFC8-23** is the shape of the Unknown. It reads: "A work item, run, or
  merged change with **no traceable warrant** renders **Unknown-provenance**:
  a first-class, filterable, counted rendered state — never green, never
  silently pooled into warranted work, and never an ingest rejection
  (RFC4-10)." Its route for such an item is "*surface it*: counted, never
  green, resolvable by supplying a warrant". Covered: counted over the served
  set, filterable within Trajectory's rendered selection, never green (the
  encoding check), and the route stated beside the count (the literal
  check). Unknown: filtering items outside the rendered selection (POC-REQ-042
  lets Trajectory count them without rendering them), "never silently
  pooled" (no warranted population exists to pool into), "never an ingest
  rejection" (see *Denominators*), the substrate-side warrant-field
  annotation (the POC reads no warrant field), and the orphaned-work limb
  (the POC detects no orphaned work).
- **RFC8-22** is the prohibition. It reads: "Where a link cannot be
  established at the answering evaluation, the chain renders the break at that
  link — Unknown with its RFC2-24 reason — and everything downstream renders
  with provenance degraded accordingly", and "Reconstructing a join by
  similarity, interpolation, or inference is forbidden". Covered: the first
  link, work item to warrant, renders Unknown with its reason; and no join is
  reconstructed (observed for the title case). Unknown: downstream
  degradation, since the POC renders no link downstream of the work item.
- **RFC8-24** reads: "The RFC2-24 reasons Trajectory most renders **on its
  claims**, each with its route visible", and lists
  `source-uncaptured-or-unreachable` among them. It goes on: "Unknown
  aggregation follows RFC2-24's rendering rule: aggregate, disclose reason
  counts, expand. **These are claim reasons only:** the normalized state's
  four absence values are state-local, take no reason from this list, and
  are counted separately — an aggregate of Unknowns never absorbs them
  (RFC8-12; RFC6-6)." Covered: Trajectory renders that reason with its route
  on the governing-intent claim; and the aggregation rule as far as the
  oracle observes it — one count, whose single reason makes it that reason's
  count, expanding to its members within the rendered selection (the
  narrowed board). Unknown: the other four reasons it lists; a retention loss
  rendered "citing the retention event"; expansion to members outside the
  rendered selection, and the full RFC6-17 disclosure that RFC2-24's
  rendering rule says any aggregate owes; and the claim-reasons-only limb,
  since Trajectory renders no RFC8-12 normalized state with absence values
  for an aggregate to absorb.
- **RFC4-15** is mapped for its authority limb, "never intent". Covered: the
  title, the only free text the POC reads, is never read as governing intent.
- **RFC2-24** is mapped because every Unknown carries one reason from its
  closed list. Its signed reason-#10 row now names POC-REQ-014 beside
  POC-REQ-003 and POC-REQ-013, because 014's oracle reads that exact reason
  and route.

**RFC8-21 moves from Part B2 to Part B1.** Round 1's text kept it in Part
B2, on the ground that its signed rationale, "POC deliberately leaves this
relationship Unknown, building no chain", stayed true. Round 2 (note 7)
answered that "leaves it Unknown" is a statement about coverage, not about
applicability. Part B2 is for clauses governing machinery the POC "neither
renders, stores, transitions, queries, nor crosses"; once POC-REQ-014
renders the chain's first link, work item to warrant, as Unknown, the POC
renders part of the chain RFC8-21 governs, and RFC8-22, a clause about that
same chain's broken joins, is already in Part A. So RFC8-21 is applicable and
uncovered: Part B1, one Unknown row, "no requirement walks the chain or
renders any other link". Its signed B2 row is removed by the patch, as the
other three are.

**The reason: `source-uncaptured-or-unreachable` (RFC2-24 #10).** Its
condition reads: "A deterministic input capable of affecting the claim was not
captured in the snapshot (RFC2-2), including observer failure and unreachable
sources." That is exactly the POC's position: whatever could carry a warrant
— Syzygy's own materialization record or a substrate provenance field — is not
captured. The other reasons were weighed and rejected:

- `missing-declaration` (#1) asserts that "No governing declaration
  (capability, topology, mapping, policy) exists". The POC cannot know that,
  since it reads nothing that would show one; asserting absence without
  evidence is what VIS-2 forbids.
- `missing-evidence` (#2) has the condition "Declaration exists; no current
  evidence artifact for the claim". It asserts that a declaration exists,
  which the POC equally cannot know.
- `mapping-coverage-absent` (#5) has the condition "No executed mapping with
  stated coverage backs the claim (empty-plot rule: absence claims need a
  coverage record)". The POC makes no absence claim, and what is missing is an
  uncaptured input, not an unrun mapping.
- `unconsented-source-or-provider` (#6) has the condition "SEC-2/SEC-4
  consent absent or withdrawn for a needed repository or model provider". The
  Butlers repository is consented; what is missing is an admitted column, not
  repository consent. [Inferred.]
- `excluded-content` (#7) has the condition "Secret-detection policy excluded
  the content, or it was unclassifiable (fails closed, SEC-5)". No content was
  excluded by a policy; the columns were never read.

**Where #10 fits weakly, stated.** Round 2 (note 7) judged #10 the best fit
of the reasons weighed, and named two weaknesses. Both are stated here
rather than argued away.

- **Its route will not resolve this Unknown by itself.** RFC2-24 gives #10
  the route "Repair the observer/source; new snapshot". Here no observer is
  broken: the input that could carry a warrant is not admitted. Only an owner
  act and a further amendment (P-100 Q1) can admit one, and only then would a
  new snapshot help. The requirement still serves this route with the
  reason. RFC2-24 says "RFC6-14 requires every machine answer to carry its
  Unknown reason **verbatim from this vocabulary**", and its rendering rule
  says "every reason routes to its resolving action"; the route served is
  the one RFC2-24's table gives the reason. [Inferred: that "repair the
  source" reads, in this case, as "admit a source", and that serving a
  different route would misstate the reason.]
- **RFC8-24's gloss names neither the POC's case.** Its parenthetical for
  #10 reads "adapter export unavailable; facts lost past the retention
  horizon before capture". The POC's case is a third one: a column never
  admitted. The gloss gives examples, not a closed list, so the reason still
  applies [Inferred], but the fit is by RFC2-24's condition text, not by
  RFC8-24's examples.

**RFC8-23's resolution, stated beside the count.** RFC8-23 gives an item
with no traceable warrant the route "*surface it*: counted, never green,
resolvable by supplying a warrant", noting such an item "may be legitimate
untraceable work — a pre-Syzygy backlog item, an import". Trajectory states
that resolution beside the count because RFC8-23 itself requires it of this
state. It is neither a second reason nor a second RFC2-24 route. Round 1's
text rested this on RFC2-24's sentence that a condition "genuinely not among
the twelve is disclosed as a **fact of the render**"; round 2 found that a
stretch, since the condition here is among the twelve. The text no longer
relies on that sentence.

**Why no edge can exist today.** No admitted input carries a warrant: none of
the nine read expressions names one, and the materialization record the POC
would store for the at most one bead its action may create (a code bound,
`MATERIALIZATION_EXTERNAL_REF`) has no governing-intent field (point 2
above). Whether any such bead was created is [Unknown]. [Inferred from the
code at `c371339d`.]

**`external_ref` is not wholly untouched.** The POC's materialization action,
`findByExternalRef` in `packages/three-surface-poc-core/src/materialization.ts`,
finds the bead it created by filtering on `external_ref` equal to the value it
wrote itself, and returns only `id`. [Observed at `c371339d`.] That filter
reads no row's `external_ref` value into the POC, so the projection's nine
expressions stay the whole of what is read; the owner packet says so.

**What is not claimed.** The requirement does not say no warrant exists for
any Butlers item. Whether any Butlers row carries a warrant reference in
`external_ref`, `spec_id` or any other column is **[Unknown]**: those columns
are outside the admitted nine and were not read for this package's evidence.
The answer waits on P-100.

## Figures, measured at named revisions

- [Observed] The work-item projection reads nine expressions, one of them
  the work lifecycle `status` column — `dolt_hashof('HEAD')`, `id`, `title`, `status`, `issue_type`, `priority`,
  `created_at`, `updated_at`, `closed_at` — at
  `packages/three-surface-poc-core/src/work-items.ts:86-88`, Syzygy commit
  `c371339d`.
- [Observed] 7,958 rows under the `bu-` prefix, 168 of them in the work
  lifecycle state `blocked`, at Butlers Dolt revision
  `p1ej266j4o1ge6dn4fei2dlv80tmqopr`, counted 2026-10-03 over the admitted
  `id` and work lifecycle `status` columns only. The
  pursuit dossier's 7,527 and 141 are an earlier capture.
- [Unknown] The contents of `external_ref`, `description`, `design` and
  `spec_id` in the Butlers database.

## What this delta does not do

- It reads no new column and adds no Butlers content class.
- It does not create `.syzygy/work/` or extend the materialization record;
  that is an option in P-100, not part of this delta.
- It does not touch the PWB specification or the shared model's
  source-to-claims index (deferred item (c)).
- It does not render governing intent on Polaris or Orrery.
- It defines no edge to a warrant; that needs a further amendment.
- It does not settle the orphaned-work limb of RFC8-23: the POC detects no
  orphaned work, so that limb has its own Unknown amendment row.

## Overlap with sibling packages (P-97, P-84)

Two other packages patch the same specification. Round 2 (finding 4) found
that this section named only P-84.

- **The block-provenance amendment (P-97), signed v1.0 on 2026-10-14.**
  `three-surface-poc-block-provenance-amendment/` patched `spec.md`
  (POC-REQ-001 and POC-REQ-010) and the `Source:` line of
  `GOVERNING-DEPENDENCIES.md`. [Observed 2026-10-14, at `814fbcc1`, where it
  is signed:] this package's round-2 `spec.md.patch` still applied (hunk 2 at
  offset 54) and its `GOVERNING-DEPENDENCIES.md.patch` failed at that
  `Source:` line, as round 2 found. All four patches were therefore
  regenerated over the signed bytes at `814fbcc1`: the spec, matrix and
  proposal edits in a scratch worktree, and `GOVERNING-DEPENDENCIES.md` only
  by `scripts/build_three_surface_poc_spec_dependencies.py` over the proposed
  `spec.md`. Each now passes `git apply --check` there. The two packages
  share no requirement or clause row. P-97 bars a work-item fact from
  carrying the observation's Dolt revision or capture instant; `governedBy`
  holds neither. [Inferred]
- **The identity amendment (P-84), unsigned.**
  `three-surface-poc-identity-amendment/` also patches `spec.md`,
  `CONTRACT-COVERAGE.md`, `GOVERNING-DEPENDENCIES.md` and `proposal.md`.
  Their hunks touch neighbouring lines: the reader-note group list, the
  family table and totals, and the insertion point before
  `## Acceptance inputs`. The P-97 builder declares the two a mutually
  exclusive pair (a coordinator's process ruling of 2026-10-04, not an owner
  act): no order applies both as drafted, so whichever is signed second must
  be regenerated against the first one's applied bytes before its sign-off.
  P-84 is being repaired in a separate lane the same day; this package does
  not edit it, and composition with its repaired bytes is not re-tested
  here. Neither package changes the other's requirements.
