# Syzygy — Human-Clarity Refactor, Public-Clone Normalization, and Final Pre-Specification Gate

Run this prompt in a **fresh Claude Fable session** at the root of the `Tzeusy/syzygy` repository.

This is a focused project-shape refactor. It is not another product-ideation cycle.

The goal is to make Syzygy understandable, maintainable, selectively loadable, and resistant to cumulative LLM-driven semantic rot **before** the first product specifications are authored.

The governing human standard is:

> A technically sound engineer who is unfamiliar with the project and team must
> be able to discover the project’s north star, understand its current state,
> navigate to exact authority, and perform a bounded task without reconstructing
> the project from hidden bootstrap records or loading the full knowledge corpus.

Syzygy must prove its own thesis on itself.

---

# 1. Primary objective

Refactor the project’s active knowledge and public repository so that all of the following become true:

1. The root of the repository clearly explains:
   - what Syzygy is;
   - why it exists;
   - what is implemented and not implemented;
   - its current lifecycle stage;
   - where a human should read next;
   - where an agent should read next.

2. `AGENTS.md` is a concise, current-state router—not an append-only historical diary and not a contradictory stack of old and new instructions.

3. Every active or candidate contract required to understand the current project shape is clone-visible or explicitly and truthfully marked founder-local and unavailable.

4. The active contract corpus is compact, modular, and task-addressable:
   - history is retained but removed from the default reading path;
   - stable clause identities are preserved;
   - oversized contracts are decomposed;
   - task-specific context can be compiled deterministically.

5. The project has one canonical plain-language vocabulary and does not require a newcomer to learn avoidable jargon.

6. Generated summaries and presentation artifacts remain subordinate to exact authority.

7. LLM-authored normative changes occur through bounded semantic deltas, not whole-file rewrites whose semantic effects are hard to reconstruct.

8. The current pending owner decisions are presented in a compact, resolvable, clone-visible interface.

9. Mission Control and bounded Missions are shaped consistently with the owner’s goal:
   - humans set goals, guardrails, risk, and budgets;
   - agents perform detailed work within a bounded envelope;
   - humans receive exception-oriented attention items rather than routine task micromanagement.

10. Syzygy is ready to begin OpenSpec authoring only after its active project shape is readable, accepted, clone-visible, and validated.

---

# 2. Current lifecycle stage and hard boundary

Syzygy remains in the **final pre-specification project-shape phase**.

This pass may:

- inspect and refactor documentation and governance artifacts;
- rewrite the public front door;
- compact candidate contracts;
- create contract indexes and migration maps;
- create or refine term registries;
- create or refine knowledge-hygiene policies;
- create Context Compiler contracts and non-runtime fixtures;
- create Mission/Autonomy contract drafts and doctrine amendment proposals;
- create public, repository-relative governance validation;
- create documentation-only GitHub Actions workflows;
- move candidate project-shape artifacts from founder-local storage into a clearly non-authoritative tracked candidate home;
- prepare exact owner acceptance records and manifests;
- use Beads only for process housekeeping if already required by repo instructions.

This pass must **not**:

- write application or library implementation code;
- create `src/`, `apps/`, `packages/`, UI components, daemon code, graph-store code, or product runtime schemas;
- choose a programming language, web framework, rendering engine, database, graph database, or deployment platform;
- create active OpenSpec product feature changesets;
- create an implementation backlog or product-delivery Beads;
- begin `/beads-orchestration`;
- auto-adopt doctrine, contracts, policies, topology, overview prose, license, or specifications;
- treat `_bootstrap/**`, generated indexes, summaries, or review syntheses as authority;
- add new broad product scope unless required to resolve a direct contradiction with the already stated product goal.

Stop at exact owner gates.

---

# 3. Settled product principles — preserve them

Do not reopen the following unless an actual contradiction is proven from adopted authority:

