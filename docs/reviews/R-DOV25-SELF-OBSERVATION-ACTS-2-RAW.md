# R-DOV25-2 — confirmation review of PR #120
Verdict: REVISE
Reviewed commit: 35e497bb802b65659439cea107e746df280f245a
Manifest sha256: consent 6e0e5b00f8fe43028939f16fd9f96023374e9521fffd0ea6b94b194212062cf1; registry 8b20e715226011f79375355996fe7d96fa721e6b6b5f689e4daf8e4356baa84b; policy cadce73458775e2791b432cc51ff14886c58ff92baa03324f4dff7499cf24793

- Subject: `origin/agent/tier4-dov25` at `35e497b`, parent `2f11704`, on `origin/main` `66114ac`.
- Package: `.syzygy/governance/contracts/candidates/pwb-self-observation-acts/`, `scripts/build_pwb_self_observation_acts.py`, its registration in `scripts/check_governance.py`, and the docs-partition row.
- Reviewer: fresh-context agent, read-only. I edited nothing in the main checkout or on the branch and pushed nothing. Mutations and `--apply` runs happened only in a throwaway clone under the scratchpad (`ap/`), which I reset after each run.
- Date: 2026-09-27

The three head digests were re-derived by `sha256sum` over the three manifest files at the reviewed commit. They match the values in the brief, so no correction is needed. [Observed]

## Commands run and outputs read

| Command (tree) | Output read |
|---|---|
| `build_pwb_self_observation_acts.py --check` (`35e497b`) | exit 0. "3 manifests match their 3 proposed artifacts". consent (pending) `66368ae0…`, registry (pending) `6b3d0b99…`, policy (pending) `4155733d…` |
| `sha256sum` over the manifests and `proposed/*` | consent manifest `6e0e5b00…`, registry manifest `8b20e715…`, policy manifest `cadce734…`, all as in the head. The drafted consent hashes `66368ae0…` and the drafted entry hashes `6b3d0b99…`, equal to the manifest rows and to the two arguments quoted in the packet (lines 63 and 79) |
| Independent policy digest: `git archive` of the policy into a scratch directory, `patch -p1 <` the proposed patch, then `sha256sum` | base `d148f036…`, post-patch `4155733ddad27abe471131baae98c681da2731d79851339a08ff5914700faf32`, equal to the policy manifest row [Observed] |
| `--selftest` | exit 0, "selftest: 118 predicates". I recounted the `expect`/`count` sites by hand: 11 consent, 26 registry, 21 policy (drift, corruption, no-op, invalid JSON and 17 mutants), 4 package-level, 9 manifest, 3 packet, 8 call sites and 36 adoption-order steps (6 orders × 3 acts × apply plus re-apply). Total 118 |
| `check_governance.py` | `32 OK, 20 WARN, 0 FAIL (52 checks)` |
| `check_governance.py --selftest` | `268 fixtures, 0 failing` |
| `check_docs_review_campaign_partition.py` | `total=243 assigned=243 raw=218 other=25 unmatched=0 overlaps=0`, with the new row "P-74 Q3 self-observation acts gate 1". `docs/README.md` says "54 rows … 243 files, 243 assigned", which agrees. The row cites `R-DOV25-SELF-OBSERVATION-ACTS-RAW.md:194`, and that line reads `Verdict: REVISE` [Observed] |
| `--apply` in all six orders (full clone at `35e497b`). After each act I ran builder `--check` and `check_governance.py`; at the end I re-applied consent and ran `git status --porcelain` | Every apply returned rc 0 in every order, and builder `--check` returned rc 0 after every act. Re-applying the consent was refused: "already holds the proposed bytes". `git status` listed exactly three paths: ` M` policy, `??` consent, `??` registry entry. `check_governance.py` stayed at 0 FAIL until the policy was applied and read 1 FAIL from then on (N6) [Observed] |
| Re-derivation of ledger sweep 2 with `git grep -nF '1.1.0-candidate.1'` at `6eb406d` and at HEAD, over `apps packages scripts` (denominator `git ls-tree -r` = 348 files at both) | `6eb406d`: 21 lines. Of these, 10 are policy-version lines in 4 files, 6 are observer-version lines in 4 files, and 5 are script lines in 3 files. This matches the ledger row for row. HEAD: 22 lines, because the builder now carries 3 (lines 93, 614, 673); see N3 [Observed] |
| Citations in `governance-inputs.ts` at `6eb406d` | Lines 48, 72, 76, 87–96, 89, 92, 93 and 95 all hold what the ledger says. Line 166 of `governance-inputs.test.ts` asserts the recording tag. The ledger's "line 53" is the `PWB_SUPERSEDED_ACT_RECORDS` declaration; its `policy` member is on line 54. That is trivial [Observed] |
| Sibling `proposed/` population via `git ls-tree -r` (recursive) at `3ee61c7`, `6eb406d` and HEAD | 21 sibling files in 7 packages at all three commits, all `.patch`, and none named like a target. One file is nested: `pwb-scoped-attributes-amendment/proposed/contract/RFC-0007-rendering-and-surface.md.patch` (N4) [Observed] |
| Doctrine population: `git ls-files .syzygy/governance/doctrine/` and the Markdown links in its README | 6 files. The README links to exactly the five phase-B files, once each [Observed] |
| Own rule-6 mutants (M1–M12 and C1–C4 below) | Listed under N2 and N5 |

