# Polaris dossier for an arbitrary public repository

Candidate exact behavioral delta; not adopted, binds nothing. This change applies to the existing polaris-generation capability. It adds three requirements to the operator-agent mode of REQ-polaris-generation-033 to 036: a standing admission for public repositories with a tree-based governed rule, reconstructed motivations, and, only if the owner reverses ruling 10b of the owner direction `REDIS-LOCAL-AGENT-SITTING-2026-10-07`, external comparisons as the agent's unverified report. It edits no byte of any predecessor requirement or scenario. For a run under the standing admission it reads the predecessor text that each requirement below names, and only that text; a run under a per-repository observation consent, Redis included, keeps every predecessor requirement and scenario with its bytes and its meaning, except where REQ-polaris-generation-038 says it applies to every operator-agent run. REQ-polaris-generation-037 also rests on an owner reading, or an amendment, of RFC1-3, RFC5-12 and RFC3-30 and of the doctrine sentence "Every observed repository consents, governance root or not." (`architecture.md`); this change cannot supply that reading, and the requirement is not satisfiable until the owner has recorded one.

## ADDED Requirements

### Requirement: Standing public-repository admission

In the operator-agent mode a run MAY rest its observation consent on the standing public-repository admission instead of on a per-repository observation consent. It SHALL do so only when every one of these holds, each established from the record of the owner act that makes it effective (RFC3-16), never from a status word or a file's presence: the standing admission record is in force; the owner's reading, or amendment, of RFC1-3, RFC5-12, RFC3-30 and the doctrine sentence quoted above, under which a standing admission instantiated per repository by a run's admission instance record is a recorded per-repository consent record, is in force; before the brief, the operator has declared the upstream URL of a public Git repository, the location of the operator's fork or clone, and a repository identity in the form the standing record fixes; the URL satisfies the standing record's host rule; no per-repository observation consent record exists for the pair (`project:syzygy`, that repository), whether in force, withdrawn or revoked; the repository is not a declared repository of any Syzygy project declaration; and the repository is not on the standing record's exclusion list. Where any of these fails, the run proceeds only under a per-repository observation consent, to which REQ-polaris-generation-033 applies unchanged, or is refused with its reason in human and machine form.

Before it issues the brief, Syzygy SHALL write, in the run's state directory, a run admission instance record that names: the consent class, observation; the subject, (`project:syzygy`, the declared repository identity); the scope, which is the pinned commit's commit object and the tree and blob objects reachable from its root tree, together with the ancestor commit objects reachable from it where, and only where, the standing record admits history; the granting principal, the owner, through the standing act, cited by its identity; the grant instant, which is the standing act's; the instance's own instant; the upstream URL and the fork or clone location, as configuration and never as repository identity (RFC1-2); and its revocation state, which follows the standing act. The pinned commit is the clone's checked-out HEAD commit at that instant. The instance record is not an owner act, adds no act and widens no consent; it is the per-repository record through which the standing act reaches one repository for one run. For a run under the standing admission, REQ-polaris-generation-033's "a revision that the in-force observation consent for the repository names" reads as the pinned commit that the run's instance record names, while the standing act is in force and the repository satisfies every condition above. At every later check, review check and render Syzygy SHALL establish those conditions again, and the withdrawal of the standing act or of the owner's reading, a new version of the standing record whose exclusion list names the repository, or a per-repository observation consent record for the pair, SHALL refuse every later step of the run. That the instance record was not altered after Syzygy wrote it is Inferred and disclosed, as for every stored record of the run (REQ-polaris-generation-033). For such a run, REQ-polaris-generation-025's "Each consent record SHALL grant exactly one class with subject, scope, granting principal, grant instant and revocation state: observation/write consent per repository" reads as met by the instance record, whose grant is the standing act's.

