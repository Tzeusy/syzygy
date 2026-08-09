Reviewer: context-packet (RD-11)
Date: 2026-08-09
Commit: 771965c
Files read: `C/rfcs/RFC-0011/README.md`; `C/rfcs/RFC-0011/packet-identity-provenance-and-memory.md`; `C/rfcs/RFC-0011/deterministic-selection-and-budget.md` (all three in full). Consulted for cross-reference only: `C/rfcs/RFC-0002/snapshot-and-evaluation-core.md` (RFC2-1, RFC2-3, RFC2-7, RFC2-11), `C/rfcs/RFC-0002/rendering-vocabularies.md` (RFC2-24 vocabulary), `C/rfcs/RFC-0010/mission-identity-approval-and-lifecycle.md` and `C/rfcs/RFC-0002/rendering-vocabularies.md` (phase-rule range comparison), `.syzygy/governance/doctrine/vision.md` (VIS-2, VIS-7), `.syzygy/governance/doctrine/trust-and-evidence.md`, and the front matter of all 11 candidate contracts. Not read, per instruction: `C/round-2026-08d/`, `C/reviews/`, `C/history/`, `_bootstrap/`.

---

## Method note on sweeps

Three sweeps below carry absence claims. All were run with Python `re` (not system grep) over the stated denominator:

- **Clause-definition sweep.** Denominator: all three package files. Bold clause openers (`**RFC11-n`) resolve to: module 1 = {1,2,3,5,6,7,8,9,10,12}; module 2 = {4,11,13,14,15,16}; README defines none (it restates RFC11-1 and RFC11-12 in prose). 16 clauses, each defined exactly once, no gaps, no duplicates. [Observed]
- **Term sweep.** Denominator: all three package files. `retention`/`retain` = 4 occurrences total; `reason` = 4; load-forms (`load|loaded|loading|loads`) = 9; `profile` = 21 (README 8, module 1 13, module 2 0). Individual results cited per finding. [Observed]
- **Edge sweep.** Denominator: the 10 `depends_on` entries declared across the two module front matters. Result in finding 8. [Observed]

---

## Direct answers to the seven review questions

1. **Packet identity — no.** Same task, same corpus, same policy does **not** yield the same packet digest under the clauses as written, and no clause asserts that it does. RFC11-4 asserts determinism of *selection* ("same inputs, same selection"), never of the digest; RFC11-5 admits inference-produced members into the same artifact RFC11-1 digests. What is digested is stated only as "the packet's **final digest**" over the RFC11-1 field list — the field list is specified, the digest's scope and reproducibility are not. Findings 2, 3. [Observed]
2. **Provenance — partially, by transitive inference only.** Only one member class carries a revision in-clause: RFC11-1 says RFC clauses are recorded "by clause ID at stated revision/digest." Doctrine rules are recorded "by identifier"; craft policies, decisions, and OpenSpec requirements carry no revision qualifier at all. Byte-pinning for those classes rests on RFC11-1's recording of "the **selected evaluation and as-of instant**" plus RFC2-1 item 2, which pins `.syzygy/governance/**` per-artifact by version or content hash — a two-hop chain through another contract, never stated in RFC-0011. Members outside `.syzygy/governance/**` — agent/model profiles most importantly, whose home is open question q2 — are pinned by nothing. Finding 3. [Observed] / [Inferred] for the transitive chain.
3. **Omission register — recorded, but not structured enough to judge risk.** RFC11-1 requires "the **explicitly omitted candidate context, each with its reason**"; RFC11-14(7) requires every excluded applicable candidate "recorded in the packet's omission register with its reason." One case (unsatisfied `depends_on` edges, RFC11-14(2)) gets real structure. Everything else gets an undeclared free-text `reason`. Findings 6, 8. [Observed]
4. **Execution-record binding — Inferred, not Observed, as written.** RFC11-2 puts the digest in the record but nothing makes the packet bytes durable and retrievable, and the sanction for a record without the digest is the undefined phrase "incomplete evidence" with no stated consequence. Findings 4, 5. [Observed]
5. **RFC11-13 — well-defined for two of its three kinds; the index rule is not unambiguously checkable.** The `craft-policy` kind cannot be expressed in the declared grammar. "Loading" is used nine times across the package and defined nowhere, so a checker cannot separate "loaded" from "read from." Findings 10, 11. [Observed]
6. **Memory/carry-forward — one narrow path.** RFC11-6's staleness trigger ("is stale against the selected evaluation") closes the main route for governance-artifact members. The residual paths are transcript content entering as *suggested* rather than mandatory context (finding 12) and members not covered by the evaluation's snapshot (finding 3). No clause was found that lets stale content masquerade as *mandatory* fresh content. [Observed]
7. **Split coherence — the clause map is exact; one clause's own text is stale against the split, and one term is stranded.** The map matches the module bodies byte-for-byte (sweep 1). But RFC11-12's coverage range was not updated when RFC11-13..16 were added (finding 1), and module 1's central term "mandatory deterministic context" is defined only in module 2 (finding 7). [Observed]

