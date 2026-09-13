# Generalized Polaris generator delivery

Working implementation proposal for the active owner goal, prepared against
`f4589e26aed9886a5776e5ac7a1c4fad4627fd26`. This is not an implementation
permission, adopted specification, provider consent or completion claim.
The candidate specification remains at
`openspec/changes/polaris-manifesto-generation/`. The practical authoring kit is
[docs/polaris-generation](../polaris-generation/README.md).

## Full completion target

An owner can select an admitted project and generation profile, start a bounded
LLM-assisted run, follow actual progress, read a coherent and beautiful manifesto,
inspect meaningful diagrams and optional deep dives, review independent findings,
request repair and regenerate after source changes. The same implementation,
prompts, validators and renderer must demonstrate this on two separately admitted
real projects. Project-specific inputs/configuration are expected; compiled
project names, hand-selected offsets and hand-fixed outputs are not the generator.

The CLI is a useful implementation and diagnosis seam, not a substitute for the
complete owner start/review experience. Synthetic providers and fixture projects
prove mechanics only. Human authorship/adoption and owner comprehension judgment
remain separate from model output and independent review.

## Architecture decisions proposed for review

| Boundary | Placement | Concrete responsibility |
|---|---|---|
| Project-neutral types and validation | `packages/polaris-generation-core/src/` | Immutable admitted-source, claim, argument, draft, asset and review records; closed versions; exact support; dependency invalidation |
| Pure run controller | Same core package | Bounded stage transitions, attempts, original deadlines, cancellation and effect uncertainty; no independent work queue |
| Existing Butlers adapter | `apps/three-surface-poc/src/polaris-generation/` | Convert an actually admitted PWB snapshot without changing its locator, policy, source tuples or exact-source behavior |
| General admitted-source adapter | Same app boundary | Resolve another registered project/profile through its own read/classification permissions into the same source-bundle contract |
| Effect adapters | Same app boundary | Provider dispatch, lifecycle join and immutable artifact persistence; permission and version checks immediately before effects |
| Bundle reading surface | Same app, shared rendering primitives | One bundle → human page and machine presentation; project-neutral vocabulary, trusted asset renderers, exact support routes and meaningful navigation |
| Owner controls | Polaris contextual authoring; Trajectory lifecycle | Start/resume/cancel/review/repair without manual record assembly or a competing queue; authenticated operations and explicit actual states |
| Versioned prompt assets | `docs/polaris-generation/prompts/` or its approved implementation home | Understanding, planning, authoring, editing, independent review and bounded repair, compiled from the reviewed kit |

The core never opens repository paths, executes project code or invokes a provider.
Adapters carry those effects and their admission evidence. Provider output cannot
add source IDs, tool capabilities, authority, identity kinds or effect routes.
The trusted authoring operation issues output identities; provider-local handles
are not accepted project identities. Source evidence, generated draft and adopted
presentation remain different objects/states.

Use existing `NarrativeRegistry`, Markdown safety, layout, source-route and
browser-verification patterns where their actual contracts fit. Do not feed
arbitrary projects through `buildButlersPocModel`, and do not use the compiled
`polaris-reading-plan.ts` representation as the generalized draft format.

Generated prose needs a project-neutral bundle renderer. Arbitrary relationships
need a data-only graph renderer beyond the current simple flow/relations forms;
unsupported graph types cannot count as successfully produced required visuals.
Geometry, grouping and arrows must preserve supported meaning and text equivalents.

## Delivery order, preserving the full goal

1. **Close the actual specification/implementation boundary.** Reconcile the
   existing candidate and applicable-consequence coverage with this architecture;
   resolve overlap with the adopted PWB/POC and inherited effect/lifecycle rules.
   Freeze independent review and the exact owner package. Existing contract prose
   and the authoring kit alone do not authorize new observable implementation.
