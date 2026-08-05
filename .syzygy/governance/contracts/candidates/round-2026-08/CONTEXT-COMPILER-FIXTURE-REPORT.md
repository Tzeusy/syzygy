# Context Compiler fixture report — round 2026-08

**Status:** working report of a candidate package. **Not authority.** It
records measurements and verdicts about the eight context-selection
fixtures; the contract they exercise is RFC-0011, which this pass did not
edit.

**Scope.** All eight fixtures now live in one home,
`.syzygy/governance/contracts/candidates/fixtures/`: the five accepted-set
fixtures (1–5, unchanged by this pass) and three candidate fixtures (6–8),
consolidated here from `_bootstrap/knowledge-refactor/fixtures/` and repaired
against the two stored §20.4 reviews
(`_bootstrap/knowledge-refactor/reviews/20-4-context-compiler-RAW.md` and
`…/20-4b-context-compiler-respawn-RAW.md`, both **EXCEPTIONS**).

**Method.** Every word and token figure below is `scripts/context_load.py`
output run in this session against **canonical-home bytes as of 2026-08-05**;
no figure is hand-estimated or copied forward from the prior report. Every
"N of 32" count is computed by diffing a fixture's selection against the
module list in `05-CONTRACT-INDEX.yaml`. Packet digests are sha256 over the
mandatory files concatenated in listed order, computed by script. Budget
verdicts are graded against the **charter §11.4 context-budget table**
(default packet 5,000–15,000 tokens; above 20,000 → explicit justification or
task decomposition; "the limits are decomposition triggers, not validity
laws"). The table's intended home — the candidate knowledge-hygiene craft
policy — **does not exist in the tree at the time of writing**, so §11.4 is
cited directly and no `CC-BUDGET-*` or `KA-*` identifier is used anywhere in
the fixtures: none resolves to a governed artifact.

**Supersedes** `_bootstrap/knowledge-refactor/CONTEXT-COMPILER-FIXTURE-REPORT.md`,
which remains in the git-excluded historical lane, unedited, and carries two
claims corrected here (§3, §6f).

---

## 1. The eight fixtures — computed loads and budget verdicts

| # | Task | Mandatory files (RFC modules) | Words | Est. tokens | §11.4 verdict | Waiver / justification emitted |
|---|---|---:|---:|---:|---|---|
| 1 | Polaris narrative / requirement re-anchor | 5 (4) | 13,864 | **18,716** | above 5–15k default band; below 20k trigger | no — band position disclosed in the load map |
| 2 | Trajectory work-provider adapter mapping | 8 (7) | 18,315 | **24,725** | **above the 20,000 trigger** | yes — disclosed risk-class exception, stated in-fixture |
| 3 | Orrery architecture-lens change | 5 (4) | 14,134 | **19,080** | above default band; below trigger | no |
| 4 | Security / execution-profile amendment | 6 (4) | 10,893 | **14,705** | **inside the default band** | not required |
| 5 | Cross-project Mission draft | 5 (4) | 12,843 | **17,338** | above default band; below trigger | no |
| 6 | Doctrine / shape amendment (D3) | 6 (2) | 11,537 | **15,574** | above default band by 574 tokens; below trigger | no — band position disclosed |
| 7 | Kernel identity change | 5 (3) | 15,767 | **21,285** | **above the 20,000 trigger** | yes — justification + 2 measured decomposition options, reviewer unassigned |
| 8 | OpenSpec requirement authoring | 6 (4) | 22,258 | **30,048** | **above the 20,000 trigger — largest in the set** | yes — waiver + 3 measured decomposition options, reviewer unassigned |

Corpus baseline, measured today: **123,180 words ≈ 166,293 estimated
tokens** (99,080 RFC + 7,783 doctrine + 9,405 craft + 6,912 topology
candidates). Median fixture load is 18,898 est. tokens — **11.4%** of
whole-corpus loading, which was rev9's only safe instruction.

Fixtures 2, 7 and 8 exceed the justification trigger. **In every case the
cause is corpus structure, not careless selection**: an indivisible
8,353-word kernel (fixtures 7, 8) or an authorization-bearing change that may
not shed its authorization contract (fixture 2). Each says so in its own text
and measures the alternatives rather than trimming mandatory context, which
RFC11-5 forbids.

## 2. §15 checklist verdicts, per fixture

| # | All mandatory context included | Unrelated modules excluded | Stable on identical inputs | Budget respected **or** waiver emitted | Omissions recorded | No generated summary replaces exact authority |
|---|---|---|---|---|---|---|
| 1 | ✅ | ✅ 28/32 absent | ✅ | ✅ (band disclosed) | ⚠️ partial | ⬜ not mechanically verifiable |
| 2 | ✅ | ✅ 25/32 absent | ✅ | ✅ (exception disclosed) | ⚠️ partial | ⬜ |
| 3 | ✅ | ✅ 28/32 absent | ✅ | ✅ | ⚠️ partial | ⬜ |
| 4 | ✅ | ✅ 28/32 absent | ✅ | ✅ | ⚠️ partial | ⬜ |
| 5 | ✅ | ✅ 28/32 absent | ✅ | ✅ | ⚠️ partial | ⬜ |
| 6 | ✅ (repaired) | ✅ **30/32** absent | ✅ | ✅ | ✅ | ⬜ |
| 7 | ✅ (repaired) | ✅ **29/32** absent | ✅ (order-independence re-run) | ✅ justification emitted | ✅ | ⬜ |
| 8 | ✅ (repaired) | ✅ **28/32** absent | ✅ (order-independence re-run) | ✅ waiver emitted | ✅ | ⬜ |

**"All mandatory context included"** is a *verified* ✅ for fixtures 1–5 —
the primary §20.4 reviewer adversarially tested inclusion on fixtures 1, 2,
4, 5 and reported "I could not name a mandatory clause any of fixtures 1–5
omitted." For fixtures 6–8 it is a ✅ *after repair*; both reviewers found
mandatory-inclusion failures in the pre-repair drafts (§4 below).

**Omission-register completeness — the ⚠️ is precise, not a hedge.** All
eight fixtures account for the RFC contract universe: no fixture leaves any
of the 11 contracts both unloaded and unnamed (checked mechanically at
contract granularity). The five accepted fixtures do not extend that
discipline beyond the RFCs:

| # | Doctrine files neither loaded nor named | Craft named | Topology named | Historical lane named |
|---|---|---|---|---|
| 1 | architecture, v1, trust-and-evidence | blanket | no | no |
| 2 | vision, architecture, v1, trust-and-evidence | blanket | no | no |
| 3 | vision, v1, trust-and-evidence | blanket | no | no |
| 4 | vision, architecture, v1, trust-and-evidence | no | no | no |
| 5 | architecture, v1, security, trust-and-evidence | blanket | no | no |
| 6 | **none** | ✅ enumerated | ✅ | ✅ |
| 7 | **none** | ✅ enumerated | ✅ | ✅ |
| 8 | **none** | ✅ enumerated | ✅ | ✅ |

The repaired fixtures set the higher bar; fixtures 1–5 were left untouched by
instruction, so the gap is recorded as a finding (§6e), not edited away.

**"No generated summary replaces exact authority"** is unchecked in all
eight, old and new. A fixture names files; nothing in the packet or the
script can establish that a consuming agent read the **clause** rather than a
README, an index, or its own prior summary — `context_load.py` reports
identical totals either way. This is a contract-level obligation (RFC11-7)
with no fixture-level test. Fixture 8 is the concrete instance of the failure
mode that gap admits: its pre-repair draft loaded RFC-0007's README, whose
phase-rule text is a restatement pointing at a module the packet did not
load, and no mechanical check caught it (§4, repair 2).

## 3. Correction — which fixture first breached a budget

The prior report claimed of fixture 8: *"It is the first fixture in the set
to breach a context budget,"* and the pre-repair fixture 8 carried the same
sentence. **That claim is false, and it is corrected in both the fixture and
here.** Computed today:

- Against the §11.4 **20,000-token justification trigger**, the first
  breaching fixture by ordinal position is **accepted fixture 2, at 24,725
  estimated tokens** — recorded as a disclosed exception in its own text and
  in `06-CONTEXT-LOAD-MAP.md` since rev10. Fixture 8's 30,048 is the
  **largest** breach in the set, not the first. Fixture 7, at 21,285, also
  breaches.
- Against the §11.4 **5,000–15,000-token default band**, the first fixture
  above it is **fixture 1, at 18,716**, and *seven of the eight* are above
  it. The only fixture inside the default band is **fixture 4, at 14,705**.

The prior report's error had a second root worth naming: it graded against
the load map's *"15–20k working target"* while the fixtures cited a *"5–15k
default band"*, so "breach" meant different things in adjacent sentences. All
verdicts in this report use one baseline — §11.4 — applied to all eight. The
two baselines still coexist in the tree; reconciling them is an owner call
(§6d).

## 4. What was repaired in fixtures 6–8

Each repair is traceable to a finding in one or both stored reviews; both
reviewers independently found repair 1.

1. **Fixture 6 now loads `doctrine:architecture.md`** — the primary D3
   amendment site, carrying the substantive bounded-mission insertion. The
   pre-repair fixture stated "the amended text itself is mandatory" and then
   omitted half of it, from both its mandatory set *and* its exclusion
   register. It also now loads **`doctrine:README.md`**, home of the
   amendment log, the D1 recording precedent the draft's adoption mechanics
   cite, and the identifier-stability rule. Cost: 8,546 words / 11,537 est.
   tokens → **11,537 words / 15,574 est. tokens** — above the default band,
   still below the justification trigger.
2. **Fixture 8 now loads `rfcs/RFC-0007/rendering-and-surface.md`** — the
   module carrying RFC7-38's clause text. RFC11-4 requires the governing
   phase-rule clause of every selected contract; the README the fixture
   already loaded restates RFC7-38 and points at this module, and the index
   marks the clause `kind: phase-rule`. It also now loads
   **`doctrine:vision.md`**: the task's output is an owner-approved spec
   delta, so VIS-3/VIS-4's adoption gate governs — matching accepted fixture
   1, which loads `vision.md` for the same gate on the same contract. Cost:
   16,933 → **22,258 words** (22,859 → 30,048 est. tokens); the waiver now
   states the honest number.
3. **Fixture 7 now loads `craft:engineering-bar.md`.** The fixture declares
   its risk class *as* CC-BAR-5 floor 7 (the identity floor), and that floor
   text — the obligation the change may not weaken — was restated nowhere in
   its selection. This follows fixture 4's precedent, where a declared craft
   duty pulls the owning craft policy. **This is a selection judgment made in
   this pass, not a reviewer finding, and it is what takes fixture 7 from
   19,554 to 21,285 est. tokens — across the trigger.** It is reversible in
   one line: if the owner rules that a floor cited to *classify* a change is
   not text the implementer must hold, drop the file and the packet returns
   to 19,554, inside the trigger. The fixture states both readings and the
   measured cost of each.
4. **Full section parity with the accepted set restored.** Fixtures 6–8 had
   dropped three of the five accepted-set sections — including the two guards
   that would have caught repairs 1 and 2: *"Why no applicable constraint was
   lost"* (the index cross-check) and the *packet digest*; and *"Suggested
   inferred additions"*, RFC11-5's mandatory-core/suggested-additions
   distinction, which they had no section for at all. All three now carry all
   five sections, in the accepted order, plus a §15 verification checklist as
   a trailing addition. Running the restored cross-check on fixture 8 is what
   located the RFC7-38 module miss.
5. **All "N of 32 modules absent" counts recomputed mechanically.** The three
   claimed 28 / 26 / 27 against a 32-module universe; no single counting rule
   made all three true. Computed by diffing each selection against
   `05-CONTRACT-INDEX.yaml`'s module list: **30 / 29 / 28** (fixture 8's
   figure reflects its added module). Doctrine, craft and topology files are
   `governance_sources`, not modules, and are excluded from the denominator.
