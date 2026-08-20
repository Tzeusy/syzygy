# Contract coverage — project-registration-and-honest-shape-visibility

> **CC-SPEC-8 coverage matrix, shipped with the specification.** Rows are
> **per observable consequence, not per clause** (the unit RFC1-33 and
> RFC6-28 fix). Consequence phrasings below are row labels for mapping
> only — the clause text is the authority, and nothing here restates a
> clause normatively.
>
> **No N/A is minted on the author's authority.** Under CC-SPEC-8 a
> reviewed N/A judgment is a recorded **owner** judgment homed in
> `decisions/`, honored only where RFC3-16(a) provenance verifies. **No
> such judgment exists for any clause today**, so every consequence not
> covered by a requirement renders **Unknown pending owner-reviewed
> N/A** — never covered, never silently omitted (VIS-2). "Believed not
> applicable" below is the author's application of CC-SPEC-8's
> applicability test, offered to the owner; it settles nothing.

## Population and denominator

`[Observed]` The accepted clause population is the Wave A/B install:
**324 defined clause identifiers across the 30 modules at
`contracts/rfcs/`** (RFC 0001–0009). Counted this session by two
methods that agree exactly per family: (1) a Python `re` sweep over the
30 module files for clause-definition headers; (2) the clause rows of
the generated `05-CONTRACT-INDEX.yaml`, excluding its RFC10/RFC11 rows
(deferred candidates, not accepted, outside this population).

| Family | Accepted clauses | Mapped by this spec | Not mapped |
|---|---|---|---|
| RFC1 | 39 | 8 | 31 |
| RFC2 | 27 | 3 | 24 |
| RFC3 | 38 | 11 | 27 |
| RFC4 | 32 | 0 | 32 |
| RFC5 | 27 | 1 | 26 |
| RFC6 | 28 | 11 | 17 |
| RFC7 | 41 | 4 | 37 |
| RFC8 | 32 | 0 | 32 |
| RFC9 | 60 | 0 | 60 |
| **Total** | **324** | **38** | **286** |

The 38 mapped clauses are exactly the `contracts[]` union in the
generated `GOVERNING-DEPENDENCIES.md`; Part A gives their
per-consequence rows. The 286 unmapped clauses are disposed in Part B.
(RFC8-18 and RFC8-19 were mapped by the Pass 1 draft and moved to
Part B in the Pass 3 repair: both are cost-scoped clauses, and this
capability renders no cost — the round-2026-08k RS-3 review's first
blocker.)

## Part A — mapped clauses, per observable consequence

Disposition vocabulary: **covered** (the named requirements' oracles
observe the consequence) or **Unknown** (no requirement covers it and no
owner-reviewed N/A exists).

**Row method.** `[Inferred]` Rows aim at one row per normatively
distinct obligation limb of the clause's text, judged by the author
from the accepted bytes; the clause text, not the row label, is the
authority. Known folds, disclosed rather than hidden: RFC2-23's six
closed degradation states fold into two rows; RFC6-19's thirteen fact
content classes fold into four rows (classes 1–6 and 8–13 ride the
general content-classes row); RFC5-3's admission rule is one row. No
method demonstrates that every clause's limb set was exhausted — a
reviewer who finds an unlisted limb has found a real gap, exactly as
the round-2026-08k RS-3 review did for RFC3-1's parse-disagreement
limb (repaired below).