Syzygy SHALL make no network request to admit, pin or verify a run under the standing admission: it SHALL NOT contact the upstream host, the fork's host or any other service. That the repository is public, that the pinned commit is published at the upstream URL, and that the fork or clone reproduces it, are the operator's declarations, labelled Inferred and attributed to the operator. The standing admission grants only read-only reads of the objects the instance record's scope names, through the registered source-acquisition entry. It grants no egress, no write and no execution, and leaves REQ-polaris-generation-033's execution rule and D9 as they are; it covers no issue, pull request, CI log, release asset, submodule not vendored at the pinned commit, or other repository. Every object Syzygy reads SHALL be classified and screened under `project:syzygy`'s effective policies, the public-source screening scope included, exactly as for a per-repository consent (REQ-polaris-generation-025; SEC-5).

For a run under the standing admission, the drawer half of REQ-polaris-generation-033's governed predicate is stated by the standing record: no kernel evidence drawer exists for a repository admitted only under it, and the admitted project input (REQ-polaris-generation-001) carries that statement from the record. The subject SHALL be governed if, and only if, Syzygy's own listing of the tree at the pinned commit holds a path with a segment, at any depth, that equals `openspec` or `.syzygy` after Unicode NFKC normalisation, case folding and the removal of trailing dots and spaces; every listed entry counts, symbolic links and submodule entries included. This is never less strict than REQ-polaris-generation-033's predicate or than a root-only, exact-case match. A subject whose listing holds no such segment is non-governed. This one predicate decides both REQ-polaris-generation-033's governed predicate and the selection of REQ-polaris-generation-032's non-governed narrative profile; for such a run, 032's "admitted project input states that no kernel evidence drawer exists" reads as the standing record's statement, and 032's three inventory conditions read as the tree test above, which is never less strict than them. For a governed subject under the standing admission, Syzygy SHALL refuse to issue a brief unless an in-force per-project statement, as REQ-polaris-generation-033 defines it, names the run's declared agent tool and provider for that pair, and the refusal SHALL name the root entries found and that route; where the run proceeds, the narrative is composed under the governed readings of REQ-polaris-generation-004 and never under the non-governed profile. A non-governed subject under the standing admission needs no per-project statement, as REQ-polaris-generation-033 already provides.

The run record and every rendered page SHALL disclose, in human and machine form: the admission basis, standing or per-repository; for a standing run, the standing act's identity, the instance record's identity, the upstream URL, the fork or clone location and the pinned commit; that the repository's public status and the pinned commit's publication are operator-declared and Inferred; whether the standing record admits history; the governed determination and the paths it rests on; and that the records Syzygy read for these gates lie within the agent sessions' write reach. The repository identity, URL and location are labels beside the anchors, never their identity (RFC7-10).

ID: REQ-polaris-generation-037
Source: RFC5-12; governing warrants below.
Scope: v1-mandatory

#### Scenario: Public repository admitted without a per-repository act

- **WHEN** the standing admission and the owner's reading are in force, and the operator declares the upstream URL of a public repository on a permitted host, a fork location and a repository identity for which no per-repository consent record exists and which is neither declared in a Syzygy project nor excluded
- **THEN** Syzygy writes the run's admission instance record naming the clone's HEAD as the pinned commit, and issues the brief without any further owner act
- **AND** the run record and every page disclose the standing basis, the instance record, the URL, the fork location and the pinned commit, with the public status labelled Inferred and attributed to the operator

#### Scenario: Standing admission not available

- **WHEN** the standing record or the owner's reading is absent, withdrawn or has no owner-act record making it effective, or the URL fails the host rule, or the repository is excluded or declared in a Syzygy project
- **THEN** Syzygy refuses the run before issuing a brief and states the reason in human and machine form
- **AND** no object is read for the run

#### Scenario: Per-repository consent takes precedence

- **WHEN** a per-repository observation consent record exists for the pair, in force, withdrawn or revoked
- **THEN** the standing admission does not apply to that repository, and the run proceeds only under that record exactly as REQ-polaris-generation-033 states, or is refused
- **AND** a withdrawn per-repository consent is never replaced by the standing admission

#### Scenario: Standing act withdrawn mid-run