6. **One budget baseline, cited to a resolvable artifact.** The pre-repair
   fixtures graded themselves against `CC-BUDGET-1/2/3` and `KA-10/KA-23`,
   which resolve to no governed artifact — they exist only in draft process
   documents in the git-excluded lane — and fixtures 6 and 7 used *different*
   baselines from each other. All three now cite the charter §11.4 table
   directly, with its status stated, and use the same band and trigger.
7. **Omission reasoning normalized to the accepted set's style.** The three
   fixtures reasoned about exclusions in structural-metadata prose and a
   "Deliberately excluded" table; they now enumerate applicable candidates
   with reasons, in the accepted set's bullet form, under the accepted
   heading — same inputs, same selection, omissions enumerated rather than
   argued. Each now accounts for **every** doctrine file, the craft policies,
   the topology bundle, and the historical lane.
8. **Wrong-home waiver citation fixed.** RFC-0001's oversize waiver is
   recorded in `03-ACTIVE-CONTRACT-COMPACTION-REPORT.md`; RFC-0001 records
   none. Fixture 7 and the prior report both said "its own oversize waiver".
   Corrected in fixtures 7 and 8 (both now cite the 03 report and say
   explicitly that RFC-0001 carries no waiver of its own). The prior report's
   copy is superseded by this file, not edited (§6f).
