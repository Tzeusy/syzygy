# Polaris dossier for an arbitrary public repository

Candidate exact behavioral delta; not adopted, binds nothing. This change applies to the existing polaris-generation capability. It adds three requirements to the operator-agent mode of REQ-polaris-generation-033 to 036: a standing public-observation consent with a tree-based governed rule (037), reconstructed motivations (038), and, only if the owner reverses ruling 10b of the owner direction `REDIS-LOCAL-AGENT-SITTING-2026-10-07`, external comparisons as the agent's unverified report (039). It edits no byte of any predecessor requirement or scenario. For a run under the standing consent it reads the predecessor text that REQ-polaris-generation-037 names, and only that text. A run under a per-repository observation consent, Redis included, keeps its admission basis, consent, statements, pinned revisions and every predecessor requirement as they are, except that REQ-polaris-generation-038 applies to every operator-agent run; whether it should apply to Redis's runs is an owner question, and if the owner rules that it should not, 038's first sentence is narrowed to runs under the standing consent before sign-off. REQ-polaris-generation-037 is an amendment in substance of adopted doctrine and of accepted contracts, not a reading of them. It admits no run until a doctrine amendment of `architecture.md` and a contract amendment of RFC1-2, RFC1-3, RFC1-4, RFC3-6, RFC3-7, RFC3-30 and RFC5-12, drafted as semantic deltas in this change's `AMENDMENTS.md`, are in force by the owner's own acts. Reading the history of the pinned commit is not part of this change unless the owner chooses it; where the standing record does not admit history, every read stays at the pinned revision exactly as REQ-polaris-generation-033 states.

## ADDED Requirements

### Requirement: Standing public-observation consent

In the operator-agent mode a run MAY rest its observation consent on the observing project's standing public-observation consent instead of on a per-repository observation consent. It SHALL do so only when every one of these holds, each established from the record of the owner act that makes it effective (RFC3-16), never from a status word or a file's presence: the standing public-observation consent record, a governance act stored in `.syzygy/governance/decisions/`, is in force; the doctrine amendment of `architecture.md` and the contract amendment of RFC1-2, RFC1-3, RFC1-4, RFC3-6, RFC3-7, RFC3-30 and RFC5-12 that define that consent are in force; before the brief, the operator has declared the upstream URL of a public Git repository, the location of the operator's fork or clone, a repository identity in the form the standing record fixes, and that the pinned commit is published in that public repository; the URL satisfies the standing record's host rule; and no exclusion below applies. Where any of these fails, the run proceeds only under a per-repository observation consent, to which REQ-polaris-generation-033 applies unchanged, or is refused with its reason in human and machine form. This requirement states no reading of the current texts of those clauses: until the amendments are in force, the standing route admits nothing.

Before it issues the brief, Syzygy SHALL write, in the run's state directory, a run admission entry that names: the consent class, observation; the subject, (`project:syzygy`, the declared repository identity); the scope, which is the pinned commit's commit object and the tree and blob objects reachable from its root tree, together with the ancestor commit objects reachable from it where, and only where, the standing record admits history; the standing consent record it rests on, by identity; the grant instant, which is the standing act's; the record's own instant; the upstream URL and the fork or clone location, as locator hints and never as repository identity; and its revocation state, which follows the standing consent. The pinned commit is the clone's checked-out HEAD commit at that instant. The admission entry is how the standing consent reaches one repository for one run, as amended RFC5-12 defines it; it is not an owner act or a consent record, grants nothing of its own and is not a governance act. For a run under the standing consent, REQ-polaris-generation-033's "a revision that the in-force observation consent for the repository names" reads as the pinned commit that the run's admission entry names, while the standing consent is in force and no exclusion applies, and REQ-polaris-generation-025's "Each consent record SHALL grant exactly one class with subject, scope, granting principal, grant instant and revocation state: observation/write consent per repository" reads as met by the standing consent record together with the run's admission entry, as amended RFC5-12 provides. At every later check, review check and render Syzygy SHALL establish every condition again; the withdrawal of the standing consent or of either amendment, a new version of the standing record whose exclusions catch the run, or a per-repository observation consent record that catches it under the exclusions below, SHALL refuse every later step of the run. That the admission entry was not altered after Syzygy wrote it is Inferred and disclosed, as for every stored record of the run (REQ-polaris-generation-033).