1. **Comprehensible truth; never comprehensible fiction.**
2. No evidence means **Unknown**, never green or zero.
3. Desired state, observed implementation state, inferred state, execution state, proposed state, and historical state are distinct.
4. Scheduled, completed, or merged work is never proof that intent was satisfied.
5. Authority is typed:
   - doctrine answers why;
   - accepted RFCs answer load-bearing how;
   - OpenSpec answers required observable behavior;
   - topology answers intended placement and boundaries;
   - craft-and-care answers the engineering and evidence bar;
   - code, tests, CI, and runtime answer what currently exists;
   - Beads answers work lifecycle;
   - Syzygy displays rebuildable projections.
6. Syzygy’s direct project-content writes are confined to:
   - `openspec/**`;
   - `.syzygy/**`.
7. Polaris (`intent/`), Trajectory (`work/`), and Orrery (`map/`) are projections over one shared kernel and are never independently authoritative.
8. Inference may challenge a positive claim but may not establish one.
9. The Project Genome is broader than behavioral specifications.
10. Full regeneration is a north star, not a current capability claim.
11. 3D spatial comprehension is required in V0, with co-equal precise non-3D paths.
12. Historical knowledge may grow without bound, but it must not remain in default task context.
13. Context is compiled, not accumulated.
14. Humans should govern high-level intent and bounded autonomy rather than approving every routine work step.
15. Mission Control is a workspace-level operator capability, not a fourth project-specific truth surface.
16. The public repository and a fresh clone must be able to reconstruct the project’s current shape without founder-machine lore.

Do not silently weaken any adopted `VIS-*`, `SEC-*`, `SDR-*`, or owner decision.

---

# 4. Required review organization

Use multiple independent fresh-context subagents or equivalent isolated review passes.

At minimum create these verticals:

1. **Fresh engineer / public-clone reviewer**
   - Starts from the root README.
   - Knows nothing about prior authoring.
   - Assesses discoverability, reading order, jargon, and current-state legibility.

2. **Vision and doctrine reviewer**
   - Tests whether the north star remains clear and memorable.
   - Identifies where constitutional prose has absorbed contract detail.
   - Checks whether plain-language restatement matches adopted meaning.

3. **Knowledge architecture and anti-rot reviewer**
   - Tests single-home authority, lifecycle lanes, archive boundaries, term drift, summary drift, and context budgets.

4. **Foundational contract and compaction reviewer**
   - Tests semantic preservation, clause migration, contract modularity, and RFC-versus-OpenSpec routing.

5. **Agent-context and Context Compiler reviewer**
   - Tests whether representative tasks can receive complete but bounded context.
   - Checks omission records and reproducibility.

6. **Mission Control and autonomy reviewer**
   - Tests whether humans can delegate bounded Missions rather than micromanaging work.
   - Checks escalation, budget, permissions, stop, and recovery semantics.

7. **Evidence and security reviewer**
   - Tests claim classes, provenance, owner-act authority, consent, machine clients, and execution profiles.

8. **Public-clone and validation reviewer**
   - Uses a clean clone or equivalent clean-tree simulation.
   - Verifies that no active claim depends on hidden `_bootstrap/**` files or machine-specific paths.

9. **Final exact-manifest reviewer**
   - Receives only current proposed active artifacts, not the authoring history.
   - Reviews the exact digests proposed for owner acceptance.

Store each raw verdict unchanged before synthesis.

Do not rename `EXCEPTIONS`, `REVISE`, or `REJECT` into softer verdicts.

---

# 5. Preflight: establish the actual current state

Before editing, inspect the repository and produce:

```text
REFRACTOR-PREFLIGHT-REPORT.md
```

Record:

```text
current branch
HEAD commit
working tree status
untracked files
ignored files relevant to project shape
Git tags
current Beads status, without creating product work
current adopted doctrine
current owner decisions
current craft-and-care state
current public overview state
current candidate contracts
current topology
current acceptance manifests
current portable verification tools
current public GitHub-visible state
```

Inspect at least:

