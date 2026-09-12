# Artifacts and generation tools

Candidate handoff conventions, not a registered runtime schema or implemented
API. Use the [run contract](README.md) and [authoring prompts](AUTHORING.md).
The example is intentionally small; a production interchange must additionally
satisfy the adopted narrative, provenance, security and lifecycle contracts.

## Per-stage envelope

A request identifies `runId`, `stageId`, `attempt`, project, audience, frozen
input bundle, allowed source/claim/asset IDs, prompt version, accepted output
kind/version, authorized provider route, tool allowlist and explicit budgets.
The source bundle includes revision/evaluation identities, source digests,
source spans, claim states, exclusions and unresolved inputs. Authorization is
verified outside the LLM; putting a grant-shaped string in JSON grants nothing.

A result repeats its request/input identities and returns `complete`, `partial`,
`failed` or `cancelled`, produced artifact references/digests, usage, unresolved
items and concise findings. Unknown fields must not become executable extensions.
A malformed result is a failed attempt, not an empty successful bundle.

These are stage outcomes, not project-health or adoption states. Record actual
provider/model metadata and outcome only when an authorized call occurred; a
synthetic handoff carries neither a fabricated provider response nor a paid-run
success record. [example.json](example.json) illustrates this distinction.

## The artifact set

| Artifact | Required content | Consumer |
|---|---|---|
| Source bundle | Project/snapshot/evaluation identity; admitted source IDs and digests; source references; exclusions and conflicts | Understanding pass; validators |
| Claim ledger | Claim ID; statement; supporting spans; evidence state; intended meaning; qualifications; conflicting/unknown inputs | Every authoring pass and fidelity reviewer |
| Argument plan | Audience/questions; section order and purpose; claim IDs; requested asset/deep-dive dispositions | Author; independent coverage reviewer |
| Draft bundle | Identified prose/list blocks; claim IDs; editorial-draft state; asset references and reading order | Trusted renderer and reviewers |
| Diagram asset | Reader question; named nodes; typed/directed edges; support for each factual node/edge; qualifications; legend; structured text equivalent; placement | Trusted diagram renderer |
| Deep-dive asset | Parent identity; focused question; supported explanation; relationships and limits; return/evidence links; disposition | Optional reader route |
| Review record | Frozen subject/input digests; criteria; independent reviewer identity; actual methods/viewports/paths; findings and unresolved checks | Repair; human review |
| Run manifest | Stage/attempt identities, tool/prompt/model versions, artifact hashes, outcomes, dependencies and invalidated reviews | Recovery and audit |

Contents are derived from existing section/asset identities. Glossary entries
are shared by inline definitions and glossary routes. Tables contain real
comparisons with supported cells and explicit missing values. Every requested
asset has a produced, unnecessary-with-reason or unresolved disposition; reviewers
check omissions against the source inventory, not just the generated output.

Keep bundles and their manifests immutable once reviewed. A repair produces new
artifact versions and invalidates affected reviews. Do not cache away a changed
qualification, hidden broken edge, failed stage or withdrawn source permission.
Narrative, diagrams, glossary and optional depth consume the same claim ledger.

## Tools available today

[Observed] The POC has the following primitives. They are not a complete generator.

| Existing surface | Actual capability and current limit |
|---|---|
| `polaris-reading.ts`: `applyReadingPlan` | Validates digest-bound excerpt/figure/chapter selectors; drift falls back to the complete declaration. It cannot synthesize new prose or infer a plan. |
| `polaris-markdown.ts`: `renderPolarisMarkdown` | Renders admitted bounded Markdown and explicit data-only flow/relationship forms. Unsupported diagrams remain literal text. It is not a general graph-layout engine. |
| `polaris.ts`: `renderProjectReading` and `renderPolarisPage` | Render existing reading/model types with source links, navigation and figures. They do not ingest the proposed draft-bundle format above. |
| POC body-read/observation pipeline | Acquires the currently configured consented source class. It is not a general repository crawler or permission grant for another project. |
| Narrative, parity, reading and browser tests | Validate existing helper/model behavior. Passing them does not establish generated-prose quality or cross-project generality. |

From a clean Syzygy checkout with its dependencies installed, these existing
commands can inspect the example and exercise the current primitives:

```sh
python3 -m json.tool docs/polaris-generation/example.json
npx vitest run apps/three-surface-poc/src/polaris-reading.test.ts apps/three-surface-poc/src/polaris-markdown.test.ts
npx vitest run apps/three-surface-poc/src/polaris-accessibility.browser.test.ts
```

JSON parsing proves syntax only. The tests use fixtures and the current POC
interfaces; none of these commands generates a manifesto from the example.
The existing `poc:fresh-checkout-demo` requires the configured repository's actual
read gates and remains a separate live proving-case check.

## Tool interfaces to build for the vertical slice

These names describe proposed operations, **not commands that exist**. Implement
and admit them through the applicable specification/implementation gates.

| Operation | Input → output | Boundary |
|---|---|---|
| Prepare sources | Admitted snapshot and project adapter → bounded source bundle | No ambient crawling or policy bypass; exclusions remain visible |
| Run authoring pass | Validated stage envelope → structured draft result and usage | Provider/content admission before dispatch; explicit bounds, cancellation and checkpoints |
| Validate bundle | Frozen bundle, source ledger and output contract → identified structural/fidelity failures | Check IDs, span/digest integrity, coverage, state, edge support and references; return per-predicate failures |
| Render preview | Validated draft bundle → local human page and corresponding machine presentation | Trusted renderers own markup/styles; no provider HTML or implicit network requests |
| Inspect reading | Frozen preview and reader criteria → layout/navigation evidence and independent findings | Test full page, disclosure/return routes, keyboard, mobile and source access |
| Revise bundle | Findings and prior artifacts → bounded replacements and invalidation manifest | Preserve prior evidence; review is not automatic adoption |

Deliver these as one usable slice before adding a generalized scheduler or a new
queue. Reuse the existing authorized lifecycle where applicable. The first slice
should let an operator follow a source-backed draft from input through preview
and repair; it must not require manually editing application code to make the
second project render.

## Validation and failure exercise

Before relying on a predicate, exercise a counterexample: remove a source span,
change a source digest, introduce a dangling deep-dive link, add an unsupported
edge, hide a material qualifier, insert active content, exceed the output budget,
and interrupt a pass. Confirm the corresponding explicit failure or partial
outcome. Do not count a crash before validation as a successful rejection test.

Mechanical validation cannot establish that a conclusion follows from its cited
source or that a page reads well. Retain independent fidelity and actual-reader
reviews alongside structural results. The portability and changed-source recipe
in [README](README.md) is the completion test for the broader generator.
