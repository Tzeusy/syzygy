# RB-5 — Agent context and Context Compiler — fresh-context review (RAW)

**Reviewer:** fresh-context reviewer, review vertical 5.
**Date of run:** 2026-08-05.
**Constraint honored:** nothing under `_bootstrap/` was read at any point. Where
a subject file cites `_bootstrap/**`, the citation is treated as unavailable
history and is neither verified nor relied on.

**Subjects reviewed.** `.syzygy/governance/contracts/candidates/` —
`rfcs/RFC-0011-context-compiler.md`; all nine files in `fixtures/`;
`06-CONTEXT-LOAD-MAP.md`; `05-CONTRACT-INDEX.yaml` (`governance_sources`
section); `TASK-TO-CONTRACT-INDEX.md`; `scripts/context_load.py`;
`round-2026-08/CONTEXT-COMPILER-FIXTURE-REPORT.md`. Supporting reads:
`scripts/build_contract_index.py`, `scripts/verify_final_prespec.py`, the 32
contract modules' front matter and phase-rule text, the six doctrine files,
the ten craft policies, `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md`,
and `syzygy_fable_human_clarity_refactor_round_prompt.md` (the charter whose
§11.4 / §11.5 / §15 / §21 this review grades against).

**Status of this file.** Reviewer output, stored verbatim. Not authority, not a
disposition. It records what reproduced, what did not, and what the corpus
claims that its own evidence no longer supports.

---

## 0. Provenance — every command run

All commands run from
`/home/tze/GitHub/syzygy/.syzygy/governance/contracts/candidates/` unless a
path says otherwise. `$D` = `/home/tze/GitHub/syzygy/.syzygy/governance/doctrine`,
`$C` = `/home/tze/GitHub/syzygy/.syzygy/governance/policies/craft-and-care`.

### 0.1 Fixture reproduction — measurement

```sh
# fixture 1
python3 scripts/context_load.py rfcs/RFC-0007/README.md \
  rfcs/RFC-0007/narrative-contract.md rfcs/RFC-0002/README.md \
  rfcs/RFC-0002/rendering-vocabularies.md doctrine:vision.md

# fixture 2
python3 scripts/context_load.py rfcs/RFC-0004/README.md \
  rfcs/RFC-0004/general-contract.md rfcs/RFC-0004/named-adapters.md \
  rfcs/RFC-0008/README.md rfcs/RFC-0008/state-vocabulary-and-cost.md \
  rfcs/RFC-0003/README.md rfcs/RFC-0003/governance-homes-and-owner-acts.md \
  doctrine:security.md

# fixture 3
python3 scripts/context_load.py rfcs/RFC-0009/README.md \
  rfcs/RFC-0009/visual-grammar-and-lenses.md rfcs/RFC-0002/README.md \
  rfcs/RFC-0002/rendering-vocabularies.md doctrine:architecture.md

# fixture 4
python3 scripts/context_load.py rfcs/RFC-0005/README.md \
  rfcs/RFC-0005/execution-profiles.md rfcs/RFC-0003/README.md \
  rfcs/RFC-0003/governance-homes-and-owner-acts.md doctrine:security.md \
  craft:security-and-secrets.md

# fixture 5
python3 scripts/context_load.py rfcs/RFC-0010-mission-control-autonomy.md \
  rfcs/RFC-0011-context-compiler.md rfcs/RFC-0003/README.md \
  rfcs/RFC-0003/governance-homes-and-owner-acts.md doctrine:vision.md

# fixture 6
python3 scripts/context_load.py doctrine:vision.md doctrine:v1.md \
  doctrine:architecture.md doctrine:README.md \
  rfcs/RFC-0003/README.md rfcs/RFC-0003/governance-homes-and-owner-acts.md

# fixture 7
python3 scripts/context_load.py rfcs/RFC-0001-project-graph-identity-state-planes.md \
  rfcs/RFC-0002/README.md rfcs/RFC-0002/snapshot-and-evaluation-core.md \
  doctrine:architecture.md craft:engineering-bar.md

# fixture 8
python3 scripts/context_load.py rfcs/RFC-0001-project-graph-identity-state-planes.md \
  rfcs/RFC-0007/README.md rfcs/RFC-0007/narrative-contract.md \
  rfcs/RFC-0007/rendering-and-surface.md doctrine:vision.md \
  craft:testing-and-verification.md
```

### 0.2 Fixture reproduction — packet digests

```sh
cat rfcs/RFC-0007/README.md rfcs/RFC-0007/narrative-contract.md \
    rfcs/RFC-0002/README.md rfcs/RFC-0002/rendering-vocabularies.md \
    $D/vision.md | sha256sum                                   # fixture 1

cat rfcs/RFC-0004/README.md rfcs/RFC-0004/general-contract.md \
    rfcs/RFC-0004/named-adapters.md rfcs/RFC-0008/README.md \
    rfcs/RFC-0008/state-vocabulary-and-cost.md rfcs/RFC-0003/README.md \
    rfcs/RFC-0003/governance-homes-and-owner-acts.md $D/security.md | sha256sum   # 2

cat rfcs/RFC-0009/README.md rfcs/RFC-0009/visual-grammar-and-lenses.md \
    rfcs/RFC-0002/README.md rfcs/RFC-0002/rendering-vocabularies.md \
    $D/architecture.md | sha256sum                              # fixture 3

cat rfcs/RFC-0005/README.md rfcs/RFC-0005/execution-profiles.md \
    rfcs/RFC-0003/README.md rfcs/RFC-0003/governance-homes-and-owner-acts.md \
    $D/security.md $C/security-and-secrets.md | sha256sum        # fixture 4

cat rfcs/RFC-0010-mission-control-autonomy.md rfcs/RFC-0011-context-compiler.md \
    rfcs/RFC-0003/README.md rfcs/RFC-0003/governance-homes-and-owner-acts.md \
    $D/vision.md | sha256sum                                     # fixture 5

cat $D/vision.md $D/v1.md $D/architecture.md $D/README.md \
    rfcs/RFC-0003/README.md rfcs/RFC-0003/governance-homes-and-owner-acts.md \
    | sha256sum                                                  # fixture 6

cat rfcs/RFC-0001-project-graph-identity-state-planes.md rfcs/RFC-0002/README.md \
    rfcs/RFC-0002/snapshot-and-evaluation-core.md $D/architecture.md \
    $C/engineering-bar.md | sha256sum                            # fixture 7

cat rfcs/RFC-0001-project-graph-identity-state-planes.md rfcs/RFC-0007/README.md \
    rfcs/RFC-0007/narrative-contract.md rfcs/RFC-0007/rendering-and-surface.md \
    $D/vision.md $C/testing-and-verification.md | sha256sum       # fixture 8
```

### 0.3 Corpus, index, and validation

```sh
python3 scripts/verify_final_prespec.py
python3 scripts/build_contract_index.py --check
wc -w $D/*.md | tail -1
wc -w $C/*.md
wc -w /home/tze/GitHub/syzygy/.syzygy/map/topology-candidates/*.md | tail -1
wc -w $C/interfaces-and-dependencies.md \
      /home/tze/GitHub/syzygy/.syzygy/map/topology-candidates/06-intent-to-reconciliation-flow.md
wc -w rfcs/RFC-0002/README.md rfcs/RFC-0002/rendering-vocabularies.md \
      rfcs/RFC-0006-cross-surface-selection-query-drawer.md $C/review-and-documentation.md
grep -F 'kind: phase-rule' 05-CONTRACT-INDEX.yaml
grep -F 'RFC7-38' 05-CONTRACT-INDEX.yaml
grep -n -F 'GOV_SOURCES' -A8 scripts/build_contract_index.py
grep -n -F 'fixtures' -A12 scripts/verify_final_prespec.py
ls -la --time-style=+%H:%M:%S rfcs/RFC-0007/ $C/ policy-candidates/
```

Python one-liners (run via `python3 - <<EOF`, transcribed in full in §1.5–§1.8):
`governance_sources` extraction and entry-role counts from
`05-CONTRACT-INDEX.yaml`; front-matter key sweep over all 32 modules
(`task_classes` / `risk_classes` / `terms` / `open_spec_mapping_status` /
`lifecycle`); a 34-item literal clause-citation presence sweep across fixtures
1–8's cited clauses; a phase-rule text sweep (`schedules nothing` /
`specification of record from which` / `phase boundary` / `phase rule`) over all
32 modules; an accessibility-term sweep (`accessib` / `WCAG` / `contrast` /
`colou?r-blind` / `screen reader` / `keyboard`) over RFCs + doctrine + craft; and
a digest-attribution experiment substituting single words in
`rfcs/RFC-0007/README.md` before re-hashing fixture 8's file list.