```text
README.md
AGENTS.md
CLAUDE.md
PROJECT-STATUS.md, if present
CONTRIBUTING.md, if present
SECURITY.md, if present
LICENSE*, if present
.gitignore

.syzygy/governance/doctrine/**
.syzygy/governance/decisions/**
.syzygy/governance/policies/**
.syzygy/governance/contracts/**
.syzygy/intent/**
.syzygy/map/**
.syzygy/work/**

.claude/skills/**
.codex/skills/**
openspec/**

_bootstrap/rfc-phase/final-prespec/**
_bootstrap/knowledge-refactor/**
```

Search for stale phrases and paths:

```text
seed, not adopted doctrine
about/**
prompts/00
ADOPT DOCTRINE
ACCEPT FOUNDATIONAL RFCS
ACCEPT COMPACTED FOUNDATIONAL RFCS
bootstrap-phase record
this copy is the bootstrap-phase record
current acceptance state
latest
pending
DRAFT
unadopted
superseded
retired
founder-local
.git-excluded
```

Do not assume that a late-file note safely supersedes an earlier instruction.

---

# 6. Resolve the public-versus-local project-state split

Build:

```text
PUBLIC-CLONE-AUTHORITY-MATRIX.md
```

with:

| Artifact | Founder machine | Git tracked | Public clone resolves it? | Lifecycle | Authority | Required action |
|---|---:|---:|---:|---|---|---|

Cover at least:

- compacted foundational contract modules;
- active-contract manifest;
- final acceptance record;
- confirming reviews;
- portable verification scripts;
- topology;
- Mission Control contract;
- Context Compiler contract;
- doctrine amendment D3;
- term registry;
- knowledge-hygiene policy draft;
- clause migration map;
- RFC/OpenSpec routing matrix;
- owner-decision ledger;
- front-door drafts;
- license packet.

Apply this principle:

> Active authority and active candidate contracts required for current review
> must be clone-visible. Raw interviews, scratch work, transcripts, and detailed
> review history may remain local or separately archived.

If candidate artifacts are not accepted yet, track them under a clearly non-authoritative home such as:

```text
.syzygy/governance/contracts/candidates/
.syzygy/map/topology-candidates/
.syzygy/governance/reviews/current-candidate/
```

or another structure consistent with the current contract.

Do not install candidates into accepted homes or label them accepted.

Do not keep current acceptance logic only inside excluded `_bootstrap/**`.

---

# 7. Triage and resolve P-1 through P-16

Use `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md` as the clone-visible queue, but do not assume it is current merely because it exists.

Regenerate or correct it from the owning records.

Apply the following owner-directed recommended dispositions unless a direct authority conflict requires returning to the owner:

## P-1 — compacted foundational contracts

**Do not accept the existing package yet.**

First:

- fix P-6;
- complete P-10 review;
- make candidates clone-visible;
- regenerate the package manifest;
- run a final exact-digest review.

Then re-offer Act 1.

## P-2 — CC-TEST-2 craft amendment

Fix P-7 and P-8 across the canonical craft cluster and installation record.

Regenerate all affected digests.

Re-offer a separate exact-digest craft-amendment act.

## P-3 — topology

Move the candidate topology into a clone-visible candidate home.

Review its current content against the final compacted contract set.

Accept separately from RFCs.

## P-4 — project overview

Do not adopt the current overview unchanged.

Complete the progressive-disclosure refactor and remove hand-maintained stale status prose.

Review and re-offer a new exact digest.

## P-5 — bounded-Mission doctrine amendment

Treat bounded Missions as strategically required for the stated goal of high-level human guardrails plus LLM-driven detailed work.

Perform a focused doctrine review.

Return the minimal amendment for explicit owner adoption, amendment, or rejection.

Do not adopt it on the owner’s behalf.

## P-6 — retired acceptance phrase in active contract digest

Fix it.

Do not knowingly accept a foundational contract containing an obsolete acceptance mechanism.

Regenerate the manifest and run one new digest-binding review.

## P-7 — false craft banners

Fix all canonical craft files that call themselves bootstrap copies.

Canonical files must truthfully describe themselves as canonical.

Historical bootstrap copies may retain historical banners.

## P-8 — unsatisfiable craft binding phrase

Fix it.

Bind policy activation to the current effective owner-act/contract-status mechanism, not a retired magic phrase.

