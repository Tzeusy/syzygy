# Semantic delta POLARIS-DLAM-1 — Polaris dossier local-agent mode

> **Candidate — binds nothing.** A proposal in the form of
> `contracts/candidates/policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`. An agent
> drafted it; adoption belongs to the owner.

**Artifact(s):**         `openspec/changes/polaris-dossier-local-agent-mode/proposed/polaris-generation/spec.md` (new); no existing file is edited
**Stable IDs affected:**  REQ-polaris-generation-033, 034, 035 and 036 (new). For a run in the operator-agent mode only, named text of REQ-polaris-generation-005, 006, 017, 018, 030 and 031 and of the base change's `INTERFACES.md` is displaced or read as quoted under "Current meaning"; no byte of any is edited. REQ-polaris-generation-001's draft-layer consent sentence and RFC7-20 are read against and not displaced (owner question O1). Relied on, unchanged: REQ-polaris-generation-004, 012, 019, 020 and 025; RFC2-24, RFC4-2, RFC4-19, RFC7-2, RFC7-9, RFC7-10, RFC7-19, RFC7-25. No RFC, doctrine or adopted byte is edited.
**Change class:**         Normative
**Author:**               lane-spec drafting agent (Claude Opus 5.5)
**Date:**                 2026-10-05

## Current meaning

Quoted by script from the effective files: the base spec
`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`,
the overlay `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`
(REQ-polaris-generation-006, 030 and 031 are effective there), the base
change's `INTERFACES.md`, and RFC-0007. Each block is the whole sentence,
scenario, bullet, paragraph or clause it names; none is an excerpt of a
sentence.

**REQ-polaris-generation-001 (base), the draft-layer consent sentence — not displaced, put to the owner as O1:**

> For absent or withdrawn provider consent, the draft layer SHALL render Unknown (`unconsented-source-or-provider`) as a policy state in both channels, including when a prior draft remains retained.

**REQ-polaris-generation-005 (base), first sentence — displaced in the operator-agent mode:**

> A generation request SHALL identify positive finite limits for provider calls, input/output volume, charged usage and elapsed time, plus a finite nonnegative repair-cycle limit before dispatch.

**REQ-polaris-generation-005 (base), scenario — "records actual usage" read as stated:**

> #### Scenario: Invalid output or exhausted budget
>
> - **WHEN** a stage returns malformed output, fails, times out or reaches an admitted limit
> - **THEN** the run stops further disallowed work, records actual usage and exposes the incomplete stage
> - **AND** the candidate does not become ready or replace a valid presentation

**REQ-polaris-generation-017 (base), the adapter-route sentence — displaced as it applies to a provider operation:**

> External authorities SHALL be accessed through their single registered adapter per project, never a competing direct route.

**REQ-polaris-generation-017 (base), scenario — displaced as it applies to a provider operation:**

> #### Scenario: Interface tries to bypass its adapter
>
> - **WHEN** a generation stage requests a direct source, scheduler or provider operation outside its registered route and effective write surface
> - **THEN** the operation is refused without performing the external effect
> - **AND** naming an internal service as an adapter does not confer that authority

**REQ-polaris-generation-018 (base), the usage sentence — "Captured usage" never captured in this mode:**

> Captured usage/timing SHALL remain distinguishable from rate-table-derived Inferred cost, with derivation and rate version retained.

**REQ-polaris-generation-018 (base), scenario — its "final usage receipt" never exists in this mode:**

> #### Scenario: Interrupted run lacks optional evidence
>
> - **WHEN** a run has no terminal report, final usage receipt, branch, PR or fine-grained telemetry
> - **THEN** its envelope preserves the required representations including unknown-terminal and explicit reasons for unavailable expected fields
> - **AND** optional telemetry absence does not reject or degrade that envelope, and missing usage is not zero

**REQ-polaris-generation-006 (overlay, effective text) — read as REQ-polaris-generation-035 states:**

> Fidelity review SHALL use an independently prepared, frozen inventory of material source claims, qualifications, conflicts and trade-offs, covering the entire admitted source population.

**REQ-polaris-generation-006 (overlay, effective text) — read as REQ-polaris-generation-035 states:**

> The bounded workflow SHALL prepare or validate the independent inventory and questions from admitted sources, accounting for those calls in its run budget; it SHALL NOT require the owner to hand-author project-specific editorial preparation before starting.

**REQ-polaris-generation-006 (overlay, effective text) — read as REQ-polaris-generation-035 states:**