---

## Findings

### 1. RFC11-12's coverage range excludes four of the package's sixteen clauses, and the README contradicts the clause rather than amending it — **blocking**

**Clause anchor — RFC11-12 (module 1, §2.5), quoted:**

> "At surface specification a clause-to-requirement coverage matrix over RFC11-1..RFC11-12 is produced — **that matrix is review material, never authority**."

**Contradicting prose — README, "Phase boundary" section, quoted:**

> "The clause text is in `packet-identity-provenance-and-memory.md` §2.5, and its clause-to-requirement coverage matrix must cover **RFC11-1…RFC11-16 across both modules**, not module 1 alone."

[Observed] The package defines RFC11-1…RFC11-16 (sweep 1). The binding clause requires the matrix over RFC11-1..RFC11-12 only. RFC11-13, RFC11-14, RFC11-15, RFC11-16 — four clauses, 25% of the package, including RFC11-13, the implementation-boundary declaration on which packet completeness turns — sit outside the obligation the clause actually creates. The README's "must cover" sentence is index prose, not a defined clause; under verification rule 8 it cannot supply the obligation, and under the repository's normative-change discipline an extension of a clause's scope is a semantic delta to the clause text, not a sentence in the index.

[Observed] Comparative measurement, denominator = all 11 candidate contracts: 5 state a matrix range in this phrasing and match their maximum defined clause exactly (RFC-0001 33/33, RFC-0002 26/26, RFC-0003 33/33, RFC-0004 30/30, RFC-0005 27/27); 4 do not use the phrasing (RFC-0006, 0007, 0008, 0009); 2 state a range short of their maximum — RFC-0010 (22 vs 24) and RFC-0011 (12 vs 16). RFC-0011 has the larger gap. The RFC-0010 result is outside my scope and is reported as a measurement for another reviewer, not as a finding.

**Why this is blocking rather than major:** the acceptance model binds module digests per wave. RFC11-12 lives in module 1 (Wave C1). An owner performing Wave C1 binds the stale range; the four uncovered clauses arrive in Wave C2 with no clause obliging their coverage, and the only artifact saying otherwise is an index the repository's own rules forbid treating as authority. The correction is not available post-act — verification rule 10 and the "never edit an artifact after an act has bound its digest" prohibition both close it.

**Repair:** amend RFC11-12's text to read "over RFC11-1..RFC11-16" as a recorded semantic delta, and delete or demote the README's "must cover" sentence to a pointer that restates the clause rather than extending it.

---

### 2. Inference-produced context sits inside the single digested packet, against the adopted deterministic/inferred seam — **blocking**

**Clause anchor — RFC11-5 (module 1, §2.2), quoted in full:**

> "**RFC11-5.** Inference (model judgment, semantic retrieval) **may add suggested context, with provenance marking it suggested and by what**; it may **never suppress, demote, or replace** mandatory deterministic context. A packet distinguishes its mandatory core from its suggested additions."

**Clause anchor — RFC11-1 (module 1, §2.1), quoted:**

> "A **Context Packet** is a versioned, **immutable**, digest-bound execution artifact, minted per compiled run. It identifies, at minimum: … and the packet's **final digest**."

**Governing doctrine — `trust-and-evidence.md`, "The deterministic/inferred seam", quoted:**

> "Deterministic facts and probabilistic inferences are computed and stored in distinct layers. **An observation record contains deterministic facts only**; the inferred layer is a separate artifact recording the model, version, and inputs that produced it, carrying its own declared reproducibility standard, excluded from the VIS-7 identity test (architecture.md)."

