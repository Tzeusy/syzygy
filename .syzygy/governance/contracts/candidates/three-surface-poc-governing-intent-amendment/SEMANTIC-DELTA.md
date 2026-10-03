# Semantic delta — governing intent on every work item (Three-Surface POC)

> **Candidate — binds nothing.** These bytes were drafted under the owner's
> 2026-10-03 overnight direction,
> `.syzygy/governance/decisions/OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md`,
> for bead `syzygy-u05.10` (vision pursuit 2026-09-22, move N10). That
> direction permits drafting; it performs no act. Only the owner's sign-off of
> this package amends the signed three-surface-poc-experience specification
> (VIS-4). This candidate edits no signed byte and authorizes no
> implementation.

**Artifact(s):** four of the six signed artifacts of
`openspec/changes/three-surface-poc-experience/`, bound since 2026-09-29 by
`.syzygy/governance/decisions/THREE-SURFACE-POC-READABILITY-SUCCESSOR-ACT.md`:
`specs/three-surface-poc-experience/spec.md`, `CONTRACT-COVERAGE.md`,
`GOVERNING-DEPENDENCIES.md` and `proposal.md`. Proposed bytes exist only as
the four unified diffs under `proposed/`. `.openspec.yaml` and `design.md`
stay byte-identical.

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
holding exactly one of:

- an **edge** to the warrant the item was materialized under, joined by a
  recorded identity; or
- **Unknown** with exactly one primary reason from RFC2-24's closed list and
  that reason's route.

It forbids deriving an edge from a title or any other work-item text by
matching, similarity or inference. Both channels serve the edge and Unknown
counts over the served item set; Trajectory marks each Unknown item, shows
the count, and lets a reader narrow the board to those items. An Unknown item
is never rendered as warranted, green, complete or orphaned.

It admits no column. Its *Scope* line says the projection stays as POC-REQ-010
to POC-REQ-013 bound it, and that while no admitted input carries a warrant,
every served item is Unknown with the reason
`source-uncaptured-or-unreachable`.

## Why each choice

**The clauses mapped.**

- **RFC8-23** is the shape of the Unknown. It reads: "A work item, run, or
  merged change with **no traceable warrant** renders **Unknown-provenance**:
  a first-class, filterable, counted rendered state — never green, never
  silently pooled into warranted work, and never an ingest rejection
  (RFC4-10)." Its route for such an item is "*surface it*: counted, never
  green, resolvable by supplying a warrant". The requirement's count, marker
  and narrowed view are this clause's consequences.
- **RFC8-22** is the prohibition. It reads: "Reconstructing a join by
  similarity, interpolation, or inference is forbidden", and, where a link
  cannot be established, "the chain renders the break at that link — Unknown
  with its RFC2-24 reason". The planted-title counterexample observes it.
- **RFC4-15** is mapped for its authority limb, "never intent": the same
  counterexample observes that no work-item text becomes a governing intent.
- **RFC2-24** is mapped because every Unknown must carry one reason from its
  closed list.

**The reason: `source-uncaptured-or-unreachable` (RFC2-24 #10).** Its
condition reads: "A deterministic input capable of affecting the claim was not
captured in the snapshot (RFC2-2), including observer failure and unreachable
sources." That is exactly the POC's position: whatever could carry a warrant
— Syzygy's own materialization record or a substrate provenance field — is not
captured. Two other reasons were weighed and rejected:

- `missing-declaration` (#1) asserts that "No governing declaration
  (capability, topology, mapping, policy) exists". The POC cannot know that,
  since it reads nothing that would show one; asserting absence without
  evidence is what VIS-2 forbids. RFC8-24 lists this reason among those
  Trajectory renders, but for "a governing declaration … absent behind a
  claim", which the POC has not observed.
- `unconsented-source-or-provider` (#6) has the condition "SEC-2/SEC-4
  consent absent or withdrawn for a needed repository or model provider". The
  Butlers repository is consented; what is missing is an admitted column, not
  repository consent. [Inferred.]

**Why no edge exists today.** No admitted input carries a warrant: none of
the nine read expressions names one, and the one bead the POC materializes
records no governing intent in Syzygy's stored record (point 2 above).
[Inferred from the code at `c371339d`.] So the requirement is met today only
by rendering all N items Unknown.

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
- It does not settle the orphaned-work limb of RFC8-23: the POC detects no
  orphaned work, so that limb has its own Unknown amendment row.

## Overlap with the identity amendment (P-84)

`three-surface-poc-identity-amendment/` also patches `spec.md`,
`CONTRACT-COVERAGE.md`, `GOVERNING-DEPENDENCIES.md` and `proposal.md`, and
both packages were cut against the same signed bytes. Their hunks touch
neighbouring lines: the reader-note group list, the family table and totals,
and the insertion point before `## Acceptance inputs`. Whichever package is
signed second must be regenerated against the first one's applied bytes
before its sign-off. Neither package changes the other's requirements.
