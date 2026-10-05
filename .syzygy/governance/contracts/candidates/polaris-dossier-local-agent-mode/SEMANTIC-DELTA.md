# Semantic delta POLARIS-DLAM-1 — Polaris dossier local-agent mode

> **Candidate — binds nothing.** A proposal in the form of
> `contracts/candidates/policy-candidates/SEMANTIC-DELTA-TEMPLATE.md`. An agent
> drafted it; adoption belongs to the owner.

**Artifact(s):**         `openspec/changes/polaris-dossier-local-agent-mode/proposed/polaris-generation/spec.md` (new); no existing file is edited
**Stable IDs affected:**  REQ-polaris-generation-033, 034, 035 and 036 (new). For a run in the operator-agent mode only, named text of REQ-polaris-generation-001, 002, 005, 006, 017, 018, 020, 021, 022, 030 and 031 and of the base change's `INTERFACES.md`, `OWNER-FLOW.md` and `SECURITY-CONTRACT.md` is displaced or read as quoted or named under "Current meaning"; no byte of any is edited. SEC-1's CLI-client bullet is read, not edited. RFC7-20 is affected by the owner's reading (`POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`, item 1), not by an edit; both reviews' finding that the reading changes the clause's effect is preserved below for the owner, not resolved. SEC-3 is not edited here; the execution permission depends on the SEC-3 amendment drafted as doctrine amendment D9, not yet adopted (`POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-2026-10-05`, item 1), and 033 and 034 carry D9's draft conditions. Relied on, unchanged: REQ-polaris-generation-003, 004, 012, 019 and 025; RFC2-24, RFC4-2, RFC4-19, RFC7-2, RFC7-9, RFC7-10, RFC7-19, RFC7-25. No RFC, doctrine or adopted byte is edited.
**Change class:**         Normative
**Author:**               lane-spec drafting agent (Claude Opus 5.5)
**Date:**                 2026-10-05

## Current meaning

Quoted by script from the effective files: the base spec
`openspec/changes/polaris-manifesto-generation/specs/polaris-generation/spec.md`,
the overlay `openspec/changes/polaris-manifesto-understanding-amendment/specs/polaris-generation/spec.md`
(REQ-polaris-generation-002, 006, 030 and 031 are effective there), the base
change's `INTERFACES.md`, and RFC-0007. Each block is the whole sentence,
scenario, bullet, paragraph or clause it names; none is an excerpt of a
sentence.

**REQ-polaris-generation-001 (base), the draft-layer consent sentence — read for an operator-computed draft under the owner's reading of RFC7-20 (rulings direction, item 1):**

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

**REQ-polaris-generation-005 (base), scenario — "with their actual inputs and outputs" read as 033 states:**

> #### Scenario: Inspectable successful run
>
> - **WHEN** a bounded run produces a candidate asset
> - **THEN** its record identifies source understanding, narrative construction, fidelity review, rendered design review and any repairs with their actual inputs and outputs
> - **AND** the owner can distinguish work completed from reviews still required

**REQ-polaris-generation-018 (base), first sentence — the Execution Record's home and integrity read as 033 states:**

> Each execution run SHALL retain one immutable, identified, integrity-verifiable Execution Record in its governing work home as execution-plane Evidence, never proof of desired-state satisfaction.

**REQ-polaris-generation-020 (base), statement, whole — its Proposal, approval, scheduler-creation and materialization gates read as 033 states for a run that makes no provider dispatch and no scheduler effect:**

> The owner SHALL be able to request generation or regeneration from project context without manually assembling governance or scheduler records. The application SHALL resolve the project's declared governance root and authorized work/artifact homes rather than infer write locations from an observed source path, showing missing/conflicting prerequisites explicitly. It SHALL prepare a bounded effect plan from admitted metadata, owner selections and effective presets without provider calls or additional body reads to authorize its own start; persistence SHALL require effective write authority. Existing work SHALL be reused only when its actual warrant, immutable join, current scheduler eligibility, pinned intent and remaining authorized allowance cover the request. Ambiguous, exclusive or undeclared-compatible candidates SHALL NOT be silently selected or merged. Otherwise the application SHALL prepare the execution-intent Proposal and concrete missing-approval context; preparation or a generic Start action SHALL NOT confer approval, and children SHALL inherit approval only when the approving Decision explicitly permits it. Approval SHALL preserve Proposal identity. The application SHALL continue the same identified request once missing authority is effective without re-requesting unchanged approvals. Authorized scheduler creation SHALL use a stable operation identity and exclusive durable creation claim before the effect; duplicates SHALL return the same outcome or a conflict, and uncertain creation SHALL NOT be retried blindly. Only the written immutable materialization record binding Proposal, complete scheduler work-item identity set and pinned warranted intent revision SHALL transition authority to the scheduler. Before that record, the Proposal SHALL remain authoritative and provider dispatch SHALL be refused. An observed scheduler item without its record SHALL produce the unfilterable orphan Contradiction and Unknown/suspended conclusion even during attempted materialization; it SHALL NOT be silently filled in or deleted. Recovery SHALL follow owner adjudication and authorized re-materialization SHALL cite and supersede the finding. Ordinary editorial stages SHALL remain subordinate run metadata rather than requiring a new Proposal/work item for each model call. Existing dispatch, cancellation, retention, review and per-block authorship gates SHALL remain distinct from start-flow success.

**REQ-polaris-generation-022 (base), the trail-location sentence — unmeetable on a same-user host, read as 033 states (owner question in the packet):**

> The trail SHALL reside outside the governed plane and untrusted actor write reach; work records or a same-user writable directory SHALL NOT substitute.

**REQ-polaris-generation-022 (base), the credential sentence — relied on unchanged; 033 issues no credential for the run:**

> Credentials authenticating to Syzygy SHALL NOT be injectable into observed-project execution.

**REQ-polaris-generation-002 (overlay, effective text), the understanding sentence — read as met by the draft's self-reported understanding record (034):**

> Before drafting the central argument, the generator SHALL expose a reviewable understanding of supported purpose, beneficiary, proposition, capabilities, component responsibilities and relationships, choices and alternatives, trade-offs, limits, terminology, contradictory accounts and unanswered questions.

**REQ-polaris-generation-003 (base), the model-version sentence — relied on unchanged; 033 records the model as operator-declared and states that no provider-reported version exists:**

> Requested model identity and provider-reported version SHALL be distinguished; unavailable version information SHALL be explicit, not guessed.

**REQ-polaris-generation-006 (overlay, effective text), the verification sentence — accuracy verified against packet spans, completeness self-reported (035):**

> The fidelity reviewer SHALL verify inventory accuracy and completeness against the owning admitted sources rather than trusting preparation output.

