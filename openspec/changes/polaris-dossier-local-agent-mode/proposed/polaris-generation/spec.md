# Polaris dossier local-agent mode

Candidate exact behavioral delta; not yet adopted, binds nothing. This change applies to the existing polaris-generation capability. It adds four requirements that define a second authoring mode, the operator-agent mode, beside the provider mode that the adopted requirements describe. It edits no byte of any predecessor requirement or scenario, in the base change or in the understanding amendment as amended by the tree-form adoption. For a run in the operator-agent mode it displaces or reads the predecessor text that each requirement below names, and only that text; for a run in the provider mode every predecessor requirement and scenario keeps its bytes and its meaning. The provider mode is parked by the owner direction of 2026-10-05, not withdrawn.

## ADDED Requirements

### Requirement: Operator-agent authoring mode

A generation run SHALL record exactly one authoring mode, `provider` or `operator-agent`, before any draft is admitted, and the mode SHALL NOT change within the run. In the operator-agent mode the draft, the independent inventory and the reviews are authored by coding-agent sessions that the human operator runs with the operator's own tools and account over a local clone of the subject, and Syzygy SHALL make no model-provider call for the run, resolve no provider route and transmit no project content to any service. The agent sessions' transmissions to their own provider are the operator's own act under the owner direction `POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05`: they are outside Syzygy's egress consent, no egress record is made for them, and Syzygy SHALL NOT present them as consented by, routed through or observed by Syzygy. The operator-agent mode SHALL be selected only for a subject that the admitted project input (REQ-polaris-generation-001) records as an observed repository that is not a governed project; a governed subject, and a subject whose project input does not say which it is, SHALL NOT be run in this mode.

Before it issues a brief, Syzygy SHALL verify that the clone's checked-out HEAD commit equals a revision that the in-force observation consent for the repository names, and SHALL record that commit as the run's pinned revision. A HEAD that differs from a named revision, a revision the consent does not name, or an absent, withdrawn or ineffective observation consent, observer registry entry, classification policy act or screening policy act SHALL refuse the run with its reason in human and machine form. Every read Syzygy makes for the run SHALL be a Git object read by object identifier at the pinned revision through the registered observer, never a read of the working tree, and every object SHALL be classified and screened under the observing project's effective policies (REQ-polaris-generation-025) before its content is used in a check or rendered. Syzygy SHALL execute no observed code. The brief SHALL instruct the agent not to build, install or run code from the clone; Syzygy cannot observe whether the agent complied, and the run record SHALL say so.

The run configuration SHALL declare, before the brief is issued, the operator, the agent tool and its version, the agent's model provider, and positive finite limits: a wall-clock deadline, at least one of a token budget or a turn budget for the agent sessions, a finite nonnegative repair-cycle limit and a finite clarification-question limit. A configuration that lacks any of these, or that states an unlimited or non-positive value, SHALL be refused; there is no default. Syzygy SHALL record each declared value as operator-declared. Syzygy SHALL enforce the limits that bind its own steps: it SHALL refuse a check or review check beyond the repair-cycle limit and any step after the deadline, measured on its own clock from the issue of the brief, and SHALL record the instants of its own steps as Observed. Syzygy cannot observe or enforce the agent sessions' usage. Agent usage SHALL be recorded only as the figure the operator declares, labelled Inferred and attributed to the operator, and where no figure is declared the run record SHALL say that the usage was not recorded and that Syzygy cannot observe it; it SHALL NOT be presented as Observed, as a provider receipt, or as zero.

The run record and every rendered page SHALL disclose, in human and machine form: the authoring mode; the agent tool, its version and its provider, as operator-declared; that the agent read the clone without restriction; that the agent's account of what it read is self-reported and Inferred; that Syzygy made no provider call; the pinned revision; and that every rendered quotation was verified by Syzygy against the Git objects at that revision.

