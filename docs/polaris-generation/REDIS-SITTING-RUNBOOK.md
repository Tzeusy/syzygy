# Redis sitting runbook

**Candidate. Binds nothing.** It mints no act record, adopts nothing and is
never authority; the sitting packet (PR 260) and the acts it names decide what
binds. This page is the order of operations *after* the owner sits, with the
conflicts a dry run found and their remedies. Method and results are
[Observed] from `scripts/simulate_redis_sitting.py` run against the open heads
listed below; anything beyond that run is [Inferred] or [Unknown] and says so.

## What the dry run is

`python3 scripts/simulate_redis_sitting.py --vitest --report sim.json` clones
this repository into a scratch directory (`git clone --shared`), merges the
open heads, performs each recorder against a **synthetic** owner argument
(the manifest row digest, so a "performed" record proves only that the
recorder accepts the bytes), simulates the install change, and runs
`check_governance.py`, the review-campaign partition check and the full
Vitest suite after the steps. It compares the real tree's HEAD, status and
refs before and after and fails if any moved. Rehearse with it before the
sitting and again after any package repair round: every head below is a
moving target (rule 7: a report is valid only for the commits it names).

Heads simulated (PR, branch tip when run): 215 (`8bcec860`), 255
(`050ddcc2`), 273 (`eafb02ee`), 257 (`fbcd1dd2`), 256 (`d867a535`), 266
(`895f1622`), 260 (`930b0631`); PR 120 (`0a8ef671`) as the ordering case.

## Order of operations

Each step is one command. Step 0 is a precondition, not an act. Steps 1 to 7
follow the row order of the sitting packet.

0. **Land the candidate bytes.** Merge the PRs above into main in this order:
   266, 255 (or 273, see row 2), 215, 257, 256, 260, resolving the conflicts
   under "Merge conflicts" below. Ask PR 120's owner to rebase first.
   Rehearse: `python3 scripts/simulate_redis_sitting.py --report sim.json`
1. **Row 1, screening scope.** No recorder exists for the policy argument; the
   install is the PR 266 builder's proposed bytes over the policy file, an
   acceptance-record entry, and the re-pin supersession (finding F4).
   ```
   python3 scripts/build_public_source_screening_scope.py --check
   ```
2. **Row 2, provider route.** Exactly one of route A (PR 255) or route B
   (PR 273) is adoptable (RFC4-1: one adapter per authority per project).
   Route A:
   ```
   python3 scripts/record_public_admission_registry_entries_acts.py --record provider-route <ARGUMENT>
   ```
   Route B has no recorder (finding F7); its install is by hand.
3. **Row 3, Git source adapter.**
   ```
   python3 scripts/record_public_admission_registry_entries_acts.py --record git-source-acquisition <ARGUMENT>
   ```
4. **Row 4, requests observation.**
   ```
   python3 scripts/record_public_repo_admission_acts.py --record requests-observation <ARGUMENT>
   ```
5. **Row 5, Redis observation.**
   ```
   python3 scripts/record_public_repo_admission_acts.py --record redis-observation <ARGUMENT>
   ```
6. **Row 6, Anthropic egress.**
   ```
   python3 scripts/record_public_repo_admission_acts.py --record egress-anthropic <ARGUMENT>
   ```
7. **Row 7, RFC5-14 class.**
   ```
   python3 scripts/record_rfc5_project_documentation_act.py --record <ARGUMENT>
   ```
8. **Install change, one commit with step 7.** The registrations, exemptions,
   chain link, patch application and manifest refresh of findings F5 and F6,
   then `python3 scripts/check_governance.py`.
9. **Row 9, narrative profile.** Move the spec from `proposed/` to `specs/`
   and generalize the recount tool in the same change (finding F8), then
   `python3 scripts/count_polaris_effective_scenarios.py --check`.
10. **Verify.** `python3 scripts/check_governance.py && python3 scripts/check_docs_review_campaign_partition.py && npx vitest run`

Each recorder also takes `--date`, `--question-opening`, `--selection-label`
and `--selection-description`; `--check` with the same arguments re-verifies
the record afterwards. Row 8 (a second egress version) is not generatable
before row 7 is performed and is out of this rehearsal. Rows 10 and 11 are
rulings and directions with no bytes.

## Merge conflicts and install-change findings

| # | Where | What happens | Remedy |
|---|---|---|---|
| F1 | PENDING-OWNER-DECISIONS.md, every branch | Each branch appends a row; merges conflict pairwise | `git merge-file --union` over real temp files, then assert the row set is the distinct union |
| F2 | scripts/check_governance.py, PR 255 with 273, PR 215 | Two packages each register a phrase or copy in the same region | Keep both registrations. `--union` is unsafe for Python (it interleaved a parenthesis and gave a SyntaxError); the script's ast-validated candidate search resolved all three, then `check_governance.py --selftest` passed (386 fixtures, 0 failing) |
| F3 | PR 215 recorder, rows 4 to 6 | Every `--record` and `--check` refuses ("manifest row population differs from the builder's instance records"): `live_inputs` passes the absolute package path to the builder, which expects the cwd-relative one | Pass the relative package path to both builder calls. A latent bug in PR 215's recorder, not a frozen package byte; reported to the lead |
| F4 | Row 1 install | The new policy argument leaves six CG-7e findings (re-pin manifest, aggregate record, re-pin act record twice, PROJECT-STATUS.md, screening manifest unregistered); the re-pin builder and recorder `--check` fail | Already listed in PR 266's impact ledger: superseded-argument entries, the chain link and the status-battery edits, in the install commit |
| F5 | Rows 2 to 6 | Each performed record is an unregistered act-copy file (CG-7e) and quotes `manifest SHA-256:`, read as a stale act argument | Register the five records in ACT_DIGEST_COPY_FILES with their labels under the aggregate record; add five (record, "manifest") pairs to BARE_DIGEST_HEADING_MANIFEST_EXEMPTIONS. After both edits CG-7e fell from 12 findings to 6, the six being F4 |
| F6 | Row 7 install | Applying the RFC-0005 patch to both mirrors fails CG-7a (active-manifest row) and CG-7h (general trusted-bootstrap contract row) | Refresh the active-manifest row from the installed bytes; add a successor-chain contract link as the contract restyle act did; register the row-7 phrase in this same commit (registering it earlier fails CG-7e) |
| F7 | Rows 1 and 2 (route B) and 9 | No recorder: the policy install, route B and the profile adoption are hand-written | Per the sitting packet: byte copy and an acceptance-record entry at the sitting |
| F8 | Row 9 install | `count_polaris_effective_scenarios.py` stops with "expected exactly one base spec.md ... found 2" once a third polaris-generation spec sits under specs/ | Generalize the tool in the install change, as the package's task list says |
| F9 | PR 120 | Based on a stale main; conflicts in docs/README.md, the partition checker and check_governance.py | Rebase onto main before the sitting; not resolved by hand |

## Known limits of the rehearsal

- [Unknown] Whether the real recorders accept the owner's actual selection:
  the rehearsal feeds a synthetic one.
- [Unknown] The Vitest result after the profile install if the recount
  generalization (F8) is not written: the dry run does not write it.
- [Observed] The dry run does not exercise rows 8, 10 and 11, route B's
  install, or any provider call; it reads no external repository.
- [Inferred] F6's chain-link edit is modelled on the contract restyle act and
  was not simulated end to end; only its two failing checks were observed.
