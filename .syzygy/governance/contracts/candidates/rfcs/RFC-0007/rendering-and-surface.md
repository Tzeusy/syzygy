---
id: RFC-0007
title: Polaris (Intent Surface) — rendering, the authority boundary, comprehension acceptance, machine parity and navigation
status_source: owner-act-record
module: rendering-and-surface
clauses: RFC7-26..RFC7-38 (no sub-clauses, no gaps, no retirements, no merges)
governs: [reading-mode, proposed-scenario-rendering, curated-diagram, authority-boundary, comprehension-test, walkthrough-record, machine-parity, non-visual-recoverability, portfolio-narrative, subproject-navigation]
applies_to: [polaris]
depends_on: [RFC-0001, RFC-0003, RFC-0006, RFC-0009]
tags: [presentation, proposed-scenario, comprehension-test, verdict-unlawful, machine-parity, non-visual, reachability, portfolio, phase-boundary]
---

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until the
independent A1 correlation mechanism exists, and as a Syzygy-verified effective
act only after correlation (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 2 of 2 of the RFC 0007 contract package. Index, clause map,
lookup rule, package-level summary, doctrine grounding, integration,
alternatives and deferrals: `README.md`. Rationale, amendment history,
alternatives, and answered §8 questions: `../../history/RFC-0007-history.md`.

**Serves:** VIS-1, VIS-2, VIS-3, VIS-6, VIS-7; SEC-3, SEC-5. Implements **owner
rulings** SDR-14, SDR-17; honors SDR-27 for non-visual parity and
SDR-28/29/30 for portfolio rendering; resolves the Polaris portion of SDR §5
question 10.

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **what the surface must show, prove, and never blur**: the two
reading modes and how proposed material renders (RFC7-26…28), the authority
boundary between what Polaris owns and what it merely composes (RFC7-29), the
cold-open comprehension walkthrough that is this surface's acceptance test and
its verdict discipline (RFC7-30…32), the machine-parity and non-visual
obligations every distinction must satisfy (RFC7-33/34), multi-project and
subproject navigation including the portfolio narrative (RFC7-35…37), and the
binding phase rule at the OpenSpec seam (RFC7-38). Read it to answer: *what
must a reader — human, agent, or one who cannot see — be able to get out of
this surface, and what may the surface never let them conclude?*

Three rules bind hardest. **Proposed is never adopted**: competing futures are
selectable one at a time and never merged, and prose describing a proposal in
the register of adopted intent violates RFC7-2 regardless of visual marking
(RFC7-26/27). **A distinction only pixels carry does not exist**: everything
this package draws is a machine-readable attribute and is recoverable without
colour, position, or layout — and the *paths* between units must be operable
without a pointing device, not only the units (RFC7-33/34). **A defective
verdict buys nothing**: an unverifiable comprehension-test judgment renders the
test Unknown-never-met, exactly as an absent record would (RFC7-31).

What this module receives from module 1 (`narrative-contract.md`): the
narrative-model units RFC7-33's `non-citable` attribute must travel on
(RFC7-5); the primary narrative RFC7-30 enters (RFC7-6); the two invariants
every clause here presupposes (RFC7-2, RFC7-3); and RFC7-25's review and record
discipline, which RFC7-31 and RFC7-32 extend to walkthrough verdicts.

---

## 3. The contract

Clauses are numbered `RFC7-n` across the whole package. Amend in place; retire
rather than renumber.

### 3.8 Proposed-state presentation

**RFC7-26 — Two reading modes, named in the kernel's vocabulary.** The default
reading mode **is RFC6-24's `Base` context** — the base graph at the selected
evaluation — and is named that. Base includes the **observed** plane, not only
adopted desired state: the reality band (RFC7-17) renders in full in default
reading, and an implementation that builds the default as a filter over
adopted desired state has built the wrong mode. ("As-adopted" may appear as
descriptive prose about the desired-state portion of a Base read; it is **not**
a mode name — Polaris coins no surface-local synonym for a kernel concept.)
The second mode is a **proposed-scenario reading**:
RFC6-24's `Proposed` context — (base evaluation, selected proposal set) —
travelling with every selection, URL, and query (RFC6-25). Proposed and
unadopted material is unmistakably distinct — visually and machine-readably —
everywhere, has no status authority, turns nothing green, anchors nothing
(RFC1-22).

**RFC7-27 — No fictitious consensus.** Competing proposals never collapse into
one merged future: the kernel refuses to union proposals in one exclusivity
group or of undeclared compatibility (RFC1-27; RFC6-24
`incompatible-scenario`); the honest render is *N candidate futures*,
selectable one at a time. Narrative prose describing a proposal in the register
of adopted intent — "the system does X" for an unadopted X — is an RFC7-2
violation regardless of visual marking.

**RFC7-28 — Curated diagrams.** A hand-composed diagram is narrative content
under every rule in this package: each named element carries an anchor or a
non-normative/proposed marking; speculated structure never looks like existing
structure [Observed: trust-and-evidence.md]; every encoding means what its
legend says (VIS-7); a text equivalent exists (RFC7-34). Curated diagrams claim
no reproducibility-from-snapshot and must not imitate the computed map;
embedded computed visuals inherit the map surface's obligations;
curated/computed provenance is a machine-readable attribute on every visual.
Live Orrery transclusion is deferred (`README.md` §7).

### 3.9 Authoritative versus presentation content — the boundary

**RFC7-29 — The boundary table.**

| Content | Polaris relation | Authority |
|---|---|---|
| Doctrine rules, non-goals | Renders by stable identifier, verbatim at leaf | `.syzygy/governance/doctrine/` |
| Accepted contracts (RFCs) | Renders; never confers acceptance | `.syzygy/governance/contracts/` |
| Requirements, scenarios | Renders verbatim (RFC7-14) | `openspec/**` artifact contract |
| Capabilities, topology, regions, mappings | Renders declarations; drafted = unadopted | Governance declarations (RFC3-17) |
| Decisions, dismissals, consents | Renders, reason/expiry visible | `.syzygy/governance/decisions/` |
| Status, evidence, freshness, challenges | Renders via the single drawer (RFC7-18) | Kernel, at identified evaluations |
| Work items, runs, queue state | Renders links and read-only state | Scheduler via typed adapter; Trajectory |
| **Narrative, sections, claim blocks, reading order, citation graph, curated diagrams, draft states** | **Owns** (governed presentation artifact, non-authoritative) | `.syzygy/intent/**` |
| Personal view state | Neither — outside the model | `.syzygy/local/`, VIS-6, exception (a) |
| Portfolio narrative | Renders as owner-workspace content (RFC7-36) | Workspace manifest (RFC3-10/11); never project truth |

Nothing in the "owns" row sources any project fact (RFC7-2/3); every other row
is composition over an authority Polaris cannot amend from within — amendments
run through RFC7-23's acts and gates.

### 3.10 Fresh-reader acceptance — the comprehension test

**RFC7-30 — The criterion.** This surface's acceptance test is the **cold-open
comprehension walkthrough**: a fresh reader (human or agent, no authoring
context — VIS-3's independence standard), entering at the primary narrative
(RFC7-6) with navigation confined to Polaris, states in their own words: why
the project exists; what it promises; what it refuses to be (naming at least
one non-goal and reaching its rule text); what its major capabilities are and
how they fit; **where exactness lives** — reaching a verbatim requirement leaf;
and **one thing the project does not currently know about itself** — an Unknown
region and how the surface showed it. The last prompt is load-bearing: a
surface passable only by a uniformly confident read has rendered
comprehensible fiction (VIS-1). A second phase checks answers against the
owned artifacts; divergences are recorded as findings.

**At least one run per release milestone is performed non-visually or
keyboard-only**, exercising RFC7-34's reachability limb: the walkthrough must
test the *paths* between units, not only the units — otherwise an
implementation satisfying RFC7-33/34 on every unit, with every path between
units pointer-only, passes every time. The non-visual run's record lives where
every other run's record lives (RFC7-31).

**RFC7-31 — Verdict discipline.** The verdict is the owner's recorded human
judgment — never rendered Observed, never a score [Observed: vision.md,
Success]. Two floors are not judgment calls: a **dangling internal link on the
walkthrough path** fails (trust floor, release-blocking); a confident wrong
answer **attributable to what the surface rendered** fails. A reader's own
misreading of an honest page, and a thin result on an undeclared project, are
judgment territory — a predominantly-Unknown narrative over an undeclared
project is **correct output** [Observed: v1.md], never failed for honest
reflection.

**Two artifacts, two homes.** Each run mints a **walkthrough execution
record** — `kernel-recorded`, in `.syzygy/governance/records/` (RFC3-15) —
naming the surface version, the evaluation identity behind any rendered
status, and whether the run was non-visual/keyboard-only (RFC7-30); absent its
record, the test renders Unknown, never met. The **judgment** — verdict,
rationale, judging party — is an owner adjudication recorded in
**`.syzygy/governance/decisions/`**, for RFC7-25's reason: it is a recorded
human judgment, not narrative content, and a decision is a warrant, never
evidence. Storing either under `.syzygy/intent/**` would let deletion of that
tree flip a v1.md-tracked success test from a recorded verdict to Unknown —
exactly what RFC7-3's deletion invariant forbids. The judgment is honored
**under RFC3-16(a)**: the home establishes durability, never authorship, and an
owner judgment a fleet worker could commit is not an owner judgment. A
judgment whose owner-act provenance does not verify — like one unattributed or
unreasoned — is recorded as **verdict-unlawful** and leaves the test rendering
**Unknown, never met**, the identical outcome assigned to an absent record, so
an unverifiable verdict buys nothing a missing one would not. *(RFC9-45 states
the same protocol in the same terms: defective verdict → recorded
`verdict-unlawful`, test renders Unknown-never-met, gate fail-closed; the
shared release-policy leg is stated at RFC9-45.)*

**RFC7-32 — When it runs (SDR-14).** At **material narrative changes and
release milestones** — not every prose edit; recorded per RFC7-25, in the
record home RFC7-25 and RFC7-31 name, with at least one non-visual/
keyboard-only run per release milestone (RFC7-30). It is the intent-surface
sibling of v1.md's spatial comprehension test: same shape, shareable protocol,
never collapsed into one test.

### 3.11 Machine parity and non-visual recoverability

**RFC7-33 — Every distinction, machine-readable.** Every distinction this
package draws — **`non-citable` / `presentation-artifact`** (below),
claim-block kind (anchored / non-normative / labeled), the narrative
claim-block **type name** (below), band membership and its authority class,
curated-versus-computed provenance, adopted versus unadopted, editorial-draft
state, proposal-context membership, review state, RFC7-11(a)'s
**target-changed** state, label + tier + reason + freshness — is carried as a
**machine-readable attribute on the rendered unit**, served identically
through the machine-queryable endpoints (RFC6-13/14) and preserved in
plain-text or exported renderings [Observed: agents are a first-class consumer
from day one (vision.md); endpoints are V0-mandatory (v1.md)]. A distinction
available only to pixels does not survive an endpoint response, a copy-paste
into an agent prompt, or a reader who cannot see it.

**Non-citability travels, on every rendering.** Every narrative-model unit
(RFC7-5) carries the **`non-citable` / `presentation-artifact`** attribute,
required on **every** exported, embedded, or plain-text rendering — not only
on the interactive surface. RFC7-3 binds Syzygy; the external agent consuming
RFC6-13's endpoints is a party RFC7-3 cannot bind, and what it receives
carries epistemic labels, resolvable anchors, and evaluation stamps — every
signal that ordinarily marks trustworthy kernel output. It can tell draft from
curated and not presentation from authority, and the RFC7-3 violation it then
commits (the package-spanning violation case in `README.md` §4) is
unattributable to any bound party. The catch-all opener above is not sufficient
cover: [Inferred] enumerations of this shape are implemented as literal field
lists, so the one field whose omission is unrecoverable at the consumer must be
named.

**Narrative claim blocks carry a distinguishing type name** in the machine
envelope, separate from the kernel's Claim entity (RFC1-5; RFC1-24 routes all
status through it): an agent querying "claims" about a Capability must never
receive kernel claim instances and narrative claim blocks under one
undifferentiated name. The dual usage in prose has doctrinal cover [Observed:
trust-and-evidence.md, "Status claims vs narrative claims"] and needs no prose
rename — the hazard exists only at this boundary.

**RFC7-34 — Non-visual recoverability.** Every such distinction is recoverable
**without colour, position, or layout** — by label, text, or structure; visual
encodings are legended and mean exactly what the legend says (VIS-7); every
curated diagram has a text equivalent carrying the same anchored elements and
markings. This is the intent-surface counterpart of the map's co-equal non-3D
obligation (SDR-27): an epistemic state a reader cannot perceive is
comprehensible fiction for that reader.

**Reachability — the second limb.** Recoverability governs *encoding*;
**operability** is a separate obligation and both bind. Every traversal of the
disclosure path must be operable **without a pointing device**: RFC7-13's
altitudes, a claim block's anchor expansion (including RFC7-11 and RFC7-11(a)
states), and the RFC6-18 drawer handoff. It is the counterpart of v1.md's
mandate that keyboard/non-3D navigation is **always available** on the map,
of which SDR-27 supplies only the semantic-equivalence half. A surface whose
every unit is recoverable and whose paths between units are pointer-only has
satisfied neither limb; RFC7-30's non-visual run is the evidence that it does.

