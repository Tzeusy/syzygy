# Impact ledger — public-source screening scope

> **Candidate — binds nothing.** Sweeps run 2026-10-03 on a clean tree at
> origin/main `c540438d`.

## Sweep 1 — files that name the policy

Predicate: Python `re.search(r"POLARIS-BUTLERS-SECRET-CLASSIFICATION-POLICY-CANDIDATE", text)`
over every path of `git ls-files -z` (1975 files). Result: 52 files. Of them 14
are code or scripts: `governance-inputs.ts`, `test-walkthrough-judgment-fixture.ts`,
`walkthrough-inputs.ts` (apps); `body-read-authority.test.ts`,
`content-classification.ts` and its test, `git-object-reader.test.ts`,
`project-shape-manifest.test.ts`, `walkthrough-judgment.test.ts` (packages);
`build_pwb_behavior_contract_repin.py`, `build_pwb_effect_acts_packet.py`,
`build_pwb_truth_policy_amendment.py`, `check_governance.py`,
`check_spec_reconciliation.py` (scripts). The other 38 are governance prose,
reviews and records, which cite it and bind nothing here.

## Sweep 2 — readers of policy keys

Predicate: files under `apps/` and `packages/` matching
`policyVersion|accessBoundary|sourceAdmission|rawBodyHandling`: 15 files.
[Observed] `body-read-authority.ts` and `governance-inputs.ts` check a policy
field at run time (`policyOwningProject`, `policyVersion`), and so does a
hard-coded copy of the version in `git-object-reader.ts`, which feeds
`PWB_SECRET_POLICY` in `content-classification.ts`, whose version every
exclusion record names. The rest read the keys in tests or fixtures; round 1
found the earlier sentence that only two files check a field to be false. [Inferred] No code rejects an additional
top-level key, because both read named fields; this is not proven by a
mutation of the file.

## Pins that carry the policy version or digest

Re-derived at the drafting base with the version literal and the act-record
path. Every one needs re-pointing in the same change as the act:

| Pin | Where | Kind |
|---|---|---|
| Expected `policyVersion` and the act-record path | `governance-inputs.ts` (policy expectations near :81, act record path near :58) | run time |
| The act's `scopeAnchors` (policy id, version, project) | `governance-inputs.ts` near :102 | run time |
| `PWB_POLICY_IDENTITY.policyVersion` | `git-object-reader.ts:43` | run time |
| `PWB_SECRET_POLICY.policyVersion`, taken from that identity | `content-classification.ts:69` | run time, follows the line above |
| Literal and equality assertions | `git-object-reader.test.ts:547`, `content-classification.test.ts` (255, 286, 406, 474, 488, 550), `governance-inputs.test.ts:311`, `project-shape-model.test.ts` (435, 592) | tests |

Predicate: the literal `1.1.0-candidate.1` over `git ls-files` under `apps/`,
`packages/` and `scripts/` (8 files). Three recorders and one builder in
`scripts/` also carry it; they restate performed history and are not pins to
re-point.

The digest in the act record is the first refusal (`exact-digest-wrong`,
`body-read-authority.ts:444`); the version pins fail next.

## Consequences

1. The read gate: any byte change is refused (`exact-digest-wrong`) before the
   version is compared. Re-pointing means every pin in the table above plus the
   act record, in one change with its tests.
2. Butlers behaviour is unchanged: no base key and no Butlers `scope` value
   moves (builder predicate "a base key altered").
3. No code consumes `publicSourceScope` yet; the any-repo reader and the
   public screening implementation (gap 6) are separate work that this scope
   authorizes but does not perform.
4. The sibling policy package (PR #120) touches the same file: see the delta.
