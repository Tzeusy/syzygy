# RFC/OpenSpec boundary review — rev10 final pre-specification package (directive §13.4)

Fresh-context reviewer. Scope: `_bootstrap/rfc-phase/final-prespec/`; rev9 baseline at `history/rev9-rfcs/`. Questions answered: (a) can any user-observable behavior be scheduled for implementation bypassing OpenSpec? (b) do contract clauses remain architectural rather than disguised user stories?

**VERDICT: EXCEPTIONS** — 9 located. None is a contract-level hole: the six phase-rule clauses are present, textually unweakened, and unconditional in their own prose. The exceptions are (i) one concrete bypass *mechanism* created by the new selective-loading regime (E1), (ii) a garbled tally and three stale/overstated boundary claims that misdescribe the very boundary they assert (E2–E4), (iii) a classification gap that loses three invariants into "OpenSpec candidate" and under-covers the skeleton (E5–E6), and (iv) three minor items (E7–E9). E1 and E2 are the ones I would not ship without fixing.

---

## Check 1 — the six phase-rule clauses: existence, shape-parallelism, unweakened

[Observed] All six exist at the stated locations:

| Clause | File:line |
|---|---|
| RFC6-28 | `rfcs/RFC-0006-cross-surface-selection-query-drawer.md:387` (§3.9) |
| RFC7-38 | `rfcs/RFC-0007/rendering-and-surface.md:306` (§3.13) |
| RFC8-32 | `rfcs/RFC-0008/accounting-reconciliation-and-release.md:269` (§3.16) |
| RFC9-52 | `rfcs/RFC-0009/interaction-parity-and-release.md:284` (§4) |
| RFC10-16 | `rfcs/RFC-0010-mission-control-autonomy.md:256` (§3.7) |
| RFC11-12 | `rfcs/RFC-0011-context-compiler.md:180` (§3.6) |

**Unweakened vs rev9 — machine-verified.** I extracted each of the four carried clauses from `history/rev9-rfcs/` and from the rev10 module, stripped the `*(History: …)*` parenthetical (extracted to `history/` by design), normalized whitespace, and diffed. [Observed] RFC6-28, RFC7-38, RFC9-52: **byte-identical**. RFC8-32: differs only in a line-wrap hyphenation (`clause-to-\nrequirement` → `clause-to-requirement`). No limb of any of the four was dropped, softened, or scoped down.

**Package scope covers the whole package** — [Observed] for all three packages that carry a phase rule, by three different mechanisms:
- RFC-0007: inline parenthetical at `rendering-and-surface.md:321` — "binds the whole package: RFC7-1…RFC7-37 spans both modules, and the coverage matrix … is a package-level deliverable, not a per-module one."
- RFC-0008: **no inline parenthetical**; covered instead by `rfcs/RFC-0008/README.md:236-243` ("## Phase boundary … must cover **RFC8-1…RFC8-31 across all three modules**, not module 3 alone") and by the clause's own RFC8-1…RFC8-31 range. Not a weakening — the range does the work — but it is the one asymmetry in the set, and it is why E1 below bites RFC-0007 and not RFC-0008.
- RFC-0009: inline parenthetical at `interaction-parity-and-release.md:298` plus `rfcs/RFC-0009/README.md:134`.

Note on the charter's "four packages": [Observed] only **three** packages carry a phase rule (0007, 0008, 0009). RFC-0006, RFC-0010, RFC-0011 are single files, so package scope is moot for them. RFC-0002/0003/0004/0005 are packages but carry no phase rule by design (they are covered by the stated RFC 0001–0005 judgment — see check 4).

**Mechanical corroboration.** [Observed] `scripts/verify_final_prespec.py` PASSes and checks all six IDs (`PHASE_RULE_CLAUSES`, line 44; check at line 232-235). It checks **presence of the clause ID only** — not text strength, not package-scope coverage, not README reachability. The claim in the acceptance record §6 that the verifier covers "phase-rule presence" is accurate and appropriately narrow; do not read it as validating E1/E4.

