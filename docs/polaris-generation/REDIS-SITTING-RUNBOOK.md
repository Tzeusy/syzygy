# Redis sitting runbook

**Candidate. Binds nothing.** It mints no act record, adopts nothing and is
never authority; the sitting packet (PR 260) and the acts it names decide what
binds. This page is the order of operations *after* the owner sits. Method and
results are [Observed] from `scripts/simulate_redis_sitting.py` run against the
heads listed below; anything beyond that run is [Inferred] or [Unknown] and
says so.

## What the dry run is

`python3 scripts/simulate_redis_sitting.py --vitest --report sim.json` clones
this repository into a scratch directory (`git clone --shared`), merges the
open heads, performs every recorder against a **synthetic** owner argument
(the manifest row digest, so a "performed" record proves only that the
recorder accepts the bytes), runs `scripts/install_redis_sitting.py` (twice,
then `--check`), checks the Butlers read gate around it, and then requires the end state to be green: `check_governance.py`
at 0 FAIL, the review-campaign partition passing and the full Vitest suite with
no failure beyond the start-of-run baseline. `--route a` takes the Agent SDK
provider route instead of the Messages API route (the default, `--route b`).
It compares the real tree's HEAD, status and refs before and after and fails
if HEAD or the status moved. Rehearse with it before the sitting and again
after any package repair round: every head below is a moving target (rule 7: a
report is valid only for the commits it names).

[Observed] The last full run (`--route b --vitest`) ended green: baseline
31 OK / 0 FAIL, after the recorders 29 OK / 2 FAIL (CG-7e 12, CG-1b 1), after
the install 31 OK / 0 FAIL; partition 343 of 343 assigned, 0 unmatched; Vitest
had no failure that persisted on a one-file rerun (28 cases failed in the
full suite at the start on a machine with load average above 60, all passed
alone; F16); before the install the gate's loader test refused the new policy
(5 failing, the real-tree case among them) and after it passed. Heads simulated (PR, branch tip): main `cf57e77c`, 278 (`597928be`), 273
(`3656a103`), 260 (`05e59fcf`); PR 120 (`0a8ef671`) as the ordering case.
Already in main: 215, 255, 256, 257, 266, 284, 288, 290.

## Order of operations