**Sibling contract's implementation of that seam — RFC2-7, quoted:**

> "Each **inference overlay** is a separate, separately versioned artifact recording the model, model version, parameters, and exact inputs (by identity/digest) that produced it, plus the snapshot it was computed over; it declares its own reproducibility standard and is excluded from the identity test."

[Observed] RFC11-5 requires only an in-artifact *distinction* between mandatory core and suggested additions. RFC11-1 mints **one** artifact with **one** final digest over both. RFC-0011 declares `depends_on: RFC-0002` and its README §5 states "**RFC 0001/0002:** packets pin evaluations and as-of instants," yet it does not adopt RFC2-7's structural answer: no separate overlay artifact, no separate digest, no requirement to record the model, model version, or parameters that produced a suggested member, and no declared reproducibility standard for the suggested layer.

[Observed] Consequences, both directly relevant to review question 1:
- The final digest is not reproducible. Two compilations at the same evaluation with the same objective, corpus, and policy differ in their suggested layer and therefore differ in digest. Nothing in the package states the property "same inputs → same digest"; the nearest clause, RFC11-4, states "**Mandatory context is selected deterministically** — same inputs, same selection," which is a property of the selection, not of the artifact's identity.
- A single digest over a mixed-layer artifact cannot be subjected to the VIS-7 identity test in part, and doctrine explicitly excludes the inferred layer from that test. As structured, either the whole packet is inside the test (and fails, because the inferred layer is not reproducible) or the whole packet is outside it (and the mandatory core loses the guarantee the RFC exists to provide).

[Inferred] The stated service of this package — README, **Serves:** "VIS-7/trust floor (what an agent saw is a provable fact, not a guess)" — is met for *content honesty* but not for *identity*, which is what VIS-7 governs.

**Repair:** either (a) scope the digest in RFC11-1 to the deterministic mandatory core and require the suggested layer to be a separately versioned, separately digested overlay carrying model, model version, parameters, and inputs by identity — mirroring RFC2-7 — with the packet recording the overlay's identity; or (b) if the owner intends one artifact, state in-clause that the packet's identity is computed over the mandatory core alone, name the suggested layer as excluded from the identity test, and cite RFC2-7 as the pattern being narrowed.

(part 2/3)

### 3. The agent/model profile is not a packet member, though RFC11-10 makes profile fields authorization-bearing and routing-determinative — **major**

**Clause anchor — RFC11-10 (module 1, §2.4), quoted:**

> "Profile fields that *satisfy an envelope-required gate* — independence, permissions, risk classes served — are authorization-bearing under RFC3-16(a): they satisfy the gate only when backed by owner-act provenance or identified evidence; a self-asserted field **fails closed** for gate satisfaction and the gate stands unsatisfied."

**Absence sweep.** Denominator: RFC11-1's complete "It identifies, at minimum:" enumeration — 14 items, read in full at module 1 lines 43–62. Items: objective; project and workspace identity; selected evaluation and as-of instant; doctrine rules; RFC clauses; OpenSpec requirements and scenarios; topology and craft policies; work warrant and autonomy envelope; code/test/evidence references; active decisions, contradictions, challenges and Unknowns; allowed tools and permissions; context-compiler and adapter versions; explicitly omitted candidate context; final digest. **The agent/model profile and its version appear in none of the 14.** Corroborating term sweep: `profile` occurs 13 times in module 1, all within §2.4/RFC11-10 and its §8 q2, zero times inside RFC11-1. [Observed]

[Observed] The consequence is asymmetric with the rest of the design. RFC11-1 records "the **context-compiler and adapter versions**," and RFC11-4 ties selection to it — "The selection rule set is versioned with the compiler (RFC11-1's version identity)" — so *how* the packet was selected is provable. But *which agent profile, at which version, satisfied the envelope's gates* is not a recorded packet fact, even though RFC11-10 states profiles "are versioned" and makes named fields gate-satisfying. The README's own violation case 7 — "*(RFC11-10)* A review is routed to an agent whose profile lacks the independence property the review class requires, because fallback order ignored it" — describes a failure that the packet, as specified, records nothing about.

