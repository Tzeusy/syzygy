# Directive register — every governing identifier and where it is defined

> **Generated navigation, never authority.** Written by
> `scripts/build_directive_register.py`; regenerate with it, never hand-edit.
> It answers one question — *where is this identifier defined?* — and refuses
> every other. The title column copies only what the corpus marks up at the
> definition site; it is never a clause body and never a paraphrase, and an
> em dash means the corpus marks no title there. To know what a rule **says**,
> open the file and line named here. Where this page and a clause disagree,
> the clause wins.
>
> Which acts are in force is owned by
> [`ACCEPTANCE-ACT-RECORD.md`](.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md)
> and summarised in [`PROJECT-STATUS.md`](PROJECT-STATUS.md). The status line
> under each heading below is a pointer to those, not a second copy of them.

[`PROCESS-GLOSSARY.md`](PROCESS-GLOSSARY.md) defines the identifier *forms* —
what `P-nn`, `RD-nn`, `CG-nn` and the rest mean. This page lists the
*instances*, which that page deliberately does not. Together they answer
"what kind of thing is this?" and "where does it live?"; neither answers
"what does it say?", because only the clause does.

**764 identifiers, 8 families**, recomputed from the files named
in each section every time the generator runs. A family whose files stop
defining its identifiers renders an empty table rather than a stale one.

## Vision doctrine — `VIS`

**Adopted, in force** since 2026-07-30. 7 identifiers, defined across 1 files.

| Identifier | Title, as the corpus marks it | Defined at |
|---|---|---|
| `VIS-1` | Comprehensible truth first; never comprehensible fiction | `.syzygy/governance/doctrine/vision.md`:82 |
| `VIS-2` | No evidence means Unknown, not success | `.syzygy/governance/doctrine/vision.md`:96 |
| `VIS-3` | Human interpretability is a core tenet | `.syzygy/governance/doctrine/vision.md`:108 |
| `VIS-4` | Humans steer the vision; agents shape within it | `.syzygy/governance/doctrine/vision.md`:122 |
| `VIS-5` | Syzygy never writes code; direct writes are confined to two namespaces | `.syzygy/governance/doctrine/vision.md`:141 |
| `VIS-6` | Syzygy is derived, with two closed exceptions | `.syzygy/governance/doctrine/vision.md`:167 |
| `VIS-7` | The observatory itself must be trustworthy | `.syzygy/governance/doctrine/vision.md`:183 |

## Security doctrine — `SEC`

**Adopted, in force** since 2026-07-30. 5 identifiers, defined across 1 files.

| Identifier | Title, as the corpus marks it | Defined at |
|---|---|---|
| `SEC-1` | Authenticated by default | `.syzygy/governance/doctrine/security.md`:10 |
| `SEC-2` | Portfolio data leaves owner-controlled infrastructure only through explicit, scoped consent | `.syzygy/governance/doctrine/security.md`:25 |
| `SEC-3` | Observed code is untrusted, everywhere | `.syzygy/governance/doctrine/security.md`:39 |
| `SEC-4` | Writes are consented, attributed, and revertable | `.syzygy/governance/doctrine/security.md`:47 |
| `SEC-5` | Secrets are never indexed | `.syzygy/governance/doctrine/security.md`:54 |

## Craft-and-care policy — `CC`

Owner-approved craft. 54 identifiers, defined across 8 files.

| Identifier | Title, as the corpus marks it | Defined at |
|---|---|---|
| `CC-BAR-1` | Canonical bar adopted; precedence fixed | `.syzygy/governance/policies/craft-and-care/engineering-bar.md`:10 |
| `CC-BAR-2` | Syzygy definition of done | `.syzygy/governance/policies/craft-and-care/engineering-bar.md`:43 |
| `CC-BAR-3` | Comprehensible truth is a merge constraint | `.syzygy/governance/policies/craft-and-care/engineering-bar.md`:67 |
| `CC-BAR-4` | No green without current evidence is a release constraint | `.syzygy/governance/policies/craft-and-care/engineering-bar.md`:88 |
| `CC-BAR-5` | Risk floors no implementing agent may downgrade | `.syzygy/governance/policies/craft-and-care/engineering-bar.md`:107 |
| `CC-BAR-6` | Evidence and review scale with declared risk, floors excepted | `.syzygy/governance/policies/craft-and-care/engineering-bar.md`:142 |
| `CC-BAR-7` | Changes stay reviewable | `.syzygy/governance/policies/craft-and-care/engineering-bar.md`:161 |
| `CC-DEP-1` | Liberal experimentation, disciplined promotion | `.syzygy/governance/policies/craft-and-care/interfaces-and-dependencies.md`:12 |
| `CC-DEP-2` | Stable identities anchor everything | `.syzygy/governance/policies/craft-and-care/interfaces-and-dependencies.md`:49 |
| `CC-DEP-3` | .syzygy/ is schema-versioned; migrations are identity-preserving | `.syzygy/governance/policies/craft-and-care/interfaces-and-dependencies.md`:69 |
| `CC-DEP-4` | External effects only through typed, explicitly authorized adapters | `.syzygy/governance/policies/craft-and-care/interfaces-and-dependencies.md`:90 |
| `CC-DEP-5` | Public interfaces are contracts with a compatibility story | `.syzygy/governance/policies/craft-and-care/interfaces-and-dependencies.md`:104 |
| `CC-DEP-6` | One kernel; surfaces never fork semantics | `.syzygy/governance/policies/craft-and-care/interfaces-and-dependencies.md`:123 |
| `CC-OBS-1` | Observation is deterministic; freshness is identity-bearing | `.syzygy/governance/policies/craft-and-care/observability-and-operations.md`:11 |
| `CC-OBS-2` | Inference is never rendered as observed fact | `.syzygy/governance/policies/craft-and-care/observability-and-operations.md`:33 |
| `CC-OBS-3` | Degradation is labelled; fidelity is never invented | `.syzygy/governance/policies/craft-and-care/observability-and-operations.md`:48 |
| `CC-OBS-4` | Operational failures leave durable, identified traces | `.syzygy/governance/policies/craft-and-care/observability-and-operations.md`:67 |
| `CC-OBS-5` | Authoritative effects are idempotent | `.syzygy/governance/policies/craft-and-care/observability-and-operations.md`:82 |
| `CC-OBS-6` | Syzygy's own operations meet the evidence bar it renders | `.syzygy/governance/policies/craft-and-care/observability-and-operations.md`:96 |
| `CC-PERF-1` | The only legal currency for performance is declared scope | `.syzygy/governance/policies/craft-and-care/performance-and-visual-discipline.md`:11 |
| `CC-PERF-2` | Derived conveniences are sacrificial; correctness of caches is not optional | `.syzygy/governance/policies/craft-and-care/performance-and-visual-discipline.md`:24 |
| `CC-PERF-3` | Performance claims carry measurement evidence | `.syzygy/governance/policies/craft-and-care/performance-and-visual-discipline.md`:35 |
| `CC-PROV-1` | Execution records are evidence artifacts | `.syzygy/governance/policies/craft-and-care/agent-provenance-and-execution-evidence.md`:12 |
| `CC-PROV-2` | Every run leaves a structured summary; the preserved set is closed | `.syzygy/governance/policies/craft-and-care/agent-provenance-and-execution-evidence.md`:29 |
| `CC-PROV-3` | Transcript retention is bounded; provenance retention is not | `.syzygy/governance/policies/craft-and-care/agent-provenance-and-execution-evidence.md`:53 |
| `CC-PROV-4` | Report facts are not the facts they report | `.syzygy/governance/policies/craft-and-care/agent-provenance-and-execution-evidence.md`:66 |
| `CC-PROV-5` | Missing cost renders Unknown, never zero | `.syzygy/governance/policies/craft-and-care/agent-provenance-and-execution-evidence.md`:87 |
| `CC-PROV-6` | Materialization is an immutable one-way mapping | `.syzygy/governance/policies/craft-and-care/agent-provenance-and-execution-evidence.md`:101 |
| `CC-PROV-7` | Inherited mutations are accounted in the parent run summary | `.syzygy/governance/policies/craft-and-care/agent-provenance-and-execution-evidence.md`:116 |
| `CC-REV-1` | Mandatory independent review classes | `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`:12 |
| `CC-REV-2` | The same-logical-change rule | `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`:52 |
| `CC-REV-3` | No hidden duplicate authority | `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`:76 |
| `CC-REV-4` | Fresh-reader review for normative artifacts | `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`:94 |
| `CC-REV-5` | Epistemic labels in documentation | `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`:107 |
| `CC-REV-6` | Review findings are dispositioned, never dropped | `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`:120 |
| `CC-REV-7` | Identifiers are stable; retire, never renumber | `.syzygy/governance/policies/craft-and-care/review-and-documentation.md`:131 |
| `CC-SEC-1` | Default-deny is the born state of every surface | `.syzygy/governance/policies/craft-and-care/security-and-secrets.md`:16 |
| `CC-SEC-2` | Egress is consent-checked in code, at every path | `.syzygy/governance/policies/craft-and-care/security-and-secrets.md`:31 |
| `CC-SEC-3` | Observed code never executes outside an accepted profile | `.syzygy/governance/policies/craft-and-care/security-and-secrets.md`:45 |
| `CC-SEC-4` | Writes are consented, attributed, atomic, revertable | `.syzygy/governance/policies/craft-and-care/security-and-secrets.md`:58 |
| `CC-SEC-5` | Secrets fail closed at every boundary | `.syzygy/governance/policies/craft-and-care/security-and-secrets.md`:71 |
| `CC-SEC-6` | Provenance retains hashes, never secret-bearing bodies | `.syzygy/governance/policies/craft-and-care/security-and-secrets.md`:88 |
| `CC-TEST-1` | Every defect fix ships a reproducing test; exceptions are rare and recorded | `.syzygy/governance/policies/craft-and-care/testing-and-verification.md`:13 |
| `CC-TEST-2` | Gate claims require retained, resolvable gate artifacts | `.syzygy/governance/policies/craft-and-care/testing-and-verification.md`:28 |
| `CC-TEST-3` | Determinism is verified, not assumed | `.syzygy/governance/policies/craft-and-care/testing-and-verification.md`:65 |
| `CC-TEST-4` | Deterministic or quarantined; a flaky gate poisons evidence | `.syzygy/governance/policies/craft-and-care/testing-and-verification.md`:81 |
| `CC-TEST-5` | Verification scope is declared; tests-as-spec is an explicit designation | `.syzygy/governance/policies/craft-and-care/testing-and-verification.md`:106 |
| `CC-TEST-6` | Unknown and absence paths are first-class test targets | `.syzygy/governance/policies/craft-and-care/testing-and-verification.md`:121 |
| `CC-TEST-7` | Re-check record: canonical bars 9 and 10 admitted without conflict | `.syzygy/governance/policies/craft-and-care/testing-and-verification.md`:136 |
| `CC-VIZ-1` | Every encoding declares source, units, legend, Unknown behavior, and freshness | `.syzygy/governance/policies/craft-and-care/performance-and-visual-discipline.md`:48 |
| `CC-VIZ-2` | No decorative element may silently misstate project truth | `.syzygy/governance/policies/craft-and-care/performance-and-visual-discipline.md`:61 |
| `CC-VIZ-3` | Unknowns are visible, aggregated honestly, never disappeared | `.syzygy/governance/policies/craft-and-care/performance-and-visual-discipline.md`:74 |
| `CC-VIZ-4` | Non-3D paths are co-equal and semantically equivalent | `.syzygy/governance/policies/craft-and-care/performance-and-visual-discipline.md`:95 |
| `CC-VIZ-5` | Layout is reproducible; geography is stable; analytical planes are labelled | `.syzygy/governance/policies/craft-and-care/performance-and-visual-discipline.md`:108 |

