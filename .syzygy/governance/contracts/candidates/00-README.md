# Final pre-specification workspace — rev10 (compaction + Mission Control + Context Compiler)

> **Historical packet readme, tracked as part of the candidate package —
> nothing here is accepted, and every digest below is the value that was
> current when this report was written (2026-08-02).** All four act
> arguments were re-quoted on 2026-08-05; the current values live only in
> `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` §1. Current package
> orientation: `README.md` in this directory.

**Directive:** `_bootstrap/rfc-phase/REV9-FINAL-PRESPEC-DIRECTIVE.md` (owner-supplied,
preserved verbatim, 2026-08-02). Cite its items as "directive §n" — its section
numbers are not owner-decision IDs.

**What this workspace is.** The rev9 package (nine RFCs at confirmed digests,
gate open, not accepted) is reworked here into the final pre-specification
package: an acceptance-semantic repair, a three-tier compaction of the active
contract corpus, an RFC 0009 contract package split, two new compact RFCs
(0010 Mission Control, 0011 Context Compiler), machine-readable contract
metadata, portable validation, and a rebuilt compact acceptance record — then
fresh-context reviews and one final owner gate
(`ACCEPT COMPACTED FOUNDATIONAL RFCS: <package-manifest-digest>`, **not
executed by the agent**).

The rev9 corpus at `_bootstrap/rfc-phase/rfcs/` is **frozen as historical
input** from this point: nothing there is edited. The rev9 acceptance
*phrase* (`ACCEPT FOUNDATIONAL RFCS`) is retired unconditionally at rev10
delivery (retirement notice in the rev9 record itself — transaction-review
E4); which *corpus* binds is decided only by the owner's act on the rev10
gate. The rev9 corpus is no longer offered for acceptance.

---

## Preflight report (directive §0) — 2026-08-02

> **Historical snapshot.** Every figure in this section describes the
> **rev9** corpus as found at preflight (RFC-0009 at 19,269 words, etc.).
> The package this README fronts has different, smaller numbers — current
> figures live in `06-CONTEXT-LOAD-MAP.md` and the acceptance record §3.

**Repository state vs rev9 packet:** [Observed] identical. All nine RFC
sha256 digests match `CURRENT-RFC-DIGESTS.md` and acceptance-record §3
(RFC1 `34f930c5…` … RFC9 `ceabc3e3…`); topology manifest digest `0d34d1b5…`,
overview `42de2eb1…`, craft CC-TEST-2 `aa2d6353…` unchanged. Working tree
clean except the rev9 zip and the directive file (both untracked by design).
HEAD `0d79d48`. No reconciliation needed.

**Adopted doctrine:** VIS-1…7 / SEC-1…5 at `.syzygy/governance/doctrine/`
(adopted 2026-07-30, commit `9bdfe98`, tag `doctrine-adopted-2026-07-30`);
amendment D1 (map historical scope) applied at `84d4a88`. 7,774 words.

**Craft-and-care:** canonical home `.syzygy/governance/policies/craft-and-care/`
(owner-approved D2, committed `fcb05c0`), 9,000 words. Amendment **CC-TEST-2**
applied in content but still gated on act 2
(`CONFIRM CRAFT AMENDMENT: CC-TEST-2@aa2d6353…`) — approved cluster,
one gated amendment.

**RFCs:** 0001–0009 all **unaccepted** (effective status: proposed drafts;
gate open since rev8 convergence). Word counts [Observed, `wc -w`]:

| RFC | words | | RFC | words |
|---|---|---|---|---|
| 0001 graph/identity/planes | 9,534 | | 0006 selection/query/drawer | 5,017 |
| 0002 observation/evaluation | 9,323 | | 0007 Polaris | 9,843 |
| 0003 manifests/governance | 10,193 | | 0008 Trajectory | 9,791 |
| 0004 sources/evidence | 9,621 | | 0009 Orrery | **19,269** |
| 0005 auth/consent/profiles | 7,819 | | **total** | **90,410** |

294 numbered clauses, 2,360 resolved citations, 57 §8 questions (36 answered,
21 open).

**Separately gated artifacts:** topology bundle (act 3, 6,737 words, nine
files + manifest) and project overview (act 4, 1,290 words) — both reviewed
drafts, unaccepted. Total active-contract reading path today:
~90,410 (RFCs) + 7,774 (doctrine) + 9,000 (craft) + 6,737 (topology)
+ 1,290 (overview) + ~5,600 (acceptance record + routing matrix)
≈ **121,000 words**, with no selective-loading mechanism.

**Historical (not current authority):** `READINESS-REPORT.md`,
`ACCEPTANCE-PACKET-ITEMS.md`, `OWNER-ANSWERS.md`, reviews 1–10 (including the
10-rev8 trio), both prior rework directives, `RFC-0009-SPLIT-ASSESSMENT.md`
(its recommendation is **reversed** by directive §4). Current authority for
acceptance state: `FOUNDATIONAL-RFC-ACCEPTANCE-RECORD.md` — to be superseded
by `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` in this workspace.

**Validation tooling:** `scripts/verify_rfcs.py` + `verify_rev7.sh` exist at
`_bootstrap/rfc-phase/scripts/` but carry machine-local absolute-path
assumptions and live in git-excluded state — directive §11 requires portable
rewrites into this package.

---

## Deliverables map (directive §12)

| File | Directive item |
|---|---|
| `01-REV9-ADVERSARIAL-FINDINGS.md` | §0/§2 findings against rev9 |
| `02-OWNER-DIRECTION-RECORD.md` | §1, §4 settled direction |
| `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md` | §3 |
| `04-CLAUSE-MIGRATION-MATRIX.md` | §3 semantic preservation, all 294 clauses |
| `05-CONTRACT-INDEX.yaml` | §5 |
| `06-CONTEXT-LOAD-MAP.md` | §5/§7 reader map + load tests |
| `07-AUTONOMY-EXTENSION-REGISTER.md` | §8 |
| `08-OPEN-QUESTION-TRIAGE.md` | §9 |
| `09-OPEN-SPEC-READINESS-REPORT.md` | §10/§14 |
| `rfcs/` (compacted 0001–0008, `RFC-0009/` package, 0010, 0011) | §3/§4/§6/§7 |
| `history/` per-RFC rationale + links to rev9 review corpus | §3 Tier 2 |
| `fixtures/` semantic-equivalence + context-selection | §3/§7 |
| `scripts/` portable validation | §11 |
| `reviews/` fresh-context reviews | §13 |
| `FINAL-FOUNDATIONAL-CONTRACT-ACCEPTANCE-RECORD.md` | §12 |
| `10-EXIT-REPORT.md` | §14 exit questions + return items |
