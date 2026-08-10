# RD-30 — Owner-packet review (round-2026-08e, frozen commit 4599701)

## 1. Subject identification

**Subject.** The frozen clone at `…/scratchpad/clone-08e-r6`, `git log --oneline -1` = `4599701 round-2026-08e: the RD-29 human-language repair batch — the navigation layer catches up to the record layer`. [Observed] No file outside that clone was read; the live repository at `/home/tze/GitHub/syzygy` was not consulted. Nothing was edited or created.

**Population reviewed** — the launch-critical set as the register's launch-scope index defines it (`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md:114–135`):

| Gate | Route as offered | Packet file exists? |
|---|---|---|
| P-31 | register row `:167` + named sources | **no** |
| P-33 | `decisions/WAVE-A-INSTALL-SHAPE-DECISION.md` | yes |
| P-37 | `decisions/PROJECT-SHAPE-FACETS-DECISION.md` | yes |
| P-38 | `decisions/HUMAN-ENTRY-DECISION.md` | yes |
| P-39 | `decisions/OPENSPEC-FORM-AND-VERSION-DECISION.md` | yes |
| P-40 | `decisions/SPECIFICATION-GRANULARITY-DECISION.md` | yes |
| P-41 | register row `:178` + `policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` | **no** |
| P-34 | `decisions/LAUNCH-GATE-AUTHORITY-DECISION.md` | yes |
| P-35 | `decisions/PROJECT-OPERATING-CONSTRAINTS-DECISION.md` | yes |
| P-36 | `decisions/UNKNOWNS-AND-GAPS-DECISION.md` | yes |

Packet-existence sweep, denominator stated: 15 files in `.syzygy/governance/decisions/`, Python `re` per identifier — **8 packets found; P-31, P-41, P-22 and P-28 have none.** [Observed]

Also on the table per charter: acceptance record §7 (15 items, `…/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:399–512`) and §1 rows A and B (`:22–23`).

## 2. Method

Read-only. Orientation in the charter's order (`AGENTS.md` → `PROJECT-STATUS.md` → register launch-scope index), then the ten routes above, then §7 and §1. Load-bearing text matching used `grep -F` or Python `re` throughout (rule 1). Digests recomputed, never transcribed (rule 3). Absence claims carry denominators (rules 2/9). Every finding quotes the sentence it anchors to with file and line.

**Mechanical checks run this session, in the clone (rule 7):**

- `sha256sum wave-manifests/*.txt` → Wave A `8af6805f…62de7`, Wave B `c0fd0e27…08261`. Both **match §1 rows A and B byte for byte.** [Observed]
- `sha256sum -c wave-manifests/WAVE-A-MANIFEST.txt` → **19 of 19 `OK`, 0 non-OK lines.** Wave B → **11 of 11 `OK`, 0 non-OK lines.** [Observed]
- `python3 scripts/check_governance.py` → **30 OK, 18 WARN, 0 FAIL (48 checks).** Relevant lines read, not the exit code (rule 4): `CG-7b wave-act arguments match the wave manifests — 6 arguments examined, 0 findings`; `CG-7a … 78 entries examined, 0 findings`; `CG-14 acceptance install routes valid — 12 paths examined, 0 findings`; `CG-24 … 18 of 25 check families have at least one fixture`. [Observed]

**Simulated-sitting log.** Reading time is my own, recorded per route; I do not scale it to a human and say so plainly. "Extra files" counts files I had to open *because the packet did not carry what it needed*, not files I opened to audit the packet's accuracy (audit opens are listed separately in the findings).