**E4 — "shape-parallel" is overstated.**
- Located: `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:11` ("all shape-parallel"), `09-OPEN-SPEC-READINESS-REPORT.md:12` ("Six shape-parallel phase-rule clauses"), `RFC-0010…:264` and `RFC-0011…:188` (self-declared "Shape-parallel with …").
- [Observed] RFC10-16 and RFC11-12 each omit **four limbs** carried by all four rev9 clauses: (a) "it is **not a specification of record from which implementation work may be scheduled**"; (b) the requirement must be "in the governance root's `openspec/**` plane"; (c) "**that matrix is review material, never authority**"; (d) "This clause creates no OpenSpec content now (none may exist during bootstrap)."
- Why it matters: (c) is the limb with teeth. Without it, RFC-0010's and RFC-0011's clause-to-requirement coverage matrices have no stated authority ceiling — the exact failure the rev8 rework added that sentence to prevent. (a)'s absence removes the "not a specification of record" characterization from the two newest, most implementation-adjacent contracts.
- Counterweight [Observed]: 10-16/11-12 are *stricter* on the N/A limb — "a reviewed N/A judgment **proving it purely structural with no independently testable behavior**" vs rev9's "recording why that consequence needs no requirement." So this is non-parallelism, not net weakening. Fix: restore (a)–(d) verbatim, keep the stricter N/A test.
- Minor: RFC10-16/RFC11-12 scope their coverage matrix over `RFC10-1..RFC10-16` / `RFC11-1..RFC11-12` (self-inclusive), where the four rev9 clauses stop one short of themselves. Harmless — broader, not narrower.

---

## Check 2 — RFC-0010/0011 row-by-row classification (16 + 12 rows)

I judged all 28 rows. Machine-verified tallies match the matrix's own per-contract figures: [Observed] RFC-0010 = 11 DI / 3 OS / 2 DI+OS (16 rows); RFC-0011 = 10 DI / 2 DI+OS (12 rows).

**Rows I judge correct (23 of 28):** RFC10-1, -2, -3, -6, -8, -9, -10, -11, -14, -15; RFC11-2..-9, -11, -12; and both DI+OS splits in RFC-0010 (RFC10-7 envelope-content invariant vs editing surface; RFC10-13 compression + never-silently-disappear vs queue UX) — these two are the model the rest should follow.

### E5 — three OS rows carry fixed invariants and name no retained DI limb
Located: `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:258` (RFC10-4), `:259` (RFC10-5), `:266` (RFC10-12).

The matrix's own convention (line 42-44, and followed by RFC7-22, RFC8-20, RFC9-33, RFC9-36, RFC10-7, RFC10-13) is that a mixed clause names its retained DI limb in the rationale column. These three do not, and each has one:

- **RFC10-4** [Observed, `RFC-0010…:109-112`]: "Pinned inputs are **immutable for the mission's life**: a change to any pinned input does not silently retarget a running mission — it raises an escalation whose choices include re-approval against the new inputs." That is a design invariant with no other home. Rationale column says only "Mission identity fields → concrete creation/approval requirements and scenarios."
- **RFC10-5** [Observed, `:127-129`]: the clause explicitly partitions itself — "What *is* fixed now: every terminal state is recorded with its reason; `expired` and `cancelled` are always reachable by human act; **no state transition widens the envelope**." Three fixed invariants, classed wholly OS.
- **RFC10-12** — the serious one [Observed, `:216-218`]: "an expiry default must be safe: expiry may narrow, pause, or block, and **may never widen an envelope or approve anything**." §4 violation case 4 (`:277`) is built entirely on this invariant. Classing the clause pure-OS routes a load-bearing safety rule into "concrete behavior to be specified later."

Blocking? Not at contract level — matrix line 31 says "Where it and an RFC clause disagree, the clause wins," and the clause text is intact. But this file is the declared input to the coverage matrices, and an OS row with no named DI limb is exactly how an invariant gets treated as elaboration at spec time. Fix is three rationale-column edits, in the shape RFC10-7/10-13 already use.

### Is any OS-classified behavior schedulable from RFC prose today?
[Observed] No, for RFC-0010/0011. RFC10-5 is the closest call — it prints a concrete lifecycle state machine in a fenced block — and it defuses itself: "[Inferred] This list is **provisional at this contract's acceptance** … freezing happens by OpenSpec requirement, not by this clause." RFC10-4/10-12 are "binding at minimum" floors with schema explicitly deferred (§7). RFC11-1 is the same shape.

