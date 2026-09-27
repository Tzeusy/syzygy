# R-DOV25-4 — confirmation review of PR #120
Verdict: REVISE
Reviewed commit: a20c2632aba484e46ee9296393af13a2f700805a
Manifest rows (act arguments, proposed-bytes sha256): consent 2901eccbc92cfcec8aaae0ec5817dd70a74d333bb3af321c81e094fc47c022e4; registry 6b3d0b9992cc4c1e6217013a62c3fc6d32e3077559895553f5234e287c423fce; policy 4155733ddad27abe471131baae98c681da2731d79851339a08ff5914700faf32

- Subject: `origin/agent/tier4-dov25` at `a20c263`, one commit on top of the round-3 reviewed commit `64746a4`. Merge-base with `origin/main`: `96ee305` (#130), which is also `origin/main`'s head.
- Package: `.syzygy/governance/contracts/candidates/pwb-self-observation-acts/` and `scripts/build_pwb_self_observation_acts.py`.
- Reviewer: fresh-context agent, read-only, detached worktree. Nothing on the branch or in the main checkout was edited, committed or pushed. Builder mutants ran as a temporary copy `scripts/_mut120c4.py`, deleted after each run (`git status --short` clean afterwards). End-to-end draft mutants ran in a `git archive` export outside the worktree.
- Head: the brief's "The raw's head" section is followed. Line 4 carries the three manifest *rows* (proposed-bytes digests), not the manifest-file digests.
- Date: 2026-09-27.

## Commands run and outputs read

| Command | Output read |
|---|---|
| `python3 scripts/check_governance.py` | `32 OK, 20 WARN, 0 FAIL (52 checks)` |
| `python3 scripts/check_governance.py --selftest` | `285 fixtures, 0 failing` |
| builder `--check` | "3 manifests match their 3 proposed artifacts"; consent `2901eccb…`, registry `6b3d0b99…`, policy `4155733d…`, all `(pending)` |
| builder `--selftest` | exit 0, `selftest: 158 predicates` |
| `scripts/check_docs_review_campaign_partition.py` | `total=251 assigned=251 raw=226 other=25 unmatched=0 overlaps=0`; row "P-74 Q3 self-observation acts gate" count 3. `R-DOV25-SELF-OBSERVATION-ACTS-3-RAW.md:193` reads `Verdict: REVISE` [Observed] |
| `cmp` scratchpad round-3 raw vs `docs/reviews/R-DOV25-SELF-OBSERVATION-ACTS-3-RAW.md` | identical (CC-REV-6) |
| Rule 3, independent digests: `sha256sum proposed/*.md proposed/*.json`; policy via `git archive` of the policy into scratch, `patch -p1 <` the proposed patch, `sha256sum`, `json.load` | consent `2901eccbc92c…22e4`, registry `6b3d0b9992cc…3fce`; policy base `d148f036…`, post-patch `4155733ddad2…faf32`, valid JSON. All three equal the manifest rows, the builder output and the packet's quoted arguments (`OWNER-DECISION-PACKET.md:66, 82`) [Observed] |
| `git diff 64746a4 HEAD --stat` | 7 files: the four package prose files, `docs/README.md`, the retained round-3 raw, the builder. No file under `proposed/` and no manifest changed, so all three act arguments are unchanged, as the drafter says [Observed] |
| Ledger figures re-derived at `a20c263` | `git ls-files apps packages scripts` 348; `git grep -nF '1.1.0-candidate.1'` 22 lines, 3 in the builder; 20 tracked files carry the PWB spec's sha256 (Python byte search over all `git ls-files`); 21 sibling `proposed/` files in 7 packages, all patches. Tracked files: 1,562 (1,561 at `64746a4`; see n9) [Observed] |

## Round-3 resolution (R1, R2, n1–n6)

| Finding | Severity | Resolved? | Evidence |
|---|---|---|---|
| R1 — "What it means" column presented as the ruling | revise | **Resolved** | [Observed] `OWNER-DECISION-PACKET.md:280-283` now reads "The record's reading of the P-74 row, in its "What it means" column and not your answer, says "The consent record, the registry entry and PWB-REQ-005 are edited on no arm"", byte-exact to the What-it-means cell at `POLARIS-PURSUIT-OWNER-RULINGS-P68-P83-DECISION.md:64`. `SEMANTIC-DELTA.md:3-9` quotes "three acts scoped to a test-only self-observation (consent record, second registry entry, secret-policy extension) before slice 6 runs", a byte-exact substring of the Ruled cell, and names "separate and dated" as the column's reading. The published regex at `OWNER-DECISION-PACKET.md:452-456` now includes `\brulings?\b`; re-run over the same 11 files it returns 52 lines at HEAD (47 before the repair per the packet; the rise is the repair's own new prose). My own sweep (below) finds no remaining site |
| R2 — `--check` coverage overclaimed; 29 widening mutants passed | revise | **Partly resolved; the new claim is again wider than the check (S1)** | [Observed] All 29 round-3 mutants are now killed: consent head and `## Scope` are compared whole (`consent_findings`, builder `:522-546`), the registry head, ordered key set and 11 values by exact value (`:467-519`), and `selfObservationScope` by exact dict equality (`:431-464`). Selftest count arithmetic 125 + 9 + 14 + 9 + 1 = 158 matches the printed count. F10's dated correction at `:383` is accurate. But the repaired claim at `:327-338` and the builder docstring at `:19-33` say *everything* about what may be read, how, and where results go is pinned, and "regenerating a manifest can never pass a widened draft". Both are false (S1) |
| n1 — occupied-target case passed for the wrong reason | note | **Resolved** | [Observed] Builder mutant B10 (`target.read_bytes() == source.read_bytes()` → `True`) is now killed: "an install target occupied by different bytes passed" |
| n2 — B15 and B20 survived | note | **Resolved** | [Observed] B15 (no-op check dropped) killed: "a no-op policy patch passed". B20 (`if not at_adoption` → `if False`) killed: "--apply installed without --at-adoption" |
| n3 — rebase onto `96ee305` unrecorded | note | **Resolved** | [Observed] `IMPACT-LEDGER.md:53-57, 121, 133-135` and `OWNER-DECISION-PACKET.md:423-431` name `96ee305` and the unreachable `35e497b`; figures re-derive (one off-by-one, n9) |
| n4 — stale delta banner | note | **Resolved** | [Observed] `SEMANTIC-DELTA.md:9-10` and `:176-183` name all three rounds |
| n5 — "not yours"; unlabelled "authorizes drafting" | note | **Resolved** | [Observed] `OWNER-DECISION-PACKET.md:221-223` quotes "took the recommended option on each with no edits", byte-exact to the rulings record lines 10-11. `:6-7` and `SEMANTIC-DELTA.md:8-9` label the drafting reading [Inferred] |
| n6 — two over-long consent lines | note | **Not changed, as dispositioned** | Inside act 1's argument; acceptable |

