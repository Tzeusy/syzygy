# The Capability 1 outline exercise — administered 2026-08-11

> **Two things are in this file and they are not the same thing.** Below the
> first rule is the **administering session's grading** against the six
> criteria `CAPABILITY-1-SPEC-OUTLINE-EXERCISE.md` fixed *before* the
> exercise ran. Below the second rule is the **agent's raw output, verbatim
> and unedited**. The grading may be argued with; the output may not be
> edited.

## Administration record

| | |
|---|---|
| **Administered** | 2026-08-11 |
| **Where** | a clean clone of the published remote, `git checkout e2efda6`, working tree clean (0 porcelain lines) |
| **Agent** | fresh context, no project history, told only the four permitted materials and the task text verbatim from the exercise |
| **Materials given** | `TASK-ROUTER.md` (and exactly the clauses/modules the Capability 1 route names), `doctrine/vision.md`, `.syzygy/intent/OVERVIEW.md`, `round-2026-08f/CAPABILITY-1-OWNER-DECISION-PACKET.md` |
| **Withheld, as specified** | the review corpus, every semantic delta, the launch-gate instrument and its history, `PROJECT-STATUS.md`, `PROCESS-LESSONS.md`, and the exercise specification itself |
| **Model family** | same family as the corpus authors — so this is evidence for D2 routing, and is **not** a launch administration |
| **Files created by the agent** | none, as required |

## The six criteria, graded individually

| # | Criterion (fixed in advance) | Result | Evidence |
|---|---|---|---|
| 1 | states the capability in one sentence | **pass** | §1 is one sentence, and it deliberately names no facet vocabulary — with the reason given |
| 2 | identifies unresolved decisions rather than selecting them | **pass** | §3 names thirteen, opening with P-37, P-36, P-38 — the three the exercise called unavoidable — and says of P-37 "This is why §1's sentence names no facets and §2 has no facet section." Nothing is chosen and nothing is written around |
| 3 | distinguishes shape from behavior | **pass** | headings A/B are declaration and membership; D/E/F are rendering behaviour; D7 states the split explicitly — "declaration Observed, satisfaction Unknown" |
| 4 | identifies testable scenarios | **pass — the weakest of the six** | the discriminations are testable as written (A2: two roots → contradiction, zero roots → Unknown `missing-declaration`, and *not* a kernel contradiction; E3: the closed four-value domain), but they are requirement headings with outcomes, not scenario blocks. The exercise asked for headings, so this is graded on the discrimination and not on form |
| 5 | cites exact authorities (clause and rule IDs, not document names) | **pass, with one exception recorded** | every row cites identifiers — `RFC3-4`, `RFC1-1`, `RFC2-24`, `RFC7-40`, `VIS-5`. The exception is F3, which cites `vision.md`'s "two first-class consumers from day one" by document rather than by rule ID, and the agent itself flags that RFC6-13/6-14 were unreadable to it |
| 6 | proposes no implementation | **pass** | swept the output for a language, framework, storage engine, schema technology or UI framework: none. `.syzygy/project.yaml` and the YAML-dialect note are quotations of `RFC3-1`, not a proposal |

**Six of six.** The exercise's own bright line — criterion 2, the failure "most likely to look like success" — is the one the output meets most convincingly.

## What the exercise found that was *not* about the agent

The specification says a failure is evidence about the **route**. Two route
findings came out of a passing run, and they are recorded here as route
defects rather than buried in a passing grade:

1. **RFC-0006 is in the route's computed dependency closure and in none of
   its Load paths.** The agent: *"RFC-0006 is in the route's computed
   dependency list but in none of its five Load paths. Heading F3 and the
   'no rollup' half of D5 cannot be properly anchored without it. **This is
   the gap I would most want closed before authoring.**"* `RFC6-17` is the
   aggregation composition that `RFC2-24`, `RFC3-32` and `RFC7-37`
   cite-never-restate, and `RFC6-13`/`RFC6-14` are the machine-endpoint
   parity clauses the capability's agent-parity requirement rests on.
2. **`RFC3-16(a)` is the provenance gate four loaded clauses defer to, and
   the route does not load the module that defines it.** The agent anchored
   its own heading H2 to a clause it had not read and said so.