[Observed] The most schedule-flavored prose in the whole corpus is **RFC9-32** (`rfcs/RFC-0009/visual-grammar-and-lenses.md:195`): "**V0 ships:** primary lenses **Architecture** … and **Verification** … always-available overlays work/construction and freshness/staleness." That reads as a delivery commitment. I verified it is **carried verbatim from rev9** (`history/rev9-rfcs/RFC-0009-orrery-map-surface.md:1030`), is classed OS → `spec/map-lenses`, and is subordinated by RFC9-52. Not a rev10 regression; naming it so it isn't rediscovered as one.

### Is any DI-classified clause a disguised user story?
[Observed] No. I checked every DI row in both new contracts. The nearest candidates and why each survives:
- **RFC10-13** DI limb ("streaming every run event to the human is a violation of this clause, not a conservative default") — reads as UX, but the binding content is an information-compression invariant, and the queue UX is already split off as OS. Correct as classed.
- **RFC10-14** fixes a concrete path, `.syzygy/work/missions/<mission-id>/`. That is a governance-home decision under RFC 0003 discipline, consistent with how every other contract names `.syzygy/**` homes — not a UI behavior. Mild asymmetry worth noting: RFC10-14 fixes a home while RFC10-15 defers the workspace-store home to §8 q3.
- **RFC10-2** "Agents consume stable machine-readable data; scraping human-rendered tables is never a conforming integration" — an integration invariant, not a story.
- **RFC11-3/11-5/11-6** — all invariants ("read everything" unlawful; inference never suppresses; incomplete-is-Unknown-and-blocks).

### E6 — an undefined fifth class, and the skeleton under-covers because of it
Located: `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:35-40` (the "four classes" table) vs `:261, :267, :276, :285` (four rows classed **`DI + OS`**), and `:289-302` (coverage skeleton).

[Observed] Rev10 introduces `DI + OS` as a class label for RFC10-7, RFC10-13, RFC11-1, RFC11-10, and counts it separately in Tallies — but never defines it in the class table, which still says "The four classes."

[Observed] The same phenomenon in RFC 0007/0008/0009 is expressed the old way, as a DI row whose rationale routes a limb. I enumerated them mechanically — **10 rows**: RFC7-5, RFC7-10, RFC7-13, RFC7-16, RFC7-17, RFC7-34 (→ `spec/intent-surface`), RFC8-14 (→ `spec/work-surface`), RFC9-13, RFC9-24 (→ `spec/map-surface`), RFC9-41 (→ `spec/map-scenes`).

The consequence is a real coverage gap, not a cosmetic one. The skeleton's sourcing column reads "RFC 0007 **OS rows** (see §RFC 0007)", "RFC 0008 **OS rows**", "RFC 0009 **OS rows**". By the matrix's own classification, "OS rows" for RFC 0007 means **exactly one row (RFC7-22)** — it excludes all six RFC7 DI rows whose rationale explicitly routes a limb to `spec/intent-surface`. Same for RFC8-14 and for RFC9-13/24/41. Meanwhile the RFC-0010/0011 skeleton rows *do* enumerate their DI+OS parts ("RFC10-7(part)", "RFC10-13(part)", "RFC11-10(part)", "RFC11-1(part)"). So the new contracts are covered precisely and the carried ones are covered by a pointer that resolves too narrowly.

Fix: either apply `DI + OS` retroactively to the 10 rows and define it in the class table, or change the skeleton's sourcing column to "OS rows **and DI rows with a named spec limb**". The former is cleaner and costs 10 cell edits.

### Rows flagged in the charter, individually
- **RFC10-4** — see E5. Should be DI + OS.
- **RFC10-5** — see E5. Should be DI + OS. The OS half is correct and well-guarded.
- **RFC10-7** — correct as DI + OS. The narrowest-reading default ("absence of a budget is zero delegated spend … absence of a path grant is no write access") is properly retained DI.
- **RFC10-12** — see E5; the highest-value fix of the three.
- **RFC10-13** — correct as DI + OS.
- **RFC11-1** — correct as DI + OS. Caveat [Inferred]: the OS limb ("packet inspection → `spec/context-packets`") is a *derived* observable — the clause text itself contains no viewing surface, only identity/immutability/field-floor. Routing a derived observable is right; just be aware nothing in the clause sources it.
- **RFC11-10** — correct as DI + OS. Caveat [Observed]: it routes the profile registry to `spec/mission-control`, but the registry's home is open (RFC 0011 §8 q2 / RFC 0010 §8 q3, `08-OPEN-QUESTION-TRIAGE.md:48`). Routing a spec domain is not choosing a home, so this is not a prejudged answer — but if the owner rules the registry into a project home, this row's target moves.