- **WHEN** after the brief, the standing act or the owner's reading is withdrawn, or a new version of the standing record excludes the repository
- **THEN** Syzygy refuses every later step of the run and states why
- **AND** the run's last checked state remains inspectable

#### Scenario: No network request to admit

- **WHEN** a run is admitted under the standing admission
- **THEN** an independent capture of Syzygy's process network activity shows no request to the upstream host, the fork's host or any other service
- **AND** the public status of the repository is shown as the operator's declaration, never as verified

#### Scenario: Governed by the pinned tree

- **WHEN** the listing of the pinned tree holds a path with an `openspec` or `.syzygy` segment, at the root or below it, in any case or Unicode form that folds to either name
- **THEN** the subject is governed, and without an in-force per-project statement naming the run's agent tool and provider Syzygy refuses the brief, naming the first paths found and the per-project statement as the route
- **AND** where such a statement is in force, the narrative is composed under the governed readings of REQ-polaris-generation-004, not the non-governed profile

#### Scenario: Non-governed without any per-repository record

- **WHEN** the listing of the pinned tree holds no path with either segment
- **THEN** Syzygy issues the brief without a per-project statement or a drawer statement, and composes the narrative under REQ-polaris-generation-032's non-governed profile
- **AND** the page states that the drawer statement comes from the standing record

#### Scenario: Instance record altered

- **WHEN** after the brief the instance record in the state directory is changed to name another commit, another repository or another scope
- **THEN** at the next step Syzygy refuses the step wherever the record no longer names the run's recorded pinned revision or the repository the run was admitted for, or a draft, inventory or verdict names a different revision, as REQ-polaris-generation-033 provides
- **AND** every value shown from the record is labelled Inferred, and no object outside the pinned commit's scope is quoted or rendered

#### Scenario: Redis keeps its own consent

- **WHEN** a run is started for `redis-redis`, whose per-repository observation consent and agent-provider statement are in force
- **THEN** the run proceeds under those records exactly as before this change, at the revisions that consent names
- **AND** the standing admission is not consulted, and the page states the per-repository basis

Form: event-response.

- **Case:** Start operator-agent runs against controlled clones and fixture records, varying independently: the standing record's presence, effect and exclusion list; the owner reading's presence and effect; the declared URL, host and identity; the presence and state of a per-repository consent record; a project declaration naming the repository; `openspec` and `.syzygy` segments at the root, nested, in other cases and in Unicode forms that fold to them; a per-project statement; and alterations of the instance record between steps. Capture Syzygy's process network activity independently.
- **Observable:** The refusals and their reasons, the instance record, the objects read, the governed determination, the profile selected, captured network effects, and the human and machine disclosures.
- **Oracle:** Expected admissions, refusals, governed determinations and profiles derived from the fixture records and an independent listing of each fixture's tree, prepared before the run.
- **Oracle independence:** Fixture records, trees and expected outcomes are written outside the code under test; network effects come from an independent capture, never Syzygy's own record.
- **Falsifier:** A run is admitted under the standing admission without the standing act, the owner's reading, or the operator's declarations; a repository with any per-repository consent record, a declared repository or an excluded one is admitted under it; Syzygy makes a network request to admit or verify; the public status is shown as verified or Observed; the instance record is presented as an owner act; a step proceeds after the standing act is withdrawn; a governed tree proceeds without a per-project statement or is composed under the non-governed profile; a nested, differently cased or Unicode-variant segment is not counted; an object outside the instance scope is read; or Redis's run changes in any respect.

```yaml
warrants:
  primary: RFC5-12
  doctrine: [SEC-2, SEC-3, SEC-5, VIS-1, VIS-2, VIS-4]
  contracts: [RFC1-2, RFC1-3, RFC3-16, RFC3-30, RFC5-12, RFC5-13, RFC5-16, RFC7-10]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05, POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05, REDIS-LOCAL-AGENT-SITTING-2026-10-07]
  topology: []
  parent_requirements: [REQ-polaris-generation-001, REQ-polaris-generation-004, REQ-polaris-generation-025, REQ-polaris-generation-032, REQ-polaris-generation-033]
```