Clauses read at source (rule 8):
- P-74 row, `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:64`. It contains "slice 6 runs only after the three acts exist, each separate and dated" and "The consent record, the registry entry and PWB-REQ-005 are edited on no arm". Both are quoted exactly in the packet and the delta ✓.
- The ruling date is 2026-09-21 (title line 1) ✓.
- Landing order: `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` §6, lines 110–118. The owner's verbatim answer is "Readiness order, lane B last (Recommended)", and the option as presented read ".21 → .30 → .22 → lane B". The packet at line 122 states only that order and places no other package ✓.
- Funnel Q3's recommended text (line 45) contains "an extension of the existing secret-classification policy to the observing project's own tree" ✓.
- Funnel line 1191 reads "No approved requirement names a self-observation" ✓.
- PWB-REQ-005 at spec lines 257–258 reads "The consent subject SHALL be exactly `(observing Syzygy project, configured Butlers repository)`" ✓.

## F1–F11 resolution

| Finding | Round-1 severity | Resolved? | Evidence |
|---|---|---|---|
| F1 — the first `--apply` blocked the other two | revise | **Resolved** | [Observed] I ran all six orders in a full clone: every act applies, `--check` passes after each, and a repeated act is refused. `target_state` treats equal bytes as adopted, and `policy_state` treats a clean reverse as adopted. The ledger's "Not changed" section is now a run (its figure of 1,552 files is the tree as of the repair, not HEAD's 1,554; see N3) |
| F2 — REQ-005 was claimed for the self pair, and there was no signed-grammar reading | revise | **Resolved** | [Observed] `SEMANTIC-DELTA.md:23-28` now says no approved requirement names the pair, and marks the analogy [Inferred]. `inheritedRules` (patch line 37) carries the reading, and `GRAMMAR_READING` is required by the builder, with a mutant covering it. Open question 10 was added |
| F3 — population not closed, scope floated | revise | **Resolved in the artifacts; the builder claim is overstated** | [Observed] The consent (lines 43–59) closes the population at six files and pins observer `1.0.0-candidate.1` and policy `1.2.0-candidate.1`. It adds "A later version of either … needs a new consent act". The policy's `phaseBPaths` and the registry's `sourcePopulation` are enforced by exact equality. However, the consent predicate checks only that six basenames are present, not that the population is closed. See **N2** |
| F4 — "never logged" was unbounded | revise | **Resolved** | [Observed] The assertion-bound sentence appears in the consent (lines 64–66), in `surfaceExposure.rule` and in `ingestBoundaryRule`. The consent's exclusions name test-runner output, snapshots and CI logs (lines 79–80). Each of the three has a mutant |
| F5 — locator unbound | note | **Resolved (routed)** | Open question 11 carries a proposal and an alternative |
| F6 — Q2 reopened, Q4 imprecise, Q9 date, missing gates | note | **Resolved** | Q2 is restated as a consequence of the ruling. Q4 says line 73 governs running the test. Q9 notes the drafting date. Q10 and Q11 were added. One trivial quote case is under N9 |
| F7 — sweep 2 missed a line; authority tuple not named | note | **Resolved** | [Observed] 10/6/5 re-derives exactly at `6eb406d`. The tuple (act identity, tag, both record paths, supersession, instant) is named with correct lines. `6eb406d` is on no remote ref, and HEAD reads 22; see N3 |
| F8 — predicates and call sites without mutants | note | **Resolved, with survivors** | [Observed] Every listed mutant exists, and the 8 sentinel call-site mutants surface through `check()`. My mutants still leave four survivors (N5) |
| F9 — Butlers discovery and implementation identities reused | note | **Resolved** | [Observed] The discovery version is `pwb-self-discovery-v1-candidate.1`, and no `implementationId`/`Version` is named. The builder compares against the Butlers entry, and both keys have mutants |
| F10 — selfReferenceRule implicit | note | **Resolved** | [Observed] The reworded rule is in the policy and mirrored in the registry, and `NO_INHERITANCE` is required in both, each with a mutant |
| F11 — composition sweep saw only patches | note | **Resolved, recursion untested** | [Observed] The glob is now `*/proposed/**/*`, and name collisions are checked with a mutant. Reverting the glob to non-recursive survives `--selftest` (N5 M1) |