### One structural observation on the new tables
[Observed] Neither RFC-0010 nor RFC-0011 has a single **CR** row — 0 of 28, against 8 CR rows across RFC 0007/0009. I judge that correct: neither new contract carries a release-gate or review-cadence obligation. The one candidate is RFC11-11's budget figure, and the matrix handles it in the rationale ("figure is policy, §8 q1") rather than by class. Acceptable; flagging so the absence is a recorded judgment rather than an omission.

---

## Check 3 — bypass hunt

I swept the active corpus (all `rfcs/**`, all numbered reports, `05-CONTRACT-INDEX.yaml`, `ACTIVE-CONTRACT-MANIFEST.txt`, `fixtures/**`, `matrix-rows/**`, the bundled `doctrine/` and `craft-and-care/` copies) for scheduling, commitment, and roadmap language, excluding `history/**`. Patterns: `will be (built|implemented|shipped|delivered)`, `we will (build|implement|ship)`, `sprint`, `backlog`, `implementation plan`, `schedul*`, `roadmap`, `must be implemented`, `shall implement`.

**[Observed] No clause, README, or report schedules implementation of observable behavior.** Every `schedul*` hit resolves to one of: the phase rules themselves; the work-*scheduling* substrate (doctrine `architecture.md`, Beads); `schedules an evaluation` (RFC5-11); or an explicit negation. Every `roadmap` hit is RFC4-29's "enrichment roadmap, **named but never required**" or doctrine's mandate that fleet monitoring stay "named and sequenced on every roadmap with entry criteria."

**Readiness report** (`09-OPEN-SPEC-READINESS-REPORT.md`) — the charter asked whether its sequence recommends or schedules. [Observed] It **recommends**. Evidence: the heading is "Recommended first OpenSpec changeset sequence" (`:25`); line 4-5 states "**No changeset is authored in this phase** (hard boundary; six phase-rule clauses)"; the ordering rationale is dependency-based ("Requires 1–3's vocabulary", "Can proceed in parallel with 4 once 1 exists"), not calendar- or commitment-based; line 52-54 imposes a *constraint* on future changesets ("Each changeset must produce its clause-to-requirement coverage rows … the phase rules make this non-optional") rather than committing to produce them; item 6 keeps the D1-gated historical bundle "dormant behind its own owner approval." One gap worth closing [Inferred]: unlike the routing matrix (`:30-31`, "This file is not a contract and creates no OpenSpec changeset"), the readiness report carries no equivalent disclaimer on the sequence itself. One sentence — "this sequence is advisory and commits nothing" — would remove the only reading under which a numbered list of six domains looks like a plan of record.

**Autonomy extension register** (`07-AUTONOMY-EXTENSION-REGISTER.md`) — clean and, in places, exemplary. [Observed] "no gate scheduled; must not be smuggled in via mission predicates" (`:21`); "Nothing above is silently begun … the register itself authorizes nothing" (`:23-28`). Its "earliest gate" column names blocking conditions, not dates. Unrelated defect: row `:19` (Environment/toolchain capsule) is missing a table cell — 3 cells in a 4-column table, so its Classification renders empty.

**Acceptance record** — [Observed] `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` contains **no** mention of the phase rule or the OpenSpec boundary anywhere. [Inferred] I'd treat this as a missed safeguard rather than an exception: the acceptance act is precisely the moment at which "accepted" is most likely to be misread as "cleared to build," and the record is the artifact installed to `.syzygy/governance/contracts/rfcs/` and read thereafter. One line in §1 or §7 — "acceptance of these contracts schedules no implementation; the six phase-rule clauses bind" — would close it. Raising as a recommendation, not scoring it as an exception.