Step 0 is a precondition, not an act. Steps 1 to 8 follow the row order of the
sitting packet; each is one command. Every recorder takes `--date`,
`--question-opening`, `--selection-label` and `--selection-description`, and
`--instant` (UTC `YYYY-MM-DDTHH:MM:SSZ` on the act's date, default now). Give
the instants in increasing order across the acts that join the contract
successor chain (the RFC5-14 act orders by its instant). `--check` with the
same arguments re-verifies a record afterwards.

0. **Land the candidate bytes.** Merge, in this order: 278 (its closed
   exclusion-reason set is the precondition of the row-1 recorder; finding
   F13), 273 if route B is the choice, 260; resolve the conflicts
   under "Merge conflicts" below. Ask PR 120's owner to rebase first.
   Rehearse: `python3 scripts/simulate_redis_sitting.py --vitest --report sim.json`
1. **Row 1, screening scope.**
   `python3 scripts/record_public_source_screening_scope_act.py --record <ARGUMENT> ...`
   writes the record, the aggregate block and applies the policy patch.
2. **Row 2, provider route.** Exactly one of route A (PR 255) or route B
   (PR 273) is adoptable (RFC4-1). Route A:
   `python3 scripts/record_public_admission_registry_entries_acts.py --record provider-route <ARGUMENT> ...`
   Route B:
   `python3 scripts/record_messages_api_route_registry_act.py --record <ARGUMENT> ...`
   (finding F7). The route-B recorder refuses until its package has a
   confirming review and `FROZEN_SUBJECT` is set from that commit, and refuses
   while route A's entry sits in the installed home.
3. **Row 3, Git source adapter.**
   `python3 scripts/record_public_admission_registry_entries_acts.py --record git-source-acquisition <ARGUMENT> ...`
4. **Row 4, requests observation.**
   `python3 scripts/record_public_repo_admission_acts.py --record requests-observation <ARGUMENT> ...`
5. **Row 5, Redis observation.** Same recorder, key `redis-observation`.
6. **Row 6, Anthropic egress.** Same recorder, key `egress-anthropic`.
7. **Row 7, RFC5-14 class.**
   `python3 scripts/record_rfc5_project_documentation_act.py --record <ARGUMENT> ...`
   (PR 290, merged; finding F12).
8. **Row 8, egress v2** (PR 299, a draft waiting on the stage list; after
   row 7). The instance is generated with
   ```
   python3 scripts/build_public_egress_v2.py --write
   ```
   Its recorder is pending: until it lands row 8 is not rehearsed and the
   install does not cover it.
9. **Row 9, narrative profile.**
   `python3 scripts/record_narrative_profile_adoption.py --record ...`
   (finding F7; no `ARGUMENT`, the adoption binds no digest). Between this
   step and the next, CG-1b reports one dangling path: the record cites the
   specification at its installed location.
   Before the install, `npx vitest run apps/three-surface-poc/src/governance-inputs.test.ts`
   is expected to fail on the real-tree case: the gate still pins the old
   policy digest and version and refuses the new bytes (packet Q2). After the
   install it passes. The simulator asserts both.
10. **Install, one commit with every record.**
   `python3 scripts/install_redis_sitting.py`. It refuses (exit 2, tree
   restored) unless every required record exists, is idempotent, and
   `--check` reports what is not installed. Needs PR 278 merged first (F13). Steps, with the findings each answers:
   - **registrations** (F5): the performed records become act-copy files; the
     `manifest SHA-256:` heading is a checked exemption.
   - **rfc5** (F6): the patch applies to both mirrors; the active-manifest row
     and the directive register are regenerated; the amendment becomes a
     row-argument contract chain link.
   - **policy** (F4, F10): the screening-scope act becomes the policy's chain
     link and the 2026-10-02 re-pin turns to history; the read gate's pins,
     the tests that assert them, the status battery lines and the workflow
     steps follow.
   - **profile** (F8, F11): the specification moves from `proposed/` to
     `specs/`; package prose naming the old path is rewritten; the status
     figure follows the recount tool (both figures, once the dossier
     local-agent addition is signed off), and its lead-in names the profile
     and its adoption record; the `openspec/README.md` row names the record
     and the table's lead paragraph says so.
   - **reconcile** (PR 365): the profile is now a Polaris addition, adopted by
     the record `check_spec_reconciliation.py` declares for it, so
     `check_spec_reconciliation.py --regenerate` rewrites `census.json` and
     the change's generated `GOVERNING-DEPENDENCIES.md`. The reconciliation
     record beside `census.json`
     (`docs/evidence/spec-readability-reconciliation-2026-10-02/README.md`)
     needs no edit: its figures are dated in place and name `census.json` as
     the current population.
   - **By hand, in the same commit:** add the profile recorder's check to the
     status battery, the hosted workflow and the count sentence together
     (CG-26), with the owner's selection text from the record:
     `python3 scripts/record_narrative_profile_adoption.py --check --date <date> --question-opening '<opening>' --selection-label '<label>' --selection-description '<description>'`.
     It re-verifies the record against the owner's selection; the
     reconciliation's R2 independently requires the installed specification
     and the confirming review's head to carry the recorder's digest.
11. **Verify.** `python3 scripts/check_governance.py && python3 scripts/check_docs_review_campaign_partition.py && python3 scripts/check_spec_reconciliation.py --check && python3 scripts/build_polaris_dependency_unions.py --check && npx vitest run`

Row 8 (a second egress version) is not generatable before row 7 is performed
and is out of this rehearsal.

After the sitting the order is: the recorders, then
`install_redis_sitting.py`, then `poc:dossier`. Pending: the `poc:dossier`
wiring PR will carry a map from each egress record digest to the stages it
authorises (an unknown digest authorises none); the install must then check
that the map's digests equal the recorded act arguments. That check does not
exist yet and the rehearsal does not cover it [Unknown until the PR lands]. Rows 10 and 11 are rulings and directions with
no bytes.

## Merge conflicts and install-change findings

Status is as of the last full run above. "Fixed" means a merged or open pull
request or the installer answers it; the finding is kept so a reader can see why.

| # | Where | What happens | Status |
|---|---|---|---|
| F1 | PENDING-OWNER-DECISIONS.md, every branch | Each branch appends a row; merges conflict pairwise | Open, mechanical: `git merge-file --union` over real temp files, then assert the row set is the distinct union |
| F2 | scripts/check_governance.py, PR 273 with others | Two packages each register a phrase or copy in the same region | Open, mechanical: keep both. `--union` is unsafe for Python; the simulator uses an ast-validated candidate search |
| F3 | PR 215 recorder, rows 4 to 6 | `live_inputs` passed the absolute package path to the builder | Fixed (PR 284, merged) |
| F4 | Row 1 install | The new policy argument leaves six CG-7e findings; the re-pin builder and recorder `--check` fail | Fixed by the installer's policy step; the two failing battery lines leave the status page and the workflow, as PR 266's ledger says |
| F5 | Rows 2 to 6 | Each performed record is an unregistered act-copy file and quotes `manifest SHA-256:` | Fixed by the installer's registrations step |
| F6 | Row 7 install | The RFC-0005 patch fails CG-7a and CG-7h until the manifest row is refreshed and a chain link exists | Fixed by the installer's rfc5 step: the PR 257 act's argument is the manifest row, not the file, so the link is a row-argument link, ordered by the record's `Act instant:` line |
| F7 | Rows 2 (route B) and 9 | No recorder | Fixed: `record_messages_api_route_registry_act.py` and `record_narrative_profile_adoption.py`. The versioned-signoff recorder does not apply to the profile: it covers the six PWB packages only and its package-builder contract is unmet (packet O3) |
| F8 | Row 9 install | `count_polaris_effective_scenarios.py` stopped at a third polaris-generation spec | Fixed (PR 288, merged) |
| F9 | PR 120 | Based on a stale main; conflicts in docs/README.md, the partition checker and check_governance.py | Open, not ours: rebase onto main before the sitting |
| F10 | Row 1 install, Vitest | Tests that pin the policy fail after the bytes change: content-classification, git-object-reader, governance-inputs, and also project-shape-model (PR 266's ledger lists the last as passing; corrected 2026-10-03: it asserts the version at two lines, 435 and 592, so it passes at the act alone and fails after the re-pin) | Fixed by the installer's policy step, which also moves the loader test's evaluation instant to the act date |
| F11 | Row 9 install | Moving the spec leaves four package files naming the old proposed/ path (CG-1b) | Fixed by the installer's profile step |
| F12 | Row 7 | The PR 257 recorder wrote no act instant, so the chain link could not be ordered | Fixed (PR 290, merged) |
| F13 | PR 278 with main | The merge is textually clean, but main's repo-corpus.ts types an excluded row's reason as a string while PR 278 closes the type, so `npm run build:poc` fails (TS2322) and two Vitest files fail with it | Open, PR 278's: type the helper parameter `GenerationExclusionReason`. The simulator applies the same one-line change in the scratch |
| F14 | PR 273 builder | `manifest_text` writes the root it is handed into the manifest rows, so a recorder passing an absolute root sees every manifest as stale | Worked around in the route-B recorder, which runs the builder from the root with relative paths; the builder is unchanged |
| F15 | tuple-encoding.test.ts | One case times out at 5000 ms on main by itself | Open, bead syzygy-8wux; the simulator reports it without counting it |
| F16 | Vitest under load | Cases that run near the 5000 ms timeout (polaris-narrative, parity sweep, proposal disclosure, tuple-encoding) fail in the full suite on a loaded machine (load average above 60 observed) and pass alone | The simulator reruns each failing file alone and counts only failures that persist; a pass on rerun is reported, not hidden |

## Known limits of the rehearsal

- [Unknown] Whether the real recorders accept the owner's actual selection:
  the rehearsal feeds a synthetic one.
- [Observed] The route-B package has no confirming review yet, so the rehearsal
  gives the scratch a synthetic confirming raw and a synthetic freeze. It
  proves the recorder's logic, not that the package is confirmed.
- [Observed] The installer's policy step takes the act date, identity, tag and
  version from the performed record and the policy file, and the owner's
  selection text for the status battery line from the record. It refuses, and
  restores the tree, if that text contains `: `, ` #` or a single quote,
  because the battery splitter and a plain workflow line cannot carry them.
- [Observed] The rehearsal does not exercise rows 8, 10 and 11 or any provider
  call; it reads no external repository.
- [Observed] `--route a` (without `--vitest`) also ended green: 31 OK / 0
  FAIL and the partition passing. Its Vitest result is not separately
  observed; the policy step is the same code for both routes.
