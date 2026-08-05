---
id: RFC-0009
title: Orrery (Map Surface) — non-3D equivalence, release gates, performance, motion, phase boundary
status_source: owner-act-record
module: interaction-parity-and-release
clauses: RFC9-46..RFC9-52 (sub-clause RFC9-47(a); no gaps, no retirements)
governs: [non-3d-equivalence, accessibility-parity, release-gate, gate-registry-maintenance, performance-budget, declared-scope-narrowing, motion, illumination, openspec-phase-boundary]
applies_to: [orrery, machine-clients]
depends_on: [RFC-0002, RFC-0006, RFC-0008]
provides_to: [RFC-0007, RFC-0008, RFC-0010, RFC-0011]
tags: [surface, equivalence, accessibility, release-gate, sdr-26, sdr-27, vis-1, vis-7]
---

# RFC 0009 — Orrery (Map Surface): non-3D equivalence, release gates, performance, motion, phase boundary

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until the
independent A1 correlation mechanism exists, and as a Syzygy-verified effective
act only after correlation (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 3 of 3 of the RFC 0009 contract package. Index and lookup
rule: `README.md`. Rationale, amendment history, alternatives, and answered §8
questions: `../../history/RFC-0009-history.md`.

**Serves:** VIS-1, VIS-7 (trust floor); architecture.md (exact 2D/tabular
equivalents); v1.md (keyboard navigation in V0 scope; comprehension test);
SDR-26, SDR-27; vision.md (Performance).

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **how the surface is checked and where its authority stops**:
the 3D/non-3D equivalence obligation and accessibility parity; the release-gate
list craft-and-care consumes, and the rule that keeps that list complete;
performance as declared scope-narrowing rather than silent decimation; motion and
illumination; and the binding phase rule that stops this RFC being read as an
implementable behavioral spec.

Position, anchoring, layout determinism and counting live in
`semantic-geography.md` (RFC9-1..RFC9-23); palette, channels, lenses, scenes and
aggregation in `visual-grammar-and-lenses.md` (RFC9-24..RFC9-45).

Two orientations: **non-3D views are co-equal** — same evaluation, same facts,
same counts, and a table and the scene disagreeing over one scope is
release-blocking — and **truth is never purchased with frame rate**.

---

## 1. Non-3D equivalence and accessibility (SDR-27)

**RFC9-46.** Non-3D views (2D, tabular) are **co-equal product surfaces** — the
precision, debugging, and assistive-technology paths — not derived exports. For
one (evaluation, scenario context, lens, declared filter scope), the 3D scene and
the non-3D view are equivalent per RFC6-22/23: same entity set, same edges, same
epistemic states (label + tier + reason + freshness **and sibling surface
states**), same counts, same evidence links, same scenario context, and —
wherever the work/construction overlay is active — **both work-state fields: the
normalized work state and the RFC2-18 chain state** (RFC9-32; RFC8-12/8-28). A
tabular view that carries the normalized state and drops the chain state is not a
finer-detail difference under RFC6-23; it answers the reconciliation question
differently from the scene, which is precisely the disagreement RFC6-23 forbids.
Non-3D views may expose finer detail than an aggregated scene — a disclosed
aggregation difference, never a contradiction (RFC6-23).

**Added to the tuple at acceptance: the positional-expression state and the
backlog partitions.** The tuple additionally carries, for the same (evaluation,
scenario context, lens, declared filter scope):

- the **RFC9-9(b) positional-expression state** — `honored` / `not-honored` /
  `unknown` — for every rendered `declared-dependency` edge; and
- **both RFC9-15(b) part 4 partition counts**, refresh-clearable and structurally
  unhonorable, separately (the unpartitioned total is not a lawful rendering on
  either surface).

**These are not statements about pixels, and the table does not compute them from
its own geometry.** The state is a function of the layout input tuple (RFC9-14)
and is evaluated against the **recorded base layout** (RFC2-6), which is a
governed artifact both surfaces read. A tabular view therefore has everything it
needs, and an implementation that derives the count from a table's non-existent
geography and reports `0` has not found a limit of the tabular surface — it has
read the wrong artifact. Scene says 12 and table says 0 over the same declared
scope is an RFC6-23 release-blocking disagreement, and it is inside the gate
rather than outside it.

*Why this one matters beyond bookkeeping:* the tabular view is RFC9-48's
designated screen-reader surface. Without these fields a screen-reader user could
not learn from **any** surface available to them that the layout is twelve
declarations behind and a refresh is due — while a sighted reader sees it
prominently. That is a parity failure, not a detail difference.

[**A maintenance note, not a ruling.** This tuple is a **hand-maintained
enumeration**, not a list derived from anything: it restates RFC6-22's
cross-surface tuple and then names, item by item, the surface-local fields this
surface adds — the work-state pair being the current instance. Whether an
equivalence tuple should enumerate surface-local fields *in general*, or be
defined so they cross automatically, is **unresolved and belongs to RFC6-22 at
the foundation layer**, not to this clause. Until it is resolved, anyone adding a
surface-local field that a reader could act on must add it here explicitly; an
omission does not fail loudly anywhere.]

**RFC9-47.** **The equivalence gate is a release check** for Syzygy's own
releases, alongside: layout determinism (two runs, one evaluation, identical base
layout); refactor stability (mapping-preserving refactor moves nothing);
append-stability (RFC9-15, fixture-tested); no double-counting (RFC9-21,
fixture-tested); legend completeness and registry-generated legend text
(RFC9-26); Unknown coverage (no Unknown renders green or absent, every reason
rendered, **including the aggregate form of RFC9-27 — no aggregated measured
channel renders without its Unknown contribution, RFC9-43**); empty-plot coverage
records (RFC9-27, at every level of the hierarchy and in the approved-intent and
proposed scenes); **proposed-scene fidelity** (RFC9-40: the exclusivity-group
union refusal — no scene unions proposals in one exclusivity group or of
undeclared compatibility, the honest render being *N candidate futures* selectable
one at a time; and **proposed structure never looks like existing structure in
any profile at any zoom**, checked per profile and per zoom step, since a
proposed district that reads as built is the most seductive lie this surface can
tell); **work-state two-field consumption** (RFC9-32: every element and every
aggregate that carries a normalized work state carries its RFC2-18 chain state
beside it — no rendering, filter, count, legend entry, or tabular row shows one
in place of the other; and `unsatisfied` and `contradiction-raised` never share a
mark, a mark's color, a count, or a legend entry with each other, with `merged`,
or with `reconciled@E`, per RFC2-17's word reservation and RFC8-28 — run against
a fixture carrying **every chain outcome the release can produce**, co-located on
one district, since a gate exercised only over merged-not-yet-evaluated data
passes vacuously; per RFC8-29 that is `merged`, `reconciliation-pending` and
`Unknown(reason)` at V0, the verdict-bearing outcomes entering the fixture with
the V1 computation that first produces them); **declared-vs-observed relation
separation** (RFC9-9: every rendered profile relation legends as itself with its
profile and state class named — the registry side of this is already covered by
legend completeness above — and no declared project-scope edge shares a mark, a
channel treatment, a legend entry, or a count with an observed `depends_on` edge,
RFC1-25's anti-conflation rule run as a rendering check; exercised over a
portfolio fixture carrying both an observed intra-project dependency and a
declared `depends-on` edge, since a single-project fixture cannot reach it); LOD
epistemic invariance (RFC9-42); link resolution for every map entity; secret
exclusion (RFC9-29, including the minimum-aggregation granularity bound); **the
masquerade check** (no view binds position or proximity to a metric without the
analytical-plane marker — RFC9-11 makes this a violation identical in class to an
unlegended channel, VIS-7); **non-visual parity** (RFC9-48: full keyboard
navigation of every action, tabular equivalent as the screen-reader surface,
textual epistemic labels for every state, reduced-motion honored — accessibility
is a truth requirement, and keyboard navigation is V0 scope per v1.md); **no
ambient motion** (RFC9-50); **encoding explainability** (RFC9-3: every rendered
encoding traceable to an identified artifact, with the RFC9-26 fail-closed rule —
no channel renders without a registry entry).

**Six layout obligations added at acceptance** *(from the B12(a)/B12(b)/A3
amendments; §4 case 3a names four of them as violation cases)*:

- **Order-independence** (RFC9-15(b) part 3): the same layout input tuple
  presented in any order yields identical coordinates. **The existing "two runs,
  one evaluation" determinism check does not cover this** — two runs inside one
  implementation share an insertion order by construction, so the natural
  implementation (iterate declarations in adoption order, pack greedily) passes
  every gate on this list and fails only after release, when a second
  implementation or a re-ordered cache rebuild disagrees. The check must permute
  the declaration set, not repeat it.
- **Baseline recording** (RFC9-14(a)): the layout baseline exists as an
  identified artifact and the recorded base layout reproduces from (declaration
  set, baseline, version). A base layout that is checkable but not reproducible
  fails here.
- **Full-not-scoped regeneration** (part 2): a refresh repositions every district;
  a scoped refresh is rejected, not honored partially.
- **Not-honored rendering** (part 1, RFC9-9(b)): an unhonorable declared
  relatedness edge renders `not-honored` — never as honored, never Unknown, never
  nothing — with its registry entry present and its Unknown value exercised by an
  edge with an unplaced endpoint.
- **Backlog partitioning** (part 4): both counts render separately and an
  unpartitioned total does not render, on both surfaces (RFC9-46).
- **The carve-out demonstration is actually run** (RFC9-16(d)): a layout version
  shipped under the note-only route carries a recorded layout-equivalence check
  result. An asserted equivalence fails the gate.

**Also gated: the residual-adjacency legend line** (RFC9-9(a)) — the
position/proximity registry entry declares all three readings, and residual
placement produces no enclosure, shared boundary, plinth or common ground plane
that mimics declared containment. This one is partly a judged check rather than a
computed one, and is named here rather than omitted for that reason.

**And: stale-layout personal state** (RFC9-13(a)) — a saved camera home carrying
an older layout version does not restore silently; run against a fixture that
bumps the version between save and restore, since a single-version fixture cannot
reach the failure.

**And: the walkthrough artifacts' completeness and the fail-closed gate**
(RFC9-45) — an execution record naming no evaluation, layout version, baseline,
scenario context, lens or filter scope is not a lawful record; an unattributed or
unreasoned judgment blocks release rather than clearing it; and a pass may clear
release only through the adopted release policy, never because a verdict is
stored.

[Inferred — the checkable form of the trust floor for this surface; the gates'
place in the release process is craft-and-care material. **This list is what
craft-and-care consumes, so an obligation absent from it is tested nowhere** —
demonstrated twice, once by a review finding six absences and once by a review
finding the equivalence tuple short of two fields the gate then could not see.]

**RFC9-47(a) — The registry maintains itself or it is wrong.** A hand-maintained
enumeration whose completeness is checked only by luck is not a release gate, it
is a hope. Two obligations make the list self-maintaining:

1. **The same-logical-change invariant.** Any amendment to this RFC — or to a
   contract this RFC consumes — that **creates, removes, or changes a
   release-blocking obligation on this surface** must update this clause's list
   **in the same logical change** (the same amendment act, reviewed and adopted
   together). An amendment that creates a checkable obligation and does not route
   it here is an incomplete amendment; the review that accepts it must treat the
   omission as a defect of the amendment, not a later housekeeping task. The same
   rule binds the craft-and-care release checklist that consumes this list.
2. **The mechanical validation contract.** The release process must include a
   **registry-completeness check**: a mechanical or checklist pass that walks
   every clause of this RFC (and every consumed cross-RFC gate this list cites)
   whose text names a release-blocking or fixture-tested obligation, and verifies
   each is either present in this list or explicitly recorded as out-of-scope with
   a reason. The check's form (script, structured checklist, review template) is
   an implementation-slice choice; what binds is that it exists, runs at each
   release, and its result is recorded. A release that cannot show the
   completeness-check result fails this gate exactly as it would fail a missing
   fixture.

[Inferred — the maintenance contract; Observed — the two demonstrated omissions
that motivate it. Note that this clause's list spans the whole package: an
obligation created in `semantic-geography.md` or `visual-grammar-and-lenses.md`
is routed **here**, and the same-logical-change invariant binds across module
boundaries exactly as it did across sections.]

**RFC9-48.** **Non-visual parity.** Every distinction the scene renders has a
non-visual path: full keyboard navigation of every action — traverse, select,
zoom, lens, analytical plane, scenario, drawer, filter — without pointer or
camera; the tabular equivalent as the screen-reader surface; textual epistemic
labels for every state (RFC9-27's two-carrier rule); reduced-motion honored with
no loss of meaning; text contrast maintained in every profile. Accessibility here
is a truth requirement: a reader who cannot perceive "Unknown" is being shown
comprehensible fiction.

---

## 2. Performance as a contract obligation

**RFC9-49.** Responsiveness budgets are declared, per scene class, in the
surface's spec (values are craft material; the obligation to declare is not), and
**the budget values must exist before V0 ships** — the same same-increment
obligation RFC9-35 binds for lenses, for the same reason: an undeclared budget is
an obligation that never becomes checkable. When a budget cannot be met, the
surface degrades **only by narrowing an explicitly declared scope, rendered as
narrowed** — in the 3D scene and the non-3D equivalent identically, so the
equivalence gate is evaluated over the same narrowed scope. **The narrowing is a
declared filter under RFC6-16 and travels in the answer's envelope**, recorded
with the answer: the narrowing scopes available to a scene class are declared in
the surface's spec beside that class's budget, the surface may select only among
those declared scopes, and the selected scope is named in the answer it produces.
It is never a render-time scope improvised from device capability. Were it
render-time, two readers — or the owner and an agent consuming the same selection
under RFC6-13's one-truth-two-consumers rule — would receive different entity
sets for the same URL at the same evaluation, each honestly labelled, with no
clause naming the divergence (RFC6-3 covers evaluation skew, not scope skew).
Silent decimation, silent entity dropping, and stripping epistemic carriers for
speed are forbidden; the permitted currency is VIS-1 rank 4, never rank 1
[Observed: vision.md, Performance]. **Truth is never purchased with frame rate.**

---

## 3. Motion (SDR-26)

**RFC9-50.** **No ambient motion at V0.** Motion is reserved for labelled
transitions, explicitly selected flows, and camera movement [Observed: SDR-26].
Any later motion (Factory, selected replay) obeys RFC9-37: capture window
visible, stops-and-marks on staleness, never synthesized, never the sole carrier
of any state, reduced-motion honored.

**RFC9-51.** Illumination and highlight are interaction state — selection, search
hits, cross-surface highlight (RFC6-3) — personal, never truth-bearing, and
legended as such. Binding light to a metric would imply liveness the evidence may
not support. [Inferred]

---

## 4. Authority boundary at the OpenSpec seam (binding phase rule)

**RFC9-52 — This contract schedules nothing.** This RFC fixes the semantics of
the map surface; it is **not a specification of record from which implementation
work may be scheduled**. No implementation work for **user-observable Orrery
behavior** may be scheduled solely from this RFC: before implementation, every
observable consequence of RFC9-1…RFC9-51 must either **map to an approved
OpenSpec requirement or scenario** in the governance root's `openspec/**` plane,
or carry an **explicit, reviewed N/A judgment** recording why that consequence
needs no requirement. The surface-specification phase must produce, as a
deliverable, a **clause-to-requirement coverage matrix** for this RFC — every
clause mapped to requirement identities or to its reviewed N/A — and that matrix
is review material, never authority. This clause creates no OpenSpec content now
(none may exist during bootstrap); it binds the phase boundary so RFC prose is
never quietly treated as an implementable behavioral spec.

*(RFC9-52 binds the whole package, not this module alone: "RFC9-1…RFC9-51" spans
all three modules, and the coverage matrix is produced for RFC 0009 entire. The
clause is shape-parallel with RFC6-28, RFC7-38 and RFC8-32.)*

---

## 5. Violation cases (module-owned)

11. *(RFC9-46/49)* Scene and table disagree on a freshness state or count; the 3D
    view silently narrows scope while the table stays full-scope.

*(Cases 1–5 and 3a belong to `semantic-geography.md`; cases 6–10 to
`visual-grammar-and-lenses.md`.)*

---

## 6. Integration (module-scoped)

**RFC 0002:** the recorded base layout (RFC2-6); the RFC2-18 chain state and
RFC2-17's word reservation. **RFC 0006:** equivalence (RFC6-22/23); filters
disclosed as filters (RFC6-16); cross-surface highlight and evaluation skew
(RFC6-3); one truth, two consumers (RFC6-13); sibling surface states (RFC6-14);
scenario context (RFC6-24). **RFC 0008:** the two work-state fields
(RFC8-12/8-28/8-29). **Provides to craft-and-care:** the release-gate list
(RFC9-47) and its self-maintenance contract (RFC9-47(a)) — this is the artifact
craft-and-care's release checklist consumes, and RFC9-47(a) part 1 binds that
checklist too. **Provides to the first map-surface spec:** every declared-value
slot this contract deliberately leaves open (budget values, treatment values,
band counts, analytical-plane catalog).

**Upstream defect reported from this module's clauses is resolved**: RFC6-22's
equivalence enumeration formerly omitted sibling surface states and scenario
context (defect 2); RFC 0006 folded both in on 2026-08-01. Trail: history file,
§5.

---

## 7. Deliberately deferred (module-scoped)

Performance budget *values* and the release-gate operating procedure →
craft-and-care / quality policy (the obligation to declare budgets, and to
declare them before V0 ships, binds here regardless). Rendering technology →
post-acceptance material; none may weaken a clause here (RFC9-2). Live fleet
streaming → deferred mandate; certificate rendering → post-V1, future-tagged.

---

## 8. Owner questions (module-owned)

Numbering is the stable package numbering; answered items keep a stub here so
numbers never shift. **None of this module's questions is open.**

- **q10** — does the return-to-home bound stay "one action" (RFC9-10(c);
  SDR-21)? **Answered — owner decision B21**, granting the relaxation. The
  surviving contract text lives at RFC9-10(c) in `semantic-geography.md`; the
  recorded cost — that no release gate can count actions any more — is why no
  such check appears in RFC9-47's list. See
  `../../history/RFC-0009-history.md` §8.

*(One package-level open follow-on — the RFC9-9 legend/edge-channel pass flagged
by the rev10 RFC-0001 compaction — is owned by `semantic-geography.md` §10.)*

---

*End of module 3. Clauses RFC9-46 … RFC9-52, plus lettered sub-clause
RFC9-47(a); no gaps, no retired or merged numbers in this range. This is the end
of the RFC 0009 clause range: RFC9-52 is the highest number in use, and a new
clause anywhere in the package takes the next free integer (53 onward).
Amend in place, add lettered sub-clauses, never renumber.*