| Route | Read | Extra files the owner must open | Why |
|---|---|---|---|
| P-31 (register row) | 6 min | 3 — `RFC-0002/reconciliation-chain.md`, acceptance record §7 item 12, RD-15 raw | The row names no packet; the actual two-route statement lives in a bracketed note inside the contract module (`reconciliation-chain.md:243–252`) |
| P-33 | 4 min | 1 — `RFC-0003/governance-homes-and-owner-acts.md` | To check whether RFC3-15(a) provides the route the packet says it provides (it does not — RD30-06) |
| P-37 | 3 min | 1 — `RFC-0006…` (fruitlessly) | The packet's "as drafted" has no referent (RD30-01) |
| P-38 | 4 min | 0 | Self-contained |
| P-39 | 4 min | 0 (lock quoted accurately) | Self-contained; but see RD30-15 |
| P-40 | 3 min | 1 — `FIRST-OPENSPEC-SEQUENCE.md` | "the current `FIRST-OPENSPEC-SEQUENCE.md` already follows this rule de facto" is the packet's only evidence for option (a) |
| P-41 (register row) | 8 min | 3 — the candidate policy, `craft-and-care/INSTALL-RECORD.md`, `ACCEPTANCE-PHRASE-REGISTRY.yaml` | No packet, no phrase, no recommendation (RD30-07) |
| P-34 | 7 min | 0 | Strongest packet in the set; states its own transaction |
| P-35 | 4 min | 0 | Self-contained; owner-knowledge only |
| P-36 | 3 min | 0 | Self-contained |
| §7 (15 items) | 14 min | 4+ | Items 1/2/3/5/14 have no packet and no register row |
| §1 rows A/B + ceremony §2 | 11 min | 0 | Procedure is stated; digests recompute |
| **Total** | **≈71 min** of reading, plus the mechanical checks | **13 distinct extra files** | |

## 3. Findings

### RD30-01 — BLOCKING — P-37's "as drafted" describes nothing that is drafted

`decisions/PROJECT-SHAPE-FACETS-DECISION.md:37–42`:

> ## Current authority
>
> Candidate RFC-0006 (RFC6-18/19 as amended at round-2026-08d: work state
> and chain state never folded; uncomputed reconciliation renders Unknown).
> **Wave A ratifies the drafted form**; this ruling is the owner's chance to
> amend before that act.

and `:46` — "**(a)** Seven facets as drafted, rules 1–4 above."

**Sweep, this session, with denominator.** Python `re`, case-insensitive, over **all 19 modules of `WAVE-A-MANIFEST.txt` and all 11 modules of `WAVE-B-MANIFEST.txt` (30 modules, the complete Waves A+B digest sets)**:

| Facet name | Wave A hits (19 modules) | Wave B hits (11 modules) |
|---|---|---|
| `Shape present` | **0** | **0** |
| `Human-understandable` | **0** | **0** |
| `Mission-ready` | **0** | **0** |

[Observed] Confirmed by a second method: the corpus-wide sweep for `Shape present` returns exactly one hit outside history — `round-2026-08d/OWNER-WORK-ORDER.md:1008`, the owner's work order, which is not in any manifest.

The two `facet` occurrences in Wave A are `RFC-0006…:401` ("a facet outside this tuple is checked by nothing" — parity scope) and `:564` ("how another surface renders a facet this contract defines" — forward-reference notice). Neither defines a shape-facet vocabulary. RFC6-18 is *"One drawer, one fact set"* and RFC6-19 *"Drawer content classes"* — eight content classes, not seven project-shape facets. Anchored to the defined clauses and quoted (rule 8).

**Consequence.** The claim propagates to two more launch-path documents: acceptance record §7 item 13 (`:490–494`) — *"the act settles the facet vocabulary RFC-0006's drawer queries expose"* — and `FIRST-OPENSPEC-SEQUENCE.md:53` — *"P-37 project-shape facets | Owner decision | **blocking** (Wave A ratifies the drafted form)"*. An owner who rules (a) believes the Wave A act binds the seven-facet vocabulary; it does not, and no act in the corpus does. An owner who considers (c) "Fewer facets" is told the cost is "re-review of RFC-0006/0008" — a cost that does not exist, because RFC-0006/0008 do not carry the facets. Both arms are mispriced. This is the charter's VIS-4 test failing directly: an "as drafted" option that does not describe what is drafted.

### RD30-02 — MAJOR — the register's launch-scope index contradicts P-36's own packet on when P-36 must be ruled

`PENDING-OWNER-DECISIONS.md:127–129`:

> - **Gate the formal launch administration, not the spec:** P-34
>   (instrument authority), P-35 (operating constraints), P-36
>   (Unknown vs Gap — on the acceptance-criteria vocabulary path).

`decisions/UNKNOWNS-AND-GAPS-DECISION.md:72–75`:

> ## Earliest required gate
>
> **Before OpenSpec Capability 1 is authored** (its acceptance criteria use
> both words).

`FIRST-OPENSPEC-SEQUENCE.md:52` agrees with the packet: "P-36 Unknown vs Gap | Owner decision | **blocking** (acceptance criteria use both words)". The index's own tie-breaker (`:135`, "Where this index and a row disagree, the row wins") does not resolve this, because P-36's **row** (`:173`) states no gate at all — only the packet and the sequence do. An owner triaging by the index would defer P-36 to the administration phase and could author Capability 1 without it, which is the exact "unresolved shape chosen by the first spec" failure the packet exists to prevent (`:44–48`).

### RD30-03 — MAJOR — the launch-scope index omits two rows whose own text says a launch wave ratifies them

`PENDING-OWNER-DECISIONS.md:120–124` names the Wave A gates as P-31/P-33/P-37 and the Wave B gate as P-38 only. But:

- `:163` (P-28) — *"**Ground changed 2026-08-09 (round 08d):** option **(b)** is drafted into candidate bytes — RFC1-7 carries a mission extension profile with named minting authority and RFC10-4 grounds Mission identity in it (semantic deltas A-2/A-7). **Accepting Wave A ratifies the profile**"*. Verified in the bytes: `rfcs/RFC-0001-project-graph-identity-state-planes.md:196` defines RFC1-7 and `:206–208` carries *"**mission** (Mission and Attention Item identities and their relations — mission-targets, attention-blocks…)"*. RFC-0001 is a Wave A module. [Observed]
- `:152` (P-22) — *"**Re-grounded 2026-08-10 (round 08e):** RFC9-8(a) now stands entirely on Wave A … **Accepting Wave B ratifies the placement**; the revert option (workspace manifest) restores the RC-4 contradiction."*

Neither appears in the launch-scope index, and neither has a §7 item. Review RD-26 recorded this defect class as *"RD26-02 — P-31/P-33/P-37 each name the Wave A act as their earliest gate and none appears in the acceptance record (the RD-8 surprised-act class, three instances)"*; the repair added §7 items 11/12/13 for those three and left these two. The class is not closed — two further instances survive at this commit.

### RD30-04 — MAJOR — the register contradicts itself, and the packets file, on the only current route for P-22

`PENDING-OWNER-DECISIONS.md:183–185`:

> **Current-packet notes (2026-08-10):** … the round-08d
> `OWNER-DECISION-PACKETS.md` remains current for packets 1, 3, 4, 5, **6**, 9,
> and 12.

