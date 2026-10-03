# RD-6's fourteen open source-of-truth findings, routed — as of 2026-10-03

> **Technical record, no act.** It grants, adopts and waives nothing, and
> performs or infers no owner decision. Bead `syzygy-0wf`, under the owner
> direction `.syzygy/governance/decisions/OWNER-DIRECTION-2026-10-03-OVERNIGHT-BEADS-LOOP.md`.
> The raw review is
> `.syzygy/governance/contracts/candidates/round-2026-08c/reviews/RD-6-source-of-truth-RAW.md`
> (verdict `REVISE`, line 6) and wins over this page about what the reviewer
> found. Every re-derivation below was run on 2026-10-03 against `main` at
> `a6c2d566`.

## The population

The round's closure report,
`.syzygy/governance/contracts/candidates/round-2026-08c/SOURCE-OF-TRUTH-CLOSURE-REPORT.md`,
counts 19 findings, 5 closed (H-1, A-2, C-3, E-1, G-2) and 14 open. The 19
are the raw's distinct identifiers with two pairs merged, because the raw
names each pair as one defect: E-3 is C-1 (raw line 484, "See **C-1**"), and
D-3 is E-2's first residual (raw line 674, "See **E-2**").

The fourteen, therefore: A-1 (its open half), A-3, C-2, D-1, D-2, D-3/E-2,
D-4, E-3/C-1, E-4, F-1, F-2, F-3, F-4 and G-1. [Observed] The closure
report's own table never names D-1, though its count of fourteen includes
it.

## Outcome in one paragraph

