# RD-60 — Capability 1 outline exercise, against the generated route

> **Provenance banner, added by the recording session — everything below the
> rule is the agent's raw output, copied verbatim and unedited.**
>
> | | |
> |---|---|
> | **Role** | owner charter §10's outline exercise, run against the **generated** route rather than a hand-maintained one. **Not a review**: no artifact was judged and no verdict word is claimed |
> | **Dispatched** | 2026-08-13 |
> | **Materials given** | the `Author Capability 1` section of `TASK-ROUTER.md`; `CAPABILITY-1-CHARTER.yaml`; `CAPABILITY-1-GENERATED-VIEWS.md`; and the contract modules those name, opened only to read clauses it cites |
> | **Subject digest at dispatch** | charter `15e92acbd5a62c3f28ff507abc59fd07fb7657ceb19978c3c4921fede64ad107` — the one digest recorded at dispatch, and independently attested by the provenance comment inside `CAPABILITY-1-CHARTER.yaml` itself. **The views' and router's digests at dispatch were not recorded**, and cannot now be recomputed because both were regenerated from the amended charter: `[Unknown]`, stated rather than reconstructed. Both are wholly generated from the charter, so the charter digest identifies the inputs; it does not attest the generator's revision |
> | **Withheld** | reviews, disposition registers, `PROJECT-STATUS.md`, README, semantic deltas, `FIRST-OPENSPEC-SEQUENCE.md`, every `round-2026-08*` tree, and the pending-decisions queue |
> | **Rulings available** | **none** — every owner decision in its materials is open, and no spec-quality policy is in force |
> | **Context** | fresh |
> | **Model family** | same family as the corpus authors |
> | **Created or edited** | nothing. Its confirmation section enumerates every file it opened |
>
> **The charter has moved since.** Three clauses — `RFC6-22`, `RFC1-27`,
> `RFC3-3` — were added *because of this exercise*, so the charter digest
> above is the pre-addition one and is the digest this document is bound to.
> The exercise found them by trying to write requirements and running out of
> authority, which is what the exercise is for.
>
> **Nothing here is a specification, and nothing here authorizes authoring
> one.** `openspec/` does not exist and was not created.

---

# Capability 1 — fresh-context outline

## The capability in one sentence

Capability 1 registers a project from its declaration and then answers, per facet and per repository, what is actually known about that project's shape — each answer carrying its own epistemic label, its Unknown reason where it has one, and the authority that gave it, identically to a human reader and to a machine client.

---

## Shape versus behaviour

### SHAPE — fixed by the governing clauses; a specification may not re-decide these