## Specification-acceptance standard — `CC-SPEC`

**In force.** Confirmed by craft act 6 on 2026-08-17 and amended at CC-SPEC-8 on 2026-09-01, whose act superseded the earlier digest. 11 identifiers, defined across 1 files.

**Read this before citing them.** Defined at a path named `policy-candidates/`, in a file named `…-CANDIDATE.md`, under a head banner that still says it binds nothing. All three are wrong and **none may be corrected**: the act bound these exact bytes. Read the act record, never the package banner (`AGENTS.md`, Governance prose and docs).

| Identifier | Title, as the corpus marks it | Defined at |
|---|---|---|
| `CC-SPEC-1` | Capability and scope are clear | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:42 |
| `CC-SPEC-2` | Every requirement names all its material governing warrants | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:62 |
| `CC-SPEC-3` | Every requirement has a stable identity | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:130 |
| `CC-SPEC-4` | Every requirement is falsifiable in a named form | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:139 |
| `CC-SPEC-5` | Non-goals and Unknowns are explicit | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:206 |
| `CC-SPEC-6` | No unresolved shape decision is silently selected | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:211 |
| `CC-SPEC-7` | Implementation detail appears only when it is required behavior | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:224 |
| `CC-SPEC-8` | Applicable contract clauses are covered or lawfully N/A | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:229 |
| `CC-SPEC-9` | A fresh technical reader can restate it | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:270 |
| `CC-SPEC-10` | Lawful adoption is recorded at the exact digest | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:280 |
| `CC-SPEC-11` | The requirement set covers the capability, and the coverage is demonstrated | `.syzygy/governance/contracts/candidates/policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`:310 |

## Shape-to-spec impact rule — `CC-IMPACT`

**In force** by craft act 7, 2026-08-17. 7 identifiers, defined across 1 files.

**Read this before citing them.** Same home and the same three-way mislabelling as `CC-SPEC`. CC-IMPACT-7 additionally names `SHAPE-TO-SPEC-PROPAGATION-FIXTURE-2.md` by path and digest; fixture 3 was added on 2026-08-30 because fixture 2 left `topology[]` unexercised, and neither the clause nor the fixture may be edited to say so.

| Identifier | Title, as the corpus marks it | Defined at |
|---|---|---|
| `CC-IMPACT-1` | Every accepted specification declares what governs it, and the declaration is generated | `.syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`:38 |
| `CC-IMPACT-2` | A shape delta performs a reverse-reference sweep, and the trigger set is the warrant set | `.syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`:71 |
| `CC-IMPACT-3` | The sweep records four sets, with its denominator and its method | `.syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`:97 |
| `CC-IMPACT-4` | Undecidable impact renders as Unknown or contradiction, never as unaffected | `.syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`:131 |
| `CC-IMPACT-5` | Every required amendment names its actor, and the sweep names one too | `.syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`:138 |
| `CC-IMPACT-6` | Affected specs move in the same logical change. There is no exception today | `.syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`:152 |
| `CC-IMPACT-7` | The path is exercised before it is relied on | `.syzygy/governance/contracts/candidates/policy-candidates/SHAPE-TO-SPEC-IMPACT-POLICY-CANDIDATE.md`:186 |

## Recorded owner decisions — `SDR`

**Recorded** — binding, not digest-bound. 37 identifiers, defined across 1 files.

**Read this before citing them.** These carry no title. The corpus marks each with the review finding or pending question it answers (`(R-12)`, `(P-40)`), which is what the title column shows. A ⚑ flag on that tag means the owner decided narrower or wider than the review recommended — open the entry to see which way.

