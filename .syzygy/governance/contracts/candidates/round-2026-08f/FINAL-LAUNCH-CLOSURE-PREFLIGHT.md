# Final launch-closure preflight — round 2026-08f

> **Historical snapshot — non-authoritative round record.** Written before
> any change of this pass. Every figure was measured this session at the
> stated HEAD, by the stated method. Where a later artifact and this file
> disagree, the later artifact wins and this file is a snapshot. Nothing
> here is an owner act, an offer, or authority.

- **Session date:** 2026-08-11
- **Charter:** `syzygy_fable_structured_launch_gate_capability1_prompt.md`
  (repo root, untracked — the owner's working copy, never committed). It
  **supersedes** `syzygy_fable_launch_gate_capability1_closure_prompt.md`,
  which the owner removed from the working tree before this session began.
  [Observed]
- **Parallel-lead check:** clean. `git status --porcelain` names exactly one
  path — the untracked charter — so no other session has uncommitted work in
  this tree; every file with a today-mtime is this track's own last commit
  (`4aa221b`) or the charter itself. [Observed]

---

## 1. Repository state

| Fact | Value | Method |
|---|---|---|
| Branch | `main`, `## main...origin/main` with no ahead/behind marker | `git status -sb` [Observed] |
| HEAD | `4aa221b` — *launch gate v1.18: measure the set, not just the rule (RD-45 closed)* | `git log --oneline -1` [Observed] |
| Working tree | clean but for the untracked charter | `git status --porcelain` → 1 line [Observed] |
| Remote | `git@github.com:Tzeusy/syzygy.git` | `git remote -v` [Observed] |

The charter's own snapshot named `4aa221b`. The repository has **not**
advanced past it; the charter's §1 escape ("if the repository has advanced")
does not fire. [Observed]

---

## 2. Wave A / Wave B — digests and review verdicts

| Wave | Current argument | Latest exact-package review | Verdict | Offer state |
|---|---|---|---|---|
| A | `8972d963…` (regenerated after the RD-31 repair batch) | **RD-31b**, at `1a23d19` | `VERDICT: CONFIRM` | **withheld solely by P-33** (acceptance record §7 item 11) |
| B | `193e3c1e…` (regenerated after the RD-32b repair batch) | **RD-32c**, at `18afdd4` | `VERDICT: CONFIRM` | nothing withholds it; it **follows Wave A** on the A → B path |

Both verdict words are quoted from
`round-2026-08e/reviews/DELIVERY-AND-VERDICT-REGISTER.md` rows RD-31b and
RD-32c, unchanged. [Observed]

Carried, knowingly deferred findings against confirmed bytes (each would
retire its confirmation if repaired now): RD-31b **N-1** (Wave A, RFC3-2
¶1/¶2 characterization lag — `bd` issue `syzygy-4si`) and RD-32c **N-1c**
(Wave B, RFC7-37 aside precision — `bd` issue `syzygy-cgm`). [Observed]

**No acceptance act has been performed.**
`.syzygy/governance/decisions/ACCEPTANCE-ACT-RECORD.md` does not exist, and
its absence is correct. [Observed]

---

## 3. P-33 — the one obstacle to offering confirmed Wave A

- **State:** open, unruled. Queued 2026-08-09 from review RD-18's blocking
  finding B2 and major M5. [Observed]
- **Current packet:**
  `.syzygy/governance/decisions/WAVE-A-INSTALL-SHAPE-DECISION.md`.
- **Question 1** (the `contracts/` containment breach): four drafted arms
  (1a) companions outside `governance/`; (1b) widen RFC3-15's `contracts/`
  cell; (1c) drop the companion copies; (1d) mint a new
  `contracts-companion/` category inside `governance/`. Current recorded
  recommendation: **(1d)**, `[Inferred]`. [Observed]
- **Question 2:** the 39-row `ACTIVE-CONTRACT-MANIFEST.txt` installed at the
  first wave act while that act accepts only its own wave's modules.
  [Observed]
- **This pass's charter (§7) rejects the framing** of the current
  recommendation: it directs a packet organised by **semantic class of
  content**, not by the material's present physical proximity to the
  contracts. The revised packet is a deliverable of this round; the ruling
  remains the owner's. [Observed — charter §7]

---

## 4. Launch gate — current version and review state

| Fact | Value |
|---|---|
| Instrument | `launch-gate-pre-specifications.md`, `effective_version: v1.18` (candidate) |
| Instrument sha256 | `616364a579115d7ab948e5c3799a95eae21262ccfe1eebedf29b9cc136ae6561` |
| Validator | `scripts/launch_gate_results.py`, sha256 `278ee1ea14fb3c87f69668ac77410f24a890a725f9285a35b53e432030aafe7a` |
| Validator fixtures | **329 fixtures, 0 failing** (`--selftest`, run in-repo this session) |
| Latest raw review | **RD-45**, on instrument **v1.17** at `963f1c4` |
| RD-45 verdict | `VERDICT: REVISE` — 4 BLOCKING, 4 MAJOR, 1 MINOR |
| v1.18 status | repairs closing all nine RD-45 findings, committed `4aa221b`; **no review is bound to v1.18** |
| Review in flight | **none.** RD-46 was composed but never dispatched. [Observed — no `RD-46` dispatch row exists in the delivery register; `bd` and the register agree] |
| Administration record | one, the 2026-08-09 **pilot** at v1.3, `GATE VERDICT: NOT READY`, immutable under `round-2026-08d/reviews/` |
| Formal administration | **none has occurred** |

Review chain to date: RD-33 … RD-45, thirteen administrations of the
instrument, **every one `REVISE`**. RD-41 through RD-45 each returned
`REVISE` on the same underlying class — whether a line of a Markdown record
is the record's own claim or a quotation of one. [Observed]

**The charter (§2.7–2.8, §5) stops that loop.** RD-46 is not to be
dispatched: no further review whose main purpose is finding one more
Markdown, HTML, list, fence, table, or rendering carrier. The representation
of an administration result changes instead. [Observed — charter §2, §5]

---

## 5. Default reading path

`DEFAULT_ROUTE_SET` (instrument §8), with current sizes:

| Path | Lines |
|---|---|
| `README.md` | 141 |
| `AGENTS.md` | 224 |
| `.syzygy/intent/OVERVIEW.md` | — (governed presentation) |
| `PROJECT-STATUS.md` | **398** |
| `.syzygy/governance/doctrine/README.md` | — |
| `.syzygy/governance/contracts/candidates/TASK-ROUTER.md` | — (generated) |

Adjacent owner-facing documents: `PENDING-OWNER-DECISIONS.md` 207 lines;
`LAUNCH-GATE-AUTHORITY-DECISION.md` (P-34 packet) **409 lines**;
`PROCESS-LESSONS.md` 463 lines. [Observed — `wc -l`]

The two the charter names for reduction (§6.1, §6.2) are the two longest:
`PROJECT-STATUS.md` at 398 lines and the P-34 packet at 409.

---

## 6. Owner-decision queue

`.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`, 207 lines.
**Open rows: P-1 … P-5, P-10, P-12, P-14 … P-25, P-27 … P-41.** Executed
and closed: P-6, P-7, P-8, P-9, P-11, P-13, P-26. [Observed — row scan]

Launch-critical subset this pass must prepare (charter §16), in the
charter's own dependency order:

```text
P-33  Wave A install shape          — the only obstacle to offering Wave A
P-31  merged-but-unreconciled Unknown
P-36  Unknown versus Gap
P-37  launch-scope facets and authority home
P-38  human entry and discoverability
P-39  OpenSpec form/version
P-40  specification granularity
P-35  operating constraints
P-34  launch-gate v2.0 process policy
P-41  specification-acceptance craft amendment
      shape-to-spec impact craft amendment (no P-n yet)
P-1   Wave A act, then Wave B act
      owner launch decision (no P-n — it is the gate's own act)
```

This pass uses that queue. It mints no competing queue. [Charter §2.13]

---

## 7. Specification prerequisites

`openspec/` **does not exist**; no specification has been authored; no
implementation tree, toolchain manifest, or product backlog exists.
[Observed — `ls`; the prohibition is `AGENTS.md`'s and the charter's]

The readiness standard is the charter's §17 conjunction (Wave A offerable
and accepted; Wave B accepted after A; P-31/P-36/P-37/P-38/P-39/P-40 ruled;
specification-acceptance policy in force; shape-to-spec propagation rule in
force with a passing fixture; operating constraints recorded; launch-gate
v2.0 owner-approved; the formal structured-data administration returns
READY; the owner separately authorises launch; F4 default-path hygiene
passes; F3 owner-packet comprehension passes). **Not one of the owner-act
conjuncts is satisfied today.**