| # | What is already fixed | Clause |
|---|---|---|
| S1 | A Project has **exactly one** designated governance root; two roots is a well-formed contradiction minted in the Project's own evaluation, zero roots is *unevaluable* and surfaces at the workspace/manifest level as Unknown (`missing-declaration`) with **no kernel contradiction minted** | `RFC1-1`, restated-by-citation in `RFC3-4` |
| S2 | The declaration's **location is its designation** — `.syzygy/project.yaml`, in exactly one repository; a field value may never designate a root | `RFC3-4` |
| S3 | The declaration's top-level field set is **closed** at the eight fields of `RFC3-5`'s table, each with a single named write authority; additions require amending RFC 0003 | `RFC3-5` (and the four authority classes it draws on) |
| S4 | Manifests are semantic contracts; the file name and location are already fixed, and nothing else in RFC 0003 names a format, storage engine, or wire encoding | `RFC3-1` |
| S5 | Repository identity is the **declared opaque identifier**, never a URL, path, or branch; locator hints may change without touching identity | `RFC3-6` (citing `RFC1-2`) |
| S6 | Observed repositories are read-only; every observed repository requires a recorded consent record, and no consent yields **Unknown, never an empty graph read as absence** | `RFC1-3` |
| S7 | Role and membership are answered by the declaration; content by the version-control authority — "two questions, two authorities; no kernel construct may merge them into one answer" | `RFC1-4` |
| S8 | Consent records are governance acts in `.syzygy/governance/decisions/`, **referenced, never embedded**; two kinds, scoped *(Project, repository)* and *(Project, provider)*, one egress record per provider pair naming the permitted **set** of content classes | `RFC3-7` |
| S9 | A consent record's attribution is a stored field and therefore a *claim*, "honored only under RFC3-16(a)" | `RFC3-7`, `RFC3-16(a)` |
| S10 | An unresolvable consent reference ⇒ **not observed** ⇒ Unknown with reason **#6 `unconsented-source-or-provider`** | `RFC3-6`, `RFC2-24 #6` |
| S11 | Unconsented content renders as a **standing policy state with its resolution route**, "never as a failure, a broken link, or an empty region"; the consented remainder renders normally | `RFC6-26` |
| S12 | Syzygy **never auto-repairs** an invalid declaration — repair is a Proposal through the owner gate; an unparseable or invalid `project.yaml` renders **every dependent claim Unknown** | `RFC3-9` |
| S13 | Drafted declaration content renders **unadopted** and binds nothing until owner sign-off | `RFC3-9` (VIS-4) |
| S14 | The Unknown-reason vocabulary is **closed at twelve**, primary + secondary drawn from the same twelve; a condition outside it is disclosed as a named fact of the render, never dressed as a reason | `RFC2-24` |
| S15 | The human entry point is the fixed path `.syzygy/intent/OVERVIEW.md`, is **governed presentation and never authority**, and its absence renders as a finding under RFC 0002's vocabulary, "never silently" | `RFC7-39` |
| S16 | Every distinction is carried as a **machine-readable attribute on the rendered unit**, served identically through the endpoints and preserved in plain-text/exported renderings; `non-citable`/`presentation-artifact` travels on **every** rendering | `RFC7-33` |
| S17 | Endpoints answer from **the same kernel-computed fact set** the surfaces render — no endpoint-only facts, no UI-only facts | `RFC6-13` |
| S18 | Labels travel **verbatim** from the RFC 0002 vocabulary (label, tier, Unknown reason, freshness), secondary annotations travel marked as secondary, and **an aggregate carries no epistemic state of its own** | `RFC6-14` |
| S19 | Every answer names its evaluation identity (source snapshot + as-of instant); "an answer that cannot name its evaluation is not an answer" | `RFC6-15` |
| S20 | Any aggregate discloses membership count and the **full RFC6-22 equivalence tuple**, with per-Unknown-reason counts computed over **primary reasons only**, and supports expansion to members | `RFC6-17` |
| S21 | For one *(selection reference, evaluation identity, scenario context)* the kernel computes **one fact set**; two surfaces differing on which facts exist is "a kernel defect, not a UI inconsistency" | `RFC6-18` |
| S22 | The fact set's content classes are enumerated (identity/plane, epistemic state, evidence, provenance incl. the **governing normative revision**, warrant, challenge and contradiction state, policy visibility incl. consent and the coverage boundary, work and reconciliation state) — and **an uncomputed reconciliation renders Unknown, never green** | `RFC6-19`, classes 1–8 |
| S23 | Cost renders as **independent measures, never a composite**; "no synthetic 'effort' number may be computed, rendered, or served" — the independence rule is explicitly not amendable in place | `RFC8-18` |
| S24 | **Absent means Unknown, never zero**; every aggregate over partially-known measures discloses coverage and never renders as a complete total | `RFC8-19` |
| S25 | The discoverability finding is **per repository, at the producing evaluation**, its answer domain **closed at four values** `yes / no / not-applicable / Unknown` carried verbatim; `not-applicable` is of this finding's own domain and is never counted among RFC2-24 Unknown reasons | `RFC7-40` |
| S26 | Syzygy **may propose** the front-door link and **may never write it**; a declining owner renders `no`, truthfully, not as an error. "Configured landing document" is **not an input** — the read is the repository's root README | `RFC7-40` (VIS-5) |
| S27 | Effective lifecycle status is read from an **owner-act record bound to the artifact's exact immutable content digest**, never from a tree-resident stamp: "`accepted` written in a file is a claim by whoever wrote the file, not proof of acceptance" | `RFC3-16` |
| S28 | The authorization-bearing predicate is the scope, and its example list is explicitly non-exhaustive | `RFC3-16(a)` |
| S29 | Clients are classified into **exactly two exhaustive classes by credential presented, never by network location or header heuristics**; loopback proves nothing; an absent `Origin` classifies nothing | `RFC5-3` |

### BEHAVIOUR — what a specification would have to state

| # | What a spec must state | Row |
|---|---|---|
| B1 | What *registration* is as an observable operation: its trigger, its inputs, its terminal outcomes, and what "registered" means when read back | 1.1 |
| B2 | The **named** failure set for an invalid declaration. `RFC3-9` fixes the consequence (all dependent claims Unknown; no auto-repair) but names no failure identifiers; the charter's "a named failure" is an obligation with no vocabulary behind it in my materials | 1.1 |
| B3 | That registration is **atomic** with respect to the declaration — the charter's "never partial registration" is a behaviour claim I could anchor to no clause | 1.1 |
| B4 | The exact YAML **dialect** for `project.yaml`, which `RFC3-1` explicitly delegates: "its exact dialect … is fixed by the first accepted spec that parses it, and is a conformance item from then on" | 1.1 |
| B5 | How consent coverage is computed and rendered per repository — which repositories count as in scope, and how the *coverage boundary* of `RFC6-19` class 7 is populated at registration time | 1.2 |
| B6 | What "serve" means observably at the fixed entry path — the request/response behaviour, not the path (the path is shape) | 1.3 |
| B7 | The **facet list itself**, and per facet: what answers it, at what tier, and which of the twelve reasons it may carry | 1.4 |
| B8 | Which reason value the **merged-but-unreconciled** rendering carries — the charter records that this "flagship V0 rendering is bound to no reason value in the closed vocabulary" | 1.4 |
| B9 | The rendering of the **Mission-ready** facet while D1/D2 are deferred ("the facet exists; its semantics do not") | 1.4 |
| B10 | How the *owning authority* of each answer is identified in the response — `RFC6-19` class 4 requires the typed authority **with its governing normative revision**; the spec must state what identity is emitted for each of doctrine rule / contract clause / requirement / policy | 1.5 |
| B11 | The parity acceptance procedure: how a human rendering and a machine answer over one declared scope are compared, and at what granularity | 1.5 |
| B12 | When and how the discoverability finding is recomputed, and what a *proposal* of the link is as an artifact and as an observable event | 1.6 |