**REQ-polaris-generation-030 (overlay), the discovery-gate sentence — read as binding Syzygy's reads (036):**

> The generator SHALL perform question-directed, bounded discovery for a selected project only after the applicable metadata-only start preparation, work/admission gates and effect permissions; investigation SHALL NOT read sources to authorize itself.

**REQ-polaris-generation-030 (overlay), the read-coverage sentence — read as binding Syzygy's reads; the agent's reads are the operator's own act (036):**

> Body, code, history and other content reads SHALL remain individually covered by applicable consent and classification; no shell or observed-project execution is implied.

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

**`SECURITY-CONTRACT.md` (base change), the trail-location paragraph — read with REQ-polaris-generation-022's trail sentence (033):**

> The trail resides outside the governed plane and outside the untrusted actor
> class's write reach. A work record, file in the repository, or owner-user-only
> directory writable by the same untrusted process is not that boundary. The
> chosen recorder/storage must demonstrate protection against those writers.
> Audit records contain no credential values, secrets or excluded bodies; rejected
> offending payloads use permitted digest provenance, never payload values.
> An unverifiable audit correlation cannot make an owner-act record effective.

The `OWNER-FLOW.md` sections "Resolve warranted work" and "Materialize once, then execute" describe the provider-mode start flow of REQ-polaris-generation-020 and are read with it, as 033 states; they are not quoted because 033 reads them whole, by heading.

**REQ-polaris-generation-021 (base), the principal sentence — read as 033 states: the `syzygy dossier` commands serve no route and are outside the route inventory; the recorded principal is the operator, credential identity Unknown:**

> Every authenticated generator act SHALL bind exactly one explicit principal and authorize its operation/project against that principal's scopes, separately from authentication.

**REQ-polaris-generation-021 (base), the machine-client sentence — read as 033 states: the commands hold no credential that authenticates to Syzygy:**

> Machine clients SHALL use their own explicitly scoped credentials issued only through an owner-attended trusted ceremony, never an owner's session, another machine credential's issuance or observed content.

**SEC-1 (`.syzygy/governance/doctrine/security.md`), the CLI-client bullet — not edited; 033 reads the local `syzygy dossier` program as no client of any Syzygy endpoint [Inferred, for the reviewer]:**

>   - **Non-browser agent and CLI clients are admitted only through an explicit
>     machine-client authentication mechanism** (an authentication-RFC matter).

**RFC4-19 (`.syzygy/governance/contracts/rfcs/RFC-0004/execution-record.md`), the work-item row — applied, not displaced: the run creates no work item and renders as unattributed execution:**

> | work item identity + substrate alias | R | Substrate-neutral identity primary; `bead_id` as alias (RFC4-6). Unattributable runs are admissible only rendered as unattributed execution noise, never dropped [Observed: vision.md anchoring mandate] |

**RFC7-20, whole (`.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`) — not edited; the owner reads its condition as governing drafts Syzygy computes (rulings direction, item 1):**

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
registered route, under limits it enforces and receipts it captures, from a
materialized work item, with an inventory and reviews it dispatches, a
producer understanding and a discovery account it produces from reads it
makes, and records held outside any untrusted actor's write reach. Someone
who runs the model outside Syzygy and hands Syzygy a draft does not comply
with 005, 017, 018, 020 or 022 as written, and 002, 006, 030 and 031 cannot
be shown met.

## Proposed meaning

Four added requirements. Their statements are quoted whole below, by script;
their scenarios and verification forms are in the artifact.

**REQ-polaris-generation-033 — Operator-agent authoring mode (new), statement, whole:**

