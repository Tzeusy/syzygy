I have everything I need. Writing the review of record.

# RD-32c — Wave B exact-package review, third administration (round-2026-08e, frozen commit 18afdd4)

## 0. Clone state, subject identification, and the recomputed argument

**Clone.** `/tmp/claude-1000/-home-tze-GitHub-syzygy/3fa62952-e192-440e-8b1f-5b48212d8da1/scratchpad/clone-08e-r17`. `git log -1` = `18afdd4`; `git status --porcelain` returned **0 lines** at session start. Nothing was written, created, or deleted anywhere; every command run was read-only. The live repository at `/home/tze/GitHub/syzygy` was never read. [Observed]

**The argument, recomputed two ways this session** [Observed]:

| Method | Result |
|---|---|
| `sha256sum wave-manifests/WAVE-B-MANIFEST.txt` | `193e3c1e15e4b1375f938d62c9e8c1a442984313e0794ada5965d2cdf9d7e3ed` |
| Python `hashlib.sha256(open(p,'rb').read())` over the same file | identical |
| `check_governance.py` CG-7b | "6 wave-act arguments match the wave manifests — 0 findings" |

**Against §1 row B.** The row reads `ACCEPT FOUNDATIONAL WAVE B: 193e3c1e15e4b1375f938d62c9e8c1a442984313e0794ada5965d2cdf9d7e3ed` — **byte-identical** to my recomputation. CG-7d independently re-verifies every act digest quoted anywhere (9 quotations, 0 findings). [Observed]

**Per-module recomputation.** Every manifest row re-hashed individually from the candidates root with Python `hashlib`, denominator computed from non-comment rows, not read off the header: **11 of 11 OK, zero mismatches.** [Observed]

**Stale predecessors, verified by git rather than by trust** — the manifest's own digest at each commit that moved it [Observed]:

| Digest | Commit | Row-B account | Verdict |
|---|---|---|---|
| `daa6a5dd37b7f92a…` | `771965c` (round-08d) | "retiring the round-08d argument `daa6a5dd…`" | ✓ |
| `2041ad053127cb1f…` | `31ebc52` (wave-wide batch, all 11 modules) | "retiring `2041ad05…`" | ✓ |
| `c0fd0e27cb309deb…` | `246af62` (RD-27 batch) | "retiring `c0fd0e27…`" | ✓ |
| `052acfb8c54bf6b7…` | `1a23d19` (RD-32 batch) | "retiring `052acfb8…`" | ✓ |
| `193e3c1e15e4b137…` | `18afdd4` (RD-32b batch) | current | ✓ |

Four regenerations in round-2026-08e (`31ebc52`, `246af62`, `1a23d19`, `18afdd4`), four stale predecessors, each named and marked "**All four earlier arguments are stale and satisfy nothing.**" **The row's history account is accurate in every particular.** [Observed]

**Wave A's argument is unmoved.** `WAVE-A-MANIFEST.txt` hashes to `8972d9630b95f5d4266432dbb1b3602114576bbd6c0f29d6f9bd6f905b1f884a` at `HEAD`, at `b00c3dd`, and at `1a23d19` — the digest RD-31b's `VERDICT: CONFIRM` is bound to. Verified by `git show <commit>:<path> | sha256sum`, not by reading the record. [Observed]

---

## 1. Method

Read: the acceptance record entire; `WAVE-B-SEMANTIC-DELTA.md` §13; `reviews/DISPOSITION-REGISTER.md` (RD-32 and RD-32b sections); `reviews/RD-32b-wave-b-RAW.md`; `reviews/DELIVERY-AND-VERDICT-REGISTER.md`; `PENDING-OWNER-DECISIONS.md` (launch-scope index, rows P-1 and P-21); `PROJECT-STATUS.md`; then the subject clauses side by side — RFC9-47 and RFC9-47(a) in full, RFC9-43, RFC7-37, RFC6-17, RFC6-22, RFC6-23, RFC2-24 — and every sweep site in the 11 modules.

Every sweep was run **this session** in Python `re`, never through the clone's ugrep bracket classes (rule 1), and states its denominator (rules 2, 9). Check **output** was read, never exit codes (rule 4). Every obligation quoted is anchored to a defined clause and quoted (rule 8). Cross-wave hits were classified by reading each site (rule 5). Digests are scripted (rule 3). Two claims I formed mid-review were killed by running the sweep with its full denominator; both are recorded in §5.4 rather than suppressed.

---

## 2. The eight RD-32b findings, verified against the actual bytes

| # | Class | Repair claimed | Verdict at the bytes |
|---|---|---|---|
| N-1 | MAJOR, digest-moving | RFC9-47's gate list gains the aggregation-attribution entry | **Closed** |
| N-2 | MINOR, digest-moving | RFC7-37's enumerated gloss deleted | **Closed** (one residual, §5.1) |
| N-3 | record | row B's "four modules" → seven | **Closed** |
| N-4 | record | "1,067" → **763**, method named in-row | **Closed — and reproduced exactly** |
| N-5 | record | three stale review-state statements + PROJECT-STATUS | **Closed** (4 sites verified) |
| N-6 | register | launch-scope Wave B bullet gains P-21(a) | **Closed** (one misquotation in the register row, §5.2) |
| N-7 | carried | the false "no WARN" figure recorded, not propagated | **Correctly carried** |
| N-8 | record | register row carries the clone-commit explanation | **Closed** |