### Genuinely on the boundary

- **The YAML dialect (B4).** Shape fixes that a dialect must be fixed, fixes the file, and fixes that two implementations disagreeing about whether one `project.yaml` parses is a contradiction routed to the owner. It deliberately hands the choice to the first accepted spec. So this is *behaviour by delegation from shape* — but I must not make the choice, and the brief forbids me from proposing a file format. I name it and stop.
- **The facet vocabulary (B7).** The router records a generation-time sweep: the facet names appear in **0 of the 30 modules** the Waves A+B manifests name. Whether the Capability 1 spec owns them, or Wave A must be amended to own them, is exactly what **P-37** decides. Until then this is not assignable to either column — it is not fixed shape, and a spec is not yet licensed to fix it either.
- **The `not-applicable` value's *predicate*.** `RFC7-40` fixes the value and fixes its meaning as "the repository has no governance root and can host no entry." Shape. But *which* repositories in a multi-repository declaration satisfy that predicate at a given evaluation is a derivation over `RFC3-5`'s `repositories[]` roles that no clause I opened spells out. I read the domain as shape and the per-entry derivation as behaviour, and I flag that I am splitting one sentence.
- **Normalized work state (`RFC6-19` class 8 (ii)).** The clause makes `RFC8-12` "a forward reference, informative until RFC 0008 is accepted: until then the field is not required, its absence renders as absence, and nothing may be substituted for it." Whether Capability 1 emits it depends on an acceptance act that has not occurred, so it is neither fixed nor spec-authorable today.

---

## Proposed requirement outline

### Row 1.1 — Parse and validate the project declaration

**R1.1-A**
- **form** — lifecycle transition
- **statement** — A declaration is either fully registered or not registered at all; there is no intermediate registered state in which some closed-set fields of `RFC3-5` are in effect and others are not.
- **reachable case** — A fixture declaration in which the first *n* top-level fields are well-formed and field *n+1* violates `RFC3-5`'s closed set (an unknown top-level key, or a `repositories[]` entry lacking a role).
- **oracle** — A hand-authored expectation per fixture stating exactly one of `{registered, not-registered}` plus, for `not-registered`, the failure identifier from B2's vocabulary. Terminating: fixture count is finite and the expectation is a literal comparison against a closed two-valued outcome.
- **falsifier** — Any read-back of the fixture project that answers a declaration-derived question with a value drawn from the valid prefix while the outcome is `not-registered`.
- **authority** — `RFC3-5` (closed field set), `RFC3-9` (invalid declaration renders every dependent claim Unknown). **The atomicity itself is anchored to no clause I opened** — `RFC3-9` gives the Unknown consequence, not the all-or-nothing transition. I flag this rather than attribute it.

**R1.1-B**
- **form** — event-response
- **statement** — On an unparseable or schema-invalid `project.yaml`, every claim dependent on the declaration answers **Unknown**, and the response names the failure.
- **reachable case** — A fixture whose `project.yaml` is byte-level unparseable; a second whose parse succeeds and whose field set violates `RFC3-5`.
- **oracle** — The set of dependent claims is enumerated from the fixture's expectation file; each expected answer is the literal `Unknown` plus its expected primary reason drawn from `RFC2-24`'s twelve. Comparison is set equality against a hand-authored expectation; both sets are finite, so it terminates.
- **falsifier** — Any dependent claim answering `Observed` or `Inferred`, or answering `Unknown` with a reason string outside the twelve, or an empty result set rendered where the expectation names claims.
- **authority** — `RFC3-9`; `RFC2-24`; `RFC6-14` (verbatim reason).

**R1.1-C**
- **form** — invariant
- **scope of quantification** — every Project evaluation over every declaration in the fixture corpus.
- **statement** — For every evaluated Project, the count of declared `governance-root` roles is exactly one; a declaration naming **two** mints a contradiction in the Project's own evaluation, and a declaration naming **zero** is unevaluable as a Project and renders Unknown (`missing-declaration`) at the workspace/manifest level with **no kernel contradiction**.
- **counterexample schema** — ⟨declaration with *k* governance roots, *k* ≠ 1, observed outcome⟩ where the outcome is: silent repair to one root; an empty project rendering; a contradiction minted for the *k=0* case; or no contradiction for the *k=2* case.
- **oracle** — Expectation per fixture: the pair (contradiction minted? yes/no, rendered value + reason). Both are closed domains, compared literally.
- **falsifier** — A *k=0* fixture producing a kernel contradiction, or a *k=2* fixture producing none, or either producing a repaired single-root declaration.
- **authority** — `RFC1-1`; `RFC3-4`.

