> **Candidate — binds nothing.** This is a drafted semantic delta under
> CC-REV-2 and the normative-change workflow. It performs no act, adopts
> nothing and authorizes no implementation. It would take effect only through
> an owner act over this package's behavior manifest, named in
> `.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md`; until that act is
> performed the adopted 2026-09-05 specification stands unchanged.

# Semantic delta PWB-RENDER-MODE-1 — the exact-source route reaches every admitted source in a closed render mode

**Artifact(s):**         `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`,
`openspec/changes/polaris-project-wide-butlers-model/design.md`,
`openspec/changes/polaris-project-wide-butlers-model/CAPABILITY-COVERAGE.md`,
`openspec/changes/polaris-project-wide-butlers-model/GOVERNING-DEPENDENCIES.md`
(generated)
**Stable IDs affected:**  PWB-REQ-011 (amended). PWB-REQ-014, PWB-REQ-020,
PWB-REQ-015, PWB-REQ-003, PWB-REQ-005, PWB-REQ-006 are reached by the change
and are **not** amended; §"What explicitly does NOT change" says why for each.
**Change class:**         Normative
**Author:**               Drafting agent session, on the owner's P-81 ruling
**Date:**                 2026-09-21

## Current meaning

PWB-REQ-011 today, in full, as adopted (spec.md lines 632–677):

````markdown
### Requirement: PWB-REQ-011 — Project summary, catalogs and exact sources are progressively reachable

Group: Presentation. Form: **invariant**.

Polaris SHALL provide a project summary, complete project catalogs, capability
deep dives and exact authoritative artifacts as progressively deeper reading
levels. A reader who stops at any level SHALL retain a true, coarser account.

- **Case (sweep)**: start from every project-level catalog category and follow
  one declared item through each available depth.
- **Observable**: each path resolves from summary to catalog to detail to exact
  source without changing the fact's identity or epistemic state.
- **Oracle**: enumerate every category and compare path targets to the machine
  answer and source anchors; the complete path population decides.
- **Oracle independence**: categories and anchors come from the source model,
  while expected depth semantics come from RFC7-13/14/17.
- **Falsifier**: a category is unreachable, a link resolves to a different
  identity, or a coarser level overstates the deeper source.

#### Scenario: Capability reaches exact requirements

- **WHEN** a reader opens a declared capability from the catalog
- **THEN** its detail links to the governing requirement identities
- **AND** exact requirement text remains reachable without treating Polaris as authority

#### Scenario: Consented baseline requirement renders verbatim

- **WHEN** the requested requirement belongs to a baseline
  `openspec/specs/*/spec.md` exact Git object already selected by the signed
  source population and the existing `declared-project-shape-text` authority,
  exact-object, secret and inert-content gates all admit it
- **THEN** Polaris may transiently encode only that requirement and its
  scenarios verbatim after verifying their source identity
- **AND** it stores, logs, caches and returns no unselected body bytes; a failed
  gate leaves the exact text Unknown and grants no wider content-class access

```yaml
warrants:
  primary: RFC7-13
  doctrine: [VIS-1, VIS-3, VIS-7]
  contracts: [RFC1-26, RFC3-27, RFC3-28, RFC6-20, RFC6-21, RFC7-13]
  policies: [CC-BAR-3]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-031]
```
````

Read literally, that text obliges progressive depth and, in its one
body-reading scenario, admits exactly one population: a requirement that
"belongs to a baseline `openspec/specs/*/spec.md` exact Git object". Nothing
in it says what the route does when the reader asks for any other source.
The implementation answers by refusing: the class gate in the app's
exact-source route admits only the baseline class and returns the refusal
reason `unconsented-source-or-provider` for everything else, and a second
gate refuses a source whose record outcome is excluded
[Observed — `apps/three-surface-poc/src/verbatim-route.ts`, the class and
exclusion gates, read 2026-09-21].

The design document's §8 states the argument that produced that scope, and
ends:

```markdown
Baseline `openspec/specs/*/spec.md` Git objects are already members of the
signed source population, and PWB-REQ-011/015 already require exact requirement
text. The performed consent covers exact Git objects selected by that
population under `declared-project-shape-text`. The live route therefore needs
no wider content class: after the ordinary authority gate, exact-object check,
whole-body secret scan, inert-content classification and requirement-identity
digest check, the renderer may transiently encode only the requested verbatim
requirement and scenarios. It stores, logs, caches and returns no unselected
body. If any gate fails, exact text remains Unknown. Any proposal to read a
body outside that population or return a raw artifact requires a separate
consent amendment and act.
```

The capability coverage table records the same scope in row 10:

```markdown
| 10 | Preserve progressive paths to catalogs, deep dives and transient verbatim baseline requirements within the existing content class | covered — PWB-REQ-011 |
```

Two neighbouring obligations bound what an amendment here may do. PWB-REQ-014
closes the anchor-identity question:

```markdown
Anchor targets SHALL use the closed classes doctrine, contract, requirement,
decision, evidence and work with durable target identity; labels, file paths
and coordinates SHALL never serve as anchor identity.
```

And PWB-REQ-020 obliges recoverability of everything the surface presents:

```markdown
Every project-shape identity, statement, source anchor, coverage state,
denominator, contradiction, body-read authority state and walkthrough-judgment
state or disclosure Polaris presents SHALL be recoverable from the same
evaluation in the machine answer, preserving multiplicity and exact provenance
state.
```

## Proposed meaning

PWB-REQ-011 as proposed, in full. The first paragraph, the two existing
scenarios and the warrants block are byte-identical to the adopted text; one
invariant paragraph, one rewritten bullet list and three scenarios are new:

````markdown
### Requirement: PWB-REQ-011 — Project summary, catalogs and exact sources are progressively reachable

Group: Presentation. Form: **invariant**.

Polaris SHALL provide a project summary, complete project catalogs, capability
deep dives and exact authoritative artifacts as progressively deeper reading
levels. A reader who stops at any level SHALL retain a true, coarser account.

The exact-source route SHALL serve every project-shape source the evaluation
admitted as a classified blob, in exactly one render mode drawn from the closed
set `requirement-sections`, `whole-body`: `requirement-sections` for a baseline
`openspec/specs/*/spec.md` source and `whole-body` for every other admitted
source. A source whose record outcome is excluded SHALL NOT be served in any
mode; it SHALL stay counted with its revision-bound identity, its content
digest and its fixed exclusion reason, and no route or sink SHALL carry any of
its body bytes. Every mode SHALL apply the same authority, exact-object,
secret-detection and inert-content gates to the complete transient body before
encoding any part of it; a failed gate SHALL leave that body Unknown with its
reason and SHALL grant no wider content-class access. Each served mode SHALL
expose a scroll anchor for each reading unit a citation can name; an anchor is
presentation only, SHALL NOT remove, narrow or reorder what the route serves
without it, and SHALL NOT enter, replace or qualify any source, claim or
narrative anchor identity. Each served route's mode, source identity and each
refusal's reason SHALL be recoverable, per rendered tuple, from the same
evaluation in the machine answer.

- **Case (sweep)**: start from every project-level catalog category and follow
  one declared item through each available depth; separately, request the
  exact-source route once for every source in the complete source population,
  admitted and excluded alike.
- **Observable**: each path resolves from summary to catalog to detail to exact
  source without changing the fact's identity or epistemic state; each source's
  served mode, or its refusal reason, is recoverable in both channels.
- **Oracle**: enumerate every category and compare path targets to the machine
  answer and source anchors; the complete path population decides. Separately
  partition the complete source population into served and refused, compare
  each served body to the exact Git object its identity names and each
  refusal to that source's recorded outcome, and report both denominators;
  the complete source population decides.
- **Oracle independence**: categories and anchors come from the source model,
  while expected depth semantics come from RFC7-13/14/17; the served/refused
  partition and every expected body come from the evaluation's own source
  records, never from the route's output.
- **Mutation proof**: independently inject a served excluded source, a mode
  outside the closed set, a mode applied to the wrong source class, a body
  encoded before a gate ran, an anchor that removes or reorders served content,
  and an anchor used as an anchor identity; confirm the oracle fails before
  restoration and report both denominators for every run.
- **Falsifier**: a category is unreachable, a link resolves to a different
  identity, a coarser level overstates the deeper source, an excluded source is
  served in any mode, a served mode is outside the closed set or wrong for its
  source class, or an anchor narrows what the route serves or serves as an
  identity.

#### Scenario: Capability reaches exact requirements

- **WHEN** a reader opens a declared capability from the catalog
- **THEN** its detail links to the governing requirement identities
- **AND** exact requirement text remains reachable without treating Polaris as authority

#### Scenario: Consented baseline requirement renders verbatim

- **WHEN** the requested requirement belongs to a baseline
  `openspec/specs/*/spec.md` exact Git object already selected by the signed
  source population and the existing `declared-project-shape-text` authority,
  exact-object, secret and inert-content gates all admit it
- **THEN** Polaris may transiently encode only that requirement and its
  scenarios verbatim after verifying their source identity
- **AND** it stores, logs, caches and returns no unselected body bytes; a failed
  gate leaves the exact text Unknown and grants no wider content-class access

#### Scenario: Consented non-baseline source renders whole-body

- **WHEN** the requested source is an exact Git object already selected by the
  signed source population, is not a baseline `openspec/specs/*/spec.md`
  source, was admitted by this evaluation as a classified blob, and the
  existing `declared-project-shape-text` authority, exact-object, secret and
  inert-content gates all admit its complete transient body
- **THEN** Polaris may transiently encode that body verbatim in the
  `whole-body` mode after verifying its source identity
- **AND** it stores, logs, caches and returns no other body bytes; a failed
  gate leaves that body Unknown with its reason and grants no wider
  content-class access

#### Scenario: Withheld source stays digest-only

- **WHEN** the requested source's record outcome is excluded
- **THEN** the route serves no body in any mode and names that source's fixed
  exclusion reason
- **AND** the source keeps its revision-bound identity and content digest in
  both channels, the source denominator is unchanged, and no route or sink
  carries any of its body bytes

#### Scenario: A citation lands on the unit it names

- **WHEN** a citation names one reading unit of a source the route serves
- **THEN** the route exposes that unit's scroll anchor as the citation's target
- **AND** the route serves exactly the units it serves without the anchor, in
  the same order

```yaml
warrants:
  primary: RFC7-13
  doctrine: [VIS-1, VIS-3, VIS-7]
  contracts: [RFC1-26, RFC3-27, RFC3-28, RFC6-20, RFC6-21, RFC7-13]
  policies: [CC-BAR-3]
  decisions: [POLARIS-DIR-2026-08-31]
  topology: []
  parent_requirements: [three-surface-poc-experience/POC-REQ-031]
