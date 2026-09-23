# Polaris generation core

Pure deterministic generation primitives. No source acquisition, permission
service, provider dispatch, filesystem writes or owner acts live here.

`encodeCanonicalJson(value, limits)` defines `polaris-json-v1`: compact JSON,
UTF-16-sorted object keys, original array order and ECMAScript JSON primitive
spelling. The output uses UTF-8 for size and digest accounting, without Unicode
normalization. Negative zero encodes as zero. Lone surrogates are JSON escapes.
This is a local versioned encoding, not a claim of RFC 8785 conformance.

Every call supplies positive safe-integer byte and node limits and a depth limit
from 0 through 256. Root depth is zero; every value occurrence counts as a node.
Shared objects count at each occurrence. Cycles, sparse arrays, non-finite numbers,
non-JSON primitives, proxies, custom prototypes, accessors, symbol/hidden fields,
extra array fields and `__proto__`/`constructor`/`prototype` object keys are refused.
Plain and null-prototype data objects are supported. Diagnostics contain only
bounded error codes, never input values or keys.

`digestCanonicalJson` hashes those exact bytes using SHA-256 and returns the
encoding and algorithm alongside the digest. It performs no I/O. Canonical shape
validation does not validate a generator schema, resolve an identity, establish
source fidelity or authorize any effect. Callers must first use a bounded parser
that rejects duplicate keys; duplicate keys cannot be recovered from an already
parsed JavaScript object. Schema validation remains a separate obligation.

## Editorial pipeline

`runGenerationPipeline` now connects independent inventory → argument plan →
authoring → editing → fidelity review, with bounded repair and fresh review.
`promptForStage` and `stageSchema` supply versioned recipes and concrete
provider-local response contracts. The serialized input binds both prompt and
schema bytes. `parseBoundedJson` refuses duplicate keys, malformed responses and
byte/depth/node overflow before stage validation. `validateStage` checks closed
fields, source references, requested section identities, diagram endpoints and
review population declarations. These checks cannot establish semantic truth.
`GenerationSource` binds each countable source to repository, revision, Git
object and evaluation identities. Only a body-backed, validated byte span
can be quoted; path-only, excluded and unavailable rows remain in the
denominator. Preview citations derive from validated anchors, so reordering
sources cannot renumber them. The PWB model is projected by an app adapter
without re-reading its released source bodies.
The operator supplies `requestedAssets` with stable IDs, kinds and requiredness;
the pipeline rejects malformed requests before dispatch. Validators join those
requests and positive review references to the same draft and admitted inputs.

The controller requires explicit source-verification, lifecycle/admission,
provider, validation and receipt adapters. It has no default network client.
Requests name six stage routes, and receipts retain the route and reported
model for each attempt. Fidelity and repair envelopes omit the author plan;
after inventory, only source spans cited by the stage input travel in an
envelope. The private scripted adapter persists exclusive reservations and
validated checkpoints outside a governed tree. Completed stages are reused
only under matching input, route, permission and artifact bindings. In-flight
and uncertain attempts remain reserved; neither a missing receipt nor an
expired lease permits replay. This is not a live effect host.
Real adapters must atomically bind immutable request inputs, enforce cumulative
reservations across restarts and concurrent callers, and re-evaluate authority.
A stalled adapter is bounded by cancellation/deadline; a late admission or lost
receipt remains conservatively reserved in its owning adapter, never permission
to replay. Durable late receipt capture belongs to the adapter; the in-process
callback supplements it and cannot survive a process crash.

Successful source review returns `awaiting-rendered-review`, never ready/adopted.
Stopped runs expose previously validated stage artifacts and content-free reasons;
invalid provider bodies are not returned. A validator and a declared complete
review denominator are mechanical evidence, not proof of model quality.

Run the controlled end-to-end example from the repository root:

```sh
npm ci
npm run poc:generator-demo -- --out /tmp/polaris-generator-demo-new
```

If dependencies are absent, the demo stops with an `npm ci` instruction before
attempting a build.

This kit grants no source access, provider egress, authorship adoption or
release. A real provider requires recorded per-project, provider and content
consent under SEC-2; the synthetic command below makes no provider call.

Use a fresh directory. The command creates two synthetic project previews, a
changed-source variant, structured draft files and stage receipts. Responses and
admission are scripted, explicitly synthetic adapters. No real source or model
provider is accessed. Open the generated HTML to inspect supported diagrams,
source references and optional depth. This intermediate preview is not the
primary Polaris publication surface or the full authored asset schema.

Still required: live admitted source/provider/lifecycle adapters, protected effect
host, full authored bundle and owner workflow, independent real-source and rendered
quality judgments, and unchanged-engine proof on two real admitted projects.