### E1 — the one real bypass mechanism: the phase rule can be absent from a lawful packet
**This is my most significant finding.** Located: `rfcs/RFC-0007/README.md` (no phase-boundary section), `fixtures/context-selection-1-polaris-narrative.md:19-33`, `05-CONTRACT-INDEX.yaml`.

Rev10 introduces selective loading. Under RFC11-3, the packet is the *entire lawful context* of a governed run ("dispatching it with no packet is a violation, not a fallback"), and under RFC11-4 the mandatory set is selected deterministically from graph and applicability metadata. So a clause that is not selected does not reach the actor at all. Chain of observations:

1. [Observed] RFC7-38 exists **only** in `rendering-and-surface.md` (module 2).
2. [Observed] `rfcs/RFC-0007/README.md` contains **no restatement** of RFC7-38 and no phase-boundary section — I grepped it for `7-38`, `phase`, `schedul`, `OpenSpec`; the only hits are clause-range bookkeeping at lines 7, 43, 55 and an unrelated RFC 0004 reference at 191. Contrast `rfcs/RFC-0008/README.md:236-243` ("## Phase boundary") and `rfcs/RFC-0009/README.md:134` ("RFC9-52 binds the package, not one module").
3. [Observed] The package's own worked example, fixture 1, selects `RFC-0007/README.md` + `narrative-contract.md` (+ two RFC-0002 modules + `vision.md`) and **explicitly omits** `rendering-and-surface` — "the task edits content, not surface rendering; its obligations bind the surface implementer, not the author."
4. [Observed] Therefore a lawful, deterministically-selected, digest-bound Polaris packet exists **containing no phase-rule text of any kind**. Its own "Why no applicable constraint was lost" section does not notice.
5. [Observed] Nothing in `05-CONTRACT-INDEX.yaml` can force the rule in: every clause is `kind: normative`, with no phase-rule marker; the `phase-boundary` tag appears on exactly one contract in the whole index — RFC-0008 (`:325`).

Contrast fixture 3 (`context-selection-3-orrery-lens.md:29-33`), which hits the identical situation for RFC 0009, *reasons about it explicitly*, and is saved by the RFC-0009 README restatement: "parity obligations bind the implementation phase; the drafted delta must route through OpenSpec anyway (RFC9-52, **restated in the README the packet carries**)." The author clearly understood the hazard for RFC-0009 and did not carry the fix to RFC-0007.

Severity: fixture 1's own task is content authoring, so the immediate risk is low. The *pattern* is the problem — the packet shape generalizes to any Polaris task selecting module 1, including tasks that do touch observable behavior, and this is precisely the boundary the six clauses exist to hold. Fixes, cheapest first: (a) add a "## Phase boundary" section to `rfcs/RFC-0007/README.md` mirroring RFC-0008's; (b) mark the six phase-rule clauses in the contract index (e.g. `kind: phase-rule` or an always-include flag) and require RFC11-4's mandatory set to include the governing phase rule of every selected contract; (c) add the check to `verify_final_prespec.py` — it currently verifies the clauses *exist*, not that they are *reachable from every packet*. I'd do (a) and (b); (a) alone closes today's instance.

---

## Check 4 — coverage skeleton completeness, and the RFC 0001–0005 judgment

**Skeleton vs RFC-0010/0011 OS rows: [Observed] complete.** All five OS/DI+OS rows of RFC-0010 (10-4, 10-5, 10-7 part, 10-12, 10-13 part) and both of RFC-0011 (11-1 part, 11-10 part) appear in the skeleton, correctly split across `spec/mission-control` and `spec/context-packets`. Domain count checks out at 8, matching the readiness report's claim.

**Skeleton vs RFC 0007/0008/0009 OS rows: [Observed] incomplete** — see E6. The pointer-style sourcing column resolves to 5 rows across three RFCs where 15 belong.

**Does the RFC 0001–0005 judgment still hold with 0010/0011 added? [Observed] Yes, and it is marginally stronger than at rev9.** RFC-0010 `depends_on` 0001/0002/0003/0005/0006/0008 and RFC-0011 `depends_on` 0001–0005 + 0010; both carry a phase rule, so every observable consequence they draw from the kernel contracts passes through a rule-carrying contract. The matrix's header extension of the judgment ("now extends to RFC-0010/0011's own dependencies the same way", `:14-16`) is sound.