### 3.12 Project and subproject navigation

**RFC7-35 — Multi-project entry.** The multi-project entry renders from the
**workspace manifest** — membership, grouping, ordering, saved views are
workspace concerns (RFC3-11) — while every project-internal fact shown derives
from that project's own plane (SDR-28; RFC3-12). Deleting the workspace
manifest changes what is arranged, never what is true. Unresolvable entries
render Unknown with their reason, never dropped (RFC3-13).

**RFC7-36 — Portfolio narrative is owner-local, never project truth.** The
owner-specific portfolio narrative SDR-29 permits lives in the workspace
manifest's scope — VIS-6, exception (a) territory (RFC3-10) — and renders
**visibly as owner-workspace content**: it is no project's narrative, holds no
claim block over any project's facts beyond references resolving into the
projects' own planes, is never a citation target (RFC7-3 in full force), and
never affects any project's truth, work, or status. There is no portfolio
governance root and this RFC creates none.

**Carry-over out of `.syzygy/intent/**`** — stated, not inferred, because the
portfolio narrative sits outside the residence rule (RFC7-5). **These follow
it:** RFC7-2 (every load-bearing claim anchored, marked non-normative, or
epistemically labeled — including the authoring-act rule); RFC7-7 (versioned,
attributed, revertible, never silently overwritten); RFC7-11 **and
RFC7-11(a)** (broken and target-changed anchors render, never silently
current); RFC7-33/34 (machine parity, the `non-citable` /
`presentation-artifact` attribute, non-visual recoverability and
reachability). **These do not follow it, and are already forbidden by those
four:** claim blocks over any project's facts, and citability in any form.