**Note on method (AGENTS.md hazard).** `grep` on this machine is ugrep. Every
load-bearing sweep in this review was run through Python `re` or `str.count`,
not shell `grep`; the two `grep -F` calls above are literal-only and are
corroborated by the Python sweeps.

### 0.4 Test C

```sh
python3 scripts/context_load.py rfcs/RFC-0008/README.md \
  rfcs/RFC-0008/state-vocabulary-and-cost.md \
  rfcs/RFC-0008/accounting-reconciliation-and-release.md \
  rfcs/RFC-0002/rendering-vocabularies.md doctrine:trust-and-evidence.md \
  craft:performance-and-visual-discipline.md doctrine:security.md

cat rfcs/RFC-0008/README.md rfcs/RFC-0008/state-vocabulary-and-cost.md \
    rfcs/RFC-0008/accounting-reconciliation-and-release.md \
    rfcs/RFC-0002/rendering-vocabularies.md $D/trust-and-evidence.md \
    $C/performance-and-visual-discipline.md $D/security.md | sha256sum
```

Plus two measured decomposition alternatives (§4.4) and the eight
`TASK-TO-CONTRACT-INDEX.md` reader-map row re-measurements (§2.3).

---

## 1. Reproducibility — results

### 1.1 All eight fixtures, measured

Charge minimum was four fixtures including 1, 2, one of 4/5, and one of 6–8. I
re-ran **all eight**, because the marginal cost was seconds and a partial sweep
cannot support a universal claim.

| # | Stated words | Computed | Stated tokens | Computed | Verdict |
|---|---:|---:|---:|---:|---|
| 1 | 13,864 | 13,864 | 18,716 | 18,716 | reproduces |
| 2 | 18,315 | 18,315 | 24,725 | 24,725 | reproduces |
| 3 | 14,134 | 14,134 | 19,080 | 19,080 | reproduces |
| 4 | 10,893 | 10,893 | 14,705 | 14,705 | reproduces |
| 5 | 12,843 | 12,843 | 17,338 | 17,338 | reproduces |
| 6 | 11,537 | 11,537 | 15,574 | 15,574 | reproduces |
| 7 | 15,767 | 15,767 | 21,285 | 21,285 | reproduces |
| 8 | 22,258 | 22,258 | 30,048 | 30,048 | reproduces |