9. **Digest-source pinning note added to each of 6–8.** Each states that its
   digest and totals are computed over canonical-home bytes as of
   2026-08-05, that no packet copies of doctrine or craft exist under this
   root any more (so there is exactly one resolution and no silent source
   swap), and that a packet pins the exact source digests it compiled from so
   a later change — a D3 adoption amending `architecture.md`/`vision.md`, the
   CC-TEST-2 amendment landing in `testing-and-verification.md`, or any
   corpus edit — **invalidates the packet rather than silently changing
   what it meant.** §6a is the live proof that this is not hypothetical.

**A size asymmetry the repairs introduce, stated rather than hidden.** The
accepted fixtures are ~3 KB each; repaired 6–8 are 8.5–12.8 KB. The
difference is entirely disclosure — waiver tables, measured decomposition
options, and registers that enumerate every doctrine file, craft policy,
topology candidate and historical lane rather than a blanket line. It is the
right trade for fixtures whose pre-repair defects were *invisible omissions*,
but it means the eight-fixture set is not uniform in length, and a future
pass that levels them should level *up* (extend 1–5's registers, §6e) rather
than trim 6–8's disclosures.

## 5. What no fixture can verify

The §15 check *"no generated summary replaces exact authority"* has no
fixture-level test, in any fixture, old or new — see §2. It is left unticked
in all eight rather than ticked by association. This is the same class of
limit as a second one worth stating plainly: **these are selection fixtures,
not packets.** RFC11-1 requires a packet to carry the evaluation and as-of
identity, the work warrant and autonomy envelope, allowed tools and
permissions, active contradictions and Unknowns, and compiler/adapter
versions. All eight fixtures demonstrate the **document-selection dimension
only**. "Eight measured fixtures" must not be read downstream as "the packet
format is validated."

## 6. Findings recorded, not fixed

These are outside this pass's write scope (fixtures 6–8 and this report
only), or are owner calls.