For a run in the operator-agent mode this requirement displaces exactly this predecessor text, quoted in the semantic delta: in REQ-polaris-generation-005, the sentence "A generation request SHALL identify positive finite limits for provider calls, input/output volume, charged usage and elapsed time, plus a finite nonnegative repair-cycle limit before dispatch.", replaced by the declared limits above, and in its scenario "Invalid output or exhausted budget" the words "records actual usage", read as the Observed instants of Syzygy's steps and the operator-declared usage; in REQ-polaris-generation-017, the clause "External authorities SHALL be accessed through their single registered adapter per project, never a competing direct route" and the scenario "Interface tries to bypass its adapter", as they apply to a provider operation, because the run has no provider route and Syzygy makes no provider operation (both continue to apply to Syzygy's Git object reads); and in REQ-polaris-generation-018, the "final usage receipt" of the scenario "Interrupted run lacks optional evidence" and the "Captured usage" of the sentence on usage and cost, which in this mode are never captured and are replaced by the operator-declared figure above. The Provider bullet and the "Budget and retry decisions" section of the base change's `INTERFACES.md` are read the same way: there is no provider adapter, and the operator, never the agent, declares the limits. The draft-layer consent sentence of REQ-polaris-generation-001 and the consent condition of RFC7-20 are not displaced; how they read for a draft that the operator's own session computed is owner question O1. The draft layer of an operator-agent run SHALL render in the editorial-draft state only while an effective owner ruling holds that this consent condition is met for such a draft, and the run record SHALL cite that ruling; without one, or after its withdrawal, the draft layer SHALL render Unknown (`unconsented-source-or-provider`) as REQ-polaris-generation-001 requires, while the source pages of blobs Syzygy read and screened, and the disclosures, remain readable. Every other sentence and scenario of REQ-polaris-generation-001, 005, 017, 018 and 025 is unchanged, including the egress check for every transmission Syzygy itself makes, the screening of every ingest, and the rule that prompt and transcript bodies do not enter the Execution Record.

ID: REQ-polaris-generation-033
Source: SEC-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Clone pinned to a consented revision

- **WHEN** the operator starts an operator-agent run over a local clone whose HEAD commit is a revision the in-force observation consent names
- **THEN** Syzygy records that commit as the pinned revision and reads every object for the run by object identifier at that commit
- **AND** an uncommitted change in the clone's working tree never reaches a check, a quotation or a source page

#### Scenario: Clone at an unconsented revision

- **WHEN** the clone's HEAD commit differs from every revision the observation consent names, or the consent, registry entry or a policy act is absent, withdrawn or ineffective
- **THEN** Syzygy refuses the run before issuing a brief and states the reason in human and machine form
- **AND** no object is read for the run

#### Scenario: No provider call and no egress record

- **WHEN** an operator-agent run completes
- **THEN** Syzygy's record shows no provider route resolved, no provider call made and no project content transmitted by Syzygy
- **AND** the run record and pages state that the agent sessions' sends to their provider were the operator's own act and are not covered by Syzygy's egress consent

#### Scenario: Limits declared by the operator

- **WHEN** the run configuration omits the deadline, omits both the token and the turn budget, omits the repair-cycle or question limit, or states an unlimited or non-positive value
- **THEN** Syzygy refuses to issue the brief and names the missing or invalid limit
- **AND** no default limit is chosen on the operator's or the agent's behalf

#### Scenario: Agent usage is not observed

- **WHEN** the operator declares the agent sessions' token or turn usage at the end of a run, or declares none
- **THEN** the run record carries the declared figure as Inferred and attributed to the operator, or states that the usage was not recorded and that Syzygy cannot observe it
- **AND** no figure is labelled Observed, presented as a provider receipt or rendered as zero

#### Scenario: Syzygy's own limits enforced

- **WHEN** the agent submits a draft for checking after the repair-cycle limit is spent, or any step is requested after the deadline
- **THEN** Syzygy refuses the step, records the refusal and its Observed instant, and the draft does not become ready
- **AND** the run's last checked state remains inspectable

