<!-- Extracted under FD-037 on 2026-08-05 from _bootstrap/rfc-phase/OWNER-ANSWERS.md.
     From extraction onward, this tracked copy is the citable required source.
     Content below this header is byte-verbatim from the original. -->

> **Historical — superseded for current acceptance by
> FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md.** Preserved below as the record
> of its moment — unchanged except one bracketed correction marked
> "[Correction, rev7 review 9]" in the verification table; do not read
> statuses or counts here as current. The owner decisions recorded here
> remain the source record of what was decided.

# Owner answers — decision register walkthrough

**Session 2026-08-01.** Recorded as given. These are owner decisions on the
Tier A / Tier B items in `ACCEPTANCE-PACKET-ITEMS.md`. They do **not**
constitute `ACCEPT FOUNDATIONAL RFCS` — the gate remains open.

## Tier A

| # | Answer |
|---|---|
| A1 | **Ceremony + audit correlation.** No owner key custody. Each governance act minted in an owner-attended ceremony, correlated to an independently kept audit trail. **Derived constraint:** the audit trail must live outside `.syzygy/**` and outside the untrusted actor's write reach — the mechanism's defense is entirely contingent on that. |
| A2 | **Three admission routes, oracle bounded.** Syzygy-launched profiled run; externally confirmed CI run; owner-declared trusted oracle scoped to a named (project, gate class) pair and carrying an expiry. The oracle declaration is authorization-bearing, so A1 governs it. |
| A3 | **Gated, with a proven-stable carve-out.** Layout version change is an owner governance act with recorded rationale, except where the bump is shown position-preserving under the RFC2-3 determinism identity test, which needs only a recorded note. The stability check must be real, not asserted. |
| A4 | **Required, bootstrapped for sign-off.** Presentation profile required wherever Polaris renders; on first render Polaris drafts a default for owner sign-off — the RFC2-24 reason #1 resolution pattern. Declaration stays an act, so RFC1-7's "never presumed present" is not violated. |
| A5 | **Twelve reasons.** Add #12 `execution-blocked` (the execution that would produce the evidence was refused or prevented; resolved by unblocking or authorizing the run). #11 `reference-unresolvable` retained. **Settles B18** (primary reason, not a secondary annotation) and **B15** (unmapped substrate status stays #1 `missing-declaration`). |
| A6 | **Mint in the core vocabulary.** `declared-dependency`, Capability→Capability and Topology→Topology, state class Desired/declared, owner-adopted. RFC1-25 amended; anti-conflation rule extended from three senses to four. |
| A7 | **Add `placed_in`.** Topology entry → Capability, Desired/declared, minted by a governance artifact. Chosen because `part_of`'s own rule bars cross-authority nesting. Preserves the declared basis for the component-block level and the shared-infrastructure district. |
| A8 | **Accept the partition.** Thirteen work-state values in three partitions (8 live, 1 terminal `closed-unmerged`, 4 state-local absence values), each with a derivation row. |
| A9 | **Accept; render the gap honestly.** Ship a surface before the A1 mechanism exists; a fresh install renders contradiction-or-blocked-effect on every consent, adoption and policy until it lands. **Carried risk:** a visibly broken-by-design V0 invites pressure to soften the clauses that make it honest — compounds the review-5 "wall of Unknowns" product risk. |

## Tier B (answered so far)

| # | Answer |
|---|---|
| B15 | Settled by A5 — `missing-declaration`. |
| B18 | Settled by A5 — primary reason `execution-blocked`, not a secondary annotation. |
| B20 | **Reverted to `depends-on`.** Owner chose the original profile-relation name over `relies-on-project`. **Consequence, owner-informed:** the graph now carries `depends_on` (2 senses), `declared-dependency` (A6), and profile `depends-on` — three dependency relations, two one hyphen apart with different state classes. The names no longer separate them, so RFC1-25's anti-conflation rule becomes the sole separator and must be written as a checkable invariant, not prose. |

## Lead corrections made during the walkthrough

- **B18's packet text was stale.** It said "no contract names that secondary or says whether the secondary vocabulary is closed." RFC2-24 as fixed states the secondary vocabulary **is** closed and **is** the same eleven. The packet described a pre-fix state of the file. Same class as review 7's FX-1 Blocker; caught by reading the clause instead of the register.

## Tier B — full record

