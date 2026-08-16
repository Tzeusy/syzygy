# Decision history — resolved rows and register chronology

> **Historical record, deliberately off the default path.** This file holds
> what the pending register used to carry inline: the resolved-row
> narratives and the register's own as-of chronology. Nothing here is open,
> and nothing here is authority — every ruling below names the record that
> owns it, and that record wins. The live queue is
> [`PENDING-OWNER-DECISIONS.md`](PENDING-OWNER-DECISIONS.md).
>
> Moved here 2026-08-17 (convergence pass, round 2026-08i). The register's
> pre-refactor row narratives — including the long accumulated open-row
> cells — are preserved verbatim in git history at commit `9c43fc5`
> (`git show 9c43fc5:.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`).

## Resolved on 2026-08-16 (owner ruling via adversarially-reviewed questionnaire packet)

Every ruling below is a **recorded decision, not a digest-binding act** —
none performs the Wave A or Wave B act, none runs the formal launch-gate
administration, and none authors OpenSpec. Each ruling was independently
adversarially reviewed (separate scope and recommendation verdicts) before
being presented, per the `user-questionnaire` subskill's mandatory gate; the
full packet, including the review record and one caught-and-corrected error
(a stale-framing discrepancy in an external plan's stated preference on
`P-33`), is the owner's local decision packet, not tracked in this
repository.