#### Scenario: Governed subject refused

- **WHEN** the admitted project input records the subject as a governed project, or does not say whether it is one
- **THEN** the operator-agent mode is not selected and the run is refused with its reason
- **AND** the subject remains eligible for the provider mode under the predecessor requirements

#### Scenario: Mode disclosed on every page

- **WHEN** an operator-agent run is rendered
- **THEN** every page and the machine manifest state the mode, the operator-declared agent tool, version and provider, the unrestricted reading, the self-reported read account, the absence of any Syzygy provider call and the pinned revision
- **AND** the human and machine disclosures carry the same values

#### Scenario: Draft layer without an owner consent ruling

- **WHEN** an operator-agent run is rendered and no effective owner ruling holds that the draft-layer consent condition of REQ-polaris-generation-001 and RFC7-20 is met for a draft the operator's own session computed, or that ruling has been withdrawn
- **THEN** the draft layer renders Unknown (`unconsented-source-or-provider`) as a policy state in both channels
- **AND** source pages and disclosures remain readable, and with an effective ruling the draft layer renders in the editorial-draft state citing it

Form: event-response.

- **Case:** Run operator-agent starts against controlled clones, consent records, registry entries, policy acts and run configurations, varying each independently; capture Syzygy's process network activity and object reads.
- **Observable:** The run record, the refusal reasons, the recorded pinned revision, the objects read and how they were addressed, the recorded limits and usage, captured network effects and the human and machine disclosures.
- **Oracle:** Expected refusals, pinned revisions and disclosures derived from the controlled inputs outside the generator; an independent capture of Syzygy's network effects, not the generator's own record of them.
- **Oracle independence:** The consent, registry, policy and configuration fixtures are prepared before the run and are not produced by the code under test.
- **Falsifier:** Syzygy makes a provider call or transmits project content; an object is read from the working tree or at another commit; a run starts at an unconsented revision or without a declared limit; agent usage is labelled Observed, shown as a receipt or as zero; a disclosure is absent or differs between channels.

```yaml
warrants:
  primary: SEC-2
  doctrine: [SEC-2, SEC-3, SEC-5, VIS-1, VIS-2, VIS-4]
  contracts: [RFC2-24, RFC3-16, RFC4-2, RFC4-19, RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: [REQ-polaris-generation-001, REQ-polaris-generation-005, REQ-polaris-generation-017, REQ-polaris-generation-018, REQ-polaris-generation-025]
```

### Requirement: Agent brief and mechanically checked draft

In the operator-agent mode Syzygy SHALL issue a versioned brief bound to the run and its pinned revision. The brief SHALL state: the reader topics the owner set for a dossier, which are core ideas, end-to-end workflows, mechanisms, maintainer-stated advantages and trade-offs; the labelling rules; the quotation rule; the clarification rule of REQ-polaris-generation-036; the run's declared limits; and the structured draft schema with its version. The brief SHALL carry no project content beyond the repository identity and the pinned revision.

The labelling rules are: every claim block carries exactly one label, Inferred or Unknown, or is marked non-normative (RFC7-2 (b)); an Unknown block names its reason; an agent SHALL NOT label its own claim Observed; and Observed is reserved for a quotation that Syzygy has verified. The quotation rule is: a quotation is one contiguous span of one cited file at the pinned revision, without elision, joining or alteration other than the normalisation stated below. Every claim block SHALL cite at least one source as a repository path and an inclusive line range at the pinned revision, and every quotation SHALL name the citation it is taken from.

Syzygy SHALL check each submitted draft and SHALL report every failure as a repair finding that names the block, the citation, the kind of failure and the location to repair. The checks are:

- the draft validates against its declared schema version, with unique identities and resolving internal references (REQ-polaris-generation-019);
- every cited path names a blob at the pinned revision, and every cited line range lies within that blob;
- every quotation, after the normalisation that the generator's existing quote check applies to both the quotation and the source, is one contiguous run of the cited blob's text, beginning and ending on word boundaries, that lies within the cited line range, and Syzygy records the span's byte range in the blob; that normalisation drops comment leaders at line starts and a closing comment marker at a line end, keeps only the text of markdown links and images, decodes character entities, removes markdown backslash escapes, drops backticks, drops paired emphasis marks at word edges, straightens curly quotes, turns an ellipsis character into three full stops, and collapses each whitespace run to one space; an ellipsis in a quotation that the source does not carry is an elision and fails;
- every label is one the labelling rules permit and every Unknown block names a reason from RFC2-24's closed list.

A blob that classification or screening excludes SHALL NOT be used to verify a quotation: the quotation is unverifiable, the block that relies on it SHALL render Unknown with `excluded-content` instead of the quotation, and its exclusion is not a repair finding. A repair finding SHALL carry no excluded bytes. Each resubmission is a new draft revision with its own identity; it counts against the repair-cycle limit, and it retires earlier check results and dependent review evidence (REQ-polaris-generation-006). A draft with an unresolved finding SHALL NOT proceed to review or become ready.

Syzygy SHALL render a checked draft through the existing multi-page dossier renderer. Every rendered quotation SHALL be the span Syzygy read from the blob at the recorded byte range, never the agent's copy of it. A source page SHALL be rendered only for a blob that Syzygy read at the pinned revision and that screening admitted. Each anchor SHALL take RFC7-10's form, with the blob's object identifier as the target identifier, the byte range as the fragment and the pinned revision as the target state; the repository path is shown beside it as a label. Generated prose SHALL render in the editorial-draft state (RFC7-20). Rendering obligations of REQ-polaris-generation-004 and 012, and of REQ-polaris-generation-032 where it is adopted and applies, are unchanged.

ID: REQ-polaris-generation-034
Source: RFC7-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Brief carries topics, rules and schema

- **WHEN** an operator-agent run's limits and pinned revision are recorded
- **THEN** Syzygy issues a brief that names the five reader topics, the labelling rules, the quotation rule, the clarification rule, the declared limits and the draft schema version
- **AND** the brief contains no project content other than the repository identity and the pinned revision

#### Scenario: Quotation verified against the pinned blob

- **WHEN** a draft block quotes a span that, after normalisation, occurs contiguously in the cited blob at the pinned revision within the cited line range
- **THEN** Syzygy records the span's byte range and renders the span from its own read of the blob as an Observed quotation with an anchor in RFC7-10's form
- **AND** a later change to the clone's working tree does not alter the rendered span

#### Scenario: Quotation altered, elided or outside its range

- **WHEN** a quotation differs from the cited blob after normalisation, joins two separate spans, or occurs only outside the cited line range
- **THEN** Syzygy reports a repair finding naming the block, the citation and the kind of failure
- **AND** the draft does not proceed to review until a resubmitted revision passes

#### Scenario: Cited path absent at the pinned revision

- **WHEN** a block cites a path that names no blob at the pinned revision, or a line range beyond the end of the blob
- **THEN** Syzygy reports a repair finding for that citation
- **AND** no source page or anchor is rendered for the absent citation

#### Scenario: Quotation from an excluded file

- **WHEN** a block quotes a file that classification or screening excludes
- **THEN** the quotation is not verified or rendered and the block renders Unknown with `excluded-content`
- **AND** no source page is rendered for the file and no finding carries its bytes

#### Scenario: Agent labels its own claim Observed

- **WHEN** a draft block carries the label Observed, carries no label, or is Unknown without a reason from the closed list
- **THEN** Syzygy reports a label finding for that block
- **AND** Observed appears on the page only on a quotation Syzygy verified

#### Scenario: Repair loop counted

- **WHEN** the agent resubmits a repaired draft
- **THEN** the resubmission is a new revision whose check counts against the repair-cycle limit, and earlier check results and dependent reviews are retired
- **AND** each finding, its repair and both revision identities remain traceable