---

## 8. Hosted CI visibility

**Observable, and green at exactly this commit** — the charter's `Unknown`
fallback does not fire:

```text
workflow    governance-docs
run         31433784576
head_sha    4aa221b1ff17f777293b8f7b90ff7a0e9f712c56
conclusion  success
createdAt   2026-08-10T21:25:33Z
```

[Observed — `gh run list --json databaseId,headSha,conclusion,workflowName,createdAt`]

**Its denominator, stated rather than implied.** The hosted workflow runs
**four** checks: `check_governance.py`, `verify_final_prespec.py`,
`build_contract_index.py --check`, `build_dependency_index.py --check`. It
does **not** run `build_budget_report.py --check`, nor either `--selftest`
suite. A green hosted run is therefore evidence about four checks, never
about the battery. The remaining checks are evidenced only by the local
clone run in §9. [Observed — `.github/workflows/governance-docs.yml`]

---

## 9. Clean-clone evidence

Fresh clone of this repository at `4aa221b` (scratchpad
`clone-08f-r1`), `git status --porcelain` → 0 lines, charter absent:

```text
check_governance.py          30 OK, 18 WARN, 0 FAIL (48 checks)
verify_final_prespec.py      PASS — all checks clean
launch_gate_results.py       329 fixtures, 0 failing
check_governance.py --selftest  121 fixtures, 0 failing
```