> Reviewers SHALL receive the artifact, governing references and acceptance criteria without the authoring conversation.

**REQ-polaris-generation-030 (overlay), the exposure sentence — its "inspected and selected material" item becomes two populations:**

> Before claiming source coverage it SHALL expose the selected project boundary and audience, admitted source classes, supported languages/source forms/repository shapes and scale bounds, inspected and selected material, and reasons relevant material is excluded, unavailable, unresolved or deferred by budget.

**REQ-polaris-generation-031 (overlay), opening sentence — "the owner" as the person asked becomes the run's operator:**

> After investigation within admitted bounds, the generator SHALL present the smallest useful prioritized group of unresolved questions material to the requested account, identifying evidence considered and the draft consequence of each answer.

**REQ-polaris-generation-031 (overlay), the owner-presentation clause — read with the operator as the person asked:**

> It SHALL offer supported interpretations where available, free-text correction and an explicit leave-unknown or defer path.

**`INTERFACES.md` (base change), the Provider bullet — no provider adapter exists in this mode:**

> - **Provider:** Accept a reserved attempt identity, admitted content and hard
>   request/output bounds. Return screened-candidate input plus usage/dispatch
>   receipts. Tool/function requests in output are not executed. A provider without
>   a usable bound or permission cannot be selected silently as a fallback.

**`INTERFACES.md`, "Budget and retry decisions", first paragraph — read as the operator-declared limits:**

> Each run supplies positive finite `maxCalls`, `maxInputBytes`, `maxOutputBytes`,
> `maxUsageUnits` and `maxElapsedMs`, plus finite nonnegative `maxRepairCycles`,
> with a versioned accounting
> unit/policy reference. There is no implicit unlimited value or agent-selected
> spending default. The UI can prefill an effective owner-approved preset and
> show its bounds before start; ordinary runs do not require re-entering technical
> limits or re-granting still-effective consent. The policy maps provider limits to worst-case reservations;
> unbounded or unknown required accounting refuses that provider dispatch.

**RFC7-20, whole (`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`) — not displaced; an accepted contract this change cannot amend:**

