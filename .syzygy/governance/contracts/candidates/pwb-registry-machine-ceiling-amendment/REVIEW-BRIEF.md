# Review brief — P-114, the Butlers machine-answer ceiling to 16 MiB

> **Candidate — binds nothing.** This brief says what an independent
> reviewer is given and what they decide. It is not a review and carries no
> verdict. **Round 1.**

## What the reviewer is given, and nothing else

**The artifact**: the package directory
`.syzygy/governance/contracts/candidates/pwb-registry-machine-ceiling-amendment/`.
That is `SEMANTIC-DELTA.md`, `IMPACT-LEDGER.md`, `OWNER-DECISION-PACKET.md`,
this brief, `PWB-REGISTRY-MACHINE-CEILING-AMENDMENT-MANIFEST.txt` and
`proposed/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json.patch`. Add
to it `scripts/build_pwb_registry_machine_ceiling_amendment.py` and the
evidence record `docs/evidence/syzygy-59s5-live-size-2026-10-20.json`.

**The subject**:
`.syzygy/governance/declarations/adapter-registry/POLARIS-BUTLERS-PROJECT-SHAPE-OBSERVER-CANDIDATE.json`
at its current bytes.

**Governing references**:

- `.syzygy/governance/decisions/OWNER-DIRECTION-MACHINE-CEILING-2026-10-15.md`
  (the direction this drafts under);
- `.syzygy/governance/decisions/OWNER-DIRECTION-VERSIONED-SIGNOFF-SCOPE-A-2026-10-02.md`;
- `.syzygy/governance/decisions/PWB-OBSERVER-REGISTRY-BEHAVIOR-CONTRACT-REPIN-ACT.md`
  (act B, the act the gate follows today);
- PWB-REQ-005 and PWB-REQ-006 in
  `openspec/changes/polaris-project-wide-butlers-model/specs/polaris-project-wide-butlers-model/spec.md`,
  and that change's `design.md` §6 "Values recommended at drafting";
- `packages/three-surface-poc-core/src/project-shape-observation.ts`,
  `apps/three-surface-poc/src/governance-inputs.ts`,
  `apps/three-surface-poc/src/routes.ts`,
  `packages/three-surface-poc-core/src/body-read-authority.ts`;
- `.syzygy/governance/decisions/OWNER-DIRECTION-IMPLEMENTATION-SIGNED-AMENDMENTS-2026-10-15.md`
  (to test the claim that it does not cover this entry);
- `.syzygy/governance/contracts/candidates/policy-candidates/NORMATIVE-CHANGE-WORKFLOW.md`
  and `SEMANTIC-DELTA-TEMPLATE.md`.

**Not given**: no Butlers repository content. Do not read or fetch anything
outside this Syzygy checkout. You may run, from the repository root,
`python3 scripts/build_pwb_registry_machine_ceiling_amendment.py --check`,
`--selftest`, `--digests` and `--manifest-digest`, plus any read-only sweep
over this checkout. Do not start a daemon.

## What the reviewer decides

1. **One value.** Does the patch change exactly
   `entries[0].resourceLimits.maxMachineResponseBytes` from 8388608 to
   16777216 and no other byte? Re-derive this yourself; do not take the
   builder's word.
2. **Honest basis.** Do the delta's claims match the evidence record and the
   code: the measurement, the growth attribution, the 16 MiB rationale? Is
   each one labelled Observed, Inferred or Unknown correctly? Is any claim
   stronger than its evidence?
3. **The impact ledger is complete.** Find any place that hard-codes the
   value, or reads the entry's bytes, that part A or B misses. The ledger
   states its method and denominators; check them (rules 2, 4 and 9).
4. **The two asks are the right split.** Is ask 2 necessary, and is it
   narrow enough? Is the "sign without authorize" arm safe (nothing is
   recorded)? Does any ask exceed the owner's direction?
5. **Versions.** Is keeping `1.2.0-candidate.1` defensible, or should the
   entry's versions move?
6. **The builder.** Does each `--selftest` mutant fail for the predicate it
   names (rule 6)? Does `--check` fail closed on a sibling's edit to the
   subject?

## Head contract (quoted from the builder's docstring)

> Review-head contract: the raw's first four non-blank lines carry
> `Reviewed commit: <40 hex>`, `Manifest SHA-256: <SHA-256 of the manifest
> FILE, as --manifest-digest prints it>` and a `Verdict:` line (`CONFIRM`,
> `CONFIRM WITH EXCEPTIONS` or `REVISE`); findings are numbered
> `**Finding N — title** (blocking|revise|note)`.

Put the findings under one `## Findings` heading. The first line of the raw
is its title, then the three head lines, with no blank line between them.