| Identifier | Title, as the corpus marks it | Defined at |
|---|---|---|
| `SDR-1` | (R-1 ⚑) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:64 |
| `SDR-2` | (R-12) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:68 |
| `SDR-3` | (R-13) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:71 |
| `SDR-4` | (R-13 declaration site) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:76 |
| `SDR-5` | (R-2) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:82 |
| `SDR-6` | (R-2/R-11 corollary) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:84 |
| `SDR-7` | (R-5, option (a) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:86 |
| `SDR-8` | (R-10 ⚑) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:89 |
| `SDR-9` | (R-11) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:92 |
| `SDR-10` | (R-6) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:96 |
| `SDR-11` | (R-16) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:100 |
| `SDR-12` | (R-15) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:102 |
| `SDR-13` | (R-3 ⚑) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:108 |
| `SDR-14` | (R-3/VIS-3 scope) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:113 |
| `SDR-15` | (R-17) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:115 |
| `SDR-16` | (P-I1 refinement) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:118 |
| `SDR-17` | (R-18) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:120 |
| `SDR-18` | (R-19) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:122 |
| `SDR-19` | (R-7) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:127 |
| `SDR-20` | (R-4) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:129 |
| `SDR-21` | (new) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:132 |
| `SDR-22` | (R-20a ⚑) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:137 |
| `SDR-23` | (R-20b) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:141 |
| `SDR-24` | (R-20c ⚑) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:142 |
| `SDR-25` | (R-20d) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:145 |
| `SDR-26` | (R-20e) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:147 |
| `SDR-27` | (R-20f) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:149 |
| `SDR-28` | (R-9) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:156 |
| `SDR-29` | (R-9 refinement) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:157 |
| `SDR-30` | (R-9/OQ-010) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:161 |
| `SDR-31` | (R-14a) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:167 |
| `SDR-32` | (R-14b) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:169 |
| `SDR-33` | (R-14c) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:171 |
| `SDR-34` | (P-31) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:183 |
| `SDR-35` | (P-36) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:187 |
| `SDR-36` | (P-37) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:189 |
| `SDR-37` | (P-40) | `.syzygy/governance/decisions/SURFACE-DECISION-RECORD.md`:195 |

## Design contract clauses — `RFC-accepted`

**Accepted** — Waves A and B, 2026-08-17. 302 identifiers, defined across 24 files.

| Identifier | Title, as the corpus marks it | Defined at |
|---|---|---|
| `RFC1-1` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:101 |
| `RFC1-2` | Repository | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:121 |
| `RFC1-3` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:130 |
| `RFC1-4` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:140 |
| `RFC1-5` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:147 |
| `RFC1-6` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:179 |
| `RFC1-7` | Extension profiles | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:196 |
| `RFC1-8` | Frozen-noun mapping | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:225 |
| `RFC1-9` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:239 |
| `RFC1-10` | Identifiers are opaque; names are labels | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:263 |
| `RFC1-11` | Split and merge mint successors, never mutations | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:269 |
| `RFC1-12` | Judgments do not silently survive identity change | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:278 |
| `RFC1-13` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:286 |
| `RFC1-14` | Capability | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:293 |
| `RFC1-15` | Requirement and Scenario are references, not owned content | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:302 |
| `RFC1-16` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:310 |
| `RFC1-17` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:319 |
| `RFC1-18` | Claim and Gap identity has two levels | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:326 |
| `RFC1-19` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:382 |
| `RFC1-20` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:388 |
| `RFC1-21` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:395 |
| `RFC1-22` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:406 |
| `RFC1-23` | Act-assignment rule | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:444 |
| `RFC1-24` | All positive status flows through Claims | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:457 |
| `RFC1-25` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:463 |
| `RFC1-26` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:636 |
| `RFC1-27` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:646 |
| `RFC1-28` | The approved-but-unmaterialized plan item is a lifecycle state of the Proposal entity | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:656 |
| `RFC1-29` | Materialization is a one-way door | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:665 |
| `RFC1-30` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:695 |
| `RFC1-31` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:703 |
| `RFC1-32` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:740 |
| `RFC1-33` | — | `.syzygy/governance/contracts/rfcs/RFC-0001-project-graph-identity-state-planes.md`:750 |
| `RFC2-1` | The closed rule, restated as binding | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:67 |
| `RFC2-2` | Uncaptured means uninfluential | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:107 |
| `RFC2-3` | Evaluation identity | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:117 |
| `RFC2-4` | Degradation-only over an unchanged snapshot | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:129 |
| `RFC2-5` | Two-level claim identity (SDR-2) | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:141 |
| `RFC2-6` | Contents and immutability | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:150 |
| `RFC2-7` | The seam | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:166 |
| `RFC2-8` | Authority ceiling | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:176 |
| `RFC2-9` | The declaration mechanism | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:187 |
| `RFC2-10` | Identity-bearing freshness | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:209 |
| `RFC2-11` | Evidence–revision binding | `.syzygy/governance/contracts/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:225 |
| `RFC2-12` | Admissibility (doctrine floor, made operational) | `.syzygy/governance/contracts/rfcs/RFC-0002/challenge-lifecycle.md`:67 |
| `RFC2-13` | States, admission, resolution, expiry | `.syzygy/governance/contracts/rfcs/RFC-0002/challenge-lifecycle.md`:75 |
| `RFC2-14` | Suspension is not erasure | `.syzygy/governance/contracts/rfcs/RFC-0002/challenge-lifecycle.md`:220 |
| `RFC2-15` | Definitions and exits | `.syzygy/governance/contracts/rfcs/RFC-0002/reconciliation-chain.md`:71 |
| `RFC2-16` | As claim predicates | `.syzygy/governance/contracts/rfcs/RFC-0002/reconciliation-chain.md`:99 |
| `RFC2-17` | Reservation of the words | `.syzygy/governance/contracts/rfcs/RFC-0002/reconciliation-chain.md`:114 |
| `RFC2-18` | The chain | `.syzygy/governance/contracts/rfcs/RFC-0002/reconciliation-chain.md`:133 |
| `RFC2-19` | Trigger and staging | `.syzygy/governance/contracts/rfcs/RFC-0002/reconciliation-chain.md`:215 |
| `RFC2-20` | The closure fallacy, forbidden | `.syzygy/governance/contracts/rfcs/RFC-0002/reconciliation-chain.md`:256 |
| `RFC2-21` | What "no gap at evaluation E" means | `.syzygy/governance/contracts/rfcs/RFC-0002/reconciliation-chain.md`:267 |
| `RFC2-22` | Fixed point (idempotence) | `.syzygy/governance/contracts/rfcs/RFC-0002/reconciliation-chain.md`:278 |
| `RFC2-23` | Six degradation states, closed, each with its rendering obligation | `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`:70 |
| `RFC2-24` | Twelve reasons, closed | `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`:92 |
| `RFC2-25` | Six tiers, closed, each inside exactly one parent label | `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`:153 |
| `RFC2-26` | — | `.syzygy/governance/contracts/rfcs/RFC-0002/rendering-vocabularies.md`:196 |
| `RFC3-1` | — | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:96 |
| `RFC3-2` | Every manifest field names exactly one write authority | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:108 |
| `RFC3-3` | Direct-write containment | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:163 |
| `RFC3-4` | Location is designation | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:175 |
| `RFC3-5` | — | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:188 |
| `RFC3-6` | Repository entries | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:204 |
| `RFC3-7` | Consent records | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:211 |
| `RFC3-8` | Revocation and withdrawal | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:236 |
| `RFC3-9` | Drafting and repair | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:250 |
| `RFC3-10` | — | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:261 |
| `RFC3-11` | — | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:270 |
| `RFC3-12` | Never authoritative for project-internal truth (SDR-30) | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:277 |
| `RFC3-13` | — | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:285 |
| `RFC3-14` | Asymmetric relation semantics | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:290 |
| `RFC3-15` | — | `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`:71 |
| `RFC3-16` | Lifecycle status: a self-declaration inside content, an effective status outside it | `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`:101 |
| `RFC3-17` | — | `.syzygy/governance/contracts/rfcs/RFC-0003/governance-homes-and-owner-acts.md`:374 |
| `RFC3-18` | — | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:336 |
| `RFC3-19` | .syzygy/work/ | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:343 |
| `RFC3-20` | .syzygy/cache/ is rebuildable projection, nothing else | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:356 |
| `RFC3-21` | .syzygy/local/ is personal presentation state | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:366 |
| `RFC3-22` | Version stamps | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:377 |
| `RFC3-23` | Migrations are identity-preserving | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:384 |
| `RFC3-24` | Migration is an explicit, reviewed, revertable act | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:393 |
| `RFC3-25` | Forward and backward behavior | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:403 |
| `RFC3-26` | openspec/ | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:412 |
| `RFC3-27` | — | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:420 |
| `RFC3-28` | Spec anchors (SDR-32) | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:428 |
| `RFC3-29` | One plane per repository; one root per Project — upheld | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:441 |
| `RFC3-30` | Dual roles are lawful and per-pair | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:446 |
| `RFC3-31` | Nesting is composition by declaration | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:477 |
| `RFC3-32` | What a parent may never do | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:489 |
| `RFC3-33` | — | `.syzygy/governance/contracts/rfcs/RFC-0003/manifests-and-namespace.md`:513 |
| `RFC4-1` | Two roles, one discipline | `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`:60 |
| `RFC4-2` | Mandatory declaration set | `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`:68 |
| `RFC4-3` | Emission obligations | `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`:90 |
| `RFC4-4` | Failure is rendered, never invisible | `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`:98 |
| `RFC4-5` | The two-limb anti-duplication invariant | `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`:105 |
| `RFC4-6` | Substrate-term translation | `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`:137 |
| `RFC4-7` | The registry | `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`:147 |
| `RFC4-8` | Version skew | `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`:163 |
| `RFC4-9` | Substitution | `.syzygy/governance/contracts/rfcs/RFC-0004/general-contract.md`:176 |
| `RFC4-10` | OpenSpec adapter | `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`:73 |
| `RFC4-11` | Git/VCS adapter (with hosting sub-adapter) | `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`:93 |
| `RFC4-12` | Code-structure observer | `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`:114 |
| `RFC4-13` | Test, CI, and gate observers | `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`:134 |
| `RFC4-14` | Runtime observer | `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`:292 |
| `RFC4-15` | Beads adapter: the read contract | `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`:301 |
| `RFC4-16` | Capture-before-horizon | `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`:325 |
| `RFC4-17` | The warrant pointer (outward limb applied) | `.syzygy/governance/contracts/rfcs/RFC-0004/named-adapters.md`:366 |
| `RFC4-18` | Classification (SDR-8) | `.syzygy/governance/contracts/rfcs/RFC-0004/execution-record.md`:65 |
| `RFC4-19` | The minimum durable run envelope | `.syzygy/governance/contracts/rfcs/RFC-0004/execution-record.md`:75 |
| `RFC4-20` | Enrichment is explicitly non-required | `.syzygy/governance/contracts/rfcs/RFC-0004/execution-record.md`:104 |
| `RFC4-21` | Model, timing, token, and cost semantics | `.syzygy/governance/contracts/rfcs/RFC-0004/execution-record.md`:128 |
| `RFC4-22` | Declared join bases | `.syzygy/governance/contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:66 |
| `RFC4-23` | Worker liveness honesty | `.syzygy/governance/contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:77 |
| `RFC4-24` | The labeling schema (SDR-33; delegated by RFC2) | `.syzygy/governance/contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:108 |
| `RFC4-25` | Degradation mapping | `.syzygy/governance/contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:125 |
| `RFC4-26` | Declaration sites (SDR-3/4) | `.syzygy/governance/contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:132 |
| `RFC4-27` | Executed coverage behind every absence claim | `.syzygy/governance/contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:150 |
| `RFC4-28` | The invariant | `.syzygy/governance/contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:162 |
| `RFC4-29` | The enrichment roadmap, named but never required | `.syzygy/governance/contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:172 |
| `RFC4-30` | — | `.syzygy/governance/contracts/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:191 |
| `RFC5-1` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:78 |
| `RFC5-2` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:92 |
| `RFC5-3` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:101 |
| `RFC5-4` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:119 |
| `RFC5-5` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:154 |
| `RFC5-6` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:181 |
| `RFC5-7` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:205 |
| `RFC5-8` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:217 |
| `RFC5-9` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:229 |
| `RFC5-10` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:237 |
| `RFC5-11` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:244 |
| `RFC5-12` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`:78 |
| `RFC5-13` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`:98 |
| `RFC5-14` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`:113 |
| `RFC5-15` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`:154 |
| `RFC5-16` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`:177 |
| `RFC5-17` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/consent-egress-secrets.md`:202 |
| `RFC5-18` | The gate | `.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md`:80 |
| `RFC5-19` | The trust distinction | `.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md`:101 |
| `RFC5-20` | Profile contents | `.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md`:122 |
| `RFC5-21` | Isolation mechanism classes | `.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md`:144 |
| `RFC5-22` | Destructive-operation gates | `.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md`:165 |
| `RFC5-23` | Profile lifecycle | `.syzygy/governance/contracts/rfcs/RFC-0005/execution-profiles.md`:176 |
| `RFC5-24` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:278 |
| `RFC5-25` | Every authenticated act is attributable | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:302 |
| `RFC5-26` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:326 |
| `RFC5-27` | — | `.syzygy/governance/contracts/rfcs/RFC-0005/admission-and-boundary.md`:337 |
| `RFC6-1` | One selection identity space | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:94 |
| `RFC6-2` | Everything selectable, one way | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:104 |
| `RFC6-3` | Cross-surface synchronization | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:117 |
| `RFC6-4` | Evaluation defaulting is stamped, never silent | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:124 |
| `RFC6-5` | Total resolution | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:134 |
| `RFC6-6` | Outcomes are not Unknown reasons | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:174 |
| `RFC6-7` | Resolution is deterministic per evaluation | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:181 |
| `RFC6-8` | What a URL pins | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:188 |
| `RFC6-9` | Rename-stability | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:198 |
| `RFC6-10` | Two URL temporalities | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:204 |
| `RFC6-11` | Retired and merged identities | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:212 |
| `RFC6-12` | URLs are surface-independent | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:221 |
| `RFC6-13` | One truth, two consumers | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:229 |
| `RFC6-14` | Label parity | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:237 |
| `RFC6-15` | Every answer is evaluation-stamped | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:262 |
| `RFC6-16` | Filters are declared scope | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:268 |
| `RFC6-17` | Aggregation discloses | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:274 |
| `RFC6-18` | One drawer, one fact set | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:303 |
| `RFC6-19` | Drawer content classes | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:317 |
| `RFC6-20` | Drawer links obey the floor | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:373 |
| `RFC6-21` | Minimal display never subtracts facts | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:382 |
| `RFC6-22` | The equivalence definition | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:390 |
| `RFC6-23` | Finer detail is allowed; contradiction is not | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:404 |
| `RFC6-24` | Scenario context is explicit and singular | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:416 |
| `RFC6-25` | Context travels with the selection | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:448 |
| `RFC6-26` | Unconsented renders as policy, never as error | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:456 |
| `RFC6-27` | Excluded is a rendered state | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:465 |
| `RFC6-28` | This contract schedules nothing | `.syzygy/governance/contracts/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:473 |
| `RFC7-1` | What Polaris is | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:71 |
| `RFC7-2` | Composition, never custody | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:78 |
| `RFC7-3` | Nothing cites the rendering | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:98 |
| `RFC7-4` | Non-authority is total | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:109 |
| `RFC7-5` | Entities | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:115 |
| `RFC7-6` | One primary narrative | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:147 |
| `RFC7-7` | The governed-presentation-artifact class (SDR-13) | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:159 |
| `RFC7-8` | Neither cache nor governance authority | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:168 |
| `RFC7-9` | Granularity, covering, minimality, bounding | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:177 |
| `RFC7-10` | Anchor form | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:204 |
| `RFC7-11` | Broken anchors render Unknown, never silent | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:225 |
| `RFC7-12` | Restatement discipline | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:265 |
| `RFC7-13` | Progressive disclosure: the obligation, and a V0 default path | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:274 |
| `RFC7-14` | The verbatim leaf | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:292 |
| `RFC7-15` | Capability catalog honesty | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:308 |
| `RFC7-16` | Status in the narrative: minimal by default (SDR-17) | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:316 |
| `RFC7-17` | Bands, machine-distinct; three authority classes, closed | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:344 |
| `RFC7-18` | Never a second computation, never a second copy | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:367 |
| `RFC7-19` | Empty is honest | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:375 |
| `RFC7-20` | The draft state | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:382 |
| `RFC7-21` | Adoption is a human act | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:398 |
| `RFC7-22` | Rejection and the queue | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:422 |
| `RFC7-23` | Acts and gates | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:432 |
| `RFC7-24` | The SDR-18 seam | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:441 |
| `RFC7-25` | Materiality and review (SDR-14) | `.syzygy/governance/contracts/rfcs/RFC-0007/narrative-contract.md`:450 |
| `RFC7-26` | Two reading modes, named in the kernel's vocabulary | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:78 |
| `RFC7-27` | No fictitious consensus | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:93 |
| `RFC7-28` | Curated diagrams | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:101 |
| `RFC7-29` | The boundary table | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:113 |
| `RFC7-30` | The criterion | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:134 |
| `RFC7-31` | Verdict discipline | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:162 |
| `RFC7-32` | When it runs (SDR-14) | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:196 |
| `RFC7-33` | Every distinction, machine-readable | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:205 |
| `RFC7-34` | Non-visual recoverability | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:241 |
| `RFC7-35` | Multi-project entry | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:261 |
| `RFC7-36` | Portfolio narrative is owner-local, never project truth | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:268 |
| `RFC7-37` | Subprojects render as declared relations | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:304 |
| `RFC7-38` | This contract schedules nothing | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:323 |
| `RFC7-39` | The fixed human entry point | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:374 |
| `RFC7-40` | Repository-front-door discoverability is a per-repository finding | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:416 |
| `RFC8-1` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:70 |
| `RFC8-2` | The anti-thesis is binding | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:77 |
| `RFC8-3` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:84 |
| `RFC8-4` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:92 |
| `RFC8-5` | Deliberate non-reifications | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:107 |
| `RFC8-6` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:117 |
| `RFC8-7` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:125 |
| `RFC8-8` | "What remains?" enumerates three planes, each labeled | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:165 |
| `RFC8-9` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:204 |
| `RFC8-10` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:218 |
| `RFC8-11` | Divergence renders; Trajectory never adjudicates it | `.syzygy/governance/contracts/rfcs/RFC-0008/identity-authority-materialization.md`:235 |
| `RFC8-12` | (this paragraph restates it for orientation) | `.syzygy/governance/contracts/rfcs/RFC-0008/README.md`:177 |
| `RFC8-13` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/state-vocabulary-and-cost.md`:187 |
| `RFC8-14` | Raw provider status stays visible and queryable | `.syzygy/governance/contracts/rfcs/RFC-0008/state-vocabulary-and-cost.md`:216 |
| `RFC8-15` | Closure is not a normalized "done." | `.syzygy/governance/contracts/rfcs/RFC-0008/state-vocabulary-and-cost.md`:229 |
| `RFC8-16` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/state-vocabulary-and-cost.md`:239 |
| `RFC8-17` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/state-vocabulary-and-cost.md`:259 |
| `RFC8-18` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/state-vocabulary-and-cost.md`:282 |
| `RFC8-19` | Absent means Unknown, never zero | `.syzygy/governance/contracts/rfcs/RFC-0008/state-vocabulary-and-cost.md`:307 |
| `RFC8-20` | V1 | `.syzygy/governance/contracts/rfcs/RFC-0008/state-vocabulary-and-cost.md`:316 |
| `RFC8-21` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:79 |
| `RFC8-22` | A broken join renders; it is never silently skipped | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:93 |
| `RFC8-23` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:102 |
| `RFC8-24` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:120 |
| `RFC8-25` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:140 |
| `RFC8-26` | The preservation set is binding | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:183 |
| `RFC8-27` | Expired-detail rendering | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:189 |
| `RFC8-28` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:217 |
| `RFC8-29` | V0 renders the absence honestly | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:256 |
| `RFC8-30` | The closure fallacy is forbidden | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:262 |
| `RFC8-31` | — | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:272 |
| `RFC8-32` | This contract schedules nothing | `.syzygy/governance/contracts/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:313 |
| `RFC9-1` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:52 |
| `RFC9-2` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:63 |
| `RFC9-3` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:67 |
| `RFC9-4` | The anchoring rule | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:86 |
| `RFC9-5` | What may anchor geography | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:95 |
| `RFC9-6` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:108 |
| `RFC9-7` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:115 |
| `RFC9-8` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:119 |
| `RFC9-9` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:203 |
| `RFC9-10` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:411 |
| `RFC9-11` | The mode boundary is a contract: an analytical layout may never masquerade as home | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:429 |
| `RFC9-12` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:437 |
| `RFC9-13` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:442 |
| `RFC9-14` | Two-tier layout contract | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:477 |
| `RFC9-15` | Append-stability | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:513 |
| `RFC9-16` | The closed relocation-trigger set | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:521 |
| `RFC9-17` | Forbidden churn | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:616 |
| `RFC9-18` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:630 |
| `RFC9-19` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:651 |
| `RFC9-20` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:666 |
| `RFC9-21` | Identity-based counting, never double-counting | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:703 |
| `RFC9-22` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:722 |
| `RFC9-23` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:730 |
| `RFC9-24` | The reserved state palette | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:61 |
| `RFC9-25` | Reserved channels | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:87 |
| `RFC9-26` | The channel declaration contract | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:98 |
| `RFC9-27` | Unknown is never invisible | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:128 |
| `RFC9-28` | Height (SDR-24) | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:155 |
| `RFC9-29` | Text is a channel | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:164 |
| `RFC9-30` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:178 |
| `RFC9-31` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:190 |
| `RFC9-32` | V0 ships | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:207 |
| `RFC9-33` | Staging | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:259 |
| `RFC9-34` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:268 |
| `RFC9-35` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:273 |
| `RFC9-36` | City is the required V0 scene profile | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:294 |
| `RFC9-37` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:301 |
| `RFC9-38` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:311 |
| `RFC9-39` | Base and intended | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:328 |
| `RFC9-40` | Proposed | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:364 |
| `RFC9-41` | Historical | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:376 |
| `RFC9-42` | LOD epistemic invariance | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:399 |
| `RFC9-43` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:409 |
| `RFC9-44` | The unmapped district (SDR-25) | `.syzygy/governance/contracts/rfcs/RFC-0009/visual-grammar-and-lenses.md`:473 |
| `RFC9-45` | — | `.syzygy/governance/contracts/rfcs/RFC-0007/rendering-and-surface.md`:520 |
| `RFC9-46` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/interaction-parity-and-release.md`:55 |
| `RFC9-47` | The equivalence gate is a release check | `.syzygy/governance/contracts/rfcs/RFC-0009/interaction-parity-and-release.md`:106 |
| `RFC9-48` | Non-visual parity | `.syzygy/governance/contracts/rfcs/RFC-0009/interaction-parity-and-release.md`:249 |
| `RFC9-49` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/interaction-parity-and-release.md`:264 |
| `RFC9-50` | No ambient motion at V0 | `.syzygy/governance/contracts/rfcs/RFC-0009/interaction-parity-and-release.md`:289 |
| `RFC9-51` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/interaction-parity-and-release.md`:295 |
| `RFC9-52` | This contract schedules nothing | `.syzygy/governance/contracts/rfcs/RFC-0009/interaction-parity-and-release.md`:304 |
| `RFC10-15` | — | `.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md`:181 |

**Cited here, defined elsewhere or nowhere (2).** These appear
in this family's own files but at no definition site in them: `RFC10-16`, `RFC11-12`.

## Design contract clauses (candidate) — `RFC-candidate`

Candidate — **binds nothing.** RFC-0010 and RFC-0011, plus the candidate copies of the accepted modules. 341 identifiers, defined across 31 files.

**Read this before citing them.** A clause number appearing in both this family and the accepted one is the same clause in two homes. The accepted copy governs.

| Identifier | Title, as the corpus marks it | Defined at |
|---|---|---|
| `RFC1-1` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:101 |
| `RFC1-2` | Repository | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:121 |
| `RFC1-3` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:130 |
| `RFC1-4` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:140 |
| `RFC1-5` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:147 |
| `RFC1-6` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:179 |
| `RFC1-7` | Extension profiles | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:196 |
| `RFC1-8` | Frozen-noun mapping | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:225 |
| `RFC1-9` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:239 |
| `RFC1-10` | Identifiers are opaque; names are labels | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:263 |
| `RFC1-11` | Split and merge mint successors, never mutations | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:269 |
| `RFC1-12` | Judgments do not silently survive identity change | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:278 |
| `RFC1-13` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:286 |
| `RFC1-14` | Capability | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:293 |
| `RFC1-15` | Requirement and Scenario are references, not owned content | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:302 |
| `RFC1-16` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:310 |
| `RFC1-17` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:319 |
| `RFC1-18` | Claim and Gap identity has two levels | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:326 |
| `RFC1-19` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:382 |
| `RFC1-20` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:388 |
| `RFC1-21` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:395 |
| `RFC1-22` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:406 |
| `RFC1-23` | Act-assignment rule | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:444 |
| `RFC1-24` | All positive status flows through Claims | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:457 |
| `RFC1-25` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:463 |
| `RFC1-26` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:636 |
| `RFC1-27` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:646 |
| `RFC1-28` | The approved-but-unmaterialized plan item is a lifecycle state of the Proposal entity | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:656 |
| `RFC1-29` | Materialization is a one-way door | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:665 |
| `RFC1-30` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:695 |
| `RFC1-31` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:703 |
| `RFC1-32` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:740 |
| `RFC1-33` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md`:750 |
| `RFC2-1` | The closed rule, restated as binding | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:67 |
| `RFC2-2` | Uncaptured means uninfluential | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:107 |
| `RFC2-3` | Evaluation identity | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:117 |
| `RFC2-4` | Degradation-only over an unchanged snapshot | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:129 |
| `RFC2-5` | Two-level claim identity (SDR-2) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:141 |
| `RFC2-6` | Contents and immutability | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:150 |
| `RFC2-7` | The seam | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:166 |
| `RFC2-8` | Authority ceiling | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:176 |
| `RFC2-9` | The declaration mechanism | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:187 |
| `RFC2-10` | Identity-bearing freshness | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:209 |
| `RFC2-11` | Evidence–revision binding | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/snapshot-and-evaluation-core.md`:225 |
| `RFC2-12` | Admissibility (doctrine floor, made operational) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/challenge-lifecycle.md`:67 |
| `RFC2-13` | States, admission, resolution, expiry | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/challenge-lifecycle.md`:75 |
| `RFC2-14` | Suspension is not erasure | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/challenge-lifecycle.md`:220 |
| `RFC2-15` | Definitions and exits | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/reconciliation-chain.md`:71 |
| `RFC2-16` | As claim predicates | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/reconciliation-chain.md`:99 |
| `RFC2-17` | Reservation of the words | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/reconciliation-chain.md`:114 |
| `RFC2-18` | The chain | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/reconciliation-chain.md`:133 |
| `RFC2-19` | Trigger and staging | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/reconciliation-chain.md`:215 |
| `RFC2-20` | The closure fallacy, forbidden | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/reconciliation-chain.md`:256 |
| `RFC2-21` | What "no gap at evaluation E" means | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/reconciliation-chain.md`:267 |
| `RFC2-22` | Fixed point (idempotence) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/reconciliation-chain.md`:278 |
| `RFC2-23` | Six degradation states, closed, each with its rendering obligation | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/rendering-vocabularies.md`:70 |
| `RFC2-24` | Twelve reasons, closed | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/rendering-vocabularies.md`:92 |
| `RFC2-25` | Six tiers, closed, each inside exactly one parent label | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/rendering-vocabularies.md`:153 |
| `RFC2-26` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0002/rendering-vocabularies.md`:196 |
| `RFC3-1` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:96 |
| `RFC3-2` | Every manifest field names exactly one write authority | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:108 |
| `RFC3-3` | Direct-write containment | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:163 |
| `RFC3-4` | Location is designation | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:175 |
| `RFC3-5` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:188 |
| `RFC3-6` | Repository entries | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:204 |
| `RFC3-7` | Consent records | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:211 |
| `RFC3-8` | Revocation and withdrawal | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:236 |
| `RFC3-9` | Drafting and repair | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:250 |
| `RFC3-10` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:261 |
| `RFC3-11` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:270 |
| `RFC3-12` | Never authoritative for project-internal truth (SDR-30) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:277 |
| `RFC3-13` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:285 |
| `RFC3-14` | Asymmetric relation semantics | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:290 |
| `RFC3-15` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/governance-homes-and-owner-acts.md`:71 |
| `RFC3-16` | Lifecycle status: a self-declaration inside content, an effective status outside it | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/governance-homes-and-owner-acts.md`:101 |
| `RFC3-17` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/governance-homes-and-owner-acts.md`:374 |
| `RFC3-18` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:336 |
| `RFC3-19` | .syzygy/work/ | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:343 |
| `RFC3-20` | .syzygy/cache/ is rebuildable projection, nothing else | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:356 |
| `RFC3-21` | .syzygy/local/ is personal presentation state | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:366 |
| `RFC3-22` | Version stamps | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:377 |
| `RFC3-23` | Migrations are identity-preserving | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:384 |
| `RFC3-24` | Migration is an explicit, reviewed, revertable act | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:393 |
| `RFC3-25` | Forward and backward behavior | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:403 |
| `RFC3-26` | openspec/ | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:412 |
| `RFC3-27` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:420 |
| `RFC3-28` | Spec anchors (SDR-32) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:428 |
| `RFC3-29` | One plane per repository; one root per Project — upheld | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:441 |
| `RFC3-30` | Dual roles are lawful and per-pair | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:446 |
| `RFC3-31` | Nesting is composition by declaration | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:477 |
| `RFC3-32` | What a parent may never do | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:489 |
| `RFC3-33` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md`:513 |
| `RFC4-1` | Two roles, one discipline | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/general-contract.md`:60 |
| `RFC4-2` | Mandatory declaration set | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/general-contract.md`:68 |
| `RFC4-3` | Emission obligations | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/general-contract.md`:90 |
| `RFC4-4` | Failure is rendered, never invisible | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/general-contract.md`:98 |
| `RFC4-5` | The two-limb anti-duplication invariant | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/general-contract.md`:105 |
| `RFC4-6` | Substrate-term translation | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/general-contract.md`:137 |
| `RFC4-7` | The registry | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/general-contract.md`:147 |
| `RFC4-8` | Version skew | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/general-contract.md`:163 |
| `RFC4-9` | Substitution | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/general-contract.md`:176 |
| `RFC4-10` | OpenSpec adapter | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/named-adapters.md`:73 |
| `RFC4-11` | Git/VCS adapter (with hosting sub-adapter) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/named-adapters.md`:93 |
| `RFC4-12` | Code-structure observer | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/named-adapters.md`:114 |
| `RFC4-13` | Test, CI, and gate observers | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/named-adapters.md`:134 |
| `RFC4-14` | Runtime observer | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/named-adapters.md`:292 |
| `RFC4-15` | Beads adapter: the read contract | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/named-adapters.md`:301 |
| `RFC4-16` | Capture-before-horizon | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/named-adapters.md`:325 |
| `RFC4-17` | The warrant pointer (outward limb applied) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/named-adapters.md`:366 |
| `RFC4-18` | Classification (SDR-8) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/execution-record.md`:65 |
| `RFC4-19` | The minimum durable run envelope | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/execution-record.md`:75 |
| `RFC4-20` | Enrichment is explicitly non-required | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/execution-record.md`:104 |
| `RFC4-21` | Model, timing, token, and cost semantics | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/execution-record.md`:128 |
| `RFC4-22` | Declared join bases | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:66 |
| `RFC4-23` | Worker liveness honesty | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:77 |
| `RFC4-24` | The labeling schema (SDR-33; delegated by RFC2) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:108 |
| `RFC4-25` | Degradation mapping | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:125 |
| `RFC4-26` | Declaration sites (SDR-3/4) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:132 |
| `RFC4-27` | Executed coverage behind every absence claim | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:150 |
| `RFC4-28` | The invariant | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:162 |
| `RFC4-29` | The enrichment roadmap, named but never required | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:172 |
| `RFC4-30` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0004/fidelity-joins-and-mappings.md`:191 |
| `RFC5-1` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:78 |
| `RFC5-2` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:92 |
| `RFC5-3` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:101 |
| `RFC5-4` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:119 |
| `RFC5-5` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:154 |
| `RFC5-6` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:181 |
| `RFC5-7` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:205 |
| `RFC5-8` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:217 |
| `RFC5-9` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:229 |
| `RFC5-10` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:237 |
| `RFC5-11` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:244 |
| `RFC5-12` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/consent-egress-secrets.md`:78 |
| `RFC5-13` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/consent-egress-secrets.md`:98 |
| `RFC5-14` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/consent-egress-secrets.md`:113 |
| `RFC5-15` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/consent-egress-secrets.md`:154 |
| `RFC5-16` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/consent-egress-secrets.md`:177 |
| `RFC5-17` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/consent-egress-secrets.md`:202 |
| `RFC5-18` | The gate | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/execution-profiles.md`:80 |
| `RFC5-19` | The trust distinction | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/execution-profiles.md`:101 |
| `RFC5-20` | Profile contents | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/execution-profiles.md`:122 |
| `RFC5-21` | Isolation mechanism classes | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/execution-profiles.md`:144 |
| `RFC5-22` | Destructive-operation gates | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/execution-profiles.md`:165 |
| `RFC5-23` | Profile lifecycle | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/execution-profiles.md`:176 |
| `RFC5-24` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:278 |
| `RFC5-25` | Every authenticated act is attributable | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:302 |
| `RFC5-26` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:326 |
| `RFC5-27` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md`:337 |
| `RFC6-1` | One selection identity space | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:94 |
| `RFC6-2` | Everything selectable, one way | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:104 |
| `RFC6-3` | Cross-surface synchronization | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:117 |
| `RFC6-4` | Evaluation defaulting is stamped, never silent | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:124 |
| `RFC6-5` | Total resolution | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:134 |
| `RFC6-6` | Outcomes are not Unknown reasons | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:174 |
| `RFC6-7` | Resolution is deterministic per evaluation | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:181 |
| `RFC6-8` | What a URL pins | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:188 |
| `RFC6-9` | Rename-stability | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:198 |
| `RFC6-10` | Two URL temporalities | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:204 |
| `RFC6-11` | Retired and merged identities | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:212 |
| `RFC6-12` | URLs are surface-independent | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:221 |
| `RFC6-13` | One truth, two consumers | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:229 |
| `RFC6-14` | Label parity | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:237 |
| `RFC6-15` | Every answer is evaluation-stamped | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:262 |
| `RFC6-16` | Filters are declared scope | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:268 |
| `RFC6-17` | Aggregation discloses | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:274 |
| `RFC6-18` | One drawer, one fact set | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:303 |
| `RFC6-19` | Drawer content classes | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:317 |
| `RFC6-20` | Drawer links obey the floor | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:373 |
| `RFC6-21` | Minimal display never subtracts facts | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:382 |
| `RFC6-22` | The equivalence definition | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:390 |
| `RFC6-23` | Finer detail is allowed; contradiction is not | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:404 |
| `RFC6-24` | Scenario context is explicit and singular | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:416 |
| `RFC6-25` | Context travels with the selection | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:448 |
| `RFC6-26` | Unconsented renders as policy, never as error | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:456 |
| `RFC6-27` | Excluded is a rendered state | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:465 |
| `RFC6-28` | This contract schedules nothing | `.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:473 |
| `RFC7-1` | What Polaris is | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:71 |
| `RFC7-2` | Composition, never custody | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:78 |
| `RFC7-3` | Nothing cites the rendering | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:98 |
| `RFC7-4` | Non-authority is total | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:109 |
| `RFC7-5` | Entities | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:115 |
| `RFC7-6` | One primary narrative | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:147 |
| `RFC7-7` | The governed-presentation-artifact class (SDR-13) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:159 |
| `RFC7-8` | Neither cache nor governance authority | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:168 |
| `RFC7-9` | Granularity, covering, minimality, bounding | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:177 |
| `RFC7-10` | Anchor form | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:204 |
| `RFC7-11` | Broken anchors render Unknown, never silent | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:225 |
| `RFC7-12` | Restatement discipline | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:265 |
| `RFC7-13` | Progressive disclosure: the obligation, and a V0 default path | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:274 |
| `RFC7-14` | The verbatim leaf | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:292 |
| `RFC7-15` | Capability catalog honesty | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:308 |
| `RFC7-16` | Status in the narrative: minimal by default (SDR-17) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:316 |
| `RFC7-17` | Bands, machine-distinct; three authority classes, closed | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:344 |
| `RFC7-18` | Never a second computation, never a second copy | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:367 |
| `RFC7-19` | Empty is honest | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:375 |
| `RFC7-20` | The draft state | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:382 |
| `RFC7-21` | Adoption is a human act | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:398 |
| `RFC7-22` | Rejection and the queue | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:422 |
| `RFC7-23` | Acts and gates | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:432 |
| `RFC7-24` | The SDR-18 seam | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:441 |
| `RFC7-25` | Materiality and review (SDR-14) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/narrative-contract.md`:450 |
| `RFC7-26` | Two reading modes, named in the kernel's vocabulary | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:78 |
| `RFC7-27` | No fictitious consensus | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:93 |
| `RFC7-28` | Curated diagrams | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:101 |
| `RFC7-29` | The boundary table | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:113 |
| `RFC7-30` | The criterion | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:134 |
| `RFC7-31` | Verdict discipline | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:162 |
| `RFC7-32` | When it runs (SDR-14) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:196 |
| `RFC7-33` | Every distinction, machine-readable | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:205 |
| `RFC7-34` | Non-visual recoverability | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:241 |
| `RFC7-35` | Multi-project entry | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:261 |
| `RFC7-36` | Portfolio narrative is owner-local, never project truth | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:268 |
| `RFC7-37` | Subprojects render as declared relations | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:304 |
| `RFC7-38` | This contract schedules nothing | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:323 |
| `RFC7-39` | The fixed human entry point | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:374 |
| `RFC7-40` | Repository-front-door discoverability is a per-repository finding | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:416 |
| `RFC8-1` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:70 |
| `RFC8-2` | The anti-thesis is binding | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:77 |
| `RFC8-3` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:84 |
| `RFC8-4` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:92 |
| `RFC8-5` | Deliberate non-reifications | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:107 |
| `RFC8-6` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:117 |
| `RFC8-7` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:125 |
| `RFC8-8` | "What remains?" enumerates three planes, each labeled | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:165 |
| `RFC8-9` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:204 |
| `RFC8-10` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:218 |
| `RFC8-11` | Divergence renders; Trajectory never adjudicates it | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/identity-authority-materialization.md`:235 |
| `RFC8-12` | (this paragraph restates it for orientation) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/README.md`:177 |
| `RFC8-13` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/state-vocabulary-and-cost.md`:187 |
| `RFC8-14` | Raw provider status stays visible and queryable | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/state-vocabulary-and-cost.md`:216 |
| `RFC8-15` | Closure is not a normalized "done." | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/state-vocabulary-and-cost.md`:229 |
| `RFC8-16` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/state-vocabulary-and-cost.md`:239 |
| `RFC8-17` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/state-vocabulary-and-cost.md`:259 |
| `RFC8-18` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/state-vocabulary-and-cost.md`:282 |
| `RFC8-19` | Absent means Unknown, never zero | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/state-vocabulary-and-cost.md`:307 |
| `RFC8-20` | V1 | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/state-vocabulary-and-cost.md`:316 |
| `RFC8-21` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:79 |
| `RFC8-22` | A broken join renders; it is never silently skipped | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:93 |
| `RFC8-23` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:102 |
| `RFC8-24` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:120 |
| `RFC8-25` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:140 |
| `RFC8-26` | The preservation set is binding | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:183 |
| `RFC8-27` | Expired-detail rendering | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:189 |
| `RFC8-28` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:217 |
| `RFC8-29` | V0 renders the absence honestly | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:256 |
| `RFC8-30` | The closure fallacy is forbidden | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:262 |
| `RFC8-31` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:272 |
| `RFC8-32` | This contract schedules nothing | `.syzygy/governance/contracts/candidates/rfcs/RFC-0008/accounting-reconciliation-and-release.md`:313 |
| `RFC9-1` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:52 |
| `RFC9-2` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:63 |
| `RFC9-3` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:67 |
| `RFC9-4` | The anchoring rule | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:86 |
| `RFC9-5` | What may anchor geography | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:95 |
| `RFC9-6` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:108 |
| `RFC9-7` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:115 |
| `RFC9-8` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:119 |
| `RFC9-9` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:203 |
| `RFC9-10` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:411 |
| `RFC9-11` | The mode boundary is a contract: an analytical layout may never masquerade as home | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:429 |
| `RFC9-12` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:437 |
| `RFC9-13` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:442 |
| `RFC9-14` | Two-tier layout contract | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:477 |
| `RFC9-15` | Append-stability | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:513 |
| `RFC9-16` | The closed relocation-trigger set | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:521 |
| `RFC9-17` | Forbidden churn | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:616 |
| `RFC9-18` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:630 |
| `RFC9-19` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:651 |
| `RFC9-20` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:666 |
| `RFC9-21` | Identity-based counting, never double-counting | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:703 |
| `RFC9-22` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:722 |
| `RFC9-23` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:730 |
| `RFC9-24` | The reserved state palette | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:61 |
| `RFC9-25` | Reserved channels | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:87 |
| `RFC9-26` | The channel declaration contract | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:98 |
| `RFC9-27` | Unknown is never invisible | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:128 |
| `RFC9-28` | Height (SDR-24) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:155 |
| `RFC9-29` | Text is a channel | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:164 |
| `RFC9-30` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:178 |
| `RFC9-31` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:190 |
| `RFC9-32` | V0 ships | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:207 |
| `RFC9-33` | Staging | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:259 |
| `RFC9-34` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:268 |
| `RFC9-35` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:273 |
| `RFC9-36` | City is the required V0 scene profile | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:294 |
| `RFC9-37` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:301 |
| `RFC9-38` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:311 |
| `RFC9-39` | Base and intended | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:328 |
| `RFC9-40` | Proposed | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:364 |
| `RFC9-41` | Historical | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:376 |
| `RFC9-42` | LOD epistemic invariance | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:399 |
| `RFC9-43` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:409 |
| `RFC9-44` | The unmapped district (SDR-25) | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/visual-grammar-and-lenses.md`:473 |
| `RFC9-45` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md`:520 |
| `RFC9-46` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/interaction-parity-and-release.md`:55 |
| `RFC9-47` | The equivalence gate is a release check | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/interaction-parity-and-release.md`:106 |
| `RFC9-48` | Non-visual parity | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/interaction-parity-and-release.md`:249 |
| `RFC9-49` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/interaction-parity-and-release.md`:264 |
| `RFC9-50` | No ambient motion at V0 | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/interaction-parity-and-release.md`:289 |
| `RFC9-51` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/interaction-parity-and-release.md`:295 |
| `RFC9-52` | This contract schedules nothing | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/interaction-parity-and-release.md`:304 |
| `RFC10-1` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md`:44 |
| `RFC10-2` | Service-and-client boundary | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md`:53 |
| `RFC10-3` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md`:67 |
| `RFC10-4` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md`:79 |
| `RFC10-5` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md`:96 |
| `RFC10-6` | A mission is not work, and work is never proof | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md`:148 |
| `RFC10-7` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/prevention-envelope-and-attention.md`:42 |
| `RFC10-8` | No self-widening — the load-bearing rule | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/prevention-envelope-and-attention.md`:109 |
| `RFC10-9` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/prevention-envelope-and-attention.md`:149 |
| `RFC10-10` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/prevention-envelope-and-attention.md`:167 |
| `RFC10-11` | Bound exhaustion never self-extends | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/prevention-envelope-and-attention.md`:202 |
| `RFC10-12` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/prevention-envelope-and-attention.md`:215 |
| `RFC10-13` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/prevention-envelope-and-attention.md`:231 |
| `RFC10-14` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md`:174 |
| `RFC10-15` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0009/semantic-geography.md`:181 |
| `RFC10-16` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md`:186 |
| `RFC10-17` | Budget is reserved, and reservation is enforcement, never accounting alone | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/budget-reservation.md`:42 |
| `RFC10-18` | Completion is reported by the executor and established by another | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/effects-recovery-and-stop.md`:43 |
| `RFC10-19` | Effects are classified before they are authorized | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/effects-recovery-and-stop.md`:152 |
| `RFC10-20` | What stop guarantees | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/effects-recovery-and-stop.md`:244 |
| `RFC10-21` | Cross-project composites carry every embedded project's consent requirement | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/portfolio-and-cross-project-consent.md`:57 |
| `RFC10-22` | The attention queue is bounded | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/prevention-envelope-and-attention.md`:244 |
| `RFC10-23` | Effect dimensions are recorded separately, and no single predicate collapses them | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/effects-recovery-and-stop.md`:291 |
| `RFC10-24` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md`:204 |
| `RFC11-1` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`:43 |
| `RFC11-2` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`:64 |
| `RFC11-3` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`:71 |
| `RFC11-4` | Mandatory context is selected deterministically | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/deterministic-selection-and-budget.md`:42 |
| `RFC11-5` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`:80 |
| `RFC11-6` | Incomplete is Unknown, and Unknown blocks when policy says complete | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`:85 |
| `RFC11-7` | No second truth store | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`:98 |
| `RFC11-8` | Raw chat history is not canonical project memory | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`:106 |
| `RFC11-9` | Retention and privacy boundaries | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`:121 |
| `RFC11-10` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`:132 |
| `RFC11-11` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/deterministic-selection-and-budget.md`:148 |
| `RFC11-12` | — | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`:150 |
| `RFC11-13` | Every active contract declares its implementation boundary | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/deterministic-selection-and-budget.md`:71 |
| `RFC11-14` | Dependency traversal is defined, bounded, and recorded | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/deterministic-selection-and-budget.md`:100 |
| `RFC11-15` | Doctrine and craft rule ownership is declared, not judged | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/deterministic-selection-and-budget.md`:128 |
| `RFC11-16` | constrains is consumed clause-first | `.syzygy/governance/contracts/candidates/rfcs/RFC-0011/deterministic-selection-and-budget.md`:140 |

## Cited without a definition site

Every identifier above was found at a **heading or a leading bold run** —
the two places this corpus marks a definition. The identifiers below appear
in their family's own files but never at such a site. Three different things
produce that, and the register does not guess which:

- a **cross-family citation** — an RFC-0003 clause naming an RFC-0001 clause
  is a citation, and the definition sits in the other module (verification
  rule 5: a citation is not a reliance);
- a clause defined in **running prose** rather than at a marked-up site,
  which is a markup gap, not a missing rule;
- a genuine **dangling reference** to a clause that no longer exists.

Resolving one means opening the citing line, not trusting this table.

| Identifier | Family it was cited in |
|---|---|
| `RFC10-16` | Design contract clauses |
| `RFC11-12` | Design contract clauses |

## What this page will not tell you

It does not say what any clause requires — that is the clause's job, and
keeping the body out of this page is the whole reason it is safe to generate.
It does not say which identifiers a task must load;
`.syzygy/governance/contracts/candidates/TASK-ROUTER.md` routes by task. It
does not define the identifier forms; `PROCESS-GLOSSARY.md` does. It does not
say what is in force beyond naming each family's home and status;
`PROJECT-STATUS.md` and the act record own that. And it resolves no
disagreement between two homes: it shows you both and leaves the
contradiction visible, which is what CC-REV-3 asks for.