> A generation run SHALL record exactly one authoring mode, `provider` or `operator-agent`, before any draft is admitted, and the mode SHALL NOT change within the run. In the operator-agent mode the draft, the independent inventory and the reviews are authored by coding-agent sessions that the human operator runs with the operator's own tools and account over a local clone of the subject, and Syzygy SHALL make no model-provider call for the run, resolve no provider route and transmit no project content to any service. The agent sessions' transmissions to their own provider are the operator's own act under the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05`: they are outside Syzygy's egress consent, no egress record is made for them, and Syzygy SHALL NOT present them as consented by, routed through or observed by Syzygy.
>
> Under the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`, item 1, and the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-2026-10-05`, item 2, the operator-agent mode MAY be used on any repository for which the required consents are in force, governed projects included; SEC-2 is unchanged by those directions and governs as follows. A subject is governed when any one of four conditions holds: the admitted project input (REQ-polaris-generation-001) records that a kernel evidence drawer exists for the subject; or the source classes of the tree at the pinned revision, as Syzygy's own path listing of that tree exposes them (REQ-polaris-generation-030), include an `openspec/**` specification, a capability declaration or declared topology. Because a path listing cannot tell whether a declaration is adopted, every path under a `.syzygy/` governance tree, where Syzygy's capability declarations and topology are held, counts toward those last two conditions, adopted or not; this is never less strict than REQ-polaris-generation-032's "adopted capability declaration", and the two predicates are an overlap that whichever of the two changes is adopted second reconciles. A subject is non-governed only when the admitted project input states that no kernel evidence drawer exists for it and the tree holds none of the other three. For a non-governed subject the agent sessions' sends are the operator's own act as stated above and no statement is required. For a governed subject, and for a subject whose project input does not state whether a drawer exists, Syzygy SHALL refuse to issue a brief unless an in-force, recorded, per-project statement names the operator's agent provider and the content classes it may receive, and SHALL cite that statement in the run record; its withdrawal SHALL refuse further steps of any run that relies on it. The statement is a consent record: it is the "explicit, recorded, per-project consent" that SEC-2 requires before governed-project content reaches a model provider, held in its own separately revocable and renderable record, and it is not an egress record of any transmission and not evidence of what the agent sent. Neither the content classes the statement names nor the observing project's classification and screening policies (SEC-5) bind the agent sessions' own reads or sends: the agent reads the clone without restriction, and content those policies would exclude, secrets included, may reach the agent's provider. Classification and screening bind every read Syzygy makes and everything Syzygy stores or renders.
>
> Before it issues a brief, Syzygy SHALL verify that the clone's checked-out HEAD commit equals a revision that the in-force observation consent for the repository names, and SHALL record that commit as the run's pinned revision. At every later check, review check and render, Syzygy SHALL verify again that the recorded pinned revision is a revision the in-force observation consent names, and SHALL refuse the step otherwise; withdrawal of the observation consent, the registry entry or a policy act refuses every later step of the run. The brief, the draft, the inventory and every review packet SHALL name the pinned revision, and a draft, inventory or verdict that names another revision SHALL be refused. Which consented revision the run was pinned to rests on a stored record and SHALL be disclosed as Inferred under the records rule below; that the revision is consented, and every object read at it, is verified at each step. A HEAD that differs from a named revision, a revision the consent does not name, or an absent, withdrawn or ineffective observation consent, observer registry entry, classification policy act or screening policy act SHALL refuse the run with its reason in human and machine form. The operator's start of the run is the owner's request under REQ-polaris-generation-020; the run creates no scheduler work item, Proposal or materialization record, because it makes no provider dispatch and no scheduler effect, and Syzygy SHALL write only to its own state directory for the run, never to a location derived from the clone's path. The Execution Record's work item identity is therefore absent, with its reason stated, and the run is rendered as unattributed execution under RFC4-19, never dropped. The `syzygy dossier` commands are a local program the operator's sessions invoke as the operator's own user: they serve no route, accept no network request, hold no credential that authenticates to Syzygy and are outside REQ-polaris-generation-021's route inventory; the principal of every admission, denial and refusal they record is the operator, operator-declared, with its credential or session identity recorded as Unknown, never fabricated. Every read Syzygy makes for the run SHALL be a Git object read by object identifier at the pinned revision through the registered observer, never a read of the working tree, and every object SHALL be classified and screened under the observing project's effective policies (REQ-polaris-generation-025) before its content is used in a check or rendered. Because the clone's object store lies within the agent sessions' write reach, those reads SHALL honour no replacement objects, grafts, repository-local configuration, hooks or alternates; the hash algorithm is the one the consented revision's identifier is written in, never one the clone's configuration declares, and a clone whose objects do not hash under it SHALL be refused. Syzygy SHALL recompute the object identifier of every commit, tree and blob it reads on the path from the pinned commit to each blob it uses, from the bytes it read, at every step that uses the object. An object whose recomputed identifier differs from the identifier by which it was reached, or that cannot be read without an alternate or a replacement, SHALL refuse the step that needed it, with its reason in human and machine form, and none of its content SHALL be used, quoted, classified as admitted or rendered.
>
> Syzygy SHALL execute no observed code, SHALL launch or schedule no process that does, and SHALL give no instruction to an agent (a brief, prompt, skill or work item) that tells it to, except in the one case D9 permits (SEC-3). The owner direction `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`, item 2, permits the agent session to build and run the observed project in the clone, and the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-2026-10-05`, item 1, makes that permission depend on an owner-adopted amendment to SEC-3, drafted as D9. The authoring session's brief SHALL say that the agent may build and run the observed project only when all of these hold: D9, or the identifier it carries when adopted, is in force and its permitted case for the owner's attended agent session applies; the operator is the owner, and the authoring session is one the owner started on the owner's own host and attends, being present to see and stop what it does, never a session Syzygy started, one left running unattended, or one left under an automatic-approval or permission-bypass setting while the owner is away; the owner's execution choice for this run, recorded as stated below, was recorded before Syzygy issued the brief, and the brief cites it; and, where D9 as adopted carries its credential condition, the credential check below passed when the brief was issued. Otherwise the brief SHALL quote SEC-3's rule that observed-project code runs only inside an explicit, opt-in execution profile, and SHALL NOT invite the agent to build or run the observed project outside such a profile. Only the authoring session's brief may carry the permission: the inventory brief, every review packet and every session prompt Syzygy prints SHALL carry SEC-3's rule. A brief that permits execution SHALL say that the permission lapses if the owner stops attending the session, including by leaving it under an automatic-approval or permission-bypass setting while away, and that the agent then runs no further observed code; whether the owner attended is the operator's declaration, labelled Inferred. Such a brief SHALL say that work the agent hands to its own subagents stays part of the session and under its rule, SHALL NOT ask for any process that outlives the session, and SHALL require the agent to stop, before its session ends, every process it started, including any it left running in the background; that the agent did so is its own report, labelled Inferred.
>
> The owner's execution choice SHALL be a record for one run that names what the instruction covers: the run, its pinned revision, and building and running the observed project in the clone from that run's authoring session. Syzygy SHALL take the choice only from a dedicated command that the operator runs personally, in a new terminal or behind the agent tool's shell-escape prefix, never from the run configuration, an earlier run, or a standing or per-project record, and SHALL refuse a choice that names another run or revision, or none. The skill and agent texts SHALL tell the agent never to run that command. Syzygy cannot observe who ran the command, or that the operator is the owner: both rest on the operator's declaration, are labelled Inferred and are disclosed, and the record lies, like every record of the run, within the agent sessions' write reach. Syzygy SHALL NOT instruct a session to run observed code before the owner's choice for that run is recorded, or on a standing record, and SHALL NOT ask for the choice while D9 is not in force.
>
> Where D9 as adopted carries its credential condition, Syzygy SHALL, before it issues a brief that permits execution, at every later check and at close, attempt as the operator's user to read every credential that Syzygy's configuration holds for its typed adapters. If any is readable, Syzygy SHALL NOT issue a permitting brief, and after one is issued SHALL report the breach as a finding of that step, tell the agent to run no further observed code, and record the breach in the run record. An agent tool's permission or deny rule does not satisfy the check, which is a read at the operating-system level. The check observes what the operator's user could read at the instant it ran; that no process the session started, directly or not, could read a credential between checks or by another route is Inferred and disclosed.
>
> The run record SHALL name the execution rule the brief carried and, where execution was permitted, the owner's recorded choice and the cost D9 states: the session runs with the owner's own credentials and network, including Syzygy's endpoints and any Syzygy credential readable on that host, and observed code it runs can change any file the owner can, the clone included. Under either rule the brief SHALL require that every claim the agent rests on building or running the observed project be marked as resting on execution, labelled Inferred and name the commands it rests on, and that the draft list every command the agent reports having run, whether or not a claim rests on it. Syzygy SHALL disclose that whole list, as the session's own report, and each rendered claim that rests on execution SHALL show the commands it names beside it. Syzygy SHALL record that list in the run record as the agent's report, labelled Inferred; it cannot observe what the agent ran, and SHALL NOT present the list as complete or as Observed.
>
> The run configuration SHALL declare, before the brief is issued, the operator, the agent tool and its version, the agent's model provider, the model identity and, where the tool shows one, the model version, and these limits: a positive wall-clock deadline; at least one of a positive token budget or a positive turn budget for the agent sessions; and a repair-cycle limit and a clarification-question limit, each a nonnegative integer, 0 allowed. A configuration that lacks any of these, or that states an unlimited, negative or non-integer value, or zero for the deadline or for a stated token or turn budget, SHALL be refused; there is no default. Syzygy SHALL record each declared value as operator-declared and Inferred, and SHALL state that no provider-reported model version is available in this mode (REQ-polaris-generation-003). Syzygy SHALL enforce the limits that bind its own steps: it SHALL refuse a check or review check beyond the repair-cycle limit and any step after the deadline, measured on its own clock from the issue of the brief, and SHALL record the instants of its own steps. Syzygy cannot observe or enforce the agent sessions' usage. Agent usage SHALL be recorded only as the figure the operator declares, labelled Inferred and attributed to the operator, and where no figure is declared the run record SHALL say that the usage was not recorded and that Syzygy cannot observe it; it SHALL NOT be presented as Observed, as a provider receipt, or as zero.
>
> Under the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-2026-10-05`, Syzygy SHALL hold the run record and every record on which a check result, a limit or readiness rests in its own state directory for the run, outside the clone, and SHALL NOT claim that directory is outside the agent sessions' write reach; no separate operating-system user or sandbox is required. Syzygy SHALL NOT rest an Observed label on a record it stored. At render, and at each check, Syzygy SHALL re-derive from objects it verifies at that step: every rendered quotation, by locating the quotation again in the verified blob rather than trusting a recorded byte range; every check result; and every verdict's binding, by rebuilding the review packet from the frozen subject and comparing its digest to the one the verdict names. Every value Syzygy shows that it cannot re-derive at that step SHALL be labelled Inferred, including the repair-cycle count, the instants of earlier steps, the run record's own history, which consented revision the run was pinned to, the brief's text and the execution rule it carried, the owner's execution choice and who entered it, the citation of a per-project statement, the declared session identifiers and launch forms, and the record of objects read in earlier steps. Syzygy SHALL issue no credential that authenticates to Syzygy for the run and SHALL place none in the clone, the brief, a review packet or the run's state directory.
>
> The run record and every rendered page SHALL disclose, in human and machine form: the authoring mode; the agent tool, its version, its provider and the model identity and version, as operator-declared; that the agent read the clone without restriction, and that neither the consented content classes nor the screening policies bound what the agent read or sent; that the agent's account of what it read is self-reported and Inferred; the execution rule the brief carried, and whether the agent reported building or running the observed project, with every command it reported, labelled Inferred and marked as self-reported; that Syzygy made no provider call; the pinned revision; that every rendered quotation was verified by Syzygy against the Git objects at that revision, with their identifiers recomputed; and that every value Syzygy shows from its stored records, rather than re-derives, is Inferred.
>
> For a run in the operator-agent mode this requirement displaces exactly this predecessor text, quoted in the semantic delta: in REQ-polaris-generation-005, the sentence "A generation request SHALL identify positive finite limits for provider calls, input/output volume, charged usage and elapsed time, plus a finite nonnegative repair-cycle limit before dispatch.", replaced by the declared limits above, in its scenario "Invalid output or exhausted budget" the words "records actual usage", read as the instants of Syzygy's steps and the operator-declared usage, and in its scenario "Inspectable successful run" the words "with their actual inputs and outputs", read for source understanding and narrative construction as the pinned revision, the brief and the agent's self-reported account, labelled Inferred, and for Syzygy's own checks, packets and render as the objects and records Syzygy used; in REQ-polaris-generation-017, the clause "External authorities SHALL be accessed through their single registered adapter per project, never a competing direct route" and the scenario "Interface tries to bypass its adapter", as they apply to a provider operation, because the run has no provider route and Syzygy makes no provider operation (both continue to apply to Syzygy's Git object reads); in REQ-polaris-generation-018, the "final usage receipt" of the scenario "Interrupted run lacks optional evidence" and the "Captured usage" of the sentence on usage and cost, which in this mode are never captured and are replaced by the operator-declared figure above, and the words "immutable, identified, integrity-verifiable Execution Record in its governing work home", read as an identified Execution Record held in the run's state directory, whose immutability and integrity are Inferred; in REQ-polaris-generation-020, the Proposal, approval, scheduler-creation and materialization gates, read as stated above for a run that makes no provider dispatch and no scheduler effect; and in REQ-polaris-generation-022, the sentence "The trail SHALL reside outside the governed plane and untrusted actor write reach; work records or a same-user writable directory SHALL NOT substitute.", which a run on a host where the agent sessions share the operator's user cannot meet, so that the audit evidence of the run's admissions, denials and refusals is held in the run's state directory, labelled Inferred and disclosed; an agent session could alter or erase it, and no surface presents it as trustworthy recovery evidence. The Provider bullet and the "Budget and retry decisions" section of the base change's `INTERFACES.md` are read the same way: there is no provider adapter, and the operator, never the agent, declares the limits. The "Resolve warranted work" and "Materialize once, then execute" sections of the base change's `OWNER-FLOW.md` are read with REQ-polaris-generation-020 as stated above, and the paragraph of its `SECURITY-CONTRACT.md` that begins "The trail resides outside the governed plane" is read with REQ-polaris-generation-022's trail sentence. In REQ-polaris-generation-001, the sentence "For absent or withdrawn provider consent, the draft layer SHALL render Unknown (`unconsented-source-or-provider`) as a policy state in both channels, including when a prior draft remains retained." is read under the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`, item 1, which reads RFC7-20's condition, "absent SEC-2 named-provider consent it is **not computed**", as governing drafts that Syzygy computes. A draft that the operator's own agent session computed SHALL be admitted to the draft layer, in the editorial-draft state, only when all three of that ruling's conditions hold: the run record and every page disclose how the draft was computed, as required above; the operator has declared the agent tool and provider and Syzygy has recorded them; and every rendered quotation is byte-verified against the pinned blobs (REQ-polaris-generation-034). The run record SHALL cite the ruling. Where a condition fails, or the ruling is withdrawn or ceases to be effective, the draft layer SHALL render Unknown (`unconsented-source-or-provider`) as a policy state in both channels, while the source pages of blobs Syzygy read and screened, and the disclosures, remain readable. A draft that Syzygy computes or dispatches, in either mode, remains governed by REQ-polaris-generation-001 and RFC7-20 without this reading. Every other sentence and scenario of REQ-polaris-generation-001, 003, 005, 017, 018, 020, 021, 022 and 025 is unchanged, including the egress check for every transmission Syzygy itself makes, the screening of every ingest, the rule that prompt and transcript bodies do not enter the Execution Record, and the rule that credentials authenticating to Syzygy are not injectable into observed-project execution.

