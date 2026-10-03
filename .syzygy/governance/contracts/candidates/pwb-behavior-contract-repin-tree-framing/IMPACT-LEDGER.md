# Impact ledger — PWB behaviour-contract re-pin (tree framing)

> **Candidate — binds nothing.** Drafted 2026-10-03 for bead `syzygy-2g0d`.
> Every count below was produced by the stated command, run on a tree with
> 1,973 tracked files (`git ls-files | wc -l`), main at `dbf8ed1`, before
> this package's own files were added. Re-run before relying on a figure.

## Sweep 1 — who reads `governingBehaviorContract`

Command: `git grep -l -F governingBehaviorContract`, 32 files.

| Class | Files | Effect of the re-pin |
|---|---|---|
| The two subjects | 2 | Changed by their own acts only |
| `scripts/check_spec_reconciliation.py` (R6) | 1 | Reads the pins. R6 goes from 2 findings to 0 after both acts. Its selftest gains the strict case `pins-after-tree-framing-repin-acts`, and R6 findings now name `syzygy-2g0d` |
| `scripts/build_pwb_behavior_contract_repin.py` and `scripts/record_pwb_behavior_contract_repin_acts.py` | 2 | The 2026-10-02 package's builder and recorder. Both read the subjects as the bytes their acts bound, so both fail after these acts until they learn the supersession (owner packet, "At adoption", step 3) |
| `apps/three-surface-poc/src/governance-inputs.ts` | 1 | One comment line saying nothing there reads the field |
| `PROJECT-STATUS.md` | 1 | Prose about the 2026-10-02 re-pin and R6. Gains this package's open-gate row |
| The 2026-10-02 package (`pwb-behavior-contract-repin/`: four prose files and two patches) | 6 | A performed package; history. Not edited |
| The 2026-10-02 act records and direction (`decisions/`) | 3 | Performed records; immutable |
| Earlier candidate package prose that discloses a stale pin (`pwb-opening-band-scenario` IMPACT-LEDGER and SEMANTIC-DELTA, `pwb-exact-source-render-mode-scenario` IMPACT-LEDGER and SEMANTIC-DELTA, `pwb-missing-currency-disclosure-scenario` IMPACT-LEDGER, `pwb-container-shape-profile-amendment` IMPACT-LEDGER) | 6 | Performed packages' disclosures, which are history. Not edited |
| `docs/evidence/spec-readability-reconciliation-2026-10-02/README.md` | 1 | Dated record of R6; not edited |
| Retained review raws under `docs/reviews/` | 9 | CC-REV-6, unchangeable |

The rows sum to 32. [Observed] `git grep -n -F governingBehaviorContract --
packages apps` returns 1 line, the comment above. No implementation code
reads the field.

## Sweep 2 — who reads either subject's bytes

Commands: `git grep -l -F <basename> -- '*.ts' '*.py' '*.yml' '*.json'`
for each basename. The registry entry has 26 matching files and the policy
20. The populations overlap; the evidence and pursuit JSON files (14
registry, 6 policy) only name the paths. Implementation and tooling
readers, with the rehearsal result where one was run:

| Reader | Reads | After both acts |
|---|---|---|
| `apps/three-surface-poc/src/governance-inputs.ts` (body-read gate loader) | Both artifacts' bytes and the act records `PWB_ACT_RECORDS` names | **Fails closed for each acted role.** See "Read gate" below |
| `apps/three-surface-poc/src/governance-inputs.test.ts`, real-tree case | Requires each act record to carry `Exact digest (SHA-256)` equal to the live artifact | [Inferred] **Fails** until the gate is re-pointed; read from the test, not run against the rehearsal |
| `content-classification.ts` and its test, `git-object-reader.test.ts`, `project-shape-manifest.test.ts`, `project-shape-observation.test.ts` | Detector, admission, version, discovery and limit fields | Unchanged, because those fields do not move |
| `walkthrough-inputs.ts`, `test-walkthrough-judgment-fixture.ts`, `walkthrough-judgment.test.ts`, `body-read-authority.test.ts` | Paths only, or synthetic fixtures | Unchanged |
| `scripts/check_governance.py` CG-7e | Act-argument copies | Rehearsal: **11 findings**, all from the act change not yet made: the new arguments sit in this manifest unregistered, while the 2026-10-02 manifest and records, the aggregate record and `PROJECT-STATUS.md` are still registered as current copies |
| `scripts/build_pwb_behavior_contract_repin.py --check` and `--selftest` | Requires the subjects to reverse its patches to the 2026-10-02 predecessors | Rehearsal: **both fail** (its patches no longer reverse-apply) |
| `scripts/record_pwb_behavior_contract_repin_acts.py --check policy` and `--check registry` | Require each subject to hash to its 2026-10-02 argument | Rehearsal: **both fail**, as a superseded recorder does by design. The lines leave the battery or learn the supersession. `--selftest` passes |
| `scripts/build_pwb_registry_currency_briefing_amendment.py --check` and `--selftest`; `scripts/record_pwb_registry_currency_amendment.py --check` | Read the registry as its 2026-09-30 bytes by reversing the 2026-10-02 re-pin patch | Rehearsal: **all three fail**: that reversal no longer applies over the new bytes. The recorder's `--selftest` passes |
| `scripts/check_spec_reconciliation.py --check` | R6 pins | Rehearsal: R1–R7 all OK, **R6 0 findings** |
| `scripts/check_spec_reconciliation.py --selftest` | The `pins-after-repin-acts` case drives the 2026-10-02 builder | Rehearsal: **fails** inside that builder, for the reason above |
| `scripts/build_pwb_truth_policy_amendment.py --check` | Policy row of the 2026-09-05 effect manifest, already history since 2026-10-02 | Rehearsal: passes |
| `scripts/check_polaris_response_ceiling_reading.py --check` | Registry ceiling sentences | Rehearsal: `OK` |
| `scripts/build_pwb_effect_acts_packet.py` | 2026-09-02 packet | Already outside the battery (fails by design since 2026-09-05) |

The rehearsal was run on 2026-10-03 in a scratch clone of this branch:
`--apply both --at-adoption`, two placeholder records at the offered record
paths, then each listed command; the clone was discarded. Every failure it
shows is the act change's work, listed in the owner packet, and is the same
class the 2026-10-02 act change handled for its predecessors.

## Read gate

[Observed] `PWB_ACT_RECORDS` names
`decisions/PWB-SECRET-CLASSIFICATION-POLICY-BEHAVIOR-CONTRACT-REPIN-ACT.md`
(policy) and
`decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md`
(registry). Once either subject carries its new bytes:

1. that role's record binds a digest the artifact no longer hashes to,
   giving `exact-digest-wrong` (`body-read-authority.ts`); and
2. the new record names the old one as superseded, so the loader's
   lifecycle scan marks it superseded.

PWB-REQ-005 requires all three authorities, so the evaluation stops
admitting and every Butlers body read is refused. Polaris then renders the
shape Unknown. This is the failure the 2026-09-30 and 2026-10-02 owner
instructions records describe, again for two roles. The owner packet names
the continuation direction that ends it.

## Not affected

- Observation consent and its act.
- The PWB specification (eleven artifacts), its signed packages and tags.
- Every version label in both files (see the semantic delta).
- Doctrine, accepted contracts, policies other than the one subject, and
  every act already performed. No record is edited.