The standing route SHALL NOT apply, and Syzygy SHALL refuse it with its reason, when any of these holds, whatever identity the operator declared:

- a per-repository observation consent record exists, in any state (in force, withdrawn or revoked), whose subject names the declared identity;
- the pinned commit, any parent commit identifier recorded in the pinned commit object, or, where history is admitted, any commit reachable from the pinned commit, equals a revision named by any per-repository observation consent record in any state, or a commit identifier on the standing record's exclusion list;
- the declared upstream URL, after normalisation (scheme and host lower-cased, user information, a default port, a trailing `/` and a trailing `.git` removed), equals the normalised upstream or locator hint of any per-repository observation consent record in any state, of any repository entry in any Syzygy project declaration, or of any URL on the exclusion list;
- the declared identity is on the exclusion list or names a repository entry of any Syzygy project declaration.

The exclusion list SHALL be able to carry identities, URLs and commit identifiers. Every comparison above is made from records Syzygy holds and objects in the local clone, with no network request. A repository whose pinned commit, the parents it records and its normalised URL overlap none of these, for example another commit of a repository whose per-repository consent was withdrawn, reached through a mirror URL under a new identity, is told apart from the excluded repository only by the operator's declaration; Syzygy SHALL disclose that residual on every page, labelled Inferred.

Syzygy SHALL make no network request to admit, pin or verify a run under the standing consent: it SHALL NOT contact the upstream host, the fork's host or any other service. Where the standing record does not admit history, the clone SHALL hold the pinned commit alone: its object store SHALL name no commit other than the pinned commit and no object outside the pinned commit's tree, and, where the pinned commit records parents, the clone's shallow boundary SHALL be exactly the pinned commit; a clone that holds anything more SHALL be refused before the brief. A commit made locally on top of a fetched public commit is therefore refused. A commit authored locally with no public counterpart cannot be told apart from a published one without a network request; that the pinned commit is published at the upstream URL, that the repository is public, and that the fork or clone reproduces it, are the operator's declarations, labelled Inferred and attributed to the operator. The standing consent grants only read-only reads of the objects the admission entry's scope names, through the registered source-acquisition entry. It grants no egress and no write; it covers no issue, pull request, CI log, release asset, submodule not vendored at the pinned commit, or other repository. Every object Syzygy reads SHALL be classified and screened under `project:syzygy`'s effective policies, the public-source screening scope included, exactly as for a per-repository consent (REQ-polaris-generation-025; SEC-5).

Where, and only where, the standing record admits history, Syzygy MAY read the ancestor commit objects of the pinned commit, each reached by a parent link from the pinned commit or from an ancestor already read and verified, and each re-hashed under the hash algorithm of the pinned commit's identifier; it SHALL NOT read an ancestor's tree or blob. For such a run this requirement reads REQ-polaris-generation-033's sentence "Every read Syzygy makes for the run SHALL be a Git object read by object identifier at the pinned revision through the registered observer, never a read of the working tree" as also admitting those ancestor commit objects; its sentence "Syzygy SHALL recompute the object identifier of every commit, tree and blob it reads on the path from the pinned commit to each blob it uses" as also applying to every ancestor commit object on the parent path from the pinned commit; and its falsifier arm "an object is read from the working tree or at another commit" as not reached by those ancestor commit objects, while every other object at another commit still falsifies it. The clone shape above then admits those ancestor commits and no other object. Syzygy SHALL withhold the author and committer lines of every commit object, and any signature it carries, before classification: they SHALL NOT be stored, rendered, quoted or placed in a review packet, and each withholding SHALL be recorded hash-not-body (RFC5-17). Only the message text of an ancestor commit is classified, screened and available for citation. Rendering author or committer identities needs its own owner act on the privacy posture and is not part of this requirement.

Under the standing consent, Syzygy SHALL refuse to record the owner's execution choice of REQ-polaris-generation-033 unless the standing record states that an execution choice may be recorded for runs under it; where it may not, every brief carries SEC-3's rule in the form REQ-polaris-generation-033 gives it. Where the standing record permits it, REQ-polaris-generation-033's execution rule applies unchanged, and the run record SHALL quote D9's cost as REQ-polaris-generation-033 requires.