**R1.1-D**
- **form** — prohibition
- **scope of quantification** — every registration attempt over every invalid or undeclared fixture project, across all writable paths.
- **statement** — Registration never mutates the declaration to make it valid; drafted content is emitted as unadopted, and repair travels as a Proposal through the owner gate.
- **counterexample schema** — ⟨invalid fixture declaration, byte diff of `.syzygy/project.yaml` before vs after a registration attempt⟩ where the diff is non-empty and no owner act intervened; or ⟨drafted field, rendering⟩ where the rendering lacks the *unadopted draft* state.
- **oracle** — Byte-for-byte comparison of the fixture tree before and after, plus a check that every drafted value carries the *unadopted draft* sibling surface state. Terminates on a finite tree.
- **falsifier** — Any non-empty diff to a governance artifact Syzygy did not author, without the conflict being surfaced; or a drafted value rendered without the unadopted state.
- **authority** — `RFC3-9`; VIS-4 (charter capability-level doctrine); `RFC6-14`/`RFC2-25`'s sibling surface states as carried by `RFC6-14`.

### Row 1.2 — Consent and repository coverage

**R1.2-A**
- **form** — event-response
- **statement** — When a `repositories[]` entry's consent reference does not resolve to an in-force consent record, that repository's content answers **Unknown** with primary reason **#6 `unconsented-source-or-provider`**, and the answer carries reason #6's declared resolution route ("Record consent").
- **reachable case** — Fixture A: entry references a record ID present in no `governance/decisions/`. Fixture B: entry references a record that exists and has been withdrawn. Fixture C: entry references an in-force record (the positive control).
- **oracle** — Per-fixture expectation naming the literal triple ⟨label, primary reason, resolution route⟩; reason and route are both fixed strings copied from `RFC2-24`'s row 6, so the comparison is literal and terminating.
- **falsifier** — An empty repository content set rendered as absence; an error state; a reason other than #6; or a missing resolution route.
- **authority** — `RFC3-6`; `RFC2-24 #6`; `RFC1-3`; `RFC6-26`.

**R1.2-B**
- **form** — prohibition
- **scope of quantification** — every surface and every endpoint response, over every fixture containing at least one unconsented repository.
- **statement** — An unconsented portion is never presented as a failure, a broken link, or an empty region, and the consented remainder renders normally alongside it.
- **counterexample schema** — ⟨fixture with mixed consent, response⟩ where the unconsented portion carries an error/exception/HTTP-failure classification, or where a consented sibling repository's facts are absent from the same response.
- **oracle** — Two checks on a hand-authored expectation: (i) the unconsented portion's rendered classification equals `Unknown` + reason #6, (ii) the set of facts for consented siblings equals the expectation's set. Both finite.
- **falsifier** — Consented facts missing because an unconsented sibling was present; or the unconsented portion classified as anything other than a policy state.
- **authority** — `RFC6-26`; `RFC1-3`.

**R1.2-C**
- **form** — invariant
- **scope of quantification** — every consent record referenced by every fixture declaration.
- **statement** — Consent records are referenced from the declaration and never embedded in it; observation consent is scoped to the pair *(observing Project, repository)*, and egress consent to the pair *(Project, provider)* naming a **set** of content classes — one record per pair, never one per content class and never per repository.
- **counterexample schema** — ⟨declaration, consent artifact⟩ where the record's content appears inline under `consents[]`; or ⟨two consent records, one *(Project, provider)* pair⟩; or a consent record whose subject is a bare repository rather than the *(Project, repository)* pair.
- **oracle** — Structural check over the fixture corpus: `consents[]` entries are references only; the multiset of *(Project, provider)* subjects has no duplicates; every observation record's subject is a pair. Finite corpus, terminating.
- **falsifier** — Any of the three counterexample forms appearing without being surfaced.
- **authority** — `RFC3-7`; `RFC3-5` (`consents[]` = "References to consent records … never the records themselves").

**R1.2-D**
- **form** — invariant
- **scope of quantification** — every consent record whose attribution is used to justify an observation.
- **statement** — A consent record's stored attribution is honored only when the owner-act provenance predicate of `RFC3-16(a)` is satisfied; an unbacked record authorizes no observation.
- **counterexample schema** — ⟨consent record with attribution but no verifying owner-act record bound to its digest, observation performed⟩.
- **oracle** — For each fixture record, the expectation states ⟨provenance-verified: yes/no, observation admitted: yes/no⟩; the required relation is *admitted ⇒ verified*. Literal, terminating.
- **falsifier** — Any observation admitted on the strength of an attribution field alone.
- **authority** — `RFC3-7` ("Attribution is a stored field and therefore a *claim* about who granted it; it is honored only under RFC3-16(a)"); `RFC3-16(a)`; `RFC3-16` (a tree-resident stamp is never self-authenticating).

### Row 1.3 — The fixed human entry

**R1.3-A**
- **form** — state projection / query
- **statement** — For a governed project, the human entry is served at `.syzygy/intent/OVERVIEW.md`, at the same path in every governed project.
- **reachable case** — Two fixture projects with different names, both governed, both carrying the file.
- **oracle** — The served path string equals the literal from `RFC7-39`, checked across both fixtures. Terminating string comparison; consults no implementation logic.
- **falsifier** — A per-project or configurable entry path; or a second path presented as the entry.
- **authority** — `RFC7-39`.