`PENDING-OWNER-DECISIONS.md:152` (P-22's own row): *"Packet 6 of `round-2026-08d/OWNER-DECISION-PACKETS.md` is stale and banner-marked"*.

`round-2026-08d/OWNER-DECISION-PACKETS.md:16`: *"Packets 1, 3, 4, 5, 9, 12 remain current here. **Packet 6 is stale…**"* — and the banner continues, *"Do not act from packet 6 below."*

Two of the three statements say stale; the register's summary note says current. Combined with RD30-03, the one launch-critical route the index does not name (P-22, ratified by Wave B) is also the one whose packet status the register gets wrong.

### RD30-05 — MAJOR — nothing on the owner's route tells them to read acceptance record §7 before an act

§7 is titled *"Items requiring explicit owner attention **at the gate**"* (`:399`) and carries fifteen items, of which items **1, 2, 3, 5 and 14** have no packet and no register row. Item 1 is load-bearing: *"RFC 0003 §8 q4 — the `declarations/` category: rule it (or knowingly ride the drafted default into the accepted digest). The default is load-bearing, not passive: RFC3-15's drafted text is a **six-name closed validator**"* (`:401–410`). Item 14 names two further drafted repairs the Wave A act ratifies (`:495–502`), both verified present in Wave A bytes (`RFC-0003/governance-homes-and-owner-acts.md:89`; `RFC-0004/execution-record.md:97`).

Sweep for a pointer at §7, denominator four routed files (`AGENTS.md`, `PROJECT-STATUS.md`, the register, the acceptance record; Python `re` for `§\s*7|section 7|owner.attention`): `PROJECT-STATUS.md` — **zero hits**. `AGENTS.md` — zero. The register — three hits, all specific (`:12` item 15, `:93` item 8, `:121` P-31/33/37). The acceptance record itself — the ceremony at §2 (`:123–201`, five steps: phrase, digest verification, installation, act record, commit/tag) **never mentions §7**, and §1's one "read before any wave act" marker (`:33`) is the wave-history note, not §7. [Observed]

An owner can execute the §2 ceremony end to end without ever meeting §7. The record's own §5 (`:333`) calls RFC 0003 §8 q4 the one question "to close at this gate" — and the gate procedure does not route there.

### RD30-06 — MAJOR — P-33's recommended option misdescribes the clause it invokes, and the option the clause implies is not offered

`decisions/WAVE-A-INSTALL-SHAPE-DECISION.md:27–40`:

> - **(1b)** **Amend RFC3-15's `contracts/` cell by its own RFC3-15(a)
>   recorded-widening route** — the clause already defines how its closed
>   table lawfully widens…
>
> **Recommendation `[Inferred]`: (1b)** — it is the route the clause itself
> provides for exactly this…

The clause says the opposite. `RFC-0003/governance-homes-and-owner-acts.md:91–99` (RFC3-15(a), quoted as the defined clause per rule 8):

> **RFC3-15(a) — Why `records/` exists** (owner decision **B19**). … The
> fifth category is an explicit widening of a structure this RFC calls
> constitutional, made by owner amendment **rather than by stretching a
> category's "exclusively"** — the precedent any future widening follows.

and the module's own closing guidance at `:521–523`:

> B19's precedent — **widen explicitly rather than stretch a category's
> "exclusively"** — is the pattern either answer should follow.

RFC3-15(a) records a route for adding a **new category**; (1b) widens what an **existing category may contain**, which is precisely "stretching a category's 'exclusively'". The packet presents the clause as sanctioning the move it names as the thing to avoid. Consequently the option the clause's own pattern implies — a new constitutional category for companion material — is absent from the three options offered. An owner ruling (1b) on the packet's stated justification would be ruling on a false premise, and the act would then bind an RFC3-15 amendment made against RFC3-15's own recorded precedent.

### RD30-07 — MAJOR — P-41 is a blocking launch prerequisite with no packet, no phrase, and no recommendation

`FIRST-OPENSPEC-SEQUENCE.md:55`: *"P-41 specification acceptance standard in force | Craft act | **blocking**"*. `PENDING-OWNER-DECISIONS.md:178` states the ask: *"Wanted: review + its `CONFIRM CRAFT AMENDMENT` act (digest computed at the act and recorded in the craft `INSTALL-RECORD.md`, per the CC-TEST-2 precedent), or a recorded ruling to author knowingly against the candidate."*

What the owner does not have, verified this session:

- **No packet.** 15 files in `decisions/`; Python `re` for `P-41` finds it in none but the register. [Observed]
- **No phrase.** `ACCEPTANCE-PHRASE-REGISTRY.yaml` carries **12 `current_phrases`**; the only craft entry is `label: "CONFIRM CRAFT AMENDMENT: CC-TEST-2"` with `subject: …/testing-and-verification.md`. No CC-SPEC entry, no subject path, no argument form. [Observed]
- **No recommendation**, labeled or otherwise — unlike all 8 packets, which carry one.
- **No review.** The candidate was proposed the same day (RD-28 finding RD28-05); `craft-and-care/INSTALL-RECORD.md:127–134` records it as *"a pointer so the cluster is aware of the namespace minting into it — it installs nothing."*

The register row's own indictment — *"the owner had no route to satisfy the prerequisite"* — is only half repaired: there is now a queue entry, but still no performable act. Compare P-34, which states its transaction in four numbered steps with the approval block verbatim (`LAUNCH-GATE-AUTHORITY-DECISION.md:83–103`). Nothing in the sitting can close P-41; the honest statement is that it needs a review pass first, and no packet says so to the owner.

### RD30-08 — MAJOR — P-38 offers four options and costs three; the uncosted one is the arm that answers the newly disclosed ruling

`decisions/HUMAN-ENTRY-DECISION.md:55–58`:

> - **(d)** Keep the fixed entry but sever the identity: the entry is a thin
>   index distinct from the primary narrative (two documents, one door) —
>   redraft RFC7-39's "there are not two front doors" sentence before the
>   Wave B act.

The `## Consequences` block (`:60–66`) carries `(a)`, `(b)`, `(c)` and stops. The recommendation (`:70`) is *"`[Inferred]` **(a)**; (b) remains reachable later as OpenSpec-level work"* — (d) is not mentioned. Option (d) is the arm the packet's own disclosure block (`:29–34`) and acceptance record §7 item 15 (`:504–512`) exist to open: *"This is a substantive answer the pass made, not a derivation; the owner may prefer a thin index entry distinct from the narrative."* The one option that responds to the disclosed drafting posture is the one the packet declines to price. The charter's decidability bar — "each option's cost honestly" — is met for 3 of 4.

*(Passing, and worth recording: the packet's four-value domain is now exact. `RFC-0007/rendering-and-surface.md:422–423` — "**The answer domain is closed at four values** — **`yes` / `no` / `not-applicable` / `Unknown`**". RD-27's RD27-02 three-vs-four defect is repaired.)*

### RD30-09 — MAJOR — the register promises an owner-facing offering that does not exist

`PENDING-OWNER-DECISIONS.md:81–84`:

> The acceptance record's per-wave owner-attention material remains part of
> each wave's knowing acceptance; the round-2026-08d owner-facing offering
> (produced after that round's review pass) **will state each wave's
> imperfections before its phrase**.

Sweep, denominator stated: `ls round-2026-08d/` → 9 entries (`ACCEPTANCE-WAVE-DESIGN.md`, `CLONE-VERIFICATION.md`, `FIRST-OPENSPEC-SEQUENCE.md`, `OWNER-DECISION-PACKETS.md`, `OWNER-WORK-ORDER.md`, `POST-INSTALL-LINK-REPORT.md`, `reviews/`, `SEMANTIC-DELTA-RECORD.md`, `STRUCTURAL-CLOSURE-PREFLIGHT.md`) — **none is an offering.** Python `re` for `owner-facing offering` over all `*.md` under `contracts/candidates/` excluding `history/` → **21 hits, none an 08d offering artifact.** `find -iname '*OFFER*'` → **0 files.** [Observed]

This is the artifact the launch-gate pilot already recorded as absent — `round-2026-08d/reviews/LAUNCH-GATE-ADMINISTRATION-2026-08-09-RAW.md:84`: *"F3 | **Not met** | The packet that would make each wave act knowing **does not exist at this commit, by the project's own statement**."* The pilot quoted `PROJECT-STATUS.md:50-54`; that sentence is gone from `PROJECT-STATUS.md` at this commit, and survives in the register. Together with RD30-05 this is the load-bearing gap in the sitting: the "imperfections before the phrase" material has no home the owner is routed to, and the register still points at one that was never written.

### RD30-10 — MINOR — the current first-spec document defines Capability 1's scope by pointer into the revision it supersedes

`FIRST-OPENSPEC-SEQUENCE.md:5–7` — *"**This is the single current first-spec document**: it supersedes `round-2026-08d/FIRST-OPENSPEC-SEQUENCE.md` (revision 2)"* — then `:26–28` — *"Scope as in revision 2 (rows 1.1–1.6 with the round-08d corrections…)"*. To learn what Capability 1 actually covers, the owner opens the superseded file. Banner-marked, so not the RD-8 class outright, but a self-containment cost on the one document that names the launch target.

### RD30-11 — MINOR — P-31's register-row recommendation is a drafting instruction for an arm already drafted

`PENDING-OWNER-DECISIONS.md:167`: *"Recommendation `[Inferred]`: draft the exemption arm; ruling wanted before Wave A is re-offered so the drafted arm is ratified knowingly"*. The arm is drafted — `RFC-0002/reconciliation-chain.md:224–252`, disclosed in a bracketed `[P-31 — drafted arm, awaiting an owner ruling.]` note. Unlike P-21, P-22, P-23 and P-28, the row carries no "Ground changed" marker, so the recommendation reads as an instruction the owner cannot act on. The index parenthetical (`:120`, "drafted RFC2-19 arm") is correct; the row it indexes is behind it.

*(The disclosure itself is exemplary and should be preserved: `:248–250` — "it is **drafted here so the owner can rule on a written arm rather than on a description**; it is candidate text like every clause around it".)*

### RD30-12 — MINOR — the P-31 exemption is normative text with no clause identifier

The exempting sentence — `RFC-0002/reconciliation-chain.md:227–230`, *"the `reconciliation-pending` state and the 'reconciliation evidence absent / Unknown' rendering it produces are **never stamped with, counted among, or absorbed by an aggregate of RFC2-24 Unknown reasons**"* — sits under a bolded lead-in, *"**What that Unknown carries, and does not**"* (`:224`), between the RFC2-19 and RFC2-20 clause headings. It carries no `RFC2-n` identifier of its own. Verification rule 8 exists for exactly this shape: a reader anchoring the exemption must cite RFC2-19, whose defined text is "Trigger and staging". Record or number it.

### RD30-13 — MINOR — hidden dependency: P-41's candidate policy cites P-40's rule by identifier

`policy-candidates/SPECIFICATION-ACCEPTANCE-POLICY-CANDIDATE.md` CC-SPEC-1: *"The specification names one coherent capability (per the granularity rule, P-40)"*. If the owner rules P-40 option (b) or (c), CC-SPEC-1's content changes without CC-SPEC-1 changing. No packet or register row states that P-40 must be ruled before P-41's act. Ruling order matters and is unstated.

### RD30-14 — MINOR — acceptance record §6 is stale as the record of review state

`FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:383–384`: *"**No CONFIRM verdict is bound to the current argument** — eight independent reviews ran on 2026-08-07 and every verdict was `REVISE`"*. The headline claim is true and important. But §6's supporting narration stops at 2026-08-07; it never mentions the round-08d fifteen reviews or the 08e fleet, both of which §1's wave-history note (`:44–58`) does carry. A reader who consults §6 — the section titled "Verification and review state" — learns a review history two rounds behind.

### RD30-15 — MINOR — P-39's recommendation defers a load-bearing fact out of the sitting

`decisions/OPENSPEC-FORM-AND-VERSION-DECISION.md:45–49`: *"`[Inferred]` **(a)** … **unless** the pre-decision diff in (b) shows the 1.3.1 format is already superseded … The deciding fact (the format delta) is checkable in minutes at decision time and should be checked then, not guessed now."* The honesty is right; the cost claim is `[Unknown]` and untested — the check requires fetching two npm package versions from outside the clone, which no other item in the sitting needs. Either state it as a pre-sitting task or mark its cost Unknown.

## 4. What passes

Stated with the evidence, not asserted.

- **Both wave arguments are current.** `sha256sum` of the two manifests reproduces §1 rows A and B exactly; per-module verification is 19/19 and 11/11 `OK` with zero non-OK lines; `CG-7b` reports 6 arguments examined, 0 findings. The §1 rows' account of what changed (Wave A: seven modules, RD-26 batch; Wave B: regenerated twice, retiring `daa6a5dd…` then `2041ad05…`) is consistent with the manifests being the generator's current output (`CG-7a`, `CG-7g`, `CG-7f` all OK). [Observed]
- **The ceremony's mechanical procedure is stated where the owner will find it.** §1's block at `:112–121` — *"**Before performing any act, verify its argument mechanically:** `python3 scripts/check_governance.py` … A CG-7 failure means the artifact moved after this record was written: **do not perform that act**"* — and §2's five steps, including the per-wave `sha256sum -c` from two named directories. `CG-14` confirms all 12 install routes resolve. This is the charter's "phrase, digest, CG-7" question, and it is answered.
- **The battery is green in the clone at this commit** — 30 OK, 18 WARN, 0 FAIL over 48 checks, with `CG-24` printing its own coverage (18 of 25 families have a fixture; the seven without are enumerated). No "all checks" claim is made anywhere I read.
- **Packet form is uniform.** 8 of 8 packets (denominator stated) carry "This file decides nothing", a labeled `[Inferred]` recommendation, an options set, "Earliest required gate", and "Independent work". No packet pre-decides; every one names its arm as candidate text the owner ratifies or reverts.
- **P-34 is the model.** Its every checkable claim held: `launch-gate-pre-specifications.md:4–5` `status: candidate process policy — owner approval pending`; `:7` `effective_version: v1.5`; the `governs:` list at `:8–11` matches the packet's list item for item; the v1.4 delta carries exactly ten sections `D-1`…`D-10` and D-8 adds three questions (C7, F5, F6) from the pilot's G1, with the delta's own header stating *"no existing question's fail condition was narrowed, no verdict word was opened, no ID renumbered."* The RD24-01 blocking finding is visibly repaired: the mechanism now orders the status edit **before** the digest (`:79–88`).
- **P-39's substrate-lock facts are exact.** `GOVERNANCE-SUBSTRATE-LOCK.yaml:181–195` — `distribution: "npm: @fission-ai/openspec"`, `installed_version: "1.3.1"`, `latest_published_at_lock_time: "1.7.0"`, `compatibility: [Unknown]`, `"Pin at the first openspec/ write."` The packet's "(from the substrate lock, verified)" is earned.
- **P-35, P-36, P-40** are self-contained, single-question, exhaustively optioned and honestly costed. P-35's "inventing a value is worse than recording Unknown" and P-36's "A sweep at ratification confirms this with a denominator (rule 9) before the no-change claim is relied on" are the discipline the charter asks for, applied to the packets' own claims.
- **P-38's four-value domain** now matches RFC7-40 exactly (RD-27's finding repaired), and the entry-identity disclosure is present on the gate path in both the packet and §7 item 15.

## 5. Overall assessment

**Is it one sitting?** Not as currently routed. The reading itself is close — roughly 70 minutes across eight packets, two register rows, §7 and the two act rows, which a determined owner could do in one long session. What breaks the sitting is not length but the thirteen extra files the routes force open, and the fact that three of the launch-critical items **cannot be closed in the sitting at all**: P-41 needs a review pass and has no phrase to perform (RD30-07); P-39's deciding fact is deferred to an out-of-clone check (RD30-15); and P-33 as offered cannot be ruled correctly because its recommendation rests on a misreading of the clause it amends (RD30-06). Realistically this is one sitting of *reading* and a second, later sitting of *ruling*, and the packets should say so rather than imply otherwise.

**Would the owner rule knowingly?** On six of the ten — P-34, P-35, P-36, P-40, and (with the noted gaps) P-38 and P-39 — yes, and those packets are genuinely good: they state the question once, price the arms, label the recommendation, and disclose the drafted posture instead of smoothing it. On the other four, no. P-37 asks the owner to ratify a vocabulary that is not in the bytes the act binds, and three separate documents repeat that claim — an owner ruling (a) would believe the Wave A act settles something it does not touch. P-33 recommends an amendment on the grounds that the clause provides the route, when the clause's own recorded precedent says do the opposite and the option that precedent implies is not offered. P-41 has no performable act. And the Wave A and Wave B acts themselves still ratify at least two open questions — P-28's mission extension profile and P-22's registry placement — that appear in neither the launch-scope index nor §7, while nothing on the ceremony's route sends the owner to §7 in the first place and the register still promises an "imperfections before the phrase" offering that was never written. The arguments are current and the machinery verifies; the *navigation to what the acts ratify* is where the surprised-act class that RD-8 named, and RD-26 partially closed, is still alive. Repair RD30-01 and RD30-03/04/05/09 and this set becomes rulable; leave them and the owner performs an act whose full content no document they were routed to disclosed.

VERDICT: REVISE