### 2.1 N-1 — the aggregation-attribution entry

**Where it landed.** `rfcs/RFC-0009/interaction-parity-and-release.md` lines 131–142, inside **RFC9-47**'s release-gate enumeration (the clause opens at line 106 and its closing `[Inferred …]` note stands at 214–218), placed between the **work-state two-field consumption (RFC9-32)** entry and the **declared-vs-observed relation separation (RFC9-9)** entry. [Observed]

**The entry, quoted whole:**

> "**aggregation attribution** (RFC9-43, restating RFC6-17's own rule: per-Unknown-reason counts are computed over **primary reasons only** — one claim instance contributes exactly one — with secondary annotations (RFC2-24) disclosed separately and never folded into the primary counts; run at aggregate level against a fixture whose members carry secondary annotations, since a fixture without them passes vacuously over the exact failure RFC6-17 states the rule prevents — two conforming surfaces producing divergent Unknown-reason totals over one declared scope, the disagreement RFC6-23 classes release-blocking; routed 2026-08-10, RD32b-N1 — the rule entered RFC9-43 with the RD-32 batch and RFC9-47(a) part 1 makes routing it here part of the same amendment, never later housekeeping)"

**Does it state the rule RFC9-43 imports, or a paraphrase that drifts?** I read RFC6-17, RFC9-43 and the new entry side by side. **RFC6-17 — Aggregation discloses** (defined clause, `rfcs/RFC-0006-cross-surface-selection-query-drawer.md`):

> "**Per-Unknown-reason counts are computed over primary reasons only** — one claim instance contributes exactly one — with secondary annotations (RFC2-24) disclosed separately and never folded into the primary counts; otherwise two conforming surfaces could produce different Unknown-reason totals over one declared scope while both satisfying this clause, which RFC6-23 would then class as a release-blocking disagreement."

The entry's operative span — *"per-Unknown-reason counts are computed over primary reasons only — one claim instance contributes exactly one — with secondary annotations (RFC2-24) disclosed separately and never folded into the primary counts"* — is **word-for-word RFC6-17's own text**, not a paraphrase. **Zero drift.** [Observed]

**Is the failure mode stated correctly?** RFC6-23 (defined clause) forbids two equivalent renderings disagreeing on, among others, "**a count over the same declared scope**," and classes any such disagreement "release-blocking under the trust floor." The entry's "two conforming surfaces producing divergent Unknown-reason totals over one declared scope, the disagreement RFC6-23 classes release-blocking" **is that clause, accurately**. [Observed]

**Is `RFC2-24` the right anchor for "secondary annotations"?** RFC2-24 — Twelve reasons, closed: "Every Unknown claim instance carries exactly one primary reason from this list (secondary reasons may annotate) … **The secondary-annotation vocabulary is closed, and it is this same list.**" The term is defined there, and the entry's "one claim instance contributes exactly one" is RFC2-24's own "exactly one primary reason." [Observed]

**Is it shaped and placed like the list's other entries?** Yes. Every entry in the list takes the form *bold gate name* + parenthetical naming the clause, the rule, and — where the failure mode is fixture-reachable — the fixture that reaches it, with the vacuity argument stated. Compare the neighbouring RFC9-32 entry ("run against a fixture carrying **every chain outcome the release can produce** … since a gate exercised only over merged-not-yet-evaluated data passes vacuously") and the RFC9-9 entry ("exercised over a portfolio fixture carrying both … since a single-project fixture cannot reach it"). The new entry's "run at aggregate level against a fixture whose members carry secondary annotations, since a fixture without them passes vacuously" is **the same idiom, applied correctly**. The grammar of the list's single governing sentence is unbroken. [Observed]

**Does it close the harm RFC9-47's closing note records?** The note, quoted: *"**This list is what craft-and-care consumes, so an obligation absent from it is tested nowhere** — demonstrated twice, once by a review finding six absences and once by a review finding the equivalence tuple short of two fields the gate then could not see."* The obligation is now present in the list craft-and-care consumes. **The harm is closed.** [Observed]

**Did the entry mint a new defect?** Four adversarial checks, each run:

| Check | Result |
|---|---|
| New cross-wave reliance? | The entry cites RFC6-17, RFC6-23 (RFC-0006) and RFC2-24 (RFC-0002). The module's front matter declares `depends_on: [RFC-0001, RFC-0002, RFC-0003, RFC-0006, RFC-0007, RFC-0008]`. **All three inside a declared edge; no deferred-wave edge; no new front matter minted** (`build_dependency_index.py --check`: 176 `depends_on`, **8 `constrains`**, matching regeneration — unchanged). [Observed] |
| New restated figure? | No numeral, count, or measurement appears in the entry. CG-21 ("contract prose states no measurement — 39 modules examined, **0 findings**") corroborates over its own population. [Observed] |
| Divergence from RFC6-17's own words? | None — the operative span is verbatim (above). [Observed] |
| **RFC9-47(a) part 1 applied to the entry itself** — does it create a checkable obligation it fails to route? | **No.** The entry's three obligations (primary-only computation; secondaries disclosed separately; the aggregate-level fixture) are the gate's own content, sitting in the gate list. Nothing is created elsewhere. Part 2's registry-completeness check reaches "every consumed cross-RFC gate this list cites," which is exactly the RFC6-17/RFC6-23 pairing the entry names. **The same-defect-one-level-down test passes.** [Observed for the clause text; Inferred for the sufficiency conclusion] |