For a run under the standing consent, the drawer half of REQ-polaris-generation-033's governed predicate is stated by the standing record: no kernel evidence drawer exists for a repository observed only under it. That statement is the owner's, made in advance for every such repository, and the admitted project input (REQ-polaris-generation-001) carries it from the record; its truth for a given repository is Inferred from the exclusions above, and the page SHALL label it so. The subject SHALL be governed if, and only if, Syzygy's own listing of the tree at the pinned commit holds a path with a segment, at any depth, that equals `openspec` or `.syzygy` after Unicode NFKC normalisation, case folding and the removal of trailing dots and spaces; every listed entry counts, symbolic links and submodule entries included. This is never less strict than REQ-polaris-generation-033's predicate or than a root-only, exact-case match. Segments that a case-insensitive or ignorable-folding filesystem would resolve to either name but that this fold does not reach (default-ignorable code points within the segment, a trailing tab, an NTFS stream suffix or an 8.3 short name) are not counted; Syzygy SHALL disclose that residual on the governed determination, labelled Inferred. This one predicate decides both REQ-polaris-generation-033's governed predicate and the selection of REQ-polaris-generation-032's non-governed narrative profile; for such a run, 032's "admitted project input states that no kernel evidence drawer exists" reads as the standing record's statement, and 032's three inventory conditions read as the tree test above, which is never less strict than them. For a governed subject under the standing consent, Syzygy SHALL refuse to issue a brief unless an in-force per-project statement, as REQ-polaris-generation-033 defines it, names the run's declared agent tool and provider for that pair, and the refusal SHALL name the first paths found and that route; where the run proceeds, the narrative is composed under the governed readings of REQ-polaris-generation-004 and never under the non-governed profile. A non-governed subject under the standing consent needs no per-project statement, as REQ-polaris-generation-033 already provides.

The run record and every rendered page SHALL disclose, in human and machine form: the admission basis, standing or per-repository; for a standing run, the standing consent's identity, the admission entry's identity, the upstream URL, the fork or clone location and the pinned commit; that the repository's public status and the pinned commit's publication are operator-declared and Inferred; the identity residual of the exclusions; whether history is admitted, and that commit author and committer lines are withheld; whether an execution choice may be recorded; the governed determination, the paths it rests on and its folding residual; that the drawer statement is the owner's statement made in advance, its truth Inferred; and that the records Syzygy read for these gates lie within the agent sessions' write reach. The repository identity, URL and location are labels beside the anchors, never their identity (RFC7-10).

ID: REQ-polaris-generation-037
Source: RFC5-12; governing warrants below.
Scope: v1-mandatory

#### Scenario: Public repository admitted without a per-repository act

- **WHEN** the standing consent and both amendments are in force, and the operator declares the upstream URL of a public repository on a permitted host, a fork location, an identity and the pinned commit's publication, and no exclusion applies
- **THEN** Syzygy writes the run's admission entry naming the clone's HEAD as the pinned commit, and issues the brief without any further owner act
- **AND** the run record and every page disclose the standing basis, the admission entry, the URL, the fork location and the pinned commit, with the public status and publication labelled Inferred and attributed to the operator

#### Scenario: Standing route not available

- **WHEN** the standing consent or either amendment is absent, withdrawn or has no owner-act record making it effective, or the operator has not declared publication, or the URL fails the host rule
- **THEN** Syzygy refuses the run before issuing a brief and states the reason in human and machine form
- **AND** no object is read for the run

#### Scenario: Per-repository consent under the same identity

- **WHEN** a per-repository observation consent record whose subject names the declared identity exists, in force, withdrawn or revoked
- **THEN** the standing route does not apply, and the run proceeds only under that record exactly as REQ-polaris-generation-033 states, or is refused
- **AND** a withdrawn per-repository consent is never replaced by the standing consent

#### Scenario: Withdrawn consent under a different identity

- **WHEN** the operator declares a new identity and an unrelated URL, and the pinned commit equals a revision named by a per-repository observation consent record that has been withdrawn
- **THEN** Syzygy refuses the standing route and names the matching revision and record
- **AND** no object is read for the run

#### Scenario: Parent commit names a consented revision

- **WHEN** the pinned commit is not named by any consent record, but a parent identifier recorded in the pinned commit object equals a revision a per-repository consent record names, in any state, or a commit on the exclusion list
- **THEN** Syzygy refuses the standing route and names the matching parent
- **AND** the parent object itself is not read

#### Scenario: Matching URL under a different identity