**R1.3-B**
- **form** — event-response
- **statement** — A governed project lacking the entry file renders the absence as a finding under RFC 0002's vocabulary — the gap surfaces where the absence is observable, Unknown where it is not — never silently.
- **reachable case** — Fixture with the file deleted (absence observable); fixture whose governance root was not captured in the snapshot (absence unobservable).
- **oracle** — Per-fixture expectation of ⟨finding present: yes, rendered value⟩, with the unobservable case expecting `Unknown` plus a reason from the twelve (`source-uncaptured-or-unreachable` is the reason `RFC2-24` row 10 defines for an uncaptured input; I do not assign it here because no clause I opened assigns it for this case). Terminating.
- **falsifier** — No finding emitted; or a green/absent-is-fine rendering.
- **authority** — `RFC7-39`; `RFC2-24`.

**R1.3-C**
- **form** — prohibition
- **scope of quantification** — every rendering of the entry — interactive, exported, embedded, plain-text — and every citation anywhere in Syzygy.
- **statement** — The entry is never cited as authority, and every rendering of it carries the `non-citable` / `presentation-artifact` attribute.
- **counterexample schema** — ⟨rendering channel, response bytes⟩ where the entry's content appears without the attribute; or ⟨any Syzygy answer, its provenance class 4 authority field⟩ naming the entry as the governing authority.
- **oracle** — Enumerate the rendering channels the fixture exercises; assert attribute presence on each; scan the provenance fields of all fixture answers for the entry's identity. Finite channels and finite answers.
- **falsifier** — A plain-text or exported rendering that drops the attribute; the recipient can then "tell draft from curated and not presentation from authority."
- **authority** — `RFC7-39`; `RFC7-33`.

### Row 1.4 — Facets answered independently

**R1.4-A**
- **form** — prohibition
- **scope of quantification** — every rendered surface, every endpoint response, and every stored derived value, over the whole fixture corpus.
- **statement** — No composite, rolled-up, or synthetic single value over the facets is computed, rendered, or served.
- **counterexample schema** — ⟨response, field⟩ where a field's value is a function of two or more facets and is not itself a disclosed composition — a score, a badge, a health number, a percentage-ready, a synthetic effort figure.
- **oracle** — Enumerate every scalar field of the response schema against a hand-authored allowlist derived from the facet list; any field not on the list is a finding. Terminating over a finite schema. (This oracle is **blocked on B7/P-37**: the allowlist cannot be authored until the facet vocabulary has an owner.)
- **falsifier** — Any single value whose change is caused by a change in more than one facet.
- **authority** — `RFC8-18` ("No synthetic 'effort' number may be computed, rendered, or served"); `RFC6-14` ("An aggregate carries no epistemic state of its own"); charter non-goal 1; VIS-1 as quoted inside `RFC6-14`.

**R1.4-B**
- **form** — invariant
- **scope of quantification** — every selection, at every evaluation, whose fact set includes `RFC6-19` class 8 (i).
- **statement** — Where reconciliation has not been computed, the chain state renders **Unknown with its reason**, never green and never a satisfied value; chain state and normalized work state are two fields, never folded into one, and neither is rendered as proof of satisfaction.
- **counterexample schema** — ⟨selection with uncomputed reconciliation, rendered class-8 value⟩ where the value is any of `RFC2-18`'s satisfied values, or where the two fields appear merged, or where the value is presented as evidence that work is done.
- **oracle** — Per fixture, an expectation naming the class-8 pair; the uncomputed case expects `Unknown(reason)`. Values are drawn from `RFC2-18`'s closed list quoted in `RFC6-19`, so comparison is literal.
- **falsifier** — A green reconciliation rendering with no computation behind it; or a single merged work/reconciliation field.
- **authority** — `RFC6-19` class 8 ("an uncomputed reconciliation renders Unknown, never green"); `RFC6-17` (an aggregate cannot satisfy the disclosure while saying nothing about reconciliation). **The specific reason value is unavailable** — see P-31 below.

**R1.4-C**
- **form** — invariant
- **scope of quantification** — every aggregate in every scene, table, or machine answer.
- **statement** — Every aggregate discloses its membership count and the full `RFC6-22` equivalence tuple — per-label, per-tier (all six tiers), per-Unknown-reason (primary only), per-freshness-state counts, the three sibling surface states, the `challenge-pending` disclosure, and per-value counts of chain state where members carry it — and supports expansion to members.
- **counterexample schema** — ⟨aggregate, disclosed tuple⟩ where any component is absent, where tier counts cover fewer than six tiers, where secondary Unknown annotations are folded into the primary counts, or where expansion is unavailable.
- **oracle** — The expected tuple is computed **from the fixture's own hand-authored member list**, not from the system: sum the per-member expectations and compare component-wise. Terminating; independent of the implementation.
- **falsifier** — Two conforming surfaces producing different Unknown-reason totals over one declared scope — which `RFC6-23` would class release-blocking.
- **authority** — `RFC6-17`; `RFC6-14`; `RFC6-22`.