**N-1: closed.**

### 2.2 N-2 — the RFC7-37 gloss

**Deleted.** The clause now reads (`rendering-and-surface.md` 307–313):

> "**Any roll-up over a child's facts additionally discloses RFC6-17's full composition** — the RFC6-22 equivalence tuple, expandable to members — **cited, never restated here**, because a paraphrase is how a roll-up rule drifts from the aggregation contract it instantiates — as this sentence itself demonstrated: its own enumerated gloss fell four items behind RFC6-17 across two repair batches before being deleted (2026-08-10, RD32b-N2)."

The enumerated list ("per-label, per-tier, per-Unknown-reason and per-freshness-state counts and sibling surface states") is **gone**; git confirms it stood byte-identical from `771965c` through `1a23d19` and was removed only at `18afdd4`. [Observed]

**Does the clause still bind what it bound?** Yes, and slightly more. The operative term is unchanged — "**RFC6-17's full composition**" — and the residual descriptor "the RFC6-22 equivalence tuple, expandable to members" is RFC6-17's own framing ("The disclosed composition is the full RFC6-22 equivalence tuple"; "supports expansion to its members"), not an enumeration that can fall behind. A conforming implementation is bound to RFC6-17's full set, which is now the *only* reading available. **The obligation is intact and the drift surface is gone.** [Observed]

**N-2: closed**, with one residual on the replacement sentence's precision — finding N-1c, §5.1.

### 2.3 N-3 — the RD-27 module count

Row B now reads "for the RD-27 batch (**seven modules** — delta §11's own '*Modules touched (7 of 11)*'; this row said 'four' until 2026-08-10, RD32b-N3)". `git diff --name-only 31ebc52 246af62` over the wave returns **seven** modules, independently recomputed this session. **Closed, and the corrected figure is correct.** [Observed]

### 2.4 N-4 — the citation figure, recomputed by me

Row B now reads: "**763 RFC 0001–0006 clause citation tokens — `RFC[1-6]-\d+` swept over the 11 manifest modules at the RD-32b rebind, 2026-08-10, replacing an unreproducible '1,067' per RD32b-N4 and rule 3**."

**My own count, run this session over the clone's bytes, denominator 11 modules, Python `re`:**

| n | module |
|---:|---|
| 43 | `rfcs/RFC-0007/README.md` |
| 82 | `rfcs/RFC-0007/narrative-contract.md` |
| 70 | `rfcs/RFC-0007/rendering-and-surface.md` |
| 6 | `rfcs/RFC-0008/README.md` |
| 85 | `rfcs/RFC-0008/accounting-reconciliation-and-release.md` |
| 85 | `rfcs/RFC-0008/identity-authority-materialization.md` |
| 124 | `rfcs/RFC-0008/state-vocabulary-and-cost.md` |
| 14 | `rfcs/RFC-0009/README.md` |
| 41 | `rfcs/RFC-0009/interaction-parity-and-release.md` |
| 124 | `rfcs/RFC-0009/semantic-geography.md` |
| 89 | `rfcs/RFC-0009/visual-grammar-and-lenses.md` |
| **763** | **total** |

**My count is 763 — identical to the row's, to the digit.** The delta between RD-32b's 758 at `b00c3dd` and 763 here is exactly the +5 tokens the batch added (RFC6-17 ×2, RFC2-24, RFC6-23 in the RFC9-47 entry; RFC6-17 ×1 in RFC7-37), which I verified from the diff. The method named in-row reproduces. **Closed; rule 3 correctly applied to the ceremony row itself.** [Observed]

### 2.5 N-5 — the three (four) stale review-state statements

| Artifact | Current text | Against the register's verdicts |
|---|---|---|
| Record §1 row A | "**RD-31b reviewed the current argument `8972d963…` exactly and returned `VERDICT: CONFIRM` (2026-08-10 …)** — the offer is now withheld solely by §7 item 11, until P-33 is ruled" | ✓ matches `RD-31b-wave-a-RAW.md` and the register row, verdict word copied exactly |
| Record §6 | "**Review state per wave (2026-08-10): Wave A's current argument `8972d963…` carries RD-31b's `VERDICT: CONFIRM` … Wave B's current argument awaits RD-32c after RD-32b returned `VERDICT: REVISE`; no C/D argument carries any round-2026-08e review**" | ✓ accurate; the retired "No CONFIRM verdict is bound to the current argument" is retained struck as a dated correction, not deleted |
| `PENDING-OWNER-DECISIONS.md` P-1 row | "**Review state 2026-08-10: Wave A's current argument carries RD-31b's `VERDICT: CONFIRM` (offer withheld solely by P-33, §7 item 11); Wave B's current argument awaits RD-32c after RD-32b's `VERDICT: REVISE`**" | ✓ |
| `PROJECT-STATUS.md` (two sentences, lines 69–73 and 114–116) | "Wave A's fresh exact-package review (RD-31b) returned `VERDICT: CONFIRM` … its offer is now withheld solely by P-33 (§7 item 11); Wave B's offer waits on RD-32c" | ✓ |

Every dated correction marker names its finding (`RD32b-N5`) and preserves the superseded sentence rather than deleting it — the record's established convention. **Closed, 4 of 4 sites.** [Observed]

### 2.6 N-6 — the launch-scope index's Wave B bullet