Every per-file row also matched the module figures in `06-CONTEXT-LOAD-MAP.md`
(all 32, cross-checked against `verify_final_prespec.py`'s own module dump).

### 1.2 Packet digests

| # | Stated prefix | Computed (full) | Verdict |
|---|---|---|---|
| 1 | `4544d4b27646e905…` | `4544d4b27646e90595ff624137329ba8d23edc76c1357c344a25067f76c758b6` | reproduces |
| 2 | `a398a06362074451…` | `a398a063620744514bc8fc60286c13d1aaf9426449540c2aeb16a1e351ea11b5` | reproduces |
| 3 | `2e408eaf40278ca7…` | `2e408eaf40278ca737b057dbbfb769ce81c37d177781dad423742427dc40aff1` | reproduces |
| 4 | `a56fb116fa588b9b…` | `a56fb116fa588b9bab7126f0d0f429864fcfef952c05195eb36c592e33679343` | reproduces |
| 5 | `c92c6f8a936b12b0…` | `c92c6f8a936b12b0a07123f42a1be7d1d2afc94d0c5c1850abc49b4e726eb462` | reproduces |
| 6 | `958090be70dd525b…` | `958090be70dd525b5a07f4378ac95fb43c44f40c58fda207a5e94c8beedccdda` | reproduces |
| 7 | `4de5ebff52463686…` | `4de5ebff52463686ae62655efda622904ef151e216b0bb5990bf9ca3e5cb4479` | reproduces |
| 8 | `36be8f90fa12a01d…` | **`14488b9b31892bfedc2b00261b6214abbfa937b6f828a91e5ee9fc8127eefdd3`** | **MISMATCH** |

Seven of eight reproduce byte-exactly under the stated method (`cat <mandatory
files in listed order> | sha256sum`, `doctrine:` → `.syzygy/governance/doctrine/`,
`craft:` → `.syzygy/governance/policies/craft-and-care/`). Fixture 8 does not.
See **F1**.

### 1.3 Secondary figures inside fixtures — all reproduce

| Claim | Location | Computed | Verdict |
|---|---|---:|---|
| suggested RFC-0006 + RFC-0001 clauses "~4,900 w" | fixture 1 | RFC-0006 alone 4,174 | consistent with "~" |
| RFC-0008 README + identity module "+4,607 w" | fixture 5 | 1,922 + 2,686 = **4,608** | off by 1 (rounding of a sum; harmless) |
| split (a) drop `craft:engineering-bar.md` → 14,485 w / 19,554 tok | fixture 7 | 14,485 / 19,554 | exact |
| split (b) drop `RFC-0002/README.md` → 13,949 / 18,831 | fixture 7 | 13,949 / 18,831 | exact |
| "446 tokens under" the 20,000 trigger | fixture 7 | 20,000 − 19,554 = 446 | exact |
| "starts at ~11,300 est. tokens" (RFC-0001 alone) | fixture 7 | 8,353 × 1.35 = 11,276 | exact within "~" |
| suggested RFC-0003 pair 5,334 w | fixture 7 | 4,414 + 920 = 5,334 | exact |
| suggested `craft:interfaces-and-dependencies.md` 1,059 w | fixture 7 | 1,059 | exact |
| suggested RFC-0002 challenge + reconciliation 4,708 w | fixture 7 | 2,231 + 2,477 = 4,708 | exact |
| suggested topology `06-intent-to-reconciliation-flow.md` 909 w | fixture 6 | 909 | exact |
| suggested RFC-0010 3,096 w | fixture 6 | 3,096 | exact |
| split "README alone" 13,948 / 18,829 | fixture 8 | 13,948 / 18,829 | exact |
| split "drop RFC-0001" 13,905 / 18,771 | fixture 8 | 13,905 / 18,771 | exact |
| split "drop narrative" 17,091 / 23,072 | fixture 8 | 17,091 / 23,072 | exact |
| suggested RFC-0002 pair 4,215 w | fixture 8 | 1,818 + 2,397 = 4,215 | exact |
| suggested RFC-0006 4,174 w | fixture 8 | 4,174 | exact |
| suggested `craft:review-and-documentation.md` 1,068 w | fixture 8 | 1,068 | exact |

This is a genuinely strong record. Every measured decomposition option the
fixtures offer the owner is real and re-runnable.

### 1.4 Corpus baseline

Report §1 states **123,180 words** = 99,080 RFC + 7,783 doctrine + **9,405**
craft + 6,912 topology.

Measured: RFC 99,080 ✅ (matches `verify_final_prespec.py`), doctrine 7,783 ✅,
topology-candidates 6,912 ✅, **craft 9,415** — ten words higher. Corrected
total **123,190 w ≈ 166,306 est. tokens**. `INSTALL-RECORD.md`'s mtime
(04:31:10) is later than the other nine craft files (04:08:54), so the ten
words most likely landed there after the report's sweep. See **F9**. The
derived percentages survive: median fixture 18,898 est. tokens = **11.36%** of
166,306, so "11.4%" holds.

### 1.5 Repository validation, re-run

```
$ python3 scripts/verify_final_prespec.py
… numbered clauses defined: 322
note: RFC-0001 8353 words over the 7,000 ceiling — JUSTIFIED …
note: total 99080 exceeds the 35–50k target band plus new RFCs …
PASS — all checks clean

$ python3 scripts/build_contract_index.py --check
index matches regeneration — no drift
```

Both reproduce the report §7 transcript. **But read the output, not the exit
code:** the verifier's fixture block (`verify_final_prespec.py:237–246`) is a
*substring-presence* check — it globs `fixtures/context-selection-*.md`,
requires ≥5 files, and requires each to contain the strings `Required context`,
`Omitted`, `estimate`, `constraint`, `Suggested`, `digest`. It never re-runs a
fixture's command block and never recomputes a digest. That is precisely why
**F1 passed the gate**. See **F8**.

### 1.6 `governance_sources` — the corpus is better than it says it is

`05-CONTRACT-INDEX.yaml` currently carries **27 `governance_sources` entries**:
6 `role: doctrine`, 10 `role: craft-policy`, 11 `role: topology`, each with
`file`, `words`, and a resolved `rule_ids` list. `build_contract_index.py:42–44`
points `GOV_SOURCES` at `../../doctrine`, `../../policies/craft-and-care`, and
`../../../map/topology-candidates` — the canonical homes, not packet copies —
and `--check` confirms no drift.

Three fixtures and the report state the opposite. See **F2**.

### 1.7 Phase-rule sweep

Literal sweep for `schedules nothing` / `specification of record from which` /
`phase boundary` / `phase rule` across all 32 modules returns hits in exactly
these files:

```
RFC-0006-…(single)                       RFC-0007/README.md
RFC-0007/rendering-and-surface.md        RFC-0008/README.md
RFC-0008/accounting-reconciliation-and-release.md
RFC-0009/README.md                       RFC-0009/interaction-parity-and-release.md
RFC-0010-…(single)                       RFC-0011-…(single)
```

`RFC-0001`, `RFC-0002` (all five files), `RFC-0003` (all three), `RFC-0004`
(all five), `RFC-0005` (all four) return **zero**. The index agrees: exactly six
clauses carry `kind: phase-rule` — RFC6-28, RFC7-38, RFC8-32, RFC9-52, RFC10-16,
RFC11-12. There is no phase rule for RFC-0001..RFC-0005 to include. See **F3**.

### 1.8 Front-matter sweep (T-1 corroboration)

32 module files; front-matter keys present across the whole set:
`applies_to`, `clauses`, `depends_on`, `governs`, `id`, `module`, `modules`,
`package`, `provides_to`, `status_source`, `tags`, `title`. Declared on **zero**
modules: `task_classes`, `risk_classes`, `terms`, `open_spec_mapping_status`,
`lifecycle`. `TASK-TO-CONTRACT-INDEX.md`'s finding T-1 is **confirmed exactly**,
by an independent method.

---

## 2. Completeness and boundedness, per fixture

### 2.1 Clause-citation spot-verification

Charge asked for ≥2 clause citations verified per re-run fixture. I ran 34
literal presence checks across all eight. Results — **33 confirmed, 1 apparent
miss that resolves on inspection**:

- **Fixture 1** — RFC7-38 present in `RFC-0007/README.md` (5×) under a heading
  literally named `Phase boundary` ✅; RFC7-11/11(a) in `narrative-contract.md`
  (11×) ✅; RFC7-23 (5×) ✅; VIS-4 in `vision.md` (6×) ✅.
- **Fixture 2** — RFC8-12 (17×) and RFC8-13 (5×) in `state-vocabulary-and-cost.md`
  ✅; RFC3-16 in `governance-homes-and-owner-acts.md` (58×) ✅; SEC-3 in
  `security.md` ✅; RFC5-25 cited inside the loaded governance-homes module (3×),
  supporting the fixture's "quoted at binding strength inside the module the
  packet carries" ✅.
- **Fixture 3** — RFC9-26 (8×) and RFC9-31 (3×) in `visual-grammar-and-lenses.md`
  ✅; RFC9-52 restated in the loaded README (7×) ✅. The claim "the README's
  package map names RFC9-49's rule" returned zero on the literal `RFC9-49`, but
  the README's reader map writes it as **`RFC9-46/47/49`** — "truth is never
  purchased with frame rate (module 3, RFC9-46/47/49)". The claim holds; the
  citation form defeated a literal sweep. Recorded so a later sweep does not
  re-raise it.
- **Fixture 4** — RFC5-18 (12×), RFC5-20 (7×), RFC5-21 (9×), RFC5-22 (5×),
  RFC5-23 (4×) all in the loaded `execution-profiles.md` ✅.
- **Fixture 5** — RFC10-8 (4×), RFC10-15 (3×) in RFC-0010 ✅; RFC8-12's
  two-field consumption rule restated in RFC-0010 ✅, supporting the
  RFC-0008-as-suggested reasoning.
- **Fixture 6** — the D1 recording precedent (3×) and the never-renumber rule
  (1×) both in the loaded `doctrine:README.md` ✅.
- **Fixture 7** — RFC1-11's exact sentence *"Split and merge mint successors,
  never mutations"* in RFC-0001 ✅; CC-BAR-5 in `engineering-bar.md` (3×) with
  floor-7 text `kernel identities` ✅; CC-DEP-2's deferral *"per the scheme
  RFC 0001 will fix"* in `interfaces-and-dependencies.md` ✅; CC-DEP-6 ✅.
- **Fixture 8** — RFC7-38 in `rendering-and-surface.md` (5×) with `3.13` ✅;
  RFC1-14 ✅ and RFC1-15's *"references, not owned content"* ✅ in RFC-0001;
  VIS-3 in `vision.md` ✅. The index row the fixture quotes —
  `{id: RFC7-38, module: RFC-0007/rendering-and-surface.md, kind: phase-rule}`
  — exists verbatim ✅.

### 2.2 Omission registers

Report §2's per-fixture omission table is **accurate**. I re-derived it
independently:

- Fixtures 1–5 account for all 11 contracts (each contract is loaded or named),
  but each leaves 3–4 doctrine files neither loaded nor named, none names the
  topology bundle or the historical lane, and fixture 4 names no craft policy
  despite loading one. Report §6e states exactly this and declines to edit it.
- Fixtures 6–8 each enumerate every doctrine file, the craft policies, the
  topology bundle, and the historical lane. Fixture 8 additionally registers
  `openspec/**` house conventions as a *real gap*, not an exclusion — the
  single most honest line in the set.
- "N of 32 absent" counts recomputed against the index's 32-module list:
  1→28, 2→25, 3→28, 4→28, 5→28, 6→30, 7→29, 8→28. **All eight match** the
  report and the three fixtures that state their own.

### 2.3 `TASK-TO-CONTRACT-INDEX.md` reader-map rows

All eight rows re-measured; **all eight reproduce exactly**:

| Row | Stated | Computed |
|---|---:|---:|
| Kernel implementer | 19,439 w / 26,242 | 19,439 / 26,242 |
| Polaris surface | 17,207 / 23,229 | 17,207 / 23,229 |
| Trajectory surface | 17,741 / 23,950 | 17,741 / 23,950 |
| Orrery surface | 24,166 / 32,624 | 24,166 / 32,624 |
| Adapter author | 13,286 / 17,936 | 13,286 / 17,936 |
| Security / execution-profile | 7,968 / 10,756 | 7,968 / 10,756 |
| Mission Control | 17,584 / 23,738 | 17,584 / 23,738 |
| Narrative author | 12,046 / 16,262 | 12,046 / 16,262 |

T-3's list of five rows above the §11.4 trigger is exact. T-1 is confirmed
(§1.8). **T-2 and T-4 are now false** — see **F6**.

### 2.4 Budget verdicts and waivers

Graded against charter §11.4 (default packet 5,000–15,000 tokens; above 20,000
→ justification or decomposition; "the limits are decomposition triggers, not
validity laws"):

- Inside the default band: **fixture 4 only** (14,705). Confirmed.
- Above the band, below the trigger: 1 (18,716), 3 (19,080), 5 (17,338),
  6 (15,574). Each discloses its band position; none claims a waiver it did not
  emit.
- Above the trigger: **2 (24,725), 7 (21,285), 8 (30,048)**. Each carries an
  explicit exception/justification/waiver in its own text. Fixtures 7 and 8
  additionally carry a **Reviewer: Unassigned — not reviewed** field stated as
  empty rather than implied complete, and 2 + 3 measured decomposition options
  respectively. This is the correct disclosure posture and I have no finding
  against it.

Report §3's ordering claims verified: fixture **2** is the first breach by
ordinal position (24,725), fixture **8** is the largest (30,048), fixture 7 also
breaches (21,285), fixture **1** is the first above the default band (18,716),
**seven of eight** are above the band, and **fixture 4 alone** is inside it. All
correct.

Report §6d's "under the working target, five of eight are inside" is correct
only under a *ceiling* reading of 06's "15–20k working target" (fixtures 1, 3,
4, 5, 6 are ≤20,000; fixture 4 at 14,705 is *below* 15,000). 06 itself uses the
ceiling reading — it marks fixture 4 "✓ within 15–20k target". Consistent, but
the report's own §3 correctly identifies this dual meaning as the root of the
prior report's error, so the ambiguity is documented rather than latent.

---

## 3. Determinism and the two guards

### 3.1 Same inputs → same selection

- `context_load.py` is order-insensitive in its total: fixture 7's argument list
  reversed returns **15,767 / 21,285**, identical. Fixtures 7 and 8 claim exactly
  this; verified.
- Fixture 6 states the stronger claim that the script "sums a set". It does not
  — it sums a *list*, with no dedup and no path canonicalization. Verified:
  `context_load.py rfcs/RFC-0002/README.md rfcs/RFC-0002/README.md` → **3,636 w**
  (double-counted), and `context_load.py doctrine:vision.md ../../doctrine/vision.md`
  → **4,312 w** for one file resolved two ways. See **F10**.
- Fixtures 6–8's selection reasoning is genuinely **enumerate-and-justify**, not
  narrative: each candidate is named with a reason, the RFC universe is closed at
  contract granularity, and the doctrine/craft/topology/history lanes are each
  either loaded or explicitly named. Fixture 7's departure from 06's reader map
  (dropping `RFC-0003/governance-homes` for a "kernel implementer" task) is
  called out **as a departure**, with the rule it applies instead and a pointer
  to fixture 3's precedent. That is the right shape.

### 3.2 Guard 1 — index cross-check

Present as a named section in fixtures 6, 7, 8 (each headed "Index cross-check,
with its limit stated"). **Absent as a named guard in fixtures 1–5** — fixture 1
carries an equivalent paragraph inside "Why no applicable constraint was lost"
("Every clause the warrant's entities cite in the index (`05-CONTRACT-INDEX.yaml`)
resolves into the selected set or into the suggested set"); fixtures 2, 3, 4, 5
do **not** mention the index at all. So the charge's premise — "the two guards
are present in all 8" — is only true if "present" means "the section the
verifier's substring check looks for". As a *cross-check against the index*, the
guard exists in 4 of 8 (1, 6, 7, 8).

Worse, in the three where it is named it is **stated as broken when it works**
(F2).

### 3.3 Guard 2 — packet digest

Present in all eight; reproduces in seven (§1.2). Fixture 8 fails (F1).

### 3.4 Does any fixture treat a generated summary as replacing exact authority?

**Yes — fixtures 1 and 3, on the corpus's own stated standard.** This is F4, and
it is the most substantive finding in this vertical after F1. Detail:

- RFC-0007's README "Phase boundary" section reads, in full: *"The phase rule
  **RFC7-38** binds the whole package … **The clause text is in
  `rendering-and-surface.md` §3.13**"*. It is a pointer, by its own words.
- RFC-0009's README says *"**RFC9-52 binds the package, not one module.** The
  phase rule names 'RFC9-1…RFC9-51'…"* — likewise a restatement; the clause text
  is in `interaction-parity-and-release.md`.
- Fixture 8's repair rationale (report §4.2, and the fixture's own §15 note)
  holds that loading the README instead of the module *"is exactly the
  summary-as-authority substitution the round exists to prevent — and it is where
  the RFC7-38 miss came from in the pre-repair draft"*.
- **Fixture 1 does the same thing to the same clause** and is graded ✅ in report
  §2. It selects `RFC-0007/README.md` + `narrative-contract.md`, omits
  `rendering-and-surface.md`, and asserts the phase rule "travels with the packet"
  on the strength of the README restatement — then adds that the index marks the
  clause `kind: phase-rule` "so a selector *can* force the full clause text",
  which this selection does not do.
- **Fixture 3 does the same for RFC9-52.**

RFC11-4's parenthetical — *"(the module or README text carrying it)"* — literally
permits both readings, so no fixture is unlawful. That is the defect: **the rule
admits two readings and the corpus applies both**, to the same contract, in the
same fixture set, and grades both ✅. RFC11-4 opens with "**same inputs, same
selection**".

---

## 4. Test C (charter §21) — run

> **Task:** *Propose how Trajectory should render a work item whose verification
> evidence is missing.*

Compiled with the corpus's own selection rules — RFC11-4 (deterministic from
`applies_to` + affected capability + declared risk class + `depends_on`, plus the
mandatory phase-rule inclusion), `TASK-TO-CONTRACT-INDEX.md`'s "Surface
implementer — Trajectory" row, and `06-CONTEXT-LOAD-MAP.md`'s "Surface
implementer (any)" reader map — then narrowed from role scope to warrant scope
the way fixtures 1–5 narrow.

### 4.1 Selection rule trace

- Warrant names **Trajectory** and a **rendering** decision → `applies_to:
  trajectory` selects **RFC-0008**. The decision is about a work item's *state
  and its evidential backing*, so module 2 `state-vocabulary-and-cost.md`
  (RFC8-12/13 normalized work state, the four absence values, the closure
  fallacy's home §6) and module 3
  `accounting-reconciliation-and-release.md` (RFC8-28 four-way chain state,
  RFC8-29 render-the-absence, RFC8-30 closure fallacy) are both mandatory. The
  package **README** carries the deterministic clause-lookup rule.
- **Module 3 also carries RFC8-32's clause text** (§3.16), so RFC11-4's
  mandatory phase-rule inclusion is satisfied *by clause text, not by the
  README's pointer* — deliberately taking fixture 8's reading of RFC11-4, not
  fixture 1's (F4).
- Rendering a state against evaluation vocabulary → **RFC-0002
  `rendering-vocabularies.md`** (the `declared-only` / `asserted-by-worker` /
  `reduced-fidelity` warrant table and its "visible, never green" rules).
- Evidence rules are doctrine → **`trust-and-evidence.md`**, which states it
  "holds the **normative statement of the trust floor**" and elaborates VIS-1,
  VIS-2, VIS-7.
- The charter names **accessibility** as a required dimension. Sweep result:
  RFC-0008 contains **no** accessibility obligation anywhere. The obligation that
  governs a Trajectory rendering is **CC-VIZ-4** in
  `craft:performance-and-visual-discipline.md` ("Non-3D views (2D, tabular,
  keyboard-navigable) are co-equal and semantically/query equivalent … Keyboard
  and non-3D navigation are always available (v1.md). This is an accessibility
  obligation and a trust obligation at once"). Mandatory.
- The charter names **security**. → **`doctrine:security.md`** (SEC-2 scoped
  consent for portfolio content; SEC-5 secrets never indexed). At 511 words it
  is cheap and squarely applicable to what a surface may disclose about an
  unverified item.

### 4.2 The compiled packet

```sh
python3 scripts/context_load.py rfcs/RFC-0008/README.md \
  rfcs/RFC-0008/state-vocabulary-and-cost.md \
  rfcs/RFC-0008/accounting-reconciliation-and-release.md \
  rfcs/RFC-0002/rendering-vocabularies.md doctrine:trust-and-evidence.md \
  craft:performance-and-visual-discipline.md doctrine:security.md
```

| File | Words |
|---|---:|
| `rfcs/RFC-0008/README.md` | 1,922 |
| `rfcs/RFC-0008/state-vocabulary-and-cost.md` | 3,507 |
| `rfcs/RFC-0008/accounting-reconciliation-and-release.md` | 3,055 |
| `rfcs/RFC-0002/rendering-vocabularies.md` | 2,397 |
| `doctrine:trust-and-evidence.md` | 1,069 |
| `craft:performance-and-visual-discipline.md` | 1,090 |
| `doctrine:security.md` | 511 |
| **TOTAL** | **13,551 w ≈ 18,293 est. tokens** |

**Packet digest:**
`4ae4e611bd12551e7eadab78bab0883d97315dbb34d90baeedb6d2683aa0378b`

**Size verdict: PASS, no waiver.** 18,293 est. tokens is **below the charter
§11.4 20,000-token trigger**, above the 5,000–15,000 default band (disclosed,
no waiver required), and **11.0% of the 166,306-token whole corpus**. It loads
**4 of 32** contract modules; 28 are absent. No waiver-with-reason needed.

**Omitted applicable candidates, with reasons.**
- `RFC-0008/identity-authority-materialization.md` — the materialization join is
  upstream of the rendering question; the durable identity a row renders against
  is consumed by identity, and module 1's clauses are not cited by RFC8-28/29/30.
  Suggested.
- `RFC-0006` — RFC8-31 binds every Trajectory rendering to RFC 0006 (selection by
  kernel identity, single drawer fact set, label parity, aggregation disclosure)
  and restates the obligations at binding strength inside the loaded module 3.
  Suggested, at 4,174 w, following fixture 1's authoring-strength-restatement
  rule. **This is the omission an owner should scrutinize most** — see §4.5.
- `RFC-0004` (evidence contract, all five modules) — the proposal renders the
  *absence* of evidence; what evidence *is* and how staleness is captured binds
  the adapter, not the renderer. Measured as an alternative: adding
  `execution-record.md` → 15,326 w ≈ **20,690** est. tokens, over the trigger.
  Suggested.
- `RFC-0002` README, `snapshot-and-evaluation-core`, `challenge-lifecycle`,
  `reconciliation-chain` — the packet consumes the rendering vocabulary; the
  evaluation is pinned by the packet's as-of. Adding the README (lookup rule) →
  15,369 w ≈ **20,748**, over the trigger. Omitted with disclosure: clause→module
  lookup for a cited `RFC2-n` is available mechanically from
  `05-CONTRACT-INDEX.yaml`, so the README's rule is not the only route.
- `RFC-0001/0003/0005/0007/0009/0010/0011` — no kernel identity change, no
  governed-home change, no client/execution surface, no other surface, no
  mission, no packet compilation in this task.
- `doctrine:vision.md` — **a disclosed gap, not a clean exclusion.** VIS-2's own
  rule text lives in `vision.md`; `trust-and-evidence.md` carries the normative
  trust-floor statement that elaborates it. Loading `vision.md` → 15,707 w ≈
  **21,204**, over the trigger. See §4.5.
- `doctrine:architecture.md`, `doctrine:v1.md`, `doctrine:README.md` — no loop or
  layout model change; no V0/V1 boundary question (though `v1.md` is the source
  CC-VIZ-4 cites for the keyboard/non-3D floor, which CC-VIZ-4 restates);
  no doctrine amendment.
- Craft policies other than `performance-and-visual-discipline.md` — no code,
  test, interface, observability, provenance, or secret-handling duty is
  exercised by a rendering proposal.
- Topology bundle (`.syzygy/map/topology-candidates/**`) — candidate material,
  binds nothing, no placement change. Named so the absence is a decision.
- `openspec/**` — **does not exist.** A real gap, rendered Unknown (RFC11-6),
  not an exclusion.
- `history/**`, `_bootstrap/**` — historical lane, never authority.

### 4.3 The six required dimensions, answered from the packet alone

| Dimension | Answer | Owning authority |
|---|---|---|
| **Applicable doctrine** | VIS-2 — no evidence yields **Unknown**, never green, never zero; VIS-7 trust floor; VIS-1 (a claim states its warrant). The normative trust-floor statement and the evidence/warrant seam are in `trust-and-evidence.md`, which declares itself the elaboration of VIS-1/2/7. | Doctrine — adopted 2026-07-30, binding |
| **Evidence rules** | Evidence is a durable, identified, integrity-verifiable artifact carrying source, capture time and scope (`trust-and-evidence.md`). Missing verification evidence is **not** a neutral state: RFC-0002's warrant table renders `declared-only` as a **composite** — the declaration Observed, its satisfaction **Unknown**, *both halves must render*; `asserted-by-worker` (an LLM assertion) is **Inferred, visible, never green, challengeable, never a status input**. | Doctrine + RFC 0002 `rendering-vocabularies` |
| **Relevant contract modules** | **RFC-0008 module 2** (RFC8-12/13 normalized state incl. the four absence values `state-undetermined` / `eligibility-undetermined` / `activity-undetermined` / `stale-or-dead`, and the closure-fallacy §6); **RFC-0008 module 3** — **RFC8-28** (the four post-merge answers *reconciled@E with evidence* / *merged, not yet evaluated* / *evaluated and unsatisfied* / *evaluated, contradiction raised* **must never share a rendering**; `unsatisfied` and `contradiction-raised` must never merge into one count or one badge), **RFC8-29** ("V0 renders the absence honestly — every merged-but-unreconciled item renders *reconciliation evidence absent / Unknown*, and a wall of such Unknowns is correct output, not a defect; nothing in V0 simulates a verdict"), **RFC8-30** (closure fallacy forbidden: no aggregate, badge, progress bar **or prose sentence** renders a `closed` item as done absent `reconciled@E` with gate-backed evidence — "a narrative sentence doing a badge's work is judged as a badge"; progress aggregates must disclose their reconciliation composition *n/m/k/c/j*); **RFC-0008 README** (lookup rule); **RFC-0002 `rendering-vocabularies`**. | RFC 0008 (candidate), RFC 0002 (candidate) |
| **Future-OpenSpec boundary** | **RFC8-32** (clause text at `accounting-reconciliation-and-release.md` §3.16): *"This contract schedules nothing … no implementation work for user-observable Trajectory behavior may be scheduled solely from this RFC."* The proposal is therefore a **specification input**, not schedulable work: every observable consequence — the badge, the composite render, the aggregate's disclosure line, the absent-evidence string — must map to an approved OpenSpec requirement/scenario in the governance root's `openspec/**`, or carry a reviewed N/A. A clause-to-requirement coverage matrix over **RFC8-1…RFC8-31, across all three modules** is produced at surface specification and is **review material, never authority**. `openspec/**` does not exist yet → the mapping renders **Unknown (RFC11-6)**, not "pending". | RFC8-32 (candidate); the seam itself is doctrine's V0/V1 discipline |
| **Accessibility obligations** | **CC-VIZ-4**: non-3D, tabular and keyboard-navigable views are **co-equal and semantically/query equivalent** — same evaluation, same filters, same epistemic state; they may expose finer detail, never a *different truth*; keyboard and non-3D navigation are always available. Consequence for this task: the "evidence missing" state must be conveyed **non-chromatically and in the tabular/keyboard path**, not by badge colour alone, and the tabular view must return the same rows for an "unverified" filter as any richer view. | Craft-and-care CC-VIZ-4 — **owner-approved (D2)**; clause-level force begins at foundational-contract acceptance |
| **Owning authority for each** | Doctrine (binding today) owns VIS-1/2/7 and the evidence/warrant seam. Craft (owner-approved, force pending) owns CC-VIZ-4 and CC-SEC-*. **RFC 0008 and RFC 0002 are candidates and bind nothing** — RFC8-28/29/30 may be *cited in the proposal as the shape being proposed*, never as authority for it. The OpenSpec plane owns the observable behaviour and **does not exist**. The rendering decision itself is an owner act. | — |

**Security obligations** (charter §21 groups these with accessibility):
**SEC-2** — portfolio content, including anything derived from it, leaves
owner-controlled infrastructure only through explicit scoped consent, so an
"evidence missing" drawer must not egress the work item's content to reach a
verdict; **SEC-5** — secrets are never indexed and unclassifiable content fails
closed, so the absent-evidence rendering must not surface excluded content as a
way of explaining the absence.

### 4.4 Test C verdict

**PASS.** Complete on all six dimensions, plus security, from a 4-module,
13,551-word packet — **18,293 est. tokens, under the 20,000 trigger, no waiver
needed, 11.0% of the corpus**. The full corpus was not loaded and was not
needed.

### 4.5 What the exercise revealed about the indexes' usability

Reported as findings F11–F13; summarized here because the charge asks for it
directly.

1. **The routing indexes cannot answer two of Test C's six dimensions.** Both
   `06-CONTEXT-LOAD-MAP.md`'s "Surface implementer (any)" row and
   `TASK-TO-CONTRACT-INDEX.md`'s "Surface implementer — Trajectory" row route to
   *owning surface package + RFC-0002 rendering + RFC-0006* and nothing else. No
   doctrine source, no craft source. A compiler that followed either row
   literally would produce a packet that **cannot state the accessibility
   obligation or the security obligation** — and would still weigh 23,950 est.
   tokens, *above* the trigger, while being *less* complete than my 18,293-token
   packet. The reader map's own caveat ("a role's orientation, not a task
   packet", T-3) is correct and does not go far enough: the rows are not merely
   oversized, they are **incomplete on dimensions the charter's own acceptance
   test requires**. Adding a doctrine/craft column to the eight rows would close
   this.
2. **Accessibility has no home on the work surface.** Sweeping
   `accessib|WCAG|contrast|colou?r-blind|screen reader|keyboard` across all 32
   modules, all doctrine and all craft returns: `RFC-0009/interaction-parity-and-release.md`
   (6 accessibility hits), `RFC-0007/rendering-and-surface.md` (keyboard only),
   `RFC-0007/narrative-contract.md` (contrast only), `doctrine:v1.md`,
   `doctrine:trust-and-evidence.md`, and `craft:performance-and-visual-discipline.md`.
   **RFC-0008 has zero.** Trajectory's accessibility floor is reachable only via
   a craft policy whose clause-level force has not yet begun. That is a genuine
   structural gap in the corpus, surfaced by running Test C rather than by
   reading about it.
3. **Doctrine selection granularity is file-level, so RFC11-1 cannot be honored
   as written.** RFC11-1 requires a packet to identify "the **exact doctrine
   rules** included, by identifier". `05-CONTRACT-INDEX.yaml`'s
   `governance_sources` gives `rule_ids` **per file** — `vision.md` carries
   VIS-1..VIS-7, `trust-and-evidence.md` carries SEC-5, VIS-1, VIS-2, VIS-6,
   VIS-7 — with no rule→offset mapping. To include VIS-2 by identifier I must
   load a whole 2,156-word file, or load its 1,069-word elaboration and disclose
   that the rule's own text is absent. I chose the latter and disclosed it. A
   clause-granular doctrine projection (the same shape the RFC clause rows
   already have) would close this, and would have let my packet answer the
   doctrine dimension from rule text rather than from its elaboration.
4. **What worked well.** `05-CONTRACT-INDEX.yaml`'s clause rows are genuinely
   load-bearing: `{id: RFC8-32, module: RFC-0008/accounting-reconciliation-and-release.md,
   kind: phase-rule}` told me in one lookup which module to force, with no
   search — the same mechanism that caught fixture 8's pre-repair miss. The
   package READMEs' contiguous-disjoint-range lookup rule resolved every
   `RFC8-n` I needed without opening a second file. `context_load.py` made the
   budget question a measurement rather than a guess, and the three measured
   alternatives above cost seconds each. The **selection** machinery is good; the
   **routing tables** are the weak layer.

---

## 5. Findings

### F1 — Fixture 8's stated packet digest does not reproduce — **BLOCKING**

`fixtures/context-selection-8-openspec-authoring.md` states
`36be8f90fa12a01d…` as the sha256 over its mandatory files concatenated in
listed order. Recomputed from the fixture's own command block, under the
fixture's own stated method and its own stated `doctrine:`/`craft:` resolution:

```
14488b9b31892bfedc2b00261b6214abbfa937b6f828a91e5ee9fc8127eefdd3
```

The word total (22,258) and every per-file row reproduce exactly, so the file
set is right and one or more member files changed **word-neutrally** after the
digest was taken. Attribution by mtime is conclusive: of fixture 8's six files,
only `rfcs/RFC-0007/README.md` (**04:33:20**) is newer than the fixture itself
(**04:27**); the other five are 00:54–04:08 or Aug-3. That is the same
word-neutral README edit whose effect on **fixture 1** was caught and refreshed
at 04:36 (`43c7e35a…` → `4544d4b2…`, per the lead disposition in report §6a).
**Fixture 8 shares the file and did not get the refresh.** I attempted
single-word attribution (substituting the "Twelve citation edges" count through
Three–Eleven and re-hashing) and reproduced none of them, so the edit was larger
than the one word the disposition note names — worth knowing before repair.

Severity is blocking because of *where* it lands, not its size. Fixture 8 is the
fixture that devotes an entire "Digest-source pinning" section to the principle
that *"a packet pins the exact source digests it compiled from precisely so that
a later change … **invalidates this packet rather than silently changing what it
meant**"* — and then ships a digest that does exactly the thing it warns about,
under a `[x]` checklist. Its parenthetical *"(Live proof: three accepted-set
fixtures no longer reproduce their stated digests…)"* is now doubly wrong: all
five accepted fixtures reproduce (§1.2), and fixture 8 is the sole
non-reproducer in the set.

**Repair:** re-run the fixture's command block, restate the digest, add a
re-measure note in the form fixtures 2/4/5 already use, and update the "live
proof" parenthetical in fixtures 6, 7 and 8 (F12).

### F2 — Three fixtures and the report state `governance_sources` is empty; it is not — **MATERIAL**

Fixtures 6, 7 and 8 each carry, under "Index cross-check, with its limit
stated", a paragraph asserting:

> The index's `governance_sources` list is **empty** in the current tree — the
> doctrine and craft packet copies it enumerated were removed when the candidate
> package moved to its tracked home — so **doctrine selection cannot be
> cross-checked against the index today**.

Report §6c states the same, with an `[Observed]` label and a causal explanation
(`build_contract_index.py` scans relative to the package root; the packet copies
are gone; the generator emits an empty list).

**Measured:** `05-CONTRACT-INDEX.yaml` currently carries **27 `governance_sources`
entries** — 6 `role: doctrine`, 10 `role: craft-policy`, 11 `role: topology` —
each with `file`, `words`, and resolved `rule_ids`. `build_contract_index.py:42–44`
points `GOV_SOURCES` at `../../doctrine`, `../../policies/craft-and-care` and
`../../../map/topology-candidates` — the **canonical homes**, exactly the
"regenerating `governance_sources` from the canonical homes would close it" fix
§6c proposes. `--check` reports no drift.

So the round already performed the repair and three fixtures plus the report
still describe the pre-repair state. Consequence: the corpus **understates its
own guard**. Every doctrine and craft selection in fixtures 6–8 *could* have been
cross-checked against the index and was instead cross-checked "against those
files directly, not against the projection. Stated rather than ticked." The
honesty is admirable and the fact is wrong. A reviewer or compiler reading these
three fixtures learns that a working mechanism is broken.

Note the residual truth worth preserving in the repair: `rule_ids` are
**file-scoped, not clause-scoped**, so the index still cannot cross-check a
selection *at rule granularity* (F13). The corrected sentence should say that,
not "empty".

### F3 — Two fixtures tick a phase-rule check over contracts that have no phase rule — **MATERIAL**

- **Fixture 6:** *"RFC-0003's governing phase rule travels with its package
  (RFC11-4's mandatory-inclusion rule) in the selected README and module."*
- **Fixture 7:** *"RFC-0001 and RFC-0002 each travel with their governing phase
  rule (RFC11-4's mandatory-inclusion rule): RFC-0001 is a single file carrying
  its own, and the selected RFC-0002 README carries the package's — no loaded
  contract's boundary rule is missing."*

**Measured (§1.7):** a four-pattern literal sweep across all 32 modules finds
phase-rule text in RFC-0006, RFC-0007, RFC-0008, RFC-0009, RFC-0010 and RFC-0011
only. RFC-0001, all five RFC-0002 files, all three RFC-0003 files, all five
RFC-0004 files and all four RFC-0005 files return **zero**. The index agrees:
exactly six clauses carry `kind: phase-rule`, none of them in RFC-0001..0005.
`RFC-0002/README.md` contains no phase-rule text at all.

The *conclusion* ("no loaded contract's boundary rule is missing") is vacuously
true — there is nothing to miss. The *reasoning* is false, and it is false in the
specific way these two fixtures were repaired to avoid: a check reported as
performed against an object that was never inspected. Both fixtures elsewhere go
out of their way to state limits rather than tick boxes; these two sentences are
the exception.

There is a second-order point the owner may want: **five of eleven foundational
contracts carry no OpenSpec phase rule.** Whether the kernel and the evaluation,
governance-home, evidence and execution contracts *should* carry one is a real
question (charter §11.6 requires every user-observable consequence in "surface
and Mission contracts" to be marked, which may be the deliberate scope). Either
way, the fixtures should say "RFC-0001 and RFC-0002 declare no phase rule" rather
than inventing one.

### F4 — RFC11-4's phase-rule inclusion rule admits two readings and the corpus applies both — **MATERIAL**

RFC11-4: *"The mandatory set always includes the governing phase-rule clause of
every selected contract **(the module or README text carrying it)** — no lawful
packet omits the boundary rule of a contract it loads."*

Two incompatible applications, both graded ✅ in report §2:

| Fixture | Contract | Phase rule | Clause text in | Loaded? | Fixture's position |
|---|---|---|---|---|---|
| 8 (repaired) | RFC-0007 | RFC7-38 | `rendering-and-surface.md` §3.13 | **yes — added by repair** | loading only the README *"is exactly the summary-as-authority substitution the round exists to prevent"* |
| 1 (accepted) | RFC-0007 | RFC7-38 | `rendering-and-surface.md` §3.13 | **no** | the README's restatement means the rule *"travels with the packet"* |
| 3 (accepted) | RFC-0009 | RFC9-52 | `interaction-parity-and-release.md` | **no** | *"the package phase rule"* is in the mandatory set |

Verified text: RFC-0007's README says, in its own words, *"The clause text is in
`rendering-and-surface.md` §3.13"* — it is a pointer. RFC-0009's README
similarly restates RFC9-52 and locates it in module 3. Report §2 explicitly
grades fixture 1's inclusion ✅ ("the primary §20.4 reviewer … reported 'I could
not name a mandatory clause any of fixtures 1–5 omitted'") while report §4.2 and
§2's closing paragraph name the identical structure in fixture 8 as the failure
mode that gap admits.

This is not a stylistic inconsistency. RFC11-4's first sentence is *"Mandatory
context is selected **deterministically** — same inputs, same selection"*. Here
the same contract with the same phase rule yields two different mandatory sets
depending on which fixture you read. The clause's parenthetical is the ambiguity
and it is inside act 1's digest set, so this is an owner call, not an edit:
either (a) narrow RFC11-4 to require the module carrying the clause text — which
adds `rendering-and-surface.md` (3,143 w) to fixture 1, taking it from 18,716 to
**22,960** est. tokens, over the trigger, and `interaction-parity-and-release.md`
(3,027 w) to fixture 3, from 19,080 to **23,166**, also over; or (b) confirm the
README restatement suffices, in which case fixture 8's repair 2 was unnecessary
and its waiver shrinks from 30,048 to **25,806**. **The reading is worth
~4,200 est. tokens per surface packet and flips two fixtures' budget verdicts
either way** — which is exactly why it should be ruled rather than left to the
parenthetical.

### F5 — The eight fixtures do not cover the charter §15 fixture list — **MATERIAL**

Charter §15 enumerates the eight fixtures to create:

> 1. doctrine amendment; 2. kernel identity change; 3. OpenSpec authoring;
> 4. **evidence adapter change**; 5. Polaris presentation edit;
> 6. **Trajectory lifecycle change**; 7. Orrery lens change;
> 8. **bounded Mission across two capabilities**.

Against what exists:

| Charter item | Fixture | Verdict |
|---|---|---|
| doctrine amendment | 6 | covered |
| kernel identity change | 7 | covered |
| OpenSpec authoring | 8 | covered |
| **evidence adapter change** | — | **absent.** Fixture 2 is a *work-provider* adapter mapping change and explicitly omits RFC-0004 `execution-record` and `fidelity-joins-and-mappings` — the evidence-capture modules an evidence-adapter fixture exists to exercise |
| Polaris presentation edit | 1 | covered |
| **Trajectory lifecycle change** | — | **absent.** Fixture 2 changes a substrate→normalized-state *derivation mapping*, not the lifecycle; no fixture exercises RFC-0008 module 1 (`identity-authority-materialization`) or module 3 |
| Orrery lens change | 3 | covered |
| **bounded Mission across two capabilities** | 5 (partial) | fixture 5 is a **cross-*project*** Mission (RFC10-15 two-plane authority split), not cross-*capability* |
| — | **4** (security/execution profile) | an **extra**, not on the charter list |

So five of eight charter items are cleanly covered, one partially, two not at
all, and one fixture is off-list. Nothing in the fixture report,
`06-CONTEXT-LOAD-MAP.md`, or `TASK-TO-CONTRACT-INDEX.md` compares the delivered
eight against the charter's eight — the report's §1 table presents "the eight
fixtures" as if the count were the coverage. It also matters more than a
bookkeeping mismatch: the two missing fixtures are the two that would have
exercised **RFC-0004's evidence lane** and **RFC-0008 modules 1 and 3**, and my
Test C run (§4) had to select from RFC-0008 module 3 with no worked precedent to
check against. Fixture 4 should be kept — it is the only fixture inside the
default band and the only one demonstrating a craft-policy pull — but it should
be numbered as an addition, not as a charter item.

### F6 — `TASK-TO-CONTRACT-INDEX.md`'s findings T-2 and T-4 are false against the current tree — **MATERIAL**

- **T-2** claims fixtures 2, 4 and 5 state stale totals, listing "As stated in
  the fixture: 18,302 / 24,707", "10,854 / 14,652", "12,830 / 17,320". The
  fixtures now state **18,315 / 24,725**, **10,893 / 14,705**, **12,843 /
  17,338** — all current, all reproduced by me (§1.1), each carrying a
  2026-08-05 re-measure note. T-2 describes a state repaired before it was
  published (index mtime 04:30; fixtures 04:35–04:36).
- **T-4** claims *"`06-CONTEXT-LOAD-MAP.md` line 16 carries a stale module
  figure: RFC-0003 governance-homes **4,401 w**, actual **4,414 w**."* 06 line 16
  currently reads `manifests 4,824 · governance-homes 4,414 · README 920`. The
  figure is correct; T-4 is false.

The index's own header says *"every figure below is `scripts/context_load.py`
output, re-run 2026-08-05"* and its §Findings says *"Recorded, not repaired"*.
Recorded findings that describe a repaired state are worse than no findings: a
reader who trusts T-2 will "fix" three fixtures that are already correct, and
T-4 sends them to edit a line that already carries the right number. Both should
be struck or restated as *resolved this round*, with the resolving change named.

### F7 — The fixture report's §6b and §6g claims are no longer supported by their own evidence — **MATERIAL**

§6b: *"`06-CONTEXT-LOAD-MAP.md` is stale in four places."* All four measured
against the current 06:

| §6b claim | Current 06 | Verdict |
|---|---|---|
| lists governance-homes at 4,401 (now 4,414) | reads **4,414** | false |
| fixture table carries pre-drift figures for 2, 4, 5 | reads 24,725 / 14,705 / 17,338 — current | false |
| baseline reads "~121,000 words ≈ 163,000 est. tokens" | reads **"~123,200 words ≈ 166,300 estimated tokens (re-measured 2026-08-05)"** | false |
| "lists five fixtures where the home now holds eight" | carries an explicit note that 6–8 are measured in the fixture report and *"deliberately not routed from here until reviewed"* | addressed |

§6g: *"The candidate knowledge-hygiene craft policy does not exist yet. The task
expected it at `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md`;
`policy-candidates/` is absent from the candidate package at the time of
writing."* **`policy-candidates/` exists** (mtime 04:26) and contains
`CRAFT-KNOWLEDGE-HYGIENE-POLICY.md` (22.7 KB, mtime 04:26), which defines
**CC-BUDGET-1..4** and carries a correct "Candidate — binds nothing … not
installed at that cluster's canonical home" banner.

The *substance* of fixtures 6–8's parenthetical survives — the policy is a
candidate, is not installed, and no `CC-BUDGET-*` identifier resolves to a
governed artifact, so citing charter §11.4 directly remains the right call. But
§6g's factual claim is wrong, and its closing sentence ("When the policy lands
and carries that table under stable clause identifiers, three citations should be
re-pointed") should now read as an *available* action, not a future one — the
table's candidate home exists today and the owner can see the clause IDs.

§6b and §6g together mean the report's "findings recorded, not fixed" register
is stale in six of its own sub-claims while presenting itself as this round's
current state. §6a, by contrast, was kept current by an explicit dated lead
disposition — that is the pattern the other two need.

### F8 — The corpus's own validation cannot catch a stale packet digest — **MATERIAL**

`verify_final_prespec.py:237–246` checks that ≥5 `context-selection-*.md` files
exist and that each contains six substrings. It never executes a fixture's
command block, never recomputes a word total, and never recomputes a digest. The
report's §7 phrasing — *"All **eight** files now satisfy it — the three repaired
fixtures pass because §4.4 restored the accepted-set structure, not because the
check was relaxed"* — is accurate about *structure* and silent about the fact
that the check has no *content*. F1 is the direct consequence: a fixture shipped
a wrong digest through a green gate.

This is the cheapest high-value repair in the vertical. The fixtures already
state their commands in fenced blocks in a uniform shape; a checker that parses
each fixture's ` ```…scripts/context_load.py …``` ` block, re-runs it, and
compares the word total and the sha256 prefix against the fixture's stated
figures is on the order of 15–25 lines and would have caught F1, T-2's original
subject, and the fixture-1 refresh, mechanically. Until it exists, "PASS — all
checks clean" over the fixture block means only that six words appear in eight
files.

### F9 — Corpus baseline is ten words low — **MINOR**

Report §1: *"123,180 words … (99,080 RFC + 7,783 doctrine + **9,405** craft +
6,912 topology)"*. Measured: craft `wc -w` = **9,415** (per-file:
972+1282+506+1059+830+1090+649+1068+846+1113). Corrected total **123,190 w ≈
166,306 est. tokens**. The 11.4% median-share figure survives (18,898/166,306 =
11.36%). `INSTALL-RECORD.md`'s mtime (04:31:10) postdates the other nine craft
files (04:08:54), so the drift is almost certainly there. Flagged because the
report's own Method section says *"no figure is hand-estimated or copied forward"*
— this one no longer reproduces.

### F10 — `context_load.py` does not dedupe or canonicalize paths — **MINOR**

Verified:

```
$ context_load.py rfcs/RFC-0002/README.md rfcs/RFC-0002/README.md
   3636  TOTAL words          # one 1,818-word file, counted twice
$ context_load.py doctrine:vision.md ../../doctrine/vision.md
   4312  TOTAL words          # one 2,156-word file, two resolutions
```

`main()` iterates the argument list and sums; `resolve()` returns a path without
canonicalizing against previously resolved paths. Consequences: (a) a selection
that names a file twice — easy when a module is pulled by two selection rules,
which is the normal RFC11-4 case — silently inflates the budget figure and could
push a lawful packet over the trigger, or mask a repair; (b) fixture 6's claim
*"order-independent (`context_load.py` **sums a set**)"* is wrong about the
mechanism even though its conclusion (order-independence) is right and verified.
A three-line `seen = set(); if p.resolve() in seen: continue` fixes both, and the
script should print a `[dedup]` note to stderr the way `resolve()` already prints
`[source]` — silent dedup would trade one invisible behaviour for another.

### F11 — The routing indexes route no doctrine or craft source for any surface task — **MINOR (material for Test C)**

`06-CONTEXT-LOAD-MAP.md`'s reader map gives "Surface implementer (any): owning
surface package + RFC-0002 rendering + RFC-0006"; `TASK-TO-CONTRACT-INDEX.md`'s
three surface rows transcribe it. Neither routes doctrine or craft. Of the eight
reader-map rows, only two ("Security/profile work", "Narrative author") name a
doctrine or craft source at all.

Test C (§4.5) is the demonstration: a packet compiled from the Trajectory row
weighs **23,950** est. tokens — above the trigger — and still cannot state the
accessibility obligation (CC-VIZ-4, craft) or the security obligation
(SEC-2/SEC-5, doctrine), two of the six dimensions charter §21 requires. My
warrant-scoped packet is 5,657 tokens *smaller* and complete. T-3 already
observes that the rows are role-scoped and oversized; the completeness half is
unrecorded. A doctrine/craft column on the eight rows would close it.

### F12 — Fixtures 6, 7 and 8's "live proof" parenthetical is now false — **MINOR**

All three carry: *"(Live proof that this is not hypothetical: three accepted-set
fixtures no longer reproduce their stated digests after the P-6 and P-7 fixes —
see the fixture report.)"* As of this review **all five accepted fixtures
reproduce exactly** (§1.2) — they were refreshed, and report §6a's lead
disposition says so. The only fixture in the set that does not reproduce is
fixture 8 (F1). The rhetorical point (a stale digest is the correct visible
outcome) is sound and worth keeping; the example must be re-pointed or the
parenthetical dropped. Repairing F1 without repairing F12 would leave three
fixtures citing as proof a condition that no longer holds.

### F13 — `governance_sources` `rule_ids` are file-scoped, so RFC11-1's "exact doctrine rules by identifier" is not achievable from the projection — **MINOR**

RFC11-1 requires a packet to identify "the **exact doctrine rules** included, by
identifier". The index gives `{file: doctrine/vision.md, words: 2156, rule_ids:
[VIS-1..VIS-7]}` — membership, not location. There is no doctrine analogue of the
RFC clause rows (`{id: RFC8-32, module: …, kind: phase-rule}`), so a compiler can
determine *that* VIS-2 is in `vision.md` and in `trust-and-evidence.md` but
cannot include VIS-2 without including one whole file. In Test C this cost me the
choice between 2,156 words for VIS-2's rule text and going over the trigger; I
disclosed the gap instead (§4.2). This is the residue of F2 that survives the
correction, and it is the natural next increment to
`build_contract_index.py` — the doctrine files already carry stable `VIS-n`/`SEC-n`
identifiers in headed form.

---

## 6. What is genuinely strong — recorded so the findings are not read as a verdict on the whole

- **Seven of eight packet digests and eight of eight word/token totals reproduce
  byte-exactly**, from the fixtures' own command blocks, on a machine that never
  saw the authoring session. So do all 17 secondary figures (§1.3), all eight
  reader-map rows (§2.3), all eight "N of 32" counts (§2.2), and both repository
  validators (§1.5). That is a high bar met.
- **Report §3's budget-ordering correction is right, and its self-correction is
  the right shape** — it names the prior claim, states it is false, gives the
  computed replacement, and identifies the *root* (two baselines meaning
  different things in adjacent sentences) rather than just the symptom.
- **The unticked checkbox in fixtures 6–8** — *"No generated summary replaces
  exact authority — not verifiable by the script"* — left unticked in all eight
  rather than ticked by association, is exactly the VIS-2 discipline the project
  claims. So are the two **"Reviewer: Unassigned — this waiver has not been
  reviewed"** fields, stated as empty rather than implied complete.
- **Report §5** ("these are selection fixtures, not packets"; RFC11-1 requires
  envelope, permissions, contradictions, as-of identity, compiler version, none
  of which any fixture demonstrates) pre-empts the single most likely downstream
  misreading, and does so in the report rather than in a footnote.
- **Report §4.3 and §6h** flag fixture 7's craft inclusion as *this pass's
  judgment, not a reviewer finding*, name it as the repair most likely to be
  reversed, and price both readings. That is how a contestable call should be
  handed to an owner.
- **RFC-0011 itself is not implicated by any finding above.** Its clauses are
  coherent, RFC11-1..12 are contiguous, RFC11-12's phase rule is present and
  shape-parallel with its five siblings, and RFC11-5's mandatory/suggested split
  is what makes every budget disclosure in the set honest rather than a trim. F4
  is a genuine ambiguity in RFC11-4's parenthetical, not a defect in the
  contract's design. My findings are against the **evidence layer** — three
  fixtures, two indexes and one report — not the contract.

---

## 7. Verdict

Reproducibility is strong and I can say so with numbers: 8/8 measurements, 7/8
digests, 17/17 secondary figures, 8/8 reader-map rows, 8/8 module counts. Test C
passes at 18,293 estimated tokens — 11.0% of the corpus, under the trigger,
complete on all six charter dimensions plus security, without loading the full
corpus. Nothing here warrants REJECT, and the honesty discipline in fixtures 6–8
and the report is above the bar.

But four things must be repaired before this evidence layer can be relied on: a
stated digest that does not reproduce in the fixture that most loudly defends
digest pinning (F1); three fixtures and the report declaring a working guard
broken (F2); two fixtures reporting a check performed against a phase rule that
does not exist (F3); and one clause read two incompatible ways inside a set whose
governing rule opens with "same inputs, same selection" (F4). F5 adds a coverage
gap against the charter's own fixture list that no artifact in the vertical
checks. None is unfixable; all are specific.

**EXCEPTIONS**
