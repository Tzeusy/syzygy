# Round dispositions — human-clarity refactor round, 2026-08-05

**Synthesized by the round lead after all eight raw reports were stored
verbatim in `reviews/`. The raw reports are the source of truth**; this file
routes, classifies, and disposes. It re-labels no verdict and restates no
finding in softer words.

## 1. Verdicts (copied exactly from each report's verdict line)

| Review | Raw file | Verdict |
|---|---|---|
| RB-1 Fresh engineer / public-clone reader | `RB-1-fresh-engineer-RAW.md` | **EXCEPTIONS** |
| RB-2 Vision and doctrine | `RB-2-vision-doctrine-RAW.md` | **EXCEPTIONS** |
| RB-3 Knowledge architecture and anti-rot | `RB-3-anti-rot-RAW.md` | **REVISE** |
| RB-4 Foundational contract and compaction | `RB-4-contract-compaction-RAW.md` | **EXCEPTIONS** |
| RB-5 Agent context and Context Compiler | `RB-5-context-compiler-RAW.md` | **EXCEPTIONS** |
| RB-6 Mission Control and autonomy | `RB-6-mission-autonomy-RAW.md` | **EXCEPTIONS** |
| RB-7 Evidence and security | `RB-7-evidence-security-RAW.md` | **EXCEPTIONS** |
| RB-8 Public clone and validation | `RB-8-public-clone-RAW.md` | **EXCEPTIONS** (scorecard 8.5/10) |

Seven EXCEPTIONS, one REVISE, zero ACCEPT, zero REJECT. **RB-3's REVISE is
the round's governing verdict**: under the review contract every REVISE
finding is fixed or explicitly overruled by the owner with rationale. Its
blocking finding is fixed (§3 D-1); its remaining findings are fixed or
listed for the owner in §4–§5.

Transport note: RB-3, RB-4 and RB-5 hit a session limit after writing their
reports and never transmitted a summary message. Their verdicts and findings
here are read from the stored files, which are complete. No reviewer's text
was edited.

## 2. Independent convergences (separate reviewers, no shared context)

| Defect | Independently found by |
|---|---|
| **All four digest-bound act arguments in the acceptance record are stale** — the act phrases as written accept nothing | RB-1 F1, RB-2 F1, RB-3 F1, RB-4 F1, RB-7 F1, RB-8 F1 — **six of eight** |
| `PROJECT-STATUS.md` claims "Known blocking defects: none" while its own named verification command exits FAIL | RB-1 F1, RB-2 F1, RB-7 F5, RB-8 F3 |
| The pending-decision register is stale: executed items listed open, owning records pointed at unreadable `_bootstrap/` paths | RB-1 F3, RB-3 F6, RB-8 F4 |
| Act 5 routed to the superseded D3 draft, not the rev1 packet | RB-1 F4, RB-2 F6 |
| The semantic-delta register's completeness claim was not met | RB-2 F7, RB-3 F2, RB-4 F4 |

The first row is the finding the round exists to have caught: the corrections
this round made to three digest sets were recorded everywhere *except* the
document that offers the acts.

## 3. Fixed this round (D-1: lead-authorized, no ceremony)