**a. Three accepted-set fixtures no longer reproduce their stated totals or
digests.** Computed this session, canonical bytes:

| # | Stated words | Measured | Stated digest prefix | Measured |
|---|---:|---:|---|---|
| 1 | 13,864 | 13,864 ✅ | `43c7e35a32e2294f` | matches ✅ |
| 2 | 18,302 | **18,315** | `be9284e68214059e` | **`a398a06362074451`** |
| 3 | 14,134 | 14,134 ✅ | `2e408eaf40278ca7` | matches ✅ |
| 4 | 10,854 | **10,893** | `cfe8cc2aebbaaf90` | **`a56fb116fa588b9b`** |
| 5 | 12,830 | **12,843** | `5c09ae303809d225` | **`c92c6f8a936b12b0`** |

Cause, isolated: `rfcs/RFC-0003/governance-homes-and-owner-acts.md` grew 13
words when the P-6 retired-acceptance-phrase fix landed (its current bytes
match `ACTIVE-CONTRACT-MANIFEST.txt`, so the manifest is consistent — the
fixtures are what went stale), and `craft:security-and-secrets.md` grew 26
words under the P-7 banner fixes. Fixtures 1 and 3 load neither file and
still reproduce exactly. **This is the digest-pinning hazard behaving
correctly**: the stale digests are visible, not silent. The fix is a
decision, not an edit I should make — restate the three fixtures' figures at
current bytes, or re-pin them to the byte state they were computed from.

> *Lead disposition, 2026-08-05 (same round, after this report was stored):
> RESTATED. Fixtures 2/4/5 were refreshed to current bytes (figures and
> digests above, "Measured" column) with re-measure notes in each fixture.
> A later word-neutral byte fix in `rfcs/RFC-0007/README.md` (cross-module
> edge count 7→12) then staled fixture 1's digest as well; it was refreshed
> the same way (`43c7e35a…` → `4544d4b2…`, 13,864 w unchanged). Fixture 3
> still reproduces its original digest. Each refresh is independently
> recomputable from the fixture's own command block.*