- **WHEN** the declared identity is new, but the declared URL normalises to the upstream of a per-repository consent record in any state, a locator hint of a repository in a Syzygy project declaration, or a URL on the exclusion list
- **THEN** Syzygy refuses the standing route and names the matching record or declaration
- **AND** the comparison is made with no network request

#### Scenario: Excluded or declared repository under its own name

- **WHEN** the declared identity is on the exclusion list or names a repository entry of a Syzygy project declaration
- **THEN** Syzygy refuses the standing route and states which
- **AND** the repository keeps whatever per-repository consent it has

#### Scenario: Unrelated commit and URL under a new identity

- **WHEN** the pinned commit, the parents it records and the normalised URL overlap no consent record, declaration or exclusion
- **THEN** the standing route applies
- **AND** every page states that the repository is told apart from excluded and withdrawn repositories only by the operator's declaration, labelled Inferred

#### Scenario: Local commit on top of a public commit

- **WHEN** the standing record does not admit history and the clone holds a commit made locally on top of the fetched commit, or any object outside the pinned commit's tree
- **THEN** Syzygy refuses the run before issuing a brief and names the extra objects
- **AND** a single locally authored commit with no public counterpart is admitted only on the operator's declaration of publication, labelled Inferred

#### Scenario: Ancestor read without history admitted

- **WHEN** the standing record does not admit history and any step would read a commit other than the pinned commit
- **THEN** the step is refused, as REQ-polaris-generation-033 provides
- **AND** a draft citation of a commit message fails the check

#### Scenario: Ancestor commits read with history admitted

- **WHEN** the standing record admits history and a check reads an ancestor commit reached by parent links from the pinned commit
- **THEN** Syzygy re-hashes each commit on the parent path, reads no ancestor tree or blob, and withholds every author, committer and signature line, recording each withholding hash-not-body
- **AND** no author or committer name or address is stored, rendered, quoted or placed in a review packet

#### Scenario: Execution choice under the standing consent

- **WHEN** the operator tries to record an execution choice for a run under the standing consent and the standing record does not permit one
- **THEN** Syzygy refuses to record it, and the brief carries SEC-3's rule in the form REQ-polaris-generation-033 gives it
- **AND** where the standing record permits it, REQ-polaris-generation-033's execution rule applies unchanged and the run record quotes D9's cost

#### Scenario: Standing consent withdrawn mid-run

- **WHEN** after the brief, the standing consent or either amendment is withdrawn, or a new version of the standing record excludes the repository by identity, URL or commit
- **THEN** Syzygy refuses every later step of the run and states why
- **AND** the run's last checked state remains inspectable

#### Scenario: No network request to admit

- **WHEN** a run is admitted under the standing consent
- **THEN** an independent capture of Syzygy's process network activity shows no request to the upstream host, the fork's host or any other service
- **AND** the public status of the repository is shown as the operator's declaration, never as verified

#### Scenario: Governed by the pinned tree

- **WHEN** the listing of the pinned tree holds a path with an `openspec` or `.syzygy` segment, at the root or below it, in any case or Unicode form that the fold reaches
- **THEN** the subject is governed, and without an in-force per-project statement naming the run's agent tool and provider Syzygy refuses the brief, naming the first paths found and the per-project statement as the route
- **AND** where such a statement is in force, the narrative is composed under the governed readings of REQ-polaris-generation-004, not the non-governed profile

#### Scenario: Non-governed without any per-repository record

- **WHEN** the listing of the pinned tree holds no path with either segment
- **THEN** Syzygy issues the brief without a per-project statement or a per-repository drawer statement, and composes the narrative under REQ-polaris-generation-032's non-governed profile
- **AND** the page states that the drawer statement is the owner's, made in advance in the standing record, with its truth for this repository Inferred, and states the fold's residual

#### Scenario: Admission entry altered

- **WHEN** after the brief the admission entry in the state directory is changed to name another commit, another repository or another scope
- **THEN** at the next step Syzygy refuses the step wherever the record no longer names the run's recorded pinned revision or the repository the run was admitted for, or a draft, inventory or verdict names a different revision, as REQ-polaris-generation-033 provides
- **AND** every value shown from the record is labelled Inferred, and no object outside the pinned commit's scope is quoted or rendered

#### Scenario: Redis keeps its own admission