| # | Answer |
|---|---|
| B1 | **Eligibility + required sweep policy.** A challenge becomes expiry-eligible at its bound but keeps suspending until a recorded resolution act; the project **must** declare a sweep policy naming what resolves eligible challenges. Undeclared sweep = challenges stay suspended. The sweep policy is authorization-bearing (it converts suspended Unknowns to green), so A1 governs it. |
| B2 | **Deterministic check, human admission for machine-minted.** Kernel presence-check with declared latency bound for human-attributed challenges; inference-minted challenges additionally require human admission. Departs from the drafted position; closes the self-certification path where a declared inference process suspends claims at machine volume. |
| B3 | **Two-level identity; successor renders un-adjudicated.** Durable identity = (declared scope, ordered set of cited claim durable identities). A changed set mints a new durable identity citing its predecessor via `succeeds`; an adjudication binds exactly the identity it named, so a successor renders **un-adjudicated with the predecessor's adjudication cited** — a visible inheritance question, never a silent carry-over. Accepts the re-adjudication tax. |
| B4 | **Label now, force re-evaluation.** Revocation immediately obliges every served render to carry the withdrawal label **and** triggers a new evaluation rather than waiting for the next scheduled one. Truth still changes only inside an evaluation. |
| B5 | **Adopted operative, delta adjacent.** Adopted text is the operative leaf; the proposed delta renders adjacent, visually distinct, clearly unadopted. |
| B6 | **Asymmetric.** The authoring party may declare a change material, never immaterial. Only the owner rules something immaterial. |
| B7 | **Obligations fixed, counts default.** The contract binds what must be disclosable per altitude and band; five altitudes / three bands are the V0 default, not a frozen constraint. |
| B8 | **Per (project, provider).** One consent record per pair, naming permitted content classes inside it. |
| B9 | **Credential only.** No device binding; session identity is the credential. **Derived constraint:** session lifetime and revocation are now the *entire* mitigation for a stolen session — RFC 0005 must state both as binding obligations, not defaults. |
| B10 | **Mint `editorial-draft`.** A distinct sibling surface state for narrative prose in revision. **Mechanical consequence:** the sibling surface states go from two to three; four cross-file enumerations reading "the two sibling surface states" must be amended. |
| B11 | **Derive, disclose collisions.** Adapter-derived run identity, with `indistinguishable-runs` and an Unknown count on collision. Never a silent single record. |
| B12(a) | **Adjacency may express declared relatedness.** Reverses the drafted "proximity inert" position. Requires the new tiebreak below. |
| B12(b) | **Release gate, with attributed judgment.** The comprehension walkthrough blocks release; a pass or fail must name the judging party and record rationale, so a false pass is findable. |
| B12(c) + B17 | **Free to use, owner act to promote.** One rule for lenses, analytical planes, and profile relations alike: personal definition and use is free; promotion to a named, governed, versioned artifact is an owner governance act under A1. A single predicate, not a per-kind enumeration. Directly applies FD-029. |
| B13 | **Declared per-project, fail closed.** The inherited-mutation threshold is quality-policy material: obligation binds now, value is owner-set per project, **undeclared means no inherited mutation is permitted**. Absence renders as absence, never as a permissive default. |
| B14 | **Derived rendering, not a Claim.** Carries its own separately-counted absence values (per A8's partition) rather than RFC2-24 Unknown reasons. Board-state absences never enter project Unknown-reason counts. |
| B15 | Settled by A5 — `missing-declaration`. |
| B16 | Retired (see `ACCEPTANCE-PACKET-ITEMS.md`). |
| B18 | Settled by A5 — primary reason `execution-blocked`. |
| B19 | **Fifth reserved category: kernel-authored records.** Durable facts the kernel authors on an actor's submission (admission records, challenge lifecycle events). Also resolves the carried residual strain — RFC3-2's three write-authority classes gain a fourth for actor-triggered kernel facts, rather than the Syzygy-maintained-with-challenger-as-field workaround. |
| B20 | **Reverted to `depends-on`** (see Tier A section for the consequence). |
| B21 | **Relaxation granted.** RFC9-10(c)'s "always available and discoverable … not any particular interaction cost" stands; SDR-21's "one action back to home" is relaxed. **Sequencing note:** craft-and-care still carries the stricter wording and must be amended to match — and craft-and-care is approved under D2, so the amendment lands after approval. |
| B22 | **Accept substance, fix the process.** The governance-root adjustment stands; any future divergence from owner-ratified text becomes a surfaced item, never an inline note. |

## New decision created during the walkthrough

| # | Answer |
|---|---|
| N1 | **Layout tiebreak — stability wins, adjacency best-effort.** Created by B12(a): append-stability and declared adjacency are now both binding and mutually unsatisfiable. Resolution: positions never move; adjacency is satisfied where the layout allows; **the map renders which adjacency declarations are currently honored and which are not.** Had this gone unasked, the tiebreak would have been chosen silently by whoever implemented the layout. |

## Separate gates

| # | Answer |
|---|---|
| D1 | **Adopt; historical bundle stays dormant.** The two-line doctrine amendment is adopted. Ghost-step opacity, milestone scenes and the time scrubber stay behind their own review — "the map may show history" and "here is how history looks" are separated. |
| D2 | **Approved.** Craft-and-care cluster approved. |
| D3 | **Ratified** via D2 — "liberal experimentation, disciplined promotion". |
| D4 | **Ratified** via D2 — the unified same-change rule. |

## Tier C items promoted and answered

| Item | Answer |
|---|---|
| RFC 0002 §8 q4 | **Both, as one paired state.** The warranted-revision binding stands; the pair must render as a single explained state ("reconciled against what was approved; N gaps against what you just changed"), never as two independent numbers the reader must reconcile. |
| RFC 0002 §8 q3 | **Deterministic check qualifies.** A deterministic, re-runnable diff-satisfies-clause check is a lawful `gate-backed` route for doc-only and governance-only work. Adds a fourth route to A2's list; "deterministic check" needs a real definition or it becomes the loosest route. |

## Remaining Tier C

21 items unanswered and deliberately so — either answer leaves the accepted
contract standing. They ride on the drafted defaults.

## N1 superseded — the refresh model (owner-proposed, 2026-08-01)

The owner replaced the bare N1 tiebreak with a stronger model after seeing the
conflict stated. **Recorded as superseding N1, not amending it.**

**The model.** Location and proximity are *fixed* within a layout version and
*manually refreshable* between versions. Incremental declarations never
relocate anything; a full regeneration of base locations, run as an owner act,
discharges the accumulated adjacency backlog. Topology evolves over time
without incremental change overhauling the layout.

| Aspect | Decision |
|---|---|
| Within a version | Append-stability absolute. Nothing moves. Declared adjacency is satisfied where the layout allows and rendered honored / not-honored where it does not. |
| Refresh scope | **Full regeneration.** Every district repositioned from the current declaration set. |
| Refresh trigger | **Owner act only** (the RFC9-16(d) / A3 gated layout-version change). No automatic relayout. The map surfaces the accumulated unsatisfied-adjacency backlog so the owner can see when a refresh is worth running. |
| Determinism | **Both** base regeneration **and** incremental append placement must be pure functions of (declaration set, layout version) — never of insertion order. |

**Why this is better than the option originally offered.** [Inferred, and the
reasoning is the lead's, not the owner's — the owner proposed the model, this
is why it holds.] Append-stable *incremental* placement is **order-dependent**:
if a district lands wherever there was room when it was added, the layout is a
function of history rather than of the declaration set. Two conforming
implementations given the same project in a different order then produce
different maps — and RFC6-22/23 make two renderings disagreeing over one
declared scope release-blocking under the trust floor. Periodic full
regeneration restores the layout to a pure function of (declarations, version).
Scoped/partial regeneration was rejected by the owner for the same reason: it
would make the layout a function of refresh *history* as well.

**Consequence:** the unsatisfied-adjacency backlog is a first-class rendered
quantity, not an incidental one — it is the only signal telling the owner a
refresh is due.

## Anchoring question raised and closed (2026-08-01)

Owner asked whether zones should correlate to tests, core modules, etc.
**Closed against adopted doctrine, not by this gate:** `architecture.md` anchors
map geography to **capability identity, not file paths**, because code
structure relocates on refactors that changed nothing about what the project
does. The instinct is served by three existing mechanisms rather than by
re-anchoring: core modules are **declared as topology entries** and placed via
A7's `placed_in` (becoming the RFC9-4 component-block level); tests drive
**inhabitation** (RFC9-27 earned emptiness, coverage records), not position; and
a module- or coverage-shaped view is an **analytical plane**, whose authority
B12(c) already settled. No new decision required.

---

# Amendments applied — 2026-08-01

All owner decisions above are now in the artifacts. **Twenty-two clause-level
amendments across eight RFCs, craft-and-care, and doctrine.** No clause was
renumbered or deleted; new material is lettered sub-clauses per the standing
rule.

| Artifact | Amendment | Decision |
|---|---|---|
| RFC1-25 | `declared-dependency` minted (Capability→Capability, Topology→Topology, Desired/declared) | A6 |
| RFC1-25 | `placed_in` minted (Topology entry → Capability, Desired/declared) | A7 |
| RFC1-25 | `depends_on` row rewritten: four senses, no third endpoint pair | A6/B20 |
| **RFC1-25(a)** *(new)* | Records that both relations are owner-decided amendments, not drafter additions | A6/A7 |
| **RFC1-25(b)** *(new)* | The dependency anti-conflation invariant — four senses, **twelve ordered pairs, mechanically checkable**, named test-coverage obligation of the first slice | B20 |
| RFC1-26 | Closure amended to admit the two; a relation may be added **only** by amendment carrying an owner decision | A6/A7 |
| RFC2-24 | **Twelve reasons, closed** — #12 `execution-blocked` added with its own resolution route | A5 |
| RFC2-13 | Sweep policy **required** wherever expiry is declared; undeclared = challenges keep suspending (fail closed); policy is RFC3-16(a)-bound | B1 |
| RFC2-13 | Admission **split by minter**: human → deterministic check; inference-minted → deterministic check **plus recorded human admission** | B2 |
| RFC2-18 | Warranted/current revision claims must render as **one paired state**, never two independent aggregates | Tier C q4 |
| RFC2-25 | **Three** sibling surface states — `editorial-draft` minted on RFC 0007's own reported distinction | B10 |
| RFC3-2 | **Fourth** write-authority class: `kernel-recorded`; never authorization-bearing | B19 |
| RFC3-15 | **Fifth** constitutional category: `records/` | B19 |
| **RFC3-15(a)** *(new)* | Why the fifth category exists; why `cache/`/`local/` cannot hold an identity-bearing snapshot input | B19 |
| RFC4-13 | Oracle route **bounded** — scoped to (project, gate class) with an expiry; **route 4** added (deterministic diff-satisfies-clause check) | A2 + Tier C q3 |
| RFC5-4 | Session identity is the credential alone; **declared max lifetime** (undeclared = no persistence beyond process) and **immediate revocation** now binding | B9 |
| RFC5-11 | Revocation **forces a new evaluation**; reconciled with RFC2-4 (schedules, does not mutate) | B4 |
| RFC5-18 | Blocked execution renders primary `execution-blocked` | A5 |
| RFC7-5/6 | Profile **required**, and Polaris **drafts a default for sign-off** — reconciles with RFC1-7 rather than overriding it | A4 |
| RFC8-25 | "Small" is a declared per-project threshold that **fails closed** | B13 |
| RFC9-9 | Proximity carries **two** declared readings (containment + declared relatedness); shortfall renders **not-honored** | B12(a) |
| **RFC9-9(a)** *(new)* | The legend has **three** lines: the two declared readings plus **residual adjacency — carries no meaning**, which must be reader-decidable and must not counterfeit containment | review 8 ML-R3 |
| **RFC9-9(b)** *(new)* | honored / not-honored / unknown is a **registered channel** with epistemic class, evidence path and mandatory Unknown value | review 8 ML-R5 |
| **RFC9-8(a)** *(new)* | The portfolio gets the reorganisation machinery it inherited the obligation from, held in the workspace manifest | review 8 ML-R15 |
| **RFC9-13(a)** *(new)* | Coordinate-bearing personal state is version-stamped and **never restores silently** across a layout version change | review 8 ML-R12 |
| **RFC1-25(c)** *(new)* | `placed_in` is **not functional** and carries no primacy marker; two edges are a declared placement contradiction, never a tie-break | review 8 ML-R8 |
| **RFC9-15(b)** *(new)* | Fixed locations, manually refreshed: nothing moves within a version; regeneration is **full**, owner-run; **both placements are pure functions of the layout input tuple — (declaration set, layout baseline, layout version)** — insertion order is never an input; backlog surfaced, **partitioned** into refresh-clearable and structurally unhonorable | owner-proposed model; corrected after review 8 |
| RFC9-16(d) | Owner-gated, with a carve-out **narrowed at the owner's direction after review 8** to versions demonstrated to be the *same placement function* — agreement on every input, not on one declaration set — established by a recorded **layout-equivalence check** (not the RFC2-3 identity test, which was miscited). An asserted exemption is not a carve-out | A3, narrowed after ML-R2/ML-R7 |
| RFC9-45 | Comprehension test is a **release gate with attributed judgment**; the record names what was walked (evaluation, layout version, baseline, scenario, lens, filter scope) and the gate is **fail-closed** — an unlawful verdict blocks release rather than clearing it | B12(b) + review 8 ML-R10/R11 |
| craft-and-care CC-VIZ-5 | "One action back" superseded by the granted relaxation; layout purity and the refresh model added | B21 + model |
| `doctrine/architecture.md` | `map/` includes **historical** system state (two sites) | D1 |

## Defects discharged rather than left standing

- **RFC 0009 §5 defect 1** (both halves) — discharged by A7 and A6.
- **RFC 0007 §5 defect 1** — discharged by B10.
- **RFC 0009 §4 violation case 3** rewritten; **case 3a** added for the refresh model.

## §8 question status

**36 of 57 answered and marked in place; 21 remain open** — the Tier C set,
riding on drafted defaults. An answered question left rendered as open is the
same failure as a stale defect report, so each answer is recorded at its
question rather than only in this file.

*(The count moved from 37 to 36 for a reason worth recording: one of the 37 was
an **orphan** — RFC 0009 q10's B21 annotation had landed after the document's
`End of RFC` marker, so q10 itself read as unanswered while the tally counted
it. The earlier placement check verified that placed annotations sat at block
boundaries and never asked whether one had landed outside its section. Orphan
removed, q10 annotated in place; the real total was 36 all along.)*

## Verification after amendment

| Check | Result |
|---|---|
| Clause ranges close, no gaps | ✓ 290 clauses, 1..n in all nine |
| Nothing renumbered or deleted | ✓ same 290 |
| Cross-RFC citations resolve | ✓ 2165 scanned, 0 unresolved (re-run after review 8) |
| Stale counts (eleven reasons, three routes, two sibling states, four categories, three write classes, `relies-on-project`) | ✓ swept; surviving matches all describe rejected or historical positions. **[Correction, rev7 review 9]** This sweep was incomplete when recorded: RFC6-14 and RFC9-43 still enumerated *two* sibling surface states (omitting `editorial-draft`, B10). Both fixed in the rev7 rework; finding S2/F3 in `reviews/09-rev7-semantic-RAW.md` / `09-rev7-fidelity-RAW.md`. |
| Answer annotations at block boundaries | ✓ 36/36 clean, none outside its section (an earlier pass split wrapped headers mid-sentence and left one orphan past the end marker; both fixed) |

## Review 8 — the map-layout cluster

The redesign B12(a) forced and the refresh model you proposed had been seen by
no reviewer. A fresh-context review of RFC9-9 / RFC9-15(b) / RFC9-16(d) /
RFC9-45 returned **REVISE — 3 Blockers, 10 Majors, 2 minors, 2 Nits**. All 17
findings were accepted and fixed; none was overruled. Dispositions and the fix
report: `reviews/08-map-layout-DISPOSITIONS.md`; raw output unchanged at
`reviews/08-map-layout-RAW.md`.

Two things you should see rather than have summarized away:

1. **ML-R1 falsified something I told you.** I said your refresh model removed a
   latent order-dependence, and wrote the clause as a pure function of two
   inputs. The reviewer proved a third input exists — the layout **baseline** —
   and that parts 2 and 3 of your model are jointly non-vacuous only if the
   two-input form is false. Your model was fine; my statement of it was not.
   Fixed at RFC9-14(a), with the falseness recorded in place rather than
   quietly corrected.
2. **ML-R2 needed your decision, and you took it** — narrow the carve-out to
   *identical placement*, agreement on every input rather than on one
   declaration set. The consequence you accepted: almost every real layout
   change is now owner-gated.

**One decision I made on your behalf and am flagging:** ML-R8 exposed that
`placed_in` had undefined cardinality. I resolved it by applying the rule you
had already ratified at RFC9-20 — a renderer never answers a governance
question — rather than putting it back to you: two `placed_in` edges are a
declared contradiction, rendered Unknown-placed with an adjudication route, and
no tie-break is lawful. If you would rather `placed_in` be **functional** (at
most one, enforced by the kernel at declaration time), say so and RFC1-25(c)
changes; the difference is whether a conflicting declaration is *rejected at
write* or *recorded and surfaced*, and the second is the one that matches the
rest of the kernel.

## Still outstanding

- **The gate itself.** `ACCEPT FOUNDATIONAL RFCS` has **not** been written and
  nothing here presumes it.
