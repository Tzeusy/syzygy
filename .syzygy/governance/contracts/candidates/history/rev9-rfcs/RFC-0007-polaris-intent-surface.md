# RFC 0007 — Polaris (Intent Surface)

**Status:** Proposed foundational contract. This line is a self-declaration at authoring time (RFC3-16): effective status is established solely by the owner-act record binding this file's exact content digest, and acceptance edits nothing here. Absent such a record, this contract binds nothing.
**Date:** 2026-07-30 (amended through 2026-08-02)
**Serves:** VIS-1…VIS-7; SEC-2, SEC-4, SEC-5. Implements SDR-13…SDR-18; honors SDR-28/29/30 for portfolio rendering; resolves the Polaris portion of SDR §5 question 10. Builds on RFC 0001 (presentation profile, Proposal exclusivity, capability identity), RFC 0002 (label/tier/reason vocabulary, V0 staging), RFC 0003 (`.syzygy/intent/**` namespace class, workspace manifest, spec anchors), RFC 0006 (selection, URLs, drawer, parity — cited, never duplicated).

---

## 0. Reader's summary (non-normative)

*Plain-language orientation. If this section and a clause ever disagree, the
clause wins.*

- Polaris is the **intent surface**: a progressively disclosed argument for
  what the project is — thesis → promises → architecture → capabilities →
  exact requirement text — with evidence and work one step away.
- Its two load-bearing invariants: **every factual sentence in the narrative
  is either anchored to the artifact that owns the fact, explicitly marked
  non-normative, or epistemically labeled** — no fourth kind; and **nothing
  in the system may ever cite a Polaris page as authority**. Deleting the
  whole narrative tree changes no truth.
- The feared failure isn't fabricated prose — it's a *faithful paragraph
  that later gets quoted instead of the rule*. So requirement and doctrine
  text renders **verbatim at the leaf**, never paraphrased in normative
  position, and anchors record the **state of their target at authorship**:
  if the cited rule later changes, the block renders "target changed since
  authorship" instead of silently staying current.
- **AI-generated prose** exists only as a marked, non-citable
  `editorial-draft` until a human adopts it claim-by-claim — and that
  adoption act itself needs verifiable owner provenance (RFC3-16(a)), so the
  same untrusted actor can't write the draft *and* the record saying a human
  adopted it.
- Every altitude of the narrative must be a **true coarser read** — a reader
  who stops early has a simpler model, never a false one. Status display is
  minimal by default but always carries label + tier + freshness; no
  composite "maturity score" exists anywhere.
- The acceptance test is a **cold-open comprehension walkthrough**: a fresh
  reader must be able to say why the project exists, what it refuses to be,
  where exactness lives, and **one thing the project doesn't know about
  itself** — a surface passable only by confident green is fiction.
- Everything visual is machine-readable and keyboard-reachable; a
  distinction only pixels carry doesn't survive an endpoint response.

Structure: §3 is the contract (RFC7-1 … RFC7-38); §4 violation cases; §8
owner questions, answered ones marked in place.

---

## 1. Summary

The semantic contract of the intent surface: "a cohesive visual argument for
what a project is, why it exists, what it promises, how it is architected, and
what its specifications require, progressively disclosing from white-paper
narrative into exact capabilities, requirements, contracts, evidence, and
work" [Observed: SDR §2 charter]. It defines the **curated narrative model**
(narrative, section, claim block, reading order, citation graph) as a
**governed presentation artifact** per SDR-13 — versioned, attributed,
revertible, human-readable, **non-authoritative** — under two load-bearing
invariants: **every load-bearing narrative claim resolves to the artifact that
owns the fact, or is explicitly marked non-normative**; and **nothing anywhere
in the system may cite a Polaris rendering as authority**; and, because
citation and generation are not the only doors, an anchor binds the **state**
of the target it was authored against, so drift renders as drift rather than
as currency (RFC7-10, RFC7-11(a)). It fixes claim
blocks and source anchors (SDR-16), verbatim spec leaves, the capability
deep-dive contract, generated editorial drafts (SDR-15), the
authoring/adoption workflow and its SDR-18 seam with Trajectory,
proposed-state rendering, the fresh-reader comprehension test as acceptance
criterion (scope per SDR-14), machine-readable non-visual parity, and
multi-project navigation. **Semantics only**: no renderer, layout, file
format, or stack.

---

## 2. Motivation and doctrine grounding

[Observed] Doctrine gives Polaris identity and anti-thesis at once: Syzygy is
"not a documentation portal" — "a Syzygy from which no work is ever dispatched
has failed, regardless of how good its documents look" [vision.md] — yet the
intent surface must displace "the README-and-ad-hoc-investigation ritual as
the owner's instinctive first stop" [vision.md, Success]. The charter's
not-satisfied-by list binds (SDR §2). [Inferred] The failure directions are
opposite and both must be designed against: the **document browser**
(authority present, no argument) and the **detached brochure** (argument
present, prose unanchored — and, worse, *cited*). The dangerous artifact is
not fabricated prose but a *faithful, correctly-derived paragraph later
quoted instead of the rule* — a second source of doctrine formed with nothing
amended [Observed: `05-POLARIS-BRIEF.md` §4.3; research, non-authoritative].

[Observed] The owner resolved the research's central governance question
against its recommendation: SDR-13 rules the narrative **a governed
presentation artifact** — neither pure governance nor pure presentation, and
explicitly *not* the recommended structure/prose split. SDR-14 scopes
fresh-reader review to material changes and release milestones; SDR-15 makes
generated prose a non-citable editorial draft until human adoption; SDR-16
sets citation granularity at claim blocks; SDR-17 sets status minimal by
default; SDR-18 gives Trajectory the drafting queue and Polaris the contextual
authoring/adoption experience. This RFC binds those rulings.

---

## 3. The contract

Clauses are numbered `RFC7-n`. Amend in place; retire rather than renumber. Parentheticals beginning
*History:* are amendment records — when and why text changed — and carry
no normative force; the clause text around them is the contract.

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
**(a) anchored** — resolvable through its claim block's source anchors (§3.3)
to the one artifact that owns the fact; **(b) explicitly non-normative** —
framing, motivation, analogy, transition, or reader guidance, machine-marked
as carrying no normative force; or **(c) epistemically labeled** — Observed
with its evidence link, Inferred with its inference provenance, or Unknown,
per trust-and-evidence.md. There is no fourth kind: an unanchored, unlabeled,
unmarked project-fact claim in curated narrative is a **defect**, not a style
choice. Granularity is the claim block (SDR-16) — the obligation binds
claims; the mechanism binds blocks.

**The check binds the authoring act, not one path through it.** RFC7-2
conformance is a property of **any act that produces curated narrative** — a
human typing prose, an agent repairing prose under VIS-3's authorship
allowance, or the adoption of an editorial draft (RFC7-21) — and is assessed
per claim at the act. No authoring path reaches curated narrative without
crossing this check; RFC7-21 is one crossing point, not the only one
(RFC7-23, RFC7-25).

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
| **Curated diagram** | A hand-composed visual with anchored or marked elements (§3.8) | The composition |
| **Editorial draft** | Generated candidate content in the SDR-15 state (§3.6) | Nothing; non-citable by construction |

