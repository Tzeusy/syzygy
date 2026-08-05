# Pending owner decisions — register

> **Status: every item below is PENDING. This file decides nothing, adopts
> nothing, accepts nothing.** It makes the open decision queue explicit and
> clone-visible. Each row points at the record that owns the full detail;
> where this file and an owning record disagree, the record wins and this
> file is stale.
>
> **As-of: 2026-08-05**, regenerated at the close of the human-clarity
> refactor round (owner round prompt §7). The previous revision (as-of
> `adddc34`) is superseded: it listed P-6/P-7/P-8/P-9/P-11 as open when the
> round executed them, and routed most owning records to the git-excluded
> `_bootstrap/` tree that a clone cannot read.
>
> **Owning records are now clone-visible** except where a row says otherwise.

## The acceptance acts (none performed)

Exact phrases, digests, and the five-step ceremony live in
`../contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md`.
**Verify every digest before acting** — `python3 scripts/check_governance.py`
(check CG-7) compares each act argument against its subject artifact; a
CG-7 failure means "do not perform that act."

| # | Decision | Owning record |
|---|---|---|
| P-1 | **Act 1** — accept the 32 compacted foundational contract modules | acceptance record §1 row 1; subject `contracts/candidates/rfcs/`, digest `contracts/candidates/ACTIVE-CONTRACT-MANIFEST.txt` |
| P-2 | **Act 2** — confirm craft amendment CC-TEST-2 | acceptance record §1 row 2; digest block in `../policies/craft-and-care/INSTALL-RECORD.md` (2026-08-05 correction) |
| P-3 | **Act 3** — accept the topology bundle | acceptance record §1 row 3; `../../map/topology-candidates/BUNDLE-MANIFEST.md` |
| P-4 | **Act 4** — adopt the project overview | acceptance record §1 row 4; `../../intent/OVERVIEW.md` (refactored this round; the authoring-time status section that previously froze into the digest is gone) |
| P-5 | **Optional act 5** — adopt, amend, or decline the D3 bounded-mission doctrine amendment | `../contracts/candidates/DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1 — supersedes the original `…-DRAFT.md`, whose `vision.md` insertion cannot be applied as written) |

The acceptance record's §7 owner-attention items remain part of P-1's knowing
acceptance.

**Act ordering (recommendation, not a rule):** perform act 1 before act 5.
Adopting D3 first would leave *bounded mission* and *autonomy envelope* as
adopted doctrine terms whose binding definitions live only in an unaccepted
contract; act 1 first removes that gap under every outcome of the D4 question
(acceptance record §7 item 8).

## Resolved during the 2026-08-05 round (recorded, not decisions to make)

| # | What happened |
|---|---|
| P-6 | **Executed.** The retired phrase was removed from both digest sets — `rfcs/RFC-0003/governance-homes-and-owner-acts.md` (act 1) and topology `README.md` (act 3). Both manifests regenerated; semantic deltas SD-1/SD-2 |
| P-7 | **Executed.** All nine canonical craft files now describe themselves truthfully as canonical; rule text byte-unchanged; digests regenerated (SD-3) |
| P-8 | **Executed.** `INSTALL-RECORD.md` binds craft force to the digest-bound acceptance act, not the retired phrase (SD-4) |
| P-9 | **Executed.** Candidate contracts, topology, acceptance record, reviews, validation scripts, decision warrants, and the license packet are tracked and clone-visible; raw interviews and bootstrap history stay founder-local (FD-021/FD-037) |
| P-11 | **Executed.** README, AGENTS.md, PROJECT-STATUS.md, CONTRIBUTING.md, SECURITY.md installed; `.gitignore` verified |
| P-13 | **Executed.** The overview's progressive-disclosure refactor landed (SD-9); its adoption is P-4 |

## Open, and only the owner can dispose

| # | Decision | Owning record |
|---|---|---|
| P-10 | **Review coverage.** The round commissioned eight independent verticals (`contracts/candidates/round-2026-08/reviews/`) covering the term registry, hygiene policy, fixtures, Mission material, and front door — the gaps the previous register named. **What remains genuinely uncovered:** RFC-0006 has *no* clause-level routing classification at all (the earlier register misdescribed an existing-but-unreviewed matrix; the artifact does not exist). Accept the deferral to RFC6-28's coverage matrix at surface specification, or commission the classification now — `RB-4-contract-compaction-RAW.md` §4.2 offers a first-pass for all 28 clauses | round reviews; `SURFACE-CLAUSE-ROUTING-MATRIX-REV10.md` |
| P-12 | **Knowledge-hygiene craft policy** (CC-KNOW-1…18, CC-BUDGET-1…4) — needs its own `CONFIRM CRAFT AMENDMENT` act. Six sub-questions listed at the policy's foot (which optional rules to keep; one file or two; whether the proposal apparatus installs with the rule text) | `../contracts/candidates/policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` |
| P-14 | **License choice** — four candidates, three `[Unknown]`s including copyleft reach into governed repositories; wants qualified legal review. Not to be chosen autonomously | `LICENSE-DECISION-PACKET.md` (this directory) |
| P-15 | **Founder decision log** — FD-n identifiers are still cited from tracked files while the log itself is founder-local. Two warrants were extracted this round (`DOCTRINE-AMENDMENT-D1-MAP-HISTORICAL.md`, `OWNER-ANSWERS-2026-08-01.md`); decide whether a compact FD register follows them into this directory | round preflight; FD-037 |
| P-16 | **Vocabulary.** The term registry (30 terms, T-01…T-30) canonicalizes the six-plane state model and separates it from claim labels, evidence tiers, work lifecycle, and governance lifecycle. Approve it as the working vocabulary, or amend. **Correction to this item as previously written:** there is no "older four-state phrasing" in the corpus — sweeps found zero. The older phrasing that exists is doctrine's own **three-state** thesis, which is adopted and stays governing; the six-plane model is a candidate refinement and a permitted compression relation, not a supersession | `../contracts/candidates/policy-candidates/TERM-REGISTRY.md`; `round-2026-08/TERM-MIGRATION-REPORT.md` |
| P-17 | **Term-registry admission gap** *(new)*: eight of the thirty foundational public terms — State plane, Proposed state, Historical state, Evidence tier, Mission, Autonomy envelope, Attention item, Context packet — have **no adopted definition anywhere**; they exist only in candidate contracts, and the public surface already uses several. Act 1 (and act 5 for the mission terms) closes this; accepting the surface before then is a knowing deferral | term registry §authority coverage; contradiction C-2 |
| P-18 | **Doctrine/contract vocabulary seams** *(new)*: three recorded contradictions the round surfaced but did not resolve — (a) `architecture.md` names **four** constitutional `governance/` categories as "minimums" while candidate RFC3-15 names **five** plus a reserved sixth and calls them "closed"; (b) **"Claim"** is the sole carrier of positive status in candidate RFC1-24 but is absent from doctrine's frozen-noun list; (c) `evidence tier` vs `rendering tier` name one dimension twice. Each is compatible on a plain reading and none blocks an act; all three want an owner ruling before OpenSpec multiplies them | `round-2026-08/TERM-MIGRATION-REPORT.md` (C-1…C-6) |
| P-19 | **Mission-envelope residuals** *(new, post-act-1 candidates)*: RFC-0010 defines checkpointing but **no rollback or compensation** of already-applied effects; RFC10-11 lets already-dispatched work complete past an exhausted budget with no reservation or recording of the overrun (a live *spend* risk, unlike the effect classes the propose-only cap bounds); and no clause names who adjudicates a mission's completion predicate. None blocks act 1; each is an amendment candidate once the contracts bind | `round-2026-08/MISSION-CONTROL-REVIEW.md`; `RB-6-mission-autonomy-RAW.md` |
| P-20 | **Round residuals carried knowingly** *(new)*: the findings the round's own battery raised and did not fix, each recorded with its evidence in `round-2026-08/ROUND-DISPOSITIONS.md` — including the craft cluster's engineering-bar reference to a machine-local skill tree (unreadable from a clone), doctrine's citation of a "README glossary" that does not exist, and the fixture set's incomplete coverage of the charter's eight fixture classes. Accept as disclosed, or direct fixes | `round-2026-08/ROUND-DISPOSITIONS.md` |

**Nothing in this register is self-executing.** Acts happen only by the exact
ceremonies their owning records define, performed by the owner.