Two refinements the matrix does not make, worth recording:
- [Observed] RFC10-16 is the **first clause anywhere in the corpus** to place CLI commands, API endpoints, and machine-client tooling explicitly under the phase rule ("CLI commands, API endpoints and their answers, MCP tools"). Combined with RFC10-3 binding machine-client admission to RFC5-5/5-6, this *shrinks* the rev9 named residue — machine-client credential handling now has a rule-carrying home it lacked at rev9.
- [Observed] The residue paragraph (`:241-248`) is carried **unchanged** and still names RFC 0005's "ceremony, login, and consent *experiences*" in full. After the above, the genuine remainder is narrower: human login and consent-ceremony UX. Correctly still named rather than hidden, and the fail-safe sentence is intact ("If a later phase finds an RFC 0001–0005 consequence reaching users without passing through a rule-carrying contract, that is a gap to route, not a licence to schedule"). Updating the paragraph to reflect what RFC10-16 now covers would be an improvement, not a correction.

### E7 — the non-exemption sentence covers DI but not CR
Located: `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:228-230` — "the DI/OS classification here is a **routing aid only** — a **DI class** never exempts a clause's observable consequences from OpenSpec coverage."

[Observed] CR is not mentioned, and CR rows carry some of the most directly user-observable material in the corpus: RFC9-49 (declared responsiveness budgets → craft performance policy), RFC7-30 (comprehension-test criterion), RFC9-45 (comprehension walkthrough gate). A reader could take "routes to craft-and-care / release policy" as a complete disposition and skip the OpenSpec route for, say, responsiveness budgets.

Why it isn't a contract hole: the phase-rule clauses are unconditional over the full clause range ("every observable consequence of RFC9-1…RFC9-51"), which includes every CR-classed clause; and matrix line 31 makes the clause win. So this is a routing-aid clarity defect. One-word fix: "a DI **or CR** class never exempts…".

### E2 — the Tallies line is garbled and materially misstates OS volume
Located: `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:313-315`: "Carried rev9 rows (RFC 0007/0008/0009): unchanged classifications — **34 DI / 31 OS / 53 CR+IR-enumerated** (see rev9 tallies, superseded only in module targets)."

[Observed] I parsed all 159 rows of the file. Actual rev10 counts for RFC 0007/0008/0009: **118 DI, 5 OS, 8 CR** (RFC7: 34 DI / 1 OS / 4 CR · RFC8: 31 DI / 1 OS / 0 CR · RFC9: 53 DI / 3 OS / 4 CR).

[Observed] The three numbers in the line — 34, 31, 53 — are the **per-RFC DI counts**, lifted from rev9's tally section (`_bootstrap/rfc-phase/SURFACE-CLAUSE-ROUTING-MATRIX.md:234-238`, which states them correctly and per-RFC) and re-labelled as an aggregate DI/OS/CR split. Rev9 was right; the rev10 compression broke it.

Why it blocks: the line asserts **31 OpenSpec-candidate clauses** where **5** exist — a 6× overstatement of how much of the carried corpus is routed to OpenSpec, sitting in the summary line of the file that the coverage matrices take as input, and pointing at a rev9 source that says something different. It also silently drops rev9's "no clause was found to be pure INFORMATIVE-RATIONALE" reading and its CR enumeration. Fix: restore the per-RFC form.

### E3 — the matrix's own rule section still says "four"
Located: `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:217-218` — "Added at the rev8 rework (directive item 7), **four** RFCs **now carry** an identically-shaped clause — RFC6-28, RFC7-38, RFC8-32, RFC9-52" — and `:231-234` — "**This matrix routes RFC 0007–0009 only**; RFC 0006's clause-level routing … is a surface-specification deliverable … not re-enumerated here."

[Observed] Both are false as of rev10 and contradict the same file's header (`:10-12`, "the binding phase rule now comprises **six** clauses") and its own RFC-0010/0011 tables at `:251-287`. Present tense ("now carry", "routes … only") makes these current claims, not historical notes. A reader who reaches §"The binding phase rule this matrix operates under" — the section that exists specifically to state the rule — concludes RFC-0010 and RFC-0011 sit outside it. Fix: "four" → "six" with the two new IDs, and re-scope the routing sentence to 0007–0011.

---

## Check 5 — stack selection in the two new contracts