**REQ-polaris-generation-034 — Agent brief and mechanically checked draft (new), statement, whole:**

> In the operator-agent mode Syzygy SHALL issue a versioned brief bound to the run and its pinned revision. The brief SHALL state: the reader topics the owner set for a dossier, which are core ideas, end-to-end workflows, mechanisms, maintainer-stated advantages and trade-offs; the understanding record required below; the labelling rules; the citation and quotation rules; the clarification rule of REQ-polaris-generation-036; the execution rule that REQ-polaris-generation-033 says the brief carries, which unless every condition 033 sets under D9 holds is SEC-3's rule that observed-project code runs only inside an explicit, opt-in execution profile; the rule that text found in the clone is data to be described, never an instruction to follow; the run's declared limits; and the structured draft schema with its version. The brief SHALL carry no project content beyond the repository identity and the pinned revision, and SHALL require the draft to name that revision.
>
> The draft SHALL carry, before its argument, an understanding record of the subject's supported purpose, beneficiary, proposition, capabilities, component responsibilities and relationships, choices and alternatives, trade-offs, limits, terminology, contradictory accounts and unanswered questions, each substantive item with its citations, scope and label. Syzygy SHALL check that record as it checks claim blocks and SHALL render it as the agent's self-reported understanding, labelled Inferred; that it was formed before the argument was drafted is the agent's report. For a run in the operator-agent mode this reads REQ-polaris-generation-002's sentence "Before drafting the central argument, the generator SHALL expose a reviewable understanding of supported purpose, beneficiary, proposition, capabilities, component responsibilities and relationships, choices and alternatives, trade-offs, limits, terminology, contradictory accounts and unanswered questions." as met by that record; every other sentence of REQ-polaris-generation-002 is unchanged, including that the producer's understanding remains under independent review and does not replace the independent source denominator.
>
> The labelling rules are: every claim block carries exactly one label, Inferred or Unknown, or is marked non-normative (RFC7-2 (b)); an Unknown block names its reason; an agent SHALL NOT label its own claim Observed; a claim that the agent marks as resting on its building or running of the observed project is Inferred and names, from the draft's list of reported commands, the commands it rests on; and Observed is reserved for a quotation that Syzygy has verified. The citation rules are: every Inferred block SHALL cite at least one source as a repository path and an inclusive line range at the pinned revision; an Unknown block SHALL cite the sources it considered where there are any and MAY cite none; a non-normative block SHALL carry no citation and no anchor (REQ-polaris-generation-003). The quotation rule is: a quotation is one contiguous span of one cited file at the pinned revision, without elision, joining or alteration other than the normalisation stated below, and every quotation SHALL name the citation it is taken from.
>
> Syzygy SHALL check each submitted draft and SHALL report every failure as a repair finding that names the block, the citation, the kind of failure and the location to repair. The checks are:
>
> - the draft validates against its declared schema version, with unique identities and resolving internal references (REQ-polaris-generation-019), and names the pinned revision;
> - every cited path names a blob at the pinned revision, and every cited line range lies within that blob;
> - every quotation, after the normalisation that the generator's existing quote check applies to both the quotation and the source, is one contiguous run of the cited blob's text, beginning and ending on word boundaries, that lies within the cited line range, and Syzygy records the span's byte range in the blob; that normalisation drops comment leaders at line starts and a closing comment marker at a line end, keeps only the text of markdown links and images, decodes character entities, removes markdown backslash escapes, drops backticks, drops paired emphasis marks at word edges, straightens curly quotes, turns an ellipsis character into three full stops, and collapses each whitespace run to one space; an ellipsis in a quotation that the source does not carry is an elision and fails;
> - every block carries a label the labelling rules permit and the citations the citation rules require, a non-normative block carries none, every Unknown block names a reason from RFC2-24's closed list, and every block the agent marks as resting on execution names at least one command present in the draft's list of reported commands. Syzygy can see only the marking; whether an unmarked claim rests on execution is the agent's report, and the page SHALL say so.
>
> A blob that classification or screening excludes SHALL NOT be used to verify a quotation: the quotation is unverifiable, the block that relies on it SHALL render Unknown with `excluded-content` instead of the quotation, and its exclusion is not a repair finding. A repair finding SHALL carry no excluded bytes. Each resubmission is a new draft revision with its own identity; it counts against the repair-cycle limit, and it retires earlier check results and dependent review evidence (REQ-polaris-generation-006). A draft with an unresolved finding SHALL NOT proceed to review or become ready.
>
> Syzygy SHALL render a checked draft through the existing multi-page dossier renderer. Every rendered quotation SHALL be the span Syzygy located, at render, in the blob it read and verified at the pinned revision, never the agent's copy of it and never a byte range taken on trust from a stored record. A source page SHALL be rendered only for a blob that Syzygy read and verified at the pinned revision and that screening admitted. Each anchor SHALL take RFC7-10's form: the target class is an evidence artifact identifier with integrity digest, whose identifier is the blob's object identifier as Syzygy recomputed it from the bytes it read, with its hash algorithm named, that algorithm being the one the consented revision's identifier is written in, serving as both the owning identifier and the integrity digest; the optional fragment is the byte range of the span; the target state is the pinned revision. The repository path is shown beside it as a label, never as its identity. Generated prose SHALL render in the editorial-draft state (RFC7-20), machine-marked with the operator-declared model identity and version as its inference provenance. Rendering obligations of REQ-polaris-generation-003, 004 and 012, and of REQ-polaris-generation-032 where it is adopted and applies, are unchanged.