## Attribution and VIS-4 sweeps

- [Observed] Owner attribution (lead's check 6): Python `re`, case-insensitive, `\b(ruling|rulings|ruled|chose|chosen|decided|answer|answers|answered|you|your|selected|took|wants?|approved)\b`, over the 11 tracked files of the package plus the builder: 75 lines, all read. Every sentence presenting something as the owner's ruling, choice or answer is backed by a Ruled/answer cell: the P-74 Q3 cell (`OWNER-DECISION-PACKET.md:16-18`, `SEMANTIC-DELTA.md:4-6, 142-144`, consent `:34-38`, `:90`), the P-76 Q2 cell (`:284-285`), the `.18` Q4 answer "Retire it in the adoption change (Recommended)" (`:167-168`, `IMPACT-LEDGER.md:29-30`), and the 2026-09-23 §6 answer "Readiness order, lane B last (Recommended)" (`:130-131`). Every "What it means" quotation is attributed to the record's reading (`:19`, `:233-235`, `:280-283`; `SEMANTIC-DELTA.md:6-8, 33-35, 144-147`). "Keep act 3 to the one scope it was ruled for" (`:260`) rests on the Ruled cell's "scoped to a test-only self-observation". No remaining over-attribution.
- [Observed] VIS-4: `\b(adopted|accepted|approved|in force|performed|installed)\b`, case-insensitive, same 11 files: 64 lines, all read. Each is a reference to a performed act or act in force, a provenance-state name, a quoted "No approved requirement", a selftest fixture label, or the builder's `installed` state (defined at `:357-358` as bytes in place, never an act). No adoption, acceptance or approval is claimed for any artifact of this package.

## Rule 6 — mutants

**Builder, against `--selftest`** (16 mutants, each applied to a copy):

- Killed (15): B10 byte comparison, B15 no-op, B20 `--at-adoption`, B25 consent head comparison off, B26 consent scope comparison off, B27 registry head off, B29 pinned loop skips `selfReferenceRule`, B30 skips `surfaceExposure`, B36 skips `adoptionStatus`, B31 self-scope comparison off, B32 Butlers-in-head off, B33 quoted-owner regex off, B34 base-key loop off, B35 seed-exists off, B37 entry count `!= 1` → `< 1`.
- Survived (1): B28, `tuple(entry) != REGISTRY_ENTRY_KEYS` → `set(entry) != set(REGISTRY_ENTRY_KEYS)` (n7).

**Drafts, against the builder's own finders** (unmutated bytes return `[]` from all three). Three controls were killed as expected: a widened `## Scope` exclusion, `typedAuthority.workingTreeRead: true`, and an extra key in `selfObservationScope`. A new top-level policy scope is also killed by the base-key loop. The policy is fully pinned: the self scope by exact value, every other key by equality with the base. Survivors:

Consent (7). None falls inside the head or the `## Scope` span.
- C14: `:98` "That state authorizes only this read-only, test-only observation" → "authorizes any observation of this repository".
- C15: `:93` "a body read under this pair requires all three to be valid" → "requires only this record to be valid".
- C16: a sentence inserted directly under `## Provenance state and effect`: "The consent also covers every tracked file under `apps/`, and results may be served on /polaris."
- C17: an appended `## Addendum` section: "This consent also covers the working tree and may be logged."
- C18: `:38-39` "That answer asks for this record; it does not grant it." → "That answer is itself the grant."
- C19: `:33-34` replaced with an unquoted "The owner said: I consent to every read of this repository." The quoted-owner check matches only `^>` lines.
- C21: `:99` "is never "independently verified"" → "may be shown as "independently verified"".

Registry entry (11). All sit in fields outside the 11 pinned values.
- R12: `observationGrammar.sourcePopulation.rule` "closed: at most these six files; … no other path is read even if linked" → "open: these six files and every file they link to, recursively, at any revision". Only the `phaseA`/`phaseB` arrays are compared.
- R13: `authorizationModeDerivation` ("… every other combination rejects before body reads") → "any single valid act suffices; every other combination proceeds under owner-trusted-bootstrap".
- R14: `resourceLimitSemantics.breachResult` → "a truncated model is emitted and may be served and logged".
- R15: `resourceLimitSemantics.maxBytesPerSource` → "advisory only; oversized blobs are passed to the extractor". Only key presence is checked.
- R16: `subject` gains `additionalObservedRepositories: ["repository:butlers-configured-poc"]`. Only two subject fields are compared.
- R17: every `secret-*` entry removed from `parsePassIdentities`.
- R18: `failureStates.consentWithdrawn` → `{"degradationState": "Fresh", "unknownReason": null}`.
- R19: `admissionFailureMapping` emptied.
- R20: `observationGrammar.fixedCatalogKeys` → `["*"]`.
- R21: `sourcePopulation` gains `extraPhaseB: ["apps/**"]`.
- R23: `governingBehaviorContract.signedBy` → "no act needed".

**End to end.** In a `git archive` export of `a20c263` I applied R12 to the registry draft and C17 to the consent draft. I ran `--write`, then replaced the two quoted digests in the packet, as the packet's landing order instructs ("update the digest quoted above"). `--check` then printed "3 manifests match their 3 proposed artifacts" and exited 0, with consent `baf66f52…` and registry `5344f09a…` [Observed].

## New findings

### S1 — revise — the repaired `--check` claim is still wider than the check: widened drafts regenerate and pass

The claim, in two places:
- `OWNER-DECISION-PACKET.md:327-339` tells the owner that "everything each draft says about what may be read, how, and where the result may go is exactly the text the builder pins … The pins live in the builder, so regenerating a manifest can never pass a widened draft".
- The builder docstring (`scripts/build_pwb_self_observation_acts.py:19-33`) repeats it: "`--check` compares, by exact value, everything each draft says about what may be read, how, and where the result may go … `--write` can never regenerate a manifest over a widened draft".

[Observed] 18 widening mutants pass the builder's finders (consent C14–C19, C21; registry R12–R21, R23). The end-to-end run above shows a draft whose `sourcePopulation.rule` opens the population recursively "at any revision", and whose consent gains a section covering the working tree and logging. That draft regenerates with `--write` and passes `--check`.

Several survivors are statements about exactly what the claim covers:
- what may be read: C14, C15, C16, R12, R16, R21;
- how reads are authorized: R13, C18;
- where results may go: C16, C17, R14.

The pinned set is well chosen and complete for the policy, so this is a narrower residue than round 3's R2. But the sentence the owner is given is false, which is the class R2 and round-2 N2 were raised for. That, and brief criterion 9's "Can any widening of a draft still pass it?", make this a revise finding.

[Inferred] It does not affect what any act binds: each act binds reviewed bytes by digest, and the current bytes are correct.

Fix, either of:
- (a) Narrow `:327-339` and the docstring to the sections and keys actually pinned, and drop "can never pass a widened draft".
- (b) Pin the rest:
  - the consent's whole text from `## Where the grant comes from` to the end, or the entire consent file;
  - the registry's `subject` as an exact dict, `observationGrammar` whole, and `authorizationModeDerivation`, `resourceLimitSemantics`, `parsePassIdentities`, `admissionFailureMapping` and `failureStates` by exact value (or the whole entry apart from the regenerated `governingBehaviorContract.version`);
  - add C14–C21 and R12–R23 as selftest cases.

Option (b) changes no act argument. Pinning the whole consent file is the simplest form, since act 1's argument is already that file's digest.

### n7 — note — the registry key-order predicate has no mutant

B28 (order-insensitive key comparison) survives `--selftest` at 158. The finding text at `scripts/build_pwb_self_observation_acts.py:481-482` says "in order". No selftest case reorders keys while keeping the set, so the "in order" half is untested (brief criterion 6). Add a case that swaps two entry keys.

### n8 — note — the docs README row misnames the round-3 R1 column

`docs/README.md:97` summarizes round-3 R1 as "two sentences still presenting the P-74 answer column as the ruling". R1 was about the "What it means" column. The answer column *is* the ruling. The packet's own summary at `OWNER-DECISION-PACKET.md:436` states it correctly. Reword the row to "the P-74 'What it means' column".

### n9 — note — "1,561 tracked files" is the pre-repair population

`OWNER-DECISION-PACKET.md:425-430` says the figures were "re-derived at the round-3 repair (… 1,561 tracked files)". `git ls-tree -r --name-only 64746a4 | wc -l` gives 1,561, but `git ls-files | wc -l` at `a20c263` gives 1,562. The repair commit added the retained round-3 raw. The other figures in that sentence (22 lines over 348 files, 21 siblings in 7 packages, 20 spec-digest citers) re-derive unchanged at `a20c263`. State the commit the 1,561 was counted at, or recount.

## Verdict

R1 and the notes n1–n5 are repaired as their dispositions say. n6 is left alone, as dispositioned. All three act arguments are unchanged and re-derive independently. All four check commands are green, and no over-attribution or adoption claim remains.

R2 is repaired for all 29 round-3 mutants. The repair's new claim, though, says `--check` pins *everything* each draft says about reads, authorization and result destinations, and that regeneration "can never pass a widened draft". 18 further widening mutants pass, and one widened draft passes `--check` end to end (S1, revise). S1 is builder-and-prose only and changes no act argument.

The three notes, n7–n9, need no further round.

Verdict: REVISE