[Observed] **RFC-0011 is clean.** Zero hits across a scan for storage engines, transports, serialization formats, languages, runtimes, and model/provider names. It goes further than neutrality: RFC11-10 affirmatively forbids the failure — "**no current model or provider name is hard-coded as permanent semantics** — names are data in profile instances, never constants in contracts." §7 defers "Storage and retrieval technology; embedding/index formats; the numeric token budget; packet transport; compiler scheduling; profile registry home." RFC11-7's mention of "embeddings" is a category of rebuildable projection, not a selection.

[Observed] **RFC-0010 is neutral on transport, storage, and models**, and explicitly says so at `:87-90`: "Exact implementation language, daemon packaging, transport, and whether distribution is literally one binary remain implementation choices; this clause binds the topology (one canonical service, one semantic API), **not the technology**." §7 defers "all transport/language/packaging choices." One exception:

### E8 — MCP is named in normative text without the owner's hedge
Located: `rfcs/RFC-0010-mission-control-autonomy.md:81` ("agent-protocol adapters (e.g. MCP)"), `:93` ("Machine clients (**CLI, MCP adapter**, scripts, fleet workers)"), `:259` ("**MCP tools**").

[Observed] Owner direction OD-R10-1 (`02-OWNER-DIRECTION-RECORD.md:17`) reads "an **MCP (or equivalent)** agent adapter". The RFC keeps the hedge at `:81` ("e.g.") but drops it at `:93` — inside normative clause RFC10-3 — and at `:259`, inside the phase rule. The standing boundary reaffirmed in the same record (`:98-101`) forbids "RPC/packaging selection."

Low severity: RFC10-3's binding content is "every client is one of RFC5-3's two classes — there is no third," and MCP appears only in a parenthetical exemplar list. But naming one agent protocol in normative text, without the hedge the owner wrote, is the seed of a de-facto selection. Fix: "(CLI, an MCP **or equivalent** adapter, scripts, fleet workers)" and likewise at `:259`.

**Topology observation, not an exception.** [Observed] RFC10-2 does bind a real architectural commitment — one canonical long-lived control-plane service with a semantic API, everything else a client — which forecloses, say, a pure-library design. That is legitimate RFC material, it is exactly what OD-R10-1 directed, and the clause is scrupulous about separating topology from technology. Recording it so the owner sees it as the architectural decision it is: the stack boundary holds, the *topology* boundary is deliberately crossed with owner authority.