**R1.4-D**
- **form** — invariant
- **scope of quantification** — every measure and every aggregate over partially-known measures.
- **statement** — An absent measure renders **Unknown, never zero**; every aggregate over partially-known measures discloses coverage ("known for *n* of *m*") and never renders as a complete total.
- **counterexample schema** — ⟨fixture with *m* items and measures recorded for *n* < *m*, aggregate rendering⟩ where the rendering shows a total without the *n/m* disclosure, or where absent values contributed 0.
- **oracle** — Author the fixture so the correct total over the *n* known items differs from the total that would result from treating absences as 0; compare against the hand-computed expectation plus the literal coverage pair.
- **falsifier** — A total equal to the treat-absence-as-zero value; or a total with no coverage disclosure.
- **authority** — `RFC8-19`; `RFC2-24`'s "Missing quantity" row ("**Unknown, never zero**; no aggregate silently treats absent as 0").

### Row 1.5 — Authority and reason, identically to human and machine

**R1.5-A**
- **form** — invariant
- **scope of quantification** — every query answer served, on every path.
- **statement** — Every answer names the evaluation identity (source snapshot + as-of instant) it was computed at; same evaluation + same filters ⇒ same answer in the deterministic layer; a mixed-evaluation answer declares its skew.
- **counterexample schema** — ⟨answer, envelope⟩ with no evaluation identity; or ⟨two requests, same evaluation, same filters, differing answers⟩; or a mixed-evaluation answer with no declared skew.
- **oracle** — Presence check on a required envelope field, plus a repeat-request equality check pinned to a fixed evaluation identity. Both terminate. (The repeat check is metamorphic and does re-run the system; the *anchor* is the presence requirement, which is checked against the clause, not the system.)
- **falsifier** — Any answer without an evaluation stamp — "an answer that cannot name its evaluation is not an answer."
- **authority** — `RFC6-15`.

**R1.5-B**
- **form** — invariant
- **scope of quantification** — every entity and claim instance in every machine answer.
- **statement** — Each carries label, tier, Unknown reason (where applicable), and freshness state **verbatim** from the RFC 0002 vocabulary; secondary annotations travel marked as secondary and drawn from the same twelve; sibling surface states and `challenge-pending` travel beside, never displacing, the four values.
- **counterexample schema** — ⟨answer element, carried state⟩ with a missing component, a reason string outside the twelve, a secondary value from no vocabulary, or a count that folds Unknowns into a total silently.
- **oracle** — Membership test of every emitted string against the twelve reasons and six tiers, transcribed once from `RFC2-24`/`RFC2-25` into the expectation file; plus a presence test for all four components per element. Finite closed vocabularies; terminates.
- **falsifier** — An answer listing entities without labels, or a total that silently absorbs Unknowns — the state in which "an agent [is not] exactly as unable to mistake Unknown for success as the owner is."
- **authority** — `RFC6-14`; `RFC2-24`.

**R1.5-C**
- **form** — invariant
- **scope of quantification** — every pair of renderings (human surface, machine answer) over one selection at one evaluation with one declared filter set.
- **statement** — Both are computed from the one fact set for that *(selection reference, evaluation identity, scenario context)*; anything a surface renders is queryable and anything queryable is renderable; presentation may differ, facts, labels, and provenance may not.
- **counterexample schema** — ⟨selection, evaluation, surface fact set, endpoint fact set⟩ where the symmetric difference is non-empty.
- **oracle** — Both renderings are normalized to the `RFC6-22` tuple and compared against **the fixture's hand-authored expected tuple** — not against each other. Comparing them only to each other would be a differential oracle over the implementation under test; comparing each to the authored expectation is not.
- **falsifier** — Any fact present on one path and absent on the other; per `RFC6-18` this is "a kernel defect, not a UI inconsistency."
- **authority** — `RFC6-13`; `RFC6-18`; `RFC6-22`; `RFC7-33`.

**R1.5-D**
- **form** — state projection / query
- **statement** — Every answer names the typed authority that answered the question, **with the governing normative revision** — the revision or digest identity of the doctrine rule, contract clause, requirement, or policy the answer rests on.
- **reachable case** — A fixture in which one facet's governing artifact is amended between two evaluations; both answers are requested.
- **oracle** — Per fixture, an expectation naming the authority identity and revision for each facet; literal comparison. Terminating.
- **falsifier** — Two answers resting on different revisions of an artifact that name the same revision identity; or an answer with an authority name and no revision.
- **authority** — `RFC6-19` class 4; `RFC3-16` (effective status is read from the owner-act record bound to the exact content digest, never from an in-file stamp).

### Row 1.6 — Repository-front-door discoverability

**R1.6-A**
- **form** — state projection / query
- **statement** — For every repository of a governed project, the kernel answers *does this repository's root README link to `.syzygy/intent/OVERVIEW.md`?* with exactly one of `yes / no / not-applicable / Unknown`, carried verbatim on every rendering and machine answer; `Unknown` carries its RFC2-24 reason; `not-applicable` carries the declared basis for the limitation and is never counted among Unknown reasons.
- **reachable case** — A four-repository fixture: one governance root whose README links the entry (`yes`); one governance root whose README does not (`no`); one observed-source repository with no governance root (`not-applicable`); one repository not captured in the snapshot (`Unknown`).
- **oracle** — A hand-authored expected value per repository, compared literally against a four-element closed domain, plus, for `Unknown`, a membership test of the reason against the twelve. Terminating; the expectation is authored from the fixture's contents, not from a run.
- **falsifier** — A fifth value; a spelling variant; `not-applicable` stamped with an Unknown reason; a "configured landing document" consulted instead of the root README; or an aggregate that counts `not-applicable` among Unknowns.
- **authority** — `RFC7-40`; `RFC6-14` (verbatim carriage); `RFC2-24`.