**b. `06-CONTEXT-LOAD-MAP.md` is stale in four places.** Its module table
lists governance-homes at 4,401 words (now 4,414); its fixture table carries
the pre-drift figures for fixtures 2, 4 and 5; its corpus baseline reads
"~121,000 words ≈ 163,000 estimated tokens" against a measured 123,180 ≈
166,293; and it lists five fixtures where the home now holds eight. Its
sentence *"Each fixture records its omitted-candidate reasons and packet
digest"* is now true of all eight — that one repaired itself.

**c. The contract index cannot cross-check doctrine, craft, or topology
selection.** `05-CONTRACT-INDEX.yaml`'s `governance_sources` list is
**empty**. [Observed] `build_contract_index.py` scans `doctrine/`,
`craft-and-care/` and `topology/` **relative to the package root**
(`GOV_SOURCES`); those were packet copies, and none exists under
`candidates/` since the package moved to its tracked home, so the generator
skips all three and emits an empty list. `build_contract_index.py --check`
reports "index matches regeneration — no drift", so this is a faithful
projection of an incomplete input, not index drift. Consequence: the
"index cross-check" section of every fixture can verify RFC clause coverage
but must verify doctrine and craft selection against the files directly.
*Lead disposition, 2026-08-05 (after this report was stored): CLOSED.*
`GOV_SOURCES` was repointed at the canonical homes
(`../../doctrine`, `../../policies/craft-and-care`,
`../../../map/topology-candidates`) and the index regenerated;
`governance_sources` now carries 26 entries and `--check` reports no drift.
Fixtures 6–8 were updated to record the limit as historical rather than
current. The finding above is preserved as written.

**d. Two budget baselines coexist in the tree.** The charter §11.4 table
(5–15k default, 20k trigger) and `06-CONTEXT-LOAD-MAP.md`'s "15–20k working
target" grade the same fixtures differently — under §11.4 seven of eight are
above the default band; under the working target, five of eight are inside.
RFC11-11 deliberately leaves the numeric figure to policy and RFC-0011 §8 q1
leaves its custody to the owner, so this is exactly the open question, now
with measurements attached. Until it is ruled on, any "budget respected"
claim must name its baseline.

**e. Fixtures 1–5's omission registers stop at the RFC universe** (§2 table):
each leaves three or four doctrine files neither loaded nor named, none names
the topology bundle or the historical lane, and fixture 4 names no craft
policy despite loading one. Not edited, by instruction. If the accepted set
is ever reopened, matching fixtures 6–8's enumerate-everything form is a
small, mechanical change.

**f. The prior report retains two corrected claims.**
`_bootstrap/knowledge-refactor/CONTEXT-COMPILER-FIXTURE-REPORT.md` still
says fixture 8 is "the first fixture in the set to breach a context budget"
(§3) and cites RFC-0001's oversize waiver to RFC-0001 itself (§4.8). It sits
in the git-excluded historical lane, which is never a default reading path
and never authority, and this pass does not write there. This report
supersedes it.

**g. The candidate knowledge-hygiene craft policy does not exist yet.** The
task expected it at `policy-candidates/CRAFT-KNOWLEDGE-HYGIENE-POLICY.md`;
`policy-candidates/` is absent from the candidate package at the time of
writing. Fixtures 6–8 therefore cite the charter §11.4 table directly. When
the policy lands and carries that table under stable clause identifiers,
three citations in fixtures 6–8 should be re-pointed to the clause IDs — a
one-line change per fixture, listed here so it is not forgotten.

**h. Fixture 7's craft inclusion is this pass's judgment, not a reviewer
finding** — see §4.3. It is the one repair that changes a fixture's headline
budget verdict, and it is the one an owner is most likely to want to reverse.
Both readings and their measured costs are stated in the fixture.

## 7. Verification evidence

Run in this session, from `.syzygy/governance/contracts/candidates/`, with
all eight fixtures in place:

```
$ python3 scripts/verify_final_prespec.py
…
PASS — all checks clean

$ python3 scripts/build_contract_index.py --check
index matches regeneration — no drift
```

The verifier's fixture block globs `fixtures/context-selection-*.md` and
requires ≥5 files, each carrying the sections *Required context*, *Omitted*,
*estimate*, *constraint*, *Suggested*, *digest*. All **eight** files now
satisfy it — the three repaired fixtures pass because §4.4 restored the
accepted-set structure, not because the check was relaxed. Two pre-existing
notes are unchanged by this pass (RFC-0001's justified oversize; total corpus
above the target band).
