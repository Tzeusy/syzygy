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
field at run time (`policyOwningProject`, `policyVersion`), and a
hard-coded copy of the version in `git-object-reader.ts` carries it too, which feeds
`PWB_SECRET_POLICY` in `content-classification.ts`, whose version every
exclusion record names. The rest read the keys in tests or fixtures; round 1
found the earlier sentence that only two files check a field to be false. [Inferred] No code rejects an additional
top-level key, because both read named fields; this is not proven by a
mutation of the file.

## What the act breaks, by simulation

Derived mechanically, not by reading: `python3
scripts/simulate_public_source_screening_scope_act.py --tests` clones the
committed tree to a scratch directory, replaces the policy with the proposed
bytes, commits them, runs the checks below and sweeps the clone for the
literals the old policy and the performed act carry (the policy's SHA-256, its
version, the act identity and recording tag, the two act-record pointers). It
edits nothing in this checkout. Output of the run for this round:

| Check run in the clone | Result |
|---|---|
| `build_pwb_behavior_contract_repin.py --check` | fails: the tree with the patch reversed no longer hashes to the re-pin argument |
| `record_pwb_behavior_contract_repin_acts.py --check policy` | fails: the policy hashes to another value than the owner argument |
| `check_governance.py` | fails CG-7e with 6 findings (the re-pin manifest and the act record no longer carry the policy's current argument; the screening package's own manifest row is a recognized argument of a superseded act) |
| Vitest `governance-inputs.test.ts` | 3 tests fail: the policy digest the act binds, the superseded-record check and the later-amendment check |
| Vitest `content-classification.test.ts` | fails: `PWB_SECRET_POLICY.policyVersion` is the old version |
| Vitest `git-object-reader.test.ts` | fails: the policy-bound constants differ from the act-bound artifact |
| Vitest `project-shape-model.test.ts` | passes: its version literals are fixtures, not pins |

Literal sweep of the clone, files under `apps/`, `packages/`, `scripts/`,
`.github/` and `PROJECT-STATUS.md` (the sweep also finds 61 governance records
that cite the old bytes, six of which are this package's own candidate files
and bind nothing; the other 55 bind and are not edited. Predicate: a tracked,
strictly UTF-8 file of the scratch clone with the proposed bytes committed,
outside `apps/`, `packages/`, `scripts/`, `.github/` and `PROJECT-STATUS.md`,
with a `str.count` above zero of the old policy file's SHA-256 or of
`1.1.0-candidate.1`. The five are the ledger, the semantic delta, the patch and
the round-1, round-2 and round-3 raws; each retained raw adds one, so the figure moves
with the package and must be re-derived):

| Pin | Where | Kind |
|---|---|---|
| Expected `policyVersion` and `scopeAnchors` | `governance-inputs.ts` (2 hits) | run time |
| Act identity, recording tag, act-record pointer and the superseded-record pointer of the policy act | `governance-inputs.ts` (policy entry of the act table and `PWB_SUPERSEDED_ACT_RECORDS`) | run time |
| `PWB_POLICY_IDENTITY.policyVersion` | `git-object-reader.ts` (1 hit); `content-classification.ts` takes its version from it | run time |
| The same identity, tag and version, asserted | `governance-inputs.test.ts`, `content-classification.test.ts` (5), `git-object-reader.test.ts` | tests |
| The re-pin builder's `--check` line (no digest literal) and the re-pin act's `--check policy` line with the policy digest | `PROJECT-STATUS.md` battery (builder line: 0 literal hits, fails with the tree; recorder line: 1 hit) | status page |
| The same two CI steps (`build_pwb_behavior_contract_repin.py --check`, `record_pwb_behavior_contract_repin_acts.py --check policy`) | `.github/workflows/governance-docs.yml` (digest, 1 hit) | workflow |
| Act-subject chain and `ACT_DIGEST_COPY_FILES` rows for the policy act | `check_governance.py` (the CG-7e findings above) | governance tooling |
| Version literal restated as performed history | `record_pwb_behavior_contract_repin_acts.py`, `record_pwb_effect_amendment_acts.py` | not pins: superseded recorders fail `--check` by design |
| `CURRENT_VERSION` | `build_pwb_registry_currency_briefing_amendment.py` | not a pin: it is the registry entry's version, not the policy's |

Version-literal predicate: the literal `1.1.0-candidate.1` over `git ls-files`
under `apps/`, `packages/` and `scripts/`: 8 files (5 under `apps/` and
`packages/`, 3 under `scripts/`: two recorders and one builder).

The digest in the act record is the first refusal (`exact-digest-wrong`,
`body-read-authority.ts:444`); the version pins fail next.

## Consequences

1. The read gate: any byte change is refused (`exact-digest-wrong`) before the
   version is compared. Re-pointing means every pin in the tables above plus the
   act record, the status battery lines, the workflow steps and the
   act-subject chain, in one change with its tests.
2. Butlers behaviour is unchanged: no base key and no Butlers `scope` value
   moves (builder predicate "a base key altered").
3. No code consumes `publicSourceScope` yet; the any-repo reader and the
   public screening implementation (gap 6) are separate work that this scope
   authorizes but does not perform.
4. The sibling policy package (PR #120) touches the same file: see the delta.