**It may not assert any governed project's status.** Those four forbid a
reader being unable to *tell* portfolio narrative from project truth, but not
the assertion itself; this clause forbids it. Portfolio prose may not assert
that a governed project is converged, aligned, verified, healthy, or any other
status — visible marking does not license it, because a narrative sentence
doing a badge's work **is judged as a badge** [Observed:
trust-and-evidence.md; RFC1-19]. Cross-project status renders only as each
project's own kernel-computed state, read from that project's plane (RFC7-35,
SDR-28).

[**OQ-010 interaction.**] Portfolio authority remains an open owner question:
where a genuine cross-project *fact* or Project-relationship entity would live
is unsettled. This clause binds the portfolio narrative's **discipline** and
settles nothing about where cross-project truth lives; it is compatible with
every option OQ-010 leaves open.

**RFC7-37 — Subprojects render as declared relations.** Related-project and
parent/child navigation renders the projects' own declared relations with
RFC3-14's asymmetric semantics: one-sided declarations render unconfirmed;
confirmed hierarchies require compatible counterpart declarations; the
narrative never draws a confirmed edge the declarations do not support. A
parent's view of a child carries the child's epistemic labels through
unchanged (RFC3-32); aggregating a child's Unknowns into anything green is the
VIS-1 violation. **Any roll-up over a child's facts additionally discloses
RFC6-17's full composition** — the RFC6-22 equivalence tuple, per-label,
per-tier, per-Unknown-reason and per-freshness-state counts and sibling
surface states, expandable to members — **cited, never restated here**,
because a paraphrase is how a roll-up rule drifts from the aggregation
contract it instantiates. The narrow reading alone (labels carried through, no
Unknown folded into green) is insufficient; the worked counter-example is in
history.

