# Vision

## What changes for the owner

In the owner's words: "I can work with my projects on any level of the
vision-spec-code hierarchy: open one place, understand what a project's vision
and goals are, tune or guide them if necessary, and know that the rest of the
project will (eventually) mold itself to fit around that goal. I end an
orchestration day knowing what was actually built and why — not with oversized
diffs, scattered completions, and no coherent account. I stop discovering
broken assumptions at deployment, and I stop commissioning ad-hoc deep-dive
audits every time a project's shape changes."

## Thesis

Syzygy (see README glossary) is a specification-driven software control plane:
an observatory (V0) and harness (proof-of-concept at V0, full at V1) that makes
a software portfolio's vision→spec→code hierarchy legible, truthful, and
navigable — for the owner and for the LLM agents that do the work. Three
states are kept semantically distinct: **desired state** lives in human-guided
doctrine and specifications; **observed implementation state** lives in code,
tests, CI, and runtime evidence; **execution state** lives in work-scheduler
records — and scheduled or completed work is never proof that the
implementation satisfies intent. Syzygy computes and shows the difference, and
harnesses the existing actuator toolchain to close it. **Showing the truth is
the soul of the product.**

## The human problem, and whose it is

The primary user is an owner running a portfolio of projects built largely by
agent fleets. The lived failures Syzygy exists to end: "I don't know what my
agents are doing" — a day of orchestration yields oversized diffs and scattered
completions with no coherent account; underspecification discovered at the most
expensive moment, after deployment; shape changes with no propagation mechanism
beyond manual deep-dive audits; learning a project via READMEs and ad-hoc
investigation, none of it comprehensive.

Syzygy is owner-first but open-source: it assumes the public actuator toolchain
(README glossary), never one private machine. It serves two first-class
consumers from day one: the owner (spatially, visually) and agents
(machine-queryable endpoints).

## What Syzygy is

- A **witness** (V0): an observatory over vision, specs, work, and code —
  trustworthy enough to believe when it says "Unknown."
- A **harness** (proof-of-concept at V0, full at V1; see v1.md): the surface
  from which the owner steers vision and triggers propagation — "specifications
  blooming into functional changes" (owner's phrase) through the existing
  toolchain.
- An **orthogonal plane**: governance artifacts living alongside each governed
  project, whose effects reach code only through scheduled work.

## What Syzygy is not

- **Not an issue tracker with a code browser.** The escape properties present
  from V0: observed truth is machine-consumable and actually consumed by the
  actuator toolchain, **and** V0 carries a working proof-of-concept of the
  vision on all three axes — intent, work, code — including one end-to-end
  propagation slice (v1.md).
- **Not a documentation portal.** Rendering and drafting governance artifacts
  is a means; the escape property is that intent changes produce dispatched
  work. A Syzygy from which no work is ever dispatched has failed, regardless
  of how good its documents look.
- **Not a replacement for its substrate.** The spec, work-scheduling, and
  orchestration tools remain the mechanisms; Syzygy integrates and harnesses
  them (architecture.md, "adapters").
- **Not an enforcement engine — outward.** It shows untruth in governed
  projects; it does not make it impossible, and gating others is secondary and
  cuttable. Inward it does enforce: the integrity of its own claims, authority
  boundaries, and write contract (VIS-4–VIS-7) is non-negotiable.
- **Not autonomous.** The loop is human-triggered; autonomy beyond VIS-4's
  stated bounds is licensed only through the mechanism VIS-4 names, never by
  reinterpretation.

## Non-negotiable rules

Rule identifiers are namespaced `VIS-n` (vision) and `SEC-n` (security.md) —
deliberately disjoint from the product lifecycle stages V0/V1 (v1.md), so a
rule citation can never be read as a release stage.

**VIS-1 — Comprehensible truth first; never comprehensible fiction.** The full
ordering, highest first: (1) truth and observation determinism; (2)
comprehension of the truth's presentation; (3) momentum (delivery speed); (4)
breadth of scope and fidelity of presentation; (5) reproducibility of derived
convenience (caches, incremental refresh, zero-token synchronization,
byte-identical inference output). Lower ranks are spent before higher ones;
rank 1 is never spent. Comprehension is achieved by simplifying
*presentation*, never *content*: an honest view may aggregate, defer, or
progressively disclose Unknowns, but may never substitute a confident state
for an Unknown one. *Honest simplification:* collapsing forty Unknown-status
modules into one region labeled "Unknown ×40." *Violation:* rendering that
region green because its neighbors are green — a view simplified until it
misrepresents.