Both are route repairs, not agent errors, and both are recorded for the
next pass rather than fixed inside a file the exercise binds.

## What this result does and does not establish

It is evidence for **D2** (task routing) and a contribution to **D1** (the
fresh-engineer test): the rules for this capability were reachable, at clause
granularity, without the process history. It establishes **nothing about
readiness** — readiness is the launch gate's question, the E rows are not
answered by a routing exercise, and the outline's own standing caveat is that
not one clause it cites is binding today.

---

# Raw output, verbatim

I read the four permitted materials plus exactly the five modules the Capability 1 route names (`RFC-0001-project-graph-identity-state-planes.md`, `RFC-0003/manifests-and-namespace.md`, `RFC-0002/rendering-vocabularies.md`, `RFC-0007/rendering-and-surface.md`, `RFC-0008/state-vocabulary-and-cost.md`). Nothing else. No file or directory was created.

**Standing caveat that colours everything below:** the route's own header says *"Authoring is forbidden today… `openspec/` does not exist and may not be created."* Every clause I cite carries the status banner *"Absent such a record, this contract binds nothing"* — Waves A and B are confirmed but **not accepted**, and P-33 retires the Wave A confirmation under every arm. So this outline names where each requirement *would* anchor; not one anchor is binding today.

---

## 1. The capability in one sentence

Capability 1 registers a project with Syzygy — one declared governance root, its declared repository membership, and the consent records that permit observation — and renders that project's shape honestly, so that every fact it shows carries its epistemic label, tier, and reason, every absence renders Unknown rather than zero or green, and nothing composes into a score.

*(This sentence deliberately does not name the facet vocabulary — see P-37 below.)*

---

## 2. Requirement headings, with the authority I would cite

### A. Registration and governance-root designation