```
````

The design document gains two paragraphs after §8's existing paragraph,
extending the same consent argument and stating why the mode set is closed:

```markdown
The same reasoning carries to every other source this evaluation admitted as
a classified blob. Each is the same kind of exact Git object, selected by the
same signed population and covered by the same consent class, so serving it
reads no wider class and asks for no new class. What differs is the reading
unit. A baseline `openspec/specs/*/spec.md` source has requirement sections
to select, and a route that finds none there can only refuse; every other
admitted source declares no such sections, so its reading unit is the whole
admitted body. The route therefore carries exactly two render modes —
`requirement-sections` and `whole-body` — chosen by the source's own class
and never by the reader. The set is closed: a third mode would be a third
reading unit, which is a new specification question, not a rendering detail.

Nothing in that carry reaches a withheld source. A source whose record
outcome is excluded has no admitted body to serve, so it keeps its identity,
its content digest and its fixed exclusion reason, stays in every denominator
and is refused in both modes. The gates do not move either: every mode runs
the same authority, exact-object, secret and inert-content checks against the
complete transient body before any of it is encoded, and a failure leaves
that body Unknown with its reason. Scroll anchors are presentation only —
they let a citation land on the unit it names, and never decide what the
route serves or stand in for any anchor identity.
```

Capability coverage row 10 is restated over the wider population:

```markdown
| 10 | Preserve progressive paths to catalogs, deep dives and transient verbatim bodies of every admitted source within the existing content class, in two closed render modes, never for a withheld source | covered — PWB-REQ-011 |
```

`GOVERNING-DEPENDENCIES.md` is generated from the specification and carries
the specification's sha256 in its source line; its patch is that regeneration
and nothing else. No requirement's `warrants` block changes, so the union of
authorities, its per-authority citation lists and all 96 distinct authorities
are identical before and after [Observed — the generator was re-run over the
proposed bytes and the only differing line is the source-digest line; the
builder's `--check` recomputes that digest rather than trusting it].

## What explicitly does NOT change

Enumerated, because "I only widened the route" is exactly the claim a reader
should distrust here.

1. **The consented content class.** No new class is requested, no new source
   population is discovered, and no source outside the signed population
   becomes readable. The proposed text reaches only sources "the evaluation
   admitted as a classified blob" — sources whose bodies the current
   evaluation already read, classified and hashed.
2. **The nine withheld sources stay withheld** — seven TOML butler manifests,
   one frontend page and one excluded roster artifact in the observed
   repository. The proposed text makes their refusal an obligation of the
   requirement rather than a property of the implementation, and adds a
   scenario whose only outcome is a refusal that names the recorded exclusion
   reason.
3. **Every gate.** Authority (PWB-REQ-005), exact-object identity, the secret
   detectors and the active-content scan run unchanged, on the complete
   transient body, before any byte is encoded. The proposed text restates
   this as an obligation of *every* mode so that a second mode cannot acquire
   a second, weaker path.
4. **PWB-REQ-014 is not amended.** A scroll anchor is a coordinate, and
   PWB-REQ-014 forbids coordinates as anchor identity. The proposed text says
   in its own words that an anchor is presentation only and never enters,
   replaces or qualifies any anchor identity, so the two clauses agree
   without either moving. The `presentation-artifact` and `non-citable`
   attributes stay on every narrative unit.
5. **PWB-REQ-020 is not amended.** Its bytes are untouched. The parity
   obligation P-81 names — the sweep extended over the anchor parameter — is
   carried as an obligation *inside* PWB-REQ-011 ("recoverable, per rendered
   tuple, from the same evaluation in the machine answer"), which PWB-REQ-020
   already requires of everything Polaris presents. This keeps the change one
   coherent category and leaves the scoped-attributes candidate's amendment
   of PWB-REQ-020 free of a second author. Per-tuple, not per-id, is
   deliberate: a claim may render more than once.
6. **PWB-REQ-015 is not amended.** The owner's P-81 Q5 asks for a separate
   PWB-REQ-015 delta; it is a later package and is not drafted here.
7. **PWB-REQ-003 and PWB-REQ-006 are not amended.** Unknown still never
   folds, denominators still count withheld sources, and the containment,
   inertness, byte-ledger and response bounds are unchanged. A refused source
   is not a counted pass.
8. **Nothing is implemented.** No route, renderer, oracle or test changes by
   this delta. The implementation needs the owner act over this package's
   manifest and then an implementation authorization; P-81 blocks the
   implementing bead on that gate.
9. **The other seven behavior artifacts.** `.openspec.yaml`, `proposal.md`,
   `CONTRACT-COVERAGE.md`, `CONTRACT-COVERAGE-REPAIR-DELTA.md` and the three
   `contract-coverage-matrix/` parts are byte-identical; the manifest carries
   them unchanged because the eleven artifacts take effect together or not at
   all.

## Change class

**Normative**, and the RFC2-26 test is the reason it cannot be Clarifying.
RFC2-26 says, in the accepted contract module
`.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`:

```markdown
**RFC2-26.** This contract schedules nothing: **it is not a specification of
record from which implementation work may be scheduled**. No implementation
work for user-observable consequences of this contract — evaluation and
snapshot displays, claim and challenge rendering, Unknown-reason and
rendering-tier presentation, reconciliation-chain and gap surfaces, API
answers over epistemic state — may be scheduled solely from this RFC. Before
implementation, every observable consequence either maps to an approved
OpenSpec requirement and scenario in the governance root's `openspec/**`
plane, or carries a reviewed N/A judgment proving it purely structural with
no independently testable behavior.
```

Applied honestly to this change: serving 77 sources that are refused today is
a user-observable consequence. The adopted PWB-REQ-011 maps one body-reading
consequence, and its scenario names the population it maps — a requirement
belonging to a baseline `openspec/specs/*/spec.md` object. A source outside
that population is mapped by no scenario, so the consequence is unmapped, and
RFC2-26's alternative (a reviewed N/A judgment proving the consequence purely
structural) is unavailable: a route that returns a body where it previously
returned a refusal is independently testable behavior, and the observable
population moves from 192 served to 269 served out of 278 [Inferred — 192 +
77, arithmetic performed in this prose and in no script's output. The two
addends are [Observed]: the M14 record
`docs/evidence/polaris-m14-provenance-depth-funnel-2026-09-17.json` reports
`headline_measurement.post_trim.rule_tally.baseline-spec-tree` = 192 and
`body_classification_for_s5_m2.nonbaseline_blob_classified.count` = 77 over
its 278-source denominator, measured by a `re.findall` sweep over the
post-trim lane A captures named in that record's `captures.post_trim` block
and the `projectShape.sources` array of its API capture. P-81 Q4 rules
machine figures Observed and sums Inferred; this is a sum]. The honest reading
is therefore that PWB-REQ-011 does **not** already admit these sources and the
change adds an obligation. Someone who complied before — by refusing every
non-baseline source — would not comply after. That is the Normative test in
the change-class table, and it is met.

Two smaller class facts, stated so a reviewer can contradict them: the
amendment also *adds* a refusal obligation (the withheld sources, today a
property of the implementation only), which is likewise Normative; and the
design and coverage edits are Structural-looking but carry the same new
obligation in prose, so they travel in this delta rather than as editorial
follow-ups.

## Warrant

The owner's dated direction of 2026-09-21,
`.syzygy/governance/decisions/POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`,
row P-81 (M14), arm A:

```markdown
**A** — Q1 yes for the 77 non-baseline sources with a render mode, never for
the 9 withheld (seven TOML butler manifests, one frontend page, one excluded
artifact), gated behind a CC-REV-2 scenario to PWB-REQ-011 and the act that
follows sign-off; Q2 a scroll anchor with the whole spec still served,
landing with slice 1
```

and, in the same row's consequence column: "slices 1–2 land together after the
scenario's act, with the 9 withheld sources still refused and the parity sweep
extended over the anchor parameter. No source outside the consented content
class is read."

That direction binds no digest and adds no acceptance-record row; it directs
that this scenario be drafted and gates the implementation behind an act over
it. This delta is the drafting, not the act.

## Evidence or decision basis

`docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md` and its retained
measurement record `docs/evidence/polaris-m14-provenance-depth-funnel-2026-09-17.json`,
reviewed in fresh context (CONFIRM WITH EXCEPTIONS, both exceptions applied):

- The post-trim capture carries 278 source rows, of which 86 are non-baseline
  [Observed, measured on the retained capture].
- Those 86 split 77 admitted classified blobs and 9 whose record outcome is
  excluded — 8 unclassifiable-excluded and 1 excluded-artifact [Observed].
- The route refuses all 86 today at the class gate, and refuses the 9 at a
  second gate that the class gate currently makes unreachable [Observed, read
  in the route module].
- Dropping the class gate alone would not serve the 77: the requirement-section
  selector refuses a body with no requirement heading and the reader would get
  `reference-unresolvable` instead of a body [Observed,
  `apps/three-surface-poc/src/capability-detail.ts`, the section selector].
  This is why the change is a *render mode* and not a widened gate, and it is
  the single strongest argument for the closed two-mode set.

The nine withheld sources' classification comes from the observed repository's
own records and the approved secret-classification policy; nothing in this
delta re-reads or re-classifies them, and no repository body was read while
drafting it.

## Terms introduced / retired

**Introduced: render mode**, with a closed two-value set —
`requirement-sections` and `whole-body`. The set is closed in the
requirement's own words, so a third mode is an amendment, not a configuration
choice. The values are a property of the *source class*, never of the reader,
the request or a preference.

**Introduced: scroll anchor**, as a presentation-only target for a citation
that names one reading unit of a served source. The term is deliberately
narrow and the requirement states its three prohibitions inline (it never
removes, narrows or reorders what the route serves; it never enters, replaces
or qualifies any source, claim or narrative anchor identity). It is not an
anchor in the PWB-REQ-014 sense and does not enter that clause's closed
classes.

**Retired:** none. No identifier is renumbered or renamed.

## Downstream impact

**Method.** Two independent sweeps over the 1,334 files tracked in this
worktree, run in this session (verification rule 2; the denominator is stated
per rule 9). Method 1: Python `re` over every tracked file for `PWB-REQ-011`
and for the continuation forms this corpus uses (`PWB-REQ-010, 011`,
`PWB-REQ-011/015`, `PWB-REQ-010..012`), since a full-identifier sweep alone
produces a false absence. Method 2: a recursive fixed-string sweep
(`grep -rF -l`, ugrep) over the same tree. Method 1 found 82 tracked
full-form citers plus 4 files that cite the requirement only in continuation
form; method 2 returned the same 82 plus one file this package itself creates
and nothing else. 4 tracked files are unreadable as UTF-8 and are excluded
from both, and named as the remainder.

The 86 citers partition as follows, counted by the same script.

| Class | Count | Moves in this change? |
|---|---:|---|
| Bound behavior artifacts that cite it (of the eleven the manifest binds) | 8 | 4 move; the other 4 citers and 3 non-citing artifacts are byte-identical rows |
| Implementation and test modules under `apps/` | 18 | No — only after a later implementation authorization |
| Retained evidence, measurement and pursuit records | 19 | No — historical records, never edited |
| Retained raw reviews and review notes | 20 | No — CC-REV-6 stores raw output unchanged |
| Design funnels and implementation plans under `docs/` | 6 | No — `docs/design/POLARIS-M14-PROVENANCE-DEPTH-FUNNEL.md` is this change's evidence and stays as measured |
| Other governance pages under `.syzygy/` | 9 | No — the scoped-attributes candidate is a parallel lane; see the collision below |
| `AGENTS.md`, the change's `tasks.md`, the three retained coverage-part audits, one other change's `design.md` | 6 | No — advisory, generated or another change's |

Three impacts deserve their own statement.

1. **A generated file collides with the parallel lane, by construction.**
   `GOVERNING-DEPENDENCIES.md` line 11 carries the specification's sha256.
   The scoped-attributes candidate amends the same specification, so both
   candidates rewrite that one line to different values and their patches
   cannot both apply. This is a regeneration, not a merge: whichever
   amendment is adopted second re-runs
   `python3 scripts/build_polaris_project_wide_spec_dependencies.py` over the
   adopted specification and re-derives the line. The builder asserts this
   rather than assuming it — `--check` applies the scoped-attributes diffs
   first and then requires that these three semantic patches still apply and
   that the generated one does not.
2. **Two governance records pin the specification's digest and go stale on
   any adoption here.** The approved secret-classification policy candidate
   and the adapter-registry observer candidate each carry a
   `governingBehaviorContract.version` naming the current specification's
   sha256. Adoption of this package (or of any other specification amendment)
   makes those pins name a superseded version. They are act-bound artifacts
   with their own amendment ceremony and this delta does not touch them; the
   pin refresh belongs to the registry amendment act the owner has already
   sequenced, and it is named here so that no later reader finds the
   staleness unannounced. [Observed — both files carry the current digest;
   [Inferred] that the refresh belongs to that act rather than this one.]
3. **The PWB-REQ-015 delta (P-81 Q5) is downstream and not drafted here.**
   PWB-REQ-015 governs capability detail's verbatim-intent band; a route that
   reaches more sources plainly reaches it. Drafting it inside this package
   would make the change two categories, which an OpenSpec change may not be.

No implementation file is edited by this package. The route, the section
selector, the parity sweep and the copy module are named in
`IMPACT-LEDGER.md` as the work an implementation would do after the act.

## Migration / supersession plan

1. **Fresh-context review** of this package against the adopted
   specification, the P-81 direction and the M14 funnel (CC-REV-1 full
   review; the change is Normative and the artifact is gate-bound). The
   review is bound to the exact bytes it reads; any later edit retires it
   (verification rule 10) and the manifest is regenerated.
2. **Owner sign-off** over `PWB-BEHAVIOR-AMENDMENT-MANIFEST.txt`, whose rows
   hash the eleven artifacts *as they will be* after the four patches under
   `proposed/` are applied. Four rows differ from the tree today; seven equal
   it. The phrase is registered in `scripts/check_governance.py` so a stale
   copy fails CG-7d/CG-7e, and it is **not offered** in this package's
   decision packet.
3. **Adoption, in one change**: a dedicated recorder in the 2026-09-05 shape
   validates the phrase against the manifest bytes; the builder's
   `--apply --at-adoption` writes the proposed bytes into `openspec/`; every
   manifest row is confirmed to hash the tree; the dedicated act record and
   the aggregate section of `ACCEPTANCE-ACT-RECORD.md` are written; the
   successor-chain link is registered. If the scoped-attributes amendment is
   adopted first, `GOVERNING-DEPENDENCIES.md` is regenerated in step 3 and
   its patch is dropped rather than merged, and the manifest is regenerated
   before the phrase is offered.
   **Sequencing caveat, round-1 finding F3.** That rule covers the sibling
   candidate landing whole. A *partial* landing — its `spec.md.patch` alone,
   cherry-picked before its package is otherwise ready — is rejected by no
   patch tool in any order, and would leave `GOVERNING-DEPENDENCIES.md`
   naming a digest for a `spec.md` that is not on disk, silently, because
   regeneration never runs on that path [Observed — the reviewer constructed
   it in four tool and order combinations, and this package's `--check` now
   reproduces the tree]. Since this package's `--check` was extended in
   response, that tree is no longer silent: the check asserts that the
   generated file's declared digest equals the sha256 of the `spec.md` bytes
   beside it, and reports a finding only if a partial tree ever becomes
   self-consistent. Neither package's tooling *prevents* the partial landing;
   the owner's sequencing decision and step 3's regeneration are what do.
4. **Supersession.** This package supersedes nothing. It would become the
   latest link over the eleven-artifact behavior population; every earlier
   act's rows stay immutable act-time history. The order of the two candidate
   successors is the owner's to set, which is why no chain link is registered
   ahead of the act.
5. **Implementation** follows only under a fresh authorization, with the nine
   withheld sources still refused and the parity sweep extended over the
   anchor parameter, per the P-81 consequence column.

## Review

**Required class:**  CC-REV-1 full fresh-context review; the artifact is
gate-bound and the class is Normative.

### Round 1 — 2026-09-21

**Reviewer:**  fresh-context reviewer, no authoring share.
**Raw output:** `docs/reviews/R-PWB-EXACT-SOURCE-RENDER-MODE-DELTA-RAW.md`,
retained verbatim and never edited (CC-REV-6).
**Verdict (copied exactly):** `CONFIRM WITH EXCEPTIONS`
**Reviewed bytes:** commit `08f980f`. The raw review states the manifest
SHA-256 it was bound to; this page does not copy it, so that there is exactly
one registered copy of the act argument (`OWNER-DECISION-PACKET.md`) for
CG-7d/CG-7e to keep current.

**Rule 10.** The raw review confirms the bytes at `08f980f`, **not** these
bytes. The repairs below edited `SEMANTIC-DELTA.md` and
`scripts/check_governance.py` and
`scripts/build_pwb_exact_source_render_mode_amendment.py` after that commit,
so round 1's confirmation is retired as to the current bytes and stands as
history for `08f980f`. A second fresh reviewer is required before the phrase
is offered. The manifest digest did **not** move: no repair touched a
manifest subject, so the phrase in `OWNER-DECISION-PACKET.md` still names
the reviewed argument.

| Finding | Class | Disposition |
|---|---|---|
| F1 | revise | **Accepted and repaired.** The 269 figure in the change-class argument now carries `[Inferred]`, names both addends' Observed sites and fields in the M14 evidence record, names the measurement method and the captures they were measured over, and cites P-81 Q4's rule that sums are Inferred. The packet already labeled the same figure |
| F2 | revise | **Accepted and repaired.** `check_governance.py --selftest` gains two rule-6 fixtures for `PWB_RENDER_MODE_LABEL` (`valid`, `missing-aggregate`) in the `PWB_TRUTH_AMENDMENT_LABEL` pattern; the battery moves 255 → 257 fixtures, 0 failing. Mutation-proved this session: neutering the dedicated-record registration fails 1 of the 2, neutering the aggregate registration fails both. **Disclosed limit:** misspelling the act *path* constant fails neither, because the fixture creates the record at whatever path the constant names — the fixtures prove the registration wiring, not the filename. The identical gap on `PWB_SCOPED_AMENDMENT_LABEL`, which F2 also names, is left to that package's own branch rather than edited from here |
| F3 | note | **Accepted; closed by tooling rather than by prose alone.** F3 owed this package nothing, and the reviewer could construct no false sentence in it. Rather than only state the caveat, `--check` was extended: it now builds the partial tree, confirms all four of this package's patches apply to it without any tool objection (reproducing the finding), and asserts the dependency digest is detectably inconsistent with the `spec.md` beside it. `--selftest` gains the inverse fixture — a no-op lane-B spec diff makes the partial tree self-consistent and must be reported. The sequencing caveat is also written into the migration plan above and the decision packet |

**Findings raised and rejected:** none.
**Findings deferred:** none. F2's sibling-label gap is disclosed above and
belongs to the scoped-attributes branch.