[Observed] This is also the one member class the RFC2-1 transitive pin does not reach: §8 q2, "**Profile registry home — OPEN.** Where agent/model profiles live (workspace governance store vs project home)", is unresolved, so profiles are not known to fall under RFC2-1 item 2's `.syzygy/governance/**` per-artifact pin. A packet can therefore be replayed against a silently-changed profile with no detection — the direct answer to review question 2's second half.

**Repair:** add the consulted agent/model profile identity and version — and the identified evidence or owner-act provenance backing any gate-satisfying field — to RFC11-1's minimum identification list.

---

### 4. Packet durability is unspecified, so RFC11-2's binding yields Unknown rather than Observed — **major**

**Clause anchor — RFC11-2 (module 1, §2.1), quoted:**

> "The packet digest is part of every resulting **Execution Record** (RFC8-18..RFC8-20 / RFC 0002 evidence): an execution record for a compiled run without its packet digest is incomplete evidence."

**Governing doctrine — VIS-2, quoted:**

> "Evidence is a durable, identified, integrity-verifiable artifact (trust-and-evidence.md; reproducibility is a declared property of an evidence class, not a prerequisite)"

**Absence sweep.** Denominator: all four occurrences of `retention`/`retain` across the three package files. Two are in README lines 29 and 102, both describing bootstrap process records "retained with the delivery packet" — unrelated. Two are in RFC11-9: the clause heading "**Retention and privacy boundaries**" and this sentence — "retention/deletion of non-canonical raw material (transcripts, scratch) is a declared policy, while canonical memory follows its home's lifecycle (RFC3-16 category lifecycles), never silent deletion." **No clause in the package states a retention or durability obligation for context packet bytes.** [Observed]

[Observed] RFC11-9's two categories do not reach a packet. RFC11-1 calls a packet an "execution artifact," and RFC11-8's enumeration of durable project memory — "accepted decisions; evidence; structured run summaries; lessons derived from incidents; mappings and supersession records; and approved contextual notes" — does not include context packets. So a packet is neither "non-canonical raw material" with a declared retention policy nor "canonical memory" following a home lifecycle.

[Inferred] RFC11-1's "**immutable**" is a mutation prohibition, not a durability guarantee. A digest whose preimage is not durably retrievable is identified but not integrity-verifiable in practice, and under VIS-2 it is therefore not evidence. "This work ran under this context" then degrades to Unknown once the packet bytes are gone — which is exactly what the package is built to prevent, per its own violation case 3: "*(RFC11-2)* An execution record says 'context: latest docs' with no packet digest; six weeks later nobody can establish which revision of the envelope the agent saw."

**Repair:** state in RFC11-2 or RFC11-9 that a packet referenced by an execution record is retained under the record's own evidence lifecycle, and that loss of the packet bytes renders the record's context claim Unknown rather than silently satisfied by the surviving digest.

---

### 5. "Incomplete evidence" in RFC11-2 is an undefined state with no stated consequence — **major**

**Clause anchor — RFC11-2 (module 1, §2.1), quoted:**

> "an execution record for a compiled run without its packet digest is incomplete evidence."

[Observed] The package never defines "incomplete evidence" and never states what it causes. Contrast the discipline of RFC11-6 in the same module, which names both the state and the consequence — "the packet is marked **incomplete/Unknown with the gap named**, and **by default the run does not launch**" — and of RFC11-13, which routes its failure explicitly — "makes every packet selecting that contract **incomplete (RFC11-6)** — never silently complete." RFC11-2 does neither: it does not route to RFC11-6, does not name an Unknown reason, and does not block anything.

[Observed] RFC-0002 already carries a closed Unknown-reason vocabulary (RFC2-24; the nearest fit is item 10, `source-uncaptured-or-unreachable` — "A deterministic input capable of affecting the claim was not captured in the snapshot (RFC2-2)"). RFC11-2 cites RFC 0002 for evidence semantics but does not reach that vocabulary. [Inferred] A record labelled "incomplete evidence" with no rendering rule is a record that can still be counted as evidence by any surface that reads it, which is the VIS-2 failure mode the label was meant to prevent.

**Repair:** in RFC11-2, replace the bare adjective with the same construction RFC11-13 uses — name the state as incomplete under RFC11-6 and cite the RFC2-24 reason the affected claims render under.