## New findings

### N1 — revise — the packet and the ledger attribute to the owner words the owner did not select

Evidence:
- `OWNER-DECISION-PACKET.md:158-161`: "On 2026-09-23 the owner ruled that the change applying `.18` "retires or rebases" that check. If `.18` lands first and retires the check, nothing more is needed. If it rebases the check, act 3's adoption change must rebase the policy row the same way."
- `IMPACT-LEDGER.md:28-30` says the same: "the owner ruled that the `.18` adoption change "retires or rebases" this check".

At source, `POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md`:
- The record says (lines 17–19) that "Each answer below is the option label the owner selected, quoted byte-for-byte."
- Question 4's owner answer (verbatim, the table row near line 76) is "Retire it in the adoption change (Recommended)".
- "retires or rebases" appears only at line 90, in the recording agent's **Reading** paragraph, not in the owner's answer.

[Observed] The packet therefore quotes interpretive prose as the owner's ruling. It then builds a conditional on the "rebases" arm, which the owner did not choose. The lead's instruction and VIS-4 both require that an owner-attributed quote carry only what the owner ruled. The sentence was already present in round-1 bytes (`2f11704` packet line 142) and was not flagged then.

Fix: quote the owner's selected label "Retire it in the adoption change". If the Reading is kept, cite it as the record's reading, and drop the rebase branch, or label it as the record's reading, not a ruling.

### N2 — revise — `--check` does not verify that the consent's population is closed, but the packet and the F3 disposition say it does

Evidence:
- `consent_findings` (`scripts/build_pwb_self_observation_acts.py`, the loop over `SELF_PHASE_A + SELF_PHASE_B`) requires only that each of the six basenames appears in backticks somewhere in the consent. Nothing requires "closed", "at most six", "No other file is read" or the absence of any other path.
- The packet (`OWNER-DECISION-PACKET.md:291-292`) tells the owner that `--check` checks "that the consent, policy scope and registry entry name the same closed population".
- The F3 disposition (line 323) says "The builder requires all three to name the same six paths".

Rule 6: I called `consent_findings` directly on four mutants of the drafted consent, and every one returned `[]`:
- C1: adds "phase A also: `AGENTS.md` and every file under `apps/`".
- C2: replaces "closed population of at most six tracked files" with "population of tracked files".
- C3: replaces "No other file is read, even if the index links to it, and no further index is followed." with "Any file the index links to is read."
- C4: adds "and the working tree" to the read grant.