## P-9 — clone visibility

Resolve in favor of tracking:

- active candidate contracts;
- current acceptance records;
- current topology candidates;
- portable validation;
- compact current owner decisions;
- substrate compatibility locks.

Keep raw research and full reviewer transcripts out of default context.

## P-10 — review coverage

Commission the missing independent reviews for:

- RFC-0006 routing rows;
- knowledge architecture `KA-*`;
- knowledge hygiene `CC-KNOW-*`;
- budget policy `CC-BUDGET-*`;
- term-registry checks;
- Context Compiler fixtures;
- Mission/Autonomy material;
- front-door drafts.

Do not represent these as independently validated until reviewed.

## P-11 — public front door

Install the refactored public front door after fresh-reader review:

- README;
- AGENTS;
- PROJECT-STATUS;
- CONTRIBUTING;
- SECURITY.

`.gitignore` is already partially resolved; verify it.

## P-12 — knowledge-hygiene craft policy

Prioritize this before OpenSpec authoring.

Review and offer it through its own craft amendment act.

## P-13 — overview refactor

Complete before P-4.

## P-14 — license

Keep this as an owner/legal decision.

Provide a concise decision packet. Do not choose a license autonomously.

## P-15 — founder decision log

Promote a compact current decision register into a clone-visible authoritative or clearly governed decision home.

Do not require a clone to resolve routine active citations into hidden bootstrap files.

## P-16 — vocabulary

Canonicalize the six-plane state model and distinguish it from:

- claim epistemic labels;
- evidence tiers;
- work lifecycle states;
- governance lifecycles.

Complete this before OpenSpec multiplies terminology.

After the pass, replace the stale P-register with a regenerated exact current queue.

---

# 8. Rewrite the repository front door

## 8.1 Root README

Replace the one-line README.

Target: roughly 600–1,200 words.

Structure:

```text
# Syzygy

one-sentence thesis

Current stage:
pre-specification / project-shape normalization
no product implementation yet

Why it exists

Four experiences:
- Polaris — intent
- Trajectory — work
- Orrery — map
- Mission Control — bounded portfolio operation

Core loop diagram

What is authoritative

Start here:
- Overview
- Doctrine
- Current status
- Candidate/accepted contracts
- Policies
- Pending owner decisions
- Contributing
- Security

What is not yet implemented

License status
```

Do not reproduce full doctrine.

Avoid unexplained internal jargon.

## 8.2 `AGENTS.md`

Replace it completely.

Target: roughly 800–1,500 words.

It must contain only current instructions:

```text
current lifecycle stage
current authoritative paths
accepted artifacts
candidate artifacts
pending owner gates
selective reading rules
task routing
hard prohibitions
validation commands
Beads posture
session completion
```

It must not:

- call adopted doctrine a seed;
- route agents through bootstrap prompts 00–24;
- name `about/**` as the target authority;
- use retired acceptance phrases;
- refer to hidden records as the sole source of current truth;
- preserve a “Notes to self” appendix as default agent context.

Move historical lessons—grep failures, stale counts, reviewer transport issues, append-path incidents, prior gate migrations—into a non-default historical process record.

`CLAUDE.md` may continue to delegate to `AGENTS.md` once the latter is correct.

## 8.3 `PROJECT-STATUS.md`

Make current status concise and preferably generated or mechanically checkable.

Include:

```text
as-of commit
doctrine status
craft status
contract candidate/accepted status
topology status
overview status
OpenSpec status
implementation status
pending owner gates
known blocking defects
next lifecycle step
```

Do not use long narrative history.

## 8.4 `CONTRIBUTING.md`

Explain:

- current no-implementation boundary;
- authority layers;
- how to propose documentation and contract changes;
- semantic-delta workflow;
- fresh-context review expectations;
- where Beads does and does not apply;
- public-clone validation.

## 8.5 `SECURITY.md`

Provide a public vulnerability-reporting path and summarize the current security posture without duplicating SEC doctrine.

## 8.6 License

If unresolved, keep a visible status:

```text
No open-source license has yet been adopted.
Public viewing is permitted by GitHub; reuse rights are not yet granted.
```

Produce `LICENSE-DECISION-PACKET.md` for the owner.

---

# 9. Refactor Polaris for progressive disclosure

Refactor `.syzygy/intent/OVERVIEW.md`.

The default path must optimize for a technically capable newcomer.

Use four layers:

## Layer 1 — 30-second thesis

```text
Humans define what should be true.
Evidence shows what is true.
Agents do work to close the difference.
Syzygy explains all three and lets humans govern bounded missions.
```

## Layer 2 — five-minute project argument

Explain:

- the owner problem;
- desired vs observed vs execution;
- the shared kernel;
- Polaris, Trajectory, Orrery, Mission Control;
- why merged work is not proof;
- what is and is not implemented.

Use no more than roughly ten foundational terms.

## Layer 3 — technical model

Explain:

- typed authority;
- evidence and Unknown;
- reconciliation;
- governance/write boundaries;
- bounded autonomy.

## Layer 4 — exact authority drill-down

Expose:

- rule IDs;
- contract clauses;
- evidence;
- adoption status;
- source drawers.

Do not show dense inline provenance in every sentence by default.

Use paragraph/claim-block source anchors and optional source drawers.

Remove or generate any “Where this stands” section. Do not maintain current status manually inside a digest-bound overview.

The overview remains a governed presentation artifact and may never be cited in place of doctrine, contracts, specifications, policy, or topology.

---

# 10. Establish a canonical term registry

Create one canonical registry for public technical vocabulary.

Each term must include:

```text
stable term ID
canonical term
plain-language sentence
formal definition
owning authority
permitted aliases
deprecated synonyms
related-but-distinct terms
example
misuse example
```

Target roughly **20–30 foundational public concepts**.

At minimum reconcile:

```text
Project
Governance root
Project Genome
Capability
Requirement
Desired state
Proposed state
Observed state
Inferred state
Execution state
Historical state
Evidence
Claim
Warrant
Gap
Contradiction
Challenge
Snapshot
Evaluation
Observation record
Aligned
Converged
Mission
Autonomy envelope
Context packet
Attention item
```

Explicitly separate:

| Dimension | Values |
|---|---|
| State plane | desired, proposed, observed, inferred, execution, historical |
| Claim epistemic label | Observed, Inferred, Unknown |
| Evidence tier | report-fact, gate-backed, trusted oracle, governed checker, etc. |
| Work lifecycle | proposed, planned, running, blocked, reviewing, merged, reconciled, etc. |
| Governance lifecycle | draft, adopted, amended, retired; active, revoked, expired; recorded, withdrawn |

Do not use one generic word such as “status” where the dimension matters.

Add a term-admission rule:

> A new durable term is admitted only when no existing term covers it, its
> distinction matters operationally, its authority is clear, and a newcomer can
> explain it after one paragraph.

Produce:

```text
TERM-REGISTRY.md
TERM-MIGRATION-REPORT.md
```

Review before broad replacement.

---

# 11. Compact and normalize the active contract corpus

Work from the actual latest candidate package.

Do not create another full prose rewrite.

## 11.1 Artifact layers

Separate:

```text
Active normative contract
Concise rationale
Historical amendment/review archive
Derived indexes and summaries
```

Only the first is required task context.

## 11.2 Clause dispositions

Every existing clause receives one disposition:

```text
retained as normative
merged into another clause
moved to rationale/history
routed to OpenSpec
routed to craft-and-care
converted to informative example
retired
```

No silent deletion.

Preserve stable clause IDs where possible.

## 11.3 Contract module structure

Every active module contains:

```text
reader map
scope
non-scope
definitions
normative clauses
state model or closed vocabulary
authority boundaries
failure/Unknown semantics
integration obligations
violation cases
explicit deferrals
historical references
```

Move revision narratives, reviewer transcripts, old alternatives, and process incidents out.

## 11.4 Context budgets

Use these review triggers:

| Artifact | Budget trigger |
|---|---:|
| Root README | 1,200 words |
| AGENTS | 1,500 words |
| Active RFC module | 4,000 words |
| Exceptional active module | focused decomposition review above 5,000 words |
| Default context packet | 5,000–15,000 tokens |
| Context packet above 20,000 tokens | justification or task decomposition |

The limits are decomposition triggers, not validity laws.

## 11.5 Machine-readable metadata

Every module declares:

```yaml
id:
title:
lifecycle:
governs:
applies_to:
depends_on:
provides_to:
task_classes:
risk_classes:
terms:
open_spec_mapping_status:
```

Generate:

```text
ACTIVE-CONTRACT-MANIFEST
CLAUSE-MIGRATION-MAP
CONTRACT-DEPENDENCY-INDEX
TASK-TO-CONTRACT-INDEX
```

These indexes are derived, not authority.

## 11.6 RFC-versus-OpenSpec boundary

Every user-observable consequence in surface and Mission contracts must be marked:

```text
future OpenSpec requirement
pure structural invariant with reviewed N/A
craft/release policy
informative rationale
```

No product implementation may later be scheduled solely from observable behavior buried in RFC prose.

---

# 12. Fix craft-and-care authority and add knowledge hygiene

## 12.1 Correct canonical banners

Canonical files under:

```text
.syzygy/governance/policies/craft-and-care/
```

must not call themselves bootstrap copies.

Correct all banners and provenance descriptions.

Historical bootstrap copies remain clearly historical.

## 12.2 Correct binding mechanism

Remove any condition on retired phrases.

Describe effective policy binding through the current accepted contract and owner-act model.

Regenerate exact file digests.

## 12.3 Add knowledge-hygiene policy

Create stable `CC-KNOW-*` and `CC-BUDGET-*` rules covering:

1. one authoritative home per fact;
2. terms are scarce;
3. active contracts exclude history;
4. normative edits use semantic deltas;
5. generated summaries are never authority;
6. material normative changes receive fresh-context review;
7. “no semantic change” is a reviewable claim;
8. every active artifact states scope and non-scope;
9. context is compiled, not accumulated;
10. superseded material exits default context immediately;
11. whole-file normative rewrites require justification and mapping;
12. current-state prose is generated or revision-scoped;
13. clone reproducibility is part of done for governance changes;
14. document budgets trigger decomposition review;
15. new vocabulary requires term admission;
16. no active artifact depends solely on founder-local history.

Review this policy independently.

Offer it through a distinct craft amendment act.

---

# 13. Semantic-delta workflow

Create:

```text
SEMANTIC-DELTA-TEMPLATE.md
NORMATIVE-CHANGE-WORKFLOW.md
```

Each normative proposal records:

```text
artifact and stable IDs
current meaning
proposed meaning
change class
warrant
evidence or decision basis
terms added/retired
downstream impact
what explicitly does not change
migration/supersession plan
review class
```

Classes:

```text
Editorial
Clarifying
Normative
Structural
```

Rules:

- “Editorial” and “no semantic change” are reviewable claims.
- Structural moves preserve stable IDs.
- Whole-file rewrites are exceptional.
- Agents draft; owning authority adopts.
- Contradictions remain explicit.
- Generated summaries update only after source adoption.

---

# 14. Mission Control and bounded Missions

Inspect the current Mission/Autonomy contract and D3 amendment proposal.

The desired operating model is:

```text
Human defines goal, constraints, risk, budget, and evidence bar
→ human approves one bounded Mission
→ agents plan, execute, verify, retry, and recover within the envelope
→ human is interrupted only for declared exceptions
```

Mission Control is workspace-level, not a fourth project-specific truth surface.

The Mission contract must cover:

```text
objective
target projects/capabilities
exact intent revisions
autonomy level
allowed/prohibited change classes
write/tool/network/model permissions
budget
time limit
parallelism
required evidence
review floors
stop conditions
escalation conditions
completion predicate
checkpoint and rollback
context packet identity
```

Define an **Attention Item** with:

```text
what happened
why human judgment is required
evidence
available choices
default if ignored
blocked work
reversibility
deadline/expiry
```