---

### 6. The omission register's `reason` has no declared vocabulary or structure — **major**

**Clause anchors, quoted:**

> RFC11-1: "the **explicitly omitted candidate context, each with its reason**"

> RFC11-14, rule 7: "**Omissions are enumerated.** Every excluded applicable candidate is recorded in the packet's omission register with its reason."

**Absence sweep.** Denominator: all four occurrences of `reason` across the three package files — module 1 line 57 (RFC11-1, above), module 2 lines 120 (RFC11-14 rule 7, above), 111 (RFC11-14 rule 2), and 146 (RFC11-16, "The packet records why each constraint entered"). **No clause declares a closed set of omission reasons, a required field structure, or a risk classification.** [Observed]

[Observed] Exactly one omission class gets real structure — RFC11-14 rule 2: "where an edge is left unsatisfied, the clause identities the loaded modules cite from the depended-on contract are enumerated and disposed of individually in the omission register." Every other class — modules dropped for budget under RFC11-11's sharding, `constrains` sources not followed under RFC11-16, candidates excluded by applicability — reduces to free text.

[Inferred] Review question 3 asks whether a reader can judge the risk. Free text is not a measurement. The project's own convention demonstrates the alternative it did not take here: RFC2-24 is a numbered closed vocabulary in which each reason carries a defined meaning and a stated repair. VIS-2's requirement that absence be visible is satisfied by the register's *existence*; its requirement that the reader not be misled is not satisfied by an unstructured reason field, since "omitted: not relevant" and "omitted: budget exceeded, mandatory-adjacent" render identically.

**Repair:** declare a closed omission-reason vocabulary in RFC11-14 (or defer it explicitly to the OpenSpec phase with the deferral named in README §7, which currently defers "Storage and retrieval technology; embedding/index formats; the numeric token budget…; packet transport; compiler scheduling; profile registry home" and not this).

---

### 7. Module 1's "mandatory deterministic context" is defined only in module 2, and the staging fallback lives in README prose — **major**

**Clause anchors, quoted:**

> RFC11-5 (module 1): "it may **never suppress, demote, or replace** mandatory deterministic context. A packet distinguishes its mandatory core from its suggested additions."

> RFC11-4 (module 2): "**Mandatory context is selected deterministically** — same inputs, same selection — from, at minimum: …"

**README's mitigation, quoted:**

> "References from module 1 to module 2's selection semantics are staged until module 2 is accepted; until then a conforming packet is compiled against module 1's identity and disclosure duties with its selection basis stated."

[Observed] The clause-mention sweep confirms the drafters' claim mechanically: module 1 mentions only clauses {1,2,3,5,6,7,8,9,10,12} — it makes **no** citation to RFC11-4, RFC11-11, or RFC11-13..16. Module 2 cites module 1's RFC11-1, RFC11-5, RFC11-6, RFC11-7. Citation direction is therefore correct for a C1-then-C2 acceptance order. [Observed]

[Observed] But the *term* travels where the citation does not. RFC11-5 and RFC11-6 are the operative disclosure clauses of module 1, and both turn on what "mandatory" denotes; the only clause that fixes that denotation is RFC11-4, in module 2. Accepting Wave C1 alone binds RFC11-5's prohibition on suppressing a set whose membership rule is not yet accepted.

[Observed] The compensating rule — "a conforming packet is compiled against module 1's identity and disclosure duties with its selection basis stated" — is a sentence in the README's "The seam, and the acceptance boundary" section. It is not a clause, carries no identifier, and under verification rule 8 cannot be cited. So in the C1-only interval, the fallback posture is unciteable. [Inferred] This is the same structural defect as finding 1 in a different place: the index is being used to carry obligations the clauses do not state.

**Repair:** give module 1 a clause — a new identifier appended to the package, not a renumbering — stating the C1-interval rule: that until the selection clause is accepted, a packet states its selection basis explicitly and does not claim deterministic mandatory selection. Alternatively, accept C1 and C2 as a single act, which removes the interval and makes the README sentence unnecessary.

---

### 8. RFC11-14(2)'s omission disposal is vacuous for six of the package's own ten declared `depends_on` edges — **major**

**Clause anchor — RFC11-14, rule 2, quoted:**

