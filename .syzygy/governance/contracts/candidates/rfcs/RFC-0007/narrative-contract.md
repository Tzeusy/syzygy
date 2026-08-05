---
id: RFC-0007
title: Polaris (Intent Surface) — the curated narrative contract: model, anchors, disclosure, drafts, authoring
status_source: owner-act-record
module: narrative-contract
clauses: RFC7-1..RFC7-25 (sub-clauses RFC7-2(a)-(c), RFC7-9(a)-(c), RFC7-11(a); no gaps, no retirements, no merges)
governs: [intent, narrative, section, claim-block, source-anchor, reading-order, citation-graph, editorial-draft, authoring-act, materiality]
applies_to: [polaris]
depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005, RFC-0006]
provides_to: [RFC-0008]
tags: [presentation, non-authoritative, claim-block, source-anchor, target-state, progressive-disclosure, editorial-draft, materiality]
---

**Status:** Proposed foundational contract (self-declaration at authoring
time). Effective status is established solely by an owner-act record binding
this file's exact content digest — as an owner-adopted bootstrap act until the
independent A1 correlation mechanism exists, and as a Syzygy-verified effective
act only after correlation (RFC3-16). Absent such a record, this contract binds
nothing.

**Package:** module 1 of 2 of the RFC 0007 contract package. Index, clause map,
lookup rule, package-level summary, doctrine grounding, integration,
alternatives and deferrals: `README.md`. Rationale, amendment history,
alternatives, and answered §8 questions: `../../history/RFC-0007-history.md`.

**Serves:** VIS-1, VIS-3, VIS-4, VIS-6; SEC-2, SEC-3, SEC-4. Implements **owner
rulings** SDR-13, SDR-14, SDR-15, SDR-16, SDR-17, SDR-18.

---

## 0. Module scope and reader map (non-normative)

*If this section and a clause disagree, the clause wins.*

This module owns **what curated narrative is, what binds a claim to the
artifact that owns the fact, and what any act producing narrative must
satisfy**: Polaris's identity and its two load-bearing invariants (RFC7-1…4),
the narrative entity model and its residence (RFC7-5…8), claim blocks and
source anchors including the target-state component and both drift states
(RFC7-9…12), progressive disclosure and the verbatim leaf (RFC7-13…16),
capability deep-dive bands (RFC7-17…19), generated editorial drafts and their
human adoption gate (RFC7-20…22), and the authoring acts, gates, and
materiality review (RFC7-23…25). Read it to answer: *may this sentence exist in
curated narrative, and what act does it take to put it there?*

Two invariants bind hardest and reach every other clause in the package: every
load-bearing narrative claim is **anchored, marked non-normative, or
epistemically labelled** — there is no fourth kind (RFC7-2); and **nothing
anywhere in Syzygy may cite a Polaris rendering as authority**, so deleting
`.syzygy/intent/**` changes no truth (RFC7-3). A third protection closes time
rather than citation: an anchor records the **state of its target at
authorship**, so a cited rule that moved renders as drifted, never as current
(RFC7-10, RFC7-11(a)).

What this module hands to module 2: every distinction drawn here must be
machine-readable and non-visually recoverable (RFC7-33/34); the primary
narrative this module requires is the entry point of the comprehension test
(RFC7-30); the review records and failed-review renderings RFC7-25 defines
share their home and their RFC3-16(a) provenance gate with RFC7-31's verdicts.

---

## 3. The contract

Clauses are numbered `RFC7-n` across the whole package. Amend in place; retire
rather than renumber.

### 3.1 Identity and the two invariants

**RFC7-1 — What Polaris is.** A **projection surface over the one shared
kernel** whose product is an argued, progressively disclosed account of the
project's intent: thesis → promises and refusals → architecture →
capabilities → exact requirements → evidence and work doorways. Never
independently authoritative [Observed: architecture.md]; never satisfied by
the anti-thesis forms (SDR §2).