| # | Fix | Sources |
|---|---|---|
| 1 | **Acceptance record §1 re-quotes all four act arguments** at their current values, and a new §1a states what changed, why, and how to verify mechanically before acting | six reviews |
| 2 | **`check_governance.py` gained CG-7c**, covering acts 2/3/4 — until now one act was checked and three were invisible, a truthful "1 examined" over a population of 4 | RB-3 F1 |
| 3 | `PROJECT-STATUS.md`'s blocking-defects section now states the gate arithmetic honestly instead of "none known" | four reviews |
| 4 | **`PENDING-OWNER-DECISIONS.md` regenerated** from owning records: executed items moved to a resolved section, every pointer repointed to a tracked home, four new items (P-17…P-20) opened for what this round surfaced and did not resolve | three reviews |
| 5 | Act 5 repointed to `DOCTRINE-AMENDMENT-BOUNDED-MISSION-D3.md` (rev1) in `AGENTS.md` and `PROJECT-STATUS.md`, with the reason the original draft cannot be applied as written | RB-1 F4, RB-2 F6 |
| 6 | Semantic-delta register completed: **SD-8** (D3 rev1), **SD-9** (overview refactor), **SD-10** (this post-review batch), with the completeness gap itself recorded rather than erased | RB-2 F7, RB-3 F2, RB-4 F4 |
| 7 | Overview: the VIS-4 sentence no longer asserts D3 as *the* licensing mechanism or pre-settles the D4 question; the north star and fleet-observability mandate are now stated, not only disclaimed | RB-2 F2 (blocking for act 4), RB-2 F8 |
| 8 | `SECURITY.md`: executable-content disclosure completed (CI workflow, `.claude/settings.json`, and the two index builders that **write**), SEC-2/SEC-3/SEC-5 rows realigned to doctrine wording (restored "inferred layer", "remote backing dependencies", "destructive-operation gates") | RB-2 F4, RB-7 F3, RB-7 F4 |
| 9 | `README.md` now says what Syzygy is as an artifact (local-first daemon + browser app, none of it built) and carries the craft binding-onset caveat | RB-1 (Test A gap), RB-3 F15 |
| 10 | `AGENTS.md` no longer declares two owners for the digest fact in one sentence | RB-3 F1 |
| 11 | `PROCESS-LESSONS.md` no longer asserts that the candidate six-plane model supersedes adopted doctrine's three-state thesis, and no longer revives a "four-state phrasing" that scores zero in the corpus | RB-3 F3 |
| 12 | Term registry: "sixteen of thirty terms outside the frozen list" corrected to **eighteen**, with the mapping shown | RB-3 F5 |
| 13 | `06-CONTEXT-LOAD-MAP.md` gained a derived-never-authority banner and now names its relationship to candidate `CC-BUDGET-1` | RB-3 F4, RB-3 F7 |
| 14 | Fixtures 6–8 and the fixture report no longer declare `governance_sources` empty — the generator was repointed at the canonical homes and the index regenerated (26 sources, no drift) | RB-5 F2 |
| 15 | Topology `README.md` title and banner say **candidate**, not draft/proposed, inside the act-3 bundle; bundle manifest regenerated | RB-8 F5 |
| 16 | `rfcs/RFC-0010` and `RFC-0011` §6 headings no longer promise history files that do not exist | RB-4 F10 |
| 17 | Fixture 1's packet digest refreshed after the word-neutral RFC-0007 edit; fixtures 2/4/5 refreshed earlier in the round; each carries a re-measure note | RB-5 F1 (fixture 8 remains — see §4) |
| 18 | `ARTIFACT-INVENTORY.md` count corrected and marked a shape record, not a live total | RB-3 F10 |

| 19 | The owner round charter moved out of the repository root into these round records, byte-unchanged (SD-11) — a public clone's second-most prominent file was a working prompt for one round | RB-1 |
| 20 | `check_governance.py` gained **CG-7d**, which checks every act digest quoted *anywhere*, not only in the acceptance record; it found a fifth stale copy on its first run (craft `INSTALL-RECORD.md:51`) that no reviewer reported, now marked historical (SD-12) | lead, from the §2 row-1 convergence |
| 21 | `check_governance.py` no longer aborts outside a git checkout: it degrades to a filesystem walk, runs all checks, and reports CG-11 as Unknown rather than passed (SD-12) | Test D re-run at final bytes |

All four manifests were regenerated **by script** after this batch. The
resulting act arguments are the ones in the acceptance record §1 and in
`FINAL-OWNER-ACCEPTANCE-RECORD.md`.

## 4. Knowingly carried, with reasons (owner may overrule)