- **WHEN** a run is started for `redis-redis`, whose per-repository observation consent and agent-provider statement are in force
- **THEN** the run proceeds under those records at the revisions that consent names, and the standing consent is not consulted
- **AND** its admission basis, consent, statements and pinned revisions are those it had before this change, and the page states the per-repository basis

Form: event-response.

- **Case:** Start operator-agent runs against controlled clones and fixture records, varying independently: the standing record's presence, effect, host rule, history and execution fields and exclusion list (identities, URLs and commits); each amendment's presence and effect; the declared URL, host, identity and publication; per-repository consent records in every state, with matching and non-matching identities, revisions and upstreams; project declarations with matching identities and locator hints; pinned commits whose recorded parents match a consented revision; clones holding an extra local commit or extra objects; `openspec` and `.syzygy` segments at the root, nested, in other cases, in Unicode forms the fold reaches and in forms it does not; a per-project statement; an execution choice; ancestor commits with author, committer and signature lines; and alterations of the admission entry between steps. Capture Syzygy's process network activity independently.
- **Observable:** The refusals and their reasons, the admission entry, the objects read and withheld, the governed determination, the profile selected, the recorded execution rule, captured network effects, and the human and machine disclosures.
- **Oracle:** Expected admissions, refusals, matches, governed determinations and profiles derived from the fixture records and an independent listing of each fixture's object store and tree, prepared before the run.
- **Oracle independence:** Fixture records, trees and expected outcomes are written outside the code under test; network effects come from an independent capture, never Syzygy's own record.
- **Falsifier:** A run is admitted under the standing route without the standing consent, either amendment or the operator's declarations; a run is admitted whose declared identity, pinned commit, recorded parent, reachable ancestor or normalised URL matches a per-repository consent record in any state, a declared repository or an exclusion; the identity residual is undisclosed; Syzygy makes a network request to admit or verify; the public status or publication is shown as verified or Observed; the admission entry is presented as an owner act or a grant; a clone holding a local commit on top of the fetched one, or an object outside the pinned tree, is admitted where history is not admitted; an ancestor commit is read where history is not admitted, or an ancestor tree or blob is read where it is; an author, committer or signature line is stored, rendered, quoted or packeted; an execution choice is recorded where the standing record does not permit one; a step proceeds after the standing consent or an amendment is withdrawn; a governed tree proceeds without a per-project statement or is composed under the non-governed profile; a segment the fold reaches is not counted, or the fold's residual is undisclosed; the drawer statement is presented as Observed; an object outside the admission entry's scope is read; or Redis's admission basis, consent, statements or pinned revisions change.

```yaml
warrants:
  primary: RFC5-12
  doctrine: [SEC-2, SEC-3, SEC-5, VIS-1, VIS-2, VIS-4]
  contracts: [RFC1-2, RFC1-3, RFC1-4, RFC3-6, RFC3-7, RFC3-16, RFC3-30, RFC5-12, RFC5-13, RFC5-16, RFC5-17, RFC7-10]
  policies: [CC-SPEC-2, CC-SPEC-4]
  decisions: [POLARIS-DOSSIER-LOCAL-AGENT-MODE-2026-10-05, POLARIS-DOSSIER-LOCAL-AGENT-SCOPE-REVIEW-SIGNOFF-2026-10-05, REDIS-LOCAL-AGENT-SITTING-2026-10-07]
  topology: []
  parent_requirements: [REQ-polaris-generation-001, REQ-polaris-generation-004, REQ-polaris-generation-025, REQ-polaris-generation-032, REQ-polaris-generation-033]
```

### Requirement: Reconstructed motivations, trade-offs and position

In every operator-agent run, Redis's included, every claim block that states why the subject is built as it is (a motivation), what it gives up for what it gains (a trade-off), what it offers over alternatives (an advantage), or where it stands among alternatives (a position) SHALL declare exactly one basis, `maintainer-stated` or `reconstructed`. The agent marks the kind and the basis; Syzygy's mechanical checks see only the marking, and the fidelity review, below, classifies every Inferred block whether or not it is marked.