### Requirement: Reconstructed motivations, trade-offs and position

In an operator-agent run, every claim block that states why the subject is built as it is (a motivation), what it gives up for what it gains (a trade-off), what it offers over alternatives (an advantage), or where it stands among alternatives (a position) SHALL declare exactly one basis, `maintainer-stated` or `reconstructed`. The agent marks the kind and the basis; Syzygy sees only the marking, and the page SHALL say that whether an unmarked block states one of the four kinds is the agent's report.

A `maintainer-stated` block SHALL carry at least one quotation, verified under REQ-polaris-generation-034, from text the subject's maintainers wrote: a source at the pinned revision that carries no generated-file marker of the run's frozen profile where one is recorded (REQ-polaris-generation-032 (a)), or, where the run's observation scope admits history, a commit message of a commit reachable from the pinned commit. Whether the quoted span states that motivation, trade-off, advantage or position is checked by the fidelity review, never by Syzygy.

A `reconstructed` block SHALL cite its premises and carry an evidence trail. Each premise is a citation that REQ-polaris-generation-034 checks: a repository path and line range at the pinned revision (code structure, tests, design comments, documentation) or, where the scope admits history, a commit object identifier with a line range of its message. The trail states, in the agent's words, the step from the premises to the claim. Syzygy SHALL render a reconstructed block Inferred, with a marker in human and machine form stating that it is reconstructed from the repository and is not the authors' stated intent, and with its trail and premises one step away. A reconstructed block SHALL NOT be written in the first person, SHALL NOT attribute an intention, wish or decision to the authors as their statement, SHALL NOT place quotation marks around text that is not a verified quotation, and SHALL NOT state an advantage over, or a position relative to, a named other project unless a verified maintainer quotation names it or REQ-polaris-generation-039 is in force. A motive about persons, organisations or their circumstances, rather than about the design, without a maintainer-stated basis SHALL remain absent or Unknown.

Where a maintainer-stated block and a reconstructed block address the same point and disagree, both SHALL render, the disagreement SHALL enter the understanding record's contradictory accounts, and the reconstruction SHALL NOT displace the statement. Under ruling 10b of the owner direction `REDIS-LOCAL-AGENT-SITTING-2026-10-07`, an advantage is maintainer-stated only: a block of the advantage kind with a `reconstructed` basis fails the check, unless the owner has reversed that ruling and REQ-polaris-generation-039 is in force.

Syzygy SHALL report as repair findings: a block of the four kinds without exactly one basis; a maintainer-stated block without a verified maintainer quotation; a reconstructed block with no premise, an unverifiable premise, no trail, or a named comparison the rules above forbid; and a commit-message citation where the scope admits no history. The fidelity verdict (REQ-polaris-generation-035) SHALL record, for every block of the four kinds, whether its quotation states what the block claims or its trail supports it from its premises, and an unsupported block is a blocking finding whose deficient subject is the argument.

For an operator-agent run this requirement reads exactly this predecessor text: in REQ-polaris-generation-034, the reader topic "maintainer-stated advantages and trade-offs", read as maintainer-stated advantages together with motivations, trade-offs and position, each maintainer-stated or reconstructed under this requirement, and the citation rule "every Inferred block SHALL cite at least one source as a repository path and an inclusive line range at the pinned revision", which a commit-message citation also satisfies where the scope admits history; and in REQ-polaris-generation-002, "Motives, history, definitions and relationships without sufficient source premises SHALL remain absent or Unknown", where the sufficient premises of a reconstructed motive are its checked premises together with a counted fidelity verdict that its trail supports it. Every other sentence and scenario of REQ-polaris-generation-002, 004 and 034 is unchanged, including "an Inferred label alone SHALL NOT make speculation eligible" and the rule that generated prose SHALL NOT impersonate an author.