**REQ-polaris-generation-035 — Fresh-context review in the operator-agent mode (new), statement, whole:**

> In the operator-agent mode the independent inventory and the fidelity and rendered-design reviews that REQ-polaris-generation-006 requires SHALL each be produced in a separate top-level agent session that the operator starts (owner direction `POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`, item 2); a session the operator starts in a new terminal, or by typing the command Syzygy printed behind the agent tool's shell-escape prefix (in Claude Code, `!`) in the authoring session's terminal, is a session the operator starts; a subagent spawned by the authoring session, a process the authoring session's agent launches, including a headless session it starts and whose output it reads, or any context whose instructions the authoring session wrote, SHALL NOT satisfy the inventory or a review. The inventory context SHALL start from Syzygy's inventory brief and SHALL NOT be given the draft; Syzygy SHALL check its quotations and citations as REQ-polaris-generation-034 checks a draft, and SHALL freeze it before the fidelity review. For each review Syzygy SHALL emit a review packet containing only the frozen subject (the draft with its understanding record, or for the rendered-design review the rendered pages excluding one named review-status region), the cited spans as Syzygy read them, the governing criteria, the verdict schema, the pinned revision and the packet's own digest, so that the review context can re-hash the packet before it reads it; the fidelity packet SHALL also carry the frozen inventory, as the criterion against which REQ-polaris-generation-006 measures coverage, and its cited spans SHALL be those cited by the draft and by the frozen inventory, screening-admitted only; the pages published after the rendered-design review SHALL be the reviewed pages with only the named review-status region changed, and a change outside that region is a revision of the subject; the packet SHALL NOT contain the brief's authoring exchange, any transcript or the agent's read account. The review context SHALL write a structured verdict that names the packet's digest and records inventory-to-draft coverage for every inventory entry, draft-to-source support for every claim block, the accuracy of every inventory entry against the cited spans in its packet, and every finding with its severity and its deficient subject (discovery, understanding, clarification, argument, prose, asset or rendering).
>
> Syzygy SHALL validate the verdict before it counts: its schema; that the packet digest equals the digest of the packet Syzygy rebuilds, at validation and at render, from the current frozen subject; that every inventory entry and every claim block has an entry; that every quotation the verdict relies on verifies as in REQ-polaris-generation-034; and that a verdict with an unresolved blocking finding does not declare the subject ready. A verdict that fails validation SHALL be recorded and SHALL NOT count as a review. Any revision of the subject or the inventory retires the verdicts bound to it.
>
> The run record SHALL record the agent tool, version and model of the authoring, inventory and review contexts as the operator declares them; each context's session identifier as that session declares it in its draft, inventory or verdict; and for each inventory and review context its launch form, which is a new terminal or the shell-escape prefix, as the operator declares it; each is labelled Inferred and attributed to whoever declared it. Syzygy SHALL refuse an inventory or verdict whose declared launch form is neither, and neither SHALL count until its launch form is declared. Syzygy SHALL refuse an inventory whose declared session identifier equals that of the authoring session, and a verdict whose declared session identifier equals that of the authoring session or of the inventory session it reviews. The record SHALL distinguish what Syzygy observed, which is the packet Syzygy built and rebuilt from the frozen subject, its digest, and that the verdict names that digest, from what remains Inferred, which is that the review context read the packet Syzygy emitted, unaltered, that each session was a top-level session the operator started, in the launch form declared, and not a subagent or process of the authoring session, that each context was fresh, that the review context saw nothing beyond its packet, that the inventory context did not see the draft, that each verdict and the inventory were written by the session declared for them, the session identifiers themselves, and the inventory's completeness over the clone and its preparation from the whole source population. The review page SHALL disclose that distinction.
>
> For a run in the operator-agent mode this requirement reads REQ-polaris-generation-006 as follows, and displaces only what it names: "Reviewers SHALL receive the artifact, governing references and acceptance criteria without the authoring conversation" is met by the packet rule above; the inventory "covering the entire admitted source population" is the inventory context's self-reported coverage of the clone at the pinned revision, labelled Inferred, and readiness SHALL NOT claim that coverage as verified; in "The fidelity reviewer SHALL verify inventory accuracy and completeness against the owning admitted sources rather than trusting preparation output.", accuracy is verified by the fidelity reviewer for each inventory entry against the cited spans in its packet, and completeness is the inventory context's self-report, labelled Inferred and never presented as verified, because the owner's ruling confines the reviewer to its packet; in "The bounded workflow SHALL prepare or validate the independent inventory and questions from admitted sources", the inventory is prepared by the inventory context from the clone it read without restriction, and Syzygy validates its quotations and citations against the blobs it read and verified at the pinned revision, while its preparation from the whole source population is the inventory context's self-report, labelled Inferred; and the words "accounting for those calls in its run budget" read as the operator-declared limits of REQ-polaris-generation-033, which cover the inventory and review contexts. Every other sentence and scenario of REQ-polaris-generation-006, including the rule that unresolved material omissions prevent readiness, the fresh-reader review of RFC7-25 and the rule that the generator does not classify its own wording change as immaterial, is unchanged.