**R1.6-B**
- **form** — prohibition
- **scope of quantification** — every repository of every fixture project, over the whole repository tree.
- **statement** — Syzygy never writes the front-door link, and more generally writes nothing outside `openspec/**` and `.syzygy/**`; a repository whose owner declines the link renders `no`, truthfully, not as an error.
- **counterexample schema** — ⟨repository tree before, tree after any Capability-1 operation⟩ with any diff outside the two namespaces; or ⟨declining repository, rendering⟩ classified as an error, warning-as-failure, or defect.
- **oracle** — Full-tree byte comparison restricted to paths outside the two namespaces (expected: empty diff), plus a literal check that the declining repository's value is `no`. Terminating over a finite tree.
- **falsifier** — Any README modified; or `no` rendered as a failure state.
- **authority** — `RFC7-40`; `RFC3-3` (direct-write containment; a field purporting to grant write access elsewhere is inoperative); VIS-5; charter non-goal 3.

**R1.6-C**
- **form** — event-response
- **statement** — Where the finding is `no` and the repository could host the link, Syzygy emits a **Proposal** — an owner-gated artifact — and the proposal's existence never changes the finding's value.
- **reachable case** — The `no` repository of R1.6-A's fixture, evaluated twice: before and after the proposal is emitted.
- **oracle** — Expectation states ⟨proposal emitted: yes, finding value at both evaluations: `no`⟩. Literal, terminating.
- **falsifier** — The finding shifting to `yes` (or to any non-`no` value) on the strength of an unaccepted proposal.
- **authority** — `RFC7-40` ("may propose the link (a Proposal, RFC1-27) and may never write it"); `RFC3-9` (repair travels as a Proposal through the owner gate). **The Proposal's own artifact shape is not defined in anything I opened** — `RFC1-27` is cited by both clauses but is not among the modules the route names, and I did not open it.

---

## Unresolved decisions this outline runs into

| Decision | Where it bites | What an author cannot write until it is ruled |
|---|---|---|
| **P-37** | Row 1.4, requirement R1.4-A and the whole of B7 | The facet vocabulary. The router records that a generation-time sweep found the facet names in **0 of the 30** Waves A+B modules. Until P-37 says whether the Capability 1 spec owns the names or Wave A must be amended to, no requirement can enumerate the facets, R1.4-A's allowlist cannot be authored, and no per-facet oracle has a domain. |
| **P-31** | Row 1.4, requirement R1.4-B | The reason value carried by the **merged-but-unreconciled** rendering. The charter states it "is bound to no reason value in the closed vocabulary" — so the flagship V0 case has an obligation (`Unknown`, never green) with no reason string to carry, and `RFC6-14` requires reasons verbatim. The requirement is writable; its expected value is not. |
| **P-36** | Rows 1.4 and 1.5 | Named by the charter and the views as blocking both rows. **I cannot say what it decides** — my materials give the identifier and the two rows, and nothing more. I did not open the pending-decisions queue. |
| **P-38** | Rows 1.3 and 1.6 | The identity of the human entry. `RFC7-39` carries the ruling inline as a **drafted arm awaiting the owner**: whether the fixed entry *is* the RFC7-6 primary narrative, or reverts to "a thin index entry distinct from the narrative." R1.3-A's path is stable either way; what a spec may require the entry to *contain*, and which narrative obligations follow it, is not. |
| **P-1, P-21, P-22, P-28, P-33, P-39, P-40, P-41, P-42** | Capability-level — they block **authoring the capability at all**, not one row | Unknown to me. The charter and views give identifiers and the label "capability-level"; neither states subject matter. Nine open rows gate the work before any row-level question is reached. |
| **P-34, P-35** | Open upstream, at a later gate | Assigned by the queue's launch-scope index to the formal launch administration, not to authoring. Named so a reader is not surprised, not because this outline consumes them. |
| **The `project.yaml` dialect** *(not a P-number)* | Row 1.1, B4 | `RFC3-1` delegates the exact YAML dialect — version, coercion rules, duplicate-key handling — to "the first accepted spec that parses it," and makes it a conformance item from then on. No spec exists, so nothing fixes it; a parse-outcome oracle for R1.1-A/B has an undefined boundary until it is fixed. I do not propose a dialect. |
| **The "named failure" vocabulary** *(not a P-number)* | Row 1.1, B2 | The charter requires an invalid declaration to be "a named failure." No clause I opened defines a failure-identifier vocabulary. Either the spec mints one — which is a decision about what the spec may own, structurally the same question P-37 poses for facets — or a contract amendment does. |
| **RFC 0008 acceptance** *(an act, not a decision)* | Row 1.4, `RFC6-19` class 8 (ii) | `RFC8-12`'s normalized work state is "a forward reference, informative until RFC 0008 is accepted: until then the field is not required, its absence renders as absence, and nothing may be substituted for it." Whether Capability 1 emits the field is settled by an acceptance act, not by an author. |
| **Waves A and B acceptance** *(the acts themselves)* | Every requirement above | Every clause cited here is a **candidate** of a confirmed-but-unaccepted wave. Each module's own banner — "absent such a record, this contract binds nothing" — governs every citation in this document. Nothing above is currently authority for anything. |