Now reads: "**Ratified or reverted at the Wave B act (nothing withholds this offer):** P-38 …; **P-22** …; **and P-21(a) for its Wave B instance (the RFC8-12/RFC9-32 declared-nowhere mutual restriction; §7 item 18 — 'the same open ruling covers a declared-nowhere instance inside Wave B'; added 2026-08-10, RD32b-N6).** The acts stay sequenced A → B (P-1)." The quoted fragment is verbatim in §7 item 18, which I read. **Closed.** [Observed] One misquotation in the *disposition register's* row for this finding — N-2c, §5.2.

### 2.7 N-7 — the carried denominator correction

The disposition register row: *"RD-32's 'no WARN names a Wave B module' was false (CG-8 names six as report-only decomposition-review triggers); recorded here so the figure cannot reach the Wave B closure report as a measurement."* **The carry is recorded.** [Observed]

**Did the false figure reach a new artifact?** Sweep for the literal string `WARN names a Wave B` over every `.md` in the clone (denominator: whole tree, `_bootstrap/` absent): **5 hits — `RD-32-wave-b-RAW.md` (the original, frozen and correctly not edited under rule 10), `RD-32b-wave-b-RAW.md` ×2 (the correction), the disposition register (marking it false), and the delivery register (marking it false).** **No artifact carries it as true; no new artifact carries it at all.** [Observed]

My own battery independently reproduces the correction: `check_governance.py` CG-8 (WARN, report-only, 43 artifacts, 15 findings) names Wave B modules as §11.4 decomposition-review triggers; CG-20's 52 findings are confined to `06-CONTEXT-LOAD-MAP.md`, `TASK-TO-CONTRACT-INDEX.md` and `candidates/README.md` — **no module**. [Observed]

### 2.8 N-8 — the register row's clone-commit discrepancy

The RD-32b row now carries, in-row and dated: *"(First attempt at `36c01a9`/clone-08e-r13 failed on the account session limit before any verdict — nothing stored; this fresh administration ran at `b00c3dd`/clone-08e-r14, where the Wave B bytes are byte-identical. RD-32b's N-8 notes the clone's register still named the r13 commit — true of the clone: the live row was corrected at `aa1a40d`, after the clone froze)."* **Explanation present, dated, and accurate: `aa1a40d` precedes `18afdd4` in this clone's history.** [Observed]

---

## 3. Regression over the RD-32 repairs — none regressed

RD-32b found all six closed at `052acfb8…`. Re-verified against the current bytes:

**3.1 B1 — RFC9-43 ↔ RFC6-17, item for item.** Read side by side this session. Seventeen items enumerated from RFC6-17's text; **all seventeen present in RFC9-43**: membership count; expansion to members; "the full RFC6-22 equivalence tuple"; per-label; per-tier; per-Unknown-reason; per-freshness-state; sibling surface states; `challenge-pending` (RFC2-13); per-value chain-state counts (RFC6-19 class 8, where members carry them); per-value normalized-work-state counts; the "never … disclosing nothing about reconciliation" consequence; the primary-reasons-only computation rule; the RFC6-23 release-blocking rationale; tier counts covering all six RFC2-25 tiers, named; the three sibling surface states per RFC6-14; "never label and Unknown reason alone." **The identity claim — "so the two are deliberately identical" — remains true as written.** `visual-grammar-and-lenses.md` is byte-identical to its `b00c3dd` state (§4.6), so no edit could have disturbed it. [Observed]

**3.2 The in-place markers.** Sweep `\bP-\d+\b` over the 11 modules: **exactly 2 hits** — `rendering-and-surface.md:383` under **RFC7-39** (defined 370) and `semantic-geography.md:143` under **RFC9-8(a)**. Both name the question, the round, the ratify-or-revert consequence, the revert alternative and the §7 item. **Standing, unchanged.** [Observed]

**3.3 Row B's solo-act sentence.** Present and intact, with only the N-4 figure substituted inside it: *"**Performed alone — before act 1 — this act binds eleven surface contracts whose operative predicates (11 of 11 modules' `depends_on`; 763 RFC 0001–0006 clause citation tokens …) resolve into unaccepted Wave A candidate text: lawful only stated at the act, and the offer path is A → B**."* **Standing.** [Observed]

**3.4 The launch-scope verb split.** Wave A bullet: "**Withholds the Wave A offer:** P-33 … **Ratified or reverted at the Wave A act (the offer, once live, stands):** P-31, P-37, **P-28**, and P-21(a)." Wave B bullet: "**Ratified or reverted at the Wave B act (nothing withholds this offer):** …". Matches §7 items 11, 15, 16, 17, 18. **Standing, and now complete.** [Observed]

**3.5 m2 / m3.** No new `constrains:` edge (8, matching regeneration); §7 item 18 and P-21's row both carry the RFC8-12 ↔ RFC9-32 disclosure; delta §7's reviewed text remains unedited with §12 and §13 as addenda. **Standing.** [Observed]

**None of the six regressed under the N-1/N-2 edits.**

---

## 4. Sweeps and battery — run this session, output read, denominators stated

### 4.1 Mechanical battery