| # | What happened |
|---|---|
| P-31 | **Ruled.** Ratify the drafted `RFC2-19(a)` exemption as written — the merged-but-unreconciled Unknown carries no thirteenth reason; the `RFC2-24` list stays closed at twelve. Recorded as **SDR-34**, `SURFACE-DECISION-RECORD.md`. Zero bytes move; the Wave A confirmation is unaffected. |
| P-33 | **Ruled.** Install shape **(M)** — leave the accepted modules' internal path strings alone; install no companion package apparatus; install neither package-wide manifest. Recorded in `WAVE-A-INSTALL-SHAPE-DECISION.md`'s own template. Zero bytes move; both Wave A and Wave B confirmations are unaffected. This was the sole obstacle withholding the Wave A offer — **the offer is now unblocked; the Wave A act itself has not been performed.** |
| P-35 | **Ruled.** Full operating-constraints table filled in (option a) — 1 operator; attention and budget Unknown; independent-review capacity is Claude-family agents plus the owner, with occasional ad hoc other-model-family review; other rows recorded or Unknown. No date or delivery commitment. Recorded in `PROJECT-OPERATING-CONSTRAINTS-DECISION.md`. |
| P-36 | **Ruled.** The two-term rule: no verifying evidence → `Unknown`; evidence of non-satisfaction → `Gap`. Recorded as **SDR-35**, `SURFACE-DECISION-RECORD.md`; the term registry's `T-20`/`T-31` disclosed conflict note collapses to a pointer at that row. Zero bytes move on any contract module. |
| P-37 | **Ruled.** Seven project-shape facets adopted, no cross-facet rollup; drafting site = the Capability 1 specification (site a2), not an RFC-0006 amendment. Recorded as **SDR-36**, `SURFACE-DECISION-RECORD.md`, naming both the facets and the site. Both Wave A and Wave B confirmations are unaffected (the cheaper of the two drafting-site arms was chosen). |
| P-38 | **Ruled.** As drafted (option a): fixed entry `.syzygy/intent/OVERVIEW.md` identified with the primary narrative (RFC7-6, "not two front doors"); four-valued per-repository discoverability finding; propose-only root-README link. Recorded in `HUMAN-ENTRY-DECISION.md`. Zero bytes move; the Wave B confirmation is unaffected. |
| P-39 | **Ruled.** Pin current upstream OpenSpec, at **1.9.0** (refreshed at answer time from the packet's measured `1.8.0`, since upstream had published again and the owner had already upgraded). The schema/template format contract is confirmed byte-identical `1.8.0`→`1.9.0`; other tooling changes exist and are recorded `[Inferred]` non-breaking, not independently verified line-by-line. Recorded in `GOVERNANCE-SUBSTRATE-LOCK.yaml`'s `openspec` block. |
| P-40 | **Ruled.** One OpenSpec change governs one coherent capability, or one coherent change to one. Recorded as **SDR-37**, `SURFACE-DECISION-RECORD.md`. `FIRST-OPENSPEC-SEQUENCE.md` now cites the SDR row instead of asserting the rule in its own voice. Zero bytes move on any contract module. |
| P-34 | **Ruled (approved), arm (a).** The owner first ruled arm (c) after the v2.3 reviews (RD-65/RD-66, both `REVISE`, the fourth consecutive pair) — the structural v2.4 repair was committed (`4dd6e20`) and its review pair RD-67/RD-68 returned `REVISE`/`REVISE`, the fifth consecutive pair. The one structural repair held (no live forgery in v2.4), but two instance-patched class defects recurred as fresh BLOCKING false-`READY` paths. The owner weighed that under arm (c)'s reasoning and on 2026-08-16 ruled arm (a): **approved v2.4 as process policy, residuals disclosed, F5 not promoted**. The readiness standard's "launch-gate is owner-approved" conjunct is satisfied at v2.4; the formal (out-of-family) administration becomes runnable with the two residuals in hand. No unilateral v2.5 was begun; a bounded v2.5 remains an owner option, not a gate. Owning record: `LAUNCH-GATE-AUTHORITY-DECISION.md`. |

## Resolved on 2026-08-06 (owner override, recorded)

| # | What happened |
|---|---|
| P-26 | **Executed.** Owner override: re-pin `th-engineering` to the installed commit `f4cf1c7` (closing the drift instead of holding the 2026-07-30 pin) **and** vendor a byte-identical local copy in-tree at `.claude/skills/th-engineering/` and `.codex/skills/th-engineering/`, superseding the `PUBLIC-CLONE-AUTHORITY-MATRIX.md` "out of scope, do not import" disposition. CC-BAR-1 and CC-TEST-1…6 were re-checked against test-rigor's two new bars and the new engineering-bar Definition-of-Done item; no conflicts found, so no override text changed — `testing-and-verification.md` gained CC-TEST-7 recording the re-check, `engineering-bar.md`'s CC-BAR-1 gained a matching note. Full detail: `../policies/GOVERNANCE-SUBSTRATE-LOCK.yaml` `th_engineering`; `../policies/craft-and-care/INSTALL-RECORD.md` (2026-08-06 correction); `../policies/craft-and-care/README.md` "Adoption by reference" |

## Resolved during the 2026-08-05 round (recorded, not decisions to make)

| # | What happened |
|---|---|
| P-6 | **Executed.** The retired phrase was removed from both digest sets — `rfcs/RFC-0003/governance-homes-and-owner-acts.md` (act 1) and topology `README.md` (act 3). Both manifests regenerated; semantic deltas SD-1/SD-2 |
| P-7 | **Executed.** All nine canonical craft files now describe themselves truthfully as canonical; rule text byte-unchanged; digests regenerated (SD-3) |
| P-8 | **Executed.** `INSTALL-RECORD.md` binds craft force to the digest-bound acceptance act, not the retired phrase (SD-4) |
| P-9 | **Executed.** Candidate contracts, topology, acceptance record, reviews, validation scripts, decision warrants, and the license packet are tracked and clone-visible; raw interviews and bootstrap history stay founder-local (FD-021/FD-037) |
| P-11 | **Executed.** README, AGENTS.md, PROJECT-STATUS.md, CONTRIBUTING.md, SECURITY.md installed; `.gitignore` verified |
| P-13 | **Executed.** The overview's progressive-disclosure refactor landed (SD-9); its adoption is P-4 |

## The register's as-of chronology (oldest last)

- **2026-08-16** — eight rows ruled by the owner in one adversarially-reviewed
  questionnaire-packet sitting: P-31, P-33, P-35, P-36, P-37, P-38, P-39,
  P-40; P-34 ruled arm (c) then arm (a) the same day (see above).
- **2026-08-13** — P-43 and P-44 added; P-41/P-42 candidates amended against
  RD-51 and the two bounded packets added to the decisions home; P-34's row
  compressed (owner charter §8) after growing to 1,280 words of chronology.
- **2026-08-10** (round 2026-08e, launch closure) — rows P-25(c), P-34…P-41
  added (P-41 the same day, RD28-05), P-22 re-grounded, P-38 corrected to
  RFC7-40's four-value domain; the RFC7-39 entry-identity ruling disclosed at
  the acceptance record's §7 item 15 travels on P-38's packet; launch-scope
  index added before the open table (RD29-06).
- **2026-08-09** (round 2026-08d, structural closure) — the single
  foundational-contract act P-1 was restructured into **six wave acts**.
  Four open rows had their ground changed by candidate-byte repairs
  (P-21(c′), P-22, P-23, P-28); a candidate-byte repair is a drafting
  posture, not a decision. Later the same day the round's fresh-context
  review pass completed — fifteen reviews, every verdict `REVISE` — adding
  P-29…P-33.
- **2026-08-07** — P-28 added; P-21 extended with review RD-4's finding F-17
  (one arm of a pending question installed into candidate front matter while
  open).
- **2026-08-06c** — P-26 closed by owner override (see above); P-27 added
  from reviews RC-11 (`REVISE`) and RC-12 (`EXCEPTIONS`); vocabulary rows
  re-checked against `round-2026-08b/TERM-CLOSURE-REPORT.md`.
- **2026-08-05** — regenerated at the close of the human-clarity refactor
  round. The previous revision (as-of `adddc34`) is superseded: it listed
  P-6/P-7/P-8/P-9/P-11 as open when the round executed them, and routed most
  owning records to the git-excluded `_bootstrap/` tree.

## Superseded packet notes (2026-08-10)

P-12's packet became `KNOWLEDGE-HYGIENE-DECISION.md` and P-33's
`WAVE-A-INSTALL-SHAPE-DECISION.md` (both this directory), superseding the
round-08d packets file for those rows; the round-08d
`OWNER-DECISION-PACKETS.md` remained current for packets 1, 3, 4, 5, 9 and
12, with packet 6 stale and banner-marked (P-22's row and the packets file's
own banner said so).