| Clause | Observable consequence (row label) | Disposition | Requirements |
|---|---|---|---|
| RFC1-1 | one governance root designates the project | covered | CAP1-REQ-001 |
| RFC1-1 | two roots yield an owner-routed contradiction, no winner picked | covered | CAP1-REQ-006 |
| RFC1-1 | zero roots yield workspace-level `Unknown` `missing-declaration`, no kernel contradiction | covered | CAP1-REQ-006 |
| RFC1-2 | rename changes the label, never the identity | covered | CAP1-REQ-060 |
| RFC1-3 | observation authority exists only per consented (project, repository) pair | covered | CAP1-REQ-011, CAP1-REQ-016 |
| RFC1-3 | a declared but unconsented repository renders unconsented, not observed | covered | CAP1-REQ-010, CAP1-REQ-012 |
| RFC1-4 | every declared repository has an explicit membership/coverage state | covered | CAP1-REQ-010 |
| RFC1-9 | deterministic identity: same inputs at one evaluation yield the same served facts | covered | CAP1-REQ-005 |
| RFC1-10 | identifiers are opaque and stable across rename and relocation | covered | CAP1-REQ-060 |
| RFC1-10 | a path or location is a designation or label, never an identity | covered | CAP1-REQ-020, CAP1-REQ-060 |
| RFC1-22 | proposed-plane material anchors and binds nothing in current state | covered | CAP1-REQ-063 |
| RFC1-27 | a Proposal renders unmistakably as proposed material | covered | CAP1-REQ-053, CAP1-REQ-063 |
| RFC1-27 | an unadopted Proposal changes no served status | covered | CAP1-REQ-004, CAP1-REQ-063 |
| RFC1-27 | Proposal exclusivity-group and adoption mechanics | **Unknown** — no requirement here exercises adoption mechanics; would be settled by an owner-reviewed N/A or a later capability's requirements | — |
| RFC2-19(a) | merged-but-unreconciled renders as a fact of the render, no thirteenth reason minted (as exempted, ratified SDR-34) | covered | CAP1-REQ-037 |
| RFC2-23 | degradation states render distinguishably; degrade-to-last-good is marked stale/broken | covered | CAP1-REQ-013, CAP1-REQ-062 |
| RFC2-23 | a partial capture declares its captured scope | covered | CAP1-REQ-014 |
| RFC2-24 | every `Unknown` carries a primary reason verbatim from the closed twelve | covered | CAP1-REQ-002, CAP1-REQ-006, CAP1-REQ-012, CAP1-REQ-013, CAP1-REQ-022, CAP1-REQ-030, CAP1-REQ-034, CAP1-REQ-051, CAP1-REQ-062 |
| RFC2-24 | secondary reasons render beside the primary, marked, never folded | covered | CAP1-REQ-035 |
| RFC2-24 | no reason is minted outside the closed vocabulary | covered | CAP1-REQ-012, CAP1-REQ-037 |
| RFC3-1 | the declaration is a semantic contract read at the fixed path in the fixed dialect; whether a governance root exists follows from whether it parses | covered | CAP1-REQ-001, CAP1-REQ-002 |
| RFC3-1 | two implementations disagreeing on whether one `project.yaml` parses is an owner-routed contradiction, never a kept dialect preference | **Unknown** — no requirement here exercises cross-implementation parse disagreement; would be settled by an owner-reviewed N/A or a conformance-suite capability's requirements | — |
| RFC3-2 | drafted governance content renders unadopted | covered | CAP1-REQ-004 |
| RFC3-3 | direct writes are confined to the two namespaces | covered | CAP1-REQ-023, CAP1-REQ-053, CAP1-REQ-061 |
| RFC3-3 | a write-widening manifest field is inoperative and renders as a contradiction | covered | CAP1-REQ-061 |
| RFC3-4 | the declaration file's location designates the governance root | covered | CAP1-REQ-001, CAP1-REQ-006 |
| RFC3-5 | the declaration's top-level field set is closed at the listed fields, each with its declared write authority | covered | CAP1-REQ-001, CAP1-REQ-003 — the closed set is the validation subject; naming the failed field is this specification's own authored strictness, not a consequence RFC3-5 states |
| RFC3-6 | consent records are per repository, with repository identity never a URL/path | covered | CAP1-REQ-010, CAP1-REQ-011, CAP1-REQ-060 |
| RFC3-6 | an unconsented repository renders per the policy rendering | covered | CAP1-REQ-012 |
| RFC3-7 | a consent record's scope, attribution, and grant state are rendered facts | covered | CAP1-REQ-011 |
| RFC3-7 | absence of a resolvable in-force record renders as absence of consent | covered | CAP1-REQ-011, CAP1-REQ-016 |
| RFC3-9 | declarations are never auto-repaired; repair travels as an unadopted Proposal | covered | CAP1-REQ-004 |
| RFC3-9 | an unparseable or invalid declaration renders every dependent claim `Unknown`, never partial registration | covered | CAP1-REQ-002, CAP1-REQ-003 — the accepted text's obligation is the `Unknown` rendering and the no-auto-repair rule; failing *by name* is this specification's own authored strictness |
| RFC3-16 | effective status derives from the owner-act record, never the self-declared stamp | covered | CAP1-REQ-046 |
| RFC3-16 | stamp/status disagreement is disclosed; the effective status governs | covered | CAP1-REQ-046 |
| RFC3-16(a) | unverifiable owner-act provenance renders the artifact effectively unadopted | covered | CAP1-REQ-046 |
| RFC3-30 | consent scope admits exactly the granted (project, repository) access, no cross-project bleed | covered | CAP1-REQ-016 |
| RFC5-3 | clients are classified by presented credential, never network location; facts go only to admitted clients | covered | CAP1-REQ-015 |
| RFC6-7 | answers pin to an evaluation identity; a repeated equivalent query is stable | covered | CAP1-REQ-005, CAP1-REQ-042 |
| RFC6-13 | one truth serves both consumers through the machine-queryable plane | covered | CAP1-REQ-015, CAP1-REQ-041, CAP1-REQ-046 |
| RFC6-14 | epistemic labels travel verbatim to every consumer | covered | CAP1-REQ-041, CAP1-REQ-045 |
| RFC6-14 | closed vocabularies render with verbatim spellings | covered | CAP1-REQ-013, CAP1-REQ-035, CAP1-REQ-050 |
| RFC6-14 | an aggregate carries no epistemic state of its own | covered | CAP1-REQ-031, CAP1-REQ-044 |
| RFC6-15 | answers are evaluation-stamped; equivalent queries expose equivalent facts | covered | CAP1-REQ-005, CAP1-REQ-042 |
| RFC6-16 | partial-scope answers disclose their scope | covered | CAP1-REQ-014 |
| RFC6-17 | aggregation disclosure: membership count, full composition, expansion to members | covered | CAP1-REQ-044 |
| RFC6-18 | one "Why this answer?" fact set per (selection, evaluation, scenario context) | covered | CAP1-REQ-033, CAP1-REQ-040 |
| RFC6-18 | answers stand independently on their own fact sets | covered | CAP1-REQ-030, CAP1-REQ-038 |
| RFC6-19 | the fact set carries the accepted content classes and nothing unwarranted | covered | CAP1-REQ-040 |
| RFC6-19 | the coverage-boundary class is served (executed coverage records + declared captured scope) | covered | CAP1-REQ-015 |
| RFC6-19 | the reconciliation-state class renders honestly (uncomputed → evidence absent) | covered | CAP1-REQ-037 |
| RFC6-19 | constituent facts behind an answer are reachable | covered | CAP1-REQ-033 |
| RFC6-22 | rendering equivalence holds across channels on existence, labels, reasons, freshness, values, counts | covered | CAP1-REQ-041, CAP1-REQ-043 |
| RFC6-23 | a rendering disagreement is a blocking defect, never resolved by presentation precedence | covered | CAP1-REQ-043 |
| RFC6-26 | unconsented content renders as a standing policy state with its resolution route | covered | CAP1-REQ-012 |
| RFC7-33 | every human-view distinction is machine-readable; parity of distinctions | covered | CAP1-REQ-045, CAP1-REQ-064 |
| RFC7-33 | generated presentation is non-citable and never a source | covered | CAP1-REQ-021, CAP1-REQ-045 |
| RFC7-34 | distinctions are recoverable without colour, position, or layout | covered | CAP1-REQ-064 |
| RFC7-39 | one fixed entry path is the primary narrative — not two front doors | covered | CAP1-REQ-020 |
| RFC7-39 | the entry is governed presentation, never authority; it routes by identifier | covered | CAP1-REQ-021 |
| RFC7-39 | absent/unreadable/stale/contradictory entry states render honestly | covered | CAP1-REQ-022 |
| RFC7-40 | one four-value discoverability finding per repository, at the producing evaluation | covered | CAP1-REQ-050 |
| RFC7-40 | `yes`/`no` rest on current captured evidence; missing evidence renders `Unknown` with reason | covered | CAP1-REQ-051 |
| RFC7-40 | `not-applicable` only under its accepted condition, with the basis served | covered | CAP1-REQ-052 |
| RFC7-40 | the link may be proposed, never written; a proposal never flips the finding | covered | CAP1-REQ-053 |