Identifiers are opaque and label-independent (RFC1-10 discipline), minted by
the recorded authoring act. Personal view state (bookmarks, density toggles,
reading position) is **not** part of this model: it lives in `.syzygy/local/`
under VIS-6, exception (a) — never truth-bearing, never a snapshot input
(RFC3-21).

**The presentation profile is required for any governed project Polaris
renders — and Polaris drafts one rather than presuming it** *(ruled at
acceptance by owner decision A4).* Without the profile Polaris has no thesis,
no reading order, and no progressive disclosure, and degenerates into a
**disconnected specification browser**, which the SDR §2 charter names as a
form that does not satisfy Polaris; RFC7-30's acceptance test, which enters at
the primary narrative, would also have no entry point.

**The requirement does not violate RFC1-7's "never presumed present", because
nothing is presumed.** On first render of a project that has not loaded the
profile, Polaris **drafts a default presentation profile for owner sign-off**
and renders it as `unadopted-draft` until signed. That is the RFC2-24 reason #1
resolution route applied exactly as written — "first-pass drafting for owner
sign-off" — and it keeps profile presence an **act** rather than an assumption:
until the owner signs, the profile is declared-but-unadopted and every
narrative element above it renders unadopted with it. A project may still
decline the profile permanently; Polaris then renders the reduced form and says
so, rather than pretending. What is barred is the third path — Polaris behaving
*as if* a profile were present because one is required. [Inferred — the
bootstrap route is the owner's decision; its grounding in reason #1 is this
RFC's, and is what reconciles the requirement with RFC1-7 rather than
overriding it.]

**RFC7-6 — One primary narrative.** A governed project has at most one
**primary narrative** — the front door the comprehension test (§3.10) enters.
Additional named narratives are permitted under the same class and rules;
none outranks another, because none is authoritative at all.

**Thin, never absent.** On an undeclared or thin project the primary narrative
may be **thin, or Syzygy-drafted and unadopted (§3.6), but never absent**: a
predominantly-Unknown catalog under an honestly thin narrative is correct
output (RFC7-15, RFC7-31), and it is the narrative's *presence* that keeps
RFC7-31's protection of honest thinness meaningful and the comprehension test
runnable on v1.md's proving ground — "real, messy, already running, mostly
undeclared" [Observed: v1.md]. Absence is not thinness; it is a missing front
door, and it fails RFC7-30 rather than passing it trivially.

**RFC7-7 — The governed-presentation-artifact class (SDR-13).** Every
narrative-model artifact is **versioned, attributed, revertible,
human-readable**: every change is a Syzygy-attributed, atomic, individually
revertable write (SEC-4, first clause — unqualified, binding prose edits
exactly as structure edits); authorship and review state are machine-readable
facts (RFC3-16 discipline); Syzygy never silently overwrites narrative
content it did not author — SEC-4's conflict-surfacing rule applies.
"Governed" names the change discipline, never the content's standing.

**RFC7-8 — Neither cache nor governance authority.** The narrative is
authored content in the governed plane: it stays with the repository at
offboarding (RFC3-18), is not rebuildable and must not live in
`.syzygy/cache/` (RFC3-20), and is not a `governance/` artifact and binds
nothing. The one thing it owns — its composition — is the fact it is the
owning artifact *of*; VIS-6 is satisfied without an exception.

### 3.3 Claim blocks and source anchors (SDR-16)

**RFC7-9 — Granularity, covering, minimality, bounding.** The citation unit is
the **claim block or section source anchor**, never a per-sentence badge
(SDR-16). Every load-bearing claim sits inside a block whose anchor set
**covers** it; an anchor targets exactly one owned artifact. Three properties
are binding, not stylistic:

**(a) Covers.** An anchor set covers a load-bearing claim when the claim is
derivable from the anchored targets **and a reader can determine which
anchor or anchors support it**. Derivability alone is not covering.

**(b) Minimality.** An anchor set carries **no anchor that no claim in the
block relies on**. A surplus anchor is a **defect, not a courtesy**: it
dilutes attribution and is indistinguishable, to a reader, from support.

**(c) Bounding.** A block **must** be bounded so that claim-to-anchor
attribution is recoverable. A block in which it is not — the twenty-anchor
set attached at section granularity, under which every claim is derivable
from *something* in the set and no claim's support can be named — is
**non-conformant**, not merely large: it fails (a) as well as (c), which is
the point of defining covering as attribution rather than derivability.
Splitting is the remedy; it is an obligation, not advice.

The ground is doctrine's **admissibility floor**, not the resolvability of
individual anchors: a challenge is admissible only if it identifies exactly
one claim and states a specific falsifiable concern
[Observed: trust-and-evidence.md; RFC2-12 makes it operational]. A challenger
facing an unattributable block can name the claim but not the support they
are contesting, so the challenge is unanswerable without re-deriving the
author's intent. That each anchor resolves individually is a different
property and does not supply per-claim attribution.

**RFC7-10 — Anchor form.** A source anchor is machine-readable and typed:
**(target class, target identifier, optional fragment, target state)**, target
class one of: a **kernel entity reference** (selection reference per RFC6-1, optionally
evaluation-qualified); a **doctrine rule or accepted-contract citation**
(stable identifier `VIS-n`/`SEC-n`/RFC clause, rendered per RFC6-20); an
**`openspec/**` anchor** (RFC3-28); a **decision or policy identifier**; or
an **evidence artifact identifier** with integrity digest. No target class
exists for narrative content, renderings, or editorial drafts (RFC7-3).
Anchors embed durable identifiers, never labels, paths, or coordinates
(RFC6-8/9).

**The target-state component** records *what the target said when the anchor
was authored*: for a declared or normative artifact (doctrine rule, accepted
contract clause, `openspec/**` requirement or scenario, decision, policy,
evidence artifact), the target's **revision**; for a kernel entity reference,
the **evaluation identity** at which the target was read together with the
label + tier + reason the reference then carried (RFC6-14's vocabulary,
verbatim). It is observed at
the authoring act and is never rewritten by a later read — an anchor binds a
target *and the state of that target it was authored against*. This imitates
a pattern the kernel already applies everywhere else: RFC2-11 binds a report
artifact to the revision it names and renders it stale otherwise, and RFC2-18
pins the exact intent revision so post-merge drift surfaces as a *new gap*
rather than a retroactive failure. Recording the target state creates no new
authority and no new epistemic state; what it enables is RFC7-11(a).

**RFC7-11 — Broken anchors render Unknown, never silent.** When an anchor no
longer resolves — target retired, spec anchor broken by edit, evidence gone —
the claim block renders the break **on the primary surface**: the anchored
claim degrades to Unknown, the break is named (which anchor, which target;
RFC6-5 outcome `unresolvable` or `retired`), and the same state is served to
machine consumers (§3.11). The narrative never silently drops an anchor,
re-guesses a target (RFC3-28: degrade, never guess), auto-redirects to a
successor (RFC6-11), or keeps rendering the claim as anchored. A dangling
anchor rendered as a live citation is a trust-floor violation [Observed:
trust-and-evidence.md, floor bullet 2].