ID: REQ-polaris-generation-038
Source: VIS-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Maintainer text anchors the motivation

- **WHEN** a design note or source comment at the pinned revision states why a mechanism exists, and the draft quotes it under a maintainer-stated block
- **THEN** the block renders with the verified quotation as its Observed anchor and the claim Inferred
- **AND** the fidelity verdict records that the span states the motivation

#### Scenario: Motivation reconstructed from code and tests

- **WHEN** no maintainer text states why a mechanism exists, and the draft carries a reconstructed block citing the code paths and tests it rests on, with a trail
- **THEN** the block renders Inferred with the marker that it is reconstructed and is not the authors' stated intent, and its trail and premises one step away
- **AND** no surface presents it as the authors' statement or as Observed

#### Scenario: Reconstruction without premises or trail

- **WHEN** a reconstructed block cites no premise, cites a path absent at the pinned revision, or carries no trail
- **THEN** Syzygy reports a repair finding naming the block and what is missing
- **AND** the draft does not proceed to review until a resubmitted revision passes

#### Scenario: Statement and reconstruction disagree

- **WHEN** a maintainer-stated block and a reconstructed block about the same design point disagree
- **THEN** both render, and the understanding record lists the disagreement among its contradictory accounts
- **AND** the reconstruction does not replace or soften the maintainers' statement

#### Scenario: Reconstructed advantage while ruling 10b stands

- **WHEN** ruling 10b is in force unreversed and a draft block of the advantage kind has a reconstructed basis, or a reconstructed block claims an advantage over a named other project that no verified maintainer quotation names
- **THEN** Syzygy reports a repair finding for that block
- **AND** a maintainer-stated advantage with a verified quotation passes

#### Scenario: Motive about people stays Unknown

- **WHEN** a block attributes a motive to the authors' circumstances, employer or commercial aims and has no maintainer-stated basis
- **THEN** the fidelity verdict records a blocking finding and the claim renders absent or Unknown
- **AND** an Inferred label alone does not make it eligible

#### Scenario: History premise without history in scope

- **WHEN** a reconstructed block cites a commit message and the run's observation scope does not admit history
- **THEN** Syzygy reports a repair finding for that citation
- **AND** where the scope admits history, the same citation to a commit reachable from the pinned commit verifies against the commit object Syzygy read and re-hashed

#### Scenario: Unsupported trail blocks readiness

- **WHEN** a validated fidelity verdict records that a reconstructed block's trail does not support its claim from its premises
- **THEN** the finding is blocking and the draft does not become ready
- **AND** the finding names the argument as its deficient subject

Form: event-response.

- **Case:** Submit controlled drafts against a fixture repository at a pinned commit, varying each block's kind, basis, quotations, premises, trail, named comparisons and commit-message citations, with history admitted and not admitted, ruling 10b reversed and not, and fidelity verdicts that support and do not support each block.
- **Observable:** The repair findings, the rendered blocks with their labels, markers, trails and anchors in human and machine form, the understanding record, the verdict validation and the readiness state.
- **Oracle:** Expected findings, labels, markers and readiness fixed in the fixture before the run, from the fixture blobs and commit objects read by an independent Git implementation.
- **Oracle independence:** The drafts and verdicts are fixture inputs written outside the code under test; the expected outcomes are not derived from the checker's output.
- **Falsifier:** A reconstructed block renders without its marker, trail or premises, or as Observed or as the authors' statement; a block of the four kinds passes without exactly one basis; a maintainer-stated block passes without a verified maintainer quotation; a reconstructed advantage passes while ruling 10b stands unreversed; a motive about people renders as a claim without a maintainer-stated basis; a commit-message citation passes without history in scope; a disagreement between statement and reconstruction is hidden; or a draft becomes ready with an unsupported reconstruction.