2. **Implement the complete data path.** Source bundle → source-independent
   inventory/claim ledger → argument plan → structured assets → validation →
   rendered editorial preview. Exercise it through a thin operator seam and
   synthetic effect adapters while preserving the final owner-facing interfaces.
   This is a stage, not the completion threshold.
3. **Connect real bounded generation and the owner flow.** Supply the admitted
   provider adapter and persistent run/effect records; integrate start, progress,
   cancellation, resume, review and repair into the existing surface/lifecycle
   boundaries. The owner should not construct manifests or scheduler records by
   hand to generate a manifesto.
4. **Prove output quality and portability.** Run both admitted real projects with
   unchanged code/prompts, independently review the complete rendered pages,
   repair findings, then change source meaning and verify every affected asset
   and review is updated or invalidated. Retain actual provider and effect
   evidence without exposing source bodies or credentials in repository reports.
5. **Audit the objective.** Inspect every requirement and explicit acceptance
   item, not just passing tests. No fixture-only, source-only, one-project or
   opening-screenshot evidence may substitute for the full scope.

Implementation may be staged, but missing later stages remain open. A proposal,
accepted schema, successful response, reviewed Butlers page or finished work item
is not generalized-generator completion.

## Keep generation progress separate from worker liveness

[Inferred] The existing no-signal normalization finding is not inherently a
prerequisite to source preparation, generation, immutable stage receipts, preview,
review or repair. A recorded provider response proves a response was captured;
it is not qualifying VCS/PR progress under the worker-liveness contracts.

Preserve Trajectory's drafting lifecycle ownership. Do not create a separate queue,
relabel stage receipts as normalized work state, or invent an absence value. The
existing candidate requirements 028/029 and their work-state contract need an
explicit applicability disposition at the affected consumer seam. A future
claimed-worker projection with a bound but no qualifying signal cannot be called
conformant merely because the generation view works.

The review must decide whether a particular normalized-work consequence maps to
an approved existing requirement, needs generator implementation, or requires an
owner-bound N/A/amendment. This proposal makes no such binding judgment. Do not
make closing all worker-accounting extensions the admission condition for building
unrelated generation mechanics; equally, do not hide a genuinely applicable
contract gap behind a smaller product scope.

## Verification matrix

| Product obligation | Required direct evidence |
|---|---|
| Project-neutral generation | Same code, prompt, schema and renderer identities for two real projects; only admitted inputs/profile differ |
| Coherent manifesto | Frozen reader questions, independent full-source fidelity and cold-reader answers; project-specific argument rather than copied headings |
| Meaningful assets | Supported nodes and factual edges, complete material qualifications, useful placement, legible diagrams and linked mini deep dives |
| Input/output integrity | Counterexamples for missing/bad spans, changed digests, duplicate/dangling identities, invalid states/versions, active content and exceeded limits |
| Semantic fidelity | Omitted qualification and omitted-source cases rejected even when every produced claim has a syntactically valid citation |
| Bounded real effects | Admission refusal/withdrawal, malformed output, timeout, cancellation, interruption, uncertain dispatch and repair exhaustion at actual adapter seams |
| Usable owner flow | Actual start/progress/review/repair/return paths; narrow/wide and keyboard checks across introduction, middle and optional depth |
| Regeneration | A real meaning change updates dependent prose, diagram edges, glossary, deep dives and links; old reviews cannot certify new bytes |
| Existing PWB preservation | Independent source/tuple/route parity and source-admission probes for the unchanged Butlers adapter |
| Authorship distinction | Draft remains non-citable; independent review does not adopt it; human acts bind their exact subject and scope |
| Completion | Required clone/hosted checks plus requirement-by-requirement evidence audit; residuals explicitly remain incomplete |

## Inputs still needed for real proving runs

The proposed second project is Syzygy, subject to owner preference and its own
admission. The actual provider route/model and allowed project content classes
must be selected and recorded before effects. These choices do not prevent
closing the provider-neutral data and behavior design. They do prevent a real
project read or provider call without the corresponding effective permissions.