A `maintainer-stated` block SHALL carry at least one quotation, verified under REQ-polaris-generation-034, from text that is Inferred to be the subject's maintainers' own from its location: a source at the pinned revision that carries no generated-file marker of the run's frozen profile where one is recorded (REQ-polaris-generation-032 (a)) and that does not lie under a path the run's frozen profile classes as vendored or third-party, or, where the run's observation scope admits history, a commit message of a commit reachable from the pinned commit. Text under a vendored or third-party path, and text the frozen profile cannot place on either side, is not maintainer-stated; it MAY serve as a premise of a reconstructed block. That a quotation is the maintainers' own is Inferred from its location and SHALL be labelled so. Whether the quoted span is maintainer text and whether it states that motivation, trade-off, advantage or position are checked by the fidelity review, never by Syzygy.

A `reconstructed` block SHALL cite its premises and carry an evidence trail. Each premise is a citation that REQ-polaris-generation-034 checks: a repository path and line range at the pinned revision (code structure, tests, design comments, documentation) or, where the scope admits history, a commit object identifier with a line range of its message. The trail states, in the agent's words, the step from the premises to the claim. Syzygy SHALL render a reconstructed block Inferred, with a marker in human and machine form stating that it is reconstructed from the repository and is not the authors' stated intent, and with its trail and premises one step away. A reconstructed block SHALL NOT state an advantage over, or a position relative to, a named other project unless a verified maintainer-stated quotation names it or REQ-polaris-generation-039 is in force. No block, of any kind or basis, marked or unmarked, SHALL be written in the first person as the authors, SHALL attribute an intention, wish or decision to the authors as their statement unless it is a maintainer-stated block whose quotation states it, or SHALL place quotation marks around text that is not a verified quotation. A motive about persons, organisations or their circumstances, rather than about the design, without a maintainer-stated basis SHALL remain absent or Unknown.

Where a maintainer-stated block and a reconstructed block address the same point and disagree, both SHALL render, the disagreement SHALL enter the understanding record's contradictory accounts, and the reconstruction SHALL NOT displace the statement. Under ruling 10b of the owner direction `REDIS-LOCAL-AGENT-SITTING-2026-10-07`, an advantage is maintainer-stated only: a block of the advantage kind with a `reconstructed` basis fails the check, unless the owner has reversed that ruling and REQ-polaris-generation-039 is in force.

Syzygy SHALL report as repair findings: a marked block of the four kinds without exactly one basis; a maintainer-stated block without a verified quotation from a source that is neither generated nor vendored or third-party by the frozen profile; a reconstructed block with no premise, an unverifiable premise, no trail, or a named comparison the rules above forbid; and a commit-message citation where the scope admits no history. The fidelity verdict (REQ-polaris-generation-035) SHALL classify every Inferred block of the draft, marked or not, as stating or not stating a motivation, trade-off, advantage or position. A block it classifies as one of the four kinds that carries no basis, or a block that attributes an intention to the authors without a maintainer-stated quotation that states it, is a blocking finding whose deficient subject is the marking. For every block of the four kinds the verdict SHALL also record whether a maintainer-stated quotation is maintainer text and states what the block claims, or whether a reconstructed block's trail supports it from its premises; an unsupported block is a blocking finding whose deficient subject is the argument.

For an operator-agent run this requirement reads exactly this predecessor text: in REQ-polaris-generation-034, the reader topic "maintainer-stated advantages and trade-offs", read as maintainer-stated advantages together with motivations, trade-offs and position, each maintainer-stated or reconstructed under this requirement, and the citation rule "every Inferred block SHALL cite at least one source as a repository path and an inclusive line range at the pinned revision", which a commit-message citation also satisfies where the scope admits history; in REQ-polaris-generation-035, the verdict's contents, which gain the classification and findings above; and in REQ-polaris-generation-002, "Motives, history, definitions and relationships without sufficient source premises SHALL remain absent or Unknown", where the sufficient premises of a reconstructed motive are its checked premises together with a counted fidelity verdict that its trail supports it. For Redis's runs, this narrows how ruling 10b and REQ-polaris-generation-034's "maintainer-stated advantages and trade-offs" apply: Redis's motivations and trade-offs may be reconstructed under this requirement, while its advantages stay governed by ruling 10b. Every other sentence and scenario of REQ-polaris-generation-002, 004, 034 and 035 is unchanged, including "an Inferred label alone SHALL NOT make speculation eligible" and the rule that generated prose SHALL NOT impersonate an author.

ID: REQ-polaris-generation-038
Source: VIS-2; governing warrants below.
Scope: v1-mandatory

#### Scenario: Maintainer text anchors the motivation

