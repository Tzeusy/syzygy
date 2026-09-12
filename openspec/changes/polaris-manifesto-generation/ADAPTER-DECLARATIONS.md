# Generator adapters and execution evidence — candidate

Proposed declarations for REQ-polaris-generation-017/018. This document specifies
the registration contract; it registers no implementation or provider, grants no
effects, and supplies no fictitious implementation version or effective owner act.

## Reuse external authority; separate internal services

The interfaces below are responsibility boundaries, not a request to install a
second adapter for every existing source. RFC4-1 permits exactly one registered
adapter per project for each external authority. Generation delegates to that
adapter; replacement is an explicit registry event, never an alternate direct
network or shell route. Internal pure transforms and governance-plane writers
remain versioned components, not newly invented external authorities.

| Responsibility | Inputs and snapshot classes | Output and owner | Permitted effect boundary |
|---|---|---|---|
| Source acquisition | Admitted repository capture and declarations (RFC2-1 items 1/2), parser/classification versions and configuration (7/8), effective acts (11) | Source references, content-class outcomes and capture records through the existing source/VCS observer | Existing consented read surface only; generation cannot crawl a suggested path |
| Scheduler adapter | Captured work export/history (3), adapter/mapping versions (7/8), materialization and warranted intent (2/6), effective acts (11) | Capture-stamped external lifecycle and qualified aliases; scheduler remains authoritative | Existing explicitly authorized scheduler writes only, synchronous and attributed, followed by re-read |
| Provider execution route | Admitted source-bundle content, run/attempt identity, effective provider/profile policy (2/7/8/11), durable dispatch admission (6) | Captured response, actual/uncertain usage and dispatch evidence; generated prose remains editorial inference | One bounded request through the registered route, permitted cancellation and separately authorized receipt lookup; no implicit tool invocation or fallback provider |
| Admission evaluator | Identified source, registry, profile, consent and act records plus applicable policy/evaluation versions (2/7/8/11) | Deterministic permission evaluation, never a provider-supplied approval flag | Internal evaluation; no independent source acquisition, grant or provider effect |
| Run controller and capture observer | Execution-control facts and source receipts (6), schemas/policies (7/8), governing acts (11) | Subordinate run/attempt controls and immutable Execution Records in the governing work home | Conditional control writes described in INTERFACES.md; never an editable scheduler mirror or modification of a frozen record |
| Authored-artifact writer | Eligible bundle, expected predecessor, write consent, per-block act and schema versions (2/6/7/8/11) | Attributed intent artifact/version and atomic application receipt in their declared homes | Existing authorized governance-plane writes; any external VCS operation delegates to its registered adapter |
| Computed-visual resolver | Declared renderer/layout, identified shared-model evaluation and view configuration (7/8 plus that evaluation's complete input closure) | Existing governed renderer output, preserved under ASSET-CONTRACT.md | Internal reference resolution/rendering only; no new acquisition, subscription or provider route |

Numbers locate source classes, not a waiver of RFC2-1's complete input closure.
Additional report, runtime, challenge or prior-observation dependencies must be
identified whenever consumed. Local control records are necessary for the
generator's own operation; imported heartbeats, spans and phase telemetry remain
optional and cannot be required to admit another toolchain's run envelope.

## Required registration fields

Before output is admitted, each external observer/adapter and execution capture
observer resolves an effective per-project registry entry with these RFC4-2
declarations. An internal component's version is a snapshot input where it affects
evaluation; it does not acquire external write authority by being listed here.

| Declaration | Concrete required content |
|---|---|
| Identity | Stable opaque role identity and distinct implementation identity; project identity and external authority answered. Names, paths and provider aliases are descriptive locators. |
| Versions | Actual implementation version and supported per-adapter contract version; no invented value for an unreported provider revision. |
| Inputs | Enumerated source classes and their snapshot-input mapping, including policy/configuration/version dependencies. |
| Outputs | Enumerated fact/evidence classes and their identity schemes; run and attempt identity origins and collision handling. |
| Determinism | Each output classified as capture or derivation-deterministic. A deterministic transform consumes identified captures; it does not make generated project claims Observed or promise repeatable model output. |
| Failure mapping | Internal failure conditions mapped to applicable RFC2-23 degradation states, claim reasons and resolution routes; conditions outside that vocabulary disclosed separately. |
| Authority and writes | Exact typed question answered and exact permitted write surface, empty without explicit authority; effective act provenance evaluated under RFC3-16. |

Every emission carries source identity, capture instant, capturing observer
identity/version, scope and source-relocation provenance. Capture time remains
distinct from any source-reported time. Registry and implementation versions are
captured with the snapshot. An unregistered or ineffectively adopted entry admits
no deterministic fact; affected claims render Unknown rather than trusting the
entry's own adoption label. Every resulting fact carries the effective
registry act reference and its exact state-(1) or state-(2) provenance; state-(1)
remains visibly uncorrelated. Successful admission does not upgrade that state.

Upgrades and registry changes create new snapshots, never reinterpret historical
records. An older declared contract version leaves unsupported fields Unknown;
an undefined claimed contract version is inadmissible. Cross-version joins use
only identity schemes both versions declare identically. Substitution preserves
role identity and historical implementation identity/aliases; it does not migrate
old native aliases into a new provider or scheduler namespace.

## Failure behavior

| Condition | Degradation and visible consequence |
|---|---|
| Capture operation errors | Observer failed; last-good observation visibly stale/broken, affected new claims Unknown with source-uncaptured-or-unreachable; repair observer/source and capture anew |
| Declared source cannot be reached | Source unreachable; unavailable source and captured absence, dependent claims Unknown with source-uncaptured-or-unreachable; no stale permissive dispatch admission |
| Effective repository/provider consent withdrawn | Consent withdrawn; affected claims Unknown with unconsented-source-or-provider, inference overlay not computed, historical records immutable with withdrawal visible |
| Only part of required input scope captured | Partial snapshot; explicit captured/missing scope and Unknown remainder, never a full-scope aggregate |
| Secret match or unclassifiable content | Excluded content; counted exclusion, no derived content on any surface/endpoint, dependent claims Unknown with excluded-content |
| Missing cost/token quantity | Missing quantity; Unknown with reason, never zero; partial totals disclose known and total populations |

Absent consent refuses effects under the existing permission predicate without
inventing a withdrawal event. Budget exhaustion, rejected editorial output,
unsupported assets and uncertain dispatch are distinct execution/editorial facts,
not new degradation vocabulary. When such a condition affects a claim, the
existing claim-reason predicate chooses the applicable reason and resolution
route; the renderer does not guess one from a generic failure string.

## Run envelope, separate from stage artifacts

Each execution run has one immutable, integrity-verifiable Execution Record in
the governing work home. Stage artifacts reference it; they cannot replace it.
The envelope uses RFC4-19's existing Evidence class and field obligations:

| Field group | Obligation |
|---|---|
| Record identity and envelope schema version | Required; deterministic identity and declared schema |
| Capture metadata | Required; capturing observer/version, capture instant and source-artifact references |
| Project identity | Required; opaque governed identity |
| Run identity | Required; toolchain-emitted or deterministically adapter-derived, origin queryable |
| Work-item identity and qualified substrate alias | Required representation; unattributable execution remains visible as execution noise, never silently dropped |
| Terminal outcome and blocker set | Required; qualified verbatim reported vocabulary, or unknown-terminal with reason when the report is absent |
| Parent identity; warrant reference; start/end; runtime/model; branch/base; commits; PR/merge fact; gate outcomes/artifacts; tokens/cost; profile identity/version; policy-violation flags | Expected wherever available; otherwise explicit Unknown with reason. Root parent is explicitly null. No invented PR, branch, terminal report, clean-policy result or zero cost. |
| Worktree; screened summary/reason prose | Optional enrichment; machine-local paths never identity-bearing. Prompt/transcript bodies never enter the envelope; permitted hashes may. |

The grouped expected fields retain RFC4-19's individual semantics. In particular,
gate outcomes carry their evaluated tiers and need the required evidence and
provenance route; missing profile identity on a Syzygy-launched run cannot qualify
through the trusted-execution route. A reported profile violation terminates the
run and caps outputs at report-fact; unavailable violation evidence is Unknown,
not a clean result. Prose is screened under the observing project's policy.

Run identity collisions are disclosed as reduced-fidelity with cause
indistinguishable-runs and Unknown run count, never silently merged records.
Distinct dispatches are counted from records, not inferred from a scheduler
mutation trail. Missing warrant/profile evidence can leave historical execution
visible while preventing a new dispatch; admission strictness never erases history.

Usage and timing are captured source facts. Rate-table-derived cost is Inferred
with its rate/version and derivation. Partial aggregates expose their coverage;
independent measures never become a composite effort score. Execution instants
remain distinct from evaluation as-of time. Retention preserves the structured
history under REQ-011, without retaining rejected prose as an adoptable draft.