Form: event-response.

- **Case:** Submit controlled drafts against a fixture repository at a pinned commit, varying each quotation, citation, label and screening outcome independently, including exact, normalised, altered, elided, joined, out-of-range and excluded-file quotations.
- **Observable:** The issued brief, the repair findings, the recorded byte ranges, the rendered quotations, anchors and source pages, and the labels in human and machine output.
- **Oracle:** Expected findings and byte ranges computed from the fixture blobs outside the checker, by an independent byte search over the fixture's own normalised text; expected labels and Unknown reasons fixed in the fixture.
- **Oracle independence:** The fixture's expected outcomes are written before the checker runs and are not derived from the checker's output.
- **Falsifier:** An altered, elided, joined or out-of-range quotation passes; a rendered quotation comes from the agent's text or the working tree; a source page appears for an excluded or unread blob; a finding carries excluded bytes; an agent-labelled Observed claim renders as Observed; a stale check or review survives a resubmission.

```yaml
warrants:
  primary: RFC7-2
  doctrine: [SEC-5, VIS-1, VIS-2, VIS-3]
  contracts: [RFC2-24, RFC7-2, RFC7-9, RFC7-10, RFC7-19, RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: [REQ-polaris-generation-004, REQ-polaris-generation-006, REQ-polaris-generation-012, REQ-polaris-generation-019, REQ-polaris-generation-025]
```

### Requirement: Fresh-context review in the operator-agent mode

In the operator-agent mode the independent inventory and the fidelity and rendered-design reviews that REQ-polaris-generation-006 requires SHALL each be produced in an agent context separate from the authoring context. The inventory context SHALL start from Syzygy's inventory brief and SHALL NOT be given the draft; Syzygy SHALL check its quotations and citations as REQ-polaris-generation-034 checks a draft, and SHALL freeze it before the fidelity review. For each review Syzygy SHALL emit a review packet containing only the frozen subject (the draft, or the rendered pages for the rendered-design review), the frozen inventory, the cited spans as Syzygy read them, the governing criteria and the verdict schema; the packet SHALL NOT contain the brief's authoring exchange, any transcript or the agent's read account. The review context SHALL write a structured verdict that names the packet's digest and records inventory-to-draft coverage for every inventory entry, draft-to-source support for every claim block, and every finding with its severity and its deficient subject (discovery, understanding, clarification, argument, prose, asset or rendering).

Syzygy SHALL validate the verdict before it counts: its schema; that the packet digest equals the packet for the current frozen subject; that every inventory entry and every claim block has an entry; that every quotation the verdict relies on verifies as in REQ-polaris-generation-034; and that a verdict with an unresolved blocking finding does not declare the subject ready. A verdict that fails validation SHALL be recorded and SHALL NOT count as a review. Any revision of the subject or the inventory retires the verdicts bound to it.

The run record SHALL record, as operator-declared, the agent tool, version and session identifier of the authoring, inventory and review contexts, and Syzygy SHALL refuse a verdict whose declared session identifier equals that of the authoring context or of the inventory context it reviews. The record SHALL distinguish what Syzygy observed, which is the packet's exact contents and the verdict's binding to it, from what remains Inferred, which is that each context was fresh, that the review context saw nothing beyond its packet, that the inventory context did not see the draft, the session identifiers themselves, and the inventory's completeness over the clone. The review page SHALL disclose that distinction.

For a run in the operator-agent mode this requirement reads REQ-polaris-generation-006 as follows, and displaces only what it names: "Reviewers SHALL receive the artifact, governing references and acceptance criteria without the authoring conversation" is met by the packet rule above; the inventory "covering the entire admitted source population" is the inventory context's self-reported coverage of the clone at the pinned revision, labelled Inferred, and readiness SHALL NOT claim that coverage as verified; and the words "accounting for those calls in its run budget" read as the operator-declared limits of REQ-polaris-generation-033, which cover the inventory and review contexts. Every other sentence and scenario of REQ-polaris-generation-006, including the rule that unresolved material omissions prevent readiness, the fresh-reader review of RFC7-25 and the rule that the generator does not classify its own wording change as immaterial, is unchanged.