- **WHEN** a design note or source comment at the pinned revision, under none of the frozen profile's generated, vendored or third-party path classes, states why a mechanism exists, and the draft quotes it under a maintainer-stated block
- **THEN** the block renders with the verified quotation as its Observed anchor, the claim Inferred, and the quotation's maintainer authorship labelled Inferred from its location
- **AND** the fidelity verdict records that the span is maintainer text and states the motivation

#### Scenario: Vendored text is not maintainer-stated

- **WHEN** a maintainer-stated block quotes a README or comment under a path the frozen profile classes as vendored or third-party
- **THEN** Syzygy reports a repair finding for that block
- **AND** the same text cited as a premise of a reconstructed block passes the check

#### Scenario: Motivation reconstructed from code and tests

- **WHEN** no maintainer text states why a mechanism exists, and the draft carries a reconstructed block citing the code paths and tests it rests on, with a trail
- **THEN** the block renders Inferred with the marker that it is reconstructed and is not the authors' stated intent, and its trail and premises one step away
- **AND** no surface presents it as the authors' statement or as Observed

#### Scenario: Unmarked motivation

- **WHEN** an Inferred block that the agent did not mark as one of the four kinds states that the authors chose a design to avoid a cost
- **THEN** the fidelity verdict classifies it as a motivation without a basis and records a blocking finding whose deficient subject is the marking
- **AND** the draft does not become ready until a revision marks it with a basis that passes the check and the review

#### Scenario: Reconstruction without premises or trail

- **WHEN** a reconstructed block cites no premise, cites a path absent at the pinned revision, or carries no trail
- **THEN** Syzygy reports a repair finding naming the block and what is missing
- **AND** the draft does not proceed to review until a resubmitted revision passes

#### Scenario: Statement and reconstruction disagree

- **WHEN** a maintainer-stated block and a reconstructed block about the same design point disagree
- **THEN** both render, and the understanding record lists the disagreement among its contradictory accounts
- **AND** the reconstruction does not replace or soften the maintainers' statement

#### Scenario: Reconstructed advantage while ruling 10b stands

- **WHEN** ruling 10b is in force unreversed and a draft block of the advantage kind has a reconstructed basis, or a reconstructed block claims an advantage over a named other project that no verified maintainer-stated quotation names
- **THEN** Syzygy reports a repair finding for that block
- **AND** a maintainer-stated advantage with a verified quotation passes

#### Scenario: Motive about people stays Unknown

- **WHEN** a block attributes a motive to the authors' circumstances, employer or commercial aims and has no maintainer-stated basis
- **THEN** the fidelity verdict records a blocking finding and the claim renders absent or Unknown
- **AND** an Inferred label alone does not make it eligible

#### Scenario: History premise without history in scope

- **WHEN** a reconstructed block cites a commit message and the run's observation scope does not admit history
- **THEN** Syzygy reports a repair finding for that citation
- **AND** where the scope admits history, the same citation to a commit reachable from the pinned commit verifies against the commit object Syzygy read and re-hashed, with its author and committer lines withheld

#### Scenario: Unsupported trail blocks readiness

- **WHEN** a validated fidelity verdict records that a reconstructed block's trail does not support its claim from its premises
- **THEN** the finding is blocking and the draft does not become ready
- **AND** the finding names the argument as its deficient subject

Form: event-response.

- **Case:** Submit controlled drafts against a fixture repository at a pinned commit, varying each block's kind, marking, basis, quotations and their paths (authored, generated, vendored, unplaced), premises, trail, named comparisons and commit-message citations, with history admitted and not admitted, ruling 10b reversed and not, and fidelity verdicts that classify, support and do not support each block, marked and unmarked.
- **Observable:** The repair findings, the rendered blocks with their labels, markers, trails and anchors in human and machine form, the understanding record, the verdict validation and the readiness state.
- **Oracle:** Expected findings, labels, markers and readiness fixed in the fixture before the run, from the fixture blobs and commit objects read by an independent Git implementation.
- **Oracle independence:** The drafts and verdicts are fixture inputs written outside the code under test; the expected outcomes are not derived from the checker's output.
- **Falsifier:** A reconstructed block renders without its marker, trail or premises, or as Observed or as the authors' statement; a marked block of the four kinds passes without exactly one basis; an unmarked block the verdict classifies as one of the four kinds leaves the draft ready; any block attributes an intention to the authors without a maintainer-stated quotation that states it and the draft becomes ready; a maintainer-stated block passes on a vendored, third-party, generated or unplaced source, or its maintainer authorship is shown as Observed; a reconstructed advantage passes while ruling 10b stands unreversed; a motive about people renders as a claim without a maintainer-stated basis; a commit-message citation passes without history in scope; a disagreement between statement and reconstruction is hidden; or a draft becomes ready with an unsupported reconstruction.

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