> "**Direct `depends_on`.** Add the direct `depends_on` obligations of every selected module. An edge is **satisfied by loading at least one module of the depended-on contract; where an edge is left unsatisfied, the clause identities the loaded modules cite from the depended-on contract are enumerated and disposed of individually in the omission register.**"

**Edge sweep.** Denominator: the 10 `depends_on` entries declared across the two module front matters. Method: Python `re` over each module body for `RFC<n>-<m>` clause identifiers and for `RFC 00<nn>` prose references, excluding the RFC3-16 status banner and RFC11-12's "(Shape-parallel with RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16.)" parenthetical, both of which verification rule 5 states are not dependency edges. Result: [Observed]

| Declaring module | Declared edge | Clause identities cited from it in that module's body |
|---|---|---|
| 1 | RFC-0001 | **none** (no clause id, no prose reference anywhere in the file) |
| 1 | RFC-0002 | **none** (prose only: "RFC 0002's temporal machinery", "RFC 0002's contradiction machinery") |
| 1 | RFC-0003 | RFC3-16, RFC3-16(a) |
| 1 | RFC-0004 | **none** |
| 1 | RFC-0005 | RFC5-14, RFC5-15, RFC5-16, RFC5-17 |
| 1 | RFC-0006 | **none** (RFC6-28 appears only in the shape-parallel parenthetical) |
| 1 | RFC-0008 | RFC8-18..RFC8-20 |
| 1 | RFC-0010 | RFC10-7, RFC10-8, RFC10-12 |
| 2 | RFC-0002 | **none** |
| 2 | RFC-0010 | **none** |

Four of module 1's eight edges and both of module 2's two edges — **6 of 10** — yield an empty enumeration.

[Observed] Applied to RFC-0011's own front matter, a selector that loads module 2 alone and leaves both its declared edges unsatisfied produces two omission-register entries whose clause enumeration is empty. Under RFC11-14(7) the register is complete; under VIS-2 it discloses nothing, because "edge to RFC-0010 unsatisfied; clauses cited: none" reads as an edge with no content at risk, when the package's substantive RFC-0010 reliance (the envelope, the prohibited and human-only surfaces in RFC11-11) is real but uncited. No clause requires a `depends_on` edge to be clause-anchored, so the disposal rule's fidelity is unbounded below.

[Observed] Module 1's declaration is byte-identical to the package README's `depends_on` list. [Inferred] It was copied from the package index rather than derived from module 1's content, which is why RFC-0001, RFC-0004, and RFC-0006 appear there — those edges are justified by README §5's package-level integration text, not by module 1.

**Repair:** either require in RFC11-14 that each declared `depends_on` edge name at least one clause identity relied on (making the enumeration non-empty by construction), or correct the two module front matters so each declares only the edges its own body relies on, with the union carried by the README.

(part 3/3)

### 9. The README carries selector-consumed and obligation-bearing content with no clause establishing an index's status — **major**

**Clause anchor — RFC11-13 (module 2), quoted:**

> "Each active contract carries, in the front matter of its index (the package README, or the file itself for a single-file contract): … The declaration lives in the governed artifact itself and is consumed, never re-derived, inferred, or overridden by a selector (RFC11-7). A contract whose declaration is absent, or whose named clause does not exist, makes every packet selecting that contract **incomplete (RFC11-6)** — never silently complete."

**README self-description, quoted:**

> "**Every clause identity appears in exactly one module.** … the map below — not range arithmetic — is the lookup authority."

[Observed] The README does three normatively-consequential things: it carries the `implementation_boundary` declaration that RFC11-13 makes packet-completeness-determinative; it declares itself "the lookup authority" for clause→module resolution; and, in the Phase boundary section, it states an obligation ("must cover") that no clause states. [Observed] No clause in the package establishes what an index is, whether its content binds, or which acceptance act binds its digest. Module 1 and module 2 each say only "Index, clause map, lookup rule, package-level integration and deferrals: `README.md`."

[Observed] I verified the declaration itself is present and well-formed: `kind: requires-openspec`, `clause: RFC11-12`, and RFC11-12 is a clause that exists (sweep 1) — so RFC-0011 does not trip RFC11-13's own failure condition. Denominator check across all 11 candidate contracts: all 11 carry an `implementation_boundary` block, all 11 declare `kind: requires-openspec`, and each named clause exists. [Observed]

