# RD-26 — Wave A dimension review (round-2026-08e) — RAW
- Review id: RD-26
- Date: 2026-08-10
- Subject: Wave A — RFC 0001–0006 + launch-critical owner decisions
- Frozen commit: aaff6fa
- Reviewer: isolated fresh-context session, Claude family (Fable 5). Same-family review — not the gate's family-diverse formal administration.
- Authoring context: none

---

## 0. Denominator — what I actually read and ran

**Wave A modules read in full: 19 of 19** (the population is `wave-manifests/WAVE-A-MANIFEST.txt`, whose 19 rows I enumerated and verified against the tree):

| # | Module | # | Module |
|---|---|---|---|
| 1 | `rfcs/RFC-0001-project-graph-identity-state-planes.md` | 11 | `rfcs/RFC-0004/README.md` |
| 2 | `rfcs/RFC-0002/README.md` | 12 | `rfcs/RFC-0004/general-contract.md` |
| 3 | `rfcs/RFC-0002/snapshot-and-evaluation-core.md` | 13 | `rfcs/RFC-0004/named-adapters.md` |
| 4 | `rfcs/RFC-0002/challenge-lifecycle.md` | 14 | `rfcs/RFC-0004/execution-record.md` |
| 5 | `rfcs/RFC-0002/reconciliation-chain.md` | 15 | `rfcs/RFC-0004/fidelity-joins-and-mappings.md` |
| 6 | `rfcs/RFC-0002/rendering-vocabularies.md` | 16 | `rfcs/RFC-0005/README.md` |
| 7 | `rfcs/RFC-0003/README.md` | 17 | `rfcs/RFC-0005/admission-and-boundary.md` |
| 8 | `rfcs/RFC-0003/manifests-and-namespace.md` | 18 | `rfcs/RFC-0005/consent-egress-secrets.md` |
| 9 | `rfcs/RFC-0003/governance-homes-and-owner-acts.md` | 19 | `rfcs/RFC-0005/execution-profiles.md` |
| 10 | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md` | | |

*(Row 10 is `RFC-0006`; the table is column-ordered, not manifest-ordered.)*

**Doctrine read in full: 6 of 6** — `README.md`, `vision.md`, `architecture.md`, `trust-and-evidence.md`, `security.md`, `v1.md`.

**Decision packets.** `PENDING-OWNER-DECISIONS.md` read by section headings plus every `P-*` row in full (P-1…P-5, P-6…P-13, P-26, P-10…P-40 — 34 rows extracted). From those rows, the pending decisions Wave A clauses or the Wave A act actually lean on are **P-1, P-17, P-18, P-21, P-28, P-31, P-33, P-36, P-37, P-39, P-40**. Packets read in full: `WAVE-A-INSTALL-SHAPE-DECISION.md` (P-33), `UNKNOWNS-AND-GAPS-DECISION.md` (P-36), `PROJECT-SHAPE-FACETS-DECISION.md` (P-37), `OPENSPEC-FORM-AND-VERSION-DECISION.md` (P-39), `SPECIFICATION-GRANULARITY-DECISION.md` (P-40), `DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md` — **6 packets**. `OWNER-ANSWERS-2026-08-01.md` read in part: header, Tier A table (A1–A9), Tier B table (B1–B22), the RFC-consequence table rows for RFC2-24/RFC3-2/RFC4-13, plus targeted `grep -F` sweeps. **8 of 16 files in `decisions/` were not read** (`HUMAN-ENTRY`, `KNOWLEDGE-HYGIENE`, `LAUNCH-GATE-AUTHORITY`, `LICENSE-DECISION-PACKET`, `PROJECT-OPERATING-CONSTRAINTS`, `PROCESS-LESSONS`, `SURFACE-DECISION-RECORD`, `launch-gate/`) — none is cited by a Wave A clause. `[Observed]`

**Also consulted:** `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` (§1, §1a, §2, §3, §5, §6 tail, §7 in full), `WAVE-A-MANIFEST.txt`, `ACTIVE-CONTRACT-MANIFEST.txt` (banner), `SURFACE-CLAUSE-ROUTING-MATRIX.md` (header + machine-extracted RFC6 rows).

**Sweeps and checks run this session** (each with its denominator):

| Check | Result |
|---|---|
| `sha256sum -c` over all 19 Wave A manifest rows | **19/19 OK** `[Observed]` |
| Manifest self-digest vs acceptance-record §1 Wave A argument | `6b98e0c6…add16b4d` — **match** `[Observed]` |
| Python `re` over `SURFACE-CLAUSE-ROUTING-MATRIX.md` for `RFC6-n` row anchors | **28 of 28 present, 0 missing** `[Observed]` |
| `grep -F "P-31"` and `grep -F "P-33"` over the acceptance record | **0 hits each** `[Observed]` |
| `grep -nF route\|checker\|fourth` over `OWNER-ANSWERS-2026-08-01.md` | 3 route hits, **0 "checker" hits**, 3 "fourth" hits `[Observed]` |
| `python3 scripts/check_governance.py` | **29 OK, 19 WARN, 0 FAIL (48 checks)** `[Observed]` |
| `python3 …/scripts/verify_final_prespec.py` | **PASS**; 341 numbered clauses, 39 modules, **11 phase-rule clauses** `[Observed]` |

Both validators are green. Every finding below survives them, because none of them is a thing these scripts check. `[Inferred]`

---

## 1. Typed authority

Each of the 19 modules carries the same status banner — *"Effective status is established solely by an owner-act record binding this file's exact content digest"* — plus front-matter `governs` / `applies_to` / `depends_on`, and a `Serves:` line naming the doctrine rules above it. **19 of 19 modules carry all four.** `[Observed]` No module self-elevates: RFC3-16's *"A tree-resident stamp is **never self-authenticating**: `accepted` written in a file is a claim by whoever wrote the file, not proof of acceptance"* is the strongest statement of this in the corpus and every module's banner defers to it.

I swept the 19 modules for clauses treating a candidate, index, or generated view as authority. **Zero found.** The near-misses each disclaim themselves in their own text: RFC3-15's `contracts/` install-gate cell says *"that record owns the acts, their exact phrases, and their arguments, and this clause quotes none of them"*; RFC1-33 and its five siblings say the coverage matrix *"is review material, never authority"*; RFC-0002's README opens *"If this map and a clause disagree, the clause wins."* `[Observed]`

One doctrine-versus-clause seam, disclosed as P-18(a) but not carried into the acceptance record's owner-attention list — **RD26-13** below.

`depends_on` closure holds: every Wave A module's declared dependencies name only RFC-0001…0006, so the acceptance record's claim *"Every `depends_on` edge of these contracts stays inside the wave"* checks out across all 19. `[Observed]` RFC-0004 and RFC-0005 declare each other, which is circular but harmless inside one act.

## 2. Registration

The identity chain is internally consistent across four clauses. RFC1-1: *"A **Project** is one or more repositories with exactly one designated **governance root** … and one owner."* RFC3-4: *"A repository carries at most one `.syzygy/` plane, at its root, and is the governance root of at most one Project."* RFC3-29 forbids sub-roots; RFC3-30 makes role and consent *"properties of the *(Project, repository)* pair … never global"*, which is what lets one repository be a governance root and another project's observed source without leaking consent. Rename behavior is single-sourced at RFC1-10 — *"renaming the thing changes its label, never its identifier"* — and RFC3-5's `project` row cites it rather than restating it. `[Observed]`

**What registration observably produces is not stated by any Wave A clause**, and this is deliberate: RFC1-33 lists *"project registration and declaration validation flows"* among the observable consequences that must map to an approved OpenSpec requirement before implementation. I swept all 19 modules for a clause defining registration's observable output and found none. `[Observed]` That is staging, not a defect — but see RD26-12, because the enumeration that would carry it does not exist for RFC 0001–0005.

One real contradiction on the zero-roots case — **RD26-03**.

## 3. Evidence

The evidence model is the strongest part of Wave A. The `no evidence → Unknown` rule is stated once per layer and cited, not forked: VIS-2 → RFC1-19 → RFC2-24's twelve closed reasons → RFC2-25's six closed tiers, of which *"`gate-backed` … The **only** tier that may support a positive status claim"*. Absence-never-zero is carried at three independent sites (RFC2-23 *"**Unknown, never zero** (SDR-6)"*; RFC4-19's `tokens / cost` row; RFC4-20's `indistinguishable-runs` run-count rule). RFC4-27's *"an unexecuted mapping is not evidence of absence"* closes the empty-plot path. RFC4-13's four-route provenance predicate and its *"Format, retention, and hash-carrying prove **non-tampering, not genuineness**"* is the clearest single sentence in the wave. `[Observed]`

I swept the 19 modules for a clause under which absence could read as success and found **one** — RFC4-19's `terminal outcome` row, **RD26-05**. I also found one clause pair that disagrees about whether a suspension can end without an act (**RD26-04**), and one normative paragraph that is explicitly not yet ruled (**RD26-06**).

## 4. Consent and authority scaling

Authority scales to irreversibility correctly and I could not find a routine path to an irreversible effect. Execution is a five-part gate (RFC5-18) whose limb (c) requires the approval Decision's *"owner-act provenance the gate cross-checks under RFC3-16(a) before launching"*; egress is a single choke point with a three-part check (RFC5-15); destructive operations are default-blocked with an always-human class mirroring VIS-4 (RFC5-22); materialization is one-way and constitutive at the record (RFC1-29). RFC5-24's injection prohibition plus RFC5-20's network-policy exclusion give the stated *"no credential to Syzygy, and no route to Syzygy"*. RFC3-16(a)'s fourth limb is honestly labelled as the vague one: *"a predicate that reaches only the failures already found is an enumeration wearing a predicate's clothes."* `[Observed]`

Non-delegability is explicit everywhere I checked. The one place a machine gets admission authority — RFC2-13 — splits it by owner decision B2 so that *"The declared inference process … [needs] The deterministic kernel check **and** a recorded human admission act"*, and the recorded B2 text matches. `[Observed]`

The defect in this dimension is not in the clauses. It is at the gate: **RD26-02**.

## 5. Shared facts

Wave A's cite-don't-restate discipline is real and mostly holds. RFC2-24's rendering rule says of RFC6-17: *"The obligation is cited here, not restated, so the two cannot drift."* RFC3-32 says the same: *"cited here, never restated."* RFC3-19 restates a schema consequence and says so: *"The obligation is stated once, in RFC 0001 (RFC1-29 …); this clause restates its schema consequence and requests no amendment."* `[Observed]`

I looked specifically for two clauses answering one question differently. **I found two such pairs** (RD26-03, RD26-04) and three citation defects (RD26-07, RD26-08, RD26-09).

## 6. Installation

The mechanical half verifies. All 19 per-module digests match the tree at `aaff6fa`, and the manifest's own sha256 matches the §1 Wave A argument exactly. The ceremony's step 2 is executable as written from a clean clone. `[Observed]`

The semantic half does not. **RD26-01** is blocking: the install the act performs violates a clause the same act binds, and the owner's own packet says so.

## 7. OpenSpec routing

RFC-0006's routing is complete and consistent: **28 of 28 clauses carry exactly one route**, 27 OS and 1 CR, and RFC6-28 — the phase clause — is the CR row, which is the right answer for a clause whose consequence is a process obligation rather than a rendered behavior. I checked the routes against the clause text for the six clauses whose observable consequence is least obvious (RFC6-6, RFC6-7, RFC6-12, RFC6-20, RFC6-21, RFC6-25) and each row's route matches what the clause actually obliges. `[Observed]`

The gap is the other 18 modules — **RD26-12**.

---

## Findings

### RD26-01 — BLOCKING — the Wave A install breaches RFC3-15, the clause the same act binds

The acceptance record's step 3 installs, into `.syzygy/governance/contracts/`: the manifest's modules under `rfcs/`, the wave manifest under `wave-manifests/`, `ACTIVE-CONTRACT-MANIFEST.txt`, and — *"Companion material, installed but not accepted"* — `history/`, `matrix-rows/`, `CONTEXT-BUDGET-REPORT.md`, and `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`.

RFC3-15, bound by that same act, opens: *"The **five** constitutional categories of `.syzygy/governance/` hold, **exclusively**"* — and its `contracts/` row's *May contain* cell reads, in full: *"Accepted load-bearing contracts (RFCs), including normative data contracts and external service contracts."* None of the seven installed companion items is an accepted load-bearing contract. The record's own defense — *"These directories are **non-normative** … sit outside every act's accepted digest set, and carry no authority"* — answers a different question: RFC3-15's "exclusively" bounds **what each category may contain**, not what it may bind.

Three aggravations, each independently checkable:
1. The act's **own apparatus** is inside the breach — `wave-manifests/` and `ACTIVE-CONTRACT-MANIFEST.txt` are not contracts either, and step 3 installs both into `contracts/`.
2. The breach is **immediate, not prospective**: `.syzygy/governance/contracts/candidates/` already exists in every clone, so the instant RFC3-15 binds, the tree it governs contains a non-contract subtree — and the ceremony does not retire it (for topology it says explicitly *"does **not** delete `topology-candidates/`"*). `[Observed — the path exists at aaff6fa]`
3. **The owner has already been told this is unruled and has not ruled.** `WAVE-A-INSTALL-SHAPE-DECISION.md` (P-33) states in its own banner: *"It must be ruled **before Wave A is re-offered**: both defects are properties of the install ceremony an act would freeze, unrepairable after binding,"* and under *Consequences of not ruling*: *"Wave A cannot be re-offered."* P-33 is listed under **"Open, and only the owner can dispose"** in `PENDING-OWNER-DECISIONS.md`, unruled at this commit. `[Observed]`

One-line direction: rule P-33 (the packet's own recommendation is 1b — the RFC3-15(a) recorded-widening route) and rewrite step 3 to match before the offer.

### RD26-02 — BLOCKING — three questions whose own earliest gate is the Wave A act are absent from the gate document

The acceptance record's §7 is titled *"Items requiring explicit owner attention at the gate"* and carries ten items. `grep -F` over the whole record returns **zero hits for "P-31" and zero for "P-33"**. `[Observed]` P-37 likewise appears nowhere. Each of the three names the Wave A act as its own gate:

- **P-33**: *"Earliest gate: before Wave A is re-offered"* (and see RD26-01).
- **P-31**: *"Recommendation `[Inferred]`: draft the exemption arm; **ruling wanted before Wave A is re-offered** so the drafted arm is ratified knowingly."*
- **P-37**: *"Earliest required gate: **Wave A act** (RFC-0006 is in Wave A); the ruling is cheapest before the Wave A re-offer."*

§7 does disclose three other Wave A items (RFC 0003 §8 q4, the [Inferred] SEC-3 extension, RFC 0005 §8 q1), which shows the section is meant to carry exactly this class. The three above were not added. An owner reading §1's Wave A row and §7 in full would perform the act without learning that it ratifies a drafted exemption arm (P-31), settles the shape vocabulary (P-37), and freezes an install ceremony whose own packet says the act cannot be offered (P-33). This is the RD-8 defect class AGENTS.md records — *"the finding that converts act 1 from a knowing act into a surprised one"* — with three instances. `[Observed for the absence and the three quoted gate lines; Inferred for the characterization]`

One-line direction: add P-31, P-33 and P-37 as §7 items with their options, or rule them.

### RD26-03 — MAJOR — RFC3-4 and RFC1-1 answer the zero-governance-roots question in opposite directions, and RFC3-4 cites RFC1-1 for the answer RFC1-1 rejects

RFC1-1, stating the case at length precisely because it is the hard one:

> *"**Zero roots** is not: with no designated governance root there is no declared home to read the declaration from and no snapshot anchor for it, hence no Project evaluation in which to mint anything. That case surfaces at the **workspace/manifest level** — unevaluable as a Project, rendered Unknown (`missing-declaration`) in the observing workspace, **with no kernel contradiction minted**: an evaluation is identified by a Project's (source snapshot, as-of instant) and by nothing else (RFC2-3), and the workspace manifest is barred from being a snapshot input, so there is no evaluation context in which a kernel contradiction could exist."*

RFC3-4, third sentence:

> *"A declaration purporting to designate a *different* repository as root, or **a Project resolving to zero or two roots, is a contradiction per RFC1-1** — routed to the owner, never repaired silently."*

RFC1-1 spends five lines proving no kernel contradiction can exist for zero roots; RFC3-4 asserts that one does, and attributes the assertion to RFC1-1. Two conforming implementations reading the two clauses produce different graphs for an undeclared project — one mints a Contradiction entity requiring owner adjudication, the other renders Unknown with reason #1 in the workspace and mints nothing. Under RFC6-23 that divergence is release-blocking. Note that RFC3-4's *two*-roots limb is correct; only the *zero* limb forks. `[Observed]`

One-line direction: narrow RFC3-4's limb to two roots and route zero to RFC1-1's workspace path by citation.

### RD26-04 — MAJOR — challenge expiry: RFC 0003 says it derives and mints nothing; RFC2-13 says it requires a recorded act, and RFC 0003 gives that act no home

Two limbs, both anchored.

**(a) The clauses disagree.** RFC3-2:

> *"**Kernel-computed expiry** — a challenge lapsing because its declared bound has passed (RFC2-3, RFC2-13) — is **derived state computed at each evaluation** from the admission record's instant and the declared bound; it mints **no record**, because it involves no act and is reproducible from snapshot inputs the tree already holds."*

RFC3-15's `records/` cell repeats it (*"kernel-computed expiry derives at evaluation and mints nothing"*) and RFC3-16's lifecycle table repeats it again (*"plus withdrawal, supersession, or **derived expiry** where its governing contract defines them (RFC2-13)"*). RFC2-13 says the opposite about the state transition:

> *"An expiry-eligible challenge **continues to suspend** the claim until a recorded resolution act — a human, or the pre-declared deterministic policy sweep — resolves it as `expired`; that act is an authoritative input of a **new snapshot** … **Automatic expiry at the instant is not available**: it would improve a claim over an unchanged snapshot by pure passage of the as-of instant."*

RFC 0003's phrase is readable as *eligibility* derives (consistent) or as *the challenge lapses* by derivation (RFC-0002 violation case 10 verbatim: *"An admitted challenge un-suspends its claim at its declared expiry instant with no recorded resolution act and no new snapshot"*). The two readings differ on whether a suspension can end without an act — a safety-relevant difference decided today by which clause a reader loads first. Owner decision B1 is on RFC2-13's side: *"A challenge becomes expiry-eligible at its bound but keeps suspending until a recorded resolution act."*

**(b) The act RFC2-13 requires has no lawful home.** The sweep resolution must be *"an authoritative input of a **new snapshot**"*, so it is durable and identity-bearing, and RFC3-20/21 bar `cache/` and `local/`. RFC3-15's `records/` category admits *"Kernel-authored durable facts minted on a non-owner actor's submission (**the only minting trigger**)"* — a deterministic policy sweep is no actor's submission. `decisions/` holds *"Recorded owner decisions"* — a policy sweep is not an owner act; RFC3-17(a) confirms *"**Resolution acts that are owner acts** … are recorded in `decisions/`"*, which by construction excludes the non-owner branch RFC2-13 explicitly authorizes (*"a human, **or** the pre-declared deterministic policy sweep"*). `policies/` holds the policy, not its executions. I swept all five categories plus the reserved sixth: **no category admits it.** `[Observed]` The consequence is fail-closed (suspensions stand forever) rather than unsafe, but the `expired` state RFC2-13 defines and owner decision B1 required is unreachable in Wave A's own namespace contract.

One-line direction: say "expiry *eligibility*" in RFC3-2/3-15/3-16 and give the sweep resolution record a named home and write authority.

### RD26-05 — MAJOR — a vanished-worker run produces no admissible Execution Record, so the run is dropped

RFC4-19 defines **R** as *"required (record inadmissible without it)"* and classes `terminal outcome + blocker set` as **R**, with the value domain fixed as *"The toolchain's closed report-status vocabulary, transmitted verbatim with the substrate qualified."* A worker that vanishes emits nothing, so no value exists to transmit verbatim, so the record is inadmissible, so the run leaves no Execution Record at all.

That collides with three rules in the same package. RFC4-19's own `work item identity` row: *"Unattributable runs are admissible only rendered as unattributed execution noise, **never dropped**."* RFC4-16(3): *"A fact lost to the horizon before capture renders **Unknown citing the retention event** — never silently absent."* And VIS-2, since a fleet account over such runs is complete-looking while a run is missing from it.

The package discloses this rather than repairing it — §8 q2, **OPEN**: *"a run whose worker vanished without any report would then be recordable only as an `unknown-terminal` outcome value. Should the envelope instead admit records with outcome Unknown-by-reason, keeping R for the field but not the value? Proposed: yes."* `unknown-terminal` is not in any toolchain's vocabulary, so the "recordable only as" branch is not available under the row as written. Disclosure mitigates; it does not close the hole the act would bind. `[Observed for the clause texts; Inferred for the composition]`

One-line direction: rule §8 q2 in the proposed direction (field required, `unknown-terminal` a legal Syzygy-side value) before the offer.

### RD26-06 — MAJOR — a normative module carries a paragraph explicitly awaiting an owner ruling, on the corpus's flagship V0 rendering

RFC2-19 carries an unmarked-normative arm — *"the `reconciliation-pending` state and the 'reconciliation evidence absent / Unknown' rendering it produces are **never stamped with, counted among, or absorbed by an aggregate of RFC2-24 Unknown reasons**"* — immediately followed by:

> *"**[P-31 — drafted arm, awaiting an owner ruling.]** … Two routes close it: a thirteenth RFC2-24 reason, which reopens a list owner decision A5 closed at twelve and is an owner act, not a drafting one; or the exemption above … it is candidate text like every clause around it, and the owner ratifies or reverts it at the act that binds this module."*

The arm is self-consistent — it composes with RFC2-18's chain states, RFC6-17's per-chain-state counts, and RFC6-6's parallel exemption for navigation outcomes, and I found no clause it breaks. The defect is that it materially narrows RFC2-24's *"Every Unknown claim instance carries exactly one primary reason from this list"* for the single state a fleet-built project renders most, and it does so on drafting authority. The block quote's honesty is the right posture and is why this is MAJOR rather than BLOCKING — but the honesty lives inside the module, not at the gate, which is why RD26-02 exists. `[Observed]`

One-line direction: rule P-31, or name the arm in the acceptance record's §7 so the ratification is knowing.

### RD26-07 — MINOR — RFC4-19 cites RFC4-26 for the declared join basis; the join-basis clause is RFC4-22

RFC4-19's `branch + base revision` row: *"The convention-grade correlation join, with its basis declared **(RFC4-26)**."* RFC4-26 is *"Declaration sites (SDR-3/4)"* — capability↔code mapping classes and code markers; it contains no join-basis obligation. The clause that does is RFC4-22: *"**Declared join bases.** Every adapter-owned link of the change-accounting chain — work item ↔ branch/worktree, branch → commits … declares its **basis**."* `verify_final_prespec.py` passes because RFC4-26 resolves as an identifier; nothing checks that it means what the citing row needs. `[Observed]`

One-line direction: change the row's citation to RFC4-22.

### RD26-08 — MINOR — route 4 is attributed to owner decision A2, which names three routes

RFC4-13: *"(owner decision **A2** confirmed the routes, bounded route 3, and added route 4; history §RFC4-13)"*, and `RFC-0004/README.md` §8 q6: *"**ANSWERED — owner decision A2:** all three admission routes confirmed, route 3 bounded … and a fourth route added for doc-only and governance-only work."*

The recorded decision reads: *"**A2** | **Three admission routes, oracle bounded.** Syzygy-launched profiled run; externally confirmed CI run; owner-declared trusted oracle…"* — three, no fourth. Route 4's actual warrant is a separate Tier C ruling in the same record: *"**RFC 0002 §8 q3** | **Deterministic check qualifies.** … **Adds a fourth route to A2's list**; 'deterministic check' needs a real definition or it becomes the loosest route."* The record's own consequence table gets it right — *"RFC4-13 | … route 4 added … | **A2 + Tier C q3**"*. So the route is genuinely owner-warranted and its caveat is discharged by RFC4-13(b); only the attribution is wrong, in two places. `[Observed]`

One-line direction: attribute route 4 to A2 + the RFC 0002 §8 q3 ruling in both sites.

### RD26-09 — MINOR — RFC 0002 declares RFC 0004 a reliance, a dependency, and an informative forward reference, in three places

Front matter: `depends_on: [RFC-0001, RFC-0003, RFC-0004, RFC-0005]`. README §5: *"**Relies on RFC 0004:** RFC4-13 route 4 and its governed-checker requirement (RFC4-13(b)) as a `gate-backed` route."* README §5, four paragraphs later: *"Where this package cites a sibling *draft* by clause number (**RFC4-n**, RFC5-n, and the surface RFCs), the citation is **informative until that RFC is accepted**."* And RFC2-18 uses the route normatively, not illustratively: *"the gate may be a **governed diff-satisfies-clause check** whose retained output is the gate artifact (RFC4-13 route 4 …)."*

The package took visible care to carve out RFC 0003 as the load-bearing exception (*"They are exactly four"*) and did not extend the same treatment to the RFC 0004 route its own chain outcome depends on. Practically harmless — Wave A binds both together — but the three statements cannot all be true. `[Observed]`

One-line direction: add RFC 0004's four route-4 citations to the stated load-bearing exception alongside RFC 0003's.

### RD26-10 — MINOR — RFC4-13's authority line says Syzygy does not run reports; route 1 of the same clause depends on Syzygy running them

RFC4-13 opens: *"*Authority:* verification evidence as it exists on disk or in CI systems — **Syzygy reads reports; it does not run them** (SEC-3) [Observed: v1.md V0 scope]."* Route 1, sixty lines later: an artifact qualifies for `gate-backed` when *"it was **produced by a Syzygy-launched profiled run** (RFC5-21)."* RFC5-19 reconciles the two (*"profiles govern only code Syzygy itself launches"*), so the intent is clear — but the flat sentence contradicts its own clause on a plain reading. The `[Observed: v1.md]` anchor is also loose: v1.md says *"Observed-project code execution: opt-in, profiled, and blocked until the execution-profile RFC is accepted (SEC-3),"* which is not "does not run them". `[Observed]`

One-line direction: qualify to "this observer reads reports and never executes; execution is RFC5-18's gate".

### RD26-11 — MINOR — a Wave A normative consequence is anchored in a Wave B clause

RFC4-23(2): *"That bound is an owner-approved declaration that unblocks a claim class — **until it is declared, `active` is unrenderable (RFC8-16)** — so it is honored **only under RFC3-16(a)**."* RFC8-16 is in Wave B, which is not accepted and is a separate act. The module's §5 acknowledges it as *"a forward citation into RFC 0008."* The rule survives Wave-A-alone because RFC4-23(2)'s own last sentence carries it (*"liveness stays unrenderable rather than degrading to a permissive default"*), so this is a citation-shape defect, not a hole. It is the only instance I found: I swept the 19 modules for `RFC7-`, `RFC8-`, `RFC9-`, `RFC10-`, `RFC11-` citations sitting inside a normative rule rather than a §5 pointer, and this is the one where the rule's *statement* is attributed outward. `[Observed]`

One-line direction: state the rule in RFC4-23(2)'s own words and demote the RFC8-16 mention to a parallel-obligation pointer.

### RD26-12 — MINOR — the routing enumeration covers 1 of Wave A's 19 modules, and describes its own population as six contracts where eleven exist

`SURFACE-CLAUSE-ROUTING-MATRIX.md` scopes itself to *"every clause of RFC 0006–0011"*, and its rationale reads: *"**Six contracts** each carry the same binding phase rule — RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16, RFC11-12."* Eleven do. The acceptance record enumerates all eleven (*"RFC1-33, RFC2-26, RFC3-33, RFC4-30, RFC5-27, RFC6-28, …"*) and `verify_final_prespec.py` counts **11 phase-rule clauses**. `[Observed]`

The consequence for Wave A: RFC 0001–0005 — 18 of the wave's 19 modules — carry phase clauses whose obligation (*"every observable consequence either maps to an approved OpenSpec requirement and scenario … or carries a reviewed N/A judgment"*) has no enumeration behind it, and the matrix's own argument for why enumeration matters applies to them verbatim: *"That rule is only as good as the enumeration behind it."* This is consistent with the clauses' staging — each says the matrix is produced *"At surface specification"* — so it is not a contract defect. It is a defect of the matrix's self-description, and a gap a Wave A reader will look for and not find. RFC-0006's own 28 rows are complete and correct (28/28, one route each). `[Observed]`

One-line direction: correct "Six contracts" to eleven and state in the matrix that RFC 0001–0005 are enumerated at surface specification.

### RD26-13 — MINOR — RFC3-15 closes a set doctrine calls a minimum, and the seam is not at the gate

architecture.md: *"The **four** `governance/` categories above are **constitutional minimums**."* RFC3-15: *"the five-category set itself being closed except by the two lawful widenings this RFC records … **A plane validator therefore accepts exactly these six names and rejects a seventh**; neither rejecting `declarations/` nor admitting an unreserved directory is conforming."*

A contract may bind more tightly than a doctrinal floor, so the two are compatible on a narrowing reading — but a validator that *rejects a seventh directory* is not obviously a narrowing of a rule whose word is "minimums", and P-18(a) records the tension as an open owner item (*"none blocks an act"*). The acceptance record's §7 item 1 covers the adjacent question (q4, `declarations/`) and describes the six-name validator as *"load-bearing, not passive"*, but does not put the four-versus-closed seam in front of the owner. `[Observed]`

One-line direction: fold the P-18(a) seam into §7 item 1's text.

---

## Findings table

| Id | Class | Dimension | Summary |
|---|---|---|---|
| RD26-01 | **BLOCKING** | 6 | The Wave A install copies companions and the act's own manifests into `governance/contracts/`, against RFC3-15's "exclusively" — the clause the act binds; P-33 says Wave A cannot be re-offered until ruled, and it is unruled |
| RD26-02 | **BLOCKING** | 4 | P-31, P-33 and P-37 each name the Wave A act as their earliest gate; none appears anywhere in the acceptance record (0 grep hits), so the act is not a knowing one on three points |
| RD26-03 | MAJOR | 2, 5 | RFC3-4 calls zero governance roots "a contradiction per RFC1-1"; RFC1-1 proves at length that no kernel contradiction is minted for that case |
| RD26-04 | MAJOR | 3, 5 | RFC3-2/3-15/3-16 say challenge expiry derives at evaluation and mints nothing; RFC2-13 and decision B1 require a recorded resolution act — and RFC 0003's closed categories give the sweep's record no home |
| RD26-05 | MAJOR | 3 | RFC4-19's R-class `terminal outcome` with a toolchain-verbatim value domain makes a vanished-worker run's record inadmissible, so the run is dropped; disclosed as open §8 q2, unrepaired |
| RD26-06 | MAJOR | 3, 4 | RFC2-19 carries a paragraph explicitly "awaiting an owner ruling" (P-31) that narrows RFC2-24's closure for the corpus's flagship V0 rendering |
| RD26-07 | MINOR | 5 | RFC4-19 cites RFC4-26 for the declared join basis; the join-basis clause is RFC4-22 |
| RD26-08 | MINOR | 4, 5 | RFC4-13 and RFC-0004 README attribute `gate-backed` route 4 to owner decision A2, which names three routes; route 4's warrant is the Tier C RFC 0002 §8 q3 ruling |
| RD26-09 | MINOR | 1, 5 | RFC 0002 declares RFC 0004 a `depends_on` edge, a stated reliance, and an informative forward reference — three incompatible typings of one relation |
| RD26-10 | MINOR | 5 | RFC4-13's "Syzygy reads reports; it does not run them" contradicts route 1 of the same clause and overstates v1.md's text |
| RD26-11 | MINOR | 1, 7 | RFC4-23(2) anchors "until it is declared, `active` is unrenderable" in RFC8-16, a Wave B clause |
| RD26-12 | MINOR | 7 | The routing matrix says "Six contracts each carry the same binding phase rule" where eleven do, and enumerates 1 of Wave A's 19 modules; RFC-0006's own 28 rows are complete |
| RD26-13 | MINOR | 1 | RFC3-15's six-name closed validator narrows what doctrine calls "constitutional minimums"; the P-18(a) seam is not in the acceptance record's §7 |

**Totals: 2 BLOCKING, 4 MAJOR, 7 MINOR.**

Note for the reader: RD26-01 and RD26-02 are both properties of the *offer*, not of the nineteen modules' semantics. The contract text itself is in materially better shape than that count suggests — the evidence model, the consent gates, and the closed vocabularies each survived targeted attempts to break them, and the four MAJORs are all narrow and locally repairable. What cannot be honestly done today is hand this wave to the owner as a knowing act.

VERDICT: REVISE