**VIS-2 — No evidence means Unknown, not success.** No surface may declare a
project aligned, converged, or genome-complete — nor turn anything green —
without current evidence. Evidence is a durable, identified,
integrity-verifiable artifact (trust-and-evidence.md; reproducibility is a
declared property of an evidence class, not a prerequisite); aligned,
converged, and genome-complete are defined in architecture.md. Currency is
judged at a status evaluation's identified as-of instant (architecture.md) —
the wall clock never silently changes a displayed status. Until a claim class
declares its currency bound, its evidence is not current and the claim renders
Unknown. *Violation:* "spec-aligned ✓" computed from a stale index; a stale
view silently green; a status flipping with no new identified evaluation.

**VIS-3 — Human interpretability is a core tenet.** Every normative artifact —
spec, doctrine, contract — must remain digestible by a human unfamiliar with
the project. The test: fresh-reader review, run at adoption and on material
amendment, by a reader (human or agent) with no access to the authoring
context, who must be able to restate the artifact's intent and constraints
correctly; failure is recorded on the artifact's surface. Within the Syzygy
repository, a failing artifact freezes **autonomous adoption, not agent
authorship**: agents may draft repairs, but every amendment to the failing
artifact requires owner adoption until it passes a fresh-reader review.
In governed projects the failure is surfaced as status — whether to freeze is
the governed project's own policy (Syzygy does not enforce outward).
*Violation:* specs eroding, LLM-edit by LLM-edit, into something only LLMs can
parse.

**VIS-4 — Humans steer the vision; agents shape within it.** Shape-defining
deltas — heart-and-soul doctrine, craft-and-care standards, topology, and RFC
acceptance — require owner sign-off, every time; Syzygy and its agents may
draft them, never adopt them. Behavioral specs (`openspec/`) sit below that
line: LLM adoption of spec changes is permitted in principle, but opening that
gate is a **doctrine amendment event** — it requires both an accepted
adjudication RFC (defining what makes adversarial judgment independent, how the
ambiguity determination is recorded, and how each adopted change stays
individually revertable) *and* the owner's explicit doctrine amendment
recording that the gate opens; RFC acceptance alone never opens it. One class
is always human-gated, gate open or not: spec changes touching security
posture, privacy or retention obligations, or normative data contracts.
Classification of a change as spec-level or shape-level is contested by default
and is never made by the agent performing the change; it is settled without a
human only while the opened gate is in force. *Violation:* an agent sprouting
specs inside an ambiguous vision; an agent certifying its own governing vision
as unambiguous; an agent editing a spec to match code it just wrote; treating
RFC acceptance alone as opening the gate.

**VIS-5 — Syzygy never writes code; direct writes are confined to two
namespaces.** Syzygy's **direct project-content writes** touch only
`openspec/**` (in OpenSpec-compatible form — architecture.md, schema
ownership) and `.syzygy/**` (its native, schema-versioned namespace). No
governance manifest, configuration, or convention may extend that direct-write
universe. Syzygy may *read* declared implementation and evidence sources
anywhere; it may never directly create, modify, move, or delete project
content outside its two roots. Effects on every other authority —
version-control metadata such as commits and tags, configured work-scheduler
state, CI, runtime systems — occur only through **typed, explicitly
authorized adapters**, governed by each authority's own contract; those stores
are never Syzygy-owned content namespaces. Syzygy never writes the form or
function of implementation code. It may *generate* code-shaped proposals
(target schemas, migration plans, adapters) as governance artifacts, and it
may commit the **proposal artifact itself** into `.syzygy/**` (that is VIS-6's
commit-out, effected through the version-control adapter); it may never apply,
commit, or merge the proposal's *generated contents* into the implementation
code tree or any implementation branch — materialization is exclusively a
worker action against scheduled work. This rule governs attribution and
separation, not human control of code: the human gates on code change are
VIS-4's sign-offs and the worker toolchain's own review gates, which live
outside Syzygy's body and are not guaranteed here. *Violation:* Syzygy
committing a source-file edit to a governed repository; a direct write landing
outside `openspec/**` and `.syzygy/**`; a manifest purporting to extend the
write universe; an adapter effect without explicit authorization.