[Observed, 2026-10-03] **Five are resolved on `main`** (A-1, E-4, F-2, D-1,
and G-1's ruled half), **one is partly resolved** (C-2, six of eleven files),
**F-3 is resolved in two of eleven rows and not reproduced in a third**, and
**everything still open has a home**: four self-drivable bead proposals
(B1–B4), two owner waits already registered (P-12 and P-21), and one owner
wait with no register row (B5, G-1's citation leg). The quotation check the
bead asked for is `scripts/check_quotations.py`, in the battery, with its
rule-6 record beside this page. Its first run found one quotation its source
never contained, recorded below.

## Routing

| ID | Re-derived 2026-10-03 | Home |
|---|---|---|
| **A-1** | **Resolved** by `771965c7` (2026-08-09). RFC11-4 now enumerates `depends_on` and `constrains` and no longer names `provides_to` (`.syzygy/governance/contracts/candidates/rfcs/RFC-0011/deterministic-selection-and-budget.md:64-66`); `provides_to` occurs nowhere under either `rfcs/` tree. | The remaining question, whether `constrains` is the right relation, is **owner row P-21** in `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`. **Waits**; nothing to add. |
| **F-1** | **Open.** `scripts/check_governance.py` still attributes `DEFAULT_LOAD` to "charter §7.3", the 900–1,200 authored-word band to "§7.1", CG-22 to "§9.4" and CG-23 to "§9.3". Of the four tracked `*CHARTER*` files, `COMPACTION-CHARTER.md` has no numbered heading and `round-2026-08/OWNER-ROUND-CHARTER.md` has §7, §9 and §11.4 but no 7.1, 7.3, 9.3 or 9.4. `TOKENS_PER_WORD` cites nothing. §11.4, cited for `BUDGETS` and the module triggers, does resolve. | Split. **(a) The four dead citations: bead B1** — say in CG-8, CG-22, CG-23 and `CHECK_OWNERS` that these are the checker's own operating figures, which is the raw's option (b), lines 247–251. **(b) Where the budget figures bind: owner wait, P-12** (`.syzygy/governance/decisions/KNOWLEDGE-HYGIENE-DECISION.md`, the round's packet 7), because `BUDGETS`, `MODULE_TRIGGER` and `MODULE_DECOMPOSE` transcribe the uninstalled `CC-BUDGET-1`. |
| **F-2** | **Resolved** by `31ebc527` (2026-08-10). `JUSTIFIED_OVERSIZE` in `candidates/scripts/verify_final_prespec.py` no longer states "23%" or says the justification is carried in the 03 report; it cites that report only for the floor, which the report states (`03-ACTIVE-CONTRACT-COMPACTION-REPORT.md:123`: "accepted as the honest floor of a dictionary contract"). | Closed. Its class, a quotation its source does not contain, now has a check: `scripts/check_quotations.py`. |
| **F-3** | Eleven rows. **Resolved:** row 8, by `31ebc527` (act subjects are derived from `ACCEPTANCE-PHRASE-REGISTRY.yaml`). **Not reproduced:** row 4 — `04-CLAUSE-MIGRATION-MATRIX.md` lines 3–9 state the closed outcome vocabulary, and did at the reviewed commit `aee13d56`. **Open:** rows 1, 2, 5, 6, 7, 9, 10, 11 and row 3 (which is D-4). Row 2 is sharper now: the two phase-rule lists have diverged, `PHASE_RULE_CLAUSES` naming eleven clauses and `build_contract_index.py`'s `PHASE_RULES` six, so `05-CONTRACT-INDEX.yaml` marks RFC1-33, RFC2-26, RFC3-33, RFC4-30 and RFC5-27 `normative` although each is its contract's phase rule. | Rows 1, 7, 11: **B1**. Rows 2, 9, 10: **B2**. Rows 3, 5: **B3**. Row 6: **owner wait, P-12** (a second copy of `CC-BUDGET-1`'s rows). |
| **F-4** | **Open.** CG-9 still prints "duplicate authority homes absent" over the 16 files under `/doctrine/` and `/craft-and-care/`; its `CHECK_OWNERS` entry already concedes "No clause states the one-home rule". | **B1.** Relabel the check; the identifier CG-9 is unchanged, so CC-REV-7 is not engaged. |
| **A-3** | **Open.** The generated `CONTEXT-BUDGET-REPORT.md` prints "The 7,000-word per-module ceiling" and an "Over the 7,000 ceiling" column (lines 146 and 151), from `build_budget_report.py`; the verifier's messages say the same. The authored sources say "~7,000". | **B3.** |
| **D-3 / E-2** | **Open.** `build_budget_report.py` still writes the generating machine's `HEAD` and a dirty-tree clause into the tracked report's as-of line, and `_without_asof()` keeps `--check` from ever verifying it. | **B3.** |
| **E-3 / C-1** | **Open.** `05-CONTRACT-INDEX.yaml` lines 1–2 name the file a generated projection and say nothing about candidacy; `build_contract_index.py:166` still emits `status_source: owner-act-record` as a literal instead of projecting it. | **B2.** |
| **E-4** | **Resolved** by `771965c7` (2026-08-09). `ACTIVE-CONTRACT-MANIFEST.txt` line 3 reads "Generated by scripts/build_active_manifest.py — regenerate with it; never hand-edit.", and `build_active_manifest.py --check` runs in both batteries. The single act 1 was restructured into six wave acts at round-2026-08d (`.syzygy/governance/contracts/candidates/FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md:11`); performed wave manifests are verified against their recorded arguments and never regenerated. | Closed. **No owner act is needed.** This corrects the dispatch brief, which listed E-4 as an owner wait. |
| **C-2** | **Partly resolved.** Six of the eleven now open with a non-authority banner in lines 1–3: `03-…`, `09-…`, `10-EXIT-REPORT.md`, `COMPACTION-CHARTER.md`, `LEAD-SWEEP-NOTES.md`, `WORKER-REPORT-DIGEST.md`. Five do not: `01-REV9-ADVERSARIAL-FINDINGS.md`, `02-OWNER-DIRECTION-RECORD.md`, `05-CONTRACT-INDEX.yaml`, `07-AUTONOMY-EXTENSION-REGISTER.md` and `08-OPEN-QUESTION-TRIAGE.md`. Method: the raw's six literals plus *historical* and *non-authoritative*, case-folded, first 30 lines, every hit read by hand; the literal hits in 01 (line 21) and 07 (line 15) are body text, not banners. | `07` stays as it is: it closes itself at line 28, which the raw accepted (lines 563–564), and `round-2026-08b/reviews/RC-7-mission-safety-RAW.md` cites its current digest. `05`: **B2**. `01`, `02`, `08`: **B4**. |
| **D-1** | **Resolved** by `7a5aa807` (2026-08-09). `_git_excluded_roots()` keeps full excluded prefixes, dotted ones included, and `--selftest` carries a dotted-root case (`.syzygy/cache/`). | Closed. |
| **D-2** | **Open, lower stakes.** The default `clone` scope still unions untracked files, justified by a docstring sentence that is no longer true ("the candidate governance package is exactly that today"); today's run reports `0 untracked-not-ignored`. | **B1.** |
| **D-4** | **Open, and now repairable without an owner.** `REV9_ENDS` still cites a rev9 record under git-excluded `_bootstrap/`, but all nine ends recompute from the tracked frozen corpus in `contracts/candidates/history/rev9-rfcs/` (highest line-start `**RFCn-m` per file: 32, 25, 32, 29, 26, 28, 38, 32, 52 — equal to the constant). | **B3.** |
| **G-1** | **Main conflict resolved by owner act:** P-22 was ratified at the Wave B act of 2026-08-17 (`.syzygy/governance/decisions/DECISION-HISTORY.md:167`), placing the RFC9-8(a) registry in typed governance. **The citation leg is open:** RFC9-8(a) still says "SDR-29 and RFC3-21 put its arrangement at **workspace scope**" (`.syzygy/governance/contracts/rfcs/RFC-0009/semantic-geography.md:187`, and the candidate mirror), and RFC3-21 governs `.syzygy/local/`, not the workspace manifest. | **Owner wait.** The sentence is inside an accepted contract, so correcting it is a contract amendment. **B5** proposes tracking it into the next RFC-0009 successor; no register row is opened here. |

## What the new check found on its first run

On its first run, on 2026-10-03 and before this page existed,
`scripts/check_quotations.py` examined 17 quotations in 9 files and found
one that no revision of its source ever contained. The
P-25(c) packet,
`.syzygy/governance/contracts/candidates/policy-candidates/DOCTRINE-AMENDMENT-ACTUATOR-DEFINITION.md`,
quotes `doctrine/v1.md:53` as ending "three-axis propagation slice". The one
revision of `v1.md` that carried the sentence, `9bdfe98a`, ends it
"three-axis propagation proof-of-concept" [Observed: all four revisions of
the file searched]. The packet was applied within doctrine amendment D5, and
its head banner says the drafting text below it is unchanged, so the
quotation is **recorded in the checker's `RECORDED` table** and printed on
every run rather than repaired. The same run lists five quotations that are
only in earlier revisions of their sources, all doctrine sentences D5
rewrote, and four whose text has moved off its cited line.

## Rule-6 record

`mutants.json`, beside this page, holds every mutant with its `old` and
`new` fragments, the commit it ran at and the checker's sha256. Twelve
predicate mutants each fail `--selftest`. Two input mutants run in a fresh
clone of that commit: a changed word in a live quotation fails the corpus
run, and a changed word in a quoted source moves its quotation into the
amended note without failing, as designed.

## Bead proposals

Sent to the coordinator; none is created by this page.

- **B1.** The checker says where each of its rules lives (F-1(a), F-3 rows
  1, 7 and 11, F-4, D-2).
- **B2.** The contract-index generator projects what it claims (E-3/C-1, F-3
  rows 2, 9 and 10, C-2's `05`).
- **B3.** The budget report and pre-specification verifier keep the
  approximation, drop machine-local state and derive the rev9 baseline
  (A-3, D-3/E-2, D-4, F-3 rows 3 and 5).
- **B4.** Banner-mark `01`, `02` and `08` at the candidates root (C-2).
- **B5.** Owner-gated: carry RFC9-8(a)'s RFC3-21 citation correction into
  the next RFC-0009 successor (G-1).
