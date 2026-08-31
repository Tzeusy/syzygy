# Surface-clause routing matrix

> **Not a contract, and not authority.** This file records, for every clause
> of RFC 0006–0011, where that clause's content belongs *after* foundational
> acceptance. Where it and a clause disagree, **the clause wins**. It creates
> no OpenSpec content — none may exist in this phase — and it schedules
> nothing.

## Why this file exists

Eleven contracts each carry the same binding phase rule — RFC1-33,
RFC2-26, RFC3-33, RFC4-30, RFC5-27, RFC6-28, RFC7-38, RFC8-32, RFC9-52,
RFC10-16, RFC11-12 (this file's full per-clause rows cover RFC 0006–0011;
RFC 0001–0005's full enumerations are staged at surface specification — a
scoping choice of this file, **not** a property of those contracts' phase
clauses, whose staging sentence is the same as the included six; the
Capability 1 clauses an author needs now are routed in the authoring
supplement below): *no implementation work for
user-observable behavior may be scheduled solely from that RFC.* Every
observable consequence must first map to an approved OpenSpec requirement, or
carry an explicit reviewed judgment that it has no independently testable
behavior.

That rule is only as good as the enumeration behind it, and that enumeration
has two layers with different units. **This matrix is the first layer only —
the clause-level routing enumeration**: every declared clause identity of
RFC 0006–0011, each routed exactly once — a population CG-17
(`scripts/check_governance.py`) recomputes against this file's rows every
battery run; its printed count, not any figure in this file, is the total of
record. **The second layer — the per-observable-consequence coverage
enumeration the phase clauses actually gate on — is not this file and cannot
be**: every phase clause states "rows are per observable consequence, not per
clause; a complete-looking matrix over under-enumerated consequences is a
defect of the matrix", and that coverage matrix is the surface-specification
deliverable each phase clause stages (review material, never authority). A
row here answers *where a clause's observable limb routes*; it never answers
*how many requirements cover that clause* — treating one route per clause as
coverage is exactly the defect the phase clauses name.

## The four routes

Every clause carries exactly one:

| Route | Meaning | What it obliges |
|---|---|---|
| **OS** | Has user-observable behavior | Becomes a future OpenSpec requirement/scenario in the **named** domain. The RFC keeps any invariant limb; the observable limb routes |
| **N/A** | Pure structural invariant, reviewed | Nothing — but the row must say *why no scenario could assert anything distinct*. N/A is a judgment on the record, not a default |
| **CR** | Craft, review, or release-gate obligation | Lands in craft-and-care or the release policy |
| **IR** | Informative rationale | Binds nothing; stays as non-normative text |

**A clause staying normative in its RFC does not exempt it from OS.** Those
are orthogonal properties, and conflating them is what the previous
revision got wrong (below).

## What changed, and why the previous revision was not usable

`SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md` — superseded by this file — used a
fifth class, `DESIGN-INVARIANT (DI)`, as though it were a routing decision.
It is not: it answers *does this stay in the RFC?*, not *does this have
behavior a spec must pin?* REV10 also disclaimed the confusion in its own
prose (":229-231": a DI class "never exempts a clause's observable
consequences from OpenSpec coverage") while leaving 129 DI rows carrying no
routing decision at all.

Three consequences, all measured rather than estimated:

- **RFC-0006 had zero rows.** Its 28 clauses — selection, URL resolution, the
  nine resolution outcomes, the drawer, endpoint parity — are the most
  directly user-observable material in the corpus, and it was the domain the
  readiness report sequenced as changeset #1. It now has 28 rows: 27 OS, 1
  CR (RFC6-28, re-decided from N/A on 2026-08-10 — note 3 in its section).
- **RFC-0007 was under-enumerated.** REV10 listed 39 rows; the contract
  declares **45** clause identities. Six sub-clauses (`RFC7-2(b)`, `(c)`,
  `RFC7-9(b)`, `(c)`, and two others) appear only as inline `**(b)` markers
  inside a parent clause body, and a `\b`-anchored regex silently drops them
  — after `)` there is no word boundary. All 45 are present here.
- **Re-deciding DI on the merits moved almost everything.** Of RFC-0009's 50
  DI rows, **47 re-decide as OS**. A coverage skeleton built from REV10 would
  have carried roughly five map clauses into surface specification instead of
  fifty-three, while looking complete.

`10-EXIT-REPORT.md:75` claimed REV10 "classifies all 322 clauses". It
classified 150 of 322 (46.6%). That claim is retired here rather than
deleted, because the number was load-bearing for a readiness judgment.

## Totals — computed by the battery, never carried in this file

A grand-total table used to sit here. Measured this session (2026-08-10),
it had gone stale against this file's own rows: the table still summed
**199** while the rows count **210** — the RFC-0010/0011 package-split rows
landed and the table did not move. That is the transcribed-derived-value
failure the verification rules name, recurring inside the artifact that
exists to be an enumeration, so the table is withdrawn rather than patched:

- **Population and uniqueness:** CG-17 (`scripts/check_governance.py`)
  recomputes, every run, the declared RFC 0006–0011 clause identities
  against this file's rows and fails on any clause routed zero times or
  twice. Its printed examined-count is the total of record.
- **Per-route split:** each per-contract section carries its tally line
  beside the rows it counts. Read the split there, next to what it counts —
  never from a summary at this distance.

**Read the shape honestly, without the withdrawn arithmetic.** Nearly every
clause in the surface corpus routes to OpenSpec, and only a handful survive
as structural N/A. That is the correct result for six contracts that exist
to describe what a person or an agent sees — but it also means the
specification phase ahead is large, and any plan that assumed most of this
was "already settled in the RFCs" was working from the previous revision's
arithmetic.

**IR is zero by construction, not by finding.** Bracketed
`[Inferred]`/`[Observed]` passages and §0/§1/§5/§6 prose are informative by
definition and are not enumerated row-by-row; only numbered clauses are.

## Future specification domains

Provisional names, minted for routing only. Nothing here creates a domain.

`spec/selection-api` · `spec/intent-surface` · `spec/work-surface` ·
`spec/map-surface` · `spec/map-scenes` · `spec/map-lenses` ·
`spec/mission-control` · `spec/context-packets` · `spec/registration`
(the ninth, minted 2026-08-10 for the Capability 1 authoring supplement —
registration, declaration validation, and consent recording flows)

One further domain is **proposed, not minted**: `spec/platform-service`, for
RFC10-2/RFC10-3's service-and-client topology and machine-client admission,
which bind every surface's clients rather than Mission Control's alone. The
owner decides whether to mint it or keep those limbs in
`spec/mission-control`.

## Capability 1 authoring supplement — RFC 0001–0005 clauses on the first spec's path

*(Added 2026-08-10, RD28-01.)* The launch scope is Capability 1 — project
registration and honest shape visibility — and its trace table
(`round-2026-08e/FIRST-SPEC-TRACE-TABLE.md`) names eleven governing clauses
from RFC 0001–0005 that the full per-clause tables above deliberately stage.
An author must not be left improvising on exactly those clauses, so they are
routed here, by the same four-route vocabulary. **Scope note:** this
supplement routes the trace table's clauses only; it is not the RFC
0001–0005 full enumeration, which remains staged at surface specification
per each phase clause. CG-17's recomputed population is deliberately scoped
to RFC 0006–0011 and does not count these rows; where a row here and a
clause disagree, the clause wins.

| Clause | Route | Domain | The rule (clause wins; read it) | What a spec must assert |
|---|---|---|---|---|
| RFC1-1 | OS | `spec/registration` | A Project is repositories plus exactly one governance root; two roots is a well-formed contradiction minted in the Project's own evaluation, zero roots is unevaluable as a Project and surfaces at the workspace level as Unknown (`missing-declaration`), no kernel contradiction minted | A scenario per limb: a declaration resolving to two roots renders an owner-routed contradiction, never silent repair; a project with zero roots renders workspace-level Unknown with its reason, is never dropped, and mints nothing in a Project evaluation |
| RFC1-3 | OS | `spec/registration` | Every observed repository requires a recorded consent record; no consent means no observation and therefore Unknown — never an empty graph read as absence | A scenario must assert an unconsented repository renders Unknown (`unconsented-source-or-provider`), not an empty or missing entry, and that egress consent is a separate per-(Project, provider) instance never folded into observation consent |
| RFC1-7 | OS | `spec/registration` | Extension profiles are named, per-project-loadable, never presumed present; the mission profile is loadable only where the Mission contracts are accepted and active | A scenario must assert an undeclared profile's entities are absent without error, a declared profile loads its vocabulary, and the mission profile refuses to load where RFC 0010 is unaccepted (deferred-wave posture rendered honestly) |
| RFC2-24 | OS | every consuming surface's domain — first `spec/registration` | Every Unknown claim instance carries exactly one primary reason from the closed twelve-reason list, verbatim on every machine answer (RFC6-14) | Capability 1's scenarios must assert reasons render verbatim from the vocabulary — at minimum `missing-declaration` (#1) and `unconsented-source-or-provider` (#6) on the registration paths — and that no rendering mints a reason outside the list |
| RFC3-1 | OS | `spec/registration` | The declaration is the file `.syzygy/project.yaml`; its exact YAML dialect is fixed by the first accepted spec that parses it and is a conformance item from then on | The first spec that parses the declaration must pin the dialect (version, coercion rules, duplicate-key handling); a scenario must assert two implementations agree on whether a given `project.yaml` parses, with disagreement routed to the owner as a contradiction |
| RFC3-4 | OS | `spec/registration` | Location is designation: the declaration's location in exactly one repository designates the governance root; a declaration designating a different root, or a Project resolving to two roots, is a contradiction per RFC1-1; zero roots follows RFC1-1's workspace-level rule | A scenario must assert designation follows file location and never a field value, with the two-roots and zero-roots limbs rendering per RFC1-1's split |
| RFC3-5 | OS | `spec/registration` | The declaration's top-level field set is closed, each field naming one write authority (RFC3-2); additions require amendment | A scenario must assert an undeclared top-level field renders the declaration invalid (a named failure, never partial registration), and that per-field authority is honored — Syzygy-drafted membership renders unadopted until owner sign-off |
| RFC3-6 | OS | `spec/registration` | Repository identity is the declared opaque identifier, never URL, path, or branch; an entry whose consent reference does not resolve to an in-force record is not observed | A scenario must assert locator-hint changes never move identity, and an unresolved consent reference renders the entry's content Unknown (`unconsented-source-or-provider`), never an empty graph |
| RFC3-7 | OS | `spec/registration` | Consent records are governance acts in `.syzygy/governance/decisions/`, referenced never embedded; observation consent is per (observing Project, repository), egress consent one record per (Project, provider) naming the permitted set | A scenario per kind: an embedded consent value is invalid; observation consent for one project never admits another; egress renders Unknown absent the (Project, provider) record |
| RFC3-9 | OS | `spec/registration` | Drafted declaration content renders unadopted and binds nothing; an unparseable or invalid `project.yaml` renders every dependent claim Unknown; Syzygy never auto-repairs — repair is a Proposal through the owner gate | A scenario must assert the invalid-declaration path yields Unknown on dependents plus a Proposal route, with no silent write to the declaration and no partial registration |
| RFC5-3 | OS | `spec/platform-service` (proposed, not minted — the owner decides; these limbs bind every surface's clients) | Every request is exactly one of two client classes, by credential presented, never by network location or header heuristics; the two classes are exhaustive for all present and future clients | A scenario must assert a request with a valid machine credential is machine-class and every other request is browser-class, that loopback location and header absence classify nothing, and that registration endpoints admit each class only under its own discipline |

Tally, this section: 11 rows, 11 OS. The supplement inherits every standing
caveat; in particular no row here schedules anything, and the
per-consequence coverage enumeration for these clauses is staged exactly as
for every other clause.

## Standing caveats

- **RFC 0001–0005 are not fully enumerated here, and the reason is
  staging, not absence of observable behavior.** *(Restated 2026-08-10,
  RD28-01 — the previous form of this caveat claimed their observable
  consequences reach users exclusively through the six rule-carrying
  contracts above and that RFC 0005's ceremony, login, and consent
  experiences carry no phase rule of their own. Both claims were false
  against the corpus: RFC1-33 and RFC3-33 enumerate their own
  user-observable consequences — "project registration and declaration
  validation flows" is Capability 1 itself — and RFC5-27 is precisely the
  phase rule for those RFC 0005 experiences.)* All eleven contracts carry a
  binding phase rule; this file's full per-clause rows cover RFC 0006–0011,
  the RFC 0001–0005 full enumerations are staged at surface specification,
  and the Capability 1 authoring supplement below routes the RFC 0001–0005
  clauses on the first spec's path so an author is not left without the
  routing authority's answer. Any bypass found is a gap to route, never a
  licence to schedule.
- **RFC-0010 remains candidate, and its doctrine alternative is satisfied.**
  Owner ruling `BOUNDED-MISSION-DOCTRINE-INTERPRETATION-2026-08-31`
  satisfies RFC10-24's owner-ruling alternative without amending doctrine.
  It does not accept RFC 0010, sign its required OpenSpec behavior, or approve
  a mission; operation remains unavailable until those independent gates and
  every mission gate pass.
- **The `CR` rows point at homes that are candidates or absent.** The
  coverage-matrix obligation now has a named candidate home — the
  specification-acceptance policy candidate, CC-SPEC-8 (approved by no act)
  — but no release-policy artifact exists at all, and naming where an
  obligation belongs does not create its home. Count the CR rows from the
  tallies beside them, not from a figure here.
- **Routing is a judgment, and judgments carry doubt.** 27 rows were flagged
  doubtful by their authors, with the alternative route and its tally shift
  recorded in the per-contract notes. A reviewer can flip any of them on
  stated grounds — which is the point of recording the doubt rather than
  smoothing it.

## Method

Each contract was routed by an independent fresh-context pass reading only
that contract, the four-route rule, and the previous revision's rationale
column (never its DI class). Clause identities were enumerated with Python
`re`, not shell `grep` — `grep` on the authoring machine is ugrep, where
`[^]]`-style classes silently match nothing. Two enumeration regexes were
corrected mid-pass after a second-method reconciliation against each
package README's declared inventory caught silently dropped sub-clauses;
both corrections are recorded in the per-contract method lines below.

---

## RFC-0006 — Cross-Surface Selection, Query and Evidence Drawer


**Enumeration method:** clause IDs were enumerated with Python `re` (never
`grep` — `grep` on this machine is ugrep and silently mismatches bracket
classes). Two independent passes over
`.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md`:

1. **Every mention**, to catch any lettered sub-clause anywhere in the file:
   `re.compile(r'RFC6-(\d+)(\([a-z]\))?')` → `finditer` over the whole file,
   72 occurrences, **28 unique** IDs, **zero** with a lettered limb.
2. **Definition sites only**, to confirm each ID is actually defined here:
   `re.compile(r'\*\*(RFC6-\d+(?:\([a-z]\))?) —')` → **28** definitional
   headers, in file order, identical to the unique set from pass 1.

Both passes agree exactly, and both agree with the RFC's own front-matter
declaration (`clauses: "RFC6-1..RFC6-28 (no gaps; none retired, merged, or
renumbered)"`) and its closing marker. **No lettered sub-clauses exist in
RFC-0006** — unlike RFC-0007 and RFC-0009, it carries none, so the inclusive
and exclusive clause conventions give the same number here.

**Clauses found:** 28 — RFC6-1, RFC6-2, RFC6-3, RFC6-4, RFC6-5, RFC6-6,
RFC6-7, RFC6-8, RFC6-9, RFC6-10, RFC6-11, RFC6-12, RFC6-13, RFC6-14, RFC6-15,
RFC6-16, RFC6-17, RFC6-18, RFC6-19, RFC6-20, RFC6-21, RFC6-22, RFC6-23,
RFC6-24, RFC6-25, RFC6-26, RFC6-27, RFC6-28

| Clause | Route | Future spec domain | Retained invariant in the RFC | Justification |
|---|---|---|---|---|
| RFC6-1 | OS | `spec/selection-api` | The reference tuple is RFC 0001's identity space verbatim (RFC1-5, RFC1-9/10) — the kernel mints no selection-specific identifier — and surfaces may keep private rendering handles internally | A spec must assert that anything crossing a surface boundary, a URL, or an endpoint is keyed only by (entity kind, durable identity), and that a request keyed on a file path, node index, work-item row, layout coordinate, or scene object id is refused rather than served |
| RFC6-2 | OS | `spec/selection-api` | Selection anchors on the durable identity level (SDR-2); the evaluation qualifier picks the instance, never the identity | A spec must assert, per V0-core entity kind (RFC1-5), that the entity is selectable by reference, and that selecting a claim or gap returns its durable identity with the qualifier deciding which instance answers |
| RFC6-3 | OS | `spec/selection-api` | Evaluations may never be silently mixed; a skew disclosure must name **both** evaluation identities, not merely flag staleness | A spec must assert that one reference opened in Polaris, Trajectory and Orrery yields the same entity, evaluation, scenario context and drawer fact set, and that a surface able to answer only at a different evaluation renders the skew explicitly |
| RFC6-4 | OS | `spec/selection-api` | "Current" is always somebody's evaluation identity (RFC2-3), and status never changes without a new identified evaluation (RFC2-4) | A spec must assert that an unqualified selection resolves at the latest identified evaluation available at resolution time and that the answer names it — including the case where the same unqualified selection honestly answers differently tomorrow, still stamped |
| RFC6-5 | OS | `spec/selection-api` | The outcome set is **closed at nine values** — no tenth outcome, and no surface or endpoint may return anything outside it | A spec must assert one scenario per outcome carrying its stated obligation (successors offered but never auto-redirected; `resolved-absent` naming the evaluations where the entity is present; `not-applicable` still offering the drawer and naming the surfaces that do project it; `unresolvable` naming what failed to resolve), and that silence, an empty panel, a dropped selection, a bare 404 and an unexplained error page never occur |
| RFC6-6 | OS | `spec/selection-api` | Navigation outcomes and claim statuses are disjoint types; RFC2-24's reason registry gains no navigation member | A spec must assert that a `retired`, `not-applicable`, `resolved-absent` or `unresolvable` outcome carries no RFC2-24 Unknown reason and contributes zero to any Unknown count or aggregate composition — a countable assertion, not a naming preference |
| RFC6-7 | OS | `spec/selection-api` | Resolution sits inside the deterministic layer (VIS-7); only display formatting is excluded from that guarantee | A spec must assert that two resolutions of the same (reference, evaluation identity, scenario context) — repeated in one surface and compared across surfaces — return an identical outcome and an identical fact set |
| RFC6-8 | OS | `spec/selection-api` | The pinnable set is closed at four identity-bearing components, and URL *spelling* (path shape, parameter names, encoding) is deliberately unbound — no downstream requirement may fix a spelling by citing this clause | A spec must assert that stripping every presentation hint from a URL yields the same entity, evaluation and fact set, i.e. that preferred surface and view state are provably non-identity-bearing |
| RFC6-9 | OS | `spec/selection-api` | URLs embed opaque durable identifiers (RFC1-10), never labels, paths or coordinates; a URL that breaks on rename has embedded a surface-local handle and violates RFC6-1 | A spec must assert that renaming a capability, moving a file, or re-laying-out the map leaves every affected URL resolving unchanged to the same entity |
| RFC6-10 | OS | `spec/selection-api` | Both temporalities are legitimate — pinned shares an answer, unpinned shares a question; pinned resolution rests on VIS-6 exception (b) | A spec must assert that an evaluation-pinned URL resolves against the immutable observation record and renders visible staleness once superseded (never silently newer state), that an unpinned URL resolves per RFC6-4, and that the rendering discloses which of the two the reader is holding |
| RFC6-11 | OS | `spec/selection-api` | Following a successor is a **reader act**: a merge or split is a governance event the reader must see, never an equivalence the kernel may assume | A spec must assert that a URL pinning a retired identity returns outcome `retired` with the retirement record, its `succeeds` edges and offered successors — never a 404, never a redirect — and that evaluation-pinned URLs to that identity keep resolving indefinitely |
| RFC6-12 | OS | `spec/selection-api` | A surface hint is a presentation hint under RFC6-8, so it can never partition the selection space into per-surface namespaces | A spec must assert that a URL-pinned selection opens in any surface (subject only to `not-applicable`), that the same URL body with different surface hints is one selection, and that a bookmark made in one surface is honored by the others |
| RFC6-13 | OS | `spec/selection-api` | One kernel-computed fact set serves both consumers; no endpoint-local and no UI-local fact store may exist to diverge from it | A spec must assert parity **in both directions** over one selection at one evaluation: every fact a surface renders is retrievable from the endpoint, and every fact the endpoint returns is renderable — a one-directional check would satisfy half the clause |
| RFC6-14 | OS | `spec/selection-api` | The vocabulary is RFC 0002's **verbatim** — endpoints may not relabel, coarsen, or invent states; `challenge-pending` (RFC2-13) is neither a tier nor an Unknown reason and travels *beside* the four values, never displacing one | A spec must assert that every entity, claim instance and aggregate in a machine answer carries label, RFC2-25 tier, RFC2-24 reason where applicable and RFC2-10 freshness, plus the three sibling surface states, and that an answer listing entities without labels — or a count folding Unknowns silently into a total — fails |
| RFC6-15 | OS | `spec/selection-api` | Query answering is inside the deterministic layer (VIS-7, RFC6-7); an answer that cannot name its evaluation is not an answer at all, not a degraded one | A spec must assert that every answer names the evaluation identity (source snapshot + as-of instant), that identical evaluation plus identical filters return an identical answer, and that a mixed-evaluation answer declares its skew per RFC6-3 |
| RFC6-16 | OS | `spec/selection-api` | The only VIS-1-permitted move is narrowing the **declared** scope, never faking coverage (RFC2-23's partial-snapshot rule applied to queries) | A spec must assert that the answer envelope names the filters applied, and that a filtered or partial result is never presented as full project scope |
| RFC6-17 | OS | `spec/selection-api` — scene and table aggregates consume it via `spec/map-scenes` and the surface specs | The aggregation obligation is exactly as wide as the RFC6-22 equivalence obligation over the same objects: labels may not be dropped at the moment elements merge | A spec must assert that every aggregate discloses membership count plus per-label, per-tier over **all six** RFC2-25 tiers, per-Unknown-reason (computed over primary reasons only, secondary annotations disclosed separately), per-freshness and sibling-surface-state composition — and, since the 2026-08-10 Wave A repair (RD-9 f5), per-value counts of chain state and normalized work state where carried plus the `challenge-pending` disclosure — and supports expansion to members; "Observed ×30" without the `reduced-fidelity` and stale counts fails the assertion |
| RFC6-18 | OS | `spec/selection-api` | Two surfaces showing different evidence for one selection at one evaluation is classified a **kernel defect, not a UI inconsistency** — a diagnosis-routing rule that survives whatever requirement is written, since it decides who owns the bug | A spec must assert that the full fact set for a (reference, evaluation, scenario) triple is reachable from every surface and from the endpoints, and that presentation differences — ordering, grouping, progressive disclosure, SDR-17 minimal-by-default — never change which facts, labels, or provenance exist |
| RFC6-19 | OS | `spec/selection-api` | The eight content classes are the **closed taxonomy** of the fact set, and challenge lifecycle state travels unflattened: `admitted` suspends the claim (Unknown, `challenge-suspended`, `suspended` tier) while `challenge-pending` suspends nothing; class 7's coverage boundary is the union of two defined constructs — executed mapping coverage records (RFC4-27, via RFC2-6) and declared captured scope (RFC2-23) — never a free-standing judgment | A spec must assert, per selection, that the fact set carries all eight classes with their named members — identity and succession edges; label+tier+reason+freshness with suspension basis visible; every evidence artifact as a resolvable link with source, capture time, scope and integrity identity; producing evaluation plus typed authority plus observer/adapter identities and versions; warrants with dismissal reason and expiry; every open challenge with its RFC2-13 state; exclusion counts, consent state and the coverage boundary; and, where work bears on the selection, the two-field work-and-reconciliation state — chain state (RFC2-18, read under RFC2-19's V0 staging) and normalized work state (RFC8-12, a staged forward reference, informative until RFC 0008 is accepted) |
| RFC6-20 | OS | `spec/selection-api` | Doctrine rules and accepted contracts are **not** V0-core graph entities (RFC1-6) and are cited by stable identifier; external URLs are classified external and may be unavailable without falsifying the internal graph | A spec must assert that every internal link in a fact set resolves to its identified target, that the kernel emits no reference it cannot resolve (RFC1-26), and that a `VIS-n` or RFC-clause citation, *if* rendered as a link, resolves to the identified artifact |
| RFC6-21 | OS | `spec/selection-api` | SDR-17's minimal default is a presentation depth, never a fourth epistemic state alongside Observed/Inferred/Unknown | A spec must assert that disclosing a minimally-rendered status yields the same fact set on every surface, and that endpoints serve the full set regardless of any display-depth parameter a client passes |
| RFC6-22 | OS | `spec/selection-api` — parity fixtures shared with `spec/map-surface` | Equivalence is over **semantics and query results, never pixels**; no requirement may satisfy it with a visual or screenshot comparison | A spec must assert the field-by-field parity tuple — same evaluation identity, same declared filters, same entities and edges, same label+tier+reason+freshness, same sibling surface states, same scenario context, and (since the 2026-08-10 Wave A repair) same `challenge-pending` disclosure plus same chain state and normalized work state where carried — holds between a 3D scene, a 2D view, a table and a machine answer for every presented element over one declared scope; "a facet outside this tuple is checked by nothing" is now the clause's own stated rationale |
| RFC6-23 | OS | `spec/selection-api` — parity fixtures shared with `spec/map-surface` | Finer detail in a non-3D rendering is permitted (SDR-27) **only** as a disclosed filter/aggregation difference; and any disagreement is release-blocking under the trust floor — a release-gate limb that craft/release policy must also carry (see Notes) | A spec must assert that no pair of equivalent renderings disagrees on an entity's existence, an edge, a label, a tier, a reason, a freshness state, a sibling surface state, a chain state, a normalized work state, a `challenge-pending` disclosure, a scenario context, or a count over the same declared scope, and that a finer-detail rendering discloses the difference as filter/aggregation per RFC6-16/17 rather than presenting it as a different graph |
| RFC6-24 | OS | `spec/selection-api` — historical *map* rendering lands in `spec/map-surface` under RFC9-41 | Exactly one context per selection with Base as the default; the three-value context set is closed; Base is distinct from RFC9-14's layout baseline; a Proposed context has **no status authority** — it never turns anything green, closes a gap, or anchors the map | A spec must assert the explicit non-default-revision marker on a Base context over a branch or PR-tree evaluation; the kernel's refusal of a context naming two proposals of one exclusivity group or of undeclared compatibility, returning `incompatible-scenario` and rendering *N candidate futures* selectable one at a time; proposed structure staying visually and queryably distinct in drawer, scene, table and endpoint alike; and Historical resolving against the immutable observation record with staleness visible on the primary surface |
| RFC6-25 | OS | `spec/selection-api` | A silent context swap is a violation **even when the fact sets overlap** — overlap is never a licence to substitute one context for another | A spec must assert that scenario context travels through cross-surface synchronization, URLs and query answers, and that a base-context selection never renders proposed structure, nor the reverse |
| RFC6-26 | OS | `spec/selection-api` | The state maps to RFC2-24 reason #6 `unconsented-source-or-provider`, and consent state is itself a drawer fact (RFC6-19 class 7) — a standing policy state, not an incident | A spec must assert that an unconsented source or provider renders Unknown with that reason and its resolution route (record consent) — never a failure, a broken link, or an empty region — while the consented remainder of the fact set renders normally |
| RFC6-27 | OS | `spec/selection-api` | Unclassifiable content fails closed (SEC-5); a secret in a query answer is identical in gravity to one in a tooltip, so no consumer class earns a weaker rule | A spec must assert that excluded content renders as *excluded* with a count rather than as absent, and that nothing derived from excluded content reaches any surface, drawer or endpoint — including the shape-leaking case of per-file match counts (§4 case 10) |
| RFC6-28 | CR | — (phase gate; the coverage-matrix deliverable's named candidate home is the specification-acceptance policy, CC-SPEC-8) | The whole clause stays normative: no implementation work for user-observable behavior under RFC6-1…RFC6-27 may be scheduled from this RFC alone; each observable consequence must map to an approved `openspec/**` requirement or carry a reviewed N/A judgment homed in `decisions/` (RFC3-15), honored only through an effective owner act under RFC3-16(a), in state (1) or state (2), with that state rendered; absent or invalid acts map nothing and leave the consequence unmapped and Unknown — the clause's own standardized sentence; the coverage matrix is review material, never authority | **Re-decided CR on 2026-08-10** — launch-gate pilot finding E4 required the six shape-parallel phase clauses to route identically, with the value a judgment this repair records. The 2026-08-07 N/A rested on one load-bearing premise: that neither craft-and-care nor any release policy owned specification-phase gating, so the CR route had no home. That premise is dissolved — the candidate specification-acceptance policy's **CC-SPEC-8** owns exactly this clause's deliverable, the clause-to-requirement coverage matrix produced with each spec. Like its five siblings, the clause is a review-and-process obligation on how work comes to be scheduled, invisible to any user of the running system, and a requirement written for it would be circular. The superseded N/A reasoning is preserved in note 3 below |

**Tally:** OS 27 · N/A 0 · CR 1 · IR 0 · total 28 (sums: yes — 27 + 0 + 1 + 0 = 28; RFC6-28 re-decided N/A → CR on 2026-08-10, note 3)

**Notes and doubts:**

*Three rows are genuinely arguable and are flagged as such. Two further
clauses were considered for N/A and settled; they are recorded so the
consideration is auditable rather than invisible.*

1. **RFC6-22 — flagged doubt (OS vs N/A).** This is the closest call in the
   contract. RFC6-22 defines a predicate ("two renderings are *equivalent*
   iff…"), and a defensible N/A reading exists: the obligation not to
   disagree is carried by RFC6-23, the disclosure obligation by RFC6-17, and
   the evaluation/filter limbs by RFC6-15/16 — so on that reading RFC6-22
   mints a shared vocabulary and nothing else. I routed it **OS** anyway,
   for two reasons. First, RFC6-23's prohibition is stated over *"equivalent
   renderings"* and is therefore circular without RFC6-22's field list; the
   assertion set of every parity scenario physically lives in RFC6-22.
   Second, two members of its tuple (evaluation identity, declared filters)
   are absent from RFC6-23's disagreement enumeration, so an N/A here would
   leave those two fields with no parity assertion at all. If the owner
   prefers the N/A reading, the safe form is "N/A, provided `spec/…`
   requirements for RFC6-23 and RFC6-17 are written against RFC6-22's tuple
   verbatim" — but that is a conditional N/A, which the four-way scheme does
   not currently express.

2. **RFC6-23 — flagged doubt (single category forced).** This is the only
   clause in RFC-0006 with two limbs in two different categories: the
   disagreement prohibition is **OS**, and "release-blocking under the trust
   floor" is **CR**. The one-row-one-category rule forced a choice; I chose
   OS because the dominant normative content is a behavioral parity
   assertion, and because classing it CR would let disagreement behavior be
   implemented with no requirement testing it. **The CR limb is therefore
   unhomed by this matrix.** That matters more than usual because RC-5 F6
   found that *no release-policy artifact exists* — `governance/policies/`
   contains only `craft-and-care/` — so every CR row in the corpus already
   routes to a named-but-absent home. Recommend the owner-facing note record
   RFC6-23's release-gate limb explicitly rather than letting the OS row
   absorb it silently.

3. **RFC6-28 — re-decided N/A → CR, 2026-08-10.** The original routing was
   N/A, on the reading that the clause constrains *scheduling*, not the
   product, and that the CR category — defined as belonging to
   *craft-and-care or release policy* — had no home for a governance-phase
   gate over the specification plane, which craft-and-care did not own.
   (RC-5 independently reached the same N/A; concurrence was noted as not
   confirmation, since both passes applied the same four-way scheme.) The
   launch-gate pilot's finding E4 then observed the six shape-parallel
   phase clauses split N/A (this one) vs CR (the other five), and the
   disposition register ordered them routed identically, the value being a
   judgment the repair records. The value chosen is **CR**, because the
   original N/A's load-bearing premise no longer holds: the candidate
   specification-acceptance policy (CC-SPEC-8,
   `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md`,
   approved by no act) now owns exactly the coverage-matrix deliverable
   this clause demands. Had the six been forced to N/A instead, five
   contracts' matrix deliverables would have lost their only named home.
   The recursion noted in the original judgment stands: this file is a
   first pass at the artifact the six clauses demand.

4. **RFC6-1 — considered for N/A, settled OS.** Its first limb ("the kernel
   mints nothing new for selection"; entity kinds and identities are exactly
   RFC 0001's) is textbook N/A — an identity-space closure with no distinct
   user-visible outcome. But the clause's second limb is a hard prohibition
   with a directly testable boundary ("every handle must resolve to a
   selection reference before it crosses a surface boundary, a URL, or an
   endpoint"), and §4 case 1 is already written as a test. Routed OS with
   the minting limb recorded as the retained invariant, per the rule that a
   retained invariant never exempts an observable limb.

5. **RFC6-6 — considered for N/A, settled OS.** It reads like type hygiene
   ("outcomes are not Unknown reasons"), but the clause's operative verb is
   *counted*: an aggregate of Unknowns must not absorb navigation outcomes.
   That is an arithmetic assertion a scenario can make and fail, so it is
   not N/A.

6. **One CR and zero IR, checked deliberately.** RFC-0006 carries no
   review-cadence, walkthrough, or release-gate clause of its own — unlike
   RFC-0007 (RFC7-25/30/31/32) and RFC-0009 (RFC9-45/47/49). Its single CR
   row is RFC6-28, the phase gate (re-decided 2026-08-10; note 3); the only
   other craft-adjacent text is RFC6-23's release-blocking limb (item 2). IR is zero because every numbered clause
   in this contract is normative; the informative material — §0 reader map,
   §2 motivation, §5 integration, §6 alternatives, §7 deferrals, §8 open
   questions, and the bracketed `[Inferred]` passages — carries no clause
   number and so produces no row under a clause-keyed matrix. If the parent
   matrix wants informative sections routed, that needs a different row key
   than a clause ID.

7. **No new spec domain is needed.** Every one of the 27 OS rows takes
   `spec/selection-api` as its primary domain, which is consistent with
   `09-OPEN-SPEC-READINESS-REPORT.md` sequencing it as changeset #1 on the
   grounds that every surface and machine client consumes it. Four rows
   (RFC6-17, RFC6-22, RFC6-23, RFC6-24) carry a secondary annotation naming
   where the *consuming* requirements land (`spec/map-scenes`,
   `spec/map-surface`); those annotations are informative routing aid — the
   owning domain in each case is still `spec/selection-api`, and no clause
   is double-counted in the tally.

8. **Two known leak passages are now routed.** RC-5's leak inventory named
   L2 (RFC6-5's nine-outcome obligation table) and L3 (RFC6-19's seven
   drawer content classes) as among the most directly implementable prose in
   the corpus, both previously carrying no routing row. Both are now OS with
   named assertion sets. Their closed-vocabulary character is preserved in
   the retained-invariant column rather than being removed from the RFC — per
   RFC 0008's argument that deleting a closed vocabulary from a contract
   causes worse divergence than leaving it there.

9. **Scope of this file.** It is a routing input, not authority, and creates
   no OpenSpec content — RFC6-28 forbids that during bootstrap and it is not
   attempted here. Where this file and an RFC-0006 clause disagree, the
   clause wins.

---

## RFC-0007 — Polaris (Intent Surface)


**Enumeration method:** run from the package's `rfcs/` over
`RFC-0007/README.md`, `RFC-0007/narrative-contract.md`,
`RFC-0007/rendering-and-surface.md` with Python `re` (not shell grep — grep on
this machine is ugrep):

```python
import re
pat = re.compile(r'RFC7-\d+(?:\([a-z]\))?(?![\w(])')
ids = set(pat.findall(open(f).read()))
```

The negative lookahead `(?![\w(])` is load-bearing: the more obvious
`\b`-terminated form silently loses every lettered sub-clause, because after a
literal `)` followed by a space there is no word boundary, so the regex
backtracks and reports `RFC7-11` where the text says `RFC7-11(a)`. That
failure was observed and corrected in this session.

**Enumeration caveat, verified two ways.** The sweep returns 41 distinct
strings. The three modules' front matter declares 45 clause identities
(`RFC7-1..RFC7-38` plus sub-clauses `RFC7-2(a)-(c)`, `RFC7-9(a)-(c)`,
`RFC7-11(a)`). The four not returned — `RFC7-2(b)`, `RFC7-2(c)`, `RFC7-9(b)`,
`RFC7-9(c)` — are **not missing**: they are written inline inside their parent
clause as `**(b) …` / `**(c) …` markers rather than as fully-qualified strings.
Confirmed by a second method: a literal-count sweep returns 0 occurrences of
each of those four strings across all three files, and a scan for
`\*\*\(([a-c])\)` in `narrative-contract.md` returns exactly six markers —
`(a) anchored`, `(b) explicitly non-normative`, `(c) epistemically labeled`
(RFC7-2) and `(a) Covers`, `(b) Minimality`, `(c) Bounding` (RFC7-9). All 45
declared identities are therefore present in the text and each gets a row.
(Rev10 enumerated only 39 rows for this package — it omitted the six
`RFC7-2`/`RFC7-9` sub-clauses entirely.)

**Clauses found:** 45 — RFC7-1, RFC7-2, RFC7-2(a), RFC7-2(b), RFC7-2(c),
RFC7-3, RFC7-4, RFC7-5, RFC7-6, RFC7-7, RFC7-8, RFC7-9, RFC7-9(a), RFC7-9(b),
RFC7-9(c), RFC7-10, RFC7-11, RFC7-11(a), RFC7-12, RFC7-13, RFC7-14, RFC7-15,
RFC7-16, RFC7-17, RFC7-18, RFC7-19, RFC7-20, RFC7-21, RFC7-22, RFC7-23,
RFC7-24, RFC7-25, RFC7-26, RFC7-27, RFC7-28, RFC7-29, RFC7-30, RFC7-31,
RFC7-32, RFC7-33, RFC7-34, RFC7-35, RFC7-36, RFC7-37, RFC7-38

| Clause | Route | Future spec domain | Retained invariant in the RFC | Justification |
|---|---|---|---|---|
| RFC7-1 | N/A | — | Polaris is a projection surface over the one shared kernel, never independently authoritative, never satisfied by the SDR §2 anti-thesis forms | Every limb of this charter is discharged by a clause already routed OS — non-authority by RFC7-3/4, "no second copy" by RFC7-18, the thesis→leaf product by RFC7-13/14 — so a scenario naming RFC7-1 could only restate one of those; "never satisfied by the anti-thesis forms" is judged by the RFC7-30 walkthrough, not asserted by any renderable outcome. |
| RFC7-2 | OS | `spec/intent-surface` | The three-way exhaustive typology (no fourth kind); granularity is the claim block; the check binds *any* act producing curated narrative, not one path | A spec must pin that an act producing curated narrative is assessed per claim and refuses a load-bearing project-fact claim that is neither anchored, non-normatively marked, nor epistemically labeled — and that the refusal fires on every authoring path (human edit, agent repair, draft adoption), not only at RFC7-21. |
| RFC7-2(a) | OS | `spec/intent-surface` | "Anchored" means resolvable through the block's own anchor set to the **one artifact that owns the fact** | A scenario must assert that a block declared `anchored` exposes a traversable path to the owning artifact, and that a claim anchored only to an artifact which does not own the asserted fact (a decision cited for requirement text) fails the RFC7-2 check rather than passing as anchored. |
| RFC7-2(b) | N/A | — | Framing, motivation, analogy, transition and reader guidance are a lawful kind, machine-marked as carrying no normative force | Alone among the three kinds it imposes no resolution or provenance obligation of its own: the marking's presence, its parity across endpoint and plain-text renderings, and its non-visual recoverability are enumerated obligations of RFC7-33/34, and its role in the exhaustive check is RFC7-2's — so any scenario written for (b) would be a verbatim restatement of the RFC7-33 claim-block-kind assertion. |
| RFC7-2(c) | OS | `spec/intent-surface` | Observed carries its evidence link, Inferred its inference provenance, Unknown stands as Unknown | A scenario must assert the label-specific companion obligation: an `[Observed]` narrative claim rendered without a resolvable evidence link, or an `[Inferred]` one without inference provenance, is non-conformant — an assertion about accompanying data that no RFC7-33 attribute scenario makes. |
| RFC7-3 | OS | `spec/intent-surface` | Non-citability of every Polaris artifact; the deletion invariant | A spec must pin refusal: any attempt to make a narrative, section, claim block, rendering, or editorial draft the target of a claim, gap, mapping, evidence link, work warrant, or anchor is rejected — plus the end-to-end scenario that deleting `.syzygy/intent/**` leaves every truth, status, work item, consent and normative fact unchanged. |
| RFC7-4 | OS | `spec/intent-surface` | Non-authority is invariant across narrative state; presentation review or adoption confers no normative force | The distinct, separately-failable scenario is the post-adoption one: after a narrative passes fresh-reader review and is adopted, it still carries `non-citable` and is still refused as an anchor target — an implementation can plausibly special-case "adopted" as promoted, which RFC7-3's scenarios over draft/curated states would not catch. |
| RFC7-5 | OS | `spec/intent-surface` | The seven-entity model and its `.syzygy/intent/**` residence; opaque label-independent identifiers; personal view state excluded from the model | A spec must pin the presentation-profile bootstrap behavior: on first render of a project with no loaded profile, Polaris drafts a default and renders it `unadopted-draft` under RFC2-24 reason #1, every narrative element above the unsigned profile renders unadopted with it, a permanent decline renders the reduced form and says so, and the third path (rendering *as if* a profile were present) never occurs. |
| RFC7-6 | OS | `spec/intent-surface` | At most one primary narrative; additional named narratives outrank nothing | Two assertions: a second primary narrative is refused, and on a thin or undeclared project the primary narrative is thin or Syzygy-drafted-unadopted but **present** — absence is a missing front door that fails the RFC7-30 entry, not a trivially passing empty state. |
| RFC7-7 | OS | `spec/intent-surface` | The governed-presentation-artifact class: versioned, attributed, revertible, human-readable; "governed" names the change discipline, not the content's standing | A spec must pin that a single narrative change — prose edit exactly as structure edit — is atomic, Syzygy-attributed and individually revertible, that authorship and review state are machine-readable, and that a write over narrative Syzygy did not author surfaces a conflict instead of silently overwriting (SEC-4). |
| RFC7-8 | OS | `spec/intent-surface` | The narrative is authored governed-plane content: not rebuildable, not cache, not a `governance/` artifact | Two testable survival behaviors nothing else asserts: a cache purge or rebuild leaves narrative content intact (it is not derivable and must not live in `.syzygy/cache/`), and offboarding carries `.syzygy/intent/**` with the repository. The "binds nothing" limb is RFC7-3's; the survival limbs are this clause's. |
| RFC7-9 | OS | `spec/intent-surface` | The citation unit is the claim block or section source anchor, never a per-sentence badge; an anchor targets exactly one owned artifact; the three properties bind and are not stylistic | A spec must pin that the surface renders citation at block granularity (a per-sentence badge rendering is a violation, not a density choice) and that an anchor naming more than one target artifact is rejected at authoring. |
| RFC7-9(a) | OS | `spec/intent-surface` | Covering = derivable **and** the supporting anchor identifiable; derivability alone is not covering | A scenario must assert per-claim attribution is recoverable by a reader — selecting a load-bearing claim identifies which anchor or anchors support it — because the admissibility floor (one claim, one falsifiable concern) is unusable without it. |
| RFC7-9(b) | OS | `spec/intent-surface` | A surplus anchor is a defect, not a courtesy | Given (a)'s attribution data, an anchor on which no claim in the block relies is detectable, and a scenario must assert the authoring/validation path reports such a block as non-conformant rather than accepting the extra anchor as harmless. |
| RFC7-9(c) | OS | `spec/intent-surface` | An unattributable block is non-conformant, not merely large; splitting is an obligation | Violation case 14 is written as a fixture: a twenty-anchor section-granularity block where every anchor resolves and every machine attribute is present must still be reported non-conformant — a scenario that fails precisely when an implementation checks resolvability instead of attributability. |
| RFC7-10 | OS | `spec/intent-surface` | The typed anchor tuple and its closed target-class list; no target class for narrative content; durable identifiers, never labels/paths/coordinates; the target-state component imitates and never extends RFC2-11/18 | A spec must pin that an anchor whose target class is narrative content is refused, that anchors carry durable identifiers rather than labels or paths, and that the recorded target state (revision, or evaluation identity plus label+tier+reason verbatim) is written at the authoring act and **never rewritten by a later read**. |
| RFC7-11 | OS | `spec/intent-surface` | Broken anchors degrade the claim to Unknown and name the break; never silently dropped, re-guessed, or auto-redirected | A scenario must assert that on `unresolvable`/`retired` the primary surface names which anchor and which target, the claim renders Unknown, and the identical state is served to machine consumers — with the negative assertions (no nearest-title re-anchor, no successor redirect, no continued live-citation rendering) tested explicitly. |
| RFC7-11(a) | OS | `spec/intent-surface` | Drift is a Polaris-local rendering obligation over a *resolving* anchor and mints no RFC2-24 Unknown reason; a new evaluation identity alone is not drift | A spec must pin the `anchored — target changed since authorship` state: what moved (recorded vs current) is named, the same state reaches machine consumers, the block is marked for RFC7-25 review, the marker clears only on an authoring act that re-reads the target, and an evaluation change with unchanged label/tier/reason does **not** trigger it. |
| RFC7-12 | OS | `spec/intent-surface` | An anchored block renders *about* its target; for adjudicative material the operative text is the owned artifact's verbatim text, never a paraphrase in normative position | RFC7-2 cannot catch this — a paraphrase of a doctrine rule is properly anchored and passes (a) — so a scenario must assert that a block paraphrasing adjudicative material presents the target's verbatim text as the operative text, and never lets the paraphrase alone occupy that position. |
| RFC7-13 | OS | `spec/intent-surface` | The per-altitude obligation: each altitude is a self-sufficient, honest, coarser read; every narrative descends to a verbatim leaf; an anchor is always one step from its owned artifact. Ordering and altitude count are a **V0 default** (owner decision B7), not frozen | A spec must pin the V0 default path (thesis → architecture → catalog → deep dive → verbatim leaf) and, per altitude, that a reader stopping there holds a true coarser model — with the one-step anchor reachability asserted independently of the browsing path. |
| RFC7-14 | OS | `spec/intent-surface` | Requirement, scenario and doctrine text render verbatim under the owning contract's identity scheme; Polaris stores no reorganized copy | A scenario must assert that under a proposed-scenario reading the leaf renders the **adopted** text as operative with the proposal's delta adjacent — visually and queryably distinct, never substituted, never interleaved past a reader's ability to tell which is which, and never anchorable. |
| RFC7-15 | OS | `spec/intent-surface` | The catalog is a projection of declared capability identities; no silent inference into a capability | Three scenarios: nothing appears that no declared artifact asserts; drafted capabilities render unadopted and unmapped code renders Unknown; a predominantly-Unknown catalog on an undeclared project renders as normal output with RFC2-24 reasons and resolution routes, not as an error state. |
| RFC7-16 | OS | `spec/intent-surface` | Status is kernel-computed at an identified evaluation, the label+tier+reason+freshness vocabulary carried verbatim, **tier in the at-rest set** (fixed here, nowhere upstream), and no composite maturity number until RFC 0002's deferral is discharged | A spec must pin the SDR-17 minimal default: one epistemic state per capability or major claim — label with its RFC2-25 tier plus freshness — with evaluation identity and drawer handoff present, staleness visible on the narrative page itself, and no metric wall, trend, count or composite number rendered. |
| RFC7-17 | OS | `spec/intent-surface` | The **three authority classes** are foundational and non-negotiable at any V; no block straddles two; no fourth class. Band count and ordering are a V0 default (B7) | A spec must pin that every band declares its class machine-readably, that the V0 argument/contract/reality composition renders in that order, and that a reality-band block never carries authored non-normative prose (or vice versa) — the straddle is the failure the class partition exists to prevent. |
| RFC7-18 | OS | `spec/intent-surface` (drawer leg: `spec/selection-api`) | Polaris chooses altitude, ordering and deferral — never contents; it holds no copy of work state; evidence summaries introduce no fact the drawer lacks | Violation case 5 is the scenario: a Polaris-side rollup that disagrees with the single evidence drawer for the same selection is a failure, and work state is reachable only through the drawer and the scheduler's typed adapter, never from a Polaris-local store. |
| RFC7-19 | OS | `spec/intent-surface` | Empty renders honest: one line naming what is absent, with its Unknown reason where a claim is implicated | Directly testable rendering: a contentless block collapses to the honest line and never to an empty heading, a hidden section, or scaffold headings — the last being the document-browser failure manufactured over an undeclared capability. |
| RFC7-20 | OS | `spec/intent-surface` | `editorial-draft` is a named RFC2-25 **sibling surface state** (B10), non-citable by construction and non-citable even after adoption | A spec must pin that generated prose appears only in that state, machine-marked with model/version/inputs, visually distinct and non-visually recoverable, never an anchor target or citation-graph member, never green — and that absent SEC-2 named-provider consent the draft is **not computed**, the layer renders `unconsented-source-or-provider`, and the rest of the surface stays fully readable. |
| RFC7-21 | OS | `spec/intent-surface` | Adoption is an attributed human act with a **per-claim-block attestation**; no conformance ritual requires a non-empty diff; adoption confers curated status, never authority | A valid state-(1) or state-(2) owner act under RFC3-16(a) binds the adoption with its exact state rendered; state (1) remains visibly uncorrelated. The fail-closed scenario is an absent or invalid act: it **does not bind**, so the draft stays a draft and renders unadopted. A draft sentence carrying an unanchorable, unlabelable project-fact claim cannot be adopted as written even under a signature over the whole. |
| RFC7-22 | OS | `spec/intent-surface` (queue leg: `spec/work-surface`) | The pending-draft queue is Trajectory's (SDR-18); Polaris renders it read-only in context; an expired draft is a discarded projection, never a lost truth | A scenario must assert that on rejection the draft leaves the intent surface entirely — no half-adopted ambient prose remains — and the rejection is recorded on the queue's work item, not in the narrative. (Open question q4 may change the retention default; the leave-the-surface obligation does not depend on it.) |
| RFC7-23 | OS | `spec/intent-surface` | The four acts and their gates; the structure-edit row is presumptively material; SDR-13's refusal of a separate governance tier for structure | Violation case 7 is the scenario: an "adopt" affordance offered in reading context must run the *target artifact's own* gate unchanged — adopting a doctrine draft without the owner's VIS-4 act is refused — and the prose-edit row is not an exemption from RFC7-2's per-claim check. |
| RFC7-24 | OS | `spec/intent-surface` (queue leg: `spec/work-surface`) | The SDR-18 seam: Trajectory owns the drafting queue and work lifecycle, Polaris the contextual authoring/adoption experience | Three testable assertions: queue state renders in Polaris read-only; no queue store exists under `.syzygy/intent/**` and no narrative store under `.syzygy/work/**`; each act is recorded exactly once, in the artifact's own governing location. |
| RFC7-25 | OS | `spec/intent-surface` | The **computable materiality floor** (reading order, section set, a block's anchor targets, manifesto/thesis are always material); B6's asymmetric declaration; the failed-review record lives in `decisions/`, and "on the narrative's surface" is a rendering duty, never a storage location | A spec must pin three behaviors: the floor classifies automatically; an authoring party's declaration of **immaterial** is refused while **material** is accepted, and an undeclared wording edit stays open and contestable rather than being recorded immaterial by silence; a failed review renders machine-readably on the narrative surface until a later pass clears it, and a valid state-(1) or state-(2) verdict may clear or hold the freeze with its exact state rendered, while an absent or invalid act does not clear it. The verdict is a warrant governing review, never project evidence. *(The conduct and cadence of the review itself is craft/review-policy material — see RFC7-32; the load-bearing part of this clause, by its own words, is the computable floor.)* |
| RFC7-26 | OS | `spec/intent-surface` (context travel: `spec/selection-api`) | The default mode **is** RFC6-24's `Base` context and is named that; Polaris coins no surface-local synonym for a kernel concept; proposed material has no status authority and anchors nothing | The discriminating scenario is stated in the clause itself: default reading includes the **observed** plane in full, so an implementation that builds the default as a filter over adopted desired state fails — plus proposed-scenario context travelling with every selection, URL and query, and proposed material rendering unmistakably distinct visually and machine-readably. |
| RFC7-27 | OS | `spec/intent-surface` | Competing futures never collapse into one merged future; prose describing a proposal in the register of adopted intent is an RFC7-2 violation regardless of visual marking | A scenario must assert the honest render of *N* candidate futures selectable one at a time, with a union across an exclusivity group or across proposals of undeclared compatibility refused as `incompatible-scenario` rather than merged. |
| RFC7-28 | OS | `spec/intent-surface` | A curated diagram is narrative content under every rule in the package; it claims no reproducibility-from-snapshot and must not imitate the computed map | A spec must pin per-element behavior: every named element carries an anchor or a non-normative/proposed marking, speculated structure never renders like existing structure, every encoding means what its legend says, a text equivalent exists, and curated-versus-computed provenance is a machine-readable attribute on every visual. |
| RFC7-29 | OS | `spec/intent-surface` | The ownership map itself: what Polaris owns (narrative model artifacts) versus composes, and the authority home of every other row | Most rows restate a behavior routed elsewhere, but two do not and must be specified: rendered decisions, dismissals and consents show their **reason and expiry**, and work items render as links plus read-only state — with the map's own consequence, that no Polaris-side path amends a non-owned row's authority except through RFC7-23's gates, asserted as a refusal. |
| RFC7-30 | CR | — (release policy; craft-and-care review bar) | The cold-open walkthrough is this surface's acceptance criterion, and the last prompt — one thing the project does not know about itself — is load-bearing: a surface passable only by a uniformly confident read has rendered comprehensible fiction | The clause specifies a **test procedure** (six enumerated prompts, an independent fresh reader, a second answer-checking phase, findings recorded), not a behavior of the product; the behavior it exercises — keyboard/non-visual operability of the paths between units — is RFC7-34's routed limb, and the non-visual run is that limb's evidence obligation, which is why the run's cadence belongs to release policy rather than to a requirement. |
| RFC7-31 | CR | — (release policy; shared leg stated at RFC9-45) | The two non-judgment floors (a dangling internal link on the walkthrough path fails, release-blocking; a confident wrong answer attributable to what the surface rendered fails); honest thinness on an undeclared project is never a failure; the two artifacts and their two homes; a verdict requires an effective owner act under RFC3-16(a), in state (1) or state (2), with that state rendered; the judgment is a warrant, never project evidence | Verdict lawfulness, the judging party, the record/judgment split across `records/` and `decisions/`, and `verdict-unlawful` are release-gate machinery evaluated by a human adjudication process, not consequences a user-facing scenario can exercise. *(Its one surface-shaped limb — an absent or invalid verdict leaves the test rendering **Unknown, never met** — is a status-rendering consequence that follows the release record wherever it renders; it is flagged in the doubts below rather than silently absorbed.)* |
| RFC7-32 | CR | — (release policy) | The trigger set: material narrative changes and release milestones, with at least one non-visual/keyboard-only run per release milestone; it is the sibling of v1.md's spatial comprehension test and is never collapsed into it | Pure cadence — *when* a review-and-walkthrough process runs, recorded in the homes RFC7-25 and RFC7-31 name. Nothing here is a rendered outcome; the materiality classification that feeds the trigger is RFC7-25's routed limb. |
| RFC7-33 | OS | `spec/intent-surface` (parity leg: `spec/selection-api`) | Every distinction the package draws is a machine-readable attribute on the rendered unit; the narrative claim-block **type name** stays distinct from the kernel Claim entity | A spec must pin the enumerated attribute set (claim-block kind, band and authority class, curated-vs-computed provenance, adopted/unadopted, editorial-draft, proposal-context membership, review state, RFC7-11(a) target-changed, label+tier+reason+freshness) served identically through the machine endpoints and preserved in plain-text and exported renderings — with `non-citable`/`presentation-artifact` named as a required field on **every** export, since its omission is unrecoverable at an unbound external consumer (violation case 13). |
| RFC7-34 | OS | `spec/intent-surface` | Two limbs both bind: recoverability governs encoding, operability governs the paths; every curated diagram has a text equivalent carrying the same anchored elements and markings | A spec must assert both limbs separately, because satisfying one alone is the stated failure: every distinction recoverable without colour, position or layout, **and** every traversal of the disclosure path — RFC7-13's altitudes, anchor expansion including the RFC7-11 and RFC7-11(a) states, and the RFC6-18 drawer handoff — operable without a pointing device. |
| RFC7-35 | OS | `spec/intent-surface` | The multi-project entry arranges from the workspace manifest while every project-internal fact derives from that project's own plane; deleting the manifest changes what is arranged, never what is true | A one-line scenario the clause states outright: an unresolvable workspace entry renders Unknown **with its reason** and is never silently dropped from the entry list. |
| RFC7-36 | OS | `spec/intent-surface` | The portfolio narrative is owner-workspace content, never project truth; there is no portfolio governance root; the enumerated carry-over of RFC7-2/7/11/11(a)/33/34 out of `.syzygy/intent/**` | Two distinct assertions: the portfolio narrative renders visibly as owner-workspace content and holds no claim block over any project's facts; and — not implied by visible marking — it may not assert that any governed project is converged, aligned, verified or healthy even when perfectly marked, because a sentence doing a badge's work is judged as a badge. Cross-project status renders only as each project's own kernel-computed state. |
| RFC7-37 | OS | `spec/intent-surface` (aggregation leg: `spec/selection-api`) | RFC3-14's asymmetric relation semantics; child epistemic labels pass through unchanged (RFC3-32); the narrow reading alone is insufficient | A scenario must assert that a one-sided declaration renders **unconfirmed** and the narrative never draws a confirmed edge the declarations do not support, that no child Unknown aggregates into anything green, and that any roll-up over a child's facts discloses RFC6-17's full composition — the equivalence tuple with per-label, per-tier, per-Unknown-reason and per-freshness counts, expandable to members. |
| RFC7-38 | CR | — (phase gate; feeds the coverage matrix this file serves) | The phase boundary: this contract fixes semantics and is not a specification of record; the coverage matrix is review material, never authority, and must span every clause of this contract other than this one, across all of the package's modules | A process obligation on how implementation work may be scheduled and on a deliverable the surface-specification phase must produce — it constrains the governance process, not any rendered outcome, so it can carry no requirement of its own without circularity. |

**Tally:** OS 39 · N/A 2 · CR 4 · IR 0 · total 45 (39 + 2 + 4 + 0 = 45 — sums: **yes**)

**Notes and doubts (RFC-0007):**

1. **RFC7-2(b) — the one N/A I would most expect to be contested.** Routing
   (a) and (c) OS while (b) is N/A is not arbitrary: (a) carries a resolution
   and ownership obligation, (c) carries per-label provenance obligations, and
   (b) carries only "machine-marked as carrying no normative force", which
   RFC7-33 enumerates as one of its attributes. If a reviewer holds that a
   closed vocabulary's members each deserve a value-level scenario, (b) becomes
   OS and the tally moves to OS 40 / N/A 1.
2. **RFC7-12 — reconsidered mid-analysis, from N/A to OS.** My first read
   routed it N/A on the grounds that its mechanizable limbs are RFC7-13's
   one-step rule and RFC7-14's verbatim leaf. That was wrong: a paraphrase of a
   doctrine rule is *properly anchored* and therefore passes RFC7-2(a), so
   nothing else in the package catches a faithful paraphrase sitting in
   normative position outside the leaf — which is the package's own named
   dangerous artifact.
3. **RFC7-25 is a genuine two-limb clause and the rubric allows one route.** I
   routed OS because the clause itself says the computable floor "is this
   clause's load-bearing part". The review-conduct limb is real CR content and
   is not discarded — it is carried by RFC7-32 (cadence) and RFC7-31 (verdict
   lawfulness), both routed CR. A reviewer preferring CR here should move the
   floor, the immaterial-declaration refusal, and the failed-review rendering
   into RFC7-32's or RFC7-33's OS scope rather than lose them.
4. **RFC7-31's Unknown-never-met rendering.** The clause's fail-closed
   outcome — absent or invalid verdict ⇒ the test renders Unknown, never
   met — is shaped like an OS obligation, but what renders is a release-record
   status, not an intent-surface unit, and RFC9-45 states the same protocol.
   Routed CR so one protocol is not specified twice in two domains; if the
   RFC9-45 side is routed OS at map specification, this row should follow it.
5. **RFC7-29 (boundary table) was the strongest N/A candidate after RFC7-1**
   and I moved it to OS on one row only: "Decisions, dismissals, consents —
   renders, reason/expiry visible" is a rendering obligation stated nowhere
   else in RFC-0007. If a reviewer finds that obligation discharged by RFC6-19's
   drawer content class 5 (warrants with reason and expiry), RFC7-29 becomes a
   clean N/A.
6. **RFC7-8** turns on whether "must not live in `.syzygy/cache/`" and "stays
   with the repository at offboarding" count as behavior. I routed OS because
   a cache purge that destroys authored narrative is a user-visible failure a
   scenario can catch; RC-5 called the same clause "borderline (b)".
7. **RFC7-9(b) (minimality)** is routed OS with an undecided detection
   mechanism: the clause makes a surplus anchor a defect, but detection depends
   on (a)'s attribution data being explicit rather than inferred. If the spec
   phase decides attribution is author-asserted rather than machine-derivable,
   (b) becomes an authoring-attestation obligation closer to CR.
8. **RFC7-4** is a quantifier over narrative states rather than a new
   obligation; I routed OS because the post-adoption case is separately
   failable and is exactly the kind of state special-casing an implementation
   invents.
9. **RFC7-30 vs RFC7-34.** I want the split recorded explicitly so it is not
   re-litigated: the *behavior* (keyboard operability of paths between units)
   is RFC7-34-OS; the *walkthrough that proves it* is RFC7-30-CR. Routing
   RFC7-30 CR does not exempt the behavior from OpenSpec coverage — RFC7-34
   carries it.
10. **No new spec domain is needed for RFC-0007.** Everything lands in
    `spec/intent-surface`, with four clauses carrying a named secondary leg
    into `spec/work-surface` (RFC7-22, RFC7-24) or `spec/selection-api`
    (RFC7-18, RFC7-26, RFC7-33, RFC7-37). The portfolio and multi-project
    clauses (RFC7-35/36/37) are Polaris renderings of workspace-manifest
    content and need no workspace domain of their own.
11. **Deltas against rev10, recorded so the change is auditable:** rev10
    enumerated 39 rows and classed 28 DI, 6 DI+OS, 1 OS, 4 CR. Here, 45 rows;
    every DI and DI+OS row is re-decided; 37 clauses that rev10 left with no
    named future artifact now carry one; the 4 CR rows (RFC7-25, 30, 31, 32) are
    re-decided as OS, CR, CR, CR — i.e. only RFC7-25 moves — and RFC7-38 moves
    from DI to CR.

---

---

## RFC-0008 — Trajectory (Work Surface)


**Enumeration method:** run from the package's `rfcs/` with
`python3` (no shell `grep`; `grep` on this machine is ugrep and mismatches
bracket classes). Definition-site regex, applied with `re.M` over each of the
four package files (`RFC-0008/README.md`,
`RFC-0008/identity-authority-materialization.md`,
`RFC-0008/state-vocabulary-and-cost.md`,
`RFC-0008/accounting-reconciliation-and-release.md`):

```python
defre = re.compile(r'^\*\*(RFC(?:8|10)-\d+)(\([a-z]\))?(?=[\s.—*])', re.M)
```

The lookahead `(?=[\s.—*])` is required: RFC8-32's heading is
`**RFC8-32 — This contract schedules nothing.**`, so a regex anchored on
`**RFC8-n.**` alone silently drops it (it did, on the first pass). Contiguity
was checked by integer set-difference against 1..32: **no gaps, no extras**.

A second sweep with `re.compile(r'RFC(?:8|10)-\d+(?:\([a-z0-9]\))?')` found
lettered mentions **RFC8-2(a)** and **RFC8-8(a)** only, both inside prose.
Per the package README lookup rule these are *list items within one clause
body*, not sub-clauses with their own identity, so they are **not** separate
rows; their routing is stated inside the parent row. `README.md` defines no
clause (0 definition sites) — it is index and non-normative reader map.

**Clauses found:** 32 — RFC8-1, RFC8-2, RFC8-3, RFC8-4, RFC8-5, RFC8-6,
RFC8-7, RFC8-8, RFC8-9, RFC8-10, RFC8-11, RFC8-12, RFC8-13, RFC8-14, RFC8-15,
RFC8-16, RFC8-17, RFC8-18, RFC8-19, RFC8-20, RFC8-21, RFC8-22, RFC8-23,
RFC8-24, RFC8-25, RFC8-26, RFC8-27, RFC8-28, RFC8-29, RFC8-30, RFC8-31,
RFC8-32

| Clause | Route | Future spec domain | Retained invariant in the RFC | Justification |
|---|---|---|---|---|
| RFC8-1 | OS | `spec/work-surface` | No plane may impersonate another (RFC1-22/23); the three-plane rendering duty | A scenario must assert that every rendered work element carries a plane label (desired / execution / observed), and that an element whose plane cannot be determined appears in the result set with plane Unknown and is **counted**, not omitted — the omission case is the testable failure. |
| RFC8-2 | OS | `spec/work-surface` | The anti-thesis itself, all three limbs, as a standing prohibition on any conforming design | Limb (c) needs its own scenario no other clause carries: a **past-window** account query must answer "what changed, at what cost, under whose authority" at the fidelity preserved records support, so a spec must pin the windowed retrospective query and its degradation. Limbs (a) and (b) are enforced observably through RFC8-3/8-7 (no local writes) and RFC8-15/8-30 (closure never renders done) — they route with those clauses, and the prohibition stays normative here. |
| RFC8-3 | OS | `spec/work-surface` | Trajectory is never independently authoritative (VIS-6); no write-locally-and-sync-later | A scenario must assert that every offered mutation performs a synchronous attributed adapter or governance-plane act **and a re-read before the new value renders**, and that an adapter failure surfaces as a failed act rather than a locally-held optimistic value; plus that discarding the projection and rebuilding it from kernel + `.syzygy/work/**` + adapters yields the same answers. |
| RFC8-4 | OS | `spec/work-surface` | No new kernel entity; the surface-concept→kernel-identity binding table is the projection's fixed shape | The binding table determines **what identity type an answer returns for each surface concept**, which a spec must pin before any scenario can be written: a rendered "review" resolves to a work item plus PR evidence identities, an "execution run" to a run plus its Execution Record, and a "warrant" is not selectable as an entity at all (the `motivates` edge is deliberately unreified). That is distinct from RFC8-31's rule that selection *uses* kernel identity; here it is *which* identity. Work items are mirrored, never minted — the surface must never issue a work-item id. |
| RFC8-5 | OS | `spec/work-surface` | The four recorded non-reifications (idea, milestone, no-Feature, contradiction/dismissal) | Directly assertable exclusions: an idea never appears in any work enumeration until promoted to a Proposal; a milestone aggregates but never appears as work or as a warrant; an intake "feature request" carries **no status at all** until it resolves to a Capability identity; a Contradiction or dismissal renders without ever becoming a work item and is never auto-scheduled. Each is a scenario with a concrete negative assertion. |
| RFC8-6 | OS | `spec/work-surface` (durable-memory limb also `spec/context-packets`) | A compaction record is a fact about retention and may never alter a status claim | A scenario must assert that after a compaction the record is durably queryable and names what it summarized, what it discarded, and what remains externally queryable — and that the status claims covering the compacted window are **bit-identical before and after**, since "compaction changed a claim" is the failure this clause exists to forbid. Physical schema defers to RFC 0003; the queryability and non-alteration behavior does not. |
| RFC8-7 | OS | `spec/work-surface` | Post-materialization scheduler state is never held in a Syzygy store; regret is a new Proposal, never a mutation | Two testable limbs: the pre-materialization lifecycle renders in RFC1-31's own state names with `queued-for-materialization` as a recorded queue act **never labelled "scheduled"**; and no annotation, field, log, or appended entry recording post-materialization scheduler state is ever written to the materialization record or as a `.syzygy/work/**` transition — a spec must assert the write does not happen while the permitted immutable evaluation-stamped *observation* of the transition does. |
| RFC8-8 | OS | `spec/work-surface` | Orphaned work is a Contradiction whose only lawful exit is adjudication; exclusivity binds every total | The highest-density behavioral clause in module 1. Scenarios: "what remains" returns three separately labeled plane groups; drafted proposals render *unadopted draft* and are excluded from every approved-intent total; a scheduler item with no materialization record mints a Contradiction, routes to adjudication, renders the affected conclusion Unknown (reason #8, `suspended` tier) and is **exempt from filtering**; two proposals in one exclusivity group render as *N candidate futures* and never sum to 2. |
| RFC8-9 | OS | `spec/work-surface` (Polaris read-only limb: `spec/intent-surface`) | The SDR-18 boundary against Polaris, and that it does not qualify the scheduler's typed authority | Observable on two surfaces: Polaris offers **no mutation affordance** over queue state, assignment, or progress (read-only rendering, RFC7-24), and an intent-shaped queue item appears in Trajectory's queue and adopts through Polaris while both surfaces answer with **one and the same Proposal identity and state** (RFC6-3) — a cross-surface consistency scenario. |
| RFC8-10 | OS | `spec/work-surface` | Materialization is a one-way door; the record's three components are all required, none conditional; until the record exists, materialization has not occurred | A spec must pin the bidirectional walk (work item → materialization record → proposal → pinned intent revision, and back), assert a record missing any of the three components is not a record, assert the materializing evaluation renders beside it as a surface-side extension, and assert a scheduler item with no record produces the RFC8-8 Contradiction rather than a silent skip. |
| RFC8-11 | OS | `spec/work-surface` | Divergence renders and is never adjudicated by the surface; the record is never rewritten | A scenario must assert the exact rendering of a substrate-side edit of a Syzygy-written warrant pointer — an annotation reading "edited in substrate at T; not a warrant claim" — that the `.syzygy/work/**` record stays authoritative, that the pointer is **re-asserted at the next evaluation**, and that no contradiction is minted on that join. |
| RFC8-12 | OS | `spec/work-surface` (two-field carriage also binds `spec/map-lenses`) | The closure at thirteen values in three partitions; the state is a per-evaluation derived projection and not a Claim; the mapping is RFC3-16(a) material | **Highest leakage risk in the package.** The clause spells out a closed value set an implementer could build straight from, skipping specification — so the spec must own it explicitly: the exact value set served on every rendering, filter, count, and machine answer; that no value outside the list is ever emitted, minted, or force-fit; that the state is recomputed per evaluation and is nowhere writable; that the chain state travels beside it on **every** carrier; and that the four absence values never enter an RFC2-24 Unknown-reason aggregate. The mapping artifact's authorization predicate (a mapping row projecting a custom status into `ready`/`active` is a privilege escalation) needs its own scenario: a valid state-(1) or state-(2) act honors the mapping with its exact state rendered, while an absent or invalid act leaves it inoperative. |
| RFC8-13 | OS | `spec/work-surface` | Every value has a declared derivation and a declared honest-absence behavior; no value is guessed or force-fit | **Highest leakage risk with RFC8-12.** Thirteen derivation rows plus thirteen absence behaviors are effectively a ready-made requirement table; left unspecified an implementer would treat the RFC as the spec. Each row is one or more scenarios: `merged` derives from a VCS merge fact only and never from scheduler closure; an unreadable dependency set yields `eligibility-undetermined`, never `planned`; `ready` is computed **over snapshot inputs only** and calling the substrate's live readiness computation at answer time is a defect (the identity test on re-run is the assertion); `review` never claims reviewer activity and a merge-readiness verdict expires when the head SHA moves; `reconciled` never renders at V0. |
| RFC8-14 | OS | `spec/work-surface` | The normalized state is a lens, never a replacement; `state-undetermined` is state-local, never an RFC2-24 reason | A scenario must assert that the substrate-qualified raw status is rendered **and queryable** beside every normalized state, and that a status the declared mapping does not cover (`pinned`, `hooked`, a custom status) returns raw status + `state-undetermined` — never dropped from the result set, never force-fit into a neighbouring state — and never increments any project Unknown-reason count. |
| RFC8-15 | OS | `spec/work-surface` | Closure is not a normalized "done"; no label meaning done/complete/finished/resolved | Assertable both ways: closure with no merge fact renders `closed-unmerged` carrying the substrate's reason **verbatim** (Unknown citing the substrate's silence where none was recorded), never green; closure *with* a merge fact renders `merged` and enters the reconciliation chain; the closure event stays queryable execution history in both cases. |
| RFC8-16 | OS | `spec/work-surface` | `active` is unrenderable until a staleness bound with an effective owner act is declared; valid state (1) or state (2) is disclosed, missing or invalid acts leave the bound undeclared; the inadmissible-signal list | Fail-closed behavior a spec must pin: with no effective bound, claimed items render `activity-undetermined` and `active` is emitted by nothing; a valid state-(1) or state-(2) act makes the bound usable with state shown but is never liveness evidence; past the bound, `stale-or-dead` **with the last-signal instant shown**; between signals, worker liveness Unknown. Negative scenarios: a fresh coordinator heartbeat, a lock label, or an existing worktree must not produce `active`. The bound's *value* is quality-policy material; the obligation, act-state disclosure and fail-closed rendering are behavior. |
| RFC8-17 | OS | `spec/work-surface` | The closed four-member blocked-cause taxonomy with a declared derivation each | A spec must pin the derivation of each cause (`dependency` from unmet edges, `pr-wait` from `external_ref` + PR/review state, `external` from a declared external event, `decision` from a pending human gate) and assert that where the substrate conflates causes the item renders **blocked with cause Unknown** — the blocked fact never suppressed, the cause never inferred from a title. |
| RFC8-18 | OS | `spec/work-surface` | Cost is independent measures; the independence rule is not amendable; the `declared-only` tier for estimates | The prohibition is directly testable at the answer surface: **no composite effort or health number is computed, rendered, or served** — no such field exists in any endpoint answer or aggregate. A spec must also pin each measure's declared source and evidence class, that derived-from-rates cost is labeled Inferred, that attempts count only from Execution Records, and that touched-components resolves through the declared implementation mapping (absent mapping ⇒ Unknown, not a guess). |
| RFC8-19 | OS | `spec/work-surface` | Absent means Unknown, never zero (SDR-6); a predominantly-Unknown cost pane is correct output | A scenario must assert every aggregate over partially-known measures carries its coverage disclosure ("cost known for n of m runs") and that no aggregate renders as a complete total; the adversarial case is a sum that silently treated Unknown runs as zero, which must be indistinguishable-proof — i.e. the total is refused, not rounded. |
| RFC8-20 | OS | `spec/work-surface` | V1 telemetry renders **exclusively** from captured Execution Records; nothing at V0 may simulate telemetry; streaming and control stay deferred | A spec must pin the V1 post-hoc telemetry fields (per-run model/runtime, timing, tokens/cost, attempts, gate outcomes at their tiers, parent/child run structure) with absent fields Unknown, and pin the V0 negative: no simulated, extrapolated, or placeholder telemetry value is ever served. |
| RFC8-21 | OS | `spec/work-surface` | The chain is honest but thin, and thinness must render as thinness — never as a chain awaiting completion | A spec must pin the eight-link bidirectional walk and assert **every link renders its declared join basis** with `naming-convention` links marked `reduced-fidelity`. The clause's own warning binds the spec too: an acceptance test must not be written that presents the thin chain as incomplete-but-improving. |
| RFC8-22 | OS | `spec/work-surface` | Reconstructing a join by similarity, interpolation, or inference is forbidden; missing evidence never renders Inferred | A scenario must assert that an unestablishable link renders the break **at that link** with its RFC2-24 reason and degrades everything downstream, and the negative: a fuzzy or heuristic match (e.g. a deleted branch name matched by similarity) must not produce a link — the chain reads broken, not clean. |
| RFC8-23 | OS | `spec/work-surface` | Unknown-provenance is first-class, never green, never an ingest rejection; it never absorbs orphaned work | A spec must pin Unknown-provenance as a filterable **and always counted** rendered state, assert ingest never rejects an unwarranted item, and assert the routing discrimination: where an item is both Unknown-provenance and orphaned, the orphaned-work Contradiction governs and is never filtered away behind the provenance badge. |
| RFC8-24 | OS | `spec/work-surface` | These are **claim** reasons only; the state vocabulary's absence values take none of them | A spec must pin each reason's rendering with its resolution route visible, and in particular that facts lost past the retention horizon render **citing the retention event** and never as "no work existed", and that an undeclared maximum inter-pass interval makes every claim depending on pre-horizon scheduler history render Unknown on currency mechanics. Aggregation follows RFC2-24 (aggregate, disclose reason counts, expand). |
| RFC8-25 | OS | `spec/work-surface` | Fail-closed inheritance (no declared threshold ⇒ nothing inherits); a warrant is never extended by execution-side prose; the sub-entry tier is fixed at `asserted-by-worker` | Several distinct scenarios: an inherited mutation renders as a sub-entry of the parent run's summary with rationale and touched surfaces (never its own work item, never invisible); a diff hunk resolving to neither renders Unknown-provenance; with **no declared threshold**, every change requires its own warrant and the account renders the absent policy; a touched surface outside the parent warrant's declared scope renders Unknown-provenance exactly as if no parent summary existed; the sub-entry is never a status input. The threshold *value* is quality policy — that limb belongs to `governance/policies/`, not to a requirement. |
| RFC8-26 | OS | `spec/work-surface` (consumed by `spec/context-packets`) | The preservation set is binding and survives **every** compaction | A scenario must assert that after any compaction the seven preserved classes (structured run summaries, work warrants, decisions, materialization mappings, known cost/token totals, evidence identities and hashes, reconciliation outcomes) remain queryable, while raw transcripts and verbose logs may be gone under declared policy — the failure case is a compaction that dropped a preserved class. |
| RFC8-27 | OS | `spec/work-surface` (consumed by `spec/context-packets`) | No observer or surface ever *upgrades* a tier; degradation happens only through a new identified evaluation; artifact resolvability alone is not the test | Dense and testable: a claim whose only substantiation expired renders Unknown **citing the compaction or retention event**; a preserved gate outcome keeps the tier its evaluation recorded even after the provider expires its records (the capture artifact carries it); a preserved hash with no capture artifact **caps at `report-fact` with the cap visible**; a gone artifact drops tier at the next evaluation with the reference rendered broken; and "no records found" must be visually **and queryably** distinguishable from "nothing happened". |
| RFC8-28 | OS | `spec/work-surface` (carriage also binds `spec/map-lenses`) | The four post-merge answers never share a rendering; the chain state is a field of its own, orthogonal to the normalized state | **Second highest leakage risk** after RFC8-12/8-13: a six-value closed chain vocabulary spelled out beside a required carriage rule is buildable-from directly. A spec must pin the values as queryable and filterable on the durable identity, assert that *reconciled at E* / *merged not yet evaluated* / *evaluated and unsatisfied* / *evaluated, contradiction raised* never collapse into one badge or count, that `unsatisfied` and `contradiction-raised` never merge, that scheduler-state repair shares no field, count, or UI string with reconciliation, and that **every** rendering, filter, count, endpoint answer, and cross-surface handoff carrying the normalized state carries the chain state beside it. |
| RFC8-29 | OS | `spec/work-surface` | V0 renders the absence honestly; nothing in V0 simulates a verdict; a wall of Unknowns is correct output | A scenario must assert every merged-but-unreconciled item renders "reconciliation evidence absent / Unknown" at V0, and the V1 staging: the reconciliation evaluation is computed and its gap rendered as a **navigable object**, not a number. The V0 negative — no simulated, defaulted, or optimistic verdict — is the load-bearing assertion. |
| RFC8-30 | OS | `spec/work-surface` | The closure fallacy is forbidden, including in prose — a narrative sentence doing a badge's work is judged as a badge | A spec must assert no aggregate, badge, progress bar, or generated sentence renders a `closed` item as done, complete, or satisfied absent a `reconciled@E` verdict with gate-backed evidence, and that every progress aggregate over merged work discloses its reconciliation composition (n reconciled, m pending, k unsatisfied, c contradiction-raised, j Unknown) — a 100% bar over merged-but-unreconciled work is the canonical failure. |
| RFC8-31 | OS | `spec/selection-api` + `spec/work-surface` | Trajectory adds **no surface-only facts**; every answer is endpoint-answerable at a named evaluation | This is Trajectory's RFC 0006 conformance surface and every limb is assertable: selection by kernel identity only (no work-item row handles crossing boundaries), the single drawer fact set, label parity on machine answers, evaluation stamping, aggregation disclosure, the closed navigation-outcome set including `incompatible-scenario`, and explicit singular scenario context travelling with every URL, cross-surface synchronization, and query answer. Parity scenario: anything rendered (normalized state, blocked cause, chain join, cost measure) is queryable **with identical labels**. |
| RFC8-32 | CR | — (routes to craft-and-care / release policy) | The whole clause: this contract schedules nothing, and the coverage matrix is review material, never authority | Not user-observable behavior and not a model-shape invariant — it is a **process and release-gate obligation**: it forbids scheduling implementation work from RFC prose and requires, as a surface-specification deliverable, a clause-to-requirement coverage matrix over every clause of this contract other than this one, across all of the package's modules, with each clause mapped to requirement identities or a reviewed N/A. Specifying it as an OpenSpec requirement would be circular — the clause governs how OpenSpec content comes to exist. This document is a precursor to that deliverable. |

**Tally:** OS 31 · N/A 0 · CR 1 · IR 0 · total 32 (sums: yes — 31 + 0 + 1 + 0 = 32)

**Notes and doubts:**

- **Zero N/A is a deliberate result, not an unapplied category.** RFC 0008 is a
  surface contract: with the single exception of the phase rule, every clause
  constrains what a human or a machine client *sees* in an answer. Under the
  stated strictness bar — N/A only where a clause shapes the model with no
  distinct user-visible outcome beyond clauses already routed OS — no clause
  cleared it. The rev10 matrix classed 30 of 32 as DI; re-decided on the
  merits, all 30 carry observable limbs. The corollary is a large
  `spec/work-surface` domain, and that is the honest shape of the seam.
- **RFC8-2 — closest N/A call.** Limbs (a) and (b) genuinely produce nothing
  observable that RFC8-3/8-7 and RFC8-15/8-30 do not already produce; had the
  clause been only (a)+(b) I would have routed it N/A. It is OS solely on limb
  (c) — the past-window "what did the fleet change, at what cost, under whose
  authority" query, which no other clause obliges as a query. If a reviewer
  judges (c) subsumed by RFC8-21 + RFC8-18/8-19 + RFC8-31's endpoint
  answerability, this row becomes N/A. Flagged.
- **RFC8-4 — second closest.** Routed OS because the binding table fixes *which
  kernel identity type* each surface concept's answer returns (and that a
  warrant is not selectable at all), which a spec must pin before any scenario
  over these answers can be written. A reviewer could reasonably hold that this
  is model shape and that all observable consequence flows through RFC8-31's
  selection rule and RFC8-5's non-reifications. Flagged.
- **RFC8-6 — third closest.** Its schema defers to RFC 0003 and its retention
  semantics are elaborated in RFC8-26/8-27; the surviving distinct assertion is
  "a compaction record is queryable and a compaction never alters a status
  claim." Thin but real. Flagged.
- **RFC8-9 — route is settled, the domain is not.** The clause binds two
  surfaces; I named `spec/work-surface` primary with the Polaris read-only limb
  in `spec/intent-surface`. If the domains are meant to partition by owning
  contract rather than by rendering surface, the read-only limb may belong
  wholly to `spec/intent-surface`. Flagged as a domain doubt.
- **RFC8-32 — CR versus N/A.** It is not behavior and not model shape, so the
  live alternative to CR was N/A. CR is correct because the clause states a
  positive obligation on a future *process* (produce a coverage matrix at
  surface specification, review it, never treat it as authority), which is
  exactly craft-and-care / release-policy territory. Flagged so the choice is
  visible rather than assumed.
- **Leakage-class clauses, as instructed.** RFC8-12, RFC8-13, and RFC8-28 are
  the package's buildable-from-prose risk: a thirteen-value closed vocabulary
  with a full derivation matrix, and a six-value chain vocabulary with a
  required-carriage rule. All three route OS, and their spec entries must own
  the *value sets and derivations themselves* — not merely cite the RFC —
  because an implementer handed only the RFC would ship them without any
  approved requirement, which is precisely what RFC8-32 forbids. RFC8-7 and
  RFC8-10 carry the same hazard in smaller form (a lifecycle state list; a
  three-component required-field list).
- **Policy limbs noted, not routed CR.** RFC8-16 (staleness bound), RFC8-24
  (maximum inter-pass interval), and RFC8-25 ("small" threshold) each defer a
  *value* to quality policy while binding a fail-closed *rendering* now. The
  rendering is the routed content; the value-declaration obligation belongs to
  `governance/policies/**` and is called out in each row rather than splitting
  the row.

---

---

## RFC-0009 — Orrery (Map Surface)


**Enumeration method:** clause *definitions* were extracted with Python `re`
(never shell grep — `grep` on this machine is ugrep and mismatches bracket
classes). Pattern, applied with `re.M` to each of the three module files
(`semantic-geography.md`, `visual-grammar-and-lenses.md`,
`interaction-parity-and-release.md`) read whole via `pathlib.Path(...).read_text()`:

```python
pat = re.compile(r'^\*\*(RFC9-\d+(?:\([a-z]\))?)(?![\w(])', re.M)
```

The trailing `(?![\w(])` is load-bearing: an earlier `\b` form silently
dropped `RFC9-16(d)` (backtracking matched the bare integer and left the
`(d)` behind), and an earlier `(?=[.,]|\s+—|\*\*)` form dropped it too
because that heading reads `**RFC9-16(d) is owner-gated…`. Both misses were
caught by a second method: reconciling the extracted set against the
README's declared inventory (52 integers + 8 lettered sub-clauses = 60) and
asserting `[n for n in range(1,53) if n not in ints] == []` and zero
duplicates. `README.md` is the package index and defines no clauses; it was
read for the lookup rule and excluded from enumeration.

Verified in the same run: 52 integers RFC9-1…RFC9-52 each present exactly
once, 8 lettered sub-clauses, 0 duplicates, 0 gaps. Note that lettered
*limbs* cited inside a parent (RFC9-10(c), RFC9-19(b), RFC9-16(a),
RFC9-15(b) parts 1–4) are parts of their parent clause per the README's
lookup rule and correctly do not appear as separate rows.

**Clauses found:** 60 — RFC9-1, RFC9-2, RFC9-3, RFC9-4, RFC9-5, RFC9-6, RFC9-7, RFC9-8, RFC9-8(a), RFC9-9, RFC9-9(a), RFC9-9(b), RFC9-10, RFC9-11, RFC9-12, RFC9-13, RFC9-13(a), RFC9-14, RFC9-14(a), RFC9-15, RFC9-16, RFC9-16(d), RFC9-15(b), RFC9-17, RFC9-18, RFC9-19, RFC9-20, RFC9-21, RFC9-22, RFC9-23, RFC9-24, RFC9-25, RFC9-26, RFC9-27, RFC9-28, RFC9-29, RFC9-30, RFC9-31, RFC9-32, RFC9-33, RFC9-34, RFC9-35, RFC9-36, RFC9-37, RFC9-38, RFC9-39, RFC9-40, RFC9-41, RFC9-42, RFC9-43, RFC9-44, RFC9-45, RFC9-46, RFC9-47, RFC9-47(a), RFC9-48, RFC9-49, RFC9-50, RFC9-51, RFC9-52

*(Rows follow document order within the package: module 1 → 2 → 3. In module
1, RFC9-16 and RFC9-16(d) are authored ahead of RFC9-15(b); that authoring
order is preserved rather than re-sorted, so the row sequence matches the
reading order a fresh reader meets.)*

| Clause | Route | Future spec domain | Retained invariant in the RFC | Justification |
|---|---|---|---|---|
| RFC9-1 | OS | `spec/map-surface` | The map is a projection over the one shared kernel, never independently authoritative; historical scope is constitutional and unconditional (D1) | A scenario must assert the map renders RFC 0002's label/tier/Unknown-reason/freshness strings **verbatim** rather than surface-paraphrased, and that "Orrery" appears only as UI chrome while schema and API names stay literal — both are directly inspectable outputs. |
| RFC9-2 | N/A | — | Semantics-and-determinism-only boundary; no conforming rendering, layout-algorithm, or tuning choice may weaken a clause of this RFC | Nothing here describes an output: the clause allocates *authority* between this contract and later design/spec material. No scenario can assert "the contract declined to bind rendering technology" — the claim is checked by reading a later artifact against this one, and the clause mandates no such check (RFC9-47(a) does). Its only enforcement is precedence during amendment review. |
| RFC9-3 | OS | `spec/map-surface` (drawer-exclusion limb also `spec/selection-api`) | Encoding provenance is surface-local, never a member of RFC6-18's shared drawer fact set, because that set carries no lens dimension | Two assertable behaviors: at the point of selection an "explain this encoding" affordance reaches the exact channel readings applied plus each metric; and an element whose encoding cannot be traced to an identified artifact **does not render that encoding**. The negative limb — the shared drawer fact set is unchanged by lens state — is a `spec/selection-api` scenario. |
| RFC9-4 | OS | `spec/map-surface` | Position in home geography is bound to declared identity; capability district is the anchor level; measurement never moves a building | A scenario must assert the rendered containment hierarchy is exactly project → capability district → component block → plot/building, and that detail below source/test evidence appears as **evidence listings, not modelled geometry** — a user-visible difference between a drill-down list and a rendered interior. |
| RFC9-5 | OS | `spec/map-surface` | The two closed lists (what may anchor, what may never) are the enforcement point for every other placement rule | A scenario must assert that a `declared-only`-tier mapping still places the building while its satisfaction claim renders Unknown; that a drafted declaration renders in the proposed treatment with an "unadopted" plate and anchors nothing; and that an inferred mapping renders hatched-with-provenance as an annotation over a position it did not produce. |
| RFC9-6 | OS | `spec/map-surface` (retired-URL limb also `spec/selection-api`) | Identity continuity is RFC 0001's and is never re-decided by the surface | A scenario must assert a rename changes the label and **no coordinate**; a split/merge renders an identity event showing old and new identities simultaneously rather than relocating silently; retirement ghosts the district as a rendered event; and a URL pinned to a retired district resolves per RFC6-11 — never 404, never auto-redirect. |
| RFC9-7 | OS | `spec/map-surface` | Code with no declared capability mapping is Unknown, never inferred into one | A scenario must assert that unmapped code appears in the unmapped district carrying the Unknown treatment, and specifically that it is **not** placed adjacent to the capability an inference would have guessed — the "plausible-looking neighborhood" is the failure to test for. |
| RFC9-8 | OS | `spec/map-surface` | The portfolio level is a derived arrangement, not an entity; portfolio relations are profile relations, never kernel `depends_on` | A scenario must assert cross-project edges render only where declared, one-sided declarations render **unconfirmed/asymmetric**, the legend names the profile relation as itself, and onboarding a new project perturbs no already-placed project's position. |
| RFC9-8(a) | OS | `spec/map-surface` | The portfolio registry and its reorganisation events live in a **typed, owner-gated governance store** at workspace scope (RFC3-15's class), honored only through an effective exact-digest owner act under RFC3-16(a), in state (1) or state (2), with that state rendered — **never the workspace manifest and never `local/`**, which carry at most a non-authoritative pointer; **until such a store exists, no portfolio re-lay is lawful**, and establishing one is an owner act of RFC3-15(a)'s recorded-widening class | A scenario must assert that with no workspace-scope governance store, or with an absent or invalid registry act, a portfolio re-lay is refused (fail-closed, manifest never substitutes); and that once the store and effective act exist, a re-lay renders the act's exact state plus a reorganisation event naming old and new **portfolio** layout versions with recorded rationale, with a portfolio-scope saved camera saved under the prior version refusing to restore silently. |
| RFC9-9 | OS | `spec/map-surface` | Proximity carries exactly two declared readings and no third; no undeclared signal is an input to placement; containment beats relatedness where they compete | A scenario must assert the position/proximity legend states containment and best-effort relatedness (never "proximity: inert"), that each `declared-dependency` edge renders an explicit **honored / not-honored** state, and that the not-honored count is surfaced as a first-class quantity rather than derivable only by inspection. |
| RFC9-9(a) | OS | `spec/map-surface` | Reader-decidability (part 2) and the anti-counterfeit bar (part 3) are what the third legend line disclaims; dropping either keeps the disclaimer and loses the property | A scenario must assert the registry produces **three** legend readings including "residual adjacency — carries no meaning"; that meaningful nearness is decidable on screen (intra-district boundary rendered, or an honored edge rendered); and that free-space placement produces no enclosure, shared boundary, plinth, or common ground plane for baseline-delta neighbours. |
| RFC9-9(b) | OS | `spec/map-surface` | The state is [Observed] about the *layout*, never an epistemic class of the relation; a `not-honored` edge is a true fact, not a defect and not an Unknown | A scenario must assert the three-value domain renders distinctly, that the state is unresolvable and therefore not shown without its layout version, that an edge with an unplaced endpoint renders the reserved Unknown with reason `missing-declaration` and is counted in **neither** RFC9-15(b) partition, and that with no registry entry the state does not render while the edge still does. |
| RFC9-10 | OS | `spec/map-lenses` | Analytical planes carry no append-stability and no cross-evaluation coordinate promise, and must say so; the *interaction cost* of returning home is deliberately unbound (B21) | A scenario must assert every analytical plane renders (a) first-class position/proximity legend entries, (b) a persistent non-dismissible not-home marker, (c) a return-to-home path that is available and discoverable from anywhere in the plane, and (d) the named evaluation it projects. |
| RFC9-11 | OS | `spec/map-lenses` (default-scene limb also `spec/map-surface`) | An analytical layout may never masquerade as home; a metric-bound position without the marker is a violation identical in class to an unlegended channel | A scenario must assert the surface opens in home geography by default, that entering a plane is an explicit labelled act, that the marker cannot be dismissed or suppressed, and that saved camera homes and "you are here" continuity are offered in home and **not** in any analytical plane. |
| RFC9-12 | OS | `spec/map-lenses` | Any view change that moves entities is by definition an analytical-plane or scenario switch, and is labelled as one | A scenario must assert that switching lenses preserves camera, selection, and every coordinate while swapping the visible legend — the exact before/after coordinate-identity check a user experiences as "the city did not move." |
| RFC9-13 | OS | `spec/map-surface` | Personal presentation state lives in `.syzygy/local/` and never affects truth-bearing encodings (VIS-6 exception (a)) | A scenario must assert that an active filter renders a **persistent count of what it hid** (not a transient toast, not an absent indicator), and that no filter, camera, or bookmark changes any epistemic or measured encoding on a rendered element. |
| RFC9-13(a) | OS | `spec/map-surface` | Coordinate-bearing personal state is the one artifact RFC6-9's identity re-resolution did not reach, so it carries its own stamp-and-refuse rule | A scenario must assert that a camera home saved under layout version *v1* and restored under *v2* is marked **stale-layout**, names both versions, offers the reorganisation event's before/after, and restores raw coordinates only after an explicit act — never landing silently on a different district. |
| RFC9-14 | OS | `spec/map-surface` | The layout input tuple is closed at (declaration set, layout baseline, layout version) and nothing else; the base layout is inside the VIS-7 identity test | A scenario must assert that the same tuple yields byte-identical coordinates across runs and implementations, and that the unmapped district's path-derived arrangement is excluded from the cross-snapshot stability guarantee **and says so on its face** to the reader looking at it. |
| RFC9-14(a) | OS | `spec/map-surface` | Each of the three inputs is defined closedly; unadopted declarations are not members of the declaration set; the baseline is immutable after the regeneration act writes it | A scenario must assert the layout baseline exists as an identified, resolvable governed artifact under `.syzygy/map/**` and is carried as a snapshot input, and that the recorded base layout **reproduces** from (declaration set, baseline, version) — a checkable-but-unreproducible base layout is the failure to catch. |
| RFC9-15 | OS | `spec/map-surface` | Determinism alone does not give stability; append-stability is an independent obligation, and a reproducible layout that reshuffles on every addition falsifies the 3D mandate | A scenario must assert that adding one capability, component, building, or project changes the coordinates of **zero** existing declared entities. (The fixture-testing and release-gating of this property is RFC9-47's obligation, not this clause's; the behavioral requirement remains OpenSpec's.) |
| RFC9-16 | OS | `spec/map-surface` | The relocation-trigger set is closed at four; a version change with no recorded rationale is not a lawful trigger | A scenario must assert each of (a)–(d) produces a **rendered event** rather than a silent teleport, that (c) surfaces its governing decision or declaration link, that (d) names old and new versions with before/after reachable and a rationale stating what the new layout buys and what it moves, and that no coordinate change occurs outside these four. |
| RFC9-16(d) | CR | — (craft-and-care / governance-act procedure; the check itself is gated by RFC9-47) | A layout version change is an owner governance act; "same placement function" means agreement on **all** input tuples; an asserted equivalence is not a carve-out but an ungated relocation | This clause governs how a change is *authorized and demonstrated*, not what a reader sees: it mandates a layout-equivalence harness that exercises both versions over a declared input space, compares coordinates, and records its result, and expressly disclaims being an RFC2-3 identity test. The user-visible consequence of a version entry lacking an effective owner act — the scene renders Unknown rather than resolving against it — is RFC9-18's clause and is routed OS there. |
| RFC9-15(b) | OS | `spec/map-surface` | Coordinates are fixed within a layout version; scoped regeneration is barred because it makes coordinates a function of refresh history; insertion order is never an input | A scenario must assert that the not-honored backlog renders **partitioned** into refresh-clearable and structurally-unhonorable counts, that an unpartitioned total does **not** render at all, that a scoped-refresh request is rejected rather than honored partially, and that a refresh never fires automatically on a declaration change. |
| RFC9-17 | OS | `spec/map-surface` | Reservation policy must be unbounded in principle, so growth never forces a version change; exhausting a reservation is a defect in the policy, never a licence to relocate | A scenario must assert a null coordinate delta across each named churn source — mapping-preserving refactor, file move/rename/reformat, any metric change in any lens, a re-evaluation over an unchanged snapshot at a later as-of, lens/filter/camera changes, and a footprint band change (which varies inside its reserved extent and displaces no neighbour). |
| RFC9-18 | OS | `spec/map-surface` | Registry entries fix which layout version a scene's positions *mean*, and nothing in `map/` becomes independently authoritative over kernel semantics | A scenario must assert that a valid state-(1) or state-(2) exact-digest owner act under RFC3-16(a) establishes the version with its exact state rendered, while an absent or invalid act **does not establish a version** and a scene resolving against it renders Unknown rather than silently adopting the version an untrusted writer declared; and that computed geometry is rebuildable `cache/` while camera state is `local/`. |
| RFC9-19 | OS | `spec/map-surface` | Two separately selectable copies of one identity break identity-based counting and selection identity — that, not the trust-floor link rule, is what the no-clone rule rests on | A scenario must assert all three placement mechanisms are supported, and specifically that under mechanism (c) the link marker in a non-home district **resolves to the one entity** — one selection reference, one drawer, one count — rather than instantiating a second selectable building. |
| RFC9-20 | OS | `spec/map-surface` | No precedence rule may resolve competing declared placements; "primary" names a declared primacy where governance supplies one and never licenses a surface to designate one | A scenario must assert that an undeclared shared component lands in the marked **placement-undeclared** aggregation with reason `missing-declaration` routing to the drafting affordance; that two co-unsatisfiable declarations (including two adopted `placed_in` edges) render **Unknown-placed** with conflict marker and adjudication route; and that such an entry counts in **neither** candidate district and once in the Unknown-placed aggregation. |
| RFC9-21 | OS | `spec/map-surface` | Aggregates count each identity once per query subject; district totals may therefore lawfully exceed the project total, and a project total computed by summing districts is comprehensible fiction | A scenario must assert the scene-scoped trigger fires: wherever a shared contribution enters more than one rendered aggregate, **every** such aggregate carries the shared-contribution disclosure ("N shared, counted once at project scope") — not only a table that happens to place district and project totals side by side. |
| RFC9-22 | OS | `spec/map-surface` | Repository membership is an overlay; partitioning space by repository first would re-anchor geography to a storage fact | A scenario must assert the repository boundary renders as a **toggleable** boundary treatment over unchanged capability geography, and that a present-but-unconsented repository renders as a walled, Unknown-filled zone — never as empty ground, which reads as "nothing there." |
| RFC9-23 | OS | `spec/map-surface` | Write authority a reader cannot see is the surprise this overlay exists to prevent | A scenario must assert the overlay renders the governance root as a civic marker legended as the only place Syzygy writes project content directly, adapter-mediated authorities as a distinct boundary kind with adapter and authorization visible, consent scopes and execution-profile boundaries on the project's surface, and secret-exclusion zones as sealed markers at the declared minimum aggregation. |
| RFC9-24 | OS | `spec/map-surface` | The *role* reservations are bound here and no lens may repurpose them; concrete hues and materials are design-contract material left open | A scenario must assert each reserved state renders in its own mutually distinct treatment — Contradicted as Unknown base plus conflict marker plus adjudication route, Dismissed-by-decision as a struck plate with reason and expiry (never green/resolved/aligned), Proposed as wireframe-and-translucent, Unadopted as proposed-plus-plate — and that the freshness family composes *on top* (stale desaturates with age plate, broken shows last-good marked broken, superseded ghosts). |
| RFC9-25 | OS | `spec/map-surface` | Freshness owns saturation exclusively, in every scene profile; which channels a lens ramp may then use is rendering material this RFC does not bind | A scenario must assert that switching between any two lenses leaves position, district boundary, epistemic rim/plate, and saturation unchanged on every element — so that a desaturated building always reads "stale" and never "low on this ramp." |
| RFC9-26 | OS | `spec/map-surface` | One channel, one meaning at a time, never unlegended; a forged entry is the sharper failure than a missing one, because it leaves every downstream status check passing | A scenario must assert that every legend string is **generated from the registry** (mutating an entry changes the rendered legend; no hand-authored fallback exists), that a channel with no registry entry does not render, that a valid state-(1) or state-(2) exact-digest owner act makes an entry effective with its exact state rendered, and that an entry with an absent or invalid act is treated exactly as absent. |
| RFC9-27 | OS | `spec/map-surface` | Unknown is a first-class colour and one rule with two scopes (per element and per aggregate); empty-looking is earned, never defaulted | A scenario must assert every channel's Unknown value is visually distinct from both ends of its own scale and from any "good" reading (a stub, never zero-height; marked-unmeasured, never cold), that each Unknown carries its RFC2-24 reason verbatim with a resolution-route affordance, that no epistemic state is carried by colour alone (≥2 of surface treatment / plate / label), and that a plot, block, or district renders *empty* only behind an executed RFC4-27 coverage record — otherwise Unknown with `mapping-coverage-absent`, in every scene including approved-intent and proposed. |
| RFC9-28 | OS | `spec/map-lenses` | No universal height meaning is frozen by this contract; the "height = LOC" anti-thesis is excluded by the lens contract rather than by freezing the channel | A scenario must assert that height carries exactly one declared meaning for the active lens, that the meaning is visible in the legend at all times, that a lens change alters both together, and that the Unknown height treatment is identical across lenses. |
| RFC9-29 | OS | `spec/map-surface` | SEC-5 sanctions rendering **the exclusion**, not its shape; the granularity bound is stated here because the map is where shape is most legible | A scenario must assert that labels, plates, counts, breadcrumbs, and tooltips state only what identified artifacts state, that truncation is marked rather than silent, that an Unknown entity carries an explicit "Unknown" label, and that a sealed marker discloses at the **declared minimum aggregation with no per-element match count** — a per-building count being a per-file match count rendered spatially. |
| RFC9-30 | OS | `spec/map-surface` | Inference never raises a status-bearing encoding; degradation is to Unknown, never to an error and never to a heuristic | A scenario must assert inferred contributions render hatched with provenance, that an open admitted challenge suspends the displayed claim to Unknown with reason `challenge-suspended` and tier `suspended` while keeping the deterministic basis visible, and that withdrawing SEC-2 consent degrades inference-dependent renderings to Unknown with `unconsented-source-or-provider`. |
| RFC9-31 | OS | `spec/map-lenses` | A lens may bind only the five named measured channels; an overlay may **never** bind a measured-magnitude channel, so lens and overlay encodings are always attributable | A scenario must assert exactly one lens is active at a time, that a lens cannot repurpose a reserved channel or palette state, move an entity, suppress an overlay's epistemic content, or render without its full legend, and that every overlay renders as categorical or state marks — never as a colour ramp, height, heat, footprint band, or edge weight. |
| RFC9-32 | OS | `spec/map-lenses` | The two work-state fields are consumed verbatim from RFC 0008 and are orthogonal; a value the overlay cannot render is a defect here, never grounds to fold it into a neighbour | A scenario must assert the V0 set ships (Architecture and Verification lenses; work/construction and freshness overlays), that completed work removes scaffolding and turns nothing green, that a state-local **absence** value renders as itself rather than being folded into an Unknown aggregate or counted among RFC2-24 reasons, and that every element and aggregate carrying a normalized state also carries its RFC2-18 chain state, with `unsatisfied` and `contradiction-raised` never sharing a mark, colour, count, or legend entry. |
| RFC9-33 | OS | `spec/map-lenses` | Risk requires a policy-declared composite — an undeclared risk heatmap is inference wearing a deterministic costume; Runtime is hard-gated by SEC-3 through RFC 0005 execution profiles | A scenario must assert the staging as shipped behavior: Change/churn renders its window at all times and labels reduced fidelity; Risk does not render at all absent a declared composite; and until a captured-trace evidence class exists, runtime flow paths render **explicitly unmeasured** rather than being omitted or animated. |
| RFC9-34 | OS | `spec/map-lenses` | A lens never narrows the entity set — narrowing is a filter and is disclosed as one (RFC6-16) | A scenario must assert that a region for which the active lens has no inputs renders in the reserved Unknown treatment with its reason, and specifically that the region is still **present** at full entity count — the difference between "no data here" and a quietly shorter map. |
| RFC9-35 | CR | — (craft-and-care increment/release discipline; governance-act predicate under RFC3-16(a)) | Promotion to a named, governed, versioned artifact others can select requires an effective owner act in state (1) or state (2), with that state rendered — for lenses, analytical planes, and profile relations alike — and rides on *promotion itself*, so an absent or invalid act promotes nothing and nothing reaches shared selectable status by accretion | The clause binds how a lens **arrives**, not what it renders: it is a same-increment completeness obligation (channel declarations, Unknown behavior, legend, and tabular equivalent ship together, never a 3D-only skin) plus an authorization predicate on promotion. RFC9-49 names it as exactly that shape of obligation. Everything a promoted lens must then *do* is bound by RFC9-26/31/34 and routed OS there. |
| RFC9-36 | OS | `spec/map-scenes` | Factory is a second emphasis over the same graph and the same truth at the same addresses, never a second semantic model; all invariants bind every profile identically | A scenario must assert City is the profile V0 actually ships, and — when Factory arrives — that an entity occupies the same address in both profiles, so spatial memory transfers rather than being relearned. |
| RFC9-37 | OS | `spec/map-scenes` | Factory's honesty obligations are bound **now** so its later contract cannot relax them | A scenario must assert the capture window renders at all times, that motion **stops and marks** when its source stales (continuing motion reads as liveness), that an unmeasured factory renders visibly unmeasured rather than calm and orderly, that no flow is synthesized for illustration, and that live views contribute to no status claim. |
| RFC9-38 | OS | `spec/map-scenes` | Time is an explicit input, never ambient; a later as-of may only degrade a claim; read alone this clause licenses no particular historical rendering design | A scenario must assert every scene names its (source snapshot, as-of instant) **on the surface, not in a menu**, that a non-default-snapshot scene carries a persistent marker, that between-evaluation motion is a labelled transition whose interpolated frames assert nothing, that gaps between identified evaluations look like gaps, and that no building decays by wall clock. |
| RFC9-39 | OS | `spec/map-scenes` | The approved-intent scene carries scenario context `Base` and no implementation may mint a fourth context value; V0 defers the gap *object*, never the marker | A scenario must assert base-vs-intended renders three visible sets, that an intended-and-absent capability, block, or plot renders as a **marked, labelled, expandable vacancy** with its reason and resolution route (never negative space), that the propagated context in URLs and cross-surface syncs is `base`, that no entity moves entering this scene, and that contradicting approved inputs render Unknown with an adjudication route rather than a resolved intent. |
| RFC9-40 | OS | `spec/map-scenes` | Determinism of a computation is not evidence of existence — a computed merge projection is derived, never solid | A scenario must assert that proposals in one exclusivity group or of undeclared compatibility are never unioned into one scene but offered as N candidate futures selectable one at a time, that proposed structure is distinguishable from existing structure **in every profile at every zoom step**, that each proposed scene names its base on-surface, and that structurally divergent proposals compare side by side in their own address spaces with shared declared districts as registration anchors. |
| RFC9-41 | OS | `spec/map-scenes` | Historical rendering is constitutionally in scope by adopted D1; the concrete interaction bundle (ghost steps, milestone scenes, scrubber) is **candidate design and binds nothing** until its own owner approval | A scenario must assert what binds whenever a historical scene renders at all: Observed + superseded state visibly distinct from current, the superseding evaluation named, staleness on the primary surface rather than in drill-down, and renderable-evaluation selection per the quality/evidence policy — plus that D1's adoption alone does not make the candidate bundle implementable. |
| RFC9-42 | OS | `spec/map-surface` | LOD may reduce geometric fidelity and label density freely but may never change a fact's epistemic state — only its aggregation | A scenario must assert the epistemic treatment set survives every zoom step by **substitution**: an Unknown or proposed region that becomes per-entity-illegible renders as an aggregate in the same reserved vocabulary ("Unknown ×40", a wireframed proposed district) rather than as ordinary solid mass, and that an unavailable interior renders Unknown rather than generic fabricated geometry. |
| RFC9-43 | OS | `spec/map-surface` | The aggregate disclosure is deliberately identical to the RFC9-46 equivalence tuple and to RFC6-17's foundation-layer enumeration; any divergence is a defect to close, never a surface-local variation | A scenario must assert an aggregate discloses membership count plus the **full** composition — per-label, all six RFC2-25 tiers, per-Unknown-reason, per-freshness-state, and the three sibling surface states — and supports expansion to members; and that an aggregated measured channel over mixed members carries its Unknown contribution as a marked stub fraction, a hatched band, or a refusal to render a magnitude, with the per-zoom legend stating which. |
| RFC9-44 | OS | `spec/map-surface` (URL-survival limb also `spec/selection-api`) | What is path-derived and unstable is the *arrangement*, never the identity; on an undeclared proving-ground project a mostly-unmapped map is the correct output | A scenario must assert the unmapped district aggregates by default with count, RFC2-24 reasons, and expandable detail; that **no** filter default, LOD step, lens, or profile can drop it; that its entities carry the "path-derived placement (may move on refactor)" marker and not a path-derived-*identity* claim; that selection references and URLs into it survive a refactor; and that its primary affordance routes to first-pass declaration drafting. |
| RFC9-45 | CR | — (craft-and-care / the effective release policy under `.syzygy/governance/policies/`) | The grey map is diagnosis, not breakage; frame rate, entity count, polish, and demo reaction are explicitly **non-criteria**; judgments, policies, and waivers are warrants for this walkthrough gate, never project evidence or proof that an effect succeeded | This is a walkthrough/release-policy gate protocol, not a rendering rule or generic release, deployment, or recovery authority. It mints three artifacts across three governance homes (execution record in `records/`, attributed judgment in `decisions/`, authorization-bearing release policy in `policies/`); state (1) and state (2) acts may make judgments, policies, and waivers effective with their exact state rendered. B12(b) is the binding default when no policy is effective; absent or invalid acts fail closed, with an unlawful verdict recorded as `verdict-unlawful`, the test Unknown-never-met, and the gate closed rather than converted to a fail. The clause's one rendering sentence — Unknown regions aggregate with reasons and routes at 90% Unknown — is already carried OS by RFC9-27/9-42/9-43/9-44. |
| RFC9-46 | OS | `spec/map-surface` | Non-3D views are co-equal product surfaces, not derived exports; the unpartitioned backlog total is not a lawful rendering on **either** surface; the tuple is a hand-maintained enumeration whose general form is an open RFC6-22 question | A scenario must assert that for one (evaluation, scenario context, lens, declared filter scope) the tabular view carries the same entity set, edges, epistemic states including sibling surface states, counts, evidence links, scenario context, **both** work-state fields where the overlay is active, the RFC9-9(b) positional-expression state per edge, and both RFC9-15(b) partition counts separately — the table reading these from the recorded base layout, never computing `0` from its own absent geometry. |
| RFC9-47 | CR | — (craft-and-care release checklist; this clause is the artifact that checklist consumes) | The gate list is the surface's checkable form of the trust floor, and an obligation absent from it is tested nowhere — demonstrated twice by review findings | Every item is a release check with a named fixture or check shape: determinism over two runs, permuted-order layout, baseline reproduction, rejected scoped refresh, not-honored rendering with its Unknown value exercised, partitioned backlog on both surfaces, the run carve-out demonstration, stale-layout camera fixture, the judged residual-adjacency check, proposed-scene fidelity per profile and per zoom, work-state fixtures carrying every chain outcome the release can produce, and a portfolio fixture carrying both an observed and a declared edge. None of this describes runtime behavior — it describes what must be exercised before a release ships. |
| RFC9-47(a) | CR | — (craft-and-care release checklist and the normative-change/amendment review) | The same-logical-change invariant binds RFC **amendment acts** — authority a craft checklist does not itself have — so an amendment that mints a checkable obligation without routing it here is an incomplete amendment, a defect of the amendment rather than later housekeeping | Both limbs are process: a review obligation at amendment time, and a per-release registry-completeness pass that walks every clause naming a release-blocking or fixture-tested obligation and verifies each is listed or explicitly recorded out-of-scope with a reason, whose result must be showable. No user ever observes the registry's completeness. |
| RFC9-48 | OS | `spec/map-surface` | Accessibility here is a truth requirement, not a compliance overlay: a reader who cannot perceive "Unknown" is being shown comprehensible fiction | A scenario must assert every action — traverse, select, zoom, lens, analytical plane, scenario, drawer, filter — completes by keyboard alone with no pointer and no camera manipulation; that the tabular equivalent is reachable as the screen-reader surface; that every epistemic state has a textual label satisfying RFC9-27's two-carrier rule; that reduced-motion is honored with no loss of meaning; and that text contrast holds in every scene profile. |
| RFC9-49 | OS | `spec/map-surface` | Truth is never purchased with frame rate; the permitted currency is VIS-1 rank 4, never rank 1; declaring the budget values before V0 ships is a craft obligation this clause holds open | A scenario must assert that when a budget cannot be met the surface narrows **only to a scope pre-declared beside that scene class's budget**, renders itself as narrowed, applies the identical narrowing to the non-3D view so the equivalence gate sees one scope, and names the selected scope in the answer's envelope as an RFC6-16 declared filter — never improvising a render-time scope from device capability, which would hand two readers different entity sets for the same URL at the same evaluation. Silent decimation, entity dropping, and stripping epistemic carriers are forbidden. |
| RFC9-50 | OS | `spec/map-surface` | Any later motion inherits RFC9-37's honesty obligations in full | A scenario must assert that at V0 nothing moves without a triggering cause — motion appears only as a labelled transition, an explicitly selected flow, or camera movement — so a static scene is genuinely static and no idle animation implies liveness. |
| RFC9-51 | OS | `spec/map-surface` | Binding light to a metric would imply liveness the evidence may not support | A scenario must assert that illumination and highlight vary only with interaction state (selection, search hits, cross-surface highlight per RFC6-3), are personal and excluded from truth-bearing encodings, and are legended as interaction state — so a brighter building never reads as a better-evidenced one. |
| RFC9-52 | CR | — (surface-specification phase deliverable; review material, never authority) | This RFC is not a specification of record and schedules nothing; the phase boundary exists so RFC prose is never quietly treated as an implementable behavioral spec; the clause creates no OpenSpec content now | The obligation is on the specification *process*, not on the product: before implementation every observable consequence of every clause of this contract other than this one must map to an approved OpenSpec requirement or scenario or carry an explicit reviewed N/A, and the phase must deliver a clause-to-requirement coverage matrix for RFC 0009 entire. This present matrix is an input to that deliverable, not a substitute for it. |

**Tally:** OS 53 · N/A 1 · CR 6 · IR 0 · total 60 (sums: yes — 53 + 1 + 6 + 0 = 60, and 60 matches the enumerated clause count)

**Per-domain distribution of the 53 OS rows** (for the coverage skeleton):

| Domain | Count | Clauses |
|---|---|---|
| `spec/map-surface` | 39 | RFC9-1, 3, 4, 5, 6, 7, 8, 8(a), 9, 9(a), 9(b), 13, 13(a), 14, 14(a), 15, 16, 15(b), 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 42, 43, 44, 46, 48, 49, 50, 51 |
| `spec/map-lenses` | 8 | RFC9-10, 11, 12, 28, 31, 32, 33, 34 |
| `spec/map-scenes` | 6 | RFC9-36, 37, 38, 39, 40, 41 |

Three rows additionally name `spec/selection-api` for a secondary limb
(RFC9-3's drawer-fact-set exclusion, RFC9-6's retired-district URL
resolution, RFC9-44's URL survival across refactor); those limbs are
consequences this surface *constrains* but RFC 0006 *owns*, so they are
listed as secondary rather than counted here. **No new spec domain is
proposed** — see the doubts below for the one case that argued for one.

**Notes and doubts:**

Five rows were genuinely contested. Each is recorded with the losing reading
so a reviewer can overturn it on the merits rather than re-derive it.

1. **RFC9-16(d) — CR, argued for OS.** The clause has a real fail-closed
   consequence a user could see: a layout version adopted without its owner
   act or recorded equivalence check should not take effect. But that
   consequence is *stated* by RFC9-18 (absent or invalid registry act ⇒ no version
   established ⇒ scene renders Unknown), which is routed OS. RFC9-16(d)'s own
   text is entirely about who may pull the trigger and what demonstration
   discharges the carve-out — including an explicit disclaimer that the
   demonstration is *not* an RFC2-3 identity test but a distinct
   layout-equivalence harness whose result is recorded. Routing it OS would
   duplicate RFC9-18's scenario and lose the fact that RFC9-47 already carries
   the check ("the carve-out demonstration is actually run"). **Overturn if** a
   reviewer holds that an owner *governance* act is categorically not
   craft-and-care material; the CR bucket as defined covers "process
   obligation," which I read as including it, but the definition names
   craft-and-care and release policy specifically, and a governance act
   belongs to neither.

2. **RFC9-35 — CR, argued for OS, and this is the closest call in the set.**
   A spec scenario could straightforwardly assert "a lens with no effective
   RFC3-16(a) promotion act does not appear in the shared lens
   selector," which is fail-closed behavior of exactly the kind that made
   RFC9-26 an OS row. I routed CR because RFC9-26 *states* a rendering rule in
   its own text ("a channel with no registry entry must not render") whereas
   RFC9-35 states only an increment-completeness obligation plus an
   authorization predicate, and the selectability consequence has to be
   inferred. RFC9-49's own cross-reference treats RFC9-35 as the archetype of
   a same-increment delivery obligation. **Overturn if** the reviewer thinks
   the selector's contents are user-observable enough to demand a scenario;
   the honest consequence of my routing is that nothing in `spec/map-lenses`
   pins lens *availability*.

3. **RFC9-45 — CR, with an OS limb deliberately absorbed elsewhere.** Its
   first paragraph does contain rendering text ("at 90% Unknown the map must
   remain legible and useful: Unknown regions aggregate with RFC2-24 reasons
   and resolution routes rendered verbatim"). I judged that limb wholly
   covered by RFC9-27 (reasons verbatim with routes), RFC9-42 (aggregate
   substitution at LOD), RFC9-43 (aggregate composition) and RFC9-44 (unmapped
   district), all OS, leaving RFC9-45's distinctive content as the
   three-artifact walkthrough gate. If a reviewer disagrees that the coverage
   is total, the correct fix is a `spec/map-surface` requirement for the
   grey-map first impression, not a re-route of this row.

4. **RFC9-8 / RFC9-8(a) — routed `spec/map-surface`, and a new domain was
   considered.** Portfolio arrangement is explicitly *not* a project concern:
   RFC3-21/SDR-29 put it in the workspace manifest, and RFC9-8(a) puts the
   portfolio layout version, its registry, and its reorganisation events
   there too. A `spec/workspace-portfolio` domain would be a defensible mint.
   I did not propose one because the obligations these clauses create are
   still *rendered on the map surface* (placement, legend, unconfirmed/
   asymmetric edges, stale-camera refusal), and the provisional domain list
   already carries no workspace-scoped domain, suggesting the omission is
   deliberate rather than an oversight. Flagged so the decision is visible.

5. **RFC9-2 — the only N/A, and I want it read as a decision.** It is
   normative (later choices may not weaken a clause here), so it is not IR;
   it mandates no check, so it is not CR; and it describes no output, so it is
   not OS. It survives the strictness bar because what it constrains is the
   *contract's own coverage boundary* — authority allocation between this RFC
   and later design/spec material — and no scenario can assert an absence of
   binding. Every other clause I tested for N/A failed the test: RFC9-14's
   determinism, RFC9-18's storage partition, RFC9-36's one-graph invariant and
   RFC9-8's derived-arrangement invariant all *look* like pure model shape but
   each carries a distinct observable consequence (coordinate reproduction,
   Unknown-on-absent-or-invalid-version-act, address transfer across profiles,
   unconfirmed/asymmetric rendering) not covered by any other OS row.

**One methodological caution for whoever consumes this file.** The rev10
matrix classed 50 of these 60 rows `DI` and routed them to "RFC." Re-decided
on the merits, 47 of those 50 are OS. That is not a marginal correction: it
means the previous coverage skeleton would have carried roughly five map
clauses into surface specification where it should have carried fifty-three,
and RFC9-52's coverage matrix built from it would have been substantially
empty while appearing complete. The DI rationale text was nonetheless a good
input — its identification of the retained invariant was usually right, and
most of this file's "retained invariant" column agrees with it.

---

## RFC-0010 — Mission Control and Autonomy Envelopes


**Enumeration method (historical — the run against the pre-split single-file
RFC-0010 module, since split into the `rfcs/RFC-0010/` package):** same
`python3` run, same definition-site regex applied with `re.M`:

```python
defre = re.compile(r'^\*\*(RFC(?:8|10)-\d+)(\([a-z]\))?(?=[\s.—*])', re.M)
```

Contiguity checked by integer set-difference against 1..16: **no gaps, no
extras**. The lettered-mention sweep
(`re.compile(r'RFC(?:8|10)-\d+(?:\([a-z0-9]\))?')`) returned **no** lettered
RFC10 identifiers anywhere in the file — the `(a)`/`(c)` forms present in the
text belong to RFC3-16, RFC4-13, RFC5-18, not to this contract. So there were,
at that run, no lettered sub-clauses to route.

**Clauses found by that historical run:** 16 — RFC10-1 through RFC10-16. The
contract has since grown past that enumeration (the budget-reservation and
effects-recovery clauses below postdate it, some with lettered sub-clauses);
the rows are the current population, and that population is recomputed —
declared identities against routed rows — by CG-17 on every battery run, never
carried in this note. *Re-run 2026-08-10 against the `rfcs/RFC-0010/` package:
the same definition-site sweep returns a contiguous clause range with no gaps
and no extras.*

| Clause | Route | Future spec domain | Retained invariant in the RFC | Justification |
|---|---|---|---|---|
| RFC10-1 | OS | `spec/mission-control` | Mission Control mints no project truth; no artifact, cache, or store becomes a second project-internal source of truth | A scenario must assert that every Mission Control view of project state is served as a projection of kernel answers carrying the kernel's evaluation identity, that no Mission Control record is independently queryable as project truth, and that the projection is rebuildable — discard it and the answers are identical. Violation case 3 (a drifting MC copy of requirement states consulted as truth) is directly testable. |
| RFC10-2 | OS | `spec/platform-service` (mission-data limb: `spec/mission-control`) | The topology binds — one canonical service, one semantic API, all other things are clients — while language, packaging, transport, and binary count stay open | A parity scenario: for one query at one evaluation, the web UI, the `syzygy` CLI, a script, and an agent-protocol adapter receive the same identities, evaluations, evidence, missions, attention items, and policy results with RFC6-14 label parity. The negative is equally testable: every datum a human sees is available in a machine answer, so an integration never has cause to scrape rendered HTML (violation case 7). Routed to the proposed `spec/platform-service` domain because this limb binds *all* surfaces' clients, not Mission Control's. |
| RFC10-3 | OS | `spec/platform-service` (mission-affecting scopes: `spec/mission-control`) | RFC5-3's two client classes are exhaustive — there is no third; a machine credential can never produce an owner act | Assertable authorization behavior: machine clients are admitted only under RFC5-5 with RFC5-6-shaped credentials, deny-by-default; a read scope never implies approve, pause, cancel, or envelope-change; and a machine client holding a mission-affecting scope produces a **submission awaiting owner attendance**, with the mission state unchanged until the owner act — the scenario asserts the act did not occur, not merely that a request was logged. |
| RFC10-4 | OS | `spec/mission-control` | Pinned inputs are immutable for the mission's life; a pinned-input change never silently retargets a running mission | Two spec obligations. First the required-field list — objective and rationale, target, exact pinned inputs by digest or revision identity, initiating owner act, parent mission, lifecycle state, terminal outcome — which must become requirements rather than be read off this prose (a mission record missing any is not a mission). Second the escalation scenario: change a pinned doctrine, contract, spec, policy, or evaluation revision under a running mission and an escalation is raised whose choices include re-approval against the new inputs, while the mission keeps running against its pinned set. |
| RFC10-5 | OS | `spec/mission-control` | Every terminal state is recorded with its reason; `expired` and `cancelled` are always reachable by human act; no transition widens the envelope; exit from RFC10-8/10-11 `blocked` is a human resolution act | The clause **self-routes**: the lifecycle vocabulary is explicitly provisional and "freezing happens by OpenSpec requirement, not by this clause", after review against RFC 0008's normalized work states. A spelled-out state machine with a transition diagram is prime leakage material, so the spec must own the frozen vocabulary and every transition, and must assert the negative that an agent's "condition cleared" assertion never takes the unblock transition. |
| RFC10-6 | OS | `spec/mission-control` | A mission is authority to proceed *inside* the gates, never authority to skip one; work is never proof | Scenarios: a mission's completion predicate evaluates against evidence at a declared minimum RFC2-25 tier and **"all work items closed" never satisfies it** (violation case 5); an unstated minimum tier resolves to the strongest applicable tier; the completion render discloses the tier actually achieved; and consent (RFC5-12), egress (RFC5-14), and execution-profile (RFC5-18) gates each still fire for a mission-authorized act. |
| RFC10-7 | OS | `spec/mission-control` | An unstated envelope field is the narrowest reading, never the widest; ambiguity resolves narrow and load-bearing ambiguity escalates; the propose-only cap until autonomy levels are enumerated by owner act | The fourteen-category minimum content list is a required-field list an implementer could build from directly, so the spec must own it. Sharp scenarios: an envelope with no budget grants **zero** delegated spend of that kind; no path grant means no write access; an envelope naming a level above propose-only has that level **not take effect** while the vocabulary is unenumerated; and a genuinely ambiguous load-bearing bound raises an Attention Item rather than being resolved by the running agent. |
| RFC10-8 | OS | `spec/mission-control` | No self-widening, in any of the enumerated forms; widening is exclusively a human act with RFC3-16(a) provenance; child missions are reservations, not copies | The safety-critical clause and the most scenario-dense. A spec must assert: an agent-proposed widening renders as an Attention Item and has **no effect** before the act; a child mission is mintable only under an explicit decomposition grant (absent grant ⇒ no children); a child's provenance is the parent act plus a recorded derivation, never a self-minted act; each child grant is **debited from the parent's remaining envelope at grant time** so siblings can never jointly exceed the one authorized budget; and an attempted self-widening transitions the mission to `blocked`, records the attempt as evidence, and mints an Attention Item. |
| RFC10-9 | OS | `spec/mission-control` | Mission approval, the envelope, and every envelope amendment require an effective human owner act that is current, attributable, scope-matched, and bound to the exact artifact digest; state (1) and state (2) are both effective and the exact state is always rendered; a machine-submitted record is not an act | Directly assertable state behavior: a mission with a valid state-(1) or state-(2) approval may leave `awaiting-approval` only when every other independent gate passes, with the exact provenance state visible. An absent, invalid, stale, revoked, superseded, wrong-scope, digest-mismatched, or machine-submitted record authorizes nothing and leaves the mission awaiting approval. A failed, unavailable, or indeterminate A1 attempt never creates state (1) or downgrades state (2). The act is a warrant, never evidence that mission effects or completion succeeded. |
| RFC10-10 | OS | `spec/mission-control` | The two enforcement planes are never conflated; the MUST is scoped honestly to Syzygy's own choke points, never to an outward enforcement claim | A scenario must assert that an out-of-envelope Syzygy-mediated act is **refused at the choke point** with no effect performed — performed-then-flagged is the failure — and that every guardrail decision (allow, refuse, halt) is recorded as identified evidence attributable to its mission, work item, and principal. The scope honesty is also assertable: acts taken with externally-granted credentials outside Syzygy's mediation render as *visible*, never as prevented. |
| RFC10-11 | OS | `spec/mission-control` | Bound exhaustion never self-extends, borrows, or downgrades the gate set | Scenarios: reaching any budget, time, retry, or risk-floor bound halts further materialization and execution under that mission and transitions to `paused` or `blocked` with an Attention Item; the bound is not raised by any amount (violation case 2's "helpful" 10% extension is the canonical failure); no other mission's budget is drawn on; and already-lawfully-dispatched work completes or checkpoints per the envelope's recovery obligations. |
| RFC10-12 | OS | `spec/mission-control` | An expiry default must be safe — expiry may narrow, pause, or block and may never widen an envelope or approve anything; one authorizing act resolves one item | The required packet-field list (what happened, why attention is needed, affected mission/work/project, evidence with its Unknowns rendered as Unknowns, available choices, consequence of each, default and expiry, what is blocked, reversibility, resolution act and provenance) must become requirements — a packet missing a field is not decision-ready. Two negative scenarios: an expiry that approves a pending deploy is a violation (case 4); a bulk act over unenumerated items **resolves nothing**. |
| RFC10-13 | OS | `spec/mission-control` | Compression into decision-ready packets is the obligation — streaming every run event is a violation, not a conservative default; items never silently disappear | Assertable queue behavior: every Attention Item terminates in a recorded resolution, an expiry-to-safe-default, or an explicit human dismissal, each attributable and queryable afterwards (no item is ever garbage-collected unresolved); and each of the six minimum escalation triggers fires — bound approach/exhaustion, risk over the delegated threshold, a protected or human-only surface in the proposed path, an unresolved contradiction or genuine product choice, evidence unable to establish progress, unsafe recovery. |
| RFC10-14 | OS | `spec/mission-control` | The mission home is never a parallel truth store; the in-tree envelope file plus any stamp is never itself the approval | The routed behavior is the approval write and its digest binding: approving a mission appends an act record to `.syzygy/governance/decisions/` binding the envelope's **exact digest** (RFC3-16(b) item 3), so a scenario can assert that an envelope edited after approval is no longer covered by it and its mission may not run — a stale-digest test with a real security consequence. The mission-artifact home under `.syzygy/work/missions/<mission-id>/` with typed, provenance-labeled entries is the weaker limb (see doubts). |
| RFC10-15 | OS | `spec/mission-control` | The workspace store's writ ends at scheduling, budget, and attention policy; where the writ meets the prohibition, **the prohibition wins**; minting the store requires a recorded owner widening | The prohibition is testable at its sharpest edge: a workspace-store entry that would set a project's requirement priority is refused rather than applied (violation case 6), and pausing a project means **Syzygy refuses to schedule against it and never mutates project-internal state or status** — a scenario asserting the project's own answers are byte-identical before and after the pause. The store's home and schema are deferred (§8 q3), so the spec pins behavior, not layout. |
| RFC10-16 | CR | — (routes to craft-and-care / release policy) | The whole clause: this contract schedules nothing, and the coverage matrix is review material, never authority | Same shape as RFC8-32 and routed identically: a process and release-gate obligation, not observable behavior and not model shape. It forbids scheduling any user-observable Mission Control implementation work from this RFC alone — naming mission creation/approval flows, lifecycle displays, envelope editing, attention-queue rendering, CLI commands, API endpoints and their answers, and MCP-or-equivalent tools — and requires a clause-to-requirement coverage matrix over every clause of this contract other than this one at surface specification. Specifying a phase rule as a requirement of the phase it gates would be circular. |

**Tally:** OS 15 · N/A 0 · CR 1 · IR 0 · total 16 (sums: yes — 15 + 0 + 1 + 0 = 16)

**Notes and doubts:**

- **New domain proposed: `spec/platform-service`.** RFC10-2's service-and-client
  topology with human/machine parity, and RFC10-3's client-class exhaustiveness
  and credential-scope admission, bind **every** surface's clients — Polaris,
  Trajectory and Orrery inherit them, and RFC 0005 is their origin. Filing them
  under `spec/mission-control` would make three surfaces' client contract a
  child of the operator domain, and none of the eight minted domains covers the
  platform service. The mission-specific limbs (mission and attention data
  parity; mission-affecting scopes as distinct entries) stay in
  `spec/mission-control`. If the owner prefers a smaller domain set, the
  fallback is to route both wholly to `spec/mission-control` and accept that
  later surfaces will re-cite them.
- **RFC10-14 — closest N/A call in this contract.** Its home-discipline limb
  (mission artifacts under `.syzygy/work/missions/<mission-id>/`, typed and
  provenance-labeled per RFC 0003) is close to pure layout, and layout alone
  would be N/A. The row is OS on the second limb: the approval act record lives
  in `.syzygy/governance/decisions/` and binds the envelope's exact digest, so
  an envelope edited after approval falls outside its act — a distinct,
  security-bearing scenario that RFC10-9 (which governs owner-act
  effectiveness and provenance-state disclosure, not digest coverage) does
  not assert. Flagged.
- **RFC10-1 — second closest.** "Not a fourth truth surface" reads as pure
  architecture, and it does overlap RFC10-2's parity rule. It is OS on the
  cache-drift scenario: an MC-held view must never be independently answerable,
  and answers must carry the kernel evaluation identity. A reviewer could hold
  this subsumed by RFC10-2. Flagged.
- **RFC10-16 — CR versus N/A**, for the same reason recorded for RFC8-32; CR
  chosen because the clause imposes a positive deliverable and review
  obligation on the surface-specification phase. Flagged.
- **Leakage-class clauses here.** RFC10-5 (lifecycle vocabulary and transition
  diagram), RFC10-4, RFC10-7, and RFC10-12 (three required-field lists, one of
  them fourteen categories long) are RFC 0010's buildable-from-prose risk.
  RFC10-5 is the least dangerous only because the clause itself declares the
  vocabulary provisional and hands freezing to OpenSpec; the three field lists
  carry no such self-limit and their spec entries must own the fields
  outright.
- **Operational caveat carried from §2, not a routing decision.** Owner ruling
  `BOUNDED-MISSION-DOCTRINE-INTERPRETATION-2026-08-31` satisfies RFC10-24's
  doctrine alternative. It does not accept RFC 0010, sign its required
  OpenSpec behavior, approve a mission, or discharge RFC10-16 or any
  effect-specific gate. Every OS row above remains a candidate specification
  obligation, never a licence to build or operate.
- **Zero N/A here as well**, and for the same reason as RFC 0008: RFC 0010's
  clauses are almost entirely about what an operator or a machine client may
  do and see. Its most structural-looking clauses (RFC10-1, RFC10-14, RFC10-15)
  each carry a refusal or a state-transition consequence that a scenario can
  assert.

---


### rev11 addition — the correction plane (RFC10-17..22)

These six clauses postdate the routing pass above; they are routed here, by
the same rule. All six are `OS`: every one of them describes something a
person or an agent can observe happening (or failing to happen) at runtime,
which is the definition of a specifiable behavior.

| Clause | Route | Future spec domain | Retained invariant in the RFC | Justification |
|---|---|---|---|---|
| RFC10-17 | OS | `spec/mission-control` | Five-quantity accounting; reserved + spent never exceeds authorized | A scenario must assert that dispatch is **refused** when the work's declared maximum cost cannot be reserved, and that Unknown measured spend halts the mission rather than reading as zero |
| RFC10-18 | OS | `spec/mission-control` | The executor may report completion and may never establish it | A scenario must assert that `running → completed` is refused when the only establisher is the executing principal or one it routed, and that an unstated minimum tier resolves to `gate-backed` |
| RFC10-19 | OS | `spec/mission-control` | An unclassified effect class is unauthorized; pause is not rollback | A scenario must assert that a mission terminating with applied effects emits each compensating action's outcome as evidence and one Attention Item enumerating what cannot be undone |
| RFC10-20 | OS | `spec/mission-control` | Stop terminates Syzygy-launched runs and their descendants | A scenario must assert that after a stop act no run Syzygy launched is still executing — within the declared maximum latency, or synchronously where none is declared |
| RFC10-21 | OS | `spec/mission-control` | Every embedded project's consent binds at the RFC5-15 choke point | A scenario must assert that a composite spanning projects A and B **fails closed** when either project's (project, provider) consent is absent, and that the refusal renders |
| RFC10-22 | OS | `spec/mission-control` | Undeclared attention maximum means one outstanding item | A scenario must assert that reaching the outstanding-count or item-rate bound **pauses the mission** instead of enqueueing, and that same-decision items deduplicate with recorded multiplicity |

**Tally:** OS 6 · N/A 0 · CR 0 · IR 0 · total 6 (sums: yes)

### rev11b addition — three sub-clauses

Added 2026-08-06 by the correction plane's second repair pass, each living
with its parent clause and routed on its own terms. All three are `OS`: each
names something that either happens or fails to happen at runtime, and each
one exists because a reviewer constructed the scenario in which it did not.

| Clause | Route | Future spec domain | Retained invariant in the RFC | Justification |
|---|---|---|---|---|
| RFC10-17(a) | OS | `spec/mission-control` | Every reservation has a stated release point; no non-terminal park holds one indefinitely | A scenario must assert that a mission parked in `blocked` releases its reservation at the transition to `expired` and not before, and that an unterminated run's reservation is **retained and named** rather than returned |
| RFC10-18(a) | OS | `spec/mission-control` | The effects-applied determination has an independent evaluator, a `gate-backed` floor, and a fail-closed Unknown rule | A scenario must assert that an executing principal's report of "no effects applied" does **not** route the mission to `blocked`, and that an Unknown determination routes it to `failed` with the Attention Item saying the disposition rests on an unresolved determination |
| RFC10-19(a) | OS | `spec/mission-control` | Sibling disposition on partial failure is a declared policy input; unstated is the strictest reading | A scenario must assert that an envelope declaring no sibling disposition does **not** default to `independent` — completed siblings' effects are dispositioned, or the mission escalates before further dispatch |

**Tally:** OS 3 · N/A 0 · CR 0 · IR 0 · total 3 (sums: yes)


---

## RFC-0011 — Context Compiler and Governed Context Packets


**Enumeration method (historical — the run against the pre-split single-file
RFC-0011 module, since split into the `rfcs/RFC-0011/` package):** the same
corrected Python `re` pattern, adapted to the namespace:

```python
import re
pat = re.compile(r'RFC11-\d+(?:\([a-z]\))?(?![\w(])')
ids = set(pat.findall(open('RFC-0011-context-compiler.md').read()))
```

Confirmed by a second method: a sweep for bold clause declarations
`\*\*(RFC11-\d+(?:\([a-z]\))?)\.` returns the identical twelve identities, so
every clause in the file was declared and no identity appeared only in
cross-reference. **No lettered sub-clauses existed in RFC-0011 at that run** —
the front matter declared `RFC11-1..RFC11-12` with no sub-clause list, and the
sub-clause branch of the regex matched nothing.

**Clauses found by that historical run:** 12 — RFC11-1 through RFC11-12. The
contract has since grown past that enumeration; the rows are the current
population, and that population is recomputed by CG-17 on every battery run,
never carried in this note. *Re-run 2026-08-10 against the `rfcs/RFC-0011/`
package: the mention sweep and the bold-declaration sweep return identical
identity sets.*

| Clause | Route | Future spec domain | Retained invariant in the RFC | Justification |
|---|---|---|---|---|
| RFC11-1 | OS | `spec/context-packets` | The packet's minimum content set and its immutability; and the load-bearing negative — a packet **reports** the envelope and permissions it was compiled under and is never itself an authorization source; whoever mints packets grants nothing | A spec must pin packet minting and inspection: every enumerated field present (objective, project/workspace, evaluation and as-of instant, doctrine rules by identifier, clause IDs at stated revision/digest, policies, warrant and envelope, evidence references, active decisions/contradictions/challenges/Unknowns, allowed tools, compiler and adapter versions, omitted candidates each with a reason, final digest) — and the enforcement scenario that a packet asserting a permission the envelope does not carry authorizes nothing, because the choke point re-derives from the envelope and its act provenance. |
| RFC11-2 | OS | `spec/context-packets` (record leg: `spec/work-surface`) | An execution record for a compiled run without its packet digest is **incomplete evidence**; packets are never edited in place | Two scenarios: the resulting execution record carries the packet digest and is marked incomplete without it; and amending context mid-run mints a new packet version with its own digest linked to its predecessor, with the record binding **every** version the run consumed, not only the last. |
| RFC11-3 | OS | `spec/context-packets` | For any run under a mission, work warrant or review charter a packet is **required**; the absence is a violation, not a fallback; un-governed human exploration is outside the clause until its output feeds a governed act | Directly testable at dispatch: a governed run dispatched with no packet is refused, and an instruction of the form "read all project documentation" is rejected rather than treated as a safe default — and the boundary scenario, where an interactive exploration's output enters a governed act, requires a packet at that moment. |
| RFC11-4 | OS | `spec/context-packets` | Determinism (same inputs, same selection) over the enumerated minimum sources; the selection rule set is versioned with the compiler; the mandatory set always includes the **governing phase-rule clause of every selected contract** | A spec must pin three assertions: two compilations from identical inputs produce the identical mandatory set; no lawful packet omits the boundary rule of a contract it loads; and before selecting from any generated projection the compiler verifies the projection regenerates faithfully and **records that verification in the packet** — selection from a stale or unfaithful projection failing rather than proceeding. |
| RFC11-5 | OS | `spec/context-packets` | Inference may add with provenance; it may never suppress, demote or replace mandatory deterministic context; a packet distinguishes its mandatory core from its suggested additions | Violation case 2 is the scenario: a retrieval layer that ranks a mandatory doctrine rule below its cutoff must not be able to produce a packet that shows no omission — suggested additions are marked as suggested and by what, and the mandatory core is separable in the packet's own structure. |
| RFC11-6 | OS | `spec/context-packets` | Incomplete is Unknown and Unknown blocks when policy says complete; the fail-closed posture of RFC5-14/16 and SEC-5 applies; staleness and contradiction are disclosed inside the packet even where a relaxation permits proceeding | A spec must pin the launch decision: undeterminable, internally contradictory, stale, or Unknown required context marks the packet incomplete **with the gap named**, and by default the run does not launch but escalates through RFC10-12 — with proceeding lawful only under an explicit owner-visible relaxation in the governing policy or envelope, never an unstated default. |
| RFC11-7 | OS | `spec/context-packets` | No second truth store: selection metadata is present in, or deterministically derived from, the active governed artifacts; a hand-maintained sidecar that can drift is a violation | Distinct from RFC11-4, which checks that a *generated* projection still regenerates: this clause makes a non-regenerable metadata source inadmissible as a selection input at all — a hand-maintained sidecar has nothing to regenerate from and would slip past RFC11-4's check entirely, so a scenario must assert that a selection input which cannot be derived from the governed artifacts is rejected rather than trusted. |
| RFC11-8 | OS | `spec/context-packets` | Raw prompts, private chain-of-thought and transcripts are never canonical memory and never mandatory context; promotion is an explicit attributable act, propose-only until §8 q3 is ruled; an authorization-bearing memory artifact without owner-act provenance binds nothing | A spec must pin that no compiled packet's mandatory set contains raw transcript material, that a machine principal's promotion proposal does not become governed memory without a human act, and that a memory artifact which *interprets* an envelope, gate or prohibited surface never enters mandatory context as an interpretation absent RFC3-16(a) provenance. |
| RFC11-9 | OS | `spec/context-packets` | Governed memory lives in governed homes; a packet is **not a consent loophole**; canonical memory follows its home's lifecycle, never silent deletion | Three testable boundaries: secret material never enters a packet or memory (SEC-5, RFC5-16/17); packet content crossing an egress boundary passes the RFC5-14/15 consent gate — violation case 6, code sent under a metadata-only consent, is the fixture; and deletion of canonical memory follows a recorded lifecycle while retention of non-canonical raw material follows a declared policy. |
| RFC11-10 | OS | `spec/mission-control` (fail-closed gate leg: `spec/context-packets`) | The profile is optional and minimal, versioned; **no current model or provider name is hard-coded as permanent semantics** — names are data in profile instances; a profile can narrow, never widen an envelope | A spec must pin routing behavior: violation case 7 — a review routed to an agent lacking the independence property its class requires because fallback order ignored it — and the fail-closed rule that a profile field satisfying an envelope-required gate (independence, permissions, risk classes) counts only when backed by owner-act provenance or identified evidence, a self-asserted field leaving the gate unsatisfied. |
| RFC11-11 | OS | `spec/context-packets` | Exceeding the budget posture is a disclosed, reasoned, owner-visible event, never silent; budget pressure never justifies dropping mandatory context — the lawful responses are sharding, narrowing the objective, or escalating; the numeric target is a policy default and must not be frozen into contract text | A spec must pin that every packet carries a size estimate, that an over-posture packet renders its reasoned exception rather than trimming, and — the sharpest scenario — that **every shard carries the non-shardable core in full**: the envelope, the prohibited and human-only surfaces, the applicable doctrine rules, and the governing phase rules; a shard missing any of these is not a lawful packet. |
| RFC11-12 | CR | — (phase gate; feeds the coverage matrix this file serves) | This contract schedules nothing; the coverage matrix over every clause of this contract other than this one, produced at surface specification, is review material, never authority; no OpenSpec content may exist during bootstrap | A process obligation on how implementation work may be scheduled and on a surface-specification deliverable — it constrains the governance process rather than any packet, compiler or view behavior, and a requirement derived from it would be circular. |

**Tally:** OS 11 · N/A 0 · CR 1 · IR 0 · total 12 (11 + 0 + 1 + 0 = 12 — sums: **yes**)

**Notes and doubts (RFC-0011):**

1. **Zero N/A is a finding, not an oversight.** I looked hardest at RFC11-7,
   which reads like a pure architectural constraint. It survives as OS on one
   residue: RFC11-4's faithfulness check only reaches projections that *claim*
   to be generated, so the prohibition on a non-derivable selection source is
   independently failable. If a reviewer folds that into RFC11-4's scenario set,
   RFC11-7 becomes the contract's single N/A and the tally moves to OS 10 /
   N/A 1.
2. **RFC11-1 is a required-field list (RC-5's leak L7)** and is the clause most
   likely to be built from directly without a spec. Routing it OS is the
   mitigation the phase rule exists to force; the retained invariant is the
   minimum set plus the reports-never-authorizes rule, not a wire schema.
3. **RFC11-10's domain is a judgment call.** Profiles are consumed by work
   routing (mission-control) but their fail-closed gate-satisfaction rule is a
   packet-compilation concern. I named `spec/mission-control` primary to match
   the rev10 skeleton's placement of the profile registry, with the gate leg
   named explicitly rather than left in prose — rev10's practice of naming the
   domain only inside the rationale column was a finding against it (RC-5 §5).
4. **RFC11-2 and RFC11-9 both reach outside `spec/context-packets`** — into the
   execution record (`spec/work-surface`, RFC8-18..20) and into the egress
   consent ceremony respectively. Neither needs a new domain; both need their
   leg named so the coverage matrix does not lose it at the seam.
5. **No new spec domain is proposed for either contract.** The provisional
   eight cover every routed limb in both RFCs.
6. **Both phase rules (RFC7-38, RFC11-12) are routed CR, not N/A.** They are
   not structural invariants of a model — they are gates on the specification
   process, which is precisely what the CR class names. Routing them N/A would
   have implied "no requirement needed" for a clause whose entire function is to
   demand that requirements be written.

---

## round-2026-08d addition — structural-closure clauses (RFC7-39/40, RFC10-23/24, RFC11-13..16)

Eight clauses postdate the routing passes above, added by the owner-ordered
structural closure round; they are routed here, by the same rule and the
same route vocabulary. Two package facts changed alongside them and are
recorded so the enumeration prose above is read as the historical method
statement it is: RFC-0010 and RFC-0011 are now **packages**
(`rfcs/RFC-0010/`, five modules; `rfcs/RFC-0011/`, two modules — the
single files the earlier enumeration commands name live on only in git
history), and **every** active contract now carries a binding phase rule
(RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27 joined the six the header
names; the five kernel-side rules sit outside this matrix's surface
population and are validated by `verify_final_prespec.py`).

| Clause | Route | Future spec domain | Retained invariant in the RFC | Justification |
|---|---|---|---|---|
| RFC7-39 | OS | `spec/intent-surface` | `.syzygy/intent/OVERVIEW.md` is the fixed, Syzygy-owned human entry point, rendered as governed presentation and **never authority**; a governed project without the file renders the absence, never silently | A scenario must assert that the entry resolves at the fixed path and renders under the narrative rules with its never-authority posture, and that a governed project missing the file surfaces the gap as a finding (absent) or Unknown (unobservable) rather than rendering nothing |
| RFC7-40 | OS | `spec/intent-surface` | The repository-front-door link to the project entry is a per-repository kernel finding whose **answer domain is closed at four values — `yes` / `no` / `not-applicable` / `Unknown`** — carried verbatim on every rendering and machine answer (RFC6-14); Syzygy **may propose** the link and **may never write it** (VIS-5) | A scenario must assert the four-valued finding renders per repository — including that a repository with no governance root renders `not-applicable`, never `no` — that a declined link renders `no` truthfully and not as an error, and that the only write path Syzygy offers is a Proposal (RFC1-27) — no conforming implementation touches the front door itself |
| RFC10-23 | OS | `spec/mission-control` | Effect dimensions — project mutation, external-system mutation, external disclosure, resource consumption — are recorded separately; no single predicate collapses them, and `propose-only` is **never rendered as "no effects"** where dimensions (i), (iii) or (iv) are non-empty | A scenario must assert that a mission's terminal record states all four dimensions, that the effects-applied predicate (RFC10-18(a)) engages on dimension (ii) alone, and that a propose-only mission which disclosed content and spent budget renders *which* effects it had, under which authorization — never a bare "no effects" |
| RFC10-24 | OS | `spec/mission-control` | Owner ruling `BOUNDED-MISSION-DOCTRINE-INTERPRETATION-2026-08-31` satisfies the clause's doctrine alternative without amending doctrine; it does not accept RFC 0010, sign OpenSpec behavior, approve or start a mission, or discharge RFC10-16 or any other gate | A scenario must assert that while RFC 0010 remains candidate, no mission operates or leaves `awaiting-approval`; after acceptance, transition remains blocked until the required OpenSpec behavior is signed, RFC10-16 is satisfied, the exact mission and envelope carry effective state-(1) or state-(2) owner acts with their exact states rendered, and every other independent gate passes. Satisfaction of the doctrine alternative alone changes none of those results. |
| RFC11-13 | OS | `spec/context-packets` | Every active contract declares its implementation boundary in its own index front matter — `{kind, clause}` — and the declaration is consumed, never re-derived, inferred, or overridden by a selector | A scenario must assert that a contract with no declaration, or whose named clause does not exist, renders every packet selecting it **incomplete (RFC11-6)** rather than silently complete, and that a selector never searches for a clause class the contract does not claim to have |
| RFC11-14 | OS | `spec/context-packets` | Dependency traversal is defined, bounded, and recorded: direct `depends_on` only (no silent transitivity), an edge satisfied by loading at least one module of the depended-on contract, unsatisfied edges enumerated clause-by-clause in the omission register, undecidable applicability failing closed | A scenario must assert that a packet leaving a `depends_on` edge unsatisfied enumerates and disposes of every cited clause individually, that `cites` is never traversed automatically, and that a task whose applicability cannot be decided from declared metadata produces an incomplete packet — never a silently thinned one |
| RFC11-15 | OS | `spec/context-packets` | Doctrine and craft rule ownership is declared metadata (owning artifact, task classes, risk classes), rebuildable and clone-visible; where none is declared, doctrine/craft selection is **not claimed deterministic** and the packet states its actual basis | A scenario must assert that a task class with declared ownership metadata selects deterministically from it, and that one without renders the judgment basis in the packet rather than implying a derivation that did not happen |
| RFC11-16 | OS | `spec/context-packets` | `constrains` is consumed clause-first: the constraining **clause** enters the mandatory set, not automatically the whole constraining contract, and the packet records why each constraint entered | A scenario must assert that a task touching a declared seam loads the constraining clause with its recorded reason, and that the constraining contract's remaining modules do not ride in on the edge |

**Tally:** OS 8 · N/A 0 · CR 0 · IR 0 · total 8 (sums: yes)

**Notes and doubts (round-2026-08d):**

1. **RFC10-24 could be argued CR** — it gates a ceremony, like the phase
   rules. It is routed OS because its consequence is a runtime refusal a
   scenario can drive (an approval act attempted and refused, a lifecycle
   transition that never fires), where the CR clauses constrain only how
   specifications come to exist. A reviewer moving it to CR changes the
   tally to OS 7 / CR 1 and must then say where the refusal scenario lives.
2. **RFC11-13..16 unbundle RFC11-4's old universal.** Their scenarios
   overlap RFC11-4's row above; at surface specification the coverage
   matrix must de-duplicate against it rather than double-count.