**RFC7-2 — Composition, never custody.** Every **load-bearing narrative
claim** — a span of narrative content asserting a fact about the project
(rules, behavior, structure, status, history, decisions) — is exactly one of:
**(a) anchored** — resolvable through its claim block's source anchors
(RFC7-9, RFC7-10) to the one artifact that owns the fact; **(b) explicitly
non-normative** — framing, motivation, analogy, transition, or reader guidance,
machine-marked as carrying no normative force; or **(c) epistemically
labeled** — Observed with its evidence link, Inferred with its inference
provenance, or Unknown, per trust-and-evidence.md. There is no fourth kind: an
unanchored, unlabeled, unmarked project-fact claim in curated narrative is a
**defect**, not a style choice. Granularity is the claim block (SDR-16) — the
obligation binds claims; the mechanism binds blocks.

**The check binds the authoring act, not one path through it**: it is a
property of **any act producing curated narrative** — a human typing prose,
an agent repairing prose under VIS-3's authorship allowance, or a draft
adoption — assessed per claim at the act. No authoring path reaches curated
narrative without crossing it; RFC7-21 is one crossing point, not the only
one (RFC7-23, RFC7-25).

**RFC7-3 — Nothing cites the rendering.** No claim, gap, mapping, evidence
link, work warrant, source anchor, or citation anywhere in Syzygy may resolve
to a Polaris narrative, section, claim block, rendering, or editorial draft
as its authority: a narrative artifact is never an admissible evidence
artifact, never a snapshot input to a status claim, never a citation target.
Deleting everything under `.syzygy/intent/**` changes **no truth, status,
work, consent, or normative fact** — it loses governed presentation work
(authored, not cache; RFC7-8), never the normative corpus. [Inferred: VIS-6
plus "surfaces are never independently authoritative," made mechanically
checkable — a second source of doctrine cannot form if nothing may cite it.]

**RFC7-4 — Non-authority is total.** RFC7-2/3 hold for every narrative state
— curated, draft, adopted-after-review, historical. Review or owner adoption
as presentation confers **no** normative force.

### 3.2 The curated narrative model

**RFC7-5 — Entities.** All resident in `.syzygy/intent/**` (RFC3-18), all in
RFC 0001's **presentation profile** (RFC1-7), never V0-core:

| Entity | Definition | Owns |
|---|---|---|
| **Narrative** | The composed account for one project: a reading order over Sections with a thesis | Its composition; no project fact |
| **Section** | A named unit with a purpose and a place in the reading order | Prose and block membership |
| **Claim block** | A contiguous span carrying a source-anchor set, a non-normative marking, and/or epistemic labels (RFC7-2) | The binding, never the fact |
| **Reading order** | The curated sequence and grouping over Sections | Order only |
| **Citation graph** | The queryable set of (claim block → source anchor) bindings | Derived from blocks; rebuildable |
| **Curated diagram** | A hand-composed visual with anchored or marked elements (RFC7-28) | The composition |
| **Editorial draft** | Generated candidate content in the SDR-15 state (RFC7-20) | Nothing; non-citable by construction |

Identifiers are opaque and label-independent (RFC1-10 discipline), minted by
the recorded authoring act. Personal view state (bookmarks, density toggles,
reading position) is **not** in this model: it lives in `.syzygy/local/` under
VIS-6, exception (a) — never truth-bearing, never a snapshot input (RFC3-21).

**The presentation profile is required for any governed project Polaris
renders, and Polaris drafts one rather than presuming it** *(owner decision
A4)*. On first render of a project that has not loaded the profile, Polaris
**drafts a default profile for owner sign-off** and renders it
`unadopted-draft` until signed — the RFC2-24 reason #1 route, "first-pass
drafting for owner sign-off" — and every narrative element above an unsigned
profile renders unadopted with it. A project may decline the profile
permanently; Polaris then renders the reduced form and says so. Barred is the
third path: behaving *as if* a profile were present because one is required.
Nothing is presumed, so RFC1-7's **"never presumed present"** holds.
[Inferred — the bootstrap route is the owner's decision; its grounding in
reason #1, and why a profile-less Polaris is the charter-excluded
"disconnected specification browser", are in history.]

**RFC7-6 — One primary narrative.** A governed project has at most one
**primary narrative** — the front door the comprehension test (RFC7-30)
enters. Additional named narratives are permitted under the same class and
rules; none outranks another, because none is authoritative at all.