**RFC7-11(a) — Resolving anchors whose target changed render as drifted,
never as current.** Where an anchor **still resolves** but its recorded target
state (RFC7-10) differs from the target's current state — a cited rule amended
in place under RFC1-10's same-identifier discipline, a requirement re-worded,
a referenced kernel entity whose label, tier, or reason now differs from the
one recorded at authorship — the claim block
renders **`anchored — target changed since authorship`** on the primary
surface, naming which anchor and what moved (recorded state versus current),
and the identical state is served to machine consumers (§3.11). The block is
**marked for RFC7-25 review**. It is never rendered as silently current, and
the drift marker is never cleared by anything but an authoring act that
re-reads the target. A **new evaluation identity alone is not drift**: for a
kernel entity reference, divergence is a change in the rendered label, tier,
or reason, not the passage of evaluations — otherwise every block would drift
on every evaluation and the marker would carry no information.

This is a **Polaris-local rendering obligation over a resolving anchor**, not
an epistemic state: the anchor resolves and the fact is present, so nothing
here mints, implies, or requires an RFC2-24 Unknown reason — that vocabulary
is closed and amended only by RFC 0002. Contrast RFC7-11, where the anchor
stops resolving and the claim genuinely degrades to Unknown.

[Inferred] Drift is the third door to a second source of doctrine. RFC7-3
closes citation and RFC7-20/21 close generation; a faithful, correctly-derived
paragraph whose cited rule moved underneath it reaches §2's named dangerous
artifact through **time** instead. A reader is permitted to stop at an early
altitude with a true, coarser model (RFC7-13); that permission is only safe if
the coarse read cannot be quietly wrong.

