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
[Observed] Only `body-read-authority.ts` and `governance-inputs.ts` check a
policy field at run time (`policyOwningProject`, `policyVersion`); the rest read
the keys in tests or fixtures. [Inferred] No code rejects an additional
top-level key, because both read named fields; this is not proven by a
mutation of the file.

## Consequences

1. The version check: `body-read-authority.ts` compares `policyVersion` with
   the pinned expectation. A bumped version is refused until
   `governance-inputs.ts` and the act-record path it names are re-pointed.
2. Butlers behaviour is unchanged: no base key and no Butlers `scope` value
   moves (builder predicate "a base key altered").
3. No code consumes `publicSourceScope` yet; the any-repo reader and the
   public screening implementation (gap 6) are separate work that this scope
   authorizes but does not perform.
4. The sibling policy package (PR #120) touches the same file: see the delta.
