# Generation progress and work state — candidate

Proposed detail for REQ-polaris-generation-028. It adopts no mapping or bound,
does not extend a closed vocabulary, and does not activate deferred fleet control.

## Show actual progress in its own field

Generation can report recorded facts such as request admitted, response captured,
draft persisted or review completed. Those are stage/receipt facts, not normalized
work states or proof that a worker is currently alive. A stale last-recorded stage
is identified as such; the UI cannot turn an old dispatch claim into a live
progress signal. Local cancellation remains the separately specified operation.

The normalized work value is derived per evaluation, not stored as editable
scheduler state or minted as a Claim. It uses the exact thirteen-value vocabulary:
future, planned, ready, active, blocked, review, merged, reconciled,
closed-unmerged, state-undetermined, eligibility-undetermined,
activity-undetermined and stale-or-dead. Raw substrate state remains qualified,
visible and queryable beside it, read from the tool's declared vocabulary rather
than a hardcoded client list. The effective, versioned normalization declaration
is a snapshot input under RFC2-1 item 7; a self-declared mapping grants no authority.

Each rendering, filter, count, export and machine answer carries separately
qualified normalized and chain fields, including normalized reconciled. The chain
keeps its existing six values. Normalized reconciled requires the underlying
reconciled@E verdict's tier and evaluation identity; it has no independent Claim
identity or observation-record membership. Missing verdict support cannot become
a positive state. State-local absence values never become claim Unknown reasons.

## Derive only from the named evaluation

Ready derives from that evaluation's captured work export and dependency feed,
not a live scheduler readiness command. New dispatch admission captures fresh
inputs into its own identified evaluation; it cannot change an older displayed
ready answer or reuse that answer as current effect authority.

The existing state predicates remain controlling:

- Future is approved/queued execution intent before materialization, with its
  sub-state and order. Unapproved drafts remain unadopted, and incompatible
  alternatives cannot be summed as parallel remaining work.
- Planned distinguishes deliberate freezing from unmet dependencies; missing
  eligibility inputs yield eligibility-undetermined with the missing input shown.
- Active requires claimed work and a permitted progress signal within an
  effectively declared bound. Review describes an exact-head review lane, not
  reviewer liveness.
- Blocked carries every derived cause from dependency, pr-wait, external and
  decision. Cause-Unknown appears only when no cause derives, never mixed into a
  nonempty set. Counts/filters/answers retain the set.
- Merged requires VCS merge evidence. Closure without it is closed-unmerged with
  the native reason or its explicit absence; neither is done or satisfied intent.
  Reconciliation remains separate, with absent V0 computation honestly Unknown.
- Unmapped native values remain state-undetermined with raw value and mapping
  route. Missing bounds and expired signals retain their specified absence cases;
  the generator does not widen those predicates itself.

Worker liveness uses only the qualifying branch-tip/commit/PR progress signals
under RFC4-23, with their actual instant and effective bound. Provider responses,
draft saves, coordinator heartbeats, locks and worktree presence are not substitute
signals. Between signals liveness is Unknown; an old signal shows stale-or-dead
and its real instant. Missing/ineffective bounds cannot make active renderable.

### Exact phase and consumer applicability

EXECUTION-PHASES.md distinguishes mechanics from live integration. Phase A creates
no live scheduler mutation, normalized-work consumer or provider effect. Phase B
must implement the paired fields for its drafting-work drawer, Trajectory work
rows, work filters/counts, work exports and machine work answers. Generation
stage receipts and narrative assets are not themselves work items.

A provider timeout or run budget is not a worker-liveness bound. Where the actual
admitted profile has no effective bound, the existing activity-undetermined
predicate applies; an effective bound cannot be silently omitted or replaced.
The bound-but-no-signal case still has no accepted fallback. If a selected live
profile requires that case, fail admission before materialization/dispatch and
expose the unsupported mapping/required-act route. No provider response or
fixture success closes that support gap. This permits staging pure mechanics
without pretending the entire live work projection is conformant.

## Capture history before the scheduler forgets it

Every scheduler-resident fact on which durable records depend must be captured
before the declared retention horizon. Effective quality policy declares both
the horizon and a maximum inter-pass interval tied to it. Capture remains within
ordinary human-triggered observations; this is not an autonomous polling mandate.
Missing/ineffective declarations leave dependent history claims Unknown under
no-currency-bound-declared mechanics. Missed capture and history loss stay visible,
with the retention event cited rather than a claim that no work existed.

Immutable history capture is not an editable copy of current scheduler fields.
Per-record substrate pins are supplementary, not the durability guarantee.
Historical telemetry comes from captured Execution Records; simulated telemetry
cannot fill missing fields. A compaction record identifies what was summarized,
discarded and remains externally queryable, and never changes claim meaning.

## Trace work without strengthening weak evidence

The warrant, approved Proposal, materialization, scheduler work, runs, change,
merge and reconciliation joins are traversable in both directions where consumed.
Every join preserves its recorded-identity or naming-convention basis and
appropriate reduced fidelity. Broken joins appear at the break with their actual
reason and downstream degradation, never guessed from similarity. A complete
but weak chain remains complete and weak; optional instrumentation is not a
missing-work verdict.

Reduced-fidelity facts carry one structured label with declared granularity,
unavailable granularity, the applicable RFC4-24 cause and an upgrade path. The
closed causes are post-merge-history-unreachable, replace-in-place-source,
retention-horizon-passed, derived-from-convention, approximated-boundary,
terminal-report-only and indistinguishable-runs. Finer-granularity questions
render Unknown rather than interpolate details; the coarser fact keeps its
otherwise-earned authority at its declared granularity. Fidelity causes are not
new claim Unknown reasons.


Unknown-provenance work remains visible, counted and separate from warranted
work; ingress does not reject it merely for that history. Orphaned work has its
own unfilterable Contradiction and owner-adjudication route, which cannot be
hidden behind the provenance label. Scheduler edits to a derived warrant pointer
are annotations; the authoritative pointer is reasserted at the next evaluation,
and the immutable materialization record is not rewritten.

Measures remain independent. Estimates/declared complexity are declared-only with
accuracy Unknown, not model inference. Derived-rate cost retains its Inferred
provenance, attempt counts come from records, overlapping blocked-cause intervals
are disclosed, and touched-component measures use the declared implementation
mapping. Missing measures remain Unknown and partial totals expose coverage.
Nothing here licenses a new liveness signal, live terminal streaming, unsupported
reconciliation computation or incidental mutation outside its own warrant.