ID: REQ-polaris-generation-035
Source: VIS-3; governing warrants below.
Scope: v1-mandatory

#### Scenario: Review packet without the authoring exchange

- **WHEN** Syzygy emits a fidelity review packet for a frozen draft
- **THEN** the packet holds the frozen draft, the frozen inventory, the cited spans as Syzygy read them, the criteria and the verdict schema, and nothing else
- **AND** its digest is recorded in the run record

#### Scenario: Verdict bound to a stale packet

- **WHEN** a verdict names a packet digest other than the packet for the current frozen draft and inventory
- **THEN** Syzygy records the verdict and refuses to count it as a review
- **AND** readiness names the review still required

#### Scenario: Reviewer declared as the author

- **WHEN** the declared session identifier of a review context equals that of the authoring context, or of the inventory context it reviews
- **THEN** Syzygy refuses the verdict and records the refusal
- **AND** the page does not show the review as independent

#### Scenario: Verdict incomplete or inconsistent

- **WHEN** a verdict omits an inventory entry or a claim block, relies on a quotation that does not verify, or declares readiness with an unresolved blocking finding
- **THEN** validation fails, the verdict is recorded and does not count
- **AND** the draft does not become ready

#### Scenario: Independence disclosed as Inferred

- **WHEN** a validated verdict counts as the review of record
- **THEN** the review page states that the packet contents and the verdict's binding are Observed, and that the freshness of each context, the session identifiers and the inventory's completeness are Inferred
- **AND** no surface states the review's independence as Observed

#### Scenario: Inventory omission blocks readiness

- **WHEN** a validated verdict records a material inventory entry that the draft does not cover and that has no justified omission
- **THEN** the omission is a blocking finding and the draft does not become ready
- **AND** the finding names its deficient subject and reopens that artifact under REQ-polaris-generation-006

Form: lifecycle transition.

- **Case:** Run the review step against controlled frozen drafts, inventories and verdict files, varying the packet digest, the declared session identifiers, verdict completeness, quotation validity and finding severity independently.
- **Observable:** The emitted packets and their digests, the recorded verdicts, validation outcomes, readiness state and the review page's disclosures.
- **Oracle:** Expected packet contents, validation outcomes and readiness derived from the controlled inputs outside the generator; the packet compared byte for byte against an independently assembled expected packet.
- **Oracle independence:** Expected outcomes are fixed before the step runs; the verdict fixtures are written outside the code under test.
- **Falsifier:** A packet carries an authoring exchange, transcript or read account; a stale, self-reviewed, incomplete or inconsistent verdict counts; independence or inventory completeness is shown as Observed; a revision leaves an old verdict in force.

```yaml
warrants:
  primary: VIS-3
  doctrine: [VIS-1, VIS-2, VIS-3]
  contracts: [RFC7-9, RFC7-13, RFC7-25]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: [REQ-polaris-generation-006, REQ-polaris-generation-033, REQ-polaris-generation-034]
```

### Requirement: Self-reported discovery and in-session clarification

In the operator-agent mode the discovery account that REQ-polaris-generation-030 requires SHALL consist of two populations, kept distinct in human and machine form. The first is the agent's account of what it inspected and selected, with its reasons for material it excluded, could not resolve or deferred, and its stopping reason; Syzygy SHALL record and render it as self-reported and labelled Inferred, and SHALL NOT present it as complete, as verified, or as Observed. Syzygy SHALL report as findings the self-reported paths that name no blob at the pinned revision; a path that does exist does not make the account Observed. The second population is the set of Git objects Syzygy itself read for the run, each with its path, object identifier, pinned revision and classification and screening outcome, labelled Observed. Syzygy SHALL NOT derive an Observed not-read figure or an Observed coverage claim from the agent's account. REQ-polaris-generation-030's obligations on scope, supported profile, stopping reason, partial findings and narrower scopes apply to the agent's account as self-reported content.