[Inferred] The tension is that the repository's standing rule forbids treating an index as authority, while RFC11-13 requires a selector to consume a fact that lives only in an index. That is resolvable — the declaration is data the index *carries*, not authority the index *asserts* — but the package never says so, and the README's "must cover" sentence is a live instance of the index crossing from carrying to asserting.

**Repair:** state in RFC11-13 that a package index is a governed artifact whose front-matter declaration is data consumed under this clause, that an index asserts no obligation not stated in a clause, and name which wave act binds the index's digest.

---

### 10. RFC11-13's declared grammar cannot express a `craft-policy` declaration — **minor**

**Clause anchor — RFC11-13 (module 2), quoted:**

```yaml
implementation_boundary:
  kind: none | requires-openspec | craft-policy
  clause: RFCx-y | null
```

> "`craft-policy` states that the contract's observable consequences are governed by a named craft policy rather than an OpenSpec phase rule; the `clause` field then names the craft clause that owns the boundary."

[Observed] The `clause` field's declared value grammar is `RFCx-y | null`. Craft-and-care clause identifiers do not match that pattern: a sweep of `.syzygy/governance/policies/craft-and-care/**/*.md` with the pattern `CC-[A-Z]+-\d+` returns **54 distinct identifiers** of the form `CC-BAR-1`, `CC-DEP-3`, `CC-REV-…`. A conforming `craft-policy` declaration therefore has no legal value for its own `clause` field.

[Observed] The defect is latent, not active: 0 of 11 candidate contracts declare `craft-policy` (all 11 declare `requires-openspec`), so no current artifact is malformed. Severity is minor on that basis, but the clause is being offered for acceptance with a grammar that cannot express one of its own three kinds.

[Observed] A second, smaller ambiguity in the same grammar: `clause: null` is grammatically legal in combination with `kind: requires-openspec`, and RFC11-13's failure condition covers "whose declaration is absent, or whose named clause does not exist" — a null clause is neither absent nor nonexistent-named, so a strict checker has no stated verdict for that combination.

**Repair:** widen the grammar to `RFCx-y | CC-<AREA>-n | null` and add a per-kind well-formedness rule — `requires-openspec` and `craft-policy` require a non-null clause; `none` requires `clause: null` — with a violation of it routing to RFC11-6 like the existing failure condition.

---

### 11. "Loading" is undefined, leaving RFC11-4's index rule and its clause→module resolution ambiguous — **minor**

**Clause anchor — RFC11-4 (module 2), quoted:**

> "The mandatory set always includes, for every selected contract, **what that contract's implementation-boundary declaration names (RFC11-13)**, consumed from the contract's own index and recorded in the packet: the declared kind and named clause, always; and, where the declared kind is `requires-openspec` **and the task itself sits on that boundary** — authoring or scheduling observable behavior at the OpenSpec seam — the module **defining** the named phase-rule clause. An index's restatement of a phase rule is never the clause: the restatement points, the defining module carries. A packet that selects a contract without loading its index records the declaration verbatim together with the digest of the index it was read from."

**Absence sweep.** Denominator: all nine load-form occurrences across the three package files — README lines 103 and 155 (both "whole-corpus loading", non-definitional), module 2 lines 61, 107, 109 and their inflections. **No occurrence defines "load."** [Observed]

[Observed] Three ambiguities follow, all bearing on review question 5's checkability:

1. The rule's own sentence uses both verbs about the same artifact: the index is "not loaded," yet the declaration "was read from" it. Without a definition separating loading (entering the packet's mandatory set) from reading (consulted during compilation), a checker cannot decide which branch a given packet is in, and therefore cannot decide whether the verbatim-plus-digest record was required.
2. The rule records "the digest of the index it was read from" but states no comparison obligation and no verdict on mismatch. RFC11-6's staleness trigger plausibly covers it, but RFC11-4 does not route there — unlike RFC11-13 and RFC11-14(8), which both route explicitly.
3. In the boundary-task branch, RFC11-4 requires "the module **defining** the named phase-rule clause." For RFC-0011 that resolution — RFC11-12 → `packet-identity-provenance-and-memory.md` — is obtainable only from the README's clause map, which the README itself calls "the lookup authority." When the index is not loaded, the rule provides no stated means to perform that resolution.