**RFC7-12 — Restatement discipline.** An anchored block renders *about* its
target; the target's own text is one step away. For **adjudicative material**
— doctrine rules, non-goals, requirement text — the operative text a reader
relies on is the owned artifact's verbatim text, never a paraphrase in
normative position: a faithful paraphrase that gets quoted becomes the
operative text (§2's failure mode).

### 3.4 White-paper composition and progressive disclosure

**RFC7-13 — Progressive disclosure: the obligation, and a V0 default path.**
The binding content is the obligation **per altitude**: a narrative discloses
progressively through named altitudes; **each altitude is a self-sufficient,
honest read** — a reader who stops at any altitude has a true, coarser model,
never a false one (VIS-1: simplify presentation, never content); every
narrative descends to a **verbatim specification leaf** (RFC7-14), so
exactness is always reachable rather than summarized away. The path bounds
*browsing*; a claim block's anchor is always **one step** from the owned
artifact.

The **V0 default ordering** is: thesis/manifesto → architecture story →
capability catalog → capability deep dive → verbatim specification leaf. The
ordering and the altitude count are a **V0 default, not a frozen foundational
constraint** (§8 q7): an additional named narrative under RFC7-6 may order its
altitudes differently for its audience, and remains bound by the per-altitude
obligation and the verbatim-leaf terminus. The primary narrative uses the V0
default unless the owner rules otherwise.

**RFC7-14 — The verbatim leaf.** Requirement and scenario text renders
**verbatim from `openspec/**`** under the artifact contract's own identity
scheme (RFC3-27, RFC4-10) — never paraphrased, reordered, or summarized in
normative position. Polaris may present an ordering and annotate around
requirement text; it may never store a reorganized copy [Observed:
architecture.md, schema ownership]. The same holds for doctrine rule text.

**Under a proposed-scenario reading (RFC7-26), the leaf renders the adopted
text as the operative text**, with the proposal's delta rendered **adjacent**
— visually and queryably distinct from it (RFC6-24), never substituted for
it, never interleaved so that a reader cannot tell which text is which, and
never anchorable (RFC1-22). Rationale: the leaf is the one place Polaris tells
a reader that the text in front of them *is* operative (RFC7-12). Rendering
proposed requirement text in that position would manufacture the most quotable
unadopted text in the system; rendering adopted text alone would make the
proposed reading silently incomplete at its most exact altitude. Adjacency
answers both. [Authored position, not an owner ruling — surfaced at §8 q6.]

**RFC7-15 — Capability catalog honesty.** The catalog is a projection of
**declared** capability identities (RFC1-14): nothing appears that no
declared artifact asserts; drafted capabilities render unadopted; unmapped
code renders Unknown, never silently inferred into a capability [Observed:
v1.md]. A predominantly-Unknown catalog on an undeclared project is correct
output, rendered as normal — not broken — with RFC2-24 reasons
(`missing-declaration` foremost) and resolution routes.

**RFC7-16 — Status in the narrative: minimal by default (SDR-17).** Every
rendered status is kernel-computed at an identified evaluation and carries
the label + tier + reason + freshness vocabulary **verbatim** (RFC6-14):
evaluation-stamped; staleness visible on the narrative page itself — the
narrative is a primary surface [Observed: trust-and-evidence.md, Staleness].
Default density is minimal: per capability or major claim, one epistemic
state — **its label with its RFC2-25 tier**, and its freshness — with its
evaluation identity and a drawer/Trajectory handoff — no metric walls,
trends, counts, or **composite maturity number**. **Tier is named in the
at-rest set for the same reason staleness is**, and this clause fixes it
there rather than leaving it to disclosure: RFC6-21 already forbids the
*fact set* shrinking at minimal density, but it says nothing about which
facts the minimal *depth* must show, and Polaris is the surface where the
omission bites hardest. A `report-fact` Observed claim or an
`asserted-by-worker` Inferred one, set in composed narrative prose, reads as
settled unless its tier renders beside it — and a narrative sentence doing a
badge's work is judged as a badge (RFC1-19). Label without tier at rest is
that sentence. [Inferred — the principle is RFC6-21's and RFC1-19's; naming
tier in this surface's at-rest set is this clause's.]
architecture.md refuses to collapse maturity's axes into one status and
reserves any composite maturity rendering to "the graph/status RFC" — **no
contract in this foundational set discharges that reservation**: neither
RFC 0001 nor RFC 0002 defines composite maturity, and this contract names no
successor. It is no longer merely unassigned, however: **RFC 0002 §7 now
carries it as an explicit deferral**, so the obligation exits this phase
tracked rather than lost, and its discharge is an amendment to RFC 0002 or a
named successor. Until then Polaris renders no composite number, regardless
of where it eventually lands.
Reader-controlled density is deferred (SDR-17 "later"); when added, it
changes presentation depth only, never the fact set (RFC6-21). A narrative
sentence doing a badge's work is judged as a badge (RFC1-19).

### 3.5 Capability deep dives — the composition contract

**RFC7-17 — Bands, machine-distinct; three authority classes, closed.** A deep
dive composes named bands, each block declaring its band machine-readably
(§3.11). The binding content is the **authority class per band**: every band
falls in exactly one of three classes, no block straddles two, and no fourth
class exists. The V0 composition is: the
**argument band** — authored, non-normative (RFC7-2 (b)): capability thesis
and outcome, why it exists (anchored to the motivating principle or decision,
never restating it), related capabilities; the **contract band** —
referenced, verbatim-reachable: requirement/scenario identities and titles
linking to the verbatim leaf, accepted contracts, declared topology
placement, active proposal deltas per §3.8; the **reality band** —
kernel-computed, VIS-2-governed: current status (RFC7-16), implementation
mappings with the four SDR-3 classes queryably distinct (RFC1-16), evidence
summaries, contradictions and open challenges (first-class in the readable
layer — prose must not resolve what adjudication has not), open work, and
intent history (adoptions, amendments, dismissals — not a commit log).

**Exactly these three bands, in this order, are the V0 default** (§8 q7) —
the count and ordering are a V0 default, not a frozen foundational
constraint; the three authority classes are foundational and are not
negotiable at any V. A narrative that composes its deep dive differently
still assigns every band to one of the three classes and declares it
machine-readably.

**RFC7-18 — Never a second computation, never a second copy.** Every
reality-band fact comes from the kernel's **single evidence drawer** for the
selection (RFC6-18/19): Polaris chooses altitude, ordering, and deferral —
never contents. Work items are reached through the drawer and the scheduler's
typed adapter; Polaris holds no copy of work state (RFC4-5). Evidence
summaries summarize drawer facts and link to resolvable artifacts; they never
introduce a fact the drawer lacks.

**RFC7-19 — Empty is honest.** A block with no content collapses to one
honest line (what is absent, with its Unknown reason where a claim is
implicated) — never an empty heading, never a hidden section, never scaffold
headings manufacturing the document-browser failure over an undeclared
capability.

### 3.6 Generated editorial drafts (SDR-15)

**RFC7-20 — The draft state.** Generated prose appears **only** in the
explicit **editorial-draft** state: machine-marked with its inference
provenance (model, version, inputs — RFC2-7's overlay discipline), visually
distinct, non-visually recoverable (§3.11), and **non-citable**: never an
anchor target (RFC7-10), never in the citation graph, never satisfying a
claim, never green. Computing a draft is inference: absent SEC-2
named-provider consent it is **not computed** — the draft layer renders
Unknown (`unconsented-source-or-provider`), visibly a policy state; the
curated skeleton, referenced authority, and deterministic derived layer must
carry a fully readable surface without it.

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
attestation are honored **only under RFC3-16(a)** — an adoption stamp is
named in that clause's own examples, and this is the gate that performs the
adoption, so it invokes the predicate rather than trusting the attribution it
records. The loop this closes is specific: RFC7-20 lets an agent generate the
draft prose and this clause lets an attributed act adopt it, so without the
predicate the same untrusted actor class (SEC-3, as RFC3-16(a) extends it
to committed artifacts) writes the draft *and*
writes the record saying a human adopted it, and no later reader can tell.
Adoption whose owner-act provenance does not verify **does not bind**: the
draft stays a draft and renders unadopted (RFC3-16), never curated narrative.

**RFC7-22 — Rejection and the queue.** The pending-draft queue is
**Trajectory's** (SDR-18): drafting is work with an owner and a lifecycle,
rendered in Polaris read-only in context. A rejected draft leaves the intent
surface entirely — never retained as ambient half-adopted prose — and the
rejection is recorded on the queue's work item, not in the narrative. Draft
artifacts are inference-layer material with their own declared
reproducibility standard; an expired draft is a discarded projection, never a
lost truth.

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
only meaningful if the owner comprehends what they adopt, and comprehension
is a reading act. No queue store exists under `.syzygy/intent/**`; no
narrative store under `.syzygy/work/**`. Each act is recorded once, in the
artifact's own governing location.

**RFC7-25 — Materiality and review (SDR-14).** Fresh-reader review applies to
**material narrative changes and release milestones**, not every prose
correction. A change is material when it alters what a fresh reader would
take the project to be, promise, or refuse — with a deterministic floor:
changes to the reading order, the section set, a claim block's anchor
targets, or manifesto/thesis sections are always material. The floor is
computable and is this clause's load-bearing part; it is not weakened by
anything below.

**Declaration is asymmetric.** For wording-only edits, the authoring party
may declare a change **material** — never **immaterial**. Only the owner, or
the resolution of a contest, classifies a change immaterial. An undeclared
wording-only edit proceeds without review but is **never recorded as
immaterial on the strength of the author's silence**: its classification
stays open and contestable until an owner classification or a contest
resolution closes it. Rationale: the drafted alternative was a
self-assessment by the party with the incentive to avoid review, and that
party is frequently an agent (below). VIS-4 states the general principle that
classification is never made by the agent performing the change; narrative is
non-authoritative and so not strictly bound by VIS-4, and this contract finds
no reason for the principle to invert here. [Authored position — §8 q1 lists
all three options, including the originally drafted self-declaration.]

**Review triggers are not narrative-edit-only.** A claim block entering the
RFC7-11(a) **target-changed** state is itself a review trigger, whether or
not a word of narrative was touched. Without this, a narrative can rot
indefinitely — every anchor resolving, no edit ever made — without any change
becoming "material".

A failed review is **recorded in `.syzygy/governance/decisions/`** — it is a
recorded human judgment, not narrative content — and is **rendered** on the
narrative's surface, machine-readably (§3.11), until a subsequent pass clears
it. "On the narrative's surface" is a **rendering duty, never a storage
location**: a review record stored under `.syzygy/intent/**` would place a
VIS-3 review-failure record — whose effect is to freeze autonomous adoption —
inside the tree RFC7-3 says may be deleted without changing any truth,
status, work, consent, or normative fact.

**The verdict is honored only under RFC3-16(a).** The record's home makes it
governance-plane content, and that plane is writable by the untrusted actor
class (SEC-3's class, extended to committed artifacts by the premise
RFC3-16(a) states), so a *pass* present in `decisions/` is a claim by whoever
wrote the file until its owner-act provenance verifies. The stake is
specific: the verdict's effect under VIS-3 is to lift or hold the freeze on
autonomous adoption, so a worker-committed pass lifts the freeze that exists
to stop that same actor class from adopting its own prose. A verdict whose
provenance does not verify **does not clear the freeze** — the failure stands
rendered and the condition mints a contradiction (RFC3-16(a)'s effect rule),
rather than the freeze quietly resolving in the author's favor.

Agents may draft repairs freely (VIS-3's freeze reaches adoption, never
authorship) — freely as to *permission*, never as to conformance: a drafted
repair is an authoring act and crosses RFC7-2's per-claim check like every
other (RFC7-2, RFC7-23). [Inferred: materiality — not the research's
structure/prose split — is the gate axis; this composes SDR-13's rejection of
the split with SDR-14's review scope.]

### 3.8 Proposed-state presentation

**RFC7-26 — Two reading modes, named in the kernel's vocabulary.** The default
reading mode **is RFC6-24's `Base` context** — the base graph at the
selected evaluation — and is named that. Base includes the **observed**
plane, not only adopted desired state: the reality band (RFC7-17) renders in
full in default reading, and an implementation that builds the default as a
filter over adopted desired state has built the wrong mode. ("As-adopted" may
appear as descriptive prose about the desired-state portion of a Base read;
it is **not** a mode name. Polaris coins no surface-local synonym for a kernel
concept, even a locally coherent one.)

The second mode is a **proposed-scenario reading**: RFC6-24's `Proposed`
context — (base evaluation, selected proposal set) — travelling with every
selection, URL, and query (RFC6-25). Proposed and unadopted material is
unmistakably distinct — visually and machine-readably — everywhere, has no
status authority, turns nothing green, anchors nothing (RFC1-22).

**RFC7-27 — No fictitious consensus.** Competing proposals never collapse
into one merged future: the kernel refuses to union proposals in one
exclusivity group or of undeclared compatibility (RFC1-27; RFC6-24
`incompatible-scenario`); the honest render is *N candidate futures*,
selectable one at a time. Narrative prose describing a proposal in the
register of adopted intent — "the system does X" for an unadopted X — is an
RFC7-2 violation regardless of visual marking.

**RFC7-28 — Curated diagrams.** A hand-composed diagram is narrative content
under every rule here: each named element carries an anchor or a
non-normative/proposed marking; speculated structure never looks like
existing structure [Observed: trust-and-evidence.md]; every encoding means
what its legend says (VIS-7); a text equivalent exists (§3.11). Curated
diagrams claim no reproducibility-from-snapshot and must not imitate the
computed map; embedded computed visuals inherit the map surface's
obligations; curated/computed provenance is a machine-readable attribute on
every visual. Live Orrery transclusion is deferred (§7).

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
| Portfolio narrative | Renders as owner-workspace content (§3.12) | Workspace manifest (RFC3-10/11); never project truth |

Nothing in the "owns" row sources any project fact (RFC7-2/3); every other
row is composition over an authority Polaris cannot amend from within —
amendments run through §3.7's acts and gates.

### 3.10 Fresh-reader acceptance — the comprehension test

**RFC7-30 — The criterion.** This surface's acceptance test is the
**cold-open comprehension walkthrough**: a fresh reader (human or agent, no
authoring context — VIS-3's independence standard), entering at the primary
narrative with navigation confined to Polaris, states in their own words: why
the project exists; what it promises; what it refuses to be (naming at least
one non-goal and reaching its rule text); what its major capabilities are and
how they fit; **where exactness lives** — reaching a verbatim requirement
leaf; and **one thing the project does not currently know about itself** — an
Unknown region and how the surface showed it. The last prompt is
load-bearing: a surface passable only by a uniformly confident read has
rendered comprehensible fiction (VIS-1). A second phase checks answers
against the owned artifacts; divergences are recorded as findings.

**At least one run per release milestone is performed non-visually or
keyboard-only**, exercising RFC7-34's reachability limb: the walkthrough must
test the *paths* between units, not only the units. Without it an
implementation can satisfy RFC7-33/34 on every rendered unit, leave every
path between units pointer-only, and pass this test every time. The
non-visual run's record lives where every other run's record lives
(RFC7-31: execution records in `records/`, judgments in `decisions/`).

**RFC7-31 — Verdict discipline.** The verdict is the owner's recorded human
judgment — never rendered Observed, never a score [Observed: vision.md,
Success]. Two floors are not judgment calls: a **dangling internal link on
the walkthrough path** fails (trust floor, release-blocking); a confident
wrong answer **attributable to what the surface rendered** fails. A reader's
own misreading of an honest page, and a thin result on an undeclared
project, are judgment territory — a predominantly-Unknown narrative over an
undeclared project is **correct output** [Observed: v1.md], never failed for
honest reflection.

**Two artifacts, two homes** *(History: aligned at the rev7 rework with RFC9-45's
three-way split; the release-policy leg is shared and stated there)*. Each
run mints a **walkthrough execution record** — `kernel-recorded`, in
`.syzygy/governance/records/` (RFC3-15) — naming the surface version, the
evaluation identity behind any rendered status, and whether the run was
non-visual/keyboard-only (RFC7-30); absent its record, the test renders
Unknown, never met. The **judgment** — the verdict, its rationale, and the
judging party — is an owner adjudication recorded in
**`.syzygy/governance/decisions/`**, for the same reason RFC7-25's review
records live there: it is a recorded human judgment, not narrative content,
and a decision is a warrant, never evidence. Storing either under
`.syzygy/intent/**` would let deletion of that tree flip a v1.md-tracked
success test from a recorded verdict to Unknown — precisely the consequence
RFC7-3's deletion invariant forbids. The judgment is honored **under
RFC3-16(a)**: the home establishes durability, never authorship, and an
owner judgment a fleet worker could commit is not an owner judgment. A
judgment whose owner-act provenance does not verify — like one that is
unattributed or unreasoned — is recorded as **verdict-unlawful** (a state
of the judgment record, RFC9-45's term for the same protocol) and leaves
the test rendering **Unknown, never met** — the identical outcome this
clause already assigns to an absent record, so an unverifiable verdict buys
nothing a missing one would not. *(RFC9-45 and this clause state one
protocol: defective verdict → recorded `verdict-unlawful`, test renders
Unknown-never-met, gate fail-closed — the same outcome on both surfaces.)*

**RFC7-32 — When it runs (SDR-14).** At **material narrative changes and
release milestones** — not every prose edit; recorded per RFC7-25, in the
record home RFC7-25 and RFC7-31 name, with at least one non-visual/
keyboard-only run per release milestone (RFC7-30). It is the intent-surface
sibling of v1.md's spatial comprehension test: same shape, shareable
protocol, never collapsed into one test.

### 3.11 Machine parity and non-visual recoverability

**RFC7-33 — Every distinction, machine-readable.** Every distinction this
contract draws — **`non-citable` / `presentation-artifact`** (below),
claim-block kind (anchored / non-normative / labeled), the narrative
claim-block **type name** (below), band membership and its authority class,
curated-versus-computed provenance, adopted versus unadopted,
editorial-draft state, proposal-context membership, review state,
RFC7-11(a)'s **target-changed** state, label +
tier + reason + freshness — is carried as a **machine-readable attribute on
the rendered unit**, served identically through the machine-queryable
endpoints (RFC6-13/14) and preserved in plain-text or exported renderings
[Observed: agents are a first-class consumer from day one (vision.md);
endpoints are V0-mandatory (v1.md)]. A distinction available only to pixels
does not survive an endpoint response, a copy-paste into an agent prompt, or
a reader who cannot see it.

**Non-citability travels, on every rendering.** Every narrative-model unit
(RFC7-5) carries the **`non-citable` / `presentation-artifact`** attribute,
required on **every** exported, embedded, or plain-text rendering per this
clause's last sentence — not only on the interactive surface. RFC7-3 is a
prohibition addressed to Syzygy; the external agent consuming RFC6-13's
endpoints is a party RFC7-3 cannot bind, and what it receives carries
epistemic labels, resolvable anchors, and evaluation stamps — every signal
that ordinarily marks trustworthy kernel output. It can tell draft from
curated and not presentation from authority, and the violation it then
commits (§4 case 2) is unattributable to any bound party. This clause's
catch-all opener is not sufficient cover: [Inferred] enumerations of this
shape are implemented as literal field lists, and the one field whose
omission is unrecoverable at the consumer must be named.

**Narrative claim blocks carry a distinguishing type name** in the machine
envelope, separate from the kernel's Claim entity (RFC1-5; RFC1-24 routes all
status through it): an agent querying "claims" about a Capability must never
receive kernel claim instances and narrative claim blocks under one
undifferentiated name. The dual usage in prose has doctrinal cover
[Observed: trust-and-evidence.md, "Status claims vs narrative claims"] and no
prose rename is required — the hazard exists only at this boundary.

**RFC7-34 — Non-visual recoverability.** Every such distinction is
recoverable **without colour, position, or layout** — by label, text, or
structure; visual encodings are legended and mean exactly what the legend
says (VIS-7); every curated diagram has a text equivalent carrying the same
anchored elements and markings. This is the intent-surface counterpart of
the map's co-equal non-3D obligation (SDR-27): an epistemic state a reader
cannot perceive is comprehensible fiction for that reader.

**Reachability — the second limb.** Recoverability governs *encoding*:
whether a distinction can be read once the reader is looking at the unit.
**Operability** is a separate obligation and both bind. Every traversal of
the disclosure path must be operable **without a pointing device**:
RFC7-13's altitudes, a claim block's anchor expansion (including RFC7-11 and
RFC7-11(a) states), and the RFC6-18 drawer handoff. This is the
intent-surface counterpart of v1.md's mandate that keyboard/non-3D
navigation is **always available** on the map — of which SDR-27 supplies only
the semantic-equivalence half, which RFC7-34's first limb already carries. A
surface whose every unit is perfectly recoverable and whose paths between
units are pointer-only has satisfied neither limb, and RFC7-30's non-visual
run is the evidence that it does.

### 3.12 Project and subproject navigation

**RFC7-35 — Multi-project entry.** The multi-project entry renders from the
**workspace manifest** — membership, grouping, ordering, saved views are
workspace concerns (RFC3-11) — while every project-internal fact shown
derives from that project's own plane (SDR-28; RFC3-12). Deleting the
workspace manifest changes what is arranged, never what is true. Unresolvable
entries render Unknown with their reason, never dropped (RFC3-13).

**RFC7-36 — Portfolio narrative is owner-local, never project truth.** The
owner-specific portfolio narrative SDR-29 permits lives in the workspace
manifest's scope — VIS-6, exception (a) territory (RFC3-10) — and renders
**visibly as owner-workspace content**: it is no project's narrative, holds
no claim block over any project's facts beyond references resolving into the
projects' own planes, is never a citation target (RFC7-3 in full force), and
never affects any project's truth, work, or status. There is no portfolio
governance root and this RFC creates none.

**Which §3.2–§3.3 obligations follow it out of `.syzygy/intent/**`.** The
portfolio narrative sits outside the narrative model's residence rule
(RFC7-5), so this clause states the carry-over explicitly rather than leaving
it to inference. **These follow it:** RFC7-2 (every load-bearing claim
anchored, marked non-normative, or epistemically labeled — including the
authoring-act rule); RFC7-7 (versioned, attributed, revertible, never
silently overwritten); RFC7-11 **and RFC7-11(a)** (broken anchors and
target-changed anchors render, never silently current); RFC7-33/34 (machine
parity, the `non-citable` / `presentation-artifact` attribute, non-visual
recoverability and reachability). **These do not follow it, and are already
forbidden by the four constraints above:** claim blocks over any project's
facts, and citability in any form.

**It may not assert any governed project's status.** The four constraints
above forbid a reader being unable to *tell* portfolio narrative from project
truth; they do not by themselves forbid the assertion. This clause does:
portfolio prose may not assert that a governed project is converged, aligned,
verified, healthy, or any other status — visible marking does not license it,
because a narrative sentence doing a badge's work **is judged as a badge**
[Observed: trust-and-evidence.md; RFC1-19]. Cross-project status renders only
as each project's own kernel-computed state, read from that project's plane
(RFC7-35, SDR-28).

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
unchanged (RFC3-32); aggregating a child's Unknowns into anything green is
the VIS-1 violation. **Any roll-up over a child's facts additionally
discloses RFC6-17's full composition** — the RFC6-22 equivalence tuple,
per-label, per-tier, per-Unknown-reason and per-freshness-state counts and
sibling surface states, expandable to members. That obligation is **cited,
never restated here**, because a paraphrase is how a roll-up rule drifts from
the aggregation contract it is supposed to be an instance of. The narrow
reading — labels carried through, no Unknown folded into green — is
satisfiable by a parent narrative rendering a child's district as "Observed
×30" while all thirty are `reduced-fidelity` and twelve are stale, which on a
composed narrative page reads as a settled claim about the child (RFC1-19).

### 3.13 Authority boundary at the OpenSpec seam (binding phase rule)

**RFC7-38 — This contract schedules nothing.** *(History: added at the rev8 rework,
directive item 7.)* This RFC fixes the semantics of the intent surface; it
is **not a specification of record from which implementation work may be
scheduled**. No implementation work for **user-observable Polaris
behavior** may be scheduled solely from this RFC: before implementation,
every observable consequence of RFC7-1…RFC7-37 must either **map to an
approved OpenSpec requirement or scenario** in the governance root's
`openspec/**` plane, or carry an **explicit, reviewed N/A judgment**
recording why that consequence needs no requirement. The surface-
specification phase must produce, as a deliverable, a **clause-to-
requirement coverage matrix** for this RFC — every clause mapped to
requirement identities or to its reviewed N/A — and that matrix is review
material, never authority. This clause creates no OpenSpec content now
(none may exist during bootstrap); it binds the phase boundary so RFC prose
is never quietly treated as an implementable behavioral spec.

---

## 4. Violation cases

1. *(RFC7-2)* A generated capability summary states a fallback behavior no
   normative artifact asserts, unanchored and unlabeled, in the register of
   intent — and an agent later implements against it.
2. *(RFC7-3)* A work item's warrant cites a Polaris paragraph; or a drawer
   lists a narrative section as supporting evidence.
3. *(RFC7-11)* A requirement anchor broken by a spec edit keeps rendering as
   a live citation; or the surface silently re-anchors to the nearest-titled
   requirement.
4. *(RFC7-12/14)* Requirement text "summarized for readability" at the leaf,
   and the summary — not `openspec/**` — settles a dispute.
5. *(RFC7-16/18)* A capability paragraph reads "fully verified and stable"
   with no evaluation identity; or a Polaris-side rollup disagrees with the
   drawer at one evaluation.
6. *(RFC7-20/21)* Generated prose in curated style with a hover tooltip as
   its only marking; or a draft paragraph quoted into a review as project
   intent before any adoption act.
7. *(RFC7-23/24)* A drafting queue materializes under `.syzygy/intent/**`;
   or an "adopt" affordance in Polaris adopts a doctrine draft without the
   owner's VIS-4 act.
8. *(RFC7-26/27)* Two exclusive proposals rendered as one merged future; or
   proposed and adopted architecture prose indistinguishable in an endpoint
   response.
9. *(RFC7-31)* The comprehension test failed because an undeclared project's
   narrative was honestly thin; or passed with a dangling link on the
   walkthrough path.
10. *(RFC7-33/34)* Band structure carried only by background colours; a
    plain-text export losing the adopted/unadopted distinction.
11. *(RFC7-36)* The portfolio narrative asserts "project B is converged" as
    workspace prose a reader cannot tell from project truth — or asserts it
    while *perfectly* marked as workspace prose, which this contract now also
    forbids.
12. *(RFC7-10/11(a)/25)* A block anchored to `SEC-2` keeps rendering as a
    live, current citation after SEC-2 is amended in place, and an agent
    reading at the argument altitude implements the superseded rule; or a
    narrative sits unedited for a year while every anchored target moves
    beneath it and no review ever triggers because no narrative change was
    "material".
13. *(RFC7-33)* An endpoint response or plain-text export carries a curated
    narrative's epistemic labels, resolvable anchors, and evaluation stamps
    but no `non-citable` / `presentation-artifact` attribute — and an
    external agent, unbound by RFC7-3, cites the paragraph in a work warrant.
14. *(RFC7-9)* A twenty-anchor set attached at section granularity: every
    claim derivable from something in the set, every anchor resolving, every
    machine attribute present, and no challenger able to name the support
    they are contesting.
15. *(RFC7-34/30)* Every rendered unit is recoverable without colour or
    layout, and the disclosure path from thesis to verbatim leaf can only be
    traversed with a pointer — passing the comprehension test every time.

---

## 5. Integration

**Relies on RFC 0001:** the presentation profile (RFC1-7); capability
identity and no-silent-inference (RFC1-14); mapping-class distinctness
(RFC1-16); Proposal exclusivity (RFC1-27); the plane rule (RFC1-22).
**RFC 0002:** the verbatim label + tier + reason + freshness vocabulary
(RFC2-10/24/25); V0 reconciliation staging (RFC2-19) wherever the reality
band shows merged work; the admissibility floor made operational (RFC2-12)
behind RFC7-9; and the revision-binding pattern — RFC2-11's evidence–revision
binding and RFC2-18's pinned intent revision — which RFC7-10's target-state
component **imitates and never extends**: RFC7-11(a) is a Polaris rendering
marker over a resolving anchor and mints no RFC2-24 Unknown reason.
**RFC 0003:** `intent/` as a schema-versioned
governed namespace (RFC3-18); spec anchors (RFC3-28); workspace-manifest
boundaries (RFC3-10…14); local-state rules (RFC3-21). **RFC 0004:** the
OpenSpec adapter's verbatim read and anchor obligations (RFC4-10); the
anti-duplication invariant (RFC4-5). **RFC 0005:** the egress choke point
(RFC5-14/15) behind RFC7-20; act attribution (RFC5-25) behind RFC7-7.
**RFC 0006:** selection references, outcomes, URLs, label parity, the single
drawer, scenario contexts — cited throughout, duplicated nowhere.

**Defects reported (not silently diverged from):**

1. **~~RFC 0002 (RFC2-25 sibling surface states).~~ DISCHARGED at acceptance —
   owner decision B10.** RFC2-25's deliberately-outside list now names
   **three** sibling surface states: `dismissed-by-decision`,
   `unadopted-draft` and **`editorial-draft`**, minted on this RFC's reported
   distinction — an unadopted draft awaits an adoption gate into *authority*;
   an editorial draft awaits a human authorship act into a
   *non-authoritative* artifact and stays non-citable even after adoption.
   RFC7-20's distinct rendering is now backed by a named state rather than
   assuming one. **§8 q3 is answered and marked as such.** Downstream
   enumerations in RFC 0006 (RFC6-14, RFC6-17 equivalence tuple) are amended
   from two to three.
2. **RFC 0002 / RFC 0006 (dangling-anchor vocabulary).** RFC7-11's broken
   anchors land in RFC6-5's `unresolvable` outcome, but RFC2-24 has no
   Unknown reason whose resolution route is "repair the reference" —
   RFC 0006 already reported this (its §5 defect note, §8 q3). Polaris is
   the most exposed surface: a citation-dense narrative over an actively
   edited spec hits this case routinely. This RFC supports adding
   `reference-unresolvable` to RFC2-24. *[Update, post-draft: RFC 0002 added
   it as reason #11, citing this finding among its four drivers; the owner may
   still strike it at acceptance (RFC 0002 §8 q1(a)).]*
3. **RFC 0001 (RFC1-7 vs RFC1-22, personal view state)** — *resolved;
   retained for the trail.* As reported: RFC1-7 listed "personal view state"
   as presentation-profile vocabulary, while RFC1-22 places personal
   presentation state **outside every plane** and RFC3-21 bars it from being
   a snapshot input, so reifying it as graph entities sat awkwardly against
   both; this RFC does not (RFC7-5). RFC1-7 has since **qualified** the
   phrase rather than dropping it — the stronger of the two closures, since
   it settles the reading instead of leaving the vocabulary silent — and now
   reads that "personal view state is deliberately **not** reified even here
   — it stays outside every state plane and is never a snapshot input,
   RFC1-22" [Observed — RFC1-7 as of 2026-08-01]. RFC7-5 needs no change.
   **No RFC 0001 change is outstanding on this item.**

**Provides to RFC 0008 (Trajectory):** the SDR-18 seam obligations
(RFC7-22/24). **Provides to RFC 0009 (Orrery):** the curated-versus-computed
provenance attribute (RFC7-28) and the transclusion question (§7).

---

## 6. Alternatives considered

- **The structure/prose governance split** (research FRC-1 Option C:
  structure gated as governance, prose free). Rejected by the owner — SDR-13
  rules the whole narrative one governed presentation artifact, with SDR-14's
  materiality scope doing the work the split aimed at: one artifact class
  (RFC7-7), review triggered by materiality (RFC7-25), not by which half was
  touched.
- **Per-sentence citation badges.** Rejected by SDR-16: the obligation binds
  claims, the mechanism binds blocks; sentence badges tax readability without
  adding challengeability block-level anchors lack (RFC7-9).
- **Narrative edits and editorial drafts as kernel Proposals.** Rejected: a
  narrative change is not a delta to desired state — modeling it as RFC1-27's
  Proposal would put presentation churn in the proposed plane and imply an
  adoption gate into authority that RFC7-4 forbids. Consequence recorded:
  RFC1-27's kind list needs no presentation kind.
- **Generated prose banned outright** (research FRC-2 Option A). Rejected by
  SDR-15: the proving ground is mostly undeclared [Observed: v1.md] and
  first-pass drafting is V0 work; the draft state plus non-citability is the
  floor that makes permission safe. The backlog-noise cost is mitigated by
  RFC7-22 — the queue lives in Trajectory, and rejected drafts leave the
  surface entirely.
- **A portfolio meta-project** for the owner's cross-project story. Not
  taken: SDR-29 gives the portfolio narrative a cheaper lawful home (owner
  workspace, VIS-6, exception (a)) at zero doctrine cost; a meta-project
  remains constructible later under RFC3-31 with no change here.
- **Polaris-local status vocabulary or rollups.** Rejected: the label + tier
  + reason vocabulary is the kernel's and closed (RFC2-24/25); rollups edge
  into the composite-maturity rendering doctrine reserves; SDR-17's minimal
  default needs neither.

---

## 7. Deliberately deferred

Concrete `.syzygy/intent/**` schemas, file grammars, and anchor wire syntax →
implementation under accepted contracts (RFC3-18 versioning and migration
apply). Reader-controlled status density (SDR-17's "later") →
post-acceptance spec material; the minimal default binds now. Live
transclusion of Orrery scenes, and whose reproducibility obligations follow
the embed → RFC 0009 coordination; until then, link-out. Blast-radius preview
of proposed changes → V1 gap-computation material (RFC2-19 staging); nothing
in RFC7-26's proposed mode computes deltas. Certificate rendering → post-V1
certificate RFC (future-tagged). Portfolio-profile detail beyond RFC7-35/36
(cross-project saved selections, workspace URLs) → portfolio profile per
RFC 0006 §7. Link-integrity verification cadence for the citation graph →
quality policy; the obligation and its trust-floor consequence bind here.
**That cadence reaches only anchors that exist and break** (RFC7-11) and, with
RFC7-10's target-state component, anchors whose targets moved (RFC7-11(a));
it never reaches a load-bearing claim that **never carried an anchor at all**,
which is caught only at the authoring act — which is why RFC7-2's check binds
every path to curated narrative rather than the draft-adoption path alone.

---

## 8. Open questions for acceptance

1. **Materiality authority (RFC7-25).** The deterministic floor (reading
   order, section set, anchor targets, manifesto/thesis sections always
   material) is common to all three options and is not in question. What is
   in question is who classifies a **wording-only** edit. Three options:
   - **(a) Owner classifies every candidate.** Strictest; adds owner touches
     on every recomposition.
   - **(b) Asymmetric declaration — ◀ the drafted position.** The authoring
     party may declare a wording-only change **material**, never
     **immaterial**; only the owner or a contest's resolution classifies a
     change immaterial, and an undeclared edit's classification stays open
     rather than defaulting to immaterial. Chosen because the author is
     frequently an agent and VIS-4 states that classification is never made
     by the agent performing the change. This is a **reviewer suggestion
     adopted as the drafted position**, not the original draft.
   - **(c) Author self-declares** (the originally drafted rule): wording-only
     edits are material only if author-declared or contested. Cheapest;
     leaves the review decision with the party that has the incentive to
     avoid review.

   Confirm (b), or select (a) or (c)?

   > **ANSWERED at acceptance — B6.** **Asymmetric.** The authoring party may declare a change **material**, never **immaterial**; only the owner rules something immaterial. Escalation is free and self-service; de-escalation requires the owner.
2. **Primary-narrative cardinality (RFC7-6).** Proposed: one primary plus
   optional named narratives. The stricter alternative — exactly one, period
   — forecloses audience-specific accounts at zero present cost. Confirm the
   permissive default?
3. **The editorial-draft surface state (Integration defect 1).** Amend
   RFC2-25's sibling-state list with `editorial-draft`, or direct reuse of
   `unadopted-draft` with a qualifier? Proposed: the distinct state — the two
   await different acts and confer different end states, and folding them
   leaks a governance-artifact connotation onto presentation prose.

   > **ANSWERED at acceptance — B10.** `editorial-draft` is **minted** as a third sibling surface state in RFC2-25, on this RFC's own reported distinction. Downstream enumerations in RFC 0006 amended from two to three.
4. **Rejected-draft retention (RFC7-22).** Proposed: discard on rejection,
   the rejection recorded on the Trajectory queue item. The alternative —
   retaining rejected drafts as inference records — aids audit of generator
   quality at the cost of accumulating non-citable prose someone may quote
   anyway. Confirm discard?
5. **Presentation-profile scope (RFC7-5/RFC7-6).** *Authored position, not an
   owner ruling — surfaced because it makes a profile RFC1-7 defines as
   "never presumed present" effectively mandatory wherever Polaris renders.*
   Drafted: the presentation profile is **required for any governed project
   Polaris renders**, and on an undeclared or thin project the primary
   narrative may be thin or Syzygy-drafted-unadopted but never absent. It
   follows from the SDR §2 charter (a profile-less Polaris is the
   "disconnected specification browser" the charter excludes) and from
   RFC7-30's test entering at the primary narrative. The alternative the
   owner may rule instead: **Polaris declines to render a governed project
   that does not load the profile.** Confirm the drafted scope?

   > **ANSWERED at acceptance — A4.** The profile is **required**, and Polaris **drafts a default for owner sign-off** on first render rather than presuming one — the RFC2-24 reason #1 route. RFC1-7's "never presumed present" holds because nothing is presumed.
6. **The verbatim leaf under a proposed-scenario reading (RFC7-14).**
   *Authored position, previously unsurfaced.* Drafted: the leaf renders the
   **adopted** requirement/scenario text as operative, with the proposed
   delta **adjacent** and visibly/queryably distinct. The two alternatives
   are proposed text at the leaf (which manufactures the most quotable
   unadopted text in the system) and adopted text alone (which makes the
   proposed reading silently incomplete at its most exact altitude). Confirm
   adjacency?

   > **ANSWERED at acceptance — B5.** **Adopted text is the operative leaf; the proposed delta renders adjacent and visually distinct.** Rendering proposed text at the leaf would make the most quotable text in the system unadopted.
7. **The V0 disclosure enumeration (RFC7-13/RFC7-17).** *Authored V0 choice,
   previously taken silently.* The **obligations** are foundational — each
   altitude a self-sufficient honest read, every narrative reaching a
   verbatim leaf, each band in exactly one of three authority classes.
   Drafted as **V0 defaults, reversible without amending the obligations**:
   the five-altitude ordering (thesis → architecture → catalog → deep dive →
   verbatim leaf) and the three-band deep-dive composition. The alternative:
   freeze the enumeration as foundational, which forecloses RFC7-6's
   audience-specific narratives ordering their altitudes differently. Confirm
   the V0-default framing?

   > **ANSWERED at acceptance — B7.** Obligations per altitude and band are binding; the five-altitude / three-band counts are the **V0 default, not a frozen constraint**.

---

*End of RFC 0007. Clauses RFC7-1 … RFC7-38, plus sub-clause RFC7-11(a). The
clause range is closed: amend in place, add lettered sub-clauses, never
renumber.*