### 3.13 Authority boundary at the OpenSpec seam (binding phase rule)

**RFC7-38 — This contract schedules nothing.** This RFC fixes the semantics
of the intent surface; it is **not a specification of record from which
implementation work may be scheduled**. No implementation work for
**user-observable Polaris behavior** may be scheduled solely from this RFC:
before implementation, every observable consequence of RFC7-1…RFC7-37 must
either **map to an approved OpenSpec requirement or scenario** in the
governance root's `openspec/**` plane, or carry an **explicit, reviewed N/A
judgment** recording why that consequence needs no requirement. The surface-
specification phase must produce, as a deliverable, a **clause-to-
requirement coverage matrix** for this RFC — every clause mapped to
requirement identities or to its reviewed N/A — and that matrix is review
material, never authority. This clause creates no OpenSpec content now (none
may exist during bootstrap); it binds the phase boundary so RFC prose is
never quietly treated as an implementable behavioral spec.

*(RFC7-38 binds the whole package: RFC7-1…RFC7-37 spans both modules, and the
coverage matrix it requires is a package-level deliverable, not a per-module
one.)*

---

## 4. Violation cases

*Package numbering; cases are distributed across modules, never renumbered.
Cases 1–7, 12 and 14 are in `narrative-contract.md`; cases 10, 13 and 15 span
both modules and are held in `README.md` §4.*