**Repair:** define "loaded" in RFC11-4 (member of the packet's mandatory set) as distinct from "read" (consulted during compilation); state the verdict on an index-digest mismatch by citing RFC11-6; and state that clause→module resolution for the boundary branch is performed from the index's clause map, with the map's digest recorded.

---

### 12. RFC11-8 bars transcripts from mandatory context but not from suggested context — **minor**

**Clause anchor — RFC11-8 (module 1, §2.3), quoted:**

> "**Raw chat history is not canonical project memory.** Raw prompts, private chain-of-thought, and chat transcripts are never canonical memory and are never mandatory context. … Promotion from transcript to memory is an explicit, attributable act, not an ambient side effect."

[Observed] The prohibition is scoped to canonical memory and to mandatory context. RFC11-5 independently permits inference to "add suggested context, with provenance marking it suggested and by what." Sweep of both clauses: no text in either bars unpromoted transcript content from entering as a suggested member. The only barrier is the provenance mark.

[Observed] The package's own violation case 5 names the harm — "*(RFC11-8)* A planning chat's conclusions are cited as project authority ('as agreed in the transcript') without promotion to a governed decision" — and the packet, as specified, may carry exactly that content one label away from the mandatory core, inside the same digested artifact (finding 2).

[Inferred] Adopted doctrine constrains the consequence independently: `trust-and-evidence.md` holds that "**Inference holds no positive status authority — it holds challenge authority only.**" So the risk is bounded in principle. But RFC-0011 does not state the bound, and RFC11-8's intent — the wording "never … mandatory context" — plainly extends further than its text reaches. This is the sole carry-forward path I found by which stale content can sit inside a fresh packet.

**Repair:** extend RFC11-8's second sentence to state that unpromoted transcript material does not enter a packet in any layer, or state explicitly that it may enter only as suggested context, marked with its unpromoted status, and never counted toward completeness.

---

## Summary

| # | Severity | Subject |
|---|---|---|
| 1 | blocking | RFC11-12 coverage range 1..12 vs a 1..16 package; README prose contradicts the clause |
| 2 | blocking | Inferred layer inside the single-digest packet; digest determinism unstated and unattainable |
| 3 | major | Agent/model profile absent from RFC11-1's packet members |
| 4 | major | Packet durability unspecified; RFC11-2's binding degrades to Unknown |
| 5 | major | "Incomplete evidence" undefined, no consequence stated |
| 6 | major | Omission-register `reason` unstructured |
| 7 | major | "Mandatory" defined only in module 2; C1 fallback is README prose |
| 8 | major | RFC11-14(2) disposal vacuous for 6 of the package's own 10 declared edges |
| 9 | major | README carries obligations no clause states |
| 10 | minor | RFC11-13 grammar cannot express `craft-policy` |
| 11 | minor | "Loading" undefined; index rule and clause→module resolution ambiguous |
| 12 | minor | Transcripts barred from mandatory but not suggested context |

**What is sound and should be recorded as such.** [Observed] The clause map is exact — 16 clauses, each defined exactly once, no gaps, no duplicates, module rows matching the bodies byte-for-byte; no clause is stranded between the modules. Citation direction across the seam is correct for a C1-then-C2 acceptance order: module 1 cites nothing from module 2. RFC11-14 is a genuinely well-specified traversal — nine numbered rules, explicit non-transitivity, explicit "Citations are not reliances," explicit undecidable-fails-closed. RFC11-6's fail-closed default and RFC11-13's routing of a missing declaration to packet incompleteness are both stated with consequences attached, which is the discipline findings 5 and 11 ask for elsewhere. The question-numbering scheme across §8 is coherent (q1 in module 2; q2, q3 in module 1; README table matches).

Findings 1 and 2 are edits that must land before this package is offered: finding 1 because a Wave C1 act would bind a coverage obligation the index already contradicts, and verification rule 10 forecloses repair afterwards; finding 2 because the single-digest structure conflicts with adopted doctrine's deterministic/inferred seam, which a candidate cannot be offered against. The seven major findings are repairable within the same pass and, in my judgment, should be — findings 3, 4, and 5 together are what stands between review question 4's answer being Observed and its being Inferred.

VERDICT: REVISE