> **RFC7-20 — The draft state.** Generated prose appears **only** in the
> explicit **editorial-draft** state: machine-marked with its inference
> provenance (model, version, inputs — RFC2-7's overlay discipline), visually
> distinct, non-visually recoverable (RFC7-33/34), and **non-citable**: never an
> anchor target (RFC7-10), never in the citation graph, never satisfying a
> claim, never green. `editorial-draft` is a **named RFC2-25 sibling surface
> state** — the third, alongside `dismissed-by-decision` and `unadopted-draft` —
> minted on this RFC's reported distinction *(owner decision B10)*: an
> `unadopted-draft` awaits an adoption gate into *authority*; an
> `editorial-draft` awaits a human authorship act into a *non-authoritative*
> artifact and stays non-citable even after adoption. Computing a draft is
> inference: absent SEC-2 named-provider consent it is **not computed** — the
> draft layer renders Unknown (`unconsented-source-or-provider`), visibly a
> policy state; the curated skeleton, referenced authority, and deterministic
> derived layer must carry a fully readable surface without it.

The common reading of all of these today: Syzygy calls the model, through a
registered route, under limits it enforces and receipts it captures, with an
inventory and reviews it dispatches, and a discovery account it produces from
reads it makes. Someone who runs the model outside Syzygy and hands Syzygy a
draft does not comply with 005, 017 or 018 as written, and 006, 030 and 031
cannot be shown met.

## Proposed meaning

Four added requirements. Their statements are quoted whole below, by script;
their scenarios and verification forms are in the artifact.

**REQ-polaris-generation-033 — Operator-agent authoring mode (new), statement, whole:**

> A generation run SHALL record exactly one authoring mode, `provider` or `operator-agent`, before any draft is admitted, and the mode SHALL NOT change within the run. In the operator-agent mode the draft, the independent inventory and the reviews are authored by coding-agent sessions that the human operator runs with the operator's own tools and account over a local clone of the subject, and Syzygy SHALL make no model-provider call for the run, resolve no provider route and transmit no project content to any service. The agent sessions' transmissions to their own provider are the operator's own act under the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05`: they are outside Syzygy's egress consent, no egress record is made for them, and Syzygy SHALL NOT present them as consented by, routed through or observed by Syzygy. The operator-agent mode SHALL be selected only for a subject that the admitted project input (REQ-polaris-generation-001) records as an observed repository that is not a governed project; a governed subject, and a subject whose project input does not say which it is, SHALL NOT be run in this mode.
>
> Before it issues a brief, Syzygy SHALL verify that the clone's checked-out HEAD commit equals a revision that the in-force observation consent for the repository names, and SHALL record that commit as the run's pinned revision. A HEAD that differs from a named revision, a revision the consent does not name, or an absent, withdrawn or ineffective observation consent, observer registry entry, classification policy act or screening policy act SHALL refuse the run with its reason in human and machine form. Every read Syzygy makes for the run SHALL be a Git object read by object identifier at the pinned revision through the registered observer, never a read of the working tree, and every object SHALL be classified and screened under the observing project's effective policies (REQ-polaris-generation-025) before its content is used in a check or rendered. Syzygy SHALL execute no observed code. The brief SHALL instruct the agent not to build, install or run code from the clone; Syzygy cannot observe whether the agent complied, and the run record SHALL say so.
>
> The run configuration SHALL declare, before the brief is issued, the operator, the agent tool and its version, the agent's model provider, and positive finite limits: a wall-clock deadline, at least one of a token budget or a turn budget for the agent sessions, a finite nonnegative repair-cycle limit and a finite clarification-question limit. A configuration that lacks any of these, or that states an unlimited or non-positive value, SHALL be refused; there is no default. Syzygy SHALL record each declared value as operator-declared. Syzygy SHALL enforce the limits that bind its own steps: it SHALL refuse a check or review check beyond the repair-cycle limit and any step after the deadline, measured on its own clock from the issue of the brief, and SHALL record the instants of its own steps as Observed. Syzygy cannot observe or enforce the agent sessions' usage. Agent usage SHALL be recorded only as the figure the operator declares, labelled Inferred and attributed to the operator, and where no figure is declared the run record SHALL say that the usage was not recorded and that Syzygy cannot observe it; it SHALL NOT be presented as Observed, as a provider receipt, or as zero.
>
> The run record and every rendered page SHALL disclose, in human and machine form: the authoring mode; the agent tool, its version and its provider, as operator-declared; that the agent read the clone without restriction; that the agent's account of what it read is self-reported and Inferred; that Syzygy made no provider call; the pinned revision; and that every rendered quotation was verified by Syzygy against the Git objects at that revision.
>
> For a run in the operator-agent mode this requirement displaces exactly this predecessor text, quoted in the semantic delta: in REQ-polaris-generation-005, the sentence "A generation request SHALL identify positive finite limits for provider calls, input/output volume, charged usage and elapsed time, plus a finite nonnegative repair-cycle limit before dispatch.", replaced by the declared limits above, and in its scenario "Invalid output or exhausted budget" the words "records actual usage", read as the Observed instants of Syzygy's steps and the operator-declared usage; in REQ-polaris-generation-017, the clause "External authorities SHALL be accessed through their single registered adapter per project, never a competing direct route" and the scenario "Interface tries to bypass its adapter", as they apply to a provider operation, because the run has no provider route and Syzygy makes no provider operation (both continue to apply to Syzygy's Git object reads); and in REQ-polaris-generation-018, the "final usage receipt" of the scenario "Interrupted run lacks optional evidence" and the "Captured usage" of the sentence on usage and cost, which in this mode are never captured and are replaced by the operator-declared figure above. The Provider bullet and the "Budget and retry decisions" section of the base change's `INTERFACES.md` are read the same way: there is no provider adapter, and the operator, never the agent, declares the limits. The draft-layer consent sentence of REQ-polaris-generation-001 and the consent condition of RFC7-20 are not displaced; how they read for a draft that the operator's own session computed is owner question O1. The draft layer of an operator-agent run SHALL render in the editorial-draft state only while an effective owner ruling holds that this consent condition is met for such a draft, and the run record SHALL cite that ruling; without one, or after its withdrawal, the draft layer SHALL render Unknown (`unconsented-source-or-provider`) as REQ-polaris-generation-001 requires, while the source pages of blobs Syzygy read and screened, and the disclosures, remain readable. Every other sentence and scenario of REQ-polaris-generation-001, 005, 017, 018 and 025 is unchanged, including the egress check for every transmission Syzygy itself makes, the screening of every ingest, and the rule that prompt and transcript bodies do not enter the Execution Record.

**REQ-polaris-generation-034 — Agent brief and mechanically checked draft (new), statement, whole:**