```yaml
warrants:
  primary: VIS-2
  doctrine: [VIS-1, VIS-2, VIS-3]
  contracts: [RFC2-24, RFC7-2, RFC7-10, RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [REDIS-LOCAL-AGENT-SITTING-2026-10-07]
  topology: []
  parent_requirements: [REQ-polaris-generation-002, REQ-polaris-generation-004, REQ-polaris-generation-032, REQ-polaris-generation-034, REQ-polaris-generation-035]
```

### Requirement: External comparisons as the agent's unverified report

This requirement has effect only while an owner ruling reversing ruling 10b of the owner direction `REDIS-LOCAL-AGENT-SITTING-2026-10-07` is in force, established from the record of the owner's act or direction that makes it (RFC3-16). Without it, a draft block that rests on a source outside the clone SHALL fail the check as a repair finding, and advantages stay maintainer-stated only.

While the ruling is in force, a draft MAY carry external-comparison blocks: claims about the subject relative to named other projects that rest on sources outside the clone, such as web pages, papers or other repositories, that the agent reports having read. Syzygy SHALL NOT fetch, read or verify any external source, and SHALL NOT render any external text as a quotation. Each external-comparison block SHALL be labelled Inferred, SHALL carry a marker in human and machine form stating that it is the agent's unverified report of external sources, and SHALL list each source as the agent reports it (a title, an address and the date the agent reports reading it) as presentation labels, never as an anchor, an evidence identifier or a source page. These blocks SHALL render together in one section of the dossier, apart from the claims anchored in the clone, and SHALL NOT appear in the opening or the concise account or discharge any reading-depth obligation of REQ-polaris-generation-004. The fidelity verdict SHALL record each such block as unverifiable from its packet and SHALL NOT count it as supported. The run record and the section SHALL disclose that the agent's reads of external sources, and any transmission they involved, were the operator's own act, outside Syzygy's consent records and not observed by Syzygy.

ID: REQ-polaris-generation-039
Source: VIS-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: External comparison while 10b is reversed

- **WHEN** the owner's reversal of ruling 10b is in force and a draft block compares the subject with a named other project, citing a web page the agent reports reading
- **THEN** the block renders Inferred in the external-comparison section with the unverified-report marker and the source as a label
- **AND** no anchor, source page or Observed quotation is rendered for the external source, and Syzygy made no request for it

#### Scenario: External comparison while 10b stands

- **WHEN** no reversal of ruling 10b is in force and a draft block rests on a source outside the clone
- **THEN** Syzygy reports a repair finding for that block
- **AND** the draft does not proceed to review until a resubmitted revision passes

#### Scenario: External comparison kept out of the primary reading

- **WHEN** a draft places an external-comparison block in the opening or the concise account, or presents it as a maintainer-stated advantage
- **THEN** Syzygy reports a repair finding
- **AND** the reading-depth obligations are judged without that block

Form: event-response.

- **Case:** Submit controlled drafts with and without external-comparison blocks, placed in and out of their section, with the owner's reversal of ruling 10b in force, absent and withdrawn, and capture Syzygy's network activity independently.
- **Observable:** The repair findings, the rendered section, labels, markers and source labels, the verdict records, captured network effects and the disclosures.
- **Oracle:** Expected findings and renderings fixed in the fixture before the run; network effects from an independent capture.
- **Oracle independence:** Drafts, rulings and expected outcomes are fixture inputs written outside the code under test.
- **Falsifier:** An external-comparison block passes while 10b stands; Syzygy requests an external source; an external source renders as an anchor, a source page, a quotation or Observed; a block appears in the opening or concise account or discharges a reading-depth obligation; a verdict counts an external block as supported; or the operator's-own-act disclosure is absent.

```yaml
warrants:
  primary: VIS-2
  doctrine: [SEC-2, VIS-1, VIS-2, VIS-4]
  contracts: [RFC3-16, RFC7-10, RFC7-20]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [REDIS-LOCAL-AGENT-SITTING-2026-10-07]
  topology: []
  parent_requirements: [REQ-polaris-generation-004, REQ-polaris-generation-034, REQ-polaris-generation-035, REQ-polaris-generation-038]
```