[Observed] The policy and the registry populations are closed by exact list equality. The consent is the one artifact whose population is the SEC-4 grant, and there the predicate is inclusion only.

[Inferred] The current consent bytes are correct, so this is not a defect in what act 1 would bind. It is a false statement to the owner about what the verification step proves, and the same gap F3 was raised to close.

Fix: either require the consent's scope section to list exactly the six paths and carry the closure sentences (with C1–C3 as mutants), or correct packet line 291-292 and the F3 disposition to say "names each of the six files".

### N3 — note — the ledger's re-derivations cite a commit no remote ref contains, and the review record omits the second rebase

Evidence:
- `IMPACT-LEDGER.md:40-54` and `:115-117` re-derive at `6eb406d`.
- The packet review record (line 313) says the repair "was made on `6eb406d`".
- `git branch -r --contains 6eb406d` prints nothing. The reviewed branch is `2f11704` → `35e497b` on `66114ac`, a second rebase that the record does not mention.
- The figures re-derive exactly at `6eb406d` (the object is present locally). At HEAD, sweep 2 is 22 lines, not 21, because the builder's own count rose from 2 to 3 lines (93, 614, 673); the apps/packages 16 lines are unchanged.
- Similarly, "1,552 files, the same as `git ls-files` here" (`:155-156`) matches the repair's tree (`6eb406d`'s 1,551 plus the raw), not HEAD's 1,554.

This is the AGENTS.md rebase-merge lesson.

Fix: name the reachable commit, or add one dated line saying the branch was rebased again onto `66114ac` and that sweep 2 reads 22 at the reviewed head, with the builder accounting for the difference.

### N4 — note — sweep 3's and sweep 4's parenthetical denominators misexplain the 20→21 change

Evidence:
- `IMPACT-LEDGER.md:117-118`: "(At `3ee61c7` the same sweep over patches alone found 20.)"
- A recursive `git ls-tree -r` at `3ee61c7` finds **21** sibling `proposed/` files in 7 packages, all patches [Observed].
- The round-1 builder found 20 because its non-recursive glob `*/proposed/*.patch` missed the nested `pwb-scoped-attributes-amendment/proposed/contract/RFC-0007-rendering-and-surface.md.patch`. The difference was not a restriction to patches, and the population did not grow.
- Sweep 3 (`:94-96`: "all 21 patch files in the 8 candidate `proposed/` directories") is the same non-recursive count; recursively there are 22 with this package's own patch.

The five spec-patching packages are unaffected, since the nested patch targets RFC-0007.

Fix: restate both denominators as recursive counts and name the nested file.

### N5 — note — four rule-6 survivors in `--selftest`

I mutated a throwaway copy of the builder, ran `--selftest`, and reset the file after each run.

| Mutant | Result |
|---|---|
| M1: composition glob `*/proposed/**/*` → `*/proposed/*` | **survives** (118 predicates, exit 0). The recursion is load-bearing: a real nested sibling patch exists (N4). Add a selftest sibling under `proposed/sub/` |
| M2: `apply()` ignores `check()` findings | **survives**. No case applies over a non-verifying package |
| M6: drop the phase-A seed `is_file()` predicate | **survives**. The only mutant for it ("about/README.md") also breaks the population-equality predicate, so the two predicates are not isolated |
| M8: drop the "names no phase-A seed" predicate | **survives**, for the same reason: the empty-list mutant also breaks population equality |
| M3 (never "adopted"), M4 (policy never reversed), M5 (no name-collision check), M7 (no patch-target check), M9 (resource-limit type), M10 (consent assertion bound), M11 (`implementationVersion`) | killed |
| M12 (inverted population equality) | killed by the initial `check()` |

[Inferred] M6 and M8 may now be redundant with population equality. If so, delete them, or isolate them. Also add one survivor case each for M1 and M2.

### N6 — note — `check_governance.py` goes red at `--apply policy`, and the packet names only the truth-policy builder