> In the operator-agent mode Syzygy SHALL issue a versioned brief bound to the run and its pinned revision. The brief SHALL state: the reader topics the owner set for a dossier, which are core ideas, end-to-end workflows, mechanisms, maintainer-stated advantages and trade-offs; the labelling rules; the quotation rule; the clarification rule of REQ-polaris-generation-036; the run's declared limits; and the structured draft schema with its version. The brief SHALL carry no project content beyond the repository identity and the pinned revision.
>
> The labelling rules are: every claim block carries exactly one label, Inferred or Unknown, or is marked non-normative (RFC7-2 (b)); an Unknown block names its reason; an agent SHALL NOT label its own claim Observed; and Observed is reserved for a quotation that Syzygy has verified. The quotation rule is: a quotation is one contiguous span of one cited file at the pinned revision, without elision, joining or alteration other than the normalisation stated below. Every claim block SHALL cite at least one source as a repository path and an inclusive line range at the pinned revision, and every quotation SHALL name the citation it is taken from.
>
> Syzygy SHALL check each submitted draft and SHALL report every failure as a repair finding that names the block, the citation, the kind of failure and the location to repair. The checks are:
>
> - the draft validates against its declared schema version, with unique identities and resolving internal references (REQ-polaris-generation-019);
> - every cited path names a blob at the pinned revision, and every cited line range lies within that blob;
> - every quotation, after the normalisation that the generator's existing quote check applies to both the quotation and the source, is one contiguous run of the cited blob's text, beginning and ending on word boundaries, that lies within the cited line range, and Syzygy records the span's byte range in the blob; that normalisation drops comment leaders at line starts and a closing comment marker at a line end, keeps only the text of markdown links and images, decodes character entities, removes markdown backslash escapes, drops backticks, drops paired emphasis marks at word edges, straightens curly quotes, turns an ellipsis character into three full stops, and collapses each whitespace run to one space; an ellipsis in a quotation that the source does not carry is an elision and fails;
> - every label is one the labelling rules permit and every Unknown block names a reason from RFC2-24's closed list.
>
> A blob that classification or screening excludes SHALL NOT be used to verify a quotation: the quotation is unverifiable, the block that relies on it SHALL render Unknown with `excluded-content` instead of the quotation, and its exclusion is not a repair finding. A repair finding SHALL carry no excluded bytes. Each resubmission is a new draft revision with its own identity; it counts against the repair-cycle limit, and it retires earlier check results and dependent review evidence (REQ-polaris-generation-006). A draft with an unresolved finding SHALL NOT proceed to review or become ready.
>
> Syzygy SHALL render a checked draft through the existing multi-page dossier renderer. Every rendered quotation SHALL be the span Syzygy read from the blob at the recorded byte range, never the agent's copy of it. A source page SHALL be rendered only for a blob that Syzygy read at the pinned revision and that screening admitted. Each anchor SHALL take RFC7-10's form, with the blob's object identifier as the target identifier, the byte range as the fragment and the pinned revision as the target state; the repository path is shown beside it as a label. Generated prose SHALL render in the editorial-draft state (RFC7-20). Rendering obligations of REQ-polaris-generation-004 and 012, and of REQ-polaris-generation-032 where it is adopted and applies, are unchanged.

**REQ-polaris-generation-035 — Fresh-context review in the operator-agent mode (new), statement, whole:**