Part A totals `[Observed, computed by the sweep in "Verifying this
table"]`: **65 consequence rows over 38 clauses — 63 covered, 2
Unknown.**

## Part B — accepted clauses not mapped by any requirement

`[Inferred]` The author applied CC-SPEC-8's applicability test — *does
Capability 1 use the entity, behavior, authority boundary, state
vocabulary, or interface the clause governs?* — and believes the 286
unmapped clauses govern machinery Capability 1 neither renders, stores,
transitions, queries, nor crosses. **That belief is not a reviewed N/A.**
Until the owner records N/A judgments in `decisions/` with verifiable
RFC3-16(a) provenance, every one of these clauses' consequences renders
**Unknown pending owner-reviewed N/A**:

| Module group | Unmapped clauses | Chiefly governs (author's reading, non-binding) |
|---|---|---|
| RFC 0001 remainder | 31 | kernel entity/relation taxonomy, state-plane mechanics, claim/challenge/contradiction lifecycles beyond the rendered postures used here |
| RFC 0002 remainder | 24 | snapshot/evaluation internals, challenge lifecycle, reconciliation-chain computation this spec defers |
| RFC 0003 remainder | 27 | manifest fields and governance-home mechanics beyond declaration/consent/status reading |
| RFC 0004 (all) | 32 | work ingestion, execution records, fidelity joins — Trajectory-family machinery |
| RFC 0005 remainder | 26 | auth/session/exposure machinery beyond the credential-classing rule |
| RFC 0006 remainder | 17 | selection/query/drawer mechanics beyond the clauses mapped |
| RFC 0007 remainder | 37 | Polaris comprehension surfaces, walkthrough machinery, white-paper composition |
| RFC 0008 (all) | 32 | Orrery map/aggregation and cost machinery — including RFC8-18/RFC8-19, whose subject is cost measures this capability never renders (moved here by the Pass 3 repair) |
| RFC 0009 (all) | 60 | cross-view/integration machinery |
| **Total** | **286** | |

## Verifying this table

- Denominator: re-run the two counting methods named above; both must
  return 324 for RFC1–9.
- Mapped set: `python3 scripts/build_capability_1_spec_dependencies.py
  --check` — Part A's clause column must equal the generated
  `contracts[]` union (38 identifiers), and 38 + 286 = 324.
- Part A totals: count rows and dispositions in this file's Part A table
  (e.g. Python over the `| RFC` rows); the printed totals above must
  match the count — they were computed that way, not transcribed.
