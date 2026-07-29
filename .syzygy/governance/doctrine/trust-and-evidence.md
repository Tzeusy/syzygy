# Trust and evidence

Domain doctrine for claims, evidence, warrants, and the deterministic/inferred
seam. This elaborates vision.md VIS-1, VIS-2, and VIS-7 and holds the **normative
statement of the trust floor**; craft-level review and testing standards live
in the project's quality policy (`.syzygy/governance/`).

## Evidence, and the two other warrants

**Evidence is a durable, identified, integrity-verifiable artifact carrying
its source, capture time, scope, and provenance** — a test run, a tool exit
status, a file hash, a commit SHA, an observation record, a captured runtime
trace or incident record. **Reproducibility is a separately declared property
of an evidence class, not a prerequisite for evidence status**: a one-off
runtime observation or anomalous external response, durably captured and
identified, is evidence. An LLM assertion is **Inferred, never Observed**,
regardless of confidence. Every claim class must declare its currency bound
(how old evidence may be and still count as current); currency is judged at a
status evaluation's identified as-of instant (architecture.md) — the wall
clock never silently alters a status outside a new identified evaluation.
Until a class declares a bound, its evidence is not current and its claims
render Unknown. Bound values are craft/RFC material; the obligation to
declare is not.

Two acts are authorized by warrants that are *not* evidence:

- **A recorded human decision** — attributed, timestamped, individually
  revertable. It may suppress a gap, rendered as *dismissed by human decision*
  — never as resolved, aligned, or green — and takes effect only once committed
  out to the governed plane with a reason and an expiry (vision.md VIS-6).
- **A work warrant** — creating or prioritizing work requires traceable
  authority (an approved requirement, a confirmed finding, a declared policy,
  or an explicit owner decision), not empirical evidence. Status describes;
  warrant authorizes. A claim that both declares status and spawns work must
  satisfy both gates.

## Status claims vs narrative claims

**Certificate and status claims** — evidence is mandatory for anything that
turns a badge or indicator green; declares alignment, convergence, or
genome-completeness; affects a certificate *(certificates are post-V1; this
trigger is future-tagged until their RFC exists)*; or claims a gap is
**factually resolved or absent**. No evidence means **Unknown**, not success.
A claim that meets any of these triggers is a status claim **whatever its
prose form** — a narrative sentence doing a green badge's work is judged as a
badge.

**A gap leaves a surface in exactly two ways, and they are not
interchangeable.** *Factual resolution or absence* — the claim that the gap is
closed, or never existed — is a status claim and requires evidence. *Policy
dismissal or suppression* — a decision not to act on a real or asserted gap —
is warranted only by the recorded human decision above: it claims nothing
about the facts, always renders as **dismissed by decision** with its reason
and expiry visible, and is never rendered green, resolved, or aligned
(vision.md VIS-6).

**Narrative and exploratory claims** — must be labeled Observed, Inferred, or
Unknown, and the labels are exclusive: **Observed** — a deterministic claim
carrying a resolvable evidence link; **Inferred** — the output of a declared
inference process, carrying its inference provenance; **Unknown** — a claim
that is neither evidence-backed Observed nor valid Inferred, including one
whose evidence is missing, inaccessible, or stale. **Missing evidence never
renders a claim Inferred** — absence of evidence does not make a claim
probabilistic; it makes it Unknown. That boundary is mechanical; link density
beyond it is a quality-policy matter (`.syzygy/governance/`). Inferences may
blend into explanatory narrative, but never rendered indistinguishably from
deterministic fact.

## The deterministic/inferred seam

Deterministic facts and probabilistic inferences are computed and stored in
distinct layers. **An observation record contains deterministic facts only**;
the inferred layer is a separate artifact recording the model, version, and
inputs that produced it, carrying its own declared reproducibility standard,
excluded from the VIS-7 identity test (architecture.md).

**Inference holds no positive status authority — it holds challenge authority
only.** Inferred evidence is excluded from evidence that establishes, raises,
or independently satisfies a positive status claim; it never establishes
alignment, convergence, or genome-completeness. It may act as a **challenge**: the
universal default is conservative suspension — an open inferred challenge
suspends the displayed claim to Unknown, rendered with its inferred provenance
visible alongside the deterministic evidence it questions, until a human or a
declared deterministic policy resolves it. An inference never silently
overrides or replaces deterministic evidence: the suspended claim's
deterministic basis stays visible, and resolving the challenge is what
restores or revises the status. **Admissibility:** a challenge must identify
one exact claim, state a specific falsifiable concern, carry its inference
provenance, and be individually resolvable; mere model uncertainty is not a
challenge. Detailed admissibility criteria are RFC material.

Rendering may blend the layers, provided provenance is
available at the point of consumption (hover, query, API field) and inferred
structure remains visually distinct from observed structure — a speculated
future component must never look like an existing one.

## Staleness

An **observation record** (the immutable result of an identified status
evaluation — source snapshot + as-of instant, architecture.md) may still be
displayed after its evaluation is superseded, but its staleness must be
visible on the primary surface, not buried in drill-down; it cannot contribute
to a current convergence certificate *(future-tagged, post-V1)*; and it cannot
silently remain green. Staleness itself is judged at the current evaluation's
as-of instant, never by an ambient wall clock. Broken observers degrade to
their last-good observation record, clearly marked stale/broken; they never
fail invisibly.

## The trust floor (normative statement)

The observatory forfeits its reason to exist the moment it presents false
information. The floor, **release-blocking for Syzygy's own releases** (Syzygy
never gates governed projects' releases — vision.md, "Not an enforcement
engine"):

- the deterministic layer of an observation record is identical across runs
  of one identified evaluation — source snapshot + as-of instant
  (architecture.md identity test);
- every rendered **internal project-entity link** — code, requirement, work
  item, capability, evidence, decision, and map entity — resolves to its
  identified target; external URLs are explicitly classified as external and
  may be unavailable without falsifying the internal project graph (this is
  the normative link rule; vision.md VIS-7 cites it);
- every visual encoding means exactly what its legend says;
- no credential or secret material appears in any surface, store, or endpoint
  (security.md SEC-5).

Changes to Syzygy that break this floor, or that present inference as fact,
are rejectable regardless of whether they otherwise work.