| Check | Output (read, not inferred from exit code) |
|---|---|
| Per-row `sha256sum -c` / Python re-hash | **11/11 OK**, 0 mismatches |
| `check_governance.py` | **30 OK / 18 WARN / 0 FAIL over 48 checks** — counts derived by the script |
| CG-7a | 78 entries, 0 findings; active manifest `250c543f…` (package identity, no act's argument) |
| CG-7b | **6 wave arguments match their manifests**, 0 findings |
| CG-7c / 7d / 7e / 7f / 7g | 0 findings each (3 / 9 / 3 / 6 / 6 examined) |
| CG-2a | **352 files, 2 retired phrases declared, 0 presented as current, 0 unmarked** |
| CG-4a / CG-4b | banners present; **105 files claim no acceptance** |
| CG-13 | **185 dependency edges resolve**, 0 findings |
| CG-14 | 12 install paths, 0 findings |
| CG-17 | **210 clauses routed exactly once**, 0 findings |
| CG-21 | **39 modules, contract prose states no measurement**, 0 findings |
| `verify_final_prespec.py` | **PASS** — 341 numbered clauses, 39 modules, 11 phase-rule clauses; two oversize notes, both `JUSTIFIED` |
| `build_active_manifest.py --check` | "all 7 manifests match regeneration — 7 manifests over 39 modules in 6 waves" |
| `build_contract_index.py --check` | no drift; 367 clauses, 39/39 modules carry a front-matter id |
| `build_dependency_index.py --check` | no drift; 176 `depends_on`, 8 `constrains` |
| `build_budget_report.py --check` | fixture anchors and report match regeneration |
| `build_task_router.py --check` | 12 task classes validated |

*(Note for the closure report: RD-32b recorded 29 OK / 19 WARN at `b00c3dd`; the current figure computed this session is **30 OK / 18 WARN / 0 FAIL over 48**, matching RD-32's figure at `ad82f1d`. The movement is in the instrument-validator lane at `95a41ea`, outside every Wave B byte. Quote the figure with its commit; neither is wrong.)* [Observed]

### 4.2 Wave containment — front matter

`depends_on` extracted from all 11 modules: **zero edges into RFC-0010 or RFC-0011, 11 of 11.** Every out-of-package edge names RFC 0001–0006 or an intra-wave sibling. `constrains:` appears on exactly one module (`narrative-contract.md`), intra-package plus Wave A, unchanged. [Observed]

### 4.3 Cross-wave clause tokens, classified by reading each site

Regex `RFC(\d{1,2})-(\d+)` over all 11 modules, every family tallied:

| Family | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tokens | 161 | 178 | 158 | 94 | 8 | 164 | 373 | 252 | 430 | **1** | **0** |

**`RFC11-n`: zero hits.** **`RFC10-n`: exactly one hit in the entire wave** — `RFC10-15`, `semantic-geography.md:178`. Read at the site: it sits inside RFC9-8(a)'s staged-successor parenthetical, which states in-clause *"It is named for orientation only: **a citation, not a reliance**. If RFC 0010 is never accepted, the rule above still stands and still fail-closes,"* and the operative rule stands on RFC3-15/RFC3-16(a)/RFC3-15(a) with the clause's own *"a reader holding RFC 0001–RFC 0009 can evaluate every condition this clause states."* **Classified: citation, not reliance (rule 5).** [Observed]

**Package-name tokens** `RFC[ -]00(10|11)` over the 11: 17 hits, each read — outbound "To RFC 0010/0011:" provides-to statements in RFC-0008, the RFC-0009 README's phase-boundary sibling list and its verified-true "no clause of RFC 0011 is cited anywhere in RFC 0009" (confirmed: `RFC11-\d+` = 0), and `semantic-geography.md`'s staged-successor and "No forward reliance" paragraphs. **Zero reliances on deferred-wave text.** [Observed]

**Corroboration of §7 item 9, recomputed over its own 30-module population.** The item claims "**Twelve citation hits exist**" across all 30 Waves A+B modules. My sweep for `RFC10-n`/`RFC11-n` clause tokens over 30 modules returns **exactly twelve**: RFC10-16 ×5 and RFC11-12 ×5 (the five `(Shape-parallel with …)` phase clauses in RFC-0001, RFC-0002, RFC-0003, RFC-0004, RFC-0005), RFC10-9 ×1 (RFC 0003's "the worked example"), RFC10-15 ×1 (RFC9-8(a)). **The record's figure reproduces exactly and its enumeration accounts for all twelve.** [Observed]

### 4.4 The Wave A seam, and the N-1 entry's three citations classified explicitly

**763** RFC 0001–0006 clause tokens across the wave (§2.4). The seam is **reliance by design, wholesale**, and is disclosed in three places in the record's own voice: §1 row B's solo-act sentence, the launch-scope index, and `DEFERRED-WAVE-POSTURE.md`.

The N-1 entry's three cross-wave citations, classified by reading the site (rule 5):

| Citation | Site reading | Classification |
|---|---|---|
| **RFC6-17** | The entry's normative content *is* RFC6-17's rule, quoted verbatim; the vacuity argument turns on "the exact failure RFC6-17 states the rule prevents" | **Reliance** — declared (`depends_on: RFC-0006`) |
| **RFC6-23** | The release-blocking consequence class is RFC6-23's, not the entry's own | **Reliance** — declared |
| **RFC2-24** | Supplies the definition and closure of "secondary annotation" | **Reliance** — declared (`depends_on: RFC-0002`) |

**All three are reliances, all three are declared, none escapes Waves A+B, and all three ride the disclosed wholesale seam.** No new class of reliance was created. [Observed]

**Cited-but-undeclared remainders**, tallied per namespace against each module's `depends_on ∪ constrains ∪ self`: the same two classes RD-32 and RD-32b each found independently — `RFC9-n` in three RFC-0008 modules (the m2 instance, disclosed at §7 item 18 and P-21's row) and `RFC10-15` in `semantic-geography.md` (classified above). **The remainder set is unchanged by this batch.** [Observed]

### 4.5 Ceremony phrase, self-presentation, drafted-arm sweeps

**Ceremony phrases.** Eight literal patterns (`re.escape`) × 11 modules = **88 cells, 0 hits**: `ACCEPT FOUNDATIONAL RFCS`, `ACCEPT COMPACTED FOUNDATIONAL RFCS`, `ACCEPT FOUNDATIONAL WAVE`, `CONFIRM CRAFT AMENDMENT`, `ACCEPT TOPOLOGY`, `ADOPT PROJECT OVERVIEW`, `REWORK FOUNDATIONAL WAVE`, `REJECT FOUNDATIONAL WAVE`. **Neither retired phrase nor any current one appears inside the digest subject.** Corroborated by CG-2a over its own 352-file population. [Observed]

**Self-presents-as-accepted.** Five regex families over 11 modules: the only hit is `is accepted` in `state-vocabulary-and-cost.md` §8, inside "**ANSWERED — owner decision A8:** the partitioned closure is accepted" — a statement about a vocabulary decision, not about the contract's status. **No 64-hex digest string appears in any module (0 hits over 11)** — no module quotes its own act argument. **11 of 11** carry the "Proposed foundational contract" banner, the RFC3-16 pointer, and (checked with whitespace normalisation, since the sentence wraps) "Absent such a record, this contract binds nothing." [Observed]

**Drafted-arm disclosure — enumerated population, denominator 11 modules.** Sweep for `drafted`, `awaiting.*ruling`, `the owner reverts`, `ratifies`, `proposed answer`, every hit read:

| Arm riding into the Wave B act | Site | Disclosed at | Verified |
|---|---|---|---|
| RFC7-39 entry-identity ("there are not two front doors") | `rendering-and-surface.md` 382–388, in-place P-38 marker | §7 item 15; P-38 row; launch-scope Wave B bullet | ✓ |
| RFC9-8(a) typed governance-store placement | `semantic-geography.md` 143–146, in-place P-22 marker | §7 item 17; P-22 row; launch-scope Wave B bullet | ✓ |
| RFC7-40's four-value answer domain | `rendering-and-surface.md` | §7 item 15 via P-38's packet | ✓ |
| RFC8-12 ↔ RFC9-32 undeclared reciprocal restriction | 3 RFC-0008 modules + RFC9-32 | §7 item 18; P-21 row; launch-scope Wave B bullet (new) | ✓ |
| Package §8 open questions | package indexes | §5 (27 open §8 questions, triaged) | ✓ |

Every other `drafted` hit (13 further sites, all read) is the ordinary rendering vocabulary — drafted proposals rendering as *unadopted draft*, drafted capabilities rendering unadopted — not an unruled arm. **The population is closed at five, every one cross-referenced, and the N-1/N-2 edits added none.** [Observed]

### 4.6 Collateral — every Wave B digest movement since `b00c3dd`, attributed by git

`git diff --stat b00c3dd..HEAD` over `rfcs/RFC-0007 RFC-0008 RFC-0009` returns **exactly two files**: `rfcs/RFC-0007/rendering-and-surface.md` (+5/−4) and `rfcs/RFC-0009/interaction-parity-and-release.md` (+12/−1). I then re-hashed all eleven modules against `git show b00c3dd:<path>`: **9 of 11 byte-identical, the two moved files being exactly the two claimed.** The full diff is exactly the N-1 entry and the N-2 deletion-plus-replacement, and nothing else — no front matter, no other clause, no whitespace churn elsewhere. **Every Wave B digest movement since `b00c3dd` is attributable to the RD-32b batch alone.** [Observed]

Three commits landed in that range (`a979842`, `2d27abf`, `8ef7117`, plus `95a41ea` and `18afdd4`); of them only `18afdd4` moved a Wave B byte. Wave A's manifest is unmoved at `8972d963…` across the whole range (§0). [Observed]

### 4.7 Record-level accuracy of the delta and the register

Delta **§13** records the batch: two digest-moving edits named with their module, finding id and class; four record-only repairs; N-7 carried; N-8 already closed; the four stale arguments listed; and *"The regenerated argument requires its own fresh exact-package review (**RD-32c**) before any offer — a repair session may not confirm its own repaired bytes."* **Every claim in §13 checks out against the bytes I read.** The disposition register's RD-32b section carries all eight findings with class and disposition. [Observed]

---

## 5. New findings — RD-32c

### 5.1 N-1c (MINOR, digest-moving, **deferred under rule 10**) — RFC7-37's replacement sentence is imprecise about which batch opened the gap

The N-2 repair replaced the deleted gloss with a self-referential aside, now bound in a numbered clause:

> "— as this sentence itself demonstrated: **its own enumerated gloss fell four items behind RFC6-17 across two repair batches** before being deleted (2026-08-10, RD32b-N2)."

**What the history actually shows** [Observed], traced with `git show <commit>:<path>` over every commit that touched either file:

- RFC6-17 gained **all four** missing items — `challenge-pending`, chain state, normalized work state, and the primary-reasons-only rule — in **one commit, `31ebc52`**. `rfcs/RFC-0006-…md` has not moved since; no later Wave A batch (RD-26, RD-30, RD-31) touched it.
- RFC7-37's gloss stood **byte-identical from `771965c` through `1a23d19`** — four commits, unchanged.

So the four-item gap **opened inside a single repair batch** (`31ebc52`, the wave-wide batch that extended RFC6-17 and rewrote RFC7-37's module without extending the gloss) and then **persisted across two further repair batches** (`246af62`/RD-27 and `1a23d19`/RD-32, both of which extended RFC9-43 and neither of which reached RFC7-37). The "two" is RD-32b's count of *batches that updated RFC9-43*, transposed onto a sentence about *falling behind RFC6-17* — rule 3's shape, one level down: a figure carried out of its owning artifact and re-stated about a different subject.

**Is it false?** [Inferred] **Not demonstrably.** English supports "fell behind across two batches" as an adverbial of extent — *was behind, across two repair batches* — under which the sentence is true and is exactly what RD-32b and delta §13 meant. On the tighter reading (the falling happened in two stages) it is wrong. It is **ambiguous, not false**, and the true reading is the intended one.

**Rule-10 disposition — retire the argument now, or batch?** **Batch. Do not retire.** My reasons, stated so the owner can overrule them:

1. **It binds nothing.** The obligation is "RFC6-17's full composition," cited whole; the aside is editorial history about the clause's own repair. No obligation is created, narrowed, widened, or misrouted. Contrast N-1, where a release-blocking obligation sat outside the gate registry — a defect with a defined clause (RFC9-47(a) part 1) addressing the accepting review by name. **There is no defined clause this aside violates**; I swept for one and found none, and the nearest rule (CG-21 / the knowledge-hygiene policy) is explicitly advisory and still a candidate at P-12. Under rule 8 I will not manufacture an anchor.
2. **The corpus precedent is squarely against calling it a defect.** See §5.4 — six pre-existing instances of dated review-finding provenance inside module text across Waves A+B, three of them inside Wave A clauses that **RD-31b confirmed**.
3. **The parallel gate answered the same question the same way.** RD-31b found a MINOR bound-byte characterization lag (its N-1, RFC3-2 ¶1/¶2), deferred it under its own rule-10 direction, and returned `VERDICT: CONFIRM`. Failing Wave B on a strictly smaller instance of the same class would apply two standards to one round.
4. **The countervailing risk is real and measured.** Three consecutive Wave B administrations have now each found a digest-moving defect *minted by the previous repair batch* — RD-32's B1 repair minted RD-32b's N-1; RD-32b's N-1/N-2 repair minted this. A fourth regeneration over a non-normative aside is as likely to extend that chain as to end it. §5.4 records the pattern for the closure report.

**Honest statement of the consequence**, because "batch it later" is not free: if no later pass moves a Wave B byte for a substantive reason, this sentence **rides into the act and is permanently bound** — the record's own §2 quotes RFC3-16(b) item 3, "an artifact edited after its act is, for the record, an artifact with no act." **My recommendation: let it ride, and record that decision in the disposition register so the choice is knowing rather than forgotten.** If the owner or the lead prefers precision in a bound clause over a fourth administration, the repair is one clause — replace "fell four items behind RFC6-17 across two repair batches" with "stood four items behind RFC6-17 through two later repair batches" — and my CONFIRM retires with the argument. That call is not mine to make silently, which is why it is here.

### 5.2 N-2c (MINOR, record, not digest-moving) — the disposition register's N-6 row misattributes a quotation

The register's N-6 row reads: *"The launch-scope index's Wave B bullet gains P-21(a) (ratified-or-reverted; **§7 item 18's** '*RFC-0007's twin rides the Wave B act the same way*')."*

**§7 item 18 contains no such words.** I read it in full; its Wave B sentence is *"The same open ruling covers a declared-nowhere instance inside Wave B: RFC8-12 and RFC9-32 restrict each other in-clause with no `depends_on` or `constrains` edge either way (RD32-m2 …)."* The quoted phrase lives in **P-21's row in `.syzygy/governance/decisions/PENDING-OWNER-DECISIONS.md`** (sole hit repo-wide, sweep run over all `.md`): *"the **Wave A act** — not the C2 act — is now the first act freezing the `constrains:` declaration (RFC-0005 is a Wave A module; **RFC-0007's twin rides the Wave B act the same way**)."* [Observed]

This is verification rule 8's exact class — *"a sentence attributed to RFC3-4 that exists nowhere"* — arriving in process bookkeeping rather than a contract. The repaired artifact itself (the launch-scope bullet) quotes §7 item 18 **correctly**; only the register row that describes the repair is wrong. **No digest moves. Repair: retarget the attribution to P-21's row, dated.**

### 5.3 N-3c (trivial, register completeness) — no RD-32c row exists in the delivery register

Four routed artifacts name RD-32c as the pending Wave B offer gate — record §1 row B, record §6, the P-1 row, and `PROJECT-STATUS.md`. The **delivery and verdict register**, whose preamble presents it as the fleet's roster and which gave RD-37 a `dispatched 2026-08-10` row the day before, **carries no RD-32c row at `18afdd4`.** [Observed] Harmless — it resolves when this review is stored — but recorded because the register's value is that its population is closed. **Not digest-moving.**

### 5.4 Two hypotheses I formed and killed with a denominator — recorded so a later reviewer need not re-run them

Both are the kind of finding that reads as convincing until swept. VIS-2 applies to my own claims first (rule 9), so both are stated with their denominators rather than suppressed.

**(a) "The batch minted a new idiom — review-finding provenance inside normative contract text."** I formed this from the Wave B sweep (`RD`-shaped identifiers over 11 modules: exactly 3 hits, all new — `RD32b-N2`, `RD32b-N1`, `RD-32`; zero at `b00c3dd`). **False when the denominator is widened.** Re-swept over all 30 Waves A+B modules, and over all 39 active modules: **10 hits, of which 7 pre-date this batch** — `RFC-0002/README.md:60` ("minted 2026-08-10, the RD-30 batch"), `RFC-0002/reconciliation-chain.md:225` ("identifier minted 2026-08-10, RD30-12") and `:245` ("RD-15 finding 3 found this rendering bound to no RFC2-24 reason"), `RFC-0004/execution-record.md:186` ("**[Drafted 2026-08-10 (RD26-05):**"), `RFC-0009/README.md:238` ("reviews RC-10 and RC-11"), `RFC-0009/semantic-geography.md:146` ("restoring the RC-4 contradiction"). **Dated review-finding provenance inside module text is an established corpus idiom, and three Wave A instances of it are inside the argument RD-31b confirmed.** The batch followed the convention; it did not invent one. [Observed]

**(b) "The N-2 edit broke the module's wrap discipline."** Line 313 is 97 characters. **Not anomalous:** sweeping all 11 modules for body-prose lines over 88 characters (denominator 5,160 lines) returns **4 hits, 3 of them pre-existing** (`rendering-and-surface.md:429` at 90, `state-vocabulary-and-cost.md:384` at 103, `interaction-parity-and-release.md:256` at 94). Cosmetic, within existing variance, **not a finding.** [Observed]

**(c) One pattern worth carrying to the Wave B closure report, not a finding.** Three consecutive Wave B administrations, each failing the offer on a defect the *previous* repair batch minted: RD-32's B1 repair imported an obligation and routed no gate (RD-32b's N-1); RD-32b's N-1/N-2 repair produced this administration's only bound-byte residual, which binds nothing. **RD-32c is the first Wave B administration to find no defect in an obligation.** Whether that is convergence or one more turn of the same wheel is a question the closure report should pose rather than answer — the same discipline RD-34 and RD-35 applied to the instrument's convergence claim. [Inferred]

---

## 6. What passes — stated plainly

The mechanics are, again, impeccable, and this time the substance matches them.

The argument reproduces two independent ways and matches §1 row B byte for byte; **11 of 11** module digests verify from the ceremony's documented working directory; the manifests are the generator's current output and still partition the 39-module package; the repo-wide battery is **0 FAIL over 48 checks**; clause continuity, contract index, dependency index, budget report and task router all check clean; **every module carries its candidate banner and the RFC3-16 pointer, 11 of 11**; no module claims acceptance and **no module contains a 64-hex string** — none quotes its own act argument; **88 phrase-module cells, zero ceremony phrases**; **zero declared or textual dependencies on the deferred waves**, the single `RFC10-15` token disclaimed in-clause and fail-closed on Wave A ground; the cited-but-undeclared remainder set reproduces RD-32's and RD-32b's exactly by independent computation; §7 item 9's twelve-hit figure reproduces exactly over its own 30-module denominator; and **all five drafted arms riding into this act are disclosed in the record's own voice**, each cross-reference verified.

All eight RD-32b findings are closed or correctly carried, and the two that mattered are closed **at the clause, not at the summary**. RFC9-47's release-gate list now carries the aggregation-attribution entry, stating RFC6-17's rule **in RFC6-17's own words**, with the fixture requirement and vacuity argument in the same idiom as its neighbours — and I could not construct a new obligation it fails to route, which is the test RFC9-47(a) part 1 sets for the entry itself. RFC7-37's four-items-short gloss is gone; the obligation it carried is now cited whole with no enumeration left to drift a fifth time. All six RD-32 repairs survive the edits intact, including the item-for-item RFC9-43 ↔ RFC6-17 identity that had failed three times.

And the record now says true things about itself: row B's regeneration history is accurate in all four entries, its citation figure reproduces to the digit under the method it names, and the four statements of review state that went stale the moment RD-31b returned CONFIRM were all corrected the same day, with the superseded text retained rather than deleted.

---

## 7. Answer to the commission question

**The package question and the offer question, separated.**

*Is the offer open?* **No, and that is correct and disclosed in the record's own voice.** The offer path is A → B (§1 row B; P-1). Wave A's own offer is withheld until P-33 is ruled — §7 item 11: *"**Until P-33 is ruled, this record offers no Wave A act** — performing act 1 over the current step 3 would freeze an install that breaches a clause the act binds."* P-33 is open. Nothing in this review changes that, and my verdict is not about it.

*Are these bytes offer-ready?* **Yes.** No defect in the eleven bound modules narrows, widens, misroutes or misstates any obligation. The one bound-byte residual I found (N-1c) is an ambiguity in an editorial aside that binds nothing, has no defined clause against it, follows an established corpus convention confirmed in Wave A, and is deferred under rule 10 with the consequence stated plainly above so the deferral is knowing. My two other findings (N-2c, N-3c) are record and register corrections outside the manifest; neither moves a digest and both should land in the next record-only change.

**Answer: yes — the Wave B act may be offered on argument `193e3c1e15e4b1375f938d62c9e8c1a442984313e0794ada5965d2cdf9d7e3ed`, once, and only once, Wave A's offer is live, which requires P-33 to be ruled.**

VERDICT: CONFIRM