| # | Item | Why carried |
|---|---|---|
| A | **Fixture 8's stated packet digest still does not reproduce** (RB-5 F1, blocking in its vertical) | Its cause is the same word-neutral RFC-0007 edit that staled fixtures 1/2/4/5. Fixtures 1/2/4/5 were refreshed; fixture 8 is a *draft* fixture outside the accepted set and outside every act's digest, and refreshing it after the manifest freeze would re-open the freeze. Recorded here and in P-20; refresh belongs with the next fixture pass |
| B | **RFC-0006 has no clause-level routing classification at all** (RB-4 F2) | The earlier register described an existing-but-unreviewed matrix; the artifact does not exist. Creating 28 classifications now would be new normative work after the review battery closed. Restated as P-10 with RB-4 §4.2's first-pass offered to the owner |
| C | **The craft cluster's engineering bar is adopted by reference to a machine-local skill tree** (RB-1 F5) | A gate-2-approved authority is unreadable from a clone. Fixing it means either importing external text into the craft cluster or amending an owner-approved policy — both owner acts, neither a lead's call. P-20 |
| D | **Adopted doctrine cites a "README glossary" that does not exist** (RB-1 F6) | The citation sites are inside adopted doctrine (`vision.md`, `v1.md`); repairing them is a doctrine amendment, not a round fix. P-20 |
| E | **The eight fixtures do not cover the charter §15 fixture list** (RB-5 F5) | Charter §15 names eight classes; the set covers a different eight. New fixtures are new work; recorded for the next context pass. P-20 |
| F | **Measurement figures live inside digest-bound modules** (RB-4 F11) and **RFC-0007's "twelve edges" enumeration is itself non-exhaustive** (RB-4 F7) | Each further `rfcs/` edit re-opens the manifest and forces another confirming cycle. The figures are correct as of the freeze; the structural point (recomputable numbers should not sit inside digest-bound text) is an amendment candidate. P-20 |
| G | **20 asymmetric `depends_on`/`provides_to` edges**, and `depends_on` under-declares against modules' own citations (RB-4 F15) | Repairing means editing metadata inside the act-1 digest set on the lead's judgment. Disclosed in `CONTRACT-DEPENDENCY-INDEX.md`, which reports rather than repairs |
| H | **Mission-envelope residuals** — no rollback/compensation clauses, the RFC10-11 budget-overrun seam (live for *spend*, not merely effects), no completion adjudicator (RB-6 F1/F2/F4) | All are amendment candidates against a digest-frozen contract; none blocks act 1. Opened as P-19 |
| I | **D3 rev1's own change table is incomplete** (RB-6 F3) | All unlisted deltas are meaning-preserving or stricter and none licenses anything; the packet is the owner's to adopt, amend, or decline, and rewriting it again mid-round would restart its review |
| J | **Doctrine/contract vocabulary seams** — governance-category count (four "minimums" vs five "closed" + reserved sixth), "Claim" absent from doctrine's frozen nouns, `evidence tier` vs `rendering tier` | Each is compatible on a plain reading; each wants an owner ruling before OpenSpec multiplies it. Opened as P-18 |
| K | **Eight of thirty foundational public terms have no adopted definition anywhere** | Closed by acts 1 and 5; using them on the public surface before then is a knowing deferral. Opened as P-17 |
| L | Minor accounting residuals: RB-4 F3/F5/F8/F9/F12/F13/F14, RB-5 F3/F4/F6/F7/F9/F10/F11/F12/F13, RB-3 F8/F9/F11/F12/F13/F14, RB-1 F7/F8/F9/F10/F11, RB-2 F3/F5/F9/F10, RB-7 F2 | Each is recorded in its raw report with file:line evidence. None changes an obligation; none blocks an act. Left for the next pass rather than batched unreviewed into a frozen package |

**The honest summary of §4:** this round fixed what it could verify and
froze the rest rather than editing digest-bound material after its review.
Every carried item has a raw-report citation; none is a silent omission.

## 5. What no reviewer covered

- **RB-9, the final exact-manifest review, is the one vertical the round
  could not run to completion** — three reviewer sessions hit the account's
  session limit during the battery, and the manifest froze after them. The
  acceptance record therefore carries **no digest-binding confirming review
  over the current digests**. This is stated in `FINAL-OWNER-ACCEPTANCE-
  RECORD.md` as the round's principal residual: the owner should commission
  one fresh-context digest-binding review before act 1, or accept knowingly.
- No fresh-reader review (VIS-3) has been run on the 30 term-registry
  entries individually.
- The corpus was never swept for terms used normatively that are absent from
  the registry — the larger, unrun half of a lexical audit.

## 6. Standing limits of this synthesis

Written by the lead, who held the round's authoring context. Where a raw
report and this file disagree, **the raw report wins**. Verdict words are
copied, never re-labeled. Counts in §3 are of fixes applied, each traceable
to the finding cited beside it.