[Observed] After `--apply policy --at-adoption`, in every order, the result is `31 OK, 20 WARN, 1 FAIL`. The failure is CG-7e with 5 findings:
- this package's `SELF-OBSERVATION-POLICY-EXTENSION-MANIFEST.txt` "is not in either act-copy registry";
- the truth-policy packet and manifest, `ACCEPTANCE-ACT-RECORD.md` and `PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md` each "does not contain its current argument".

[Inferred] This is expected until act 3's record, its amendment row and the manifest's registration land in the same change. But `OWNER-DECISION-PACKET.md:152-161` lists only `build_pwb_truth_policy_amendment.py --check` as going red, and the "act 3 not registered" section (`:111-118`) does not say that the policy manifest must be registered at adoption.

Fix: one sentence naming the CG-7e state and the registration step.

### N7 — note — the packet omits the sibling ruling P-76 Q2, which bears on why three acts are needed

At source, `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md`, P-76 row:
- "Q2 an observing project reading its own tree, recorded here, needs no consent record, registry entry or act";
- "slice 3 is bounded to Syzygy's own tracked governed corpus with zero egress".

[Inferred] P-74 Q3 is the specific ruling for slice 6, so there is no conflict in authority. However, the doctrine files slice 6 would read are inside the governed corpus that M7 slice 3 reads with no act. The owner deciding Q3/Q10 should see both rulings side by side. An absence sweep (`grep -rn -F 'P-76'` over the package and the builder) returned 0 hits.

Fix: one sentence under open question 10.

### N8 — note — pinning the policy version in the consent makes every later policy act lapse the self consent, and the packet does not state that cost

Consent lines 57–59: "This consent covers those two versions only. A later version of either … needs a new consent act."

[Inferred] The policy is shared with Butlers. Any later policy act that bumps `policyVersion` for a Butlers-only reason, including the spec-pin refresh proposed as its own act in open question 8, would require a new self consent act before slice 6 runs again. This is conservative and consistent with F3, but open questions 6 and 8 cost only the registry's regeneration and not this lapse.

Fix: add the cost to Q8 or Q9.

### N9 — note — Q4's quotation is not byte-exact

`OWNER-DECISION-PACKET.md:210-211` quotes "slices 1, 3, 4, 6 (design) and 7 under the PWB implementation act". The source (P-74 row, line 64) reads "Slices 1, 3, 4, 6 (design) and 7 under the PWB implementation act as continued 2026-09-05." Only the capital letter differs, and the quote ends before the source sentence does. [Observed]

### N10 — note — the builder's state word "adopted" is derived from bytes, not from an act record

`--check` prints `consent (adopted)` as soon as `--apply` has copied the file, with no act record anywhere in the tree. I observed this in the clone.

[Inferred] This is not a VIS-4 claim in the package prose: the packet uses "adopted" only as the builder's state. But the word labels a state that only the owner's act confers. "installed" would say what the builder can know.

## VIS-4 and scope

- [Observed] Every artifact is banner-marked candidate. The consent quotes no owner statement (line 33), and a predicate plus a mutant back that.
- No act record, recorder, acceptance row or `PWB_SUCCESSOR_CHAIN` link is written. `check_governance.py` registers only acts 1 and 2, existence-gated, with selftest fixtures for 0, 1 and 2 subjects present.
- The Butlers consent, the Butlers registry entry and the PWB specification are byte-unchanged by the diff and by all three applies (`git status` in the clone).
- A sweep for "adopted|accepted|approved|in force" over the package found only provenance-state names, references to the acts in force, and the builder state (N10).
- Nothing claims adoption.

## Verdict

F1–F4 are repaired in the artifacts, and F5–F11 are resolved or routed. Two new revise findings keep this from confirming:
- N1: an owner-attributed quotation carries the recording agent's reading ("retires or rebases") in place of the owner's selected label ("Retire it in the adoption change").
- N2: the owner is told that `--check` verifies the consent's closed population, and four widening mutants of the consent pass it.

Both are small, local repairs. N3–N10 are notes.

Verdict: REVISE
