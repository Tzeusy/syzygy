# Generator design — candidate

This document is a proposed design, not an accepted topology, implementation
plan or grant of effect authority. The specification owns observable behavior.

## Context

The current renderer provides useful presentation primitives but takes a
Butlers-specific model and two compiled reading selections. Reuse requires a
project-neutral generation boundary and a lifecycle that can produce and review
new assets. Existing RFC7 profile, editorial-draft, authorship and queue rules
remain controlling. The practical product and authoring guidance is recorded in
`docs/polaris-generation/README.md`. The current implementation proposal is
`docs/design/POLARIS-GENERATOR-DELIVERY.md`.

## Goals / Non-Goals

**Goals:** One reusable generation path, meaningful project-specific synthesis,
truthful reading depths, bounded execution/recovery, beautiful accessible assets,
source drift handling, preservation of human authorship and inspectable evidence.

**Non-Goals:** A new authority tier, a second work queue, automatic project or
provider consent, autonomous adoption, implementation-code writes, or release.
Synthetic providers prove mechanics only; real synthesis and reader evidence
remain required for the full product outcome.

## Decisions

### Separate acquisition, inference and presentation

Source acquisition evaluates the applicable project permission and classification
rules. The generator consumes only the admitted snapshot and cannot crawl more
files from a model suggestion. A request for additional information is returned
as a bounded finding with the needed source class; it does not widen admission.

The engine accepts a project-neutral bundle consisting of opaque project and
snapshot identities, source references, their captured claims/states, declared
concepts and exclusions. No caller-supplied `approved` flag is trusted. The
admission adapter's evaluated result is checked at dispatch and reuse boundaries.
A presentation profile is a separate input state; a missing or declined profile
follows RFC7-5 rather than being silently constructed as adopted.

The output is a versioned editorial asset bundle: Narrative, Sections, claim
blocks, reading order, source anchors, typed supporting assets, generation provenance
and review references. Identifiers follow the existing opaque identity discipline;
labels and source paths are locators, not identity. The proposed record fields, effect boundaries, budget/retry and retention
decisions are specified in INTERFACES.md. Their schema and adapter registrations
must pass the contract-coverage review before sign-off. ASSET-CONTRACT.md specifies
project-specific composition and the distinct editorial/computed visual boundary;
required unsupported assets cannot silently disappear.

### One authoritative lifecycle

The runner records progress against the authoritative drafting work item, with
an execution identity and immutable stage input/output references. It does not
own an independent queue or store authored narrative under work. Polaris renders
contextual draft review and authorship; Trajectory renders execution lifecycle.
Trajectory owns that presentation relative to Polaris; after materialization the
scheduler owns current work lifecycle. Both surfaces re-read it at the answering
evaluation. Typed generation-control records own only stage, reservation,
dispatch and finalization facts, never a mutable copy of scheduler-owned fields.
The materialization join stays immutable; missing joins follow RFC8-8's orphaned
work finding and owner-adjudication path.

Execution progress and editorial state remain separate. A completed model stage
can yield an invalid draft. A confirmed draft can still be awaiting a profile or
human authorship act. A valid owner act is a warrant, not empirical comprehension
or release evidence.

Stage progression is admission → independent inventory/question preparation →
source understanding → narrative design →
drafting → independent fidelity review → actual rendered design review → bounded
repair or ready-for-owner. This is execution detail, not a new kernel epistemic
vocabulary. Failed, cancelled and uncertain effects are recorded explicitly; no
state proceeds because a file exists or a provider returned HTTP success.

### Explicit bounds and recovery

A run requires finite positive dispatch/content/usage/time limits before dispatch
and a finite nonnegative repair-cycle limit. The admitted policy names their
values; zero repair cycles means a failed review stops rather than repairs.
Dispatch reserves the relevant remaining budget using the provider's available
bounded request limits. A provider whose required usage cannot be bounded cannot
be silently used under that policy. Actual receipts reconcile reservations and
remain visible, including charges arriving after cancellation.

A checkpoint binds project/snapshot, admission context, generation policy,
provider/model/version, stage inputs and artifact digests. Resume re-evaluates
permissions and verifies those bindings. It reuses completed valid stages; it
cannot transfer old review evidence to edited content. The lifecycle adapter reserves budget and exclusive dispatch ownership durably
before a provider effect. A possibly completed effect remains reserved and
uncertain; it is not automatically redispatched. INTERFACES.md defines the
reservation and authored-write commitment/receipt-recovery boundaries.
Scheduler admission uses a fresh, identified observation for each dispatch.
Local cancellation and the durable dispatch-admission transition are serialized;
external scheduler changes are observed rather than included in that transaction.
An already admitted attempt may be in flight, including the uncertain pre-send
crash window. Later observed withdrawal stops further admissions and
readiness and not-yet-committed finalization without rewriting an actual effect
as stopped. Ready and authored-write commitment each recheck scheduler eligibility. The full
protocol and its separate consent predicate are in INTERFACES.md.
Duplicate request identities map to the same authoritative execution record;
different identities cannot overwrite artifacts.