The consequential questions of REQ-polaris-generation-031 SHALL be asked of the human operator within the agent session. The draft SHALL record each question with the evidence considered, the consequence for the draft, the interpretations offered, and the operator's answer as free text, a selected interpretation, leave-unknown or defer, attributed to the operator. Because Syzygy does not observe the exchange, the record SHALL be labelled as the agent's report of it. The number of questions SHALL NOT exceed the declared clarification-question limit of REQ-polaris-generation-033. Every other obligation of REQ-polaris-generation-031 is unchanged: an answer does not prove implementation behavior or adopt intent, unchanged questions reuse prior answers, a purpose left unknown stays unknown, and answer changes invalidate dependent content and reviews.

For a run in the operator-agent mode this requirement displaces exactly this predecessor text: in REQ-polaris-generation-030, the item "inspected and selected material" in the list the generator "SHALL expose" before claiming source coverage, read there as an account the generator itself produced, which becomes the two populations above; and in REQ-polaris-generation-031, "owner" as the person asked, which becomes the human operator of the run, whose answers are attributed to the operator. Every other sentence and scenario of REQ-polaris-generation-030 and 031 is unchanged.

ID: REQ-polaris-generation-036
Source: VIS-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Two read populations shown apart

- **WHEN** an operator-agent run is rendered
- **THEN** the discovery account shows the agent's self-reported inspected and selected material labelled Inferred, and Syzygy's own object reads with object identifiers and screening outcomes labelled Observed
- **AND** no figure on the page merges the two populations

#### Scenario: Self-reported path absent at the pinned revision

- **WHEN** the agent's account names a path that is not a blob at the pinned revision
- **THEN** Syzygy reports a finding for that path
- **AND** the remaining account stays labelled Inferred, not upgraded by the paths that exist

#### Scenario: No Observed not-read claim

- **WHEN** the agent's account omits part of the repository
- **THEN** no surface states as Observed that the omitted part was not read
- **AND** any not-read statement is shown as part of the agent's self-report

#### Scenario: Consequential question asked in-session

- **WHEN** the agent cannot establish the subject's purpose or another consequential premise from the clone
- **THEN** it asks the operator in-session and the draft records the question, the evidence, the consequence, the options and the operator's answer, attributed to the operator and labelled as the agent's report
- **AND** an answer neither proves implementation behavior nor adopts intent

#### Scenario: Question limit reached

- **WHEN** the declared clarification-question limit is reached with optional uncertainties remaining
- **THEN** the remaining questions are recorded as unasked and their facts stay explicit as unresolved in the affected reading
- **AND** a draft whose clarification record exceeds the limit fails the check

Form: event-response.

- **Case:** Submit controlled drafts whose discovery accounts and clarification records vary in existing and absent paths, omissions, answers, deferrals and question counts, against a fixture repository at a pinned commit.
- **Observable:** The rendered discovery account, its two populations and their labels, the findings, the clarification records and their attributions, and the human and machine outputs.
- **Oracle:** Expected labels, findings and populations derived from the fixture and the controlled drafts outside the generator; Syzygy's object reads captured independently of its own record.
- **Oracle independence:** Expected outcomes are fixed before the run; the self-reported accounts are fixture inputs, never expected truth.
- **Falsifier:** The agent's account is labelled Observed or presented as complete; the two populations are merged; an Observed not-read or coverage figure is derived from the self-report; a clarification answer adopts intent; the question limit is exceeded without a finding.

```yaml
warrants:
  primary: VIS-2
  doctrine: [SEC-2, VIS-1, VIS-2, VIS-4]
  contracts: [RFC2-24, RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: []
  topology: []
  parent_requirements: [REQ-polaris-generation-030, REQ-polaris-generation-031, REQ-polaris-generation-033]
```