> In the operator-agent mode the independent inventory and the fidelity and rendered-design reviews that REQ-polaris-generation-006 requires SHALL each be produced in an agent context separate from the authoring context. The inventory context SHALL start from Syzygy's inventory brief and SHALL NOT be given the draft; Syzygy SHALL check its quotations and citations as REQ-polaris-generation-034 checks a draft, and SHALL freeze it before the fidelity review. For each review Syzygy SHALL emit a review packet containing only the frozen subject (the draft, or the rendered pages for the rendered-design review), the frozen inventory, the cited spans as Syzygy read them, the governing criteria and the verdict schema; the packet SHALL NOT contain the brief's authoring exchange, any transcript or the agent's read account. The review context SHALL write a structured verdict that names the packet's digest and records inventory-to-draft coverage for every inventory entry, draft-to-source support for every claim block, and every finding with its severity and its deficient subject (discovery, understanding, clarification, argument, prose, asset or rendering).
>
> Syzygy SHALL validate the verdict before it counts: its schema; that the packet digest equals the packet for the current frozen subject; that every inventory entry and every claim block has an entry; that every quotation the verdict relies on verifies as in REQ-polaris-generation-034; and that a verdict with an unresolved blocking finding does not declare the subject ready. A verdict that fails validation SHALL be recorded and SHALL NOT count as a review. Any revision of the subject or the inventory retires the verdicts bound to it.
>
> The run record SHALL record, as operator-declared, the agent tool, version and session identifier of the authoring, inventory and review contexts, and Syzygy SHALL refuse a verdict whose declared session identifier equals that of the authoring context or of the inventory context it reviews. The record SHALL distinguish what Syzygy observed, which is the packet's exact contents and the verdict's binding to it, from what remains Inferred, which is that each context was fresh, that the review context saw nothing beyond its packet, that the inventory context did not see the draft, the session identifiers themselves, and the inventory's completeness over the clone. The review page SHALL disclose that distinction.
>
> For a run in the operator-agent mode this requirement reads REQ-polaris-generation-006 as follows, and displaces only what it names: "Reviewers SHALL receive the artifact, governing references and acceptance criteria without the authoring conversation" is met by the packet rule above; the inventory "covering the entire admitted source population" is the inventory context's self-reported coverage of the clone at the pinned revision, labelled Inferred, and readiness SHALL NOT claim that coverage as verified; and the words "accounting for those calls in its run budget" read as the operator-declared limits of REQ-polaris-generation-033, which cover the inventory and review contexts. Every other sentence and scenario of REQ-polaris-generation-006, including the rule that unresolved material omissions prevent readiness, the fresh-reader review of RFC7-25 and the rule that the generator does not classify its own wording change as immaterial, is unchanged.

**REQ-polaris-generation-036 — Self-reported discovery and in-session clarification (new), statement, whole:**

> In the operator-agent mode the discovery account that REQ-polaris-generation-030 requires SHALL consist of two populations, kept distinct in human and machine form. The first is the agent's account of what it inspected and selected, with its reasons for material it excluded, could not resolve or deferred, and its stopping reason; Syzygy SHALL record and render it as self-reported and labelled Inferred, and SHALL NOT present it as complete, as verified, or as Observed. Syzygy SHALL report as findings the self-reported paths that name no blob at the pinned revision; a path that does exist does not make the account Observed. The second population is the set of Git objects Syzygy itself read for the run, each with its path, object identifier, pinned revision and classification and screening outcome, labelled Observed. Syzygy SHALL NOT derive an Observed not-read figure or an Observed coverage claim from the agent's account. REQ-polaris-generation-030's obligations on scope, supported profile, stopping reason, partial findings and narrower scopes apply to the agent's account as self-reported content.
>
> The consequential questions of REQ-polaris-generation-031 SHALL be asked of the human operator within the agent session. The draft SHALL record each question with the evidence considered, the consequence for the draft, the interpretations offered, and the operator's answer as free text, a selected interpretation, leave-unknown or defer, attributed to the operator. Because Syzygy does not observe the exchange, the record SHALL be labelled as the agent's report of it. The number of questions SHALL NOT exceed the declared clarification-question limit of REQ-polaris-generation-033. Every other obligation of REQ-polaris-generation-031 is unchanged: an answer does not prove implementation behavior or adopt intent, unchanged questions reuse prior answers, a purpose left unknown stays unknown, and answer changes invalidate dependent content and reviews.
>
> For a run in the operator-agent mode this requirement displaces exactly this predecessor text: in REQ-polaris-generation-030, the item "inspected and selected material" in the list the generator "SHALL expose" before claiming source coverage, read there as an account the generator itself produced, which becomes the two populations above; and in REQ-polaris-generation-031, "owner" as the person asked, which becomes the human operator of the run, whose answers are attributed to the operator. Every other sentence and scenario of REQ-polaris-generation-030 and 031 is unchanged.

In plain terms: a run declares its mode. In the operator-agent mode the
displaced text above is replaced as each requirement's last paragraph says,
and every other sentence of the predecessor requirements still binds. In the
provider mode nothing changes.

## What explicitly does NOT change

- **Every byte** of the base spec, the overlay, `INTERFACES.md` and every other
  file of both adopted changes. The displacement is per run mode, by a new
  requirement, as the profile change (032) displaces text of 004.
- **The provider mode.** Every predecessor requirement and scenario binds a
  provider-mode run with its full meaning. The mode is parked by the owner's
  direction, not withdrawn.
- **Syzygy's own reads.** Observation consent, the observer registry entry
  and the classification and screening policy acts apply to every Git object
  Syzygy reads (REQ-polaris-generation-025; direction item 3).
