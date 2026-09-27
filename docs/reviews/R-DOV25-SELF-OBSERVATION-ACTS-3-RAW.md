# R-DOV25-3 — confirmation review of PR #120
Verdict: REVISE
Reviewed commit: 64746a410765529aec964a41914bdddc4fab3728
Manifest rows (act arguments, proposed-bytes sha256): consent 2901eccbc92cfcec8aaae0ec5817dd70a74d333bb3af321c81e094fc47c022e4; registry 6b3d0b9992cc4c1e6217013a62c3fc6d32e3077559895553f5234e287c423fce; policy 4155733ddad27abe471131baae98c681da2731d79851339a08ff5914700faf32

- Subject: `origin/agent/tier4-dov25` at `64746a4`. Its merge-base with `origin/main` is `96ee305` (#130).
- Package under review: `.syzygy/governance/contracts/candidates/pwb-self-observation-acts/` and `scripts/build_pwb_self_observation_acts.py`. I also read the package's registration in `scripts/check_governance.py` and the docs-partition row.
- Reviewer: a fresh-context agent working read-only in a detached worktree. I did not edit, commit or push anything on the branch or in the main checkout. Builder mutants ran as a temporary copy, `scripts/_mut120c3.py`, which was deleted after each run.
- Date: 2026-09-27.

**Head line 4.** `REVIEW-BRIEF.md` states no head contract for the raw; it has no sentence naming which digest line 4 carries. Following the lead's instruction, line 4 carries the act arguments: each manifest's row digest, which is the digest of the proposed bytes. It does not carry the hashes of the manifest files. For reference, the manifest files hash as follows:
- consent `05384b9d…`, which changed since round 2 because act 1's argument changed;
- registry `8b20e715…`, unchanged;
- policy `cadce734…`, unchanged.

## Commands run and outputs read

| Command | Output read |
|---|---|
| `python3 scripts/check_governance.py` | `32 OK, 20 WARN, 0 FAIL (52 checks)` |
| `python3 scripts/check_governance.py --selftest` | `285 fixtures, 0 failing` |
| builder `--check` | Prints "3 manifests match their 3 proposed artifacts". All three acts show as `pending`: consent `2901eccb…`, registry `6b3d0b99…`, policy `4155733d…` |
| builder `--selftest` | exit 0, `selftest: 125 predicates` |
| `scripts/check_docs_review_campaign_partition.py` | `total=250 assigned=250 raw=225 other=25 unmatched=0 overlaps=0`. The row "P-74 Q3 self-observation acts gate 2" is present. The README row cites `R-DOV25-SELF-OBSERVATION-ACTS-2-RAW.md:185`, and that line reads `Verdict: REVISE` [Observed] |
| Independent digests (rule 3): `sha256sum` over `proposed/*.md` and `proposed/*.json`. For the policy, `git archive` of the policy into a scratch directory, `patch -p1 <` the proposed patch, then `sha256sum` and `json.load` | consent `2901eccbc92c…22e4` and registry `6b3d0b9992cc…3fce`. Policy base `d148f036…`, post-patch `4155733ddad2…faf32`, valid JSON. All three equal the manifest rows and the builder's output. The packet quotes the consent argument at line 65 and the registry argument in its act-2 block [Observed] |
| `cmp` of the scratchpad round-2 raw against `docs/reviews/R-DOV25-SELF-OBSERVATION-ACTS-2-RAW.md` | identical (CC-REV-6) |
| Sweep 2 re-run: `git grep -nF '1.1.0-candidate.1' <c> -- apps packages scripts` at `6eb406d`, `35e497b` and `HEAD` | 348 files at each commit. `6eb406d`: 21 lines. `35e497b`: 22. HEAD: 22, with the builder carrying 3. This matches the ledger's corrected text [Observed] |
| Sweep 3 re-run: every tracked file containing the PWB spec's current sha256, computed two ways (`xargs grep -lF` and Python byte search over all 1,561 `git ls-files`) | 20 by both methods. That is the ledger's 19 plus the drafted self entry, and the breakdown matches: 7 evidence files, 2 raws, `GOVERNING-DEPENDENCIES.md` plus 5 patches, 1 manifest, 1 act record, the Butlers entry, the policy and the self entry [Observed] |
| Sweeps 3 and 4: `git ls-tree -r` under `*/proposed/`, and the `+++ b/` targets of every patch | HEAD has 24 files in 8 packages. 21 are siblings in 7 packages, all patches, one of them nested (`pwb-scoped-attributes-amendment/proposed/contract/RFC-0007-rendering-and-surface.md.patch`). With this package's own patch there are 22 patches. 5 packages patch the PWB spec, and `polaris-edit-repair-deletion-scenario` patches a different spec. None targets the policy or either install path, and none shares a target's name [Observed] |

## Round-2 resolution (N1–N10)

| Finding | Severity | Resolved? | Evidence |
|---|---|---|---|
| N1 — "retires or rebases" quoted as the owner's ruling | revise | **Resolved at the named sites. The sweep claimed with the repair is incomplete (see R1)** | [Observed] `IMPACT-LEDGER.md:28-32` and `OWNER-DECISION-PACKET.md:165-172` quote "Retire it in the adoption change (Recommended)". That is byte-exact to the answer cell at `POLARIS-GATE-PACKAGE-OPEN-QUESTIONS-2026-09-23-DECISION.md:75`, and lines 16-18 of that record say the answers are the owner's selected labels. The rebase branch is gone, and the act-3 carry-over is labelled a proposal [Inferred]. The packet's opening (`:15-19`), `SEMANTIC-DELTA.md:29-31, 137-143`, and consent `:34-39` now separate the answer cell from the "What it means" column. Two sites the repair's own sweep should have found remain (R1) |
| N2 — the consent's closed population was not enforced | revise | **Resolved as scoped** | [Observed] `consent_findings` compares the grant paragraph, from `## Scope` up to "The reads are selected", whole and whitespace-normalized against `CONSENT_GRANT`. The round-2 mutants C1–C4 are selftest cases, and each one fails. A builder mutant that disables the comparison (B1) is killed. The packet's `--check` bullet at `:324-326` now describes exactly this. The rest of the consent's scope section is still unchecked, and so is another packet bullet (R2) |
| N3 — `6eb406d` unreachable; 22 lines at head | note | **Resolved; the same drift has recurred** | [Observed] The ledger at `:49-53` and the packet at `:350-353, 372-374` name both earlier rebases, and 22 lines re-derives at HEAD. The branch has since been rebased onto `96ee305` (#130). No package file mentions that base. `35e497b`, the round-2 reviewed commit, is now also contained in no remote ref (`git branch -r --contains` prints nothing). The figures still re-derive at `64746a4` (n3) |
| N4 — sweep 3 and 4 denominators | note | **Resolved** | [Observed] 22 patches in 8 packages, 21 siblings in 7, and the nested file named. All re-derived above |
| N5 — M1, M2, M6, M8 survived | note | **Resolved** | [Observed] My builder mutants are all killed: B2 (non-recursive glob), B3 (`apply` ignores `check`) and B4 (seed `is_file` dropped). The "names no phase-A seed" predicate is gone. Count: 118 + 4 consent cases + nested sibling + apply-over-non-verifying + absent seed = 125, which matches the printed count |
| N6 — `check_governance` red at `--apply policy` | note | **Resolved** | `OWNER-DECISION-PACKET.md:173-179` names CG-7e and its 5 findings, and `:122-125` names the same-commit registration. I did not re-run `--apply` in this round |
| N7 — P-76 Q2 missing | note | **Resolved** | [Observed] `:278-280` quotes "an observing project reading its own tree, recorded here, needs no consent record, registry entry or act". That is byte-exact to the P-76 Ruled cell (`POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:62`). The no-conflict reading is labelled [Inferred] |
| N8 — cost of the policy-version pin | note | **Resolved** | Stated in Q8 at `:258-262` [Inferred label present] |
| N9 — Q4 quote not byte-exact | note | **Resolved** | [Observed] `:231-233` matches the P-74 "What it means" cell exactly, capital included, to the end of the sentence. It is attributed to the row's reading, not to the owner |
| N10 — "adopted" state word | note | **Resolved** | [Observed] The builder's states are `pending` and `installed`. `--check` prints `(pending)`. The packet's `:340-341` says only the owner's act performs an act |

The drafter's other claimed repairs:
- The landing order quotes "Readiness order, lane B last (Recommended)" at `:129-132`. That is byte-exact to `POLARIS-GATE-PACKAGE-OWNER-VALUES-2026-09-23-DECISION.md` §6 (line 110 area). The presented order is attributed as "an option presented as" ✓.
- Q2 quotes "secret-policy extension" at `:216`, a fragment of the P-74 Ruled cell ✓. See n5 for the sentence after it.
- Act 1's argument changed from `66368ae0…` to `2901eccb…`. The consent diff is confined to "Where the grant comes from" and one word at line 90 ✓. The registry and policy arguments are unchanged ✓.
- The rebase onto #130 did not break the gate: `check_governance` shows 0 FAIL and CG-7e passes.

## New findings

### R1 — revise — two sentences still present the P-74 "What it means" column as the owner's ruling, and the repair's attribution sweep could not see them

Evidence, with the source row being `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:64`, P-74:
- The Ruled cell for question 3 reads: "Q3 three acts scoped to a test-only self-observation (consent record, second registry entry, secret-policy extension) before slice 6 runs".
- The "What it means" cell carries "slice 6 runs only after the three acts exist, each separate and dated" and "The consent record, the registry entry and PWB-REQ-005 are edited on no arm".

The two sites:
1. `OWNER-DECISION-PACKET.md:276-278` reads "The ruling forbids editing PWB-REQ-005." That is the "What it means" cell presented as the ruling. `SEMANTIC-DELTA.md:29-31`, repaired in this same round, correctly says of the same sentence: "The record's reading of the P-74 row, in its 'What it means' column and not the owner's answer, says …". The two files now contradict each other.
2. `SEMANTIC-DELTA.md:3-5` (the head banner) reads: "the owner's 2026-09-21 ruling on P-74 question 3, which asks for three separate, dated owner acts". "separate, dated" is the "What it means" wording. The N1 disposition at `OWNER-DECISION-PACKET.md:381` says the consent's "separate, dated" was repaired for exactly this reason, but the delta's banner keeps it.

[Observed] Why the sweep missed them. The attribution sweep stated at `:392-398` uses the verb set `\b(ruled?|rules|chose|chosen|decided|answer(ed)?|set|[Rr]eading)\b`:
- "ruling" matches none of these (`ruled?` covers "rule" and "ruled"), and neither do "forbids" or "asks".
- Both sites are "The ruling / the ruling … forbids / asks" sentences.
- My own sweep (Python `re`, case-insensitive) paired a wider verb set that includes "ruling", "asks", "requires" and "says" with an owner/you/P-7x/ruling token. It returned 39 lines over 7 files, and I read all 39. These are the only two that attribute a "What it means" clause to the ruling.

This is the class N1 was raised for (VIS-4; the lead's check 6).

[Inferred] Neither site is in an act-bound file, so repairing them changes no argument.

Fix:
- Reword both sites to the pattern `SEMANTIC-DELTA.md:29-31` already uses.
- Widen the sweep's predicate to include the noun "ruling" and any verb, publish the regex, and re-run it.

### R2 — revise — the packet says `--check` verifies that "the drafted files and the patched policy say what this packet says", and 29 widening mutants of the three drafts pass it

`OWNER-DECISION-PACKET.md:323` tells the owner the first thing `--check` checks is "that the drafted files and the patched policy say what this packet says". The packet says the use is test-only and never served, and brief criterion 1 asks that "nothing observed can reach a route, cache, log, stored evaluation or walkthrough record". Criterion 3 asks about `selfReferenceRule`.

Rule 6: I called the builder's own predicates (`consent_findings`, `policy_findings`, `registry_findings`) on mutants of the proposed bytes. The unmutated bytes return `[]`. Every mutant below also returned `[]`, so each survives.

Consent, 9 mutants, all outside the paragraph N2's check covers:
- C5: delete the "the working tree, untracked or ignored files, …" exclusion.
- C6: append "The consent also covers every tracked file under `apps/`." after the version-pin sentence.
- C7: "they are never served, cached, logged, written to disk…" becomes "they may be served and cached."
- C8: "Purpose: test-only." becomes "Purpose: production."
- C9: delete the code-execution and egress exclusion.
- C10: widen the locator to "any remote clone of it fetched at test time".
- C11: the Butlers exclusion becomes "any repository other than this one or the Butlers repository".
- C12: delete "any write to this repository".
- C13: the revocation state becomes "irrevocable; supersedes the Butlers consent".

Policy `selfObservationScope`, 9 mutants:
- P1: add `detectors: []`.
- P2: add authorization mode `agent-asserted`.
- P3: `ingestBoundaries: []`.
- P4: purpose becomes "production: rendered and served on /polaris".
- P5: drop "every detector," from `inheritedRules`.
- P6: `selfReferenceRule` reduced to "authority is never inherited from another pair". This deletes the "no object read as an observed Git blob … is an authority input" half.
- P7: `derivedSeedRule` becomes "phase B reads every file the seed links to".
- P8: `ingestBoundaryRule` becomes "may be served and cached; " plus the assertion-bound sentence.
- P9: remove `authorizationModes`.

Registry entry, 11 mutants:
- R1: `typedAuthority.readAuthority` becomes "any repository and the working tree".
- R2: purpose "production; serves /polaris".
- R3: authorization mode `agent-asserted`.
- R4: `selfReferenceRule` gutted as in P6.
- R5: `maxSources` × 1000.
- R6: `adoptionStatus: "adopted"`.
- R7: `implementation` names a file.
- R8: an `http-fetch` input class.
- R9: `surfaceExposure.diskWrite: true`.
- R10: `typedAuthority.processEnvironmentRead: true`.
- R11: remove `provenanceDisclosure`.

[Observed] The predicates test phrase presence and a few exact keys. They do not test what each artifact says as a whole.

Two dispositions overclaim in the same way:
- F10 at `:369` says "A builder predicate requires it in both". It requires only the `NO_INHERITANCE` fragment, and P6/R4 remove the half brief question 3 is about.
- N2 was raised in round 2 as a revise finding for the same class of claim: a false statement to the owner about what the verification step proves.

[Inferred] What each act binds is unaffected. The current bytes are correct, and each act binds a digest of reviewed bytes. The defect is the stated coverage. `--write` regenerates manifests without running `check()`, so a widened draft would get a fresh, consistent manifest, and `--check` would then pass it.

Fix, either of:
- (a) Narrow `:323` to list what is actually checked, and correct the F10 disposition.
- (b) Extend the exact-text comparison to the consent's whole `## Scope` section (grant, surface sentence and exclusions) and its `Purpose:` line. Pin `selfObservationScope` and the registry's `purpose`, `typedAuthority`, `surfaceExposure`, `authorizationModes` and `selfReferenceRule` by exact value or closed key set. Add these mutants as selftest cases.

Option (b) changes no act argument.

### n1 — note — the "occupied install target" selftest case passes for the wrong reason, and the byte comparison it names is untested

Builder mutant B10 replaces `target.read_bytes() == source.read_bytes()` in `target_state` with `True`. It **survives** `--selftest` (125, exit 0).

The fixture at `scripts/build_pwb_self_observation_acts.py:787-794` writes the target in an empty temporary root that has no `proposed/`. So `source.is_file()` is false and the `ValueError` comes from the missing source, not from differing bytes.

Under B10, a real tree whose install target held different bytes would report `installed`, `--check` would pass, and `--apply` would refuse as a "repeat". The package's own "occupied … anything else would be overwritten" guarantee (docstring `:392-393`) would silently read as success.

Fix: build the fixture in a `scratch_root` copy so that the source exists.

### n2 — note — two more builder survivors

- B15: dropping the `proposed == current` no-op check in `policy_findings` survives. The "a no-op policy patch" case (`:728`) is also caught by the unbumped-`policyVersion` predicate, so the two predicates are not isolated. The same pattern as round 2's M6/M8.
- B20: dropping the `--at-adoption` guard in `apply()` survives, because the selftest always passes `True`.

Of my 24 builder mutants, the other 21 were killed: B1–B9, B11–B14, B16–B19 and B21–B24. That set includes the grant check, the collision checks, the manifest exact-regeneration check, the stale packet digest, the policy offer, repeat-apply refusal, the spec digest and the quoted-owner regex.

### n3 — note — the rebase onto `96ee305` (#130) is not recorded, and `35e497b` is now unreachable

The package names bases `66114ac` and `08d4d02` (`IMPACT-LEDGER.md:50, 117, 129`; `OWNER-DECISION-PACKET.md:374`). HEAD's merge-base is `96ee305`.

The round-2 reviewed commit `35e497b` is on no remote ref, and neither are the round-2 repair commits as originally made. Every figure I checked re-derives at `64746a4`: 22 lines, 348 files, 21 siblings in 7 packages, and 20 spec-digest citers. So this is provenance, not a wrong number.

This is the AGENTS.md rebase-merge lesson; cite the surface or current head rather than a base that moves.

### n4 — note — the `SEMANTIC-DELTA.md` banner is stale

`:5-7` reads "Round 1 of review returned REVISE; these bytes are the repair and are not yet reviewed". Round 2 also returned REVISE, and these bytes are the round-2 repair. `REVIEW-BRIEF.md` and the packet already say so.

### n5 — note — the packet disowns wording the owner selected

`OWNER-DECISION-PACKET.md:216-221` says the funnel's "an extension of the existing secret-classification policy to the observing project's own tree" is "the funnel's, not yours". But the rulings record says, at lines 10-11, "the owner took the recommended option on each with no edits", and, at 12-13, "Where this file and the owner's own words differ, the words win". The recommended option the owner selected is the funnel's Q3 text (`docs/design/POLARIS-M8-PORTABILITY-FUNNEL.md`, Q3 Recommended cell). The Ruled cell is the recorder's compression of that selection.

This under-attributes rather than over-attributes, so it is not a VIS-4 breach, but "not yours" is inaccurate. Suggested wording: "the option you selected, as the funnel worded it".

Separately, `:6` and `SEMANTIC-DELTA.md:4-5` say the ruling "authorizes drafting and nothing more". Neither P-74 cell mentions drafting. That is the drafter's reading and is unlabelled; mark it [Inferred].

### n6 — note — cosmetic: two consent lines run past the wrap

`proposed/SYZYGY-SELF-PROJECT-SHAPE-OBSERVATION-CONSENT.md:36` is 81 columns and `:39` is 113. They are inside act 1's argument, so fix them only together with a substantive change.

## VIS-4 and scope

- [Observed] A Python `re` sweep for `adopted|accepted|approved|in force|performed|installed` over all 10 package files returned 39 lines, and I read all 39. Every hit is one of these, and none claims adoption or acceptance:
  - a reference to a performed act or an act in force;
  - a provenance-state name;
  - a quoted requirement ("No approved requirement…");
  - the builder's `installed` state, defined at `:340-341`.
- Every artifact is banner-marked candidate. The consent `Status:` line is candidate, and a predicate with a mutant backs it. The registry entry's `adoptionStatus` is `candidate-unadopted`, but no predicate backs it (R2, R6).
- `check_governance.py` registers acts 1 and 2 only, existence-gated. Act 3 and any `PWB_SUCCESSOR_CHAIN` link are deliberately absent. No act record, recorder or acceptance row is written.

## Verdict

N1–N10 are repaired as their dispositions say, apart from the incomplete attribution sweep. Every manifest row re-derives independently, and all four check commands are green.

Two revise findings remain, both prose-only or builder-only. Neither changes an act argument.
- **R1:** two sentences still present the P-74 "What it means" column as the owner's ruling. One of them contradicts the delta's own repaired sentence, and the stated sweep's regex cannot match "ruling".
- **R2:** the packet tells the owner that `--check` verifies the drafts "say what this packet says", and 29 widening mutants pass.

The six notes, n1–n6, need no further round.

Verdict: REVISE