**VIS-6 — Syzygy is derived, with two closed exceptions.** Every fact Syzygy
holds must be rebuildable from the artifact that owns it; its databases and
views are projections, and content it authors is committed out to the governed
plane, which becomes the authoritative source. The exceptions, closed: (a) the
owner's **personal presentation state** (layouts, filters, bookmarks,
unpromoted notes), which may never affect truth, work, status, or
certificates — promoting a note into governance (an annotation or a dismissal)
commits it out to the governed plane, attributed and reasoned, dismissals
carrying an expiry (a dismissal without a reason current at the evaluation's
as-of instant renders the gap again — expiry acts only through a new
identified evaluation, architecture.md); (b) **observation records** —
historical evidence, immutable, evaluation-identified, marked stale, exempt
from rebuildability. *Violation:*
any other fact living only inside Syzygy; a view preference influencing a
status claim; a dismissal taking effect without living in the governed plane.

**VIS-7 — The observatory itself must be trustworthy.** The normative trust
floor lives in trust-and-evidence.md: the deterministic layer of an
observation record is identical across runs of one identified evaluation
(source snapshot + as-of instant, architecture.md); every rendered internal
project-entity link resolves to its identified target (the normative link
rule, exactly as stated in trust-and-evidence.md floor bullet 2); every
encoding means what its legend says; no secret material appears in any
surface or store. Release-blocking for Syzygy's own releases — Syzygy never
gates governed projects' releases. *Violation:* a dangling internal link; an
unfaithful heatmap; two runs of one identified evaluation disagreeing in the
deterministic layer.

## Performance

No performance target is constitutional; responsiveness is contractual (RFC and
spec material). Performance is never purchased with truth, determinism, or
completeness — the permitted currency is VIS-1's rank 4: breadth of scope and
fidelity of presentation, never below the comprehension constraint.
Performance may *narrow an explicitly declared scope*; it may never present
incomplete coverage as complete within that scope.

## The north star (honestly labeled)

The regeneration ideal — that a project's complete normative corpus (its
**Project Genome**, architecture.md) could regenerate the entire codebase, code
being a replaceable realization (with the marked-handcrafted carve-out,
architecture.md) — is the **north star, not present doctrine**. It exerts
direction: decisions should nudge projects toward it, and a decision that
materially forecloses it must record that foreclosure — the unrecorded
foreclosure is the violation. No artifact may claim the ideal as current
capability. The converse flow is equally legitimate today: deriving *candidate*
vision and shape drafts, work, and map surfaces from an existing codebase —
inferred intent becomes desired state only after owner adoption (VIS-4).
[Unknown] whether full regeneration is achievable; its biggest named risk is
spec completeness, especially adapting existing durable state without freezing
schemas into specs.

## Eventual mandate: live fleet observability

Syzygy is not complete until its owner can watch agent fleets work live —
deferred only because live monitoring is meaningless without the observed truth
it would annotate. Every roadmap must carry it as a named, sequenced item with
stated entry criteria; removing it, or leaving it unsequenced, violates
doctrine. It is governed by the same evidence classes as everything else:
streamed process output is Observed only when captured as a durable, identified
artifact; live views never contribute to status claims. Its escape property
from a terminal cockpit: every stream is anchored to the spec and work item
that motivated it.

## Success — and what failure would look like

Success means the observatory displaces the README-and-ad-hoc-investigation
ritual as the owner's instinctive first stop, and orchestration days end with a
coherent, evidence-linked account of what changed and why. By explicit owner
ruling, no single quantitative metric is constitutional: usefulness differs
between people and, for one person, between projects. The operational,
stage-labeled tests — each with a declared evidence artifact — live in v1.md.
Success tests are human judgments, recorded as such and never rendered
Observed; the owner re-judges them at each stage gate. And the thesis is
falsifiable: if, after sustained real use across the proving ground, the owner
still learns projects through the old ritual and still cannot account for
fleet days from Syzygy alone, the thesis — not the scope — is judged wrong and
reformulated.