### E9 — a count claim that doesn't match its own enumeration, propagating into the readiness verdict
Located: `08-OPEN-QUESTION-TRIAGE.md:51-54` and `:66-68`; propagated to `09-OPEN-SPEC-READINESS-REPORT.md:18` and `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §5.

[Observed] I parsed the triage table's class column. Actual base counts (27 §8 questions, excluding the RFC9-9 addendum): 1 at the gate · **6** may remain open before OpenSpec · **12** before V0 implementation · **7** before Mission Control V1 · 1 post-V1 = 27. Stated everywhere: "7 may remain open … 13 close before V0 … 6 before Mission Control V1." The may-remain-open and Mission-Control-V1 figures are **transposed**, and V0 is off by one. The revised summary at `:66-68` ("14 before V0") is likewise one high against an actual 13-with-addendum.

Precisely: may-remain-open = RFC1 q2, RFC3 q1, RFC5 q5, RFC6 q1, RFC6 q2, RFC11 q1 (6). Mission-Control-V1 = RFC3 q2, RFC5 q4, RFC10 q1/q2/q3, RFC11 q2/q3 (7).

On-remit because the readiness verdict rests on which questions are safe to leave open at the OpenSpec boundary: the error overstates by one the questions safe to carry past the gate and understates by one those blocking Mission Control V1. Small, arithmetic, and it lands in three files including the acceptance record. Probably belongs to the open-question reviewer to fix; flagging with the enumeration so it isn't re-derived.

---

## Things I checked that are clean

- [Observed] `ACTIVE-CONTRACT-MANIFEST.txt`: all **32/32** module digests verify against the working tree (`sha256sum -c`).
- [Observed] `scripts/verify_final_prespec.py` runs from the packet on a fresh path and PASSes: 322 clauses, clause continuity, package disjointness/completeness, citation resolution, closed matrix vocabulary, phase-rule presence, fixture completeness, module ceilings. Two honest notes printed, not suppressed (RFC-0001 oversize with justification; corpus over the 35–50k band).
- [Observed] The four carried phase-rule clauses are textually unweakened (diff method above).
- [Observed] The `history/` extraction removed only `*(History: …)*` parentheticals from the phase-rule clauses — no normative limb went to history.
- [Observed] RFC-0006 needs no README restatement: it is a single file, so its phase rule always loads with it, and `:43` carries a summary-level restatement ("this contract schedules no…").
- [Observed] Matrix per-contract tallies for RFC-0010/0011 (11 DI / 3 OS / 2 DI+OS; 10 DI / 2 DI+OS) are correct — I recounted both.
- [Observed] The coverage skeleton correctly routes RFC 0006 to `spec/selection-api` as a deliverable of RFC6-28's own coverage matrix rather than pre-enumerating it.

**Review-integrity note.** [Observed] `doctrine/` and `craft-and-care/` were not present when I first enumerated the workspace and appeared during the review (mtime 2026-08-03 01:19). I verified both are byte-identical to the canonical governed homes (`.syzygy/governance/doctrine/`, `.syzygy/governance/policies/craft-and-care/`) by sha256, so they are reference copies and introduce no new authority. Flagging only because the package was mutating under review — if further files land, the manifest digest and my digest-based findings need re-checking.

---

## Summary of exceptions

| # | Located | Why it blocks / doesn't |
|---|---|---|
| **E1** | `rfcs/RFC-0007/README.md` (no phase-boundary section); `fixtures/context-selection-1…md:19-33`; `05-CONTRACT-INDEX.yaml` | **Blocks.** A lawful, deterministic, digest-bound Polaris packet can contain no phase-rule text; the index has no marker that could force it in. RFC-0008/0009 READMEs already carry the fix. |
| **E2** | `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md:313-315` | **Blocks.** Tallies line claims 31 OS clauses where 5 exist; the three figures are rev9's per-RFC DI counts re-labelled. |
| **E3** | same file, `:217-218`, `:231-234` | Should fix. The section that states the rule says "four RFCs now carry" and "routes RFC 0007–0009 only", contradicting the same file's header and tables. |
| **E4** | same file `:11`; `09-…REPORT.md:12`; `RFC-0010…:264`; `RFC-0011…:188` | Should fix. "Shape-parallel" overstated — 10-16/11-12 omit four limbs including "the matrix is review material, never authority". Stricter N/A limb means no net weakening. |
| **E5** | matrix `:258`, `:259`, `:266` | Should fix. RFC10-4/-5/-12 classed pure OS while carrying fixed invariants, none named as retained DI; RFC10-12's is a safety invariant a §4 violation case depends on. |
| **E6** | matrix `:35-40` vs `:261/267/276/285`, `:289-302` | Should fix. `DI + OS` undefined as a class; skeleton's "OS rows" pointer excludes 10 carried DI rows that route a limb to a named spec domain. |
| **E7** | matrix `:228-230` | Minor. Non-exemption sentence names DI but not CR, the class carrying responsiveness budgets and comprehension gates. Contract rule is unconditional, so clarity only. |
| **E8** | `RFC-0010…:93`, `:259` | Minor. MCP named in normative text without OD-R10-1's "(or equivalent)"; standing boundary forbids RPC selection. |
| **E9** | `08-…TRIAGE.md:51-54, 66-68`; `09-…REPORT.md:18`; acceptance record §5 | Minor, propagating. Open-question class counts transposed (6/7, not 7/6) and V0 off by one, in three files. |

Plus two recommendations that are not exceptions: add a one-sentence "this sequence commits nothing" disclaimer to the readiness report's recommended sequence, and one line to the acceptance record stating that acceptance schedules no implementation.

**Bottom line on the two charter questions.** Can observable behavior be scheduled bypassing OpenSpec? Not by any clause, report, or README text — the sweep is clean and the six clauses are intact and unweakened. But **yes, by omission**, through the new context-packet path: E1 shows a lawful packet from which the rule is simply absent. Do contract clauses remain architectural? Yes — I found no disguised user story in either new contract; the risk runs the other direction, with three genuine invariants (E5) filed as OpenSpec candidates.