**REQ-polaris-generation-036 — Self-reported discovery and in-session clarification (new), statement, whole:**

> In the operator-agent mode the discovery account that REQ-polaris-generation-030 requires SHALL consist of two populations, kept distinct in human and machine form. The first is the agent's account of what it inspected and selected, with its reasons for material it excluded, could not resolve or deferred, and its stopping reason; Syzygy SHALL record and render it as self-reported and labelled Inferred, and SHALL NOT present it as complete, as verified, or as Observed. Syzygy SHALL report as findings the self-reported paths that name no blob at the pinned revision; a path that does exist does not make the account Observed. The second population is the set of Git objects that the render itself reads and verifies, each with its path, object identifier, pinned revision and classification and screening outcome, labelled Observed; which objects Syzygy read in earlier steps comes from a stored record and, where shown, is labelled Inferred. Syzygy SHALL NOT derive an Observed not-read figure or an Observed coverage claim from the agent's account. REQ-polaris-generation-030's obligations on scope, supported profile, stopping reason, partial findings and narrower scopes apply to the agent's account as self-reported content.
>
> The consequential questions of REQ-polaris-generation-031 SHALL be asked of the human operator within the agent session. The draft SHALL record each question with the evidence considered, the consequence for the draft, the interpretations offered, and the operator's answer as free text, a selected interpretation, leave-unknown or defer, attributed to the operator. Because Syzygy does not observe the exchange, the record SHALL be labelled as the agent's report of it. The number of questions SHALL NOT exceed the declared clarification-question limit of REQ-polaris-generation-033. Every other obligation of REQ-polaris-generation-031 is unchanged: an answer does not prove implementation behavior or adopt intent, unchanged questions reuse prior answers, a purpose left unknown stays unknown, and answer changes invalidate dependent content and reviews.
>
> For a run in the operator-agent mode this requirement displaces or reads exactly this predecessor text: in REQ-polaris-generation-030, the item "inspected and selected material" in the list the generator "SHALL expose" before claiming source coverage, read there as an account the generator itself produced, which becomes the two populations above; the sentence "The generator SHALL perform question-directed, bounded discovery for a selected project only after the applicable metadata-only start preparation, work/admission gates and effect permissions; investigation SHALL NOT read sources to authorize itself.", read as binding Syzygy, whose start gates of REQ-polaris-generation-033 all pass before it issues the brief or reads any object for a check, while the agent's own exploration of the clone, before or after the brief, is the operator's own act under the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05` and is disclosed as such; the sentence "Body, code, history and other content reads SHALL remain individually covered by applicable consent and classification; no shell or observed-project execution is implied.", read as binding every read Syzygy makes, each of which is covered by the observation consent and classified and screened, while the agent's reads are the operator's own act, unclassified and disclosed as such, and the agent's building or running of the observed project is governed by the execution rule of REQ-polaris-generation-033, never implied by discovery; and in REQ-polaris-generation-031, "owner" as the person asked, which becomes the human operator of the run, whose answers are attributed to the operator. Every other sentence and scenario of REQ-polaris-generation-030 and 031 is unchanged.

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
- **RFC7-20's text and REQ-polaris-generation-001 for Syzygy-computed
  drafts.** No byte changes. A draft Syzygy computes or dispatches, in either
  mode, still renders Unknown (`unconsented-source-or-provider`) without
  named-provider consent. Only an operator-computed draft meeting the three
  conditions of the rulings direction, item 1, is admitted.
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
- **REQ-polaris-generation-020 for the provider mode.** In the
  operator-agent mode 033 reads its gates for a run that makes no provider
  dispatch and no scheduler effect: the operator's start is the request, no
  Proposal, scheduler item or materialization record is made, and Syzygy
  writes only to its own state directory. That reading is the drafter's. The
  owner's records ruling (R1) does not cover it (second review, finding 5),
  so it goes to the owner with the sign-off offering.
- **REQ-polaris-generation-022's credential rule and audit content.** No
  credential authenticating to Syzygy is issued for the run or placed where
  the agent or observed code can read it. Only the trail-location sentence is
  read, and only for this mode.
- **RFC2-24's closed Unknown reasons.** No reason is minted; unobserved agent
  usage is disclosed as a fact of the render.
- **Doctrine.** No doctrine byte changes. SEC-2 is read, not changed; for
  governed projects the per-project statement 033 requires is the consent
  record, and the spec states that neither its content classes nor SEC-5
  screening bind the agent's own reads and sends (review-1 rulings, item 2).
  SEC-3 is not read down: unless D9 is adopted and in force, the operator is
  the owner attending sessions the owner started on the owner's host, the
  owner's choice for that one run is recorded by the operator before the
  brief, and any credential check D9 requires passes, the
  brief quotes SEC-3's rule and does not invite execution outside an
  execution profile (review-1 rulings, item 1; D9's draft conditions), and
  this change may not be signed before D9's adoption. Syzygy executes no
  observed code, and launches or schedules nothing that does, in any case.
  SEC-1 is read, not changed: the `syzygy dossier` commands are a local
  program serving no route [Inferred].

## The owner's trade-off, preserved

The owner chose "Rule it by interpretation" over the recommended per-project
provider record, with the description shown at the time: "it rests on an
interpretation of an accepted contract and a reviewer may call it a contract
change." This change relies on that reading in REQ-polaris-generation-033 and
does not resolve the question it leaves open. The first review (finding 6)
found that RFC7-20's clause "carries no qualifier about who computes the
draft", so that for an operator-computed draft the reading is "a change to
the clause's effect, not an application of its text", and offered a second
basis: for a non-governed subject SEC-2 does not reach the content, and for a
governed subject the per-project statement is itself the named-provider
consent. The owner kept the ruling ("Keep my ruling") and directed that the
finding be recorded for the owner and preserved, not resolved
(`POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-2026-10-05`, item 3). It goes
to the owner with the sign-off offering. The drafter neither concedes it nor
argues it away. The second review (finding 7) agreed, and added that under
the spec as now written the reading does work only for non-governed
subjects, because a governed subject's per-project statement would meet
RFC7-20's condition on its own text. That too goes to the owner. The
alternative the owner declined, a per-project consent record naming the operator's provider, is
also the remedy if the owner later reverses the reading: 033 already renders
the draft layer Unknown when the reading ceases to be effective.

The owner chose "Any repo" over the recommended "Observed repos only"
(`POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`, item 1),
with SEC-2 unchanged and the reconciliation left to this amendment. The
first review (finding 7) reported that the consented content classes cannot
be enforced or observed in this mode, that content SEC-5 would exclude,
secrets included, may reach the agent's provider, and that the statement is
arguably an egress record. The owner chose "Keep any repo, disclose" over
"Public repos for now", expecting the SEC-2 "scoped" and SEC-5 questions to
be raised again (review-1 rulings, item 2). 033 now says plainly that the
statement is a consent record held in its own record, not an egress record,
and that neither its classes nor SEC-5 screening bind the agent's own reads
and sends; it decides "governed" by the four conditions of the sibling
candidate 032 (finding 7d), restated in 033 so that the predicate does not
depend on 032's adoption. Whether a consent whose class limit nothing
enforces is SEC-2's "scoped" consent remains the owner's question, carried
with the sign-off offering. The second review (finding 8) located it: 033's
sentence "The statement is a consent record: it is the "explicit, recorded,
per-project consent" that SEC-2 requires before governed-project content
reaches a model provider" asserts the answer, while SEC-2's head reads
"explicit, scoped consent". The sign-off decides that sentence. On the
predicate, a path listing cannot tell whether a capability declaration is
adopted, so 033 counts every `.syzygy/` path, adopted or not: never less
strict than 032, and an overlap that whichever of the two is adopted second
reconciles.

The owner chose "Separate session" for review independence (same record,
item 2). 035 applies it; the fidelity packet also carries the frozen
inventory, as the criterion REQ-polaris-generation-006 measures coverage
against, which is a reading of "only the draft, cited spans and criteria"
flagged for the reviewer; the verdict schema it adds is a format, not
content. After round 1 the owner's lead ruled on the launch forms (finding
9): a session the operator starts in a new terminal, or with the agent
tool's `!` shell-escape prefix in the authoring session's terminal, counts
as operator-started; a headless session the authoring agent starts and
reads does not, because it is not a session the operator starts and it
brushes against "No unattended agent coordination". The launch form is
recorded as operator-declared. The second review (finding 4) set out what
the owner should see, and the packet now shows it: admitting `!` is the
lead's reading of the owner's words "A second top-level Claude Code/Codex
session you start", not an owner ruling. The printed command is headless
(`claude -p` or `codex exec`); launched with `!` it runs as a child of the
authoring tool's shell, inherits its environment, and its whole output lands
in the authoring agent's context, so the only difference from the excluded
headless launch is who typed the command, which Syzygy cannot observe. The
owner's sign-off covers that reading. Extending the separate-session rule to the inventory and the
rendered-design review, and the session-identifier refusal to the inventory,
is the drafter's choice, stricter than the ruling and never wider. Because
the ruling confines the reviewer to its packet, 006's "completeness against
the owning admitted sources" cannot be verified in this mode: 035 verifies
each entry's accuracy against the packet spans and labels completeness the
inventory context's self-report, Inferred. If the owner wants completeness
verified, that needs a change to the ruled packet.

The owner also chose "Allow, disclose" over the recommended "Forbid,
disclose" for the agent's code execution, accepting that claims may rest on
behaviour the agent observed by running the project, which Syzygy cannot
observe or reproduce; those claims stay Inferred. The first review (finding
8) found that SEC-3's text ("Observed code is untrusted, everywhere.
Observed-project code runs only inside an explicit, opt-in execution
profile.") is not limited to code Syzygy runs, and the lead disclosed to the
owner that the earlier question had stated a reading, not the doctrine's
text. The owner chose "Allow on host, amend SEC-3" over "Only in a sandbox"
and "Forbid, disclose" (review-1 rulings, item 1): a SEC-3 amendment is to be
drafted and reviewed, this change may not be signed until the owner adopts
it, and until then nothing in the mode may tell an agent to run observed
code outside an execution profile. 033 and 034 make the brief's execution
rule depend on that amendment being in force.

The owner answered the records question (R1) with "Re-derive, label
Inferred (Recommended)" over "Separate OS user" and "Sandbox the agent"
(`POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-2026-10-05`). 033 cites it, rests no
Observed label on any stored record, and labels Inferred every value it
shows without re-deriving it. The second review (finding 5) found that the
question as asked did not cover the drafter's reading of 020's work-item
gates, and that the option's stated cost omitted three things: the 022
audit evidence of admissions, denials and refusals becomes agent-editable
(a refusal can be erased), and the pinned revision and the emitted packets
are stored records too. The 020 reading and those costs go to the owner with
the sign-off offering; the record does not present 020 as ruled.

The history of that question: the first review (finding 2) found that Syzygy's records sit within
the agent's write reach on a single-user host, against REQ-polaris-generation-018's
"immutable, identified, integrity-verifiable Execution Record in its
governing work home" and REQ-polaris-generation-022's "outside the governed plane and
untrusted actor write reach; work records or a same-user writable directory
SHALL NOT substitute". The honest option the drafter chose, in 033: hold the
records in Syzygy's state directory outside the clone, never call that
directory out of the agent's reach, rest no Observed label on a stored
record, re-derive every quotation, check and verdict binding from verified
objects at each check and at render, and label the integrity of what cannot
be re-derived (the repair-cycle count, earlier instants, the record's
history) Inferred. That reads 018 and the 022 trail sentence for this mode,
which is a security-posture question and therefore the owner's; the packet
asks it, with the alternatives (a separate operating-system user or the
daemon's own store for Syzygy's records, or the sandbox the owner declined
for the agent). R1 answered it as above.

D9, the drafted SEC-3 amendment (draft PR #357, arm A as frozen at
62c29093 after its round-2 repair), binds every instruction a Syzygy
feature gives an agent (a brief, prompt, skill or work item) and names one
permitted case: a Syzygy instruction may let a session on the owner's own
host, which the owner started and attends, "being present to see and stop
what it does", build and run observed code, on the owner's recorded choice
"for that one run, naming what the instruction covers"; "A standing or
per-project record does not qualify." Its conditions: the choice is
recorded before the instruction; claims resting on the run are Inferred;
every command the session reports is disclosed as its own report; and, if
the owner adopts the packet's Q3(b), Syzygy keeps its typed-adapter
credentials unreadable at the operating-system level by the session and
everything it starts, for as long as any of them runs. Syzygy never gives
the instruction to a session it started or one left unattended, and never
asks for a process that outlives the session; the session's subagents are
part of it.

033 carries each of these, and closes three points the doctrine leaves to
the spec. Who records the choice: the operator, personally, through a
dedicated command in a new terminal or behind the shell-escape prefix,
never the run configuration the agent writes, an earlier run or a standing
record; the choice names the run and its pinned revision, and the agent
texts never run the command. Syzygy cannot observe who ran it, so that the
owner made the choice is Inferred and disclosed, and the record is within
the sessions' write reach like every record of the run (R1). Attendance:
only the authoring session's brief may carry the permission, never the
inventory brief, a review packet or a session prompt, and the brief says
the permission lapses if the owner leaves the session under automatic
approval or permission bypass while away. The credential condition, where
adopted: Syzygy itself attempts, as the operator's user, to read every
adapter credential its configuration holds, before the permitting brief,
at every later check and at close; a tool's permission or deny rule does
not satisfy it, and between-check readability is Inferred. 033 and 034 cite
D9 by identifier. If D9's text changes, 033 and 034 follow it.

## Warrant

The owner direction `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05`
recorded in `.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-MODE-DIRECTION.md`,
items 1 to 5. Item 5: "The affected requirements are amended through one
reviewed CC-REV-2 delta, which binds only on the owner's sign-off." And the
owner direction `POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-2026-10-05`, recorded in
`.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RULINGS-DIRECTION.md`,
items 1 (the reading of RFC7-20) and 2 (code execution by the agent). And
the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05`,
recorded in
`.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-DIRECTION.md`,
items 1 (any repository), 2 (review independence) and 3 (sign-off form). And
the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-2026-10-05`,
recorded in
`.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-REVIEW-1-RULINGS-DIRECTION.md`,
items 1 (SEC-3 amendment gate), 2 (governed projects, disclosed) and 3
(RFC7-20 reading kept, finding preserved). And the owner direction
`POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-2026-10-05`, recorded in
`.syzygy/governance/decisions/POLARIS-DOSSIER-LOCAL-AGENT-RECORDS-DIRECTION.md`,
items 1 to 3 (records re-derived, stored values Inferred, no separate user or
sandbox). The doctrine amendment D9 is a dependency, not a warrant, until
the owner adopts it.

## Evidence or decision basis

- The direction above, with the owner's words and three selections quoted
  there.
- The adopted text quoted under "Current meaning".
- [Observed] The existing code each check reuses, named in `design.md`; the
  consent reader of PR #263 is on `main` since `b60e6cd2`. The isolation
  flags and environment of `apps/three-surface-poc/src/polaris-generation/isolated-git.ts`
  already disable replacement objects, system and global configuration and
  hooks; [Unknown] whether that reader re-hashes the objects it returns, which
  033 now requires either way.
- The first fresh-context review, verdict REVISE over `f1bd0b5c`, retained
  at `docs/reviews/R-POLARIS-DOSSIER-LOCAL-AGENT-MODE-1-RAW.md`; the second,
  verdict REVISE over `af97611d`, retained by the lead. Their dispositions
  are in `REVIEW-BRIEF.md`.
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
- **State directory**: the directory, outside the clone, where Syzygy holds a
  run's records; within the agent's write reach on a same-user host, so no
  Observed label rests on anything in it.
- **Recomputed identifier**: an object identifier Syzygy computes from the
  bytes it read, compared with the identifier it reached the object by.

None retires an existing term. Whether any belongs in `PROCESS-GLOSSARY.md`
is left to review.

## Downstream impact

See `IMPACT-LEDGER.md`: method, regexes, denominators and every citer
classified.

## Migration / supersession plan

- Signing waits for the owner's adoption of the SEC-3 amendment, drafted as
  D9 (review-1 rulings, item 1). Nothing is superseded. On adoption, in one logical change (CC-REV-2):
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
**Verdict:**         Round 1 REVISE over `f1bd0b5c` (21 findings; five
blocking). Round 2 REVISE over `af97611d` (17 findings; four blocking).
Repaired as `REVIEW-BRIEF.md` disposes. Round 3 is the confirming round,
dispatched by the lead after D9's text is fixed by its own review.