- **Syzygy's own transmissions.** REQ-polaris-generation-025's single egress
  check still governs every transmission Syzygy makes; in this mode it makes
  none.
- **REQ-polaris-generation-001's draft-layer consent sentence and RFC7-20.**
  Not displaced. Until the owner rules on O1, the operator-agent draft layer
  renders Unknown (`unconsented-source-or-provider`).
- **REQ-polaris-generation-006's readiness rule, materiality floor and
  fresh-reader review (RFC7-25).** An unresolved material omission still
  prevents readiness; the generator still never classifies its own wording
  change as immaterial.
- **REQ-polaris-generation-018's envelope.** Required field groups, the
  exclusion of prompt and transcript bodies, "missing usage is not zero",
  identity-collision handling.
- **REQ-polaris-generation-030's honesty obligations.** Scope, profile,
  stopping reason, partial findings, narrower scopes; they apply to the
  agent's account as self-reported content.
- **REQ-polaris-generation-031's authority rules.** An answer proves no
  implementation and adopts no intent; unchanged questions reuse answers;
  answer changes invalidate dependants.
- **REQ-polaris-generation-020.** Start preparation, materialization and
  work reuse are not displaced; whether a local run materializes a work item
  is an implementation-planning question against 020's unchanged text
  (`design.md`).
- **RFC2-24's closed Unknown reasons.** No reason is minted; unobserved agent
  usage is disclosed as a fact of the render.
- **Doctrine.** SEC-2 is read, not changed (direction, "What this direction
  does not do"). SEC-3 binds Syzygy's execution, and Syzygy executes no
  observed code; the agent's conduct in the clone is disclosed as unobserved.

## Warrant

The owner direction `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05`
recorded in `POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md` in the decisions home (it lands by PR #351 and is not on `main` at this change's base),
items 1 to 5. Item 5: "The affected requirements are amended through one
reviewed CC-REV-2 delta, which binds only on the owner's sign-off."

## Evidence or decision basis

- The direction above, with the owner's words and three selections quoted
  there.
- The adopted text quoted under "Current meaning".
- [Observed] The existing code each check reuses, named in `design.md`; the
  consent reader is PR #263, open and not on `main` at
  `ac35c998ec3f7b20c47adc19b22ac540f851b099`.
- [Inferred] The capabilities of Claude Code and Codex (local file reading,
  in-session questions, separate sessions) from general knowledge; no target
  repository content was read in drafting.

## Terms introduced / retired

- **Authoring mode** (`provider` | `operator-agent`): introduced, scoped to
  `polaris-generation` run records. Not a kernel term.
- **Operator-agent mode**: the mode in which the operator's own coding-agent
  sessions author the draft, inventory and reviews.
- **Pinned revision**: the clone's HEAD commit, verified against the
  observation consent and recorded by `init`.
- **Review packet**: the exact bundle Syzygy emits to a review context, bound
  by digest.
- **Operator-declared**: a value Syzygy records on the operator's statement
  and cannot observe; rendered Inferred and attributed.

None retires an existing term. Whether any belongs in `PROCESS-GLOSSARY.md`
is left to review.

## Downstream impact

See `IMPACT-LEDGER.md`: method, regexes, denominators and every citer
classified.

## Migration / supersession plan

- Nothing is superseded. On adoption, in one logical change (CC-REV-2):
  move the spec from `proposed/` to `specs/`, generalize the effective-scenario
  recount, recount `PROJECT-STATUS.md`, regenerate `DIRECTIVE-REGISTER.md`
  and a generated dependency union (`tasks.md`).
- The live presentation docs that describe dossier generation as a provider
  run (`docs/polaris-generation/README.md`, `TARGETS.md`,
  `REDIS-DOSSIER-GAP-ANALYSIS.md`, `REDIS-SITTING-RUNBOOK.md`) gain the
  operator-agent route in the same adoption change; they are not authority
  and are not edited before it.
- No digest-bound artifact is touched, so no manifest regeneration is due. The
  sibling candidates that patch the overlay (`polaris-edit-repair-deletion-scenario`
  appends to REQ-polaris-generation-006) leave every fragment quoted here
  intact; this was checked against its patch, not assumed.

## Review

**Required class:**  Full review per CC-REV-1 (Normative).
**Reviewer:**        Dispatched by the lead; must not have authored this change or shared its session.
**Verdict:**         None yet.