[Observed — run in the clone this session]

In-repository, the same battery plus the three drift checks:
`build_contract_index.py --check` no drift (11 contracts, 39 modules, 367
clauses); `build_dependency_index.py --check` no drift (176 `depends_on`, 8
`constrains`); `build_budget_report.py --check` fixture anchors and report
match regeneration. [Observed]

**The battery has no FAIL at this HEAD.** The single expected FAIL of the
previous pass was caused by the retired-phrase quotations inside the *old*
charter file; that file is gone and the new charter trips no check. This is
a change of state worth naming, because a report written from the previous
pass's habit would have described a FAIL that no longer exists.

`verify_final_prespec.py` prints one standing note, not a failure: total
context `119253` exceeds the 35–50k target band, "owner-facing justification
required (charter)". [Observed]

---

## 10. What this preflight establishes for the pass

1. The charter's snapshot is exact; nothing has advanced; no verdict needs
   re-reading. [Observed]
2. Waves A and B are both **confirmed** and neither is **offered** — Wave A
   for P-33, Wave B for order. [Observed]
3. The launch gate is at v1.18 with **no review bound to it**, and the loop
   that produced thirteen consecutive `REVISE` verdicts is closed by owner
   direction rather than by another repair. [Observed — charter §2.7]
4. Hosted CI is observable and green over four of the battery's checks; the
   rest are clone-evidenced. [Observed]
5. Every launch-critical owner decision is open. The pass prepares them; it
   rules none. [Observed]