This requirement is conditional. It has effect only while an owner ruling reversing ruling 10b of the owner direction `REDIS-LOCAL-AGENT-SITTING-2026-10-07` is in force, established from the record of the owner's act or direction that makes it (RFC3-16); if the owner keeps ruling 10b, this requirement is struck from the change before sign-off. While no reversal is in force, a draft block that the agent marks as resting on a source outside the clone SHALL fail the check as a repair finding, and advantages stay maintainer-stated only. Syzygy can detect such a block only from the agent's marking; the fidelity review is the backstop, and a block it finds resting on a source outside the clone without that marking is a blocking finding.

While the reversal is in force, a draft MAY carry external-comparison blocks: claims about the subject relative to named other projects that rest on sources outside the clone, such as web pages, papers or other repositories, that the agent reports having read. Syzygy SHALL NOT fetch, read or verify any external source, and SHALL NOT render any external text as a quotation. Each external-comparison block SHALL be labelled Inferred, SHALL carry a marker in human and machine form stating that it is the agent's unverified report of external sources, and SHALL list each source as the agent reports it (a title, an address and the date the agent reports reading it) as presentation labels, never as an anchor, an evidence identifier or a source page. These blocks SHALL render together in one section of the dossier, apart from the claims anchored in the clone, and SHALL NOT appear in the opening or the concise account or discharge any reading-depth obligation of REQ-polaris-generation-004. The fidelity verdict SHALL record each such block as unverifiable from its packet and SHALL NOT count it as supported. The run record and the section SHALL disclose that the agent's reads of external sources, and any transmission they involved, were the operator's own act, outside Syzygy's consent records and not observed by Syzygy.

ID: REQ-polaris-generation-039
Source: VIS-2; governing warrants below.
Scope: v1-reserved

#### Scenario: External comparison while 10b is reversed

- **WHEN** the owner's reversal of ruling 10b is in force and a draft block, marked as resting on an external source, compares the subject with a named other project, citing a web page the agent reports reading
- **THEN** the block renders Inferred in the external-comparison section with the unverified-report marker and the source as a label
- **AND** no anchor, source page or Observed quotation is rendered for the external source, and Syzygy made no request for it

#### Scenario: External comparison while 10b stands

- **WHEN** no reversal of ruling 10b is in force and a draft block is marked as resting on a source outside the clone
- **THEN** Syzygy reports a repair finding for that block
- **AND** the draft does not proceed to review until a resubmitted revision passes

#### Scenario: Unmarked external source

- **WHEN** a block rests on a source outside the clone but the agent did not mark it so
- **THEN** Syzygy's check does not detect it, and the fidelity verdict records a blocking finding
- **AND** the draft does not become ready

#### Scenario: External comparison kept out of the primary reading

- **WHEN** a draft places an external-comparison block in the opening or the concise account, or presents it as a maintainer-stated advantage
- **THEN** Syzygy reports a repair finding
- **AND** the reading-depth obligations are judged without that block

Form: event-response.

- **Case:** Submit controlled drafts with and without external-comparison blocks, marked and unmarked, placed in and out of their section, with the owner's reversal of ruling 10b in force, absent and withdrawn, and capture Syzygy's network activity independently.
- **Observable:** The repair findings, the rendered section, labels, markers and source labels, the verdict records, captured network effects and the disclosures.
- **Oracle:** Expected findings and renderings fixed in the fixture before the run; network effects from an independent capture.
- **Oracle independence:** Drafts, rulings and expected outcomes are fixture inputs written outside the code under test.
- **Falsifier:** A marked external-comparison block passes while 10b stands; an unmarked one leaves the draft ready after a counted fidelity verdict; Syzygy requests an external source; an external source renders as an anchor, a source page, a quotation or Observed; a block appears in the opening or concise account or discharges a reading-depth obligation; a verdict counts an external block as supported; or the operator's-own-act disclosure is absent.

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