| # | Heading | Authority I would cite |
|---|---|---|
| A1 | A project is registered by the location of its declaration | `RFC3-4` (location is designation, not a field value); `RFC1-1` (one governance root, kernel invariant); `RFC3-29` (one `.syzygy/` plane, at a repository root; no directory-scoped sub-roots) |
| A2 | Two governance roots is a contradiction; zero is not | `RFC1-1` (two roots → contradiction minted in the Project's own evaluation; zero roots → unevaluable, surfaced at workspace level, Unknown `missing-declaration`, **no** kernel contradiction); `RFC3-4` (restates the zero-roots deferral by citation); `RFC1-21` (contradictions route to the owner, never resolved by precedence, never auto-scheduled) |
| A3 | The declaration's field set is closed | `RFC3-5` (the eight top-level fields and their write authorities); `RFC3-2` (four write-authority classes; no field has two writers); `RFC3-1` (the declaration is `.syzygy/project.yaml`; YAML dialect becomes a conformance item at the first accepted spec that parses it) |
| A4 | Registration identifiers are opaque; names are labels | `RFC1-10`; `RFC1-2` (repository identity is declared, never a URL, path, or branch); `RFC3-6` |
| A5 | An unparseable or invalid declaration degrades, never auto-repairs | `RFC3-9` (dependent claims Unknown; repair is a Proposal through the owner gate); `RFC1-27` (Proposal is the single container for every unadopted delta); `VIS-4` |
| A6 | Drafted registration content renders unadopted | `RFC3-9`; `RFC3-5` (Syzygy-drafted entries render unadopted); `RFC2-25` sibling surface state `unadopted-draft`; `VIS-4` |

### B. Membership, roles, and consent

| # | Heading | Authority |
|---|---|---|
| B1 | Repository role and membership are answered by the declaration; content by the version-control authority | `RFC1-4` (two questions, two authorities — no construct may merge them); `RFC1-2` (role is a property of one entity class) |
| B2 | No consent, no observation — and therefore Unknown, never an empty graph | `RFC1-3`; `RFC3-6` (unresolved consent reference → not observed); `RFC2-24` #6 `unconsented-source-or-provider`; `SEC-4` *(cited as named by RFC1-3/RFC3-7 — see §4, I did not read `security.md`)* |
| B3 | Consent is per-pair, referenced never embedded, and revocable without erasure | `RFC3-7` (observation consent keyed on *(Project, repository)*; egress consent on *(Project, provider)*); `RFC3-8` (revocation effect on claims at the next evaluation vs. on rendering immediately); `RFC2-23` *Consent withdrawn* degradation state |
| B4 | Dual roles are lawful and per-pair; an observing project screens under **its own** policies | `RFC3-30`; `RFC3-32` (what a parent may never do) |

### C. Write containment

| # | Heading | Authority |
|---|---|---|
| C1 | No manifest field may widen the write universe | `RFC3-3` (a field purporting to grant write elsewhere is inoperative *and* surfaced as a contradiction — never silently ignored, never silently obeyed); `VIS-5` |
| C2 | Registration writes only into the two namespaces | `VIS-5`; `RFC3-30` (an observing project reads another plane read-only) |

### D. Honest shape rendering — the vocabularies

| # | Heading | Authority |
|---|---|---|
| D1 | Every Unknown carries exactly one primary reason from the closed twelve, verbatim | `RFC2-24` (twelve reasons; the secondary-annotation vocabulary is the same twelve; a condition outside them is a fact of the render, never dressed as a reason) |
| D2 | Every claim renders at a label, and a tier only restricts it | `RFC2-25` (six tiers, closed; `gate-backed` is the only tier that may support a positive status claim; a tier is never a fourth label); `RFC1-19` (a narrative sentence doing a badge's work is judged as a badge) |
| D3 | Degradation is one of six named states, and a partial snapshot never renders as whole | `RFC2-23`; `VIS-1` (narrow the declared scope, never fake coverage) |
| D4 | Absence renders Unknown, never zero | `RFC2-23` *Missing quantity*; `RFC8-19`; `VIS-2` |
| D5 | Nothing composes into a score | `RFC8-18` (independent measures; **no synthetic effort number may be computed, rendered, or served**); `VIS-1`; `VIS-2` |
| D6 | Status flows only through Claims, and only via `supports` | `RFC1-24` (no evidence-to-status backdoor); `RFC1-19` |
| D7 | A declared-but-unverified shape renders as both halves | `RFC2-25` `declared-only` (declaration Observed, satisfaction Unknown); `RFC1-14` (code mapping to no declared capability renders Unknown, never inferred into one) |
| D8 | Drafted declarations may not anchor status or the map | `RFC1-14`; `RFC1-31` (declared-class lifecycle); `RFC1-22` (Proposed plane may not anchor the map) |

### E. The human entry point and its discoverability

| # | Heading | Authority |
|---|---|---|
| E1 | The fixed human entry point | `RFC7-39` — **and its P-38 drafted-arm marker is in the clause bytes**: the entry-identity answer is awaiting an owner ruling. A governed project without the file renders the absence as a finding, never silently |
| E2 | The entry is governed presentation, never authority | `RFC7-39`; `RFC7-29` (the boundary table); the OVERVIEW's own banner (presentation, adopted only by its own unperformed act) |
| E3 | Repository-front-door discoverability is a per-repository finding with a closed four-value domain | `RFC7-40` (`yes` / `no` / `not-applicable` / `Unknown`, carried verbatim); `VIS-5` (propose-only — Syzygy may never write the README link); `RFC1-27` (the propose affordance) |
| E4 | `Unknown` on that finding carries its RFC2-24 reason; `not-applicable` is not an Unknown | `RFC7-40`; `RFC2-24` (#6 cited, never restated; `source-uncaptured-or-unreachable`, `missing-declaration`) |
| E5 | No configurable landing document is an input | `RFC7-40`; `RFC3-5` (closed field set — an input with no declaration site is unclassified as a snapshot input) |

### F. Parity — machine, non-visual, and cross-rendering

| # | Heading | Authority |
|---|---|---|
| F1 | Every distinction is a machine-readable attribute on the rendered unit | `RFC7-33` (including the `non-citable` / `presentation-artifact` attribute on *every* exported, embedded, or plain-text rendering, and the distinguishing type name for narrative claim blocks) |
| F2 | Every distinction is recoverable without colour, position, or layout — and every path is operable without a pointing device | `RFC7-34` (both limbs); `VIS-7` (every encoding means what its legend says) |
| F3 | Registration and shape answers are served identically to agents | `RFC7-33`; `VIS-1`/`vision.md` "two first-class consumers from day one". **The endpoint-parity clauses themselves (RFC6-13/6-14) I could not read — see §4** |

### G. Cross-project and portfolio containment (only insofar as registration touches it)

| # | Heading | Authority |
|---|---|---|
| G1 | The workspace manifest is never authoritative for project-internal truth | `RFC3-12`; `RFC3-10` (VIS-6 exception (a)); `RFC3-13` (unresolvable entries render Unknown, never dropped) |
| G2 | Cross-project relations render asymmetrically until both sides declare | `RFC3-14`; `RFC7-37`; `RFC3-31` (nesting is composition by declaration) |
| G3 | Portfolio narrative may never assert a governed project's status | `RFC7-36`; `RFC1-19` |

### H. The phase boundary the specification itself must honor

| # | Heading | Authority |
|---|---|---|
| H1 | Every observable consequence maps to a requirement or a reviewed N/A judgment | `RFC1-33`, `RFC3-33`, `RFC2-26`, `RFC7-38` — all four say *this contract schedules nothing* and all four require rows **per observable consequence, not per clause**; the coverage matrix is review material, never authority |
| H2 | A reviewed N/A judgment is honored only under owner-act provenance | `RFC3-16(a)` as cited by all four clauses above — **a clause I was not routed to and did not read (§4)**; `VIS-2` (where provenance does not verify, the consequence renders Unknown, never covered) |

---

## 3. Decisions I would need that have not been made

Each of these is open; I have not chosen any of them, and I have not written around any of them.

1. **P-37 — project-shape facets and their authority home.** The route states the facet vocabulary "appears in zero of the 30 Waves A+B modules," and the decision packet records that three launch-path documents wrongly claimed the Wave A act ratifies it. Until P-37 is ruled I cannot write a single facet heading: I do not know whether *Registered / Shape present / Human-understandable / Observable / Traceable / Reconciled* are this specification's own vocabulary or shared contract semantics requiring a Wave A amendment, regeneration, and fresh confirmation. This is why §1's sentence names no facets and §2 has no facet section. It is the single largest hole in the outline.
2. **P-36 — Unknown versus Gap.** Both words appear throughout the material I read (`RFC2-24` is Unknown-only; `RFC1-20` governs gap exits; the OVERVIEW distinguishes gap from contradiction). Their boundary is unruled, and the decision packet states plainly that leaving them undistinguished makes this specification's tests unwritable. Every acceptance criterion under §2.D depends on it.
3. **P-38 — human entry and repository discoverability.** `RFC7-39` carries its own in-clause `[P-38 — drafted arm, awaiting an owner ruling]` marker. Whether the fixed entry *is* the primary narrative, or a thin index entry distinct from it, changes what heading E1 requires and whether E1 and the comprehension test walk the same path.
4. **P-40 — specification granularity.** I do not know what "one OpenSpec change" is, so I cannot know whether the eight heading groups above are one specification, or several. The outline's shape is therefore provisional in a way I cannot resolve.
5. **P-39 — OpenSpec form and version.** No pinned version, no fixed artifact format. Heading structure, requirement/scenario shape, and anchor stability all sit downstream of it; the packet also flags this as the one launch-critical check needing material from outside the clone.
6. **P-41 (CC-SPEC-1…10) and P-42 (CC-IMPACT-1…7).** Both candidate; the route explicitly says they "are routed as prerequisites, never cited as binding — which is why they are not listed under Craft." Without the first there is no acceptance standard for this outline to be judged against; without the second, no rule for what a later shape amendment does to it.
7. **P-33 — Wave A install shape.** No arm preserves the Wave A confirmation. Every RFC1-n and RFC3-n citation above rests on bytes that will be regenerated before any act.
8. **P-31 — merged, but not reconciled.** Whether `RFC2-19(a)` is ratified or reverted decides whether the flagship "merged, evidence exists, reconciliation not computed" rendering is bound to a reason at all — directly under heading D1.
9. **P-35 — project operating constraints** and **P-34 — the launch-gate policy itself.** Both gate the formal administration that precedes the launch decision that precedes authoring.
10. **RFC-0003 §7 q1 — monorepo subprojects.** Whether an owner may govern several projects inside one physical repository is foreclosed-pending-amendment. Heading A1/A3 would be written differently under each answer.
11. **RFC-0001 §8 q1–q3** (judgment lapse on split/merge; no doctrine-claim entities at V0; decomposition approval inheritance) and **RFC-0003 §7 q2** (workspace-manifest classification) are recorded as unanswered in the clause bytes; q1 in particular touches whether a registration-time dismissal survives a later declared split.
12. **The A1 correlation mechanism does not exist.** Every module's status banner says effective status is *owner-adopted bootstrap* until correlation (`RFC3-16`). Heading H2's gate therefore has no verifiable form yet, and the OVERVIEW says as much: "owner-adopted (bootstrap, uncorrelated)", never "verified".
13. **The owner's launch decision itself.** Unmade. Authoring remains forbidden.

---

## 4. What I could not determine from the materials I was given

Stated as measurement, not impression — these are clauses I *know* are load-bearing here because the modules I read cite them, but which I was not routed to and did not read.

- **`RFC3-16(a)` — the owner-act provenance predicate.** Cited as the gate by `RFC1-33`, `RFC2-26`, `RFC3-33`, `RFC7-31`, `RFC7-38`, `RFC8-12`, `RFC8-16`, and `RFC3-7`'s attribution rule. It lives in `RFC-0003/governance-homes-and-owner-acts.md`, which the Capability 1 route does **not** load. Heading H2 is anchored to a clause I have not read. Same for `RFC3-15` (the `decisions/` and `records/` homes) and `RFC3-17`.
- **All of RFC-0006.** `RFC6-13`/`RFC6-14` (machine endpoints, verbatim label parity), `RFC6-17` (the aggregation composition every roll-up owes *in full*, cited-never-restated by `RFC2-24`, `RFC3-32`, and `RFC7-37`), `RFC6-22`/`RFC6-23` (two renderings disagreeing is release-blocking), `RFC6-24`/`RFC6-25`, `RFC6-5`/`RFC6-6`. RFC-0006 is in the route's computed dependency list but in none of its five Load paths. Heading F3 and the "no rollup" half of D5 cannot be properly anchored without it. **This is the gap I would most want closed before authoring.**
- **RFC-0002 modules 1–3.** `RFC2-1`/`RFC2-2`/`RFC2-3` (snapshot inputs, the uncaptured-source rule, evaluation identity) and `RFC2-17`/`RFC2-18`/`RFC2-19` (the reconciliation chain). Evaluation identity is required on essentially every rendering in §2.D, and the *Reconciled* and *Traceable* notions have no readable anchor for me. The route loads only `rendering-vocabularies.md`.
- **RFC-0004 entirely.** `RFC4-11` (VCS merge facts, never scheduler closure), `RFC4-15`, `RFC4-23`, and the code-element and OpenSpec-anchor identity schemes `RFC1-15`/`RFC3-28` delegate to. `RFC1-15` records as `[Unknown]` whether OpenSpec identities survive edit and rename — an open question, not merely unread by me.
- **`security.md`.** `SEC-1…5` are cited by identifier in the modules I read (SEC-2 egress, SEC-4 consent, SEC-3 untrusted actor class, SEC-5 secret detection) but I read none of their text. Every SEC citation above is second-hand.
- **`architecture.md`, `trust-and-evidence.md`, `v1.md`, `doctrine/README.md` (the glossary).** `VIS-2` defines *aligned*, *converged*, and *genome-complete* by reference to `architecture.md`; the three-label rule, staleness, gap exits, and the work-warrant list live in `trust-and-evidence.md`. I have their consequences quoted inside the RFCs, never their own text.
- **All craft policy text.** No `CC-*` clause was read. The route lists no Craft row for this task class, and the two candidate craft policies are P-41/P-42.
- **The facet definitions.** The decision packet names six core facets inside an `[Inferred]` recommendation that "decides nothing." I have six words and no definitions, no constituent facts, and no evaluation semantics.
- **Current gate state.** I was told not to read `PROJECT-STATUS.md`, which the OVERVIEW names as the single authority for it. Everything I say about gate state above is from AGENTS.md and the decision packet, both of which defer to it.
- **Whether the eight heading groups are complete.** I have no denominator. I did not sweep the 30 Waves A+B modules for clauses governing registration or shape — I read exactly the five modules the route named. A claim that §2 covers Capability 1's observable consequences would be a claim of absence without a sweep, and I am not making it.