8. *(RFC7-26/27)* Two exclusive proposals rendered as one merged future; or
   proposed and adopted architecture prose indistinguishable in an endpoint
   response.
9. *(RFC7-31)* The comprehension test failed because an undeclared project's
   narrative was honestly thin; or passed with a dangling link on the
   walkthrough path.
11. *(RFC7-36)* The portfolio narrative asserts "project B is converged" as
    workspace prose a reader cannot tell from project truth — or asserts it
    while *perfectly* marked as workspace prose, also forbidden.

---

## 5. Integration (module-local)

**Relies on RFC 0001:** the Claim entity (RFC1-5) that RFC7-33's type name must
stay distinct from, and the status routing through it (RFC1-24); the badge rule
(RFC1-19) behind RFC7-36's status prohibition; the plane rule (RFC1-22) that
stops proposed material anchoring anything; Proposal exclusivity (RFC1-27)
behind RFC7-27. **On RFC 0003:** workspace-manifest boundaries (RFC3-10…14) —
scope, membership, project-plane sourcing, unresolvable entries, and RFC3-14's
asymmetric relation semantics; governance declarations (RFC3-17) in the
boundary table; the `kernel-recorded` record home (RFC3-15); the child-label
pass-through rule (RFC3-32); and the **owner-act provenance predicate
(RFC3-16(a))**, which gates RFC7-31's verdict exactly as it gates RFC7-25's.
**On RFC 0006:** the machine-queryable endpoints and label parity
(RFC6-13/14) that carry RFC7-33's attributes; the aggregation contract
(RFC6-17) and equivalence tuple (RFC6-22) RFC7-37 cites without restating; the
drawer handoff (RFC6-18) in RFC7-34's reachability limb; and scenario contexts
and their URL travel (RFC6-24/25) behind RFC7-26.

**Provides to RFC 0009 (Orrery):** the curated-versus-computed provenance
attribute (RFC7-28) and the transclusion question (`README.md` §7). RFC7-31 and
**RFC9-45** state one verdict protocol in the same terms — defective verdict →
recorded `verdict-unlawful`, test renders Unknown-never-met, gate fail-closed —
with the shared release-policy leg stated at RFC9-45, never duplicated here.

**Receives from module 1 (`narrative-contract.md`):** the narrative-model units
RFC7-33's attribute travels on (RFC7-5); the primary narrative RFC7-30 enters
(RFC7-6); the two invariants every clause here presupposes (RFC7-2, RFC7-3);
RFC7-17's bands, whose authority classes RFC7-26 and RFC7-33 both depend on;
and RFC7-25's review and record discipline, extended here to walkthrough
verdicts.

---

*End of module 2 of 2. Clauses RFC7-26 … RFC7-38, no lettered sub-clauses.
Contiguous, nothing retired, merged, or renumbered. This module carries no §8
question — both open package questions own clauses in module 1. Amend in place,
add lettered sub-clauses, never renumber.*
