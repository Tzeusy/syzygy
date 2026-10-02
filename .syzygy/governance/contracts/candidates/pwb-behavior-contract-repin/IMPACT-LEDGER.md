# Impact ledger — PWB behaviour-contract re-pin

> **Candidate — binds nothing.** Drafted 2026-10-02 for bead `syzygy-jloi`.
> Every count below was produced by the stated command, run on a tree with
> 1,858 tracked files (`git ls-files | wc -l`), main at `efee1b2`, before
> this package's own files were added. Re-run before relying on a figure.

## Sweep 1 — who reads `governingBehaviorContract`

Command: `git grep -l -F governingBehaviorContract`, 18 files.

| Class | Files | Effect of the re-pin |
|---|---|---|
| The two subjects | 2 | Changed by their own acts only |
| `scripts/check_spec_reconciliation.py` (R6) | 1 | Reads the pins. R6 goes from 2 findings to 0 after both acts. Its selftest gains the strict case `pins-after-repin-acts` |
| `docs/evidence/spec-readability-reconciliation-2026-10-02/README.md` | 1 | Describes R6 as found on 2026-10-02. It is a dated record and is not edited |
| Candidate package prose that discloses the stale pin (`pwb-opening-band-scenario` IMPACT-LEDGER and SEMANTIC-DELTA, `pwb-exact-source-render-mode-scenario` IMPACT-LEDGER and SEMANTIC-DELTA, `pwb-missing-currency-disclosure-scenario` IMPACT-LEDGER, `pwb-container-shape-profile-amendment` IMPACT-LEDGER) | 6 | Performed packages' disclosures, which are history. Not edited |
| Retained review raws under `docs/reviews/` | 8 | CC-REV-6, unchangeable |

[Observed] `git grep -n -F governingBehaviorContract -- packages apps`
returns 0 lines. No implementation code reads the field.

## Sweep 2 — who reads either subject's bytes

Commands: `git grep -l -F <basename> -- '*.ts' '*.py' '*.yml' '*.json'`
for each basename. The registry entry has 21 matching files and the policy
16. The populations overlap, and the evidence and pursuit JSON files (10
registry, 3 policy) only name the paths. Implementation and tooling
readers:

| Reader | Reads | After the act |
|---|---|---|
| `apps/three-surface-poc/src/governance-inputs.ts` (body-read gate loader) | Both artifacts' bytes and the act records `PWB_ACT_RECORDS` names | **Fails closed for the acted role.** See "Read gate" below |
| `apps/three-surface-poc/src/governance-inputs.test.ts`, real-tree case | Requires each act record to carry `Exact digest (SHA-256)` equal to the live artifact | **Fails** until the gate is re-pointed |
| `content-classification.ts` and its test, `git-object-reader.test.ts`, `project-shape-manifest.test.ts`, `project-shape-observation.test.ts` | Detector, admission, version, discovery and limit fields | Unchanged, because those fields do not move |
| `walkthrough-inputs.ts`, `test-walkthrough-judgment-fixture.ts`, `walkthrough-judgment.test.ts`, `body-read-authority.test.ts` | Paths only, or synthetic fixtures | Unchanged |
| `scripts/check_governance.py` CG-7e | Act-argument copies | Needs new chain rows at the act (owner packet, step 4). A rehearsal on a scratch tree with both patches applied and no rows added gave 12 CG-7e findings |
| `scripts/build_pwb_truth_policy_amendment.py --check` | Policy row of the 2026-09-05 effect manifest | Fails unless the row is marked superseded by the new policy record |
| `scripts/build_pwb_registry_currency_briefing_amendment.py --check` | Requires the registry to equal its 2026-09-30 proposed bytes | Fails unless a later superseding act is recognized |
| `scripts/record_pwb_registry_currency_amendment.py --check` (battery line) | Requires the registry to hash to its 2026-09-30 argument | Fails by design, as a superseded recorder does. The line leaves the battery or learns the supersession |
| `scripts/check_polaris_response_ceiling_reading.py` | Registry ceiling sentences | Unchanged. The rehearsal printed `OK` |
| `scripts/build_pwb_effect_acts_packet.py` | 2026-09-02 packet | Already outside the battery (fails by design since 2026-09-05) |

The rehearsal was run on 2026-10-02: both patches applied with `--apply both
--at-adoption` and two placeholder records, then restored with `git
checkout`. Rows 5–9 come from that run. Row 2 is [Inferred] from reading
the test, which was not run against the rehearsal.

## Read gate

[Observed] `PWB_ACT_RECORDS` names
`decisions/PWB-SECRET-CLASSIFICATION-POLICY-AMENDMENT-ACT.md` (policy) and
`decisions/PWB-OBSERVER-REGISTRY-CURRENCY-BRIEFING-AMENDMENT-ACT.md`
(registry). Once either subject carries its new bytes:

1. that role's record binds a digest the artifact no longer hashes to,
   giving `exact-digest-wrong` (`body-read-authority.ts`); and
2. the new record names the old one as superseded, so the loader's
   lifecycle scan marks it superseded.

PWB-REQ-005 requires all three authorities, so the evaluation stops
admitting and every Butlers body read is refused. Polaris then renders the
shape Unknown. This is the 2026-09-30 failure the owner instructions record
describes, now for two roles. The owner packet names the continuation
direction that ends it.

## Not affected

- Observation consent and its act.
- The PWB specification (eleven artifacts), its signed packages and tags.
- Every version label in both files (see the semantic delta).
- Doctrine, accepted contracts, policies other than the one subject, and
  every act already performed. No record is edited.