**Thin, never absent.** On an undeclared or thin project the primary narrative
may be **thin, or Syzygy-drafted and unadopted (RFC7-20), but never absent**: a
predominantly-Unknown catalog under an honestly thin narrative is correct
output (RFC7-15, RFC7-31) on v1.md's proving ground — "real, messy, already
running, mostly undeclared" [Observed: v1.md]. Absence is not thinness; it is
a missing front door, and it fails RFC7-30 rather than passing it trivially.

**RFC7-7 — The governed-presentation-artifact class (SDR-13).** Every
narrative-model artifact is **versioned, attributed, revertible,
human-readable**: every change is a Syzygy-attributed, atomic, individually
revertable write (SEC-4, first clause — unqualified, binding prose edits
exactly as structure edits); authorship and review state are machine-readable
facts (RFC3-16 discipline); Syzygy never silently overwrites narrative content
it did not author (SEC-4's conflict-surfacing rule). "Governed" names the
change discipline, never the content's standing.

**RFC7-8 — Neither cache nor governance authority.** The narrative is authored
content in the governed plane: it stays with the repository at offboarding
(RFC3-18), is not rebuildable and must not live in `.syzygy/cache/` (RFC3-20),
and is not a `governance/` artifact and binds nothing. The one thing it owns —
its composition — is the fact it is the owning artifact *of*; VIS-6 is
satisfied without an exception.

### 3.3 Claim blocks and source anchors (SDR-16)

**RFC7-9 — Granularity, covering, minimality, bounding.** The citation unit is
the **claim block or section source anchor**, never a per-sentence badge
(SDR-16). Every load-bearing claim sits inside a block whose anchor set
**covers** it; an anchor targets exactly one owned artifact. Three properties
bind, and are not stylistic:

**(a) Covers.** An anchor set covers a load-bearing claim when the claim is
derivable from the anchored targets **and a reader can determine which anchor
or anchors support it**. Derivability alone is not covering.

**(b) Minimality.** An anchor set carries **no anchor that no claim in the
block relies on**. A surplus anchor is a **defect, not a courtesy**: it
dilutes attribution and is indistinguishable, to a reader, from support.

**(c) Bounding.** A block **must** be bounded so claim-to-anchor attribution
is recoverable. A block in which it is not — the twenty-anchor set at section
granularity, where every claim is derivable from *something* and no claim's
support can be named — is **non-conformant**, not merely large: it fails (a)
as well as (c). Splitting is the remedy, and an obligation, not advice.

The ground is doctrine's **admissibility floor** — a challenge is admissible
only if it identifies exactly one claim and states a specific falsifiable
concern [Observed: trust-and-evidence.md; RFC2-12 makes it operational] — not
per-anchor resolvability, which supplies no per-claim attribution: a
challenger facing an unattributable block can name the claim but not the
support they contest.

**RFC7-10 — Anchor form.** A source anchor is machine-readable and typed:
**(target class, target identifier, optional fragment, target state)**, target
class one of: a **kernel entity reference** (selection reference per RFC6-1,
optionally evaluation-qualified); a **doctrine rule or accepted-contract
citation** (stable identifier `VIS-n`/`SEC-n`/RFC clause, rendered per
RFC6-20); an **`openspec/**` anchor** (RFC3-28); a **decision or policy
identifier**; or an **evidence artifact identifier** with integrity digest. No
target class exists for narrative content, renderings, or editorial drafts
(RFC7-3). Anchors embed durable identifiers, never labels, paths, or
coordinates (RFC6-8/9).

**The target-state component** records what the target said when the anchor
was authored: for a declared or normative artifact (doctrine rule, accepted
contract clause, `openspec/**` requirement or scenario, decision, policy,
evidence artifact), its **revision**; for a kernel entity reference, the
**evaluation identity** at which it was read together with the label + tier +
reason the reference then carried (RFC6-14's vocabulary, verbatim). It is
observed at the authoring act and **never rewritten by a later read**. It
creates no new authority and no new epistemic state (`README.md` §5), and
exists to enable RFC7-11(a).

**RFC7-11 — Broken anchors render Unknown, never silent.** When an anchor no
longer resolves — target retired, spec anchor broken by edit, evidence gone —
the block renders the break **on the primary surface**: the anchored claim
degrades to Unknown, the break is named (which anchor, which target; RFC6-5
outcome `unresolvable` or `retired`), and the same state is served to machine
consumers (RFC7-33). The narrative never silently drops an anchor, re-guesses
a target (RFC3-28: degrade, never guess), auto-redirects to a successor
(RFC6-11), or keeps rendering the claim as anchored. A dangling anchor
rendered as a live citation is a trust-floor violation [Observed:
trust-and-evidence.md, floor bullet 2].

**RFC7-11(a) — Resolving anchors whose target changed render as drifted,
never as current.** Where an anchor **still resolves** but its recorded target
state (RFC7-10) differs from the target's current state — a cited rule amended
in place under RFC1-10's same-identifier discipline, a requirement re-worded,
a referenced kernel entity whose label, tier, or reason now differs from the
one recorded at authorship — the block renders **`anchored — target changed
since authorship`** on the primary surface, naming which anchor and what moved
(recorded versus current), with the identical state served to machine
consumers (RFC7-33), and is **marked for RFC7-25 review**. It is never rendered
as silently current, and the drift marker is cleared only by an authoring act
that re-reads the target. A **new evaluation identity alone is not drift**:
for a kernel entity reference, divergence is a change in the rendered label,
tier, or reason, not the passage of evaluations — otherwise every block would
drift on every evaluation and the marker would carry no information.

This is a **Polaris-local rendering obligation over a resolving anchor**, not
an epistemic state: the anchor resolves and the fact is present, so nothing
here mints, implies, or requires an RFC2-24 Unknown reason — that vocabulary
is closed and amended only by RFC 0002. Contrast RFC7-11, where the anchor
stops resolving and the claim genuinely degrades to Unknown. [Inferred: drift
is the third door to the dangerous artifact named in the package's doctrine
grounding (`README.md` §2) — RFC7-3 closes citation, RFC7-20/21 close
generation, and this closes time; reasoning in history.]

**RFC7-12 — Restatement discipline.** An anchored block renders *about* its
target; the target's own text is one step away. For **adjudicative material**
— doctrine rules, non-goals, requirement text — the operative text a reader
relies on is the owned artifact's verbatim text, never a paraphrase in
normative position: a faithful paraphrase that gets quoted becomes the
operative text (the failure mode named in `README.md` §2).

### 3.4 White-paper composition and progressive disclosure

**RFC7-13 — Progressive disclosure: the obligation, and a V0 default path.**
The binding content is the obligation **per altitude**: a narrative discloses
progressively through named altitudes; **each altitude is a self-sufficient,
honest read** — a reader who stops at any altitude has a true, coarser model,
never a false one (VIS-1: simplify presentation, never content); every
narrative descends to a **verbatim specification leaf** (RFC7-14), so
exactness is reachable rather than summarized away. The path bounds
*browsing*; a claim block's anchor is always **one step** from the owned
artifact.

The **V0 default ordering** is thesis/manifesto → architecture story →
capability catalog → capability deep dive → verbatim specification leaf.
Ordering and altitude count are a **V0 default, not a frozen foundational
constraint** *(owner decision B7)*: another named narrative under RFC7-6 may
order its altitudes differently for its audience, bound still by the
per-altitude obligation and the verbatim-leaf terminus. The primary narrative
uses the V0 default unless the owner rules otherwise.

**RFC7-14 — The verbatim leaf.** Requirement and scenario text renders
**verbatim from `openspec/**`** under the artifact contract's own identity
scheme (RFC3-27, RFC4-10) — never paraphrased, reordered, or summarized in
normative position. Polaris may present an ordering and annotate around
requirement text; it may never store a reorganized copy [Observed:
architecture.md, schema ownership]. The same holds for doctrine rule text.

**Under a proposed-scenario reading (RFC7-26) the leaf renders the adopted
text as operative**, with the proposal's delta **adjacent** — visually and
queryably distinct (RFC6-24), never substituted for it, never interleaved so
a reader cannot tell which text is which, never anchorable (RFC1-22). The leaf
is the one place Polaris tells a reader the text before them *is* operative
(RFC7-12); proposed text there would manufacture the most quotable unadopted
text in the system. *(Owner decision B5; the rejected alternatives are in
history.)*

**RFC7-15 — Capability catalog honesty.** The catalog projects **declared**
capability identities (RFC1-14): nothing appears that no declared artifact
asserts; drafted capabilities render unadopted; unmapped code renders Unknown,
never silently inferred into a capability [Observed: v1.md]. A
predominantly-Unknown catalog on an undeclared project is correct output,
rendered as normal — not broken — with RFC2-24 reasons and resolution routes
(`missing-declaration` foremost).

**RFC7-16 — Status in the narrative: minimal by default (SDR-17).** Every
rendered status is kernel-computed at an identified evaluation and carries the
label + tier + reason + freshness vocabulary **verbatim** (RFC6-14); staleness
is visible on the narrative page itself — the narrative is a primary surface
[Observed: trust-and-evidence.md, Staleness]. Default density is minimal: per
capability or major claim, one epistemic state — **its label with its RFC2-25
tier**, and its freshness — with its evaluation identity and a
drawer/Trajectory handoff; no metric walls, trends, counts, or **composite
maturity number**.

**Tier is in the at-rest set for the same reason staleness is**, fixed by this
clause rather than left to disclosure: a `report-fact` Observed claim or an
`asserted-by-worker` Inferred one, set in composed prose, reads as settled
unless its tier renders beside it, and a narrative sentence doing a badge's
work is judged as a badge (RFC1-19). [Inferred — the principle is RFC6-21's
and RFC1-19's; naming tier in this surface's at-rest set is this clause's;
reasoning in history.]

architecture.md reserves composite maturity rendering to "the graph/status
RFC"; **no contract in this foundational set discharges that reservation**,
but **RFC 0002 carries it as an explicit deferral**, so discharge is an
amendment to RFC 0002 or a named successor. Until then Polaris renders no
composite number, wherever it eventually lands. Reader-controlled density is
deferred (SDR-17's "later"); when added it changes presentation depth only,
never the fact set (RFC6-21).

### 3.5 Capability deep dives — the composition contract

**RFC7-17 — Bands, machine-distinct; three authority classes, closed.** A deep
dive composes named bands, each block declaring its band machine-readably
(RFC7-33). The binding content is the **authority class per band**: every band
falls in exactly one of three classes, no block straddles two, and no fourth
class exists. The V0 composition is: the **argument band** — authored,
non-normative (RFC7-2 (b)): capability thesis and outcome, why it exists
(anchored to the motivating principle or decision, never restating it),
related capabilities; the **contract band** — referenced, verbatim-reachable:
requirement/scenario identities and titles linking to the verbatim leaf,
accepted contracts, declared topology placement, active proposal deltas per
RFC7-26; the **reality band** — kernel-computed, VIS-2-governed: current
status (RFC7-16), implementation mappings with the four SDR-3 classes queryably
distinct (RFC1-16), evidence summaries, contradictions and open challenges
(first-class in the readable layer — prose must not resolve what adjudication
has not), open work, and intent history (adoptions, amendments, dismissals —
not a commit log).

**Exactly these three bands, in this order, are the V0 default** *(owner
decision B7)* — count and ordering are a V0 default, not a frozen constraint;
the three authority classes are foundational and not negotiable at any V. A
narrative composing its deep dive differently still assigns every band to one
of the three classes and declares it machine-readably.

**RFC7-18 — Never a second computation, never a second copy.** Every
reality-band fact comes from the kernel's **single evidence drawer** for the
selection (RFC6-18/19): Polaris chooses altitude, ordering, and deferral —
never contents. Work items are reached through the drawer and the scheduler's
typed adapter; Polaris holds no copy of work state (RFC4-5). Evidence
summaries summarize drawer facts and link to resolvable artifacts; they never
introduce a fact the drawer lacks.

**RFC7-19 — Empty is honest.** A block with no content collapses to one honest
line (what is absent, with its Unknown reason where a claim is implicated) —
never an empty heading, never a hidden section, never scaffold headings
manufacturing the document-browser failure over an undeclared capability.

### 3.6 Generated editorial drafts (SDR-15)

**RFC7-20 — The draft state.** Generated prose appears **only** in the
explicit **editorial-draft** state: machine-marked with its inference
provenance (model, version, inputs — RFC2-7's overlay discipline), visually
distinct, non-visually recoverable (RFC7-33/34), and **non-citable**: never an
anchor target (RFC7-10), never in the citation graph, never satisfying a
claim, never green. `editorial-draft` is a **named RFC2-25 sibling surface
state** — the third, alongside `dismissed-by-decision` and `unadopted-draft` —
minted on this RFC's reported distinction *(owner decision B10)*: an
`unadopted-draft` awaits an adoption gate into *authority*; an
`editorial-draft` awaits a human authorship act into a *non-authoritative*
artifact and stays non-citable even after adoption. Computing a draft is
inference: absent SEC-2 named-provider consent it is **not computed** — the
draft layer renders Unknown (`unconsented-source-or-provider`), visibly a
policy state; the curated skeleton, referenced authority, and deterministic
derived layer must carry a fully readable surface without it.

**RFC7-21 — Adoption is a human act.** A draft becomes curated narrative only
through an attributed human adoption act. **The adopter attests per claim
block**: RFC7-2 is enforced at adoption, claim by claim — a draft sentence
carrying a project-fact claim that cannot be anchored, labeled, or marked
non-normative may not be adopted as written, and the attestation is recorded
with the act (RFC7-7). The test is the per-claim attestation, never whether
the adopter changed a word: no conformance ritual requires a non-empty diff,
and no draft is adopted by signature over an unattested whole. Adoption
confers curated status, never authority (RFC7-4).

**Human is a provenance claim, not a stored field.** The adoption act and its
attestation are honored **only under RFC3-16(a)** — an adoption stamp is named
in that clause's own examples, and this is the gate performing the adoption,
so it invokes the predicate rather than trusting the attribution it records.
The loop this closes is specific: RFC7-20 lets an agent generate the draft and
this clause lets an attributed act adopt it, so without the predicate the same
untrusted actor class (SEC-3, as RFC3-16(a) extends it to committed artifacts)
writes the draft *and* the record saying a human adopted it, and no later
reader can tell. Adoption whose owner-act provenance does not verify **does not
bind**: the draft stays a draft and renders unadopted (RFC3-16), never curated
narrative.

**RFC7-22 — Rejection and the queue.** The pending-draft queue is
**Trajectory's** (SDR-18): drafting is work with an owner and a lifecycle,
rendered in Polaris read-only in context. A rejected draft leaves the intent
surface entirely — never retained as ambient half-adopted prose — and the
rejection is recorded on the queue's work item, not in the narrative. Draft
artifacts are inference-layer material with their own declared reproducibility
standard; an expired draft is a discarded projection, never a lost truth.

### 3.7 Authoring and adoption workflow

**RFC7-23 — Acts and gates.**

| Act | What changes | Gate |
|---|---|---|
| **Edit prose** | Wording within existing structure of a curated Narrative | RFC7-7's write discipline **and RFC7-2 at the act**, per claim (RFC7-2's authoring-act rule — this row is not an exemption); materiality assessed per RFC7-25 |
| **Edit structure** | Reading order, section set, claim-block anchor sets, canonical diagram set | Same artifact class and discipline (SDR-13 — deliberately **not** a separate governance tier); presumptively **material** (RFC7-25) |
| **Adopt editorial draft** | Draft → curated narrative | Human act; RFC7-2 enforced (RFC7-21) |
| **Author/adopt intent artifacts** | Doctrine drafts, spec deltas, capability/topology declarations — drafted, reviewed, **adopted in reading context** | The target artifact's own gate, unchanged: owner sign-off per VIS-4 for shape-level deltas; the spec-adoption gate stays closed absent the VIS-4 amendment event; Polaris confers nothing |

**RFC7-24 — The SDR-18 seam.** Trajectory owns the **drafting queue and work
lifecycle**; Polaris owns the **contextual intent-authoring and adoption
experience**. Queue state, assignment, and progress live in the work surface;
Polaris renders that state read-only and hosts the acts — an adoption gate is
only meaningful if the owner comprehends what they adopt, and comprehension is
a reading act. No queue store exists under `.syzygy/intent/**`; no narrative
store under `.syzygy/work/**`. Each act is recorded once, in the artifact's own
governing location.

**RFC7-25 — Materiality and review (SDR-14).** Fresh-reader review applies to
**material narrative changes and release milestones**, not every prose
correction. A change is material when it alters what a fresh reader would take
the project to be, promise, or refuse — with a deterministic floor: changes to
the reading order, the section set, a claim block's anchor targets, or
manifesto/thesis sections are **always material**. The floor is computable and
is this clause's load-bearing part; nothing below weakens it.

**Declaration is asymmetric** *(owner decision B6: "Escalation is free and
self-service; de-escalation requires the owner.")*. For wording-only edits the
authoring party may declare a change **material**, never **immaterial**; only
the owner, or a contest's resolution, classifies a change immaterial. An
undeclared wording-only edit proceeds without review but is **never recorded
as immaterial on the strength of the author's silence**: its classification
stays open and contestable until an owner classification or contest resolution
closes it. Self-declaration would leave the review decision with the party
that has the incentive to avoid review, frequently an agent; VIS-4 states
classification is never made by the agent performing the change.

**Review triggers are not narrative-edit-only.** A block entering the
RFC7-11(a) **target-changed** state is itself a review trigger, whether or not
a word of narrative was touched — otherwise a narrative can rot indefinitely,
every anchor resolving and no change ever becoming "material".

A failed review is **recorded in `.syzygy/governance/decisions/`** — a
recorded human judgment, not narrative content — and is **rendered** on the
narrative's surface, machine-readably (RFC7-33), until a subsequent pass clears
it. "On the narrative's surface" is a **rendering duty, never a storage
location**: storing the record under `.syzygy/intent/**` would put a VIS-3
review-failure record — whose effect is to freeze autonomous adoption — inside
the tree RFC7-3 says may be deleted without changing any truth, status, work,
consent, or normative fact.

**The verdict is honored only under RFC3-16(a).** The record's home makes it
governance-plane content, and that plane is writable by the untrusted actor
class (SEC-3's class, extended to committed artifacts by the premise
RFC3-16(a) states), so a *pass* in `decisions/` is a claim by whoever wrote the
file until its owner-act provenance verifies. The stake: the verdict's effect
under VIS-3 is to lift or hold the freeze on autonomous adoption, so a
worker-committed pass would lift the freeze that exists to stop that same
actor class from adopting its own prose. A verdict whose provenance does not
verify **does not clear the freeze** — the failure stands rendered and the
condition mints a contradiction (RFC3-16(a)'s effect rule), rather than the
freeze quietly resolving in the author's favor.

Agents may draft repairs freely (VIS-3's freeze reaches adoption, never
authorship) — freely as to *permission*, never as to conformance: a drafted
repair is an authoring act and crosses RFC7-2's per-claim check like every
other (RFC7-2, RFC7-23). [Inferred: materiality, not a structure/prose split,
is the gate axis — SDR-13's rejection of the split composed with SDR-14's
review scope.]

---

## 4. Violation cases

*Package numbering; cases are distributed across modules, never renumbered.
Cases 8, 9 and 11 are in `rendering-and-surface.md`; cases 10, 13 and 15 span
both modules and are held in `README.md` §4.*

1. *(RFC7-2)* A generated capability summary states a fallback behavior no
   normative artifact asserts, unanchored and unlabeled, in the register of
   intent — and an agent later implements against it.
2. *(RFC7-3)* A work item's warrant cites a Polaris paragraph; or a drawer
   lists a narrative section as supporting evidence.
3. *(RFC7-11)* A requirement anchor broken by a spec edit keeps rendering as a
   live citation; or the surface silently re-anchors to the nearest-titled
   requirement.
4. *(RFC7-12/14)* Requirement text "summarized for readability" at the leaf,
   and the summary — not `openspec/**` — settles a dispute.
5. *(RFC7-16/18)* A capability paragraph reads "fully verified and stable" with
   no evaluation identity; or a Polaris-side rollup disagrees with the drawer.
6. *(RFC7-20/21)* Generated prose in curated style with a hover tooltip as its
   only marking; or a draft paragraph quoted into a review as project intent
   before any adoption act.
7. *(RFC7-23/24)* A drafting queue materializes under `.syzygy/intent/**`; or
   an "adopt" affordance adopts a doctrine draft without the owner's VIS-4 act.
12. *(RFC7-10/11(a)/25)* A block anchored to `SEC-2` keeps rendering as a live
    citation after SEC-2 is amended in place, and an agent reading at the
    argument altitude implements the superseded rule; or a narrative sits
    unedited for a year while every anchored target moves beneath it and no
    review triggers because no narrative change was "material".
14. *(RFC7-9)* A twenty-anchor set at section granularity: every claim
    derivable from something in the set, every anchor resolving, every machine
    attribute present, and no challenger able to name the support they contest.

---

## 5. Integration (module-local)

**Relies on RFC 0001:** the presentation profile (RFC1-7) this module requires
and drafts; the opaque-identifier discipline (RFC1-10) behind entity identity
and RFC7-11(a)'s same-identifier drift case; capability identity and
no-silent-inference (RFC1-14) behind RFC7-15; mapping-class distinctness
(RFC1-16) in the reality band; the badge rule (RFC1-19) behind RFC7-16's tier;
the plane rule (RFC1-22) that stops a proposed delta being anchorable at the
leaf. **On RFC 0002:** the inference-overlay discipline (RFC2-7) an editorial
draft carries; the verbatim label + tier + reason + freshness vocabulary
(RFC2-10/24/25) — including `editorial-draft` as the third sibling surface
state RFC7-20 mints; the admissibility floor made operational (RFC2-12) behind
RFC7-9; the revision-binding pattern (RFC2-11, RFC2-18) which RFC7-10's
target-state component **imitates and never extends**, so RFC7-11(a) mints no
RFC2-24 Unknown reason; V0 reconciliation staging (RFC2-19) wherever the
reality band shows merged work. **On RFC 0003:** `intent/` as a
schema-versioned governed namespace (RFC3-18) and the cache exclusion
(RFC3-20); spec anchors and their degrade-never-guess rule (RFC3-28); the
verbatim identity scheme (RFC3-27); local-state rules (RFC3-21); and the
**owner-act provenance predicate (RFC3-16(a))**, which gates two clauses here —
draft adoption (RFC7-21) and the review verdict (RFC7-25). **On RFC 0004:** the
OpenSpec adapter's verbatim read and anchor obligations (RFC4-10) behind
RFC7-14; the anti-duplication invariant (RFC4-5) behind RFC7-18. **On
RFC 0005:** the egress choke point (RFC5-14/15) behind RFC7-20's consent gate;
act attribution (RFC5-25) behind RFC7-7. **On RFC 0006:** selection references
(RFC6-1), unresolvable/retired outcomes (RFC6-5), durable-identifier anchoring
(RFC6-8/9), no auto-redirect (RFC6-11), the label vocabulary (RFC6-14), the
single drawer (RFC6-18/19), citation rendering (RFC6-20), the
minimal-density fact-set rule (RFC6-21), and scenario contexts (RFC6-24).

**Provides to RFC 0008 (Trajectory):** the SDR-18 seam obligations
(RFC7-22/24) — the drafting queue's ownership, the read-only rendering
contract, and where a rejection is recorded.

**Hands to module 2 (`rendering-and-surface.md`):** every distinction drawn
here is subject to RFC7-33/34's machine-parity and non-visual obligations; the
primary narrative RFC7-6 requires is RFC7-30's entry point; RFC7-25's review
records share their home and their RFC3-16(a) gate with RFC7-31's verdicts.

---

## 8. Owner questions

*Package numbering; both open questions in the package own clauses in this
module. Answered items keep their number and their reasoning is in
`../../history/RFC-0007-history.md` §8. Full package index: `README.md` §8.*

2. **Primary-narrative cardinality (RFC7-6) — OPEN.** Proposed: one primary
   plus optional named narratives. The stricter alternative — exactly one,
   period — forecloses audience-specific accounts at zero present cost. Confirm
   the permissive default?
4. **Rejected-draft retention (RFC7-22) — OPEN.** Proposed: discard on
   rejection, the rejection recorded on the Trajectory queue item. The
   alternative — retaining rejected drafts as inference records — aids audit of
   generator quality at the cost of accumulating non-citable prose someone may
   quote anyway. Confirm discard?

---

*End of module 1 of 2. Clauses RFC7-1 … RFC7-25, with lettered sub-clauses
RFC7-2(a)–(c), RFC7-9(a)–(c), and RFC7-11(a). Contiguous, nothing retired,
merged, or renumbered. Amend in place, add lettered sub-clauses, never
renumber.*