Ensure the doctrine’s “not autonomous” wording does not accidentally require task-level human approval when a bounded Mission has been explicitly approved.

If amendment is needed, produce a minimal D3 packet.

Do not adopt it.

---

# 15. Context Compiler

Inspect and refine the existing Context Compiler contract.

It must produce immutable, digest-bound packets for:

```text
Mission
work item
review
spec authoring
reconciliation
```

A packet contains:

```text
objective
work warrant
exact doctrine rules
exact contract clauses
exact OpenSpec requirements
topology
craft policies
autonomy envelope
relevant code/evidence references
active contradictions/challenges
permissions
evaluation/as-of identity
compiler version
selection explanation
omitted-context register
digest
```

Selection is deterministic first:

```text
stable IDs
affected capabilities
dependency graph
task class
risk class
explicit applies_to metadata
typed authority
```

Inference may add context, never remove mandatory context.

Create fixtures for:

1. doctrine amendment;
2. kernel identity change;
3. OpenSpec authoring;
4. evidence adapter change;
5. Polaris presentation edit;
6. Trajectory lifecycle change;
7. Orrery lens change;
8. bounded Mission across two capabilities.

Verify:

- all mandatory context included;
- unrelated modules excluded;
- stable output for identical inputs;
- budget respected or waiver emitted;
- omissions recorded;
- no generated summary replaces exact authority.

The Context Compiler itself is not implemented in this pass.

---

# 16. Knowledge Health capability

Create a reviewed capability brief for a future shared Knowledge Health observer.

It should detect:

```text
undefined terms
duplicate definitions
conflicting definitions
deprecated synonyms
duplicate normative claims
summary/source divergence
references to superseded decisions
orphaned requirements or clauses
dangling internal links
stale evidence
context-budget violations
missing fresh-reader review
historical material in active context
agent-authored claims without source/warrant
current-state prose past its revision
hidden active authority
```

Outputs are:

```text
Observed issue
Inferred concern
Unknown coverage
Suggested remediation
```

It may never automatically rewrite normative artifacts.

Route future user-visible behavior to OpenSpec later.

---

# 17. Public, portable validation

Create repository-relative scripts and a minimal documentation/governance CI workflow.

Do not use founder-machine absolute paths.

Checks:

```text
internal links resolve
stable IDs unique
term definitions complete
deprecated normative terms absent
active docs do not cite superseded decisions
presentation does not claim authority
historical artifacts excluded from active context
context budgets reported
module metadata valid
clause migration complete
active manifest digest valid
context fixtures deterministic
duplicate authority homes absent
cache/local ignored
current instructions contain no retired bootstrap paths
no active candidate depends on hidden _bootstrap source
pending-decision register is current
canonical craft banners are truthful
root README and AGENTS pass fresh-reader review
```

Commit GitHub Actions for these documentation checks only.

Do not choose application tooling.

---

# 18. Public self-containment

A fresh clone must be able to answer:

```text
What is Syzygy?
What stage is it in?
Which doctrine is adopted?
Which contracts are candidates or accepted?
Which topology is candidate or accepted?
Which policies are binding or pending?
Which overview is draft or adopted?
Which owner decisions remain?
How do I validate all of this?
What should I read for my task?
```

No active clone-visible file may rely on an inaccessible `_bootstrap/**` pointer for essential meaning.

Historical evidence may be unavailable, but the active decision and current candidate must be self-contained.

---

# 19. Final review and acceptance package

After all corrections:

1. regenerate exact digests;
2. run all portable checks;
3. run the independent vertical reviews;
4. store raw verdicts unchanged;
5. disposition every `REVISE` or `EXCEPTIONS` finding;
6. run one final exact-manifest fresh review.

Produce one concise owner-facing record that names:

```text
exact files
exact digests
exact lifecycle
known accepted exceptions
remaining open questions
installation destination
commit/tag process
separate owner acts
```

Keep separate acts for:

```text
ACCEPT COMPACTED FOUNDATIONAL RFCS: <manifest digest>

CONFIRM CRAFT AMENDMENT:
<policy IDs>@<bundle digest>

ACCEPT TOPOLOGY:
<bundle digest>

ADOPT PROJECT OVERVIEW:
<digest>

ADOPT DOCTRINE AMENDMENT:
D3@<digest>   # only if owner chooses bounded Missions amendment
```

Do not implicitly bundle artifact classes.

Do not accept anything on the owner’s behalf.

---

# 20. Required outputs

Produce or update:

```text
README.md
AGENTS.md
PROJECT-STATUS.md
CONTRIBUTING.md
SECURITY.md
.gitignore

REFRACTOR-PREFLIGHT-REPORT.md
PUBLIC-CLONE-AUTHORITY-MATRIX.md
ACTIVE-AUTHORITY-MAP.md
ARTIFACT-INVENTORY.md
HISTORICAL-ARCHIVE-INDEX.md

TERM-REGISTRY.md
TERM-MIGRATION-REPORT.md

ACTIVE-CONTRACT-MANIFEST
CLAUSE-MIGRATION-MAP
CONTRACT-DEPENDENCY-INDEX
TASK-TO-CONTRACT-INDEX
COMPACTION-EQUIVALENCE-REPORT.md

SEMANTIC-DELTA-TEMPLATE.md
NORMATIVE-CHANGE-WORKFLOW.md

KNOWLEDGE-HEALTH-BRIEF.md
CONTEXT-COMPILER-FIXTURE-REPORT.md
MISSION-CONTROL-REVIEW.md

PUBLIC-CLONE-VERIFICATION-REPORT.md
FINAL-HUMAN-CLARITY-REVIEW.md
FINAL-PRE-SPECIFICATION-READINESS-REPORT.md
FINAL-OWNER-ACCEPTANCE-RECORD.md
```

If applicable:

```text
DOCTRINE-AMENDMENT-BOUNDED-MISSIONS-D3.md
LICENSE-DECISION-PACKET.md
```

---

# 21. Completion tests

The final readiness report must answer with evidence:

## Test A — 30 seconds

A fresh engineer opens the root README and can state:

- what Syzygy is;
- why it exists;
- its current stage;
- where to read next.

## Test B — 10 minutes

After the overview, the engineer can explain:

- desired vs observed vs execution state;
- Polaris, Trajectory, Orrery, Mission Control;
- why merged work is not proof;
- what Syzygy may write;
- what is not yet implemented.

## Test C — bounded task

A fresh agent receives a compiled context packet for:

> Propose how Trajectory should render a work item whose verification evidence
> is missing.

The agent must identify:

- applicable doctrine;
- evidence rules;
- relevant contract;
- future OpenSpec requirement boundary;
- accessibility and security obligations;
- owning authority.

It must not load the full corpus.

## Test D — clone equality

A clean clone derives the same:

- authority map;
- current lifecycle;
- candidate/accepted artifact statuses;
- active contract manifest;
- pending owner queue;
- validation results.

## Test E — no hidden semantic dependency

Remove access to `_bootstrap/**`.

Every active current-state and candidate artifact remains understandable and reviewable.

---

# 22. Final stop condition

Stop after presenting the exact owner gates.

Do not:

- create OpenSpec feature changesets;
- create implementation Beads;
- choose an implementation stack;
- scaffold product code;
- dispatch implementation agents.

Syzygy is ready for the specification phase only when:

```text
the front door is clear
the active knowledge is compact
the vocabulary is canonical
candidate/accepted contracts are clone-visible
the Context Compiler contract is tested by fixtures
bounded-Mission policy is owner-resolved
knowledge-hygiene policy is adopted
exact project-shape artifacts are accepted
```

Then the next phase is:

```text
/th-projects project-feature-request
```

for the first coherent V0 specification.

---

# Governing success condition

The refactor succeeds only when this statement is true:

> A technically capable person unfamiliar with Syzygy can understand its
> purpose, current state, governing rules, and next step without reconstructing
> the project from hidden history—and an LLM can receive exactly the context
> needed for one task without ingesting the entire Project Genome.

Preserve rigor. Remove accidental cognitive load.