---

## What I could not do, and why

1. **I could not anchor "never partial registration."** The charter's row 1.1 asserts atomicity. `RFC3-9` gives me the *consequence* of invalidity (all dependent claims Unknown; no auto-repair) and `RFC3-5` gives me the closed field set, but neither states an all-or-nothing transition. R1.1-A is therefore proposed with its authority marked incomplete rather than attributed to a clause that does not say it. Verification rule 8 applies: I will not justify a clause-level claim from adjacent prose.

2. **I could not enumerate the facets, and so could not write per-facet requirements.** Row 1.4 is the capability's centre and it is the row I could take least far. The generated route reports the sweep result — 0 of 30 modules — so this is a measured absence, not my failure to find them. Every row-1.4 requirement above is therefore a *frame* with an empty domain.

3. **I could not give R1.4-B its expected value.** The merged-but-unreconciled rendering is named in the charter as the flagship V0 case, and it is bound to no reason in a vocabulary that `RFC2-24` closes at twelve and `RFC6-14` requires verbatim. A requirement whose oracle cannot state the expected string is not yet testable.

4. **I could not say what P-36 decides, or what any of the nine capability-level decisions decide.** I have identifiers only. Opening `decisions/PENDING-OWNER-DECISIONS.md` would have exceeded my reading scope, so I report the identifiers and the rows they attach to and stop. This is an `[Unknown]`, not a zero.

5. **I could not evaluate this outline against any spec-quality bar, because none is in force.** The route states it explicitly: CC-SPEC-1…10 and CC-IMPACT-1…7 are candidate craft policy, "routed as prerequisites, never cited as binding." The form/oracle/falsifier structure I used is my own construction to satisfy the brief, not a policy-derived shape. A reviewer should treat the *shape* of these requirements as unwarranted by anything in the repository.

6. **I could not describe the Proposal artifact.** `RFC1-27` is cited by both `RFC7-40` and `RFC3-9` as the Proposal construct, but RFC-0001's clause 27 is outside the range the route names and outside the range I read. R1.6-C names the obligation and leaves the artifact undefined.

7. **I did not open two files the route's "Load" list names.** `FIRST-OPENSPEC-SEQUENCE.md` is explicitly excluded by my brief. `HOW-TO-AUTHOR-A-SYZYGY-SPEC.md` I did not need — it is a router, and authoring is forbidden. I also did not open RFC-0004 or RFC-0009, which appear in the route's *computed* declared-dependency list but govern no clause of this capability; per verification rule 5, a declared dependency edge is not a reliance.

8. **I made no choice on any unresolved arm, and proposed no implementation.** No language, framework, storage engine, schema, API shape, serialization dialect, or deployment target appears above. Where `RFC3-1` fixes `.syzygy/project.yaml`, I am reporting a clause, not choosing a format.

---

## Confirmation

**Files I opened** (all read-only; several read as line ranges rather than in full):

1. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/TASK-ROUTER.md` — heading list, then lines 111–126 only (the "Author Capability 1" section)
2. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/CAPABILITY-1-CHARTER.yaml` — in full
3. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/CAPABILITY-1-GENERATED-VIEWS.md` — in full
4. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/rfcs/RFC-0001-project-graph-identity-state-planes.md` — lines ~85–150 (`RFC1-1` … `RFC1-4`)
5. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/rfcs/RFC-0002/rendering-vocabularies.md` — lines ~88–135 (`RFC2-24`)
6. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/rfcs/RFC-0003/manifests-and-namespace.md` — lines ~90–270 (`RFC3-1` … `RFC3-11`)
7. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/rfcs/RFC-0003/governance-homes-and-owner-acts.md` — lines ~103–135 and ~158–200 (`RFC3-16`, `RFC3-16(a)`)
8. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/rfcs/RFC-0005/admission-and-boundary.md` — lines ~101–130 (`RFC5-3`, opening of `RFC5-4`)
9. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/rfcs/RFC-0006-cross-surface-selection-query-drawer.md` — lines ~229–400 and ~456–480 (`RFC6-13` … `RFC6-22`, `RFC6-26` … `RFC6-28`)
10. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/rfcs/RFC-0007/rendering-and-surface.md` — lines ~201–225 and ~370–450 (`RFC7-33`, `RFC7-39`, `RFC7-40`)
11. `/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/rfcs/RFC-0008/state-vocabulary-and-cost.md` — lines ~258–320 (`RFC8-17` … `RFC8-20`)

Items 4–11 are the contract modules named under the route's "Directly governing clauses"; I opened each only to read the text of clauses I cite, and every quotation above comes from a module in this list.

**I created no files and edited no files.** No `openspec/` directory was created. Nothing was written to disk anywhere in the repository or outside it — every tool call I made was a read (`sed`, `grep`, `Read`). Nothing in the working tree changed.