### Preserve authored presentation

Regeneration always produces a separate editorial candidate. It does not replace
human-curated composition merely because source content or a model improved.
Source drift remains visible on the existing narrative; the new candidate carries
new input identity and needs its own applicable reviews and per-block authorship
act. Finalization is conditionally committed against cancellation/rejection before
any authored write. Atomic writes compare the expected predecessor, record an
application receipt with the version, and surface conflicts; acknowledgment loss
is reconciled without replaying the write or replacing later human edits.
Individual reversals preserve attribution. Authored narrative remains in the
repository's intent home and survives offboarding.

Rejected drafts leave Polaris reading, search and adoption surfaces entirely.
The work item records rejection. Permitted execution evidence is not an ambient
copy of adoptable prose. Generated projections obey an explicit retention policy;
curated composition is not disposable cache data. Export requires its own allowed
content/destination and cannot imply publication or adoption.

### Treat editorial quality as an outcome

The synthesis task must explain the project's distinctive argument, not merely
extract headings or fit source text into a fixed template. Supporting material
must preserve qualifications and opposing choices. Founder-like voice is an
account of supported motives; generated quotations or invented biography fail.

Review takes the actual full default reading, supporting depths, source material
and desktop/mobile captures. It records whether readers can restate the thesis,
motives, promises, limits and capability relationships, find exact intent and
identify an honest Unknown. Visual review evaluates hierarchy, pace, terminology,
contents, reference dominance, navigation and responsive composition. Human
judgment is recorded as such; a numeric score does not manufacture it.

`DESIGN-ACCEPTANCE.md` makes the owner's manifesto expectation concrete for
independent evaluation: purpose-first reading, coherent argument, concise prose,
deliberate full-page composition, useful contents and terminology, unobtrusive
evidence access, and accessible navigation. It includes the reported interface
failures as blocking counterexamples. This is candidate review guidance, not
evidence that the generated experience already passes.

## Coexistence and applicability

These requirements add a generation workflow. They do not replace adopted PWB
behavior. For Butlers, the following existing requirements remain controlling:

| Existing requirement | Preserved obligation | New generator relationship |
|---|---|---|
| PWB-REQ-005 | Evaluated repository/content-class authority | Generator admission cannot bypass it |
| PWB-REQ-010/011 | Whole-project account, complete catalogs and exact-source depths | Generated candidate adds prose/structure without losing any required population or route |
| PWB-REQ-014 | Typed revision-bound minimal anchors, closed target classes, non-citable narrative | Generator asset representation must satisfy the full existing contract |
| PWB-REQ-015 | Capability authority bands and verbatim normative leaf | New draft prose cannot substitute for current intent |
| PWB-REQ-016 | Keyboard/nonvisual comprehension | Generated assets enter the same accessibility obligations |
| PWB-REQ-020 | Complete human/machine tuple parity | Both generated presentation and deterministic facts preserve their distinct identities/states |
| PWB-REQ-021/022 | Existing walkthrough population and effective judgment predicate | New product validation is additional; it does not replace or auto-pass the existing walkthrough |

The generic engine must not force other projects into Butlers' categories or
compiled source hashes. Their applicable adopted profiles/specifications govern
project-specific population and exact-intent obligations. If integration needs to
change any PWB behavior above, that becomes an explicit amendment; it cannot be
hidden under the declaration that no existing capability is modified.

## Risks / Trade-offs

- A provider seam with synthetic fixtures makes mechanics testable but cannot
  prove editorial intelligence. Two authorized real projects and changed-source
  regeneration remain completion evidence.
- Free-form generation is expressive but difficult to audit; structured blocks
  and minimal anchors enable challenge without equating citation presence with
  factual support.
- Automatic replacement is convenient but would erase authorship. Separate
  candidates and explicit acts preserve attribution and reversibility.
- A shared visual system promotes reuse but must allow meaningful project-specific
  composition. Identical shells with swapped names are not the target outcome.
- The new schema, retention policy, adapter registrations and full applicable
  contract coverage remain sign-off work. This initial design makes no claim that
  those gates have already passed.

### Protected effect host

EFFECT-HOST-DESIGN.md selects a separate local origin/process and a narrow
protected recorder for the generator. Existing PWB routes and tokens remain a
separate compatibility surface; they do not authorize generator operations.
Real host provisioning and project/provider/write effects still need their
concrete permissions. This is a product-specific effect boundary, not a new
portfolio identity or scheduling platform.
